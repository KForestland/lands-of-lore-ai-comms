# I23 finale movies

No frame was opened. No player was run. MOVIES.MIX has no `.vqa` names, so a name was not joined to a MIX key. Opcode 21 and opcode 22 were not entered.

Hintbook line 5487 names the "Belial's birth" scene, after the curse enters the mother. Lines 5574–5576 name the last video: Luther with Dawn, then the Draracle appears and vanishes. Grade HINTBOOK. Those two scenes are the only finale movies the hintbook names. Brady printed 142 narrates the ending and does not name a file. Grade BRADY.

## Names stored on the finale levels

L19_BC, three names:

| file | name | bytes after the name |
| --- | --- | --- |
| 58149 | `e224e.vqa` | `Dawn good Luthe` |
| 179971 | `dn03.vqa` | no caption read |
| 620247 | `sm01.vqa` | no caption read |

L20_BB, thirteen names: `5970320e.vqa` (326579), `e226e.vqa` (347904), `dd01.vqa` (441841), `bb07.vqa` (461773), `bi03.vqa` (528365), `6e.vqa` (549622), `4e.vqa` (567893), `b231411e.vqa` (582256), `9306e.vqa` (667522), `f238750e.vqa` (703936), `bi01.vqa` (773955), `placenta.vqa` (5066703), `3340820e.vqa` (14796208).

`placenta.vqa` is the only name that matches the birth prop's template, `Frank's Placenta`. That is a name match, not a trigger. `e224e.vqa` is the only name with the Dawn fragment in the following bytes. That adjacency was not read as the ending reel. The other names were not ordered.

L17_HC stores `hw01.vqa`, `hw12.vqa`, and `hw14.vqa`. Those sit on the cavern archive, not on L19 or L20.

## MOVIES.MIX

Length 186871279. Twenty-nine entries. Twenty-eight begin `FORM` / `WVQA`. Entry 28, key 1846428659, is 6041 bytes and is not a FORM. Inside each VQHD, the payload u16 at +4, the u16 at +6, and the u16 at +8 are the three fields below. A VQA header uses +4 as the frame count. No player checked that.

| i | key | bytes | +4 | width | height |
| --- | --- | --- | --- | --- | --- |
| 0 | 2432533574 | 27480468 | 1125 | 640 | 400 |
| 1 | 2968225553 | 16640056 | 699 | 640 | 400 |
| 2 | 3008970044 | 82206194 | 3576 | 640 | 400 |
| 3 | 3501392159 | 27881582 | 1130 | 640 | 400 |
| 4 | 1299118734 | 978372 | 75 | 320 | 400 |
| 5 | 1299118736 | 906600 | 75 | 320 | 400 |
| 6 | 1299118738 | 922596 | 75 | 320 | 400 |
| 7 | 1299118740 | 1074220 | 75 | 320 | 400 |
| 8 | 1299118742 | 939768 | 75 | 320 | 400 |
| 9 | 1299118744 | 1061704 | 75 | 320 | 400 |
| 10 | 1299118746 | 975916 | 75 | 320 | 400 |
| 11 | 1299118748 | 790930 | 75 | 320 | 400 |
| 12 | 1299118750 | 888644 | 75 | 320 | 400 |
| 13 | 1366227596 | 842890 | 75 | 320 | 400 |
| 14 | 1366227598 | 998702 | 75 | 320 | 400 |
| 15 | 1366227600 | 1487170 | 123 | 320 | 400 |
| 16 | 1366227602 | 951222 | 75 | 320 | 400 |
| 17 | 1366227604 | 894228 | 75 | 320 | 400 |
| 18 | 1366227606 | 946092 | 75 | 320 | 400 |
| 19 | 1366227608 | 3755934 | 450 | 320 | 400 |
| 20 | 1433336466 | 7759300 | 676 | 320 | 400 |
| 21 | 1500445334 | 882694 | 75 | 320 | 400 |
| 22 | 1500445338 | 1045646 | 75 | 320 | 400 |
| 23 | 1500445340 | 901680 | 75 | 320 | 400 |
| 24 | 1500445342 | 1033182 | 75 | 320 | 400 |
| 25 | 1567554188 | 853654 | 75 | 320 | 400 |
| 26 | 1567554190 | 803968 | 75 | 320 | 400 |
| 27 | 1567554192 | 961472 | 75 | 320 | 400 |

Version u16 at payload +0 is 2 on every one of these 28.

## Still open

Which key is `placenta.vqa`. Which key is `e224e.vqa`. The order of the other thirteen names. A played frame. No longplay frame.
