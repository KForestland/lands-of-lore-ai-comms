# H12 Crystal crate, steel door, amulet, gauntlets

Beat 83. `L7_DH`, same archive as H10. The door, the crates, and the amulet are three separate scripts. None of the crate groups names the door.

OPTIONAL. The Halls are not required (BRADY 3343-3346). These two items are the payoff inside them.

## What the books say

HINTBOOK 2528-2533: past the last sliding bookcase, do not enter the round room yet. A steel door is farther down. Take a box with the crystals showing, move it next to the door, step back, and cast Spark at level three. The door is gone. Inside are Colin's Amulet and the Gauntlets of Might.

BRADY 3385-3389: some crates open and show a crystalline mass. They are explosives. A Spark spell detonates them. BRADY 7006 calls the same entrance step a Spark on the monastery bookshelves, which is H09's room, not this door.

## Steel door

Control 84, static slot 40 `Iron Door`, native (−1243, 614), height 750, region 1589. Kind 6 value 21, predicate `0005000000`, group 7656, event link file 4880071, MIX match:

`0e104a0003000000` opcode 14, target u16 74, byte 4 = 3, then opcode 16 byte 4 = 1 on u16 84, opcode 5 byte 4 = 1 on 84, opcode 9 byte 4 = 8 on 84.

Left kind 5 was not entered. The group does not name a crate, does not write local 6 `Door_destroyed`, and has no Spark command. Local 6 is written by movable 56, a different `Door` at (−2612, 2459), group 13634. That is not this steel door.

## Crates

89 controls have a kind-9 value-17 event. The ones within 800 of the door are all static `crate 20rwc`, and they share one shape. Nearest is control 448 at (−1243, 530), height 750, region 1248, 84 units due south of the door on the same stored x. Event links file 4880359 and 4880365, MIX match.

- Kind 3 value 1, no predicate, group 8732: opcode 9 byte 4 = 0x11 on u16 448, opcode 16 byte 4 = 1 on 448.
- Kind 9 value 17, predicate `0005000001`, group 8750: opcode 15 `0f10c0016510bf01` on u16 448, opcode 16 byte 4 = 2, opcode 9 byte 4 = 2.

The same pair, with each crate's own index, repeats on controls 55-70 and 445-453. Heights are 750, except 64, 65, 69, and 70 at 771. No crate raw in that set contains u16 84. Opcode 15 was not entered. Kind 5 was not entered, so the predicate's last byte 1 is not named "crystals showing." That phrase is HINTBOOK 2530. A command that moves a crate was not found. Putting 448 next to the door is the book's action. The nearest row is the spatial candidate, and every nearby crate has the same script.

## Colin's Amulet

Control 71, static slot 0 `Bookcase1`, native (−1075, 727), height 750, region 1587, about 200 units from the door. Kind 4 value 0, predicate `0005000000`, group 7608, event link file 4880043, MIX match:

- opcode 3 `03010000d90846aa00000000` (dword `0xAA4608D9`, byte 8 = 0)
- opcode 16 byte 4 = 1 on u16 71

`GLOBAL.MIX` holds that dword at file 6002670. The cstring join to Colim's Amulet was not re-proven. The printed name is HINTBOOK 2532, "Colin's Amulet." Opcode 3 was not entered.

## Gauntlets of Might

The dword `0x2B5E32FC` occurs zero times in `L7_DH.MIX`. No group grants it. A different dword, `0xF071C0B5`, occurs once in the same file. This pass did not place that second dword on a control. The Might pair is the book's sentence. It is not a grant in this level.

## Opens

- Kind 6 value 21 on the door, and opcode 14 byte 4 = 3 aimed at u16 74.
- Whether kind 9 value 17 is the Spark hit. The predicate requires the unentered kind-5 test to be 1. The door group never runs from a crate group.
- Who moves the crate. 
- Where the Gauntlets of Might are granted.
- No longplay frame was opened.

## Grades

HINTBOOK 2528-2533 and BRADY 3385-3389 for the crystals, the Spark, the door, and the two items. DECODED for control 84, control 71, control 448 and the shared crate shape, and for the Might dword being absent. FRAME open.
