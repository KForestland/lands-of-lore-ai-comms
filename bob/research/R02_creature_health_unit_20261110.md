# Creature health unit

Pinned `LOLG.DAT` sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`. Analysis address A is file A+`0x37000`. Difficulty byte 1, the arm that leaves the amount. No menu. No host. The scale itself stays in `R01_damage_formula_20261110.md`.

## Grades

| Claim | Grade |
| --- | --- |
| The integer at context+`0x1E` is the health unit. Context+`0x26` is context+`0x22` minus that integer, and a negative difference is stored as 0 | PROVEN. Restated from the formula note; the store bytes were not re-opened |
| A creature strike puts the word at actor+`0x88` into context+`0x22` and context+`0x26`, calls `0x62728`, then writes the remainder back through `0xA7A74` | PROVEN |
| `0xA7A74` stores `min(slot +0x8C, argument)` at actor+`0x88` when the argument is nonzero and the min differs from the word already there | PROVEN |
| Slot +`0x8C` (`0xA7B8C`) returns the word at actor+`0xB0` | PROVEN |
| The constructor stores definition word +`0x63` at actor+`0xB0` (`0xA2197`, `0xA21A0`) | PROVEN |
| Player slot +`0x88` (`0xD69D8`) returns dword +`0x14D`. Slot +`0x84` (`0xD6A08`) adds its argument to that dword | PROVEN |
| Byte 1 of `[0xB7FB2]` leaves the amount, and leaves the word returned from creature slot +`0x9C` | PROVEN in the formula note. Not re-derived here |
| File placement word +`0x2B`, and file definition word +`0x63`, for the actors below | PROVEN as file bytes |
| Those file words are the constructor's two operands | LIKELY |
| A zero health argument, and what a creature's own blow adds into the amount | UNKNOWN |

## The read and the write

Creature strike, analysis `0xA6C69`: `mov dx, [ebx+0x88]`, then both context+`0x22` and context+`0x26` get that zero-extended word. `0xA6CBE` calls `0x62728`. `0xA6CDF` calls `0xA7A74` with the actor, the dword now at context+`0x26`, and the sign-extended kind byte at context+`0x14`.

`0xA7A74`: a nonzero argument calls slot +`0x8C` and keeps the smaller of that return and the argument. If that value differs from the word at actor+`0x88`, `0xA7B02` stores it. A zero argument does not reach that store. Byte +`0xA8` equal to `0x0F` stores 0 and skips it. These paths were re-disassembled.

Slot +`0x8C` is `mov ax, [actor+0xB0]`. The constructor loads `ax` from `[definition+0x63]`, where the definition pointer is `[actor+0x2C]`, and stores that word at actor+`0xB0`.

The constructor then takes the dword at local+`0x2B`, adds one, and stores that word at actor+`0x88`. It immediately calls `0xA7A74` with the original word at the same local. On the nonzero path the added one is replaced by `min(cap, that word)`.

Player path `0xB424C`: slot +`0x88` fills context+`0x22` and context+`0x26`, `0x62728` runs, and slot +`0x84` is called with context+`0x26` minus the value slot +`0x88` returned. `0xD6A08` adds that argument to dword +`0x14D` when the dword is nonzero and bit 1 of byte +`0x229` is clear, and it caps the sum with dword +`0x149`. A sum that is not greater than 0 stores 0 and calls `0xD8D48`. Bit `0x40` of the context kind byte takes the other arm at `0xB4227`: it forces context+`0x22` to 1, calls the formula, and does not write `+0x14D`.

The same integer is subtracted from creature word +`0x88` and from player dword +`0x14D`. The percentage at context+`0x2A` is not the unit.

## File words for the Act 2 actors

`L8_SJ.MIX` sha256 `3eff07430a453d2c6f09133f869874e0530af1b6a3bfff7f4297761b96a28bc2`. `L9_DR.MIX` sha256 `700300d0cdf7df0af9471f3476c4e6ba473a603fa89e3a6e1855037d70be09c7`. Placement records are 56 bytes. Definition records in the level metadata are 147 bytes, name at +135. Word +30 of the placement is a different field.

| Actor | Record name | Definition index | Placement word +`0x2B` | Definition word +`0x63` | Placement word +30 |
| --- | --- | ---: | ---: | ---: | ---: |
| L8 68 | LAMPLT | 9 | 200 | 200 | 30 |
| L8 70 | LAMPLT | 9 | 200 | 200 | 30 |
| L8 73 | LAMPLT | 10 | 200 | 200 | 50 |
| L9 61 | StSquid | 0 | 800 | 800 | 255 |
| L9 68 | StSquid | 0 | 800 | 800 | 255 |

The L8 record named WILD, definition 0, has word +`0x63` equal to 500. Actors 68, 70, and 73 are not that record. Word +`0x65` is 0 on LAMPLT, on StSquid, and on that WILD record. `0xA1FBC` returns definition word +`0x65` and the constructor stores it at actor+`0xB2`. That is the word slot +`0x9C` returns. It is not the health word, and this pass did not trace a creature's outgoing blow.

The loader at `0xA1C6B` reads `0x87` bytes into each record, then reads `0x0C` bytes aside. `0x87+0x0C` is 147, the file stride. The stored table stride is `0x8B` (139). Offset `0x63` sits inside the `0x87` bytes, and the loop does not write it. `0x118820` is the call used for that read and for the constructor's `0x38`-byte read. Its body was not entered, so the file words above reaching those two operands stays LIKELY. If both links hold, the nonzero path sets word +`0x88` to 200 for those three L8 actors and to 800 for those two L9 actors, because each pair is equal and `min` of a pair is that value.

## What the port is using

The port's 15 a blow is the constant in `prepare_act2_creatures.py`: each hit percent is multiplied by 15 and divided by 100. The port's 8 a blow and Luther's 30 are the flat stand-ins named by task R-01. They are not definition byte +`0x40` and they are not dword +`0x14D`. Byte 1 does not scale the native amount. Signed definition byte +`0x40` is one term of that amount, from the item-number note, and the other terms are still open. No blow count is claimed here.

Use byte 1. Creature health is word +`0x88`, capped by definition word +`0x63`. Player health is dword +`0x14D`. One point of either is one point of context+`0x1E`.
