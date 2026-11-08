# Kimi K40 — BG27/28/29 + Fable light-l14 review (2026-11-08)

Lead: merge after r18b ends: BG27-29 then build ledger; light-l14 after Fable's 674 sweep posts; resolve DEVIATIONS by re-render only.

All checks are complete. Here is the review.

  # K40 review — BG27/BG28/BG29 + Fable light-l14 vs r18-work 3b6a929

  ## A. Grok patches (stacked after BG26 per ORDER.md items 28–30)

  | Patch | Owner report | Fixes it? | Test plays like a player? | Applies on 3b6a929? | Act 1 risk |
  |---|---|---|---|---|---|
  | BG27_stone_squid | r17 18-19-21 "stone creature is supposed to be still, not moving, shooting plasma" | Yes — actor 58 (StSquid, def 0, behavior 6, at 4883,2,-4535) is anchored to its placement via new `anchored()`/`on_anchor_impact()` hooks; attack moved to selector 3 (verified present in sprites.json, 14 frames, same resource 1060 pictures as selector 2) with the plasma bolt fired at frame 4 through the existing `dawn_spell_bolts.gd`; melee damage forced to 0. Matches the lead's 01:56Z APPROVED line exactly. | Yes — `l9_stone_squid_test.gd` loads the real `dragon_level.tscn`, walks the player capsule from (4682,32,-4512) toward the squid, asserts it stayed (<1 unit drift), the bolt was ranged (>80), and health dropped. | Yes — I reconstructed every hunk's old-text and found it verbatim in the 3b6a929 blobs; selector-2/frames-14 block is unique in L9_DR.json; new test/registry/piece files don't exist yet; registry order 932 free (max is 931); ledger piece 0339 free (max 0338). | None direct (L9 is Act 2). The shared `scripted_creature_population.gd advance()` change is behavior-neutral for non-anchored actors (anchored defaults false; I traced both branches). |
  | BG28_cave_crate_shove | r17 16-23-39 "can't stack boxes or move boxes" | Yes — root cause verified in the tree: old reach `PLAYER_R(8) + half_size`, but the human capsule (radius 15, `player_form_body.RADII=[15,23,8]` confirmed) stops outside that reach; patch uses form radius + crate corner + 1, and `rest_all`/`support_top` gain a `floor_y` param (default keeps the old constant) fed by `_world_floor()` from the translated homes. Diagnosis and fix are consistent with the code. | Yes — `cave_crate_shove_earned_test.gd` instantiates the real cave scene, walks the actual player body into crate 94 toward 95 with `move_and_slide`, asserts it moved and rests on top. | Yes — all six hunks' old-text verbatim at 3b6a929; the DEVIATIONS.md tail context (BG23/BG24/BG26 rows) matches; the existing `cave_crate_stack_test.gd` (order 781) calls `rest_all(centers, sizes)` — the new defaulted parameter keeps it source-compatible; order 933 / piece 0340 free. | Low — Cave is the certified start, but the change is scoped to the crate-stack room (controls 94–122, optional mace-climb content) and the physics gate is unchanged. |
  | BG29_draracle_door | r17 16-25-58 "the door in front of the Draracle is missing" | Yes — hosts movables 74/77 (templates 11/10, resource 478) as a closed double leaf at the arch; kind-4 use opens both leaves (travel 21845), second use closes; save/validate wired into `walkthrough_save.gd` (old saves without the key still validate). I decoded the patch's binary hunk: the PNG is 15,732 bytes and its sha256 is exactly the `material_sha256` the source JSON pins (`06692da5…`), so the `assets_ready()` gate will pass. | Yes — `cave_draracle_door_earned_test.gd` walks the corridor in the real cave scene, is stopped by the closed leaves (slide-collision group check + ray), uses the door, walks through the arch. | Yes — all seven hunks' old-text verbatim (including `_unhandled_input`, `_process`, `_save_state`, `_quickload_unrecorded` contexts); `_indexed_material` exists via the `indexed_complete_cave_review.gd` ancestor and loads by `Image.load_from_file`, so no `.png.import` is needed; new files (door script, source JSON, PNG, test, registry 934, piece 0341) all absent at 3b6a929. | Medium-low — this ADDS a closed door on the main path to the Draracle (previously open). If `try_use` ever failed in real play it would convert a non-blocker into a blocker. Mitigations: earned test covers block→use→pass; asset-gate failure falls back to today's open corridor; prompt respects mouse-capture. |

  The three patches touch disjoint files (population/L9_DR vs crate stack/DEVIATIONS.md vs cave_walkthrough/walkthrough_save), so they stack in any order — ORDER.md's "in any order" claim is accurate.

  ## B. Fable light-l14 (lol2_light, 353402f + 2 commits)

  | Commit | Lead's ask (01:24Z board) | Delivers? | Merge on 3b6a929? |
  |---|---|---|---|
  | b3ff8a5 L14 sector shading | (b) L14 sector shading from the original, captures at the owner's 4 poses | Yes — `sector_shades/L14_HT.json` (64 rows, area L14_HT, shade/palette sha256 retained, produced by the same `prepare_l8_night_shade.py` that backs L10/L13/L16/L19) + one-line `AREAS += L14_HT`. The host hooks (`sector_lighting`, `static_face_light`, `sector_light_enabled` revert) already exist identically in act2_map.gd on 3b6a929. Captures delivered: `fable_lane/light_l14_20261109/captures_lit/` has all 4 owner poses (hangings, hall, garden, doors) + g_275/g_276 stand-ins and the comparison composite. | Clean for code/data — cross-repo diff 3b6a929→light-l14 of `act2_sector_light.gd` is exactly the one AREAS line; JSON is new. |
  | ca8e1de three-door decision | (a) doors 88/89/90 far view: black vs see-through, logged | Yes — decision "see-through stays" backed by the archive's own potential-visibility set (sector 77 names rooms 80/81/82) and frame/door/lintel coverage; docs-only (ledger text piece + DEVIATIONS.md). | Clean except the ledger (below). |

  `git merge-tree --write-tree 3b6a929 light-l14` (run in lol2_light, which has both objects) reports exactly **one conflict: `docs/DEVIATIONS.md`** — nothing else.

  ## Merge order

  1. BG27 → BG28 → BG29 (ORDER.md 28–30; disjoint, so order is cosmetic), then run `python3 tools/build_deviations.py build` — pieces 0339–0341 render together (429 pieces) and BG28's hand-appended DEVIATIONS row gets regenerated from its piece. Run the three new tests (orders 932–934) plus `cave_crate_stack_test` (781) and the ledger `--check`.
  2. Merge light-l14: expect the single DEVIATIONS.md conflict; resolve by keeping r18's file, then re-render from pieces (Fable's two pieces come along automatically). Do not hand-merge the ledger text.
  3. Note BG30 is closed-as-original (no merge) and BH04 is already queued behind these.

  ## Problems by severity

  **High:** none.

  **Medium:**
  - Fable's DEVIATIONS.md merge conflict (confirmed by merge-tree). Trivially resolved by re-render, but if the lead hand-resolves it by keeping Fable's side, `build_deviations.py --check` will fail and the BG rows could be dropped.
  - Fable's 674-test affected regression (act2_sector_light.gd is preloaded by act2_map.gd, the base of every Act 2/3 host) was started but the result is still not on the board ("result follows" in RELEASE.md; last fable board line is 01:31Z). Merge should wait for it or re-run it.

  **Low:**
  - BG27's definition-0 attack change is shared by StSquid actors 61/68: their melee hit frame moves 5→4 (same pictures, same damage). Grok's note says "61 and 68 still hunt" — true for motion, but the timing shift isn't disclosed. Minor.
  - Fable's pieces are numbered 0322/0323, already taken on 3b6a929 (0322 = e05-player-water, 0323 = e06-jungle-bridge-decks). The build tool explicitly permits equal numbers (renders in name order, "lanes never renumber"), so functional impact is nil — just two unrelated pairs sharing numbers. Fable's rows are also dated 2026-11-09, a day ahead.
  - `act2_sector_light_test.gd` was not touched: it auto-iterates `AREAS` (so L14 really is covered — the PASS claim is structurally valid), but its PASS string still prints "four Act2 maps" while testing five. Cosmetic.
  - Naming mismatch already reconciled on the board, but for the record: triage row 18-19-21 says "L12", the actor is in the L9_DR (dragon_level) scene — same actor 58/pose, and the lead's 01:56Z answer confirms it.
  - BG27/BG29 both leave native decoding open by design (frame-event value 82; opcodes 16/197 on region 1906) — disclosed in the ledger rows 0339/0341 as adapters, consistent with the owner-rule convention.

  Bottom line: all five items do what the reports/asks require, the tests are genuine scene-walk earned tests, typed vars/PASS/registry orders are in order, and nothing here threatens the certified Cave start beyond BG29's gated, earned-tested door. Safe to merge in the order above once the DEVIATIONS.md re-render step and Fable's pending 674 result are handled.

