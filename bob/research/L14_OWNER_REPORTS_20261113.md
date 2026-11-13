# L14 owner reports, six Temple stands (2026-11-13)

Read-only. Godot was not run. Nothing was built. The guard list was not edited. This is not a geometry move and not a spell change.

Build the owner played: playtest/r19f, dacf858, normal play from the Savage Jungle F2 start. The six rows are in playtest_feedback_20261023/TRIAGE_r19f_20261113.md. Report order below follows the board: plants, armor, spider, hidden wall, door, priest stop. A report coordinate (x, y, height) is Godot (x, z, feet). A plan hit is standing only when the feet sit between that region's floor and ceiling.

Grades. PROVEN is a port line that runs, or a book line that was read. LIKELY is a source record whose shape matches a decode that was read, without the matcher being run on this level. UNKNOWN is a command whose body was not entered. The native dump scripts/lol2/native_scripts/L14_HT.json says itself that it does not claim opcode effects. Opcode meanings below are only the ones named in docs/jungle-harvest.md or in a port script.

Chain means the Huline Temple main chain: tests/l14_temple_chain_a_test.gd then tests/l14_temple_chain_b_test.gd. Optional means neither header names the spot.

## 1. Plants. Report 01-15-26. (651, -4143), feet 40. "this grows plants"

Standing. Region 3007, floor 8, ceiling 120, flags 512. Feet 40 are inside it.

Nearest rows, plan distance from the stand:

- static assembly 54, template 87, source 54, at (609, -4139), height 0, distance 42. Same record as control 54.
- prop 82, template 58, selector 0, region 3008, material prop_78, at (607, 0, -4139), 211 by 157, distance 44. The published frame is one small green sprout on a black field.
- static assembly 53, template 88, source 53, at (570, -4139), height 0, distance 81. Same record as control 53.
- static assembly 52, template 89, source 52, at (566, -4140), height 39, distance 85. Its plan point is in region 2950 (floor 42, ceiling 103). Same record as control 52.

These four records point at each other. Prop 82's list, native_scripts/L14_HT.json:

- kind 2 value 128, group 428: opcode 9 on prop 82, raw 090352001500
- kind 6 value 20, group 440, predicate 206: opcode 5 on prop 82, argument 1
- kind 6 value 2, group 446: opcode 16 argument 1, opcode 9 on control 54, opcode 5 argument 2
- kind 4 value 0, group 470, predicate 207: opcode 16 argument 2, opcode 3 raw 03010000a3ccddbf04000000, opcode 5 argument 3
- kind 4 value 0, group 500, predicate 208: opcode 16 argument 3, the same opcode 3, opcode 5 argument 4
- kind 3 value 4, group 530: opcode 16 argument 4, opcode 14
- kind 6 value 20, group 550, predicate 210, and group 568, predicate 208: opcode 5 and opcode 16 stepping back through 3, 2, and 1, plus opcode 14

The identity bytes a3ccddbf are item identity 3218984099. That is act2:L14_HT:item68, definition 109, name 107-Aloe, at (2950, 10, -4609), region 140. docs/jungle-harvest.md says an aloe plant grants 107-Aloe with opcode 3 property 4, and uses opcode 16, opcode 5, and opcode 14 for state, selector, and timers. This level's matcher was not run, and these commands were not matched byte for byte against a jungle plant, so the grant is LIKELY and the timer length is UNKNOWN.

Control 52 group 16520 also has opcode 196 on region 2950, raw c490860b2700000000000000. The height word is 39 and the following word is 0. Region 2950's floor base is 42. Assembly 52 is placed at height 39. What that command does to the floor was not executed.

No l14 script contains the words plant or grow. act2_world_items.gd does not hide or show a plant here. The pew aloe, item 68, is a different row and is the one chain A picks up.

Books read this pass do not put a growing bed at (651, -4143). Hintbook 4342-4343 puts poison and aloe on the raised end of the pew room. Brady 8129-8130 says kneeling before the Gods of Life or Death gives an Aloe Leaf or a Poison Plant, and that line was not tied to this coordinate.

