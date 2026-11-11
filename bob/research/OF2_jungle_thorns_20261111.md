# OF2. Jungle thorns grow back as the full roots

Owner F10 at Jungle (-3632, 2229, h -38), reports T23-00-41 and T23-01-17. He cut a wall with the sword. The roots did not grow back visibly, and the wall was still there. The stand faces L4_HJ control 103, template 10. The same host covers controls 101-109.

## Grades

| Claim | Grade |
| --- | --- |
| Control 103 is the wall in front of that stand. Its box is about x -3678..-3568, z 2158, y -70..60 | PROVEN. static_collision_L4_HJ.json placement x -3623, y -2158, h -70, width 110, depth 1, height 130. Godot puts native y on -z |
| Selector 5 draws material_0756, about 8% opaque. Selectors 0, 1 and 2 are the root pictures (about 88%, 82% and 70%). Selector 3 is the open cut, about 10% opaque, and it is not solid | PROVEN. Assembly 103 faces. Mask 1 is material_0767, mask 32 is material_0756, mask 8 is material_0770. Alpha counted on the PNGs, threshold 16 |
| The timer group sets the solid bit and selector 5. Kind 6 caller 2 then stores selector 0 and state 0 and does not clear the solid bit | PROVEN. Control 103 group 22540, kind 2, predicate owner state 3, value 16, file offset 12767818. Commands: opcode 9 arm 0x11, opcode 9 arm 7, opcode 16 value 4, opcode 5 value 5. Group 22600, kind 6, value 2, predicate owner state 4, file offset 12767832. Commands: opcode 7 index 2, opcode 7 index 1, opcode 16 value 0, opcode 5 value 0. No opcode 9 in that group |
| Applying those two writes when timer 0 expires is the adapter. Opcode 7 in group 22600 is not played. Who pushes caller byte 2 was not traced | PROVEN as the patch. The caller is UNKNOWN. Kind 6 runs only when a caller byte matches. Opcode 9 arm 0x15 enqueues caller 0x14, not 2. Group 22600 is the only write back to selector 0 on these controls |
| A saved state 4 is the stuck packet. Restore shows selector 0 before the box comes back | PROVEN. validate() still accepts state 4 with selector 5. restore() rewrites that row to state 0 and selector 0 |
| Three cuts at the reported stand open the wall, the walk crosses, the roots and the box come back together, the return walk sticks, and Spark still burns it open | PROVEN. tests/jungle_bramble_earned_test.gd on Xvfb display :241. PASS, exit 0, no resource line. Headless leaves the mouse visible, so world_active() is false and the strike does not fire. The rendered run is the one that counts |

## What changed

`scripts/lol2/jungle_bramble.gd` keeps the sword path. When timer 0 expires in state 3, the solid bit and flag 0x4000 are set, then state and selector become 0. A restored state 4 takes the same picture. The collision still follows the solid bit.

Commit 409e10ce0bd7a187742ffd3a0abac3ca4da48931 on grok/of9. Piece 0512. Lead runs tools/build_deviations.py build. This lane did not.

`DISPLAY=:241 /tmp/godot_dummy.sh --display-driver x11 --rendering-method gl_compatibility --resolution 1280x720 --fixed-fps 60 --path ~/opus_work/lol2_grok_of9 --script res://tests/jungle_bramble_earned_test.gd`

Printed `PASS bramble: control 103 at the reported stand opens on the third cut, grows back as the full roots, and Spark burns it down`.

godot_check: 16 scripts, 0 failed.
