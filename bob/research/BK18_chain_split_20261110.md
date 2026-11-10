# BK18 split of the BK17 39 (2026-11-10)

The list is `grok_research/BK17_main_chain_stops_20261110.md`. Fire lines are `grok_research/BK17_chain_fire_20261110.txt` (`BK17_DONE stops=39 ran=75`). Godot stands stay those coordinates. This note does not retype them.

Writers were read from `L16_CA.json`, `L19_BC.json`, and `L20_BB.json` in the BK17 worktree. Predicate bytes are the five-byte table entries. Opcode 198 stores byte 5 at local `[0x26E54 + byte 4]`. Opcode 207 adds signed byte 5 to that slot. Opcode 199 stores into `[0x26E58 + byte 4]`. Opcode 16 stores byte 4 at the target's `+0x25`. L19 has no opcode 199 command. L20's two are group 316 (`e58[1] = 20`) and group 7704 (`e58[52] = 1`).

The host evaluates every matching record's predicate before any accepted group's commands run. A sibling in the same `fire_event` still sees the pre-command state. A later chain row is a later `fire_event`, so an earlier row's commands have committed.

## How a row was classed

Unearned: the predicate asks for a value an earlier player action writes, and this fire had not committed that write. A record that wants the value its own click stores is the next click. A rejected `left 0` on a counter a playthrough raises is this class. These rows are not host bugs and are not seeded.

Real: the entry predicate is the fresh state, or it has already passed, and the group still stops. That is an undecoded command, or a read of a slot the fresh game would already hold and this host will not read.

Deferred: real host gaps the task says to leave unless a later row needs their stores. None does.

Counts: 2 deferred, 14 real, 23 unearned.

## Deferred (leave alone)

| # | story | group | why it stays | why the chain does not need it |
| --- | --- | --- | --- | --- |
| 1 | 068 | L16 40510 prop 626 kind 9 value 32 | Predicate 206 (`+0x25 == 0`) passed. Opcode 9 arm `0x10` (`090372021000`) is not decoded. | A refusal rolls the group back, so the later opcode 16 store of `+0x25 = 1` does not commit. No later stop row reads prop 626. |
| 2 | 070 | L16 37776 prop 602 kind 10 value 0 | Kind 10 matcher is not implemented. No predicate. | Sibling 37758 (kind 6 value 20) ran. The unrun commands are opcode 2 arm `0x0C`, opcode 9 on control 7, travels of 92/94/93, and opcode 9 arm 2 on prop 602. No later stop predicate reads those targets' fields. |

## Real stops, chain order (the fix queue)

| # | story | group | entry | stop |
| --- | --- | --- | --- | --- |
| 3 | 078 | L16 6384 prop 241 | pred 206 passed | opcode 7 index 10, `0703f1000a08`. Log: `prop slot +0xB4 index 10 is not decoded`. |
| 4 | 081 | L19 2778 prop 222 | pred 34 = `(local 9 == 0) both (e58[13] operator 3 literal 1)` | local 9 is not known. Operator 3 is not decoded. |
| 5 | 081 | L19 2814 prop 222 | pred 33 = `(local 9 == 0) both (e58[13] == 0)` | local 9 is not known. No L19 opcode 199 writes `e58[13]`. |
| 9 | 083 | L19 3762 movable 50 | pred 4 `local 2 == 0` | local 2 is not known. First throw. |
| 11 | 083 | L19 5652 movable 71 | pred 4 `local 2 == 0` | same |
| 13 | 083 | L19 5744 movable 72 | pred 4 `local 2 == 0` | same |
| 28 | 087 | L20 7704 prop 242 | pred 206 passed | opcode 2 arm `0x23`, `020100002300`. Index 52 is not written. |
| 30 | 088 | L20 9768 movable 57 | L20 pred 10 `0003030000`, local 3 == 0 | local 3 is not known. Fresh read. |
| 31 | 088 | L20 9800 movable 58 | same | same |
| 32 | 088 | L20 9832 movable 59 | same | same |
| 33 | 088 | L20 9864 movable 60 | same | same |
| 34 | 088 | L20 9896 movable 61 | same | same |
| 35 | 091 | L20 12052 actor 46 kind 6 value 20 | no predicate | opcode 13 index 4, `0d022e00040f0000` |
| 36 | 092 | L20 29496 actor 75 kind 5 value 0 | no predicate | opcode 13 index 4, `0d024b00040c0000`. Kind 6 value 0 group 29526 ran, so this record was reached. |

L19 local names, from the decoded cstrings: 0 `Sewer_block_1`, 2 `Drop_down_sewer_door`, 4 `Lab_elevator_two`, 9 `Level_entered`, 11 `Imp_summoner`. L20 local 3 is that map's own array. It is not L19's `Lab_elevator`.

What blocks a seed or a guessed adapter:

