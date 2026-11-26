# World Layout — Stonewake Dale and Stoneheart Deeps

[← World Layout Index](00-world-layout.md) · Zones: [Stonewake Dale](../05-zones/t1-stonewake-dale.md) · [Stoneheart Deeps](../05-zones/t2-stoneheart-deeps.md) · Prev: [Harrowfield and Russetwood](02-harrowfield-russetwood.md) · Next: [Thornwick Marches](04-thornwick-marches.md)

Notation and rules are in the [index](00-world-layout.md).

# Stonewake Dale

Laid out again on 2026-11-26, after the owner played the zone and found it sparse: the square, its place on the continent and its four exits are kept, and the dale inside it is made compact, enclosed and densely dressed. The 18 quests, their NPCs, the creature list and every camp's count are as before. The rules the generator follows for the mountains, the ground, the trees, the dressing sets, the walls and the light are in [World Construction](10-world-construction.md) §2 to §5, §12 and §13.

| | |
|---|---|
| Size and offset | 1,400 × 1,400 m · Khazrun (1200, 4600). Each grid cell is 140 m |
| Playable dale | About 55 ha of the square's 196 ha: the ground inside the dale outline below (49.5 ha), the four gorges (4.5 ha) and the dam crest. Everything else is mountain that cannot be climbed |
| Shape | A small farmed dale under Mount Khaz (west and north-west), closed by a wooded ridge to the south and a long ridge to the east. A starter bowl round Sunbank Steading lies in its south-west; Hopstead stands outside the bowl's gate in the middle; the hop-yards, the Adit and the Old Brewery lie along the mountain's foot to the west and north-west, Ridgefold and the High Pastures on the east ridge. The dam closes the valley head in the north-east; its millrace runs down past Hopstead's mills to the mill-pool |
| Elevation | Valley floor 6–16 m · Sunbank 12 m · Hopstead 10 m · terraces 14–38 m · Greywall Quarry floor 40 m, face top 54 m · Larch Hangers crest 60 m · Daleside Adit 30 m · Old Brewery 14 m · Ridgefold 36 m · High Pastures 52 m · ridge top 66 m · dam foot 15 m, dam crest 85 m · Mount Khaz's flank 220–300 m · south ridge 150 m · east rim 95 m · east ridge 190 m · valley head 200–240 m |
| Enclosure | The horizon stands at least 12° above eye level in every direction, measured every 5° of bearing on what the client draws, from each of: the start point, the Sunbank gate, Hopstead's green, the hop-yard gate, the brewery yard gate, the Adit's spoil banks, Ridgefold and the High Fold. No view runs out of the zone: each gorge bends, and past the zone's edge the client draws the zone's skyline, never a flat plane |
| Landmark | Stonewake Dam, a grey wall 320 m wide and 70 m high across the valley head, its middle at (880, 1290): 554 m from Hopstead's green, seen above the village's roofs, and seen from the starter bowl through the Sunbank gate and over the bank, drawn there on the skyline past the draw distance |
| Exits | Dalegate road → Hammerdeep (100, 1400) · Bouldergate Pass → Embercrag Hollow (300, 1400) · Daleside Adit → Stoneheart Deeps (0, 800) · south road → Ironroot (700, 0). Each is reached through a gorge |
| Start point | (332, 680), facing west toward the longhouse porch 14 m away and into the bowl: the terraces rise behind the longhouse, the quarry's derrick stands on the skyline to its right, the first sink's rag poles are in the low field to its left |

```
      A  B  C  D  E  F  G  H  I  J
 10   .. .. .. ## ## DM DM DM ## ##
  9   ## OB .. ## MR MR DM ## ## ##
  8   DA HY HY .. MR HP HP ## ## ##
  7   DA LH .. HS RF HP ## ## ## ##
  6   GQ BT .. .. .. ## ## ## ## ##
  5   ## GS SS .. .. ## ## ## ## ##
  4   ## GS .. ## ## .. ## ## ## ##
  3   ## ## ## ## ## .. ## ## ## ##
  2   ## ## ## ## ## .. ## ## ## ##
  1   ## ## ## ## ## .. ## ## ## ##
```

The grid is the coarse picture. The edge of the playable ground is the dale outline, and every `##` cell and every part of another cell outside the outline is mountain.

## Dale outline

The playable floor is the ground inside this polygon, its points given clockwise from the bowl's south side. The gorges leave it where the table of ridges and gorges says.

| Stretch | Points |
|---|---|
| The starter bowl, south and west | (285, 430) → (190, 455) → (120, 535) → (100, 650) → (88, 715) → (86, 825) |
| The Larch Hangers and the Adit's spoil banks | (128, 835) → (128, 937) → (60, 940) → (60, 1087) |
| The mountain's foot and the Old Brewery | (120, 1180) → (197, 1245) → (285, 1268) → (322, 1268) |
| The mill meadows, north of Hopstead | (400, 1175) → (430, 1250) → (540, 1250) → (630, 1200) → (690, 1235) |
| The dam foot | (735, 1235) → (900, 1235) → (860, 1150) → (722, 1122) |
| The High Pastures and Ridgefold | (950, 1120) → (950, 890) → (722, 890) → (708, 880) |
| The low meadows and the south gorge's mouth | (790, 800) → (720, 720) → (665, 735) → (615, 730) → (545, 775) |
| The starter bowl, east | (515, 700) → (512, 610) → (475, 505) → (385, 440) → back to (285, 430) |

