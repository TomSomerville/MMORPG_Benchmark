# World Layout — Brightmead Vale and Embercrag Hollow

[← World Layout Index](00-world-layout.md) · Zones: [Brightmead Vale](../05-zones/t1-brightmead-vale.md) · [Embercrag Hollow](../05-zones/t1-embercrag-hollow.md) · Next: [Harrowfield and Russetwood](02-harrowfield-russetwood.md)

Notation and rules are in the [index](00-world-layout.md).

# Brightmead Vale

| | |
|---|---|
| Size and offset | 1,000 × 1,000 m · Meridia (1300, 600) |
| Shape | A bowl open to the south. Wooded ridge along the west (the mine), low hills along the north, the Silverrun running north to south down the east-centre |
| Elevation | Valley floor 0–10 m · Larkhill knoll 18 m · west ridge 35 m · northern hills 30 m |
| Landmark | The mill's sails at (760, 620), visible from the whole vale; after BM-11 a column of smoke |
| Exits | South gate → Solhaven (500, 0) · north road → Harrowfield (800, 1000) · north-west track → Russetwood (200, 1000) |
| Start point | (250, 205), facing north toward the Warden's lodge |

```
      A  B  C  D  E  F  G  H  I  J
 10   ## .. .. AC AC .. SC .. .. ##
  9   ## GH GH AC AC .. SC SC .. ##
  8   ## GH GH GH .. .. SC SC .. ##
  7   ## GH GH GH .. .. SC BM BM ##
  6   ## .. GH .. .. MB .. BM BM ##
  5   HM HM .. BF BF MB MB .. .. ##
  4   HM HM .. BF BF BF SC .. .. ##
  3   ## LP LP LP BF .. SC .. .. ##
  2   ## LS LS LP .. .. SC .. .. ##
  1   ## .. .. .. .. .. SC .. .. ##
```

## Sub-areas

| Code | Sub-area | Centre | Size | Elevation and terrain |
|---|---|---|---|---|
| LS | Larkhill Steading | (250, 220) | 160 × 140 | Knoll, 18 m; lodge at the top, lane running down east |
| LP | Larkhill Pastures | (320, 330) | 260 × 180 | Rolling grass, dry-stone sheep pens |
| HM | Hartwell Mine | Mouth (130, 450); interior under the west ridge | Surface 180 × 180; interior 3 galleries, about 220 m of tunnel, and Hartwell Deep below | Timbered adit, candle-lit; Deep is a single cavern 45 m across |
| BF | Brightmead Fields | (450, 400) | 300 × 260 | Flat tilled strips, hedges, copper outcrops on the west bank |
| MB | Millbrook | (560, 520) | 180 × 170 | Town on the west bank of the creek, one stone bridge at (640, 520) |
| GH | Greenhollow Woods | (270, 760) | 300 × 380 | Mixed woodland, dense in the north-west; fallen oak at (180, 880) |
| BM | The Burned Mill and Cray's Orchard | (790, 640) | 220 × 220 | Mill on the east bank, a building 9 × 9 m standing just beyond the end of Mill Lane with its door to the lane; orchard rows running east |
| SC | Silverrun Creek | Runs (650, 1000) → (680, 700) → (640, 520) → (620, 300) → (560, 0) | 40 m wide band; Gillkin pool at (700, 840), 90 × 120 | Shallow, wadeable everywhere; willow at (690, 800) |
| AC | Ashhand Camp | (430, 920) | 200 × 160 | Hollow between two hills; palisade open to the south |

## Hubs

| Hub | Centre | Radius | Buildings and spots (offset from centre) |
|---|---|---|---|
| Larkhill Steading | (250, 220) | 60 | Warden's lodge and porch (0, +30) · practice yard (−35, +5) · wayside shrine (+35, +10) · old oak (+45, −30) · store shed (−10, −25) · lodge kitchen (+12, +38) · graveyard (−60, −40) |
| Millbrook | (560, 520) | 80 | Reeve's hall (0, +40) · *The Miller's Rest* (−30, 0) · eyrie platform (+50, +45) · seamstress on the green (+10, −10) · forge (−55, −30) · tannery (−70, +50) · garden plot (+35, −45) · cart-shed workshop (−20, −55) · general store (+30, +15) · mailbox by the inn door · graveyard (−90, +70) |

