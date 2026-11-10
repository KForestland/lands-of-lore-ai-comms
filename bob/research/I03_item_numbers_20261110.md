# Item definition numbers (I-03)

Pinned `LOLG.DAT` sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`. Definition blob is GLOBAL.MIX entry `3984507021`, sha256 `b399b5c8bfea3597293a3237f30f45985efa2dd88d2dc29d5d18ca7488f60891`, record base 496, stride 91, count 170. Analysis address A is file A+`0x37000`. An object-2 dword becomes an analysis address by adding `0x59024`. No host. No test. `definitions.json` in lol2_r18 was not edited. Lead applies the graded column in I-04.

The 21 undecoded bytes are the varying offsets outside the producer's known set `{24..27, 0x2E, 0x2F, 0x32, 0x3B, 0x3C, 0x3F, 0x41, 0x42, 0x47..0x5A}`. Recount of the 170 records: `0x1C, 0x1E, 0x20, 0x21, 0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x34, 0x37, 0x38, 0x39, 0x3A, 0x3D, 0x40, 0x43, 0x44, 0x45, 0x46`. Bytes `+0x1C` and `+0x29` are equal on all 170 records.

`formula_finished` stays false. The weapon term below is one addend of the strike amount. Four other addends are player dwords.

## Grades

| Claim | Grade |
| --- | --- |
| Signed definition byte `+0x40` of the object at `[0x23348+0x2EC]` is stored at `[0x23348+0x3AC]` and added into the strike amount | PROVEN |
| That amount is the dword at context `+0x16`. The formula `0x62728` reads an amount at that same offset | The store and the formula's read are PROVEN. That the strike's virtual call reaches `0x62728` | LIKELY |
| Word `+0x3D` is copied to context `+2` as the flags word. Two branches OR `0x40` or `0x20` into the copy's low byte | PROVEN |
| Word `+0x3B` is copied to context `+0` | PROVEN |
| Word `+0x37`, when nonzero, is the index argument of `0xE3924` | PROVEN as the argument. The callee body past the index check | Not entered |
| Byte `+0x44` is zero-extended, halved when bit `0x400` of `[0x2270E]` is set, and added to dword `[0x22C5A]`. That sum is the return EAX. All five direct callers keep only AL | PROVEN. A name for the byte | UNKNOWN |
| Signed byte `+0x41` is summed from every occupied equipment pointer into `[0x23348+0x3A8]` | PROVEN. This is the defense byte already in the producer |
| Signed byte `+0x40` of the pointers at `+0x2E4`, `+0x2E8`, `+0x2F4`, and `+0x2F8` is summed into `[0x23348+0x3A4]`, which is another amount addend | PROVEN |
| Signed byte `+0x40` of the pointer at `+0x2F0` is stored at `[0x23348+0x3B0]` | PROVEN. A reader of that dword in the amount | Not found |
| Charges, price, weight, and description text | UNKNOWN |
| The other 21-set bytes (`0x1C/0x29`, `0x1E`, `0x20`, `0x21`, `0x28`, `0x2A`, `0x2B`, `0x2C`, `0x2D`, `0x34`, `0x38`, `0x39`, `0x3A`, `0x43`, `0x45`, `0x46`) have no entered meaning | UNKNOWN |

## Where byte +0x40 enters the amount

`0x88908` pushes `0x23348` and calls `0x8A364` (call at `0x88A8A`, fixup object 5 offset `0x23348`). When dword `[0x968DC]` is zero the callee returns. When it is nonzero, `0x8A578` zeros `[ebx+0x3A4]`, `[ebx+0x3A8]`, `[ebx+0x3AC]`, `[ebx+0x3B0]`, `[ebx+0x40D]`, and `[ebx+0x411]`, then switches on `byte [0x23C2D] - 1`.

The switch table is eleven object-2 dwords at `0x8A338`. Arms 0, 7, and 8 (`byte` values 1, 8, and 9) jump to `0x8A3A1`. The in-reach strike at `0x88F2E` loads that same byte and continues only when it is 1, 8, or 9 (`cmp al, 1 / 8 / 9` at `0x88F47`). The other arms write `[ebx+0x394]` and `[ebx+0x398]` from `[ebx+0x38C]` and `[ebx+0x390]` and do not walk the equipment pointers. What writes `[0x23C2D]` was not found. What `[0x968DC]` points at was not entered.

`0x8A3A1` walks six pointers at `[ebx+0x2E4]` stepping by 4. A null pointer is skipped. For each occupied pointer, EAX is the first dword, which is the definition. The definition's signed byte `+0x40` is `sar(dword [definition+0x3D], 24)`.

- Index 2, the pointer at `[ebx+0x2EC]`: the signed byte is stored at `[ebx+0x3AC]` (`0x8A40A` `8B 68 3D`, `0x8A40D` `C1 FD 18`, `0x8A410` `89 AB AC 03 00 00`). Signed byte `+0x46` is stored at `[ebx+0x411]`.
- Index 3, `[ebx+0x2F0]`: signed `+0x40` goes to `[ebx+0x3B0]`, signed `+0x46` to `[ebx+0x40D]`.
- The other four indexes add signed `+0x40` into `[ebx+0x3A4]`.
- Every occupied pointer adds signed byte `+0x41` into `[ebx+0x3A8]`. That extraction is `sar(dword [definition+0x3E], 24)`.

The strike loads the same pointer. `lea edx, [ebx+8]` at `0x88F2B`, then `mov edx, [edx+0x2E4]` at `0x88F33`, is `[ebx+0x2EC]`. It is stored at `[ebp+0x6A]`. The `mov al, [0x23C2D]` at `0x88F2E` sits between those two and does not change EDX. Its first dword is the definition used for the mask, the flags, word `+0x37`, and byte `+0x44`.

Three copies of the amount sum, at `0x88FE6`, `0x890CA`, and `0x89115`, all store the same total at `[ebp-0x7C]`:

`[ebx+0x3A4] + [ebx+0x394] + [ebx+0x39C] + sar(dword [ebx+0x3E4], 24) + [ebx+0x3AC]`

Context is `[ebp-0x92]`. `[ebp-0x7C]` is context `+0x16`. `[ebp-0x8A]` is context `+8` and holds `0x22574`. The flags word is stored at `[ebp-0x90]`, context `+2`. The mask word is stored at `[ebp-0x92]`. On the path where byte `[0x23C44]` is nonzero the copy's low byte is ORed with `0x40`. On the path where that byte is zero and byte `[0x23C43]` is nonzero, the low byte is ORed with `0x20`. The third path stores the definition word unchanged. The definition record is not written.

`0x8915C` passes this context to the target's slot `+0x80`. `0x62728` reads its amount from context `+0x16` and its attacker from context `+8`. This strike does not call `0x62728` directly. The shared layout is the reason the link is LIKELY.

On arms 0, 7, and 8, `[ebx+0x394]` is a copy of `[ebx+0x38C]` and `[ebx+0x398]` is a copy of `[ebx+0x390]`. The amount reads `[ebx+0x394]` and `[ebx+0x39C]`, not `[ebx+0x398]`. Writers of `[ebx+0x38C]`, `[ebx+0x390]`, `[ebx+0x39C]`, and `[ebx+0x3E4]` were not entered. Those four dwords are not definition fields.

Every nonzero `+0x40` in the 170 records is in 1..100, so the signed extraction equals the raw byte. Class `0x44` is 25 records, all nonzero. Class `0x48` is 12 records; only the rock is nonzero. Three class `0x43` records are nonzero and contribute only when they sit in one of the four summing slots.

## Graded weapon term (signed byte +0x40)

This is the slot-2 term. It is not the whole strike amount. A 0 means that term is 0.

| Index | Name | +0x40 |
| --- | --- | --- |
| 0 | 1-Stalagmite | 4 |
| 1 | 2-Br Mace | 6 |
| 2 | 3-Halberd | 15 |
| 3 | 4-Hand axe | 8 |
| 4 | 5-Short swd | 10 |
| 5 | 6-Fine longswd | 12 |
| 6 | 7-Long arm | 12 |
| 7 | 8-Prism | 18 |
| 8 | 9-Firestorm | 40 |
| 10 | 11-Serpent staf | 50 |
| 12 | 13-Gaunt strike | 15 |
| 13 | 14-Plasma staff | 10 |
| 14 | 15-War blade | 12 |
| 15 | 16-Ax Traitor | 50 |
| 16 | 17-Drac dagger | 8 |
| 17 | 18-Reaver of GO | 80 |
| 18 | 19-Blizzard | 50 |
| 19 | 20-Bastion | 30 |
| 20 | 21-Tho fixed | 25 |
| 21 | 22-Darkstorm | 100 |
| 22 | 23-Hrn Belial | 25 |
| 27 | 28-Dag Light | 2 |
| 29 | 30-Empty hand | 10 |
| 71 | 69-Tho enchant | 80 |
| 115 | 113-Brook flou | 25 |
| 9 | 10-Th Dagger | 0 |
| 23 | 24-Rock | 1 |
| 24 | 25-Defender | 0 |
| 26 | 27-Snare | 0 |
| 28 | 29-Lt crosbow | 0 |
| 30 | 31-Shift | 0 |
| 31 | 32-Shard | 0 |
| 32 | 33-Myriad | 0 |
| 33 | 34-Valkryie | 0 |
| 34 | 35-N valk crsbw | 0 |
| 35 | 36-Darkbow | 0 |
| 61 | 60-Stroke dager | 0 |

Same byte, other records, added only through the four summing slots:

| Index | Name | Class | +0x40 |
| --- | --- | --- | --- |
| 47 | 48-Gau Might | 0x43 | 15 |
| 81 | 79-Portrait Ken | 0x43 | 1 |
| 90 | 88-Keneths chrm | 0x43 | 10 |

G01's sentence that the sum is stored at `0x8A364` names this function's entry. The weapon-term store is `0x8A410`. G01's file values 10, 12, and 10 for the short sword, the fine longsword, and the empty hand match these records.

## What stayed unknown

No entered reader uses a definition byte as a remaining charge, a price, or a weight. Byte `+0x45` is 0..9 on the weapon rows and 0 on every other class. Byte `+0x46` is stored for slots 2 and 3 and was not read back here. Byte `+0x43` bit `0x10` is tested by an unreferenced function at `0x935D4` (`and al, 0x10` / `ret`) and by the strike at `0x894E0` before `call 0x89C40`. `0x89C40` was not entered. Short functions at `0x93594`..`0x93624` return bytes `+0x44`, `+0x45`, `+0x43`, the mask, the flags, word `+0x37`, signed `+0x41`, signed `+0x40`, and the class byte. No direct call and no stored object-2 pointer to them was found. They are not the live readers.

Word `+0x37` is passed to `0xE3924` with object `0x23C68` when the word is nonzero. The callee rejects the index when it is at least the count at `[object+0x1C]`. The body after that compare was not entered.

Byte `+0x44` is the addend described above. The five callers of `0x88D2C` (`0x7DAC0`, `0x7DF7F`, `0x7E19B`, `0x7E279`, `0x7E7AA`) each keep AL of the returned sum and branch on it being zero. They do not store the full sum. The byte is not named.

The name table is 30 bytes per record. The bytes after it are not description text. The text file was not located.

Difficulty byte 1, already posted, leaves the formula's amount unchanged. It does not change this definition byte.

## Apply

Lead, I-04. Put the `+0x40` column on the generated definitions as the graded weapon term. Leave the unknown offsets raw. Do not invent charges, prices, or a speed number.
