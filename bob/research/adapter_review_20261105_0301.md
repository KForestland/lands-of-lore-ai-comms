# R2 adapter review, rows 0301–0308, 2026-11-05

No Godot was run. No opcode callee was entered. LOLG.DAT was not opened. The longplay was not opened. r15 is `f6a5aa4`. r12y is `56812f9` and has 228 deviation files. These twelve numbered files are absent there. cmp says r15 only. `adapter_review_20261103.md` already opened the temple sections. `adapter_review_20261104.md` slice 7 already opened the six later rows. Those files stay as they are. This pass reads the named hosts and the same printed sentences.

The opcode-18 text also numbered 0306 still matches astraprogression `6986998` byte for byte. It stays the 2026-11-03 review. `0xB2A54` and `0x65BB0` were not entered.

## 0301 temple-blade-bypass-boulder

Doors 81 then 80 rise by 80 after the oil covers close. Region 777 starts a 2-second falling boulder. Descent 180, the lethal window 0.75 to 1.5 seconds, and centre bands 62 and 55 stay modern tuning. Native trigger and motion stay unentered.

DECODED. `l14_trap_route.gd` raises movables 81 then 80 on local E, and only after the flute slot is covered. The boulder is template image 473 at 130 by 80. It starts at (29, 360, 1136) and drops 180 in the first second, then holds through elapsed 2. The lethal test is that window, those bands, and feet 130 to 180. The start box is a coordinate test. It does not name region 777. That region id stays the row.

HINTBOOK lines 4585–4589. Do not walk into the blades. The right passage bypasses them. The centre of the next hall is a sudden boulder. One side is safe. The lines print no 80, no 2 seconds, and no band. The raise and the fall stay the adapter. No simpler native build.

## 0302 temple-idol-stair-crossing

Three cases take one earned idol each. Fourteen stair meshes move over 4 active seconds. The cases drop by 250. Word 10 stays unread. Opcode 18 mode stays unentered.

DECODED. `l14_idol_pedestals.gd` owns movables 85, 86, and 87 and static assemblies 90 through 103. Each case node starts at y -250. `l14_idol_bridge_plan.json` has 14 stairs. Each `unentered_word10` is 129. The motion lerps the listed from and to points, and the sample stair keeps y 260. Heading is interpolated. Word 10 is not a height. The 2026-11-03 note that temple flags `0x0081` lack `0x0004` still supplies no replacement motion.

HINTBOOK lines 4594–4595. One statue on each of three pedestals, then an opening. The lines print no 4 and no 250. The interpolation stays the adapter. No simpler native build.

## 0303 temple-hopper-body-platform

Five hoppers wake on the raised gallery. Dead bodies settle at 80 units a second. Hover holds 340. Five modern corpse ids, then a Human step, run a 4-second descent. The opcode 3 drop stays a venom sac, not a corpse. The weight join stays modern.

DECODED. `l14_hopper_platform.gd` names actors 91 through 95. A living body is pulled toward y 340. A dead uncollected body uses velocity y -80. Carry ids are `act2:L14_HT:hopper_corpse` plus the actor id. `lowered` advances by process `delta` to 4. Floor 2447 uses the -370 offset. The other named floors use 200. The host does not read source words 300, 500, or -70. Those words stay the row.

HINTBOOK lines 4606–4608. Kill the five hoppers. Do not step on the wooden platform while placing the corpses. Step on it only when all five are there. The lines print no hover, no 80, and no 4 seconds. The encounter stays the adapter. No simpler native build.

## 0304 temple-weighted-platform-return

The book stops at the step onto the platform. The ride back is a separate 4-second return clock. Direct jump from the low floor fails. No printed duration replaces that clock.

DECODED. The same host keeps `l14_hopper_return`. Local E after `lowered` is 4 starts `raised`, which advances by `delta` to 4. The five corpse receipts stay. The player rides the same floor nodes. No new landing is built. The source caller stays unentered, as the row says.

## 0305 temple-belial-admission

The file holds the elevator admission, the faux-Belial fight, and the optional return guard. Flags `0x0004` stay the row's relocation claim. Host activation, grounding, the summary, and the reflection stay adapters. Dialogue and reflection modes stay unentered.

