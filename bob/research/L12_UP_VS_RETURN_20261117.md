# L12 way up and way back

Fact page, 17 Nov 2026. No proposal. Header: X = Godot x, Y = Godot z, H = Godot y. The two sittings are not one road reversed.

Way up: 17 Nov, r19o12, from the gulch arrival sha de88903cf254873c19988dbeb90aa86c5322cf9ed1ceb819aa4bf6d0e0ab2db6. Human. Health 27 at the ravine. The pack on that save does not list the Dreamstone. No named place aid. No player STOP. The screen on the plain walks was the dampen-charm HUD.

Way back: 17 Nov, r19o12, from the citadel-exit sha 2eeacb8ec431c556f5113f4053810e946121f631ef7fbe01a5d31cdeb82e477d. Human. Health 21. No named place aid. No player STOP. E at the opening was not pressed.

## 1. Way up, in walk order

1. Ravine. Walk. In at X -344.7 Y -5603.1 H -30.7. Held at X -618.9 Y -8274.6 H 112.0. No jump.
2. Path north-east. Walk. Held at X 484.9 Y -6964.5 H 111.0. No jump.
3. Valley. Walk to X 4588.2 Y -9483.0 H -218.0. The avalanche line was not on this leg. No jump.
4. Glacier. At X 3148.5 Y -11337.0 H -558.0 the screen said "The glacier gives way. Keep to the right-hand wall." Held at X 3330.5 Y -11442.0 H -558.0. Motion height -939, started. No jump. This leg sets the glacier motion.
5. Ice caves. Walk along the right-hand wall to X 4584.5 Y -14107.4 H -558.0. Motion height -1090, remaining 0. No jump.
6. Kenneth, same stand, before the leaps. The screen said "E - Search Kenneth." E. "You find a picture among Kenneth's belongings." Then "Right click - Throw picture at the ground." Right click. "The picture breaks. You recover Kenneth's charm from the frame." No walk between the caves and the search. This leg sets the picture, then the charm.
7. Ice leaps. Eight running jumps, Shift held, one try each. Landed X 4418.3 Y -14270.9 H -727.0, X 4324.8 Y -14389.7 H -738.0, X 4302.5 Y -14527.2 H -767.0, X 4242.2 Y -14696.8 H -763.0, X 4169.4 Y -14874.5 H -777.0, X 4060.0 Y -15008.2 H -763.0, X 3930.8 Y -15153.4 H -778.0, and X 3672.8 Y -15082.1 H -954.1. The screen did not name a run.
8. Far cave. One running jump, Shift held. Held at X 3500.7 Y -14961.7 H -918.0.
9. Ice crossing. Walk to X 2786.1 Y -18233.9 H -1198.0. The screen said "E - Speak with Baccata." No jump.
10. Baccata, same stand. E. "You listen to Baccata's account before continuing toward the citadel."
11. Citadel door. Held at X 3633.3 Y -19267.2 H -1206.0, flat gap 107 from the deck aim. Aimed control 74. The screen was the dampen-charm HUD. It did not say "The Citadel lies ahead. The way in is on the deck." and it did not name E. E was not pressed. This leg does not open the citadel.

The way up needs Human, a walk, then Shift on nine jumps, then E at Kenneth and at Baccata. It does not need the Dreamstone.

## 2. Way back, in walk order

