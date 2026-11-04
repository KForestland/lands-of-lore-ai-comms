# K7 — Behaviour specs for Act 1 MISSING beats 73, 77, 79, 83, 84

Run 2026-11-04 by Kimi Code CLI (read-only). Source: hintbook.txt line numbers only. Lead spot-checked 2433, 2486-2488, 2528-2533 and 'cellar' (0 hits): match. Note: Spark on the crate is LEVEL THREE (2530).

## Beat 73 - Boulder breaks the floor, opens a cellar

UNKNOWN. The hintbook contains no mention of a cellar anywhere, and no Dark Halls / Monastery passage describing a boulder falling from a wall and breaking a floor. The only boulder encounters the book describes are: a rolling-boulder trap room in the Hive Caves where two boulders roll back and forth and the player dodges them to grab a healing scroll (lines 2787–2796), and a later lethal boulder at line 4588 ("the center, a boulder will quite suddenly and firmly end Luther's life"). Neither matches this beat, so no player-facing behavior can be specified from this source.

## Beat 77 - Click every bookshelf for the secret ways

- **What the player does:** While exploring the Dark Halls, click on every bookshelf. Some are sliding/secret bookcases.
- **What happens:** Clicking bookshelves reveals secret accesses hidden throughout the level (line 2433: "be sure to click on all the bookshelves to find all the secret accesses in the Dark Halls"). This is also how the Dark Halls are entered in the first place — the player stacks boxes next to a bookshelf in the Monastery library, climbs up, and attacks the bookshelf with a spell or weapon to breach the entrance (lines 2400–2402).
- **Success:** Secret rooms open, yielding loot: Ancients' Stones in the room with all the beds and a Healing Scroll in the room with the sliding bookcase (lines 2480–2481), and the Prism spell group scroll hidden in a bookcase (lines 2486–2487). Late in the level, "yet another sliding bookcase" opens onto the final hall leading toward the round blue-ball room (line 2527).
- **Fail:** The hintbook describes no fail state for missing bookshelves; skipping them simply means missing the secret rooms and their contents (inferred from lines 2433, 2480–2487).

## Beat 79 - Find the Prism scroll in a bookcase and right-click it

- **What the player does:** Find the Prism spell group scroll hidden in one of the Dark Halls bookcases (line 2486–2487), then right-click it on Luther (lines 2487–2488).
- **What happens:** The Prism spell group is added to Luther's repertoire — the same interaction the player already used with the Summon Group Scroll from the Museum (line 2488: "as you did with the Summon Group Scroll from the Museum"; the general rule that the first scroll of a new group adds the group to Luther's repertoire is at lines 1598–1599).
- **Success:** Luther gains the Prism spell group, which the book calls "instrumental to your long-term success" (line 2486); without it the end of the game is much harder, though not impossible (lines 755–756).
- **Fail:** No explicit fail state; the only consequence stated is missing the spell group if the bookcase is overlooked (lines 755–756, 2486–2487).

## Beat 83 - Spark a crystal crate against the steel door; take Colin's Amulet and the Gauntlets of Might

- **What the player does:** At the end of the final hall past the last sliding bookcase, do **not** enter the big round room with the large blue ball yet (lines 2526–2528). Instead, spot the steel door a bit farther down (lines 2528–2529). Take one of the boxes, make sure the crystals inside are showing, and move it next to the door (lines 2530–2531). Step back and cast a level-three Spark spell at it (line 2531).
- **What happens:** "Kaboom! No more door" — the crystal crate explodes and destroys the steel door (lines 2531–2532).
- **Success:** The player enters and finds Colin's Amulet and the Gauntlets of Might (lines 2532–2533), then turns around and grabs another box (needed for the escape, line 2533). (Item notes elsewhere in the book: the Gauntlets of Might increase Luther's might score, lines 1421–1423; Colin's Amulet has no effect the author could determine, lines 1335–1338.)
- **Fail:** Standing too close when Sparking the crate is implied dangerous (the book says "Step back," line 2531); entering the round blue-ball room prematurely is the warned-against mistake (line 2528: "be careful not to enter this round room just yet"), since that room spawns ghosts relentlessly (line 2526).

## Beat 84 - Drag a crate to the bricked-up window at seven o'clock, Spark it, jump out

- **What the player does:** Grab another crystal box after looting the steel-door room (line 2533). Check the automap to locate the bricked-up window at about seven o'clock on the round room — visible as background brown lines that are open (lines 2536–2538). Drag the box of crystals to that spot on the wall, step back, and blow it up with a Spark spell (lines 2538–2539).
- **What happens:** The explosion blows a hole in the bricked-up window — "There you go — an exit" (lines 2539–2540, 2548–2549).
- **Success:** The player jumps through the hole to escape the Dark Halls (line 2540; escaping is described as "much, much harder than breaking in," line 2428). If the box is positioned correctly, the player can escape before the ghosts spawn; on average only about one ghost will be on Luther's back by the time he finishes (lines 2534–2536).
- **Fail / optional rumor:** A rumor says dragging enough boxes into the round room lets in enough light to destroy the blue ball and kill all the ghosts, but this requires hauling several boxes in while dodging or killing ghosts the whole time — the book advises patience and thoroughness if attempted (lines 2541–2547). Either way, the player still must blow the hole in the bricked-up window and jump through the gap to get out (lines 2548–2550).
