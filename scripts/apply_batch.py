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

Par défaut les tags du lot s'AJOUTENT à ceux déjà présents sur l'article. `--replace`
remplace au contraire l'ensemble des tags par ceux du lot : c'est le mode du re-tagging
rétroactif, seul moyen de retirer un tag devenu faux après une évolution des règles. Les
tags retirés sont listés explicitement avant écriture. `--dry-run` affiche ce qui serait
fait sans rien modifier, ni sur WordPress ni dans state.json.

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


# Composants PC internes : chacun doit toujours s'accompagner de "Matériel PC" (§4).
COMPOSANTS_INTERNES = {
    "Carte mère", "Processeur", "Carte graphique", "RAM", "SSD",
    "Alimentation", "Boîtier", "Refroidissement",
}
# Matériel externe : chacun doit toujours s'accompagner de "Périphérique" (§4).
COMPOSANTS_EXTERNES = {
    "Casque audio", "Chaise gaming", "Clavier", "Souris", "Microphone", "Écran",
    "Manette", "Périphérique de Simulation",
}


# Thèmes/univers de §5 — sert au contrôle de couverture de la Grille #6.
# Liste tenue à jour manuellement depuis regles-tagging-actives.md : c'est une politique
# éditoriale, pas un inventaire de ce qui existe sur WordPress.
THEMES_UNIVERS = {
    "Années 80", "Aviation", "Cyberpunk", "Dinosaures", "Enquête", "Espace", "Fantasy",
    "Fantastique", "Far West", "Guerre", "Guerre froide", "Horreur", "IA", "Lovecraftien",
    "Médiéval", "Mythologie", "Pirates", "Policier", "Post-apocalyptique",
    "Robot", "Science-fiction", "Steampunk", "Super-héros", "WW1", "WW2", "Zombies",
}

# Tout le vocabulaire FERMÉ hors §5 univers : genres, plateformes, mécaniques,
# qualificatifs, événements, rubriques. Un tag qui n'est dans AUCUNE de ces listes est,
# par élimination, un tag d'identité (§1/§2/§8) — licence, studio, personne ou pays.
VOCABULAIRE_FERME_AUTRE = {
    # §3 genres
    "Action", "Action-aventure", "Action-RPG", "Aventure", "Battle royale", "Beat'em up",
    "Combat", "Cosy", "Course", "Deckbuilder", "Extraction shooter", "FPS", "Gestion",
    "Hack'n'slash", "Idle", "Infiltration", "JRPG", "Metroidvania", "MMO", "MOBA",
    "Narratif", "Party game", "Plateforme", "Point &amp; click", "Réflexion", "Roguelike",
    "RPG", "Rythme", "Shoot'em up", "Simulation", "Souls-like", "Sport", "Stratégie",
    "Survie", "TPS", "Biopic", "Comédie", "Documentaire", "Drame", "Thriller",
    # §4 plateformes & matériel
    "Cloud gaming", "Mobile", "Nintendo Switch", "PC", "PlayStation", "Rétro",
    "Steam Deck", "VR", "Xbox", "Apple TV+", "Canal+", "Crunchyroll", "Disney+",
    "HBO Max", "Netflix", "Paramount+", "Peacock", "Prime Video",
    "Alimentation", "AR", "Aspirateur robot", "Boîtier", "Carte graphique", "Carte mère",
    "Casque audio", "Chaise gaming", "Clavier", "Écran", "Électroménager", "Manette",
    "Matériel PC", "Microphone", "Montre connectée", "Périphérique",
    "Périphérique de Simulation", "Processeur", "RAM", "Refroidissement", "Réseau",
    "Smartphone", "Souris", "SSD",
    # §5 mécaniques, qualificatifs, métiers, rubriques
    "Compétitif", "Coopératif", "En ligne", "Local", "Monde ouvert", "Multijoueur", "Solo",
    "Animation", "Esport", "Indé", "Remake", "Remaster",
    "Cinéma", "Doublage", "Manga", "Carnet noir", "Montage PC", "Game Conscient",
    # §5bis, §7
    "Voiture", "Voiture hybride", "Voiture électrique", "Suisse",
}


