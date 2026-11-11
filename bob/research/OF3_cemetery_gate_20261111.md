# OF3. The cemetery gate's clear field drew as a black slab

Owner F10 T23-33-43, "the textures looks not right", at L10 Dc (-167, -966, h 39). The scene is res://scenes/lol2/maps/L10_DC.tscn. The report area says Jungle. That label is OF10. The camera looks at the main gate.

## Grades

| Claim | Grade |
| --- | --- |
| The slab in that view is one vertical face: static assembly 70, material 304, from x -180 to -71, y 14 to 57, z -1019 | PROVEN. L10_DC area.json. No other vertical face of that size sits in front of the camera |
| Material 304 is the gate mechanism on a clear field. 7854 texels are opaque and 8721 are alpha 0. It is on the pack cut-out list | PROVEN. d44346eb11c0f54203ff.png, alpha_cutout_materials |
| The static mesh never draws assembly 70. l10_main_gate.gd rebuilds those faces and did not set alpha scissor, so the clear field painted black | PROVEN. act2_map.gd excludes source index 70. The presenter before this patch set no transparency |
| The two material 539 faces on the same assembly are opaque and stay opaque. Movables 72 and 73 (materials 302 and 303, the skull) already take the hinge cut-out path | PROVEN. Face records. act2_progression.gd sets scissor when the material is on the list |
| The closed gate still blocks on the full quad. The pack UVs stay 0..1. This patch does not rescale them | PROVEN. The presenter still builds the trimesh from the whole face. The test checks transparency only |
| Assembly 70 now draws material 304 with alpha scissor and the two 539 faces without it | PROVEN. tests/l10_main_gate_cutout_test.gd. PASS, exit 0, no script error |

## What changed

`scripts/lol2/l10_main_gate.gd` sets alpha scissor at 0.5 when the face material is on the pack cut-out list.

Commit 18b1b9bd5cc34052935953858260e33907404c99 on grok/of9. Piece 0513. Registry order 752. Lead runs tools/build_deviations.py build. This lane did not.

`/tmp/godot_dummy.sh --headless --path ~/opus_work/lol2_grok_of9 --script res://tests/l10_main_gate_cutout_test.gd`

Printed `PASS gate cutout: assembly 70 draws cut-out 1 and solid 2`.

godot_check: 18 scripts, 0 failed.
