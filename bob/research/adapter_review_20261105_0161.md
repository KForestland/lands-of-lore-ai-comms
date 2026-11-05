# R2 adapter review, rows 0161–0176, 2026-11-05

No Godot was run. No opcode callee was entered. LOLG.DAT was not opened. The longplay was not opened. Newest owner file is still `TRIAGE_20261104.md`. r15 is `f6a5aa4`, act3-story is `d9e3aaf`, and r12y is `56812f9`. The board tail is the lead's Kimi K13d receipt for J04. That receipt is not a new commit and not an Astra question. J04 stays Kimi's note.

`adapter_review_20261104.md` slices 5 and 6 already opened these rows as table text. This pass reads the named hosts and the printed sentences. That file stays as it is.

These sixteen deviation files match r12y byte for byte. `native_script_host.gd`, `dark_halls.gd`, `cave_roach_population.gd`, `cave_old_orc.gd`, `creature_sprite_library.gd`, and `jungle_dino_sprite.gdshader` also match r12y. `act2_progression.gd`, `region_blockers.gd`, and `dragon_level.gd` differ. The host lines below are the r15 text. Counts the rows give stay the rows. This pass did not recount them.

## 0161 Rix fanfix

The load-time patch changes trailer byte 4882703 from 208 to 207 so group 14234 can select predicate 207. The archive stays unchanged. Groups 14102 and 14234 still open on opcode 2 arm `0x26`. The opcode 16 writer of `+0x25` stays LIKELY.

DECODED. `RECORD_PATCHES` for L7_DH names adapter `rix_fanfix_208_207`, file offset 4882701, byte 2, from 208 to 207. The patch runs on the loaded record. Row 0171 stages the entered stores of arm `0x26` and leaves the arm LIKELY. The opcode 16 command was not entered.

BRADY lines 3415–3424, printed page 85, say Rixx is possessed, that the blind spell lets him recover and leave, and that killing him yields the staff. Those sentences stay separate. They print no 208 and no 207. The fanfix stays the row.

## 0162 progression binder

`act2_progression.gd` loads the native host, fires region entry once per region change, fires a movable's kind-4 use on E, and logs the host's commits. Opcode 2 arm `0x1C` writes globals `0x223C8` and `0x223CC`. The node reads them as level and arrival selector.

DECODED. `enter_region` fires event 2 on `region:N` when the region changes. The use path uses reach 120, facing dot 0.7, and `arg_c` 0. `_on_global` stores `0x223C8` as the level and `0x223CC` as the selector, then changes to the staged scene. Setup supplies global `0x223D6` as 0 and also supplies `0x223D4` as 0. The row's 72 and 105 readings, and the L14 body `020100001c30`, stay the row. Those exit bodies were not opened. The byte-5 split stays the port's reading.

HINTBOOK line 3631 says to enter the Dracoid Ruins through the pit. BRADY line 1013 says the same ruins are reached through a hole. HINTBOOK line 289 titles "Birthing Chamber". BRADY lines 1075–1077 print "Birthing Chambers". Those names stay separate. No printed sentence names 72, 105, or byte 5.

## 0163 opcode 197

Arms 0–5 and 8–9 stage the region-record bits. Arms 6 and 7 use `opcode197_region_record`. Arm 10 uses `opcode197_list_mark`. Arms above 10 store nothing.

DECODED. `_op_one_nine_seven` matches those arms. Above 10 returns before a store. The two adapter names are in the host table. `0x64CD4` and `0x66664` were not entered. The row's opcode 198 write of local 11 stays the row. That command was not entered.

The follow-up the row names is row 0165. The binder calls `set_region_blocked` on each committed bit `0x1C` bit 0.

Books print no such arm. The list table stays unheld.

## 0164 preview seed

A preview start of L19_BC seeds local 52 with 0. A native level change leaves the local open. The value 0 is not a proven initial state.

DECODED. `PREVIEW_SEEDS` is `{"L19_BC": {"e58": {52: 0}}}`. Setup applies it only when `arrived_by_level_change` is not true. The file comment names L20 group 7704 opcode 199 as a framed writer and still calls that writer LIKELY. Opcode 199 was not entered.

Books print no local 52. The seed stays a preview adapter.

## 0165 live blocker toggle

