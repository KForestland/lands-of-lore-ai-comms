# R116 review: L13 pad and vault opener at 791fd4a

Verdict: MERGE.

Head `791fd4a3b1644ac73bc1290ff68adc703656c49c`, single parent `1b1177cd61b49d1a43c3c727a5e323a4e237378a`, subject "Host Citadel vault use and native teleporter step events." The diff is 17 files, 551 insertions and 6 deletions. It does not touch `act2_progression.gd`, `native_script_host.gd`, `act2_map.gd`, player scripts, or geometry. The only owner change is one late row in `scripts/lol2/area_owners/L13_RC.gd`: `generic_object_actions.gd`, needs progression. The catalog count goes from 116 to 117. Restore counts go from 22/8 to 23/9. Ledger 0647 and the DEVIATIONS row name the height adapter. Pink headroom is not in this diff.

## Source

Control 53 has one event: kind 5, value 4, group 8134, predicate null. The placement centre is Godot (-4955, 1711). Nav region 987 contains that point, and `regions[987][1]` is -900. The pad test uses that value as the floor. Group 8134 is one opcode 18, raw `1201000046f32bea000085040000000a0000`. The signed words are x -3258, native y -5589, height 0, flags 0x0485. Flag 0x0100 is absent, so the pose keeps the current height. Region 1166 is the only quad that contains (-3258, 5589), and `regions[1166][1]` is 0. `fire()` then sets the body y to that floor plus 32, so the body lands at (-3258, 32, 5589). That adapter is the 0647 row. The opcode is unchanged.

Prop 250 has kind-4 group 4366 with predicate entry `0005000000`, and kind-4 group 4456 with `0005000002`. Group 4366 enqueues movable 84. Movable 84 kind-6 group 9904 is opcode 16, then opcode 1 `012054006400` (byte 4 is 100). Placement mode byte 0x22 is 2, and angle byte 0x24 is 95. `GenericCatalog.movables` is empty outside L10, so this mover uses the existing non-rotary `_pose`. Travel 95 over angle word 95 is fraction 1, and the slide length is the existing bounds axis plus 8. Sprite record 250 sits at [-4534, -1040, 1767], left -33, right 33, bottom 0, top 89. The billboard centre is (-4534, -995.5, 1767). Reach is 256 along that rectangle, and a solid in the way blocks it. Loading while already on the pad seeds the latch and does not fire.

## Robot

Graded folder `robot/L13_RC/20261113_791fd4a-r116b`. Private display :324, Dummy audio, one Godot of this worktree. Clock `Engine.time_scale = 4` and `physics_ticks_per_second = 240`. F2 pin `c15_l13_rc`, sha256 `21db5d3f9596650ad96df594e103eca6eb79dea299d91e585e610b146622b948`. Boot set health from 27 to 30 once. Body fit stayed on. GREEN 13, RED 0, BLOCKED 0, deaths 0, stops 0, resets 0. An earlier F5 file is copied back onto slot 1 so the real F9 key can load it.

| Check | Result |
| --- | --- |
| Step onto control 53 | (-3258, 32, 5589), region 1166, on the floor, resets 0 |
| F9 of the landing F5 | same pose |
| F9 of the stand F5, then a second step | back at the stair stand (-4867, -874, 1702), region 1232, then the same landing again |
| E and left click from 581 away | hinge stays (-4426, -1040, 1753), byte25 0, travel word absent. Prompt is not the opener |
| Off-aim click at the stand | hinge stays shut, byte25 0, attack icon down |
| Aimed E | screen "The vault mechanism moves." Travel 95, byte25 1. Hinge 84 moves from (-4426, -1040, 1753) to (-4354, -1040, 1878), 144 units |
| F9 of the open F5 | travel 95, byte25 1, same hinge, gap 0. A second E leaves travel 95 |
| Closed F9, then aimed left click | click moves the hinge the same 144 units to (-4354, -1040, 1878), travel 95, byte25 1, attack icon down |

The arrival frame is the stone chamber at H 32. The opener frame shows the use line and "The vault mechanism moves." The floor drawing in that view changes between the before and after shots.

`field()` returns -1 when the travel word has never been written. A shut opener has byte25 0 and no travel word. The first folder, `robot/L13_RC/20261113_791fd4a-r116`, required travel 0, so its outside-reach, off-aim, and closed-load rows are RED, and it returned before the left click. The hinge in that folder did not move on the far inputs, and the closed load put it back at (-4426, -1040, 1753). The graded pass is r116b.

Pink headroom stays with Opus. This lane does not apply the merge.
