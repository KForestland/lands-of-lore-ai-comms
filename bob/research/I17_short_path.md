# I17 the short path

Place L19_BC. No frame was opened. No Godot was run. Static slot 0 is `Golden Door`. Name-at-index stays LIKELY. No compass was read off the automap, so south and east stay the book's words. A degree-2 walk is the neighbor chain. It stops where a quad has more than one unused neighbor.

Hintbook lines 5443–5451: click the door, go forward, turn right, turn right, follow the corridor south, turn east, fall off the ledge into the rapids, duck, and jump out. Grade HINTBOOK. Lines 5452–5456 are the other route: east, north, west, north, a lever, and a bow shot at a high switch. Grade HINTBOOK. Either route is the book's way through. The short one is the one named in the task. Both are REQUIRED as choices, and one of them has to be taken.

## The door

Eighteen movables use static slot 0. The pair at one x is movables 51 and 52, (2550, 854) and (2550, 914), both region 1931, floor −100, ceiling 60. Godot (2550, −854) and (2550, −914). The quad is about 14 wide and 119 tall, center (2550, 884).

Its neighbor words are 65535, 1932, 65535, and 1937.

| step | region | center | floor | why it stops |
| --- | --- | --- | --- | --- |
| door | 1931 | (2550, 884) | −100 | the pair of doors |
| west neighbor | 1932 | (2518, 884) | 0 | ceiling 0 |
| next | 2010 | (2477, 884) | −100 | then three neighbors: 2009 (2477, 816), 1991 (2452, 884), 2011 (2477, 946) |
| other side | 1937 | (2561, 884) | −90 | then three neighbors: 1936 (2561, 820), 1935 (2561, 947), 1943 (2622, 884) |

Past 1937 the chain is not one corridor. 1936 is lower y, 1935 is higher y, and 1943 is higher x. The book's two rights and the south-then-east run are not a stored polyline. No region in this prefix is marked ledge, rapids, or guck.

## Still open

Which branch is the first right. Which axis the book calls south. The ledge and the rapids as regions. The lever on the long route. No frame.
