# Progression: Levels, XP & Pacing

[← Master Plan](../../MASTER_PLAN.md) · Prev: [World & Travel](../01-world/world-and-travel.md) · Next: [Combat & Stats](combat-and-stats.md)

Goal: **leveling pace extremely close to the 2004–2006 "classic" MMO standard.** Launch cap is **30**; all tables are defined to 60 so raising the cap is a config change plus content.

> Source note: the XP-per-level table was checked on 2026-11-12 against published classic-era figures. Three things match exactly: levels 1–7 (400, 900, 1,400, 2,100, 2,800, 3,600, 4,500), the running total through level 31 (597,200), and the 1–60 total (4,084,700). The individual values for levels 8–30 and 32–59 were not each compared line by line, but a table that reproduces those three checkpoints is very unlikely to be wrong in between. The kill-XP and quest-XP rules below are still from working knowledge and remain balance v0.

## 1. XP required per level

| Lvl→ | XP | Cumulative | | Lvl→ | XP | Cumulative |
|---|---|---|---|---|---|---|
| 1→2 | 400 | 400 | | 16→17 | 16,000 | 108,800 |
| 2→3 | 900 | 1,300 | | 17→18 | 17,700 | 126,500 |
| 3→4 | 1,400 | 2,700 | | 18→19 | 19,400 | 145,900 |
| 4→5 | 2,100 | 4,800 | | 19→20 | 21,300 | 167,200 |
| 5→6 | 2,800 | 7,600 | | 20→21 | 23,200 | 190,400 |
| 6→7 | 3,600 | 11,200 | | 21→22 | 25,200 | 215,600 |
| 7→8 | 4,500 | 15,700 | | 22→23 | 27,300 | 242,900 |
| 8→9 | 5,400 | 21,100 | | 23→24 | 29,400 | 272,300 |
| 9→10 | 6,500 | 27,600 | | 24→25 | 31,700 | 304,000 |
| 10→11 | 7,600 | 35,200 | | 25→26 | 34,000 | 338,000 |
| 11→12 | 8,800 | 44,000 | | 26→27 | 36,400 | 374,400 |
| 12→13 | 10,100 | 54,100 | | 27→28 | 38,900 | 413,300 |
| 13→14 | 11,400 | 65,500 | | 28→29 | 41,400 | 454,700 |
| 14→15 | 12,900 | 78,400 | | 29→30 | 44,300 | **499,000** |
| 15→16 | 14,400 | 92,800 | | | | |

**Reserved for 30–60:** 47,400 · 50,800 · 54,500 · 58,600 · 62,800 · 67,100 · 71,600 · 76,100 · 80,800 · 85,700 · 90,700 · 95,800 · 101,000 · 106,300 · 111,800 · 117,500 · 123,200 · 129,100 · 135,100 · 141,200 · 147,500 · 153,900 · 160,400 · 167,100 · 173,900 · 180,800 · 187,900 · 195,000 · 202,300 · 209,800 (30→31 … 59→60).

## 2. Kill XP

**Base XP for a same-level normal mob:** `45 + 5 × mobLevel` (L1 = 50, L10 = 95, L20 = 145, L30 = 195).

| Case | Formula |
|---|---|
| Mob higher level than player | `base × (1 + 0.05 × (mobLvl − charLvl))`, capped at +4 levels (×1.2) |
| Mob lower, not grey | `base × (1 − (charLvl − mobLvl) / ZD)` |
| Mob grey | 0 |

Kill XP is worked in exact arithmetic and a half rounds up: a level-13 creature gives a level-10 character 110 × 1.15 = 126.5, so 127.

**ZD (zero-difference):** levels 1–7 → 5; 8–9 → 6; 10–11 → 7; 12–15 → 8; 16–19 → 9; 20–29 → 11; 30–39 → 12.

**Grey level:** player level 1–5 → nothing is grey; 6–39 → `charLvl − floor(charLvl / 10) − 5` and below is grey.

| Modifier | Value |
|---|---|
| Elite mob | ×2 (in dungeons ×2.5) |
| Rare mob | ×1 XP but guaranteed green+ drop |
| Rested | ×2 on kill XP until the rested pool is used: the bonus is as much again as the kill gave, or what is left of the pool if that is less |
| Mob tapped by another player | 0 XP, no loot. Kill XP and quest kill credit go to the player who tapped it and to that player's party members who are alive and within 100 yd |

### Group XP rules

