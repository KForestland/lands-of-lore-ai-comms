# Kimi K69 — pre-merge review: grok BK08d, BK07b, BK10, BK09b, BK08e

## Findings (numbered, with file:line)
## Problems (numbered)
## Merge order and verdict

Findings to include:
1. Hashes + apply checks (all 5 clean on 5b769dc; both orders for the shared file; ORDER.md order works as a stack).
2. Sol Task 2 did not touch act2_progression.gd (file list) — the only shared file is between BK07b and BK08e.
3. BK08d: real clicks via Input.parse_input_event; gate `_player_click()` headless allowance documented in row 0385 + header comment; adapter logged (15/16 pairing). Ledger 0385 free.
4. BK07b: fixes K63 problems 3+4 exactly as prescribed; row 0379 amendment also fixes K63 problem 2 wording; test adds fresh-boot claim + physics-ray deck checks; adapter logged row 0388.
5. BK10: pins verified internally consistent (sha/index/key/frames); tools deps exist; ogv gitignored via assets/lol2/generated/; registry 1018 free, schema matches; adapters honest; hw01/bb_brth stay unplayed (comment-only).
6. BK09b: receivers layer 4/mask 7 = L19 switch ray; record_shot shared by E and click paths; tests now keep player on the lip with real clicks (removes old teleports-to-pillars); adapters logged row 0390. Note: record_shot not lip-gated in code.
7. BK08e death caller: NOT generic — gated to L20_BB 47/48 (act2_creatures.gd:134-140 of patch); fire_event kind-6 matcher requires caller_byte match (native_script_host.gd:707-711). Sweep: 10 levels have actor kind-6 caller-0x0B records (list), none can fire because the hook is area+id gated — no risk to other-level earned walks from this hook. Within L20, actor:46's caller-0x0B record (group 12398, op9 arm 0x15 on prop:4) remains unfired — residual gap.
8. Group bytes verified: 12732/12898/9278/9384 contents match K67 and rows; GRATE_OPCODE_22 matches group 12732's command exactly; stub refuses all other opcode-22 (verdicts unchanged for the 53 other L20 opcode-22 groups); no test asserts old refusal text.
9. Open-bit collision drop: mechanism correct (object_state_changed → _on_field → _apply_open_bit; arm 0x0E stages bit_0x15_0x80 at native_script_host.gd:~1502; initial build call is a no-op since fields only come from staged writes), logged as adapter in row 0391 — BUT generic, not scoped to 50/51 (see Problems).
10. Physics sync in advance_movers (force_update_transform + PhysicsServer3D body_set_state) is generic for all mover bodies in all act2 levels — improves same-step accuracy; low risk, untested outside L20.
11. Ledger 484 PASS at HEAD; new pieces 0385/0388-0391 free; 0379 amendment base line matches HEAD. Registry max order is 1033 (Sol 1020-1033), not 1073 — 1018 free; no dups introduced.
12. Tests real input / teleports: BK08d + BK09b tests now inject real InputEventMouseButton and keep the player in place; BK08e's new segments use cross() with real move_grounded walking and negative blocked-checks, but the guardian kill teleports the player and calls pop.strike()/strike_remaining directly, and hammer() calls progression.strike_ref directly — consistent with the file's pre-existing style, not the new real-click standard. BK07b's fresh_boot places the player via the save (earned earlier in the same run) — fine.
13. Board lines (COORDINATION.txt:4945,4966,4969,4971,4978) match patches (hashes, claims, named runs). ORDER.md entries 31-35 consistent with verified apply behavior.

