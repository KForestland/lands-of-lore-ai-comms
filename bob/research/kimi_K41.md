# Kimi K41 — BH04-06 Dark Halls review (2026-11-08)

Lead: merge BH04->05->06 into r18 (no blockers). Open for follow-up (grok BH09): P9 jump through the blasted window (owner 17-17-34 wants it), sunlight ghost kill in the atrium, blast damages creatures, walks from the Dark Halls entry. WHATS_NEW_r18 says these plainly.

All evidence gathered. Here's the review.

  # K41 — Review: Grok Dark Halls BH04/BH05/BH06 vs brief K35 (P8/P9/P7)

  Base verified: `~/opus_work/lol2_act3` on `r18-work` @ `3b6a929` (Sol's slides/bookcases/crouch merged). I read every hunk of all three patches against the base files; BG27/BG28/BG29 file lists checked for overlap. No Godot/git-apply run, per role.

  ## BH04 — `dark_halls_crates.patch` (P8 crates + Iron Door, ledger piece 0342)

  | Aspect | Verdict |
  |---|---|
  | Contract (hintbook 2525–2533) | Met as adapters, all declared: 89 template-20 crates solid, E opens → crystal billboard (child 175 / prop_617.png, binary patch included), walk-into shove, level-3 Spark gate (native kind-9 predicate is caller bytes, not "crystals showing" — documented), detonation within radius 200 of door 84 runs group-7656 stand-in (mesh hide, collision off). Colin's Amulet gating is restored by making the door solid. |
  | Native fidelity | `dark_halls_crates_source.json` (3,041 lines): 89 crates, all template 20; crate 448 at (−1243, 750, −530), 84 units from door 84 (−1243, 750, −614) → native falloff damage 23, asserted in both tests. `dark_halls_blast_source.json` (67k lines): 600 falloff cases, 27 recipient-prefix cases, 2,014 region rows, radius 200, factor 40 — replayed exactly by `dark_halls_blast_rules_test`. Control 973's three prefix commands preserved into the quest bag. |
  | 17-18-15 clipping | Fixed for the player: solid `SCENERY_LAYER` boxes + player mask update; `_blocked` stops shove-overlap. 38 natively overlapping crate pairs stay visually interpenetrating (original placement), which is correct. |
  | Earned walk | Real physics at the spot: walk-into shove (90 ticks), crate stops 0–1.5 from the door, player blocked by crate and door, retreat, real `spark(3)` raycast, hp drop equals the native falloff, walk through the removed door. **But** the player is teleported next to crate 448 — no earned route from the level entry. |
  | Applies after BG27–29? | Yes. Contexts in `dark_halls.gd` (slides/bookcases lines from Sol's merge), `act_one_quest_state.gd:513` (dark_halls_doors block) match the base verbatim. BG27–29 touch none of these files. |
  | Ledger/vars/registry | Row 0342 present, evidence-dense. Typed vars throughout. Two registry entries, orders 935/936 — no collision (base max 931; BG27–29 take 932–934). PASS lines present. |

  ## BH05 — `dark_halls_escape.patch` (P9 escape blast, piece 0343)

  | Aspect | Verdict |
  |---|---|
  | Contract (hintbook 2534–2540) | Partial. Detonating an open crate within radius 200 of window 246 stores the group-8280 mark (opcode 197 arm 10 on region 1413, kept as record since table 0x2B53C isn't held), lights the pane broken-green, and opens `exits_open()` — while keeping the window-counter route as the other original path (matches the brief's "rumor" reading). **The player cannot jump through the hole**: sill + 10-unit curb stop the capsule 136 from the pane; exit happens via the shared route regions gated by `exits_open()`. Documented in the ledger row. |
  | Earned walk | Strongest of the three: verifies no crate reaches window 246 unshoved, then a real ~1,400-unit, 26-waypoint shove of crate 449 across the dome (2,400 physics ticks), retreat, spark, hp drop = falloff, and the walk to the pane stopping at the curb is asserted, not hidden. Still a teleported start at crate 449. |
  | Applies? | Requires BH04 (edits `dark_halls_crates.gd`, extends its `validate`, `_detonate`). Contexts match post-BH04 state. `dark_halls_windows.gd` hunk at `done()` matches base; `exit_center()`/`break_exit()` use existing `source.exit` (window 246 ✓), `by_control`, `_vec`, `_light(row, true)` ✓. `exits_open()` rewrite keeps the window-counter path intact. |
  | Ledger/vars/registry | Row 0343; `blast_exit`/`exit_group` validated; registry order 937 free; PASS present. |

  ## BH06 — `dark_halls_atrium.patch` (P7 atrium, piece 0344)

  | Aspect | Verdict |
  |---|---|
  | Contract (hintbook 2498–2507) | Partial. Chain 252 (kind 5 → group 8526 = sound 1084 on prop 639) via E → roof movables 52–55 slide to the decoded open poses (1362/2969, 1362/3228, 2194/3225, 2196/2967 — the opcode-18 +4/+6 words), bed floors swap soil→grass, the 12 prop_114 fruits (records 220–231) swap to frame 20 (matches the 21 op14 timer values 0–20). **Missing beat: "the sunlight destroys the ghosts"** — no shade stands in the atrium natively and the groups contain no kill, so nothing dies; a roaming shade (population wakes all at spawn, the known P2 deviation) inside the atrium survives the roof opening. The brief's plan had a kill adapter; Grok dropped it on byte evidence and documented that. |
  | Structure | Correctly *removes* the old static pre-grown adapter (the `static_face_material` grass swap and `frames[-1]` forced-grown material) so the bed starts brown/bare and the pull causes the change — this is the right direction vs the 2026-10-31 deviation. Garden test rewritten consistently (frame 24 → frame 20, grown→bare start). Parent `static_face_material` exists (`jungle_review.gd:736`), no break. |
  | Earned walk | Teleports to 220 from the chain, real walk to ≤110, real E. Weakest earned character of the three; start height y=432 is hardcoded (foot 12 units above the h420 floor — works only because gravity settles it; can't verify without running). |
  | Applies? | Needs strict sequence: its `dark_halls.gd` var-block hunk carries BH05's modified `exits_open` comment as context, and the `act_one_quest_state.gd` hunk sits on BH04's crates block. All contexts match the post-BH04+BH05 tree. |
  | Ledger/vars/registry | Row 0344 is exemplary (group-by-group decode: 12540/12564/13044/13530 op18, 12686's 21 timers, why 13062/13490 do *not* run). Registry order 938 free; PASS present. |

  ## Apply order

  Strict: **BH04 → BH05 → BH06** (BH05 edits BH04's new file; BH06's contexts quote both). BG27/BG28/BG29 commute with all three — zero file overlap (they touch act2/cave files, `scripted_creature_population.gd`, `walkthrough_save.gd`, `docs/DEVIATIONS.md`). Piece numbering 0339–0344 is sequential and consistent with ORDER.md's counts (427 → 432 after BH06). Note ORDER also lists **BH07** (orb) after BH06 — outside this review's scope.

  ## Problems by severity

  **Medium**
  1. **P9 escape is not walkable through the window** (BH05): the blast opens `exits_open()`, but the capsule stops 136 from the pane and region 1413 stays unreachable — the hintbook's "jump through the hole" is reduced to "the normal exit walk unlocks." Documented in row 0343 and codified by the test, so it's an accepted limitation, but the owner (17-17-34) will not be able to do what he described.
  2. **No sunlight ghost kill** (BH06): hintbook 2498–2507's "Two ghosts await … the sunlight destroys the ghosts" has no hosted effect. Evidence-based (no atrium shade, no kill in the groups) and documented, but with the all-awake population a live shade can stand in the atrium and survive the pull.

  **Low**
  3. **Blast doesn't damage creatures** (BH04): only the player takes falloff damage; brief P8 said "damage actors/player in a radius." Consequently `Rules.eligible()`, the 27 `recipient_cases`, and `candidate_regions()` are dead production code, exercised only by their unit test.
  4. **Earned tests teleport to the puzzle** (all three): real physics/input after placement, but no walk from the Dark Halls entry — the standard the triage rows 17-57-09/18-08-06 demand ("earned walk," not a placed probe). The shove/blast interactions themselves are genuinely earned.
  5. **Source-record inconsistency** (BH04): `crates_source.json`'s `crystal.texture` points at `res://assets/lol2/generated/dark_halls_crates/sprites/prop_617.png`, but the code loads `res://assets/lol2/dark_halls/prop_617.png`. The field is unused; cosmetic only.

  **Info / nits**
  6. BH06: `garden_bed_faces`/`grown_props` counters are now permanently 0, kept only so the rewritten garden test can assert it; sound 1084 is stored, never played (consistent with the SOUND backlog); the old 2026-10-31 garden deviation row stays in the ledger as history (append-only convention — fine).
  7. BH04's 67k-line `dark_halls_blast_source.json` is heavy, but matches the project's source-record pattern and is fully consumed by the rules test.
  8. Could not verify runtime behavior (no Godot per role); the atrium test's hardcoded spawn height and the escape test's 2,400-tick shove are the two spots most likely to be flaky when actually run.

