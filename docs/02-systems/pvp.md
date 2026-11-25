# PvP

[← Master Plan](../../MASTER_PLAN.md) · Prev: [NPC AI & World](npc-ai-and-world.md) · Next: [UI & Controls](ui-and-controls.md)

Launch PvP is deliberately small — **duels, one free-for-all arena, one three-team battleground** — but every piece is built on the N-allegiance rules in [Factions & Races](../01-world/factions-and-races.md) so real faction warfare can be switched on later.

## 1. PvP rules common to all modes

- Player-vs-player damage uses the same formulas as PvE; crowd control has diminishing returns (see [Combat](combat-and-stats.md#8-crowd-control--diminishing-returns)).
- No durability loss, no XP loss on PvP death.
- Level differences are not normalised; brackets keep battlegrounds fair.
- A player is attackable only when the **hostility check** passes: `reaction(allegianceA, allegianceB) == Hostile` **or** both are in a Free-for-all area **or** they are duelling **or** they are on different battleground teams. One function, used everywhere.

## 2. Duels

- Right-click → Duel, or `/duel`. Target accepts or declines. A flag drops; 3 s countdown.
- Ends when one player reaches 1 health (no death), leaves a 40 yd radius for 10 s, or forfeits (`/forfeit`).
- Not allowed in instances, the arena, or within capitals' inner districts (a duelling ground sits outside each gate).
- Result announced in the zone's local chat. Tracked stat: duels won/lost.

## 3. The Dustpit — free-for-all arena

| | |
|---|---|
| Location | A natural sinkhole arena in the rock beneath **Kite's Rest**, [Riftlands](../05-zones/t4-riftlands.md) |
| Rule | Entering the pit floor flags you **Free-for-all**: every other player is hostile, including party members |
| Access | Any level (the zone is 20–30). Spectator terraces above are safe |
| Layout | 60 yd oval sand floor, four pillars for line-of-sight, a central trapdoor, two ramps and one drop-in ledge. Deep loose sand in the outer ring slows by 20% |
| **The Pitmaster's Chest** | Spawns in the centre every 3 hours (announced zone-wide 5 min before). Opening takes a 10 s uninterrupted channel. Contains coin, a blue item from the Dustpit list, and a **Pit Champion's Token** |
| Token turn-in | 12 tokens → *Dustpit Champion's Knot* (trinket: removes movement-impairing effects, 5 min CD) via a Freeholders quest |
| Death | Respawn at the terrace graveyard after 20 s; no corpse run |
| Rewards per kill | 1 Mark of Valor for a killing blow on a player within 5 levels (diminishing: same victim gives nothing for 10 min) |
| Anti-grief | Guards on the terraces; no combat outside the pit floor |

**Dustpit blue list (level 28–30):** Pitfighter's Cestus (mail hands), Sandscoured Leggings (leather), Trapdoor Buckler (shield), Champion's Cutlass (1H sword), Spectator's Parasol (staff), Blood-on-the-Sand Band (ring).

## 4. Crownfall — three-team battleground

A king-of-the-hill map with a carry objective, built for three sides from day one.

| | |
|---|---|
| Fiction | A broken-off mesa-top that once held Tor Vael's coronation terrace, where a phantom of the Hollow Crown manifests. Whoever holds it is "crowned" |
| Teams | **Red, Blue, Yellow.** At launch players are assigned at random to balance team sizes (premade groups of up to 5 stay together). When allegiances exist: Red = Covenant, Blue = Concord, Yellow = Wildpact |
| Team size | 8 v 8 v 8 (24 players). Starts at 4 v 4 v 4 minimum |
| Brackets | 10–19, 20–29, 30 |
| Queue | From any battlemaster or the PvP panel; solo or group; teleports in and returns you to where you were |
| Map | Triangular plateau ~220 yd per side. Three team bases at the corners (each with a graveyard and a short tunnel). A raised **Hill** in the centre with three ramps. Three **Shrines** midway along each edge |
| Win | First team to **1,000 points**, or highest after 20 minutes |

**Scoring**

| Source | Points |
|---|---|
| Controlling the Hill (most players on it, uncontested by majority) | 5 per 3 s |
| **Crown-bearer** on your team standing on the Hill | Hill income ×2 |
| Killing blow | 2 |
| Killing the Crown-bearer | 15 |
| Each Shrine your team holds | +1 per 3 s and a team-wide buff |

**The Crown:** spawns on the Hill 60 s after the gates open. Channel 5 s to pick up. The bearer takes +25% damage (stacking +10% each 30 s), cannot mount or stealth, and drops it on death; it can be picked up by anyone after 3 s or resets to the Hill after 15 s.

**Shrines (capture points, 8 s channel):** *Shrine of Steel* (+10% armor), *Shrine of Bloom* (+10% healing received), *Shrine of Aether* (+10% spell and attack power) — the three faction resources from the [lore triangle](../01-world/lore.md#4-the-three-factions--the-power-triangle).

**Why three teams works here:** the team in the lead becomes the natural target of the other two, so matches self-balance; the Crown damage debuff forces passes rather than a single unkillable carrier.

Other details: 2 min preparation; respawn waves every 25 s; deserter debuff 15 min for leaving; AFK report; scoreboard (kills, deaths, damage, healing, hill time, crown time); late-join backfill.

**Rewards:** win 3 Marks of Valor, second place 2, third 1; bonus XP per [Progression](progression.md#4-other-xp-sources).

## 5. Marks of Valor and PvP gear

Vendor: Quartermaster at each capital's battlemaster and in Kite's Rest.

| Item | Level | Cost |
|---|---|---|
| Valor consumables (bandages, potions usable only in PvP areas) | any | 1 |
| Insignia of the Hearth-Oath (trinket: break stun/fear/root, 5 min CD) | 20 | 30 |
| Contender's set — 5 blue pieces per class (L30; Sta-heavy; 2-pc +20 Sta, 4-pc −0.5 s on a class escape) | 30 | 15–30 each |
| Contender's weapons (1H, 2H, staff, shield) | 30 | 40–60 |
| Tabard of the Three Banners | any | 20 |

No rank ladder / honor grind at launch (that classic system is post-launch if wanted).

## 6. Designed-in future: faction warfare

| Feature | When allegiances 2 and 3 arrive |
|---|---|
| World PvP flagging | Contested zones (all T4, Sundrel) auto-flag; own Territory is opt-in |
| Triangle expressed in play | Each allegiance's prey holds resource nodes it needs: capturing **Steel / Lifebloom / Aether** nodes in contested zones buffs your whole zone population |
| Battlegrounds | Crownfall becomes allegiance-vs-allegiance-vs-allegiance; a second map (three-flag capture) is planned |
| Keeps / zone control | Wellspring Scar (Sundrel 55–60) designed as a three-way control zone |
| Guards, flight paths, cities | Already per-allegiance in data |
| Kill credit / honor | "Honorable kill" rule and diminishing returns already exist via the Dustpit rule |
