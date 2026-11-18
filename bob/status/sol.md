# SOL — LoL1 reverse-engineering

Completed work order: `fable_lane/LOL1_RE_ORDER_20261118.md`, owner decision 2026-11-18.
Worktree: `~/lol1_re_sol`, branch `sol/lol1-unknowns-20261118`.

- 7 EMC2 scripts — READY at `f6d1469`. Both editions pass 60/60. Follow-up `e581326` confirms the native handler for 0x7E and records native dispatch offsets.
- 8a Executable tables — READY at `df3b8e8`. Native static table offsets and item/monster script records located for both editions.
- 8c Save format — READY at `ba4932b`. Original writer and reader offsets, four floppy sidecars and eleven ScummVM saves checked. Some native field meanings remain open.
- 8b Rules — READY at `e581326`. Documented hit, armour, damage, magic, experience, monster modes, light and time. Native hit and evade differences are confirmed. Native Vortex behavior, skipped save field meanings and behaviors supported only by ScummVM are marked UNCONFIRMED.

Branch is local and ready for Fable’s review.

## Round 2

- Q17 native save fields — STARTED.
- Q18 native item and monster records — queued.
- Q7 remaining native rules — queued.
- Q8 downstream updates — queued.
- Q15 ADL and C55 — queued.
- Review defects — queued.
