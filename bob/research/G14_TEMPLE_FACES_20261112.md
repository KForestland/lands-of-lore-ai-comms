# Temple faces, 2026-11-12

Later Opus Temple legends append under a new heading in this file. One line per face. Grades are PROVEN, LIKELY, or UNKNOWN. A longplay line is marked LONGPLAY. Leave an earlier line as it stands.

Pack `DAT/L14_HT.MIX`, sha256 `c294f9ab142b55c36fff545a1293c419c42353fedefbfe8b77b9c38a2d9a0719`, geometry sha256 `f5831b7ef235be70489aee179112f5293b1e2067467077cbc0202f15565480b3`, 16185 faces in `assets/lol2/generated/maps/L14_HT/area.json`. A face number is that list index. A wall record is the archive index. These two use builder `0x114aa4` with `source_wall` true. `tools/lol2/map_source_walls.py` adds no synthetic face for a missing record. `vertical_offset` is the native byte at output `+0x31` and is not a second height. Regions 21 and 22 each have one ceiling face, so `island_sky_ceilings.gd` adds no sky polygon on them. The roofless set is the regions whose ceiling face the pack omits.

## 06-23-17

Legend `AI_COMMS/opus_lane/g14/faceid_06-23-17/`. Camera Godot (2758.62, 61.45, -3394.81) is inside region 21. Material 495 front is `aae3b5f537e69dbcf911.png`, the carved wood with a circular face. Material 473 front is `9a92798449ff90c8154c.png`.

- Face 8238, wall record 7478, region 21, room 0, material 495 front, plane x=2677, y 80..125, z -3485..-3360: PROVEN the original draws it, with ceiling 43 of region 21 (material 473 at y 125) meeting its top edge, the opening below y 80 into region 819 around it, ceiling 1632 of region 819 (material 473 at y 80, room 28) meeting its bottom edge, and wall 8229 (record 7469, region 17, material 181, y 0..125) meeting its north corner. Sky is not drawn on region 21. This room is not the roofless centre.
- Face 8239, wall record 7479, region 22, room 0, material 495 front, plane x=2677, y 80..125, z -3524..-3485: PROVEN the original draws it, with ceiling 45 of region 22 (material 473 at y 125) meeting its top edge, the opening below y 80 into region 837 around it, ceiling 1662 of region 837 (material 473 at y 80, room 28) meeting its bottom edge, and wall 8237 (record 7477, region 20, material 495, y 0..125) continuing the same wood on the south corner. Sky is not drawn on region 22. This room is not the roofless centre.
- Longplay: LONGPLAY this doorway is absent from g_00267, g_00268, and g_00275 through g_00278. g_00268 at 4:03:10 shows the same carved wood as a wall beside an opening. g_00267 at 4:02:40 is a pedestal under a hanging. g_00275 at 4:06:40 is the three-door room under a dark sky. g_00276 through g_00278 are the black ledge maze.

## Later legends
