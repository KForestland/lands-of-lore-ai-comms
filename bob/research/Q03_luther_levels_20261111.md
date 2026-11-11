# Q03 Luther's health, might and level

complete true

formula_finished false

A new Luther's health cap is 8, and current health is that same 8. Health, might and magic are not rows in the file. One crossing of the first threshold adds 6, 7 or 8 to the cap, so the cap is then 14, 15 or 16. The executable does not hold an Act 1 experience total, so a Luther who leaves Act 1 without 250 in the first bank is still at 8. No host.

Pinned LOLG.DAT sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`. Code address A is file A+`0x37000`. Capstone from the function entries below.

## What the two functions add

PROVEN. `0xD8A1C` (file `0x10FA1C`) is the bank at player `+0x159`, index byte `+0x161`. `0xD8B94` (file `0x10FB94`) is the bank at `+0x15D`, index byte `+0x162`. Both index the same 31 dwords. The fixup on the load at `0xD8A77` is object 5, offset `0xE810` (record `0700530a0510e8`). The image is file `0x1CF834` through `0x1CF8AF`.

`0xCFA18` stores the new-Luther row, then copies the caps into the current dwords. Callers `0x9C87C`, `0xB97E8` and `0xCB298` push `0x22574`.

| Dword | Init | Site | File |
| --- | --- | ---: | --- |
| `+0x159` first bank | 0 | `0xCFAA2` | `0x106AA2` |
| `+0x15D` second bank | 0 | `0xCFA98` | `0x106A98` |
| `+0x161` first index | 1 | `0xCFB07` | `0x106B07` |
| `+0x162` second index | 1 | `0xCFB00` | `0x106B00` |
| `+0x149` health cap | 8 | `0xCFB0E` | `0x106B0E` |
| `+0x14D` current health | copy of `+0x149` | `0xCFCDB` / `0xCFCE7` | `0x106CE7` |
| `+0x151` might | 5 | `0xCFB22` | `0x106B22` |
| `+0x155` magic | 10 | `0xCFB2C` | `0x106B2C` |
| `+0x141` pool cap | 20 | `0xCFB18` | `0x106B18` |
| `+0x145` current pool | copy of `+0x141` | `0xCFCF5` / `0xCFCFE` | `0x106CFE` |
| `+0x17D` | 0 | `0xCFB77` | `0x106B77` |

While the index byte is at most `0x1E` and the bank is not below `table[index]`, the body subtracts that dword, increments the byte, and rolls. The subscript is the index byte itself. A new Luther starts at 1, so dword 0 is not consumed, and dword 30 is the sentinel `0x7FFFFFFF`. The bank is replaced by `0x7FFFFFF0` when a sum is not below `0x7FFFFFFF`, so index 30 does not complete. The live costs are indexes 1 through 29.

Each crossing of `0xD8A1C` calls `0x12415C(0x221D8, 0, bound)` and uses `sar(eax, 5)`.

| Bound | Return | After the shift and the add | Stored at |
| --- | --- | --- | --- |
| `0x5F` | 0..95 | 6, 7 or 8, 32 values each | `+0x149`, and `+0x14D` when `+0x17D` is 0 |
| `0x3F` | 0..63 | 1 or 2, 32 values each | `+0x151` |
| `0x3F` again | 0..63 | 1 or 2, 32 values each | `+0x155` |

`0xD8B94` uses bound `0x9F`. The return is 0..159. After the shift, adding `0xB` gives 11, 12, 13, 14 or 15, 32 values each. That sum is added to both `+0x141` and `+0x145`. This function does not write `+0x151` or `+0x155`.

The roll is `0x12415C` (file `0x15B15C`), return at `0x1241CD`. The state dword is `[0x221D8]`, past the object-5 file image, so the seed is not in the file. The step is `state * 0x41C64E6D + 0x3039`, then bits 10..24, masked down to the span. Equal bounds return the bound. The particular sequence is runtime.

## Experience thresholds

PROVEN. File `0x1CF834 + index * 4`. These are the costs subtracted on a crossing, not a running total. Index 1 costs 250, then index 2 costs another 500.

| Index | Cost | File |
| ---: | ---: | --- |
| 0 | 0 | `0x1CF834` |
| 1 | 250 | `0x1CF838` |
| 2 | 500 | `0x1CF83C` |
| 3 | 750 | `0x1CF840` |
| 4 | 1000 | `0x1CF844` |
| 5 | 1250 | `0x1CF848` |
| 6 | 1500 | `0x1CF84C` |
| 7 | 1750 | `0x1CF850` |
| 8 | 2000 | `0x1CF854` |
| 9 | 2250 | `0x1CF858` |
| 10 | 2500 | `0x1CF85C` |
| 11 | 2750 | `0x1CF860` |
| 12 | 3000 | `0x1CF864` |
| 13 | 3250 | `0x1CF868` |
| 14 | 3500 | `0x1CF86C` |
| 15 | 3750 | `0x1CF870` |
| 16 | 4000 | `0x1CF874` |
| 17 | 4250 | `0x1CF878` |
| 18 | 4500 | `0x1CF87C` |
| 19 | 4750 | `0x1CF880` |
| 20 | 5000 | `0x1CF884` |
| 21 | 6000 | `0x1CF888` |
| 22 | 7000 | `0x1CF88C` |
| 23 | 8000 | `0x1CF890` |
| 24 | 9000 | `0x1CF894` |
| 25 | 10000 | `0x1CF898` |
| 26 | 11000 | `0x1CF89C` |
| 27 | 12000 | `0x1CF8A0` |
| 28 | 13000 | `0x1CF8A4` |
| 29 | 15000 | `0x1CF8A8` |
| 30 | 2147483647 | `0x1CF8AC` |

## What feeds +0x14D

PROVEN for the three writers entered here. Current health starts as the cap, 8, at `0xCFCE7`. A crossing adds the same 6, 7 or 8 when `+0x17D` is 0 (`0xD8AC4` tests, `0xD8AC8` adds, file `0x10FAC8`). The new-game store of `+0x17D` is 0. R01's receive `0xD6A08` adds a later difference and clamps the sum to `+0x149`. That body was not re-entered.

After the index changes, `0xD8B15` pushes the cap and the current health to `0x7CADC(0x23819)`, copies might and magic to `[0x236D4]` and `[0x236D8]`, and calls `0x8A364(0x23348)`. That is the path Q02's strike reads.

## The one line

A new Luther's health cap is 8. The first bank must reach 250 before the cap moves, and the move is +6, +7 or +8. An Act 1 total for that bank is not in this table.
