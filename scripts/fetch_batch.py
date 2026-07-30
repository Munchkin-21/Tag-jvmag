"""Construit un lot d'articles sans tags à proposer pour tagging.

Usage:
    python scripts/fetch_batch.py --size 20      # reprend où le scan précédent s'est arrêté
    python scripts/fetch_batch.py --from-top     # repart des articles les plus récents

Écrit batches/batch_XXXX.json (XXXX = prochain numéro de lot disponible).

Deux modes de parcours du catalogue :

**Mode reprise (par défaut).** Le scan continue à partir de `scan_cursor` (dans
state.json), la date du dernier article parcouru lors de l'exécution précédente. Il
descend ainsi progressivement du plus récent vers le plus ancien, sans jamais
re-télécharger ce qui a déjà été parcouru. Sans ce curseur, chaque appel repartirait
de l'article le plus récent : une fois quelques milliers d'articles tagués, le scan
épuiserait son budget (`max_scan`) sur des articles déjà traités et rendrait des lots
vides alors que le catalogue est loin d'être fini.

**Mode `--from-top`.** Ignore le curseur et repart du plus récent, pour rattraper les
articles publiés depuis le début du chantier (ils sont plus récents que le curseur,
donc invisibles en mode reprise). Ce mode ne touche pas au curseur : la position dans
le backlog est préservée.
"""
import argparse
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

from bs4 import BeautifulSoup

import wp_client

ROOT = Path(__file__).resolve().parent.parent
BATCHES_DIR = ROOT / "batches"
STATE_PATH = Path(__file__).resolve().parent / "state.json"


def load_state():
    if STATE_PATH.exists():
        state = json.loads(STATE_PATH.read_text())
    else:
        state = {}
    state.setdefault("processed", [])
    state.setdefault("queued", [])
    state.setdefault("skipped", [])  # articles écartés (ex: encore en rédaction), à reconsidérer plus tard
    state.setdefault("scan_cursor", None)  # date du dernier article parcouru (mode reprise)
    return state


def save_state(state):
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def cursor_to_before(cursor):
    """Convertit le curseur en paramètre `before` pour l'API WordPress.

    `before` est exclusif : `before=D` ne retourne que les articles strictement plus
    anciens que D. Utilisé tel quel, un article publié à la seconde exacte du curseur
    serait sauté définitivement (cas réel lors d'un import en masse, où plusieurs
    articles partagent le même horodatage). On ajoute donc une seconde : le dernier
    article déjà parcouru est re-parcouru, ce qui ne coûte rien (il est soit dans
    skip_ids, soit encore réellement à taguer, donc légitimement re-proposé), et
    aucun de ses jumeaux d'horodatage n'est perdu. Un léger recouvrement vaut mieux
    qu'un trou silencieux.
    """
    if not cursor:
        return None
    try:
        return (datetime.fromisoformat(cursor) + timedelta(seconds=1)).isoformat()
    except ValueError:
        # Curseur illisible (édité à la main, format inattendu) : on préfère repartir
        # du haut plutôt que de planter ou de sauter silencieusement du catalogue.
        print(f"Attention — curseur illisible ({cursor!r}), scan repris depuis le début.")
        return None


def next_batch_number():
    BATCHES_DIR.mkdir(exist_ok=True)
    existing = [p.stem for p in BATCHES_DIR.glob("batch_*.json") if "_proposed" not in p.stem and "_reviewed" not in p.stem]
    nums = [int(re.search(r"batch_(\d+)$", n).group(1)) for n in existing if re.search(r"batch_(\d+)$", n)]
    return (max(nums) + 1) if nums else 1


