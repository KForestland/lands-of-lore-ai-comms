# World state in saves, 12 November 2026

Read-only. No build. Pinned `LOLG.DAT` sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`, size `0x1e2aaf`. A code address A is file A+`0x37000`. Object-5 addresses are the fixup offsets (runtime base `0x180000`). Grades are PROVEN, LIKELY, or UNKNOWN.

The playtest F9 path is `lol2_play_r19pre` `scripts/lol2/act2_save.gd` `save_host`, loaded by `act2_map.gd` `apply_save`. The slot file is Sol's tree `lol2_sol_autosave` `scripts/lol2/game_save.gd`. The playtest tree has no `game_save.gd`.

## Summary

F9 puts Luther back where he stood. It leaves a moved floor where the move left it. L19 floors 40 and 61 are that case. The original per-level file keeps the floor height inside the region record, and it keeps a moved lid or door inside the movable's own object. Our F9 packet has the body pose, the inventory, the quest dictionary, and the region number the body was standing on. It has no floor height for regions 40 and 61.

The original writes one file per level. The writer is `0xE7F68`. It reads the level's `.img` (the suffix at object-5 `0x3153`) and writes the level's `.lsv` (the suffix at object-5 `0x3158`). The level index is the high byte of the caller's argument (`0xE7F8A`). For the sections that hold movables, floors, controls, and script locals, each stored byte is the live byte mixed with the same byte from that `.img`. A byte that has not changed mixes to zero. A later step can rewrite a pointer-shaped dword in that mixture. The position, the state, the floor height, and the life byte are not the addresses that step is given.

The slot then copies twenty of those per-level `.lsv` files (levels 1 through `0x14`, suffix object-5 `0x3149`) into the named save. The function that makes the just-written `.lsv` show up under that second suffix was not entered. LIKELY they are the same blob. UNKNOWN which function links them.

A dead creature stays in the actor element. The death function stores 0 in the health word and `0x0F` in byte `+0xA8`. Both sit inside the saved stride, and the pool count is left as it was. The 68 section arms were listed in full. None is sized as the 37-byte placement table, so the byte that remembers a taken item stays UNKNOWN.

## What the per-level file stores

The section switch is `0xE8914`. Index `0` through `0x43` are 68 sections. Each arm returns a pointer, a size, a second value, and flags. Flag bit 1 (value 2) selects the mix with the `.img`. Flag bit 2 (value 4) sends that buffer through `0xEB6A0`, which writes a counted series of chunks. With neither bit set, `0x118864` writes the live pointer. PROVEN from `0xE8192`, `0xE820E`, `0xE8283`, `0xE82AE`, and `0xE82D0`.

The element size of a class pool is `[header+0xC]`, written by `0x5F724`. The pool setup at `0x9D229` pushes that size. PROVEN.

| Asked item | Where | Grade |
| --- | --- | --- |
| Movable position dword `+0x48` and state byte `+0x55` | Section 22. Header at object-5 `0x2B500`. Element base `[header]`, count `[header+8]`, stride `[header+0xC]`. The setup pushes `0x58` (`0x9D33C`), and `0x58` divides by the alignment 4, so the stride is `0x58`. Both fields sit inside it. Flags 7. | PROVEN |
| Region floor height | Section 12. Pointer at object-5 `0x22D0C` (unnamed). Count at `0x22D2C`. Size is count times 44. Second value `0x2C`. Flags 7. The height word is record `+0x12` (R02). `0x12` is inside the 44 bytes. | PROVEN the record is the section. LIKELY the height word is still in the written mixture. |
| Control life, object byte `+0x26` | Section 19. Controls are class `0x10`, header at object-5 `0x273E0`. The setup pushes `0x40` (`0x9D278`), so the stride is `0x40`. `+0x26` is inside it. `0xAE990` copies placement byte `0x1E` to `+0x26`. `0xB71EC` adds a delta to that byte and stores it back, clamped to 0..255. Flags 7. | PROVEN |
| Script locals | Section 24. Pointer is the dword at object-5 `0x26E54`. Size is the dword at `0x26E5C`. Second value 1. Flags 7. Opcode 198 at `0x64887` stores command byte 5 at that buffer plus command byte 4. | PROVEN |
| Script flags, the other array | Global section 1, in the slot header, outside the per-level file. Pointer is the dword at object-5 `0x26E58`. Size is the dword at `0x26E60`. Second value 1. Flags 7. Switch `0xE867C`, arm at `0xE86BD`. Opcode 199 writes this array (prior note). | PROVEN this section copies that buffer. |
| Timers | Kind-2 list: section 61 is the `0xC` bytes at object-5 `0xB7DA4` (flags 3). Section 62 is the buffer that dword points at, length `[0xB7DA8]<<2`, flags 1, so a direct copy. Sections 63 and 64 are the same pair at `0xB7DB0` / `[0xB7DB4]`. The count used by older notes at `0xB7DAC` is a different cell. Clock bytes: section 67 copies object-5 `0x22C40` through `0x22C91` (`0x51` bytes, flags 3). The clock word `0x22C58` and dword `0x22C5A` sit in that range (Q12). | PROVEN the bytes are copied. LIKELY the `0xB7DA4` pair is the kind-2 timer list, from the earlier list note. |
| Dead creatures | Section 21, the same class-2 element. Header at object-5 `0x9696C`, stride `0xBC`. Death `0xA7544` stores word `+0x88` as 0 (`0xA77EB`) and byte `+0xA8` as `0x0F` (`0xA77DF`). It also stores byte `+0xA9` as `0x0F`, byte `+0xAA` as `0x0F`, and byte `+0xAB` as `0x10`, and it clears bit `0x40` of byte `+0x15`. None of those stores changes the pool count. | PROVEN the stores. The element remains the saved record. |
| Taken items | All 68 arms of `0xE8914` were read. None sizes its buffer as count times 37. The level geometry file, as the port readers decode it, stores placements at header field `0x20` with count field `0x6C` and stride 37. That table is not one of the 68 sections. | UNKNOWN which saved byte records a take. |

`0xA7A74` is the health setter. When byte `+0xA8` is already `0x0F` it stores word `+0x88` as 0 and returns. When the amount is 0, definition byte `+0x3C` has bit `0x10` clear, and actor byte `+0xB5` has bit 0 clear, it calls `0xA7544` instead of the normal health store. A set bit `0x10` forces the amount to 1 and takes the normal store. A set bit 0 of `+0xB5` returns without a store. If `0xA7544` finds `+0xA8` already `0x0F`, it returns at `0xA6359` without writing. PROVEN from those arms.

The follow-up before the write is `0xE96EC`, switched by section index. The short arm `0xE97AC` stores nothing. Sections 24 and 67 use it. Section 22 (movables) arm `0xE9C59` calls `0xEB2C8` at element offsets `+0xC`, `+0x10`, `+0x2C`, and `+0x30`. Section 19 (controls) arm `0xE9AAE` calls it at the same four offsets. `+0x48`, `+0x55`, and `+0x26` are not among them. `0xEB2C8` rewrites one dword when that dword falls inside one of 26 ranges, and returns without a store when it does not. Section 12's arm `0xE9923` calls the helper once per stride step. The helper's source pointer on that arm was not reduced, so the height word staying intact is LIKELY.

## What our saves store

F9, `act2_save.gd` `save_host` lines 52–66, writes one JSON packet:

- `player.position`, `yaw`, `pitch`
- `player.region` only when region collision is on and the tracked region is at least 0. That is the region number, for the L17 throat overlap. The comment on lines 61–62 says so. It is not a floor height.
- `inventory`
- `quests`, the whole quest dictionary. That includes `act2_creatures_*` for the ten Act 2/3 areas, `act2_items` when present, `act2_struck` after a strike has stored it, and `l19_dawn_elevator` for cab regions 1935–1943.
- `atlas_explored`

`apply_save` (lines 429–455) restores the pose, the tracked region while the body is still inside it, the creature populations, `restore_struck`, the item catalog, and the named nodes (fences, L12 pieces, L13 pieces, the Dawn elevator). `restore_struck` reads `quests.act2_struck` and puts the remaining life back on kind-9 movables and controls. It does not write `progression.regions`.

The Dawn elevator key stores local 4 and the heights of regions 1935–1943 (`l19_dawn_elevator.gd`). Regions 40 and 61 are outside that list. Their heights live in `progression.regions` and in the floor-motion table. `apply_save` does not write either. A reload therefore shows the height the level was built with. Sol's report matches that: the pose returns, and floors 40 and 61 come back at that built height.

Sol's `game_save.gd` `make_document` (lines 112–119) wraps that same area packet (`area_snapshot` calls `snapshot_host`, the same fields as F9) and adds `native_bank`. `game_session.gd` `snapshot_bank` (lines 40–47) stores, for the current area, the four VM fields plus `struck_durability`. The four fields are `state`, `locals`, `locals_e58`, and `record_state` (`native_script_host.gd` lines 333 and 369). Load calls `replace_bank` (`game_save.gd` line 226) and, on area entry, `native.restore` (`act2_progression.gd` lines 218–221). `restore` copies the dictionaries and does not emit the field signal (lines 386–387).

| Asked item | F9 `save_host` | Sol slot `native_bank` |
| --- | --- | --- |
| Movable `+0x48` / `+0x55` | Absent. The host has no field for either. | Absent. `state` holds staged fields such as `travel_0x50` and `byte_0x25`. The opcode-1 note in the host says the `+0x48` / `+0x55` continuation is not staged. |
| Region floor height | Absent for 40/61. Cab regions 1935–1943 are the elevator quest key. `player.region` is the region number. | `state` can hold `floor_target` and `floor_rate` on key `0x22d0c:N` after opcode 196 has run. `restore` puts that dictionary back and does not call `_start_floor`, so the collision height in `progression.regions` stays the source height. |
| Control life `+0x26` | `quests.act2_struck` keeps the remaining life of kind-9 movables and controls after a strike has written the key. A save before that strike has no key, and `restore_struck` leaves the placement seed. | `struck_durability` is the same remaining-life map, written with the bank on every snapshot. It is still only the kind-9 set the strike index collected. |
| Script locals | Absent, apart from a bespoke key such as the elevator's local 4. | `locals` is the opcode-198 array. PROVEN the key is in the bank. |
| The `0x26E58` flags | Absent. | `locals_e58`. PROVEN the key is in the bank. |
| Timers | Absent. | Absent. No timer field in the five bank keys. |
| Dead creatures | `quests.act2_creatures_*` is the port's population list. | The bank does not add an actor element. The population list is only in the area packet. |
| Taken items | `inventory` and `quests.act2_items`. | The same area packet. The bank does not add an item section. |

## Missing

From F9, against the original per-level file: the movable object (`+0x48`, `+0x55`), the region-record floor word, control life beyond the kind-9 strike key, the script-local buffer, the `0x26E58` flag buffer, both timer sets, and the actor element. Creature populations and the item catalog are present as quest and inventory keys. They are the port's own lists.

From Sol's slot, beyond F9: `locals`, `locals_e58`, `record_state`, `state`, and `struck_durability`. Still absent: the movable position and state bytes, the live region height (including L19 floors 40 and 61), the kind-2 timer list, the clock range, the actor element, and a taken-item section. A staged `floor_target` can sit in `state` and still leave the floor mesh at the source height, because load does not apply it.

## Grades

PROVEN: the 68-section switch, the mix with the level `.img` for flag bit 1, the chunked write for flag bit 2, stride `0x58` for movables, stride `0x40` for controls, stride `0xBC` for actors, section 12's 44-byte records, section 24 as the opcode-198 buffer, global section 1 as the `0x26E58` buffer, sections 61–64 and 67 as the timer and clock bytes, the F9 and slot field lists above, and the death stores of health 0 and byte `+0xA8` = `0x0F` inside that actor element.

LIKELY: the floor height survives the per-record helper. The `0xB7DA4` / `0xB7DB0` pair is the kind-2 timer list. The `.lsv` just written and the `.lsv` the slot copies are the same blob.

UNKNOWN: which saved byte records a taken placement. The helper's source pointer in the region arm. The function that links suffix `0x3158` to suffix `0x3149`.
