# Fable 5.2: map out how to complete the rest of Lands of Lore 2 (owner, 2026-11-10)
Owner: "Give Fable 5.2 the task of mapping out how to complete the rest of the game, the best way to do it, and write up all the tasks needed to be done. The main rule is to have the classic, but if it is too hard, modernize."
Method: Fable plans, the lead (Opus) and the lanes build. You change no game code. Read-only; if a fact needs a run, at most 1 Godot from a temporary worktree, MemAvailable >= 10 GiB.

Deliver ~/AI_COMMS/fable_lane/MASTER_PLAN_COMPLETE_GAME.md, last line exactly: PLAN READY
and ~/AI_COMMS/fable_lane/master_tasks.json (proposed tasks; the lead imports them, do not edit BACKLOG/backlog.json).

Scope: LoL2 Classic from today's r19-work to a finished, releasable game. Enhanced Edition and LoL3 only where they constrain a choice.

The plan must answer:
1. Where the game really stands, area by area and system by system, from the code and tests, not from task counts. "Built" and "a player can do it" are different things; say which.
2. The best way to finish: phases, order, what can run in parallel, and why. What would you change in how we work?
3. Every task needed, including work missing from the backlog. Triage the 566 open backlog rows: keep, merge into a batch, or drop with a reason. Group look-alike work (165 items, 31 spells, 45 creatures, 153 review rows, 53 test rows) into batches rather than one row each.
4. Classic-or-modern call per task under the owner's rule. Classic is the default. Define when something counts as "too hard" (a time-box and evidence), and give the modern fallback in advance so nobody stalls.
5. Decisions only the owner can make, listed plainly with a recommendation. Gameplay changes go to the owner.
6. Effort per phase and an honest range for the finish date, with what would move it. Top risks, and what you could not confirm.

master_tasks.json: a JSON list of {id, title, area, phase, batch, depends, lane, size (S/M/L), classic_or_modern, fallback, acceptance}. Acceptance means what a player can do, proved by an earned real-input test.

Inputs: AI_COMMS/BACKLOG/backlog.json and BACKLOG.md; lead_notes/DECISIONS_AFTER_FABLE52_REVIEW_20261109.md; fable_lane/REVIEW_FABLE52_20261109.md; your BJ13_PLAN.md; grok_research/BK17_main_chain_stops_20261110.md; docs/DEVIATIONS.md; the hint book and Brady guide (AI_COMMS/reference*); kimi_K66 "not yet" list.
Owner's standing direction: maps -> main quest chain A to Z -> items (all in one pass) -> RPG -> dialog -> small stuff, with sound and combat last, and playtests are the check. Every original bug gets fixed. No invented caps or timers; known behaviour is built directly and only unknowns are decoded; hard map details may use a logged adapter that matches the longplay; mechanics changes go to the owner. Machine limit: memory, not cores (Sol 6, Grok 2, Fable 2 Godot; MemAvailable >= 10 GiB).
Use the owner's recent screenshots if useful: ~/Downloads/LoL2_P*.png (Parts 1 to 5, list in LoL2_screenshots_rename_list.csv).
