# L16 starry floor, 2026-11-13

Read-only. Playtest tree not edited. No Godot was run for this note. The chain stop it explains is robot folder `robot/L16_CA/20261113_890108b-chain3`: the northeast lift landed, the stairs reached floor 0 at (15556, 32, 4123) region 7669, and the box, the disk, and the yellow figure were not on that floor.

Grades below are the grades already filed in `I03_starry_tower.md`, `I02_ne_tower_interior.md`, `source_ids_066_075.md`, and `source_ids_076_085.md`. This pass did not re-enter an opcode. A book sentence is not a MIX row.

## What the player does

Two guides, both REQUIRED as clicks, neither one a placed id.

Hintbook 5224–5236, grade HINTBOOK, copied in `I03_starry_tower.md`: you arrive in one of four corner towers, put the box in the square hole where you entered, and do not push it back through the disk. Outside, click the yellow eight-sided figure. One portion of the center tower rises, and a similar structure rises in the city. Four visits finish it.

Brady printed 131, grade BRADY, same note: push the dragon box through the sphere, slide it into the hole, touch the golden crystal that appears on the plain, and one section of the Grand Tower rises in the Netherworld and in the city. Four sections. Looking around the plain is the book's aside.

A different paragraph, hintbook 4842–4847, is the northwest room's exit, not this floor. `I02_ne_tower_interior.md` keeps it there: after the moving-wall room, go up the stairs, push the box through the shimmering disk, and the box is transported. It was not matched to a placed object in the northeast interior.

The greenhouse yellow figure is a third sentence. Hintbook 4855–4894 says it waters the plots, and the same page says planting is optional. `K06_act3_city_steps.md` grades that figure MISSING. It is not the crystal on the starry plain.

## Longplay frames

Path `~/lol2_original_screens/longplay_frames_act2plus/`. Time base is the one in `I33_act3_frames.md`: `6580+(N-1)*30` seconds. This pass opened four jpegs. No native id was read off a picture.

| frame | time | on screen | not bound |
| --- | --- | --- | --- |
| g_00311 | 268:10 | one gold block against a pale stone wall, checkered floor | a disk, a push, a hole |
| g_00316 | 270:40 | not re-described here; I33 lists it as the outdoor towers | a box or a figure |
| g_00340 | 282:40 | checkered room, gold pyramid on a stand, banners; a yellow octahedron high in the view and a small pink mark | the octahedron sits where the cursor is drawn; I33 already refused to bind g_00340 and g_00344 to the eight-sided figure |
| g_00344 | 284:40 | long checkered hall, dark vase in a wall niche; the same yellow octahedron high in the view and a small pink mark | same refusal |

I33's row for STORY-076 stays the grade: frames show a yellow octahedron at the top of two rooms, not bound to the figure. STORY-069's frames show gold blocks, and a disk and a push were not on screen.

## MIX records

L16 static names are the 30-byte run at file 19098082, 87 names. Template names are the 38-byte run at file 19073622, 136 names. Name-at-index stays LIKELY, as in I03.

Searches already filed, not repeated as a new scan:

| book object | cstring | placements | events |
| --- | --- | --- | --- |
| box | none. No template and no static name is box. A four-byte `Box` at file 14424350 sits in binary, not a name record (`I02`) | none | none |
| shimmering disk / sphere | none. No `disk` cstring | none | none |
| square hole | static Tower Hole, index 64 | zero | none |
| yellow eight-sided figure / golden crystal | no yellow cstring. Templates Bool and Bright Star have zero placements | none | none |
| heaven stair, Teleporter, Staged Button | static names | zero | none |

What is placed, and is not those three:

The arrival is four kind-12 city-gate regions. Each stores an opcode 18 with flags `0x0c04` and target u16 0. I03 files that target as not the player. Bit `0x0004` is the direct-relocation form. The other bits in `0x0c04` were not read. Kind 12 timing was not re-proved, so these rows are stored commands, not a proven step-on.

| city region | opcode 18 words | destination region | floor, ceiling | corner key |
| --- | --- | --- | --- | --- |
| 3107 | (16082, −3886) | 7658 | 100, 800 | control 119 (15948, −4005) |
| 3243 | (10467, −3668) | 7722 | 100, 800 | control 120 (10666, −3970) |
| 3443 | (10444, −9314) | 7600 | 100, 800 | control 122 (10605, −9187) |
| 2846 | (15978, −9312) | 7267 | 100, 800 | control 121 (15892, −9211) |

Godot flips stored y, so the northeast arrival is (16082, 3886). That is where the chain3 lift stood, region 7658. Each destination quad is a few hundred units on a side. None of the four is a pit. No item row sits in that band. Each corner's placed contents are the Key Object, one Jumbo Gate with no events, and two poles. Poles are props 402, 403, 447, and 494, template Pole w/ globe on top. The groups also opcode 9 them with byte 4 = 21. Opcode 9 was not entered, so a pole is not the yellow figure.