| Rule | Detail |
|---|---|
| **No split, no bonus** | Every group member within 100 yd of the kill receives the **full** XP they would have earned killing that mob alone, calculated from their own level. If a boar is worth 5 XP, both players in a pair get 5 XP. Group size does not change the number |
| Applies to | Parties (2–5) only |
| **Raid groups** | Creatures killed while in a raid group (10 or 20) give **no kill XP**, anywhere (decided 2026-11-12). Raid groups also give no quest credit except for raid and world-boss quests. Inside a raid instance, bosses grant reputation and loot, not XP |
| **Level-spread cut-off** | If the highest-level member of the group is **more than 5 levels above** the lowest-level member, **every member receives 0 XP** from kills. This is checked per kill against the members in range. It removes power-leveling without any scaling formula |
| Quest XP | Unaffected by grouping; shared kill and (where flagged) item credit |
| Rested XP | Applied per player after the rule above |

Pacing consequence to keep in mind: because XP is not divided, a full party kills far faster than a solo player for the same XP per kill, so grouped players will level noticeably faster than the solo targets in §6. That is accepted as a deliberate reward for grouping; the solo figures remain the balance baseline, and dungeon elite XP (×2.5) is the first number to trim if grouped leveling proves too fast in playtests.

## 3. Quest XP

Standard quest XP by quest level:

| Lvl | XP | Lvl | XP | Lvl | XP | Lvl | XP | Lvl | XP |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 80 | 7 | 500 | 13 | 1,020 | 19 | 1,640 | 25 | 2,350 |
| 2 | 130 | 8 | 580 | 14 | 1,120 | 20 | 1,750 | 26 | 2,480 |
| 3 | 200 | 9 | 660 | 15 | 1,220 | 21 | 1,860 | 27 | 2,610 |
| 4 | 270 | 10 | 750 | 16 | 1,320 | 22 | 1,980 | 28 | 2,750 |
| 5 | 350 | 11 | 840 | 17 | 1,420 | 23 | 2,100 | 29 | 2,890 |
| 6 | 420 | 12 | 930 | 18 | 1,530 | 24 | 2,220 | 30 | 3,050 |

| Quest difficulty tag | Multiplier | Used for |
|---|---|---|
| Breadcrumb / talk-to | ×0.25–0.5 | Delivery, travel, hand-offs |
| Standard | ×1.0 | Kill 8–12, collect 6–10 |
| Long | ×1.25 | Multi-objective, long travel |
| Elite / group | ×1.5 | Named elite, 2–3 players suggested |
| Chain finale | ×1.5–2.0 | Last step of a Main Chain act |
| Dungeon | ×2.0–2.5 | Must be completed inside an instance |
| Raid | ×3.0 | Converted to gold at cap |

**Over-level penalty:** full XP while player level ≤ quest level + 5; then 80% / 60% / 40% / 20% at +6 / +7 / +8 / +9; 10% from +10. Quest colours: red (≥ +5 above player), orange (+3/+4), yellow (±2), green, grey.

**Quest log limit:** 20 quests. At level cap, quest XP converts to coin at 6 copper per XP.

## 4. Other XP sources

| Source | Amount |
|---|---|
| Discovering a sub-area | `areaLevel × 15` XP (min 10), nothing if area is grey. The area's level is its own, or its zone's lowest level if it has none. An area that is grey to the character is still recorded as discovered. The character must be alive |
| Gathering, crafting | None (classic rule) |
| Battleground win / loss | ½ standard quest XP for player level on win; ¼ on loss (kept small so PvP is not the fastest leveling route) |

## 5. XP budget per tier (design target)

| Tier | XP needed | Quest XP (one zone) | Kills done for quests | Dungeon / explore / grind | Notes |
|---|---|---|---|---|---|
| T1 1→5(6) | 7,600 | ~4,060 (53%) | ~4,600 | ~4,000–4,400 more from kills made on the way | Player leaves at about level 7, after about 200–280 kills in all, about 75 of them asked for by quests |
| T2 5→10 | 20,000 | ~12,170 (60%) | ~12,500 | — | Over-provided so the elite quests are optional |
| T3 10→20 | 139,600 | ~50,000 per zone (36%) | ~50,000 | ~40,000 | Gap filled by repeat Gallowmere Crypts runs, class quests, part of the *other* T3 zone |
| T4 20→30 | 331,800 | ~95,000 per zone | ~95,000 per zone | — | Needs ≈ 2 of 3 zones + dungeon runs |

