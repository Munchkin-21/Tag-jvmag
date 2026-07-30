# Nomenclature des tags — JVMag (v3.18)

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
- **v3.18** (2026-07-30) : nouvelle distinction structurante **tag d'identité vs tag de
  facette de contenu**, suite à une question directe sur le rôle de la recherche externe :
  - **Tags d'identité** (studio dev, éditeur, franchise — §1/§2) répondent à "de quelle œuvre
    s'agit-il ?". Quand un titre précis et **non-ambigu** est nommé dans le texte mais que son
    studio/éditeur n'y est pas explicite, une **recherche ciblée** est autorisée pour compléter ce
    tag — mais **seulement si une source unique et non-contradictoire confirme l'info sans
    ambiguïté** (pas d'homonyme, pas de résultats divergents). En cas de doute (titre indé/peu
    documenté, résultats contradictoires) → ne pas inventer, laisser en incertitude comme avant.
    Voir §2. **La plateforme n'entre pas dans cette exception** : elle reste un pur fait
    contextuel, jamais déduite ni recherchée (règle confirmée sans exception depuis v3.12) — une
    œuvre a un studio unique mais peut sortir sur plusieurs plateformes, l'article n'en couvrant
    parfois qu'une seule ; deviner la plateforme risquerait de sur-tagger des supports jamais
    évoqués.
  - **Tags de facette de contenu** (genre, mécaniques, thèmes, événements — §3/§5/§6) répondent à
    "de quoi cet article parle-t-il ?", jamais "qu'est-ce qui est vrai sur cette œuvre en
    général ?". Ils ne sont **jamais** complétés par recherche externe, même quand le fait est
    notoire (ex. un jeu multijoueur connu dont l'article ne traite que d'un conflit interne au
    studio → pas de tag `Multijoueur`, l'article ne couvre pas cet angle). L'absence du tag est
    une information correcte pour la reco ("cet article ne couvre pas cette facette"), pas un trou
    à combler — confirme et généralise la règle "mécaniques jamais déduites" de la v3.17.
  - Reformulation de la règle **Trait stable vs fait contextuel** (Règles transversales) pour
    intégrer cette distinction explicitement.
- **v3.17** (2026-07-29, pilote lot #11) : `Manga` et `CinemaCon` ajoutés au vocabulaire fermé
  (§5, §6). Clarifications suite à une revue intensive :
  - **Trait stable réservé à l'œuvre-sujet** : le genre/univers d'une franchise ne se déduit que
    quand cette œuvre EST le sujet de l'article (Dragon Age, Stargate), pas quand une personne qui
    l'a traversée dans sa carrière est le sujet (ex. un Carnet noir sur un acteur associé à une
    franchise — la franchise se tague, son univers/genre non).
  - **Sous-titre à retirer : seulement pour les franchises multi-épisodes** (Red Dead Redemption 2
    → Red Dead Redemption), jamais pour un jeu unique et autonome dont le titre complet inclut un
    sous-titre (`Hela: of Mice & Magic`, `Agefield High: Rock the School` — rien à consolider).
  - **Mécaniques (§5) : jamais déduites, même d'une franchise très connue** — seulement si
    réellement décrites dans CE texte précis. Corrige une inférence erronée (Dragon Ball Xenoverse
    3, Assetto Corsa EVO) qui traitait les mécaniques comme un trait stable au même titre que le
    genre — ce n'en est pas un, elles restent un fait contextuel comme la plateforme.
  - **Thème/univers unique par franchise, pas par article** : un article qui mentionne plusieurs
    franchises différentes (ex. restructuration chez un éditeur touchant Fallout + Avowed + The
    Outer Worlds + Grounded) ne doit pas recevoir un thème qui n'est vrai que pour UNE des
    franchises citées (`Post-apocalyptique` retiré d'un tel article — vrai pour Fallout seul, faux
    pour les 3 autres).
  - **Éditeur first-party vs plateforme** : quand un article parle de la structure
    actionnariale/éditoriale d'un studio (qui possède qui, restructuration), c'est l'éditeur
    (`Xbox Game Studios`) qui s'applique, pas la plateforme (`Xbox`) — les deux facettes sont
    différentes même si le mot est identique. `Obsidian Entertainment` → `Xbox Game Studios`
    ajouté aux paires systématiques (§2), même logique que Rockstar Games/Take-Two.
  - **`Alien` reste l'ombrelle cross-media unique** : pas de tag séparé pour une série dérivée
    (`Alien: Earth`) quand `Alien` est déjà pensé pour relier jeu/film/série (voir §1).
  - **Pokémon** : le studio dev dépend du produit précis — `Niantic` pour Pokémon GO, `Game Freak`
    pour les jeux principaux — jamais les deux indifféremment. `The Pokémon Company` (coentreprise
    Nintendo/Game Freak/Creatures qui gère toute la franchise) proposé comme paire stable avec
    `Pokémon`, à l'usage.
- **v3.16** (2026-07-29) : règle Suisse (§7) resserrée — un prix en CHF ou une date de sortie
  suisse mentionnés en routine (parce que JVMag est un média suisse et localise systématiquement
  ces infos) **ne suffisent plus** pour `Suisse`. Il faut que la Suisse soit l'acteur/le lieu/le
  sujet réel de l'actu (événement, œuvre, personne, lieu ou implantation de marché suisses) — ou
  que le prix/la date soit lui-même l'anomalie qui fait l'actu (ex. plus cher en Suisse, retardé
  pour une raison suisse). 5 articles corrigés rétroactivement (tag retiré) : Samsung 990 SSD,
  Samsung Galaxy Watch9/Ultra2, Samsung Galaxy Z Fold 8/Flip 8, Call of Duty (film), The Batman
  Part II — tous n'avaient qu'un prix/une date CH routiniers, pas un vrai sujet suisse.
- **v3.15** (2026-07-29, pilote lot #10) : `MOBA` et `Peacock` ajoutés au vocabulaire fermé (§3,
  §4). `Matériel PC` formalisé comme pendant interne de `Périphérique` — s'applique EN PLUS d'un
  composant précis (Carte mère, Processeur, Carte graphique, RAM, SSD, Alimentation, Boîtier,
  Refroidissement), jamais à sa place (§4). `Rockstar Games` → toujours accompagné de
  `Take-Two Interactive` (éditeur first-party, même logique que Xbox Game Studios) (§2). Nouvelle
  règle sur les programmes de cinéma mono-film (§7/Grille) : si un article "programme" ne
  développe substantiellement qu'un seul film, ce film est le sujet et se tague — réservé aux
  vraies programmations multi-films (ex. ARENA Cinemas) pour la règle "listes = pas de tags".
  **Corrections de process** suite à plusieurs oublis constatés sur le lot #10 (voir Grille de
  tagging obligatoire, nouvelles notes) : Coopératif/Compétitif doivent systématiquement
  s'accompagner de `Multijoueur` ; toujours vérifier `En ligne` explicitement quand du multijoueur
  est mentionné ; relire le texte une seconde fois avant de conclure qu'aucun genre ne s'applique
  (mot-clé manqué sur Beastro : "deck-building **stratégique**" était bien dans le texte).
