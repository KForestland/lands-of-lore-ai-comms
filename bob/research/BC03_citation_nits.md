# BC03 — AX01 citation nits

Edited in place. No game script changed for this item. Lines are newline counts in `~/AI_COMMS/reference_hintbook/hintbook.txt` (5901 LF). Form-feeds are not line breaks for these citations.

| Id | Was wrong by | Now |
|---|---|---|
| STORY-088 | Trinity line missed | HINTBOOK 5492–5506. Line 5506 is `level-five prism spell (Trinity) and away she goes.` Line 5505 is blank. |
| STORY-089 | Started on the Trinity line | HINTBOOK 5507–5512. Line 5507 is `The moving pillars are your next challenge.` Line 5512 ends `to reload.` Shifted so 5506 stays on 088. |
| STORY-074 | Freeze range short | HINTBOOK 5155–5164. The ice-seed sentence is 5163–5164. |
| STORY-069 | Disk sentences missing | Added 4842–4847 (NW box through the disk), 4896–4897 (NE box and Luther through the shimmering disk), 4921–4923 (SE parallel). 4710–4714 stays. |
| STORY-092 | Frame clock | `g_00389` at 303:40 and `g_00390` at 304:10. Formula `6580+(N-1)*30` seconds: N=389 is 18220 s = 303:40; N=390 is 18250 s = 304:10. |

The same two frame times are in `I33_act3_frames.md` row 092. AX03 does not say "at 304:10" and was left as it was.

STORY-078 in AX01 still describes the applied tree (walk sets `pad_seen`; aimed E is the host). The walk-on change is the unapplied BC01 patch, not a citation edit.

No runtime test applies. The check is the awk read of those hintbook lines.
