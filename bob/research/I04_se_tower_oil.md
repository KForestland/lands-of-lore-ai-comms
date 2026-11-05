# I04 SE tower oil

Place L16_CA. No frame was opened. No Godot was run. Template and static names are the same L16 runs as I03. Name-at-index stays LIKELY. Opcode 1, opcode 3, opcode 9, and opcode 18 were not entered. Target u16 0 is not the player.

Hintbook lines 4911–4920: float the canal to a stair, leave the west doors open, ignite the oil under a head statue, take the bow that appears, and retreat east. Lines 4931–4936: the Dark Bow drains like the Dark Sword, and do not surrender the blue bow. Grade HINTBOOK. Brady printed 127: spark the oil only after the door pairs are left open, run, leap the canal, and the water is what saves you. The Dark Bow under the head is the challenge grab. Printed 233 repeats the spark, the run, and the grab. Grade BRADY. The escape is REQUIRED. Brady calls the bow a challenge. The hintbook says take it.

## The oil strip

Prop 392, LIKELY Oil fountain, is stored (−2201, −12864), height −5, region 3661, flags 0x4402. Godot (−2201, 12864). Region 3661 is floor −5, ceiling 200, about x −2227 to −2148 and y −12881 to −12846.

The same floor and the same 35-unit y span continue west through three regions:

| region | x span | what sits there |
| --- | --- | --- |
| 3661 | −2227..−2148 | prop 392, the fountain |
| 3665 | −2451..−2227 | the join |
| 3663 | −2670..−2451 | item 24 and prop 169 |
| 3620 | −2929..−2670 | prop 609, and the west neighbor is 65535 |

Item 24, identity 0xD58C34FE, is the placed Darkbow. Definition 35, name slot `36-Darkbow`, stays LIKELY. Stored (−2546, −12858), height −5, word 10 = 3663, flags 0x1002. Godot (−2546, 12858). No opcode 3 of `fe348cd5` is in the L16 JSON. The bow is already placed. A command that makes it appear was not found.

Prop 169, LIKELY Light Source, is (−2496, −12864), height −5, region 3663, event 0. Prop 609, LIKELY Additive Ancient!, is (−2840, −12865), height 15, region 3620. Its groups are opcode 18 on itself, words (−2840, −12865, 0), flags 0x0804, and opcode 9 on itself, byte 4 = 2. No template name in the 136-name run is head. No statue prop stands on this strip. The floating head stays UNKNOWN.

## What the fountain names

Prop 392 kind 9 group 14558, value 0:

| opcode | raw | target | note |
| --- | --- | --- | --- |
| 9 | `090418000300` | u16 24 | byte 4 = 3. Index 24 is item 24 and also actor 24, prop 24, control 24, and movable 24. Ambiguous. |
| 1 | `012062006400` | movable 98 | byte 4 = 100. Fire door (684, −12855), region 10210, event 0. |
| 1 | `012051006400` | movable 81 | byte 4 = 100. Sm fire door (63, −13262), region 6813, event 0. |
| 1 | `012050006400` | movable 80 | byte 4 = 100. Sm fire door (222, −13264), region 6819, event 0. |
| 198 | `c60000000b01` | 0 | byte 4 = 11. The only opcode 198 on L16 with byte 4 = 11. Local slot 11 is the cstring `Fire_puzzle_triggered`. The binding was not entered. |
| 9 | `090360021500` | prop 608 | byte 4 = 21 |
| 9 | `090388010200` | prop 392 | byte 4 = 2 |

Prop 608, LIKELY Altar, is (−2534, −13476), region 6567. Its group 38508 is opcode 9, byte 4 = 3, on Fire Burst props 637–640 and on Wall o Fire controls 185–189, then opcode 9 byte 4 = 21 on altar prop 607. Prop 607 at (−2355, −13447) then has opcode 18 on those same nine objects, flags 0x0800. Bit 0x0004 is clear, so that is not the direct-relocation form. Burning the oil is these stored names. The effect of opcode 9 and of flag 0x0800 stays open.

## The door grid

Movables 122–169 are LIKELY FireWall Door, flags 0x0582, eight columns at x −1937, −1639, −1339, −1088, −838, −539, −290, and −14. Each column has six doors, at y −12550, −12600, −12825, −12875, −13100, and −13150. That is three east-west bands. Group 14558 does not name these indexes.

Movable 122 was the one pair copied. Kind 4 group 50380 is opcode 9 byte 4 = 21 on movables 122 and 123. Kind 6 group 50398 is opcode 16 and opcode 1 byte 4 = 100 on 122. Group 50416 is opcode 16 and opcode 1 byte 4 = 0 on 122. The predicates differ (`0413ce00` and `0413cf00`). Opcode 1 was not entered. The other forty-six doors were counted and not copied.

Movables 95–97, the three FireWall Doors at x 1704, y −12841, −12891, and −12791, have no events. Prop 603, Ball O Smoke, at (429, −12857), region 6775, has opcode 18 words (1703, −12835, 0), flags 0x0812, the same shape as the NE ball. Bit 0x0004 is clear.

## The blue bow

No L16 template, static, or item name is blue bow. The catalog name for the placed bow is `36-Darkbow`. The hintbook's blue bow is the ice-cave melt at lines 4240–4245, and line 4935 says not to surrender it. No L16 command stores that surrender. The rule is HINTBOOK. It is not a row on this level.

## Still open

The head mesh. Whether u16 24 is the Darkbow. Opcode 1 on the doors. Opcode 9 as the burn. Flag 0x0800. The other forty-six door bodies. No frame.
