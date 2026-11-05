# R2 adapter review fork 05, 2026-11-05

No Godot was run. No opcode callee was entered. The idle line still names ~/opus_work/lol2_r12y at 56812f9. These rows were read in ~/opus_work/lol2_r15 at f6a5aa4.

Each of the eight row files matches r12y byte for byte. `jungle_walkthrough.gd`, `build_jungle_blocker_routes.py`, `jungle_blocker_routes_test.gd`, `L4_HJ.json` blockers, `jungle_river_dam.gd`, `player_curse.gd`, `player_form_rules.gd`, `jungle_river_dam/source.json`, `L5_HC/assemblies.json`, `hive_chasm.gd`, `dialogue_skip.gd`, and `museum_dragon_heart.gd` match r12y. `region_blockers.gd` differs only on Savage Jungle strip 2417. `hive_review.gd` differs by a jump-input helper. `static_assemblies.gd` differs by L9 raised decks 481-483.

## 0056 jungle

The off-switch does not stay. The live walls do. DECODED: `jungle_walkthrough.gd` sets `region_blockers_enabled` true and attaches `region_blockers.gd` on L4_HJ. The pack lists 946 blocked regions and 815 edges. Ids 883, 1318, 3211, 3355, 3501, 3805, 3811, and 4543 are the dynamic set and are absent from the blocked list. Wall headroom is 1024. A centre already inside drops the blocker layer until it leaves the outline. The blocker layer is separate from aim rays. Creatures stay off that layer.

B0D98 and AFF85 stay unread. That mover pair is the row's gap. Op197 stays unread. A later chamfer in the same host shortens a portal corner so the capsule can use a narrow native opening. The fringe walls stay.

The books print no such number. HINTBOOK lines 2225-2228 say jungle streams and the large river can drown Luther. BRADY lines 2754-2755, printed page 72, say shallow streams are wadeable and deep water drowns. Those sentences print no region count.

0057 is the live on-switch. The old fixture crossings of 29 stay the row. They were not remeasured.

PROPOSE Retire the 0056 off-switch | jungle_walkthrough.gd region_blockers_enabled true and row 0057 | Acceptance is 0056 marked historical and 0057 left as the live blocker row.

## 0057 jungle

The on-switch stays. DECODED: `build_jungle_blocker_routes.py` removes every edge into a blocked region, then walks source neighbours. With the west side refused, the magic-shop route uses passage 2443/3805. The tool writes 9 files and 15 routes when avoidance is on, including Dark Halls entry6 and both chief-hut legs. It does not write `chut_pool_route`.

DECODED: `jungle_blocker_routes_test.gd` lists 10 fixture files and 16 route names, adds `chut_to_pool`, and rejects a route that enters a blocked id. Region 3555 is in the blocked set. The test source stops a walk into it. Godot was not run, so the pass itself stays unread. The row's 12 routes and 8 files are short of this census. The 6-12 lengthening was not remeasured. It stays the row.

Op197 stays unread. The books print no such number. The same HINTBOOK and BRADY water sentences as 0056 print no blocker count.

PROPOSE Recount 0057 routes | tests/jungle_blocker_routes_test.gd ROUTES | Acceptance is the row naming 10 fixture files and 16 routes, or a note that chief-hut and chut sit past the stated 12 and 8.

## 0058 jungle

The dam host stays the row. DECODED: `jungle_river_dam.gd` and its source pack. Durability starts at 50. The break threshold is 1. Human armed damage in `player_form_rules.gd` is 8, so seven human armed hits leave 1 or less. Beast damage there is 12. Lizard damage there is 1. Non-breaking hits play sound 956. The breaking hit plays 719. Awards are 500 and 500. Movers are 76: 66 relative -50, 9 relative -20, and region 4543 absolute -70. Speed 3 times 2.5 is 7.5 units/s. Settled floors swap to the pack's final face. Stones are 37 and cover rows are 46. Both take that floor offset. `walls_after` has 87 faces. Twenty have an empty material. The host collides those and draws the rest. Timer countdown is the stored 1140 at 60 ticks/s. The ask is 120 to 180. `player_curse.gd` caps duration at 450.

LONGPLAY 35:36-36:42 stays the row's witness for two hits. Native weapon damage stays untraced. Opcode 649D8 stays unread. That decoder is the row's gap. Burrow room records are floor -70 and ceiling -50. The lizard-only mouth stays the row. The walk was not run.

BRADY lines 2811-2814, printed page 72: attack the waterspout in the northernmost river, the river dries, and a lizard tunnel holds items. HINTBOOK lines 2225-2228 name drowning in the large river and print no waterspout. Those stay two sentences. The books print no such number for 50, 500, 1140, or 19 s.

A one-strike drain would be simpler and would drop the durability record. The record stays. The two-hit witness and the unread decoder stay open.

## 0059 hive

The generic renderer stays the row. DECODED: `L5_HC/assemblies.json` counts 157 placements, 96 drawn, 11 owned, and 50 without faces. Owned ids are rune entry 0, Reaver amber 121 and 123, and elevator 125 through 132. `hive_review.gd` calls `static_assemblies.setup` for L5_HC. `static_assemblies.gd` draws those faces and builds the native solid boxes for the drawn set. The Hive call passes no extra owner list.

The 50 faceless placements stay outside the row's sentence. The row's "same recipe as the Cave/Museum/Jungle" is this one renderer. Boxes under height 16 stay walkable in that shared file. Hive has no raised-deck exception. The r15 diff on `static_assemblies.gd` is the L9 balcony list. The assembly counts file matches r12y.

The books print no such number. HINTBOOK lines 2569-2573 describe the Hive as a hack-and-bash cave and print no assembly count. No simpler split is sitting in the host. The faceless 50 stay open. No opcode is named, so none was left unread beyond that silence.

