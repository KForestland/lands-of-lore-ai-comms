# L10 Cemetery behaviour cards

2026-11-01. Closes the 17:10:08Z line. Prima folios are form-feed index minus 12. Brady pages were read from the page images. Printed 186, 187, 188, 189, 207, 208, 209, and 210. No DOSBox. No Godot. Charger coordinates stay in charger_altar_anchors.md and in Astra's 17:58:06Z join. This page does not move them.

Prima says gold. Brady says yellow. That is the same cemetery charger and the same disagreement as the altar card. Do not pick a colour word. The catalog rows are unchanged: index 98 is 96-E Globe, 99 is 97-Y globe, 100 is 98-W globe, 101 is 99-B globe.

Catalog strings that use the book's words, not placements: index 102 "100-Drac sigil" identity 3319438660, index 97 "95-D Ankh" identity 3885062029, index 117 "115-Silverleaf" identity 238320129. "58-Br dead", "76-Caretk urn", and "34-Valkryie" are also catalog names. Those three are not the book sentences, so they are not assigned to the priest, the urn, or the crossbow.

## 1. Gate

Player action. Open the locked gate at the winged statue with the item the shaman gave.

Prima printed 97. The key the Huline shaman gave opens that gate. No key means go back to chapter 8.

Brady printed 187, checked. Must-step 1: open the main gate with a Dracoid Sigil from the Wild One Shaman. Brady printed 207, checked, step 24: use the Sigil to open the gate and go inside.

Agree: one shaman item opens the gate. Disagree: key versus sigil. Whether the item is consumed is not on these pages.

Test. No item, or the wrong item, and the gate stays shut. The shaman item opens it. Save and reload and it stays open. A second use does not take a second item. Joins STORY-006.

## 2. Globes and doors

Player action. Pick up empty glass globes. Ignore the globes that have swords in them. A charged globe of the matching colour opens a tomb. The gargoyle pedestal names the colour.

Prima printed 97. Sword globes are not the ones to charge. Charge one only for a use. Printed 98. Gold doors first. Pick up free globes. Printed 99. One gold globe finishes the early stage. One of each colour is required for the last leg.

Brady printed 186, checked. At least two blue and one yellow are necessary. Touching the gargoyle outside a tomb shows the colour. Keep one white, one blue, and one yellow for the Emperor. Printed 189, checked. At least five spheres: two white, two blue, one yellow. One white opens the northern of the two west mausoleums. One blue opens the priest's tomb on the east. One yellow, one blue, and one white go in the Emperor's pedestals. Printed 188, checked, step 6 says collect three empty orbs, then charge one of each. That three is the Emperor set, not the door count.

The sword-globe warning is Prima only. The gargoyle colour hint is Brady only. The five-sphere count is Brady printed 189. Prima's "one gold now, one of each later, two white from the tower, two blue minimum" is a different list. Do not add the lists into one number. The Valkyrie crossbow is Prima printed 102: a third blue globe, and the book says the two are enough if the third is missing. It is not in Brady's must-steps on these pages.

Test. A sword globe is refused by a charger and by a tomb. An empty globe is refused by a tomb. A charged globe of the pedestal's colour opens that tomb once. The wrong colour is refused and stays in hand. Save and reload keeps the open door and the spent globe. Joins STORY-007.

## 3. Chargers

Player action. Put an empty globe in the claws. They close and turn. Click the globe to take it back.

Prima printed 99. The three-clawed thing is the gold charger, northeast in the catacombs, past one-way fences that lead the wrong way if climbed. A few seconds, then click. The white charger is in the Mage's Tower. If the cemetery teleporter works, walk into the winged statue. If it does not, use the pit in the Savage Jungle. Come back with two white globes. Printed 102. The blue charger is north, reached after the oil breach. Leave by the same stairs used to enter, jumping the low fences.

Brady printed 207, checked, step 27. Click an empty globe on the Dragon's Claw altar. Printed 189, checked. White altar, second level of the Mage's Tomb. Yellow altar, catacombs through the open south mausoleum. Blue altar, catacombs through the tomb blasted open with the oil barrel.

The claws, the few seconds, and the click-to-retrieve are Prima. Brady names the click onto the altar and does not time it. "A few seconds" is not a duration to encode. The occupy and retrieve contract is the charger API. Anchors already posted are not repeated here.

Test. One empty globe goes in, a save while it is held by the altar reloads still held, one retrieve returns the charged globe, a second retrieve is refused. The other colours are the same contract. Joins STORY-009, STORY-010, and STORY-017.

## 4. Fences and boards

Player action. Cross the low fences only in the direction the book allows.

Prima printed 98 and 99. The low fences are one-way. The crossing toward the other stairs is south, more or less, and needs a run, a jump, and a crouch in the air. The other direction is called impossible on the page. Climbing the higher fences in the catacombs puts Luther on the wrong-way side.

Brady printed 208, checked, step 33. Boards separate one catacomb room from another. A human can jump them. A beast cannot. That sentence does not say one-way, and it does not say crouch.

These stay two descriptions. Do not merge them into one obstacle.

Test. On the Prima fences, the southward jump crosses and the return does not. On the Brady boards, human crosses and beast does not. No distance or height is in either book, so the test uses the placed geometry and does not invent a number.

## 5. Barrel and oil

Player action. Open the white-globe tomb, throw the switch, get the barrel into the north tomb, and ignite the spill from far enough away that Luther survives.

Prima printed 100. White globe, switch by the door, barrel blocking the south door. As Human, sidle past, touch the top, path clear of zombies, the barrel tips, a nudge rolls it north, it breaks, oil spills. If it will not tip, the book says reload and, if needed, restart. Printed 101. Dragon's blood is activated on the portrait, set in the oil, and Luther backs away. A level-three spark reaches. A level-one or level-two spark only reaches from close enough to be in the blast. The page also says "some other means" on printed 100.

