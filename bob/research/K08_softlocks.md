# K08 Where K01 through K07 can stick

No Godot was run. Newest owner file is still `TRIAGE_20261104.md`. Owner rule: an original softlock is fixed in both editions. A timed death, a centre-strip kill, and the chalice taking the stone are the books' own punishments. A missing host is not one of those. It is an unbuilt step.

## Original softlocks the owner list already names

| point | book remedy | what the port does |
| --- | --- | --- |
| Daniel's blade never changes hands, and the Wild Ones leave first. HINTBOOK 2916–2921: pick the knife up and try again, or the rest of the game is fruitless. | Keep the gift available until it lands. ORIGINAL_BUGS row 3. | The earned walk offers the blade before the hoppers. No deviation title states the other order. The bug stays open. |
| Cemetery barrel will not tip. HINTBOOK 3371–3373: reload, reboot, then a patch. PATCH.TXT 5.2 says the 1.30 barrel pushes and rolls. | Tip whenever Luther is human, touches the top, and the path is clear. ORIGINAL_BUGS row 6. | The oil chain's earned test walks a tip. No deviation names the failure. The original miss is not marked fixed. |
| Bracers given to Dawn the wrong way, then the ghost or the silver leaf never appears. Fan note, ORIGINAL_BUGS row 13. | The leaf and the ghost stay reachable. | `l10_silverleaf.gd` refuses to grow while the bracers are still carried, and grows on the return without them after the Emperor and Dawn. The ghost half of the row was not re-read. |
| A key item dropped or never picked up ends the game. ORIGINAL_BUGS row 14. | The item cannot be lost, or it comes back. | A full pack refuses a retrieve with "no room to carry". The shaman trade and a leaf use that kit. No deviation states a no-drop rule. |

## Stuck on a hosted step

The Larkhon without admission is the owner's save. HINTBOOK chapter 8 says join the tribe first. The note `larkhon_join_tribe` is the lead's fix, and it shows only within 600 of actor 115. Away from him the chain is silent. The kill-Malik key is not hosted.

The tomb oil. HINTBOOK 3363–3366: dragon's blood or a level-three spark, from a fair distance. The host accepts spark levels 1, 3, and 5 after the barrel's second phase, and the earned test refuses a basic spark that is too close. Dragon's blood is MISSING. A player who has only the weak spark, and no blood, has no book method.

The flood. HINTBOOK 3829–3846: be at the table before it lifts, or reload and start the bowl again. Standing on grate 82 is hosted. Picking the grate up and throwing it is MISSING. The ride does not depend on the throw. Being late is the book's reload, and the drown branch is hosted.

The statue. HINTBOOK 3805–3808: follow as human, with dampen. The walk checks the human form. Dampen is not a qualified spell. A player who cannot become human is stuck. A human is not stuck on the missing spell.

The bracers. While they are carried, the cemetery trees stay dead (`l10_silverleaf.gd`). The remedy is Dawn's exchange, which is hosted. The Dreamstone slots on the citadel exit and the temple door both give the stone back. The chalice consumes it on purpose (HINTBOOK 4636–4641). Later cards do not ask for it.

The hourglass with no leaf only chimes. The remedy is one silverleaf in the pyramid. That placement is hosted. The book also says planting is not required. The host does not make the player plant.

The ruins ledge. HINTBOOK 3766–3767: a misstep strands Luther, and the only remedy in the book is a save from before the step. No return from that ledge was read. The owner rule wants a way back. That fix is not specified here beyond "a path back onto the ledge."

## Where the chain simply stops

STORY-068 is BROKEN. The map does not attach `L16FountainBall`, and the earned test still breaks prop 602. H22's pad orb is prop 210 and has no events. Nine lichen clumps do not grow. The book's other city route, the avenue and the disk, is STORY-069 and has no script. After the greenhouse tower the cards 071 through 078 and 079 through 093 have no host and no earned test. A player who has the Dreamstone, the chamber, and the one tower cannot finish.

## Not a stuck point

The thrown grate, the Bracers of Valor, and the yellow figure are book sentences the spine does not walk. The hosted path does not need them. The five Larkhon notes match the earned stage once the player is near actor 115. They are not missing items.
