# Stacked floors and the original region mover, 12 November 2026

Read-only. No build. The lead's collision trial stays paused. Pinned `LOLG.DAT` sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`, size `0x1e2aaf`. A code address A is file A+`0x37000`. Pinned `DAT/L10_DC.MIX` sha256 `543c86c4fdd425cac166d9a1d371aa856b7070d4fded983a8733c473e48341f9`. Geometry key `3260615568`, sha256 `ef89467deb4073f6d60e70baa45bd5ec55b422f1d28b518b16f7cab86434d5e3`, 6190 vertices, 4320 regions. Vertex stride 8 at geometry `0x14B4`. Region stride `0x2C` at geometry `0x1D70A`. A vertex is two signed dwords in the same 16.16 units as the moving point. Numbers below are those units divided by 65536. Grades are PROVEN, LIKELY, or UNKNOWN.

The box is the lead's three hours on `lead_notes/TRIAL_A_REGION_COLLISION_20261112.md`. This note stops at the region rule. The fall, the collapsed-tomb drop, and the lift writer are what is left.

## Summary

The original keeps the region it already has while the plan point stays inside that region's four-vertex polygon. The step that changes region is the first of the four neighbor slots whose polygon contains the point. The height word is not read by that choice.

On the Emperor stairs the three records are different quads that overlap in plan. Region 1880 and region 1872 are floor 0. While either one is the stored hint and the point is still inside it, the finder returns that same region and does not consult the catacomb underneath. Region 3922 is floor −100 and has flag bit `0x20` set, so a hint of 3922 is not kept. The finder walks the run that starts at word `+0x20`, regions 3923 through 3932, floors −90 through 0, and returns the first of those thin quads that contains the point. The centroid of 1880, passed in with hint 3922, comes back as band 3925 at −70.

The per-step search is `0xAF9A4`, called from the actor tick `0xB286C`, with the finder's fourth argument 0. A search that returns 0 refuses the new point: a short step snaps back, a longer step is halved and tried again. The floor height is a separate read of the signed word at region `+0x14`. A second wall mesh was not found in the search. The tail of `0xB0880` still loads the four vertices and was not entered.

## The finder

`0xF40AC(x, y, hint, arg4)` chooses the region. Local `[esp+0x14]` is the constant 1 and is the flag passed into `0xF3EF0`. PROVEN from `0xF40AC`.

1. A null hint goes to the scan exit at `0xF433D`.
2. Otherwise `0xF3D20(hint, x, y, 0)`. If the point is inside, the finder returns `0xF3EF0(hint, x, y, 1)`. This is the keep.
3. Otherwise the four neighbor words at hint `+0x04`, `+0x06`, `+0x08`, `+0x0A` are tested in that order. `0xFFFF` is skipped. The region is `[0x22D0C] + index*0x2C`. The first `0xF3D20(..., 1)` hit returns `0xF3EF0` of that region and the later slots are not tested.
4. If the hint's flag bit `0x80` is set, the finder walks backward one record at a time while the previous record also has bit `0x80`, then tests that record.
5. Word `+0x18` indexes the chain at `[0x22D10]` with stride 42. `0xE26A0` is called. Its body was not entered. The walk after the call was: byte `[entry+0x17]` is a count, word `[entry]` is a start index, and that many consecutive regions are tested. The first hit returns through `0xF3EF0`.
6. `0xE2760` runs, body not entered. The list at `[0xB8780]` is then walked with the same count and start-index pair. A hit whose returned region has byte `+0x26` equal to the hint's byte `+0x26` calls `0xE2810` and returns that region. A different `+0x26` is remembered when the slot is empty. After the list, a remembered region is returned. `0xE2810`'s body was not entered.
7. At `0xF433D`, a null hint or a nonzero `arg4` returns `0xF3FE4(x, y, -1)`. A nonzero hint with `arg4` 0 returns 0.

`0xF3D20` loads the four vertex indices at words `+0x0C`, `+0x0E`, `+0x10`, `+0x12` through the vertex table at `[0x22D04]`. A nonzero fourth argument runs a bounds pass over those four vertices before the edges. That pass was not copied out in full. The four edges were. Each edge from `(x0,y0)` to `(x1,y1)` keeps the point when the high half of `(px-x1)*(y0-y1)` minus the high half of `(py-y1)*(x0-x1)` is less than or equal to 0 (`imul`, then `edx`). A positive result returns 0. The fourth edge is `0xF3EA2`. All four edges passing returns 1 at `0xF3EE1`. PROVEN.

`0xF3EF0(region, x, y, flag)` is the stacked-floor step. PROVEN.

