# P06 LoL1 chunk 7: the lake through the burned nests

No Godot was run. The tree is `~/lol1_godot` at `9987d7e`, clean. L06 chunk 7 plays cards LOL1-07 through LOL1-11 as far as the walkthrough is written: the lake, Opinwood, the swamp, Dawn's wagon, and Urbish through the burned nests. The missing-call rule is the same as chunk 5. The White Tower stair redirect is in this chunk. Floppy-only Dawn's Key is outside this plan.

## Data

L03 is the step source for these five cards. Blocks, item types, and give calls were not read. A syscall is ported when `missing` on these levels names it.

- LOL1-07. The party crosses Lake Dread. Victor says Dawn already took the boat. Acceptance is the party on the far side. The fallen keep is a second return. It is a different scene from the poisoning.
- LOL1-08. The green skull is carried. The beggar is paid. Dawn's wagon refuses the party. The lightning scroll and the long sword are picked up in the same chapter and are not required.
- LOL1-09. The witch doctor translates the riddle. The brass helmet from the stickmen is given to the chieftain. The Ruby of Truth is carried. Freeze is the crossing the walkthrough writes. Whether another crossing exists was not read.
- LOL1-10. Dawn is shown the ruby and the riddle. She gives empty flasks and the pyramid key. Acceptance is the pyramid key carried.
- LOL1-11. The green skull is used on the giant slug. The silver key is on mine level 3. Fireballs burn the nests. Acceptance is the nests burned. The text stops. The rest of the mine, the mask temple, and whether Paulson joins stay unknown. The party list says he joins. The steps never say he joins.

`olol_moveBlockObjects` in `script_lol.cpp`: when `_currentLevel` is 21, the destination level is 21, and `destBlock` is 0x3E0, the move is rewritten to level 20, block 0x0247. The comment says items thrown toward the White Tower level 3 stairs would vanish. The port has no `moveBlockObjects` syscall. `items.gd` can `place_move` an item. There is no combat throw yet, so the path is reachable once chunk 3 exists. The redirect still belongs here.

Dawn's Key is the floppy v1.05 softlock. The CD data this port imports does not include it. M04 index 198 is named Dawn's Key. That row stays unmerged from the floppy bug. The ScummVM note about item 264, Vaelan's cube equippable as a weapon on an unpatched floppy, is a different sentence and is not changed here.

## Behaviour

Play the five cards through the burned nests and stop where the walkthrough stops. Do not add Paulson because the party list names him. If a later read of the mine script shows `addCharacter(6)`, that call is this chunk's meeting and it uses the chunk 6 guard.

When `moveBlockObjects` is ported, the 0x3E0 rewrite is inside it. Any other destination on level 21 stays on level 21. An item that takes the rewritten path remains in the 400-slot table.

## Tests

1. The lake crossing ends on the far side. A reload stays there. The poisoning TIM does not replay.
2. The green skull is carried and the wagon has refused. The lightning scroll and the long sword are absent unless a missing call created them.
3. The Ruby of Truth is carried. The pit crossing that is implemented is Freeze. A second crossing is absent.
4. After Dawn is shown the ruby and the riddle, the pyramid key is carried. The flasks are the ones that call creates. No flask type is written here.
5. The nests are burned. The save stops in the mine. No mask-temple flag is set. Paulson is absent unless the mine script's own call added him through the chunk 6 guard.
6. `moveBlockObjects` from level 21 to level 21 block 0x3E0 lands on level 20 block 0x0247, and the item id is still in the table. The same call to block 0x3E1 stays on level 21 block 0x3E1.
