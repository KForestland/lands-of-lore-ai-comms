# OF6. The clipped globe at (-529, -4058)

Owner F10 T23-38-40. "got the orb by cheting clip ture the wall". Origin (-529.21, -4058.43), height 32.04, yaw -0.544. HUD "E Globe taken." He was already inside the room. Item 46, definition 98 `96-E Globe`, sits at (-537, 0, -4079) in region 1492. No globe was spawned. No door was cut into the south wall.

## Grades

| Claim | Grade |
| --- | --- |
| Item 46 is the globe he took. The take from inside the room already worked. The bug was getting in | PROVEN. Placement in act2_items_source.json. The earned test takes `act2:L10_DC:item46` after walking in |
| The south face at z -4286 is three source walls on null-neighbour edges: wall 5503 (region 1444 edge 0, y 0 to 100), wall 5505 (region 1447 edge 0, y 10 to 100), wall 5514 (region 1452 edge 0, y 10 to 100). They form one continuous span, about x -654 to -375, with no south door | PROVEN. L10_DC.MIX geometry, region.neighbors null on those three edges |
| The OF9 probe left those three open because the yard floor (region 405) lies outside them | PROVEN. They are absent from scripts/lol2/l10_void_edges.json for that reason. The extra want-set in act2_map.gd is what puts them on the movement body |
| Wall 5503 is the wall he walked through. His stand is on that wall's x, and the wall is full height from y 0 | LIKELY. The report stores no path |
| Once that face is solid, the only ground entrance is the seam from corridor regions 859 and 860 into 1436 and 1435. A search that blocks that seam does not reach yard 405 | PROVEN. Floor-0 region graph |
| Movables 124 and 125, template 14 "Maus Door", are the partition in that corridor. Each is a solid mode-2 box, 8 by 50 by 100, word +8 = 0x0182. Heading 16384. Motion byte +0x53 is mode 6. The gap beside the pair is 23 wide, so a radius-15 body cannot pass while they stay shut | PROVEN. Placement records. The shut-door ray in the earned test hits |
| Neither movable has events, and no opcode 1 targets them. Prop kind-4 use (opcode 9 arm 0x12) only clears bit 0x40 of byte +0x15. It does not move the leaf | PROVEN |
| Byte +0x52 is the hinge corner (124 stores 2, 125 stores 1). The corner table is the jump at VA 0x63AAE, immediate 0xA20C, and that immediate has no fixup | PROVEN for the bytes and the missing fixup. Which corner the byte selects is UNKNOWN |
| Contact turns each leaf 90 degrees about its southwest corner, Godot yaw -PI/2. That swing leaves a radius-15 lane at z -3795 and keeps the arc off the east approach | PROVEN as the lane the earned test walked. Adapter. The native push byte +0x57 was not hosted, and the corner was not decoded |

## What the test walks

Stand (-513, 32, -4310) is inside the region-405 yard polygon. Rays through 5503, 5505 and 5514 hit. A 240-tick push north stays at z < -4270, origin above 20, resets 0.

Stand (-280, 32, -3795) is the east yard. A ray west through the shut door hits. Contact opens movable 124. The walk then goes (-330, -3795), (-450, -3795), (-510, -3850), (-512, -3924), (-514, -4004), (-514, -4084), into region 1492, and takes item 46. Resets 0.

`/tmp/godot_dummy.sh --headless --path ~/opus_work/lol2_grok_of9 --script res://tests/l10_globe_room_wall_test.gd`

Printed `PASS L10 globe room: walls 5503, 5505 and 5514 hold, the maus door takes item 46, resets 0`.

`tests/l10_map_test.gd` also PASS after the three extra walls and after the door faces left the shell.

Pieces 0509 (the south face) and 0510 (the maus-door adapter). Lead runs tools/build_deviations.py build for 0359, 0507, 0508, 0509 and 0510.
