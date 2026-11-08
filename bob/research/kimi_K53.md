# Kimi K53 — pre-merge review: grok BJ07 + fable BJ08 (r19)

• ## Findings

**Grok BJ07 — `BJ07_l12_return_l14.patch` (tests only)**

1. Patch is 100% test code: 10 parent earned tests refactored to `input_path()`/`input_ready()`/`pass_line()` hooks (parents keep their sha-pinned qualified snapshots, e.g. patch line 25), and 11 new `*_chain_earned_test.gd` subclasses that only swap the input to the previous step's earned save (`input_ready` = `FileAccess.file_exists`, same pattern as the already-merged BJ01/BJ06 chains, cf. `tests/registry/l13_exit_lock_chain_earned_test.json`). No gameplay/progression change; no ledger piece, consistent with the tests-only precedent (BJ01, commit 7e5d5ec).
2. The relay order matches the BJ07 task leg exactly: 963 exit_cave → 964 river_niche → 965 niche_armor → 966 river_return → 967 crevasse → 968 frozen_bow → 969 logs_approach → 970 return_logs → 971 gulch_return → 972 l8_river_return → 973 l8_temple_door (patch lines 533, 599, 577, 610, 522, 544, 566, 588, 555, 621, 632). Each chain test's `input_path()` is the save the previous step writes — verified link by link.
3. One change is not a pure refactor: `tests/l12_river_return_earned_test.gd` boarding (patch lines 367–411). The single hard attempt (`check(scene.request_jump(),…)` + "first landing is the moving raft") becomes a 4-attempt retry loop that tolerates jump refusals and missed boards; and the ride aim is clamped to 100 units inside the deck with a comment explaining boat 50's deck ends at local z +137 (patch line 416).
4. Applies cleanly to r19-work (`git apply --check` passes); the pinned shas it references (`tmp/l12_river_return_qualified_save.json` 193c8f8e…, `tmp/l13_exit_lock_qualified_save.json` b6cd377b…) match the files in the base.

**Fable BJ08 — `bj08-temple-chain_e3b2870.patch` (2 commits)**

5. Commit 1 adds the three-sitting chain (`l14_temple_chain_a/b/c_test.gd`, orders 963/964/965 — patch lines 795, 802, 809) plus `atlas_readable_l14_test.gd`; commit 2 adds the `L14_HT` Atlas table in `scripts/lol2/atlas_places.gd` (patch line 858: 17 places, 2 exits, 4 Journal plot markers), ledger piece `docs/deviations/0357-row-2026-11-08-atlas-readable-l14.md` + the inline DEVIATIONS.md row, test hardening, and renumbers the atlas test 947→966 (patch line 962; 947 was already taken by `l13_upper_ruloi_chain` in r19-work).
6. Chain A pins `tmp/l14_temple_arrival_qualified_save.json` sha 761850f6… (patch line 196) — the file exists in r19-work and the sha matches exactly. B reads A's output, C reads B's; 963<964<965 preserves that. All 17 `tests/fixtures/l14_*.json` the walks read already exist in the base. Parents exist (`l12_logs_approach_earned_test.gd`, `l14_ledge_maze_earned_test.gd` — the latter supplies `jump_gap`).
7. STORY-066: confirmed hosted per K52 and NOTES (`scripts/lol2/l14_chamber_voices.gd`, qualified at registry 748); the backlog card "todo" is stale — a backlog/doc flip for the lead, no code change. Part C walks it end-to-end to the native L16 arrival 1 and even pins the F5-refusal message inside the voices overlay (patch line 764).
8. Only production-code touch is `atlas_places.gd` data — presentation/modern aid, declared as such in the DEVIATIONS row. No gameplay/progression change. Ledger 0357 is the next free number (r19-work max is 0356); filename follows the NNNN-row-DATE-slug rule, one row.
9. Test accommodations, all with stated reasons: the entry stair-lip auto-hop (NOTES finding 2; the parent `walk()` helper in `tests/l12_logs_approach_earned_test.gd:18-20` already carries the checked version) — the underlying map/collision lip is deferred as Fable's follow-up, not fixed; the chalice click is E-substituted headless with the rendered `l14_chamber_voices_earned_test` covering the click (NOTES finding 4); `combat_tick_budget()->18000` matches the existing `tests/l14_tilt_earned_test.gd:3`.
10. Applies cleanly to r19-work. NOTES.md line 15 says "registry 944-946" — stale vs the patch's 963–966 (944-946 are BJ06's L13 chain tests in the base); cosmetic only.

## Problems

1. **Registry collisions between the patches at 963, 964, 965, 966.** r19-work is free from 963 up (max 962), but Grok claims 963–973 and Fable claims 963–966 for different tests (Grok 963 = `l12_exit_cave_chain`, Fable 963 = `l14_temple_chain_a`; … Grok 966 = `l12_river_return_chain`, Fable 966 = `atlas_readable_l14`). The no-collide rule (Grok's relay depends on strict order) requires renumbering one set before merge. Neither patch alone collides with r19-work.
2. **Grok loosened a qualified parent test without a stated reason** (rule: loosen only with a stated reason). The `l12_river_return_earned_test.gd` boarding retry loop (patch lines 389–411) lets up to 3 jump refusals/missed boards pass where the old test failed on the first. The accompanying deck-edge aim clamp *is* justified in-comment (patch line 416) and is a correctness fix, but the retry itself has no reason in the patch, commit message, or ledger. Lead should ask Grok for the reason (likely raft-timing flake at 4× time scale) or accept explicitly.
3. Minor: Fable's atlas-test auto-hop calls `scene.request_jump()` unchecked (patch line 933), where the parent helper does `check(scene.request_jump(),…)` — a small asymmetry, reason for hopping itself is stated.
4. Minor: stale "registry 944-946" in `bj08_20261108/NOTES.md:15`.

## Merge order and verdict

**Order: Grok BJ07 first, then Fable BJ08.** Task order and state flow demand it (BJ07's temple-door leg earns the L14 arrival BJ08 starts from), and it lets Grok keep 963–973 untouched. Fable then needs a one-line renumber of four registry files: `l14_temple_chain_a` 963→974, `l14_temple_chain_b` 964→975, `l14_temple_chain_c` 965→976, `atlas_readable_l14` 966→977 — keeping A<B<C after Grok's 973 temple-door step, which is exactly the walk sequence. The two patches share no files, so the renumber is the only conflict resolution needed; ledger 0357 stands.

**Verdict: merge both after the Fable renumber (974–977) and a stated reason (or lead acceptance) for Grok's river-return boarding retry.** Both patches are task-faithful earned walks — player-style movement, quicksave/reload/re-save checkpoints, no-seeds/no-recovery assertions, sha-pinned qualified inputs verified against the base — with no gameplay or progression changes; the only production delta is Fable's presentation-only Atlas table with a correct ledger row. Follow-ups for the board, not merge blockers: the L14 entry stair-lip map fix (Fable), and closing the stale STORY-066 backlog card (lead).

