# Lands of Lore 2 Classic: roadmap, 15 November 2026

Lands of Lore 2 Classic is a fan rebuild of *Lands of Lore: Guardians of Destiny* in the Godot engine. It will need the player's own copy of the original game. Kevin owns and playtests the project; AI agents write the code.

This replaces the roadmap of 12 November.

## What changed in three days

- **Kevin played from New Game to the Ruloi Citadel in one sitting** (15 November, about three hours). He was stopped four times; two of those were fixed while he was still playing.
- **A robot player reached the ending.** It plays with real keyboard and mouse input. It has walked every level from the Ruloi Citadel to the end of the game in one unbroken life: the Dreamstone, back to the Huline Temple, the City of the Ancients, the Hidden Caverns, Belial's caverns and the final level.
- **The Dracoid Cemetery is playable.** Chests, crypt tops, doors and breakable fronts work; the orb chargers and globes work; the lower rails can be crossed; the oil blast opens the tomb floor.
- **The eight spells the main quest needs are built**, and the game now teaches a needed spell at the place where the player first needs it, if they never picked up the optional scroll.
- **Saving keeps the world:** lit spires, placed items, part-open doors, raised floors and lifts. Loading a save no longer repeats what happens when you walk into a room.
- **Objects on nine more levels and the first item classes** (food and healing, keys and quest items, scrolls, thrown items, light sources, equipment) are built and reviewed, and merge next.

## What we learned about the maps

The original engine only draws and collides with the room the player stands in and the rooms connected to it, so its designers could put two rooms in the same place. A modern engine keeps the whole level in the world at once, and those rooms cut into each other.

We tried moving rooms apart. It works where the moved piece is closed in (a crawl tunnel that ran through a wooden room in the Huline Temple now runs under it; the floor of the Emperor's tomb in the Cemetery was lowered). It does not work on open, roofless ground: raise a piece of an open yard and the player looks over the wall tops of the rooms around it.

So the goal is now **nothing a player can see or feel**, not "no two rooms share space in the data". Reported spots are fixed one by one; the original's own rule (handle only connected rooms) covers the rest.

## Where it stands

These are judgments from what a player can do today, not counts of finished tasks.

| Phase | Goal | 12 Nov | Today |
|---|---|---|---|
| 0. Foundations | One save, one way to give items, one object behaviour, tests based on real input | 35% | about 60% |
| 1. Main quest | A player finishes the game from New Game to the ending | 45% | about 65% |
| 2. Maps and side content | Every level looks right; every optional area and puzzle is in | 35% | about 40% |
| 3. Items | Every item works | 15% | about 25% |
| 4. Role-playing systems | Real combat, spells, creatures, bosses, shape-changing | 10% | about 15% |
| 5. Story and dialogue | Every line, both moral paths, both endings, every movie | 15% | 15% |
| 6. Game shell and sound | Title, menus, options, save slots, music | 5% | 5% |
| 7. Release | A stranger can install it and finish it | 5% | 5% |

**Overall: about 27%** (it was about 20%).

## When

These are estimates, not promises, and they could be wrong by months.

| Milestone | Most likely | On 12 Nov we said |
|---|---|---|
| The Dracoid Cemetery passes for a player | Done, 13 November | late November to early December |
| Kevin plays from New Game to the ending | mid to late December 2026 | late January 2027 |
| Version 1.0 | July to August 2027 | July to August 2027 |

The start-to-end date moved forward because the stretch from the Citadel to the ending already walks for the robot. The 1.0 date has not moved: combat, most items, side content, story branches, music and the installer are still ahead.

## Not working yet

- A real player has not gone past the Ruloi Citadel in one run. On 15 November Kevin was stopped there by a door that opens when you cast a spell at a globe, with nothing on screen saying so. Hints for that are being built.
- Combat is basic. Most of the 170 items do nothing yet.
- Side content is parked until the main quest plays through: the starry floor and the ivory chips in the City of the Ancients, most optional puzzles.
- The good and evil branches are not being worked on until the game is playable start to end.
- Some levels still show other rooms through walls in places.

## How we work now

- A robot player walks each level before Kevin does. From now on it plays like he does: it walks into a level from the previous one, picks up nothing optional, and knows only what the screen tells it.
- Every stop Kevin reports is fixed and then checked across the whole level for the same kind of fault.
- A builder never reviews its own work.

## Where outside help is welcome

None of this needs game files from us; your own memory, your own copy or public sources are enough.

- **City of the Ancients:** must you raise all four tower sections (the starry floor, the box and the yellow figure) before you can go on? We cannot find those objects in the game data.
- **The glass orbs charged at the Cemetery altars:** which colour stores which spell, and what does the white one do?
- **The Claw Mountains tiger cave:** how the switch and the rising platform work.
- **Numbers from the original:** creature health, weapon and spell damage, what the difficulty setting changes.
- **Which music plays where.**
- **Later, in 2027:** playtesters on Windows and Linux.

Post findings as an issue on this repository, with where the information comes from.
