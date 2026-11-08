# BI10 meta duck — L8 straw pit at (4405, 972)

1. Problem. At the owner's pose the straw pit on the Larkhon approach shows its wooden ramps. It should look covered, and walking onto it should trap the player. Report F10 15-45-37.

2. Main chain. Yes. A visible pit on the Darker Jungle path. Not presentation-only: the player can avoid it because it already looks sprung, and a real drop with no stairs would strand them.

3. Intent. Threaten. A straw-covered pit you trip by walking in. Burroni (guide) also has a later cut-the-rope beat. That beat is not this fix.

4. Player contract. Walk onto what looks like straw. The body drops into the hole. The hole is dangerous (the guide says save first). Afterwards the stairs exist, so it is not a permanent softlock. The rope cut is a later use of prop 533 and is not played here.

5. Exact vs approximate.
- EXACT: assemblies 93 and 94 start absent (word +8 0x1082). Straw 95 stays (word 0x401, not solid). Control 112's mode-0 stakes stay (word 0x481). Region 3255 group 1902 opcode 16 stores 1 at control 112 byte +0x25. Group 13046 links 93 and 94 only when that byte is 1 and a kind-6 event with caller byte 7 arrives. That caller is not known. Group 12994 (control 112 kind 5 value 4) is the step-on of the bottom plate: link prop 533 (word 0x5482, starts absent), sound on 95, opcode 9 arm 2 releases the player from 95, opcode 18 on 112, opcode 9 arm 6 on 533. Opcode 18's reader and arm 6 were not entered.
- APPROXIMATE: keeping the absent ramp meshes and their two type-1 stakes out of the pack (same presence path as the tree bridge), and a walk lid over the straw because 95 has no solid bit. The ramps are shown when a grounded walk enters region 3255. That is not group 13046. It is the stand-in for the unentered motion, and it is what keeps the source stairs available as the way out. Grade of the straw-trip story: GUIDE (burroni.txt). Flags and groups: DECODED.

6. Chosen option. (b) Hide and collide the ramps from the absent flag. Adapter for the lid and for revealing the stairs on the walk-in. Do not play opcode 18, arm 6, or the rope cut. Do not hide control 112.

7. Prove it. Earned walk from the report pose, no jump, into the straw centre, body down in the pit, stairs present, save/reload, then walk back to the grass.
