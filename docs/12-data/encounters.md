# Encounter Data — dungeons, raid and world bosses

[← Data Index](00-data-index.md) · Design: [Dungeons](../07-instances/dungeons.md) · [The Hollow Throne](../07-instances/raid-the-hollow-throne.md) · [World Bosses](../07-instances/world-bosses.md)

The numbers behind every instanced and world encounter: trash packs room by room, boss health, melee damage, every ability's timer and damage, and the drop chance of every item. The mechanics themselves are described in the design documents; this file only adds the numbers. All values are balance v0.

## 1. Rules used to set the numbers

| Value | Rule |
|---|---|
| Dungeon trash | Elite: ×2.4 template health, ×1.8 template damage at its level. "Weak" trash (Laborers, sprite swarms, Blots) uses the normal template |
| Boss health | **Set by fight length**: expected group damage per second × the target duration. This replaces the "×12–18 normal health" guideline, which gave fights of under a minute and could not fit the designed mechanics |
| Expected group DPS | Gallowmere 90 · Slagworks 145 · Hollowspire 320 · raid (10 players) 750 · world boss (20 players) 1,650 |
| Boss melee | Raw damage per second before armor: Gallowmere 40 · Slagworks 85 · Hollowspire 180 · raid 460 · world boss 520. Swing 2.0 s unless stated; ±15% per hit |
| Reference player health | Non-tank / tank: level 15: 600 / 850 · level 22: 1,000 / 1,400 · level 30 dungeon: 1,600 / 2,100 · level 30 raid: 1,900 / 2,700 |
| Avoidable damage | 35–45% of a non-tank's health per hit |
| Unavoidable group damage | 8–12% of a non-tank's health per pulse |
| Boss level | Dungeon bosses are their listed level; raid and world bosses are 33, so crushing blows (150%) apply to tanks below 165 Defense |
| Enrage | Every dungeon boss enrages (+200% damage) at 8 minutes; raid bosses at the time listed |
| Boss immunities | All bosses are immune to stun, root, fear, sleep, charm and taunt-forcing effects unless a mechanic says otherwise. Slows work at half strength |
| Dungeon loot | Each boss drops 2 items (final boss 3), chosen without repeats from its table. The chance shown per item is the chance that it is one of them |
| Trash loot | World green 8%, world blue 1%, coin level × 12–36 copper (humanoid and undead), cloth 45% |
| Reset | Dungeons reset when empty for 30 minutes; raid weekly |

## 2. Gallowmere Crypts (levels 13–16)

### Trash stat blocks

| Creature | Level | Health | Damage per swing | Abilities with numbers |
|---|---|---|---|---|
| Crypt Shambler | 14 | 725 | 60–82 (2.6 s swing) | Rotting Grasp: disease, −10% Strength for 30 s, on hit, 20% chance |
| Cinderbrand Corpse-Stitcher | 14–15 | 580–630 | 20–27 | Stitch Flesh: heals an undead for 250, 2.5 s cast, every 12 s · Cinder Bolt: 62–84 Fire, 2.0 s cast |
| Cinderwight Thrall | 14–15 | 725–787 | 48–66 | Burning Grasp: 66 Fire over 12 s · explodes on death: 110 Fire within 8 yd after 2 s |
| Bone Sentinel | 15 | 787 | 52–70 | Blocks 30% of frontal attacks · Bone Wall: on death leaves a wall 6 yd wide for 60 s that blocks line of sight |
| Kiln Stoker | 15–16 | 787–862 | 52–76 | Throw Coals: ground fire 4 yd, 45 Fire per second for 8 s, every 10 s |
| Gravebound Hound | 14 | 363 (pack of 3; ×1.2 template) | 34–46 (1.6 s swing) | Leaps to the furthest target every 10 s |

### Packs by room

| Room | Packs | Composition |
|---|---|---|
| Gibbet stair | 3 | 2 Crypt Shamblers · 3 Gravebound Hounds · 1 Shambler + 1 Corpse-Stitcher |
| Charnel Hall | 5 | 2 Shamblers + 1 Stitcher (×2) · 3 Hounds (patrol) · 2 Cinderwight Thralls (×2) |
| Embalmers' Gallery | 4 | 1 Bone Sentinel + 2 Stitchers · 2 Thralls + 1 Stitcher · 3 Hounds · 2 Bone Sentinels |
| Side chapel approach (optional) | 2 | 2 Shamblers + 1 Bone Sentinel · 1 Stitcher + 2 Thralls |
| Cinder Kiln | 5 | 2 Kiln Stokers (×2) · 1 Stoker + 2 Thralls (×2) · 1 Bone Sentinel + 1 Stoker + 1 Stitcher |
| Sanctum stair | 2 | 2 Bone Sentinels + 1 Stitcher (×2). These Sentinels' Bone Walls are the cover used in the final fight |

