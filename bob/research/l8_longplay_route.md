# L8 longplay route to the Claw Mountains

Frames are `~/lol2_original_screens/longplay_frames_act2plus/g_NNNNN.jpg`, one every 30 seconds. Clock: g_N is 6580+(N-1)*30 seconds from the start of the video, and g_00001 is 109:40 (1:49:40). Pictures are 640x360. Nothing on these frames is burned-in dialogue. Names that are not drawn on the picture are marked HINTBOOK, from `~/AI_COMMS/reference_hintbook/hintbook.txt` lines 2866–3178. What the picture itself shows is LONGPLAY.

The 30-second grid misses lines of speech and short clicks. A step is listed only when a frame shows it, or when the book names a picture that was opened.

## What the player does

1. Arrival, g_00001–g_00004 (1:49:40–1:51:10). Night forest. g_00001: three humanoids around a low plant, sword cursor, Luther's portrait. g_00002: the same three, empty hand. g_00003–g_00004: a path and a tree, still the forest, hand cursor. HINTBOOK 2896–2924: this is Daniel and two companions; the blade is offered, hoppers break it up, and the blade is picked up again. The frames show the trio and then the path. They do not show the hoppers.

2. Huline Temple scene, g_00005–g_00007 (1:51:40–1:52:40). No portrait. g_00005 and g_00006: a pale figure on a round stone in front of wooden doors with a gold arch, and a lit brazier. g_00007: a larger horned creature on the steps, and a white body on the grass in front of the same doorway. HINTBOOK 2932–2945: the old priest speaks, then a Belial-like creature snatches him. LONGPLAY: the doors are in the scene. The player is not shown walking through them.

3. Outside again, g_00008 (1:53:10). Portrait is back. Forest, a trunk, hand cursor. The temple was not entered. The doors stay behind the scene.

4. Toward the village, g_00009–g_00014 (1:53:40–1:56:10). g_00009: a skull totem and one standing humanoid. g_00010: a dark frame, no portrait. g_00011: tall trunks with round platforms. g_00012–g_00013: a hut, a seated figure, hanging cords. g_00014: an armored cat-person beside a slat wall inside that hut. HINTBOOK 2924–2984 and 2988–2996: the visit is what lets the Wild Village be used; the guard wants Daniel's blade; the huts are the herbalist, the shaman, and Daniel. LONGPLAY shows the tree platforms and the hut after the scene, not an open temple.

5. The long middle, g_00017–g_00144 (1:57:40–3:01:10). Stone rooms, crates, a green reptile (g_00020 is that reptile against a stone wall, and the portrait is the red beast form), chairs, red floors, inventories, purple light, a pale standing figure (g_00120–g_00123), and a winged statue (g_00124). g_00138–g_00140 have no portrait: a body on rock, then a cyan underwater view. HINTBOOK 3000–3056: silverleaf does not grow until the Dracoid cemetery and the ruins, the wet exit, and Dawn taking the bracers. The frames show stone interiors, a fight, and an underwater shot. They are not labeled with room names.

6. Back in the jungle, g_00145–g_00161 (3:01:40–3:09:40). g_00145: a woman in a white blouse on a path, two pale objects behind her. HINTBOOK 3021–3033 names her Dawn, on the shore after the wet exit. g_00153 and g_00157: the tree platforms again. g_00156: a striped cat-warrior on a red floor. HINTBOOK 3069–3074: offering a silverleaf starts the initiation fight with Daniel. g_00160–g_00161: the hut again, a seated cat-person. HINTBOOK 3075–3076: the shaman then gives a potion for another silverleaf.

7. The way into the mountains, g_00163–g_00174 (3:10:40–3:16:10). g_00163: the inventory covers the right half; a red and green shape lies on the grass. That shape is not clear enough to name. g_00164 and g_00166 are forest. g_00169 (3:13:40): no portrait, a rock cleft opening onto snow. g_00170: snow peaks, still no portrait. g_00171–g_00172: the same woman standing in the snow, portrait back. g_00174: an ice fence over snow. HINTBOOK 3146–3166 and 3173–3178: the pass is across the river; Amaranth and a silverleaf are mixed; the dose is used on the Larkhon's upper chest; once it sleeps, the cave leads to the Claw Mountains, and the Larkhon wakes again after Luther leaves. The grid does not show the awake serpent or the click. It does show the cleft onto snow, then the snow with the woman, about three minutes after the village hut.

The temple doors are not the way to the Claw Mountains. From the scene at 1:51:40 until the snow at 3:13:40 the player is in the jungle, the village, and stone rooms. The doors in g_00005 are not crossed.

## Build, darker start

Compared on r19-work `0adf21a`, which contains `64e84ea` (the sealed-door sentence) and `14ddedd`. Commits after `14ddedd` do not change `l8_temple_door.gd`, `l8_journey.gd`, or `l8_journey_state.gd`.

The F2 start `act1-end-darker-jungle` has no `l8_journey` key. The visit has not run (`temple_visited` false, gift `unoffered`, not admitted). The blade is already in the pack. The village guard is not present. The temple door has no Dreamstone, so it is shut before the visit and it stays shut after the visit. That matches the frames: the scene plays, and the doors are not used.

The village still needs the visit. `show_guard` refuses without `temple_visited`. That matches the book (the visit is what opens the village) and the frame order (the hut is after g_00005–g_00007).

The first dead end is the line on that shut door. It said only the Dreamstone opens it. The Dreamstone is how the same door opens much later, after the mountains, which is true and is already the `64e84ea` sentence. It is not the next step. The frames go to the village. On this start the blade has not been given to Daniel, so the guard will not take it yet either. The village panel offered "Show Daniel's blade" and then refused with "The village encounter is not ready."

The fix leaves the Dreamstone sentence in place. Before admission it adds the next step: meet Daniel and take the blade back, or show it to the guard once it has been taken back. After admission the door line is only the Dreamstone sentence again. At the village, the panel says to meet Daniel instead of offering a blade the guard will not accept. The door still does not open.
