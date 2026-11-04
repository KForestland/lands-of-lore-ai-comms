# H07 Spider attack start

Beat 59. Owner F10 2026-11-03 17:56:31, native (5154, 3751). Compared with the Hive sword spider. `L4_HJ.json`, `L5_HC.json`, and `L8_SJ.json`. No new owner F10 after `TRIAGE_20261103.md`.

## Which map the point is

The coordinate lands in the Huline Jungle. The nearest L4 actors are 509 to 538 away:

| Actor | Native x, y | Height | Definition u16 at byte 32 | Events |
| --- | --- | --- | --- | --- |
| 59 | 5634, 3583 | -114 | 1289 | 5 |
| 60 | 5689, 3706 | -114 | 1289 | 9 |
| 58 | 5658, 3938 | -114 | 1289 | 6 |

Beside them, controls 52, 53, and 54 are static slot 91 `Guard block`, at (5553, 3578), (5584, 3713), and (5569, 3924), all height -114, and none of those three controls has an event. The definition number 1289 was not joined to a name. The cstring `GGuard` is in this MIX at file 13290047 and was not joined to definition 1289 either.

No L4 prop within 800 has a spider template. The words `Spider corpse` are a cstring at file 13193278. They sit in a different record from the 38-byte prop names, and no placement near the point uses them.

L5 (the Hive) has no object within 800 of this coordinate. Its nearest actor is 5107 away, at (189, 4949). L8's nearest actor is 680 away, at (4474, 3730). The point is the jungle cluster, not the Hive.

## The book spider

HINTBOOK lines 2569-2573: on the first Hive visit Luther only needs the first level, and the one fight is an icky spider with a large sword.

HINTBOOK lines 2594-2601: rocks dropped into the ravine can be used against that spider later. North of the ravine, a lookout hears the spider in the next cavern. The fight is unavoidable. Later the same blue spiders fall in one hit. This is the weak-Luther fight.

That is the Hive Caves, first visit. It is not a jungle coordinate, and it is not the guard cluster above.

HINTBOOK lines 2416-2420 are the jungle fight people meet if they skip Baccata: a pack of Gladstone guards at the bridge, then the broken thorn gate and the Savage Jungle. Those lines do not say spider. They were not pinned to actors 58-60. The distance from the owner point to those actors is about 500.

## Required or optional

The Hive sword spider is on the first Hive trip. Brady's must-do for that trip is to kill the Hive Warrior and rescue Shalla (file lines 6701-6705). The book spider and the Hive Warrior were not shown to be the same creature.

The jungle point is not that fight. If it is the Gladstone pack, HINTBOOK 2417 presents that pack as what happens when you do not bother with Baccata, so it is not required. The join is open, so this point stays off the required list until the actors are named.

## Frame

No longplay frame was opened.

## Still open

- The name of definition 1289, and whether `GGuard` is that definition.
- Which group starts the attack. The actors' events were not decoded.
- A placement for `Spider corpse`.
- A longplay frame at (5154, 3751).

Grades: the distances, the guard-block controls, and the two cstrings are DECODED. The sword spider and the lookout fight are HINTBOOK. The frame is open.
