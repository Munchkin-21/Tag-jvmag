# Règles de tagging — JVMag (règles actives)

> **Ce fichier est le seul document fourni à l'exécution d'un lot de tagging.**
> Il ne contient que l'état actuel des règles — jamais d'historique, de justification
> par version ou de raisonnement narratif. Le "pourquoi" de chaque règle vit dans
> `changelog-nomenclature.md`, un fichier séparé, à consulter uniquement en dehors
> de l'exécution d'un lot (calibration humaine, revue de règles).
>
> Toute modification de ce fichier se fait par **remplacement direct** de la règle
> concernée, ici. Ne jamais ajouter de mention de version, de date ou de "avant/après"
> dans ce document — ça appartient au changelog.

---

## Légende (à lire avant tout le reste)

- **Tag d'identité** (§1, §2, §8) : répond à *"de quelle œuvre/personne/marque/pays
  s'agit-il ?"*. Vocabulaire **OUVERT** (on peut créer un nouveau tag), forme canonique
  unique, validé par l'humain avant écriture sur WordPress. Peut être complété par une
  **recherche externe ciblée** dans les conditions strictes du §2.
- **Tag de facette de contenu** (§3, §4, §5, §5bis, §6, §7) : répond à *"de quoi CET
  article parle-t-il ?"*, jamais "qu'est-ce qui est vrai sur cette œuvre en général ?".
  Vocabulaire **FERMÉ** (on pioche uniquement dans la liste ci-dessous, on n'invente
  jamais) ou **semi-fermé** (§5 : liste fermée mais admission par test, voir §5).
  Jamais complété par recherche externe, même si le fait est notoire.
- **Trait stable vs fait contextuel** — distinction interne aux facettes de contenu :
  un trait stable (genre, univers/thème) peut être déduit d'une licence connue même non
  cité littéralement. Un fait contextuel (plateforme, mécaniques revendiquées,
  événement, pays) ne se déduit **jamais** : il doit être explicitement dans le texte,
  sinon → incertitude. Détail des deux catégories : voir "Règles transversales".

---

## Grille de tagging obligatoire

**À parcourir intégralement, dans l'ordre, pour CHAQUE article, sans exception.**
Pour chaque ligne : soit un tag est posé, soit on note explicitement pourquoi elle ne
s'applique pas (ne jamais passer une ligne sous silence). Relire le texte une seconde
fois avant de conclure qu'un mot-clé n'y est pas. C'est le seul document de travail
pour proposer un lot — il remplace tout autre résumé ou checklist condensé.

