## Verification table

| Claim | Found? | Note |
|---|---|---|
| `L4_HJ.MIX` sha256 prefix `517afe6d` | ✅ | `jungle_review/jungle.json` `source_sha256` and `jungle_props/props.json` `source.sha256` both start `517afe6d59a4a062…` |
| Record 3268, native (−598, 5252) | ✅ | `L4_HJ.json` object index 3268, placement x=−598, z=5252; also instance `[−598, 0, −5252]` in `jungle_props/props.json` prop_727 group |
| Record 3277, native (−769, 5188) | ✅ | Same sources; placement x=−769, z=5188 |
| Both records in region 1667 | ✅ | Placement bytes 10–11 = 0x0683 = 1667 for both |
| Both records have no events | ✅ | `"events": []` on both objects in `L4_HJ.json` |
| Template u16 at placement byte 32 = 22 | ✅ | Bytes 32–33 = `16 00` = 22 for both records |
| Selector at byte 35 = 0 | ✅ | Byte 35 = 0x00 for both (the trailing 0x03 is byte 36, not the selector) |
| All 53 placements of template 22 are selector 0 | ✅ | Exactly 53 template-22 props in `L4_HJ.json`; byte 35 is 0 for every one |
| Descriptor 727, drawn frame `prop_727_0.png` | ✅ | `jungle_props/materials.prop_727 = {frames: ["prop_727_0.png"]}`; PNG exists, 64×200 ✓ |
| Box −16..12, height 0..100 | ✅ | prop_727 group in `props.json`: left −16.0, right 12.0, bottom 0, top 100 |
| Top 8 rows of PNG opaque, 42 px each | ✅ | Verified pixel-by-pixel: rows 0–7 each have exactly 42 alpha>0 pixels |
| Region 1667 ceiling 127 / region 1714 ceiling 255 | ✅ (indirect) | Face 8631 spans y 127→255 exactly; record 3268 placement byte 18–19 = 127; no explicit ceiling field exists in the packs |
| Region 1714 has no wall records (first index 65535, count 0) | ⚠️ consistent, not literal | `65535` appears nowhere in either JSON; but `wall_bindings` has zero entries for region 1714 and 1714 has exactly one wall face, so the data is consistent |
| Face 8631: region 1714 wall, (−788, 5139)→(−541, 5248), heights 127→255 | ✅ | `faces[8631]` matches exactly (godot z = −5139.31/−5248, i.e. native 5139/5248), no material key |
| `wall_unresolved` says `missing_record` | ✅ | `{region: 1714, edge: 1, code: 1, reason: "missing_record", candidates: []}` (keyed by region/edge, not face index) |
| `jungle_review.gd` leaves `draw_unbound_walls` true | ✅ | `jungle_review.gd:16` `var draw_unbound_walls := true`; skip only when false (`:216`) |
| Unbound wall colour `Color(0.32, 0.34, 0.31)` | ✅ | `jungle_review.gd:174` — the `else` branch when the material key has no texture |
| F10 (−627, −5177) inside region 1714 | ✅ | Point-in-polygon test against the region-1714 floor quad in `jungle.json` returns true |
| Selectors 1/2 (descriptors 728/729) absent from staged pack | ✅ | No `prop_728*`/`prop_729*` anywhere under `generated/`; not in `props.json` materials |
| Selector 1/2 boxes (−10..10 h56; −39.5..39.5 h86) | ❌ not verifiable | No descriptor/box data for 728/729 exists in the packs |
| Old export paths `lol2_out/all_maps_20260922/L4_HJ/props/sprites/prop_728.png` / `prop_729.png` | ❌ not verifiable | That directory tree is not in `~/opus_work/lol2_r15` |
| 128-name run at file offset 13259149, index 22 = `verytall` | ❌ not verifiable | `L4_HJ.MIX` binary is not in the repo; spec itself flags this as LIKELY/open |

## Summary

Every claim that is checkable against the staged packs — records 3268/3277, coordinates, region 1667, template 22 / selector 0 (including the 53-placement census), descriptor 727 with box −16..12 × 0..100, the 64×200 frame with its 8 opaque 42-pixel top rows, face 8631 in region 1714 with no material key, the `missing_record` unresolved-wall entry, and `jungle_review.gd`'s `draw_unbound_walls = true` with the `Color(0.32, 0.34, 0.31)` fallback — verifies exactly as written. The only unverifiable items are ones requiring artifacts outside the repo (the `L4_HJ.MIX` name table at offset 13259149, the old `all_maps_20260922` export, and the raw 65535 wall-record header), and the spec itself already flags those as open.

