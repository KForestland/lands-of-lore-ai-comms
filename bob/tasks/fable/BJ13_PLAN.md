# BJ13 PLAN: serum and Silverleaf as a player gets them (Fable plans, lead builds)

Written 2026-11-10 by Fable from `BJ13_SERUM_SILVERLEAF_20261110.md`, for an engineer who has not seen my session.
Base: worktree `~/opus_work/lol2_bj12`, branch `bj12-l8-quests` = `b3e384e` + `5b518c9` (lake bank) + `7f5cab5` (village chain).
Stack every step below as its own small commit on that branch. Ledger block 0550-0599 (0550-0552 used), registry orders 1250-1299 (1250-1252 used).
Limits: max 2 Godot, MemAvailable >= 10 GiB before each launch, `--audio-driver Dummy`.

Grades used below: **PROVEN** = I read it in the data or ran it today; **LIKELY** = inferred, not run; **UNKNOWN** = not confirmed, do not build on it without checking.

---

## 0. Read this first: one finding that changes the task

**The tree-room mixing slots cannot be where the player makes the FIRST potion.** (PROVEN from data + docs, see section 3.)

- The raised tree room opens only with a Crystal Shard (`act2:L14_HT:post_shard`, definition 105). The shard comes from the Huline Temple (L14).
- The temple door needs the Dreamstone from L13 (`docs/act2_route.md` row `L8_SJ / temple_entry`), and L12/L13 lie behind the Larkhon.
- So the room is reachable only AFTER the player has already passed the Larkhon once. The hint book says the same (line ~3119): the slots "produce **another** Larkhon-soothing potion ... the option of returning to the Claw Mountains".
- The native data agrees: the room holds its **own** Amaranth Serum (prop 99 gives one on E), so the second potion does not need the shaman again.

Consequence for the owner's answer ("the small hut is where the potion and leaf are mixed, i.e. the raised tree room"): that is true for the second potion only. The first potion is mixed by hand (book ~3150), which today is the pack button and the shaman's-table button from BJ12, and after step 4 also pack-item-on-pack-item.

**OWNER DECIDED 2026-11-10: option A.** Tree-room slots as the optional second potion; by-hand combine is the first potion.

**Decision the lead should put to the owner before step 3 is called done** (it does not block building step 3):
- (A, my recommendation) Build the tree-room slots faithfully as the optional second potion, and make the by-hand combine (step 4) the real answer to "serum not accessible".
- (B) Open the tree room earlier than the original does, so it can serve the first mix. I advise against it: it removes the shard puzzle and contradicts the data.

A second consequence: in the port the Larkhon never wakes once dosed (DEVIATIONS 0307). So the second potion has **no gameplay use** in the port today. It is a real item the player can make and keep; say so in the ledger row rather than inventing a use.

---

## 1. The player contract, step by step

What the player must be able to see and do with no test help. "Today" is the state on `7f5cab5`.

| # | Player step | Contract | Today |
|---|---|---|---|
| P1 | F2 start "End of Act 1 - Darker Jungle arrival" | Arrives alive at full health (owner decision 2026-11-10) | 19 of 30 health; four blows of 6 on the way kill a walker who does not fight |
| P2 | Emperor's sarcophagus without the bracers | Told that Silverleaf now grows on the dead trees; a Journal note says so | Feedback line only (`l10_silverleaf.gd:37`). No Journal note. UNKNOWN whether the owner saw the line |
| P3 | Dead trees in the cemetery | The leaves are visibly on the trees | Trees 159-170 are scale 0 until grown, then shown (`l10_silverleaf.gd:25-29`). NOT confirmed by me in a rendered frame |
| P4 | Pick nine | "E — Pick Silverleaf" when aimed; each pick says so; pack shows "Silverleaf" with icon 117 | Works by code (`l10_silverleaf.gd:57-66`). E needs a captured mouse (line 62), so no headless real-key test exists |
| P5 | Village: present a leaf | Initiation starts | Done in BJ12 (real input test) |
| P6 | Shaman: offer a leaf | He gives the Amaranth Serum; pack shows it by name with icon 119 | Done in BJ12. Icon/name in the pack NOT asserted by any test |
| P7 | Keep both across save/reload and across the level change L10 -> L8 | Nothing lost | Serum + vapors F5/F9 asserted in BJ12 test. Nine leaves across L10 -> L8 is covered only by older chain tests that call handlers directly |
| P8 | Combine by hand | Drop serum on leaf or leaf on serum in the pack -> Larkhon Vapors | Only a "Mix with Silverleaf" button on the selected serum, plus the shaman's-table button |
| P9 | Left click the potion on Luther, right click the Larkhon's upper chest | Vapors activate; dose applies | "Activate vapors" button in the pack, then real right click (tested in BJ12) |
| P10 | (after the temple) tree room: back-of-room slots | Serum in one slot, leaf in the other -> a potion appears -> take it. Slots give the item back if taken out first | Not hosted at all |

---

## 2. Build order (small steps, one commit each)

