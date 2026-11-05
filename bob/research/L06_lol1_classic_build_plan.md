# L06 LoL1 Classic build plan

No Godot was run. The tree is `~/lol1_godot` at `9987d7e`. View, doors, EMC level scripts, text, items, the inventory bar, one hero, and monster walking already run. Later chunks add calls. They do not replace those systems. Sizes are GUESS, in lane-days, not measured. The owner's three weeks is the budget named in the task list. The guesses below add to about five weeks if every later level needs new calls. They shrink if `level_scripts.gd` already covers that level. Its `missing` counter is how a chunk learns which calls to add.

Classic is this tree. An Enhanced pass comes after, and it does not reopen a chunk to change a bug fix. Both editions get the same fix. Cut content in the March patch plan (the shuriken, Jana's scene) is not a chunk.

## Chunks

1. Save and load. Write the flag bytes, script words, money, lamp oil, block, facing, the one hero, the item chains, and the live monsters. Read them back. Two days. No new scene.

2. Hero select. The four templates in `party.gd` (Ak'shel, Michael, Kieran, Conrad), one of them starts, and the save keeps the choice. Two days. The selection screen is the missing piece. The portraits already draw.

3. Combat on the grid that already walks. Monster attack modes, a party attack, damage, and death. Six days. Numbers come from the original tables. LoL2 combat is not a source. The large-fireball width stays the original accidental 63, from ScummVM `items_lol.cpp`. A White Tower sound id of 255 stays silent.

4. TIM for the opening and the throne room, cards LOL1-01, LOL1-02, and LOL1-05. Four days. The RE repo has the TIM notes. This tree does not run them. No other cutscene in this chunk.

5. Play cards LOL1-02 through LOL1-05 (keep, thugs, Roland, the poisoning). Four days. Port only the EMC calls those levels report as missing, including the atlas item and the compass if those calls are in the missing list. Do not add a second atlas later.

6. Party joins for cards LOL1-04 through LOL1-06. Timothy, then Baccata, then Lora, then Lora stays with the Draracle. Four days. `addCharacter` must include the ScummVM workaround: a full party that still has Lora does not crash when Paulson is met. Paulson himself waits until the mine chunk.

7. Cards LOL1-07 through LOL1-11, as far as the walkthrough is written: the lake, Opinwood, the swamp, Dawn's key, and Urbish through the burned nests. Five days. Same missing-call rule. The White Tower stair bug (level 21, destination block 0x3E0) is fixed in this chunk when that level is first played, not in a later pass.

8. Cards LOL1-12 and LOL1-13 are not buildable from the current walkthrough. It stops in the mine and only names the tower and Cimmeria. The reference's Whole Truth sentence is not a step list. This chunk starts when a second step source is read. No size until then.

9. Sound. The 215 VOC files and the 67 music files are already extracted. Two days, after the levels that call them. `playSoundEffect` is already a quiet no-op, so this fills that call. It does not move earlier chunks.

The string typos (Duble ring, Nathanial's Key) are a display fix inside chunk 5, when those names first show. They are not their own chunk. Floppy-only Dawn's Key is outside this plan: the importer reads the CD data, and the March plan says that bug is already gone there.