The starting zones are expected to give more than their quests ask for (decided 2026-11-25, in place of thinning the zones' creatures). A player fights what stands between them and the objectives and kills more than once for items that drop by chance, so a starting zone is about 200–280 kills in all, about 75 of them asked for by quests, and a player leaves it at about level 7. The quest XP is exactly as designed. Measured by the zone bot runs: Brightmead Vale about 281 kills, 4,060 quest XP, about 13,175 XP in all, level 7; Embercrag Hollow, when it was the dwarf starting zone on this same template, 211 kills in 96 minutes, level 7. Open: Stonewake Dale, the dwarf starting zone since 2026-11-25, has not been measured.

Rule of thumb used when authoring zones: **≈40% quests, ≈35–40% kills made while questing, ≈20–25% dungeons/exploration/grind** — the classic split. Having two or three zones per tier is what removes forced grinding.

## 6. Target /played time

| Reach level | Cumulative hours (average first-time player) |
|---|---|
| 5 | 1.5 |
| 10 | 5 |
| 15 | 11 |
| 20 | 20 |
| 25 | 33 |
| 30 | 48 |

## 7. Rested XP

- Accrues at **5% of the current level's XP per 8 hours** in a rest area (an inn or capital). Online it builds only while the character is in a rest area. Logged out it builds by the wall clock since logout: at the full rate if the character logged out in a rest area, at ¼ of it elsewhere.
- Cap: 150% of the current level's requirement. On gaining a level the pool is cut to the new level's cap.
- Kept in fractions and saved in whole points.
- Doubles kill XP only. Shown as a blue notch on the XP bar.

## 8. Level-gated unlocks

| Level | Unlock |
|---|---|
| 1 | Hearthstone, the capital ship, mail, 16-slot backpack |
| 5 | Primary and secondary professions (Apprentice, cap 75) |
| 8 | First mob debuffs requiring a cleanse appear |
| 10 | Talent points begin (1 per level); class quest #1; Journeyman professions (150); battleground bracket 10–19 |
| 13 | Dungeon 1 — Gallowmere Crypts |
| 15 | Main Chain 2 begins |
| 20 | Class quest #2; Expert professions (225); Dungeon 2; Fighter dual wield; Druid Reawaken; bracket 20–29 |
| 27 | Dungeon 3 |
| 30 | Cap. Riding; raid attunement; world bosses; bracket 30 |
| *40 / 60* | *Reserved: plate armor at 40, Artisan professions at 35, epic riding at 60* |

Talent points at cap 30: **21** (enough for one tier-5 "signature" talent). See [Class Framework](../03-classes/class-framework.md).

## 9. Ability training

New ability ranks are bought from class trainers at the even levels where the class tables give a rank. Abilities at level 1 are known from the start and cost nothing: Attack, one special attack and, for a class that heals, one basic heal (Fighter: Strike, and Battle Stance to stand in; Cleric: Oath of Radiance and Mending Light; Druid: Thornlash and Mend), each at rank 1 and nothing else (decided 2026-11-24). **The first trainer rank of every class is at level 2**, at the curve's level-2 price: Battle Cry (Fighter), Litany of Resolve (Cleric), Gift of the Grove (Druid), each rank 1. Cost curve (per rank): L2 10c · L4 1s · L6 2s · L8 5s · L10 8s · L12 12s · L14 20s · L16 30s · L18 50s · L20 60s · L22 80s · L24 1g · L26 1g 20s · L28 1g 40s · L30 1g 60s. A character who trains everything spends ≈ 14g by 30, which is roughly half of expected income — the classic "can I afford my spells?" tension is intentional.

| Rule | Detail |
|---|---|
| Previous rank | A rank can be bought only when the rank before it of the same ability is known. Abilities known from the start count, so the second rank of a level-1 ability needs nothing bought first |
| Level | A rank is refused below its level ("level too low") and shown as unavailable |
| Whose trainer | A class trainer teaches only its own class; another class is refused, not shown an empty list |
| First rank free | The starting-zone quest that sends a new character to its trainer makes the next rank bought cost nothing, once; a refused purchase does not use it up. The quest is offered only from level 2, when the class's level-2 rank can be bought, so that rank is the one a new character gets free |
| Class-quest abilities | The first rank is granted by the quest and costs nothing ([Class Framework §6](../03-classes/class-framework.md#6-class-quests)) |

## 10. Death

| Step | Rule |
|---|---|
| On death | Body stays; player becomes a ghost at the nearest graveyard. 10% durability loss on all equipped items |
| Corpse run | Run back as a ghost (+25% speed) and resurrect within 30 yd of the corpse at 50% health/mana |
| Repeated deaths | Resurrection timer: 0 s, then 30 s, 60 s, 120 s if dying again within 5 min |
| Spirit healer | Resurrect at the graveyard: extra 25% durability loss and (level > 10) **Resurrection Sickness** −75% all stats for 1 min per level above 10, max 10 min |
| Player resurrection | Cleric *Raise the Fallen* (out of combat), Druid *Reawaken* (in combat, 30 min CD) |
| In dungeons | Ghost runs to the instance entrance |
| No XP loss, no item loss | Classic rule |
| PvP death | No durability loss |
