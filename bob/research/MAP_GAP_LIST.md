# MAP GAP LIST

Open owner map, texture, clipping, and collision rows from `playtest_feedback_20261023`. Source is `TRIAGE_20261103.md` sections D and E, plus the later rows the 2026-11-04 triage left open. One row each. r14 was not re-tested and no Godot was run. The Nov 4 triage of the r14 playtest did not mark the Nov 3 D/E rows fixed.

F10 map Y is native Y with the sign flipped (`MAPS/README.md`). A containing-quad hit is a same-sign cross test after a bbox reject. A miss means that sample is not inside a quad. It does not mean there is no nearby face. Floor and ceiling are the signed words at region record +20 and +22. Grades on the region numbers are DECODED. The owner sentences are the reports. No frame was opened. `map.png` was not regenerated.

## Open rows

| area | report | F10 | native | what is wrong | native face |
| --- | --- | --- | --- | --- | --- |
| L1 Cave | 17-03-39 | (532, −12371) | (532, 12371) | clipped through the wall; boxes cannot be moved to the next floor | region 1081, floor −215, ceiling −43, bbox (474, 12315)–(597, 12403). One quad. Control 121 sits at (564, 12367) height −215. This is the known crate hole. |
| L3 Museum | 17-14-40/52 | (1107, −830) | (1107, 830) | gates have the wrong colour; no textures | region 1057, floor 0, ceiling 120, bbox (1062, 644)–(1194, 902). One quad. |
| L4 Jungle | 17-16-55 | (−627, −5177) | (−627, 5177) | the chopped tree is still missing its top | region 1714, floor 0, ceiling 255, bbox (−797, 5054)–(−476, 5248). One quad. |
| L4 Jungle | 17-26-29 | (−3022, 475) | (−3022, −475) | owner asks what the brick box in the distance is | region 2122, floor 0, ceiling 127, bbox (−3081.4, −579.2)–(−2871, −258). One quad. The object was not named. |
| L4 Jungle | 23-04-55 | (5563, −3922) | (5563, 3922) | bridge sequence worked; some textures missing. Triage: textures to the presentation backlog | region 4399, floor −114, ceiling 13, bbox (5468.5, 3898)–(5598, 4003). One quad. The volume pose native (5564, 3817) is the next region, 4398, same floor and ceiling, bbox (5468, 3542)–(5619, 3946). |
| L5 Hive | 17-41-10 | (−2066, −7611) | (−2066, 7611) | texture jumping on a flat roof | two quads. Region 265, floor −235, ceiling −107, bbox (−2112, 7536)–(−1984, 7696). Region 269, floor −57, ceiling 12, bbox (−2112, 7596)–(−2048, 7616). Stacked floors. |
| L5 Hive | 17-42-38 / 43-05 / 43-17 | x −3507..−3689, y −7394..−7143 | x −3689..−3507, y 7143..7394 | clipping walls | sample (−3507, 7268): no containing quad. Sample (−3689, 7143): region 751, floor −1011, ceiling −639, bbox (−3730, 7136)–(−3658, 7215). |
| L5 Hive | 17-27-36 / 17-29-05 | none | none | the gas does not flow and is not transparent; the green stuff glitches | no coordinate. Region not looked up. |
| L4 Jungle | 17-55-53 / 17-56-12 | none | none | texture error; a bright texture in the sky | no coordinate. Region not looked up. |
| L14 Temple | 18-01-10/36/44 | x 2625..2884, y −2698..−3375 | x 2625..2884, y 2698..3375 | textures all wrong; geometry wrong | sample (2750, 3000): no containing quad. I00 already counted that window: 66 regions on floor 0, 16 on floor −80, 8 on floor −100. The lead's region-visibility pass is on act3-story and was uncommitted at board 2026-11-05T00:31Z. This pass did not re-test it. |
| L8 Darker Jungle | 23-20-29 | (−1076, −2621) | (−1076, 2621) | the ladder does not work. Triage: L8-CACHE-LADDER, P2, Brady printed 175 point 7 | region 678, floor −10, ceiling 390, bbox (−1110, 2486)–(−970, 2764). One quad. The climb is I26. |
| L8 Darker Jungle | 23-23-53 | (5063, 1888) | (5063, −1888) | knock the tree down to bridge the chasm. Triage: L8-TREE-BRIDGE, P2, Brady step 51 | region 3206, floor 0, ceiling 200, bbox (4914, −2012)–(5121, −1852.1). One quad. The knock-over is I27. |

## Left out

Nov 4 rows the triage marks FIXED are not map gaps: Bacatta volume (23-01-56), bridge volume (23-04-16), drowning (23-05-28, also db5efe5), Bacatta leaving after the scene (23-06-02), and the quiet-voice pass (1c33ac0). Those fixes are named on act3-story. This pass did not check whether r14 contains them.

23-25-07, "can't continue: Dracoid quest", is I24. It is not a face.

Section B of the Nov 3 triage is mechanics. The teleporter clip at 18-10-50, F10 (−310, −2304), native (−310, 2304), is already I00: Nice Door movables 88/89/90 and the stacked floor-190 shells. It was not scanned again. The hive elevator that starts at the bottom (17-41-36) is the known lift hole, not a D/E face.
