R107 review: opus/g05-classB-20261112, commits 73963ca + c66af82 (base 20c7797). Read-only; nothing run.
Note: during the review the shard_5 worktree was switched to opus/g05-classB-narrow-20261112 at 20c7797; I reviewed c66af82 by hash. Line numbers are in the c66af82 tree.

BLOCKER
B1. Whole-face keys and partial polygons are computed from STATIC floor heights, but scripts move floors on these levels (opcode 196; act2_progression.gd:118, 636: only the floor rides the deck, walls stay). A riser band below a raised floor stays solid after that floor comes down level with its neighbour. act2_map.gd:254 (keys), 258-273 (partials). Affected keyed faces: L12 15, L13 1, L14 38, plus partials L12 face 7384 and L14 face 10548. Concrete cases:
- L14 region 2291 (floor 340, groups 786/791/796/801 lower it to 190) joins 2684 and 2290 (both 190). Keys `wall|-176,1180|151,1180|190|340` (face 11697) and `wall|112,972|-137,970|190|340` (12314) wall it off for good: the lowered block cannot be crossed.
- L14 platform 2137-2142 (350, groups 590/591 lower to -10): 16 ring faces 11564-11580 (-10..260) stay solid, so the player cannot step on or off it at the bottom.
- L14 1019-1021 (200 -> 130 -> 0) and 53/62 (65/85 -> 0): faces 9743, 9745, 10079, 10085, 10087, 8276, 8277, 8284, 8308.
- L12 919-930 (-590 -> -1090, group 108): faces 6005-6016. L12 pit 2945 (0 -> -200): key 7414 plus partial 7384 seal region 3002.
- L13 lift 147 (-40 <-> -1040): face 2934 at the bottom.
Before the commit these stale drawn walls were walk-through. Fix: leave out every edge where either side is an opcode-196 region, or toggle them with the floor.

MAJOR
M1. No test added or changed in either commit; tests/registry untouched. The "0.0 -> 78.7 units" claim is not reproducible from the repo.
M2. c66af82 changes collision of every generic mover on every act2_progression level (L8-L20), not only the Citadel vault (act2_progression.gd:1038-1128; exclusions only at 1042-1045).

MINOR
m1. act2_progression.gd:1073 tests flatness only, not facing: an underside in the upper half (lintel) becomes a slab reaching 4 units into the opening (1113).
m2. A standable face in the lower half (cab floor under a roof) stays trimesh (1109-1111): the stuck case can persist there.
m3. Loader (act2_map.gd:248-256) fails silently and does not check the JSON's input hashes; a regenerated area.json silently drops keys. The generator is not on this branch.
m4. Rising floors (L14 2001, 2071, 2086, 2088, 2101, 2104: -100 -> 140 beside 150) leave a solid 10-unit lip.

Checked and sound
- Path: key -> edge_block_keys (254) -> region_edge_blocks (275) -> include_collision_face (235) -> jungle_review.gd:311-315. Owner claims are tested first (234). L10 OF6 code untouched.
- Every key matches exactly one face (0 dead, 0 ambiguous). Map sha in each JSON equals the area.json on disk.
- Keys on edges the nav lists as walkable: 0 / 0 / 0. File counts: L12 2022 no-neighbour edges + 412 raised-band edges; L13 829 + 163; L14 1876 + 960. Regions touched: 1912 / 716 / 1982.
- 10 sampled keys per file: all on edges without a nav link; 8 with nothing beyond, the rest riser bands whose top equals the higher floor (e.g. L12 6055 -310..-200 between floors -301/-201; L13 2979 -1140..-1040; L14 12241 340..428). None overlaps an opening with a step of 48 or less in the static state.
- Door-like movers: keyed faces beside L12 movers 69/72/73 are jambs, not across the doorway.
- Partials: 4-point convex, fan triangulation, two-sided, StaticBody3D layer 1 / mask 1, child of the map, rebuilt in _ready, not saved. Region-aware collision is L17/L19 only.
- Both metas are only read, never set or saved.
- Movers only yaw or translate, so slabs stay flat and ride the hinge (existing body_set_state sync). "MoverCollision" name kept; readers still valid (l16_dragon_mouth.gd:27, l19_sewer_forms.gd:188, act2_body_fit.gd:77, tests/act2_mover_case.gd:37, tests/l19_switch_shot_test.gd:60).
- Nothing in the diff outside the two purposes.

Cannot be judged without running
- Whether each B1 spot is on the required path, and whether body-fit pushes the player out.
- Native link versus coincident geometry for single raised-band faces (native neighbour table not in this branch).
- Slab seams, lips, creatures and projectiles against the new walls; the vault fix itself.

VERDICT: MERGE AFTER FIXES
