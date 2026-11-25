# Spell Data — every ability, every rank

← [Data Index](00-data-index.md) · Classes: [Fighter](../03-classes/fighter.md) · [Cleric](../03-classes/cleric.md) · [Druid](../03-classes/druid.md)

Generated from the ability tables in the class documents using the rules in the [Data Index](00-data-index.md#3-spell-rules). **Do not edit by hand.** One row per rank. Values between the first and last rank are interpolated in a straight line by the level at which each rank is learned. Ranks learned above level 30 are listed as reserved.

## Fighter

| ID | Ability | Rank | Level | Training | School | Cost | Cast / cooldown | Range | GCD | Coefficient | Effect |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SPL-FIG-01-r1 | Strike | 1 | 1 | free | Physical | 15 rage | next swing | melee | no | — | Weapon damage +11; extra threat |
| SPL-FIG-01-r2 | Strike | 2 | 8 | 5s | Physical | 15 rage | next swing | melee | no | — | Weapon damage +32; extra threat |
| SPL-FIG-01-r3 | Strike | 3 | 16 | 30s | Physical | 15 rage | next swing | melee | no | — | Weapon damage +56; extra threat |
| SPL-FIG-01-r4 | Strike | 4 | 24 | 1g | Physical | 15 rage | next swing | melee | no | — | Weapon damage +80; extra threat |
| SPL-FIG-02-r1 | Battle Cry | 1 | 1 | free | Physical | 10 | — | 20 yd | yes | — | Party within 20 yd: +15 attack power, 2 min |
| SPL-FIG-02-r2 | Battle Cry | 2 | 12 | 12s | Physical | 10 | — | 20 yd | yes | — | Party within 20 yd: +52 attack power, 2 min |
| SPL-FIG-02-r3 | Battle Cry | 3 | 22 | 80s | Physical | 10 | — | 20 yd | yes | — | Party within 20 yd: +85 attack power, 2 min |
| SPL-FIG-03-r1 | Charge | 1 | 4 | 1s | Physical | 0 (gains 9 rage) | 15 s | 25 yd | yes | — | [Battle] Rush an enemy 8–25 yd away, out of combat only; stun 1 s |
| SPL-FIG-03-r2 | Charge | 2 | 26 | 1g 20s | Physical | 0 (gains 12 rage) | 15 s | 25 yd | yes | — | [Battle] Rush an enemy 8–25 yd away, out of combat only; stun 1 s |
| SPL-FIG-04-r1 | Rend | 1 | 4 | 1s | Physical | 10 | — | melee | yes | — | [Battle, Guard] Bleed: 15 over 9 s |
| SPL-FIG-04-r2 | Rend | 2 | 10 | 8s | Physical | 10 | — | melee | yes | — | [Battle, Guard] Bleed: 34 over 10 s |
| SPL-FIG-04-r3 | Rend | 3 | 20 | 60s | Physical | 10 | — | melee | yes | — | [Battle, Guard] Bleed: 66 over 13 s |
| SPL-FIG-04-r4 | Rend | 4 | 30 | 1g 60s | Physical | 10 | — | melee | yes | — | [Battle, Guard] Bleed: 98 over 15 s |
| SPL-FIG-05-r1 | Thunderous Stomp | 1 | 6 | 2s | Physical | 20 | 4 s | 8 yd | yes | — | [Battle] 10 damage to up to 4 enemies within 8 yd; their attack speed −10% for 10 s |
| SPL-FIG-05-r2 | Thunderous Stomp | 2 | 18 | 50s | Physical | 20 | 4 s | 8 yd | yes | — | [Battle] 35 damage to up to 4 enemies within 8 yd; their attack speed −10% for 17 s |
| SPL-FIG-05-r3 | Thunderous Stomp | 3 | 28 | 1g 40s | Physical | 20 | 4 s | 8 yd | yes | — | [Battle] 55 damage to up to 4 enemies within 8 yd; their attack speed −10% for 22 s |
| SPL-FIG-06-r1 | Hamstring | 1 | 8 | 5s | Physical | 10 | — | melee | yes | — | [Battle, Reckless] 5 damage; movement −40% for 15 s |
| SPL-FIG-06-r2 | Hamstring | 2 | 32 (above cap) | reserved | Physical | 10 | — | melee | yes | — | [Battle, Reckless] 18 damage; movement −40% for 15 s |
| SPL-FIG-07 | Taunt | 1 | 10 | 8s | Physical | 0 | 10 s | melee | yes | — | [Guard] Force target to attack you for 3 s; match top threat |
| SPL-FIG-08-r1 | Sunder | 1 | 10 | 8s | Physical | 15 | — | melee | yes | — | Target armor −90 per stack, 5 stacks, 30 s; high threat |
| SPL-FIG-08-r2 | Sunder | 2 | 22 | 80s | Physical | 15 | — | melee | yes | — | Target armor −270 per stack, 5 stacks, 30 s; high threat |
| SPL-FIG-09 | Bloodletting | 1 | 10 | 8s | Physical | 0 (costs 10% base health) | 60 s | self | yes | — | Gain 10 rage now + 10 over 10 s; puts you in combat |
| SPL-FIG-10-r1 | Opening | 1 | 12 | 12s | Physical | 5 | 5 s | melee | yes | — | [Battle] Usable for 5 s after the target dodges. Weapon damage +5; cannot be dodged, blocked or parried |
| SPL-FIG-10-r2 | Opening | 2 | 28 | 1g 40s | Physical | 5 | 5 s | melee | yes | — | [Battle] Usable for 5 s after the target dodges. Weapon damage +25; cannot be dodged, blocked or parried |
| SPL-FIG-11-r1 | Shield Bash | 1 | 12 | 12s | Physical | 10 | 12 s | melee | yes | — | [Battle, Guard (shield)] 6 damage; interrupts and locks the school 6 s |
| SPL-FIG-11-r2 | Shield Bash | 2 | 32 (above cap) | reserved | Physical | 10 | 12 s | melee | yes | — | [Battle, Guard (shield)] 45 damage; interrupts and locks the school 6 s |
| SPL-FIG-12-r1 | Demoralizing Roar | 1 | 14 | 20s | Physical | 10 | — | 10 yd | yes | — | Enemies within 10 yd: −45 attack power, 30 s |
| SPL-FIG-12-r2 | Demoralizing Roar | 2 | 24 | 1g | Physical | 10 | — | 10 yd | yes | — | Enemies within 10 yd: −110 attack power, 30 s |
| SPL-FIG-13-r1 | Retaliate | 1 | 14 | 20s | Physical | 5 | 5 s | melee | yes | — | [Guard] Usable after you block, dodge or parry. 12–14 damage; very high threat |
| SPL-FIG-13-r2 | Retaliate | 2 | 24 | 1g | Physical | 5 | 5 s | melee | yes | — | [Guard] Usable after you block, dodge or parry. 40–50 damage; very high threat |
| SPL-FIG-14 | Shield Block | 1 | 16 | 30s | Physical | 10 | 5 s | melee | yes | — | [Guard (shield)] +75% block chance for 5 s or 1 block |
| SPL-FIG-15-r1 | Mocking Strike | 1 | 16 | 30s | Physical | 10 | 2 min | melee | yes | — | [Battle] 16 damage; forces target to attack you for 6 s |
| SPL-FIG-15-r2 | Mocking Strike | 2 | 26 | 1g 20s | Physical | 10 | 2 min | melee | yes | — | [Battle] 40 damage; forces target to attack you for 6 s |
| SPL-FIG-16 | Disarm | 1 | 18 | 50s | Physical | 20 | 60 s | melee | yes | — | [Guard] Target cannot use its weapon for 10 s (mobs: −40% damage) |
| SPL-FIG-17-r1 | Cleave | 1 | 20 | 60s | Physical | 20 | next swing | melee | no | — | Weapon damage +5 to target and one adjacent enemy |
| SPL-FIG-17-r2 | Cleave | 2 | 30 | 1g 60s | Physical | 20 | next swing | melee | no | — | Weapon damage +18 to target and one adjacent enemy |
| SPL-FIG-18 | Dual Wield | 1 | 20 | 60s | Physical | passive | — | melee | no | — | May equip one-handed weapons in the off hand |
| SPL-FIG-19 | Intimidating Shout | 1 | 22 | 80s | Physical | 25 | 3 min | 10 yd | yes | — | Target cowers 8 s; up to 5 other enemies within 10 yd flee 8 s |
| SPL-FIG-20 | Pummel | 1 | 22 | 80s | Physical | 10 | 10 s | melee | yes | — | [Reckless] 20 damage; interrupts, locks the school 4 s |
| SPL-FIG-21-r1 | Execute | 1 | 24 | 1g | Physical | 15 + all remaining rage | — | melee | yes | — | [Battle, Reckless] Target below 20% health only: 125 damage +3 per extra rage |
| SPL-FIG-21-r2 | Execute | 2 | 32 (above cap) | reserved | Physical | 15 + all remaining rage | — | melee | yes | — | [Battle, Reckless] Target below 20% health only: 200 damage +6 per extra rage |
| SPL-FIG-22 | Challenging Shout | 1 | 26 | 1g 20s | Physical | 5 | 10 min | 10 yd | yes | — | All enemies within 10 yd attack you for 6 s |
| SPL-FIG-23 | Whirlwind | 1 | 28 | 1g 40s | Physical | 25 | 10 s | 8 yd | yes | — | [Reckless] Weapon damage to up to 4 enemies within 8 yd |
| SPL-FIG-24 | Shield Wall | 1 | 28 | 1g 40s | Physical | 0 | 30 min | melee | yes | — | [Guard (shield)] −75% all damage taken for 10 s |
| SPL-FIG-25 | Slam | 1 | 30 | 1g 60s | Physical | 15 | 1.5 s cast | melee | yes | — | Weapon damage +32; resets swing timer |
| SPL-FIG-26 | Recklessness | 1 | 30 | 1g 60s | Physical | 0 | 30 min | self | yes | — | [Reckless] 15 s: +100% crit chance, immune to fear, +20% damage taken |
| SPL-FIG-27 | Unbroken | 1 | 30 | 1g 60s | Physical | 0 | 30 s | self | yes | — | [Reckless] 10 s: immune to fear and incapacitate; taking damage generates extra rage |

## Cleric

| ID | Ability | Rank | Level | Training | School | Cost | Cast / cooldown | Range | GCD | Coefficient | Effect |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SPL-CLE-01-r1 | Oath of Radiance | 1 | 1 | free | Holy | 20 | instant | self | yes | 3% per hit | 30 s: each swing deals +3 Holy damage (scaled by weapon speed). **Verdict:** 12 Holy damage |
| SPL-CLE-01-r2 | Oath of Radiance | 2 | 10 | 8s | Holy | 45 | instant | self | yes | 6% per hit | 30 s: each swing deals +10 Holy damage (scaled by weapon speed). **Verdict:** 33 Holy damage |
| SPL-CLE-01-r3 | Oath of Radiance | 3 | 18 | 50s | Holy | 68 | instant | self | yes | 9% per hit | 30 s: each swing deals +16 Holy damage (scaled by weapon speed). **Verdict:** 51 Holy damage |
| SPL-CLE-01-r4 | Oath of Radiance | 4 | 26 | 1g 20s | Holy | 90 | instant | self | yes | 10% per hit | 30 s: each swing deals +22 Holy damage (scaled by weapon speed). **Verdict:** 70 Holy damage |
| SPL-CLE-02-r1 | Mending Light | 1 | 1 | free | Holy | 35 | 2.5 s | 40 yd | yes | 21% | Heal 42 |
| SPL-CLE-02-r2 | Mending Light | 2 | 6 | 2s | Holy | 76 | 2.5 s | 40 yd | yes | 34% | Heal 99 |
| SPL-CLE-02-r3 | Mending Light | 3 | 14 | 20s | Holy | 143 | 2.5 s | 40 yd | yes | 55% | Heal 189 |
| SPL-CLE-02-r4 | Mending Light | 4 | 22 | 80s | Holy | 209 | 2.5 s | 40 yd | yes | 71% | Heal 280 |
| SPL-CLE-02-r5 | Mending Light | 5 | 30 | 1g 60s | Holy | 275 | 2.5 s | 40 yd | yes | 71% | Heal 370 |
| SPL-CLE-03-r1 | Litany of Resolve | 1 | 1 | free | Holy | — | aura | self | no | — | Party armor +55 |
| SPL-CLE-03-r2 | Litany of Resolve | 2 | 10 | 8s | Holy | — | aura | self | no | — | Party armor +140 |
| SPL-CLE-03-r3 | Litany of Resolve | 3 | 20 | 60s | Holy | — | aura | self | no | — | Party armor +235 |
| SPL-CLE-03-r4 | Litany of Resolve | 4 | 30 | 1g 60s | Holy | — | aura | self | no | — | Party armor +330 |
| SPL-CLE-04 | Verdict | 1 | 4 | 1s | Holy | 5% base mana | instant / 10 s | 30 yd | yes | — | Consumes Oath for its Verdict effect |
| SPL-CLE-05-r1 | Benediction of Might | 1 | 4 | 1s | Holy | 20 | instant | 30 yd | yes | — | +20 attack power, 5 min |
| SPL-CLE-05-r2 | Benediction of Might | 2 | 12 | 12s | Holy | 38 | instant | 30 yd | yes | — | +49 attack power, 5 min |
| SPL-CLE-05-r3 | Benediction of Might | 3 | 22 | 80s | Holy | 60 | instant | 30 yd | yes | — | +85 attack power, 5 min |
| SPL-CLE-06-r1 | Dawnstrike | 1 | 6 | 2s | Physical + Holy | 4% base mana | instant / 6 s | melee | yes | 20% | Weapon damage +8 as Holy-infused physical; refreshes all active Verdict debuffs on the target |
| SPL-CLE-06-r2 | Dawnstrike | 2 | 14 | 20s | Physical + Holy | 4% base mana | instant / 6 s | melee | yes | 33% | Weapon damage +20 as Holy-infused physical; refreshes all active Verdict debuffs on the target |
| SPL-CLE-06-r3 | Dawnstrike | 3 | 22 | 80s | Physical + Holy | 4% base mana | instant / 6 s | melee | yes | 43% | Weapon damage +33 as Holy-infused physical; refreshes all active Verdict debuffs on the target |
| SPL-CLE-06-r4 | Dawnstrike | 4 | 30 | 1g 60s | Physical + Holy | 4% base mana | instant / 6 s | melee | yes | 43% | Weapon damage +45 as Holy-infused physical; refreshes all active Verdict debuffs on the target |
| SPL-CLE-07-r1 | Divine Ward | 1 | 6 | 2s | Holy | 15 | instant / 5 min | self | yes | 20% | Immune to all damage for 6 s; you cannot attack. Causes *Forbearance* (no Ward/Protection for 1 min) |
| SPL-CLE-07-r2 | Divine Ward | 2 | 18 | 50s | Holy | 15 | instant / 5 min | self | yes | 40% | Immune to all damage for 6 s; you cannot attack. Causes *Forbearance* (no Ward/Protection for 1 min) |
| SPL-CLE-08-r1 | Oath of the Zealot | 1 | 8 | 5s | Holy | 25 | instant | self | yes | 6% per hit | 30 s: +30 attack power but each swing deals 40% less (builds threat/speed feel). **Verdict:** target takes +20 Holy damage from all Holy hits for 10 s |
| SPL-CLE-08-r2 | Oath of the Zealot | 2 | 16 | 30s | Holy | 52 | instant | self | yes | 9% per hit | 30 s: +78 attack power but each swing deals 40% less (builds threat/speed feel). **Verdict:** target takes +50 Holy damage from all Holy hits for 10 s |
| SPL-CLE-08-r3 | Oath of the Zealot | 3 | 24 | 1g | Holy | 80 | instant | self | yes | 10% per hit | 30 s: +125 attack power but each swing deals 40% less (builds threat/speed feel). **Verdict:** target takes +80 Holy damage from all Holy hits for 10 s |
| SPL-CLE-09-r1 | Hammer of Rebuke | 1 | 8 | 5s | Holy | 30 | instant / 60 s | 10 yd | yes | — | 10 yd: stun 3 s |
| SPL-CLE-09-r2 | Hammer of Rebuke | 2 | 24 | 1g | Holy | 30 | instant / 60 s | 10 yd | yes | — | 10 yd: stun 4 s |
| SPL-CLE-10 | Purify | 1 | 8 | 5s | Holy | 6% base mana | instant | 40 yd | yes | — | Remove 1 disease and 1 poison from a friendly target |
| SPL-CLE-11 | Dawn's Mercy | 1 | 10 | 8s | Holy | all mana | instant / 60 min | 40 yd | yes | 27% | Heal a friendly target for your maximum health |
| SPL-CLE-12-r1 | Benediction of Protection | 1 | 10 | 8s | Holy | 6% base mana | instant / 5 min | 40 yd | yes | 27% | Ally immune to physical damage for 6 s, cannot attack. Forbearance |
| SPL-CLE-12-r2 | Benediction of Protection | 2 | 24 | 1g | Holy | 6% base mana | instant / 5 min | 40 yd | yes | 43% | Ally immune to physical damage for 8 s, cannot attack. Forbearance |
| SPL-CLE-13 | Raise the Fallen | 1 | 12 | quest | Holy | 60% base mana | 10 s | 40 yd | yes | 70% | Out of combat: resurrect a dead player at 20% health/mana (class quest) |
| SPL-CLE-14-r1 | Benediction of Wisdom | 1 | 14 | 20s | Holy | 30 | instant | 30 yd | yes | — | +10 mana per 5 s, 5 min |
| SPL-CLE-14-r2 | Benediction of Wisdom | 2 | 24 | 1g | Holy | 55 | instant | 30 yd | yes | — | +20 mana per 5 s, 5 min |
| SPL-CLE-15 | Challenge of Faith | 1 | 16 | 30s | Holy | 3% base mana | instant / 10 s | 30 yd | yes | — | Taunt: target attacks you for 3 s; match top threat. *(Deliberate improvement over the classic archetype, which had no taunt)* |
| SPL-CLE-16 | Righteous Bulwark | 1 | 16 | 30s | Holy | 20% base mana | instant | self | yes | 36% | 30 min self-buff: Holy damage threat +60% |
| SPL-CLE-17-r1 | Litany of Thorns | 1 | 16 | 30s | Holy | — | aura | self | no | 9% per hit | Attackers of party members take 5 Holy damage |
| SPL-CLE-17-r2 | Litany of Thorns | 2 | 26 | 1g 20s | Holy | — | aura | self | no | 10% per hit | Attackers of party members take 12 Holy damage |
| SPL-CLE-18 | Benediction of Freedom | 1 | 18 | 50s | Holy | 6% base mana | instant / 20 s | 40 yd | yes | — | Ally immune to movement-impairing effects for 10 s |
| SPL-CLE-19-r1 | Flash of Dawn | 1 | 20 | 60s | Holy | 35 | 1.5 s | 40 yd | yes | 43% | Heal 65 (fast, efficient, small) |
| SPL-CLE-19-r2 | Flash of Dawn | 2 | 26 | 1g 20s | Holy | 70 | 1.5 s | 40 yd | yes | 43% | Heal 140 (fast, efficient, small) |
| SPL-CLE-20-r1 | Hallowed Ground | 1 | 20 | quest | Holy | 135 | instant / 8 s | 8 yd | yes | 53% over time | Consecrate 8 yd around you: 64 Holy damage over 8 s to enemies inside (class quest) |
| SPL-CLE-20-r2 | Hallowed Ground | 2 | 30 | 1g 60s | Holy | 235 | instant / 8 s | 8 yd | yes | 53% over time | Consecrate 8 yd around you: 160 Holy damage over 8 s to enemies inside (class quest) |
| SPL-CLE-21-r1 | Exorcise | 1 | 20 | 60s | Holy | 85 | instant / 15 s | 30 yd | yes | 43% | 30 yd: 90–102 Holy damage to an Undead or Aberration |
| SPL-CLE-21-r2 | Exorcise | 2 | 28 | 1g 40s | Holy | 135 | instant / 15 s | 30 yd | yes | 43% | 30 yd: 160–180 Holy damage to an Undead or Aberration |
| SPL-CLE-22 | Sense Undead | 1 | 20 | 60s | Holy | — | toggle | self | no | — | Shows undead on the minimap |
| SPL-CLE-23 | Litany of Focus | 1 | 22 | 80s | Holy | — | aura | self | no | — | Party: 35% chance to ignore cast pushback |
| SPL-CLE-24 | Oath of Justice | 1 | 22 | 80s | Holy | 50 | instant | self | yes | — | 30 s: swings have a chance to stun 2 s (≈ 5 procs/min, not on bosses). **Verdict:** target cannot flee for 10 s |
| SPL-CLE-25 | Rebuke Undead | 1 | 24 | 1g | Holy | 9% base mana | 1.5 s / 30 s | 30 yd | yes | — | Undead target flees for 10 s |
| SPL-CLE-26 | Benediction of Salvation | 1 | 26 | 1g 20s | Holy | 6% base mana | instant | 40 yd | yes | — | Ally's threat generation −30%, 5 min |
| SPL-CLE-27 | Oath of Light | 1 | 30 | 1g 60s | Holy | 60 | instant | self | yes | 10% per hit | 30 s: swings have a chance to heal you for 39. **Verdict:** melee attackers of the target have a chance to be healed for 25, 10 s |

## Druid

| ID | Ability | Rank | Level | Training | School | Cost | Cast / cooldown | Range | GCD | Coefficient | Effect |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SPL-DRU-01-r1 | Thornlash | 1 | 1 | free | Nature | 20 | 1.5 s | 30 yd | yes | 12% | 13–16 Nature damage, 30 yd |
| SPL-DRU-01-r2 | Thornlash | 2 | 6 | 2s | Nature | 34 | 1.5 s | 30 yd | yes | 20% | 33–39 Nature damage, 30 yd |
| SPL-DRU-01-r3 | Thornlash | 3 | 14 | 20s | Nature | 56 | 1.5 s | 30 yd | yes | 33% | 65–76 Nature damage, 30 yd |
| SPL-DRU-01-r4 | Thornlash | 4 | 22 | 80s | Nature | 78 | 2.0 s | 30 yd | yes | 57% | 98–113 Nature damage, 30 yd |
| SPL-DRU-01-r5 | Thornlash | 5 | 30 | 1g 60s | Nature | 100 | 2.0 s | 30 yd | yes | 57% | 130–150 Nature damage, 30 yd |
| SPL-DRU-02-r1 | Mend | 1 | 1 | free | Nature | 25 | 1.5 s | 40 yd | yes | 12% | Heal 40 |
| SPL-DRU-02-r2 | Mend | 2 | 8 | 5s | Nature | 92 | 2.0 s | 40 yd | yes | 31% | Heal 174 |
| SPL-DRU-02-r3 | Mend | 3 | 14 | 20s | Nature | 150 | 2.5 s | 40 yd | yes | 55% | Heal 290 |
| SPL-DRU-02-r4 | Mend | 4 | 20 | 60s | Nature | 207 | 2.5 s | 40 yd | yes | 71% | Heal 405 |
| SPL-DRU-02-r5 | Mend | 5 | 26 | 1g 20s | Nature | 265 | 3.0 s | 40 yd | yes | 86% | Heal 520 |
| SPL-DRU-03-r1 | Gift of the Grove | 1 | 1 | free | Nature | 20 | instant | 30 yd | yes | — | 30 min: +25 armor; from rank 2 also +2 all attributes and +5 all resistances |
| SPL-DRU-03-r2 | Gift of the Grove | 2 | 10 | 8s | Nature | 45 | instant | 30 yd | yes | — | 30 min: +64 armor; from rank 2 also +3 all attributes and +7 all resistances |
| SPL-DRU-03-r3 | Gift of the Grove | 3 | 20 | 60s | Nature | 72 | instant | 30 yd | yes | — | 30 min: +107 armor; from rank 2 also +5 all attributes and +8 all resistances |
| SPL-DRU-03-r4 | Gift of the Grove | 4 | 30 | 1g 60s | Nature | 100 | instant | 30 yd | yes | — | 30 min: +150 armor; from rank 2 also +6 all attributes and +10 all resistances |
| SPL-DRU-04-r1 | Starbrand | 1 | 4 | 1s | Arcane | 25 | instant | 30 yd | yes | 9% direct + 12% over time | 9–12 Arcane damage plus 12 over 9 s |
| SPL-DRU-04-r2 | Starbrand | 2 | 10 | 8s | Arcane | 56 | instant | 30 yd | yes | 13% direct + 21% over time | 28–34 Arcane damage plus 46 over 10 s |
| SPL-DRU-04-r3 | Starbrand | 3 | 16 | 30s | Arcane | 88 | instant | 30 yd | yes | 18% direct + 28% over time | 47–56 Arcane damage plus 81 over 10 s |
| SPL-DRU-04-r4 | Starbrand | 4 | 22 | 80s | Arcane | 119 | instant | 30 yd | yes | 21% direct + 37% over time | 66–78 Arcane damage plus 116 over 11 s |
| SPL-DRU-04-r5 | Starbrand | 5 | 28 | 1g 40s | Arcane | 150 | instant | 30 yd | yes | 21% direct + 40% over time | 85–100 Arcane damage plus 150 over 12 s |
| SPL-DRU-05-r1 | Renewal | 1 | 4 | 1s | Nature | 25 | instant | 40 yd | yes | 32% over time | Heal 32 over 12 s (4 ticks) |
| SPL-DRU-05-r2 | Renewal | 2 | 10 | 8s | Nature | 59 | instant | 40 yd | yes | 50% over time | Heal 99 over 12 s (4 ticks) |
| SPL-DRU-05-r3 | Renewal | 3 | 16 | 30s | Nature | 92 | instant | 40 yd | yes | 68% over time | Heal 166 over 12 s (4 ticks) |
| SPL-DRU-05-r4 | Renewal | 4 | 22 | 80s | Nature | 126 | instant | 40 yd | yes | 80% over time | Heal 233 over 12 s (4 ticks) |
| SPL-DRU-05-r5 | Renewal | 5 | 28 | 1g 40s | Nature | 160 | instant | 40 yd | yes | 80% over time | Heal 300 over 12 s (4 ticks) |
| SPL-DRU-06-r1 | Briarskin | 1 | 6 | 2s | Nature | 35 | instant | 40 yd | yes | 5% per hit | 10 min on a friendly target: melee attackers take 3 Nature damage |
| SPL-DRU-06-r2 | Briarskin | 2 | 14 | 20s | Nature | 66 | instant | 40 yd | yes | 8% per hit | 10 min on a friendly target: melee attackers take 7 Nature damage |
| SPL-DRU-06-r3 | Briarskin | 3 | 24 | 1g | Nature | 105 | instant | 40 yd | yes | 10% per hit | 10 min on a friendly target: melee attackers take 12 Nature damage |
| SPL-DRU-07-r1 | Rootgrasp | 1 | 8 | 5s | Nature | 50 | 1.5 s | 30 yd | yes | 55% over time | Root 12 s; 20 Nature damage over the duration; damage may break it |
| SPL-DRU-07-r2 | Rootgrasp | 2 | 18 | 50s | Nature | 65 | 1.5 s | 30 yd | yes | 93% over time | Root 16 s; 50 Nature damage over the duration; damage may break it |
| SPL-DRU-07-r3 | Rootgrasp | 3 | 28 | 1g 40s | Nature | 80 | 1.5 s | 30 yd | yes | 100% over time | Root 21 s; 80 Nature damage over the duration; damage may break it |
| SPL-DRU-08-r1 | Overgrowth | 1 | 10 | quest | Nature | 120 | 2.0 s | 40 yd | yes | 18% direct + 31% over time | Heal 85 instantly plus 100 over 21 s (class quest) |
| SPL-DRU-08-r2 | Overgrowth | 2 | 18 | 50s | Nature | 212 | 2.0 s | 40 yd | yes | 26% direct + 46% over time | Heal 183 instantly plus 198 over 21 s (class quest) |
| SPL-DRU-08-r3 | Overgrowth | 3 | 24 | 1g | Nature | 281 | 2.0 s | 40 yd | yes | 29% direct + 50% over time | Heal 256 instantly plus 272 over 21 s (class quest) |
| SPL-DRU-08-r4 | Overgrowth | 4 | 30 | 1g 60s | Nature | 350 | 2.0 s | 40 yd | yes | 29% direct + 50% over time | Heal 330 instantly plus 345 over 21 s (class quest) |
| SPL-DRU-09-r1 | Cleanse Toxin | 1 | 10 | 8s | Nature | 8% base mana | instant | 30 yd | yes | — | Remove 1 poison; at rank 2 (L26) also cleanses again each 2 s for 8 s |
| SPL-DRU-09-r2 | Cleanse Toxin | 2 | 26 | 1g 20s | Nature | 8% base mana | instant | 30 yd | yes | — | Remove 1 poison; at rank 2 (L26) also cleanses again each 2 s for 8 s |
| SPL-DRU-10-r1 | Glimmer Mark | 1 | 12 | 12s | Arcane | 55 | instant | 30 yd | yes | — | 40 s: target armor −175 and cannot stealth or turn invisible |
| SPL-DRU-10-r2 | Glimmer Mark | 2 | 18 | 50s | Arcane | 65 | instant | 30 yd | yes | — | 40 s: target armor −248 and cannot stealth or turn invisible |
| SPL-DRU-10-r3 | Glimmer Mark | 3 | 30 | 1g 60s | Arcane | 85 | instant | 30 yd | yes | — | 40 s: target armor −395 and cannot stealth or turn invisible |
| SPL-DRU-11-r1 | Stinging Swarm | 1 | 14 | 20s | Nature | 45 | instant | 30 yd | yes | 62% over time | 66 Nature damage over 12 s; target's hit chance −2% |
| SPL-DRU-11-r2 | Stinging Swarm | 2 | 20 | 60s | Nature | 66 | instant | 30 yd | yes | 80% over time | 124 Nature damage over 12 s; target's hit chance −2% |
| SPL-DRU-11-r3 | Stinging Swarm | 3 | 30 | 1g 60s | Nature | 100 | instant | 30 yd | yes | 80% over time | 220 Nature damage over 12 s; target's hit chance −2% |
| SPL-DRU-12-r1 | Lull Beast | 1 | 18 | 50s | Nature | 90 | 1.5 s | 30 yd | yes | 40% | Sleep a Beast or Dragonkin for 20 s; damage wakes it; one target at a time |
| SPL-DRU-12-r2 | Lull Beast | 2 | 28 | 1g 40s | Nature | 90 | 1.5 s | 30 yd | yes | 43% | Sleep a Beast or Dragonkin for 30 s; damage wakes it; one target at a time |
| SPL-DRU-13-r1 | Astral Lance | 1 | 20 | 60s | Arcane | 95 | 3.5 s | 30 yd | yes | 100% | 95–115 Arcane damage, 30 yd |
| SPL-DRU-13-r2 | Astral Lance | 2 | 26 | 1g 20s | Arcane | 180 | 3.5 s | 30 yd | yes | 100% | 200–240 Arcane damage, 30 yd |
| SPL-DRU-14-r1 | Reawaken | 1 | 20 | quest | Nature | 30% base mana + Seed of Renewal | 2.0 s / 30 min | 40 yd | yes | 57% | Resurrect a dead player **in combat** with 400 health and 700 mana (class quest) |
| SPL-DRU-14-r2 | Reawaken | 2 | 30 | 1g 60s | Nature | 30% base mana + Seed of Renewal | 2.0 s / 30 min | 40 yd | yes | 57% | Resurrect a dead player **in combat** with 400 health and 700 mana (class quest) |
| SPL-DRU-15 | Lift Curse | 1 | 22 | 80s | Arcane | 8% base mana | instant | 40 yd | yes | — | Remove 1 curse from a friendly target |
| SPL-DRU-16 | Barkward | 1 | 24 | 1g | Nature | 60 | instant / 2 min | self | yes | 43% | 15 s: −20% physical damage taken, immune to cast pushback, but your cast times are 1 s longer |
| SPL-DRU-17 | Squall | 1 | 26 | 1g 20s | Nature | 320 | 10 s channel / 60 s | 30 yd | yes | 13% per tick | Storm at a target location (30 yd, 10 yd radius): 45 Nature damage per second to enemies inside and −20% attack speed |
| SPL-DRU-18 | Wellspring | 1 | 28 | 1g 40s | Nature | 5% base mana | instant / 6 min | 40 yd | yes | — | Friendly target: mana regeneration +400% and regenerates while casting, 20 s |
| SPL-DRU-19 | Stillwater | 1 | 30 | 1g 60s | Nature | 375 | 10 s channel / 5 min | 30 yd | yes | 13% per tick | Heals all party members within 30 yd for 98 every 2 s |

**Totals:** 73 abilities · 152 rank rows.
