# H18 Temple L14: spider floor, quill, portal doors

Three owner rows in `TRIAGE_20261103.md`. `L14_HT.MIX` sha256 prefix `c294f9ab142b55c3`. JSON `L14_HT.json`. Godot y in the reports is the native y with the sign flipped.

## Spider, 18:02:30

Report Godot (3061, −5374), native (3061, 5374). The note says the spider burrows through the floor and opens a tunnel.

No `Spider` or `spider` cstring is in this MIX. No opcode 196 is owned by an object within 500 of that point. The objects on that spot are the ceilings:

- Control 81, native (3052, 5484), height 141. Kind 5 value 4, group 17740: opcode 16 byte 4 = 2 on u16 81. Kind 5 value 1, predicate `0005000001`, group 17746: opcode 2 `020100001100` (arm 0x11, not arm 0x1C). Kind 6 groups 17752 and 17770: opcode 9 byte 4 = 6 on u16 81 and u16 80.
- Control 80, native (3051, 5226), height 141. Kind 6 value 7, group 17658, also opcode 9s a run of prop indexes and opcode 20 on u16 82. Kind 5 value 1, group 17728: the same arm 0x11. Kind 5 value 4, group 17734: opcode 16 byte 4 = 2 on u16 80.

Those groups match the MIX. Arm 0x11 and opcode 9 were not entered. Left kind 5 was not entered. HINTBOOK and BRADY have no burrow sentence in the passages searched. The tunnel stays open.

## Quill, 18:04:58

Report Godot (2251, −5103), native (2251, 5103). The note says the quill opens the door or tunnel in front of the player.

BRADY 4964-4965 and 8162-8163: ignite the candle and the lamps with Spark, then click the feather quill. A secret passage opens. No `quill` cstring is in the MIX. The cstring `Inkwell` is at file 11882569.

Prop 344 at (2211, 5110), height 125, is the object at this report. Group 13364, file 11725946, MIX match, six commands:

- opcode 9 byte 4 = 0x0d on u16 91
- opcode 5 byte 4 = 1 on u16 350 and on u16 343
- opcode 196 `c4904e066400000a` region 1614 toward floor 100, speed 10
- opcode 196 `c4904e06c800010a` region 1614 toward floor 456, speed 10
- opcode 196 `c4906510be00010a` region 4197 toward floor 190, speed 10

Opcode 5 and opcode 9 were not entered, so the lamp indexes are not proven to be "ignite." The floor writes are the passage motion in this group. Prop 8, a switch at (2245, 5209), groups 116 and 146, opcode 1 byte 4 = 0 and then 100 on u16 0 and u16 1. Movable 0 (2264, 5312) and movable 1 (2264, 5230) have no events. Index 0 and 1 also fit other tables. The secret passage is OPTIONAL in Brady's "other things to do."

## Portal doors, 18:10:50

Report Godot (−310, −2304), native (−310, 2304). The note says the doors are teleporters and their textures clip into the main map.

Movable 88 at (−305, 2132), height 190, region 1459, and movable 89 at (32, 2061), height 190, region 1461, have no events. Neither owns a level change. The clip is a render report and was not a script. The level's arm 0x1C commands are elsewhere: stream 0 groups 1462 and 3836 are `020100001c68`, and stream 1 group 9210 is `020100001c30`. Byte 5 stays unnamed. They are not events of these two movables.

## Opens

- What arm 0x11 does on the ceilings. No spider row.
- Whether opcode 5 on u16 350 and 343 is the lamp-lighting the book names, and which floor word is the open passage.
- A destination for byte 5 = 0x68 and 0x30.
- No longplay frame was opened.

## Grades

BRADY 4964-4965 and 8162-8163 for the quill passage. DECODED for controls 80 and 81, prop 344 group 13364, prop 8, and movables 88 and 89 having no events. The burrow and the teleporter stay open. FRAME open.
