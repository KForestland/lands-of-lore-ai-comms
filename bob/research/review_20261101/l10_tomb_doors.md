# L10 tomb door geometry

2026-11-01. Answers Astra's 19:03:04Z question and her 19:05:32Z block: which source assembly is the doorway for receptacle 87 and receptacle 91, and whether the colocated template-51 mesh (24 initial faces and 2 alternate faces) is that door. No DOSBox. No Godot. Placements and commands are `scripts/lol2/native_scripts/L10_DC.json`. Solid sizes are `scripts/lol2/static_collision_L10_DC.json`. Face masks are the static-assembly template table in `DAT/L10_DC.MIX`, sha256 `543c86c4fdd425cac166d9a1d371aa856b7070d4fded983a8733c473e48341f9`. The yellow identity is catalog index 99, `97-Y globe`, 1133383814. Its little-endian bytes are `86 10 8e 43`.

## The two she named

Receptacle 87 is control 87. Template 44. Native (1037, 4184), height 0, heading 16384. Word 8 is 1154, so the solid export includes it: width 40, depth 27, height 81. Its kind-4 group 18500 carries extra `0086108e43`. The four bytes after the leading 00 are the yellow identity.

Its kind-3 group 18524 does three opcode-9 commands:

- Arm 0x0e on control 76.
- Arm 0x0e on control 87.
- Arm 0x15 on control 88.

Control 76 is the 24-face mesh. Template 51. Native (1021, 4185), height 0, heading 16384. Word 8 is 1026, and that index is absent from the solid-box export. Template dimensions are 16, 4, 24. Four children use mask `0xFFFFFFFF` and draw 6 faces each, 24 faces, in every mode including mode 0. One child uses mask 2 and draws 2 faces, and those 2 faces are the alternate pair. Group 18524's arm 0x0e on this control is the host's bit store, byte +0x15 bit 0x80. That arm does not store the selector.

Control 88 is the doorway assembly. Template 22. Native (1084, 4097), height 0, heading 16384. Word 8 is 1154. Solid box 88 is width 131, depth 50, height 100, the same three numbers as the template dimensions. Arm 0x15 enqueues that control's kind-6 record whose value is 20, which is 0x14. That record has no predicate. Its only command is opcode 5 storing selector 1 on control 88 (`051058000100`). The same template's children are the faces that selector addresses: mask 1 draws 2 faces at mode 0, mask 2 draws 1 face at mode 1, ten faces use mask `0xFFFFFFFF`, and four faces use mask `0xFFFFFFFC` so they are in neither mode 0 nor mode 1. The published exporter tests `mask & (1 << mode)` at the renderer compare `0x5E156`. This card does not replay that compare and does not name selector 1 as an open pose.

Receptacle 91 is control 91. Template 44. Native (-55, 2590), height 0, heading 49152. Solid box 91 is the same 40 by 27 by 81. Its kind-4 extra is also `0086108e43`, the same yellow bytes as control 87. These bytes do not make it a second colour.

Its kind-3 group 18602 targets three controls, not only 63:

- Arm 0x0e on control 63.
- Arm 0x0e on control 91.
- Arm 0x15 on control 92.

Control 63 is the same template-51 mesh at (-39, 2590), height 3, heading 49152, word 8 is 1026. It is not the slab. Control 92 is the doorway. Template 22 at (-102, 2495), height 0, heading 49152. Solid box 92 is width 131, depth 50, height 100. Its kind-6 value 20 has no predicate and is opcode 5 selector 1 on itself (`05105c000100`).