## 0060 hive

Spark on the rock stays. The gorge rescue stays until a fall rule is read. DECODED: `hive_chasm.gd` puts rock233 on melee layer 4 and Spark layer 8. `receive_spark` calls `activate`. The gorge list is 25 region ids at floor -600. Standing on that floor writes a fixed east-bank point and the line "You climb back out of the gorge." The host comment names that point region 121. The polygon test for region 121 was not added here.

Kind9 mask 0x09FF stays the row's sentence. That mask was not entered. The native fall rule stays the row's gap. The owner line from 2026-10-22 is the witness that Spark missed while the player was in the gorge. r7c melee-only stays the row's history. The rescue is the port's stand-in for that untraced fall. A sealed gorge lip would be simpler and would hide the fall. The Spark layer stays.

HINTBOOK lines 2594-2597: drop the rocks overhead to bridge the ravine, and a crossing without dropping them is possible. BRADY lines 2934-2948, printed page 75: spark the ceiling boulders so the rocks fall, and a lizard-sized passage is the other way. Those stay two sentences. The books print no climb-out line and no region 94 or 121. The unread mask and the fall stay open.

## 0061 all

Enter stays the row. DECODED: `dialogue_skip.gd` takes Enter and keypad Enter and calls the first `skip_line`. Each owner pushes its own clock. Hosts cover monastery rooms, including CAN and LIZ, both shops, Hive rune entry, Kelsrick, Jungle Dawn, Hive Dawn, Bacatta65, Kityara, the drunk, the exit woman, the village gate, the follow-up child, the Hive warrior talk, story clips, departure, the jungle exit movie, the cave captain, the guard sequence, guard-control clips, the old orc single pass, and the chief hut movie. Bacatta65, the exit woman, and the old orc return false when the clip is repeating. Story `skip_line` advances one clip. Esc still closes the whole story.

The row's reason is the owner request. Space and left click stay jump and attack, so the chosen key is Enter. The autoload returns false when nobody is speaking. Follow-up speech inherits `skip_line` and overrides `skip_remaining`. A single global speech clock would be simpler and would finish another speaker's line. This per-owner clock stays.

HINTBOOK lines 989-991 name the star key for skip conversation, and say never skip a first hearing. BRADY lines 804-811, printed page 22: an hourglass means you listen. BRADY lines 822-824, printed page 23: click again to keep talking. Those stay two sentences. The books print no Enter-skip. The hintbook file has no PDF page marker beside line 989.

Thieves den, the cave fall room, and the L8 backroom also implement `skip_line` and sit outside this row's list. That later list stays open.

## 0062 text piece

The file is one newline. It matches r12y. The byte size is 1. It states no date, no area, no claim, and no host. No script name appears, so no gameplay file was opened for this piece. Hintbook and Brady were given no distinctive word from this file. No HINTBOOK, BRADY, LONGPLAY, or DECODED grade attaches.

There is no adapter to keep and no simpler build to choose. The books print no such number. The empty piece stays open. A board can ignore it until it holds a row.

## 0063 museum

The plain-item retry stays the row. DECODED: `museum_dragon_heart.gd`. Reach requires an empty hand, the gem visible, and the revealed or departed phase. `use` appends the gem only while `carried_collected` is under `MAX_CARRIED` 64. A full pack feeds back "You cannot carry more." and leaves `taken` false, so the gem stays and E can retry. The held item is put away by the hand check. This pickup does not consume it.

The row names the existing plain-item adapter and owner r12c report7. Status in the row is pending. The gem sprite stays visible while the phase is revealed or departed and `taken` is false. Spark starts the movie in this same host. That movie is outside this sentence. A pickup that consumed the gem on a full pack would lose the retry. This refusal stays.

BRADY lines 2645-2647, printed page 69: fire a spark at the Dragon Heart Statue and take the Dragon Gem that is revealed. HINTBOOK lines 2104-2107: a spark on the brown blob reveals a lightning crystal, and the same room lists a dragon gem among the pickups. Those stay two sentences. HINTBOOK lines 1391-1393 say to use another dragon gem once you have it. That is the item, and it prints no museum retry. The books print no E retry and no pack size. The pack constant stays open only as a port limit. The books print no such number.

## Receipts

- 0056 jungle: The live Jungle host keeps the 946-region blocker walls on, so the row's r11 off-switch does not stay. B0D98 and AFF85 stay unread. Books print no such number.
- 0057 jungle: The on-switch, the route rebuild tool, and the blocker test stay, and the test lists 16 routes in 10 files against the row's 12 and 8. Op197 stays unread. Books print no such number.
- 0058 jungle: The dam host stays on durability 50, human armed damage 8, seven hits, and a 1140-tick lizard timer, while the longplay's two hits stay the witness. Opcode 649D8 stays unread. Books print no such number.
- 0059 hive: Hive static assemblies stay 96 drawn of 157, with 11 left on the rune entry, Reaver amber, and elevator hosts. Fifty faceless placements stay outside the sentence. Books print no such number.
- 0060 hive: The chasm rock stays open to Spark and melee, and a player on the gorge floor is returned to the east bank. The kind9 mask and the native fall rule stay unread. Books print no climb-out line.
- 0061 all: Enter stays the per-line skip for the row's speakers, and idle loops stay unskipped. Hintbook names the star key and Brady says listen then click again. Books print no Enter-skip.
- 0062 text piece: The file is a single newline and matches r12y, so there is no claim to host. Books print no such number.
- 0063 museum: The Dragon Gem pickup stays an empty-hand retry, and a full pack leaves the gem in the world. Brady says spark the statue and take the revealed gem. Books print no pack size.
