# R2 adapter review fork 02, 2026-11-05

No Godot was run. No opcode callee was entered. The idle line still names ~/opus_work/lol2_r12y at 56812f9. These rows were read in ~/opus_work/lol2_r15 at f6a5aa4.

All eight deviation files match r12y byte for byte.

## 0032 cave museum

The row is pending.
Mode-3 objects collide as one box per child, so archway openings stay walkable.
Children under 16 stay walkable, and the slide is the Godot body.
The reason is archway 50 on the gallery to hourglass route.
DECODED: `static_assemblies.gd` admits a child when mask bit 0 is set and the top is at least 16.
Museum mode 3 uses templates 4 and 45: assemblies 50-53 are template 4, and 90, 101, and 102 are template 45.
Cave table 156 is mode 3, template 3, with child types 0 and 1.
The producer source refuses a type-2 child.
The collision test source expects archway 50's opening to pass, its pillar to block, and table 156 child 12 to box.
Godot was not run.
`static_assemblies.gd` differs from r12y only in the L9 raised-deck list, and the mode-3 child path is the same text.
The adapter stays the row.
Books print no such number.
5BFEC and DF8D4 stay unread, and that is the row's gap.
No simpler build keeps the openings while those two addresses stay unread.

## 0033 text owner requests

This note matches r12y.
The first lines say the original player cannot push the shrine blocks.
Each block's only script is a contact for actor 38, and region 1941 spawns the guard.
The longplay shows the blocks closed at 9:05 and open at 9:35. LONGPLAY.
The corrected lines say the 4 fps longplay from 9:04 to 9:10 shows the player pressing the blocks, with no guard in view. LONGPLAY.
Those two longplay sentences stay two sentences.
DECODED: `cave_shrine_doors.gd` matches r12y.
Guard contact and player contact both run the touched control's group, and the slide lasts 1.5 seconds.
AE7D8 was not entered, and that walker stays the row's gap.
HINTBOOK lines 2025-2028 say to grasp the middle pillar and drag it.
BRADY lines 2348-2356, printed page 63, say to drag a pillar aside.
Those pillar sentences print no shrine-block number.
The adapter stays the corrected player-contact lines.
The actor-38 record stays the file's original-data sentence.
What stays open is the unread walker.

## 0034 dark halls

The row is pending.
Doors 56 and 57 toggle on E within 120, the leaf swings 120 degrees in 1 second on its hinge, and the collider is the template box.
A grounded entry into region 1338 slams and locks door 57 and moves shade 73.
Shade 73's death, kind 6 value 10, unlocks it.
Three hits and region 83 stay unhosted.
DECODED: `dark_halls_doors.gd` and its source match r12y.
Reach is 120, swing time is 1 second, and both leaves store swing 120 and a box of 53 by 80 by 4.
E fires kind 4 and also requires a facing dot of at least 0.7.
A grounded point in the trap polygon closes and locks door 57 and moves actor 73.
Health 0 on actor 73 clears the lock and fires kind 6 with caller byte 10, and the same unlock runs when that actor record is missing.
Kind 9 and region 83 are listed unhosted, group 794 is applied as a close while its opcodes stay unread, and stored speed bytes 45 and 30 are unused.
The source file does not store the word template, so template 16 stays the row's word. LIKELY.
HINTBOOK lines 2477-2479 say Luther may chop through a door, and the ghosts say he cannot leave.
BRADY lines 3376-3379, printed page 84, say walls close behind you.
Those stay two sentences. Books print no such number.
The adapter stays the row's E, swing, trap, and unhosted list, and the native speed and group 794 stay open.

## 0035 jungle

