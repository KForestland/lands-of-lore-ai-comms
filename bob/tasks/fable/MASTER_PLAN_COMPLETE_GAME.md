# MASTER PLAN: finishing Lands of Lore 2 Classic

Fable 5.2, 2026-11-10, from `MASTER_PLAN_TASK_20261110.md`. Plan only; no game code was changed and nothing was run for it.

Companion files:
- `fable_lane/master_tasks.json` — 124 proposed tasks in the requested shape.
- `fable_lane/master_backlog_triage.json` — one line for each of the 574 open backlog rows (566 todo + 8 claimed): keep, merge into which task, close after a check, or drop, with the reason.

**How this was made.** I read the inputs named in the brief and the tree `lol2_bj12` (= r19-work `b3e384e` + the two BJ12 commits). Five read-only survey agents each read one part of the code and reported with file and line; I measured the test suite and the ledger myself. Nothing here comes from task counts. The tree is one day behind r19-work (BK14-BK18, Sol 3b/3c are not in it), so Act 3 lines may be slightly pessimistic.

Grades: **PROVEN** = read in code, data or a test. **LIKELY** = inferred. **UNKNOWN** = not confirmed.

---

## The short version

1. **The game is much further along as a world than as a game.** All 15 levels load, and a main chain exists from the first Cave room to an ending card. But the chain is proven mostly by tests that call functions, not by a player's keys and mouse; and the RPG, the items, the dialog, the sound and the game shell are between one tenth and one third done.
2. **Three things are missing that no backlog row sizes:** a game shell (title, menus, options, slots), music and general sound, and a way to ship the game without the original media inside it.
3. **The best way to finish** is eight phases. Two of them (foundations, and the long-lead release work) start now and run beside the content phases. The owner's order is kept for content: maps and chain, then items, then RPG, then dialog, then small things, with sound and combat tuning last.
4. **The biggest change in method:** a task is done when a player can do it, shown by a real-input sitting. Status comes from one table of player stops, not from rows or green suites.
5. **Honest finish range:** between about April and August 2027, most likely early summer. Section 6 says what that rests on and what would move it.

---

## 1. Where the game really stands

"Built" means code exists. "Player" means a person at the keyboard can do it in a build today.

### 1.1 Areas

| Area | Main chain built | A player can do it | Evidence and gaps |
|---|---|---|---|
| Cave (L1_DC) | Yes | Yes | Owner crossed it on 11-07 and 11-08 (PROVEN from his F10 logs). Crates and the Draracle door are fixed on r19-work but not retested. Wisps, the mace climb, bridge lever, "third visit" bars are not established. |
| Museum (L3_DH map) + dragon ride | Yes | Yes | Owner: "much better, wall needs redo later". Scrolls are pickups only. Several side puzzles unhosted (skeleton theft, floor panel, blob crystal, blue gem, niche level). |
| Huline Jungle (L4_HJ) + rooms | Yes | Yes, with stops | Owner confirmed village, Hive, monastery, Kit'yara, Bacatta. Not found in code (LIKELY missing): imp-scroll floor trap, switch behind the statue, hidden door, spider start, fish death. Rooms and shops are tested by handler calls. Map look is not signed off. |
| Hive (L5_HC) | Yes | Yes | Owner crossed it. Open: four-button puzzle (decoded, not built), boulder-to-cellar, flying knives, gas, cat pedestals; "needs a texture pass". |
| Dark Halls (L7_DH), optional | Yes | Not confirmed | Sol's puzzle rebuild is merged; the owner has not played it since his 15 reports of 11-07. Entry is a shortcut; Rix's branch is missing. |
| L8 Savage Jungle + Wild Village | Yes | LIKELY after BJ12/BJ13 | The village chain now has real-input tests. Village views are a text panel. Tree-room slots, by-hand combine and full-health start are being built (BJ13). |
| L10 Cemetery, L9 Ruins | Yes | UNKNOWN | Hand-written scripts cover every step; tests walk physically but press almost no real keys. Nobody has surveyed these as a player. |
| L12 Claw Mountains | Yes | UNKNOWN | Same. Gorilla village, tiger cave, lake platform are inert: the level binder fires only one of the region event kinds. Avalanche is a stand-in. |
| L13 Ruloi Citadel | Yes | UNKNOWN | 39 earned tests, none with an input event. The least player-proven level. |
| L14 Huline Temple | Yes | UNKNOWN | One test uses real E and click. Nine stone cubes not built. Portal rooms clip into the map (owner). |
| L16 City of the Ancients | Partly | Only by shortcuts | Standing in a region poses the Mantle, a proximity pad is the exit, the centre fight is "E drops the foe". The towers, ivory chips, box-through-disk and Starry Tower are not built; no native rows were found for box, disk or figure. |
| L17 Caverns | Yes | LIKELY | The carry across the pit is a stand-in; the beast scene reel is not in any archive. |
| L19 | Partly | **No** | Four known stops for a real body (pool channel, post-flood float, low rapids, closed movers). 14 native rows stop on unread locals. The L19 to L20 gate is seeded. Every earned test teleports. |
| L20 | Partly | UNKNOWN | Never walked end to end. Bosses are E prompts. The ending is a caption card and a one-line credits stub. |

