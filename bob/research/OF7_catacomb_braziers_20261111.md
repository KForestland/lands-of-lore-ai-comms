# OF7. Catacomb braziers stay dark when hit, and the rooms are dim

Owner F10, "need lighting magic or something that produces light, the braziers do not light up when hit", at (2148, -1521, h -118). The map is L10 Dracoid Cemetery. Overlay H is the feet. The camera sits about 10 above the feet, so the eyes are near (2148, -108, -1521). The report area "Jungle" is the F10 label (OF10), not this room.

## Grades

| Claim | Grade |
| --- | --- |
| The stand is the lower bone-basket set, template 23, 47 props (153, 200-241, 336-339). It is not courtyard controls 113/114 (template 42, surface) | PROVEN. L10_DC area.json placements. Heights about y -135 to -150 |
| The nearest basket from that stand is prop 222. The 3D gap from the eyes to its aim is about 254. E reach is 140, so E cannot light it from the reported stand. A level-1 spark ray is 384 and the segment is clear | PROVEN. Placement positions. tests/l10_brazier_spark_test.gd: reachable("222") is false, spark_aimed and spark_target are 222, the mask-3 ray hits the basket |
| Each of the 47 kind-9 records is mask0 0x0051, mask2 0, byte +8 = 1, byte +9 = 0x84 (mode 4, one-shot). Placement byte 30 (durability) is 1. Mode 4 admits when remaining durability is <= 1 | PROVEN. L10_DC native script export, all 47 groups the same shape. placement_hex byte 30 is 1 |
| Spark word0 0x0091 shares bits with 0x0051. Sword word0 0x080E shares none. A remaining of 2 or more rejects | PROVEN. Mask arithmetic. The test asserts admits(spark, 0), rejects the sword, and rejects remaining 2 |
| Opcode 5 in those groups stores prop byte +0x30 = 1. Opcode 6 arm 1 starts the record animation and is not replayed. Firing the host with adapters off rolls the stage back, so the presenter owns the lit state | PROVEN for the command bytes. The production path does not call the host |
| Kind 3 group 5192 is opcode 20, not a hit. There is no kind-4 use event on these props | PROVEN. The same export |
| A spark from the stand lights 222, shows descriptor 219, hides the cold MultiMesh (zero basis), refuses a sword on 223, refuses a second spark, and restores from the saved lit list | PROVEN. tests/l10_brazier_spark_test.gd on gl_compatibility, exit 0. PASS line below |
| The catacomb shade inside the fade start is dim, not black. Sector light on 46 of the 47 baskets is [15, 400, 200, 128]. Row 15 is about 15% RGB. Row 0 (black) is past 600 units | PROVEN. scripts/lol2/sector_shades/L10_DC.json row 15 red channel was inside 0.10..0.25 in the test. Ambient was not raised |
| A lit basket uploads a warm pool, nearest 16, colour (1, 0.62, 0.28), range 640, through the existing night light uniforms | PROVEN as an adapter upload. The test reads light_count 1, position = prop 222's aim, colour w = 640. The native light-record list at runtime 0xFD8C4 was not read, so the colour and the range are not a native record |
| The on-screen hint is "Spark — Light brazier" inside spark range and facing. The journal note names a spark, and only while underground (y < -80) beside an unlit basket | PROVEN. The same test, plus the five journal tests below |
| global 23331 == 5 would reject mode 4 in the native host. The spark cast does not set that global | UNKNOWN whether a live cast ever holds 5. Not exercised here |
| Prima chapter 9 says to light the big braziers and does not name Spark or E. The Hive line that says "spark" is a different room | PROVEN as book text. The mask, not the Hive sentence, is why this room takes a spark |
| Headless Godot cannot see the hidden basket. The dummy renderer ignores set_instance_transform and get_instance_transform returns identity | PROVEN. Godot 4.7.2 dummy mesh storage. The test registry mode is rendered for that reason. The first headless run failed the scale readback for this reason; the GL run stored a zero basis |

## What changed

`scripts/lol2/l10_braziers.gd` admits a hit when (0x0051 & word0) != 0 and remaining durability <= 1. A spark body on layer 2 carries that receiver. The player is a collision exception so the box does not block walking. E inside 140 still calls ignite(). A lit basket scales its source instance to zero and shows the flame. The nearest 16 lit aims call l8_night.apply_lights. Unlit baskets add no light.

`scripts/lol2/l10_journal_hints.gd` adds note l10_catacomb_braziers: "The bone baskets in the dark take a spark. The sword leaves them cold."

Commit 0264ceb3ad536206ca5e36bdb0cb21c31f344cee on grok/of9. Piece 0514. Registry order 753, mode rendered. Lead runs tools/build_deviations.py build. This lane did not.

## Tests

`DISPLAY=:351 /tmp/godot_dummy.sh --display-driver x11 --rendering-method gl_compatibility --resolution 1280x720 --fixed-fps 60 --path ~/opus_work/lol2_grok_of9 --script res://tests/l10_brazier_spark_test.gd`

Printed `PASS brazier spark: prop 222 lights from the reported stand, the sword does not, the flame restores`. Exit 0. No script error.

Headless, exit 0, each printed its PASS line: tests/my_journal_test.gd (51 notes), tests/act1_journal_hints_test.gd, tests/act3_journal_hints_test.gd, tests/act2_findable_test.gd (seventeen in the six scripts), tests/act2_journal_hints_test.gd.

godot_check: 20 scripts, 0 failed.

The older catacomb walk tests/l10_catacomb_earned_test.gd was not re-run. ignite() still checks reach, then commits. That walk is registry order 603.
