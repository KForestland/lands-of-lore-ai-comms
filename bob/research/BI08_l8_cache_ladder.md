# BI08 L8 cache ladder

The ladder worked once. A saved climb then ignored E, on the shelf and back on the ground. The up hop stays the native opcode 18. The way down is the adapter.

## Duck

1. Owner r18, F10 15-30-40, Darker Jungle (-1092,-2627), body height 22. "the ladder only works one time." The triage says a second climb does nothing, so the player can be left above or below.
2. On the chain as a way into the shaman cache. A one-shot climb can strand the player on the shelf, and a player who gets down cannot go up again. The lead asked for every climb, both ways, across a save.
3. Intent: a ladder. You go up to the cache, and you come back down the same way.
4. Contract: walk up to control 69 and press E. You arrive on the floor-100 shelf and stay there. Press E again and you are back at the base where the owner stood. Press E again and you are on the shelf. A save on the shelf reloads on the shelf, and both presses still work. Opcode 20 stays unplayed.
5. Exact: control 69, region 678, opcode 18 destination (-1004, 2590, height 100), region 657. That group is the up hop. It has no return command. The saved packet stays version 1 with the climbed bool, so an old save still loads. Approximate: the return placement, which is the owner's stance (-1092,-2627) at body height 22. Grade DECODED for the up hop (group 12668). Grade for the return: it is not in that group.
6. Cheapest faithful: keep the opcode 18 landing. Stop treating the saved bool as a lock. E on the shelf climbs down to the reported base. E at the base climbs up again. A new region or a second invented opcode 18 would claim a command the group does not have.
7. Earned walk from outside the 96 reach to the reported base, E up, save, reload, E down, E up. The older probe that required a second E to stay on the shelf is the bug, so that one check changes with this rule.

## Source

Control 69 at (-1034, -10, -2606), flags 0x0482, region 678 floor -10. Kind-4 group 12668: opcode 20 sound 780, then opcode 18 direct relocation to (-1004, 2590, 100), region 657 floor 100. No other opcode 18 sits inside 800 of the shaft. I26. The book page for the cache does not say ladder. Grade BRADY for the cache name, not for this climb.
