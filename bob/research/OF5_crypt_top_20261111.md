# OF5. The stone chest at (1358, -1269)

Owner F10 T23-37-32. "cant open the crats to get the orb". Origin height 22.04, yaw 3.08, looking north at a closed carved chest. No behavior change. The chest has no orb, and a globe that does sit under a different crypt top is taken from beside it.

## Grades

| Claim | Grade |
| --- | --- |
| The chest on that look is movable 83, template 8, name "crypt top 4", source (1374, 1196), height 35, heading 2912. Map point (1374, 35, -1196). The slab is 60 by 40 by 8. The four chests within 400 are movables 83, 84, 85 and 86, all the same template | PROVEN. Placement record and the template name table in L10_DC.MIX. No other movable is within 400 |
| Movable 83 has an empty event list. No command in L10_DC.json targets class 0x20 index 83, 84, 85, 86, 51 or 67 | PROVEN |
| Motion bytes of 83 are `01 04 02 1f 14 00 00 00`. Byte 34 is mode 4. Modes 0 and 1 are the vertical arms. Modes 2 through 5 are the slide family. Mode 6 is the rotary store | PROVEN for the bytes and for which arms exist. Which of the four slide stubs mode 4 uses is UNKNOWN. The jump at 0x63C59 reads a relocated table at immediate 0xA22C, and that fixup did not match |
| No placed world item is under lid 83. The nearest empty globe to the reported stand is about 590 away | PROVEN. The earned test looks at (1374, 35, -1196) and `target()` is empty. The nearest definition-98 aim is more than 400 away |
| Standing there stays on the floor. Origin stays near 22, resets 0 | PROVEN (same test) |
| Item 55, `96-E Globe` at (1272, 15, -1853), is under movable 51, another crypt top 4. From a stand beside it, origin settles at 42 (feet on y 10), and `take` collects it. The lid is not moved | PROVEN (`tests/l10_crypt_top_globe_test.gd`) |
| The same side take works for the other placed empty globes 8 and 43 through 58, except item 9, which was only tried from origin 32 | PROVEN for that teleport-and-aim sweep. It is not the earned test. Item 9 at height 50 was blocked by a floor from origin 32. Whether a higher stand takes it was not tried. Not this report |
| E opens these lids | Not found. Nothing in the script file addresses them. The contact path copies a slide dword between two bodies and is not an E handler |
| The original slides a mode-4 lid when the player pushes it | LIKELY for the mode family, UNKNOWN for the axis and for the trigger that starts a lid with distance byte 0. Not hosted. Sliding lid 83 would still show no orb |

## What the contact path actually is

Movable vtable immediate 0x55B4, object-5 file 0x1C65D8. Slot 0 is 0x631A8 and returns class 0x20. Slot +0x38 is 0x63260. At 0x632AA it stores dword object+0x48 into the absolute address `[0x2B4FC]`. Slot +0x40 is 0x63C78. At 0x63C94, when its second argument is not zero, it copies that global back into object+0x48. The pair scan at 0x5BA5D calls slot +0x40 with argument 1 on the first body. That is a push handoff between two colliding bodies. It is not a use opcode. Opcode 1 for a non-rotary movable stays unhosted (`opcode1_other_modes` off), and no command sends opcode 1 to these lids.

## What was not this chest

OF4 is item 47, already posted. OF6 is item 46 at (-537, 0, -4079). The report shows that take already succeeded after a clip. The entrance is the next note.

## Test

`/tmp/godot_dummy.sh --headless --path ~/opus_work/lol2_grok_of9 --script res://tests/l10_crypt_top_globe_test.gd`

Printed `PASS L10 crypt top: the reported chest has no globe, and item 55 is taken from beside its lid, resets 0`. Exit 0.

No new deviation piece. No lid motion was added.