Two statements that sound alike and are not:
- "Every step walked in testing" (the r19 notes) is true of the test walker's feet.
- "A player can finish the game" is not yet true. L19 stops him, and on most levels his hands (E, clicks, pack) have never been tested.

### 1.2 Tests, measured (PROVEN)

- 1,112 test files, 1,077 registered. 173 send any real input event.
- Of 251 "earned" tests: 142 neither send input nor call the common handlers by name (they walk and check state), 52 call `interact()` / `offer()` / `pick()` directly, 38 set the player's position, and 9 are clean real-input tests.
- Only two registry rows declare teleports or test aids (both mine, from BJ12). Every L17/L19/L20 earned test sets the position without declaring it.
- The Act 1 "CERTIFIED" campaign of 2026-10-04 is eleven linked legs with physical walking and handler calls. The owner's first manual run that day stopped at the Museum.
- A full qualification takes 3 to 4 hours. Touching `act2_map.gd` selects 797 of 1,077 tests. One Godot is about 1.3 GiB (LIKELY), which is why 17 at once crashed the PC.

### 1.3 Systems

| System | Built | Player gets | Missing for a finished Classic |
|---|---|---|---|
| Movement, forms, drowning, crouch | Yes | Yes | Same rules in every area; body versus tight native passages (Sol 3c). |
| Native script host | 15 levels load their original scripts; about 30 opcodes hosted | Indirectly | L8-L14 are 82 of 86 hand-written owners, not native. Missing game-wide: opcode 17 (counters), opcode 206 (soul), region events 1 and 4, several arms on the Act 3 chain. |
| Saves | F5/F9, one quicksave per area, about 13 formats, strict validators | Partly | No slots, no save UI, no migration (`version == 1` only). Other levels' native state LIKELY lives only in session memory, so quit-and-load in Act 2/3 can lose it. No resume for Act 2/3 saves from the opening screen. |
| Items | 170 definitions carried and shown; 20 have behaviour | Partly | 103 definitions answer "not hosted". No per-weapon damage, no rings, no throwing, no scroll reading, no recipes, no stacks, no drop, no containers. No generic path from a script's "give item" to the pack: 25 files append by hand. Two catalogs. |
| Combat | Flat adapter: 30 health, armed blow 8 | Yes, but not as a game | Decoded progression is computed and then ignored by combat. Act 2 creature health is 200 to 10,000 against 8 per blow. No ranged attack at all. Strike code is copied in about 12 hosts; health has three owners. |
| Spells | Spark 1/3/5 and Heal 1 | Those four | 26 of 30 spell levels; no learning; every story cast is an "E" prompt. |
| Creatures | About 30 of 45 kinds have a body on one shared host | They chase, hit, die | One AI for all; no loot drops; bosses are prompts; stats untuned. |
| Good/evil | Soul value stored (start 5, 0..10); a handful of Act 1 writers | Invisible | 83 native soul changes unhosted. BRANCH-01..08 are marked done in the backlog but are **not in the tree** (unapplied patches that never compare the soul). One ending exists, as a card. |
| Dialog | Per-scene scripts play original speech where hosted | Where hosted | No shared speech host, no subtitles, all eight NPC rows open, no census of which lines play. |
| Movies | 85 names in the game's table; 39 reels converted; 10 players bound | Some | Intro and endings unreferenced; no audit of which are cards. |
| Music and sound | Voice and some effects | Voice, some effects | **No music code at all.** No ambience, footsteps, UI sounds, volume control. |
| Game shell | A developer opening screen | No | Title, menu, New Game with intro, options, pause, game over, credits. No backlog rows exist for any of it. |
| HUD, Journal, Atlas | Classic HUD; Journal and Atlas are modern aids | Yes | Spell bar for all schools, pack size and stacks, quick belt, Atlas for L9/L10/L16-L20. |
| Build and release | Owner-only build, 6.7 GB, original media inside | No | **Cannot be shipped as is.** No converter for a player's own copy (249 separate producer tools), no Windows test, stale README. |

