# ITEM GRANT PLAN: one path for every item that enters the pack (F-08)

Fable, 2026-11-11. **Revision 2** (after Kimi's audit K95; the changes are listed in section 10). Plan only, no game code. For Sol, after F-17.
All anchors are `scripts/lol2/<file>:<line>` on Sol's Plan 3 head **742dcab** (branch `sol/foundation-whole-game-save-20261111`), because F-08 will be built on top of that stack. If F-17 or a rebase moves lines, the function names in the tables are the stable key.

Grades: PROVEN = I read the line. LIKELY = inferred or machine-derived. UNKNOWN = not checked.

## 0. The short version

- This is structure, not design. **Every item id, every refusal text, every capacity check (and every missing one), every save key stays as it is today.** The plan flags the inconsistencies it finds; it does not smooth them.
- Today an item reaches the pack in six different ways (section 1.3), written out in **62 functions in 53 files** that append, **31 functions in 26 files** that replace the whole pack with a transaction result, and the Cave, which has no pack at all (it derives one from ten owners). 12 more functions in 12 files only remove items.
- The original scripts carry **876 "give item" commands** (opcode 3, kind 1) over the 15 levels. The Act 2 host turns each into an `item_request` signal that is only written to a log (`act2_progression.gd:211`). Nothing reaches the pack from it.
- The plan adds one static module, `item_grants.gd`. The pack arrays stay where they are and keep their names, so the 295 test files that read them and the 85 that write them keep working. The module becomes the only **production** writer.
- Native grants go through a per-level table, **default "log only" as today**, because the command's argument byte (values 4, 1, 0, 3, 5) is not decoded. A row is switched on only with evidence.
- Eleven commits. Commit 0 pins today's behaviour; each later commit keeps it green.
- **Old saves keep loading because no save key is added, renamed or removed.** The pack, the Act 2 item packet and the world-item histories stay in their present fields.

## 1. What exists today

### 1.1 Four pack stores (PROVEN)

| Host | Store | Where |
|---|---|---|
| Museum | `carried_collected: Array` | `museum_walkthrough.gd:52` |
| Jungle and every host that extends it (Dark Halls, Savage Jungle, Ruins, every Act 2/3 map, the Jungle return) | `carried_collected: Array` | `jungle_walkthrough.gd:50`; extended by `dark_halls.gd:1`, `darker_jungle.gd:1`, `dragon_level.gd:1`, `act2_map.gd:1`, `act2_jungle_return.gd` |
| Hive | `carried_inventory.collected` inside a dictionary that also holds the equipped items | `hive_review.gd:25` |
| Cave | **no store.** `carried_items()` adds up ten owners' own state and filters out spent ids | `cave_walkthrough.gd:803-812` |

One accessor already hides three of the four: `player_item_controller.gd:33-34` (`carried()`: Cave method, else Hive dictionary, else `carried_collected`).

Related stores that travel with the pack: `hand_item` (written in 25 files, not traced here), `equipped_item`, `equipped_armor`, `item_effects.spent` (consumed history).

### 1.2 Two catalogs (PROVEN)

| Catalog | Ids | Row by identity | Validation |
|---|---|---|---|
| `item_catalog.gd` (Act 1 and shared) | fixed names, per-owner ids, `item:defNNN` generic ids in scope "world" (`:33`, `:220`) | `item_definitions.gd:45` `by_identity(identity) -> index` | `validate_carried` `:302` (no duplicates, admitted in scope, at most `MAX_CARRIED := 64` `:55`) |
| `act2_items_catalog.gd` (Act 2/3) | placement ids `act2:<AREA>:itemN`, about 30 hand-written special ids in `row()` `:36-91`, `:charged:<colour>` variants | each row carries `identity` | `validate` `:95-106`: carried at most 64, no duplicate base id, **every carried id must be in the `collected` history** |

The Act 2 packet lives at `quest_state.act2_items = {version, carried, collected}` (`:94`). `sync(host)` `:107-110` rebuilds `carried` from the pack; `restore(host)` `:111-118` rebuilds the pack from it. The combined limit (old items plus Act 2 items at most 64) is checked at `:116`, `act2_map.gd:324` and `darker_jungle.gd:274`.

### 1.3 The six ways an item enters the pack

| # | Way | Example | Count |
|---|---|---|---|
| A | Owner appends to the pack itself | `museum_prism.gd:83`, `l19_belial_horn.gd:69` | section 2.1 |
| B | Owner passes the pack into a rule function that appends in place | `museum_aloe.gd:54` -> `museum_aloe_state.gd:22` | in 2.1, callers in 2.2 |
| C | Owner replaces the whole pack with a transaction result (`mechanism_transaction.gd`, or an owner's own pure function) | `l8_tree.gd:72`, `l10_priest.gd:45` | section 2.3 |
| D | Cave: owner sets its own "taken" state; the pack is derived | `cave_guard38_loot.gd:72-75` | section 2.4 |
| E | An Act 1 character's own script reader decodes the give command and calls back | `jungle_kityara_state.gd:213` -> `jungle_walkthrough.gd:886-890` | section 2.5 |
| F | Act 2 native host: `item_request` signal | `native_script_host.gd:1093`, `:1697-1709` | 876 commands, section 2.6 |

### 1.4 What differs between sites today (flag, do not fix)

- **Capacity.** Three spellings of 64: `Catalog.MAX_CARRIED`, a literal `64` (`l12_citadel.gd:23`, `l8_herbalist.gd:26`, and 30 default arguments `capacity:int=64` in 24 files), `l8_journey_state.gd:7` `LIMIT := 64`. One different number: the Hive Ancient Stone refuses at 23 items (`hive_ancient_stone.gd:15`, `:26`). 26 grant functions show no capacity check in their own body (table 2.1, column Cap); for some the caller checks, for some nobody does (for example `museum_walkthrough.gd:1039` `take_mail`, `:1051` `take_stone`, `hive_wax.gd:35`, `jungle_walkthrough.gd:889`).
- **Refusal text.** "Inventory full." (the world-item owners `act2_world_items.gd:84`, `area_world_items.gd:171`, `jungle_world_items.gd:98`, `hive_world_items.gd:91`, `jungle_river_dam.gd:354`; `dark_halls_loot.gd:59`, `dark_halls_rix.gd:52`; `l12_frozen_bow.gd:54`, `l12_niche_armor.gd:41`, `l14_trials.gd:61`, `l14_post_shard.gd:32`, `l8_herbalist.gd:26`, `l8_journey_state.gd:51`, `:70`), "You cannot carry more." (Museum owners, `hive_net_exile.gd:77`, `jungle_harvest.gd`), "Your inventory is full." (`jungle_kelsrick.gd:305`, `l12_citadel.gd:23`, `l13_altar_state.gd:34`), "You cannot carry more wax." (`jungle_beehives.gd:97`).
- **History.** Act 2 owners append to `quest_state.act2_items.collected` by hand. Two things differ per site (table 2.9): **whether the append is guarded** (16 sites append unconditionally, two of them inside a pure builder; 8 append only if the id is absent) and **how the packet is written** (in place, or a deep copy that is assigned back; `l10_priest.gd:52` and `l10_silverleaf_harvest.gd:24` build the new packet in a pure function). The packet is saved data and `validate` (`act2_items_catalog.gd:95-106`) refuses a duplicate in `collected`, so the guard is behaviour, not style. World-item owners keep their own `history(true).collected`. Many Act 1 owners keep only a `taken` flag.
- **Sync.** Some Act 2 owners call `Items.sync(host)` after the write, some do not (column Sync).
- **Text on success.** "<Item> added to inventory.", "<Item> taken.", "You pick a Silverleaf (9 of 9).", or nothing.
- **Journal.** Only a few grants touch the Journal (column Journal).

## 2. Census

How it was made: the tree at 742dcab was searched for every line that appends to, erases from, assigns or aliases `carried_collected`, `carried_inventory.collected`, `carried_items()`, `carried()`, or a local named `inventory`, `carried`, `pack`, `collected`, `bag`; each hit was put under its function. The side-effect columns are a **text search of that function's body** (LIKELY, not read line by line): Cap = mentions `MAX_CARRIED`, `capacity`, `>= 64` or `LIMIT`; Dup guard = a "not in" test; History = writes a history or `collected` list; Sync = `Items.sync`; Text = `save_feedback`; Journal = Journal call; Equip/HUD = touches equipment, the hand or the HUD. A "-" under Cap can mean the caller checks.
Kimi: the raw line list is 166 lines in 88 files; `.orig` files were left out (`museum_walkthrough.gd.orig` repeats six Museum lines).

### 2.1 Functions that add to a pack or a history (62 functions, 53 files)

Includes rule functions that append to an array handed to them (way B) and three `restore` functions that rebuild a history from the pack. `player_dragon_blood.gd:29` `place` was listed here in revision 1; it only appends to the spent history and **erases** from the live pack, so it now sits in 2.7.

| File:lines | Function | Cap | Dup guard | History | Sync | Text | Journal | Equip/HUD |
|---|---|---|---|---|---|---|---|---|
| `act2_world_items.gd:87,88` | `take` | yes | - | yes | - | yes | - | - |
| `area_world_items.gd:113` | `restore` | - | yes | yes | - | - | - | - |
| `area_world_items.gd:173,174` | `collect` | yes | - | yes | - | - | - | - |
| `cave_aloe.gd:80` | `harvest` | - | - | yes | - | - | - | - |
| `cave_stalagmite.gd:97` | `harvest` | - | - | yes | - | - | - | - |
| `cave_stone_manafoil.gd:127` | `take` | yes | - | yes | - | - | - | - |
| `dark_halls_loot.gd:61` | `take` | yes | - | yes | - | yes | - | - |
| `dark_halls_rix.gd:54` | `take_staff` | yes | yes | yes | - | yes | - | - |
| `hive_flute_floor.gd:214` | `_apply` | - | - | - | - | - | - | - |
| `hive_net_exile.gd:78` | `use` | yes | yes | yes | - | yes | - | - |
| `hive_reaver_amber_state.gd:103` | `take_reaver` | yes | yes | yes | - | - | - | - |
| `hive_reaver_amber_state.gd:113` | `harvest_amber` | yes | - | yes | - | - | - | - |
| `hive_rune_transaction.gd:59,60` | `copy_wax` | - | yes | yes | - | - | - | - |
| `hive_wax.gd:35` | `collect` | - | - | yes | - | - | - | - |
| `hive_world_items.gd:41` | `restore` | - | yes | yes | - | - | - | - |
| `hive_world_items.gd:93,94` | `collect` | yes | - | yes | - | - | - | - |
| `jungle_beehives_state.gd:36` | `harvest` | yes | yes | yes | - | - | - | - |
| `jungle_harvest_state.gd:97` | `harvest` | yes | - | yes | - | - | - | - |
| `jungle_kelsrick.gd:307` | `collect_loot` | yes | - | yes | - | yes | - | yes |
| `jungle_river_dam.gd:356,357` | `collect` | yes | - | yes | - | yes | - | - |
| `jungle_source_pickups.gd:68` | `collect` | - | - | yes | - | - | - | - |
| `jungle_walkthrough.gd:889` | `_kityara_grant` | - | yes | yes | - | - | - | yes |
| `jungle_world_items.gd:68` | `restore` | - | - | yes | - | - | - | - |
| `jungle_world_items.gd:100,101` | `collect` | yes | - | yes | - | yes | - | - |
| `l10_emperor_state.gd:67` | `take` | yes | - | - | - | - | - | - |
| `l10_priest.gd:52,53` | `grant` | yes | - | yes | - | - | - | - |
| `l10_silverleaf_harvest.gd:24,25` | `pick` | yes | - | yes | - | - | - | - |
| `l12_citadel.gd:25` | `search_body` | yes | - | yes | yes | - | - | - |
| `l12_frozen_bow.gd:56` | `take` | yes | - | yes | yes | - | - | - |
| `l12_niche_armor.gd:43,44` | `take` | yes | - | yes | yes | - | - | yes |
| `l13_altar_state.gd:36` | `take_stone` | yes | - | - | - | - | - | - |
| `l13_dawn_release.gd:35` | `offer` | yes | - | - | - | - | - | - |
| `l14_hopper_platform.gd:78,79` | `take` | yes | - | yes | yes | - | - | - |
| `l14_post_shard.gd:33,34` | `take` | yes | - | yes | yes | - | - | - |
| `l14_trials.gd:64,65` | `take` | yes | yes | yes | yes | - | - | - |
| `l16_dry_fountain.gd:156,158` | `take` | yes | yes | yes | yes | - | - | - |
| `l16_fountain_ball.gd:85,86` | `take` | yes | - | yes | yes | - | - | - |
| `l19_belial_horn.gd:65,69` | `take` | yes | yes | yes | yes | - | - | - |
| `l19_dawn_curse.gd:242,245` | `_grant_ruby` | yes | yes | yes | yes | - | - | - |
| `l8_herbalist.gd:32` | `pick` | yes | - | yes | - | - | - | - |
| `l8_journey_state.gd:44,52,71` | `act` | yes | yes | - | - | - | - | - |
| `magic_shop_rooms.gd:221` | `grant` | - | - | - | - | - | - | - |
| `monastery_rooms.gd:233` | `grant` | - | yes | - | - | - | - | - |
| `monastery_rooms.gd:417` | `take_wax` | yes | - | - | - | yes | - | - |
| `monastery_rooms.gd:468` | `take_stone` | - | - | - | - | yes | - | - |
| `museum_aloe_state.gd:22` | `take` | - | - | - | - | - | - | - |
| `museum_blood_loot.gd:71` | `use` | yes | - | yes | - | - | - | yes |
| `museum_broken_thohan.gd:78,89,90` | `run_source_group` | - | yes | yes | - | - | yes | yes |
| `museum_crystal.gd:60` | `use` | yes | yes | yes | - | yes | - | - |
| `museum_dragon_heart.gd:104` | `use` | yes | - | yes | - | yes | - | - |
| `museum_ivory_state.gd:23` | `take` | yes | - | - | - | - | - | - |
| `museum_key_locks_state.gd:51,57` | `run` | - | - | yes | - | - | - | - |
| `museum_key_locks_state.gd:75,79` | `run_panel` | - | - | yes | - | - | - | - |
| `museum_lightning_crystal.gd:32` | `use` | - | - | yes | - | yes | - | - |
| `museum_long_arm_state.gd:46` | `take` | - | - | yes | - | - | - | - |
| `museum_prism.gd:83` | `_collect` | yes | - | yes | - | yes | - | - |
| `museum_scroll_state.gd:28` | `take` | - | - | - | - | - | - | - |
| `museum_walkthrough.gd:541` | `take_sword` | - | yes | yes | - | - | - | yes |
| `museum_walkthrough.gd:1039` | `take_mail` | - | - | yes | - | yes | - | - |
| `museum_walkthrough.gd:1051` | `take_stone` | - | - | yes | - | yes | - | - |
| `thieves_den_rooms.gd:241` | `grant` | - | - | - | - | - | - | yes |
| `weapon_shop_rooms.gd:141` | `apply_effects` | - | yes | yes | - | - | - | - |

### 2.2 Callers that hand the live pack to a rule function (way B, PROVEN)

| Caller | Rule function |
|---|---|
| `museum_aloe.gd:54` | `museum_aloe_state.gd:22` `take` |
| `museum_scrolls.gd:54` | `museum_scroll_state.gd:28` `take` |
| `museum_ivory.gd:84` | `museum_ivory_state.gd:23` `take` |
| `museum_long_arm.gd:134-136` (packet `{collected, hand}`) | `museum_long_arm_state.gd:46` `take` |
| `museum_key_locks.gd:367`, `:369` (packet) | `museum_key_locks_state.gd:51-57` `run`, `:75-79` `run_panel` |
| `jungle_beehives.gd:95-96` (packet) | `jungle_beehives_state.gd:36` `harvest` |
| `jungle_harvest.gd:125-126` (packet with `spent`) | `jungle_harvest_state.gd:97` `harvest` |
| `hive_reaver_amber.gd:214` | `hive_reaver_amber_state.gd:103` `take_reaver`, `:113` `harvest_amber` |
| `hive_net_exile.gd:75-78` | appends through the alias `collected` |
| `hive_world_items.gd:88-94` | appends through the alias `carried` |
| `hive_rune_entry.gd:259` | `hive_rune_transaction.gd:59-60` `copy_wax` (erases the wax, appends the copy) |
| `hive_rune_entry.gd:246`, `:278` | `hive_ancient_stone.gd:14-17` `begin`, `:19-29` `advance` (appends the Ancient Stone at `:27` to the parameter `items`). **Not in table 2.1**: the search did not look for a parameter of that name. Found by a second sweep for calls that pass the live pack as an argument; that sweep found no other case |
| `magic_shop_rooms.gd:217-221`, `monastery_rooms.gd:226-233`, `:411-417`, `:463-468`, `thieves_den_rooms.gd:238-241` | append through the alias `carried` of `get_parent().carried_collected` |
| `l8_herbalist.gd:32` | appends to the `carried` it is given |

### 2.3 Functions that replace the whole pack with a result (31 functions, 26 files)

These both add and remove. The new pack is computed by `mechanism_transaction.gd` (`offer` `:50`, `commit` `:79`, `retrieve` `:95`; preloaded as `Kit` in 35 files) or by the owner's own pure function, then assigned.

| File:lines | Function | Cap | Dup guard | History | Sync | Text | Journal | Equip/HUD |
|---|---|---|---|---|---|---|---|---|
| `act2_chargers.gd:55` | `interact` | - | - | - | yes | - | - | - |
| `l10_emperor.gd:66,69` | `interact` | - | - | yes | yes | - | - | - |
| `l10_emperor.gd:124,126` | `collect_remains` | - | - | yes | yes | - | - | - |
| `l10_emperor_entry.gd:73` | `offer` | - | - | yes | yes | - | - | - |
| `l10_priest.gd:45` | `speak` | - | - | yes | yes | - | - | - |
| `l10_priest.gd:72,76,78` | `exchange_ashes` | - | yes | yes | yes | - | - | - |
| `l10_silverleaf.gd:56` | `pick` | - | - | yes | yes | - | - | - |
| `l10_tombs.gd:81` | `offer` | - | - | - | yes | - | - | - |
| `l12_citadel.gd:40` | `throw_picture` | - | - | yes | yes | - | - | yes |
| `l13_altar.gd:38,39` | `enchant` | - | - | yes | yes | - | - | yes |
| `l13_altar.gd:47,48` | `take_stone` | - | - | yes | yes | - | - | - |
| `l13_dawn_prison.gd:88` | `finish` | - | - | yes | yes | yes | - | - |
| `l13_exit_lock.gd:36` | `interact` | - | - | - | yes | - | - | yes |
| `l14_flute_slot.gd:64` | `interact` | yes | - | - | yes | - | - | yes |
| `l14_hopper_platform.gd:93` | `place` | yes | - | - | yes | - | - | yes |
| `l14_idol_pedestals.gd:75` | `offer` | yes | - | - | yes | - | - | yes |
| `l14_niche.gd:60` | `offer` | yes | - | - | yes | - | - | yes |
| `l14_priest_ritual.gd:75` | `offer` | - | yes | - | yes | - | - | yes |
| `l14_shard_bowls.gd:68` | `offer` | yes | - | - | yes | - | - | yes |
| `l14_spiral.gd:70` | `interact` | yes | - | - | yes | - | - | yes |
| `l8_dawn.gd:27,28` | `interact` | - | - | yes | yes | - | yes | yes |
| `l8_journey.gd:92,111` | `interact` | - | - | yes | - | yes | - | yes |
| `l8_larkhon.gd:56,57` | `mix` | - | - | yes | yes | yes | - | yes |
| `l8_larkhon.gd:78` | `offer` | - | - | - | yes | - | - | yes |
| `l8_temple_door.gd:24` | `interact` | - | - | - | yes | - | - | yes |
| `l8_tree.gd:72` | `interact` | - | - | - | yes | - | - | yes |
| `l8_tribe.gd:25` | `offer` | - | - | - | yes | - | - | - |
| `l8_tribe.gd:100,101` | `offer_shaman` | - | - | yes | yes | - | - | - |
| `l9_pyre.gd:72,74` | `urn` | - | - | yes | yes | - | - | - |
| `l9_statue.gd:46` | `offer` | - | - | - | yes | - | - | - |
| `player_item_controller.gd:68,75,96,105,113,124,130,131` | `use` | - | yes | yes | - | yes | - | - |

Pure functions that build the new pack for those owners (PROVEN): `l10_emperor_state.gd:61-67`, `l10_priest.gd:47-53`, `l10_silverleaf_harvest.gd:24-25`, `l13_altar_state.gd:34-36`, `l13_dawn_release.gd:21-35`, `l8_journey_state.gd:44-71`, `l8_dawn_state.gd:22`, `l8_shaman_trade.gd:23`, `l8_tribe_state.gd:37`, `l9_statue_state.gd:15`, `l10_tomb_state.gd:31`, and the insert/retrieve pairs in `l8_temple_door_state.gd:9,21`, `l8_tree_slot_state.gd:9,21`, `l13_exit_lock_state.gd:9,21`. `l8_herbalist.gd:30-33` `pick` and `mechanism_transaction.gd:72`, `:104` (inside `occupy` and `retrieve`) are builders of the same kind.

**These builders stay as they are, for good.** They append to and erase from a fresh copy (`inventory.duplicate()`), never the live store, and they have their own tests. The source guard of commit 9 must not match them (section 4, commit 9).

### 2.4 The Cave: ten owners, no pack (way D, PROVEN)

`cave_walkthrough.gd:803-812` adds up: `collectible.saved_ids()` (`cave_collectible.gd:26`), `aloe.collected` (`cave_aloe.gd:80`), `stalagmites.collected` (`cave_stalagmite.gd:97`), `stone_manafoil.collected` (`cave_stone_manafoil.gd:124-127`, capacity checked against `carried_items()` at `:126`), the captain's grants (`cave_captain_items.gd:7-19`, from `cave_captain_state.gd:216` `grant_player` and the loot at `cave_captain_loot.gd:62-67`), and four guard loots (`cave_guard38_loot.gd:72-75`, `cave_guard39_loot.gd:97`, `cave_guard54_loot.gd:108`, `cave_guard_pair_loot.gd:110` used twice). Collect calls: `cave_walkthrough.gd:720-729`. The pack leaves the Cave as a list in `_completion_state()` `:814-818` and enters the Museum at `museum_walkthrough.gd:183` / `:204`.

### 2.5 Act 1 characters that read the give command themselves (way E, PROVEN)

| Reader | Hand-off |
|---|---|
| `jungle_kityara_state.gd:213` (`b[1]==1` -> effect "grant") | `jungle_kityara.gd:93` -> `jungle_walkthrough.gd:886-890` `_kityara_grant` (wired at `:347`) |
| `jungle_kelsrick_state.gd:181-182` (effect "grant_player", and the actor's own item list) | `jungle_kelsrick.gd:237`; the loot is taken at `jungle_kelsrick.gd:303-307` `collect_loot` |
| `cave_captain_state.gd:216-218` ("grant_player", "grant_actor") | `cave_captain.gd:153` |
| `jungle_dawn_state.gd:29`, `:219`; `hive_dawn20_state.gd:36`, `:241` (Dawn's own item list, `b[0]==3`) | stays inside Dawn's state; not a pack grant |
| `museum_broken_thohan.gd:67-90` `run_source_group` (group "grant") | appends at `:78` |
| Museum Prism and Hive Net of Exile sources (named in `native_script_host.gd:1694-1695` as the evidence that the dword is an item identity) | `museum_prism.gd:83`, `hive_net_exile.gd:78` |

### 2.6 Native give commands in the Act 2 host (way F)

Read from the generated `scripts/lol2/native_scripts/<AREA>.json` in my worktree (gitignored; generated on an earlier commit, so the counts are LIKELY for 742dcab and must be regenerated by the tool in commit 7).

- **876 commands** with opcode byte 3 and kind byte 1; every one is 12 bytes, target 0, bytes 9-11 zero.
- **All 876 dwords are identities of the 170 item definitions** (0 misses).
- Argument byte 8: **4 in 695, 1 in 129, 0 in 34, 3 in 17, 5 in 1**. Its meaning is UNKNOWN. The host comment (`native_script_host.gd:1692-1696`) says the callee was not entered. Evidence that it is not simply "give": L8 group 7364 holds 26 commands with arguments 0 and 3 for swords, armour, sap and aloe together (it reads like a kit or a test list), and L8 group 2358 names the Larkhon Vapors with argument 4 although the player mixes those himself.
- Per level (commands, distinct identity+argument pairs): L1 106/28, L3 56/16, L4 70/17, L5 18/12, L7 19/15, L8 61/24, L9 35/26, L10 61/12, L12 36/13, L13 22/14, L14 25/13, L16 292/33, L17 26/24, L19 30/15, L20 19/14. 276 pairs in all. The full list with definition names and group numbers is in `fable_lane/ITEM_GRANT_NATIVE_CENSUS.txt`.
- The signal carries `ref` = `target_ref(1, target)`, which is always `"0x01:0"` (the player), so **today the listener cannot tell which object or group asked** (`native_script_host.gd:1708`, `:425`).
- The task's own example: `prop:99` in L8 has one event, kind 4 (use), group 2530; that group's command is definition 119 "117-Amaranth sr", identity 77237872, argument 1. A second serum command sits in group 12234 with argument 4.
- Which of the 276 pairs already have a hand-written owner is **UNKNOWN** as a whole. Known from catalog grades (`act2_items_catalog.gd:64-90`): L19 horn (prop 222), L12 Kenneth's picture (prop 4), L8 control token (prop 102, group 4340), L8 vapors (actor 115), L13 altar awards (sources 174, 175, 326), L14 trial idols (groups 15150, 15210, 15378), L14 post shard (group 16904).

### 2.7 Functions that only remove (12 functions, 12 files; listed, see commit 10)

| File:lines | Function | Cap | Dup guard | History | Sync | Text | Journal | Equip/HUD |
|---|---|---|---|---|---|---|---|---|
| `jungle_walkthrough.gd:750` | `_consume_hand_item` | - | - | - | - | - | - | yes |
| `l14_chamber_voices.gd:99` | `offer` | - | - | - | yes | - | - | yes |
| `l16_greenhouse.gd:73` | `place_silverleaf` | - | - | - | yes | - | - | yes |
| `l16_sw_chips.gd:146` | `offer` | - | - | - | - | - | - | yes |
| `magic_shop_rooms.gd:202` | `_apply` | - | yes | - | - | - | - | yes |
| `monastery_rooms.gd:489,502` | `offer_item` | - | yes | - | - | - | - | - |
| `museum_scroll_state.gd:34` | `record_consumption` | - | - | - | - | - | - | - |
| `player_dragon_blood.gd:29` | `place` (`controller.carried().erase(id)`: a live-pack removal through the accessor; also appends the id to `saved.spent`) | - | yes | spent | - | - | - | - |
| `player_item_effects.gd:82` | `use` | - | yes | - | - | - | - | - |
| `thieves_den_rooms.gd:215` | `_apply` | - | yes | - | - | yes | yes | yes |
| `weapon_poison.gd:70` | `use` | - | yes | - | - | - | - | yes |
| `weapon_shop_rooms.gd:112` | `offer_item` | - | - | - | - | - | - | - |

Also PROVEN removals inside the lists above: `jungle_walkthrough.gd:750` `_consume_hand_item`, `museum_broken_thohan.gd:89-90`, `museum_key_locks_state.gd:51,79`, `museum_scroll_state.gd:34`, `l8_journey_state.gd:44`, `hive_rune_transaction.gd:59`.

Revision 1 listed `jungle_walkthrough.gd:504` `apply_save` and `:592` `apply_area_handoff` here. Both lines are `inventory.erase("fighting")`, a dictionary-key erase on a copied transport packet, not an item removal. They are loaders and are now in 2.8.

### 2.8 Loaders and validators (not grants; they must keep working unchanged)

| File:lines | Function | Cap | Dup guard | History | Sync | Text | Journal | Equip/HUD |
|---|---|---|---|---|---|---|---|---|
| `act2_items_catalog.gd:117` | `restore` | yes | - | yes | - | - | - | - |
| `area_world_items.gd:74` | `carried` | - | - | yes | - | - | - | - |
| `hive_review.gd:370,372` | `apply_area_handoff` | - | yes | - | - | - | - | yes |
| `jungle_source_pickups.gd:39` | `carried` | - | - | - | - | - | - | - |
| `jungle_walkthrough.gd:454` | `apply_inventory_handoff` (the pack assignment for the two loaders below) | - | yes | - | - | - | - | yes |
| `jungle_walkthrough.gd:504` | `apply_save` (erases the dictionary key "fighting" from a copied packet; no item is touched) | - | - | - | - | - | - | - |
| `jungle_walkthrough.gd:592` | `apply_area_handoff` (same key erase) | - | - | - | - | - | - | - |
| `jungle_world_items.gd:60` | `carried` | - | - | yes | - | - | - | - |
| `l9_pyre.gd:109,111` | `_unhandled_input` | - | - | - | - | yes | - | - |
| `museum_broken_thohan.gd:131` | `_carried` | - | - | - | - | - | - | - |
| `museum_walkthrough.gd:23` | `validate_cave_transfer` | - | yes | - | - | - | - | yes |
| `museum_walkthrough.gd:183,204` | `_ready` | - | yes | - | - | - | - | yes |
| `museum_walkthrough.gd:963` | `apply_save` | - | yes | - | - | yes | - | yes |

Save serializers and history normalizations (PROVEN; they write a **save copy or a history list**, never the live pack, and must not trip the guard):

| File:line | What it writes |
|---|---|
| `act2_map.gd:338`, `darker_jungle.gd:292`, `dragon_level.gd:175`, `act2_jungle_return.gd:49` | `inventory_state()`: `result.collected = result.collected.filter(...)` on the dictionary returned by `super.inventory_state()` |
| `area_world_items.gd:79`, `jungle_world_items.gd:53` | `history()`: `host.quest_state[key].collected = ....map(int)` (a world-item history of row numbers, not a pack) |
| `act2_items_catalog.gd:107-110` | `sync`: rebuilds `packet.carried` from the pack |
| `act2_world_items.gd:89` | `packet.carried = host.carried_collected.filter(...)` on a copied packet |

Save validators that bound the pack: `jungle_save.gd:24-25`, `museum_save.gd:35-36`, `walkthrough_save.gd:155-159` (Cave: a consumed id must have been picked up; it erases from a local validation copy), `act2_items_catalog.gd:95-106`. Transfer check: `player_continuity.gd:13-38`.

### 2.9 Act 2 history writes, site by site (PROVEN, read line by line)

`collected` here is `quest_state.act2_items.collected`. "Guard" = today's spelling: **always** (appends without looking) or **once** (appends only if absent). "Packet" = **in place** (mutates the live dictionary; fails if the key is missing), **copy** (deep copy, append, assign back; several start from `Items.initial()` when the key is missing), **builder** (a pure function returns the new packet and the owner assigns it).

| Site | Function | Guard | Packet | Order on the line(s) |
|---|---|---|---|---|
| `l12_citadel.gd:25` | `search_body` | always | in place | pack, history, sync |
| `l12_citadel.gd:40` | `throw_picture` | always | in place | state, pack assign, history (the charm) |
| `l12_frozen_bow.gd:56` | `take` | always | copy | history, assign, pack, sync |
| `l12_niche_armor.gd:43-44` | `take` | always | copy | history, assign, pack, sync, equip |
| `l13_altar.gd:39` | `enchant` | always | in place | pack assign, history, sync |
| `l13_altar.gd:48` | `take_stone` | always | in place | pack assign, history, sync |
| `l13_dawn_prison.gd:88` | `finish` | always | in place | pack assign, history, sync |
| `l14_hopper_platform.gd:78-79` | `take` | always | copy | pack, history, assign, sync |
| `l14_post_shard.gd:33-34` | `take` | always | copy | history, assign, pack, sync |
| `l14_trials.gd:64-65` | `take` | always | copy | history, assign, pack, sync |
| `l8_dawn.gd:26-28` | `interact` | always | copy | history, pack assign, packet assign |
| `l8_tribe.gd:100-101` | `offer_shaman` | always | copy | history, pack assign, packet assign, sync |
| `l8_larkhon.gd:56-57` | `mix` | always | copy | history, packet assign, pack assign, state |
| `act2_world_items.gd:86-90` | `take` | always (but `:82` refuses an id already carried) | copy | history, pack, `carried` rebuilt by hand, assign; no `sync` call |
| `l10_priest.gd:52` | `grant` (builder for `speak` `:43-45`) | always (but `:49` refuses when the urn is already in `collected`) | builder | - |
| `l10_silverleaf_harvest.gd:24-25` | `pick` (builder for `l10_silverleaf.gd:54-56`) | always | builder | owner: state, pack, packet, sync |
| `l16_dry_fountain.gd:156-158` | `take` | once | in place | pack, (line 157), history |
| `l16_fountain_ball.gd:85-86` | `take` | once | in place | pack, **sync, then history** |
| `l10_emperor.gd:66-70` | `interact` | once | copy | state, pack assign, history, packet assign |
| `l10_emperor.gd:126` | `collect_remains` | once | copy | same pattern |
| `l10_priest.gd:78` | `exchange_ashes` | once | copy | same pattern |
| `l9_pyre.gd:72-75` | `urn` | once | copy (from `Items.initial()` if missing) | state, pack assign, history, packet assign, sync |
| `l19_belial_horn.gd:62-69` | `take` | once (history and pack each guarded) | read, append, assign | history, pack |
| `l19_dawn_curse.gd:239-245` | `_grant_ruby` | once | read, append, assign | history, pack |

Whether an "always" site can fire twice for the same id was **not** proven site by site (most are behind a "taken" state check on the same function). The plan therefore does not rely on it: each site keeps its own spelling through the migration (section 3, step 5).

## 3. The contract

One new file, `scripts/lol2/item_grants.gd`, `extends RefCounted`, static functions only. No new node, no new saved state.

```
ItemGrants.pack(host) -> Array            # the live array: Hive dictionary's list, else carried_collected. Cave: carried_items() (a copy; read only)
ItemGrants.room(host, extra := 1) -> bool # pack size + extra <= Catalog.MAX_CARRIED
ItemGrants.known(host, id) -> bool        # Act 2 row valid, or Act 1 entry admitted in the host's scope
ItemGrants.grant(host, id, opts := {}) -> Dictionary   # {ok, reason}
ItemGrants.commit(host, new_pack: Array, opts := {}) -> Dictionary   # for way C
ItemGrants.remove(host, id) -> bool       # commit 10 only
ItemGrants.native(host, source: Dictionary) -> Dictionary   # way F, through the level table
```

`grant` does, in this order, and stops at the first refusal without changing anything:
1. **Catalog row.** `known(host, id)`; unknown id -> `{ok:false, reason:"unknown item"}` and a `push_error`. (Today an unknown id is appended silently and fails at the next save.)
2. **Duplicate.** If the id is already in the pack: `opts.duplicate` = "refuse" (default), "skip" (return ok without adding; today's `if id not in ...: append` sites).
3. **Capacity.** If `opts.cap` (default true) and not `room(host)`: refuse with `opts.full_text` (required whenever `cap` is true, so each site keeps its own wording). Sites that have no check today pass `cap:false` in their migration commit so behaviour does not change; the list of those sites is the input for question Q2.
4. **Append** to `pack(host)`.
5. **History.** `opts.history` has three values, and each migrated site passes the one that matches its row in table 2.9:
   - `"act2"`: append the base id to `quest_state.act2_items.collected` **unconditionally** (today's 14 "always" sites that are not builders);
   - `"act2_once"`: append **only if absent** (today's 8 "once" sites, and every native grant);
   - `"none"` (default): the API does not touch the packet. Used by Act 1 sites, by world-item owners (they keep writing their own history row), and by the two **builder** sites (`l10_priest.gd:43-45`, `l10_silverleaf.gd:54-56`), where the owner keeps assigning the packet its pure function returned.

   For both "act2" modes the API reads the packet with `host.quest_state.get("act2_items", Items.initial())`, deep-copies it, appends, and assigns it back. For the "in place" sites this is a **flagged normalization**: the end state is equal field by field, but a missing packet no longer raises an error there (it is created). Commit 0 pins the packet contents after each site, so a difference shows.
   `opts.sync` (default false): call `Items.sync(host)`. `opts.sync_first` (default false) calls it **before** the history write; only `l16_fountain_ball.gd:85-86` needs it. `sync` only rebuilds `carried` from the pack (`act2_items_catalog.gd:107-110`), so the order does not change the result as far as I can read, but the site keeps its order anyway.
6. **Text.** `opts.text` non-empty -> `host.save_feedback(text)` (Cave: `_save_feedback`).
7. **Journal.** `opts.note` non-empty -> `MyJournal.discover(host, note)`.
8. **HUD.** `opts.hud` true -> `interface_hud.refresh_equipment()` when the host has one.

`commit` is for the owners in 2.3: it takes the pack a transaction computed, checks every **added** id with step 1 and the total with `MAX_CARRIED`, assigns it (Hive: into the dictionary), and runs steps 5-8 for the added ids, or for the single id named in `opts.history_id` when the owner records a reward that is not a new pack entry. It does not re-judge the transaction's own rules.

The rule functions in 2.2 and the pure builders in 2.3 stay as they are (they have their own tests). Callers of the 2.2 rule functions pass `ItemGrants.pack(host)` instead of naming the store.

**Save.** Nothing new is saved. The pack is written where it is today (`inventory.collected` in each area's save, inside the slot file's `area_save` from Plan 3), the Act 2 packet in `quest_state.act2_items`, world-item histories in their owners' keys.

### 3.1 The native path

Three small additions, all additive:

1. `native_script_host.gd:1708`: the staged effect also carries `group`, `stream` and the command's `file_offset` (all three are already on the command and group dictionaries). A second signal `item_source(source: Dictionary)` is emitted next to `item_request` at `:1093`; the old signal and its three arguments stay.
2. `act2_progression.gd:447` `fire`: remember the `object_ref` and `event_kind` being fired (a stack, because groups can enqueue groups) and add them to the source before handing it on. `:211` keeps the log row and calls `ItemGrants.native(host, source)`.
3. A table per level, `scripts/lol2/item_grants/<AREA>.json`, one row per command, keyed by `file_offset`:
   `{file_offset, group, object, event, identity, definition, arg, action, id, text, note, grade}`.
   `action` is `"log"` (default for every row; today's behaviour), `"owner"` (a hand-written owner already gives this item; names the owner file) or `"grant"`.

For a `"grant"` row, `native` builds the pack id `act2:<AREA>:grant<file_offset>` and calls `grant` with `history:"act2_once"`, after refusing when the base id is already in `collected`. `act2_items_catalog.gd` `row()` gets one new prefix rule beside the Silverleaf and lichen ones (`:51-62`): for `act2:<AREA>:grant<N>` it looks N up in that level's table and returns a row built from the definition (name, label, icon, handler from `item_definitions.gd`, identity from the command). Because of that refusal, a script that fires twice cannot give the item twice, also after the player has used the item up.

A row may be set to `"grant"` only when all of these hold; the row's `grade` says which evidence was used:
- the group is reached by a player event on a visible object (kind 4 use, or a region entry) and not only from another group;
- no hand-written owner gives the same item at the same place (search the owner files for the identity and the definition);
- the book or the longplay shows the player receiving that item there.

The argument byte stays undecoded in this task (question Q3). No rule may read meaning into it.

## 4. Migration: eleven commits, each one green

Reserve the next free ledger and registry numbers on the board before commit 0. Same launcher limits as before.

**Commit 0. Pin today.** No production change.
- `tests/item_grant_census_test.gd`: a source scan that pins the lists of section 2 as a fixture (`tests/fixtures/item_grant_census_742dcab.json`: file, function, kind; kinds: add, rule, transaction, builder, cave, reader, remove, loader, serializer, validator; for the 24 rows of table 2.9 also guard and packet spelling). It fails when a writer appears or disappears, so every later commit must update the fixture on purpose.
- `tests/item_grant_site_fixture_test.gd`: for one site of each way A-E in each host family (Museum prism, Museum aloe rule, Jungle world item, Kityara's knife, Hive wax, Dark Halls loot, L8 tree slot, L10 priest urn, L12 frozen bow, L14 trials idol, L16 fountain ball, L19 horn, Cave guard 38 loot), record before and after: pack, Act 2 packet, the owner's state, the feedback text, the Journal list. Also the refusal with a pack of 64 where the site has a check, and the success with 64 where it has none.
- `tests/item_grant_history_spelling_test.gd`: for every row of table 2.9, the packet after the grant; and for each "always" site that can be reached twice from a test (call the function again on a state where its own guard lets it through, if one exists), the packet after the second call. This is what makes "act2" against "act2_once" a tested difference and not a guess.
- A save written by each host after those grants, kept as bytes, for commit 9.

**Commit 1. The module, unused.** `item_grants.gd` with `pack`, `room`, `known`, `grant`, `commit`. Unit test `tests/item_grants_test.gd` on a bare host stub for each of the four stores: every step of 3, each option, refusals change nothing.

**Commit 2. Act 2/3 owners that append (way A).** The `l10_`-`l19_` and `l8_`/`l9_` rows of table 2.1 that append directly: `l12_citadel.gd:25`, `l12_frozen_bow.gd:56`, `l12_niche_armor.gd:43-44`, `l14_hopper_platform.gd:78-79`, `l14_post_shard.gd:33-34`, `l14_trials.gd:64-65`, `l16_dry_fountain.gd:156-158`, `l16_fountain_ball.gd:85-86`, `l19_belial_horn.gd:65-69`, `l19_dawn_curse.gd:242-245`. Each keeps its own state write and passes the history mode of its row in table 2.9 (`"act2"` for the L12 and L14 sites, `"act2_once"` for the L16 and L19 sites, `sync_first` for the fountain ball), its exact text, and `cap:false` where it has no check today.

**Commit 3. World-item pickups.** `act2_world_items.gd:81-90`, `area_world_items.gd:163-174`, `jungle_world_items.gd:92-101`, `hive_world_items.gd:88-94`, `jungle_river_dam.gd:353-357`, `jungle_source_pickups.gd:63-68`, `dark_halls_loot.gd:50-61`, `dark_halls_rix.gd:44-54`, `jungle_kelsrick.gd:303-307`. Their own history rows stay. `act2_world_items.gd` passes `history:"act2"` and keeps its own `packet.carried` line (it does not call `sync`).

**Commit 4. Museum.** Host functions `museum_walkthrough.gd:541`, `:1039`, `:1051`; owners `museum_blood_loot.gd:71`, `museum_crystal.gd:60`, `museum_dragon_heart.gd:104`, `museum_lightning_crystal.gd:32`, `museum_prism.gd:83`, `museum_broken_thohan.gd:78`; and the way-B callers `museum_aloe.gd:54`, `museum_scrolls.gd:54`, `museum_ivory.gd:84`, `museum_long_arm.gd:134`, `museum_key_locks.gd:367-369` (pass `ItemGrants.pack(host)`).

**Commit 5. Transactions (way C).** The 31 functions of table 2.3 call `ItemGrants.commit(host, result.inventory, {...})` in place of the assignment; the hand-written `act2_items.collected.append` beside them (`l13_altar.gd:39,48`, `l13_dawn_prison.gd:88`, `l12_citadel.gd:40`, `l10_emperor.gd:69,126`, `l10_priest.gd:78`, `l9_pyre.gd:74`, `l8_dawn.gd:27`, `l8_larkhon.gd:56`, `l8_tribe.gd:100`) moves into the history option with the mode of table 2.9: `"act2"` for `l13_altar.gd:39,48`, `l13_dawn_prison.gd:88`, `l12_citadel.gd:40`, `l8_dawn.gd:27`, `l8_larkhon.gd:56`, `l8_tribe.gd:100`; `"act2_once"` for `l10_emperor.gd:69,126`, `l10_priest.gd:78`, `l9_pyre.gd:74`; `"none"` for the two builder sites, which keep their packet assignment. The pure builders are not edited. `player_item_controller.gd:130-131` (item use writes back a pack) is in this commit too.

**Commit 6. Hive, Act 1 shops and characters.** `hive_wax.gd:35`, `hive_net_exile.gd:75-78`, `hive_reaver_amber.gd:214`, `hive_flute_floor.gd:213-214`, `hive_rune_entry.gd:246`, `:259`, `:278`; `jungle_walkthrough.gd:886-890`; `jungle_beehives.gd:95`, `jungle_harvest.gd:125`; `magic_shop_rooms.gd:214-221`, `monastery_rooms.gd:225-233`, `:411-417`, `:463-468`, `thieves_den_rooms.gd:235-241`, `weapon_shop_rooms.gd:141`; `l8_herbalist.gd:32`.

**Commit 7. Native table tool and tables, all rows "log".** `tools/build_item_grant_tables.py` reads the generated native script files and the definitions and writes the fifteen tables with `object` and `event` filled from the objects' event lists. Test: counts per level equal the tool's own summary; every identity resolves; with all rows "log" a fired group changes nothing in the pack (same as today). Mark rows `"owner"` for the known owners in 2.6.

**Commit 8. Native path live for four rows.** Host signal, progression context, `ItemGrants.native`, the catalog prefix rule. Switch on L8 `prop:99` (group 2530, serum) and three more rows that pass the three conditions of 3.1. Candidates to check first, from the census: L8 "112-Lamplt eggs" (argument 1, groups 6442-6882; check for an existing egg owner), L8 "113-Brook flou" (argument 4, groups 8762-9226), and one argument-1 row in L10 or L9 that the book confirms. Each gets a rendered real-input test: walk to the object, press E, the item is in the pack, the Journal or screen says so, save, reload, press E again, still one copy.

**Commit 9. Source guard and old saves.** `tests/item_grant_source_guard_test.gd` matches **writes to the live store only**, by three rules:
1. *Direct.* A line where `carried_collected`, `carried_inventory.collected` (or `carried_inventory =`), `carried()` or `get_parent().carried_collected` is followed by `.append`, `.push_back`, `.insert`, `.erase`, `.remove_at`, `.assign`, `.clear`, `.append_array`, `=` or `+=`. (Erase and its relatives are only enforced after commit 10; before that they are reported, not failed.)
2. *Alias.* Inside one function, a local bound to a live store without `.duplicate(` (`var carried = get_parent().carried_collected`, `var collected: Array = host.carried_inventory.collected`) and then mutated by one of those calls.
3. *Argument.* A call that passes a live store, or such an alias, as an argument to a function that is not on the rule-function list.

Allowed by name (file and function): `item_grants.gd`; the loaders of 2.8; the rule functions of 2.2 as callees for rule 3; the Cave owners of 2.4 (they write their own state, not a pack, and are listed so the census test keeps them known).

**Not matched, by construction**, and the test asserts each of these still exists and is clean so the rule cannot drift into them: the pure builders (`l10_emperor_state.gd:67`, `l13_altar_state.gd:36`, `l13_dawn_release.gd:35`, `l10_silverleaf_harvest.gd:25`, `l10_priest.gd:53`, `l8_journey_state.gd:52,71`, `l8_herbalist.gd:32`, the state files named under table 2.3), `mechanism_transaction.gd:72,104`, the four `inventory_state()` serializers (`act2_map.gd:338`, `darker_jungle.gd:292`, `dragon_level.gd:175`, `act2_jungle_return.gd:49`), the world-item history normalizations (`area_world_items.gd:79`, `jungle_world_items.gd:53`), `act2_world_items.gd:89`, `walkthrough_save.gd:155-159`, and the two key erases `jungle_walkthrough.gd:504,592`. All of them write a duplicate, a result, a save dictionary or a history list.

Mutation probes, one per rule: a direct append in a throwaway owner; an alias append; a live pack passed to an unlisted function. Each must fail the test. A fourth probe adds `x.duplicate().append(id)` in a throwaway builder and must **pass**. Old-save test: every save from commit 0 and the fifteen golden saves from Plan 3 load, and the pack, packet and histories are equal field by field.

**Commit 10. Removals (optional in this task; say on the board if it is left for I-01).** `ItemGrants.remove` and the 12 functions of 2.7 (among them `player_dragon_blood.gd:29`, which goes through `controller.carried()`) plus the removals listed under it. No behaviour change; the guard then covers erase as well.

Not in this task: the Cave's derived pack (it becomes a real pack with the unified item core, I-01), the `hand_item` writers, one refusal text, one capacity rule.

## 5. Old saves

- No key is added, renamed or removed in any area save, in the Act 2 packet or in the slot file. Versions do not change.
- Native grant ids (`act2:<AREA>:grant<N>`) are new **values** inside existing lists. A save made after commit 8 that holds one will not validate on a build before commit 8; that is the normal direction and needs no migration. Saves from before load unchanged.
- The table files are data shipped with the build. If a table row is later changed from "grant" back to "log", a save holding that id must still load: the catalog rule builds the row from the table whatever the `action` is.

## 6. Tests (summary)

| Test | Kind | Proves |
|---|---|---|
| `item_grant_census_test` | source scan | the writer lists of section 2 are complete and stay known |
| `item_grant_site_fixture_test` | scene, one site per way and host family | pack, history, text, Journal, refusal identical before and after each commit |
| `item_grants_test` | unit | each step and option of the contract; refusals change nothing |
| existing owner tests (the 85 files that write the pack, the 295 that read it) | unchanged | the stores kept their names and shape |
| four native grant tests | rendered, real E | the item arrives once, survives save and reload, is not given twice |
| `item_grant_history_spelling_test` | scene, the 24 rows of table 2.9 | each site's history spelling (always or once) is unchanged |
| `item_grant_source_guard_test` | source scan, three rules, four mutation probes | nothing outside the allow-list writes the **live** pack; builders and serializers stay free |
| old-save test | bytes from commit 0 and Plan 3's goldens | saves load to the same pack, packet and histories |

## 7. Risks

1. **The argument byte.** If 4 means "the player must hold this" or "take this away", switching such a row to "grant" invents an item. The default "log" and the three conditions are the guard; nothing is switched on by a rule.
2. **`cap:false` sites.** Keeping today's missing checks means a pack can pass 64 through those sites and then fail the save validator (`jungle_save.gd:25`, `museum_save.gd:36`). That is today's behaviour; the plan makes the list visible, it does not cure it.
3. **Order of side effects.** Several owners write their own state between the append and the history write, and `restore()` or `present()` runs after. Keep each owner's order; the API call replaces only the append and the history lines.
4. **Aliases.** Shops and Hive owners hold the pack in a local variable. `pack(host)` must return the live array, never a copy, or their later reads go stale. For the Hive, `hive_flute_floor.gd:214` uses `assign` on the alias for that reason.
5. **Act 2 history rule.** `validate` refuses a carried id whose base id is not in `collected`. An owner that today appends to the pack without history (a "-" under History in table 2.1 among `l1x_` files) only works because its id is in `legacy_equipment` (`act2_items_catalog.gd:19`) or because `sync` filters it. Check each such row before passing `history:"act2"`.
6. **Machine-derived columns.** The side-effect columns come from a text search; a "yes" can be a match in a comment or another branch. Read each function when migrating it.

## 8. Open questions

- **Q1 (owner): one refusal text?** Four exist today. Not changed here.
- **Q2 (owner or lead): should every grant respect the 64 limit?** The `cap:false` list after commit 6 is the exact set of exceptions.
- **Q3 (Grok): what is byte 8 of the give command?** Enter the callee the host comment names (0x95B68 and vtable slot +0x6C). Until then only hand-checked rows are live.
- **Q4 (lead): commit 10 here or with I-01?**

## 9. What I could not confirm

- Nothing was run. This is a code and data reading on 742dcab.
- The native counts come from generated files in my worktree made on an earlier commit; regenerate before trusting the numbers.
- The side-effect columns of the tables (see 2 and risk 6).
- Which of the 276 native pairs already have a hand-written owner, beyond the eleven named in 2.6.
- The 25 files that write `hand_item` and whether an item can sit in the hand without being in the pack.
- Whether any test fixture or developer start file builds a pack with ids no catalog admits (the scripts hold no literal kit; the start files are saves).
- Whether another rule function appends to a pack it receives under a parameter name I did not search (the Ancient Stone was found only by the second sweep).
- Whether dynamic writes exist that a text search cannot see (`set("carried_collected", ...)` was searched and not found; `call`-by-name was not searched).

## 10. Revision 2: what changed after Kimi's audit (K95)

All four gaps were checked against the source at 742dcab and are right.

- **A. Source guard.** As written it would have failed on the pure builders, the transaction kit and the save serializers that the census itself keeps. The guard now matches writes to the live store only (three rules, commit 9), with the builders and serializers named as must-stay-clean and a probe that proves a builder passes. Section 2.8 lists the serializers.
- **B. History mode.** One "append if absent" mode would have changed saved data at the 16 sites that append unconditionally. There are now two modes, `"act2"` and `"act2_once"`, table 2.9 records each site's spelling (read line by line), the builder sites keep their own packet, and commit 0 gets a test for it. The in-place against copy difference is named as a flagged normalization.
- **C. Dragon blood.** `player_dragon_blood.gd:29` is a live-pack removal through `controller.carried()`. It moved from 2.1 to 2.7 and is in commit 10 and under guard rule 1.
- **D. Two loaders.** `jungle_walkthrough.gd:504`, `:592` erase a dictionary key, not an item. They moved from 2.7 to 2.8.

Counts after the moves: 62 functions in 53 files add; 12 functions in 12 files only remove.

Still not confirmed beyond section 9: whether any "always" site can in fact fire twice (the plan no longer depends on it).

PLAN READY