| # | Facette | Type | Où | Question à trancher |
|---|---------|------|-----|----------------------|
| 1 | Licence/sujet | Identité — OUVERT | §1 | Œuvre/franchise/produit identifiable ? Forme canonique (sans numéro/adjectif) ? |
| 2 | Personne | Identité — OUVERT | §1 | Personne réelle = sujet ou vedette-hook ? Si oui : œuvre-signature à tagger aussi (sauf si l'œuvre du moment est déjà taguée par ailleurs) ? |
| 3 | Studio/éditeur/marque | Identité — OUVERT | §2 | Studio dev cité ? Éditeur first-party majeur (trait stable) ? Non cité mais titre précis et non-ambigu → recherche ciblée autorisée (conditions strictes §2), sinon incertitude. Produit dérivé → licence/marque oui, genre du jeu source NON. |
| 4 | Genre | Contenu — FERMÉ | §3 | Cité dans le texte (relire une 2e fois), OU trait stable d'une licence connue (jamais pour un produit dérivé) ? |
| 5 | Plateforme/composant | Contenu — FERMÉ | §4 | Cité explicitement — fait contextuel, ne se déduit jamais. Composant PC interne → ajouter aussi `Matériel PC` ; matériel externe → ajouter aussi `Périphérique`. |
| 6 | Thème/univers | Contenu — semi-fermé | §5 | Systématique dès qu'une licence est taguée en #1 : trait stable de cette licence (même non cité) OU thème explicite dans le texte ? Ne jamais laisser cette ligne vide sans y avoir réfléchi. |
| 7 | Mécaniques revendiquées | Contenu — FERMÉ | §5 | Solo/Multi/Coop/Compétitif/En ligne/Local/Cross-play/Monde ouvert — seulement si réellement décrites. `Coopératif`/`Compétitif` ⇒ toujours `Multijoueur` aussi. Vérifier `En ligne` explicitement dès que serveurs/connexion/matchmaking sont mentionnés. |
| 8 | Qualificatif permanent | Contenu — FERMÉ | §5 | Indé/Remake/Remaster/Rétro/Esport/Animation, si applicable ? |
| 9 | Automobile | Contenu — FERMÉ | §5bis | Voiture réelle = sujet ? (jamais pour un jeu de course → `Course` en #4) |
| 10 | Événement | Contenu — FERMÉ | §6 | Un événement de la liste est-il le contexte de l'annonce ? |
| 11 | Local suisse | Contenu — FERMÉ | §7 | La Suisse est-elle l'acteur/lieu/sujet réel (pas juste un prix CHF ou une date CH donnés en routine) ? |
| 12 | Pays | Identité — OUVERT | §8 | Un pays est-il l'acteur central (jamais une mention incidente) ? |

**Après la grille, vérifier les exceptions transversales** : liste d'éléments (§ Listes
= pas de tags, sauf exception ≤5 concrète) ; médium déjà couvert par la catégorie
(sauf `Cinéma`) ; comparaison ou mention anecdotique (jamais taguées) ; aucune variante
(casse/accent/pluriel/tiret) du tag n'existe déjà dans le snapshot du lot.

**Sortie par article :** `{ "tags": [...], "nouveaux_tags": [...], "incertitudes": [...] }`

---

## §1 — Licences / sujets — Identité, OUVERT

- **Franchise sans numéro ni adjectif.** Red Dead Redemption 2 → `Red Dead Redemption` ;
  Final Fantasy VII Revelation → `Final Fantasy` ; Alien Isolation 2 → `Alien`.
  → La différenciation interne se fait par les genres (`Final Fantasy` + `MMO` = FF XIV ;
  `Final Fantasy` + `Action-RPG` = le remake FF7). Pas de double franchise+sous-saga.
  → Bonus cross-media : une ombrelle établie (ex. `Alien`) relie jeu/film/série — ne pas
  créer de tag séparé pour une série/spin-off dérivé quand l'ombrelle existe déjà.
  → **Sous-titre à retirer = seulement pour consolider une franchise multi-épisodes.**
  Un jeu unique et autonome dont le titre officiel complet inclut un sous-titre garde
  son titre entier : il n'y a rien à consolider, ce n'est pas un numéro de suite.
- **Œuvre citée en comparaison ≠ tag** (« à la sauce God of War » → pas de tag).
- **Personne = sujet → taguée** (interview, portrait, nécro, news de casting qui porte
  sur elle). Rôle central tagué, mention anecdotique non.
- **Personne réelle en vedette taguée si elle est le hook éditorial de l'article** —
  distinguer : la personne EST l'angle éditorial de l'article vs. la personne apparaît
  dans la couverture d'une œuvre déjà nommée et taguée, sans être elle-même le sujet
  (dans ce second cas → pas de tag personne).
- **Personne taguée + son œuvre-signature** : si la personne est taguée comme sujet et
  que sa notoriété repose sur une œuvre/franchise précise et largement identifiée par
  le public, on tague aussi cette œuvre/franchise, même si l'article n'en parle pas
  directement. But : un tag uniquement "personne" est trop rare sur +10 000 articles
  pour nourrir la reco. Différent du **pedigree d'équipe** (ex. « l'équipe de Yakuza »
  sur un jeu sans rapport), qui reste exclu car trop diffus, sans porte-parole identifié.
