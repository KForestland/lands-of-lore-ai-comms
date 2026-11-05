# J06 L5 flat roof, two faces on one height

Owner 17-41-10. F10 (−2066, −7611) is native (−2066, 7611). That point is inside region 265 and inside region 269. No Godot was run. No longplay frame was matched. `hive_review/hive.json`.

Region 269 is a floor subdivision of region 265. Its raw ceiling word is 12. The geometry export stores no ceiling for it, and the pack draws no ceiling face.

## Not a z-fight

These two do not share a height:

| face | region | kind | height | material |
| --- | --- | --- | --- | --- |
| 654 | 265 | ceiling | −107 | none |
| 658 | 269 | floor | −67, −57, −57, −67 | `234` (`material_234.png`) |

The gap is about 40 units. `hive_review.gd` extends `jungle_review.gd`, so the ceiling with no material key draws as the flat unbound colour.

## The coplanar pair

Face 654, region 265 ceiling, is the whole quad (−2112, 7536)–(−1984, 7696) at height −107, no material. Four subdivision floors sit on that same height with material `234`:

| face | region | height |
| --- | --- | --- |
| 655 | 266 | −107 |
| 662 | 273 | −107 |
| 663 | 274 | −107 |
| 670 | 281 | −107 |

Each of those floors overlaps the ceiling quad in x/z. Both are drawn. That is the texture jump: a textured floor and an untextured ceiling in the same plane.

## Still open

Which of the four floors the owner was looking at. A longplay frame of this roof.
