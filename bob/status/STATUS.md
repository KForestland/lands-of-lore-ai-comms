# LoL2 status, 2026-11-18 night (Opus for the lead)

**Build to play: r19p3** (launcher `play_r19p3.sh`, head 17ec1001; your saves are copied from your last play). Fallback: r19p2 (`play_r19p2.sh`).

## What r19p2 changes after your r19p play
- **Darker Jungle frame rate:** the belt looked up every carried item by name on every frame; it now remembers them. A new test fails if the game's own script work per frame grows again. It measures script time on a short walk from your saved spot, not the frame time you see (that includes drawing); The full frame where you stood is measured below.
- **The Atlas uncovers about three times as much as you walk** in the Jungle, the Hive and the Dark Halls. The Cave and the Museum keep the old rule (the wider one opened the Cave map too far out and left nothing to discover in the Museum).
- **The wrong Huline voice line is gone;** that line is silent until its sound is checked.
- **The clubhouse guard** appears only once you are a tribe member. Before that the doors say the clubhouse is reserved for members of the tribe. A dead guard stays dead.

## How r19p2 was checked
- **Targeted gates:** 153 item and level tests, then the new tests. Every level family has at least one item test.
- **Full sweep of every test (1425) on r19p2, head e44f9f26, finished 18 November: 1351 pass, 17 fail, 57 skipped** (they need inputs not on this machine). The last full sweep before it, on head f38664a2 (15 November), had 27 failing; 19 of those now pass. r19p itself (head 3e2e65c5) had no full sweep, only targeted gates; the last full sweep before this one ran on head f38664a2 (r19-work, 15 November) and had 27 failing tests.
  - **Caused by r19p2, and fixed for the next build:** a Hive recovery test that did not know the new Atlas rule; the record of deviations, which needed one file per row; and a quest-protection check that keeps a fingerprint of the item list and had to learn the new one. None of the three changes the game.
  - **Already failing before r19p2, with owners:** the tower descent on the Dracoid Ruins, where the fall recovery moves you (Opus finds the cause); one belt refusal test on the Cemetery (Sol); the item-grant census, which needs re-pinning after the quest-protection work (Sol); four older tests that also failed on f38664a2 (two Hive tests, a map index, a label).
  - **Older failures found by the sweep, not caused by r19p2** (they fail the same way on r19p): a Hive screen test that expects an old save message; four tests from the Claw Mountains, City, Belial's Laboratory and Museum work of the last days. Opus finds which change caused each.
- **Grok's replay on r19p2 by real keys:** the Atlas and the silent voice line pass. Frame time where you stood in the Darker Jungle: 196 ms on r19p, 139 ms on r19p2, on Grok's virtual display. Opus measured the same spot on another virtual display: 172 ms on r19p, 83 ms on r19p2, so about 12 frames a second, still slow. Drawing takes about 22 ms of that. Most of the rest is the 97 Darker Jungle creatures, all moved on every physics step even when far away. The lead decides whether that is fixed next. The clubhouse guard check is still open.
- **States:** READY and reviewed (in part). Not merged into r19-work. Not owner-played.

## r19p3, ready to play (head 17ec1001)
r19p2 plus: Sol's **Dark Halls crates** (E exposes the crystals; Dragon's Blood only when it can reach an exposed crate), the **brown-dirt floor** (the garden beds hold you), Sol's **Hive locks**, the clubhouse doors no longer offering "Open the door" to a non-member, and the test and record fixes above. All three Sol changes passed independent review.
- **Checked on head 17ec1001:** 300 Dark Halls, Hive, item, Atlas and recovery tests. All pass except 8 known failures that already failed on r19p, each with an owner (Opus: the four older ones; Sol: the item census and one belt refusal; two older Hive tests). The 14 Sol tests that use your saves passed once those saves were in place. Not owner-played.
- **Known, not fixed in r19p3:** at the Claw Mountains Citadel deck the screen does not name E. Aim at the deck and press E. The line "E — Enter the Citadel" comes in the next build.

## Dark Halls (Sol)
- After the crates and the floor: Rix, then wax handed over from the belt.