Total: 21 packs, about 52 elite creatures, about 18 minutes of trash.

### Bosses

| Boss | Level | Health | Melee | Ability | Timer | Numbers |
|---|---|---|---|---|---|---|
| Gravedigger Holt | 15 | 13,500 | 80–108 per 2.4 s | Shovel Sweep | Every 9 s | 180–220 Physical in a 120° cone, 8 yd |
| | | | | Dig Up | Every 20 s | 2 Crypt Shamblers at 60% health from marked plots (6 plots) |
| | | | | Six Feet Under | Once at 50% | Random non-tank in an open grave for 4 s; 40 damage per second until pulled out (click) |
| The Stitched Choir | 15 | 16,000 | 68–92 per 2.0 s | Dirge | Constant | 8 Shadow per second to all, +8 per stack every 5 s; stops for 6 s and loses all stacks after 400 damage within 4 s, or an interrupt |
| | | | | Loose Stitch | At 66% and 33% | Arm add: 1,400 health, 40–54 per swing |
| | | | | Discord | Every 15 s | Random player: next spell costs double; lasts 10 s |
| Sister Maudlin (optional) | 15 | 13,500 | 60–82 per 2.0 s | Wail | Every 30 s | Fear 3 s to anyone not in the lit Circle of Candles |
| | | | | Candles | 6 at start | She snuffs one every 25 s; with none lit she casts Wail every 10 s |
| | | | | Sorrow | Constant | Heals herself 120 per 3 s; halved for each lit candle a player stands in |
| | | | | Unshriven Touch | Every 20 s on the tank | Curse: −25% healing received for 15 s |
| Brandfather Oswin Kray | 16 | 19,000 | 76–104 per 2.0 s | Searing Brand | Every 14 s | Random player: 120 Fire over 12 s; that player deals and takes +20% damage |
| | | | | Kindle the Faithful | Every 25 s | 2 Cinderwight Thralls at 50% health |
| | | | | Sermon of Ash | Every 30 s | 3 s channel, 60° cone, 30 yd: 110 Fire per second |
| | | | | Phase 2 at 40% | | +50% attack speed; stops Kindle |
| | | | | Ashen Nova | Every 12 s in phase 2 | 3 s cast: 380 Fire to all in line of sight; blocked by Bone Walls |

### Drop chances

| Boss | Items in table | Chance each | Other |
|---|---|---|---|
| Gravedigger Holt | 4 | 50% | — |
| The Stitched Choir | 4 | 50% | Choir's Tuning Fork: 100% for players on TM-16 |
| Sister Maudlin | 4 | 50% | Maudlin's Remains object appears on death (TM-17) |
| Brandfather Kray (3 items) | 6 | 50% | Kray's Dossier: 100% for players on TM-15 |

## 3. The Slagworks (levels 20–23)

Slag hazard: 90 Fire per second and −30% movement while standing in molten slag.

### Trash stat blocks

| Creature | Level | Health | Damage per swing | Abilities with numbers |
|---|---|---|---|---|
| Slagworks Laborer | 21 | 520 (normal) | 43–58 | Packs of 4 · at 30% health runs to the nearest lever (6 s); a pulled lever floods a marked floor strip with slag for 15 s |
| Slagborn Taskmaster | 22 | 1,334 | 82–110 | Whip Crack: Laborers within 20 yd +30% damage for 15 s, every 20 s |
| Slagborn Slagcaster | 22–23 | 1,067–1,137 | 33–45 | Slag Wave: 150–200 Fire in a 30 yd line, 2.5 s cast · Molten Armor: attackers take 25 Fire per hit, 30 s |
| Crucible Golem | 23 | 1,421 | 105–145 (2.4 s swing) | Slam: 160 Physical and 12 yd knockback, every 14 s |
| Ember Sprite Swarm | 21 | 6 × 210 (40% template) | 12–16 each | Blink every 8 s |
| Slagborn Shieldbearer | 22–23 | 1,334–1,421 | 82–118 | Immune to frontal attacks; allies behind it within 8 yd take −50% damage |

