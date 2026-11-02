# PROJECT ORGANIZATION — Lands of Lore: Two Tracks
## How the build and the stories fit together, and what to do when

---

## THE TWO TRACKS

You are running two projects that share lore but not a timeline. Keep them
separated in your head and in your folders — mixing them is where confusion
starts.

| | Track A: Chronicles of Time | Track B: Chronicles of Souls |
|---|---|---|
| **What it is** | The build — LoL I, II, III remade in Godot, unified by Asynchronia | The stories — original LoL IV, V, VI concepts, unified by the same structural pattern |
| **Status** | Actively building, phase-gated, technical docs complete | Concept-stage prose, no build docs yet |
| **Who works on it** | Codex (orchestration) + Claude (sub-agents), following `MASTER_OVERVIEW.md` | You, writing — AI can assist drafting but this is not agent-driven yet |
| **Blocking dependency** | None — proceeds on its own phase gates | Nothing blocks it from being *written* in parallel; it should not be *built* until Track A ships |

**"Modernized Lands of Lore 1"** is Track A, Phase 2 (`03_PHASE2_SCOTIA_FULL.md`).
It's already scoped — nothing new needs organizing there. It happens after
Phase 1 (demo) is tagged, and before Phase 3 (Luther / LoL2).

---

## TRACK A — CURRENT STATE (unchanged, for reference)

Phase gates from `MASTER_OVERVIEW.md`:

1. `v0.1-scotia-demo` — Gladstone Keep + Northland Forest demo
2. `v0.2-scotia-full` — **← "modernized LoL1"** — full Scotia campaign
3. `v0.3-luther-full` — **← "LoL2"** — Luther, three spheres
4. `v0.4-copper-full` — LoL3 — Copper, portals, guilds
5. `v1.0-chronicles-complete` — unification, Asynchronia, 12 endings

`NARRATIVE_TODO.md` already correctly queues dialogue for Phases 3–5 and
keeps it out of code — that pattern is working well. No changes needed here.

---

## TRACK B — WHAT NEEDS ORGANIZING NOW

### Problem: LoL4 has no canonical version

Right now `lore_4`, `lol4`, and `lol4_locations` are three drafts of the same
story with real content differences:

- `lore_4` — the original narrative outline, includes the Copper LeGré exile
  subplot and Draicele city, written as flowing prose
- `lol4` — a restructured "AI agent" GDD version, same story, formatted for
  prompting, but written *before* the Copper/Draicele additions were folded in
- `lol4_locations` — an expansion pass adding four new zones (Last Haven,
  Whispering Canyons, Crystal Soul Caverns, Azure Spire), references "v1.0"
  and "v1.1" but was never merged back into a single master file

If an agent (or you, months from now) opens the wrong one, you get an
inconsistent story. This needs one canonical file with everything merged and
a changelog at the top, the same discipline `02_PHASE1_SCOTIA_DEMO.md` uses
("Corrections applied: ...").

### Recommended folder structure

```
/narrative/
  /chronicles-of-time/          (Track A — leave exactly as-is)
    NARRATIVE_TODO.md

  /chronicles-of-souls/         (Track B — new)
    00_MASTER_STORY_BIBLE.md    <- canon lock: characters, timeline, locked facts
    01_LOL4_SEEDS_OF_THE_ANCIENTS.md   <- merge of lore_4 + lol4 + lol4_locations
    02_LOL5_SHADOWS_OF_THE_WESTERNLANDS.md
    03_LOL6_THE_SHINING_PATH.md
    04_CHRONICLES_OF_SOULS_UNIFICATION.md
    NARRATIVE_TODO_SOULS.md     <- mirrors the Track A pattern
    CHANGELOG.md                <- one line per revision, dated
```

Every story doc gets a version number and a one-line changelog entry at the
top, same as your technical docs already do. That's the fix — it's a
formatting discipline, not new content.

### Continuity notes worth locking early (found while reading)

- **LoL5** picks up after LoL4, with King Richard dead and Copper retired —
  this only makes sense if LoL4's "good ending" (Copper returns to Gladstone)
  is the one being treated as canon going forward. Worth stating that
  explicitly in the Master Story Bible so LoL6 doesn't quietly assume a
  different ending.
- **LoL6** introduces "Queen Eina Ashveil" and the Chronowalker/Echo Stone —
  these connect back to LoL5's Varen Ashveil thread. Good sign the throughline
  is intact; just make sure the Master Story Bible captures the Ashveil
  lineage once, rather than each doc re-deriving it.
- **Chronicles of Souls** (the unification doc) explicitly names the seven
  structural elements it's borrowing from Chronicles of Time. That's your
  best anchor document — it's the one place that states *why* IV–VI belong
  together, and it's worth keeping it short and canonical rather than letting
  it grow like the LoL4 docs did.

---

## SEQUENCING — WHAT HAPPENS WHEN

| Now | Track A continues (Phase 1/2 build) — top priority, unaffected |
|---|---|
| **In parallel, low-effort** | Consolidate the LoL4 drafts into one canonical file. Pure writing/editing, no agent time needed, fixes a real problem before it compounds. |
| **After LoL2 (Phase 3) ships** | Start structured story development on Track B in earnest — Master Story Bible, then fill gaps in LoL5/LoL6 (both are explicitly marked as drafts needing fuller character work) |
| **Do not start until Track A Phase 5 ships** | Any *building* of Chronicles of Souls. Same phase-gate discipline you already enforce elsewhere — writing ahead is fine, building ahead is the scope-creep risk. |

---

## FAN / WORKFLOW SHARING (for later, flagged not detailed)

You mentioned wanting to maximize fan support and share the workflow once
LoL2 is done. Worth deciding in advance which of these you're aiming for,
since they lead to different prep work:

- **Share the finished game + dev diary** (lowest effort, highest reach)
- **Share the workflow/pipeline itself** (asset extraction scripts, agent
  prompting setup) so other fans can build their own remakes — this needs
  the technical docs cleaned of anything project-specific before publishing
- **Open the story bible to fan input** on Chronicles of Souls specifically,
  since that content is original (not derived from Westwood material) and
  is the one place community co-writing could work without IP concerns

Happy to build out whichever of these you want next — the Master Story Bible
merge, or the fan-sharing plan.

---

## CONCEPT PACKS (added 2026-09-20)

Games 4–6 are **new games, not Classic editions** — "Classic" means Lands of
Lore 1–3 only. Each new game gets a concept pack outside this folder, built
the same way: story spine, world and routes, art direction, then (after the
user's decisions) room graphs, dialogue, quests and a systems checklist, plus
a human review document in Word/Google Docs format with a decision table.

| Pack | Location | Status |
|---|---|---|
| LoL IV | `(owner local) lol4_concept/` | Complete for concept scope; all decisions applied |
| LoL V | `(owner local) lol5_concept/` | Started 2026-09-20; spine drafted, awaiting decisions |
| LoL VI | not started | — |

This folder stays the master plan. Concept packs feed decisions back into the
`GAMEn_*_REFERENCE.md` files only when the user asks for it.
