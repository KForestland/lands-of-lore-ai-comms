# R2 adapter review, rows 0145–0160, 2026-11-05

No Godot was run. No opcode callee was entered. LOLG.DAT was not opened. The longplay was not opened. Newest owner file is still `TRIAGE_20261104.md`. r15 is `f6a5aa4`, act3-story is `d9e3aaf`, and r12y is `56812f9`. The idle line still names r12y.

`adapter_review_20261104.md` slices 4 and 5 already opened these rows as table text. This pass reads the named hosts and the printed sentences. That file stays as it is.

These sixteen deviation files match r12y byte for byte. `prop_billboards.gd`, `native_script_host.gd`, `act2_maps.json`, `movie_table.json`, `movie_players.json`, and `dawn_projectile_world.gd` also match r12y. `act2_map.gd`, `darker_jungle.gd`, `jungle_review.gd`, and `original_game_gate.gd` differ. The host lines below are the r15 text. Face counts stay the rows. This pass did not recount them.

## 0145 floorless floors

The row keeps 44 selector-255 floors as collision-only faces and sets `draw_floorless` false. The fill borrows the nearest textured floor. Solid boxes and bit0 blockers attach on the live scene.

DECODED. `jungle_walkthrough.gd` sets `draw_floorless` false and `fill_untextured_edges` true. `darker_jungle.gd` still names the 44 floorless floors and attaches the L8 solid boxes and the L8 blockers in `_ready`.

Books print no 44. The collision-only floors stay the row.

## 0146 props

The row draws 1765 prop rows as fixed-Y billboards, first frame only, with frame flags `0x40` and `0x80`. The helper adds no collision. Native blocking stays UNKNOWN. No L8 frame rate is proven.

DECODED. `prop_billboards.gd` batches one MultiMesh per material, box, and flip, uses `BILLBOARD_FIXED_Y`, and flips UVs from flags `0x40` and `0x80`. It adds no collision body.

Books print no 1765 and no such flag. The still first frame stays the row.

## 0147 panorama

The night panorama is `backgrnd.pcx`, 1280 by 300, vertical origin 42. The Cave sky shader draws it.

DECODED. `darker_jungle_sky/environment.json` stores vertical origin 42, width 1280, and height 300. `prepare_jungle_sky.py` names that origin for L8_SJ. `all_maps_sky.gdshader` uses the origin.

Row 0147's unshaded sentence does not stay. Row 0186 draws the night shade, and `darker_jungle.gd` leaves `night_enabled` true.

HINTBOOK lines 2074–2076 tell the player to take the shining path to the southern continent. BRADY lines 1010–1011 call the next jungle more dangerous than the Huline Jungle. Those sentences print no origin and no pixel size. The Cave projection stays the adapter.

## 0148 preview button

The gate offers "Preview: Act 2 start" whenever the darker-jungle pack is staged. `--l8-preview` starts that scene at once. The Act 1 chain still reaches L8 through the departure.

DECODED. `original_game_gate.gd` adds that button when `arrival_assets_ready` returns, with no edition test around the button. The `--l8-preview` argument calls the same preview start. The comment names `act_one_departure` as the Classic chain. The button was not clicked.

Books print no such button. The test label stays the row.

## 0149 generic host

`act2_map.gd` draws a pack at the Jungle standard: source walls drawn, floorless floors as collision, the shared billboards, the area panorama, solid boxes, and bit0 blockers.

DECODED. `map_blockers_enabled` defaults true, and `_ready` copies it onto `region_blockers_enabled` before the attach. L10_DC, L13_RC, L16_CA, and L19_BC leave that default. L12_CM, L14_HT, L17_HC, and L20_BB set the export false. Row 0166 already records those four previews as disabled pending walk evidence.

Row 0149's no-progression sentence does not stay. Row 0162 attaches `act2_progression.gd` when the level's scripts are staged. The header comment still says there are no progression scripts.

Books print no pack path. The shared draw recipe stays.

## 0150 Dracoid cemetery

