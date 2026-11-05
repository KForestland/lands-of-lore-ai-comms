# M05 LoL1 interface, party, and combat

No Godot was run. No manual was in `lands-of-lore-1-re/docs` or `ScotiaEraPrototype/RESEARCH`. Nothing below is a manual page. A behaviour is exact where the Godot port and the ScummVM source that was opened say the same thing. L06 stays the build order. L04 stays the reuse limit. Fireball collision width stays 63.

## Interface

The frame is the original `playfld.bin`, 320 wide, drawn through the palette shader. The view copied into that frame is 176 by 120 and starts at x 112 (`walk.gd` `VIEW_X`). A left click in that rectangle uses the wall ahead when it hits `Rect2i(24, 8, 128, 96)` in view space. The arrow pad is six rectangles: forward (33, 131, 22, 19), back (33, 150, 22, 18), strafe left (11, 150, 22, 18), strafe right (53, 150, 22, 18), turn left (11, 131, 22, 19), turn right (53, 131, 22, 19).

README keys, DECODED from that file: W or Up steps forward, S or Down steps back, A and D strafe, Q and E or Left and Right turn, Space or Enter uses the door ahead. Numpad 8, 2, 4, 6, 7, 9, and 5 are also named there. F1 shows the party position. The selection screen, the compass drawing, TIM, and sound are not in the port. The remake still has to grow those. This pass did not read their pixels.

Inventory storage is 48 slots (`_inventory[48]` in `walk.gd`, and `olol_checkPartyForItemType` loops 48 plus the hand). Nine slots are drawn, at x 0x6A, 0x7F, 0x94, 0xA9, 0xBE, 0xD3, 0xE8, 0xFD, and 0x112, y 179, each 21 by 21. Scroll is one slot, or nine with shift. A new game puts item types 216, 217, and 218 in the first three slots: Salve, Aloe, and Ginseng.

The portrait panel is 66 by 34. The magic bar is drawn before the hit-point bar. The two labels are lands strings 0x4253 and 0x4254, which are the letters M and H. One character is selected. The weapon slot and the magic slot are the two icons under the bars. `weapons_disabled`, a zero `weaponHit` when flags demand it, or no affordable spell level draws the checker grid over that icon.

Door timer 0 runs every 15 ticks (`timer_lol.cpp` and `doors.gd`). Wall flag 0x10 is the open frame and 0x20 is the closed frame. A switch on the party's own block does not start the door.

Message text fades on timer 11, period 360. Lamp state is timer 10, period 360. Portrait animation is timer 9, period 10. Point regen is timer 8, period 1200. Those periods are tick counts from `setupTimers`. `walk.gd` uses a 16 ms tick. `KyraEngine_v1` sets `_tickLength` to `(uint8)(1000.0 / 60)`, which is 16, and `LoLEngine` extends `KyraRpgEngine`. This pass did not read that parent's constructor, so the 16 ms figure stays the port's tick plus the v1 line, not a second measurement.

New-game campaign words in `game_state.gd`, matching the comments there: 100 flag bytes, 24 script words, 8 more words filled with 0x100, 41 credits, brightness 3, `compass_broken` 0, `lamp_oil` 0. There is no save call.

## Party

Nine templates, from `charDefaults`. Hit points, magic, might, and protection are the max and base values stored there. The three skill numbers were not given names. `raceClassSex` was not given a specialty name, so L03's Kieran and Conrad disagreement stays unknown.

