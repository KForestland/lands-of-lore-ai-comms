# Kimi K55 — struck (kind-9) events: L20 chase doors + a generic binder (prep for Grok BK08)

Lead spot-check: act2_progression.gd setup kind-4 scan around :183 and the L20 native script carry kind-9 records - confirmed. LEAD DECISION: build the generic struck binder (not a per-door host); log the three adapters (strike masks, remaining-durability dword_26, global_23331=0); exclude bespoke hosts (bramble/dam, L12 frozen bow/crevasse controls 89/91); persist record_state or log the reset; L10 mode-3 stays out of scope.

## Event firing today
- native_script_host.gd fire_event (:524) two-phase; kinds matched in _match_object (:661); kind 9 matcher _match_kind9 (:761): masks word0/word2 (+4/+6), mode byte9&7: 0 reject, 1 (byte8 vs dword_1e), 4 (byte8 vs dword_26 + global_23331), >4 reject, 2/3 undecoded→unhosted (:820). One kind-9 record enqueued per hit (:540-547). Predicate evaluation _evaluate_predicate (:848), left type 5 = context object byte+0x25 (:861-868); trailer kind-0x13 supplies predicate index (:278-283).
- act2_progression.gd fire() (:306) wraps fire_event + route_log. Bound triggers: region entry kind 12 event 2 (:339-342), E on scripted movable → kind 4 (scripted_movables list built :183-188, aimed() :458, use() :472-474 fires kind 4 with arg_c 0 + context), exit_objects/use_exit (:478-496) fires kinds 5/6 with caller bytes, timers kind 2 (:229-244). _unhandled_input handles only KEY_E (:517-532). No kind-9 binding anywhere; no caller fires kind 9 (grep).

## Melee hit resolution
- No generic melee dispatcher in act2_map.gd or jungle_walkthrough base; every strike owner registers its own _unhandled_input LMB + camera raycast and calls set_input_as_handled. Creatures: scripted_creature_population.gd:355-376 (STRIKE_REACH 110, mask 3, meta population_owner), _unhandled_input :398-400. Bramble: jungle_bramble.gd:185-191 strike() → raycast mask 2 vs own hit bodies (aimed_id :234-242), receive_hit :193 models kind-9 masks by hand. River dam: jungle_river_dam.gd:253-265 (ray mask 1 vs its rock body; receive_hit :267-268 comments the native kind-9 admission). l16_dragon_room.gd:97-103 aim-dot only, sets quest flag, no raycast, no native fire. HUD swing: museum_interface.gd:252 + attack_swing.gd:86; landed-report via combat_feedback.gd:11.
- Identifying a movable: binder builds AnimatableBody3D per mover (act2_progression.gd:381-387, collision_layer 1, mover_bodies map id→body). mover_ids (:99-109) = opcode-1 targets + kind-4 owners; in L20 all movables 50-99 are opcode-1 targets, so doors 50-54 (and 55, 99) already have drawn hinges and collision bodies. A camera ray on mask 1 whose first hit collider is in mover_bodies identifies the movable id (reverse map needed). Controls have no hinge bodies; their colliders are the static-assembly solid bodies (preview_assemblies.solid_bodies), where present.

## L20 doors 50-54 native
From L20_BB.json:
- movable:50: 4 kind-9 records (stream 1): g9254 mask2 0x0004 byte8 190 mode 4; g9266 same byte8 100; g9278 byte8 1 + predicate 206 (0005000000 = context byte+0x25 == 0); g9332 mode 1 byte8 1, pred 206. Plus kind-6 g9342 (caller 0x0f).
- movable:51: g9360/9372/9384 (same pattern; pred 206 on g9384), g9438 mode 1 + pred, kind-6 g9448/9454.
- movable:52: NO kind-9; only kind-6 g9472 (caller 0x0f; group runs op14 arm3 on prop:2 — a timer).
- movable:53: g9480/9492/9504 (no predicate on the open group!), g9540 mode 1 + pred 206.
- movable:54: g9550/9562/9574 (no pred), g9610 mode 1 + pred 206.
- Also movable:55 (g9620/9638/9656/9692, prop 235 enqueues) and movable:99 (g11376...11448) have the same 4-record pattern — paired second door.
- Groups: first two = op5 selector 1/2 (damage frames). Third (open): op9 arm 0x15 enqueue prop 112/113 kind-6 caller 0x14; op16 byte+0x25=1 on both leaves (owner-state → 1); op9 arm 0x0E set byte+0x15 bit 0x80 (the 0xB5000 skip-walk bit = opened); op5 selector 3; op1 travel 0x64 (rotary swing open, mode 6 from placement byte 0x22 = 6). Fourth = op20 sound (request ...).
- Record semantics: byte9 bit 0x80 set on the mode-4 records → one-shot (matcher clears byte9 after enqueue, :822-826). Thresholds 190/100/1 vs dword_26 (mode 4, :791-808) accept when dword_26 <= byte8; placement byte 0x1E = 0xFF (initial durability 255, FIELD_BYTE26 at load :335). So door opens after ~254 accumulated damage, frames at <=190 and <=100 — if dword_26 is carried as remaining durability (adapter; the dam precedent jungle_river_dam.gd:267-290 models exactly this).
- All group opcodes (1, 5, 9, 16, 20) have host handlers (register_builtins :370-391). Predicate 206 needs input context = the movable ref (:861-868) and byte_0x25 initial 0 (:335).

