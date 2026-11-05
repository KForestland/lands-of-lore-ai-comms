# I01 NE tower walkway

The FireWall doors are movables 92, 93, and 94, stored (2242, 2947), (2342, 2947), and (2292, 2947), height 0, static byte 44, no events. Movable 94 sits in region 3018, floor 0, ceiling 100. Godot positions are (2242, −2947), (2342, −2947), and (2292, −2947). The earlier pack calls slot 44 FireWall Door. This pass did not re-walk that name table, so the name stays LIKELY. The greenhouse point (2289, 648) is prop 602, Ball O Smoke, height 18, region 6098, floor 3, ceiling 375. Godot (2289, −648). No frame was opened. No Godot was run.

## There is a floor strip

Geometry neighbors, not creature_nav, connect region 6098 to region 10205 in 26 steps. The quads stay inside x about 2173–2403 and march in native +y.

| region | floor | ceiling | native y span | note |
| --- | --- | --- | --- | --- |
| 6098 | 3 | 375 | 523–663 | greenhouse |
| 6088 | 45 | 375 | 1045–1081 | hourglass band, prop 627 is (2293, 1070) |
| 6079 | 45 | 375 | 1108–1127 | last region the nav graph still shares |
| 6084 | 100 | 475 | 1127–1230 | nav has no edge 6079→6084 |
| 6066 | 105 | 480 | 1380–1410 | |
| 6078 | 70 | 590 | 1410–1605 | nav has no edge 6066→6078 |
| 6074 | 105 | 480 | 1605–1635 | nav has no edge 6078→6074 |
| 6071 | 100 | 650 | 1635–1911 | |
| 10187 | 5 | 799 | 1911–2188 | floor drops; ceiling jumps |
| 10189 | 0 | 992 | 2187–2359 | |
| 10195 | 0 | 1054 | 2339–2516 | |
| 10197 | 0 | 1094 | 2513–2619 | |
| 10201 | 0 | 1100 | 2617–2739 | |
| 10204 | 0 | 1071 | 2738–2814 | |
| 10205 | 0 | 1001 | 2805–2883 | |
| 10198 |  |  | 2882–2943 | nav quad only; geometry floor not restated. Neighbors join 10205 to 3018 |
| 3018 | 0 | 100 | 2943–2958 | door 94 |

No prop, control, or movable is stored on the step regions 6079 through 10205. The walkway is this strip of quads. It is not a bridge movable.

## Why nav calls it an island

`creature_nav/L16_CA.json` uses the same region ids, with Y stored as native Y flipped. Greenhouse is nav region 6098. The hourglass is 6088. Door 94 is 3018. The greenhouse nav component is 3704 regions and includes the hourglass. It does not include 3018, 10205, 10198, or 3127. Those four sit in a separate component of 271 regions. The cut is the three missing edges above. A walker that trusts nav stops on region 6079, at the north lip of the hourglass, and the next quad is 6084. That is the fall. Walking the geometry neighbors crosses it.

## The flame is not the walk

Brady printed 124–125: the northeast obsidian tower is behind the arboretum. The hourglass is at the north end of the arboretum, between the steps to the tower. Clicking it grows the silverleaf, and a cloud of flame from the pyramid opens the door in the tower's side. Grade BRADY.

Prop 602 kind 6 group 37758, value 20, is opcode 18 raw `12035a02f208870b00001208000000280000`. Kind byte 3, target u16 602, signed words (2290, 2951, 0), flags `0x0812`. Bit `0x0004` is clear, so this is not the direct-relocation form. The words sit on the door. The effect of `0x0812` was not entered. A second record, kind 10 group 37776 value 0, was not read. The three doors still have no events.

## Still open

Opcode 18 flag `0x0812` (I29). The kind-10 record on prop 602. Region 10198's geometry floor. No frame.
