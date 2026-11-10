# BJ14: stops and fix plan, village -> sleeping Larkhon -> Claw Mountains (Fable plans, lead builds)

Written 2026-11-10 by Fable from `BJ14_LARKHON_TO_CLAW_20261110.md`, for an engineer who has not seen my session.
Base walked: r19-work `bf8b21f`, worktree `~/opus_work/lol2_bj12`, branch `bj14-survey`. No game code was touched; the survey tools live in `tmp/bj14/` (untracked).
Limits kept: max 2 Godot, MemAvailable >= 10 GiB before each launch, `--audio-driver Dummy`.

Grades: **PROVEN** = I ran it today on real input; **LIKELY** = read in code, not run; **UNKNOWN** = not confirmed.

---

## 0. The short answer

**The whole chain can be walked on real keys and mouse and ends in L12, but only with two things a player does not have.**
Every quest step itself works on real input: every E, Q, Ctrl+Q, click, drag and right click on the chain did what it should.

What stops a real player, in order of weight:

1. **Luther dies to the Jungle's roaming creatures before he reaches the village.** (PROVEN) From the F2 start with no help, he died 7 times in a row at (328, -3381), 1,160 units short of the village point. This is the first stop of the chain and the biggest.
2. **He falls through the world on the Cemetery catacomb stairs** when the body-fit code is on. (PROVEN) This looks like the class Sol's unmerged body-fit fix covers, on a map that fix does not list (L10). See S5.
3. **The two stone squids at the Ruins opening** cannot be beaten with the mana Luther has. (PROVEN)
4. **Eleven places take E (or a click) but show no prompt**, so the player is not told the step exists. None of them is broken.

