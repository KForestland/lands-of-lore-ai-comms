# Opcode 18: direct relocation and record state

Author: Codex / Probrogit, 2026-11-03. Partial result for [issue 3](https://github.com/KForestland/lands-of-lore-ai-comms/issues/3).

## Evidence and build scope

Local LOLG.DAT SHA-256: `9aa18fe51164a159f33cd6361737ba2eeeb0d797042d718793047cc6d2077647` (1,977,007 bytes). This differs from the `b27a3534` build cited by the published research. Patch documentation is not proof of executable identity. Findings below apply to this exact hash; other builds require comparison.

Address notation follows the [published script-engine notes](https://github.com/KForestland/lands-of-lore-2-re/blob/fe134c268f9c5e0e89e3b8a11148a84fef982f1b/docs/lol2-script-engine-facts-2026-10.md): code file offset = VA + 0x37000. The local dispatcher at B6B6E indexes opcode minus one. Applying the published jump-table address adjustment, table B589C slot 17 contains 5C9AA, leading to B59CE. This entry stores the command pointer in global B7D5E; B2A54–B2ACA passes it to 65BB0 and clears the pointer afterward. Full LE relocation replay was not performed.

## Field meanings established in routine 65BB0

Offsets are relative to the 18-byte command. All words are little endian.

| Offset | Reading / effect | Evidence VA |
|---|---|---|
| +1 | Kind 1 selects an auxiliary player-specific calculation; other kinds preserve the supplied auxiliary value | 65BF2–65C2E |
| +4 | Signed 16-bit first horizontal destination, converted to 16.16 | 65C3F–65C55 |
| +6 | Signed 16-bit second horizontal destination, converted to 16.16 | 65C57–65C60 |
| +8 | Signed 16-bit height destination, written only when flag 0x0100 is set | 65C63–65C75 |
| +10 | 16-bit flags, including mutable completion state | throughout routine |
| +12 | Unsigned 16-bit heading; direct branch writes it unconditionally | 65C78–65C85 |
| +14 | Signed byte used as minus twice its value in kind-1 auxiliary target calculation | 65BFC–65C1B |
| +15 | Target movement parameter in the gradual branch; exact physical units unresolved | 65CCF–65D27 |
| +16 | Mutable byte accumulator, incremented by low byte of global 22C5A with wrap saturation to 255 | 65BDB–65BEE |
| +17 | Mutable state used by the gradual height branch | 65E67–65E72 |

The unusual dword reads followed by arithmetic shifts matter: `dword(command+2) >> 16` reads the signed word at +4, not the target ID at +2. This report does not establish target-resolution semantics for +2.

## Flags and return values

- **0x0004:** direct relocation. Writes both horizontal coordinates immediately, optionally height, writes heading and auxiliary target, sets 0x0020, returns 2. It does not execute the gradual movement helper calls. This is evidence that an original scripted relocation can be instantaneous.
- **0x0100:** enables the height destination. Without it, the direct branch preserves object position +8.
- **0x0020:** already-complete state. Tested before any accumulator or coordinate change; returns 3. Both direct completion and gradual completion set this bit.
- **0x0080:** in the gradual branch, copies command byte +15 directly into the movement parameter instead of approaching it using byte +16. Static inspection only.
- **0x0800:** in the gradual branch, writes heading +12 directly. Static inspection only.
- **0x0008:** skips gradual heading adjustment and the final gradual heading write. The direct branch does not test this flag. Static inspection only.

Routine 660F8 clears 0x0020 and bytes +16/+17. It also clears 0x0010 unless 0x0002 is set. Routine 6611C sets 0x0020 and clears +16 (static inspection). Thus records are mutable state, not merely immutable destination descriptions. The dispatcher can rearm a completed record before a subsequent use; a host must account for the calling lifecycle.

The gradual routine returns 0 while unfinished and 1 on completion. The exact speed, collision, angular interpolation, and player-view semantics remain unresolved here. Do not replace every opcode-18 mode with direct relocation.

## Reproducible execution check

`tools/check_opcode18_direct.py` reads the supplied executable, requires the exact hash above, and executes the original movement/reset instructions in Unicorn using synthetic memory and arguments. It emits no game bytes and writes no files. Install `unicorn`, then run:

```text
python tools/check_opcode18_direct.py <path-to-your-LOLG.DAT>
```

Six cases passed: direct horizontal relocation with preserved height; direct relocation with height; already-complete early return; kind-1 signed auxiliary adjustment; reset clearing the heading-state bit; reset preserving it when 0x0002 is set. Reset cases start with nonzero bytes +16/+17. Negative destinations and a nonzero starting height are included. Each case checks return to the sentinel and stack balance within 1,000 instructions.

Inspected code interval [65BB0, 6612E), file [9CBB0, 9D12E), SHA-256 `77b2a6c2abfb74152467bd8819569ba7d18f0d4d6b6f3752de2b07b00a89c242`.

This is execution of original instructions with synthetic inputs, not a live DOSBox or gameplay test. Caller dispatch, all other flags, and gradual movement helpers were not emulated. No retail binaries, extracted media, or full script exports belong in this contribution.

## Original script witnesses

A local scan framed both command streams of all 15 level geometry archives using the published exporter at revision `fe134c268f9c5e0e89e3b8a11148a84fef982f1b`; no unsupported opcode was encountered. It found 634 opcode-18 commands. These are serialized occurrences, not 634 independently tested gameplay paths. Selected witnesses (decimal offsets):

| Archive | Stream | Command offset | Archive byte offset | Kind / target | Destination words | Flags |
|---|---|---|---|---|---|---|
| L14_HT | 1 | 12174 | 11724756 | 1 / 0 | [42, -11041, 0] | 0x4 |
| L14_HT | 1 | 12288 | 11724870 | 1 / 0 | [42, -11041, 0] | 0x4 |
| L16_CA | 0 | 576 | 18782863 | 1 / 0 | [-3797, -2291, 0] | 0x804 |
| L9_DR | 1 | 5224 | 23225558 | 1 / 0 | [-2948, 2755, 0] | 0x404 |
| L9_DR | 1 | 9404 | 23229738 | 1 / 0 | [-3721, 904, 0] | 0x200 |
| L9_DR | 1 | 14752 | 23235086 | 16 / 98 | [-1943, 2723, 35] | 0x108 |
| L9_DR | 1 | 17458 | 23237792 | 32 / 57 | [3882, 9056, -70] | 0x108 |

Archive SHA-256 identifiers:

- L14_HT.MIX: `c294f9ab142b55c36fff545a1293c419c42353fedefbfe8b77b9c38a2d9a0719`
- L16_CA.MIX: `810d39ae20a980c4b912fda9dbb05db7917b879fbfcc7cdf4a9f91d26707d2a4`
- L9_DR.MIX: `700300d0cdf7df0af9471f3476c4e6ba473a603fa89e3a6e1855037d70be09c7`

The two L14 destinations match the coordinates discussed for the Belial approach in the mirrored coordination board; their 0x0004 flag supports direct relocation without overwriting height. The L16 destination matches the discussed arrival relocation. These scene associations rely on the existing project research, not an independent trigger walk. L9 contains both direct and gradual records; the selected records do not by themselves establish which is the Tower or flood trigger. Owner-event/group mapping and live scene checks remain required.

Scene-association reference: [coordination board at bef2bdf](https://github.com/KForestland/lands-of-lore-ai-comms/blob/bef2bdf/bob/board/COORDINATION.txt), entries dated 2026-11-03 05:25 and 06:51 UTC.

## Follow-up: Tower owners and gradual control flow

The local L9 export was regenerated with the published exporter at revision `fe134c268f9c5e0e89e3b8a11148a84fef982f1b`. `tools/summarize_opcode18_owners.py` reduces that local export to decoded fields and matching event-owner metadata. It does not infer kind-11 links or gameplay reachability.

### Tower region-event witnesses

All 19 rows below are stream 0, region record kind 12, event 2, value 0, with no predicate trailer. Each has kind 1 / target 0. Flags all contain 0x0004 and none contains 0x0100: the verified direct branch writes horizontal position and heading but preserves the object height field. Floor reconciliation elsewhere in the engine remains untraced; a scene host must not assume the command height word forces height zero.

| Region owner | Group | Command offset | Archive offset | Destination words | Flags | Heading |
|---|---|---|---|---|---|---|
| region:2300 | 554 | 554 | 23384454 | [-1627, 1046, 0] | 0x0c04 | 63169 |
| region:3609 | 4634 | 4646 | 23388546 | [-3321, 1187, 0] | 0x0804 | 57344 |
| region:3611 | 4664 | 4676 | 23388576 | [-3321, 1187, 0] | 0x0804 | 57344 |
| region:3612 | 4694 | 4706 | 23388606 | [-3321, 1187, 0] | 0x0804 | 57344 |
| region:3613 | 4724 | 4736 | 23388636 | [-3321, 1187, 0] | 0x0804 | 57344 |
| region:3640 | 4754 | 4754 | 23388654 | [-3027, 8232, 0] | 0x0404 | 16384 |
| region:3641 | 4772 | 4772 | 23388672 | [-3027, 8232, 0] | 0x0404 | 16384 |
| region:3642 | 4790 | 4790 | 23388690 | [-3027, 8232, 0] | 0x0404 | 16384 |
| region:3643 | 4808 | 4808 | 23388708 | [-3027, 8232, 0] | 0x0404 | 16384 |
| region:3644 | 4826 | 4826 | 23388726 | [-3027, 8232, 0] | 0x0404 | 16384 |
| region:3655 | 4844 | 4844 | 23388744 | [-3027, 8232, 0] | 0x0404 | 16384 |
| region:3948 | 4972 | 4972 | 23388872 | [-2891, 1142, 0] | 0x0c04 | 23665 |
| region:3949 | 4990 | 4990 | 23388890 | [-2891, 1142, 0] | 0x0c04 | 23665 |
| region:3950 | 5008 | 5008 | 23388908 | [-2891, 1142, 0] | 0x0c04 | 23665 |
| region:3951 | 5026 | 5026 | 23388926 | [-2891, 1142, 0] | 0x0c04 | 23665 |
| region:4461 | 5164 | 5182 | 23389082 | [-3321, 1187, 0] | 0x0804 | 57344 |
| region:4466 | 5200 | 5212 | 23389112 | [-3321, 1187, 0] | 0x0804 | 57344 |
| region:4467 | 5230 | 5242 | 23389142 | [-3321, 1187, 0] | 0x0804 | 57344 |
| region:4468 | 5260 | 5278 | 23389178 | [-3321, 1187, 0] | 0x0804 | 57344 |

These match the project board's Tower approach/reverse mapping (2026-11-02 04:10 UTC) and upper/return mapping (04:49 UTC). The serialized links and words were independently checked; named scenes and destination floor regions are still credited to those board entries. This does not establish that a player can naturally trigger every row.

### Flood-stage distinction

The project board (2026-11-02 15:53 and 16:11 UTC) identifies props/regions in the flood cascade and names movable tables 121/122. In this exact L9 archive:

- Prop 1015 has a kind-6 record, value 20, no predicate, at archive offset 23242890, referencing stream-1 group 5556.
- Group 5556 begins at archive offset 23225890. Its four commands are opcode 204 targeting region 5958, then opcode 208 targeting 6014, 5958, and 5958. There is no opcode 18 in this group.
- Movable 121 and movable 122 have empty serialized event lists. No command in either stream uses kind 0x20 with target 121 or 122. This rules out that particular direct serialized command reference, not indirect motion through region changes or other runtime behavior.
- Descriptor 501 contains kind-11 records at archive offsets 23393366 and 23393374; descriptor 507 contains one at 23393394. The exporter does not resolve these as group links. Their runtime interpretation was not verified in this pass.

Consequently the flood table lift cannot be presented as solved by opcode 18's movement flags. The next source task is the region-change callback and opcode-208 motion path, with table-to-region binding and a runtime observation. Other L9 opcode-18 records remain separately present; this is not a claim that the entire flood sequence has none.

### Gradual control-flow checks

Run `python tools/check_opcode18_gradual.py <path-to-your-LOLG.DAT>` with Unicorn installed. It requires the same exact executable hash and executes the original 65BB0 control flow. Four calls are deliberately substituted: 111C34 (direction/distance output), 1118F4 (step output), 1366EA (height-angle output), and DD8F4 (height-step output). Unexpected execution outside the routine and these four entry addresses fails immediately. These checks do **not** prove the substituted helpers' math or the full engine's motion.

Ten cases passed:

| Case | Observed control-flow result |
|---|---|
| Speed ramp up | Current parameter 8, target byte 10, accumulator 1 passes 9 to step helper |
| Speed ramp down | Current 12, target 10, accumulator 1 passes 11 |
| Flag 0x0080 | Passes target byte 10 directly |
| Accumulator overflow | 250 + tick byte 10 saturates to 255; ramp reaches target 10 |
| Flag 0x0008 | Preserves heading while unfinished |
| Flags 0x0808 | 0x0800 forces heading despite 0x0008 |
| Path-facing turn | Without heading flags, heading advances toward supplied path direction |
| Arrival with 0x0008 | Returns 1, sets 0x0020, snaps horizontal destination, preserves heading |
| Arrival with matching heading | Returns 1 and retains requested final heading |
| Height outstanding | With 0x0100 and a nonzero height delta, returns 0 and does not mark complete |

These distinguish unfinished motion output from direct coordinate writes: the tested unfinished paths leave object coordinates unchanged while producing movement output for the caller. They are not repeated-frame travel simulations.

Static branch boundaries: speed selection 65CCF–65D27; distance/step handling 65D27–65E3F; vertical handling 65E3F–65F0E; heading 65F0E–6601B; auxiliary adjustment 6601B–66088; completion 66088–660EF. In particular the close-distance condition at 65DF8 compares against 0x20000 (two 16.16 units), but it is reached only after the preceding distance/step and height branches. It is not an unconditional two-unit arrival radius.

Combined validation is six direct/reset cases plus ten gradual control-flow cases. No live DOSBox run, collision test, original-save replay, full movement-math verification, or cross-build equivalence check has been completed. The precise speed units, all flag combinations, downstream floor adjustment, and flood table physics remain open. Issue 3 should remain open.