- **Trait stable réservé à l'œuvre qui EST le sujet** : le genre/univers d'une franchise
  ne se déduit (voir Règles transversales) que quand cette œuvre est elle-même le sujet
  de l'article. Quand le sujet est une personne qui a traversé cette œuvre dans sa
  carrière, l'œuvre se tague (lien pertinent pour la reco) mais pas son univers/thème —
  le lien est biographique, pas définissant. Ex. : Carnet noir Sam Neill →
  `Jurassic Park` oui, `Dinosaures` non.

## §2 — Studios / éditeurs / marques — Identité, OUVERT

- **Recherche ciblée d'identité** : quand un titre précis et non-ambigu est nommé dans
  le texte mais que son studio dev/éditeur n'y est pas explicite, une recherche externe
  ponctuelle est autorisée pour identifier ce studio/éditeur et compléter le tag — au
  même titre qu'une identification, pas un enrichissement de contenu. **Condition
  stricte** : n'appliquer que si une source unique confirme l'info sans ambiguïté ni
  contradiction (pas d'homonyme, pas de résultats divergents). En cas de doute, ne pas
  deviner — laisser en incertitude et signaler pour validation humaine. Réservé aux
  tags d'identité ; ne s'étend jamais aux tags de facette de contenu.
- Règle « acteur le plus utile » : God of War → Santa Monica Studio.
- **Studio dev toujours + éditeur first-party majeur** s'il est une marque-source
  suivie (Xbox Game Studios, PlayStation Studios, Nintendo, SEGA, Square Enix…). NB :
  le tag plateforme (`Xbox`) ≠ l'éditeur (`Xbox Game Studios`) — l'un = dispo, l'autre =
  curation first-party. Un article sur la structure actionnariale/éditoriale d'un
  studio (restructuration, licenciements) appelle l'éditeur, pas forcément une
  plateforme de sortie.
  **Paires systématiques actées :** `Rockstar Games` → toujours + `Take-Two
  Interactive` ; `The Coalition` → toujours + `Xbox Game Studios` ; `Obsidian
  Entertainment` → toujours + `Xbox Game Studios` ; `Bethesda Game Studios` → toujours
  + `Xbox Game Studios`. **Portée** : ces paires ne s'appliquent que quand le studio
  est tagué comme développeur/éditeur d'une œuvre précise dont parle l'article. Si le
  studio est tagué via la règle "personne + œuvre-signature" (ex. Dan Houser,
  cofondateur de Rockstar) — un lien biographique, pas la publication d'un jeu — la
  paire ne se déclenche pas : on tague le studio seul.
  **Pokémon :** le studio dev dépend du produit précis, jamais appliqué en bloc —
  `Niantic` pour Pokémon GO, `Game Freak` pour les jeux principaux. **Pas de paire
  `The Pokémon Company` / `Pokémon`** — tranché à l'usage : le nom est long, la
  distinction entité-juridique/franchise n'ouvre aucun angle de reco vraiment
  différent de `Pokémon` seul (contrairement à Rockstar/Take-Two, où studio créatif et
  maison-mère correspondent à deux curiosités lecteur réellement distinctes). Rester
  sur `Pokémon` seul, même quand l'entité est nommée explicitement dans le texte.
- **Service/abonnement ≠ plateforme** : même logique que l'éditeur vs la plateforme.
  Un service (`PlayStation Plus`) se tague en plus de, jamais à la place de, la
  plateforme qu'il utilise (`PlayStation`). **Un article qui décrit un accès gratuit/
  exceptionnel à une fonctionnalité du service reste tagué avec ce service**, tant que
  la fonctionnalité appartient techniquement à son infrastructure/marque — ne pas
  confondre « ne nécessite pas l'abonnement payant pour CETTE offre précise » avec
  « n'a aucun rapport avec le service » (ex. test de cloud gaming gratuit sans
  abonnement Game Pass : reste un service Xbox Game Pass, juste rendu accessible sans
  palier payant pour l'occasion).
- **Marque/studio obscur : tagué s'il EST le sujet** ; ignoré s'il est secondaire.
- Pas de studio connu mentionné → tague les autres jeux du même créateur (pont d'auteur).
- **Pedigree non tagué** : anciens employeurs / équipe d'origine ≠ tag.
- **Marque selon ce que dit l'article**, pas selon ce qu'elle est : sponsor cité au
  titre mais absent du corps → non tagué.
- **Produit dérivé** (jouet, figurine, produit licencié) : on tague la licence/marque
  (ex. `LEGO` + `Donkey Kong` + `Nintendo`), mais jamais le genre du jeu source — le
  sujet de l'article est l'objet dérivé, pas le jeu. Exception : si le contenu porte
  réellement sur l'histoire/l'univers du jeu d'origine, les traits vraiment couverts
  par le texte restent taguables.

## §3 — Genres — Contenu, FERMÉ (triés alphabétiquement)

Action · Action-aventure · Action-RPG · Aventure · Battle royale · Beat'em up ·
Combat · Cosy · Course · Deckbuilder · FPS · Gestion · Hack'n'slash · Idle ·
Infiltration · JRPG · Metroidvania · MMO · MOBA · Narratif · Party game · Plateforme ·
Point & click · Réflexion · Roguelike · RPG · Rythme · Shoot'em up · Simulation ·
Souls-like · Sport · Stratégie · Survie · Tactique · Tower defense · TPS

*Film/série :* Action · Aventure · Biopic · Comédie · Documentaire · Drame ·
Fantastique · Horreur · Policier · Science-fiction · Thriller (+ `Animation` si pas
d'acteurs réels).

`Sport` couvre aussi les jeux de trick/scoring type skateboard/rollers/BMX — pas de
genre dédié "Skate" pour éviter un tag de niche peu réutilisé.

**Genre cité comme nuance de ton ≠ genre à tagger.** Une formule du type « à la frontière
de X, Y et Z » ou « avec des accents de X » décrit une ambiance/un mélange, pas une
déclaration de genre — c'est une variante de l'exclusion "Ton / ambiance" (§5). Seul le
genre principal, assumé par le texte comme ce que l'œuvre EST, se tague. Ex. : un film
« à la frontière de la comédie, du fantastique et de l'horreur » qui reste par ailleurs
qualifié de comédie dans le reste du texte → `Comédie` + `Fantastique`, pas `Horreur`.

## §4 — Plateformes & matériel — Contenu, FERMÉ (triés alphabétiquement)

On liste chaque plateforme réelle. Pas de collectif « Console ». **Pas de numéro ni de
génération** : `Nintendo Switch` couvre aussi bien la Switch que la Switch 2 (jamais de
tag `Nintendo Switch 2` séparé), même logique que `PlayStation` (pas de distinction
PS4/PS5) et `Xbox` (pas de distinction Xbox One/Series X) — le texte peut nommer la
génération précise, le tag reste toujours la plateforme générique.

**Jeux :** Cloud gaming · Mobile · Nintendo Switch · PC · PlayStation · Rétro ·
Steam Deck · VR · Xbox
*(`Rétro` ici = jeu/console d'époque, pas "vieux" au sens large.)*

**Films/séries :** Apple TV+ · Canal+ · Crunchyroll · Disney+ · HBO Max · Netflix ·
Paramount+ · Peacock · Prime Video

**Composants & matériel :** Alimentation · AR · Aspirateur robot · Boîtier ·
Carte graphique · Carte mère · Casque audio · Clavier · Électroménager · Écran ·
Manette · Matériel PC · Microphone · Montre connectée · Périphérique · Processeur ·
RAM · Refroidissement · Réseau · Smartphone · Souris · SSD

*(`Aspirateur robot` réservé aux appareils réellement autonomes (navigation sans
intervention). `Électroménager` couvre les autres appareils ménagers connectés
(aspirateur-balai/laveur manuel, et futurs appareils du même type) — ne pas taguer
`Aspirateur robot` par réflexe dès qu'un appareil aspire, vérifier qu'il navigue
vraiment seul.)*

*(`Périphérique` = matériel EXTERNE en plus d'un tag précis (Casque audio, Clavier,
Souris, Microphone, Écran, Manette) — jamais à sa place. `Matériel PC` = son pendant
pour les composants INTERNES (Carte mère, Processeur, Carte graphique, RAM, SSD,
Alimentation, Boîtier, Refroidissement) — même logique. Les deux umbrella-tags ne se
mélangent jamais entre eux.)*

*(Ces tags composants sont scopés à l'écosystème PC/console — un accessoire externe ou
une pièce interne d'ordinateur/console. Une technologie intégrée à un autre appareil
(ex. l'écran pliable d'un smartphone) n'est pas un `Écran` au sens de cette liste : pas
de tag composant, `Smartphone` seul suffit, comme on ne crée pas de tag `Processeur`
séparé à chaque puce de smartphone annoncée.)*

## §5 — Thèmes & univers — Contenu, semi-fermée (listes triées alphabétiquement)

**Systématique, jeux comme films/séries (voir Grille #6)** : un jeu au cadre
spatial/fantasy/etc. se tague en univers même si l'article se concentre sur le
gameplay/genre. C'est la facette la plus souvent oubliée si on ne la vérifie pas
explicitement à chaque article.

**Admission (3 tests) :** factuel + définissant + revendiqué par le lecteur
(« j'aime les ___ »).

**Univers / cadre :** Années 80 · Aviation · Cyberpunk · Dinosaures · Enquête ·
Espace · Fantasy · Far West · Guerre · Guerre froide · Horreur · IA · Lovecraftien ·
Maritime · Médiéval · Mythologie · Pirates · Post-apocalyptique · Robot ·
Science-fiction · Steampunk · Super-héros · WW1 · WW2 · Zombies
*(`IA` et `Robot` couvrent aussi bien le contenu réel/industrie que les thèmes
fictionnels.)*

**Mécaniques revendiquées :** Compétitif · Coopératif · Cross-play · En ligne ·
Local · Monde ouvert · Multijoueur · Solo

**`Compétitif` réservé à une compétition structurante**, pas à un mode secondaire greffé
sur un jeu principalement solo/coop. Test : le genre est-il compétitif par nature
(baston, MOBA, battle royale, racing avec ranked/matchmaking réel), ou l'article
décrit-il un vrai mode dédié avec classement/matchmaking (ex. "1v1, 2v2" explicites) ?
Si oui → `Compétitif`. Si la compétition n'est qu'une option secondaire (ex. un
deathmatch local en bonus d'une campagne solo/coop qui reste le vrai sujet) → non,
même si le mode existe techniquement. Image utile : Mario Party et Overwatch sont tous
deux "compétitifs" au sens large, mais pas au même niveau — seul le second mérite le tag.

**Qualificatifs permanents :** Animation · Esport · Indé · Remake · Remaster · Rétro
*(`Rétro` = contenu rétro-gaming (voir note §4), mais s'étend à toute rétrospective
matérielle/tech portant sur une pièce d'époque précise (ex. anniversaire d'un
processeur) — pas seulement jeu/console. Reste réservé à un vrai objet d'époque ou à
une couverture qui porte sur son histoire, jamais à un style "rétro-inspiré".)*

**Métiers / sujets :** Cinéma · Doublage · Manga
*(`Manga` = thème transversal pour toute œuvre issue d'un manga — jeu, film, série —
posé EN PLUS de la licence précise, jamais à sa place.)*

**Rubriques éditoriales (suivies par le lecteur) :** Carnet noir · Montage PC

**EXCLUS :**
- **Ton / ambiance** (Sombre, Mélancolique, Stressant, Épique) → interprétatif.
- **Statut / format** (Démo, Bande-annonce, Teaser, Accès anticipé, AAA, Reboot,
  Exclusivité) → transitoire/subjectif. (Remaster/Remake restent : nature permanente.)
- **Techniques de production & styles graphiques** (Procédural, Ray tracing, moteurs,
  Pixel art, voxel, cel-shading, esthétique "rétro-inspirée") → invisibles / non
  revendiqués. `Rétro` reste réservé à un vrai jeu/console d'époque, ou à une
  couverture qui porte sur son histoire.
- **`Gratuit`** : le prix n'est pas un connecteur éditorial fiable pour la reco.

## §5bis — Automobile — Contenu, sujet RÉEL uniquement

`Voiture` (générique) · `Voiture hybride` · `Voiture électrique`. Chaque voiture =
`Voiture` + sa motorisation. Les jeux de voiture/course se taguent via le genre
`Course`, jamais `Voiture`.

## §6 — Événements — Contenu, FERMÉ (triés alphabétiquement)

Evergreen (l'année vit dans la date). Un événement terminé garde son tag.

**Jeux vidéo :** Gamescom · Nintendo Direct · Paris Games Week · Polymanga ·
Red Bull Gamerations · State of Play · Summer Game Fest · The Game Awards ·
Xbox Games Showcase

**Tech / auto :** CES · Computex · Goodwood Festival of Speed · SIGGRAPH · WWDC

**Ciné / pop culture :** CinemaCon · Festival de Cannes · Oscars · San Diego Comic-Con

## §7 — Local suisse — Contenu, FERMÉ (un seul tag)

`Suisse` dès qu'il y a un angle suisse réel : la Suisse est l'acteur, le lieu ou le
sujet de l'actualité — un événement en Suisse, une œuvre/personne/lieu suisse, une
entreprise qui s'implante ou agit spécifiquement sur le marché suisse. Pas de tags
de ville.

**Test resserré — prix/date CH ≠ Suisse par défaut :** un prix converti en CHF ou une
date de sortie suisse mentionnés en routine ne suffisent PAS. Exception : quand le
prix/la date est lui-même l'anomalie qui fait l'actu (produit plus cher en Suisse,
lancement retardé pour une raison suisse) — là le CH est bien le sujet. **L'anomalie
doit être substantielle, pas juste une phrase isolée dans un article qui parle d'autre
chose.** Une simple mention en passant (« pas encore de date CH connue, il faudra
se tourner vers le streaming ») noyée dans un article centré sur un tout autre sujet
(ex. une bande-annonce) ne suffit pas — le test reste : la Suisse est-elle un axe
réel de CET article, pas un détail incident qu'on pourrait retirer sans rien changer
au sujet.

**Cas négatif :** une phrase qui mentionne la Suisse pour dire qu'elle n'est PAS
touchée par un problème qui frappe d'autres pays n'est pas un angle suisse réel.

**Enseignes locales (cinéma, salle, lieu) :** on tague le nom de l'enseigne
(`ARENA Cinemas`, `Cinémas de Sierre`), jamais la ville seule.

**Programme mono-film vs vraie programmation :** un article "programme de la semaine"
qui ne développe substantiellement qu'un seul film a ce film comme véritable sujet →
le tagger. Réserver la règle "listes = pas de tags" aux vraies programmations
multi-films qui listent effectivement plusieurs séances/films sans en développer un
en particulier.

## §8 — Pays — Identité, OUVERT, barrière stricte

Un pays n'est tagué que s'il est l'acteur central (« la Chine légifère », « ventes au
Japon »), jamais pour une mention incidente.

---

## Règles transversales

Exceptions et principes qui s'appliquent après avoir parcouru la Grille, pas facette
par facette.

- **Trait stable vs fait contextuel** : un trait stable de l'œuvre (genre,
  univers/thème uniquement) peut être déduit d'une licence connue même si le texte ne
  le cite pas explicitement. Un fait contextuel (plateforme dispo, événement, chiffres,
  pays concerné) ne se déduit jamais de la connaissance générale du sujet : il doit
  être dit par le texte, sinon → incertitude. Le test : est-ce que ce trait resterait
  vrai pour n'importe quel article parlant de cette œuvre (stable), ou est-ce que ça
  dépend de CET article précis (contextuel) ? Ne s'applique jamais à un produit dérivé
  (§2).
  Les mécaniques revendiquées (Solo/Multi/Coop/Compétitif/En ligne/Local/Cross-play/
  Monde ouvert) ne sont JAMAIS éligibles à cette déduction, même pour une franchise
  réputée multijoueur : ce sont des faits contextuels au même titre que la plateforme.
  Un thème/univers déduit ne vaut que pour la franchise concernée, pas pour tout
  l'article : si plusieurs franchises différentes sont citées ensemble, ne pas tagger
  un thème qui n'est vrai que pour une seule d'entre elles.
  **Identité vs contenu** : cette règle "trait stable" ne concerne que le genre et le
  thème/univers. Elle est distincte de la question de la recherche externe ciblée,
  réservée aux seuls tags d'identité (studio/éditeur d'un titre précis déjà nommé dans
  le texte, §2) — jamais aux tags de facette de contenu, qui restent strictement
  bornés à ce que CE texte couvre, recherche externe ou pas. Le test à appliquer :
  "ce tag identifie-t-il DE QUELLE œuvre on parle (identité) ou DE QUOI l'article
  parle (contenu) ?"
- **Tag large vs catégorie** : on ne tague pas le médium si la catégorie le dit déjà
  (pas de `Série` en News Séries). Exception `Cinéma` (thème transversal
  salle/industrie/festival — pas sur chaque film précis).
- **Listes = pas de tags** : nominés, jeux-épreuves, programmes, line-up → on ne tague
  que le sujet. Exception : une liste courte (≤5) d'éléments qui deviennent chacun
  concrètement et individuellement disponibles/accessibles → on tague chaque élément.
  Une liste plus longue, ou qui évoque une intention/un projet futur, reste non taguée
  individuellement.
- **SF spatial** → `Science-fiction` + `Espace` quand l'espace est central.
- **Pas de tag `Adaptation`** : le jeu et son film partagent simplement la franchise.
- **Facette contextuelle absente → incertitudes** : si une facette contextuelle clé
  manque (plateforme non citée notamment), le pipeline le signale pour complément
  humain — il n'invente pas. Ne s'applique pas aux traits stables, qui se déduisent
  normalement.
- **Nommage** : facettes fermées = on pioche ; une forme canonique unique
  (casse/accent/pluriel) ; singulier par défaut ; un tag = une entité/concept.

---

## Gouvernance & pipeline (verrou anti-dérive)

Le pipeline (`scripts/fetch_batch.py` + `scripts/apply_batch.py`) interroge
`/wp-json/wp/v2/tags` et `/wp-json/wp/v2/categories` en direct à chaque lot et
embarque ce snapshot dans le fichier exporté — le vocabulaire OUVERT existant est donc
toujours à jour, sans entretien. Le vocabulaire FERMÉ (§3 à §8 ci-dessus), lui, reste
défini uniquement dans ce document : ce n'est pas un inventaire de ce qui existe déjà
sur le site, c'est une politique éditoriale.

1. Facettes **fermées** (Identité = non) : on pioche dans ce document, on n'invente
   jamais.
2. Facettes **ouvertes** (Identité = oui) : réutiliser la forme exacte trouvée dans le
   snapshot du lot ; vérifier les variantes (casse/accent/pluriel/tiret) avant de
   proposer un nouveau tag.
3. **Un nouveau tag n'est jamais écrit direct** : il sort dans `nouveaux_tags`, validé
   par l'humain avant que `apply_batch.py` ne l'écrive dans WordPress.
4. **Chaque proposition de lot part de la Grille de tagging obligatoire** (ci-dessus),
   parcourue intégralement pour chaque article — entrée : le TEXTE INTÉGRAL, la
   CATÉGORIE et le snapshot des tags/catégories existants, tous fournis par
   `batch_XXXX.json`.

Toute règle nouvelle qui se révèle nécessaire pendant un lot se documente d'abord
dans `changelog-nomenclature.md` (avec le raisonnement complet), puis se répercute
ici en remplaçant directement la règle concernée — jamais l'inverse.