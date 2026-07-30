"""Vérifie que chaque wp_client.X appelé par les scripts existe réellement.

Ce test existe parce qu'un contrôle de syntaxe ne l'attrape pas : supprimer par erreur
la ligne `def ma_fonction():` laisse son corps comme code orphelin après un `return`,
ce qui reste syntaxiquement valide. Le pipeline ne plante qu'à l'exécution, sur le
premier article traité.
"""
import ast, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"

wp_src = ast.parse((SCRIPTS / "wp_client.py").read_text())
definies = {n.name for n in wp_src.body if isinstance(n, ast.FunctionDef)}

manquantes = []
for f in ("fetch_batch.py", "apply_batch.py"):
    tree = ast.parse((SCRIPTS / f).read_text())
    for node in ast.walk(tree):
        if (isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name)
                and node.value.id == "wp_client"):
            if node.attr not in definies:
                manquantes.append(f"{f} appelle wp_client.{node.attr}() — introuvable")

# les fonctions publiques du client doivent aussi être appelées quelque part
appelees = set()
for f in ("fetch_batch.py", "apply_batch.py"):
    tree = ast.parse((SCRIPTS / f).read_text())
    for node in ast.walk(tree):
        if (isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name)
                and node.value.id == "wp_client"):
            appelees.add(node.attr)
publiques = {d for d in definies if not d.startswith("_")}
# `get` et `post` sont des primitives internes utilisées par les autres helpers
mortes = publiques - appelees - {"get", "post", "get_posts_by_ids"}

print(f"fonctions définies dans wp_client : {len(definies)}")
print(f"  {sorted(definies)}")
print(f"\nappelées par les scripts : {sorted(appelees)}")

if manquantes:
    print("\nECHEC — appels vers des fonctions inexistantes :")
    for m in manquantes:
        print(f"  - {m}")
if mortes:
    print(f"\nAttention — fonctions publiques jamais appelées : {sorted(mortes)}")
if not manquantes and not mortes:
    print("\nOK — le contrat entre les scripts et wp_client est complet, aucune fonction morte.")
sys.exit(1 if manquantes else 0)