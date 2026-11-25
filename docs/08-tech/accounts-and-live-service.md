# Accounts and Live Service

[← Master Plan](../../MASTER_PLAN.md) · Related: [Database Schema](database-schema.md) · [Network Protocol](network-protocol.md) · [Architecture](architecture.md) · [Milestone Task Lists](milestone-tasks.md) · [Build Procedure](build-procedure.md)

What surrounds the game itself: accounts, names, conduct and moderation, support, anti-cheat and anti-botting, updates, restarts, telemetry, and the policy pages. Most of it is built in milestones M12 to M14; names and chat rules apply from M0. Where a rule needs a company decision the builder cannot make (prices, a mail provider, lawyers), a working default is given and the open item goes in `build/for-the-owner.md`.

## 1. Accounts

| Topic | Rule |
|---|---|
| Registration | A web page served by the login service: account name, e-mail, password, date of birth, acceptance of the terms. Also reachable from a button on the client's login screen |
| Account name | 3 to 20 lower-case letters and digits, unique, used to log in. It and the e-mail address are never shown to other players |
| Password | 10 to 128 characters; checked against a list of the 10,000 most common passwords; stored with Argon2id; never logged |
| E-mail verification | A link valid for 24 hours. An unverified account can create characters but cannot trade, mail, use the auction house or speak in public channels |
| Password reset | A link valid for 1 hour, single use. Using it ends every session on the account |
| Login protection | 5 failed logins in 15 minutes locks login for 15 minutes for that account and address pair. Every login, failure, reset and e-mail change is written to the account security log, which the player can read on the account page |
| Second factor | Not at launch. The login flow has a step reserved for it |
| One session | One game session per account. A second login asks whether to disconnect the first |
| Age | Under 13 (or the local age of digital consent, set by configuration) is refused at registration |
| Cost | Free at launch: no subscription, shop or paid currency. The account record has an `entitlements` field so that a business model can be added without a schema change. The choice is the owner's |
| Mail delivery | Through an SMTP server set by configuration. Tests use a local mail catcher |
| Deletion | A player can request deletion from the account page. The account is disabled at once and erased after 30 days: personal data is removed, character names are released, and economy logs keep only an anonymous id |
| Export | A player can download their account data (account fields, characters, security log) as a file |

## 2. Names

| Rule | Detail |
|---|---|
| Character names | 2 to 12 letters, one capital then lower case, no digits, spaces or symbols; unique on the realm; not three of the same letter in a row |
| Guild names | 2 to 24 characters, letters and single spaces; unique on the realm |
| Reserved | Every named NPC, boss, zone, city and faction in these documents; the words GM, Admin, Moderator, Support and the game's name in any spelling; names of the classes and races. The list is generated from the content, so new content reserves its own names |
| Filter | A profanity list (the builder assembles one from freely licensed word lists, and records the source) applied to names with look-alike letters folded together. Chat uses the same list, on by default, and each player can turn it off for what they read |
| Forced rename | A GM can flag a name. The player must choose a new one at next login; the old name is held for 30 days |
| Released names | A deleted character's name is held for 30 days, in case of restoration, then released |
| Deleted characters | Restorable for 30 days by the player from the character screen, once per 7 days; after that by a GM while the data exists (90 days) |

## 3. Conduct and moderation