### 1.4 Provisional numbers in the game today

The owner's rule is "no invented caps or timers". These are in the code now and need a source or an owner decision (task R-19): health 30; Heal +6; Spark 8/16 and range 384/768; cast cooldown 0.5 s; mana regeneration every 3 s; melee 8/4/12/1; strike cooldown 0.45 s; incoming damage times 0.4; creature alert 600/240, reach 50/60, speeds 48/55/42; Dawn's bolts 15/12/20 every 2.2 s; prism blind 10 s; form times 60/120 s at G prompts; L14 Belial damage cap 15; L13 Belial poison tick 2 s; fire crystal 8.

---

## 2. The best way to finish

### 2.1 Phases

```
            Nov        Dec        Jan        Feb        Mar        Apr   ...
P0 foundations  ████████
P1 chain        ██████████
P2 maps + side        ████████████████
P3 items                   ██████████████
P4 RPG                            ████████████████████
P5 story/dialog                          ████████████████
P6 shell + sound    ░░ research ░░░░░░░░░       ████████████
P7 release      ░░ converter, long lead ░░░░░░░░░░░░░░░    ████████████
```
The bars show order and overlap, not promised dates (section 6).

| Phase | Goal | Exit test |
|---|---|---|
| **P0 Foundations** | Make every later task cheaper and every claim checkable | Golden-path gate exists; one whole-game save; one item grant path; one strike module; host gaps listed |
| **P1 Chain** | A player finishes the game from New Game to the ending | Owner plays start to end; every sitting green on one commit (build r20) |
| **P2 Maps and side content** | Maps "100%", every puzzle and optional area in the guides | Owner signs off each level; his F10 lists are empty |
| **P3 Items** | All items in one pass | Every definition works, or is proven absent from the original, or is listed unknown |
| **P4 RPG** | Real combat, spells, creatures, bosses, forms | Owner plays each act without cheats; no story prompt stands in for a spell or a boss |
| **P5 Story and dialog** | Every line, every branch, both endings, every movie | Good and evil route tests pass with earned soul values |
| **P6 Shell and sound** | It starts, saves, sounds and ends like a game | Owner uses the game without the developer screen |
| **P7 Release** | A stranger can install and finish it | Outside players finish it; 1.0 |

### 2.2 Why this order

- **P0 first, because three pieces of debt multiply every later task.** Twelve copies of the strike code make each RPG task twelve tasks. Hand-rolled item grants make each item task a per-level task. Per-area saves make every state change a save-breaking change. Paying these once is cheaper than paying them 200 times.
- **P1 before P2, as the owner said (chain before refine).** A finished chain is also the test bed for everything else.
- **Items before RPG, as the owner said.** Weapons, ammunition, scrolls and tokens are what combat and spells consume. One exception: the item *numbers* decode (I-03) and the combat model decision (R-01) inform each other, so both start in P3.
- **Three spells are on the main chain** (level-1 Mist at the heads, level-5 Expel at the mother, level-5 Trinity at Scotia) and one side puzzle needs a level-3 imp. P1 keeps them as prompts; P4 replaces them. That is why L16's towers (M-15) wait for Summon (R-10).
- **Dialog after RPG, as the owner said.** But the branch scenes need the soul value, and the soul handler is a small host task, so it sits in P0.
- **Sound and shell are late for integration but their unknowns start now.** Whether the music archive decodes is a research risk. Research is cheap to start and expensive to discover late.
- **The release converter starts now too.** It is the one item that decides whether the game can be released at all, and it gets harder with every new producer tool.