# Genres (§3) et plateformes/services (§4) — servent à repérer les articles qui portent
# sur une ŒUVRE (jeu, film, série) plutôt que sur du matériel ou de l'actualité
# économique. C'est un proxy imparfait mais c'est le seul disponible : WordPress ne
# stocke que des noms de tags, rien ne distingue `Star Wars` (licence) de `Dreame`
# (marque d'électroménager) ou `Quantic Dream` (studio).
MARQUEURS_OEUVRE = {
    # §3 genres
    "Action", "Action-aventure", "Action-RPG", "Aventure", "Battle royale", "Beat'em up",
    "Combat", "Cosy", "Course", "Deckbuilder", "Extraction shooter", "FPS", "Gestion",
    "Hack'n'slash", "Idle", "Infiltration", "JRPG", "Metroidvania", "MMO", "MOBA",
    "Narratif", "Party game", "Plateforme", "Point &amp; click", "Réflexion", "Roguelike",
    "RPG", "Rythme", "Shoot'em up", "Simulation", "Souls-like", "Sport", "Stratégie",
    "Survie", "TPS", "Biopic", "Comédie", "Documentaire", "Drame", "Thriller", "Animation",
    # §4 plateformes de jeu et services de diffusion
    "Cloud gaming", "Mobile", "Nintendo Switch", "PC", "PlayStation", "Steam Deck", "VR",
    "Xbox", "Apple TV+", "Canal+", "Crunchyroll", "Disney+", "HBO Max", "Netflix",
    "Paramount+", "Peacock", "Prime Video",
}


def check_theme_coverage(articles):
    """Liste les articles portant sur une œuvre mais sans aucun thème/univers §5.

    NON BLOQUANT, et volontairement compact : une seule ligne récapitulative plutôt
    qu'un avertissement par article. La détection est imprécise par construction — sur
    un lot réel, environ un tiers des articles listés sont de vrais oublis, le reste
    étant des œuvres qui n'ont légitimement pas d'univers (jeu de combat, de course, de
    sport) ou des articles de matériel qui portent un tag de plateforme. Un avertissement
    par article noierait la sortie ; une liste d'identifiants se parcourt en quelques
    secondes pendant la relecture.

    Ce contrôle existe parce que la Grille #6 déclare le thème « systématique dès qu'une
    licence est taguée », et que c'est en pratique la facette la plus souvent sautée —
    or elle porte le maillage transversal dont dépend la recommandation.

    Les articles dont le champ `incertitudes` mentionne déjà l'univers ou le thème sont
    exclus : le choix a été explicité, il n'y a rien à re-signaler.
    """
    sans_theme = []
    for article in articles:
        names = set(article.get("tags") or []) | set(article.get("nouveaux_tags") or [])
        if names & THEMES_UNIVERS:
            continue
        if not names & MARQUEURS_OEUVRE:
            continue  # ni genre ni plateforme : probablement pas une œuvre de fiction
        deja_signale = any(
            mot in (i or "").lower()
            for i in (article.get("incertitudes") or [])
            for mot in ("univers", "thème", "theme")
        )
        if deja_signale:
            continue
        sans_theme.append(article.get("id"))
    return sans_theme

