# Kimi K36 — Sol Dark Halls work review (2026-11-07)

Lead: integrate the 8-commit chain c9295da..be4cf78 after committing Sol's two uncommitted fix sets (lead does it, Sol is out of usage). Hold P3/P4 owner-clearance until slides 236/890 + bookcases 51/58 earned runs pass in the full r18 sweep.

# K36 — Sol lane Dark Halls review (read-only)

  Reviewed branches `sol/dark-halls-20261107` (tip `64104d0`), `sol/dark-halls-followup-20261107` and `sol/crouch-restore-20261107` (both tips `be4cf78`), all linear over `act3-chain` `c9295da`. Verified against `kimi_K35.md`, the r17 triage row, and the `[sol]` board lines.

  ## Findings

  | # | Check | Result | Evidence |
  |---|---|---|---|
  | 1 | P3 slides vs contract | PASS (with declared adapters). All six controls (236/890/891/1013/1015/1041) dispatch native kind‑4 toggles through `native_script_host`, state saved as bool, sounds 630/631 logged, prop465 link and prop416 op6 dispatched. `73fa6bb` corrects the visuals to the original template22 mask1/2 cutout textures 367/368 (supersedes the earlier translation). K35's "opcode6 selector" mis-claim is explicitly corrected in the doc. Open, honestly flagged: E‑aim replaces click, state→mode mapping is an adapter, candle/prop465 render side‑effects unrendered, sounds logged not played | `scripts/lol2/dark_halls_slides.gd:100`, `docs/dark-halls-slides-sol.md`, DEVIATIONS row 513 |
  | 1 | P4 bookcases vs contract | PASS (with declared adapters). 51/59 one‑way, 58 toggles per the native groups; solid closed via mesh‑bound StaticBody; state read from the native travel word; no grants added. Slide direction is a documented presentation adapter (native modes 2/4 direction unproven) | `scripts/lol2/dark_halls_bookcases.gd:98-110`, `docs/dark-halls-bookcases-sol.md`, DEVIATIONS row 512 |
  | 1 | P5 crouch vs contract | PASS. Hold‑C, Human‑only, reuses the established Museum 32/46 dimensions and clearance query; gates on form/fly/pause/mouse‑capture; no geometry or save‑format change. `be4cf78` fixes a real restore bug (Human46 rebuilt inside native gap40 after F5‑under‑header), reproduced by an earned negative before the fix | `scripts/lol2/player_crouch.gd`, `player_form_body.gd` diff, `docs/crouch-all-areas-sol.md`, DEVIATIONS rows 510–511 |
  | 2 | Earned tests play like a player | YES. All earned tests start from the sha‑pinned r17 repaired‑monastery save, click the actual MENT/MCEL hotspot rects, wait out the cellar conversation, verify the live 51‑body population and unchanged inventory/globals across the handoff, walk by input (`walk_points`/`walk_to`), aim and `tap(KEY_E)`, F5/F9 disk save and real reload. Negative checks: standing refused in the 40‑unit crawlspace, release‑under‑header refuses stand, no‑op reload can't pass, earlier arrival restores closed. Captures at every key pose | `tests/dark_halls_slides_earned_test.gd`, `…_bookcases_earned_test.gd`, `…_crouch_earned_test.gd`, `…_objects_earned_test.gd` |
  | 3 | Ledger rows + rendered DEVIATIONS.md | PASS. Four rows (`docs/DEVIATIONS.md:510-513`) each with a matching `docs/deviations/0317-row-2026-11-07-sol-*.md` piece; piece text matches the rendered row verbatim; statuses honestly "(in progress)" | listed above |
  | 4 | Typed vars / PASS lines / registry | PASS with one nit. New scripts fully typed (no untyped `var x =` in slides/bookcases/player_crouch/objects tests). Precise PASS lines in all five tests. Registry JSONs exist for all five with correct mode and env/fixture needs. Nit: the bookcases and crouch earned registry notes point to `docs/dark-halls-slides-sol.md` (copy‑paste; should cite their own docs) | `tests/registry/dark_halls_*` |

  ## Integration order

  Both follow‑up branches point to the **same commit** `be4cf78`, and `act3-chain` is still at `c9295da` — so this is one linear chain, zero inter‑branch conflict, fast‑forwardable:

  1. `0c55d92` — P3 slide toggles + earned slide1015
  2. `3ac59da` — P4 bookcase doors + earned59
  3. `4e85027` — wall‑rejection aiming + silent restore hardening
  4. `c4b3bad` — P5 shared crouch + earned crawl
  5. `64104d0` — P3 aperture frame record (docs only; squash candidate)
  6. `70e44d0` — native‑neighbor route plans + earned slide1041
  7. `73fa6bb` — P3 original cutout variants (supersedes earlier P3 motion — must be included)
  8. `be4cf78` — P5 low‑header body restore fix (must be included)

  Recommended: integrate `sol/dark-halls-followup-20261107` @ `be4cf78` as a single fast‑forward onto `act3-chain`. The `lol2_sol_dark_halls` worktree (tip `64104d0`) is a strict prefix — nothing extra to take. `sol/crouch-restore-20261107` is the same tip — nothing extra either, **but see the uncommitted WIP below**.

  ## Problems by severity

  **High — uncommitted work completes claimed fixes and is on no branch:**
  - `lol2_sol_dark_halls_next` (dirty): route stand‑off planner fix in `tools/build_dark_halls_objects_walk.py` + regenerated `tests/dark_halls_objects_walk.json` — this is the fix for the board's "final236 stance too close to wall (6.7 vs 6)" earned failure on slides 236/890. Plus untracked `tests/dark_halls_bookcase51_earned_test.gd`.
  - `lol2_sol_crouch_restore` (dirty): bookcase58 oblique‑ray self‑rejection fix (`dark_halls_bookcases.gd` aimed() + regression test) — a real earned‑approach failure fix. Untracked P8 groundwork (`dark_halls_blast_rules.gd`, crates doc) is also here — keep it out of the P3–P5 merge.
  - The two dirty sets touch disjoint files, so committing both onto the follow‑up branch is conflict‑free. Do that before integrating, or the known failures ship.

  **Medium:**
  - Affected sweep is incomplete and stale: 96/687 run on the frozen `64104d0` snapshot (pre‑`73fa6bb`, pre‑`be4cf78`), 91 PASS / 5 FAIL. Four FAILs are documented fixture‑env receipts; the fifth, `cave_prop83_lift_live_test`, is an unexplained 300s timeout hang after quickload — needs a rerun on the final integrated snapshot.
  - Earned coverage is partial per the docs' own gates: slides 236/890 and bookcases 51/58 have no passing earned route yet; `73fa6bb` is tagged WIP and the refreshed 8‑object earned run was still in flight on the board. P3/P4 are not owner‑cleared.

  **Low:**
  - Registry note copy‑paste (bookcases/crouch earned → slides doc).
  - Board line 4682 names `c9295da` as the P3 WIP commit; corrected by 4688 (`0c55d92`) — no action, just read the board with the correction applied.

  **Verdict:** integrate the 8‑commit chain as ordered above after Sol commits the two uncommitted fix sets; hold P3/P4 clearance until slides 236/890 + bookcases 51/58 earned runs and a full‑snapshot affected sweep (incl. the cave_prop83 rerun) pass. P5 is the cleanest of the three and its restore fix is well‑evidenced.