Chain or optional: optional. Chain A and chain B do not name this bed.

## 2. Armor. Report 01-16-00. (1026, -4359), feet 32. "should be an armor thing here or item"

Standing. Region 1202, floor 0, ceiling 100, flags 512. Feet 32 are inside it.

The item row is act2:L14_HT:item71, flags 2, region 1185, definition 43, name 44-Platemail, handler 0, grade LIKELY in act2_items_source.json. Position (1000, 0, -4283). Plan distance 80. Region 1185 is floor 0, ceiling 100, flags 514, so the item sits on the same floor height in the next region, not under the floor.

act2_world_items.gd places every L14 item row as a sprite and has no extra hide for item 71. The icon file assets/lol2/generated/items/icons/043.png is present. Pickup range in that script is 96 with a facing dot above 0.97. Whether the sprite read as armor from his stand was not rendered.

Four static assemblies, template 37, source indexes 117, 118, 119, and 120, have empty event lists. Nearest is 119 at (992, -4308), height 15, distance 61. The others are 118 at (1132, -4310), 117 at (994, -4475), and 120 at (1132, -4474), all height 15. No script names them. Their mesh was not opened, so they are not labeled armor stands here.

Books read this pass do not list platemail as Temple loot. Brady's Temple "things to get" (8098-8120) names aloe, poison paint, stones, scrolls, the flute, shards, the statuette, and the idols, and does not name plate mail. Hintbook 1548-1550 puts a platemail breastplate in the Hive executioner's nest. Brady 7728-7736 puts reflective plate mail in a Cemetery mausoleum. Those lines are other places. They do not remove the L14 row.

Chain or optional: optional. Neither chain header names platemail or these four assemblies.

## 3. Spider trap. Report 01-17-14. (1355, -5298), feet 32. "spider trap here"

Standing. Region 2703, floor 0, ceiling 160, flags 512. Feet 32 are inside it.

The wall is static assembly 64, template 78, source 64, at (1351, -5396), height 0, distance 98. That is the point in l14_spider_passage.gd (Vector3(1351, 40, -5396)). He is inside the script's 150 wake radius. The same index is control 64.

Actor 68, act2_populations/L14_HT.json: definition 2, position (1364, 0, -5442), health 1500, behavior 14, present true. Plan distance from the stand 144, further down the corridor than the wall.

Port today, l14_spider_passage.gd. The wall stays solid until l14_hanging.opened is true and the player is within 150 of the point. Then it hides, wakes actor 68, and says "The wall crumbles. An arachnopod emerges." A 12 second respawn is marked in that file as a modern adapter, not a decoded interval. The wake also requires the hanging, and the hanging requires the ritual to have vanished the body (l14_hanging.gd). His priest question is the earlier report 01-14-29, so this stand can be the corridor before that gate has opened. The script then does nothing. That was not replayed from his bundle.

Native, control 64: kind 6 value 20, group 16852, predicate 206 (opcode 20 on actor 68, opcode 16 and opcode 7 on control 64); kind 6 value 2, group 16880 (opcode 9 on control 64, opcode 9 on actor 68). Actor 68: kind 6 value 9, group 21252, and kind 6 value 20, group 21260, both opcode 13. Those bodies were not entered. UNKNOWN as opcodes. The book sequence is the behavior:

- Hintbook 4384-4385: click the left wall hanging to uncover the passage.
- Hintbook 4414-4416: past the body-zapping room, a wall crumbles and the spiders come out.

Chain or optional: main chain. Chain A step 7 walks l14_hanging_spider.json and checks actor 68 dead. The burrow at the other spider comment in l14_spider_burrow.gd is a different spot and is not this wall.

## 4. Hidden wall. Report 01-18-16. (2212, -5268), feet 152. "hidden items behind this wall"

Standing. Region 2340, floor 120, ceiling 190, flags 512. Feet 152 are inside it. The same plan point also falls in region 2358 (floor 10, ceiling 100), and the feet are above that ceiling, so he is not standing in 2358. Region 2358 is the crack ceiling the bedroom script owns.

