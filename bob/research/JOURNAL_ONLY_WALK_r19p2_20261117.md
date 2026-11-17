# Journal-only walk, r19p2, 17 Nov 2026

Fact page for Saturday. Sol builds nothing from it before then. Header: X = Godot x, Y = Godot z, H = Godot y.

Build r19p2 `e44f9f26`. Save: the owner's latest autosave, sha `863675d4f2bb9a065ac2e3b26f5c93cec3fc9644adc948ec2313d85fb8f55d01`, area L14_HT, health 30, Human. The arrival stand was on the screen at 18:40Z. A keyed walk from that same file, at 19:33Z, stood rows 1 to 3. A later keyed walk, at 20:34Z, stood rows 4 and 5. A keyed walk at 21:11Z stood the niche, the scale, the spiral, and the three doors. A plain walk then left the ledge maze. The owner's save file was not written. Rows 8 to 11 were not stood.

The sheet he holds has two notes and no Temple note and no City note:

- Thohan's blade is past his forge. The magic seller might mend what steel cannot, and he will name a Power Orb as his price.
- Bacatta's goodbye had the weight of a last word. The tavern is no place for me now; its people talk.

The Thohan sentence and the magic seller are one side chain. The note is `thohan_sword_broken` in `weapon_shop_state.gd`. The seller is the person that same note names, and the Power Orb is his price. BRADY printed 212, PDF PAGE 213, step 70, treats a repaired Thohan sword as optional beside the Great Sword. It is not the Temple main quest. The tavern sentence is `tavern_after_farewell` in `monastery_quest_state.gd`, Bacatta's farewell, also side.

The save already has the Temple door receipt: `l8_temple_door` slot `temple:entrance1198` is committed and empty, and `act2:L13_RC:dreamstone` is still carried. There is no `l14` quest key. The carried list and the collected list have no aloe leaf, no poison paint (`weapon_poison` paint 0, sac 0), and no crystal shard. `monastery:item94:Iron_Flute` is collected. That id is the monastery flute. The book still tells him to find a flute in the Temple coffin.

## Gap rows

A gap is a stand where this Journal, and the Temple notes the build can add, do not name the next action. The four Temple notes in `l14_journal_hints.gd` are absent from the save. They are named in the last section, where the script does speak.

