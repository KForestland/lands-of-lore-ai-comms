# R2 adapter review, rows 0193–0206, 2026-11-05

No Godot was run. No opcode callee was entered. LOLG.DAT was not opened. The longplay was not opened. Newest owner file by mtime in `playtest_feedback_20261023` is still `TRIAGE_20261104.md`. Copies under `ai_comms_public/bob/playtests/` share those bytes and a later copy time. They are not a new report. r15 is `f6a5aa4`, act3-story is `d9e3aaf`, and r12y is `56812f9`.

Fifteen deviation files match r12y byte for byte. `0206-row-2026-11-02-hive-flute-floor.md` is DIFFER. `native_script_host.gd`, `liquid_drowning.gd`, `river_drowning_state.gd`, `river_region_query.gd`, `act2_sector_light.gd`, `l8_night.gd`, `area_world_items_state.gd`, `hive_flute_floor.gd`, `verify_act2_temple_door.py`, and `verify_act2_predicate_vm.py` match r12y. `act2_progression.gd`, `area_world_items.gd`, `region_blockers.gd`, `act2_map.gd`, `hive_elevator.gd`, and `prepare_act_one_item_defenses.py` differ. The sentences cited below are the r15 text. Counts the rows give stay the rows.

`adapter_review_20261104.md` slice 6 and slice 3, and `adapter_review_20261102.md` for both 0206 files, stay as they are.

## 0193 opcode 210 arm 9

Byte 4 above `0xB` stores nothing. Arm 9 stages `((byte 5 << 15) - byte 5) >> 8` at both `0x26d1e` and `0x26d1c`. The dword test that would skip the second word was not read.

DECODED. `_op_two_one_zero` returns before a store when the arm is above `0x0B` and refuses arms other than 9. With `opcode210_arm9` on, both words are written. `0x65B37` stays the row's entered arm and was not entered again. The witness `d20000000900` stays word 0. `HOST_ADAPTERS_OFF` for L8 is empty, so the adapter stays on.

Books print no such word. The staged pair stays the adapter. The readers stay unentered.

## 0194 opcode 1 modes 0 and 2

Mode 0 and mode 2 take the same travel-word store as mode 1. The continuation stays unmodelled.

DECODED. `_travel_word` stores `(angle * byte 4) / 100` when `opcode1_other_modes` is on and the mode is not the rotary mode. `0xE3924`, `0xB3B04`, and `0xB3AC4` were not entered. The L13 counts, 35 targets and 51 commands, stay the row. Survival of word `+0x4E` past slot `+0x18` stays LIKELY.

Books print no travel word. One store stays the adapter. No second sample was added.

## 0195 opcode 2 arm 0x3C

Every native branch returns 1 and stores nothing. The host still runs that path with the adapter off. The two zero stores are the adapter. The kind-4 mode-3 match stays the proven matcher.

DECODED. Arm `0x3C` returns with no store when the adapter is off, when byte 5 is not 0, or when bit `0x10` of `+0x228` is clear. An unknown bit is not 0, so the host writes `dword_0x1a2` 0 and, when global `0x223D4` is 0, `byte_0x199` 0. `0x80064`, `0xD6B20`, `0xD6D2C`, and `0xADC84` were not entered. Kind-4 mode 3 matches `arg_object_identity` to the record dword. The hosts still supply that identity. The 151 further L8 commands stay the row. Return of 1 stays the no-store path.

Books print no arm `0x3C` and no wave rate. The unread gates stay the adapter.

## 0196 world items

Seventeen live rows are hosted: Museum row 0, Dark Halls rows 4, 5, and 28, and Savage Jungle rows 10–21 and 28. E takes the aimed sprite.

DECODED. `area_world_items_state.gd` lists those seventeen identities at the native points. `area_world_items.gd` uses reach 96, aim 0.97, and an 80-unit floor settle. The r15 file adds a twin check so an Act 2 copy of the same placement counts as taken. That check does not replace the E pickup. Rows 25, 26, 29, and 30, and the Cave and Hive flag rows, stay out. `prepare_act_one_item_defenses.py` still pins Dark Halls Gaunt strike and Orc shield. The file differs by four later Act 2 identities. Those pins stay the adapter.

HINTBOOK line 5003 names a pile of lamplight eggs behind later doors. Line 1563 names Gauntlets of Might, not Gaunt strike. Those sentences print no reach and no row id. They were not merged onto this pickup. The E adapter stays.

## 0197 museum portal clearance

