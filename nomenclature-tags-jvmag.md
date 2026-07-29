# Nomenclature des tags — JVMag (v3.11)

**But unique des tags :** nourrir la recherche et la reco de l'app via un maillage dense.
Un tag vaut par les liens qu'il crée. Cible : **8–10 tags / article** (moins pour les news courtes,
agendas et programmes — c'est normal).
**Catégories WordPress : on n'y touche pas.** Tags uniquement.

Ce fichier est la seule source de vérité pour les règles (vocabulaire fermé inclus). Il n'a plus
de suffixe de version dans son nom : les évolutions se suivent via le **Changelog** ci-dessous,
pas via un renommage de fichier. L'historique concret (exemples par lot) vit dans
[liste-maitresse-tags-jvmag.md](liste-maitresse-tags-jvmag.md) — ce document-ci ne garde que les
règles actives.

## Changelog
- **v3.11** (2026-07-29, audit général) : remplacement du checklist auteur + de l'ancienne
  "Étape de proposition" (redondants entre eux) par une **Grille de tagging obligatoire** unique,
  à parcourir intégralement pour chaque article — objectif : ne plus jamais sauter une facette
  (§5 en particulier a été manquée deux fois avant cette version). Ajout de la règle **produit
  dérivé** (§2) : licence/marque taguée, jamais le genre du jeu source. Vocabulaire fermé (§3–§6)
  trié alphabétiquement. `Xbox Showcase` corrigé en `Xbox Games Showcase` (vrai nom du tag WP).
