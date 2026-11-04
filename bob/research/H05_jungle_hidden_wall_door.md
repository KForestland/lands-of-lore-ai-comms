# H05 Jungle hidden wall and hidden door

Beat 40b. Owner F10 2026-11-03 17:21:01, native (3196, 4160), and 17:50:19, native (918, 3664). Read from `L4_HJ.MIX` and `L4_HJ.json`. Opcode 1, opcode 14, opcode 8, and opcode 2 were not entered.

No new owner F10 after `TRIAGE_20261103.md`. HINTBOOK 2297-2327 has no hidden wall and no door you conceal (kimi K5). Brady's "secret passage behind the statues" is the shrine switch in H04, not a sentence for these two points.

## (3196, 4160) — no sliding wall

The only control or movable within 450 is control 136, static `Inviso platform`, at (3016, 4178). That is the shrine ledge from H03. It has no events.

Region 1902, center (3167, 4256), floor 0, is 100 from the point. Kind 12 group 3768 (file 13026746) runs when predicate `0003010001` passes: local slot 1 equals 1. Slot 1, counting from `villager` at file 13153135, is `First_WO_Seen`. The group opcode 9 / 5 / 8s prop 554. Prop 554 is template 83 `Baccatta w/ maps` at (5874, 3779), 2705 away. Region 1903, 137 from the point, repeats that group shape (group 3810). These are a Baccatta trigger after the Wild One has been seen. They are not a wall record.

No command near this point writes a floor or names a wall mesh. The hidden wall at this coordinate stays open.

## (918, 3664) — Imp switch and Imp door

Region 624 is centered on (917, 3699), floor 0, 35 from the point. Its kind-12 group 862 (file 13023840) is opcode 2 `020100000400`. Arm 4 was not entered.

The door pair sits just east of that:

| Record | Static byte 32 | Name | Native x, y | Height | Region |
| --- | --- | --- | --- | --- | --- |
| movable 51 | 85 | Imp switch, file 13287375 | 1073, 3727 | 50 | 4570 |
| movable 52 | 83 | Imp door, file 13287315 | 1045, 3692 | 0 | 4766 |

These are a second pair with the same static names as H04's movables 54 and 55. This switch's groups name the door.

Movable 51 kind 4:

- State 0, predicate `0005000000`, group 27342 (file 12755646): opcode 14 twice on movable 52, opcode 1 `012034006400` on the door (word 0x64), opcode 16 sets the switch to 1, opcode 1 word 0x64 on the switch.
- State 1, predicate `0005000001`, group 27382 (file 12755686): opcode 14 on the door, opcode 1 word 0 on the door, opcode 16 clears the switch, opcode 1 word 0 on the switch.

Movable 52 kind 2 value 48, group 27414 (file 12755718), no predicate: opcode 1 word 0 on the door and on the switch, and opcode 16 clears the switch. Using the door puts both back to the closed words.

## What the player does

At the second point, click the Imp switch. The groups write the door's opcode 1 word to 0x64, and a click on the door writes it back to 0. What 0x64 does to the mesh was not entered, so "the door slides" stays the shape of those words, not a proven motion.

At the first point, the records under the owner are the Baccatta surface trigger and the shrine's invisible platform. A wall that opens was not in those groups.

## Required or optional

OPTIONAL for both spots. No printed step says the game stops until either one is used. The shrine itself is the optional Summon (HINTBOOK 2300-2302). `First_WO_Seen` only gates the Baccatta poke.

## Frame

No longplay frame was opened.

## Still open

- A hidden-wall mesh at (3196, 4160). None of the nearby groups is a floor or a door write.
- Opcode 1 word 0x64 on movable 52. The open and the close are those two words.
- Opcode 2 arm 4 on region 624, under the second owner point.
- A longplay frame of either spot.

Grades: the door pair, the static names, the group bytes, and the Baccatta trigger are DECODED. The hintbook does not describe beat 40b. The frame is open.