- Group 6384's next command after index 10 is opcode 7 index 2 (`0703f1000200`), which calls `0xF2814`, then index 0 (`0703f1000000`), which ORs `0x05` into `+0x36`. Hosting index 10 alone still rolls the group back at index 2. G67 proved `0xF282E` stores the requested index at `+0x31`, or 0 when the index is above `+0x32`. G48's constructor note stores template byte `0x30 & 0x0F` at `+0x37`. Those notes are not yet checked against this prop, so the row stays open.
- Groups 2778 and 2814 want local 9 == 0 on the first click. They themselves are the only opcode 198 writers, and they store 1. A proven zero of local 9 still leaves 2778 on operator 3 and 2814 on `e58[13]`, which no L19 group writes. Do not seed local 9.
- Locals 2 and 3. The only writers of L19 local 2 are the six toggle groups: the `== 0` groups store 1 (`3762`, `5652`, `5744`) and the `== 1` groups store 0. The only writers of L20 local 3 are prop 197 group 6406 (store 1, predicate local 3 == 0) and group 6476 (store 0, predicate local 3 == 1). The probe did not fire prop 197, and the switch predicate wants 0, so this is the fresh read, not a raised value. Opcode 207's "unread slot starts at 0" did not re-enter the callee. A global unread-as-0 would move Dark Halls region 83 predicate 19, which nests to local 6, from unhosted to rejected. Do not seed local 2 or local 3 until a constructor or level-load zero is proven.
- Group 7704. Arms `0x23`, `0x25`, and `0x35` have no host arm. The opcode 199 that would store `e58[52] = 1` is later in the same group and does not run. Do not seed index 52.
- Opcode 13 index 4. G97 step4: actor slot `+0xAC` index 10 (command byte 0 == 13) indexes a further table, and those arm bodies stay UNKNOWN. Do not invent index 4.

BK14, BK15, and BK16 do not host these commands. BK14's actor 46 caller `0x0B` is group 12398, which already ran.

## Unearned (23)

The probe fired every matching record of one event in one call. The value a real playthrough raises was still the pre-command value, or the raising event was a different kind or value and was never fired.

| # | group | predicate | who raises it | what this fire saw |
| --- | --- | --- | --- | --- |
| 6 | 2850 | local 9 == 1 | 2778 and 2814 store 1, and they did not run | local 9 not known. Second state of the same click. |
| 7 | 5930 | local 0 == 2 | 5906, 6578, and 7250 each add 1, no predicate, and each ran | same fire as the first add, so the slot was still unknown |
| 8 | 6602 | local 0 == 2 | same adds | left 1, the add 5906 had already committed. 6578's add had not. |
| 10 | 3808 | local 2 == 1 | 3762 stores 1 | same fire as 3762, which did not run |
| 12 | 5698 | local 2 == 1 | 5652 stores 1 | same fire |
| 14 | 5790 | local 2 == 1 | 5744 stores 1 | same fire |
| 15 | 3998 | `+0x25 == 1` | 3854 (pred 206) ran in that fire and its opcode 16 stores 1 | left 0 |
| 16 | 66 | local 11 == 10 | opcode 207 on props 67–70 kind 6 value 6: groups 432 (+4), 664 (+2), 896 (+1), 1128 (+3). The probe fired value 21. | local 11 not known. Group 66 itself stores 0, after the predicate. |
| 17 | 1230 | `+0x25 == 1` | prop 77 group 1166, kind 6 value 20, no predicate, opcode 16 `10034e000100` onto prop 78. Not fired. | left 0 |
| 18 | 1250 | `+0x25 == 2` | 1230 stores 2, after the missing 1 | left 0 |
| 19 | 1500 | `+0x25 == 5` | later step on the same counter | left 0 |
| 20 | 1544 | `+0x25 == 3` | 1250 stores 3 | left 0 |
| 21 | 1566 | `+0x25 == 20` | groups 1324 and 1432 store 20 | left 0 |
| 22 | 1672 | `+0x25 == 25` | groups 1604 and 1638 store 25 | left 0. The prop 78 record is the one that fired. Region 2086 also points at this group with predicate local 1 == 0; that record was not this stop. |
| 23 | 8150 | `+0x25 == 1` | prop 79 group 1698, kind 6 value 20, opcode 16 `100227000100` onto actor 39. Not fired. | left 0 |
| 24 | 8170 | `+0x25 == 2` | 8150 stores 2 | left 0 |
| 25 | 8290 | `+0x25 == 5` | 8226 stores 5 | left 0 |
| 26 | 1964 | local 4 == 1 | sibling 1762 (local 4 == 0) ran in that fire and stores 1 | left 0. Second trip. Group 3854, earlier, also stores local 4 = 0, so 1762's entry predicate still passes. |
| 27 | 15790 | `e58[52] == 1` | selector 1 seeds 0. Sibling 15784 (`e58[52] == 0`) ran. | left 0, right 1. Correct on selector 1. L20 group 7704 writes L20's array, not this one. |
| 29 | 770 | `+0x25 == 13` | prop 87 kind 2 groups 316 through 744 step `+0x25` from 1 to 13. The probe fired kind 6 value 20. | left 0 |
| 37 | 12152 | `+0x25 == 2` | group 12078, kind 6 value 3, pred 206, stores 1. Not fired. Group 12116 (kind 8 value 254) stores 2. | left 0. Value 11 group 12398 ran and does not store 2. |
| 38 | 12196 | `+0x25 == 3` | 12152 stores 3 | left 0 |
| 39 | 12240 | `+0x25 == 4` | 12196 stores 4 | left 0 |

The sewer switches show the difference. Movable 76 group 7274 has the same predicate as 5930 and 6602 (`0003000002`, local 0 == 2). It ran. By that fire, 5906 and 6578 had each committed one add, so the left side was already 2. 5930 and 6602 failed only because their own fires had not earned 2 yet.

## Fix order

First real row is group 6384. Native data before any adapter. Opcode 9 arm `0x10` and group 37776 stay deferred. No local, no index 52, and no `+0x25` counter is seeded to hide an unearned row.
