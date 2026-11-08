# GROK list BI (lead: Opus), 2026-11-08 — r18 held-back owner fixes (BG07, BG15, BG26). After BH09.
Why: the r18b sweep (lol2_act3 r18-work 3b6a929: 705/726) failed 21 tests. Bisect (two copies: Grok-only vs merges-only)
put the main-path walk blocks on three BG commits. r18 ships WITHOUT them (branch r18-cut, reverts 67e6f64/4a2396f/5e606f5).
Base for the redo: lol2_act3 branch r18-cut (or r18-integration in lol2_r18). Re-apply your commit, then fix as below.
Rules as always: meta duck line, earned walks like a player (no placing at the goal, no E where none), ledger piece,
typed vars, registry json, RUN the affected tests (affected_tests.py --changed-since r18-cut) — the 20 listed in
lol2_act3/tmp/regressions/r18b/report.json must PASS.

BI01 (BG15 bramble walls, grok): keep the decoded rule (solid until 3 sword cuts / Spark; regrows after the timer).
  Brambles 103 (-3623, z 2158) and 109 (-3414, z 710) stand ON the earned routes: jungle_to_village waypoint 27
  (hive_quest_walk, kelsrick_inner_gate_walk, jungle_chief_hut_walk, dampen_prerequisite) and monastery_to_hive waypoint 80
  (hive_flute_return). The walks must CUT them like a player (aim + strike with the carried Fine Longsword; the broken-sword
  route too), then pass before the regrow timer. One shared helper in tests/ preferred over 8 copies. Also: jungle_props
  solid count (+9 bramble solids), and hive_route/hive_small_route expected packets (jungle_bramble initial).
  QUESTION FOR THE LEAD FIRST if any route cannot be cut (no weapon on that save): then it is a mechanics question for the owner.
BI02 (BG07 bridge decks, fable or grok): decks 223 (407, z -2430) and 224 (-1478, z -2543) as solid boxes stop
  dampen_knowledge/dampen_departure (shop walk at region 1189, (337, 7, -2387)) and the village escape (shop_to_gate point 61,
  (-1553, 7, -2515)). Find why the walker cannot get onto/past the deck edge (lip height vs the floor under it, box vs the
  source deck top) and make the deck walkable from its banks; keep "Human and Lizard do not fall through" (owner r17 16-54-13).
BI03 (BG26 boundary hedges, fable or grok): boundary_edges.json makes 2906 L8 source walls solid (all materials), which
  breaks l8_map (shell 21404 tris), l8_pit_earned (pit descent point0) and l8_tree_room / act2_temple_tree loops. Limit it
  to what the owner reported (hedge material 276 on neighbour-less edges, or narrower), prove the pit/tree walks still pass,
  and update l8_map's bound with the reason.
"[grok] BI<NN> DONE patch <file>" board line each (patches into grok_research/patches/R19/).
