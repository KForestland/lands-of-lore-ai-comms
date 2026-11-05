# K04 Act 2 chain, part 4

No Godot was run. Newest owner file is still `TRIAGE_20261104.md`. HINTBOOK 3894–3928: the dreamstone is the key to the Huline Temple, and the mountains are the gulch plus the citadel. BRADY printed 211–214, file markers PDF PAGE 212–215, steps 52–81. No `l12` or `l13` script is in `my_journal.gd`.

## Steps

Gulch and the ice caves. HINTBOOK 3924–3928: the arrival is the bottom of an icy gulch; climb a ravine to the north-east; an ice bridge leads to the white-furred village. BRADY steps 55–56: plateau, ice caves, Kenneth's body, platforms, Baccata in the tunnel before the citadel. Host: `l12_glacier.gd`, `l12_citadel.gd`. Earned tests `l12_gulch_earned_test.gd` (arrival, ramp, controls 113, 112, 110, 107, 109, 111, 106, 108, and it records the non-gorilla path), `l12_ice_earned_test.gd`, `l12_citadel_earned_test.gd` (Kenneth, the ice crossing, Baccata, movie 13, native L13 selector 1). Verdict: HOSTED+TESTED for that path. BRADY step 52's Bracers of Valor are not in any `l12_*.gd`. Verdict: MISSING. Fix: the shelf item in the white-fur hut. The gulch test does not go there, so the spine does not depend on it.

Citadel entry, drains, elevator, Ruloi. BRADY steps 57–64. Host: `l13_egg_door.gd` (globe 420, door 106, region 1226), `l13_eggs.gd`, `l13_basin.gd` (items 145, 146, 147), `l13_elevator.gd`, `l13_prison.gd`, `l13_spires.gd`. Earned tests `l13_egg_door_earned_test.gd`, `l13_eggs_earned_test.gd`, `l13_basin_earned_test.gd`, `l13_elevator_earned_test.gd`, `l13_upper_ruloi_earned_test.gd`, `l13_lower_ruloi_earned_test.gd` (nineteen Ruloi), `l13_prison_refusal_earned_test.gd` (maidens refuse while Ruloi live), `l13_spires_prison_earned_test.gd`. Verdict: HOSTED+TESTED.

Bridge, Hive Lord, forge, Dreamstone. BRADY steps 65–71: plasma bridge, web door, kill the Hive Lord, put the sword on the pedestal, take the Dreamstone. Host: `l13_bridge.gd` (plates 90–100), `l13_belial.gd`, `l13_altar.gd`. The altar is `Vector3(-2343, -1020, -4538)`. The stone pedestal is `Vector3(-2710, -1020, -4183)`. The sword converts first; the stone is taken second. Earned tests `l13_bridge_earned_test.gd`, `l13_pink_steps_earned_test.gd`, `l13_belial_entry_earned_test.gd`, `l13_belial_combat_earned_test.gd`, `l13_altar_earned_test.gd`. Verdict: HOSTED+TESTED. The repaired-Thohan sword is the sentence Brady allows and this altar test does not walk.

Free Dawn and leave. BRADY steps 73–75: the stone opens her lock, she gives the Bestial Disk, the stone opens the entrance and must be taken back. Host: `l13_dawn_release.gd`, `l13_exit_lock.gd` (place, then retrieve). Earned tests `l13_dawn_recess_earned_test.gd` (wrong items refused), `l13_dawn_release_earned_test.gd`, `l13_exit_lock_earned_test.gd` (native Claw Mountains exit), `l13_return_pad_earned_test.gd`, `l13_return_descent_earned_test.gd`, `l12_exit_cave_earned_test.gd`. Verdict: HOSTED+TESTED.

Back to the temple door. BRADY step 81: Dreamstone on the front door, then the inner double doors. Host: `l14_temple_doors.gd` hides movables 92 and 93 when `l8_temple_door_state.gd` is unlocked. The slot target is `temple:entrance1198`. The item must be definition 136, and `retrieve` gives it back. Earned test `l14_temple_entry_earned_test.gd` walks the doors and keeps the stone. Verdict: HOSTED+TESTED.

Side earned tests that are not this spine: `l12_niche_armor_earned_test.gd`, `l12_frozen_bow_earned_test.gd`, `l12_crevasse_earned_test.gd`, `l12_river_niche_earned_test.gd`, `l12_logs_approach_earned_test.gd`. They were not graded against a second book paragraph.

## Journal

No note tells a lost player to climb the gulch, drain the basin, or take the stone after the sword. Verdict: MISSING. Fix: one `discover` on `l13_altar.gd` while the sword is not yet converted, and one on `l14_temple_doors.gd` while definition 136 is carried and the slot is still locked. Wording is the K09 list.

## Still open

The Valor bracers. The Thohan sword on the same pedestal. A journal line anywhere in L12 or L13.