### 2.3 What runs in parallel

Machine limit is memory: Sol 6 Godot, Grok 2, Fable 2, lead as needed, with 10 GiB free before each launch.

| Lane | P0-P1 | P2-P3 | P4-P5 | P6-P7 |
|---|---|---|---|---|
| **Lead (Opus)** builds from plans, merges, owns the gate | Gate, item grant API, L8, Act 1 golden path | Museum, Cave, L14, item core and UI | Combat model, spell core, curse, bosses, speech host, NPC passes | Shell, release kit |
| **Sol** engine and large slices | Save, strike module, input rule, L19 body | Jungle, Hive, Dark Halls, missiles | Spells by school, creature families | Options, sound, converter, slimming |
| **Grok** native data and decode | Host opcodes, L19/L20 rows, L16 | Act 2 side areas, item behaviours | Branches, soul census, movies, rooms | Music decode (starts early) |
| **Fable** plans, surveys, checks | Player survey sittings L9-L14, L20 | Plans per batch; item acceptance sweep | Plans; route tests review | Release candidate review |
| **Kimi** review | Prep traces, merge reviews | Ledger review (282 rows) | Provisional-number audit | — |
| **Owner** | r19/r20 playtests, decisions D1-D5 | Level sign-offs | Balance playtests | Beta, 1.0 |

### 2.4 What I would change in how we work

1. **Done means a player can do it.** Each task's acceptance is a real-input sitting: real keys and mouse, on foot, no handler calls, no position sets, no test aids. Unit and state tests stay, underneath.
2. **One STOP table is the status.** `lead_notes/OPEN_STOPS.md` (decided on 11-09, not yet created) in chain order, regenerated from the sittings. "Qualified" means the sittings pass, not that the suite is green.
3. **Survey before fix, on every level.** A survey walk continues past each stop and lists them all. It gave an Act 3 stop list in an afternoon. L9, L10, L12, L13, L14 and L20 have never had one.
4. **Declare every shortcut in a test.** Teleports and test aids are counted in the registry and checked by a tool. Today two rows declare any.
5. **Plan, then build** (the trial the owner started with BJ13). One lane writes the contract, the data facts, the files and the test; another builds. The plan found the native slots and the "second potion" fact before any code was written. Use it for every batch of size L.
6. **Cut the cost of a gate.** A lane change should select tens of tests, not 797. The lead runs the full sweep nightly. This is the cheapest speed-up available.
7. **One backlog, in batches.** 124 tasks replace 574 rows. A row per item or per spell hides the real unit of work, which is the shared mechanism.
8. **Stop the backlog and the docs going stale.** `act2_route.md` says "not hosted" for 58 rows that mostly are; 25 STORY rows say "todo" for work that exists; BRANCH rows say "done" for work that is not in the tree. A task closes only with the commit and the sitting that prove it.
9. **A weekly owner build with a short "please test" list** tied to the phase exit, instead of a build per fix. His playtests are the scarcest input in the project.
10. **One staging command for worktrees.** Missing inputs caused 3 of 7 failures in my first BJ12 gate and 14 of 16 in the second.

---

## 3. Every task

`master_tasks.json` holds all 124 with dependencies, lane, size, classic-or-modern call, fallback and acceptance. Summary by phase:

