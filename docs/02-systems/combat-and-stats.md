# Combat & Stats

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Progression](progression.md) · Next: [Items & Loot](items-and-loot.md)

Tab-target, global-cooldown combat in the classic style. All numbers are **balance v0** — a coherent first pass. During the build they are tuned only where the combat simulator misses the targets in §11; after that, by play. Small rules not given here (movement speeds, ranges, timers, skill gains) are in the [Rules Reference](rules-reference.md).

## 1. Primary attributes

| Attribute | Effect |
|---|---|
| **Strength** | Fighter, Cleric: 2 attack power (AP) per point. Druid: 1 AP. Also block value: Str / 20 |
| **Agility** | Crit and dodge (table below); 2 armor per point |
| **Stamina** | 10 health per point (first 20 points give 1 each) |
| **Intellect** | 15 mana per point (first 20 give 1 each); spell crit |
| **Spirit** | Out-of-combat health regen; mana regen outside the five-second rule |

| Class | Agi per 1% melee crit | Agi per 1% dodge | Int per 1% spell crit |
|---|---|---|---|
| Fighter | `5 + 0.25 × level` (L30: 12.5) | same | — |
| Cleric | `5 + 0.25 × level` | same | `12 + 0.7 × level` (L30: 33) |
| Druid | `5 + 0.25 × level` | same | `12 + 0.8 × level` (L30: 36) |

Base crit 5% melee; base spell crit Cleric 3.5%, Druid 1.8%. Base dodge: Fighter 0%, Cleric 0.7%, Druid 0.9%.

## 2. Derived stats

| Stat | Rule |
|---|---|
| Attack power | 14 AP = +1 weapon DPS |
| Melee swing damage | `weaponDamage + AP / 14 × weaponSpeed` |
| Armor | Physical damage reduction = `armor / (armor + 400 + 85 × attackerLevel)`, cap 75% |
| Defense skill | 5 per level cap. Each point above attacker's weapon skill: +0.04% miss, dodge, parry, block and −0.04% chance to be crit |
| Weapon skill | 5 per level cap, per weapon type; raised by use. Each point below target defense: −0.04% hit/crit (a classic system, kept by decision on 2026-11-12) |
| Block | Blocks reduce the hit by block value (`shield value + Str / 20`) |
| Parry | Fighter and Cleric base 5%; parrying speeds the parrier's next swing by 40% |
| Spell power | Added to spells by coefficient (§6) |
| Resistances | Fire, Frost, Nature, Arcane, Shadow. Average reduction = `resist / (attackerLevel × 5) × 75%`, applied in 0/25/50/75/100% partial bands. Holy cannot be resisted |
| Health regen | Out of combat only: Spirit-based (Fighter `Spi × 0.8 + 6` per 2 s); eating restores far more |
| Mana regen | Per 2 s outside five-second rule: Cleric `Spi / 5 + 15`, Druid `Spi / 4.5 + 15`. **Five-second rule:** no Spirit regen for 5 s after spending mana. "mp5" on gear always applies |

## 3. Resources

| Resource | Class | Rules |
|---|---|---|
| **Rage** (0–100) | Fighter | Starts at 0. Gained from dealing damage: `damage / c × 7.5`; from taking damage: `damage / c × 2.5`; where `c = 0.0091 × L² + 3.2256 × L + 4.2653` (L30 ≈ 109). Decays 1/s after 5 s out of combat. Lost on stance change (see talents) |
| **Mana** | Cleric, Druid | Pool from Intellect + class base. Drinking restores out of combat |
| *Energy, focus, combo points, soul shards* | *future classes* | The resource is a field on the class record; adding one means adding a regen rule, not rewriting combat |

## 4. The melee attack table (single roll)

Player attacking a same-level mob from the front, in order of priority:

| Outcome | Base chance | Notes |
|---|---|---|
| Miss | 5% (24% dual-wielding) | +1% per level the target is above you (+2% from +3) |
| Dodge | 5% | Cannot dodge from behind is **not** applied to mobs; players cannot dodge/parry/block from behind |
| Parry | 5% (humanoid mobs) | Front only |
| Glancing blow | 10% + 10% per level above | White hits only; 70% damage at equal skill |
| Block | 5% (shield mobs) | Front only |
| Critical | crit% | ×2 damage |
| Crushing blow | 0% | Mobs only, when ≥ 3 levels above the defender: 150% damage. Raid bosses are level 33, so tank defense matters |
| Ordinary hit | remainder | |