- **v3.14** (2026-07-29, pilote lot #9) : `Aspirateur robot` ajouté au vocabulaire fermé (§4).
  Clarification : `IA` et `Robot` (§5) couvrent le vrai contenu tech/industrie, pas seulement les
  thèmes fictionnels — précédent déjà présent au pilote ("Robots humanoïdes Chine" → Robot · IA ·
  Chine · Unitree) mais mal appliqué sur deux articles avant correction. Sujets société-tech hors
  IA (ex. régulation des réseaux sociaux) : pas de nouveau tag pour l'instant, un seul cas à ce
  jour, à surveiller.
- **v3.13** (2026-07-29) : `Périphérique` reformulé — s'applique EN PLUS de, jamais à la place de,
  un tag matériel externe précis (`Casque audio`, `Clavier`, `Souris`, `Microphone`, `Écran`,
  `Manette`), d'après le précédent déjà observé sur le site (Écran + Manette + Périphérique
  ensemble). Ne s'applique jamais aux composants internes (Carte mère, RAM, SSD...). `Manette`
  ajoutée au vocabulaire fermé (§4) — existait déjà comme tag WordPress mais jamais formalisée.
- **v3.12** (2026-07-29, pilote lot #7) : `Microphone` ajouté au vocabulaire fermé (§4). Précision
  §5 EXCLUS : un jeu **neuf** à esthétique rétro-inspirée (ex. graphisme vectoriel) n'est PAS
  `Rétro` — c'est un style/technique, exclu comme le cel-shading. `Rétro` reste réservé au vrai
  contenu rétro-gaming (jeu/console d'époque, ou couverture qui porte sur leur histoire).
  Confirmation : la règle "plateforme jamais déduite" (§ Trait stable vs fait contextuel) reste
  absolue, aucune exception pour les franchises sportives annuelles — un cas isolé peut être
  complété manuellement par l'humain sans changer la règle générale.
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
jamais passer une ligne sous silence). **Relire le texte une seconde fois avant de conclure qu'un
mot-clé n'y est pas** — plusieurs oublis (lot #10) venaient d'un mot-clé explicite présent mais
manqué à la première lecture, pas d'une vraie absence. C'est le seul document de travail pour proposer un lot —
il remplace tout autre résumé ou checklist condensé.

| # | Facette | Où | Question à trancher |
|---|---------|-----|----------------------|
| 1 | Licence/sujet | §1 OUVERT | Œuvre/franchise/produit identifiable ? Forme canonique (sans numéro/adjectif) ? |
| 2 | Personne | §1 OUVERT | Personne réelle = sujet ou vedette-hook ? Si oui : œuvre-signature à tagger aussi (sauf si l'œuvre du moment est déjà taguée par ailleurs, voir §1) ? |
| 3 | Studio/éditeur/marque | §2 OUVERT | Studio dev cité ? Éditeur first-party majeur (trait stable — ex. `Rockstar Games` → toujours + `Take-Two Interactive`, `The Coalition` → toujours + `Xbox Game Studios`) ? Non cité mais titre précis et non-ambigu → recherche ciblée autorisée si une source unique confirme sans ambiguïté (voir §2), sinon incertitude. **Produit dérivé** (jouet, figurine, produit dérivé) → licence/marque oui, genre du jeu source NON (voir §2) |
| 4 | Genre | §3 FERMÉ | Cité dans le texte (relire une 2e fois — mot-clé souvent présent mais manqué), OU trait stable d'une licence connue (jamais pour un produit dérivé, voir #3) ? |
| 5 | Plateforme/composant | §4 FERMÉ | Cité explicitement dans le texte — fait contextuel, ne se déduit **jamais**. Composant PC (Carte mère/Processeur/Carte graphique/RAM/SSD/Alimentation/Boîtier/Refroidissement) → ajouter aussi `Matériel PC` ; matériel externe (Casque audio/Clavier/Souris/Microphone/Écran/Manette) → ajouter aussi `Périphérique`. |
| 6 | Thème/univers | §5 semi-fermé | **Systématique dès qu'une licence est taguée en #1** : trait stable de cette licence (même non cité) OU thème explicite dans le texte ? Ne jamais laisser cette ligne vide sans y avoir réfléchi. |
| 7 | Mécaniques revendiquées | §5 | Solo/Multi/Coop/Compétitif/En ligne/Local/Cross-play/Monde ouvert — seulement si réellement décrites, pas juste théoriquement possibles. **`Coopératif` ou `Compétitif` ⇒ toujours ajouter `Multijoueur` aussi** (jouer à plusieurs = multijoueur, par définition). Vérifier `En ligne` explicitement dès que serveurs/connexion/matchmaking sont mentionnés — ne pas l'oublier par défaut. |
| 8 | Qualificatif permanent | §5 | Indé/Remake/Remaster/Rétro/Esport/Animation, si applicable ? |
| 9 | Automobile | §5bis | Voiture réelle = sujet ? (jamais pour un jeu de course → `Course` en #4) |
| 10 | Événement | §6 FERMÉ | Un événement de la liste est-il le contexte de l'annonce ? |
| 11 | Local suisse | §7 FERMÉ | La Suisse est-elle l'acteur/lieu/sujet réel (pas juste un prix CHF ou une date CH donnés en routine) ? |
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
  → Bonus cross-media : `Alien` relie le jeu ET le film ET la série — **ne pas créer de tag
  séparé pour une série/spin-off dérivé** (ex. pas de `Alien: Earth` en plus de `Alien`), l'ombrelle
  existe précisément pour ça.
  → **Sous-titre à retirer = seulement pour consolider une franchise multi-épisodes.** Un jeu
  **unique et autonome** dont le titre officiel complet inclut un sous-titre (`Hela: of Mice &
  Magic`, `Agefield High: Rock the School`) garde son titre entier : il n'y a rien à consolider,
  ce n'est pas un numéro de suite.
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
- **Trait stable réservé à l'œuvre qui EST le sujet** : le genre/univers d'une franchise ne se
  déduit (voir Règles transversales) que quand cette œuvre est elle-même le sujet de l'article
  (Dragon Age, Stargate). Quand le sujet est une **personne** qui a traversé cette œuvre dans sa
  carrière (ex. un Carnet noir sur un acteur associé à une franchise), l'œuvre se tague (lien
  pertinent pour la reco) mais **pas son univers/thème** — le lien est biographique, pas
  définissant. Ex. : Carnet noir Sam Neill → `Jurassic Park` oui, `Dinosaures` non.

## §2 — Studios / éditeurs / marques — OUVERT
- **Recherche ciblée d'identité (v3.18)** : quand un titre précis et **non-ambigu** est nommé dans
  le texte mais que son studio dev/éditeur n'y est pas explicite, une recherche externe ponctuelle
  est autorisée pour identifier ce studio/éditeur et compléter le tag — au même titre qu'une
  identification, pas un enrichissement de contenu. **Condition stricte** : n'appliquer que si une
  source unique confirme l'info **sans ambiguïté ni contradiction** (pas d'homonyme, pas de
  résultats divergents). Beaucoup de titres couverts sont indés/peu documentés : en cas de doute,
  ne pas deviner — laisser en incertitude et signaler pour validation humaine, comme pour toute
  autre facette non confirmée. Réservé aux tags d'identité (studio/éditeur/plateforme/franchise) ;
  ne s'étend jamais aux tags de facette de contenu (mécaniques, thèmes, événements — voir Règles
  transversales).
