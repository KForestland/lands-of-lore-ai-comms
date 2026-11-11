• Review complete. Here's what I checked and found.

  ## Scope of the change

  Only **L10_DC (Dracoid Cemetery)** is touched. `_l10_void_walls` (`scripts/lol2/act2_map.gd:348`) early-returns for every other `area_id`; `EDGE_RULE_AREAS` and `REGION_COLLISION_AREAS` are unchanged, so L17/L19 and all Act 1 maps are unaffected. The mechanism: the new function runs before `super._ready()` (`act2_map.gd:155`), loads 3165 `(region, edge)` pairs from `l10_void_edges.json`, matches them to `kind == "source_wall"` faces, and inserts their `RegionEdgeRule.face_key` into `edge_block_keys`. The existing `region_edge_blocks` hook in `jungle_review.gd:298` then puts those quads on the movement shell (a default-layer StaticBody3D), alongside the projectile-wall layer they already had.

  ## Verification performed (independent of the commit's own tests)

  - **Data integrity**: all 3165 JSON rows are unique, well-formed, and each matches exactly one `source_wall` face in `area.json` (3165/3165, no unmatched rows, no duplicate `face_key`s). The incident walls check out: face 13722 = wall record 2849 (region 4004, edge 0), face 13721 = wall 2848 (edge 2); both pairs are in the list, and no pair references region 4148.
  - **"Does it seal a real opening?"** I re-ran the generator's outward-probe rule myself against `creature_nav/L10_DC.json` (probe 10 units outward at 3 points along each edge, walkable polygon floor within 48 of the wall base): **0 of 3165 walls have anything walkable beyond them**. The list is consistent with its own stated rule.
  - **"Does it seal a linked passage?"** Cross-checked every matched wall against the stored nav links of its region. Two walls had a link point within ~4 units and were investigated in detail: region 1788's link to 4025 lies exactly on edge **3** of that quad (distance 0.0), while the blocked wall is on edge **1** — a different side of a small quad, and the probes beyond edge 1 hit nothing. Region 3602's link to 3598 crosses the shared interior of two overlapping sliver quads; the blocked wall is on the outer edge (x=2557) with void beyond. Both passages stay open. No matched wall lies on its region's linked side.
  - **Doors / moving floors / scripted geometry**: all 3165 matched faces have no `placement_kind`/`source_index` — pure static source walls. L10 doors, tombs, gate, fences, oil, and Emperor entry are `static_assembly`/`movable` faces excluded via their own `owns()` functions (which match only floor/ceiling/static_assembly), and `claim_moving_floors` is a no-op. No door, moving floor, or scripted face can be keyed.
  - **"Can it trap the player or seal a ledge?"** 320 matched walls have a walkable polygon beyond with floor >48 *below* the wall base (drop rooms), and many of those walls are only ~15 units tall. These are null-neighbour sides the original treats as impassable; a low rim can still be jumped over physically, so pre-existing drop-in routes remain physically possible, and the lower rooms' own linked exits are unaffected. No trap vector found.
  - **Creatures**: `scripted_creature_population.gd:60` gives creature bodies `collision_mask=1|256`, so they already collide with the movement shell — they will now also meet these 3165 walls. This matches native semantics (the probe used the *creature* nav graph, so blocked sides are exactly those creatures could never cross natively). Change is consistent, not a regression.
  - **Code path**: keyed faces flow through `jungle_review.gd:297-299` (`source_drawn_only` + `region_edge_blocks`), not the dead `bool(source_wall)` branch at `act2_map.gd:337` — L10 faces carry no `source_wall` boolean, which is fine because the shell-build check keys on `kind`. Keys are computed by the same `face_key` function on both sides. Counter `edge_rule_counts["l10_void_walls"]` will be 3165, satisfying both updated tests.

  ## Concerns checked and dropped

  - **Unrendered DEVIATIONS.md / ledger test**: per instructions, not a defect; the research note documents that the lead renders it and `tests/deviations_ledger_test.gd` is expected to fail on this branch until then.
  - **Wall 1180 (region 3602) near a nav link**: dropped — wall is on the outer edge of a sliver overlap; the 3602↔3598 passage is interior and stays open.
  - **Wall 2724 (region 1788 edge 1) near the 4025 link**: dropped — the link crosses edge 3, not edge 1.
  - **Stale-data risk** (`archive_sha256`/`geometry_sha256` in the JSON are never validated at load): mitigated by `l10_map_test.gd` requiring >3000 matched walls; a regenerated pack would fail the test loudly rather than silently misblock. Note, not a defect.
  - **135 null-neighbour sides with no drawn wall remain open** (documented in the research note): a residual fall-through gap, but out of this commit's stated scope and not a regression.

  No real defects found. The change is L10-only, data-verified against the nav graph, leaves every linked side, door, moving floor, and stacked-room opening untouched, and restores native collision semantics for both player and creatures.

  APPROVE