Fight-Daniel on real input: **works** (left clicks took Daniel 600 -> 0, Luther 500 -> 204; E leaves the arena).
Activate on real input: **works** (pack, wheel-scroll to the vapors, click "Activate vapors"; then right click on the Larkhon's upper chest put it to sleep; walked through the cave into L12).
Drag to mix on real input: **works** (serum dragged onto a Silverleaf in the pack made the vapors). The shaman's-table button works too.

---

## 1. How the walk was done, and what was not player-pure

One rendered Godot on a private Xvfb (`tmp/bj14/run.sh`), so the mouse is really captured. A bot (`tmp/bj14/bot.gd`, legs in `survey.gd` and `s1.gd`) sends key and mouse events: held W/Shift/Space/Ctrl, mouse motion to turn, E/Q/1/2/I/R/Enter/Esc, left and right clicks. Physics, creatures and the game's own level changes all run. The pack drag went through X11 (xdotool), because Godot only performs a drop for window events.

The walk ran in sittings, each from the save the one before wrote: F2 start -> village -> Daniel -> temple -> village (sigil) -> Cemetery gate -> catacomb -> Jungle pit -> Ruins x4 and Cemetery x4 -> flood escape -> shore and Dawn -> Cemetery (Emperor, nine leaves) -> village (initiation, serum, mix) -> activate -> river -> Larkhon -> L12 at (-345, -31, -5603).

**Declared aids (three, all survey-wide):**

| Aid | Why it was unavoidable | Where used |
|---|---|---|
| Body fit switched off (`scene.body_fit = null`) | With it on, Luther falls through the world on the L10 catacomb stairs (S5) | Every map, from the Cemetery gate on. The first sitting up to the gate also ran with it off |
| Health topped up to 30 when it fell under 12 in a fight | Without it the walk ends at S1, S4 or S6. Counted | 16 times start -> gate; about 35 in the last Cemetery and Jungle leg; 8 from village to Larkhon; more in the Ruins |
| A save per leg through the game's quicksave path (`_quicksave_unrecorded`) | To resume a sitting after a bot fault | Between legs. A player would use F5 |

Also: the bot wore the Burnt Chain (equipped through the pack) and kept the Max Spark aura up (Shift+Q) near enemies. A player can do both, but nothing tells him to.

**Not confirmed:**
- No run without the health aid got past S1. So "the chain is completable by an unaided player" is NOT shown; the opposite is.
- I did not look at rendered frames. Every "the player sees" below is the on-screen text the game set, read from the Labels, not a picture.
- One run ended oddly: on arrival in the Ruins mirror room (fourth visit) the scene was freed while Luther stood still casting Heal (keys 2, Q). The same leg from its save ran clean. UNKNOWN cause; could be my tool. Listed as N9.
- The flood escape passed once on real input; I did not measure how much time a first-time player has.
- R (recover here) failed to revive three times in a row at (729, -3223) among three creatures, then worked. LIKELY the creatures killed him again inside the bot's wait; not proven.

---

## 2. Stop list in chain order

"Sees" is the text on screen. Coordinates are (x, y, z).

### Stops that end the walk for a real player

**S1. Jungle, start -> village. Roaming creatures kill Luther.** PROVEN.
- Sees: "<name> struck you." then "You fell. R: recover here · F9: load save".
- Cannot: reach the village. R revives him in place among the same creatures; he died 7 times at (328, 32, -3381) on creatures 52, 54, 59. The first fight is creature 81 (500 health) at (-3910, 0, 1263), 670 units from the start.
- Why: 61 roaming creatures with 200 health each (`scripts/lol2/act2_populations/L8_SJ.json`, definitions 9, 10, 11; five stand at 279..1072, -3244..-3698 on the village approach). Luther has 30 health and hits for 8, so one creature takes 25 blows and each blow on him costs about half his health unarmoured. Damage lands at `scripts/lol2/scripted_creature_population.gd:198-200`; R at `:401-403` restores health but does not move him or the creatures.
- With armour, the aura and the health aid he passes (16 top-ups to the Cemetery gate).

**S2. Jungle, arrival from the Cemetery at (3972, 32, -2482).** PROVEN. Same cause as S1; creatures 68-70 stand at (3882..3957, -1169..-1529). Death loop without the aura; passes with armour and Shift+Q.

**S3. Jungle, Cemetery gate -> village with the nine leaves.** PROVEN. Same cause; died at (729, 32, -3223) on creatures 54, 55, 56.

**S4. Ruins opening, two stone squids (actors 61 and 68, 800 health each).** PROVEN.
- Sees: the squids strike; "You fell."
- Cannot: kill both. Killing one under the aura used all the mana; he then died six times at the second. `scripts/lol2/act2_populations/L9_DR.json` actors 61 at (156, -398), 68 at (102, 403).

**S5. Cemetery, catacomb stairs. Luther falls through the world.** PROVEN, and this is the body-fit class.
- Sees: the view drops; he is put back at (-542, 32, -856).
- Cannot: go down the stairs. Walking near (1335, -1315) he falls near (1126, -1376), every time.
- Why: `scripts/lol2/act2_body_fit.gd`. With `scene.body_fit = null` the same walk passes at height 31-32. Sol's unmerged fix names L12 gulch, L14 and L16; **this is L10, so check that fix covers it**. I moved on with body fit off, as the brief says.
- Two more falls of the same kind off the route: Jungle near (3161, 28, -1505) and Cemetery near (1, 42, -1094).

### Steps that work but are not offered on screen (the player is not told)

| # | Where | Sees | Cannot know | file:line |
|---|---|---|---|---|
| S6 | Cemetery, world items: gold globe 44, globes 56, 8, 45, 9, empty globe 43. Ruins: the bracers | Only the base line "Tab — Interface · M — Atlas ..." | That E takes the item (reach 96, aim 0.97). After E: "<item> taken." | `scripts/lol2/act2_world_items.gd:84-90` (no hint Label in the file) |
| S7 | Cemetery, winged statue (control 150), every visit | No prompt. After E: "You use the passage control." | That E works; the hint book says to walk into it | `scripts/lol2/act2_progression.gd:1312-1331` |
| S8 | Cemetery, both fences (74 and 174) | Nothing | That a sprint jump with **Ctrl held** in the air crosses them. Shift+W, Space, Ctrl worked both times | `scripts/lol2/l10_fences.gd:33-43` |
| S9 | Ruins, noble house rail | Nothing before; "The rail breaks." after a left click | That a left click breaks the rail and that this is the way on | `scripts/lol2/l9_noble_rails.gd:38-48` |
| S10 | Cemetery, priest with the ashes | "Take the ankh. Use it on the slab beside my tomb." on the first E **and** the second; after the first the ankh is not in the pack yet | That a second E is needed | `scripts/lol2/l10_priest.gd:61-76` |
| S11 | Cemetery, slab beside the priest's tomb | No prompt at all | That E with the ankh opens the Emperor's tomb | `scripts/lol2/l10_emperor_entry.gd:60-73` (no hint Label in the file) |
| S12 | Ruins, after the statue fight | "Water begins to rise in the ruins." | Where to go. The way out is a jump from the low roof at (2280, -9340) onto the table at (2440, -9260), ride it up, jump into the tunnel, walk to the raft. Late = "You drowned. F9 loads your earned save." | `scripts/lol2/l9_escape.gd:58-69` |
| S13 | Jungle shore, after giving Dawn the bracers | "Dawn accepts the bracers and explains reflecting magic. She gives you a Control Token ..." The Journal does not change | That the next step is the Emperor in the Cemetery. The old note "Dawn on the river wants the bracers" is still the last one | `scripts/lol2/l8_dawn.gd:33-38`, `scripts/lol2/l8_tribe_dawn_hints.gd:9` |
| S14 | Arena, after the bout | "E — Listen" and "E — Return to the village" together | Why the first E does not leave: it starts a Huline's speech ("Enter — Skip speech"). The second E leaves | `scripts/lol2/l8_huline_speech.gd:56`, `scripts/lol2/l8_tribe.gd:87,93` |
| S15 | Village, back from the arena at (531, 32, -4414) | "You return to the Wild Village after your initiation." and no prompt | That the village point is 192 away (reach is 160), and that the shaman is next | `scripts/lol2/l8_tribe.gd:110`, `scripts/lol2/l8_journey.gd:6-7` |
| S16 | Pack with 20 items | The vapors (and the serum) sit on row 6; five rows show | That the list scrolls. The wheel works | `scripts/lol2/museum_inventory.gd:63-70` |

### Notes (not stops)

- N1. Each of these told the player the next step and worked: guard ("l8_guard_wants_blade_back"), Daniel, temple, "Show Daniel's blade", shaman's sigil, Journal "l8_cemetery_gate_east", main gate "E — Unlock with the Dracoid Sigil", Emperor's inner door "E — Use the ankh", Emperor "E — Take the Emperor's remains", statue bowl "E — Offer the Emperor's remains", Dawn "E — Give Dawn the Bracers of the Dead", Emperor without bracers ("Silverleaf begins growing ..." + Journal "l10_silverleaf_grows"), "E — Pick Silverleaf" (9 of 9), "Present a Silverleaf — the initiation begins", "Offer a Silverleaf — he gives the Amaranth Serum", the mix line ("Activate them from the pack, then use them on the Larkhon's upper chest"), "Activate vapors", "Right click — Apply activated vapors to the Larkhon's upper chest", "The Larkhon falls asleep. The cave entrance is clear."
- N2. The river: "E — Chop the tree" shows at the bank; a sprint jump from (5130, 1880) also crosses. Nothing says which bank.
- N3. Arrival in L12 shows no line and adds no Journal note. The last note is still "larkhon_vapors_unactivated".
- N4. E to yield does nothing before the first blow (`l8_tribe.gd:59`), with no line. After one blow, E ends the bout and Luther is accepted all the same.
- N5. The shaman's lines skip with Enter.
- N6. Luther can walk under the lift table in the flood room (table top at 59).
- N7. The walking statue (actor 76, 200 health) can be aimed at; my one left click did not take health off it this run. The earlier code read says it is killable, which would end the chain. UNKNOWN; worth one test.
- N8. The Journal still says a "dampen spell" is needed in the Ruins; none was.
- N9. The scene freed once on arrival in the mirror room while healing (section 1). Not reproduced.

---

## 3. The player contract

| # | Step | Contract | Today |
|---|---|---|---|
| C1 | Walk the Jungle from the F2 start | A careful player with the starting kit reaches the village alive, and a death does not loop | Dies in a loop (S1-S3) |
| C2 | Catacomb stairs | Luther walks down | Falls through with body fit on (S5) |
| C3 | Ruins opening | The squids can be beaten or passed with the starting kit | Not with 30 health and the starting mana (S4) |
| C4 | Anything that takes E, a click or a special move | A prompt says so when the player faces it | Eleven places are silent (S6-S16) |
| C5 | After each quest step | A screen line or a Journal note names the next place | Missing after Dawn (S13), after the arena (S15), after the statue fight (S12), on arrival in L12 (N3) |
| C6 | Fight Daniel, mix, activate, dose, cave | Work on real input | PROVEN working |

---

## 4. Fixes, smallest first (one commit each)

Ledger and registry numbers: take the next free ones after BJ13's block. Every test below must run **rendered on Xvfb with real events and scene physics on** (copy `tmp/bj14/run.sh` and the event helpers in `tmp/bj14/bot.gd` into `tests/`); a headless test that calls handlers cannot see any of this.

**F1. Prompts for world items (S6).** Smallest, widest gain.
- Contract: facing a takeable world item inside reach shows "E — Take <label>".
- Files: `scripts/lol2/act2_world_items.gd` (add a hint Label like `l10_priest.gd:30`, set it in `_process` from `target()`).
- Test: rendered; walk to globe 44, look at it, assert the Label text, press E, assert the item is carried.
- Accept: the six L10 items and the L9 bracers each show the line. Note the Ruins rule that the bracers stay shielded while Saar lives; show "The bracers are shielded." there instead of nothing.

**F2. Prompt for the winged statue (S7) and the slab (S11).**
- Contract: "E — Touch the winged statue" at control 150; "E — Use the ankh on the slab" when the ankh is carried, "The slab has an ankh-shaped hollow." when not.
- Files: `scripts/lol2/act2_progression.gd:1312-1331` (or a small owner node for control 150), `scripts/lol2/l10_emperor_entry.gd` (Label; `reachable()` at `:60` already exists).
- Test: rendered, from `tmp/bj14/keep_ck_before_c4_ankh.json`-style save (make an earned one); assert both lines.
- Accept: both lines show; E still works.

**F3. Priest gives the ankh on one E (S10).**
- Contract: one E with the ashes -> ankh in the pack and the line.
- Files: `scripts/lol2/l10_priest.gd:61-76`. Find why the first press only shows the line (LIKELY the first E runs `speak()` and the second `exchange_ashes`).
- Test: rendered; one E; assert `Ankh.ANKH` carried.
- Accept: second press not needed.

**F4. Say the next step (S13, S15, N3).**
- Contract: after Dawn: a Journal note "The Emperor in the Cemetery may know what the trees need." After the arena: Luther is set down inside the village reach (or reach raised to 200) and the line says "The shaman will trade for another Silverleaf." On L12 arrival: one line and a Journal note.
- Files: `scripts/lol2/l8_tribe_dawn_hints.gd` (new row), `scripts/lol2/l8_tribe.gd:110` (position or text), `scripts/lol2/l8_journey.gd:6`, the L12 arrival hook, `scripts/lol2/atlas_places.gd:342-343` for the Atlas marks.
- Test: rendered; give Dawn the bracers, assert the note; leave the arena, assert `journey.target() == "village"`.
- Accept: the three lines exist; Atlas marks the Emperor after Dawn.

**F5. Arena E order (S14) and silent yield (N4).**
- Contract: after the bout only "E — Return to the village" shows; listening is offered only when Luther faces a Huline closely. E before the first blow says "Daniel waits for your first move."
- Files: `scripts/lol2/l8_huline_speech.gd:56`, `scripts/lol2/l8_tribe.gd:56-60,87-93`.
- Test: rendered; finish the bout; one E; assert phase "departed".
- Accept: one E leaves.

**F6. Hints for the rail, the fences and the flood (S8, S9, S12).** These are the original's own puzzles, so use the Journal, not a prompt that solves them (owner rule: Classic keeps stuck points and adds a Journal hint).
- Contract: Journal notes on first approach: rail "The rail is rotten; a blow would break it."; fence "Too high to climb. A running jump, tucking in (Ctrl) at the top, might clear it."; flood "The water is rising. The table by the low roof floats."
- Files: `scripts/lol2/l9_noble_rails.gd`, `scripts/lol2/l10_fences.gd`, `scripts/lol2/l9_escape.gd`, plus the hint tables (`l10_journal_hints.gd` pattern).
- Test: rendered; approach each; assert the note is discovered.
- Accept: three notes; the Controls help lists Ctrl as crouch/tuck.

**F7. Pack shows that it scrolls (S16).**
- Contract: a visible scroll bar or "more below" mark when the list is longer than five rows; a new quest item is scrolled into view when the pack opens after it is gained.
- Files: `scripts/lol2/museum_inventory.gd:63-70`.
- Test: rendered with 21 items; open the pack; assert the scroll bar is visible; `ensure_current_is_visible` on the newest item.
- Accept: the vapors are in view when the pack opens after the mix.

**F8. Body fit on the catacomb stairs (S5).** Not mine to design: first check whether Sol's fix cures it.
- Contract: body fit on, Luther walks from (1335, -1315) down the stairs without a world reset.
- Files: `scripts/lol2/act2_body_fit.gd` (Sol's branch).
- Test: `tmp/bj14/probe2.gd` is the repro (run without `--no-fit`); make it a rendered test: walk the stairs route, assert `scene.resets == 0`.
- Accept: resets 0 on L10 stairs and at the two off-route spots.

**F9. The Jungle and Ruins must be survivable (S1-S4).** The biggest fix, and a design call, so it is last and needs the owner.
- Contract: C1 and C3.
- The cause is that Act 2 creature health and damage are original-scale numbers against a 30-health Luther who hits for 8; the master plan puts real combat in a later phase.
- Options, my recommendation first:
  - (A) One interim scale until the combat phase: Act 2 roaming creatures deal a quarter damage and have a quarter health (`scripted_creature_population.gd:198`, one constant, ledger row "interim, removed by the combat phase"). Smallest, removable, keeps placements.
  - (B) R recovery also pushes nearby creatures back to their posts and gives 5 s of protection, so a death does not loop. Fixes the loop, not the difficulty. Goes away anyway with owner decision D6 (game over and reload).
  - (C) Give the F2 start Act-1-end strength (more health, a real weapon). Honest to the original, but needs the level and stat system first.
  - I would build (A) now and (B) not at all.
- Files: `scripts/lol2/scripted_creature_population.gd`, `scripts/lol2/act2_creatures.gd`, a DEVIATIONS row.
- Test: rendered real-input walk start -> village with **no aid**, armour on, no aura: assert arrival with health > 0 and no death; same for the Ruins opening.
- Accept: `tmp/bj14/s1.gd` without `--aid=1 --guard=1` reaches the Cemetery gate.

**F10. Then run the whole chain once more with no aids** (my job when F1-F9 are in): `s1.gd` then `survey.gd --from=c1_catacomb --noaid=1`, body fit on. Accept: L12 reached, stops 0, aids 0.

---

## 5. Where things are

- Tools: `lol2_bj12/tmp/bj14/run.sh`, `bot.gd`, `survey.gd` (39 legs), `s1.gd` (first sitting).
- Logs: `tmp/bj14/s1a.log` (no aid, dies at S1), `s1b.log` (start -> gate), `b3.log`..`b12.log` (later legs), stop rows in `tmp/bj14/stops.jsonl`.
- Saves per leg: `tmp/bj14/ck_before_<leg>.json` (+ `keep_` copies). They are survey saves made with the aids above; do not use them as earned evidence.

PLAN READY
