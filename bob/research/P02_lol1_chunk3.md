# P02 LoL1 chunk 3: combat on the walking grid

No Godot was run. The tree is `~/lol1_godot` at `9987d7e`, clean. L06 chunk 3 is monster attack modes, a party attack, damage, and death, on the grid that already walks. LoL2 combat is not a source. L04 keeps inventory, party, and scripts in this tree.

## Data

`monsters.gd` holds 30 slots. `difficulty` is 0, 1, or 2. `set_mode` returns when the slot is in mode 13 and the new mode is not 14. Mode 7 writes `party_pos()` into `destX` and `destY`. `party_pos()` is the centre of the party's block, `Items.coords(block, 0x80, 0x80)`. Mode 14 sets `hitPoints` to 0. The function comment says death handling and the party-wide alert are not in this function. The 30-count alert loop is absent from it.

`update` handles modes 1, 2, 4, and 14. Its comment says modes 3 and 5 through 13 are not ported. Property flag 0x40 adds a roll of 1 through 8 hit points, capped at the property total. Mode 14 clears `damageReceived`. `timer` walks even slots, then odd slots, step 2, stop at 30, every 6 ticks. `walk` returns at once when property flags include 0x400. `init_monster` sets hit points to property hit points times `monsterModifiers1[difficulty]`, shifted down 8, then times a roll of 1 through 128 plus 192, shifted down 8. Level 12 type 2 skips that second roll.

M05 is the mode table to match. Modes 0 and 1 are friendly, and mode 1 also moves. Flag 0x10 on mode 0 or 1 sets other mode-1 monsters to mode 7. That is the party-wide alert. A change from mode 1 to mode 7 also enters a 30-count loop that tests the same monster pointer. That loop is not the alert. Mode 2 moves. Mode 3 sets mode 7 when the party is adjacent or the block test says so. Mode 4 strays. Modes 5 and 6 are recovery. Mode 5 rearranges and sets `partyAwake`. Mode 7 chases the party and tries distance attacks before close attacks. Mode 8 goes to mode 5 after more than 2 ticks. Mode 9 close-attacks until its tick counter hits 0, then goes to mode 7. Modes 10 and 11 have no case. Mode 12 runs level script 0x404 after more than 13 ticks. Mode 13, after more than 2 ticks, calls `killMonster`. The body of `killMonster` was not read. Mode 14 zeros hit points and clears damage received.

`items.gd` stores `flying` and can `place_move` an item. It has no width 63. ScummVM `updateFlyingObject` calls `checkBlockBeforeObjectPlacement` with width 63. The 256 alternative is commented out. The comment names large fireballs from the white-tower birds and the Cimmeria wraith knights, which read the wrong item-flag field and usually get width 63. Both editions keep 63. Those monsters were not given item ids here.

`placeMonster` returns before the environmental sound when `sounds[0]` is 0 or 255. The comment says the last valid track is 249 and that 255 happens to read silence. Chunk 9 does not invent a file for 255.

`inflictDamage` in `lol.cpp` is the damage write that was read. A monster target (bit 0x8000) returns 0 when its mode is 13 or higher. A positive damage subtracts from hit points, stores `damageReceived` as `0x8000 | damage`, sets flag bit 0x10, and sets both hit offsets to a roll of 1 through 24 minus 12. Hit points clip to 0 through the property total. At 0 the mode becomes 13. `calcInflictableDamagePerItem` produces the number and its body was not read. No damage number is added from a guess.

On a character target, a value above 3 is matched to a character `id`. No match returns 0. The scene is not named. An inactive character, or one with flag bit 8, returns 0. Flag bit 0x1000 skips `screamSfx`. The face frame becomes 6 for 4 ticks. When `flags` is 4 and item type 229 is equipped, the comment calls that item the cloud ring and the damage is shifted down 2. The hit-point write is `setCharacterMagicOrHitPoints(target, 0, -damage, 1)`. Its body was not read. If current hit points then are 0 or below, `characterHitpointsZero` stores 0 and sets flag bit 8. Otherwise `damageSuffered` becomes the damage.

## Behaviour

Modes 3 and 5 through 13 follow the M05 cases, including the empty cases 10 and 11. Mode 7 still aims at `party_pos()`. Mode 13 still refuses every later mode except 14. Flag 0x10 on mode 0 or 1 is the alert that walks the other mode-1 slots. The same-pointer loop is not used as that alert.

A party attack uses `inflictDamage` with the number from the unread item function. Until that function is read, a test supplies the damage and checks the write. Width 63 is what a large-fireball flight asks for. Sound 0 and sound 255 place the monster and play nothing.

## Tests

1. `set_mode(7)` writes `destX` and `destY` from `party_pos()`.
2. A mode-13 slot ignores `set_mode(7)` and accepts `set_mode(14)`. Mode 14 leaves hit points at 0 and the next `update` clears `damageReceived`.
3. Flag 0x10 on a mode-0 or mode-1 monster sets the other mode-1 monsters to mode 7. Updating one monster does not do that by itself.
4. A monster target in mode 13 or 14 takes no further damage. A positive hit stores `0x8000 | damage`, sets flag bit 0x10, and clamps hit points. Reaching 0 sets mode 13.
5. Character target 4 that equals a living character id hits that slot. The same value with no matching id returns 0. Flag bit 8 returns 0. Item 229 with `flags == 4` quarters the damage before the hit-point call. A hit that exhausts hit points sets flag bit 8 and stores 0.
6. A large-fireball step asks for placement width 63. The 256 expression stays commented out.
7. `sounds[0]` of 0 and of 255 place the monster and start no sound.
