# Lamplight egg use (C6, visual still open)

ENH-L8-EGG-NIGHTVISION is not claimed. DOSBox was not started.

## Handler

DECODED. GLOBAL definition index 114, slot `112-Lamplt eggs`, is the only definition on handler 69 (`item19_items/evidence.json`). Handler 69 is `LOLG.DAT` file 854728, VA `0x99AC8`. The matching `ret` is file 854931. The next handler entry is file 854932. File offset is VA plus `0x37000`. The archive sha256 checked this pass is `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775`, size 1977007.

The body does this and then returns. None of the four calls was entered.

- The first stack argument is a pointer. Its first byte is compared with 1. Any other value returns 0.
- When that byte is 1, bit 0 of the byte at `[0x269C4]` is tested. If the bit is clear, the handler calls `0xE3924`. The pushes are `1`, then a word loaded from `([0x269CC] + 0x12E)`, then `0`, then `0`, then immediate `0x23C68`.
- It then calls `0x77ACC` with immediate `0x23348` and `0`.
- If that call returns nonzero, it calls `0x9B8F0` and then `0x5F830`. The second call receives either `[0x96918]` or `[0x9691C]`, chosen by a range test on the first call's result.
- It then loads the word at `[0x22750]`, adds immediate `0xE10` (3600), stores that word back, and returns 1.

The unit of `0xE10` is UNKNOWN. Handler 4, whose only definition is `121-Champion st`, adds the same immediate to a different word, `[0x23AC3]`, at file 840263. A third `81c2100e0000` sits at file 1124431 and falls outside the 108 handler spans. That site was not decoded. No instruction in handler 69 names a palette, a brightness, or a picture.

## Book

BRADY. `brady_guide.txt` line 1515 is the marker `PDF PAGE 42 = PRINTED PAGE 41`. Lines 1526–1529 are the egg entry. The title on line 1526 is messy OCR. Line 1529 reads `low-light vision for 1 minute.` The sentence before it says the eggs are usually recovered from the lair of the Lamplight Queen. That 1 minute is the printed sentence. It was not read out of the `0xE10` add.

## Call chain

DECODED from `LOLG.DAT`, same pin as the handler section. The four calls named there were entered only as far as this section says.

`0xE3924` is large. The first instructions test a byte and can leave. The body was not finished. The port's `item_handlers.gd` group 15 lists handler 69 with that callee and grades the group UNKNOWN. Its "see in the dark" phrase is marked hintbook. Prima's spell chapter and the egg recipe lines do not say that. Brady's sentence is the one in the book section above.

`0x77ACC(0x23348, 0)` returns 0 when the byte at `[0x223D4]` is nonzero. When that byte is zero it stores 0 through the first argument and calls `0xACA44(0x22518, -1, 12, 12)`. `0xACA44` writes a record at argument `+0x40`: the byte at `+3` is 0 because the second argument is `-1`, the word at `+0` is `0xFFFF`, and the bytes at `+4` and `+5` are 12 and 12. It then calls `0xAC7E8`. That call walks ten 8-byte slots while `[0x96A7C]` is nonzero, and jumps elsewhere when that dword is zero. The other branch was not entered. Those 12s were not named a brightness.

`0x9B8F0` returns its argument. `0x5F830` clears one bit in a byte map. Neither call is a picture.

The only `LOLG.DAT` immediates of address `0x22750` are the load and the store in handler 69. No countdown of that word was found. The unit of `0xE10` stays UNKNOWN. Handler 86's port note calls the same immediate ticks on a different word. That note was not re-proven here and was not copied onto `[0x22750]`.

## DOSBox

Not started. Socket `:3` was present earlier this session and no DOSBox process was running. All 30 files in the original `SAVEGAME` directory were scanned for identity `4126891770` (`0xF5FB5EFA`, definition 114 `112-Lamplt eggs`). None contain it. An open walk to the queen was not started. The eaten-egg picture and a played duration stay UNKNOWN. ENH-L8-EGG-NIGHTVISION is not claimed.
