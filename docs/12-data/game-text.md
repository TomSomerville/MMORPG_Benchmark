# Game Text — messages, tips, emotes and stock phrases

[← Data Index](00-data-index.md) · Interface: [UI Specification](../08-tech/ui-specification.md) · Errors: [Network Protocol §6](../08-tech/network-protocol.md#6-error-codes) · Quests: [Quest Text](../06-quests/text/00-quest-text-index.md)

Quest text and NPC greetings are written elsewhere. This page holds the rest of the words the player reads: system and error messages, tutorial and loading tips, emote text, tooltip wording and NPC stock phrases, and the rules for any text not listed. Validation rule V29 checks that every string the game uses exists in the string table.

## 1. Rules for all text

| Rule | Detail |
|---|---|
| String table | Every piece of display text is a row in `content/strings/en.yaml` with an id. Code and content refer to ids, never to literal text |
| Ids | `err.<Code>` for error codes · `sys.<area>.<event>` for system messages · `ui.<window>.<control>` for labels · `tip.<n>` and `load.<n>` · `emote.<name>.none` / `.target` / `.self` · `npc.stock.<role>.<n>` |
| Placeholders | In braces: `{name}`, `{item}`, `{count}`, `{money}`, `{level}`, `{zone}`, `{skill}`, `{target}`. `{key:<action>}` shows the key currently bound to that action, so tips stay right when keys are rebound |
| Voice | Plain and short, second person ("You receive…"). No exclamation marks except level-up, a rare item and a boss kill. No jokes in errors |
| Capitals | Sentence case. Names of items, spells, zones, classes and skills keep their capitals |
| Money | `{g}g {s}s {c}c`, leaving out any part that is zero |
| Numbers | Thousands separated by a comma. Durations as "2 min", "30 sec", "1.5 sec cast" |
| Units | Yards for range in tooltips |
| Anything not on this page | The builder writes it in the same voice, adds it to the string table, and keeps interface labels to the names used in the [UI Specification](../08-tech/ui-specification.md) |

## 2. Error messages

One per code in [Network Protocol §6](../08-tech/network-protocol.md#6-error-codes). Shown in red at top centre for 3 seconds, and in the system channel.

| Code | Text | | Code | Text |
|---|---|---|---|---|
| Unknown | Something went wrong. | | NotAllowed | You can't do that. |
| Throttled | You're doing that too quickly. | | InvalidTarget | Invalid target. |
| TooFarAway | You are too far away. | | NotInLineOfSight | Target not in line of sight. |
| NotFacing | You must be facing your target. | | YouAreDead | You are dead. |
| TargetIsDead | Your target is dead. | | InCombat | You can't do that while in combat. |
| NotInCombat | You must be in combat to do that. | | Busy | You are busy. |
| NotKnown | You haven't learned that. | | NotReady | That isn't ready yet. |
| NotEnoughRage | Not enough rage. | | NotEnoughMana | Not enough mana. |
| Silenced | You are silenced. | | Stunned | You are stunned. |
| Rooted | You can't move. | | Moving | You can't do that while moving. |
| WrongStance | You must be in {stance}. | | NeedsShield | You need a shield equipped. |
| NeedsWeaponType | You need a {weaponType} equipped. | | TargetNotBelowHealth | Your target has too much health. |
| TargetWrongType | That can't be used on this target. | | OutOfRange | Out of range. |
| TooClose | You are too close. | | Interrupted | Interrupted. |
| SchoolLocked | You can't cast {school} spells for {seconds} sec. | | NothingToDispel | Nothing to remove. |
| ReagentMissing | You need {item}. | | TargetFriendly | You can't attack that target. |
| TargetHostile | You can't help that target. | | NoPath | No path available. |
| BagsFull | Your bags are full. | | ItemNotFound | Item not found. |
| CannotEquip | You can't equip that. | | LevelTooLow | You must be level {level} to use that. |
| WrongClass | Your class can't use that. | | AlreadyBound | That item is bound to you. |
| UniqueLimit | You can't carry any more of those. | | NotEnoughMoney | You don't have enough money. |
| VendorOutOfStock | That is out of stock. | | CannotSell | The merchant doesn't want that. |
| DurabilityBroken | That item is broken. | | StackFull | That stack is full. |
| QuestLogFull | Your quest log is full. | | LevelTooLowForQuest | You aren't experienced enough for that quest. |
| PrerequisiteMissing | You don't meet the requirements for that quest. | | AlreadyOnQuest | You are already on that quest. |
| AlreadyCompleted | You have already completed that quest. | | ObjectivesNotComplete | You haven't finished that yet. |
| RewardNotChosen | Choose a reward. | | PlayerNotFound | No player named {name} is online. |
| PlayerOffline | {name} is offline. | | PlayerIgnoresYou | {name} is ignoring you. |
| AlreadyInGroup | {name} is already in a group. | | GroupFull | Your group is full. |
| NotLeader | You are not the group leader. | | NameInvalid | That name isn't allowed. |
| NameTaken | That name is taken. | | TradeTooFar | You are too far away to trade. |
| TradeCancelled | Trade cancelled. | | MailboxFull | That player's mailbox is full. |
| CannotMailBound | You can't mail a bound item. | | AuctionBidTooLow | Your bid is too low. |
| AuctionOwnItem | You can't bid on your own auction. | | AuctionNotFound | That auction has ended. |
| AlreadyInGuild | {name} is already in a guild. | | NoPermission | Your guild rank doesn't allow that. |
| GuildBankLimitReached | You have reached your withdrawal limit for today. | | GuildBankTabFull | That bank tab is full. |
| InstanceLocked | You are saved to a different instance. | | InstanceFull | That instance is full. |
| NeedsGroup | You must be in a group to enter. | | NeedsRaid | You must be in a raid group to enter. |
| NotAttuned | You are not yet able to enter. | | TooManyInstances | You have entered too many instances recently. |
| BadCredentials | The account name or password is incorrect. | | Banned | This account has been suspended. |
| VersionMismatch | Your game is out of date. Please update. | | ContentMismatch | Your game files need repair. Please update. |
| RealmFull | The realm is full. Position in queue: {count}. Estimated wait: {minutes} min. | | AlreadyLoggedIn | This account is already logged in. |
| CharacterLimit | You have the maximum number of characters. | | | |

## 3. System messages

| Id | Text |
|---|---|
| sys.xp.kill | {name} dies, you gain {count} experience. |
| sys.xp.rested | {name} dies, you gain {count} experience. (+{bonus} rested) |
| sys.xp.quest | You gain {count} experience. |
| sys.xp.explore | Discovered {zone}: {count} experience gained. |
| sys.level.up | Congratulations, you have reached level {level}! |
| sys.level.gains | You gain {health} health and {resource} {resourceName}. |
| sys.level.talent | You have gained a talent point. |
| sys.loot.item | You receive loot: {item}. |
| sys.loot.items | You receive loot: {item} x{count}. |
| sys.loot.money | You loot {money}. |
| sys.loot.share | Your share of the loot is {money}. |
| sys.loot.other | {name} receives loot: {item}. |
| sys.loot.roll | {name} rolls {roll} ({kind}) for {item}. |
| sys.loot.won | {name} won {item}. |
| sys.loot.passed | {name} passed on {item}. |
| sys.item.created | You create {item}. |
| sys.item.bound | {item} is now bound to you. |
| sys.item.broken | Your {item} is broken. |
| sys.item.lowdurability | Your {item} is damaged. |
| sys.money.gain | You receive {money}. |
| sys.money.spend | You pay {money}. |
| sys.quest.accepted | Quest accepted: {quest} |
| sys.quest.progress | {objective}: {count}/{total} |
| sys.quest.objectivedone | {objective} (complete) |
| sys.quest.complete | {quest} completed. |
| sys.quest.abandoned | Quest abandoned: {quest} |
| sys.quest.failed | {quest} failed. |
| sys.skill.up | Your skill in {skill} has increased to {count}. |
| sys.skill.learned | You have learned {spell}. |
| sys.skill.recipe | You have learned how to create {item}. |
| sys.rep.gain | Your reputation with {faction} has increased by {count}. |
| sys.rep.loss | Your reputation with {faction} has decreased by {count}. |
| sys.rep.rank | You are now {rank} with {faction}. |
| sys.group.invite | {name} invites you to a group. |
| sys.group.joined | {name} joins the group. |
| sys.group.left | {name} leaves the group. |
| sys.group.disband | Your group has been disbanded. |
| sys.group.leader | {name} is now the group leader. |
| sys.group.lootmethod | Loot method changed to {method}. |
| sys.group.ready | {name} is ready. |
| sys.guild.joined | {name} has joined the guild. |
| sys.guild.left | {name} has left the guild. |
| sys.guild.promoted | {name} has been promoted to {rank} by {target}. |
| sys.guild.demoted | {name} has been demoted to {rank} by {target}. |
| sys.guild.motd | Guild message of the day: {text} |
| sys.guild.online | {name} has come online. |
| sys.guild.offline | {name} has gone offline. |
| sys.friend.online | Your friend {name} has come online. |
| sys.friend.offline | Your friend {name} has gone offline. |
| sys.trade.request | {name} wants to trade with you. |
| sys.trade.done | Trade complete. |
| sys.duel.request | {name} has challenged you to a duel. |
| sys.duel.start | Duel starting: {count} |
| sys.duel.won | {name} has defeated {target} in a duel. |
| sys.duel.fled | {name} has fled from {target} in a duel. |
| sys.mail.new | You have new mail. |
| sys.mail.sent | Mail sent. |
| sys.auction.sold | A buyer has been found for your auction of {item}. |
| sys.auction.outbid | You have been outbid on {item}. |
| sys.auction.won | You won an auction for {item}. |
| sys.auction.expired | Your auction of {item} has expired. |
| sys.death.release | You have died. Release to the nearest graveyard? |
| sys.death.corpse | Return to your corpse to come back to life. |
| sys.death.healer | The spirit healer can bring you back now, at a cost to your equipment. |
| sys.death.sickness | You are weakened by your return for {minutes} min. |
| sys.rest.enter | You feel rested here. |
| sys.rest.leave | You no longer feel rested. |
| sys.rest.full | You are fully rested. |
| sys.bind.set | {zone} is now your home. |
| sys.zone.enter | {zone} |
| sys.zone.pvp | Free-for-all territory: other players can attack you here. |
| sys.instance.enter | You have entered {zone}. |
| sys.instance.reset | {zone} has been reset. |
| sys.instance.saved | You are now saved to {zone}. It resets in {duration}. |
| sys.boss.kill | {name} has been slain! |
| sys.world.boss | {name} has been sighted in {zone}. |
| sys.bg.ready | Your battleground is ready. Enter within {seconds} sec. |
| sys.bg.won | {team} wins! |
| sys.bg.deserter | You left a battle early and cannot queue for {minutes} min. |
| sys.afk.on | You are now away: {text} |
| sys.afk.off | You are no longer away. |
| sys.afk.kick | You have been logged out for inactivity. |
| sys.logout.timer | Logging out in {seconds} sec. |
| sys.server.restart | The realm will restart in {duration}. |
| sys.server.message | [Realm] {text} |
| sys.chat.muted | You are muted for {duration}. |
| sys.chat.ignored | You are now ignoring {name}. |
| sys.who.count | {count} players found. |
| sys.played.total | Time played: {duration}. This level: {duration2}. |
| sys.stuck.start | Returning you to a safe place. Don't move. |

## 4. Tutorial tips

The triggers are in [UI Specification §7](../08-tech/ui-specification.md#7-first-session-tutorial-tips).

| # | Text |
|---|---|
| 1 | Move with W, A, S and D. Hold the right mouse button to turn and look. Space jumps. |
| 2 | Someone with a gold ! over their head has work for you. Right-click them to talk. |
| 3 | Your quests are in the quest log ({key:QuestLog}). The tracker on the right shows what is left to do. |
| 4 | Right-click an enemy to attack. Use the abilities on your action bar with the number keys. |
| 5 | Right-click a sparkling corpse to loot it. Hold Shift to take everything at once. |
| 6 | Right-click an item in your bags to wear it. Hold Shift over an item to compare it with what you have on. |
| 7 | You are a spirit. Run back to your body to live again, or ask the spirit healer at the graveyard, who will damage your gear in return. |
| 8 | You have grown stronger. Visit your class trainer to learn new abilities; each costs coin. |
| 9 | Your bags are full. Sell what you don't need to any merchant. |
| 10 | Innkeepers can make this inn your home, where your hearthstone returns you. Resting here earns bonus experience for later. |
| 11 | You can now learn two professions. Look for profession trainers in any town. |
| 12 | Eyrie masters fly you between places you have already visited. Talk to each one you meet. |
| 13 | You have a talent point. Press {key:Talents} to spend it and shape your class. |
| 14 | In a group, loot is shared in turn and experience is split. A much higher-level friend will reduce what you earn. |
| 15 | Mailboxes send letters, coin and items to other players for a small postage. |

## 5. Loading screen tips

One is chosen at random, never the same twice running.

| # | Text |
|---|---|
| 1 | Eating and drinking while seated restores you much faster than waiting. |
| 2 | A grey quest still pays coin, but little experience. |
| 3 | Enemies marked with a skull are far beyond you. Go around. |
| 4 | Creatures of one kind near each other will come to each other's aid. Pull them apart. |
| 5 | Humanoids run for help when they are nearly dead. Finish them quickly. |
| 6 | A monster that chases you too far gives up, runs home and heals. |
| 7 | Rested experience builds while you are logged out in an inn or a capital. |
| 8 | Your hearthstone takes you back to the inn you chose as home. |
| 9 | Armor wears out as you fight and when you die. Any armorer or smith can repair it. |
| 10 | The auction houses in Solhaven and Hammerdeep share one list of goods. |
| 11 | Banks keep what your bags cannot. Extra bank slots can be bought. |
| 12 | A Fighter's rage fades quickly out of combat. Keep fighting to keep it. |
| 13 | A Cleric's mana returns faster when no spell has been cast for five seconds. |
| 14 | Druids call on Nature and the Arcane, and never change shape. |
| 15 | Green items are bound when you put them on. Sell or trade them before you do. |
| 16 | Items from quests and dungeons are bound the moment you pick them up. |
| 17 | Elite enemies are marked on their portrait. Bring friends. |
| 18 | Gathering professions pay well from the start. Crafting pays later. |
| 19 | Ore and herbs grow back in the same places. Learn where they are. |
| 20 | Cooked food gives a lasting bonus that raw food does not. |
| 21 | Bandages work in a fight, as long as nothing hits you. |
| 22 | A tank should keep enemies facing away from the group. |
| 23 | Healing draws the attention of every enemy in the fight. Let the tank strike first. |
| 24 | Meeting stones outside dungeons help you find a group. |
| 25 | A dungeon can be reset by its leader once everyone is outside. |
| 26 | The raid resets once a week. Until then you are saved to your own copy of it. |
| 27 | In the Dustpit, anyone can attack anyone. The chest in the middle is worth it. |
| 28 | Crownfall has three teams. Two of them are always your enemy. |
| 29 | Attack another player from behind and they cannot dodge, parry or block. |
| 30 | Weapon skill rises as you use a weapon. A new kind of weapon will miss until you practise. |
| 31 | Doing quests for a people earns their trust, and in time their rewards. |
| 32 | Type /who to see who is nearby and what they are looking for. |
| 33 | Shift-click an item to link it in chat. |
| 34 | The ship between Solhaven and Hammerdeep is free and leaves every five minutes. |
| 35 | Stoneheart Deeps has no sky. Its map is in layers; watch which one you are on. |
| 36 | Rare creatures are marked on their portrait and always drop something good. |
| 37 | A guild shares a bank. Ask an officer what you may take. |
| 38 | Type /stuck if you are trapped. It takes you to the nearest graveyard. |
| 39 | Falling far enough will kill you. Deep water will not, unless you run out of breath. |
| 40 | There is one world. Everyone you see is really there. |

## 6. Emotes

The 44 commands in [UI Specification §5](../08-tech/ui-specification.md#5-slash-commands). Each has three lines: with no target, with a target, and what the target sees uses the same line with "you" in place of the target's name. Emotes with an animation in the character art list play it; the rest are text only.

| Command | No target | With a target |
|---|---|---|
| /sit | You sit down. | You sit down beside {target}. |
| /stand | You stand up. | You stand up. |
| /sleep | You fall asleep. | You fall asleep. |
| /kneel | You kneel. | You kneel before {target}. |
| /wave | You wave. | You wave at {target}. |
| /bow | You bow. | You bow before {target}. |
| /cheer | You cheer. | You cheer at {target}. |
| /dance | You burst into dance. | You dance with {target}. |
| /laugh | You laugh. | You laugh at {target}. |
| /cry | You cry. | You cry on {target}'s shoulder. |
| /point | You point over there. | You point at {target}. |
| /salute | You salute. | You salute {target}. |
| /thank | You thank everyone around you. | You thank {target}. |
| /hello | You greet everyone. | You greet {target}. |
| /bye | You wave goodbye to everyone. | You wave goodbye to {target}. |
| /no | You shake your head. | You tell {target} no. |
| /yes | You nod. | You nod at {target}. |
| /shrug | You shrug. | You shrug at {target}. |
| /roar | You roar. | You roar at {target}. |
| /flex | You flex. | You flex at {target}. |
| /clap | You clap. | You clap for {target}. |
| /kiss | You blow a kiss into the wind. | You blow a kiss to {target}. |
| /hug | You need a hug. | You hug {target}. |
| /beg | You beg everyone around you. | You beg {target}. |
| /rude | You make a rude gesture. | You make a rude gesture at {target}. |
| /chicken | You flap your arms and cluck. | You cluck at {target}. |
| /train | You make the sound of a mine-cart rolling. | You roll past {target} like a mine-cart. |
| /applaud | You applaud. | You applaud {target}. |
| /shy | You look away shyly. | You smile shyly at {target}. |
| /surrender | You surrender. | You surrender to {target}. |
| /talk | You talk to yourself. | You talk things over with {target}. |
| /taunt | You taunt everyone around you. | You taunt {target}. |
| /threaten | You threaten everyone around you. | You threaten {target}. |
| /violin | You play the world's smallest fiddle. | You play the world's smallest fiddle for {target}. |
| /whistle | You whistle. | You whistle at {target}. |
| /yawn | You yawn. | You yawn at {target}. |
| /cower | You cower in fear. | You cower before {target}. |
| /gasp | You gasp. | You gasp at {target}. |
| /lol | You laugh out loud. | You laugh out loud at {target}. |
| /pray | You pray. | You say a prayer for {target}. |
| /drink | You raise a drink. | You raise a drink to {target}. |
| /eat | You begin to eat. | You begin to eat in front of {target}. |
| /charge | You start to charge. | You charge at {target}. |
| /victory | You bask in the glory of victory. | You bask in the glory of victory with {target}. |

Others nearby see the third-person form: "{name} waves." or "{name} waves at {target}.", made by the rule: replace "You" with the name and put the first verb in its "-s" form. The string table stores both forms.

## 7. Tooltips

| Thing | Lines, top to bottom |
|---|---|
| Item | Name in its quality colour · binding · "Unique" if so · slot and type on one line (left, right) · damage and speed, then "({dps} damage per second)" · armor · stats as "+{n} {Stat}" in white · durability "{cur} / {max}" · "Classes: …" · "Requires Level {n}" (red if unmet) · "Requires {skill} ({n})" · green lines "Equip:", "Use:", "Chance on hit:" · set name and pieces · yellow flavour text in quotes · "Sell Price: {money}" |
| Spell | Name · rank (right, grey) · cost (left) and range (right) · cast time (left) and cooldown (right) · requirement line (stance, weapon, reagent) in white, red if unmet · description in gold with numbers filled in from the caster's stats |
| Aura | Name · description with current numbers · time remaining · dispel type if any |
| Unit | Name · title or guild in angle brackets · "Level {n} {type}" with "(Elite)" or "(Rare)" · for players "Level {n} {race} {class}" · tapped names are grey · "Skinnable", "Requires Mining" where true |
| Quest objective object | Name · the quest's name · "{count}/{total}" |

## 8. NPC stock phrases

Named NPCs have their own greeting in the [rosters](../11-npcs/00-npc-index.md). Unnamed and generic NPCs, and every NPC's goodbye, draw from these, three per role, chosen at random.

| Role | Phrases |
|---|---|
| Vendor, greeting | "Take a look." · "What do you need?" · "Fair prices, same as always." |
| Vendor, goodbye | "Come again." · "Safe roads." · "Mind how you go." |
| Trainer | "Ready to learn?" · "Show me what you remember." · "There is always more to know." |
| Innkeeper | "Bed, board, or both?" · "Sit by the fire a while." · "You look like you've walked far." |
| Guard, idle | "Keep the peace." · "Move along." · "Roads are watched. Mostly." |
| Guard, directions | "{place}? I'll mark it on your map." |
| Guard, attacking | "To arms!" · "Stand down!" · "You'll answer for that!" |
| Flight master | "Where to?" · "They know the way." · "Hold on to the harness." |
| Banker | "Your vault is as you left it." · "Deposits or withdrawals?" · "Everything is accounted for." |
| Auctioneer | "Buying or selling?" · "The list is long today." · "Bids close when they close." |
| Citizen, human | "Morning." · "Mind the cart." · "They say the mill's still smoking." |
| Citizen, dwarf | "Aye?" · "Watch your head on the lintel." · "Stone keep you." |
| Quest giver with nothing to offer | "Nothing more for you just now." |
| Hostile humanoid, aggro | "Get them!" · "You picked the wrong road." · "No witnesses." |
| Hostile humanoid, fleeing | "{name} attempts to run away in fear!" (emote line) |
