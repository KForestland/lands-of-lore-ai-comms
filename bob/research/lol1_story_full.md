# LoL1 story, cards 01 through 13

No Godot was run. The tree is `~/lol1_godot` at `9987d7e`, clean. Cards 01 through 06 use L03 and M03. Cards 07 through 11 use U02. Cards 12 and 13 use U01. LOL1-14 stays out of this table. Disagreeing sentences named in those files stay unmerged here.

`level_scripts.gd` keeps `missing` as an empty dictionary. The default arm of `_call` increments it when a playthrough hits a call that is neither implemented, nor in `IMPORTER_CALLS`, nor in `QUIET_CALLS`. That dictionary has no entries until a script runs. The counts below are static. Each number is how many distinct opcode names in that level's `levelNN_inf.asm` and `levelNN_ini.asm` would take the default arm. Sites are how many `sysCall` lines those names occupy. A site inside a branch that never runs is still counted. The archive asm path is the one named in U01.

## Cards

| card | levels | blocks and flags | items | NPCs | cutscenes | EMC missing, static |
| --- | --- | --- | --- | --- | --- | --- |
| LOL1-01 | none for the select screen; a new game is already on level 1 | first visit stands on block 557 facing north, from M03 | the four hero templates | Ak'shel -9, Michael -1, Kieran -8, Conrad -5 | opening is L06 chunk 4 TIM; this tree does not run TIM | level 1: 51 names, 403 sites |
| LOL1-02 | 1 Gladstone Keep, KEEP | north gate function 621 loads level 2 block 106 face 2 | Writ of Passage 244, Library key 185; atlas has no ONETIME name | King Richard, Geron, in the level 1 dialogue file | throne arrival is the same TIM chunk | level 1, same row |
| LOL1-03 | 5 Thug's Hideout, CAVE1; the walkthrough's Northland sentence stays a second place | lantern 249 on block 97, thug key 167 on block 165, both INI function 1 | lantern, thug key; lockpicks 245 are created on level 6 block 168 and stay a separate sentence | thugs, dialogue substring on level 2 | none named | level 5: 7 names, 14 sites |
| LOL1-04 | 3 Southland Forest, FOREST1; 4 Roland's Manor, MANOR | compass item type UNKNOWN; `compass_broken` is a game flag name with no item | burnt scroll is the walkthrough object; no compass type | Timothy id 2; no concrete `addRemoveCharacter(2)` | Roland's scene is named by the walkthrough; TIM was not executed | level 3: 50 names, 307 sites; level 4: 32 names, 125 sites |
| LOL1-05 | 1 again | poisoning script UNKNOWN | Dawn's spell book, type UNKNOWN | Timothy leaves, Baccata id 3 joins, Dawn id 7; no concrete add for 3 or 7 | Scotia poisons the king; L06 puts this TIM in chunk 4 | level 1, same row |
| LOL1-06 | 6 Caves Level 1, 7 Caves Level 2, 8 Caves Level 3, 9 Caves Level 4, all CAVE1 | Lora add is function 66 on level 7, mask 0x0040, behind a test | Sledge 59 on level 7 INI function 1; Riddle Scroll 241 given by level 8 function 335; Emerald Eye 222 made on level 6 | Lora id 4; the Draracle has no character id in M03 | Draracle meeting is script chat, not a movie file | level 6: 25/71; level 7: 46/144; level 8: 40/213; level 9: 19/62 |
| LOL1-07 | 10 Opinwood holds the Lake Dread substring; the lake and the file name stay unmerged | crossing block UNKNOWN | Victor's longsword is the clue book gift; the Computer Show boat sentence stays | Victor, substring only; Timothy's last scene is the clue book point | none named | level 10: 49 names, 213 sites |
| LOL1-08 | 10 | skull block UNKNOWN; beggar help is 5 silver | Green Skull 266; lightning scroll 235 and the longsword stay optional | beggar; Droek at the wagon | none named | level 10, same row |
| LOL1-09 | 11 Gorkha Swamp, SWAMP | ruby give is function 132, no floor block; Freeze is the written crossing | Ruby of Truth 220; Ceremonial Mask 259 made in function 45; brass helmet stays the Computer Show name with no item row | chieftain, witch doctor, Hurzel | none named | level 11: 64 names, 372 sites |
| LOL1-10 | 10 | Dawn give block UNKNOWN | pyramid key is the Computer Show name; Dawn's Key is type 198; empty flask 211 stays the cave create | Dawn id 7, Droek | none named | level 10, same row |
| LOL1-11 | 12 Urbish Mining Co., 13 Mines Level 1, 14 Mines Level 2, 15 Mines Level 3, 16 Mines Level 4 | silver key on level 15 block 55, DECODED; Paulson add and cube on level 16 function 517, block 611, LIKELY; Lora workaround is level 16 block 549 | Green Skull, Silver key 173, Bloodstone 273, Vaelan's Cube 264, Paulson's Key 200 | Paulson id 6; Larkhon and giant slug stay two names | none named | level 12: 45/267; 13: 13/44; 14: 25/77; 15: 19/79; 16: 44/156 |
| LOL1-12 | 18 Tower Level 1, 19 Tower Sub-level, 20 Tower Level 2, 21 Tower Level 3, all TOWER1 | ivory key level 21 block 37, LIKELY; amber ring level 18 function 559 block 73; altar test is function 40, flag 347, hand item 260; pit function 199 loads level 20 block 199 | Amber Ring 226, Ivory Key 184, Crucible of Faith 260, Minotaur Horn 172, mystic keys 192 through 197 | Lyle and Jana are level 18 strings; no Jana id | none named; the woods Scotia meeting is after the mix | level 18: 47/127; 19: 33/71; 20: 16/74; 21: 33/80 |
| LOL1-13 | 26 Dungeons, RUIN; 27 Castle Level 1, 28 Castle Level 2, 29 Castle Level 3, CIMMERIA | Nathanial's Key level 26 block 75, LIKELY; Shard of truth level 28 function 555 block 520, LIKELY | Shard of truth 281, The Whole Truth 280, Dawn's Key 198, diamond 221, statuette 255, the four pyramid keys 198 through 201 | Dawn in the crystal, King Richard, Scotia | Whole Truth click is an inventory use; no movie file was named | level 26: 45/148; 27: 45/190; 28: 49/393; 29: 47/192 |

