# Fable lane status (updated 2026-11-08, ~22:30Z)

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
