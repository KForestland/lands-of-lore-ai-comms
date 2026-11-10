• Review complete. Everything checked out; here are the findings.

  ## Scope verified

  - Patch applies cleanly to 97dce7e (`git apply --check` passes, sha256 `44319ed5…` matches the board note). Deviation slots 0505/0506 and registry order 1203 are unoccupied.
  - Board note (`COORDINATION.txt:5111,5118,5130,5131`) is accurate: ledger 0505 correction + 0506 adapter, registry 1203, teleports 1.

  ## The two stated risks

  **1. Host-wide effect of `opcode7_prop_frame` — real, but disclosed and one-directional.** The adapter goes into the `ADAPTERS` const (`scripts/lol2/native_script_host.gd:78`), which `_init` enables for every host on every level. I enumerated the data: 445 groups across 14 areas (L1, L3, L4, L7, L8, L9, L10, L12, L13, L14, L16, L17, L20) contain opcode 7 index 2 or 10 on a prop, and 369 of those have commands after it. Previously those groups always aborted at that command ("prop slot +0xB4 index %d is not decoded") and, because staging is all-or-nothing (`_run`, native_script_host.gd:999-1004), committed nothing; now they run to completion. So yes, props on other levels can now change state where they silently couldn't before. This is strictly "more of the native script runs" — no previously-completing group changes behavior, since these arms never passed before. The new stores themselves are inert in the port: nothing reads `byte_0x31`/`byte_0x37` by field name anywhere, and the predicate evaluator only reads +0x25, locals, and the e58 array (native_script_host.gd:913-950), so no predicate outcome can flip. No existing test asserts the old refusal strings. This matches the project's default-on adapter convention and is exactly what deviation 0506 declares. Checked and dropped as a defect; flagged as the known, intended blast radius.

  **2. Save/reload of +0x37/+0x31 — survives level changes, not disk saves; no defect.** On level exit the full host `state` (including `prop:241` fields) is banked in `lol2_act2_native_bank` and restored on re-entry (`scripts/lol2/act2_progression.gd:374-379`, `215-218`), so the stores survive in-session transitions. Disk saves never serialize native state (`act2_save.gd` has no native/bank handling) — but that is pre-existing for every native field, not introduced here. The consequential state is `quest_state.l16_dragon_room.chopped`, which *is* saved and gates `chop()`; after a reload, group 6384 cannot re-fire because the swing's strike word 0x080E doesn't share bit 0x0002 and props aren't in the struck set, so the room module is the only admit path and it's blocked by the quest flag. The frame bytes reverting on disk reload is cosmetic and identical to every other prop. Dropped.

  ## Other checks (all dropped)

  - **Group 6384 sequence vs test expectations** (L16_CA.json, group 6384): op9 arm 0x12 → op9 arm 3/0x15 on control 73 (enqueue kind 6 caller 0x14) → op16 (+0x25=1) → op5 (+0x30=3) → op7 idx10 byte5=8 (+0x37=8) → op7 idx2 (+0x31=0) → op7 idx0 (+0x36 |= 0x05). Matches every assertion in `tests/bk18_dragon_chop_test.gd`, including predicate 206 (`0005000000` = +0x25 == 0) rejecting the second fire.
  - **`fire_results.size() == 1`**: prop 241 has exactly one kind-9 record (group 6384; its other record is kind 6). Holds.
  - **Index 10 semantics**: `(held & 0xF0) | byte5` with unstaged high = 0 matches the disassembly (`8a7037 80e6f0 … 08d3 885837`) and the constructor mask; `stage_read` is seeded from committed state (`_stage_state = state.duplicate(true)`, native_script_host.gd:981), so the read-modify-write survives across groups. Index 2 correctly ignores byte 5 (the table entry always pushes 0 — L17's byte5=8 index-2 commands still store 0 natively).
  - **Room module API**: `apply_chop`, `state()`, `aimed`, `save_feedback`, `host.get("progression")`, `progression.fire` (act2_progression.gd:444), `starting_magic.world_active()` all exist and are used consistently with the base file. Test's scene members (`adapter_exit_seeds`, `ready_for_review` via jungle_review, `progression.change_scene_enabled`, `interface_request`) all exist on the L16_CA scene chain.
  - **Rendered `docs/DEVIATIONS.md` absent**: per instructions, not a defect.

  ## Not verified

  Per instructions I did not launch Godot, so the new test's PASS is taken from Grok's board claim; static cross-checks of every assertion against the data and code all agree with it.

  APPROVE
