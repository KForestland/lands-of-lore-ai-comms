# I20 blue pillars, Scotia, moving pillars

Place L20_BB. No frame was opened. No Godot was run. Static name-at-index stays LIKELY. Opcode 1, 2, 8, 9, 13, 15, 16, and 20 were not entered. No cstring is blue, stair, orb, or faux. No pillar command is opcode 18 or opcode 196.

Hintbook lines 5492–5505: shoot the blue pillars to make a path, then fight the faux-Scotia. A level-five prism spell, Trinity, finishes her. Grade HINTBOOK. Lines 5506–5511: jump the moving pillars. Two stairways lead back up. One fall is not fatal. Grade HINTBOOK. Both are REQUIRED as book steps.

Brady printed 140: destroy the crystals on the ceiling, with a fireball crystal or a level-five Spark, to cross the energy field. Printed 141: leap the moving platforms, get past Scotia, and click the blue orbs. Invisibility or the Ruby of Truth is the Scotia sentence on that page. Grade BRADY. The hintbook's shot pillars and Trinity are not those sentences. They stay separate. The third chamber's moving columns and the stone that stops them are the next room's book text.

## Pillar rows

Static slot 3 is `Fire pillar`. Static slot 4 is `Ice pillar`. Nineteen fire movables and twenty-three ice movables. Every opcode 1 on them names that same movable. Fire pillars: byte 4 = 100 thirty-eight times and byte 4 = 0 thirty-eight times. Ice pillars: the same two bytes, twenty-three times each. Ice pillars also store opcode 16 on themselves with byte 4 = 1 and byte 4 = 0. Movables 57 and 62 are height −50, flags 0x0582.

Five fire pillars stand on y 4299:

| id | native | Godot | region |
| --- | --- | --- | --- |
| 57 | (−3340, 4299) | (−3340, −4299) | 780 |
| 58 | (−3404, 4299) | (−3404, −4299) | 782 |
| 59 | (−3482, 4299) | (−3482, −4299) | 784 |
| 60 | (−3559, 4299) | (−3559, −4299) | 788 |
| 61 | (−3636, 4299) | (−3636, −4299) | 788 |

Three ice pillars stand on y 4462..4463: 62 (−3400, 4463) region 800, 63 (−3503, 4462) region 806, 64 (−3602, 4462) region 808. The other fire and ice rows are scattered from y 2352 to 3483. Nothing in the commands says a shot opens a path, or that a pillar moves.

## The two def-12 actors

Actor 48 is (−3539, 3877), height −50, region 766, flags 0x7582. The definition field is the u16 at byte 32, and that u16 is 1292 (bytes `0c 05`). The low byte is 12. Godot (−3539, −3877). Region 766 is x −3632..−3508, y 3794..4082, floor −50, ceiling 205. Actor 47, definition u16 1, shares that region at (−3576, 3986). Actor 65 stores the same u16, 1292, and is (−2207, 1180), region 74. Godot (−2207, −1180). The cstring `SCOTIA` is in the MIX. It was not joined to definition 12.

Actor 48's groups are opcode 2 `020100002700` and `020230000600`, opcode 8, opcode 13, opcode 9, opcode 20, and one opcode 1 `012034006400` (u16 52, byte 4 = 100). U16 52 fits an actor, a prop, a control, and movable 52. No opcode 3 on L20 contains `d9cd0de5`. That dword is definition 7. The name slot at GLOBAL file 6015177 is `8-Prism`. The name stays LIKELY. Trinity stays the book.

## Two level-change bands

Ten regions store `020100001c53`. Byte 5 stays unread. They form two stacks near x −2620.

| regions | y span | floors |
| --- | --- | --- |
| 1475–1479 | 4185..4343 | 9, 42, 0, 10, 39 |
| 1484–1488 | 3133..3291 | 0, 9, 42, 10, 39 |

No stair cstring. The two stacks are the only level-change owners. They were not walked as the book's two stairways.

## Still open

Which rows are the blue pillars. A path opening. The Trinity cast. Whether the pillars move. Whether the two bands are the stairways. Definition 12's name. No frame.
