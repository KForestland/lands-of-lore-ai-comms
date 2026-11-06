# AE03 L5 Shalla

Base maps-y 4a32849. Godot was not run. Map.png was not regenerated. The placement patch was not applied.

Actor 20 stays Dawn. `hive_dawn20_population_source.json` stores definition 3, name Dawn, position (−3063, −1659, −6333), which is native (−3063, 6333), height −1659. The L5 actor-definition list is HIVEW, EXEC, WORM, DAWNL4, and B_HUMAN. Shalla is not one of those names.

The prop-template table (38-byte names, count 63) has no Shalla. Template 34 is Girl's Bones. Prop 236 of that template sits at (−1161, 8279), height −235. That prop is the child's remains in Brady printed 75. It was not marked as Shalla.

The assembly-name table is 30 bytes, count 65, ending at metadata +0x14. Index 6 is the name Shalla. Static-assembly placements are geometry +0x18, count 157, stride 33, template byte 32. One placement uses template 6: index 75, native (−1133, 8885), height −235, heading 7281, flags word 0x5402. Bit 0x1000 is set, so the collision export skips it. The same 33 bytes are control 75 in `L5_HC.json`. The placement hex is `93fbb522711c15ff0254e3030a0b7f000000000001000000000000002400020006`.

Control 75's records point at groups 5808, 5872, 5892, 5912, and 5932. Group 5808 contains opcode 9, opcode 20, opcode 8, opcode 18, opcode 2, and opcode 16. Those groups were not replayed. Local 25 `Shalla_cries` is still unread. The village-gate journal line is an L4 note, not this coordinate.

Brady printed 75 is the Shalla walkthrough. Brady printed 154 point 8 is the map point. The marker is control 75. Actor 20 was not moved.

The unapplied host is `hive_shalla_state.gd`. It records the placement and does not spawn her. Order 864. A pending DEVIATIONS row says the cry and the groups stay unrun.

Patch: `grok_research/patches/AE03_shalla/`. Apply-checked on a throwaway of maps-y 4a32849. Not applied.
