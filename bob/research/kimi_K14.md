# K14 verification — J07 (L5 hive clipping walls)

Sources: `assets/lol2/generated/hive_review/hive.json`, `scripts/lol2/native_scripts/L5_HC.json`.

| claim | found? | note |
|---|---|---|
| Faces live in `hive_review/hive.json` | yes | 4305 faces, kinds floor/ceiling/wall |
| `L5_HC.MIX` sha256 prefix `a1979e60` | yes | `L5_HC.json.source.sha256` and `hive.json.source_sha256` both `a1979e60d401…` |
| Region 758 floor −1011, ceiling −639 | yes | face 1900 floor @ −1011, face 1901 ceiling @ −639 |
| Region 758 flags `0x2204` | no | no `flags` field anywhere in either pack; "2204" substring hits are a wall_record id and uv floats |
| Floor face 1900 = material 234, ceiling 1901 = material 21 | yes | exact match; both keys in `materials`, `material_234.png` / `material_21.png` on disk |
| Regions 911, 907: floor −941 / ceiling −691, faces 2393/2394, 2376/2377, mats 234/231 | yes | all four faces match exactly |
| Overlap areas 758∩911 = 571, 758∩907 = 359 | yes | recomputed by polygon clip: 571.0 and 359.0 exactly |
| Face 1902: region 758, record 1826, resource 65, heights −1011..−639, edge (−3694,7215)–(−3650,7277) | yes | face geometry matches (F10 z = −native y); binding record 1826 → region 758 edge 3, resource 65 |
| "Middle of face-1902 edge is inside 911 and 907" | partial | midpoint (−3672,7246) is inside 911, but **not** inside 907; the edge enters 907 only for its last ~22% (from ≈(−3660,7263) to (−3650,7277)) |
| Face 2396: region 911, record 1536, resource 225, −941..−691, edge (−3641,7250)–(−3688,7223), whole edge inside 758 | yes | geometry, binding, and both endpoints inside 758 all confirmed |
| Face 2379: region 907, record 1534, resource 210, −941..−691, crosses 3793/3794 edge at (−3633,7263) | yes | binding matches; segment intersection computed at (−3633.0, 7262.6) |
| Faces 3793/3794: records 1825/1824, resource 65, −1011..−921 / −891..−639 | yes | bindings → region 758 edge 0, resource 65; heights exact |
| `material_65.png`, `material_225.png`, `material_210.png` | yes | all exist in `hive_review/` |
| West sample (−3689,7143) is region 751 (floor −1011, ceiling −639); 757 next room on same floor | yes | point-in-polygon: inside 751, not 757; both regions' floors @ −1011 |
| Thin slabs 1178/1176/1175/1191: floor −921, ceiling −891, faces 3160/3161, 3152/3153, 3148/3149, 3195/3196, mats 21/65 | yes | all eight faces match exactly |
| Slab overlap areas 470/273/122/140/107/91 | yes | recomputed: 469.7, 272.9, 122.3, 139.7, 107.0, 90.7 |
| Region 1178 has no wall records | yes | zero entries with `region: 1178` in `wall_bindings` |
| Region 1179 sloped; corners −911,−911,−921,−921 / −901,−901,−891,−891; faces 3162/3163; overlaps 910 by 470, 909 by 44 | yes (geometry) | corner heights in listed order ✓; recomputed overlaps 469.5 / 43.8 ✓ |
| Region 1179 flags `0xa20c` | no | no flags data in staged packs |
| Region 752: floor −981, ceiling −921, footprint ≈(−3536,7184)–(−3485,7235); floor meets none of the pairs | yes | bbox matches; recomputed overlap with 758/907/911 = 0 |
| Region 756 edge 2: faces 3791 (rec 1817, res 65, −1011..−981) and 3792 (rec 1818, res 65, −921..−639); open band = 752's heights | yes | both bindings are region 756 **edge 2**, resource 65; band −981..−921 matches region 752 exactly |
| Owner ids 17-42-38 / 43-05 / 43-17 | no | report metadata; absent from all four staged files |

Summary: every region, face index, material key, record/resource id, height band, coordinate, and overlap area in J07 reproduces from `hive.json`/`L5_HC.json` (all 10 recomputed intersection areas match to rounding). Two exceptions: the midpoint of face 1902's edge is inside region 911 only (it enters 907 just for its last ~22%), and region flags `0x2204`/`0xa20c` plus the owner ids are not recorded in the staged packs.

