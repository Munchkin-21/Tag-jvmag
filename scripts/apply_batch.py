"""Applique un lot relu/validé de propositions de tags à WordPress.

Usage: python scripts/apply_batch.py batches/batch_0001_reviewed.json

Format attendu du fichier reviewed (liste d'objets, un par article) :
[
  {
    "id": 123,
    "tags": ["Hitman", "IO Interactive", "PC", "Action", "Infiltration"],
    "nouveaux_tags": ["Nom Du Nouveau Tag"]   # déjà validés humainement, créés si absents
  },
  ...
]
Le champ "incertitudes" (s'il est présent) est ignoré ici : c'est un signal humain,
pas une instruction d'écriture.

Garde-fou anti-doublon : seuls les noms listés dans "nouveaux_tags" peuvent déclencher la
création d'un tag WordPress (ils sont censés avoir déjà été validés humainement en amont, dans
la conversation). Un nom dans "tags" est censé DÉJÀ exister ; s'il ne matche rien exactement,
c'est traité comme une erreur bloquante (faute de frappe/casse probable) plutôt que créé en
silence — pour ne jamais faire grossir la liste de tags sans validation explicite.
"""
import argparse
import json
from pathlib import Path

import wp_client

SCRIPTS_DIR = Path(__file__).resolve().parent
STATE_PATH = SCRIPTS_DIR / "state.json"


def load_state():
    if STATE_PATH.exists():
        state = json.loads(STATE_PATH.read_text())
    else:
        state = {}
    state.setdefault("processed", [])
    state.setdefault("queued", [])
    state.setdefault("skipped", [])
    return state


def save_state(state):
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("reviewed_file")
    args = parser.parse_args()

    articles = json.loads(Path(args.reviewed_file).read_text())
    tag_map = wp_client.list_all_tags()  # name -> id, rafraîchi une fois pour tout le lot

    # Validation à blanc de tout le lot avant la moindre écriture : un nom dans "tags" qui
    # ne matche rien exactement est bloquant (probable faute de frappe/casse), pas un nouveau
    # tag à créer silencieusement. Seul "nouveaux_tags" est autorisé à créer.
    errors = []
    for article in articles:
        for name in article.get("tags", []):
            if name not in tag_map and name not in article.get("nouveaux_tags", []):
                errors.append((article["id"], name))
    if errors:
        print("Lot refusé, des noms dans 'tags' n'existent pas encore sur WordPress :")
        for post_id, name in errors:
            print(f"  - article {post_id} : {name!r}")
        print(
            "Si ce sont vraiment de nouveaux tags, déplace-les dans 'nouveaux_tags'. "
            "Sinon corrige la casse/orthographe pour matcher le tag existant."
        )
        return

    state = load_state()

    for article in articles:
        post_id = article["id"]
        existing_names = list(article.get("tags", []))
        new_names = list(article.get("nouveaux_tags", []))

        tag_ids = [tag_map[name] for name in existing_names]
        for name in new_names:
            tag_id = tag_map.get(name)
            if tag_id is None:
                tag_id = wp_client.create_tag(name)
                tag_map[name] = tag_id
                print(f"  + nouveau tag créé : {name!r} (id {tag_id})")
            tag_ids.append(tag_id)

        current = wp_client.get("posts", include=post_id, _fields="id,tags")
        current_tag_ids = current[0]["tags"] if current else []
        merged_ids = sorted(set(current_tag_ids) | set(tag_ids))

        wp_client.update_post_tags(post_id, merged_ids)
        print(f"Article {post_id} : {len(merged_ids)} tags posés ({existing_names + new_names}).")

        state["queued"] = [pid for pid in state["queued"] if pid != post_id]
        if post_id not in state["processed"]:
            state["processed"].append(post_id)
        save_state(state)  # sauvegarde incrémentale : un crash en cours de lot ne perd pas
        # le suivi des articles déjà écrits sur WordPress avant l'erreur

    print(f"\nLot appliqué : {len(articles)} article(s).")


if __name__ == "__main__":
    main()