def html_to_text(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ")
    return re.sub(r"\s+", " ", text).strip()


def parse_ids(raw):
    """Accepte "123,456" ou le chemin d'un fichier contenant un ID par ligne.

    Lève ValueError (jamais une exception brute) si l'entrée est vide ou contient un
    token non numérique — le contrat est explicite pour l'appelant, comme validate_schema
    dans apply_batch.py.
    """
    try:
        path = Path(raw)
        is_file = path.exists()
    except OSError:
        # Une longue liste d'IDs inline (ex. 131 IDs séparés par des virgules, ~650
        # caractères) dépasse la limite de nom de fichier de l'OS (ENAMETOOLONG) :
        # Path.exists() lève alors une exception au lieu de renvoyer False. Dans ce
        # cas ce n'est de toute façon jamais un chemin valide, donc on traite l'entrée
        # comme une liste d'IDs inline plutôt que de planter.
        is_file = False
    if is_file:
        raw = path.read_text()

    tokens = [t for t in re.split(r"[,\s]+", raw.strip()) if t]
    if not tokens:
        raise ValueError("--ids : aucun identifiant fourni.")

    ids = []
    invalides = []
    for token in tokens:
        if token.isdigit():
            ids.append(int(token))
        else:
            invalides.append(token)
    if invalides:
        raise ValueError(f"--ids : identifiant(s) non numérique(s) : {invalides}")
    return ids


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=20)
    parser.add_argument(
        "--from-top",
        action="store_true",
        help="Ignore le curseur et repart des articles les plus récents "
        "(pour rattraper les publications récentes). Ne modifie pas le curseur.",
    )
    parser.add_argument(
        "--ids",
        help="Liste d'IDs d'articles à traiter (\"123,456\" ou chemin d'un fichier, un ID "
        "par ligne), quel que soit leur nombre de tags actuel. Sert au re-tagging "
        "rétroactif d'articles déjà tagués. Ignore le curseur, --size et --from-top.",
    )
    args = parser.parse_args()

    if args.ids:
        try:
            wanted = parse_ids(args.ids)
        except ValueError as e:
            print(f"Erreur : {e}")
            return

    state = load_state()
    skip_ids = set(state["processed"]) | set(state["queued"]) | set(state["skipped"])

    categories = wp_client.list_categories()
    all_tags_map = wp_client.list_all_tags()  # name -> id, snapshot live à l'instant du lot
    tags_by_id = {tid: name for name, tid in all_tags_map.items()}

    if args.ids:
        # Mode ciblé : on ne filtre ni sur le nombre de tags, ni sur skip_ids (ces articles
        # sont justement déjà traités), et on ne touche pas au curseur du backlog.
        batch_posts = wp_client.get_posts_by_ids(wanted)
        trouves = {p["id"] for p in batch_posts}
        manquants = [i for i in wanted if i not in trouves]
        print(f"Mode --ids : {len(batch_posts)}/{len(wanted)} article(s) récupéré(s).")
        if manquants:
            print(f"  Introuvables (supprimés, brouillons ou IDs erronés) : {manquants}")
        if not batch_posts:
            return
        scan = None
    else:
        before = None if args.from_top else cursor_to_before(state["scan_cursor"])
        if args.from_top:
            print("Mode --from-top : scan depuis les articles les plus récents.")
        elif before:
            print(f"Reprise du scan avant {state['scan_cursor']}.")
        else:
            print("Aucun curseur enregistré : scan depuis les articles les plus récents.")

        scan = wp_client.list_untagged_posts(args.size, skip_ids=skip_ids, before=before)
        batch_posts = scan["posts"]

        # Le curseur avance même si le lot est vide ou partiel : c'est justement ce qui fait
        # progresser le scan d'une exécution à l'autre. En mode --from-top on n'y touche pas,
        # pour ne pas perdre la position dans le backlog.
        if not args.from_top and scan["last_scanned_date"]:
            state["scan_cursor"] = scan["last_scanned_date"]

        if not batch_posts:
            save_state(state)
            if scan["reached_end"]:
                print(
                    "Fin du catalogue atteinte : plus aucun article plus ancien à parcourir.\n"
                    "Pour rattraper les articles publiés depuis, relance avec --from-top."
                )
            else:
                print(
                    f"Aucun article à taguer trouvé dans les {scan['scanned']} articles parcourus "
                    "(déjà tagués ou déjà en file).\n"
                    "Le curseur a avancé : relance la commande pour continuer plus loin dans le "
                    "catalogue."
                )
            return

        if len(batch_posts) < args.size:
            if scan["reached_end"]:
                print(
                    f"Note : {len(batch_posts)}/{args.size} articles trouvés — fin du catalogue "
                    "atteinte."
                )
            else:
                print(
                    f"Note : {len(batch_posts)}/{args.size} articles trouvés "
                    f"(limite de scan atteinte après {scan['scanned']} articles parcourus). "
                    "Relance après ce lot pour continuer."
                )

    articles = []
    for p in batch_posts:
        content_html = wp_client.get_post_content(p["id"])
        cat_names = [categories.get(cid, str(cid)) for cid in p.get("categories", [])]
        existing_tag_names = [tags_by_id.get(tid, str(tid)) for tid in p.get("tags", [])]
        articles.append(
            {
                "id": p["id"],
                "title": p["title"]["rendered"],
                "category": cat_names,
                "content_text": html_to_text(content_html),
                "existing_tags": existing_tag_names,
            }
        )

    batch_num = next_batch_number()
    out_path = BATCHES_DIR / f"batch_{batch_num:04d}.json"
    out_data = {
        "tags_existants": sorted(all_tags_map.keys()),
        "categories_existantes": sorted(categories.values()),
        "articles": articles,
    }
    out_path.write_text(json.dumps(out_data, indent=2, ensure_ascii=False))

    state["queued"].extend(p["id"] for p in batch_posts)
    save_state(state)

    print(f"Lot écrit : {out_path} ({len(articles)} articles)")
    if args.ids:
        print(
            "Re-tagging : les tags proposés devront être appliqués avec "
            "`apply_batch.py --replace` pour remplacer les tags actuels au lieu de s'y ajouter."
        )
    elif not args.from_top:
        print(f"Curseur : {state['scan_cursor']}")


if __name__ == "__main__":
    main()