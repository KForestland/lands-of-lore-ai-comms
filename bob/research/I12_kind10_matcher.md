# I12 kind 10 matcher

No frame was opened. No Godot was run. LOLG.DAT sha256 prefix `b27a35341c6e877e`, length 1977007. File offset = VA + 0x37000. This pass re-read the compare. It did not re-read the post-match enqueue. Dword `[0x22D0C]` stays unnamed. Opcode 1 and opcode 9 were not entered.

The host's `_match_object` has no kind 10 arm. The fallthrough string is `matcher for record kind %d was not entered`. That is the line the task quotes. Grade DECODED as the host text.

## What the record is

Kind 10 is an object-event record, kind byte `0x0A`. The port's object-event framing already reads word +2 as a stream-1 group. That framing is the export, not this matcher. L16 has 12 of these records. Every one is 8 bytes. Byte +4 is 0. Byte +5 is `0x90`. Word +6 is a region index the same object already uses elsewhere. The number match is DECODED. The matcher does not load a region table by name.

| owner | raw | group | word +6 | that region |
| --- | --- | --- | --- | --- |
| prop 602 Ball O Smoke | `080a90930090d627` | 37776 | 10198 | floor 0, ceiling 1000, x 2267..2310, y 2882..2943 |
| prop 603 Ball O Smoke | `080ad4930090e427` | 37844 | 10212 | floor 0, ceiling 1000, x 1639..1701, y −12915..−12767 |
| control 71 Push/Pull | `080a2aa30090541f` | 41770 | 8020 | floor 22, the drop region in I07 |
| control 108 Push/Pull | `080abca70090b41f` | 42940 | 8116 | floor −28, the other drop region |
| control 115 Key Object | `080a7ca80090730d` | 43132 | 3443 | SW city gate, floor 100 |
| control 116 Key Object | `080a8ea80090ab0c` | 43150 | 3243 | NW city gate, floor 100 |
| control 117 Key Object | `080aa0a80090230c` | 43168 | 3107 | NE city gate, floor 100 |
| control 118 Key Object | `080ab2a800901e0b` | 43186 | 2846 | SE city gate, floor 100 |
| control 119 | `080ac4a80090dc1d` | 43204 | 7644 | the key's opcode 18 landing quad |
| control 120 | `080afaa800900c1e` | 43258 | 7692 | same |
| control 121 | `080a30a90090551c` | 43312 | 7253 | same |
| control 122 | `080a66a90090ac1d` | 43366 | 7596 | same |

Names are the I03 tables and stay LIKELY. Balls 600 and 601 do not have a kind 10 record. Their door commands are kind 6.

## The compare

Walker `0xAE608`, file `0xE5608`. File `0xE5625`, `80fa0a`, compares the record kind with `0x0A`. File `0xE562E`, `8b4c241531c0c1f9188a430489df39c8`, loads the dword at `[esp+0x15]`, shifts it arithmetic right 24, and compares that with zero-extended byte +4. The shifted byte is the low byte of the second argument. A low byte of `0x80` or above is negative after the shift, so it cannot equal the zero-extended record byte. Grade DECODED.

On equal, file `0xE5646`, `668b43066bc02c8b0d0c2d02008b6c241c01c839e8`, compares word +6 times `0x2C`, plus dword `[0x22D0C]`, with the third argument at `[esp+0x1C]`. Byte +5 is not read on this arm. Grade DECODED. The base dword stays unnamed, so word +6 cannot be turned into a pointer from this note.

On not equal, file `0xE56E7`, `807c241800`, rejects when the second argument's low byte is not 0. File `0xE56F2`, `83f807`, then requires byte +4 equal to 7. File `0xE5704`, `668b4d18668b430639c8`, compares word +6 with the word at the third argument +0x18. Grade DECODED. No L16 kind 10 record has byte +4 equal to 7, so this arm does not accept them.

The input an L16 kind 10 record can match is a second argument whose low byte is 0, and a third argument equal to `word_6 * 0x2C + dword [0x22D0C]`. Anything else in the low byte rejects. What the caller stores in those two arguments was not re-read. The enqueue after a match was not re-read.

## Still open

The name of dword `[0x22D0C]`. The caller's second and third arguments. The post-match enqueue. Byte +5 = `0x90`, unread on the equal arm.
