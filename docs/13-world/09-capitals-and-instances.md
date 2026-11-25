# World Layout — Capitals and Instances

[← World Layout Index](00-world-layout.md) · Prev: [Veilmoor](08-veilmoor.md) · NPCs: [Solhaven](../11-npcs/08-solhaven.md) · [Hammerdeep](../11-npcs/09-hammerdeep.md) · Numbers: [Encounter Data](../12-data/encounters.md)

Notation and rules are in the [index](00-world-layout.md).

# Solhaven

| | |
|---|---|
| Size and offset | 600 × 600 m · Meridia (1500, 0) |
| Shape | A white-stone city on a hill above the Silverrun estuary. The keep stands on the highest ground in the north-west; the harbour fills the south-east. Sea to the south and east |
| Elevation | Crown Terrace 45 m · Dawnspire Close 30 m · Coinmarket 20 m · Smith's Row 15 m · the Hedgerow 18 m · the Athenaeum 25 m · harbour 2 m |
| Landmark | The Dawnspire, the cathedral's twin-flamed tower at (380, 420) |
| Gates | North gate → Brightmead (300, 600). There is no other land gate. The estuary mouth is at (520, 80) |
| Walking times | North gate to the bank: 35 s · bank to the harbour pier: 40 s · north gate to the pier: 75 s |

```
      A  B  C  D  E  F
  6   CT CT NG NG .. ..
  5   CT CT CM DC DC ..
  4   CT AT CM DC DC HR
  3   AT AT CM CM SR HR
  2   .. SR SR SR HB HB
  1   ## ~~ ~~ HB HB ~~      (cells are 100 m)
```

| Code | District | Centre | Size | Contents (NPC ids in the roster) |
|---|---|---|---|---|
| NG | North gate and stables | (300, 570) | 200 × 60 | Gate, stables and paddock just inside on the east (360, 550), duelling ground outside (300, 640), city notice board (260, 540) |
| CT | Crown Terrace | (120, 480) | 220 × 240 | Marrowind Keep (90, 520): audience hall, throne room · tilt-yard (160, 450) · salle (120, 420) · armoury steps (190, 500) · banner court (200, 440) |
| DC | Dawnspire Close | (400, 430) | 180 × 180 | Cathedral of the Twin Flames (380, 420): high altar, north transept, infirmary, porch |
| CM | Coinmarket | (270, 380) | 160 × 280 | Royal Bank (250, 420) · auction hall (290, 400) · *The Gilded Lark* (260, 340) · draper's row (300, 330) · saddlers' lane (230, 310) · gilded stair (300, 440) · guild registry (240, 460) · barber (280, 300) · covered market (270, 370) · mailboxes at the bank and the inn |
| AT | The Athenaeum | (130, 310) | 200 × 160 | Entrance desk, reading room, bursar's window, vault (not enterable) |
| SR | Smith's Row | (300, 190) | 320 × 100 | Great forge (220, 200) · ore-yard (180, 180) · clock-works (280, 210) · armorer (330, 190) · weaponsmith (360, 200) · fletcher's corner shop (400, 190) |
| HR | The Hedgerow | (540, 340) | 100 × 200 | Stone circle (540, 380) · star-pool (560, 320) · physic beds (530, 290) · glasshouse (550, 260) |
| HB | Solhaven Harbor | (430, 110) | 300 × 180 | Pier-head and ship berth (470, 60) · lighthouse eyrie (560, 130) · fish-quay (400, 90) · chowder-house (370, 130) |

Other points: graveyard outside the north gate (220, 650) · spirit healer there · guards at the gate (4), on every district stair (2 each) and patrolling in pairs on three loops · ship *The Hearth-Oath* docks at (470, 60) for 60 seconds in every 5 minutes.

# Hammerdeep

| | |
|---|---|
| Footprint and offset | 1,000 × 800 m · Khazrun (300, 6000). Entirely inside Mount Khaz |
| Structure | A hollow shaft 300 m across with three ring-levels cut into its walls and halls opening off them. **Ground** 0 m · **Middle** +40 m · **Upper** +85 m. A great stair spirals the shaft; two lifts run Ground ↔ Upper |
| Landmark | The Great Forge's glow at the top of the shaft, visible from every ring |
| Gates | The Seagate arch on the west sea-face (0, 400) · Coldgate, north, to Embercrag (500, 800) · Dalegate, east, to Stonewake Dale (1000, 100) · Deepgate, south, down the Long Stair to Stoneheart Deeps (400, 0) |
| Walking times | Seagate quay to the bank (one level up): 50 s · bank to the Great Forge (one level up): 45 s · Seagate to Thane's Hall by lift: 55 s |

