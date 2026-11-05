# I09 dragon room

Place L16_CA. No frame was opened. No Godot was run. Names are the I03 tables. Name-at-index stays LIKELY. Opcode 2 byte 5, opcode 3's grant, opcode 5, opcode 7, opcode 9, opcode 16, and opcode 198 were not entered. A level-change shape is `020100001c`, and byte 5 stays unread.

Hintbook lines 5269–5288: this is the dragon room, not the dragon special scene. Chop the dragon. The blood opens the door behind it. The teleporter beyond is one-way to the Subterranean Caverns. The longer note says spark the side globes, click the curtain, and attack from the fountain edge. Grade HINTBOOK. Brady printed 234 says cut the throat and take the secret door into the caverns. Grade BRADY. The chop and the exit are REQUIRED. The mantle is the book's prerequisite. The telepad command does not store that test.

## The dragon

Prop 241, LIKELY Dragon, is (1625, −4417), height 52, region 9476, flags 0x4482. Godot (1625, 4417). Group 6384 is opcode 9 on itself byte 4 = 18, opcode 9 on u16 73 byte 4 = 3 and byte 4 = 21, opcode 16, opcode 5, and three opcode 7. Group 6438 is opcode 9 on itself byte 4 = 17, opcode 5, and two opcode 7. Index 73 fits a prop, a control, and a movable. Control 73, LIKELY Blood plate, is (1626, −4398), height 51, the same region, 12 events. The command does not pick the table.

Prop 144, LIKELY Dead dragon, is (1623, −4946), height 35, region 9965, event 0. Props 237–240 are Sm Dragon and props 141–143 are Sm dead drag, all event 0, in the same neighborhood. Controls 56–61, LIKELY Blood, cluster at y −4889 to −5121. No Fountain template is in this room. The fountain edge stays UNKNOWN as a mesh.

Prop 92, LIKELY Dracoid, is (1836, −3997), region 9639, a different row from the Dragon. Control 52, LIKELY Blood, shares that region and has no events.

## Curtain and telepad

Control 92, LIKELY Tapestry, is (1620, −5181), height 30, region 8457, south of the dead dragon. Its groups are opcode 20, opcode 16, and opcode 5 on itself, then opcode 9 byte 4 = 8 on itself. They do not name a door. The curtain click stays those bytes.

Control 74, LIKELY Telepad, is (2100, −4296), height 15, region 9615. Godot (2100, 4296). Its only command is `020100001c31`. That is the level-change shape. Byte 5 is 0x31 and stays unread, so the destination level is not named by this pass. The group has no second level-change. One-way is the book's word. Prop 242, a Light Source, and five Lightning props share that telepad's neighborhood. Their bodies were not copied.

Prop 377, LIKELY Light Source, is (1629, −4225), just north of the dragon. It owns the three groups whose opcode 198 byte is 13. Local slot 13 is `Belials_access`. The opcode was not entered. The telepad group does not name that byte.

## Still open

Byte 5 of the level change. Whether u16 73 is the blood plate. The fountain mesh. Opcode 9 as the chop. The mantle test. No frame.
