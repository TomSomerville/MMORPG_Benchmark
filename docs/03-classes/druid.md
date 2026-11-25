# Druid

[← Master Plan](../../MASTER_PLAN.md) · [Class Framework](class-framework.md) · Prev: [Cleric](cleric.md) · Next: [Gathering](../04-professions/gathering.md)

**Fantasy:** Hedgewardens (human) and Stonesingers (dwarf) — keepers of the old rites who speak to the Verdant Choir and read the star-light of the Lattice. A pure caster: **the Druid never shapeshifts** and is always in humanoid form (decided 2026-11-12; there is no travel form either). **Resource:** Mana. **Armor:** leather or cloth. **Weapons:** staves, daggers, one-handed maces, held off-hands (2H maces at 20). **Relic slot:** Charm.

Three ways to play: **Verdance** (pre-emptive heal-over-time healing), **Stormcall** (Nature ranged damage — thorns, swarms, lightning), **Starweave** (Arcane ranged damage — star-fire and moonlight).

## 1. Abilities (levels 1–30)

| Lvl | Ability | School | Cost | Cast / CD | Effect | Ranks at |
|---|---|---|---|---|---|---|
| 1 | **Thornlash** | Nature | 20 → 100 | 1.5 → 2.0 s | 13–16 → 130–150 Nature damage, 30 yd | 1, 6, 14, 22, 30 |
| 1 | **Mend** | Nature | 25 → 265 | 1.5 → 3.0 s | Heal 40 → 520 | 1, 8, 14, 20, 26 |
| 1 | **Gift of the Grove** | Nature | 20 → 100 | instant | 30 min: +25 → +150 armor; from rank 2 also +2 → +6 all attributes and +5 → +10 all resistances | 1, 10, 20, 30 |
| 4 | **Starbrand** | Arcane | 25 → 150 | instant | 9–12 → 85–100 Arcane damage plus 12 → 150 over 9 → 12 s | 4, 10, 16, 22, 28 |
| 4 | **Renewal** | Nature | 25 → 160 | instant | Heal 32 → 300 over 12 s (4 ticks) | 4, 10, 16, 22, 28 |
| 6 | **Briarskin** | Nature | 35 → 105 | instant | 10 min on a friendly target: melee attackers take 3 → 12 Nature damage | 6, 14, 24 |
| 8 | **Rootgrasp** | Nature | 50 → 80 | 1.5 s | Root 12 → 21 s; 20 → 80 Nature damage over the duration; damage may break it | 8, 18, 28 |
| 10 | **Overgrowth** | Nature | 120 → 350 | 2.0 s | Heal 85 → 330 instantly plus 100 → 345 over 21 s (class quest) | 10, 18, 24, 30 |
| 10 | **Cleanse Toxin** | Nature | 8% base mana | instant | Remove 1 poison; at rank 2 (L26) also cleanses again each 2 s for 8 s | 10, 26 |
| 12 | **Glimmer Mark** | Arcane | 55 → 85 | instant | 40 s: target armor −175 → −395 and cannot stealth or turn invisible | 12, 18, 30 |
| 14 | **Stinging Swarm** | Nature | 45 → 100 | instant | 66 → 220 Nature damage over 12 s; target's hit chance −2% | 14, 20, 30 |
| 18 | **Lull Beast** | Nature | 90 | 1.5 s | Sleep a Beast or Dragonkin for 20 → 30 s; damage wakes it; one target at a time | 18, 28 |
| 20 | **Astral Lance** | Arcane | 95 → 180 | 3.5 s | 95–115 → 200–240 Arcane damage, 30 yd | 20, 26 |
| 20 | **Reawaken** | Nature | 30% base mana + Seed of Renewal | 2.0 s / 30 min | Resurrect a dead player **in combat** with 400 health and 700 mana (class quest) | 20, 30 |
| 22 | **Lift Curse** | Arcane | 8% base mana | instant | Remove 1 curse from a friendly target | — |
| 24 | **Barkward** | Nature | 60 | instant / 2 min | 15 s: −20% physical damage taken, immune to cast pushback, but your cast times are 1 s longer | 24 |
| 26 | **Squall** | Nature | 320 | 10 s channel / 60 s | Storm at a target location (30 yd, 10 yd radius): 45 Nature damage per second to enemies inside and −20% attack speed | 26 |
| 28 | **Wellspring** | Nature | 5% base mana | instant / 6 min | Friendly target: mana regeneration +400% and regenerates while casting, 20 s | — |
| 30 | **Stillwater** | Nature | 375 | 10 s channel / 5 min | Heals all party members within 30 yd for 98 every 2 s | 30 |

