# BG24 Darker Jungle bark sheets (17-50-18)

Grade: DECODED for the quads. The longplay of these three poses was not found, so the sheets were not moved and not hidden.

Owner r17, Darker Jungle, three looks upward:

- 17-50-18 at (-2386, 589), pitch about 29 degrees: "this structure is out of place here".
- 17-50-38 at (-3794, 979): "out of place".
- 17-50-53 at (-3797, 1400): "out of place textures".

The center of each shot is a source wall, material 130, from height 60 to 200.

| Face | Region | Edge | Neighbor ceiling | Span |
| --- | --- | --- | --- | --- |
| 7526 | 516 | 1, neighbor 526 | 60 | 60–200 |
| 7540 | 531 | 1, neighbor 537 | 60 | 60–200 |
| 7542 | 532 | 1 | 60 on the hedge side | 60–200 |
| 7544 | 533 | 1, neighbor 535 | 60 | 60–200 |
| 7546 | 534 | 1, neighbor 536 | 60 | 60–200 |

Each record is `8200000080011000`. Surface code 1, caller `0x114aa4`, vertical offset 0. Material word 130. The region floor is 0 and the region ceiling is 200. The quad is the part of that volume above the neighboring hedge ceiling. It is not a guessed band. Face 12017 (region 3944, code 2, the same material and the same 60–200 gap) is the same pattern and is not in these three shots.

UV is the wall formula for byte 6 bit 0x10 and byte 7 scale 2: about 4.7 by 4.4 repeats of the 64×64 bark. The texture is opaque. It is not in the cutout list. Foliage 276 beside these spans is the 0–60 hedge.

Longplay. Act 2 frame g_00157 at 3:07:40 is the tree village: dark trunks and round platforms. g_00001 at 1:49:40 and g_00153 at 3:05:40 are forest and rock. None of those frames is one of these three poses, and none of them shows this tiled sheet. Reseating the quads on 0–64, or on the y=200 deck, would invent a height the records do not store. Hiding the five risers would invent a skip the builder does not have.

No patch. Smallest adapter, not applied: do not draw faces 7526, 7540, 7542, 7544 and 7546. That needs a longplay frame of one of these poses, or a render rule that drops them, before it is applied.