**The starter bowl** is the part of the outline south of the Sunbank bank and the Larch Hangers' foot: about 420 × 380 m of floor (14 ha) with Sunbank Steading in its middle, ringed by the terraces and the quarry (west), the Larch Hangers (north), the Sunbank bank and its gate (north-east), the east rim (east) and the south ridge's wooded face (south). It holds levels 1 to 3 and quests ST-01 to ST-07. Nothing in it is more than 190 m of walking from the start point.

## Ridges, banks, gorges and gates

| Feature | Where | Shape |
|---|---|---|
| Mount Khaz's flank | West and north-west of the outline, from the quarry round to the passes | Rises from the outline to 220–300 m within 250 m; crags and larches on its lowest 60 m |
| The Greywall spur | Between the quarry and the Adit cut, (60–128, 825–935) | A rock spur, crest 80 m |
| The south ridge | South of the bowl; crest along z = 360 from x = 120 to x = 600 | Crest 150 m. Its north face is wooded and is the bowl's south rim |
| The east rim | Between the bowl and the south gorge; crest along x = 590 from z = 520 to z = 760 | Crest 95 m, falling north to the Sunbank bank at (545, 775) |
| The east ridge | East of Ridgefold and the High Pastures; crest along x = 1010 from z = 760 to z = 1200 | Crest 190 m |
| The valley head | Either side of the dam: (560–720, 1250–1400) and (1040–1260, 1180–1400) | 200–240 m; the dam stands between the two |
| The Sunbank bank | From the Hangers' east end (320, 838) through the gate (400, 818) to the east rim (545, 775) | A wooded bank 10 m high (crest 22 m) with a continuous dry-stone wall along its crest. Its only gap is the gate |
| The Sunbank gate | (400, 818) | A gap 8 m wide in the bank and its wall: two gate piers and a field gate standing open. The lane goes through it and crosses the race on a slab bridge 18 m beyond, at (408, 836). Hopstead's roofs and the lower mill's wheel are seen through it |
| South gorge | The Dale Road from (700, 0) to the gorge mouth (640, 740) | Floor 40 m wide at road height, rock walls 60–120 m high; bends at (720, 300) and (700, 560). No gate, no signpost arm, no milestone and no guard: the south road stays open and unmarked |
| Adit cut | Adit Lane from (130, 935) to the Adit door (0, 800) | Floor 20 m wide, walls 30–60 m; bends at (65, 870). The Adit's timber door-frame stands at its end |
| Dalegate gorge | The Dale Road from the fork (300, 1262) to the Dalegate (100, 1400) | Floor 30 m wide, walls 60–100 m; bends at (215, 1322). The Dalegate itself closes its end |
| Bouldergate gorge | Bouldergate Path from the fork (300, 1262) to (300, 1400) | Floor 30 m wide, walls 60–100 m; bends at (318, 1330). The Bouldergate arch, a hill-dwarf stone arch over the path, at (312, 1306) |

## Sub-areas

