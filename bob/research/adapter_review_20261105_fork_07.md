# R2 adapter review fork 07, 2026-11-05

No Godot was run. No opcode callee was entered. The idle line still names ~/opus_work/lol2_r12y at 56812f9. These rows were read in ~/opus_work/lol2_r15 at f6a5aa4. All seven deviation files match the r12y copies byte for byte.

## 0072 cave

`0072-row-2026-10-26-cave.md` is pending. While prop1333 rests, player-only walls close neck exits 866 to 768 and 870 to 774.
The beast arms the rock on plate109. A bump then slides it, and the walls come off. Group9470 was not entered.
The host comment names an unread move. The native radius stays untraced. Radius 24 stays the row.
DECODED. `cave_boulder1333.gd` matches r12y. Only the player mask receives bit 11, and that bit clears when the host state leaves rest.
`cave_opening_route_walk.gd` matches r12y. Form 1 walks the rock. Form 2 takes the low tunnel.
`player_form_body.gd` matches r12y and stores height 8 at index 2.
The route-walk comment also names regions 636 and 778. The region graph was not reopened. The 20 to 40 headroom was not remeasured.
`cave_walkthrough.gd` differs by a lever prompt. Its region631 rising edge still calls the request.
`player_curse.gd` matches r12y. From a human idle phase, `choose_form` returns beast or lizard.
A later contact calls again. The function accepts that call when the form is human and the phase is idle.
HINTBOOK lines 2022–2024. Bump the rock out of the way to the north as the Beast. Those lines print no radius and no region id.
BRADY lines 2284–2290, marker PDF PAGE 62, printed 61. A boulder blocks the path. The right-hand tunnel is the first morph. A beast goes back and pushes the boulder. A lizard keeps going through the low-ceilinged tunnel, or returns to the other path. The sentence is cut after "go around".
Lines 6386–6387, printed 147, say pass the first roadblock by morphing into either a beast or a lizard. Those two Brady sentences stay two sentences. They print no 24, no 20–40, and no 8.
The neck walls stay the row. No printed number replaces them. No simpler native build while the radius and group9470 stay unread.
Open: the native radius, the unread group9470 move, the 20–40 headroom, and regions 636 and 778.

## 0073 jungle plank

`0073-text-jungle-wooden-plank-bridge-support-and-creature.md` is a note. Plank210 is a beast-only support-entry break, hosted apart from the Bacatta causeway.
The four-unit grounded support adapter replaces the original vertical solver. Selector1 removes deck faces. The whole-box collision remains.
Assembly211 and five debris sprites appear on the break, with the original sound requests. Region3032 then refuses creatures on layer11.
Quest state restores the break without replaying sound.
DECODED. `docs/jungle-bridge-break.md`, `jungle_bridge_break.gd`, `jungle_bridge_break_state.gd`, `source_control_contact.gd`, and `creature_region_barrier.gd` match r12y.
Value 9 is admitted for form 1. The cave walk uses form 1 as the beast.
The foot test is `absf(foot - height) <= 4.0`. The contact comment names ADA30. That callee was not entered.
The barrier constant is `1 << 10`. A causeway test calls that bit layer 11.
Player movement is left off that bit. A creature already inside receives an exit exception and loses it after leaving.
Aim rays were not read. The selector callee was not entered.
HINTBOOK lines 2361–2367. A long wooden bridge on the way to the Monastery collapses under the Beast.
BRADY lines 2805–2809, printed 72. The rickety bridge over the quicksand fails under a beast, and the plank may be shoved back.
Line 6570, printed 152. As a beast, you can collapse the bridge over the quicksand.
The monastery sentence and the quicksand sentences stay separate. Books print no plank210, no 4, and no region3032.
The four-unit adapter stays the row. Brady's shove-back sentence has no host in the files opened here. No simpler native build while ADA30 stays unread.
Open: whether plank210 is the quicksand bridge, the unread vertical solver, the selector callee, and aim rays.

## 0074 item slots

`0074-row-2026-10-25-all-areas.md` is pending. Slot choice for 170 definitions comes from record byte +0x3F.
The row maps 0x44 and 0x48 to weapon, 0x50 and 0x53 to offhand, and 0x60 to armor. Rings, amulets, and gauntlets at 0x43 stay carried only.
Net of Exile, class 0x40, stays a held weapon. The row says the native reader of the byte is not traced. The row's 34 was not recounted.
DECODED. `item_definitions.gd` matches r12y. `CLASS_SLOTS` is that map, and 0x43 is absent.
The comment says 0x43 stays carried only.
`docs/item-definitions.md` matches r12y and later names address 8FD40. That callee was not entered.
The unread reader stays the row's gap.
The fixed Net of Exile id in `item_catalog.gd` is slot weapon. The class byte on the definition record was not re-read.
That catalog differs from r12y by four Act 2 fixed rows and a use on generic index 119. The class map is the same.
HINTBOOK lines 1421–1423 say the gauntlets of might increase might. Line 1459 names a cat's eye ring.
BRADY lines 1155–1158, printed 31, say wear the gauntlets of striking. Lines 1313–1314, printed 35, say gauntlets of might increase strength.
Line 3147, printed 79, says killing the Executioner may yield a Net of Exile. A hintbook search found no "Net of Exile".
The wear sentences and the carried-only rule stay separate. Books print no 0x3F, no 170, and no 34.
The slot map stays the row. No simpler equip build for 0x43 while 8FD40 stays unread.
Open: the unread reader, the unrecounted 34, and original slots for rings, amulets, and gauntlets.