| # | Level | Stand | What the Journal says | What the main quest needs next | Main or side |
| --- | --- | --- | --- | --- | --- |
| 1 | Huline Temple | Arrival court, region 864, X 2406.7 Y -2415.7 H 32.0. Played. Round stone court, a willow, blood on the floor. The screen showed Dampen charm, used, the belt line Broken Thohan, and the key legend. It named no action. E was not pressed. | The two side notes above. Neither says how to go on, or where the seller stands. | The door step is already in the save (BRADY printed 214, PDF PAGE 215, step 81). Next is the priest's body near the entrance: pick it up and take it to the low slab. HINTBOOK chapter 12, lines 4306-4344. | Main. The notes on the sheet are side. |
| 2 | Huline Temple | Slab room, the two bowls. Walked. X 2424.6 Y -3600.9 H 30.5, health 30. The screen named carry, place, both supplies, both offerings, then The floor begins to descend. | Still the two side notes. No ritual note exists. | Aloe in the western bowl, poison in the eastern bowl, then a spark on the body. HINTBOOK 4348-4355. BRADY steps 82. | Main |
| 3 | Huline Temple | Healing pool, the wooden post. Walked. X 3045.6 Y -5684.9 H 76.8, health 30. The screen named the green crystal shard and he took it. After that, the key legend only. | Still the two side notes. | The first crystal shard, from the wooden post by the pool. HINTBOOK 4376-4377. BRADY step 83. | Main |
| 4 | Huline Temple | Lower halls, the two machines. Walked at 20:34Z. The hanging opened. In the spider corridor the screen showed the hive warrior at 1500/1500 and said he struck. Health fell to 27 while a run past failed, then a mouse fight dropped the warrior and health was 20. The pedestal button said the body moves onto the grinder's belt, at X 2198.5 Y -3896.9 H -48.0. The trough slid in. The statuette was taken. The coffin flute was not named, so it was not taken. | Still the two side notes. | The button by the body, the red mulch into the second machine, the statuette. HINTBOOK 4455-4473. BRADY step 84. | Main |
| 5 | Huline Temple | Bedroom, library, and the niche. Walked. Bedroom at X 2194.5 Y -5236.9 H 152.0, health 30. The screen said the headboard was pushed aside. One hall button said the stairs descend. The next said the library door opens. The exit button said the library exit opens. The niche said the statue fits and a crystal rises on the pedestal. The second shard was taken at X 2777.6 Y -3899.2 H 12.0, and the screen said Cry shard taken. The coffin flute was not named, so it was not taken. | Still the two side notes at the bedroom. The scale id appears later, at the bowls. | The headboard, the two hallway buttons, the library button, the statuette in the empty niche, the second shard. HINTBOOK 4515-4527. BRADY steps 85-86. Step 85 is the coffin flute. | Main |
| 6 | Huline Temple | Spiral, after the scale. Walked at 21:11Z. Both bowls held a shard. The screen said the passage opens behind the bowls. At the slot, X 737.8 Y -3453.0 H 32.0, it said the spiral staircase rises, then he took the Dreamstone back, and it said the spiral is open. He climbed the stair to H 232. The marker at X 606 Y -3464 was not entered. | The running list gained `l14_scale_bowls`. The HUD at the slot did not print that sentence. | Click the Dreamstone on the receptacle to raise the steps. BRADY printed 203, PDF PAGE 204, line 8253, and printed 215, step 87. | Main |
| 7 | Huline Temple | The three doors. Walked at X 36.0 Y -2247.7 H 222.0, health 30. The left-hand door said it opens onto the ledge maze. The last floor was X 1183.1 Y -1945.3 H 172.0. He then fell off that ledge into empty space. The body ended at X 2701.2 Y -3092.2 H -376.8, health 30. The map has no floor in that column. The screen showed the key legend, Dreamstone, and Dampen charm. The location line read H -327.4. There was no fall line and no recovery. He cannot walk back up. STOP. | The running list still had `l14_scale_bowls` plus the two side notes. The HUD named no new sentence. | The ledge path, the tilt room, and the fire paths, one idol from each. HINTBOOK 4536-4572. BRADY steps 88-90. | Main |
| 8 | Huline Temple | Flute slot and the blade hall. Not stood. The ledge maze was left on a plain walk. | The running list had the scale id by then. The stand was not reached. | The flute in the angled slot, then the right-hand passage around the blades. HINTBOOK 4576-4585. BRADY step 91. | Main |
| 9 | Huline Temple | Boulder hall, before the stone moves. Not stood. The ledge maze was left on a plain walk. | The running list had the scale id by then. The stand was not reached. The boulder note is not written on the way in. | Walk the side, not the centre. HINTBOOK 4586-4589. BRADY step 91, the two buttons. | Main |
| 10 | Huline Temple | Three pedestals. Not stood. The ledge maze was left on a plain walk. | The running list had the scale id by then. The stand was not reached. | One idol on each pedestal. HINTBOOK 4594-4596. BRADY step 92. | Main |
| 11 | Huline Temple | Faux-Belial. Not stood. The ledge maze was left on a plain walk. | The running list had the scale id by then. The stand was not reached. No fight note exists. | Beast form, then hack. Other forms lose. HINTBOOK 4616-4631. BRADY printed 203, the Hive Lord line before the Chamber of Voices. | Main |

## Keyed walk, 19:33Z

Same file. The running scene, not a second save. At every mark the Journal ids were still only `thohan_sword_broken` and `tavern_after_farewell`.

The screen at the bowls named the next action. Carry, place, take aloe, take the paint, offer aloe, offer poison. After the poison it said the floor begins to descend. It also showed a use line for the paint. That use was not pressed. MISSING HINT: at the slab the screen did not name Spark or Q. One Q was the ritual Spark aid. The screen then said the priest's body disappears, and it named the Lizard for the low passage.

The post named the green crystal shard. He took it. The screen after that was the key legend.

The left hanging then said it was drawn aside. Past it, in the spider corridor, the screen showed a hive warrior at 1500/1500 and said the warrior struck him. Health 29. The walk stopped there. That is not a player stop: nothing on the screen failed, and the warrior was in the way. Rows 4 to 11 were not stood at in that life.

## Keyed walk, 20:34Z

