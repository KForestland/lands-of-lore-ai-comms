# R105. G-05 region tracker against the stacked-floor note

Read-only. Commit `24bc18968b50318bdedd381d1b3d8b8da2605dcf` on `lead/region-collision-trial-20261112`, worktree `~/opus_work/lol2_lead_regions`. Compared with `grok_research/REGION_STACK_MOVER_20261112.md`. The note's L10 proof points were checked on the generated table `assets/lol2/generated/region_mover/L10_DC.json` (source sha256 begins `543c86c4fdd425ca`, the pinned MIX). This pass did not relaunch Godot. The commit message is the source for the five earned routes.

## What follows the note

`_collision_region_at` keeps the tracked region while the plan point is inside its four-vertex quad. That test reads x and z only. The four neighbour words are then tried in slot order, and the first quad that holds the point wins. Flag bit `0x80` returns that record. Flag bit `0x20` walks the run and returns the first record of the run whose quad holds the point, with no second resolve on that record.

The table matches the note on the Emperor stair. Region 1880 is flags `0x0000`, floor 0, neighbours 1870, 1872, 1879, none. Region 1872 is flags `0x0202`, floor 0, neighbours 1880, 1874, 1871, 1867. Region 3922 is flags `0x0220`, floor −100, neighbours 3859, 3933, 3851, 3921, and its run is 3923 through 3932. Those bands are flags `0x02A0` and floors −90 through 0. Godot z is the native y with the sign flipped, and the quads are the note's vertices. The three centroids classify the same way as the edge test: the 1880 centroid is inside 1880, 3922, and band 3925; the 1872 centroid is inside 1872, 3922, and band 3932; the 3922 centroid is inside 1880, 3922, and band 3928.

Applied to the tracker, a hint of 1880 at its own centroid stays 1880. A hint of 1872 stays 1872. A hint of 3922 at the 1880 centroid resolves to band 3925. A band hint stays on that band while the point is inside it. Leaving a band toward the next one hits neighbour 3922 first, and the run walk then returns the band that holds the point. That is the same hand-off the note describes.

`tools/prepare_region_mover.py` builds each row as quad, flags word `+0x1C`, the four neighbour words, the floor word, and the floor run. The run is the geometry export's `floor_subdivisions`, and that export follows `0xF3EF0`: start at word `+0x20`, step one record, stop when word `+0x16` is 0. The tables are unfiltered. The source pin matches the note.

## Named replacements

Ledger `docs/deviations/0625-row-2026-11-12-g05-region-mover-collision.md` names three replacements. The code matches the ledger.

1. The vertical column stands in for the undecoded fall, tomb-collapse, and lift writers. It is floor triangles whose absolute normal y is at least 0.7, at or below the feet plus 48, in the body's grid cell and the eight cells around it, sticky inside one cell. Walls stay with the 8-hop ball. A band's hop ball uses the parent region, because the band has no nav quad.

2. When the tracked floor is more than 64 above the body, or the keep and the four neighbours all miss, the region is chosen again as the highest floor at or below the feet plus 48 among quads that hold the point. Records with bit `0x80` are skipped in that scan, then the chosen record is resolved with the same `0x20` / `0x80` rule. The ledger cites this in place of the record-order scan `0xF3FE4`.

3. A `0x20` run that misses keeps the parent. The note left `0xF4A4C` unread, and the code says so.

The header comment above `COLUMN_LEAVE` still says 48. The give-up in `_collision_region_at` uses `COLUMN_DROP`, which is 64, and `COLUMN_LEAVE` is unused. The ledger's 64 is the value that runs.

## Left open, and one restore detail

The note's per-step reject, flag bit `0x01` or `0x02` against the unread player byte at `0xB7D4D`, is not in the tracker. Region 1872 has bit `0x02`. Whether the player byte is 2 was UNKNOWN, so accepting that neighbour is the open case, not a second rule.

The finder steps after the four neighbours, the backward `0x80` walk and the unread `+0x18` and `0xE2760` lists, are not coded. The note did not enter those bodies. On the stair, the fresh pick still resolves a point inside 3922 through the run.

A total miss that the fresh pick also fails falls through to `progression.region_at`, which picks the quad containing the point whose floor is nearest the body, and that path can return an `0x80` record. The tick keeps the previous collision set when the result is negative.

`apply_save` still accepts a saved region only when the nav quad contains the body. A saved band index has an empty nav quad, so it is dropped and the next tick picks again. On the stair, a body more than 48 below floor 0 resolves through 3922 to the band that holds the point.

## Where a player can lose the floor

Fall. The finder would keep the upper region while the plan point stayed inside it. This tracker gives that region up once the body is more than 64 below its floor, then picks the highest floor under the feet. The landing mesh is the column plus the hop ball. A riser steeper than the 0.7 cut is left out of the column, which is the named fix for the Emperor-stair push-back. That steep triangle is present only when its region sits in the hop ball of the region just picked. A steep landing outside that ball is the hole inside the named replacement. The commit reports the Emperor route, including the door at the top of these stairs, as passing. This pass did not re-run it.

Tomb collapse. The oil test in the same commit turns every region on for one physics frame, then asserts the probe hits the lower floor near y = −90 and walks the body down. The live floor word is preferred when the nav quad is non-empty, so a written height moves the give-up test. The original writer that moves the body is still the open item in the note. The test is the evidence the landing is held. This pass did not re-run it.

Lift. The tracked region stays while the plan point is inside the quad. A lift that moves the region's collision shape keeps that shape inside the hop ball, so the physics floor moves with the shape. The column remembers triangle heights from the moment the grid is built. If the live floor word rises more than 64 above a body that was not carried, the tracker drops the region and picks again. The note left the original carry UNKNOWN. A negative pick leaves the previous collision set in place, so the set is not cleared to empty.

VERDICT: MERGE
