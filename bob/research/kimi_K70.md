# Kimi K70 — pre-merge review: grok BK08e + BK08f (L20 doorways, open-bit scope)

## Findings

**Apply + base state**

1. Base is clean for this review: `~/opus_work/lol2_r18` is on branch `r19-work` at `828cd8e9a8d31feec27b96b1d1c4bc99b790f6b8`; `git status` shows only untracked asset files. `BK08e_l20_doorways.patch` passes `git apply --check` on 828cd8e; `BK08f_l20_open_bit_scope.patch` does **not** apply alone (its context is BK08e's inserted `_apply_open_bit(id)` call) but passes `--check` after BK08e is applied (verified cumulatively via a temporary git index, worktree untouched). Order BK08e → BK08f is required and works.

**Scope gate (the K69 problem-1 fix)**

2. After both patches, the collision drop can only fire for L20 movables 50/51. `_apply_open_bit` (added by BK08e at `scripts/lol2/act2_progression.gd` ~934, gated by BK08f patch lines 12-13) opens with `if area_id != "L20_BB" or (id != 50 and id != 51): return`. Its only two callers are the new `_on_field` branch and the `_build_hinges` tail (both from BK08e), so the gate covers every entry. No other code sets a mover body's `collision_layer` to 0 — the only `collision_layer` writes in `act2_progression.gd:564,675,900` are all `= 1`. The L9 55/58/59, L14 85/86/87 + 58-63, L16 66, and L19 61/62 paths from K69 problem 1 all hit the `area_id` or id half of the gate and keep their collision.
3. The field pipeline is intact and exact: opcode 9 arm 0x0E stages `_stage_bits(ref, 0x15, 0x80, 1)` (`scripts/lol2/native_script_host.gd:1502`); `_bit_name(0x15, 0x80)` yields `"bit_0x15_0x80"` (`native_script_host.gd:1045-1046`); commit emits `object_state_changed`, connected at `act2_progression.gd:245` into `_on_field` at `act2_progression.gd:325`, where BK08e's new branch matches that exact field name for `movable:` refs.

**Death caller and native data**

4. The death-caller hook (BK08e, `scripts/lol2/act2_creatures.gd` after :137) is gated to `area_id == "L20_BB"` and id 47/48 with health == 0; `fire_event`'s kind-6 matcher requires record byte +4 == caller_byte (`native_script_host.gd:707-711`). Verified against `scripts/lol2/native_scripts/L20_BB.json`: actor:47 has kind-6 record `0606bc310b00` (byte+4 = 0x0B) → group 12732; actor:48 has `060662320b00` → group 12898.
5. Group bytes match ledger row 0391 exactly: group 12732 @ file offset 15503525 = op1 travel 100 on movable:52 + opcode 22 raw `1603830030313735363230650000ff9dfa00` (byte-identical to the `GRATE_OPCODE_22` constant); 12898 @ 15503691 = the travel alone; 9278/9384 each do op9 arm 0x0E on both leaves 50/51 plus travel 100 on both. The `_op_unread_22` stub accepts only that one raw and returns the refusal string for everything else, so the other L20 opcode-22 groups keep their refused verdicts; no test asserts the old unregistered text.

**Ledger honesty and numbering**

6. Row 0391 as amended by BK08f (patch lines 53-54) now says "When byte +0x15 bit 0x80 is set on L20 movable 50 or 51, that leaf body stops colliding… The same bit on any other movable leaves its collision as it was" and "the open bit drops collision for L20 movables 50 and 51 only. Other levels keep their collision." That is exactly what the gated code does — honest.
7. Numbering: `tools/build_deviations.py --check` passes with **488 pieces** at HEAD; row 0391 is free (0390 = east-lip-shots, next used are 0400-0402). Registry: `tests/registry/` holds **1074 files**, max `"order"` 1033 — the task's "~1074" is the file count; neither patch adds a registry piece, so nothing to check there.

**Test logic (not executed — logic review)**

8. Post-merge `tests/l20_struck_doors_test.gd` is internally sound: negative cross checks (doorway and grate) run before any trigger; hammer(50) drops both leaves (L20 → gate passes, native field reads 1 via `field()` `native_script_host.gd:488`). BK08f's new segment sets `bit_0x15_0x80` on movable:53 via `set_field` (`native_script_host.gd:477`) + direct `_on_field` and asserts layer stays 1 (id gate), then swaps `area_id` through L9_DR/L14_HT/L16_CA/L19_BC and asserts leaf 50 stays solid (area gate), then restores and re-drops 50/51 before the successful cross. The leftover bit-1 on movable:53 is harmless downstream: the only consumer of that bit as a gate is the kind-4 walk skip (`native_script_host.gd:568-574`), and the rest of the scene's checks use kind-9 `strike_ref` (`act2_progression.gd:1096`) or fresh scene instances.
9. Grate scenarios: actors 47/48 start absent (matches `act2_creatures.gd:9-19` `_birth_area_quiet`), the test spawns them via `State.spawn`, kills via `pop.strike()`/`strike_remaining` (both exist, `scripted_creature_population.gd:28,362`), asserts `travel[52] == travel_for(52, 100)`, then BK08e's `advance_movers` physics-server sync makes the risen grate solid in the same step so `cross()` succeeds. Consistent end to end.
10. Residual gap unchanged from K69: actor:46's caller-0x0B record (group 12398, op9 arm 0x15 on prop:4) still never fires. Not a regression; backlog note.

## Problems

1. Test-style carryover (K69 problem 2 persists, unchanged): the guardian kills teleport the player and drive `pop.strike()`/`strike_remaining` directly rather than real input. Consistent with this file's pre-existing style; not a blocker, but keep it flagged for the qualification run.
2. I did not execute the Godot test suite — this is a static/logic review only (the scenes need the full asset build). The checks above trace every assertion against the merged code, but a headless run of `l20_struck_doors_test.gd` after merging is still required.
3. Task-statement nuance, not a patch defect: registry **max order** at HEAD is 1033 (1074 is the registry file count); ledger is 488 pieces as stated.

## Verdict

**Approve both for merge on 828cd8e, in order BK08e → BK08f.** BK08f resolves K69 problem 1 exactly as the lead decided: the open-bit collision drop is hard-gated to L20_BB movables 50/51 at the single choke point, the previously-reached L9/L14/L16/L19 doors can no longer lose collision, and row 0391's amended text matches the code honestly. Native claims (groups 9278/9384/12732/12898, the opcode-22 raw, the actor 47/48 caller-0x0B records) all re-verify against `L20_BB.json`, numbering is clean (488 pieces, 0391 free), and both patches apply cleanly in the stated order. Conditions: run `build_deviations.py build` after merging the new row, and run `l20_struck_doors_test.gd` headless before the r19 qualification, since this review verified logic, not execution.

