# Q06 How often a creature strikes, and from how far

complete true

formula_finished false

LAMPLT reach is 0. StSquid reach is 50. Both are the signed definition word at `+0x61`, compared as a 16.16 length against the octagonal distance in placement x/z. A strike frame costs 1024 animation units, which is `79520/1193182` seconds (0.066645 s) on the standard PIT. While the attack selector stays selected, the kind-1 blows are one clip apart: LAMPLT selector 8 is 1.266 s, selector 9 is 1.200 s, and StSquid selector 2 is 0.933 s. The port uses reach 50 and an 8 fps clip plus a 0.8 s recovery, so it does not agree. No host. No piece.

Pinned LOLG.DAT sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`, size 1977007. A code address A is file A+`0x37000`. Capstone, from the entries named below. L8_SJ.MIX sha256 `3eff07430a453d2c6f09133f869874e0530af1b6a3bfff7f4297761b96a28bc2`, size 13831538. L9_DR.MIX sha256 `700300d0cdf7df0af9471f3476c4e6ba473a603fa89e3a6e1855037d70be09c7`, size 23611578.

## Reach

PROVEN. The in-range bit is actor byte `+0xB7` bit 0, set at `0xA4ED7` (`or byte [ebx+0xB7], 1`) and cleared at `0xA4EE0`.

`0xA4E68` loads the runtime definition from `[ebx+0x2C]`. `0xA4E6B` (file `0xDBE6B`) loads the word at definition `+0x61`. `0xA4E6F` sign-extends it. `0xA4E72` shifts it left 16. `0xA4E7B` compares the distance return with that threshold. Greater jumps to the clear at `0xA4EE0`. No radius is added.

The distance is `0x1365C4`: octagonal `max(|dx|,|dz|) + min/2` of actor `+0`/`+4` against the target's `+0`/`+4`. Height is not an argument.

The 16.16 unit is `0xAE990` (entry `push ebx`). Placement dword 0 is int16 x, int16 z. `0xAE99F` sign-extends the low word, `0xAE9B6` shifts it left 16, and `0xAE9C3` stores it at `[ebx]`. `0xAE9A2` takes the high word, `0xAE9C0` shifts it, and `0xAE9C8` stores it at `[ebx+4]`. Those are placement x and z. The definition word is therefore the integer reach in those units. A zero word sets the bit only when that distance is 0.

File words, re-read from the MIX:

| Record | Archive offset | Word `+0x61` | Word `+0x63` |
| --- | ---: | ---: | ---: |
| L8 LAMPLT def 9 | 13809498 | 0 | 200 |
| L8 LAMPLT def 10 | 13809645 | 0 | 200 |
| L8 LAMPLT def 11 | 13809792 | 0 | 200 |
| L9 StSquid def 0 | 23602319 | 50 | 800 |

`[actor+0x2C]` is that runtime definition: `0xA22DB` stores index times `0x8B` plus `[0x22D50]`. The word sits inside the 0x87-byte copy. The copy helper `0x118820` was not entered, so the file-to-runtime link stays LIKELY. The compare itself is PROVEN.

Two other gates can clear the bit before the compare matters. `0xA4E54` requires bit 1 or bit 2 of byte `+0x9E`. `0xA4E8B` calls `0xB25CC`, and a nonzero return also clears the bit. Those two were not interpreted. Q01 already pointed at this bit. It was not rewritten.

## What the 1024 is

PROVEN. The animation clock is the block at `0xA55AE` (`xor esi, esi`), reached on the same actor.

- `0xA55B9` skips the block when byte `+0xB5` bit 1 is set.
- `0xA55C1` addresses the countdown word at `+0x7C`. `0xA55C4` loads the global delta word `[0x22C58]`. `0xA55D1` subtracts it.
- `0xA55DC` sign-tests that word through the dword at `+0x7A`. A non-negative countdown leaves.
- `0xA55F0` reads the selector byte at `+0x30`. `0xA55F6` reads the definition. `0xA55FC` loads definition `+0x14`, the state table. `0xA55FF` loads state dword `+4` of that selector. `0xA5606` shifts it right 8 and `0xA560C` adds it to the countdown.

Attack selectors carry dword `0x00040000`, so the add is 1024. Re-read from the metadata state records (L8 key 1161068061, L9 key 3510921278):

| Clip | State in the metadata | Dword `+4` | After `>> 8` | Kind-1 event |
| --- | ---: | ---: | ---: | --- |
| LAMPLT defs 9, 10, 11 selector 8 | `0xB661`, `0xB7E1`, `0xB961` | `0x40000` | 1024 | frame 7, value 100 |
| LAMPLT selector 9 | next state | `0x40000` | 1024 | frame 7, value 70 |
| StSquid selector 2 | `0xEBC2` | `0x40000` | 1024 | frame 5, value 100 |
| StSquid selector 3 | `0xEBD2` | `0xC0000` | 3072 | none (kind 3, frame 4, value 82) |

Action-row byte 0 is 5 on LAMPLT selectors 8 and 9 and on StSquid selector 2. That is the strike row. StSquid selector 3 is action 6.

`0xA5723` jumps back to the sign test when the frame-event call returns 0, so one delta can advance more than one frame. Landing on the last frame can force a negative countdown back to 0 (`0xA56C7`). A delta smaller than 1024 does not take that clear.

## Seconds

PROVEN for the unit. The delta word is controller `0x227A4` field `+0x4B4`, which is `[0x22C58]`.

`0x5909A` pushes `0x227A4` and `0x590A5` calls `0xE0058`. That constructor's ebx walks to `0x227A4+0x4A0` (`0x22C44`). `0xE00D0` pushes key `0x1E0` (480) and `0xE00E8` calls `0x14F9BC`, which registers the key through `0x15CD06`. The following timer is key `0x3C` (60).

`0x167BE0` divides `0x1234DC` by the key and `0x167BE4` passes the quotient to `0x168157`, which stores it at `[0x1C62C]` and calls `0x17875A`. `0x17877B` writes mode `0x36` to port `0x43` and the divisor's low and high bytes to port `0x40`. `0x1234DC / 480` is 2485. Between keys 480 and 60, 480 is the faster one and wins the PIT. A key registered elsewhere that needs a still smaller divisor would replace it. Those two are the keys this constructor registers.

On a standard PIT input of 1193182 Hz, divisor 2485 interrupts at `1193182/2485` Hz. The key-480 slot increment is one tick per interrupt at that divisor (`(480 << 16) / 480`).

The per-call smoother, on the same controller ebx, is `0xE0BE4` (elapsed from `0x14FA79` on the key-480 timer) through `0xE0C82`:

- Each of four samples is clamped to 480 (`0xE0C11`, immediate `0x1E0`).
- Their sum is at `[ebx+0x4BA]`. `0xE0C43` through `0xE0C56` multiplies that sum by 2048. `0xE0C62` clamps the product to `0x80000` (524288), which is a sum of 256.
- `0xE0C79` adds the fraction at `[ebx+0x529]` and `0xE0C7F` shifts right 8. `0xE0C82` stores the word at `[ebx+0x4B4]`.

Below the clamp, one call's delta is 8 times the sum of the last four tick samples. Each tick then sits in four calls, so the stream is 32 key-480 ticks per second. One 1024-unit frame is

`1024 * 2485 / (32 * 1193182) = 79520/1193182` seconds, which is 0.066645 s, or 15.005 frames per second.

The code's own dividend is `0x1234DC` (1193180), two counts below the standard PIT constant. That is about two parts in a million. The seconds above use 1193182.

The setter `0xA7DC4` stores 0 at the countdown (`0xA7DE9`) and stores `F1F94(definition, selector) - 1` at byte `+0x32` (`0xA7DF4`, `0xA7DF9`). `0xF1F94` returns a table byte. Definition byte `+0x32` is 1 on all four records, so bit 3 is clear and the return is the third arm (`0xF2051`, byte `[0x22D78 + index*12 + 8]`). That live byte was not read. The decoded texture groups in `act2_creatures/L8_SJ/sprites.json` and `L9_DR/sprites.json` are 19 frames (LAMPLT selector 8), 18 frames (selector 9) and 14 frames (StSquid selector 2). The same helper matched the texture count on WORM. Matching it again here is LIKELY, not re-executed.

While selector `+0x30` stays on that clip, the clock wraps to frame 0 by itself (`0xA5638` calls `0xF2814` with frame 0 once the frame index has reached `+0x32`). Kind 1 then repeats once per loop:

| Clip | Frames | Seconds between kind-1 events |
| --- | ---: | --- |
| LAMPLT selector 8 | 19 | 1.266 s (`19 * 79520/1193182`) |
| LAMPLT selector 9 | 18 | 1.200 s |
| StSquid selector 2 | 14 | 0.933 s |

The blow is not on frame 0. LAMPLT kind 1 is frame 7 (value 100 on selector 8, value 70 on selector 9). StSquid kind 1 is frame 5, value 100. Those value bytes are the percent the attack path scales, already in the frame-event note. They are not a second clock.

Arriving on the last frame calls `[vtable+0xB8]` with argument 3 (`0xA56A3`). That virtual was not entered. If it changes selector `+0x30`, the next gap is whatever clip it selects. The clock itself does not insert a recovery.

## The port

Read, not edited. `scripted_creature_state.gd` uses `FPS` 8, `REACH` 50 and `ALERT_RANGE` 600 for every definition that has an attack row, and 0 when it has none. Clip seconds are `frames/8`. `creature_live_rules.gd` `RECOVERY` is 0.8 s, stored as `live.cooldown` when the clip ends, and a cooldown blocks the next attack. `scripted_creature_population.gd:190` calls `State.advance_live`.

| | Native | Port |
| --- | --- | --- |
| LAMPLT reach | word `+0x61` = 0 | 50 |
| StSquid reach | word `+0x61` = 50 | 50, not read from the word |
| LAMPLT selector 8 | 1.266 s loop, hit on frame 7 | 19/8 = 2.375 s clip, hit at 0.875 s, then 0.8 s |
| LAMPLT selector 9 | 1.200 s loop, hit on frame 7 | 18/8 = 2.250 s, then 0.8 s |
| StSquid strike | selector 2, 0.933 s, hit on frame 5 | staged selector 3, 14 frames, hit frame 4 |

The staged StSquid attack in `act2_populations/L9_DR.json` is selector 3. That state is action 6, interval 3072, kind 3 frame 4. It is not the kind-1 row. Time between port impacts, if the creature stays in reach, is the clip plus 0.8 s: 3.175 s, 3.050 s, and 2.550 s for those three staged clips.

## Behaviour 14

Read from the same population files. Of 66 LAMPLT actors (definitions 9, 10 and 11), 52 have placement byte 37 equal to 14 and 14 have 6. All 16 StSquid actors have 6. The constructor keeps a behaviour below `0x10` (`0xA23D1` compares with `0x10` and stores 6 otherwise), so 14 stays. The reach compare and the frame clock do not read actor `+0xA8`. The writer of the stack byte copied to `+0xA8` at `0xA23C0` was not found.

## Sites that are not the interval

The frame stepper at `0xA3CD0` advances `+0xA5` only after the waypoint test at `0xA3C15`. That is locomotion. The 4-byte rows it reads are not the definition action rows. State dword `+4` is the refill above, not a separate 1024-tick pause. Kind-1's frame number is where the blow sits inside the clip, not the seconds between clips.