1. Ice opening. At X 2500.3 Y -15457.9 H -918.0 the screen said "The way on is down: jump onto an ice floe on the river, or E - Climb down to the icy gulch." It stayed for 3 seconds, and on the edge at X 2382.5 Y -15727.8 H -918.0 it stayed for the whole wait. E was not pressed. The line is the build's. The code shows it when the Dreamstone condition holds.
2. Floe. From X 2383.8 Y -15730.2 H -918.0 one plain jump, no Shift, landed on floe 0 at X 2236.0 Y -15689.5 H -1145.4.
3. Step off and snow steps. At X 2994.7 Y -12510.7 H -1149.0 the screen said "Step off the floe here and walk up the snow bank." W only. He stood at X 3134.7 Y -12125.7 H -1058.0, feet -1090.
4. Ice bridge. Walk, no jump and no Shift, to X 2999.8 Y -12979.3 H -1058.0. He stayed on the floor.
5. Logs. Eighteen plain jumps, no Shift, onto logs 68, 73, 72, 67, 71, 70, 66, 69, 65, 64, 61, 63, 60, 62, 59, 58, 57 and 56. The hop aimed at log 54, three tries, rose onto the upper floor at X 3424.5 Y -11640.6 H -558.0, feet -590. That height is the glacier band the way up stands on at H -558.
6. Gulch. One walk, no jump, held at X -1079.9 Y -5602.4 H 32.0.
7. River bed. He walked in at X 3020.5 Y -12218.3 H -1158.0, feet -1190. The screen said "Walk up the snow bank to the ice bridge." Held W walked back up to X 3133.9 Y -12123.4 H -1058.0. No jump.

The way back needs the Dreamstone for the opening line, one plain jump, then W on the added steps, then plain jumps on the logs. It does not need Shift and it does not need a form change. Pressing E at the opening is the other choice. This sitting did not press it.

## 3. Where the two roads meet

The way up ends at the citadel door, outside, with E not pressed. The way back begins on the ice after a citadel exit, at the opening around X 2500 Y -15458 H -918. They share the glacier height. The way up reaches H -558 by the right-hand wall after the glacier line. The way back reaches H -558 by the log hop that leaves the river. Between those stands the roads are not the same shelves.

The lake switch is neither road. On 17 Nov at 03:10Z, from the gulch arrival, one plain jump aimed the owner's second shelf (gap 229) and fell. The owner's next shelf is 110 away. That sitting never reached the switch. The completed way back did not go there.

## 4. What the build added, and what each sitting did with it

1. Glacier. `l12_glacier.gd` says "The glacier gives way. Keep to the right-hand wall." when the body enters region 932 or 916, and it moves the glacier floors. Once the motion has started and the citadel exit is not unlocked, source logs 52 through 57 are taken off the collision. The way up heard the line and the motion ran to remaining 0. The way back did not hear this line. Its log hop landed on the upper floor at H -558.
2. Opening and the climb-down. `l12_citadel.gd` says "The way on is down: jump onto an ice floe on the river, or E - Climb down to the icy gulch." E sets the body to about X -1066 Y -5587 H 32 and says the jungle is east. The 17 Nov way back heard the line and took the floe. It did not take the climb-down. On 15 Nov, r19o4, E did take the climb-down and the river was not walked. That is a second way down, not a leg of the floe road.
3. Snow bank. `l12_river_bank.gd` adds invisible packed-snow steps on regions 998 through 1003, rises of 25, and three lines: "Step off the floe here and walk up the snow bank," "Walk up the snow bank to the ice bridge," and "No way up here: step back onto the next ice floe on the river." The 17 Nov way back heard the first two and walked the steps with W. The third line was not the one on that stand. The source bank faces are unchanged. The comment on the script says the bank slope is past the body's step angle, and the floe passes the bank out of a plain jump's reach.

## 5. What the 15 Nov fall recovery hid

Owner bundle report_2026-11-15T04-46-31, 118 poses on MapL12. They walk the gulch from about X -345 Y -5603 H -31 to X -1634 Y -5975, fall in place to H -2313, and 0.256 seconds later stand at X 2784 Y -18222 H -1198, with no pose between. From there they stay on H -1198 out to about X 3624 Y -19290. That H -1198 stretch is the ice tunnel between Baccata and the citadel door.

The snap hides the ravine, the path north-east, the valley, the glacier line, the ice caves, Kenneth, the eight leaps, and the far cave. Those are legs 1 through 8 of the 17 Nov way up. The recovery does not show the river, the floes, the snow steps, or the logs. Those are the way back.

On 15 Nov the reverse walk from the citadel door, r19o3, also did not walk that middle. The tunnel mouth at about X 2886 Y -14791 left the floor, the screen was the key legend, and a named place aid onto the lower ice did not reach the gulch. A later named aid put the body on the gulch path. The opening that day showed the key legend only. The climb-down line was not on that build yet.
