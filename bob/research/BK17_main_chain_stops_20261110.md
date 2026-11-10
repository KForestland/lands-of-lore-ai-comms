# BK17 ranked list (2026-11-10) — L16, L17, L19, L20 main chain

The two groups named in the first look (L19 5836, L20 7704) were not this list. Fire status is from a host run with adapters left on. Chain order is AX01, then STORY-067 through STORY-093. Each map boots from `scenes/lol2/maps/L{16_CA,17_HC,19_BC,20_BB}.tscn`, selector 1, `adapter_exit_seeds` true, `change_scene_enabled` false. L16 seeds none. L17 seeds local 0 = 10 (`L17_to_L16_prepare_pred0`). L19 seeds `0x26E58` index 52 = 0 (`L19_to_L20_pred204_205`). L20 seeds none.

Coordinates below are Godot x,z: stored placement word 0, and the negation of stored word 2. Movable 74 is stored (−323, 2124) and the switch stand is `Vector3(-323, 30, -2124)`. Region 2369 uses the AE12 mark (3321, 875) with that same negation, so the stand point is (3321, −875).

## Two fires

First fire, before the host edits: `BK17_DONE stops=60 ran=54`. Log: the session terminal `call-a550c60b-356e-4d32-a944-25ecedfd8335-110.log`.

After the three host edits, the same probe printed `BK17_DONE stops=39 ran=75`. Log lines: `grok_research/BK17_chain_fire_20261110.txt` (copied from `/tmp/bk17_chain2.log`, exit 0). Twenty-one groups left the stop list. No new group entered it.

Those twenty-one now run:

- STORY-069 props 489–492, groups 20286, 20344, 20402, 20460. Predicate 206 is true because a placed prop starts at +0x25 = 0.
- STORY-084 movable 73, group 5836. Opcode 7 index 0 runs on adapter `opcode7_movable_records`.
- STORY-085 props 67–70, groups 224, 276, 328, 380, 456, 508, 560, 612, 688, 740, 792, 844, 920, 972, 1024, 1076. Same +0x25 seed.

## What the host change is

Ledger pieces 0502, 0503, 0504. Registry order 1202 is `bk17_host_stops_test`. The chain probe stays unregistered.

- 0502 Correction. Prop constructor `0xF2064` calls `0xAE990`, which stores 0 at +0x25. Actors, movables, and controls already had that store. The copy of placement byte +0x1E into +0x26 is not seeded on props.
- 0503 Correction. Predicate type 4 calls `0x66AB0` again. Left type 4 pushes entry byte 2. Right type 4 pushes entry byte 4. A nested gap stays unhosted. The nest stops at depth 8.
- 0504 Adapter `opcode7_movable_records`. A movable uses the same slot `0x5D5F8` as a control. Index 0 ORs bit 1 into the staged records' byte +3. Index 7 ORs bit 2. Indexes 1–6, 8, and 9 stay unhosted. An index above 9 returns with no store.

Group 40510 now passes predicate 206 and stops on opcode 9 arm 0x10. Group 6384 now passes predicate 206 and stops on opcode 7 index 10. Group 7704 now passes predicate 206 and stops on opcode 2 byte 4 = 35 (`020100002300`). It does not write index 52. Group 770 (predicate 219, +0x25 == 13) is rejected while +0x25 is 0. Groups 2778 and 2814 no longer stop on "right type 4". They stop because local 9 is not known.

Named runs, not the wide selector: `native_script_host_test`, `l8_activation_test`, `native_host_op199_test`, `bk17_host_stops_test`, `dark_halls_doors_native_test`, `act2_exit_blockers_test`, `deviations_ledger_test`, `test_registry_test`. `godot_check` on the five changed scripts: 0 failed. Audio driver Dummy. One Godot at a time. MemAvailable stayed above 17 GiB.

## Ranked remainder (39)

Story order. Status is the second fire. Kimi traces the first three. The rest were not adapted: a false predicate stays false, and an unknown local or an undecoded arm was not invented.

