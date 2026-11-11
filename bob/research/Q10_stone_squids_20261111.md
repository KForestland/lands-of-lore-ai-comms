# Q10 Stone squids: are they meant to be fought?

complete true

formula_finished false

The book says to kill the stone monsters, and to click the corpse. It calls them immobile. Actors 61 and 68 are two of the sixteen placed StSquid. Every one of those sixteen has behavior 6 and flags `0x4482`. Behavior 6 is the Wander handler. It does not store the player as the target. The handlers that do that are behavior 4 and behavior 5, and no StSquid placement uses them. No host. No piece.

Pinned LOLG.DAT sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`, size 1977007. A code address A is file A+`0x37000`. Capstone, from the spawn at `0xA2283`, from `0xAE990`, and from the behavior table at `0xA2640`. L9_DR.MIX sha256 `700300d0cdf7df0af9471f3476c4e6ba473a603fa89e3a6e1855037d70be09c7`, size 23611578. Population file `scripts/lol2/act2_populations/L9_DR.json` in the of9 tree, same mix hash. GLOBAL.MIX sha256 `1e3e2a46340d714aaf4d583e5aff7e58dc11005bac6c694fac49c07d13e01edd`. The reach compare is Q06 and is not re-opened.

## Book

HINTBOOK.

Line 1149: find gorgonite nodules by clicking on the corpse of a stone monster in the Dracoid Ruins.

Lines 3563–3572: exterminate the stone monsters along with the Saar. They have stone blocks for lower bodies, and fangs and tentacles above. The book calls them immobile, and says they are dangerous with missiles and in hand-to-hand. Fight them up close, and do not fight a Saar while one is nearby.

Lines 3631–3635: enter the ruins through the pit in the Savage Jungle. The opening clear is two or three Saar and two or three stone monsters.

Line 3676: the first westward dead end houses a stone monster.

The book does not print actor numbers, the string StSquid, or a health figure. Killing is the instruction. Clicking is on the corpse. Passing them is not the instruction for the opening.

## The sixteen placements

PROVEN as file rows. Definition 0 is the only StSquid record, archive offset 23602319, name bytes `StSquid`. All 16 placements are definition 0, behavior byte 6, flags 17538 (`0x4482`), present, health word 800. The population `present` bit is the same `0x1000` test as Q07, and that bit is clear on all sixteen.

| Actor | Position | Behavior | Flags |
| ---: | --- | ---: | --- |
| 61 | (156, −3, −398) | 6 | `0x4482` |
| 68 | (102, −2, 403) | 6 | `0x4482` |

The other fourteen are actors 57–60, 62–67 and 69–72, same byte and the same flag word. Actors 61 and 68 are about 800 units apart in z. Nothing in this pass ties those two coordinates to the pit mouth. The book’s “two or three” is not an actor id.

A placed SSAR that is present and behavior 6 has flags `0x6582`, which is this word plus bits `0x100` and `0x2000`. The reader of those two bits was not found, the same open point Q07 left for `0x2000`. They are not cited here as a chase switch.

## What behavior 6 does

PROVEN for the dispatch. The spawn reads 0x38 placement bytes at `0xA2283`. `0xA23C0` stores placement byte `0x25` at actor `+0xA8`. `0xA23D7` compares it with `0x10` and stores 6 only when it is not below. Six stays. `0xA2438` copies it to `+0xA9`. `0xA239F` stores 0 at `+0x38`. `0xA23AD` stores 0 at `+0x34`.

`0xAE9D8` zero-extends placement word `+8` into actor `+0x14`. For these rows that word is `0x4482`. `0xA240B` zeros the dword at `+0xB4`. `0xA243E` sets bit 0 of `+0xB8` only. Bits `0x30` of `+0xB8` stay clear.

`0xA267C` takes `+0xA8`. A value of 14 or below jumps to `0xA3DC2`, `jmp dword ptr [esi*4 + disp]`. The displacement is fixed up, object 2, target offset `0x4961C`, so the table is `0xA2640`. Slot 6 is `0xA3BB6`. Slot 4 is `0xA3688`. Slot 5 is `0xA3681`.

`0xA3681` and `0xA3688` store `0x22574` at `+0x38` when that dword is 0. That is the player object used everywhere else in these notes. Those are the Get-player and Destroy slots of `global\ai\globalai.csv`. No StSquid row selects them.

The Wander slot is the whole body at `0xA3BB6`: push 3, push 0, push the actor, call `0xA9720`, return. It does not write `+0x38`.

Inside `0xA9720`, the second argument 0 is neither 1 nor 2, so `0xA97F0` sets a local 1 and does not read a target. The third argument is 3, so `0xA97F8` joins `0xA981C`. With `+0xB8` bits `0x30` clear, `0xA983B` calls `0x6EE80` with a null point and mode 3. `0x6EE80` can return at `0x6EF67` without a position store when that mode is 3 and `0xB3B8C` returns 0. The rest of `0x6EE80` was not walked. A later wander step is not ruled out. A chase of the player is not this handler.

The goal selector `0x59DAC` writes `+0xA9` only when byte `+0xB5` has bit 0 clear and bit 2 set (hive goal-choice note). The spawn tail from `0xA22BE` through `0xA246A` does not store `+0xB5`. Whether the fresh allocation is zero, and whether a later tick sets bit 2, was not read. The placed goal stays 6 until that store happens.

`global\ai\StSquid\goals.csv` has two nonzero weight rows. Stat row 19, Motion, is +5 on Destroy and −5 on Recover. Stat row 26 is +5 on Destroy and −8 on Recover. The other goal cells are empty. That table was not scored on a live stat bank. `stat.csv` leaves Motion empty. The selector was not run.

## Sense, reach, corpse

The definition words, same record as Q06’s reach word. File-to-runtime copy stays LIKELY.

| Word | Value | Reader, already posted |
| --- | ---: | --- |
| `+0x59` / `+0x5B` | 0 / 100 | First channel, sum 100 |
| `+0x55` / `+0x57` | 750 / 500 | Second channel, sum 1250 |
| `+0x61` | 50 | Blow bit, Q06 |
| `+0x63` | 800 | Cap, R02 |

They can be in melee range. That is not a chase. The book’s missile is not this reach word. A projectile writer was not entered. The corpse click in line 1149 was not matched to a handler.

## One longplay minute

Frames are `longplay_frames_act2plus/g_NNNNN.jpg`. g_N is 6580+(N−1)*30 seconds.

LONGPLAY. g_00092 at 2:35:10 is a dark round stone shaft, hand cursor, sword selected, both bars full. g_00093 at 2:35:40 is a cracked stone floor, fire on the ground, a dark figure in front of the player, sword still selected, health no longer full. g_00095 at 2:36:40 is the cracked bridge, and the creature on it has wings and a long arm. That last shape matches the book’s Saar, not the block-bodied stone monster. The minute between the shaft and that bridge is a fight. The frame does not print a name, and these pixels were not matched to the StSquid texture. The book’s opening order is the pit, then the stone monsters and the Saar, then the bridge.

## The port

Read, not edited. `L9_DR.json` gives StSquid a walk clip on selector 0, the same selector as idle, and stages the attack on selector 3. The BG27 note anchored actor 58 and left actors 61 and 68 hunting. That hunt is the port. The placed native byte is Wander, and Wander does not store the player.

## Still open

Whether `+0xB5` bit 2 is set after spawn, so `0x59DAC` can leave Wander. The rest of `0x6EE80` after `0x6EF68`. What reads flag bits `0x100` and `0x2000`. The corpse-click handler. Which of the sixteen stand at the pit mouth.
