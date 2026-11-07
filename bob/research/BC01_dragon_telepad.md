# BC01 — STORY-078 dragon-room telepad is a step-on

Scratch only: detached worktree `/tmp/bc-act3` at `e21eb43` (act3-chain). The live tree was not edited. The patch is unapplied.

## 1. The problem

On the applied port, walking onto the dragon-room telepad only sets `pad_seen`. Travel to the caverns needs aimed E. Kimi K28, problem of the one-way pad in `l16_dragon_room.gd`.

## 2. On the main chain

Yes. The book sends the player through this pad into the Subterranean Caverns. It is not presentation.

## 3. What the game is trying to do

*Gate* plus *orient*. After the dragon is chopped, the player passes through a one-way teleporter and arrives in the caverns. The pad is the way out, not a second aimed action.

Evidence order is original data, then the longplay, then the book.

- Control 74 is kind 5, value 4, group 42056. Event raw `060548a40400`. Command `020100001c31`. Destination L17_HC selector 1 at (1434, 32, -7075). Predicate null. The pad position stored on the control is (2100, 15, 4296).
- The support-owner contract (`BRIDGE_EVENT5_CONTRACT_20261025.md`) is the player tick at `0xD3A13`: when `player+0x7D` differs from `player+0x79`, the new owner is passed to ADA30 (`0xADA30`). Kind 5 value 4 is admitted always, every form. Values 5 and 6 are never. That is a step-on, not aimed E.
- I33 g_00321 is a pale winged shape on a wall. The chop and the teleporter were not on screen. The longplay does not contradict the record, and it does not show the pad.
- Hintbook 5269–5288: chop the dragon and pass through the one-way teleporter. The mantle is not stored on the telepad command.

## 4. Player-visible contract

1. Left-click chops prop 241 (the dragon). Prop 211 (the statue) does not chop.
2. The player walks onto the pad. No E.
3. The scene becomes L17 arrival 1. Luther is at (1434, 32, -7075).
4. The trip is one-way. `pad_seen` stays set, so standing on the pad again does not fire a second exit.
5. The module does not move Luther. Progression moves the scene. `relocates_player()` stays false.
6. No mantle flag is read. No door id is stored.

## 5. Exact vs approximate

Exact: chop prop 241, then a step onto control 74, then level 17 selector 1, once. Not aimed E.

Approximate, and logged: the port does not classify the support owner. Standing within 40 flat units of (2100, 15, 4296) after the chop stands in for that owner change. 40 is the distance the module already used for "on the pad". It is not a decoded footprint.

## 6. Option taken

Smallest faithful option: after the chop, the first time the player is within 40, call `use_exit("control:74")` once. `use_exit` already supplies caller byte = record value 4 and caller byte 2 = event raw byte 5 (0) and then `fire`. Full support-owner classification is not wired for this control.

Not done: a mantle gate, a door id, or moving Luther inside the module.

The applied-tree sentence in AX01 STORY-078 still describes the tree at `e21eb43` (the module does not call `use_exit`; aimed E is the host). This patch is the change. AX01 was not rewritten to claim the patch is already live.

## 7. Prove it like a player

The earned test loads the centre-tower save, chops prop 241, stands at (2100, 47, 4351) which is outside the 40 radius, then calls `move_grounded` toward the pad with no KEY_E. It requires a level-17 selector-1 request while the area is still L16_CA, writes `l16_dragon_room_earned_save.json` before the scene change, reloads that L16 save, then changes scene and requires L17 arrival 1 within 2 of (1434, 32, -7075).

The certifying run was the scratch chain on private display :2, source stable, 11/11 passed. The dragon earned log printed:

`PASS earned centre save -> chop of prop 241 -> walk onto control 74 without E -> L17 arrival 1`

The headless unit log printed `PASS l16_dragon_room_test: chop 241, not 211, level 17 arrival 1`. The cavern earned test then loaded the L16 save and passed, so the save stayed an L16 save. No KEY_E was sent. The patch is unapplied.

## 8. Where it is written

Ledger row dated 2026-11-07, "L16 dragon telepad (STORY-078)", status Adapter (owner rule 2026-10-30). Historical 2026-11-06 rows that say the module does not fire control 74 stay. The new row is the patch.