### Packs by room

| Room | Packs | Composition |
|---|---|---|
| Ore Lift landing | 2 | 4 Laborers + 1 Taskmaster (×2) |
| Sorting Floor | 6 | 4 Laborers + 1 Taskmaster (×2) · 1 Shieldbearer + 2 Slagcasters (×2) · Ember Sprite Swarm (×2) |
| Slag Sluice banks | 4 | 1 Crucible Golem (×2) · 1 Shieldbearer + 1 Slagcaster + 1 Taskmaster · Ember Sprite Swarm |
| Bellows Hall | 6 | Two packs guard each of the 3 Great Bellows: 1 Shieldbearer + 2 Slagcasters, and 4 Laborers + 1 Taskmaster |
| Crucible approach | 3 | 2 Crucible Golems · 1 Shieldbearer + 2 Slagcasters (×2) |

Total: 21 packs, about 70 creatures, about 24 minutes of trash. Each Great Bellows has 2,500 health and is damaged only by the Sapper's Charge (CF-10) or by 6,000 player damage.

### Bosses

| Boss | Level | Health | Melee | Ability | Timer | Numbers |
|---|---|---|---|---|---|---|
| Overseer Grint | 22 | 22,000 | 145–195 per 2.0 s | Double Shift | At 75%, 50%, 25% | Calls 4 Laborers, enraged (+50% damage, +30% speed) for 20 s |
| | | | | Lash | Every 10 s on the tank | 240 Physical over 12 s, stacks to 3 |
| | | | | Dock Pay | Every 25 s | 3 s stun on the highest-threat non-tank; 140 Physical |
| Molten Maw | 22 | 26,000 | 150–200 per 2.2 s | Engulf | Every 30 s | Swallows the occupied platform after 8 s; anyone still on it takes 700 Fire |
| | | | | Slag Spit | Every 8 s | 5 yd pool under a random player: 90 Fire per second for 12 s |
| | | | | Cool and Crack | When lured onto a grate (lever, 45 s reset) | +100% damage taken for 10 s |
| | | | | Immunities | | Fire, bleeds |
| Bellows-Master Thurga | 23 | 14,000 | 55–75 (caster) | Stoke | Every 18 s | 2.5 s cast: heals Cinderpaw 1,500 and gives it +25% damage for 12 s; interruptible |
| | | | | Bellows Blast | Every 15 s | 180 Fire in a line and 15 yd knockback |
| Cinderpaw | 23 | 12,000 | 150–200 per 1.8 s | Fire Breath | Every 12 s | 220–260 Fire in a 90° cone, 15 yd |
| | | | | Fetch | Every 30 s | Drags a healer to Thurga and stuns 2 s |
| | | | | Lull | | Can be put to sleep by Lull Beast (duration halved to 10–15 s) |
| | | | | Survivor's rage | 15 s after the other dies | +100% damage, +50% attack speed |
| Forgemaster Khardun Slagheart | 23 | 35,000 | 160–215 per 2.4 s | Hammer of the Forge | Every 15 s | 380 Physical; if not blocked, Ringing: stun 3 s |
| | | | | Quench | Every 35 s | Random non-tank removed from the fight 4 s; their debuffs are cleansed |
| | | | | Sparks | Every 10 s | 90 Fire to all |
| | | | | Phase 2 at 50% | | Hollow-Forged: each melee hit drains 60 mana or 10 rage |
| | | | | Shard Resonance | Every 20 s in phase 2 | 3 expanding rings of Shadow, 350 each, with a gap to step through |
| | | | | Phase 3 at 20% | | Slag floods one floor quarter every 15 s; after 60 s the whole floor is slag |

### Drop chances

| Boss | Items in table | Chance each | Other |
|---|---|---|---|
| Overseer Grint | 4 | 50% | — |
| Molten Maw | 4 | 50% | Molten Maw's Core: 100% for players on CF-11 |
| Thurga and Cinderpaw (one chest) | 4 | 50% | Counts as the kill for CF-10 with the three Bellows |
| Khardun Slagheart (3 items) | 6 | 50% | Second Shard (Great Crucible object): 100% on CF-09 · Slagheart's Crucible-Shard: 100% on RL-35 · Plans: Starforged Longblade 10% · Schematic: Starmetal-Barrel Rifle 10% |

