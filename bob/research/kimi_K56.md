# Kimi K56 — pre-merge review: grok BJ09 + BK11 (r19)

## Findings

**BJ09 — L16 city chain**

1. Applies cleanly to HEAD: context matches at `scripts/lol2/l16_ne_tower.gd:14` (ARRIVAL `y 100` → `132`), `tests/l16_dry_fountain_earned_test.gd:1-3,45-48,92-98`, `tests/l16_ne_tower_test.gd:12`. All new files (3 tests, 3 registry entries, 1 fixture, 1 ledger row) are absent on HEAD — no conflicts.
2. The lift change is adapter-scoped: the lift is already a logged adapter (`scripts/lol2/l16_ne_tower.gd:5-8,75` — "Target u16 0 is not the player, so this rise is an adapter"). The patch only corrects the teleport target from floor height 100 to the body-origin height 132, with the reason stated in the ledger row and the code comment. Existing `tests/l16_ne_tower_earned_test.gd:60` reads `tower.ARRIVAL`, so the constant change flows through with no stale pin.
3. Earned rule satisfied: the dry-fountain test loses its placement teleport (`scene.player.position = Vector3(438, 82, 10390)`) and instead walks the west ledge — a tightening, not a loosening. The three new tests chain earned saves (ground → dry fountain → greenhouse → NE tower → starry floor); the NE tower steps use `scene.request_jump()`, a player action. Chain prerequisites exist and run earlier in registry order: `l16_ground_earned_save.json` from `l16_arrival_elevator_earned_test` (order 749), dry fountain at 785.
4. Fixture dependency `tests/fixtures/l16_greenhouse_to_hourglass.json` already exists on HEAD; the new `l16_avenue_to_greenhouse.json` is supplied by the patch.
5. Starry-floor sitting honestly stops where the data stops: the test header and ledger row repeat the host's standing note that box, disk, yellow figure and prop 615 have no placements (matches `l16_ne_tower.gd:6-7`) — that remainder is BK12's scope, not silently skipped.

**BK11 — native claims verified against `scripts/lol2/native_scripts/L16_CA.json`**

6. Group 14558 (stream 1, file offset 18669504, 7 commands) matches every claim: opcode 9 kind 4 target 24 (`090418000300`); opcode 1 on movables 98/81/80 (`012062006400`, `012051006400`, `012050006400` — byte 4 = `0x64` = 100 on all three); opcode 198 `c60000000b01` stores byte 5 = 1 at local index `0x0b` = 11; opcode 9 `090360021500` arm `0x15` enqueues prop 608; opcode 9 arm 2 on prop 392.
7. Doors 80/81/98 placements decode as claimed: byte +0x22 = `0x01` (mode 1) on all three; byte +0x24 angle word: 80→`0x28`=40, 81→`0x64`=100, 98→`0x96`=150. The native store (`scripts/lol2/native_script_host.gd:1141`) is `(angle_word * byte4)/100` = angle word, so travel = 40/100/150 — exactly `DOOR_TRAVEL` in the patch, and the ledger's "150, 100, 40" for "98, 81, 80" is in the matching order.
8. Prop 392's kind-9 record (`0a09de38110000000184`): mask +4 = `0x0011` ✓, byte +8 = 1 ✓, byte +9 = `0x84` → mode 4 with the one-shot bit. The mode-4 matcher (`native_script_host.gd:791-808`) admits when `dword_26` ≤ byte+8, so "dword_26 at most 1" is accurate, and bit 7 clears byte +9 after the enqueue — the native record is one-shot, matching the script's own `burned` guard.
9. The spark word0 is genuinely not in the export; the admit dict supplies `word0 = 0x0011` (the mask value itself) and this is declared as an adapter in both the ledger row's last column and the script comment. Not smuggled.
10. The group really runs on HEAD: `opcode1_other_modes`, `opcode9_enqueue`, and `b71a0_bit_clear` all default on (`native_script_host.gd:180-181`) and `HOST_ADAPTERS_OFF` is `{"L8_SJ": []}` (`scripts/lol2/act2_progression.gd:34`), so nothing is disabled for L16_CA. Staged `FIELD_TRAVEL` writes flow through `_on_field` (`act2_progression.gd:256-260`) into `travel` + `_pose`. The patch's `_pose_fire_doors` is redundant on the burn path but is the piece that makes save/reload keep the doors, since restoring native state does not re-emit field writes.
11. Old behavior is replaced faithfully: the old `l16_se_oil.gd:5` said opcode 1 "stays unread, so those doors stay put" and the old test pinned "fire doors stay". The patch removes exactly that, keeps the burn guard, spark receiver, bow reveal and drain mesh unchanged, and updates both tests to pin `[40, 100, 150]` with the ledger row as the stated reason.
12. The chain test's 16 canal door ids (124–165) all exist as movables in the native export. The chain base (`l16_ground_earned_save.json`) is produced by an existing registered test at order 749.

## Problems

1. **Ledger row collisions with Fable's pending work.** BJ09's `0360-row-2026-11-09-l16-ne-lift-stand.md` collides with Fable's pending `0360-row-2026-11-09-l19-guck-liquid.md`, and BK11's `0361-row-2026-11-09-l16-se-oil-doors.md` collides with Fable's pending `0361-row-2026-11-09-region-aware-collision.md` (both in `~/AI_COMMS/fable_lane/bk_20261109/` patches 0001 and 0002). Against r19-work HEAD alone Grok's numbering is correct — HEAD max is 0359 (0358 act3-hosts, 0359 l8-shore-soul; there is no 0360 on HEAD, contrary to the task brief). Whoever merges second renumbers.
2. **Registry order collisions.** BJ09 takes 978/979/980; Fable's pending patches take 978/979/980 (patch 0001) and 981 (patch 0002). BK11's 982 is free under both merge orders and looks deliberately placed past Fable's 981.
3. Minor — registry gap if Grok merges first: order 981 would be skipped with no test. Harmless, but it only makes sense as deference to Fable's pending 981.
4. Minor — `burn()` fires the group but doesn't gate the burn on the verdict (`l16_se_oil.gd` new `burn()`): burn proceeds even if the group were rejected. The earned tests assert `status == "ran"`, so a regression is caught in CI, but gameplay state and group verdict can diverge silently. Acceptable given the group is verified to run; noted for the lead.
5. Minor — a few untyped vars (`var input =`, `var scene =`, `var gh =`) in the new tests; these mirror the existing earned-test idiom in the same files (`l16_dry_fountain_earned_test.gd:41` etc.), so the typed-vars rule is effectively observed to house style.

## Merge order and verdict

Merge order: **Fable's bk_20261109 patches first** (they are BK01–03, earlier in the BK list, and they occupy ledger 0359–0361 and registry 978–981), then **BJ09 renumbered** (ledger 0362, registry 982–984), then **BK11 renumbered** (ledger 0363, registry 985). BJ09 before BK11 keeps registry order monotone with merge order; the two Grok patches share no files and BK11's chain test is independent of BJ09's saves (it walks the canal from the ground save), so the order between them is cosmetic. If Grok merges before Fable instead, his numbers stand as submitted (BK11's 982 already dodges Fable's 981) and Fable renumbers.

Verdict: **merge after renumbering.** BK11's native claims are fully verified against the export (group 14558 opcodes, mode-1 doors 98/81/80, travels 150/100/40, mask 0x0011, byte +8 = 1, one-shot record), the old doors-stay-put behavior is replaced faithfully with the one spark-word adapter honestly logged, BJ09's lift fix is adapter-scoped and ledgered, all tests are earned or tightened with stated reasons, and every chain prerequisite is already registered on HEAD.

