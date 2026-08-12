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
- **v3.33** (2026-08-12, pilote lot #11) : `D23` et `TwitchCon` ajoutés aux événements
  fermés (§6) — contrairement à `Pixel Arcadia` (v3.32), ce sont deux conventions déjà
  bien établies (D23 : convention officielle Disney bisannuelle ; TwitchCon :
  convention internationale de Twitch, citée dans l'interview Lenchanteur comme
  rendez-vous récurrent depuis plusieurs années), pas des paris sur une récurrence
  future.
- **v3.32** (2026-08-12, pilote lot #10) : `Pixel Arcadia` ajouté aux événements fermés
  (§6) — nouveau showcase dédié au rétro-gaming annoncé par Pixel Helix, première
  édition le 24 août. Accepté malgré l'absence de récurrence prouvée (contrairement à
  `EVO`/`Amazon Prime Day`, déjà établis) : même philosophie qu'en v3.21 (`SIGGRAPH`) —
  accepter les événements légitimes au fil de l'eau plutôt que de bloquer sur leur usage
  futur, quitte à réviser collectivement les tags sous-utilisés plus tard.
- **v3.31** (2026-08-05, réconciliation) : ce chantier a temporairement divergé sur deux
  lignes de travail parallèles sans visibilité croisée — l'audit du registre de tags
  (v3.27/v3.28, commit `2c63a84`) d'un côté, une refonte de §3/§5 menée dans une session
  séparée de l'autre, cette dernière étant repartie d'une version antérieure du dépôt
  (avant `2c63a84`) sans le savoir. Résultat à la sauvegarde : version numbers en
  collision (deux v3.27/v3.28 différents), et plusieurs décisions déjà actées et déjà
  appliquées sur WordPress silencieusement absentes des documents. Cette entrée
  documente la réconciliation :
  - **Repris tel quel** (aucune régression) : restriction œuvre-signature aux
    réalisateurs/créateurs (§1, cas Jenna Ortega/`Wednesday`), fusion `Sony Pictures
    Television` → `Sony Pictures` (§2), retrait de `Maritime` du vocabulaire (§5, 1
    seul usage réel), `EVO`/`Amazon Prime Day` réintégrés aux événements fermés (§6).
  - **`Cross-play` réellement retiré cette fois** : la version sauvegardée avait un
    changelog affirmant le retrait, mais le mot restait encore présent dans la Grille
    #7, §5 Mécaniques revendiquées et Règles transversales — l'édition n'avait jamais
    suivi l'entrée de changelog. Corrigé, avec la justification enrichie (échoue 2 des
    3 tests d'admission de §5 : ni définissant ni revendiqué, voir détail dans la
    section EXCLUS §5).
  - **`AR` → `Périphérique` : gardé, mais précisé plutôt que retiré.** Le retrait silencieux
    dans la version sauvegardée réglait un vrai problème (le mode caméra AR de
    Pokémon GO n'est pas du matériel), mais au prix de désarmer aussi le cas légitime
    (lunettes AR physiques, ex. ROG XREAL R1). Le pairing reste actif, avec une note
    explicite en §4 : ne s'applique qu'au sens matériel du mot, jamais à une
    fonctionnalité logicielle de même nom. `Pokémon GO` → `Pokémon` (déjà appliqué sur
    WordPress, article 113119 : `Pokémon` + `Mobile` + `Niantic` suffisent à le
    distinguer des jeux principaux, même logique que `Alien`/`Alien: Earth`) documenté
    dans la paire Pokémon du §2.
  - **`Guerre`/`WW1`/`WW2`/`Guerre froide` : la règle de mutuelle exclusivité (v3.28)
    est confirmée comme la règle en vigueur**, au détriment de l'exemple `Battlefield`
    → `Guerre` introduit dans le brouillon parallèle de la déduction §5 (v3.30 de cette
    réconciliation) : si `Guerre` se déduisait en bloc pour toute une franchise de
    guerre, une entrée de cette franchise située dans un conflit historique précis
    récolterait les deux tags à la fois — exactement la redondance corrigée en v3.28.
    Précisé en §5 : ces quatre tags ne se déduisent jamais par franchise, seulement par
    œuvre précise.
  - **`Tactique` : retiré, mais pas pour le motif initialement avancé.** Le brouillon
    parallèle justifiait le retrait par un usage "trop peu représenté" — vérification
    sur les tags WordPress réels : **7 articles l'utilisaient**, ce n'est pas
    négligeable. La vraie raison, plus solide : sur ces 7, seuls 2 (*Terrinoth: Heroes
    of Descent*, *Star Wars Zero Company*) relèvent du genre stratégie/tactique au sens
    de `Stratégie`+`RPG` (voir §3) ; les 5 autres l'utilisaient dans un sens totalement
    différent — comme qualificatif d'un FPS/TPS "tactique" (rythme réaliste/méthodique),
    déjà couvert par ailleurs (`TPS`, `Infiltration`, `Souls-like`...). Le tag mélangeait
    deux sens incompatibles, ce qui est en soi suffisant pour le retirer — mieux vaut
    aucun tag qu'un tag ambigu. Pas de migration automatique : les 7 articles restent
    en l'état, à revoir individuellement lors d'un futur lot de retag ciblé (la moitié
    n'a de toute façon pas besoin de `Stratégie`).
- **v3.30** (2026-08-05) : **règle de déduction des univers renforcée (§5) + contrôle non
  bloquant de la Grille #6.** Constat mesuré sur les lots 19 et 20 (les plus récents,
  donc produits sous les règles actuelles) : sur 46 œuvres de fiction taguées, 32 ne
  portaient aucun thème §5, dont plusieurs cas où le tag existait déjà et où le trait
  était parfaitement stable — `Star Wars` sans `Espace`, `Batman` sans `Super-héros`,
  `One Piece` sans `Pirates`, `Stargate`, `Ghostbusters`, `Monster Fantasy`, `Stuart
  Fails to Save the Universe`. La ligne #6 est donc sautée massivement alors qu'elle
  porte le maillage transversal dont dépend la recommandation. Hypothèse retenue sur la
  cause : la prudence générale du document (« ne jamais déduire ») déteignait sur les
  traits stables, où la déduction est pourtant explicitement autorisée. §5 dit désormais
  en toutes lettres que l'univers d'une licence connue SE DÉDUIT et que c'est attendu,
  avec des exemples concrets ; symétriquement, une section « Quand ne rien poser »
  légitime l'absence d'univers pour les œuvres définies par leur seul gameplay (combat,
  course, sport, simulation d'engins), et demande de signaler le cas en `incertitudes`
  plutôt que de laisser la ligne silencieusement vide — seul moyen de distinguer un
  choix d'un oubli. **Exception explicitement posée à cette déduction** :
  `Guerre`/`WW1`/`WW2`/`Guerre froide` (v3.28) restent exclus de la déduction en bloc
  par franchise, un exemple `Battlefield` → `Guerre` évoqué initialement ayant été
  écarté en v3.31 pour cette raison précise.
  Côté outil, `apply_batch.py` liste désormais en fin de validation les articles portant
  sur une œuvre sans aucun thème §5. **Non bloquant et volontairement imprécis** : les
  tags plats de WordPress ne permettent pas de distinguer une licence d'un studio ou
  d'une marque de matériel, donc le contrôle repose sur la présence d'un genre ou d'une
  plateforme comme proxy d'« article portant sur une œuvre ». Sur un lot de 40, il liste
  une vingtaine d'identifiants dont environ un tiers sont de vrais oublis. Forme choisie :
  une seule ligne récapitulative plutôt qu'un avertissement par article, pour rester
  lisible. Couvert par `tests/test_theme_coverage.py`.
- **v3.29** (2026-08-05) : **§3 entièrement redéfini — une définition opérationnelle par
  genre.** §3 n'était qu'une liste de noms : le seul critère de tagging était la présence du
  mot dans le texte. Or une quinzaine de genres sont aussi des mots français courants
  (Action, Aventure, Course, Gestion, Narratif, Réflexion, Simulation, Stratégie, Survie…),
  ce qui produit des faux positifs invisibles — cas déclencheur : `Narratif` posé sur
  Unhinged (112433) sur la seule foi d'une formule « à la frontière entre série, film
  d'horreur et jeu narratif », alors que la v3.20 exclut précisément ces formules, et
  `Thriller` — le genre réellement assumé par le texte — non tagué. Chaque genre a
  désormais une définition d'une à trois lignes, avec le piège lexical signalé par ⚠️ quand
  il existe. Bloc de départage ajouté pour `Réflexion`/`Stratégie`/`Gestion`, dont la
  frontière était la source de confusion la plus fréquente.
  **Nombre de genres par article — règle souple retenue** : le genre principal assumé + tout
  genre secondaire clairement identifiable, qu'il soit nommé ou décrit sans ambiguïté. Un
  genre non nommé se tague dès que le texte décrit ce que sa définition exige (ex. :
  `Infiltration` sur un test décrivant l'évitement de la détection comme mécanique centrale,
  même sans le mot). Motif : la transversalité prime — un article reliant plusieurs genres
  crée plus de liens pour la reco. Deux garde-fous en sens inverse : une mécanique ponctuelle
  n'est pas un genre (le seuil est dans chaque définition), et dans le doute on ne pose pas
  et on signale en `incertitudes` — un genre en trop pollue le score d'affinité de tous les
  lecteurs de l'article, un genre manquant ne coûte qu'un lien. **Ce compromis reste à
  vérifier sur des lots réels** — c'est un pari mesuré, pas une certitude : plus de liens
  par article peut aussi diluer la précision du score d'affinité si la règle est appliquée
  trop largement.
  **Corollaire — un mot ne peut plus être à la fois genre (§3) et thème (§5).** `Horreur`
  et `Science-fiction` étaient dans les deux sections, `Fantastique` et `Policier`
  seulement en §3. Décision : ces registres sont des **thèmes**, pas des genres, et valent
  pour tous les médiums — un film d'horreur et un jeu d'horreur reçoivent le même tag,
  posé depuis §5. Motif : le maillage transversal (un lecteur qui aime l'horreur trouve
  les deux) prime sur une distinction genre/thème que la nomenclature ne tenait de toute
  façon pas. `Fantastique` ajouté à §5 avec sa frontière vis-à-vis de `Fantasy` ;
  `Policier` basculé en thème §5 également : il ne fait pas doublon avec `Enquête` (un film
  de braquage vu côté police n'a pas d'investigation ; une enquête surnaturelle n'a pas de
  police), les deux cohabitent avec leur frontière documentée. `Thriller` reste en revanche
  un **genre** : il décrit la mécanique du récit (tension, suspense), pas son univers, et se
  cumule donc avec un thème — `Thriller` + `Policier` pour un thriller policier. Grille #4
  renvoie explicitement vers les définitions et rappelle que ces registres relèvent de la
  ligne 6.
  **`Tactique` retiré du vocabulaire fermé au passage — motif corrigé en v3.31** (voir
  cette entrée : l'usage réel du tag mélangeait deux sens incompatibles, pas un simple
  manque de volume). `Stratégie` couvre désormais explicitement les deux échelles
  (empire/économie et combats posés d'escouade) ; un tactical RPG se tague `RPG` +
  `Stratégie`. **`Tower defense` retiré séparément** — trop niche, rattaché à une époque
  de jeux navigateur/Java révolue, volume d'articles insuffisant pour créer du maillage
  (confirmé sans usage réel sur le site).
  Impact : §3 passe de ~330 à ~2700 tokens, le fichier de règles de ~6600 à ~9300.
- **v3.28** (2026-07-31, audit du registre des tags, 704 tags) : premier passage de
  contrôle qualité sur l'ensemble des tags déjà posés (pas un nouveau lot d'articles).
  Six décisions, fondées sur les co-occurrences réelles observées sur WordPress (voir
  `liste-maitresse-tags-jvmag.md` pour le détail article par article) :
  - **`Battlefield Studios` supprimé, fusionné dans `Battlefield`** — n'apparaît jamais
    sans `Battlefield` (1 usage, aucune réutilisation cross-franchise), contrairement à
    `Take-Two Interactive` qui couvre plusieurs studios distincts. Une paire de tags qui
    coïncide à 100% avec un tag déjà existant n'apporte aucun angle de reco propre.
  - **`Cross-play` retiré du vocabulaire fermé (§5)** — sur ses 2 usages réels, toujours
    posé aux côtés de `En ligne` ET `Multijoueur` déjà présents : n'a jamais porté de
    distinction propre en pratique (raisonnement enrichi en v3.31 avec les trois tests
    d'admission de §5).
  - **`Maritime` retiré du vocabulaire fermé (§5)** — 1 seul usage réel, aucune
    récurrence observée.
  - **`Sony Pictures Television` supprimé, fusionné dans `Sony Pictures`** —
    contrairement à `Sony` (gaming/matériel/corporate) vs `Sony Pictures` (cinéma), qui
    n'ont *aucun* recoupement d'audience réel (vérifié sur les 6 + 4 usages), la
    distinction animation/prises de vues réelles ou cinéma/télévision au sein du même
    studio de production n'ouvre pas d'angle de reco distinct. `Sony Interactive
    Entertainment` (déjà déprécié en v3.24, 0 usage) supprimé pour de bon — vrai
    doublon orphelin, pas une correction de règle.
  - **`Pokémon GO` supprimé, fusionné dans `Pokémon`** — même logique que
    `Alien`/`Alien: Earth` (v3.17) : l'ombrelle `Pokémon` suffit, la distinction se fait
    déjà par `Mobile` + `Niantic` (§2, paire déjà actée), sans perte d'info sur l'unique
    article concerné.
  - **`UGREEN NASync` supprimé, fusionné dans `Ugreen`** (au passage : casse harmonisée
    sur `Ugreen`, cf. incident `ATLUS`/`Ugreen` de casse déjà rencontré) — même
    situation que Battlefield Studios, un sous-tag gamme qui n'existe jamais sans son
    tag marque.
  - **`WW1`/`WW2`/`Guerre froide` et `Guerre` (§5) rendus mutuellement exclusifs** —
    jusqu'ici appliqués de façon incohérente (parfois `Guerre` + le conflit précis
    ensemble, parfois le conflit précis seul). Nouvelle règle : un contenu de guerre
    reçoit EXACTEMENT un des quatre tags. `Guerre` devient le générique réservé aux
    contextes modernes/fictionnels/non rattachés à un conflit historique précis —
    jamais posé en plus de `WW1`/`WW2`/`Guerre froide` sur le même article, pour éviter
    qu'il ne devienne un tag fourre-tout.
  - **`Toy Story 5` renommé `Toy Story`** — rattrapage de la règle "pas de numéro dans
    le nom de la licence" (§1), manquée à la création du tag.
  `Narratif` et le triptyque `Réflexion`/`Stratégie`/`Gestion` identifiés comme
  sous-définis (trop dépendants de la présence littérale d'un mot dans le texte plutôt
  que d'un cadre de genre explicite) — repris et résolu en v3.29.
- **v3.27** (2026-07-31, reprise du catalogue principal, lot #3) : trois décisions :
  - **`personne + œuvre-signature` (§1) restreinte aux réalisateurs/créateurs** — un·e
    acteur/actrice n'y est plus éligible par défaut. Motivé par Klara and the Sun (Jenna
    Ortega, Taika Waititi) : le rôle-signature d'un·e interprète identifie un personnage/une
    franchise précise (`Wednesday`), pas une parenté de genre/style transposable à tout le
    reste de sa filmographie comme peut l'être le film-signature d'un réalisateur. Tagger ce
    rôle sur un article sans rapport dénature le sujet réel plutôt que d'enrichir la reco.
  - **`AR` ajouté à la liste de pairing `Périphérique`** (§4) — oubli lors de l'ajout initial
    du tag : une paire de lunettes AR gaming est un matériel EXTERNE au même titre qu'un
    casque audio ou une manette, motivé par le TEST ROG XREAL R1. Précisé en v3.31 : ne
    s'applique qu'au sens matériel du mot (Pokémon GO utilise `AR` dans un sens logiciel
    qui n'entre pas dans cette paire).
  - **`EVO` et `Amazon Prime Day` ajoutés aux événements fermés** (§6) — le premier est le
    tournoi de référence mondial du jeu de combat (contexte du DLC Kenshiro, Fatal Fury: City
    of the Wolves), le second un rendez-vous commercial annuel récurrent (promo UGREEN),
    même statut que les autres événements déjà actés (Festival d'Annecy, THQ Nordic Digital
    Showcase).
  Confirmation sans changement de règle, alignée sur le précédent Halo Campaign Evolved
  (créateur historique non tagué, seul le studio dev actuel l'est via recherche ciblée) :
  `Piranha Bytes` retiré de la proposition Gothic 1 Remake — créateur historique de la
  licence, pas le studio dev actuel (`Alkimia Interactive`, déjà cité explicitement dans le
  texte).
- **v3.26** (2026-07-31, pilote lot #8) : `Chaise gaming` ajouté au vocabulaire fermé (§4),
  rejoint la famille `Périphérique` (même patron que `Casque audio`/`Clavier`/`Manette`/
  `Périphérique de Simulation` — un tag précis qui s'accompagne toujours du tag ombrelle,
  jamais à sa place). Motivé par le TEST Razer Soma Chroma (chaise gaming RGB) : aucun tag
  composant existant ne couvrait le mobilier gaming. `Festival d'Annecy` et `THQ Nordic
  Digital Showcase` ajoutés aux événements fermés (§6) — le premier apparu deux fois dans le
  même lot (annonces DC/Warner Bros. Animation, Ghostbusters: Night Shift), le second désigné
  par l'article lui-même comme rendez-vous annuel récurrent ("l'an dernier, le Digital Showcase
  2025"), même statut que `Xbox Games Showcase`/`State of Play`. Confirmation (pas de
  changement de règle) : `Star Wars Eclipse` ne reçoit pas de tag séparé de `Star Wars` — même
  logique que la décision `Alien`/`Alien: Earth` (v3.17) déjà actée, l'ombrelle cross-media
  couvre aussi les jeux annoncés/en développement rattachés à une franchise déjà taguée.
  Décision de ne PAS étendre `Sport` (§3) aux produits réels adjacents à un événement sportif
  (ballon connecté Adidas Trionda, Coupe du Monde 2026) — `Sport` reste un genre d'œuvre
  (jeu/film/série), pas un thème "sport en général" au sens où `IA`/`Robot` couvrent
  explicitement réel et fiction ; loggée dans le journal, pas un changement de vocabulaire.
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