## 4. Hollowspire Keep (levels 27–30)

### Trash stat blocks

| Creature | Level | Health | Damage per swing | Abilities with numbers |
|---|---|---|---|---|
| Hollowed Footman | 28 | 1,927 | 111–151 | Formations of 3 · Hold the Line: +40% armor while 2 or more stand within 5 yd |
| Hollowed Chamberlain | 28–29 | 1,540–1,630 | 45–63 | Announce: 3 s cast, calls the next pack; interruptible · Hollow Whisper: 180 Shadow over 9 s |
| Spectral Handmaiden | 29 | 1,630 | 47–63 | Phase: untargetable 2 s every 12 s · Mend: heals an ally 500, 2 s cast · Shadow Bolt: 150–200, 2 s cast |
| Animated Armor | 29 | 2,040 | 140–190 (2.4 s swing) | Reassemble: returns at 50% health 8 s after death unless its Fallen Helm object is clicked (3 s) |
| Ink Wraith | 29 | 1,630 | 47–63 | Silence 3 s every 15 s · splits into 2 Blots (425 health each) on death |
| Hollowed Chaplain | 29–30 | 1,630–1,720 | 47–67 | Inverted Prayer: Shadow damage equal to 40% of the target's missing mana (minimum 120), 2 s cast |
| Spire Gargoyle | 30 | 2,150 | 122–166 (pairs) | Stone Form: immune and heals 5% per second for 6 s, at 40% health, once |

### Packs by room

| Room | Packs | Composition |
|---|---|---|
| Gatehouse | 3 | 3 Footmen (×2) · 3 Footmen + 1 Chamberlain |
| Great Hall | 5 | 3 Footmen + 1 Chamberlain (×2) · 2 Handmaidens + 1 Chamberlain (×2) · 2 Animated Armor |
| Library (west) | 6 | 2 Ink Wraiths (×3) · 1 Chamberlain + 2 Handmaidens (×2) · 2 Animated Armor |
| Barracks Chapel (east) | 6 | 3 Footmen + 1 Chaplain (×3) · 2 Chaplains + 1 Handmaiden (×2) · 2 Animated Armor |
| Spire stair | 4 | 2 Spire Gargoyles (×4) |

Total: 24 packs, about 75 elite creatures, about 30 minutes of trash. Each dungeon run also has 1–2 guaranteed Starpetal nodes and 2 Starmetal deposits.

### Bosses

| Boss | Level | Health | Melee | Ability | Timer | Numbers |
|---|---|---|---|---|---|---|
| Castellan Vorn | 29 | 57,000 | 305–415 per 2.0 s | Lock the Gates | Every 45 s | Splits the room for 15 s; each half faces 2 Footmen at 60% health |
| | | | | Ring of Keys | With each Lock | A marked circle appears for 5 s; a player standing in it opens the gates after 6 s instead of 15 |
| | | | | Dutiful Strike | Every 6 s on the tank | −8% armor per stack, 20 s, resets when the gates drop |
| The Banquet of Hollows | 29 | Event | — | Toast | Before each course | 4 s to click a seat or take 900 Shadow |
| | | | | Soup | Course 1 | 3 nobles, 5,000 health each; their hits slow 30% for 6 s |
| | | | | Roast | Course 2 | 3 knife-throwers, 5,000 each; 180–220 Physical thrown every 3 s at random players |
| | | | | Wine | Course 3 | The Baron: 14,000 health, 380–500 per 2.6 s swing, staggers 5 yd left or right every 8 s |
| | | | | Dessert | Course 4 | Lord-Chamberlain Aubrec: 26,000 health, 280–380 per swing; uses the slow, the knives (every 6 s) and a Toast every 30 s |
| Librarian Quill | 30 | 58,000 | 110–150 (caster) | Ink Lash | Constant | 320–380 Shadow, 2.0 s cast, on the tank |
| | | | | Overdue | Every 25 s | Marks a player; an Ink Wraith (unkillable, 60% speed) chases them until led through a light-shaft (4 shafts) |
| | | | | Redact | Passive | Ink pools (5 yd) left by dead Blots silence anyone inside |
| | | | | Index | At 50% and 25% | Immune to one school for 20 s: Nature, Arcane, Holy or Physical, shown by the glowing shelf |
| Ser Aldous the Faithless | 30 | 60,000 | 320–430 per 2.2 s | Oath of Hollow, then Verdict | Every 25 s | 4 s Oath buff, then 1,100 Shadow to a random player; cancelled if he is stunned during the Oath (the one stun that works on him) |
| | | | | Unhallowed Ground | Constant | Zone under him grows 1 yd every 3 s while he stands still: 150 Shadow per second |
| | | | | Hollow Ward | At 30% | Immune and heals 2% per second for 8 s; broken by Verdict (Radiance) or 10 hits of Holy damage |
| Lady Seraphine Vael | 30 | 86,000 | Phase 2: 300–400 per 1.8 s | Phase 1 (100–60%) | | She is immune. Three Reflections (9,000 health each) must die; each kill removes 13% of her health |
| | | | | Shard of Ambition | Every 20 s | Two Fire beams sweep the room: 600 per touch |
| | | | | Shard of Memory | Every 30 s | Hollow copy of a random player: 4,000 health, uses 2 of that player's abilities at 60% strength |
| | | | | Shard of Hunger | Constant | Drains 80 per second from the player furthest from her |
| | | | | Phase 2 (60–25%) Imperial Decree | Every 18 s | Random player must stop moving, casting or attacking for 4 s, or take 1,000 Shadow |
| | | | | Courtly Step | Every 22 s | Teleports behind the healer; next swing +50% |
| | | | | Phase 3 (25–0%) Crown's Shadow | Every 5 s | 120 Shadow to all, +40 each pulse |