| Level | District | Centre | Size | Contents |
|---|---|---|---|---|
| Ground | The Seagate | (180, 400) | 320 × 260 | Sea-cave harbour: the arch at (0, 400), inner quay and ship berth (200, 400), customs hall (260, 460), quay steps (fishing) (160, 340), quay kitchens (240, 340), eyrie-lift (300, 420) |
| Ground | The Rootvault | (460, 420) | 260 × 240 | Terraced garden: upper terrace (480, 480), sky-shaft pool (460, 400), channel-side beds (420, 360), rune-cistern and screw-pumps (360, 420) |
| Ground | Gate halls | — | — | Deepgate hall (400, 60) · Coldgate tunnel mouth (500, 760) · Dalegate hall, ram-pens and paddock (940, 120) · duelling ring outside Dalegate (1040, 100) |
| Middle | Goldring Commons | (520, 400) | 300 × 300, the ring itself | Deep Vault (520, 520) · auction ring (600, 440) · *The Brazen Tankard* (440, 460) · weavers' arcade (600, 340) · tanners' arcade (440, 320) · rune-stair (520, 280) · charter-hall (640, 400) · braiding-bench (400, 400) · ring-market (520, 400) · hall notice-stone (560, 480) · mailboxes at the vault and the inn |
| Middle | Hall of Embers | (760, 520) | 180 × 160 | The Forge-flame, oath-stone, mending-hall, porch |
| Middle | The Scrollery | (280, 540) | 160 × 140 | Reading hall, tablet-stacks, tally-desk |
| Upper | The Great Forge | (520, 420) | 260 × 240 | First anvil (520, 440) · ore-chutes (600, 420) · gear-loft (440, 380) · forge terrace: armorer, weaponsmith, gunsmith and proofing range (520, 320) · the Forge Balcony eyrie on the west face (300, 420) |
| Upper | Thane's Hall | (760, 300) | 220 × 200 | High seat (800, 300) · seal-table (760, 300) · shield-ring (720, 360) · axe-court (700, 260) · weapon gallery (780, 380) · banner gallery (820, 240) |

Other points: graveyard in the Deepgate hall (440, 100) with a spirit healer · guards at each gate (4), each lift (2) and on each ring (6) · the ship enters under the arch, docks at (200, 400) for 60 seconds in every 5 minutes · Hammerdeep has no day or night; the Rootvault's sky-shaft shows the true time.

# The Dustpit

