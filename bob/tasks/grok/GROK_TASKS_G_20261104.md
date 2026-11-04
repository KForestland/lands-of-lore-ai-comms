# GROK tasks G 2026-11-04 (lead: Opus) — Act 1 Hive puzzles, read-only

Owner is sick/resting; lead builds r15 (branch act1-missing: dragon click, Cave lever prompt, Bacatta prompt, Hive lift
starts at bottom). These two owner F10 beats need research before the lead builds them. No Godot. Claim/done with
BACKLOG/backlog.py + one board line each. Time-box each ~60 min; write what stays open.

G1. HIVE-4-BUTTONS (owner F10 17:43:48, Hive native (-3509,7128), region 753). Lead decode (L5_HC.json stream 1):
    Lock L1 = control 116, L2 = 115, L3 = 114; kind-3 records keyed on each lock's own +0x25:
    L1: 0->1 (g6676); 1-> L3=1, L1=2 (g6698); 2-> reset L3,L2, L1=1 (g6726).  L3: 0-> reset (g6408); 1-> L2=1, L3=0, L1=0 (g6436).
    L2: 0-> reset (g6532); predicate 25 '0603080500' (op6 both-nonzero: local[8] AND right type 5) -> g6560/g6632:
    op198 local16 (Spout_2) = 0, op196 region 760 'c490f8021cfc001400000000', sound 0x2bd on prop 79.
    => order L1, L1, L3, L2.  OPEN: (a) who writes local 8 (no op198 index 8 in L5_HC; other levels? loader?);
    (b) what op196 on region 760 does in play (floor -1011 -> -996?) and what it unlocks; (c) what Spout_2 is
    (group 3700 from prop 293 kind-6 sets it to 5: op204 x5 on regions 0x370-0x374, op196 region 884, op208);
    (d) the top-floor clue: glyph controls 117-120 near (-1859..-1886,7696) region 283 — find them in the longplay
    frame index and describe what they show. (e) Is this puzzle on the required A-to-Z path or optional?
G2. HIVE-BOULDER-CELLAR (owner F10 17:45:07/36, Hive native (-3345,6074)): a boulder falls from the wall, breaks the
    floor and opens a hidden cellar. Find the native records (region/movable/prop near that point, the falling boulder,
    the floor-break opcode), the longplay frame time, what is in the cellar, and whether it is required.
Answer in grok_research/hive_buttons_g1.md and hive_boulder_cellar_g2.md.