| Code | Sub-area | Centre | Size | Elevation and terrain |
|---|---|---|---|---|
| SS | Sunbank Steading | (335, 680) | 120 × 110 | A low sunny bank, 12 m, in the middle of the starter bowl at the foot of the terraces; the longhouse on its west side with the terraces rising behind it, the yard in front of its porch, the lambing paddock to the south, the lane leaving north-east to the gate |
| BT | The Barley Terraces | (231, 745) | 120 × 170 | Stepped fields of young barley with dry-stone walls: five curved benches 18–30 m wide, climbing west from 14 m to 38 m, three or four of them in view from the yard |
| GQ | Greywall Quarry | (130, 770) | 85 × 110 | A quarry floor at 40 m above the top terrace, its face 14 m high on the west and north sides; the derrick on the floor's east lip at (168, 760); dressed stone stacked on its floor |
| LH | The Larch Hangers | (225, 890) | 190 × 120 | Larch wood on a steep ridge that closes the bowl's north side: crest 60 m along z = 888, a bench 25 m wide along the crest, ledges on the north face; felled logs and the sawyers' slide down the south face to the terraces at (200, 832) |
| GS | The Gravelkin Sinks | Mouth (212, 592), in the first sink; interior under the low fields and the bowl's south rim, running in south from the mouth within (110–330, 300–585) | Surface 130 × 135 around (205, 572), five sinkholes; interior 2 galleries, about 220 m of tunnel, and the Deep Sink below | Round gnawed tunnels under fallen-in barley strips; the Deep Sink is a single cavern 40 m across. The first sink, at (212, 612) and 24 m in radius, is a hollow that is walked down into, and the mouth opens in its south bank; the other four sinks, at (178, 566), (230, 560), (196, 530) and (244, 532), are open pits with broken rims and are not ways in |
| HS | Hopstead | (450, 940) | 180 × 180 | Market village around a brewhouse green, 10 m; two mills on the race, which runs down its west side |
| HY | The Hop-Yards | (295, 1045) | 160 × 120 | Hop-poles in new leaf, in blocks of 6–10 rows with headlands between them; the herb banks along the south edge, a sunny bank between Adit Lane and the yards; the hop-kiln at the south-east corner, by the hop-yard gate |
| MR | The Millrace | Runs dam foot (800, 1215) → (705, 1150) → (590, 1065) → (470, 1030) → Hopstead's mills (405, 995) → (402, 900) → (404, 852) → along the foot of the Sunbank bank (470, 822) → mill-pool (520, 808) | 12 m channel with a path; 6 culverts | Stone-lined, fast water, crossed by 4 slab bridges: the Dale Road's (455, 1022), Adit Lane's (403, 951), Sunbank Lane's (408, 836) and the Race Path's footbridge at the dam foot (790, 1208) |
| OB | The Old Brewery | (262, 1180) | 130 × 130 | Stone brewhouse with a vat hall, cellar and walled yard, 14 m, under Mount Khaz; its tall chimney is seen from the Dale Road |
| DA | Daleside Adit | Adit door (0, 800), the exit; upper drift mouth (95, 1020), running in west | Surface 150 × 150 around (135, 1012); the upper drift is an interior of 1 gallery and about 60 m of tunnel | Timbered mine mouths in the west mountainside, 30 m, spoil banks below them. The upper drift is a worked-out level of its own, not joined to the way through to the Deeps |
| RF | Ridgefold | (630, 955) | 150 × 140 | Sheep-folds and bothies on a shoulder of the east ridge, 36 m |
| HP | The High Pastures | (805, 1005) | 180 × 210 | Open hill grazing on a shelf of the east ridge, 52 m; the High Fold at its south-west corner, 4 stone bothies, three rustler tent camps, the ridge top at its north-east corner, 66 m, with a beacon cairn |
| DM | Stonewake Dam | (880, 1310) | 320 × 180 | Dam crest road at 85 m, two sluice-houses (east and west), the dam stair at the west end; reservoir behind (scenery). The wall runs along z = 1290 from x = 720 to x = 1040; its foot is at z = 1215 on the valley floor |

No sink lies within 60 m of Sunbank's edge. The Old Brewery is a building that is entered: its vat hall, with a cellar below reached by a hatch and stair. The four bothies and the High Fold are built: the bothies as buildings of the hill-dwarf kit, the High Fold as a sheep-fold.

| Building on the High Pastures | Position |
|---|---|
| The High Fold (an empty sheep-fold) | (735, 950) |
| Lower bothy | (812, 938) |
| Middle bothy | (858, 990) |
| Upper bothy | (748, 1048) |
| High bothy | (846, 1084) |

## Hubs

| Hub | Centre | Radius | Buildings and spots |
|---|---|---|---|
| Sunbank Steading | (335, 680) | 50 | Longhouse and hearth, its door and porch facing east onto the yard (−30, 0) · longhouse porch (−17, 0) · stone-sledge (−34, +28) · terrace wall, the end of the lowest wall, with the Stonesinger's standing stone (−20, +44) · practice yard (−2, +38) · hearth-nook, opening onto the practice yard (+16, +44) · kitchen (−30, −28) · kitchen hearth, outdoors (−16, −30) · lambing paddock (+2, −44) · sawpit (+30, −26) · graveyard (+75, −45) |
| Hopstead | (450, 940) | 90 | Moot-house (0, +45) · moot-stone (0, +12) · brewhouse (−26, +26) and the eyrie against its gable (−26, +40) · *The Dry Boot* (+30, 0) · smithy on the green (+8, −30) · market stall (−8, −6) · upper mill (−48, +42) · lower mill (−46, −30) · hop-yard gate (−78, +38) · hop-kiln (−66, +56) · tan-yard (−66, −60) · weaving-house (+60, −16) · physic garden (+60, +34) · cottage at the lane end (+82, −30) · mailbox by the inn · graveyard (+90, −38) |
| Ridgefold | (630, 955) | 45 | Ranger bothy (0, 0) · sheep-fold (+25, +18) · lambing shed (−22, +24) |
| Dam east sluice-house | (1000, 1300) | 25 | Dammaster's post |

The three class trainers stand round the one practice yard: the Fighter trainer in it, the Cleric trainer at the hearth-nook on its east side, the Druid trainer on the terrace wall on its west side, by his standing stone. Every Hopstead building stands within 70 m of the green except the hop-yard gate, the hop-kiln, the tan-yard and the cottage at the lane end.

## Points