# K14 verification — J10 (L14 temple window)

Sources: `assets/lol2/generated/maps/L14_HT/area.json`, `scripts/lol2/native_scripts/L14_HT.json`.

| claim | found? | note |
|---|---|---|
| `L14_HT.MIX` sha256 prefix `c294f9ab` | yes | `area.json.source.sha256` and `L14_HT.json.source.sha256` both `c294f9ab142b…` |
| Region 918 floor 0 / ceiling 110; region 630 floor −100 / ceiling 1200; camera (2625.3, 2698.8) inside both | yes | faces 1809/1810 give 0/110; 630 gives −100/1200; point-in-polygon true for both footprints |
| Region 21 floor 0 / ceiling 125; hall cameras (2876.3,3361.9), (2884.7,3375.9) inside | yes | footprint containment confirmed for both points |
| Face 9152: region 630, mat 182, −100..156, native ≈(2635,2649) | yes | face center (2635, 2649.5); edge 2, wall_record 4775 |
| Texture `47f5b112c200646a0843.png` = material 182 | yes | `materials["182"]` maps to it; file on disk |
| Faces 9154 (631, 182, −100..145) and 9168 (640, 182, −100..150) | yes | exact match |
| Face 12894: region 3255, mat 221, −80..20 | yes | exact match |
| Cluster 278 membership (532–537, 552, 609, 610, 614, 630, 631, 638–640, 644, 670–677) | partial | all 24 region ids exist in `area.json` and the list is exactly 24, but the cluster batching itself is not in the staged packs (`region_visibility.gd` is absent from this repo — no `PORTAL_VISIBILITY_AREAS` anywhere under `lol2_r15`) |
| Cluster 0 (0–3, 5–7, 12, 17, 20–28, 30, 819, 835, 837, 838, 1055) and cluster 3 = {15,16} | partial | all ids exist (24 and 2 entries); batching source unverifiable, as above |
| Material keys 495→`aae3b5f5…`, 496→`c723b1e0…`, 473→`9a9279844…`, 181→`f54ade4501…` | yes | all four match the `materials` dict; all PNGs on disk |
| Face 8230: region 17, 496, 95..125, (2709,3312)–(2889,3269); face 8240: region 25, 496, 95..125, to (3091,3348) | yes | exact match both |
| Face 8228: region 16, 181, 80..95, x 2743–2900, y 3254–3266; face 8245: region 30, 181, 80..95, to x 3107 | yes | exact; 8228 carries `edge: 2`, confirming "region 16's edge 2" |
| No wall face covers 0..80 on region 16's edge (2900,3254)→(2743,3266) | yes | region 16 has exactly two wall faces: 8228 (80..95, this edge) and 8227 (0..95, a different edge to (2709,3312)) |
| Region 15's lower faces 8225/8226 sit at native y ≈3234, not on that edge | yes | both 0..80 at y 3234–3238; they touch the edge only at the single corner (2743,3266) |
| Garden faces: 1810 (918, 473, 110), 9634 (915, 473, 110..135), 9656/9657 (933, 473, 135..150), 9670 (940, 473, 135..150); floor 1809 = 473 | yes | all exact |
| Face 9634 is the step on the shared 918/915 edge | yes | 918 and 915 footprints share exactly the segment (2626,2705)–(2595,2663) = 9634's base edge; ceilings 110/135 confirmed |
| Face 9634 "about 32 units from the camera" | no | horizontal distance from (2625.3,2698.8) to the face's base edge ≈ 3 units; to face midpoint ≈ 21; no measure I tried gives 32 |
| Green ground/willow: no `area.json` prop within 120 units | yes | nearest prop to the camera is 166.7 units away (record 410, region 912); 288 props scanned |
| Report ids, longplay frames `g_262`–`g_286`, portal walk rule | no | not present in the staged packs (external report/repo data) |

Summary: all named faces, regions, materials, heights, and coordinates in J10 verify against `area.json`/`L14_HT.json`, including the camera containment, the uncovered 0–80 strip on region 16's edge 2, the 918/915 shared-edge step, and the >120-unit prop-free radius. The cluster membership lists are consistent (all ids exist, 24 per batch) but the batching/portal rule itself lives in the absent `region_visibility.gd`, and the "32 units" camera distance for face 9634 does not reproduce (actual ≈3 units horizontally).