- Flag bit `0x80` of word `+0x1C` returns the region immediately (`0xF3F07`).
- When `flag` is nonzero and bit `0x20` is clear, the region is returned immediately (`0xF3F25`). When bit `0x20` is set, the run starts at word `+0x20`. Each record is tested with `0xF3D20(..., 1)`. The first hit is returned as itself, with no second call to `0xF3EF0`. Word `+0x16` nonzero advances `0x2C` and repeats. A run that misses calls `0xF4A4C(original, &xy, -1, flag)`. The body of `0xF4A4C` was not entered.
- When `flag` is 0, the same shape uses bit `0x40` and word `+0x22`.

`0xF3FE4(x, y, mask)` scans from `[0x22D0C]` for count `[0x22D2C]`. Mask `−1` skips flag bit `0x80` and returns the first polygon hit through `0xF3EF0`. A nonzero mask also requires `(byte +0x26 & mask)` to be nonzero. The scan is record order. PROVEN from `0xF3FE4`. The no-hit exit at `0xF40A1` was not printed.

None of `0xF3D20`, `0xF3EF0`, `0xF3FE4`, or `0xF40AC` reads the height word. PROVEN.

## Who calls it for a moving body

`0xB30AC` walks the actor list and calls `0xB286C` at `0xB3173`. After that list it calls `0xD26B0` at `0xB31F9` with the unnamed player object. `0xD26B0` reads the stored region and fires events. It does not call the finder.

`0xB286C(actor)` sets `[0xB7CA1]` to the actor. If byte `[actor+0x15]` bit `0x10` is set, it returns at `0xB28EB` before the floor read and before the search (`sete` then `je`). If the bit is clear, the current region is `[0xB7CDD]` when `[0xB7D84]` is nonzero and the actor is `[0xB7CA1]`, otherwise `[link+4]` when `[actor+0xC]` is a link, otherwise the pointer stored at `[actor+0xC]`. PROVEN.

The search runs at `0xB3054` unless every one of these is true: local `[ebp-0xC]` is 0, `[0xB7C6C]` is 0, byte `[actor+0x24]` is 0, the facing word `[actor+0x1E]` equals `[0xB7CD1]`, `[0xB7C70]` is 0, and dword `[actor+0x14]` bit `0x10000` is clear. An earlier call at `0xB2B10` also enters `0xAF9A4`. What the still-bits mean in play was not named.

`0xAF9A4(actor)` is the per-step solver. PROVEN from its entry at `0xAF9A4` through the accept and the reject.

- It resolves the current region into `[ebp-0x5C]`, copies it to `[0xB7CDD]`, and sets `[0xB7D84]` to 1.
- The step in x,y is built from the sine table at `0xDB650` and added to `[0xB7C75]` and `[0xB7C79]`. The vtable slots on `[actor+0x28]` that feed that step were not entered.
- At `0xAFF3A` the fourth argument pushed for `0xF40AC` is 0. The hint is the register that held the current region, or `[ebp-0x5C]` when that register is 0. X and y are the full 16.16 values.
- An earlier call at `0xAFE02` runs only when byte `[0xB7D4D]` is `0x20`, using `[actor+0x40]` and `[actor+0x44]` and fourth argument 1. What `0x20` means is UNKNOWN. If the main search returns 0, that earlier result is used.
- A returned region equal to `[ebp-0x5C]` is kept.
- A different region is rejected, by clearing the result, when byte `[0xB7D4D]` is 1 or 4 and the new region's flag bit `0x01` is set (`0xAFF85`), or when the byte is 2 and flag bit `0x02` is set (`0xAFF99`). The byte is a vtable return stored at `0xAFA81`. UNKNOWN which value the player returns.
- A zero result refuses the candidate. If both axis deltas from the old x,y are at most `0xFFF`, the old x,y are restored and the remaining step is cleared. Otherwise the remaining step is halved and the candidate is the average of the new point and the old point. A halved step that becomes 0 restores the old point. The loop returns to `0xAFF32`. PROVEN. LIKELY this refusal is the wall: the only geometric reject in the finder is a point that sits in no linked polygon, and a neighbor of `0xFFFF` cannot be crossed by the four-slot walk. With fourth argument 0 the full scan does not run.
- On a kept result, `[0xB7CDD]` is set to the region (`0xB007C`) and the region is also stored through the pointer in `[0xB7D94]` (`0xB008B`). `0xB0880` is then called. No direct store to the global `0xB7D94` was found. `0xAE966` pushes the address of that global into `0x14F85D`. That call was not entered. UNKNOWN which slot the pointer addresses.
- When the remaining step is finished, x and y are written to `[actor]` and `[actor+4]` (`0xB021C`). A following loop calls `0xB85A4` to relink. How many links it writes was not reduced.

