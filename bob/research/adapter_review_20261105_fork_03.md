# R2 adapter review fork 03, 2026-11-05

No Godot was run. No opcode callee was entered. The idle line still names ~/opus_work/lol2_r12y at 56812f9. These rows were read in ~/opus_work/lol2_r15 at f6a5aa4. All eight deviation files match r12y byte for byte.

## 0040 museum

`0040-row-2026-10-23-museum.md` matches r12y and stays pending. `museum_mirror_route.gd` matches r12y. `museum_walkthrough.gd` differs on the dragon picture. The mirror functions are the same in both trees.

DECODED: the strip is rect (-4099, -1393, size 82 by 24). The host names it region 1419. A step into it travels. E uses that rect with forward dot above 0.7. `mirror_was_inside` starts true, so a load inside the strip waits for a leave and a fresh step. A move of 32 units or more also waits. The scene change is immediate.

The row says the mirror animation and the op18 pull are not replayed. That opcode stays unread. No motion is taken from it.

BRADY lines 2452–2454, printed page 65: step through the mirror and be teleported to the Southern Continent. BRADY lines 2706–2708, printed page 70: go through the Shining Path, or use the secret door behind the tapestry. HINTBOOK line 2073 tells Luther to take the shining path. HINTBOOK lines 2111–2114 leave on the dragon. Those stay separate sentences. Books print no region 1419.

The mouth travel stays the row. The unread pull stays open.

## 0041 museum

`0041-row-2026-10-23-museum.md` matches r12y and stays pending. `museum_ivory.gd` matches r12y. The hand retry in `museum_walkthrough.gd` is the same text in r12y.

DECODED: a full hand makes `offered()` fail. E then clears the hand and retries the plain pickups, and the feedback says the held item was put away. Aim accepts the chip sprite plus 4 degrees, and also the anchor reach test.

HINTBOOK line 2110: break the vases and pick up two ivory chips. BRADY lines 2575–2576, printed page 67: smash the vases. Some contain ivory chips. The next sentence says they give additional mana if equipped. That mana sentence stays separate. Books print no hand rule and no aim size.

The put-away retry stays the row. The smash lines are the printed reveal. Nothing printed replaces the hand retry.

## 0042 jungle

`0042-row-2026-10-23-jungle.md` matches r12y and stays pending. `jungle_walkthrough.gd` matches r12y. It sets one-sided walls on, floorless drawing off, `backdrop_edges` false, and edge fill on. `backdrop.gdshader` matches r12y and multiplies view-space position by 1.001. That shader attaches only while `backdrop_edges` is true. `jungle_review.gd` differs by a jump hook that still returns 200. The wall loop is the same.

DECODED: one-sided winding covers boundary walls, material 744, and source walls. Interior spans stay two-sided in that loop. The live Jungle leaves the panorama shader off.

The row still asks for panorama on unbound edges, floorless floors, and wall backs, and it leaves native per-portal clipping open, including the thin vine strip in report 44. Books print no such number. The live host has left the backdrop sentence. The edge fill is the build now running. Open: the unread portal walk, and report 44.

PROPOSE drop the jungle backdrop sentence | jungle_walkthrough backdrop_edges false | live Jungle uses the edge fill and leaves the 0.1 percent shader unattached.

## 0043 jungle

`0043-row-2026-10-24-jungle.md` matches r12y and stays pending. `jungle_walkthrough.gd` matches r12y and turns the fill on.

DECODED: `jungle.json` has 54 visible untextured outer walls and 57 zero-size ones before the interior spans. Region 589 has one such wall, first point x -783, the face the fill test calls edge 0. The UV is 2 texels per world unit across and one stretch over the height, taken from the nearest textured outer wall. The same function also fills floorless floors, clear material 469, and untextured step spans. The row says those stay unchanged.

The row cites longplay frames and gives no time. No frame was opened. The record-less edge renderer stays unread. Books print no 54 and no region 589.

The 54-wall fill stays the row. The wider fill is past this row. Open: the untraced record-less edge.

## 0044 hive

`0044-row-2026-10-24-hive.md` matches r12y and stays pending. `hive_rune_entry.gd`, `hive_rune_light.gd`, and `hive_rune_pit_source.json` match r12y. `player_starting_magic.gd` differs on level-3 Spark. The charge-1 brazier path is still there.

DECODED: 105 pit tiles, owner region 506, event 1 value 1. 104 are room 11, RUNES. Region 625 is the one room-10 RUNECL tile, and `enter_pit` skips it. A grounded arrival on a room-11 tile opens RUNES, stores return -3113, -6282, sets marker642 when the tile has it, and calls the Dawn20 link. E on the totem body opens RUNES. Q casts Spark, and an aimed brazier spends 1 mana. A fire crystal spends one charge, and `ignite()` debits no mana. That crystal use requires human form. Beast form cannot cast. No G binding lights this brazier. kind12 is the row's word. The pit file has no kind field.

The row says the native event1 condition and the crystal fire hit mask are not traced. Both stay unread. LONGPLAY 1:37:17–1:37:18 stays the row's witness.

HINTBOOK lines 2691–2698: the floor falls away, a spark spell lights the brazier, and you enter the pit. HINTBOOK lines 2802–2809: light the brazier, avoid the pit, then enter it. BRADY lines 3267–3269, printed page 81: a Spark Spell ignites the brazier, then click the ladder. BRADY lines 3276–3279, printed page 82: use wax on the engravings. BRADY lines 2151–2153, printed page 58: a Fire Crystal creates a fireball. HINTBOOK line 2108 is the museum gem's fire crystals. Those stay separate sentences. Books print no 104 and no pose.

