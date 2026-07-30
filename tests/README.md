# Tests du pipeline de tagging

Aucune dépendance de test à installer, aucun accès réseau : les tests remplacent la
couche HTTP de `wp_client` par un faux WordPress en mémoire. Ils ne touchent jamais au
vrai site.

À lancer depuis la racine du repo.

## `test_contrat.py` — à lancer avant chaque commit

```
python tests/test_contrat.py
```

Vérifie que chaque `wp_client.X()` appelé par les scripts existe réellement dans
`wp_client.py`, et signale les fonctions publiques jamais appelées.

Ce test existe pour une raison précise : supprimer par accident la ligne
`def ma_fonction():` laisse son corps comme code orphelin après un `return`, ce qui
reste **syntaxiquement valide**. Un contrôle de syntaxe ne voit rien, et le pipeline ne
plante qu'à l'exécution, sur le premier article traité. C'est arrivé.

## `test_cursor.py` — non-régression du parcours du catalogue

```
python tests/test_cursor.py
```

Simule le tagging complet d'un catalogue de 13 000 articles et vérifie que le curseur
de date permet bien de tout parcourir, sans jamais rendre un lot vide prématurément.
Teste aussi le cas des horodatages identiques (import en masse) et la détection propre
de la fin du catalogue.

Repère : le catalogue entier doit être traité en ~1 requête API par lot. Sans curseur,
le scan s'arrêtait à 2 000 articles.

## `test_fromtop.py` — non-régression du mode `--from-top`

```
python tests/test_fromtop.py
```

Vérifie que `--from-top` rattrape bien les articles publiés récemment, **sans** faire
perdre la position dans le backlog, et que le mode reprise repart ensuite au bon
endroit.

## `test_parse_ids.py` — non-régression du parsing `--ids`

```
python tests/test_parse_ids.py
```

Vérifie `fetch_batch.parse_ids()` sur une liste réaliste de 131 IDs inline (~650
caractères) : `Path(raw).exists()` levait une `OSError` (nom de fichier trop long) au
lieu de renvoyer `False`, donc le script plantait avant de rien faire dès qu'on lui
donnait un vrai lot d'IDs à re-tagger. Couvre aussi virgules/espaces/fichier/token
invalide/liste vide.

## `test_list_params.py` — non-régression du paramètre `include`

```
python tests/test_list_params.py
```

Vérifie que `wp_client.get()` joint une valeur liste (ex. `include=[1,2,3]`) en chaîne
séparée par des virgules avant l'envoi. `requests` sérialise sinon une liste en clé
répétée (`include=1&include=2&include=3`), et PHP côté WordPress ne garde que la
**dernière** occurrence d'une clé répétée sans crochets : `get_posts_by_ids()` sur 19
IDs réels n'en retournait qu'un seul, silencieusement. `fake_wp.py` ne peut pas
attraper ce bug (il ne modélise pas cette sérialisation HTTP + ce comportement PHP),
d'où ce test dédié qui vérifie le mécanisme du correctif directement.

## `test_pairings.py` — non-régression des paires de tags obligatoires

```
python tests/test_pairings.py
```

Vérifie `apply_batch.validate_pairings()` : composant PC interne sans `Matériel PC`,
matériel externe sans `Périphérique`, `Coopératif`/`Compétitif` sans `Multijoueur`. Ces
règles (§4 et Grille #7 de `regles-tagging-actives.md`) sont mécaniques et sans
exception, contrairement aux paires studio/éditeur du §2 — un script peut donc les
garantir de façon fiable. C'est arrivé : `Carte graphique` posé sans `Matériel PC` sur
un article DLSS 5, repéré seulement après coup.

## `fake_wp.py`

Faux WordPress utilisé par les deux simulations. Reproduit la sémantique de l'API
réelle pour `before`, `page` et `per_page`.