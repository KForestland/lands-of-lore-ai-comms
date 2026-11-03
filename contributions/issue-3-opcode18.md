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
