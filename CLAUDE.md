# Instructions pour Claude Code — pipeline de tagging JVMag

Ce fichier fixe le **workflow** (quoi lire, quoi produire, dans quel format). Les
**règles de tagging elles-mêmes** (vocabulaire, Grille, cas particuliers) vivent dans
`regles-tagging-actives.md` — c'est l'unique fichier à lire pour savoir *comment*
tagger un article. Ne jamais lire `changelog-nomenclature.md` pendant l'exécution d'un
lot : c'est un historique destiné aux sessions de calibration, pas à l'exécution.

**La nomenclature n'est pas figée.** Elle évolue lot après lot, au fil des cas que le
corpus fait apparaître. Faire évoluer les règles fait partie du travail (voir
« Corriger un lot » ci-dessous) — ce n'est pas une exception à signaler, c'est le
fonctionnement normal.

## Séquence d'un lot

1. **L'humain** lance `python scripts/fetch_batch.py --size N`, qui écrit
   `batches/batch_XXXX.json` (texte intégral + catégorie + tags/catégories existants
   par article). Le scan reprend automatiquement où le précédent s'est arrêté et
   descend du plus récent vers le plus ancien ; `--from-top` repart des articles les
   plus récents pour rattraper les publications faites depuis le début du chantier.
   Un lot vide ou partiel n'est pas une anomalie : le message affiché indique s'il
   faut relancer pour continuer, ou si la fin du catalogue est atteinte.
2. **Claude Code** lit `regles-tagging-actives.md` en entier, puis
   `batches/batch_XXXX.json`.
