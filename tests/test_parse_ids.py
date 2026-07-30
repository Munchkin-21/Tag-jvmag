"""Non-régression : fetch_batch.parse_ids() avec une longue liste d'IDs inline.

Path(raw).exists() lève OSError (ENAMETOOLONG) au lieu de renvoyer False quand `raw`
dépasse la limite de nom de fichier de l'OS (~255 caractères) — ce qui arrive
justement avec une liste réaliste d'IDs pour le re-tagging rétroactif (131 IDs
séparés par des virgules font ~650 caractères). C'est arrivé : le script plantait
avant de rien faire sur le premier essai avec le vrai lot d'IDs à retraiter.
"""
import sys
from pathlib import Path

sys.path.insert(0, "scripts")
import fetch_batch as fb

failures = []


def check(label, fn, expect_error=False):
    try:
        result = fn()
        if expect_error:
            failures.append(f"{label} : attendu une erreur, obtenu {result!r}")
        else:
            print(f"OK  {label} -> {result}")
    except ValueError as e:
        if expect_error:
            print(f"OK  {label} -> ValueError propre : {e}")
        else:
            failures.append(f"{label} : ValueError inattendue -> {e}")
    except Exception as e:
        failures.append(f"{label} : {type(e).__name__} inattendue -> {e}")


# Le cas réel qui a planté : 131 IDs, ~650 caractères, largement au-delà de la limite
# de nom de fichier de l'OS.
ids_131 = ",".join(str(1000 + i) for i in range(131))
check("131 IDs inline (cas réel)", lambda: fb.parse_ids(ids_131))

check("virgules", lambda: fb.parse_ids("123,456,789"))
check("espaces", lambda: fb.parse_ids("123 456 789"))
check("mix virgule+espace", lambda: fb.parse_ids("123, 456,  789"))

tmp = Path("/tmp/test_parse_ids_file.txt")
tmp.write_text("111\n222\n333\n")
check("fichier", lambda: fb.parse_ids(str(tmp)))
tmp.unlink()

check("token non numérique", lambda: fb.parse_ids("123,abc,456"), expect_error=True)
check("liste vide", lambda: fb.parse_ids("   "), expect_error=True)

if failures:
    print("\nECHEC :")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("\nOK — parse_ids gère la liste réaliste de 131 IDs sans planter.")