| Phase | Tasks | What is in it |
|---|---|---|
| P0 Foundations | 17 (F-01..F-17) | Golden-path gate and STOP table; test honesty; staging; headless input rule; smaller gates; whole-game save with native state; item grant API; opcodes 17 and 206; region events 1/4; game-wide unhosted-opcode table; backlog rewrite; one strike module; one health owner; area host base; per-level smoke |
| P1 Chain | 16 (C-01..C-16) | BJ13; Act 1 golden path by real input; owner retest of r19; survey sittings L10/L9, L12, L13, L14; L16 main line; L17; L19 body, liquid and native rows; L20 walk and chain rows; Act 2/3 playtest starts; r20 |
| P2 Maps and side | 20 (M-01..M-20) | Per Act 1 area: missing puzzles and look; L8 tunnels and real village views; L10/L9, L12, L13, L14, L16, L19/L20 side content; Act 2/3 map review; lighting; Atlas v2; ledger review; movement rules |
| P3 Items | 16 (I-01..I-16) | Unified core; inventory UI; numbers decode; 10 behaviour batches; placements; containers and shops; book tabs; acceptance sweep |
| P4 RPG | 20 (R-01..R-20) | Combat model; creature units; ranged attack; spell core and five school batches; story casts; creature families and three act batches; bosses; loot; forms; provisional numbers; balance playtest |
| P5 Story and dialog | 16 (S-01..S-24) | Speech host; speech census; three NPC passes; Bacatta; subtitles; NPC bodies; branches; soul census; endings; movie audit and playback; special scenes; room archives; original bugs |
| P6 Shell and sound | 10 (U-01..U-06, A-01..A-04) | Title and menus; intro; save slots; options; game over and credits; dev keys hidden; music decode and playback; ambience and effects; audio buses |
| P7 Release | 9 (X-01..X-09) | No-media distribution and first-run converter; producer chain; slimming; Windows; release kit; closed beta; orphan tests; stability; release candidate |

**Work that was missing from the backlog** (no row, or one tangential row): the whole game shell; music and general sound; the distribution model and converter; a whole-game save with slots; native script state in the save; a generic item grant path; the combat model; a player ranged attack; subtitles; a speech census; a movie audit; branches actually built; region events 1/4; opcode 17 and 206 in the host; every Act 1 story step (there are no Act 1 STORY rows at all); a real-input Act 1 run; player surveys of L9-L14 and L20; the L16 tower design; test honesty tooling.

### 3.1 Backlog triage

Per row in `master_backlog_triage.json`. In summary:

| Rows | Decision |
|---|---|
| 159 ITEM | Merge into the behaviour batches I-04..I-12. The handler histogram is nearly flat (107 handlers, 98 used once), so the unit of work is the 42 callee groups in `item_handlers.gd`, not the row. I-16 checks all 170 definitions at the end. |
| 153 REVIEW | Merge into M-19: the 29 native-host rows go to Grok to confirm from the disassembly; the rest are decided inside each area's map pass, not as separate work. None dropped. |
| 53 TEST | Merge into X-07: register or retire with a reason. |
| 45 CREATURE | Merge into R-13/R-14/R-15 by act and R-16 for bosses, after the family table (R-12). |
| 31 SPELL | Merge into R-06..R-10 by school. |
| 27 STORY | 13 close after their sitting passes (the scripts exist; the status is stale). 11 merge into the L16 tower and Act 3 extras tasks. 3 (route tests, endings) merge into S-12. |
| 20 ACT1, 16 BUG, 17 build, 12 MECH, 10 ENGINE, 9 NPC, 5 UI, 4 INFRA, 3 MAP, others | Merged into the named task; 6 more close after a check (ladder, tree bridge, Larkhon, platform, crouch x2). |
| Dropped: 2 | `INFRA-W17` (superseded by the 11-09 decision that lanes pull their own next task) and `PLAN-MASTER-REMAKE` (this plan replaces it for LoL2 Classic). |
| Kept as they are: 4 | Three workspace clean-ups and the drowning animation polish. |

---

## 4. Classic or modern

Classic is the default for every task. The call per task is in `master_tasks.json`: 38 are classic outright, 57 are classic with a named modern fallback, 29 are modern by nature (tools, shell, release, owner-approved aids).

### 4.1 When something counts as "too hard"

A classic attempt has a time-box set by task size, counted in working lane-days on that one unknown:

| Size | Time-box for the unknown | 
|---|---|
| S | half a day |
| M | one day |
| L | two days (three for the combat formula and the music archive) |

At the end of the box the lane posts **evidence**, not a feeling:
1. where the native record, opcode or table is, or proof that it is not in the data;
2. exactly what stayed unknown;
3. what a further day would likely buy.

If an unknown remains, the fallback named in the task is built at once. Nobody waits for a decision that was made in advance.

### 4.2 Rules for the fallback

