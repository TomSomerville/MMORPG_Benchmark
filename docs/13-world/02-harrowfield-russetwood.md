# World Layout — Harrowfield and Russetwood

[← World Layout Index](00-world-layout.md) · Zones: [Harrowfield](../05-zones/t2-harrowfield.md) · [Russetwood](../05-zones/t2-russetwood.md) · Prev: [Brightmead and Embercrag](01-brightmead-embercrag.md) · Next: [Stonewake and Stoneheart](03-stonewake-stoneheart.md)

Notation and rules are in the [index](00-world-layout.md). Each grid cell is 140 m.

# Harrowfield

| | |
|---|---|
| Size and offset | 1,400 × 1,400 m · Meridia (1800, 1600) |
| Shape | Open farmland tilting gently east to the sea. A low hill in the middle, a quarry pit in the north-west, a walled manor on a rise in the north-east |
| Elevation | Fields 0–12 m · Scarecrow Hill 30 m · Vane Manor rise 22 m · quarry floor −18 m · beach 0 m |
| Landmark | The bare tree on Scarecrow Hill (700, 800) |
| Exits | South → Brightmead (300, 0) · west → Russetwood, open edge at (0, 500–800) · north → Thornwick by the Old Tollbridge (600, 1400) |

```
      A  B  C  D  E  F  G  H  I  J
 10   ## .. .. .. TB .. .. VM VM ~~
  9   ## .. .. .. .. BR BR VM VM ~~
  8   ## DQ DQ .. .. BR BR .. LS ~~
  7   ## DQ DQ .. .. .. .. .. LS ~~
  6   ## DQ .. .. SH SH .. .. LS ~~
  5   .. .. .. .. SH SH RR RR LS ~~
  4   .. .. .. HC .. .. RR RR LS ~~
  3   ## .. GF HC .. FF .. RR .. ~~
  2   ## GF GF GF .. FF .. .. .. ~~
  1   ## .. GF .. .. .. .. .. .. ~~
```

## Sub-areas

| Code | Sub-area | Centre | Size | Elevation and terrain |
|---|---|---|---|---|
| HC | Harrow's Cross | (490, 450) | 200 × 200 | Town at the crossing of the King's Road and the east–west cart road |
| GF | The Gleaning Fields | (330, 220) | 420 × 380 | Stubble fields, stooks, Bramblethorn hedges |
| FF | Fenner Farmstead | (760, 300) | 180 × 200 | Farmhouse, barn, turnip field to the east |
| RR | Reaver's Row | (950, 520) | 300 × 380 | A dry ditch running north–south with shanties along both banks; the captain's wagon at the centre |
| SH | Scarecrow Hill | (700, 770) | 300 × 260 | Rounded hill, poles in rows up the slope |
| LS | Longstrand | (1220, 780) | 180 × 700 | Shingle beach below a 10 m bluff; three Gillkin villages; jetty at (1210, 560) |
| DQ | Dustwater Quarry | (250, 980) | 300 × 400 | Stepped pit, a ramp spiralling down, flooded sump at the bottom (scenery) |
| BR | The Burning Rows | (820, 1160) | 300 × 260 | Burning field strips; smoke plume |
| VM | Vane Manor | (1080, 1280) | 260 × 240 | Walled estate: gatehouse south, hall, east wing with the study, servants' stair on the north side |
| TB | Old Tollbridge | (600, 1380) | 120 × 60 | Stone bridge over the border stream; militia tent on the south bank |

## Hubs

| Hub | Centre | Radius | Buildings and spots |
|---|---|---|---|
| Harrow's Cross | (490, 450) | 100 | Moot-hall (0, +50) · militia yard and stores (−60, +20) · *The Gleaner's Cup* (+30, 0) · eyrie on the tithe barn (+70, +60) · alchemist on the crossroads (−10, −15) · smithy and room above (−70, −40) · tannery (−95, +70) · weaving shed (+50, −45) · harvest chapel (+85, −10) · hedge-shrine (+110, −60) · militia tent (−40, +55) · notice board at the crossroads · mailbox by the inn · graveyard (−130, +90) |
| Fenner Farmstead | (760, 300) | 50 | Yard (0, 0) · kitchen door (+15, +20) |
| Old Tollbridge | (600, 1380) | 30 | Militia tent (−15, −20) |

