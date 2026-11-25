# Economy & Social Systems

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Items & Loot](items-and-loot.md) · Next: [NPC AI & World Simulation](npc-ai-and-world.md)

## Part A — Economy

### 1. Currency
100 copper = 1 silver; 100 silver = 1 gold. No premium currency. PvP uses **Marks of Valor** (see [PvP](pvp.md)).

### 2. Income targets (cumulative, average player)

| Level | Wallet if nothing is spent | Main sinks so far |
|---|---|---|
| 10 | 1g 50s–2g | Skills 20s, bags, first profession |
| 20 | 8–10g | Skills 2g, repairs, professions |
| 30 | 45–55g | Skills 14g total, riding 30g + mount 5g (49g in all, so a character who trains everything reaches 30 just short of a mount: the intended classic tension) |

These figures were recomputed on 2026-11-12 from the written quest rewards: quest coin alone is about 1g 30s by level 10, 5g 70s by 20 and 33g by 30 on a typical route (one zone per tier to 20, then two level 20–30 zones), with creature coin and vendor sales adding roughly 40% on top. The earlier figures (60–90s, 7–9g, 28–35g) could not have paid for training and riding.
| *60 (design target)* | *≈ 25–35g earned per hour of active play* | See §4 |

Quest coin rewards follow the per-level table in the [Quest Text index](../06-quests/text/00-quest-text-index.md) (L10 5s, L20 20s, L30 55s for a standard quest; half for deliveries, 1.5× for elite and dungeon quests). The exact coin for every quest is written in its quest text entry.

### 3. Sinks

| Sink | Cost | Kind |
|---|---|---|
| Ability training | ≈ 14g total by 30 | One-off per rank |
| Repairs | ≈ `ilvl × quality` copper per durability point | **Continuous** |
| Eyrie fares | 50c–8s per flight | **Continuous** |
| Riding (level 30) + mount | 30g + 5g | One-off |
| Epic riding (level 60) + epic mount | 500g + 100g | One-off |
| **Epic mount feed** | See §4 | **Continuous, scales with time played** |
| Profession training, vendor recipes | 10c–2g each | One-off |
| Crafting vendor components (vials, thread, flux, coal, spices, dyes) | Copper to silver each | **Continuous** |
| Reagents, ammo | Per use | **Continuous** |
| Bank bag slots | 10s, 1g, 10g, 25g, 50g, 100g | One-off |
| Auction house cut and deposits | 5% of sale (neutral house 15%); deposit lost if unsold | **Continuous** |
| **Mail postage** | **1s** per mail, plus 1s per attached item | **Continuous** |
| **Talent respec** | **1g** first time, +1g per respec, **maximum 5g**. The price **decays by 1g per week** without a respec, down to a **minimum of 1g** | **Continuous** |
| Guild charter, tabard | 10s; 1g design + 10s each | One-off |
| **Guild bank tabs** | See §14 | One-off, large |
| Barber | 50s–2g | Occasional |

### 4. The level-60 gold sink plan

**Goal:** at the level cap, gold must keep leaving the economy at a rate that tracks **how much a character plays**, so wealth does not simply pile up and inflate prices. One-off purchases cannot do this; the sinks below can, because each is paid again for every hour or every activity.

| Continuous sink | How it scales with play | Estimated cost per hour played at 60 |
|---|---|---|
| **Epic mount feed** | Consumed by time logged in | ≈ 60s |
| Repairs | By deaths and combat | 1–3g (raiding/dungeons), 0.5–1g (solo) |
| Auction house cut | By trading volume | 5% of everything sold |
| Consumable components and reagents | By raiding and crafting | 0.5–2g |
| Eyrie fares | By travel | 10–40s |
| Mail | By trading volume | 1s per item |
| Respec | By role-swapping | 1–5g per swap |
| **Total target** | | **≈ 20–25% of hourly income removed** |

#### Epic mount feed