### Drop chances

| Boss | Items in table | Chance each | Other |
|---|---|---|---|
| Castellan Vorn | 4 | 50% | — |
| The Banquet of Hollows (chest) | 5 | 40% | — |
| Librarian Quill | 4 | 50% | Librarian's Index: 100% for players on VM-31 |
| Ser Aldous | 4 | 50% | Aldous' Oathblade: 100% on VM-30. Psalter of Doubt drops only if a Cleric is in the group |
| Lady Seraphine (3 items) | 7 | 43% | Seraphine's Signet: 100% on RL-35 · Plans: Starmetal Bulwark 10% · Pattern: Grovekeeper's Mantle 10%. Charm of the Empty Gown drops only if a Druid is in the group |

## 5. The Hollow Throne (10 players, level 30; bosses level 33)

Ward Strain: each boss room has 5 ward-pylons. Each pylon cracks after the raid takes 12,000 points of avoidable damage in that room; when the fifth breaks the room collapses and the raid wipes. Pylons do not repair during an attempt.

### Trash stat blocks (level 31–32 elites, ×4 template health)

| Creature | Level | Health | Damage per swing | Abilities with numbers |
|---|---|---|---|---|
| Buried Praetorian | 32 | 4,000 | 260–350 | Testudo: immune to frontal attacks for 8 s every 20 s when 3 stand together |
| Vaultbound Magister | 32 | 3,200 | 100–140 | Aether Lance: 600–700 Arcane, 2.5 s cast · Mana Burn: burns 300 mana and deals the same, 2 s cast |
| Vault Sentinel | 32 | 4,400 | 290–390 (2.4 s) | Resists Arcane 50% · Overload on death: 500 Arcane within 10 yd after 3 s |
| Rubble Horror | 31 | 3,800 | 240–320 | Constrict: holds a player, 200 per second, until it takes 1,500 damage |
| Hollow Courtier | 31 | 3,000 | 90–120 | Applause: allies within 20 yd +25% damage 10 s, every 15 s · Hollow Whisper: 400 Shadow over 9 s |
| Chasm Stalker | 32 | 3,600 | 280–380 (1.6 s) | Stealth patrol; Pounce on the nearest healer: stun 2 s and 500 Physical |

| Section | Packs | Composition |
|---|---|---|
| Vault Gate approach | 4 | 3 Praetorians + 1 Magister (×2) · 2 Vault Sentinels (×2) |
| Hall of Petitioners | 6 | 4 Hollow Courtiers + 1 Praetorian (×3) · 2 Rubble Horrors (×2) · Chasm Stalker patrol |
| Buried Parade Ground | 5 | 3 Praetorians + 2 Magisters (×3) · 2 Vault Sentinels (×2) |
| Choir Vault | 5 | 4 Courtiers (×2) · 2 Magisters + 2 Praetorians (×2) · Chasm Stalker patrol |
| Aether Conservatory | 5 | 2 Vault Sentinels + 2 Magisters (×3) · 2 Rubble Horrors (×2) |
| Throne approach | 3 | 3 Praetorians + 2 Magisters + 1 Courtier (×3) |

