# Kimi K54 — pre-merge review: fable BJ10 captions + grok BJ04 + BJ07 boarding reason (r19)

## Findings
1. All three patches pass `git apply --check` on dd8feec.
2. Fable patch contents: 28 string rewrites across 12 host scripts + 1 test substring + ledger row 0358 (piece + rendered DEVIATIONS.md) + new tools/build_act3_routes.py. Only behavior change: l19_belial_horn.gd at_pipe() gains RIM_AT.
3. Honesty audit per rewrite (list which are fine, which aren't).
4. l17_cavern_run else-branch problem: CIRCLE (50) and SIDE (1318) exits decode to level 16, but new shared text says "The way on into Belial's chamber." Wrong text for the L16 exits.
5. l17_beast_blade "the wall gives way" overstates — relocates_player() false; test pins Luther stays.
6. Sewer forms "shoot"/"thrown" wording vs proximity-recorded, no keypress.
7. Ledger 0358 collision: both Fable's piece and Grok's BJ04 piece use NNNN 0358; distinct filenames so git merges clean, and duplicates have precedent (0350, 0351 already duplicated). Recommend renumber one.
8. DEVIATIONS.md ordering: Fable's patch made on c611100 inserts its row after 0356; dd8feec appended 0357 after that. Result: 0358 row lands before 0357 row → build_deviations.py --check fails. Fix: run tools/build_deviations.py build after applying (pieces sort by NNNN).
9. BJ04: group number 7888 correct per BJ04_soul_writes.md (task text's "7088" is a different unentered group). add_soul exists, clamps 0..10; closed() guard prevents double add on reload; test checks both. Typed vars ok. No registry change.
10. BJ07 comment matches HEAD code (retry loop merged in dd8feec); comment-only.
11. Registry orders untouched by all three (max 977 stands).
12. Horn rim change untested: l19_belial_horn_earned_test teleports to PIPE_AT; no test exercises RIM_AT. The only progression change in the batch has no earned coverage.
13. Grok BJ04 patch doesn't include rendered DEVIATIONS.md (their convention: merger runs build). Fable's includes both. One build run after both fixes everything.

## Problems
1. l17_cavern_run.gd:92-93 — merged hint wrong for level-16 exits.
2. l17_beast_blade.gd stage text "the wall gives way" claims a passage that doesn't happen.
3. DEVIATIONS.md row ordering breaks --check after apply (fix via build).
4. Ledger 0358 number collision (advisory; precedent exists).
5. Rim grant untested (advisory).
6. Minor: "shoot"/"thrown" wording.

## Merge order and verdict
Order: BJ07 comment (trivial) → BJ04 → Fable BJ10, then run build_deviations.py build, renumber one 0358. Verdict: merge with fixes — fix the two caption overstatements before merge (lead decision), renumber ledger piece, re-render.

Actually on the cavern run: is the else branch reachable? reached() returns CIRCLE/SIDE for those anchors; the text shows whenever the player is near those. Yes reachable. Definitely wrong text there.

Verdict: take BJ04 and BJ07 as-is (with ledger renumber advisory for BJ04); Fable patch needs the l17_cavern_run else-text fixed (keep distinct text for the L16 exits) and ideally soften "the wall gives way" / add rim test; then merge.

• Review complete. Everything below was verified against the base tree at dd8feec (read-only; `git apply --check` and `--check` runs only, no files touched).

## Findings

1. **All three patches apply cleanly on dd8feec** (`git apply --check` passes for each). Fable's patch was made on c611100 but nothing in c611100..dd8feec touches its scripts.
2. **Fable patch scope** (`bj10-finale_7708887.patch`): 28 HUD/caption rewrites across 12 Act-3 host scripts, one pinned-substring update in `tests/l17_beast_blade_earned_test.gd:60`, ledger piece `docs/deviations/0358-row-2026-11-09-act3-hosts-player-voice.md` plus the rendered `docs/DEVIATIONS.md` row, and new `tools/build_act3_routes.py`. The **only code-behavior change** is `scripts/lol2/l19_belial_horn.gd:56` — `at_pipe()` gains `RIM_AT (120,0,350)`, 175 units short of `PIPE_AT`, non-overlapping reach. Everything else is string-only. No progression change beyond the horn rim — confirmed.
3. **Caption honesty — the rewrites that are fine**: `l19_beast_wall.gd` ("drawn into the beast and steps through" — the module really relocates the player to `STEP_AT`); `l19_ghostly_heads.gd` (the token mesh moves to the circle); `l19_drain_path.gd` (the door really opens via `open_doors()`); `l19_sewer_forms.gd` bars/gutter lines (the leaf/mouth meshes visibly move); `l19_dawn_curse.gd`, `l20_finale.gd`, `l20_pillars_scotia.gd`, `l20_faux_draracle.gd`, `l20_armory.gd`, `l19_belial_horn.gd` — all describe what the E actually records; the "Baccata is dead." pin (`tests/l19_belial_horn_earned_test.gd:53`) and the birth/birth-card pins are preserved. The missing movies are no longer claimed anywhere.
4. **Caption honesty — two that are not honest** (see Problems 1–2): `l17_cavern_run.gd` and `l17_beast_blade.gd`.
5. **Grok BJ04** (`BJ04_l8_shore_soul.patch`): the group number in the patch is **7888, which is correct** — `grok_research/BJ04_soul_writes.md:11` documents prop 630 / stream-1 group 7888 / opcode 206 `ce0000000001` at offset 13448384. The task text's "7088" is a different, still-unentered group (`adapter_review_20261105_0253.md:95`). The patch hooks `add_soul` (`scripts/lol2/shared_global_defaults.gd:19`, clamps 0..10) onto the existing shore receipt after the `closed()` guard, so reload cannot double-add; the test pins the +1 and the reload persistence against an actual completed raft save. Typed vars throughout. No registry change.
6. **Grok BJ07** (`BJ07_boarding_reason.patch`): comment-only; its claim matches the merged retry loop at `tests/l12_river_return_earned_test.gd:23-33` (four attempts, `request_jump()` refusal → `continue`, success = riding the raft). Applies on dd8feec as ORDER.md states.
7. **Registry**: none of the three patches touches `tests/registry/` — max order stays 977, no collisions.
8. **Ledger 0358 collides**: Fable's piece `0358-row-2026-11-09-act3-hosts-player-voice.md` and Grok's `0358-row-2026-11-08-l8-shore-soul.md` share NNNN 0358. Distinct filenames, so git merges clean, and duplicate numbers already exist in the ledger (0350 ×2, 0351 ×2) — but it's a real duplicate worth renumbering.
9. **DEVIATIONS.md ordering breaks `--check`**: Fable's patch (based on c611100) inserts its row right after the 0356 Citadel row; dd8feec since appended the 0357 row after that (`docs/DEVIATIONS.md:569`). Post-merge file order becomes 0356, **0358, 0357**, while `tools/build_deviations.py build` renders sorted by NNNN — so `build_deviations.py --check` (currently PASS, 445 pieces) will fail until the merger re-renders. ORDER.md already prescribes `build` after Grok patches; one run fixes both.
10. **The horn-rim grant is untested**: `tests/l19_belial_horn_earned_test.gd:43` teleports Luther to `PIPE_AT`; no test walks to `RIM_AT` or pins `at_pipe()` from the rim. The batch's only progression change has probe evidence (`l19_pipe_rim.png`) but no earned test.

## Problems

1. **`scripts/lol2/l17_cavern_run.gd:90-93` (patch line 78-83) — factually wrong caption.** The patch makes both branches read "The way on into Belial's chamber." But the `else` branch covers the movable-50 circle (level 16 arrival 2) and region 1318 (level 16 arrival 3) — those exits lead to **L16, not Belial's chamber** (constants at lines 16-23). It also drops "Luther stays" for the 1312/1313 exit, which the module still records without changing the scene (line 7-8 docstring: "records the region and does not change the scene"). Needs a per-branch text, e.g. "The way back to the Claw Mountains." for the L16 exits.
2. **`scripts/lol2/l17_beast_blade.gd:82` — "the wall gives way" claims a mechanic that does not exist.** `relocates_player()` returns false and the earned test still pins "Luther stays on the west edge"; NOTES mechanics 2 lists the beast-scene relocation as unhosted. "Luther cuts the red strands" alone would be honest; "the wall gives way" is not.
3. **Ledger bookkeeping**: duplicate NNNN 0358 across the two patches (Finding 8) and the rendered-row ordering break (Finding 9). Both fixed at merge time by renumbering one piece (0359) and running `python3 tools/build_deviations.py build`.
4. **Minor wording**: `l19_sewer_forms.gd` "Back to the Human to **shoot** the three slotted switches" and "Switch %d **thrown**." — no bow binding exists (NOTES mechanics 4) and the switches record on proximity in `_process` with no keypress. Pre-existing behavior, but the new wording now attributes an action the player never takes.
5. **Advisory**: no earned test for the new rim grant (Finding 10).

## Merge order and verdict

Order (all independent, this minimizes re-work):

1. `BJ07_boarding_reason.patch` — comment only, zero risk.
2. `BJ04_l8_shore_soul.patch` — renumber its piece to `0359-row-2026-11-08-l8-shore-soul.md`.
3. `bj10-finale_7708887.patch` — after fixing Problems 1 and 2 (two-line edits in `l17_cavern_run.gd` and `l17_beast_blade.gd`).
4. Run `python3 tools/build_deviations.py build`, then `--check` to confirm.

**Verdict: merge with fixes.** BJ04 and BJ07 are clean as-is (BJ04's group 7888 is the correct decoded number; the soul write is well-guarded and well-tested). Fable's patch is honest in 26 of 28 rewrites and correctly scoped to one progression change, but the two L17 captions (Problems 1–2) violate the "no claim that a missing mechanic now exists" bar and should be corrected before merge rather than after — Problem 1 is not just an overstatement, it mislabels exits to the wrong level.

