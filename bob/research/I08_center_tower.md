# I08 center tower

Place L16_CA. No frame was opened. No Godot was run. Names are the I03 tables. Name-at-index stays LIKELY. Opcode 1, opcode 2, opcode 3's grant, opcode 8, opcode 9, opcode 13, opcode 18, and opcode 198 were not entered. Target u16 0 is not the player.

Hintbook lines 5250–5268: after the four raises, enter the center tower, fight the last faux-Belial up close, and walk into the horizontal bars of light. That is the mantle. Grade HINTBOOK. Brady printed 131: the raised tower's black entrance, the third Belial, then the far door. Grade BRADY. The fight and the walk are REQUIRED. No stored count of four gates this door.

## The hall

The mantle cluster is x about 5300–5800, y about −9900 to −9600. Four props, LIKELY Mantle, height 10, flags 0x0002, event 0, regions floor 0, ceiling 200:

| prop | native | Godot | region |
| --- | --- | --- | --- |
| 331 | (5443, −9749) | (5443, 9749) | 223 |
| 332 | (5578, −9751) | (5578, 9751) | 228 |
| 333 | (5636, −9879) | (5636, 9879) | 214 |
| 348 | (5384, −9879) | (5384, 9879) | 215 |

Six props, LIKELY Lightning, height 0, sit on the same cluster: 129 (5445, −9840), 130 (5750, −9840), 131 (5628, −9602), 132 (5439, −9627), 133 (5308, −9784), and 134 (5658, −9782). Prop 129's own group is opcode 9 on itself, byte 4 = 2. No placed item is named mantle. Static Mantle Gate has zero placements.

Kind 12 on regions 217 and 218, the south edge of that cluster (y −9963 to −9813), stores opcode 198 byte 4 = 12 and four opcode 18 commands, one on each mantle. Local slot 12 is the cstring `Mantle_conveyed`. The opcode was not entered. Kind 12 timing is I31.

Each opcode 18 has flags 0x0112. Bit 0x0004 is clear, so this is not the direct-relocation form. Bit 0x0100 is set, so the word at +8 is the height field. The height word is 40.

| target | words |
| --- | --- |
| 331 | (5334, −9622, 40) |
| 332 | (5713, −9617, 40) |
| 333 | (5809, −9893, 40) |
| 348 | (5201, −9893, 40) |

No opcode 198 on L16 has byte 4 = 1. Local slot 1, `Got_mantle`, is not that byte. The walk-in stays the book's sentence plus these stored bytes.

## The actor north of the bars

Actor 45, definition u16 1282, is (5522, −7968), height 0, region 9311, 14 events. The short L16 actor-def labels in the earlier pack are VISC, HL3, bacl16, and B_HUMAN. None is Belial. This pass did not read a new name for definition 1282.

Movables 84 and 85, LIKELY Jack's Door, are (5476, −7783) and (5562, −7783), region 9654. Group 49752 names actor 45 with opcode 9 byte 4 = 3, opcode 3 identity 0x15D29D6D byte +8 = 1, and opcode 9 byte 4 = 21. The identity is not in the item notes read this pass. The same group has opcode 18 target 0, words (5511, −7858, 0), flags 0x0a81. Bit 0x0004 is clear. Movables 99 and 100, the Jack's Doors at y −6404, have events and were not copied. A sparkling door was not a stored name.

Prop 377, LIKELY Light Source, at (1629, −4225), is the owner of the three groups whose opcode 198 byte is 13. Local slot 13 is `Belials_access`. That prop is not in this hall. The opcode was not entered.

## Still open

The fourth-raise gate. Definition 1282's name. The opcode 3 identity 0x15D29D6D. Opcode 18 flag 0x0112. Kind 12 timing. No frame.
