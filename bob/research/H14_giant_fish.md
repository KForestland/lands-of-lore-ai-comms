# H14 Giant Fish by the land bridge

Beat 33. `L4_HJ`. The fish command is the river regions' death list. Drowning on this river is a separate hosted beat and was not reopened. Opcode 2 arm 57 was not given a new callee. The handlers at `0xD7E54` and `0xB3B04` were not entered.

OPTIONAL. HINTBOOK 2225-2229 tells you to drown in the large river near the big land bridge at least once, to see Luther eaten by the Giant Fish. It is a spectacle, not a step in the outline just above it (2220-2222). BRADY 2754-2755 is the general deep-water warning and does not name the fish. BRADY 7632's giant worm is a different sentence.

## The death groups

439 groups contain opcode 2 `020100003900`. Byte 4 is 0x39, which is arm 57. 436 of those groups also contain opcode 21 `1503a1001c00`. Byte 4 of that command is 0x1C, index 28. The movie-name table's index 28 is the cstring `fishdeth`. No command byte stores the filename. Playback was not re-entered.

436 of those pairs are region kind-12 events. 425 of the 436 also contain opcode 198 `c60000003101`, which stores 1 at local 49. Slot 49, file 13153135 plus 49 times 41, is `Stop_Hive_Warrior_OT`. The store is the proven opcode 198 write. What the local does to the bridge fight was not read.

The search point used for the bridge river is native (5452, 4100). Nearest fish regions, all floor −200:

| region | center | group | sets local 49 | distance |
| --- | --- | --- | --- | --- |
| 4384 | 5383, 4058 | 16886 | no | 81 |
| 4388 | 5431, 3958 | 17064 | yes | 144 |
| 4365 | 5323, 4262 | 16478 | yes | 207 |
| 4385 | 5241, 4049 | 16904 | yes | 217 |
| 4389 | 5303, 3926 | 17088 | yes | 229 |
| 4368 | 5180, 4250 | 16550 | yes | 310 |

Sample groups 8474, 8498, and 8522 match the MIX. Their raw is `c600000031011503a1001c00020100003900` plus the group header. Region 4384 is the nearby row that plays the movie command and the arm without writing local 49.

## Opens

- Which of the 436 regions is the one step the player takes off the land bridge. The nearest is 4384.
- Playback of `fishdeth`, and arm 57's own effect beside that command.
- The 3 arm-57 groups that do not carry this movie command. They were counted and not listed.
- The 8 opcode-21 index-28 commands that sit outside the 436 pairs. They were counted and not listed.
- No longplay frame was opened.

## Grades

HINTBOOK 2225-2229 for Luther, the land bridge, and the Giant Fish. DECODED for the 436 region pairs, local 49, and the index-28 cstring. FRAME open.