`0xAF0E0(owner, hint)` is the placement relink, not the per-step walk. If `[owner+0xC]` is nonzero and bit `0x10` of byte `+0x15` is clear, it unlinks until the slot is 0. If the bit is set, it stores 0 there first. It then calls `0xF40AC` with fourth argument 1. A nonzero result with the bit clear allocates `0x10` bytes from the cell `[0xB7E24]` and calls `0xB85A4`. A nonzero result with the bit set stores the region pointer at `[owner+0xC]` (`0xAF18A`). PROVEN. The reader in `0xB286C` takes the region from `[link+4]` for the bit-clear form.

`0xD0250` is placement. It stores x, y, and the facing word, then calls `0xF40AC` with fourth argument 1 (`0xD029F`). A 0 result calls `0xF43B4` and stores the two returned dwords as x and y. `0xF43B4` was not entered. It then calls `0xAF0E0`. When the sixth argument is nonzero it writes `[actor+8]`: `0xF4614` when flag bit `0x04` is set, otherwise the signed height word minus byte `+0x27`, shifted back to 16.16 (`0xD033E`). PROVEN.

UNKNOWN which form the live player uses. Bit `0x10` set makes `0xB286C` return before `0xAF9A4`. The per-step search entered here is the bit-clear form.

## Floor height is a separate read

The height the mover uses is the signed word at region `+0x14`. The instruction is `mov eax, [region+0x12]; sar eax, 16; shl eax, 16`. The word at `+0x12` is vertex index 3. The dword at `+0x12` packs that index in the low half and the height in the high half. PROVEN at `0xB2996`, at `0xB0A86`, at `0xAFD54`, and at `0xD031D`.

Flag bit `0x04` selects `0xF4614(region, x, y, 0)` instead of that word. The body of `0xF4614` was not entered. Regions 1880, 1872, 3922, and bands 3923–3932 all have bit `0x04` clear, so this case uses the stored word.

`0xB286C` stores `(floor − [actor+8])` at `[0xB7D15]`. A negative difference, body above the floor, jumps to `0xB2A2F` and skips the scale that follows. The same block stores `(byte [region+0x27] << 16)` at `[0xB7D19]`. PROVEN. On the stair records that byte is 0.

`0xB0880` runs after a successful pick. Flag bit `0x800` clear, which is the stair records, goes to `0xB0A53`. There `[0xB7D25]` becomes the floor minus `[0xB7D19]`. If that value is above the vertical target `[0xB7D35]`, the target is raised to it (`0xB0B87`). `[0xB7D35]` was set from `[actor+8]` at `0xAFC54`. A floor below the body does not take that raise. `[0xB7D29]` is `0x3FFF0000` when byte `+0x22` is `0xFF` (`0xB0AE5`). 1880 and 1872 have byte `+0x22` equal to `0xFF`, so the later lower-the-target test does not apply at a height of 0. Region 3922 has byte `+0x22` equal to 0 and word `+0x16` equal to 200, and with flag bit `0x80` clear and bit `0x08` clear the ceiling value is that word shifted to 16.16. A body at 0 is below it. PROVEN for these bytes. UNKNOWN whether some other actor bit reaches the copy of `[0xB7D25]` into the target at `0xB041D`. That copy sits behind byte `+0x15` bit `0x20`, dword `+0x14` bit `0x400000`, and byte `+0x24`.

After that, `0xAF9A4` writes `[actor+8]` from `[0xB7D35]` (`0xB051D` when the target is less than or equal to the current height, `0xB0518` on the other arm). PROVEN the stores exist. The arm that would fire for a body left above a lowered floor was not reduced, because the player's bit `0x15` and bit `0x20` were not read from a live object.

## L10 Emperor stairs

Native quads, measured with the edge test above. Each centroid is the average of its four vertices and is inside its own polygon.

| Region | Floor word `+0x14` | Flags `+0x1C` | Word `+0x16` | Word `+0x20` | Byte `+0x26` | Byte `+0x27` | Neighbors |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1880 | 0 | `0x0000` | 175 | 32768 | 1 | 0 | 1870, 1872, 1879, none |
| 1872 | 0 | `0x0202` | 130 | 32768 | 1 | 0 | 1880, 1874, 1871, 1867 |
| 3922 | −100 | `0x0220` | 200 | 3923 | 2 | 0 | 3859, 3933, 3851, 3921 |

1880 vertices 1892, 2304, 2305, 1893: (3148, 1941), (3163, 2174), (3252, 2174), (3210, 1941). Centroid (3193.25, 2057.5).

