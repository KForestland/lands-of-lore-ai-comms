# H06 Kit'yara's knife for Daniel

Beat 52. Owner F10 2026-11-03 17:54:07, jungle native (775, 1718). Read from `L4_HJ.MIX` and `L4_HJ.json`. Opcode 2, opcode 9, and the dialogue picker were not entered.

No new owner F10 after `TRIAGE_20261103.md`.

## Where she stands

Control 0, static slot 57 `Kityara` (file 13286535), is at (808, 1802), height -14, region 3767. That is 90 from the owner point. She has 14 real events.

The knife flag is local slot 41. Counting from `villager` at file 13153135, slot 41 at file 13154816 is `kityara_gave_knife`. Kind 6 value 0, predicate 206 `0005000000` (her own state equals 0), group 18022 (file 12746326, MIX match) writes it:

- opcode 9 on prop 65
- opcode 2 `021000000600` (arm 0x06)
- opcode 9 on control 0
- opcode 198 `c60000002901` sets slot 41 to 1
- opcode 16 sets her state to 1
- opcode 2 `020100002700` (arm 0x27)

A second flag, slot 23 at file 13154078 `Kityara_Given_Orb`, is written by group 18086 (file 12746390, `c60000001701`) along with opcode 2 arm 0x18. That is the orb handoff, not the knife.

Predicate 185 is `0003290001` (slot 41 equals 1). No event in L4 cites it. No later level was searched for an inventory check. The item id of the knife was not in these commands.

## When she gives it

BRADY printed page 73 (file lines 2793-2795): a special knife for her son, and she gives it only after the Runes have been retrieved. She may also give a special item if you give her what she asks for (the orb).

HINTBOOK lines 2412-2415: after you leave the armorer (the Power Orb traded for Firestorm, or the museum sword repaired), you meet her again. Accept the gift. It is for Daniel.

HINTBOOK lines 1669-1670 name the item Warblade: "This is Daniel's gift from his mother."

The two book times are both after the Hive errand. They were not merged into one trigger. Which of her kind values runs group 18022 in play is still the unentered dialogue.

## What it opens later

BRADY lines 2799-2801: you cannot enter the Wild One settlement across the River Bane until you have the knife. You can cross and talk to a Wild One, and he turns you away.

BRADY lines 3702-3703: show the knife to the guard outside and he lets you in. Without it you fight your way in.

HINTBOOK lines 2982-2984: show Daniel's gift to the Huline guard and he lets you into the Wild Village. Do not attack him.

HINTBOOK lines 2898-2919: in the first meeting, put the gift on Daniel's chest (the middle of the three). Success is Daniel saying "Ah, Grandfather's blade ...". "Uh oh" is a miss. Attacking him with it calls the Draracle. Failing to pass the knife makes the rest of the quest fruitless.

HINTBOOK lines 2920-2922: when the hoppers arrive he drops the knife. Pick it up. The same paragraph says you need it to enter the village.

HINTBOOK lines 2997-2999: his treehouse is on the left. Hand the gift over there. He can invite you into the tribe.

HINTBOOK line 2414 calls the gift the key to the next major area. The next paragraphs enter the Savage Jungle.

These village sentences are separate visits in the book. They were not collapsed into one click.

## Required or optional

REQUIRED. HINTBOOK 2917-2919: the quest does not continue if Daniel never receives the knife. Brady's guard fight is a way past the door without showing it. The handoff to Daniel is the step both books treat as the one that must happen. Killing her changes the later fight (BRADY 3766-3776): he shows no mercy if she is dead, and mercy if she lives. That fight is how you become a Tuani, which Brady's must-do for the Savage Jungle includes.

## Frame

No longplay frame was opened.

## Still open

- The inventory id inside group 18022. Slot 41 is the flag. The opcode 2 arms were not entered.
- Which later level reads the item. L4 never tests predicate 185.
- A longplay frame of her giving it.

Grades: her placement, the static name, and the two local names and writes are DECODED. The timing, the guard, and Daniel's chest are HINTBOOK and BRADY as cited. The frame is open.
