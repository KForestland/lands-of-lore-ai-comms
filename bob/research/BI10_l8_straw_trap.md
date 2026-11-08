# BI10 meta duck — L8 straw pit at (4405, 972)

1. Problem. At the owner's pose the straw pit on the Larkhon approach shows its wooden ramps. It should look covered, and walking onto it should trap the player. Report F10 15-45-37.

2. Main chain. Yes. A visible pit on the Darker Jungle path. Not presentation-only: the player can avoid it because it already looks sprung, and a drop with no way out would strand them.

3. Intent. Threaten. A straw-covered pit you trip by walking in. Burroni (guide) also has a later cut-the-rope beat. That beat is not this fix.

4. Player contract. Walk onto what looks like straw. The body drops onto the plate. Afterwards there is a way back to the grass, so it is not a permanent softlock. The rope cut is a later use of prop 533 and is not played here.

5. Exact vs approximate.
- EXACT: assemblies 93 and 94 start absent (word +8 0x1082). Straw 95 stays drawn (word 0x401, not solid, so its quads are not a floor). Control 112's mode-0 stakes stay (word 0x481). Its plate is the floor of the hole at y=-65. Region 3255 group 1902 opcode 16 stores 1 at control 112 byte +0x25. Group 13046 links 93 and 94 only when that byte is 1 and a kind-6 event with caller byte 7 arrives. That caller is not known. Group 12994 (control 112 kind 5 value 4) is the step-on of the bottom plate: link prop 533 (word 0x5482, starts absent), sound on 95, opcode 9 arm 2 releases the player from 95, opcode 18 on 112, opcode 9 arm 6 on 533. Opcode 18's reader and arm 6 were not entered.
- APPROXIMATE: keeping the absent ramp meshes and their static_93 / static_94 stakes out of the pack (same presence path as the tree bridge). A walk lid over the straw, because 95 has no solid bit. The lid drops when a grounded walk enters region 3255. The ramp meshes are shown after the body is resting on the plate. Their solid boxes stay off, because those boxes sit on the plate and would cork the landing. A slope from the plate (y=-65) up to the grass of region 3263, reaching y=0 while still inside the pit and then a flat across the edge, is the way out. That slope is not opcode 18 and not group 13046. Grade of the straw-trip story: GUIDE (burroni.txt). Flags and groups: DECODED.

6. Chosen option. (b) Hide the ramps from the absent flag. Adapter for the lid, for showing the meshes only after the drop, for leaving the source solids off, and for the exit slope. Do not play opcode 18, arm 6, or the rope cut. Do not hide control 112.

7. Prove it. Earned walk from the report pose, no jump, into the straw. The body drops onto the plate. Save, reload, then walk the slope back to the grass.