Trash loot: Vault Pearl 15% · *Vaultwalker Treads* 1% · *Praetorian's Seal* 1% · Formula: Enchant Weapon — Dawnfire 0.5% · world epic 0.5%. Trash respawns after 2 hours if the following boss is alive.

### Bosses

| Boss | Health | Melee | Ability | Timer | Numbers |
|---|---|---|---|---|---|
| The Bulwark of Tor Vael | 225,000 | 780–1,060 per 2.4 s | Seismic Slam | Every 12 s | 1,500 Physical; Fractured: −20% armor per stack for 30 s |
| | | | Rockfall | Every 20 s | One of 4 lanes, 3 s warning: 1,400 Physical |
| | | | Ward Pulse | Every 30 s | 450 Arcane to all |
| | | | Cave-In | At 6 min | Two lanes per Rockfall; hard enrage at 8 min |
| The Echo Sisters | 75,000 each | Lirael 250–340 · Morwen 250–340 · Ysa 640–860 | Beckon (Lirael) | Every 25 s | Charms the 2 nearest players for 8 s or until they take 600 damage |
| | | | Chain Squall (Morwen) | Every 12 s | 500 Nature, arcs to players within 8 yd, +25% per jump, up to 5 |
| | | | Downdraft, then Crush (Ysa) | Every 35 s | Pulls all to her; 3 s later 1,800 Physical within 12 yd |
| | | | Harmony | When two are within 15 yd | Each heals the other 2% per second |
| | | | Revive | | A dead sister returns at 50% if the others live 15 s longer. Enrage at 8 min |
| Marshal Korvash | 270,000 | 800–1,080 per 2.2 s | Ballista Volley | Every 18 s | 2 of 5 lanes, 3 s warning: 1,300 Physical |
| | | | Fall In! | Every 40 s | 4 Buried Legionaries (3,500 health; 180–240 per swing; Choking Dust silence 3 s) |
| | | | Entomb | Every 30 s | Random player buried 6 s: 300 per second |
| | | | Hold the Line | At 30% | Slabs fall everywhere outside 3 arches; one arch falls every 30 s. Enrage when the last falls |
| Ghul'thar | 290,000 | 760–1,030 per 2.0 s | Undermine | Every 45 s | 8 s warning; players left on the ledge take 2,500 and fall |
| | | | Grit Breath | Every 15 s | 900–1,100 Nature in a 60° cone |
| | | | Spawn | Every 30 s | 3 eggs (1,200 health); hatch after 15 s into Rift Spawn (2,500 health, 200–270 per swing) |
| | | | Maw phase | At 50%, then every 90 s | Swallows the main tank for up to 30 s; inside, 4 Stomach Polyps (2,000 health each; each kill deals 2% of the boss's health); stomach acid 150 per second |
| Archmagister Ilyra | 270,000 | 280–380 (caster) | Aether Polarity | Every 40 s | Flow or Ebb for 20 s: +10% damage per same-mark ally within 5 yd; opposite marks within 5 yd explode for 800 Arcane each |
| | | | Recitation | Every 60 s | 10 s cast that kills the raid; needs 3 interrupts or stuns, each at least 2 s apart |
| | | | Hollow Lance | Every 15 s on the tank | 2,200 Shadow (resistible) |
| | | | Mirror of Years | At 40% | Each player's copy has 30% of their health and 50% of their damage; 20 s to kill it or it explodes for 1,500 |
| Vaelric, the Hollow King | 400,000 | 820–1,110 per 2.2 s | Phase 1: Imperial Edict | Every 20 s | Two groups get different orders (stop moving, casting or attacking) for 4 s, or take 1,400 Shadow |
| | | | Sceptre Strike | Every 12 s | 1,700 Physical on the tank |
| | | | Summon Court | Every 45 s | 4 Hollow Courtiers (3,000 health) kneel for 15 s; each one that finishes gives him +10% damage for the rest of the fight |
| | | | Phase 2 (65–30%): Crown-bearers | Rotates every 30 s | Ambition: deal and take +50% · Memory: abilities echoed at 30% against the raid · Hunger: drains 100 per second from allies within 8 yd · Grief: cannot be healed above 50% · Pride: 1,000 Shadow per second while moving |
| | | | Hollow Echoes | 5, one per shard | 12,000 health each; killing one halves that shard's burden for the rest of the phase |
| | | | Phase 3 (30–0%): Collapse | Every 20 s | The arena radius shrinks 5 yd, from 40 to 10; outside it 1,500 per second |
| | | | Earthen Wrath | Every 6 s | 350 Physical to all, +50 each pulse |
| | | | Bury | Every 25 s | A healer is buried until 2,000 damage is dealt to the rubble |
| | | | Hard enrage | 11 min | |

### Raid drop chances

| Boss | Tier token | Other items in table | Chance each (2 drop; 3 from Vaelric) | Extras |
|---|---|---|---|---|
| The Bulwark | Vaultforged Grips ×2 (100%) | 4 | 50% | — |
| The Echo Sisters | — (3 non-token items instead of 2) | 5 | 60% | — |
| Marshal Korvash | Vaultforged Mantle ×2 | 4 | 50% | — |
| Ghul'thar | Vaultforged Legguards ×2 | 4 | 50% | Rift-Spawn Scale is one of the 4 |
| Archmagister Ilyra | Vaultforged Crown ×2 | 4 | 50% | — |
| Vaelric | Vaultforged Raiment ×2 | 6 | 50% | Hollow Shard Fragment 5% · Reins of the Vault Charger 1% |

Athenaeum reputation: 150 per boss, 300 for Vaelric.

## 6. World bosses (level 33; one 20-player raid)

| Boss | Health | Melee | Ability | Timer | Numbers |
|---|---|---|---|---|---|
| Grimroot, the Hangman's Oak | 750,000 | 880–1,190 per 2.4 s | Root Lash | Every swing | Also hits the second-highest threat within 8 yd; Splintered: −10% armor per stack, 20 s |
| | | | Gallows Vines | Every 40 s | 3 players hoisted: 250 per second; each Noose has 4,000 health |
| | | | Rotfall | Every 15 s | 5 circles of 6 yd: 800 Nature and a poison of 600 over 12 s |
| | | | Saplings | Every 45 s | 6 Grimroot Saplings (2,400 health) reach the trunk in 20 s; each heals it 1% |
| | | | Heartwood Exposed | At 30% | Takes +100% damage; Root Lash hits everyone within 10 yd |
| | | | Resistance | | Nature 50% |
| Pyrraxis, the Cinder Wyrm | 750,000 | 900–1,220 per 2.2 s | Flame Breath | Every 14 s | 1,400–1,700 Fire in a 70° cone, 30 yd |
| | | | Tail Sweep | Every 20 s | 700 Physical and 20 yd knockback behind her |
| | | | Wing Buffet | Every 30 s | 500 Physical to the front and halves the tank's threat |
| | | | Air phase | Every 90 s for 25 s | 4 fire lines (1,500 each); 3 Cinderwing Drakes land (elite, 6,000 health); she takes −50% damage from ranged |
| | | | Ashfall | Constant | 30 Fire per second per stack, +1 stack every 10 s; standing in geyser steam (2 of 6 geysers active, rotating every 20 s) clears it |
| | | | Immolate the Roost | At 20% | The plateau burns inward 4 yd every 10 s |
| | | | Immunity | | Fire |
| Gorrath, the Rift Maw | 750,000 | 860–1,160 per 2.4 s | Maw | Every 60 s | 6 s pull toward the mouth; swallowed players are spat out at 20% health and stunned 3 s |
| | | | Coils | Every 45 s | 4 coils (15,000 health) each pin a player (200 per second); each coil killed deals 3% of Gorrath's health |
| | | | Landslide | At 75%, 50% | Upper terrace falls; the climb back passes 6 Chasm Lurkers |
| | | | Dust Plume | Every 25 s | 12 yd cloud for 10 s: −50% hit chance |
| | | | Rift Spawn | Every 50 s | 2 adds (elite, 8,000 health, 400–540 per swing) |
| | | | Going to Ground | At 25% | 90 s to kill or it escapes with no loot |

World boss loot: 4 items from a table of 7, so each item has a 57% chance per kill. The quest item for CF-34, RL-34 or VM-35 is credited to every raid member on the quest. Respawn 3–5 days.
