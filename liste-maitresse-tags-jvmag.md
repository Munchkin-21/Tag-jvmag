# Journal des tags — JVMag

> Ce fichier n'est plus un inventaire de tags. Il a trois rôles :
> 1. **Journal des lots traités** par le pipeline d'automatisation (`scripts/`), avec le détail des
>    tags posés et le raisonnement — c'est ici, et nulle part ailleurs, que vit l'historique complet.
> 2. **Décisions ouvertes à surveiller** — cas tranchés au fil de l'eau qui ne méritaient pas
>    forcément un amendement formel de [regles-tagging-actives.md](regles-tagging-actives.md),
>    mais qu'il faut garder en tête pour rester cohérent.
> 3. **Journal des nettoyages** — corrections apportées à des tags hérités d'avant l'automatisation.
>
> Pour savoir **quels tags existent déjà** sur le site : c'est lu en direct via l'API WordPress
> (`scripts/wp_client.py::list_all_tags()`), plus besoin de le recopier ici — `fetch_batch.py`
> embarque ce snapshot dans chaque lot exporté.
> Pour savoir **quelles règles appliquer** (vocabulaire fermé compris) : voir
> [regles-tagging-actives.md](regles-tagging-actives.md), seule source de vérité pour les règles
> actives. Le raisonnement historique derrière chaque règle vit dans
> [changelog-nomenclature.md](changelog-nomenclature.md) — les règles elles-mêmes n'y sont jamais
> définies, juste expliquées.

---

## Journal des lots

### Pilote pré-automatisation (échantillon représentatif, 50 articles)
- **TEST Echo Generation 2** : Echo Generation · Deckbuilder · Narratif · Solo · Science-fiction · Zombies · Années 80 *(ni plateforme ni studio cités → incertitudes)*
- **Hitman Remastered** : Hitman · IO Interactive · Saber Interactive · PC · PlayStation · Xbox · Action · Infiltration · Remaster
- **Gears of War: E-Day** : Gears of War · The Coalition · Xbox Game Studios · Xbox · PC · TPS · Science-fiction
- **Final Fantasy VII Revelation** : Final Fantasy · Square Enix · PlayStation · PC · Action-RPG · Remake
- **Stranger Than Heaven** : Stranger Than Heaven · SEGA · Action · Tupac · Snoop Dogg *(Yakuza = pedigree, non tagué)*
- **BYD × Cannes** : BYD · Mediawan · Cinéma · Festival de Cannes
- **Interview Adeline Chetail** : Adeline Chetail · Doublage · The Last of Us · The Legend of Zelda · Clair Obscur: Expédition 33 · Polymanga · Suisse
- **Carnet noir Anthony Head** : Anthony Head · Carnet noir · Buffy contre les vampires · Ted Lasso · Merlin
- **Red Bull Gamerations** : Red Bull Gamerations · Red Bull · Esport · Rétro · Suisse
- **Guide carte mère** : Carte mère · Matériel PC · Montage PC · PC · AMD · Intel
- **BYD Dolphin G DM-i** : BYD · Voiture · Voiture hybride
- **Robots humanoïdes Chine** : Robot · IA · Chine · Unitree
- **ARENA Cinemas (programme)** : ARENA Cinemas · Cinéma · Suisse

### Lot #1 — 2026-07-29 (premier lot post-automatisation, 5 articles)
- **Dragon Age, un Remaster presque impossible** : Dragon Age · BioWare · Remaster · RPG · Fantasy
  *(genre + univers déduits de la licence connue, non cités littéralement — trait stable ;
  plateforme non citée → incertitude, non déduite car fait contextuel)*
- **Crazy Taxi: World Tour, test multijoueur** : Crazy Taxi · SEGA · Course · PC · PlayStation ·
  Xbox · Nintendo Switch · Multijoueur · Cross-play · En ligne *(Cross-play et En ligne posés pour
  la première fois sur le site : vocabulaire fermé valide même si jamais utilisé avant)*
- **PlayStation Plus Essential, jeux du mois** : PlayStation · PlayStation Plus *(service distinct
  de la plateforme ; les 3 jeux de la liste non tagués individuellement — règle "listes")*
