# O01 master open list, 2026-11-05

No Godot was run. Heads at this check: r15 `f6a5aa4`, act3-story `75597f2`. act3-story also has an uncommitted edit in `scripts/lol2/region_visibility.gd`. That file is not a commit, so it is not a fix in this table. The newest owner file is still `TRIAGE_20261104.md`.

The window is 280 reports from 2026-10-23 through 2026-11-04. Two reports on 2026-10-22 sit outside it: Jungle "no wall here", and Hive "the rocks did not fall".

A row is fixed on a tree only when the code commit is an ancestor of that head. Three hashes the older triages cited are ancestors and are not the code: `72d256e` is the CFALL docs page, `4ad7358` is the icon docs page, and `f45de3d` is a registry line. `b89397d` is not an ancestor of r15 or of act3-story.

On act3-story and not on r15: `1c33ac0` (talk with no distance fade, and the Larkhon journal note), `db5efe5` (mid-river drown, Bacatta leaves, louder escort voices), `44a6d98` (L14 doorway cull), `75597f2` (L9 and L10 doorway cull, and the delivered-gift hint).

On r15 and not on act3-story: `330b027` and `f6a5aa4` (Hive lift waits at the bottom, flute on the return), `91db679` (dragon picture travel), `85d1b31` (E prompt at the sleeping Bacatta), `3642265` (Cave lever hint says Pull lever).

Owner order is maps, then quest, then presentation, then other. One table.

