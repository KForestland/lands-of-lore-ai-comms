# LoL1 one-save chain through the ending attempt

Base is `~/lol1_godot` master `9987d7e`. Apply the ten diffs, then AY02, AY04, and `grok_research/patches/AZ01_lol1_chain_ending.diff`. The test is `tests/lol1_az_chain_test.gd`. The save is `user://lol1_ay_az.json`. Godot `4.7.2.stable.flathub.ed1daf0bf` ran it headless. Exit 0. The present path still printed the index `1` and shapeIndex errors. Level 21 printed `EMC LEVEL21.INF: step limit reached at 53` on the ivory-key visits. The run did not print `5 resources still in use`.

The first write is a click on Michael's box and accept. The save then carries that hero.

| Chunk | Result |
| --- | --- |
| hero | PASS. Michael, level 1 block 557 facing north, credits 41. |
| 1–7 | PASS. The AY04 keep, Timothy, silver key, bloodstones, ivory key, and castle key still hold on this save. |
| 8 tower | PASS. Level 18 has the two prop-192 keys, prop 196 at block 393 flying 8, and the strings LYLE and JANA. Level 20 and level 26 keep their placed keys. Party stays Michael and Timothy. Function 199 and function 734 leave the next level pending. |
| 8 ending | STOP. Levels 27 and 28 do not place prop 255, shard 281, or Whole Truth 280. Script 555 does not add the shard. Level 29 still has castle key 202 and does not place Dawn 198. Script 846 does not add Dawn and does not change level. Flag 347 is set only when item 260 is in hand. `LOLFINAL.TIM` is refused. The fight does not start. The save stays on level 24 with Michael and Timothy. |
| 9 sound | PASS, on that stopped save. Track 12 names PMETLHI at volume 255, track 255 stays silent, syscall 87 plays PMETLHI, and track 250 names LORE01A. The resolver does not open a mixer. |

The chain stops at chunk 8's ending. Chunk 9 still resolves names on the save from that stop. Unread, and not asserted as done: the lake far side, the skull, the wagon, the ruby, Dawn's give, the nest, mine level 26 from function 427, the shard, the Whole Truth, Dawn's key, a crucible, a statuette, and the ending fight.
