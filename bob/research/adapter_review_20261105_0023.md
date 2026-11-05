# R2 adapter review, row 0023, 2026-11-05

No Godot was run. No opcode callee was entered. The idle line still names `~/opus_work/lol2_r12y` at `56812f9`. The row, `dark_halls_rix.gd`, `dark_halls_population_source.json`, `dark_halls_loot_source.json`, and the two Dark Halls prepare scripts match `~/opus_work/lol2_r15` at `f6a5aa4` byte for byte. `monastery_quest_state.gd` differs. Its MCEL line is the same test: flag 170 clear and `GV_RIX_DEAD` clear. The next unopened file is `0024-row-2026-10-21-dark-halls.md`.

## 0023 Rix

The row puts actor 57 at his source spot as a hostile melee fighter, health 200, combat base 15. Death runs group 14414 once, soul -1 and `GV_RIX_DEAD` 1, and the cellar stops showing him. E on the body gives the Plasma staff, group 14496. Talk and give stay unhosted. The row says the soul +2 branch needs owner state 0, the first-sight group sets state 1, and the original cannot save him. Status is pending.

The staged placement is position `[3242, 530, -634]`, heading 16384, health 200, behavior byte 6. The population script wakes every present creature and hunts on sight. `dark_halls.gd` does not read the behavior byte. The one Rix attack clip is selector 4, frame 5, a 100 percent hit for 15. `native_bases` for RIX stores base 15, total 30, minimum 3. That 15 is the row's number.

Group 14414 stores eleven commands. The host applies two of them: `ce00000000ff` as soul -1, clamped 0 through 10, and `c70000003001` as `GV_RIX_DEAD` 1. It applies them once. The other nine commands stay in the JSON. The MCEL room is present only while flag 170 is clear and `GV_RIX_DEAD` is clear, so the flag hides him there.

The staff grant is `030100005cce832001000000`, name `14-Plasma staff`. Take is E, within 110, facing dot at least 0.75, and only after the death flag. The same 110 is the loot-control adapter from row 0022.

Groups 14102, 14186, 14234, and 14330 stay on the `not_hosted` list. Group 14330 stores `ce0000000002`. The host reads the sibling byte `ff` as -1, so the stored `02` is the row's +2. That group is not run.

The earlier Rix reports already framed the state bytes. The constructor stores 0 at object +0x25. Predicate 206 compares that byte with 0, 207 with 1, and 208 with 2. Group 14102's kind-9 trailer is 206, and that group contains the only kind-2 index-57 opcode 16 that stores 1 (`100239000100`). Group 14234's trailer is 208, and that group contains the opcode 16 that stores 5. A store of 2 at that slot was not closed, so "he can never be saved" is ahead of those bytes. The kind-9 record is a hit whose context word includes bit 0x0040. It is not named first sight. The object in the predicate stays LIKELY. Opcode 2 arm 0x26, which opens 14102 and 14234, stays LIKELY and was not entered again.

HINTBOOK lines 2512–2517: the guest has a staff that shoots plasma bolts, a close fight is hand to hand, and the staff is a weak weapon. Those lines print no 200 and no 15.

BRADY lines 3418–3424: Rixx is possessed and attacks with the Plasma Staff. A blind spell lets him ask for help, more of that spell lets him leave, and killing him yields the staff. Lines 7341–7343 say kill him for the staff, or a Light Spell frees him. The blind sentence and the Light sentence stay two sentences. Both stay off the owner's "unsaveable" line. The owner line in the 2026-10-30 Rix report is "the quest is buged in the game, have no clue how to save rix".

No printed number replaces 15, 200, or 110. No simpler native build while the other nine death commands, the kind-9 verb, and arm 0x26 stay unread. The melee hit and the unhosted talk stay the row.

## Still open

Whether byte +0x25 is ever 2. Which player verb sets kind-9 bit 0x0040. The plasma bolt. The nine unread commands in group 14414.
