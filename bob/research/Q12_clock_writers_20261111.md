# Q12 Writers of the two kind-2 clocks

complete true

formula_finished false

Word `[0x22C58]` and dword `[0x22C5A]` are fields of controller `0x227A4`. `0xE066C` writes them at `0xE0C82` and `0xE0CD2` when its first argument is that controller. The main loop calls it at `0x14F647`. Each key-480 interrupt contributes 32 units to the word. The dword gains one eighth of a unit per interrupt, which is `1193182/19880` per second on a standard PIT. Sixty dword-units are `1192800/1193182` seconds. A movie entered through `0xCF3C0` holds that main-loop call until the movie loop returns, and the next sample is clamped to 480. Bits 0, 1, and 2 of `[0x22CDC]` all set skip the same call. No menu function was found that sets those bits. No host. No piece.

Pinned LOLG.DAT sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`, size 1977007. A code address A is file A+`0x37000`. Capstone from `0xE066C`, `0xE0A43`, `0xE0B5E`, `0x14F185`, `0x14F61E`, and `0xCF3C0`. Object-5 fixups use page `1 + (address - 0x59024) / 4096`. The two known loads at `0x9D9C6` (offset `0x223E0`) and `0xB8BE7` (offset `0x22C5A`) match that page. R03 is not rewritten.

## Writers

PROVEN. `0xE066C` pushes ebx, esi, edi, and ebp, then `mov ebp, esp`, so the first argument is `[ebp+0x14]` and the second is `[ebp+0x18]`. `0xE0678` loads the first into ebx. `0xE067E` compares ebx with `0x227A4` and jumps to `0xE0768` when it matches. The other arm returns at `0xE0767` and does not reach the stores.

`0xE0768` keeps that ebx. From there through `0xE0C82` no instruction writes ebx. The stores are:

- `0xE0C82` `mov word ptr [ebx+0x4B4], ax`, which is word `[0x22C58]`
- `0xE0CD2` `mov dword ptr [ebx+0x4B6], eax`, which is dword `[0x22C5A]`

An object-5 scan of every code fixup page found no absolute store of either address. The hits are loads. R03's absolute scan missed these two writes because they are base plus displacement. `[0x22C54]`, the Spark aura step from Q08, is a different global.

The main loop at `0x14F185` reaches the call on the arm that does not take the three-bit jump below. `0x14F63D` pushes `0x22574`, `0x14F642` pushes `0x227A4`, and `0x14F647` calls `0xE066C`. `0x14F61E` has already called `0xB30AC`. The `je` at `0x14F638` skips only the vtable slot at `[eax+0x7C]`.

Eleven direct `E8` sites call `0xE066C`: `0xA05BD`, `0xA0BF9`, `0xA14EE`, `0xAEEA4`, `0xAEF1B`, `0xB938C`, `0xBB347`, `0xBC88A`, `0xC9821`, `0xDFF7E`, and `0x14F647`. The aligned windows push `0x227A4` and `0x22574`. The windows before `0xA0BF9`, `0xA14EE`, and `0xAEEA4` were not aligned, so those three arguments stay unread.

One skip is earlier than the stores. `0xE0A43` loads `[ebx+0x4A0]`. Zero jumps to `0xE0F90`, which is `mov esp, ebp` and the four pops and `ret`. That pointer is the timer object Q06's constructor fills. An empty pointer does not publish a sample.

The compare at `0xE0AD2` does not skip the stores. Elapsed from `0x14FA79` on `[ebx+0x4A0]` is compared with a threshold. Below the threshold, the arm jumps back to `0xE0AC1` and samples again. At or above it, `0xE0B5E` falls through `0xE0BE4` into both stores. The threshold is 8, 16, or 24:

| `[0x22398]` | `[0x223D6]` | `[0xE890] == 0x5D18` | Threshold |
| --- | --- | --- | --- |
| 0 | either | yes | 24 |
| 0 | either | no | 16 |
| nonzero | 0 | yes | 8 |
| nonzero | 0 | no | 16 |
| nonzero | nonzero | yes | 24 |
| nonzero | nonzero | no | 16 |

`0x22398` is one byte in the block stored with `0x22390` through `0x2239E` at `0xBFF06`, `0xCB919`, and `0xCBEBF`. It changes the sample size. It is not a stop flag.

## Unit

PROVEN for the conversion below the clamp. `0xE0BE4` calls `0x14FA79` on the key-480 timer. The return is clamped to `0x1E0` (480) at `0xE0C11` and stored in a ring of four samples. The sum is `[ebx+0x4BA]`. `0xE0C43` through `0xE0C56` turn that sum into `sum * 2048`, and `0xE0C62` clamps the product to `0x80000` (a sum of 256).

`0xE0C79` adds the fraction at `[ebx+0x529]`. `0xE0C7F` shifts right 8. `0xE0C82` stores the word. Below the clamp the word is `sum * 8`, plus that fraction. `0xE0CC0` adds the other fraction at `[ebx+0x52D]`. `0xE0CCF` shifts right 16. `0xE0CD2` stores the dword. Below the clamp the dword is `sum / 32`, plus that second fraction. A word of 1024 is a dword of 4 only apart from those two fractions.

Each new sample stays in the sum for four calls. Each call contributes 8 times the sample to the word, so one key-480 interrupt contributes 32 word-units. The same interrupt contributes `32/256 = 1/8` of a dword-unit.

This session re-read `0x167BDB` and `0x167BE0`: eax is `0x1234DC` (1193180) and `div dword [ebp+0x14]` produces the PIT divisor. Q06 entered the key-480 registration and the port `0x40` write. `0x1234DC / 480` is 2485. On a standard PIT of 1193182 Hz the interrupt rate is `1193182/2485` Hz. The code's own dividend is two counts lower.

Word-units per second are `32 * 1193182 / 2485`. Dword-units per second are `1193182 / 19880`, which is 60 and `382/19880`. Sixty dword-units are `1192800/1193182` seconds. R03's reload multiplies by the word `[0x223A8]`, and the only absolute store of that word writes 60. A countdown that R03 selects the dword for, stored as `N * 60`, is N of those intervals when each published dword is subtracted once. The open main-loop path calls the expiry walk at `0x14F61E` and then publishes at `0x14F647`, so the walk subtracts the previous publish. Q06's sentence that the stream is 32 key-480 ticks per second is the 32 word-units per interrupt, at this interrupt rate.

A sample that arrives above 480 is stored as 480. Time since the previous sample beyond 480 counts is not added.

## Movies

PROVEN for the player this session entered. `0xCF3C0` is a direct callee of `0x14F02C` in the startup path that also calls `0x9BCF8(0x22CD8)`, and of `0xCF31B`, and of twelve sites from `0x95ECA` through `0x9A669`. The opcode 21 note already entered this function as the `.vqa` player. This session did not re-walk that switch.

Inside `0xCF3C0`, `0xCF5F7` calls `0x15ACC1`, then `0x15ACEE` when that return is nonzero, then `0x15E6C8`, then the dwords at `[0xE890]+0x48` and `[0xE890]+4` when they differ from the zeroed esi. `0xCF674` tests ebx and jumps back to `0xCF5F7` while ebx is 0. ebx becomes 2 when the polled low byte is `0x6E` or equals `[0x2235C]` or `[0x22360]`, and becomes 1 when `0x15E6C8` returns -2. The loop does not call `0xE066C`. `0x15ACC1` returns without a call. `0x15ACEE` reads the key ring at `[0x1890D]`. `0x15E6C8`'s direct calls are `0x171EB4`, `0x16D66C`, `0x171A98`, `0x172BE4`, `0x172C38`, `0x171ABC`, `0x16DBF4`, and `[ebx+0x50]`. None is `0xE066C`.

The caller does not resume until that loop ends. `0xB30AC` at `0x14F61E` returns before `0x14F647`, and `0xA03DC` at `0x14F71C` is the other script walk on the same loop. A movie entered from either walk holds the next publish. The publish that follows is one sample, clamped to 480, so the movie's real length is not added.

## The three-bit skip

PROVEN as a skip. Not named as a menu.

`0x14F192` loads `[0x22CDC]`. `shl` by `0x1D` and `0x1E` extract bits 2 and 1, and `and ebx, 1` extracts bit 0. `0x14F1B5` jumps to `0x14F707` when all three are set. `0x14F707` clears esi, stores 0 at `[0x223C8]`, calls `0x7555C` and `0xA03DC`, and jumps to `0x14F185`. It does not call `0xE066C`.

The same three bits are tested again at `0x14F4E1`. That jump lands at `0x14F52D`, which is before the clock call, so it does not remove the publish.

No object-5 fixup writes `[0x22CDC]`. The relocated references are loads (`A1` and `8B 1D` / `8B 15`). A scan for `or` of 1, 2, 4, or 7 into `[reg+4]` found `0x9DEE4` (`or byte [eax+4], 1`) and two byte ors inside the frame function at `0x15E93F` and `0x15E94A`. The object in eax at `0x9DEE4` was not reduced to `0x22CD8`. The bytes `PAUSED`, `NOTIMER`, and `NORATE` at file `0x1C46A8` sit with `NOAUDSIZ`, `AUDSYNC`, and `SETLOOP`. That is the audio library's token table. `options.shp` is opened at `0x6FDBE` during an asset load that returns. Neither is this dword.

`[0x223C4] == 0` at `0x14F185` jumps to `0x14F735`, which is past the loop's backward jump at `0x14F730`. That leaves the loop body. What stores that dword was not read.

## Unread

- Which function sets bits 0, 1, and 2 of `[0x22CDC]`.
- The calls nested under `0x15E6C8` past the direct list.
- The three unaligned callers of `0xE066C`.
- Whether a later menu loop, other than `0xCF3C0`, calls one of those callers.
