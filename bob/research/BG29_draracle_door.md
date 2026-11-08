# BG29 Draracle corridor door

Owner r17 16-25-58, Cave (-62, -17617), "the door in front of the Draracle is missing".

Grade DECODED for the records and the closed start. LONGPLAY only for the sampled frames: 5:06 is the cave mouth, and 13:20 shows the red Draracle in the arch with no leaf because the player is already in the chamber. The 5-second sample does not show a closed leaf. The hintbook says see him twice and does not name this door.

The missing door is L1_DC movables 74 and 77. Static names: 74 is the left door (template 11) and 77 is the right door (template 10). Each is a 64 by 12 by 128 box, resource 478 on the four side faces, word 0x0582, drawn and solid from the start. Placement is x -98 and -34, native y 17741, height -295, heading 32768. Together they cover x -130 to -2, in front of the player at x -62. The hosted doors 75 and 79 are the other pair. Static assemblies and static collision do not contain this arch.

Kind-4 use, predicate 206 (owner state 0), runs opcode 1 byte 4 = 100 on both leaves. Predicate 207 (state 1) runs opcode 1 byte 4 = 0. Byte 34 is 6, so opcode 1 is the proven rotary path. The angle word is 21845. First use sets travel 21845. Second use of that same leaf returns it to 0. A third use of that leaf matches neither predicate. Initial constructor travel is 0, so the leaves start closed.

The hinge corner is the mode table. Door 74 is mode 7 (odd, pivot at world (-130, 17747)). Door 77 is mode 4 (even, pivot at world (-2, 17747)). Mode 4 is in the composed check. Mode 7 uses the same corner table the hinge replay checked for every mode. Open, the leaves leave x -62 clear. The pose snaps. The swing clock at +0x55 is not modelled. Opcode 16 stays unread. Opcode 197 targets region 1906, which is not in the blocker pack, so it does not stop the walk.

Earned walk: from native y 17690 at x -62 the closed leaves stopped the body, a forward ray hit a leaf, the use set travel 21845, and the walk continued past the door line. PASS door: walked the corridor at (-62,-17617), the leaves stopped the walk, and the use opened them.

Patch `grok_research/patches/ACT3P2/BG29_draracle_door.patch`, ledger piece 0341. Unapplied. Applies to r18-work 3b6a929.
