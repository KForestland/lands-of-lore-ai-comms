# L01 LoL1 decoded data

No Godot was run. The public notes are `~/lands-of-lore-1-re` (README status about 99.999%, `docs/closure_memo.md` dated 2026-03-20). The extracted pictures and sound are not in that repo. They are under `<owner-media>`. The memo's old `~/lol1_*` paths are not there anymore. The Godot core is `~/lol1_godot`. Its generated levels are on disk and are gitignored.

## Where each kind of data is

| kind | decoded as | files |
| --- | --- | --- |
| Levels | 29 maps. CMZ is a 32×32 grid, four uint8 wall ids per block. Level 24 is 9 bytes per block. Tilesets KEEP, FOREST1, MANOR, CAVE1, SWAMP, URBISH, MINE1, TOWER1, YVEL1, CATWALK, RUIN, CIMMERIA. | Memo and `docs/level_tileset_map.md`. Rendered maps: archive `lol1_levels_rendered/` (29 files). Wall records: `lands-of-lore-1-re/data/wll_parsed.json`. Godot: `assets/lol1/generated/level01` through `level29` (29 directories). |
| Scripts | 60 EMC2 scripts decompiled to asm. 19 VM opcodes and 192 game opcodes, per the memo. TIM dialogue timing is separate: 139 AVFS files, all parsed. | Archive `lol1_scripts_decompiled/` (29 `levelNN_inf.asm`, 29 `levelNN_ini.asm`, `onetime_inf.asm`, `item_inf.asm`). TIM inventory: `lands-of-lore-1-re/data/tim_analysis.json`. The public `tools/` directory has no EMC decompiler. The port runs the original bytecode in `scripts/lol1/emc.gd`. |
| Items | 285 types, built by running ONETIME.INF. | `tests/items_test.gd` asserts `properties.size() == 285`. There is no item-name JSON in the RE `data/` directory. |
| Monsters | 44 shape banks. 30 live slots. Properties are filled by the level script, not by a static row count. | `assets/lol1/generated/ui/monsters.json` has 44 keys, one per `.SHP`. `scripts/lol1/monsters.gd` `MAX_MONSTERS` is 30. |
| Spells | 17 property rows from ScummVM `lol_dos_cd.h`. Each row has a name code, four magic costs, and four hit-point costs. Some name codes are 0. The names were not looked up. | `scripts/lol1/static_tables.json`, key `spellProperties`. |
| NPCs | Nine character templates: Michael, Timothy, Baccata, Lora, Conrad, Paulson, Dawn, Kieran, Ak'shel. The four starting heroes are Ak'shel, Michael, Kieran, and Conrad. Speech is the dialogue corpus, not a separate NPC file. | `charDefaults` in `static_tables.json`. Dialogue: `data/dialogue_summary.json`, 90 files, 6495 strings, 2165 each in ENG, FRE, and GER. LANDS.ENG is 735 strings. Clean text: archive `lol1_dialogue_decoded/` (90 files). |
| Movies | No movie container is in the PAK index. The moving pictures are WSA. 241 files, 4480 frames, inventory `decoded` 241 and `failed` 0. TIM opcodes play those frames with text, VOC, and music. | `data/wsa_inventory.json`. Frames: archive `lol1_wsa_all_frames/` (4481 files, the frames plus one extra file that was not opened). |
| Music | 67 files: XMI 18, C55 17, ADL 16, PCS 16. | `data/music_inventory.json`. The JSON still names output `~/lol1_music`. The files now sit in archive `lol1_music/` (67 files). |
| Also extracted | CPS 85, SHP 89 files / 3492 frames, VOC 215, fonts 4, VCN 13, palettes 11. | Archive `lol1_cps_complete` 85, `lol1_shp_rendered` 3492, `lol1_audio_complete` 215, `lol1_fonts` 10, `lol1_vcn_tiles` 20. Inventories in `lands-of-lore-1-re/data/`. |

## One header correction

`docs/closure_memo.md` says a SHP has a 12-byte alternate header with a 2-byte prefix. `lol1_godot/tools/scene_shapes.py` says a CD shape has no alternate header. This pass did not decode a frame. The importer is the later note for the CD data the port reads.

## Still not a game database

Item names, spell names, and a full NPC list are not published as tables. They are inside ONETIME.INF, the string codes, and the ENG files. Combat numbers are not in this inventory.
