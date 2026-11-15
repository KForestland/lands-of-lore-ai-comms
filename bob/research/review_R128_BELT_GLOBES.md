# R128 belt, globes, and give-list — HOLD

Head `a5d56a0427d006c02435962a896310c51c6397d0` on `sol/item-belt-globes-20261115`. Review tree `~/opus_work/lol2_review_r128` only. Rendered, `Engine.time_scale` 1, physics 60, private display `:91`, dummy audio, `--demo-interface` so F is the belt. No SCRIPT ERROR. Grok did not merge.

## The save

HOLD. After the same empty globe `act2:L10_DC:item44` was charged at the yellow altar, taken, cast, and charged again, real F5 refused. The player was on the floor. No autosave was in progress. Save admission was empty. Both presses showed `Save failed: Invalid charger receipt.` Slot 1 was not rewritten.

The charger stores a receipt `L10:yellow:` plus the globe id and keeps that list across a repeatable cycle. The second insert of the same id appends the same receipt. `act2_charger_state.validate` rejects a repeated receipt, and the whole-game save stops. F9 of that belt was not reached.

## What was played

Real keys and the mouse. Disclosed aids, named in the log: a health set to 10, `stand_at` at the yellow altar and at tomb 154, and item grants. Frames are under `/tmp/r128_frames/`.

(a) PASS. Museum lock 87. E pickup put `museum:control87:Sk_key` alone in slot 0, definition 94. Facing lock 88 rolled to it, left the door shut, and the belt read `E — use Sk key` with the center card gold. F did not use it. Waiting did not use it. E opened the lock and the key left the pack. `a_aimed_lock.png`, `a_opened.png`.

(b) PASS. Bracket right, bracket left, wheel down, and wheel up each walked the four filled ids and returned to `act2:L10_DC:item44`. The fifth slot was empty and was skipped. F on aloe at health 10 consumed it and health became 16. A wrong item, rolled on after the altar had already selected the empty globe, gave one line, `That does not fit here`, and stayed in the pack. The altar globe stayed hidden. F on the fitting empty globe does not charge it. E does.

(c) PASS. Yellow F took mana from 20 to 17, said `Spark cast. The glass globe is empty.`, and did not teach Spark. The empty globe charged again at the same altar. Blue F on ghostly head 67 recorded shot 67, emptied the globe, and did not teach a school (`c_head.png`). White F kept the globe and the mana, and the line was `The white globe holds a spell that does nothing here yet.` (`c2_white.png`). At tomb 154 the belt selected the blue globe. F said `The spell has no effect here` and kept the globe. E opened the tomb and consumed it (`c2_tomb.png`).

(d) PASS. The give list at 1280x720 and at a 960x540 window held 25 types plus the empty hand. `Healing Scroll x2` had an icon. The wheel and the down arrow reached `Ancients' Stone`. Names on screen were catalog names (`Hrn Belial`, `SS1`, `Reaver of GO`, `Sk key`, `Broken Thohan`, `Enchanted Thohan's Sword`). The popup stayed inside the window. `d_open_1280.png`, `d_scrolled_960.png`.

(e) PASS. With nothing aimed, the belt name faded from alpha 1.00 to 0.00 (`e2_fade.png`). The wheel / E / F footer stays up for the session minute. The monastery room hides the HUD, and the belt hides with it.

(f) The round trip above is the hold. A separate r19n owner save, byte-copied into the private user directory and loaded with real F9, came up in `L13_RC` with belt `[96, 76, 101, 102, 112]`: Iron Flute, Control tokn, Blue globe, Dracoid Sigil, Amber. Carried 30, which is the file's own 16 collected items plus 14 `quests.act2_items.carried`, including that save's charged blue globe. The source file was not rewritten. `f_owner_960.png`, `f_owner_1280.png`.

(g) On the Temple platform, before Belial, F is the belt and E still descends. The loaded belt's active item was Broken Thohan. F said `That does not fit here` and Belial stayed. The descend prompt stayed (`g2_f_before.png`). E said `The weighted elevator descends into the Chamber of Voices.`, health stayed 29, and resets stayed 0 (`g2_e.png`). A granted yellow globe did not replace the five quest slots `[11, 96, 102, 35, 76]`. The pack click missed that row, so Spark from the belt on the platform was not seen.

(h) At 960x540 the belt stays clear of the portrait, and the give list stays inside the window (`b_belt_960.png`, `g2_960.png`, `d_scrolled_960.png`). The one-line action notice sits against the belt name (`The item is used.` over `Item belt`). The slots stay readable. On the owner load, `Autosaved.` sits just above the belt name, and a world glow in the Citadel passes behind the left slots.

## Verdict

HOLD. A second charge of the same glass globe makes F5 refuse with `Save failed: Invalid charger receipt.` That save is the Monday bar. The key, the rolls, the aloe, the wrong item, Spark 3, the blue head, the white refusal, the tomb, the give list, the name fade, the owner belt, and Temple F-stays / E-descends are in place.
