# TUESDAY 17 NOVEMBER, evening: r19p2 is ready (lead, 17:15Z)

```
~/lol2_playtests/play_r19p2.sh
```

Your saves are copied from your r19p play today. F10 where you stop or something looks wrong.

**What r19p2 changes after your play today**
- **The slow, shaking Darker Jungle should be better.** The belt looked up every carried item by name on every frame; that is fixed. At your own spot the robot measured r19p2 about 30% faster than r19p (139 against 196 ms on its slow software display). The speed test measures script time on a walk from your spot, not real frame time, so your own eyes decide this one.
- **The Atlas uncovers more as you walk** in the Jungle, the Hive and the Dark Halls (a Jungle walk showed 4 areas, now 12). The Cave and the Museum keep the old rule: there the wider rule opened the whole map at once.
- **The wrong voice clip is gone** (it is silent there now).
- **The clubhouse guard only lets tribe members through;** the two doors give his line, and a dead guard stays dead.

**Not in r19p2 yet (Sol is building them in this order):** Dark Halls chests and crates that cannot be primed; the hole at the brown dirt (cause found: the garden-bed floor had no collision); Rix; wax handed over from the belt.

**Checked how:** 153 item and level tests plus the new speed test; three fail the same way on r19p. The full sweep of every level (1,425 tests) is two-thirds done with 14 failing: 6 known from before, 3 test-side faults already fixed for the next build, 1 for Sol, and 4 older ones that are also failing on r19p and are being traced. None of the 14 comes from a fault r19p2 added to the game.

**Two questions when you have a minute**
- Dark Halls: what do you remember about the three ghosts and the orb (what releases the door, does the orb keep pulling ghosts in)? The original script names one ghost for the door and we will not guess the rest.
- The belt: which small alterations do you want?

Everything below is this afternoon's r19p note and still holds.

---

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

**How it was checked:** three full sweeps of earlier versions of this build (CORRECTION 17 Nov evening: the final r19p itself never had a full sweep; the last one was 55 changes earlier, and four tests that fail today were not seen then), independent reviews of the item protection, the recorder and the switches, and the robot played the belt, the protection, the globes, the City and the doors by real keys and said MERGE. You are the first person to play it.

**Saturday 21 November: the review you called** (Act 2 workarounds, Act 2 in pieces, the Claw return, items). The fact pages are being collected in `AI_COMMS/sol_lane/review_20261121/` and `AI_COMMS/grok_research/`.

**Jobs only you can do**
- Security, ten minutes, a job only you can do: ask me in the chat and I walk you through it. (Details are not written here because this folder is mirrored publicly.)
- Decisions: should the "E - Climb down" shortcut stay in Classic (I lean yes); the brazier in the Hive alcove (what belongs there); finale captions, once you have seen the ending.

Fallback: `play_r19o12.sh` (what you played this morning). The morning's note is kept as `FOR_OWNER_20261117_r19o12.md`.
