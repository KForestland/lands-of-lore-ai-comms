# Kimi K42 — r18 integration check (museum dragon merge, cat ladies save clock)

Lead spot-check: click_dragon_chamber at museum_walkthrough.gd:1127, earned-test hint 'Click — Travel with the dragon' at :44, checkpoint elapsed 0.0 at jungle_cat_ladies.gd:37 — all confirmed.

## Findings

**(a) Museum dragon merge** — `scripts/lol2/museum_walkthrough.gd`

1. Input chain order in `_unhandled_input` (`museum_walkthrough.gd:688-704`): prism pointer click → `click_dragon(pixel)` for **any** left click (captured mode uses viewport centre via `_pointer_pixel()`, visible cursor uses `event.position`) → cursor-active early return → captured-mouse strike chain ending in `click_dragon_chamber()`. This matches `k42_museum.diff` exactly; no lines from the diff are missing in the merged file.
2. No lost lines in the refactor: old `can_enter_dragon()` guards were split into `dragon_lair_ready()` (mirror/pause/flying/introduction + y-range + region1422 polygon, `:1094-1100`) and the cursor guard plus facing check kept in `can_enter_dragon()` (`:1089-1091`). The full original condition set is preserved.
3. No double start: when a captured click hits the picture hotspot, line 691 starts the journey and returns before the strike chain runs; when the hotspot misses but `can_enter_dragon()` holds, only `click_dragon_chamber()` (`:1127-1128`) fires. After a start, `mirror_transition_pending` makes `dragon_lair_ready()` false, so a second click can't re-enter (verified by `tests/museum_dragon_picture_click_test.gd:48`).
4. `click_dragon_chamber()` delegates to `enter_dragon()`, which itself re-checks `can_enter_dragon()` (`:1130-1132`) — the ternary's pre-check is redundant but harmless; `_start_dragon_journey()` runs once per click.
5. Neither-fires path that is intentional: visible-cursor click on a non-dragon part of the picture (chest, torch) — `click_dragon` misses, line 693 returns on `cursor_active`, and the chamber fallback is captured-mode-only. The comment at `:1102-1104` says exactly this ("the chest and the rest of the picture do nothing").
6. Residual neither-fires edge: captured mouse, player inside the lair polygon but yawed so `(-camera.global_basis.z).dot(FORWARD) < 0.7` while the centre-pixel ray also misses the hotspot — the click silently does nothing (no feedback). This is the same geometry the BG12 adapter accepted; only a narrow angular band remains uncovered.
7. Tests still match:
   - `tests/museum_dragon_picture_click_test.gd` calls `click_dragon(pixel)` (`:20,34,48`) and `dragon_picture_target`/`dragon_lair_ready` (`:28,33,38`) — all exist with matching signatures. Its line 44 `_unhandled_input(click)` with cursor active relies on line 691 firing **before** the cursor guard — which is the merged order. Its line 48 second-click-false assertion relies on `mirror_transition_pending` gating — present in `dragon_lair_ready()`.
   - `tests/museum_dragon_click_earned_test.gd` expects hint `"Click — Travel with the dragon"` (`:44`), which requires `dragon_picture_target(_pointer_pixel())` at `:866` to be false at the alcove position (otherwise the hint would read "Click the dragon — …") and `can_enter_dragon()` to be true — consistent with the BG12 premise that the hotspot misses from that spot. Its captured click then reaches `click_dragon_chamber()` via the strike chain and starts the journey.
   - Other callers (`museum_dragon_route_test.gd`, `museum_exhibit_route_test.gd`, `museum_earned_walk_test.gd:106`, `museum_escape_wall_test.gd:121`) use only `enter_dragon()`/`can_enter_dragon()`, whose semantics are unchanged. No caller of the old no-arg `click_dragon()` remains anywhere in the tree.
8. Minor observation (pre-existing pattern, shared with the prism line): in visible-cursor mode a click on the picture starts the journey even with the cursor active; `dragon_lair_ready()` has no cursor guard. This is deliberate per the point-and-click design and is what the picture test asserts.

**(b) Cat ladies elapsed** — `scripts/lol2/jungle_cat_ladies.gd`, `k42_catladies.diff`

9. `checkpoint()` (`jungle_cat_ladies.gd:36-37`) now writes `"elapsed": 0.0` while keeping `segment`/`passes`/`owner_state`. The only reader of a saved elapsed is `restore()` (`:80-92`), which sets the animation clock and restarts voice via `show_frame()` at `first/15.0 + elapsed` (`:187-190`) — with 0.0 the voice and the animation restart together, so sync is preserved.
10. One-shot segments: `offer()`/`play_segment()` advance `owner_state` at segment *start* (`:120-138`), and `advance()` clamps elapsed to duration (`:165-166`), so nothing logic-wise consumes a mid-segment clock; a save/load mid-talk replays the talk from its start, which the new comment (`:34-35`) states is intended.
11. `validate()` (`:39-49`) accepts 0.0, and its "absent ⇒ elapsed 0.0" rule (`:48`) is unaffected since `hide_ladies()` already zeroes the clock (`:142-149`).
12. All consumers of the packet — `jungle_walkthrough.gd:314,536,608` (restore) and `:652` (checkpoint), `act_one_quest_state.gd:427-429` (validate only), `tests/hive_route_test.gd:115-117` and `tests/hive_small_route_test.gd:124-126` (validate then erase, matching the diff) — work with elapsed 0.0. `tests/jungle_cat_ladies_earned_test.gd` never touches checkpoint/restore; its assertions (loiter segment 1, E → segment 0/state 2, voice playing) are unaffected.

## Problems

1. none (a): the merge is faithful — no lost lines, no double-start, and both dragon tests align with the merged input order and signatures. The only residue is the narrow captured-mode angle band (Finding 6) where a click still does nothing, which is inherent to the accepted BG12 geometry, not a merge defect.
2. none (b): no code, validate rule, or test relies on a non-zero saved elapsed; the 0.0 write is round-trip stable and keeps voice/animation in sync.

## Verdict

Both r18 integrations are sound. The museum merge correctly composes the r16 pixel hotspot (firing first, in both mouse modes) with BG12's captured-mouse chamber fallback, with exactly one journey start per click and both dragon tests still matching the code. The cat ladies elapsed-0.0 checkpoint is safe: the only consumer (`restore()`) treats it as a clean loop restart with voice in sync, and all validators, route tests, and the earned test remain consistent.

