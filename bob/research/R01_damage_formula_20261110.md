# Damage formula, byte 0xB7FB2, creature health

Pinned `LOLG.DAT` sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`. Analysis address A is file A+`0x37000`. An object-2 fixup target is that offset plus `0x59024`. Object-5 immediates in the image are the object-5 offsets. No difficulty menu. No host change. D16 still says the build uses one level.

## Grades

| Claim | Grade |
| --- | --- |
| `[0xB7FB2]` is the clamped `Difficulty` integer, copied from `[0x2239C]` | PROVEN |
| Byte 0, 1, and 2 scale the amount dword at context+`0x16` as written below. Any other byte leaves it | PROVEN |
| That scale runs only when the target or the attacker pointer is object-5 `0x22574` | PROVEN |
| The integer stored at context+`0x1E` is subtracted from the health value the caller put at context+`0x22` | PROVEN |
| A creature strike writes that remainder back to the word at actor+`0x88`, capped by the word at actor+`0xB0` | PROVEN on the nonzero path |
| Actor+`0xB0` is definition word +`0x63`. Shade and L10 SKEL are 200. Both L20 EYE records are 10000 | PROVEN for those records |
| The player slot +`0x88` returns dword +`0x14D`, and slot +`0x84` adds its argument to that dword | PROVEN |
| Byte 0/1/2 also scale the word returned from creature slot +`0x9C` (actor+`0xB2`) | PROVEN for the return. Callers of that return were not all followed |
| This install's `OPTIONS.INI` value is 0. A missing key's result | 0 is the argument that is formatted first. `0xCE974` was not entered, so a reader that ignores that buffer stays LIKELY |
| Kind byte 6 and above, when the descriptor pointer is null | UNKNOWN. That arm does not write the fixed-point slot before the final shift |

## Where the byte comes from

`OPTIONS.INI` section `Miscellaneous`, key `Difficulty`. The reader at analysis `0xCC0C3` pushes 0, the key at object-5 `0x19F2`, and the section at object-5 `0x19FD`, and calls `0xCE8C0`. That call formats the pushed 0 with the `%d` at object-5 `0x2C65`, then calls `0xCE974`. The return is clamped: a negative value becomes 0, a value above 2 becomes 2. Analysis `0xCC0F7` stores it at `[0x2239C]` (fixup object 5, offset `0x2239C`).

Analysis `0xCCD5C` loads `[0x2239C]` and `0xCCD61` stores that byte at `[0xB7FB2]`. Both immediates are object-5 fixups (`0x2239C` and `0xB7FB2`). `[0xB7FB2]` is past the initialized image, so it is 0 until this store or one of the other writers runs.

This install's line is `Difficulty=0`, with a comment that 0 is the easy setting and that 1 or 2 is the challenge setting. The formula agrees with that comment. It does not agree with treating 0 as Medium. Byte 1 is the arm that does not change the amount. D16 says the build uses that original Medium default and does not grow a difficulty option. The missing-key argument in the executable is 0, not 1.

## What the three values do

The load is analysis `0x62868`, `mov al, [0xB7FB2]` (fixup object 5, offset `0xB7FB2`). The amount is the signed dword at context+`0x16`. The four compares with `0x22574` are object-5 fixups. Context+4 is the target. Context+8 is the attacker.

Byte 0, in this order:

- If the target is `0x22574` and the amount is greater than 3, the amount becomes the toward-zero quotient of the amount divided by 3.
- If the attacker is `0x22574`, the amount is then doubled.

Byte 1, and every byte other than 0 and 2: the amount is left as it is.

Byte 2, in this order:

- If the target is `0x22574`, the amount is doubled.
- If the attacker is `0x22574` and the amount is greater than 2, the amount becomes the toward-zero half (`sar` of `amount - sign(amount)`).

A hit where neither pointer is `0x22574` is unchanged for every byte. When both pointers are `0x22574`, byte 0 divides by 3 and then doubles, and byte 2 doubles and then halves.

The same byte is read again at analysis `0xA7CED` (fixup object 5, offset `0xB7FB2`). Creature vtable object-5 `0x58D0` slot +`0x9C` is `0xA7CE8`. It returns the word at actor+`0xB2`:

| Byte | Return |
| --- | --- |
| 0 | toward-zero half of the word |
| 1, or any byte other than 0 or 2 | the word |
| 2, word at least `0xA000` | `0xFFFF` |
| 2, word below `0xA000` | the word plus its toward-zero half |

The constructor stores definition word +`0x65` at actor+`0xB2` before this slot runs (`0xA21B0` in the earlier stat note; the call itself is `0xA21DD`). This return is not the health word.

## The amount, before the byte

`0x62728` is the formula. Eight direct calls: `0x5DB58`, `0x8A055`, `0x8A080`, `0xA6CBE`, `0xB4242`, `0xB426D`, `0xF2B15`, `0xF2B41`. The first argument is the context. The second is the scalar in ebx. The third is a descriptor pointer.

If context+`0x16` is negative, it is replaced by context+`0x22`.

The heading window runs when the target's slot 0 returns 2, or returns 1 on the second call. The attacker's word +`0x1E` must lie within ±`0x2000` of the target's word +`0x1E`, the attacker must be nonzero and not the target, and the window is skipped when the target is `0x22574` and dword `[0x2276A]` is nonzero. On that path the amount gains its toward-zero tenth (`idiv` by 10), and bit 8 is set in the flag byte at context+2. This runs before the difficulty byte.

## After the byte

Kind byte context+`0x14`:

| Kind | Fixed-point value at `[esp+0x34]` |
| --- | --- |
| 0, 1, 3, 4, 5, and flag bit 8 set, or the mask word 0 | amount shifted left 16 |
| 0, 1, 3, 4, 5, otherwise, scalar greater than or equal to the amount | amount times `(amount << 15) / scalar`, with a zero scalar forced to 1 |
| 0, 1, 3, 4, 5, otherwise, scalar below a positive amount | amount times `0x10000 - (scalar << 15) / amount` |
| 2, attacker null | amount shifted left 16 |
| 2, attacker present | `(attacker slot +0xE8 byte) * (amount << 16) / (target slot +0xE8 byte)`. If that quotient exceeds `amount << 16`, the excess times the scalar, divided by 256 toward zero, is subtracted |
| 6 and above | this arm does not write `[esp+0x34]` |

The kind-2 divide uses the returned byte as the divisor with no zero test in this function.

The low 16 bits of the mask word are counted. The flag word masked by `0xE7` is counted. The fixed-point value is divided by the greater of 1 and the mask count, and that divisor is multiplied by the flag count when the flag count is above 1. A zero quotient is replaced by `0x10000` divided by the same divisor. That quotient is `[esp+0x28]`.

If the descriptor pointer is null, or the mask word is 0, or the mask count is 0, the walk is skipped and `[esp+0x34]` stays the kind result. Otherwise `[esp+0x34]` is cleared and each set mask bit contributes as follows. The working value starts as the quotient, or twice the quotient when `[esp+0x20]` is nonzero and the bit is bit 0. `[esp+0x20]` is 0 or 2, from bit 1 of the byte at `[preset+0x16]` indexed through `[eax+0xBBC0]`. Up to four rows then scale it. The row's selector byte:

| Selector | Effect on the working value |
| --- | --- |
| 0 or 1 | row skipped |
| 2 | doubled |
| 3 | tripled |
| 4 | shifted left 2 |
| 5 | toward-zero quarter, unless flag bit `0x10` is set and the row's flag filter lacks bit `0x10` |
| 6 | toward-zero half, same exception |
| 7 | three quarters, toward zero, same exception |
| 8 | no scale. The bit is ORed into `[esp+8]`, and into `[esp+0x30]` when the mask count is 1. The row loop stops |
| 9 | target slot +`0x84` is called with the toward-zero half, converted by `sar(x + 0xFFFF, 16)`. The working value becomes 0 |
| 10 | the same call with `sar(x + 0xFFFF, 16)` of the unhalved value. The working value becomes 0 |
| above 10 | row skipped |

A zero mask-filter word does not reject the bit. A nonzero mask filter must overlap the current bit. A nonzero flag filter must overlap the current flag bit. After the rows, bit `0x1000` stores `sar(value + 0xFFFF, 16)` at `[esp+0x24]` and does not add. Every other bit adds the working value into `[esp+0x34]` (`01 54 24 34` at `0x62E72`). The jump table is analysis `0x62E6B`, fixup object 2, offset `0x96E0`, which is `0x62704`. Nine raw dwords there plus `0x59024` are the arms `0x62CE6` through `0x62E1F`.

The stored integer is `sar([esp+0x34] + 0xFFFF, 16)`, written at context+`0x1E` (`89 42 1E` at `0x62EC9`). It is then replaced by the smaller of itself and context+`0x22`. Context+`0x26` becomes context+`0x22` minus that integer, and a negative difference is stored as 0. Context+`0x2A` is `(100 * the integer) / context+0x22` when that health value is nonzero, and `0x64` when it is zero. The percentage is not the health unit.

For a positive fixed-point value, adding `0xFFFF` before the shift by 16 is the ceiling of the value over `0x10000`.

## Creature health is that integer

Definition records are 147 bytes. Analysis `0xA2197` loads the word at +`0x63` and `0xA21A0` stores it at actor+`0xB0`. Creature slot +`0x8C` is `0xA7B8C`, and `0xA7B92` returns that word.

Re-read from the level MIX metadata, word +`0x63`:

| Record | Word +`0x63` | Word +`0x65` |
| --- | ---: | ---: |
| L1 Roach | 10 | 0 |
| L1 GGUARD | 80 | 0 |
| L7 SHADE | 200 | 100 |
| L7 Rat | 20 | 0 |
| L10 SKEL | 200 | 10 |
| L20 EYE, both records | 10000 | 5000 and 10000 |

The plan's 200 and 10000 are this word. One point of it is one point of the integer at context+`0x1E`.

The creature strike at `0xA6C69` zero-extends the word at actor+`0x88` into context+`0x22` and context+`0x26`, calls `0x62728`, calls `0xB4298`, then calls `0xA7A74` with the context+`0x26` remainder. The 0x600 bytes at `0xB4298` contain no operand `+0x26`. `0xA7A74` stores 0 at +`0x88` when byte +`0xA8` is `0x0F`. A zero argument does not reach the store at `0xA7B02`. A nonzero argument calls slot +`0x8C` and stores the smaller of that cap and the argument when it differs from the word already at +`0x88`.

The constructor's first store at +`0x88` is the placement dword at buffer+`0x2B`, plus one (`0xA21BA`, `0xA21BE`). It then calls `0xA7A74` with the original word (`66 8B 45 E7` at `0xA21C9`). On the nonzero path that call replaces the incremented word with `min(cap, placement word)`.

## Player health is the same integer

Player vtable object-5 `0x5C20`. Slot +`0x88` is `0xD69D8`, which returns dword `[object+0x14D]`. Slot +`0x84` is `0xD6A08`. Slot +`0x80` is `0xD03B8`.

`0xB424C` reads slot +`0x88` into context+`0x22` and into edi, calls `0x62728`, then calls slot +`0x84` with `context+0x26 - edi`. `0xD6A08` adds that argument to dword +`0x14D` when the current dword is nonzero and bit 1 of byte +`0x229` is clear. The sum is capped by dword +`0x149`. A sum that is not greater than 0 stores 0 and calls `0xD8D48`. The added difference is the change in the same integer the formula subtracted.

## What the build should use

Use byte 1 where a result depends on `[0xB7FB2]`. That is the arm that leaves the amount and the +`0xB2` word alone. Do not add Easy or Hard, and do not read this install's `Difficulty=0` as the shipped default. Creature current health is the word at +`0x88`. Its cap is definition +`0x63` at +`0xB0`. Player current health is the dword at +`0x14D`. Both are the unit of context+`0x1E`.
