# Proposals, 2026-11-02

No new PROPOSE line in the idle pass. The lines below are task 19.

PROPOSE item-count pin | r12y 850f717 and c23cc94 pinned item_definitions to 302 Act 1 ids and retargeted jungle_aloe_use_test at the herbalist consumables | a check fails when a test's item total differs from the generator list unless the same commit updates the pin
PROPOSE face-exclusion pin | r12y 850f717 changed l10_progression to the tomb-door and assembly-70 exclusions from astra c981337 | a check fails when an excluded-face total is not the sum of the named sets in that test
PROPOSE chain-save pin | r12y 73dc3c7 had to declare l10_tomb_crossing_earned_test as an earned-save chain | a check fails when a chain test still loads a fixture whose scene or item count is older than the save the chain writes

The commit messages name those three pin classes. They do not name six test files, so this pass does not invent the other three.

R3's four reports and the wall note are already JUNGLE-BACATTA, ITEMS-HALF2-PICKUP, PT-L8-HULINE-SPEECH, PT-L9-WALLS, and the r12y bridge fix. R4's gameplay bugs are already rows 1 through 14 of `ORIGINAL_BUGS_TO_FIX.md`. A second title would duplicate those rows. The lead turns a PROPOSE line into a backlog task; nothing new was offered.

The lines below are task B1. They are gaps in the first Act 2 loop, written out in act2_loop_duck.md.

PROPOSE village double-view | hintbook.txt 3008-3016 says you have to approach a treehouse more than once and go backward twice | STORY-004 names the herbalist, the shaman, the doorway, and Daniel, and does not name those extra screens
PROPOSE catacomb fence crouch | hintbook.txt 3287-3289 says the low-fence leap is run, then jump, then crouch in midair | STORY-009 and STORY-017 name the jumps and do not name the crouch. This is the catacomb fence, not the library window
PROPOSE tower blank globe | hintbook.txt 3335-3337 says that if only one glass globe is held, a blank one can be found in the Mage's Tower | STORY-013 names charging two white globes and does not name that pickup. The step is conditional on holding one globe

The lines below are task C1. They are gaps in STORY-028 through STORY-053, written out in act2_part2_duck.md.

PROPOSE citadel green jump | hintbook.txt 4127-4130 says Dawn's prison and the maidens' cell are reached by jumping into the middle of a circular green thing | STORY-040 names the globes and the upper-left switch and does not name that jump
PROPOSE citadel reward | hintbook.txt 4203-4204 lists a reward from Dawn and the maidens as a condition before the hallway exit | STORY-041 frees Dawn with the dreamstone and does not name a reward. The item is not named here
PROPOSE obsidian mail on | hintbook.txt 4225-4230 says to toss the other armor and put on the obsidian chain mail | STORY-045 sparks the tripod so the mail appears and does not name putting it on. The book calls that mail a key item
PROPOSE niche jump Human | hintbook.txt 4221 says to be Human for the jump from the floe into the river-level niche | STORY-045 names the drop onto the floe and the spark and does not name Human

The lines below are task C2. They are required Act 1 steps the promoted r12x build still does not host, written out in act1_duck.md.

PROPOSE tavern Bacatta | hintbook.txt 2344-2349 and 2416-2422 say Baccata is met in the tavern and then leads Luther to the bridge | WHATS_NEW_r12x.txt still lists him hostile after the Jungle, and TRIAGE_20261102.md 12-22-02 is the same tavern report. JUNGLE-BACATTA is still todo. This pass does not claim a later fix
PROPOSE r12x oily floor | hintbook.txt 2684-2686 and 2798-2801 say the oil hall is passed by a quick step through the fire trap or by putting the flute in the slot | WHATS_NEW_r12x.txt says that flute slot is the next build. r12y hosts the slide and asks if the flute comes back out. The owner has said the flute stays in the wall. This pass does not propose taking it out, and it does not check whether the fire-trap step is hosted

The lines below are task C3. They are gaps in STORY-054 through STORY-093, written out in act3_duck.md.

PROPOSE temple blade bypass | hintbook.txt 4585-4586 says do not walk into the blades and take the passage on the right to bypass that trap | STORY-062 names the angled flute slot and the off-center walk past the boulder and does not name the blade passage
PROPOSE armory fireball ledge | hintbook.txt 5513-5518 says that on the way into the Armory you jump onto the side ledge so the corridor fireball trap does not operate | STORY-090 starts inside the Armory and does not name that ledge
PROPOSE city silverleaf | hintbook.txt 4882-4904 and 5075-5109 say that if you have no silverleaf, the greenhouse pyramid still needs one, and the city room without a floor grows one after an ivory chip is set in the gold-bar pedestal and the left-hand ball of light is followed | STORY-070 names putting a silverleaf in the pyramid and does not name that room. The step is conditional on holding none. A different light chase in the secret storeroom takes the right branch, hintbook.txt 4991-4993, and is not this room

The line below is the 2026-11-04 adapter review. It is the one simpler descent in rows 0227 through 0279.

PROPOSE citadel elevator click | brady_guide.txt 4636-4638, 7984-7985, 8051, and 8574-8575 say click the Brain Switch to lower the elevator | r13 row 0261 binds both Spark and nearby Human E. The simpler descent is the click. The 60 Hz clock stays. Rows 0263 and 0271 are not those sentences

PROPOSE Read opcode 18 flag 0x0812 for a native speed | I29 and act3 DEVIATIONS row 452 | The greenhouse ball stays on the 120 units/s adapter until that speed is read. Do not remove the adapter first.
