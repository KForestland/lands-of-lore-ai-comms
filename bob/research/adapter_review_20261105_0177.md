# R2 adapter review, rows 0177–0192, 2026-11-05

No Godot was run. No opcode callee was entered. LOLG.DAT was not opened. The longplay was not opened. Newest owner file is still `TRIAGE_20261104.md`. r15 is `f6a5aa4`, act3-story is `d9e3aaf`, and r12y is `56812f9`. The board tail is the lead's 19:56Z watch that this continue prompt was sent. That line is not a new commit and not an Astra question.

`adapter_review_20261104.md` slice 6 already opened these rows as table text. This pass reads the named hosts and the printed sentences. That file stays as it is.

These sixteen deviation files match r12y byte for byte. `native_script_host.gd`, `dark_halls.gd`, `l8_night.gd`, `prepare_map_portable.py`, `tests/l16_map_test.gd`, `prepare_region_blockers.py`, and `prepare_l8_night_shade.py` also match r12y. `cave_walkthrough.gd`, `museum_walkthrough.gd`, `hive_review.gd`, and `darker_jungle.gd` differ. The on-flags and the pitch constant below are the same sentences on both trees. The host lines are the r15 text. Counts the rows give stay the rows. This pass did not recount the command totals.

## 0177 opcode 15 effect request

Opcode 15 with byte 4 above `0x70` stores nothing. A lower form logs `effect_request` and does not play the effect.

DECODED. `_op_fifteen` returns before a store when the form is above `0x70`. Otherwise it appends an effect and emits `effect_request(form, ref, lookup)`. The play callees named by the row stay unentered. `0x5FBC8` stays unentered. A search of the gameplay scripts finds the signal and no form binding.

Books print no form `0x65` and no form `0x66`. The logged request stays the adapter.

## 0178 opcode 18 pending slot

A zero dword at `0xB7D5E` stores the command. A nonzero dword is left. The host takes the cell as empty at start.

DECODED. `_op_eighteen` reads `0xb7d5e` `command_file_offset` with default 0 and writes the command file offset only when that read is 0. Bit 5 of byte 10 returns before that store. `0xB2A54` and `0x65BB0` were not entered.

Books print no such cell. The empty start stays the adapter.

## 0179 opcode 19 effect record

The host logs the record fields and does not call vtable slot `+0x80`. Byte 9 of 1 or 2 is refused.

DECODED. `_op_nineteen` returns on byte 9 of 1 or 2 and names the unread percentage slots. Any other byte 9 emits `effect_record_request` with value `UNKNOWN`. Byte 9 of 0 uses byte 8. The vtable slot stays unentered.

Books print no such record. The log stays the adapter.

## 0180 opcode 208 cells

Byte 4 of 0 raises `0x26B4E` to byte 6 times 60 shifted 16, and raises `0x26B52` to byte 5, only when the stored values are lower. Byte 5 of 0 clears both. The host takes both as 0 at start.

DECODED. `_op_two_oh_eight` refuses a nonzero byte 4. The product and the two lower-than stores match the row. The default reads are 0. The cell readers stay unentered. The tar witness stays the row.

Books print no 60 and no cell. The start values stay the adapter.

## 0181 kind-9 one record

One hit enqueues at most one kind-9 record. A cleared byte +9 is mode 0 and admits nothing. Actors start with `+0x25` equal to 0.

DECODED. `fire_event` marks a later kind-9 record `not_reached` once one record is accepted. `_match_kind9` rejects mode 0. `reset_state` stores `byte_0x25` 0 on every actor. This pass did not re-fire door 57 or the Rix groups. Those effects stay the row.

This row is the correction. It is not an adapter. Books print no kind 9. The one-record rule stays.

## 0182 L16 selector 1

The preview start is arrival selector 1, source pair (-3860, 1341), heading 1, region 137, floor 0. The level change is L14 group 9210. Caller byte `0x14` stays untraced.

DECODED. `prepare_map_portable.py` sets `L16_CA` `start_selector` to 1 and names that group. `tests/l16_map_test.gd` pins `Vector3(-3860, 32, -1341)`, heading 1, and selector 1. The scene height is floor 0 plus 32, and the packed z is the negated source z. The test was not run. Caller byte `0x14` was not traced.

HINTBOOK line 257 titles "The City of the Ancients". BRADY line 341, printed page 10, says the Third Sphere begins with the City of the Ancients. Those sentences print no selector and no coordinate. Selector 1 stays the witnessed start. Selector 3 does not stay.

## 0183 opcode 2 arm 6 and two actor slots

Arm 6 counts a call on the object and stores nothing else. Opcode 13 slots 7 and `0x0D` join the proven stores behind the `+0xA8` gate.

DECODED. `_op_two_arm6` increments `opcode2_arm6_calls` and returns. `0x79310` was not entered. `_op_thirteen_actor` clears bit 0 of `+0xB5` on slot 7, sets bits 2 and 3 on slot `0x0D`, and writes word `+0x7C` as 0. An unknown `+0xA8` still uses `opcode13_actor_a8`. The Rix witnesses stay the row.

Books print no arm 6. The count stays the adapter.

## 0184 museum region 1422

Region 1422 is taken out of the static blocked set. Its opener stays UNKNOWN.

DECODED. The L3 pack lists `open_regions` as `[1422]`, 491 blocked regions, and 551 edges. Dynamic initial is true for 1477. Region 1422 is not in that dynamic map. The five arm-10 marks and the event-4 owners stay the row. The bit-0 drops were not entered. `opcode197_list_mark` remains the host write from row 0163. It does not by itself open the static set.

Books print no region 1422. The open list stays the adapter.

