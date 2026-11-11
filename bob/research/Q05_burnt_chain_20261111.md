# Q05 How armour lowers a blow

complete true

formula_finished false

Worn armour is not read inside `0x62728`. The function scales context+`0x16` by the scalar its caller pushed. On the ordinary gate that scalar includes the defence sum, and the Burnt Chain's signed byte `+0x41` is 8. The port's `scalar()` is that sum alone, so it does not agree. No host. The descriptor walk can still replace the product before context+`0x1E`, so this note does not give a lost-HP integer. Q01 was not rewritten.

Pinned LOLG.DAT sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`, size 1977007. A code address A is file A+`0x37000`. Capstone, from the function entries named below. GLOBAL.MIX sha256 `1e3e2a46340d714aaf4d583e5aff7e58dc11005bac6c694fac49c07d13e01edd`, size 7407657. Definition blob entry `3984507021`, mix offset `0x5B76F9`, size 724388, sha256 `b399b5c8bfea3597293a3237f30f45985efa2dd88d2dc29d5d18ca7488f60891`. Record base 496, stride 91, count 170.

## Where the amount is scaled

PROVEN. `0x62728` (file `0x99728`): four pushes, `sub esp, 0x50`. `0x6272F` (file `0x9972F`) loads the scalar from `[esp+0x68]`, the second argument. `0x62733` loads the context from `[esp+0x64]`.

The kind arm is kinds 0, 1, 3, 4 and 5. Kind 2 and kind 6 and above take other arms. For these five kinds:

- `0x6295B` loads the flag word at context+2. `0x6295F` (file `0x9995F`) is `test al, 8`. A set bit jumps to `0x629BF`.
- `0x62967` jumps to the same place when the mask word is 0.
- `0x629BF` shifts context+`0x16` left 16 and stores that at `[esp+0x34]`. The scalar is not used.
- Otherwise `0x6296D` loads the amount from context+`0x16` and `0x62970` compares the scalar with it.
- Scalar greater than or equal to the amount: a zero scalar is incremented (`0x62978`), then esi = `(amount << 15) / scalar` (`0x62980`, `0x62988`).
- Scalar below a positive amount: esi = `0x10000 - (scalar << 15) / amount` (`0x62994`, `0x629A3`, `0x629A5`, `0x629AA`). A zero scalar on this arm leaves esi at `0x10000`.
- `0x629B0` reloads the amount. `0x629B3` (file `0x999B3`) is `imul eax, esi`. `0x629B6` (file `0x999B6`) stores the product at `[esp+0x34]`.

A larger scalar makes that product smaller. That is the reduction. A byte search of `0x62728` through `0x62F20` found no displacement `0x3A8`. The later store of the walked integer is still `sar([esp+0x34] + 0xFFFF, 16)` at `0x62EC9`, then the min with context+`0x22` (R01, Q01). Those steps stay open.

## Who pushes the armour

PROVEN for the call. Player receive `0xD03B8` reaches `0xD0483` `push 0x23348` and `0xD0488` (file `0x107488`) `call 0x89E7C`. `0x89E83` puts `0x23348` in esi and the context in edi. Q01's three gates, re-read from that entry:

- Bit `0x80000` of `[0x2270E]` set (`0x8A02E`): push scalar 0 and a null descriptor, then join the call.
- Else bit 24 of `[0x2279A]` set (`shl 7` / `shr 31` at `0x8A045`): push scalar 0 and a stack descriptor. Call at `0x8A055`.
- Else, file `0xC1067`: `0x8A067` loads `[esi+0x3A8]`, `0x8A06E` loads `[esi+0x398]`, `0x8A074` loads `[esi+0x3A0]`, `0x8A07A` and `0x8A07C` add them, and `0x8A07E` (file `0xC107E`) pushes the sum. `0x8A080` calls `0x62728`.

Those two flag bits were not read. Whether a played blow takes the third gate is UNKNOWN. A scalar of 0 does not reduce a positive amount.

The other six calls do not push `[0x23348+0x3A8]`:

| Call | Scalar |
| --- | --- |
| `0x5DB58` | edx, and `0x5DB38` is `xor edx, edx` |
| `0xA6CBE` | zero-extended byte `[ebx+0xA7]`. The walk from `0xA6C69` reads `[ebx+0x88]` before this push, so ebx is the creature, not `0x23348` |
| `0xB4242`, `0xB426D` | immediate 0. `0xB426D` then reads slot +`0x88` and applies the difference through slot +`0x84`. That path does not pass armour |
| `0xF2B15` | edx, and `0xF2AED` is `xor edx, edx` |
| `0xF2B41` | immediate 0 |

`0x8A20B` adds `[ebx+0x3A8]` and `[ebx+0x3A0]`, and `0x8A218` loads `[ebx+0x398]`, then `0x8A22E` calls `0x9269C` with those as separate arguments (`push` of `0xFF` and `0x61` as well). That call is not `0x62728`.

## The three dwords

PROVEN as the words the third gate adds.

`[+0x3A8]` is I03's sum of signed definition byte `+0x41` from every occupied equipment pointer. The strike forms, byte `[0x23C2D]` equal to 1, 8 or 9, share one switch arm. The jump table at `0x8A5CF` is object-2 raw `0x31314`, analysis `0x8A338`. Indexes 0, 7 and 8 (those three byte values) land on `0x8A3A1`. The loop adds `sar(dword [definition+0x3E], 24)` at `0x8A3E1` through `0x8A3EB`, including the weapon slot. I03's three class `0x43` records are the other column, byte `+0x40`. They are not this sum.

`[+0x398]` on that same arm is the copy of `[+0x390]` at `0x8A430` / `0x8A43C`. Q02: `[+0x390]` is player dword `+0x155`, and a new Luther's magic is 10. The constructor stores 0 at `[edi+0x398]` (`0x86F7B`). The 10 is there only after this recompute, and only while `+0x155` is still 10. Other switch arms write a multiple (`0x8A4CE` shifts the copy left 2; `0x8A534` doubles it). Bytes 1, 8 and 9 do not take those arms.

`[+0x3A0]` of this controller is the constructor 0 at `0x86F8F` (`mov [edi+0x3A0], 0`). The other object-field stores of displacement `0x3A0` in the code image sit in `0x7F444` (`0x7F46D` stores 0, `0x7F651` stores the incremented dword, `0x7F687` stores 0). ebx there is argument 0. `0xD128E` pushes the immediate `0x23819` and `0xD1299` calls `0x7F444`. `0x7AA8C` pushes the ebx that `0x7AA79` just passed to `0x7F200`, which Q02 already tied to `0x23819`. Neither writer is `0x23348`.

So on the third gate, after a form 1, 8 or 9 recompute, with magic still 10 and `+0x3A0` still 0, the scalar is 10 plus the `+0x41` sum. Before that recompute the magic term is 0.

## The three bytes

PROVEN. Read from the blob, not from `definitions.json`. Signed equals raw; each byte is below `0x80`.

| Index | Name | Byte `+0x41` | Mix offset of that byte |
| ---: | --- | ---: | --- |
| 36 | `37-Brnt Chain` | 8 | `0x5B85F6` |
| 40 | `41-Mail shirt` | 20 | `0x5B8762` |
| 43 | `44-Platemail` | 30 | `0x5B8873` |

Blob offsets of those bytes are `0xEFD`, `0x1069` and `0x117A` (base + index * 91 + `0x41`).

The same column, not required as the two other armours: index 37 `38-Guard shield` is 5 (mix `0x5B8651`); index 41 `42-Gargoyle br` is 5 (mix `0x5B87BD`). Index 4 `5-Short swd` and index 29 `30-Empty hand` are 0. A worn short sword adds nothing to this sum.

Worked scalar, third gate only, new Luther, magic still 10, `+0x3A0` still 0, one of these worn and the short sword adding 0: Burnt Chain 18, Mail shirt 30, Platemail 40. That is the scalar argument, not a lost-HP count. The arrival Luther's magic was not read (Q03: no Act 1 experience total).

## The port

PROVEN as a reading of `scripts/lol2/player_defense.gd`. It was not edited.

`scalar()` returns 0 unless `player_form` is 0. Otherwise it adds the catalog defence of the offhand, the armour, and the weapon. The comment names Gargoyle bracers 5 and Guard shield 5, and those match the bytes above. `tests/captain_equipment_transport_test.gd` expects Burnt Chain 8 + bracers 5 = 13. That 13 is the `+0x3A8` piece. The native ordinary-gate scalar is `[+0x398] + [+0x3A0] + [+0x3A8]`. The port omits the magic copy and `+0x3A0`. It does not agree.

`damage()` then multiplies by 0.4 (`round(native_loss * 0.4)`, and the `defense <= 0` arm also returns `request * 0.4`). That factor is not in the kind arm.
