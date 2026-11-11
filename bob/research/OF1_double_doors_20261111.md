# OF1. The double doors face the wrong way

Owner F10. Cave T22-33-46, "the left door is facasing <- should be faceing ->", at (-58, -17638, h -261), looking at the Draracle doors. Jungle T22-47-41, "the left door is <- should be ->", at (-1270, -5249, h 32), yaw 1.55, with the line "The village gate is closed." Same bake on both.

## Grades

| Claim | Grade |
| --- | --- |
| A type-0 box face picks its orientation from surface byte +6. The renderer dispatch is `(flags >> 6) & 3`. Bit 0x40 is mode 1, which swaps the two top corners against mode 0 | PROVEN. `verify_door_uv_orientation.py` runs that dispatch for all 256 flag bytes. The 0-to-1 panel this port draws is the same full-face approximation the other doors already use |
| The bake mirrors box face 3 and no other face, whatever the byte says | PROVEN. `export_map_movables.py` sets `_QUAD_UV_FACE3` when `fi == 3`. The village gate prepare script uses that line |
| Draracle leaf 74, template 11, the source name "left door", stores 0x40 on face 2 and 0 on face 3. Leaf 77, template 10, stores 0x40 on face 3 and 0 on face 2 | PROVEN. L1_DC.MIX child slots, resource 478 |
| He stands at map z -17638 looking toward -Z, so the near side of both leaves is face 3 (z -17735). Leaf 74's near side was mirrored and the byte says it is not. Leaf 77's near side was mirrored and the byte says it is | PROVEN. Placement and the earned test. After the swap, texture u on leaf 74's near top edge increases toward screen right. Leaf 77 still increases toward screen left |
| Village leaves 78 and 79 are the closed gate under that hint. Leaf 78, template 6, stores 0x40 on the broad face 2 and 0 on face 3. Leaf 79, template 5, stores 0x40 on face 3 | PROVEN. L4_HJ.MIX |
| From his stand, x -1270 looking -X, the near side is the greater x. That is face 3 of both leaves. Leaf 78's near side was mirrored against a clear bit. Leaf 79's near side already matched 0x40 | PROVEN. The earned test. Leaf 78 is the screen-right leaf (hinge toward -Z). Leaf 79 is the screen-left leaf and was not the one the bake had backwards |
| The screen-left village leaf should be mirrored the other way from the flag | Not found. The bit on the face he can see is already what the bake drew. The leaf the bit moves is 78 |

## What changed

Leaf 74's source UVs for faces 2 and 3 are swapped, closed and open, so face 2 is the mirrored panel and face 3 is not. The village gate reader mirrors U on leaf 78's two `material_0742` faces, which is the same swap on the baked panels. Collision, hinge, and the open pose are untouched.

`/tmp/godot_dummy.sh --headless --path ~/opus_work/lol2_grok_of9 --script res://tests/of1_double_door_facing_test.gd`

Printed `PASS double doors: Draracle leaf 74 and village leaf 78 follow surface byte +6, the matching leaves stay`.

Piece 0511. Lead runs tools/build_deviations.py build for 0359, 0507, 0508, 0509, 0510 and 0511.
