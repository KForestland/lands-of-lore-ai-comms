REVIEW R108: Sol F-08 commits 0 and 1 (8721e40, b5af917 on 20c7797), read-only

BLOCKER
None.

MAJOR
1. scripts/lol2/item_grants.gd:86-88: `duplicate:"skip"` returns before history, sync, text, Journal and HUD, and the result has no "added" field. Today's skip sites still run their effects: jungle_walkthrough.gd:889-890 refreshes the HUD whether or not the knife was appended; l19_belial_horn.gd:63-70 writes history-if-absent and syncs even when the horn is already in the pack. Migrating them with "skip" changes behaviour (commits 2 and 6). tests/item_grants_test.gd:90 pins the early return. Fix: run steps 5-8 on skip, or return `added` so the owner can.
2. Commit 0 is partial. Plan section 4 also asks for item_grant_site_fixture_test, item_grant_history_spelling_test and a save per host plus the loaded-state record. None exists; ledger 0635 says "REQUIRED before migration". The census pins source text only; nothing pins pack, packet, text or Journal per site. Must land before commit 2.
3. tools/check_item_grant_census.py:147-156: a live pack wrapped in a dictionary literal and handed to a rule function is invisible (probed in memory: `var p := {"collected":host.carried_collected}` then `State.take(state, p)` gives no site). That is the existing way-B idiom (museum_long_arm.gd:134, jungle_beehives.gd:95, museum_key_locks.gd). Also unseen: `pop_at`, `resize` (MUTATORS :19-21), a parameter with an unlisted name, call-by-name. A new writer of these forms passes the census.

MINOR
- Fixture: player_dragon_blood.gd::place is kind "add" (anchor "2.1:29") but its only site is an erase; the plan puts it in 2.7 (remove). Kind "serializer" is never used; act2_map inventory_state, act2_items_catalog sync and walkthrough_save migrate_loaded are "loader". l9_pyre.gd::_unhandled_input has a row although plan 2.8 says none.
- Brittleness: sites are whitespace-free token strings, sorted per function, so line shifts, comments and reordering inside a function pass; a new, removed, duplicated or moved-between-functions site fails (:191-192). 80 rows also carry a whole-function hash, so any edit inside those functions fails (intended for the 24 history rows). `plan_anchors` are not checked.
- tools/test_item_grant_census.py:81-86: three probes, all "writer appears". No probe for a removed writer, changed hash, builder reclassified, golden change or module reference.
- Unused-module guard (:202-207) matches only the exact res:// string in scripts/lol2/*.gd.
- item_grants.gd:55: `sync:true` with history "none" does not check quest_state; Items.sync would fail after the append. :62: `sync_first` without `sync` is silently ignored.
- item_grants.gd:112: Hive commit uses `assign`; today's only Hive way-C write replaces the array (player_item_controller.gd:130). Same value, different aliasing; check at commit 5.
- Test: Museum stub's validate_cave_transfer is an instance method, the real one is static (museum_walkthrough.gd:15). Lines 103-107 assert the same end state for both sync orders, so sync_first cannot fail. "Act2 history needs quest_state" and null host are untested.
- Ledger row has run-together words; 0633/0634 absent from the tree.

Sound
- Only production file added: scripts/lol2/item_grants.gd. No script or scene references it (grep). regression_source.py only adds the two tools to the source snapshot; registry entries are new; nothing loosened.
- Fixture is current: I ran the tool's scan read-only on the tree at b5af917; 220 functions with sites, zero differences; build_base records 20c7797 (742dcab is the plan's file name).
- All 12 named sites are present with sensible kinds (except dragon blood); 24 history rows match table 2.9; the builders of check 1 are kind "builder" and enforced by must_remain_builders.
- Module: pack is live for Museum, Jungle and Hive (the list inside the dictionary); Cave gets a copy and grant/commit refuse with push_error (pinned). Order known, duplicate, options, cap, append, effects; all checks precede any write. History modes, base id, deep copy with Items.initial() fallback, cap defaults (grant true with required full_text, commit false), history_id and the written scope map follow the plan. Extra refusals (unknown note, invalid history id, option typos) and "allow" are improvements.
- Unit test uses stubs with the real field names; assertions compare full snapshots and can fail.

Not judged without running
GDScript parsing of module and test; has_method on the static Museum function; whether the test's act2 ids are valid; the Godot wrapper's OS.execute; the registry audit_sha256 (no validator in this worktree).

VERDICT: MERGE AFTER FIXES
