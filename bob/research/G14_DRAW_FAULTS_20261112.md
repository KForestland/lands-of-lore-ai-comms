# G-14a: faces drawn where they should not be (12 November 2026)

Playtest build in the triage: playtest/r19a `5930fd4`. Geometry read here is r19-work `25cac0f` (`assets/lol2/generated/maps/<area>/area.json` and `creature_nav/<area>.json`), the map that playtest was on. Each pose is `report.json` `render_camera` in that bundle. The walk is the game's: `scripts/lol2/act2_map.gd` portal areas and islands, `scripts/lol2/region_visibility.gd` opening overlap 24, near edge 160, clusters of 24. A potential-set bound applies only on the Temple. A face whose region has no cluster is always drawn. Once any opening reaches a room, the whole room mesh draws.

Portal areas today: L14_HT, L10_DC, L9_DR, L16_CA, L19_BC, L20_BB. Islands: L14_HT only. L12_CM and L13_RC have no portal drawing.

Room numbers below are the pack's `render_sector`. Grades of a cause are from this walk. This file does not change the game. Collision, the class-C behaviours, and lighting stay out. G-14b is the fix.

## Cause counts

| Cause | Count | Reports |
| --- | --- | --- |
| 1. The level has no portal drawing | 5 | the five L12_CM reports |
| 2. Temple island or potential-set leak | 3 | 06-23-17, 06-24-24, 06-29-47 |
| 3. Two faces in the same plane | 1 | 07-01-12 |
| 4. A wall with no neighbour | 1 | 06-25-52 |
| 5. Other | 3 | 06-51-31, 07-00-11, 07-10-13 |

13 reports. One cause each.

## Class A

Coordinates in the pose column are Godot x, z, height, from the triage (x, y, height).

| Report | Level | Pose | Player region | Face drawn wrongly | Its region / room | Cause |
| --- | --- | --- | --- | --- | --- | --- |
| 06-23-17 | L14_HT | 2759, -3395, h 51 | 21, room 0, floor 0 | ceiling 1632, y 80, 89 units out, up and to the right of center | region 819, room 28 | 2 |
| 06-24-24 | L14_HT | 3050, -3856, h 52 | 1056, room 38, floor 0 | floor 5063 is the face in the doorway and it is not drawn, so the hole is black | region 2577, room 128 | 2 |
| 06-25-52 | L14_HT | 2926, -3268, h 32 | 30, room 0, floor 0 | the black wedge is not a face. Wall 8226 is the left wall and has no neighbour | region 15, room 0 | 4 |
| 06-29-47 | L14_HT | 2318, -3649, h -48 | walk starts in 861, room 28, floor 0. Feet are in 3243, floor -80 | floor 1651, y 0, 280 units out | region 830, room 28 | 2 |
| 06-41-16 | L12_CM | 2443, -15730, h -918 | 2394, cluster 228, floor -950 | wall 7820, y -1190..-440, 195 units | region 3410, sector 227, cluster 95 | 1 |
| 06-41-39 | L12_CM | 2418, -15586, h -918 | 2403, cluster 228, floor -950 | wall 7819, y -1190..-440, 130 units | region 3409, sector 227, cluster 95 | 1 |
| 06-44-03 | L12_CM | 2409, -11886, h -1158 | 2804, cluster 119, floor -1190 | floor 363, y 80, 2003 units (the grey quad). The smaller brown quad was not matched | region 326, sector 50, cluster 33 | 1 |
| 06-45-18 | L12_CM | 1817, -15699, h -1149 | 3415, cluster 716, floor -1190 | wall 6932, y -950..-750, 813 units | region 2399, sector 162, cluster 228 | 1 |
| 06-46-15 | L12_CM | 2598, -15768, h -1149 | 3410, cluster 95, floor -1190 | floor 2949, y -950, 241 units | region 2394, sector 162, cluster 228 | 1 |
| 06-51-31 | L13_RC | -3928, 4172, h -4 | 0, cluster 0, floor -40 | source wall 3255, y -40..137, 89 units | region 479, sector 36, cluster -1 | 5 |
| 07-00-11 | L16_CA | -3684, 3118, h 32 | 2268, sector 30, cluster 34. Camera y 61 | source wall 17029, y 130..808, on the left of the view | region 298, sector 8, cluster 35 | 5 |
| 07-01-12 | L16_CA | 2101, 852, h 32 | 2317, sector 32, cluster 332. Camera y 61 | source wall 29065, same depth 171.6 as source wall 22606 | 29065 is region 10580, sector 372, cluster 1504. 22606 is region 4830, sector 83, cluster 462 | 3 |
| 07-10-13 | L16_CA | -4072, 4566, h 32 | 389, sector 9, cluster 50. Camera y 42 | source wall 17127, y 130..600, 850 units, the house wall on the center ray | region 366, sector 9, cluster 53 | 5 |

### Temple