Version 2 of the blocker producer keeps the static set and adds the opcode-197 regions. The binder builds those edges from the data bit and rebuilds them when arms 0–5 change bit 0. The wall spans floor-64 through ceiling+1024.

DECODED. `region_blockers.gd` uses footroom 64 and `HEADROOM` 1024. `enable_dynamic` and `set_region_blocked` are the calls the binder makes. The L8 pack's `dynamic_initial` is true for 3277 and 3278 and false for 3455, 3456, and 3457. `0xB7D4D` was not entered.

Books print no such height. The span stays the port adapter.

## 0166 five previews

The note covers L9, L12, L14, L17, and L20. Selector 0 is the preview choice. L9's pack start is (3607, -12, -8471) with source heading 24003. The preview yaw is 0. The panorama is `cavebk.pcx` with vertical origin -100. L17 has no decoded DEFAULT panorama. Absent-neighbour walls stay omitted. The other four notes use the linear heading adapter and the floor+32 height.

DECODED for the L9 pose and the sky. The L9 pack's `start` is `[3607, -12, -8471]` and arrival 0 carries heading 24003. `jungle_review.gd` places the player on `data.start`. `dragon_level.gd` then sets yaw 0, and converts a heading only when a level-change selector is supplied. `dragon_sky/environment.json` stores vertical origin -100 and the `cavebk.pcx` path. `map_sky/L17_HC` is absent. L12_CM, L14_HT, L17_HC, and L20_BB still set `map_blockers_enabled` false.

The L9 sentence that blockers stay disabled does not stay on r15. r12y leaves `region_blockers_enabled` false. r15 sets it true. The sentence that these maps have no progression scripts does not stay. Each of the five areas has a native script file, and the live hosts attach `act2_progression.gd`.

Books print no selector 0 and no origin -100. The omitted neighbours stay omitted.

## 0167 fruit garden

The 24 bed floors that use material 96 draw with grass material 97. The `prop_114` plants draw the last frame of the growth sprite. Opcode 14 growth stays untraced. Longplay 81:30 stays the row's witness.

DECODED. `GARDEN_BED_REGIONS` holds 24 region ids. `static_face_material` returns `97__front` for soil `96__front` on those regions. The prop loop uses `animations[key].frames[-1]` for `prop_114`. The frame was not opened.

HINTBOOK line 2362 names a garden outside the Monastery. That sentence prints no material 97. The grass swap stays the adapter.

## 0168 shade ghost

Views with flags `0x18` draw as a grey intensity ramp. The tint is 0.62, 0.80, 1.0. Alpha is intensity times 0.85. Longplay frame f_00934 stays the row's witness.

DECODED. `GHOST_FLAGS` is `0x18`. `present` sets the shader `ghost` flag from that test. The shader uses tint `vec4(0.62, 0.80, 1.0, 0.85)` and multiplies the byte by that alpha over 255. The frame was not opened.

BRADY lines 3440–3441 say a ghost in a bedroom attacks. That sentence prints no `0x18` and no tint. The tint stays the port's.

## 0169 roach lift

Roaches whose origin sits under the floor are lifted onto it. The row names roaches 50 and 51, native height 9, and surfaces 7.6 and 1.5 above those spots. The other roaches stay at the source height.

DECODED. `_snap_to_floor` casts a ray from 24 above the body to 4 below it and lifts the body when the hit is above the origin. The test file `tests/cave_roach_floor_test.gd` is present and was not run.

HINTBOOK lines 2035–2037 and 2047–2048 say to beware the giant cockroaches and to fight them with the mace. BRADY line 2420 names one large cockroach. Those sentences print no height 9. The lift stays the row.

## 0170 old orc movie

Control 136, `orc-diee.vqa`, is an indexed billboard. The producer quantises frames to the Cave palette. The quad is the template size 120 by 90.

DECODED. `prepare_cave_old_orc.py` asserts template bytes `[120, 0, 90]` and writes `dimensions` from those bytes. `cave_old_orc.gd` sizes the quad from `source.dimensions` and uses the indexed sprite shader. The native blit was not entered.

HINTBOOK lines 2041–2045 print "old ore" in the chamber and say he dies before he leads Luther to the gift. Brady's searched text prints no "old orc". The nearest-colour quantisation stays the port's.

