# Cleric

[← Master Plan](../../MASTER_PLAN.md) · [Class Framework](class-framework.md) · Prev: [Fighter](fighter.md) · Next: [Druid](druid.md)

**Fantasy:** an armoured priest of the Twin Flames — hammer in hand, Dawnflame on the tongue. Physical combat flavoured with Holy magic. **Resource:** Mana. **Armor:** mail + shield (plate at 40). **Weapons:** one- and two-handed maces and swords, polearms (20). **Relic slot:** Psalter.

## 1. Core mechanics

| Mechanic | Rule |
|---|---|
| **Oaths** | A self-buff on your weapon lasting 30 s. Only one Oath active. Each Oath changes what your melee swings do |
| **Verdict** | Instant, 10 s cooldown, 10 yd. *Consumes* your active Oath to deliver that Oath's Verdict effect on the enemy. The Oath → Verdict → re-Oath loop is the Cleric's rotation |
| **Litanies** | Aura affecting the party within 30 yd. One Litany per Cleric; free, permanent until changed |
| **Benedictions** | 5-minute buff on one friendly target. One Benediction per Cleric per target |
| **Holy school** | Cannot be resisted; cannot be locked out by most mob silences (still interruptible) |

## 2. Abilities (levels 1–30)

Mana costs given as rank 1 → rank at 30.

| Lvl | Ability | Cost | Cast / CD | Effect | Ranks at |
|---|---|---|---|---|---|
| 1 | **Oath of Radiance** | 20 → 90 | instant | 30 s: each swing deals +3 → +22 Holy damage (scaled by weapon speed). **Verdict:** 12 → 70 Holy damage | 1, 10, 18, 26 |
| 1 | **Mending Light** | 35 → 275 | 2.5 s | Heal 42 → 370 | 1, 6, 14, 22, 30 |
| 1 | **Litany of Resolve** | — | aura | Party armor +55 → +330 | 1, 10, 20, 30 |
| 4 | **Verdict** | 5% base mana | instant / 10 s | Consumes Oath for its Verdict effect | — |
| 4 | **Benediction of Might** | 20 → 60 | instant | +20 → +85 attack power, 5 min | 4, 12, 22 |
| 6 | **Dawnstrike** | 4% base mana | instant / 6 s | Weapon damage +8 → +45 as Holy-infused physical; refreshes all active Verdict debuffs on the target | 6, 14, 22, 30 |
| 6 | **Divine Ward** | 15 | instant / 5 min | Immune to all damage for 6 s; you cannot attack. Causes *Forbearance* (no Ward/Protection for 1 min) | 6, 18 (8 s) |
| 8 | **Oath of the Zealot** | 25 → 80 | instant | 30 s: +30 → +125 attack power but each swing deals 40% less (builds threat/speed feel). **Verdict:** target takes +20 → +80 Holy damage from all Holy hits for 10 s | 8, 16, 24 |
| 8 | **Hammer of Rebuke** | 30 | instant / 60 s | 10 yd: stun 3 → 4 s | 8, 24 |
| 8 | **Purify** | 6% base mana | instant | Remove 1 disease and 1 poison from a friendly target | — |
| 10 | **Dawn's Mercy** | all mana | instant / 60 min | Heal a friendly target for your maximum health | — |
| 10 | **Benediction of Protection** | 6% base mana | instant / 5 min | Ally immune to physical damage for 6 → 8 s, cannot attack. Forbearance | 10, 24 |
| 12 | **Raise the Fallen** | 60% base mana | 10 s | Out of combat: resurrect a dead player at 20% health/mana (class quest) | — |
| 14 | **Benediction of Wisdom** | 30 → 55 | instant | +10 → +20 mana per 5 s, 5 min | 14, 24 |
| 16 | **Challenge of Faith** | 3% base mana | instant / 10 s | Taunt: target attacks you for 3 s; match top threat. *(Deliberate improvement over the classic archetype, which had no taunt)* | — |
| 16 | **Righteous Bulwark** | 20% base mana | instant | 30 min self-buff: Holy damage threat +60% | — |
| 16 | **Litany of Thorns** | — | aura | Attackers of party members take 5 → 12 Holy damage | 16, 26 |
| 18 | **Benediction of Freedom** | 6% base mana | instant / 20 s | Ally immune to movement-impairing effects for 10 s | — |
| 20 | **Flash of Dawn** | 35 → 70 | 1.5 s | Heal 65 → 140 (fast, efficient, small) | 20, 26 |
| 20 | **Hallowed Ground** | 135 → 235 | instant / 8 s | Consecrate 8 yd around you: 64 → 160 Holy damage over 8 s to enemies inside (class quest) | 20, 30 |
| 20 | **Exorcise** | 85 → 135 | instant / 15 s | 30 yd: 90–102 → 160–180 Holy damage to an Undead or Aberration | 20, 28 |
| 20 | **Sense Undead** | — | toggle | Shows undead on the minimap | — |
| 22 | **Litany of Focus** | — | aura | Party: 35% chance to ignore cast pushback | — |
| 22 | **Oath of Justice** | 50 | instant | 30 s: swings have a chance to stun 2 s (≈ 5 procs/min, not on bosses). **Verdict:** target cannot flee for 10 s | — |
| 24 | **Rebuke Undead** | 9% base mana | 1.5 s / 30 s | Undead target flees for 10 → 15 s | 24 |
| 26 | **Benediction of Salvation** | 6% base mana | instant | Ally's threat generation −30%, 5 min | — |
| 30 | **Oath of Light** | 60 | instant | 30 s: swings have a chance to heal you for 39. **Verdict:** melee attackers of the target have a chance to be healed for 25, 10 s | — |