| Tool | Rule |
|---|---|
| Report | Right-click a player or a chat line, choose Report, pick a reason (spam, abuse, name, cheating, botting) and add a note. The report stores the last 50 chat lines from that player seen by the reporter, both positions and the time |
| Automatic mute | A character reported for spam by 5 different accounts in 10 minutes is muted in public channels for 30 minutes and placed in the GM queue. Accounts under 2 hours old count as half a report |
| Chat limits | The rate limits in [Network Protocol §7](network-protocol.md#7-rate-limits). In addition: the same line cannot be repeated in a public channel within 30 seconds; whispers to strangers are limited to 10 different players per minute |
| Ignore | Hides chat, whispers, mail, invites, trades and duel requests from that character's whole account |
| Penalties | Warning · mute (1 hour to 7 days) · suspension (1 to 30 days) · permanent ban. Each is recorded with a reason and the GM who applied it; the player sees the reason and the end time at login |
| Appeals | One appeal per penalty, through the ticket system; answered by a different GM account |
| GM levels | The three command levels in [Network Protocol §5.11](network-protocol.md#511-gm-and-debug-0x0fxx). GMs are visible as GMs when they speak, cannot trade or use the auction house on a GM account, and every command is written to the audit table |

## 4. Support

| Topic | Rule |
|---|---|
| Tickets | `/ticket` opens a form: category (stuck, lost item, bug, harassment, account, other) and text. One open ticket per account. The player sees its state: open, answered, closed |
| Self-help first | `/stuck` (already specified), restoring a deleted character, and item buy-back from vendors need no GM |
| Item restoration | A GM can restore an item that was destroyed, sold or disenchanted, from the economy log, once per account per 30 days. Traded or mailed items are not restored |
| Bugs | `/bug` records the text with the character's position, target, zone and build |
| Web admin | For GMs: search accounts and characters, read the security log, penalty history, tickets, the economy log and the audit log; apply penalties; restore items and characters. Reached only from addresses on an allow-list, with its own login |

## 5. Anti-cheat and anti-botting

The server decides everything that matters ([Architecture §5](architecture.md#5-networking)), so the client is never trusted. On top of that:

| Check | Rule |
|---|---|
| Movement | The checks and strikes in [Network Protocol §4](network-protocol.md#4-entities-and-movement) |
| Timing | Cooldowns, cast times and the global cooldown are enforced with server time. A client sending actions early is refused, and 20 refusals in a minute are logged |
| Economy anomalies | A nightly report lists accounts whose coin earned per hour is above the 99.5th percentile for their level, one-way trades and mails of coin between accounts with no other contact, and auctions bought at over 20 times the median price |
| Bot signals | Scored per character per day: more than 16 hours played; pathing that repeats within 1 m for over 2 hours; no chat, no failed actions and no camera movement over 4 hours of play; gathering the same route more than 30 times. A score over the threshold puts the character in the GM queue. Nothing is banned automatically |
| New accounts | Unverified accounts are restricted (§1). Accounts under 24 hours old cannot send coin by mail |
| Duplication | Every item and coin movement is one database transaction ([Database Schema](database-schema.md)); a nightly job checks that coin created minus coin destroyed equals the change in coin held, and raises an alert if not |
| Client integrity | The patcher verifies files (§6). There is no kernel-level anti-cheat |

## 6. Updates, versions and restarts

| Topic | Rule |
|---|---|
| Versions | `major.minor.patch` for the client and server build, and a content hash for the content pack. Both are exchanged at login; a mismatch is refused with a message to update |
| Patcher | The launcher downloads a manifest (file path, size, hash), fetches only changed files over HTTPS, resumes interrupted downloads, verifies every file, and can repair an installation |
| Content hotfix | A content-only change (numbers, text, spawn tables) is published as a new content pack. Zone hosts load it at a rolling restart; clients fetch it at next login. No client build is needed |
| Weekly restart | Once a week, at the raid reset, with warnings in the system channel at 15, 10, 5 and 1 minutes. Target downtime under 15 minutes |
| Emergency restart | Warnings at 5 and 1 minutes. Characters are saved before shutdown |
| Rollback | Every release keeps the previous server build and content pack ready to redeploy. Database migrations are forward-only and each has a tested way to run the previous build against the new schema for one release |
| Backups | Nightly full backup and continuous log archiving, giving recovery to any point in the last 7 days; kept 30 days; a restore is rehearsed in milestone M12 and monthly after |
| Realm status | A status page shows: up, restarting, queue length, last incident |
| Server clock | Realm time is one time zone, set by configuration (default UTC). The in-game day is 4 real hours ([World & Travel](../01-world/world-and-travel.md)) and is the same for every player on the realm |

## 7. Telemetry and crash reports

| Topic | Rule |
|---|---|
| Server metrics | Tick time per host, players per zone, queue length, database latency, error rates, bandwidth per client; kept 30 days |
| Gameplay events | Level-ups, deaths (where, to what), quests accepted, completed and abandoned, items created and destroyed, coin sources and sinks, instance runs and wipes, time per level. Stored by character id, not by person, and used for balance reports |
| Balance reports | Weekly, generated: time to each level against the target in [Progression](../02-systems/progression.md), quests most abandoned, deadliest creatures, coin created and destroyed, most and least chosen talents |
| Client crash reports | On a crash the client offers to send the log, build, graphics card and the last 60 seconds of events. Nothing is sent without that consent |
| Privacy | No advertising identifiers, no third-party analytics, no data sold. The privacy page lists exactly what is stored |

## 8. Legal and policy pages

The builder drafts these as pages served by the login service and linked from the login screen, the launcher and registration. Each is marked DRAFT until the owner has had it reviewed.

| Page | Contents the draft must cover |
|---|---|
| Terms of service | The account is personal; conduct rules by reference; no selling of accounts, coin or items for real money; no automation; penalties and appeals; the service may change or end |
| Privacy policy | What is collected (§1, §7), why, how long it is kept, deletion and export (§1), contact address |
| Code of conduct | Harassment, hate speech, cheating, exploiting bugs, naming rules, spam; what each penalty level is for |
| AI-generated content statement | That the game's art, models, animation, music, sound and voice are AI-generated, and the game's code and data were built by an AI model from a written specification |
| Third-party notices | Licences of every library, tool, font source and generation model used, generated from the build and from `forge/bringup-report.md` |

## 9. Security of the deployment

| Topic | Rule |
|---|---|
| Open ports | Only the login port (7778, TLS), the game port (7777, UDP), HTTPS for the patcher, registration and policy pages, and SSH. Everything else, including the database, Redis, the supervisor and metrics, listens only on the private network or on localhost |
| Certificates | Development and tests use a self-signed certificate that the debug client accepts. A real deployment takes a certificate and key from configuration; obtaining one for the owner's domain is the owner's |
| Secrets | Database passwords, the session signing key, the SMTP password and the admin allow-list come from environment files that are never committed. The deploy command refuses to run with the example values |
| First administrator | Created from the command line on the server, never through the game or the web: `Game.Tools account create --name <name> --gm 3`. The README says how |
| Floods | The gateway limits new connections per address (10 per minute), drops unknown packets before any game code runs, and holds at most 3 connections waiting for a ticket per address |
| Web admin | Its own login, an address allow-list, and every action in the audit table (§4) |
| Database access | The game server's database user cannot drop or alter tables; migrations run as a separate user |
| Updates of the servers themselves | Operating system and container updates are the owner's, listed in `build/for-the-owner.md` with the versions the build was tested on |

## 10. Launch day

The plan for one shared world is task T-M14-06: a staggered release of the login queue, the starting zones' respawn at its floor, and extra guards on the roads out. In addition: character creation opens 24 hours before the world does, so names are chosen without a rush; and `realm.maxPlayers` starts at 60% of measured capacity and is raised in steps as tick times allow.
