# J09 L4 bright textures in the sky

No Godot was run. Jungle pack source sha256 prefix `517afe6d`. Geometry sha256 prefix `56435e56`.

## 17-56-12, the orange brick

Owner report `report_2026-11-03T17-56-12_2720210190`, text "brig texure in the sky". The camera is Godot (3890.4, −69.9, −3604.1), native (3890.4, 3604.1), eye height −59.9, yaw −0.830, pitch 0.883. That point is inside region 1897, floor −114, ceiling 99, flags 0x2004.

The rectangle in the sky is face 10239, region 4411, kind wall, material `5`. The quad is native (4007.0, 3730.0) to (3974.6, 3728.9), heights 104 to 127, about 32 by 23. It sits about 161 units from the camera. The texture is `jungle_review/material_5.png`, the orange brick in the shot.

The wall binding is region 4411 edge 2, code 2, wall record 4401, resource 5, raw `0500000080021000`. The record names resource 5. The exported image for that resource is the brick.

Region 4411 floor −74, ceiling 127, flags 0x2, neighbors [4409, 4412, 4408, None]. Edge 2 faces region 4408. Region 4408 floor −114, ceiling 104, flags 0x2004. Face 10239 is the lip of 4411 from 4408's ceiling 104 up to 127. From the lower room that lip is in the sky.

The band under it is face 10234, region 4408 edge 3, wall record 1919, resource 556, raw `2c02d2b0800b1000`, heights −114 to −74, `jungle_review/material_556.png`. Face 10233 on region 4408 has no material, heights 99 to 104. Region 4408 edge 2 and region 4407 edge 2 are `missing_record`.

The cliff beside the brick is resource 615 (`jungle_review/material_615.png`, foliage). Region 1897 edge 1 is record 4433 and edge 3 is record 4432, both resource 615. Region 4411 edge 3 is record 4402, resource 615. Face 6874 is that foliage wall, heights −74 to 127, and it is not the brick.

The only other high material-5 faces are 7532 through 7535, all on region 4770, native x about −2750 to −2028. They are far west of this camera.

## 17-55-53, the dark panel

Owner report `report_2026-11-03T17-55-53_2701152683`, text "texture error here". The camera is Godot (3438.0, 32.0, −4110.3), native (3438.0, 4110.3), eye height 42.0, yaw −2.128, pitch 0.287. That point is inside region 3785, floor 0, ceiling 127, flags 0.

The panel is face 9929, region 3787, kind wall, material `617`. The quad is native (3495, 4022) to (3597, 4137), heights 64 to 127, about 154 by 63, about 112 units from the camera. The texture is `jungle_review/material_617.png`, dark stone with pale veins. The binding is region 3787 edge 3, code 3, wall record 3057, resource 617, raw `6902000080031000`.

Region 3787 neighbors [3786, None, None, 3790], so edge 3 faces region 3790. Region 3790 floor 0, ceiling 64. The quad is the part of that edge above 3790's ceiling. The camera's own edge toward 3790 is region 3785 edge 2, unresolved `missing_record`, drawn as face 9927 with no material, heights 64 to 127, from (3597, 4137) to (3453, 4029). That opening is why the 617 lip is seen against the sky. The foliage walls on region 3787 are faces 6099 and 6100, resource 615, records 3059 and 3058, full height 0 to 127. They are the next edges, not this lip.

## Still open

No longplay frame was matched to either camera. The records name resources 5 and 617, and those exported images are what the shots show. Whether the original portal clip hides the lips above the lower ceilings was not read.
