# I27 L8 tree bridge

Owner report 23-23-53, F10 (5063, 1888). F10 map Y is native Y with the sign flipped, so the native point is (5063, −1888). That point is region 3206, floor 0, ceiling 200, bbox (4914, −2012)–(5121, −1852.1). Brady printed 210, step 51: knock over a tree, cross the log, jump to another log, and jump from the tree to cross the chasm to the Larkhon. Grade on that sentence is BRADY. r14 `8732a39` has `l8_tree.gd`, and that file is the five-torch platform around native y 2146–2595. It does not reference this chasm. No Godot was run.

## Records

Static names are the 30-byte run at L8 file 13805419, name at byte 0. The join is LIKELY. Index 12 is the cstring `Tree standing ` with the trailing space. Index 10 is `Tree Bridge`. Index 11 is `Little Branch`.

| object | native | height | region | static byte | events |
| --- | --- | --- | --- | --- | --- |
| control 114 | (5096, −1916) | 0 | 3206, floor 0, ceiling 200 | 12 | kind 4, stream 1 group 13090, value 0, no predicate |
| control 116 | (5252, −1908) | 0 | 3300, floor −550, ceiling 200 | 10 | none |
| control 115 | (5396, −1907) | −9 | 3297, floor −179, ceiling 200 | 11 | none |
| prop 1014 | (5101, −1799) | 0 | 3209, floor 0, ceiling 200 | 44, LIKELY `Ameranth Indent` | kind 6, stream 1 group 8706, value 20 |

Group 13090, the only group on the standing tree:

- opcode 9 on prop 115, byte 4 = `0x15`, raw `090373001500`. Prop 115 is stored at (4680, −1351), static byte 15, LIKELY `Trap Top`.
- opcode 9 on prop 1014, byte 4 = `0x15`, raw `0903f6031500`.
- opcode 20 on prop 1014, raw `1403f6030c0380011f3e`. Not entered.
- opcode 9 on control 116, byte 4 = 3, raw `091074000300`.
- opcode 9 on control 114, byte 4 = 2, raw `091072000200`.

Opcode 9 was not entered, so byte 4 is only the stored byte. Group 8706 is opcode 20 on prop 1014, raw `1403f6035f01ff111f3e`, also not entered. No opcode 18 destination lies within 900 units of the chasm. The knock-over is not the direct-relocation form.

## What the port does

Nothing in r14 handles control 114, group 13090, or these three static slots. The owner can stand in region 3206 and the tree does not fall. The book’s walk across the log is control 116’s name plus the two opcode 9 bytes aimed at it. The fall motion itself was not read.

## Still open

Opcode 9 and opcode 20. Whether byte 4 = 2 lays the tree down. Prop 115 is named by the group and sits hundreds of units away. No frame was opened.
