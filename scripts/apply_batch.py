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

Deux validations successives ont lieu avant la moindre écriture, et une seule erreur
suffit à refuser tout le lot :
  1. **Forme du fichier** (`validate_schema`, sans aucun appel réseau) : structure, `id`
     présent et entier, `tags`/`nouveaux_tags` bien des listes d'objets, et surtout
     `grille_line` présent sur chaque tag avec une valeur entière entre 1 et 12. Ce
     contrôle est indispensable car `grille_line` est invisible côté WordPress : un tag
     sans ligne de Grille s'écrirait correctement sur le site tout en corrompant
     silencieusement l'archive de provenance. Un article sans aucun tag déclenche un
     avertissement non bloquant (rare mais légitime : programme, liste pure).
  2. **Existence des noms sur WordPress** (voir garde-fou anti-doublon ci-dessous).

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


GRILLE_LINE_MIN = 1
GRILLE_LINE_MAX = 12


def validate_schema(articles):
    """Vérifie la forme du lot AVANT la moindre écriture WordPress.

    Retourne (erreurs, avertissements), deux listes de strings. Une seule erreur
    suffit à refuser tout le lot : mieux vaut corriger le fichier et relancer que
    d'écrire la moitié d'un lot mal formé.

    Ce contrôle existe parce que `grille_line` est invisible côté WordPress : un tag
    sans ligne de Grille, ou avec une valeur absurde, s'écrirait tout de même
    correctement sur le site tout en corrompant silencieusement
    `tag_provenance.jsonl` — la seule trace durable dont dépend le futur système de
    points de l'app. Un problème silencieux ici ne se découvrirait que des milliers
    d'articles plus tard.
    """
    errors = []
    warnings = []

    if not isinstance(articles, list):
        return ["Le fichier doit contenir une liste d'articles (JSON array)."], []

    for index, article in enumerate(articles):
        where = f"article #{index + 1}"
        if not isinstance(article, dict):
            errors.append(f"{where} : doit être un objet JSON, reçu {type(article).__name__}.")
            continue

        post_id = article.get("id")
        if post_id is None:
            errors.append(f"{where} : champ 'id' manquant.")
        elif not isinstance(post_id, int):
            errors.append(f"{where} : 'id' doit être un entier, reçu {post_id!r}.")
        else:
            where = f"article {post_id}"

        for field in ("tags", "nouveaux_tags"):
            entries = article.get(field, [])
            if not isinstance(entries, list):
                errors.append(f"{where} : '{field}' doit être une liste.")
                continue

            for entry in entries:
                # Cas le plus probable : l'ancien format (simple liste de noms), soit
                # parce que le lot vient d'avant le changement de schéma, soit parce que
                # Claude Code a produit l'ancienne forme. Message explicite plutôt qu'un
                # TypeError incompréhensible plus loin dans le script.
                if isinstance(entry, str):
                    errors.append(
                        f"{where} : '{field}' contient le nom brut {entry!r} au lieu d'un "
                        f"objet. Format attendu : {{\"name\": {entry!r}, \"grille_line\": N}}."
                    )
                    continue
                if not isinstance(entry, dict):
                    errors.append(
                        f"{where} : '{field}' contient une entrée invalide ({entry!r})."
                    )
                    continue

                name = entry.get("name")
                if not isinstance(name, str) or not name.strip():
                    errors.append(
                        f"{where} : '{field}' contient une entrée sans 'name' utilisable "
                        f"({entry!r})."
                    )
                    name = repr(entry)

                if "grille_line" not in entry:
                    errors.append(
                        f"{where} : tag {name!r} sans 'grille_line'. Chaque tag doit porter "
                        f"le numéro de ligne de la Grille ({GRILLE_LINE_MIN}-{GRILLE_LINE_MAX}) "
                        "qui l'a produit."
                    )
                else:
                    line = entry["grille_line"]
                    if not isinstance(line, int) or isinstance(line, bool):
                        errors.append(
                            f"{where} : tag {name!r} a un 'grille_line' non entier ({line!r})."
                        )
                    elif not GRILLE_LINE_MIN <= line <= GRILLE_LINE_MAX:
                        errors.append(
                            f"{where} : tag {name!r} a un 'grille_line' hors bornes ({line}). "
                            f"Valeurs valides : {GRILLE_LINE_MIN} à {GRILLE_LINE_MAX}."
                        )

        total_tags = len(article.get("tags", []) or []) + len(article.get("nouveaux_tags", []) or [])
        if total_tags == 0:
            # Non bloquant : un article sans aucun tag est légitime dans de rares cas
            # (programme multi-films, liste pure). Mais la nomenclature cible 8-10 tags
            # par article, donc c'est assez inhabituel pour mériter une relecture humaine.
            warnings.append(
                f"{where} : aucun tag proposé. Vérifier que c'est volontaire "
                "(programme/liste) et non un article mal traité."
            )

    return errors, warnings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("reviewed_file")
    args = parser.parse_args()

    articles = json.loads(Path(args.reviewed_file).read_text())

    # 1) Validation de forme, avant même d'interroger WordPress : un lot mal formé est
    # refusé en bloc, sans aucun appel réseau ni écriture.
    schema_errors, schema_warnings = validate_schema(articles)
    if schema_errors:
        print(f"Lot refusé, {len(schema_errors)} erreur(s) de format :")
        for message in schema_errors:
            print(f"  - {message}")
        print("\nAucune écriture effectuée. Corrige le fichier et relance.")
        return
    for message in schema_warnings:
        print(f"Attention — {message}")
    if schema_warnings:
        print()

    tag_map = wp_client.list_all_tags()  # name -> id, rafraîchi une fois pour tout le lot

    # 2) Validation des noms contre WordPress : un nom dans "tags" qui ne matche rien
    # exactement est bloquant (probable faute de frappe/casse), pas un nouveau tag à créer
    # silencieusement. Seul "nouveaux_tags" est autorisé à créer.
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