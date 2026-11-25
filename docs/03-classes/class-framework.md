# Class Framework

[← Master Plan](../../MASTER_PLAN.md) · Prev: [UI & Controls](../02-systems/ui-and-controls.md) · Next: [Fighter](fighter.md) · [Cleric](cleric.md) · [Druid](druid.md)

## 1. Launch classes and roles

| Class | Resource | Armor (to 39) | Tree 1 | Tree 2 | Tree 3 |
|---|---|---|---|---|---|
| [**Fighter**](fighter.md) | Rage | Mail + shield | **Bulwark** — tank | **Reaver** — dual-wield melee DPS | **Greatarms** — two-handed melee DPS |
| [**Cleric**](cleric.md) | Mana | Mail + shield | **Aegis** — tank | **Grace** — healer | **Reckoning** — two-handed melee DPS |
| [**Druid**](druid.md) | Mana | Leather / cloth | **Verdance** — heal-over-time healer | **Stormcall** — Nature ranged DPS | **Starweave** — Arcane ranged DPS |

Role coverage: 2 tank specs, 2 healer specs, 2 melee DPS specs + 1 hybrid, 2 ranged DPS specs. A 5-player dungeon group can always be formed from the three classes.

## 2. Class as data (extensibility)

A **class record** holds: id, name, resource type, base stats and per-level growth, armor/weapon proficiencies, allowed races, spell list (spell id + learn level + trainer cost), three talent trees, starting gear, class quest ids, UI colour.

Adding Warlock, Rogue or Archer later means:
1. A class record and its spells/talents (data).
2. Any **new mechanics** the class needs, added once as reusable spell-effect or resource types — e.g. *energy + combo points* (Rogue), *pet control* (Warlock, Archer), *ranged auto-shot + ammo* (Archer), *stealth* (Rogue). The pet bar, stealth detection racials and ammo slot are already reserved in UI and item design so these do not require rework.
3. Art: armor fits all races automatically (armor is per-skeleton, not per-class); only spell effects and class-set models are new.

Planned class identities (for consistency of future design): **Warlock** — Shadow/Fire caster with summoned thralls (the Hollow), cloth; **Rogue** — energy/combo stealth melee, leather; **Archer** — ranged physical with a beast companion, leather→mail.

## 3. Base stats

Class contribution added to racial base at level 1, and average gain per level:

| Class | Str | Agi | Sta | Int | Spi | Gain/level (Str/Agi/Sta/Int/Spi) |
|---|---|---|---|---|---|---|
| Fighter | +3 | 0 | +2 | 0 | 0 | 1.35 / 0.8 / 1.2 / 0.15 / 0.4 |
| Cleric | +2 | 0 | +2 | 0 | +1 | 1.1 / 0.6 / 1.1 / 0.7 / 0.75 |
| Druid | +1 | 0 | 0 | +2 | +2 | 0.55 / 0.6 / 0.7 / 1.15 / 1.25 |

| Class | Base health L1 / 10 / 20 / 30 | Base mana L1 / 10 / 20 / 30 |
|---|---|---|
| Fighter | 60 / 200 / 430 / 690 | — |
| Cleric | 58 / 190 / 400 / 640 | 80 / 300 / 590 / 900 |
| Druid | 54 / 170 / 350 / 560 | 100 / 350 / 680 / 1,050 |

(Base health/mana is before Stamina/Intellect.)

## 4. Abilities

- Learned from class trainers at even levels (cost table in [Progression](../02-systems/progression.md#9-ability-training)); a few come from **class quests**.
- Most abilities have **ranks**; a new rank roughly every 6–8 levels. Lower ranks stay castable.
- Each ability is a **spell record**: school, cost, cast time, cooldown, GCD flag, range, target rules, a list of effects (damage, heal, apply aura, summon, teleport, dispel, threat…), an optional aura (periodic damage/heal, stat mod, control, proc trigger), required stance/weapon, and visuals. See [Data Model](../08-tech/data-model.md).
- In the class files, the value shown is **rank 1 at learn level → highest rank available by 30**, before spell power/attack power.

## 5. Talents

- 1 point per level from **level 10**: 21 points at cap 30, 51 at 60.
- Three trees per class, **7 tiers**. Tier N needs `5 × (N − 1)` points spent in that tree. Some talents require a specific earlier talent (shown as "req.").
- Tier 5 holds each tree's **signature** ability (needs 20 points → available at level 30 with the 21st point). Tiers 6–7 are fully designed below but unreachable until the cap rises past 30 — this is deliberate so launch builds remain valid forever.
- Respec at a class trainer (cost in [Economy](../02-systems/economy-and-social.md#3-sinks)).
- A talent is a data record: tree, tier, column, max rank, prerequisite, and per-rank spell id (passive aura or a taught ability). No talent needs custom code beyond the spell-effect library.

Typical builds at 30: 21/0/0 for a pure role, or 16/5/0-style mixes that give up the signature for utility.

## 6. Class quests

| Level | Fighter | Cleric | Druid |
|---|---|---|---|
| 10 | *The Shield-Wall Lesson* → **Guard Stance**, Taunt, Sunder | *Vigil of the First Flame* → **Raise the Fallen** (granted at 12 on completion of part 2) and a class mace | *The Circle's Welcome* → **Overgrowth** and a staff |
| 20 | *Trial of the Red Field* → **Reckless Stance**; choice of a blue 2H or pair of 1H weapons | *The Oath Unbroken* → **Hallowed Ground**; blue shield or 2H mace | *Seed of the Old Wood* → **Reawaken**; held off-hand or 1H mace |
| 30 | *Bladebound* → blue class weapon (pre-raid) | *The Dawnbearer's Charge* → blue psalter relic | *Convergence* → blue charm relic |

Each class quest has identical versions on both continents (trainer in either capital starts it; objectives are in the nearest T2/T3/T4 zone).

## 7. Shared design rules

1. **Every spec must be able to solo-level.** Healers and tanks get enough damage to kill at ~75% of a DPS spec's speed.
2. **No required interrupts or magic-dispels** in content until a class can reliably provide them (see [Combat §9](../02-systems/combat-and-stats.md#9-buff-and-debuff-rules)).
3. **Group buffs** come from all three classes so every party composition has some: Fighter *Battle Cry* (AP), Cleric *Benedictions/Litanies*, Druid *Gift of the Grove*/*Briarskin*.
4. **Out-of-combat resurrection:** Cleric only. **Combat resurrection:** Druid only.
5. Tooltips state exact numbers. No hidden mechanics.
