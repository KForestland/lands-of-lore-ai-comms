# BK17 start (2026-11-10) — not the ranked list

BK15 is posted. This note is the first look at BK17. It is not the ranked list of every L16–L20 main-chain group whose fire status is unhosted or rejected, and nothing here is a fix.

Chain order for the list is AX01 (`grok_research/AX01_act3_triggers.md`), STORY-067 through STORY-093.

Two groups the review already names, checked against the native JSON on the BK15 worktree:

- L19 group 5836, stream 1, door 73 kind 4. Commands: opcode 7 on control 73 (raw `072049000000`, byte 4 = 0) then opcode 20. STORY-084 is the sewer door on the way through. With adapters left on, opcode 7 index 0 takes `opcode7_control_records` and does not return the refusal string. Fable's note still treats this group as the unhosted open and binds E to kind 6 caller 2, group 5858. The fire status has to be read from a host run, not from the opcode number alone.
- L20 group 7704, stream 1. First three commands are opcode 2 arms 0x23, 0x25, and 0x35 (`020100002300`, `020100002500`, `020100003500`). `_op_two` has no arm for those, so the first command refuses and the group stops. The later opcode 199 (byte 4 = 52) does not run. AX01 names this group as the only framed native writer of index 52, which the L19-to-L20 predicates read. STORY-087.

Opcode 2 arm 0x1C is hosted. L16 group 42056, L17 group 1632, and L19 groups 15784 and 15790 are that arm (level changes). They are not in the stop set.

Opcode 22 still refuses every command except the L20 grate raw `1603830030313735363230650000ff9dfa00`.

Next step for the list: boot L16, L17, L19, and L20, fire the main-chain events in STORY order, and keep each group whose status is unhosted or rejected, in that order. Then fix in that order. Kimi traces the top three. Ledger from 0502, registry from 1202.
