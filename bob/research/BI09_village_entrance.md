# BI09 village entrance before the temple

No native Huline stands at the village entrance before the temple visit. The guard is actor 113, and his placement starts absent.

## Evidence

Owner r18 F10 15-32-38 at (508,-4484). Journal `l8_see_temple_first` is set, so the temple has not been visited.

Population `scripts/lol2/act2_populations/L8_SJ.json`, source DAT/L8_SJ.MIX sha256 3eff07430a453d2c6f09133f869874e0530af1b6a3bfff7f4297761b96a28bc2. Actor 113, definition 1, name WILD, position (676, 0, -4541), flags 30082, behavior 7, present false. That point is 177 from the report. Actor 22, definition 4, name DANIEL, at (522, -30, -4743), is also present false. No other actor is within 500 of (508,-4484).

The link is native group 7770, called by prop 531 (pack record 531 at (705, 0, -4636), region 1716) on kind 6 value 20. Predicate 97 is `0003060001`: opcode-198 index 6 equals 1 (`native_script_host.gd`, operator 0, left type 3). Group 7770 is opcode 9 arm 3 on actor 113, then opcode 13 and two opcode 14s. Opcode 9 arm 3 is the presence link.

Index 6 is set to 1 by kind 12 on regions 1514, 1515, 1519, 1523, 1527, and 1530, and only while it is 0 (predicate 146, `0003060000`). Those floors sit around (1018..1333, 2749..2928), the temple side. Prop 502 at (-5227, 0, 1269) also stores 1, on kind 5 value 19. Nothing at the gate writes index 6. The L8 arrival seed writes index 13, not 6.

HINTBOOK 2932-2941 and 2979-2984, and BRADY printed 91 lines 3685-3686: the settlement stays closed until the temple talk, and the guard is met after that. Grade DECODED for the actor, the group, and the predicate. Grade HINTBOOK for the order.

BG25's figure at the tree (554,-3929) is this same actor after `temple_visited`. His native point is the gate. The port spawns him in `l8_journey.gd` only once `temple_visited` is set, which matches the bytes. No patch.
