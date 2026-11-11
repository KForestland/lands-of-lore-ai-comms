# Q04 Health and mana at the Darker Jungle arrival

complete true

formula_finished false

The arrival HUD prints no health number, no mana number, and no level. Both bars are filled to the frame. A full bar is a fraction of the cap. It does not say what the cap is. No host.

## Longplay

Grade LONGPLAY. Frames are `~/lol2_original_screens/longplay_frames_act2plus/g_NNNNN.jpg`, 640×360. Clock `g_N = 6580+(N-1)*30` seconds, so `g_00001` is 109:40. The survey's L8 label is 109:46. The 30-second grid has no frame of the step out of the Huline jungle. `g_00001` is already the night clearing.

The bar row is y=350. The mana interior is x=465 through 507 (43 pixels). The health interior is x=528 through 598 (71 pixels). On the four frames below, every one of those pixels is the fill color. None is dark.

| Frame | Clock | Picture | Mana | Health | Number |
| --- | --- | --- | --- | --- | --- |
| `g_00001.jpg` | 109:40 | Night clearing, three figures, sword cursor | 43/43 | 71/71 | none |
| `g_00002.jpg` | 110:10 | Same clearing, hand cursor | 43/43 | 71/71 | none |
| `g_00004.jpg` | 111:10 | Trees, hand cursor | 43/43 | 71/71 | none |
| `g_00005.jpg` | 111:40 | Carved door and a pale figure | HUD not drawn | HUD not drawn | none |

`g_00001`'s HUD rectangle (x=430..629, y=300..359) contains no near-white pixel, so no digit is drawn there.

## Owner frames

Grade LONGPLAY. `~/lol2_original_screens/youtube_playthrough_20261110/`. The earliest Savage Jungle shot is `LoL2_P3_097_L8-SavageJungle_night_path_to_gate.png`, the player chrome reading 8:30 of 1:08:59. That is the path toward the gate, already inside the night jungle, not the exit step.

On row y=1883 the mana gold edge is x≈2552 and the health gold edge is x≈2956. The same edges are on 102 and 103.

| Frame | Mana | Health | Number |
| --- | --- | --- | --- |
| `LoL2_P3_097_L8-SavageJungle_night_path_to_gate.png` | Blue runs to the gold edge. The last ~40 px are darker blue (about 155) than the 254 of the rest. | Red runs to the gold edge. The last ~40 px are darker red (about 172) than the 253 of the rest. | none |
| `LoL2_P3_102_L8-SavageJungle_night_wall_torches.png` | Bright blue (b≈255) through x=2548, gold at 2552. 201 px. | Bright red through x=2928, then the cap, gold at 2956. | none |
| `LoL2_P3_103_L8-SavageJungle_lizard_creature_by_totem.png` | Bright blue through x=2548, gold at 2552. | Bright red through x=2948, gold at 2956. | none |

`LoL2_P3_098_L8-SavageJungle_dragon_gate.png` has no mana-colored run in the HUD band. That frame was not read as a bar.

The darker tail on 097 stays blue and stays red. It is not a black empty slot. 102 and 103 fill the same edges with the bright color. All three read as the whole bar.
