# O05 LoL1 chunk 1: save, the chosen hero, the party packet

No Godot was run. The tree is `~/lol1_godot` at `9987d7e`, clean. L06 chunk 1 is save and load, and it adds no scene. Hero select is L06 chunk 2. Party joins are L06 chunk 6. This spec covers the packet those three share. It does not build combat, TIM, or the later cards.

The original DOS or ScummVM save file was not read. The packet below is an adapter. It round-trips fields the port already stores. It is not a claim about the retail file.

## Packet

One JSON object, version 1. A loader rejects any other version and leaves the new game untouched.

`game`, from `game_state.gd`. `flags` is 100 bytes, bit-addressed: flag n is byte `n >> 3`, bit `n & 7`. `script_vars` is 24 integers (`global_script_vars`). `vars2` is 8 integers (`global_vars2`). Then `credits`, `brightness`, `compass_broken`, `lamp_oil`, `update_flags`, `scene_default_update`, and `visited_levels`. A new game sets credits to 41, brightness to 3, lamp oil to 0, flags to 0, and every `vars2` entry to `0x100`.

`walk`. `level`, `block`, and `direction`. Direction 0 is north, 1 east, 2 south, 3 west. A new game with scripts on is block 557, direction 0. Direction 2 on the keep-gate path is a different stored value, not a second format.

`party`. `hero_id` is one of Michael −1, Conrad −5, Kieran −8, Ak'shel −9. `selected`, `selected_spell`, `available_spells` (8 integers; a new game is `[0, -1, -1, -1, -1, -1, -1, -1]`), `weapons_disabled`, and `characters`. Each character is the `charDefaults` record plus `face_bank`, `defaultModifiers`, and `nextAnimUpdateCountdown`. The record fields are `flags`, `name`, `raceClassSex`, `id`, `curFaceFrame`, `tempFaceFrame`, `screamSfx`, `itemsMight` (8), `protectionAgainstItems` (8), `itemProtection`, `hitPointsCur`, `hitPointsMax`, `magicPointsCur`, `magicPointsMax`, `field_41`, `damageSuffered`, `weaponHit`, `totalMightModifier`, `totalProtectionModifier`, `might`, `protection`, `items` (11 item ids), `skillLevels` (3), `skillModifiers` (3), `experiencePts` (3), `characterUpdateEvents` (5), `characterUpdateDelay` (5). `raceClassSex` is stored as the table number. Michael and Conrad are 0, Kieran is 2, Ak'shel is 4. No specialty name is added.

`items`. All 400 slots. Each slot is `next_assigned`, `next_draw`, `flying`, `block`, `x`, `y`, `level`, `prop`, `frame`. A free slot keeps frame `0x8000`. `assigned`, `draw`, and `bdir` are the 1024-length chains of the loaded level. `bdir` starts at 5. `inventory` is 48 item ids. `inventory_cur` is the scroll index. `item_in_hand` is one id or 0. Character `items[]` and the inventory hold these ids, so the item table is restored before the party.

`monsters`. The level number and the 30 slots. Each slot is the `monsters.gd` blank: `id`, `next_assigned`, `next_draw`, `flying`, `block`, `x`, `y`, `destDirection`, `shiftStep`, `destX`, `destY`, `hitOffsX`, `hitOffsY`, `currentSubFrame`, `mode`, `fightCurTick`, `direction`, `facing`, `flags`, `damageReceived`, `hitPoints`, `speedTick`, `type`, `numDistAttacks`, `curDistWeapon`, `distAttackTick`, `assignedItems`, `equipmentShapes` (4). Monsters are per level. This packet stores the live level only. Temp data for other visited levels was not read and is not invented. `visited_levels` is still stored.

Load order. Reject a bad version. Restore items, then inventory and `item_in_hand`, then the party, then monsters. Do not call `startupNew`'s three `make_item(216 + i)` calls, and do not call `monsters.reset`, when a save loaded. A missing file keeps today's new game.

## Hero select

L06 chunk 1 only stores `hero_id`. The screen is L06 chunk 2, and the portraits already draw.

The screen shows the four templates and no fifth. A click stores that id and then runs the existing new-game order: items of type 216, 217, and 218, then `add_character` for that id, which also makes the hero's own items. The headless export `hero` stays the four names, default Conrad, for tests that do not click.

## Party data

`characters` holds up to four records so a later join has a slot. `add_character` returns false when `count()` is already 3. `count()` counts records whose `flags` bit 0 is set. Chunk 1 does not change that refusal. The Lora and Paulson workaround is chunk 6 and is not in this packet's behavior. A save of a one-hero game reloads as one hero. A save that already contains two or three reloads with the same ids, in the same order.

## Tests

No test invents a retail save byte.

1. New game, no file. Block 557, direction 0, credits 41, lamp oil 0, flags all 0, `vars2` all `0x100`, inventory types 216, 217, 218, one character, and the requested hero id.
2. Round trip. Set flag 10 (byte 1, bit 2). Set script var 3. Set credits, lamp oil, and `compass_broken`. Step to another block and face south (direction 2). Put a known id in `item_in_hand` and in inventory slot 4. Save, construct a fresh state, load. Every field above matches, including `next_assigned` on that item and frame `0x8000` on a free slot.
3. Each of the four hero ids. After save and load, `count()` is 1, `id` and `name` match, and `raceClassSex` is the table number above. An unknown id does not append a character.
4. Fill three characters by calling `add_character` with three of the four ids. The fourth call returns false. The reloaded packet still has three, and the refused id is absent.
5. Monsters. After the opening script has moved the guard, save and load on the same level. The 30 slots match the saved slots. They are not the blank `reset()` slots. Loading does not run `reset`.
6. A version other than 1 is rejected. Credits stay 41 and the party stays the new-game hero.

`party_test.gd` already checks the four templates and the portrait panels. It is not a save test. These six are the new ones.
