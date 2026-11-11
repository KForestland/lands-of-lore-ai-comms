# G3 ruins mirror walk into the Jungle

The original room does have the walk. Region 2301 stays. The arrival heading stays 0. The Journal line is recorded on first presence in region 2306, while Luther is still in the Ruins. The Jungle landing has no neighboring way back.

No longplay frame of this arrival was opened. The decision uses the native script export and the hintbook.

## What the bytes do

Cemetery control 150 is kind 6, group 19732, file 13115417, raw `0606144d0902`. That group is opcodes 197, 9, 9, 198. It is not the level change.

The level change is L10 region 42, kind 12, event 2, group 108. Group 108 is opcode 2, file 13162976, raw `020100001c69`. Byte `0x69` is level 9, selector 3. Region 42 carries a predicate (`entry_hex` `00030b0001`). That predicate was not decoded here.

L9 selector 3, in `act2_maps.json`, is x `-3032`, y `8232`, heading word 0, region 2306, floor 200, file 23383756, raw `28f428200000020903000000`. The row's own grade of the field binding is LIKELY. The port stand is `(-3032, 232, -8232)`: floor plus 32, and y negated. `dragon_level.gd` still applies that heading as `rotation.y = -TAU * heading / 65536`. Heading 0 is yaw 0. Forward in this port is `-basis.z`, which is -Z.

Region 2306, from `creature_nav/L9_DR.json`, is x `-3081..-2972`, z `-8281..-8175`, floor 200. The stand is inside that cell and no other. Region 2301 is the next cell along -Z: x `-3082..-2972`, z `-8399..-8363`, floor 200. The near edge is 131 units from the stand, with region 2307 between them. Region 2301, kind 12, event 2, has no predicate. It fires group 572. Group 572 is opcode 2, file 23384472, raw `020100001cc8`. Byte `0xC8` is level 8, selector 6. Entering the region is the trip. That script was left in place.

Opcode 2 arm `0x1C` is the host already marked PROVEN: byte 5's low five bits are the level, and the top three bits are the arrival selector, when global byte `[0x223D6]` is 0. These two groups were read from the area script export. They were not re-disassembled from LOLG.DAT.

## The book

Hintbook lines 3682–3686. The room past the bridge has three teleporting mirrors. One goes to the cemetery. One goes to the Savage Jungle. One stays in the ruins. The book says not to take them yet. It prints no region id. Grade of the printed jungle mirror: HINTBOOK. Grade of the join to region 2301: it is the only level change straight ahead of the cemetery arrival. The book does not number that region, so the name "that mirror" stays LIKELY. The level change itself is what the script does.

## The way back

L8 selector 6 is x `2063`, y `2326`, heading 29127, region 3539, floor 0, file 13550225, raw `0f081609c771d30d06000000`. The record stand `(2063, -2326)` is region 3539 and no other. That region has no events. The reported stand `(2101, -2221)` is in regions 3535 and 3537, also with no events.

The only L8 region entries that change to level 9 are:

- Region 3132, group 1670, raw `020100001c29`, level 9 selector 1, floor -500. About 1115 units from `(2101, -2221)` and 1166 from the record.
- Regions 3569, 3570, and 3573, groups 2076, 2082, and 2088, raw `020100001c49`, level 9 selector 2, floor -55. About 5240 units from either stand.

Nothing nearer than 1000 units is a level change of any destination. Prop 30 is not a region. Its kind-6 groups are 1968, 2022, 2076, and 2130. Only 2076 changes level, and that is the same far selector 2. No return portal was added.

## The note

`l9_mirror_jungle`: "One of these mirrors leads back to the jungle." It records when the body, after `native_translation`, is inside region 2306 and between y 160 and 320. Region 2301 does not record it, so the sentence is said in the room and the exit is past the room. No new piece. `arrival_pose` was not edited.

Tests: `l9_mirror_room_test`, `act2_journal_hints_test`, `act2_findable_test`, `my_journal_test`, `act1_journal_hints_test`, `act3_journal_hints_test`. The note count those tests pin is 52. The six Act 2 scripts pin 18.
