# BK13 L19 guck effect

complete false for a seconds rate. The per-call arms below were re-read on LOLG.DAT sha256 b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775. formula_finished stays false. No host change. The invented 1 mana / 0.5 s and 1 health / 4 s timers stay out.

## Book

Hintbook lines 5428–5432: the guck sucks away Luther's mana quickly and his health slowly, and he will not be in it long enough to worry. Lines 5448–5451: the rapids drown a slow crossing, which is a different sentence. No number is in the book. Grade HINTBOOK. Brady's acid sentence is not this kind byte.

## Which preset

L19_BC metadata, 25 presets. Kind is preset byte 22. Depth is preset byte 21. Grade DECODED.

| index | resource | name | kind | depth |
|---|---|---|---|---|
| 7 | 265 | Black floor | 0x00 | 0 |
| 8–9 | 266 | Giger bottom, Giger top | 0x0D | 0 |
| 10–13 | 266 | Sludge W/N/S/E | 0x0D | 30 |
| 14 | 211 | Shallow | 0x0D | 15 |
| 15 | 211 | Medium | 0x0D | 30 |
| 16 | 211 | Deep | 0x0D | 40 |
| 17 | 211 | Dead | 0x0D | 100 |

Material 265 does not enter the liquid switch. Kinds 0 through 4 return 0 at 0x67844 (`sub al, 5` / `cmp al, 0x12` / `ja`). Material 211 and the 266 sludge and giger presets are kind 0x0D. Depth changes only the submerged test. It is not a rate.

## The switch

Player slot +0x4C is 0xD651C (object-5 vtable 0x5C20, raw dword 0x7D4F8). While the caller's height is at or below the floor minus the depth byte, 0xD6785 pushes 1, 0, the actor, and the kind, and calls 0x67820. The kind is preset byte 22 (`sar` of the dword at preset+0x13). There is no seconds compare in that window.

0x67820 zeros 0x36 bytes, then:

```
8A 44 24 78          mov al, [esp+0x78]     ; kind
2C 05                sub al, 5
3C 12                cmp al, 0x12
0F 87 01 06 00 00    ja  return 0
25 FF 00 00 00       and eax, 0xff
2E FF 24 85 B0 E7 00 00
                     jmp dword ptr cs:[eax*4+0xE7B0]
```

The displacement 0xE7B0 is the same object-2 offset form the vtable slots use. Adding 0x59024 lands at 0x677D4. The 19 dwords there, each plus 0x59024, are the arms. File 0x9E7D4. Grade DECODED.

| index | kind | raw | arm |
|---|---|---|---|
| 0 | 0x05 | 0xE833 | 0x67857 |
| 1 | 0x06 | 0xE8C0 | 0x678E4 |
| 2 | 0x07 | 0xEE27 | 0x67E4B return 0 |
| 3 | 0x08 | 0xEE27 | 0x67E4B return 0 |
| 4 | 0x09 | 0xE950 | 0x67974 |
| 5 | 0x0A | 0xEE27 | 0x67E4B return 0 |
| 6 | 0x0B | 0xE9D5 | 0x679F9 |
| 7 | 0x0C | 0xEE27 | 0x67E4B return 0 |
| 8 | 0x0D | 0xEA63 | 0x67A87 |
| 9 | 0x0E | 0xEB72 | 0x67B96 |
| 10 | 0x0F | 0xEBB3 | 0x67BD7 |
| 11 | 0x10 | 0xEBF4 | 0x67C18 |
| 12 | 0x11 | 0xEC59 | 0x67C7D |
| 13 | 0x12 | 0xECCC | 0x67CF0 |
| 14 | 0x13 | 0xED23 | 0x67D47 |
| 15 | 0x14 | 0xEDBE | 0x67DE2 |
| 16 | 0x15 | 0xEDBE | 0x67DE2 |
| 17 | 0x16 | 0xEDBE | 0x67DE2 |
| 18 | 0x17 | 0xEDEC | 0x67E10 |

Kind 0x0D is index 8, arm 0x67A87. The earlier sequential-body guess that put kind 0x0D at 0x67C7D was wrong. 0x67C7D is index 12, kind 0x11.

## Kind 0x0D on the player

Player vtable 0x5C20. Slot +0xE4 is 0xD8A04 and returns the byte at actor+0x161. Slot +0xE8 is 0xD8A10 and returns the byte at actor+0x162. Slot +0x90 is 0xD6AE8. Slot +0x94 is 0xD6A88, which adds its signed argument to the dword at actor+0x145 and clamps it between 0 and the dword at actor+0x141. Slot +0x80 is 0xD03B8, the player hit.

Gates, both past the initialized object-5 image, so both start at 0 until a writer runs. The writers were not entered.

- The high byte of the dword at 0x22CC1 (address 0x22CC4) must be nonzero. Otherwise 0x67A91 jumps to the shared return.
- The actor's first three dwords are compared with the dwords at 0x22574, 0x22578, and 0x2257C. The player object matches itself. When it matches and bit 17 of the dword at 0x2279A is set (`shl 0x0E` / `shr 0x1F` at 0x67ADE), the arm returns 0 and neither drain runs.

When both gates allow it:

Mana, grade DECODED as a per-call integer. 0x67B5B calls slot +0xE8. The byte at +0x162 is divided by 3 (`xor edx, edx` / `mov dl, al` / `idiv` by 3 at 0x67B64). A zero quotient skips the call. A nonzero quotient is pushed to slot +0x90. That slot tests bit 0x2000000 of the dword at actor+0x19A. If the bit is set it returns 0 and does not call slot +0x94. If the bit is clear it negates the quotient and calls slot +0x94, which subtracts it from the mana dword at +0x145. Mana does not call the death store.

Health, grade DECODED for the record that is built, UNKNOWN for the final hit points. 0x67AF0 calls slot +0xE4. The byte at +0x161 is divided by 3 the same way. A zero quotient skips the hit. A nonzero quotient is stored at record+0x16 (the following `max` with 1 does not change a positive quotient). The record is mask word 0x80, flags word 4, target the actor, attacker 0, byte +0x14 = 3, byte +0x15 = 0xFF. Slot +0x80 then calls 0x89E7C, which calls 0x62728. Kind byte 3 takes the same ratio path as kind 1. Mask 0x80 is not the zero-mask shortcut, so the stored quotient is not the number subtracted from the dword at +0x14D. Difficulty byte 0xB7FB2 and the scalar argument can change it first. The final health store stays inside that unfinished formula.

The two bytes are the bytes the experience adders 0xD8A1C and 0xD8B94 increment. Those adders were not re-entered here. No English name is given to them.

## What is not hosted

There is no seconds constant in 0x67A87 or in the submerged test at 0xD6781. Slot +0x4C has several indirect callers. Which of them runs once per frame was not closed. A 0.5 s mana timer or a 4 s health timer would be an invented period. The smallest adapter is the one already in the tree: the drain stays unhosted, `l19_guck_test` still stands a Human in the guck and expects health not to drop, and piece 0364 stays the liquid row. Material 265 is not given a drain. Classic drowning LIMIT 15 is a different mechanic and is not this arm.
