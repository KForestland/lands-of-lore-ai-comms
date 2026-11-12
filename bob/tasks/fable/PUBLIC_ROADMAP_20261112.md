# Lands of Lore 2 Classic: roadmap, 12 November 2026

Lands of Lore 2 Classic is a fan rebuild of *Lands of Lore: Guardians of Destiny* in the Godot engine. It will need the player's own copy of the original game. Kevin owns and playtests the project; AI agents write the code.

This replaces the roadmap of 11 November. The overall number has not moved, and this page says why.

## What changed since yesterday

We stopped building for a night and reviewed how the project works. Three findings:

- **The Dracoid Cemetery was not passable for a real player.** Chest lids, crypt tops, some doors and breakable fronts did nothing. The original opens and breaks these through one shared engine behaviour, and our rebuild never had it. It covers 219 objects across the game, 85 of them in the Cemetery.
- **The big maps are not impossible spaces.** They are mostly rooms stacked above rooms. In the Cemetery 37% of the floor has another room above or below it, in the Huline Temple 9%; at most about 1.5% is two rooms at the same height. Rooms appeared to cut into each other because the rebuild treated every room as solid at once, while the original only handles the rooms connected to where the player stands.
- **Our automated tests passed where a player was stopped.** They used prepared saves, teleports or another route.

What we are doing about it:

- Building the missing object behaviour once, for all 219 objects, Cemetery first.
- Saving the state of the world (opened lids, broken fronts, moved floors), not only the player.
- Rebuilding room tracking the way the original does it, now that the rule has been read from the original program.
- **A robot player walks each level with real keyboard and mouse input before Kevin does.** A level counts as ready only when the robot finds no stops and Kevin has walked it himself.
- Research into the original program now starts only when a build task needs a specific answer, with a two-hour limit and a modern replacement ready.

Finished since yesterday and merged: one combat module and one health owner for the whole game, a common base for all levels, one save for the whole game with autosave, and playtest starts for every level of Act 2 and Act 3.

## Where it stands

| Phase | Goal | Today |
|---|---|---|
| 0. Foundations | One save, one combat core, one way to give items, one object behaviour, tests based on real input | 35% (was 15%; several pieces merged, and two new pieces added to the list) |
| 1. Main quest | A player finishes the game from New Game to the ending | 45% (was 50%; the Cemetery finding lowered it) |
| 2. Maps and side content | Every level looks right; every optional area and puzzle is in | 35% |
| 3. Items | Every item works | 15% |
| 4. Role-playing systems | Real combat, spells, creatures, bosses, shape-changing | 10% |
| 5. Story and dialogue | Every line, both moral paths, both endings, every movie | 15% |
| 6. Game shell and sound | Title, menus, options, save slots, music | 5% |
| 7. Release | A stranger can install it and finish it | 5% |

**Overall: still about 20%.** Two days of work finished roughly one lane-week of tasks, and the review added about as much newly discovered work. The percentages are judgments from what a player can do today, not counts of finished tasks.

## When

These are estimates, not promises, and they could be wrong by months.

| Milestone | Most likely |
|---|---|
| The Dracoid Cemetery passes for a player | late November to early December 2026 |
| All of Act 2 passes | mid to late December 2026 |
| Kevin plays from New Game to the ending | late January 2027 (earliest: early January) |
| Version 1.0 | July to August 2027 |

The start-to-end date moved by about a month from the earlier "mid-December" checkpoint, as that roadmap said it would if the checkpoint slipped. The 1.0 date moved less, because the missing pieces would have surfaced later anyway.

Not being built until Kevin has played start to end once: real combat numbers, spells beyond the main quest, side areas, music, the installer, the good and evil branches, and an enhanced edition. Classic comes first.

## Where outside help is welcome

None of this needs game files from us; your own memory, your own copy or public sources are enough.

- **Which key or button is "use" in the original.** Our reading of the program suggests the keyboard letter C for opening chests and lids, with no mouse path. Can anyone confirm from the manual or from play?
- **Which music plays where:** a list of level or scene against soundtrack track.
- **Side content knowledge:** the City of the Ancients side rooms and ivory chip quests, secrets in the Dracoid Ruins, anything optional the printed guides skip.
- **Numbers from the original:** creature health, weapon and spell damage, what the difficulty setting changes.
- **Good and evil:** which actions shift Luther's moral standing, and what changes afterwards.
- **Later, in 2027:** playtesters on Windows and Linux.

Post findings as an issue on this repository, with where the information comes from.