def validate_pairings(articles):
    """Vérifie les paires de tags obligatoires et SANS EXCEPTION de
    regles-tagging-actives.md : composant interne -> Matériel PC, matériel externe ->
    Périphérique (§4), Coopératif/Compétitif -> Multijoueur (Grille #7).

    Contrairement aux paires studio/éditeur (§2, ex. Rockstar Games -> Take-Two), qui
    ont une exception documentée (règle "personne + œuvre-signature") et exigent donc
    un jugement éditorial, ces trois paires sont purement mécaniques : si la condition
    est remplie, le tag d'accompagnement l'est toujours aussi, sans cas particulier.
    C'est exactement le genre de règle qu'un script vérifie de façon fiable là où une
    proposition de lot, même relue avec soin, peut en oublier une au fil des articles
    (c'est arrivé : Carte graphique posé sans Matériel PC sur un article DLSS 5).
    """
    errors = []
    for article in articles:
        post_id = article.get("id")
        names = {t for t in (article.get("tags") or []) if isinstance(t, str)}
        names |= {t for t in (article.get("nouveaux_tags") or []) if isinstance(t, str)}

        manquants_internes = sorted(names & COMPOSANTS_INTERNES)
        if manquants_internes and "Matériel PC" not in names:
            errors.append(
                f"article {post_id} : {manquants_internes} présent(s) sans 'Matériel PC' "
                "(§4 — obligatoire pour tout composant PC interne)."
            )

        manquants_externes = sorted(names & COMPOSANTS_EXTERNES)
        if manquants_externes and "Périphérique" not in names:
            errors.append(
                f"article {post_id} : {manquants_externes} présent(s) sans 'Périphérique' "
                "(§4 — obligatoire pour tout matériel externe)."
            )

        if ("Coopératif" in names or "Compétitif" in names) and "Multijoueur" not in names:
            errors.append(
                f"article {post_id} : 'Coopératif'/'Compétitif' présent sans 'Multijoueur' "
                "(Grille #7 — obligatoire dès que l'un des deux est posé)."
            )

    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("reviewed_file")
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Remplace les tags de l'article par ceux du lot, au lieu de les ajouter aux "
        "tags existants. Nécessaire pour le re-tagging rétroactif (retirer un tag devenu "
        "faux). Les tags retirés sont listés avant écriture.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Affiche ce qui serait écrit sans rien modifier — ni WordPress, ni state.json.",
    )
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

    # 2) Paires de tags obligatoires (Matériel PC, Périphérique, Multijoueur) : comme
    # la validation de forme, sans appel réseau, et bloquant pour tout le lot.
    pairing_errors = validate_pairings(articles)
    if pairing_errors:
        print(f"Lot refusé, {len(pairing_errors)} paire(s) de tags obligatoire(s) manquante(s) :")
        for message in pairing_errors:
            print(f"  - {message}")
        print("\nAucune écriture effectuée. Corrige le fichier et relance.")
        return

    # 2bis) Couverture thématique (Grille #6) : NON BLOQUANT. Le script ne peut pas savoir
    # si l'absence d'univers est un choix ou un oubli — il signale, l'humain tranche.
    sans_theme = check_theme_coverage(articles)
    if sans_theme:
        print(
            f"Grille #6 — {len(sans_theme)} article(s) sur une œuvre sans thème/univers §5 : "
            + ", ".join(str(i) for i in sans_theme)
        )
        print(
            "  L'univers d'une licence connue se déduit même s'il n'est pas cité "
            "(Star Wars → Espace, Batman → Super-héros). Une œuvre définie par son seul "
            "gameplay (combat, course, sport) n'en a pas besoin — cette liste est "
            "indicative, pas une liste d'erreurs.\n"
        )

    tag_map = wp_client.list_all_tags()  # name -> id, rafraîchi une fois pour tout le lot
    names_by_id = {tid: name for name, tid in tag_map.items()}

    # 3) Validation des noms contre WordPress : un nom dans "tags" qui ne matche rien
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

    if args.dry_run:
        print("--- DRY RUN : aucune écriture, ni sur WordPress ni dans state.json ---\n")
    if args.replace:
        print("Mode --replace : les tags absents du lot seront RETIRÉS des articles.\n")

    # Lecture groupée des tags actuels : une requête par paquet de 100 articles au lieu
    # d'une par article.
    current_by_id = wp_client.get_current_tags([a["id"] for a in articles])

    state = load_state()
    # En dry-run, un tag pas encore créé reçoit un ID négatif fictif (jamais attribué par
    # WordPress, qui ne produit que des IDs positifs) : sans ça, un tag "à créer" était
    # absent du décompte final affiché (`len(final_ids)` sous-estimait l'aperçu), alors que
    # la liste des tags RETIRÉS — la partie sensible avant un --replace — restait juste,
    # puisqu'un tag qui n'existe pas encore ne peut de toute façon pas être retiré.
    next_fake_id = 0

    for article in articles:
        post_id = article["id"]
        existing_names = list(article.get("tags", []))
        new_names = list(article.get("nouveaux_tags", []))

        tag_ids = [tag_map[name] for name in existing_names]
        for name in new_names:
            tag_id = tag_map.get(name)
            if tag_id is None:
                if args.dry_run:
                    next_fake_id -= 1
                    tag_id = next_fake_id
                    print(f"  + tag à créer : {name!r}")
                else:
                    tag_id = wp_client.create_tag(name)
                    print(f"  + nouveau tag créé : {name!r} (id {tag_id})")
                tag_map[name] = tag_id
                names_by_id[tag_id] = name
            tag_ids.append(tag_id)

        current_tag_ids = current_by_id.get(post_id, [])
        if args.replace:
            final_ids = sorted(set(tag_ids))
            removed = sorted(set(current_tag_ids) - set(final_ids))
        else:
            final_ids = sorted(set(current_tag_ids) | set(tag_ids))
            removed = []

        if not args.dry_run:
            wp_client.update_post_tags(post_id, final_ids)

        prefix = "[dry-run] " if args.dry_run else ""
        print(f"{prefix}Article {post_id} : {len(final_ids)} tags ({existing_names + new_names}).")
        if removed:
            removed_names = [names_by_id.get(tid, f"id {tid}") for tid in removed]
            print(f"{prefix}  - retirés : {removed_names}")

        if args.dry_run:
            continue

        state["queued"] = [pid for pid in state["queued"] if pid != post_id]
        if post_id not in state["processed"]:
            state["processed"].append(post_id)
        save_state(state)  # sauvegarde incrémentale : un crash en cours de lot ne perd pas
        # le suivi des articles déjà écrits sur WordPress avant l'erreur

    if args.dry_run:
        print(f"\nDry run terminé : {len(articles)} article(s) analysé(s), rien écrit.")
    else:
        print(f"\nLot appliqué : {len(articles)} article(s).")


if __name__ == "__main__":
    main()