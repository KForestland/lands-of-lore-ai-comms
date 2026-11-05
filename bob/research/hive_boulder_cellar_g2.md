# G2 Hive boulder cellar

Acceptance for HIVE-BOULDER-CELLAR-RESEARCH. Owner F10 2026-11-03 17:45:07 and 17:45:36, Hive native (-3345, 6074). Placements and group bytes are the ones in `H02_hive_boulder_cellar.md`. Read from `L5_HC.MIX` sha256 prefix `a1979e60d401ae30`. Opcode 197, opcode 196, opcode 18, opcode 12, and opcode 9 were not entered. No Godot.

## Native records

The owner point is inside region 685, a 20-by-30 quad centered near (-3258, 6151), floor -1659, ceiling -1521. Prop 70, template 33 `Inviso Light`, sits on that quad and has no events. No control or movable uses static slot 15 `Boulder`. No `Rolling Boulder` or `Puzzle Boulder` prop is within 800 of the point.

Controls 135 and 134, both `Button`, stand in this room at (-3399, 6143) and (-3288, 5995), region 682. Their groups run opcode 196 on region 685 and the chasm floor formula rises that quad by 30, from the stored floor -1659. Those buttons are not the floor break. No opcode 196 in the groups near this point lowers a floor.

The boulder script that names the pit is prop 460, template 28 `Rolling Boulder`, stored at (-2293, 7102), height -1259, region 677, about 1471 away. Kind 6 value 6, group 4740:

- opcode 197 `c590fa010300` on region 506
- opcode 9 and opcode 20 on prop 69
- opcode 20 on prop 377
- opcode 9 byte 2 on control 133 `Boldr Covr`
- opcode 9 byte 3 on control 0 `Ladder`
- opcode 9 byte 2 on prop 460

Region 506 is the pit under the corridor: floor -1709, center about (-3178, 6225). Opcode 197 was not entered. This is the boulder's only tie to the pit, not a decoded floor-break motion. How prop 460 arrives at the hole stays open.

Fixtures within a few hundred of the owner point:

| Record | Name | Native x, y | Height | Region |
| --- | --- | --- | --- | --- |
| prop 377 template 36 | Brazier | -3248, 6307 | -1629 | 837 |
| control 133 slot 18 | Boldr Covr | -3179, 6229 | -1675 | 590 |
| control 0 slot 64 | Ladder | -3142, 6190 | -1764 | 595 |

Control 133 has no events. The boulder group opcode 9s it. Control 0's group 5244 includes opcode 12 `0c1000000b00`. The u16 at +4 is 11. Room-name index 11 in `LOLG.DAT` is `runes_`. Index 10 is `runecl_`. The callee that loads the room was not entered.

Slot 5 `Boulder_Fall` is written by group 866 on region 473, around (-1490, 6480). That is a different place. The behavior strings "Boulder falls to the floor" and the three lines beside it were not joined to a group. `Runes_Lights_On` (slot 27) is written by brazier group 4124 and read by no predicate in this file.

Props 74 and 75 are the other rolling-boulder pair, near (1340..1947, 4895..4901). Hintbook lines 2785-2796 put two rolling boulders in a different room and pay a healing scroll. That room is optional. It is not this cellar.

## Longplay time

Frame n is `(n-1)*5` seconds. `longplay_deep/jungle/REFERENCE.md` puts rolling boulders at 96:14-96:24 and a pit or chasm at 97:14. Frames opened this pass:

| Frame | Time | What it shows |
| --- | --- | --- |
| f_01155 | 96:10 | A green-black corridor. A dark curve sits at the left edge. No hole. |
| f_01156 | 96:15 | Two spheres side by side in that corridor. |
| f_01157 | 96:20 | One sphere in a dark alcove. |
| f_01160 | 96:35 | A carved double door in a stone wall. |
| f_01162 | 96:45 | A raised stone lip and a dark opening. No ladder and no broken floor. |

No opened still shows a boulder leaving a wall, a floor breaking, or a cellar. Two spheres at 96:15 match the optional pair, and that picture stays off the cellar. The smash frame time stays open. The camera was not measured, so none of these stills is pinned to region 506 or prop 460.

## Contents

The stone and the runes are inside room `runes_`, not placed as L5 props beside the ladder.

HINTBOOK lines 2691-2698: the floor falls away, spark the brazier, enter the pit, click the clamshell for an Ancients' Stone, click left, press wax on the runes twice until Luther says "That worked!"

BRADY lines 3269-3280 and 7301-7304: click the orb for a Stone of Ancient Magic, then the engravings (a triangular glyph) for two wax impressions.

Those two sentences stay unmerged. Brady has the player dodge the boulder so it smashes the hole. The hintbook quick path says the floor falls away when you step on it. The stored pit is already floor -1709. A separate smash write was not found. The orb click and the wax click live in `runes_`. Their item grants were not read. f_01145 (95:20) shows a block with a blue glow during the relief-panel window. That still is not pinned to the orb.

## Required or optional

REQUIRED. Both books make two wax copies from this chamber the thing the Hive return is for (HINTBOOK 2659-2704, BRADY 7254-7308). Dawn takes one copy outside, and Brother Julian takes the other. The healing-scroll boulder room is the optional pair.

## Still open

- Opcode 197 on region 506. The floor-break motion is not a decoded opcode 196.
- How prop 460, stored 1471 away at height -1259, arrives at this hole.
- What Boldr Covr does in play.
- Which record plays "Boulder falls to the floor", and a longplay frame of the smash.
- The item grants inside `runes_`.

Grades: placements, template names, group bytes, region floors, and the room-name index are DECODED. The dodge, the smash, the ladder click, the orb, and the two impressions are BRADY. The falling floor, the clamshell, and the wax line are HINTBOOK. f_01156 is LONGPLAY of two spheres, not of this cellar. The smash frame is open.
