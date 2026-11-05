# J04 L4 brick box in the distance

Owner 17-26-29. F10 (−3022, 475) is native (−3022, −475), inside region 2122. That region is one floor quad, material key `100` (`jungle_review/material_100.png`, grass). It has no wall of its own. No Godot was run. No longplay frame was matched. `L4_HJ.MIX` sha256 prefix `517afe6d`.

## The box

The closed brick box in view of that point is region 4758. No neighbors. Floor 0, ceiling 64, flags `0x0200`. Native footprint (−4303, 3856), (−4129, 3856), (−4138, 3962), (−4294, 3950). Godot centre is about (−4216, −3909), about 4500 units from the owner. Wall-table first index 39, count 4. All four boundary faces are resource 65:

| edge | record | code | resource |
| --- | --- | --- | --- |
| 0 | 42 | 4 | 65 |
| 1 | 41 | 5 | 65 |
| 2 | 40 | 6 | 65 |
| 3 | 39 | 7 | 65 |

`jungle_review/jungle.json` draws those four walls with material key `65`, file `material_65.png`. That image is a tan brick course. The floor and the ceiling of 4758 are not key 65. The original shows this box: the four wall records are resource 65, and the pack uses that same key.

A second closed brick room is region 3218, native (5824, −2560)–(5952, −2432), floor 0, ceiling 80, also no neighbors. Records 1912–1915, all resource 65, plus the floor and the ceiling on key 65. It is about 9100 units from the owner.

## Not this box

The static-assembly name run at file offset 13284825 has 98 names, the same count as the static template table. Index 18 is `Brick`. Name-at-index stays LIKELY. That template is a 5×2×2 child, all six faces resource 65, and its 11 placements sit near (4500, −3200), beside the Monastery walls. They are not region 4758, and `jungle.json` does not draw static assemblies.

Closer brick walls, regions 89–91, are about 800 units west of the owner (records 3843, 3844, 3847, 3848, 3851, resource 65). They are pieces of a larger wall, not a closed box.

## Still open

Which longplay frame shows region 4758. A name for the region itself.
