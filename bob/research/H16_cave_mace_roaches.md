# H16 Cave crates, the mace, and the roaches

Beat 10. `L1_DC.MIX` sha256 prefix `6384ec4d4d78f1aa`. Owner report 17:03:39 in `TRIAGE_20261103.md`: Cave Godot (532, −12371), clipped through the wall, boxes cannot be moved to reach the next floor. That Godot pair is native (532, 12371), inside this crate cluster.

The passage is on the way out of the caves. HINTBOOK 2033-2048: giant cockroaches in the fire room, and in the other chamber stack the boxes, climb to a mace, and use it on the cockroaches. Do not keep the mace. The stack is the book's way up. Keeping the mace is explicitly not the point.

## Crates

Static slots from the 30-byte run at file 7415073: slot 25 `Small crate`, slot 26 `Medium Crate`. The table-start pointer was not read from a header. All seven sit at height −215. None has an event.

| control | static | native x, y | region |
| --- | --- | --- | --- |
| 94 | Small crate | 429, 12278 | 1085 |
| 95 | Small crate | 412, 12264 | 1085 |
| 96 | Medium Crate | 650, 12243 | 1087 |
| 97 | Medium Crate | 623, 12218 | 1087 |
| 112 | Medium Crate | 593, 12350 | 1087 |
| 121 | Medium Crate | 564, 12367 | 1081 |
| 122 | Medium Crate | 635, 12271 | 1087 |

No opcode 18 in `L1_DC.json` targets these seven indexes. Three opcode 9 commands name u16 94, 95, and 97, and their owners are props 94, 95, and 97, not these controls. The script does not move the boxes. The owner's "cannot be moved" matches that absence. How the original player pushed a crate is not an opcode in this file.

## Mace

Two MIX records carry dword `0x8FCB4F6D` at byte 32, height −130, 85 above the crate height:

| file | native x, y | height | region |
| --- | --- | --- | --- |
| 7323635 | 417, 12444 | −130 | 1092 |
| 7323746 | 471, 12480 | −130 | 1099 |

`GLOBAL.MIX` has the cstring `2-Br Mace` at file 6014997 and the same dword at file 5994844. This pass did not re-prove they are one item record. The printed name is the hintbook's mace. The JSON has no item objects, so a pickup script was not framed. A third record of the same dword is file 7323191, native (329, 16631), height −285, region 1171, the bridge room, not this stack.

## Roaches

Thirteen actors use definition u16 13572 at height −215. Twelve of them stand in regions 1087 or 1083, on the same floor as the crates. Actor 33 is (628, 12271), one unit from Medium Crate 122 in y and on top of that cluster. Actor 34 is (651, 12244), one unit from Medium Crate 96. Their event lists are empty. A cstring `Roach` is in `L1_DC.MIX` at file 7119990. The definition join was not re-proven. HINTBOOK 2033-2035 names the giant cockroaches in this fire room.

## Opens

- The push. No command moves controls 94-122.
- The item-pickup callee for the two height −130 records.
- Definition 13572's name.
- No longplay frame was opened.

## Grades

HINTBOOK 2033-2048 for the roaches, the stack, the mace, and not keeping it. DECODED for the seven empty crate controls, the two mace records, and the thirteen actors. The owner's blocked climb is the missing push. FRAME open.
