# World Layout — Index and Rules

[← Master Plan](../../MASTER_PLAN.md) · Design: [World & Travel](../01-world/world-and-travel.md) · Zones: [Leveling Path](../05-zones/00-leveling-path.md)

Where everything is. For each zone: its size and place on the continent, a grid map, every sub-area with its position and terrain, every hub with its buildings, every quest location, every spawn camp with its creature count, gathering node counts, graveyards and roads. This is the brief the zone builder works from; the terrain is sculpted to fit it.

| File | Covers |
|---|---|
| [01-brightmead-embercrag.md](01-brightmead-embercrag.md) | Brightmead Vale, Embercrag Hollow |
| [02-harrowfield-russetwood.md](02-harrowfield-russetwood.md) | Harrowfield, Russetwood |
| [03-stonewake-stoneheart.md](03-stonewake-stoneheart.md) | Stonewake Dale, Stoneheart Deeps |
| [04-thornwick-marches.md](04-thornwick-marches.md) | Thornwick Marches |
| [05-ironroot-highlands.md](05-ironroot-highlands.md) | Ironroot Highlands |
| [06-cinderfall-barrens.md](06-cinderfall-barrens.md) | Cinderfall Barrens |
| [07-riftlands.md](07-riftlands.md) | The Riftlands |
| [08-veilmoor.md](08-veilmoor.md) | Veilmoor |
| [09-capitals-and-instances.md](09-capitals-and-instances.md) | Solhaven, Hammerdeep, the three dungeons, the raid, Crownfall, the Dustpit |
| [10-world-construction.md](10-world-construction.md) | How these tables become terrain, textures, scattered nature, buildings, spawn points and interiors, by rule |

## 1. Coordinates and notation

| Rule | Detail |
|---|---|
| Units | Metres. (Gameplay ranges are in yards; 1 yard = 0.9144 m. A 40-yard range is about 37 m.) |
| Zone-local coordinates | `(x, z)`: x runs east from the zone's west edge, z runs north from its south edge. Height comes from the terrain |
| Continent coordinates | Each zone has an offset; continent position = offset + local position |
| Grid maps | Each cell is one-tenth of the zone's width. Columns A–J run west to east, rows 1–10 run **south to north** (row 10 is printed at the top). Cell codes are the sub-area codes in the table below each map; `..` is open country belonging to the nearest sub-area, `##` is impassable border terrain, `~~` is water (scenery only) |
| Sub-area | Centre and size (east–west × north–south). Sub-area boundaries are drawn as polygons in the editor, roughly these rectangles |
| Camp notation | `Creature ×N @ (x, z) r40` means N spawn points scattered within 40 m of that point. "spread" means scattered across the whole sub-area. "pack" means the group is linked and pulls together |
| Hub buildings | Offsets `(+east, +north)` in metres from the hub centre |
| Elevation | Given as low, mid, high with rough metres above the zone's lowest point |

## 2. Rules the layouts follow

