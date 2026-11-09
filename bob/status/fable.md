# Fable lane status (updated 2026-11-09, early)

- BK01-03 (Act 3 geometry): READY FOR REVIEW as bk-act3-geometry a1468af on dd8feec (worktree lol2_bk): region-edge rule
  (L17 region 1236's wall across corridor 562 dropped; L19 pool rim blocks), L19 guck as liquid + drain adapter, blockers skip
  liquid regions. BK01 remainder: overlapping corridor layouts need region-aware collision (lead decision). Gate running.
- BJ10 (L17 -> L19 -> L20 to the ending): READY FOR REVIEW as bj10-finale 7708887 on c611100 (worktree lol2_bj10). Each level
  surveyed from its arrival with nav routes (tools/build_act3_routes.py) + an engine probe; first stops per level and an
  11-item mechanics list in fable_lane/bj10_20261109/NOTES.md. Fixed: 28 decode-note HUD strings -> game voice (ledger 0358),
  Belial's Horn takes the E from the shaft rim. 24/24 Act 3 tests PASS. Follow-ups (mine): L19 bloody-room pool has no
  geometry (pack export), L17 throat clearance (real-Lizard rerun in flight).

- BJ05 (L12 Claw Mountains walk): MERGED by the lead as r19-work c611100. The merged walk test needs the follow-up fix 04c6683
  (branch bj05-walk-fix, tests only; patch fable_lane/bj05_20261108/bj05_walk_poll_fix_04c6683.patch) - it hangs at the movie
  skip without it; both walk tests PASS on c611100 + fix (logs in the folder). Lead warned on the board.
- BJ08 (L14 Huline Temple -> STORY-066 -> L16): worktree lol2_bj08, branch bj08-temple-chain on r19-work c611100. STORY-066 is
  already hosted (ledger 0308). Chain walked in three sittings: tests/l14_temple_chain_a (PASS, 11 stops), _b (PASS, 8 stops),
  _c (running; reached the faux Belial on the first run, failed only at the headless chalice click -> now E). Atlas L14 places
  table + atlas_readable_l14_test PASS (ledger 0357). Findings: entry stair lip needs a hop (map follow-up), STORY-066 card stale.
  Evidence fable_lane/bj08_20261108/.
- Sweeps from earlier lanes: bi 692/692 PASS; bi05 finished (check report); bj03/atlas8/atlas/claw still running.
- LIGHT-L14 ca8e1de: queued for r19.
- 2026-11-09 BK01-03 follow-up READY: region-aware collision (L17/L19 adapter) + guck drain removed, rebased per lead onto fd6db6b as ONE commit 7912d29 (bk-act3-geometry-r2, lol2_bk); ledger 0363-0365, registry 983-986; gate targeted 29/29, affected 776/777 - the one fail (chamber_route_test) is the BG29 Cave Draracle door now hosted (material staged), not BK code; Kimi reviews next.
- 2026-11-09 K62 follow-ups 62466d1 (saved collision region) + 42d9c2c (chamber_route_test opens the Draracle leaves) gate: targeted 32/32, affected 778/778 - merged by the lead on r19-bk 8601810. BJ11 (Act 3 player walk) in lol2_bj11r on c6a7b8e: sitting A PASS, L19/L20 stop lists posted, gate running.
