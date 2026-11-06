# Kimi K21 — LoL1 story table + U01/U02 vs MAPS_LOL1 + decompiled scripts (read-only, 2026-11-06)

Lead spot-check: func_132 absent from level11_inf.asm (confirmed); func_45 present. Decompiled scripts moved 2026-11-03 to <owner-media> (mount Arikv). Four function/item-id errors in grok's LoL1 docs (Riddle Scroll 241 vs 234 at L8 func_335, Ruby func 132 -> 45, flask func 0+1 -> 1, Bloodstone func 18 -> label L_18 in func_1); levels and block ids all verify. Fix in the LoL1 docs before chunk work starts.

All checks are done. Here is the K21 report.

  # K21 verification: lol1_story_full.md, U01, U02 vs MAPS_LOL1 + decompiled scripts

  Scope notes: each `MAPS_LOL1/LEVELn/` folder contains only `markers.json`, so "block exists in the level's map" was checked against that file's `block` fields (plus script references). All 29 level script pairs (`level01`–`level29`, `_inf.asm` + `_ini.asm`) are present at `<owner-media>`, and all 29 map folders exist — no missing level numbers anywhere. U01's note that `~/lol1_scripts_decompiled` is absent and the archive copy is the one in use is accurate.

  ## Verification table

  | card | level | block/flag/item | found | evidence |
  |---|---|---|---|---|
  | LOL1-01 | 1 | start block 557 face north | yes | MAPS_LOL1/LEVEL1/markers.json (block 557, DECODED) |
  | LOL1-02 | 1→2 | func 621 `loadNewLevel(2,106,2)` | yes | level01_inf.asm:4873-4876 (`push 2; push 106; push 2; sysCall 60`); LEVEL1 marker block 621 (LIKELY). LEVEL2 markers.json has no block-106 entry (docs claim none) |
  | LOL1-02 | 1 | Writ of Passage 244, Library key 185 | partial | 185: level01_inf.asm:4400; 244: not in level01 scripts (appears in level03_ini/inf, level22_ini, level26_inf) — docs pin no location, see notes |
  | LOL1-03 | 5 | lantern 249 @ block 97, thug key 167 @ block 165, INI func 1 | yes | level05_ini.asm func_1 (asm 234-241: 165/167; asm 255-261: 97/249); LEVEL5 markers 97, 165 (LIKELY) |
  | LOL1-03 | 6 | lockpicks 245 @ block 168 | yes | level06_ini.asm func_1 (asm 467-476); LEVEL6 marker 168 (DECODED) |
  | LOL1-06 | 7 | Lora add func 66, addRemoveCharacter(4), behind tests | yes | level07_inf.asm func_66 (asm 2992-3005: checkForCertainPartyMember(4) + testGameFlag 9 → addRemoveCharacter(4)); "mask 0x0040" not visible in asm (map-trigger property, see notes) |
  | LOL1-06 | 7 | Sledge 59, INI func 1 | yes | level07_ini.asm func_1 (asm 489-495, block 196) |
  | LOL1-06 | 8 | Riddle Scroll 241 "given by function 335" | **NO** | level08_inf.asm func_335 (asm 2164-2175) creates type **234** (Freeze scroll per M04) on block 368 via createLevelItem — see Mismatch 1 |
  | LOL1-06 | 6 | Emerald Eye 222 made | yes | level06_ini.asm func_1, makeItem 222 (asm 343-347) |
  | LOL1-07/U02 | 10 | no constant-destination loadNewLevel | yes | level10_inf.asm:1205 — only loadNewLevel, all args `pushBPAdd` (non-constant) |
  | LOL1-08/U02 | 10/17 | no constant createLevelItem of Green Skull 266 | yes | level10_inf.asm:3290 (266 feeds no floor create), level17_inf.asm:1041 (createHandItem 266) |
  | LOL1-09/U02 | 11 | Ceremonial Mask 259 makeItem, func 45 | yes | level11_inf.asm func_45 (asm 6217-6219) |
  | LOL1-09/U02 | 11 | Ruby of Truth 220 give "function 132" | **NO** | no func_132 in level11_inf.asm or level11_ini.asm; giveItem(220) is inside func_45 (asm 6347, 6376) — see Mismatch 2 |
  | LOL1-10/U02 | 8 | empty flask 211 @ blocks 117, 469, "INI functions 0 and 1" | **partly wrong** | both creates are in func_1 (level08_ini.asm asm 353-357, 365-370); func_0 has none; markers agree (both func 1) — see Mismatch 3 |
  | LOL1-10/U02 | 24→29 | func 846 places Dawn's Key 198 on level 29 block 1021 | yes | level24_inf.asm func_846 (asm 3071-3086: 1021, 29, 198, createLevelItem); LEVEL29 marker 1021 is type 22 (DECODED), as docs say |
  | LOL1-11/U02 | 15 | silver key 173 @ block 55, offset 0,128, INI func 1, DECODED | yes | level15_ini.asm func_1 (asm 360-367); LEVEL15 marker 55 (DECODED) |
  | LOL1-11/U02 | 16 | Bloodstone 273 makeItem, "INI function 18" | **partly wrong** | level16_ini has only func_0/func_1; makeItem(273) is in local subroutine `L_18` (level16_ini.asm:50-74, asm 33-35), reached by `jmp L_18` from func_1 — see Mismatch 4 |
  | LOL1-11/U02 | 16 | cube 264 + addRemoveCharacter(6) func 517 @ block 611, flags 230/78 | yes | level16_inf.asm func_517 (asm 1840-1910: testGameFlag 230 ×2, testGameFlag 78, createLevelItem 264 @ 611, addRemoveCharacter(6)) |
  | LOL1-11/U02 | 16 | markers on block 611 are other INI items (chain mail 134, great helm 140, …) | yes | LEVEL16/markers.json block 611: 10 DECODED INI rows (134, 140, 248, 33, 262, 130, 149, 176) + LIKELY cube row |
  | LOL1-11/U02 | 16 | Lora workaround block 549 (0x225) | yes (script ref) | block 549 referenced twice in level16_inf func_517 (asm 1904, 1914); the drop-items behavior itself is ScummVM-side (not in these corpora); block 549 not in LEVEL16 markers |
  | LOL1-12/U01 | 18 | Amber Ring 226, func 559 @ block 73 + giveItem, wall-type + inventory tests | yes | level18_inf.asm func_559 (asm 1743-1765: 73/226 createLevelItem + giveItem; getWallType asm 1705; checkInventoryFull/getItemInHand asm 1731-1757); LEVEL18 markers lack block 73, as doc says |
  | LOL1-12/U01 | 21 | Ivory Key 184 @ block 37, INI func 1, marker LIKELY | yes | level21_ini.asm func_1 (asm 535-539); LEVEL21 marker 37 (LIKELY) |
  | LOL1-12/U01 | 18/21 | mystic keys 192@548, 196@393 (L18 INI f1), 195@591 (L21 INI f1) | yes | level18_ini.asm func_1 (asm 804-809, 818-823); level21_ini.asm func_1 (asm 521-526); LEVEL21 marker 591 (LIKELY); 548/393 have no markers (none claimed) |
  | LOL1-12/U01 | 20 | Minotaur Horn 172 makeItem, INI func 1 | yes | level20_ini.asm func_1 (asm 214-216) |
  | LOL1-12/U01 | 18 | altar: func 40, item-in-hand 260, sets flag 347, changes wall | yes | level18_inf.asm func_40 (asm 2677-2736: getItemInHand, cmp 260, setGameFlag 347, setWallType ×5, deleteHandItem) |
  | LOL1-12/U01 | 21→20 | func 199 `loadNewLevel(20,199,getDirection)` | yes | level21_inf.asm func_199 (asm 2344-2349) |
  | LOL1-12/U01 | 24→26 | func 427 `loadNewLevel(26,427,2)` | yes | level24_inf.asm func_427 (asm 1812-1816) |
  | LOL1-12/U01 | 26→23 | func 734 `loadNewLevel(23,857,dir)` after moveBlockObjects | yes | level26_inf.asm func_734 (asm 4388-4402) |
  | LOL1-12/U01 | 18 | strings LYLE and JANA in LEVEL18.INF | yes | level18_inf.asm:15-23 (str[14]="LYLE", str[19]="JANA") |
  | LOL1-12/U01 | 26 | Vaelan's Cube 264 placed by funcs 414 and 834 | yes | level26_inf.asm func_414 (asm 3880-3882, 3960-3962) and func_834 (asm 3194-3196, 3257-3259): makeItem+giveItemToMonster and createLevelItem |
  | LOL1-13/U01 | 26 | Nathanial's Key 199 @ block 75, INI func 1, marker LIKELY | yes | level26_ini.asm func_1 (asm 861-865); LEVEL26 marker 75 (LIKELY) |
  | LOL1-13/U01 | 28 | Shard of truth 281, func 555 @ block 520 + giveItem, wall-type test | yes | level28_inf.asm func_555 (asm 7103-7117; getWallType asm 6631/6663); LEVEL28 markers lack 520, as doc says |
  | LOL1-13/U01 | 28/29 | The Whole Truth 280 pushed in both INF files | yes | level28_inf.asm ×6 (e.g. asm 3563), level29_inf.asm:3934 (asm 4184) |
  | LOL1-13/U01 | 29 | keys 202@211, 205@200, 179@915, 204@995, INI func 1; dull-key marker DECODED | yes | level29_ini.asm func_1 (asm 783-838); LEVEL29 markers 211/200/915/995 all DECODED |
  | all | — | item type↔name pairs (249 Lantern … 281 Shard of truth, mystic keys 192-197, pyramid keys 198-201) | yes | M04_lol1_tables.md item table matches every pair cited |

  ## Mismatches

  1. **Riddle Scroll 241 / level 8 function 335** (story card LOL1-06, line 16). `level08_inf.asm` func_335 does a `createLevelItem` of type **234** on block 368 behind a wall-type test — type 234 is "Freeze scroll" in the M04 table (`M04_lol1_tables.md:249`); Riddle Scroll is 241 (`M04_lol1_tables.md:256`). No `push 241` anywhere near func_335. Wrong item type (and it's a floor create, not a give).
  2. **Ruby of Truth "function 132"** (story card LOL1-09, line 19; U02 line 42). No `func_132` exists in `level11_inf.asm` or `level11_ini.asm` (level11_inf has func_131, func_135, … but no 132; level11_ini has only funcs 0 and 1). The `giveItem` on type 220 is inside **func_45** (asm 6347→6376) — the same function that makes the Ceremonial Mask. The function number is wrong in both files.
  3. **Empty flask "LEVEL8.INI functions 0 and 1"** (U02 line 50). Both constant flask creates (blocks 117 and 469) are in **func_1** only; func_0 contains no flask create (its only 211 push is an `initMonster` argument). The LEVEL8 markers also attribute both blocks to function 1. The blocks are right; the "functions 0 and 1" split is wrong.
  4. **Bloodstone "LEVEL16.INI function 18"** (U02 line 80). `level16_ini.asm` has only two ORDR functions (0 and 1). The `makeItem(273)` sits in the local subroutine labelled `L_18` (asm addresses 18-42, file lines 50-74), which func_1 reaches via `jmp L_18`. Looks like a label-vs-function-number confusion; the substance (makeItem 273, no block argument, LIKELY grade) is correct.

  ## Notes (checked, not mismatches)

  - Writ of Passage 244 has no level-1 script site (appears in levels 3, 22, 26); the story card 02 item row makes no placement claim, so this is informational only.
  - "Mask 0x0040" for the level-7 Lora add is not recoverable from the decompiled asm (it is a map-trigger property); the function, the tests, and `addRemoveCharacter(4)` are all confirmed.
  - U01's `olol_moveBlockObjects` 992→583 stair rewrite and U02's Lora item-drop behavior are ScummVM `script_lol.cpp` claims — outside MAPS_LOL1 and the decompiled scripts, so unverifiable here; block 549 is at least referenced by level16_inf func_517.
  - `onetime_inf.asm` contains no ATLAS/writ/library strings, consistent with the story's "atlas has no ONETIME name".