## 0075 generic ids

`0075-row-2026-10-25-all-areas.md` is pending.
Generic ids `item:defNNN` cover 165 carriable definitions and are admitted only in scope "world".
Act 1 keeps per-placement ids.
Untraced definition stats stay raw and unused.
DECODED. In `item_catalog.gd`, `ids()` appends those generic ids only when the scope is world and the index is carriable.
Scope order is cave, museum, jungle, world. An Act 1 scope stops before world.
`item_definitions.gd` says stats that stay undecoded are unused, and it names ghost rows 152–156.
The row's 165 is 170 minus those five. The generated JSON was not recounted.
The r15 catalog use on generic 119 is one traced behaviour. It leaves the id outside Act 1.
HINTBOOK lines 1011–1014 name a limited inventory and print no count.
Books print no `item:defNNN` and no 165.
The world scope stays the row.
No printed source is more faithful.
No simpler build puts these ids into Act 1 saves.
Open: the unrecounted 165, and the raw bytes still marked undecoded.

## 0076 inventory text

`0076-row-2026-10-25-inventory.md` is pending.
An item with no traced inventory use and no slot shows "No inventory use is known for this item yet."
Unknown non-definition finds keep "This item has not been identified."
DECODED. `use_hint` in `item_catalog.gd` returns the first sentence when `definition(id)` is at least 0, the use is empty, and the slot is empty.
It returns the second sentence for every other id.
That function text matches r12y. The rest of the file differs as in 0075.
HINTBOOK lines 1015–1018 call the problem figuring out what something does.
Lines 1023–1027 point at the item list. They print neither refusal sentence.
A Brady search found neither sentence.
Books print no such number.
The two sentences stay the row.
No printed line is a more faithful refusal.
No simpler build.
Open: which definitions still have an empty use.

## 0077 thieves den text

`0077-text-thieves-den-text-tcel-tdoor-tint-2026-10-27-fabl.md` matches r12y.
The file is a title for Thieves' Den text, TCEL, TDOOR, and TINT, marked fable.
It names `AI_COMMS THIEVES_DEN_DECODE_20261027.md`.
The table under that title has no change row.
It names no script, no player action, and no number.
The named source was not opened.
No gameplay file was compared for this row.
The empty table states no adapter to keep.
No printed source is more faithful. The file states no claim.
No simpler build is present.
Books print no such number.
Open: the empty table.

## 0078 jungle den

`0078-row-2026-10-27-jungle-den.md` is approved. A full pack refuses the Poison Paint and Skull Key shelf pickups with "You cannot carry more."
The sprite and the flag stay untouched, so the pickup can be retried. The Firestorm grant waits in `pending_items`.
The row says the DLL sets the flag first and never checks capacity, at TINT 0x680 and 0xEB8. The LIZ wax host was not reopened.
DECODED. `thieves_den_rooms.gd` and `thieves_den.gd` match r12y. The sprite click returns the refusal before `click_sprite`.
`grant()` appends a refused name to `pending_items`. The Firestorm `give_item` for `9-Firestorm` uses that same `grant()`.
`thieves_den_state.gd` differs by one journal hint. `click_sprite` is unchanged.
TINT 0x680 and 0xEB8 were not entered. The port's `tint_sprite` lists `set_flag` before `give_item`. That list was not checked against the DLL.
HINTBOOK lines 2406–2407 trade the Power Orb at the armorer for Great Sword Firestorm. Lines 5682–5683 say kill Kelsrick and the thief gives that sword. Those stay two sentences. A hintbook search found no Skull Key line.
BRADY lines 6729–6730, printed 157, take a Skull Key from a hook. Lines 7325–7329, printed 171, hang that key on a hook and have Muari give Firestorm after Kelsrick dies. The hook sentences and the row's shelf noun stay separate.
BRADY lines 1590–1594, printed 43, describe Poison Paint as a mix that is ingested or rubbed on a weapon. Lines 4910 and 4955, printed 115 and 116, put it in a red bowl or on a statue. Those sentences do not place the bottle in the den. Books print no "You cannot carry more."
The full-pack refusal stays the row. No printed source replaces it. No simpler build consumes the flag on a full pack while 0x680 stays unread.
Open: the unread TINT pair, the shelf noun beside Brady's hook, and the unreopened wax host.

## Receipts

- 0072 cave: The resting prop1333 neck stays closed to every player form, the beast slide and the lizard tunnel stay the two ways through, and the books print no radius, region id, or headroom.
- 0073 jungle plank: Plank210 stays a beast-only four-unit break apart from the Bacatta causeway, creature walls use bit 10, and the books print no plank id or unit count.
- 0074 item slots: Equipment slots stay the class-byte map, 0x43 stays carried only, Net of Exile stays a held weapon, and the books print no class byte.
- 0075 generic ids: Generic item:defNNN ids stay in the world scope, Act 1 keeps its placement ids, and the books print no 165.
- 0076 inventory text: Definitions with no traced use keep the known-use refusal, other unknown finds keep the old unidentified line, and the books print neither sentence.
- 0077 thieves den text: The Thieves' Den deviation file is a title and an empty table, so it states no adapter claim and no number.
- 0078 jungle den: A full pack still refuses Poison Paint and the Skull Key before the flag changes, Firestorm still waits in pending_items, and the books print no carry-limit sentence.
