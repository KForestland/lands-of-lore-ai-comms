# I21 Armory sources and blocks

Place L20_BB. No frame was opened. No Godot was run. Template and static name-at-index stay LIKELY. Opcode 1, 5, 7, 9, 14, 16, 20, 196, and 198 were not entered. No cstring is brick, ball, pyrapod, white, torch, or spear.

Hintbook lines 5522–5534: three floating objects, like the northwest tower. Left, a spinning brick. Center, a white ball. Right, a fire ball. Hack or shoot the brick and the stone pillars stop. Shoot the white ball with a pyrapod spark or a level-three imp. Blast the fire ball with the blue bow. The objects return if you are slow. Grade HINTBOOK. The red-hole ledge on lines 5513–5518 is the corridor before that room. REQUIRED: the three objects in that order.

Brady printed 141–142: a rotating stone block on the left, destroyed with a sword, stops the moving pillars. A flame sphere goes out with Mist of Doom. Frozen vapor goes out with a fire spell. All three must fall or they come back, and the iron bars stay down until stone, fire, and ice are destroyed. Grade BRADY. Sword, Mist of Doom, and a fire spell are not the hintbook's dark bow, pyrapod, and blue bow. Those sentences stay separate.

## Three sources

| prop | template | native | Godot | region |
| --- | --- | --- | --- | --- |
| 195 | Phy source | (−3880, 2630) | (−3880, −2630) | 636 |
| 196 | Ice source | (−2650, 2924) | (−2650, −2924) | 1540 |
| 197 | Fire source | (−3619, 3431) | (−3619, −3431) | 1576 |

Each is height −50. Prop 195 is the westernmost. That was not joined to the book's left-hand stone.

Prop 197, group 6476, stores opcode 9 with byte 4 = 21 on u16 57, 58, 59, 60, 61, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, and 98. Those nineteen indexes are the Fire pillar movables. Other tables also use some of those indexes.

Prop 196, groups 5946 and 6170, stores opcode 9 with byte 4 = 21 on u16 62 through 84, twice. Those twenty-three indexes are the Ice pillar movables. Other tables also use some of those indexes.

Prop 195, group 5494, stores twenty-eight opcode 196 commands. Every one has byte 6 = 1, word +4 = −45, and byte 7 = 150. Byte 6 is not 0, so the floor formula stays off. The target u16s are 563 through 1551. They are not the pillar indexes and not the block controls.

Opcode 198 on these three uses byte 4 = 1, 2, and 3, each with byte 5 = 1 and byte 5 = 0. Local slots at a 41-byte stride are 1 `Phy_defense`, 2 `Ice_def`, and 3 `Fire_def`. The join stays unbound.

## Six blocks

Controls 62 through 67 are static slot 8, `Block`, height −110, flags 0x8481, on y 1718..1729. Native x is −1375, −1209, −1041, −870, −701, and −547. Godot y is −1719. Each kind-5 group is one opcode 20 on that control. The raw for 62 is `14103e00c00196000a14`. Opcode 20 was not entered.

Six `Crystal ceiling` props, 144–146 and 153–155, sit on the same x's at height 94..98. Each opcode 9 names the block under it with byte 4 = 2, and also names two other u16s. Six `Magic Cloud` props, 147–152, share the row. Their only records are kind 1. Kind 1 was not read as a command.

Eight `Big Smokem` props sit around (−7800, 4800). They have no events. They are not this row.

## Still open

Which source is the brick, the white ball, or the fire ball. What opcode 9 byte 4 = 21 does to a pillar. The opcode 196 targets. What opcode 20 does to a block. The red hole and the ledge. No frame.