| Rule | Detail |
|---|---|
| What needs feeding | Epic mounts only (level 60, +100% speed). Level-30 mounts never need feed |
| **Fed** state | A status on the *character*, shown on the mount's tooltip and as a small icon by the minimap, with hours remaining |
| Fed clock | Counts down **only while the character is logged in** (time played), whether or not they are riding. It does not tick while logged out, so it is a cost per hour of play, not a subscription |
| Feed item | *Sack of Charger's Oats* (horses) / *Ram-Mash* (rams): **6g** from stable feed merchants. Bind on Pickup, vendor-only, cannot be crafted, traded or auctioned — so the gold is destroyed, not moved. One sack adds **10 hours** of Fed time; the clock holds up to 30 hours |
| **Unfed** | When the clock reaches zero the epic mount is still usable but moves at the **level-30 speed (+60%)** instead of +100%. Feeding restores full speed immediately. Nothing is ever lost or locked |
| Warnings | Chat and icon warnings at 60 and 10 minutes remaining; the stable master's gossip shows the clock |
| Tuning lever | The price per sack is a single data value, adjusted as the real income rate at 60 becomes known |
| Launch status | Built with the mount system; **dormant while the cap is 30** because epic riding does not exist yet |

Design note: feed is deliberately a soft penalty (slower, not dismounted) so a returning player is never stranded, while a player who is active for many hours pays steadily.

### 5. Vendors
- Vendors buy any sellable item at its vendor value and sell it back (buyback tab, last 12 items).
- Types: general goods, trade supplies, food & drink, armorer, weaponsmith, reagents, recipes, stable and feed merchant, reputation quartermaster, PvP quartermaster.
- Limited-stock items restock on a timer (rare recipes, a few white weapons).
- Reputation discount: Friendly 5%, Honored 10%, Revered 15%, Exalted 20% (never applies to mount feed).

### 6. Auction house
- Locations: Solhaven, Hammerdeep (linked, Concord), Kite's Rest (neutral — becomes the cross-allegiance house later).
- Listing: stack, starting bid, optional buyout, duration 2/8/24 h. Deposit = 5% / 15% / 25% of vendor value × stack, refunded on sale. **House cut 5%** (neutral 15%) — a permanent, proportional gold sink.
- Browse by category, level range, quality, name; sort by any column. Won items and proceeds arrive by mail (1 h delay on proceeds).

### 7. Mail
- Mailboxes in every town. Send text, coin, up to 12 item attachments, or cash-on-delivery.
- **Postage 1s per mail and 1s per attached item.** Player-to-player items arrive after 1 h; auction and system mail instantly and free.
- Mail expires after 30 days. Soulbound items cannot be mailed.

### 8. Trade
Player-to-player trade window, 6 item slots + coin + 1 "will not be traded" slot (for enchanting). Both must accept; any change resets acceptance.

### 9. Banking
Personal bank in capitals and Kite's Rest (see [Items](items-and-loot.md#6-bags-bank-inventory)). Guild bank: §14.

## Part B — Social

### 10. Chat

| Channel | Scope |
|---|---|
| /say, /yell, /emote | 25 yd / 300 yd / 25 yd |
| /party, /raid, /raid warning | Group |
| /guild, /officer | Guild |
| /whisper, /reply | Realm-wide, same allegiance |
| General, Trade (capitals only), LocalDefense, LookingForGroup | Zone-wide auto-joined channels |
| Custom channels | Player-created, password optional |

