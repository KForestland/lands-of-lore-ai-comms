# P05 LoL1 chunk 6: Timothy, Baccata, and Lora

No Godot was run. The tree is `~/lol1_godot` at `9987d7e`, clean. L06 chunk 6 is the party joins for cards LOL1-04 through LOL1-06. Timothy joins, then Baccata joins and Timothy leaves, then Lora joins and stays with the Draracle. Paulson waits until the mine chunk. The crash guard is in this chunk so that later meeting can add him.

## Data

M05 templates: Timothy is id 2, hit points 27, magic 5, skills 3 2 1, starting types 93, 131, 153, and 162. Baccata is id 3, hit points 22, magic 18, skills 1 1 3, starting types 108, 149, 145, 153, and 129. Lora is id 4, hit points 48, magic 5, skills 1 4 1, starting types 137 and 162. Paulson is id 6. The three skill numbers were not given names.

`add_character` returns false when `count()` is already 3. `count()` counts every record whose `flags` bit 0 is set. On a match it copies `charDefaults`, sets `defaultModifiers` from the nine-table list, sets `face_bank` to `face%02d` of the absolute id, rolls `nextAnimUpdateCountdown` as 1 through 12 plus 6, and calls `make_item` for each nonzero starting type. It does not run item script 0x80. ScummVM does run that script on each starting item. L06 names the workaround and does not name 0x80. The script stays unported.

ScummVM `countActiveCharacters` counts a leading run of flag bit 0 and stops at the first clear bit. The workaround looks at slot index 2, so the test party is three leading active records and both counters agree.

`addCharacter` in `lol.cpp`: when the active count is at least 3, and `_characters[2].id` is 4, and the new id is 6, and the level is 16, and the block is 0x225, each of her 11 items that is nonzero is placed with `placeMoveLevelItem` on that level and block at offsets 0, 0 and flying 0. `_displayLoraPaulsonWorkaroundMsg` is set. The count is then treated as 2, and the new character is written over slot 2. Any other full party returns false. The message string was not read. The port's `place_move(id, level, block, xo, yo, flying)` is the call to use. The port's array appends. This path replaces index 2 and does not append a fourth record.

N04 found no `addRemoveCharacter` for id 2. The inn block and the join call were not read. L03 names Lora's pod, the riddle scroll, and the stay with the Draracle. The two path orders past the walkthrough's lever list were not read. The key item names on that card are the sledgehammer, the emerald eye, the sapphire eye, the red key, and the bezel ring. Their types and blocks were not read. A call is ported when `missing` names it, or when a found `addRemoveCharacter` names the id. A block this spec does not have is not invented.

## Behaviour

The walkthrough order is the join order. Timothy joins at the Grey Eagle. At the poisoning, Timothy's flag bit 0 is cleared and Baccata joins. In the caves, Lora joins, and at the Draracle her flag bit 0 is cleared. The riddle scroll is carried when the script call that creates it has been read. Until that call is read, the stay does not require an item type.

`add_character` gains the exception above. The Urbish meeting that passes id 6 is chunk 7. Calling the function with those arguments is how this chunk proves the guard. A full party that is not Lora in index 2, or that is not level 16 block 0x225, still returns false. Item script 0x80 is not run.

## Tests

1. From one hero, `add_character(2)` adds Timothy. `count()` is 2. His starting types are 93, 131, 153, and 162. His hit points are 27 and his magic is 5.
2. After the poisoning leave, Timothy's flag bit 0 is clear. `add_character(3)` adds Baccata. `count()` is 2. His starting types are 108, 149, 145, 153, and 129.
3. `add_character(4)` adds Lora. After the Draracle stay, her flag bit 0 is clear and `count()` no longer includes her. No riddle-scroll type is required until the create call is read.
4. Three active records, index 2 id 4, level 16, block 0x225, `add_character(6)` returns true. Index 2 is Paulson. Lora's nonzero items sit on block 0x225 with flying 0. `count()` is 3. The workaround message flag is set. The same call at block 0x226 returns false and leaves Lora in index 2. The same call with Lora in index 1 returns false.
5. None of these joins run item script 0x80.
