# AD01 L1_DC map gaps

Base maps-y 4a32849. The live scripts were searched. Map.png was not regenerated. No game patch.

## South-exit death

Already hosted by `cave_entrance_death.gd`.

Brady printed 147 says the south exit kills you. Control 135 is the cave-mouth plate at native (−1453, 3144), height 83. Opcode 2 sub 0x39 kills the player. Opcode 21 plays the form movie. The north exit stays region 1190. A marker was added. Test `cave_entrance_death_test.gd`. Godot was not run.

## Giant cockroach

Brady printed 147 names two giants. The host name is ROACH.

- The tunnel one is already hosted by `cave_wild_roach.gd`. Actor 0, definition 5, source health 100, at (177, 10282), height −250. A marker was added. Test `cave_wild_roach_state_test.gd` pins that position. Godot was not run.
- The Fire Pit sentence stays open. The pit cover stays the immolation marker at (−187, 14830). Population actor 44, definition 4, source health 10, stands at (−155, 14685), height −265. That is the nest definition. No second high-health ROACH sits on the pit. No patch.

`markers.json` had 35 rows. It now has 37.