The gate label is "Preview: Dracoid Cemetary (L10_DC)". The pack starts at selector 2, position -542, 856, heading 24758. Yaw is minus the heading times TAU over 65536. The destination byte stays undecoded. Longplay times 137:10 and 137:40 stay the pack's witness.

DECODED. `act2_maps.json` keeps that label. The L10 pack's `start_selector` is 2, `start` is `[-542, 32, -856]`, and `start_heading_units` is 24758. `act2_map.gd` applies the linear yaw. The witness string still says the destination byte is undecoded. G93 was not entered. The video was not opened.

HINTBOOK line 189 titles the chapter "Dracoid Cemetery". BRADY line 1018 prints "The Dracoid Cemetery". BRADY line 4383 prints "Cemetary" once. The hintbook title and that Brady line stay two sentences. The button keeps the export's Cemetary. No printed sentence names selector 2.

## 0151 Ruloi

The label is "Preview: L13_RC (Ruloi caverns)". The pack starts at selector 0, -3344, -6564, heading 28089. The longplay time about 202:30 stays the pack's witness.

DECODED. `act2_maps.json` and the L13 pack keep selector 0, start `[-3344, 32, 6564]`, and heading 28089. `prepare_jungle_sky.py` gives L13_RC vertical origin 0 and names the L16_CA image path.

HINTBOOK line 226 titles "The Citadel of the Ruloi". Brady's text prints no "Ruloi". The button's "Ruloi caverns" stays the longplay witness. The video was not opened.

## 0152 City of the Ancients

The label is "Preview: City of the Ancients (L16_CA)". The row's test start is selector 3. The panorama origin is 100.

Row 0152's selector 3 does not stay. Row 0182 moves the preview to selector 1 (-3860, 1341, heading 1, region 137). The live L16 pack's `start_selector` is 1, `start` is `[-3860, 32, -1341]`, and `start_heading_units` is 1. The same witness is on r12y.

DECODED for the label and the sky. `act2_maps.json` keeps the City label. `prepare_jungle_sky.py` stores vertical origin 100 for L16_CA.

HINTBOOK line 257 and BRADY lines 340–341 print "City of the Ancients". The button stays a test start. The destination byte stays undecoded in the row.

## 0153 Belial's Chamber

The label is "Preview: Belial's Chamber (L19_BC)". The pack starts at selector 1, 84, -305, heading 49152. No panorama pack is staged.

DECODED. `act2_maps.json` keeps that label. The L19 pack's `start_selector` is 1, `start` is `[84, 22, 305]`, and `start_heading_units` is 49152. `prepare_jungle_sky.py` has no L19_BC entry, and `map_sky/L19_BC` is absent. The authored sky remains the `jungle_review.gd` fallback.

BRADY lines 1068–1070 print "Belial's Chambers". HINTBOOK lines 283–284 print Belial's Laboratory and Belial's Summoning Room. Those names stay two sentences. The button keeps the export's Chamber. The destination byte stays undecoded in the pack witness.

## 0154 source walls

Kind `source_wall` is drawn and left out of the movement shell. Dark Halls can keep those faces solid.

DECODED. `jungle_review.gd` skips movement collision when the kind is `source_wall` and `source_wall_kind_collides` is false. The default is false. `dark_halls.gd` sets that flag true. The test named in the row was not run.

BRADY line 4376 says the player can pass through some walls in the Catacombs. That sentence prints no wall-record count. The drawn-only rule stays the row.

## 0155 projectile walls

Source walls also build `ProjectileWalls` on layer `1 << 10` with mask 0. Movement queries omit that layer. The bolt host is pending.

DECODED. `jungle_review.gd` uses `PROJECTILE_WALL_LAYER` `1 << 10`, names the body `ProjectileWalls`, and sets its mask to 0. `dawn_projectile_world.gd` defaults the query mask to 3. `jungle_dawn.gd` and `hive_dawn.gd` call it with that default. `tests/projectile_walls_test.gd` is present and was not run.

