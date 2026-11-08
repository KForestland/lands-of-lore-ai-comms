# Kimi K47 — L8 temple shut / darker start trace

Lead spot-check: l8_temple_door.gd:30 hint, l8_journey.gd:53 visited skip, l8_larkhon.gd:18-25 guidance chain — confirmed. Lead applied the suggested hint fix (r19-work, ledger 0350).

## Darker start state

The F2 "darker" start is manifest entry `act1-end-darker-jungle` (`scripts/lol2/playtest_starts.json:375-416`). It loads the real earned save `assets/lol2/generated/playtest_starts/act1_dark_halls_darker_arrival.json` (sha256-pinned), read through `JungleSave.read_save(path, "lol2-restoration-darker-jungle")` (`scripts/lol2/playtest_starts.gd:111`), and resumes into `darker_jungle.tscn` (`darker_jungle.gd:6,213-216`).

What that save actually carries for L8:

- **No `l8_journey` key at all** → the journey state is the default `initial()`: `gift="unoffered"`, `temple_visited=false`, `admitted=false`, `key_awarded=false` (`scripts/lol2/l8_journey_state.gd:8-9`). So **the temple visit has NOT run**; the priest has not been "killed" by any state.
- No `l8_temple_door` key → door slot at `initial()` (closed, nothing inserted) (`scripts/lol2/l8_temple_door_state.gd:6`).
- No journal/notes key → `l8_see_temple_first` not recorded; notes re-derive live (`scripts/lol2/l8_village_hints.gd:37-42`).
- Player at (-4577, 32, 1168) — the west arrival, ~5300 units from the temple point (758,32,2046), so nothing auto-fires on spawn.
- Inventory contains `jungle:kityara:Empty_hand` (Daniel's blade), no Dreamstone; `act2_items.carried` is null.
- `act2_creatures_L8_SJ`: actor **113 (village guard) `present:false`** — correct, he only spawns after the visit (`scripts/lol2/l8_journey.gd:104-105`).

## Temple visit and door gating

Two separate things at the same world point (758,32,2046), and they are easy to conflate:

**The visit (priest scene).** Pure proximity walk-in: `L8Journey.target()` returns `"temple"` within 160 units with line of sight (`scripts/lol2/l8_journey.gd:7,53`), and `_process` auto-fires `interact("visit_temple")` with no E press when you walk up on foot (`l8_journey.gd:121-126`; pinned by `tests/l8_temple_earned_test.gd:52`: "temple scene fires on approach without E"). `visit_temple` sets `temple_visited=true` with the notice "At the temple, a creature seizes the priest." (`l8_journey_state.gd:53-56`). The priest is presentation text only — there is no priest actor in the L8 population, so no save can have him "already dead". The visit cannot be skipped by state: it fires on approach regardless of save contents.

**The door (prop 1198).** Natively, prop:1198's only event is kind 6 / value 20 under **predicate 136 = local13==1**, dispatching group 11612 = level 14 / selector 1; the local13 writer is the TMPLDOR Dreamstone hotspot module, runtime writer UNKNOWN (`tools/verify_act2_temple_door.py:41-43`; DEVIATIONS rows 323, 401). The port reproduces this as a Kit slot: `L8TempleDoor.can_leave()` requires the Dreamstone (definition 136) inserted and retrieved (`scripts/lol2/l8_temple_door.gd:15,30`, `l8_temple_door_state.gd:11`), and only then `use_exit("prop:1198")` supplies `set_local(13,1)` and fires the original level change (`scripts/lol2/act2_progression.gd:478-482`). The Dreamstone itself is earned much later, in L13: `act2:L13_RC:dreamstone`, "source326 award" (`act2_items_catalog.gd:70`), taken from the citadel altar after the boss and the sword enchant (`scripts/lol2/l13_altar_state.gd:31-37`).

**Predicate 97 / opcode-198 index 6 (native chain, not hosted in the port).** In `native_scripts/L8_SJ.json`: predicate 97 = entry `0003060001` = `[0x26E58+6] == 1`. It is written by opcode 198 `c60000000601` in groups 1044/1092/1140/1188/1236/1284, called by the kind-12 region-entry events of temple-approach regions 1514/1515/1519/1523/1527/1530 under predicate 146 (`0003060000`, i.e. only while e58[6]==0 — first approach). Predicate 97 gates the two village doors prop:531 (~(705,-4636)) and prop:1091 (~(313,-4661)): their pred-97 kind-5/6 groups 7728/7770/9334/9376 run opcodes 9/13/14 on **actor 113** (summon/move the guard); their unpredicated groups 7722/9328 are just an opcode-197 blocker. So natively "temple approach sets e58[6]" is the same "visit → village opens" chain. In the port this chain is deliberately not executed: `locals_e58` is only ever seeded for L19_BC (`act2_progression.gd:30`), so predicate-146/97 reads evaluate as "unhosted" (`native_script_host.gd:874-876`), and the modern `l8_journey.temple_visited` owns the chain instead (DEVIATIONS row 328).

## Village admission

`L8Journey.target()` suppresses the village encounter until `temple_visited` (unless the blade is already recovered/returned) and shows "Visit the Huline Temple first…" (`l8_journey.gd:8-9,54-55,127-133`). After the visit, guard actor 113 is spawned (`l8_journey.gd:104-105`; DEVIATIONS row 328), and admission requires showing Daniel's recovered blade (`l8_journey_state.gd:57-62`). Admission then unlocks shaman/cemetery key, tribe initiation, and Silverleaf; Silverleaf + Amaranth Serum → Larkhon Vapors → Larkhon asleep → L8→L12 exit (`scripts/lol2/l8_larkhon.gd:18-25,70-77`; DEVIATIONS row 442). So admission — and therefore the whole route to the Dreamstone — strictly post-dates the temple visit.

## Dead-end analysis

- **The closed temple after the priest scene is faithful, not a bug.** STORY-049 / Prima 129,131: the temple door takes the Citadel Dreamstone and gives it back (DEVIATIONS row 401). First arrival: you see the priest scene, the door is sealed, you go to the village. The owner read intended behaviour as a defect.
- **No path leaves the door shut while the visit has not run.** The door only matters once you hold the Dreamstone; the stone requires the L13 boss, which requires L12, which requires the sleeping Larkhon, which requires Vapors ← Silverleaf ← tribe membership ← village admission ← `temple_visited`. The visit auto-fires on approach, so the prerequisite order is unbreakable. Even a hypothetical stone-without-visit state would still open the door — `can_leave()` never checks `temple_visited` (`l8_temple_door.gd:15`).
- **From the darker start specifically** there is also no divergence: the save has `temple_visited=false`, guard absent, blade in inventory — the full chain is playable from the unoffered gift onward, exactly as after a natural Act-1 completion.
- The only genuine rough edge is **presentation**: at the sealed door with no stone, the hint still reads "E — Place Dreamstone" (`l8_temple_door.gd:30`), and pressing E answers only "The slot needs the Dreamstone." Guidance does exist — standing at the closed door records the journal note `l13_dreamstone`: "The Dreamstone is past the Hive Lord. Dawn's lock and the temple door both take it, and both give it back." (`scripts/lol2/l13_journal_hints.gd:8,38-41`, attached in `darker_jungle.gd:234`) — but the on-screen hint itself invites an impossible action.

## Suggested fix (smallest, faithful)

No quest-logic change is warranted — the gating matches the original (DEVIATIONS rows 401, 328). The minimal fix is to make the sealed door self-explanatory in `scripts/lol2/l8_temple_door.gd:28-43`:

- In `_process`, when the slot is empty and no definition-136 item is in `host.carried_collected`, replace `"E — Place Dreamstone"` with a sealed message, e.g. `"The Temple entrance is sealed. Only the Dreamstone opens it."` (the journal note already explains where it is).
- In the insert path (`l8_temple_door_state.gd:11` / the `""`-item refusal in `l8_temple_door.gd:38-42`), return that same sealed reason when the player carries no Dreamstone, instead of "The slot needs the Dreamstone."

That closes the owner's "closed because the priest died" misreading at the exact point of confusion, touches no saved state or gating, and keeps the original predicate/local13 chain untouched.

