# Lands of Lore — Master Plan

Owner: Kjetil (KForestland). Updated: 2026-11-05.
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

## LoL2 Classic: phases and status (2026-11-06)

Order (owner, 2026-11-06): **maps → the main quest chain complete A to Z → then refine until the full game** (edge
cases, scene order, puzzle nuance, items, RPG, dialog, sound). Refinement does not start before the chain is complete.
A passing test is not a cleared area: only the owner's playtest clears one. Quality comes before speed; estimates are
for orientation.

| Area | Done | Notes |
|---|---|---|
| Maps / world | ~93% | Every Brady/Prima map point in 14 areas checked against the original data and the longplay: nothing the original shows is missing. "Draw only what can be seen through doorways" (like the original engine) fixed most clipping; owner: Huline Jungle "much better" (r16). Open: the Huline Temple interior (parked for the next builder lane), L8 ladder/tree bridge/platform and Museum crouch/niche in the next build |
| Act 1 | ~92% | Playable start to finish, certified as one campaign chain. Owner playtests r14/r16 confirmed escort, routes, drowning, voices |
| Act 2 story | ~75% | Steps 7–65 built and tested; owner r16 playtest found the first Huline Temple scene must trigger by walking in (book), not by a button: fix in the next build |
| Act 3 story | ~25% | 4 of 28 steps built; all 28 drafted as one save chain from the greenhouse to the final scene, under review and test |
| Good/evil branches | drafted | All branches drafted with both outcomes, under review |
| Items | ~25% | All 170 original items placed and carriable; effects hosted one by one; Luther's book (Items/Creatures/Characters/Lore) data generated |
| Creatures / combat / spells / RPG | ~10% | Act 1 combat works; creature/spell tables collected |
| NPCs / dialog | ~20% | Act 1 conversations, first Act 2 encounters |
| Sound / music | ~20% | Act 1 mostly |
| Polish / Enhanced | ~5% | Plan approved (below) |

Overall LoL2 Classic: **about 60%**. Latest playtest build: r16 (2026-11-06).

Other projects:
- **LoL1 Classic in Godot**: a full draft of the game in nine chunks (save/load, hero select, combat, opening, the keep
  to the burned nests, the mine, the White Tower and Cimmeria to the ending, sound) exists; ten draft tests pass in the
  research lane's run. Lead review and owner playtests come after LoL2's chain.
- **LoL3 Classic**: research done (walkthroughs per guild path, story cards, known bugs and patches, longplay index, a
  first build plan); texture colour decoding is the main open blocker.

Rough timeline (orientation only; depends on AI usage limits and playtests):
- Next playtest build r17: about 1–2 days (L8 ladder/tree bridge/platform, the first Huline Temple scene on walk-in, drowning
  feedback, Atlas improvements, the first Act 3 chain pieces).
- Classic playable A to Z (every story step, start to end): mid-December 2026.
- Classic with all systems (items, creatures, spells, RPG, dialog, sound): February–March 2027.
- Enhanced editions (gray box first, then art): after LoL1 and LoL3 Classic, see the order of work above.

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
