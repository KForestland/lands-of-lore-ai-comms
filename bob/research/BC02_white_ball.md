# BC02 — STORY-072 white ball keeps the charge adapter

Scratch only: `/tmp/bc-act3` at `e21eb43`. `break_ice` is unchanged. The live tree was not edited.

## Book

Hintbook 4831–4832, counted by newline (the file contains form-feeds; Python `splitlines` is not the citation count):

> A third-level summoned imp destroys the ice ball, as will a fireball cast using the spark spell altered by a pyrapod.

## What the port has

`player_starting_magic.gd` `cast` accepts only `"spark"` and `"heal"`. Charges are 1, 3, and 5. A spark hit calls `receive_spark_level(charge)` on a body marked `spark_receiver`.

`l16_nw_traps.gd` `IceReceiver.receive_spark_level` calls `break_ice`. `break_ice` returns false when `level < 3`, otherwise marks the ice. That is any spark of charge 3 or more. No summoned imp reaches the ball.

`item_handlers.gd` group 32, handler 64, callee `0x81820`, grade UNKNOWN, likely "Pyrapod: swaps the spark spell for fire". That handler is not hosted. There is no spell-table swap.

## Decision

Keep the adapter. Do not fake a level-3 imp or a pyrapod fireball. The header comment names the missing pieces. The ledger row dated 2026-11-07, "L16 white ball (STORY-072)", records the same limit. The 2026-11-06 charge-3 row stays as history.

Unit check already printed, headless: `PASS l16_nw_traps_test: three props, blue bow only`. The earned NW-traps test still expects `receive_spark_level(1)` false and `receive_spark_level(3)` true. Its result is filled in when the chain prints it.

## Owner question

Should the white ball wait until a level-3 imp summon and a pyrapod spark swap exist, or keep breaking on any spark of charge 3 or more?