Same owner's file, sha unchanged, and the file was not written. The running scene. At every mark the Journal ids were still only `thohan_sword_broken` and `tavern_after_farewell`.

The corridor warrior blocked a run past at X 1348.1 Y -5377.6 H 32.0, health 27, warrior 1500/1500. The screen had said he struck. One mouse fight then dropped him. Health 20. No reload. MISSING HINT: the screen did not name F5. Before the fight it said L14_HT preview saved. That slot is the game's own slot 1 from this walk, sha `7aa6c2e585de62038f8b9ba3316cf35a9ba41d927d0dce2c99beb2d3c5c8a956`, stand X 1344.0 Y -5207.4 H 32.0.

The machines named the pedestal button, the filled trough, and the long edge. The button's line was that the body moves onto the grinder's belt. The statuette's line was Statuette taken, at X 3347.1 Y -3616.3 H -23.0.

The bedroom named the headboard and said it was pushed aside, at X 2213.9 Y -5232.2 H 152.0. The hall button said the stairs descend, at X 2422.7 Y -5271.6 H 32.0. A later press said the library door opens. Further presses said the door is already open. The niche was not stood at in that life. The screen there named no action. Rows 6 to 11 were not stood at in that life.

## Keyed walk, 21:11Z

Same owner's file, sha unchanged, and the file was not written. Step budget 1800. The running scene.

The library exit button said the library exit opens, at X 1725.5 Y -4892.1 H 84.0. The niche said the statue fits and a crystal rises on the pedestal. The pedestal shard was taken when the screen said E, Take Cry shard, and then Cry shard taken, at X 2777.6 Y -3899.2 H 12.0. Both bowls then held a shard. The second bowl said the passage opens behind the bowls. The Journal list gained `l14_scale_bowls`. The HUD did not print that note's sentence.

At the slot, X 737.8 Y -3453.0 H 32.0, the screen said the spiral staircase rises, take back the Dreamstone. He took it back. The screen then said the spiral is open. He climbed the stair to H 232 and crossed the bridge. The three doors stood at X 36.0 Y -2247.7 H 222.0, health 30. The left-hand door said it opens onto the ledge maze.

A plain walk left the last ledge floor at X 1183.1 Y -1945.3 H 172.0 and fell into empty space. The body ended at X 2701.2 Y -3092.2 H -376.8, health 30. The map has no floor in that column. The screen showed the key legend, Dreamstone, and Dampen charm, and the location line read H -327.4. There was no fall line and no recovery. He cannot walk back up. STOP. Rows 8 to 11 were not stood. MISSING HINT: the screen did not name Spark, and it did not name F5. Before the corridor fight the screen said L14_HT preview saved. The game's own slot 1 from this walk is sha `6e2abd52e2b298b36522bb0ecbb8bc2927a338f4c403be42c3ea29e25002ef67`, stand X 1344.0 Y -5207.4 H 32.0.

## Where the Journal does name the next step

Read from `l14_journal_hints.gd` and `l16_journal_hints.gd` on r19p2 `e44f9f26`. The owner's file still has none of these ids. The running scene gained `l14_scale_bowls` at 21:11Z.

- Scale bowls. In reach of tray 405 or 406, with a shard carried and the bowls not done: "The scale in the temple wants both crystal shards, one in each bowl, before the way behind it opens." That matches HINTBOOK 4528-4529 and BRADY step 87's first sentence. The id appeared in the running list. The HUD did not print the sentence.
- Hoppers. The platform in view, not done: "Five hopper bodies belong on the wooden platform. My own weight is not enough to make it rise." HINTBOOK 4600-4608.
- Chalice door. In reach, Dreamstone carried, Belial dead, stone not yet offered: "The Chamber of Voices takes the Dreamstone into the chalice, and the stone does not come back." HINTBOOK 4636-4641. BRADY lines 8259-8260.
- City main road. The road notes are written when the City map is up. The first is: follow the south avenue to the dry fountain, strike the ball, then the glass pyramid and hourglass. HINTBOOK 4784-4808 is that same first chore. Later road lines name the canal, the oil stair, the Dark Bow, the dragon, and the telepad. They do not name the four towers, the ivory chips, or the mantle. HINTBOOK 4692-4695 and 5266-5268 say the mantle comes before the dragon. That disagreement was not stood in. His Journal has no City line because this save is still the Temple.