## Points

| Point | Position | Used by |
|---|---|---|
| Paymaster Grice's tent and strongbox | (1000, 690) | HF-07 |
| Poached Goods crates (12 positions) | Along the Row | HF-06 |
| "Sweet" Sal's wagon | (950, 520) | HF-19 |
| Old Rattlebones | (700, 800) | HF-18 |
| Fisher Corran's jetty | (1210, 560) | HF-10 |
| Widow Brell's cottage | (1150, 640), on the bluff | HF-11 |
| Quarry-boss Garrow's hut | (330, 800), quarry rim | HF-12 |
| Tinker Marsh's wagon | (680, 1060) | HF-13 |
| Field Fires (12 positions) | BR, spread | HF-14 |
| Sealed Letters (study desk) | (1160, 1300), upper floor | HF-16 |
| Marshal Vane | Great hall (1080, 1290) | HF-17 |
| Mudtusk (rare) | 3 points in the turnip field | — |
| Graveyards | Harrow's Cross (360, 540) · Longstrand bluff (1120, 900) · Tollbridge road (640, 1180) | — |
| Chests (one active) | Reaver's Row shanty · Gillkin north village · quarry floor · manor cellar | — |

## Spawn camps

| Camp | Creature | Count | Where | Notes |
|---|---|---|---|---|
| HF-S01 | Harrow Jackal | 24 | GF, spread | Packs of 2 |
| HF-S02 | Field Harrier | 14 | GF stooks | |
| HF-S03 | Tusked Rooter | 20 | Turnip field @ (860, 300) r110 | |
| HF-S04 | Harrow Reaver Thug | 24 | RR, both banks | |
| HF-S05 | Reaver Poacher | 16 | RR, beside the crates | |
| HF-S06 | Reaver Firestarter | 14 | BR | |
| HF-S07 | Cinderstuffed Scarecrow | 22 | SH slopes | 6 ring Old Rattlebones |
| HF-S08 | Thresher Construct | 12 | BR, patrolling the strips | |
| HF-S09 | Longstrand Netter | 22 | LS, three villages at z = 520, 780, 1040 | |
| HF-S10 | Longstrand Tidecaller | 10 | LS, one or two per village and the north village's shrine | |
| HF-S11 | Quarry Burrowkin Sapper | 18 | DQ upper steps | |
| HF-S12 | Quarry Skink | 18 | DQ lower steps | |
| HF-S13 | Vane Houseguard | 18 | VM: 4 gate and grounds, 10 hall, 4 servants' stair | Packs of 2 |

## Nodes

| Node | Positions | Where |
|---|---|---|
| Copper Vein | 24 | Field banks and the ditch 16 · quarry rim 8 |
| Tin Vein | 12 | DQ steps |
| Dewleaf | 12 | Hedges near RW edge |
| Bramblethorn | 22 | GF hedges, FF, SH |
| Marshbloom | 14 | Longstrand bluff seeps |
| Fishing | Longstrand, whole coast | |

## Roads

| Road | Path |
|---|---|
| King's Road | (300, 0) → Harrow's Cross (490, 450) → (560, 900) → Tollbridge (600, 1400) |
| Cart Road | Russetwood edge (0, 600) → Harrow's Cross → Fenner's (760, 300) → Reaver's Row (900, 420) → jetty (1210, 560) |
| Hill Path | Harrow's Cross → (620, 640) → hilltop (700, 800) |
| Quarry Road | (560, 900) → rim hut (330, 800) → ramp |
| Manor Drive | (560, 1150) → Burning Rows → gatehouse (1080, 1170) |

