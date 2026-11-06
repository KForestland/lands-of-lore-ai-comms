# Act 3 findable

Grade HINTBOOK. The walk is `act3_duck.md` STORY-067 through STORY-093. Temple steps 054–066 are in `AA03_act2_findable.md`. Lines below were read in hintbook.txt for this list, or they are `hint.text` from the live base and the unapplied S/T/W/X diffs. No Godot. Six notes are added. A step whose prop is not stored gets no id.

hintbook.txt 4786–4807: south around the square, the avenue, the dry fountain, destroy the ball. The live line already says "Left click — Strike the floating ball" and "E — Take black lichen" (`l16_dry_fountain.gd`). The journal adds the place.

hintbook.txt 5363–5368: the caverns can be a straight run for the exit, and the map shows the heading. T03's line is "Killing stays optional. Luther stays." That is a developer sentence.

hintbook.txt 5410–5434: Baccata gives Belial's horn and passes away; keep the horn. As Human, break the bars. As the Lizard, enter the gutter. Three switches across the guck raise it. OCR prints "Hom" and "Bae, cata". The sentences are the horn and the sewer.

hintbook.txt 5460–5466: four ghostly heads, a level-one mist of doom each (OCR: "mists"), drag the demon onto the white circle, stay out of the fountain.

hintbook.txt 5484–5488: the curse spell at ancient-magic level five, and a purple glob enters the mother. The note does not name a movie.

## Walk

| Step | How the player learns | Id added |
| --- | --- | --- |
| 067 Arrival elevator | That script was not opened this pass. | none |
| 068 South dry fountain | Visible strike and lichen lines. Journal `l16_south_fountain` when `L16DryFountain` is present, the ball is unbroken, and the player is within 800 of `ORB` Vector3(440, 85, 10438). | `l16_south_fountain` |
| 069 Three towers, disk and box | S01: "The disk and the box are not placed. The centre stays down." | none. The disk and the box are not stored. |
| 070 Greenhouse | `l16_greenhouse.gd`: "E — Put a silverleaf into the glass pyramid" and "E — Turn the hourglass". Journal `l16_hourglass_leaf`. | none |
| 071 Southeast oil and the Dark Bow | S02: "Left click — Ignite the oil". | none |
| 072 Northwest traps | S03: "Left click — Strike the brick", "Left click — Loose the blue bow", "A level-three spark breaks the white ball." | none |
| 073–075 Ivory chips, southwest last | S04: "E — Set an ivory chip on the pedestal". Journal `l16_one_tower`. | none |
| 076 Box and the yellow figure | The book names Starry Tower. No script on this base contains Starry. S01 does not store the figure. | none |
| 077 Centre tower, Dark Sword, mantle | T01: "The fight is not hosted" and "Mantle Gate is not placed." | none |
| 078 Chop the dragon, then the teleporter | T02: "Left click — Chop the dragon" and "The statue is not the dragon." | none |
| 079 Caverns, run for the exit | T03's line does not teach the exit. Journal `l17_cavern_exit` when `L17CavernRun` is present, `exit_region` is still below 0, and the player is within 160 of `FORWARD_AT` Vector3(-5436, 32, 5802). | `l17_cavern_exit` |
| 080 West wall, blade, frond | W01: "E — Cut the west wall with a blade". The frond click is not stored. | none |
| 081 Belial's horn | W02: "E — Take Belial's Horn." Journal `l19_horn_keep` while `taken` is false, within 160 of `PIPE_AT` Vector3(120, 0, 525), node `L19BelialHorn`. | `l19_horn_keep` |
| 082 Bars, gutter, three switches | W03's lines say the bars and the gutter are unplaced. Journal `l19_sewer_cross` while fewer than three switches are stored, within 200 of `AT_74` Vector3(-323, 30, -2124), node `L19SewerForms`. | `l19_sewer_cross` |
| 083 Drain, or leave the guck | W04: "E — Click the door. The drain stays optional." | none |
| 084 Short path through the rapids | The right-right-south-east heading is not stored on a node. | none |
| 085 Four heads, white circle | W05: "E — Level-one Mist of Doom. The demon id stays -1." Journal `l19_ghostly_heads` while fewer than four shots are stored and the player is within 160 of any of props 67, 69, 68, 70. Node `L19GhostlyHeads`. | `l19_ghostly_heads` |
| 086 Dawn, expel the curse | X01: "E — keep clicking Dawn. The curse line is not a stored cstring." | none as its own id. The curse note below is the spell. |
| 087 Curse at level five, purple glob | X01 also shows the level beside a movie name. Journal `l19_curse_mother` while `curse_said` is false, within 160 of `DAWN_AT` Vector3(2802, -1000, -882) on `L19DawnCurse`, or of `MOTHER_AT` Vector3(-1160, -20, -4258) on `L20MotherCurse`. | `l19_curse_mother` |
| 088 Blue pillars, faux-Scotia | X02: "E — shoot. Blue stays -1." and "E — level-five Trinity." The path stays closed in that module. | none |
| 089 Moving pillars | No separate stored heading was read. | none |
| 090 Armory brick, white ball, fireball | X03: "E — hack the westernmost block. The brick id stays -1." | none |
| 091 Faux-Draracle, then the doors | X04: "E — strike actor 46" and "The doors stay still." | none |
| 092 Three ways to start the fight | X05: "E — the blue bow, the Dark Sword, and the horn start the same flag." | none |
| 093 Dawn and the Draracle | X05: "Dawn stays off L20." The scene is not a stored line. | none |

## Patch

`scripts/lol2/act3_journal_hints.gd` attaches from `act2_map.gd` after `sky_pack` is set. `attach` returns null, and frees its node, unless the area is L16_CA, L17_HC, L19_BC, or L20_BB. `MyJournal` SOURCES gains this file. The note count goes from 39 to 45 in `tests/my_journal_test.gd` and `tests/act1_journal_hints_test.gd`. Registry order 858. The headless test types `load().new()` through `attach` and frees every host.

Apply the S/T/W/X chain before the L17 and L19 nodes exist in play. `L16DryFountain` is already on a123d3f. The diff itself applies on a123d3f. It does not edit `docs/DEVIATIONS.md`.