The wall is the headboard. Movable faces:

- movable 0, template 40, at placement (2264, source y 5312, height 120). Faces x 2256..2272, y 120..190, z -5353..-5271.
- movable 1, template 41, at placement (2264, source y 5230, height 120). Faces x 2256..2272, y 120..190, z -5271..-5189.

Together one panel at x 2256..2272, from z -5353 to -5189, between heights 120 and 190. His x 2212 is 44 west of that panel, his z -5268 is inside the panel's z span, and feet 152 are inside its height. He is against the west face.

Both movables have empty event lists. Prop 8, template 26, material prop_1060, at (2245, 115, -5209), region 2354, is the bedroom point. Its two kind-4 records pose the panels: group 116 sets opcode 1 on movables 0 and 1 to 0, and group 146 sets both to 100 (raw 012000006400 and 012001006400). Which predicate lets which record run was not decoded.

Items on the east side of the panel, both flag 2, both placed by act2_world_items.gd with no extra hide:

- item 2, act2:L14_HT:item2, definition 68, name 66-Ancients stn, handler 6, (2325, 140, -5234), region 4188
- item 3, act2:L14_HT:item3, definition 167, name Cocos Cap, handler 103, (2322, 140, -5322), region 4192

Red pillows prop 348 and prop 349, material prop_1051, are within 40 of the stand and have no events. They are the bedroom dressing, not the hidden items.

Port today, l14_bedroom.gd. E at Vector3(2245, 145, -5209), reach 145, slides movables 0 and 1 on z. His stand is about 68 from that point, so he is inside the reach if he is facing it. The script refuses with "Find the passage first." unless l14_hanging.opened is already true. The prompt when it allows the push is "E - Push headboard".

Books: hintbook 4477-4479 names the red-pillow bedroom, and hintbook 4516-4517 says push the headboard to reveal a secret area with goodies. Brady 8166-8167 says click a bedpost in the priest's bedroom to open a secret room. The book order does the left hanging first (hintbook 4384) and the headboard much later. The port's hard refusal until the hanging is open is the script's own gate. The native predicates on prop 8 were not read as that same lock.

Chain or optional: main chain. Chain B walks the headboard, the hop behind the altar, and the crack, and it does that after chain A's hanging.

## 5. Door. Report 01-18-59. (2413, -3064), feet 52. "cant open door"

Standing on the upper floor. Region 786, floor 0, ceiling 80, flags 33280. Feet 52 are inside it. The same plan point also falls in region 781, floor -80, ceiling 20, and the feet are above that ceiling. He is not in the lower crawl. Chain A's lower-passage check wants the body below -40 near z -3046. This stand is the upper pair.

The leaves are movables 92 and 93, both template 1, placement height 0, at source (2447, y 3027) and (2376, y 3027):

- movable 92 faces: x 2412..2483, y 0..80, z -3029..-3025
- movable 93 faces: x 2340..2411, y 0..80, z -3029..-3025

They meet at x 2411/2412. Together they cross x 2340..2483 at about z -3027, up to height 80. He stands at x 2413, on that seam, 35 units south of the leaf. The next static assembly is 105, distance 141, so this pair is the door.

Both movable records have empty event lists. No opcode 1 of kind 32 in the L14 group stream targets 92 or 93, so act2_progression.gd mover_ids does not build a hinge for them. Commands whose target number is 92 or 93 in that stream are prop, actor, or control rows of those indexes, not these two movables.

Port today, l14_temple_doors.gd. It draws this pair and has no E. restore() hides the mesh and clears its collision only when l8_temple_door_state.unlocked is true, which is the committed slot temple:entrance1198. That slot is the jungle entrance in l8_temple_door.gd: place the Dreamstone, take it back, then enter. Chain A starts from that earned arrival and checks that this gate is already hidden. A player who still sees the leaves has that receipt unset, and nothing on the leaves themselves opens them.

