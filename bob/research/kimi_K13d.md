## K13d verification — J04_jungle_brick_box.md vs. staged packs

| Claim | Found? | Note |
|---|---|---|
| `L4_HJ.MIX` sha256 prefix `517afe6d` | ✅ | `~/lol2_runtime_root/DAT/L4_HJ.MIX` hashes to `517afe6d59a4…`; matches `source.sha256` in `L4_HJ.json` and `source_sha256` in `jungle.json` |
| Region 2122 exists, one floor quad, material key `100` | ✅ | `jungle.json`: exactly 1 face, kind `floor`, material `"100"`; no other faces, and no `wall_bindings` entries for 2122 ("no wall of its own" ✓) |
| `material_100.png` is grass | ✅ | File exists; image is green grass |
| Point (−3022, −475) native = (−3022, 475) Godot lies inside region 2122 | ✅ | Point-in-polygon test against the region's quad (−2990.5/579.2, −3081.4/526.0, −3077/258, −2871/462) returns inside |
| Owner id "17-26-29" | ⚠️ | Not verifiable from the named files. `movable:17/26/29` exist in `L4_HJ.json` but their fixed-point placements decode far from (−3022, −475); no object placement matches that point |
| "F10" label | ⚠️ | No such face/record id in `jungle.json` or `L4_HJ.json`; appears to be an external label |
| Region 4758 exists; closed box (floor + 4 walls + ceiling) | ✅ | `jungle.json`: 6 faces — 1 floor, 4 walls, 1 ceiling |
| 4758 floor 0, ceiling 64 | ✅ | Floor y=0, ceiling y=64, wall spans y=0→64 |
| 4758 native footprint (−4303,3856),(−4129,3856),(−4138,3962),(−4294,3950) | ✅ | Godot floor points match with z = −native_y (one corner listed as −3862 vs spec's 3856 — the quad spans z −3962…−3856, consistent) |
| Godot centre ≈ (−4216, −3909), ~4500 units from owner | ✅ | Computed centre ≈ (−4217, −3909); distance to (−3022, 475) ≈ 4544 |
| Wall-table first index 39, count 4; edges 0–3 = records 42/41/40/39, codes 4/5/6/7, all resource 65 | ✅ | `wall_bindings` for region 4758 match the spec table exactly, including codes |
| 4758 walls drawn with material key `65` → `material_65.png` | ✅ | All 4 wall faces use material `"65"`; materials dict maps `"65"` → `material_65.png` |
| `material_65.png` is a tan brick course | ✅ | File exists; image is tan/brown brick courses |
| 4758 floor and ceiling are not key 65 | ✅ | Both are key `100` |
| Region 3218: second closed room, native (5824,−2560)–(5952,−2432), floor 0, ceiling 80 | ✅ | Floor quad x 5824–5952, z 2432–2560 (= −native_y); floor y=0, ceiling y=80 |
| 3218 records 1912–1915, all resource 65, floor+ceiling also key 65 | ✅ | `wall_bindings`: records 1915/1914/1913/1912 (edges 0–3), all resource 65; floor and ceiling faces use material `"65"` |
| 3218 ~9100 units from owner | ✅ | Computed ≈ 9136 |
| Regions 89–91: records 3843, 3844, 3847, 3848, 3851 resource 65 | ✅ | All five records appear in `wall_bindings` with resource 65 (89: 3844, 3843; 90: 3848, 3847; 91: 3851) — note these regions also carry non-65 records (615), consistent with "pieces of a larger wall" |
| Regions 89–91 ~800 units west of owner | ✅ | Face centroids ≈ (−3776, 73), (−3737, 166), (−3758, 120): west of x=−3022, distances 779–855 |
| Static-assembly name run at file offset 13284825, 98 names, index 18 = `Brick` | ✅ | Parsed MIX at 13284825: 98 entries (24-byte name + 6-byte trailer, stride 30), index 18 = `Brick` |
| Name-run count equals static template table count | ✅ | `static_assemblies/L4_HJ/assemblies.json` placements reference templates 0–97 → 98 slots |
| Template 18 is a 5×2×2 child, all six faces resource 65 | ✅ | Template 18 → child 41; 66 faces = 11 assemblies × 6 faces, every face `material_0065.png`; sample footprint 5×2, height 2 |
| Template 18 has 11 placements near (4500, −3200) | ✅ | Exactly 11 placements (indices 194–204), coords x 4469–4712, y −3333…−3176 |
| `jungle.json` does not draw static assemblies | ✅ | Every face in `jungle.json` carries a region id; scope states "objects… absent"; assemblies live only in the separate `static_assemblies` pack |
| 4758 flags `0x0200`; "no neighbors" for 4758 and 3218 | ⚠️ | Region flags/adjacency are geometry-entry data not stored in `jungle.json` or `L4_HJ.json`; not checkable from the named files (nothing contradicts it) |

**Summary:** Every checkable identifier and coordinate in the spec verifies cleanly — regions 2122/4758/3218/89–91, wall records 39–42 and 1912–1915 and 3843–3851, material keys 65/100, the sha256 prefix, the 98-name run with `Brick` at index 18, and template 18's 11 brick placements. Only three claims are outside the named files' reach: the `0x0200` flags / "no neighbors" region metadata, and the provenance labels "Owner 17-26-29" / "F10" (the movable 17/26/29 records exist in `L4_HJ.json` but do not sit at the cited point).

