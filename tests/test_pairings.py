"""Non-régression : apply_batch.validate_pairings() attrape les paires obligatoires
manquantes (Matériel PC, Périphérique, Multijoueur) avant toute écriture WordPress.

C'est arrivé en vrai : un article DLSS 5 taggé 'Carte graphique' sans 'Matériel PC'
est passé inaperçu à la relecture humaine d'un lot de 19 articles. Comme la règle est
mécanique et sans exception (contrairement aux paires studio/éditeur du §2, qui ont un
cas particulier documenté), un script peut la vérifier de façon fiable — ce test
garantit que ce filet de sécurité reste en place.
"""
import sys

sys.path.insert(0, "scripts")
import apply_batch as ab

failures = []


def check(label, articles, expect_errors):
    errors = ab.validate_pairings(articles)
    got = len(errors) > 0
    if got != expect_errors:
        failures.append(f"{label} : attendu erreurs={expect_errors}, obtenu {errors!r}")
    else:
        print(f"OK  {label}{' -> ' + str(errors) if errors else ''}")


# Le cas réel qui est passé inaperçu.
check(
    "Carte graphique sans Matériel PC",
    [{"id": 113854, "tags": ["Carte graphique", "NVIDIA"], "nouveaux_tags": []}],
    expect_errors=True,
)
check(
    "Composant interne dans nouveaux_tags sans Matériel PC",
    [{"id": 1, "tags": [], "nouveaux_tags": ["Processeur"]}],
    expect_errors=True,
)
check(
    "Casque audio sans Périphérique",
    [{"id": 2, "tags": ["Casque audio"], "nouveaux_tags": []}],
    expect_errors=True,
)
check(
    "Coopératif sans Multijoueur",
    [{"id": 3, "tags": ["Coopératif", "PC"], "nouveaux_tags": []}],
    expect_errors=True,
)
check(
    "Compétitif sans Multijoueur",
    [{"id": 4, "tags": ["Compétitif", "PC"], "nouveaux_tags": []}],
    expect_errors=True,
)
check(
    "Toutes les paires correctement complètes",
    [{
        "id": 5,
        "tags": [
            "Carte graphique", "Matériel PC", "Casque audio", "Périphérique",
            "Coopératif", "Compétitif", "Multijoueur",
        ],
        "nouveaux_tags": [],
    }],
    expect_errors=False,
)
check(
    "Aucun composant/mécanique concerné -> rien à signaler",
    [{"id": 6, "tags": ["PC", "Action"], "nouveaux_tags": []}],
    expect_errors=False,
)

if failures:
    print("\nECHEC :")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("\nOK — validate_pairings attrape les paires obligatoires manquantes.")
