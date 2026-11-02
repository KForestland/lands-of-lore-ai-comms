# PT-L9-WALLS card

Grade DECODED from r12x and r12y, same counts. No Godot. The wall-trap F10 has no position, so no region is bound to it.

## Why the Ruins walls have no collision

`dragon_level.gd` sets `region_blockers_enabled` false, and the attach of `region_blockers/L9_DR.json` is inside that flag. `include_collision_face` returns only floors and ceilings. `jungle_review.gd` also leaves kind `source_wall` out of movement collision unless `source_wall_kind_collides` is true. L9 never sets that flag. Drawn Ruins walls are source-wall faces, so they do not stop the player.

## Comparison

| area | host | bit0 pack attached | static blocked | static edges | other solid |
|---|---|---|---|---|---|
| Cave L1_DC | `cave_walkthrough.gd` flag true | yes | 6 | 12 | source walls stay non-solid |
| Museum L3_DH | `museum_walkthrough.gd` flag true | yes | 491 | 551 | open-regions 1422 |
| Hive L5_HC | `hive_review.gd` flag true | yes | 63 | 68 | source walls stay non-solid |
| Dark Halls L7_DH | `dark_halls_blockers_enabled` true | yes | 61 | 42 | `source_wall_kind_collides` true |
| Ruins L9_DR | `dragon_level.gd` flag false | no | 125 present, unused | 116 present, unused | floors and ceilings only |

L9 geometry has 6829 regions and 179 with word +0x1C bit 0. The pack's static set is those 179 minus the opcode-197 regions: 125 static, 116 edges. Opcode-197 regions: 79, with 243 dynamic edges. 54 of the 79 start with bit 0 (179 − 125). Open set is empty. The same tool, `tools/prepare_region_blockers.py`, built the Cave, Museum, Hive, and Dark Halls packs.

## What a builder makes solid

The movement solid is the existing bit0 pack, not a new material list. Turn the L9 flag on and attach `L9_DR`. Leave the 79 opcode-197 regions on the dynamic list so a script can open them. Baking all rendered source walls would copy the Dark Halls flag onto faces the Act 2 comment keeps non-solid (hedges and veils the player may cross).

Drawn wall census, `L9_DR/surface_coverage.json`: 14500 source-wall records, 12006 rendered (class 0: 3426, class 4: 4710, class 8: 3856, class 12: 14). Those faces stay the picture. They are not the bit0 set.