---

# Russetwood

| | |
|---|---|
| Size and offset | 1,400 × 1,400 m · Meridia (400, 1600) |
| Shape | Rolling forest, open in the south and east ("the Rides"), dense in the west, rising to old growth in the north. A quarried hollow in the north-east holds the Great Kiln |
| Elevation | Rides 5–15 m · Snare Hollow −10 m · High Canopy ground 20 m, walkways +14 m · Mossback Stand 35 m · kiln quarry floor −15 m |
| Landmark | The Great Kiln's smoke at (1240, 1240); at night its glow |
| Exits | South → Brightmead (1100, 0) · east → Harrowfield, open edge at (1400, 500–800) · north → Thornwick by the Old Timber Road (900, 1400) |

```
      A  B  C  D  E  F  G  H  I  J
 10   ## .. .. .. .. .. TR .. GK GK
  9   ## RB RB .. MS MS .. BU GK GK
  8   ## RB RB .. MS MS .. BU BU ..
  7   ## .. HC HC .. .. CC CC .. ..
  6   ## .. HC HC .. .. CC CC .. ..
  5   ## SN SN .. BL .. .. PC .. ..
  4   ## SN SN .. BL .. .. .. .. ..
  3   ## .. .. CR CR CR CH CH .. ##
  2   ## .. CR CR CR CR CH .. .. ##
  1   ## .. .. CR CR .. .. .. .. ##
```

## Sub-areas

| Code | Sub-area | Centre | Size | Elevation and terrain |
|---|---|---|---|---|
| CH | Cooper's Hollow | (920, 360) | 200 × 200 | Clearing with a green; cooperage on the north side |
| CR | The Copperleaf Rides | (620, 250) | 560 × 400 | Open woodland with broad grassy rides |
| BL | Birch's Lodge | (620, 610) | 120 × 140 | Log lodge on a rise, archery butts behind |
| SN | Snare Hollow | (280, 610) | 280 × 280 | Sunken dell; poacher camps; hanging tree at (240, 640); Ketch's cabin at (200, 520) |
| HC | The High Canopy | (420, 900) | 280 × 280 | Giant oaks joined by rope walkways with 3 ladders up |
| RB | Rootgnaw Burrows | (240, 1170) | 280 × 280 | Fallen giants; burrow mouths under the root-plates; about 180 m of tunnel |
| MS | The Mossback Stand | (700, 1180) | 280 × 280 | Old growth; singing-circle at the south edge |
| CC | The Charcoal Clearings | (960, 900) | 280 × 280 | Four smouldering stacks in cut clearings |
| PC | Charcoal-Burners' Camp | (1060, 660) | 100 × 100 | Old Peg's honest camp |
| BU | The Burning Ride | (1110, 1160) | 200 × 260 | A strip of forest alight; a stream on its west side stops the fire |
| GK | The Great Kiln | (1250, 1270) | 260 × 260 | Quarry hollow: cart road in from the south, spoil heaps on the east rim, counting-shed on the north rim, kiln floor at the bottom |
| TR | Old Timber Road gate | (900, 1380) | 120 × 60 | Log-corduroy road; forester post |

## Hubs

| Hub | Centre | Radius | Buildings and spots |
|---|---|---|---|
| Cooper's Hollow | (920, 360) | 100 | Reeve's hall (0, +55) · cooperage and shopfront (−40, +30) · *The Split Stave* and lean-to (+30, 0) · eyrie in the tall beech (+75, +60) · apothecary (−10, −20) · hoop-forge (−75, −35) · tan-pits (−100, +70) · seamstress's cottage (+55, −45) · woodland chapel (+85, −10) · saw-pit (−30, −65) · notice board on the green · mailbox by the inn · graveyard (+130, +80) |
| Birch's Lodge | (620, 610) | 50 | Porch (0, 0) · cook-fire (+20, −15) · butts (−25, +30) · sick-bay (+15, +20) |
| Charcoal-Burners' Camp | (1060, 660) | 30 | Old Peg's stack (0, 0) |

