# F-11 region events 1 and 4

Pinned LOLG.DAT sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`, size `0x1e2aaf`. Code VA plus `0x37000` is the file offset. An object-2 dword becomes a file offset by adding `0x90024`. Hosted on branch `grok/f10` in `~/opus_work/lol2_grok_f10`, commit `fe92b6732889f26eb2f551a4ea4fedaf77995546`. `lol2_r18` was not edited. Not pushed.

## The compare

Kind-12 selection is unchanged: word +4 is the region, byte +6 is the event. The arm table is the ten raw dwords at file `0x129D04`.

| slot | raw dword | file | compare |
| --- | --- | --- | --- |
| 0, 7 | `0x00099D93` | `0x129DB7` | always match |
| 1 | `0x00099DAD` | `0x129DD1` | zero-extend byte +7, shift left 2, `setle` against the third argument |
| 2, 3, 4 | `0x00099DD9` | `0x129DFD` | byte +7 == 0 matches and does not read the third argument; otherwise the third argument is loaded and a nonzero value matches |
| 5, 6 | `0x00099DFA` | `0x129E1E` | `test esi, esi` with ESI not written in that arm |

Grade of those four compares: PROVEN. Events 5 and 6 stay unhosted. The host does not treat a missing third argument as 0 inside the matcher.

Event 1 is file `0x129DD1`. Its only push is file `0x10D8A1` (`push edi` at `0x10D898`, then `push 1`). The function at file `0x10D51C` stores the argument at `0x10D53F`: `sar dword [ebx+0x163], 16` minus `sar dword [ebx+8], 16`. That difference can be negative. Polygon entry does not measure it. The binder passes 0, which is the equal case: byte +7 == 0 matches, and byte +7 >= 1 does not. Grade of that stand-in: LIKELY. Ledger piece 0507.

Events 2, 3, and 4 share file `0x129DFD`. Event 2 with no third argument still rejects a nonzero byte +7, so an existing event-2 sitting does not change status. Events 3 and 4 with no third argument leave a nonzero byte +7 unhosted.

Event 4's caller is the player tick. Two pushes of immediate 4 were checked. File `0x10A8CE` pushes 4 for an object that is neither the old nor the new support, then ORs 2 into byte +0x28 at file `0x10A8DB` after the call. File `0x10A944` pushes 4 for the new support after the OR at file `0x10A93D`, and the third argument there is the `setle` of the high words at +8 and +0x12. The binder does not walk the object list at `0xB7DC0`. It fires event 4 only on the new region, once, with no third argument, so only byte +7 == 0 matches. The port has no region byte +0x28. The once-latch is `_region_event4_fired` on the binder. A new scene has an empty latch, so the first entry after a load fires event 4 again. Grade of that stand-in: LIKELY. Piece 0507.

`enter_region` order is event 2, then event 4 if this binder has not fired it for that region, then event 1 with `{"arg2": 0}`. Event 3 is not fired from entry. An event kind with no records is not written to `route_log`.

## What starts

A fresh host, adapters on, event 4 with no third argument and event 1 with third argument 0. "Starts" means the compare matched. "Commits" means status `ran`. A refusal drops the whole group.

442 records stay unhosted because byte +7 is not 0 and event 4 was given no third argument. 439 of those are the L4 event-4 records with byte +7 == 1. They do not start. Event 1 records with byte +7 >= 1 are rejected when the third argument is 0 (L5 106, L19 230, L3 12). They do not start.

91 groups commit. 205 groups start and then stop. L17 has neither. No per-level allow-list: the commits below are the original byte-+7 == 0 records, and the named entry tests still pass.

### Groups that commit

| area | groups |
| --- | --- |
| L1_DC | 536, 898, 904, 910, 928, 996, 1738 |
| L3_DH | 640, 1026, 1032, 1098, 1104, 1170, 1266, 1630 |
| L4_HJ | 1778, 1930, 5310 |
| L5_HC | 110, 5454, 5648, 6718 |
| L7_DH | 48, 94, 104, 114, 192, 214, 252, 262, 300, 310, 320, 342, 352, 362, 372, 410, 420, 430, 540, 550, 604, 614, 652, 756, 982, 1066 |
| L8_SJ | 430, 436, 448, 454, 460, 466, 472, 582, 1038, 1594, 1604, 1614, 1902, 1926, 1932, 1938 |
| L9_DR | 128, 5576 |
| L10_DC | 2194 |
| L12_CM | 912, 918, 924 |
| L13_RC | 0, 2192, 2214, 2236, 2258, 2280 |
| L14_HT | 2372, 3842 |
| L16_CA | 666, 6900, 7248 |
| L19_BC | 882 |
| L20_BB | 456, 1902, 1908, 1914, 3918, 3924, 3930, 3936, 3942 |

Opcode 197 arm 10 commits only because adapter `opcode197_list_mark` is on. The host does not hold `[0x2B53C]`. It stores `byte_0x09 = 1` at `0x2b53c:<word>`. L12 regions 1950, 1951, and 1952 (groups 912, 918, 924, file `9859968`) each mark word 3642. The same arm-10 mark is the whole of L3 groups 1026, 1032, 1098, 1104, and 1170, L4 group 5310, L8 groups 430, 436, 448, 454, 460, 466, 582, 1926, 1932, and 1938, L9 groups 128 and 5576, L19 group 882, and L20 group 456.

L7's 26 groups are the event-4 door, floor, and pose groups, including region 1596 group 1066. They commit on the first entry of those regions. The bespoke `dark_halls_orb.gd` path is a different scene and does not call this binder.

L20 regions 1615–1619 groups 3918, 3924, 3930, 3936, and 3942 are opcode 21 movie commands. They commit because adapter `opcode21_movie` is on.

L4 region 3205 group 6292 is the level change (`020100001c27` at file `13029282`, after opcode 9 `09104e000300`). It starts. On a fresh host it stops because global `0x223D6` is unknown, and the group commits nothing. `setup()` sets that global to 0, so a map that enters region 3205 will commit the change. None of the named tests enter that region. The bespoke Dark Halls route does not use this binder.

L4 region 1921 group 3926 is the opcode 206 +2. It starts and stops: the nested predicate reads local 41, which is not known. Soul is not added. L3 region 1419 group 1724 starts at opcode 206 and stops because `[0x26E58 + 0]` is not known. Nothing is committed.

### Groups that start and stop

| area | groups |
| --- | --- |
| L1_DC | 6, 52, 76, 94, 148, 160, 172, 184, 208, 232, 296, 322, 348, 374, 400, 916, 1720, 1936, 1954, 1972, 1990 |
| L3_DH | 60, 94, 112, 130, 148, 166, 184, 202, 220, 238, 256, 274, 292, 310, 328, 346, 364, 382, 400, 600, 646, 680, 720, 1290, 1724 |
| L4_HJ | 0, 6, 132, 3926, 3988, 3994, 4000, 4006, 4116, 4122, 4128, 4134, 4140, 4146, 4152, 4164, 4170, 4176, 4182, 4188, 4194, 4200, 4206, 4212, 4218, 4224, 4230, 4236, 4242, 4248, 4254, 4260, 4544, 5322, 5406, 6292 |
| L5_HC | 6598 |
| L7_DH | 794 |
| L8_SJ | 734, 740, 746, 752, 758, 1896 |
| L9_DR | 3810, 3828, 3846, 3864, 3882, 3900, 3918, 3936, 3954, 3972, 3990, 4008, 4026, 4044, 4062, 4080, 4098, 4116, 4134, 4152, 4170, 4188, 4206, 4224, 4242, 4260, 4278, 4296, 4314, 4332, 4350, 4368, 4386, 4404, 4422, 4506, 5588, 5606, 5624, 5642, 5660, 5678, 5696, 6744, 6750, 6768, 6786, 6804, 6840, 6858 |
| L12_CM | 192, 210, 260, 1218, 1348, 1478, 1608, 1738, 1868 |
| L13_RC | 1062 |
| L14_HT | 2142, 2148, 2154, 2160, 2166, 2172, 2178, 2184, 2190, 2196, 2202, 2208, 2214, 2220, 2226, 2232 |
| L19_BC | 486, 530, 574, 618, 662, 706, 750, 794, 838, 1288 |
| L20_BB | 384, 396, 462, 512, 1228, 1260, 1920, 2226, 2254, 2290, 2326, 2344, 2362, 2380, 2410, 2440, 2470, 2488, 2506, 2524, 2554, 2590, 2688, 3750, 3756, 3762, 3768, 3774, 3780 |

L10, L16, and L17 have no group in this column. The stop reasons are unread locals, opcode 2 arms that are not hosted, and `0x223D6` unknown. Locals were not seeded.

## L12 gorilla village, tiger cave, lake platform

Kind-12 records in L12 are only (event 2, byte +7 0) × 60, (event 1, byte +7 0) × 6, and (event 4, byte +7 0) × 6.

The six event-1 records are the gorilla village. Regions and groups: 2952/1218, 2953/1348, 2959/1478, 2960/1608, 2965/1738, 2966/1868. Each predicate is index 11, `0003030001` (local 3 equals 1). A fresh host stops there and does not invent local 3. With local 3 set to 1 the group is admitted and stops on the first command, opcode 210 arm 10 (`d20000000a1e`). The local stays 1. Arm 10 was not hosted. Local 3 was not seeded.

Event 4 on region 1253 is groups 192, 210, and 260 (Dawn at the gulch). They start and stop because locals 0 and 1 are not known. Those locals were not seeded.

Regions 1950, 1951, and 1952 commit the arm-10 mark described above.

The tiger cave and the lake platform do not start from events 1 or 4. Props 74–78 each have one kind-9 value-16 record (groups 208, 256, 322, 376, 442, stream 1). Those groups' opcode 196 commands have byte 6 equal to `0x09`, and the host refuses a nonzero byte 6, so the lake square does not rise from this task. Group 612 and group 2706 are the other lake moves. They are not kind-12 events 1 or 4.

## Tests

`tests/native_host_region14_test.gd` passed. It checks the missing-argument refusal, the gorilla stop at opcode 210 arm 10, the negative third argument, the L4 byte-+7 == 1 refusal, the event-4 latch, and the 91 committing groups. Registry order 1205.

`tests/act2_exit_seed_test.gd`, `tests/act2_progression_levels_test.gd`, and `tests/l10_progression_test.gd` passed. Those regions have only event 2, and the level-change counts stayed the same.

`godot_check.py` reported 1813 scripts, 0 failed, before the empty-`route_log` line. The three scene tests then ran that line.

Piece 0507 is the entry stand-in. `docs/DEVIATIONS.md` was not rendered. Please run `tools/build_deviations.py build` for pieces 0359 and 0507.

Opcode 17 is not hosted. The blocked BK18 rows were not touched. No difficulty byte was decoded.