DECODED. `l14_belial.gd` admits on local F only after five committed corpses, `lowered` 4, and a settled return (`raised` 0 or 4). A moving phase is refused. Arrival is (42, 22, 11041). Floors 2137 through 2142 drop by 360, which is the row's 350 to -10. Feet use the shared 32 offset. `act2_creatures.gd` keeps actor 90 peaceful until E. That E wakes him and prints the modern warning. G requests Beast form 1 for 120 seconds, or Human back. `permits_hit` refuses a non-Beast melee and reflects other hits by at most 15. `L14_HT.json` actor 90 stores health 50 and constructor operands 50 and 1600. The mapping grade there is LIKELY. This pass did not enter the opcode 18 callee.

HINTBOOK lines 4616–4631. The fight follows a long conversation, so pre-cast spells wear off. Beast form wins. Any other form loses. The Beast has no useful missile weapons and no spells. The lines print no 15, no E key, and no 50. The summary and the cap stay the adapter. No simpler native build.

## 0306 l8-larkhon-tree-guidance

Within 600 of actor 115 the journal line matches the earned step. Within 420 of torches 1338 through 1342 the torch line shows while fewer than five are lit. The L8 to L12 refusal appends the same guardian line. Radii and notes stay modern. No mechanic changes.

DECODED. `l8_larkhon.gd` sets `NEAR` to 600 and cites deviation 0306. `l8_larkhon_state.gd` holds the four `JOURNAL_HINTS`. `l8_tree.gd` sets `NEAR` to 420 around the mean of the five torches and cites the same deviation. `act2_progression.gd` appends `note_guidance` when the dose receipt is missing.

HINTBOOK lines 3075–3077. The shaman gives a potion for a silverleaf. Luther needs it for the Claw Mountains. Lines 3151–3157. Combine the potion and the leaf, left-click to activate, then right-click the Larkon's upper chest. The lines print no radius. The journal lines and both radii stay the presentation adapter. Line 3105 says to visit the platform after the first green shard. Line 3107 says the spark raises new steps after the stairs and the torches. That order stays the book's.

## 0306 target-status-single-line

One top-left line per area host. The fall wording wins while Luther is down. A stale aim line is not drawn. The Hive guardians' own line still wins that spot. The Cave keeps its HUD-hint fall prompt.

DECODED. `target_status.gd` hides each population label and draws one line at (16, 48). `FELL` is `You fell · R: recover here · F9: load save`. `compose` returns that string when health is 0, else the first text of a population that is processing. `yield_to` clears this line while another owner's label overlaps it. No book sentence was opened. The fall wording stays the row.

## 0306 opcode18-native-direct-relocation

Flags `0x0004` select direct relocation. Signed +4 and +6 are the horizontal destination. Height is assigned only with `0x0100`. +12 is heading. The City elevator gameplay stays unimplemented. Citadel `0x0293` and temple-stair `0x0081` still lack `0x0004`. The Wild Village shaman place call is not opcode 18.

DECODED. The numbered file matches astraprogression `6986998`. `native_script_host.gd` `_op_eighteen` still writes `0xb7d5e` `command_file_offset` only when the staged read is 0. The later note `opcode18_b27a3534.md` already read that call on build b27a3534. This pass did not enter `0xB2A54` or `0x65BB0`. No book sentence names flag `0x0004`. No simpler build is added.

## 0307 confidante-journal-hint-armorer

The note `no_confidante_yet` now names Kit'yara's glen. The Confidante gate stays the native gate. The "before the Hive" order stays the row.

DECODED. `thieves_den_state.gd` stores the Kit'yara sentence. `jungle_confidante.gd` `_journal_region` still records that note only in region 3408 when shared 47 and shared 25 are clear. This pass did not re-read a Hive sentence.

HINTBOOK line 2253, chapter 6. Go directly to the south to the Armorer's Glen. The new note names Kit'yara there. The gate stays the row's.

## 0307 l8-larkhon-stays-asleep

After the chest receipt the guardian stays asleep. The 60-second clock only drives the falling-asleep frames. Regions 3455 through 3457 are not re-armed. The L8 to L12 exit checks the receipt, not the clock. The second-potion supply stays unhosted. The printed wake stays unhosted.

DECODED. `l8_larkhon.gd` is the host. It cites deviation 0307. `asleep` is the used receipt. `SLEEP` is 60. `_process` subtracts `delta` while the world is active. That clock stays a frame clock. Selector 9 plays, then resting selector 8 holds, and collision is cleared. Lines 83 through 85 open regions 3277 and 3278 only after the dose, and write 3455, 3456, and 3457 open. The comment says no expiry softlock. `act2_progression.gd` refuses level 12 until `used`. Row 0165 still says those five regions follow the data bit until a script changes them. This script is that change. It does not replace that sentence.

