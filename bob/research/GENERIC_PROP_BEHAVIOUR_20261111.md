# Generic object behaviour, 11 November 2026

Read-only. No build. The playtest rows are the ones in `grok_research/L10_L9_globe_loop_20261111.md`. Counts are from the fifteen native-script files in the r19pre tree (`scripts/lol2/native_scripts/L*.json`). Engine addresses are virtual addresses in the pinned `LOLG.DAT` (sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`). File offset is that address plus `0x37000`.

Grades are PROVEN, LIKELY, or UNKNOWN.

## Summary

The chests, crypt tops, and cemetery doors the player cannot open are movables. They are placed shut, and they have no script rows of their own. The original still opens them. A click calls one shared function on every movable. That function looks at a single bit in the placement. When the bit is set, a shut lid starts opening, a shut door starts its swing, and a later tick moves it. The cemetery rows all have that bit. The direction is another placement byte: chest lids move up or down, crypt tops slide sideways, and the named doors swing a quarter turn.

The breakable fronts are a different object, a control, and they do have script rows. A sword hit lowers a life number that starts at 100 on the cemetery covers. Four script rows wait for that number to fall through 80, then 60, then 40, then 20. The test that lets a row run is engine code (kind 9, mode 3). The row itself is what plays the break. Our port does not run mode 3, and the sword ray never hits these fronts.

Across every level file we have, 946 movables carry the click bit. 912 of those have no script on the object. 700 of the 912 are one copied block of fifty rows in each level, with the absent flag set. Setting that flag aside, 162 movables are in the same state as the cemetery lids: click bit set, no script, absent flag clear. The cemetery holds 56 of those 162. The port's shared click path hosts none of the 162, because that path only runs a script, and these objects have none. Two Maus doors turn when the player walks up to them, in a separate cemetery script. Nine temple pieces are shown or hidden by temple scripts. The chests, crypt tops, crypt covers, and the secret-crypt doors are not among those eleven.

Fifty-seven objects have the break test. Twenty-nine are cemetery controls, twenty-eight of them the four-stage covers. The port hosts none of the fifty-seven.

## A click on a lid or a door

These objects are class `0x20` movables. The constructor is `0x630A0` / `0x62FD4`. It writes the movable vtable `0x55B4` and copies the placement tail onto the object. PROVEN from the stores, with the object pointer plus `0x40` in `ebx` during the copies:

| Placement byte | Object field | Role on these rows |
| --- | --- | --- |
| `0x22` | byte `+0x53` | How it moves. 0 and 1 are height, opposite ways. 2 through 5 are the two flat directions, each with a sign. 6 is a turn. |
| `0x23` bit 1 (value 2) | byte `+0x54` | The click is allowed to start the motion. |
| `0x23` bit 2 (value 4) | same byte | The tick itself may start the motion. The cemetery rows do not have this bit. |
| `0x24` | word `+0x4E` | Distance, or, for a turn, the angle. |
| `0x25` | byte `+0x56` | Step size used by the tick. |
| `0x26` | dword `+0x48`, shifted up 16 | Starting position. These rows store 0. |
| `0x27` | byte `+0x55` | Starting state. Every row in the census stores 0, shut. |

For a turn (mode 6), byte `0x24` is doubled and passed to `0x605F0`. That function divides by 360 and returns `(degrees << 16) / 360`. PROVEN. The cemetery doors store 45, so the angle word is a quarter turn (`(90 << 16) / 360`).

The use function is vtable slot `+0x64`, address `0x641B0`. PROVEN:

- If object byte `+0x15` has bit `0x80`, it returns without moving.
- If byte `+0x54` does not have bit 1, it skips the motion and only calls `0x5DA48`.
- If the click context's dword `+0xC` is nonzero, or its dword `+0x28` is above `0x1000000`, it also skips the motion.
- Otherwise it switches on the state byte `+0x55` (table at `0x641A0`). State 0 becomes state 2 and copies the span word into the travel word. State 1 becomes state 3 and clears the travel word. State 2 becomes state 1. State 3 becomes state 0. States 2 and 3 also raise kind 6 with caller `0x11` (`0xADDE0`). An object with no rows has nothing for that hook to run.
- It then always calls `0x5DA48`. Earlier work showed that call only runs kind-4 script rows. These objects have no rows, so the call matches nothing. The state change has already happened.

The matching call site found in this pass is `0x110ACD`: `call [vtable+0x64]`, and only when the context byte `+0x33` is not 2, byte `+0x32` is 4, dword `+0x28` is at most `0x1000000`, and the object's flags lack bit `0x4000000`. PROVEN as that call. Byte `+0x32` is written by the pick, and the input that runs that pick is queue code `0x41`. The section below names the key.

The tick is vtable slot `+0x38`, address `0x63260`. The arm at `0x63732` adds a step to the position until it reaches the travel distance, then sets the state to 1 and raises kind 6 with caller `0x0F`, then `0x11`. A second arm at `0x63880` subtracts and finishes at state 5 with caller `0x10`. PROVEN as those arms. Which state number enters which arm was not the question this pass closed.

What the player sees is published at the end of that tick, from mode byte `+0x53` (`0x63C2A`). PROVEN:

- Mode 0 writes a height offset to global `0xB7C70` (`0x63B31`) and returns.
- Mode 1 writes the opposite combination to the same global (`0x63B57`).
- Modes 2 and 3 put the position, or its negative, on one flat component. Modes 4 and 5 do the same on the other component. The shared tail (`0x63B8E`) subtracts the object's own world position, then stores the two results in globals `0xB7C6C` and `0xB7C68` and clears `0xB7C70`.
- Mode 6 and above add no extra slide component before that same tail. Their motion is the angle word, not this slide.

The cemetery placements match that split. All of them are state 0, click bit set, no events, and not the target of an opcode-1 command:

| What the player sees | Movables | Template | Mode | Span byte | Step |
| --- | --- | --- | --- | --- | --- |
| Lid with chains, rises or lowers | 18, including 107 and 117 | 0 | 0 | 45 or 22 | 12 |
| Crypt top 3, slides sideways | 12 | 7 | 4 or 5 | 30 | 10 |
| Crypt top 4, slides sideways | 14, including 86 | 8 | 2, 3, 4, or 5 | 27 to 51 | 12 to 20 |
| Crypt top 1, slides sideways | 4, including 52 | 5 | 4 or 5 | 27 or 30 | 7 or 10 |
| Crypt cover, slides sideways | 66 and 67 | 4 | 4 | 28 | 5 |
| Secret crypt door, quarter turn | 126 and 127 | 3 | 6 | 45 | 12 |
| Maus door, quarter turn | 124 and 125 | 14 | 6 | 45 | 12 |
| Maus door 2, quarter turn | 122 and 123 | 15 | 6 | 45 | 15 |

The template names are the ones already used in the globe-loop note. The join from template byte to that name table was not re-read from the MIX tonight. LIKELY.

Flags on these rows are `0x0181` or `0x0182`. Both include bit `0x80` (solid) and neither includes the absent bit `0x1000`.

## A hit on a cover

The breakable fronts are controls, class `0x10`, not movables. A control has no slide bytes. The cemetery covers are template 1, flags `0x4482`, and each one has script rows. They are not the empty-event case.

A hit that reaches vtable function `0xB4218` does this. PROVEN:

- Flags byte `+0x14` bit `0x40` is clear on `0x4482` (the low byte is `0x82`), so the cap is the durability byte at object `+0x26`, not the constant 1. The getter is `0xB722C`. Placement byte `0x1E` is that starting durability. On the twenty-eight covers it is 100.
- The cap is copied into the hit context at `+0x22` and `+0x26`. Damage `0x62728` is called with a scale of 0. No armour value is passed.
- When `0x62728` returns, context `+0x26` is the cap minus the applied amount, and not below 0 (`0x62F5E`, `0x62F60`, `0x62F67`). The strike subtracts that amount from the durability byte through `0xB71EC`.
- `0xB4298` then runs only if flags dword `+0x14` has bit `0x400`. These covers have it. It calls kind 9 at `0xAE2C8`. That is the only direct call to `0xAE2C8` in the image.

Kind 9 reads byte `+8` of the script record and byte `+9`. The mode is byte `+9` masked with 7 (`0xAE435` to `0xAE440`). Mode 3 is `0xAE3A6`. It admits the row when the threshold is below the old cap and at least the life left after the hit: remaining `<=` byte `+8` `<` cap. PROVEN. The four cemetery rows are thresholds 80, 60, 40, 20, masks zero, mode byte 3. A hit that drops the life from 100 to 70 runs the 80 row only. The next hit uses the new life as the cap, so the 80 row cannot run again, and the 60 row can. One hit runs at most the first row whose threshold sits in that window. The rows do not delete the mesh by themselves. What each row plays is the script already listed in the globe-loop note.

The same test is on 57 objects. Every one of them has flag bit `0x400`.

| Level | Class | Count | Start life | Thresholds | Notes |
| --- | --- | --- | --- | --- | --- |
| L10 cemetery | control | 28 | 100 | 80, 60, 40, 20 | Template 1, the covers. Flags `0x4482`. |
| L10 cemetery | control | 1 | 80 | 50 | Control 5, template 66. Flags `0x4481`. |
| L4 | control | 1 | 100 | 60, 40, 20 | Control 79, template 71. |
| L3 | prop | 18 | 2 | 1 | Template 30. |
| L1 | prop | 2 | 3 | 2 | Template 68. Props 223 and 574. |
| L20 | prop | 6 | 255 | 1 | Template 12. A small hit does not cross 1. |
| L5 | actor | 1 | 200 | 1 | Actor 32. |

L3, L1, L20, and the one L5 actor are the same engine test on a different class. They are not the cemetery covers.

## Census

Fifteen level files. 1,401 movables.

| | Count |
| --- | --- |
| Movables whose placement byte `0x23` has the click bit | 946 |
| Of those, no script rows on the object | 912 |
| Of those 912, absent flag `0x1000` set | 700 |
| Same fifty-row pattern, but on L19 the absent flag is clear | 50 |
| Present click-slides with no script, outside that copied block | 162 |

The 700 are fifty rows in every level: mode 6, span byte 45, step 1, ten each of five templates, flags `0x1102`. Bit `0x1000` is set. Other notes in this project treat a set `0x1000` as "not in the world at the start," and the collision export skips it. A clear bit is not, by itself, a visibility grade. The original test that reads the bit was not re-entered tonight, so the "starts absent" reading stays LIKELY. The bit on these 700 rows is PROVEN.

L19 has the same fifty rows with flags `0x0102`, so the absent bit is clear. They are counted on their own line, not inside the 162.

The 162, by level and by mode:

| Level | Count | Mode 0–1 height | Mode 2–5 sideways | Mode 6 turn |
| --- | --- | --- | --- | --- |
| L3 | 4 | 0 | 0 | 4 |
| L4 | 4 | 1 | 0 | 3 |
| L5 | 2 | 0 | 0 | 2 |
| L9 | 57 | 1 | 0 | 56 |
| L10 cemetery | 56 | 18 | 32 | 6 |
| L12 | 8 | 0 | 0 | 8 |
| L14 | 17 | 0 | 2 | 15 |
| L16 | 14 | 4 | 0 | 10 |
| L1, L7, L8, L13, L17, L19, L20 | 0 | | | |
| Total | 162 | 24 | 34 | 104 |

L1, L7, L8, L13, L17, and L20 have the fifty-row absent block and no further event-less click-slides. Doors that do have script rows are outside this table. There are 34 click-bit movables that do own script rows, and 21 of those own a kind-4 row. The shared E path can run those 21. That is the scripted-door case, not this gap.

## What the port does today

Playtest tree `lol2_play_r19pre`, the r19pre scripts.

The shared E key lists only movables that already own a kind-4 row (`act2_progression.gd` lines 259–264) and fires kind 4 (`use`, lines 1142–1144). The input is lines 1365–1378. An event-less movable is not on that list. The hinge builder uses the same set, plus opcode-1 targets (`mover_ids`, lines 180–190). Seven of the 162 are named by an opcode-1 command somewhere in the level: one in L9, three in L14, and three in L16. A script can set their travel word. The other 155 are not built as moving hinges. They stay in the static mesh.

A captured swing looks for kind-9 rows on movables and controls (`_collect_struck`, lines 1195–1208) and casts a ray of mask 1 (`aimed_struck`, lines 1232–1246). Control solids are layer 256 (`static_assemblies.gd` line 85). Scripted solids are not given a body (line 99). Cemetery cover 241 is `scripted: true` in `static_collision_L10_DC.json`. The ray does not hit it. Props are not in the strike index, so the L1, L3, and L20 mode-3 props are not reached either.

If a hit did call kind 9, mode 3 still would not run. The matcher returns unhosted for every mode other than 1 and 4 (`native_script_host.gd` lines 845–846). The swing also passes the life left as `dword_26` and the damage as `dword_1e` (`strike_ref`, lines 1257–1261). Mode 3 needs the old cap as well, and this caller does not pass it.

Hand-written scripts that do move a member of the 162:

| Script | Movables | What it does |
| --- | --- | --- |
| `l10_globe_door.gd` | 124, 125 | Turns each Maus door a quarter turn when the player walks within 20. Not the state machine. |
| `l14_temple_doors.gd` | 92, 93 | Hides the pair when the temple door is unlocked. |
| `l14_trials.gd` | 88, 89, 90 | Owns the three trial doors and keeps an open list. |
| `l14_trap_route.gd` | 80, 81 | Owns the two bypass doors and keeps an open list. |
| `l14_bedroom.gd` | 0, 1 | Owns the headboard pair. |

That is 11 of the 162. The cemetery lids, crypt tops, crypt covers, secret-crypt doors, and Maus door 2 are not in that list. Dark Halls doors, jungle gates, and bookcases are scripted movables. They sit in the 34, not in the 162.

Hosted through the original click or the original break test: 0 of 162, and 0 of 57.

The click that requires context byte `+0x32` equal to 4 runs from queue code `0x41`. That code is written when the keyboard map returns byte `0x63`, the ASCII letter c. The letter e is not a compared byte, and no mouse button writes the code. A socket then accepts the use when the straight-line length is at most `0x1000000`. The port's socket test is a length of 140 and a facing dot of 0.8.

## Grades

PROVEN: the use function, the placement-byte copies, the quarter-turn conversion, the tick's add and subtract arms, the height and sideways publish, the strike's durability update, the mode-3 compare, the cemetery byte values, the counts above, queue code `0x41` as the input that reaches the use, byte `0x63` as the map value that writes that code, and the length test `0x1000000` on context `+0x28`.

LIKELY: template names, carried forward from the globe-loop note. Bit `0x1000` set means the row starts absent, carried forward from earlier notes. `0x5DA48` only runs kind-4 rows, from the earlier use-slot report. The sound call `0xE3924` inside the use function was not re-opened. The physical keycap for byte `0x63` is C. The length limit `0x1000000` is 256 in 16.16 units.

UNKNOWN: the name of context `+0xC`. Where the 60-byte movable template table pointed at by global `0x22D4C` lives in the level file. The draw code that reads globals `0xB7C68`, `0xB7C6C`, and `0xB7C70` was not entered, so this note says what is published, not which polygon moves on screen. The bytes inside the scancode map at driver `+0x1C9`, so the physical keycap that becomes byte `0x63` stays LIKELY rather than read from a table in the file. Whether ray `0xE2E40` can reject a socket because a wall is in the way.

## Which input runs the click

Context byte `+0x32` is not a key code. Two functions store the constant 4 there: `0x11112C` and `0x111198`. They run while the pick is choosing an object. The use gate then calls vtable `+0x64` only when that byte is already 4.

The input that reaches the use is queue code `0x41`. The dispatcher at `0x7508B` compares the low byte with `0x41` and with `0x42`. Equal `0x41` sets a flag and later calls `0x75D98` at `0x75120`. Equal `0x42` takes the same mouse-position call and then returns without `0x75D98`. Any other low byte returns. `0x75D98` is the function that runs the pick and then the use gate. Its only direct caller is `0x75120`. PROVEN.

Code `0x41` is written by the keyboard translator `0x15B21C`. After the scancode map, it compares the byte:

- Byte `0x63` becomes `0x41` (`0x15B27C`). `0x63` is the ASCII letter c.
- When driver dword `+4` has bit `0x2000` set, bytes `0x2B`, `0x3D`, and `0x6C` (`+`, `=`, and `l`) also become `0x41`.
- Byte `0x68` (`h`) becomes `0x42`. Byte `0x64` (`d`) becomes `0x43`. Byte `0x65`, the letter e, is not one of these compares.

The map read is `mov al, [driver + scancode + 0x1C9]` at `0x15B84D`. The driver is the block at `[0x1890D]`. That table is filled into the driver at runtime. A set-1 ASCII table with `e` at scancode `0x12` and `c` at scancode `0x2E` is not present in the file image, so the physical keycap is LIKELY the C key and was not read off a stored map. PROVEN the compared byte. LIKELY the keycap.

The translator's only direct caller is `0x15B962`, inside the keyboard handler that just performed that map read. The enqueue of the queue word has three call sites, all inside the translator. A search of object-2 code found no other `mov al, 0x41` that enters this queue. The mouse x and y are copied onto the event after the key is translated (`driver +0x379` and `+0x381` snapshotted at `0x15B22D`). They do not select code `0x41`. PROVEN.

A press and a release both leave the low byte as `0x41`. The handler sets bit 8 of the high byte on a break code (`0x15B80A`). The translator still stores `0x41` and still enqueues, and on the break it clears bit 0 of driver `+0x3C8` (`0x15B292`). The dispatcher compares only the low byte, so the release enters `0x75D98` as well. PROVEN.

## Socket reach

The T6 gargoyle is control 158, class `0x10`. Its use slot is vtable `+0x64` = `0x5DA48` (object-5 `0x5484`). The gate calls that slot when byte `+0x32` is 4, byte `+0x33` is not 2, the object flags lack bit `0x4000000`, and the length at context `+0x28` is at most `0x1000000`. `0x5DA48` repeats the length test on its second argument `+0x28` (`0x5DA61`) and returns before the script call when object byte `+0x15` has bit `0x80`. PROVEN.

The length is the return of `0x136594`. That function subtracts the two pairs, squares them, adds them, and takes the integer square root (`fild` / `fimul` / `fsqrt` / `fistp` at `0x1365AB`). The pick `0xE1050` passes the controller `0x227A4`: the standing pair is dword `+0x19` and dword `+0x1D`, and the target pair is context `+0` and context `+4`. The result is stored at context `+0x28` (`0xE1194`). PROVEN. LIKELY those dwords are 16.16 positions, which makes `0x1000000` equal 256. A plain-integer limit of 16777216 would sit far outside a cemetery coordinate, and the movable position dword is already stored shifted up by 16. The shift on this pair was not re-read.

The gate and `0x5DA48` do not compare a facing dot. The ray that chooses the object is `0xE2E40`. Its wall test was not entered, so whether a wall can keep the gargoyle out of the pick stays UNKNOWN.

The port's test is `l10_tombs.gd` `reachable`, lines 70–76. It rejects a length over 140, a length under 0.01, or a facing dot under 0.8, and the ray mask is `1|AIM_LAYER`. Success is an empty ray or a hit on that receptacle. That is the port's test. Sol's T6 report is that this ray hits ProjectileWalls, so `reachable` stays false.

## Left for review

No port change is in this note. Q13 stays parked. Assignments B, C, and D were not started.
