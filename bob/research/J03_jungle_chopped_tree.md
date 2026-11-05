# J03 L4 chopped tree, the missing top

Owner 17-16-55. F10 (−627, −5177) is native (−627, 5177), inside region 1714. No Godot was run. No longplay frame was matched: that clock is the playtest. `L4_HJ.MIX` sha256 prefix `517afe6d`.

## The tree

Two props stand on the north edge, in region 1667 (ceiling 127), which shares an edge with 1714 (ceiling 255):

| record | native (godot z) | template | selector | descriptor | box |
| --- | --- | --- | --- | --- | --- |
| 3268 | (−598, 5252) | 22 | 0 | 727 | −16..12, height 0..100 |
| 3277 | (−769, 5188) | 22 | 0 | 727 | same |

Template 22 is a u16 at placement byte 32. The 38-byte name run at file offset 13259149 has 128 names, the same count as the prop-template table. Index 22 is `verytall`. Name-at-index stays LIKELY. Selector is placement byte 35, and it is 0. All 53 placements of template 22 are selector 0. These two records have no event, so `jungle_props` draws them.

The drawn part is one frame: `jungle_props/prop_727_0.png`, 64×200. The billboard quad is the native box, 28 wide and 100 tall. Frame trim is 0. The top eight rows of the PNG are opaque (42 pixels each), so the painting ends in a flat cut. That is the chopped top the owner sees.

## The part that is not drawn

The same template has two more selectors. Nothing in L4 selects them, and the staged pack has neither image.

| selector | descriptor | state height | box | image in the old L4 prop export |
| --- | --- | --- | --- | --- |
| 1 | 728 | 56 | −10..10 | `lol2_out/all_maps_20260922/L4_HJ/props/sprites/prop_728.png` — a shorter bare stub |
| 2 | 729 | 86 | −39.5..39.5 | `.../prop_729.png` — leafy crown on a short trunk |

Selector 2 is the crown. It is not this placement's selector. Putting it on records 3268 and 3277 would be a new state, not the byte the file stores.

## The untextured cap above them

Region 1714 has no wall records (first index 65535, count 0). `jungle_review/jungle.json` face 8631 is the interior span on the edge toward 1667, heights 127 to 255, from (−788, 5139) to (−541, 5248). `wall_unresolved` says `missing_record`. The face has no material key. `jungle_review.gd` leaves `draw_unbound_walls` true, so that span draws as the flat unbound colour `Color(0.32, 0.34, 0.31)`. It is not a prop part.

## Still open

Which longplay frame shows records 3268 and 3277. Whether any unentered callee switches template 22 off selector 0. The name-table header.
