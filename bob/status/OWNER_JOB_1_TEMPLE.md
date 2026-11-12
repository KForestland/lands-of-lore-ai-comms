# Your job 1: mark where the Huline Temple clips (about 15 minutes)

**Do not start until the lead says build r19a is ready.** The build you have now has no Temple start.

## Why
We are about to rebuild how the game decides which rooms are solid. Before that, we need to know exactly which spots look or feel wrong to you, so we fix those and can check afterwards that they are gone.

## Steps
1. Start the game with `~/lol2_playtests/play_r19a.sh`.
2. Press **F2** and choose **"Act 2 - Huline Temple, arrival (full health)"**.
3. Walk the Temple as you normally would. You do not need to solve anything.
4. Every time rooms clip into each other, a wall or floor from another room shows through, or you walk into something that is not there: stop, face it, press **F10**, type a few words ("wall from other room", "floor shows through", "invisible wall"), and confirm.
5. Stop after about 15 minutes, or earlier if you have marked the places you remember.

## Good to know
- F10 now also saves your exact situation (a save, your last inputs, a few frames), so we can load the same spot. You do not need to describe where you are.
- If you fall through the world or get stuck, press F10 there too, then F2 back to the Temple start.
- Three places we suspect, if you want to look at them: east of the three trial doors; one block south of that, toward the shard bowls; and the corridor north of the rolling boulder, south of the idol pedestals.
- If nothing clips for you, that is a useful answer too: tell the lead "Temple looked fine".

## What happens next
The lead sorts your marks into kinds within the hour. The collision rebuild is then tested against exactly those spots, and you get the Temple again afterwards for a two-minute check.
