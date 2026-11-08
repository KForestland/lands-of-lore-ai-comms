# BG28 Cave crates

Owner r17 16-23-39 at Cave map (549, -12225). "cant stack boxxes or move boxes."

Controls 94, 95, 96, 97, 112, 121 and 122 have no move opcode. The shove is the existing adapter. It used a radius of 8, which is the beast capsule. Human is 15 and lizard is 23. The solid crate stops the body outside that old reach, so a walk never started a shove.

The reach is now the current form radius plus the crate's horizontal corner and one unit of contact. The rest height uses the placed floor. That floor already includes the cave translation. The old constant -215 dropped a shoved crate out of the room on the first push.

A shove that overlaps another crate still snaps onto that crate's top.

Grade: adapter. Patch `grok_research/patches/ACT3P2/BG28_cave_crate_shove.patch` on r18-work `3b6a929`. Unapplied.

PASS crate: walked into crate 94, it moved, and it rests on crate 95. The old seven-crate unit test still passes.