| Row | Group | What was reported | r15 / act3-story | Report stamps |
|---|---|---|---|---|
| M-crates | maps | Cave crates will not drag or stack, and the player clips the crate-room wall. | Open on both. No movable-drag commit. | 10-29 19-52-08, 10-28 15-20-41, 10-30 09-18-27, 10-23 19-50-47, 10-31 11-44-44, 10-29 19-52-16, 11-03 17-03-39, 10-30 09-18-05, 10-31 11-45-02 |
| M-roach-box | maps | Died in the crate room with no roach on screen. | Open on both. Triage guess was roaches inside solid crates. No capture commit. | 10-28 15-20-52 |
| M-boulder | maps | Human can jump or walk through the Cave neck rock. | Fixed on both. 1dac1ef closes the neck to every form. 3290fc1 stops a body at the drawn rock. | 10-24 17-32-57, 10-28 15-16-36, 10-28 15-17-55, 10-26 12-07-29, 10-23 19-42-44 |
| M-exit | maps | Player can jump over the Cave exit to the Museum. | Fixed on both. 8125574 uses native region 1221. The old cite b89397d is not an ancestor of either head. | 10-23 19-59-50 |
| M-prop83 | maps | Point-and-click at the Cave side chamber. | Open. r12c classed it original: the chamber stays sealed. No host. | 10-23 19-45-34, 10-24 17-35-03 |
| M-falls | maps | Cave waterfalls do not animate. | Open on both. | 10-23 19-36-30 |
| M-orc | maps | Orc animation clips the stone in front of it. | Open on both. | 10-29 19-52-56, 10-30 09-19-01 |
| M-see | maps | Jungle black blocks and see-through outer walls. | Fixed on both. 7f20130, f56bef4, 596062b, stamp a85780e. Later texture reports are M-jtex, not this row. | 10-26 12-25-29, 10-23 20-44-35, 10-26 12-26-08, 10-23 20-40-03, 10-23 20-21-49, 10-24 14-20-49, 10-26 13-01-50, 10-23 20-46-54, 10-23 20-25-59 |
| M-seams | maps | Jungle slope seams show a sky sliver. | Fixed on both. 135b6f4 names these four poses. | 10-26 12-18-10, 10-26 12-18-30, 10-26 12-17-46, 10-26 12-17-58 |
| M-gorge | maps | Big hole in the Jungle, and the Darker Jungle road blocked. | Fixed on both. 1925b13 names r12e reports 4 and 6. | 10-25 11-05-54, 10-25 11-02-44 |
| M-deck227 | maps | Fall through the thin stream deck. | Fixed on both. 7267cce keeps raised thin decks solid (assembly 227). | 10-26 12-27-18 |
| M-deck210 | maps | Fall through the Jungle bridge. Beast-only break was the owner's guess. | Fixed on both. 8f0f095 makes that deck walkable. The beast-only break was not traced. | 10-24 17-53-16 |
| M-hidden | maps | Hidden blockage in the Jungle. | Open. Bit0 blockers were later turned on (6c0bacf, 77cbe8b, a0e85db). This pose was not re-captured. | 10-26 12-25-08 |
| M-jtex | maps | Jungle faces still wrong after the see-through pass: missing walls, museum marble, items in the sky, missing roof, secret-area wall, bright sky texture. | Open on both. MAP_GAP keeps the Nov 3 sky and texture rows. | 10-29 19-59-59, 10-30 10-07-12, 10-30 09-29-20, 10-29 20-01-15, 10-23 20-47-12, 10-23 20-39-46, 10-30 09-30-00, 10-24 17-58-32, 10-30 09-28-41, 10-30 09-33-50, 10-30 09-40-31, 11-03 17-56-12, 11-03 17-55-53, 10-24 17-50-25, 10-30 09-43-12, 10-30 09-43-24, 10-30 10-42-39, 10-24 17-56-49 |
| M-trees | maps | Chopped tree has no crown. A tree sits in the sky. 10-26 12-19-03 also says the trees have no spiders. | Open on both. MAP_GAP 17-16-55. No floor-snap commit and no tree-spider commit. | 11-03 17-16-55, 10-29 19-59-03, 10-26 12-19-03, 10-24 17-51-00, 10-24 17-49-42 |
| M-brick | maps | Unnamed brick box in the Jungle distance. | Open on both. MAP_GAP 17-26-29. | 11-03 17-26-29 |
| M-bridge-tex | maps | Bridge sequence works. Textures on that span are missing. | Open on both. MAP_GAP 23-04-55. The sequence itself is the quest row. | 11-04 23-04-55 |
| M-causeway | maps | Transparent river-end wall, transparent water wall, and the collapsed causeway side. | Open on both. r12h could not reproduce 13-09-05 from a fresh scene. | 10-26 13-09-05, 10-31 12-10-12, 10-30 09-32-52 |
| M-hive-clip | maps | Hive walls clip, and a flat roof's texture jumps. | Open on both. MAP_GAP 17-41-10 and 17-42-38. | 11-03 17-43-17, 11-03 17-41-10, 11-03 17-43-05, 11-03 17-42-38, 10-24 18-27-16 |
| M-flute-bridge | maps | A Hive bridge should slide out when the flute is used or the lift arrives. | Open on both. No commit names this slide. | 10-30 10-26-06, 10-30 10-26-38 |
| M-call | maps | Hive call button does nothing. | Fixed on both. 8a6b910 plays native sound 388 on every press. The lift-at-bottom row is separate. | 10-23 20-36-20 |
| M-chasm | maps | Hive chasm rocks: a hit from the near side does not drop them. | Open on both. r12c: only rock 233 has a hit body. | 10-23 20-35-01, 10-24 18-03-08 |
| M-mgate | maps | Museum gates, wrong colour, no textures. | Open on both. MAP_GAP 17-14-40. | 11-03 17-14-52, 11-03 17-14-40 |
| M-plank | maps | Museum door bar or plank should slide into the gap. Orb opens the Sk-key panel. | Open on both. | 10-29 19-58-29, 10-30 09-24-26, 10-23 20-18-28, 10-30 09-28-01 |
| M-blocks | maps | Museum blocks cannot be moved. | Open on both. | 10-23 20-12-22 |
| M-dust | maps | Museum dust pile draws on the ceiling. | Open on both. | 10-30 09-27-28, 10-29 19-57-54 |
| M-pillars | maps | Museum pillars the owner remembers are missing. | Open on both. One report, not re-checked against the pack. | 10-31 11-48-56 |
| M-l14 | maps | Textures and geometry wrong. The report area field says Jungle. The Nov 3 triage places the coordinates in Temple L14. | Open on both. MAP_GAP 18-01-10. Portal cull does not retile this. | 11-03 18-01-44, 11-03 18-01-36, 11-03 18-01-10 |
| M-l14-portal | maps | Temple doors are teleporters and their textures clip into the main map. Report area field says Jungle. Triage places it at L14 (-310,-2304). | r15 open. act3-story has the doorway cull 44a6d98. 75597f2 is the L9/L10 cull and is also act3-only. The shared-edge edit in region_visibility.gd is not committed. | 11-03 18-10-50 |
| M-ladder | maps | Darker Jungle ladder under the cache does not work. | Open on both. No ladder commit. MAP_GAP L8-CACHE-LADDER. | 11-04 23-20-29 |
| M-log | maps | Knock a tree down to make a bridge. | Open on both. No knock commit. MAP_GAP L8-TREE-BRIDGE. The owner reached the Larkhon without it. | 11-04 23-23-53 |
| M-dh | maps | Dark Halls: bookcases, explosive crates, barrels, locked door, slots, chain, fruit, and the puzzle exit. Also 'quest bugged, no clue how to save Rix'. | Open on both. No bookcase or blowout commit. 0986d4b hosts Rix as a hostile fighter. That is not the save-Rix puzzle. | 10-30 10-18-53, 10-30 10-14-31, 10-24 18-47-32, 10-26 13-00-17, 10-30 10-12-30, 10-30 10-16-31, 10-30 10-15-04, 10-26 12-55-30, 10-24 18-51-14, 10-30 10-16-12, 10-26 12-59-39, 10-24 18-45-34, 10-30 10-10-26, 10-30 10-17-38, 10-30 10-11-42, 10-26 13-00-32, 10-24 18-47-11, 10-26 12-59-19 |
| Q-kenneth | quest | After the guard speech the gates and the wall should move, Kenneth or the guard should leave, the bridge lever should open the side, and two guards should spawn. | Part on both. cef69bc and merge 5b57410 host the CFALL pool, the FLOOD movie, and lever 67 / gate 71. 79ca69b hosts see-through bars. The docs cite 72d256e is docs only. The wall-then-gates order and the two-guard spawn have no commit. | 10-28 15-23-21, 11-03 17-05-51, 10-30 09-21-34, 11-03 17-05-40, 10-30 09-22-23, 10-23 19-57-17 |
| Q-human-cut | quest | Curse form must become human before the Cave cutscene. | Open on both. No cave caller of request_human was named in a later commit. | 10-24 17-33-52, 10-23 19-44-09 |
| Q-cfall | quest | No point-and-click at the Cave pool. | Fixed on both. cef69bc. This is the pool, not the sealed side chamber. | 10-28 15-19-37 |
| Q-password | quest | The password man is not there, so the owner cannot go on. | The man is still absent on both. The den room chain is b052a4b and the chief hut is a70bdd7. a5346bf keeps the Confidante gate native and the journal names the armorer's glen. That is guidance, not the man. | 11-03 17-33-29, 11-03 17-34-59, 10-24 18-13-45, 10-30 10-05-07, 10-24 18-15-14 |
| Q-larkhon | quest | Cannot drug the Larkhon or finish the Dracoid chain for the sleeping potion. | The serum softlock is closed on both by 054228d. The journal note larkhon_join_tribe is 1c33ac0, act3-story only, not r15. The owner still says the quest cannot be finished (23-25-07). That question is open. | 11-03 18-17-06, 11-04 23-25-07 |
| Q-platform | quest | Cannot raise the Darker Jungle platform. | Fixed on both. 14c5b41 is STORY-053, the tree torches, the shard room, and the Temple return. The cache ladder is the maps row. | 11-03 18-15-18 |
| Q-eggs | quest | Cannot pick up the eggs. | Fixed on both. f3378fd. The triage cite f45de3d is only the registry line. | 11-02 12-25-33 |
| Q-huline | quest | No speech with the cat guys in L8. | Part on both. c497c9d plays the shaman backroom voices. The other Huline lines have no commit. | 11-02 12-25-01 |
| Q-bacatta | quest | Tavern talk made Bacatta hostile. Later he was quiet, did not follow, then had to leave after the bridge film. | Hostile tavern visit is fixed on both by 461ef85. Owner confirmed not hostile (17-36-38, 23-02-17) and that he walks (23-03-14). Quiet escort and bridge voices, and leaving after the film, are db5efe5 on act3-story only. r15 has the earlier reach change 047a849, which the Nov 4 notes still called too quiet. | 11-02 12-22-02, 11-04 23-06-02, 11-04 23-01-56, 11-03 17-55-37, 10-30 10-03-33, 10-30 10-03-18, 11-04 23-04-16 |
| Q-cat-knife | quest | Cat lady should give Daniel the knife. | Owner confirmed it on r14 (23-00-23). r14 stamp 8732a39 is on both heads. No separate feature hash was found. | 11-04 23-00-23, 11-03 17-54-07 |
| Q-dawn-runes | quest | Cannot hand Dawn the wax runes. Sometimes no sound. | The hand-over prompt is on both: 7cd6348. The owner later gave the runes (10-34-32, 10-34-44). First-talk silence was not given its own commit. Distance fade is the voice row. | 10-30 10-33-38, 11-03 17-48-05, 10-31 12-21-47, 10-30 10-34-32, 10-26 12-48-18, 10-26 12-48-48, 10-30 10-34-44 |
| Q-wax-menu | quest | Wax is missing from the hand menu, so the rune quest stops. | Fixed on both. e29367a lists the wax copies first. | 10-25 10-48-57, 10-25 10-47-05 |
| Q-wax-hand | quest | Cannot take Jungle wax while the Prism is in hand. | Fixed on both. c021428 puts the held item away and takes the wax. | 10-24 17-55-50 |
| Q-wax-pit | quest | Cannot enter the hole where the wax is used. | Fixed on both. 3335762 opens the rune pit on walking in. Spark or a fire crystal lights the brazier. | 10-24 18-31-12 |
| Q-shining | quest | Shining Path shortcut does not start. | Fixed on both. ed44f21 on region 1419, then e1d1e59 counts only a real walk-in. | 10-23 20-02-08 |
| Q-ivory | quest | Ivory chip is visible and cannot be taken. | Fixed on both. ed44f21 takes it with an item in hand. The empty urn was the other object. | 10-23 20-03-37, 10-23 20-10-08 |
| Q-locks | quest | Museum key makes no sound, no worm line, and cannot be taken back. | Fixed on both. a5e481a. Not the old b89397d cite. | 10-23 20-06-12, 10-23 20-05-07, 10-23 20-14-17 |
| Q-sk-pack | quest | Sk key in the pack cannot be used while something else is in hand. | Fixed on both. dc5ebed. | 10-26 12-16-09 |
| Q-steal | quest | Skeletons should be neutral, about half of them larger, and they should steal the Sk key. | Steal and the size split are open on both. Waking hostile is what the r10 triage called original. The steal was not hosted. | 10-24 17-46-13, 10-23 20-07-33 |
| Q-gem | quest | Dragon gem has a blue box and cannot be picked up with a sword in hand. | Fixed on both. 0f05727 keys the backdrop and stows the held item. | 10-24 17-40-05 |
| Q-longarm | quest | Cannot take the axe. The platform should trap and change form. | The trap was already hosted. 38cf634 makes the passage-78 guard Enhanced only, so Classic stays native. 4b901fb stows a held item. afc0a0b keeps the tiny form in the chute. All three are on both. | 10-24 17-44-19 |
| Q-hourglass | quest | Breaking the time glass should darken the screen and age the portrait. | Open on both. No trip commit. | 10-24 17-48-31 |
| Q-torches | quest | No torches on the Museum walls, and a niche should light them all. | The 35-torch plate-to-Spark chain is on both via b0b8628 (stamp 09750c8). These two reports were not re-walked after that. | 10-26 12-12-49, 10-23 20-17-07 |
| Q-axe-switch | quest | Switch that opens the door in the Axe puzzle. Later, a wall that will not open. | Open on both. r12h saw an empty niche. No commit names this switch. | 10-26 12-13-30, 11-03 17-09-20 |
| Q-dragon-pic | quest | Click the dragon picture to travel to the southern continent. | Fixed on r15 only. 91db679. Not an ancestor of act3-story. | 11-03 17-16-20, 10-30 09-28-19 |
| Q-imp | quest | Take the imp scroll, the floor drops, then fire. | Open on both. | 10-23 20-22-56, 10-31 11-53-08, 11-03 17-20-06 |
| Q-statue | quest | Switch that opens the door behind the statue. | Open on both. | 11-03 17-20-31 |
| Q-hidden-door | quest | A hidden wall, and a door that should be hidden. | Open on both. | 11-03 17-50-19, 11-03 17-21-01 |
| Q-burn | quest | Spark should burn the bramble. Cut it and it grows back. Tar should ignite. | Open on both. | 10-23 20-28-26, 10-30 10-00-25, 10-30 09-44-46 |
| Q-gland | quest | No poison gland from the cub. | Open on both. | 10-30 09-36-08 |
| Q-spider-atk | quest | The spider attack should start here. | Open on both. | 11-03 17-56-31 |
| Q-t-spider | quest | Temple spider burrows and opens a tunnel. Report area field says Jungle. | 5dcd882 on both qualifies the Temple spider passage. The burrow was not re-walked. | 11-03 18-02-30 |
| Q-quill | quest | The quill opens the tunnel ahead. Report area field says Jungle. | Open on both. | 11-03 18-04-58, 11-03 18-05-07 |
| Q-lift | quest | Hive elevator starts at the bottom and must be called with the flute. | Fixed on r15. 330b027 waits at the bottom. f6a5aa4 plays the flute on the return when it is already down. Neither commit is on act3-story. | 11-03 17-41-36 |
| Q-hive-door | quest | A Hive button should open a door. Another door will not open. | Open on both. r12c: call post 127 only sets the lift target. | 10-30 10-26-54, 10-24 18-25-02 |
| Q-hive-puz | quest | Four-button order, the boulder that breaks the floor, rock traps, and a puzzle that does not work. | Open on both. | 10-30 10-30-07, 11-03 17-45-07, 10-30 10-31-19, 10-30 10-32-45, 11-03 17-43-48, 11-03 17-45-36 |
| Q-alcove | quest | Cannot move the boxes in the Hive alcoves. | Open on both. | 10-24 18-26-55 |
| Q-hive-marks | quest | Owner marks a bow, a shield, a flute, a pulse door, traps, a ring, and a flute slot. | Part on both. 6a29807 hosts Hive item rows 5-9, including Kelen's ring. The bow, shield, flute pickup, and pulse door are not named by that commit. | 10-24 18-27-43, 10-24 18-29-53, 10-31 12-19-37, 10-24 18-30-56, 10-24 18-30-07, 10-24 18-35-09, 10-24 18-27-31, 10-24 18-29-34 |
| Q-flute-note | quest | Owner marks where the flute calls the elevator. | Note. The call itself is the lift row. This report predates the bottom-wait fix. | 10-24 18-23-32 |
| Q-chief | quest | Chief point-and-click does not start. | The hut chain a70bdd7 and the r12f CHUT room (stamp 6c0bacf) are on both. Why 18-12-30 started nothing was not re-tested. | 10-24 18-12-30 |
| Q-bridge-seq | quest | Bridge should break after Bacatta's tour, or when someone is mid-bridge. Later the delay feels long. | The tour working is an owner confirmation on r14 (23-04-55), and r14 is on both. A collapse under a creature was not adopted. Textures are the maps row. Bacatta leaving is db5efe5, act3 only. | 10-25 11-05-08, 10-26 13-08-18, 10-30 10-44-26 |
| Q-spark | quest | Spark should raise the Ruins bridge. | Fixed on both. a6b7a96. | 11-02 12-31-30 |
| Q-drown | quest | Cannot drown in the river. | Form drowning is on both (fda6866, 4cbbb8e). The Nov 4 bank-less mid-river spot is db5efe5 on act3-story only, via tools/propagate_liquid_surface.py. r15 does not have db5efe5. | 11-04 23-05-28 |
| Q-fall-text | quest | Fell in the river. The recover line is drawn on top of another line. | Fixed on both. 6a8b574. | 11-03 17-57-47 |
| P-dawn | presentation | Dawn is about 3 m tall. | Fixed on both. 236c7f7 sets BODY_SCALE 0.282. 29810ab was the earlier talk-clip size. | 10-31 11-59-30, 10-25 10-50-53, 10-30 09-59-04, 10-28 15-30-39 |
| P-tall | presentation | Bacatta looks about 4 m. A Jungle man looks 3 m and two cat-lady animations do not play. | Open on both. No Bacatta body-scale commit. | 10-26 12-29-38, 11-03 17-32-47 |
| P-kelsrick | presentation | Kelsrick stands with a knife out while peaceful. | Fixed on both. 5879749 uses selector 18 until he wakes. | 10-28 15-36-05 |
| P-ui | presentation | UI and inventory too small on a large display. One report says 150% looks best. | Fixed on both. 12e35a1 scales by window height and adds 300% and 350%. Icons are 6576693. The 150% report is a confirmation of the default. | 10-26 12-06-08, 10-23 19-47-36, 10-23 20-11-43 |
| P-fringe | presentation | Sprites have a blue fringe. | Open on both. | 10-23 19-53-49 |
| P-speed | presentation | Museum walk and run should match the Cave. | a0ba86a on both is one shared walk/run pair. The Museum complaint was not re-measured. | 10-24 17-37-45, 10-23 20-01-13 |
| P-voice | presentation | Kelsrick, Dawn, and Bacatta are too quiet. One report is 'no sound from the guy'. | Reach unit_size 300 is on both (047a849). Speech with no distance fade is 1c33ac0, act3-story only. r15 does not have it. The Nov 4 quiet reports are the Bacatta row. | 11-03 17-35-21 |
| P-lock-glow | presentation | Museum lock shows a flat plate. The key should glow as a triangle. | Open on both. | 10-26 12-12-18 |
| P-hive-surf | presentation | Hive gas does not flow or stay transparent. Green-blue floor. Bridge holes. No platforms. Falling walls are slow. Brazier wall is transparent. Red gas and a falling-rock animation look wrong. | Open on both. MAP_GAP keeps 17-27-36. | 10-31 11-58-11, 10-30 09-58-01, 10-30 09-50-35, 11-03 17-29-05, 10-30 09-46-09, 10-30 09-50-03, 10-31 11-56-13, 11-03 17-27-36, 10-24 18-06-42, 10-30 10-32-17, 10-31 11-57-30, 10-30 09-51-11 |
| P-ghost | presentation | Dark Halls ghost looks stretched, not blue and transparent. | Open on both. | 10-30 10-13-23 |
| P-rats | presentation | Cannot hit the skeleton rats. | 8f0f095 on both says the small-creature capsules match the sprites. The Dark Halls pose was not re-walked. | 10-24 18-44-04 |
| P-barrel | presentation | A Jungle barrel does not crumble. | Open on both. Dark Halls barrels are the Dark Halls maps row. | 10-29 20-00-14 |
| P-lift-btn | presentation | Lift buttons have a tiny hit box. | Open on both. The later 'buttons work great' report is a different spot. | 10-24 18-24-39 |
| O-light | other | Cave light should be ambient plus sources, torch flames should flicker, and the 0 key should change the lighting. Flames should push a darkness filter. | Open wishes. No commit. | 10-30 09-12-24, 10-31 11-46-18, 10-30 09-11-20, 10-23 19-37-59, 10-31 11-47-00 |
| O-spells | other | Charged spells: a bigger Spark, a travelling orb, a lightning strike. | Open wish. | 10-23 19-41-10 |
| O-roaches | other | Wants more roaches, and roaches that scatter. One report is the death pit. | r12c: all 23 native roaches are hosted and no scatter behaviour exists in the source. Scatter stays a wish. The crate-room death is the other row. | 10-23 19-41-40, 10-24 17-32-32, 10-23 19-54-30, 10-23 19-49-51 |
| O-pillars | other | Stone pillars should move with E. The owner also said it works as it is. | Open wish. | 10-23 19-49-02 |
| O-shards | other | Hitting the blue crystal should chip three fire shards. | Open wish. | 10-23 20-08-57 |
| O-prism | other | Prism sword blinds on hit. | Open. Triage left it as a check. | 10-23 20-15-40 |
| O-crouch | other | C should crouch. | Open wish. 11-03 17-10-12 is this row. 10-31 11-44-44 also asks for crouch and is filed on the crate row because that sentence leads with the boxes. | 11-03 17-10-12, 10-23 20-19-17 |
| O-birds | other | Birds should fly. | Open wish. | 10-23 20-20-23 |
| O-ape | other | An ape stands still. | Open. No AI commit names this actor. | 10-23 20-21-06 |
| O-map | other | Map should scale, look like a book, and show points of interest. | Open wish. | 10-23 20-26-41 |
| O-lizard-mark | other | Lizard cave entrance, a tunnel the owner does not remember, and a spot the lizard form can reach. | Open markers. No commit. The reach spot was left as a content check in the r10 triage. | 10-23 20-32-04, 10-30 09-42-30, 10-23 20-42-26 |
| O-spark-lake | other | Spark should bonus a spell and fire the lake. | Open. Triage left it as a confirmation question. | 10-23 20-33-00 |
| O-dark-entry | other | Cave entrance in the Jungle should get darker. | Open. | 10-23 20-33-37 |
| O-spiders | other | Two spiders where the owner remembers one. | r10 triage: actors 32 and 34 are both original. Left as original. | 10-23 20-35-36 |
| O-belt | other | A five-slot quick belt in the middle of the screen. | Open wish. Triage asked Classic or Enhanced. | 11-03 17-24-43 |
| O-gate-which | other | Museum gates should close after the player walks through. Which gate was not named. | Open. No gate record was found near that spot in the r12c triage. | 10-24 17-38-13 |
| O-hive-note | other | Jumping puzzle in this Hive room. | Note. No host in the r12c triage. | 10-24 18-03-46 |
| O-chest | other | Chests should open an inventory. | r12c: native use grants the items. A chest window is an Enhanced wish. | 10-24 18-49-45 |
| O-bed | other | Nothing under the bed. | Open. r12c could not read the nearest scripted bed. | 10-24 18-50-00 |
| O-root | other | Transparent texture in the root wall. | Open as a question. r12h: the cut-outs are the art. A vertical seam would be a texture edge. | 10-26 12-21-10 |
| O-vine | other | Something should cover a Jungle entrance. | Open. Not identified. | 10-26 12-24-21 |
| O-fight | other | A fight option appears when speaking to Bacatta. | Open. r12h could not tell cursor from dialogue. He is non-hostile by the later confirmation. | 10-26 12-29-07 |
| O-click | other | Point-and-click expected at a stream, and again in the Jungle. | Open. The object was not named. | 10-26 13-04-16, 10-31 12-08-56 |
| O-delay | other | The time delay is too great. | Open. The report does not say which delay. The bridge tour is the sequence row. | 10-30 10-44-51 |
| O-good | other | Praise or a confirmation that the current behaviour is right. | No change. Hive wall collapse, Hive buttons, UI at 150%, Bacatta not hostile, volume and walk normal on 23-03-14. | 10-24 18-05-05, 11-04 23-03-14, 10-26 12-37-34, 11-03 17-36-38, 10-28 15-15-38, 11-04 23-02-17 |

