# Q11 Placement reward_scale and the loot dword

complete true

formula_finished false

`reward_scale` is definition byte +`0x83`. Creature slots +`0xE4` and +`0xE8` return that byte, and a 0 becomes 1. Formula kind 2 uses the attacker's byte over the target's byte. A call of `0x67820` with kind argument 5 builds a hit whose amount is that byte times 5 when the object is a creature. The loot field is placement dword +52, stored at actor +`0x74` on spawn. The death function does not read it. The attack path passes it on only when the target is the player and a shifted roll is strictly below definition byte +`0x3B`.

Pinned LOLG.DAT sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`, size 1977007. A code address A is file A+`0x37000`. Capstone from `0x62728`, `0x67820`, `0xA2127`, `0xA2283`, `0xA5780`, `0xA6A88`, `0xA6AA8`, `0xA6C40`, `0xA7544`, `0xD0BEC`, and `0x77F7C`. Object-2 fixup is raw dword + `0x59024`. Population files are the of9 `scripts/lol2/act2_populations/*.json`. Placement bytes were re-read from the level MIX at each row's `placement_offset`. No host. No piece.

## The scale byte

PROVEN. `0xA6A88` and `0xA6AA8` each take the actor, load `[actor+0x2C]`, and return byte `[definition+0x83]`. A zero byte returns 1.

Those two functions are the slots beside the hit slot. The pointer table that holds raw `bc da 04 00` at slot +`0x80` (that is `0xA6AE0`, the hit receiver from Q01) holds raw `64 da 04 00` at +`0xE4` and raw `84 da 04 00` at +`0xE8`. Adding `0x59024` gives `0xA6A88` and `0xA6AA8`. The bytes were read from object index 4 at offset `0x59B4`, which is `0x58D0+0xE4`. The spawn stores `0x58D0` at actor +`0x28` (`0xA22DE`).

The hit receiver copies the same byte into the hit context. From `0xA6C5E`: load the definition, `mov cl, [eax+0x83]` at `0xA6C63`, coerce 0 to 1, store the current health word at context+`0x22` and context+`0x26`, store the scale at context+`0x1A` (`0xA6C88`). The formula then overwrites context+`0x26` with remaining health at `0x62F60`, and clamps a negative remainder to 0 at `0x62F67`. The formula body has no read of context+`0x1A`.

## Where the returned byte is used

PROVEN for kind 2 of `0x62728`, in the linear stream from that entry. At `0x629D6` the arm loads context+8, which R01 identified as the attacker, and calls its slot +`0xE8`. It shifts the amount at context+`0x16` left by 16 and multiplies by that byte (`0x629EE`, `0x629F4`). At `0x629FE` it calls slot +`0xE8` on context+4, the target, and divides (`0x62A16`). The quotient is stored at `[esp+0x34]` (`0x62A1B`). R01's later ceiling shift turns that fixed-point value into the integer at context+`0x1E`.

On a creature, both slots return definition +`0x83` or 1. On the player, BK13 entered slot +`0xE8` as the byte at +`0x162`. This note did not re-enter the player function. A new Luther's +`0x162` is 1 (Q03). Q01's creature blow builds kind 1, and kind 1 does not take this arm. The ratio runs when the context kind is 2.

PROVEN for one arm of `0x67820`. The argument byte is compared after subtracting 5 (`0x6783C`). The jump table at `0xE7B0` is object 2. Index 0, kind argument 5, lands at `0x67857`. That arm calls slot +`0xE4`, multiplies the byte by 5 (`lea eax, [edx*4]` / `add eax, edx` at `0x67889`), and raises a 0 result to 1. It stores that product at context+`0x16`, sets the context kind byte to 3, and calls slot +`0x80`. When the object is a creature, the product is `reward_scale * 5`. When the object is the player, BK13's slot +`0xE4` is the byte at +`0x161` instead. The four direct callers pass the kind in the high byte of a preset dword (`0xB0844`, `0xB2FC9`, `0xD37EB`, `0xD6794`). Which preset selects kind 5 was not walked.

The `*10` body inside `0xD0BEC` is real and is not this path. From the entry `0xD0BEC`, modes 1 and 5 meet at `0xD0C8A`. When context+`0x26` is 0, `0xD0CAF` sets the working value to context+`0x1A` times 10. When context+`0x26` is nonzero and context+`0x32` is nonzero, `0xD0CCA` uses times 3. A positive result for mode 1 or 5 is passed to `0xD8A1C`. Both direct callers of `0xD0BEC` store mode 2: `0xA4AA5` and `0xFB534`. Mode 2 reads effect byte 1 at `0xB95D` (`0xD0CDF`) and does not take the times-10 arm. No other `E8` calls `0xD0BEC`. The hit context's copy of the scale is therefore not shown reaching that arm.

## The loot dword

PROVEN store. `0xA2283` copies `0x38` placement bytes to `[ebp-0x44]`. The same function's tail, reached by `jmp 0xA2110` at `0xA246A` and by the bit-`0x20` arm at `0xA210C`, all three nibble paths of `[ebx+0x70]` arrive at `0xA2127`. That instruction stores 0 at actor +`0x78`. `0xA212E` loads `[ebp-0x10]`. `0xA2131` stores it at actor +`0x74`. `[ebp-0x44+0x34]` is `[ebp-0x10]`, so the stored dword is placement +52. A zero dword is stored as zero. The item-list head +`0x78` starts at 0.

PROVEN the death function does not read it. A zero remaining-health argument to `0xA7A74`, with behavior not 15, definition byte +`0x3C` bit `0x10` clear, and actor +`0xB5` bit 1 clear, calls `0xA7544` (`0xA7AC6`). Inside that function, `0xA77DF` stores behavior 15 and `0xA77EB` stores health word 0. The second argument from this caller is 0, so `0xA780C` jumps to `0xA7A15`. The index there is bits 1 and 2 of byte +`0xB7` (`shl 5` / `shr 0x1E` at `0xA7A22`). The table at `0x4E510` is object 2 and lands on `0xA7850`, `0xA7849`, `0xA78E8`, and `0xA7997`. Those four arms start a selector or an effect. None reads actor +`0x74`.

PROVEN one reader on the attack path, from the aligned stream at `0xA5780`. After the target's slot +`0x80` returns, `0xA57EF` compares actor +`0x74` with 0 and actor +`0x38` with `0x22574`. Both must pass. It then calls `0x12415C(0x221D8, 0, 0x1FDF)`, shifts the return right by 5, and continues only when that value is strictly below definition byte +`0x3B` (`0xA581C`, `setl`). `0xA582A` loads the dword and `0xA5833` calls `0x77F7C(0x23348, dword, 1)`. The return is stored at actor +`0x34`.

`0x77F7C` calls `0x77BD0` and, when that returns nonzero, calls `0x95894` with the player `0x22574`. `0x77BD0` walks the list at `[0x23348+0x90F]` for a node whose definition +`0x18` equals the dword. A miss calls `0x88908`. That callee was not entered.

Q03 entered `0x12415C`. Its return is 0 through the bound, and this note did not replay bound `0x1FDF`. A non-negative return shifted right by 5 is not below a zero byte. Four of the five rows store 0 at +`0x3B`, so this grant does not run for them on that generator. WORM stores 50.

A second reader is `0xA2A38`, on the stream through `0xA29F0`. It runs when a local equals 3 and actor +`0xB5` bit `0x10` is set. It passes actor +`0x74` and the list head +`0x78` to `0x9BA88`, then stores the returned list head. The local's event number was not named. `0xA998B` compares an argument with actor +`0x74` while walking the actor array at `[0x9696C]`.

`0xA0C8F`, `0xA1584`, and `0xAD7B4` are calls through the global at `[0xE890]`. They are not the actor field.

## Five rows

The record name sits at definition +`0x87`. Byte +`0x83` is the scale. Placement files matched `placement_hex`, and dword +52 matched the JSON loot. L9 also has scales 14 and 25. The five rows below are the distinct asked values plus one scale outside that set, and one nonzero loot whose +`0x3B` can pass.

| Level | Actor | Name | Record file | +0x83 | +0x3B | Placement file | Dword +52 |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| L9 | 61 | StSquid | 23602319 | 8 | 0 | 23374324 | 0 |
| L10 | 71 | SKEL | 13809875 | 10 | 0 | 13152742 | 0 |
| L8 | 81 | WILD2 | 13808469 | 12 | 0 | 13543370 | 514 |
| L8 | 22 | DANIEL | 13808763 | 15 | 0 | 13540066 | 16712194 |
| L9 | 0 | WORM | 23602907 | 20 | 50 | 23370908 | 552 |

Kind argument 5, on these creatures, requests 40, 50, 60, 75, and 100. Kind 2, with a new Luther's attacker or target byte of 1, multiplies the amount by the scale when the creature is the attacker and divides by the scale when the creature is the target. StSquid's 8 and a zero loot dword take neither the attack-path grant nor a nonzero identity. WORM's 552 is the dword `0x77F7C` receives when the shifted roll is below 50.

## Still open

Which preset dword's high byte is 5, so which caller actually builds the times-5 hit on a creature. The body of `0x88908`. Whether bound `0x1FDF` stays inside Q03's 0-through-bound rule. The event number on the `0xA2A38` branch. No mode-1 or mode-5 caller of `0xD0BEC`.