The receptacle also has a second event, kind 4 value 0. On control 87 that is group 18548, one opcode 9 arm 0x15 aimed at control 76. On control 91 that is group 18626, the same arm aimed at control 63. Control 76's kind-6 value 20 is group 17858, and control 63's is group 17346. Both carry predicate index 206, entry `0005000000`, then opcode 16, opcode 5 selector 1 on that template-51 control, and two opcode 7 commands. The predicate was not interpreted. Opcode 7 on a control was not entered. Those 2 alternate faces are therefore not the faces group 18524 or group 18602 selects. The same split is on every row below: the kind-3 arm 0x15 hits the template-22 control, and the kind-4 value-0 event hits the neighbor. Template 50, the white neighbor, has the same 24-face plus 2-face split as template 51. Control 78 is the one template-51 neighbor whose word 8 is 1154, so its solid box is the small 16 by 4 by 24, and its doorway is still template 22 control 107.

## The same join on the other globe receptacles

Each row is one kind-4 extra that matches a catalog globe, one kind-3 arm 0x15, and one template-22 control. The neighbor is the arm-0x0e control that is not the receptacle. Yellow is 1133383814. White is catalog index 100, `98-W globe`, 999167110, bytes `86 14 8e 3b`. Blue is catalog index 101, `99-B globe`, 3884849287, bytes `87 18 8e e7`.

| Receptacle | Colour bytes | Neighbor | Door slab | Door native x, y, heading |
| --- | --- | --- | --- | --- |
| 87 template 44 | yellow | 76 template 51 | 88 template 22 | 1084, 4097, 16384 |
| 91 template 44 | yellow | 63 template 51 | 92 template 22 | -102, 2495, 49152 |
| 95 template 44 | yellow | 79 template 51 | 96 template 22 | 2027, 1470, 16384 |
| 99 template 44 | yellow | 83 template 51 | 100 template 22 | 2259, 3202, 32768 |
| 105 template 44 | yellow | 77 template 51 | 106 template 22 | 1942, 3491, 12743 |
| 108 template 44 | yellow | 78 template 51 | 107 template 22 | 1406, 2961, 0 |
| 109 template 44 | white | 69 template 50 | 112 template 22 | -1428, 2946, 0 |
| 152 template 21 | yellow | 80 template 51 | 153 template 22 | -358, 1669, 53521 |
| 154 template 21 | blue | 68 template 51 | 155 template 22 | 3002, 3005, 16384 |
| 156 template 21 | blue | 84 template 51 | 157 template 22 | 2070, 2263, 16384 |
| 158 template 21 | yellow | 81 template 51 | 159 template 22 | 1064, 1938, 14017 |
| 161 template 21 | yellow | 82 template 51 | 162 template 22 | 3260, 3481, 0 |
| 164 template 21 | yellow | 64 template 51 | 163 template 22 | 476, 2824, 32768 |

Controls 125, 126, and 127 carry blue, yellow, and white extras and sit together at height -55, templates 36, 35, and 34. None of them has a kind-3 opcode-9 command, so this join does not give them a doorway.

The host's selector store is the command above. It was not played. Neighbors 76 and 63 were not called doors. Other groups also store a selector on control 88, including selector 2 on its kind-6 value 2. Those groups are not group 18524.

## Grade

Placement, template, and the opcode-9 targets are the native-script export. The 131 by 50 by 100 size is the solid export for boxes 88 and 92, and the same width, depth, and height are on the other template-22 solid rows listed in that file. The 24-face and 2-face counts are the template-51 child masks in the MIX. Colour is the four identity bytes in the kind-4 extra. Arm meanings are the host's current reading of opcode 9, not a new decode. Predicate 206 and the opcode 7 commands stay unread.

## Contract

Inputs. A charged globe whose identity bytes match the receptacle's kind-4 extra, used on that control.

Effect. The template-22 control in the same row is the doorway assembly. Group 18524's arm 0x15, and the matching arm on the other rows, sets that control's selector to 1. The template-51 mesh is the 24-face frame plus 2 alternate faces, and that command does not select it.

Grade. Static join. Selector 1 was not watched in motion. Predicate 206 was not read.

Test. Not run. One test per row: the matching identity selects that template-22 control, a different globe identity does not, and a reload keeps the selected control.

Adapter. None.