| Topic | Rule |
|---|---|
| One world | There are no layers. Each zone exists once, and every player in it shares these spawns and nodes. Crowds are handled by dynamic respawn (down to 15% of the listed time at 150 or more players in a sub-area) and per-player quest objects (see [Architecture](../08-tech/architecture.md#one-world-no-layers)) |
| Spawn counts | For every kill objective of N, the zone has at least 2 × N of that creature (the validator requires 1.5 ×). Starting-zone creatures used by the first three quests have at least 3 × N, because launch crowds gather there |
| Density | Camps hold one creature per 180–350 m² in open country, one per 80–150 m² in caves and buildings. No hostile spawn within 60 m of a hub edge or 25 m of a main road, except where a quest calls for an ambush |
| Level gradient | Creature levels rise with distance from the zone's first hub, so a player can read danger from position |
| Pull size | Outdoor camps are placed so a careful player can pull one creature at a time; pairs are marked "pack". Elite areas use packs of 2–3 |
| Roads | Main roads are 5 m wide and safe. Every quest location is within 150 m of a road or a marked path |
| Graveyards | One at each hub and one for every 600 m of travel between them; none further than 450 m from any quest location |
| Gathering nodes | Each zone lists node **positions**; about 40% are populated at any moment and each respawns in 5–10 minutes |
| Rares | Each rare has 3–4 possible spawn points, listed under "Points"; one is chosen per spawn |
| Chests | 3–5 chest positions per zone tier band inside hostile camps; one active at a time per band |
| Sub-area sizes | Sum to less than the zone, leaving open country between them for roads and breathing room |
| Sightlines | Each zone has one landmark visible from most of it (named in the zone's facts), for navigation without a map |
| Travel times | At run speed (6.4 m/s): a 1,000 m zone is crossed in about 2.5 minutes, a 2,400 m zone in about 6 |

## 3. Meridia

Continent coordinates in metres. The Wildpact deepwoods lie west of x = 400 and the Pale Downs north of z = 8,000; both are sealed by impassable terrain. The planned zones fill the eastern half of the continent only.

| Zone | Size | Offset (x, z) | Borders and crossings |
|---|---|---|---|
| Solhaven | 600 × 600 | 1500, 0 | Sea to the south and east (harbour). North gate → Brightmead at continent (1800, 600) |
| Brightmead Vale | 1,000 × 1,000 | 1300, 600 | South gate ↔ Solhaven (1800, 600) · north road ↔ Harrowfield (2100, 1600) · north-west track ↔ Russetwood (1500, 1600) |
| Russetwood | 1,400 × 1,400 | 400, 1600 | East ↔ Harrowfield along x = 1800 at z = 2200 (open woodland edge, 300 m wide) · north ↔ Thornwick, Old Timber Road (1300, 3000) |
| Harrowfield | 1,400 × 1,400 | 1800, 1600 | East edge is the Longstrand coast · north ↔ Thornwick, Old Tollbridge (2400, 3000) |
| Thornwick Marches | 2,200 × 2,200 | 700, 3000 | West: the thorn-wall (sealed) · north-west corner: sea-cliff and the Brandspire · east ↔ Riftlands by the east road through a ridge pass (2900–3100, 4000) · north-east ↔ Veilmoor by the Lantern Road through a ridge pass (2800, 5200–5600) |
| The Riftlands | 2,400 × 2,400 | 3100, 3000 | West pass ↔ Thornwick · north track ↔ Veilmoor (4200, 5400–5600) · east and south: sea cliffs · the sealed Imperial Causeway stub at the south-east tip |
| Veilmoor | 2,400 × 2,400 | 2700, 5600 | South-west pass ↔ Thornwick · south track ↔ Riftlands · north: the Pale Downs (sealed by the Long Barrow ridge) |

```
z
8000 +-----------------------------------------------+
     |              (Pale Downs, sealed)             |
     |          +----------------------+             |
     |          |       VEILMOOR       |             |
5600 |          +---+--------------+---+             |
     |   pass ----> |  ridge       | <-- track       |
5200 | +-------------+  +------------------------+   |
     | |  THORNWICK  |==|       THE RIFTLANDS    | sea
     | |   MARCHES   |  |  Kite's Rest   Tor Vael|   |
3000 | +---+-----+---+  +------------------------+   |
     |  |RUSSET- | HARROW- |~ Longstrand             |
     |  | WOOD   | FIELD   |~                        |
1600 |  +----+---+----+----+                         |
     |       | BRIGHT- |                             |
 600 |       |  MEAD   |                             |
     |       +SOLHAVEN-+~~~~ ship to Khazrun ~~~~>   |
   0 +-----------------------------------------------+
     0      1000     2000     3000     4000     5500  x
```

## 4. Khazrun

Khazrun lies east of Meridia across the Hearth Strait. Its west coast faces Solhaven. Continent coordinates in metres; the planned zones fill the western half only.

| Zone | Size | Offset (x, z) | Borders and crossings |
|---|---|---|---|
| Hammerdeep (Mount Khaz) | 1,000 × 800 footprint, interior | 300, 6000 | West face on the sea: the Seagate arch at (300, 6400) · Coldgate ↔ Embercrag (800, 6800) · Dalegate ↔ Stonewake Dale (1300, 6100) · Deepgate ↔ Stoneheart Deeps (700, 6000), by the Long Stair |
| Embercrag Hollow | 1,000 × 1,000 | 500, 6800 | South: Coldgate tunnel · south-east: Bouldergate Pass, running outside the mountain's east flank to Stonewake Dale (1500, 6800 → 1500, 6000) |
| Stoneheart Deeps | 900 × 1,000 footprint, three levels | 200, 5000 | Up: the Long Stair to Hammerdeep · east: Daleside Adit ↔ Stonewake Dale (1100, 5400) · south: Deep Gate rail-tunnel to Ironroot Hold (700, 5000 → 1200, 4400) |
| Stonewake Dale | 1,400 × 1,400 | 1200, 4600 | North-west: Dalegate road · north: Bouldergate Pass · west: Daleside Adit · south road ↔ Ironroot (1900, 4600) |
| Ironroot Highlands | 2,200 × 2,200 | 500, 2400 | North ↔ Stonewake · Deep Gate rail-head at the Hold · south ↔ Cinderfall, the Ash Road (1600, 2400) · east: the collapsed Stonemaw pass (sealed) |
| Cinderfall Barrens | 2,400 × 2,400 | 400, 0 | North ↔ Ironroot · east: the sealed Blackanvil Gate · west and south: lava coast |

Stonewake Dale is the dwarf starting zone (levels 1–5; decided 2026-11-25). Embercrag Hollow and Stoneheart Deeps are the two level 5–10 zones: Embercrag is reached from the Dale by Bouldergate Pass or through Hammerdeep by the Coldgate, the Deeps by the Daleside Adit or the Long Stair. The Dale also opens south onto Ironroot Highlands (10–20).

```
z
7800 +----------------------------------+
     |      EMBERCRAG HOLLOW  5-10      |
6800 |   +----------+ Bouldergate       |
sea  |)) | HAMMER-  |   Pass            |
     |)) |  DEEP    +----------+        |
6000 |   +--+-------+          |        |
     |   |DEEPS|   | STONEWAKE |        |
5000 |   +--+--+   | DALE 1-5  |        |
4600 |      \rail  +-----+-----+        |
     |   +---------------+----------+   |
     |   |   IRONROOT HIGHLANDS     |## collapsed pass
2400 |   +-------------+------------+   |
     |   |   CINDERFALL BARRENS     |[] Blackanvil Gate
   0 |   +--------------------------+   |
     +----------------------------------+
     0       1000      2000      3000   x
```

## 5. Counts

| | Count |
|---|---|
| Zones laid out | 11, plus 2 capitals, 3 dungeons, the raid, the arena and the battleground |
| Sub-areas and city districts | 143 |
| Hubs with building positions | 37, plus the two capitals |
| Spawn camps | 158, holding 3,027 spawn points for 153 creature types |
| Graveyards | 57 |

## 6. Checks run on these files

`tools/doc-generators/spawn-check.ps1` reads every "Spawn camps" table and checks three things. Result at the last run:

| Check | Result |
|---|---|
| Every creature in a zone creature table has at least one camp | Pass: all 152, plus the Exile Challengers |
| Every camp's creature exists in a zone creature table | Pass |
| For every kill objective of 4 or more, the zone holds at least twice that many of the creature | Pass for all creature objectives. Two objectives are world objects, not creatures (Wyrm Eggs, Ward-Pylons); they are listed under Points |

What is **not** fixed by these files, and is decided while building each zone: the exact point of each individual spawn inside its camp radius, patrol paths other than those listed, the exact polygon of each sub-area, prop and decoration placement, and the precise terrain between the stated elevations.
