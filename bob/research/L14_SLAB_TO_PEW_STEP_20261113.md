# Temple slab room onto the pew floor

Read-only. No build. The question on the board at 2026-11-13T07:19Z is which original step puts the player from the slab room (floor −80) onto the pew floor (floor 0) after the priest is laid: (a) the floor-0 ritual floors, regions 801..861 including 856, are walkable at that phase and the port removes them too early or always, or (b) a climb from the −80 sheet (lips 3233/3234 at floor 70, or the floor-20 lips with flag `0x02`, byte `[0xB7D4D]`).

Answer: (a). In the longplay he is already standing on the room’s tile floor when the body is on the low rectangle. That floor is the walkable upper floor. The bowl commands are what lower it.

## Longplay

Frames are `~/lol2_original_screens/longplay_frames_act2plus/g_NNNNN.jpg`. Clock `g_N = 6580+(N-1)*30` seconds. This set is the AegisAmaranth “Most Difficult” longplay, video `xXNHBdF9rC4`. Images are 640×360 and have no burned-in dialogue. Samples are 30 seconds apart. Grade LONGPLAY for what is on the frame, LIKELY for the name of the body.

Opened for this note: `g_00190`–`g_00269` (3:24:10 through 4:03:40), plus the earlier pass `g_00270`–`g_00340`. The temple interior in this visit is `g_00247`–`g_00275`. Before `g_00245` the view is still the citadel, then ice, then the night jungle. After `g_00275` the view leaves through a cinematic into the ancient-city court. No second look at this room is in `g_00276`–`g_00340`.

`g_00247` at 3:52:40. First person, HUD up. Tan stone tiles, a red hanging with a gold serpent, a dark block wall. A grey-blue human-shaped mass lies on those tiles. The pink hand sits over it. The tiles run from the camera to the mass. He is on that floor.

`g_00251` at 3:54:40. Same HUD. The same kind of grey-blue mass lies lengthwise on a low dark stone rectangle. Tan tiles fill the foreground, so the camera is standing on them. The rectangle is a low step in that room. The view is not from the bottom of a pit, and the frame has no Climb text.

Between those two frames he opens the inventory (`g_00248`), passes the hanging cauldron (`g_00249`), and a rough rock opening (`g_00250`). Nothing on those three frames is a label, so the mass is LIKELY the priest and not a named object. No line of text on either body frame says “priest”.

After the rectangle he fights the green spiders (`g_00252`–`g_00261`), walks a vaulted stone hall at eye level on a continuous floor (`g_00262`, `g_00263`), and at `g_00267` (4:02:40) the hand is on the green crystal in the wooden post. `g_00268` is one low bench against a carved wooden wall, not a row of pews. No opened frame in this visit shows pew rows, two bowls together, the word Climb, or Luther looking up a lip out of a hole.

`g_00264` at 4:01:10 is a torn capture: black side bars, a floating band with one gold bowl and a green fill, and a dark band below. It is not used.

Pew rows were not in the 30-second samples. The stand the question asks for is the one beside the rectangle, and that stand is the upper tile floor.

## Bytes behind that picture

`TEMPLE_SLAB_PEW_20261112.md` already has the two sheets at `(2370, -3328)`: region 164 floor −80 and region 856 floor 0. The −80 sheet has no floor-0 neighbor. The pew way 856, 812, 816, 814, 821, and on to 1058 is wholly on floor 0. Those packed floors stay 0 until a command moves them.

Groups 14556 and 14868 in `scripts/lol2/native_scripts/L14_HT.json` on `b2b698c` are the same 23 opcode 196 commands. The accepted floor formula is a signed word at byte +4, byte 6 = 0, byte 7 = speed (`I03_starry_tower.md`). Applied here, not a new callee proof. The MIX was not re-opened this pass, so the export grade is LIKELY.

| Regions | Word |
| --- | --- |
| 861, 840, 833 | −10 |
| 839, 841, 834 | −20 |
| 801, 831, 855, 830, 836, 821, 856, 812, 816, 815, 814, 828, 851, 853, 845, 813 | −30 |

Region 821 is named twice. Region 856’s word is −30, not −80. Prop 369’s kind-3 value 2 names group 14556, and prop 370’s matching event names group 14868. Hintbook Chapter Twelve, `reference_hintbook/hintbook.txt` 4339–4355: drag the body onto the rectangle, walk east and north to the pews for the poison and the aloe, return, fill the bowls, and only then the floor around the rectangle descends. The book does not describe a climb.

Byte `[0xB7D4D]` stays UNKNOWN. The floor-70 lips 3233/3234 and the twelve floor-20 lips are real neighbors of the −80 sheet, and this visit does not show him using them.

## What the port does with the same floors

`act2_map.gd` skips a face the area owner claims, both for the static mesh (line 140) and for collision (line 237). `l14_priest_ritual.gd` owns every floor face whose region is in `FLOORS`, which is the same 801..861 set, from load. `restore` sets each ritual floor node to `FLOORS[id] * lowered / 2`. `lowered` starts at 0, so those nodes sit at y = 0 until both bowls are committed, then 856 moves to −30. The chain robot on `b2b698c` was already at y = −48, region 163, before the place. The rebuilt floor-0 faces were not the floor he was standing on. That is the port removing the upper floors from the map collision for the whole visit, which is (a).

## For Opus, after r19g

Build (a). The floor-0 ritual floors, 801..861 including 856, stay solid through the phase in `g_00247` and `g_00251`, which is before the bowls. The longplay stand is that tile floor, so the player can walk from the rectangle the way the frames walk on. The board’s climb line is the fallback for a picture this visit does not show. Grok does not build the floor or a climb.