3. Pour **chaque article** du lot, parcourir intégralement la Grille de tagging
   obligatoire (les 12 lignes, dans l'ordre, sans en sauter aucune).
4. **Claude Code** écrit `batches/batch_XXXX_proposed.json` — le lot proposé, pas encore
   validé (voir format ci-dessous).
5. **L'humain** relit et demande les corrections nécessaires (voir « Corriger un lot »).
6. **L'humain** copie le fichier corrigé en `batch_XXXX_reviewed.json`, puis lance
   `python scripts/apply_batch.py batches/batch_XXXX_reviewed.json`.
7. **Claude Code** consigne le lot dans `liste-maitresse-tags-jvmag.md` (tags posés,
   décisions prises, cas litigieux tranchés).

Claude Code ne doit **jamais** appeler `apply_batch.py` lui-même : l'écriture sur
WordPress est un acte humain, après relecture.

## Corriger un lot

Quand l'humain signale un tag qui ne convient pas, distinguer deux situations.

**Cas 1 — erreur ponctuelle** (mauvais tag sur cet article, oubli, faute de casse) :
corriger directement `batch_XXXX_proposed.json`. Aucune règle ne change.

**Cas 2 — le cas révèle une règle ambiguë, absente ou trop large** : c'est le mécanisme
normal d'évolution de la nomenclature. Alors :
1. Rédiger l'amendement et **le soumettre à l'humain avant de l'écrire** — il valide le
   texte de la règle, pas seulement l'intention.
2. Une fois validé : ajouter une entrée dans `changelog-nomenclature.md` (avec le
   raisonnement complet et le cas concret qui l'a motivé), **puis** répercuter dans
   `regles-tagging-actives.md` en **remplaçant directement** la règle concernée.
3. Ne jamais mettre de numéro de version, de date ou de mention « avant/après » dans
   `regles-tagging-actives.md` — ce fichier ne décrit que l'état présent. L'historique
   vit dans le changelog, et nulle part ailleurs.
4. Si l'amendement invalide des tags déjà posés sur des lots antérieurs, le signaler
   explicitement à l'humain plutôt que de le laisser passer : une correction rétroactive
   est parfois nécessaire.

En cas de doute sur la portée d'un amendement (est-ce que ça touche l'architecture, la
cohérence globale du vocabulaire, ou plusieurs sections à la fois ?), le dire plutôt que
de trancher seul.

## Re-tagging rétroactif

Les règles mûrissent lot après lot : les articles tagués tôt l'ont été avec une
nomenclature moins complète que ceux tagués plus tard. Repasser sur eux une fois les
règles stabilisées fait partie du chantier.

Un article déjà tagué est **invisible** pour le scan normal (`fetch_batch.py` ne
retourne que les articles à 0 ou 1 tag). Il faut donc le cibler explicitement :

```
python scripts/fetch_batch.py --ids 1234,5678          # ou un fichier, un ID par ligne
```

Ce mode ignore le curseur et `skip_ids` — un article déjà dans `processed` est bien
récupéré. Le lot contient `existing_tags` pour chaque article : **les lire avant de
proposer**, pour décider consciemment de ce qui est conservé et de ce qui tombe.

L'application se fait avec `--replace`, qui remplace l'ensemble des tags de l'article
au lieu de s'y ajouter — sans ça, un tag devenu faux resterait en place :

```
python scripts/apply_batch.py batches/batch_XXXX_reviewed.json --replace --dry-run
python scripts/apply_batch.py batches/batch_XXXX_reviewed.json --replace
```

`--dry-run` affiche les tags qui seraient retirés sans rien modifier. **Toujours le
lancer d'abord en mode re-tagging** et soumettre la liste des retraits à l'humain : un
tag absent du lot proposé disparaît définitivement de l'article, y compris s'il était
légitime et simplement oublié.

## Format de sortie attendu — `batch_XXXX_proposed.json`

Liste d'objets, un par article du lot d'entrée, dans le même ordre :

```json
[
  {
    "id": 123,
    "tags": ["Hitman", "IO Interactive", "PC", "Action", "Infiltration"],
    "nouveaux_tags": ["Nom Du Nouveau Tag"],
    "incertitudes": [
      "Studio dev non cité, titre trop peu documenté pour recherche ciblée fiable"
    ]
  }
]
```

- **`tags`** : uniquement des noms qui existent déjà dans `tags_existants` (snapshot
  fourni dans le batch d'entrée). Un nom qui n'existe pas encore ne doit **jamais**
  apparaître ici — il va dans `nouveaux_tags`. `apply_batch.py` refuse le lot entier si
  un nom de `tags` est introuvable sur WordPress (garde-fou anti-doublon).
- **`nouveaux_tags`** : candidats à un tag qui n'existe pas encore sur WordPress.
  L'humain les valide un par un avant que quoi que ce soit ne soit écrit — Claude Code
  ne décide jamais seul de créer un tag.
- **`incertitudes`** : liste de strings en langage naturel, une par doute non résolu
  (facette non déduite faute d'info dans le texte, ambiguïté non tranchée). Champ
  optionnel — absent ou vide si l'article ne soulève aucun doute. C'est le canal normal
  pour remonter ce qui manque : mieux vaut une incertitude explicite qu'un tag deviné.

## Rappels de posture (résumé — le détail est dans regles-tagging-actives.md)

- Vocabulaire **FERMÉ** (Grille lignes 4-11) : on pioche dans la liste donnée, on
  n'invente jamais, même un cas qui semble légitime. Un manque réel dans le vocabulaire
  fermé se traite comme un amendement (Cas 2 ci-dessus), pas comme un tag improvisé.
- Vocabulaire **OUVERT** (Grille lignes 1, 2, 3, 12) : réutiliser la forme exacte
  trouvée dans `tags_existants` du batch avant de proposer un nouveau tag — vérifier les
  variantes de casse/accent/pluriel/tiret.
- Relire le texte une seconde fois avant de conclure qu'une facette ne s'applique pas.
- Un fait contextuel (plateforme, mécanique, événement, pays) ne se déduit jamais de
  la notoriété générale du sujet — seul un trait stable (genre, univers/thème d'une
  œuvre qui EST le sujet) peut l'être.