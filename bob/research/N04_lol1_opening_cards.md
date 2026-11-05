# N04 LoL1 opening cards

No Godot was run. `script_walk_test.gd` was not run. These cards stop when Roland is found. The throne return, the poisoning, and the Draracle stay on L03's later cards. The walkthrough order is Roland before the poisoning. The classic reference puts the Draracle first. Those orders stay unmerged.

The step source is `~/ScotiaEraPrototype/RESEARCH/LoL1_Walkthrough.md`. Grades below cite that file as WALKTHROUGH. The manual page is `<owner-media> files or things/LANDSoL/!-landslore-manual.txt` page 1. Placements are the N03 markers. `tests/script_walk_test.gd` is the existing keep check.

Acceptance on each card is the LoL2 production sentence: semantic use, save/reload, wrong item refused, earned route, one owner. A missing piece stays in Unknown.

## LOL1-OPEN-01

Player clicks one of the four portraits. Place: before Gladstone. Item: none. Page: WALKTHROUGH opening scenes, and the manual page 1. Acceptance: the new game stores that hero and a reload keeps the id. No wrong-item check. The earned route is that one hero through OPEN-06. One owner.

WALKTHROUGH calls Kieran balanced, Ak'shel magic-focused, Michael combat-focused, and Conrad rogue-focused. L03's reference calls Kieran the fast one and Conrad balanced. The manual calls Ak' Shel the magic one, Michael the fighter, Kieran the fast one, and Conrad well-rounded. The manual spelling is Ak' Shel. The id table spelling is Ak'shel. Those sentences stay unmerged.

DECODED from M03: the ids are Michael -1, Kieran -8, Conrad -5, Ak'shel -9. `party.gd` starts from those four. `raceClassSex` is 0, 0, 2, and 4 on Michael, Conrad, Kieran, and Ak'shel, with no specialty names. Character select is not in the port.

## LOL1-OPEN-02

Player hears the king in the throne room. Place: Gladstone Keep, LEVEL1, area KEEP. Item: none. Page: WALKTHROUGH Gladstone step 1. Acceptance: the throne line plays once and a reload does not repeat the grant. No item to refuse. Earned route starts at block 557 facing north, which the test file asserts and this pass did not re-run. One owner.

Unknown: the throne function. TIM is not in the port. The function number of block 557 was not read.

## LOL1-OPEN-03

Player takes the King's Writ from Geron. Place: Geron's office. Item: type 244, Writ of Passage. Page: WALKTHROUGH Gladstone step 2. Acceptance: the writ is in the pack, a reload keeps it, a different item is refused, and the route is the office before the gate. One owner.

Unknown: Geron's block and the give call. No N03 marker places type 244. Whether function 621 tests the writ was not read.

## LOL1-OPEN-04

Player opens the library with a key and takes the Magic Atlas. Place: King's library. Item: library key type 185. Page: WALKTHROUGH Gladstone step 3. Acceptance: the atlas is carried, a reload keeps it, a wrong key is refused, and the route is after the writ. One owner.

Unknown: both blocks. No ONETIME name contains atlas. No N03 marker places type 185. The key's open call was not read.

## LOL1-OPEN-05

Player buys a mace and sells a dagger at Victor's Arms. Place: the keep shop. Item: a mace. Page: WALKTHROUGH Gladstone step 4. L03 does not mark this stop required. Acceptance: the mace is bought once, a reload does not buy it again, and a sale without the dagger is refused. One owner.

Unknown: the shop function and the mace type. LEVEL1.INI makes Halberds. That grant was not named as this shop.

## LOL1-OPEN-06

Player leaves by the north gate into the Northland. Place: LEVEL1 block 589, facing south, using the wall ahead. Item: none in the test. Page: WALKTHROUGH Gladstone step 5. Acceptance: the arrival is level 2 block 106 facing south, a reload keeps that arrival, and the guard on the start side refuses the step. The test file is that check. This pass did not re-run it. One owner.

DECODED from `level_data.gd`: facing 2 steps by +32, and 589 + 32 is 621. DECODED from `walk.gd`: direction 2 is South and direction 0 is North. LIKELY, N03: LEVEL1.INF function 621, mask 0x0041, `loadNewLevel(2, 106, 2)`, after a tainted branch. The test file asserts the arrival numbers. LEVEL2.INF function 74, mask 0x0041, `loadNewLevel(1, 589, 0)`, is the return, also LIKELY.

Unknown: the writ check on this gate.

## LOL1-OPEN-07

Player takes the lantern and the thugs' key, then the lock picks from the chest. Place: the walkthrough says the Northland hideout. LEVEL5's English name is Thug's Hideout and its area is CAVE1. Those two place sentences stay unmerged. Item: lantern type 249, Thug's key type 167. Page: WALKTHROUGH Thugs' Hideout. Acceptance: both items are carried, a reload keeps them, a wrong item on the chest is refused, and the route enters from LEVEL2. One owner.

LIKELY, N03: lantern on LEVEL5 block 97, Thug's key on block 165, both from LEVEL5.INI function 1. Two exits, both LIKELY: LEVEL2.INF function 96, mask 0x00C3, and function 99, mask 0x4001, each `loadNewLevel(5, 260, 3)`. Face 3 was not named. M03 left faces 1 and 3 unnamed. `walk.gd` lists index 3 as West. Those two sentences stay unmerged.

The lock picks stay a separate sentence. WALKTHROUGH puts them in the hideout chest. LEVEL6.INI function 1 creates type 245 on Caves Level 1, block 168, grade DECODED. The hideout chest and that cave placement were not merged.

Unknown: the lever, the plates, the three buttons, and the chest. The walkthrough's rock steps were not given control ids. LEVEL5 does place Rock type 99. A rock row is not a plate.

## LOL1-OPEN-08

Player takes the compass in the Grey Eagle and Timothy joins. Place: Southland Forest, LEVEL3, area FOREST1. Item: a compass. Page: WALKTHROUGH Southlands steps 1 and 2. Acceptance: Timothy is in the party, a reload keeps him, and a second join is refused. One owner.

DECODED from M03: Timothy is id 2. No concrete `addRemoveCharacter` for id 2 was found. No ONETIME name contains compass. `game_state.gd` has `compass_broken`. Lands string 603 says the compass appears broken. That string was not joined to an item. LEVEL3 dialogue contains the substrings Timothy and Roland. A substring is not a placement.

LIKELY, N03: LEVEL3.INF function 772, mask 0x0041, `loadNewLevel(4, 167, 0)`. That is the manor exit, not the inn.

Unknown: the inn block and the join call.

## LOL1-OPEN-09

Player reads the burnt scroll, takes the oil and the aloe, passes the ogre by bluff or by fight, and finds Roland. The chest opens with Roland's key. Place: Roland's Manor, LEVEL4, area MANOR. Item: Roland's key type 166. Page: WALKTHROUGH Roland's Manor steps 1 through 6. Acceptance: the scroll has been read, Roland's scene has played, the key is carried, a reload keeps them, a wrong item on the chest is refused, and the route is the LEVEL3 exit onto block 167. One owner.

LIKELY, N03: Roland's key on block 41. Aloe type 217 and Oil Flask type 248 share block 260. The walkthrough's hidden niche and that shared block were not joined. LEVEL4.INF function 199, mask 0x0083, `loadNewLevel(3, 804, 2)`, is the way back.

Unknown: the burnt-scroll type, the ogre block, which ogre choice is required, and the saber. The ruby is already gone in the walkthrough. No placement for it was read here.
