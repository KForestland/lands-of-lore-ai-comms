# Kimi K15 — verify K01_act2_chain_arrival.md names against lol2_r15 (read-only, 2026-11-06)

Lead spot-check: REACH 160 (l8_journey.gd:6) OK; my_journal.gd has no l8_journey reference OK; larkhon_join_tribe absent in r15 OK, but it EXISTS on act3-story (l8_larkhon.gd/l8_larkhon_state.gd, added 11-05 after the owner's r14 report) and lands in r16. Not a defect.

Verification complete. All checks were done read-only against `~/opus_work/lol2_r15` (paths below are relative to it).

  ## K01 verification table

  | Name | Kind | Exists | Evidence |
  |---|---|---|---|
  | `darker_jungle.gd` | script | yes | `scripts/lol2/darker_jungle.gd:178` — `Binder.arrival_pose("L8_SJ", data, selector)` |
  | `l8_journey.gd` | script | yes | `scripts/lol2/l8_journey.gd:7` — `TARGETS` with all three anchors |
  | `l8_journey_state.gd` | script | yes | `scripts/lol2/l8_journey_state.gd:5-6` — `BLADE`/`KEY` consts |
  | `l10_main_gate.gd` | script | yes | `scripts/lol2/l10_main_gate.gd:4` — `const SIGIL := "l8:shaman:Dracoid_sigil"` |
  | `my_journal.gd` | script | yes | `scripts/lol2/my_journal.gd:46` — `static func discover(host, id)` |
  | `l8_larkhon.gd` | script | yes | `scripts/lol2/l8_larkhon.gd:7` — `const NEAR:=600.0` |
  | `l8_gift_earned_test.gd` | test | yes | `tests/l8_gift_earned_test.gd:50` — prints `PASS STORY-001`; lines 31-45 run the three actions with wrong-offer refusal and save/reload |
  | `l8_temple_earned_test.gd` | test | yes | `tests/l8_temple_earned_test.gd:40` — `PASS STORY-002`; line 22 loads the walk fixture, line 28 commits `visit_temple` |
  | `l8_departure_earned_test.gd` | test | yes | `tests/l8_departure_earned_test.gd:7` — runs `show_guard`,`offer_daniel`,`visit_shaman`; line 11 checks blade not consumed |
  | `l10_gate_earned_test.gd` | test | yes | `tests/l10_gate_earned_test.gd` (file present) |
  | `l8_guidance_test.gd` | test | yes | `tests/l8_guidance_test.gd:28` — checks the guidance id on a placed probe; header line 6 confirms "presentation probe, not a progression route" (matches doc's "not an `*_earned_test.gd` walk") |
  | `l8_first_departure_walk.json` | fixture | yes | `tests/fixtures/l8_first_departure_walk.json` |
  | `TRIAGE_20261104.md` | owner doc | **no** (in lol2_r15) | Not under lol2_r15; it lives at `~/AI_COMMS/playtest_feedback_20261023/TRIAGE_20261104.md` |
  | `offer_daniel` | action | yes | `scripts/lol2/l8_journey.gd:60,155,174`; `l8_journey_state.gd:33` |
  | `hopper_interruption` | action | yes | `l8_journey.gd:61,156`; `l8_journey_state.gd:43` |
  | `recover_blade` | action | yes | `l8_journey.gd:61,157`; `l8_journey_state.gd:47` |
  | `visit_temple` | action | yes | `l8_journey.gd:62,159`; `l8_journey_state.gd:53` |
  | `show_guard` | action | yes | `l8_journey.gd:63,161`; `l8_journey_state.gd:57` |
  | `visit_shaman` | action | yes | `l8_journey.gd:175`; `l8_journey_state.gd:63` |
  | `target()` | function | yes | `l8_journey.gd:37` — `func target() -> String` |
  | `discover` | function | yes | `my_journal.gd:46` (static); called from `l8_larkhon.gd:103` |
  | `temple_visited` | state flag | yes | `l8_journey.gd:51,101,159` |
  | `TARGETS` anchors | const | yes | `l8_journey.gd:7` — entry `(-3854,32,1190)`, temple `(758,32,2046)`, village `(676,32,-4541)` — all three match the doc |
  | reach 160 | const | yes | `l8_journey.gd:6` — `const REACH := 160.0` |
  | `L8_SJ` | area id | yes | `darker_jungle.gd:144,178,202` etc. |
  | actor 93 | id | yes | `l8_journey.gd:105` (`["81","92","93"]`) |
  | actor 113 | id | yes | `l8_journey.gd:101-102` — spawned when `temple_visited` |
  | prop 1198 | id | partial | Exists (`l8_temple_door_state.gd:5`, `act2_progression.gd:477`, `l8_temple_door.gd:20`) but **not referenced in `l8_journey.gd`** as the doc's "same panel" phrasing implies |
  | actor 115 | id | yes | `l8_larkhon.gd:31,61,64` — guidance radius measured from body "115" |
  | blade id `jungle:kityara:Empty_hand` | item id | yes | `l8_journey_state.gd:5`; also `item_catalog.gd:122` |
  | sigil `l8:shaman:Dracoid_sigil` | item id | yes | `l8_journey_state.gd:6` — comment confirms "Original definition102 = 100-Drac sigil"; `l10_main_gate.gd:4` uses the same id |
  | **`larkhon_join_tribe`** | journal id | **no** | Zero matches in any `.gd` file. The actual ids are `larkhon_must_sleep`, `larkhon_ask_shaman`, `larkhon_serum_needs_leaf`, `larkhon_vapors_unactivated` (`l8_larkhon.gd:21-24`, `l8_larkhon_state.gd:13-16`) |

  Also verified the doc's negative claim: `my_journal.gd` contains no reference to `l8_journey` — true. And the doc's own proposed fix (`discover` from `L8Journey` when `target()` is set) is correctly absent — that is the MISSING verdict the doc states, not an error.

  ## Missing / mismatched items

  1. **`larkhon_join_tribe` (journal id)** — does not exist anywhere. The real pre-tribe id is `larkhon_must_sleep`, and the logic differs from the doc's description: `guidance_for` returns `larkhon_must_sleep` as the default (no Act 2 progress), and `larkhon_ask_shaman` only when the player is already a tribe member with the shaman trade incomplete (`l8_larkhon.gd:23-24`). The doc's quoted text ("Only the shaman can make the Larkhon sleep… Show Daniel's blade to the village guard first.") also does not exist; the real hint is "The Larkhon guards the way to the Claw Mountains. I cannot get past it awake; something must put it to sleep." (`l8_larkhon_state.gd:13`). The "owner's r14 case" framing (gift recovered, not admitted → blade-to-guard note) has no corresponding branch in the code.
  2. **`TRIAGE_20261104.md`** — not in lol2_r15 (it's in AI_COMMS, which is fine if the doc only means it as the owner's file, but it fails a literal "exists in lol2_r15" check).
  3. **prop 1198 in `l8_journey.gd`** — the id exists in the repo (temple door exit), but the journey panel code does not reference it; only the anchor/`visit_temple` action does.

  Everything else the K01 file names — all six script files, all five test files, the fixture, all six journey actions, `target()`, `TARGETS`, both item ids (including the definition-102 comment), the anchors, reach 160, the 600-unit Larkhon radius, and actors 93/113/115 — checks out.

