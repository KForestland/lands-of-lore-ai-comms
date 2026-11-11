# Lands of Lore — Master Plan

Owner: Kevin (KForestland). Updated: 2026-11-11.
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
| 2 | LoL2 reverse engineering | **Almost fully understood** (2026-11-06), published ([lands-of-lore-2-re](https://github.com/KForestland/lands-of-lore-2-re), [November summary](https://github.com/KForestland/lands-of-lore-2-re/blob/main/docs/lol2-understanding-2026-11.md)) |
| 3 | **LoL2 Classic in Godot** | **In progress, main project** (details below) |
| 4 | LoL3 Classic | After LoL2 is finished |
| 5 | LoL1 Enhanced, then the other Enhanced editions | After LoL2 and LoL3 are finished |
| 6 | 3D characters/items/creatures for the Enhanced editions | Not before 1–2 years from now; LoL1 assets first |

## LoL2 Classic: status (2026-11-11)

Full roadmap with the eight phases, what each needs, and where help is welcome: **[LOL2_ROADMAP.md](LOL2_ROADMAP.md)**.

- **About 20% complete (give or take five points).** Earlier versions of this page said about 60%. That number counted
  pieces that were built; the new one measures what a player can actually do, against all the work still planned
  (137 tasks, 74 to 130 agent-weeks). The world and the main quest are far along; combat, items, spells, dialog, music
  and the game's menus are the larger share and have barely started.
- **Act 1** is playable start to finish. **Act 2** is built to the Claw Mountains and was walked there with real input,
  but not yet without help; Kevin's latest playtest stopped in the Dracoid Cemetery. **Act 3** is partly built.
- **When:** most likely **July 2027**; earliest late April 2027; August 2027 or later if the big unknowns go badly.
  These are estimates, not promises.
- **Next checkpoint:** mid-December 2026, a player finishes the main quest from New Game to the ending.

Order (owner): maps, then the main quest from A to Z, then everything else; classic first, modernised only where the
original is too hard to rebuild, and every difference is logged. A passing test is not a cleared area: only Kevin's
playtest clears one.

Other projects:
- **LoL1 Classic in Godot**: a full draft exists; lead review and owner playtests come after LoL2's main quest.
- **LoL3 Classic**: research done; texture colour decoding is the main open blocker.
- **Enhanced editions**: after the Classic editions (see the order of work above).

### Future workflow for the Enhanced editions (approved 2026-11-05; starts after LoL3 Classic)

One story, one save, one quest logic for every edition. Tools ("pipes") run on all levels at once:
1. Gray-box generator: decoded level geometry → simple box levels.
2. Box people: every quest character/creature/prop as a labelled box with the same id.
3. Quest walk: the existing automated walk tests run on the gray box too, proving the chain end to end.
4. Art import: AI-generated 3D models replace gray boxes by id with one import rule.
5. Owner playtests stay the final check.
Then refine → test → refine, level by level: textures, tessellation, lighting, and sightlines that show places and
hidden areas so the hint system can be lighter. Rules and tools evolve by iteration on what works.

## How the work is done

- The owner makes the design calls and playtests every build; he does not write code.
- Several AI "lanes" share the work through this repository and a local coordination board:
  - Claude Opus is the lead and integrator.
  - An OpenAI Codex lane builds the story progression (moving from Astra 6 to Sol 6.2; back ~2026-11-08).
  - Grok researches the original game and the strategy guides.
  - Claude Fable is a second builder.
  - Kimi runs small verification tasks on a timer: it checks other lanes' claims against the data.
- **How and why this works, and what went wrong before:** see [METHOD.md](METHOD.md).
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