Portal corners are chamfered by the body radius plus 1. The human capsule is 30 wide. A centre may stand in the cut triangle.

DECODED. `region_blockers.gd` recesses a corner where two walls of one blocked region meet different passable regions. Pillars and walls between different blocked regions keep the corner. `player_form_body.gd` radii are 15, 23, and 8. The inside test uses floor minus 8 as height slack, not a new arch. The r15 file also clamps L8 region 2417. That clamp is outside this chamfer. The Museum test still walks the 24-unit opening at native y -1094. The row's 88 and 93 corners stay the row. The cut-triangle leak stays.

Books print no 24-unit opening. The chamfer stays the adapter.

## 0198 drowning per form

A Lizard is under when its feet are below the surface. A Human or Beast is under when the head top is. The measured limit is 15 s. The row's Cave clock sentence still says 12 s.

DECODED. `liquid_drowning.gd` uses feet at origin minus 32 and heads at 46 and 69. `river_region_query.gd` uses the same heads on plane -295. `river_drowning_state.gd` sets `LIMIT` to 15. The bank surface, the texture class, the lizard-any-water reading, the movie gate, and that limit stay the five adapters. Jungle 810, Savage Jungle 40, and Museum 19 stay the row. `act2_map` is still untouched.

HINTBOOK lines 2225–2229. Luther can drown in the jungle streams and the large river. The giant fish eats him there. The lines print no seconds. Lines 4865–4868. The city canal is deep and Luther can drown. The upper water is shallow. Those lines print no surface height. The canal stays unhosted.

BRADY lines 2754–2755, printed page 71. Wade shallow streams. Drown if you go in over your head. That sentence prints neither 46 nor 15 seconds nor the bank surface. Lines 5898–5900, printed page 136. The blood hurts, and the player must move fast before the lizard drowns. That liquid stays outside this water class. The two book pairs stay unmerged. No book number replaces 15 s.

## 0199 connected arrivals

Six arrival seeds are invented port inputs. L9 reads counters 300 and 120 at 60 Hz. That clock does not enter the native kind-2 walk.

DECODED. `act2_progression.gd` writes local 13 = 1, local 22 = 1, local 0 = 10, second-array 52 = 0 or 1, and control 82 byte `+0x25` = 2. The same six writes are in r12y. The file differs elsewhere. `advance_exit_timers` divides the record word by 60 and fires event 2 on L9 prop 104 only. Reach 120 and facing 0.7 stay the binder. A separate preview seed writes L19 cell 52 as 0 and names opcode 199. That opcode was not entered. The longplay times in the row stay the row. The frames were not opened.

Books print no local 13 and no 60 Hz. The six seeds stay invented. The 60 Hz reading stays this file's clock.

## 0200 sector-light heading

The heading table has a date, an area, a change, evidence, and a kind. It has no data row.

DECODED. No host is named. No book sentence is named. Nothing here replaces 0201–0204.

## 0201 L10 sector light

L10 faces and props use that area's own shade-table RGB rows. Per-pixel indexed shading stays unreproduced.

DECODED. `act2_sector_light.gd` loads `sector_shades/L10_DC.json` into a 64-by-1 texture and multiplies through `l8_night.gd`. A face without a sector takes the floor nearest its centre. `act2_map.gd` turns `sector_light_enabled` on for L10, L13, L16, and L19. The map file differs for other attachments. The shade ratios were not remeasured. The shader's 0.5 stays the exposure floor.

Books print no shade row. The RGB average stays the adapter.

## 0202 L13 sector light

L13 uses the same shader and its own shade table. The floor assignment is the same adapter.

DECODED. The area list includes `L13_RC`, and the loader reads `sector_shades/L13_RC.json`. Per-pixel indexed shading stays unreproduced. Placements were not remeasured.

Books print no L13 ratio. The area's own rows stay the adapter.

## 0203 L16 sector light

L16 uses the same shader and its own shade table.

DECODED. The loader reads `sector_shades/L16_CA.json`. Per-pixel indexed shading stays unreproduced. Placements were not remeasured.

Books print no L16 ratio. The area's own rows stay the adapter.

## 0204 L19 sector light

L19 uses the same shader and its own shade table.

DECODED. The loader reads `sector_shades/L19_BC.json`. Per-pixel indexed shading stays unreproduced. Placements were not remeasured.

Books print no L19 ratio. The area's own rows stay the adapter.

## 0205 hive flute pit lip

