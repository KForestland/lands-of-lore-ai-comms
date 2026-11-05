# J02 L3 gallery bars, wrong colour

Owner 17-14-40/52. F10 (1107, −830) is native (1107, 830). That point is inside region 1057. No Godot was run. `L3_DH.MIX` sha256 prefix `bd85c12d`. Geometry key 3106551060.

The 17:14 clock is the playtest, not the longplay. Longplay `f_00208` (about 17:15) is the Draracle throne cutscene. The lattice the longplay opens at 17:58 is gate 77, a different object. No longplay frame of this hall was matched.

## The hall

Region 1057 is one quad, floor 0, ceiling 120, flags `0x2200`, wall-record count 0. `museum_review/museum.json` draws two faces: floor material key `237` (`material_237.png`, preset Floor14, resource 237) and ceiling key `872` (`material_872.png`, preset Floor13, resource 872). Both files are in that pack. The hall floor and ceiling are textured.

## The gates

The north edge of the hall is three bar movables. Placement byte 32 is the template index. The 30-byte name run at file offset 5943202 has 77 names, the same count as the template table. Name-at-index stays LIKELY.

| movable | native | height | template | LIKELY name | what it is |
| --- | --- | --- | --- | --- | --- |
| 51 | (1128, 948) | 0 | 71 | Bar door | 14 bars, dims 135×5×120 |
| 62 | (1050, 948) | 0 | 55 | Bar | one bar, dims 5×5×120 |
| 78 | (1206, 949) | 0 | 55 | Bar | one bar, dims 5×5×120 |

Each bar child is type 0, mask bit 0 set, so mode 0 draws it. Six surface slots, signed resource at the slot start:

- Faces 0 and 1 (the top and bottom caps) resource 433.
- Faces 2–5 (the four sides the player sees) resource 431.

Template 71's 14 children sit on local x −68..67, each 5 units wide. That is the grate across the hall. Templates 55's two placements are the single bars just outside that span.

The same two resources are already staged, from the Draracle bars (also template 55):

- `museum_draracle_bars/material_0431.png` (resource 431)
- `museum_draracle_bars/material_0433.png` (resource 433)

Copies with the same names are under `static_assemblies/L3_DH/`. `museum_review/` has `material_433.png` and does not have `material_431.png`.

`museum_walkthrough.gd` adds `museum_gallery.gd`. That script builds the grate as 14 `BoxMesh` nodes of size (5, 120, 5) on an `AnimatableBody3D` at Godot (1128, 0, −948), which is native (1128, 948), movable 51. The material is `Color(0.52, 0.43, 0.27)` with no texture. Movables 62 and 78 are not in that script.

`museum_gate` is not this grate. Its `gate.json` is template 58 (LIKELY Iron Door) at native (−4060, 844), texture `gate.png`. That is gate 77.

## The block above the ceiling

Movable 63 at (1128, 916), height 120, template 42 (LIKELY Block wall). Two children, all six faces resource 185 (`museum_review/material_185.png`). Child 106 mask `0x1` is the mode-0 draw. Child 105 mask `0x2` is a later mode and was not entered. Placement height 120 plus local z 0..150 puts the slab from 120 to 270, at and above the hall ceiling. It is not the eye-level grate.

## Still open

Which longplay frame shows movables 51/62/78. The name-table header. Movable 63's mask `0x2` state.
