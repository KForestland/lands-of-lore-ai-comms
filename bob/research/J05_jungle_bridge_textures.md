# J05 L4 bridge span, faces with no material

Owner 23-04-55. F10 (5563, −3922) is native (5563, 3922), inside region 4399. The volume pose (5564, 3817) is region 4398. Both are floor −114, ceiling 13. No Godot was run. No longplay frame was matched. `L4_HJ.MIX` sha256 prefix `517afe6d`.

The floors are textured. Region 4399 and 4398 both use material key `100` (`jungle_review/material_100.png`). The faces with no material key are interior spans. Each of these regions has wall-record count 0 (first index 65535), so `wall_unresolved` says `missing_record` and the candidates list is empty. `jungle_review.gd` has `draw_unbound_walls` true, so each span draws as the flat unbound colour and not as a texture.

| face | region | native x | native y (godot z negated) | heights |
| --- | --- | --- | --- | --- |
| 10223 | 4399 | 5468.5–5469 | 3946–4000.9 | −100 to 13 |
| 10205 | 4383 | 5467–5571.9 | 4003–4122.5 | 13 to 117 |
| 10206 | 4383 | 5468.5–5571.9 | 4000.9–4003 | 13 to 117 |
| 10207 | 4383 | 5430–5468.5 | 4000.9–4121 | −100 to 117 |
| 10208 | 4383 | 5430–5467 | 4121–4122.5 | 13 to 117 |
| 10215 | 4390 | 5412–5469 | 3887–3946 | −100 to 127 |
| 10216 | 4390 | 5468–5469 | 3542–3946 | 13 to 127 |
| 10217 | 4390 | 5412–5468 | 3542–3612 | −100 to 127 |
| 10222 | 4397 | 5468–5546.6 | 3392.2–3542 | −100 to 13 |

Region 4383's ceiling is 117 and 4390's is 127, against the bridge floor's ceiling of 13. The tall spans are that step. Face 10223 is the half-unit seam on the owner's region.

Two faces next to the seam do have a material. Region 4388 records 699 and 700 are resource 740 (`material_740.png`). Region 4396 record 3530 is resource 615 (`material_615.png`). Region 4388's floor is key `808`.

`jungle_bridge_break` is a different bridge. Its props 961 and the rest sit near native (1420, −1178), materials `prop_1037.png` and `prop_1038.png`. They are not these faces.

## Still open

Whether the original draws a span that has no wall record. Which longplay frame shows this deck.
