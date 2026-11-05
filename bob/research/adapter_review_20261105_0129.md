# R2 adapter review, rows 0129–0144, 2026-11-05

No Godot was run. No opcode callee was entered. Newest owner file is still `TRIAGE_20261104.md`. r15 is `f6a5aa4`, act3-story is `d9e3aaf`, and r12y is `56812f9`. The idle line still names r12y.

Rows 0086 through 0128 already have a per-row section in `adapter_review_20261102.md`. Each of those deviation files matches r15 byte for byte. They were not rewritten.

These sixteen files also match r12y byte for byte. `dark_halls_doors.gd` matches r12y. The live blocker flags below are the same in both trees.

## 0129 dark halls doors

The row sends doors 56 and 57 through `native_script_host.gd`. E within reach and facing fires kind 4 with `arg_c` 0. The click path and the meaning of `arg_c` stay UNKNOWN in the row. Slot N as placement record N stays LIKELY.

DECODED. `dark_halls_doors.gd` uses reach 120, facing dot 0.7, and `fire_event` with `arg_c` 0 and context `movable:<id>`. A locked door returns the feedback line and does not fire kind 4. The host still names adapter `slot_index_binding` and still calls the index LIKELY.

HINTBOOK lines 2531–2540 say to spark a crystal box against a door and against a bricked window. BRADY lines 2117–2123 say the Dark Halls crates blast holes through locked doors. Those sentences print no reach and no `arg_c`. The E adapter stays the row.

Still open: the original click path, and the proof of slot N.

## 0130 swing

The leaf turns by sign times the travel word times 360/65536. Word 21845 is about 120 degrees. The swing is 1 second because the native speed is unproven. Door sounds are logged and not played.

DECODED. `_target_degrees` is that formula. `SWING_SECONDS` is 1.0. The tick comment says the native speed is not proven.

The hintbook and Brady sentences above print no 21845 and no 1 second. No printed number replaces the second. The logged sounds stay the row.

## 0131 save fields

Saves keep `+0x25`, `+0x3D`, `+0x26`, the travel word, and the opcode-198 array. Open mirrors travel not equal to 0. An old save loads an open door as `+0x25` 1 with word 21845.

DECODED. `NATIVE_FIELDS` is those four names. The load comment maps a missing native block the same way. The constructor comment says the travel word is absent until a door group writes it.

Books print no such field. The old-save map stays the row.

## 0132 trap and lock

Group 794 stays unhosted because it holds opcodes 18 and 13. Entry applies travel word 0. E on the locked door gives feedback. Shade 73's death runs group 15750. Group 15756, opcode 6, stays unhosted.

DECODED. `spring_trap` sets travel 0, locks the door, and says opcodes 18 and 13 are not hosted. `use` on a lock saves the feedback and returns. Those opcodes were not entered.

HINTBOOK 2531–2540 and BRADY 2117–2123 stay the crate sentences. They print no group 794. The closing adapter stays the row.

## 0133 source walls

The row appends 280 Jungle wall records and 304 Hive wall records, drawn one-sided, with no collision. Hive records with byte 5 bit `0x10` stay out. The 120 retired span indexes stay the port's.

This pass did not recount 280 or 304 and did not enter the span builder. Books print no such count. The one-sided draw stays the row.

## 0134 jungle ceilings

460 ceilings come from the native ceiling selector. Selector 255 is none. The row calls this native.

This pass did not recount 460. Books print no ceiling count and no selector 255. The two-sided ceilings stay the row.

## 0135 region 65535

Placements whose region word is 65535 take the native spawn lookup. Jungle 75, Hive 3, and L8 2 stay unhosted when no region contains them. The row says a region-less draw is untraced.

The lookup addresses stay unread. Books print no 65535. The parked rows stay the row.

## 0136 blockers attached

Cave, Museum, Hive, and Dark Halls take the Jungle bit-0 walls, height floor through ceiling+1024, on physics layer `1<<9`. The row's counts are Cave 6/12, Museum 492/549, Hive 63/68, Dark Halls 61/42.

DECODED. Each of those four hosts attaches `region_blockers.gd` when its flag is true. The counts were not recounted. Books print no 1024. The height band stays the port adapter the row already names.

## 0137 off by default

The row turns those blockers off outside the Jungle, because the earned Museum escape stopped at region 1422.

DECODED. The live flags are true: `cave_walkthrough.gd`, `museum_walkthrough.gd`, and `hive_review.gd` set `region_blockers_enabled` true, and `dark_halls.gd` sets `dark_halls_blockers_enabled` true. The museum comment says region 1422 is open in the pack. Row 0185 is the later on-row and says it replaces this off default. Row 0184 takes 1422 out of the static blocked set and leaves the opcode-197 opener UNKNOWN. That opcode was not entered.

Books print no sentence that disables the blockers. The off default does not stay. 0185 is the live row, so this pass adds no new proposal.

## 0138 museum frame flags

Thirteen Museum prop records apply frame flags `0x40` and `0x80`. The dust prop is flag `0x80` at the ceiling. Positions stay native.

DECODED. `museum_props.gd` flips columns on `0x40` and rows on `0x80`, and names the ceiling dust. Books print no such flag. The dust sentence in the hintbook is a cemetery line and stays off this prop. The flip stays the row.

## 0139 slot index

Kind-byte target N is placement record N. The class is PROVEN in the row. The index stays LIKELY.

DECODED. `native_script_host.gd` still documents `slot_index_binding` as that LIKELY index. The resolver was not entered. Books print no slot rule. The index stays LIKELY.

## 0140 constructor bits

Bytes `+0x15` bits `0x80` and `0x10` are taken as clear when the constructor value is unknown. The row says that value is not decoded.

DECODED. The host still names `b5000_bit_clear` and `b71a0_bit_clear` for those two bits. `0xB5000` and `0xB71A0` were not entered. Books print no such bit. The clear stays the row.

## 0141 opcode 5 follow-ups

Opcode 5 stores the selector at `+0x3D`. The `+0x3B` update and the vtable loop stay unentered. The bit-`0x400` store stays LIKELY in the row.

DECODED. The host comment for `opcode5_followups` says those calls are not modelled. They were not entered. Books print no selector store. The follow-ups stay open.

## 0142 opcode 5 spatial

Props and actors store `+0x30` from command byte 4. The frame count and the restart stay unmodelled. Relative prop selectors stay unhosted.

DECODED. The host comment for `opcode5_spatial` matches that sentence. Those calls were not entered. Books print no frame count. The restart stays open.

## 0143 ray masks

This file repeats the 0136 attachment and adds the ray-mask exclusions for the hourglass, the gallery, the wheel door, and the floor probes. The height band stays the same port adapter.

The test named in the row was not run. Books print no mask bit. The exclusions stay the row.

## 0144 museum flags again

This file matches 0138 byte for byte. The same flip stays. Books still print no flag `0x40` or `0x80`.

## Grade

HINTBOOK for lines 2531–2540. BRADY for lines 2117–2123. DECODED for the sixteen-file match, the door host, the four blocker flags, the museum flip, and the four host adapter names. The slot index and the opcode-5 stores stay the rows' LIKELY. No printed number replaces 120, 1, 21845, 280, 304, 460, or 1024.

## Still open

The door click path. Group 794's opcodes 18 and 13. The opcode-5 follow-ups. The opcode-197 opener on region 1422, which row 0184 already leaves UNKNOWN.
