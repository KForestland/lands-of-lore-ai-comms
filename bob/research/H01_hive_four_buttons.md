# H01 Hive four buttons

Owner F10 2026-11-03 17:43:48, Hive native (-3509, 7128), region 753. Beat 70. Read from `L5_HC.MIX` sha256 prefix `a1979e60d401ae30` and the matching command bodies in `L5_HC.json`. Opcode 16, opcode 196, opcode 20, and predicate kind 5 were not entered.

No new owner F10 after `TRIAGE_20261103.md` (newest report dir 2026-11-03T18:17:06Z).

## What the player does

Three locks stand on the north edge of region 753. There is no fourth lock. The "four buttons" are four presses.

| Control | Static name | File of name | Native x, y | Height | Slot byte 32 |
| --- | --- | --- | --- | --- | --- |
| 116 | Lock L1 | 6024451 | -3471, 7167 | -981 | 33 |
| 115 | Lock L2 | 6024481 | -3454, 7148 | -951 | 34 |
| 114 | Lock L3 | 6024511 | -3437, 7131 | -981 | 35 |

All three are flags 0x0402, region 753. L2 sits 30 above the other two. L1 is west of L3. The room polygon of region 753 reaches them along its north edge, so a player standing in the room faces L1 on the left, L3 on the right, and L2 on top.

Press order from the kind-3 groups, starting at state 0: Lock L1, Lock L1, Lock L3, Lock L2.

- L1 state 0 (predicate `0005000000`, groups 6676 and 6760, file 5899007): opcode 16 sets L1 to 1 (`101074000100`).
- L1 state 1 (predicate `0005000001`, groups 6698 and 6782): opcode 16 sets L3 to 1 and L1 to 2.
- L3 state 1 (predicate `0005000001`, groups 6436 and 6498, file 5898767): opcode 16 sets L2 to 1, L1 to 0, and L3 to 0.
- L2 then runs groups 6560 (value 0) and 6632 (value 1) only when predicate 25 passes.

A press in the wrong state runs a reset group (6408, 6470, 6532, 6604, 6726, 6810) that writes the other locks back to 0. Opcode 16's target index also fits a prop with the same number. The placed rows at 114, 115, and 116 are these locks.

## What happens

Predicate 25, file 5982744, bytes `0603080500`. Under the G76 layout this is operator 6 (both sides nonzero), left kind 3 index 8, right kind 5, last byte 0. Left index 8 is local slot 8. Right kind 5 was not entered.

When that predicate passes, groups 6560 (file 5898891) and 6632 (file 5898963) each do four commands:

1. Opcode 20 on the lock that was pressed.
2. Opcode 198 `c60000001000`: local slot 16 set to 0.
3. Opcode 196 `c490f8021cfc001400000000` on region 760.
4. Opcode 20 `14034f00bd0280000a14` on prop 79 (the `bd02` word is 0x2bd). Prop 79 is at (-3772, 7106), height -873, region 973, template 13, and has no events.

Region 760 is the small quad (-3654..-3572, 6975..7027) on the southwest corner of the lock room. Its 44-byte record at file 5865379 has floor word -1011 and ceiling word -639 (`0dfc81fd`), the same floor as region 753. The opcode 196 signed word is -996 and byte 7 is 20. The Hive chasm pack's floor formula (absolute target minus the word at record +20, byte 7 as the speed) gives a rise of 15, from -1011 to -996. No region in this level is stored at floor -996. Neighbors 754, 759, and 761 stay at -1011. Region 752, beside the locks, is already at floor -981, which this command does not reach. The callee was not entered, so the motion is that formula applied to these bytes.

## Local 8

Local names are 41-byte cstrings. Slot 0 is file 5981266. Slot 8 at file 5981594 is `Rampraise_Check`. Slot 16 at file 5981922 is `Spout_2`.

L5_HC.MIX contains zero copies of opcode bytes `c6/c7/c8/c9/cc/ce/cf` followed by `00000008`. Nothing in this level writes local 8 through those framed stores. Predicate 16 `0003080000` (equality, left kind 3 index 8) is cited by no event. The 33 bytes before slot 0 are mostly zero with one `01` and were not bound to an initial value.

If slot 8 starts at 0 and nothing else writes it, predicate 25 never passes and groups 6560 and 6632 never run. That initial value is still open.

## Spout_2

The success groups write slot 16 to 0. The other writer is group 3700 (file 5896031), from prop 293 kind 6 value 20 when predicate `0005000002` passes. Prop 293 is at (138, 6535), height -275, region 874, template 1, far from the locks. Group 3700 writes slot 16 to 5 (`c60000001005`), opcode 204 on regions 879-884, and opcode 196 on region 884 with signed word -240 (that region's stored floor is -275). No book line names Spout_2. What the player sees for that name is still open. The lock-room success command that matches Brady's ramp is the region 760 floor write, not the Spout_2 store.

## Glyph clue

Controls 117-120 have no events. Flags 0x0002, region 283, height -205. Region 283 floor is -235 and ceiling is -107, on the upper cave (y 7696). West to east:

| Control | x | Static name | Name file | Slot |
| --- | --- | --- | --- | --- |
| 120 | -1886 | Glyph L1 | 6024361 | 30 |
| 119 | -1877 | Glyph L1 | 6024361 | 30 |
| 118 | -1868 | Glyph L3 | 6024421 | 32 |
| 117 | -1859 | Glyph L2 | 6024391 | 31 |

That row is L1, L1, L3, L2, the same press order as the lock groups. Two controls share slot 30, so the second L1 is a second mark, not a fourth lock.

## Books

BRADY printed page 170 (file lines 7254-7271): the only Hive level the player must reach is the bottom one. Level Six is listed with the other gear. "Click on the three buttons—left twice, right once, then top once—to raise the ramp" to three cat carvings. Moving those blocks opens the Deathstroke Shield and the Longbow Shift.

BRADY printed page 80 (file lines 3188-3204) says the same thing without the press order: three stone squares around a cat carving, a certain order, a ramp, then the shield and the bow.

HINTBOOK lines 2703-2704, after the rune copies and Dawn: "You have done all that you need to do here." The shield and the bow are the tourist items at lines 2747-2749. The hintbook has no four-press sentence. The ordered presses are Brady's.

## Required or optional

OPTIONAL for finishing the game. The required Hive stop is the bottom rune copy, the flute, two wax impressions, and Dawn (HINTBOOK 2659-2704, BRADY 7254-7308). The buttons open loot.

## Frame

Longplay frames are `f_#####.jpg`, frame n = (n-1)*5 s. No caption index is in that directory. No frame was opened. The glyph row is the static names above. Which frame shows them is still open.

## Still open

- Initial value of `Rampraise_Check`, and any writer outside the framed local stores.
- Predicate 25's right kind 5. Until that is entered, the success groups can be blocked even after L1, L1, L3, L2.
- Opcode 196 was not entered. The +15 rise is the chasm pack's formula on these bytes. Whether that 15-unit bump is the whole Brady ramp, and which controls are the three cat blocks, the shield, and the bow, is still open.
- What Spout_2 changes in play.
- A longplay frame of glyphs 117-120.

Grades: lock placements, names, group bytes, region 760 floor, and the L1-L1-L3-L2 press chain are DECODED. Left / right / top and the loot are BRADY. "Done here" after the runes is HINTBOOK. The frame is open.