## Points

| Point | Position | Used by |
|---|---|---|
| Shepherd Dunn's sheepfold | (330, 600) | BM-17 |
| Grain Sacks (10 positions) | Tunneler gallery, second gallery of the mine | BM-07 |
| Hartwell Deep (Hale Morrow) | Lowest cavern; reached by the ramp from the third gallery | BM-16 |
| Kibbler the Candle King (rare) | 3 points in the Candlewarden gallery | — |
| Old Greymaw's patrol | (180, 880) → (230, 930) → (140, 940) | BM-17 |
| Cray's cider press (Miller Cray) | (850, 600) | BM-11–13 |
| Mill yard trigger | (760, 620) r25 | BM-11 |
| Cider Barrels (8 positions) | Orchard rows, (800–900, 560–720) | BM-13 |
| Fisher Rill's cottage | (720, 790) | BM-14 |
| Graveyards | Larkhill (190, 180) · Millbrook (470, 590) · Greenhollow edge (400, 800) | — |
| Chests (one active) | Mine third gallery · Ashhand Camp tent (450, 950) · Gillkin huts (710, 870) | — |

Until Harrowfield and Russetwood are built, the two NPCs who end BM-18 wait inside the vale, each about 15 m in from the exit that leads to their zone and beside its road: Reeve Holt at the north road, Forest-Reeve Birch at the north-west track.

## Spawn camps

| Camp | Creature | Count | Where | Notes |
|---|---|---|---|---|
| BM-S01 | Vale Wolf Pup | 26 | LP, spread | Within 120 m of the lane |
| BM-S02 | Meadow Boar | 22 | BF, spread | |
| BM-S03 | Vale Wolf | 12 | GH south edge @ (300, 620) r90 | |
| BM-S04 | Burrowkin Digger | 26 | HM mouth and first gallery | 8 outside the adit |
| BM-S05 | Burrowkin Tunneler | 14 | HM second gallery | Around the grain sacks |
| BM-S06 | Burrowkin Candlewarden | 10 | HM third gallery | |
| BM-S07 | Greenhollow Spider | 24 | GH, spread | Denser toward the north-west |
| BM-S08 | Ashhand Cutpurse | 18 | BM mill ruin and house @ (770, 630) r50 | 6 more at AC |
| BM-S09 | Ashhand Torchbearer | 10 | BM orchard rows | 6 more at AC |
| BM-S10 | Ashhand Cutpurse | 6 | AC | |
| BM-S11 | Ashhand Torchbearer | 6 | AC | |
| BM-S12 | Ashhand Brander | 5 | AC centre and Hartwell Deep approach | |
| BM-S13 | Silverrun Gillkin | 18 | SC Gillkin pool | Huts in pairs |
| BM-S14 | Creek Snapper | 10 | SC banks from z = 300 to 700 | |

## Nodes

| Node | Positions | Where |
|---|---|---|
| Copper Vein | 22 | West ridge and mine mouth 12 · BF west bank 6 · northern hills 4 |
| Sunpetal | 20 | LP and BF roadsides |
| Hearthroot | 16 | Foot of the west ridge and the northern hills |
| Dewleaf | 12 | GH |
| Fishing | Creek, whole length | No pools at this level |

## Roads

| Road | Path |
|---|---|
| King's Road | (500, 0) → (520, 300) → Millbrook (560, 520) → bridge (640, 520) → (720, 700) → (800, 1000) |
| Larkhill Lane | Larkhill (250, 220) → (380, 300) → joins the King's Road at (520, 300) |
| Mine Track | (380, 300) → (250, 420) → mine mouth (130, 450) |
| Forest Track | Millbrook (520, 580) → (400, 700) → (260, 880) → (200, 1000) |
| Mill Lane | Bridge (640, 520) → the mill's door (760, 620) |

---

# Embercrag Hollow

