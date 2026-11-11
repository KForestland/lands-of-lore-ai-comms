# Q02 Luther's strike before the weapon byte

complete true

formula_finished false

The amount before the weapon byte is one sum of four player words. For the Luther stated below it is 5. With the short sword the dword stored at context+0x16 is 15. With the fine longsword it is 17. No host. I03 was not rewritten. `0x62728` still scales that stored dword, so the hit points a creature keeps stay outside this note.

Pinned LOLG.DAT sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`, size 1977007. A code address A is file A+`0x37000`. Capstone, from instruction boundaries. The weapon bytes 10 and 12 are I03's graded column, not re-read here.

## The sum

PROVEN. `0x88D2C` is the strike. All five callers push 0 and `0x23348`, then call it, then keep AL: `0x7DAC0`, `0x7DF7F`, `0x7E19B`, `0x7E279`, `0x7E7AA`. Each site is `6A 00 68 48 33 02 00 E8`. AL is the byte-`+0x44` addend from I03. It is not this amount.

`0x88D3E` loads ebx from `[ebp+0x9A]`. After `sub ebp, 0x86` that slot is argument 0, so ebx is `0x23348` on these calls.

The first sum, file `0xBFFE6`:

- `0x88FE6` loads `[ebx+0x3A4]`
- `0x88FEC` loads `[ebx+0x394]`
- `0x88FF4` loads `[ebx+0x39C]`
- `0x88FFC` loads `[ebx+0x3E4]`, and `0x89002` is `sar eax, 0x18`
- `0x89005` (file `0xC0005`) is the four-term total, in eax
- `0x89007` (file `0xC0007`) loads `[ebx+0x3AC]`, the weapon byte
- `0x8900D` adds it
- `0x8903E` (file `0xC003E`) stores the five-term total at `[ebp-0x7C]`

`[ebp-0x92]` receives the mask word and `[ebp-0x90]` the flags word in the same window, so `[ebp-0x7C]` is context+`0x16`. The sites at `0x890CA` and `0x89115` begin with the same three displacements, `+0x3A4`, `+0x394`, `+0x39C`. The strike does not call `0x8A364`. It reads the words the last recompute left.

The amount before the weapon add is:

`[0x23348+0x394] + [0x23348+0x39C] + [0x23348+0x3A4] + sar([0x23348+0x3E4], 24)`

`sar` by 24 is the signed byte at `+0x3E7`.

## Which words

PROVEN on the equipment arm of `0x8A364`. That arm runs when `[0x968DC]` is nonzero and byte `[0x23C2D]` is 1, 8, or 9 (`0x8A393` jumps to `0x8A578`, then the switch at `0x8A5CF`). The strike itself accepts only those three byte values.

| Word the sum reads | What was stored there | Site |
| --- | --- | --- |
| `[ebx+0x394]` | copy of `[ebx+0x38C]` | `0x8A424` / `0x8A42A`, file `0xC1424` |
| `[ebx+0x38C]`, absolute `[0x236D4]` | player `[0x22574+0x151]` | `0xCFDF5`, `0xD8B4B`, `0xD8C77` |
| `[ebx+0x39C]`, absolute `[0x236E4]` | 0 at construction; champion stone adds 20 | `0x86F85`; `0x961BF` / `0x961C7` |
| `[ebx+0x3A4]` | signed byte `+0x40` of occupied slots 0, 1, 4, and 5 | zero `0x8A58C`, add `0x8A3DC` |
| byte `[ebx+0x3E7]` | 0 when slot 2's pointer is not null | zero `0x8A596`; the negate at `0x8A45E` is the empty-slot arm |

`[ebx+0x398]` is the copy of `[ebx+0x390]`, and that word is the copy of player `+0x155`. The sum loads `+0x394` and `+0x39C`. Equip `0x90020` writes the item pointer at `[base+index*4+0x2E4]` and then calls `0x8A364(0x23348)` at `0x90033`. That call refreshes `+0x394`, `+0x3A4`, `+0x3AC`, and `+0x3E7`. It does not write `+0x39C`.

Player `+0x151` starts at 5. `0x9C87C`, `0xB97E8`, and `0xCB298` each push `0x22574` and call `0xCFA18`. That function stores the 5 at `0xCFB22` (`C7 83 51 01 00 00 05 00 00 00`, file `0x106B22`). A fourth caller, `0xCF9D4`, pushes ebx. The same block stores 10 at `+0x155` (`0xCFB2C`) and 1 at bytes `+0x161` and `+0x162` (`0xCFB00`, `0xCFB07`). `0xCFDD4` loads `+0x151` into edx and `0xCFDF5` (file `0x106DF5`) stores edx at `[0x236D4]`. Those three absolute stores are the only direct writes of `[0x236D4]` in the code object. `0xD8B4B` and `0xD8C77` are the level-up copies, after `0xD8A1C` or `0xD8B94` has changed the player dwords. A Luther whose byte `+0x161` is still 1 has not taken that add, so `+0x151` is still 5, and `[0x236D4]` is still 5.

`+0x39C` of the controller is 0 after construction. `0xCFD36` pushes `0x23348` and calls `0x76CB0`. `0x76CB9` puts argument 0 in esi. `0x76E66` pushes esi and calls `0x86EF8`. `0x86EFC` puts that pointer in edi, and `0x86F85` stores 0 at `[edi+0x39C]`. The champion-stone arm loads `[0x236E4]`, adds `0x14`, and stores it back at `0x961C7` (file `0xCD1C7`), then calls `0x8A364`. The remove arm stores at `0x9633C`. Those two are the only direct writes of `[0x236E4]`. The tick that increments `[ebx+0x39C]` at `0x7F402` sits in `0x7F200`. Its callers pass `0x23819`: `0xD120F` moves that immediate, and `0x7AA79` pushes the ebx of `0x797A4`. The only direct caller of `0x797A4` is `0x7735A`, which pushes `[esi+0x4D1]`. esi is argument 0 of `0x772C0` (`0x772D0`), and the four callers `0xE08DE`, `0xEE226`, `0xEF3FB`, and `0xF1301` each push `0x23348`. `0x23348+0x4D1` is `0x23819`. That tick writes `[0x23BB5]`, not `[0x236E4]`.

The table byte at `0x82816` is the same split. `0x82748` is called with ebx from that dispatcher (`0x7AD03`) or with the immediate `0x23819` (`0xD096F`). It stores the looked-up byte at `[ebx+0x38C]` of `0x23819`. It is not a store to `[0x236D4]`.

`0xDD7F4` would store its second argument at `[arg+0x38C]` and call `0x8A364`. The code object has no `E8` to `0xDD7F4` and no immediate of the entry or of its object-2 offset `0x847D0`. It is not on this path.

The high byte stays 0 while a weapon is in slot 2. `0x8A596` stores 0 before the switch. `0x8A442` tests slot 2 at `[ebx+0x2EC]` and jumps over the negate at `0x8A45E` when the pointer is not null. Both direct callers of `0x81DFC`, which writes `[ebx+0x3E4]`, push `0x23819` (`0x7ACAA`, `0xA6F0E`). The word stores around `0x8B0F6` are `mov word [ebx+0x3E4], imm16`. They do not reach `+0x3E7`.

`[0x968DC]` is the return of `0x14FBE0`, stored at `0x77707`. The callee was not entered. A zero return makes `0x8A364` store 0 at `+0x3A4` and `+0x3A8` and return, so the weapon byte never reaches `+0x3AC`. The worked numbers are the other arm, the one that runs when the dword is nonzero.

## The two numbers

PROVEN as the equipment arm's arithmetic. The Luther is the one `0xCFA18` just built: byte `+0x161` is 1, dword `+0x151` is 5, controller `+0x39C` is still 0, and slots `+0x2E4`, `+0x2E8`, `+0x2F4`, and `+0x2F8` are empty. Slot `+0x2EC` holds the named weapon. Byte `[0x23C2D]` is 1, 8, or 9, and `[0x968DC]` is nonzero, so equip's call at `0x90033` took `0x8A578`.

| Term | Value |
| --- | --- |
| `[+0x394]`, from `+0x151` | 5 |
| `[+0x39C]` | 0 |
| `[+0x3A4]`, four empty slots | 0 |
| `sar([+0x3E4], 24)` | 0 |
| Amount before the weapon byte | 5 |
| Short sword, I03 byte `+0x40` = 10, context+`0x16` | 15 |
| Fine longsword, I03 byte `+0x40` = 12, context+`0x16` | 17 |

The champion stone makes the second term 20 and the pre-weapon amount 25. That Luther is not the one in the table. A later pass of `0xD8A1C` adds to `+0x151` and copies the new dword to `[0x236D4]`. The addend is `(return of 0x12415C >> 5) + 1` with bound `0x3F`. `0x12415C` was not entered. That step is Q03. This Luther is the one before it.

Player `+0x155` is 10 at the same init and is copied to `[0x236D8]`. The strike sum does not load it.
