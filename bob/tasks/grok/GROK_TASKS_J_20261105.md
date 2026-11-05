# GROK task list J — maps to 100% first (owner order 2026-11-05), lead: Opus

Read-only, no Godot. Output grok_research/J<NN>_<slug>.md, one "[grok] J<NN> DONE" board line each, status/grok.md current.
New owner F10 reports go first. The lead fixes; you give exact specs (native ids, material/texture keys in the staged packs
under ~/opus_work/lol2_act3/assets/lol2/generated/, region/face numbers, what the original shows: longplay frame).

## A. Fix specs for every MAP_GAP_LIST.md row (one file per row)
J01 L1 Cave 17-03-39 wall clip + boxes cannot be moved (region 1081, control 121): what wall the player passed, which
    face is missing collision, and the crate-stack mechanism (H16 overlap).
J02 L3 Museum 17-14-40/52 gates wrong colour / no texture (region 1057): which gate objects, which texture resource the
    original uses, what the pack draws now (material key or none).
J03 L4 Jungle 17-16-55 chopped tree missing its top (region 1714): the tree object, its parts, which part is not drawn.
J04 L4 Jungle 17-26-29 "brick box in the distance" (region 2122): what object it is and whether the original shows it.
J05 L4 Jungle 23-04-55 bridge-sequence missing textures (region 4399): which faces lack a material.
J06 L5 Hive 17-41-10 texture jumping on a flat roof (regions 265/269): z-fighting faces? give both faces and heights.
J07 L5 Hive 17-42..43 clipping walls (x -3689..-3507, y 7143..7394): which faces/regions overlap.
J08 L5 Hive gas does not flow / not transparent; green stuff glitches: which material/animation, the original's look.
J09 L4 Jungle 17-55-53/56-12 bright texture in the sky: find the face (sky-facing material) and what it should be.
J10 L14 Temple 18-01 textures/geometry wrong window (x 2625..2884, y 2698..3375): after the lead's portal visibility
    (act3-story 44a6d98) which faces are still wrong; compare with longplay g_262..g_286.

## B. Clipping audit for portal visibility (the Temple fix, other areas next)
J11 For every area pack (maps/<AREA>/area.json and the Act 1 packs), list region pairs whose floor polygons overlap in
    x/z AND whose floor-ceiling ranges overlap or nearly touch (stacked/overlapping rooms). Rank areas by count: the
    lead turns portal visibility on where it matters most.
J12 Areas whose original clears to black (indoor) vs shows sky, per region band (from the longplay), so the black-void
    background can be set per area/region.

## C. Atlas v2 support (ATLAS_AND_CODEX_PLAN_20261105.md, owner decisions section 8)
J13 Storey grouping per area: propose floor bands by height AND connectivity (ramps stay one storey); give the counts.
J14 For each area: the regions that are niches/alcoves/Lizard-only cracks (the book says the automap shows them).

## D. Then (only after A-C)
J15 Opcode 18 flag 0x0812 native drift speed (your proposal).
J16 GROK_STANDING_IDLE.md loop.
