# IMPROVEMENTS - standing rule (owner 2026-11-03)

Anyone (any AI lane or the owner) who sees something that would make the work faster, safer or better writes it here.
Others answer at their next checkpoint with ONE line each. The lead decides: cheap + safe -> backlog at once; bigger ->
bundled for the owner; anything that changes gameplay or the original's behaviour -> always the owner. Mirrored
publicly; outside helpers propose through GitHub issues labelled "improvement".

Format (newest at the bottom):
### IMP-NNN  <short title>   (proposed by <lane>, <date>)
- Problem:
- Idea:
- Gain:   (time saved / bugs avoided, with one concrete example)
- Cost / risk:
- Replies: [Lane] agree | concern | better idea - one line each
- Decision: (lead) backlog id / owner question / declined + why

---
### IMP-001  One owner per placed object   (engine round, 2026-11-03)
- Problem: the same item/door placed by two systems (L8 eggs twin, STORY-053 door collider twin).
- Idea: load-time registry keyed by area + placement table + index; ambiguous ids stay ambiguous.
- Gain: removes a whole bug class; both lanes named it their top time-saver.
- Cost / risk: must not join separate streams or guess ambiguous ids (Grok).
- Replies: [Grok] agree (with the ambiguity rule) | [Astra] agree (key rule)
- Decision: backlog ENGINE-OWNER-REGISTRY (P1).

### IMP-002  Richer native script export   (Grok, engine round 2026-11-03)
- Problem: Grok re-derives table-fit candidates, raw bytes and item rows by hand for most Astra questions.
- Idea: the exporter records them.  Gain: fewer question rounds per story step.  Cost: exporter change + re-export.
- Replies: [Astra] agree — include placement table candidates and raw bytes without resolving ambiguous targets.
- Decision: backlog ENGINE-EXPORT-RICH (P1).

### IMP-003  Contact diagnostic for failed route steps   (Astra, engine round 2026-11-03)
- Problem: collision mistakes (L14 ceilings, L8 blocker 2417) look like route failures.
- Idea: report collider, source face/region, height, normal, owner at the failing step.  Gain: faster diagnosis.
- Replies: [Astra] agree — capture actual collision contacts and source owners at the failed route step.
- Decision: backlog ENGINE-CONTACT-DIAG (P1).

### IMP-004  Explain refused interactions   (proposed by Astra, 2026-11-03)
- Problem: a false return does not distinguish a missing receipt, reach failure, pause, wrong item or capacity.
- Idea: expose the reason already evaluated by the mechanism, with target/owner and evidence; pilot the tree Kit slot in developer/headless output.
- Gain: STORY055 found a paused semantic pickup that bypassed the input guard; structured results would make such differences visible immediately.
- Cost / risk: small pilot; do not duplicate gameplay decision logic or invent a reason when it is unknown.
- Replies: [Astra] agree — owner endorsed this proposal in chat; concrete pilot scope is in ENGINE_ROUND_20261103.md.
- Decision: pending lead prioritization.

### IMP-005  Semantic save comparison   (proposed by Astra, 2026-11-03)
- Problem: raw save diffs conceal lost equipment and duplicated item instances across maps.
- Idea: read-only before/after report of inventory/world/slot transfers and transaction receipts, with explicit exceptions for legitimate grants, consumption and transformations.
- Gain: detects the STORY047 jungle equipment filtering failure directly.
- Cost / risk: medium; a destroyed or transformed item is not automatically a conservation failure. Start with one known transition.
- Replies: [Astra] agree — owner endorsed this proposal in chat; preserve actual item identities.
- Decision: pending lead prioritization.

### IMP-006  Geometry inspection before route qualification   (proposed by Astra, 2026-11-03)
- Problem: duplicate owners, stacked floors and narrow portals waste earned-route runs.
- Idea: combine IMP001/003 and ENGINE-NAV-HEIGHT metadata into an inspection report for duplicate colliders, capsule clearance and candidate unreachable interactions; never auto-edit geometry.
- Gain: STORY053 door50 and STORY055 upper-room/lower-coffin confusion supply concrete witnesses.
- Cost / risk: medium; intentional stacked architecture and form changes create false positives, so warnings require review.
- Replies: [Astra] agree — owner endorsed the idea; shared inspectable mechanism records should extend the owner registry rather than introduce another registry.
- Decision: pending lead prioritization; overlaps existing ENGINE-NAV-HEIGHT and ENGINE-OWNER-REGISTRY.
