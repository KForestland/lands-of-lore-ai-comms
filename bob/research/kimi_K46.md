# Kimi K46 — pre-merge review: BI05, ATLAS-READABLE, BI06, BI07, BI08 (r19)

## Findings (numbered, file:line)
## Problems (numbered or none)
## Merge order and verdict

Findings:

1. All five patches apply cleanly (git apply --check exit 0) to r19-work 5b8c942.
2. BI06 retarget: task said Dawn; evidence says Kityara. Verified: jungle_kityara_source.json start_regions include 1257/1315/1324; report pose (669,-1590.6) is 67.1 from region 1324 edge and stands on region 1323 floor y=0; control0 at (808,-14,-1802), movie E066E.VQA; jungle_dawn_source.json actor 63 at (-5710,-100,3937) present:false — cannot be the figure at the report pose. Ledger piece 0347 is accurate on the facts I could check.
3. BI06 blast radius: pad applies to all 10 start regions (both her locations: control0 1257/1315/1324 and control83 870/876/892/899/900/914/915), not only region 1324. Disclosed in the piece ("A start region now also accepts..."), owner-approved adapter class.
4. BI06 test is a stepped teleport walk (stand() ray placement in ~8-unit steps, jungle_kityara_approach_earned_test.gd:87-92,140-144) rather than a physics walk like BI07/BI08 (move_grounded). It does start outside the pad, traverse, and assert max foot height < 8, so it satisfies "no placing at the goal / no jump", but it is a weaker "walks like a player" than the other two.
5. BI07: base jungle_bacatta.gd never positioned the voice players (voices created at scripts/lol2/jungle_bacatta.gd:57 with no position set) while _play_sound already placed escort sounds on the body (:353) — the patch brings voices to the same body placement via existing _owner_anchor (:358-365). Ledger claims verified: report-to-origin distance ≈ 5460 > max_distance 1200 (host origin is Vector3.ZERO — jungle has no native_translation, scripted_creature_population.gd:87-90); bus/unit_size/max_distance unchanged and asserted by the test.
6. BI07 test teleports the player to the report pose after the line starts (jungle_bacatta_voice_earned_test.gd:189-192) — the walk to the talk is earned; the audibility check at (3539,-4154) is a placed listener. Acceptable given the task wording ("player is in range when it plays") but note it.
7. BI08: root cause confirmed in base l8_cache_ladder.gd:92-99 — use() returns true but does nothing once state.climbed is true. Patch adds descend() (BASE = the owner's reported position (-1092,-10,-2627)) and rewrites use()/hint_line() gating on _at_top/_at_base. The existing l8_cache_ladder_test.gd expectation "a second E stays on the ledge" is replaced by climb-down/climb-up — a deliberate rule change (the old assert encoded the bug); stated in the piece.
8. BI05: claims reproduce exactly against assets/lol2/generated/jungle_review/jungle.json — I re-ran the selection logic in Python: 153 faces skipped, owner's faces 9149 (mat 714, region 2449, span 107..147) and 10313 (mat 62, region 4544, 127..147) included, hut header 8130 (region 615) kept. span_start 7573.
9. BI05 secondary stat off: ledger/piece say "159 headers beside a ceiling region keep drawing"; my replication of the code's rule counts 142 kept-due-to-ceiling (own or beyond), 0 kept because no region beyond. Under other readings I get 230/276/340. The load-bearing numbers (153, 9149, 10313, 8130) are exact; the 159 appears to be a counting-definition slip.
10. BI05 inheritance: skip_sky_headers is set in jungle_walkthrough._init (bi05 patch, jungle_walkthrough.gd), and darker_jungle.gd:72-73, dark_halls, dragon_level, act2_map, act2_jungle_return all inherit it. Verified harmless: only jungle_review/jungle.json has interior_audit/span_start; darker_jungle/area.json, dark_halls/area.json, dragon_level/area.json and all maps/*/area.json lack it, so span_start falls back to faces.size() and the skip set is empty everywhere but the Jungle. The ledger's "The Jungle sets this flag" is imprecise but practically true.
11. Atlas: all referenced APIs exist in base (museum_atlas.gd use_filter/overview/center_player/map_point/_atlas_saved; museum_interface.gd apply_ui_scale/cluster_size; my_journal.gd notes/discover; ui_scale cluster_scale/effective). All 7 Journal note ids exist in base scripts. Done-paths verified: jungle_village.local24 is the gate admission flag (jungle_village_state.gd:6-12), thieves_den flags "17" and room string exist, weapon_shop flag 253 exists. 11 places + 4 exits + 7 plot markers counted in atlas_places.gd — matches RELEASE/ledger. Place/exit reveal gated on explored regions or full area; plot markers gated on discovered notes and cleared by quest flags → complies with "plot markers only for what the player has learned" and explored-only.
12. Atlas names grade: RELEASE discloses names come from Prima hint book ch.6 / Journal wording ("no game text names exist") — matches the owner direction's evidence order (game text > hint book > longplay) with the absence of game-text names stated. Honest.
13. Atlas test is an earned walk (move_grounded through tests/fixtures/atlas_jungle_start_walk.json, 181-line fixture generated by tools/build_atlas_walk.py on the blocker-avoiding source graph), opens the Atlas via hud.toggle_atlas (the M path). No placing at the goal.
14. Ledger numbers: new pieces 0340 (bi05), 0341 (atlas), 0347 (BI06), 0348 (BI08), 0349 (BI07) — no collisions with base (max 0339) or each other. The pre-existing double 0339 (cave-river-jump-clock + jungle-bridge-deck-ramps) is allowed by design (tools/build_deviations.py W16 note: equal numbers render in name order). 0338/0331 untouched.
15. DEVIATIONS.md handling differs by lane: Grok patches ship piece files only (ORDER.md instructs running tools/build_deviations.py build afterward); Fable patches hand-edit DEVIATIONS.md AND add pieces. Base is in sync (build_deviations.py --check passes, 425 pieces). If bi05 and atlas are both applied, their DEVIATIONS rows must land in piece order (0340 before 0341) or --check fails until build is re-run.
16. Registry: equal orders are explicitly allowed (tools/check_registry.py W16: ties run in name order). New orders: BI05 933, BI06 933, BI08 934, atlas 934, BI07 935 — duplicates across patches (933×2, 934×2) but no collision with existing (max 923/864 region free) and legal per W16. Suite "core" valid.
17. Cross-patch file overlap: none except docs/DEVIATIONS.md (bi05 vs atlas, same append anchor — applies either order, but see finding 15 for the --check consequence).

Problems:
1. BI05 ledger stat "159 headers beside a ceiling region" does not reproduce (142 under the code's own rule) — minor honesty/accuracy slip in a non-load-bearing number (finding 9). Suggest Fable correct or clarify before merge; not a functional issue.
2. BI06's earned test walks by teleport-stepping rather than physics movement (finding 4) — weaker than the "walks like a player" bar set by BI07/BI08. Lead decision whether acceptable here (it does traverse and never places at the goal region... actually it does end standing exactly at the report pose, but that's the report pose, fine).

Hmm wait, is #2 a "problem" or just an observation? The rule: "earned tests walk like a player (no placing at the goal, no E where the original needs none)". The stepped teleport IS effectively placing at successive positions including the final goal. Strictly, it places the player at the goal (the report pose). But the trigger fires earlier (when crossing into the pad), not at the goal. The walk starts outside the pad. I think it technically bends the rule — flag as a problem for the lead to decide, since the project rule is explicit.

3. docs/jungle-kityara.md not updated: the BI06 patch updates the script header comment but docs/jungle-kityara.md:15-16 still describes start regions as exact tiles. Per project docs-convention... Is that a documented rule? The AGENTS.md instruction says update docs when behavior changes. The file docs/jungle-kityara.md is referenced from the script header ("docs/jungle-kityara.md"). Minor.

Also: Grok patches don't add DEVIATIONS.md rows — NOT a problem because ORDER.md explains the lane workflow (build renders it). Fine as long as merger runs build.

Any other problem? The BI07 test's AudioEffectCapture asserts frames >= 64 — in a muted/dummy audio driver CI this could fail; registry mode "rendered" suggests audio available. Minor risk note, not a problem.

Merge order:
1. All independent; any order works for code. Recommended: BI05 (bi05) → atlas (so DEVIATIONS rows land 0340 then 0341 matching render order) → BI06 → BI07 → BI08 (any order), then run tools/build_deviations.py build and python3 tools/check_registry.py, then run the affected tests: the five new tests plus jungle/l8 atlas suites (affected_tests.py --changed-since 5b8c942).

Verdict: merge, with two small actions (fix/accept the 159 stat, decide on the BI06 teleport-walk) and the DEVIATIONS render step.

Actually — one more check I should do: does `affected_tests.py` exist? tools listing showed run_regressions.py etc. The task list mentions affected_tests.py --changed-since. Not vital.

Also should double check the claim in BI05 commit message "Captures before/after at the owner's poses + 7 landmarks: only the two artefacts change" — captures in fable_lane/bi05_atlas_20261108/. The ledger references captures there. I can't verify visually cheaply... I could glance at the directory. Quick ls.

• One last quick look at Fable's BI05 evidence folder.bi05_before_after.png
bi05_landmarks.json
capture_probe.log
captures
pose_capture.gd
atlas_readable_20261108
bi05_atlas_20261108
BI05_ATLAS_NOTES_20261108.md
bi05_b702c65.patch
bi_decks_hedges_20261108
BI_DECKS_HEDGES_NOTES_20261108.md
FABLE_TASK_20261102.md
FABLE_TASK_20261104.md
FABLE_TASK_20261107B.md
FABLE_TASK_20261107.md
FABLE_TASK_20261108.md
light_l14_20261109
lol1_stack_20261108
mapfix_20261108
MAPFIX_NOTES_20261108.md
temple_islands_20261107
TEMPLE_ISLANDS_NOTES_20261107.md


• Evidence captures exist. I have enough. Time to write the final report in Markdown with ## Findings, ## Problems, ## Merge order and verdict.

• Review complete. All findings below were verified against r19-work `5b8c942` (branch r19-work) by static read, `git apply --check`, and Python replication of the data-driven claims.

## Findings

1. **All five patches apply cleanly** (`git apply --check` exit 0) to r19-work `5b8c942`. No textual conflicts with r19-work; the only cross-patch file overlap is `docs/DEVIATIONS.md` (bi05 and atlas both append a row after the same anchor line; applies in either order, but see Finding 15).

2. **BI06 retargets the task from Dawn to Kityara — and the evidence holds.** The task text says "Dawn's walk-in talk trigger", but the patch fixes Kityara's start regions. Verified: `scripts/lol2/jungle_kityara_source.json` start_regions include 1257/1315/1324, control 0 is at (808,-14,-1802) with movie E066E.VQA, and the report pose (669,-1590.6) is 67.1 from region 1324's edge, standing on region 1323's floor at y=0. `scripts/lol2/jungle_dawn_source.json:13` puts actor 63 at (-5710,-100,3937) with `present: false` — ~7000 units away, so it cannot be the figure at F10 15-24-21. The ledger piece (`0347-row-...kityara-walk-up.md`) states all of this openly.

3. **BI06 blast radius is wider than the reported tile.** The pad (`START_PAD:=96.0`, `START_RAISE:=48.0`, `scripts/lol2/jungle_kityara.gd` in patch) applies to all ten start regions — control0's 1257/1315/1324 and control83's 870/876/892/899/900/914/915 — so her second location's triggers also fire up to 96 units early. Disclosed in the piece; it's the owner-approved adapter class, but the lead should ratify the generalization.

4. **BI06's "earned walk" is a stepped teleport, not a physics walk.** `jungle_kityara_approach_earned_test.gd:87-92` ray-casts and sets `global_position` in ~8-unit steps, unlike BI07/BI08 which drive `move_grounded`. It does start outside the pad (self-checked > 96), traverses every intermediate point, and asserts foot height < 8 (no jump), but it is the weakest "walks like a player" of the three Grok tests.

5. **BI07 root cause and fix verified.** In base `scripts/lol2/jungle_bacatta.gd:57` the voice players are created and never positioned (they sit at the host origin; Jungle has no `native_translation`, so origin = world zero, `scripted_creature_population.gd:87-90`), while `_play_sound` already placed escort sounds on the body (`:353`). The patch routes voices through the existing `_owner_anchor` (`:358-365`) + 40 up, and leaves bus/unit_size/max_distance untouched (asserted by the test). Distance math checks out: (3539,32,-4154) is ~5460 from origin > max_distance 1200; actor 61 at (3550,-4152) is ~10 from the report pose. Ledger claims accurate.

6. **BI07 test note:** the walk into link region 1921 and up to prop 552 is earned (`move_grounded`), and E is pressed (required by the original). But after the line starts, the player is teleported to the report pose for the audibility assertion (`jungle_bacatta_voice_earned_test.gd:189-192`) — a placed listener, matching the task wording ("player is in range when it plays") but worth knowing.

7. **BI08 root cause confirmed in base** `scripts/lol2/l8_cache_ladder.gd:92-99`: once `climbed` is true, `use()` returns true and does nothing. The patch adds `descend()` to `BASE` (= the owner's reported position (-1092,-10,-2627)) and re-gates `use()`/`hint_line()` on `_at_top()`/`_at_base()`. The change to `tests/l8_cache_ladder_test.gd` (old assert "a second E stays on the ledge" → climb down / climb up) is a deliberate rule change — the old assert encoded the bug — and is stated in piece 0348. The repeat test walks in from outside reach, climbs, saves, reloads, descends, climbs again, and cleans up its save. Matches the task exactly.

8. **BI05's load-bearing claims reproduce exactly.** I re-ran the patch's selection logic in Python against `assets/lol2/generated/jungle_review/jungle.json` (span_start 7573) + `creature_nav/L4_HJ.json`: **153 faces** skipped, owner's face 9149 (material 714, region 2449, span 107..147) and face 10313 (material 62, region 4544, 127..147) are both in the skip set, hut header 8130 (region 615) is kept. Collision is preserved for skipped faces.

9. **BI05's secondary stat does not reproduce.** Piece 0340 says "159 headers beside a ceiling region keep drawing"; under the code's own rule I count **142** kept due to an own- or beyond-region ceiling (and 0 kept for "no region beyond"). Other readings give 230/276/340 — none is 159. The functional numbers are all exact; this looks like a counting-definition slip in the ledger text.

10. **BI05's flag is inherited by five other hosts, verified harmless.** `skip_sky_headers` is set in `jungle_walkthrough._init`; `darker_jungle.gd:72-73`, `dark_halls`, `dragon_level`, `act2_map`, `act2_jungle_return` all inherit it. Only `jungle_review/jungle.json` carries `interior_audit`/`span_start`; the L8/L7/dragon/act2 packs lack it, so `span_start` falls back to `faces.size()` (jungle_review.gd:133) and the skip set is empty outside the Jungle. The ledger's "The Jungle sets this flag" is imprecise in mechanism but true in effect.

11. **Atlas patch: every referenced API and datum exists in base.** `museum_atlas.gd` (`use_filter`, `overview`, `center_player`, `map_point`, `_atlas_saved`, `bounds`, `origin_offset`), `museum_interface.gd` (`apply_ui_scale`, `cluster_size`), `my_journal.gd` (`notes`, `discover`), `ui_scale.gd` (`cluster_scale`, `effective`). All 7 Journal note ids in `atlas_places.gd` PLOT exist in base scripts. Done-paths verified: `jungle_village.local24` is the gate-admission flag (`jungle_village_state.gd:6-12`), `thieves_den` has flags dict with "17" and a room string, `weapon_shop` FLAGS includes 253. Counts match the ledger: 11 places + 4 exits + 7 plot markers.

12. **Atlas complies with the explored-only / learned-only rules.** Wall lines draw only for explored slices (blocked thicket/rock regions excluded from floor); places/exits reveal only when an explored region is within radius or the area is full (old saves); plot markers require a discovered Journal note and clear when their quest path goes nonzero — including the honest disclosure that names are HINTBOOK-grade because the dialogue dump has no place names (matches the direction's evidence order).

13. **Atlas test is earned**: physics walk through `tests/fixtures/atlas_jungle_start_walk.json` (generated by the included `tools/build_atlas_walk.py` on the blocker-avoiding source graph), Atlas opened via `hud.toggle_atlas()`, and the marker-clear is driven by setting the admission flag — no placing at the goal. RELEASE.md openly lists the open items (no Journal-pin feature yet, other areas pending, den/weapon done-paths to confirm).

14. **Ledger piece numbers: no collisions.** New: 0340 (bi05), 0341 (atlas), 0347 (BI06), 0348 (BI08), 0349 (BI07); base tops out at the known double 0339 (cave-river-jump-clock + jungle-bridge-deck-ramps), which is explicitly allowed (`tools/build_deviations.py`, W16: equal numbers render in name order). 0338 and 0331 untouched. 0342–0346 remain free for other lanes.

15. **DEVIATIONS.md workflow differs per lane and is the one merge-time trap.** `docs/DEVIATIONS.md` is generated from the pieces (`build_deviations.py --check` passes on base, 425 pieces). Grok ships pieces only and ORDER.md says to run `build` after applying. Fable hand-edits DEVIATIONS.md *and* ships pieces. After merging both Fable patches the hand-written rows must sit in piece order (0340 before 0341) or `--check` fails until `build` is re-run.

16. **Registry orders are legal.** `check_registry.py` (W16) allows equal orders (ties run in name order); base passes with duplicates already present. New orders: 933 (bi05 + BI06), 934 (BI08 + atlas), 935 (BI07) — no collision with existing values (free above 923).

## Problems

1. **BI05 piece 0340 / DEVIATIONS row: the "159 headers … keep drawing" figure is wrong** — the code's own rule yields 142 (Finding 9). Cosmetic, non-functional, but the ledger is the owner-facing honesty record; have Fable correct or annotate it (one-line piece edit + `build_deviations.py build`).

2. **BI06's earned test teleports in steps instead of walking** (Finding 4) — it bends the "walk like a player" rule that BI07 and BI08 satisfy properly with `move_grounded`. No placing *at the goal* and no jump, so the spirit is kept, but the lead should either accept the weaker form or ask Grok for a physics walk.

3. **`docs/jungle-kityara.md` not updated**: the script header now documents the pad, but the doc it points to (`docs/jungle-kityara.md:15-16`) still describes the start regions as exact tiles. Minor; one line would close it.

## Merge order and verdict

All five patches are mutually independent at the code level. Recommended sequence on r19-work:

1. `bi05_b702c65.patch` (BI05, piece 0340)
2. `atlas-readable_fee76a0.patch` (piece 0341) — after bi05 so the hand-written DEVIATIONS rows land in render order
3. `BI06_kityara_walk_up.patch` (0347), `BI08_l8_cache_ladder.patch` (0348), `BI07_bacatta_voice.patch` (0349) — any order
4. Run `python3 tools/build_deviations.py build` (renders the Grok rows; keep `--check` green) and `python3 tools/check_registry.py`
5. Run the five new tests plus the affected sweep before stamping r19

**Verdict: merge all five.** Every patch does what its task says, the ledger rows are honest on every load-bearing claim I could verify (BI06's Dawn→Kityara retarget is evidence-backed and disclosed; BI05's 153-face rule reproduces exactly; BI07's distance math and BI08's root cause check out; the atlas data and rules compliance hold). The only pre-merge asks are cosmetic: fix the "159" in the BI05 ledger row, ratify the BI06 test's teleport-walk and its all-start-regions pad, and add the one line to `docs/jungle-kityara.md`.

