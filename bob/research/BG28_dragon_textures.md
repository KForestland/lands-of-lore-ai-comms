# BG28 Dragon Level textures

Owner r17 18-22-43. The capture is Dragon Level, not L12. Camera (-2962, 314, -7396), pitch -0.312, yaw 3.007. The scene node is DragonLevel.

The white floor in the shot is region 4853, face 9668, material 748, preset Floor27, scale 2, a 128 image. The UV matches `floor_uv` in `tools/lol2/map_surfaces.py` (max difference 0). The pack image matches `material_0748/mip_0_palette.png`. The pattern is the original white field with brown spots. The polygon is 140 by 23, so the shot sees a short slice of that tile.

The round shield is assembly face 30920, source index 297, 90 by 90, material 750. That image matches `material_0750/mip_0_palette.png`. Material 750 is an alpha cutout, so the square corners stay clear. UV on that quad is 0 to 1.

Props 1020, 1021 and 1022 sit beside the camera. The drawn boxes are left/right/bottom/top: 1020 is 14 by 10, and 1021 and 1022 are 9 by 14. The width and height fields are the texture pixels (187 by 111, 159 by 229). Those props do not fill the shot.

The floor under the player, region 4852 material 625, and the stair material 571 also match `floor_uv`. Materials 625, 821, 749 and 750 match their source mips.

Pitch 0.312 is under the 37.6 degree panorama limit. This shot is not the steep look.

Grade DECODED. No patch. The pictures and the UV are the source.
