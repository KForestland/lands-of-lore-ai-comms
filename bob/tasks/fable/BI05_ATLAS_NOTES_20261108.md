# Fable notes 2026-11-08 — BI05 (Jungle sky slab + beam) and ATLAS-READABLE (Jungle first)

## BI05 meta duck
1. Problem: owner r18 F10 14-55-28/14-55-48 at (-741,-4356): a large flat rectangle with a forest-floor look standing in the
   view; 15-18-02 at (-4667,-459): a dark plank floating against the sky above the canopy.
2. Main chain: no (presentation), but the owner reports it on the Act 1 path; cheap to fix once identified.
3. Intent: *atmosphere*: open jungle under the sky; nothing hangs in the air.
4. Contract: the owner's three views show canopy and sky where the slab/beam were; nothing else changes.
5. EXACT: nothing. APPROXIMATE: which exporter spans are drawn.
6. Found (ray probe at the screen centre of the owner's poses, tmp/pose_capture.gd + LOL2_PACK): face 9149 (interior span,
   material 714, 107..147 over region 2449) and face 10313 (material 62, 127..147 over region 4544): textured "header" spans
   the exporter builds between two regions' nominal ceiling heights, drawn two-sided; neither region has a native ceiling
   (open sky), so the original has nothing to carry a header. My first attempt (narrowing the untextured edge fills) changed
   nothing at the poses: the untextured twins 8110/8111 were hidden behind the textured headers. Fix: jungle_review.gd
   skip_sky_headers (Jungle only): interior textured spans (index >= span_start, not appended source walls) whose foot
   stands on no floor vertex and whose own region and the region 6 units beyond both lack a ceiling face are not drawn;
   collision unchanged; 153 faces. The 159 headers beside a ceiling region (hut fronts above a door) keep drawing.
7. Proof: captures before/after at the owner's 3 poses + 7 landmarks (bi05_atlas_20261108/bi05_before_after.png): only the two
   artefacts change (river/village diffs are animated foliage/water pixels). tests/jungle_sky_headers_test.gd. Ledger 0340.
   Branch bi05-atlas b702c65 on r19-work 5b8c942 (worktree lol2_bi05); affected sweep 704 running.

## ATLAS-READABLE meta duck (Jungle)
1. Problem: owner after the r18 playthrough: "the map needs to be understandable and have edges and have points of interest
   like location and plot points". The Jungle Atlas showed a 420x200 dark box with one dot (atlas_readable_20261108/atlas_jungle_before.png).
2. Main chain: the Atlas is the player aid for finding the way (owner: maps first); readability is on the path.
3. Intent: *orient*: where am I, where have I been, where are the places I know of, which way is out.
4. Contract (ATLAS_READABLE_20261108.md): edges of the explored part (walls solid, openings as gaps, exits marked), named places
   once seen, plot markers for what Luther knows (clear when done), legend + player arrow + north; explored-only, no pause.
5. EXACT: nothing mechanical (modern aid). APPROXIMATE: all drawing; names (game text > hint book > longplay: the dialogue dump
   has no place names, so the Prima hint book ch.6 and the Journal's wording name the places; graded HINTBOOK).
6. Built (branch atlas-readable 79da1ed on r19-work, worktree lol2_atlas):
   - museum_atlas.gd: wall sides = creature_nav polygon sides without a linked neighbour OR toward a native impassable region
     (region_blockers/<AREA>.json; the Jungle's thickets are blocked regions, not missing neighbours - without this the explored
     area is one blob). Blocked regions are not floor. Linked sides stay open. Fit-to-explored on open; legend top-left; north;
     labels step aside from each other; off-map plot markers keep to the border.
   - atlas_places.gd: 11 Jungle places + 4 exits (museum road, Hive Caves, lizard tunnel, land bridge) with reveal radii and
     sources; 7 plot markers = Journal notes -> place + done quest path (gate note clears on jungle_village.local24).
   - museum_interface.gd: the Atlas page fills the room apply_ui_scale leaves (sheet sized in unscaled units so the fit lands on
     the UI scale), one title line.
   - Test: atlas_readable_jungle_test (rendered): new-game arrival -> M -> walk tests/fixtures/atlas_jungle_start_walk.json
     (tools/build_atlas_walk.py on the blocker-avoiding graph) to the clearing outside the gate -> M. PASS.
7. Proof for the owner: atlas_readable_20261108/atlas_sheet.png (before / arrival / after the gate walk with the Hive marker / full
   old-save area). Ledger 0341. Then other areas get their place tables.
Open: Journal "pins" do not exist yet (no pin feature in my_journal.gd), so none are drawn; plot "done" paths for the thieves
den/weapon shop use flags 17/253 and the den room field - to be confirmed against the state scripts when those chains are played.
