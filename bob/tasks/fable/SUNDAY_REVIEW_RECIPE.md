# Sunday auto review: recipe (lead, written 2026-11-12)

The owner, 12 November: "we will do a review next sunday of how this went, do an auto review on sunday like we did here today." First one: **Sunday 15 November 2026**. The lead runs it without being asked. If the lead's session was restarted and the timer is gone, run it anyway on Sunday when you read this.

Model: `fable_lane/review_20261112/` (three rounds, replies in files, a final write-up).

## 1. Gather the facts first (no questions yet)
- The plan: `fable_lane/LEAD_PLAN_A_TO_Z_20261112.md`. Where is milestone M1 (the Cemetery passes)?
- The board since 12 November: every READY, every review verdict, every STOP.
- `AI_COMMS/status/STATUS.md`: levels ready for the owner.
- Robot reports under `AI_COMMS/robot/`.
- Owner playtests in the week: F10 bundles and what they found.
- The four numbers: stops per owner walk; days (or hours) from READY to merged; share of work redone (review rounds that sent work back); robot stops found before the owner.
- Usage: ask the owner for the three usage screenshots, or read Grok's with `/usage` at an idle moment.

## 2. Round 1 questions to Grok, Sol and Opus (each at most 400 words, no code, reply files in `fable_lane/review_20261115/`)
1. What did you finish this week that a player can see? What did you finish that only we can see?
2. Your three biggest time losses, rough hours, what would have prevented each.
3. Did the lead's rules help or hinder: READY with a starting state and an input-caused change; red-then-green; two-hour research box; review within the hour; long queues? Name one to drop and one to add.
4. Where did you wait, and for whom?
5. What should the lead do differently?
6. What is the biggest risk to M1 and to "start to end" that nobody is working on?

## 3. Rounds 2 and 3 (only if needed, at most three rounds in all)
Put the disagreements and the proposed changes to all three; ask for objections; settle.

## 4. Write `fable_lane/review_20261115/REVIEW_FINAL.md`
- The four numbers, against last week's.
- Milestone status and whether the dates in the plan still hold; move them honestly if not.
- What worked; what cost time; the changes to rules and to the plan.
- Decisions for the owner, each with a recommendation.
- What was not confirmed.
Then: one board line; update the plan file and the public roadmap text if dates or percentages moved (Opus publishes to GitHub); a short report to the owner.

## 5. Standing notes from the owner (12 November)
- The lead gives the owner playtests when it suits the work or when the lead needs them; he has limited time, so each one is one level, about 30 minutes, with a try-list, robot first.
- More testers may come later; write job sheets so that someone who is not the owner could follow them.

## 6. Added 15 November 2026 (the owner caught this)
- The lanes are ALWAYS asked, even in a light week: at least one round (section 2's questions, plus "what did the lead get wrong", one out-of-the-box idea, one idea that makes the game better for a player). The lead does not write the final alone. If the lanes are busy with the owner's stops, the round is asked "at a natural break" with a deadline, and the final waits for it.
- A lane that does not read its queue within two hours gets its review items reassigned; note it in the review as a time loss.

## 7. Next review: SATURDAY 21 November 2026 (owner, 17 Nov)
The owner's words: "we need to do some changes here from savage jungle to temple, I think the workarounds are getting out of hand, so Act 2 is too big to get at once, and since the return from Claw creates complications we need to reassess. And items need to be more understood."
Themes to prepare BEFORE Saturday (facts, no decisions):
1. A WORKAROUND LEDGER for Act 2 (Savage/Darker Jungle L8 -> Claw L12 -> Citadel L13 -> back -> Temple L14): every DEVIATIONS row, adapter, hint line and fence added since 12 Nov, per level, with why it was added and what the original does there if known. Count per level.
2. ACT 2 IN PIECES: a proposal for cutting Act 2 into pieces that can each be understood, built, walked by the robot and played by the owner on their own (and in which order), instead of the whole act at once.
3. THE RETURN FROM THE CLAW MOUNTAINS: what differs between the way up and the way back (routes, state, what the fall recovery hid), and what it costs to do both properly.
4. ITEMS: one page a player could read - what each item class does today, where each quest item comes from and where it is used (the paint recipe, aloe, Silverleaf, the bows, the Dreamstone, orbs), what is unknown.
The lanes are asked their round as always (section 6).
5. (added 17 Nov, owner) THE TEMPLE MAP: "figure out temple, we need to redraw the map so no more overlapping." Prepare facts: what overlaps in L14 today (rooms stacked, ceilings walked on, the 318 withheld walls, the moved zones), what a redraw would mean (which rooms move where, what the original connections are, what it costs in geometry, collision, objects, chains and tests), and the alternative already in work (walls + ceilings from below only) with what it does and does not cure. Opus's L14 census and ceilings reports are the starting material. No Temple redraw work before Saturday.
6. THE BELT (owner, 17 Nov, after playing r19p): "The belt is great, works fantastic; some small alterations and it will be great." Collect his alterations.
