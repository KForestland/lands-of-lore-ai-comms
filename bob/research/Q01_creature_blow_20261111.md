# Q01 creature blow amounts

complete false

The asked integer at context+0x1E is not one number. Every kind-1 row below has a nonzero mask and flag bit 8 clear, so the ordinary formula walks Luther's scalar and his equipment. The table is the amount stored at context+0x16, which is what the formula receives. Grade of that column: LIKELY. Difficulty byte 1, as posted in R01: that byte leaves the amount. No host.

LOLG.DAT sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`, size 1977007. Code file offset = analysis + `0x37000`. Archives are the museum `L8_SJ.MIX`, `L9_DR.MIX`, and `L10_DC.MIX`, checked against `game-actors.json`. GLOBAL.MIX sha256 `1e3e2a46340d714aaf4d583e5aff7e58dc11005bac6c694fac49c07d13e01edd`.

## The store

Creature vtable slot +`0x38` is `0xA4934`. A linear sweep from that entry reaches the strike. After `0xF2814` returns the event-table base in esi:

- `0xA5729` skips when `[esi+4]` is 0. That pointer is the kind-1 record.
- `0xA5762` skips unless actor byte +`0xB7` bit 0 is set.
- `0xA576F` skips when global byte `[0x9699E]` is 0.
- `0xA577C` loads the kind-1 record into edi. `0xA5783` zero-extends byte `[edi+2]`. `0xA5786` zero-extends actor byte +`0xA6`. `0xA578C` multiplies them. `0xA5799` is a signed `idiv` by `0x64`. The product is non-negative here, so the quotient truncates toward zero.
- A zero quotient skips the hit (`0xA579E`).
- `0xA57A6` clears `0x36` bytes at `[ebp+0x22]`. That is the context. Kind byte at `[ebp+0x36]` is 1, so context+`0x14` is 1. Context+`0x15` is `0xFF`. Context+0 is the mask word `[edi+4]`. Context+2 is the flag word `[edi+6]`. Context+4 is `[actor+0x38]`, the target. Context+8 is the actor.
- `0xA57DB` (`mov dword ptr [ebp+0x38], eax`, file `0xDC7DB`) stores the quotient at context+`0x16`.
- `0xA57E6` calls the target's vtable slot +`0x80`. For this target that slot is player receive `0xD03B8`.

Read sites of the amount, same for every row: percent byte at analysis `0xA5783` (file `0xDC783`); actor byte +`0xA6` at `0xA5786` (file `0xDC786`); quotient store `0xA57DB` (file `0xDC7DB`).

Player receive `0xD03B8` copies player byte +`0x161` to context+`0x1A` and player dword +`0x14D` to context+`0x22` and context+`0x26` (`0xD03C9` through `0xD03E1`). A mov sweep from the entry to the formula call found no write of context+`0x16`. Byte `[0x223D4]` nonzero returns 0 before the formula. The call at `0xD0488` is `0x89E7C` with object-5 `0x23348` and the context. `0x89E83` puts that object in esi and the context in edi.

## Actor byte +0xA6

Constructor `0xA2332` calls `0xA1F2C` and `0xA2337` stores the byte at actor+`0xA6`. The two arguments are actor+`0x4E` and actor+`0x4F`, zero-extended. Those bytes are the third and fourth bytes of a `0x20`-byte copy from `[definition+0x87]+8` onto actor+`0x4C` (`0xA231A`).

`0xA1F2C` (ends `0xA1F7E`): edx is actor+`0x4F`, ecx is actor+`0x4E`.

- edx 0: eax = 1, then the floor.
- ecx 0: return definition byte +`0x81`, with no floor (`0xA1F4D`, file `0xD8F4D`).
- otherwise: `(byte +0x81 * edx) / (ecx + edx)`, unsigned, then the floor (`0xA1F5A`, file `0xD8F5A`).
- Floor: if eax is less than or equal to runtime byte +`0x82`, eax becomes that byte.

File byte +`0x82` is 0 on every L8, L9, and L10 record read here. The loader writes the runtime byte. `0xA1D2A` computes `(byte +0x81 * 10) / 100` and `0xA1D3C` (file `0xD8D3C`) stores it at +`0x82`. A zero quotient is forced to 1 (`0xA1D46`). The loop stride is `0x8B` (`0xA1D4D`). The copy into the runtime record is `0x87` bytes (`0xA1C6B`), so offset `0x81` is inside it, then 12 more bytes, then a pointer is stored at runtime+`0x87` (`0xA1CAF`). Stepping into the copy helper `0x118820` was left. Runtime byte +`0x81` equaling the file byte is LIKELY. The file bytes themselves were read from the MIX.

The profile bytes are LIKELY the stat.csv rows. Entries were opened by the hash of `global\ai\<name>\stat.csv`. That format string was not re-read from LOLG.DAT this pass. Data row 2 is the value used as actor+`0x4E`. Data row 3 is actor+`0x4F`. The rows actually read are 0, 25, or 50. The caller zero-extends. The +`0x16` column uses those rows, so the column is LIKELY.

When actor byte +`0xA3` is nonzero, `0xA235F` replaces +`0xA6` with three quarters of itself, toward zero. A linear mov sweep from analysis `0xA0000` to `0xB8000` found one write of disp `0xA3`: `0xAB64D` decrements the byte when it is already nonzero. The sweep can miss a store in a desynced gap. Nothing read here shows the byte's value at spawn. The table is the value at `0xA2337`, before that cut. Grade of the cut: UNKNOWN.

## Why context+0x1E stays open

`0x89E7C` calls `0x62728` on one of three gates (`0x8A02E` through `0x8A080`):

- Bit `0x80000` of `[0x2270E]` set: scalar 0 and a null descriptor.
- Else bit 24 of `[0x2279A]` set (`shl 7` / `shr 31` at `0x8A045`): scalar 0 and a stack descriptor.
- Else: scalar = `[player+0x398] + [player+0x3A0] + [player+0x3A8]`, and the same stack descriptor.

R01: a zero scalar is forced to 1. For a positive amount and scalar 1, the kind arm's ceiling equals the amount before any mask walk. A null descriptor skips the walk. On the first gate, context+`0x1E` before the min with context+`0x22` therefore equals the +`0x16` integer. Whether bit `0x80000` is set in play was not read. The second gate still walks the descriptor. The third gate walks it with a scalar that was not read. Do not treat those three dwords as 0.

Every kind-1 mask in the table is nonzero, and no flag word has bit `0x100`. The shift-only arm in R01 does not apply to these file rows. The descriptor is built from the player item slots in `0x89E7C`. Those rows were not read. The ordinary integer at context+`0x1E` is UNKNOWN.

The stored integer is still `sar([esp+0x34] + 0xFFFF, 16)` at `0x62EC9` (file `0x99EC9`), then the min with context+`0x22`. That health dword is the player's +`0x14D`. It was not given a number. R01's heading window can change the amount before the kind arm. It is skipped when the target is object-5 `0x22574` and dword `[0x2276A]` is nonzero. That dword was not read. The creature compares `[actor+0x38]` with `0x22574` at `0xA57F5`. The formula's player object is `0x23348`.

Linking the metadata event list to the table `0xF2814` publishes is LIKELY. The event bytes below were read from the MIX and checked against the parsed row. That part is PROVEN as file contents. A state with no kind-1 row in that list does not take this store. Grade of each absence, as a fact about the metadata list: PROVEN.

The population files store `damage_base_adapter` 15, and StSquid's attack clip stores damage 15 on selector 3. The kind-1 row for StSquid is selector 2. The +`0x16` amount for that row is 30.

The question's Saar is the archive name SSAR, definitions 1 and 2. SSAR_P is a separate definition. These files do not contain a definition named Saar.

## context+0x16

`+0x16 = (A6 * event byte +2) / 100`. A6 is the constructor byte above. Grade LIKELY on every amount. Mask and flags are the file words. Event file and byte +`0x81` file are offsets in that level's MIX.

| Lv | Def | Name | Sel | Fr | A6 | Pct | +0x16 | Mask | Flags | Event file | +0x81 file |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| L8 | 0 | WILD | 4 | 7 | 25 | 100 | 25 | 0x000A | 0x0004 | 0xD30409 | 0xD2B2B0 |
| L8 | 1 | WILD | 4 | 6 | 25 | 100 | 25 | 0x000A | 0x0004 | 0xD30431 | 0xD2B343 |
| L8 | 2 | WILD2 | 4 | 4 | 25 | 50 | 12 | 0x000A | 0x0004 | 0xD30459 | 0xD2B3D6 |
| L8 | 2 | WILD2 | 4 | 10 | 25 | 50 | 12 | 0x000A | 0x0004 | 0xD30461 | 0xD2B3D6 |
| L8 | 3 | WILD | 4 | 4 | 25 | 50 | 12 | 0x000A | 0x0004 | 0xD30479 | 0xD2B469 |
| L8 | 3 | WILD | 4 | 10 | 25 | 50 | 12 | 0x000A | 0x0004 | 0xD30481 | 0xD2B469 |
| L8 | 4 | DANIEL | 4 | 6 | 35 | 100 | 35 | 0x000A | 0x0004 | 0xD30499 | 0xD2B4FC |
| L8 | 5 | SHAMAN | 4 | 6 | 20 | 100 | 20 | 0x0002 | 0x0004 | 0xD304D1 | 0xD2B58F |
| L8 | 7 | LARKHON | 2 | 6 | 40 | 100 | 40 | 0x0108 | 0x004C | 0xD307B1 | 0xD2B6B5 |
| L8 | 8 | BACL8 | 8 | 10 | 50 | 50 | 25 | 0x0104 | 0x0044 | 0xD30641 | 0xD2B748 |
| L8 | 8 | BACL8 | 9 | 9 | 50 | 100 | 50 | 0x0104 | 0x0044 | 0xD30661 | 0xD2B748 |
| L8 | 9 | LAMPLT | 8 | 7 | 2 | 100 | 2 | 0x0008 | 0x0024 | 0xD306C1 | 0xD2B7DB |
| L8 | 9 | LAMPLT | 9 | 7 | 2 | 70 | 1 | 0x0008 | 0x0024 | 0xD306D9 | 0xD2B7DB |
| L8 | 10 | LAMPLT | 8 | 7 | 5 | 100 | 5 | 0x0008 | 0x0024 | 0xD30711 | 0xD2B86E |
| L8 | 10 | LAMPLT | 9 | 7 | 5 | 70 | 3 | 0x0008 | 0x0024 | 0xD30729 | 0xD2B86E |
| L8 | 11 | LAMPLT | 8 | 7 | 8 | 100 | 8 | 0x0008 | 0x0024 | 0xD30761 | 0xD2B901 |
| L8 | 11 | LAMPLT | 9 | 7 | 8 | 70 | 5 | 0x0008 | 0x0024 | 0xD30779 | 0xD2B901 |
| L8 | 12 | LAMP_QN | 5 | 6 | 40 | 100 | 40 | 0x010A | 0x0004 | 0xD30579 | 0xD2B994 |
| L8 | 14 | DANIEL | 4 | 11 | 35 | 100 | 35 | 0x0002 | 0x000C | 0xD305F9 | 0xD2BABA |
| L9 | 0 | StSquid | 2 | 5 | 30 | 100 | 30 | 0x0008 | 0x0044 | 0x16844E1 | 0x1682510 |
| L9 | 1 | SSAR | 7 | 3 | 20 | 50 | 10 | 0x0104 | 0x0014 | 0x1684561 | 0x16825A3 |
| L9 | 1 | SSAR | 7 | 11 | 20 | 50 | 10 | 0x0102 | 0x0014 | 0x1684569 | 0x16825A3 |
| L9 | 2 | SSAR | 7 | 3 | 30 | 50 | 15 | 0x0102 | 0x0014 | 0x16844C1 | 0x1682636 |
| L9 | 2 | SSAR | 7 | 11 | 30 | 50 | 15 | 0x0102 | 0x0014 | 0x16844C9 | 0x1682636 |
| L9 | 3 | SSAR_P | 4 | 7 | 75 | 100 | 75 | 0x0102 | 0x0004 | 0x16844F9 | 0x16826C9 |
| L9 | 4 | WORM | 7 | 7 | 120 | 50 | 60 | 0x0108 | 0x0044 | 0x1684531 | 0x168275C |
| L9 | 4 | WORM | 7 | 11 | 120 | 50 | 60 | 0x0108 | 0x0044 | 0x1684539 | 0x168275C |
| L9 | 4 | WORM | 8 | 8 | 120 | 60 | 72 | 0x0108 | 0x0024 | 0x16845D9 | 0x168275C |
| L9 | 5 | BELSTAT | 1 | 7 | 65 | 100 | 65 | 0x0104 | 0x000C | 0x1684581 | 0x16827EF |
| L10 | 0 | DRACOID | 4 | 6 | 12 | 100 | 12 | 0x0104 | 0x0004 | 0xD2C577 | 0xD2B79B |
| L10 | 2 | RAT | 3 | 7 | 2 | 100 | 2 | 0x0008 | 0x0004 | 0xD2C59F | 0xD2B8C1 |

WILD definition 0, event file `0xD30409`, is the eight bytes `01 07 64 00 0a 00 04 00`. Definition byte +`0x81` at `0xD2B2B0` is 50. Stat rows 2 and 3 are 50 and 50, so A6 is 25 and the percent 100 leaves 25.

Byte +`0x81`, the runtime floor, and the two stat rows behind A6:

| Name | +81 | Floor | Stat +0x4E | Stat +0x4F | A6 |
| --- | ---: | ---: | ---: | ---: | ---: |
| WILD, WILD2 | 50 | 5 | 50 | 50 | 25 |
| LAMPLT def 9 | 20 | 2 | 25 | 0 | 2 |
| LAMPLT def 10 and 15 | 50 | 5 | 25 | 0 | 5 |
| LAMPLT def 11 | 80 | 8 | 25 | 0 | 8 |
| LAMP_QN | 80 | 8 | 50 | 50 | 40 |
| DANIEL | 70 | 7 | 50 | 50 | 35 |
| SHAMAN | 40 | 4 | 50 | 50 | 20 |
| LARKHON | 80 | 8 | 50 | 50 | 40 |
| BACL8 | 100 | 10 | 50 | 50 | 50 |
| DAWNL8 | 50 | 5 | 0 | 50 | 50 |
| StSquid | 60 | 6 | 50 | 50 | 30 |
| SSAR def 1 | 40 | 4 | 50 | 50 | 20 |
| SSAR def 2 | 60 | 6 | 50 | 50 | 30 |
| SSAR_P | 75 | 7 | 0 | 50 | 75 |
| WORM | 120 | 12 | 0 | 50 | 120 |
| BELSTAT | 130 | 13 | 50 | 50 | 65 |
| DRACOID | 120 | 12 | 25 | 0 | 12 |
| PDRACOID | 25 | 2 | 0 | 50 | 25 |
| RAT | 5 | 1 | 50 | 50 | 2 |
| SKEL | 10 | 1 | 50 | 50 | 5 |

Stat +`0x4F` of 0 takes the floor. Stat +`0x4E` of 0 returns byte +`0x81` and skips the floor. RAT's file quotient `5 * 10 / 100` is 0, so the floor is the forced 1, and `5 * 50 / 100` is 2.

## No kind-1 row

This store does not run. PROVEN for the metadata event list.

| Lv | Def | Name | Kinds in the list | +81 | +0x81 file |
| --- | ---: | --- | --- | ---: | --- |
| L8 | 6 | DANIEL | none | 70 | 0xD2B622 |
| L8 | 13 | DAWNL8 | 2, 3, 5 | 50 | 0xD2BA27 |
| L8 | 15 | LAMPLT | none | 50 | 0xD2BB4D |
| L8 | 16 | B_HUMAN | none | 0 | 0xD2BBE0 |
| L8 | 17 | B_HUMAN | none | 0 | 0xD2BC73 |
| L9 | 6 | B_HUMAN | none | 0 | 0x1682882 |
| L9 | 7 | B_HUMAN | none | 0 | 0x1682915 |
| L10 | 1 | PDRACOID | 2, 5 | 25 | 0xD2B82E |
| L10 | 3 | SKEL | none | 10 | 0xD2B954 |
| L10 | 4 | B_HUMAN | none | 0 | 0xD2B9E7 |
| L10 | 5 | B_HUMAN | none | 0 | 0xD2BA7A |

SKEL's constructor base would be 5 on the same LIKELY stat rows. The event list has no row, so there is no blow from this store. B_HUMAN has no `stat.csv` under that name. Its A6 was not computed.

Metadata file starts: L8 `0xD21458` (317 events), L9 `0x1673D89` (133 events), L10 `0xD1F0A9` (62 events).

## Other writers, not this blow

Creature slot +`0x80` is `0xA6AE0`. That receive reads context+`0x16` and does not write it. It loads definition byte +`0x83` into context+`0x1A`. The same byte is the population `reward_scale`. It is not the outgoing blow.

`0x67820` writes context+`0x16` from the target's slot +`0xE4` and sets the attacker field to 0. That is a preset on the creature.

Script callers of `0xD03B8` store a constant or a sum of the dwords at `0x236DC`, `0x236E4`, `0x236EC`, `0x236F4`, and the high byte at `0x2372C`. They do not read a creature definition.

## Left unread

The three player dwords, the stack descriptor's item rows, the spawn value of actor byte +`0xA3`, bit `0x80000` of `[0x2270E]`, bit 24 of `[0x2279A]`, and dword `[0x2276A]`. What sets actor byte +`0xB7` bit 0 is the reach question in Q06. The weapon byte added on Luther's own strike is Q02.
