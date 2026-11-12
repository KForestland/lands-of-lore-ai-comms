# Your job 2: look at your five Claw Mountains spots (about 5 minutes)

Build r19b has the fix for the ice walls and slabs you reported in the Claw Mountains on 12 November. Each command starts the game standing exactly where you pressed F10, paused, so you see the same view.

## Steps
Run these one at a time. After each, look, then close the game and run the next.

| Command | Your report | You wrote |
|---|---|---|
| `~/lol2_playtests/play_r19b_spot.sh 1` | 06-41-16 | "wall texture is wrong should not be there" |
| `~/lol2_playtests/play_r19b_spot.sh 2` | 06-41-39 | "wall texture should not be here" |
| `~/lol2_playtests/play_r19b_spot.sh 3` | 06-44-03 | "texture in the sky but can be hidden by more ice/rock textures" |
| `~/lol2_playtests/play_r19b_spot.sh 4` | 06-45-18 | "weird texture in the mountains" |
| `~/lol2_playtests/play_r19b_spot.sh 5` | 06-46-15 | "the map clips here ... make a tunnel here instead" |

- The game starts paused at your spot with the line "Loaded at your report - press any key to continue". **Look around with the mouse first**; spots 3, 4 and 5 are on the glacier, and the ice slide carries you away as soon as you continue.
- If the fault is gone: nothing to do, go to the next.
- If it is still there, or something else looks wrong or is missing: press **F10**, type a few words, confirm.

## What to tell the lead afterwards
One line is enough: "all five fine", or which numbers are not.

## Not in this build
The Temple fixes and the Cemetery objects. Those come later.