## 0185 Act 1 blockers on

Cave, Museum, Hive, and Dark Halls turn native bit-0 blockers on. Each host keeps its own flag. Dark Halls walls stay solid.

DECODED. `cave_walkthrough.gd`, `museum_walkthrough.gd`, and `hive_review.gd` set `region_blockers_enabled` true. `dark_halls.gd` sets `dark_halls_blockers_enabled` true and `source_wall_kind_collides` true. The packs match the row's static counts: Cave 6 regions and 12 edges, Museum 491 and 551, Hive 63 and 68, Dark Halls 61 and 42. Dynamic initial is true for Cave 10, 29, and 1143, true for Museum 1477, false for Hive 985, 986, and 987, and true for Dark Halls 30. The same three on-assignments are present on r12y. The whole Cave, Museum, and Hive files differ for other reasons.

Books print no such edge count. The on default stays. It is the live Act 1 on-row.

## 0186 L8 night shade

Every static face, prop billboard, and assembly is drawn through `l8_night.gd`. Colour is scaled by the shade-table row. The row's ratios stay 0.92, 0.44, 0.10, 0.07, and 0. Assemblies take the sector of the region they stand in. Longplay 110–111 minutes stays the row's witness.

DECODED. `darker_jungle.gd` sets `vertex_light_enabled` and builds night materials for static meshes and `DarkerProps`. `static_face_light` uses the face sector, else the region under the centre. `l8_night.gd` multiplies albedo by the shade-row texel. `shade_rows.json` holds 64 rows. The channel means are 0.92 at row 63, 0.4426 at row 52, 0.1029 at row 30, 0.0716 at row 16, and 0 at row 0. The row's rounded ratios stay. Per-pixel index remap stays unreproduced. The frame was not opened.

HINTBOOK line 2911 titles "The Savage Jungle". BRADY lines 1005–1011, printed page 27, say Luther reaches that jungle across the Bane River. Those sentences print no ratio and no pitch. The colour scale stays the adapter.

## 0187 pitch limit

Look-up stops at 0.656 rad. The same limit downward is an adapter.

DECODED. `darker_jungle.gd` sets `pitch_limit` to `PITCH_LIMIT` 0.656. The comment names 37.6 degrees from the panorama. The native look-down value stays untraced. Other hosts are outside this assignment.

Books print no 0.656. The upward clamp stays the row. The downward copy stays the adapter.

## 0188 opcode 1 other modes

A movable whose mode is not 6 stores the travel word. The motion calls stay unentered. Opcode 2 arm `0x24` sets two bits and calls nothing.

DECODED. `_travel_word` stores `(angle * byte 4) / 100` when `opcode1_other_modes` is on. `0xE3924`, `0xB3B04`, and `0xB3AC4` were not entered. Arm `0x24` sets bits `0x10` and `0x20` of `+0x228` and returns. Mode 6 stays the rotary path. The witnesses stay the row.

Books print no mode 1 and no travel word. The staged word stays the adapter.

## 0189 kind-2 timer

A kind-2 record matches when byte +5 bit 0 is clear. The native expiry walk stays unentered. The world side owns the clock.

DECODED. `_match_object` rejects a set bit 0 and matches a clear bit. The adapter comment leaves the count to the world side. `act2_progression.gd` `advance_exit_timers` fires event 2 on L9 prop 104 only, and it reads the count as a 60 Hz duration. That clock does not enter the native walk. The tick rate stays unentered.

Books print no count 120. The match stays the adapter.

## 0190 opcode 2 arm 0x18

The host clears dword `0x23348+0x90B`. The old pointer's callees stay unentered.

DECODED. Arm `0x18` writes `dword_0x90b` as 0 and returns. `0x95C24` and the six callees stay unentered. `HOST_ADAPTERS_OFF` exists. The L8 list is empty, so this adapter stays on. The witness stays the row.

Books print no such dword. The clear stays the adapter.

## 0191 opcode 3 item grant

When global `0x223D4` is 0, the host emits `item_request` and stores nothing. Slot `+0x6C` stays unentered.

DECODED. `_op_three_item` returns with no effect when that global is not 0. Otherwise it appends the identity and byte 8. The grant callees were not entered. The count 1086 stays the row. The L8 list in `HOST_ADAPTERS_OFF` is empty.

Books print no such identity. The request stays the adapter.

## 0192 opcode 12 room

Byte 4 below 46 emits `room_request` and stages bit 1 of `0x269C4`. The two gates stay unread.

DECODED. `_op_twelve` returns with no store at index 46 or above. A lower index emits the stem and archive and sets that bit. `room_stems.json` index 39 is `settle1_` and `SETTLE1.MIX`. The gates named by the row were not entered. The slot count 46 stays the row.

Books print no stem index. The request stays the adapter.

## Grade

DECODED for the host stores, the L16 selector, the four on-flags, the shade means, and the pitch constant. HINTBOOK for line 257 and line 2911. BRADY for line 341, printed page 10, and lines 1005–1011, printed page 27. LONGPLAY only as the row's 110–111 minute witness. The frames were not opened.

No printed number replaces the cells, the forms, the shade ratios, or 0.656. No simpler native build replaces these adapters. Selector 3 does not stay. The Act 1 off default does not stay.

## Still open

The play effects, the `0xB7D5E` reader, vtable `+0x80`, the opcode 208 readers, caller byte `0x14`, `0x79310`, the region-1422 list reader, per-pixel shading, the native look-down, the opcode 1 motion calls, the native kind-2 expiry walk, the old arm-`0x18` pointer, slot `+0x6C`, and the opcode 12 gates stay unentered.