- **v3.10** (2026-07-29, pilote lot #6) : `Montre connectée` ajouté au vocabulaire fermé (§4).
  Exception précisée à la règle "listes = pas de tags" (Règles transversales) : une courte liste
  (≤5) d'éléments qui deviennent chacun concrètement disponibles a un impact de reco réel et se
  tague individuellement — distinct d'une liste longue ou d'une intention/projet futur.
- **v3.9** (2026-07-29, pilote lot #5) : `Gratuit` retiré du vocabulaire fermé (§5) — le prix n'est
  pas un connecteur éditorial fiable pour la reco (deux jeux gratuits n'ont souvent rien en commun),
  contrairement à `Indé`/`Rétro` qui identifient une vraie scène/communauté. Clarification de la
  règle *vedette-hook* (§1) : distinction entre une personne qui EST l'angle éditorial (Tupac,
  Josh Hartnett) et une personne qui apparaît dans la couverture d'une œuvre déjà nommée/taguée
  sans être elle-même le sujet (Johnny Depp dans un article sur le trailer de Scrooge).
- **v3.8** (2026-07-29, pilote lot #4) : `Sport` précisé comme genre à utiliser pour les jeux de
  trick/scoring type skateboard (§3). Décision de ne PAS ajouter de genre `Rally` distinct de
  `Course` — loggée dans le journal, pas un changement de vocabulaire.
- **v3.7** (2026-07-29, pilote lot #3) : nouvelle règle *personne taguée + son œuvre-signature*
  (§1) — distincte du pedigree d'équipe, toujours exclu ; ajout de `San Diego Comic-Con` aux
  événements fermés (§6).
- **v3.6** (2026-07-29, pilote lot #2) : `Rétro` recadré au rétro-gaming uniquement (§5) ; rappel
  explicite de vérifier §5 (univers/thème) pour les JEUX aussi, pas seulement les films (§5) ;
  précision sur le nommage des enseignes locales, avec nettoyage d'un tag de ville hérité (§7).
- **v3.5** (2026-07-29, pilote lot #1 post-automatisation) : ajout du principe *trait stable vs
  fait contextuel* (§ Règles transversales) ; distinction service/abonnement vs plateforme (§2) ;
  affinage de la règle Suisse avec un cas négatif (§7) ; gouvernance mise à jour pour un accès API
  live plutôt qu'une liste maîtresse tenue à la main (§ Gouvernance).
- **v3.4** : finale après pilote de 50 articles (voir historique git pour le détail antérieur).

---

## Grille de tagging obligatoire

**À parcourir intégralement, dans l'ordre, pour CHAQUE article, sans exception.** Pour chaque
ligne : soit un tag est posé, soit on note explicitement pourquoi elle ne s'applique pas (ne
jamais passer une ligne sous silence). C'est le seul document de travail pour proposer un lot —
il remplace tout autre résumé ou checklist condensé.

| # | Facette | Où | Question à trancher |
|---|---------|-----|----------------------|
| 1 | Licence/sujet | §1 OUVERT | Œuvre/franchise/produit identifiable ? Forme canonique (sans numéro/adjectif) ? |
| 2 | Personne | §1 OUVERT | Personne réelle = sujet ou vedette-hook ? Si oui : œuvre-signature à tagger aussi (sauf si l'œuvre du moment est déjà taguée par ailleurs, voir §1) ? |
| 3 | Studio/éditeur/marque | §2 OUVERT | Studio dev cité ? Éditeur first-party majeur ? **Produit dérivé** (jouet, figurine, produit dérivé) → licence/marque oui, genre du jeu source NON (voir §2) |
| 4 | Genre | §3 FERMÉ | Cité dans le texte, OU trait stable d'une licence connue (jamais pour un produit dérivé, voir #3) ? |
| 5 | Plateforme/composant | §4 FERMÉ | Cité explicitement dans le texte — fait contextuel, ne se déduit **jamais** ? |
| 6 | Thème/univers | §5 semi-fermé | **Systématique dès qu'une licence est taguée en #1** : trait stable de cette licence (même non cité) OU thème explicite dans le texte ? Ne jamais laisser cette ligne vide sans y avoir réfléchi. |
| 7 | Mécaniques revendiquées | §5 | Solo/Multi/Coop/Compétitif/En ligne/Local/Cross-play/Monde ouvert — seulement si réellement décrites, pas juste théoriquement possibles ? |
| 8 | Qualificatif permanent | §5 | Indé/Remake/Remaster/Rétro/Esport/Animation, si applicable ? |
| 9 | Automobile | §5bis | Voiture réelle = sujet ? (jamais pour un jeu de course → `Course` en #4) |
| 10 | Événement | §6 FERMÉ | Un événement de la liste est-il le contexte de l'annonce ? |
| 11 | Local suisse | §7 FERMÉ | Angle suisse réel et impactant (pas une mention comparative) ? |
| 12 | Pays | §8 OUVERT | Un pays est-il l'acteur central (jamais une mention incidente) ? |

**Après la grille, vérifier les exceptions transversales** (détail dans la section dédiée
ci-dessous) : liste d'éléments (§ Listes = pas de tags, sauf exception ≤5 concrète) ; médium déjà
couvert par la catégorie (sauf `Cinéma`) ; comparaison ou mention anecdotique (jamais taguées) ;
aucune variante (casse/accent/pluriel/tiret) du tag n'existe déjà dans le snapshot du lot.

Sortie par article : `{ "tags": [...], "nouveaux_tags": [...], "incertitudes": [...] }`

---

## §1 — Licences / sujets — OUVERT
- **Franchise sans numéro ni adjectif.** Red Dead Redemption 2 → `Red Dead Redemption` ;
  Final Fantasy VII Revelation → `Final Fantasy` ; Alien Isolation 2 → `Alien`.
  → La différenciation interne se fait par les **genres** (`Final Fantasy` + `MMO` = FF XIV ;
  `Final Fantasy` + `Action-RPG` = le remake FF7). Pas de double franchise+sous-saga.
  → Bonus cross-media : `Alien` relie le jeu ET le film ET la série.
- **Œuvre citée en comparaison ≠ tag** (« à la sauce God of War » → pas de tag).
- **Personne = sujet → taguée** (interview, portrait, nécro, news de casting qui porte sur elle).
- **Rôle central tagué, mention anecdotique non.**
- **Personne réelle en vedette taguée si elle est le hook** (Tupac & Snoop Dogg dans un jeu).
  → Distinguer : la personne EST l'angle éditorial de l'article (Tupac/Snoop Dogg dans un jeu,
  Josh Hartnett nommé au titre d'un article sur SA série) vs. la personne apparaît dans la
  couverture d'une œuvre déjà nommée et taguée, sans être elle-même le sujet (ex. Johnny Depp dans
  un article sur le trailer de `Scrooge` — le film est le sujet, pas l'acteur → pas de tag
  personne dans ce cas).
- **Personne taguée + son œuvre-signature** : si la personne est taguée comme sujet et que sa
  notoriété repose sur une œuvre/franchise précise et largement identifiée par le public (ex.
  Dan Houser → `Grand Theft Auto` + `Rockstar Games`), on tague aussi cette œuvre/franchise, même
  si l'article n'en parle pas directement. But : sans ça, l'article n'est quasiment jamais
  recommandé à un lecteur fan de cette œuvre — un tag uniquement "personne" est trop rare sur
  +10 000 articles pour nourrir la reco. Différent du **pedigree d'équipe** (ex. « l'équipe de
  Yakuza » sur un jeu sans rapport), qui reste exclu car trop diffus, sans porte-parole identifié.

## §2 — Studios / éditeurs / marques — OUVERT
- Règle « acteur le plus **utile** » : God of War → Santa Monica Studio.
- **Studio dev toujours + éditeur first-party majeur** s'il est une marque-source suivie
  (Xbox Game Studios, PlayStation Studios, Nintendo, SEGA, Square Enix…). NB : le tag plateforme
  (`Xbox`) ≠ l'éditeur (`Xbox Game Studios`) — l'un = dispo, l'autre = curation first-party.
- **Service/abonnement ≠ plateforme** : même logique que l'éditeur vs la plateforme. Un service
  comme `PlayStation Plus` se tague en plus de, jamais à la place de, la plateforme qu'il utilise
  (`PlayStation`). Ex. : news sur les jeux du mois PS Plus → `PlayStation` + `PlayStation Plus`.
- **Marque/studio obscur : tagué s'il EST le sujet** (Ventiva) ; ignoré s'il est secondaire.
- Pas de studio connu mentionné → tague les **autres jeux du même créateur** (pont d'auteur).
- **Pedigree non tagué** : anciens employeurs / équipe d'origine ≠ tag (Bioware/ND/343 ;
  « l'équipe de Yakuza »).
- **Marque selon ce que dit l'article**, pas selon ce qu'elle est : sponsor cité au titre mais
  absent du corps → non tagué.
- **Produit dérivé (jouet, figurine, produit licencié)** : on tague la licence/marque (ex. `LEGO`
  + `Donkey Kong` + `Nintendo` ; `Hasbro` + `The Legend of Zelda`), mais **jamais le genre du jeu
  source** — le sujet de l'article est l'objet dérivé, pas le jeu. Exception : si le contenu de
  l'article lui-même porte sur l'histoire/l'univers du jeu d'origine (ex. rétrospective arcade),
  les traits vraiment couverts par le texte restent taguables (ex. `Rétro` si l'article parle de
  nostalgie/histoire du jeu, pas parce que le jouet existe).

## §3 — Genres — FERMÉ (triés alphabétiquement)
Action · Action-aventure · Action-RPG · Aventure · Battle royale · Beat'em up · Combat · Cosy ·
Course · Deckbuilder · FPS · Gestion · Hack'n'slash · Idle · Infiltration · JRPG · Metroidvania ·
MMO · Narratif · Party game · Plateforme · Point & click · Réflexion · Roguelike · RPG · Rythme ·
Shoot'em up · Simulation · Souls-like · Sport · Stratégie · Survie · Tactique · Tower defense · TPS
*Film/série :* Action · Aventure · Biopic · Comédie · Documentaire · Drame · Fantastique ·
Horreur · Policier · Science-fiction · Thriller (+ `Animation` si pas d'acteurs réels).
**`Sport` couvre aussi les jeux de trick/scoring type skateboard/rollers/BMX** (Denshattack!,
Tony Hawk's Pro Skater, OlliOlli World, Skate Story) — pas de genre dédié "Skate" pour éviter un
tag de niche peu réutilisé ; `Sport` est le plus proche et correspond au classement standard de
l'industrie pour ce type de jeu.

## §4 — Plateformes & matériel — FERMÉ (triés alphabétiquement)
**On liste chaque plateforme réelle.** Pas de collectif « Console ». Pas de numéro.
**Jeux :** Cloud gaming · Mobile · Nintendo Switch · PC · PlayStation · Rétro · Steam Deck · VR · Xbox
*(`Rétro` ici = jeu/console d'époque, pas "vieux" au sens large — un CPU ou un produit qui fête un
anniversaire n'est pas rétro-gaming.)*
**Films/séries :** Apple TV+ · Canal+ · Crunchyroll · Disney+ · HBO Max · Netflix · Paramount+ ·
Prime Video
**Composants & matériel :** Alimentation · AR · Boîtier · Carte graphique · Carte mère ·
Casque audio · Clavier · Écran · Matériel PC · Montre connectée · Périphérique · Processeur · RAM ·
Refroidissement · Réseau · Smartphone · Souris · SSD

## §5 — Thèmes & univers — semi-fermée (le moteur du maillage, listes triées alphabétiquement)
**Systématique, jeux comme films/séries (voir Grille #6)** : un jeu au cadre spatial/fantasy/etc.
se tague en univers même si l'article se concentre sur le gameplay/genre (ex. `BioEden` → cadre
spatial → `Science-fiction` + `Espace`, en plus de `Simulation`/`Gestion`). C'est la facette la
plus souvent oubliée si on ne la vérifie pas explicitement à chaque article.
**Admission (3 tests) :** factuel + définissant + **revendiqué par le lecteur** (« j'aime les ___ »).
**Univers / cadre :** Années 80 · Aviation · Cyberpunk · Dinosaures · Enquête · Espace · Fantasy ·
Far West · Guerre · Guerre froide · Horreur · IA · Lovecraftien · Maritime · Médiéval ·
Mythologie · Pirates · Post-apocalyptique · Robot · Science-fiction · Steampunk · Super-héros ·
WW1 · WW2 · Zombies
**Mécaniques revendiquées :** Compétitif · Coopératif · Cross-play · En ligne · Local ·
Monde ouvert · Multijoueur · Solo
**Qualificatifs permanents :** Animation · Esport · Indé · Remake · Remaster · Rétro
*(`Rétro` = contenu rétro-gaming, voir note §4 — pas un synonyme de "ancien/nostalgique".)*
**`Gratuit` retiré (v3.9)** : le prix n'est pas un connecteur éditorial fiable — deux jeux gratuits
n'ont souvent rien en commun (contrairement à `Indé`/`Rétro`, qui identifient une vraie
scène/communauté suivie). Ne pas retaguer.
**Métiers / sujets :** Doublage · Cinéma
**Rubriques éditoriales (suivies par le lecteur) :** Carnet noir · Montage PC

**EXCLUS :**
- **Ton / ambiance** (Sombre, Mélancolique, Stressant, Épique) → interprétatif.
- **Statut / format** (Démo, Bande-annonce, Teaser, Accès anticipé, AAA, **Reboot**, **Exclusivité**)
  → transitoire/subjectif. *(Remaster/Remake restent : nature permanente.)*
- **Techniques de production & styles graphiques** (Procédural, Ray tracing, moteurs, **Pixel art**,
  voxel, self-shading, cel-shading) → invisibles / non revendiqués.

## §5bis — Automobile — sujet RÉEL uniquement
`Voiture` (générique) · `Voiture hybride` · `Voiture électrique`. Chaque voiture = `Voiture` +
sa motorisation. **Les jeux de voiture/course se taguent via le genre `Course`**, jamais `Voiture`.

## §6 — Événements — FERMÉ (triés alphabétiquement)
Evergreen (l'année vit dans la date). Un événement terminé garde son tag.
**Jeux vidéo :** Gamescom · Nintendo Direct · Paris Games Week · Polymanga ·
Red Bull Gamerations · State of Play · Summer Game Fest · The Game Awards · Xbox Games Showcase
*(le tag réel sur le site est `Xbox Games Showcase`, pas `Xbox Showcase` — corrigé ici pour
matcher la réalité, 12 articles déjà taggés ainsi.)*
**Tech / auto :** CES · Computex · Goodwood Festival of Speed · WWDC
**Ciné / pop culture :** Festival de Cannes · Oscars · San Diego Comic-Con
*(San Diego Comic-Con peut aussi porter des annonces jeux vidéo, à la manière de Gamescom — reste
classé ici car son identité dominante est pop culture/ciné/séries.)*

## §7 — Local suisse — FERMÉ (un seul tag)
**`Suisse`** dès qu'il y a un **angle suisse réel** (sujet local, événement en Suisse,
lancement/prix spécifiquement suisse) — pas pour une simple dispo mondiale. **Pas de tags de ville.**
**Cas négatif :** une phrase qui mentionne la Suisse pour dire qu'elle **n'est PAS touchée** par un
problème qui frappe d'autres pays (« en Suisse tout fonctionne normalement ») n'est **pas** un
angle suisse réel — ce n'est qu'une précision de contexte, pas le sujet. Ne taguer `Suisse` que si
le pays est réellement concerné/impacté par ce dont parle l'article.
**Enseignes locales (cinéma, salle, lieu) :** on tague le **nom de l'enseigne** (`ARENA Cinemas`,
`Cinémas de Sierre`), jamais la ville seule (`Sierre`) — c'est la même règle que "pas de tags de
ville", juste avec l'enseigne en OUVERT (§ licences/marques) + `Suisse` en plus. Si un tag de ville
brut traîne dans l'historique du site, le corriger : retagger les articles concernés avec la bonne
enseigne puis supprimer le tag de ville (`scripts/wp_client.py::delete_tag`).

## §8 — Pays — OUVERT, barrière stricte
Un pays n'est tagué **que s'il est l'acteur central** (« la Chine légifère », « ventes au Japon »),
jamais pour une mention incidente.

---

## Règles transversales

Exceptions et principes qui s'appliquent après avoir parcouru la Grille, pas facette par facette.

- **Trait stable vs fait contextuel** : un trait stable de l'œuvre (genre, univers/thème) peut être
  déduit d'une licence connue même si le texte ne le cite pas explicitement — c'est le même
  principe que la désambiguïsation `Final Fantasy` + `MMO` = FF XIV / `Final Fantasy` +
  `Action-RPG` = le remake FF7 (§1). Un fait contextuel (plateforme dispo, événement, chiffres,
  pays concerné) ne se déduit **jamais** de la connaissance générale du sujet : il doit être dit
  par le texte, sinon → incertitude. Le test : est-ce que ce trait resterait vrai pour n'importe
  quel article parlant de cette œuvre (stable), ou est-ce que ça dépend de CET article précis
  (contextuel) ? Ne s'applique jamais à un produit dérivé (§2).
- **Tag large vs catégorie** : on ne tague pas le médium si la catégorie le dit déjà
  (pas de `Série` en News Séries). Exception `Cinéma` (thème transversal salle/industrie/festival —
  pas sur chaque film précis).
- **Listes = pas de tags** : nominés, jeux-épreuves, programmes, line-up → on ne tague que le sujet.
  **Exception** : une liste **courte (≤ 5)** d'éléments qui deviennent chacun **concrètement et
  individuellement disponibles/accessibles** (ex. 4 jeux qui rejoignent un programme de
  rétrocompatibilité) → on tague chaque élément, l'impact de reco est réel et immédiat pour
  chacun. Une liste plus longue, ou qui évoque une intention/un projet futur (10 jeux à adapter en
  films, jeux du mois d'un abonnement) reste non taguée individuellement.
- **SF spatial** → `Science-fiction` + `Espace` quand l'espace est central.
- **Pas de tag `Adaptation`** : le jeu et son film partagent simplement la franchise.
- **Facette contextuelle absente → incertitudes** : si une facette contextuelle clé manque
  (plateforme non citée notamment), le pipeline le signale pour complément humain — il n'invente
  pas. Ne s'applique pas aux traits stables (voir ci-dessus), qui se déduisent normalement.
- **Nommage** : facettes fermées = on pioche ; une forme canonique unique (casse/accent/pluriel) ;
  singulier par défaut ; un tag = une entité/concept.

---

## Gouvernance & pipeline (verrou anti-dérive)
Le pipeline (`scripts/fetch_batch.py` + `scripts/apply_batch.py`) est opérationnel depuis le lot #1
(2026-07-29). **Il n'y a plus de liste maîtresse tenue à la main pour les facettes OUVERTES** :
`fetch_batch.py` interroge `/wp-json/wp/v2/tags` et `/wp-json/wp/v2/categories` en direct à chaque
lot et embarque ce snapshot dans le fichier exporté — le vocabulaire ouvert existant est donc
toujours à jour, sans entretien. Le vocabulaire **FERMÉ** (§3 à §8 ci-dessus), lui, reste défini
uniquement dans ce document : ce n'est pas un inventaire de ce qui existe déjà sur le site (des
tags fermés valides, comme `Cross-play` ou `Disney+`, peuvent très bien n'avoir jamais été utilisés
avant d'être posés pour la première fois), c'est une politique éditoriale.

`liste-maitresse-tags-jvmag.md` a changé de rôle en conséquence : ce n'est plus un inventaire, mais
le **journal des lots traités** (décisions prises, nouveaux tags créés, cas litigieux tranchés).

1. Facettes **fermées** : on pioche dans ce document, on n'invente **jamais**.
2. Facettes **ouvertes** : réutiliser la forme **exacte** trouvée dans le snapshot du lot ; vérifier
   les variantes (casse/accent/pluriel/tiret) avant de proposer un nouveau tag.
3. **Un nouveau tag n'est jamais écrit direct** : il sort dans `nouveaux_tags`, validé par l'humain
   avant que `apply_batch.py` ne l'écrive dans WordPress.
4. Après validation d'un lot, reporter dans ce document toute règle nouvelle qui s'est révélée
   nécessaire (comme les amendements ci-dessus) et logger le lot dans `liste-maitresse-tags-jvmag.md`.
5. **Chaque proposition de lot part de la Grille de tagging obligatoire** (ci-dessus), parcourue
   intégralement pour chaque article — entrée : le TEXTE INTÉGRAL, la CATÉGORIE et le snapshot des
   tags/catégories existants, tous fournis par `batch_XXXX.json`.