## 0171 opcode 2 arms 0x26 and 0x27

The arms stage the entered stores on ref `0x22574`. The `0x151DAE` path stays unentered. The arm stays LIKELY. The name "conversation lock" is not in the bytes.

DECODED. `_op_two_lock` sets and clears the bits the row names and calls the staged reset. `0xD0138` and `0x151DAE` were not entered.

Books print no such bit. The unentered path stays open.

## 0172 opcode 2 arm 5

The arm stores the command's kind and word at the `+0xAD` fields. A nonzero byte 5 sets bit 0 of `+0x228` and runs the reset. A zero byte 5 clears the bit. The kind switch stays unentered.

DECODED. `_op_two_object_ad` writes `object_0xad_kind`, `object_0xad_index`, and that bit. `0x5FBC8` and `0x136594` were not entered.

Books print no such field. The arm stays LIKELY.

## 0173 opcode 2 counters

Arms `0x0C` and `0x0B` add byte 5 times 100 into the hosted sums when global `0x223D4` is 0. The clamp and the `0x12415C` compare stay unmodelled.

DECODED. `_op_two_counter` adds `byte5 * 100` into `dword_0x15d_added` or `dword_0x159_added` when the staged global is 0. An unknown global refuses. `0x12415C` was not entered. The binder supplies `0x223D4` as 0.

Books print no such sum. The arm stays LIKELY.

## 0174 opcode 2 arm 57

The arm sets bit 0 of byte `+0x16` when `0x223D4` is 0. The three calls stay unentered. The fish-death links still wait on the region event matcher.

DECODED. `_op_two_arm57` stages that bit and returns before the three calls. `0xB3B04`, `0xB3AC4`, and `0xD8D48` were not entered.

Books print no such bit. The calls stay open.

## 0175 opcode 13 actor

Slots 6 and 10, and a byte 4 above `0x16`, store 0 at word `+0x7C`. Slot 6 sets bit 0 of `+0xB5`. Slot 10 clears bits 2 and 3. An unknown `+0xA8` is taken as not `0x0F`. Slots 7 and `0x0D` are in the host. The other slots stay refused.

DECODED. `_op_thirteen_actor` returns with no store when `+0xA8` is `0x0F`. The adapter gate is the unknown case. Slots 7 and `0x0D` stage the bit the function names. An index outside 0, 6, 7, 10, `0x0D`, and above `0x16` returns unentered. The gate byte stays unread.

Books print no such slot. The stores stay the row's PROVEN logic behind that gate.

## 0176 opcode 7 control

Indexes 0 and 7 stage bits on `<control>:records`. Indexes 1–6, 8, and 9 stay unentered. Above 9 returns with no store. The slot lookup stays unentered.

DECODED. The control arm returns the unentered line for those middle indexes, returns empty above 9, and ORs bit 1 or bit 2 when the adapter is on. The comment names a `+0x36 == 0xFFFF` leave. The function body does not read that word. `0x5F878` was not entered.

Books print no such record. What the records drive stays unhosted.

## Grade

HINTBOOK for the Dracoid Ruins pit (3631), the Birthing Chamber title (289), the cockroaches (2035), and the dying speaker (2041). BRADY for Rixx on printed page 85 (3415), the ruins hole (1013), the Birthing Chambers (1075), the bedroom ghost (3440), and the large cockroach (2420). DECODED for the sixteen-file match, the fanfix patch, the binder calls, the opcode-197 arms, the preview seed, the L8 dynamic bits, the L9 pack start, the garden swap, the ghost flag, the roach ray, the orc template size, and the six opcode adapter names. Arms the rows mark LIKELY stay LIKELY. Refused arms stay refused.

No printed number replaces 208, 207, 72, 105, 52, 97, `0x18`, or 120 by 90.

## Still open

The opcode 16 writer of `+0x25`. The `0x151DAE` path. The opcode 198 write of local 11. Opcode 199 as the local-52 writer. `0xB7D4D`. The opcode 14 garden growth. The native ghost blit and the native movie blit. The counter compare at `0x12415C`. Arm 57's three calls. The control word `+0x36` and the record effect. The L9 blocker flag on r15, which this row's disabled sentence no longer describes.
