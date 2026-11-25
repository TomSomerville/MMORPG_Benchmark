# Art To-Do 2 — Creatures & NPCs

[← Art Master To-Do](00-art-master-todo.md) · Prev: [Characters, Armor & Weapons](01-characters-armor-weapons.md) · Next: [Environments & Props](03-environments-props.md)

Every creature and NPC in levels 1–30, grouped by **rig** (skeleton). A rig is built and animated once; each creature that uses it is a **skin** (texture, sometimes with a mesh variant or scale). ☐ = not started.

**How a creature is made.** A rig's base model is a generated model fitted to the rig's contract, the same way as a player body ([Characters §1](01-characters-armor-weapons.md#1-base-bodies)): a picture of the creature painted in the game's style, an image-to-3D mesh of it, then the fitting step, which keeps the generated mesh, reduces it to the triangle budget, bakes its colour onto its own 1024² texture and skins it to the contract skeleton in the contract's rest pose. The fitting reads the joints by body plan: two-legged figures (which may have a tail and no fingers), four-legged animals, and, more roughly, spiders and floating things. The result is a single mesh with its own baked texture.

**How a skin is made.** Each variety on a fitted rig has its own skin row and its own texture, which is the fitted model's texture tinted for that variety (a darker grey for an old wolf, tan for a jackal, white for a snow cat). A named creature has its own row like any other variety. Mesh variants noted in a row (a mane, an egg sac, a crown) are not part of a tinted skin.

Open: whether the palette lock and the repaint pass apply to fitted creature models and their tinted skins is not decided; they keep their generator's colours today.

**Standard creature animation set (10 clips per rig):** Idle, Idle fidget, Walk, Run, Attack A, Attack B, Hit react, Death, Stunned, Special (named per rig). Casters add Cast and Channel. Extra clips are listed per rig.

## 1. Beasts

| ID | Done | Rig | Extra clips | Skins (creature → texture/mesh variant) | Skins |
|---|---|---|---|---|---|
| CRE-B01 | ☐ | **Canine** | Howl, Pounce, Sit | Vale Wolf Pup (small, grey) · Vale Wolf · Old Greymaw (large, scarred) · Rime Wolf (white) · Harrow Jackal (tan, lean mesh) · Briarwood Stalker (black) · Scarhide (large, scarred) · Ash Jackal (soot) · Dustmaw · Moor Hound (shaggy, lantern eyes) · Rustler's Hound (collar) · Gnawbone (spotted hyena, mane mesh) · Gravebound Hound (undead, exposed ribs mesh) · Pyrehound (ember cracks, flame mane) · Cinderpaw (boss variant, collar) | 15 |
| CRE-B02 | ☐ | **Boar** | Charge, Root | Meadow Boar · Tuskfall Boar (snowy) · Tusked Rooter · Mudtusk (large, muddy) · Thornback Boar (spine mesh) | 5 |
| CRE-B03 | ☐ | **Spider** | Web spit, Drop from ceiling, Rear up | Greenhollow Spider · Briar Widow (red hourglass) · Mother Mirefang (huge, egg-sac mesh) · Canopy Weaver (leaf-gold) · Crystal Skitterer (crystal carapace mesh) · Glimmerqueen · Tunnel Lurker (pale) · Chasm Lurker (pale, glow-sac mesh) | 8 |
| CRE-B04 | ☐ | **Bear** | Stand and roar, Maul, Sleep | Young Shale Bear (small, grey) · Shale Bear (grey) · Pale Cave Bear (white, blind eyes) · Old Blindmaw · Russet Bear · Ironroot Bear (dark) · Old Ironhide (armoured scars) | 7 |
| CRE-B05 | ☐ | **Big cat** | Stealth prowl, Pounce | Snowshoe Lynx · Whitepelt · Crag Stalker (tawny) · Mistcat (smoke-grey, wispy shader) · Mistcat Matriarch | 5 |
| CRE-B06 | ☐ | **Ram / goat** | Headbutt, Graze | Crag Ram · Ironhorn Ram (iron-dark horns) · Feral Billy (goat mesh: beard, thin horns) · Old Bitterhorn (giant) · + mount skins (see doc 1) · farm goats and sheep (critters) | 6 |
| CRE-B07 | ☐ | **Stag** | Antler charge, Graze, Alert | Rutting Stag · ambient deer (doe mesh, no antlers) | 2 |
| CRE-B08 | ☐ | **Fox** | Dash, Dig | Russet Fox · Red Tom | 2 |
| CRE-B09 | ☐ | **Bird (flying)** | Fly idle, Fly forward, Swoop, Land, Perch | Field Harrier · Highland Buzzard · Horned Owl (owl head mesh) · Carrion Kite · Crag Eagle (large; flight taxi) · ambient crows, gulls over Solhaven | 6 |
| CRE-B10 | ☐ | **Bat** | Fly idle, Fly forward, Screech, Hang | Lanternwing Bat (glowing wing-tips) · Gloom Bat | 2 |
| CRE-B11 | ☐ | **Snapper (turtle)** | Withdraw into shell | Creek Snapper | 1 |
| CRE-B12 | ☐ | **Mirejaw (crocodilian)** | Death roll, Submerge, Lunge | Fen Lurker | 1 |
| CRE-B13 | ☐ | **Skink / gazer (lizard)** | Gaze (head raise), Tail shed | Quarry Skink · Cinder Skink (ember stripes) · Obsidian Gazer (glass-black, crystal crest mesh) · Gazer Matriarch Vitrea | 4 |
| CRE-B14 | ☐ | **Scorpion** | Sting, Claw grip | Scoria Stinger | 1 |
| CRE-B15 | ☐ | **Beetle** | Spray, Burrow, Roll | Leafmold Beetle · Hop-Blight Beetle (sickly green) · Stonecrawler (rock carapace mesh) · Old Flint · Stonecrawler Behemoth (huge, own mesh detail) | 5 |
| CRE-B16 | ☐ | **Rat** | Gnaw | Rail Rat · critter rat | 2 |
| CRE-B17 | ☐ | **Worm / wyrm** | Burrow in, Burrow out, Constrict, Spit | Rock Borer · Rift Wyrm (segmented plates) | 2 |
| CRE-B18 | ☐ | **Strider (tall bird)** | Kick, Sprint, Preen | Mesa Strider | 1 |
| CRE-B19 | ☐ | **Drake** | Fly idle, Fly forward, Breath, Wing buffet, Land | Rimewing Whelp (small, frost) · Cinderwing Drake (ember) | 2 |

## 2. Humanoid creatures (own rigs)

| ID | Done | Rig | Extra clips | Skins | Skins |
|---|---|---|---|---|---|
| CRE-H01 | ☐ | **Burrowkin** (mole-folk, candle on head) | Dig, Throw, Cast, Flee | Digger · Tunneler (pick) · Candlewarden (robe, big candle) · Kibbler the Candle King (crown of candles) · Quarry Sapper (dynamite belt) · Rootgnawer (bark armour) | 6 |
| CRE-H02 | ☐ | **Gravelkin** (squat rock-eaters) | Gnaw, Throw rock, Frenzy | Scrabbler · Gnasher · Rockchucker · Grawl the Boulder-Eater (large) · Sinkdweller (mud) · Bonechewer (bone jewellery) · Chief Gnarr · Underdweller (pale) · Shardchewer (crystal teeth) · Shard-Chief Krakk · Deepdelver (lamp-helmet) | 11 |
| CRE-H03 | ☐ | **Gillkin** (fish-folk) | Net throw, Cast, Call allies | Silverrun Gillkin · Longstrand Netter · Longstrand Tidecaller (shell staff) | 3 |
| CRE-H04 | ☐ | **Ogre** | Smash, Stomp, Cast, Boulder throw, Sit | Stonemaw Brute · Hexer (fetishes, staff) · Crusher Gorm (iron fists) · Warlord Urgoth (armour, tusk helm) · Mugga One-Tusk (shaman) · Stonemaw Exile · Hrokk the Unbought | 7 |
| CRE-H05 | ☐ | **Howler** (hyena-folk) | Bola throw, Cackle, Cast | Raider · Bonecaller (bone staff, mask) | 2 |
| CRE-H06 | ☐ | **Harpy** | Fly idle, Fly forward, Dive, Screech | Peak Screecher · Shriekmother Kaa (large, crest) | 2 |
| CRE-H07 | ☐ | **Elf** (future player rig; NPC-quality now) | Uses the player animation set, retargeted | Pactwatch Scout · Thornspeaker · Ysolde Thornwake · Blightwatcher Aelar · Blightwatcher archers | 5 outfits, 2 bodies (M/F) |

## 3. Undead, spirits and aberrations

| ID | Done | Rig | Extra clips | Skins | Skins |
|---|---|---|---|---|---|
| CRE-U01 | ☐ | **Skeleton** | Reassemble, Shield block | Restless Bones · Bone Sentinel (shield, helm) · Barrow Guardian (ancient armour) · Buried Legionary (imperial armour, tower shield) · Buried Praetorian (raid) | 5 |
| CRE-U02 | ☐ | **Shambling dead** | Lurch, Grab, Rise from ground | Cinderwight (glowing chest cinder) · Cinderwight Thrall · Crypt Shambler (bloated) · Drowned Pilgrim (sodden robes) · Barrow Wight (frost) · Gallows Jack (noose, large) · Hollowed Husk (cracked, violet glow) | 7 |
| CRE-U03 | ☐ | **Spectre (floating, no legs)** | Float idle, Phase out/in, Wail, Cast | Spectral Handmaiden · Echo Wraith · Sister Maudlin (boss) · The Lamplighter's Ghost (lantern) · Marshal's Shade · Buried / Vaultbound Magister (robed lich-look) · Ink Wraith (black liquid shader) + Ink Blot (small) · Restless Ancestor (dwarf proportions mesh) · Echo Sisters ×3 (raid, unique heads/gowns) | 12 |
| CRE-U04 | ☐ | **Ooze** | Split, Engulf | Fermented Ooze (amber, foam) · Sulfur Ooze (yellow) · small split versions | 4 |
| CRE-U05 | ☐ | **Horror (tentacled mass)** | Constrict, Burrow | The Deepseam Horror (unique boss) · Rubble Horror (raid trash) · Stomach Polyp (raid, small) | 3 |

## 4. Elementals, constructs and plants

| ID | Done | Rig | Extra clips | Skins | Skins |
|---|---|---|---|---|---|
| CRE-E01 | ☐ | **Sprite (small floating elemental)** | Blink, Cast | Rimewater Sprite (ice) · Loose Slag Sprite · Ember Sprite · Kilnfire Wisp · Geode Sprite (crystal) · Bog Wisp (light orb) · Dust Devil (Hexwright pet) | 7 |
| CRE-E02 | ☐ | **Hulk (large elemental)** | Slam, Erupt, Crumble death | Slag Elemental · Molten Hulk · Clinker · Ore-Bound Elemental (stone + ore veins) · Crucible Golem (iron bands) | 5 |
| CRE-E03 | ☐ | **Gargoyle** | Stone form (freeze), Dive, Fly | Cairn Gargoyle · Spire Gargoyle | 2 |
| CRE-C01 | ☐ | **Scarecrow** | Flail, Collapse into straw | Cinderstuffed Scarecrow · Old Rattlebones (crown, cowbell) | 2 |
| CRE-C02 | ☐ | **Machine (wheeled/tracked)** | Spin blades, Rail charge, Break down | Thresher Construct · Rogue Rail-Golem · Clockwork Ram (engineering) · Target Dummy (static) · Mechanical Squirrel (tiny) | 5 |
| CRE-C03 | ☐ | **Animated armour (sentinel)** | Halberd sweep, Reassemble, Power down | Brandspire Sentinel (black iron, ember glow) · Tor Vael Sentinel (imperial bronze, violet glow) · Vault Sentinel · Hollowspire Sentinel (gothic steel) · Animated Armor (dungeon, removable helm) | 5 |
| CRE-P01 | ☐ | **Shambler (plant mound)** | Entangle, Spore puff | Bog Shambler · Glowcap Shambler (mushroom caps, glow) | 2 |
| CRE-P02 | ☐ | **Treant** | Root slam, Uproot, Take root | Mossback Treant · Old Mossback (huge, bird nests) · Grimroot Sapling (gnarled, noose vines) | 3 |

## 5. Unique bosses (own rig or heavily modified)

| ID | Done | Boss | Where | Needs |
|---|---|---|---|---|
| BOS-01 | ☐ | The Wickerman | Thornwick | Giant wicker effigy rig; burning state; 8 clips |
| BOS-02 | ☐ | The Stitched Choir | Gallowmere Crypts | Six-torso abomination; detachable arms (2 add meshes); six animated mouths; 10 clips |
| BOS-03 | ☐ | Molten Maw | The Slagworks | Slag serpent-mound rising from a sluice; hardened-crust state; 8 clips |
| BOS-04 | ☐ | The Great Bore | Stoneheart Deeps | Drilling engine (animated prop): sweep arm, 3 valves, steam vents |
| BOS-05 | ☐ | Lady Seraphine Vael | Hollowspire Keep | Human-F rig; unique gown, crown-less; 3 orbiting Shard objects; sword; dissolve-to-empty-gown |
| BOS-06 | ☐ | Ser Aldous the Faithless | Hollowspire Keep | Human-M rig; unique tarnished Cleric plate, cracked halo |
| BOS-07 | ☐ | Librarian Quill | Hollowspire Keep | Human-M rig; ink-dripping robes shader; giant book prop |
| BOS-08 | ☐ | Lord-Chamberlain Aubrec + 12 banquet nobles | Hollowspire Keep | Human rigs; 6 noble outfits ×2 colourways; seated/rise clips |
| BOS-09 | ☐ | Castellan Vorn | Hollowspire Keep | Human-M rig; steward armour; key-ring |
| BOS-10 | ☐ | The Bulwark of Tor Vael | Raid | Huge ward-golem built into a gate (upper body only); 8 clips |
| BOS-11 | ☐ | Marshal Korvash the Entombed | Raid | Skeleton rig, large; unique imperial marshal armour, cloak |
| BOS-12 | ☐ | Ghul'thar, Spawn of the Rift Maw | Raid | Giant wyrm rig (shared with BOS-15 at different scale); interior "stomach" room uses environment art |
| BOS-13 | ☐ | Archmagister Ilyra | Raid | Spectre rig variant with legs hidden by robes; polarity sigils |
| BOS-14 | ☐ | Vaelric, the Hollow King | Raid | Unique: seated-to-standing emperor, the Hollow Crown (5 detachable shards), sceptre; 14 clips incl. 3 phase transitions |
| BOS-15 | ☐ | Gorrath, the Rift Maw | World boss | Colossal wyrm: head/maw rig + 4 separate "coil" segments that erupt from terrain |
| BOS-16 | ☐ | Grimroot, the Hangman's Oak | World boss | Colossal rooted treant; noose-vines (grab clips), split-bark state |
| BOS-17 | ☐ | Pyrraxis, the Cinder Wyrm | World boss | Large dragon rig: ground set + flight set + strafing breath; 16 clips |
| BOS-18 | ☐ | Tor Vael Courtiers / Hollow Echoes | Raid | Human rig; translucent hollow shader; 1 outfit ×2 |

Other named bosses (Hale Morrow, Grolm Sootbeard, Edrik Vane, Dolga Blackmatch, Bertram Soot, Vigga Deepdrill, Urgoth, Hedda Cinderlock, Corvin Ashgrave, Oswin Kray, Gravedigger Holt, Overseer Grint, Thurga, Khardun Slagheart, Morrigan Blackspade, Hrothmund, Brannoch) use player or creature rigs with a **unique outfit** — counted in §6.

## 6. NPC outfits on player rigs

Enemy and friendly humanoids on the Human and Dwarf rigs. Each row is an outfit worn by male and female bodies. "Named" = a variant for the listed character, which has an outfit row of its own.

**How an outfit is made.** An outfit is a **dressed body**: a whole generated model of a person wearing the outfit, made once for each body it is worn on and fitted to that body's rig like a player body. It is a single mesh with its own baked texture; the clothing, hair and face are part of the mesh, so an NPC in a dressed body takes its face and hair from the model and not from customisation pieces. A dressed body stands on the body's own skeleton and plays the player animation set. The game looks for a dressed body by outfit and body, and uses it whole in place of the body and an outfit texture. An outfit that has no dressed body for a body is a texture painted for the constructed body's layout (body-region textures plus any helm or shoulder piece) and is drawn on the constructed body.

A humanoid enemy in a dwarven outfit stands on a dwarf body.

Open: whether dressed bodies are the permanent method for NPCs or a measure for the starting zones is not decided; the Asset Manifest has no row kind for a dressed body.

### Human rig

| ID | Done | Outfit | Worn by |
|---|---|---|---|
| NPC-HU01 | ☐ | Villager ×6 (farmer, miller, goodwife, labourer, child-size none, elder) | Brightmead, Harrowfield, Russetwood, Thornwick townsfolk |
| NPC-HU02 | ☐ | Tradesfolk ×4 (smith apron, innkeeper, merchant, cook) | All human hubs |
| NPC-HU03 | ☐ | Solhaven guard + officer | Solhaven, Brightmead, Harrowfield militia (tabard variant) |
| NPC-HU04 | ☐ | Thornwick Warden + Warden-Captain Dunmoor | Thornwick, Warden's Rest, Brandspire siege |
| NPC-HU05 | ☐ | Forester / hunter ×2 | Russetwood, Thornwick, Veilmoor |
| NPC-HU06 | ☐ | Cleric of the Dawn ×2 (brother, sister) | Trainers, Sister Avelyn, Sister Rosalind |
| NPC-HU07 | ☐ | Hedgewarden druid ×2 | Trainers, Corwin Ashby, Sorrel |
| NPC-HU08 | ☐ | Fighter trainer / sergeant | Trainers |
| NPC-HU09 | ☐ | Scholar / archivist ×2 | Maelis Dorne, Fenwick, Athenaeum staff, Petra Lowe |
| NPC-HU10 | ☐ | Noble / court ×3 | Queen Isolde (unique crown, gown), courtiers, Mayor |
| NPC-HU11 | ☐ | Lamplighter / peat-cutter ×2 | Veilmoor |
| NPC-HU12 | ☐ | Freeholder ×3 (caravaneer, pit-guard, barkeep) + Pitmaster Grask | Kite's Rest |
| NPC-HU13 | ☐ | Knight of Vigil's End + Knight-Commander | Veilmoor |
| NPC-HU14 | ☐ | Athenaeum digger ×2 | Spire Camp |
| NPC-HU15 | ☐ | **Ashhand cultist** ×3 (cutpurse, torchbearer, brander) + Hale Morrow | Brightmead, Russetwood charcoalers (soot variant) |
| NPC-HU16 | ☐ | **Harrow Reaver** ×3 (thug, poacher, firestarter) + Paymaster Grice, Sal Marrow | Harrowfield |
| NPC-HU17 | ☐ | **Woodland poacher** ×2 + Odo Ketch, Garrick Snare | Russetwood |
| NPC-HU18 | ☐ | **Kiln worker** ×3 (charcoaler, tender, guard) + Kilnmaster Soot | Russetwood |
| NPC-HU19 | ☐ | **Vane household** (houseguard) + Marshal Edrik Vane (unique armour) | Harrowfield |
| NPC-HU20 | ☐ | **Graverobber** | Thornwick |
| NPC-HU21 | ☐ | **Cinderbrand acolyte / preceptor / corpse-stitcher / kiln stoker** ×4 + Brandfather Kray (unique vestments) + Gravedigger Holt (large body scale, shovel) | Thornwick, Gallowmere Crypts |
| NPC-HU22 | ☐ | **Ashgrave household** (houseguard, ember-mage) + Brandspire pyromancer + Magister Ashgrave (two states: robed; chest split with shard) | Thornwick |
| NPC-HU23 | ☐ | **Hollowed villager** (blank-eyed shader over villager outfits) + Elder Tamsin Reed | Thornwick |
| NPC-HU24 | ☐ | **Hag** ×2 (fen, moor; hunched pose set, unique head) + Grizelda Pondwife | Thornwick, Veilmoor |
| NPC-HU25 | ☐ | **Blackspade** ×3 (digger, cutthroat, hexwright) + Red Harl, Captain Morrigan (unique coat, hat, pistol) | Riftlands |
| NPC-HU26 | ☐ | **Hollowed court** ×4 (knight, courtier, footman, chamberlain, chaplain) + Ser Cadoc | Veilmoor, Hollowspire Keep |
| NPC-HU27 | ☐ | Hrothmund the Barrow-King (ancient king armour, on skeleton or human rig) | Veilmoor |
| NPC-HU28 | ☐ | Legate Corvane (Covenant envoy: fine clothes, grey skin, stitched) | Kite's Rest |

### Dwarf rig

| ID | Done | Outfit | Worn by |
|---|---|---|---|
| NPC-DW01 | ☐ | **Hallborn** townsfolk ×5 (miner, smith, lamp-keeper, rail-wright, hall-wife) | Embercrag, Hammerdeep, Stoneheart Deeps, Ironroot Hold, Deepseam |
| NPC-DW02 | ☐ | **Dalefolk** townsfolk ×5 (farmer, shepherdess, brewer, hop-grower, cook) | Stonewake Dale, Ramshead, Emberwell |
| NPC-DW03 | ☐ | Hammerdeep guard + hall-captain | Hammerdeep, Embercrag, Deeps |
| NPC-DW04 | ☐ | Dale ranger + Dale-Reeve Stonewake | Stonewake Dale, Ironroot rangers (Ranger-Captain Farstride variant) |
| NPC-DW05 | ☐ | Hearthpriest ×2 | Cleric trainers |
| NPC-DW06 | ☐ | Stonesinger ×2 | Druid trainers, Deepmoss, Fjola |
| NPC-DW07 | ☐ | Battlemaster / fighter trainer | Trainers |
| NPC-DW08 | ☐ | Engineer / dammaster ×2 | Sluicewright, Sparkwright, Golemsbane |
| NPC-DW09 | ☐ | Lorekeeper | Brunhild Deepscroll, Inkfinger |
| NPC-DW10 | ☐ | High Thane Durek (unique regalia) + hall-thanes ×2 | Hammerdeep |
| NPC-DW11 | ☐ | Fort Ashwatch soldier + Commander Ragna | Cinderfall |
| NPC-DW12 | ☐ | Hunter ×2 | Ramshead Lodge, drake-hunter |
| NPC-DW13 | ☐ | **Slagborn** ×10 (lookout, firebrand, sapper, powderkeg, tunneler, blastwright, smuggler, runesmith, raider, pyresmith) — soot skin, ember tattoos, black iron | All Khazrun zones |
| NPC-DW14 | ☐ | **Slagborn named**: Grolm Sootbeard, Dolga Blackmatch, Powderkeg Pol, Vigga Deepdrill, Fusewright Odd, Runner Vask, Hedda Cinderlock, Captain Dorrun, Pyre-Captain Ilga | 9 head/prop variants |
| NPC-DW15 | ☐ | **Brandforge / Blackanvil heavy** ×4 (guard, slagcaster, ironbreaker, flamecaller) + Gatewarden Brannoch | Ironroot, Cinderfall |
| NPC-DW16 | ☐ | **Slagworks** ×5 (laborer, taskmaster, slagcaster, shieldbearer) + Overseer Grint, Bellows-Master Thurga, Forgemaster Khardun Slagheart (unique) | The Slagworks |
| NPC-DW17 | ☐ | **Dale Rustler** ×2 (rustler, hound-master) + Greedy Gund | Stonewake Dale |
| NPC-DW18 | ☐ | **Hollowed miner** + Foreman Brokk | Ironroot |

### Service and world NPCs (reuse outfits above; listed so none is missed)

Quest givers · vendors (general, trade, food, armorer, weaponsmith, reagent, recipe, stable/feed, reputation, PvP) · class trainers ×3 × both rigs · profession trainers ×12 · weapon master · innkeepers · eyrie-keepers · bankers · guild vault keeper · auctioneers · guild master · tabard designer · battlemaster · barber · riding trainer · ship captain and crew · mine-cart conductor · **spirit healer** (unique winged spectre, 1 model) · town criers · ambient citizens.

## 7. Critters and ambient life

| ID | Done | Critter | Zones |
|---|---|---|---|
| CRT-01 | ☐ | Rabbit / hare | Meridia fields, Stonewake |
| CRT-02 | ☐ | Squirrel | Forests |
| CRT-03 | ☐ | Chicken | Farms |
| CRT-04 | ☐ | Sheep | Stonewake, Ironroot steadings |
| CRT-05 | ☐ | Cow | Brightmead, Harrowfield |
| CRT-06 | ☐ | Frog / toad | Fens, Veilmoor |
| CRT-07 | ☐ | Snake | Riftlands, Cinderfall |
| CRT-08 | ☐ | Crow | Thornwick, Veilmoor |
| CRT-09 | ☐ | Cave cricket / glow-beetle | Stoneheart Deeps |
| CRT-10 | ☐ | Lizard | Cinderfall, Riftlands |
| CRT-11 | ☐ | Songbird flock (particle) | Brightmead, Russetwood |
| CRT-12 | ☐ | Fish school (under-surface decal) | Fishing waters |

## 8. Totals for this document

| Category | Rigs | Skins / outfits |
|---|---|---|
| Beasts | 19 | 79 |
| Humanoid creatures | 7 | 36 |
| Undead / aberrations | 5 | 31 |
| Elementals, constructs, plants | 8 | 31 |
| Unique bosses | 12 new rigs | 18 |
| NPC outfits (Human rig) | — | ≈ 75 outfits/variants |
| NPC outfits (Dwarf rig) | — | ≈ 65 outfits/variants |
| Critters | 11 | 12 |
| **Total** | **≈ 62 rigs** | **≈ 350 skins and outfits** |

Animation clips: ≈ 39 standard creature rigs × ~13 clips + 12 boss rigs × ~10 + critters ≈ **650 creature clips**.
