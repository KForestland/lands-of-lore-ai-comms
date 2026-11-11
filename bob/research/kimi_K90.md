• Pre-merge review of `2461984..cdac6d8` (7 commits, grok/of9) complete. I read the full diff of every source file, the board posts in `COORDINATION.txt`, and traced each stated risk into the surrounding engine code.

  ## Stated risks — verdicts

  **OF2 (bramble regrow) — risk does not hold, dropped.** The collision timing is unchanged: the old code also set `row["solid"] = true` at the same timer expiry (`jungle_bramble.gd:172-181`). Only the drawn selector changes (5 → 0), which actually removes a picture/collision mismatch. A player mid-passage when the timer fires is re-solidified exactly as before this commit and as in the native sequence. Old saves with state 4 are migrated by `restore()` (`jungle_bramble.gd:149-152`).

  **OF7 (spark lights braziers) — melee risk does not hold, dropped.** The brazier hit bodies carry only the `spark_receiver` meta (`l10_braziers.gd:77`); melee strike dispatch uses `hive_hit_receiver`, and `receive_hit` is reachable solely via `receive_spark`, which hardcodes the spark word (`l10_braziers.gd:126-132`). The sword word 0x080E shares no bits with mask 0x0051 and could never pass `admits()` anyway. `crystal_fire()` deliberately does not consult `spark_receiver`. One minor finding below.

  **OF11 (crate carry) — mostly holds.** No duplication path (single attach, bodies reused); a carried crate cannot get stuck in Luther (collision layer 0 while carried, set-down lands `CARRY_GAP` past the body radius); saves are versioned/validated and old saves without `cave_crates` load fine; the shove path and its tests are preserved. Findings below.

  ## Findings (all Low severity)

  1. **Set-down ignores the local floor — `scripts/lol2/cave_crate_stack.gd:259`.** A floor drop always uses `_world_floor()` (the stack-room floor, ≈ -215). Scenario: stack five crates, climb to the -130 lip while carrying a sixth, press E facing the plateau — the crate center is placed 85 units under the lip surface, inside the riser rock: invisible, and unreachable from above because the lift height check (`cave_crate_stack.gd:223`) rejects it. It is only recoverable because `_nearest_faced` (`cave_crate_stack.gd:209-236`) has no line-of-sight check, so E can also grab it through the rock from below. Mirrored case: set down in the -285 bridge room and the crate floats 70 units up. No progression loss on realistic paths (the five-crate stack stays behind), but a quicksave after the bury makes the odd state permanent. Severity: Low.

  2. **Lifting the bottom of a stack leaves the rest floating — `scripts/lol2/cave_crate_stack.gd:270-276`.** The lift branch never runs `rest_all`, so crates resting on the lifted one hang in the air until the next shove or set-down; the eventual `rest_all` can then drop them onto the player's position. Self-correcting, cosmetic. Severity: Low.

  3. **No input-context guard on the crate E — `scripts/lol2/cave_walkthrough.gd:726-728`.** Unlike the adjacent `draracle_door.try_use()` (line 724, requires `MOUSE_MODE_CAPTURED`) and the brazier E handler (checks captured mouse, inventory, `actor_input_locked`), `crates.try_use()` fires on any unhandled E — mouse free after ESC, or with a menu that doesn't consume the key — and lifts/drops a crate behind the UI. It matches the file's existing loot-collect sloppiness, but those don't move world state this visibly. Severity: Low.

  4. **Brazier hint regression — `scripts/lol2/l10_braziers.gd:179-180`.** The old "E — Light brazier" hint is gone entirely; the hint now shows only "Spark — Light brazier" via `spark_target()` (reach 384, no line-of-sight, no mana check). A player inside E range with no mana sees a hint for an action they can't perform, and the still-working E option (`l10_braziers.gd:183-190`) is never advertised. Severity: Low.

  ## Holds with no findings

  - **OF3** (`l10_main_gate.gd:32-35`): same `str(material) in alpha_cutout_materials` idiom as `dark_halls_slides.gd:47` and `act2_progression.gd:1011`; collision quad untouched.
  - **OF8** (`museum_atlas.gd`): union-time pile check feeds `_piled` the same `{"grid": ...}` shape it expects (`museum_atlas.gd:787`); refusing a pile union can only split genuinely stacked rooms — non-piled components still join one storey, so other maps' counts are stable; draw/fit/label filters are consistently gated on `section_hi > 0 and viewed >= 0`.
  - **OF10** (`dev_diagnostics.gd:36-46`): `area_name` is used only by diagnostics/F10; `L10_DC` is in `Places.AREA_NAMES`; host_kind dispatch unchanged.
  - **OF12** (`museum_key_locks.gd:112`, `museum_gallery.gd`): plate node kept with no collision and reach still via `aim_point`; UV spans covered by the extended test.

  APPROVE