## Points

| Point | Position | Used by |
|---|---|---|
| Bundles of Stolen Pelts (12 positions) | SN camps | RW-06 |
| Odo Ketch's cabin and tally-desk | (200, 520) | RW-07 |
| Garrick Snare | Hanging tree (240, 640) | RW-19 |
| Woodcutter Hewer | Foot of the east ladder (540, 860) | RW-08, RW-11 |
| Hedgewarden Sorrel | (700, 1050) | RW-12, RW-18 |
| Old Mossback | (720, 1230) | RW-18 |
| Ride Fires (12 positions) | BU | RW-14 |
| Kilnmaster's Ledger | Counting-shed (1250, 1380) | RW-16 |
| Kilnmaster Soot | Kiln floor (1250, 1260) | RW-17 |
| Fisher Brook's ford | (1150, 380) | — |
| Red Tom (rare) | 3 points in the Rides | — |
| Graveyards | Cooper's Hollow (1050, 440) · Birch's Lodge (560, 680) · Timber Road (860, 1240) | — |
| Chests (one active) | Snare Hollow camp · burrow chamber · kiln spoil heap · canopy platform | — |

## Spawn camps

| Camp | Creature | Count | Where | Notes |
|---|---|---|---|---|
| RW-S01 | Russet Fox | 24 | CR, spread | |
| RW-S02 | Rutting Stag | 18 | CR west half | |
| RW-S03 | Leafmold Beetle | 20 | CR north edge and around BL | |
| RW-S04 | Woodland Poacher | 24 | SN, 5 camps | |
| RW-S05 | Poacher Trapper | 16 | SN, beside the pelt bundles | |
| RW-S06 | Canopy Weaver | 20 | HC, on and under the walkways | Drop from above |
| RW-S07 | Ashhand Charcoaler | 20 | CC, 5 per stack | |
| RW-S08 | Burrowkin Rootgnawer | 24 | RB, mouths and tunnels | |
| RW-S09 | Mossback Treant | 18 | MS, spread | |
| RW-S10 | Kiln Tender | 14 | BU | |
| RW-S11 | Horned Owl | 16 | BU edges and the stream | Stealthed |
| RW-S12 | Kilnfire Wisp | 18 | CC north and BU south | |
| RW-S13 | Russet Bear | 10 | Between MS and TR | |
| RW-S14 | Great Kiln Guard | 18 | GK: 10 cart road, 4 spoil-heap path, 4 kiln floor | Packs of 2 |

## Nodes

| Node | Positions | Where |
|---|---|---|
| Copper Vein | 20 | Rocky outcrops in CR and SN |
| Tin Vein | 12 | Kiln quarry walls |
| Dewleaf | 30 | Everywhere under trees |
| Bramblethorn | 18 | Clearings: CC, CH edge, BL |
| Marshbloom | 16 | Stream banks: Fisher's ford, BU stream |
| Fishing | Forest streams at (1150, 380) and (1000, 1150) | |

## Roads

| Road | Path |
|---|---|
| Hollow Road | (1100, 0) → Cooper's Hollow (920, 360) → (1150, 500) → Harrowfield edge (1400, 600) |
| Lodge Ride | Cooper's Hollow → Birch's Lodge (620, 610) → Snare Hollow rim (420, 610) |
| Old Timber Road | Cooper's Hollow → (900, 800) → (880, 1150) → gate (900, 1400) |
| Canopy Path | Birch's Lodge → east ladder (540, 860) |
| Burners' Track | (900, 800) → Charcoal-Burners' Camp (1060, 660) and → Charcoal Clearings |
| Kiln Cart Road | (880, 1150) → Burning Ride → kiln gate (1240, 1150) |
