# R118 review: load rule at bfaba78

Verdict: hold.

Head `bfaba78caff868f0ad46a5bf2078e6f4e2adb01c` on branch `load-rule` in `~/opus_work/lol2_l19cab`. That commit is the log fix on parent `bb92bad`: the re-arm row goes to `progression.load_rearm_log` and no longer into `route_log`. The rule itself is `scripts/lol2/load_region_rule.gd`. This lane did not edit the tree.

A load sets `progression.current_region` from where the body stands and does not fire the entry. `rearm_region` then matches kind-12 event-2 records, reads the predicate the way an entry does, and runs only opcodes 12, 14, 15, 196, 197 and 198 on a synthetic stream-3 key. Opcodes 199 and 204 stay on the never list. The predicate reads the host's `locals` and `locals_e58`. An empty input dict does not by itself blank those. A local or cell that was never stored is "not known", the row is `not_rearmed:unhosted`, and none of that record's re-arm commands run.

## (a) A re-arm command that is not repeat-safe in context

L4 record 3805, byte +0x1C. Five entry groups set both bits (opcode 197 arm 4) when cell 29 is 1 (`00021d0001`):

| Region | Group |
| --- | --- |
| 1654 | 3300 |
| 1655 | 3342 |
| 2453 | 4502 |
| 2465 | 4592 |
| 2467 | 4654 |

Cell 29 is stored as 1 by control 85 group 19674, control 99 group 21222, control 100 groups 21372 and 21418, and actor 64 groups 30456, 30544 and 30756. No opcode 199 in L4 stores cell 29 as 0. Slot saves keep `locals_e58`, so a load still sees cell 29 as 1.

Control 82 kind 3 value 1, group 18864, null predicate, then clears bit 0 of record 3805 (opcode 197 arm 0, `c590dd0e0000`). A later F5/F9 while the body is still in one of those five regions runs arm 4 again and puts that bit back. This was read from the L4 script tables. It was not walked.

Two nearby cases do not fail the same way. L9 region 1269 group 378 does re-apply a long list of opcode 196 floors when local 12 is 1, and prop 1214 group 9868 is what sets local 12. No second floor writer for those records turned up, so the re-arm repeats the entry rather than undoing a later floor. L14 region 777 group 1212 would set records 1632, 1636, 1645 and 1646 to 250 and record 777 to 135 when local 24 is 0, and prop 385 group 15462 later sets those same records to 110 or 140. Nothing in L14 writes local 24, so the predicate stays unhosted and the re-arm does not clobber the later floors.

## (b) Real F5/F9 in three regions Opus did not test

Place aid, then real F5 and F9. `Engine.time_scale` 1, physics 60. Creatures disabled. Private displays, Dummy audio, `LOL2_ORIGINAL_GAME_EXE` set, `original_game_verified` set. Opus had already used L10 yard 247, L14 2546, and the L19 cab.

| Case | Stand | After F9 |
| --- | --- | --- |
| Lift, L13 region 524, start act2-l13 | (-5704.25, 42.5, 178.75) | Entry did not run. Nothing enqueued. No movie. Re-arm ran group 726: kept the opcode 196, dropped the opcode 20. Floor target 5, rate 10. Body (-5704, 37, 179). |
| Hazard, L10 region 1655, start act2-l10 | (1872, -117.5, -1707) | Entry did not run. The opcode 9 enqueue in group 306 was not replayed (`nothing_to_rearm`). Group 312 re-armed its opcode 14 timer. Body stayed on the stand. |
| Movie, L16 region 233, start act3-l16 | (-3866.25, 32.5, -1134.75) | The entry asks for movie `elevator` and the body is already at the arrival (-3797, 32, 2291), region 343, while the overlay is up. Space ends it. F5 then F9: no movie, no entry, gap 0. Region 343 has no entry group, so the re-arm row is empty. The arrival is the saved position. |

Log: `/tmp/r118_out/input.log` for the lift and the hazard, `/tmp/r118_out/movie.log` for the movie. The first movie attempt failed F9 because the overlay had the tree paused; the follow-up is the one in the table.

## (c) Mid-move and mid-movie

The lift save is the mid-move save. The body started at y 42.5 on floor 10 and the entry's opcode 196 had already set the target to 5. After F9 the target was still 5 and the body was at y 37. The opcode 20 timer in that entry was not re-armed. Event 3 group 754 would set the same record to 10, and the port never fires region event 3, so that target is not part of play and the load does not owe it.

F5 during the elevator movie writes no slot. `museum_interface.gd` returns while the tree is paused, and `act2_save.gd` refuses a save or a load with the overlay up. The overlay takes Escape and Space only. After Space, the save in section (b) keeps the arrival and does not play the movie again.

## (d) The two not_rearmed:unhosted legacy regions

Opus's load of the four legacy area saves (log under the oldsaves scratchpad, same rule) landed here:

| Save | Where the load stood | Re-arm |
| --- | --- | --- |
| L10 | region 3589, body (2951, 32, -2990) | Group 526 `not_rearmed:unhosted`. Group 562 `nothing_to_rearm`. |
| L19 | region 698, body (3, 20, -1095) | Group 838 `not_rearmed:unhosted`. |
| Darker Jungle (L8) | region 2359 | No entry record. |
| Dragon (L9) | region 1244 | No entry record. |

A legacy load passes an empty `native_bank`, so locals are unknown.

L19 group 838 is the loss. Its predicate is local 1 == 0. The commands are an opcode 15 effect (form 0x36), three opcode 14 kind-2 timers, and an opcode 198 store of local 0 = 1. None of them run. The effect and the three timers are the commands this rule exists to restore, and this room does not get them.

L10 group 526 is predicate local 1 == 1. The only re-arm command is opcode 198, local 0 = 1. The four opcode 9 enqueues in that group are on the never list, so they would not run even if the predicate matched. The player loses the local store. Group 562 is opcode 2, which is not re-armed. L8 and L9 lose nothing from the rule, because those stands have no entry.

## Opcodes 199 and 204

They stay on the never list. Both are absolute writes. A slot save already carries the cells and the region-record bytes in the native bank. Re-firing them would fight that bank. F2 checkpoints and legacy loads do not carry them. That gap belongs to the save, which is the note already on the board.

## Why this is a hold

The three new F5/F9 regions do not replay an entry, an enqueue, or a movie, and the lift keeps its floor target through a save taken while the floor is moving. The hold is the other two checks. A load in the five L4 regions puts back a bit a later control cleared, for as long as cell 29 stays 1. A legacy load in L19 region 698 drops the effect and the three timers the re-arm was added to restore. This lane does not apply the change.
