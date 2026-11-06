# AJ02 Fire Pit giant

Base is the AJ01 tree, still unapplied on stack-ah01 a04c73a. Patch `grok_research/patches/AJ02_firepit_giant.diff`.

cave_roach_population.gd marks source actor 44 as the Fire Pit giant. The body stays SourceRoach44 at (-155, -265, -14685), health 10, definition 4, capsule radius 6 and height 12. The population sprite stays visible. No added actor and no save change. Brady printed 64/147 names a sofa-sized roach. That size stays unread as a mesh scale.

Test `cave_firepit_giant_test` prints `PASS: Fire Pit giant roach 44 is SourceRoach44 definition 4 at (-155, -265, -14685)`. Registry order 868.

The Cave earned chain stays unchanged. The tests that prove it are `cave_roach_floor_test` (still searches SourceRoach*), `cave_firepit_roach_state_test`, and `l12_exit_cave_earned_test`.
