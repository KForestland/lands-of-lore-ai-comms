# R2 adapter review, rows 0207–0222, 2026-11-05

No Godot was run. No opcode callee was entered. LOLG.DAT was not opened. The longplay was not opened. r15 is `f6a5aa4`. r12y is `56812f9`. Fifteen of these deviation files match r12y. `0222-row-2026-11-02-tower-alcoves-fields.md` differs. This pass did not post a board line.

`adapter_review_20261104.md` slice 6 and slice 3, and `adapter_review_20261102.md`, stay as written. Counts the rows give stay the rows, except the host id ranges counted under 0215 and 0218.

## 0207 L8 activation

Slot 0, opcode 9 arm 3, and kind-4 mode 1 stay the row's PROVEN stores. An unknown `+0xA8` still uses the 0175 gate, adapter `opcode13_actor_a8`. `0xAF0E0`, `0xB4130`, and `0x5C9D0` stay unstaged.

DECODED. `native_script_host.gd` lines 1102–1127 write command byte 5 at `+0xA8` and `+0xA9`, OR 1 into `+0xB8`, and store 0 at word `+0x7C`, and return before those stores when `+0xA8` is `0x0F`. Lines 1446–1463 store 0 at `+0x0C`, clear bit `0x10`, OR 1 into `+0x16`, and OR `0x20` into `+0x17` when that bit is set, and write nothing when it is clear. An unstaged bit uses placement word `+8`. Lines 730–744 accept kind-4 mode 1 when `arg_c` is nonzero, and byte `+5` inverts that. `tests/l8_activation_test.gd` lines 38–40, 48, 56, and 73 pin those stores. `act2_creatures.gd` lines 45–49 set the population present boolean from bit `+0x16`. The host and the test match r12y. `act2_creatures.gd` differs in later functions and does not replace this link.

Books print no slot 0 and no arm 3. The stores stay.

## 0208 L8 first departure

The summary notices and the discrete actions stay modern. They do not quote dialogue and they do not time the scene.

HINTBOOK. Lines 2916–2924 say give the knife to Daniel, watch him drop it when the hoppers arrive, and pick it up. Lines 2934–2938 say the first temple visit is a scene and a creature snatches the priest. Lines 2979–2983 say show Daniel's gift to the guard. Lines 2997–2999 say hand the gift over in the left treehouse. Those sentences print no timing.

`l8_journey_state.gd` matches r12y. Lines 33–70 are the gift, interruption, recovery, temple, guard, and shaman transactions. `l8_journey.gd` lines 153–161 and 174–175 are the first-visit buttons. That file differs by later Silverleaf buttons. Those buttons are not this row. The notices stay.

## 0209 L8 encounter binding

Reach 160, the layer-1 ray, the summary panel, and the instant disappearance stay modern.

DECODED for the host anchors. `l8_journey.gd` lines 6–7 and 37–49 use reach 160 and a layer-1 ray. Lines 98–111 clear actors 81, 92, and 93 once the gift is dropped, and spawn guard 113 after the temple visit. The file differs. Those lines are the r15 text. The first-visit panels stay.

HINTBOOK lines 2920–2921 name the flight. They print no panel and no 160. The panels stay.

## 0210 charged globe identities

The charged id stays the original placement id plus `:charged:` and yellow, white, or blue. Charging on insert stays synchronous. The occupied output stays until retrieve.

`act2_charger_state.gd` lines 21–22 and 36–46. The file differs. An insert now refuses a definition that `item_handlers.gd` does not host. That check does not replace the synchronous commit.

HINTBOOK lines 3220–3222 say open the doors with a globe charged gold, blue, or white. Lines 3317–3319 say place the globe in the claws, wait a few seconds, and click it back. BRADY lines 7852–7866, marker PDF PAGE 190 = PRINTED PAGE 189, say charge spheres at colored altars and name the white, yellow, and blue places. BRADY lines 8385–8406, marker PDF PAGE 208 = PRINTED PAGE 207, say find the white altar and click a globe on the yellow claw altar. The markers PDF PAGE 181 = PRINTED PAGE 180 and PDF PAGE 186 = PRINTED PAGE 185 have no altar sentence. Gold and yellow stay separate names. None of those sentences prints 140 or a synchronous instant. The transaction stays.

## 0211 charger production binding

The three source anchors, reach 140, facing 0.8, the first carried empty globe, the 8-unit lift, and the radius-7 sphere stay the modern interaction.

`act2_chargers.gd` matches r12y. Lines 5 and 21–28 are the anchors, the radius-7 sphere, and the 8-unit lift. Lines 38–44 and 66–75 are reach 140, facing 0.8, and definition 98.

