# TUESDAY 17 NOVEMBER, afternoon: the big build is ready (lead, 14:00Z)

```
~/lol2_playtests/play_r19p.sh
```

Your saves are copied from r19o12 (your play this morning). F10 where you stop or something looks wrong.

**What is new for you in r19p**
- **The item belt:** five slots at the bottom, the middle one is active; roll through it; **F uses the active item on yourself**; E at a target uses the item it needs from your pack even if it is not the active one.
- **Quest items are protected:** the game will not let you eat, throw, drop, give or sell the last copy of something the main quest still needs, and it says why. Nothing is used up when it would do nothing (aloe at full health).
- **Glass globes** charged at the Cemetery altars are stored spells: cast, recharge, save in between.
- **Every closed door or gate that E opens says so,** on every level.
- **Journal directions** along the City main road and through the Caverns, Belial's Laboratory and the last level.
- **The Citadel's original switches** work, including the black one (it wakes the bridge; ours starts by itself, so it tells you that).
- **City of the Ancients:** walls and low steps hold; the canal doors fold back to the frame.
- Everything from r19o9-r19o12: lake switch, river steps, climb-down line, ice columns, empty Dreamstone holder, Dark Bow, the Laboratory ramp fence.

**Known, not fixed in this build**
- Claw Mountains tower descent: a fall can still move you across the level.
- The Temple: clipping and the "overlapping" look (walls and ceilings are being closed; not in this build).
- The river bank steps are a workaround, as you said.
- The final level can be skipped: after the birth the end card is two E presses away. Being worked on as main-quest work.
- The Blizzard axe still comes from the lever; it moves to the end of the lake's jumping puzzle next.

**How it was checked:** three full sweeps (the last one clean except the known tower fault), independent reviews of the item protection, the recorder and the switches, and the robot played the belt, the protection, the globes, the City and the doors by real keys and said MERGE. You are the first person to play it.

**Saturday 21 November: the review you called** (Act 2 workarounds, Act 2 in pieces, the Claw return, items). The fact pages are being collected in `AI_COMMS/sol_lane/review_20261121/` and `AI_COMMS/grok_research/`.

**Jobs only you can do**
- Security, ten minutes: the `AI_COMMS` folder's git settings hold a GitHub token in plain text. Ask me and I walk you through replacing it.
- Decisions: should the "E - Climb down" shortcut stay in Classic (I lean yes); the brazier in the Hive alcove (what belongs there); finale captions, once you have seen the ending.

Fallback: `play_r19o12.sh` (what you played this morning). The morning's note is kept as `FOR_OWNER_20261117_r19o12.md`.