- Règle « acteur le plus **utile** » : God of War → Santa Monica Studio.
- **Studio dev toujours + éditeur first-party majeur** s'il est une marque-source suivie
  (Xbox Game Studios, PlayStation Studios, Nintendo, SEGA, Square Enix…). NB : le tag plateforme
  (`Xbox`) ≠ l'éditeur (`Xbox Game Studios`) — l'un = dispo, l'autre = curation first-party.
  **Paires systématiques déjà actées** : `Rockstar Games` → toujours + `Take-Two Interactive` ;
  `The Coalition` → toujours + `Xbox Game Studios` ; `Obsidian Entertainment` → toujours +
  `Xbox Game Studios`. Trait stable de propriété, pas besoin que l'article cite explicitement
  l'éditeur pour l'ajouter. **Attention à ne pas confondre `Xbox Game Studios` (éditeur, qui
  possède le studio) et `Xbox` (plateforme de sortie, §4)** : un article sur la structure
  actionnariale/éditoriale d'un studio (ex. restructuration, licenciements) appelle l'éditeur, pas
  forcément une plateforme de sortie.
  **Pokémon** : le studio dev dépend du produit précis, jamais appliqué en bloc — `Niantic` pour
  Pokémon GO, `Game Freak` pour les jeux principaux. `The Pokémon Company` (coentreprise
  Nintendo/Game Freak/Creatures qui gère toute la franchise) est candidat à une paire stable avec
  `Pokémon`, à confirmer à l'usage.
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
MMO · MOBA · Narratif · Party game · Plateforme · Point & click · Réflexion · Roguelike · RPG ·
Rythme · Shoot'em up · Simulation · Souls-like · Sport · Stratégie · Survie · Tactique ·
Tower defense · TPS
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
Peacock · Prime Video
**Composants & matériel :** Alimentation · AR · Aspirateur robot · Boîtier · Carte graphique ·
Carte mère · Casque audio · Clavier · Écran · Manette · Matériel PC · Microphone ·
Montre connectée · Périphérique · Processeur · RAM · Refroidissement · Réseau · Smartphone ·
Souris · SSD
*(`Périphérique` = matériel EXTERNE en plus d'un tag précis — `Casque audio`, `Clavier`, `Souris`,
`Microphone`, `Écran`, `Manette` — jamais à sa place. `Matériel PC` = son pendant pour les
composants INTERNES — `Carte mère`, `Processeur`, `Carte graphique`, `RAM`, `SSD`, `Alimentation`,
`Boîtier`, `Refroidissement` — même logique, en plus jamais à la place. Les deux umbrella-tags ne
se mélangent jamais entre eux : un SSD est interne → `Matériel PC`, pas `Périphérique`.)*

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
*(`IA` et `Robot` couvrent aussi bien le contenu réel/industrie — ex. adoption de l'IA générative
dans le jeu vidéo, robots humanoïdes — que les thèmes fictionnels. Toujours vérifier le précédent
avant de conclure qu'aucun tag §5 ne s'applique.)*
**Mécaniques revendiquées :** Compétitif · Coopératif · Cross-play · En ligne · Local ·
Monde ouvert · Multijoueur · Solo
**Qualificatifs permanents :** Animation · Esport · Indé · Remake · Remaster · Rétro
*(`Rétro` = contenu rétro-gaming, voir note §4 — pas un synonyme de "ancien/nostalgique".)*
**`Gratuit` retiré (v3.9)** : le prix n'est pas un connecteur éditorial fiable — deux jeux gratuits
n'ont souvent rien en commun (contrairement à `Indé`/`Rétro`, qui identifient une vraie
scène/communauté suivie). Ne pas retaguer.
**Métiers / sujets :** Cinéma · Doublage · Manga
*(`Manga` = thème transversal pour toute œuvre issue d'un manga — jeu, film, série — posé EN PLUS
de la licence précise, jamais à sa place. Ex. Naruto, One Piece, Dragon Ball, Fairy Tail : chacune
garde son tag propre, `Manga` les relie tous pour la reco, même logique que `Super-héros` pour
Marvel/DC.)*
**Rubriques éditoriales (suivies par le lecteur) :** Carnet noir · Montage PC

