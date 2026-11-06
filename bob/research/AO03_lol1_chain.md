# LoL1 chain status, chunks 1 through 9

Read-only plan. Base is `~/lol1_godot` master `9987d7e`. AK01 through AO02 are unapplied. Godot `4.7.2.stable.flathub.ed1daf0bf` ran the ten tests on a scratch of that base and each printed PASS.

Apply order is the list in `grok_research/patches/AM03_lol1_ORDER.md`: AK01, AK02, AL01, AL02, AM01, AM02, AN01, AN02, AO01, AO02. That order is the patch order. The card walk is keep, party, lake, mine, then the White Tower. Sound names files on every level once AO02 is applied.

Each row's test opens its own walk. A file it writes is erased before the test returns. The next row does not read that file.

| Chunk | Patch | Earned test | Starts | Ends | Open gaps |
| --- | --- | --- | --- | --- | --- |
| 1 save | `grok_research/patches/AK01_lol1_save.diff` | `tests/save_roundtrip_test.gd` | No file at `user://ak01_missing.json`. New Michael, level 1 block 557 facing north. | Erases `user://ak01_missing.json`, `user://ak01_round.json`, `user://ak01_hero.json`, `user://ak01_trio.json`, and `user://ak01_bad.json`. | The round trip, the hero ids, and the rejected version stay inside this test. |
| 2 hero select | `grok_research/patches/AK02_lol1_hero_select.diff` | `tests/hero_select_test.gd` | Selection screen. `load_save` is false until this test reloads `user://ak02_hero.json`. | Erases `user://ak02_hero.json`. | The click boxes are the test. Chunk 1's files are not read. |
| 3 combat | `grok_research/patches/AL01_lol1_combat.diff` | `tests/combat_test.gd` | No walk scene and no save. Items and monsters only. Seed 12345. | No save file. | Sounds 0 and 255 stay silent inside combat. This test does not call the chunk 9 resolver. |
| 4 TIM | `grok_research/patches/AL02_lol1_tim.diff` | `tests/tim_opening_test.gd` | Selection screen, then level 1 block 557 facing north. | Writes `user://lol1_al_tim.json`, reloads it, then erases it. | LOLFINAL.TIM stays refused. No chunk 2 file is read. |
| 5 keep | `grok_research/patches/AM01_lol1_keep.diff` | `tests/keep_cards_test.gd` | New Michael, level 1 block 557 facing north. | Writes `user://lol1_am_keep.json`, reloads it, then erases it. | The north gate and the return stay inside this test. |
| 6 party | `grok_research/patches/AM02_lol1_party.diff` | `tests/party_join_test.gd` | New Michael. `save_path` is `user://lol1_am_party.json`. The test does not write it. | Erases `user://lol1_am_party.json`. | Timothy, Baccata, Lora, and the Paulson block stay inside this test. The keep save is not read. |
| 7 lake | `grok_research/patches/AN01_lol1_lake.diff` | `tests/chunk7_cards_test.gd` | New Michael, then level 10 block 1. | Writes `user://lol1_an_chunk7.json`, reloads it, then erases it. | The far side, the skull, the wagon, the ruby floor, Dawn's give, and the nest block stay unread. |
| 7b mine | `grok_research/patches/AN02_lol1_mine.diff` | `tests/mine_path_test.gd` | New Michael, then level 16 block 1. | `user://lol1_an_mine.json` is erased. The test does not write it. | Level 26 is not entered from function 427. The lake save is not read. |
| 8 tower | `grok_research/patches/AO01_lol1_tower.diff` | `tests/tower_cards_test.gd` | New Michael, then level 18 block 1. | `user://lol1_ao_tower.json` is erased. The test does not write it. | The shard, the Whole Truth, Dawn's recovery key, a floor crucible, and a statuette stay unplaced. The ending fight stays unrun. Level 21 prints the step limit at ip 53. The mine save is not read. |
| 9 sound | `grok_research/patches/AO02_lol1_sound.diff` | `tests/sound_files_test.gd` | New Michael, level 1. The test notes the 215 wav stems and the 67 music files. | `user://lol1_ao_sound.json` is erased. The test does not write it. | The resolver returns a name. No mixer is opened. The tower save is not read. |
