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


def _session():
    _check_config()
    s = requests.Session()
    s.auth = (USERNAME, APP_PASSWORD)
    s.headers.update({"Accept": "application/json"})
    adapter = HTTPAdapter(max_retries=RETRY_STRATEGY)
    s.mount("https://", adapter)
    s.mount("http://", adapter)
    return s


def get(endpoint, **params):
    """GET paginé sur /wp-json/wp/v2/<endpoint>, retourne la liste complète des items."""
    s = _session()
    items = []
    page = 1
    while True:
        resp = s.get(
            f"{API_BASE}/{endpoint}",
            params={**params, "page": page, "per_page": params.get("per_page", 50)},
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


def list_untagged_posts(max_posts, skip_ids=frozenset(), max_scan=2000):
    """Scanne les articles du plus récent au plus ancien et s'arrête dès que
    `max_posts` articles sans tag (ou 1 seul) ont été trouvés.

    Le site a des milliers d'articles : on ne veut pas paginer tout le catalogue
    pour construire un petit lot, donc on s'arrête tôt. `max_scan` est un
    garde-fou si peu d'articles récents sont sans tag (site déjà bien tagué).
    """
    s = _session()
    found = []
    scanned = 0
    page = 1
    per_page = 100
    while len(found) < max_posts and scanned < max_scan:
        resp = s.get(
            f"{API_BASE}/posts",
            params={
                "status": "publish",
                "_fields": "id,title,categories,tags",
                "orderby": "date",
                "order": "desc",
                "per_page": per_page,
                "page": page,
            },
            timeout=30,
        )
        if resp.status_code == 400:
            break  # plus de pages
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        scanned += len(batch)
        for p in batch:
            if len(p.get("tags", [])) <= 1 and p["id"] not in skip_ids:
                found.append(p)
                if len(found) >= max_posts:
                    break
        page += 1
    return found


def get_post_content(post_id):
    """Contenu HTML brut (rendu) d'un article, pour extraction texte côté fetch_batch."""
    s = _session()
    resp = s.get(f"{API_BASE}/posts/{post_id}", params={"_fields": "content"}, timeout=30)
    resp.raise_for_status()
    return resp.json()["content"]["rendered"]


def create_tag(name):
    return post("tags", {"name": name})["id"]


def delete_tag(tag_id):
    """Supprime définitivement un tag (le retire de tous les articles qui l'utilisent)."""
    s = _session()
    resp = s.delete(f"{API_BASE}/tags/{tag_id}", params={"force": "true"}, timeout=30)
    resp.raise_for_status()
    return resp.json()


def update_post_tags(post_id, tag_ids):
    return post(f"posts/{post_id}", {"tags": tag_ids})