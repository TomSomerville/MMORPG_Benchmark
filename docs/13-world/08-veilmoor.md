# World Layout — Veilmoor

[← World Layout Index](00-world-layout.md) · Zone: [Veilmoor](../05-zones/t4-veilmoor.md) · Prev: [The Riftlands](07-riftlands.md) · Next: [Capitals and instances](09-capitals-and-instances.md)

Notation and rules are in the [index](00-world-layout.md). Each grid cell is 240 m.

| | |
|---|---|
| Size and offset | 2,400 × 2,400 m · Meridia (2700, 5600) |
| Shape | Rolling moor rising from the south-west to the keep in the north-east. Fog limits sight to about 90 m everywhere except on the lit road and the high ground |
| Elevation | Lanternwatch 20 m · Low Tarn 5 m · Cairn 45 m · Barrowfield 50–70 m · Hangman's Hill 85 m · Cairn Heights 110 m · Vigil's End 95 m · Hollowspire 140 m |
| Landmark | By day nothing; that is the point. The line of road-lanterns is the navigation. From high ground, the lit windows of Hollowspire Keep at (2150, 2250) |
| Exits | South-west → Thornwick, Lantern Road (100, 0) · south → the Riftlands (1500, 0) · north: the Long Barrow ridge, sealed |
| Lit road | Lanterns every 40 m. Within 15 m of a lit lantern no hostile creature spawns or paths |

```
      A  B  C  D  E  F  G  H  I  J
 10   ## .. .. .. .. CH .. .. HG HG
  9   ## .. .. .. .. CH CH VE HG HG
  8   ## .. .. .. .. CH .. VE .. ##
  7   ## .. .. .. .. .. BF BF .. ##
  6   ## .. GH GH .. .. BF BF .. ##
  5   ## .. GH .. PC .. BF .. .. ##
  4   ## .. .. .. PC .. .. HH HH ##
  3   ## .. LT LT .. .. .. HH HH ##
  2   ## LW LT LT .. .. .. .. .. ##
  1   LW LW .. .. .. .. .. .. .. ##
```

## Sub-areas

| Code | Sub-area | Centre | Size | Elevation and terrain |
|---|---|---|---|---|
| LW | Lanternwatch | (330, 330) | 260 × 260 | Walled town; beacon tower at its centre |
| — | The Lantern Road | Lanternwatch → Cairn → Vigil's End | 15 m lit corridor, 3,100 m long | West stretch (6 dark lanterns) between (500, 500) and (800, 800) |
| LT | Low Tarn and the Peat Cuts | (720, 520) | 460 × 460 | Black tarn with a stilt hut in the middle, reached by stepping-logs; peat cuts along the west shore |
| PC | Pilgrim's Cairn | (1100, 1080) | 200 × 300 | Shrine and hostel around a great cairn |
| GH | Gloomhollow | (660, 1340) | 440 × 440 | Three bat caves in a limestone scar |
| BF | The Barrowfield | (1560, 1440) | 480 × 660 | 14 mounds; the great mound at (1600, 1500); a barrow-spring at (1480, 1300) |
| HH | Hangman's Hill | (1880, 860) | 440 × 440 | Bare hill crowned by the oak at (1900, 900); Blightwatchers' camp at (1700, 700); overlook at (1840, 800) |
| CH | Cairn Heights | (1300, 2100) | 300 × 640 | Rocky ridge of stacked stones |
| VE | Vigil's End | (1780, 2040) | 220 × 300 | Siege camp below the keep |
| HG | Hollowspire Grounds | (2100, 2180) | 440 × 440 | Dead gardens, outer wards with 4 pylons; **dungeon portal at the keep gate (2180, 2280)** |

## Hubs

| Hub | Centre | Radius | Buildings and spots |
|---|---|---|---|
| Lanternwatch | (330, 330) | 120 | Gate-lamp, east gate (+110, 0) · lamp-store (+20, +40) · drying-loft (−40, +60) · peat-yard (−80, −30) · *The Last Light* (0, 0) · beacon tower eyrie (0, +20) · lamp-forge (+50, −50) · chandlery (−30, −40) · watch-house (+70, +30) · mailbox by the inn · graveyard (−150, +70) |
| Pilgrim's Cairn | (1100, 1080) | 80 | The Cairn and shrine (0, 0) · tent of rubbings (+40, +30) · pilgrim hostel (−40, 0) · cairn-top perch eyrie (0, +15) · roadside stall (+30, −40) · font (−10, −20) · mailbox · graveyard (−110, −60) |
| Vigil's End | (1780, 2040) | 100 | Command pavilion (0, +30) · unmarked tent behind the farrier (−60, −20) · sutler's wagon (+30, −30) · standard-pole eyrie (+50, +50) · siege train (−30, −60) · surgery (+70, 0) · cook-fire (0, −40) · chapel-tent (−70, +40) · mailbox · graveyard (−140, −30) |
| Blightwatchers' camp | (1700, 700) | 40 | Aelar's fire |