- It must **match the longplay or the guides**, and say which minute or page.
- It gets a **ledger row** with the unknown named, so it can be replaced later.
- **No seeded predicate, no silent default.** An adapter binds a player action to a proven group; it does not fake the state that would have made the group run.
- **Numbers:** a number comes from the data, then from the books, then from a measurement of the longplay. If none exists, the owner picks it. Lanes do not invent rates, caps or timers.
- **A fallback that changes how the game plays goes to the owner first.** One that only changes how something is shown does not.

### 4.3 Things that are modern from the start

- Where the original data has nothing: L16's box, disk and yellow figure; the Mantle gate; the L20 room door.
- Player aids the owner already approved: Journal, Atlas, quick belt, larger pack and stacks, R recovery, F2 starts.
- Everything a 1997 game got from DOS and a CD: the shell's options, save slots, the installer and converter.
- Original bugs: fixed in both editions by the owner's rule.

---

## 5. Decisions only the owner can make

Each with my recommendation. D1 to D5 are needed in the next two weeks; the rest can wait for their phase.

| # | Decision | Recommendation |
|---|---|---|
| D1 | **Combat scale.** Use the decoded original model for health, attack and defence, or one deliberate rescale? | Decoded model first, three-day time-box on the damage formula. If it does not decode, one rescale table that you approve once. Not per-creature tuning. |
| D2 | **How the game is shipped.** | The release holds no original media. The player points it at their own copy and a converter builds the rest. Anything else cannot be published. |
| D3 | **Saves.** Whole-game save with slots and autosave on level change? | Yes. The original had slots; per-area quicksaves cannot carry a full playthrough. |
| D4 | **Scope of 1.0.** Everything in the hint book, or the main chain plus major side content? | Everything that has data in the original. Things the books mention but the data lacks are listed, not invented. |
| D5 | **L16 towers.** No native rows were found for the box, disk and figure. Build from the book and longplay as one adapter? | Yes, after Grok spends one more day looking. It is the largest stand-in in the game, so it should be your call. |
| D6 | **Death.** Keep "R recovers" in Classic, or the original game-over and load? | Game-over screen with Load and "last autosave"; keep R as an option in settings. |
| D7 | **Subtitles**, which the original lacked. | Yes, optional. |
| D8 | **Scenes with no reel in the archives** (the L17 beast scene). In-engine staging that matches the longplay, or a card? | Staging, logged as an adapter. |
| D9 | **Guck drain rate** and other rates that do not decode. | You pick the value from the longplay once; it is logged. |
| D10 | **Music fallback** if the archive does not decode in three days. | Ship the optional user music folder and say so plainly; keep trying in the background. |
| D11 | **Second Larkhon potion.** The Larkhon never wakes in the port, so it has no use. | Leave it as an item with no use. Do not make the Larkhon wake again. |
| D12 | **Developer keys and F2 starts in the release.** | Hidden behind a flag; F2 starts become "chapter start" only if you want them public. |
| D13 | **Platforms for 1.0.** | Linux and Windows. |
| D14 | **Closed beta** with outside players before 1.0. | Yes: Amy Schmidt, mohammadkoush, Kolec76 if they agree. |
| D15 | **Weekly build rhythm** instead of a build per fix. | Yes, one build a week with a short test list. |

Standing gameplay matters that also need you when they arise: any creature damage change, any change to curse timing, any puzzle solved differently from the book.

---

## 6. Effort, dates, risks

### 6.1 Effort per phase

In lane-weeks: one building lane working a normal week inside its usage limits. Low and high, not a midpoint.

| Phase | Lane-weeks | Main uncertainty |
|---|---|---|
| P0 Foundations | 5 to 8 | How entangled the Act 1 hosts are with the strike and save code |
| P1 Chain | 5 to 10 | L19/L20 unread locals; what the L9-L14 surveys find |
| P2 Maps and side | 10 to 18 | Hive and Jungle puzzles; L16 towers; how many map defects the owner finds |
| P3 Items | 8 to 14 | Whether the item numbers decode |
| P4 RPG | 14 to 24 | The combat formula; 26 spell levels; boss fights |
| P5 Story and dialog | 10 to 18 | How many lines and movies are not yet triggered; the census will say |
| P6 Shell and sound | 6 to 12 | Music archive format |
| P7 Release | 8 to 14 | Converter on Windows; what beta players find |
| **Total** | **66 to 118** | |