## 2. Role playstyles at 30

- **Verdance (healer):** keep **Renewal** rolling on the tank and anyone taking damage, layer **Blossom** (signature) to three stacks on the tank, **Overgrowth** when a hit lands, **Mend** only for big holes. Healing is done *before* the damage: a Druid who is surprised is behind. Strong on the move and for sustained raid-wide damage, weak at burst single-target rescue (the Cleric's job). Wellspring for mana; Reawaken as the only combat resurrection in the game.
- **Stormcall (Nature DPS):** **Stinging Swarm** → **Thornlash** spam (fast casts, high crit, long crit multiplier from *Vengeful Bloom*) → **Call Lightning** (signature) on cooldown, which chains to two more targets; **Squall** for packs; Rootgrasp/Nature's Grasp to kite. Mobile-ish, sustained, cleave-friendly.
- **Starweave (Arcane DPS):** **Glimmer Mark** → **Starbrand** (instant; its crits shorten the next Lance) → **Astral Lance** hard casts → **Starfall** (signature) for burst/AoE. Slower, bigger hits; best single-target burst of the three; brings an armor debuff for melee-heavy groups.

Because Nature and Arcane are different schools, the two DPS trees have different strengths against resistant enemies (e.g. Bog Shamblers resist Nature; Tor Vael constructs resist Arcane) — a deliberate reason for both to exist.

## 3. Talents

### 3.1 Verdance (heal-over-time healer)

| Tier | Talent | Ranks | Effect |
|---|---|---|---|
| 1 (0) | Improved Gift of the Grove | 5 | Its effects +7% per rank |
| 1 | Verdant Focus | 5 | 14% chance per rank to avoid pushback on healing spells |
| 2 (5) | Naturalist | 5 | Mend cast time −0.1 s per rank |
| 2 | Lingering Bloom | 3 | Renewal duration +3 s per rank (one extra tick each) |
| 2 | Subtlety | 5 | Healing threat −4% per rank |
| 3 (10) | Improved Renewal | 3 | Renewal healing +5% per rank |
| 3 | Tranquil Spirit | 5 | Mend and Stillwater mana cost −2% per rank |
| 3 | Seedling | 3 | When your Renewal expires or is dispelled, it heals for 10 / 20 / 30% of its total (req. Lingering Bloom 3) |
| 4 (15) | Gift of Seasons | 5 | All healing +2% per rank |
| 4 | Improved Overgrowth | 5 | Overgrowth initial heal crit chance +10% per rank |
| 5 (20) | ★ **Blossom** | 1 | Active, instant, 60 mana: HoT on an ally — 39 every 1 s for 7 s, stacks to 3. When it expires or is dispelled it *blooms* for 180 per stack. Refreshing before expiry keeps the stacks rolling (req. Improved Renewal 3) |
| 5 | Living Spirit | 3 | Spirit +5% per rank |
| 6 (25) | **Nature's Swiftness** | 1 | Active, 3 min CD: your next Nature spell is instant |
| 6 | Evergreen | 3 | Your HoT ticks have a 5 / 10 / 15% chance to tick again immediately |
| 7 (30) | **Harvest** | 1 | Active, 15 s CD (req. Blossom): consume your Renewal or Overgrowth on the target to instantly heal for 12 s of Renewal or 18 s of Overgrowth |

### 3.2 Stormcall (Nature ranged DPS)

| Tier | Talent | Ranks | Effect |
|---|---|---|---|
| 1 (0) | Improved Thornlash | 5 | Thornlash cast time −0.1 s per rank |
| 1 | Nature's Reach | 2 | Range of Nature damage spells +10 / +20% |
| 1 | Improved Briarskin | 3 | Briarskin damage +25% per rank |
| 2 (5) | Improved Rootgrasp | 3 | 40 / 70 / 100% chance to ignore pushback while casting Rootgrasp |
| 2 | **Nature's Grasp** | 1 | Active, 60 s CD: for 45 s, the next enemy to strike you in melee is caught by Rootgrasp (same rank) |
| 2 | Venomous Swarm | 3 | Stinging Swarm damage +10% per rank |
| 3 (10) | Gathering Storm | 5 | Nature damage spell crit +2% per rank |
| 3 | Static Charge | 2 | Thornlash crits daze the target (−50% movement) for 2 / 4 s |
| 4 (15) | Vengeful Bloom | 5 | Nature damage spell crit bonus +20% per rank (crit ×1.5 → ×2.0) (req. Gathering Storm 5) |
| 4 | Thick Hide | 3 | Armor from items +4% per rank |
| 5 (20) | ★ **Call Lightning** | 1 | Active, 150 mana, 2.0 s cast, 10 s CD: 190–220 Nature damage, then arcs to 2 additional enemies within 10 yd for 70% each |
| 5 | Eye of the Storm | 3 | Damage spell hits have a 2 / 4 / 6% chance to make your next spell cost no mana |
| 6 (25) | Stormborn | 5 | Nature damage +2% per rank |
| 6 | Improved Squall | 2 | Squall cooldown −15 / −30 s; its slow +5 / +10% |
| 7 (30) | **Heart of the Storm** | 1 | Passive aura (req. Call Lightning): party within 30 yd gains +3% spell crit; your Thornlash crits refund 30% of its mana cost |

### 3.3 Starweave (Arcane ranged DPS)

| Tier | Talent | Ranks | Effect |
|---|---|---|---|
| 1 (0) | Improved Starbrand | 5 | Starbrand damage and crit chance +2% per rank |
| 1 | Starlit Mind | 5 | Arcane spell mana cost −2% per rank |
| 2 (5) | Improved Glimmer Mark | 3 | Marked target is also 1% easier to hit per rank for all attackers |
| 2 | Starglow | 3 | Mana cost of Starbrand, Astral Lance, Mend, Renewal −3% per rank |
| 2 | Celestial Focus | 3 | Astral Lance has a 5 / 10 / 15% chance to stun 3 s and 25 / 50 / 70% pushback resistance |
| 3 (10) | Lunar Guidance | 3 | Spell power increased by 8 / 16 / 25% of your Intellect |
| 3 | Astral Alignment | 2 | Starbrand crits reduce the cast time of your next Astral Lance by 0.5 / 1.0 s |
| 4 (15) | Starfury | 5 | Arcane damage +2% per rank |
| 4 | Twilight Veil | 2 | Threat from Arcane spells −10 / −20% |
| 5 (20) | ★ **Starfall** | 1 | Active, 215 mana, instant, 45 s CD (req. Astral Alignment 2): stars fall on up to 3 enemies within 10 yd of the target — 4 waves over 8 s, 55–65 Arcane each |
| 5 | Wrath of the Heavens | 5 | Spell crit +1% per rank |
| 6 (25) | Dreamstate | 3 | Regenerate 4 / 7 / 10% of Intellect as mana per 5 s |
| 6 | Improved Astral Lance | 2 | Astral Lance cast time −0.25 / −0.5 s |
| 7 (30) | **Astral Convergence** | 1 | Active, 3 min CD (req. Starfall): 20 s of +25% Arcane damage; Starbrand's periodic damage ticks twice as fast |

## 4. Gearing notes

| Spec | Wants |
|---|---|
| Verdance | Healing power, Spirit, Intellect, mp5 (HoTs don't crit — crit is nearly worthless) |
| Stormcall | Nature spell power, spell crit, Intellect, spell hit |
| Starweave | Arcane spell power, Intellect (Lunar Guidance), spell hit, crit |

Cloth with caster stats is often better than leather for Druids below 30 — an intended classic-style trade-off (and the reason Tailoring matters before cloth classes exist).

## 5. Reagents

*Seed of Renewal* (Reawaken) — 20s from reagent vendors. *Wild Thornroot* (Gift of the Grove group version, post-30).

## 6. Trainers

Hedgewarden Mirelle (Larkhill), Stonesinger Yrsa Mosshelm (Coldhearth), one in every T1/T2 town, three in each capital (The Hedgerow / The Rootvault).
