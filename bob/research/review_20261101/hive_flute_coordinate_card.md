# Hive flute coordinate — behaviour card

2026-11-01. Answers the 17:14:15Z question that blocks HIVE-FLUTE-FLOOR. No DOSBox. No Godot. Prima printed folio = form-feed index minus 12, the same count the Hive six cards already use: the oil-spill sentence is form-feed 90, printed 78. Brady pages stay the ones checked for those cards. Grades are LIKELY, UNKNOWN, HINTBOOK, or BRADY.

## Answer

The owner's 10-26-06 coordinate is the top-floor pit lip, region 225, on the storey where the flute summons the lift. The oily-floor slot is a different room. The L5 and L14 exports do not name that room.

## (1) The coordinate

Source. Owner note 10-26-06, "this birge slides out when you use the flute". Map (-2352.037109375, -7609.46142578125, h -202.952514648438). Native x is the map x. Native y is the negation of the map y: (-2352.037109375, 7609.46142578125, -202.952514648438). Item 11 report, flute section.

Player action. Stand at the open pit on the top floor and use the flute. Prima printed 77: the hall leads to an open pit, and the flute summons the elevator. Eight squares, the current floor already selected.

Geometry, remeasured from hive_geometry_20260914/geometry.json. Vertices are 16.16 fixed, divided by 65536. Region 225 floor_base -235, ceiling_base -107, neighbors 242, 248, 245, 776. Corners: (-2370, 7695), (-2240, 7696), (-2240, 7536), (-2371, 7536). The bbox is x -2371..-2240, native y 7536..7696, which is the quad in the 17:14:15Z line. The owner point is inside the quad. Height -202.952514648438 sits between floor -235 and ceiling -107.

Region 776 is the shaft. floor_base -2000, ceiling_base 0, neighbors 773, 775, 225, 777. Corners include (-2484, 7575), (-2484, 7653), (-2370, 7695), (-2371, 7536). The shared corners with 225 are (-2371, 7536) and (-2370, 7695). The owner point is outside 776.

Trigger 282 in r12w assets/lol2/generated/hive_elevator/elevator.json is floor -235, polygon (-1896, -7696), (-1900, -7556), (-1984, -7536), (-1984, -7696). Same storey, and the owner map y -7609.46142578125 is inside that polygon's y band. The polygon's nearest x, -1984, is 368.037109375 units toward less-negative x from the owner. The owner is outside the polygon.

Region 234's quad also contains the point. floor_base -57. This export's ceiling_base is null. Item 11 measured ceiling word 7 and left map h -203 outside that storey. Height -202.95 is below floor -57, so the standing storey is 225. Region 225 has no event group.

Nearest grouped control, item 11, grade stays LIKELY. Control 76 Light panel, placement hex e2f6801d008033ff, decoded int16 (-2334, 7552, unnamed 0x8000, height word -205). Planar 60.2. Stream-1 groups 5980 and 5998 are opcode 6. The cstring is Light panel. The catalog name is Light panel. No slide distance is in the placement.

Grade. LIKELY that this coordinate is the top-floor pit lip beside shaft 776. UNKNOWN for a floor that slides at this quad. The Light panel grade is not raised.

What r12w does, read only, not re-run. hive_elevator.gd play_flute returns false unless monastery_conversation.gd FLUTE is in carried inventory. hive_elevator_state.gd play_flute sets flute_signal to 1 when played_flute is false. enter_trigger arms the poll only for region 282. After one second with flute_signal 1, advance sets target to 0 and played_flute true. Region 283 clears the arm. STOPS are -235, -427, -619, -811, -1003, -1195, -1387, -1579. SPEED 96 and the one-second poll are the adapter named in that file. Standing in region 225 does not arm the poll.

HIVE-FLUTE-FLOOR's backlog row joins this coordinate to the green-floor slide on Prima 78 and 81. The quad is the pit lip. The green floor is section (2).

## (2) The oily-floor slot

Player action. Offer the iron flute to the slot beside the oil. The floor closes over the oil. A step onto the oil with the slot empty starts the fire. Hive six card 1.

Book place. Prima printed 78: oil spill, step forward and back, or slide the flute into the slot, then the blades shatter. Prima printed 77 names floor seven in the column that leads into that sentence. Prima printed 81: oily floor and a diagonal slit, and the flute slides a green tile floor into place. Brady printed 160 and 170, checked on the page images for the Hive six cards. The flute closes a floor over the oil. Brady puts the receptacle on the passage after Level Seven, after emerging on Level Eight. The books disagree on the floor index. This card does not pick one.

Region. ~/lol2_out/all_maps_20260922/L5_HC/materials.json and materials/materials.json contain the string oil 0 times and the string flute 0 times. The same two strings are 0 times across the L14_HT export tree. No region id, no native x, no native y, and no floor word is assigned to the slot.

Control 83, item 11, placement hex 79f68e1e22e273fe, decoded int16 (-2439, 7822, -7646, height word -397). Opcode 6 groups 6232 and 6250. The height word is the next lift storey, the storey of owner note 10-26-38. It is a second opcode-6 pair on that storey. It is left off the slot.

Grade. UNKNOWN for the slot's region and for the slide distance. HINTBOOK and BRADY for the player action, on the pages above. The slide distance stays a logged adapter.

## (3) L14

Player action, same form-feed count. Printed 137, form-feed 149: "Remember what you did with the flute in the Hive Caves? See". Printed 138, form-feed 150: "the angled slot? Insert the flute to cover the oil and proceed. Don't walk into the blades, and take the passage to your right to bypass the blade trap." The next sentences: in the main hallway the center is a boulder, so walk to one side. Chapter Twelve's table-of-contents page is printed 131. That is the chapter start. This sentence is 137–138.

Region. The L14_HT export tree has no oil string and no flute string. No region id.

Grade. HINTBOOK for the action. UNKNOWN for the region, the slide distance, and the blade radius.

## Test

At the owner's point, inside the region 225 quad, floor -235, with the flute carried: play the flute and the lift is called. A green floor over an oil pool does not appear in that quad. Save and reload keep the lift stop the kit already stores. A test that only enters trigger 282 misses this note, because the standing point is outside that polygon.

The oil-slot test stays hive six card 1. It waits until a walk or a named floor supplies the room. Region 225 does not satisfy it.

L14, when that level is built: insert the flute in the angled slot, the floor covers the oil, the right-hand passage bypasses the blades, and the center of the next hall is the boulder. No world region is named yet, so that test has no coordinate.

## Adapter

None for the identity of the coordinate. Lift speed 96 and the one-second poll stay the existing adapter. The oil slide distance stays unknown. The lead's 17:24:46Z note keeps a non-repeatable flute-floor commit. This card does not change that.

## Unknown

The oily-floor region id, its native position, and its floor word. The slide distance. Whether control 76's opcode 6 groups move a bridge. L14's region id. The blade radius and the boulder trigger in the Huline hall.