BRADY printed page 189 names the three altar places and prints no coordinate. The reach stays.

## 0212 herbalist first visit

The summary menu stays the replacement for the jar hotspots. Two items from each jar stay the row.

`l8_herbalist.gd` matches r12y. Lines 3–8 and 27–34 give two ids each for sap, amber, and aloe, at definition indexes 111, 112, and 110. The row's source names `109-Ironwod sap`, `110-Amber`, and `108-Cave aloe` stay the row. This pass did not relabel those indexes. `l8_journey.gd` lines 172–173 offer the three menu lines.

HINTBOOK lines 2991–2992 say the herbalist does not mind if Luther picks up several items among her jars. Those lines do not print two. The menu stays.

## 0213 cemetery sigil gate

The sigil stays in inventory. The outward slide along X stays the row's inference.

`l10_main_gate.gd` matches r12y. Lines 4–5, 37–46, and 55–61 are the aim, reach 140, facing 0.8, the retained sigil, and the X slide by the source extent.

HINTBOOK lines 3256–3258 say the key the Huline shaman gave Luther opens the gate. They do not say the key is consumed. The chapter title is Dracoid Cemetery.

BRADY line 4141, marker PDF PAGE 101 = PRINTED PAGE 100, says place the sigil in the lock and the gates open. Line 7549, marker PDF PAGE 179 = PRINTED PAGE 178, says the shaman gives a key to enter the Dracoid Cemetery. Line 7789, marker PDF PAGE 188 = PRINTED PAGE 187, says open the main gate with a Dracoid Sigil from the Wild One Shaman. Line 8397, marker PDF PAGE 208 = PRINTED PAGE 207, says use the sigil to open the gate and go inside. Line 4383, marker PDF PAGE 105 = PRINTED PAGE 104, spells Cemetary. That spelling stays off the Dracoid Cemetery sentences. The five sentences stay unmerged. Consumption stays unstated. The retain and the X slide stay.

## 0214 shaman backroom voices

Voices 225 through 235, then 236, then 237, stay the order. Eleven initial clips stay the row. Audio-only playback and the saved index stay the presentation.

`l8_backroom.gd` matches r12y. Lines 5 and 34–65 are those three sequences and the line advance. `l8_journey.gd` line 72 says Enter skips a line.

HINTBOOK line 2996 is the click on the doorway. It prints no clip number. The clips stay untranscribed. The pictures stay unhosted.

## 0215 tomb globe doors

The shared offer, the one-time consume, reach 140, facing 0.8, and the instant rise of 110 stay modern.

`l10_tomb_state.gd` matches r12y. Line 6 lists the joins. This pass counted 13 keys, the row's thirteen. `l10_tombs.gd` differs at lines 27–28. Receptacle 154 aims at the box center. The other aims stay height plus 45. Lines 67–76 and 91–100 are the 110 rise, reach 140, facing 0.8, and the first matching carried globe.

HINTBOOK lines 3220–3227 and 3267–3268 say a charged globe of the proper color opens the doors, gold first, and name the sword globes as the wrong globes. Lines 3458–3463 say place each colored globe in its colored box. They print no 140 and no 110. The motion stays.

## 0216 cemetery stacked blockers

L10 blocker walls begin at the source floor. A buried wall ends at the source ceiling. Other levels keep the prior pad.

`region_blockers.gd` differs for L8 region 2417. That change is not this row. Lines 14 and 202–203 still default the pad to 64 below the floor and 1024 above the ceiling. Lines 238–243 set L10 footroom to 0, and headroom to 0 when the ceiling is below 0.

Books print no pad. The L10 cut stays.

## 0217 Act 2 Spark transport

Act 2 scene paths and source actor ids stay the aura whitelist. The existing Spark damage rules stay. The level-3 request amounts stay out of that path.

`player_spark_aura_state.gd` matches r12y. Lines 8–9 and 55 name the Act 2 scenes and refuse an area outside that list. Finished HP, range, and selected mana stay unread.

Books print no scene path. The whitelist stays.

## 0218 catacomb braziers

E, reach 140, facing 0.8, no item cost, and the shared 10 fps loop stay modern. Spark does not replace E.

`l10_braziers.gd` matches r12y. Lines 12–15, 37–43, 54–63, and 71 are the id test, the 64 by 86 quad, reach 140, facing 0.8, and the 10 fps frame. The id test is 153, 200 through 241, and 336 through 339. That is the row's 47.

