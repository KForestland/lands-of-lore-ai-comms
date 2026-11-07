# BG11 — Museum plank into the slot

Base `c9295da`, after BF01–BF07 and BG00a through BG10. Patch `patches/ACT3P2/BG11_museum_plank_hole.patch`. Not applied to the live tree.

Owner r17 16-37-36 at Museum Godot (3001, -813): "the plack should go in the hole." The same beam is in 2026-10-29 19-58-29, 2026-10-30 09-28-01, and 2026-10-23 20-18-28. It is static assembly / control 92, template 32, placement (3049, 826) height 35. The beam spans x 3008..3090, y 35..43, z -828..-823. The hole is region 1011, floor 31, ceiling 47, x 3119..3225, z -830..-815. The dragon-door frame (movable 82) is a different opening.

Group 7596 opcode 18 names control 92 at (3114, 824), height word 0, flags 0x0092, byte 15 0x28. Bit 0x0004 is clear, so the words are a slide (the pending reader is unentered). Bit 0x0100 is clear, so the height word stays unread and the beam keeps height 35. Godot delta is (65, 0, 2). The far end then sits past x 3119. The 1.5 s time is the cave-shrine slide adapter. Byte 15 stays unread. Kind 6 value 6, group 7678, sets movable 82 to state 1, which opens the hosted dragon door. Actor 20 still wakes through the existing control-92 use. Opcode 9, opcode 13, and the opcode 20 sound on group 7596 stay unhosted.

A Human walked to (3001, -813) with a fine longsword in hand, looked level at the beam, and pressed E.

Printed rendered, display :2, 7.11s:

`PASS plank: walked to (3001,-813), a level look with a held sword slid the beam into the slot, and the door opened`

`museum_control_live_test` PASS 4.25s. `museum_dragon_door_test` PASS 4.16s. Ledger `--check` is 406 pieces.

Grade: Adapter (owner rule 2026-10-30).