The row is pending.
It draws 171 of 228 scenery assemblies on the generic renderer.
It says 53 native solids at least 16 tall block as in the Cave and Museum.
Assembly 57 stays with the terrain mesh.
The witness is the owner's Jungle longplay. LONGPLAY.
DECODED: `L4_HJ/assemblies.json` matches r12y, with placements 228, drawn 171, and owned 1.
Assembly 57 is owned by the jungle terrain mesh and is absent from the drawn list.
The collision file has 53 drawn, unscripted boxes of height at least 16.
Twenty-four drawn boxes are shorter, including deck 227 at height 10, and the runtime also solids deck 227.
The walkthrough adds scripted bridge solids 213, 214, 210, and 212.
`static_assemblies.gd` differs from r12y only by the L9 deck ids, and jungle deck 227 is in both files.
The props test source still prints 53, and its assert expects 54 plus the bridge ids plus causeway unlink ids.
Godot was not run.
Books print no such number.
The adapter stays the row's 171, 228, 57, and 53.
Deck 227 and the four bridge solids stay open, and no simpler build draws assembly 57 a second time.

## 0036 jungle

The row is pending.
It draws 5904 unscripted sprite props as Y-locked billboards and leaves 283 scripted props with their hosts.
Props are walk-through, and animated props share one phase per sprite.
DECODED: `jungle_props.gd` and `props.json` match r12y.
The pack field is props 5830 and excluded_scripted 282.
Materials use `BILLBOARD_FIXED_Y`, and the node builds no collision.
One clock per material advances every instance of that material together.
The props test source says 5830 billboards, and it says 5904 stood before 75 placements with region word 65535 left the set.
5904 minus 5830 is 74, and 283 minus 282 is 1, and those two deltas add to 75. LIKELY that split.
The 75 records were not listed here.
Books print no such number.
The adapter draws 5830 and excludes 282.
The counts 5904 and 283 stay the row's text, and the pack at this commit is the smaller set.
No printed source is more faithful.
The shared phase and the walk-through stay the row.
PROPOSE Jungle billboard counts | props.json props 5830 excluded_scripted 282 and jungle_props_test.gd | acceptance is the row stating 5904 and 283, or naming the 75 region-65535 placements

## 0037 jungle

The row is pending.
A Spark on prop 1350 at state 0 lights 15 flames for good through group 14784.
The first ignition grants magic 100, op2 sub 0x0C value 1, and saves it with the lit state.
An already lit save gets no later grant.
Sound 411 and the screen shake stay unhosted.
The longplay time is 39:44. LONGPLAY.
DECODED: `jungle_oil_fire.gd` and its source match r12y.
The source lists prop 1350 and 15 flame props.
`ignite` returns immediately when the quest is already lit, and a new light calls `player_property_rewards.magic` with 100 and stores lit true.
The script has no sound 411 and no shake.
The oil test source expects the command `020100000c01`, one grant of 100, and no grant for a legacy lit save. Godot was not run.
Op2 was not entered, and that opcode stays the row's gap.
HINTBOOK lines 2286-2291 say an oil pool follows the thorn doors and the Hive entrance is beyond it. BRADY lines 749-750, printed page 21, say a pool of oil can be set aflame by a Spark. BRADY lines 2860-2862, printed page 73, say a Spark on thorn walls keeps the thorns from growing back.
Those stay three sentences. Books print no 15 and no 100.
The adapter stays the row's Spark, 15 flames, one grant, and the two unhosted effects, and group 14784's unread commands stay open.

## 0038 cave

The row is pending.
Chamber arrival starts on entry to region 1221, called a 296-unit corridor, event 2 to g1454, at any height between floor and ceiling.
A player already in regions 1214 or 1189 also starts it.
The old trigger was a 36-unit box on region 1214 with an 8-unit floor check.
Local2 equal to 5 stays unchecked, and the port's own gating stays.
DECODED: `cave_walkthrough.gd` differs from r12y in a lever prompt, and the exit check is the same text.
`EXIT_REGION` is a rect of height 298, while the comment says 296 units, floor -295, ceiling -132.
The height test is y from -295 through -92.
A 36-unit past rect starts the arrival with no floor test, and a chamber polygon starts it at y at or below 22.
`play_chamber_arrival` requires the story assets, the Museum scene, and state `not_started`.
That function leaves local2 unread.
Event 2 and g1454 stay unread, and that pair is the row's gap.
HINTBOOK lines 2083-2086 say to click the east wall and the violet stones to open the way to the museum.
BRADY lines 2505-2509, printed page 66, say to touch the tapestry and then the wall.
Those stay two sentences. Books print no 1221 and no 296.
The adapter stays the row's corridor trigger and the past-region trigger, and the 2-unit rect gap, the extra 40 on the ceiling, and local2 stay open.

