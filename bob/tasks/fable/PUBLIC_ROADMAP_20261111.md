# Lands of Lore 2 Classic: roadmap, 11 November 2026

Lands of Lore 2 Classic is a fan rebuild of *Lands of Lore: Guardians of Destiny* in the Godot engine. It will need the player's own copy of the original game. Kevin owns and playtests the project; AI agents write the code.

## Where it stands today

- **All 15 levels load and can be walked**, and the main quest is built from the first cave to an ending card.
- **Act 1 is playable.** Kevin has played it through: the cave, the museum, the Huline Jungle, the Hive.
- **Act 2 is built but does not yet hold up for a player.** An automated walk using real keyboard and mouse input got from the start of the Savage Jungle to the Claw Mountains, but only with help: extra health in fights and a save before each leg. Kevin's own playtest last night stopped in the Dracoid Cemetery. Three globes were out of reach, the catacombs were too dark, and he fell through the world after clipping a wall.
- **Act 3 is partly built.** One of its last two levels still stops a player in four known places, and the bosses are placeholders.
- **Mostly missing:** real combat and character growth (combat is a flat placeholder), 26 of 30 spell levels, behaviour for most of the 170 items, side puzzles and optional areas, the good and evil branches and second ending, many movies, music, a title screen and menus, save slots, and an installer that builds the game from your own copy.

In short: the world is much further along than the game.

## The steps to finish

Eight phases. The first and the last two run alongside the others. The percentages are judgments from what a player can do today, not counts of finished tasks.

| Phase | Goal | Done when | Today |
|---|---|---|---|
| 0. Foundations | One save for the whole game, one combat core, one way to give items, a test gate based on real input | Those pieces exist and every later task uses them | 15% |
| 1. Main quest | A player finishes the game from New Game to the ending | Kevin plays start to end on one build | 50% |
| 2. Maps and side content | Every level looks right; every puzzle and optional area from the guides is in | Kevin signs off each level with an empty defect list | 35% |
| 3. Items | Every item works | Each item works, or is shown to be absent from the original | 15% |
| 4. Role-playing systems | Real combat, spells, creatures, bosses, shape-changing | Kevin plays each act without cheats; no prompt stands in for a spell or a boss | 10% |
| 5. Story and dialogue | Every line, both moral paths, both endings, every movie | The good and the evil route can each be played to its ending | 15% |
| 6. Game shell and sound | Title, menus, options, save slots, music, ambience | The game is used without any developer screen | 5% |
| 7. Release | A stranger can install it and finish it | Outside players finish it; version 1.0 | 5% |

## Overall: about 20% complete

How this was computed: the remaining work is estimated at **74 to 130 lane-weeks** (one AI agent building for one week is a lane-week), summed over 137 planned tasks. Turning the phase percentages above into work already done gives about 27 lane-weeks. 27 out of 27 + 102 (the middle of the remaining range) is 21%. A second check, six weeks of work so far by three to four agents, gives 18 to 24 lane-weeks, or 12% to 25% across the range. Call it **one fifth, give or take five points**.

It feels further along than 20% when you walk around in it, because maps and the main quest came first. The systems that make it a game are the larger share of the work and have barely started.

## When

With three agents building in parallel:

- **Earliest: late April 2027.** Needs the original combat and item numbers to decode quickly and the remaining levels to hold few surprises.
- **Most likely: July 2027.**
- **Late: August 2027 or after**, if two of the big unknowns go badly.

These are estimates, not promises, and they could be wrong by months either way. The pace so far built things quickly; proving them for a real player is slower, as last night's playtest showed. That playtest does not move the range: the plan already allowed for unknown stops in levels no person had played. It does make the first checkpoint the one to watch.

Checkpoints that will tell us early:

1. **Mid-December 2026:** a player can finish the main quest. If not, add a month to everything.
2. **End of January 2027:** combat model decided.
3. **Before Christmas:** music decoded from the original files, or the fallback chosen (the music is confirmed decodable; which track plays where is still open).
4. **End of February 2027:** the installer works on a second machine.

The biggest risks: the game cannot be shared until the installer exists; the original combat numbers may not decode cleanly; and Kevin is the only human playtester.

## Where outside help is welcome

None of this needs game files from us; your own memory, your own copy or public sources are enough.

- **Which music plays where:** a list of level or scene against soundtrack track.
- **Side content knowledge:** the City of the Ancients side rooms and ivory chip quests, secrets in the Dracoid Ruins, anything optional the printed guides skip.
- **Numbers from the original:** creature health, weapon and spell damage, what the difficulty setting changes. Notes from memory editors or modding tools are ideal.
- **Timings:** for example how long the Hive guck takes to drain you, or how fast the Ruins flood rises.
- **Good and evil:** which actions shift Luther's moral standing, and what changes afterwards.
- **Version differences:** CD releases, patches and the GOG release, especially music and executables.
- **Later, in 2027:** playtesters on Windows and Linux.

Post findings as an issue on this repository, with where the information comes from.

PLAN READY
