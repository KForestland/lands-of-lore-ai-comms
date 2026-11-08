# BG22 Jungle tree top

Owner r17 17-02-01 at Jungle (307, -4290), body height 32, pitch 0.306, yaw 1.663. The note was "the tree missing top of the tree". The frame is a bare trunk in the middle of crowned palms.

Face 8631 is not this tree. It is the unbound span at (−788, −5139) to (−541, −5248), about 1300 units away, already skipped by TREE_TOP_SKIP. That skip stays.

DECODED. The trunk in the shot is prop record 5211 at (111, 0, −4261), dead ahead. It is one of the 53 template-22 placements. Template 22 is `verytall`. Every one of them stores selector 0, descriptor 727. The drawn frame is `prop_727_0.png`, 64 by 200, a bare trunk whose top rows are opaque bark. The billboard is the native box, −16..12 by 0..100.

The crown is selector 2, descriptor 729 (`prop_729.png`, a leafy top on a short trunk). Selector 1, descriptor 728, is a shorter stub. Nothing in L4 selects either. J03 already left the selector alone at the other chopped tree.

LONGPLAY f_00470 at 39:05 shows crowned palms. That frame was not matched to record 5211, so the crown was not added. Smallest adapter, not applied: draw descriptor 729 on these selector-0 trunks. That would be a state the file does not store.
