# BG25 village guard, first approach after the temple

Owner r17 18-06-16 at (554, -3929). The figure in front of the carved trunk is actor 113 (WILD) at (676, 0, -4541). Actor 22 (Daniel) at (522, -30, -4743) is group 6424 and is not spawned here.

`l8_journey.gd` `restore_world` links 113 when `temple_visited` becomes true. That is the same link as r17. Grade HINTBOOK for the temple-then-village order (deviation 0309). Grade DECODED for the placement.

The walk stands on the pose before the temple (he is absent), walks the fixture to the temple, then walks back once to the pose. No save and no second trip. He is present, his body is visible, and the sprite texture is set.

PASS guard: walked the temple, then once to (554,-3929), and actor 113 was in front of the tree. 44.51s, source_stable. Patch `patches/ACT3P2/BG25_village_guard.patch` is the test only.
