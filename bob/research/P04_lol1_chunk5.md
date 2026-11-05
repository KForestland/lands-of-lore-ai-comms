# P04 LoL1 chunk 5: keep, thugs, Roland, the poisoning

No Godot was run. The tree is `~/lol1_godot` at `9987d7e`, clean. L06 chunk 5 plays cards LOL1-02 through LOL1-05: the keep, the thugs, Roland, and the poisoning. Chunk 4 owns the TIM. This chunk owns the walk and the EMC calls those levels report as missing. The string typos are a display fix in this chunk, when those names first show.

## Data

`level_scripts.gd` counts an unimplemented call in `missing` and returns 0. `IMPORTER_CALLS` and `QUIET_CALLS` return 1 and are not counted. `playSoundEffect` is quiet, so a level that calls it does not add a sound chunk. Compass state is global var index 11, `game.compass_broken`. The atlas and the compass are in this chunk only when `missing` on these levels names their call. A second atlas is not added later.

Placements from N04 that this chunk may use:

- Earned start is block 557, direction 0. The north gate is LEVEL1 block 589 facing south, direction 2. Arrival is level 2 block 106 facing south. LEVEL1.INF function 621, mask 0x0041, `loadNewLevel(2, 106, 2)`, is LIKELY. The return is LEVEL2.INF function 74, mask 0x0041, `loadNewLevel(1, 589, 0)`, LIKELY. The writ check on that gate was not read.
- King's Writ is type 244. Geron's block and the give call were not read.
- Library key is type 185. Both blocks were not read. No ONETIME name contains atlas.
- The mace at Victor's Arms is not required. The shop function and the mace type were not read. LEVEL1.INI makes Halberds. That grant was not named as this shop.
- Lantern type 249 is on LEVEL5 block 97. Thug's key type 167 is on block 165. Both come from LEVEL5.INI function 1, grade LIKELY. LEVEL2.INF functions 96 (mask 0x00C3) and 99 (mask 0x4001) each `loadNewLevel(5, 260, 3)`. Face 3 against `walk.gd` index 3 West stays unmerged. The walkthrough puts the lock picks in the hideout chest. LEVEL6.INI function 1 creates type 245 on Caves Level 1 block 168. Those two placements stay unmerged. The lever, the plates, the three buttons, and the chest were not read. LEVEL5 places Rock type 99. A rock row is not a plate. LEVEL5's English name is Thug's Hideout, area CAVE1. The walkthrough says the Northland hideout. Those place names stay unmerged.
- Roland's key type 166 is on LEVEL4 block 41, LIKELY. Aloe type 217 and Oil Flask type 248 share block 260. The walkthrough's hidden niche was not joined to that block. LEVEL4.INF function 199, mask 0x0083, `loadNewLevel(3, 804, 2)`, is the way back. The burnt-scroll type, the ogre block, which ogre choice is required, and the saber were not read. The ruby is already gone. No placement for it was read.

L03's poisoning acceptance is Timothy gone, Baccata in, and the king poisoned. The join and the leave are chunk 6. The cup and the shield shape have no required action.

M04 stores item 228 as Duble ring and item 199 as Nathanial's Key. Patch 001 writes four byte replacements into a GOG CD STARTUP.PAK and is not imported. English becomes Double ring and Nathaniel's Key. French and German change the Duble spelling. Nathaniel's Key is the English string. Both editions show the corrected names. The leading null on the NECROSAP shape string has no patch file. It is not added.

## Behaviour

Run levels 1 through 5 far enough to finish these four cards. Port a syscall only when `missing` names it on those levels. Show the patched spellings for items 199 and 228 when the name is drawn. The retail bytes stay the record of the typo.

An unknown block stays unknown. The writ, the atlas, the mace, the lock picks' chest, the ogre choice, and the burnt scroll are not given coordinates by this spec.

## Tests

1. A new game with scripts on is block 557, direction 0. The north-gate step arrives at level 2 block 106, direction 2. The return arrives at level 1 block 589, direction 0. A test that requires the writ on that gate fails until the gate function is read.
2. After those levels have run, every name that was in `missing` is either implemented or still listed. A call that was never listed is absent. `playSoundEffect` is still quiet and still uncounted.
3. The lantern and the thugs' key are the LEVEL5 placements above. Type 245 stays on LEVEL6 block 168. Rock type 99 is not used as a plate.
4. Roland's key is the LEVEL4 placement. The ogre path accepts bluff and accepts fight. Neither is the only one.
5. The drawn name of item 228 is Double ring. The drawn name of item 199 is Nathaniel's Key. A French or German lands file shows the patched Duble spelling and leaves Nathaniel's Key on the English file.
6. A reload keeps the writ if it was taken, the atlas if a missing call created it, the lantern, the thugs' key, and Roland's key. An item this spec leaves unplaced is absent.
