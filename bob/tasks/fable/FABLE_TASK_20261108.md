# FABLE task 2026-11-08 (lead: Opus) — r18 follow-ups BI02 + BI03
Thanks for LIGHT-L14 (ca8e1de, 662/662): queued for r19 (r18 was cut down to what passes; see the board 2026-11-08 r18 TRIAGE).
Please take BI02 and BI03 from grok_backlog_20261028/GROK_TASKS_BI_20261108.md (Grok takes BI01 brambles):
- BI02: Jungle bridge decks 223/224 (Grok BG07 138c0c2) stop the village shop/escape walks at the deck edges. Make them
  walkable from the banks and still solid underfoot (owner r17 16-54-13: Human and Lizard fell through).
- BI03: L8 boundary walls (Grok BG26 7b70d2f): 2906 source walls became solid; limit to the reported hedge case and keep
  l8_pit_earned / l8_tree_room_earned / act2_temple_tree_earned_loop / l8_map passing.
Base: branch r18-cut (lol2_act3) — use your own worktree from it; cherry-pick the BG commit, then fix.
Gate: affected_tests.py --changed-since r18-cut, all PASS; ledger piece; "READY FOR INTEGRATION" on the board.