HINTBOOK lines 2514–2515 say a staff shoots plasma bolts. BRADY lines 1239–1240 say a staff emits plasma spheres. BRADY lines 3206–3207 say a statue fires a plasma bolt. Those sentences print no wall layer. Stopping every drawn wall stays the port's rule. The host stays unbuilt.

## 0156 opcode 21

Byte 4 indexes an 85-name table. The host emits `movie_request`. Nineteen Act 1 names bind to a player or to none. Play through `0xCF3C0` stays LIKELY.

DECODED for the table file. `movie_table.json` count is 85 and the format string is `%s.vqa`. The loader appends each entry's name. `movie_players.json` holds 19 names, and nine are `none`: e029e, e030e, e031e, fishdeth, hut-fire, and the four dialogue clips. A negative index, or an index above the table size, returns with no request. An index equal to the size stages an empty name. `0xCF3C0` was not entered. LOLG.DAT was not opened.

Books print no 85 and no `.vqa` name. The play stays LIKELY.

## 0157 opcode 8

Arms 0, 1, 2, 3, and 10 stage player-record fields. Arms 4 through 8 stage the pointer stores. Arms 9 and above 10 are refused. Play meaning stays UNKNOWN.

DECODED. The host names `opcode8_player` and `opcode8_gates`. Arms above 10 return the `0xB4390` refusal. Arm 9 returns no arm. With the gate adapter on, the unknown bits are taken as passing. `0xB43EC` was not entered.

Books print no such store. The play meaning stays UNKNOWN.

## 0158 opcode 6

Arms 3 through 6 store command byte 5 on the 42-byte record. Arms 0 through 2 stage the start, the list move, and the restart bit. Arms 7 through `0xC` are refused. Above `0xC` stores nothing on the record. Play meaning stays UNKNOWN.

DECODED. The host names `opcode6_gates` and `opcode6_record` and returns the no-effect line for arms 7 through `0xC`. Above `0xC` returns before a record store. `0xB3EC8` was not entered.

Books print no such record. The play meaning stays UNKNOWN.

## 0159 opcode 14

Arms 3 and 4 list and unlist the selected kind-2 record. A nonzero command byte 5 stores a word the host can draw only when bit `0x20` of byte 4 is set. Kind-2 meaning stays UNKNOWN.

DECODED. The host names `opcode14_timer`. Arm 3 sets `listed` to 1. Arm 4 sets `listed` to 0. The other word store is the constant UNKNOWN. `0x12415C` and `0x223A8` were not entered.

Books print no such timer. The kind-2 meaning stays UNKNOWN.

## 0160 opcode 9

Arm 2 clears the player fields the row names. Arm `0x15` enqueues the kind-6 event, and the host fires it after the group commits, at most 8 deep. The native queue timing stays unmodelled.

DECODED. The host names `opcode9_release` and `opcode9_enqueue`. `ENQUEUE_DEPTH_LIMIT` is 8. The nested fire writes `enqueued_results`. `0x9EFA8`, `0xADDE0`, and `0x26E6C` were not entered.

Books print no such clear. Both arms stay LIKELY.

## Grade

HINTBOOK for the southern continent (2074), the Cemetery title (189), the Citadel of the Ruloi (226), the City of the Ancients (257), and the staff's plasma bolts (2514). BRADY for the Savage Jungle (1010), the Dracoid Cemetery (1018), the one Cemetary spelling (4383), the City of the Ancients (340), Belial's Chambers (1068), the Catacombs walls (4376), and the plasma sentences (1239, 3206). DECODED for the sixteen-file match, the preview button, the four start packs, the sky origins, the source-wall rule, the projectile body, and the five opcode adapter names. The opcode play meanings stay the rows' LIKELY or UNKNOWN. Refused arms stay refused.

No printed number replaces 44, 1765, 42, 85, or layer `1 << 10`.

## Still open

The L8 prop frame rate and native prop blocking. The level-change destination byte. The projectile host that would add layer `1 << 10` to a bolt mask. The opcode-21 play loop. The play meaning of opcodes 8, 6, and 14. The native queue timing for opcode 9. Rows 0162, 0166, 0182, and 0186 already own the later host edits named above.
