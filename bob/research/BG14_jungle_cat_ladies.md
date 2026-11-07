# BG14 — Jungle cat ladies

Base `c9295da`, after BF01–BF07 and BG00a through BG13. Patch `patches/ACT3P2/BG14_jungle_cat_ladies.patch`. Not applied to the live tree.

Owner r17 16-40-18 at Jungle (-698, -4230), body height 68: the clearing should have two cat ladies telling him about the missing cats. That spot is control 186, template 27, movie E056E.VQA (two Huline women). Kind 5 group 26572 sets property 10 = 1, the loiter, and property 7 = 255 so it loops. Aimed E follows property 10 through segments 0, 2 and 4, then opcode 9 property 2 hides them.

Placement flags are 0x1402, which includes bit 0x1000, so the control starts absent. The only link is prop 4620 (a bigleaf at -629, -4783) event 6 value 265, group 17322, opcode 9 property 3. That producer is unread, so the women start present. No command writes owner state 1, so the first E runs the state==1 group and sets state 2. Opcode 16 stores that state and is not a segment id. The strike group 26702 stays unread. The billboard is not a movement solid. A look toward its middle, within 140, starts the talk, and a layer-1 wall in between refuses it.

Frames and voice are local output of `tools/prepare_jungle_cat_ladies_media.py`. They are not in the patch. The lead runs that preparer on the original `E056E.VQA` before the women appear. One source frame has a non-key corner; the key stays (0, 251, 251).

A Human walked from (-900, -4350) along the ground to (-698, -4350) and then to (-698, -4230). The women were loitering. E started segment 0 and the voice.

Printed rendered, display :2, 12.85s:

`PASS cat ladies: walked to (-698,-4230), the two women were loitering, and E started their first talk`

Ledger `--check` is 409 pieces. The stack from BF01 through BG14 applies on `c9295da`.

Grade: Adapter (owner rule 2026-10-30).
