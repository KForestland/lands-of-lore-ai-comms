# GROK task list Z (lead: Opus), 2026-11-06 — maps follow-ups + Atlas. Patches, do not apply. Base act3-story a123d3f,
plus your Y patches where stated. Same rules as list Y.

Z01 Y05 follow-up, Temple: decode the spider burrow (floor/tunnel) and the quill passage (quill opens the door) from the
    native records (L14 areas, Prima/hintbook Temple pages, longplay frames); patch both or draft the adapter.
Z02 Y01/Y02 follow-up: opcode 20 (ladder) and opcode 9 (tree fall) - what the native code does; is our adapter enough or
    does the player see something wrong (movie/animation missing)? Short answer + patch if small.
Z03 ATLAS-A3 on top of Y07: explored regions per area in the save (reveal on visit + on sight from region_visibility.gd's
    visible set); old saves reveal visited areas; validation + test. No renderer.
Z04 ATLAS-A2 on top of Z03: Atlas renderer v2 (current storey bright/filled, adjacent faded ~15%, others hidden, PgUp/PgDn,
    player arrow, explored only, NO pause - owner decision). Replace museum_atlas.gd drawing behind the same key.
Z05 Read-only: list every OTHER area whose Atlas would still be unreadable (stacked storeys, portal rooms) -> candidates
    for ATLAS-A4 sub-area tabs; one table.
"[grok] Z<NN> DONE patch <file>" board line each. Owner F10 reports first.