`playCharacterScriptChat` is the largest unimplemented name on almost every level in this table. `loadTimScript` is unimplemented on the early levels that L06 assigned to TIM. `moveBlockObjects` is unimplemented on the mine and tower levels, which is where the level 21 stair rewrite has to live. `triggerDoorSwitch` is unimplemented and is common on the mine and castle files.

Importer calls and the quiet calls are already returned as done inside `level_scripts.gd`, so they are outside these counts. `playSoundEffect` is quiet. A White Tower sound id of 255 stays silent when that call is filled, from L06.

## Level rows

The card table's EMC column is these rows, grouped. Names are the six most common unimplemented names in that file pair.

| level | distinct names | sites | six most common unimplemented names |
| --- | --- | --- | --- |
| 1 | 51 | 403 | checkRectForMousePointer, playCharacterScriptChat, drawExitButton, copyRegion, setupDialogueButtons, loadTimScript |
| 2 | 50 | 312 | playCharacterScriptChat, playAnimationPart, checkRectForMousePointer, setupBackgroundAnimationPart, loadTimScript, releaseTimScript |
| 3 | 50 | 307 | checkRectForMousePointer, playCharacterScriptChat, drawExitButton, copyRegion, initAnimStruct, setupBackgroundAnimationPart |
| 4 | 32 | 125 | playCharacterScriptChat, setupDialogueButtons, op_-108, restoreAfterSceneWindowDialogue, updateBlockAnimations, loadTimScript |
| 5 | 7 | 14 | playCharacterScriptChat, op_-108, characterSkillTest, giveTakeMoney, countBlockItems, setMusicTrack |
| 6 | 25 | 71 | playCharacterScriptChat, op_-108, moveBlockObjects, characterSkillTest, update, updateBlockAnimations |
| 7 | 46 | 144 | playCharacterScriptChat, op_-108, drawExitButton, playAnimationPart, playMusicTrack, moveBlockObjects |
| 8 | 40 | 213 | playCharacterScriptChat, startBackgroundAnimation, initAnimStruct, stopBackgroundAnimation, characterSkillTest, setupBackgroundAnimationPart |
| 9 | 19 | 62 | playCharacterScriptChat, playEnvironmentalSfx, distanceAttack, op_-108, characterSkillTest, op_-118 |
| 10 | 49 | 213 | checkRectForMousePointer, playCharacterScriptChat, playMusicTrack, drawExitButton, initAnimStruct, freeAnimStruct |
| 11 | 64 | 372 | checkRectForMousePointer, playCharacterScriptChat, initAnimStruct, setupBackgroundAnimationPart, startBackgroundAnimation, op_-124 |
| 12 | 45 | 267 | playCharacterScriptChat, checkRectForMousePointer, playAnimationPart, copyRegion, initAnimStruct, freeAnimStruct |
| 13 | 13 | 44 | playCharacterScriptChat, op_-108, moveBlockObjects, setDoorState, op_-82, inflictDamage |
| 14 | 25 | 77 | playCharacterScriptChat, triggerDoorSwitch, moveBlockObjects, inflictDamage, op_-108, op_-82 |
| 15 | 19 | 79 | playCharacterScriptChat, triggerDoorSwitch, op_-108, moveParty, characterSkillTest, op_-92 |
| 16 | 44 | 156 | playCharacterScriptChat, startBackgroundAnimation, playAnimationPart, stopBackgroundAnimation, checkRectForMousePointer, setDoorState |
| 17 | 38 | 101 | playCharacterScriptChat, op_-108, setupBackgroundAnimationPart, op_-118, initAnimStruct, op_-117 |
| 18 | 47 | 127 | playCharacterScriptChat, checkRectForMousePointer, op_-108, triggerDoorSwitch, playMusicTrack, playAnimationPart |
| 19 | 33 | 71 | moveBlockObjects, playCharacterScriptChat, op_-120, op_-108, suspendMonster, clearDialogueField |
| 20 | 16 | 74 | playCharacterScriptChat, playEnvironmentalSfx, distanceAttack, op_-108, characterSkillTest, moveBlockObjects |
| 21 | 33 | 80 | playCharacterScriptChat, changeMonsterStat, playAnimationPart, op_-108, op_-109, clearDialogueField |
| 22 | 61 | 468 | checkRectForMousePointer, setupBackgroundAnimationPart, playAnimationPart, initAnimStruct, freeAnimStruct, startBackgroundAnimation |
| 23 | 50 | 281 | triggerDoorSwitch, playCharacterScriptChat, setupBackgroundAnimationPart, moveParty, op_-108, startBackgroundAnimation |
| 24 | 49 | 160 | playCharacterScriptChat, checkRectForMousePointer, op_-108, initAnimStruct, playMusicTrack, playAnimationPart |
| 25 | 4 | 10 | op_-108, moveBlockObjects, op_-82, setMusicTrack |
| 26 | 45 | 148 | playCharacterScriptChat, checkRectForMousePointer, startBackgroundAnimation, setupBackgroundAnimationPart, op_-108, playEnvironmentalSfx |
| 27 | 45 | 190 | moveParty, playCharacterScriptChat, characterSurpriseFeedback, triggerDoorSwitch, op_-108, moveBlockObjects |
| 28 | 49 | 393 | copyRegion, playAnimationPart, playCharacterScriptChat, drawExitButton, checkRectForMousePointer, playEnvironmentalSfx |
| 29 | 47 | 192 | op_-108, playCharacterScriptChat, op_-106, playEnvironmentalSfx, changeMonsterStat, inflictDamage |

Levels 17, 22, 23, 24, and 25 are on the clue book path between the mine and the castle. L03 filed them as LOL1-14. They are in this level list because U04 has to size that path. They are not a fourteenth card in the table above.