## 0039 museum

The row is pending.
Every insert plays 676 and every take plays 677, and fifteen locks play an op24 chain after the click.
Lock 88 uses clips 17 through 20, a take stops the narration, and a load starts silent.
With another item in hand, E puts that item away and takes the key back, and a sconce burn stays off that retry.
Effect props 109-125 stay unhosted.
DECODED: `museum_key_locks.gd` matches r12y, and the audio table stores 676 and 677 on every lock.
Fifteen locks have chains, locks 78 and 87 are empty, and lock 88's chain is 17, 18, 19, 20.
`lock_sound` plays the click, waits out that clip, then plays the chain, and a take or a load stops it.
`museum_walkthrough.gd` differs by a dragon click and a world-item use, and the key path still stows the hand before `use_take`.
`use_take` admits take and give, and a sconce burn stays on the full `use` path.
Op20, op24, and kind 8 stay unread, and those opcodes are the row's gap.
HINTBOOK lines 2093-2104 say to take the triangular key, grab it back, and hear the pedestals.
HINTBOOK lines 4975-5011 say a city room yields a skeleton key and that the early key need not be carried.
BRADY lines 2543-2565, printed page 67, say a recess speaks when the key is clicked, and you cannot leave the Museum without the key.
BRADY lines 2588-2597, printed page 68, say the entrance orb speaks and a floor silhouette takes the key.
Those stay separate sentences. Books print no 676. The adapter stays the row's sounds, chains, take-back, and silent load, and the unread kind-8 timing stays open.

## Receipts

- 0032 cave museum: Text matches r12y. Mode-3 templates 4 and 45 and cave table 156 use one box per child. Children under 16 stay walkable. The slide stays the Godot body. Books print no such number. 5BFEC and DF8D4 stay unread.
- 0033 text owner requests: Text matches r12y. The original says the player cannot push the shrine blocks. The correction says the player presses them open, and the port does that. AE7D8 stays unread. Books print no shrine-block number.
- 0034 dark halls: Text matches r12y. Doors 56 and 57 take E within 120 and swing 120 degrees in 1 second. A grounded entry slams door 57, and shade 73's death unlocks it. Three hits and region 83 stay unhosted. Books print no such number.
- 0035 jungle: Text matches r12y. The pack draws 171 of 228 assemblies, leaves assembly 57 on the terrain mesh, and has 53 solids at least 16 tall. Deck 227 and four bridge solids are extra. Books print no such number.
- 0036 jungle: Text matches r12y. The row says 5904 props and 283 scripted. The pack draws 5830 and excludes 282. Billboards stay walk-through with one shared phase per material. Books print no such number.
- 0037 jungle: Text matches r12y. A Spark on prop 1350 lights 15 flames and grants magic 100 once. Sound 411 and the shake stay unhosted. Op2 stays unread. Books print no 15 and no 100.
- 0038 cave: Text matches r12y. The corridor rect and a player already past it start the chamber arrival. The rect height is 298 while the comment says 296. Local2 equal to 5 and event 2 stay unread. Books print no such number.
- 0039 museum: Text matches r12y. Insert plays 676 and take plays 677. Fifteen locks have narration chains, and lock 88 plays clips 17 through 20. A held item is put away for a take, and a load starts silent. Books print no sound number.
