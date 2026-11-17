# Journal-only walk, r19p2, 17 Nov 2026

Fact page for Saturday. Sol builds nothing from it before then. Header: X = Godot x, Y = Godot z, H = Godot y.

Build r19p2 `e44f9f26`. Save: the owner's latest autosave, sha `863675d4f2bb9a065ac2e3b26f5c93cec3fc9644adc948ec2313d85fb8f55d01`, area L14_HT, health 30, Human. The arrival stand was on the screen at 18:40Z. A keyed walk from that same file, at 19:33Z, stood rows 1 to 3. The save file was not written. Rows 4 to 11 were not reached.

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
| 4 | Huline Temple | Lower halls, the two machines. Not walked. The hanging opened. The walk then stopped in the spider corridor at X 1345.8 Y -5378.2 H 32.0, health 29, against a hive warrior. The machines were not stood at. | Still the two side notes. | The button by the body, the red mulch into the second machine, the statuette. HINTBOOK 4455-4473. BRADY step 84. | Main |
| 5 | Huline Temple | Bedroom, library, empty niche. Not walked. Not reached. | Still the two side notes. | The headboard, the two hallway buttons, the library button, the statuette in the empty niche, the second shard. HINTBOOK 4515-4527. BRADY steps 85-86. Step 85 is the coffin flute. | Main |
| 6 | Huline Temple | Spiral, after the scale. Not walked. Not reached. | Still the two side notes. The scale note, once he is at the bowls with a shard, does not mention the spiral. | Click the Dreamstone on the receptacle to raise the steps. BRADY printed 203, PDF PAGE 204, line 8253, and printed 215, step 87. | Main |
| 7 | Huline Temple | The three doors. Not walked. Not reached. | Still the two side notes. | The ledge path, the tilt room, and the fire paths, one idol from each. HINTBOOK 4536-4572. BRADY steps 88-90. | Main |
| 8 | Huline Temple | Flute slot and the blade hall. Not walked. Not reached. | Still the two side notes. | The flute in the angled slot, then the right-hand passage around the blades. HINTBOOK 4576-4585. BRADY step 91. | Main |
| 9 | Huline Temple | Boulder hall, before the stone moves. Not walked. Not reached. | Still the two side notes. The boulder note is not written on the way in. The script adds it only inside the kill box, and only for a short moment after the trap has already started. | Walk the side, not the centre. HINTBOOK 4586-4589. BRADY step 91, the two buttons. | Main |
| 10 | Huline Temple | Three pedestals. Not walked. Not reached. | Still the two side notes. | One idol on each pedestal. HINTBOOK 4594-4596. BRADY step 92. | Main |
| 11 | Huline Temple | Faux-Belial. Not walked. Not reached. | Still the two side notes. No fight note exists. | Beast form, then hack. Other forms lose. HINTBOOK 4616-4631. BRADY printed 203, the Hive Lord line before the Chamber of Voices. | Main |

## Keyed walk, 19:33Z

Same file. The running scene, not a second save. At every mark the Journal ids were still only `thohan_sword_broken` and `tavern_after_farewell`.

The screen at the bowls named the next action. Carry, place, take aloe, take the paint, offer aloe, offer poison. After the poison it said the floor begins to descend. It also showed a use line for the paint. That use was not pressed. MISSING HINT: at the slab the screen did not name Spark or Q. One Q was the ritual Spark aid. The screen then said the priest's body disappears, and it named the Lizard for the low passage.

The post named the green crystal shard. He took it. The screen after that was the key legend.

The left hanging then said it was drawn aside. Past it, in the spider corridor, the screen showed a hive warrior at 1500/1500 and said the warrior struck him. Health 29. The walk stopped there. That is not a player stop: nothing on the screen failed, and the warrior was in the way. Rows 4 to 11 were not stood at.

## Where the Journal does name the next step

Not stood in. Read from `l14_journal_hints.gd` and `l16_journal_hints.gd` on r19p2 `e44f9f26`. None of these ids are in the save.

- Scale bowls. In reach of tray 405 or 406, with a shard carried and the bowls not done: "The scale in the temple wants both crystal shards, one in each bowl, before the way behind it opens." That matches HINTBOOK 4528-4529 and BRADY step 87's first sentence.
- Hoppers. The platform in view, not done: "Five hopper bodies belong on the wooden platform. My own weight is not enough to make it rise." HINTBOOK 4600-4608.
- Chalice door. In reach, Dreamstone carried, Belial dead, stone not yet offered: "The Chamber of Voices takes the Dreamstone into the chalice, and the stone does not come back." HINTBOOK 4636-4641. BRADY lines 8259-8260.
- City main road. The road notes are written when the City map is up. The first is: follow the south avenue to the dry fountain, strike the ball, then the glass pyramid and hourglass. HINTBOOK 4784-4808 is that same first chore. Later road lines name the canal, the oil stair, the Dark Bow, the dragon, and the telepad. They do not name the four towers, the ivory chips, or the mantle. HINTBOOK 4692-4695 and 5266-5268 say the mantle comes before the dragon. That disagreement was not stood in. His Journal has no City line because this save is still the Temple.
