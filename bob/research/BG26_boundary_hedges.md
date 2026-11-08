# BG26 boundary hedges

Owner r17 17-59-34 at (1842, 2499). The picture is the tall hedge on the left of the path.

Source wall 8693, material 276, is region 1389 edge 3, from 0 to 200. The region flags are 0x200. Bit0 is clear. The neighbours are 1388, 1398, 1390, and none. Edge 3 has no neighbour. The point (1780, 2400), just past the hedge, is in no region.

The port drew source walls for projectiles only. Movement stays on the region graph. A neighbour-less edge had nothing to stop the body, so the walk went through the hedge.

A source wall on a neighbour-less edge now collides. The collider is that drawn quad. A source wall on a linked edge stays open, including the other material 276 hedges. The ray through wall 6959, region 23 edge 2, misses the movement layer and still hits the projectile layer.

Grade DECODED for the empty neighbour and the empty ground past the hedge. The collision is the port's stand-in for a step the original mover cannot take.

PASS hedge walk: stood at (1842,2499), the boundary hedge stopped the walk, and the path beside it still walks. 7.48s, source_stable. Patch `patches/ACT3P2/BG26_boundary_hedges.patch`. Ledger 0338.
