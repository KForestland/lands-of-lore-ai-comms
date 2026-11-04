# H02 Hive boulder cellar

Owner F10 2026-11-03 17:45:07 and 17:45:36, Hive native (-3345, 6074). Read from `L5_HC.MIX` sha256 prefix `a1979e60d401ae30`. Opcode 197, opcode 196, opcode 18, opcode 12, and opcode 9 were not entered.

No new owner F10 after `TRIAGE_20261103.md`.

## Where the owner stood

The point is inside region 685, a 20-by-30 quad centered near (-3258, 6151), floor -1659, ceiling -1521. Prop 70, template 33 `Inviso Light` (name file 6007897), sits on that quad at (-3259, 6150) with no events. No control or movable uses static slot 15 `Boulder` (name file 6023911). No prop with template 28 `Rolling Boulder` or template 35 `Puzzle Boulder` is within 800 of the point.

The two buttons in this room are not the floor break. Control 135 and control 134, both static `Button`, are at (-3399, 6143) and (-3288, 5995), height -1629, region 682. Their kind-3 groups 8520 and 8604 (predicate `0005000001`) run opcode 196 `c490ad02a3f9001e00000000` on region 685: signed word -1629, so the chasm floor formula rises that quad by 30. Groups 8560 and 8644 write the word -1659, which is the stored floor (delta 0), play opcode 20 `bb02` on prop 70, and opcode 16 the other button. Bytes matched in the MIX at files 5900851, 5900935, 5900891, and 5900975.

## The boulder that names this cellar

Template 28 `Rolling Boulder` props are 68, 74, and 75 near (1340..1947, 4895..4901), and prop 460 at (-2293, 7102), height -1259, region 677. Prop 460 is the one whose script names the cellar. Kind 6 value 6, group 4740, file 5897071:

- opcode 197 `c590fa010300` on region 506
- opcode 9 and opcode 20 on prop 69 (another brazier, at (-2257, 7138))
- opcode 20 `14037901c401ff001914` on prop 377
- opcode 9 byte 2 on control 133 `Boldr Covr`
- opcode 9 byte 3 on control 0 `Ladder`
- opcode 9 byte 2 on prop 460 itself

Region 506 is the pit under the corridor: floor -1709, center about (-3178, 6225), neighbor of corridor region 679 (floor -1659). Opcode 197 was not entered, so this is the link from the rolling boulder to the pit, not a decoded floor-break motion. No opcode 196 in the groups near this point lowers a floor.

Props 74 and 75 are the pair. Hintbook lines 2785-2796 put two rolling boulders in a different room and pay a healing scroll. That room is optional. Prop 68's kind-2 group 78 is opcode 2 `020100003d28` and was not entered.

## What the player does, and the hole

BRADY printed page 81 (file lines 3262-3273) and the walkthrough on printed page 170 (lines 7273-7304): past the broken blades, a boulder rolls out of a wall. Run the other way. It smashes a hole. Spark the brazier. Click the ladder. The room below is the rune chamber.

Native fixtures on that hole, all within a few hundred of the owner point:

| Record | Name | Native x, y | Height | Region |
| --- | --- | --- | --- | --- |
| prop 377 template 36 | Brazier | -3248, 6307 | -1629 | 837 |
| control 133 slot 18 | Boldr Covr | -3179, 6229 | -1675 | 590 |
| control 0 slot 64 | Ladder | -3142, 6190 | -1764 | 595 |

The brazier has a kind-1 record, a kind-9 value 17 (group 4118, opcode 5 on itself), and kind-3 value 1 group 4124 (file 5896455). Group 4124 is the only opcode 198 that writes local 27: `c60000001b01`. Slot 27 at file 5982373 is `Runes_Lights_On`. No predicate in this level reads slot 27.

Control 133 has no events. Control 0 kind 4 group 5244 (file 5897575) is opcode 197 on u16 642, opcode 9 on prop 71, opcode 12 `0c1000000b00` (u16 at +4 is 11), and opcode 18 to (-3116, 6284).

Region 506 owns the floor subdivisions the rune-pit pack already counted. The kind-12 value-1 groups on those tiles (sample: region 654 group 5244, region 656 group 5328 file 5957001) repeat that room entry. Group 5328's opcode 12 is `0c0371010b00`: u16 at +4 is 11, and the u16 at +2 is 369 (prop 369, template 24 `sml rock`, at (-3372, 5960) in the button room). Region 655's group 5286 does not enter the room. It opcode 15 / 14 / 9 on u16 53.

The room-name cstrings in `LOLG.DAT` run `pool_`, `cave_`, `skel_`, `ment_`, `mcel_`, `mgar_`, `moff_`, `mlib_`, `wpn_`, `sever_`, `runecl_`, `runes_`. Index 10 is `runecl_` (file 1852255) and index 11 is `runes_` (file 1852263). The pit groups' room word 11 is that `runes_` slot. One tile, region 625, uses room 10 (`runecl_`) in the rune-pit pack. The callee that loads the room was not entered.

## Cellar contents

The stone and the runes are inside that room, not placed as L5 props beside the ladder.

HINTBOOK lines 2691-2698: the floor falls away, spark the brazier, enter the pit, click the clamshell for an Ancients' Stone, click left, press wax on the runes twice until Luther says "That worked!"

BRADY lines 3269-3280 and 7301-7304: click the orb for a Stone of Ancient Magic, then the engravings (a triangular glyph) for two wax impressions.

## Required or optional

REQUIRED. Both books make two wax copies from this chamber the thing the Hive return is for (HINTBOOK 2659-2704, BRADY 7254-7308). Dawn takes one copy outside, and Brother Julian takes the other. The healing-scroll boulder room is the optional pair.

Brady has the player dodge the boulder so it opens the hole. The hintbook quick path says the floor falls away when you step on it. The stored pit is already floor -1709. A separate "smash" write was not found.

## Local Boulder_Fall

Slot 5 at file 5981471 is `Boulder_Fall`. Its only framed writer is group 866 (file 5952539), `c60000000501`, plus slot 26 `Collapse_Hallway`. Region 473 kind 12 group 866 fires when predicate `00031a0000` passes (local 26 equals 0). Region 473 is the quad around (-1490, 6480), not this cellar. Predicates `0003050001` and `0003050000` exist and no event cites them. The behavior strings at file 5995369 (`Boulder falls to the floor`, `Boulder goes on "patrol"`, `Boulder comes to rest`, `Boulder damages player`, each twice) were not joined to a group.

## Frame

No longplay frame was opened. Frame time for the smash is still open.

## Still open

- Opcode 197 on region 506: the boulder group's only tie to the pit. The floor-break motion itself is not a decoded opcode 196.
- How prop 460, stored 1471 away at height -1259, arrives at this hole.
- Boldr Covr has no events. The boulder group opcode 9s it. What the cover does in play is open.
- `Runes_Lights_On` is written by the brazier and read by no predicate here.
- Which record plays the "Boulder falls to the floor" strings, and a longplay frame of the smash.
- The orb click and the wax click live in room `runes_`. Their item grants were not read out of that room.

Grades: placements, template names, group bytes, region floors, and the room-name index are DECODED. The dodge, the smash, the ladder, the orb, and the two impressions are BRADY. The falling floor, the clamshell, and the wax line are HINTBOOK. The frame is open.
