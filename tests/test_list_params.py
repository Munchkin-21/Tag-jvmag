"""Non-régression : wp_client.get() avec un paramètre de type liste (ex. `include`).

`requests` sérialise une valeur liste en clé répétée (`include=1&include=2&include=3`),
jamais en chaîne jointe par des virgules. Côté WordPress, PHP ($_GET) ne garde que la
DERNIÈRE occurrence d'une clé répétée sans crochets : l'API ne voyait donc qu'un seul ID
au lieu de tous, silencieusement (pas d'erreur, juste un résultat tronqué à 1 élément).
C'est arrivé : `get_posts_by_ids()` sur 19 IDs réels ne retournait que le dernier —
attrapé seulement parce qu'il a été testé contre le vrai WordPress avant le retag, pas
par la suite de tests (fake_wp.py ne modélise pas cette sérialisation HTTP + ce
comportement PHP, donc ne peut pas l'attraper).

Ce test vérifie le mécanisme du correctif directement : n'importe quelle valeur liste
passée à wp_client.get() doit arriver côté session HTTP comme une chaîne jointe par des
virgules, jamais comme la liste Python d'origine.
"""
import sys

sys.path.insert(0, "scripts")
import wp_client

captured = {}


class FakeResp:
    def __init__(self):
        self.status_code = 200
        self.headers = {}

    def json(self):
        return []

    def raise_for_status(self):
        pass


class FakeSession:
    def get(self, url, params=None, timeout=None):
        captured["params"] = params
        return FakeResp()


wp_client._session = lambda: FakeSession()

wp_client.get("posts", include=[114278, 114268, 114273], _fields="id,tags")

failures = []
value = captured["params"].get("include")
if isinstance(value, (list, tuple, set)):
    failures.append(f"'include' est encore une liste Python ({value!r}) au lieu d'une chaîne jointe.")
elif value != "114278,114268,114273":
    failures.append(f"'include' mal joint : {value!r}")
else:
    print(f"OK  include jointe correctement : {value!r}")

# Une valeur scalaire (cas normal, ex. `page`) ne doit pas être touchée.
if captured["params"].get("_fields") != "id,tags":
    failures.append(f"'_fields' (scalaire) altéré à tort : {captured['params'].get('_fields')!r}")
else:
    print("OK  paramètre scalaire non affecté")

if failures:
    print("\nECHEC :")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("\nOK — les paramètres de type liste sont joints en chaîne avant l'envoi.")
