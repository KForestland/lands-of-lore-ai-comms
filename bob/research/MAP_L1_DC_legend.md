# MAP-MARK L1_DC

Brady printed 145 is the cave map (points 3–9). Printed 146 is what can happen. Printed 147 is the item list and the four must-steps. Museum printed 148 is L3, not this level.

Static names are the 30-byte run at file 7415073, name at byte 0. Slot 25 is `Small crate` and slot 43 is `Push box`. Prop template names are the 38-byte run at file 7401491, name at byte 0. Index 63 is `aloe`, 67 is `breakoff`, 77 is `Orc Door`, 78 is `Morph React`, 83 is `Kenneth Speech`. Local names are the 41-byte run at file 7362921. Slot 4 is `First_morph`, slot 34 is `Lizard_Trigger`, slot 50 is `Aloe`, slot 51 is `Orc_Conv`. Name-at-index stays LIKELY.

Item rows are the geometry section at the L1 geometry entry file 7091978. Count at +0x6C is 26. Offset at +0x20 is 231028. Stride 37. The identity dword is at byte 32 and matches item19's definition identity. The name on that index stays LIKELY. The word at byte 10 was not called a region. Coordinates are the signed words at bytes 0 and 2. Height is the signed word at byte 6.

`markers.json` has 34 rows. It was `[]` at the start of this pass, then seven legend rows, and this pass added the rest.

| Brady point | where |
| --- | --- |
| 3 Waterfall Grotto | control 88, slot 36, (−210, 4656) |
| 4 Move pillar / must-step 3 | controls 0 and 1, slot 43, y 10758 |
| 5 Old Orc | control 136, slot 20, (1452, 12257). Groups store `Orc_Conv` and `Orc_Dead`. |
| 6 Crates | controls 94–122, height −215. Maces are the item rows above them. |
| 7 Fire pit | controls 92 and 93, slot 40, y 14830 |
| 8 Bridge | movables 56–61, slot 49 |
| 9 Doors / must-step 4 | Port Door movables 68 and 69, Iron Gate 70, 71, 73 |
| must-step 2 morph | region 631 center (−521, 6093) stores `First_morph`. Owner R7 is (−550, 6084). |
| Cave Aloe | props 791, 792, 793, template 63. Opcode 3 identity 0xDE73C93C. |
| Orc maces and shield | item rows at (417, 12444), (471, 12480), and the shield at (421, 12480), height −130 |
| Ancient Magic Stone | prop 1050 (1356, 11738). Orc Door is prop 544 (1216, 11501). |
| Halberd, hand axe, shield | item rows (113, 10489), (308, 10718), (88, 10740) |
| Mana Foil | control 75 Plank (209, 10691) height −1000, group 9768, identity 0xC221EB6B |
| Guardian Sphere, Pyra Pod, Light Crossbow | item rows (297, 16702), (329, 16631), (311, 16717) |
| Green crystals | props 144–149 and 641, template 67, opcode 3 identity 92534515 |
| Kenneth | prop 456 (158, 16640) |

Actor 53, definition 2, at (159, 12009) is not the orc. Prop 343 grants a kit (aloe, halberd, guardian orb, pyra pod, light crossbow, ancients stone) and was not marked. Nine mana-foil opcode 3s have no object owner. Template 93 `Mana foil` has no prop.

Still open: the waterfall flood command, the push-box move command, which door command opens the chamber, kind 12 fire time, the orc-door chain command, the giant cockroach's name, and actor definitions 769 and 770. No longplay frame was opened. Placements were read from the JSON and from the geometry item rows. They were not re-matched against a second copy of the MIX.
