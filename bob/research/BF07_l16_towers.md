# BF07 NE lift, SE route, SW field, centre

Intent: the NE lift carries Luther up, the SE oil opens a drain, four ivory chips show the SW field, and the centre foe can be killed without moving Luther.

Player contract: the greenhouse doors must already be open. Standing at the NE door quad sets at_doors and lifts Luther once to (16082, 100, 3886). Burning prop 392 still gives the Dark Bow and still does not move doors 80, 81, and 98. The chain save has no ivory chip, so the SW field stays hidden on that save. Placing four known chips through apply_place shows the field, and the save written for the centre test stays empty. At actor 45, Human form with a weapon drops the foe and opens a gate leaf. Luther stays.

Exact: doors 92-94, arrival words (16082, 100, 3886), prop 392, doors 80/81/98, pedestals and the five chip ids, pyramid 604, actor 45 definition 1282, door id still -1. Opcode 18 target u16 0 is not the player (I03). The centre regions do not move Luther.

Approximate: the NE rise contradicts that decode and is logged as an adapter. The drain mouth, the force field, the gargoyle, the ice fountain, the ceiling, the foe, and the Mantle Gate leaf have no placements. foe_down is an optional fourth key so a size-3 save still loads. The dragon room is not edited. It already calls use_exit on this base.

Proof: each earned test must show its visible result. The centre save must still carry at_bars and seen_actor for the dragon test. The SE burn flag must still be true for the NW chain. The SW save must still have empty pedestals.