## Triage rows with no F10 file

| Where | What the triage said | r15 / act3-story |
|---|---|---|
| L9, 2026-11-02, no position | Trapped in a wall. Later, many Ruins walls are no-clip. | `a3311c5` turned Ruins bit0 walls on and `1b775ba` reverted that. The current walls commit on both heads is `d5c1b0b`. No position was filed, and this pass did not re-walk it. |
| r12l recording | Inventory showed ground sprites. | Fixed on both by the icon commit `6576693`. |
| r12l recording | Dragon Gem says no inventory use is known. | Open. The triage called it an items-behaviour gap, not a new report. |
| r12l recording | Cave tar reads as a black void. | Left as probably native. The longplay also shows a black tar pit. |
| r12l recording | Weapon shop, no error seen. Two deaths to the cave-mouth guards. A focus_entered disconnect line at launch. | No gameplay row. Guard deaths were called native. The disconnect line was called engine noise. |
| r12c note | Dark Halls orb start, one-by-one Shade pull, pit floor, broken-wall exit, Rix talk, scroll use. | Open. They were listed because the owner did not file them. The filed Dark Halls reports are M-dh. |

## Counts

280 reports are in the table. 114 rows. Group sizes by report: maps 111, quest 97, presentation 31, other 41.

The maps that are still open on both heads are the crate drag and the crate-room clip, the Hive clip and the flute bridge, the Jungle faces filed after the see-through commits, the Museum gate colour, plank, blocks, and ceiling dust, the Temple texture and geometry, the cache ladder, the knock-down tree, and the Dark Halls puzzle. The quests still open on both heads are the password man, the unfinished Dracoid step, the quill tunnel, the imp-scroll floor, the statue switch, the hidden door, the bramble and the tar, the poison gland, the spider-attack start, the Hive door, the four-button order, and the boulder cellar.

L9 and L10 portal visibility is `75597f2` on act3-story only. r15 does not have it. This list does not review that commit again.
