# I14 subterranean caverns

Place L17_HC. No frame was opened. No Godot was run. Template names are the 38-byte table in the metadata entry, 42 names. Static names are the 30-byte run whose slot 7 is `Teleport circle`. Name-at-index stays LIKELY. Opcode 1, opcode 6, opcode 9, opcode 16, opcode 18, and opcode 198 were not entered. A level-change shape is `020100001c`. Byte 5 stays unread.

Hintbook lines 5363–5369: run for the mapped exit, and side trips only when the tunnels are crowded. The Lizard is harder to trap. Lines 5375–5378: the other choice is to reach the exit first, then fight. Grade HINTBOOK. Lines 5383–5398: in the exit room, cut the red strands on the west wall, get pulled into the beast, click left and attack, click the middle green frond, wait while a spider repairs it, then cut the next red strands and enter the laboratory. Grade HINTBOOK. The run and the cut are REQUIRED. Killing spiders is the book's optional fight.

Brady printed 234, steps 18–22: run to the Hive Mother, hack the fleshy columns, attack the valve, click the decaying organ, wait for a Hive Guardian to transplant a new one, then take the opening into Belial's Chambers. Grade BRADY. Those nouns are not the hintbook's strands and frond. The two sentences stay separate. Both routes are REQUIRED in their own book.

## Stored exits

No cstring is `spider`, `strand`, or `frond`. The book's enemies and the west-wall strands stay UNKNOWN as placed rows.

Four level changes. Byte 5 is not a level name.

| owner | place | command | byte 5 |
| --- | --- | --- | --- |
| movable 50, LIKELY Teleport circle, kind 5 group 3896 | (1439, 7256), height 135, region 118. Godot (1439, −7256). The quad is x 1359..1519, y 7175..7337, floor −15, ceiling 140 | `020100001c50` | 0x50 |
| kind 12 region 1312, group 1632 | x −5632..−5240, y −5826..−5779, floor 0, ceiling 90 | `020100001c33` | 0x33 |
| kind 12 region 1313, group 1638 | the quad directly south, y −5873..−5826, same floor | `020100001c33` | 0x33 |
| kind 12 region 1318, group 1644 | x 8186..8509, y −2370..−2100, floor −30, ceiling 90 | `020100001c70` | 0x70 |

Group 3896 also stores opcode 198 raw `c60000000000` (byte 4 = 0, byte 5 = 0), opcode 16 on movable 50, opcode 9 byte 4 = 17 and opcode 6 byte 4 = 2 and opcode 16 on props 310, 309, 308, and 307, and opcode 1 byte 4 = 0 on movable 50. A second record, kind 6 group 3878 value 20, is opcode 1 byte 4 = 100 on movable 50 and opcode 16. The opcode was not entered.

Those four props, LIKELY the crystals, sit on region 118's neighborhood:

| prop | template | native | Godot |
| --- | --- | --- | --- |
| 310 | Yellow Crystal | (1561, 7144), region 121 | (1561, −7144) |
| 309 | Red Crystal | (1308, 7145), region 114 | (1308, −7145) |
| 308 | Green Crystal | (1308, 7382), region 122 | (1308, −7382) |
| 307 | Purple Crystal | (1561, 7379), region 121 | (1561, −7379) |

## The one relocation

Kind 12 on region 1293, group 1566, is the only opcode 18. Target 0, words (−6084, −6404, 0), flags 0x0005. Bit 0x0004 is set. Target 0 is not the player. The words land in region 1259, floor 0, ceiling 120, x −6154..−6064, y −6461..−6379. Region 1293 itself is a different quad, y −6022..−5980. This is not one of the level changes.

## Organic rows

The gut templates are Wide guts, Long guts, Gut stub, Intestine, and Hive Duct. Sixty-seven props use them. Thirteen have events. Prop 99, LIKELY Wide guts, is (−6243, −5890), region 1302, four events. Prop 153, LIKELY Hive Duct, is (−4993, −7063), region 79, four events. Neither name is a strand or a frond. The book's west wall and the Brady valve stay those sentences.

## Still open

Byte 5 of all four level changes. Which of the four is the mapped exit. The red strands, the green frond, the valve, and the organ as meshes. Spider colors. No frame.
