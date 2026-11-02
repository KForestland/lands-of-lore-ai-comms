# ORACLE-SOUL-CUTOFF

Grades are DECODED for bytes read this pass, and BRADY for the printed Draracle split. The live soul byte was not snapped. 0x156F12 was not entered. The opcode 198 body at 0x64887 was not re-entered; its store is the one G76 already entered.

## Soul constant

L20 predicate table file 15602362, 255 entries of 5 bytes. The only shared-index-0 compares in L20, L19, and L16 are L20 index 0 and index 1.

- Index 0, bytes `0302000005`, name `Lsoul_good` at file 15603637. Shared 0 >= immediate 5. Owner is prop 236 only, group 6904. Commands `c60000000601` and `c60000000501`.
- Index 1, bytes `0502000005`, name `Lsoul_evil` at file 15603682. Shared 0 < immediate 5. Owner is prop 236 only, group 6886. Commands `c60000000602` and `c60000000401`.

Equal to 5 takes `Lsoul_good`. Prop 236 is template 11 Will-O-wisp at (-2348, 4217, h0), region 314. That template stays Will-O-wisp.

GLOBAL.MIX slot 0 at the `GV_LUTHERS_SOUL` cstring, stride 41, is that name. Shared index 0 is that slot. The kind-2 read is the byte at the pointer stored at encoded 0x26E58. The earlier DOSBox dword there was 0x1039617c and was not a present guest page, so the live soul byte stays unread.

G76 entered opcode 198 at 0x64887: it stores command byte 5 at the index in command byte 4 of the array at object-5 0x26E54. That array is the local array, not the shared array at 0x26E58. Applied to these four commands, `Lsoul_good` stores local 6 = 1 and local 5 = 1, and `Lsoul_evil` stores local 6 = 2 and local 4 = 1.

Predicate 7, bytes `0003060001`, name `L_is_Good`, is local 6 == 1. Predicate 8, bytes `0003060002`, name `L_is_Evil`, is local 6 == 2. Their owners are actors 49 through 56 and props 1 and 7. Each pair of groups stores the same command bytes on both sides: opcode 9 `090307001500`, and prop 7 also opcode 21 `1503b4004500`. The opcode 9 callee was not entered. Those commands were not read as a Dawn placement or a Draracle placement.

## Dawn

`Dawn_good` and `Dawn_Evil` are not soul compares.

- Index 2, bytes `00020c0002`, name `Dawn_good` at file 15603727. Shared 12 == 2. Owner prop 15, group 304, command `ce0000000001`.
- Index 3, bytes `00020c0000`, name `Dawn_Evil` at file 15603772. Shared 12 == 0. Owner prop 15, group 310, command `ce00000000fe`.

GLOBAL.MIX slot 12 is `GV_DAWN_RELATIONSHIP`. Slot 13 is `GV_BACATTA_RELATIONSHIP`. The last bytes 0x01 and 0xFE are the signed immediates +1 and -2. The opcode 206 callee was not re-entered. The MIX also contains the strings `Dawn Rel is good, Luthers soul increased` at file 15672300 and `Dawn Rel is evil, Luthers soul decreased` at file 15672416. The dwords in front of those strings were not read as group ids.

## Draracle

Brady printed 142 describes a spectral image of the Draracle on the good path and the real Draracle on the evil path. Grade BRADY. L20 and L19 contain no cstring `spectral`, `Spectral`, `faux`, or `Faux`. No predicate name in the L20 name list is a Draracle soul test. The real-versus-spectral soul constant stays unread.

## Static recheck, 2026-11-02

No DOSBox. L20 predicate records at file 15603637, stride 45, name at byte 5, were read again. No name is Draracle, spectral, or real. The only shared-0 compares are still `Lsoul_good` and `Lsoul_evil`. Comment strings include `Evil Luther killed by Draracle - Finale 233`, `Evil Luther kills the Draracle - Finale 244`, `Good Luther beats belial!`, and `Ruby of Truth`. None of those strings contains a soul number, and none says spectral or real. The integers in front of the strings were not read as predicate indexes. The real-versus-spectral constant stays unread.

## Watch

One watch per branch was not aimed. DOSBox was not relaunched for this pass. The task receipt is the decoded names and constants above.
