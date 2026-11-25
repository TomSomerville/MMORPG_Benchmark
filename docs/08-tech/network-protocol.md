# Network Protocol

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Database Schema](database-schema.md) · Next: [UI Specification](ui-specification.md) · Overview: [Architecture §5](architecture.md#5-networking)

Every message the client and server exchange: the connection sequence, the wire format, and the full message catalogue with fields. The message types live in `Game.Shared/Protocol`; this page is their specification.

## 1. Connections

| Connection | Transport | Port | Carries |
|---|---|---|---|
| Login | TCP with TLS 1.3, length-prefixed frames | 7778 | Account login, realm list, character list, create and delete |
| Game | LiteNetLib (reliable UDP), encrypted with the session key | 7777 | Everything after "Enter World" |

Game channels:

| Channel | Delivery | Used for |
|---|---|---|
| 0 | Reliable, ordered | State changes: spells, combat results, inventory, quests, chat, UI responses |
| 1 | Unreliable, sequenced (newest wins) | Movement, both directions |
| 2 | Reliable, ordered, low priority | Bulk data: auction listings, mail lists, guild roster, map data |

## 2. Wire format

| Rule | Detail |
|---|---|
| Frame | `[opcode: u16][payload]`. LiteNetLib supplies length and ordering on the game connection; the login connection prefixes `[length: u16]` |
| Byte order | Little-endian |
| Integers | `u8`, `u16`, `u32`, `i32`, `i64`; `varint` (unsigned LEB128) for counts and small values |
| Entity id | `u64` |
| Content id | `u32` handle. The handle table (id string → handle) is part of the compiled content pack, identical on both sides; its hash is checked at login |
| Strings | `varint` byte length + UTF-8. Maximum lengths are enforced per field |
| Positions | Three `f32` in yards, zone-local. Movement packets pack facing into a `u16` (0–65535 = 0–360°) |
| Time | Server time as `u32` milliseconds since the session began |
| Booleans and small enums | Packed into flag bytes |
| Optional fields | A leading flags byte says which are present |
| Version | `ProtocolVersion` (u16) and `ContentHash` (u64) are exchanged at login. A mismatch refuses the connection with a message telling the player to update |

Opcode ranges: `0x00xx` connection · `0x01xx` login and characters · `0x02xx` entities and movement · `0x03xx` combat and spells · `0x04xx` inventory, loot, vendors · `0x05xx` quests and gossip · `0x06xx` chat and social · `0x07xx` groups and instances · `0x08xx` economy (trade, mail, auctions) · `0x09xx` professions · `0x0Axx` guilds · `0x0Bxx` PvP · `0x0Cxx` world and travel · `0x0Fxx` GM and debug. `C→S` messages use even opcodes within a range and `S→C` odd, so a misdirected packet is caught by one bit test. The messages of inns, the hearthstone, sitting and experience status (`BindHearth`, `UseHearthstone`, `SitStand`, `BindSet`, `XpStatus`) are numbered in `0x05xx` with the quest and gossip messages, and are listed in §5.3.

## 3. Connection sequence

```
Client                                Login server (TLS)
  |-- LoginRequest(name, password, protocolVersion, contentHash) -->|
  |<-- LoginResult(ok | error, accountFlags) ----------------------|
  |-- RealmListRequest ------------------------------------------->|
  |<-- RealmList(realms[]: name, address, population, characters) -|
  |-- CharacterListRequest(realm) -------------------------------->|
  |<-- CharacterList(characters[]) --------------------------------|
  |   (optional) CharacterCreate / CharacterDelete / results
  |-- EnterWorldRequest(characterId) ------------------------------>|
  |<-- EnterWorldTicket(ticket, sessionKey, gameAddress) ----------|

Client                                Game server (UDP)
  |-- Connect(ticket)  [LiteNetLib connect payload] --------------->|
  |<-- ConnectAccepted(serverTime, tickMs) ------------------------|
  |<-- WorldEnter(self snapshot: see 4.2) -------------------------|
  |<-- InitialState batch: spells, talents, skills, action bars,
  |     inventory, quest log, reputations, explored areas, flight
  |     nodes, friends, guild, settings, cooldowns, auras, mail flag
  |<-- EntityCreate ... (everything in the interest area) ---------|
  |-- ClientReady ------------------------------------------------->|
  |<-- ChatMotd, GuildMotd ----------------------------------------|
```

Rules:

- The initial state batch begins with an `EntityCreate` for the player's own character (its health, resource and level), then `InventoryFull` with `CharacterStats`, `SpellsKnown`, `QuestLogFull`, `XpStatus` and `ExploredAreas`; each later system adds its own message to the batch when it is built.
- The ticket is single-use and expires 30 seconds after issue.
- One game connection per account. A second login disconnects the first with `Disconnect(reason: LoggedInElsewhere)`.
- `Ping` / `Pong` every 5 seconds give round-trip time and clock offset; the client shows latency from them. No packet for 30 seconds drops the connection.
- **Logout:** `LogoutRequest` starts a 20-second timer (instant in an inn or capital) and is answered with `LogoutResult` (result code, seconds on the timer; 0 means logged out now). Moving or taking damage cancels it, as does `LogoutCancel`. On a dropped connection the character stays in the world for 20 seconds, or until out of combat if longer, up to 2 minutes.

## 4. Entities and movement

### 4.1 Interest

The server sends a client only what is in its interest set: entities in its grid cell and the eight neighbours (cells are 55 yards), plus subscriptions (party and raid members anywhere in the zone, the current target, world bosses within 200 yards). `EntityCreate` is sent when an entity enters the set and `EntityDestroy` when it leaves, with a reason (`OutOfRange`, `Died`, `Despawned`).

### 4.2 Entity messages (S→C)

| Message | Fields |
|---|---|
| `WorldEnter` | zoneId, instanceId, position, facing, serverTime, gameClock (minutes of day), weather state |
| `EntityCreate` | entityId, kind (player, creature, npc, object, corpse, pet), contentId, position, facing, movement state, level, health, maxHealth, resourceType, resource, maxResource, flags (dead, inCombat, elite, tapped, lootable, pvp, sitting, stealthed, ghost, resting, away), reaction to the receiver, questGiverState, displayed auras[], cast in progress (optional); players add: name, race, class, sex, appearance, visible equipment[19] (item content id + enchant visual), guild name, title, groupId |
| `EntityDestroy` | entityId, reason |
| `EntityUpdate` | entityId, fieldMask, then only the changed fields: health, maxHealth, resource, maxResource, level, flags, target, equipment slot, displayed aura changes, speed, scale, questGiverState |
| `EntityMove` | entityId, serverTime, position, facing, movement flags (forward, back, strafeL, strafeR, turning, jumping, falling, swimming, walking), speed; creatures on paths send `EntityPath` instead: start time, speed, list of waypoints |
| `EntityTeleport` | entityId, position, facing (snap, no interpolation) |
| `EntityEmote` / `EntityAnim` | entityId, emote or one-shot animation id |

Health and resource are sent as exact values for the player's own character and party members, and as a 0–255 fraction for everything else. In use: exact values (`i32`) are sent for every entity; the fraction is a bandwidth measure applied with the bandwidth checks of T-M12-02. **Open:** whether players may see the exact health of creatures and of players outside their party, as now, or only the fraction, is the owner's choice.

The `resting` flag marks a character in a rest area and `away` one with no input for the idle time ([Rules Reference §3](../02-systems/rules-reference.md)); both are visible to others. A per-player world object that a character has already used is left out of that character's interest set: the character never receives its `EntityCreate`, and receives `EntityDestroy` when it uses it.

### 4.3 Player movement (C→S, channel 1)

`MoveInput`: sequence (u16), clientTime, position, facing, movement flags, fall start height (if falling). Sent on every change of flags and at 10 Hz while moving.

Server validation, per packet:

| Check | Rule | On failure |
|---|---|---|
| Speed | Distance since the last accepted packet ≤ the character's movement allowance + 0.5 yards. The allowance builds with time, by allowed speed × elapsed × 1.15, up to at most one second's worth, and each accepted move spends its distance from it; packets bunched together by the network are therefore not mistaken for speeding | `MoveCorrection` to the last valid position |
| Bounds | The position lies inside the zone | `MoveCorrection` |
| Floor | The position has a floor on the zone's walk grid ([Terrain and Cutouts §1.1](terrain-and-cutouts.md#11-the-walk-grid)): not a cliff, a wall, deep water or a hole with nothing under it. Unless falling or jumping, its height is within 2 yards of that floor | `MoveCorrection` |
| State | Not rooted, stunned, dead (unless ghost) or on a taxi: such a character may not move at all, not even inside the 0.5-yard slack | `MoveCorrection` |
| Jump and fall | Fall damage computed server-side, from the highest point the character reported while in the air to where it landed | Applied by the server |
| Teleport | Any jump over 12 yards in one packet | Correction, and a strike logged; 5 strikes in a minute disconnects |

`MoveCorrection` (S→C): sequence acknowledged, position, facing, flags. The client replays its unacknowledged inputs from that point.

Other players are shown 100 ms in the past, interpolated between the two most recent `EntityMove` packets.

## 5. Message catalogue

Field lists give the content of each message; "result" messages carry `ok` or an error code from §6.

### 5.1 Combat and spells (0x03xx)

| Direction | Message | Fields |
|---|---|---|
| C→S | `SetTarget` | entityId (0 clears) |
| C→S | `AttackStart` / `AttackStop` | targetId |
| C→S | `CastSpell` | spellId, targetId or ground position, clientTime, queue flag |
| C→S | `CancelCast` | — |
| C→S | `CancelAura` | auraId (own buffs only) |
| C→S | `SetStance` | stanceId |
| C→S | `UseItem` | bag, slot, targetId or position |
| S→C | `CastFailed` | spellId, reason code |
| S→C | `CastStart` | casterId, spellId, targetId, castTimeMs, serverTime (all in interest) |
| S→C | `CastDelayed` | casterId, addedMs (pushback) |
| S→C | `CastInterrupted` | casterId, spellId, reason, lockout school and ms |
| S→C | `CastGo` | casterId, spellId, targets[], missed[] with miss reason, projectile travel ms |
| S→C | `ChannelStart` / `ChannelUpdate` | casterId, spellId, remainingMs |
| S→C | `Cooldown` | spellId or group, durationMs, plus `GlobalCooldown` ms |
| S→C | `CombatEvent` | sourceId, targetId, spellId (0 = auto-attack), kind (damage, heal, miss, dodge, parry, block, resist, immune, absorb, energize, drain), amount, school, flags (crit, glancing, crushing, partial block, partial resist), overkill or overheal |
| S→C | `PeriodicTick` | as `CombatEvent`, for auras |
| S→C | `AuraApplied` / `AuraRefreshed` / `AuraRemoved` | targetId, auraId, casterId, stacks, durationMs, remainingMs |
| S→C | `ThreatUpdate` | creatureId, list of (entityId, percent of top) for the receiver's party; sent at most twice a second |
| S→C | `AttackSwing` | attackerId, targetId, hand (for swing timers and animation) |
| S→C | `CombatState` | inCombat (bool) |
| S→C | `Death` | entityId, killerId; for the player also: release timer, corpse position |
| C→S | `ReleaseSpirit` · `ReclaimCorpse` · `AcceptResurrect` (casterId, accept) · `SpiritHealerResurrect` | |
| S→C | `ResurrectOffer` | casterName, spellId, health and mana offered |
| S→C | `XpGain` | amount, restedBonus, source (kill, quest, explore), victimId |
| S→C | `LevelUp` | level, stat gains, health and resource gains, talent point (bool), new abilities available at trainers[] |

### 5.2 Inventory, loot, vendors (0x04xx)

| Direction | Message | Fields |
|---|---|---|
| S→C | `InventoryFull` (initial) | every item: instanceId, itemId, container, slot, stack, durability, suffix, enchant, bound, charges |
| S→C | `ItemAdded` / `ItemChanged` / `ItemRemoved` | instanceId and the changed fields |
| C→S | `MoveItem` | from (container, slot), to (container, slot), count (split) |
| C→S | `EquipItem` / `UnequipItem` · `DestroyItem` (instanceId, count) · `SortBags` | |
| S→C | `MoneyChanged` | total |
| S→C | `ItemError` | reason code, instanceId (0 if none): an inventory, vendor or trainer request was refused |
| S→C | `CharacterStats` | the character's own numbers for its character window: the five attributes with gear, armor, attack power, spell power, healing power, weapon damage min and max, weapon speed, crit, dodge, parry and block percent, block value, defense. Sent on entering the world and whenever what is worn, or whether it is broken, changes |
| S→C | `EquipmentChanged` | entityId, slot, itemId (0: nothing): what another player is seen to wear changed |
| C→S | `LootOpen` | entityId (corpse, chest, node) |
| S→C | `LootWindow` | sourceId, coin, items[]: lootSlot, itemId, count, questItem, suffix; with group loot (M7) also needsRoll. Quality is read from the item record |
| C→S | `LootTake` (lootSlot) · `LootTakeMoney` · `LootClose` | |
| S→C | `LootRemoved` | sourceId, lootSlot (255: the coin): something was taken from an open loot window |
| S→C | `LootClosed` | sourceId: the window closes because it is empty, out of reach or gone |
| S→C | `LootRollStart` | rollId, itemId, count, timeoutMs |
| C→S | `LootRollChoice` | rollId, choice (need, greed, pass) |
| S→C | `LootRollResult` | rollId, rolls[] (name, choice, value), winner |
| C→S | `SetLootMethod` (method, threshold, master looter) · `MasterLootGive` (lootSlot, playerId) | |
| C→S | `VendorOpen` (npcId) | |
| S→C | `VendorList` | npcId, repairs (bool), items[]: index, itemId, price of one lot, lot size, lots left (−1: no limit), can afford and can use flags; buyback[]: itemId, suffix, count, price. Sent when the window opens and after every change. Lines the character is not offered (a stock condition) are left out |
| C→S | `VendorBuy` (itemId, count of lots) · `VendorSell` (instanceId, count; 0: the whole stack) · `VendorBuyback` (index) · `RepairItem` (instanceId or 0 for all, useGuildBank) · `VendorClose` | |
| S→C | `VendorClosed` | npcId: the character walked away, or the vendor is gone |
| C→S | `TrainerOpen` (npcId) | A class trainer of another class answers `WrongClass` |
| S→C | `TrainerList` | npcId, nextIsFree (bool: the character's next rank costs nothing), entries[]: spellId or recipeId, cost, required level, required skill, state (available, unavailable, known). Sent when the window opens and after every purchase |
| C→S | `TrainerBuy` (spellId) · `TrainerClose` · `TalentLearn` (talentId) · `TalentReset` | |
| S→C | `TrainerClosed` | npcId: the character walked away |
| S→C | `SpellsKnown` | spellIds[]: every spell the character knows, on entering the world. The client builds its spellbook and action bar from it |
| S→C | `SpellLearned` | spellId |
| C→S | `BankOpen` · `BankBuySlot` | |

### 5.3 Quests and gossip (0x05xx)

| Direction | Message | Fields |
|---|---|---|
| C→S | `Interact` | entityId (the server decides: gossip, quest, vendor, loot, object use) |
| S→C | `GossipMenu` | sourceId (an NPC or a world object), services (flags: vendor, repair, trainer, innkeeper), quests[]: questId, state (available, available low level, in progress, complete). The greeting and every other text come from the client's string table by the source's id. An NPC with no quest for the character and one service opens that service at once and sends no menu |
| C→S | `GossipSelect` (npcId, index) | For gossip options that are neither a quest nor one of the four service flags (taxi, bank, battlemaster, scripted options), with `options[]` (index, icon, string id) added to `GossipMenu`. Not in use: no built NPC has such an option; a service is opened with its own message (`VendorOpen`, `TrainerOpen`, `BindHearth`) |
| S→C | `QuestOffer` | npcId, questId, level, XP, coin, reward lists, objectives (text comes from the client's string table). Not in use: see below |
| C→S | `QuestAccept` (sourceId, questId) · `QuestAbandon` (questId) | |
| S→C | `QuestLogFull` | active[]: questId, counts[] (one per objective, in order); done[]: questId. Sent once on entering the world: the log and every quest the character has done |
| S→C | `QuestAdded` | questId, counts[] |
| S→C | `QuestProgressed` | questId, objective index, count, required |
| S→C | `QuestObjectivesComplete` | questId: it can be handed in |
| S→C | `QuestRemoved` | questId: the quest left the log without being handed in (abandoned) |
| S→C | `QuestFailed` | questId, reason code: a request about a quest was refused |
| S→C | `QuestTurnInWindow` | npcId, questId, canComplete, rewards. Not in use: see below |
| C→S | `QuestComplete` | sourceId, questId, chosen reward index (0 where there is no choice) |
| S→C | `QuestCompleted` | questId, XP, coin, items[] (itemId, count), next quest offered by the same source; reputation gains[] are added with reputation (T-M6-03) |
| C→S | `QuestShare` (questId) · S→C `QuestShareOffer` | |
| S→C | `QuestGiverStatus` | sent inside `EntityUpdate`: none, available, available low level, in progress, complete |
| S→C | `ExploredArea` | subareaId, XP |
| S→C | `ExploredAreas` | subareaIds[] (on entering the world: every sub-area already found) |
| S→C | `XpStatus` | XP into the level, XP the level needs (0 at the cap), rested XP. Sent on entering the world and after every change |
| C→S | `BindHearth` (npcId) · `UseHearthstone` · `SitStand` (sit) | |
| S→C | `BindSet` | zoneId, position: the character's home is now this place |
| S→C | `ObjectState` | objectId, state, for world objects with more than two states (doors, levers). Not in use: a per-player object that has been used leaves that character's interest set (§4.2), which needs no message |
| S→C | `ScriptedScene` | sceneId, parameters (escort start, shard resonance, the VM-29 ending) |

**Quest pages.** The client draws the offer, progress and completion pages from its own content pack: the server sends ids and states (`GossipMenu`, `QuestLogFull`, `QuestProgressed`), never text or reward lists, and the rewards, objectives and XP on a page are computed from the same quest records the server uses. `QuestOffer` and `QuestTurnInWindow` are therefore not sent, and the content hash checked at login is what guarantees the two sides agree. **Open:** whether `QuestOffer` and `QuestTurnInWindow` are dropped from the protocol or built later (they would be needed for a quest whose offer the server must vary per character) is the owner's choice; `GossipSelect` and `ObjectState` stay in the catalogue and are built with the first content that needs them.

### 5.4 Chat and social (0x06xx)

| Direction | Message | Fields |
|---|---|---|
| C→S | `ChatSend` | channel (say, yell, emote, party, raid, raid warning, guild, officer, whisper, general, trade, local defense, looking for group, battleground), target name (whisper), text (max 255) |
| S→C | `ChatMessage` | channel, senderId, senderName, text, flags (GM, AFK, DND) |
| S→C | `ChatError` | reason (player not found, ignored, muted, throttled) |
| C→S | `ChannelJoin` / `ChannelLeave` · `TextEmote` (emoteId, targetId) | |
| C→S | `WhoRequest` | filters: name, guild, level range, class, zone |
| S→C | `WhoResult` | up to 49 rows: name, guild, level, class, race, zone; total count |
| C→S | `FriendAdd` / `FriendRemove` / `IgnoreAdd` / `IgnoreRemove` (name) · `FriendNote` | |
| S→C | `FriendList` · `FriendStatus` (name, online, level, class, zone) | |
| C→S | `SetAfk` / `SetDnd` (message) · `InspectRequest` (entityId) | |
| S→C | `InspectResult` | equipment[19], talents spent per tree, guild |
| C→S | `DuelRequest` (targetId) · `DuelRespond` (accept) · `DuelForfeit` | |
| S→C | `DuelOffer` · `DuelCountdown` · `DuelResult` | |
| C→S | `ReportPlayer` | targetId or name, reason (spam, abuse, name, cheating, botting), note (max 200), chatLineId (optional), alsoIgnore |
| S→C | `ReportResult` | accepted or throttled (5 reports per 10 minutes) |
| C→S | `TicketOpen` (category, text max 500) · `TicketClose` · `TicketStateRequest` | One open ticket per account |
| S→C | `TicketState` | state (none, open, answered, closed), reply text, replied at |
| S→C | `PenaltyNotice` | kind (warning, mute, suspension, ban), reason, ends at; sent at login and when applied |
| S→C | `ServerNotice` | kind (restart countdown, realm message), text, seconds |

The rules behind these are in [Accounts and Live Service](accounts-and-live-service.md).

Chat limits: 1 message per second sustained, burst of 5; yell and global channels 1 per 10 seconds for characters below level 5.

### 5.5 Groups and instances (0x07xx)

| Direction | Message | Fields |
|---|---|---|
| C→S | `GroupInvite` (name) · `GroupAccept` / `GroupDecline` · `GroupLeave` · `GroupKick` (name) · `GroupSetLeader` · `GroupConvertToRaid` · `RaidMoveMember` (name, subgroup) · `SetAssistant` · `ReadyCheck` / `ReadyCheckReply` · `SetRaidTarget` (entityId, icon) | |
| S→C | `GroupInviteOffer` | inviter name |
| S→C | `GroupRoster` | groupId, isRaid, leader, loot method, members[]: entityId, name, class, level, online, subgroup, role flags, zone |
| S→C | `GroupMemberState` | entityId, health, maxHealth, resource, auras (dispellable debuffs), position on the zone map, dead or ghost — sent at 2 Hz for members outside the interest set |
| S→C | `ReadyCheckState` · `RaidTargetUpdate` | |
| S→C | `InstanceEnterResult` | ok or reason (level, lockout, group required, attunement, entry cap, full) |
| S→C | `InstanceReset` · `InstanceLockInfo` (instance, save id, bosses killed, reset time) | |
| C→S | `InstanceResetRequest` · `MeetingStoneJoin` · `LfgPost` (activity, role, note) / `LfgBrowse` / `LfgRemove` | |
| S→C | `LfgList` · `EncounterState` (encounterId, phase, timer bars[] for the encounter debugger and boss frames) | |

### 5.6 Economy (0x08xx)

| Direction | Message | Fields |
|---|---|---|
| C→S | `TradeRequest` (targetId) · `TradeSetItem` (tradeSlot, instanceId) · `TradeSetMoney` · `TradeAccept` · `TradeCancel` | |
| S→C | `TradeOpened` · `TradeState` (both sides' items, money, accepted flags) · `TradeClosed` (result) | |
| C→S | `MailList` · `MailSend` (to, subject, body, money, COD, attachments[]) · `MailTakeItem` · `MailTakeMoney` · `MailDelete` · `MailReturn` · `MailMarkRead` | |
| S→C | `MailListResult` · `MailSendResult` · `NewMail` | |
| C→S | `AuctionSearch` | house, name text, level range, slot, type, quality, usable only, page, sort |
| S→C | `AuctionResults` | page of 50: auctionId, itemId, stack, suffix, bid, buyout, time left band, seller name; total |
| C→S | `AuctionCreate` (instanceId, stack, start bid, buyout, duration 2/8/24 h) · `AuctionBid` (auctionId, amount) · `AuctionBuyout` · `AuctionCancel` · `AuctionMyAuctions` · `AuctionMyBids` | |
| S→C | `AuctionResult` · `AuctionOutbid` · `AuctionSold` (notifications; goods and coin arrive by mail) | |

### 5.7 Professions (0x09xx)

| Direction | Message | Fields |
|---|---|---|
| C→S | `GatherStart` (nodeId or corpseId) | then the normal cast flow, then a loot window |
| C→S | `Craft` (recipeId, count) · `CraftCancel` | |
| S→C | `CraftProgress` (recipeId, remaining) · `SkillChanged` (skillId, value, max) · `RecipeLearned` | |
| C→S | `Disenchant` (instanceId) · `EnchantItem` (recipeId, target instanceId or trade slot) | |
| C→S | `FishingCast` · `FishingHook` | S→C `FishingBobber` (entityId), `FishingBite` |
| C→S | `ProfessionUnlearn` (skillId) | |

### 5.8 Guilds (0x0Axx)

| Direction | Message | Fields |
|---|---|---|
| C→S | `GuildCreate` (name, signatures) · `GuildInvite` · `GuildAccept` / `GuildDecline` · `GuildLeave` · `GuildKick` · `GuildPromote` / `GuildDemote` · `GuildSetMotd` · `GuildSetInfo` · `GuildSetNote` (name, public or officer, text) · `GuildSetRank` (index, name, permissions, money per day) · `GuildDisband` · `GuildSetLeader` · `GuildTabardSave` | |
| S→C | `GuildRoster` (members[], ranks[]) · `GuildEvent` (kind, names) · `GuildInfo` | |
| C→S | `GuildBankOpen` · `GuildBankTab` (tab) · `GuildBankDeposit` (instanceId, tab, slot) · `GuildBankWithdraw` (tab, slot, count) · `GuildBankMove` · `GuildBankMoney` (deposit or withdraw, amount) · `GuildBankBuyTab` · `GuildBankSetTab` (name, icon, note) · `GuildBankSetPermission` (rank, tab, view, deposit, withdrawals per day) · `GuildBankLog` (tab or money) | |
| S→C | `GuildBankState` (money, tabs bought, remaining withdrawals today) · `GuildBankTabContents` (tab, 98 slots) · `GuildBankSlotChanged` · `GuildBankLogResult` | |

### 5.9 PvP (0x0Bxx)

| Direction | Message | Fields |
|---|---|---|
| C→S | `BattlegroundQueue` (battlegroundId, as group) · `BattlegroundLeaveQueue` · `BattlegroundAccept` · `BattlegroundLeave` | |
| S→C | `BattlegroundStatus` (queued with estimated wait, ready with 60 s to accept, in progress, finished) · `BattlegroundScore` (team scores, per-player rows) · `BattlegroundObjective` (hill owner, crown bearer, shrine owners) · `BattlegroundEnd` (placing, marks awarded) | |
| S→C | `PvpZoneState` (free-for-all on or off) · `MarksChanged` · `PitChestAnnounce` (minutes) | |

### 5.10 World and travel (0x0Cxx)

| Direction | Message | Fields |
|---|---|---|
| C→S | `TaxiOpen` (npcId) · `TaxiTake` (destination node) | S→C `TaxiMap` (known nodes, fares) · `TaxiStart` (path, duration) · `TaxiEnd` |
| S→C | `TransportState` | transportId, position on its path, at stop or under way (the ship, lifts, mine-carts) |
| C→S | `Mount` (itemId) / `Dismount` · `AreaTriggerEnter` (triggerId; verified by position) | `UseHearthstone` and `SitStand` are in §5.3 |
| S→C | `ZoneChange` (zoneId; a hand-over between zone hosts, invisible to the player) · `LoginQueue` (position, estimated wait; sent on the login connection while the realm is full) · `WeatherChange` · `GameClock` (every 60 s) · `ServerMessage` (restart warnings, world boss spawn) · `RestState` | |
| C→S | `SettingsSave` (keybindings, UI, action buttons, macros; channel 2) · `BarberApply` · `TicketCreate` | |

### 5.11 GM and debug (0x0Fxx)

`GmCommand` (C→S, text) and `GmResult` (S→C, text). Accepted only from accounts with `gm_level` ≥ 1; every command is written to `gm_audit`.

| Command | Level | Effect |
|---|---|---|
| `.tele <zone> [x y z]` · `.goto <player>` · `.summon <player>` | 1 | Movement |
| `.info <player>` · `.who` | 1 | Inspection |
| `.mute <player> <minutes>` · `.kick <player>` | 1 | Moderation |
| `.additem <id> [count]` · `.money <copper>` · `.level <n>` · `.learn <spell>` · `.skill <id> <value>` · `.rep <id> <value>` | 2 | Character fix-ups |
| `.quest add / complete / remove <id>` | 2 | Quest fix-ups |
| `.spawn <creature>` · `.despawn` · `.kill` · `.revive` · `.respawn` | 2 | World |
| `.god` · `.speed <mult>` · `.fly` · `.invis` | 2 | Testing |
| `.encounter start / skip-phase / reset` · `.timer <key> now` | 2 | Encounter and world-boss testing |
| `.ban <account> <hours> <reason>` · `.shutdown <seconds>` · `.reload content` | 3 | Administration |

## 6. Error codes

One enum, `ResultCode` (u16), used by every "result" and "failed" message. Each code has an English string in `content/strings/en/errors.yaml`.

| Group | Codes |
|---|---|
| General | Ok · Unknown · NotAllowed · Throttled · InvalidTarget · TooFarAway · NotInLineOfSight · NotFacing · YouAreDead · TargetIsDead · InCombat · NotInCombat · Busy |
| Spells | NotKnown · NotReady · NotEnoughRage · NotEnoughMana · Silenced · Stunned · Rooted · Moving · WrongStance · NeedsShield · NeedsWeaponType · TargetNotBelowHealth · TargetWrongType · OutOfRange · TooClose · Interrupted · SchoolLocked · NothingToDispel · ReagentMissing · TargetFriendly · TargetHostile · NoPath |
| Items | BagsFull · ItemNotFound · CannotEquip · LevelTooLow · WrongClass · AlreadyBound · UniqueLimit · NotEnoughMoney · VendorOutOfStock · CannotSell · DurabilityBroken · StackFull |
| Quests | QuestLogFull · LevelTooLowForQuest · PrerequisiteMissing · AlreadyOnQuest · AlreadyCompleted · ObjectivesNotComplete · RewardNotChosen |
| Social | PlayerNotFound · PlayerOffline · PlayerIgnoresYou · AlreadyInGroup · GroupFull · NotLeader · NameInvalid · NameTaken |
| Economy | TradeTooFar · TradeCancelled · MailboxFull · CannotMailBound · AuctionBidTooLow · AuctionOwnItem · AuctionNotFound |
| Guild | AlreadyInGuild · NoPermission · GuildBankLimitReached · GuildBankTabFull |
| Instances | InstanceLocked · InstanceFull · NeedsGroup · NeedsRaid · NotAttuned · TooManyInstances |
| Login | BadCredentials · Banned · VersionMismatch · ContentMismatch · RealmFull · AlreadyLoggedIn · CharacterLimit |

## 7. Rate limits

Per connection. Exceeding a limit drops the packet and returns `Throttled`; five drops in ten seconds disconnects.

| Class of message | Limit |
|---|---|
| `MoveInput` | 30 per second |
| `CastSpell`, `UseItem`, `AttackStart` | 10 per second |
| Inventory moves, loot, vendor | 20 per second |
| Chat | See §5.4 |
| `WhoRequest`, `AuctionSearch`, `InspectRequest` | 1 per 2 seconds |
| `MailSend`, `AuctionCreate` | 2 per second |
| Everything else | 30 per second |

## 8. Bandwidth budget

| Situation | Target per client | How it is met |
|---|---|---|
| Idle in a capital with 60 players near | ≤ 6 KB/s | Movement of others at 10 Hz, delta updates, health as a byte fraction |
| 5-player dungeon fight | ≤ 5 KB/s | Combat events are 12–20 bytes each |
| 40-player world boss | ≤ 15 KB/s | Movement of distant players drops to 5 Hz; periodic ticks from other players' auras on other targets are batched every 500 ms |

## 9. Tests required for the protocol

Every message type has a round-trip test (write, read, compare). `Game.Protocol.Tests` also holds: a fuzz test that feeds random bytes to every reader and requires a clean rejection; a version-mismatch test; and a golden-file test that fails if any existing message's byte layout changes without the protocol version being raised.
