# Creature Data — stat blocks, abilities and loot

← [Data Index](00-data-index.md) · Rules: [NPC AI & World](../02-systems/npc-ai-and-world.md) · [Items & Loot](../02-systems/items-and-loot.md#7-loot-generation)

Generated from the creature tables in the zone documents using the rules in the [Data Index](00-data-index.md#2-creature-rules). **Do not edit by hand**: change the zone table or the rule, then regenerate. Health and damage are given at the lowest and highest level of the creature's range. Ability numbers are at the highest level.

## Brightmead Vale — T1, levels 1–5 (Meridia)

### Stat blocks

| ID | Creature | Level | Type | Health | Damage per swing | Swing | Armor | Mana | Respawn | XP |
|---|---|---|---|---|---|---|---|---|---|---|
| CRE-BM-01 | Vale Wolf Pup | 1 | Beast | 42 | 3–5 | 2 s | 20 | — | 2.5 min | 50 |
| CRE-BM-02 | Vale Wolf | 2–3 | Beast | 57–72 | 5–7 to 6–9 | 2 s | 75 | — | 2.5 min | 55–60 |
| CRE-BM-03 | Meadow Boar | 2–3 | Beast | 57–72 | 5–7 to 6–9 | 2 s | 75 | — | 2.5 min | 55–60 |
| CRE-BM-04 | Burrowkin Digger | 1–2 | Humanoid | 42–57 | 3–5 to 5–7 | 2 s | 48 | — | 2.5 min | 50–55 |
| CRE-BM-05 | Burrowkin Tunneler | 3 | Humanoid | 72 | 6–9 | 2 s | 75 | — | 2.5 min | 60 |
| CRE-BM-06 | Burrowkin Candlewarden | 3–4 | Humanoid (caster) | 58–70 | 3–3 to 3–4 | 2 s | 77 | 240 | 2.5 min | 60–65 |
| CRE-BM-07 | Greenhollow Spider | 3–4 | Beast | 72–87 | 6–9 to 8–11 | 2 s | 102 | — | 2.5 min | 60–65 |
| CRE-BM-08 | Ashhand Cutpurse | 3–4 | Humanoid | 72–87 | 6–9 to 8–11 | 2 s | 102 | — | 2.5 min | 60–65 |
| CRE-BM-09 | Ashhand Torchbearer | 4–5 | Humanoid | 87–102 | 8–11 to 9–13 | 2 s | 130 | — | 2.5 min | 65–70 |
| CRE-BM-10 | Ashhand Brander | 5 | Humanoid (caster) | 82 | 4–5 | 2 s | 98 | 285 | 2.5 min | 70 |
| CRE-BM-11 | Silverrun Gillkin | 4–5 | Humanoid | 87–102 | 8–11 to 9–13 | 2 s | 130 | — | 2.5 min | 65–70 |
| CRE-BM-12 | Creek Snapper | 4 | Beast | 87 | 8–11 | 2 s | 102 | — | 2.5 min | 65 |
| CRE-BM-13 | **Kibbler the Candle King** (Rare) | 4 | Humanoid | 130 | 9–13 | 2 s | 102 | — | 2–8 h | 65 |
| CRE-BM-14 | **Old Greymaw** (Elite) | 5 | Beast | 306 | 17–23 | 2 s | 130 | — | 7 min | 140 |
| CRE-BM-15 | **"Brander" Hale Morrow** (Mini-boss) | 5 | Humanoid | 204 | 12–16 | 2 s | 130 | — | 5 min | 210 |

### Abilities

| Creature | Ability | Kind | Effect at top level |
|---|---|---|---|
| Vale Wolf Pup | — | — | Melee only |
| Vale Wolf | Bite | Damage over time | 18 Physical over 12 s (4 ticks); applied on hit, cooldown 15 s; small bleed |
| Meadow Boar | Charge | Opener | 12 Physical on the first hit; closes from 8 to 25 yd; first hit |
| Burrowkin Digger | — | — | Melee only |
| Burrowkin Tunneler | Pick Throw | Ranged or spell | 8–12 Physical; 2 s cast; range 30 yd |
| Burrowkin Candlewarden | Hot Wax | Ranged or spell | 17–23 Fire; 2 s cast; range 30 yd |
| Greenhollow Spider | Weak Poison | Damage over time | 22 Nature over 12 s (4 ticks); applied on hit, cooldown 15 s; DoT |
| Ashhand Cutpurse | Backstab opener | Opener | 14 Physical on the first hit; the creature is hidden until within 8 yd |
| Ashhand Torchbearer | Torch Toss | Ranged or spell | 12–16 Fire; 2 s cast; range 30 yd |
| Ashhand Brander | Searing Brand | Damage over time | 26 Fire over 12 s (4 ticks); applied on hit, cooldown 15 s; DoT |
| Ashhand Brander | Flee | Movement | Runs at 15% health for 8 s and alerts allies within 30 yd |
| Silverrun Gillkin | Net | Root | Roots 3 s; range 20 yd; cooldown 20 s |
| Silverrun Gillkin | calls allies | Summon | Calls 1 ally of the same family within 30 yd; once per fight unless a cooldown is given |
| Creek Snapper | Shell | Defensive | −50% damage, 4 s; lasts 6 s unless stated; cooldown 30 s |

### Loot

| Creature | Loot table |
|---|---|
| Vale Wolf Pup | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps · Stringy Wolf Meat 40% · World table |
| Vale Wolf | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Wolf meat 40% · Sharp Fang 25% · World table |
| Meadow Boar | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Boar Haunch 40% · World table |
| Burrowkin Digger | Coin 3–18c (100%) · Linen Cloth 35% · Grey junk 70% · Tallow Candle 40% · World table |
| Burrowkin Tunneler | Coin 9–27c (100%) · Linen Cloth 35% · Grey junk 70% · Tallow Candle 40% · World table |
| Burrowkin Candlewarden | Coin 9–36c (100%) · Linen Cloth 35% · Grey junk 70% · Candles 40% · World table |
| Greenhollow Spider | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Gooey Spider Leg 40% · Spider Silk 25% · World table |
| Ashhand Cutpurse | Coin 9–36c (100%) · Linen Cloth 35% · Grey junk 70% · Branded Coin 40% · World table |
| Ashhand Torchbearer | Coin 12–45c (100%) · Linen Cloth 35% · Grey junk 70% · Branded Coin 40% · World table |
| Ashhand Brander | Coin 15–45c (100%) · Linen Cloth 35% · Grey junk 70% · minor potions 40% · World table |
| Silverrun Gillkin | Coin 12–45c (100%) · Linen Cloth 35% · Grey junk 70% · Fish 40% · shiny scales 25% · World table |
| Creek Snapper | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Snapper meat 40% · World table |
| **Kibbler the Candle King** | Coin 48–144c · Guaranteed green (100%) · named drop and quest items as listed in the zone and quest text documents |
| **Old Greymaw** | World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **"Brander" Hale Morrow** | Coin 60–180c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |

## Stonewake Dale — T1, levels 1–5 (Khazrun)

### Stat blocks

| ID | Creature | Level | Type | Health | Damage per swing | Swing | Armor | Mana | Respawn | XP |
|---|---|---|---|---|---|---|---|---|---|---|
| CRE-ST-01 | Highland Buzzard | 1 | Beast (bird) | 42 | 3–4 | 1.8 s | 20 | — | 2.5 min | 50 |
| CRE-ST-02 | Feral Billy | 1–2 | Beast (goat) | 42–57 | 3–5 to 5–7 | 2 s | 48 | — | 2.5 min | 50–55 |
| CRE-ST-03 | Young Shale Bear | 2–3 | Beast | 57–72 | 5–7 to 6–9 | 2 s | 75 | — | 2.5 min | 55–60 |
| CRE-ST-04 | Gravelkin Sinkdweller | 1–2 | Humanoid | 42–57 | 3–5 to 5–7 | 2 s | 48 | — | 2.5 min | 50–55 |
| CRE-ST-05 | Gravelkin Bonechewer | 3 | Humanoid | 72 | 6–9 | 2 s | 75 | — | 2.5 min | 60 |
| CRE-ST-06 | Hop-Blight Beetle | 3–4 | Beast | 72–87 | 6–9 to 8–11 | 2 s | 102 | — | 2.5 min | 60–65 |
| CRE-ST-07 | Shale Bear | 4 | Beast | 87 | 8–11 | 2 s | 102 | — | 2.5 min | 65 |
| CRE-ST-08 | Fermented Ooze | 4–5 | Aberration | 87–102 | 8–11 to 9–13 | 2 s | 130 | — | 2.5 min | 65–70 |
| CRE-ST-09 | Dale Rustler | 4 | Humanoid | 87 | 8–11 | 2 s | 102 | — | 2.5 min | 65 |
| CRE-ST-10 | Rustler's Hound | 4 | Beast | 87 | 8–11 | 2 s | 102 | — | 2.5 min | 65 |
| CRE-ST-11 | Rustler Hound-Master | 5 | Humanoid | 102 | 9–13 | 2 s | 130 | — | 2.5 min | 70 |
| CRE-ST-12 | **Greedy Gund** (Rare) | 4 | Humanoid | 130 | 9–13 | 2 s | 102 | — | 2–8 h | 65 |
| CRE-ST-13 | **Old Bitterhorn** (Elite) | 5 | Beast | 306 | 17–23 | 2 s | 130 | — | 7 min | 140 |
| CRE-ST-14 | **Chief Gnarr** (Mini-boss) | 5 | Humanoid | 204 | 12–16 | 2 s | 130 | — | 5 min | 210 |

### Abilities

| Creature | Ability | Kind | Effect at top level |
|---|---|---|---|
| Highland Buzzard | — | — | Melee only |
| Feral Billy | Headbutt | Strike | 7 Physical; cooldown 8 s |
| Young Shale Bear | Maul | Strike | 10 Physical; cooldown 8 s |
| Gravelkin Sinkdweller | — | — | Melee only |
| Gravelkin Bonechewer | Gnaw | Debuff | armor −10; lasts 15 s; cooldown 20 s |
| Hop-Blight Beetle | Blight Spray | Damage over time | 22 Nature over 12 s (4 ticks); applied on hit, cooldown 15 s; disease |
| Shale Bear | Maul | Strike | 11 Physical; cooldown 8 s |
| Fermented Ooze | Sour Splash | Slow | Slows movement 20% for 6 s; deals 7 Physical; cooldown 12 s |
| Dale Rustler | Lasso | Root | Roots 3 s; range 20 yd; cooldown 20 s |
| Rustler's Hound | Bite | Strike | 11 Physical; cooldown 8 s |
| Rustler Hound-Master | Whistle | Summon | calls allies; once per fight unless a cooldown is given |
| Rustler Hound-Master | Cudgel | Strike | 13 Physical; cooldown 8 s |

### Loot

| Creature | Loot table |
|---|---|
| Highland Buzzard | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps · Buzzard Egg 40% · feathers 25% · World table |
| Feral Billy | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps · Goat Meat 40% · World table |
| Young Shale Bear | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Bear Meat 40% · World table |
| Gravelkin Sinkdweller | Coin 3–18c (100%) · Linen Cloth 35% · Grey junk 70% · Stolen Whetstone 40% · World table |
| Gravelkin Bonechewer | Coin 9–27c (100%) · Linen Cloth 35% · Grey junk 70% · Rough Stone 40% · World table |
| Hop-Blight Beetle | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Blight Gland 40% · shell 25% · World table |
| Shale Bear | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Bear Meat 40% · World table |
| Fermented Ooze | No coin · Slime grey 65% · Copper Fitting 40% · yeast 25% · World table |
| Dale Rustler | Coin 12–36c (100%) · Linen Cloth 35% · Grey junk 70% · Peddler's Coin 40% · World table |
| Rustler's Hound | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Sharp Fang 40% · World table |
| Rustler Hound-Master | Coin 15–45c (100%) · Linen Cloth 35% · Grey junk 70% · Peddler's Coin 40% · World table |
| **Greedy Gund** | Coin 48–144c · Guaranteed green (100%) · named drop and quest items as listed in the zone and quest text documents |
| **Old Bitterhorn** | World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Chief Gnarr** | Coin 60–180c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |

## Embercrag Hollow — T2, levels 5–10 (Khazrun)

### Stat blocks

| ID | Creature | Level | Type | Health | Damage per swing | Swing | Armor | Mana | Respawn | XP |
|---|---|---|---|---|---|---|---|---|---|---|
| CRE-EC-01 | Rime Wolf | 5–6 | Beast | 102–121 | 9–13 to 11–15 | 2 s | 184 | — | 5 min | 70–75 |
| CRE-EC-02 | Crag Ram | 5–6 | Beast | 102–121 | 9–13 to 11–15 | 2 s | 184 | — | 5 min | 70–75 |
| CRE-EC-03 | Tuskfall Boar | 6–7 | Beast | 121–140 | 11–15 to 13–18 | 2 s | 238 | — | 5 min | 75–80 |
| CRE-EC-04 | Gravelkin Scrabbler | 6–7 | Humanoid | 121–140 | 11–15 to 13–18 | 2 s | 238 | — | 5 min | 75–80 |
| CRE-EC-05 | Gravelkin Gnasher | 7–8 | Humanoid | 140–160 | 13–18 to 15–20 | 2 s | 292 | — | 5 min | 80–85 |
| CRE-EC-06 | Slagborn Lookout | 7–8 | Humanoid | 140–160 | 13–18 to 15–20 | 2 s | 292 | — | 5 min | 80–85 |
| CRE-EC-07 | Snowshoe Lynx | 7–8 | Beast | 140–160 | 13–18 to 15–20 | 2 s | 292 | — | 5 min | 80–85 |
| CRE-EC-08 | Slagborn Firebrand | 8 | Humanoid (caster) | 128 | 6–8 | 2 s | 219 | 420 | 5 min | 85 |
| CRE-EC-09 | Gravelkin Rockchucker | 8–9 | Humanoid (ranged) | 160–179 | 15–20 to 17–23 | 2 s | 346 | — | 5 min | 85–90 |
| CRE-EC-10 | Rimewater Sprite | 8–9 | Elemental | 160–179 | 16–22 to 19–25 | 2.2 s | 346 | — | 5 min | 85–90 |
| CRE-EC-11 | Slagborn Sapper | 8–9 | Humanoid | 160–179 | 15–20 to 17–23 | 2 s | 346 | — | 5 min | 85–90 |
| CRE-EC-12 | Loose Slag Sprite | 9 | Elemental | 179 | 19–25 | 2.2 s | 346 | — | 5 min | 90 |
| CRE-EC-13 | Slagborn Powderkeg | 9–10 | Humanoid | 179–198 | 17–23 to 19–25 | 2 s | 400 | — | 5 min | 90–95 |
| CRE-EC-14 | **Whitepelt** (Rare) | 8 | Beast | 239 | 18–24 | 2 s | 292 | — | 2–8 h | 85 |
| CRE-EC-15 | **Grawl the Boulder-Eater** (Elite) | 9 | Humanoid | 536 | 30–41 | 2 s | 346 | — | 7 min | 180 |
| CRE-EC-16 | **Powderkeg Pol** (Elite) | 10 | Humanoid | 594 | 34–46 | 2 s | 400 | — | 7 min | 190 |
| CRE-EC-17 | **Grolm Sootbeard** (Named) | 8 | Humanoid | 239 | 18–24 | 2 s | 292 | — | 5 min | 85 |
| CRE-EC-18 | **Sapper-Chief Dolga Blackmatch** (Chain boss (elite)) | 10 | Humanoid | 990 | 37–51 | 2 s | 400 | — | 5 min | 285 |

### Abilities

| Creature | Ability | Kind | Effect at top level |
|---|---|---|---|
| Rime Wolf | Bite | Strike | 16 Physical; cooldown 8 s |
| Crag Ram | Headbutt | Control | Stun/incapacitate 1 s; deals 13 Physical; cooldown 20 s |
| Tuskfall Boar | Charge | Opener | 22 Physical on the first hit; closes from 8 to 25 yd |
| Gravelkin Scrabbler | Gnaw | Debuff | armor −10; lasts 15 s; cooldown 20 s |
| Gravelkin Gnasher | Gnaw | Debuff | armor −10; lasts 15 s; cooldown 20 s |
| Gravelkin Gnasher | Frenzy at 30% | Buff | Self: +25% damage and +30% attack speed for 10 s; cooldown 30 s |
| Slagborn Lookout | Shoot | Ranged or spell | 20–26 Physical; 2 s cast; range 30 yd |
| Slagborn Lookout | calls allies | Summon | Calls 1 ally of the same family within 30 yd; once per fight unless a cooldown is given |
| Snowshoe Lynx | Pounce | Opener | 27 Physical on the first hit; the creature is hidden until within 8 yd; stealth opener |
| Slagborn Firebrand | Slag Bolt | Ranged or spell | 33–45 Fire; 2 s cast; range 30 yd |
| Slagborn Firebrand | Soot Cloud | Debuff | −10% hit; lasts 15 s; cooldown 20 s |
| Gravelkin Rockchucker | Throw Rock | Ranged or spell | 22–30 Physical; 2 s cast; range 30 yd |
| Rimewater Sprite | Frost Nip | Slow | Slows movement 20% for 6 s; deals 13 Frost; cooldown 12 s |
| Slagborn Sapper | Throw Charge | Ranged or spell | 22–30 Physical; 2 s cast; range 30 yd; aimed at the ground, avoidable |
| Slagborn Sapper | Sunder | Debuff | −10% armor; lasts 15 s; cooldown 20 s |
| Loose Slag Sprite | Slag Spit | Damage over time | 42 Fire over 12 s (4 ticks); applied on hit, cooldown 15 s; Fire DoT |
| Slagborn Powderkeg | Explodes on death | Area attack | 18 Physical to all enemies within 8 yd, on death; 2 s warning; cooldown 12 s; AoE, 3 s warning |

### Loot

| Creature | Loot table |
|---|---|
| Rime Wolf | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Wolf meat 40% · Sharp Fang 25% · World table |
| Crag Ram | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Ram Flank 40% · World table |
| Tuskfall Boar | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Boar Haunch 40% · World table |
| Gravelkin Scrabbler | Coin 18–63c (100%) · Linen Cloth 35% · Grey junk 70% · Rough Stone 40% · World table |
| Gravelkin Gnasher | Coin 21–72c (100%) · Linen Cloth 35% · Grey junk 70% · Rough Stone 40% · World table |
| Slagborn Lookout | Coin 21–72c (100%) · Linen Cloth 35% · Grey junk 70% · Branded Ingot 40% · World table |
| Snowshoe Lynx | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Musk Gland 40% · Big Cat Meat 25% · World table |
| Slagborn Firebrand | Coin 24–72c (100%) · Linen Cloth 35% · Grey junk 70% · Branded Ingot 40% · World table |
| Gravelkin Rockchucker | Coin 24–81c (100%) · Linen Cloth 35% · Grey junk 70% · Rough Stone 40% · World table |
| Rimewater Sprite | No coin · Elemental grey 60% · Rimewater Shard 40% · World table |
| Slagborn Sapper | Coin 24–81c (100%) · Linen Cloth 35% · Grey junk 70% · blasting powder 40% · World table |
| Loose Slag Sprite | No coin · Elemental grey 60% · Small Ember Core 3% · Coal 25% · World table |
| Slagborn Powderkeg | Coin 27–90c (100%) · Linen Cloth 35% · Grey junk 70% · World table |
| **Whitepelt** | Guaranteed green (100%) · named drop and quest items as listed in the zone and quest text documents |
| **Grawl the Boulder-Eater** | Coin 108–324c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Powderkeg Pol** | Coin 120–360c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Grolm Sootbeard** | Coin 96–288c · World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **Sapper-Chief Dolga Blackmatch** | Coin 120–360c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |

## Harrowfield — T2, levels 5–10 (Meridia)

### Stat blocks

| ID | Creature | Level | Type | Health | Damage per swing | Swing | Armor | Mana | Respawn | XP |
|---|---|---|---|---|---|---|---|---|---|---|
| CRE-HF-01 | Harrow Jackal | 5–6 | Beast | 102–121 | 9–13 to 11–15 | 2 s | 184 | — | 5 min | 70–75 |
| CRE-HF-02 | Field Harrier | 5–6 | Beast (bird) | 102–121 | 8–11 to 10–14 | 1.8 s | 184 | — | 5 min | 70–75 |
| CRE-HF-03 | Tusked Rooter | 6–7 | Beast | 121–140 | 11–15 to 13–18 | 2 s | 238 | — | 5 min | 75–80 |
| CRE-HF-04 | Harrow Reaver Thug | 6–7 | Humanoid | 121–140 | 11–15 to 13–18 | 2 s | 238 | — | 5 min | 75–80 |
| CRE-HF-05 | Reaver Poacher | 7–8 | Humanoid (ranged) | 140–160 | 13–18 to 15–20 | 2 s | 292 | — | 5 min | 80–85 |
| CRE-HF-06 | Reaver Firestarter | 8–9 | Humanoid (caster) | 128–143 | 6–8 to 7–9 | 2 s | 260 | 465 | 5 min | 85–90 |
| CRE-HF-07 | Cinderstuffed Scarecrow | 7–8 | Construct | 140–160 | 16–21 to 18–24 | 2.4 s | 292 | — | 5 min | 80–85 |
| CRE-HF-08 | Thresher Construct | 8–9 | Construct | 160–179 | 18–24 to 20–27 | 2.4 s | 346 | — | 5 min | 85–90 |
| CRE-HF-09 | Longstrand Netter | 7–8 | Humanoid (Gillkin) | 140–160 | 13–18 to 15–20 | 2 s | 292 | — | 5 min | 80–85 |
| CRE-HF-10 | Longstrand Tidecaller | 9 | Humanoid (caster) | 143 | 7–9 | 2 s | 260 | 465 | 5 min | 90 |
| CRE-HF-11 | Quarry Burrowkin Sapper | 8–9 | Humanoid | 160–179 | 15–20 to 17–23 | 2 s | 346 | — | 5 min | 85–90 |
| CRE-HF-12 | Quarry Skink | 9–10 | Beast | 179–198 | 17–23 to 19–25 | 2 s | 400 | — | 5 min | 90–95 |
| CRE-HF-13 | Vane Houseguard | 9–10 | Humanoid | 179–198 | 17–23 to 19–25 | 2 s | 400 | — | 5 min | 90–95 |
| CRE-HF-14 | **Mudtusk** (Rare) | 8 | Beast | 239 | 18–24 | 2 s | 292 | — | 2–8 h | 85 |
| CRE-HF-15 | **Old Rattlebones, the Scarecrow King** (Elite) | 9 | Construct | 536 | 36–49 | 2.4 s | 346 | — | 7 min | 180 |
| CRE-HF-16 | **Captain "Sweet" Sal Marrow** (Elite) | 10 | Humanoid | 594 | 34–46 | 2 s | 400 | — | 7 min | 190 |
| CRE-HF-17 | **Marshal Edrik Vane** (Chain boss (elite)) | 10 | Humanoid | 990 | 37–51 | 2 s | 400 | — | 5 min | 285 |
| CRE-HF-18 | **P** (Named) | a | y | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 530 |
| CRE-HF-19 | **8** (Named) |  |  | 40 | 2–3 | 2 s | -8 | — | 5 min | 45 |
| CRE-HF-20 | **H** (Named) | u | m | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 630 |
| CRE-HF-21 | **n** (Named) | a | m | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 530 |

### Abilities

| Creature | Ability | Kind | Effect at top level |
|---|---|---|---|
| Harrow Jackal | Pack Howl | Buff | Allies within 15 yd: +25% damage for 10 s; triggers at 10% health |
| Field Harrier | Swoop | Opener | 18 Physical on the first hit; closes from 8 to 25 yd |
| Tusked Rooter | Charge | Opener | 22 Physical on the first hit; closes from 8 to 25 yd |
| Tusked Rooter | Gore | Damage over time | 34 Physical over 12 s (4 ticks); applied on hit, cooldown 15 s; bleed |
| Harrow Reaver Thug | Cheap Shot | Control | Stun/incapacitate 2 s; deals 15 Physical; cooldown 20 s |
| Reaver Poacher | Shoot | Ranged or spell | 20–26 Physical; 2 s cast; range 30 yd |
| Reaver Poacher | Trap | Root | Roots 4 s; range 20 yd; cooldown 20 s |
| Reaver Firestarter | Firebrand | Damage over time | 42 Fire over 12 s (4 ticks); applied on hit, cooldown 15 s; Fire bolt |
| Reaver Firestarter | Ignite Ground | Strike | 24 Physical; cooldown 8 s |
| Cinderstuffed Scarecrow | Flail | Area attack | 17 Physical to all enemies within 5 yd; cooldown 12 s; 2 targets |
| Cinderstuffed Scarecrow | Fire vulnerability | Trait | Fire vulnerability |
| Thresher Construct | Whirling Blades | Area attack | 19 Physical to all enemies within 5 yd; 2 s warning; cooldown 12 s; AoE, telegraphed |
| Longstrand Netter | Net | Root | Roots 3 s; range 20 yd; cooldown 20 s |
| Longstrand Tidecaller | Water Bolt | Ranged or spell | 37–51 Nature; 2 s cast; range 30 yd |
| Longstrand Tidecaller | Healing Tide | Heal | Heals 17 (12% of max health); 2.0 s cast, interruptible; cooldown 20 s; used below 50% health |
| Quarry Burrowkin Sapper | Throw Dynamite | Ranged or spell | 22–30 Physical; 2 s cast; range 30 yd; aimed at the ground, avoidable |
| Quarry Skink | Stone Gaze | Control | Stun/incapacitate 2 s; deals 22 Physical; 2.0 s cast, avoid by facing away or interrupting; cooldown 20 s |
| Vane Houseguard | Shield Bash | Defensive | −50% damage taken; lasts 6 s unless stated; cooldown 30 s |
| Vane Houseguard | Defensive Stance | Defensive | −50% damage taken; lasts 6 s unless stated; cooldown 30 s |

### Loot

| Creature | Loot table |
|---|---|
| Harrow Jackal | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · World table |
| Field Harrier | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Harrier Egg 40% · feathers 25% · World table |
| Tusked Rooter | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Rooter Flank 40% · World table |
| Harrow Reaver Thug | Coin 18–63c (100%) · Linen Cloth 35% · Grey junk 70% · World table |
| Reaver Poacher | Coin 21–72c (100%) · Linen Cloth 35% · Grey junk 70% · Poached Goods 40% · World table |
| Reaver Firestarter | Coin 24–81c (100%) · Linen Cloth 35% · Grey junk 70% · World table |
| Cinderstuffed Scarecrow | No coin · Scrap grey 65% · Smoldering Cinder-Heart 40% · straw 25% · World table |
| Thresher Construct | No coin · Scrap grey 65% · Copper Bolts 40% · gears 25% · World table |
| Longstrand Netter | Coin 21–72c (100%) · Linen Cloth 35% · Grey junk 70% · Fish 40% · World table |
| Longstrand Tidecaller | Coin 27–81c (100%) · Linen Cloth 35% · Grey junk 70% · River Pearl 3% · Widow's Locket 25% · World table |
| Quarry Burrowkin Sapper | Coin 24–81c (100%) · Linen Cloth 35% · Grey junk 70% · Blasting powder 40% · Tin Ore 25% · World table |
| Quarry Skink | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Skink Eye 40% · World table |
| Vane Houseguard | Coin 27–90c (100%) · Linen Cloth 35% · Grey junk 70% · World table |
| **Mudtusk** | Guaranteed green (100%) · named drop and quest items as listed in the zone and quest text documents |
| **Old Rattlebones, the Scarecrow King** | World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Captain "Sweet" Sal Marrow** | Coin 120–360c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Marshal Edrik Vane** | Coin 120–360c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **P** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **8** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **H** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **n** | World green 2% · named drop and quest items as listed in the zone and quest text documents |

## Russetwood — T2, levels 5–10 (Meridia)

### Stat blocks

| ID | Creature | Level | Type | Health | Damage per swing | Swing | Armor | Mana | Respawn | XP |
|---|---|---|---|---|---|---|---|---|---|---|
| CRE-RW-01 | Russet Fox | 5–6 | Beast | 102–121 | 9–13 to 11–15 | 2 s | 184 | — | 5 min | 70–75 |
| CRE-RW-02 | Rutting Stag | 5–6 | Beast | 102–121 | 9–13 to 11–15 | 2 s | 184 | — | 5 min | 70–75 |
| CRE-RW-03 | Leafmold Beetle | 6–7 | Beast | 121–140 | 11–15 to 13–18 | 2 s | 238 | — | 5 min | 75–80 |
| CRE-RW-04 | Woodland Poacher | 6–7 | Humanoid | 121–140 | 11–15 to 13–18 | 2 s | 238 | — | 5 min | 75–80 |
| CRE-RW-05 | Poacher Trapper | 7–8 | Humanoid | 140–160 | 13–18 to 15–20 | 2 s | 292 | — | 5 min | 80–85 |
| CRE-RW-06 | Canopy Weaver | 7–8 | Beast (spider) | 140–160 | 12–16 to 13–18 | 1.8 s | 292 | — | 5 min | 80–85 |
| CRE-RW-07 | Ashhand Charcoaler | 7–8 | Humanoid | 140–160 | 13–18 to 15–20 | 2 s | 292 | — | 5 min | 80–85 |
| CRE-RW-08 | Burrowkin Rootgnawer | 8 | Humanoid | 160 | 15–20 | 2 s | 292 | — | 5 min | 85 |
| CRE-RW-09 | Mossback Treant | 8–9 | Plant | 160–179 | 18–24 to 20–27 | 2.4 s | 346 | — | 5 min | 85–90 |
| CRE-RW-10 | Kiln Tender | 8–9 | Humanoid (caster) | 128–143 | 6–8 to 7–9 | 2 s | 260 | 465 | 5 min | 85–90 |
| CRE-RW-11 | Horned Owl | 8–9 | Beast (bird) | 160–179 | 13–18 to 15–20 | 1.8 s | 346 | — | 5 min | 85–90 |
| CRE-RW-12 | Kilnfire Wisp | 9 | Elemental | 179 | 19–25 | 2.2 s | 346 | — | 5 min | 90 |
| CRE-RW-13 | Russet Bear | 9–10 | Beast | 179–198 | 17–23 to 19–25 | 2 s | 400 | — | 5 min | 90–95 |
| CRE-RW-14 | Great Kiln Guard | 9–10 | Humanoid | 179–198 | 17–23 to 19–25 | 2 s | 400 | — | 5 min | 90–95 |
| CRE-RW-15 | **Red Tom** (Rare) | 7 | Beast | 211 | 16–21 | 2 s | 238 | — | 2–8 h | 80 |
| CRE-RW-16 | **Old Mossback** (Elite) | 9 | Plant | 536 | 36–49 | 2.4 s | 346 | — | 7 min | 180 |
| CRE-RW-17 | **Garrick Snare, the Poacher-King** (Elite) | 10 | Humanoid | 594 | 34–46 | 2 s | 400 | — | 7 min | 190 |
| CRE-RW-18 | **Kilnmaster Bertram Soot** (Chain boss (elite)) | 10 | Humanoid | 990 | 37–51 | 2 s | 400 | — | 5 min | 285 |
| CRE-RW-19 | **O** (Named) | d | o | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 545 |
| CRE-RW-20 | **8** (Named) |  |  | 40 | 2–3 | 2 s | -8 | — | 5 min | 45 |
| CRE-RW-21 | **H** (Named) | u | m | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 630 |
| CRE-RW-22 | **n** (Named) | a | m | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 530 |

### Abilities

| Creature | Ability | Kind | Effect at top level |
|---|---|---|---|
| Russet Fox | Nip | Slow | Slows movement 40% for 6 s; deals 8 Physical; cooldown 12 s |
| Russet Fox | Dash | Opener | 20 Physical on the first hit; closes from 8 to 25 yd |
| Rutting Stag | Antler Charge | Opener | 20 Physical on the first hit; closes from 8 to 25 yd; knockback |
| Leafmold Beetle | Acid Spit | Ranged or spell | 17–23 Nature; 2 s cast; range 30 yd |
| Woodland Poacher | Shoot | Ranged or spell | 17–23 Physical; 2 s cast; range 30 yd |
| Woodland Poacher | Skinning Knife | Damage over time | 34 Physical over 12 s (4 ticks); applied on hit, cooldown 15 s; bleed |
| Poacher Trapper | Snare | Root | Roots 4 s; range 20 yd; cooldown 20 s |
| Poacher Trapper | Net | Root | Roots 3 s; range 20 yd; cooldown 20 s |
| Canopy Weaver | Web Drop | Root | Roots 3 s; range 20 yd; cooldown 20 s |
| Canopy Weaver | Venom | Damage over time | 38 Nature over 12 s (4 ticks); applied on hit, cooldown 15 s |
| Ashhand Charcoaler | Shovel Bash | Strike | 22 Physical; cooldown 8 s |
| Ashhand Charcoaler | Throw Embers | Ranged or spell | 20–26 Fire; 2 s cast; range 30 yd |
| Burrowkin Rootgnawer | Gnaw | Debuff | −10% armor; lasts 15 s; cooldown 20 s |
| Burrowkin Rootgnawer | Undermine | Control | Stun/incapacitate 1 s; deals 18 Physical; cooldown 20 s |
| Mossback Treant | Root Slam | Root | Roots 3 s; range 20 yd; cooldown 20 s |
| Mossback Treant | Bark Skin | Defensive | −50% damage taken; lasts 6 s unless stated; cooldown 30 s |
| Mossback Treant | resists Nature 50% | Trait | resists Nature 50% |
| Mossback Treant | weak to Fire | Trait | weak to Fire |
| Kiln Tender | Kilnfire Bolt | Ranged or spell | 37–51 Fire; 2 s cast; range 30 yd |
| Kiln Tender | Stoke | Buff | Allies within 15 yd: +25% damage and +30% attack speed for 10 s; cooldown 30 s |
| Horned Owl | Silent Dive | Opener | 27 Physical on the first hit; the creature is hidden until within 8 yd; stealth opener |
| Horned Owl | Screech | Silence | Silences or interrupts for 3 s; range 20 yd; cooldown 25 s |
| Kilnfire Wisp | Flicker | Movement | blink; cooldown 15 s |
| Kilnfire Wisp | Scorch | Strike | 26 Physical; cooldown 8 s |
| Russet Bear | Maul | Strike | 26 Physical; cooldown 8 s |
| Russet Bear | Swipe | Area attack | 18 Physical to all enemies within 5 yd; cooldown 12 s |
| Great Kiln Guard | Shield Bash | Defensive | −50% damage taken; lasts 6 s unless stated; cooldown 30 s |
| Great Kiln Guard | Hold Fast | Defensive | −50% damage taken; lasts 6 s unless stated; cooldown 30 s |

### Loot

| Creature | Loot table |
|---|---|
| Russet Fox | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · fox tail 40% · World table |
| Rutting Stag | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Venison 40% · World table |
| Leafmold Beetle | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Beetle shell 40% · chanterelles 25% · World table |
| Woodland Poacher | Coin 18–63c (100%) · Linen Cloth 35% · Grey junk 70% · stolen pelts 40% · World table |
| Poacher Trapper | Coin 21–72c (100%) · Linen Cloth 35% · Grey junk 70% · Poachers' Tally quest rate · World table |
| Canopy Weaver | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Small Venom Sac 40% · World table |
| Ashhand Charcoaler | Coin 21–72c (100%) · Linen Cloth 35% · Grey junk 70% · Cinder-Charcoal 40% · World table |
| Burrowkin Rootgnawer | Coin 24–72c (100%) · Linen Cloth 35% · Grey junk 70% · Tin Ore 40% · Woodcutter's Axe quest rate · World table |
| Mossback Treant | No coin · Plant grey 65% · Herbalism on corpse where the zone doc says so · Heartknot 40% · Dewleaf 25% · World table |
| Kiln Tender | Coin 24–81c (100%) · Linen Cloth 35% · Grey junk 70% · World table |
| Horned Owl | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Owl Pellet 40% · feathers 25% · World table |
| Kilnfire Wisp | No coin · Elemental grey 60% · Small Ember Core 3% · World table |
| Russet Bear | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Bear Meat 40% · World table |
| Great Kiln Guard | Coin 27–90c (100%) · Linen Cloth 35% · Grey junk 70% · World table |
| **Red Tom** | Guaranteed green (100%) · named drop and quest items as listed in the zone and quest text documents |
| **Old Mossback** | World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Garrick Snare, the Poacher-King** | Coin 120–360c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Kilnmaster Bertram Soot** | Coin 120–360c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **O** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **8** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **H** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **n** | World green 2% · named drop and quest items as listed in the zone and quest text documents |

## Stoneheart Deeps — T2, levels 5–10 (Khazrun, inside the mountain)

### Stat blocks

| ID | Creature | Level | Type | Health | Damage per swing | Swing | Armor | Mana | Respawn | XP |
|---|---|---|---|---|---|---|---|---|---|---|
| CRE-SD-01 | Lanternwing Bat | 5–6 | Beast | 102–121 | 9–13 to 11–15 | 2 s | 184 | — | 5 min | 70–75 |
| CRE-SD-02 | Rail Rat | 5–6 | Beast | 102–121 | 9–13 to 11–15 | 2 s | 184 | — | 5 min | 70–75 |
| CRE-SD-03 | Glowcap Shambler | 5–6 | Plant | 102–121 | 11–15 to 13–18 | 2.4 s | 184 | — | 5 min | 70–75 |
| CRE-SD-04 | Pale Cave Bear | 6–7 | Beast | 121–140 | 11–15 to 13–18 | 2 s | 238 | — | 5 min | 75–80 |
| CRE-SD-05 | Gravelkin Underdweller | 6–7 | Humanoid | 121–140 | 11–15 to 13–18 | 2 s | 238 | — | 5 min | 75–80 |
| CRE-SD-06 | Gravelkin Shardchewer | 7–8 | Humanoid | 140–160 | 13–18 to 15–20 | 2 s | 292 | — | 5 min | 80–85 |
| CRE-SD-07 | Crystal Skitterer | 7–8 | Beast (spider) | 140–160 | 12–16 to 13–18 | 1.8 s | 292 | — | 5 min | 80–85 |
| CRE-SD-08 | Restless Ancestor | 8–9 | Undead | 160–179 | 15–20 to 17–23 | 2 s | 346 | — | 5 min | 85–90 |
| CRE-SD-09 | Rogue Rail-Golem | 8–9 | Construct | 160–179 | 18–24 to 20–27 | 2.4 s | 346 | — | 5 min | 85–90 |
| CRE-SD-10 | Rock Borer | 8–9 | Beast (worm) | 160–179 | 15–20 to 17–23 | 2 s | 346 | — | 5 min | 85–90 |
| CRE-SD-11 | Slagborn Tunneler | 8–9 | Humanoid | 160–179 | 15–20 to 17–23 | 2 s | 346 | — | 5 min | 85–90 |
| CRE-SD-12 | Geode Sprite | 9 | Elemental | 179 | 19–25 | 2.2 s | 346 | — | 5 min | 90 |
| CRE-SD-13 | Slagborn Blastwright | 9–10 | Humanoid (caster) | 143–158 | 7–9 to 7–10 | 2 s | 300 | 510 | 5 min | 90–95 |
| CRE-SD-14 | **Glimmerqueen** (Rare) | 8 | Beast | 239 | 18–24 | 2 s | 292 | — | 2–8 h | 85 |
| CRE-SD-15 | **Old Blindmaw** (Elite) | 9 | Beast | 536 | 30–41 | 2 s | 346 | — | 7 min | 180 |
| CRE-SD-16 | **Fusewright Odd** (Elite) | 10 | Humanoid | 594 | 34–46 | 2 s | 400 | — | 7 min | 190 |
| CRE-SD-17 | **Bore-Captain Vigga Deepdrill** (Chain boss (elite)) | 10 | Humanoid | 990 | 37–51 | 2 s | 400 | — | 5 min | 285 |
| CRE-SD-18 | **S** (Named) | h | a | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 565 |
| CRE-SD-19 | **8** (Named) |  |  | 40 | 2–3 | 2 s | -8 | — | 5 min | 45 |
| CRE-SD-20 | **H** (Named) | u | m | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 630 |
| CRE-SD-21 | **n** (Named) | a | m | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 530 |

### Abilities

| Creature | Ability | Kind | Effect at top level |
|---|---|---|---|
| Lanternwing Bat | Sonic Chirp | Silence | Silences or interrupts for 3 s; range 20 yd; cooldown 25 s |
| Lanternwing Bat | Swoop | Opener | 20 Physical on the first hit; closes from 8 to 25 yd |
| Rail Rat | Gnaw | Debuff | −10% armor; lasts 15 s; cooldown 20 s |
| Rail Rat | swarms of 2 | Strike | 16 Physical; cooldown 8 s |
| Glowcap Shambler | Spore Puff | Debuff | −10% hit; lasts 15 s; cooldown 20 s |
| Glowcap Shambler | resists Nature 50% | Trait | resists Nature 50% |
| Pale Cave Bear | Maul | Strike | 18 Physical; cooldown 8 s |
| Pale Cave Bear | Blind Rage | Strike | 18 Physical; cooldown 8 s; ignores taunts briefly |
| Gravelkin Underdweller | Gnaw | Debuff | −10% armor; lasts 15 s; cooldown 20 s |
| Gravelkin Shardchewer | Crystal Spit | Ranged or spell | 20–26 Arcane; 2 s cast; range 30 yd |
| Gravelkin Shardchewer | Frenzy at 30% | Buff | Self: +25% damage and +30% attack speed for 10 s; cooldown 30 s |
| Crystal Skitterer | Refract | Defensive | reflects first spell; lasts 6 s unless stated; cooldown 30 s |
| Crystal Skitterer | Venom | Damage over time | 38 Nature over 12 s (4 ticks); applied on hit, cooldown 15 s |
| Restless Ancestor | Ancestral Hammer | Strike | 24 Physical; cooldown 8 s |
| Restless Ancestor | Reproach | Silence | Silences or interrupts for 2 s; range 20 yd; cooldown 25 s |
| Rogue Rail-Golem | Rail Charge | Opener | 36 Physical on the first hit; closes from 8 to 25 yd; line attack, telegraphed |
| Rogue Rail-Golem | immune to bleed/poison | Trait | immune to bleed/poison |
| Rock Borer | Burrow ambush | Opener | 30 Physical on the first hit; the creature is hidden until within 8 yd |
| Rock Borer | Acid Bite | Strike | 24 Physical; cooldown 8 s |
| Slagborn Tunneler | Throw Charge | Ranged or spell | 22–30 Physical; 2 s cast; range 30 yd; aimed at the ground, avoidable |
| Slagborn Tunneler | Pick Sunder | Debuff | −10% armor; lasts 15 s; cooldown 20 s |
| Geode Sprite | Shard Volley | Ranged or spell | 22–30 Arcane; 2 s cast; range 30 yd; hits all targets in the area |
| Geode Sprite | resists Arcane 50% | Trait | resists Arcane 50% |
| Slagborn Blastwright | Slag Bolt | Ranged or spell | 41–55 Fire; 2 s cast; range 30 yd |
| Slagborn Blastwright | Lay Charge | Opener | 33 Physical on the first hit; closes from 8 to 25 yd; ground bomb, 3 s fuse |

### Loot

| Creature | Loot table |
|---|---|
| Lanternwing Bat | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Bat wing 40% · lamp-oil 25% · World table |
| Rail Rat | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Rat tail 40% · World table |
| Glowcap Shambler | No coin · Plant grey 65% · Herbalism on corpse where the zone doc says so · Glowcap 40% · Dewleaf 25% · World table |
| Pale Cave Bear | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Bear Meat 40% · World table |
| Gravelkin Underdweller | Coin 18–63c (100%) · Linen Cloth 35% · Grey junk 70% · Rough Stone 40% · World table |
| Gravelkin Shardchewer | Coin 21–72c (100%) · Linen Cloth 35% · Grey junk 70% · crystal shards 40% · World table |
| Crystal Skitterer | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Small Venom Sac 40% · crystal leg 25% · World table |
| Restless Ancestor | Coin 12–40c (60%) · Linen Cloth 25% · Grey junk 70% · old coins 40% · World table |
| Rogue Rail-Golem | No coin · Scrap grey 65% · Copper Bolts 40% · Control-Rune 25% · World table |
| Rock Borer | No coin · Grey junk 75% · Skinning: Ruined Leather Scraps or Light Leather · Borer Tooth 40% · World table |
| Slagborn Tunneler | Coin 24–81c (100%) · Linen Cloth 35% · Grey junk 70% · blasting powder 40% · World table |
| Geode Sprite | No coin · Elemental grey 60% · Tigerseye/Malachite 3% · Coarse Stone 25% · World table |
| Slagborn Blastwright | Coin 27–90c (100%) · Linen Cloth 35% · Grey junk 70% · World table |
| **Glimmerqueen** | Guaranteed green (100%) · named drop and quest items as listed in the zone and quest text documents |
| **Old Blindmaw** | World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Fusewright Odd** | Coin 120–360c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Bore-Captain Vigga Deepdrill** | Coin 120–360c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **S** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **8** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **H** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **n** | World green 2% · named drop and quest items as listed in the zone and quest text documents |

## Ironroot Highlands — T3, levels 10–20 (Khazrun)

### Stat blocks

| ID | Creature | Level | Type | Health | Damage per swing | Swing | Armor | Mana | Respawn | XP |
|---|---|---|---|---|---|---|---|---|---|---|
| CRE-IR-01 | Ironhorn Ram | 10–11 | Beast | 198–224 | 19–25 to 21–28 | 2 s | 472 | — | 5 min | 95–100 |
| CRE-IR-02 | Crag Stalker | 11–12 | Beast (cat) | 224–250 | 19–25 to 21–28 | 1.8 s | 544 | — | 5 min | 100–105 |
| CRE-IR-03 | Ironroot Bear | 12–13 | Beast | 250–276 | 23–31 to 25–34 | 2 s | 616 | — | 5 min | 105–110 |
| CRE-IR-04 | Gravelkin Deepdelver | 12–13 | Humanoid | 250–276 | 23–31 to 25–34 | 2 s | 616 | — | 5 min | 105–110 |
| CRE-IR-05 | Stonemaw Brute | 13–14 | Giant (ogre) | 276–302 | 32–44 to 35–47 | 2.6 s | 688 | — | 5 min | 110–115 |
| CRE-IR-06 | Stonemaw Hexer | 14–15 | Giant (caster) | 242–262 | 14–19 to 15–20 | 2.6 s | 570 | 735 | 5 min | 115–120 |
| CRE-IR-07 | Tunnel Lurker | 13–14 | Beast (spider) | 276–302 | 22–30 to 24–33 | 1.8 s | 688 | — | 5 min | 110–115 |
| CRE-IR-08 | Slagborn Smuggler | 14–15 | Humanoid | 302–328 | 27–36 to 29–39 | 2 s | 760 | — | 5 min | 115–120 |
| CRE-IR-09 | Slagborn Runesmith | 15–16 | Humanoid (caster) | 262–287 | 12–16 to 13–17 | 2 s | 606 | 780 | 5 min | 120–125 |
| CRE-IR-10 | Peak Screecher | 16–17 | Humanoid (harpy) | 359–390 | 28–38 to 30–41 | 1.8 s | 856 | — | 5 min | 125–130 |
| CRE-IR-11 | Hollowed Miner | 16–17 | Humanoid (Hollowed) | 359–390 | 31–42 to 34–46 | 2 s | 856 | — | 5 min | 125–130 |
| CRE-IR-12 | Ore-Bound Elemental | 17–18 | Elemental | 390–422 | 37–50 to 40–54 | 2.2 s | 904 | — | 5 min | 130–135 |
| CRE-IR-13 | Rimewing Whelp | 18–19 | Dragonkin | 422–453 | 36–49 to 38–52 | 2 s | 952 | — | 5 min | 135–140 |
| CRE-IR-14 | Brandforge Guard | 19–20 | Humanoid | 453–484 | 38–52 to 41–55 | 2 s | 1000 | — | 5 min | 140–145 |
| CRE-IR-15 | Brandforge Slagcaster | 19–20 | Humanoid (caster) | 362–387 | 15–21 to 16–22 | 2 s | 750 | 960 | 5 min | 140–145 |
| CRE-IR-16 | **Old Ironhide** (Elite) | 13 | Beast | 828 | 45–60 | 2 s | 616 | — | 7 min | 220 |
| CRE-IR-17 | **Gnawbone** (Rare) | 14 | Beast | 453 | 32–44 | 2 s | 688 | — | 2–8 h | 115 |
| CRE-IR-18 | **Stonemaw Crusher Gorm** (Elite) | 16 | Giant | 1078 | 73–99 | 2.6 s | 808 | — | 7 min | 250 |
| CRE-IR-19 | **Shriekmother Kaa** (Elite) | 17 | Humanoid | 1171 | 61–82 | 2 s | 856 | — | 7 min | 260 |
| CRE-IR-20 | **Hollowed Foreman Brokk** (Elite) | 18 | Humanoid | 1265 | 65–88 | 2 s | 904 | — | 7 min | 270 |
| CRE-IR-21 | **The Deepseam Horror** (Elite) | 19 | Aberration | 1358 | 69–94 | 2 s | 952 | — | 7 min | 280 |
| CRE-IR-22 | **Warlord Urgoth Stonemaw** (Chain boss (elite)) | 15 | Giant | 1640 | 75–102 | 2.6 s | 760 | — | 5 min | 360 |
| CRE-IR-23 | **Runemaster Hedda Cinderlock** (Chain boss (elite)) | 20 | Humanoid | 2420 | 82–110 | 2 s | 1000 | — | 5 min | 435 |
| CRE-IR-24 | **R** (Named) | u | n | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 630 |
| CRE-IR-25 | **15** (Named) |  |  | 40 | 2–3 | 2 s | -8 | — | 5 min | 45 |
| CRE-IR-26 | **H** (Named) | u | m | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 630 |
| CRE-IR-27 | **n** (Named) | a | m | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 530 |

### Abilities

| Creature | Ability | Kind | Effect at top level |
|---|---|---|---|
| Ironhorn Ram | Headbutt | Control | Stun/incapacitate 2 s; deals 24 Physical; cooldown 20 s |
| Crag Stalker | Pounce | Opener | 36 Physical on the first hit; closes from 8 to 25 yd |
| Crag Stalker | Rake | Damage over time | 54 Physical over 12 s (4 ticks); applied on hit, cooldown 15 s; bleed |
| Ironroot Bear | Maul | Strike | 35 Physical; cooldown 8 s |
| Ironroot Bear | Enrage at 25% | Buff | Self: +25% damage and +30% attack speed for 10 s; cooldown 30 s |
| Gravelkin Deepdelver | Gnaw | Debuff | −10% armor; lasts 15 s; cooldown 20 s |
| Gravelkin Deepdelver | Rock Shell | Defensive | −50% damage taken; lasts 6 s unless stated; cooldown 30 s |
| Stonemaw Brute | Smash | Control | Stun/incapacitate 2 s; deals 41 Physical; cooldown 20 s |
| Stonemaw Hexer | Hex | Debuff | curse: −15% attack speed; lasts 15 s; cooldown 20 s |
| Stonemaw Hexer | Lightning Bolt | Ranged or spell | 64–86 Nature; 2 s cast; range 30 yd |
| Stonemaw Hexer | Bloodlust on allies | Buff | Allies within 15 yd: +25% damage for 10 s; cooldown 30 s |
| Tunnel Lurker | Web | Root | Roots 3 s; range 20 yd; cooldown 20 s |
| Tunnel Lurker | Paralytic Bite | Strike | 34 Physical; cooldown 8 s; −20% speed |
| Slagborn Smuggler | Gouge | Control | Stun/incapacitate 3 s; deals 34 Physical; cooldown 20 s |
| Slagborn Smuggler | Throw Net | Root | Roots 3 s; range 20 yd; cooldown 20 s |
| Slagborn Runesmith | Rune of Fire | Root | Roots 3 s; range 20 yd; cooldown 20 s |
| Slagborn Runesmith | Slag Bolt | Ranged or spell | 69–93 Fire; 2 s cast; range 30 yd |
| Peak Screecher | Screech | Silence | Silences or interrupts for 3 s; range 20 yd; cooldown 25 s |
| Peak Screecher | Dive | Opener | 54 Physical on the first hit; closes from 8 to 25 yd |
| Hollowed Miner | Pick Swing | Strike | 48 Physical; cooldown 8 s |
| Hollowed Miner | Empty Stare | Debuff | −10% armor; lasts 15 s; cooldown 20 s |
| Ore-Bound Elemental | Stone Fist | Strike | 56 Physical; cooldown 8 s |
| Ore-Bound Elemental | Shatter | Area attack | 38 Physical to all enemies within 8 yd, on death; cooldown 12 s; AoE at death |
| Ore-Bound Elemental | resists Arcane 50% | Trait | resists Arcane 50% |
| Rimewing Whelp | Frost Breath | Slow | Slows movement 40% for 6 s; deals 27 Frost; cooldown 12 s |
| Brandforge Guard | Shield Slam | Area attack | 38 Physical to all enemies within 5 yd; cooldown 12 s |
| Brandforge Guard | Hold the Line | Defensive | +armor aura; lasts 6 s unless stated; cooldown 30 s |
| Brandforge Slagcaster | Slag Wave | Ranged or spell | 90–122 Fire; 2 s cast; range 30 yd; hits all targets in the area |
| Brandforge Slagcaster | Molten Armor | Debuff | −10% armor; lasts 15 s; cooldown 20 s |

### Loot

| Creature | Loot table |
|---|---|
| Ironhorn Ram | No coin · Grey junk 75% · Skinning: Light Leather (Light Hide 10%) · Ram Flank 40% · World table |
| Crag Stalker | No coin · Grey junk 75% · Skinning: Light Leather (Light Hide 10%) · Big Cat Meat 40% · World table |
| Ironroot Bear | No coin · Grey junk 75% · Skinning: Light Leather (Light Hide 10%) · Bear Meat 40% · Claws 25% · World table |
| Gravelkin Deepdelver | Coin 36–117c (100%) · Linen Cloth 20%, Wool Cloth 20% · Grey junk 70% · Coarse Stone 40% · Tin Ore 25% · World table |
| Stonemaw Brute | Coin 39–126c (100%) · Linen Cloth 20%, Wool Cloth 20% · Grey junk 70% · Branded Warhammer 40% · World table |
| Stonemaw Hexer | Coin 42–135c (100%) · Wool Cloth 35% · Grey junk 70% · hex-fetishes 40% · World table |
| Tunnel Lurker | No coin · Grey junk 75% · Skinning: Light Leather (Light Hide 10%) · Lurker Silk Gland 40% · Venom Sac 25% · World table |
| Slagborn Smuggler | Coin 42–135c (100%) · Wool Cloth 35% · Grey junk 70% · Bronze 40% · World table |
| Slagborn Runesmith | Coin 45–144c (100%) · Wool Cloth 35% · Grey junk 70% · Rune-Plate 40% · World table |
| Peak Screecher | Coin 48–153c (100%) · Wool Cloth 35% · Grey junk 70% · Screecher Feather 40% · World table |
| Hollowed Miner | Coin 48–153c (100%) · Wool Cloth 35% · Grey junk 70% · Iron Ore 40% · World table |
| Ore-Bound Elemental | No coin · Elemental grey 60% · Ore-Bound Core 40% · Iron Ore 25% · Heavy Stone 25% · World table |
| Rimewing Whelp | No coin · Grey junk 75% · Skinning: Medium Leather (Medium Hide 10%) · Rimewing Scale 40% · World table |
| Brandforge Guard | Coin 57–180c (100%) · Wool Cloth 35% · Grey junk 70% · Steel scraps 40% · World table |
| Brandforge Slagcaster | Coin 57–180c (100%) · Wool Cloth 35% · Grey junk 70% · Small Ember Core 40% · World table |
| **Old Ironhide** | World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Gnawbone** | Guaranteed green (100%) · named drop and quest items as listed in the zone and quest text documents |
| **Stonemaw Crusher Gorm** | Coin 192–576c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Shriekmother Kaa** | Coin 204–612c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Hollowed Foreman Brokk** | Coin 216–648c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **The Deepseam Horror** | World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Warlord Urgoth Stonemaw** | Coin 180–540c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Runemaster Hedda Cinderlock** | Coin 240–720c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **R** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **15** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **H** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **n** | World green 2% · named drop and quest items as listed in the zone and quest text documents |

## Thornwick Marches — T3, levels 10–20 (Meridia)

### Stat blocks

| ID | Creature | Level | Type | Health | Damage per swing | Swing | Armor | Mana | Respawn | XP |
|---|---|---|---|---|---|---|---|---|---|---|
| CRE-TM-01 | Briarwood Stalker | 10–11 | Beast (wolf) | 198–224 | 19–25 to 21–28 | 2 s | 472 | — | 5 min | 95–100 |
| CRE-TM-02 | Thornback Boar | 11–12 | Beast | 224–250 | 21–28 to 23–31 | 2 s | 544 | — | 5 min | 100–105 |
| CRE-TM-03 | Briar Widow | 12–13 | Beast (spider) | 250–276 | 21–28 to 22–30 | 1.8 s | 616 | — | 5 min | 105–110 |
| CRE-TM-04 | Graverobber | 11–12 | Humanoid | 224–250 | 21–28 to 23–31 | 2 s | 544 | — | 5 min | 100–105 |
| CRE-TM-05 | Restless Bones | 12–13 | Undead | 250–276 | 23–31 to 25–34 | 2 s | 616 | — | 5 min | 105–110 |
| CRE-TM-06 | Cinderbrand Acolyte | 12–13 | Humanoid (caster) | 200–221 | 9–12 to 10–13 | 2 s | 462 | 645 | 5 min | 105–110 |
| CRE-TM-07 | Cinderwight | 13–14 | Undead | 276–302 | 25–34 to 27–36 | 2 s | 688 | — | 5 min | 110–115 |
| CRE-TM-08 | Fen Lurker | 14–15 | Beast (mirejaw) | 302–328 | 27–36 to 29–39 | 2 s | 760 | — | 5 min | 115–120 |
| CRE-TM-09 | Bog Shambler | 14–15 | Plant | 302–328 | 32–44 to 35–47 | 2.4 s | 760 | — | 5 min | 115–120 |
| CRE-TM-10 | Pactwatch Scout | 15–16 | Humanoid (elf, ranged) | 328–359 | 29–39 to 31–42 | 2 s | 808 | — | 5 min | 120–125 |
| CRE-TM-11 | Pactwatch Thornspeaker | 16–17 | Humanoid (caster) | 287–312 | 13–17 to 13–18 | 2 s | 642 | 825 | 5 min | 125–130 |
| CRE-TM-12 | Ashgrave Houseguard | 16–17 | Humanoid | 359–390 | 31–42 to 34–46 | 2 s | 856 | — | 5 min | 125–130 |
| CRE-TM-13 | Ashgrave Ember-Mage | 17–18 | Humanoid (caster) | 312–337 | 13–18 to 14–20 | 2 s | 678 | 870 | 5 min | 130–135 |
| CRE-TM-14 | Hollowed Villager | 16–17 | Humanoid (Hollowed) | 359–390 | 31–42 to 34–46 | 2 s | 856 | — | 5 min | 125–130 |
| CRE-TM-15 | Hollowed Husk | 18 | Aberration | 422 | 36–49 | 2 s | 904 | — | 5 min | 135 |
| CRE-TM-16 | Fen Witch | 18–19 | Humanoid (caster) | 337–362 | 14–20 to 15–21 | 2 s | 714 | 915 | 5 min | 135–140 |
| CRE-TM-17 | Brandspire Sentinel | 19–20 | Construct | 453–484 | 46–62 to 49–66 | 2.4 s | 1000 | — | 5 min | 140–145 |
| CRE-TM-18 | Brandspire Pyromancer | 19–20 | Humanoid (caster) | 362–387 | 15–21 to 16–22 | 2 s | 750 | 960 | 5 min | 140–145 |
| CRE-TM-19 | **Mother Mirefang** (Elite) | 13 | Beast | 828 | 45–60 | 2 s | 616 | — | 7 min | 220 |
| CRE-TM-20 | **Scarhide** (Elite) | 14 | Beast | 906 | 48–65 | 2 s | 688 | — | 7 min | 230 |
| CRE-TM-21 | **Gallows Jack** (Elite) | 15 | Undead | 984 | 52–70 | 2 s | 760 | — | 7 min | 240 |
| CRE-TM-22 | **The Wickerman** (Elite) | 16 | Construct | 1078 | 68–91 | 2.4 s | 808 | — | 7 min | 250 |
| CRE-TM-23 | **Hollowed Elder Tamsin Reed** (Elite) | 18 | Humanoid | 1265 | 65–88 | 2 s | 904 | — | 7 min | 270 |
| CRE-TM-24 | **Magister Corvin Ashgrave, the Branded Lord** (Chain boss (elite)) | 20 | Humanoid | 2420 | 82–110 | 2 s | 1000 | — | 5 min | 435 |
| CRE-TM-25 | **P** (Named) | r | e | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 615 |
| CRE-TM-26 | **14** (Named) |  |  | 40 | 2–3 | 2 s | -8 | — | 5 min | 45 |
| CRE-TM-27 | **H** (Named) | u | m | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 630 |
| CRE-TM-28 | **n** (Named) | a | m | 1725 | 102–138 | 2 s | 1750 | — | 5 min | 530 |

### Abilities

| Creature | Ability | Kind | Effect at top level |
|---|---|---|---|
| Briarwood Stalker | Bite | Strike | 29 Physical; cooldown 8 s |
| Briarwood Stalker | Howl | Buff | Allies within 15 yd: +25% damage for 10 s; cooldown 30 s |
| Thornback Boar | Charge | Opener | 40 Physical on the first hit; closes from 8 to 25 yd |
| Thornback Boar | Thorn Hide | Defensive | reflects 3; lasts 6 s unless stated; cooldown 30 s |
| Briar Widow | Venom Spit | Damage over time | 58 Nature over 12 s (4 ticks); applied on hit, cooldown 15 s |
| Briar Widow | Web | Root | Roots 4 s; range 20 yd; cooldown 20 s |
| Graverobber | Shovel Smack | Control | Stun/incapacitate 1 s; deals 27 Physical; cooldown 20 s |
| Graverobber | Flee | Movement | Runs at 15% health for 8 s and alerts allies within 30 yd |
| Restless Bones | Bone Shard throw | Ranged or spell | 32–44 Shadow; 2 s cast; range 30 yd |
| Cinderbrand Acolyte | Cinder Bolt | Ranged or spell | 54–74 Fire; 2 s cast; range 30 yd |
| Cinderbrand Acolyte | Kindle Corpse | Summon | raises a nearby corpse; once per fight unless a cooldown is given |
| Cinderwight | Burning Grasp | Damage over time | 62 Fire over 12 s (4 ticks); applied on hit, cooldown 15 s; Fire DoT |
| Cinderwight | explodes for small AoE on death | Area attack | 26 Physical to all enemies within 8 yd, on death; cooldown 12 s |
| Fen Lurker | Death Roll | Strike | 41 Physical; cooldown 8 s |
| Fen Lurker | submerges | Opener | 51 Physical on the first hit; the creature is hidden until within 8 yd; stealth |
| Bog Shambler | Entangle | Root | Roots 3 s; range 20 yd; cooldown 20 s |
| Bog Shambler | regenerates | Heal | Heals 39 (12% of max health); 2.0 s cast, interruptible; cooldown 20 s; used below 50% health |
| Bog Shambler | resists Nature 50% | Trait | resists Nature 50% |
| Pactwatch Scout | Aimed Shot | Strike | 44 Physical; cooldown 8 s |
| Pactwatch Scout | Disengage | Movement | Teleports or leaps 10 yd and resets its swing; cooldown 15 s |
| Pactwatch Thornspeaker | Thornlash | Ranged or spell | 74–100 Nature; 2 s cast; range 30 yd |
| Pactwatch Thornspeaker | Renewal on allies | Heal | Heals 37 (12% of max health); 2.0 s cast, interruptible; cooldown 20 s; used below 50% health |
| Ashgrave Houseguard | Shield Block | Defensive | −50% damage taken; lasts 6 s unless stated; cooldown 30 s |
| Ashgrave Houseguard | Pummel | Strike | 48 Physical; cooldown 8 s |
| Ashgrave Ember-Mage | Fireball | Ranged or spell | 99–135 Fire; 2.5 s cast; range 30 yd |
| Ashgrave Ember-Mage | Flame Ward | Defensive | −50% damage taken; lasts 6 s unless stated; cooldown 30 s |
| Hollowed Villager | Empty Stare | Debuff | −10% damage dealt; lasts 15 s; cooldown 20 s |
| Hollowed Villager | does not flee | Movement | Teleports or leaps 10 yd and resets its swing; cooldown 15 s |
| Hollowed Husk | Hollow Touch | Drain | 42 Shadow per 2 s for 6 s (channel); burns the same amount of mana; cooldown 18 s |
| Fen Witch | Hex of Weakness | Debuff | curse; lasts 15 s; cooldown 20 s |
| Fen Witch | Bog Bolt | Ranged or spell | 84–114 Shadow; 2 s cast; range 30 yd |
| Brandspire Sentinel | Cleave | Area attack | 46 Physical to all enemies within 5 yd; cooldown 12 s |
| Brandspire Sentinel | immune to bleed | Trait | immune to bleed |
| Brandspire Pyromancer | Pyroblast | Silence | Silences or interrupts for 4 s; range 20 yd; cooldown 25 s |
| Brandspire Pyromancer | Blink | Movement | Teleports or leaps 10 yd and resets its swing; cooldown 15 s |

### Loot

| Creature | Loot table |
|---|---|
| Briarwood Stalker | No coin · Grey junk 75% · Skinning: Light Leather (Light Hide 10%) · Sharp Fang 40% · World table |
| Thornback Boar | No coin · Grey junk 75% · Skinning: Light Leather (Light Hide 10%) · Thornback Hide 40% · Ribs 25% · World table |
| Briar Widow | No coin · Grey junk 75% · Skinning: Light Leather (Light Hide 10%) · Small Venom Sac 40% · World table |
| Graverobber | Coin 33–108c (100%) · Linen Cloth 20%, Wool Cloth 20% · Grey junk 70% · orders 40% · World table |
| Restless Bones | Coin 18–58c (60%) · Linen Cloth 20%, Wool Cloth 20% · Grey junk 70% · Bone dust 40% · World table |
| Cinderbrand Acolyte | Coin 36–117c (100%) · Linen Cloth 20%, Wool Cloth 20% · Grey junk 70% · minor potions 40% · World table |
| Cinderwight | Coin 20–63c (60%) · Linen Cloth 20%, Wool Cloth 20% · Grey junk 70% · Corpse-Cinder 40% · World table |
| Fen Lurker | No coin · Grey junk 75% · Skinning: Light Leather (Light Hide 10%) · Mirejaw Hide 40% · Meat 25% · World table |
| Bog Shambler | No coin · Plant grey 65% · Herbalism on corpse where the zone doc says so · Shambler Heartwood 40% · Marshbloom 25% · World table |
| Pactwatch Scout | Coin 45–144c (100%) · Wool Cloth 35% · Grey junk 70% · arrows 40% · World table |
| Pactwatch Thornspeaker | Coin 48–153c (100%) · Wool Cloth 35% · Grey junk 70% · Crownleaf 40% · World table |
| Ashgrave Houseguard | Coin 48–153c (100%) · Wool Cloth 35% · Grey junk 70% · World table |
| Ashgrave Ember-Mage | Coin 51–162c (100%) · Wool Cloth 35% · Grey junk 70% · folios 40% · World table |
| Hollowed Villager | Coin 48–153c (100%) · Wool Cloth 35% · Grey junk 70% · World table |
| Hollowed Husk | No coin · Slime grey 65% · Faint aether residue 40% · World table |
| Fen Witch | Coin 54–171c (100%) · Wool Cloth 35% · Grey junk 70% · Hag-Charm 40% · Waterlogged Locket 3% · World table |
| Brandspire Sentinel | No coin · Scrap grey 65% · Iron scrap 40% · Bronze 25% · World table |
| Brandspire Pyromancer | Coin 57–180c (100%) · Wool Cloth 35% · Grey junk 70% · Spire Key fragment 40% · World table |
| **Mother Mirefang** | World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Scarhide** | World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Gallows Jack** | Coin 180–540c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **The Wickerman** | World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Hollowed Elder Tamsin Reed** | Coin 216–648c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Magister Corvin Ashgrave, the Branded Lord** | Coin 240–720c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **P** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **14** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **H** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **n** | World green 2% · named drop and quest items as listed in the zone and quest text documents |

## Cinderfall Barrens — T4, levels 20–30 (Khazrun)

### Stat blocks

| ID | Creature | Level | Type | Health | Damage per swing | Swing | Armor | Mana | Respawn | XP |
|---|---|---|---|---|---|---|---|---|---|---|
| CRE-CF-01 | Ash Jackal | 20–21 | Beast | 484–520 | 41–55 to 43–58 | 2 s | 1052 | — | 5 min | 145–150 |
| CRE-CF-02 | Cinder Skink | 21–22 | Beast | 520–556 | 43–58 to 46–62 | 2 s | 1104 | — | 5 min | 150–155 |
| CRE-CF-03 | Scoria Stinger | 21–22 | Beast (scorpion) | 520–556 | 43–58 to 46–62 | 2 s | 1104 | — | 5 min | 150–155 |
| CRE-CF-04 | Ember Sprite | 22–23 | Elemental | 556–592 | 50–68 to 53–71 | 2.2 s | 1156 | — | 5 min | 155–160 |
| CRE-CF-05 | Slagborn Raider | 22–23 | Humanoid | 556–592 | 46–62 to 48–65 | 2 s | 1156 | — | 5 min | 155–160 |
| CRE-CF-06 | Slagborn Pyresmith | 23–24 | Humanoid (caster) | 474–502 | 19–26 to 20–27 | 2 s | 906 | 1140 | 5 min | 160–165 |
| CRE-CF-07 | Slag Elemental | 24–25 | Elemental | 628–664 | 55–75 to 58–78 | 2.2 s | 1260 | — | 5 min | 165–170 |
| CRE-CF-08 | Obsidian Gazer | 25–26 | Beast (basilisk) | 664–710 | 53–71 to 56–75 | 2 s | 1308 | — | 5 min | 170–175 |
| CRE-CF-09 | Sulfur Ooze | 25–26 | Aberration | 664–710 | 53–71 to 56–75 | 2 s | 1308 | — | 5 min | 170–175 |
| CRE-CF-10 | Stonemaw Exile | 26–27 | Giant | 710–757 | 72–98 to 76–103 | 2.6 s | 1356 | — | 5 min | 175–180 |
| CRE-CF-11 | Cinderwing Drake | 27–28 | Dragonkin | 757–803 | 59–80 to 62–84 | 2 s | 1404 | — | 5 min | 180–185 |
| CRE-CF-12 | Molten Hulk | 28–29 | Elemental | 803–850 | 68–92 to 71–97 | 2.2 s | 1452 | — | 5 min | 185–190 |
| CRE-CF-13 | Pyrehound | 28–29 | Beast (elemental hound) | 803–850 | 68–92 to 71–97 | 2.2 s | 1452 | — | 5 min | 185–190 |
| CRE-CF-14 | Blackanvil Ironbreaker | 29–30 | Humanoid | 850–896 | 65–88 to 68–92 | 2 s | 1500 | — | 5 min | 190–195 |
| CRE-CF-15 | Blackanvil Flamecaller | 29–30 | Humanoid (caster) | 680–717 | 26–35 to 27–37 | 2 s | 1125 | 1410 | 5 min | 190–195 |
| CRE-CF-16 | **Dustmaw** (Rare) | 22 | Beast | 834 | 55–74 | 2 s | 1104 | — | 2–8 h | 155 |
| CRE-CF-17 | **Pyresmith Captain Dorrun** (Named) | 22 | Humanoid | 834 | 55–74 | 2 s | 1104 | — | 5 min | 155 |
| CRE-CF-18 | **Pyre-Captain Ilga** (Elite) | 25 | Humanoid | 1992 | 95–128 | 2 s | 1260 | — | 7 min | 340 |
| CRE-CF-19 | **Gazer Matriarch Vitrea** (Elite) | 26 | Beast | 2131 | 100–136 | 2 s | 1308 | — | 7 min | 350 |
| CRE-CF-20 | **Clinker** (Rare) | 28 | Elemental | 1205 | 82–111 | 2.2 s | 1404 | — | 2–8 h | 185 |
| CRE-CF-21 | **Gatewarden Brannoch** (Group boss (elite)) | 30 | Humanoid | 7168 | 150–202 | 2 s | 1500 | — | 15 min | 585 |

### Abilities

| Creature | Ability | Kind | Effect at top level |
|---|---|---|---|
| Ash Jackal | Pack Tactics | Buff | Allies within 15 yd: +25% damage for 10 s; cooldown 30 s |
| Ash Jackal | Hamstring bite | Slow | Slows movement 40% for 6 s; deals 31 Physical; cooldown 12 s |
| Cinder Skink | Ember Spit | Ranged or spell | 60–80 Fire; 2 s cast; range 30 yd |
| Cinder Skink | sheds tail | Movement | escape at 20%; cooldown 15 s |
| Scoria Stinger | Venom Sting | Damage over time | 94 Nature over 12 s (4 ticks), stacks to 5; applied on hit, cooldown 15 s; stacking |
| Scoria Stinger | Claw Grip | Pull or charm | Pulls the target to the creature; range 25 yd; cooldown 20 s |
| Ember Sprite | Fire Bolt | Ranged or spell | 62–84 Fire; 2 s cast; range 30 yd |
| Ember Sprite | Blink | Movement | Teleports or leaps 10 yd and resets its swing; cooldown 15 s |
| Slagborn Raider | Dual Strike | Strike | 67 Physical; cooldown 8 s |
| Slagborn Raider | Rend | Damage over time | 98 Physical over 12 s (4 ticks); applied on hit, cooldown 15 s |
| Slagborn Pyresmith | Slag Bolt | Ranged or spell | 110–150 Fire; 2 s cast; range 30 yd |
| Slagborn Pyresmith | Molten Weapon | Buff | Allies within 15 yd: +25% damage for 10 s; cooldown 30 s |
| Slag Elemental | Slag Slam | Area attack | 54 Fire to all enemies within 5 yd; cooldown 12 s |
| Slag Elemental | Leaves burning pool on death | Damage over time | 106 Fire over 12 s (4 ticks); applied on hit, cooldown 15 s |
| Obsidian Gazer | Petrifying Gaze | Control | Stun/incapacitate 3 s; deals 66 Physical; 2.0 s cast, avoid by facing away or interrupting; cooldown 20 s |
| Obsidian Gazer | Glass Hide | Defensive | reflects 10% spell damage; lasts 6 s unless stated; cooldown 30 s |
| Sulfur Ooze | Corrode | Damage over time | 110 Physical over 12 s (4 ticks), stacks to 5; applied on hit, cooldown 15 s; armor −200, stacks |
| Sulfur Ooze | splits at 50% | Strike | 79 Physical; cooldown 8 s |
| Stonemaw Exile | Smash | Area attack | 72 Physical to all enemies within 5 yd; cooldown 12 s |
| Stonemaw Exile | War Stomp | Area attack | 72 Physical to all enemies within 5 yd; cooldown 12 s |
| Cinderwing Drake | Flame Breath | Ranged or spell | 81–109 Fire; 2 s cast; range 30 yd; hits all targets in the area |
| Cinderwing Drake | Wing Buffet | Strike | 88 Physical; cooldown 8 s; knockback |
| Molten Hulk | Magma Fist | Strike | 101 Physical; cooldown 8 s |
| Molten Hulk | Eruption | Area attack | 67 Physical to all enemies within 5 yd; 2 s warning; cooldown 12 s; ground AoE, telegraphed |
| Molten Hulk | immune to Fire | Trait | immune to Fire |
| Pyrehound | Fire Breath | Ranged or spell | 84–114 Fire; 2 s cast; range 30 yd; hits all targets in the area |
| Pyrehound | Pack Howl | Buff | Allies within 15 yd: +25% damage for 10 s; cooldown 30 s |
| Blackanvil Ironbreaker | Shield Wall | Defensive | −50% damage taken; lasts 6 s unless stated; cooldown 30 s |
| Blackanvil Ironbreaker | Sunder | Debuff | −10% armor; lasts 15 s; cooldown 20 s |
| Blackanvil Ironbreaker | Shield Charge | Opener | 120 Physical on the first hit; closes from 8 to 25 yd |
| Blackanvil Flamecaller | Flamestrike | Ranged or spell | 150–202 Fire; 2 s cast; range 30 yd; hits all targets in the area |
| Blackanvil Flamecaller | Cauterize | Heal | Heals 86 (12% of max health); 2.0 s cast, interruptible; cooldown 20 s; used below 50% health |

### Loot

| Creature | Loot table |
|---|---|
| Ash Jackal | No coin · Grey junk 75% · Skinning: Medium Leather (Medium Hide 10%) · Ash Jackal Meat 40% · World table |
| Cinder Skink | No coin · Grey junk 75% · Skinning: Medium Leather (Medium Hide 10%) · Cinder Skink Tail 40% · Cinder Scale 25% · World table |
| Scoria Stinger | No coin · Grey junk 75% · Skinning: Medium Leather (Medium Hide 10%) · Large Venom Sac 40% · chitin 25% · World table |
| Ember Sprite | No coin · Elemental grey 60% · Small Ember Core 40% · World table |
| Slagborn Raider | Coin 66–207c (100%) · Wool Cloth 15%, Silk Cloth 25% · Grey junk 70% · Iron 40% · World table |
| Slagborn Pyresmith | Coin 69–216c (100%) · Wool Cloth 15%, Silk Cloth 25% · Grey junk 70% · Coal 40% · World table |
| Slag Elemental | No coin · Elemental grey 60% · Slag Heap (minable) 40% · Ember Core 25% · World table |
| Obsidian Gazer | No coin · Grey junk 75% · Skinning: Heavy Leather (Heavy Hide 10%) · Gazer Eye 40% · World table |
| Sulfur Ooze | No coin · Slime grey 65% · Sulfur 40% · slime 25% · World table |
| Stonemaw Exile | Coin 78–243c (100%) · Silk Cloth 35% · Grey junk 70% · coin (neutral until attacked) 40% · World table |
| Cinderwing Drake | No coin · Grey junk 75% · Skinning: Heavy Leather (Heavy Hide 10%) · Cinder Scale 40% · Hide 25% · World table |
| Molten Hulk | No coin · Elemental grey 60% · Ember Core 40% · Starmetal Ore 3% · World table |
| Pyrehound | No coin · Grey junk 75% · Skinning: Heavy Leather (Heavy Hide 10%) · Pyrehound Fang 40% · World table |
| Blackanvil Ironbreaker | Coin 87–270c (100%) · Silk Cloth 35% · Grey junk 70% · Steel 40% · World table |
| Blackanvil Flamecaller | Coin 87–270c (100%) · Silk Cloth 35% · Grey junk 70% · Gate Plans 40% · World table |
| **Dustmaw** | Guaranteed green (100%) · named drop and quest items as listed in the zone and quest text documents |
| **Pyresmith Captain Dorrun** | Coin 264–792c · World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **Pyre-Captain Ilga** | Coin 300–900c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Gazer Matriarch Vitrea** | World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Clinker** | Guaranteed green (100%) · named drop and quest items as listed in the zone and quest text documents |
| **Gatewarden Brannoch** | Coin 360–1080c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |

## The Riftlands — T4, levels 20–30 (Meridia)

### Stat blocks

| ID | Creature | Level | Type | Health | Damage per swing | Swing | Armor | Mana | Respawn | XP |
|---|---|---|---|---|---|---|---|---|---|---|
| CRE-RL-01 | Mesa Strider | 20–21 | Beast (tall running bird) | 484–520 | 37–50 to 39–53 | 1.8 s | 1052 | — | 5 min | 145–150 |
| CRE-RL-02 | Carrion Kite | 20–21 | Beast (bird) | 484–520 | 37–50 to 39–53 | 1.8 s | 1052 | — | 5 min | 145–150 |
| CRE-RL-03 | Blackspade Digger | 21–22 | Humanoid | 520–556 | 43–58 to 46–62 | 2 s | 1104 | — | 5 min | 150–155 |
| CRE-RL-04 | Howler Raider | 22–23 | Humanoid (hyena-folk) | 556–592 | 46–62 to 48–65 | 2 s | 1156 | — | 5 min | 155–160 |
| CRE-RL-05 | Blackspade Cutthroat | 23–24 | Humanoid | 592–628 | 48–65 to 50–68 | 2 s | 1208 | — | 5 min | 160–165 |
| CRE-RL-06 | Howler Bonecaller | 24–25 | Humanoid (caster) | 502–531 | 20–27 to 21–29 | 2 s | 945 | 1185 | 5 min | 165–170 |
| CRE-RL-07 | Blackspade Hexwright | 24–25 | Humanoid (caster) | 502–531 | 20–27 to 21–29 | 2 s | 945 | 1185 | 5 min | 165–170 |
| CRE-RL-08 | Rift Wyrm | 25–26 | Beast (burrowing worm) | 664–710 | 53–71 to 56–75 | 2 s | 1308 | — | 5 min | 170–175 |
| CRE-RL-09 | Chasm Lurker | 26–27 | Beast (pale cave-spider) | 710–757 | 50–68 to 53–72 | 1.8 s | 1356 | — | 5 min | 175–180 |
| CRE-RL-10 | Tor Vael Sentinel | 26–27 | Construct | 710–757 | 67–91 to 71–95 | 2.4 s | 1356 | — | 5 min | 175–180 |
| CRE-RL-11 | Buried Legionary | 27–28 | Undead | 757–803 | 59–80 to 62–84 | 2 s | 1404 | — | 5 min | 180–185 |
| CRE-RL-12 | Buried Magister | 28–29 | Undead (caster) | 643–680 | 25–33 to 26–35 | 2 s | 1089 | 1365 | 5 min | 185–190 |
| CRE-RL-13 | Echo Wraith | 28–29 | Undead (caster) | 643–680 | 25–33 to 26–35 | 2 s | 1089 | 1365 | 5 min | 185–190 |
| CRE-RL-14 | Stonecrawler | 29–30 | Beast (armoured rock-beetle) | 850–896 | 65–88 to 68–92 | 2 s | 1500 | — | 5 min | 190–195 |
| CRE-RL-15 | **Gang-boss "Red" Harl** (Elite) | 23 | Humanoid | 1776 | 86–117 | 2 s | 1156 | — | 7 min | 320 |
| CRE-RL-16 | **Old Flint** (Elite) | 26 | Beast | 2131 | 100–136 | 2 s | 1308 | — | 7 min | 350 |
| CRE-RL-17 | **Captain Morrigan Blackspade** (Group elite) | 26 | Humanoid | 3552 | 112–151 | 2 s | 1308 | — | 10 min | 525 |
| CRE-RL-18 | **The Stonecrawler Behemoth** (Group boss (elite)) | 30 | Beast | 7168 | 150–202 | 2 s | 1500 | — | 15 min | 585 |
| CRE-RL-19 | **Marshal's Shade** (Rare) | 28 | Undead | 1205 | 74–100 | 2 s | 1404 | — | 2–8 h | 185 |

### Abilities

| Creature | Ability | Kind | Effect at top level |
|---|---|---|---|
| Mesa Strider | Kick | Strike | 55 Physical; cooldown 8 s; knockback |
| Mesa Strider | Sprint | Movement | Teleports or leaps 10 yd and resets its swing; cooldown 15 s |
| Carrion Kite | Dive | Opener | 69 Physical on the first hit; closes from 8 to 25 yd |
| Carrion Kite | steals a buff | Strike | 55 Physical; cooldown 8 s |
| Blackspade Digger | Pick Swing | Strike | 65 Physical; cooldown 8 s |
| Blackspade Digger | Grog | Heal | Heals 67 (12% of max health); 2.0 s cast, interruptible; cooldown 20 s; used below 50% health |
| Howler Raider | Bola | Root | Roots 3 s; range 20 yd; cooldown 20 s |
| Howler Raider | Cackle | Summon | calls allies; once per fight unless a cooldown is given |
| Blackspade Cutthroat | Stealth ambush | Opener | 88 Physical on the first hit; the creature is hidden until within 8 yd |
| Blackspade Cutthroat | Poisoned Blade | Damage over time | 102 Nature over 12 s (4 ticks); applied on hit, cooldown 15 s |
| Howler Bonecaller | Bone Bolt | Ranged or spell | 116–156 Shadow; 2 s cast; range 30 yd |
| Howler Bonecaller | Bone Shield | Defensive | −50% damage taken; lasts 6 s unless stated; cooldown 30 s |
| Howler Bonecaller | heals | Heal | Heals 64 (12% of max health); 2.0 s cast, interruptible; cooldown 20 s; used below 50% health |
| Blackspade Hexwright | Dust Hex | Silence | Silences or interrupts for 3 s; range 20 yd; cooldown 25 s |
| Blackspade Hexwright | Lightning | Ranged or spell | 116–156 Nature; 2 s cast; range 30 yd |
| Blackspade Hexwright | Dust Devil pet | Silence | Silences or interrupts for 3 s; range 20 yd; cooldown 25 s |
| Rift Wyrm | Burrow ambush | Opener | 99 Physical on the first hit; the creature is hidden until within 8 yd |
| Rift Wyrm | Constrict | Root | Roots 3 s; range 20 yd; cooldown 20 s; 56 Physical per 2 s while held |
| Rift Wyrm | resists Nature 30% | Trait | resists Nature 30% |
| Chasm Lurker | Drag-line | Pull or charm | Pulls the target to the creature; range 25 yd; cooldown 20 s |
| Chasm Lurker | Bite | Strike | 74 Physical; cooldown 8 s |
| Tor Vael Sentinel | Arcane Cleave | Area attack | 66 Arcane to all enemies within 5 yd; cooldown 12 s |
| Tor Vael Sentinel | resists Arcane 50% | Trait | resists Arcane 50% |
| Tor Vael Sentinel | immune to bleed/poison | Trait | immune to bleed/poison |
| Buried Legionary | Shield Wall | Defensive | −50% damage taken; lasts 6 s unless stated; cooldown 30 s |
| Buried Legionary | Choking Dust | Silence | Silences or interrupts for 3 s; range 20 yd; cooldown 25 s |
| Buried Magister | Aether Lance | Ranged or spell | 143–193 Arcane; 2 s cast; range 30 yd |
| Buried Magister | Mana Burn | Drain | 64 Fire per 2 s for 6 s (channel); burns the same amount of mana; cooldown 18 s |
| Echo Wraith | Beckon | Pull or charm | Charms 5 s; breaks on damage; range 25 yd; cooldown 20 s |
| Echo Wraith | Shriek | Ranged or spell | 143–193 Physical; 2 s cast; range 30 yd |
| Stonecrawler | Crush | Strike | 96 Physical; cooldown 8 s |
| Stonecrawler | Rubble Prison | Root | Roots 3 s; range 20 yd; cooldown 20 s |

### Loot

| Creature | Loot table |
|---|---|
| Mesa Strider | No coin · Grey junk 75% · Skinning: Medium Leather (Medium Hide 10%) · Strider Drumstick 40% · World table |
| Carrion Kite | No coin · Grey junk 75% · Skinning: Medium Leather (Medium Hide 10%) · Kite Feathers 40% · World table |
| Blackspade Digger | Coin 63–198c (100%) · Wool Cloth 15%, Silk Cloth 25% · Grey junk 70% · Ration Crate 40% · World table |
| Howler Raider | Coin 66–207c (100%) · Wool Cloth 15%, Silk Cloth 25% · Grey junk 70% · bone trinkets 40% · World table |
| Blackspade Cutthroat | Coin 69–216c (100%) · Wool Cloth 15%, Silk Cloth 25% · Grey junk 70% · Smuggler's Key 40% · charts 25% · World table |
| Howler Bonecaller | Coin 72–225c (100%) · Wool Cloth 15%, Silk Cloth 25% · Grey junk 70% · Riftbloom 40% · World table |
| Blackspade Hexwright | Coin 72–225c (100%) · Wool Cloth 15%, Silk Cloth 25% · Grey junk 70% · Hexwright's Chime 40% · World table |
| Rift Wyrm | No coin · Grey junk 75% · Skinning: Heavy Leather (Heavy Hide 10%) · Rift Wyrm Hide 40% · Fillet 25% · World table |
| Chasm Lurker | No coin · Grey junk 75% · Skinning: Heavy Leather (Heavy Hide 10%) · Lurker Glow-Sac 40% · World table |
| Tor Vael Sentinel | No coin · Scrap grey 65% · Imperial scrap 40% · Starmetal 3% · World table |
| Buried Legionary | Coin 40–126c (60%) · Silk Cloth 25% · Grey junk 70% · imperial coins 40% · World table |
| Buried Magister | Coin 42–130c (60%) · Silk Cloth 25% · Grey junk 70% · Aether Prism 40% · World table |
| Echo Wraith | Coin 42–130c (60%) · Silk Cloth 25% · Grey junk 70% · Voice-Stone 40% · World table |
| Stonecrawler | No coin · Grey junk 75% · Skinning: Heavy Leather (Heavy Hide 10%) · World table |
| **Gang-boss "Red" Harl** | Coin 276–828c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Old Flint** | World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Captain Morrigan Blackspade** | Coin 312–936c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **The Stonecrawler Behemoth** | World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Marshal's Shade** | Coin 336–1008c · Guaranteed green (100%) · named drop and quest items as listed in the zone and quest text documents |

## Veilmoor — T4, levels 20–30 (Meridia)

### Stat blocks

| ID | Creature | Level | Type | Health | Damage per swing | Swing | Armor | Mana | Respawn | XP |
|---|---|---|---|---|---|---|---|---|---|---|
| CRE-VM-01 | Moor Hound | 20–21 | Beast | 484–520 | 41–55 to 43–58 | 2 s | 1052 | — | 5 min | 145–150 |
| CRE-VM-02 | Mistcat | 21–22 | Beast | 520–556 | 43–58 to 46–62 | 2 s | 1104 | — | 5 min | 150–155 |
| CRE-VM-03 | Bog Wisp | 22–23 | Elemental | 556–592 | 50–68 to 53–71 | 2.2 s | 1156 | — | 5 min | 155–160 |
| CRE-VM-04 | Drowned Pilgrim | 22–23 | Undead | 556–592 | 46–62 to 48–65 | 2 s | 1156 | — | 5 min | 155–160 |
| CRE-VM-05 | Moor Hag | 23–24 | Humanoid (caster) | 474–502 | 19–26 to 20–27 | 2 s | 906 | 1140 | 5 min | 160–165 |
| CRE-VM-06 | Gloom Bat | 24–25 | Beast | 628–664 | 50–68 to 53–71 | 2 s | 1260 | — | 5 min | 165–170 |
| CRE-VM-07 | Barrow Wight | 24–25 | Undead | 628–664 | 50–68 to 53–71 | 2 s | 1260 | — | 5 min | 165–170 |
| CRE-VM-08 | Barrow Guardian | 25–26 | Undead | 664–710 | 53–71 to 56–75 | 2 s | 1308 | — | 5 min | 170–175 |
| CRE-VM-09 | Grimroot Sapling | 25–26 | Plant | 664–710 | 63–86 to 67–91 | 2.4 s | 1308 | — | 5 min | 170–175 |
| CRE-VM-10 | Cairn Gargoyle | 26–27 | Elemental | 710–757 | 61–83 to 65–88 | 2.2 s | 1356 | — | 5 min | 175–180 |
| CRE-VM-11 | Hollowed Knight | 27–28 | Humanoid (Hollowed) | 757–803 | 59–80 to 62–84 | 2 s | 1404 | — | 5 min | 180–185 |
| CRE-VM-12 | Hollowed Courtier | 27–28 | Humanoid (caster) | 605–643 | 24–32 to 25–33 | 2 s | 1053 | 1320 | 5 min | 180–185 |
| CRE-VM-13 | Spectral Handmaiden | 28–29 | Undead (caster) | 643–680 | 25–33 to 26–35 | 2 s | 1089 | 1365 | 5 min | 185–190 |
| CRE-VM-14 | Hollowspire Sentinel | 29–30 | Construct | 850–896 | 78–105 to 82–110 | 2.4 s | 1500 | — | 5 min | 190–195 |
| CRE-VM-15 | **Grizelda Pondwife, Hag of Low Tarn** (Elite) | 23 | Humanoid | 1776 | 86–117 | 2 s | 1156 | — | 7 min | 320 |
| CRE-VM-16 | **Mistcat Matriarch** (Named) | 22 | Beast | 834 | 55–74 | 2 s | 1104 | — | 5 min | 155 |
| CRE-VM-17 | **Hrothmund, the Barrow-King** (Group elite) | 26 | Undead | 3552 | 112–151 | 2 s | 1308 | — | 10 min | 525 |
| CRE-VM-18 | **The Lamplighter's Ghost** (Rare) | 25 | Undead | 996 | 63–86 | 2 s | 1260 | — | 2–8 h | 170 |
| CRE-VM-19 | **Ser Cadoc the Unhorsed** (Rare elite) | 29 | Undead | 2549 | 117–158 | 2 s | 1452 | — | 2–8 h | 380 |

### Abilities

| Creature | Ability | Kind | Effect at top level |
|---|---|---|---|
| Moor Hound | Baying | Fear | Fear 2 s; 8 yd around the creature; cooldown 30 s |
| Moor Hound | Bite | Strike | 61 Physical; cooldown 8 s |
| Mistcat | Stealth | Opener | 81 Physical on the first hit; the creature is hidden until within 8 yd |
| Mistcat | Pounce | Opener | 81 Physical on the first hit; closes from 8 to 25 yd |
| Mistcat | Fade | Movement | Teleports or leaps 10 yd and resets its swing; cooldown 15 s |
| Bog Wisp | Lure-light | Pull or charm | Pulls the target to the creature; range 25 yd; cooldown 20 s |
| Bog Wisp | Arcane Zap | Ranged or spell | 62–84 Arcane; 2 s cast; range 30 yd |
| Bog Wisp | Flee | Movement | Runs at 15% health for 8 s and alerts allies within 30 yd |
| Drowned Pilgrim | Waterlogged Grasp | Slow | Slows movement 40% for 6 s; deals 34 Nature; cooldown 12 s |
| Drowned Pilgrim | Disease: Bog Rot | Damage over time | 98 Shadow over 12 s (4 ticks); applied on hit, cooldown 15 s |
| Moor Hag | Curse of the Fog | Debuff | −hit; lasts 15 s; cooldown 20 s |
| Moor Hag | Bog Bolt | Ranged or spell | 110–150 Shadow; 2 s cast; range 30 yd |
| Moor Hag | Summon Wisp | Summon | Calls 1 ally of the same family within 30 yd; once per fight unless a cooldown is given |
| Gloom Bat | Sonic Screech | Silence | Silences or interrupts for 3 s; range 20 yd; cooldown 25 s |
| Gloom Bat | Leech | Drain | 56 Physical per 2 s for 6 s (channel); heals the creature for the damage dealt; cooldown 18 s |
| Barrow Wight | Chilling Touch | Strike | 74 Physical; cooldown 8 s; Frost |
| Barrow Wight | Life Drain | Drain | 56 Shadow per 2 s for 6 s (channel); heals the creature for the damage dealt; cooldown 18 s |
| Barrow Guardian | Shield Block | Defensive | −50% damage taken; lasts 6 s unless stated; cooldown 30 s |
| Barrow Guardian | Ancient Oath | Defensive | reflects first spell; lasts 6 s unless stated; cooldown 30 s |
| Grimroot Sapling | Root Lash | Root | Roots 3 s; range 20 yd; cooldown 20 s |
| Grimroot Sapling | Regrowth | Heal | Heals 85 (12% of max health); 2.0 s cast, interruptible; cooldown 20 s; used below 50% health |
| Grimroot Sapling | resists Nature 50% | Trait | resists Nature 50% |
| Cairn Gargoyle | Stone Form | Trait | immune, heals |
| Cairn Gargoyle | Dive | Opener | 114 Physical on the first hit; closes from 8 to 25 yd |
| Hollowed Knight | Mortal Cleave | Heal | Heals 96 (12% of max health); 2.0 s cast, interruptible; cooldown 20 s; used below 50% health |
| Hollowed Knight | Hollow Oath | Defensive | −50% damage taken; lasts 6 s unless stated; cooldown 30 s |
| Hollowed Courtier | Hollow Whisper | Damage over time | 118 Shadow over 12 s (4 ticks); applied on hit, cooldown 15 s; Shadow DoT |
| Hollowed Courtier | Polite Applause | Buff | Allies within 15 yd: +25% damage for 10 s; cooldown 30 s |
| Spectral Handmaiden | Phase | Movement | untargetable 2 s; cooldown 15 s |
| Spectral Handmaiden | Shadow Bolt | Ranged or spell | 143–193 Shadow; 2 s cast; range 30 yd |
| Spectral Handmaiden | Mend Mistress | Heal | Heals 82 (12% of max health); 2.0 s cast, interruptible; cooldown 20 s; used below 50% health |
| Hollowspire Sentinel | Halberd Sweep | Area attack | 77 Physical to all enemies within 5 yd; cooldown 12 s |
| Hollowspire Sentinel | Ward Link | Defensive | shields nearby pylon; lasts 6 s unless stated; cooldown 30 s |

### Loot

| Creature | Loot table |
|---|---|
| Moor Hound | No coin · Grey junk 75% · Skinning: Medium Leather (Medium Hide 10%) · Moor Hound Flank 40% · World table |
| Mistcat | No coin · Grey junk 75% · Skinning: Medium Leather (Medium Hide 10%) · Whiskers 40% · World table |
| Bog Wisp | No coin · Elemental grey 60% · Wisp Essence 40% · World table |
| Drowned Pilgrim | Coin 33–104c (60%) · Wool Cloth 15%, Silk Cloth 25% · Grey junk 70% · Pilgrim's Token 40% · World table |
| Moor Hag | Coin 69–216c (100%) · Wool Cloth 15%, Silk Cloth 25% · Grey junk 70% · Hag-Stone 40% · World table |
| Gloom Bat | No coin · Grey junk 75% · Skinning: Heavy Leather (Heavy Hide 10%) · Bat Wing 40% · World table |
| Barrow Wight | Coin 36–112c (60%) · Wool Cloth 15%, Silk Cloth 25% · Grey junk 70% · Grave Goods 40% · World table |
| Barrow Guardian | Coin 38–117c (60%) · Wool Cloth 15%, Silk Cloth 25% · Grey junk 70% · old iron 40% · Starmetal 3% · World table |
| Grimroot Sapling | No coin · Plant grey 65% · Herbalism on corpse where the zone doc says so · Veilshade 40% · sap 25% · World table |
| Cairn Gargoyle | No coin · Elemental grey 60% · Gargoyle Heart 40% · Solid Stone 25% · World table |
| Hollowed Knight | Coin 81–252c (100%) · Silk Cloth 35% · Grey junk 70% · Steel 40% · World table |
| Hollowed Courtier | Coin 81–252c (100%) · Silk Cloth 35% · Grey junk 70% · Invitation 40% · World table |
| Spectral Handmaiden | Coin 42–130c (60%) · Silk Cloth 25% · Grey junk 70% · diary pages 40% · Ghostlily 25% · World table |
| Hollowspire Sentinel | No coin · Scrap grey 65% · Starmetal 3% · scrap 25% · World table |
| **Grizelda Pondwife, Hag of Low Tarn** | Coin 276–828c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **Mistcat Matriarch** | World green 2% · named drop and quest items as listed in the zone and quest text documents |
| **Hrothmund, the Barrow-King** | Coin 312–936c · World green 8%, world blue 1% · named drop and quest items as listed in the zone and quest text documents |
| **The Lamplighter's Ghost** | Coin 300–900c · Guaranteed green (100%) · named drop and quest items as listed in the zone and quest text documents |
| **Ser Cadoc the Unhorsed** | Coin 348–1044c · Guaranteed green (100%) · named drop and quest items as listed in the zone and quest text documents |

**Totals:** 152 creature types · 73 named, rare and elite creatures · 272 ability rows.
