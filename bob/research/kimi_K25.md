# Kimi K25 — LoL1 draft stack AK01..AO02 vs specs (read-only, 2026-11-06)

Lead: good result - every number traces to LoL1 sources (no LoL2 leaks) and all four ScummVM workarounds are present with tests. Follow-ups for the LoL1 lane later (not now, LoL2 chain first): AL01 chase scream path missing shakeScene + removeCharacterItem(i,15); character-hit screamSfx not ported; TIM VOC opcodes 8/10 not wired to play_effect; 3 rendered tests not run + 5 leaked resources in walk tests.

All checks are done. Every diff number I traced landed in a LoL1 source, and all four required workarounds are present. Here is the report.

  # K25 review: AM03 order (AK01–AO02) against the chunk specs

  Reference points used: `lol.cpp` (startupNew, addCharacter, inflictDamage), `sprites_lol.cpp` (placeMonster, updateMonster, chase*), `script_lol.cpp` (olol_moveBlockObjects), `sound_lol.cpp` (snd_playSoundEffect/snd_playTrack), `items_lol.cpp` (updateFlyingObject, checkDrawObjectSpace), `sequence/sequences_lol.cpp` (char selection), `resource/staticres_lol.cpp` (_charPreviews), and the LoL1 DOS CD tables in `devtools/create_kyradat/resources/lol_dos_cd.h` + `lol_dos_cd_english.h`.

  | chunk | spec requirement | in diff | test | ok |
  |---|---|---|---|---|
  | O05 (AK01) | version-1 JSON packet, other versions rejected | save_game.gd `VERSION`/`load_into` | bad-version case | yes |
  | O05 | game section: 100 bit-addressed flags, 24 script vars, 8 vars2, credits/brightness/compass/lamp/update/scene/visited | `_game_section`/`_apply` | round trip | yes |
  | O05 | new game: credits 41, brightness 3, lamp 0, flags 0, vars2 0x100, items 216-218, block 557 dir 0 | `_begin_new_game` | `_assert_new_game` | yes (41 / 0x100 / 216-218 verified in `lol.cpp:923-973`) |
  | O05 | party packet: hero_id, available_spells, characters with face_bank etc. | `_party_section` | hero round trips | yes |
  | O05 | 400 item slots, 1024 chains, bdir, free frame 0x8000, inventory 48, item_in_hand | `_items_section` | round trip | yes |
  | O05 | 30 monster slots + level; load without `monsters.reset` | `_monsters_section`, `reset_count` | reset_count == 0 | yes |
  | O05 | load order items→inventory→party→monsters; no startupNew items on load | `_apply`, `_present_loaded_level` | round trip | yes |
  | O05 | add_character refuses at 3 active; refused id absent | party.gd cap | trio case | yes |
  | P01 (AK02) | ids −9/−1/−8/−5, four 32×32 boxes at (0x060,0x7F)…(0x10F,0x7F), miss −1 | hero_select.gd BOXES/SELECT_IDS | box edge cases | yes (verified `staticres_lol.cpp:687`) |
  | P01 | accept (88,180,41,15) / cancel (196,180,41,15), ZH rects (223,176,42,17)/(271,176,43,17) | ACCEPT/CANCEL/ZH rects | click cases | yes (verified `sequences_lol.cpp:722-740`) |
  | P01 | accept runs new-game order with id; cancel stores nobody, no items 216-218 | `begin_from_selection` | cancel + bad index | yes |
  | P01 | face banks face09/01/08/05; raceClassSex 0,0,2,4; no specialty string | FACE_BANKS | reload + `_has_key` | yes (raceClassSex verified in char table) |
  | P01 | headless export `hero` default Conrad, four names, no click | walk.gd export | export case | yes |
  | P02 (AL01) | set_mode: mode 13 yields only to 14; mode 7 aims party_pos; mode 14 HP 0 | set_mode | `_mode_seven_aims`, `_death_mode` | yes |
  | P02 | update modes 0-14, empty 10/11; flag 0x10 alert walk; same-pointer loop not the alert | update match arms | `_alert` | yes (matches `sprites_lol.cpp:1016-1162`) |
  | P02 | mode 14 clears damageReceived; mode 5 partyAwake; 8→5 with modifiers3; 9→7 flags&0xFFF7; 12 script 0x404; 13 kill | update | `_death_mode` | yes |
  | P02 | inflictDamage monster path: mode ≥13 returns 0, `0x8000|damage`, flag 0x10, hitOffs 1..24−12, clip to property total, 0 → mode 13 | inflict_damage | `_monster_damage` | yes (verified `lol.cpp:3553-3587`) |
  | P02 | character path: id match above 3, flag 1/8 refusal, face 6 for 4 ticks, cloud ring 229 flags==4 shifts >>2, HP 0 → flag bit 8 | inflict_damage | `_character_damage` | yes (verified `lol.cpp:3590-3624`, with gaps noted below) |
  | P02 | large-fireball width 63, 256 expression commented out | large_fireball_step | `_fireball` | yes (verbatim `items_lol.cpp:548`) |
  | P02 | placeMonster silent on sounds[0] 0 or 255 | place | `_silent_sounds` | yes (verified `sprites_lol.cpp:278-294`) |
  | P03 (AL02) | opening asks LOLINTRO.TIM, no substitute file, runs to end | TimPlayer.play_opening | BANNED list checks | yes |
  | P03 | keep starts 557 dir 0 after opening; throne_played/poisoning_played booleans, no replay after reload | play_throne/play_poisoning + packet fields | save/reload case | yes |
  | P03 | null WSA skips frame, TIM continues; LOLFINAL.TIM refused | opcode 6 null check; load_file refusal | opcode sequence [6,1] | yes (opcode map matches `script_tim.cpp` LoL table: 13/16/17/24/28/29→1, 30→−1) |
  | P03 | sound opcodes 8-14 quiet; chunk 4 adds no joins | sound_calls; poisoning keeps Timothy | ids unchanged | yes |
  | P04 (AM01) | gate: fn 621 mask 0x41 → L2 block 106 dir 2; fn 74 → L1 block 589 dir 0 | test drives INF scripts | gate asserts | yes |
  | P04 | missing-call rule; playSoundEffect quiet and uncounted | keep test LISTED set | missing sweep | yes |
  | P04 | placements: 166 L4/41, 167 L5/165, 249 L5/97, 245 L6/168 (not L5), rock 99 not a plate | item sweep asserts | `_place` checks | yes |
  | P04 | ogre accepts bluff and fight, neither only | ogre_accepts | assert | yes |
  | P04 | display spellings: Double ring; Nathaniel's Key ENG only; FRE/GER Duble fixed | patched_item_name/drawn_item_name | string asserts | yes |
  | P04 | writ not required; atlas and compass absent | asserts | reload case | yes |
  | P05 (AM02) | Timothy 27/5, skills 3 2 1, items 93,131,153,162; Baccata 22/18, 1 1 3, 108,149,145,153,129; Lora 25/48, 5, 1 4 1, 137,162 | charDefaults in static tables | stat/type asserts | yes — all verified against `lol_dos_cd_english.h` |
  | P05 | count vs leading_count; deactivate via negative id | party.gd | join/leave asserts | yes |
  | P05 | workaround: full party, slot 2 id 4, id 6, level 16 block 0x225 → items placed 0,0 flying 0, message flag, replace index 2; block 0x226 and wrong slot refuse | add_character | all three cases | yes (verified `lol.cpp:1237-1254`) |
  | P05 | item script 0x80 never run by joins | run_item_script counter | script80_runs == 0 | yes |
  | P06 (AN01) | poisoning no replay; level-10 reload stays on entered block | booleans + packet | save/reload | yes |
  | P06 | swamp crossing is Freeze only | swamp_accepts | assert | yes |
  | P06 | silver key 173 on level 15 block 55 | item sweep | `_at(173,55,8)` | yes |
  | P06 | moveBlockObjects syscall with 0x3E0 → L20/0x0247 rewrite; other destinations unchanged; item stays in 400-slot table; 0x80 script only when run_script and level still current | move_block_objects | `_stair` | yes (verified `script_lol.cpp:1528-1578`) |
  | P06 | Paulson absent unless the script's own call adds him | party asserts | mine entry | yes |
  | U04/7b (AN02) | function 517 does not add Paulson or cube 264 while its flag tests fail | test drives fn 517 | asserts | yes (matches U04 risk note) |
  | U04/7b | two bloodstones (273) block 0; woods stairs 674, 971, 427; fn 427 leaves party L24 block 395 with L26 load pending | INF script run | asserts | yes (fn 427 = loadNewLevel(26,427,2) per U01) |
  | U04/7b | no invented blocks from printed map numbers; honey/earth powder/Geron's key absent | ABSENT sweep | asserts | yes |
  | P07/U01 (AO01) | ivory key 184 L21/37; Nathanial's key 199 L26/75; castle keys 202/211, 205/200, 179/915, 204/995 L29; shard 281 and Whole Truth 280 unplaced; Dawn's key 198 absent | INI placements + sweeps | asserts | yes (matches U01 script checks) |
  | P07/U01 | conditional creates stay unplaced (fn 555 shard, fn 846 Dawn's key, fn 40 crucible flag 347) | test drives functions | count/flag asserts | yes |
  | P07/U01 | LEVEL21 fn 199 → L20 block 199; LEVEL26 fn 734 → L23 block 857 | pending_level asserts | asserts | yes |
  | P08 (AO02) | playSoundEffect wired to the bank, leaves QUIET_CALLS, missing does not gain it | level_scripts.gd + sound.gd | syscall test | yes |
  | P08 | tracks −1, 0, 1 (last −1/1), 255, ≥250 silent | play_effect guards | track asserts | yes (verified `sound_lol.cpp:158-164`) |
  | P08 | volume mask 0xFF then {223,159,95,47,15,0}→{255,191,127,63,30,0}; −1→255→255; 160→191 | VOL_IN/VOL_OUT | volume asserts | yes (tables verified `sound_lol.cpp:170-178`) |
  | P08 | EMPTY/missing stem silent; DOS MT32/GM/PCSpkr fallback and 168→167 not ported | _voice + comment | stem-erased case | yes (spec allows: "index arrays were not copied") |
  | P08 | music map (track−250)*3; 250 names LORE01A; out-of-set stem not played | play_music | asserts | yes (verified `kLoLMusicTrackMapDOSCD`, `snd_playTrack`/`snd_loadSoundFile`) |
  | P08 | 215 VOCs / 67 music counted from the archive dirs | test counts | asserts | yes |

  ## Problems

  **LoL2-number check (P02 rule): none found.** Every game number in the diffs traces to a LoL1 source: party stats and starting items match `kLoLCharacterDefsDOSCDEnglish` exactly (including Lora's 25 cur / 48 max); scream attack damage 20 and sound 147 match `sprites_lol.cpp:1244-1257`; hit offsets 1..24−12 match `lol.cpp:3566-3569`; the volume tables, the 500-entry sfx index, the 230-name sfx list, and the music map match the DOS CD tables in `lol_dos_cd.h` (track 12 → index 52 → PMETLHI, track 250 → LORE01A); hero boxes/attribute bytes/accept rects match `staticres_lol.cpp:687` and `sequences_lol.cpp:722`; credits 41, vars2 0x100, and items 216-218 match `lol.cpp:923-973`.

  **Required workarounds: all four present, with tests.**
  - Large-fireball width 63: `large_fireball_step` in AL01, 256 left commented out (exactly `items_lol.cpp:548`), tested.
  - White Tower sound 255 silent: AL01 `place` (0 and 255) plus AO02 track 255 silent, tested.
  - addCharacter full-party + Lora workaround: AM02 `add_character` (slot 2 id 4, id 6, level 16, block 0x225, items placed at offsets 0,0 flying 0, message flag, replace index 2), tested including the 0x226 and wrong-slot refusals.
  - White Tower stair fix: AN01 `move_block_objects` rewrites L21→L21 block 0x3E0 to L20 block 0x0247, other destinations untouched, item stays in the table — tested.

  **Gaps and deviations worth noting (not LoL2 leaks):**

  1. AL01 `inflict_damage` character path guards the hit-point write with `target <= 2`; ScummVM applies it to any matched slot 0-3 (`lol.cpp:3616`). Slot 3 is unreachable in LoL1 (party capped at 3), so impact is nil, but it is a deviation.
  2. AL01 `_chase_distance` flying==1 plays sound 147 and inflicts 20 damage correctly but omits the source's `shakeScene(10,2,2,1)` and `removeCharacterItem(i, 15)` (`sprites_lol.cpp:1245-1256`). Not covered by any spec test.
  3. The character-hit scream (`screamSfx`, skipped on flag 0x1000) described in P02's Data section is not ported anywhere; P02's test list does not require it.
  4. AO02 wires only `play_music_track` into TimPlayer; TIM VOC opcodes (8, 10) still just append to `sound_calls`. P08's "TIM may call the player" is satisfied for music but the `tlol_playSoundEffect` → `play_effect` path is not wired (the EMC path is).
  5. AN01 `move_block_objects` omits the source's `checkSceneUpdateNeed` calls (its own comment says so) — visual refresh only, no game-state effect.
  6. P05's text says "Lora … hit points 48" while the LoL1 table is 25 cur / 48 max; AM02 correctly asserts the table values. Spec-text imprecision only, not a wrong number in code.
  7. Declared by AM03 itself: `party_test.gd`, `script_walk_test.gd`, and `items_test.gd` were not run (they wait on `RenderingServer.frame_post_draw`), and the walk-scene tests print "5 resources still in use at exit" after PASS.