Passives: Block (1), Parry (8).

Rules the table states briefly:

- **Oath swing damage and weapon speed.** An Oath's extra Holy damage on a swing is the stated amount for a 2.0 s swing, multiplied by `weapon speed ÷ 2.0`: a 3.0 s weapon deals one and a half times the figure, a 1.6 s weapon four fifths of it.
- **Oath of the Zealot.** Its 40% reduction applies to all the Cleric's physical damage while the Oath is up, so to Dawnstrike as well as to swings.
- **Forbearance** is a debuff: the Cleric or ally who carries it cannot cancel it, and it runs its full minute.

## 3. Role playstyles at 30

- **Aegis (tank):** Righteous Bulwark on; Litany of Resolve or Thorns. Pull with Verdict (Radiance) → Hallowed Ground under the pack → Shield of Dawn on cooldown (blocks deal Holy damage) → Dawnstrike/Oath/Verdict loop. Strongest AoE tank; weaker single-target burst threat than a Bulwark Fighter. Mana is the limit — getting hit and Benediction of Wisdom sustain it.
- **Grace (healer):** Mending Light as the workhorse, Flash of Dawn for efficiency, Divine Favor + Mending Light for emergencies, Dawn's Mercy as the oh-no button; Benedictions on everyone; Purify. A direct-heal, single-target, armoured healer who can stand in melee — the opposite of the Druid's pre-emptive HoTs.
- **Reckoning (2H DPS):** Oath of Command (talent) → Verdict → Dawnstrike on cooldown, Exorcise on undead, Hammer of Rebuke into a Verdict for double damage; Sanctity Litany buffs the party's Holy damage. Bursty, proc-driven.

## 4. Talents

### 4.1 Aegis (tank)

| Tier | Talent | Ranks | Effect |
|---|---|---|---|
| 1 (0) | Improved Litany of Resolve | 5 | Litany of Resolve armor +5% per rank |
| 1 | Redoubt | 5 | After being crit: +6% block chance per rank for 10 s or 5 blocks |
| 2 (5) | Precision | 3 | +1% melee hit per rank |
| 2 | Guardian's Favor | 2 | Benediction of Protection CD −60 s per rank; Freedom +3 s per rank |
| 2 | Toughness | 5 | +2% armor from items per rank |
| 3 (10) | **Benediction of Kings** | 1 | New Benediction: +10% to all attributes, 5 min |
| 3 | Improved Righteous Bulwark | 3 | Its threat bonus +16 / 33 / 50%; while active, damage taken −2 / 4 / 6% |
| 3 | Shield Specialization | 3 | Amount blocked +10 / 20 / 30% (req. Redoubt 5) |
| 4 (15) | Anticipation | 5 | +2 Defense per rank |
| 4 | Improved Hammer of Rebuke | 3 | Cooldown −5 s per rank |
| 4 | Stalwart Challenge | 2 | Challenge of Faith cooldown −1 s per rank and +2 yd range per rank |
| 5 (20) | ★ **Shield of Dawn** | 1 | Active, 10 s CD (req. Benediction of Kings): 10 s or 4 blocks of +30% block chance; each block deals 35 Holy damage with +20% threat |
| 5 | Requital | 5 | 2% chance per rank after being hit to gain an extra attack; 20% per rank when crit |
| 6 (25) | One-Handed Mastery | 5 | +2% damage with one-handed weapons per rank |
| 6 | Sacred Duty | 2 | Stamina +3 / +6%; Divine Ward no longer prevents attacking for the first 2 / 4 s |
| 7 (30) | **Dawnbreaker Shield** | 1 | Active, 30 s CD (req. Shield of Dawn): hurl your shield at 30 yd — 270–330 Holy damage, bounces to 2 more enemies, dazes 6 s |