## Other unhosted kind-9 events
Scan of native_scripts/*.json for kind-9 records on movable:/control: objects:
- Binder-hosted levels today (act2_map + darker_jungle L8 + dragon_level L9):
  - L8_SJ: 1 (control:82 g12844, mask0 0x1FFF mask2 0x0007, mode 4 one-shot; arms op9 arm2/arm8 on itself)
  - L9_DR: 40 records on 23 objects (controls 84-87; movables 0,3,4,72-85,131,132; modes 1/4). e.g. movable:0 g17356 (mode 4, threshold 2; op9 arm2 + enqueue prop:3)
  - L10_DC: 142 records on 30 controls (5, 62, 241-256, 262-273); 113 are mode 3 — matcher mode 3 is NOT decoded (:820 "unhosted"), so a struck binder alone won't host those; 29 mode 1.
  - L12_CM: 2 (control:89 g3048 mask0 0x0011 mode 4 pred 206; control:91 g3198 mask0 0x0008 mode 4 pred 206) — the frozen bow/crevasse targets (l12_frozen_bow.gd:26, l12_crevasse.gd:14 own the same-numbered assemblies and disable their collision once solved).
  - L14_HT: 1 (control:151 g19078, mask0 0x000A mode 1 one-shot; op9 arm 0x12 + sound + byte25=1 + selector 1)
  - L20_BB: 24 records on 6 movables (50,51,53,54,55,99) — the BK08 doors.
  - L13_RC, L16_CA, L17_HC, L19_BC: none.
- Not binder-hosted (Act 1 hosts): L1_DC 3, L3_DH 4, L4_HJ 66 (25 objects incl. bramble controls 101-109, modeled bespoke by jungle_bramble.gd, NOT fired through the native host), L7_DH 99 (92 objects, mostly mode 4 — Dark Halls, its own route hosts, no NativeHost binding).

## Recommended design + risks
Generic struck binder in act2_progression.gd:
- At setup, collect struck ids: every movable/control ref with >=1 kind-9 record (mirror the scripted_movables loop :183-188).
- LMB in _unhandled_input (next to KEY_E at :517): guard same conditions; raycast camera forward ~140 (bramble/dam convention; creatures use 110), mask 1 (world + mover bodies; movers are layer 1, :384), exclude player. If first hit collider is a mover body (reverse mover_bodies) → ref movable:N; for controls, match preview_assemblies.solid_bodies. Then fire(ref, 9, input) with input: word0/word2 = the weapon's strike masks (adapter — precedents: sword cut 0x080E/0x0004 jungle_bramble.gd:21-22, dam melee 0x0906/0x0004 jungle_river_dam.gd, spark 0x0091/0x0003; unarmed refused per bramble :187 and dam :262), dword_26 = remaining durability after damage (adapter, needs a per-object durability ledger seeded from placement byte 0x1E / FIELD_BYTE26 and decremented by Forms.melee_damage — the river-dam model), dword_1e = damage, global_23331 = 0 (adapter), context = ref (predicate left type 5).
- Report landed hits through combat_feedback.landed (combat_feedback.gd:11) so the HUD ring splash works (attack_swing.gd:104-119).
- Native one-record-per-hit rule already enforced (:540-547); one-shot byte9-bit7 rewrite already modeled (:822-826); rejected/unhosted rows land in route_log via fire() (:306-314).

Risks:
1. Double-fire with bespoke strike hosts that model the same records by hand: jungle_bramble (L4_HJ controls 101-109) and jungle_river_dam (L1? jungle) — both are on Act 1 jungle_walkthrough maps without the binder today, but act2_jungle_return.gd (LEVEL_SCENES[4]) shares jungle_walkthrough and instantiates bramble (jungle_walkthrough.gd:162-165); if the binder is ever attached to L4_HJ or the struck binder goes into a shared base, controls 101-109 would fire natively AND run the bespoke model. Mitigation: per-area exclusion lists like the hinge exclusions (:358-361) or skip refs a dedicated host owns.
2. Input arbitration/order: creatures' population host, bramble, dragon_room etc. all listen to LMB in _unhandled_input; Godot delivers deepest/latest nodes first. progression is added before act2_creatures in act2_map.gd:159-165, so creatures get the click first — good (a creature in front of the door absorbs the hit). But a binder ray on mask 1 ignores creature bodies (layer 2, scripted_creature_population.gd:60), so with a creature between camera and door the creature host handles it and the door doesn't fire (correct), while aimed side-by-side could let both fire if neither calls set_input_as_handled first — must call set_input_as_handled on an accepted fire and return without firing when the creature ray would hit closer. Simplest: compare hit distance — if any layer-2 strike target is closer than the movable, stand down (or just let ordering handle it and only fire when nothing handled the click — the default since _unhandled_input stops after handling).
3. dword_26 semantics is an adapter (UNKNOWN natively): damage vs remaining-durability changes how many hits a door takes. The 190/100/1 thresholds + placement durability 0xFF fit the remaining-durability reading (river-dam precedent), but it must be logged as an adapter per the lead rule.
4. Mode 3 undecoded (:820): L10's 113 records stay unhosted — firing kind 9 there logs unhosted rows; harmless but noisy; don't claim BK08 fixes L10.
5. Mode-4 records with bit7: after the rewrite byte8 becomes UNKNOWN; a later fire of the same record rejects as mode 0 — correct, but save/load must carry record_state (the bank already saves record_state across level changes, :293-297; act2_save must persist it too — check save coverage).
6. L20 movable 52 has no kind-9 (only kind-6 caller 0x0f timer on prop:2): BK08's "50-54" really means 50,51,53,54 (paired leaves 50+51 and 53+54; open groups move both leaves of a pair). 55+99 are a second paired door (armory-side?) that the same binder opens for free.
7. Doors' collision while open: hinge mover bodies keep collision layer 1; opened rotary doors rotate away via travel (op1 0x64 → _pose :414-432) — the body moves with the hinge, fine; but mode-6 pose uses travel directly, and op1's travel target semantics on mode 6 is the proven path (FIELD_TRAVEL :60).

Alternative: a per-door host (l20_chase_doors.gd) like l16_dragon_room: cheaper, but duplicates the masks/predicate/durability by hand again (the bramble pattern) and leaves L8/L9/L12/L14 kind-9 records dead; the generic binder is ~40 lines in act2_progression.gd and hosts 24 L20 records + ~66 more across L8/L9/L12/L14 with the same code.

I should also double check save coverage of record_state in act2_save quickly? That's a detail; the bank saves across level changes. Quick grep act2_save for record_state.

• One last check on save persistence of the native record state (needed for the one-shot door records):

• act2_save.gd does not persist record_state — the native host state survives level changes via the tree meta bank (act2_progression.gd:293-297) but is not saved to disk. Worth flagging as a risk for one-shot door state across save/load.

Now write the final report.

• # K55 / BK08 research: L20 "attack the door" (kind-9 STRUCK on movables 50–54)

All read-only; branch `r19-work` at `~/opus_work/lol2_r18`.

## Event firing today

- `scripts/lol2/native_script_host.gd:524` `fire_event(object_ref, event_kind, input)`: two-phase — every record of the object whose kind byte == event_kind is matched (`_match_object`, :661), predicates evaluated (`_evaluate_predicate`, :848; trailer kind-0x13 record supplies the predicate index, :278-283), accepted groups run via `_run` (:902) with per-record status `ran`/`rejected`/`unhosted` + reasons.
- Kind-9 matcher `_match_kind9` (:761): mask0 = u16 +4 vs `input.word0`, mask2 = u16 +6 vs `input.word2`; mode = byte +9 & 7. Mode 0 rejects ("byte +9 cleared after an enqueue", :784-787); mode 1 accepts when byte+8 ≤ `dword_1e` (:809-818); mode 4 accepts when byte+8 ≥ `dword_26` and also needs `global_23331` (:791-808); modes 2/3 → `unhosted` (:819-820). Byte +9 bit 0x80 = one-shot: after an enqueue the matcher clears byte+9 and writes byte+8 back as UNKNOWN (:822-826). Native one-record-per-hit rule (0xAE2C8) is enforced: later kind-9 records report `not_reached` (:540-547).
- Predicate entry bytes: `[op, left_type, operand, right_type, literal]`; op 0 = equality; left type 5 = byte +0x25 of the object named by `input.context` (:861-868). Kind-9 records carry no 0xB5000 gate (that gate is kind-4-only, :554-577).
- `scripts/lol2/act2_progression.gd:306` `fire()` wraps `fire_event` and logs per-group verdicts to `route_log`. Bound triggers today: region-entry kind 12 event 2 (:339-342), kind-2 timers (:229-244), exit/controls kinds 5/6 via `use_exit` (:478-496), and **movables: kind 4 (E) only** — `scripted_movables` is built from kind-4 records (:183-188), `use()` fires `kind 4, arg_c 0, context` (:472-474), and `_unhandled_input` handles only `KEY_E` (:517-532). No code path anywhere fires kind 9 through the host (grep for `, 9,` / kind-9 callers confirms zero).

## Melee hit resolution

- There is **no generic melee dispatcher** on Act 2/3 maps. `act2_map.gd` has no strike code; every strike owner registers its own `_unhandled_input` on LMB and calls `set_input_as_handled()` when it lands:
  - Creatures: `scripted_creature_population.gd:355-376` — camera ray, `STRIKE_REACH 110`, mask 3, collider must carry `population_owner`/`population_actor` meta; `_unhandled_input` at :398-400. Creature bodies are collision layer 2 (:60).
  - Bramble (the bespoke kind-9 model): `jungle_bramble.gd:185-191` `strike()` → ray mask 2 against its own hit bodies (`aimed_id`, :234-242); `receive_hit` (:193) hand-models the native masks (cut `0x080E/0x0004`, spark `0x0091/0x0003`, :19-22) and durability.
  - River dam: `jungle_river_dam.gd:253-265` ray mask 1 vs its rock body; :267-290 models "native kind9 admission (masks 0x0906/0x0004, predicate owner state 0, mode4 threshold first, else mode1)" with a durability ledger — the closest existing precedent for the L20 doors.
  - `l16_dragon_room.gd:97-103` — aim-dot only, sets a quest flag; no raycast, no native fire.
  - HUD: `museum_interface.gd:252` plays the swing on every LMB (`attack_swing.gd:86`); landed hits are reported via `combat_feedback.landed()` (`combat_feedback.gd:11`) for the ring splash.
- **Identifying a movable is already cheap**: the binder builds an `AnimatableBody3D` per mover under its hinge (`act2_progression.gd:381-387`, `collision_layer = 1`) with `mover_bodies[id]` mapping id → body. `mover_ids()` (:99-109) = all opcode-1 targets ∪ kind-4 owners — in L20 every movable 50–99 is an opcode-1 target, so **doors 50–54 (and 55, 99) already have drawn hinges and collision bodies**. A camera ray on mask 1 whose first hit collider is in `mover_bodies` (reverse map) names the movable. Controls have no hinge bodies; their colliders, where they exist, are `preview_assemblies.solid_bodies[id]`.

## L20 doors 50-54 native

From `scripts/lol2/native_scripts/L20_BB.json` (all stream 1; record layout `0a 09 | group | mask0 | mask2 | byte8 | byte9`):

| movable | kind-9 records (group: mask0/mask2, byte8, mode, pred) | other |
|---|---|---|
| 50 | 9254: -/0x0004, 190, m4 · 9266: -/0x0004, 100, m4 · 9278: -/0x0004, 1, m4, **pred 206** · 9332: -/0x0004, 1, m1, pred 206 | kind 6 g9342 (caller 0x0f) |
| 51 | 9360/9372/9384 (same; pred 206 on 9384) · 9438: m1, pred 206 | kind 6 g9448, g9454 |
| 52 | **none** | kind 6 g9472 (caller 0x0f → op14 arm 3 on prop:2, a timer) |
| 53 | 9480/9492/9504 (no pred on the open group) · 9540: m1, pred 206 | — |
| 54 | 9550/9562/9574 (no pred) · 9610: m1, pred 206 | — |
| 55 | 9620/9638/9656/9692 (same pattern, prop 235) | — |
| 99 | 11376/11394/11412/11448 (same pattern, prop 235) | — |

- mask0 = 0, mask2 = `0x0004` on every record — the melee/cut bit (same bit as bramble's cut mask and the dam's melee mask).
- Predicate 206 = `00 05 00 00 00`: op 0 (==), left type 5 → **context object's byte +0x25 == 0**, i.e. owner-state 0 (byte +0x25 is initialized to 0 at load, `native_script_host.gd:335`).
- All mode-4 records have byte9 = 0x84 → mode 4 + one-shot bit. Byte8 thresholds **190 / 100 / 1**; placement byte +0x1E = 0xFF (initial durability 255, stored as `FIELD_BYTE26`, :335). Reads naturally as remaining-durability thresholds: damage frame 1 at ≤190, frame 2 at ≤100, open at ≤1 (the dam's model exactly). Durable → several strikes per door.
- Groups: 9254/9266 = `op5 selector 1/2` (damage frames). Open group 9278 (8 commands): `op9 arm 0x15` enqueue prop:112's kind-6 caller 0x14; `op16` byte +0x25 = 1 on movables 50 **and** 51 (owner-state flips on both leaves); `op9 arm 0x0E` sets byte +0x15 bit 0x80 on both (the 0xB5000 "skip walk" bit = opened); `op5` selector 3; `op1` travel word 0x64 on both (rotary swing — placement byte +0x22 = mode 6, so `_pose` :414-419 rotates the hinge). Fourth record (9332 etc.) = `op20` sound, repeatable while owner-state is 0.
- All opcodes used (1, 5, 9, 14, 16, 20) have host handlers (`register_builtins`, :370-391). Firing kind 9 today needs only the right `input` (`word2` with bit 0x0004, `dword_26`, `dword_1e`, `global_23331`, `context`).
- Note: BK08's "50-54" is really **50/51 (paired leaves) and 53/54 (paired leaves)**; 52 has no kind-9. 55+99 are a third paired door the same mechanism opens for free.

## Other unhosted kind-9 events

Scan of `native_scripts/*.json`, kind-9 records on `movable:`/`control:` objects (modes in parentheses):

**On binder-hosted levels** (act2_map scenes + darker_jungle L8 + dragon_level L9):
- **L20_BB**: 24 records / 6 movables (m4: 18, m1: 6) — this task.
- **L9_DR**: 40 records / 23 objects (controls 84-87; movables 0,3,4,72-85,131,132; m1: 21, m4: 19). e.g. movable:0 g17356 (m4, threshold 2 → op9 arm 2 + enqueue prop:3), control:84 g14668 (m1 → op5 selector 1).
- **L10_DC**: 142 records / 30 controls (5, 62, 241-256, 262-273) — but **113 are mode 3, which the matcher does not decode** (:820 → `unhosted`); a struck binder alone does not host these. 29 mode-1 records would work.
- **L12_CM**: 2 — control:89 g3048 (mask0 0x0011, m4, pred 206 → op16/op8×2) and control:91 g3198 (mask0 0x0008, m4, pred 206 → op5/op7). `l12_frozen_bow.gd:26` / `l12_crevasse.gd:14` own the same-numbered assemblies and zero their collision once solved.
- **L8_SJ**: 1 — control:82 g12844 (mask0 0x1FFF, mask2 0x0007, m4 one-shot → op9 arms 2/8 on itself).
- **L14_HT**: 1 — control:151 g19078 (mask0 0x000A, m1 one-shot → op9 arm 0x12 + sound + byte25=1 + selector 1). No dedicated host references control 151.
- L13_RC, L16_CA, L17_HC, L19_BC: none.

**Not on the binder** (Act 1 hosts; would need the binder attached first): L1_DC 3, L3_DH 4, L4_HJ 66 (25 objects incl. bramble controls 101-109 — already modeled bespoke by `jungle_bramble.gd`, *not* fired through the native host), L7_DH 99 records / 92 objects (Dark Halls, mostly m4; its route hosts don't use NativeHost at all).

## Recommended design + risks

**Recommended: a generic "struck" binder inside `act2_progression.gd`** (~40 lines), not a per-door host.

1. In `setup()`, beside the kind-4 scan (:183-188), collect `struck_objects`: every movable/control ref with ≥1 kind-9 record; build reverse maps `mover_bodies` body→id and (for controls) `preview_assemblies.solid_bodies` body→id.
2. In `_unhandled_input` (:517), on LMB with the same guards as the other strike hosts (captured mouse, not paused/flying, form/weapon present per bramble :187 / dam :262): camera ray, reach ~140 (bramble/dam convention; creatures use 110), mask 1, exclude the player. If the first hit maps to a struck object, call `fire(ref, 9, input)` and `set_input_as_handled()`.
3. `input`: `word0`/`word2` = the weapon's strike masks (**adapter** — precedents: sword cut `0x080E/0x0004` `jungle_bramble.gd:21-22`; dam melee `0x0906/0x0004`; spark `0x0091/0x0003`), `dword_1e` = damage, `dword_26` = **remaining durability after the hit** (**adapter**, natively UNKNOWN) from a per-object ledger seeded from placement byte +0x1E (`FIELD_BYTE26`) and decremented by `Forms.melee_damage` (+ `item_effects.melee_damage`, the dam's exact recipe `jungle_river_dam.gd:261-265`), `global_23331` = 0 (**adapter**), `context` = ref (required by predicate 206).
4. Report accepted fires through `combat_feedback.landed()` so the HUD ring splash works.
5. One-record-per-hit (:540-547), the one-shot byte9 rewrite (:822-826), and route_log verdicts come free.

A per-door host (`l20_chase_doors.gd`, the `l16_dragon_room.gd` pattern) would re-hand-model masks/predicate/durability a third time (after bramble and dam) and leave the ~69 other binder-hosted kind-9 records (L8/L9/L12/L14) dead. The generic binder hosts all of them with the same code — but log the three adapters above per the lead rule.

**Risks** (file:line):
1. **Double-fire with bespoke kind-9 models**: `jungle_bramble.gd` (L4_HJ controls 101-109) and `jungle_river_dam.gd` both live on `jungle_walkthrough.gd` (:162-165), which `act2_jungle_return.gd` (LEVEL_SCENES[4], `act2_progression.gd:18`) also extends — today it never attaches the binder, so no conflict, but if L4_HJ is ever binder-hosted or the struck logic moves into a shared base, controls 101-109 would run both the bespoke model and the native records. Mitigation: per-area exclusion lists, same pattern as the hinge exclusions (:358-361).
2. **Input arbitration**: creature population, bramble, dragon_room all share the LMB `_unhandled_input` channel. `progression` is added before `act2_creatures` (`act2_map.gd:159-165`), and Godot delivers unhandled input to later/deeper nodes first, so a creature in front of a door absorbs the click — desirable. But the binder's mask-1 ray can't see creature bodies (layer 2, `scripted_creature_population.gd:60`), so never fire when the click was already handled, and only handle on an accepted/`ran` result — otherwise swings at a creature standing against a door could double-count.
3. **`dword_26` semantics is an adapter**: damage vs remaining-durability changes the door's hit count by an order of magnitude. The 190/100/1 thresholds + durability 0xFF support the dam-style remaining-durability reading, but it must be logged as an adapter, not PROVEN.
4. **Mode 3 undecoded** (`native_script_host.gd:819-820`): L10's 113 records stay `unhosted` even with the binder; don't let BK08 claim L10. `not_reached`/`unhosted` rows will accumulate in `route_log` — noise, not failure.
5. **Persistence**: the one-shot byte9/byte8 rewrites live in `record_state`, which survives level changes via the meta bank (`act2_progression.gd:293-297`) but `act2_save.gd` does **not** persist any native state — a save/load on L20 resets struck-door progress. Either persist `record_state`/`state` or accept the reset as a logged deviation.
6. **Scope correction**: movable 52 has no kind-9 (only kind-6 caller 0x0f → prop:2 timer); the chase doors are the pairs 50+51 and 53+54, and 55+99 come along. Open groups already move both leaves of a pair (op1 on both), and mark both opened (op16, op9 arm 0x0E), so the predicate's owner-state flip is consistent per pair.