## Two questions for you
- **Dark Halls, the three ghosts and the orb:** what do you remember? What releases the door, and does the orb keep pulling ghosts in? The original script names one ghost for the door, and we will not guess the rest.
- **The belt:** which small alterations do you want?

## Also done today
- A publish check now refuses any code export that holds your saves or recordings, machine paths, or private details. Nothing has been published.

---

# Earlier: LoL2 status, 2026-11-15 23:5xZ (hand refresh, Opus for the lead)

**Build to play Monday: r19o4** (`play_r19o4.sh`, 9311792). Fallbacks: r19o3, r19o.

Four separate states (rule of 15 Nov): **READY** = a lane says it is built and names what was not run; **reviewed** = a second lane read or replayed it; **merged** = it is in r19-work; **owner-played** = you played it. A PASS is not "owner-played".

## Your verdicts, 15 November (your words)
- **Cave:** "Cave is complete." Signed off.
- **Museum:** "some minor issues with the Museum still" (glowing key on the active slot; the orb that raises the key from the floor; the switch for the door on the right).
- **Jungle:** "some issues with the Jungle" (textures at the river and cliff, tree foliage, transparent textures and water after the puzzle).
- **Darker Jungle (Savage Jungle, L8):** "the Darker Jungle needs work" (the hut mixer behind an invisible wall, the shaft).

## Per level

| Level | READY | reviewed | merged (r19-work) | owner-played |
|---|---|---|---|---|
| L1 Cave | yes | yes | yes | **yes, complete (15 Nov)** |
| L2 Museum | yes | yes | yes | yes, 15 Nov: minor issues |
| L3 Dark Halls | yes | yes | yes | yes, earlier: crates, barrels and box still open |
| L4 Jungle | yes | yes | yes | yes, 15 Nov: some issues |
| L5 Hive | yes | yes | yes | yes, earlier: Hive puzzle still open |
| L8 Savage Jungle | yes | yes | yes | yes, 15 Nov: needs work (hut mixer wall, shaft) |
| L9 Dracoid Ruins | yes | yes (robot main chain 12 Nov) | yes | not yet |
| L10 Cemetery | yes | yes (robot Emperor + rails) | yes; r19o yard-ledge and passage-door fixes are in | yes, 15 Nov (yard ledge, passage door: fixed in r19o) |
| L12 Claw Mountains | r19o4: READY | yes: Grok replayed on r19o4 by real input, no aid, the way back both ways (floe route, and E climb-down to the gulch) | **no**: the r19o4 fixes are on the playtest line only | partly, 15 Nov: you went up by an accident of the fall recovery; the real way UP has not been played by anyone |
| L13 Citadel | r19o4: READY | yes: Grok on your own Citadel save, door to Dreamstone to exit | **no** (r19o2-r19o4 Citadel fixes are on the playtest line only) | yes, 15 Nov (spell hints fixed in r19o) |
| L14 Temple | yes | Grok on your save: Temple door takes and returns the stone, inside the Temple; ritual onward still walking | yes (r19o) | not yet |
| L16 City of the Ancients | yes | robot oil, bows, centre, dragon (13 Nov) | yes | not yet |
| L17 Hidden Caverns | yes | robot (13 Nov) | yes | not yet |
| L19 Belial's Lab | yes | robot (14 Nov) | yes | not yet |
| L20 Birthing Chamber | yes | robot to the ending (14 Nov) | yes | not yet |

## r19o4 in the four states
- **READY:** yes. It was checked by targeted gates only: 109/113 on c7c46f8, its own two reds fixed in 9311792, and two baseline Journal-count reds.
- **Reviewed:** robot-replayed (Grok, real input, no aid) on your own save, from the Citadel door to inside the Huline Temple, including both ways back through the Claw Mountains.
- **Not full-swept.**
- **Not merged** into r19-work.
- **Not owner-played.**

## Open
- The L12 UP route (gulch, logs, ice bridge, floe, ice opening, tunnel, Citadel door) must be proven walkable before the last-safe-ground change merges.
- R130 (Sol's items and belt candidate): on HOLD for three test-side steps. There is no game defect.

Previous page (14 Nov): STATUS_20261114.md.
