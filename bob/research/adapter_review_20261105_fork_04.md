# R2 adapter review fork 04, 2026-11-05

No Godot was run. No opcode callee was entered. The idle line still names ~/opus_work/lol2_r12y at 56812f9. These rows were read in ~/opus_work/lol2_r15 at f6a5aa4. All eight row files match the r12y copies.

## 0048 jungle

The row is pending. `jungle_causeway.gd`, `creature_region_barrier.gd`, and the causeway source match r12y.
DECODED: twelve floor records end at -200. Region 4445 goes from -114 to -134.
Preset 42 is stored on eleven regions. Records 4426, 4428, 4434, and 4438 are already -200 on both sides.
Controls 61 and 62 link. Control 84 unlinks. Its box is template 24, height 60, child 47 bounds 0 through 60.
Regions 4429, 4448, and 4447 refuse creatures and leave the player through.
The host shows those final floors when an ending queues group 17352. A played ending with no causeway entry loads collapsed.
Eight props use `prop_755.png`. Records 507, 509, and 4162 unlink. Records 4161, 508, 506, 4181, and 4160 move to the stored x/z at their own height. Template 39 stays the row.
HINTBOOK lines 2416–2420 walk Bacatta to the bridge and name a shore video. Those lines print no collapse.
BRADY lines 3499–3507, marker PDF PAGE 87 = printed 86, say Hive Warriors destroy the bridge after the escort. Those sentences stay apart.
Both books print no -200, no 20, and no 60. The row's mover at 65BB0 stays unread.
The shake and movables 59, 60, 62, and 63 stay open. The settled floors stay the row.

## 0049 jungle

The row is pending. `jungle.json` matches r12y. The sunken-clip function is the row's rule.
The r15 diff in `jungle_review.gd` is a jump speed.
DECODED: floors 1902 and 1905 sit at 0. Thirteen ids in 3314–3335 sit at -500. Nine sit from -140 to -95.
Eighteen wall faces in that span have a top above -10, and the tall faces reach 400.
The Jungle host turns the clip on. `darker_jungle.gd` inherits that init. This review did not count a Darker Jungle group.
The headless test source expects 18 gorge walls drawn to -10 with collision kept.
LONGPLAY 36:40–38:10 stays the row's witness.
HINTBOOK lines 2309–2310 name a waterfall and a boulder shrine.
BRADY lines 2815–2823, marker PDF PAGE 73 = printed 72, name a waterfall movie, a cave, and a Speaking Stone.
Those sentences stay apart. They print no -500, no 400, and no 18.
The drained-channel view stays open. The draw clip stays the row.
PROPOSE narrow gorge floors to the 13 regions at -500 | jungle.json | the 18-wall clip to -10 stays.

## 0050 darker jungle

The row is approved. The assemblies file matches r12y.
DECODED: L8 placement 99 is template 8 at (-4433, -1173), with four faces of material 874.
`static_collision_L8_SJ.json` has no box 99. The row's word8 bit 0x80 stays the row's sentence.
r12y `darker_jungle.gd` opens only assembly 99.
r15 `OPEN_ASSEMBLIES` is 99 and 111, and `include_collision_face` also drops faces `l8_tree.gd` owns.
Assembly 99 stays drawn and open.
A search of both books printed no vine arch and no assembly 99. Books print no such index.
The approved removal stays the row for assembly 99.
Facade 111 and the tree door stay on the later host notes.

## 0051 jungle

The row is pending.
DECODED: the first visit sets flag 152 and plays `CHUT_FIRST`, fifteen durations.
Flag 151 is written at cursor 8. `Met_Kelsrick` is written at cursor 12.
Luther is then placed at (-1769, -5464), heading 150, yaw equal to degrees minus 90.
The dead branch raises the alert, sets flag 153, and plays `CHUT_DEAD`.
The same room file hosts `CHUT_ATTACK`, `CHUT_KILL`, stone flags 154–159, and the refusal lines.
Rows 0093–0096 already record those branches. Host 0xF0 stays unread.
LONGPLAY 61:35–62:56 stays the row's witness.
HINTBOOK lines 5682–5685 say killing Kelsrick yields the thief's sword and Ancients' Stones after a switch.
BRADY lines 3063–3071, marker PDF PAGE 79 = printed 78, name Anyar, Kelsrick, and a gate lock until he dies and a switch or the den tunnel opens.
BRADY lines 6737–6741, marker PDF PAGE 158 = printed 157, say you can meet Anyar and kill Kelsrick for Firestorm.
Those sentences stay apart. They print no line numbers and no coordinates.
Ambient 338, the speaker 29 hotspot, and control 100 events 5 and 6 stay open.
Rendered qualification of the dead branch stays open. The first-visit place stays the row.

## 0052 cave museum dark halls