**06-23-17, cause 2.** Room 0's potential set has 26 rooms and includes room 28. The opening walk reached room 28, so the whole of that room draws, including parts outside the doorway. Ceiling 1632 of region 819 sits at y 80, 89 units from the camera, above the view center. That is the slab in the air. The center ray's first drawn face is a different piece of the same room: floor 1660, region 836, y 0, 281 units out, which is the floor ahead. Ceiling 6501 of room 174 is closer on the center ray and is correctly hidden.

**06-24-24, cause 2.** The center ray hits only floor 5063 of region 2577, room 128, at 289 units, and that face is not drawn. Room 128 is in room 38's potential set (15 rooms). No region the walk reached shares an edge with 2577, so the opening never enters it. The doorway is the empty background. The face that should fill it is 5063.

**06-25-52, cause 4.** The black wedge sits between the striped stone wall on the left and the carved-wood room on the right. The center ray hits wall 8226, region 15, room 0, material 181, y 0..80, 124 units, and that face is drawn. Material 181 is the stone with two dark-red stripes, which is the left wall, not the black. That wall's edge has no neighbouring region. The sample to its right jumps from same-room walls to wall 9542 of room 28 at 800 units. The gap between them is empty. Cause 4 is that missing neighbour. Room 28 being drawn at all is the same potential leak as 06-23-17, and it is not what makes the wedge black.

**06-29-47, cause 2.** The feet at height -48 stand in region 3243, floor -80. The camera is closer to region 861, floor 0, room 28, and the walk starts there, so room 28 is drawn across the lower hall. Floor 1651, region 830, y 0, is the stone plane overhead. Two walls of the same region, 9520 and 9518, region 817, also land on one plane at 467 units. They belong to the leaked room. The report is counted once, as cause 2.

### Claw Mountains

All five are cause 1. L12_CM is not in `PORTAL_VISIBILITY_AREAS`. On each pose the walk from the player's region does not reach the face, so a portal pass would hide it, and today the face is drawn anyway.

06-41-16 and 06-41-39 are one stacked pair. The player stands in cluster 228, floor -950, and sees the wall of cluster 95, floor -1190 (faces 7820 and 7819, regions 3410 and 3409). 06-46-15 is the same pair from the other side: the player is in region 3410 and sees floor 2949 of region 2394 at y -950. The owner's words on 06-46-15 ask for a tunnel instead of the two maps cutting through each other. The draw fault is still cause 1. A portal pass from this camera does not reach region 2394, so the floor would hide. Whether the two floors should stay one path is the tunnel decision, and that is G-14b.

06-44-03's center ray hits floor 363 at 2003 units and nothing closer. That is the grey quad in the sky. A second floor, face 365, sits 24 units off that plane and is not the brown quad. The brown quad was not matched.

06-45-18's center face is wall 6932, region 2399, cluster 228, 813 units out, not the player's cluster 716.

### Citadel

**06-51-31, cause 5.** Source wall 3255, region 479, sector 36, material 1, y -40..137, 89 units, is the dark wall in the cave mouth. Region 479 has an empty nav polygon, so it is in no cluster. A face with no cluster is always drawn. L13_RC also has no portal drawing, but switching that on would not hide this face. The two movable faces just behind it, 5223 and 5222, have no region either.

### City of the Ancients

L16_CA already uses 24-region clusters. None of these three is cause 1 or cause 2.

**07-00-11, cause 5.** The picture is a stone front with a mountain vista in the left part of that front, then sky and a spire. The player's region is 2268, sector 30, cluster 34. The left-hand tall wall is source wall 17029, region 298, sector 8, cluster 35, material 951, y 130..808, about 500 units out. The walk reached region 298, so the cluster pass draws that other sector across the building. The center ray's first face is a different reached wall, 19558, region 2130, sector 28, 764 units out. The sky to the right of center is a real miss, not a hidden face.

**07-01-12, cause 3.** Two source walls are both drawn at distance 171.6. Face 29065, region 10580, sector 372, cluster 1504, was not entered; it draws because another region of that cluster was. Face 22606, region 4830, sector 83, cluster 462, was entered. That pair is the flicker. Movable faces 29074 and 29075, material 1287, sit just behind them and have no region, so they always draw.

**07-10-13, cause 5.** The houses in the picture are walls of the player's own sector 9. The center face is source wall 17127, region 366, sector 9, cluster 53, material 1050, y 130..600, 850 units, and the walk reached it. The near floor is region 390, the player's cluster 50. Nothing closer is a foreign room. The mixed marble, wood, and green panels are the materials of those reached walls. The repeated line "The lift carries Luther to the upper floor..." is a caption on the screenshot, not a face.

## Class C

These are the owner's words from the triage, source the owner, 12 November 2026. They are not rows in `census.json`. Position is census space: x, height, z, with z equal to the triage's y. A census index is named only where a row is actually at the pose and a script names that object. The others stay UNKNOWN. Nothing here was implemented.

