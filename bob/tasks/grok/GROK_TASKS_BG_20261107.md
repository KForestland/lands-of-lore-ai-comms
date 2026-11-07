# GROK list BG (lead: Opus), 2026-11-07 — fix-ups before the lead applies BF01-BF07 (Kimi K34: grok_research/kimi_K34.md).
Paste only after the owner's playthrough session (no window switching while his game runs). Re-issue as ACT3P2/ (one stacked
series on act3-chain 373b5d7 + ORDER.md), RUN the tests.
BG01 Ledger: after adding the row pieces, run tools/build_deviations.py build and include the rendered docs/DEVIATIONS.md
     (--check must PASS after the series).
BG02 BF03 mother — OWNER 2026-11-07: the player does not kill her (curse expelled into her), but she DIES after birthing
     Belial; the spiders/monsters of that area are not seen again for the rest of the game. Make the mother die after the
     birth beat (scripted), remove the area's creatures afterwards (persist over save), and build the MotherBody/DemonWave/
     BirthDoor boxes only on L20_BB (not on the L19 instance).
BG03 BF06 beast wall: the Luther step must fire only on the beast-wall arrival (selector/region of that arrival + proximity),
     not on any first L19 entry.
BG04 BF01 ending: pace the beats in seconds (chasm -> vow -> slump -> Dawn -> Draracle -> vanish), place a chasm prop, set a
     game_finished flag that survives save/load, and show an end screen (credits stub) after the last card.
BG05 Then the owner's r17 playtest fixes from AI_COMMS/playtest_feedback_20261023/TRIAGE_20261107.md (Cave crates can't be
     pushed; the door before the Draracle) and any further rows the lead adds there.
"[grok] BG<NN> DONE patch <file>" board line each.
