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