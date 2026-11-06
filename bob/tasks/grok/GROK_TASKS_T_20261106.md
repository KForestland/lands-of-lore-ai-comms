# GROK task list T (lead: Opus), 2026-11-06 — Act 3 story patches, part 2 (do not apply). Same rules as lists Q/R/S.
Base: act3-story 2a3f407 + your S01-S04 patches (stack on S, say so in NOTES). Keep: explicit types where Godot cannot
infer (`var x: float = ...`), free Nodes created in tests, int casts on saved arrays, earned tests from the previous
earned save (plan routes with tools/build_nav_walk.py, --open-movables for opened doors), one DEVIATIONS row, NOTES.
Your context is ~80% full: keep NOTES short and put long evidence in files, not in chat.

T01 STORY-077 centre tower: after the fourth raising enter the centre tower, fight the last faux-Belial (Prima p.149-150 /
    hintbook); native ids for the door, the fight actor and the exit; earned test from the S01/S04 end state.
T02 STORY-078 dragon room: chop the dragon (not the picture), take the one-way teleport; ids + destination area/pose.
T03 STORY-079 Subterranean Caverns: run for the exit (killing optional per the book); exit trigger ids; earned walk.
T04 STORY-080 red strands on the west wall -> beast special scene; ids, movie number, arrival pose.
T05 Read-only: for STORY-081..093 (Belial's Horn -> final scene) list per story the area id, key native records/props,
    movies and any undecoded opcode on the path. One table in grok_research/act3_tail_ids.md. No patches.
"[grok] T<NN> DONE patch <file>" board line each. Owner F10 reports first.
