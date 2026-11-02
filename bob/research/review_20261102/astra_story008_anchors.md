# Anchors for Astra's 02:50:00Z question

2026-11-02. STORY-008 through STORY-027 placement IDs. No DOSBox. No Godot. Assembly names are the 30-byte table after the 60-byte template records, one name per template index. The tomb card's templates check that order: template 22 is Cool Door, template 44 is Stand alone gargoyle, template 50 is White Designator, template 51 is Yellow Designator. Prop names are the 38-byte table, index equal to the prop template. Item rows are G93 evidence.json. A destination byte on opcode 2 stays unread. Adjacent arrival labels stay unbound.

## L10 entrance and braziers

No control, movable, or prop template is named Stair. The texture entry string Stair Step at file 404133 is not a placement.

The south entrance mesh is control 65, template 57, Cemetary Gates, native (-154, 29, h0). Region 0, centroid (-152, 66), owns opcode-2 body 020100001c48. Arrival selector 1 is (-150, 221), region 5.

The courtyard braziers are control 113 at (-627, 842, h29) and control 114 at (-534, 935, h29). Both are template 42, Brazier for Maus. Prop template 23, Bone Brazier, is the lower-floor set and is not these two.

The sigil gate stays control 70, template 45, Gate Lock, (-125, 1019, h14), with movables 70 and 71 the Gate leaves and movables 72 and 73 the latches. Control 67, Freeman's gate, is at (-127, 1148, h14).

Region 42, centroid (-646, 953), floor 30, owns opcode-2 body 020100001c69, predicate 63. That is the level-change west of the gate. Brady printed 184 point 3 draws the teleport there. Predicate 63 and byte 5 stay unread.

## L9 bridge and orb

Magic Bridge controls are 466 at (-1364, 1803, h13) and 467 at (-1586, 1802, h13), template 29. The nearest prop named Drac Orb is prop 1086 at (-1888, 1267, h0), template 11. Prima's word is black. Brady printed 179 point 3 says Dragon's Orb and Bridge. The template name is Drac Orb. The spark command that would tie prop 1086 to controls 466 and 467 was not read.

Other plain Drac Orb props are 2541 (2510, 3078), 2549 (1883, 3149), 2686 (-2089, 7321), and 2687 (-1805, 7320). They are not the pair next to that bridge.

## L9 tower field, altar, bracers

Assembly template 101 is named Forcefield. No control, movable, or prop placement uses template 101.

Green Drac Orb props next to the white altar are 1087 (-3820, 1037, h270), 1088 (-3750, 1126, h130), 1089 (-3793, 1093, h400), and 1090 (-3661, 863, h0). They stay Green Drac Orb. They are not renamed to the force field.

The white altar stays prop 1094, template 64, Charger Station, (-3656, 833, h150).

The bracers are item row 55, slot 58-Br dead, (-3764, 802, h430), region 4722, dormant bit clear. No template is named niche. Brady printed 180 point 7 is that level-3 placement. Gauntlets, slot 48-Gau Might, are item row 53 at (-3257, 1028, h-110).

## L9 cremation

Funeral Pyre is control 301, template 59, (10882, 12569, h140). Fire for Pyre is controls 299 and 300. More Fire for Pyre is controls 236 and 237. Dead Priest is prop 2406, template 9, (10538, 12996, h140). Brown Drac Orb props are 1205 (10737, 12586, h140) and 1206 (10871, 12711, h140). The urn row is item row 0, slot Fullurn, (11129, 12729, h0), region 6752. Brady's dragon-orb pedestals and Prima's cremation sparks use those placed orbs. Brown is the template name and was not recolored.

## L9 remains bowl and flood exit

No template is named bowl or remains. The editor marker Statue's Home is (4135, 10151), region 5945. Prop 104, template 32, Inviso Light, at (2672, 10506, h10), owns opcode-2 body 020100001ca8. That owner is a prop event, value 304. It is not a bowl.

Water fog is control 104, template 115, (2647, 9595, h-17). Little Bridge is control 99 at (3006, 9845, h32). Bridge with no supports is movable 56 at (3007, 9325, h225) and movable 57 at (3272, 8589, h-7).

Region-owned level changes, destination byte unread:

- Region 2299, centroid (-3220, 8228), floor 200, body 020100001c4a. Control 304, Teleport to 10, is at (-3215, 8228, h200).
- Region 2301, centroid (-3027, 8381), floor 200, body 020100001cc8. Control 154, Teleport to Ruins, is at (-3027, 8372, h200).
- Region 5340, centroid (7316, 1785), floor 10, body 020100001ce8.

None of the three was selected as the flood exit. The flood note strings were not executed.

## Grade

DECODED for the template names and the coordinates above. BRADY for printed 179, 180, 184, and 185. HINTBOOK for Prima's black orb, stair, and cremation wording. The orb-to-bridge command, the force field, the bowl, and the flood-exit choice stay UNKNOWN.