HINTBOOK lines 3294–3295 say light the big braziers scattered everywhere. Lines 3429–3431 say lighting the braziers makes departure easier. Neither names E or Spark. BRADY line 3267, marker PDF PAGE 82 = PRINTED PAGE 81, says use a Spark spell to ignite the brazier in the wall. That sentence is the boulder hallway. It stays off these catacombs. The E adapter stays.

## 0219 earned route configuration

Carrying `adapter_exit_seeds` stays the correction. A false option leaves the destination gate unresolved. The preview defaults stay available.

`act2_progression.gd` differs in later passage checks. Lines 196–213 are the same seed table, including L8 local 13 and L9 control 82, and they return when the option is not true. `act2_map.gd` line 23 still exports the option true. That file differs for later owners.

Books print no seed. The option stays.

## 0220 ruins magic bridge

The immediate selector-7 raise, the 26 by 57 by 12 receiver, and the saved flag stay modern. The printed spark sentence does not replace them.

`l9_magic_bridge.gd` matches r12y. Lines 4, 23, and 35–44 are the aim `(-1193, 28, -1943)`, the box, and selector 7. The row's prop height stays h0.

HINTBOOK lines 3676–3679 say use a spark spell on the black orb on a pedestal and a bridge appears. The row keeps the template name Green Drac Orb and calls the staged selector-0 image dark. That sentence prints no selector 7 and no 26. The immediate raise stays.

## 0221 Silverleaf use

Plus 5 stays the Brady amount. A living human, an open inventory, and a full-mana refusal stay the modern admission.

`player_item_controller.gd` differs for the serum refusal. Lines 42–44 refuse a non-human form and a closed inventory. Lines 97–105 add 5 and return without spending at full mana. `item_catalog.gd` line 202 still marks definition 117 as Silverleaf and cites Brady printed 41. That file differs by serum 119. Handler 39 was not entered.

BRADY lines 1541–1542, marker PDF PAGE 42 = PRINTED PAGE 41, say Silverleaf gives you 5 Magic Points. HINTBOOK lines 1270–1271 are mix recipes. They print no 5. Those recipes stay off this use. The +5 stays. The admission stays.

## 0222 tower alcoves and fields

r12y says opcode 18's reader is UNKNOWN. It says treating words `+4`, `+6`, and `+8` as coordinates and `+12` as heading is a narrow modern adapter, not arrival selector 4.

The r15 row says flags `0x0804` and `0x0C04` select native direct relocation. It says signed `+4` and `+6` are horizontal, `+12` is heading, and a clear bit `0x0100` means `+8` is not a height. Floor plus 32 stays a host adapter, not selector 4.

LIKELY for that word split. `l9_tower_source.json` matches r12y. Lines 17–38 hold the row's pairs `(-3321, 1187)` and `(-2891, 1142)`, flags `0x0804` and `0x0C04`, and headings 57344 and 23665. The stored landing y is 32. Line 4 still says the operand interpretation is not decoded. `opcode18_b27a3534.md` says the flag table, including `0x0100`, was not re-proven one flag at a time. This pass did not enter the opcode body.

`l9_tower.gd` differs. Lines 92–106 still move the player to that landing, set the heading, and wait 0.5 s. Lines 57–65 give the green mesh its own node and zero footroom and headroom on the owned edges. That split does not replace the walk-in.

HINTBOOK lines 3687–3693 say enter the shadowy alcove, then light two globes, one for the green force field and one for a basement stair. BRADY lines 8371–8372 and 8381–8383, printed page 207, say spark an orb to lower the green force field and spark an orb to lower stairs. Those spark sentences stay off the walk-in. No printed coordinate replaces the landing. The 0.5 s debounce and the saved orb ids stay adapters.

The r12y UNKNOWN-reader sentence does not stay. The r15 row is the replacement. Floor plus 32 still stays a host adapter.

## Grade

DECODED for the 0207 stores, the matching hosts, the L10 blocker cut, and the thirteen tomb keys. HINTBOOK for lines 2916–2924, 2934–2938, 2979–2983, 2991–2999, 3220–3227, 3256–3258, 3267–3268, 3294–3295, 3317–3319, 3429–3431, 3458–3463, 3676–3679, and 3687–3693. BRADY for printed pages 41, 81, 100, 104, 178, 187, 189, and 207. LIKELY for the 0222 word split. The longplay was not opened.

No printed number replaces reach 140, facing 0.8, the two-from-each-jar menu, the retained sigil, the E brazier, the full-mana refusal, or floor plus 32. No simpler native build replaces these adapters.

## Still open

The three unstaged arm-3 callees, the unnamed kind-4 dword, the herbalist definition labels, handler 39, the opcode-18 flag table, native charger timing, native gate motion, the backroom pictures, and the rendered routes the rows leave unqualified stay unread.
