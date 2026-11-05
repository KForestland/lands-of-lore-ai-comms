# H19 Ruins no-clip reports and the wall faces

The owner report has no coordinate. The faces that were missing are the L9 bit0 pack, not one walked quad.

## The report

`TRIAGE_20261102.md`: owner chat, L9 Ruins, many walls are no-clip, trapped once. Backlog `PT-L9-WALLS`, priority P2. No F10 position was stored. The 2026-11-03 triage's only "clipped through" row is the cave boxes at Godot (532, −12371), which is H16, not the Ruins.

`grok_research/l9_walls_card.md` and `grok_research/f10_triage_20261102.md` repeat that the wall-trap F10 has no position, so no region was bound to it.

## The faces

On r12x and r12y the card's reading of `dragon_level.gd` was `region_blockers_enabled` false, and `include_collision_face` kept floors and ceilings only. L9 never set `source_wall_kind_collides`. The drawn walls (14500 source-wall records, 12006 rendered) are the picture. They are not the movement solid.

The unused pack, from the same card:

- L9 geometry has 6829 regions. 179 have word +0x1C bit 0.
- 125 of those are the static blocked set, 116 edges.
- 79 are opcode 197 dynamic regions, 243 dynamic edges. 54 of the 79 also start with bit 0.

`docs/l9-region-walls.md` in `lol2_r14` says that pack is now enabled: 125 static regions and 116 edges stay on, and the opcode 197 binder owns all 79 dynamic regions. `scripts/lol2/dragon_level.gd` line 36 sets `region_blockers_enabled = true`. The same doc names one dynamic face the qualification actually hit: region 3565, around x 1892, cleared by offering group 12766 opcode 197 arm 2. That is the statue-follow wall, not the owner's trap. The doc says no owner-playtest acceptance was claimed.

## Opens

- Which of the 125 static regions was the wall the owner walked through. The report never gave a point.
- No longplay frame was opened.

## Grades

The triage row is the owner report. The counts and the flag are the card and the r14 script line, read this pass. Region 3565 is the qualification note in `docs/l9-region-walls.md`. FRAME open.
