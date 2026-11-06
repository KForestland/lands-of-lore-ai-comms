# Kimi K19 — Act 3 chain links (act3_chain_status.md vs patches S/T/W/X), 2026-11-06

Lead spot-check: T03 earned test opens L17_HC.tscn directly (no start save) CONFIRMED; T01 centre tower reads an L16 save via read_save (start = greenhouse save per Kimi). Lead conclusion: the Act 3 drafts are NOT one A-to-Z chain yet. Fix list for Grok (list AB): order 070 before 069/076; towers NE/SE/NW (any order) -> SW last (075 needs the other three) -> centre 077 starts from the SW end save; 078 from 077; L16->L17 and L17->L19 transitions as earned walks (T03/T04 start from the previous end save); STORY-080 rows relinked in order.

# K19 — Act 3 chain check: `act3_chain_status.md` (STORY-066..093) vs `grok_research/patches/`

  Method: verified every patch file exists, then extracted the save paths each earned test loads (`var path :=`) and writes (`var save :=` / `_quicksave_unrecorded`) — from the base tree `tests/` for the live rows (066, 067, 068, 070) and from the `tests/*_earned_test.gd` sections inside each diff for S/T/W/X.

  ## Chain table

  | Story | Patch exists | Test start save | Previous row's end save | Link ok |
  |---|---|---|---|---|
  | 066 | yes (live `l14_chamber_voices.gd`) | `l14_belial_combat_qualified_save.json` | — (chain head, act1 save) | n/a |
  | 067 | yes (live `l16_arrival_elevator.gd`) | `l16_arrival_earned_save.json` | `l16_arrival_earned_save.json` (066, 2nd write) | ✅ |
  | 068 | yes (`R04_dry_fountain.diff`) | `l16_ground_earned_save.json` | `l16_ground_earned_save.json` (067) | ✅ |
  | 069, 076 | yes (`S01_ne_tower.diff`) | `l16_greenhouse_earned_save.json` | `l16_dry_fountain_earned_save.json` (068) | ❌ branch |
  | 070 | yes (live `l16_greenhouse.gd`) | `l16_ground_earned_save.json` | `l16_ne_tower_earned_save.json` (069/076) | ❌ branch |
  | 071 | yes (`S02_se_oil.diff`) | `l16_greenhouse_earned_save.json` | `l16_greenhouse_earned_save.json` (070) | ✅ |
  | 072 | yes (`S03_nw_traps.diff`) | `l16_greenhouse_earned_save.json` | `l16_se_oil_earned_save.json` (071) | ❌ branch |
  | 073–075 | yes (`S04_sw_chips.diff`) | `l16_greenhouse_earned_save.json` | `l16_nw_traps_earned_save.json` (072) | ❌ branch |
  | 077 | yes (`T01_centre_tower.diff`) | `l16_greenhouse_earned_save.json` | `l16_sw_chips_earned_save.json` (073–075) | ❌ branch |
  | 078 | yes (`T02_dragon_room.diff`) | `l16_greenhouse_earned_save.json` | `l16_centre_tower_earned_save.json` (077) | ❌ branch |
  | 079 | yes (`T03_cavern_run.diff`) | none — opens `L17_HC.tscn` directly | `l16_dragon_room_earned_save.json` (078) | ❌ no link |
  | 080 (T04) | yes (`T04_beast_wall.diff`) | none — opens `L19_BC.tscn` directly | `l17_cavern_run_earned_save.json` (079) | ❌ no link |
  | 080 (W01) | yes (`W01_beast_wall_blade.diff`) | `l17_cavern_run_earned_save.json` | `l19_beast_wall_earned_save.json` (T04) | ❌ branch |
  | 081 | yes (`W02_belial_horn.diff`) | `l19_beast_wall_earned_save.json` | `l17_beast_blade_earned_save.json` (W01) | ❌ branch |
  | 082 | yes (`W03_sewer_forms.diff`) | `l19_belial_horn_earned_save.json` | `l19_belial_horn_earned_save.json` (081) | ✅ |
  | 083, 084 | yes (`W04_drain_short_path.diff`) | `l19_sewer_forms_earned_save.json` | `l19_sewer_forms_earned_save.json` (082) | ✅ |
  | 085 | yes (`W05_ghostly_heads.diff`) | `l19_drain_path_earned_save.json` | `l19_drain_path_earned_save.json` (083/084) | ✅ |
  | 086, 087 | yes (`X01_dawn_curse.diff`) | `l19_ghostly_heads_earned_save.json` | `l19_ghostly_heads_earned_save.json` (085) | ✅ |
  | 088, 089 | yes (`X02_pillars_scotia.diff`) | `l20_dawn_curse_earned_save.json` | `l20_dawn_curse_earned_save.json` (X01, 2nd write) | ✅ |
  | 090 | yes (`X03_armory.diff`) | `l20_pillars_earned_save.json` | `l20_pillars_earned_save.json` (088/089) | ✅ |
  | 091 | yes (`X04_faux_draracle.diff`) | `l20_armory_earned_save.json` | `l20_armory_earned_save.json` (090) | ✅ |
  | 092, 093 | yes (`X05_finale.diff`) | `l20_faux_draracle_earned_save.json` | `l20_faux_draracle_earned_save.json` (091) | ✅ |

  ## Gaps and broken links

  1. **Ordering inversion in the doc.** "Apply the unapplied rows in the order below" lists 069/076 (S01) before 070 — but S01's test loads `l16_greenhouse_earned_save.json`, which only row 070's test produces. Row 070 must run before 069/076, 071, 072, 073–075, 077, 078.
  2. **Greenhouse fan-out, not a chain.** S02, S03, S04, T01, T02 all start from `l16_greenhouse_earned_save.json`, so consecutive rows 071→072→073→077→078 do not chain; each is a sibling branch off 070. Their end saves (`l16_se_oil`, `l16_nw_traps`, `l16_sw_chips`, `l16_centre_tower`, `l16_dragon_room`) are dead ends — no later test consumes any of them.
  3. **S01 (069/076) also branches off 070's greenhouse save**, not 068's dry-fountain save — and its end save `l16_ne_tower_earned_save.json` is likewise never consumed. Row 068's `l16_dry_fountain_earned_save.json` is a dead end too.
  4. **079 (T03) and 080 (T04) have no start save at all** — the earned tests open `L17_HC.tscn` / `L19_BC.tscn` directly, so the L16→L17 and L17→L19 transitions are unlinked. Nothing carries state from the L16 cluster into L17 or from L17 into L19.
  5. **The two STORY-080 rows cross-link.** W01 starts from T03's end (`l17_cavern_run`), W02 starts from T04's end (`l19_beast_wall`) — each matches an *earlier* row's end, not the row above it. `l17_beast_blade_earned_save.json` (W01's end) is a dead end.
  6. **Only W02→W03→W04→W05→X01→X02→X03→X04→X05 is a true linear chain** (`l19_beast_wall` → … → `l20_finale`). X01's dual write (`l19_dawn_curse` then `l20_dawn_curse`) is correct as documented — the L19 packet is copied into the L20 save.
  7. **No missing patches.** Every patch named in the table exists under `grok_research/patches/` (S01–S04, T01–T04, W01–W05, X01–X05, plus R04), and each diff does add the named `tests/*_earned_test.gd`. Rows 066, 067, 070 are live scripts confirmed present in the base tree, with their earned tests present in `tests/`.

  Bottom line: the doc's Starts/Ends cells accurately reflect what the tests read and write (including the declared branches), but the chain is a tree rooted at 070's greenhouse save with two scene-only jumps (T03, T04), not a linear sequence — and the doc's apply order puts S01 before the row that generates its input save.

