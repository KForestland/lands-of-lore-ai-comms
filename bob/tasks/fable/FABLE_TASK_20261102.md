# FABLE task 2026-11-02 (lead: Opus) - owner playtest fixes

Owner is doing a full playthrough on r12x today. Two owner F10 bugs, in this order:

1. ITEMS-HALF2-PICKUP (P0, yours from before): owner F10 2026-11-02 12:25:33 "cant pick up the eggs" in the night jungle L8
   at (-2433, 145). Report: AI_COMMS/playtest_feedback_20261023/report_2026-11-02T12-25-33_1932835883 (report.json + screenshot).
   Your items-half-2 rows (eggs, R-Manafoil, Cocos Cap, SS6/Gaunt strike/Orc shield) are placed but E pickup does not work in
   the rendered run. Fix E pickup for all of them; test at the owner coordinates (area_world_items_live_test rendered + a headless one).
2. JUNGLE-BACATTA (P0): owner F10 12:22:02 Jungle tavern (-1864,-4907) "the dialogue is wrong in the tavern and leads to hostile
   Bacatta". Owner rule: build from known behaviour (Bacatta friendly and leading after the Jungle); DEVIATIONS piece. Read the
   backlog rows JUNGLE-BACATTA and NPC-BACATTA and the Bacatta memories in docs/ first.

Worktree READY: ~/opus_work/lol2_pickup, branch pt-l8-pickup from r12y 56812f9 (qualified), generated media +
native_scripts + tmp host already staged. Commit with git -c user.name=fable -c user.email=fable@local.
CPU: owner is PLAYING - run tests at nice -n19 taskset -c 8-15 only (Astra 24-31, Grok 16-23). Rendered runs: Xvfb only,
never the owner's display :0.
Claim each row with python3 ~/AI_COMMS/BACKLOG/backlog.py (ITEMS-HALF2-PICKUP is lead-claimed: release/claim as fable),
post CHECKPOINT/READY on act1_completion_20261017/COORDINATION.txt, keep status/fable.md current. Lead integrates into r12z.