**EXCLUS :**
- **Ton / ambiance** (Sombre, Mélancolique, Stressant, Épique) → interprétatif.
- **Statut / format** (Démo, Bande-annonce, Teaser, Accès anticipé, AAA, **Reboot**, **Exclusivité**)
  → transitoire/subjectif. *(Remaster/Remake restent : nature permanente.)*
- **Techniques de production & styles graphiques** (Procédural, Ray tracing, moteurs, **Pixel art**,
  voxel, self-shading, cel-shading) → invisibles / non revendiqués. **Ceci inclut l'esthétique
  "rétro-inspirée"** (ex. graphisme vectoriel façon arcade 1970s sur un jeu neuf) : c'est un style,
  pas du contenu rétro-gaming → pas de tag `Rétro`. `Rétro` reste réservé à un vrai jeu/console
  d'époque, ou à une couverture qui porte sur son histoire (voir §4).

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
**Ciné / pop culture :** CinemaCon · Festival de Cannes · Oscars · San Diego Comic-Con
*(San Diego Comic-Con peut aussi porter des annonces jeux vidéo, à la manière de Gamescom — reste
classé ici car son identité dominante est pop culture/ciné/séries. CinemaCon revenait sur
plusieurs lots, ajouté en conséquence — contrairement à Annecy/SIGGRAPH, restés isolés et non
ajoutés.)*