Books: hintbook 4306-4308 says use the Dreamstone to enter the temple. That sentence is the jungle entrance. It does not name an interior pair. The chain's reading, that these leaves are the main doors the receipt leaves open, is the port and the test, not a decoded command on movable 92 or 93. Grade of the entrance link: LIKELY as the chain uses it. Grade of a native pose on these two movables: UNKNOWN, because no command in this stream targets them.

Chain or optional: main chain. Chain A step 1 requires the pair already open. They are not the trial doors 88, 89, and 90, and they are not the ritual spark point, which shares x 2413 but sits at z -3328.

## 6. Priest stop. Report 01-14-29. (2320, -3691), feet 52. "stops here; I need to complete priest ritual?"

Standing on the upper ritual floor. Region 809, floor 0, ceiling 95, flags 520. Feet 52 are inside it. The same plan point also falls in region 3241, floor -80, ceiling 20, and the feet are not in that lower room. He is already in the ritual room, at the altar end. The slab is Vector3(2413, 2, -3328), about 370 units north. This is not a door in front of the ritual.

Nearest rows:

- west bowl, the aloe bowl. Prop 370, template 15, material prop_694, (2375, 27, -3691), region 806, distance 55. Static assembly 68, template 76, sits at (2374, -3691), height 25. l14_priest_ritual.gd bowl "370" is Vector3(2375, 30, -3691) and accepts act2:L14_HT:item68.
- left hanging. Static assembly 124, template 49, source 124, at (2260, -3706), height 0, distance 62. That is control 124 and the point in l14_hanging.gd, Vector3(2260, 45, -3706), reach 145. He is inside that reach if he faces it.
- east bowl, the poison bowl, is further: prop 369 at (2441, 27, -3691), distance 121. Bowl "369" accepts item 72.

The lead's question: is this the gate before the ritual? The hanging is the gate, and it opens after the ritual, not before it. He is on the ritual-room side of it, next to the west bowl.

Port today:

- Bowls refuse until l14_priest_body phase is "placed" ("Place the priest on the stone rectangle first."). Offering both lowers the floor list in l14_priest_ritual.gd. Spark at (2413, 9, -3328), charges 1 or 3, after the floor has finished, sets vanished and removes body prop 274.
- The hanging then accepts E. Until vanished it says "Complete the priest's ritual first." The prompt is "E - Draw aside left wall hanging".

Native floor commands match that port list. Prop 369 group 14556 and prop 370 group 14868 are each 23 opcode 196 commands on 22 regions (region 821 is listed twice). The height words are -10, -20, and -30, the same regions and the same three heights as the FLOORS dict in l14_priest_ritual.gd. docs/l14-priest.md says the native drag and the opcode join were not entered, so the click that runs those groups is the port's E adapter, not a hosted opcode. Body prop 274 has its own kind-10 and kind-2 groups (12754, 12774). Those bodies were not entered.

Books, this room: hintbook 4348-4367, aloe in the western bowl, poison in the eastern bowl, the floor descends, Spark on the body, the body disappears. Hintbook 4384-4385, then click the left hanging. Brady 8124-8136 is the same order: bowls, drag the body, lightning, then the tapestry left of the altar. Brady also says a second pair of bowls further east. That second pair is not this stand.

Chain or optional: main chain. Chain A is body, pew aloe and poison, these two bowls, Spark, then this hanging, then the spider corridor.

## Chain against optional

- Plants, prop 82 and controls 52, 53, 54: optional. LIKELY an aloe harvest. No port script.
- Platemail item 71 and assemblies 117-120: optional. The item row is placed. The four assemblies have no events.
- Spider wall, control 64 and actor 68: chain A. Port waits on the open hanging.
- Headboard, movables 0 and 1, items 2 and 3 behind them: chain B. Port waits on the open hanging.
- Main doors, movables 92 and 93: chain A. No E. Hidden only by the Dreamstone entrance receipt.
- Priest stand: already the ritual room, chain A. The hanging beside him is the way on, after the ritual.

Godot was not run. No bundle was replayed. Q13 stays parked.
