# Changelog — historique de la nomenclature de tagging JVMag

> **Rôle de ce fichier :** journal chronologique des évolutions de la nomenclature, avec
> le raisonnement complet derrière chaque changement. Ce n'est **plus** la source de
> vérité pour les règles actives — c'est [regles-tagging-actives.md](regles-tagging-actives.md)
> qui joue ce rôle, à la racine du repo. Ce fichier-ci n'est utile que pour comprendre
> *pourquoi* une règle existe ; il n'est jamais fourni à Claude Code pendant l'exécution
> d'un lot (voir `CLAUDE.md`).
>
> L'historique concret des lots traités (décisions prises, tags créés, cas litigieux
> tranchés) vit dans [liste-maitresse-tags-jvmag.md](liste-maitresse-tags-jvmag.md).

## Changelog
- **v3.25** (2026-07-31, reprise du catalogue principal, lot #2) : deux décisions :
  - **`Bethesda Game Studios` renommé `Bethesda`** — nom trop long pour un gain de
    précision nul (même logique que le retrait de `Sony Interactive Entertainment` en
    v3.24). Tag WordPress renommé directement (id conservé, aucune réécriture
    d'article nécessaire) ; la paire systématique `Bethesda` → `Xbox Game Studios`
    (§2) mise à jour en conséquence.
  - **`Game Conscient` ajouté aux Rubriques éditoriales** (§5) : podcast JVMag
    récurrent, même statut que `Carnet noir`/`Montage PC`.
- **v3.24** (2026-07-30, reprise du catalogue principal, lot #1) : quatre décisions
  actées pendant la revue du premier lot post-retag :
  - **`Périphérique de Simulation` ajouté** (§4) : matériel dédié à la simulation
    (volants, palonniers, panneaux de cockpit, écrans de simulateur) — rejoint la
    catégorie `Périphérique` comme les autres tags précis (Casque audio, Manette,
    etc.), ne la remplace pas. Coexiste avec un autre tag précis si applicable (ex. un
    panneau à écran intégré reste aussi `Écran`).
  - **`Indé` éligible à la recherche ciblée d'identité** : le statut d'indépendance
    d'un studio déjà nommé est un fait stable sur ce studio, pas un fait propre à
    l'article — traité comme un studio/éditeur non cité (§2), mêmes conditions
    strictes (source unique, sinon incertitude).
  - **`Sony Interactive Entertainment` retiré, remplacé par `Sony`** : le nom complet
    n'ouvre aucun angle de reco distinct de `Sony` seul, contrairement à `PlayStation
    Studios`/`Sony Santa Monica` qui restent des identités créatives à part entière et
    gardent leur tag propre. Correction rétroactive appliquée à l'article Ratchet &
    Clank: Ranger Rumble (lot #4 du retag).
  - **`Extraction shooter` ajouté au vocabulaire fermé des genres** (§3), suite à un
    article (Rules of Engagement: The Grey State) où le texte nommait explicitement ce
    genre, absent jusqu'ici.
- **v3.23** (2026-07-30, retagging rétroactif lot #5/7, dernier lot) : trois clarifications :
  - **`Compétitif` réservé à une compétition structurante** (§5) : ne se tague plus pour
    un mode secondaire greffé sur un jeu principalement solo/coop (ex. deathmatch local
    en bonus d'une campagne, écarté sur Agent 64: Spies Never Die), réservé aux genres
    compétitifs par nature (baston, MOBA, battle royale) ou aux vrais modes dédiés avec
    classement/matchmaking réel. Image retenue : Mario Party et Overwatch sont tous deux
    "compétitifs" au sens large, mais pas au même niveau.
  - **Composants PC/console scopés, pas les specs d'appareils intégrés** (§4) : un écran
    pliable de smartphone n'est pas un `Écran` au sens de la liste composants (qui ne
    couvre que l'écosystème PC/console, externe ou interne) — `Smartphone` seul suffit,
    corrige un tag `Écran` posé à tort sur une actu Samsung Flex Titanium.
  - **`Bethesda Game Studios` retiré** d'un article sur la restructuration Xbox/Obsidian
    où le tag n'apparaissait que dans une comparaison historique (New Vegas développé
    "en dehors de" BGS) — le nouveau projet Fallout est développé par Obsidian, pas BGS ;
    la paire Obsidian Entertainment → Xbox Game Studios suffit à couvrir l'éditeur.
- **v3.22** (2026-07-30, retagging rétroactif lot #4/7) : trois décisions actées :
  - **`Bethesda Game Studios` → toujours + `Xbox Game Studios`** ajouté aux paires
    systématiques (§2) : Bethesda Game Studios est lui-même un label Xbox Game Studios
    depuis le rachat Microsoft/ZeniMax, même logique que Obsidian/The Coalition.
  - **Pas de paire `The Pokémon Company` / `Pokémon`** : question tranchée
    définitivement (l'item était marqué "à confirmer à l'usage" depuis v3.18). Même
    quand l'entité est nommée explicitement dans le texte, on reste sur `Pokémon`
    seul — contrairement à Rockstar/Take-Two, la distinction entité-juridique/
    franchise n'ouvre pas d'angle de reco différent, juste un nom plus long.
  - **`Électroménager` ajouté au vocabulaire fermé** (§4), distinct de `Aspirateur
    robot`. Corrige une erreur trouvée en retagging : un aspirateur-laveur manuel
    (poussé à la main, pas de navigation autonome) avait été tagué `Aspirateur robot`
    par réflexe — les deux tags ne se confondent plus désormais.
- **v3.21** (2026-07-30, retagging rétroactif lot #3/7) : `SIGGRAPH` ajouté au vocabulaire
  fermé des événements tech (§6, ex. DLSS 5 de NVIDIA). Philosophie actée pour ce type
  d'ajout à ce stade du chantier : accepter les événements légitimes au fil de l'eau
  plutôt que de bloquer sur leur usage futur — une fois les 13 000 articles parcourus,
  les tags sous-utilisés seront révisés collectivement, pas au cas par cas maintenant.
- **v3.20** (2026-07-30, retagging rétroactif lot #2/7) : trois nouvelles clarifications
  tranchées pendant la revue du lot #2 :
  - **Genre cité en nuance de ton ≠ genre à tagger** (§3) : une formule « à la frontière
    de X, Y, Z » décrit une ambiance, pas une déclaration de genre — corrige une
    proposition erronée (`Horreur` sur Scrooge, alors que le texte le qualifie par
    ailleurs de comédie ; « horreur » n'apparaissait que dans un « à la frontière de »).
  - **Service/abonnement reste tagué même en accès gratuit exceptionnel** (§2) : un
    article sur un test de cloud gaming Xbox accessible sans abonnement payant reste
    tagué `Xbox Game Pass` — la fonctionnalité appartient techniquement à ce service/
    cette marque, même rendue accessible sans le palier payant pour l'occasion. Ne pas
    confondre "pas besoin de l'abonnement pour CETTE offre" et "aucun rapport avec le
    service".
  - **Anomalie Suisse : doit être substantielle, pas un détail isolé** (§7) : une
    mention en passant d'une date CH non confirmée, noyée dans un article centré sur
    autre chose (ex. une bande-annonce), ne suffit pas à déclencher l'exception
    anomalie — resserre le test ajouté en v3.16, qui ne précisait pas ce seuil.
- **v3.19** (2026-07-30, retagging rétroactif lot #1/7) : trois clarifications tranchées
  pendant la relecture du premier lot de retag :
  - **Plateformes jamais versionnées** (§4) : confirmation explicite que "Switch 2",
    "PS5", "Xbox Series X" etc. cités dans le texte restent tagués sous la plateforme
    générique (`Nintendo Switch`, `PlayStation`, `Xbox`) — la règle "pas de numéro"
    existait déjà mais manquait d'exemples concrets, ce qui a fait remonter la question
    inutilement sur 3 articles du lot.
  - **Portée des paires studio/éditeur systématiques** (§2) : `Rockstar Games` →
    `Take-Two Interactive` (et les paires équivalentes) ne s'applique QUE quand le
    studio est tagué comme développeur/éditeur d'une œuvre précise. Ne se déclenche pas
    quand le studio est tagué via la règle "personne + œuvre-signature" (cas Dan Houser,
    cofondateur de Rockstar interviewé sur son nouveau studio Absurd Ventures) — lien
    biographique, pas publication d'un jeu.
  - **`Rétro` étendu au-delà du jeu/console** (§5) : une rétrospective matérielle/tech
    portant sur une pièce d'époque précise (ex. anniversaire d'un processeur Intel Core
    2 Duo) est éligible, même logique qu'un jeu/console d'époque — reste réservé à un
    vrai objet d'époque, jamais à un style visuel "rétro-inspiré".
  - Confirmé aussi (pas un changement de règle, juste une application) : pas de
    genre/thème ajouté pour des jeux juste listés côte à côte sans description (ex.
    jeux du mois PS Plus) — même principe que "thème vaut pour la franchise, pas pour
    tout l'article" (v3.18, cas Obsidian/Fallout/Avowed).
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