### 6.2 Finish date

With three building lanes that is 22 to 39 calendar weeks of pure work. Add owner playtest turnaround, lane usage limits, gate time and holidays, and overlap gives some back.

- **Earliest I can defend: April 2027.** Needs the item numbers and the combat formula to decode quickly, the music archive to be a known format, and the surveys of L9-L14 to find little.
- **Most likely: June to July 2027.**
- **If two of the large unknowns go badly: August 2027 or later.**

Checkpoints that will tell us early which it is:
- **r20, a player finishes the game** (P1 exit): if this is not in hand by mid-December, add a month to everything.
- **Combat model decided** (R-01, R-02): by the end of January.
- **Music decoded or fallback chosen** (A-01): research can answer this before Christmas.
- **Converter runs on a second machine** (X-01, X-02): by the end of February.

This estimate rests on the pace I can see: 820 commits in 23 days, and ten levels of owner-scripted chain in about ten days. That pace built things; it did not prove them for a player, and proving is slower. I could be wrong by a wide margin in either direction, and the range above is honest rather than precise.

### 6.3 What would move the date

Earlier:
- Smaller gates (F-05). Every lane gains from the first week.
- The owner answering D1 to D5 soon.
- A fourth building lane once P0 is in, because P2 to P5 split well by area and by batch.
- Cutting 1.0 scope to the main chain plus major side content (D4) would save roughly 8 to 15 lane-weeks.

Later:
- Finding that Act 2 creature numbers are not hit points and the damage formula does not decode.
- A music format nobody has decoded.
- The Windows converter.
- Owner playtests more than a week apart.

### 6.4 Top risks

1. **The game cannot be shipped in its present form.** Every build embeds converted original media. Mitigation: X-01 starts in P0, not at the end.
2. **Combat scale.** If creature health and weapon damage do not come from data, balance becomes a design job that needs the owner's time. Mitigation: R-02 first, D1 decided in advance.
3. **A full playthrough save.** State changes during development break testers' saves, and native state may not be saved at all. Mitigation: F-06/F-07 before content.
4. **Unknown player stops on six levels.** Nobody has surveyed L9, L10, L12, L13, L14 or L20 as a player. Mitigation: C-04 to C-07 and C-13 early; they are cheap.
5. **L19/L20 native rows that will not decode.** Mitigation: the adapter rule of 4.2, a day per row.
6. **Music.** No code, no decoder, one tangential backlog row. Mitigation: research now, fallback named.
7. **Gate cost and memory.** A 3 to 4 hour gate with a hard cap on parallel runs slows everything. Mitigation: F-05, nightly sweeps.
8. **Stale status.** Backlog and docs disagree with the tree in both directions. Mitigation: F-13 and the closing rule.
9. **Owner time.** He is the only real player and works full time. Mitigation: weekly builds, short lists, outside beta players.
10. **Scope creep from Enhanced and LoL3.** Mitigation: nothing for either enters this plan unless it constrains a Classic choice. The two places it does: the whole-game save format, and the unified item core, should be written so Enhanced can extend them.

### 6.5 What I could not confirm

- Whether Act 2 creature health values are hit points or another unit.
- Whether level changes lose other levels' native script state on quit (LIKELY, not traced to the end).
- What format `DMUSIC.MIX` is. It is 81 MB, which suggests recorded audio rather than MIDI, but I did not open it.
- How many original speech lines and movies exist against how many play. Only the converted counts are known (716 WAV, 39 reels).
- Whether the owner's 11-08 Act 1 run did every quest step by hand.
- Whether L9, L10, L12, L13 and L14 have player stops; no survey exists.
- The state of L19/L20 on today's r19-work.
- Exact pickable-item counts for Cave, Hive and Dark Halls.
- Which of the 1,086 native "item" commands are gives rather than takes or checks.
- Windows behaviour, real load times and memory of a packaged build.
- Whether the non-GOG executable passes the launch check.
- The Brady guide was used through the backlog's page references, not re-read; the hint book was read directly for the chapters I cite.
- The owner's screenshots in `~/Downloads` were listed, not opened.
- My survey agents read code; none ran the game. Where they said LIKELY I kept it.

PLAN READY
