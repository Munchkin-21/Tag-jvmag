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

Deux validations successives ont lieu avant la moindre écriture, et une seule erreur
suffit à refuser tout le lot — mieux vaut corriger le fichier et relancer que d'écrire
la moitié d'un lot mal formé :
  1. **Forme du fichier** (`validate_schema`, sans aucun appel réseau) : le fichier est
     bien une liste, chaque article a un `id` entier, `tags` et `nouveaux_tags` sont des
     listes de noms non vides. Un article sans aucun tag déclenche un avertissement non
     bloquant (rare mais légitime : programme, liste pure).
  2. **Existence des noms sur WordPress** (voir garde-fou anti-doublon ci-dessous).

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


def validate_schema(articles):
    """Vérifie la forme du lot AVANT tout appel réseau et toute écriture.

    Retourne (erreurs, avertissements), deux listes de messages prêts à afficher.
    Le but n'est pas d'être exhaustif mais d'attraper les erreurs réelles avec un
    message qui dit quoi corriger, plutôt que de laisser le script planter plus loin
    sur un KeyError ou un TypeError incompréhensible.
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
        elif not isinstance(post_id, int) or isinstance(post_id, bool):
            errors.append(f"{where} : 'id' doit être un entier, reçu {post_id!r}.")
        else:
            where = f"article {post_id}"

        for field in ("tags", "nouveaux_tags"):
            entries = article.get(field, [])
            if not isinstance(entries, list):
                errors.append(f"{where} : '{field}' doit être une liste de noms de tags.")
                continue

            for entry in entries:
                if isinstance(entry, dict):
                    # Un objet au lieu d'un nom : message explicite plutôt qu'un
                    # TypeError plus loin. Format attendu = simple liste de noms.
                    name = entry.get("name", "?")
                    errors.append(
                        f"{where} : '{field}' contient un objet ({entry!r}) au lieu du seul "
                        f"nom du tag. Format attendu : \"{name}\"."
                    )
                elif not isinstance(entry, str):
                    errors.append(
                        f"{where} : '{field}' contient une entrée invalide ({entry!r}), "
                        "attendu un nom de tag."
                    )
                elif not entry.strip():
                    errors.append(f"{where} : '{field}' contient un nom vide.")

        total_tags = len(article.get("tags") or []) + len(article.get("nouveaux_tags") or [])
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
        new_names = set(article.get("nouveaux_tags", []))
        for name in article.get("tags", []):
            if name not in tag_map and name not in new_names:
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