## §7 — Local suisse — FERMÉ (un seul tag)
**`Suisse`** dès qu'il y a un **angle suisse réel** : la Suisse est l'acteur, le lieu ou le sujet
de l'actualité — un événement en Suisse, une œuvre/personne/lieu suisse, une entreprise qui
s'implante ou agit spécifiquement sur le marché suisse. **Pas de tags de ville.**
**Test resserré (v3.16) — prix/date CH ≠ Suisse par défaut :** JVMag est un média suisse, donc un
prix converti en CHF ou une date de sortie suisse mentionnés en routine (comme sur quasiment tous
les articles produits/films/jeux) ne suffisent PAS — c'est un service au lecteur, pas une info sur
la Suisse. Exception : quand le prix/la date est lui-même l'anomalie qui fait l'actu (ex. un
produit **plus cher** en Suisse qu'ailleurs, un lancement **retardé pour une raison suisse**) — là
le CH est bien le sujet, pas juste la devise d'affichage.
*(Distinction : `DENZA` → un réseau de concessionnaires s'implante activement EN Suisse, sujet
réel. `Samsung 990 SSD` → prix CHF donné en routine pour un produit mondial, pas un sujet — tag
retiré en v3.16.)*
**Cas négatif :** une phrase qui mentionne la Suisse pour dire qu'elle **n'est PAS touchée** par un
problème qui frappe d'autres pays (« en Suisse tout fonctionne normalement ») n'est **pas** un
angle suisse réel — ce n'est qu'une précision de contexte, pas le sujet. Ne taguer `Suisse` que si
le pays est réellement concerné/impacté par ce dont parle l'article.
**Enseignes locales (cinéma, salle, lieu) :** on tague le **nom de l'enseigne** (`ARENA Cinemas`,
`Cinémas de Sierre`), jamais la ville seule (`Sierre`) — c'est la même règle que "pas de tags de
ville", juste avec l'enseigne en OUVERT (§ licences/marques) + `Suisse` en plus. Si un tag de ville
brut traîne dans l'historique du site, le corriger : retagger les articles concernés avec la bonne
enseigne puis supprimer le tag de ville (`scripts/wp_client.py::delete_tag`).
**Programme mono-film vs vraie programmation (v3.15) :** un article "programme de la semaine" qui
ne développe substantiellement qu'**un seul film** (synopsis complet, casting, durée — le reste
n'étant qu'un lien vers "le programme complet") a ce film comme véritable sujet → le tagger. Réserver
la règle "listes = pas de tags" aux vraies programmations multi-films qui listent effectivement
plusieurs séances/films sans en développer un en particulier (ex. ARENA Cinemas, plusieurs films
avec horaires détaillés pour chacun).

