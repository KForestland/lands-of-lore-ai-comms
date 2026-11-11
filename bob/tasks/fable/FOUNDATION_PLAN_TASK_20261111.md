# Fable: plan the foundation tasks for Sol to build (owner, 2026-11-11)
Owner: "start the foundation tasks with Sol." Method: Fable plans, Sol builds, Kimi reviews. Plan only, no code.
Order (lead): 1) F-14 + F-15 together: one player-combat module (strike, reach, cooldown, damage) used by every host, and one owner of Luther's health (today: about 40 files with strike code, three health owners). Keep today's behaviour and numbers exactly, including the interim Act 2 scale (DEVIATIONS 0558) and the debug kill key; this is structure, not balance. Real numbers come later from Grok's I-03 / R-01.
2) F-16: an area host base where each level's owners register themselves instead of act2_map.gd's hand-written attach list.
3) F-06 (+F-07): one save for the whole game with 10 slots and autosave every 10 minutes and on entering a map (owner D3), including the native script state.
Deliver fable_lane/FOUNDATION_PLAN.md: for each, the contract, the exact files and functions with line anchors on r19-work d5da60a, a migration order in small commits that keep every test green, how old saves keep loading, the tests (real input where behaviour is visible), the risks, and what you could not confirm. Last line exactly PLAN READY. Plan 1 first and post it on the board as soon as it is done so Sol can start; then 2 and 3.
Not for Thursday's r19: these land after the owner's playtest build is cut.