The four Iris Doors (controls 109–112) and Tower Pylons (props 489–492) sit on the mid-sides, floor 0, ceiling 5000. Their opcode 18 flags are `0x0912`, bit `0x0004` clear, and the target is the pylon itself. That is the smoke-ball shape, not the corner arrival and not a disk.

Prop 615, LIKELY template Tower, is a real placement: stored (13273, −6464), height −999, region 6517, flags `0x0002`, event 0. Godot (13273, 6464). Region 6517 floor is −1000 and the ceiling is 5000. The mesh sits one unit above that pit floor. It has no events of its own. It is the center structure, not the box.

Three altars in region 8301 hold the raises. Region 8301 does not connect to the plain. The opcode 196 floor formula already accepted in I03, applied there and not re-proved: signed word at +4 is an absolute floor target, byte 6 is 0, byte 7 is speed.

| altar | native | group | current floor | target | speed | delta |
| --- | --- | --- | --- | --- | --- | --- |
| prop 487 | (20003, −6112) | 20160 | 80 | 1200 | 50 | 1120 |
| prop 614 | (19998, −6238) | 38598 | −1000 | 850 | 50 | 1850 |
| prop 616 | (20002, −6367) | 38718 | 10 | 500 | 20 | 490 |

Group 38598 includes the tower's own region 6517. Each of those groups also has opcode 20 on prop 615. Opcode 20 was not entered. A fourth floor group that names this pit was not found. Stream 0 groups 4578, 4584, and 4606 are opcode 9 on prop 615, byte 4 = 16, and no object or region event points at them.

Props 365–374, the Shape rows, are a statue hall around (5500, −7000), event 0. They are not a ring around prop 615. The city's copy of the rising structure stays UNKNOWN. Locals slot 0 `Star_Elevator` and slots 6–9 `Trigger_Nth_tower_pylon` were not bound: the pylon groups contain no opcode 198.

## Why the port places none of the three

The port instances a placement row. These three have no placement row, so there is nothing to instance and nothing a producer filter could have dropped.

- Box: no name, no row.
- Disk: no name, no row. The iris opcode 18 is a different target and a different flag word.
- Yellow figure: no name, no row. Bool and Bright Star are names with a placement count of zero, which is the same fact, not a hidden mesh.

Prop 615 is placed. `l16_ne_tower.gd` leaves it at height −999, its authored height, because Tower Hole, the box, and the yellow figure have zero placements. The host does not raise it. The northeast lift the robot rode is the separate adapter in that same script: standing on the opened FireWall doors writes the player to (16082, 132, 3886) because I03 files opcode 18 target u16 0 as not the player. That write is the arrival, not the box puzzle. `SECTIONS` stays 0.

The chain3 floor at region 7669 is the stair landing next to that arrival. The stairs are placed. The three book objects are not on them.

## What each must do for the chain to go on

From the guides, not from an entered command:

- The box is pushed through the disk once, into the hole at the entrance, and is not pushed back.
- The disk is the thing that transports the box. Brady calls it a sphere. No stored opcode 18 in the corner quad has a box id.
- The yellow figure is one click on the plain after that. One section of the center tower rises, in the Netherworld and in the city. Four such visits finish it.

The stored numbers that match "a section rises" are the three altar opcode 196 groups above. Nothing in those groups names a box, a disk, or a figure, and opcode 9 between the corner and the closet altars was not entered, so the click is not yet a command. The fourth raise was not found. Until that link is read, placing a fake box on region 7669 does not make the chain true.

Oil, the ivory chips, the centre mantle, and the dragon do not read these locals. Their earned tests start from a ground save or an oil-chain save, not from a starry-floor flag. They can be walked while this floor stays unplaced.

## Modern replacement while the rule stays unknown

Do not spawn a box, a disk, or a yellow mesh. There is no id, no template, and no placement to attach.

The smallest continuation that uses only numbers already copied: after a plain-input arrival in one corner quad, one click on the plain, with no new prop, runs altar 614's group 38598 once. That group is the pit, including region 6517, from floor −1000 toward target 850 at speed 50. The click logs that the box, the disk, and the figure were not placed, and that opcode 20 on prop 615 was not entered. It does not invent the fourth raise, does not bind a pole or the cursor octahedron to the figure, and does not gate the oil, the chips, the centre, or the dragon. Four clicks would claim four towers the MIX does not distinguish. One click is the whole replacement until a placement or an entered opcode 9 says otherwise.

Sol's next chain item can start from this note. The replacement is not a patch on the playtest tree.
