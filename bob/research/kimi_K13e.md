| claim | found? | note |
|---|---|---|
| `L4_HJ.MIX` sha256 prefix `517afe6d` | yes | `jungle.json.source_sha256`, `L4_HJ.json.source.sha256`, and bridge_break `media.json.source.sha256` all start `517afe6d…` |
| Face 10223, region 4399, 5468.5–5469 / y 3946–4000.9 / −100..13 | yes | exact match (z −4000.87..−3946 → native y 3946–4000.9); kind wall, no material key |
| Face 10205, region 4383, 5467–5571.9 / 4003–4122.5 / 13..117 | yes | min x is 5466.98 (rounds to 5467); rest exact; no material key |
| Face 10206, region 4383, 5468.5–5571.9 / 4000.9–4003 / 13..117 | yes | exact (y 4000.87–4003.03); no material key |
| Face 10207, region 4383, 5430–5468.5 / 4000.9–4121 / −100..117 | yes | exact; no material key |
| Face 10208, region 4383, 5430–5467 / 4121–4122.5 / 13..117 | yes | max x 5466.98 (rounds to 5467); y 4120.98–4122.47; no material key |
| Face 10215, region 4390, 5412–5469 / 3887–3946 / −100..127 | yes | exact; no material key |
| Face 10216, region 4390, 5468–5469 / 3542–3946 / 13..127 | yes | exact; no material key |
| Face 10217, region 4390, 5412–5468 / 3542–3612 / −100..127 | yes | exact; no material key |
| Face 10222, region 4397, 5468–5546.6 / 3392.2–3542 / −100..13 | yes | exact (z −3542..−3392.19 → 3392.2); no material key |
| Regions 4399 and 4398 floors use material key `100` | yes | both have exactly one floor face, material `"100"`; `material_100.png` exists in jungle_review |
| Floor −114, ceiling 13 for 4399/4398 | partial | floor y = −114 confirmed on both floor faces; no ceiling faces or region-height records are staged — ceiling 13 is only corroborated indirectly (spans 10223/10222 top out at 13, 4390's spans start at 13) |
| Region 4383 ceiling 117, 4390 ceiling 127 | partial | matches the span y-maxima of faces 10205–10208 (117) and 10215–10217 (127), but no explicit ceiling record staged |
| Wall-record count 0 (first index 65535) → `missing_record`, empty candidates | mostly | `wall_unresolved` has `missing_record` with `candidates: []` for 4383 (edges 0–3), 4390 (edges 1–3), 4397 (edge 1), 4399 (edge 1); the literal value 65535 appears in no staged L4_HJ JSON |
| `jungle_review.gd` has `draw_unbound_walls` true | yes | `scripts/lol2/jungle_review.gd:16` `var draw_unbound_walls := true` |
| Region 4388 records 699 and 700 → resource 740 | yes | `wall_bindings`: record 699 (edge 3) and 700 (edge 2), region 4388, resource 740; `material_740.png` exists |
| Region 4396 record 3530 → resource 615 | yes | `wall_bindings`: record 3530, region 4396, edge 3, resource 615; `material_615.png` exists |
| Region 4388 floor is key `808` | yes | 4388's floor face has material `"808"` (floor y −200); `material_808.png` exists |
| F10 native (5563, 3922) inside region 4399 | yes | point-in-polygon against 4399's floor quad returns true |
| Volume pose (5564, 3817) is region 4398 | yes | point-in-polygon against 4398's floor quad returns true |
| `jungle_bridge_break` props 961+ near native (1420, −1178), `prop_1037/1038` | yes | `media.json` props 961–965, record 961 at position [1420, −103, 1178] (godot z 1178 → native −1178), region 3032; both `prop_1037.png` and `prop_1038.png` exist and are used |
| Owner 23-04-55 | n/a | not a map datum; nothing in the staged packs to check it against |

Summary: every face index, region, material key, record id, and coordinate in the spec checks out against the staged packs — the nine no-material spans match exactly (two values are rounded in the spec: 5466.98→5467). The only soft spots are the ceiling heights (13/117/127), which are inferable from span tops but not staged as explicit records, and the literal "first index 65535", which appears in no staged L4_HJ JSON — the `missing_record` / empty-candidates entries in `wall_unresolved` are the staged evidence for it.

