# Kimi K22 — WHATS_NEW_r16.txt vs lol2_r16 (read-only, 2026-11-06)

Lead: point 1 accepted - WHATS_NEW_r16 now says 'two Act 1 stuck points (Hive pit lift, big Jungle river)'. Point 2 is a false alarm: the full qualification (chain + detour + fresh + compare + build + package + smoke) lives in AI_COMMS/act1_completion_20261017/r16_qualification and tmp/r16_qualify.log, outside Kimi's read dirs. Point 3 OK (owner calls it the bridge film).

All checks are done — I have file:line evidence for every line. Here is the report.

  # K22 — Verification of `WHATS_NEW_r16.txt` against `~/opus_work/lol2_r16`

  Range checked: `589810c..HEAD` (r15 stamp → r16 stamp `53ef72f`), 24 commits. Final recorded test run: `tmp/regressions/r16c_rerun/report.json` — 894 tests, complete, **passed: true**, source-stable (2026-11-06 05:59 UTC). Build `~/opus_work/builds/act1_opus_20261106_r16` exists, `SOURCE_COMMIT` = `53ef72f` (HEAD), Linux export log ends in DONE.

  ## Claim table

  | Claim (WHATS_NEW line) | Script evidence | Test | Accurate? |
  |---|---|---|---|
  | FIXED: Talkers loud everywhere, no fading — Kelsrick, village people, exit woman | `ATTENUATION_DISABLED` + `max_distance=1200` on all 12 Jungle/Hive talker voices: `scripts/lol2/jungle_kelsrick.gd:70`, `jungle_village_dialogue.gd:43`, `jungle_exit_woman.gd:67`, also dawn, drunk, kityara, confidante, bacatta(×2), actor62, bacatta65, exit_encounter (`:64`), `hive_dawn20.gd:90` (commits `1c33ac0`, `db5efe5`) | `tests/npc_voice_reach_test.gd:27-30` asserts `ATTENUATION_DISABLED` on every Jungle talker + Hive Dawn20 | yes |
  | FIXED: Drowning works mid-Jungle-river (surface was missing) | `tools/propagate_liquid_surface.py` (bank-less regions take their bed's common bank level); applied — worktree `assets/lol2/generated/liquid/L4_HJ.json` has 367 regions with `"surface_from": "bed_common_bank"`, all depth > 0, only 3 bank-less regions still depth 0 (commit `db5efe5`) | `tests/liquid_drowning_test.gd:54-59` (mid-river region 4311 deeper than a Human, Human submerged) | yes |
  | FIXED: Bacatta leaves after the bridge film | `scripts/lol2/jungle_bacatta.gd:183-186` — once the exit encounter's ending movie (E068E.VQA) phase is "done", `bacatta.present=false` (commit `db5efe5`) | `tests/jungle_bacatta_live_test.gd:139-145` ("Bacatta leaves after the ending movie") | yes (see note 2 — the code/commit call it the *shore/ending* film E068E, not "bridge film") |
  | FIXED: Larkhon — journal says join the tribe first | `scripts/lol2/l8_larkhon.gd:24` (`larkhon_join_tribe` guidance), `l8_larkhon_state.gd:14` (note text) (commit `1c33ac0`) | `tests/l8_guidance_test.gd:28,63,70-73`; `tests/my_journal_test.gd` | yes |
  | MAPS: Huline Temple rooms no longer show through each other; draws only rooms seen through doors/openings | `scripts/lol2/region_visibility.gd:1-27` (Build-style BFS over shared region edges, window narrowing), wired for `L14_HT` in `act2_map.gd:59,102-104,167-169` (commit `44a6d98`, widened to all shared edges in `d9e3aaf`) | `tests/portal_areas_test.gd:11-18`; BFS exercised in `tests/hive_clip_test.gd:4` | yes |
  | MAPS: Same fix in Hive, Jungle, several Act 2/3 levels | `act2_map.gd:59` `PORTAL_VISIBILITY_AREAS = [L14_HT, L10_DC, L9_DR, L16_CA, L19_BC, L20_BB]`; Hive via `hive_review.gd:78-88` (L5_HC, hive.json only); Jungle via `jungle_walkthrough.gd:125-135` (L4_HJ, huline_content only) (commits `75597f2`, `2a3f407`) | `tests/portal_areas_test.gd` (asserts exactly this area list, Hive/Jungle off the const but on their hosts) | yes |
  | MAPS: Museum gallery bars fixed | `scripts/lol2/museum_gallery.gd:54-63,126` — real two-surface ArrayMesh bars (materials 431/433) + previously missing static bars 62/78 (commit `907a595`) | `tests/museum_gallery_bars_test.gd` | yes |
  | MAPS: Jungle tree top + sky edges fixed | `scripts/lol2/jungle_review.gd:73,120` (`TREE_TOP_SKIP=8631` dropped via `skipped_faces`, commit `0ae8f39`); `:143,577` `_lip_top` clips exactly faces 10239 and 9929 at region ceilings (commit `907a595`) | `tests/jungle_tree_top_test.gd`, `tests/jungle_sky_lip_test.gd`, `tests/jungle_arrival_test.gd` (face count) | yes ("sky edges" = two specific clipped wall faces) |
  | MAPS: flickering Hive roof fixed | `scripts/lol2/hive_review.gd:66,77` (`ROOF_SKIP=654` excluded → z-fight gone) (commit `907a595`); related Hive clip fix + `CROSSING_FACES` in `2a3f407` | `tests/hive_roof_test.gd`, `tests/hive_clip_test.gd` | yes |
  | MAPS: Cave crates can be pushed and stacked | `scripts/lol2/cave_crate_stack.gd:1-5,62` (shove adapter; crate pushed onto another rests on top), `cave_crate_wall.gd:1-4` + `textured_cave_review.gd:119-120` (riser collider) (commit `2a3f407`) | `tests/cave_crate_stack_test.gd`; `tests/static_collision_test.gd` updated in `0ae8f39` | yes |
  | JOURNAL: notes for the Act 1 stuck points | `scripts/lol2/act1_journal_hints.gd:7-9` — **exactly two** notes (Hive pit flute, Jungle river); header: "No other Act 1 beat had a hint sentence"; attached `hive_review.gd:126`, `jungle_walkthrough.gd:226` | `tests/act1_journal_hints_test.gd` | **partly** — see overstatement 1 |
  | JOURNAL: L8 village (blade, temple, guard, shaman mark) | `scripts/lol2/l8_village_hints.gd:8-11` — four notes matching those four beats; attached `darker_jungle.gd:208` (commit `77f63c7`) | `tests/l8_village_hints_test.gd` | yes |
  | JOURNAL: the tribe and Dawn | `scripts/lol2/l8_tribe_dawn_hints.gd:6-8` (initiation + Dawn's bracers/cemetery trees); attached `darker_jungle.gd:213`, `act2_map.gd:152` | `tests/act2_journal_hints_test.gd` | yes |
  | JOURNAL: cemetery/ruins | `l9_journal_hints.gd:5-6` (statue, flood), `l10_journal_hints.gd:6-7` (tomb oil, Emperor's door); attached `dragon_level.gd:145`, `act2_map.gd:151` | `tests/act2_journal_hints_test.gd` | yes |
  | JOURNAL: the Temple | `l14_journal_hints.gd:6-9` (scale, boulder, hoppers, chalice) attached `act2_map.gd:194`; plus `l13_journal_hints.gd` "temple" role attached `darker_jungle.gd:218` | `tests/act2_journal_hints_test.gd` | yes |
  | JOURNAL: the city (L16) | `scripts/lol2/l16_journal_hints.gd:6-7` (hourglass, one open tower); attached `act2_map.gd:174`; registered in `my_journal.gd:23` | `tests/act2_journal_hints_test.gd`, `tests/my_journal_test.gd` | yes |
  | ACT 3: Chamber of Voices → city | `scripts/lol2/l14_chamber_voices.gd:1-8` (Dreamstone in chalice → CITY movie → native go-to-level-16) (commit `ac79bcc`) | `tests/l14_chamber_voices_earned_test.gd` | yes |
  | ACT 3: arrival lift | `scripts/lol2/l16_arrival_elevator.gd:1-9` (plate opens doorway, ELEVATOR movie, decoded relocation to ground) (commit `5435c13`) | `tests/l16_arrival_elevator_earned_test.gd` | yes |
  | ACT 3: greenhouse fireball opens the tower doors | `scripts/lol2/l16_greenhouse.gd:1-8` — silverleaf in pyramid → hourglass → fireball drifts to the middle tower → opens the three FireWall doors (movables 92/93/94) (commit `70ce5a0`) | `tests/l16_greenhouse_earned_test.gd` | yes |
  | ACT 3: the dry fountain | `scripts/lol2/l16_dry_fountain.gd:1-6` — break orb (prop 210) → water plane → nine black-lichen clumps (commit `2a3f407`; earlier prop-602 attempt withdrawn in `d9fc8da`) | `tests/l16_dry_fountain_test.gd`, `tests/l16_dry_fountain_earned_test.gd` | yes |
  | ACT 3: later steps drafted, not in build | Consistent: `l16_journal_hints.gd:2` — "The other three towers are not fields in l16_greenhouse.gd and are not invented here" | — | yes |
  | STILL OPEN: L8 ladder/cache, tree bridge, platform, Museum crouch, magic niche | No such scripts exist (grep over `scripts/lol2`: no shaman-cache ladder, tree bridge, or magic niche code) | — | yes (correctly absent) |
  | Header: "Qualified: full Act 1 campaign + Dark Halls detour, build, packaged earned-resume smoke" | Build + exports exist (`SOURCE_COMMIT`=HEAD); recorded run `tmp/regressions/r16c_rerun` passed | — | **partly** — see overstatement 2 |

  ## Overstatements / suggested rewording

  1. **"New notes for the Act 1 stuck points"** — r16 adds exactly **two** Act 1 journal notes: the Hive pit lift flute and the big Jungle river (`act1_journal_hints.gd:7-9`, which itself says "No other Act 1 beat had a hint sentence"). If you were stuck anywhere else in Act 1 in r14, there is no new note for it.
     Suggested: *"New notes for the two Act 1 stuck points from r14 (the Hive pit lift, the big Jungle river), …"*

  2. **"Qualified: full Act 1 campaign + … (same profile as r14/r15)"** — the recorded r16 verification run on disk (`tmp/regressions/r16c_rerun/report.json`) is a **filtered "affected" run** (894 tests, `filtered: true`), not the full suite; it passed. The packaged build exists and matches HEAD. So "qualified" rests on an affected-subset run this time unless a full-suite/campaign record exists elsewhere (I found none in the worktree).
     Suggested: *"Qualified: r16 affected-test run green (894 tests), build + packaged smoke as in r14/r15."* (Also beware: `docs/act-one-r16-verification.md` in the repo is for an **older October "R16"** classic build — a naming collision; it is not evidence for this build.)

  3. **Minor wording (not an error): "Bacatta leaves after the bridge film"** — the trigger is the exit encounter's ending movie **E068E.VQA** reaching phase "done" (`jungle_bacatta.gd:183-186`); the commit and code comment call it the *shore/ending film*. If the owner knows it as the bridge film this is fine, but the F10 reference in the code is "he needs to disappear after the scene" — worth knowing the departure is keyed to the movie finishing, not to leaving the area.

  Everything else in the file — all MAPS lines, the Larkhon/journal fixes, the mid-river drowning fix, and all four ACT 3 items — checks out against the code and has at least one registered covering test, with the final recorded run green.

