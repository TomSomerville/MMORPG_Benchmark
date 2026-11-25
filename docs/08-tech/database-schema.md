# Database Schema

[← Master Plan](../../MASTER_PLAN.md) · Prev: [Content Schemas](content-schemas.md) · Next: [Network Protocol](network-protocol.md) · Overview: [Data Model §2](data-model.md#2-persistent-database-records)

Every table the server writes, for PostgreSQL. Static game content is never stored here; rows refer to content by its string id. The definitions below are the specification that the migration files in `db/migrations/` implement, in the order shown.

## 1. Rules

| Rule | Detail |
|---|---|
| Keys | `bigint generated always as identity` unless stated. Character and item ids are never reused |
| Content references | `text` columns ending in `_id` that hold a content id, such as `item.quest.tm36.brandbreaker`. No foreign key; the server checks them against the loaded pack at start and logs orphans |
| Time | `timestamptz` in UTC. Durations as `integer` milliseconds |
| Money | `bigint` copper, with `check (money >= 0)` |
| Deletion | Characters are soft-deleted (`deleted_at`) and purged after 30 days. Everything else cascades from its owner |
| Saves | Character rows are written every 60 seconds and on logout, level-up, zone change and death. **Item, money, mail, auction, trade and guild-bank changes are written at once, inside one transaction** |
| Ownership of an item | Exactly one of the location columns applies, enforced by `item_instance.location` |
| Migrations | Numbered, forward-only. A migration never edits an earlier file |

## 2. Accounts

```sql
create table account (
  id            bigint generated always as identity primary key,
  name          text not null unique,          -- login, lowercase, 3-20 chars
  email         text not null unique,
  password_hash text not null,                 -- Argon2id
  created_at    timestamptz not null default now(),
  last_login_at timestamptz,
  gm_level      smallint not null default 0,   -- 0 player, 1 helper, 2 GM, 3 admin
  settings      jsonb not null default '{}'    -- account-wide options
);

create table account_ban (
  id          bigint generated always as identity primary key,
  account_id  bigint not null references account(id) on delete cascade,
  reason      text not null,
  banned_by   bigint references account(id),
  starts_at   timestamptz not null default now(),
  ends_at     timestamptz                      -- null = permanent
);

create table session (
  ticket      uuid primary key,
  account_id  bigint not null references account(id) on delete cascade,
  created_at  timestamptz not null default now(),
  expires_at  timestamptz not null,
  remote_addr inet
);
```

## 3. Characters

```sql
create table "character" (
  id              bigint generated always as identity primary key,
  account_id      bigint not null references account(id),
  name            text not null,               -- 2-12 letters, first capital
  race_id         text not null,
  class_id        text not null,
  sex             smallint not null,           -- 0 male, 1 female
  appearance      jsonb not null,              -- skin, face, hair, hairColour, facial
  level           smallint not null default 1,
  xp              integer not null default 0,
  rested_xp       integer not null default 0,
  money           bigint not null default 0 check (money >= 0),
  zone_id         text not null,
  instance_id     bigint,                      -- null when in the open world
  pos_x real not null, pos_y real not null, pos_z real not null, facing real not null,
  bind_zone_id    text not null,
  bind_x real not null, bind_y real not null, bind_z real not null,
  health          integer not null,
  resource        integer not null,
  is_dead         boolean not null default false,
  corpse_zone_id  text, corpse_x real, corpse_y real, corpse_z real,
  played_seconds  bigint not null default 0,
  level_played_seconds bigint not null default 0,
  talent_points_spent smallint not null default 0,
  respec_price    bigint not null default 10000,          -- copper; 1g
  respec_decay_at timestamptz,                            -- next weekly decay
  mount_fed_seconds integer not null default 0,           -- epic mount Fed clock
  active_title_id text,
  created_at      timestamptz not null default now(),
  last_logout_at  timestamptz,
  deleted_at      timestamptz
);
create unique index character_name_live on "character"(lower(name)) where deleted_at is null;
create index character_account on "character"(account_id) where deleted_at is null;

create table character_aura (               -- auras that persist through logout
  character_id bigint not null references "character"(id) on delete cascade,
  aura_id      text not null,
  caster_id    bigint,
  stacks       smallint not null default 1,
  remaining_ms integer not null,
  primary key (character_id, aura_id, caster_id)
);

create table character_cooldown (
  character_id bigint not null references "character"(id) on delete cascade,
  spell_id     text not null,              -- or a shared cooldown group id
  ready_at     timestamptz not null,
  primary key (character_id, spell_id)
);

create table character_spell   (character_id bigint not null references "character"(id) on delete cascade, spell_id text not null, primary key (character_id, spell_id));
create table character_talent  (character_id bigint not null references "character"(id) on delete cascade, talent_id text not null, rank smallint not null, primary key (character_id, talent_id));
create table character_skill   (character_id bigint not null references "character"(id) on delete cascade, skill_id text not null, value smallint not null, max_value smallint not null, primary key (character_id, skill_id));
create table character_recipe  (character_id bigint not null references "character"(id) on delete cascade, recipe_id text not null, primary key (character_id, recipe_id));
create table character_reputation (character_id bigint not null references "character"(id) on delete cascade, reputation_id text not null, value integer not null default 0, at_war boolean not null default false, primary key (character_id, reputation_id));
create table character_explored (character_id bigint not null references "character"(id) on delete cascade, subarea_id text not null, primary key (character_id, subarea_id));
create table character_flight_node (character_id bigint not null references "character"(id) on delete cascade, node_id text not null, primary key (character_id, node_id));
create table character_title   (character_id bigint not null references "character"(id) on delete cascade, title_id text not null, primary key (character_id, title_id));
create table character_currency (character_id bigint not null references "character"(id) on delete cascade, currency_id text not null, amount integer not null check (amount >= 0), primary key (character_id, currency_id));  -- Marks of Valor

create table character_action_button (
  character_id bigint not null references "character"(id) on delete cascade,
  bar smallint not null, slot smallint not null,
  kind smallint not null,                  -- 0 spell, 1 item, 2 macro
  ref  text not null,
  primary key (character_id, bar, slot)
);

create table character_macro (
  id bigint generated always as identity primary key,
  character_id bigint not null references "character"(id) on delete cascade,
  name text not null, icon text not null, body text not null check (length(body) <= 255)
);

create table character_settings (
  character_id bigint primary key references "character"(id) on delete cascade,
  keybindings jsonb not null default '{}',
  ui          jsonb not null default '{}',   -- window positions, chat tabs, tracked quests
  flags       jsonb not null default '{}'    -- tutorial tips seen, story flags such as rl14_ysolde
);
```

## 4. Quests

```sql
create table character_quest (             -- quests in the log
  character_id bigint not null references "character"(id) on delete cascade,
  quest_id     text not null,
  accepted_at  timestamptz not null default now(),
  progress     integer[] not null,         -- one counter per objective, in order
  state        smallint not null default 0,-- 0 active, 1 objectives complete, 2 failed
  expires_at   timestamptz,
  primary key (character_id, quest_id)
);

create table character_quest_done (
  character_id bigint not null references "character"(id) on delete cascade,
  quest_id     text not null,
  completed_at timestamptz not null default now(),
  primary key (character_id, quest_id)
);

create table character_object_state (      -- per-player world objects and world-state changes
  character_id bigint not null references "character"(id) on delete cascade,
  object_id    text not null,              -- lit lanterns, defused charges, the lit Old Forge
  state        smallint not null,
  primary key (character_id, object_id)
);
```

## 5. Items

```sql
create type item_location as enum ('equipped','bag','bank','mail','auction','guild_bank','trade_escrow');

create table item_instance (
  id            bigint generated always as identity primary key,
  item_id       text not null,
  location      item_location not null,
  owner_character_id bigint references "character"(id) on delete cascade,
  container     smallint,                  -- equipped: 0; bag index 0-4; bank bag index 0-6
  slot          smallint,                  -- slot within the container, or equipment slot
  mail_id       bigint,
  auction_id    bigint,
  guild_id      bigint,
  guild_tab     smallint,
  stack         smallint not null default 1 check (stack >= 1),
  durability    smallint,
  suffix_id     text,
  enchant_id    text,
  temp_enchant_id text, temp_enchant_expires_at timestamptz,
  creator_character_id bigint,
  bound         boolean not null default false,
  charges       smallint,
  tradeable_until timestamptz,             -- raid loot trade window
  created_at    timestamptz not null default now()
);
create unique index item_slot_unique on item_instance(owner_character_id, location, container, slot)
  where location in ('equipped','bag','bank');
create unique index item_guild_slot_unique on item_instance(guild_id, guild_tab, slot) where location = 'guild_bank';
create index item_mail on item_instance(mail_id) where mail_id is not null;
create index item_auction on item_instance(auction_id) where auction_id is not null;

create table character_bank (
  character_id bigint primary key references "character"(id) on delete cascade,
  bag_slots_bought smallint not null default 0     -- 0-6
);
```

## 6. Social, mail and auctions

```sql
create table friend  (character_id bigint not null references "character"(id) on delete cascade, friend_id bigint not null references "character"(id) on delete cascade, note text, primary key (character_id, friend_id));
create table ignored (character_id bigint not null references "character"(id) on delete cascade, ignored_id bigint not null references "character"(id) on delete cascade, primary key (character_id, ignored_id));

create table mail (
  id            bigint generated always as identity primary key,
  to_character_id   bigint not null references "character"(id) on delete cascade,
  from_character_id bigint,                -- null for system and auction mail
  from_name     text not null,
  subject       text not null, body text not null default '',
  money         bigint not null default 0,
  cod           bigint not null default 0,
  sent_at       timestamptz not null default now(),
  deliver_at    timestamptz not null,      -- 1 hour for items between players; instant otherwise
  expires_at    timestamptz not null,      -- 30 days
  read          boolean not null default false,
  returned      boolean not null default false
);
create index mail_to on mail(to_character_id, deliver_at);

create table auction (
  id            bigint generated always as identity primary key,
  house         smallint not null,         -- 0 Concord (linked capitals), 1 neutral (Kite's Rest)
  seller_id     bigint not null references "character"(id),
  item_id       text not null,             -- copied for search
  stack         smallint not null,
  start_bid     bigint not null, buyout bigint,
  current_bid   bigint, bidder_id bigint references "character"(id),
  deposit       bigint not null,
  ends_at       timestamptz not null
);
create index auction_search on auction(house, item_id, ends_at);

create table economy_log (                 -- audit trail for anti-cheat and the economy report
  id          bigint generated always as identity primary key,
  at          timestamptz not null default now(),
  kind        smallint not null,           -- trade, mail, auction sale, vendor, quest, loot, repair, training, guild bank
  character_id bigint, other_character_id bigint,
  money_delta bigint not null default 0,
  item_id     text, item_count smallint
);
create index economy_log_char on economy_log(character_id, at);
```

## 7. Guilds and guild bank

```sql
create table guild (
  id          bigint generated always as identity primary key,
  name        text not null unique,
  leader_id   bigint not null references "character"(id),
  motd        text not null default '', info text not null default '',
  tabard      jsonb,                       -- emblem, border, colours
  bank_money  bigint not null default 0 check (bank_money >= 0),
  bank_tabs_bought smallint not null default 0,   -- 0-6
  created_at  timestamptz not null default now()
);

create table guild_rank (
  guild_id    bigint not null references guild(id) on delete cascade,
  rank_index  smallint not null,           -- 0 = guild master
  name        text not null,
  permissions integer not null,            -- bit flags: invite, kick, promote, demote, motd, officer chat, notes...
  money_per_day bigint not null default 0, -- -1 = unlimited
  primary key (guild_id, rank_index)
);

create table guild_member (
  character_id bigint primary key references "character"(id) on delete cascade,
  guild_id    bigint not null references guild(id) on delete cascade,
  rank_index  smallint not null,
  public_note text not null default '', officer_note text not null default '',
  joined_at   timestamptz not null default now()
);
create index guild_member_guild on guild_member(guild_id);

create table guild_event (guild_id bigint not null references guild(id) on delete cascade, at timestamptz not null default now(), kind smallint not null, actor_id bigint, target_id bigint, detail text);

create table guild_bank_tab (
  guild_id bigint not null references guild(id) on delete cascade,
  tab smallint not null, name text not null, icon text not null, note text not null default '',
  primary key (guild_id, tab)
);

create table guild_bank_permission (
  guild_id bigint not null, rank_index smallint not null, tab smallint not null,
  can_view boolean not null default false, can_deposit boolean not null default false,
  withdrawals_per_day smallint not null default 0,          -- item stacks; -1 = unlimited
  primary key (guild_id, rank_index, tab),
  foreign key (guild_id, rank_index) references guild_rank(guild_id, rank_index) on delete cascade
);

create table guild_bank_usage (            -- daily counters, reset at 09:00 server time
  character_id bigint not null references "character"(id) on delete cascade,
  day date not null, tab smallint not null,                 -- tab -1 = money
  used bigint not null default 0,
  primary key (character_id, day, tab)
);

create table guild_bank_log (
  id bigint generated always as identity primary key,
  guild_id bigint not null references guild(id) on delete cascade,
  at timestamptz not null default now(),
  character_id bigint not null, character_name text not null,
  action smallint not null,                -- deposit, withdraw, move, money in, money out, repair
  tab smallint, item_id text, item_count smallint, money bigint
);
create index guild_bank_log_guild on guild_bank_log(guild_id, at desc);
```

## 8. Instances and world state

```sql
create table instance_save (
  id          bigint generated always as identity primary key,
  instance_content_id text not null,       -- instance.hollow_throne
  created_at  timestamptz not null default now(),
  resets_at   timestamptz not null
);
create table instance_boss_kill (instance_save_id bigint not null references instance_save(id) on delete cascade, encounter_id text not null, killed_at timestamptz not null default now(), primary key (instance_save_id, encounter_id));
create table character_instance_lock (character_id bigint not null references "character"(id) on delete cascade, instance_save_id bigint not null references instance_save(id) on delete cascade, primary key (character_id, instance_save_id));
create table character_instance_entry (character_id bigint not null references "character"(id) on delete cascade, entered_at timestamptz not null default now());  -- 5 per hour cap
create table character_boss_loot_lock (character_id bigint not null references "character"(id) on delete cascade, boss_spawn_key text not null, primary key (character_id, boss_spawn_key));  -- world bosses, once per spawn

create table world_timer (
  key        text primary key,             -- world boss, rare spawn or Pitmaster's Chest id
  next_at    timestamptz not null,
  state      jsonb not null default '{}'
);
```

## 9. Support

```sql
create table gm_audit (id bigint generated always as identity primary key, at timestamptz not null default now(), account_id bigint not null, command text not null, target text);
create table ticket   (id bigint generated always as identity primary key, character_id bigint not null references "character"(id) on delete cascade, opened_at timestamptz not null default now(), body text not null, state smallint not null default 0, handled_by bigint, reply text);
create table schema_version (version integer primary key, applied_at timestamptz not null default now());
```

### Accounts and live service

Added for [Accounts and Live Service](accounts-and-live-service.md), in a later migration than the tables above.

```sql
alter table account
  add column email_verified_at     timestamptz,
  add column birth_date            date,
  add column terms_accepted_at     timestamptz,
  add column entitlements          jsonb not null default '{}',   -- reserved for a future business model
  add column deletion_requested_at timestamptz;                   -- erased 30 days after this

alter table ticket
  add column category smallint not null default 0,                -- stuck, lost item, bug, harassment, account, other
  add column replied_at timestamptz;

create table account_security_log (
  id          bigint generated always as identity primary key,
  account_id  bigint not null references account(id) on delete cascade,
  at          timestamptz not null default now(),
  event       text not null,                 -- login, login_failed, password_reset, email_changed, session_ended
  remote_addr inet
);

create table account_token (                 -- e-mail verification and password reset links
  token       uuid primary key,
  account_id  bigint not null references account(id) on delete cascade,
  kind        smallint not null,             -- 0 verify e-mail, 1 reset password
  expires_at  timestamptz not null,
  used_at     timestamptz
);

create table account_penalty (               -- warnings and mutes; suspensions and bans stay in account_ban
  id          bigint generated always as identity primary key,
  account_id  bigint not null references account(id) on delete cascade,
  kind        smallint not null,             -- 0 warning, 1 mute
  reason      text not null,
  applied_by  bigint references account(id), -- null = automatic
  starts_at   timestamptz not null default now(),
  ends_at     timestamptz,
  appeal_ticket bigint references ticket(id)
);

create table player_report (
  id            bigint generated always as identity primary key,
  at            timestamptz not null default now(),
  reporter_id   bigint not null references "character"(id) on delete cascade,
  reported_id   bigint not null references "character"(id) on delete cascade,
  reason        smallint not null,           -- spam, abuse, name, cheating, botting
  note          text,
  chat_context  jsonb not null default '[]', -- the last 50 lines from the reported player seen by the reporter
  zone_id       text, reporter_pos real[], reported_pos real[],
  state         smallint not null default 0, -- open, actioned, dismissed
  handled_by    bigint references account(id)
);
create index player_report_open on player_report(reported_id) where state = 0;

create table bot_signal (                    -- daily score per character; review only, never an automatic ban
  character_id bigint not null references "character"(id) on delete cascade,
  day          date not null,
  score        real not null,
  detail       jsonb not null,
  primary key (character_id, day)
);

create table name_hold (                     -- names of deleted or renamed characters, held 30 days
  name        text primary key,
  held_until  timestamptz not null,
  character_id bigint
);

create table gameplay_event (                -- telemetry; partitioned by month, kept 13 months
  at           timestamptz not null default now(),
  character_id bigint not null,
  kind         smallint not null,            -- level_up, death, quest_accept, quest_complete, quest_abandon,
                                             -- item_created, item_destroyed, coin_source, coin_sink, instance_run, wipe
  ref          text,                         -- content id concerned
  amount       bigint,
  zone_id      text,
  detail       jsonb
) partition by range (at);
```

## 10. Limits enforced by the server, not the schema

| Limit | Value |
|---|---|
| Characters per account | 10 |
| Character name | 2–12 letters, one capital at the start, no digits, not on the reserved list, unique among live characters |
| Friends / ignores | 50 / 50 |
| Mail in the box | 100; attachments 12 per mail |
| Active auctions per character | 100 |
| Guild members | 500; ranks 10 |
| Macros | 18 per character |

## 11. Transactions that must be atomic

| Operation | Rows touched in one transaction |
|---|---|
| Loot an item | `item_instance` insert, `economy_log` |
| Vendor buy, sell, repair, training | `character.money`, `item_instance`, `character_spell` or `character_recipe`, `economy_log` |
| Trade | Both characters' `money` and every traded `item_instance`, `economy_log` |
| Send or take mail | `mail`, `item_instance`, `character.money` |
| Auction create, bid, buyout, expire | `auction`, `item_instance`, both `character.money`, `mail` (results are mailed) |
| Guild bank move | `item_instance` or `guild.bank_money`, `guild_bank_usage`, `guild_bank_log` |
| Quest turn-in | `character_quest` delete, `character_quest_done` insert, `character` (xp, money, level), reward `item_instance`, `character_reputation` |
| Crafting | Reagent `item_instance` rows, output `item_instance`, `character_skill` |

If the transaction fails, the in-memory change is rolled back and the player sees "That action could not be completed."
