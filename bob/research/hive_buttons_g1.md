# G1 Hive four buttons

Acceptance for HIVE-4-BUTTONS-RESEARCH. Owner F10 2026-11-03 17:43:48, Hive native (-3509, 7128), region 753. Placements and group bytes are the ones in `H01_hive_four_buttons.md`. This pass rechecked `L5_HC.MIX` sha256 prefix `a1979e60d401ae30` (6,030,400 bytes) under `lol2_out/native_sky_look_up_20260923/game/DAT`. Opcode 16, opcode 196, opcode 20, and predicate kind 5 were not entered. No Godot.

Press order stays DECODED: Lock L1, Lock L1, Lock L3, Lock L2. Controls 116, 115, and 114. There is no fourth lock.

## (a) Who writes local 8

Slot 8 at file 5981594 is `Rampraise_Check`. That cstring is in `L5_HC.MIX` only. The same DAT directory's other MIX files do not contain it, and `LOLG.DAT` does not contain it. `L5_HC.MIX` has zero copies of opcode bytes `c6`, `c7`, `c8`, `c9`, `cc`, `ce`, or `cf` followed by `00000008`. Other MIX files do contain that byte shape aimed at index 8. Each of those is that file's own local 8. Nothing joins them to `Rampraise_Check`.

Predicate 25 is `0603080500`: operator 6, left kind 3 index 8, right kind 5. Right kind 5 was not entered. If slot 8 starts at 0 and nothing writes it, groups 6560 and 6632 never run. The 33 bytes before slot 0 were not bound to an initial value. The writer, including any loader init, stays open.

## (b) What opcode 196 on region 760 does

Region 760 is the quad (-3654..-3572, 6975..7027), floor word -1011, same floor as region 753. Groups 6560 and 6632 store opcode 196 `c490f8021cfc001400000000` on that region. The signed word is -996 and byte 7 is 20. The Hive chasm floor formula on those bytes is a rise of 15, from -1011 to -996. No region in this level is stored at floor -996. Neighbors 754, 759, and 761 stay at -1011. Region 752, beside the locks, is already at -981, and this command does not reach it.

The callee was not entered, so that rise is the formula on the bytes, not a proven ramp. Brady's sentence says the presses raise a ramp to three cat carvings, and moving the blocks opens the Deathstroke Shield and the Longbow Shift. Which controls are the blocks, the shield, and the bow stays open. What the rise unlocks past that sentence stays open.

## (c) What Spout_2 is

Slot 16 at file 5981922 is `Spout_2`. The success groups write it to 0 (`c60000001000`). The other writer is group 3700, from prop 293 kind 6 value 20. Prop 293 is at (138, 6535), height -275, region 874, far from the locks. Group 3700 writes slot 16 to 5, then opcode 204 on regions 879 through 884, and opcode 196 on region 884 with signed word -240. That region's stored floor is -275. Opcode 204 and that opcode 196 were not entered. No book line names Spout_2. What the player sees for that name stays open. The lock-room command that matches Brady's ramp is the region 760 floor write, not the Spout_2 store.

## (d) Glyphs 117-120

Controls 120, 119, 118, and 117 have no events. Region 283, height -205, on the upper cave at y 7696. West to east the static names are Glyph L1, Glyph L1, Glyph L3, Glyph L2. That is the same order as the lock presses. Two controls share slot 30, so the second L1 is a second mark.

`longplay_frames` has no caption index. Frame n is `(n-1)*5` seconds. The written time index `longplay_deep/jungle/REFERENCE.md` does not name these four controls. Frames opened this pass:

| Frame | Time | What it shows |
| --- | --- | --- |
| f_01100 | 91:35 | A dark cave mouth. No glyph row. |
| f_01120 | 93:15 | A tiled hall and a dark mass. No glyph row. |
| f_01130 | 94:05 | A limb on rocks. No glyph row. |
| f_01137 | 94:40 | Three square plates, left, right, and top, around a tall central carving. |
| f_01141 | 95:00 | Two carved doors, each with a small plate. |
| f_01145 | 95:20 | One tall carving and a block with a blue glow. |

None of those is a west-to-east row of four glyphs. f_01137 matches Brady's left / right / top arrangement. It is not pinned to controls 117-120, and the central carving was not read as a cat. The longplay frame of the glyph row stays open. The names above are what the records store.

## (e) Required or optional

OPTIONAL for finishing the game. HINTBOOK lines 2703-2704, after the rune copies and Dawn: "You have done all that you need to do here." The shield and the bow are the tourist items at lines 2747-2749. The hintbook has no four-press sentence. BRADY printed page 170 (file lines 7254-7271) says the only Hive level the player must reach is the bottom one, and lists Level Six with the other gear. The ordered presses and the loot are Brady's. The required Hive stop is the bottom rune copy, the flute, two wax impressions, and Dawn.

## Still open

- The initial value of `Rampraise_Check`, and any writer outside the framed local stores.
- Predicate 25's right kind 5. The success groups can stay blocked after L1, L1, L3, L2.
- Opcode 196 was not entered. The +15 rise is the chasm formula on these bytes. It is not proven to be the whole Brady ramp.
- Which controls are the three cat blocks, the shield, and the bow.
- What Spout_2 changes in play.
- A longplay frame of glyphs 117-120.

Grades: lock names, the press chain, region 760's stored floor, the glyph names, and the zero local-8 stores in `L5_HC.MIX` are DECODED. Left / right / top and the loot are BRADY. "Done here" after the runes is HINTBOOK. f_01137 is LONGPLAY of three plates, not of controls 117-120. The glyph frame is open.