| Report | Area | x | height | z | Owner's words | on_main_chain | Census | Grade |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 06-25-13 | L14_HT | 2993 | 31 | -5231 | the flor should erupt here and spiders should spawn out | unknown | none at this pose | UNKNOWN |
| 06-47-40 | L12_CM | 3063 | -1198 | -18712 | ruloi entrencae do not work | unknown | none at this pose | UNKNOWN |
| 06-52-18 | L13_RC | -4947 | -867 | 1707 | this is a teleporter | unknown | none at this pose | UNKNOWN |
| 06-58-25 | L13_RC | -4576 | -1008 | 1765 | this open the valut | unknown | none at this pose | UNKNOWN |
| 07-01-57 | L16_CA | 2198 | 32 | -869 | this gass\passma\thing shoul go to the 3 doors and blow them up | unknown | none at this pose | UNKNOWN |
| 07-02-41 | L16_CA | 15946 | 132 | 3923 | need to puch this box in the slott | unknown | none at this pose | UNKNOWN |
| 07-04-37 | L16_CA | -4260 | 82 | 1533 | ivory chip in the hands here i think | unknown | none at this pose | UNKNOWN |
| 07-04-57 | L16_CA | -3896 | 2 | 1399 | pussle box | unknown | none at this pose | UNKNOWN |
| 07-12-10 | L16_CA | -9499 | 32 | 12902 | ivoriy chips inn here | yes | control 176 | LIKELY |
| 07-19-17 | L17_HC | -4953 | 32 | 6455 | here everting moves | unknown | none at this pose | UNKNOWN |
| 07-22-31 | L19_BC | 882 | -98 | -1494 | the next map loding is incorect | unknown | none at this pose | UNKNOWN |
| 07-23-11 | L19_BC | 958 | -93 | -2453 | the door is blocked | unknown | none at this pose | UNKNOWN |
| 07-24-27 | L19_BC | 1973 | -93 | -888 | this is the blod alter that drains | unknown | none at this pose | UNKNOWN |

Source of every row: the owner, 12 November 2026.

Control 176 is the ivory pedestal at (-9505, 30, 12936). The pose is 34 units away in the horizontal and the height matches the pedestal. `l16_sw_chips.gd` says controls 173-176 are the ivory pedestals. The census already marks that row `on_main_chain` yes. The join is LIKELY. The missing chip behaviour was not tried.

Near rows that were not joined:

- The spider-burrow script pins Godot (3061, 0, -5374), reach 64. This pose is about 158 away, and control 80 is 110 above the feet. Not this pose.
- The Ruloi-entrance pose is about 900 from L12 control 74, the citadel exit. Not this pose.
- Both Citadel poses are about 600 from L13 control 102, the elevator in `l13_elevator.gd`. The census has no L13 control 104. Not these poses.
- The puzzle-box pose is 58 from L16 control 107. `l16_centre_tower.gd` says controls 71, 107, and 108 are not the box. Not joined.
- The blood-altar pose is 34 from L19 actor 39. `l19_dawn_curse.gd` names actor 39 as the Dawn curse actor, not an altar. Not joined.
- L17 has no census row at (-4953, 6455). The one L17 row in the census is a door far from this pose.

## Class E

Report 06-28-49, L14_HT, pose 2227, -3913, height -48. The owner's words: "i do not know this, im not sure this in the main game." The screenshot is a carved-wood room, a wooden table, a blue-grey body on the table, and a blue stone wall on the right. Height -48 is a lower floor.

Both guides describe that room.

- Hintbook (`reference_hintbook/hintbook.txt`), Chapter Twelve. Lines 4418-4421: the tunnel leads to a flute in a coffin and the priest's corpse on a table. Lines 4455-4458: find the corpse on the table near the chokepoint, press the button on the pedestal to the right, and the dead guy moves to the conveyor. The bedroom with the red pillows is the next paragraph (line 4477), not this room. Grade HINTBOOK.
- Brady (`reference_hintbook/brady_guide.txt`). Printed 115 (PDF 116), under the lower halls: the Caretaker's body has been teleported down, and the button near the body moves it onto the conveyor. Printed 202 (PDF 203): "In the lower halls you will find the Caretaker's body on a table. Push the button to the right." Grade BRADY. Brady's name for the body is the Caretaker. The hintbook's names are the priest's corpse and the dead guy. The books do not say the body is blue.

Longplay. Frames `g_00276` through `g_00295` in `lol2_original_screens/longplay_frames_act2plus/` were opened. The clock is 6580+(N-1)*30 seconds, so that stretch is 4:07:10 through 4:16:40. They show cliff paths, stone halls, a fight, and then the city rising (`g_00294`, `g_00295`). None of them is this carved-wood room with a body on a table. Grade LONGPLAY NOT SEEN. `g_00275` was not opened this pass. An earlier note calls that frame the sun-trimmed door.

The room is in the retail guides. This longplay sample does not show it.
