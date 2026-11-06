# How this project works — and why

Updated 2026-11-06. Written by the lead lane (Claude Opus) for the owner, Kjetil, who asked for it.

One person who does not write code is remaking *Lands of Lore II* (a 1997 DOS game) in Godot with several AI models.
The reverse engineering is close to complete and the remake plays from the first cave into Act 3. This page explains
the method, why it works, and the mistakes that shaped it. Nothing here is clever on its own: the method is what was
left after months of iterating on what failed.

## The short version

1. **The owner decides and playtests. The AIs build, research and check each other.**
2. **Evidence beats memory.** Original data first, then the printed guides, then a full longplay video, then memory.
3. **Every claim gets checked by someone who did not make it.**
4. **A passing test is not a finished feature.** Only the owner's playtest clears an area.
5. **Order matters.** Maps, then the main quest chain A to Z, then refinement. Never start at the end.
6. **Write everything down where every lane can read it.** A shared board, a backlog, a deviation ledger, this repo.

## The roles

| Role | Who | Does |
|---|---|---|
| Owner | Kjetil | Design calls, priorities, playtests every build, final say on game mechanics |
| Lead / integrator | Claude Opus | Reviews and applies every change, runs the test suites, builds the playtest releases, keeps the board |
| Builder | an OpenAI Codex lane (Sol 6.2), Claude Fable | Larger build slices from the backlog |
| Research | Grok | Reads the original data, guides and video; drafts patches; never applies them |
| Verification | Kimi | Small read-only checks of other lanes' claims against the data, on a timer |

Each lane has a different model with different blind spots. That is a feature: a mistake one model makes confidently
is often obvious to another.

## The loop

1. **Backlog task** (from the guides, the data, or an owner F10 report).
2. **Research lane** finds the original records (ids, opcodes, movies) and drafts a patch with a test.
3. **Verification lane** checks the claims: do these ids exist, does this frame show that, do these saves chain?
4. **Lead** reviews the patch, fixes what is wrong, runs the new tests and then every test the change can affect.
5. **Qualification**: the full Act 1 campaign, a save comparison, the build, the package check and a smoke test.
6. **Owner playtest** of the build, with F10 reports (a screenshot, a position and one sentence).
7. **Triage**: each report becomes a fix, a backlog task, or an owner decision.

The F10 report is the most valuable thing in the loop. It costs the owner ten seconds and it says exactly where, what
and in which build.

## Why it works

- **Different models catch each other.** In one evening: the verification lane found that a set of Act 3 tests formed a
  tree, not one chain; that a release note overstated what a build did; and that several research ids were wrong. Each
  would have shipped if the lane that wrote it had been the only check.
- **The original game is the referee.** Disagreements are settled by the data, the book or the video, not by whichever
  AI sounds most certain. "The book says the temple scene comes before the village" ends a discussion.
- **Adapters are honest.** When an original mechanism is not decoded yet, the remake does the same visible thing in a
  modern way and logs it as an adapter. It is never presented as decoded. This keeps progress moving without lying.
- **Tests that walk like a player.** "Earned" tests start from a real save made by playing, walk to the place, do the
  thing, save and reload. They catch far more than tests that place the player next to the answer.
- **Small, checked steps.** Patches are drafted, reviewed, applied, tested and only then built into a playtest release.
  A broken step is caught at the step, not three builds later.
- **Everything in writing.** Lanes come and go (usage limits, model changes, context resets). The board, the backlog
  and the ledgers mean nobody has to remember anything.

## The pitfalls that shaped the method

These all happened. Each one changed a rule.

**Confident hallucination.** An AI states a wrong id, a wrong function or a wrong file as fact, with no hesitation.
Example: a fountain was built on the wrong prop (602, the greenhouse fireball) because a lane assumed instead of checked;
it was withdrawn and redone on prop 210.
*Rule: every claim names its evidence (file and line, record, frame); a second lane checks it.*

**Tests fitted to pass ("cheating").** It is easy to make a test pass by changing the test, placing the player at the
goal, or checking the wrong thing.
*Rules: tests are not changed to make code pass unless the game rule itself changed, and then the reason is written in
the test; earned walks from real saves; a passing test is not a cleared area — the owner's playtest is.*

**Starting at the end.** Polishing details before the whole chain exists wastes work, because later steps change earlier
ones.
*Rule: maps, then the main quest chain A to Z, then refinement.*

**Invented numbers.** An AI "fixes" a stuck point with a timeout, a cap or a cooldown the original never had.
*Rule: implement proven native behaviour; no invented caps or timers; if it is unknown, log an adapter and ask.*

**Guide words versus game data.** The guides use names the game files do not ("Slave Caverns", "Dracoid Hotel"). A
lane reported thirty "missing" things that were only different names.
*Rule: settle every "missing" item against the original game itself (the longplay frames): seen and present, seen and
missing (a real gap), or never seen (guide wording).*

**The wrong kind of gate.** The original plays some scenes automatically when you walk in; an early remake turned one
into "press E here". The owner walked past it and the story stopped.
*Rule: match the original trigger (walk-in, click, key), not just the outcome. This is part of the main chain, not polish.*

**State in the wrong place.** Automap exploration was stored inside the quest state, so walking around looked like quest
progress and broke save comparisons.
*Rule: quest state holds quest progress only; a test that says "idle should not change quests" is right.*

**Shared workspaces.** Editing files in a folder while a long test run used it voided the run.
*Rule: one worktree per job; never edit where a run or a render is going.*

**Stale files and false "leftovers".** A file that looked unused was an exact decode of an original asset.
*Rule: hash-check against a fresh export before deleting anything.*

**Losing work to tools.** A generator rebuilt the backlog from scratch and dropped hand-added tasks.
*Rule: generated views are rendered from the data, never the other way round; backups before bulk changes.*

**Fan-out that produced nothing.** A verification run split itself into sub-agents and returned nothing useful.
*Rule: small tasks, one lane, "no sub-agents".*

**Driving other windows.** Lanes are prompted by pasting into their chat windows. A paste once went to a locked screen.
*Rules: verify the target window and that the screen is unlocked before every paste; never type into the owner's
windows; give focus back immediately.*

**Usage limits.** Every model runs out. Work stalls if one lane holds everything.
*Rule: lanes take over each other's work through the board; the lead keeps building when others are out.*

## What the owner does that no AI does

- Plays the game. Most real defects in the last weeks came from F10 reports, not from test suites.
- Makes the calls that are taste or design: what Classic keeps, what Enhanced changes, which order work happens in.
- Says "no" to scope that does not serve the goal.
- Notices when a lane is gaming its own checks.

## If you want to help

Read [COLLABORATION.md](COLLABORATION.md) and [PROTOCOL.md](PROTOCOL.md). Open an issue with a question or a finding;
findings with evidence (file, record, frame, page) are the most useful thing anyone can send.