## §8 — Pays — OUVERT, barrière stricte
Un pays n'est tagué **que s'il est l'acteur central** (« la Chine légifère », « ventes au Japon »),
jamais pour une mention incidente.

---

## Règles transversales

Exceptions et principes qui s'appliquent après avoir parcouru la Grille, pas facette par facette.

- **Trait stable vs fait contextuel** : un trait stable de l'œuvre (**genre, univers/thème
  uniquement**) peut être déduit d'une licence connue même si le texte ne le cite pas
  explicitement — c'est le même principe que la désambiguïsation `Final Fantasy` + `MMO` = FF XIV
  / `Final Fantasy` + `Action-RPG` = le remake FF7 (§1). Un fait contextuel (plateforme dispo,
  événement, chiffres, pays concerné) ne se déduit **jamais** de la connaissance générale du
  sujet : il doit être dit par le texte, sinon → incertitude. Le test : est-ce que ce trait
  resterait vrai pour n'importe quel article parlant de cette œuvre (stable), ou est-ce que ça
  dépend de CET article précis (contextuel) ? Ne s'applique jamais à un produit dérivé (§2).
  **Les mécaniques revendiquées (Solo/Multi/Coop/Compétitif/En ligne/Local/Cross-play/Monde
  ouvert) ne sont JAMAIS éligibles à cette déduction**, même pour une franchise réputée
  multijoueur (ex. Dragon Ball Xenoverse, connu pour son online) : ce sont des faits contextuels
  au même titre que la plateforme, elles ne se taguent que si réellement décrites dans CE texte.
  **Un thème/univers déduit ne vaut que pour la franchise concernée, pas pour tout l'article** :
  si plusieurs franchises différentes sont citées ensemble (ex. une restructuration d'éditeur
  touchant Fallout + Avowed + The Outer Worlds + Grounded), ne pas tagger un thème qui n'est vrai
  que pour une seule d'entre elles (`Post-apocalyptique` ne vaut que pour Fallout, pas pour les
  3 autres franchises citées dans le même article).
  - **Identité vs contenu (v3.18)** : cette règle "trait stable" ne concerne que le **genre et le
    thème/univers**. Elle est distincte de la question de la **recherche externe ciblée**, réservée
    aux seuls **tags d'identité** (studio/éditeur d'un titre précis déjà nommé dans le texte, voir
    §2) — jamais aux tags de facette de contenu (mécaniques, thèmes, événements), qui restent
    strictement bornés à ce que CE texte couvre, recherche externe ou pas. Le test à appliquer :
    "ce tag identifie-t-il DE QUELLE œuvre on parle (identité) ou DE QUOI l'article parle
    (contenu) ?" Un studio non cité peut se compléter par recherche si le titre est non-ambigu ;
    un `Multijoueur` non discuté dans le texte ne se tague jamais, même si le jeu en question est
    notoirement multijoueur — l'absence signale correctement que l'article ne couvre pas cet angle.
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
