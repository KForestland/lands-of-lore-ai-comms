# Q01 creature blow amounts

Not posted. Difficulty byte 1.

## Proven this pass

Creature strike is `FUN_000a6ae3` (file offset `0xDDAE3`). Its only direct callers of the formula are this function and `0x89E7C`. Ghidra listed no direct caller of `0xA6AE3`.

Before `call 0x62728` at `0xA6CBE` (file `0xDDCBE`):

- Context+`0x22` and context+`0x26` get the target's word +`0x88` (`0xA6C69`, file `0xDDC69`).
- Definition pointer is `[actor+0x2C]`. Byte +`0x83` of that record is loaded at `0xA6C63` (file `0xDDC63`). A zero byte becomes 1. The value is stored at context+`0x1A` (`0xA6C88`).
- The third argument is that definition pointer. The second is actor byte +`0xA7`.
- This function reads context+`0x16` at `0xA6B7B` and does not write it. That read is the half-amount passed to slot +`0x94` when actor byte +`0x91` is `0x3D` and flag bit 0 of context+2 is set.

`0x62728` uses context+`0x16` as the amount. If that dword is negative, `0x62744` copies context+`0x22` into it. The first sixty instructions do not read context+`0x1A`. A scan of the function found no `+0x1A` operand. The integer written to context+`0x1E` is still the formula's ceiling of the fixed-point amount, then the min with context+`0x22`, as posted in R-01.

## Not yet graded

Which store fills context+`0x16` for an L8, L9, or L10 creature. The population field `damage: [15]` is `damage_base_adapter` in `prepare_act2_creatures.py`. It is the port constant, not a definition byte. No blow table yet. LAMPLT, StSquid, WILD, SKEL, and the Saar are unread for this amount.