| # | story | where | group | status | why |
| --- | --- | --- | --- | --- | --- |
| 1 | 068 | L16 prop 626 (−4111, 15457) region 4900 | 40510 | unhosted | opcode 9 arm 0x10 is not decoded |
| 2 | 070 | L16 prop 602 (2289, −648) region 6098 | 37776 | unhosted | kind 10 matcher was not entered |
| 3 | 078 | L16 prop 241 (1625, 4417) region 9476 | 6384 | unhosted | opcode 7 prop index 10; +0x37 is not held |
| 4 | 081 | L19 prop 222 (120, 525) region 687 | 2778 | unhosted | predicate 34 nests to local 9, not known |
| 5 | 081 | L19 prop 222 (120, 525) region 687 | 2814 | unhosted | predicate 33 nests to local 9, not known |
| 6 | 081 | L19 prop 222 (120, 525) region 687 | 2850 | unhosted | predicate 30 reads local 9, not known |
| 7 | 082 | L19 movable 74 (−323, −2124) region 36 | 5930 | unhosted | predicate 0 reads local 0, not known |
| 8 | 082 | L19 movable 75 (−304, −2124) region 34 | 6602 | rejected | predicate 0 false (left 1, right 2) |
| 9 | 083 | L19 movable 50 (1535, −3282) region 213 | 3762 | unhosted | predicate 4 reads local 2, not known |
| 10 | 083 | L19 movable 50 (1535, −3282) region 213 | 3808 | unhosted | predicate 3 reads local 2, not known |
| 11 | 083 | L19 movable 71 (1622, −3609) region 609 | 5652 | unhosted | predicate 4 reads local 2, not known |
| 12 | 083 | L19 movable 71 (1622, −3609) region 609 | 5698 | unhosted | predicate 3 reads local 2, not known |
| 13 | 083 | L19 movable 72 (1629, −3246) region 606 | 5744 | unhosted | predicate 4 reads local 2, not known |
| 14 | 083 | L19 movable 72 (1629, −3246) region 606 | 5790 | unhosted | predicate 3 reads local 2, not known |
| 15 | 084 | L19 movable 51 (2550, −854) region 1931 | 3998 | rejected | predicate 207 false (left 0, right 1) |
| 16 | 085 | L19 prop 65 (1306, −1444) region 1706 | 66 | unhosted | predicate 39 reads local 11, not known |
| 17 | 086 | L19 prop 78 (2802, −882) region 1461 | 1230 | rejected | predicate 207 false (left 0, right 1) |
| 18 | 086 | L19 prop 78 (2802, −882) region 1461 | 1250 | rejected | predicate 208 false (left 0, right 2) |
| 19 | 086 | L19 prop 78 (2802, −882) region 1461 | 1500 | rejected | predicate 211 false (left 0, right 5) |
| 20 | 086 | L19 prop 78 (2802, −882) region 1461 | 1544 | rejected | predicate 209 false (left 0, right 3) |
| 21 | 086 | L19 prop 78 (2802, −882) region 1461 | 1566 | rejected | predicate 226 false (left 0, right 20) |
| 22 | 086 | L19 prop 78 (2802, −882) region 1461 | 1672 | rejected | predicate 231 false (left 0, right 25) |
| 23 | 086 | L19 actor 39 (1939, −891) region 2182 | 8150 | rejected | predicate 207 false (left 0, right 1) |
| 24 | 086 | L19 actor 39 (1939, −891) region 2182 | 8170 | rejected | predicate 208 false (left 0, right 2) |
| 25 | 086 | L19 actor 39 (1939, −891) region 2182 | 8290 | rejected | predicate 211 false (left 0, right 5) |
| 26 | 087 | L19 prop 98 (2616, −774) region 1933 | 1964 | rejected | predicate 8 false (left 0, right 1) |
| 27 | 087 | L19 region 2369 (3321, −875) region 2369 | 15790 | rejected | predicate 205 false (left 0, right 1). Index 52 stays the arrival seed 0. |
| 28 | 087 | L20 prop 242 (−1160, −4258) region 262 | 7704 | unhosted | opcode 2 byte 4 = 35, arm 0x23. Index 52 is not written. |
| 29 | 087 | L20 prop 87 (−1496, −4268) region 291 | 770 | rejected | predicate 219 false (left 0, right 13). +0x25 stays 0. |
| 30 | 088 | L20 movable 57 (−3340, −4299) region 780 | 9768 | unhosted | predicate 10 reads local 3, not known |
| 31 | 088 | L20 movable 58 (−3404, −4299) region 782 | 9800 | unhosted | predicate 10 reads local 3, not known |
| 32 | 088 | L20 movable 59 (−3482, −4299) region 784 | 9832 | unhosted | predicate 10 reads local 3, not known |
| 33 | 088 | L20 movable 60 (−3559, −4299) region 788 | 9864 | unhosted | predicate 10 reads local 3, not known |
| 34 | 088 | L20 movable 61 (−3636, −4299) region 788 | 9896 | unhosted | predicate 10 reads local 3, not known |
| 35 | 091 | L20 actor 46 (−6921, −4828) region 1272 | 12052 | unhosted | opcode 13 actor slot +0xAC index 4 was not entered |
| 36 | 092 | L20 actor 75 (−1238, −3207) region 177 | 29496 | unhosted | opcode 13 actor slot +0xAC index 4 was not entered |
| 37 | 093 | L20 actor 46 (−6921, −4828) region 1272 | 12152 | rejected | predicate 208 false (left 0, right 2) |
| 38 | 093 | L20 actor 46 (−6921, −4828) region 1272 | 12196 | rejected | predicate 209 false (left 0, right 3) |
| 39 | 093 | L20 actor 46 (−6921, −4828) region 1272 | 12240 | rejected | predicate 210 false (left 0, right 4) |

L17 had no stop on either fire. STORY-079 region 1312 group 1632 ran. STORY-080 region 1293 group 1566 ran.

## Gaps (no group to fire)

- STORY-068 prop 210: no native event. The dry-fountain ball. The fountain that did fire is prop 626.
- STORY-073: ivory chips are placed rows with event 0.
- STORY-075: pedestals are event 0.
- STORY-076: no placed box, disk, or yellow figure.
- STORY-080: `hw01.vqa` is not a movie-MIX entry. Region 1293 still fired and ran.

## Left undecoded on purpose

Opcode 9 arm 0x10 has no host arm. The kind 10 matcher needs walker arguments this chain fire does not supply, so group 37776 was not forced to match. Opcode 7 on a prop, index 10, is the store `(+0x37 & 0xF0) | byte 5`, and +0x37 is not known, so group 6384 stays unhosted. Opcode 2 arms 0x23, 0x25, and 0x35 have no arm. Opcode 13 index 4 was not entered. Locals 0, 2, 3, 9, and 11 were not seeded. Index 52 was not seeded to hide group 7704. Predicate 219 was not seeded to 13.
