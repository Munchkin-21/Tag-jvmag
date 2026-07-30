"""Applique un lot relu/validé de propositions de tags à WordPress.

Usage: python scripts/apply_batch.py batches/batch_0001_reviewed.json

Format attendu du fichier reviewed (liste d'objets, un par article) :
[
  {
    "id": 123,
    "tags": [
      {"name": "Hitman", "grille_line": 1},
      {"name": "IO Interactive", "grille_line": 3},
      {"name": "PC", "grille_line": 5},
      {"name": "Action", "grille_line": 4},
      {"name": "Infiltration", "grille_line": 4}
    ],
    "nouveaux_tags": [
      {"name": "Nom Du Nouveau Tag", "grille_line": 1}
    ]
  },
  ...
]
`grille_line` = numéro de ligne de la Grille de tagging obligatoire (1-12, voir
regles-tagging-actives.md) qui a produit ce tag. Sert à distinguer a posteriori un tag
d'identité (lignes 1, 2, 3, 12 — OUVERT) d'un tag de facette de contenu (lignes 4 à 11 —
FERMÉ/semi-fermé) : WordPress ne porte que des tags plats, cette distinction ne survit
que si elle est archivée ailleurs — voir `tag_provenance.jsonl` ci-dessous.

Le champ "incertitudes" (s'il est présent) est ignoré ici : c'est un signal humain,
pas une instruction d'écriture.

Garde-fou anti-doublon : seuls les noms listés dans "nouveaux_tags" peuvent déclencher la
création d'un tag WordPress (ils sont censés avoir déjà été validés humainement en amont, dans
la conversation). Un nom dans "tags" est censé DÉJÀ exister ; s'il ne matche rien exactement,
c'est traité comme une erreur bloquante (faute de frappe/casse probable) plutôt que créé en
silence — pour ne jamais faire grossir la liste de tags sans validation explicite.

Archive de provenance : à chaque article appliqué, un enregistrement complet (id article,
tags + grille_line, nouveaux_tags, horodatage) est ajouté à `tag_provenance.jsonl`, à la
racine du repo. Contrairement à `batches/` (gitignored, éphémère), ce fichier est committé :
c'est la seule trace durable du lien tag <-> ligne de Grille une fois les tags aplatis sur
WordPress. Format JSON Lines (un objet JSON par ligne) pour permettre l'ajout incrémental
sans jamais relire/réécrire tout le fichier.
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import wp_client

SCRIPTS_DIR = Path(__file__).resolve().parent
ROOT = SCRIPTS_DIR.parent
STATE_PATH = SCRIPTS_DIR / "state.json"
PROVENANCE_PATH = ROOT / "tag_provenance.jsonl"


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


def append_provenance(record):
    with PROVENANCE_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


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
        new_names = {t["name"] for t in article.get("nouveaux_tags", [])}
        for tag in article.get("tags", []):
            if tag["name"] not in tag_map and tag["name"] not in new_names:
                errors.append((article["id"], tag["name"]))
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
        existing_tags = list(article.get("tags", []))
        new_tags = list(article.get("nouveaux_tags", []))

        tag_ids = [tag_map[t["name"]] for t in existing_tags]
        for t in new_tags:
            tag_id = tag_map.get(t["name"])
            if tag_id is None:
                tag_id = wp_client.create_tag(t["name"])
                tag_map[t["name"]] = tag_id
                print(f"  + nouveau tag créé : {t['name']!r} (id {tag_id})")
            tag_ids.append(tag_id)

        current = wp_client.get("posts", include=post_id, _fields="id,tags")
        current_tag_ids = current[0]["tags"] if current else []
        merged_ids = sorted(set(current_tag_ids) | set(tag_ids))

        wp_client.update_post_tags(post_id, merged_ids)
        all_names = [t["name"] for t in existing_tags + new_tags]
        print(f"Article {post_id} : {len(merged_ids)} tags posés ({all_names}).")

        append_provenance(
            {
                "article_id": post_id,
                "tags": existing_tags,
                "nouveaux_tags": new_tags,
                "applied_at": datetime.now(timezone.utc).isoformat(),
            }
        )

        state["queued"] = [pid for pid in state["queued"] if pid != post_id]
        if post_id not in state["processed"]:
            state["processed"].append(post_id)
        save_state(state)  # sauvegarde incrémentale : un crash en cours de lot ne perd pas
        # le suivi des articles déjà écrits sur WordPress avant l'erreur

    print(f"\nLot appliqué : {len(articles)} article(s).")


if __name__ == "__main__":
    main()