Brady printed 208, checked, steps 29 to 31. Northernmost west mausoleum, white globe, switch on the right when facing the door, south door opens. Push and drag the barrel, knock it over, roll it into the first mausoleum, oil spills. Spark the oil. Too far hits the ceiling. Too close kills Luther. No spark level is numbered.

Agree: white globe, a switch, a barrel, a spill, then fire, from a distance. Disagree: touch-the-top versus push-and-drag, and level-three versus an unnumbered Spark. The ceiling-hit failure is Brady only. The restart-the-PC failure is Prima's description of a bug, not the behaviour to rebuild. The working tip is the card.

Test. Beast or a blocked path does not complete the spill. Human, clear path, and the barrel breaks in the north tomb. Dragon's blood set in the pool opens the breach once. A spark from the short range does not. Save and reload keeps the breach. A second fire does not close it. Joins STORY-015 and STORY-016.

## 6. Priest, urn, ankh

Player action. Open the priest with a blue globe, hear him because the bracers are in hand, take the vessel, bring back the ashes, and receive the ankh.

Prima printed 102. Blue globe. The dead bracers make him intelligible. The OCR of this file gives the vessel as "um". The next pages use it for the ashes. Printed 103. Finished, he gives an ankh. The ankh goes in the slab by the tomb and the Emperor's tomb opens.

Brady printed 187, checked. Possess the Bracers of the Dead, blue orb, collect an urn. After the cremation, click the urn on the ashes and he gives an Ankh Key. Printed 208, checked, steps 34 and 35. The east gargoyle shows blue. The step-35 sentence says wearing the bracers, and he gives an urn and asks for the ashes from a cave beyond the big lake. Printed 209, checked, steps 38, 39, and 42. Drag the body onto the platform, spark both dragon-orb pedestals, click the urn on the ashes, give the urn back for an ankh.

Possess and wearing are both printed, on different Brady steps. Do not collapse them. The cremation sparks are in the ruins, so they join STORY-020, and the cemetery only receives the urn and gives the ankh. Joins STORY-018 and STORY-021.

Test. No bracers, and the talk does not yield the vessel. Blue globe missing, and the tomb stays shut. One vessel, one ankh, a second talk does not give a second one. The ankh in the slab opens the Emperor tomb and the ankh remains available for the later door. Save and reload keeps all three.

## 7. Emperor

Player action. Put one globe of each colour in the matching box and take the remains.

Prima printed 103. Gold, then white, then blue works. The page says there may be more than one way. Click the sarcophagus. The entrance teleporter works after this. Printed 99 already said the teleporter might not work before then, and the jungle pit is the other road.

Brady printed 189, checked, step 5. One yellow, one blue, one white, in the colour-coded pedestals. No order. Printed 209, checked, step 44. The sentence order is yellow, blue, and white. Then the ankh opens the doors. If the bracers are still worn, click the remains. Printed 188, checked, step 11 also says wearing the bracers for that talk.

The order that Prima guarantees is gold, white, blue. Brady's step 44 lists yellow, blue, white and does not say the other orders fail. Prima's "more than one way" stays. A test that allows only one order fails this card. Wearing is Brady's condition for the remains click. Prima says "have" the bracers for the priest and does not repeat an equip line for this click.

After the flood, Prima printed 103 says the bracers are given up to speak with Dawn, the return visit to the Emperor is unintelligible, and silverleaf is growing. That later visit is not the remains click.

Test. Each wrong colour is refused and stays in hand. Any complete set of the three colours opens the sarcophagus. Remove one and it closes again, unless a later source says the set latches. One set of remains. Reload in the middle keeps the partial set. Joins STORY-022 and STORY-023.

## 8. Silverleaf

Player action. After the flood and the return, take the leaves and bring them to the village.

Prima printed 103. Pick nine leaves. Printed 104. The mission's item is the silverleaf for the shaman.

Brady printed 210, checked, step 48. Gather as much as you can. Step 49. Give the silverleaf to the Shaman, then fight Daniel. Printed 188, checked. Malik gives that leaf back after the ceremonial fight, to mix with Amaranth Serum. Save one leaf by itself for the City of the Ancients.

Nine is Prima's number. "As much as you can" is Brady's, plus one kept unmixed. Do not make nine the amount that unlocks the shaman. Brady printed 186 says the leaf exists only after both this level and the ruins are done. Prima puts the growth on the return after the flood.

Malik is the name on printed 188. The Shaman is the name on printed 210 and in Prima. These pages do not say they are the same person.

Test. No leaves before the flood return. After it, leaves can be picked, a reload keeps the grown plants, and handing one to the shaman does not erase a second leaf kept back. Joins STORY-030 and STORY-031.

## Grade

HINTBOOK for printed 97 through 104. BRADY for the eight image-checked pages. Catalog rows are the definition file, not placements. The claw duration, the fence size, the spark range, the gate consumption, and a single globe total stay UNKNOWN. No region id was measured for these cards.

## Contract

Inputs are Prima chapter 9 and the Brady pages named above, plus the existing altar card. The effect is these eight acceptance specs. The grade is HINTBOOK and BRADY, with the colour words left unmatched. No test was run. No adapter was written.

## Test

The eight tests above are the acceptance. The charger test is the one already named on the altar work: one earned empty globe, save while the altar holds it, one retrieve, second retrieve refused. The barrel test is the next cemetery mechanism, and it follows the working tip rather than Prima's restart loop.
