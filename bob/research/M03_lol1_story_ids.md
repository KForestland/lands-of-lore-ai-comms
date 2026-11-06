# M03 LoL1 story ids

No Godot was run. L03's cards were not rewritten. The walkthrough order stays the card order. The classic reference still puts the Draracle before the poisoning, and it still names the Whole Truth. Those two orders stay unmerged. Nothing past the Urbish stop is a written step.

Ids below were read from `~/lol1_godot` at `9987d7e` and from ScummVM `script_lol.cpp` / `lol.cpp`. Level English names are `lands.json` slots 529 through 557, one per level. Tileset areas are each `level.json` `area` field. Item types are ONETIME.INF property indexes, named through `olol_setItemProperty` (stack position 1 is the lands string, bit 0x4000 selects LANDS). Character ids are `static_tables.json` `charDefaults`. EMC calls come from a path scan of the generated LEVEL scripts. A call reached only by taking both sides of an unknown test is marked LIKELY. A destination outside levels 1 through 29 was dropped. TIM dialogue was not executed, so a join that lives only in a TIM file has no script id here.

## Shared ids

| id | name | grade |
| --- | --- | --- |
| -9 | Ak'shel | DECODED |
| -1 | Michael | DECODED |
| -8 | Kieran | DECODED |
| -5 | Conrad | DECODED |
| 2 | Timothy | DECODED |
| 3 | Baccata | DECODED |
| 4 | Lora | DECODED |
| 6 | Paulson | DECODED |
| 7 | Dawn | DECODED |

`party.gd` starts a game from the four negative ids only. `addCharacter` refuses a new member when three are already active. The one exception is in ScummVM, not in `party.gd`: if slot 2 is Lora (id 4) and the new id is Paulson (id 6) on level 16, block 0x225 (549), her eleven items are dropped and she is removed. Level 16's English name is Mines Level 4, area MINE1. That path is not a walkthrough step.

Face 0 is north and face 2 is south, from `tests/script_walk_test.gd`'s own sentences. Faces 1 and 3 were not named.

## LOL1-01

Grade DECODED for the four hero ids. Grade UNKNOWN for which specialty is which. No level file is the character select screen. `raceClassSex` is 0, 0, 2, and 4 on Michael, Conrad, Kieran, and Ak'shel. Those numbers were not given specialty names.

A new game is already inside level 1. The test says the first visit leaves the party on block 557 facing north. The function number of that square was not printed.

## LOL1-02

Grade DECODED for the level file and for two item types. Grade UNKNOWN for who hands the writ over.

| field | value |
| --- | --- |
| level file | LEVEL1, English name Gladstone Keep, area KEEP |
| dialogue | `level01.json` contains the substrings King Richard, Geron, Writ, and Magic Atlas |
| writ | item type 244, name Writ of Passage, shape 40 |
| library key | item type 185, name Library key, shape 29 |
| atlas | no ONETIME name contains "atlas" |
| gate | LEVEL1.INF function 621, entry mask 0x0041, `loadNewLevel(2, 106, 2)` |

The gate call is the test's sentence and the path scan agreed. LEVEL1.INI functions 0 and 1 call `makeItem` on type 75, Halberd. The test says the keep starts with four Halberds. This pass did not count the calls inside one function.

The north gate arrives on level 2, Northland Forest, area FOREST1, block 106, face 2. `walk.gd` says block 589 on level 1 is LEVEL2.INF's `loadNewLevel(1, 589, 0)`. A zero-return run of LEVEL2.INF function 74 produced those three arguments. The fork scan did not reach that function again.

## LOL1-03

Grade DECODED for two placements. The walkthrough's place and the level name do not name the same file, so they stay two rows.

The walkthrough puts the thugs in the Northland. That arrival is the level 2 gate above. `level02.json` contains the substring thug.

LEVEL5 is named Thug's Hideout and its area is CAVE1. LEVEL5.INI function 1, taint 0, calls `createLevelItem` for type 167, Thug's key, shape 58, and type 249, Lantern, shape 44. The walkthrough's lockpicks are not in that function. LEVEL6.INI function 1 creates type 245, Lockpicks. Level 6 is Caves Level 1, area CAVE1. The hideout sentence and the lockpick placement were not merged.

## LOL1-04

Grade DECODED for the two level files. Grade UNKNOWN for Timothy's join script and for a compass item type.

| file | English name | area | dialogue substrings |
| --- | --- | --- | --- |
| LEVEL3 | Southland Forest | FOREST1 | Timothy, Roland |
| LEVEL4 | Roland's Manor | MANOR | Roland, Timothy, compass |

No ONETIME name contains "compass". `game_state.gd` has `compass_broken`. Lands string 603 is "The compass appears to be broken." That string was not joined to an item type. No EMC `addRemoveCharacter` for id 2 was concrete. TIM was not executed.

## LOL1-05

Grade UNKNOWN for the poisoning script, Dawn's spell book, and Baccata's join. The return is still Gladstone, LEVEL1. `level01.json` also contains the substrings Scotia, Dawn, and Baccata. Those substrings are mentions in the file, not a placed NPC id. No concrete `addRemoveCharacter` for id 3 or id 7.

## LOL1-06

Grade DECODED for the cave names, one Lora call, the sledge, and one riddle-scroll give. The walkthrough's "after the poisoning" order and the reference's "before the poisoning" order stay unmerged.

| level | English name | area |
| --- | --- | --- |
| 6 | Caves Level 1 | CAVE1 |
| 7 | Caves Level 2 | CAVE1 |
| 8 | Caves Level 3 | CAVE1 |
| 9 | Caves Level 4 | CAVE1 |

