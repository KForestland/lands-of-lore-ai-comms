# BG13 — Jungle gate planks

Base `c9295da`, after BF01–BF07 and BG00a through BG12. Patch `patches/ACT3P2/BG13_jungle_gate_planks.patch`. Not applied to the live tree.

Owner r17 16-39-14 at Jungle (-1176, -5247), body height 32, looking down: two plank paths lie on the grass in front of the still-standing village doors. Those are fallen leaves, controls 80 and 81, template 74. Placement flags are 0x1082, which includes bit 0x1000, so they start absent. `jungle_gate_leaves` already hides its own copies until Force gate links them. The static batch was drawing the same two assemblies at load. They are now managed presence, so the absent bit keeps those copies hidden. The gate-leaf host remains the drawer. Their collision boxes are 2 high and marked scripted, so they were never solid.

A Human walked from (-1080, -5247) to (-1176, -5247). Both doors were up and both planks were gone. E on the closed south door was refused. After the Huline alert and Killed_Confidante, E on each door laid that door's plank. The static copies stayed hidden.

Printed rendered, display :2, 18.76s:

`PASS gate planks: walked to (-1176,-5247), the two planks were gone while the doors stood, and forcing both doors laid the planks down`

Ledger `--check` is 408 pieces. The stack from BF01 through BG13 applies on `c9295da`.

Grade: Adapter (owner rule 2026-10-30). The native 0x0800 producer stays unread. Force gate is the existing consumer.