Yellow (ability) attacks use a two-roll system: hit/avoid first, then crit.

**Dual wield:** off-hand deals 50% damage; both hands suffer +19% miss on white swings. Abilities use main-hand hit chance.

## 5. Spells

| Rule | Value |
|---|---|
| Global cooldown | 1.5 s for all spells and most abilities |
| Spell hit vs same level | 96%; −1% per level above (−11% at +3); never above 99% |
| Spell crit | ×1.5 damage/healing (talents can raise) |
| Cast pushback | Each damaging hit adds 1.0 s to a cast (first two hits), then 0.5 s; channel loses 25% per hit |
| Interrupts | Interrupt effects lock the interrupted **school** for 3–6 s |
| Range | Melee 5 yd; most spells 30 yd; heals 40 yd |
| Line of sight & facing | Required for casts; 180° frontal arc for melee and direct spells |
| Movement | Cancels any spell with a cast time |
| Schools | Physical, Holy, Nature, Arcane, Fire, Frost, Shadow |

## 6. Spell power coefficients

- Direct spell: `castTime / 3.5` (instant = 1.5 / 3.5 = 43%).
- Over-time effect: `duration / 15`, split evenly across ticks (max 100%).
- Hybrid (direct + over-time): each part scaled by its share.
- AoE: one-third of the single-target coefficient.
- Spells learned below level 20 lose `(20 − learnLevel) × 3.75%` of their coefficient.

## 7. Threat

| Action | Threat |
|---|---|
| 1 damage | 1 |
| 1 healing done | 0.5 (split among mobs in combat) |
| Gaining a resource from an ability | 5 per point |
| Buffs / debuffs | Fixed amount per spell |
| Fighter Guard Stance | ×1.3 |
| Cleric Righteous Bulwark | Holy damage ×1.6 |
| Taunt | Sets caster's threat equal to the current top and forces attack for 3 s |

A mob switches target when another unit exceeds **110%** of its current target's threat in melee range, **130%** at range. Threat is wiped on evade.

## 8. Crowd control & diminishing returns

Categories: stun, root, fear, incapacitate (breaks on damage), sleep, disarm, silence/interrupt, snare. Against **players**, repeated effects of the same category within 15 s last 100% → 50% → 25% → immune. Against mobs, no diminishing returns; raid bosses are immune to most control.

## 9. Buff and debuff rules

- Buff cap 32, debuff cap 40 per unit (no artificial 16-slot limit).
- Same-name buffs do not stack; a higher rank overwrites a lower one.
- Categories that are mutually exclusive are declared in data (e.g. one Cleric Benediction per caster per target; one Litany per Cleric; one Oath active).
- Dispel types: Magic, Curse, Disease, Poison. Who removes what: Cleric — Disease, Poison (Purify); Druid — Poison (Cleanse Toxin), Curse (Lift Curse). **No launch class removes Magic from allies** (Fighter's Shield Slam dispels enemies) — dungeon design must respect this.

## 10. Combat flow

| Rule | Value |
|---|---|
| Auto-attack | Toggle; swing timer per hand |
| Entering combat | On dealing/taking damage or aggro; blocks eating, mounting and some abilities |
| Leaving combat | 5 s after no hostile unit has you on its threat list |
| Aggro radius | 20 yd at equal level, ±1 yd per level difference, min 5, max 45 |
| Social pull | Mobs of the same family within 10 yd assist |
| Leash / evade | Mob resets if pulled > 60 yd from spawn or cannot path: runs home, heals to full |
| Fleeing | Humanoids flee at 15% health and may bring friends |
| Tapping | First damage tags the mob for XP/loot for that player or group |
| Level difference | +3 or more: big miss/resist penalties, crushing blows. Skull level = more than 10 above |
| Falling | Damage from 15 yd; lethal around 65 yd |
| Drowning | After 60 s breath: 10% max health per 2 s |

## 11. Role balance targets at level 30 (v0)

| Role | Target |
|---|---|
| DPS in quest greens | 70–85 DPS sustained |
| DPS in dungeon blues | 95–115 |
| DPS in raid epics | 125–150 |
| Tank health in dungeon blues | 1,900–2,200; armor 45–50% reduction |
| Healer throughput | 140–180 HPS sustained, mana for a 4–5 min fight |
| Solo kill time, same-level mob | 12–18 s; player ends at 60–75% health |
