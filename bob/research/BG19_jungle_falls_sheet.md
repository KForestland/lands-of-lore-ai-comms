# BG19 Jungle falls sheet

Owner r17 16-53-49 at Jungle (-4540, -1659), camera Godot (-4540.02, 36.76, -1659.71), yaw 1.353, pitch -0.111. The note was "no point and click". The shot is a flat triangle of RGB 134, 134, 154 across the lower view, with the waterfall picture above it and the jungle bank on the right.

DECODED. That color is texel (0, 0) of Jungle material 808. The r17 script `jungle_water_skirts.gd` built a draw-only sheet and skirts for every water region and set every vertex UV to (0, 0), so the whole triangle sampled that one texel. The sheet sits on the falls pool in front of source wall 72 (the waterfall picture, region 2694). It is not a hotspot, and a click on it had nothing to do.

BG06 already dropped those sheets. The only added water mesh left is the region 2559 sheet, and its UVs are world position divided by 64. The native floor of this pool keeps the authored material 808 UVs. Stood at the owner pose: the lower view shows more than one texel of that texture, source wall 72 is still the waterfall picture, and no WaterSkirt node is in the tree. No new mesh.