0. F2 full-health start (small, owner decision).
1. Player walk of both items from the F2 start, real input, **no test aids**; publish the STOP list on the board before fixing anything.
2. (BJ13 item 3, FIRST FIX) Tree-room mixing slots, native data.
3. (BJ13 item 4) By-hand combine: pack item dropped on pack item.
4. (BJ13 item 2) The remaining stops from step 1, in chain order.
5. (BJ13 item 5, only if time before Wednesday's cutoff) real village views.

Do step 1 before 2 even though 2 is "first fix": step 1 is a survey that changes no game code, and its STOP list is what the owner asked to see first.

---

## Step 0 — F2 darker start at full health

**Contract:** starting "End of Act 1 - Darker Jungle arrival" from the F2 list gives Luther 30 health. The normal "Resume darker jungle", every save file, and the Hulines' damage stay exactly as they are.

**Facts (PROVEN, read today):**
- The F2 list is `scripts/lol2/playtest_starts.json`; the entry is id `act1-end-darker-jungle`, resume kind `darker`, save `act1_dark_halls_darker_arrival.json` (pinned by sha256, health 19 inside).
- `scripts/lol2/playtest_starts.gd`: required fields are `FIELDS` (line ~25). An extra optional key is not rejected by `entry_error()`.
- `scripts/lol2/original_game_gate.gd`: `start_playtest(id)` at ~234-260 points `darker_save_path` at the staged file and calls `_verify_and_start(...)`; the darker branch at ~309-318 reads the save with `JungleSave.read_save(darker_save_path, Darker.FORMAT)` and sets tree meta `lol2_darker_resume` = `saved.state`.
- Health is `state.health`, an integer 1..30 (`scripts/lol2/jungle_save.gd:20`). 30 is the maximum the validator accepts. UNKNOWN: whether any later system raises the maximum; I found none.

**Build:**
- Add an optional key `"full_health": true` to that one manifest entry. Do not change the save file or its sha256.
- In `original_game_gate.gd`, add a member `var start_full_health := false`. In `start_playtest`, set it from `bool(entry.get("full_health", false))` just before `_verify_and_start(...)` and clear it right after (next to the `kept` restore at ~259).
- In the darker branch, after the read succeeds and before `set_meta("lol2_darker_resume", ...)`: `if start_full_health: saved.state.health = 30`.
- Update `docs/playtest-starts.md` with one line.

**Test (new, registry order 1253):** `tests/playtest_start_full_health_test.gd`, modelled on `tests/playtest_starts_test.gd` (it already instantiates the gate and calls `start_playtest`, see its lines ~120-127).
- Start `act1-end-darker-jungle` through the gate; assert the resume meta (and, if the test loads the scene, `scene.starting_magic.health()`) is 30.
- Call the plain resume path with `darker_save_path` pointed at the same file and assert health is still 19. This is the proof that only the test start changed.
- Assert the staged save's sha256 is unchanged.

**Then:** in `tests/l8_village_views_earned_test.gd` apply the same full health the gate applies (the test reads the pinned save directly at its `run()` start; set `source.state.health = 30` with a comment naming the F2 rule), delete the TEST AID block in `walk()` (the `health_kept` / `blows` members and the "TEST AID" prints), and delete `"test_aids"` from `tests/registry/l8_village_views_earned_test.json`. The earlier walk took 4 blows of 6 = 24 damage, so 30 should survive with 6 left; this is LIKELY, not run. **If he still dies, do not put the aid back: post it on the board.**

**Ledger 0553:** "F2 darker start gives full health (test start only)", class Modern (playtest aid), owner 2026-11-10.

**Acceptance:** new test PASS; `playtest_starts_test` PASS; `l8_village_views_earned_test` PASS with no "TEST AID" line in its log.

---

## Step 1 — walk both items as a player; publish the STOP list

**Contract:** one honest answer per row P2-P9 above: can the player see it, do it, and know what comes next.

**How:** survey tests (unregistered until green, like my BJ11 sittings), real keys and real mouse, on foot, from the F2 start at full health. No handler calls, no `set_health`, no position sets. If a position set is unavoidable print `TELEPORT` and count it in the registry row (lead rule P1).

Suggested sittings (each ends in an earned save the next one loads; pin the sha256 once green):
- A: F2 start -> Daniel -> temple -> village -> shaman's sigil -> on foot into L10. This is `tests/l8_village_views_earned_test.gd` as it stands; reuse its `walk()`, `key()`, `click()` helpers.
- B: L10 gate -> Emperor (globes, ankh, remains). Existing chain: `tests/l10_tomb_earned_test.gd` and the tests that extend it (`l10_ruins_departure_earned_test.gd` has `prepare()`).
- C: ruins -> wet exit -> lake -> Dawn takes the bracers (`l8_shore.gd`, `l8_dawn.gd:22-31`).
- D: back to L10 -> Emperor without bracers -> growth -> pick nine -> back to L8 -> village. Existing: `tests/l10_silverleaf_growth_earned_test.gd`, `tests/l10_silverleaf_harvest_earned_test.gd` (both call handlers directly; K71 lists them).
- E: initiation -> serum -> mix -> Larkhon. This is `tests/l8_tribe_serum_earned_test.gd` + `tests/l8_larkhon_earned_test.gd`.

**Things to assert that nothing asserts today:**
- A rendered frame of a grown tree and of a bare tree (use `~/opus_work/ai_tools/godot_capture.py`, script mode) and look at it. `l10_silverleaf.gd:27-29` sets scale 0 / identity on a multimesh instance; I never saw the result.
- After each pick, the pack row: open the real inventory (Tab), find the row, assert label "Silverleaf" and a non-null icon. Same for "Amaranth Serum" (catalog label, `act2_items_catalog.gd:75`; the raw definition label is "Amaranth sr") and "Larkhon Vapors" (`:74`).
- Leaves survive the L10 -> L8 level change and F5/F9 on both sides.
- At each step, the HUD hint and the Journal say the next thing. Record the exact text.

**Stops I expect (LIKELY, from reading the code; confirm each before fixing):**
1. `l10_silverleaf.gd:62` and `l8_dawn.gd` / `l10_emperor.gd` E handlers require a captured mouse, so a headless real-key test cannot press E there. Use the BJ12 pattern (`l8_journey.gd` `_unhandled_input`, `l10_main_gate.gd:68`): `Input.mouse_mode != CAPTURED and DisplayServer.get_name() != "headless"`.
2. Growth has no Journal note. A player who dismisses the feedback line has nothing that says "the dead trees". Proposed note `l10_silverleaf_grows` ("Silverleaf grows on the cemetery's dead trees now. Nine leaves for the Wild Village."), <= 130 characters (see traps).
3. The pick hint needs aim within 150 units and dot > 0.8 at a point 42 above the prop origin (`l10_silverleaf.gd:39-45`). UNKNOWN whether that matches where the leaves are drawn.
4. Nothing tells the player how many leaves he has or that nine is the number. The clearing text in `l8_journey.gd next_step()` mentions nine only before the first pick.
5. The serum's "Use" is refused with a hint (DEVIATIONS 0308) and "Mix with Silverleaf" appears only when the serum row is selected (`museum_inventory.gd:313`).

**Acceptance:** a STOP list on the board in chain order, each line with the player step, what he sees, and file:line. Signed. Before any fix.

---

## Step 2 — tree-room mixing slots (FIRST FIX; most detail)

### 2.1 Player contract

After the bamboo door is open and Luther stands in the room:
1. A bottle stands in the room (prop 99). `E — Take the Amaranth Serum`. Once only.
2. At the back of the room are two slots. Holding the serum at the first: `E — Place the Amaranth Serum`. Holding a Silverleaf at the second: `E — Place a Silverleaf`. Order does not matter.
3. With an empty hand at a filled slot: `E — Take back ...` returns the same item.
4. When both are filled a potion appears between them (prop 96). `E — Take the Larkhon Vapors`. Both slots empty again; the ingredients are gone.
5. It can be repeated as long as the player has serum and leaf (natively nothing limits it; in practice there is one serum in the room).
6. Wrong item, other form, paused, too far: refused, nothing lost. Save/reload at every stage keeps slot contents and the potion.

### 2.2 Native data (L8_SJ.MIX sha256 `3eff0743...28bc2`, the same file `docs/l8-tree-source.json` pins)

All of this is PROVEN as bytes; I read it from `scripts/lol2/native_scripts/L8_SJ.json` (generated, git-ignored, staged in lol2_bj12) and from the archive. Positions are Godot (x, height, z = -native y) from the placement's first four words. Region ids are from `assets/lol2/generated/creature_nav/L8_SJ.json`.

| Object | Godot position | Nav region (floor) | Event records |
|---|---|---|---|
| control 50 = serum slot | (-1740, 240, -2767) | 3722 (220) | kind 4 mode 3, identity `049A8E70` (def 119 Amaranth), predicate 206 -> group s1:12198. kind 4 mode 0 (empty hand), predicate 207 -> group s1:12234 |
| control 51 = leaf slot | (-1700, 240, -2826) | 3720 (220) | kind 4 mode 3, identity `0E347A01` (def 117 Silverleaf, = 238320129, the catalog's value), predicate 206 -> s1:12270. kind 4 mode 0, predicate 207 -> s1:12306 |
| prop 95 = the counter | (-1691, 250, -2904) | 3817 (250) | kind 6 caller 0x14, predicate 208 -> s1:2328 |
| prop 96 = the produced potion | (-1692, 250, -2776) | 3727 (250) | kind 4 mode 0, **no predicate** -> s1:2358. Also kind 6 -> s1:2400 |
| prop 99 = serum in the room | (-1570, 250, -2553) | 3735 (250) | kind 4 mode 0, no predicate -> s1:2530 |
| prop 98 | (-1559, 280, -2570) | 3740 (220) | kind 2 (timer) -> s1:2478 |
| control 70 = outer shard slot | (-1395, 230, -2626) | 681 (-10) | shard `D0421BDE`, predicates 206/207/208 -> s1:12702 / 12778 / 12814 |
| control 66 = inner shard slot | (-1464, 220, -2710) | 3740 (220) | shard, predicates 206/207/208 -> s1:12542 / 12594 / 12634 |
| movable 50 = bamboo door | (-1430, 220, -2575) | 3742 (220) | none |

Predicates 206 / 207 / 208 are table entries `0005000000` / `...01` / `...02`: the context object's byte +0x25 equals 0 / 1 / 2 (host: `native_script_host.gd` ~875-883, left type 5 reads `FIELD_BYTE25` of `input.context`).

Command groups, bytes verbatim:

```
12198 (serum in):   10 10 32 00 01 00   op16 control50 byte+0x25 = 1
                    02 01 00 00 18 00   op2 arm 0x18 (host adapter opcode2_arm18_clear: clears the held item)
                    11 03 5f 00 01 00   op17 prop95, byte4 = +1
                    09 03 5f 00 15 00   op9 prop95 arm 0x15 (enqueue prop95's kind-6 caller-0x14 event)
                    05 10 32 00 01 00   op5 control50 selector = 1
12234 (serum out):  11 03 5f 00 ff 00   op17 prop95, byte4 = 0xFF (-1)
                    10 10 32 00 00 00   op16 control50 = 0
                    03 01 00 00 70 8e 9a 04 04 00 00 00   op3 give item 049A8E70, arg 4
                    05 10 32 00 00 00   op5 control50 selector = 0
12270 / 12306       the same two groups for control 51 with identity 0E347A01
2328 (both in):     09 03 60 00 03 00   op9 prop96 arm 3
                    05 03 60 00 00 00   op5 prop96 selector 0
                    07 03 60 00 02 00 / 07 03 60 00 00 00   op7 prop96 (x2)
2358 (take potion): 10 03 5f 00 00 00   op16 prop95 = 0
                    10 10 33 00 00 00 / 10 10 32 00 00 00   op16 control51 = 0, control50 = 0
                    03 01 00 00 01 57 c8 58 04 00 00 00    op3 give item 58C85701 (def 128 Larkhon Vapors), arg 4
                    09 03 60 00 02 00   op9 prop96 arm 2
2400 (prop96 kind6): op16 control51 = 2, op16 control50 = 2, op5 control50 = 0, op5 control51 = 0, op5 prop96 = 1
2530 (room serum):  0e 03 62 00 03 00 00 00   op14 prop98 arm 3
                    14 03 62 00 08 03 80 15 06 06   op20 (sound) x2 around:
                    c4 90 97 0e c8 00 00 19 00 00 00 00   op196 region 3735 floor -> 200
                    03 01 00 00 70 8e 9a 04 01 00 00 00   op3 give item 049A8E70, arg 1
                    09 03 63 00 0e 00   op9 prop99 arm 0x0E (on itself)
12702 (outer shard in, control 70): op9 arm 0x0D on prop 99, prop 95 and class-4 objects 49, 30, 50, 29; op1 movable 50 travel 100; op2 arm 0x18; op20; op5
12542 (inner shard in, control 66): op9 arm 3 on class-4 objects 24, 50, 49
```

**My reading (LIKELY, not proven from the EXE):**
- op17 adds its signed byte 4 to the target's byte +0x25. That makes prop 95 a counter: 0 -> 1 -> 2, and predicate 208 (== 2) fires 2328 exactly when both slots are filled, whichever is filled second. Taking an item out decrements. This fits every byte above, but **op17 has never been decoded**; it is only in the size table (`tools/lol2_source_format.py:26`, size 6).
- 2328 shows prop 96 (op9 arm 3 = "release"/show, then selector and frames). 2358 hides it again (arm 2).
- op9 arm 0x0E on prop 99 retires it after the serum is taken (the host sets `bit_0x15_0x80`).
- op9 arm 0x0D from the outer door's group switches the room's props and items on when the door opens.
- 2400 (prop 96 kind 6, caller UNKNOWN) sets both controls to state 2. Under predicates 206/207 state 2 matches neither record, so the slots would be locked while the potion waits. Who fires it is UNKNOWN; I did not find the caller. If it is not fired, a player could take the leaf back out after the potion appears. Treat as unknown and guard in the owner (2.4).

**UNKNOWN, say so in the ledger row:**
- What class-4 objects 24, 29, 30, 49, 50 are (the chest's dagger, the two recipes, the circlet, the Lizard Seal by the book; not checked).
- What prop 98 is (a kind-2 timer that moves region 3735's floor to 250; perhaps the bottle's shelf or lid).
- Whether the room's interior is walkable to the slots in the port. The slots sit ~300 units west-south-west of the doorway point the existing test reaches ((-1460, -2640), region 3740). Regions 3722 / 3720 / 3727 / 3817 are small 220/250-high cells; I did not walk them. `l8_tree.gd:36 owns()` and the 0284 notes say blocker 2417's wall was trimmed at height 220 for this room; expect similar clipping work.
- Whether props 95/96/99 and controls 50/51 have visible meshes in the port's L8 pack. Not checked.

### 2.3 What I ran (PROVEN today, data only, no scene)

Probe: `~/AI_COMMS/fable_lane/bj13_probe/mixer_probe.gd` (a SceneTree script; it needs only `scripts/lol2/native_script_host.gd` and `scripts/lol2/native_scripts/L8_SJ.json`). It calls `host.fire_event(ref, 4, {"arg_c", "arg_object_identity", "context"})`. Results on `7f5cab5`:

| Event | Result |
|---|---|
| prop 99, empty hand | group 2530 **ran** (adapters slot_index_binding, b71a0_bit_clear, opcode14_timer, opcode3_item_grant); `item_request(0x01:0, 049a8e70, 1)`; prop 99 gets `bit_0x15_0x80 = 1` |
| prop 99 again | **ran again and gave a second serum.** The host does not stop a retired prop; the owner must check `bit_0x15_0x80` |
| control 50, leaf offered | rejected by the mode-3 matcher (correct) |
| control 50, serum offered | group 12198 **unhosted: "opcode 17 has no handler"** |
| control 51, leaf offered | group 12270 **unhosted: "opcode 17 has no handler"** |
| control 50, empty hand, state 0 | 12234 rejected by predicate 207 (correct) |
| prop 96, empty hand, at any time | group 2358 **ran and gave the vapors with nothing in the slots** (no predicate; natively the prop is not there to click). The owner must gate on prop 96 being shown |

So the whole mechanism is one missing opcode away from running natively, plus two gates the owner must hold.

### 2.4 Build

**(a) Opcode 17 in `scripts/lol2/native_script_host.gd`.**
- Register a handler the way the others are (`_handlers[opcode] = handler` at ~363; model on `_op_byte25` at ~1757, which writes `FIELD_BYTE25` for op16).
- Behaviour: `stage_write(ref, FIELD_BYTE25, (stage_read(ref, FIELD_BYTE25, 0) + signed(bytes[4])) & 0xFF)`. A never-written byte reads as 0 (the predicate code treats an unknown +0x25 as unhosted, so op16 on prop 95 has never run before the first insert; decide the default deliberately and comment it).
- It rests on a LIKELY reading, so call `use_adapter("opcode17_byte25_add")`, add it to `ADAPTERS` (~77) and give it a DEVIATIONS row (0554). Ask Grok to confirm op17 from the disassembly (the handler table is at native 0x645E0 per `tools/prepare_native_scripts.py`); if he proves it, drop the adapter flag.
- Check no other level starts behaving differently: `grep` the 15 `native_scripts/*.json` for opcode 17 and list the groups in the commit message. Any group that was "unhosted" only because of op17 will now run. (Not done by me.)
- Unit test in the style of `tests/act2_movers_test.gd` (it builds a host with `fresh("L8_SJ")` and runs groups): the probe's sequence must give serum-in -> state 1, counter 1; leaf-in -> counter 2 and `event_enqueued(prop:95, 6, 0x14)` and group 2328 ran; serum-out -> counter back, `item_request` serum; etc.

**(b) New owner `scripts/lol2/l8_tree_mixer.gd`** (+ `l8_tree_mixer_state.gd` if you keep the state/validator split the other owners use), attached where `L8Tree` is attached (`darker_jungle.gd` ~257-274). Pattern to copy: `l8_tree.gd` (reach test `reachable()` 63-66, hint in `_process` 90-95, E in `_unhandled_key_input` 96-106).
- It does not re-implement the recipe. It fires the native events through the binder: `host.progression.fire(ref, 4, input)` (`act2_progression.gd:443`), with `input = {"context": ref, "arg_c": 0 or 1, "arg_object_identity": identity of the held item or 0}`. The held item is `host.hand_item`, falling back to the first carried item of the right definition exactly as `l8_tree.gd:101-105` does for the shard. Identity comes from `act2_items_catalog.gd` (`identity` field of the row; 119 -> 77237872, 117 -> 238320129).
- It listens to the native `item_request` signal (the binder already logs it at `act2_progression.gd:207`; connect a second listener on `host.progression.native`) and turns identity `049A8E70` / `0E347A01` / `58C85701` into pack items.
- It removes the offered item from `host.carried_collected` itself when the insert group reports `status == "ran"`. The native op2 arm 0x18 only clears a host global; nothing in the port takes the item out of the pack. Do the remove and the grant through `mechanism_transaction.gd` (Kit) like every other receptacle, so a full pack or a failed group loses nothing.
- **Item ids.** The existing ids are singletons with strict validators: `l8_shaman_trade.gd:7` `SERUM = "act2:L8_SJ:shaman_amaranth"` and `l8_larkhon_state.gd:5` `VAPORS = "act2:L8_SJ:larkhon_vapors"`; `l8_larkhon_state.validate()` (49-67) rejects a save where those ids do not match its own receipts. So:
  - the room's serum gets a new id, e.g. `act2:L8_SJ:tree_amaranth` (definition 119);
  - the slot's output gets a new id, e.g. `act2:L8_SJ:tree_vapors` (definition 128);
  - add both to `act2_items_catalog.gd` next to lines 74-75, same icon/label/handler as their definitions;
  - which leaf sits in the slot is recorded by its real id (`act2:L10_DC:silverleafNNN`) so "take back" returns the same instance;
  - `l8_larkhon.gd can_mix()` (45) accepts any carried definition-119 item, so the room's serum can also be hand-mixed, but `State.mix()` is once-only (`l8_larkhon_state.gd:30`). Decide: either leave the by-hand mix once-only (then the room's serum can only go through the slots) or make it repeatable. I recommend leaving it; say so in the row.
  - `l8_larkhon.gd activate()` (59) and `State.apply()` (42-48) accept only `VAPORS`. The second potion will not activate. Given 0307 that is harmless; state it in the ledger row, or widen both to "definition 128" if the lead wants the second potion usable.
- **Gates the host does not hold** (from 2.3): refuse E on prop 99 once its `bit_0x15_0x80` is set; refuse E on prop 96 unless prop 95's byte +0x25 is 2; refuse everything while the door is shut (`l8_tree_slot_state.unlocked(state().lock)`); refuse a slot's take-back once the potion is waiting if you choose to follow group 2400's lock (unknown caller; simplest is to allow take-back and let the counter drop, which the native groups already support, and re-hide prop 96 when the counter leaves 2. Write down which you chose).
- **State and saves.** The native host's state for this area is banked on level change (`act2_progression.gd:373-378`: `state`, `locals`, `locals_e58`, `record_state`). CHECK how it is saved on F5 (I did not read that path); if the binder already persists `native.state`, the slot bytes come back for free and the owner only stores which pack item id sits in which slot. Add the owner's key to the L8 save validator list the same way `l8_tree` is (`l8_tree.gd validate()` 25-35 is the model: slots used before the door opened must be rejected).
- **Presentation.** Reach points are the placements above; start with reach 150 and facing dot > 0.85 like `l8_tree.gd`. If the pack has no mesh for the potion (prop 96) or the bottle (prop 99), draw the item icon as a small billboard at the placement (the flame sprites at `l8_tree.gd:56` are the pattern) and say so in the row.
- **The existing "slot66" proxy.** `l8_tree.gd:6` `POINT` is a door-face stand-in that the port calls slot 66; natively the outer slot is control 70 and control 66 is inside the room. Do not untangle that in this step. Only make sure the new owner does not answer E at the same spot.

**(c) Geometry.** Before writing the test, walk from the doorway (-1460, -2640) to each of the three points with a probe and print where the body stops. Expect to trim a ground-level blocker at the upper floor as 0284 did. If a slot cannot be reached, put the reach point at the nearest standing place and log it; do not move the native placement.

### 2.5 Earned test

`tests/l8_tree_mixer_earned_test.gd`, registry order 1254. Extend `tests/l8_tree_room_earned_test.gd`'s chain: its output `res://tmp/l8_tree_room_earned_save.json` is Luther inside the open room with the shard back in the pack.

- The test needs a Silverleaf in that save. The qualified tree chain was earned from the temple shard, and I did not check whether leaves are still carried at that point (UNKNOWN). If not, the honest input is a save from the full chain; if you add a leaf to the save by hand, print it as a declared `TEST AID` and mark the registry row. Prefer finding or producing a real chain save.
- Real E for every action (the mouse-capture guard must allow headless as in step 1's stop 1). `root.size = Vector2i(1280, 720)` first if anything is clicked.
- Sequence: E at prop 99 -> serum in the pack, second E gives nothing. Wrong item at each slot refused, pack unchanged. Serum in -> F5/F9 -> still in. E empty-handed -> serum back. Serum in, leaf in (then repeat in the other order on a second run or from a reload) -> potion shown -> F5/F9 -> E takes the vapors -> both slots empty, leaf and serum gone, one new vapors item, pack row labelled "Larkhon Vapors". E at prop 96 again gives nothing. `scene.resets == 0`.
- Also assert through the binder's log (`progression.route_log`) that groups 12198, 12270, 2328, 2358 have `status == "ran"`. That is the proof the native data did the work, not a parallel recipe.

**Acceptance:** that test PASS; `l8_tree_room_earned_test`, `l8_larkhon_earned_test`, `l8_tribe_serum_earned_test`, `act2_movers_test` still PASS; the opcode-17 group list reviewed; ledger rows 0554 (opcode 17 adapter) and 0555 (tree-room mixer: second potion, no use after 0307, the ids, the gates, the unknowns).

---

## Step 3 — by-hand combine: pack item on pack item

**Contract:** in the pack, dragging the serum onto a Silverleaf, or a Silverleaf onto the serum, makes the Larkhon Vapors. The existing buttons stay.

**Facts (PROVEN, read):** `scripts/lol2/museum_inventory.gd`
- 189: `item_list.set_drag_forwarding(func(at): return _drag_item(at), Callable(), Callable())` — the grid starts drags but accepts no drops.
- 456-466 `_drag_item` returns `{"inventory_item": id, "index": index}`.
- 143, 475-484: drops exist only for equipment slots (`_can_drop(role, data)`, `_drop`).
- 223-226: the "Mix with Silverleaf" button calls `get_parent().get_node("L8Larkhon").mix(id)` and closes the pack; 313 shows it only for a serum that `can_mix`.
- `l8_larkhon.gd` 45 `can_mix(serum)`, 47-58 `mix(serum, station)`: it takes the first carried leaf itself.

**Build:** give the grid's second and third forwarding callables: can-drop = the dragged id and the row under the cursor (`item_list.get_item_at_position(at, true)` -> metadata) are one definition-119 and one definition-117 item, in either order, and `can_mix(the serum)`; drop = `L8Larkhon.mix(the serum)`, then refresh the list (or close, like the button). If the lead wants the dropped-on leaf to be the one consumed, add an optional `leaf` argument to `mix()`; today it always takes the first leaf.
Keep it specific to this pair. `docs/l8-larkhon.md` says plainly this is a book-led story recipe, not a general alchemy engine, and no native recipe table has been decoded.

**Test:** `tests/l8_hand_combine_earned_test.gd`, order 1255, from `res://tmp/l8_shaman_serum_earned_save.json` (serum + leaves, written by `l8_shaman_trade_earned_test`). Open the pack with the real Tab key, then real mouse: motion to the serum row, left press, motion to a leaf row, release (`root.push_input`, as `click()` in my tests; Godot needs the motion events between press and release to start a drag, and a few frames between them). Assert vapors in the pack, serum and one leaf gone, the Journal note `larkhon_vapors_unactivated`, F5/F9. Second case from a reload: leaf dropped on serum. Third: leaf dropped on a sword does nothing.
UNKNOWN: whether pushed mouse events start a Control drag in headless. If they do not, run this one test in `rendered` mode (the runner starts its own Xvfb) rather than calling `_drop` directly.

**Ledger 0556.** **Acceptance:** test PASS both orders; `combat_feedback_inventory_test` and the inventory tests that the affected list names still PASS.

---

## Step 4 — the remaining stops, in chain order

Fix what step 1 found. For the stops I expect:
- Headless E guards: one-line change per owner, as in `l10_main_gate.gd:68`.
- Journal note on growth: add the row to the owner's `JOURNAL_HINTS`, discover it in `l10_silverleaf.gd revisit()` (37) with `MyJournal.discover(host, id)`; add an Atlas plot row in `atlas_places.gd` `PLOT` for L10 if the lead wants the trees marked.
- Leaf count: put "N of 9" in the pick feedback (`l10_silverleaf_harvest.gd:26` reason) and in `l8_journey.gd next_step()`.
Each gets a real-input assertion in the sitting that covers it. One ledger row per presentation choice.

---

## Step 5 — real village views (only if time allows)

**Contract:** E at the village shows the original rendered views (clearing, herbalist, shaman, Daniel) with the same actions as today's text panel; the panel stays until the art version passes.

**Facts:**
- PROVEN: `scripts/lol2/room_stems.json` lists `village_` / VILLAGE.MIX, `shaman_` / SHAMAN.MIX, `herb_` / HERB.MIX, `daniel_` / DANIEL.MIX, and `settle1_`..; all four .MIX files are in `~/lol2_runtime_root/DAT/`.
- PROVEN: `assets/lol2/generated/bacatta_rooms/` holds `VILLAGE`, `CAN` and `rooms.json`. HERB, SHAMAN and DANIEL are **not** converted there.
- LIKELY: they convert with the same producer that made VILLAGE (I did not find or run it; look for the tool that writes `bacatta_rooms/rooms.json`). I cannot say the three will convert cleanly. If they do not, say so on the board before building anything.
- Pattern: `scripts/lol2/monastery_room_view.gd` (`enter_room` 78, `play_patch` 96, `play_idle` 116, `show_frame` 125).
- Owner's reference shots: `~/Downloads/LoL2_P3_106..111_L8-WildVillage_*.png` (I listed them, did not open them).
- Native hook worth knowing (PROVEN bytes, meaning UNKNOWN): controls 63 and 64 sit at the village, Godot (655, 0, -4697) and (519, 0, -4649), next to the port's anchor (676, 32, -4541). Control 64 accepts the Runestone (identity `DC2A401E`, definition 104) and its kind-6 groups address actor 113 (the guard) and prop 119. This may be the original "point to click" at the village. I did not decode it; it is a lead for Grok, not a plan item.

**Build outline:** a view node per stem behind `l8_journey.gd`'s `view` variable (BJ12 added `view`, `show_view()`, `village_view()`); hotspots as rectangles over the picture that call the same `interact()` actions the panel buttons call. Do not duplicate quest logic.

**Test:** rendered mode, real clicks on the hotspots, the same assertions as `l8_village_views_earned_test`, plus a captured frame per view that someone looks at.

---

## Traps I already hit (each cost a round)

1. **Headless root window is 64x64.** A pushed mouse click on a panel button misses silently. Set `root.size = Vector2i(1280, 720)` at the start of any test that clicks.
2. **Mouse capture.** Headless cannot capture the mouse. E handlers that require `MOUSE_MODE_CAPTURED` never fire; left-click sparring cannot be driven (my serum test calls `pop.strike()` for the blows and says so in its header).
3. **Unstaged inputs in a fresh worktree.** `tmp/` is not in git. Missing there, and copied from `~/opus_work/lol2_r18/tmp/`: `dampen_darker_arrival_regression_anchor.json`, `owner_saves/darker_jungle_quicksave.json`, `act2_wild_village_qualified/`. The generated `scripts/lol2/native_scripts/*.json` and `assets/lol2/generated/` are git-ignored too. A test that fails on "anchor" or a sha256 line is staging, not code.
4. **`assets/lol2/doors/indices_478.png`** shows as untracked in lol2_bj12. Leave it; never `git add -A`.
5. **Test aids must be declared.** The walk test undid creature blows; it prints `TEST AID` and its registry row carries `"test_aids"`. Step 0 is meant to remove it. Position sets print `TELEPORT` and are counted in the registry row.
6. **A dead Luther cannot save** ("Invalid player health.", `jungle_save.gd:20`) and the next level then fails to bind its scripts ("progression not bound"), which shows up as dictionary-key errors in `l10_main_gate.gd:60` / `l10_barrel.gd:60`. If you see those, check health first.
7. **Journal notes:** each hint must be <= 130 characters (`tests/l8_village_hints_test.gd:31`) and two tests pin the total count, now 48 (`tests/act1_journal_hints_test.gd:36`, `tests/act3_journal_hints_test.gd:51`). Every new note moves that number.
8. **Lingering `notice`.** `l8_journey.gd` keeps the last notice across panel opens; a branch that writes its text only `if notice.is_empty()` shows the old line. I fixed one; check new branches.
9. **Direct callers.** Old tests call `journey.interact(...)` with the panel closed. Anything that re-opens the panel or pauses must do so only when the panel was open (`at_table` in `interact()`), or their saves are refused ("Close the current overlay before saving.").
10. **Creature piles.** The eight wild Hulines (actors 52-59) gather on one nav midpoint (494, -4080) on the way out of the village; a walker that avoids creatures cannot reach a waypoint under them. My `walk()` counts such a point as passed from 110 units.
11. **Routes.** `tools/build_act3_routes.py AREA --min-width 36 x,z ...` avoids nav edges narrower than the body (a 24-wide edge at L8 2293/2376 stopped the first route). Legs for L8/L10 are in `tests/fixtures/l8_bj12_village_routes.json`.
12. **The runner.** `tools/run_isolated_regressions.py --godot` cannot be given `--audio-driver`. Use a wrapper script (mine: `lol2_bj12/tmp/godot_dummy.sh`, which also waits for MemAvailable >= 10 GiB). The runner snapshots the sources at start and end: **no edits while a gate runs**, or the report says `source_stable: false`.
13. **Never `pkill -x godot-bin` or `pkill -f <pattern>`**: other lanes' engines, and your own shell, match. Kill by PID after checking `/proc/PID/cwd`.
14. **Notes on a long walk test:** `l8_village_views_earned_test` takes ~330 s; give the runner `--timeout 1700`.

---

## State of my own work when this was written

- `bj12-l8-quests` = `b3e384e` + `5b518c9` + `7f5cab5`. Targeted gate (39 L8/L10/drowning tests) green after fixes.
- The BJ12 affected gate (798 tests, sequential) is still running in lol2_bj12: at 241 of 798 with 15 failures when I last looked. I have **not** diagnosed those failures; the first five are rendered Cave/continuity tests (`cave_prop83_lift_live_test`, four `player_continuity_*`), which my changes should not reach except through `liquid_drowning.gd`. I post the result on the board when it finishes. Do not edit or commit in lol2_bj12 until then.
- I created one temporary worktree for the data probe and removed it again. Nothing in lol2_bj12 was edited for this plan.

## What I could not confirm (summary)

- Opcode 17's meaning (inferred from these four groups only).
- Who fires prop 96's kind-6 group 2400, and therefore whether the slots lock while the potion waits.
- That the room's back is walkable in the port and that the slot props have meshes.
- That grown leaves are visible on the trees in a rendered frame.
- That a carried Silverleaf exists in the qualified tree-room chain save.
- How the binder's native state is written to F5 saves.
- That HERB / SHAMAN / DANIEL convert like VILLAGE.
- That pushed mouse events start a drag in headless.
- That 30 health survives the walk without the test aid.
- Why the owner did not drown in r18 at the lake (this tree kills on the 15 s clock; not reproduced on r18).

PLAN READY