`0205-row-2026-11-01-hive-flute-pit-lip-summon.md` matches r12y. Standing in region 225 arms the flute summon. Native triggers 282 and 283 stay unchanged.

DECODED. `hive_elevator.gd` treats the pit-lip polygon at floor -235 as trigger 282. The r15 file differs at the control-aim gate. The lip lines match r12y. Region 225 stays the row.

HINTBOOK lines 2665–2666. The hall leads to an open pit. Use the flute to summon the elevator. The lines print no region 225. BRADY lines 3104–3105, printed page 78. Go to the edge of the pit and use the flute. The melody summons an elevator. That sentence was not merged with the hall sentence. It also prints no region. The lip arm stays the modern save-at-the-pit case.

## 0205 temple door contract

`0205-row-2026-11-01-temple-door-contract.md` matches r12y. The test pins the Dreamstone name, room flag 272, and local 13, then names prop 1198 group 11612. The full route is not hosted.

DECODED. `verify_act2_temple_door.py` checks those static names and the two command bytes. It does not run the original module. No arrival seed is applied. HINTBOOK lines 4578–4584 tell the player to insert the flute in the temple oil slot. That route was not added. Those lines were not copied onto the Hive floor.

The subsystem adapter stays. No printed flag 272 replaces it.

## 0206 quest-actor selector

`0206-row-2026-11-01-quest-actor-selector.md` matches r12y. Arm 4 reuses the spatial selector and clears word `+0x7C`. It is not installed as the gameplay route.

DECODED. `act2_quest_native_host.gd` copies byte 5 into an opcode-5 command and writes word `+0x7C` as 0. Unknown `+0xA8` still uses `opcode13_actor_a8`. `0xA642F` stays the row's call and was not entered. `verify_act2_predicate_vm.py` pins the dispatch bytes and 69 explicit executions. Books print no arm 4. The subsystem adapter stays. It has no printed behaviour sentence.

## 0206 hive flute floor

`0206-row-2026-11-02-hive-flute-floor.md` is DIFFER. The r12y sentence was: retrievability, so the flute still summons the lift and serves the Huline Temple slot, and the refusal texts, are port choices. The r15 sentence replaces that reason. It says the original flute disappears into the wall, and the owner prefers that the player keep it and take it back once.

DECODED. `hive_flute_floor.gd` matches r12y. The slide is still `+91` x and `+91` z over 1.5 s, with reach 110, and `retrievable` stays true. `retrieve` still takes the flute back and leaves the floor. The oil fire trap stays unhosted. No simpler number replaces the slide.

HINTBOOK lines 2684–2686. Slide the flute into the slot for safer footing. Lines 2799–2801. Place the iron flute in the slot. That trick slides a green tile floor. The same lines also name the fire trap. Those two actions stay unmerged. Neither prints 91 or 1.5. BRADY line 6864, printed page 160. Use the Flute to move a section of floor over the oil pool. Lines 7274–7275, printed page 170. Place the Flute in a receptacle, closing a floor over an open pool of oil. Lines 3248–3251, printed page 81. Place the magic flute in the silhouette. A panel closes over the floor. That page was not merged with 160 or 170. None of them prints the slide width.

## Grade

DECODED for the host stores, the seventeen item rows, the chamfer, the drowning limit, the six seeds, the four shade loaders, the pit lip, and both subsystem pins. LIKELY for the unread `0x26D2C` path and for word `+0x4E` past slot `+0x18`. HINTBOOK for lines 2225–2229, 2665–2666, 2684–2686, 2799–2801, 4578–4584, and 4865–4868. BRADY for lines 2754–2755, printed page 71; lines 3104–3105, printed page 78; lines 3248–3251, printed page 81; lines 5898–5900, printed page 136; line 6864, printed page 160; and lines 7274–7275, printed page 170. LONGPLAY only as the arrival times the 0199 row already prints. The frames were not opened.

No printed number replaces the opcode cells, the E reach, the chamfer, 15 s, the six seeds, the shade ratios, region 225, or the 1.5 s slide. The r12y retrievability sentence does not stay. The r15 owner-choice sentence replaces it. The take-back in the host stays.

## Still open

The opcode 210 readers, the opcode 1 motion calls, the arm-`0x3C` gates, `0x80064` and `0xD6D2C`, the kind-4 second argument, the world-item flag bits `0x8000` and `0x0400`, the native liquid level, per-pixel indexed shading, the arrival-local writers, opcode 199, the temple route, the quest-actor install, and the oil fire trap stay unentered.
