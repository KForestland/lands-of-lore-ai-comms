# H21 Opcode 14 arm 5

Handler VA `0xB59BF` reaches `0xB47B4`. Image `~/lol2_runtime_root/LOLG.DAT`, sha256 prefix `b27a35341c6e877e`, file = VA + `0x37000`. Object-2 fixup used here is offset + `0x59024`. Arms 0, 1, and 2 were read only to check the table index. Arms 3 and 4 were not closed. `0x12415C` was not entered. The word at encoded `0x223A8` was not read. Opcode 1 was not entered. Kind 12's fire time was not entered.

## The switch

File `0xEB824` is `2eff248574b70500`: `jmp dword ptr cs:[eax*4 + 0x5b774]`. The displacement is the object-2 offset. `0x5B774 + 0x59024` is VA `0xB4798`, file `0xEB798`. Seven dwords there are `08b80500 18b80500 28b80500 38b80500 27b90500 96b90500 adb90500`. Plus `0x59024` they are VAs `0xB482C`, `0xB483C`, `0xB484C`, `0xB485C`, `0xB494B`, `0xB49BA`, `0xB49D1`.

Slot 0 is the instruction after the jump, and it stores command byte 5 at record byte +4. Slot 1 stores that byte at record +6. Slot 2 stores it at record +7. The index is command byte 4. Byte 4 above 6 jumps to `0xB478E` (`b801000000` then the pops), which returns 1 and does not store. Arm 5 is slot 5, VA `0xB49BA`.

Before the switch, byte 6 selects the kind-2 record. `[vtable+0xB8]` is called, then the list is walked for byte +1 equal to 2, counting down byte 6. The selected pointer is `ebx`. If the walk ends with no record, `ebx` is the saved one, or 0 when none was seen.

## What arm 5 stores

`0xB49BA`: `push ebx; call 0xB8AC4; add esp, 4; mov word ptr [ebx+8], ax; mov eax, 1; pop ebp/edi/esi/ebx; ret`.

The store is the low 16 bits of `0xB8AC4`'s return, written at the selected kind-2 record, word +8. Command byte 5 is not read. A command whose byte 5 is 0 still writes.

`0xB8AC4` takes that record:

- Byte +4 bit `0x20` set: AX becomes record byte +6. The call is skipped.
- Bit `0x20` clear: it pushes byte +6, byte +7, and encoded `0x221D8`, then calls `0x12415C`. That call was not entered.
- Byte +4 bit `0x10` set: AX is multiplied by the word at encoded `0x223A8` (`imul ax`).
- Else bit `0x80` set: the result is byte +6 times that same word, times `0x3C`.
- Else the previous AX is shifted left 8.

The word at encoded `0x223A8` was not read. File `0x593A8` (VA + `0x37000`) is `0e05e423...`, not a scale constant. The numeric product stays open.

## L16 gates

Across the act3 native JSON set, 478 commands are opcode 14 with byte 4 = 5, in 11 levels. `L19_BC.json` has 355. `L16_CA.json` has 5. The three named groups match `L16_CA.MIX` sha256 prefix `810d39ae20a980c4`:

| stream | group | file | owner | raw |
| --- | --- | --- | --- | --- |
| 0 | 672 | 18782959 | region 2286, kind 12, event 2 | `f000000003000e20020005000000012002006400012001006400` |
| 0 | 698 | 18782985 | region 2317, kind 12, event 2 | same three commands |
| 0 | 3004 | 18785291 | region 4832, kind 12, event 2 | same three commands |

`0e20020005000000` is opcode 14, u16 at +2 = 2, byte 4 = 5, byte 5 = 0, byte 6 = 0. The next commands are opcode 1, u16 2 then u16 1, byte 4 = `0x64`. Opcode 1 was not entered, so `0x64` is not named "open."

Region centers from the geometry entry at file 17959024 (marker 18, region stride 44): 2286 (2300.5, −554), floor 0, ceiling 180; 2317 (2297, −988), ceiling 375; 4832 (2298, −719), ceiling 257. Neighbors join 2317 to 4832. Godot y is the native y with the sign flipped.

Index 2 fits four tables. The only one with a kind-2 record is movable 2, native (2431, −669), height 0, region 10581, static slot 86, byte 34 = 5. Movable 1 is (2175, −669), region 10579, slot 86, byte 34 = 4, and it has no kind-2 record. Both sit on the north lip of region 4832. Actor 2, prop 2, and control 2 have no kind-2 record. The target resolver was not entered. If the target is one of those, `ebx` is 0 and the store is not a skip.

Movable 2's kind-2 record, stream 1 group 49084, raw `0a02bcbf30010400f000`: byte +4 = `0x30` (bits `0x20` and `0x10`), byte +6 = 4, word +8 currently `0x00F0` (240). Byte 6 of the command is 0, so this is the record the walk selects. Arm 5 takes the bit-`0x20` path, skips `0x12415C`, and stores `(4 * word[0x223A8])` in the low 16 bits. Group 49084 itself is opcode 14 byte 4 = 4 on u16 2, then opcode 1 byte 4 = 0 on u16 2 and on u16 1. Arm 4 was not closed in this pass.

Two other L16 arm-5 commands are not these gates. Stream 1 group 2612 (prop 92) has `0e035c0005000000`, target u16 92. Stream 1 group 49690 (movable 76's kind-2 record `0a021ac2300105002c01`, byte +4 = `0x30`, byte +6 = 5, word +8 = 300) has `0e204c0005000000`, target u16 76. Same formula shape. 240/4 and 300/5 are both 60. That is arithmetic on the stored words. It is not a read of `0x223A8`.

## No-op

A no-op adapter is not what these bytes do. Arm 5 always writes record word +8. On the gate command the written value is four times an unread word, and the record already holds 240, so equality was not shown. Dropping the store drops that write. The two other L16 arm-5 commands would be dropped with it.

## Grades

DECODED for the table, the arm-5 store, the `0xB8AC4` bit tests, the three MIX-matched gate groups, the region centers, and movable 2's kind-2 bytes. The scale word, `0x12415C`, opcode 1, kind 12's moment, and the target-table bind stay open. FRAME was not asked.
