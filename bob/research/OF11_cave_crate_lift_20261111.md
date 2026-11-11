# OF11. Cave crates lift with E

The owner said the caves are done except stacking the boxes by lifting them with E. The hintbook (lines 2046-2048) says to stack the boxes, climb, and take the mace. It does not name a key. The mouse-grasp sentence just above that is the stone pillars, not these boxes. Longplay frame f_00127 is 10:30 and shows the crates in the mine passage.

## Grades

| Claim | Grade |
| --- | --- |
| Controls 94, 95, 96, 97, 112, 121, and 122 are the mine crates. Templates 25 and 26, height -215, flags 0x2982. None of those control records has an event | PROVEN. native_scripts/L1_DC.json placement bytes |
| No opcode 18 targets those controls. Groups that mention index 94 and its neighbours belong to the dungeon props at y about 17000, not these crates | PROVEN. The same index on prop 94 is at (-102, 17036). Movable 58, which zeros those indexes, is at (-65, 17092) |
| Whether the original drags a crate with the mouse was not read in the player code | UNKNOWN |
| E now lifts the faced crate and E sets it on the crate in front, or on the floor. A walk still shoves. Five medium crates (20 each) clear the 85-unit lip. The player stands on that stack, and a save restores it | PROVEN. tests/cave_crate_lift_earned_test.gd PASS, exit 0. tests/cave_crate_shove_earned_test.gd PASS, exit 0. The unit test PASS |

## What changed

`scripts/lol2/cave_crate_stack.gd` keeps the shove. E, from the cave key handler, calls `try_use`. The lift reach is 24 past the shove, so the body is not already pushing the crate it takes. A carried crate has no collision and follows Luther. The save key is `cave_crates` on the cavern quicksave. An old save without that key is unchanged.

Commit 9ad612f1355880c302f0c9cce12006e584c8854c on grok/of9. Piece 0517. Registry order 755, headless. Lead runs tools/build_deviations.py build. This lane did not.

`/tmp/godot_dummy.sh --headless --path ~/opus_work/lol2_grok_of9 --script res://tests/cave_crate_lift_earned_test.gd`

Printed `PASS crate lift: E stacked five crates to the lip, and the save kept the stand`. Exit 0. No "resources still in use".

The shove test printed `PASS crate: walked into crate 94, it moved, and it rests on crate 95`. Exit 0.

godot_check: 29 scripts, 0 failed.
