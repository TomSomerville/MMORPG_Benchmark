# Fighter

[← Master Plan](../../MASTER_PLAN.md) · [Class Framework](class-framework.md) · Next: [Cleric](cleric.md)

**Fantasy:** the professional soldier — shield-wall veteran, whirling twin-blade reaver, or greatsword executioner. **Resource:** Rage (see [Combat §3](../02-systems/combat-and-stats.md#3-resources)). **Armor:** mail (plate at 40). **Weapons:** everything except wands.

## 1. Stances

Only one stance at a time. The stance abilities share one 1 s cooldown and are off the global cooldown; changing stance sets rage to 0 (talent *Tactical Mastery* keeps some). A Fighter starts in Battle Stance. The stance bar swaps the main action bar.

| Stance | Learned | Effect | Unlocks |
|---|---|---|---|
| **Battle Stance** | 1 | No modifiers | Charge, Rend, Opening, Thunderous Stomp, Mocking Strike |
| **Guard Stance** | 10 (quest) | −10% damage taken, −10% damage dealt, threat ×1.3 | Taunt, Retaliate, Shield Block, Disarm, Shield Wall |
| **Reckless Stance** | 20 (quest) | +3% crit, +10% damage taken | Pummel, Whirlwind, Recklessness, Unbroken |

## 2. Abilities (levels 1–30)

Damage values are *rank 1 → rank at 30*. "Next swing" abilities replace the next auto-attack.

**Level 1 and level 2** (decided 2026-11-24). A new Fighter knows Attack and Strike (rank 1) and stands in Battle Stance, which is where rage comes from and is not an ability the player presses; it knows no other ability. Battle Cry (rank 1) is the first rank bought from the trainer, at level 2.

| Lvl | Ability | Cost | Cooldown | Stance | Effect | Ranks at |
|---|---|---|---|---|---|---|
| 1 | **Strike** | 15 rage | next swing | any | Weapon damage +11 → +80; extra threat | 1, 8, 16, 24 |
| 2 | **Battle Cry** | 10 | — | any | Party within 20 yd: +15 → +85 attack power, 2 min | 2, 12, 22 |
| 4 | **Charge** | 0 (gains 9 → 12 rage) | 15 s | Battle | Rush an enemy 8–25 yd away, out of combat only; stun 1 s | 4, 26 |
| 4 | **Rend** | 10 | — | Battle, Guard | Bleed: 15 → 98 over 9 → 15 s | 4, 10, 20, 30 |
| 6 | **Thunderous Stomp** | 20 | 4 s | Battle | 10 → 55 damage to up to 4 enemies within 8 yd; their attack speed −10% for 10 → 22 s | 6, 18, 28 |
| 8 | **Hamstring** | 10 | — | Battle, Reckless | 5 → 18 damage; movement −40% for 15 s | 8, 32 |
| 10 | **Taunt** | 0 | 10 s | Guard | Force target to attack you for 3 s; match top threat | — |
| 10 | **Sunder** | 15 | — | any | Target armor −90 → −270 per stack, 5 stacks, 30 s; high threat | 10, 22 |
| 10 | **Bloodletting** | 0 (costs 10% base health) | 60 s | any | Gain 10 rage now + 10 over 10 s; puts you in combat | — |
| 12 | **Opening** | 5 | 5 s | Battle | Usable for 5 s after the target dodges. Weapon damage +5 → +25; cannot be dodged, blocked or parried | 12, 28 |
| 12 | **Shield Bash** | 10 | 12 s | Battle, Guard (shield) | 6 → 45 damage; interrupts and locks the school 6 s | 12, 32 |
| 14 | **Demoralizing Roar** | 10 | — | any | Enemies within 10 yd: −45 → −110 attack power, 30 s | 14, 24 |
| 14 | **Retaliate** | 5 | 5 s | Guard | Usable after you block, dodge or parry. 12–14 → 40–50 damage; very high threat | 14, 24 |
| 16 | **Shield Block** | 10 | 5 s | Guard (shield) | +75% block chance for 5 s or 1 block | — |
| 16 | **Mocking Strike** | 10 | 2 min | Battle | 16 → 40 damage; forces target to attack you for 6 s | 16, 26 |
| 18 | **Disarm** | 20 | 60 s | Guard | Target cannot use its weapon for 10 s (mobs: −40% damage) | — |
| 20 | **Cleave** | 20 | next swing | any | Weapon damage +5 → +18 to target and one adjacent enemy | 20, 30 |
| 20 | **Dual Wield** | passive | — | — | May equip one-handed weapons in the off hand | — |
| 22 | **Intimidating Shout** | 25 | 3 min | any | Target cowers 8 s; up to 5 other enemies within 10 yd flee 8 s | — |
| 22 | **Pummel** | 10 | 10 s | Reckless | 20 damage; interrupts, locks the school 4 s | — |
| 24 | **Execute** | 15 + all remaining rage | — | Battle, Reckless | Target below 20% health only: 125 → 200 damage +3 → +6 per extra rage | 24, 32 |
| 26 | **Challenging Shout** | 5 | 10 min | any | All enemies within 10 yd attack you for 6 s | — |
| 28 | **Whirlwind** | 25 | 10 s | Reckless | Weapon damage to up to 4 enemies within 8 yd | — |
| 28 | **Shield Wall** | 0 | 30 min | Guard (shield) | −75% all damage taken for 10 s | — |
| 30 | **Slam** | 15 | 1.5 s cast | any | Weapon damage +32; resets swing timer | 30 |
| 30 | **Recklessness** | 0 | 30 min | Reckless | 15 s: +100% crit chance, immune to fear, +20% damage taken | — |
| 30 | **Unbroken** | 0 | 30 s | Reckless | 10 s: immune to fear and incapacitate; taking damage generates extra rage | — |

Passive: **Parry** (L8), **Block** (L1), **Dodge**. Ranged pulling: bows, crossbows, guns and thrown weapons use *Shoot/Throw* (no rage).

Threat, where the table gives only a word: **Strike**'s extra threat is a fixed amount on top of the threat of its damage, 20 at rank 1 and 39 at rank 2. **Sunder**'s high threat is a fixed 100 for each use.

## 3. Role playstyles at 30

- **Bulwark (tank):** Charge in Battle → swap to Guard → Sunder ×5, Retaliate on every proc, Shield Block on cooldown, Strike as rage dump; Thunderous Stomp/Demoralizing Roar for packs; Concussive Blow as stun; Shield Wall / Last Stand as emergency buttons.
- **Reaver (dual wield):** Reckless Stance. White-hit rage engine from two weapons → Whirlwind on cooldown, Strike/Cleave dump, Execute phase; Red Mist on cooldown; Unbridled Wrath and Flurry (later) feed speed.
- **Greatarms (2H):** Battle Stance. Charge → Rend → slow, heavy swings → Opening on dodges → Sweeping Strikes for cleave; Slam between swings; stance-dance to Reckless for Whirlwind using Tactical Mastery.

## 4. Talents

Format: tier (points required in tree) · talent · max rank · effect per rank. ★ = signature. Tiers 6–7 are unreachable at cap 30 (see [framework](class-framework.md#5-talents)).

### 4.1 Bulwark (tank)

| Tier | Talent | Ranks | Effect |
|---|---|---|---|
| 1 (0) | Shield Mastery | 5 | +1% block chance per rank |
| 1 | Anticipation | 5 | +2 Defense per rank |
| 2 (5) | Hardened | 5 | +2% armor from items per rank |
| 2 | Improved Bloodletting | 2 | Bloodletting gives +5 / +10 instant rage |
| 2 | Iron Will | 5 | +3% chance to resist stun and charm per rank |
| 3 (10) | **Last Stand** | 1 | Active, 10 min CD: +30% maximum health for 20 s |
| 3 | Improved Shield Block | 3 | Shield Block blocks 1 extra attack; duration +0.5 s per rank (req. Shield Mastery 5) |
| 3 | Improved Sunder | 3 | Sunder costs −1 rage per rank |
| 4 (15) | Defiance | 5 | +3% threat in Guard Stance per rank |
| 4 | Improved Retaliate | 3 | Retaliate has 15 / 30 / 45% chance to stun 3 s |
| 4 | Improved Taunt | 2 | Taunt cooldown −1 s per rank |
| 5 (20) | ★ **Concussive Blow** | 1 | Active, 15 rage, 45 s CD: stun 5 s |
| 5 | Improved Disarm | 3 | Disarm duration +1 s and cooldown −5 s per rank |
| 6 (25) | One-Hand Specialization | 5 | +2% damage with one-handed weapons per rank |
| 6 | Improved Shield Wall | 2 | Shield Wall duration +3 / +5 s |
| 7 (30) | **Shield Slam** | 1 | Active, 20 rage, 6 s CD (req. Concussive Blow): 225–235 damage + block value, dispels 1 magic effect from the enemy, high threat |

### 4.2 Reaver (dual-wield DPS)

| Tier | Talent | Ranks | Effect |
|---|---|---|---|
| 1 (0) | Cruelty | 5 | +1% melee crit per rank |
| 1 | Booming Voice | 5 | Shout duration and radius +10% per rank |
| 2 (5) | Unbridled Wrath | 5 | 8% chance per rank to gain 1 extra rage on a white hit |
| 2 | Improved Demoralizing Roar | 5 | Its attack-power reduction +8% per rank |
| 2 | **Piercing Howl** | 1 | Active, 10 rage: enemies within 10 yd dazed, −50% movement, 6 s |
| 3 (10) | Twinblade Training | 5 | Off-hand damage +5% per rank (50% → 62.5% of normal) |
| 3 | Improved Cleave | 3 | Cleave bonus damage +40 / 80 / 120% |
| 3 | Blood Craze | 3 | After being crit, regenerate 1 / 2 / 3% health over 6 s |
| 4 (15) | Enrage | 5 | After being crit: +5% melee damage per rank for 12 s (max 12 swings) |
| 4 | Improved Battle Cry | 5 | Battle Cry attack power +5% per rank |
| 4 | Improved Execute | 2 | Execute costs −2 / −5 rage |
| 5 (20) | ★ **Red Mist** | 1 | Active, 10 rage, 3 min CD (req. Enrage 5): 30 s of +20% physical damage and fear immunity, but +20% damage taken |
| 5 | Improved Pummel | 2 | Pummel lockout +1 / +2 s |
| 6 (25) | Flurry | 5 | After a melee crit, attack speed +10 / 15 / 20 / 25 / 30% for the next 3 swings |
| 6 | Improved Reckless Stance | 5 | +1% crit in Reckless Stance per rank; damage-taken penalty −1% per rank |
| 7 (30) | **Bloodreave** | 1 | Active, 30 rage, 6 s CD (req. Red Mist): instant attack for 45% of attack power; your next 5 hits heal you for 10 each |

### 4.3 Greatarms (two-handed DPS)

| Tier | Talent | Ranks | Effect |
|---|---|---|---|
| 1 (0) | Improved Strike | 3 | Strike costs −1 rage per rank |
| 1 | Deflection | 5 | +1% parry per rank |
| 1 | Improved Rend | 3 | Rend bleed damage +15 / 25 / 35% |
| 2 (5) | Improved Charge | 2 | Charge generates +3 / +6 rage |
| 2 | Tactical Mastery | 5 | Keep up to 5 rage per rank when changing stance |
| 2 | Improved Thunderous Stomp | 3 | Costs −1 / −2 / −4 rage; slow +2% per rank |
| 3 (10) | Improved Opening | 2 | Opening crit chance +25 / +50% |
| 3 | **Anger Management** | 1 | Out-of-combat rage decay 30% slower; +1 rage per 3 s in combat |
| 3 | Deep Wounds | 3 | Your melee crits bleed for 20 / 40 / 60% of average weapon damage over 12 s |
| 4 (15) | Two-Hand Specialization | 5 | +1% damage with two-handed weapons per rank |
| 4 | Impale | 2 | Ability crit damage bonus +10 / +20% (req. Deep Wounds 3) |
| 5 (20) | ★ **Sweeping Strikes** | 1 | Active, 30 rage, 30 s CD: your next 5 melee attacks also strike one additional nearby enemy |
| 5 | Weapon Mastery | 5 | By equipped type, per rank — axes/polearms: +1% crit; maces: 1% chance to stun 3 s; swords: 1% chance for an extra attack |
| 6 (25) | Improved Hamstring | 3 | Hamstring has 5 / 10 / 15% chance to root for 5 s |
| 6 | Trauma | 2 | Your crits make the target take +15 / +30% bleed damage for 15 s |
| 7 (30) | **Grievous Strike** | 1 | Active, 30 rage, 6 s CD (req. Sweeping Strikes): weapon damage +85; target's healing received −50% for 10 s |

## 5. Gearing notes

| Spec | Wants | Weapons |
|---|---|---|
| Bulwark | Stamina, Strength, Defense, armor, block | 1H + shield (fast 1H for rage and threat) |
| Reaver | Strength, Agility, crit, hit (dual-wield miss is punishing — hit is king) | Slow main hand, fast off hand |
| Greatarms | Strength, crit, Stamina | Slowest, highest top-end 2H |

## 6. Trainers

Sergeant Tobias Kern (Larkhill), Dale-Sergeant Hakon Shieldwall (Sunbank), Battlemaster Kol Ironvow (Coldhearth), one in every T1/T2 town, three in each capital. Class quests: [framework §6](class-framework.md#6-class-quests).
