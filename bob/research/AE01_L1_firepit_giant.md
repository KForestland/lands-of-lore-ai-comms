# AE01 L1 Fire Pit cockroach

Base maps-y 4a32849. Godot was not run. Map.png was not regenerated. The placement patch was not applied.

All 57 L1 actors were read from `scripts/lol2/native_scripts/L1_DC.json`. Definition is byte 32. Health is the u16 at bytes 30–31. `tools/prepare_cave_roach_extra_media.py` asserts actor 23 byte 32 is 5.

Two actors are definition 5, health 100, name ROACH. Actor 0 is the tunnel roach at (177, 10282), height −250, already hosted by `cave_wild_roach.gd`. Actor 23 is the entrance roach at (−1900, 5627), height 4.

The Fire Pit cover stays controls 92 and 93 at (−187, 14830). The only roach in that neighborhood is actor 44 at (−155, 14685), height −265. Byte 32 is 0x04. Health is 10. The placement hex starts `65ff5d39`. `cave_roach_population_source.json` stores that position and health 10. `cave_roach_population_state.gd` `audio_actors()` sets definition 4 on every population row, which matches the native byte. `initial()` keeps actor 44 at that position. Actor 54 at (−264, 15435) is definition 1, the guard. Actors 36 and 37 are definition 6, name WORM.

Brady PDF page 65, printed 64, names one sofa-sized cockroach in the pit. PDF page 147, printed 146, names another Giant Cockroach in the Fire Pit. The hintbook fire-room sentence stays on the crate swarm at height −215. Prima has no separate Fire Pit coordinate in the reference folder. No longplay coordinate was found. No second definition-5 record sits in the pit. No new actor was added.

The marker is actor 44. The unapplied test is `cave_firepit_roach_state_test`, order 862. It asserts the source row and definition 4. `cave_roach_population_state_test.gd` already keeps actor 44 unchanged on the crate-room contact and does not assert this coordinate.

Patch: `grok_research/patches/AE01_firepit_roach/`. Apply-checked on a throwaway of maps-y 4a32849. Not applied.