| Point | Position | Used by |
|---|---|---|
| Crates of Stolen Stores (10 positions) | Second gallery of the Sinks | ST-07 |
| Herb Baskets (8 positions) | The herb banks, (225–365, 962–984) | ST-09 |
| High Fold trigger | (735, 950) r25 | ST-11 |
| Brewmaster Maltby | Brewery yard gate (328, 1162) | ST-13 |
| Chief Gnarr | Middle of the Deep Sink, the lowest cavern, reached by the ramp from the second gallery | ST-16 |
| Old Bitterhorn | Ridge top (850, 1062) | ST-17 |
| Greedy Gund (rare) | 3 bothies on the High Pastures: the lower, middle and upper bothy | — |
| Tinker Sparkwright's sluice hut | (600, 1046) | — |
| Angler Pikehook | Mill-pool below Hopstead (528, 798) | — |
| Graveyards | Sunbank (410, 635) · Hopstead (540, 902) · Ridgefold (690, 985) · Brewery Lane (396, 1140) · dam road (690, 1125) | — |
| Chests (one active) | Second gallery of the Sinks · brewery cellar · high bothy | — |

Until Embercrag Hollow and Stoneheart Deeps are built as level 5–10 zones, the two NPCs who end ST-18 wait inside the dale, each about 15 m in from the exit that leads to their zone and beside its road: Forgemaster Emberhand at Bouldergate Pass, Hallwarden Lampwright at the Daleside Adit.

## Spawn camps

Each creature stands in a place that explains it; the props of those places are in the dressing sets below.

| Camp | Creature | Count | Where | Notes |
|---|---|---|---|---|
| ST-S01 | Highland Buzzard | 26 | BT lower three benches and their wall tops, (219–285, 662–828) | From 15 m outside Sunbank's edge; the nearest about 65 m from the start point. Perched on the wall tops and circling |
| ST-S02 | Feral Billy | 22 | BT upper two benches and the Quarry Track, (171–219, 662–828) | |
| ST-S03 | Young Shale Bear | 12 | LH crest bench and north ledges, (140–310, 862–926) | None within 25 m of Adit Lane |
| ST-S04 | Gravelkin Sinkdweller | 26 | GS first sink and first gallery | 8 outside, in the first sink and among the spoil heaps on the rims, within 55 m of (208, 580) |
| ST-S05 | Gravelkin Bonechewer | 14 | GS second gallery and the Deep Sink approach | 12 in the second gallery, around the crates · 2 on the ramp down to the Deep Sink, who are Chief Gnarr's two guards |
| ST-S06 | Hop-Blight Beetle | 24 | HY blocks west of x = 300, (215–300, 990–1100) | Clear of Adit Lane; 60 m from Hopstead's edge |
| ST-S07 | Shale Bear | 18 | DA spoil banks @ (140, 1022) r45 and the upper drift | 12 outside, round the den · 6 in the drift's gallery; none within 40 m of Adit Lane |
| ST-S08 | Fermented Ooze | 16 | OB yard, vat hall and cellar | 10 in the yard and round the walls · 4 in the vat hall · 2 in the cellar; none within 25 m of the Dale Road |
| ST-S09 | Dale Rustler | 20 | HP south and middle, (740–890, 905–1000): the lower and middle tent camps and the two bothies beside them | None within 60 m of Ridgefold's edge |
| ST-S10 | Rustler's Hound | 10 | HP north, (722–890, 1008–1105): the upper tent camp and its pen | |
| ST-S11 | Rustler Hound-Master | 12 | HP north, the upper tent camp and the upper and high bothies | No two within 30 m of each other |

## Nodes

| Node | Positions | Where |
|---|---|---|
| Copper Vein | 22 | Terrace walls 10 · quarry face 6 · adit spoil banks 6 |
| Sunpetal | 20 | Field margins and lanes |
| Hearthroot | 16 | Feet of the terrace walls and the quarry |
| Dewleaf | 12 | Larch Hangers and the herb banks |
| Fishing | Millrace and the mill-pool | No pools at this level |

## Roads

Every quest area is reached along a road or track that is seen on the ground and that runs toward the area's own landmark, so the eye is led before the feet are.

| Road | Path | Leads the eye to |
|---|---|---|
| Dale Road | Ironroot (700, 0) → up the south gorge (720, 300) → (700, 560) → the gorge mouth (640, 740) → (560, 840) → (490, 895) → Hopstead (450, 940) → round the east end of the moot-house (476, 990) → over the race (455, 1022) → (420, 1100) → (380, 1150) → the fork (300, 1262) → up the Dalegate gorge (215, 1322) → Dalegate (100, 1400) | Hopstead's moot-house; northbound, the two gorges in Mount Khaz |
| Bouldergate Path | The fork (300, 1262) → (318, 1330) → (300, 1400) | The Bouldergate arch |
| Sunbank Lane | Sunbank (335, 680) → (372, 720) → (392, 780) → the Sunbank gate (400, 818) → over the race (408, 836) → (425, 880) → Hopstead (450, 940) | The gate, and through it the lower mill's wheel and the dam |
| Sink Track | Sunbank's yard (312, 654) → (262, 630) → the first sink's rim (234, 616) → down into the sink to the mouth (214, 594) | The farmers' rag poles round the first sink |
| Quarry Track | Sunbank's stone-sledge (303, 706) → up the terrace steps (262, 726) → (218, 748) → Greywall Quarry (170, 762) → along the top bench (178, 800) → the sawyers' slide (200, 832) | The quarry's derrick; then the slide's timber rails |
| Adit Lane | Hopstead → over the race (403, 951) → along the foot of the Larch Hangers, south of the herb banks (215, 952) → (130, 935) → up the Adit cut (65, 870) → Daleside Adit (0, 800) | The hop-kiln's cowl; then the Adit's timber door-frame |
| Foot Path | Adit Lane (190, 952) → the Adit's spoil banks (150, 1040) → along the mountain's foot (185, 1100) → the brewery yard (232, 1150) | The upper drift's lamps; the brewery's chimney |
| Brewery Lane | Dale Road (380, 1150) → brewery yard gate (328, 1162) | The brewery's chimney |
| Ridge Track | Hopstead's green, east side (530, 945) → Ridgefold (630, 955) → the High Fold (735, 950) → (790, 1005) → the ridge top (850, 1062) | Ridgefold's sheep-fold; then the beacon cairn on the ridge top |
| Race Path | Dale Road at the race bridge (455, 1022) → along the race's south bank (590, 1050) → (700, 1135) → dam foot (790, 1205) → the dam stair (742, 1218) up to the crest (735, 1300) | The dam |
| Dam crest road | (735, 1300) → (880, 1300) → (1000, 1300) | The east sluice-house |

