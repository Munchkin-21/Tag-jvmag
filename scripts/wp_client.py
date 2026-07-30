"""Client REST API WordPress (auth par Application Password)."""
import os

import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

load_dotenv()

SITE_URL = os.environ.get("WP_SITE_URL", "").rstrip("/")
USERNAME = os.environ.get("WP_USERNAME", "")
APP_PASSWORD = os.environ.get("WP_APP_PASSWORD", "")

API_BASE = f"{SITE_URL}/wp-json/wp/v2"

# Retry réseau : 1 appel + 3 tentatives, backoff exponentiel (1s, 2s, 4s, 8s).
# Couvre les erreurs de connexion/timeout (perdues avant que WordPress ait
# traité la requête) et les statuts serveur transitoires (429 rate limit,
# 500/502/503/504). GET et POST sont tous deux concernés : `update_post_tags`
# est naturellement idempotent (fusion par set, voir apply_batch.py) donc un
# rejeu ne crée jamais de doublon ; `create_tag` est protégé côté WordPress,
# qui refuse la création d'un terme portant un nom déjà existant — le pire cas
# d'un retry après succès silencieux est un échec propre, pas une duplication.
# NB : `allowed_methods` est le nom du paramètre depuis urllib3 >= 1.26
# (`method_whitelist` avant, supprimé en 2.0) — vérifier la version installée
# si ce fichier est repris sur un environnement différent.
RETRY_STRATEGY = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET", "POST"],
    raise_on_status=False,
)


def _check_config():
    missing = [
        name
        for name, val in [
            ("WP_SITE_URL", SITE_URL),
            ("WP_USERNAME", USERNAME),
            ("WP_APP_PASSWORD", APP_PASSWORD),
        ]
        if not val
    ]
    if missing:
        raise RuntimeError(
            f"Variables manquantes dans .env : {', '.join(missing)}. "
            "Copie .env.example vers .env et remplis-le."
        )


_SESSION = None


def _session():
    """Session HTTP unique, réutilisée par tous les appels du processus.

    Une `requests.Session` maintient un pool de connexions avec keep-alive : la poignée
    de main TCP puis la négociation TLS n'ont lieu qu'une fois, les requêtes suivantes
    réutilisent la connexion ouverte. En recréant une session à chaque appel, chaque
    requête repayait ces deux étapes — mesuré à ~64 ms de surcoût par requête, soit
    ~2,8 s par lot de 20 articles (45 sessions créées là qu'une seule est nécessaire).

    Les scripts sont mono-thread, donc pas de précaution particulière à prendre ici :
    `requests.Session` n'est pas garantie thread-safe et ce cache ne conviendrait pas
    tel quel à un usage concurrent.
    """
    global _SESSION
    if _SESSION is None:
        _check_config()
        s = requests.Session()
        s.auth = (USERNAME, APP_PASSWORD)
        s.headers.update({"Accept": "application/json"})
        adapter = HTTPAdapter(max_retries=RETRY_STRATEGY)
        s.mount("https://", adapter)
        s.mount("http://", adapter)
        _SESSION = s
    return _SESSION


def get(endpoint, **params):
    """GET paginé sur /wp-json/wp/v2/<endpoint>, retourne la liste complète des items.

    `per_page` par défaut à 100, le maximum autorisé par WordPress : la liste des tags
    est relue à chaque lot par les deux scripts, autant la récupérer en deux fois moins
    de requêtes.

    Une valeur de type liste (ex. `include=[1, 2, 3]`, utilisé par `get_posts_by_ids`)
    est jointe en chaîne séparée par des virgules avant l'envoi. Sans ça, `requests`
    sérialise une liste en clé répétée (`include=1&include=2&include=3`) — et côté
    WordPress, PHP ($_GET) ne garde que la DERNIÈRE occurrence d'une clé répétée sans
    crochets : l'API ne voit alors qu'un seul ID au lieu de tous. C'est arrivé :
    `get_posts_by_ids()` sur 19 IDs ne retournait que le dernier de la liste, en
    silence (pas d'erreur, juste un résultat tronqué).
    """
    s = _session()
    params = {
        k: (",".join(str(v) for v in val) if isinstance(val, (list, tuple, set)) else val)
        for k, val in params.items()
    }
    items = []
    page = 1
    while True:
        resp = s.get(
            f"{API_BASE}/{endpoint}",
            params={**params, "page": page, "per_page": params.get("per_page", 100)},
            timeout=30,
        )
        if resp.status_code == 400 and page > 1:
            break  # WP renvoie 400 rest_post_invalid_page_number au-delà de la dernière page
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        items.extend(batch)
        total_pages = int(resp.headers.get("X-WP-TotalPages", "1"))
        if page >= total_pages:
            break
        page += 1
    return items


def post(endpoint, json_body):
    s = _session()
    resp = s.post(f"{API_BASE}/{endpoint}", json=json_body, timeout=30)
    resp.raise_for_status()
    return resp.json()


