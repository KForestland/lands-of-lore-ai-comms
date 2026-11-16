# TUESDAY 17 NOVEMBER: play this (lead, written Monday 18:20Z)

```
~/lol2_playtests/play_r19o11.sh
```

Your saves from Monday evening are carried over. F10 where you stop or something looks wrong.

**What Monday's run found, and what this build does about it**
- **The freeze at the lake switch (Claw Mountains):** fixed. Pulling it started ten floor pieces that each re-read the whole level; the longest frame went from 2.6 seconds to 23 milliseconds, from your own save.
- **The river:** you had jumped from the floe at the bank five times, fallen short and dropped into the river bed with no way out. Now: the screen tells you where to step off the floe; snow steps lead from the river bed up onto the bank (hold forward); and the "E - Climb down to the icy gulch" line stays on screen while you stand at the ice opening (it had shown for one second).
- **The ice lake drawn wrong:** the platforms the switch raises were bare slabs over a hole. They are solid ice columns now. No frame of your longplay shows them raised, so the look is our best reading; say if it is wrong.
- **The Dreamstone holder** is empty once you have taken the stone.
- **The Dark Bow can now be held.** The robot, playing on from your state, reached Belial's Laboratory and found that the three slotted switches want a bow, and the Dark Bow from the City could not be put in the hand. Fixed: hold or equip either bow and shoot the three switches. After Belial's Horn the screen now names the corridor back to the barred door.
- **City of the Ancients:** this build has the wall rule (about 5,400 walls that used to let you fall through). Press E at the silent canal doors and **walk through the middle of the opened pair** (the sides are too narrow on this build). Stay off the starry floor.
- **Temple:** you clipped through a wall by the left wall hanging and stood outside the room. That is the same fault class as the City; the Temple's walls are being checked the same way. Not fixed in this build.

**Still true from before:** at the web press E and wait out the 70-second movie; heal before the boss; altar before the Dreamstone; at the Temple Hive Lord step onto open floor if G does nothing; lizard and a run-up to jump back up from the Temple's low passage; keep one Silverleaf.

**Robot on your own save (state Monday evening):** everything from the web through the City (dragon, telepad), the Hidden Caverns and into Belial's Laboratory (the Horn, the bars, the slotted switches, door 73, the head road), by real keys and the game's own saves. It is stopped at a golden wall further on in the Laboratory; I add below what that turns out to be.

**The big build (r19p)** with the belt, items, quest-item protection and the Citadel switches is not for today: its second full sweep showed eight new failures in the first half; they are being traced.

**Jobs only you can do**
- Security, ten minutes: the `AI_COMMS` folder's git settings hold a GitHub token in plain text. Revoke it on GitHub, make a new one, let a credential helper hold it. Ask me and I walk you through it.
- Decision: should the "E - Climb down" shortcut stay in Classic? I lean yes.
- Decision, later: the finale shows captions that narrate what happens. Keep them or not, once you have seen the ending.

Fallbacks: `play_r19o10.sh`, `play_r19o8.sh` (Monday's build), `play_r19o7.sh`.

Monday evening's note is kept as `FOR_OWNER_20261116_evening.md`.
