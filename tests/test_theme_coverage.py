"""Vérifie le contrôle non bloquant de couverture thématique (Grille #6).

Ce contrôle est imprécis par construction : WordPress ne stocke que des noms de tags,
donc rien ne distingue une licence d'un studio ou d'une marque de matériel. Les tests
ci-dessous fixent le comportement attendu sur les cas nets, pas un taux de précision.
"""
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.modules.setdefault("wp_client", types.ModuleType("wp_client"))
import apply_batch  # noqa: E402

CAS = [
    # (libellé, article, doit être signalé)
    (
        "licence de fiction sans thème (vrai oubli type Battlefield)",
        {"id": 1, "tags": ["Battlefield", "FPS", "PC"], "nouveaux_tags": []},
        True,
    ),
    (
        "même article avec le thème posé",
        {"id": 2, "tags": ["Battlefield", "FPS", "PC", "Guerre"], "nouveaux_tags": []},
        False,
    ),
    (
        "thème présent uniquement dans nouveaux_tags",
        {"id": 3, "tags": ["Gothic", "RPG"], "nouveaux_tags": ["Médiéval"]},
        False,
    ),
    (
        "matériel : marque + composant, aucun marqueur d'œuvre",
        {"id": 4, "tags": ["Dreame", "Aspirateur robot", "Électroménager"], "nouveaux_tags": []},
        False,
    ),
    (
        "actualité économique sans genre ni plateforme",
        {"id": 5, "tags": ["Microsoft", "Sony"], "nouveaux_tags": []},
        False,
    ),
    (
        "choix déjà explicité dans incertitudes",
        {
            "id": 6,
            "tags": ["CAPTCHA Hell", "Aventure", "PC"],
            "nouveaux_tags": [],
            "incertitudes": ["Pas de thème/univers fermé qui corresponde"],
        },
        False,
    ),
    (
        "article vide de tags",
        {"id": 7, "tags": [], "nouveaux_tags": []},
        False,
    ),
    (
        "champs tags/nouveaux_tags absents",
        {"id": 8},
        False,
    ),
]

echecs = 0
for libelle, article, attendu in CAS:
    signale = article.get("id") in apply_batch.check_theme_coverage([article])
    ok = signale == attendu
    if not ok:
        echecs += 1
    print(f"  {'OK  ' if ok else 'FAIL'} {libelle:58} signalé={signale} attendu={attendu}")

print()
if echecs:
    print(f"ECHEC — {echecs} cas incorrect(s).")
    sys.exit(1)
print("OK — le contrôle de couverture thématique se comporte comme prévu.")