def list_categories():
    """Retourne {id: name}."""
    return {c["id"]: c["name"] for c in get("categories", _fields="id,name")}


def list_all_tags():
    """Retourne {name: id}, casse exacte (pas de normalisation) — la correspondance est
    volontairement stricte, voir la règle de nommage dans regles-tagging-actives.md."""
    tags = get("tags", _fields="id,name")
    return {t["name"]: t["id"] for t in tags}


def list_untagged_posts(max_posts, skip_ids=frozenset(), max_scan=2000, before=None):
    """Scanne les articles du plus récent au plus ancien et s'arrête dès que
    `max_posts` articles sans tag (ou 1 seul) ont été trouvés.

    `before` (date ISO 8601, ex. "2024-03-15T14:30:00") restreint le scan aux
    articles publiés strictement avant cette date. C'est le mécanisme de reprise :
    sans lui, chaque appel repart de l'article le plus récent et re-télécharge tout
    ce qui est déjà tagué avant d'atteindre du travail utile — au bout de `max_scan`
    articles déjà traités, le scan rendrait un lot vide alors que le catalogue est
    loin d'être fini. La comparaison porte sur le champ `date` (fuseau du site), pas
    `date_gmt` : c'est ce que compare le paramètre `before` de l'API WordPress.

    `max_scan` reste un garde-fou par exécution, pour qu'un seul appel ne parcoure
    pas tout le catalogue. L'atteindre n'est plus un problème : il suffit de relancer,
    le curseur ayant avancé.

    Retourne un dict :
      - `posts` : les articles trouvés
      - `last_scanned_date` : date du dernier article parcouru (None si aucun), à
        stocker comme curseur pour la reprise
      - `reached_end` : True si le catalogue a été parcouru jusqu'au bout (plus
        aucun article plus ancien), False si l'arrêt vient de `max_posts` ou `max_scan`
      - `scanned` : nombre d'articles parcourus
    """
    s = _session()
    found = []
    scanned = 0
    page = 1
    per_page = 100
    last_scanned_date = None
    reached_end = False

    while len(found) < max_posts and scanned < max_scan:
        params = {
            "status": "publish",
            # `date` est indispensable : c'est la valeur du curseur de reprise.
            "_fields": "id,title,categories,tags,date",
            "orderby": "date",
            "order": "desc",
            "per_page": per_page,
            "page": page,
        }
        if before:
            params["before"] = before

        resp = s.get(f"{API_BASE}/posts", params=params, timeout=30)
        if resp.status_code == 400:
            reached_end = True  # au-delà de la dernière page : plus rien à scanner
            break
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            reached_end = True
            break

        scanned += len(batch)
        stop = False
        for p in batch:
            last_scanned_date = p.get("date") or last_scanned_date
            if len(p.get("tags", [])) <= 1 and p["id"] not in skip_ids:
                found.append(p)
                if len(found) >= max_posts:
                    stop = True
                    break
        if stop:
            break
        if len(batch) < per_page:
            reached_end = True  # page incomplète = dernière page du catalogue
            break
        page += 1

    return {
        "posts": found,
        "last_scanned_date": last_scanned_date,
        "reached_end": reached_end,
        "scanned": scanned,
    }


def get_posts_by_ids(ids, fields="id,title,categories,tags,date"):
    """Récupère des articles par leurs IDs, quel que soit leur nombre de tags.

    Sert au re-tagging rétroactif : `list_untagged_posts` ne retourne que les articles
    à 0 ou 1 tag, donc un article déjà tagué lui est invisible. Ici on cible
    explicitement, sans filtre.

    Les IDs sont découpés en paquets de 100 (maximum `per_page` de WordPress). L'ordre
    de retour suit celui de WordPress (date décroissante), pas celui des IDs fournis.
    """
    ids = list(ids)
    out = []
    for start in range(0, len(ids), 100):
        chunk = ids[start:start + 100]
        out.extend(get("posts", include=chunk, _fields=fields, per_page=100))
    return out


def get_current_tags(post_ids):
    """Retourne {post_id: [tag_ids]} pour plusieurs articles en une seule requête par
    paquet de 100, au lieu d'une requête par article."""
    result = {}
    for post in get_posts_by_ids(post_ids, fields="id,tags"):
        result[post["id"]] = post.get("tags", [])
    return result


def get_post_content(post_id):
    """Contenu HTML brut (rendu) d'un article, pour extraction texte côté fetch_batch."""
    s = _session()
    resp = s.get(f"{API_BASE}/posts/{post_id}", params={"_fields": "content"}, timeout=30)
    resp.raise_for_status()
    return resp.json()["content"]["rendered"]


def create_tag(name):
    return post("tags", {"name": name})["id"]


def update_post_tags(post_id, tag_ids):
    return post(f"posts/{post_id}", {"tags": tag_ids})