1872 vertices 2305, 2304, 2437, 2508: (3252, 2174), (3163, 2174), (3164, 2250), (3251, 2301). Centroid (3207.5, 2224.75). 1880 and 1872 share the edge at y 2174.

3922 vertices 2024, 2023, 2416, 2417: (3257, 2010), (3151, 2010), (3111, 2231), (3307, 2231). Centroid (3206.5, 2120.5).

1880's centroid is inside 1880, inside 3922, and inside band 3925. 1872's centroid is inside 1872, inside 3922, and inside band 3932. 3922's centroid is inside 1880, inside 3922, and inside band 3928. PROVEN.

Bits `0x20` and `0x40` are clear on 1880 and on 1872, so `0xF3EF0` returns that record and does not walk word `+0x16`, even though those words are 175 and 130. Bit `0x20` is set on 3922, so the run starts at 3923. The run is consecutive. Word `+0x16` counts down and the walk stops on 3932, where `+0x16` is 0. Each band has flags `0x02A0` (bits `0x20` and `0x80`), byte `+0x27` equal to 0, and neighbors that name the next band and 3922. PROVEN.

| Region | Floor | Word `+0x16` | Y span of the quad |
| --- | --- | --- | --- |
| 3923 | −90 | 9 | 2010 to about 2033 |
| 3924 | −80 | 8 | about 2032 to 2052 |
| 3925 | −70 | 7 | about 2052 to 2075 |
| 3926 | −60 | 6 | about 2074 to 2099 |
| 3927 | −50 | 5 | about 2098 to 2119 |
| 3928 | −40 | 4 | about 2119 to 2139 |
| 3929 | −30 | 3 | about 2139 to 2162 |
| 3930 | −20 | 2 | about 2162 to 2187 |
| 3931 | −10 | 1 | about 2187 to 2209 |
| 3932 | 0 | 0 | about 2209 to 2231 |

Applied to the stair, PROVEN:

- Hint 1880, point still inside 1880: the finder returns 1880. Region 3922 is not a neighbor and is not read.
- Hint 1872, point still inside 1872: the finder returns 1872. Flag bit `0x02` is set, so a per-step change into 1872 is rejected when byte `[0xB7D4D]` is 2. UNKNOWN whether the player byte is 2. 1880's flags are 0, so that reject does not apply to 1880.
- Hint 3922: the finder returns the first band whose polygon contains the point. At the 1880 centroid that band is 3925, floor −70. It does not return 1880.
- Once a band is the hint, bit `0x80` keeps that band while the point stays inside it. Leaving it tests the four neighbor slots. A slot that names 3922 calls `0xF3EF0(3922)`, which enters the run again. 1880 and 1872 are not neighbors of the bands.
- 1870 (floor 0, flags 0, neighbors include 1880) and 1879 (floor 0, flags 0, neighbors include 1880) are the side records that name 1880. Crossing from one of those into 1880 is the neighbor step.
- A write to the height word, with the plan point left where it is, does not change the region `0xF40AC` returns.

## What is left

The three-hour box stops here. These were asked and were not closed.

- Fall. `[actor+8]` is written from the vertical target at `0xB0518` and `0xB051D`. The clamp in `0xB0880` raises that target up to a floor that sits above it, and on these stair flags it does not pull a target down onto a floor that has dropped below the body. The copy of the adjusted floor into the target at `0xB041D` depends on actor bits that were not read from a live player. The countdown at `[actor+0x1D6]` was entered in an earlier pass, does not call the finder, and was not re-entered here. UNKNOWN which path moves the body down when the floor under it is lower.
- Collapsed tomb. Lowering word `+0x14` leaves the finder on the same region. UNKNOWN which function writes that word for a tomb, and UNKNOWN whether the body is then moved down. The whole 44-byte region record is the saved section 12, so a later tick would read the written word. That is the read. It is not a drop.
- Lifts. UNKNOWN which function writes the floor word while a floor is moving, and UNKNOWN whether `[actor+8]` is carried with it. `0xD0250` writes `[actor+8]` only when its sixth argument is nonzero, and that is placement.
- A further wall test. LIKELY the halved step is the wall. UNKNOWN whether the unread tail of `0xB0880` after `0xB0BDD`, or vtable `+0x50` at `0xB3084`, or vtable `+0xD8` at `0xB00C3`, tests edges again. `0xF4614` and `0xF48C4` were not entered. `0xF4A4C` was not entered. The sampled 3922 points do not miss the band run, so that miss path is not required for this stair.

Q13 stays parked. The tracker rebuild belongs to the lead's trial. This pass did not turn region collision on and did not edit the trial branch.