Features: chat tabs and filters, item links, ignore list (50), profanity filter toggle, spam throttle, /who search, /roll, 44 text emotes, those with a matching animation playing it (/wave, /dance, /bow, …; the list is in [UI Specification §5](../08-tech/ui-specification.md#5-slash-commands) and the text in [Game Text §6](../12-data/game-text.md#6-emotes)), AFK/DND flags, combat log tab.

### 11. Friends and ignore
Friends list (100) with online status, zone, level, class; notes. Ignore blocks whispers, invites, trades, duels and mail.

### 12. Groups and raids
- **Party:** up to 5. Leader can invite, kick, set loot rule, mark targets (8 raid icons), ready check, convert to raid.
- **Raid group:** up to **20** players in four sub-groups of 5. Raid instances come in two sizes only — **10-player and 20-player**. There are no 40-player raids. Assistants, main-tank/main-assist tags.
- Shared quest credit for kills and (where flagged) item drops; quest sharing from the log.
- **Group XP:** no split and no bonus — every member gets full solo XP per kill, and nobody gets any if the group's level spread exceeds 5. See [Progression](progression.md#group-xp-rules).
- **Meeting stones** at each dungeon entrance: two players can summon a third group member.
- **Looking for group:** a LFG channel plus a simple **group-finder board** (list yourself or your group for a dungeon/quest with a role flag; no automatic matchmaking or teleport — keeps the classic social feel).

### 13. Guilds

Guilds are a launch feature.

| Feature | Detail |
|---|---|
| Founding | Buy a charter (10s) from a guild master NPC in either capital; collect **4** signatures from other players (reduced from the genre's 9 for a small launch population); return it |
| Size | Up to 500 members |
| Ranks | 5 by default, up to 10; renameable; ordered. Rank 1 is the Guild Master |
| Permissions per rank | Guild chat (listen/speak), officer chat, invite, remove, promote, demote, set message of the day, edit public note, view/edit officer note, edit guild info, **guild bank permissions per tab** (§14), withdraw gold limit, repair from guild funds |
| Roster | Name, level, class, zone, rank, note, officer note, last online; sort and filter; show offline toggle |
| Message of the day and guild info | Shown on login / in the guild panel |
| Tabard | Designer NPC: emblem, emblem colour, border, background (1g to set the design; each member buys the tabard for 10s) |
| Leadership | Guild Master can promote, transfer leadership, disband (the bank must be empty). If the Guild Master is inactive 60 days, the highest-ranked active member can claim leadership |
| Guild chat channels | /guild and /officer |
| Guild events log | Joins, leaves, promotions, demotions, kicks (last 100) |
| Later | Guild calendar, guild reputation/perks (not classic; not planned) |

### 14. Guild bank

A shared vault for a guild's items and gold. In scope for launch.

| Topic | Design |
|---|---|
| Access points | **Guild Vault** NPC/object next to the bank in Solhaven (Coinmarket), Hammerdeep (Goldring Commons) and Kite's Rest |
| Unlocking | The Guild Master buys tabs at a Guild Vault |
| Tabs | Up to **6 tabs of 98 slots**. Prices: **10g · 50g · 150g · 400g · 1,000g · 2,500g** — the first is reachable at the level-30 cap; the last three are level-60 guild goals and a large gold sink |
| Tab settings | Name, icon, and a free-text info note per tab |
| Item rules | Any non-soulbound, non-quest item. Stacks behave as in personal bags. Bags cannot be placed in the vault as containers |
| Gold | A guild money pool. Anyone may deposit. Withdrawals limited per rank per day |
| Permissions (per rank, per tab) | *View tab* · *Deposit items* · *Withdraw items* with a **daily limit in stacks** (0 to unlimited) |
| Permissions (per rank, gold) | *Daily gold withdrawal limit* · *May use guild funds for repairs* (with its own daily limit) |
| Guild Master | Unlimited access; sets all limits |
| Logs | Per-tab item log (who deposited/withdrew/moved what, when; last 250 entries) and a money log (deposits, withdrawals, repairs, tab purchases). Readable by ranks with the *View logs* permission |
| Safety | Every vault transaction is an atomic database transaction with an audit record; two players cannot take the same stack; limits reset at the daily server reset; a guild cannot be disbanded while the vault holds items or gold |
| Anti-abuse | New members have a configurable probation (default 7 days) before withdrawal limits apply; GM tools can restore from the audit log |
| Data | Guild → tabs → slots → item instances; guild money; per-rank permission rows; log tables. See [Data Model](../08-tech/data-model.md) |

### 15. Other social features
- **Duels:** see [PvP](pvp.md).
- **Inspect** another player's gear and talents.
- **/played**, **/time**, in-game calendar (holidays post-launch).
- **Barber** in capitals: change hair and facial features for 50s–2g.
- **Reporting:** right-click report (spam, name, cheating) feeding a GM queue; GM tickets.

## Part C — Reputation
Defined in [Factions & Races](../01-world/factions-and-races.md#4-reputation-factions-launch). Rules: +reputation from quests (≈ 25% of quest XP as rep, min 10), kills where flagged, and repeatable turn-ins (cloth donations: 60 linen / wool / silk → 350 rep each, once per cloth type per capital). "At war" toggle exists for future hostile factions.
