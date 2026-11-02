# Lands of Lore — Master Plan

Owner: Kjetil (KForestland). Updated: 2026-11-02.
Fan project, non-commercial. Lands of Lore is © Westwood Studios / Electronic Arts. No original game files are
distributed: the remakes read the data from the player's own copy of the games.

## Vision

Give the Lands of Lore series back to the players who loved it, and introduce it to new ones. This is a long-term
effort ("if it takes 10 years, we will do it").

1. **Classic editions** of Lands of Lore 1, 2 and 3: the original games, faithfully remade in the Godot engine.
   They keep the original look, story and behaviour, fix every original bug, and log every deviation in a public
   ledger.
2. **Enhanced editions** after that: optional modern lighting, quality-of-life features, wider outdoor maps, and
   compatibility between LoL 1–3. They add story threads from the unified *Chronicles of Time* outline and ruins from
   the age of the Ancients.
3. **New stories later**: the LoL 4–6 and Chronicles outlines in [outlines/](outlines/README.md) are design
   context for the future, not current work.

## Order of work

| Step | Game | State |
|---|---|---|
| 1 | LoL1 reverse engineering | **Done and published** ([lands-of-lore-1-re](https://github.com/KForestland/lands-of-lore-1-re)) |
| 2 | LoL2 reverse engineering | Largely done, published ([lands-of-lore-2-re](https://github.com/KForestland/lands-of-lore-2-re)) |
| 3 | **LoL2 Classic in Godot** | **In progress, main project** (details below) |
| 4 | LoL3 Classic | After LoL2 is finished |
| 5 | LoL1 Enhanced, then the other Enhanced editions | After LoL2 and LoL3 are finished |
| 6 | 3D characters/items/creatures for the Enhanced editions | Not before 1–2 years from now; LoL1 assets first |

## LoL2 Classic: phases and status (2026-11-02)

Phase order: **maps → story progression → items → RPG → dialog → small fixes**. Sound and combat polish come last.
Quality comes before speed; the estimates below are for orientation, not deadlines.

| Area | Done | Notes |
|---|---|---|
| Maps / world | ~95% | All 15 levels built and connected (exits, creatures, items placed) |
| Act 1 | ~85% | Playable start to finish; passes full automated campaign runs on every build |
| Act 2–3 story | ~35% | First Act 2 loop complete and tested in one continuous run (Savage Jungle → Dracoid Cemetery → Dracoid Ruins / Mage's Tower → flood escape → Wild Village); tribe initiation in progress |
| Items | ~25% | All 170 original items placed and carriable; effects being hosted one by one |
| Creatures / combat / spells / RPG | ~10% | Act 1 combat works; printed creature/spell tables collected |
| NPCs / dialog | ~15% | Act 1 conversations; first Act 2 encounters |
| Sound / music | ~20% | Act 1 mostly |
| Polish / Enhanced | ~5% | Ideas collected |

Rough estimate to a complete, playable LoL2 Classic with all systems: **2–3 months**, depending on AI usage limits
and playtest findings.

## How the work is done

- The owner makes the design calls and playtests every build; he does not write code.
- Several AI "lanes" share the work through this repository and a local coordination board:
  - Claude Opus is the lead and integrator.
  - Astra (OpenAI) builds the story progression.
  - Grok researches the original game and the strategy guides.
  - Claude Fable is a second builder.
- **Evidence order:** the original game's own data and scripts, then the printed guides (Prima, Brady), then the
  owner's longplay video, then the owner's memory. When a detail is hard to trace, a logged adapter that matches the
  original's visible behaviour is allowed, and every such deviation is recorded in the ledger.
- **Quality gates:** every build passes a regression suite, a scripted Act 1 campaign, an export/package check and a
  packaged smoke test before it reaches the owner's playtest launcher.

## Collaboration

We are happy to exchange findings with other Lands of Lore researchers and fan projects. See
[COLLABORATION.md](COLLABORATION.md) for what we can offer and the open questions where help is welcome.

## Credits (so far)

- Westwood Studios: the original games; Frank Klepacki: the original music.
- Amy Schmidt (landsoflore.de): the tested Rix rescue fix, used as the source for that bug fix.
- Onkel Dave: "Schon gewusst? – Lands of Lore II" fan guide, used as a reference witness.
- smgtoxa (LoL1 project) and MohammadKoush (Lore Tweaks): collaborators in this workspace.
