# LoL1 A-to-Z chain

One save carried chunk to chunk. Base is `~/lol1_godot` master `9987d7e`. Apply the ten diffs in `grok_research/patches/AM03_lol1_ORDER.md`, then AY02_chase_scream, AY02_tim_voc, AY02_walk_leak, and AY04_lol1_az_chain. The test file is `tests/lol1_az_chain_test.gd`. The save is `user://lol1_ay_az.json`. Each chunk closes the walk and the next chunk opens it with `load_save` true.

The earlier card tests still open their own files and erase them. This chain does not read those files.

Godot `4.7.2.stable.flathub.ed1daf0bf` ran the test headless on the scratch. Each chunk printed PASS and the process exited 0. Entering level 21 printed `EMC LEVEL21.INF: step limit reached at 53`. The present path still printed the index `1` and shapeIndex errors. The run did not print `5 resources still in use`.

| Chunk | Starts from the save | Earned step | Ends in the save |
| --- | --- | --- | --- |
| 1 | no file | new Michael, level 1 block 557 facing north, credits 41 | that position, credits 41, Michael |
| 2 | level 1 block 557 facing north | direction 2, script 621 mask 0x41, then after_scripts | level 2 block 106 facing south, Michael |
| 3 | level 2 block 106 facing south | syscall 75 adds Timothy, id 2 | party of two, Michael then Timothy |
| 4 | that party on level 2 | enter level 15 | silver key prop 173, count 1, block 55, flying 8, party of two |
| 5 | level 15, key still counted, party of two | enter level 16, then function 517 | two bloodstones prop 273, both block 0, no Paulson, party still Michael and Timothy |
| 6 | level 16, party of two | enter level 21, then enter level 29 | ivory key 184 on block 37 flying 8 was present on 21; castle key 202 on level 29 block 211 flying 0; party of two |
| 7 | level 29 | reload only | level 29, key 202, credits 41, Michael and Timothy |

Unread, and not asserted here: the lake far side, the skull, the wagon, the ruby floor, Dawn's give, the nest block, entering level 26 from function 427, the shard, the Whole Truth, Dawn's key, a floor crucible, a statuette, and the ending fight. Level 21's step limit is the same print the tower card already records. The sound resolver is not part of this chain.
