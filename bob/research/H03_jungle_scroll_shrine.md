# H03 Jungle scroll shrine trap

Beats 39 and 40. Owner F10 2026-11-03 17:20:06, jungle native (3015, 4098). Read from `L4_HJ.MIX` (geometry entry file 12409578, marker 18, 4787 regions) and `L4_HJ.json`. Opcode 196, opcode 18, opcode 15, opcode 14, and opcode 12 were not entered.

No new owner F10 after `TRIAGE_20261103.md`.

## Where the owner stood

Region 3329 is centered on (3016, 4098), floor -120, ceiling 400. Its kind-12 value-0 group 6662 (file 13029640) runs when predicate `0003050000` passes. That predicate is equality on local slot 5. Counting the 41-byte names from `villager` at file 13153135, slot 5 at file 13153340 is `Imp_shrine`. The bytes before `villager` are not names. Group 6662 writes slot 5 to 1 (`c60000000501`), opcode 20 `14045200d90080000a14` on u16 82, and opcode 18 `12108800c70b5210b0ff1209000000140000` on control 136.

Control 136 is at (3016, 4178), height -120, region 3325, static slot 39. The 30-byte static names that start at file 13284825 (`planks`) put slot 39 at file 13285995, `Inviso platform`. The opcode 18 words are (3015, 4178, -80), flags 0x0912. Bit 0x0004, the proven direct-relocation bit, is clear, so the move itself stays open. The words sit 40 above the placed height, on the north side of the shrine.

## What the player does

HINTBOOK lines 2298-2325: a hidden shrine to the right of the big bridge. Two ways in, a lizard tunnel or a step down you cannot jump back up. A platform holds a Scroll of Summoning. Taking it drops the floor behind you. The jump raises rocky spikes and the gargoyles spit fire. Jump the spikes or cut them (the Axe of the Long Arm is the example). Escape is a lizard ledge to the right when the waterfall is behind Luther. You already have Summon from the Museum, so the puzzle is optional. A human-form bug wants a backup save.

BRADY printed page 73 (file lines 2831-2848): secret shrine, summon scroll, save first, back out before the trap. Warding imp statues kill you. Unlock the secret passage behind the statues before you take the scroll. Another way out is the lizard tunnel south along the Bane.

## The take and the drop

Prop 0, template 48, is at (3017, 4024), height -125, region 3318, on the platform just south of the owner point. Template 48's 38-byte name, counting `Big Cattails 2` at file 13259183 as template 0, is `hangin 2` (file 13261007). That is a mesh name, not the word scroll. The book's scroll is this pickup's role.

Kind 6 value 20, predicate `0005000000`, group 0 (file 12728304): opcode 20 on itself, opcode 16 sets its state to 1, opcode 208.

Kind 2 value 48, group 30 (file 12728334): opcode 14 on itself, then opcode 196 on region 3318 `c490f60c0cfe003200000000` and region 3321 `c490f90c0cfe003200000000`. Both signed words are -500 and byte 7 is 50. Stored floors are -125 and -140, so the chasm floor formula drops them by 375 and 360. Region 3318 is the platform. Region 3321 is the quad just south of it, floor -140, center (3016, 3946). That is the floor behind the player if they face north toward the waterfall side. The callee was not entered.

## Spikes and the imp statues

South of the drop, still in the shrine:

| Record | Template name | Native x, y | Height | Region |
| --- | --- | --- | --- | --- |
| prop 534 | Small Expolsion (81) | 2953, 3789 | -140 | 3312 |
| prop 535 | Small Expolsion (81) | 3078, 3788 | -140 | 3281 |
| prop 536 | Imp Lord (80) | 3144, 3693 | -140 | 3350 |
| prop 537 | Imp Lord (80) | 2889, 3694 | -140 | 3342 |
| prop 538 | Medium Imp (79) | 2952, 3597 | -140 | 3300 |
| prop 539 | Medium Imp (79) | 3079, 3597 | -140 | 3279 |

Each of 534, 535, 536, 537, 538, and 539 has a kind-2 value-48 group gated by predicate `0005000001`, and that group ends in opcode 15 (`0f03....20030802`) on the prop itself. The groups chain the props: 536's group 10534 opcode 16s 539, 539's group 10666 opcode 16s 538, 538's group 10622 opcode 16s 537, 537's group 10578 opcode 16s 534. Opcode 15 was not entered. The fireballs and the protruding spikes are the book lines. These opcode 15s are the native records on the statues and the two explosion props at the jump line.

Region 3286, center (3013, 3726), floor -180, kind 12 group 6516 (file 13029494) runs when `Imp_shrine` equals 1. It opcode 15s props 516, 517, and 519 (template 86 `Tall tree`, around y 3573) and writes `Imp_shrine` to 2. What those three trees do in play is open.

## Required or optional

OPTIONAL. HINTBOOK 2300-2302: the Museum already gave Summon, so this shrine is not required to go on. Brady's First Sphere must-do list does not name this scroll. The lizard escape is how you leave the shrine, not a step the rest of the game waits on.

## Frame

No longplay frame was opened.

## Still open

- The item id on prop 0. The mesh name is `hangin 2`. The Scroll of Summoning is the book, not a cstring in this MIX.
- Opcode 18 on the invis platform: flags 0x0912 omit bit 0x0004, so the ledge raise is the coordinate words only.
- Opcode 15 on the imps, the explosion props, and the three tall trees. Which of those is the spike pop and which is the fireball is open.
- Brady's "unlock the passage before you take the scroll." Prop 123, another template 48 at (2940, 3535), writes local 45 and opcode 18s control 57. That was not joined to a door.
- A longplay frame of the drop.

Grades: placements, floors, group bytes, `Imp_shrine`, and the template and static names are DECODED. The scroll, the drop, the spikes, the gargoyle fire, and the lizard ledge are HINTBOOK. The imp statues, the secret passage, and the second exit are BRADY. The frame is open.