The Dale Road, Sunbank Lane, Adit Lane and Brewery Lane are main roads; the others are tracks. No road is cut more than 1.5 m into the ground or raised more than 1.5 m above it; the Quarry Track climbs the terraces by steps at the wall gaps, and the Ridge Track switches back where the shoulder is steeper than 15%.

## Signposts, milestones and lamp posts

| Kind | Where | Detail |
|---|---|---|
| Signpost | Sunbank's yard, where the lane leaves (346, 692) | Hopstead |
| Signpost | Where the Sink Track and the Quarry Track leave the yard: (312, 654) and (303, 706) | The Sinks · Greywall Quarry |
| Signpost | The Sunbank gate, outside (404, 826) | Sunbank Steading · Hopstead |
| Signpost | Hopstead's green, by the moot-stone (454, 950) | Sunbank · the Adit · Ridgefold · the dam · Dalegate and Bouldergate. No arm for the south road |
| Signpost | The hop-yard gate (372, 978) | The Hop-Yards · Daleside Adit |
| Signpost | Adit Lane at the Foot Path (190, 952) | The spoil banks · the Old Brewery |
| Signpost | Dale Road at the race bridge (455, 1022) | The dam · the sluice hut |
| Signpost | Dale Road at Brewery Lane (380, 1150) | The Old Brewery · the passes |
| Signpost | The fork (300, 1262) | Dalegate, Hammerdeep · Bouldergate Pass, Embercrag Hollow |
| Signpost | Hopstead's green, east side (530, 945), and Ridgefold (630, 955) | Ridgefold · the High Fold |
| Milestone | Every 100 m along the Dale Road north of Hopstead (5), Adit Lane (5) and Sunbank Lane (2), counted from the moot-stone | Each carved with the distance to Hopstead. None on the Dale Road south of Hopstead |
| Lamp post | Sunbank's yard 2 · the Sunbank gate 2 · Sunbank Lane from the gate to Hopstead, one every 30 m (4) · Hopstead's green 4 · the Dale Road from the green to the race bridge 2 · Ridgefold 1 · the brewery yard gate 1 · the Adit door 2 · the Bouldergate arch 2 · the dam foot 2 | The hill-dwarf lamp post; lit at night |

## Dressing sets