HINTBOOK lines 3177–3178. The Larkon still sleeps. Once you exit, it awakens. Lines 4256–4258. It wakes after some distance, and a return needs another potion. Lines 3119–3122. The tree-room slots make that second potion. The port keeps the sleeping half and does not host that supply.

## 0308 shaman-serum-standalone-refusal

Use of the shaman serum is refused. The serum stays carried. Mixing is unchanged. Other definition 119 serums still take handler 98. Item 26 stays unverified as a replacement, as the row says.

DECODED. `player_item_controller.gd` returns on `l8_shaman_trade.gd` `SERUM` after the refusal string and does not erase it. Any other `amaranth_serum` is appended to spent and erased. `item_catalog.gd` marks definition 119 as that use and names handler 98. `act2_items_source.json` still lists `act2:L8_SJ:item26` as definition 119, identity 77237872, handler 98, grade LIKELY. This pass did not treat that placement as a replacement route.

BRADY line 1556, printed page 42. Amaranth serum has no effect by itself. HINTBOOK lines 3163–3165 say to reload a flung potion. The refusal stays the bug fix. No simpler native build.

## 0308 talker-voice-reach

Kelsrick, Jungle Dawn, escort Bacatta, and Hive Dawn 20 use speech `unit_size` 300. Native attenuation stays untraced. The value stays the port loudness adapter.

DECODED. `jungle_kelsrick.gd` sets `VOICE_UNIT_SIZE` to 300. `jungle_dawn.gd`, `jungle_bacatta.gd` (prop 552, bacatta, and guard 60), and `hive_dawn20.gd` copy that constant. A search of `hintbook.txt` and `brady_guide.txt` found no volume, loudness, attenuation, or "no sound" sentence. No book sentence replaces 300.

## Ledger tail 2026-11-04

`DEVIATIONS.md` ends at the 2026-11-04 Museum dragon lair sentence. There is no numbered file for it under `docs/deviations`. The picture is source wall 34 on region 1425, x 2946 to 3156, z -1247.5, y -20 to 120. A left click on the dragon from inside region 1422 starts DRAGON7, DRGNFLGT, and DRAGON8, then the Jungle. The prompt is on the outline only. E stays the fallback. The native click dispatch stays untraced. The hotspot stays a presentation adapter.

DECODED. `museum_walkthrough.gd` is the host. `DRAGON_PICTURE_HOTSPOT` has 10 uv points. `dragon_picture_uv` uses the plane z -1247.5 and the same face. `click_dragon` runs on left click, including the captured crosshair. The prompt at the pointer is `Click the dragon — Travel with the dragon`. `_use_world` still calls `enter_dragon`. `DRAGON_CLIPS` is `[6, 7, 8]`. `cave_video_review.gd` stores `dragon7.ogv`, `drgnflgt.ogv`, and `dragon8.ogv` at those indices. Longplay 31:26–31:40 stays the row's witness. The frames were not opened.

## Grade

DECODED for the twelve r15-only files, the host stores, the 600 and 420 radii, the single fall line, the `0xb7d5e` stage, the blocker writes, the serum refusal, unit size 300, and the dragon hotspot. HINTBOOK for lines 2253, 3075–3077, 3105–3107, 3119–3122, 3151–3157, 3163–3165, 3177–3178, 4256–4258, 4585–4589, 4594–4595, 4606–4608, and 4616–4631. BRADY for line 1556, printed page 42. LONGPLAY only as the dragon row's 31:26–31:40 witness. LIKELY only as the actor-90 health mapping and the item-26 catalog grade already in the sources. The frames were not opened.

No printed number replaces the door raise, the boulder bands, the 4-second clocks, the 250 drop, the reflection cap, the radii, or unit size 300. No simpler native build replaces these adapters. The dragon sentence has no numbered file. Row 0165's "until a script changes them" stays.

## Still open

The boulder trigger callee, opcode 18 mode on the stairs, the venom-sac opcode 3, the weight-word reader, the return caller, Belial dialogue and reflection, the `0xB7D5E` reader, native speech attenuation, the second Larkon potion, and the wall-34 click dispatch stay unentered. Item 26 stays unverified as a shaman-serum replacement.
