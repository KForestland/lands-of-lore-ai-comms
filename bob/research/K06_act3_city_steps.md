# K06 Act 3, STORY-068 through STORY-078

No Godot was run. Newest owner file is still `TRIAGE_20261104.md`. `act2_map.gd` attaches `l16_arrival_elevator.gd` and `l16_greenhouse.gd` on L16. It does not attach `l16_fountain_ball.gd`. No script under `scripts/lol2` names STORY-069 or STORY-071 through STORY-078. No `l17`, `l19`, or `l20` script exists.

## What the lead already built

STORY-066 is the Chamber handoff, hosted in `l14_chamber_voices.gd` and walked by `l14_chamber_voices_earned_test.gd`. HINTBOOK 4636–4641. Verdict: HOSTED+TESTED. Detail is K05.

STORY-067. HINTBOOK 4666–4668: the elevator ride from the arrival point down to the ground. Host: `l16_arrival_elevator.gd`. Plate control 78, movables 194 and 325, region 233, group 564, movie 27, opcode 18 words native (−3797, −2291), flags 0x0804. Earned test `l16_arrival_elevator_earned_test.gd`. Verdict: HOSTED+TESTED. The plate's door motion is still the deviation's adapter.

STORY-070. HINTBOOK 4855–4894: walk the avenue or take the canal; the yellow figure waters the plots; planting is a separate sentence and the same page says you do not have to plant; a silverleaf goes in the glass pyramid; the hourglass then sends the fireball into the tower doors. Those two planting sentences stay unmerged. Host: `l16_greenhouse.gd`. Control 75 takes one silverleaf. Prop 627 is the hourglass. Prop 602 then moves from native (2289, 648) to (2290, 2951). The 120 units/s figure is the adapter. J15 found no speed byte. Earned test `l16_greenhouse_earned_test.gd`. Verdict: HOSTED+TESTED for the leaf, the hourglass, and the door pose. The yellow figure and valves 123–134, 163, and 164 are not in the script. Verdict for that figure: MISSING. Fix: the same control ids, and do not require them before the hourglass until the left-type-4 predicate is read.

## STORY-068 is broken

HINTBOOK 4788–4814: the southern avenue ends in a raised pad, a ball floats over the dry fountain, any attack destroys it, water returns, and nine clumps of black lichen grow.

The earned test `l16_fountain_ball_earned_test.gd` still does `get_node("L16FountainBall")` and its header still breaks prop 602 and runs kind-10 group 37776. The map never attaches that node. The script header says it is not attached, and that prop 602 is the greenhouse fireball. DEVIATIONS row 451 withdraws row 447. Verdict: BROKEN. The test cannot see its node.

H22, not re-proved from the MIX this pass: the pad orb is prop 210, template 5, native (440, −10438), height 85, region 9806, and it has no events. Prop 96 on the same pad is not a ball. The only local-3 water store found then sits on prop 221 at the ice fountain, not on this pad. Fix: a new host on prop 210. Do not call group 37776. Do not grant the lichen from that greenhouse group. The 14 lichen rows stay the greenhouse planters until a producer for this pad is read. Nine clumps is the book's count.

## Not in code

| story | player, from the card and the hintbook | verdict |
| --- | --- | --- |
| 069 | Three towers other than the southwest, then push a box through the disk. HINTBOOK 4842–4847. | MISSING |
| 071 | Burn the oil under the head and take the bow. HINTBOOK 4913–4920. | MISSING |
| 072 | Blue bow on the fireball, imp or pyrapod spark on the white ball, hit the spinning brick. HINTBOOK 4824–4834. | MISSING |
| 073 | Four ivory chips, two of them possibly from the museum. Card page Prima 150. | MISSING |
| 074 | Four chip spots. Card page Prima 155–157. | MISSING |
| 075 | Southwest tower last: four chips on four pedestals. | MISSING |
| 076 | Box in the square hole, yellow eight-sided figure, one section rises. HINTBOOK 4848–4850 names the Starry Tower and the box. | MISSING |
| 077 | Fourth rise, fight, take the mantle from the bars of light. | MISSING |
| 078 | Chop the live dragon, not the picture, and take the teleporter only with the mantle. | MISSING |

Ids for 069 and 071–075 are already filed in `source_ids_066_075.md`. Ids for 076–078 are in `source_ids_076_085.md`. This pass did not re-read those packs. A fix is a host per card, in that order, after 068's prop 210. No new item id.

## Still open

Prop 210's shatter command. Whether the ice-fountain local 3 is the dry fountain's water. The yellow figure. Every tower after 070.
