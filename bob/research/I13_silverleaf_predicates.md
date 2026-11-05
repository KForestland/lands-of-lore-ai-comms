# I13 Silverleaf predicates

Place L16_CA. No frame was opened. No Godot was run. Prop 605, LIKELY template Silverleaf Pyramid, is (2287, 599), height −15, region 6098. Godot (2287, −599). Opcode 14, opcode 198, opcode 20, opcode 5, opcode 7, opcode 16, and opcode 9 were not entered. Predicate left type 5 was not re-entered. The join from a predicate operand to a local cstring stays unbound.

Hintbook lines 4891–4894: a plant bursts from the glass pyramid, and a fireball wafts to the doors. Grade HINTBOOK. That burst is REQUIRED for the northeast tower. These two predicates are the stored gates on the pyramid. The book does not print the entry bytes.

The predicate table has 255 entries of 5 bytes. Entry byte 0 is the operator, byte 1 the left type, byte 2 the operand, byte 3 the right type, byte 4 the literal. The host comment reads operator 6 as 1 only when both sides are nonzero, operator 0 as equality, right type 0 as the literal byte, and left type 3 as the byte at `[0x26E54 + operand]`. This pass did not re-read those VAs. Left type 4 and right type 4 are the nested call already filed: each pushes its operand byte into `0x66AB0`. The host still returns unhosted on right type 4 before it reads the left type.

## Entry 121, `0604780404`

Owner: prop 605, kind 6, group 37986, value 20. The record raw is `060662941400`.

Operator 6. The left operand is 120. The right operand is 4.

| nested | bytes | hosted reading |
| --- | --- | --- |
| 120 | `0003170000` | operator 0, left type 3, operand 23, literal 0 |
| 4 | `0003030000` | operator 0, left type 3, operand 3, literal 0 |

Both sides have to be nonzero, so both equalities have to hold. Operand 23 is the index. Local slot 23's cstring is `Silverleaf_clue`. Operand 3's cstring is `Has_Water_been_started`. The join stays unbound.

The group stores opcode 14 raw `0e03000003000000` and opcode 198 raw `c60000001701`. Opcode 198 byte 4 is 23 and byte 5 is 1. The opcode was not entered. The same index 23 is the predicate operand and this byte.

## Entry 119, `0604cf0405`

Owner: prop 605, kind 6, group 38006, value 20. The record raw is `060676941400`.

Operator 6. The left operand is 207. The right operand is 5.

| nested | bytes | hosted reading |
| --- | --- | --- |
| 207 | `0005000001` | operator 0, left type 5, literal 1 |
| 5 | `0003030001` | operator 0, left type 3, operand 3, literal 1 |

Left type 5 is the host's read of byte +0x25 on the object in `0xB7D80`. That object stays unnamed, and the type was not re-entered. The right side is operand 3 equal to 1. The same unbound cstring is `Has_Water_been_started`.

The group stores two opcode 20 commands on prop 605, opcode 5 byte 4 = 9, two opcode 7 commands, and opcode 16 byte 4 = 2. None of those was entered. No command in this group names the smoke ball.

## The other two records

Group 38056, value 2, predicate entry 208 `0005000002`, is the pair of opcode 9s on ball 602 from I11. Left type 5, literal 2. Group 38086, value 2, predicate entry 209 `0005000003`, is opcode 16 and opcode 7 on the pyramid. Left type 5, literal 3. Those are not the two entries this task named.

## Still open

Whether operand 23 and operand 3 are the local slots. The object whose byte +0x25 left type 5 reads. What opcode 198 stores. What group 38006 plays. No frame.
