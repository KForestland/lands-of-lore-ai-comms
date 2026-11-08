# Fable BI02 + BI03 notes (2026-11-08) — Jungle bridge decks, L8 boundary hedges

Task: AI_COMMS/fable_lane/FABLE_TASK_20261108.md (lead Opus), items BI02/BI03 of grok_backlog_20261028/GROK_TASKS_BI_20261108.md.
Worktree ~/opus_work/lol2_bi, branch bi-decks-hedges = r18-cut f4aa7c1 + cherry-picked BG07 138c0c2 + BG26 7b70d2f + fixes.

## BI02 meta duck — bridge decks 223/224 (Grok BG07)

1. Problem: BG07 made the stream decks 219/221-224 solid boxes (owner r17 16-54-13: Human and Lizard fell through). The r18
   bisect: decks 223 (407, -2430) and 224 (-1478, -2543) stop dampen_knowledge/dampen_departure (magic-shop walk) and the
   village escape (shop_to_gate point 61).
2. Main chain: yes (village escape, shop walks).
3. Intent: *orient/atmosphere*: plank bridges over the streams; the player walks on them.
4. Contract: Human and Lizard stand on a deck they walk onto; the earned walks along the stream still pass.
5. EXACT: nothing mechanical. APPROXIMATE: the collider shape.
6. Measured (tmp/deck_probe.gd, rendered on Xvfb :97): the fixtures' routes run ALONG THE STREAM BED (floor -25; regions
   1189/1192/1197 under 223, 1085 under 224). Deck tops: 223 = 11, 224 = 10 (source h + height). From the banks (floor 0)
   the step is 10-11 and the Human walks on and off the deck already (to_monastery leg: feet 9.5 -> 11 -> -11). From the bed
   the lip is 35-36 > the 32-unit step (walk_step.gd), so the Human stops at the deck's LONG side (hit normal = -side axis).
   The Lizard (8 tall) crawled under 224 (26 clearance). Options: (a) raise the global step to 36: invented, global risk;
   (b) reroute the fixtures around the decks: the stream bed is the corridor the route builder found, the deck covers it;
   (c) ramps: collision-only skirt from the deck top down and out on every side -> a body on the bed climbs onto the deck
   and walks off the far side. Chosen (c): ConvexPolygonShape3D prism, top = source box top, base = footprint + 60 per side,
   40 lower (34 degrees, inside the 45-degree floor limit). Drawn deck unchanged. RAISED_DECKS (227) keep the box (beast
   walks under). Logged as adapter (ledger 0339).
7. Proof: tests/jungle_bridge_bank_walk_test.gd walks the real fixture points over 223 (both ways) and 224 as Human and
   Lizard and asserts feet on the deck top while inside the footprint; Grok's jungle_bridge_walk_earned_test (crossings on
   top) + jungle_props_test (solid count) + the three walks that failed in r18b.

## BI03 meta duck — L8 boundary hedges (Grok BG26)

1. Problem: BG26 (owner r17 17-59-34, hedge at (1842, 2499), face 8693 material 276, region 1389 edge 3) put every source wall
   on a neighbour-less edge on the movement body via assets/lol2/generated/darker_jungle/boundary_edges.json (2952 edge
   keys, 2906 of the pack's 5101 wall records, 43 materials). r18b: l8_map (shell 21404 tris), l8_pit_earned (pit descent
   point0), l8_tree_room_earned / act2_temple_tree loops fail.
2. Main chain: yes (L8 pit -> Ruins, tree room, temple path).
3. Intent: *orient*: the hedge is the edge of the world; the player may not leave the map through it.
4. Contract: walking into the boundary hedge stops; every path beside/through the jungle still walks.
5. EXACT: nothing mechanical. APPROXIMATE: which drawn walls collide.
6. Measured: the neighbour-less set is not the map boundary — the pit descent itself crosses hedge face 10432 (material 276,
   region 2811 edge 0, 'neighbour-less', with the pit shaft floor at -520 beyond it), and the tree-to-temple walk crosses
   884 curbs (-30..-16) on such edges. The region neighbour words are not fully decoded (same class as the Hive unbound
   faces in MAPFIX). Narrowed rule: material-276 hedge on a neighbour-less edge AND no floor polygon of another region
   (any height up to 60 above the wall foot; a hole counts) within 60 units beyond it -> 118 of 139 such hedges; the owner's
   8693 is in, 10432 (pit) is out, the linked hedge 6959 stays open. Producer tools/prepare_l8_boundary_hedges.py
   (inputs: the pack's area.json + Grok's boundary_edges.json; exit 2 on mismatch) -> TRACKED scripts/lol2/l8_boundary_hedges.json;
   darker_jungle.gd reads that file, the gitignored generated boundary_edges.json is no longer read at run time.
   None of the three failing walks' fixture legs crosses a kept hedge (2-D check, tmp/boundary_analysis.py).
7. Proof: l8_boundary_hedge_test (Grok's, unchanged), l8_map (bound = 2 x (non-wall faces + boundary hedges), reason in
   the test), l8_pit_earned, l8_tree_room_earned, act2_temple_tree_earned_loop, then the affected sweep.

## Housekeeping
- BG07's ledger piece is numbered 0323 (row); my light-l14 (queued for r19) also has 0323-text. The lead renumbers one at merge.
- Ledger row 0338 (BG26) text updated to the narrowed rule (the first-cut rule is wrong as stated); new row 0339 for BI02.
