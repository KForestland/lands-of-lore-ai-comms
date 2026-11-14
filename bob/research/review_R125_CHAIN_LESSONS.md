# R125 chain lessons — HOLD

Head `de0cbb6e94beeeaa50d8161203be71a62d057536` on `sol/l19-heads-lesson-20261114`, parent r19-work `1230b9e`. Review tree `~/opus_work/lol2_grok_r125` only. Rendered, `Engine.time_scale` 1, physics 60, private display. No SCRIPT ERROR. Seventh life not started. `playtest/r19n` was not on the branch list at the verdict.

## (a) Head 67

Pin `tests/fixtures/chain_spell_lessons/sixth_life_head67.json` sha `1f6636eae4481520b47e466352efa16bb527934ee6c8f5a7797cf0aa7093a60f`. Loaded pose `(1451, -98, -1142)`, `near_head` 67, feet on the anchor (delta 0), shot empty, book without `mists1`.

The lesson sentence was the HUD for 9 frames, one run. The arrival autosave then set the HUD to `Autosaved.` for 180 frames. The sentence did not return. The book already held the Mists group, so the one-shot teacher did not write the line again. Stepping back with S could not happen first: the teacher runs on the first playable frames while the save is already inside the reach.

After that, key 4 then Q recorded 67, 69, 68, 70. Mana went 180, 179, 178, 177. E left the shot list unchanged on each head. Nothing was auto-cast. Skull 66 stayed out. F5 then F9 kept `mists1` and the four shots. Heads 69, 68 and 70 used the disclosed `stand_at` aid. Head 67 was the loaded pose. The 0.5s cast cooldown was waited out between heads.

Same life, earlier pin `sixth_life_before_heads.json` sha `ad5b66a596456d626d2213b96655596b41cb8239349f8915eb4f1ded3acf9ce5`. Disclosed stand 90 south of head 67, real look, real W. The sentence appeared once for 181 frames. Shot stayed empty. That walk is the continuous-life case. It is not the F5 load.

## (b) Eight rows

`docs/chain_spell_lessons.md` and the live queries. Each lesson fires when the player is already at the first place that cast is required. It is not taught in an earlier room. A second entrance to the same admission runs the same query.

| Cast | Lesson query | Before the first need? | Other way in |
| --- | --- | --- | --- |
| Curse1 Dampen | `L9StatueWalk.needs_shape_lesson`: fight not done, and the body is inside the fight-region polygon and floor band | At the fight, which is where Dampen is required | Another entrance to that polygon still teaches |
| Curse2 | Same query, and the row admits only form 2 | At that fight, only while Lizard. The group is also taught at the crevasse and the gutter | Human in the same region gets the Dampen row only |
| Curse3 | `L12Crevasse.needs_shape_lesson`: within 256 of the spark rock `(3052, -1050, -13628)`. Later copy `L19SewerForms.at_mouth`: flat distance to the mouth under 80, not flying, world active | At the rock, and again at the gutter mouth | A crevasse route that stays outside the 256 ball misses that copy. The gutter copy is the later required use |
| Curse5 Expel | `l19_dawn_curse.accepts_player_spell`: `curse5`, area `L20_BB`, mother not yet entered, flat reach | At the mother, which is the cast reach | Another approach still enters that reach |
| Mists1 | `needs_mists_lesson`: unfinished head in 67/69/68/70, flat reach 20, feet within 24 of that head's floor | At the head. The F5 feet are on the floor | Another door onto that floor still teaches. The cast itself checks only the flat reach, so a body more than 24 off the floor and still within flat 20 is in cast range without this lesson |
| Mists3 | Fountain `accepts_player_spell`: `mists3`, not frozen, aimed | At the optional fountain aim | The fountain is not the City exit. Skipping it skips this copy. The required Mists use is the heads |
| Prism5 | Scotia `accepts_player_spell`: `prism5`, flat reach, Trinity not set | At Scotia, which is the cast reach | Another approach still enters that reach |
| Summon3 | City `L16NwTraps.accepts_player_spell`: `summon3` and aimed at the ice ball. Armory: `summon3`, brick hacked, ball not done, aimed at source 196 | At each ball's existing aim | The city ball is optional. The armory ball still requires the brick. Another approach to an aimed ball still teaches |

## (c) Already known

Headless `tests/chain_spell_lessons_test.gd` exit 0. A complete book makes `live_candidates` return empty, the owner query count stays 0, and `save_feedback` is not called. That is the lesson line. The printed line was `PASS all eight chain casts: named production queries, optional eligibility/no global grant, numeric form admission, learned skip, pure query, pinned genuine unlearned sixth-life book`.

## Verdict

HOLD. The F5 load does not keep the lesson sentence on the HUD. The casts, the save round-trip, the walk-in sentence, and the already-known skip are in place.
