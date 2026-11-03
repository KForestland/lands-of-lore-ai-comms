# LoL2 lessons -> cleanup, workflow, LoL3 and LoL1 (DRAFT for the owner talk, 2026-11-03)

Draft by the lead. Discussion points, not decisions. Mirrored publicly.

## 1. What worked (keep)
- **Quality gates before every build:** affected tests, the earned Act 1 campaign, build, package and smoke. No broken build
  reached the owner's launcher, and every integration problem was caught before playtest.
- **Known behaviour -> build directly, decode only unknowns.** Hint book plus longplay plus owner memory, then logged adapters.
  This is the single biggest speed-up: Astra did ~60 story steps in ~2 days once it applied.
- **One board, one backlog with claims, one status file per lane.**
  - The lead watches every 30 min and unblocks lanes with decisions.
  - The improvements file catches lessons as they happen.
- **A research lane ahead of the builder:**
  - Grok's cards and source-id packs removed most question rounds.
  - Its rubber-duck walks found real gaps.
- **Owner playtests on real builds** and F10 reports with position and screenshot. Four of five reports were fixed the same day.
- **Deviations ledger:** every difference from the original is written down with its source.
- **Public coordination repo:** an outside AI contributed useful opcode-18 research within hours.

## 2. What cost time (fix)
- **Stale test pins:**
  - Hard-coded counts broke at every integration: item ids, face counts, solids. Six to eight per build.
  - Fix: derive the counts from generator lists (TOOL-PIN-CHECKS).
- **Earned tests depending on untracked `tmp/` saves:**
  - 80+ Act 2 tests can only run in the builder's own folder.
  - Fix: a committed or staged chain-fixture mechanism, as the Act 1 campaign has.
- **Two systems owning one object:** the egg twins and the door colliders. Fix: ENGINE-OWNER-REGISTRY.
- **Per-area host copies:** the same feature behaves differently per area, as with the L9 walls flag. Fix: ENGINE-AREA-HOST, gradually.
- **Lanes not running the shared affected tests** before calling work READY. Fix: make it part of READY.
- **Generated media staging:**
  - Producers refuse existing folders, so clips silently went missing.
  - Fix: ENGINE-STAGE-MANIFEST.
- **Long qualification:** about 3-4 h per build. Fix: ENGINE-FAST-QUALIFY, without weakening the checks.
- **Lanes idle between turns:** the 30-min watch helps, but standing queues and "never stop" rules helped more.

## 3. Cleanup candidates (for the talk)
- **Old worktrees:** about 30 under opus_work (r7..r12x, fork_*, astra side lanes).
  - Archive the qualified ones and delete the rest after a backup.
- **AI_COMMS:**
  - Archive old dated folders into `archive/`.
  - Keep LEAD_STATE, BACKLOG, status, board and IMPROVEMENTS on top.
  - Trim the 3,900-line board into monthly files.
- **Backlog:**
  - Close or merge duplicate rows: the AUDIT rows are done, and several "any" rows were overtaken.
  - Re-rank by the phase order.
- **The ~300 DEVIATIONS pieces:** a quick sweep for adapters that can now become native, for example opcode 18 after Probrogit's work.
- **GitHub:**
  - the clean code snapshot (still pending);
  - merging Probrogit's PRs;
  - the trusted-sender list.

## 4. Applying it to LoL3
- **Start with what LoL2 learned:**
  - the shared area host;
  - the owner registry;
  - the earned-chain fixtures;
  - the playtest start points;
  - the stage manifest.

  All from day one, not retrofitted.
- **Order:**
  1. RE/extraction status (Lands-of-lore-3-re exists).
  2. Maps first, then progression from the hint book, then items, then RPG, then dialog. That's the LoL2 phase order, which held up.
- **Research lane first:** story cards plus a source-id pack per area before building starts.
- **A playable vertical slice early,** so the owner playtests real builds within the first weeks.

## 5. Applying it to LoL1
- The RE is closed and published, and the Godot port has started (lol1_godot, faithful core).
- Plan: Classic first. Then LoL1 is the first Enhanced edition (owner plan), and its 3D assets come first, in 1-2 years.
- Reuse the engine layer LoL2 builds (area host, item router, mechanism kit, save migrations) rather than a separate one.
- smgtoxa's LoL1 project: decide how the two relate (handoff #1 on GitHub).

## 6. Questions for the owner
1. Retire or archive old worktrees and builds (keep the last 3 qualified)?
2. Astra 6.2: same task style, or bigger slices per prompt?
3. LoL3 start: after LoL2 Act 3 is done, or in parallel with a research-only lane?
4. LoL1: our Godot port or smgtoxa's project as the base?
5. Probrogit: trust, merge PRs #8/#9, and run their opcode-18 check?