| | |
|---|---|
| Size and offset | 1,000 × 1,000 m · Khazrun (500, 6800) |
| Shape | A snowbound hanging valley that drops from north-west to south-east. Mount Khaz fills the southern horizon |
| Elevation | Coldhearth 60 m · Frostpine Rise 85 m · Old Forge 40 m · Anvilrest 20 m · Rimewater 5 m. A hanging valley: the land beyond the north edge lies at 85 m and beyond the west edge at 66 m, the valley's own height on those sides; the south and east edges meet the valley floor |
| Landmark | The Old Forge's chimney-stack at (480, 620); dark until EC-16, then a red glow on the snow |
| Exits | Coldgate tunnel → Hammerdeep (300, 0), the inner road running on through Hammerdeep to Stoneheart Deeps · Bouldergate Pass → Stonewake Dale (960, 40) |
| Start point | (250, 765), facing north toward the Warden's hall |

```
      A  B  C  D  E  F  G  H  I  J
 10   ## FR FR FR ## ## ## KC KC ##
  9   ## FR FR FR .. .. .. KC KC ##
  8   ## CH CH .. .. .. .. KC .. ##
  7   GW GW CH .. OF OF .. TR TR ##
  6   GW GW .. .. OF OF .. TR TR ##
  5   ## .. .. .. .. AR .. TR TR ##
  4   ## .. .. .. AR AR .. .. .. ##
  3   ## .. .. .. .. .. RP RP .. ##
  2   ## .. .. .. .. .. RP RP .. ..
  1   ## ## .. .. ## ## ## ## .. ..
```

## Sub-areas

| Code | Sub-area | Centre | Size | Elevation and terrain |
|---|---|---|---|---|
| CH | Coldhearth Camp | (250, 780) | 160 × 140 | Palisaded shelf, 60 m; hall at the north end |
| FR | Frostpine Rise | (290, 920) | 300 × 160 | Steep snow slope with frostpines |
| GW | Gravelkin Warrens | Mouth (150, 690); interior under the camp, running in north-east from the mouth within (70–345, 610–850) | Surface 160 × 160; interior 3 chambers, about 200 m of tunnel, deep warren 40 m across below | Round gnawed tunnels; the mouth opens in a mound 9 m high. The hole in the larder floor is a pit of its own under the larder, not joined to the warren |
| OF | The Old Forge | (480, 640) | 180 × 180 | Open stone platform with the firebed at its centre |
| AR | Anvilrest | (540, 430) | 180 × 170 | Stone town on a terrace above the pond |
| TR | Tuskfall Ridge | (810, 600) | 200 × 300 | Rocky spine with ledges; copper outcrops. Its feet (the cart road, the graveyard) lie at 30 m and the spine stands 34 m over them |
| RP | Rimewater Pond | (690, 260) | 200 × 180 | Frozen pond 170 × 150, ice to walk on; 4 ice-fishing holes |
| KC | Kiln Cave | Mouth (850, 880); approach (790, 800); interior running north-west from the mouth within (690–900, 870–1000) | Approach 180 × 200; interior a hall 43 m across and, beyond it, Sootbeard's chamber 30 m across, about 80 m of tunnel, about 160 m from mouth to back | Soot-blackened; ledges for lookouts; the mouth opens in a mound 9 m high |

Kiln Cave runs north-west so that its back stays within 450 m of the Tuskfall foot graveyard. The Slagborn shoot and cast, so its hall is wide: each creature in it is given 150 m² of floor, and those who stand along its wall are out of each other's notice.

## Hubs

| Hub | Centre | Radius | Buildings and spots |
|---|---|---|---|
| Coldhearth Camp | (250, 780) | 60 | Warden's hall and hearth (0, +30) · the ring (−35, 0) · hearth-shrine (+35, +10) · standing stone (+53, −20), beside the Forge Road where it leaves the camp · larder (−12, −28), with a hatch in its floor to the pit beneath · adit mouth (−70, −60) · graveyard (+70, −50) |
| Anvilrest | (540, 430) | 80 | Forge-hall (0, +40) · *The Banked Coal* (−30, 0) · eyrie ledge (+55, +50) · drying racks (−60, +45) · brewhouse (+30, −40) · loom-house (+10, −10) · cart-works (−20, −55) · stores (+35, +15) · mailbox by the inn · sheltered south wall (+5, −72), the south edge of the terrace · graveyard (−95, +60) |

