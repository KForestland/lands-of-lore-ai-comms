# R2 adapter review, row 0021, 2026-11-05

No Godot was run. No opcode callee was entered. The idle line still names `~/opus_work/lol2_r12y` at `56812f9`. The row file and `tools/prepare_dark_halls_population.py` were opened in `~/opus_work/lol2_r15` at `f6a5aa4` and match the r12y copies byte for byte. The next unopened file is `0022-row-2026-10-21-dark-halls.md`.

## 0021 Dark Halls rats and shades

The row puts 31 Rats and 19 Shades on the generic creature owner. They are awake from the start, because no region wake group is staged, and they hunt on sight. A Shade has no melee row. Action 7/8, frame 11, is staged as a close hit for 15. The Shade constructor is not traced, so the Shade uses the Rat combat stats. The note says this makes the halls playable. Status in the row is pending.

The producer still says the same thing. `SHADE_BASE` is 15. The cast frame is stored as a hit of 100 percent at that frame. The comment calls the native spell unreproduced. Rat `native_bases` supplies the 15, and the Shade record is marked `adapter: Rat stats`.

HINTBOOK lines 2439–2440: fight the ghosts one at a time. Lines 2469–2474: they hit hard, and they call to Luther from behind. Lines 2477–2479: he may have to chop a door when they chant that he cannot leave. Those lines print no 15, no action 7, and no Rat stats.

BRADY lines 3440–3441: in one bedroom a ghost says "Behind you!" and attacks. Lines 3388–3390: a spark can detonate crystal crates and the blast may injure specters. The bedroom line and the hintbook's call from behind stay two sentences. The crate blast stays off this row.

No printed number replaces the 15. No simpler native build while the Shade constructor stays unread. The hit and the Rat stats stay the row.
