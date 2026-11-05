# MAP-MARK L4_HJ

Brady printed 153 lists the jungle items and the six must-steps. Printed 154 is the Hive Caves map, not a numbered jungle map. The jungle page has no point numbers 1–9 in the text that was read. `b-155.png` is printed 154, the hive.

Item rows are the geometry section at file 12409578. Count at +0x6C is 88. Offset at +0x20 is 605856. Stride 37. Identity at byte 32 matches item19. Names stay LIKELY.

Locals are the 41-byte run at file 13153135, 57 names. Slot 5 is `Imp_shrine`, 17 is `Gave_Dawn_Runes`, 23 is `Kityara_Given_Orb`, 37 is `Bacatta_accommpany_Luther_across_bridge`, 43 is `Bane_Bridge_destroyed`, 50 is `quicksand_bridge_destroyed`. The book's spelling is Baccata. The local spelling is Bacatta.

`markers.json` was `[]`. It now has 36 rows.

| place | marker |
| --- | --- |
| Cave aloe | 18 item rows, x −6374..2078, y −3117..4605 |
| Ironwood sap | (−2214, 4662) and (−2123, 4647) |
| Wax | (−1764, 5033) |
| Imp shrine | summon scroll (3015, 4178). Region 3329 stores `Imp_shrine`. Owner R78. |
| Kityara | control 83 (−3765, 2551) and control 0 (808, 1802), both store the orb and knife locals |
| Baccata | prop 552 (3592, 4145) stores the trigger and the bridge-accompany local. Prop 553 (61, 4135) stores the approach local. |
| Dawn | actor 63 (−5710, −3937) stores `Gave_Dawn_Runes`. Owner R72. |
| Bane bridge | prop 4648 (5683, 4197) stores `Bane_Bridge_destroyed` |
| Quicksand bridge | control 210 (1466, −1205) |
| Lightning, storm, ancients | the shop pile near (1889, 3855), the west cache near (−3834, 3888), and the north stones near (−2005, 5741) |
| Placed dagger | (−1629, 4932), not joined to Kityara's knife props |

Home-name cstrings exist for Kityara, Bacatta, Dawn, and the Wild One. Actor definition numbers were not joined to that 26-byte home table.

Still open: speaking stones, the beehive mesh under the wax row, the waterfall lightning crystal, the Wild One, the lizard cave to the hive, and a numbered jungle map. Kind 12 fire time was not entered. No frame was opened. Map.png was not regenerated.