Problems:
1. BK08e's open-bit collision drop is generic, not scoped to 50/51, and row 0391 doesn't disclose cross-level reach. Live hosted paths that already set bit_0x15_0x80 on faced movables with NO travel (collision drops while the mesh stays): L14 movable 85/86/87 (kind-4 E-use, groups 20436/20524/20660), L16 movable 66 (kind-4 E-use, groups 49134-49324, no predicate), L19 movables 61/62 (region 1903 entry group 1082, no predicate — region entries hosted since BK07), L9 movable 58 (kind-4 E-use group 17512) and 55/59 (prop:949 caller-20 enqueue group 5094). Plus with-travel cases (L19 57/58, 63/73; L16 99/100; L14 58-63/80) which are likely benign. Whether each no-travel case is a native-faithful fix or a walk-through-visible-door regression is untested. Condition: r19 affected sweep must include the L9/L14/L16/L19 earned walks; consider narrowing _apply_open_bit or ledgering the cross-level effect.
2. BK08e test uses direct strike_ref/pop.strike calls + teleports for the guardian kills, not real input — weaker than the BK08d/BK09b standard set in the same batch (the board line for BJ11 asked for real clicks). Not a merge blocker; the cross() walks and negative checks are good.
3. BK09b's shot is not gated to region 1477 in code (only the hint is) — row 0390 says "stands on region 1477"; in-game any line-of-sight within 960 with form 0 + weapon records a pillar. Cosmetic/scope note.
4. Registry max at HEAD is 1033, not 1073 as the task stated; 1018 is free either way. (Observation, not a patch defect.)
5. BK10 operational: the test fails until the two prepare scripts run against the game files; CI/merge runbook must include staging (ORDER.md line 133 covers it). ogv stays out of git — fine.

Merge order: per ORDER.md 31-35 — BK08d → BK07b → BK10 → BK09b → BK08e on 5b769dc; all apply individually and cumulatively (verified both orders for the shared act2_progression.gd). After each ledger piece run build_deviations.py build; stage reels before running l19_placed_vqa_test. Verdict: approve all five for merge in ORDER.md order, with condition: affected sweep includes L9/L14/L16/L19 earned walks because of BK08e's generic open-bit drop, and ledger a follow-up noting the cross-level reach (or scope it).

• All checks complete. Here is the review.

## Findings

**Cross-cutting / mechanics**

