# H04 Jungle statue switch

Beat 40a. Owner F10 2026-11-03 17:20:31, jungle native (2951, 3525). Read from `L4_HJ.MIX` and `L4_HJ.json`. Opcode 18, opcode 9, opcode 1, and opcode 16 were not entered.

No new owner F10 after `TRIAGE_20261103.md`. The hintbook has no statue-switch sentence (kimi K5). Brady's shrine passage is the book match.

## The switch and the door

The indexes 54 and 55 are movables, not controls. Control 54 is static `Guard block` at (5569, 3924). Control 55 is static `Inviso Block` at (3060, 3150). Neither is this spot.

| Record | Static byte 32 | Name file | Native x, y | Height | Region | Events |
| --- | --- | --- | --- | --- | --- | --- |
| movable 54 | 85 | Imp switch, file 13287375 | 2911, 3535 | -125 | 4567 | kind 4 groups 27438 and 27462 |
| movable 55 | 83 | Imp door, file 13287315 | 2850, 3693 | -170 | 4577 | none |

Static names are the 30-byte run that starts at file 13284825 (`planks`). Movable 54 is 46 from the owner point. Prop 123, template 48 `hangin 2`, is at (2940, 3535), height -170, region 3273, 15 from the owner point.

No command in the export targets u16 55. The Imp door is placed and has no group.

## What the player does

Movable 54 kind 4, both states, opcode 9 byte 0x15 on prop 123.

- State 0, predicate `0005000000`, group 27438 (file 12755742): opcode 16 sets movable 54 to 1, opcode 1 `012036006400` (word 0x64), opcode 9 on prop 123.
- State 1, predicate `0005000001`, group 27462 (file 12755766): opcode 16 sets it to 0, opcode 1 word 0, opcode 9 on prop 123.

Prop 123 then toggles local slot 45. Counting from `villager` at file 13153135, slot 45 is `Imp_mover` (file 13154980).

- `Imp_mover` equals 0, group 514 (file 12728818): opcode 208, opcode 20 on prop 537 (an Imp Lord), opcode 198 sets slot 45 to 1, opcode 18 on control 57.
- `Imp_mover` equals 1, group 562 (file 12728866): the same shape, slot 45 cleared, opcode 18 on control 57 with a different height word.

Control 57, static slot 88 `Imp stand` (file 13287465), is at (2888, 3693), height -240, region word 65535. It stands on the same y as the Imp door, 38 to the east. Its own kind-6 value-6 group 18748 is only opcode 20 on itself.

The opcode 18 words, flags 0x0109 (bit 0x0004 is clear, bit 0x0100 is set):

- Group 514: (2887, 3694, -172)
- Group 562: (2887, 3694, -240)

-172 is 68 above the placed height. -240 is the placed height. The stand is the record the switch writes. The door movable is not named by a command.

## Books

BRADY lines 2838-2842: the warding imp statues kill you if you take the scroll first. Unlock the secret passage behind the statues before you take the scroll. Look behind the statues.

HINTBOOK 2298-2325 describes the shrine, the drop, the spikes, and the lizard ledge. It does not describe this switch.

## Required or optional

OPTIONAL. The shrine scroll is the optional Summon the Museum already gave (HINTBOOK 2300-2302). This switch is Brady's unlock for that same shrine. Nothing outside the shrine reads `Imp_mover`.

## Frame

No longplay frame was opened.

## Still open

- Opcode 18 does not have bit 0x0004 set, so the stand's motion is the height words only.
- Opcode 1 words 0 and 0x64 on the switch. What those do to the mesh is open.
- Movable 55 Imp door has no group and no command target. Whether the stand's height change is the door opening is open.
- A longplay frame of the passage.

Grades: placements, static names, `Imp_mover`, and the group bytes are DECODED. The secret passage behind the statues is BRADY. The hintbook does not name this switch.