### 4.2 Grace (healer)

| Tier | Talent | Ranks | Effect |
|---|---|---|---|
| 1 (0) | Divine Intellect | 5 | Intellect +2% per rank |
| 1 | Spiritual Focus | 5 | 14% chance per rank to avoid pushback on Mending Light and Flash of Dawn |
| 2 (5) | Healing Light | 3 | Mending Light and Flash of Dawn heal +4% per rank |
| 2 | Improved Oath of Radiance | 5 | Its damage (swing and Verdict) +3% per rank |
| 2 | Improved Dawn's Mercy | 2 | Target also gains +15 / +30% armor for 2 min; cooldown −10 / −20 min |
| 3 (10) | Illumination | 5 | After a critical heal, 20% chance per rank to refund its mana cost |
| 3 | Unyielding Faith | 2 | +5 / +10% chance to resist fear and disorient |
| 3 | Improved Benediction of Wisdom | 2 | Its mana regeneration +10 / +20% |
| 4 (15) | **Divine Favor** | 1 | Active, 2 min CD (req. Illumination 5): your next heal is a guaranteed crit |
| 4 | Lasting Verdict | 3 | Verdict debuffs last +10 s per rank |
| 5 (20) | ★ **Light's Grace** | 1 | Each Mending Light cast reduces the cast time of your next Mending Light by 0.5 s (15 s window) and heals the target for an additional 10% over 6 s |
| 5 | Holy Power | 5 | +1% crit with Holy spells per rank |
| 6 (25) | Purifying Power | 2 | Purify costs 25 / 50% less mana; rank 2 also adds +10% crit to Exorcise |
| 6 | Radiant Reach | 2 | Range of heals and Verdict +10 / +20% |
| 7 (30) | **Dawnshock** | 1 | Active, 30 s CD (req. Divine Favor): instant — heal an ally for 204–220 or deal that much Holy damage to an enemy, 20 yd |

### 4.3 Reckoning (two-handed DPS)

| Tier | Talent | Ranks | Effect |
|---|---|---|---|
| 1 (0) | Improved Benediction of Might | 5 | Its attack power +4% per rank |
| 1 | Benefaction | 5 | Oaths and Verdict cost −3% mana per rank |
| 2 (5) | Improved Verdict | 2 | Verdict cooldown −1 s per rank |
| 2 | Improved Oath of the Zealot | 3 | Its attack power and Verdict bonus +5% per rank |
| 2 | Deflection | 5 | +1% parry per rank |
| 3 (10) | Conviction | 5 | +1% melee crit per rank |
| 3 | **Oath of Command** | 1 | New Oath: swings have a chance (7 procs/min) to deal 70% weapon damage as Holy. **Verdict:** 46–51 → 110–122 Holy damage, doubled if the target is stunned |
| 3 | Pursuit of Justice | 2 | Movement speed +4 / +8% (also mounted) |
| 4 (15) | Two-Handed Mastery | 3 | +2% damage with two-handed weapons per rank |
| 4 | Eye for an Eye | 2 | When you are hit by a spell crit, the caster takes 15 / 30% of that damage |
| 5 (20) | ★ **Litany of Sanctity** | 1 | New Litany: party Holy damage +10% (req. Oath of Command) |
| 5 | Vengeance | 5 | After you crit: +3% physical and Holy damage per rank for 8 s |
| 6 (25) | **Rebuke** | 1 | Active, 30 s CD: interrupt a cast, lock the school 4 s |
| 6 | Improved Litany of Thorns | 2 | Its damage +25 / +50% |
| 7 (30) | **Avenging Dawn** | 1 | Active, 3 min CD (req. Litany of Sanctity): 20 s of +30% damage dealt; wings of light. Forbearance |

## 5. Gearing notes

| Spec | Wants | Weapons |
|---|---|---|
| Aegis | Stamina, Defense, block value, Intellect (mana pool = threat), spell power for threat | 1H + shield; fast 1H |
| Grace | Intellect, healing power, spell crit (Illumination), mp5 | 1H mace + shield |
| Reckoning | Strength, crit, slow 2H (Oath of Command scales with weapon damage), a little Intellect | Slow 2H mace/sword/polearm |

## 6. Trainers

Brother Aldwin (Larkhill), Hearthpriest Magna Coalbright (Coldhearth), one in every T1/T2 town, three in each capital (Dawnspire Close / Hall of Embers).