- **Below (Netflix)** : Below · Netflix · Thriller · Science-fiction · Maritime · Josh Hartnett
  *(vedette-hook nommée dans le titre taguée ; casting secondaire non taguée ; pas de tag Horreur
  car l'article se revendique lui-même thriller/SF)*
- **Disney+ sans 4K (Allemagne/Belgique/France)** : Disney+ · Allemagne · Belgique · France
  *(3 pays tagués car acteurs centraux du problème ; Suisse non taguée car mentionnée uniquement
  comme non concernée — cas négatif de la règle §7)*

Nouveaux tags créés : `Dragon Age`, `BioWare`, `Cross-play`, `En ligne`, `PlayStation Plus`,
`Below`, `Maritime`, `Josh Hartnett`, `Disney+`, `Allemagne`, `Belgique`, `France`.
Amendements → v3.5 : trait stable vs fait contextuel, service vs plateforme, cas négatif Suisse.

### Lot #2 — 2026-07-29 (5 articles + 1 legacy migré)
- **BioEden** : BioEden · Broken Arms Games · Focus Entertainment · Simulation · Gestion · Xbox ·
  PlayStation · Nintendo Switch · PC · Science-fiction · Espace *(univers spatial déduit même si
  l'article se concentre sur le gameplay — voir rappel §5)*
- **Cinémas de Sierre (programme n°31)** : Cinémas de Sierre · Cinéma · Suisse *(enseigne locale,
  pas de tag ville ; Spider-Man: Brand New Day non tagué — le sujet réel est "les prochaines
  sorties du cinéma", pas le film ; ancien tag `Sierre` supprimé et migré sur l'article legacy
  concerné, #111470)*
- **ARENA Cinemas (programme, avec Spider-Man)** : ARENA Cinemas · Cinéma · Suisse *(même logique :
  le film vedette d'un programme n'est pas le sujet de l'article)*
- **Intel Core 2 Duo, 20 ans** : Intel · AMD · Processeur · PC *(pas de `Rétro` — anniversaire
  matériel ≠ rétro-gaming, voir clarification §4/§5)*
- **ZeroSpace (RTS/RPG)** : ZeroSpace · Starlance Studios · Ironward · Stratégie · RPG ·
  Science-fiction · Espace · Solo · Multijoueur · Coopératif · PC

Nouveaux tags créés : `BioEden`, `Broken Arms Games`, `Focus Entertainment`, `Cinémas de Sierre`,
`ZeroSpace`, `Starlance Studios`, `Ironward`.
Tag supprimé : `Sierre` (id 2802, tag de ville hérité contraire à la règle §7).
Amendements → v3.6 : `Rétro` recadré au rétro-gaming, rappel §5 pour les jeux, nommage des
enseignes locales.
Article volontairement écarté : `Jumanji: Open World` (id 114285, encore en rédaction), mis dans
`scripts/state.json::skipped` — à retaguer une fois publié.

### Lot #3 — 2026-07-29 (5 articles)
- **STALKER 2 : Cost of Hope (DLC)** : STALKER · GSC Game World · FPS · Survie ·
  Post-apocalyptique · PC · Xbox · PlayStation *(FPS/Survie déduits de la licence connue — trait
  stable — texte centré sur le narratif du DLC)*
- **Suika Game (PS5/PC)** : Suika Game · Réflexion · PC · PlayStation · Nintendo Switch · Mobile
  *(studio développeur non cité dans le texte → non déduit, pas de tag ; pas jugé assez important
  pour amender la règle)*
- **Hard Worker (MMO construction)** : Hard Worker · REGION 23 · Simulation · Gestion · MMO ·
  Monde ouvert · Coopératif · Multijoueur · PC
- **Dan Houser (Rockstar) sur les jeux physiques** : Dan Houser · Rockstar Games ·
  Grand Theft Auto · San Diego Comic-Con *(première application de la règle "personne +
  œuvre-signature" : GTA/Rockstar taggés bien que l'article ne parle pas d'eux directement, pour
  la reco envers les fans de GTA)*
- **SDCC Jour 2, récap annonces** : Cinéma · San Diego Comic-Con *(roundup multi-titres — aucune
  œuvre individuelle taguée, règle "listes = pas de tags" ; première utilisation du tag SDCC)*

Nouveaux tags créés : `STALKER`, `GSC Game World`, `Suika Game`, `Hard Worker`, `REGION 23`,
`Dan Houser`, `San Diego Comic-Con`.
Amendements → v3.7 : règle *personne taguée + son œuvre-signature* ; `San Diego Comic-Con` ajouté
aux événements fermés (§6).
Cas mineur non formalisé : studio développeur de Suika Game non cité → non déduit, laissé tel quel.

### Lot #4 — 2026-07-29 (5 articles)
- **TEST Denshattack!** : Denshattack! · Undercoders · Sport · Plateforme · Post-apocalyptique ·
  Nintendo Switch · Indé *(genre trick/scoring → `Sport`, pas `Course` ; techniques graphiques
  comme le cel-shading restent exclues même très mises en avant dans le test)*
- **Carnet noir Chuck Russell** : Chuck Russell · Carnet noir · The Mask · A Nightmare on Elm
  Street · The Blob · Le Roi Scorpion *(personne + œuvres-signature développées dans le texte ;
  Eraser et Witchboard cités trop brièvement pour être taggés — mention anecdotique)*
- **Sega Rally sur émulateur Model 2** : Sega Rally · SEGA · Wanszai · Course · Rétro · PC · Xbox ·
  Multijoueur · En ligne *(Rétro pleinement justifié ici, vrai contenu rétrogaming ; pas de genre
  `Rally` distinct, `Course` reste générique ; Daytona USA/Virtua Fighter/Virtua Cop cités comme
  souhaits futurs non couverts, non tagués)*
- **Rachat Warner Bros. par Paramount, suspendu** : Warner Bros. · Paramount · Cinéma *(retiré puis
  remis : la catégorie "News Films" couvre déjà le média, mais `Cinéma` reste l'exception
  transversale salle/industrie/festival déjà actée — même logique que BYD × Cannes ; Netflix cité
  comme argument dans le dossier antitrust, non taguée — rôle de référence, pas sujet)*
- **Stargate, #SaveStargate à la SDCC** : Stargate · Amazon MGM Studios · San Diego Comic-Con ·
  Science-fiction · Espace *(univers spatial déduit de la licence connue — trait stable, même
  logique que Dragon Age/BioEden/ZeroSpace)*

Nouveaux tags créés : `Denshattack!`, `Undercoders`, `Sport`, `Chuck Russell`, `The Mask`,
`A Nightmare on Elm Street`, `The Blob`, `Le Roi Scorpion`, `Sega Rally`, `Wanszai`.
Amendements → v3.8 : `Sport` précisé pour les jeux de trick/scoring type skateboard.
Décision (pas d'amendement) : pas de genre `Rally` distinct de `Course` — à réévaluer si le rally
revient souvent sur le site.
Résolu : `Cinéma` un temps retiré de l'article Warner Bros./Paramount, puis remis — la règle
existante était déjà correcte.

### Lot #5 — 2026-07-29 (10 articles)
- **Rings of Power S3 (Nazgnagôl)** : Le Seigneur des Anneaux · Prime Video · Fantasy
- **Scrooge (Johnny Depp)** : Scrooge · Comédie · Fantastique *(pas de tag Horreur malgré le texte
  — "à la frontière de l'horreur" jugé trop timide ; pas de tag Johnny Depp — le film est le sujet,
  pas l'acteur, voir clarification vedette-hook §1)*
- **Preview Honkai: Nexus Anima** : Honkai · HoYoverse · Stratégie · Gestion · Aventure ·
  Monde ouvert · PC · Mobile *(licence consolidée sur `Honkai`, pas `Honkai: Nexus Anima` — genre
  différencie en interne, comme Final Fantasy ; Genshin Impact/Pokémon/Teamfight Tactics non
  tagués — comparaisons ; MMO écarté après vérification externe : creature-collector/autobattler,
  pas un MMO)*
- **Xbox cloud gaming gratuit contre pub** : Microsoft · Xbox · Cloud gaming · Xbox Game Pass
- **TEST Conker: Live & Reloaded** : Conker · Rare · PC · Xbox · Xbox Game Pass · Plateforme ·
  Rétro · Remake *(pas de Multijoueur/Coopératif — l'en ligne est cassé dans ce portage précis)*
- **Aliens: Fireteam Elite 2** : Alien · Cold Iron Studios · Daybreak Game Company · TPS ·
  Science-fiction · Horreur · Coopératif · Multijoueur · PC · Xbox · PlayStation
- **Atari × Universal (10 jeux adaptés)** : Universal · Cinéma · Atari *(liste de 10 titres, aucun
  taggé individuellement — règle "listes", même Pong malgré le clin d'œil de l'article)*
- **Marvel's Wolverine, trailer scénario** : Wolverine · Insomniac Games · PlayStation Studios ·
  Marvel · Action-aventure · Super-héros · PlayStation *(genre + éditeur first-party déduits du
  studio connu — trait stable)*
- **TEST Halo Campaign Evolved** : Halo · Xbox Game Studios · FPS · Science-fiction · Espace ·
  Remake · PC · Xbox · PlayStation · Coopératif · Multijoueur · Cross-play · En ligne ·
  Xbox Game Pass *(14 tags, test très dense et explicite ; pas de tag studio dev — seul Bungie est
  cité, comme créateur historique/pedigree, le studio actuel n'est jamais nommé dans le texte :
  gap éditorial de l'article, pas un cas d'extension du trait stable au studio dev)*
- **Coyote vs. Acme** : Warner Bros. · Comédie · Animation · Looney Tunes *(pas de tag Suisse —
  jugement au cas par cas, pas un changement de règle §7)*

Nouveaux tags créés : `Le Seigneur des Anneaux`, `Scrooge`, `Honkai`, `Conker`, `Rare`,
`Cold Iron Studios`, `Daybreak Game Company`, `Atari`, `Looney Tunes`.
Amendements → v3.9 : `Gratuit` retiré du vocabulaire fermé (prix jugé pas assez connecteur pour la
reco) ; clarification de la règle vedette-hook (§1) — Johnny Depp non taggé sur Scrooge.
Vérification externe (WebSearch) : Honkai: Nexus Anima n'est pas un MMO — confirmé.
Cas isolé, pas de règle : Suisse retiré de Coyote vs. Acme (jugement au cas par cas).
Constat éditorial (hors tagging) : l'article Halo Campaign Evolved ne cite jamais le studio dev
actuel (Halo Studios), seulement Bungie comme créateur historique — gap côté rédaction.

### Lot #6 — 2026-07-29 (10 articles)
- **Resident Evil (Zach Cregger), trailer** : Resident Evil · Capcom · Sony Pictures · Horreur
  *(Zach Cregger non taggé malgré ses citations dans l'article — le film reste le sujet, règle
  vedette-hook)*
- **LEGO Donkey Kong** : Donkey Kong · LEGO · Nintendo · Rétro *(Rétro justifié par le sujet du
  contenu — rétrogaming/nostalgie arcade — pas par l'objet lui-même ; pas de genre Plateforme, le
  sujet est le produit dérivé pas le jeu ; Steve Wiebe cité en bonus, non taggé)*
- **Dear Passengers** : Dear Passengers · Party game · Coopératif · Multijoueur · PC *(studio non
  cité)*
- **Xbox rétrocompatibilité PC (4 jeux)** : Microsoft · Xbox · PC · Xbox Game Pass · Rétro ·
  Cloud gaming · Conker · BLiNX: The Time Sweeper · Crimson Skies · Fuzion Frenzy *(exception à
  "listes = pas de tags" : 4 jeux individuellement et concrètement disponibles, impact de reco réel)*
- **Clayface (DC)** : Clayface · DC · Warner Bros. · Horreur · Thriller *(Thriller car le texte le
  dit explicitement, pas de structure policière/enquête ici — différent de Fantômas ci-dessous)*
- **Hasbro × Nintendo, figurines Zelda** : The Legend of Zelda · Hasbro · Nintendo ·
  San Diego Comic-Con
- **NBA 2K27** : NBA 2K · 2K · Visual Concepts · Sport · Multijoueur · PC · PlayStation · Xbox ·
  Nintendo Switch *(`2K` gardé distinct de `NBA 2K` : l'éditeur publie aussi WWE 2K, Civilization,
  XCOM, Bioshock, Borderlands, Mafia — même logique que Square Enix/Final Fantasy)*
- **Fantômas – Le Nouveau Monde** : Fantômas · Policier · Enquête *(Policier = genre structurel,
  Enquête = thème suivi ; trilogie De Funès/Hunebelle citée comme contexte historique, non taguée ;
  Batman cité en comparaison, non taggé)*
- **Samsung Galaxy Z Fold 8/Flip 8** : Samsung · Smartphone · Suisse *(section "Prix en Suisse"
  dédiée avec tarifs CHF détaillés — un des cas Suisse les plus explicites à date)*
- **Samsung Galaxy Watch9/Ultra2** : Samsung · Montre connectée · Suisse *(première utilisation de
  la nouvelle catégorie fermée)*

Nouveaux tags créés : `Donkey Kong`, `LEGO`, `Dear Passengers`, `BLiNX: The Time Sweeper`,
`Crimson Skies`, `Fuzion Frenzy`, `Clayface`, `DC`, `Hasbro`, `The Legend of Zelda`, `NBA 2K`, `2K`,
`Visual Concepts`, `Fantômas`, `Samsung`, `Smartphone`, `Montre connectée`.
Amendements → v3.10 : ajout de `Montre connectée` (§4) ; exception "listes" pour les courtes listes
(≤5) d'éléments individuellement et concrètement disponibles.
Découverte notable : `The Legend of Zelda` n'existait en fait pas encore sur WordPress, malgré une
mention dans l'ancien inventaire statique pré-automatisation — confirme que l'API live est la
seule source fiable.

### Lot #7 — 2026-07-29 (10 articles, premier lot avec la Grille de tagging obligatoire)
- **VectaGuard (jeu vectoriel rétro-inspiré)** : VectaGuard · Tony Barnes · RetroNinja ·
  Shoot'em up · PC · En ligne *(Tony Barnes taggé — nommé au titre, bio développée — mais pas ses
  jeux passés : l'œuvre du moment est déjà taguée, cohérent avec la règle Depp/Scrooge ; pas de
  `Rétro` — esthétique vectorielle = style/technique, pas du vrai contenu rétro-gaming, voir §5)*
- **Scarlet Deer Inn** : Scarlet Deer Inn · Aventure · Mythologie · PC · Indé *(indé confirmé par
  recherche externe — développé par Attu Games, studio tchèque de 3 personnes — mais le studio
  lui-même n'est pas taggé, absent du texte)*
- **Interdiction réseaux sociaux <15 ans en France** : France *(1 seul tag — aucun autre facteur
  applicable, sujet société/légal hors du champ gaming/divertissement habituel ; idée à explorer
  plus tard : un tag pour ce type de sujet société-tech, pas tranché)*
- **DENZA (BYD) arrive en Suisse** : BYD · DENZA · Voiture · Suisse *(motorisation non précisée
  dans le texte → tag générique Voiture seulement, pas de Voiture hybride/électrique)*
- **Wreckreation 2** : Wreckreation · When Tides Turn · Course · PC · Xbox · PlayStation ·
  Monde ouvert · En ligne *(Fiona Sperry non taguée — son passé chez Criterion Games est un
  pedigree, pas le sujet de l'article)*
- **Kylian Mbappé, jaquette EA SPORTS FC 27** : EA SPORTS FC · Kylian Mbappé · Electronic Arts ·
  Sport · Mobile · PlayStation · Xbox *(cas particulier : PlayStation/Xbox ajoutés manuellement
  sur demande explicite malgré la règle "plateforme jamais déduite" — la règle générale reste
  inchangée, exception ponctuelle assumée pour ce seul article)*
- **Licenciements chez Pixar (Disney)** : Disney · Pixar · Cinéma *(actu industrie → `Cinéma`
  s'applique ; Toy Story 5 cité comme contexte ironique, non taggé — pas le sujet)*
- **Razer Seiren V3 Chroma (micro)** : Razer · Microphone *(première utilisation de la nouvelle
  catégorie fermée `Microphone`)*
- **Spider-Man: Brand New Day, 3e trailer** : Spider-Man · Sony Pictures · Marvel · Super-héros
  *(pas de `Cinéma` — règle testée par l'utilisateur : réservé aux actus d'industrie/festival,
  jamais à la couverture normale d'un film précis, comme Scrooge/Clayface/Coyote vs. Acme/Fantômas
  avant lui)*
- **Xbox Game Pass, jeux de juillet (2e salve)** : Microsoft · Xbox · PC · Cloud gaming ·
  Xbox Game Pass *(liste de 16 jeux — 8 qui arrivent + 8 qui partent — aucun taggé individuellement,
  dépasse le seuil ≤5 ; `Halo: Campaign Evolved` cité mais pas retaggé malgré le tag déjà existant)*

Nouveaux tags créés : `VectaGuard`, `Tony Barnes`, `RetroNinja`, `Scarlet Deer Inn`, `DENZA`, `BYD`,
`Wreckreation`, `When Tides Turn`, `EA SPORTS FC`, `Kylian Mbappé`, `Pixar`, `Razer`, `Microphone`,
`Spider-Man`.
Amendements → v3.12 : `Microphone` ajouté au vocabulaire fermé (§4) ; précision §5 EXCLUS sur le
style rétro-inspiré vs vrai contenu rétro-gaming ; confirmation que la règle "plateforme jamais
déduite" reste absolue (pas d'exception pour les franchises sportives annuelles).
Incident technique : une erreur 429 (rate limit WordPress) a interrompu l'application du lot en
cours de route — grâce à la sauvegarde incrémentale de l'état ajoutée lors de l'audit, aucun
article déjà traité n'a été perdu, reprise immédiate sans doublon.

**Correction post-lot #7** : `Périphérique` avait été retiré à tort de l'article Razer Seiren
(remplacé par `Microphone` seul). Vérification de l'historique : le seul précédent existant
(accessoires PlayStation, écran + pad) combinait `Périphérique` AVEC les tags précis `Écran` et
`Manette`, pas à leur place. Corrigé → v3.13 : `Périphérique` s'applique désormais en plus d'un
tag matériel externe précis, jamais à sa place. `Manette` ajoutée au vocabulaire fermé (§4).

---

## Audit général — 2026-07-29

Premier audit complet du pipeline après 6 lots (41 articles traités). Voir aussi les 3 fixes de
code dans `scripts/` (docstring `list_all_tags`, sauvegarde incrémentale de l'état dans
`apply_batch.py`, message si lot incomplet dans `fetch_batch.py`).

**Réorganisation documentaire** : les listes de vocabulaire fermé (§3 à §6) sont maintenant triées
alphabétiquement dans `regles-tagging-actives.md` pour rester scannables. La section "Exemples
validés" (qui avait grossi à 136 lignes) a été déplacée ici, dans le Journal des lots — le fichier
de nomenclature ne contient plus que les règles actives.

**Correction** : `Xbox Showcase` → `Xbox Games Showcase` dans §6 — le doc avait le mauvais nom,
le vrai tag WordPress (12 articles) s'appelle `Xbox Games Showcase`.

**v3.11 — Grille de tagging obligatoire.** Suite à discussion : le checklist "Structure d'un
article" et l'ancienne "Étape de proposition" (§ Gouvernance) faisaient doublon et restaient de
simples rappels facultatifs — §5 (thème/univers) a été oublié deux fois malgré ça (BioEden,
rattrapé seul ; Stargate, rattrapé par l'utilisateur). Les deux sont remplacés par une seule
**Grille de tagging obligatoire** (tableau à 12 lignes, une par facette, en tête de doc) à
parcourir intégralement pour chaque article — chaque ligne doit être explicitement tranchée
(tag posé ou raison de non-application), jamais silencieusement sautée. Ajout aussi de la règle
**produit dérivé** (§2) : licence/marque taguée sur un jouet/figurine, jamais le genre du jeu
source — règle qu'on appliquait déjà en pratique (LEGO Donkey Kong, figurines Zelda) sans
jamais l'avoir écrite.

**Nettoyage de tags hérités d'avant l'automatisation** (aucun de nos 6 lots n'était concerné,
tous vérifiés à 1 article d'usage avant correction) :
- `Deer &amp; Boy` → `Deer & Boy` et `Point &amp; click` → `Point & click` : bug d'encodage HTML
  hérité (l'entité `&amp;` était stockée littéralement au lieu du caractère `&`). Invisible dans
  l'admin WordPress (le navigateur décode l'entité à l'affichage) mais bien réel via l'API REST —
  aurait causé un doublon la prochaine fois que `Point & click` (genre fermé) aurait été posé.
- `assassin's creed` → `Assassin's Creed` : casse corrigée (article #113164).
- `piraterie` fusionné dans `Pirates` (déjà dans le vocabulaire fermé §5) : tag `Pirates` créé,
  posé sur l'article #113164 à la place, `piraterie` supprimé.
- `tactical rpg` fusionné dans `Tactique` + `RPG` (deux tags fermés déjà existants) : posés sur
  l'article #113049 à la place, `tactical rpg` supprimé.

**Vérifié et écarté** (pas des erreurs) : `gen ATLAS` et `genDESIGN` sont des noms stylisés réels
(le jeu et son studio, fondé par Fumito Ueda) — casse intentionnelle, pas une faute.

**Laissé en l'état, pas encore tranché** : le tag `dungeon crawler` (minuscule, article #113049)
n'est pas dans le vocabulaire fermé §3 — casse à corriger et/ou vocabulaire à amender, discussion
à poursuivre.

### Lot #8 — 2026-07-29 (20 articles, premier lot à taille doublée)
- **Batman: Knightfall** : Batman · Warner Bros. · DC · Mir · Animation · Super-héros
- **LEGO The X-Files** : The X-Files · LEGO · Science-fiction · Enquête
- **Other Mommy** : Other Mommy · Jessica Chastain · Blumhouse · Universal · Horreur
- **Glorious GHS Wireless InfinitePlay** : Glorious · Casque audio · Périphérique · PC ·
  PlayStation · Nintendo Switch
- **TEST Splatoon Raiders** : Splatoon · Nintendo · TPS · Roguelike · Nintendo Switch ·
  Coopératif · Multijoueur · En ligne · Solo
- **NVIDIA DLSS 5** : NVIDIA · Carte graphique *(SIGGRAPH cité, pas ajouté au vocabulaire)*
- **DCKO** : DC · DCKO · Drop Fake · Warner Bros. · Combat · Mobile · Super-héros · Multijoueur ·
  En ligne · Compétitif
- **Call of Duty: Modern Warfare 4 (bêta)** : Call of Duty · Activision · Infinity Ward · FPS ·
  PlayStation · Xbox · PC · Nintendo Switch · Guerre · Multijoueur · En ligne
- **ARENA Cinemas (programme générique)** : ARENA Cinemas · Cinéma · Suisse
- **Skatesterre** : Skatesterre · Sterre Meijer · Headup Games · Goon Squad · Sport · PC · Xbox ·
  PlayStation · Nintendo Switch *(pas de Rétro — jeu neuf inspiré des années 2000, comme
  VectaGuard ; Sterre Meijer = athlète réelle jouable, précédent Tupac/Snoop Dogg)*
- **LEGO One Piece** : One Piece · LEGO · Shueisha · Atomic Cartoons · Animation · Aventure ·
  Netflix · Pirates
- **Avengers: Doomsday (trailer)** : Avengers · Marvel · X-Men · Super-héros *(X-Men taggé — leur
  arrivée dans le MCU est développée comme "la vraie bombe" de l'article ; Robert Downey Jr./Chris
  Evans non tagués malgré leurs retours notables, aucun acteur au titre, cohérent avec Spider-Man ;
  Quatre Fantastiques/Thunderbolts en simple liste, non tagués)*
- **MXGP 26: The Official Game** : MXGP · Nacon · Artefacts Studio · Course · Simulation ·
  PlayStation · Xbox · PC · Multijoueur · En ligne
- **Interview Name No Manga** : Name No Manga · Fairy Tail · Rave · Holyland · Rétro · Suisse
  *(3 œuvres développées substantiellement taguées ; Naruto/GTA/Pokémon/Mario écartés — mentions
  anecdotiques ; Rétro justifié car l'interview porte explicitement sur sa collection/passion)*
- **Cinémas de Sierre (programme, Vaiana)** : Cinémas de Sierre · Cinéma · Suisse *(même logique
  que le précédent Spider-Man du lot #2 — le programme est le sujet, pas le film en tête d'affiche)*
- **Call of Duty (film, 2028)** : Call of Duty · Paramount · Activision · Action · Guerre · Suisse
- **GTA VI — l'encyclopédie** (20 chapitres) : Grand Theft Auto · Rockstar Games ·
  Take-Two Interactive · Action-aventure · Monde ouvert · PlayStation · Xbox *(Sam Houser/Strauss
  Zelnick/Jason Schreier non tagués — portes-paroles cités à plusieurs reprises, jamais le sujet)*
- **GTA III/Vice City modé dans San Andreas** : Grand Theft Auto · Dryxio · Action-aventure ·
  Monde ouvert · PC *(Dryxio = moddeur individuel, précédent Wanszai)*
- **THEA1200 (clone Amiga)** : Amiga · Retro Games Ltd. · Rétro *(vrai matériel/logiciel d'époque
  — confirme la distinction v3.12 par contraste avec Skatesterre ci-dessus)*
- **Spider-Man: Brand New Day, minuit à l'ARENA Fribourg** : Spider-Man · Marvel · ARENA Cinemas ·
  Super-héros · Suisse

Nouveaux tags créés : `Batman`, `Mir`, `The X-Files`,
`Other Mommy`, `Jessica Chastain`, `Blumhouse`, `Glorious`, `Casque audio`, `Splatoon`, `NVIDIA`,
`Carte graphique`, `DCKO`, `Drop Fake`, `Call of Duty`, `Infinity Ward`, `Skatesterre`,
`Sterre Meijer`, `Headup Games`, `Goon Squad`, `One Piece`, `Shueisha`, `Atomic Cartoons`,
`Avengers`, `X-Men`, `MXGP`, `Nacon`, `Artefacts Studio`, `Name No Manga`, `Fairy Tail`, `Rave`,
`Holyland`, `Take-Two Interactive`, `Dryxio`, `Amiga`, `Retro Games Ltd.`.
Deux gaps d'événements repérés (Festival d'Annecy, SIGGRAPH) — décision de ne PAS les ajouter au
vocabulaire fermé §6, jugés pas assez pertinents/récurrents pour l'instant.
Confirmations utiles : la distinction v3.12 (style rétro-inspiré ≠ `Rétro`) testée sur 2 cas
opposés dans le même lot — `Skatesterre` (jeu neuf, pas de Rétro) vs `THEA1200` (vrai matériel
Amiga, Rétro justifié) ; précédent `Sterre Meijer` confirme que le patron `Wanszai`/`Dryxio`
(créateur individuel taggé) s'étend bien aux athlètes réels représentés en jeu (même logique que
Tupac/Snoop Dogg) ; interview Name No Manga : 3 œuvres tagués sur les ~8 mentionnées (Fairy Tail,
Rave, Holyland — substantiellement développées), le reste écarté comme anecdotique.
Premier test d'un lot à 20 articles (au lieu de 10) — RAS côté qualité, aucune facette oubliée
malgré le volume.

### Lot #9 — 2026-07-29 (20 articles)
- **Bethesda (Starfield/Fallout/Elder Scrolls VI)** : Starfield · Fallout · The Elder Scrolls ·
  Bethesda Game Studios · Obsidian Entertainment · RPG · Science-fiction · Espace ·
  Post-apocalyptique · Fantasy *(3 licences développées substantiellement, toutes taguées)*
- **GameStop (Ryan Cohen)** : Ryan Cohen · GameStop · PlayStation
- **Zenless Zone Zero, anniversaire** : Zenless Zone Zero · HoYoverse · Action-RPG · Xbox ·
  Science-fiction
- **WW1: Gallipoli** : Blackmill Games · FPS · PC · PlayStation · Xbox · WW1 *(pas de tag licence
  séparé — la saga n'a pas de nom de marque distinct de son thème `WW1`, qui fait double usage)*
- **God of War (série), Ryan Hurst blessé** : God of War · Ryan Hurst · Sony Pictures Television ·
  Amazon MGM Studios · Prime Video · Mythologie
- **Cosmo Tales** : Cosmo Tales · Bohemia Interactive · Roguelike · Action-aventure ·
  Science-fiction · Espace *(pas de Rétro — esthétique rétrofuturiste = style, v3.12)*
- **Dreame T16 Pro Heat (aspirateur)** : Dreame · Aspirateur robot · Suisse *(première utilisation
  de la nouvelle catégorie fermée)*
- **Hela: of Mice & Magic** : Hela: of Mice & Magic · Aventure · PC · Xbox · PlayStation ·
  Nintendo Switch · Mythologie · Fantasy · Solo · Coopératif *(studio non nommé dans le texte)*
- **Call of Duty MW4 (re-couverture)** : Call of Duty · Activision · Infinity Ward · FPS · Xbox ·
  PlayStation · Nintendo Switch · PC · Guerre · Multijoueur *(tout existant, bonne consolidation)*
- **Ratchet & Clank: Ranger Rumble** : Ratchet & Clank · Sony Interactive Entertainment · Oh BiBi ·
  TPS · Battle royale · Mobile · Science-fiction · Espace · Multijoueur · Compétitif · En ligne
- **OKU** : OKU · Irox Games · ByteRockers' Games · Aventure · PC · Indé
- **Razer × Pokémon** : Pokémon · Razer · Casque audio · Clavier · Souris · Périphérique
- **PlayStation Plus, jeux de juillet** : PlayStation · PlayStation Plus *(9 jeux listés, aucun
  taggé individuellement)*
- **The Duskbloods (FromSoftware)** : The Duskbloods · FromSoftware · Action · Nintendo Switch ·
  Multijoueur · En ligne
- **The Batman Part II** : Batman · Warner Bros. · DC · Super-héros · Suisse
- **I Play Rocky (biopic)** : I Play Rocky · Rocky · Sylvester Stallone · Amazon MGM Studios ·
  Biopic *(franchise dépeinte ET film biopic tagués ensemble — cas distinct du double
  franchise+sous-saga habituel)*
- **Netflix, IA générative** : Netflix · IA · Ted Sarandos *(correction en cours de lot — voir
  Changelog v3.14)*
- **Studios japonais et l'IA** : Japon · IA *(idem)*
- **Criterion Games → Battlefield only** : Need for Speed · Burnout · Battlefield · Rebecka Coutaz
  · Criterion Games · Electronic Arts *(NF Speed/Burnout taggés — sujet du titre lui-même, pas du
  pedigree ; fondateurs historiques Alex Ward/Fiona Sperry non tagués)*
- **Wabisabi SushiDerby** : Wabisabi SushiDerby · ITAMAE Studio · Kodansha · Course · Simulation ·
  Nintendo Switch · PC

Nouveaux tags créés : `Starfield`, `Fallout`, `The Elder Scrolls`, `Bethesda Game Studios`,
`Obsidian Entertainment`, `Ryan Cohen`, `GameStop`, `Blackmill Games`, `Ted Sarandos`,
`Ryan Hurst`, `Sony Pictures Television`, `Cosmo Tales`, `Bohemia Interactive`, `Dreame`,
`Aspirateur robot`, `Hela: of Mice & Magic`, `Ratchet & Clank`, `Sony Interactive Entertainment`,
`Oh BiBi`, `Battle royale`, `OKU`, `Irox Games`, `ByteRockers' Games`, `Clavier`, `Souris`,
`The Duskbloods`, `FromSoftware`, `I Play Rocky`, `Rocky`, `Sylvester Stallone`, `Biopic`,
`Need for Speed`, `Burnout`, `Battlefield`, `Rebecka Coutaz`, `Criterion Games`,
`Wabisabi SushiDerby`, `ITAMAE Studio`, `Kodansha`.
Amendements → v3.14 : `Aspirateur robot` ajouté (§4) ; clarification `IA`/`Robot` (§5) couvrent le
contenu réel/industrie, pas seulement fictionnel — erreur d'application corrigée en cours de lot
(voir échange avec l'utilisateur, pas juste un oubli de grille mais une mauvaise interprétation de
la portée d'un tag existant, à re-vérifier systématiquement contre les précédents à l'avenir).
Sujet société-tech hors IA (régulation numérique, ex. France <15 ans) : toujours pas de tag dédié,
un seul cas à ce jour, en observation.

### Lot #10 — 2026-07-29 (20 articles, revue à contre-courant intensive)
- **The Hunt for Gollum** : Le Seigneur des Anneaux · Warner Bros. · Fantasy
- **DIEATHLON** : DIEATHLON · Long Void Games · Loopr Partners · FPS · Course · PC
- **Samsung Flex Titanium** : Samsung · Écran · Smartphone
- **Caristream** : Caristream · Le Copain · Suisse
- **Final Boss: The Video Game** : Final Boss · Bit Bot Media · Mecanimal Games · Image Comics ·
  Beat'em up · PC · Solo · Coopératif · Local · Multijoueur *(Multijoueur corrigé après coup)*
- **TEST Beastro** : Beastro · Timberline Studio · Deckbuilder · Gestion · Cosy · Roguelike · PC ·
  PlayStation · Xbox · Steam Deck · Fantasy · Xbox Game Pass · Stratégie *(Stratégie corrigée)*
- **Samsung 990 SSD** : Samsung · SSD · Suisse · Matériel PC *(Matériel PC corrigé)*
- **Battlefield 6, saison 4** : Battlefield · Electronic Arts · FPS · PC · Xbox · PlayStation ·
  Guerre · Multijoueur · En ligne *(En ligne corrigé)*
- **League of Legends Classic** : League of Legends · Riot Games · MOBA · Multijoueur ·
  Coopératif · En ligne · Compétitif *(première utilisation de MOBA)*
- **Cinémas de Sierre (L'Odyssée)** : Cinémas de Sierre · Cinéma · Suisse · L'Odyssée *(nouvelle
  règle "programme mono-film" — inverse le précédent du lot #2)*
- **GTA Online, Kortz Center Heist** : Grand Theft Auto · Rockstar Games · Take-Two Interactive ·
  Action-aventure · PlayStation · Xbox · PC · Monde ouvert · Coopératif · Multijoueur · En ligne
  *(Take-Two corrigé — paire systématique avec Rockstar Games désormais actée)*
- **Worlds Upon The Wind** : Worlds Upon The Wind · Max Shawabkeh · Roguelike · Deckbuilder ·
  Stratégie · Gestion · Cosy · PC · Post-apocalyptique · Indé
- **ARENA Cinemas (programme générique)** : ARENA Cinemas · Cinéma · Suisse
- **A Nightmare on Elm Street (reboot)** : A Nightmare on Elm Street · Paramount · Horreur
- **Crystal Lake (préquelle Vendredi 13)** : Vendredi 13 · Crystal Lake · A24 · Horreur · Peacock
  *(première utilisation de Peacock)*
- **Agent 64: Spies Never Die** : Agent 64: Spies Never Die · Replicant D6 · FPS · PC · Solo ·
  Coopératif · Multijoueur · Local · En ligne *(pas de Rétro malgré le mot dans le texte — style
  d'hommage N64, cohérent avec VectaGuard/Skatesterre/Blast Vein)*
- **Worlds of Play (Tencent, Gamescom)** : Tencent · Gamescom *(~25 jeux exposés cités, aucun
  taggé — règle listes)*
- **Digger (Tom Cruise)** : Digger · Tom Cruise · Warner Bros. · Comédie · Science-fiction
- **Meta/Instagram, IA générative** : Meta · Instagram · IA
- **Blast Vein** : Blast Vein · Greewook Studio · FPS · Roguelike · PC · Horreur *(pas de Rétro,
  même logique qu'Agent 64)*

Ce lot a servi de session de calibration : sur 20 propositions initiales, 4 vrais oublis identifiés
par l'utilisateur (Multijoueur manquant sur Final Boss malgré Coopératif/Local ; En ligne manquant
sur Battlefield 6 ; Stratégie manquée sur Beastro alors que le mot était dans le texte ;
Take-Two Interactive manquant sur l'article GTA Online alors que posé sur l'encyclopédie GTA VI du
lot #8). Tous corrigés avant application.
Nouveaux tags créés : `DIEATHLON`, `Long Void Games`, `Loopr Partners`, `Caristream`, `Le Copain`,
`Final Boss`, `Bit Bot Media`, `Mecanimal Games`, `Image Comics`, `Beat'em up`, `Local`, `Beastro`,
`Timberline Studio`, `Deckbuilder`, `Gestion`, `Cosy`, `Roguelike`, `Steam Deck`, `League of
Legends`, `Riot Games`, `MOBA`, `L'Odyssée`, `Worlds Upon The Wind`, `Max Shawabkeh`, `Vendredi 13`,
`Crystal Lake`, `Peacock`, `Agent 64: Spies Never Die`, `Replicant D6`, `Tencent`, `Gamescom`,
`Digger`, `Tom Cruise`, `Meta`, `Instagram`, `Blast Vein`, `Greewook Studio`.
Amendements → v3.15 :
- `MOBA` et `Peacock` ajoutés au vocabulaire fermé.
- `Matériel PC` formalisé comme pendant interne de `Périphérique` (composants internes vs
  matériel externe) — était déjà dans le vocabulaire mais pas appliqué systématiquement.
- `Rockstar Games` → toujours + `Take-Two Interactive` (éditeur first-party, trait stable, comme
  Xbox Game Studios). Codifié explicitement dans §2 pour éviter la prochaine incohérence.
- Nouvelle règle "programme mono-film" (§7) : un article "programme" qui ne développe qu'un seul
  film substantiellement (comme les programmes des Cinémas de Sierre, contrairement aux vraies
  programmations multi-films d'ARENA Cinemas) doit taguer ce film — réexamen du précédent posé au
  lot #2, qui suivait la règle "listes" par réflexe sans la remettre en question.
- Grille de tagging enrichie de garde-fous mécaniques : Coopératif/Compétitif ⇒ toujours
  Multijoueur ; vérifier En ligne explicitement ; relire le texte une 2e fois avant de conclure
  qu'aucun mot-clé de genre n'est présent.
Deux cas de jugement confirmés par l'utilisateur après explication : `Écran` sur une actu de
technologie d'affichage (pas un écran physique précis, même logique que Carte graphique/DLSS) ;
`Tencent` taggé malgré la règle "listes" qui exclut les ~25 jeux de son exposition (Tencent =
l'acteur/organisateur, pas un élément de la liste).
Incident technique : un deuxième crash (timeout réseau cette fois, pas un rate limit) a interrompu
l'application en cours de lot — sauvegarde incrémentale à nouveau vérifiée efficace, reprise sans
perte ni doublon sur les 4 derniers articles.

### Correction rétroactive — règle Suisse (2026-07-29)
L'utilisateur a challengé le tag `Suisse` posé sur le SSD Samsung 990 (lot #10) : un prix en CHF
donné en routine (JVMag étant un média suisse) ne fait pas de l'article un sujet suisse. Règle
resserrée en v3.16 (§7) : Suisse = la Suisse doit être l'acteur/lieu/sujet réel, pas juste la
devise d'affichage. Exception actée : si le prix/la date EST l'anomalie qui fait l'actu (plus cher
en Suisse, retard pour raison suisse), ça reste un vrai sujet.
5 articles corrigés rétroactivement (tag `Suisse` retiré, même schéma "prix/date CH routiniers") :
- Samsung 990 SSD (lot #10, #113426)
- Samsung Galaxy Watch9/Ultra2 (lot #6, #113708)
- Samsung Galaxy Z Fold 8/Flip 8 (lot #6, #113721)
- Call of Duty, le film (lot #8, #107235)
- The Batman Part II (lot #9, #113581)
Restent corrects sous la nouvelle règle (vrai sujet suisse) : DENZA (implantation active d'un
réseau de concessionnaires en Suisse), Cinémas de Sierre/ARENA Cinemas (lieux physiques suisses),
Caristream (événement caritatif suisse), interview Name No Manga (créateur basé en Suisse
romande).

### Lot #11 — 2026-07-29 (20 articles, revue à contre-courant approfondie)
- **LEGO Donkey Kong (leak)** : Donkey Kong · LEGO · Nintendo · Rétro
- **Carnet noir Sam Neill** : Jurassic Park · Sam Neill · Carnet noir *(pas de `Dinosaures` — la
  personne est le sujet, pas la franchise ; règle affinée en v3.17)*
- **TEST ASUS RTX 5070 Ti** : ASUS · NVIDIA · Carte graphique · Matériel PC
- **Agefield High: Rock the School** : Agefield High: Rock the School · Refugium Games · PC ·
  Monde ouvert · Indé *(sous-titre gardé — jeu unique, rien à consolider, contrairement à une
  franchise multi-épisodes ; indé confirmé par recherche externe)*
- **Sony/UE, jeux physiques** : Sony · PlayStation · Michael McGrath
- **TEST Arcade Archives 2 Tekken** : Tekken · Bandai Namco · Hamster Corporation · Combat · Xbox
  · PlayStation · Nintendo Switch · Multijoueur · Local · Rétro · Compétitif *(Compétitif ajouté —
  jeu de combat versus)*
- **Alien: Earth saison 2** : Alien · Science-fiction · Espace · Horreur *(pas de tag séparé pour
  la série dérivée — Alien est déjà l'ombrelle cross-media)*
- **State of Decay 3** : State of Decay · Brant Fitzgerald · Undead Labs · Survie · Xbox · PC ·
  Zombies · Post-apocalyptique · Coopératif · Multijoueur · En ligne *(En ligne ajouté)*
- **Naruto live-action** : Naruto · Lionsgate · Action · Manga *(première utilisation du tag
  transversal Manga)*
- **Tempest Rising, DLC Veti's Wrath** : Tempest Rising · Stratégie · PC · Guerre ·
  Science-fiction · Multijoueur · En ligne · Solo
- **Pokémon GO, 10 ans** : Pokémon · Pokémon GO · Mobile · AR · Niantic *(Niantic ajouté — bon
  studio pour CE produit précis, pas Game Freak qui fait les jeux principaux)*
- **Hope (Na Hong-jin, Cannes)** : Hope · Science-fiction · Espace · Festival de Cannes *(pas de
  Suisse — date CH confirmée mais routinière, cohérent v3.16)*
- **Godzilla Minus Zero** : Godzilla · TOHO · Science-fiction · CinemaCon *(2e occurrence de
  CinemaCon après Digger — ajouté au vocabulaire ; pas de Suisse — absence de date CH, pas un sujet)*
- **Dragon Ball Xenoverse 3** : Dragon Ball · Bandai Namco · Dimps · Combat · PlayStation · Xbox ·
  PC *(pas de Multijoueur/En ligne — mécaniques jamais déduites de la réputation de la série,
  même règle que pour la plateforme ; texte trop ambigu pour confirmer)*
- **Transport Fever 3** : Transport Fever · Urban Games · Paradox Interactive · Gestion ·
  Simulation · Xbox · PlayStation · PC *(pas de Course — jeu de gestion, pas de compétition)*
- **Assetto Corsa EVO, Update 0.8** : Assetto Corsa · KUNOS Simulazioni · 505 Games · Simulation
  · Course · PC · VR *(Course + Simulation légitimement ensemble ; pas de Multijoueur — non décrit
  dans ce texte précis malgré la réputation du jeu)*
- **Twisted Tower** : Twisted Tower · Atmos Games · 3D Realms · FPS · PC · Horreur · Espace ·
  Indé *("station spatiale" repérée à la 2e lecture ; indé confirmé par recherche externe)*
- **Fallout/Obsidian, Avowed 2 annulé** : Fallout · Avowed · The Outer Worlds · Grounded ·
  Josh Sawyer · Obsidian Entertainment · Bethesda Game Studios · Xbox Game Studios *(retiré :
  Post-apocalyptique, ne valait que pour Fallout parmi 4 franchises citées ; retiré `Xbox`
  plateforme, remplacé par `Xbox Game Studios` éditeur — l'article parle de structure éditoriale,
  pas de sortie ; paire Obsidian/Xbox Game Studios actée)*
- **BYD/DENZA/YANGWANG, Goodwood** : BYD · DENZA · YANGWANG · Voiture · Voiture électrique ·
  Voiture hybride · Goodwood Festival of Speed
- **The Crew Motorfest sur Switch 2** : The Crew · Ubisoft · Ivory Tower · Course · Nintendo
  Switch · PlayStation · Xbox · PC · Multijoueur · En ligne · Compétitif

Nouveaux tags créés : `Sam Neill`, `ASUS`, `Agefield High: Rock the School`, `Refugium Games`,
`Sony`, `Michael McGrath`, `Tekken`, `Hamster Corporation`, `Brant Fitzgerald`, `Manga`, `Naruto`,
`Tempest Rising`, `Pokémon GO`, `Niantic`, `AR`, `Hope`, `Festival de Cannes`, `Godzilla`, `TOHO`,
`CinemaCon`, `Dragon Ball`, `Dimps`, `Transport Fever`, `Urban Games`, `Paradox Interactive`,
`Twisted Tower`, `Atmos Games`, `3D Realms`, `Avowed`, `The Outer Worlds`, `Grounded`,
`Josh Sawyer`, `YANGWANG`, `Voiture électrique`, `Goodwood Festival of Speed`, `The Crew`,
`Ivory Tower`.
Amendements → v3.17 (détail complet dans le Changelog du doc de nomenclature) : trait stable
réservé à l'œuvre-sujet (pas à une personne qui l'a traversée) ; sous-titre à retirer seulement
pour les franchises multi-épisodes ; mécaniques jamais déduites même d'une franchise réputée ;
thème/univers déduit ne vaut que pour la franchise concernée, pas tout un article multi-franchises
; distinction éditeur first-party (Xbox Game Studios) vs plateforme (Xbox) quand l'article parle
de structure actionnariale ; `Alien` confirmé comme ombrelle cross-media unique (pas de tag
séparé pour ses spin-offs) ; `Manga` et `CinemaCon` ajoutés au vocabulaire fermé ; Pokémon —
studio dev à choisir selon le produit précis (Niantic/Game Freak), jamais en bloc.
Ce lot a servi de seconde session de calibration intensive (après le lot #10) — l'utilisateur a
re-challengé quasiment chaque tag posé, révélant plusieurs erreurs de raisonnement plus subtiles
que de simples oublis (confusion éditeur/plateforme, sur-extension du trait stable aux mécaniques
et aux personnes-sujets, tag redondant avec une ombrelle déjà existante).

---

### Retag rétroactif — Lot #1/7 — 2026-07-30 (19 articles sur 131 déjà tagués)

Premier lot du retagging rétroactif des 131 articles traités avant que la nomenclature
n'atteigne sa forme actuelle (v3.19). Appliqué via `apply_batch.py --replace` après
`--dry-run` de vérification. Détail par article :

- **114254** Disney+ sans 4K : + `Disney` (acteur central du litige, distinct de la plateforme).
- **114278** Dragon Age Remaster impossible : inchangé, déjà conforme.
- **114268** Crazy Taxi test multijoueur : + `Compétitif` (modes explicitement décrits « en
  compétition » / « opposera deux équipes »).
- **114273** Jeux PS Plus d'août : + `Dying Light`, `Big Walk`, `Signalis` (nouveaux tags) —
  exception liste ≤5 concrètement disponible ; pas de genre/thème ajouté (plusieurs jeux
  différents, même logique que la restriction Obsidian/Fallout/Avowed en v3.18).
- **114263** Below (Netflix) : inchangé, déjà conforme.
- **114249** BioEden : inchangé, déjà conforme.
- **114243** Cinémas de Sierre #31 : + `Spider-Man`, `Super-héros`, `Action` — règle programme
  mono-film (seul film substantiellement développé dans le texte).
- **114238** Intel Core 2 Duo 20 ans : + `Matériel PC` (composant interne oublié), + `Rétro`
  (rétrospective matérielle, extension de la règle actée pendant cette revue).
- **114228** ARENA Cinemas : + `Spider-Man`, `Marvel` (nommé explicitement), `Super-héros`,
  `Action` — highlight éditorial distinct du reste de la grille horaire (non retaguée).
- **110764** ZeroSpace : + `Compétitif` (1v1/2v2 explicites), + `En ligne` (MMO persistant).
- **105614** STALKER 2 Cost of Hope : inchangé, déjà conforme.
- **114206** Suika Game sur PS5/PC : inchangé, déjà conforme.
- **114201** Hard Worker : + `En ligne` (MMO explicite).
- **114196** Dan Houser jeux physiques : + `Absurd Ventures` (nouveau tag, son nouveau studio,
  explicitement nommé) ; `Take-Two Interactive` **non** ajouté malgré la paire systématique
  Rockstar Games — portée clarifiée (v3.19) : la paire ne s'applique que si le studio est tagué
  comme éditeur d'une œuvre précise, pas via la règle personne + œuvre-signature.
- **114138** SDCC Jour 2 : inchangé — long roundup de 8+ franchises différentes, sous le seuil
  de l'exception liste (≤5), pas de tag individuel par franchise annoncée.
- **113979** Denshattack! (test) : + `Course` (texte explicite : « mélange course, plateforme et
  freestyle »).
- **114180** Carnet noir Chuck Russell : + `Eraser` (nouveau tag, même niveau de traitement
  textuel que Le Roi Scorpion déjà tagué) ; `Witchboard` écarté (mention anecdotique, « un des
  plusieurs projets »).
- **114163** Sega Rally Model 2 : inchangé — `Compétitif` envisagé mais écarté, le texte ne
  décrit que du « jeu en réseau » sans langage compétitif explicite (contraste volontaire avec
  114268/110764 où la compétition est explicitement nommée).
- **111470** Cinémas de Sierre #24 (Toy Story 5) : + `Animation` (film sans acteurs réels),
  + `Pixar` (studio non-ambigu) ; **– `Programme`** retiré (tag hors vocabulaire documenté,
  jugé non pertinent).

5 nouveaux tags créés : `Dying Light`, `Big Walk`, `Signalis`, `Absurd Ventures`, `Eraser`.
3 clarifications de règle actées pendant cette revue, documentées en v3.19 du changelog
(plateformes jamais versionnées, portée des paires studio/éditeur, `Rétro` étendu au matériel).

---

### Retag rétroactif — Lot #2/7 — 2026-07-30 (19 articles sur 131 déjà tagués)

Corrections apportées : **113972** Halo Campaign Evolved (+ `Halo Studios`, développeur
actuel non cité mais franchise non-ambiguë) ; **107654** Clayface (+ `Batman`, franchise
explicitement nommée). Deux propositions rejetées à la relecture, qui ont affiné la
nomenclature (v3.20) : **114117** Scrooge — `Horreur` proposé à tort (le texte le
mentionne seulement comme nuance de ton "à la frontière de", le film reste une comédie
d'après le reste de l'article) ; **107631** Coyote vs. Acme — `Suisse` proposé à tort
(l'absence de date CH n'est qu'un détail isolé dans un article centré sur la
bande-annonce, pas un axe substantiel). Une proposition initialement discutée puis
tranchée en sens inverse : **114107** Xbox cloud gaming gratuit — `Xbox Game Pass`
maintenu malgré l'absence d'abonnement requis pour cette offre précise, la
fonctionnalité restant techniquement rattachée au service. Aucun nouveau tag créé ce
lot-ci. 12 articles inchangés (déjà conformes).

---

### Retag rétroactif — Lot #3/7 — 2026-07-30 (19 articles sur 131 déjà tagués)

Lot le plus propre jusqu'ici : 17 articles déjà conformes, 2 corrections seulement.
**113708** Samsung Galaxy Watch9/Ultra2 : + `IA` (le texte dit explicitement que
l'IA "joue un rôle central", contrairement au Fold 8/Flip 8 du même lot où l'IA n'est
qu'une ligne de specs parmi d'autres — pas ajoutée là). **113854** NVIDIA DLSS 5 : +
`SIGGRAPH` — nouveau tag créé, événement tech absent du vocabulaire fermé jusqu'ici
(v3.21). Suisse confirmé correctement absent sur les deux articles Samsung (CHF/date
routiniers) et correctement présent sur DENZA (vraie implantation marché suisse) —
aucune correction nécessaire, la règle resserrée en lot #2 tient bon.

---

### Retag rétroactif — Lot #4/7 — 2026-07-30 (30 articles sur 131 déjà tagués)

Premier lot à 30 articles (contre 19 précédemment) — qualité tenue, 26 articles déjà
conformes, 4 corrections. **113785** Cinémas de Sierre #30 : + `Vaiana` (nouveau tag,
règle programme mono-film). **113679** Bethesda roadmap : + `Xbox Game Studios` (paire
Obsidian Entertainment déclenchée, développeur d'un projet réel, pas biographique).
**107405** Hela: of Mice & Magic : + `Multijoueur` (Coopératif posé sans son
accompagnement obligatoire). **113588** The Duskbloods : + `Compétitif` (PvPvE
explicite). Deux décisions de fond actées (v3.22, voir changelog) : `Bethesda Game
Studios` ajouté aux paires systématiques → `Xbox Game Studios` ; pas de paire
`The Pokémon Company`/`Pokémon` (tranché définitivement, aucun angle de reco distinct).
Une vraie erreur trouvée et corrigée : **113637** Dreame T16 Pro Heat était tagué
`Aspirateur robot` alors qu'il s'agit d'un aspirateur-laveur manuel (pas de navigation
autonome) — nouveau tag `Électroménager` créé pour ce type d'appareil, `Aspirateur
robot` retiré et désormais réservé aux appareils réellement autonomes.

---

### Correctif ponctuel — 2026-07-30

**113854** NVIDIA DLSS 5 (lot #3) : `Matériel PC` manquant malgré `Carte graphique`
posé — oubli repéré par relecture humaine après coup, corrigé. A motivé l'ajout de
`validate_pairings()` dans `apply_batch.py` (voir `tests/test_pairings.py`) : cette
règle de paire est désormais vérifiée automatiquement et bloque tout lot qui l'omet,
plutôt que de dépendre d'une relecture attentive à chaque fois.

---

### Retag rétroactif — Lot #5/5 — 2026-07-30 (44 articles sur 131 déjà tagués)

**Dernier lot du retag rétroactif — les 131 articles sont maintenant à jour avec la
nomenclature actuelle (v3.23).** 41 articles déjà conformes, 2 corrections, 1 refus
justifié après discussion. **113441** Agent 64: Spies Never Die : `Compétitif`
initialement proposé (deathmatch local explicite) puis **retiré** après challenge —
mode secondaire greffé sur une campagne solo/coop, pas une compétition structurante.
A motivé une clarification durable de la règle (v3.23, voir changelog) : `Compétitif`
réservé aux genres compétitifs par nature ou aux vrais modes dédiés avec classement
réel, pas à tout ce qui est techniquement jouable à plusieurs contre. **113225**
Fallout/Obsidian : `Bethesda Game Studios` retiré (n'apparaissait que dans une
comparaison historique, le studio n'est pas impliqué dans le nouveau projet).
**113535** Samsung Flex Titanium : `Écran` retiré, `Smartphone` suffit — les tags
composants (§4) sont scopés à l'écosystème PC/console, pas aux specs intégrées
d'autres appareils.

**Bilan des 5 lots de retag (131 articles)** : 5 nouveaux tags créés (`Dying Light`,
`Big Walk`, `Signalis`, `Absurd Ventures`, `Eraser`, `Vaiana`, `Électroménager`,
`SIGGRAPH` — 8 au total en comptant tous les lots), plusieurs clarifications de règles
actées (v3.19 à v3.23 : plateformes non-versionnées, portée des paires studio/éditeur,
Rétro matériel, genre-vs-ton, service en accès gratuit, seuil anomalie Suisse, paire
Bethesda/Xbox Game Studios, Pokémon Company écarté, Électroménager, Compétitif
resserré, composants scopés PC/console), et un garde-fou automatique ajouté au
pipeline (`validate_pairings()`) suite à un oubli réel (Matériel PC manquant).

---

## Reprise du catalogue principal (post-retag)

### Lot #1 — 2026-07-30 (30 articles, premier lot via curseur de reprise)

Premier lot d'articles jamais tagués depuis la fin du retag rétroactif, récupéré via
`fetch_batch.py --size 30` (mode curseur, sans `--ids`). Contenu très varié (jeux,
films, séries, tech, une interview locale) — voir le résumé complet dans la
conversation pour le détail par article. Points marquants :

- **Trois décisions de fond actées pendant la revue** (v3.24, voir changelog) :
  `Périphérique de Simulation` ajouté (§4, coexiste avec `Périphérique` comme les
  autres composants précis) ; `Indé` rendu éligible à la recherche ciblée d'identité
  (statut d'un studio = fait stable) ; `Sony Interactive Entertainment` retiré au
  profit de `Sony` seul (correction rétroactive appliquée à l'article Ratchet & Clank:
  Ranger Rumble du lot #4 du retag).
- **`Extraction shooter` ajouté au vocabulaire fermé des genres**, nommé explicitement
  dans le texte d'un article (Rules of Engagement: The Grey State).
- Plusieurs corrections issues d'un challenge direct : `Indé` ajouté sur Orbitals
  (aucun gros éditeur cité, profil clairement indépendant) ; `Shoot'em up` ajouté sur
  Cobra Strike (texte explicite "tir arcade") ; `En ligne` ajouté sur Honkai: Star Rail
  (structure live-service à bannières datées = connexion permanente par nature, même
  sans le mot explicite).
- ~30 nouveaux tags créés (studios, licences, personnes — voir l'historique WordPress
  pour la liste complète).

---

### Lot #2 — 2026-07-31 (30 articles, catalogue principal)

Contenu très varié (jeux, films, séries, tech, deux interviews locales). Deux décisions
actées pendant la revue (v3.25, voir changelog) : `Bethesda Game Studios` renommé
`Bethesda` (tag WordPress renommé directement, id conservé) ; `Game Conscient` ajouté
aux Rubriques éditoriales. Corrections issues du challenge : `Gestion` au lieu de
`Simulation` sur Cat Mail Co. (pas de simulation réaliste, juste un loop cosy de tri de
courrier) ; `FPS` confirmé et ajouté sur Nivalis Nights (le texte le dit explicitement,
la vidéo — invisible pour moi — montre des éléments de tir absents du texte seul).

**Incident technique** : le lot a crashé à mi-parcours sur une tentative de création du
tag `Atlus` — `term_exists`, le tag vivait déjà sous la forme `ATLUS` (toutes
majuscules, même convention que `SEGA`), invisible dans mon diff parce que la
correspondance est sensible à la casse. Repris proprement grâce à la sauvegarde
incrémentale (24 articles déjà écrits n'ont pas été retouchés) ; les 6 restants
appliqués avec `ATLUS` correctement réutilisé. À garder en tête : les marques
japonaises courtes semblent parfois taguées tout en majuscules par convention
historique du site (SEGA, ATLUS) — vérifier avant de proposer une casse "standard".

---

### Lot #3 — 2026-07-31 (40 articles, catalogue principal — premier lot à 40)

Premier lot testé à 40 articles (après 20→30→30). Contenu très varié : plusieurs
articles GTA 6 (carte fan-made, leak, prix, disque, pénurie de consoles), une bonne
part cinéma/animation (Werwulf, Shrek, DC/Warner Bros., Ghostbusters, ONE PIECE, Blair
Witch, Evil Dead Burn, Le Bus Magique, Stuart Fails to Save the Universe), et plusieurs
jeux indés/niches (CAPTCHA Hell, Paralives, Monster Fantasy, ExeKiller). Qualité tenue
sur les 40 malgré le volume.

Trois décisions actées pendant la revue (v3.26, voir changelog) :
- `Chaise gaming` ajouté au vocabulaire fermé (§4), rejoint la famille `Périphérique`
  (Razer Soma Chroma — aucun tag composant existant ne couvrait le mobilier gaming).
- `Festival d'Annecy` et `THQ Nordic Digital Showcase` ajoutés aux événements fermés
  (§6) — le premier apparu deux fois dans le lot (DC/Warner Bros., Ghostbusters:
  Night Shift), le second désigné par l'article lui-même comme rendez-vous annuel.
- Confirmations sans changement de règle : `Star Wars Eclipse` ne reçoit pas de tag
  séparé de `Star Wars` (même logique que `Alien`/`Alien: Earth`, v3.17) ; `Warner
  Bros. Animation` écarté au profit de `Warner Bros.` seul (répétition inutile,
  contrairement à `PlayStation Studios`/`Sony Santa Monica` qui restent des identités
  créatives distinctes) ; `Sport` (§3) reste un genre d'œuvre et ne s'étend pas à un
  produit réel adjacent à un événement sportif (ballon connecté Adidas Trionda).

**Piège technique découvert** : certains tags WordPress contenant une esperluette sont
stockés HTML-encodés (`Point &amp; click`, `Ratchet &amp; Clank`, `Hela: of Mice &amp;
Magic`, `Deer &amp; Boy`) — une proposition avec `&` littéral ("Point & click") est
rejetée par la validation d'existence car elle ne matche pas la forme stockée. Vérifier
systématiquement `tags_existants` pour toute proposition contenant "&" avant de
l'écrire en clair.

40 nouveaux tags créés (licences, studios, personnes, événements — voir l'historique
WordPress pour le détail).

---

### Audit du registre des tags — 2026-07-31 (704 → 698 tags)

Premier contrôle qualité de l'ensemble des tags déjà posés (pas un lot d'articles). Généré
un registre complet (id/nom/compteur d'usage) et détecté les quasi-doublons par
normalisation casse/accent — zéro collision réelle restante (les deux incidents de casse
de la session, `ATLUS` et `Ugreen`, avaient déjà été résolus au moment de l'écriture).
Six fusions/suppressions actées (v3.28, voir changelog) :

- **`Battlefield Studios` → `Battlefield`** (article 112664) : jamais utilisé sans
  `Battlefield`, aucune réutilisation cross-franchise contrairement à `Take-Two
  Interactive`.
- **`Cross-play` retiré du vocabulaire** (articles 114268, 113972) : toujours posé aux
  côtés de `En ligne` + `Multijoueur`, n'a jamais porté de distinction propre.
- **`Maritime` retiré du vocabulaire** (article 114263, *Below*) : 1 seul usage.
- **`Sony Pictures Television` → `Sony Pictures`** (article 113645, *God of War* TV) :
  `Sony` (gaming/matériel/corporate) reste distinct de `Sony Pictures` (cinéma, 0
  recoupement d'audience réel sur 6+4 usages vérifiés), mais la distinction
  cinéma/télévision au sein du studio Sony Pictures n'ouvre aucun angle propre.
  `Sony Interactive Entertainment` (0 usage, déprécié depuis v3.24) supprimé pour de bon.
- **`Toy Story 5` renommé `Toy Story`** (article 111470) : rattrapage de la règle "pas de
  numéro" (§1), manquée à la création.
- **`UGREEN NASync` → `Ugreen`** (article 110899) : même situation que Battlefield
  Studios, jamais utilisé sans `Ugreen`.
- **`Guerre`/`WW1`/`WW2`/`Guerre froide` rendus mutuellement exclusifs** — `Guerre`
  retiré de 3 articles qui portaient déjà le conflit précis : 111120 (*A Lost Man*, garde
  `WW1`), 100310 (*The Defiant*, garde `WW2`), 97804 (*Hell Let Loose: Vietnam*, garde
  `Guerre froide`). `Guerre` reste réservé aux contextes de guerre non rattachés à l'un
  des trois conflits historiques précis.

**Résolu depuis** : `Pokémon GO` → `Pokémon` a été complété (article 113119 : `Pokémon` +
`Mobile` + `Niantic`, sans `AR` associé à `Périphérique`) — voir la réconciliation
ci-dessous, qui documente aussi la précision apportée à la paire `AR`/`Périphérique`
(matériel uniquement, jamais une fonctionnalité logicielle de même nom).

---

### Réconciliation de la nomenclature — 2026-08-05 (v3.29 → v3.31)

`Narratif` et le triptyque `Réflexion`/`Stratégie`/`Gestion`, identifiés comme
sous-définis lors du lot #9, ont été retravaillés en profondeur (§3 entièrement réécrit
avec une définition opérationnelle par genre + piège lexical ⚠️, arbre de décision
Réflexion/Stratégie/Gestion). En parallèle, §5 a été renforcé pour rendre la déduction
des univers de licences connues explicite et attendue, avec un contrôle non bloquant en
fin de lot (`apply_batch.py` signale désormais les articles sur une œuvre sans thème
§5). Voir changelog v3.29/v3.30 pour le détail complet — c'est le morceau de travail le
plus substantiel de la nomenclature depuis l'audit initial de la Grille (v3.11).

Ce travail ayant été mené dans une session séparée repartie d'une version du dépôt
antérieure à l'audit du registre de tags de ce même jour, la sauvegarde a fait
collision avec les décisions déjà actées et déjà appliquées sur WordPress (numéros de
version dupliqués, `Cross-play` resté dans le texte des règles malgré un changelog
affirmant le contraire, `Maritime`/restriction œuvre-signature/`EVO`/`Amazon Prime Day`
disparus des documents). Réconciliation complète en v3.31 (changelog) : le travail
génuinement nouveau est conservé, les décisions déjà actées sont restaurées, et deux
conflits réels ont été tranchés plutôt que fusionnés à l'aveugle :
- `Guerre`/`WW1`/`WW2`/`Guerre froide` restent mutuellement exclusifs (v3.28) — l'exemple
  `Battlefield` → `Guerre` proposé dans le travail parallèle aurait réintroduit
  exactement la redondance corrigée par cette règle.
- `Tactique` reste retiré, mais pour un motif vérifié plutôt que supposé : sur les 7
  articles réels qui le portaient, seuls 2 relevaient du genre stratégie/tactique
  (`Stratégie` + `RPG`), les 5 autres l'utilisant comme qualificatif de FPS/TPS
  "tactique" sans rapport avec le genre. Nettoyage rétroactif de ces 7 articles effectué
  dans la foulée :
  - **113049** Terrinoth: Heroes of Descent : `Tactique` → `Stratégie` (garde `RPG`
    déjà présent, complète la paire). Au passage, `Multijoueur` ajouté — `Coopératif`
    était posé seul depuis l'origine, gap antérieur repéré par le contrôle mécanique
    Grille #7 en relisant l'article pour cette correction.
  - **80487** Star Wars Zero Company : `Tactique` retiré, `Stratégie` déjà présent
    suffit (pas de progression de personnage, ce n'est pas un RPG).
  - **111292** Final Fantasy VII Revelation, **111255** Crossfire, **111068** Pokémon
    Champions, **97804** Hell Let Loose: Vietnam, **110844** DIOXIDE : `Tactique`
    simplement retiré, déjà pleinement couverts par leurs autres tags (`Action-RPG`,
    `TPS`+`Infiltration`, `Compétitif`+`Multijoueur`, `FPS`+`Simulation`,
    `FPS`+`Souls-like` respectivement).
  Tag `Tactique` supprimé de WordPress après vérification à 0 usage.

---

### Lot #10 — 2026-08-12 (10 articles, catalogue principal — premier lot sous la nomenclature réconciliée)

Premier lot d'articles réellement nouveaux depuis la réconciliation v3.29-v3.31. Objectif
explicite : vérifier que les nouvelles définitions §3/§5 tiennent sur du contenu réel,
pas seulement sur les cas déjà connus de l'audit. Deux règles neuves ont été directement
exercées :
- **101905 Hellraiser: Revival** : le texte dit « survival horror », mais aucune mécanique
  de faim/froid/récolte n'est décrite — piège lexical ⚠️ exactement documenté dans la
  nouvelle définition de `Survie` (§3). Pas de `Survie` posé ; `Action` retenu à la place
  (« action brutale » explicite dans le texte).
- **111937 Billie, à la croisée des mondes** et **96760 Astérix et le Royaume de Nubie** :
  `Aventure` posé sans que le mot ne déclare un genre explicitement, sur la base de la
  définition (récit structuré comme un voyage/quête) — test de la règle « un genre non
  nommé se tague quand le texte décrit ce que sa définition exige » (§3, v3.29).
- **76464 Shrek 5** : `Comédie` déduit comme trait stable de la licence (aucune
  déclaration explicite dans ce texte court), cohérent avec le tag déjà posé sur le
  précédent article Shrek du lot #8 — `Fantasy` volontairement écarté par cohérence avec
  ce même précédent (le fairy-tale de Shrek fonctionne comme décor parodique, pas comme
  univers définissant au sens de l'admission §5).
- **111880 Don't Nod** : article sur les finances du studio, aucun jeu précis n'étant le
  sujet — pas de genre posé, `Life is Strange`/`Lost Records`/`Aphelion` mentionnés en
  contexte seulement, non développés individuellement.
- **111904 Kiki la petite sorcière** : `Studio Ghibli` et `Hayao Miyazaki` volontairement
  écartés — pedigree historique (film de 1989), sans rapport avec cette nouvelle
  production live-action BBC Studios/Wheel in Motion/Kadokawa.

Une décision de vocabulaire actée pendant la revue (v3.32, voir changelog) :
`Pixel Arcadia` ajouté aux événements fermés (§6) malgré l'absence de récurrence prouvée
(première édition annoncée) — accepté au fil de l'eau, même philosophie que `SIGGRAPH`
en v3.21.

10 nouveaux tags créés (licences, studios — voir l'historique WordPress pour le détail).

---

### Lot #11 — 2026-08-12 (40 articles, premier lot en mode `--from-top`)

Premier lot depuis le basculement du mode curseur (backlog profond) vers `--from-top` :
au lieu de continuer à remonter lentement depuis le fond du catalogue, on rattrape
maintenant les publications les plus récentes. Deux décisions de vocabulaire actées
pendant la revue (v3.33, voir changelog) : `D23` et `TwitchCon` ajoutés aux événements
fermés (§6) — contrairement à `Pixel Arcadia` (lot #10), ce sont deux conventions déjà
bien établies, pas des paris sur une récurrence future.

Points notables :
- **114826 Lord of the Rings: War in the North** et **114395 Truxton Extreme** :
  créateurs historiques (Snowblind Studios, Toaplan) écartés au profit des studios dev
  actuels (Aspyr, Tatsujin) — application directe de la règle actée lors de l'audit
  (§2, précédent Halo/Piranha Bytes).
  - **74457 Over the Hill** et **114728 Cinémas de Sierre #33** (The End of Oak Street) :
  studio dev laissé en incertitude plutôt que deviné — le texte relie seulement
  indirectement au studio (comparaison à Art of Rally) ou ne le cite pas du tout.
- **105622 Serious Sam: Shatterverse** : le texte source nomme deux studios différents
  de façon contradictoire (Croteam en intro informelle, Behaviour Interactive en
  annonce formelle) — les deux ont été reflétés plutôt que tranchés unilatéralement.
- **113352 Interview Lenchanteur** : plusieurs tags qu'on aurait pu croire déjà
  existants (`Kirby`, `Polymanga`) n'avaient en réalité jamais été créés sur WordPress —
  même situation que `Médiéval`/`Point & click` précédemment.

39 nouveaux tags créés (licences, studios, personnes — voir l'historique WordPress).

---

### Lot #12 — 2026-08-12 (40 articles, mode `--from-top`)

Une décision de vocabulaire actée pendant la revue (v3.34, voir changelog) :
`Virtual Boy` ajouté aux plateformes fermées (§4) — console historique Nintendo,
motivé par un article sur deux prototypes annulés (Zero Racers, D-Hopper)
redécouverts, absent jusqu'ici du vocabulaire alors que `Neo Geo` y figurait déjà.

Points notables :
- **111811 Cinémas de Sierre #25 (Toy Story 5)** : `Disney` + `Pixar` ajoutés par
  recherche ciblée bien qu'absents du texte — franchise à l'ambiguïté nulle (§2).
- **114405 Parc Dragon Ball en France** : `France` tagué comme acteur central réel
  (négociations gouvernementales, préfet d'Île-de-France impliqué), pas une mention
  incidente.
- **111790 Royaume-Uni interdit les réseaux sociaux <16 ans** : cas texte-book de la
  règle §8 (un pays légifère) — `Royaume-Uni` créé.
- **111863 Fermetures de studios Xbox** : `Double Fine`/`Ninja Theory` tagués malgré
  n'être que cités en exemple — chacun est individuellement nommé comme étant dans la
  même situation de risque, pas juste listés en passant.

37 nouveaux tags créés (licences, studios, personnes, marques — voir l'historique
WordPress).

---

### Lot #13 — 2026-08-19 (10 articles, mode `--from-top`, reprise après une semaine)

Premier lot de la reprise du chantier après une pause d'une semaine (dernier lot :
#12, 2026-08-12). Contenu varié : jeux indés (Fantasy Online 2, Riot Riders, Kumarn:
The Wandering Spirit, Future Knight), un produit dérivé (LEGO Batmobile), une actu
GTA 6, un roundup Xbox Game Pass, une actu cinéma (Fast Forever) et une programmation
ARENA Cinemas.

Points notables :
- **115235 LEGO Batmobile (Batman Returns)** : `DC` + `Warner Bros.` ajoutés par
  recherche ciblée bien qu'absents du texte — même logique que Toy Story/Disney+Pixar
  (lot #12) : franchise à l'ambiguïté nulle, marque-source d'une licence tagée sur un
  produit dérivé (§2 "produit dérivé"), pas juste le fabricant (`LEGO`). Repéré après
  coup par l'utilisateur — la règle existait déjà, simple oubli d'application au
  moment de la rédaction du lot.
- **115261 Kumarn: The Wandering Spirit** : `WereBuff Studio` (dev) et `Indé`
  complétés par recherche ciblée externe (§2) — titre non-ambigu, source unique
  (communiqués Wired Productions/Gamescom 2026).
- **115256 Riot Riders** : `Guerre froide` posé — conflit précis explicitement le
  cadre narratif du jeu (pas une franchise, donc pas concerné par l'exclusion de
  déduction en bloc).
- **115266 Fantasy Online 2** : titre consolidé en `Fantasy Online` (retrait du
  numéro, règle §1) ; thème Fantasy volontairement écarté malgré le nom — aucun
  élément fantastique décrit dans le texte, signalé en incertitude plutôt que déduit
  du seul nom du jeu.
- **115179 ARENA Cinemas (Jason Statham/Mutiny)** : `Mutiny` + `Jason Statham`
  tagués — film mis en avant dans le titre du programme, distinct du reste de la
  grille horaire (même règle que le précédent Spider-Man des lots #2/#8).

16 nouveaux tags créés : `Fantasy Online`, `Pixel Games LLC`, `Jeromy Stroh`,
`Riot Riders`, `Bombed School`, `Kumarn: The Wandering Spirit`, `WereBuff Studio`,
`Fast & Furious`, `Vin Diesel`, `Bodycam`, `Reissad Studio`, `Mutiny`,
`Jason Statham`, `Future Knight`, `Studio Koba`, `Aeternum Game Studios`.

---

### Lot #14 — 2026-08-19 (10 articles, mode `--from-top`)

Contenu varié : tech (YouTube), sport (EA Sports FC 27), série (It: Welcome to
Derry), FPS (Battlefield 6), hardware (PlayStation 6), un visual novel suisse, une
franchise ciné (Pirates des Caraïbes), un programme de cinéma local, un plateformer
indé (Panic 64), un Carnet noir (Hayden Panettiere).

Points notables :
- **115136 It: Welcome to Derry** : consolidé sur l'ombrelle `It` (pas
  `It: Welcome to Derry`) — même logique que `Alien`/`Alien: Earth`, signalé par
  l'utilisateur après relecture, corrigé avant écriture.
- **115101 Cinémas de Sierre n°34** : cas limite non couvert explicitement par la
  règle "programme mono-film" — 3 films (`L'Odyssée`, `Spider-Man`, `La fin d'Oak
  Street`) substantiellement synopsés dans le même programme, tagués individuellement
  par extension de l'exception liste ≤5, plutôt qu'un seul film vedette. Validé par
  l'utilisateur, à garder en tête comme précédent pour les prochains programmes
  multi-films développés.
- **115083 Carnet noir Hayden Panettiere** : 6 œuvres tagées parmi celles
  substantiellement développées dans le texte (Heroes, Scream, Nashville, Remember
  the Titans, Until Dawn, Kingdom Hearts) ; Ice Princess et Bring It On: All or
  Nothing écartés — mentions trop anecdotiques (simple liste sans développement).
- **115120 Das Hexencafé am Zürichsee** : `Fantasy` + `Fantastique` posés ensemble —
  le texte cite littéralement "fantasy" tout en décrivant un surnaturel qui surgit
  dans un cadre suisse réaliste (Zurich), satisfaisant les deux définitions
  distinctement.

18 nouveaux tags créés : `YouTube`, `It`, `Hiroki Totoki`, `Das Hexencafé am
Zürichsee: Der letzte Eintrag`, `Micjam Games`, `Pirates des Caraïbes`,
`Johnny Depp`, `Margot Robbie`, `Jerry Bruckheimer`, `La fin d'Oak Street`,
`Panic 64`, `Spicy Gyro Games`, `Hayden Panettiere`, `Heroes`, `Scream`,
`Nashville`, `Remember the Titans`, `Kingdom Hearts`.

---

### Lot #15 — 2026-08-19 (10 articles, mode `--from-top`)

Contenu varié : hardware (ASUS Raikiri 2 Pro, Keychron K5 Max), un fan-portage
rétrogaming (Ridge Racer Collection), deux articles Kingdom Hearts 4 (le sien +
mentionné dans le récap D23), un récap D23 Disney à 14 annonces, une mise à jour
STALKER 2, un VR remake (System Shock), un RPG cyberpunk indé (Neo Berlin 2087), une
compilation Mafia et un film d'horreur (Beware Boiúna).

Points notables :
- **115023 D23 récap Disney** : roundup de 14 annonces distinctes (Marvel, Star
  Wars, Pixar, Disney Animation) — seules les grandes marques organisatrices et
  `Kingdom Hearts` (sous-section développée en détail, cœur éditorial JVMag) sont
  taguées individuellement ; les ~13 autres titres écartés, règle "listes = pas de
  tags" (même logique que le précédent SDCC/Tencent-Gamescom).
- **114980 Neo Berlin 2087** : studio dev (`Elysium Game Studio`) et éditeur
  (`ByteRockers' Games`) absents du texte, complétés par recherche ciblée externe
  (§2) — titre non-ambigu, sources concordantes.
- **115062 Ridge Racer Collection** : le texte orthographie "Wanzai" mais le tag
  existant `Wanszai` (même développeur que le portage Sega Rally, lot #4) a été
  réutilisé plutôt que d'en créer un doublon.
- **Correction avant écriture** (signalée par l'utilisateur) : `PC` manquait sur
  Keychron K5 Max alors que le texte dit explicitement "Compatible PC et MAC" —
  même logique de plateforme-périphérique que le précédent Glorious GHS Wireless
  (lot #8), appliquée de façon incohérente entre les deux articles hardware de ce
  lot avant relecture.
- **Erreur technique interceptée par le dry-run** : `Mafia` et `Hangar 13` avaient
  été classés à tort dans `tags` au lieu de `nouveaux_tags` (n'existaient pas encore
  sur WordPress) — bloqué par le garde-fou anti-doublon d'`apply_batch.py`, corrigé
  avant écriture réelle.

13 nouveaux tags créés : `Rave Racer`, `Nintendo Direct`, `Keychron`,
`System Shock`, `Flat2VR Studios`, `Nightdive Studios`, `Neo Berlin 2087`,
`Elysium Game Studio`, `Mafia`, `Hangar 13`, `Beware Boiúna`, `Mike P. Nelson`,
`Brésil`.

---

### Amendement — sous-titres de titres de jeu (2026-08-19, v3.35)

Demande de l'utilisateur en cours de lot #16 : retirer systématiquement le
sous-titre des titres au format « Nom : Sous-titre », même pour une œuvre unique et
autonome (auparavant réservé à la consolidation de franchises multi-épisodes,
v3.17). Motif : longueur des tags, et impossible de savoir au moment du tagging si
une œuvre restera isolée ou deviendra une série. Garde-fou ajouté : si le nom de
base seul est trop générique pour identifier l'œuvre sans ambiguïté, le sous-titre
complet est gardé et le cas signalé en `incertitudes`. Détail complet et
raisonnement → changelog v3.35.

**Rétroactif appliqué** : les deux tags créés dans cette même session sous
l'ancienne règle ont été renommés directement sur WordPress (id conservé, aucun
article à retoucher) : `Kumarn: The Wandering Spirit` → `Kumarn` (id 3566,
article 115261) et `Das Hexencafé am Zürichsee: Der letzte Eintrag` → `Das
Hexencafé am Zürichsee` (id 3580, article 115120).

---

### Lot #16 — 2026-08-19 (10 articles, mode `--from-top`)

Contenu varié : deux nouveaux jeux (Nautus: Echoes from Below, Waste The Fallen),
American Horror Story: 13, l'annonce Twitch/IA, les jeux PS Plus d'août, deux tests
hardware (Logitech Mobi Fold, à côté des Pixel Watch 5/Pixel 11 de Google),
Hordeguard: Winds of the North et Formula E sur Disney+. Premier lot appliqué sous
la nouvelle règle de sous-titres (v3.35) : `Nautus: Echoes from Below` → `Nautus`
et `Hordeguard: Winds of the North` → `Hordeguard` dès la proposition initiale.

Points notables :
- **114906 Formula E** : `Formula E` créé comme tag d'identité ouvert (championnat
  récurrent, pas une convention ponctuelle du vocabulaire fermé §6) ; `Voiture` +
  `Voiture électrique` posés — la voiture GEN4 100% électrique est décrite en détail
  dans le texte, pas une mention incidente.
- **114945 Twitch/IA** : `Amazon` créé distinct de `Amazon Games Studios`/`Amazon
  MGM Studios` déjà existants — même logique que Sony/Sony Pictures.
- **114950 American Horror Story: 13** : Jessica Lange et Evan Peters tagués (leurs
  retours de personnages sont littéralement le sujet de la news), le reste du
  "casting XXL" écarté comme liste anecdotique ; plateforme régionale non confirmée
  (Disney+ probable mais pas annoncé officiellement) → incertitude plutôt que
  déduite.
- **114929 PS Plus jeux d'août** : 10 jeux listés, aucun tagué individuellement
  (au-delà du seuil ≤5, cohérent avec les précédents PS Plus).

13 nouveaux tags créés : `Nautus`, `Magic Design Studios`, `Waste The Fallen`,
`Royal Crow`, `Lovecraftien`, `American Horror Story`, `Jessica Lange`,
`Evan Peters`, `Twitch`, `Amazon`, `Mike Minton`, `Hordeguard`, `Formula E`.

---

### Lot #17 — 2026-08-19 (10 articles, mode `--from-top`)

Dernier lot de la reprise du chantier après une semaine de pause (~50 articles
traités au total sur les lots #13 à #17). Contenu varié : une saison Netflix
(Monster: The Lizzie Borden Story), un crossover comics Star Wars/Marvel, un film
Brad Pitt, une preview Rhythm Paradise Groove, un article logistique Coupe du monde
2026, deux jeux suisses (Horses of Hoofprint Bay, Roulette Dungeon), le "Reset"
interne Xbox, Vaiana (remake) et les jeux PS Plus de juin.

Points notables :
- **114899 Monster: The Lizzie Borden Story** : première application de
  l'exception ajoutée en v3.35 — le nom de base seul (`Monster`) jugé trop
  générique pour identifier l'œuvre sans ambiguïté (collision possible avec
  `Monster Fantasy` déjà existant), sous-titre complet conservé.
- **111684 Coupe du monde 2026** : pas de tag d'identité récurrent créé — jugé
  après discussion comme un article ponctuel (logistique de diffusion), pas un
  sujet appelé à revenir comme `Formula E`. Décision au cas par cas, pas un
  changement de vocabulaire.
- **111644 Horses of Hoofprint Bay** et **111633 Roulette Dungeon** : deux jeux
  suisses annoncés au même showcase Women-Led Games du Summer Game Fest.
- **111677 XBOX Reset** : tagué `Microsoft` + `Xbox` (pas `Xbox Game Studios`) —
  l'article couvre la direction corporate de la division dans son ensemble, pas
  la publication d'un jeu précis par un studio first-party.

17 nouveaux tags créés : `Monster: The Lizzie Borden Story`, `Ella Beatty`,
`Charlie Hunnam`, `Kevin Smith`, `David Marquez`, `Heart Of The Beast`,
`David Ayer`, `Brad Pitt`, `Rhythm Paradise`, `Rythme`, `Horses of Hoofprint Bay`,
`thogli studios`, `The Mane Quest`, `Asha Sharma`, `Dwayne Johnson`,
`Roulette Dungeon`, `Hooded Traveler Games`.

---

## Décisions ouvertes à surveiller
- **Mediawan** : gardé, à réévaluer s'il n'est pas réutilisé.
- **Unitree** : gardé comme le plus connu des fabricants de robots.
- **Montage PC** : rubrique provisoire, on juge à l'usage.
- **Labels ciné vs distributeurs** : labels créatifs reconnaissables tagués (A24, Disney, Pixar…) — à confirmer.
- **Xbox Game Studios / éditeurs first-party** : tagués comme axe « curation » distinct de la plateforme — réversible si bruit.
- **`dungeon crawler`** (article #113049) : casse non conforme, vocabulaire fermé §3 à amender ou
  fondre dans un genre existant — à trancher lors de la discussion documentation.
- **Sujets société-tech hors gaming/divertissement** (ex. lois sur les réseaux sociaux) : idée d'un
  tag dédié évoquée, pas tranchée — ces articles ressortent avec très peu de tags faute de facette
  applicable (voir France <15 ans, lot #7).
- **`AR` conflate matériel et fonctionnalité logicielle** : posé à la fois pour du vrai matériel
  (lunettes ROG XREAL R1, pairing `Périphérique` ajouté v3.27) et pour un mode caméra en réalité
  augmentée dans un jeu mobile (Pokémon GO, article 113119). Le pairing mécanique bloque la fusion
  `Pokémon GO` → `Pokémon` tant que ce n'est pas tranché — à trancher : deux tags distincts
  (`AR` matériel vs un thème `Réalité augmentée` pour la fonctionnalité), ou une exception au
  pairing pour ce cas d'usage.