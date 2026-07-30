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

## `fake_wp.py`

Faux WordPress utilisé par les deux simulations. Reproduit la sémantique de l'API
réelle pour `before`, `page` et `per_page`.