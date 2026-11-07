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
BG00a FIRST (owner r17): the Y02 L8 tree bridge (17-57-09) and the Y01 cache ladder (18-08-06) do NOT work in real play - their tests were probes. Redo each with an EARNED WALK that goes there as Human, uses it the player way, and crosses/climbs. Pass is not cleared.
BG00 FIRST (owner blocker 17-53-55): at the L8 village tree without the temple visit, make the guard (or a clear on-screen line) say to visit the Huline Temple first (east of the entry, far side of the map); earned test from gift=recovered/temple_visited=false. Then BG01..
BG05 Then the owner's r17 playtest fixes from AI_COMMS/playtest_feedback_20261023/TRIAGE_20261107.md (Cave crates can't be
     pushed; the door before the Draracle) and any further rows the lead adds there.
"[grok] BG<NN> DONE patch <file>" board line each.

OWNER 2026-11-07 (meta duck, overrides the AV04 approach): solve underwater/drowning on the PLAYER side, not in the world.
BG06 Underwater view: when the camera is below a water surface (liquid_drowning regions), apply a blue-green screen tint + fog
     (hides open sides; NO skirt walls) + muffled sound. Drowning: keep the rising veil (AS02), add a slow sink of Luther while
     the clock runs and a slide-down on death (not a drop). The only world change: the missing water SURFACE at the r16 stream
     bed (region 2559), limited to that region, real water material (not a grey fallback). Capture test of both r16 spots + a
     check that no other water region changed. Ledger rows.