The pit entry and the Spark light stay the row. The crystal stays the owner's extra. Brady's ladder stays Brady's sentence. Open: event1, the hit mask, and RUNECL.

## 0045 all areas

`0045-row-2026-10-24-all-areas.md` matches r12y and stays pending. `walk_feel.gd` matches r12y. F4 in `museum_interface.gd` toggles it. The saved key is `walk/modern_feel`, off when missing. `museum_interface.gd` differs on the magic button. The F4 block is the same in r12y.

DECODED: accelerate 0.12 s, stop 0.06 s, bob constants 0.9 and 1.5, step constants 1.9 and 2.6. Shift run at 144 uses 0.8 of that span, amplitude 1.38 and about 2.46 steps per second. The offset is `Camera3D.v_offset` only.

Cave, Museum, Jungle, Hive, and Dark Halls call this bob. Hive and Dark Halls inherit the Jungle mover. The Cave interface extends the Museum interface. Jump launch on the Museum and Jungle paths stays 200. The Cave jump stays 96.

LONGPLAY 22:07 Museum and 34:00 Jungle stay the row's witness that the horizon stays level. Books print no such number. Off is the simpler original feel. The opt-in stays the row. The camera node, the aim rays, and the collision body stay put, as the row says. Open: native easing, which the row already leaves unproven.

## 0046 museum jungle hive dark halls

`0046-row-2026-10-24-museum-jungle-hive-dark-halls.md` matches r12y and stays pending. `walk_feel.gd` matches r12y.

DECODED: walk 80 and run 144. The Cave reads them from `original_walk_review.gd`. The Museum reads them from `museum_review.gd`. Jungle, Hive, and Dark Halls read them from `jungle_review.gd`. No 120 walk speed remains in the scripts.

The row's earlier Museum-only walk and the 120 run stay the row's history. A running jump keeps the horizontal speed. Launch speed stays 200 on those paths. The row leaves jumps for later.

Books print no such number. Native speeds stay untraced, as the row says, and the row says the longplay cannot measure them reliably. The one pair stays the row. No printed speed is more faithful. A per-area speed split would be the older build the row replaced.

## 0047 jungle

`0047-row-2026-10-24-jungle.md` matches r12y and stays pending. `jungle_walkthrough.gd`, `jungle_bridge_break.gd`, `jungle_bridge_break_state.gd`, `jungle_bridge_break_source.json`, `source_control_contact.gd`, and `static_collision_L4_HJ.json` match r12y. `static_assemblies.gd` differs by L9 raised decks. The Jungle bridge boxes are the same.

DECODED: assemblies 213, 214, 210, and 212 are scripted solids. Each box has base -90 and height 90, so the top is 0. `add_scripted_solids` keeps them standing. Form 1 is Beast. Plank 210 value 9 admits Beast while the owner state is 0, and the host can set broken and show debris plus assembly 211. Values 10 on 212, 213, and 214 admit Human and Beast. The host plays those commands as sounds. The collision boxes stay after the mode change. The row names op20. Native op20 stays unread. No motion is taken from it.

LONGPLAY 50:05 stays the row's witness for human Luther crossing. HINTBOOK lines 2361–2367: the long wooden bridge to the Monastery collapses under the Beast. BRADY lines 2805–2809, printed page 72: the rickety bridge over the quicksand fails under a beast, and you may shove the plank back. BRADY lines 2799–2801, printed page 72: you can cross the bridge toward the Wild Ones. Those stay three sentences. Books print no assembly ids and no height 0.

The solid boxes stay. The row's never-break sentence is behind the Beast contact on plank 210. Open: native op20, and which book bridge this deck is.

PROPOSE mark the Beast break hosted | plank 210 value 9 form 1 | the never-break line is behind the contact, and the boxes stay solid.

## Receipts

- 0040 museum: 0040 matches r12y: walking into the region 1419 strip travels, E still works, a load inside waits for a fresh step, op18 stays unread, and Brady printed page 65 says step through the mirror.
- 0041 museum: 0041 matches r12y: E with an item in hand puts it away and takes a revealed ivory chip aimed on the sprite, Brady printed page 67 says smash the vases for chips, and the books print no hand rule.
- 0042 jungle: 0042 matches r12y: the live Jungle leaves the backdrop off and keeps one-sided boundary walls, the 0.1 percent shader stays unattached there, report 44 stays open, and the books print no such number.
- 0043 jungle: 0043 matches r12y: the geometry has 54 visible record-less outer walls including region 589, they take the nearest textured wall at 2 texels per unit, and the books print no such number.
- 0044 hive: 0044 matches r12y: 104 room-11 pit tiles under region 506 open RUNES when grounded, Q Spark lights the brazier, the fire crystal stays the owner's extra, RUNECL stays unhosted, and the books print no tile count.
- 0045 all areas: 0045 matches r12y: F4 modern bob stays off by default at the row's constants, Shift run reaches amplitude 1.38, the level-horizon witness stays the row, and the books print no such number.
- 0046 museum jungle hive dark halls: 0046 matches r12y: Cave, Museum, Jungle, Hive, and Dark Halls walk and run at 80 and 144, native speeds stay untraced, and the books print no such number.
- 0047 jungle: 0047 matches r12y: bridge assemblies 213, 214, 210, and 212 stay solid with tops at height 0, Beast contact on plank 210 can set the break, native op20 stays unread, and the books print no assembly numbers.