| | |
|---|---|
| Place | A sinkhole under Kite's Rest, reached by the pit stair from (1160, 1280) in the [Riftlands](07-riftlands.md) |
| Floor | Oval, 55 m × 42 m, sand. Outer ring 6 m wide of deep sand (−20% movement) |
| Features | 4 stone pillars 3 m across, at the corners of a 24 × 16 m rectangle · central trapdoor (the Pitmaster's Chest rises here) · 2 ramps (north and south) · 1 drop-in ledge 4 m high on the east |
| Terraces | Spectator ring 5 m above the floor; safe; terrace graveyard at the north end; 4 Freeholder Peacekeepers |

# Crownfall

| | |
|---|---|
| Map | Equilateral triangle, 200 m per side (220 yards), on a mesa-top; edges are cliffs |
| Bases | One at each corner: Red (south-west), Blue (south-east), Yellow (north). Each has a graveyard, a gate that opens after 2 minutes, and a 25 m tunnel onto the field |
| The Hill | Raised round platform 24 m across at the centre, 4 m high, with three ramps, each facing the gap between two bases |
| Shrines | Midway along each edge, 60 m from the Hill: Steel (south edge, between Red and Blue), Bloom (north-west edge, between Red and Yellow), Aether (north-east edge, between Blue and Yellow) |
| Cover | 6 broken pillar clusters between the Hill and the shrines; low walls along each tunnel exit |
| Distances | Base to Hill 115 m (18 s on foot) · base to its nearer shrines 100 m · shrine to shrine 100 m |

# Gallowmere Crypts

Entrance: the crypt gate at Thornwick (1080, 1260). Total walkable length about 620 m.

| # | Room | Size | Connects to | Contents |
|---|---|---|---|---|
| 1 | Gibbet stair | 8 m wide, 70 m long, descending 25 m | 2 | 3 packs; shortcut door at the bottom (opens after boss 2) |
| 2 | The Charnel Hall | 45 × 30 m, 6 marked grave-plots | 1, 3 | 5 packs; **Gravedigger Holt** at the far end |
| 3 | Embalmers' Gallery | 60 × 14 m with 6 alcoves | 2, 4, 5 | 4 packs; **The Stitched Choir** in the widened middle (22 m across) |
| 4 | Side chapel (optional) | 20 × 20 m, circle of 6 candles | 3 | 2 packs on the approach; **Sister Maudlin** |
| 5 | The Cinder Kiln | 40 × 40 m around a central kiln, gantry above | 3, 6 | 5 packs |
| 6 | Sanctum stair | 6 m wide, 40 m | 5, 7 | 2 packs of Bone Sentinels |
| 7 | The Brandfather's Sanctum | 30 m round, 8 wall-niches | 6 | **Brandfather Kray** |

# The Slagworks

Entrance: the Ore Lift at Cinderfall (320, 1640). Total walkable length about 760 m.

| # | Room | Size | Connects to | Contents |
|---|---|---|---|---|
| 1 | Ore Lift landing | 25 × 25 m | 2 | 2 packs |
| 2 | Sorting Floor | 70 × 40 m, conveyor lanes, 4 slag levers | 1, 3 | 6 packs; **Overseer Grint** on the far dais |
| 3 | The Slag Sluice | 120 m river of slag, 14 m wide, with 9 crust-platforms and 3 cooling grates; banks either side | 2, 4 | 4 packs on the banks; **Molten Maw** in the river |
| 4 | Bellows Hall | 80 × 45 m, 3 Great Bellows along the north wall | 3, 5 | 6 packs; **Thurga and Cinderpaw** at the third bellows |
| 5 | Crucible approach | 10 m wide ramp, 60 m | 4, 6 | 3 packs |
| 6 | The Grand Crucible | 40 m round floor in four quarters, quench-trough on the east, the crucible hanging at the centre | 5 | **Forgemaster Khardun** |

# Hollowspire Keep

Entrance: the keep gate at Veilmoor (2180, 2280). Total walkable length about 900 m.

| # | Room | Size | Connects to | Contents |
|---|---|---|---|---|
| 1 | Gatehouse and bailey | 40 × 30 m, two portcullis lines | 2 | 3 packs; **Castellan Vorn** |
| 2 | Great Hall | 60 × 24 m, one long table with 12 seats | 1, 3, 4, 5 | 5 packs, then **the Banquet of Hollows** |
| 3 | Library (west wing) | 50 × 30 m, two floors of shelves, 4 light-shafts | 2 | 6 packs; **Librarian Quill** |
| 4 | Barracks Chapel (east wing) | 45 × 25 m | 2 | 6 packs; **Ser Aldous** |
| 5 | Spire stair | Spiral, 4 landings | 2, 6 | 4 pairs of Spire Gargoyles; opens when bosses 3 and 4 are dead |
| 6 | The Crown Chapel | 32 m round | 5 | **Lady Seraphine Vael** |

# The Hollow Throne

Entrance: behind the Maw-Scar at the Riftlands (2300, 120). Total walkable length about 1,300 m. Each boss room has 5 ward-pylons around its edge.

| # | Section | Size | Connects to | Contents |
|---|---|---|---|---|
| 1 | The Vault Gate | Approach 80 × 20 m; gate court 50 × 50 m with 4 floor-lanes | 2 | 4 packs; **The Bulwark of Tor Vael** |
| 2 | Hall of Petitioners | 120 × 30 m, rubble walls with entombed courtiers | 1, 3, 4 | 6 packs |
| 3 | The Choir Vault | 60 m round, three daises 40 m apart | 2, 5 | 5 packs; **The Echo Sisters** |
| 4 | The Buried Parade Ground | 90 × 60 m, 5 ballista lanes, 3 arches, barracks doors on the north | 2, 5 | 5 packs; **Marshal Korvash** |
| 5 | The Aether Conservatory | Broken dome 70 m across with 3 ledges at different heights | 3, 4, 6 | 5 packs; **Ghul'thar**; then **Archmagister Ilyra** on the dome's inner floor (40 m round) once the wyrm is dead |
| 6 | The Throne of Tor Vael | Approach 60 m; throne hall 80 m round, shrinking in phase 3 | 5 | 3 packs; **Vaelric, the Hollow King** |

Sections 3 and 4 can be done in either order; both must be cleared to open section 5.
