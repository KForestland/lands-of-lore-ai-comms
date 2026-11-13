# R111. F-08 corrections at 4ebbd30

Read-only. Branch `sol/item-grants-foundation-20261112`, worktree `~/opus_work/lol2_sol_item_grants`, head `4ebbd304691df0f9a068f9bfc5f6333de7dadb8c`. Base `20c7797`. The range is `8721e40`, `b5af917`, and the correction `4ebbd30`. Compared with `grok_research/review_R108_sol_f08_commits_0_1.md` and `fable_lane/ITEM_GRANT_PLAN.md` section 13. The Python census checker returned 0 failures on this tree, and its 14 probes passed in 53.0 seconds. The Godot gates were not relaunched.

## Duplicate skip, and the two sync rules

Section 13 and R108 major 1 are closed. `grant` sets `added` false when `duplicate` is `"skip"` and does not return there. `_effects` then runs history, sync, text, Journal, and HUD. The result is `{"ok":true,"added":false}`. A refusal dictionary also carries `added:false`. `tests/item_grants_test.gd` pins the knife-style skip (text and HUD, pack unchanged) and the horn-style skip (history and sync on a full pack of 64, text, Journal, and HUD).

`sync:true` with `history:"none"` checks `quest_state` before any write. A missing packet is accepted through `Items.initial()`, and `Items.sync` rebuilds `carried` from the pack. The unit test grants an Act 2 id that way and expects `collected` empty and `carried` holding that id. `sync_first` without `sync` returns `"sync_first needs sync"` before a write. The two sync orders now expect different packets: an empty `collected` when sync runs first, and the new base id when history runs first.

## Commit 0's three pins

R108 major 2 and the last paragraph of section 13 are closed. No commit after `4ebbd30` exists, so no migration commit is on the branch.

`tests/item_grant_site_fixture_test.gd` runs the 13 section-4 sites, each as `normal` and `full64` (26 cases). The normal case must change the observation. Kityara's knife and the Hive wax still reach 65. The Cave guard loot stays the derived pack. The other full packs stay unchanged. The frozen file is `tests/fixtures/item_grant_site_baseline_20c7797.json`. Each observation has pack, quests, owner, messages, Journal, HUD refreshes, and sync packets, plus the repeat. The test asserts the whole document.

`tests/item_grant_history_spelling_test.gd` requires the census history guards to equal the 24 rows of table 2.9. The frozen baseline has all 24. Each of the 16 `always` rows has exactly one of `second_call` or `second_call_blocked`, and in this baseline every one is the blocked form: the second call is refused and the packet is unchanged, with the guard line cited.

`tests/item_grant_host_save_test.gd` boots the production scene, loads each of the 15 golden area saves, calls the original grant methods, writes with `_quicksave_unrecorded`, and loads that file in a fresh scene. The manifest's 12 post-grant areas cover all 13 named sites: Museum prism and aloe on L3, Jungle world item and Kityara on L4, Hive wax on L5, Dark Halls loot on L7, the L8 tree slot, the L10 priest urn, the L12 bow, the L14 idol, the L16 fountain ball, the L19 horn, and Cave guard 38 on L1. L9's pyre urn and L16's dry fountain are extra rows in those saves. Fresh loaded records also cover the 15 round-trips, Cave v1, and the five Plan 1 witnesses, 36 packets in all. Comparison is the loaded record and, for the post-grant files, the writer bytes.

A missed assertion stops the Godot test. The unit test calls `quit(1)` when a check fails.

## The census

R108 major 3 is closed. `operation_sites` treats a dictionary value as a live pack, so `{"collected":host.carried_collected}` passed onward is a site. The live fixture records `museum_long_arm.gd::use` at `State.take(state, inventory)` and `jungle_beehives.gd::use` at `State.harvest(state, id, inventory)`. Those are the wrapped-pack calls. `pop_at`, `resize`, `call`, and `call_deferred` are scanned. The probe list emits a site for each of those spellings, including an arbitrary parameter name.

The probes that must fail are present and passed here: a removed `append` in `museum_prism.gd`, a changed string in `l12_frozen_bow.gd` (the pinned hash), a builder reclassified as `add`, a changed golden byte, a changed runtime baseline, and a module reference by relative path, split string, or scene. The live `check()` on this worktree returned no failures: 361 functions, 24 history rows, 25 builders forced to kind `builder`.

## The smaller R108 notes

`player_dragon_blood.gd::place` is kind `remove`. Kind `serializer` is used on 8 rows, including `act2_map.gd::inventory_state`, the other three `inventory_state` functions, `act2_items_catalog.gd::sync`, and `walkthrough_save.gd::migrate_loaded`. The `l9_pyre.gd` fixture row is `urn` only. `_unhandled_input` is not a row. The Museum stub's `validate_cave_transfer` is static. Hive `commit` assigns `carried_inventory.collected` to the new array. The unit test expects the previous alias to stay empty and the dictionary's other fields to stay. The unused-module scan reads `scripts` and `scenes`, and it follows a preload split across string pieces.

`plan_anchors` are stored on 188 rows and are not compared. The ledger calls them informational. A semantic hash still covers 80 of the 361 functions, so a comment-only edit in one of the other functions does not fail. Ledger `0635` is written in spaced sentences. Rows `0633` and `0634` are absent because this branch's base is `20c7797`.

## Production

Against `20c7797`, the only new file under `scripts` is `scripts/lol2/item_grants.gd`. No scene references it. The unused-module scan reported no owner reference. `tools/regression_source.py` adds the two census tools to the source snapshot. Saves, native grants, and owner call sites are unchanged.

VERDICT: MERGE
