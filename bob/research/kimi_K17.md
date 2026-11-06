# Kimi K17 — verify K08_softlocks.md names against lol2_r15 (read-only, 2026-11-06)

Lead spot-check: Kimi checked r15, but K08 was written against act3-story. The L16 items (l16_* scripts: 0 in r15, 5 on act3; L16FountainBall in act3 l16_fountain_ball.gd; prop 602 = act3 l16_greenhouse.gd BALL_RECORD) and larkhon_join_tribe all EXIST on act3-story and ship in r16. Prop ids are per level, so prop 210 in L13 does not conflict with the L16 fountain orb prop 210. H22 is a Grok task id, not a repo id. Real finding: K08 says 'five Larkhon notes', r15 has four (+ larkhon_join_tribe on act3 = five). No code action.

All checks complete. Here is the verification of `~/AI_COMMS/grok_research/K08_softlocks.md` against `~/opus_work/lol2_r15`.

  ## Verification table

  | name | kind | exists | evidence (path:line) |
  | --- | --- | --- | --- |
  | `l10_silverleaf.gd` | script file | yes | `scripts/lol2/l10_silverleaf.gd:33,37` — refuses growth while bracers carried, grows without them, matching K08's description |
  | actor 115 (Larkhon) | actor id | yes | `docs/l8-larkhon-source.json:238` (`"ref": "actor:115"`); `scripts/lol2/act2_items_catalog.gd:47`; `docs/DEVIATIONS.md:377` |
  | "within 600 of actor 115" | behavior/radius | yes | `docs/DEVIATIONS.md:431` — "Within 600 units of the Larkhon (actor115)…" |
  | prop 210 | prop id | yes | `docs/l13-prison-source.json:1165` (`"ref": "prop:210"`) — but see mismatch note below |
  | grate 82 | control id | yes (as `control82`) | `docs/l9-flood-source.md:19` — "The final grate is control82"; `tools/prepare_l9_flood_source.py:37` |
  | chalice (consumes Dreamstone) | mechanic | yes | `docs/l14-chamber-voices.md:3,9`; `docs/act2_route.json:2673`; `tools/prepare_act2_route.py:73` |
  | hourglass | script/mechanic | yes | `scripts/lol2/museum_hourglass.gd` (file present; pinned in `docs/magic-speech-hive-earned-rune-return-checks.json:96`) |
  | dampen | spell/charm | yes | `docs/monastery-dawn-dampen.md:1,7` — Dampen charm, definition72 |
  | Dreamstone (citadel exit / temple door slots) | item/mechanic | yes | `tools/prepare_act2_route.py:60,61` (dreamstone, exit_slot) |
  | `TRIAGE_20261104.md` | owner file | no | not in `lol2_r15`; lives at `~/AI_COMMS/playtest_feedback_20261023/TRIAGE_20261104.md` |
  | ORIGINAL_BUGS (rows 3/6/13/14) | doc/table | no | no `ORIGINAL_BUGS*` file in the repo; `docs/DEVIATIONS.md:195,201,234` cite `ORIGINAL_BUGS_TO_FIX.md`, which also does not exist in the repo |
  | `larkhon_join_tribe` | note id | no | zero matches; real notes are `larkhon_must_sleep`, `larkhon_ask_shaman`, `larkhon_serum_needs_leaf`, `larkhon_vapors_unactivated` (`scripts/lol2/l8_larkhon_state.gd:13–16`); the string does exist in AI_COMMS |
  | "five Larkhon notes" | count claim | mismatch | `JOURNAL_HINTS` in `scripts/lol2/l8_larkhon_state.gd:12–16` holds exactly **4** Larkhon notes |
  | `L16FountainBall` | script/map attachment | no | zero matches; no `l16*` or `*fountain*` scripts exist at all (consistent with K08's "map does not attach" claim) |
  | STORY-068 | story id | no (in repo) | no match; exists only in `~/AI_COMMS/BACKLOG/BACKLOG.md:117` and `backlog.json:1799` |
  | STORY-069 | story id | no (in repo) | no match; only in `~/AI_COMMS/BACKLOG/BACKLOG.md:118` |
  | cards 071–078 / 079–093 (STORY-071…093) | story ids | no | no `STORY-065`…`STORY-093` anywhere in the repo (highest seen is STORY-066, written without a dash, in `docs/l14-chamber-voices.md:9`) |
  | prop 602 | prop id | no | no `prop:602`/`prop602`; bare `602` appears only as movie-file numbers in `docs/moff-revisit-checks.json:1042` etc. |
  | H22 | region/room id | no | only lowercase `h22` meaning "height 22" (`tests/cave_crack_movable_test.gd:29`, `docs/DEVIATIONS.md:352`) — not a place id |
  | HINTBOOK line refs (2916–2921, 3363–3366, …) | external book | no (external) | repo points outside: `docs/l9-flood-source.md:19` cites `AI_COMMS/reference_hintbook/hintbook.txt` |
  | PATCH.TXT 5.2 | external doc | no | not found in repo |

  ## Missing or mismatched items

  1. **`TRIAGE_20261104.md`** — not in `lol2_r15` (exists in `AI_COMMS/playtest_feedback_20261023/`).
  2. **ORIGINAL_BUGS rows 3/6/13/14** — no `ORIGINAL_BUGS*` file in the repo; even the `ORIGINAL_BUGS_TO_FIX.md` that repo docs reference is absent from `lol2_r15`. K08's row numbers can't be checked against anything in-tree.
  3. **`larkhon_join_tribe`** — no such note id in the repo; the hosted notes are the four `larkhon_*` keys in `l8_larkhon_state.gd`.
  4. **"five Larkhon notes"** — count mismatch: only four Larkhon journal notes exist (`l8_larkhon_state.gd:13–16`).
  5. **`L16FountainBall`** — not present anywhere (no L16 scripts at all). K08 itself claims the map doesn't attach it, so absence supports the claim, but the identifier resolves to nothing.
  6. **STORY-068, STORY-069, STORY-071–078, STORY-079–093** — none exist in `lol2_r15` (068/069 only in the AI_COMMS backlog). Consistent with K08's "no host and no earned test," but the ids don't resolve in the repo.
  7. **prop 602** — not found; K08 says "the earned test still breaks prop 602," but no such prop id exists anywhere in the repo.
  8. **H22** — not a repo id (only `h22` = height 22). K08's "H22's pad orb is prop 210" is mismatched: prop 210 is documented under **L13 prison** (`docs/l13-prison-source.json:1165`), not any H22 location.
  9. **HINTBOOK / PATCH.TXT** — external references, not in the repo (the hintbook lives at `AI_COMMS/reference_hintbook/hintbook.txt`).

  Everything else named in the file (`l10_silverleaf.gd`, actor 115, the 600-unit radius, prop 210, grate/control 82, chalice, hourglass, dampen, Dreamstone slots) checks out with concrete in-repo evidence.