## Points

| Point | Position | Used by |
|---|---|---|
| Cold Firebed | (480, 640) | EC-07 |
| Sooty Footprints (3 triggers) | (560, 690) → (660, 740) → (760, 790) | EC-11 |
| Scout Brynja's boulder | (800, 830) | EC-11, EC-12 |
| Grolm Sootbeard | Middle of Sootbeard's chamber in Kiln Cave, before the crucible | EC-16 |
| Slag Crucible (Ever-Ember) | Back of Kiln Cave: against the far wall of Sootbeard's chamber, behind him | EC-16 |
| Grawl the Boulder-Eater | Deep warren, past the second rock-fall | EC-17 |
| Whitepelt (rare) | 3 ledges on Tuskfall Ridge | — |
| Ice-fisher's hut | (700, 300) | — |
| Graveyards | Coldhearth (320, 730) · Anvilrest (445, 490) · Tuskfall foot (720, 520) | — |
| Chests (one active) | Second warren chamber · Kiln Cave ledge · ridge top (840, 700) | — |

Until Stonewake Dale and Stoneheart Deeps are built, the two NPCs who end EC-18 wait inside the hollow, each about 15 m in from the exit that leads to their zone and beside its road: Dale-Reeve Stonewake at Bouldergate Pass, Hallwarden Lampwright at the Coldgate tunnel, since the road to the Deeps runs through Hammerdeep.

## Spawn camps

| Camp | Creature | Count | Where | Notes |
|---|---|---|---|---|
| EC-S01 | Rime Wolf Cub | 26 | FR, spread | |
| EC-S02 | Crag Ram | 22 | FR east half and the slope down to OF | |
| EC-S03 | Rime Wolf | 12 | Between OF and TR @ (640, 620) r90 | |
| EC-S04 | Gravelkin Scrabbler | 26 | GW mouth and first chamber | 8 outside |
| EC-S05 | Gravelkin Gnasher | 12 | GW second chamber | |
| EC-S06 | Gravelkin Rockchucker | 24 | TR west ledges above the cart road | |
| EC-S07 | Snowshoe Lynx | 20 | TR upper ledges | Stealthed |
| EC-S08 | Tuskfall Boar | 18 | TR east foot @ (880, 520) r90 | |
| EC-S09 | Rimewater Sprite | 16 | RP, on the ice | |
| EC-S10 | Slagborn Lookout | 20 | KC approach ledges and cave mouth @ (805, 835) r55, and inside | 12 outside · 6 in the hall · 2 on the ramp to Sootbeard's chamber, who are his two guards |
| EC-S11 | Slagborn Firebrand | 12 | East side of the KC approach, (812–898, 728–878), and inside | 10 outside, no two within 30 m of each other and all clear of Scout Brynja's boulder · 2 in the hall |

## Nodes

| Node | Positions | Where |
|---|---|---|
| Copper Vein | 22 | TR 14 · GW mouth 4 · OF platform edge 4 |
| Sunpetal | 14 | South-facing slopes below AR |
| Hearthroot | 14 | Foot of TR and the terrace walls |
| Dewleaf | 10 | Under the frostpines |
| Fishing | 4 ice holes on RP | |

## Roads

| Road | Path |
|---|---|
| Forge Road | Coldhearth (250, 780) → Old Forge (480, 640) → Anvilrest (540, 430) |
| Coldgate Road | Anvilrest → (420, 250) → Coldgate (300, 0) |
| Cart Road | Anvilrest → east below the stores (612, 420) → (700, 520) → round the south foot of TR (790, 425) → (868, 310) → (884, 200) → (938, 138) → Bouldergate (960, 40) |
| Kiln Track | Old Forge → (660, 740) → Kiln Cave approach (790, 800) |