1. All five patches sha256-match their board lines and apply cleanly on `5b769dc`, individually and cumulatively (`git apply --check`): ORDER.md order 31→35 passes as a stack, and the one shared file — `scripts/lol2/act2_progression.gd`, touched by BK07b (header + `aimed_struck` comment) and BK08e (`_on_field`, `_build_hinges`, `advance_movers`) — checks clean in **both** orders, matching ORDER.md:139.
2. Sol's Task 2 (`5b769dc`) does **not** touch `act2_progression.gd` — its 59 files are all Dark Halls / registry / docs (`git show --stat 5b769dc`). No conflict there.
3. Numbering: ledger is 484 pieces at HEAD and `tools/build_deviations.py --check` PASSes; pieces 0385, 0388, 0389, 0390, 0391 are all free (0384 = BK08c, 0400-0402 = Sol). Registry max order at HEAD is **1033** (Sol's 1020-1033), not 1073 as the task stated; order 1018 is free, no duplicates introduced, and BK10's `tests/registry/l19_placed_vqa_test.json` matches sibling schema.

**BK08d (0385)** — `tests/l19_bars_strike_test.gd`, `tests/l19_switch_shot_test.gd`

4. Does what the task says: tests now inject real `InputEventMouseButton` events via `Input.parse_input_event` + flush, replacing direct `strike_from_camera()/shot_from_camera()` calls. The host gate widens from `mouse_mode == CAPTURED` to `_player_click()` (`scripts/lol2/l19_sewer_forms.gd`, patch lines 23-29) which also accepts headless — documented in the header comment and row 0385 ("Headless has no window… A real window still requires capture"). The 15/16 left/right pairing stays flagged as an adapter.

**BK07b (0388, amends 0379)** — `scripts/lol2/l19_dawn_elevator.gd:90-102` (patch)

5. Implements exactly the K63 follow-ups: fresh-boot `restore()` now calls `pr._claim_region_floor(id)` while the region height is still the source floor, *before* `_place` writes the saved height (K63 problem 3), and local 4 is always written from the save (K63 problem 4). The amended row 0379's old line matches HEAD byte-for-byte and the new text fixes K63 problem 2's misleading "movable or control" wording (ray is mask 1, control solids layer 256).
6. The test's new `fresh_boot()` boots a second L19 scene, loads the earlier earned save, and verifies deck claim with real physics rays (`intersect_ray` down onto the platform, plus a "source floor is gone" ray) and a 45-tick physics stand check. The only placement is via the save written by the earned first half — no teleport across blockers.

**BK10 (0389, registry 1018)**

7. `tools/prepare_l19_e224e_movie.py` / `prepare_l20_placenta_movie.py` pin everything internally consistent with row 0389 and the board line: e224e = L19_BCI index 5, key 1194504581, 1256 frames 228x348; placenta = index 24, key 3224565000, 60 frames 640x340. Deps exist (`tools/lol2/map_video_inventory.py:131 lookup_movie`, `tools/prepare_cave_entrance_death.py:109 encode`). ogv output lands under `assets/lol2/generated/`, which `.gitignore:25` covers. `l17_beast_blade.gd` / `l19_dawn_curse.gd` / `l20_finale.gd` changes are comment-only and keep those cards as adapters; bb_brth and hw01 stay unplayed. Adapters (0x342 enable not entered, loop bit unread, ogg presentation) are honestly logged in row 0389.

**BK09b (0390)** — `scripts/lol2/l20_pillars_scotia.gd`

8. Does what the task says: five `PillarShot` receivers on the template-19 centre quads (layer 4, ray mask 7 — same as the L19 switch ray, patch lines 41-43), `record_shot()` shared by the old E path and the new `_unhandled_input` click path, west-proximity E preserved, ice 62 has no receiver. The earned tests now keep the player on the lip (region 1477) for all five shots with real click events — this *removes* the old teleport-to-each-pillar pattern, and adds an empty-hand negative check. Body/ray-length adapters are logged in row 0390 and the header comment.

**BK08e (0391)** — `scripts/lol2/act2_creatures.gd`, `act2_progression.gd`, `native_script_host.gd`

9. **Death caller is NOT generic.** The hook (patch lines 15-21) fires only when `area_id == "L20_BB" and (id == "47" or id == "48")` and the landed hit leaves health 0; `fire_event`'s kind-6 matcher requires `byte+4 == caller_byte` (`native_script_host.gd:707-711`), so only the two grate records run. My sweep found actor kind-6 caller-0x0B records in 10 levels — L12_CM (actors 29/36/37), L14_HT (~40 shade records, groups 21162-24160), L16_CA (actor 46), L19_BC (actor 31), L1_DC (6 records), L3_DH (~20 records), L4_HJ (actor 64), L8_SJ (7 records), L9_DR (actor 79), L20_BB (46/47/48) — **none** can fire from this hook because of the area+id gate. Zero risk to other-level earned walks from the death caller itself.
10. Within L20 the gate is exact but leaves one residual gap: `actor:46` also has a caller-0x0B kind-6 record (group 12398, op9 arm 0x15 on prop:4, `L20_BB.json`) that still never fires. Not a regression — worth a backlog note.
11. Group bytes verified against `L20_BB.json`: 12732 = `op1 travel 100 movable:52` + opcode 22 raw `1603...fa00` (exactly the `GRATE_OPCODE_22` constant), 12898 = the travel alone; 9278/9384 each do op16, op9 arm 0x0E, op5 arm 3, op1 travel 100 on **both** leaves. The opcode-22 stub refuses every other command, so the other 53 L20 opcode-22 groups keep their current refused verdicts; no test asserts the old unregistered-refusal string.
12. The open-bit mechanism is wired correctly: opcode 9 arm 0x0E stages `bit_0x15_0x80` (pre-existing, `native_script_host.gd` ~line 1502), the commit emits `object_state_changed` → `_on_field` (`act2_progression.gd:242,322`), and BK08e's new branch drops the mover body layer. The initial `_apply_open_bit` in `_build_hinges` is a no-op on fresh boot because native fields only exist after staged writes (`native_script_host.gd:488-491`). It is logged as an adapter in row 0391 — **but see Problem 1: it is not scoped to 50/51.**
13. The `advance_movers` physics sync (`force_update_transform` + `PhysicsServer3D.body_set_state`) is generic for all mover bodies on all act2 levels, not just the grate — a same-step accuracy improvement, low risk, but exercised only by the L20 test.
14. Test style: `cross()` walks with real `move_grounded` steps and includes proper negative checks (doorway and grate both block before the trigger). The guardian kill, though, teleports the player next to the body and loops `pop.strike()` with `strike_remaining = 0.0`, and `hammer()` calls `progression.strike_ref` directly — consistent with this file's pre-existing style, but not the real-input standard BK08d/BK09b set in this same batch.
15. Board lines (`COORDINATION.txt:4945,4966,4969,4971,4978`) match the patches on hashes, claims, and named runs; ORDER.md entries 31-35 match verified apply behavior.

## Problems

1. **BK08e's collision drop is generic, not scoped to movables 50/51, and row 0391 does not disclose the cross-level reach.** `_apply_open_bit` runs for every movable with a mover body whenever any hosted group sets `bit_0x15_0x80`. My sweep of all `native_scripts/*.json` for opcode-9 arm 0x0E on movables, cross-referenced with faced movables in each level's `area.json`, found live hosted paths that set the bit with **no travel command** — collision will drop while the mesh visibly stays:
   - L14_HT movables 85/86/87 — kind-4 E-use, groups 20436/20524/20660 (no predicate); also 58-63 via control:74 caller-20 enqueue group 17180.
   - L16_CA movable 66 — kind-4 E-use, groups 49134-49324 (no predicate, six records).
   - L19_BC movables 61/62 — region 1903 entry event 2, group 1082 (no predicate; region entries are hosted since BK07's group 1100).
   - L9_DR movable 58 — kind-4 E-use group 17512; 55/59 via prop:949 caller-20 enqueue group 5094. (L9 movables 55/58/59 are faced in `assets/lol2/generated/dragon_level/area.json`.)
   Plus likely-benign with-travel cases (L19 57/58, 63, 73; L16 99/100; L14 80). Each no-travel case is either a native-faithful fix (same argument as 50/51) or a walk-through-a-visually-closed-door regression — untested either way. Condition the merge on the r19 affected sweep including the L9, L14, L16, and L19 earned walks, and ledger the cross-level effect (or scope `_apply_open_bit`).
2. **BK08e's new test segments don't use real input** for the guardian kills (`pop.strike()` direct, player teleported to the body) — weaker than the BK08d/BK09b real-click standard this batch establishes, and the BJ11 board ask was about real player actions. Not a blocker (the walk-through checks use real movement and assert the blocked state first), but flag it for the qualification run.
3. **BK09b's shot is not gated to region 1477 in code** — only the hint text checks `on_east_lip()`; `record_shot` accepts any form-0, weapon-equipped click whose 960-unit ray meets a receiver. Row 0390's "stands on region 1477" overstates the gate. Cosmetic; the receiver geometry makes off-lip hits unlikely.
4. **BK10 is operationally gated**: `l19_placed_vqa_test` fails until both prepare scripts are run against the game files (ORDER.md line 133 covers this; the test's failure message says so). Make sure the merge runbook stages the reels before the suite run.
5. Task-statement discrepancy (not a patch defect): registry max order at HEAD is 1033, not 1073.

## Merge order and verdict

Apply on `5b769dc` in ORDER.md order — verified clean as a cumulative stack:

1. `BK08d_l19_real_clicks.patch` (0385) → `build_deviations.py build`
2. `BK07b_l19_cab_decks.patch` (0388, amends 0379) → re-render (order vs BK08e interchangeable, verified both ways)
3. `BK10_placed_reels.patch` (0389, registry 1018) → re-render, then stage reels (`prepare_l19_e224e_movie.py`, `prepare_l20_placenta_movie.py`) before running `l19_placed_vqa_test`
4. `BK09b_east_lip_shots.patch` (0390) → re-render
5. `BK08e_l20_doorways.patch` (0391) → re-render

**Verdict: approve all five for merge**, with one condition and two follow-ups: (a) the r19 affected sweep must include the L9/L14/L16/L19 earned walks because BK08e's open-bit collision drop reaches faced movables outside L20 through already-hosted use/enqueue/region-entry paths (Problem 1); (b) ledger that cross-level reach as a follow-up row or scope `_apply_open_bit`; (c) note BK08e's direct-call test style and the unfired actor:46 caller-0x0B record for the backlog. Nothing here blocks the merge itself — every patch does what its task and board line say, the native claims I re-derived (groups 9278/9384/12732/12898/12398, the opcode-22 raw, the reel pins, the cab-claim ordering) all check out, and numbering is clean.

