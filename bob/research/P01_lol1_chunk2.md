# P01 LoL1 chunk 2: hero select

No Godot was run. The tree is `~/lol1_godot` at `9987d7e`, clean. L06 chunk 2 is the selection screen. Chunk 1 already stores `hero_id` and round-trips it. This chunk does not rebuild that packet. Party joins are chunk 6. The portraits already draw. `party_test.gd` checks the four templates and the portrait panels. It is not a click test.

## Data

`party.gd` `HEROES` maps Ak'shel to −9, Michael to −1, Kieran to −8, and Conrad to −5. ScummVM `startupNew` uses `selectIds[]` in that same index order: 0 is −9, 1 is −1, 2 is −8, 3 is −5. `_charPreviewNamesDefault` is Ak'shel, Michael, Kieran, Conrad.

`getCharSelection` returns index i when the input flag is 200 and the mouse lies inside `_charPreviews[i]`. Each box is 32 by 32: `x` through `x + 31`, `y` through `y + 31`. The origins in `staticres_lol.cpp` are (0x060, 0x7F), (0x09A, 0x7F), (0x0D4, 0x7F), and (0x10F, 0x7F). A miss returns −1. The three attribute bytes on those rows are drawn and were not given names.

`chooseCharacter` loads CHAR.CPS (CHARCHI.CPS when the language is ZH_TWN), BACKGRND.CPS, ITEMICN.SHP, and CHARGEN.WSA, and sets the language file LOLINTRO.DIP. A portrait click stores the index. `selectionCharInfo` then shows FACE09.SHP, FACE01.SHP, FACE08.SHP, or FACE05.SHP for indexes 0 through 3. Those are `face%02d` of the absolute ids. `selectionCharAccept` returns 1 inside (88, 180, 41, 15) and 0 inside (196, 180, 41, 15). The ZH_TWN pair is (223, 176, 42, 17) for 1 and (271, 176, 43, 17) for 0. Any other click returns −1. A result other than 1 clears the index and the loop continues. A result of 1 returns the index. `startupNew` then calls `addCharacter(selectIds[index])`. The value 100 restarts the king intro. The control that writes 100 was not read.

The demo sets `_charSelection` to 0 and skips `chooseCharacter`. This chunk does not spec the demo.

`walk.gd` export `hero` stays the four names, default Conrad. Startup makes inventory types 216, 217, and 218, then `add_character` for `HEROES[hero]`. Headless tests that do not click keep that export.

Specialty sentences stay unmerged. The walkthrough calls Kieran balanced and Conrad a rogue. The reference calls Kieran fast and Conrad balanced. The manual page 1 calls Ak' Shel the magic one, Michael the fighter, Kieran the fast one, and Conrad well-rounded. The manual spelling is Ak' Shel. The table spelling is Ak'shel. `raceClassSex` stays 0, 0, 2, and 4 on Michael, Conrad, Kieran, and Ak'shel. No specialty name is stored.

Voice names KING01, KING02, and KING03 are requested by the intro, the reminder, and the outro. Playback waits for chunk 9. A quiet `playSoundEffect` still lets the screen finish.

## Behaviour

The screen shows these four boxes and no fifth. A click inside one box stores that index and opens the info panel. Accept runs the existing new-game order with that id. Cancel stores nobody and does not make items 216, 217, and 218. An index outside 0..3 does not call `add_character`.

Save and load keep the id through the chunk 1 packet. This chunk does not change version rejection or the three-person refusal.

## Tests

1. A click in (0x060, 0x7F) size 32, then accept, stores id −9 and the name Ak'shel. `count()` is 1. The same path gives −1 Michael, −8 Kieran, and −5 Conrad for the other three origins.
2. A click outside all four boxes leaves the index unset. Cancel on the info panel leaves the party empty and does not make items 216, 217, and 218.
3. After accept, save and load with the chunk 1 packet. `hero_id`, `id`, and `name` match. `raceClassSex` is the table number. The packet has no specialty string.
4. The headless export `hero` still defaults to Conrad. Setting it to one of the four names adds that one hero with no click.
5. `party_test.gd` remains the portrait check. These five do not replace it.