The row is pending.
`dark_halls.gd`, `museum_skeleton_population.gd`, `cave_wild_roach.gd`, and `cave_lurking_roach.gd` match r12y.
DECODED: Rat look is radius 16 and height 32. ROACH and WORM are radius 13 and height 26.
The shared scale is about 0.21818. The capsule is the movement body and the aim target.
The r15 diff in `scripted_creature_population.gd` is a shared aim label and a peaceful-actor gate.
The radius formula stays. The native actor hit size stays unread.
BRADY lines 2420–2426, marker PDF PAGE 65 = printed 64, describe a cave cockroach the size of a sofa.
Those lines print no 16, no 13, and no 6.
The hintbook search printed no such radius. The sprite capsule stays the row.

## 0053 jungle

The row is pending. `jungle_beehives.gd` and `jungle_harvest.gd` match r12y.
DECODED: E with a carried hand item clears that hand.
The empty-hand harvest then grants wax, aloe, or sap into the pack and the hand.
A failed grant leaves the hand as it was. A hand item absent from the pack is refused.
The barrel grant is aloe. The plant and the barrel each stop at three takes.
HINTBOOK lines 2383–2384 say click a bee hive for wax.
Lines 1154–1156 say strike gray-barked trees with a blade for sap. Lines 1111–1112 say pick aloe from bushes.
BRADY lines 2759–2769, marker PDF PAGE 72 = printed 71, say click a hive, click twice, attack an ironwood trunk, and collect three leaves from each aloe tree.
Those sentences stay apart. They print no "puts away" and no kind4 mode.
The stow stays the row. The native empty-hand refusal stays the row's source sentence.

## 0054 hive monastery

The row is pending. `hand_selector_order.gd` and `hive_rune_entry.gd` match r12y.
DECODED: `wanted_first` lists the wanted ids in carried order, then the rest in carried order.
The RUNECL selector asks for wax. The monastery selector asks for rune copies.
HINTBOOK lines 2696–2697 say take wax and click it on the runes.
BRADY lines 3276–3279, marker PDF PAGE 83 = printed 82, say use the wax on the engravings and get two impressions.
Those sentences stay apart. They print no list order and no 19.
The owner's report of 19 carried items stays the row's witness.
The ordered selector stays the row. The original held cursor stays unbuilt.

## 0055 jungle hive

The row is pending. Kelsrick `CLIP_SCALE` stays 0.235. His population look stays 0.47.
The r15 diff on that file is voice unit size 300.
Dawn's Jungle and Hive scripts use `BODY_SCALE` 0.282 and `CLIP_SCALE` 0.141.
Row 0110 already records that height, about 44 units against the player's 46, and calls it the completion of this owner report.
Bacatta, the exit woman, and the exit-guard pose stay at 0.47. The guard look canvas is 400 by 248.
LONGPLAY 99:46–101:06 and 61:20–61:50 stay the row's witnesses.
The books print no 0.235, no 78, and no 1.8.
The row's 1.8 m sentence and row 0110's 1.5 m sentence stay two sentences.
The native clip scale stays unread. Kelsrick's 0.235 stays this row. Dawn's height stays row 0110.

## Receipts

- 0048 jungle: Causeway row matches r12y. Twelve floors end at -200, region 4445 drops 20, and control 84 is 60 high. Brady says Hive Warriors destroy the bridge. The hintbook prints no collapse. The mover, shake, and four movables stay open.
- 0049 jungle: Gorge row matches r12y. Floors 1902 and 1905 sit at 0. Thirteen of 3314-3335 sit at -500. Eighteen walls rise past -10. Books print no such heights. The longplay stays the witness. The drained view stays open.
- 0050 darker jungle: Vine arch 99, template 8, material 874, has four faces and no collision box. The row matches r12y and stays approved for that arch. r15 also opens assembly 111 and the tree-door faces. Books print no arch index.
- 0051 jungle: CHUT places Luther at -1769,-5464 after the fifteen-line talk. The dead branch is hosted. Attack and stones are hosted past this row. Books print no coordinates. Ambient 338, speaker 29, control 100, and unread 0xF0 stay open.
- 0052 cave museum dark halls: Rat capsules are 16 by 32 and roach and worm capsules are 13 by 26. The row matches r12y. Books print no such radius. The native hit size stays unread.
- 0053 jungle: A carried hand item is stowed, then wax, aloe, or sap is taken. The row matches r12y. Books say click the hive, strike the sap tree, and pick aloe. They print no puts-away line.
- 0054 hive monastery: The Hive inscription lists wax first and the monastery rooms list rune copies first. The row matches r12y. Books say click wax on the runes and print no list order.
- 0055 jungle hive: Kelsrick's talk clip stays 0.235. Dawn's body 0.282 and clip 0.141 stay on row 0110. Bacatta, the exit woman, and the guard pose stay at 0.47. Books print no 0.235. The native clip scale stays unread.
