| claim | found? | note |
|---|---|---|
| Region 1057 exists | ✅ | `region:1057` object in `L3_DH.json`; 2 faces (floor+ceiling) in `museum_review/museum.json` |
| Region 1057 one quad, floor 0, ceiling 120 | ✅ | Floor face 4 pts at y=0, ceiling 4 pts at y=120; x 1062–1194, z −902…−644 |
| Region 1057 flags `0x2200`, wall-record count 0 | ⚠️ partial | Wall-record count 0 corroborated (no `interior_bindings` entries for 1057). Flags not stored in staged packs; raw MIX geometry has exactly one floor0/ceil120 record with flags `0x2200`, but its leading fields don't match 1057's quad — unconfirmed |
| Floor material key `237` → `material_237.png`, preset Floor14 | ✅ | Face material `"237"`; file exists; Floor14↔resource 237 binding present in pack (bound to regions 177/178/180; 1057's own floor binding only appears as the face material) |
| Ceiling material key `872` → `material_872.png`, preset Floor13 | ✅ | `ceiling_bindings` has `{"region":1057,"name":"Floor13","resource_index":872}`; file exists |
| Movable 51 native (1128, 948), height 0, template 71 | ✅ | `placement_hex` in `L3_DH.json` decodes x=1128 y=948 h=0, byte32=0x47=71 |
| Movable 62 (1050, 948), h 0, template 55 | ✅ | Decodes exactly; byte32=0x37=55 |
| Movable 78 (1206, 949), h 0, template 55 | ✅ | Decodes exactly; byte32=0x37=55 |
| Movable 63 (1128, 916), height 120, template 42 | ✅ | Decodes exactly (h=0x78=120, byte32=0x2A=42) |
| Placement byte 32 = template index | ✅ | Holds for all four movables |
| Template 71 "Bar door": 14 children, dims 135×5×120, x −68..67, each 5 wide | ✅ | `museum_gallery/gallery.json` template 71: dims [135,5,120], 14 children, bounds (−68,−63)…(62,67), all type_byte 0 |
| Bar child faces 0–1 resource 433, faces 2–5 resource 431, mask bit 0 | ✅ | Child surfaces [433,433,431,431,431,431], mask `01000000`; confirmed in gallery.json and raw MIX child 173 |
| Template 55 "Bar": one bar, dims 5×5×120 | ✅ | MIX template record @5930622: dims [5,5,120], child count 1; Draracle bar faces span 5×120×5 |
| Name run @5943202, 30-byte records, 77 names; index 71="Bar door", 55="Bar", 42="Block wall", 58="Iron Door" | ✅ | Parsed from real `L3_DH.MIX`: 77 non-empty names then empty; all four names match |
| `L3_DH.MIX` sha256 prefix `bd85c12d` | ✅ | Actual file hashes `bd85c12d4a2c…`, matching `L3_DH.json` source record |
| Geometry key 3106551060 | ✅ | In `L3_DH.json` source block and `museum_draracle_bars_source.json` |
| `museum_draracle_bars/material_0431.png` + `material_0433.png` (Draracle bars also template 55) | ✅ | Both files exist; bars source JSON: movables 71–74 all template 55, materials map those two PNGs |
| Copies under `static_assemblies/L3_DH/` | ✅ | `material_0431.png` and `material_0433.png` both present |
| `museum_review/` has `material_433.png`, lacks `material_431.png` | ✅ | Confirmed by listing and `materials` dict (433 present, 431 absent) |
| `museum_gallery.gd`: 14 BoxMesh (5,120,5) on AnimatableBody3D at Godot (1128,0,−948), Color(0.52,0.43,0.27), no texture | ✅ | `range(14)` loop, `grate.position = Vector3(1128,0,-948)`, `albedo_color = Color(0.52,0.43,0.27)`, unshaded, no texture (same material is shared with the lever) |
| `museum_walkthrough.gd` adds `museum_gallery.gd`; movables 62/78 not in gallery script | ✅ | `preload(...museum_gallery.gd)` at line 296; no 1050/1206 coordinates in the script |
| `museum_gate/gate.json` = record 77, template 58, native (−4060, 844), `gate.png` | ✅ | gate.json: `"record":77,"template":58,"position":[-4060,0,-844]`; gate.png exists; template 58 dims [54,1,78] match width 54/height 78 |
| Template 42: 2 children, all six faces resource 185; child 106 mask 0x1, child 105 mask 0x2 | ✅ | MIX child records 105/106: surfaces [185]×6, masks 0x2/0x1; template dims z=150 → slab 120–270 with height 120 |
| `museum_review/material_185.png` | ✅ | File present |
| Point (1107, 830) inside region 1057 | ✅ | 1107 ∈ 1062–1194, 830 ∈ 644–902 |
| Owner 17-14-40/52, longplay f_00208 / 17:58 gate-77 claims, "No Godot was run" | ➖ n/a | Video/provenance statements; nothing in the staged packs to check them against |

**Summary:** Every concrete id, coordinate, template, material, file, and script claim in the spec verifies against the staged packs, `L3_DH.json`, or the raw `L3_DH.MIX` (sha256 `bd85c12d…` confirmed) — including the name table at offset 5943202 and the template-42 child masks. The only unconfirmed datum is region 1057's flags `0x2200` (not carried in staged files, and the one matching raw-geometry record doesn't align with 1057's quad); wall-record count 0 is supported indirectly by the empty interior bindings.

