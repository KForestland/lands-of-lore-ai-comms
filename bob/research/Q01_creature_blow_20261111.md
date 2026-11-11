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

Which store fills context+`0x16` when an L8, L9, or L10 creature strikes Luther. The population field `damage: [15]` is `damage_base_adapter` in `prepare_act2_creatures.py`. It is the port constant, not a definition byte. No blow table yet. LAMPLT, StSquid, WILD, SKEL, and the Saar are unread for this amount.

## Proven while the K90 Godot slot was busy

Creature vtable object-5 `0x58D0` (file `0x1C68F4`). Slot +`0x80` is `0xA6AE0`. The Ghidra entry `0xA6AE3` is three pushes later (`push ebx; push esi; push edi`). That slot is the creature's receive-hit. It does not write context+`0x16`.

Slot +`0xE4` (`0xA6A88`) returns definition byte +`0x83`, or 1 when that byte is 0. The same byte is what `prepare_act2_creatures.py` stores as `reward_scale`. `0xAAA74` compares it with the average of the player's slot +`0xE4` and slot +`0xE8` bytes. It is not the outgoing blow.

Player hit is `0xD03B8`. It writes player byte +`0x161` at context+`0x1A` and the health dword +`0x14D` at context+`0x22` and +`0x26`. It does not write context+`0x16`. It then calls `0x89E7C`. The scalar that call pushes to `0x62728` is 0, or the sum of the dwords at +`0x398`, +`0x3A0`, and +`0x3A8`, depending on bit 24 of `[0x2279A]` (`shl 7` / `shr 0x1F` at `0x8A045`).

`0x67820` does write context+`0x16`, from the target's own slot +`0xE4`, then calls the target's slot +`0x80`. On a creature that amount is byte +`0x83` scaled by the preset kind (kind 5 times 5, kind 6 times 10, kind 9 the byte, kind `0x0B` the byte divided by 5). The attacker field is 0. That is a preset effect on the creature, not the creature striking Luther. Kind `0x0D` is the guck arm already posted in BK13.

Script handlers at `0x96942`, `0x96B06`, `0x9822C`, and `0x82280` store a constant 1, 0, or `0x14` and call `0xD03B8`. `0x988B0` stores a sum of the dwords at `0x236DC`, `0x236E4`, `0x236EC`, `0x236F4`, and the high byte at `0x2372C`. None of those reads a creature definition.
