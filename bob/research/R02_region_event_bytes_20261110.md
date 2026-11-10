# Region event bytes 0, 1, 3, 4, 5, 7, 9

Pinned `LOLG.DAT` sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`, size `0x1e2aaf`. Analysis address A is file A+`0x37000`. An object-2 dword becomes an analysis address by adding `0x59024`. The host on `grok/f10` (`fe92b67`) was not edited. F-11 stays as posted. Events 5 and 6 are still not fired. No test was run.

The walker is analysis `0xF2D2C` (file `0x129D2C`). Sixteen direct `E8` calls target it. No `E8` or `E9` in analysis `0x1F000`–`0x173000` targets it except those sixteen, and the image has no relocated pointer to `0xF2D2C`. A scan of VA `0x40000`–`0x170000` found no other `E8`.

## Grades

| Claim | Grade |
| --- | --- |
| Arm table at file `0x129D04`. Events 0 and 7 always match. Event 8 is `(byte +7) <=` the third argument. Events 1 and 9 are `(byte +7 << 2) <=` the third argument. Events 2, 3, and 4 match when byte +7 is 0, and otherwise match when the third argument is nonzero. Events 5 and 6 test ESI and do not write it | PROVEN |
| The only event-5 call leaves ESI as `byte [actor+0x3E] << 16`, so the match is that byte being nonzero | PROVEN |
| No direct call requests event 6. A kind-12 record whose byte +6 is 6 is still offered to the script caller when the requested event is 2 | PROVEN. The 15 exports contain no such record |
| Event 2 and event 4 run when the player region pointer changes. Event 3 runs on the old region and on the side list, not on the new region | PROVEN |
| Event 1 and event 9 run from player-vtable slot +`0x4C` (`0xD651C`), not from the region-change function | PROVEN |
| Event 0's only call is `0xD70BA`. Event 7's call is `0xDB2B0`, reached from three sites | PROVEN |
| The current binder's event-1 argument 0, event-4 argument omitted, and event-3 not fired on entry | Still the F-11 stand-in. This pass did not change it. LIKELY against the native arguments below |
| Who calls the event-0 thunk at `0x75CF8` | UNKNOWN. No `E8` or `E9` in the scanned range targets it |

## The compare

Arguments, after the prologue's four pushes and `sub esp, 4`: the region object is `[esp+0x18]`, the event is the low byte of `[esp+0x1C]`, and the third argument is `[esp+0x20]`. The event byte is taken by `mov edx, [esp+0x19]; sar edx, 0x18`.

The record chain is selected before the event compare. The index is the signed quotient `(region_object - dword [0x22D0C]) / 0x2C`. The chain head is `word [dword [0x22D10] + word [region+0x18] * 42 + 0xA] + dword [0xB877C]`. A zero head returns without a match. A record is considered when byte +1 is `0x0C` and word +4 equals that index. Byte +6 is then compared with the requested event.

The arm table is ten object-2 dwords at file `0x129D04`. The jump is analysis `0xF2E16`. A requested event above 9 does not write ESI and falls into the same `test esi, esi` as events 5 and 6.

| slot | raw dword | analysis | compare |
| --- | --- | --- | --- |
| 0, 7 | `0x00099D93` | `0xF2DB7` | `mov esi, 1` |
| 8 | `0x00099D9A` | `0xF2DBE` | zero-extend byte +7, `setle` against the third argument, no shift |
| 1 | `0x00099DAD` | `0xF2DD1` | zero-extend byte +7, shift left 2, `setle` against the third argument |
| 9 | `0x00099DC3` | `0xF2DE7` | same shifted `setle` as event 1 |
| 2, 3, 4 | `0x00099DD9` | `0xF2DFD` | byte +7 == 0 matches and does not read the third argument; otherwise ESI becomes the third argument |
| 5, 6 | `0x00099DFA` | `0xF2E1E` | `test esi, esi`. The prologue pushes ESI and does not clear it |

A match then calls `0x646EC` with `word [record+2] + dword [0x2B51C]`, unless the record's nested kind byte is `0x13` and `0x66AB0` returns 0. That gate is the same one F-11 already hosts as the predicate.

Two neighbors of the kind-12 compare, not hosted here. If byte +6 is 6 and the requested event is 2, the record takes that same script call even though the event bytes differ (`0xF2EB9`). If byte +1 is `0x0F` and the requested event is 2, 3, or 4, a nonzero third argument is required for 2..4 and any other requested event forces a match, then analysis `0xF2F88` calls `0xF37C8`. That callee was not entered.

## Where each event is pushed

The region object at every call below is this resolver, unless the line names another pointer. Actor in EAX. If dword `[0xB7D84]` is nonzero and the actor equals dword `[0xB7CA1]`, the pointer is dword `[0xB7CDD]`. Otherwise, when byte `[actor+0x15]` bit `0x10` is clear, the pointer is dword `[dword [actor+0xC]+4]`, or 0 when `[actor+0xC]` is 0. When that bit is set, the pointer is dword `[actor+0xC]`.

| call | event | third argument | when |
| --- | --- | --- | --- |
| `0xD383C` | 3 | `setle` of `sar16([actor+8]) <= sar16([region+0x12])` | old region `[actor+0x75]`, and only after the resolved pointer differs from it |
| `0xD38D1` | 4 | same `setle`, per list entry | each pointer in the list at `0xB7DC0` (count dword `[0xB7DBC]`) that is neither the old nor the new pointer, and only when word `[region+0x28]` bit 1 is clear. The bit is ORed after the call |
| `0xD38ED` | 2 | that same list `setle` | the same list entries, every such change, no bit test |
| `0xD38FE` | 3 | that same list `setle` | the same list entries, immediately after event 2 |
| `0xD394A` | 4 | the new region's `setle` | the new pointer, only when bit 1 of byte +`0x28` is clear. The bit is ORed before the call |
| `0xD39BB` | 2 | that new-region `setle` | the new pointer, after event 4. Bit 0 of byte +`0x28` is ORed before the call |
| `0xD607C` | 5 | 0 | inside `0xD5F94`. ESI at the walker is `byte [actor+0x3E] << 16` |
| `0xD67E0` | 9 | `sar16([actor+0x163]) - sar16([actor+8])` | inside `0xD651C`, under the height test below |
| `0xD68DC` | 1 | the same difference, the value stored at `0xD653F` before later edits of EDI | the rest of `0xD651C`, unless it returned early |
| `0xD69AA`, `0xD69B9`, `0xD69C9` | 8 | `sar16` of the second argument | `0xD6964`, player-vtable slot +`0x50` |
| `0xD70BA` | 0 | 0 | `0xD6FE4`, the flag gate below |
| `0xDB482`, `0xDB491`, `0xDB4A1` | 7 | 0 | every entry of `0xDB2B0` |

The pushes of object `0x22574` at `0x75CFE`, `0x898F7`, `0xB31F5`, and `0xB3CFD` are object-5 fixups, offset `0x22574`.

`mov edi, [ebp+0x18]` at `0xD68D9` sits between the region push and the event-1 call. It does not change the third argument. The third argument remains the difference stored at `0xD653F`.

## Event 2, 3, and 4

All six of those calls are in `0xD26B0`. Its only direct caller is `0xB31F9`, which pushes object `0x22574`. That call is in `0xB30AC`. `0xB30AC` has six direct callers: `0xA055B`, `0xA0BC0`, `0xA14B5`, `0xAEE95`, `0xAEF0C`, `0x14F61E`. The same function also calls `0xB8BA0`. That walk was not entered.

`0xD26B0` computes a new region pointer with the resolver and compares it with dword `[actor+0x75]`. Equal pointers skip every event push in this function. On a change:

- The old pointer, when nonzero, gets event 3. After the call, bit 0 of byte `[region+0x28]` is cleared and a word is stored at +`0x2A`.
- The list at `0xB7DC0` is walked even when the old pointer is null. Entries equal to the old or the new pointer are skipped. Each other entry gets event 4 once (bit 1), then event 2, then event 3.
- The new pointer is stored to `[actor+0x75]`. When it is nonzero it gets event 4 once (bit 1 ORed first), then event 2.

Event 3 does not run on the new region. Event 2 does not run on the old region. Neither runs while the pointer stays the same, so this is a change, not a standing tick. The third argument is 1 when `sar16(actor+8) <= sar16(region+0x12)`. Byte +7 == 0 matches either way. A nonzero byte +7 matches only when that compare is 1.

The binder still fires event 2, then event 4 once, on entry of the new region only, and it does not pass the `setle`. Event 3 is still not fired from `enter_region`. The list at `0xB7DC0` is still not walked. That is the F-11 stand-in. Native order on the new region is event 4, then event 2.

## Event 1 and event 9

`0xD651C` is player-vtable slot +`0x4C`. The table is object-5 `0x5C20`. Slot +`0x80` of that table is `0xD03B8`, the same slot the damage note uses for the player. File `0x1C6C90` relocates to `0xD651C`. There is no direct `E8` to `0xD651C`. Calls of the form `call [reg+0x4C]` were not each tied to this table.

The third argument for both events is `sar16([actor+0x163]) - sar16([actor+8])`, which can be negative. Polygon entry still passes 0 for event 1. With 0, byte +7 == 0 matches and byte +7 >= 1 does not. That stand-in stays LIKELY.

Event 9 is the same compare. It is skipped, and event 1 still runs, when byte `[region+0x20]` is `0xFF`, or when dword `[actor+8]` is greater than the height just computed. That height is the return of `0xF4614(region, dword [actor], dword [actor+4], 0)` when bit 2 of the low byte of word `[region+0x1C]` is set. Otherwise it is `sar16([region+0x12]) << 16`. `0xF4614`'s body was not entered. `0x67820` runs immediately before the event-9 call and was not entered.

Both events are skipped when bit 6 of byte `[actor+0x22A]` is set. That bit is cleared and the function returns. A later block can also return before event 1 when byte `[0x23331]` is 5 and the region pointer minus dword `[0x22D0C]`, divided by `0x2C`, is `0x158`, `0x304`, `0x305`, `0x306`, or `0x307`. That block calls `0xD8D48` and was not followed further.

## Event 0

Arm 0 ignores the third argument and ignores byte +7. The only push is `0xD70BA`: third argument 0, event 0, then the resolved region. It is inside `0xD6FE4`, whose only caller is `0x75D02`.

`0x75CF8` pushes its own first argument, pushes object `0x22574`, calls `0xD6FE4`, and returns 1. No `E8` or `E9` in the scanned range targets `0x75CF8`. Who calls the thunk is UNKNOWN.

Inside `0xD6FE4` the call is reached only when all of these hold. Dword `[actor+0x14D]` is nonzero. Bit 6 of byte +`0x227` is set. Bit 0 of byte +`0x229` is clear. Bit 7 of byte +`0x228` is clear. Bit 3 of the byte at `[ebp+0x15]` is clear. Byte +`0x1B4` is 0. Byte +`0x24` is 0. Byte +`0x43` is nonzero, and it is copied into byte +`0x24` before the call, so a later entry with the same byte +`0x24` returns at that compare. The call of slot +`0x48` just above the event push was not entered.

## Event 5

The arm does not write ESI. At the only call, `0xD607C`, ESI is still `byte [actor+0x3E] << 16` from `0xD5FD7`. The match is that byte being nonzero. Byte +7 is not read. The third argument is 0 and is not read. Both exported records have byte +7 == 0, so the byte does not change the result.

`0xD5F94` is player-vtable slot +`0x08` (file `0x1C6C4C`). It also has direct callers `0x898FB`, `0xB19C4`, `0xB3D07`, `0xD6120`, `0xD6144`, `0xD619F`, and `0xD63FB`. The ones checked push the actor, often object `0x22574`, and a second argument 1. The event push is inside the function, not that 1.

The push is reached only when dword `[actor+0x16D]` is nonzero, `byte [actor+0x3F] << 16` is not greater than that dword, and bit 4 of byte `[actor+0x229]` is clear. After the call that bit is set, so the push does not repeat while the bit stays set. The port still does not fire event 5.

## Event 7

Arm 7 always matches. The third argument is 0. `0xDB2B0` has no branch around the push at `0xDB453`. Its three callers:

- `0xD3360`, inside the player region function, when the signed dword `[actor+0x1D6]` is not positive. `0xDB2B0` stores 0 at that dword before the event push.
- `0xD6B55`, inside `0xD6B20`, when bit 1 of byte `[actor+0x229]` is clear, bit 0 of that byte is set, and either byte `[actor+0x1AB]` is 0 or the low byte of the second argument is 0. The rest of `0xD6B20` was not entered. It has direct callers `0x97F74`, `0x98142`, `0x9AB8B`, `0xD1E55`, `0xD1F10`, `0xD1FA9`, `0xD494D`, `0xD6F7A`, `0xD6FCE`, `0xD7EC0`, `0xD7F38`, `0xD7F97`, `0xD801F`, `0xD806F`, `0xD80BF`, `0xD810E`, `0xD8226`, `0xD8877`, `0xDAF36`, and `0xED3CB`.
- `0xDD712`, inside `0xDD5DC`, when bit 0 of byte `[ebx+0x229]` is set. The direct caller of `0xDD5DC` is `0xB5AF8`.

## Event 8

Slot 8 is the unshifted `setle`. `0xD6964` is player-vtable slot +`0x50` (file `0x1C6C94`). The third argument is the arithmetic shift of the second argument by 16. The 15 exports contain no event-8 record. The port does not fire it.

## Census

Counted once per `file_offset` across the 15 `native_scripts/*.json` files. The same record is also listed under `region_lists.records`, so a count of every `"kind": 12` node is double. K79's 478 / 918 / 3132 / 632 / 1254 / 4 / 2 / 62 is that doubled count. Unique records: 3241.

| area | 0 | 1 | 2 | 3 | 4 | 5 | 7 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1_DC |  |  | 68 | 1 | 28 |  |  |  |
| L3_DH |  | 13 | 37 |  | 35 |  |  |  |
| L4_HJ |  | 28 | 388 |  | 450 |  |  |  |
| L5_HC |  | 106 | 66 | 3 | 5 |  |  |  |
| L7_DH |  |  | 18 |  | 27 |  |  |  |
| L8_SJ |  | 8 | 109 |  | 14 |  | 1 |  |
| L9_DR |  | 43 | 130 |  | 9 |  |  |  |
| L10_DC |  |  | 107 | 7 | 1 |  |  |  |
| L12_CM |  | 6 | 60 |  | 6 |  |  |  |
| L13_RC |  |  | 50 | 14 | 7 |  |  |  |
| L14_HT |  | 16 | 127 |  | 2 | 2 |  | 31 |
| L16_CA |  |  | 101 | 24 | 3 |  |  |  |
| L17_HC |  |  | 21 |  |  |  |  |  |
| L19_BC | 239 | 239 | 246 | 239 | 2 |  |  |  |
| L20_BB |  |  | 38 | 28 | 38 |  |  |  |
| total | 239 | 459 | 1566 | 316 | 627 | 2 | 1 | 31 |

Byte +7 is 0 on every event-5, event-7, and event-9 record. Event 0 is byte +7 == 1 on 230 records and 0 on 9, all of them L19, and the arm ignores that byte. Event 1 is 0 on 111 and 1 on 348. Event 2 is 0 on 1304 and 1 on 262. Event 3 is 0 on 83 and 1 on 233. Event 4 is 0 on 185 and 1 on 442. There is no event 6 and no event 8.

The one event-7 record is L8 region 66, group 36, file `13552777`, raw `080c240042000700`. The two event-5 records are L14 region 2895 group 2450 and region 2908 group 2468. The 31 event-9 records are L14, regions 1624 through 1690 with gaps, groups 1676 through 1878, every raw ending `0900`.

L19 region 2083 is the usual doubled shape, not one record per event. Groups 1294 and 1390 each have events 2, 3, 1, and 0, and each byte +7 is 1. 115 regions have that eight-record shape. Nine have a single 2, 3, 1, 0 set.

## Host

No matcher arm and no `enter_region` call was changed. Events 0, 3, 5, 7, 8, and 9 stay unhosted. Event 3 is a leave and a side-list event, so firing it from entry would not match this decode. Event 1's native third argument is the height difference, and the binder's 0 remains the equal case only.
