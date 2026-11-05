# R6 improvement ideas, 2026-11-02

Classic stays the original game. Ideas marked ENHANCED change comfort or tooling and stay off the classic rules. No Godot. No DOSBox. Nothing here authorizes an adapter.

## Tooling, from this lane's own misses

1. Board appends should keep a question only when the line starts with `[2026-11-02T` and contains `astra -> grok`, `astra -> grok/lead`, or `astra -> lead/grok`, and the compare should use the full stamp `ln[1:27]`. A shorter prefix compare treats a longer fractional stamp as newer and has already aborted an append before any write.

2. A deviation census should search `\bprima\b`, `\bbrady\b`, and `\bhintbook\b`, and a second pattern for the word jammed against a digit (`Prima86`). A substring search counts `primary` as Prima. `0153` is that false hit.

3. An F10 schema check should compare the area field with the camera node. Report `12-31-30` stores area Jungle and camera `/root/DragonLevel/...`. The lead already triaged it as L9. The check would flag the label.

4. Deviation titles should not rename an unread callee. `0207` titles opcode 9 arm 3 "link". The entered item13 report left the bit-set continuation UNKNOWN, and this lane did not re-enter `0xB49EC`. A review note is enough until that entry exists.

## Tests that match reports already owned

5. ITEMS-HALF2-PICKUP is the lead's row. A standing test at native (−2432.27, 145.66) on the r12x Darker Jungle scene would have caught "cant pick up the eggs". The nearest egg marker, row 20 at (−2374, −137), is 288.6 units away, so the test belongs at the report point.

6. JUNGLE-BACATTA is already queued. A tavern talk at native (−1863.87, −4906.14) that expects the non-hostile branch would have caught the 12-22-02 report. PT-L8-HULINE-SPEECH is Astra's later row for the cat-guy silence at (−3982.58, 1142.37).

## ENHANCED

7. ENHANCED. The compiled fan note's inventory complaint (few slots, little stacking) is a comfort change. Classic slot limits stay.

8. ENHANCED. Wayfarer's Arts already carries where-next clues, as `ORIGINAL_BUGS_TO_FIX.md` records. A second hint system would duplicate it. Classic puzzles stay as printed.

9. ENHANCED. The same fan note asks for wider screen and cutscene fixes. Those are presentation. Classic framing stays.

## ENHANCED, task 20

Classic stays the original game. These three are comfort, from owner F10 notes that are not in a TRIAGE file. They do not change classic rules.

10. ENHANCED. Museum walk and run felt slow (2026-10-24T17-37-45). A speed option would be a comfort setting. Classic movement stays the original.

11. ENHANCED. Cave torch flames were asked to grow and dim (2026-10-30T09-12-24). A flicker pass is presentation. Classic light levels stay the original shade table.

12. ENHANCED. One Cave note asked for more scattering bugs (2026-10-24T17-32-32). Extra ambient insects would be dressing. Classic spawns stay the placed actors.

## Left alone

Longplay times already written in 31 deviation rows were not re-timed. Videos were not opened. Spark damage, crouch size, and bowl index stay unread, so none of them becomes an idea.

## 2026-11-05, after list K

13. A done-line search must look for ` grok] K10 DONE`, with the space before grok. The stamp sits inside the same brackets, so `[grok] K10 DONE` matches neither a grok line nor, by itself, the Kimi line that already says `K10 DONE`. The K05 append check used the bracket form and treated a successful write as a miss.

14. An earned test that calls `get_node` should fail when the area map does not attach that node. `l16_fountain_ball_earned_test.gd` still asks for `L16FountainBall` while `act2_map.gd` never adds it, and the test header still breaks prop 602. K06 is that break. The check is the node's name against the map's attach list.

15. ENHANCED. The twenty-four Luther lines in `K09_journal_hints.md` are the journal adapter, which Classic does not have. They stay off classic rules. The five Larkhon notes already in the adapter are not part of this idea.
