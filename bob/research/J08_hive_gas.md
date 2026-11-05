# J08 L5 gas cloud and the green floor shapes

No Godot was run. `L5_HC.MIX` sha256 prefix `a1979e60`.

## The gas

Owner 17-27-36, report `report_2026-11-03T17-27-36_1003704274`. The camera is Godot (1196, −30.5, −3926.6), native (1196, 3926.6), inside region 57. Floor face 167 is material `21` (`hive_review/material_21.png`), the lava cracks. That is the floor, not the cloud.

The cloud in front of the camera is scenery record 133, template 55, material `prop_66`. The scenery row names it `Smoke pit`. Name-at-index stays LIKELY. Position (1220, −30, −3878), region 53, about 54 units from the camera. The quad is left −48, right 49, bottom 0, top 95. Frame flag is 32. There are 15 frames, `hive_jungle_scenery/L5_HC_prop_66_0.png` through `L5_HC_prop_66_14.png`. Frame 0 and frame 7 differ (mean absolute change about 10). Eighty-three placements share this material.

`hive_jungle_scenery.gd` assigns frame 0 and has no playback. `frame_seconds` in the scenery source is null. The material is alpha scissor at 0.5. The PNG alpha is only 0 or 255 (58% clear, 42% opaque, no partial pixels), so the body of the cloud is solid.

The original cloud is see-through. Longplay `f_00489` shows a soft red mass with the cave showing through it, over the same red-cracked floor. That frame is not pinned to region 53. HINTBOOK lines 2581–2586 call these vents of gas and say the gas itself is not the hazard. BRADY printed page 74 (PDF page 75, lines 2883–2888) describes the red-cracked floors.

## The green shapes

Owner 17-29-05, report `report_2026-11-03T17-29-05_1093342559`. The camera is Godot (−1096.6, −203, −7578), native (−1096.6, 7578). That point is inside region 188 and region 189. Floor face 546 (region 188) has no material, height −235. Floor face 550 (region 189) is material `21`, height −235, about 19 units from the camera. The screenshot shows neon green jagged shapes on that floor, with a bright centre.

No colour PNG under `hive_jungle_scenery`, `hive_props`, or `hive_review` has those green pixels. The smoke pits near this camera are still `prop_66` (records 161, 162, 163). HINTBOOK 2582–2585 and BRADY printed page 74 lines 2886–2887 call the green floor marks poisonous pools. The indexed surface shaders write the palette index into red and green, with blue held at 0. That path was not matched to a face at this camera.

## Still open

A native frame rate for `prop_66`. Which mesh draws the neon green at region 189.
