# K13a verification — J01_cave_crate_wall.md vs staged packs

| claim | found? | note |
|---|---|---|
| `L1_DC.MIX` sha256 prefix `6384ec4d` | yes | `native_scripts/L1_DC.json` source.sha256 and `region_blockers/L1_DC.json` archive_sha256 both `6384ec4d…` |
| Region 1081 exists, one quad | yes | `creature_nav/L1_DC.json` region 1081 = 4-vertex outline; exactly 1 floor face in `original_floors/floors.json` |
| Region 1081 floor −215 | yes | floors.json face y·64 = −215; nav file −215 |
| Region 1081 ceiling −43 | yes | floors.json shell ceiling face for 1081 at y·64 = −43 |
| Region 1081 flags `0x0200` | no | no region-flags table staged in generated/, scripts/, docs/, or tests |
| Neighbors none, 1087, 1082, 1102 (edges 0–3) | yes | geometric edge-match over all nav regions gives edge0=none, edge1=1087, edge2=1082; edge3=1102 via the deferred-connector record in `original_floors/interior_audit.json` |
| Region 1102 floor −130, ceiling −62 | yes | floors.json: floor face −130, shell ceiling face −62 |
| Region 1102 flags `0x0A10` / bit `0x10` | no | not staged anywhere (grep for `0x0A10`/`0x0200` empty) |
| 1081 and 1102 share no vertex pair | yes | vertex sets fully disjoint (1081: (586,12403),(597,12383),(481,12315),(474,12338); 1102: (479,12388),(515,12438),(547,12382),(506,12357)) |
| Span builder defers both directions as "special connector", no boundary/interior face on edge 3 | yes | `interior_audit.json` lists `1081 edge3→1102` and `1102 edge2→1081`, both reason "special connector"; shell has ceiling + edge-0 boundary + edge-2 interior for 1081 but **no** edge-3 face |
| Record 1485: region 1081, descriptor 304, addressing 16 | yes | `wall_review/walls.json` record 1485 matches |
| Record 1485 Godot quad (474,−130,−12338)(586,−130,−12403)(586,−215,−12403)(474,−215,−12338) | yes | points_godot identical to the quoted 4 points; = native (474,12338)–(586,12403), −215→−130 (85-unit step) |
| Point (532,12371) inside 1081 and on edge 3 | yes | computed: inside all 4 edges, 0.57 units from edge 3 at t≈0.52 |
| Record 1484: descriptor 134, addressing 8, heights −62→−43 | yes | walls.json: y range −43..−62, same footprint |
| Records 1486, 1487: descriptor 304, addressing 16 (side closers) | yes | both in walls.json, matching attributes |
| `wall_review/material_304_variant_0.png` and `material_134_variant_0.png` | yes | both files exist (with .import) in `assets/lol2/generated/wall_review/` |
| `original_walk_review.gd` builds collision from floors + shell only | yes | `scripts/lol2/original_walk_review.gd:39,79–107` — collision_faces from floors.json faces + shell |
| `textured_cave_review.gd` draws walls.json, leaves collision | yes | `scripts/lol2/textured_cave_review.gd:75–79,47,51` — loads wall_review/walls.json, "existing collision retained" |
| Record 1485 drawn but not in collision set | yes | in walls.json; no shell/boundary/interior face on edge 3 in floors.json (deferral) |
| Record 1488: descriptor 85, edge 0, neighbor none, (586,12403)→(597,12383), collides | yes | walls.json matches coords (addressing 0); floors.json shell has a boundary face on exactly that edge; no region shares that edge |
| Record 1489: descriptor 85, edge 2 toward 1082; 1082 floor=ceiling=425 | yes | walls.json coords (481,12315)–(474,12338) = edge 2; 1082 is adjacent on that edge; floors.json gives 1082 floor 425, ceiling 425 |
| Seven crate controls 94, 95, 96, 97, 112, 121, 122 exist | yes | all present in L1_DC.json control table (174 controls) |
| All seven at height −215, none with an event | yes | every one has `events: []`; placement hex decodes h=0xFF29=−215; static_collision and `static_assemblies/L1_DC/assemblies.json` agree |
| No opcode 18 targets them | yes | 24 opcode-18 commands (matches counts.opcode_use); targets {0,1,19,99–103,1333} — none of the seven |
| static_collision boxes: scripted false, sizes/coords/templates per table (25→10³, 26→20³) | yes | `scripts/lol2/static_collision_L1_DC.json` rows match all 7 lines exactly (template, x, y, h −215, width/depth/height, scripted false) |
| Template 25 = "Small crate", 26 = "Medium Crate" (names) | partial | template numbers 25/26 confirmed; the names are not staged in any pack, doc, or item table |
| Crate region assignments (1085, 1087, 1081) | yes | point-in-region tests pass for all 7; control 121 (564,12367) sits inside region 1081 ("box in the hole") |
| Mace records at height −130: (417,12444) region 1092 and (471,12480) region 1099 | partial | regions 1092/1099 exist with floor −130 and both points fall inside them; but no object record at those exact coordinates exists in L1_DC.json (scanned all 1949 objects, all tables, all offsets) |
| HINTBOOK 2033–2048 text | no | no hintbook data staged in the packs |
| Definition 13572 | no | not in any staged L1 file (hits only incidental numbers in other levels' area.json) — consistent with "still open" |
| Owner 17-03-39, F10 mapping, "H16 stands" | n/a | provenance/hypothesis references, not checkable against staged data |

**Summary:** Every geometric, record-level, and script claim in the spec verifies against the staged packs — the deferral, records 1484–1489, the missing collision on edge 3, and all seven crate rows match exactly. Three claims are not checkable from staged data (region flags `0x0200`/`0x0A10`, template names, HINTBOOK text), and the two mace records could not be located in `L1_DC.json` even though their cited regions and height corroborate — that one is worth a follow-up before grading the mace paragraph.

