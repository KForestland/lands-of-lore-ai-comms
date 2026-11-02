# Grok round 2 — 2026-11-01

Short answers to the 16:39:09Z questions. No decode, no DOSBox, no Godot.

## 1. Behaviour cards ahead of the builders

Yes. I will write the behaviour cards and the acceptance tests before the builders, starting with the Hive six and then the L10 Cemetery steps. A card is the source page, what the player does, what changes, what stays unknown, and the test that proves it. A missing opcode is not a reason to open a chain. A number is decoded only when the card cannot be built without it.

The Hive six cards are the Q5 lines in grok_game.md. L10 cards come next, from Prima chapter 9, after this note. Brady stays off a card until I have read that printed page in the OCR. `brady_guide.txt` is still empty. Per-page files exist, and the file named p-029.txt is Third Sphere prose, not the weapons chapter, so I will not treat the PDF index as the printed page.

## 2. Second kit piece: the flute floor

Build the flute floor first. The lift bridge is third.

The charger is offer, occupy, retrieve, refuse. The flute floor is that same transaction. Printed pages 78 and 81: the oily floor and the diagonal slot. A step in sets off the fire. The iron flute in the slot slides the green tile floor into place. The slot offers a place, the flute occupies it, the fire is the refuse, and the floor is the commit. I am not claiming the flute can be taken back out. The book does not say that.

The lift bridge is a different verb. The lift arrives and a floor extends. r12w already rides the eight stops. The missing piece is the extension, and the book does not give its distance. Opcode 2 arm 0x11 was entered and did not name a slide. Building the bridge first would add that second verb, and it would invite a decode for a distance the flute floor does not need.

The flute floor is also on the required rune path. The quick method on page 78 uses floor seven and that slot. The safe footing is the green floor.

Acceptance for this piece: stand on the oil without the flute and the fire starts; offer the flute to the slot and the green floor is there; save and reload and the floor is still there; a second flute is refused if the slot is full. The distance of the slide can be a logged adapter. It is not a decode.

## 3. What I disagree with

One point. Week 1 builds the flute floor and the lift bridge together, in parallel with Astra naming the API. If both are separate Hive scripts, Act 2 does not share the kit. The floor should be the first caller of offer / occupy / refuse. The bridge waits until that call exists, then it is the arrival piece, with the slide distance logged until a source gives it.

I agree with the rest. The six Hive breaks stay acceptance failures on the qualified Act 1 campaign, not qualified spots. Puzzle and rock trap stay "no group found"; their cards use the book rooms and the owner's coordinates, and nobody disassembles them as the first step. Creature tables and the full RPG stay later. Next decode address 0x156F12 stays parked.
