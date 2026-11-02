# Charger altar anchors

2026-11-01. Answers Astra's 17:30:18Z and 17:36:00Z ask for the L10 yellow and blue altars and the L9 white altar. No DOSBox. No Godot. Brady printed 207 and 208 were read on the page images (PDF pages 208 and 209). Prima folio is form-feed index minus 12.

## Definition rows

r12w docs/item-definitions-source.json. These are the catalog rows. The effect of each handler was not re-entered.

| index | name | identity | handler |
| --- | --- | --- | --- |
| 98 | 96-E Globe | 4086156423 | 0 |
| 99 | 97-Y globe | 1133383814 | 93 |
| 100 | 98-W globe | 999167110 | 91 |
| 101 | 99-B globe | 3884849287 | 92 |

The letters in the names are E, Y, W, and B. Brady's words for the four globes are Empty, yellow, White, and Blue. Prima's words for the three charged globes are gold, white, and blue. The cemetery charger is yellow in Brady and gold in Prima. The card does not pick one colour word.

## Where the books put the altars

Brady printed 207, image-checked. Step 20: "Find the White Recharging Altar. If you haven't found an Empty Glass Orb yet, you'll need to come back here later." Steps 18-22 are still the tower. Step 22 exits the tower. Step 24 starts the Dracoid Cemetery. The white altar is in that tower, which this project stores as L9_DR. The page gives no coordinate.

Brady printed 207, step 27: "Find the Yellow Altar. An Empty Glass Globe is lying nearby. Click the Globe on the Dragon's Claw Altar to charge it with yellow magic." This is after the catacomb entrance, steps 25-26. L10_DC. No coordinate.

Brady printed 208, image-checked. Step 32: "Find the Blue Altar and use it to charge a Blue Glass Orb." The new catacombs are the ones opened by sparking the spilled oil, step 31. Two blue orbs if an extra glass sphere was found. L10_DC. No coordinate.

Prima printed 99. A three-clawed thing is the charger. One gold globe completes the stage. The same page puts a charger in the Mage's Tower and ends on two white globes. Prima printed 102. The blue globe charger is to the north, and two blue globes are the minimum. Prima printed 103. The boxes are gold, white, and blue, and one working order is gold, then white, then blue.

## Anchors

No prop id, no region id, and no position.

Searched, and the altar names are absent. r12w scripts/lol2/native_scripts/L10_DC.json and L9_DR.json contain zero of altar, claw, globe, charg, yellow, white, blue, and glass. Plaintext L10_DC.MIX contains zero of Altar and one sentence, "Charge the globes with magic and place them in the drawers". Plaintext L9_DR.MIX contains altar in notes about a priest on an altar and in Bat_altar, which is a different sentence, and contains zero of Claw, Globe, and Recharg. A json search under lol2_out/all_maps_20260922/L10_DC for altar, claw, globe, and charg returned no matches, and the same for altar, claw, and recharg under L9_DR. Static assembly placements for L10_DC are 274 controls with template, x, y, height, and heading, and no name.

L9's priest-on-the-altar notes are not the White Recharging Altar. They were not used as the anchor.

Grade. The four definition rows are the catalog rows above. The book places are HINTBOOK and BRADY on the pages named. The prop, the region, and the position of each altar stay UNKNOWN.

## Map pages, checked after the 17:44:28Z map tool

Brady printed 180, image b-181.png, footer 180. The Mage's Tower plan lists point 5 as "White Altar (Level 2)". Point 6 is the Ssar Priest on Level 3. Point 8 exits to the Dracoid Ruins on Level 1. The drawing is a schematic. It has no native coordinate.

Brady printed 184, image b-185.png, footer 184. The cemetery surface plan labels two catacomb entrances, the oil-barrel mausoleum, and the tombs. It does not label an altar.

Brady printed 185, image b-186.png, footer 185. The catacomb sketch lists point 3 as the Yellow Altar and point 4 as the Blue Altar. Point 1 is an entrance and point 5 is a second entrance. The drawing is a schematic. It has no native coordinate.

Brady printed 188, image b-189.png, footer 188. Step 7 is the White Altar in the Mage's Tower. Step 8 is the Yellow Altar in the catacombs. Step 9 is the Blue Altar in the catacombs.

L9_DR/markers.json and L10_DC/markers.json stay empty. A point on these sketches is not a native x,y, and no control in the exports is named as an altar. The oracle copy has 30 saves and none is named as the cemetery charger. DOSBox was not launched.