A dressing set is a small arrangement of props placed as one unit ([World Construction §5](10-world-construction.md#dressing-sets)). The sets below are this zone's own; their props are listed in [Environments & Props](../10-art/03-environments-props.md#stonewake-dale). A set at a hub spot stands at that spot; the others are placed at the positions given. Road furniture and field edges are placed by the rules of World Construction and are not listed. A lamp post, signpost or milestone named in a set is the one the table above already places there.

| Place | Set | Props | Count |
|---|---|---|---|
| Sunbank: longhouse porch | Porch | Two benches, a banner pole with the Dale-Moot banner, a wood stack, two barrels, a hanging lantern, two flower beds | 9 |
| Sunbank: yard, between the porch and the lane | Hay yard | Hay cart, three haystacks, a pitchfork, a water trough, a feed sack | 7 |
| Sunbank: kitchen hearth | Outdoor kitchen | Outdoor hearth with a cook pot, a trestle table, a bench, two barrels, a clay jar, an egg basket, a loaf, a washing tub | 9 |
| Sunbank: practice yard | Practice yard | Two training dummies, a weapon rack, two benches, four runs of post-and-rail fence with one gap | 9 |
| Sunbank: sawpit | Sawpit | The sawpit, two log piles, two fallen logs, a saw, a felling axe, two stumps, a cart | 10 |
| Sunbank: stone-sledge | Sledge | The stone-sledge, three stacks of cut blocks, a bench, a hammer | 6 |
| Sunbank: lambing paddock | Paddock | Four runs of wattle fence, a field gate, a water trough, a hay bale, a feed sack | 8 |
| Terraces: one at the end of each bench (5), and at (240, 700) and (205, 790) | Terrace corner | A rowan or blossom tree, a hay bale, three barley clumps, a stile in the wall | 6 each, 42 |
| Terraces: (255, 760) and (225, 690) | Scarecrow | A scarecrow, two barley clumps | 3 each, 6 |
| Greywall Quarry floor | Quarry | The quarry face, the derrick, four stacks of cut blocks, a bench, a hammer, a shovel, three quarry spoil heaps, a log pile, a hand lantern, a cart | 15 |
| Larch Hangers: the slide foot (200, 832) and the crest bench (225, 888) | Felling | A log pile, two fallen logs, three stumps, a felling axe, a saw | 8 each, 16 |
| Larch Hangers: down the south face from the crest (215, 880) to (200, 832) | Slide | The sawyers' log slide | 1 |
| The first sink's rim, at three places round (212, 612) | Gravelkin spoil | Two Gravelkin spoil heaps, a stolen-sack pile, a crate, a junk pile, a candle cluster | 6 each, 18 |
| Each of the four pits | Farmers' warning | Two rag warning poles, a tilted fence run | 3 each, 12 |
| Sunbank gate (400, 818) | Gate | Two gate piers, a field gate standing open, two wall ends, two lamp posts, a milestone, a signpost | 9 |
| Hopstead: the green | Green | The moot-stone, a well, four lamp posts, three trees, two benches, a notice board | 12 |
| Hopstead: market stall | Market | Three market stalls, a loaf, a cheese wheel, an apple basket, cabbages, turnips, a sausage string, a barrel | 10 |
| Hopstead: *The Dry Boot* | Inn front | Three barrels, two benches, a tavern table, a hanging lantern, tankards | 8 |
| Hopstead: brewhouse | Cask yard | Five ale casks, a cart, a hand lantern | 7 |
| Hopstead: smithy on the green | Smithy front | The anvil, a cart with a wheel off, a work bench, a hammer, a water trough, a barrel | 6 |
| Hopstead: tan-yard | Tan-yard | Three drying racks, two washing tubs, a hide rug | 6 |
| Hopstead: weaving-house, cottage at the lane end | Cottage garden | Two runs of picket fence, a flower bed, a bench, a clay jar | 5 each, 10 |
| Hopstead: physic garden | Physic garden | Four plots edged with wattle fence, two flower beds, a bench, two clay jars | 9 |
| Hopstead: each mill | Mill door | Three grain sacks, a cart, a barrel | 5 each, 10 |
| Hop-kiln and hop-yard gate | Kiln yard | Three picking baskets with ladders, a hop-string bundle, a cart, two sacks, a field gate | 8 |
| Hop-Yards: one at each headland (6) | Headland | A picking basket and ladder, a hop-string bundle, a sack | 3 each, 18 |
| Hop-Yards: north-west corner (225, 1095) | Blighted corner | The blighted bine corner | 1 |
| The herb banks, at three places | Herb bank | Two wattle hurdles, a drying rack, two flower clumps | 5 each, 15 |
| Mill-pool (528, 798) | Angler's bank | A bench, a barrel, a fish basket, a hand lantern, a crate | 5 |
| Ridgefold: sheep-fold and lambing shed | Fold | The sheep-fold, four wattle hurdles, a water trough, two hay bales, a feed sack | 9 |
| The High Fold (735, 950) | Empty fold | The sheep-fold with its gate broken, three thrown hurdles, a tipped trough | 5 |
| High Pastures: lower camp (790, 962), middle camp (840, 975), upper camp (790, 1052) | Rustler camp | Two rustler tents, a campfire with a spit, two bedrolls, a crate, a sack pile, a weapon rack, a stool | 9 each, 27 |
| High Pastures: upper camp | Stolen-sheep pen | The stolen-sheep pen | 1 |
| Each of the four bothies | Bothy door | A wood pile, a bench, a barrel, a shovel | 4 each, 16 |
| Ridge top (850, 1062) | Beacon | The ridge beacon cairn | 1 |
| Brewery yard | Brewery yard | Three barrel stacks, a cart with a wheel off, four ooze puddles, a run of rubble wall with a gap, two burst vats | 11 |
| Brewery yard gate (328, 1162) | Lane end | A cart, two ale casks, a hand lantern, a lamp post | 5 |
| Adit spoil banks (140, 1022) | Spoil banks | Three adit spoil banks, a length of rail, an ore cart, two hanging lanterns, a timber prop stack, the bear den with bones | 9 |
| Adit door (0, 800) | Adit door | Two lamp posts, an ore cart, a tool rack, a crate | 5 |
| Bouldergate arch (312, 1306) | Pass gate | The hill-dwarf gate arch, two lamp posts, a milestone | 4 |
| Sluice hut (600, 1046) | Sluice hut | A work bench, two crates, a barrel, a hand lantern, a bucket | 6 |
| Dam foot (790, 1205) | Dam foot | The dam face stair, two lamp posts, a crate stack, a barrel | 5 |

Within 60 m of the start point stand the seven Sunbank sets, 58 props, beside the buildings, the walls and the trees.

Ambient life, with no quests: sheep and lambs in the lambing paddock, on the bowl's east meadow and at Ridgefold; chickens in Sunbank's yard; two farmhands at work on the terraces and one at the hop-kiln.

## Walking distances

Along the roads above, from the start point and from Hopstead's green, at 6.4 m/s.

| From | To | Distance | Time |
|---|---|---|---|
| Start point | Steadwife Sunbank, on the longhouse porch | 14 m | 2 s |
| Start point | Nearest Highland Buzzard | about 65 m | 10 s |
| Start point | The first sink's mouth | 150 m | 23 s |
| Start point | Feral Billies, upper benches | about 150 m | 23 s |
| Start point | Greywall Quarry | 185 m | 29 s |
| Start point | Hopstead's green | 290 m | 45 s |
| Hopstead | The herb banks | 150 m | 23 s |
| Hopstead | Hop-Blight Beetles | about 210 m | 33 s |
| Hopstead | Ridgefold | 180 m | 28 s |
| Hopstead | The High Fold | 285 m | 45 s |
| Hopstead | Ridge top, Old Bitterhorn | 445 m | 70 s |
| Hopstead | Brewmaster Maltby | 300 m | 47 s |
| Hopstead | Shale Bears at the Adit's spoil banks | about 340 m | 53 s |
| Hopstead | The first sink's mouth, by the gate and Sunbank | 440 m | 69 s |
| Hopstead | Bouldergate Pass | 525 m | 82 s |
| Hopstead | Daleside Adit door | 510 m | 80 s |
| Hopstead | Dam foot | 485 m | 76 s |

The quest flow line is the zone page's flow walked along these roads with its returns: Sunbank and the bowl (ST-01 to ST-07), to Hopstead (ST-08), the hop-yards and herb banks (ST-09, ST-10), Ridgefold, the High Pastures and the ridge top (ST-11, ST-12, ST-15, ST-17), the Old Brewery and on by the Foot Path to the Adit (ST-13, ST-14), back into the bowl for the Deep Sink (ST-16), then out by a pass (ST-18). Summed from this table it is about 4.9 km, where the same sum on the layout before gives about 10.2 km and the walk grid measured 8.9 km; so the built zone should measure about 4.3 km. The target is about 4 km and no more than 4.5 km, 8 to 12 minutes of running, and it is measured on the built zone.

---

# Stoneheart Deeps

| | |
|---|---|
| Footprint and offset | 900 × 1,000 m · Khazrun (200, 5000) |
| Structure | Three cavern levels stacked under Mount Khaz. **U** Upper Galleries at +80 m · **G** the Great Cavern at 0 m (800 m across, 120 m ceiling) · **W** the Underworks at −70 m. Positions are given as level and (x, z) |
| Landmark | Lanternhold's lamps on the north wall of the Great Cavern, visible from everywhere on level G |
| Exits | Long Stair up to Hammerdeep's Deepgate (U 500, 1000) · Daleside Adit to Stonewake Dale (U 900, 400) · Deep Gate rail-tunnel to Ironroot (W 500, 0) |
| Links between levels | Long Stair (U → G at Lanternhold) · Lanternhold lift (G ↔ W) · Trestle rail-ramps (G ↔ W) · Underwarren tunnels (U ↔ G ↔ W, hostile) · Crystal Galleries stair (U ↔ G) |

```
 Side view, looking east            north (Hammerdeep) -->
 +80  U  [Adit]---Upper Galleries---Crystal Galleries (upper)---[Long Stair top]
                \                         |stair                    /
   0  G   Glowcap Grotto -- Junction -- Crystal Galleries -- LANTERNHOLD
            |underwarrens|      \trestles                       |lift
 -70  W  [Deep Gate]--Runaway Line--------Shattered Hall----the Undercut
```

## Sub-areas

| Code | Sub-area | Level | Centre | Size | Terrain |
|---|---|---|---|---|---|
| LS | The Long Stair | U → G | (500, 960) → (460, 840) | 60 wide, 220 m of stair in 4 flights | Carved stair with lamp-niches and landings |
| LH | Lanternhold | G | (450, 800) | 240 × 160 | Hall-town built into the north cavern wall on 3 terraces; lower gate at (450, 720) |
| GG | Glowcap Grotto | G | (230, 540) | 320 × 360 | Mushroom forest; tending-ring at (300, 620); deep grotto at (120, 420) |
| CJ | Cartwright's Junction | G | (600, 540) | 160 × 160 | Rail yard and turntable |
| TS | The Trestles | G → W | (720, 340) | 240 × 300 | Timber rail viaducts over a chasm; wrecked carts on the lower spans |
| UW | Gravelkin Underwarrens | U ↔ W | (320, 260) | 300 × 300 footprint, about 300 m of tunnel on 3 levels | Round gnawed tunnels; Krakk's chamber at the bottom |
| UG | Upper Galleries | U | (600, 480) | 500 × 300 | Worked-out copper galleries from the Adit to the Crystal stair |
| CG | Crystal Galleries | U and G | (790, 720) | 200 × 360 | Geode caverns; assay bench at (760, 640) on G; 12 gallery pillars |
| SH | The Shattered Hall | W | (240, 760) | 260 × 240 | Collapsed ancestral hall; sealed threshold at (330, 700) |
| RL | The Runaway Line | W | (460, 420) | 420 × 160 | A long straight of track with sidings; signal hut at (560, 470) |
| UC | The Undercut | W | (690, 800) | 320 × 320 | Six bore mouths in an arc, drafting-tent on a side ledge, ventilation crawl along the east wall, the Great Bore chamber at the north end |
| DG | Deep Gate | W | (500, 60) | 120 × 120 | Rail-head and tunnel mouth |

## Hubs

| Hub | Centre | Radius | Buildings and spots |
|---|---|---|---|
| Lanternhold | G (450, 800) | 110 | Warden's balcony, top terrace (0, +50) · *The Trimmed Wick* (−40, +20) · hall kitchen (−20, +35) · still-room (+40, +30) · market gallery (+10, 0) · wick-loft (+70, +10) · lower terrace hide-worker (−80, −20) · sick-hall (+90, −10) · drill gallery (−60, −40) · lower gate and Sapper-Sergeant (0, −80) · lift to the Underworks (+110, −60) · wanted board at the gate · mailbox by the inn · graveyard (−130, −30) |
| Cartwright's Junction | G (600, 540) | 50 | Turntable (0, 0) · rail-forge (+30, +20) · cart platform (−20, −25) |
| Mine-cart stops | Lanternhold lower gate · Junction · Deep Gate | — | 45 seconds a leg |

## Points

| Point | Position | Used by |
|---|---|---|
| Lamp-keeper Wickfast | U (500, 970), top landing | SD-02 |
| Ore Crates in wrecked carts (12) | TS lower spans | SD-06 |
| Shard-Chief Krakk | UW bottom chamber, W (330, 200) | SD-07 |
| Gallery Pillars (6 with charges) | CG, G level | SD-09 |
| Thane's threshold (Ancestor-speaker) | W (330, 700) | SD-10, SD-11 |
| Rune-wright's signal hut | W (560, 470) | SD-12 |
| Bore Mouths (6) | UC arc, W (560–820, 700–760) | SD-14 |
| Survey Plans | Drafting-tent, W (820, 840) | SD-16 |
| Vigga Deepdrill and the Great Bore (3 valves) | W (690, 930) | SD-17 |
| Fusewright Odd | Powder magazine, W (590, 880) | SD-19 |
| Old Blindmaw | Deep grotto, G (120, 420) | SD-18 |
| Glimmerqueen (rare) | 3 geodes in CG | — |
| Graveyards | Lanternhold (320, 770) · Junction (650, 600) · Underworks lift foot, W (560, 740) | — |
| Chests (one active) | Underwarren chamber · Shattered Hall dais · trestle cart · Undercut crawl | — |

## Spawn camps

| Camp | Creature | Count | Where | Notes |
|---|---|---|---|---|
| SD-S01 | Lanternwing Bat | 24 | LS niches and UG | |
| SD-S02 | Rail Rat | 16 | TS and CJ sidings | Pairs |
| SD-S03 | Glowcap Shambler | 20 | GG, spread | |
| SD-S04 | Pale Cave Bear | 16 | GG west half | |
| SD-S05 | Gravelkin Underdweller | 24 | UW upper and middle tunnels | |
| SD-S06 | Gravelkin Shardchewer | 14 | UW lower tunnels and TS lower spans | |
| SD-S07 | Crystal Skitterer | 20 | CG, both levels | Camouflaged on walls |
| SD-S08 | Restless Ancestor | 24 | SH | |
| SD-S09 | Rogue Rail-Golem | 18 | RL, patrolling the track | Charge along the rails |
| SD-S10 | Rock Borer | 16 | RL sidings and the tunnel to DG | Burrowed |
| SD-S11 | Geode Sprite | 18 | CG lower level and the stair | |
| SD-S12 | Slagborn Tunneler | 18 | UC bore mouths, 3 each | Plus scripted spawns at 2 pillars |
| SD-S13 | Slagborn Blastwright | 14 | UC: 4 ventilation crawl, 10 main bore | |

## Nodes

| Node | Positions | Where |
|---|---|---|
| Copper Vein | 18 | UG |
| Tin Vein | 26 | CG 18 · UW 8 |
| Silver Vein | Replaces a tin vein in CG 12% of the time | |
| Dewleaf | 10 | GG |
| Glowcap (cooking) | From Shamblers only | |
| Fishing | None | |

## Routes

| Route | Path |
|---|---|
| Lantern Road (lit, safe) | Long Stair → Lanternhold → Junction → Trestle upper span → Adit branch up to U |
| Grotto Path (lit to the tending-ring) | Lanternhold → (300, 620) |
| Gallery Stair | Junction → Crystal Galleries G → U |
| Lower Road (lamps out; lit again after SD-17) | Lanternhold lift foot → Shattered Hall threshold, and → Runaway Line → Deep Gate |
| Bore Road | Lift foot → the Undercut |
| Rail | Lanternhold lower gate → Junction → Trestles ramp down → Runaway Line → Deep Gate → tunnel to Ironroot |
