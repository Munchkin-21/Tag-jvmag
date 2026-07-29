# Journal des tags — JVMag

> Ce fichier n'est plus un inventaire de tags. Il a trois rôles :
> 1. **Journal des lots traités** par le pipeline d'automatisation (`scripts/`), avec le détail des
>    tags posés et le raisonnement — c'est ici, et nulle part ailleurs, que vit l'historique complet.
> 2. **Décisions ouvertes à surveiller** — cas tranchés au fil de l'eau qui ne méritaient pas
>    forcément un amendement formel de [nomenclature-tags-jvmag.md](nomenclature-tags-jvmag.md),
>    mais qu'il faut garder en tête pour rester cohérent.
> 3. **Journal des nettoyages** — corrections apportées à des tags hérités d'avant l'automatisation.
>
> Pour savoir **quels tags existent déjà** sur le site : c'est lu en direct via l'API WordPress
> (`scripts/wp_client.py::list_all_tags()`), plus besoin de le recopier ici — `fetch_batch.py`
> embarque ce snapshot dans chaque lot exporté.
> Pour savoir **quelles règles appliquer** (vocabulaire fermé compris) : voir
> [nomenclature-tags-jvmag.md](nomenclature-tags-jvmag.md), seule source de vérité pour les règles
> actives. Ce fichier-ci ne contient que l'historique — les règles n'y sont jamais définies, juste
> référencées.

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

---

## Audit général — 2026-07-29

Premier audit complet du pipeline après 6 lots (41 articles traités). Voir aussi les 3 fixes de
code dans `scripts/` (docstring `list_all_tags`, sauvegarde incrémentale de l'état dans
`apply_batch.py`, message si lot incomplet dans `fetch_batch.py`).

**Réorganisation documentaire** : les listes de vocabulaire fermé (§3 à §6) sont maintenant triées
alphabétiquement dans `nomenclature-tags-jvmag.md` pour rester scannables. La section "Exemples
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

---

## Décisions ouvertes à surveiller
- **Mediawan** : gardé, à réévaluer s'il n'est pas réutilisé.
- **Unitree** : gardé comme le plus connu des fabricants de robots.
- **Montage PC** : rubrique provisoire, on juge à l'usage.
- **Labels ciné vs distributeurs** : labels créatifs reconnaissables tagués (A24, Disney, Pixar…) — à confirmer.
- **Xbox Game Studios / éditeurs first-party** : tagués comme axe « curation » distinct de la plateforme — réversible si bruit.
- **`dungeon crawler`** (article #113049) : casse non conforme, vocabulaire fermé §3 à amender ou
  fondre dans un genre existant — à trancher lors de la discussion documentation.