`level07.json` contains Lora, Baccata, and Draracle. LEVEL7.INF function 66, mask 0x0040, calls `addRemoveCharacter(4)`. That call is LIKELY: it sits behind an unknown test. Id 4 is Lora. No concrete call removes her.

| item | type | where the scan saw it |
| --- | --- | --- |
| Sledge | 59, shape 56, might 15, type word 5 | LEVEL7.INI function 1, `createLevelItem`, taint 0 |
| Emerald Eye | 222, shape 49 | LEVEL6.INI function 1, `makeItem`, taint 0 |
| Sapphire Eye | 223, shape 48 | type exists; no placement call was concrete |
| Red key | 170, shape 61 | type exists; no placement call was concrete |
| Bezel ring | 225, shape 116, type word 1536 | type exists; no placement call was concrete |
| Freeze scroll | 234, shape 34 | LEVEL8.INF function 335, `createLevelItem`, block 368 |
| Riddle Scroll | 241, shape 34 | type stays 241; function 335 does not place it |

The item name is Sledge, not sledgehammer. Type word 5 is the weapon-slot value in the Vaelan comment in `olol_setItemProperty`. Empty flask, type 211, is created by LEVEL8.INI function 1, on blocks 117 and 469. Function 0 does not create it. The walkthrough says Dawn gives the flasks later. Those two sentences stay separate. The elixir-in-a-tower sentence has no script id here.

## LOL1-07

Grade DECODED for the dialogue file only. Level 10's English name is Opinwood, area FOREST1, and `level10.json` contains the substring Lake Dread. The lake sentence and the Opinwood name were not merged. Victor is a substring in `level02.json` and `level10.json`. No character id is named Victor.

## LOL1-08

Grade DECODED for the level name. Grade UNKNOWN for the skull's placement and for the wagon refusal.

Level 10 is Opinwood, the same file as LOL1-07. Green Skull is item type 266, shape 68, might 8, type word 5. No concrete placement call named it. `level10.json` contains the substring wagon. Lands has no brass-helmet item name.

## LOL1-09

Grade DECODED for the level file. Grade UNKNOWN for the ruby hand-off.

Level 11 is Gorkha Swamp, area SWAMP. `level11.json` contains Gorkha and Ruby. Ruby of Truth is item type 220, shape 105, type word 64. No concrete placement or `giveItem` named it. Freeze is spell row 2 in M04. No EMC function was tied to the pits.

## LOL1-10

Grade UNKNOWN for Dawn's give. `level10.json` contains Dawn and the wagon substring, on the Opinwood file from LOL1-08. Empty flask is type 211, and the only concrete creates were the cave ones in LOL1-06. Lands string 419 is "Magic Pyramid", and no item type uses that string. Item type 198 is named Dawn's Key, shape 41. L05 says the CD import does not include Dawn's Key. The ONETIME scan found type 198 anyway. Those two sentences stay unmerged. Neither id was given by a concrete EMC call.

## LOL1-11

Grade DECODED for the mine file names, as far as the walkthrough is written. The text stops in the mine. Later mine facts are not steps.

| level | English name | area |
| --- | --- | --- |
| 12 | Urbish Mining Co. | URBISH |
| 13 | Mines Level 1 | MINE1 |
| 14 | Mines Level 2 | MINE1 |
| 15 | Mines Level 3 | MINE1 |

`level12.json` contains Urbish. Silver key is item type 173, shape 62. No concrete placement named it. Fireball is spell row 3. No nest function was read. Paulson's template is id 6. The only engine path that names him is the level 16 workaround above, and the walkthrough never says he joins. `level27.json` also contains the substring Paulson. Level 27 is Castle Level 1. That mention is not a mine step.

## LOL1-12

Acceptance is not written. This is not a build step. Levels 18 through 21 are named Tower Level 1, Tower Sub-level, Tower Level 2, and Tower Level 3, area TOWER1. `level18.json` contains Jana. No Jana character id exists in `charDefaults`.

## LOL1-13

Acceptance is not written. This is not a build step. Levels 27 through 29 are Castle Level 1 through 3, area CIMMERIA. `level29.json` contains Scotia, Ruby, Shard, and Nether Mask. Shard of truth is item type 281, shape 57, type word 1536. The Whole Truth is item type 280, shape 73. No concrete EMC call gives either of them. The walkthrough never names them. The reference does. Those endings stay unmerged.

## LOL1-14

No player step. Reference only.

| level | English name | area | dialogue substring that was present |
| --- | --- | --- | --- |
| 17 | Upper Opinwood | FOREST1 | none of the card's names |
| 22 | City of Yvel | YVEL1 | Lora, among many other names |
| 23 | Catwalk Caves 1 | CATWALK | Frendor, Mylek |
| 24 | Yvel Woods | FOREST1 | White Tower, Cimmeria |
| 25 | Catwalk Caves 2 | CATWALK | none of the card's names |

Level 24's name is Yvel Woods, its area is FOREST1, and its dialogue contains White Tower. Those three were not merged. LEVEL24.INI function 1 calls `makeItem` on type 264, Vaelan's Cube. A second row, type 263, has the same display name. The floppy workaround in `olol_setItemProperty` forces type word 5 to 0 on index 264. The CD scan already stored type word 0 on both rows. That workaround and the cube placement stay separate sentences.

LEVEL22.INF function 1003, mask 0x0041, taint 0, calls `loadNewLevel(24, 674, 2)`. LEVEL24.INF function 642, mask 0x0083, taint 0, calls `loadNewLevel(22, 971, 0)`. LEVEL24.INF function 427, mask 0x82C2, taint 0, calls `loadNewLevel(26, 427, 2)`. Level 26 is named Dungeons, area RUIN. These edges are not walkthrough steps.