## Points

| Point | Position | Used by |
|---|---|---|
| Dark Road-Lanterns (6) | Every 60 m from (520, 520) to (780, 780) | VM-06 |
| Peat Brick Stacks (16 positions) | West shore of the tarn | VM-10 |
| Grizelda Pondwife's hut | (760, 540) | VM-08 |
| Lost watchmen | Cairn at (300, 760) (two alive) · (360, 900) (the fallen one) | VM-09 |
| Mistcat Matriarch | (340, 840) | VM-09 |
| Unblessed Graves (4) | (1220, 1180) · (1320, 1260) · (1400, 1340) · (1460, 1220) | VM-21 |
| Rag-Marked Veilshade (14 positions) | Fog hollows around LT and GH | VM-22 |
| Hrothmund, the Barrow-King | Great mound (1600, 1500) | VM-15 |
| Barrow-spring (class quests) | (1480, 1300) | CQ-FIG-30, CQ-CLE-20 |
| Grimroot | (1900, 900) | VM-35 |
| Ward-Pylons (4) | (1980, 2080) · (2080, 2000) · (2200, 2100) · (2040, 2260) | VM-28 |
| Garden Ghostlily (12 positions) | HG dead gardens | VM-34 |
| Ser Cadoc the Unhorsed (rare elite) | 3 points in the grounds | — |
| The Lamplighter's Ghost (rare) | 3 lanterns on the west stretch, at night | — |
| Memorial Stones (5) | (1700, 1900) · (1620, 2140) · (1500, 2280) · (1900, 2340) · (1300, 2360) | VM-36 |
| Graveyards | Lanternwatch (180, 400) · Tarn road (900, 700) · Cairn (990, 1020) · Barrowfield edge (1380, 1560) · Hill road (1640, 1000) · Vigil's End (1640, 2010) · Gloomhollow (820, 1200) | — |
| Chests (one active per band) | 20–24: peat cut, bat cave, tarn island · 25–30: barrow chamber, heights cairn, garden pavilion | — |

## Spawn camps

| Camp | Creature | Count | Where | Notes |
|---|---|---|---|---|
| VM-S01 | Moor Hound | 26 | Both sides of the road from LW to the west stretch | Packs of 2 |
| VM-S02 | Mistcat | 20 | North spur (300–400, 600–900) and road verges | Stealthed |
| VM-S03 | Bog Wisp | 20 | LT shore and the west stretch | |
| VM-S04 | Drowned Pilgrim | 28 | LT peat cuts and the barrow road | |
| VM-S05 | Moor Hag | 22 | LT east shore and the fog hollows north of it | Each with a wisp |
| VM-S06 | Gloom Bat | 20 | GH, three caves | |
| VM-S07 | Barrow Wight | 26 | BF outer mounds | |
| VM-S08 | Barrow Guardian | 22 | BF great mounds, at the doors | Packs of 2 |
| VM-S09 | Grimroot Sapling | 24 | HH slopes | |
| VM-S10 | Cairn Gargoyle | 20 | CH | Perched; pairs |
| VM-S11 | Hollowed Knight | 26 | HG outer wards and the keep road | |
| VM-S12 | Hollowed Courtier | 22 | HG gardens | Groups of 3 |
| VM-S13 | Spectral Handmaiden | 18 | HG inner gardens | |
| VM-S14 | Hollowspire Sentinel | 26 | HG: 8 at the pylons (2 each), 18 on the walks | |

## Nodes

| Node | Positions | Where |
|---|---|---|
| Iron Deposit | 40 | Gloomhollow scar 12 · Cairn Heights 16 · Hill 12 |
| Gold Vein | Replaces iron 6% of the time | |
| Starmetal Deposit | 8 | Barrowfield mounds |
| Wyrmtongue | 18 | Tors on Cairn Heights and the Hill |
| Veilshade | 30 | Fog hollows across the zone |
| Ghostlily | 14 | Hollowspire Grounds |
| Fishing | Moor pools at (980, 1100), (500, 1000), (1200, 600); 6 pool positions | |

## Roads

| Road | Path |
|---|---|
| The Lantern Road (lit) | Thornwick pass (100, 0) → Lanternwatch east gate (440, 330) → west stretch → (900, 900) → Pilgrim's Cairn (1100, 1080) → barrow road (1400, 1500) → (1600, 1800) → Vigil's End (1780, 2040) |
| Keep Road (unlit) | Vigil's End → outer wards → keep gate (2180, 2280) |
| Tarn Path | Lanternwatch → peat cuts → stepping-logs to the hut |
| Riftlands Track (lit to the zone edge) | Cairn → (1300, 600) → (1500, 0) |
| Hill Path | Riftlands Track at (1400, 700) → Blightwatchers' camp → overlook |
| Heights Track | (1600, 1800) → Cairn Heights (1300, 2100) |
| North Spur | Lanternwatch north gate → (300, 760) |
