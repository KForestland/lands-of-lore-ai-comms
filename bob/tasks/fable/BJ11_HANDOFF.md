# BJ11 handoff (Fable, 2026-11-09 late) - Act 3 walked like a player

- Worktree `~/opus_work/lol2_bj11r`, branch `bj11-act3-walk-r2`, head 5cff4a7 = r19-work b3e384e + 10 commits (rebase clean;
  ledger check PASS 491 pieces; godot_check 0). Staged from lol2_r18 + my liquid pack (fable_lane/bj11_20261109/liquid_L19_BC.json).
  Nothing pushed; not READY (no gate on b3e384e yet). Old worktrees lol2_bj11 / lol2_bk are history only.
- Tests: act3_walk_l17_test (registry 1060, PASS on c6a7b8e; rerun on b3e384e), act3_walk_l19a/l19b/l20 (unregistered survey
  sittings; LOL2_SURVEY=1 keeps walking past a stop). Ledger 0364 amended, 0386 (door-gap floors), 0387 (door 73 E bind).
- Sitting run on b3e384e (L19 from its arrival, tmp/act3_b1.log): horn OK; bars strike lifts Luther; gutter; three shots; flood.
  FIRST STOP = the blood pool channel wedge at (-180, 11, -1372), region 613 -> 18. SECOND = after the flood, (651, -3, -2081),
  the body floats over the raised channel deck and stalls before region 133.
- Next session, in order: (1) rerun l19b and l20 sittings on b3e384e (Grok's cab decks, east-lip shots, grate 52, 50/51 open bit
  are new there; my helpers call handlers directly - real clicks now exist upstream (BK08d), simplify player_click/player_use);
  (2) fix door_ahead aim order: pivot, then exit_objects[ref].position, then leaf centre (door 73 misses with pivot-only);
  (3) l19_bars_strike_test rose Luther to 10.94 not 12 with my branch on c6a7b8e - check pool/gap collision near region 40;
  (4) stage tmp/l16_dragon_room_earned_save.json for l17_cavern_run_earned_test; (5) gate: targeted tmp/gate_names.txt then
  affected sweep since b3e384e; format-patch to fable_lane/bj11_20261109/; READY.
- Mechanics for the lead (unchanged unless a rerun clears them): pool wedge (Human radius 15 vs 24-30 wide native channel);
  float/stall over the raised channel after the flood (liquid bank surface vs 196 deck); rapids low area regions 760-759 with
  20 units clearance (no body fits; act2_map has no crouch); L20 birth save "Absent creature has live state"; door 73's kind-4
  group is opcode 7 (unhosted). To re-verify on b3e384e: cab -> ring step, 64/65 and 53/54 E, L20 doorways, pillars from the lip.
- Details: fable_lane/bj11_20261109/NOTES.md, memory lol2-bj11-20261109.
