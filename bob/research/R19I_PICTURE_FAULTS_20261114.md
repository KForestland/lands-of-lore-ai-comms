# r19i picture faults, 2026-11-14

Read from the owner's three screenshots and the r19i pack at 91044aa. No F10. No second Godot. Opus still had one Godot on lol2_door92, and the door 73 review is the next boot.

Screenshots: `Pictures/Screenshot from 2026-11-14 02-22-40.png`, `02-25-41.png`, `02-32-43.png`. The overlay on each shot is the pose.

## L13 magenta is material 96, the pink-plate texture

Both citadel shots use the same purple image. It is material 96, file `assets/lol2/generated/maps/L13_RC/1c19879f0b67eacde553.png`, 128 by 128, four colours: (166, 28, 170), (113, 8, 117), (215, 81, 219), (247, 134, 251). The file is present. L13 has 112 material files and none are missing. It is not the review debug colour `Color(1, 0, 0.8)`, and a face with no material key is drawn grey-green in `jungle_review.gd`, not this purple.

The faces are static-assembly template 10, child 12, the pink plates (`l13_pink_plates.gd`, placements static_55 through static_75 and the same child elsewhere). Nearest-filter magnification turns the four texels into blocks.

02-22-40, overlay L13 X -2998.7 Y 359.3 H -726. The camera stands on the pink stair. The nearest plate is static_73, centroid (-2981, -759, 350), then static_67 and static_66. Those are the ceiling slab and the floor block in the shot.

02-25-41, overlay L13 X -4314.8 Y -1463.4 H -1008. The faces within 250 of that stand are ordinary floors, material `414__front` (and one `418__front`), files present. The strip in the shot is the same four purple colours, and material 96 is the only purple texture on L13. The nearest plate at that height is static_72, centroid about (-3076, -1009, 290), about 2100 away, so the strip is those plates seen across the citadel, not a hole in the floor under the camera.

## L16 cut is the native skewed end of region 5997

02-32-43, overlay L16 X -2782.6 Y 14836.9 H 122. The camera is inside region 5997. Floor face 7916 and ceiling face 7917 are parallelograms, not axis-aligned quads. The long edges run about 60 in x and 240 to 270 in z. The short end is 30 by 15, from (-2775, 90, 14917) to (-2805, 90, 14932) on the floor. Wall face 23731 follows that same skew. Floor material `835__front`, wall and ceiling `1235__front`. Those files are present. L16 has 427 material files and none are missing.

Region 5997 neighbours are [null, 5994, 5996, null]. The city past the cut is the open side of that skewed end. Two null links, not a dropped texture and not the debug colour.
