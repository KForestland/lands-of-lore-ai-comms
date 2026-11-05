# R2 adapter review, 2026-11-05

No Godot was run. The idle line still names `lol2_r12y`. This pass opened `~/opus_work/lol2_r15_campaign2` at `f6a5aa4` and did not edit it. Rows 0227 through 0308 stay in the 2026-11-03 and 2026-11-04 reviews. The new behaviour since those files is the Hive lift.

## Lift speed and the pit lip

`hive_elevator_state.gd` starts a fresh lift at stop 7, height −1579, until the flute sets target 0. `SPEED` is 96. The armed flute is polled once a second. HINTBOOK lines 2665–2668 say the hall leads to an open pit, the flute summons the elevator, and a flat floor rises from the depths. Those lines print no speed and no seconds. 96 and the one-second poll stay the adapter. No printed number replaces them.

Native trigger 282 in `assets/lol2/generated/hive_elevator/elevator.json` is a four-corner box, floor −235, x −1984 to −1896, z −7696 to −7536. The pit lip in `hive_elevator.gd` is x −2370 to −2240 on the same z band. The wax route stands at (−2355, −7614), which is inside the lip and outside trigger 282. Trigger 283 is further east and does not contain that point either. Deviation 0205 already calls the lip a modern arm so a save at the pit can still summon. The book’s pit is not that native box, so the lip is not a second copy of 282. Removing it would leave the wax route’s stand-point with no arm.

Commit `f6a5aa4` adds no deviation row. It plays the flute in `hive_lift_wax_walk_test.gd` when the platform is not already at −235, and only on the extended route, which is the wax return. That matches lines 2665–2666. `play_flute` still refuses a second play once `played_flute` is set. The later “whistle again” at lines 2699–2700 was not given a second host.

Grade: HINTBOOK for lines 2665–2668 and 2699–2700. DECODED for trigger 282’s box and for the lip test. No simpler native build.
