# H11 Prism scroll in a Dark Halls bookcase

Beat 79. Same `L7_DH` archive as H10. Two controls carry the same opcode 3 dword. The right-click that learns the group is the book's sentence. It is not a command in these groups.

OPTIONAL for finishing. HINTBOOK 753-756: the Prism group is easy to miss, and without it the end of the game is much more difficult, though not impossible.

## What the book says

HINTBOOK 2486-2488: the Prism spell group is hidden in a bookcase. Right-click the scroll on Luther, the same way as the Summon scroll from the Museum. HINTBOOK 626: many Prism spells are duds. The Museum summon scroll is a different item and was not opened here.

## The two bookcases

Static names are the same 47-name run as H10, file 5052795. Slot 4 is `Bookcase2`. Slot 5 is `Bookcase3`.

Control 971, slot 4 `Bookcase2`, native (−2595, 3634), height 85, region 154. This is the long room beside sliding movable 59 (H10). Kind 4 value 0, predicate `0005000000`, group 12130, file 4872537, MIX match:

- opcode 3 `03010000d8183efc04000000` (dword `0xFC3E18D8`, byte 8 = 4)
- opcode 199 `c70000002001`
- opcode 16 `1010cb030100` (u16 971, byte 4 = 1)

Control 975, slot 5 `Bookcase3`, native (−2331, 2393), height 55, region 33. Two kind-4 value-0 rows, both MIX match:

- Predicate `0005000000`, group 12272, file 4872679: the same opcode 3, the same opcode 199, opcode 16 byte 4 = 1 on u16 975.
- Predicate `0005000001`, group 12302, file 4872709: the same opcode 3 and opcode 199 again, opcode 16 byte 4 = 2 on u16 975.

Left kind 5 was not entered. Opcodes 3, 16, and 199 were not entered. Byte 4 of the opcode 199 command is 0x20. At the `Blowout_happens` local alignment (slot 5, file 4988576, stride 41), slot 32's cstring is empty. That does not prove opcode 199 writes it.

`GLOBAL.MIX` holds the cstring `149-Prsmscrl` at file 6019497 and the dword `0xFC3E18D8` at file 6008494. This pass did not re-prove that the name and the dword are one item record. The printed name Prism is the hintbook's.

A third bookcase in the north room, control 968 at (−2809, 3891), grants a different dword, `0x7B8015C7`, and is not this scroll.

## How the spell is learned

The groups hand the player the dword and then set the bookcase state. They contain no cast and no portrait click. HINTBOOK 2487-2488 is the learn step: right-click the scroll on Luther. Control 975's second row grants the same dword again after the first state change. Whether a second copy casts instead of teaching was not read out of opcode 3.

## Opens

- Opcode 3 byte 8 = 4, and the callee that would add a spell group.
- The right-click handler.
- Which of the two controls is the bookcase the player is meant to find. 971 sits next to sliding shelf 59. 975 is a second copy on a lower height band.
- The name-to-dword join inside `GLOBAL.MIX`.
- No longplay frame was opened.

## Grades

HINTBOOK 2486-2488 and 753-756 for the hiding place, the right-click, and the "not impossible" ending. DECODED for controls 971 and 975 and the three groups. FRAME open.