| id | name | hp | mp | might | protection | skills | starting item types |
| --- | --- | --- | --- | --- | --- | --- | --- |
| -1 | Michael | 20 | 6 | 5 | 2 | 1 1 1 | 44 Dagger, 138 Shirt, 162 Sandals |
| 2 | Timothy | 27 | 5 | 0 | 0 | 3 2 1 | 93 Rapier, 131 Buckler, 153 Leather jerkin, 162 Sandals |
| 3 | Baccata | 22 | 18 | 0 | 0 | 1 1 3 | 108 Staff, 149 Kite shield, 145 Helm, 153 Leather jerkin, 129 Boots |
| 4 | Lora | 48 | 5 | 0 | 0 | 1 4 1 | 137 Torn shirt, 162 Sandals |
| -5 | Conrad | 23 | 10 | 2 | 3 | 1 1 1 | 44 Dagger, 138 Shirt, 162 Sandals |
| 6 | Paulson | 105 | 45 | 0 | 0 | 5 2 3 | 138 Shirt, 129 Boots |
| 7 | Dawn | 50 | 80 | 0 | 0 | 1 2 10 | 138 Shirt, 129 Boots |
| -8 | Kieran | 23 | 8 | 5 | 1 | 1 1 1 | 44 Dagger, 138 Shirt, 162 Sandals |
| -9 | Ak'shel | 28 | 32 | 1 | 1 | 1 1 1 | 44 Dagger, 138 Shirt, 162 Sandals |

Each character has 11 item slots. `addCharacter` copies a template only when fewer than three members have flag bit 0 active. The ScummVM exception, absent from `party.gd`, is level 16 block 0x225 when slot 2 is Lora and the new id is Paulson: her 11 items are placed on that block and the count is treated as 2. Starting items also run item script 0x80 in ScummVM. The port's `add_character` does not. A character face bank is `face%02d` of the absolute id. The next face delay is a roll of 1 through 12, plus 6.

The selectable heroes are the four negative ids. The selection screen is not in the port. The portrait timer walks four slots and skips a slot whose flag bit 0 is clear. Five update-event slots sit on each character.

## Combat

Monster timers 0x10 and 0x11 each have period 6. Timer 0x11's first run is three tick lengths later. Each timer updates every other slot: 0x10 starts at slot 0, 0x11 starts at slot 1, both step by 2, and both stop at 30. That is the port's even-slot then odd-slot comment, and it is the loop in `timerProcessMonsters`.

`updateMonster` in `sprites_lol.cpp` names the modes that were read:

| mode | what the comment or the case does |
| --- | --- |
| 0 and 1 | friendly. Mode 1 also moves. Flag 0x10 on mode 0 or 1 sets other mode-1 monsters to mode 7. |
| 2 | move |
| 3 | if the party is on an adjacent block, or the block test says so, set mode 7 |
| 4 | stray, not tracing the party |
| 5 | recovery after an attack, and monsters rearrange. `partyAwake` is set. |
| 6 | the same recovery without rearranging |
| 7 | chase. Destination is the party. Distance attacks are tried before close attacks. |
| 8 | first recovery. After more than 2 ticks, go to mode 5. |
| 9 | close attacks until the tick counter hits 0, then mode 7 |
| 10 and 11 | no case in `updateMonster` |
| 12 | after more than 13 ticks, run level script 0x404 |
| 13 | death. After more than 2 ticks, `killMonster`. Mode 13 ignores a later mode other than 14. |
| 14 | hit points are set to 0 and damage received is cleared |

Flag 0x40 on the property regens 1 through 8 hit points, capped at the property's hit points. The port's `update` does that regen and the movement modes. Its own comment says combat modes 3 and 5 through 13 are not ported. The remake matches the ScummVM cases, including that gap on 10 and 11. `setMonsterMode` to 7 writes the party position into the destination. A change from mode 1 to mode 7 also enters a 30-count loop, and that loop tests the same monster pointer rather than `_monsters[i]`. The first pass sets that one monster to mode 7, and the later passes then skip. The alert that does walk the slots is the flag 0x10 case in modes 0 and 1. The port's `set_mode` comment says the party-wide alert is not ported, and `set_mode` does not contain that loop.

Live monsters cap at 30. Hit points at spawn are the property hit points times `monsterModifiers1[difficulty]`, shifted down 8, then times a roll of 1 through 128 plus 192, shifted down 8. Level 12 type 2 skips that second roll. Difficulty 0, 1, and 2 are easy, normal, and hard. The modifier tables were not copied into this note.

Flying objects use timer 4, period 1. The large fireball's placement width stays 63.
