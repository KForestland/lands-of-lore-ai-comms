# GROK task list K — quest chains A to Z from the guides (owner order: maps -> QUEST CHAINS -> Act 3), lead: Opus

Read-only, no Godot. Output grok_research/K<NN>_<slug>.md, "[grok] K<NN> DONE" board line each, status/grok.md current.
New owner F10 reports go first. For every step: guide lines (Prima hintbook.txt / brady_guide.txt), what the player
does, the hosting code in ~/opus_work/lol2_act3 (scripts/lol2/*.gd) and the earned test that walks it
(tests/*_earned_test.gd), and a verdict: HOSTED+TESTED / HOSTED-UNTESTED / MISSING / BROKEN (why). A MISSING or BROKEN
row gets a short fix spec (native ids, adapter idea). Owner's real blocker: at the Larkhon without the serum because he
was never admitted to the tribe (TRIAGE_20261104.md) - the chain must be findable for a player who does not know it.

K01 Act 2 chain part 1: arriving in the Savage Jungle (L8) -> Daniel's gift -> temple first visit -> village admission
    -> shaman -> cemetery quest. Include every journal hint a lost player would see.
K02 Act 2 part 2: Cemetery (L10) -> Dracoid Ruins (L9) -> urn/ashes/ankh -> Emperor's tomb -> statue/worm -> flood escape.
K03 Act 2 part 3: back in L8 -> silverleaf -> initiation fight -> serum -> vapors -> Larkhon -> Claw Mountains (L12).
K04 Act 2 part 4: Claw Mountains -> Ruloi Citadel (L13) -> Dreamstone -> Temple entry (L14).
K05 Act 2 part 5: Huline Temple (L14) start to the Chamber of Voices (the lead built STORY-066 Chamber -> L16).
K06 Act 3: L16 city steps STORY-068..078 vs the lead's act3-story branch (066/067/070 built; 068 ball = your H22 prop 210).
K07 Finale STORY-079..093: what exists in code today (probably nothing) and the order to build it.
K08 Every point in K01-K07 where the player can get STUCK or lose a required item (softlock list), with the original's
    own remedy if any (owner rule: original softlocks are fixed in both editions).
K09 Journal hint coverage: for each required step, does My Journal have a vague in-character hint when the player is
    stuck there? List the missing ones with a proposed <=130-char Luther line.
K10 Portal visibility candidates from your J11 audit: the top 5 areas where the lead should turn region_visibility on next,
    with one owner report or longplay frame each.
K11 Then GROK_STANDING_IDLE.md loop.
