# BI06 Kityara walk-up

The figure at the owner's pose is Kityara, control 0. Dawn63 is a different body. The volume change is a presentation adapter on Kityara's existing start regions. The source polygons are unchanged.

## Duck

1. Owner r18, build act1_opus_20261108_r18, F10 15-24-21, Jungle (669,-1590). A walk missed the speech. A jump reached it. The task named her Dawn.
2. On the chain as a reveal after the shop meeting. Missing the walk-up lets the player pass the line. The volume is presentation. The group that runs stays the native one.
3. Intent: reveal. Walking up to the woman in the first clearing starts her line.
4. Contract: Met_Kityara is already set (the shop does that; the walk does not). Runes are translated. She is alive. Walking toward her, with no jump, starts the talk once. She holds, the line plays, and the same start commands run. A second entry does not restart it.
5. Exact: predicate 151 (local 21 is 0, shared 14 runes translated is 1, shared 25 she is not dead is 0, local 35 Met_Kityara is 1). Location 0 start regions 1257, 1315, and 1324 run groups 1802, 2074, and 2154. Those commands set local 21, hold 0x26, and reposition. Presence and unlink regions stay on the exact polygon. Dawn's regions stay exact. Approximate: how far around those start tiles still counts as walking up.
6. Cheapest faithful: keep the native polygons and the same groups. A start region also accepts a foot within 96 of its polygon and up to 48 above the native floor. A new region id, or a change to Dawn, would miss this pose.
7. Earned walk, no jump, from outside that pad to (669,-1590). The runner recorded a pass and exited 0. The three existing Kityara tests (state, live, hostile) are the check that a centre of a native tile still starts and that an unmet start still refuses.

## Pose

Report `report_2026-11-08T15-24-21_2969347404`. Camera Godot (669.03, 42.05, -1590.61). Jungle `native_translation` is 0. The player stands on floor region 1323, foot on y=0. Diagnostics already had `collected[jungle:kityara:Empty_hand]=1`, so the jump had fired the talk before the shot.

Control 0, template 57, movie E066E.VQA, stored (808, -14, -1802). Planar distance about 253. Prop 64, the dropped knife, is at (837, 3, -1786). Actor 42, a Huline cub, is at (1208, 0, -1972), farther along the same look. Grade DECODED for the control and the regions. Source `jungle_kityara_source.json`, DAT/L4_HJ.MIX sha256 517afe6d59a4a06212bf4aea7eb42dfbb07826a4677fb77a4032674e64657e8f.

Dawn63 is actor definition 8 at (-5710, -100, 3937), about 8440 away, present false until region 2812. Her floors are -100 or -70. A jump at this pose goes up, away from that band. She is not this trigger.

The straight walk from (669,-1590) toward her crosses regions 1323, 1322, 1321, 1320, 1319, then her floor 3767. None of those is a start region. Region 1324 is the nearest start tile, 67 units back the other way, south of the pose. Its floor is 0, the same as the path. The old band already contained a standing foot (floor-4 through floor+6). The miss is horizontal. Jump launch 200 and gravity 320 cover about 67 units while the foot is still in that band.

## Adapter

In `jungle_kityara.gd`, start regions only. Foot may sit from floor_min-4 to floor_max+48. A point inside the native polygon, or within 96 of an edge, enters and calls the same `State.enter_region`. Other regions stay on the exact polygon and the old band. Location 83's start regions use the same list, so the same pad applies there. Predicate 151 still gates the group. Ledger piece 0347.
