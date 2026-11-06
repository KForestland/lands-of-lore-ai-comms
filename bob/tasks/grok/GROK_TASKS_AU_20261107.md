# GROK task list AU (lead: Opus), 2026-11-07 — Act 2 MAIN CHAIN, the triggers (owner order: maps + main chain first).
The L8 temple showed the pattern: the original fires a scene on walk-in, our port asked for E at one point, the owner
walked past and the chain stopped. Find every other place like that in Act 2 before the owner does.
Owner's own Act 2 sequence (2026-11-06): knife to Daniel -> (temple scene) -> village -> return the knife -> Dracoid key ->
cemetery, explore -> Dracoid ruins -> return to wake the emperor -> silverleaf -> gladiator fight -> the things for the
Claw Mountains; the Huline Temple itself later needs a dream stone/orb and plays an animation.
Base: lol2_act3 stack-ah01 + your AS fixes. Patches, do not apply. Same rules; RUN the tests.

AU01 One table grok_research/AU01_act2_triggers.md, every Act 2 main-chain step (STORY 7-65): original trigger (walk-in /
     click / E / dialog / item use) with its source (native record, hintbook line, longplay frame) | our trigger (script) |
     match? | can a player miss it? Mark every mismatch where the player can walk past the step.
AU02 Patch the mismatches that can stop the chain (walk-in scenes, missing movies, auto dialog), each with an earned walk
     from the previous chain save that does NOT press E where the original does not need it.
AU03 AS01 follow-up: the first temple visit should play the priest scene. Find its native movie (or the scene records) and
     play it on walk-in; if no movie exists, say what the original shows (longplay frame) and log the adapter.
"[grok] AU<NN> DONE <file>" board line each. Owner F10 reports first.
