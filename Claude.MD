# Instructions pour Claude Code — pipeline de tagging JVMag

Ce fichier fixe le **workflow** (quoi lire, quoi produire, dans quel format). Les
**règles de tagging elles-mêmes** (vocabulaire, Grille, cas particuliers) vivent dans
`regles-tagging-actives.md` — c'est l'unique fichier à lire pour savoir *comment*
tagger un article. Ne jamais lire `changelog-nomenclature.md` pendant l'exécution d'un
lot : c'est un historique destiné aux sessions de calibration humaine, pas à
l'exécution.

## Séquence d'un lot

1. L'humain lance `python scripts/fetch_batch.py --size N`, qui écrit
   `batches/batch_XXXX.json` (texte intégral + catégorie + tags/catégories existants
   par article).
2. Claude Code lit `regles-tagging-actives.md` en entier, puis `batches/batch_XXXX.json`.
3. Pour **chaque article** du lot, parcourir intégralement la Grille de tagging
   obligatoire (les 12 lignes, dans l'ordre, sans en sauter aucune).
4. Produire un fichier `batches/batch_XXXX_proposed.json` — le lot proposé, pas encore
   validé par l'humain (voir format ci-dessous).
5. L'humain relit et corrige `batch_XXXX_proposed.json`, le renomme/copie en
   `batch_XXXX_reviewed.json` une fois qu'il est satisfait.
6. L'humain lance `python scripts/apply_batch.py batches/batch_XXXX_reviewed.json`,
   qui écrit sur WordPress et archive dans `tag_provenance.jsonl`.

Claude Code ne doit **jamais** appeler `apply_batch.py` lui-même : l'écriture sur
WordPress est un acte humain, après relecture. Le rôle de Claude Code s'arrête à la
production du fichier `_proposed.json`.

## Format de sortie attendu — `batch_XXXX_proposed.json`

Liste d'objets, un par article du lot d'entrée, dans le même ordre :

```json
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
    ],
    "incertitudes": [
      "Studio dev non cité, titre trop peu documenté pour recherche ciblée fiable"
    ]
  }
]
```

- **`tags`** : uniquement des noms qui existent déjà dans `tags_existants` (snapshot
  fourni dans le batch d'entrée). Un nom qui n'existe pas encore ne doit **jamais**
  apparaître ici — il va dans `nouveaux_tags`.
- **`nouveaux_tags`** : candidats à un tag qui n'existe pas encore sur WordPress.
  L'humain les valide un par un avant que quoi que ce soit ne soit écrit — Claude Code
  ne décide jamais seul de créer un tag.
- **`grille_line`** : le numéro de ligne de la Grille (1 à 12) qui a produit ce tag —
  obligatoire sur chaque tag, `tags` comme `nouveaux_tags`. C'est ce qui permettra plus
  tard à l'app de distinguer un tag d'identité (lignes 1, 2, 3, 12) d'un tag de facette
  de contenu (lignes 4 à 11) dans le calcul du score de recommandation. Un tag sans
  `grille_line` est un lot mal formé : ne jamais l'omettre, même quand la ligne semble
  évidente.
- **`incertitudes`** : liste de strings en langage naturel, une par doute non résolu
  (facette non déduite faute d'info dans le texte, ambiguïté non tranchée). Champ
  optionnel — absent ou vide si le lot ne soulève aucun doute pour cet article.

## Rappels de posture (résumé — le détail est dans regles-tagging-actives.md)

- Vocabulaire **FERMÉ** (lignes 4-11) : on pioche dans la liste donnée, on n'invente
  jamais, même un cas qui semble légitime.
- Vocabulaire **OUVERT** (lignes 1, 2, 3, 12) : réutiliser la forme exacte trouvée dans
  `tags_existants` du batch avant de proposer un nouveau tag — vérifier les variantes
  de casse/accent/pluriel/tiret.
- Relire le texte une seconde fois avant de conclure qu'une facette ne s'applique pas.
- Un fait contextuel (plateforme, mécanique, événement, pays) ne se déduit jamais de
  la notoriété générale du sujet — seul un trait stable (genre, univers/thème d'une
  œuvre qui EST le sujet) peut l'être.