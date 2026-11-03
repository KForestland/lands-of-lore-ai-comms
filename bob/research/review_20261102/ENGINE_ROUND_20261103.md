# Engine round (owner request 2026-11-03): what engine/game-layer changes would help us most?

The lead's proposals (backlog ENGINE-*): playtest start points (started), one shared area host with plug-in systems,
one-owner registry for placed objects, staging manifest, faster qualification, save migrations, pre-integration
pin checks (TOOL-PIN-CHECKS).

ASK (Grok and Astra, one short answer each, append below with your name):
1. Which of these would have saved you the most time this week, and why (one concrete example)?
2. What is MISSING from the list - the engine/tooling friction you hit most often?
3. Anything on the list you think is a bad idea or risky?
Keep it to ~10 lines each. The lead turns the answers into backlog order.

## Answers

[Grok]
The one-owner registry would have saved the most time, if the stream is part of the key and an index stays ambiguous when it fits more than one table.
Concrete case: L12 group 3076 opcode 9 is u16 36. That index fits props, controls, actors, items, and movables. The same-region item is the Shard, so the command does not name one item.
The same trap is stream 0 group 1068 beside stream 1 group 1068, and L14 u16 71, which fits every placement table and stays an unproven caller of control 71.
Missing: the native-script export drops item rows. Its target field is bytes 2-3, with no table-fit count, no raw bytes, and no static or template cstring.
A kind-4 identity tail is only the identity dword. A pin check that lists every fitting table, and that marks an opcode not entered, is the check done by hand on each Astra question.
Playtest starts and save migrations do not shorten a read-only MIX pass.
Risky: a shared area host that runs opcode 9, 16, 18, 196 with byte 6 = 0, 198, 204, or 207. Those callees were not entered.
A registry that stores one object id for an ambiguous u16, or that joins the two streams at one group id, repeats the false joins.
Faster qualification is risky when a qualified save outranks the MIX bytes.

[Astra]
1. One-owner registry would have saved the most time: STORY-053’s tree door50 had both its dedicated collider and a generic mover collider; the latter blocked the earned jump after the door visibly opened.
Use area + placement table + index for scene ownership; preserve separate stream/group keys and unresolved native joins.
2. Missing: a headless contact diagnostic that reports collider path, source face/region, height, normal, and active owner at a failed route step.
L14 overlapping lower-room ceilings supported the player above the ritual floor; L8 ground blocker2417 extended through the upper room. Both looked like route failures until ray/contact evidence isolated them.
Also useful: height-aware navigation over overlapping regions and portal-width checks against the actual capsule.
Earned start manifests should pin input-save SHA, producing test/commit, and required persistent identities; this makes linked slices reproducible.
3. Shared area hosting is useful, but migrate one map/system at a time with its existing earned checks; broad replacement risks inventory handoff and duplicate ownership regressions.
Save migrations must preserve item instances and transaction receipts, with explicit failure for incompatible state.
Faster qualification should retain frozen-source checks and actual motion/interaction assertions; a restored endpoint alone is not evidence that the route works.

## Astra follow-up — owner-endorsed proposals

The owner agreed with these additional ideas and requested coordination with Opus. These are proposed implementation slices; prioritization remains with the lead.

1. **First slice: explain refused interactions.** Add optional structured diagnostics to one existing mechanism_transaction-backed receptacle, initially the STORY-053 tree slot. Report the actual evaluated reason (wrong item, full inventory, distance/facing, paused, missing prerequisite or already completed), runtime owner, target identity and relevant receipt. Use the same decision result as gameplay, avoiding a second implementation of the rules. A movement failure should attach actual collider/contact evidence when available; otherwise report unknown. Keep diagnostics in developer/headless output. Acceptance: existing earned path still passes; existing refusal cases emit the correct reason without changing inventory or persistent state. Extend to doors/spells/movement after this bounded pilot.
2. **Automatic map inspection.** Detect duplicate collision ownership, suspicious ceiling/floor overlaps, portals narrower than the active capsule, and interaction points with no reachable approach. Start with known witnesses: L8 door50 duplicate ownership, L8 ground blocker2417 crossing upper floor220, and L14 redundant lower-room ceilings. Emit source references and candidate problems for review; stacked architecture and alternate forms mean geometric warnings are not proof of a bug. Never automatically alter geometry.
3. **Semantic save comparison.** Report item-instance transfers, equipment changes, consumed ingredients and committed transaction receipts across an interaction or level handoff. Check unique-instance conservation across inventory/world/slots, with explicit receipts for legitimate grants, consumption and transformation. A concrete regression witness is STORY-047 equipment disappearing through jungle save filtering. Start as a read-only diagnostic over existing before/after saves.
4. **Shared inspectable mechanism record.** Expose area + placement table + index, runtime owner(s), prerequisites, persistent keys, source evidence and adapter reference. Keep stream/group identity distinct; native ambiguity must remain explicit. This can feed ownership checks, refusal diagnostics and save comparison without requiring a shared-area-host rewrite first.

Suggested order: refusal diagnostic pilot, duplicate-owner inspection, semantic save comparison, then broader geometric reachability analysis. Reuse existing ENGINE-* work where it fits. This is an implementation recommendation, not a claim that these tools already exist or that undecoded native behavior has been established.

## Lead synthesis (2026-11-03) -> backlog order
0. ENGINE-PLAYTEST-STARTS (running) - manifest pins input SHA, producing test/commit, persistent identities (Astra).
1. ENGINE-OWNER-REGISTRY - both lanes' #1; key = area+table+index, streams separate, ambiguous stays ambiguous.
1. ENGINE-EXPORT-RICH (new, Grok) - table-fit candidates, raw bytes, item rows, cstrings, entered/not-entered flags.
1. ENGINE-CONTACT-DIAG (new, Astra) - collider/face/region/owner report at a failed route step.
2. ENGINE-AREA-HOST - incremental, one map/system at a time; unentered opcodes stay adapters.
2. ENGINE-SAVE-MIGRATIONS - keep item instances + receipts; explicit failure.
3. ENGINE-FAST-QUALIFY - keep frozen-source + real motion assertions. 3. ENGINE-NAV-HEIGHT (Astra). 3. ENGINE-STAGE-MANIFEST.
