# M04 LoL1 item, monster, and spell tables

No Godot was run. The item rows are ONETIME.INF property indexes from the generated `onetime.inf`, read with the stack order in ScummVM `olol_setItemProperty`: position 1 name string, 2 shape index, 3 type word, 4 item-script function, 5 might, 6 skill, 7 protection, 8 flags. Bit 0x4000 on the name selects `lands.json`. All 285 names resolved. The shape column is `shpIndex`, not a filename.

Type word 5 is the weapon slot in the same function's Vaelan comment (`stackPos(0) == 264` and type 5 is forced to 0 on an unpatched floppy). The CD scan already stores type word 0 on indexes 263 and 264. Other type words are not named. Counts: 0 x120, 5 x112, 32 x17, 16 x11, 10 x7, 1536 x7, 256 x4, 128 x4, 64 x2, 15 x1.

Flag bit 2 (value 4) is the bit `items.gd` `moveable` treats as outside the distant-level recycle test. The other flag bits were not named. Script function 255 was not given a meaning.

L05 says the CD import does not include Dawn's Key. Index 198 in this table is named Dawn's Key. Those two sentences stay unmerged. Index 199 is stored as Nathanial's Key.

## Items

| id | name | shape | type | script | might | skill | prot | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Illegal Item | 0 | 0 | 255 | 0 | 0 | 0 | 0000 |
| 1 | Poison dart | 6 | 0 | 25 | 8 | 1 | 0 | 1000 |
| 2 | Arrow | 6 | 0 | 2 | 10 | 1 | 0 | 1000 |
| 3 | Arrow | 12 | 0 | 2 | 15 | 4 | 0 | 1000 |
| 4 | Quarrel | 9 | 0 | 2 | 15 | 1 | 0 | 1000 |
| 5 | Shurikan | 8 | 0 | 2 | 10 | 1 | 0 | 1000 |
| 6 | Shurikan | 8 | 0 | 2 | 10 | 1 | 0 | 1000 |
| 7 | Muck | 10 | 0 | 2 | 10 | 1 | 0 | 1000 |
| 8 | Spit | 11 | 0 | 2 | 22 | 1 | 0 | 1000 |
| 9 | temp item | 0 | 0 | 5 | 35 | 4 | 0 | 5000 |
| 10 | Ice Bolt | 1 | 0 | 27 | 25 | 3 | 0 | 5000 |
| 11 | Spike | 2 | 0 | 2 | 15 | 1 | 0 | 1000 |
| 12 | Pain | 5 | 0 | 23 | 25 | 128 | 0 | 1000 |
| 13 | Dispell | 4 | 0 | 26 | 0 | 128 | 0 | 5000 |
| 14 | Poison | 3 | 0 | 25 | 10 | 128 | 0 | 1000 |
| 15 | Dispell | 4 | 0 | 2 | 15 | 128 | 0 | 5000 |
| 16 | Dwarvish horseshoe | 38 | 0 | 255 | 0 | 0 | 0 | 0002 |
| 17 | Dwarvish helm | 22 | 16 | 1 | 0 | 0 | 8 | 0012 |
| 18 | Saber "Cougar" | 4 | 5 | 0 | 16 | 0 | 3 | 000a |
| 19 | Wand of Death | 27 | 0 | 20 | 5 | 0 | 0 | 0005 |
| 20 | Cobra figurine | 121 | 0 | 255 | 0 | 0 | 0 | 0004 |
| 21 | Dragon figurine | 123 | 0 | 255 | 0 | 0 | 0 | 0004 |
| 22 | Humanoid figurine | 122 | 0 | 255 | 0 | 0 | 0 | 0004 |
| 23 | Unicorn figurine | 124 | 0 | 255 | 0 | 0 | 0 | 0004 |
| 24 | Arbalest | 23 | 5 | 11 | 4 | 40 | 0 | 0408 |
| 25 | Arbalest "Equalizer" | 23 | 5 | 11 | 4 | 0 | 0 | 0408 |
| 26 | Arbalest "Redemption" | 23 | 5 | 11 | 4 | 56 | 0 | 0408 |
| 27 | Arbalest "Eternity" | 23 | 5 | 11 | 4 | 60 | 0 | 0408 |
| 28 | Pick | 9 | 5 | 0 | 7 | 0 | 0 | 000a |
| 29 | Axe | 1 | 5 | 0 | 10 | 0 | 0 | 000a |
| 30 | Axe "Dominance" | 1 | 5 | 0 | 10 | 0 | 0 | 000a |
| 31 | Axe "Slitter" | 1 | 5 | 0 | 11 | 0 | 0 | 000a |
| 32 | Axe "Splitter" | 1 | 5 | 0 | 11 | 0 | 0 | 000a |
| 33 | Axe "Vixen" | 1 | 5 | 0 | 16 | 0 | 0 | 000a |
| 34 | Axe "Butcher" | 1 | 5 | 0 | 15 | 0 | 0 | 000a |
| 35 | Bow | 25 | 5 | 11 | 2 | 10 | 0 | 0408 |
| 36 | Bow "Gemini" | 25 | 5 | 11 | 2 | 10 | 0 | 0408 |
| 37 | Bow "Scout" | 25 | 5 | 11 | 2 | 11 | 0 | 0408 |
| 38 | Bow "Tempest" | 25 | 5 | 11 | 2 | 15 | 0 | 0408 |
| 39 | Crossbow | 23 | 5 | 11 | 4 | 15 | 0 | 0408 |
| 40 | Crossbow "Valkyrie" | 23 | 5 | 11 | 3 | 15 | 0 | 0408 |
| 41 | Crossbow "Swift" | 23 | 5 | 11 | 4 | 17 | 0 | 0408 |
| 42 | Crossbow "Elayna" | 23 | 5 | 11 | 4 | 23 | 0 | 0408 |
| 43 | Weathered dagger | 7 | 5 | 0 | 4 | 1 | 0 | 180a |
| 44 | Dagger | 7 | 5 | 0 | 10 | 1 | 0 | 180a |
| 45 | Dagger "Riposte" | 7 | 5 | 0 | 5 | 1 | 25 | 180a |
| 46 | Dagger "Stiletto" | 7 | 5 | 0 | 6 | 1 | 0 | 180a |
| 47 | Dagger "Back Biter" | 7 | 5 | 0 | 7 | 1 | 0 | 180a |
| 48 | Dagger "Fang" | 7 | 5 | 0 | 8 | 1 | 0 | 180a |
| 49 | Dagger "Razor" | 7 | 5 | 0 | 9 | 1 | 0 | 180a |
| 50 | Dagger "Assassin" | 7 | 5 | 0 | 12 | 1 | 0 | 180a |
| 51 | Jewelled Dagger | 53 | 5 | 0 | 45 | 1 | 0 | 180e |
| 52 | Great axe | 8 | 5 | 0 | 30 | 0 | 0 | 000a |
| 53 | Great axe "Master" | 8 | 5 | 0 | 30 | 0 | 0 | 000a |
| 54 | Great axe "Meister" | 8 | 5 | 0 | 30 | 0 | 0 | 000a |
| 55 | Great axe "Reaper" | 8 | 5 | 0 | 36 | 0 | 0 | 000a |
| 56 | Great axe "Death" | 8 | 5 | 0 | 39 | 0 | 0 | 000a |
| 57 | Great axe "Brimstone" | 8 | 5 | 0 | 42 | 0 | 0 | 000a |
| 58 | Great axe "Executioner" | 8 | 5 | 0 | 45 | 0 | 0 | 000a |
| 59 | Sledge | 56 | 5 | 0 | 15 | 2 | 0 | 000a |
| 60 | Great maul | 56 | 5 | 0 | 40 | 2 | 0 | 000a |
| 61 | Great maul "Hammerhead" | 56 | 5 | 0 | 44 | 2 | 0 | 000a |
| 62 | Great maul "Pillage" | 56 | 5 | 0 | 48 | 2 | 0 | 000a |
| 63 | Great maul "Thor's Fist" | 56 | 5 | 0 | 52 | 2 | 0 | 000a |
| 64 | Great maul "Thunder" | 56 | 5 | 0 | 56 | 2 | 0 | 000a |
| 65 | Great maul "Armageddon" | 56 | 5 | 0 | 60 | 2 | 0 | 000a |
| 66 | Great bow | 25 | 5 | 11 | 2 | 20 | 0 | 0408 |
| 67 | Great bow "Tracker" | 25 | 5 | 11 | 2 | 22 | 0 | 0408 |
| 68 | Peregrin great bow | 25 | 5 | 11 | 2 | 24 | 0 | 0408 |
| 69 | Great bow "Darkness" | 25 | 5 | 11 | 2 | 30 | 0 | 0408 |
| 70 | Great sword | 6 | 5 | 0 | 40 | 1 | 0 | 000a |
| 71 | Great sword "Trouble" | 6 | 5 | 0 | 48 | 1 | 0 | 000a |
| 72 | Eagle great sword | 6 | 5 | 0 | 52 | 1 | 0 | 000a |
| 73 | Great sword "Doom" | 6 | 5 | 0 | 56 | 1 | 0 | 000a |
| 74 | Great sword "Justice" | 6 | 5 | 0 | 60 | 1 | 0 | 000a |
| 75 | Halberd | 13 | 5 | 0 | 40 | 0 | 0 | 000a |
| 76 | Halberd "Sever" | 13 | 5 | 0 | 44 | 0 | 0 | 000a |
| 77 | Halberd "Widow" | 13 | 5 | 0 | 52 | 0 | 0 | 000a |
| 78 | Halberd "Death's Hand" | 13 | 5 | 0 | 60 | 0 | 0 | 000a |
| 79 | Horseshoe | 38 | 0 | 255 | 0 | 0 | 0 | 0002 |
| 80 | Bronze horseshoe | 38 | 0 | 255 | 0 | 0 | 0 | 0002 |
| 81 | Long sword | 5 | 5 | 0 | 20 | 1 | 0 | 000a |
| 82 | Long sword "Entropy" | 45 | 5 | 0 | 20 | 1 | 0 | 000a |
| 83 | Long sword "Protector" | 44 | 5 | 0 | 20 | 1 | 5 | 000a |
| 84 | Long sword "Flayer" | 47 | 5 | 0 | 22 | 1 | 0 | 000a |
| 85 | Long sword "Gnarl" | 46 | 5 | 0 | 27 | 1 | 0 | 000a |
| 86 | Long sword "Gnash" | 44 | 5 | 0 | 27 | 1 | 0 | 000a |
| 87 | Long sword "Snarl" | 45 | 5 | 0 | 24 | 1 | 0 | 000a |
| 88 | Long sword "Ares' Breath" | 46 | 5 | 0 | 26 | 1 | 0 | 000a |
| 89 | Long sword "Life Taker" | 44 | 5 | 0 | 30 | 1 | 0 | 000a |
| 90 | Mace | 2 | 5 | 0 | 13 | 2 | 0 | 000a |
| 91 | Mace "Bouncer" | 2 | 5 | 0 | 16 | 2 | 1 | 000a |
| 92 | Mace "Puma" | 2 | 5 | 0 | 17 | 2 | 0 | 000a |
| 93 | Rapier | 3 | 5 | 0 | 16 | 1 | 3 | 000a |
| 94 | Rapier "Coup D' Grace" | 3 | 5 | 0 | 16 | 1 | 3 | 000a |
| 95 | Rapier "Ripper" | 3 | 5 | 0 | 18 | 1 | 3 | 000a |
| 96 | Rapier "Dicer" | 3 | 5 | 0 | 20 | 1 | 3 | 000a |
| 97 | Rapier "Talon" | 3 | 5 | 0 | 23 | 1 | 3 | 000a |
| 98 | Lump of coal | 55 | 5 | 2 | 2 | 2 | 0 | 0008 |
| 99 | Rock | 35 | 5 | 2 | 2 | 2 | 0 | 0008 |
| 100 | Granite rock | 35 | 5 | 2 | 3 | 2 | 0 | 0008 |
| 101 | Smooth rock | 35 | 5 | 2 | 3 | 2 | 0 | 0008 |
| 102 | Saber | 4 | 5 | 0 | 12 | 0 | 0 | 000a |
| 103 | Sabre "Cutter" | 4 | 5 | 0 | 13 | 0 | 13 | 000a |
| 104 | Sabre "Gutter" | 4 | 5 | 0 | 13 | 0 | 3 | 000a |
| 105 | Saber "Wolf" | 4 | 5 | 0 | 14 | 0 | 3 | 000a |
| 106 | Saber "Dragon's Tooth" | 4 | 5 | 0 | 17 | 0 | 3 | 000a |
| 107 | Sickle | 4 | 5 | 0 | 15 | 0 | 0 | 000a |
| 108 | Staff | 11 | 5 | 0 | 10 | 2 | 5 | 0008 |
| 109 | Staff "Gustavus" | 11 | 5 | 0 | 10 | 2 | 5 | 0008 |
| 110 | Staff "Beater" | 11 | 5 | 0 | 11 | 2 | 5 | 0008 |
| 111 | Staff "Gainful" | 11 | 5 | 0 | 12 | 2 | 5 | 0008 |
| 112 | Staff "Tarsal" | 11 | 5 | 0 | 13 | 2 | 5 | 0008 |
| 113 | Bloody staff | 11 | 5 | 0 | 14 | 2 | 5 | 0008 |
| 114 | Death Stick | 11 | 5 | 0 | 15 | 2 | 5 | 0008 |
| 115 | Star | 10 | 5 | 11 | 5 | 7 | 0 | 000a |
| 116 | Star "Shining" | 10 | 5 | 11 | 5 | 8 | 0 | 000a |
| 117 | Star "Shooting" | 10 | 5 | 11 | 5 | 9 | 0 | 000a |
| 118 | Star "Fire" | 10 | 5 | 11 | 5 | 10 | 0 | 000a |
| 119 | Star "Polaris" | 10 | 5 | 11 | 5 | 11 | 0 | 000a |
| 120 | Star "Vega" | 10 | 5 | 11 | 5 | 12 | 0 | 000a |
| 121 | Stick | 36 | 5 | 0 | 2 | 2 | 0 | 0008 |
| 122 | Treant stick | 36 | 5 | 0 | 5 | 2 | 0 | 0008 |
| 123 | Westwood stick | 36 | 5 | 0 | 10 | 2 | 0 | 0008 |
| 124 | Trident | 12 | 5 | 0 | 30 | 0 | 0 | 000a |
| 125 | Trident "Mantis" | 12 | 5 | 0 | 36 | 0 | 0 | 000a |
| 126 | Trident "Mandible" | 12 | 5 | 0 | 39 | 0 | 3 | 000a |
| 127 | Trident "Plague" | 12 | 5 | 0 | 42 | 0 | 0 | 000a |
| 128 | Trident "Pestilence" | 12 | 5 | 0 | 45 | 0 | 0 | 000a |
| 129 | Boots | 32 | 256 | 1 | 0 | 0 | 5 | 0010 |
| 130 | Dwarvish boots | 32 | 256 | 1 | 0 | 0 | 7 | 0010 |
| 131 | Buckler | 19 | 10 | 1 | 0 | 0 | 5 | 0010 |
| 132 | Shield of Stealth | 19 | 10 | 1 | 0 | 0 | 6 | 0010 |
| 133 | Dwarvish buckler | 19 | 10 | 1 | 0 | 0 | 7 | 0010 |
| 134 | Chain mail | 17 | 32 | 1 | 0 | 0 | 30 | 0012 |
| 135 | Dwarvish chain mail | 78 | 32 | 1 | 0 | 0 | 40 | 0012 |
| 136 | Chain mail "Protector" | 78 | 32 | 1 | 0 | 0 | 45 | 0012 |
| 137 | Torn shirt | 14 | 32 | 1 | 0 | 0 | 4 | 0010 |
| 138 | Shirt | 14 | 32 | 1 | 0 | 0 | 5 | 0010 |
| 139 | Whisper Cloak | 14 | 32 | 1 | 0 | 0 | 7 | 0010 |
| 140 | Great helm | 22 | 16 | 1 | 0 | 0 | 10 | 0012 |
| 141 | Mesmer's great helm | 22 | 16 | 1 | 0 | 0 | 10 | 0012 |
| 142 | Great helm "Nestor" | 22 | 16 | 1 | 0 | 0 | 10 | 0012 |
| 143 | Dwarvish great helm | 22 | 16 | 1 | 0 | 0 | 15 | 0012 |
| 144 | Aegis great helm | 22 | 16 | 1 | 0 | 0 | 20 | 0012 |
| 145 | Helm | 22 | 16 | 1 | 0 | 0 | 5 | 0012 |
| 146 | Helm "Talamar" | 22 | 16 | 1 | 0 | 0 | 7 | 0012 |
| 147 | Helm "Prentis" | 22 | 16 | 1 | 0 | 0 | 12 | 0012 |
| 148 | Aegis helm | 22 | 16 | 1 | 0 | 0 | 11 | 0012 |
| 149 | Kite shield | 39 | 10 | 1 | 0 | 0 | 12 | 0012 |
| 150 | George's kite shield | 39 | 10 | 1 | 0 | 0 | 14 | 0012 |
| 151 | Dwarvish kite shield | 20 | 10 | 1 | 0 | 0 | 15 | 0012 |
| 152 | Aegis kite shield | 20 | 10 | 1 | 0 | 0 | 25 | 0012 |
| 153 | Leather jerkin | 15 | 32 | 1 | 0 | 0 | 10 | 0010 |
| 154 | Hale leather jerkin | 110 | 32 | 1 | 0 | 0 | 13 | 0010 |
| 155 | Kane leather jerkin | 15 | 32 | 1 | 0 | 0 | 15 | 0010 |
| 156 | Plate mail | 18 | 32 | 1 | 0 | 0 | 40 | 0012 |
| 157 | Galenian plate mail | 79 | 32 | 1 | 0 | 0 | 40 | 0012 |
| 158 | Dwarvish plate mail | 79 | 32 | 1 | 0 | 0 | 50 | 0012 |
| 159 | Bastion plate mail | 79 | 32 | 1 | 0 | 0 | 50 | 0012 |
| 160 | Aegis plate mail | 79 | 32 | 1 | 0 | 0 | 60 | 0012 |
| 161 | Silent sandals | 33 | 256 | 1 | 0 | 0 | 0 | 0010 |
| 162 | Sandals | 33 | 256 | 1 | 0 | 0 | 1 | 0010 |
| 163 | Scale mail | 16 | 32 | 1 | 0 | 0 | 20 | 0012 |
| 164 | Glint mail | 77 | 32 | 1 | 0 | 0 | 23 | 0012 |
| 165 | Dwarvish scale mail | 77 | 32 | 1 | 0 | 0 | 28 | 0012 |
| 166 | Roland's key | 59 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 167 | Thug's key | 58 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 168 | Bronze key | 60 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 169 | Worn key | 62 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 170 | Red key | 61 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 171 | Iron key | 63 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 172 | Minotaur Horn | 85 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 173 | Silver key | 62 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 174 | Mine key 2 | 62 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 175 | Mine key 3 | 62 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 176 | Mine key 4 | 62 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 177 | Mine key 5 | 62 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 178 | Ebony Key | 115 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 179 | Gold Key | 101 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 180 | Xeob Key | 99 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 181 | Knowle Key | 100 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 182 | Silver Key | 117 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 183 | Copper Key | 75 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 184 | Ivory Key | 74 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 185 | Library key | 29 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 186 | Worn key | 64 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 187 | Blue Key | 65 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 188 | Yellow Key | 101 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 189 | Small Key | 102 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 190 | Speckled Key | 119 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 191 | Jade Key | 120 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 192 | Mystic Key | 86 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 193 | Mystic Key | 87 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 194 | Mystic Key | 88 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 195 | Mystic Key | 89 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 196 | Mystic Key | 90 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 197 | Mystic Key | 91 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 198 | Dawn's Key | 41 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 199 | Nathanial's Key | 41 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 200 | Paulson's Key | 41 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 201 | Geron's Key | 41 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 202 | Death Key | 83 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 203 | Noir key | 125 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 204 | Dull key | 126 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 205 | Oily key | 127 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 206 | Carrion key | 61 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 207 | Blood key | 61 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 208 | Adder key | 118 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 209 | Shiney key | 74 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 210 | Rusty key | 75 | 0 | 255 | 1 | 0 | 0 | 0104 |
| 211 | Empty flask | 106 | 0 | 255 | 0 | 0 | 0 | 0004 |
| 212 | Swamp Vial | 107 | 0 | 32 | 4 | 16 | 0 | 0005 |
| 213 | Honey | 108 | 0 | 32 | 4 | 16 | 0 | 0005 |
| 214 | Earth Vial | 109 | 0 | 32 | 4 | 16 | 0 | 0005 |
| 215 | Bannon's reserve | 114 | 0 | 30 | 0 | 0 | 0 | 0001 |
| 216 | Salve | 30 | 0 | 4 | 4 | 16 | 0 | 0021 |
| 217 | Aloe | 43 | 0 | 4 | 1 | 6 | 0 | 0021 |
| 218 | Ginseng | 42 | 0 | 4 | 2 | 6 | 0 | 0021 |
| 219 | Jade Necklace | 104 | 64 | 31 | 0 | 0 | 0 | 0001 |
| 220 | Ruby of Truth | 105 | 64 | 31 | 0 | 0 | 0 | 0005 |
| 221 | Diamond | 103 | 0 | 255 | 0 | 0 | 0 | 0004 |
| 222 | Emerald Eye | 49 | 0 | 255 | 0 | 0 | 0 | 0004 |
| 223 | Sapphire Eye | 48 | 0 | 255 | 0 | 0 | 0 | 0004 |
| 224 | Gold Jewel | 81 | 0 | 255 | 0 | 0 | 0 | 0004 |
| 225 | Bezel ring | 116 | 1536 | 255 | 0 | 0 | 0 | 0004 |
| 226 | Amber Ring | 82 | 1536 | 1 | 0 | 0 | 5 | 0004 |
| 227 | Talba Ring | 82 | 1536 | 255 | 0 | 0 | 0 | 0004 |
| 228 | Duble ring | 82 | 1536 | 255 | 0 | 0 | 0 | 0004 |
| 229 | Cloud ring | 129 | 1536 | 255 | 0 | 0 | 0 | 0004 |
| 230 | Zephyr ring | 129 | 1536 | 255 | 0 | 0 | 0 | 0004 |
| 231 | Ebony staff | 84 | 0 | 20 | 9 | 0 | 0 | 0005 |
| 232 | Wand of Fireballs | 28 | 0 | 20 | 3 | 0 | 0 | 0001 |
| 233 | Wand of Lightning | 28 | 5 | 20 | 6 | 0 | 0 | 0001 |
| 234 | Freeze scroll | 34 | 0 | 14 | 2 | 0 | 0 | 0005 |
| 235 | Lightning scroll | 34 | 0 | 14 | 6 | 0 | 0 | 0005 |
| 236 | Fireball scroll | 34 | 0 | 14 | 3 | 0 | 0 | 0005 |
| 237 | Hand of Fate scroll | 34 | 0 | 14 | 4 | 0 | 0 | 0005 |
| 238 | Mist of Doom scroll | 34 | 0 | 14 | 5 | 0 | 0 | 0005 |
| 239 | Vortex scroll | 34 | 0 | 14 | 7 | 0 | 0 | 0005 |
| 240 | Burnt Scroll | 34 | 0 | 12 | 102 | 64 | 0 | 0001 |
| 241 | Riddle Scroll | 34 | 0 | 17 | 0 | 0 | 0 | 0005 |
| 242 | Note | 67 | 0 | 12 | 118 | 65 | 0 | 0001 |
| 243 | Coin Purse | 45 | 0 | 9 | 0 | 0 | 0 | 00c0 |
| 244 | Writ of Passage | 40 | 0 | 12 | 120 | 65 | 0 | 0005 |
| 245 | Lockpicks | 37 | 0 | 255 | 0 | 0 | 0 | 0004 |
| 246 | Silver goblet | 54 | 0 | 15 | -1 | 1 | 0 | 0025 |
| 247 | Broken glass | 0 | 0 | 13 | 0 | 0 | 0 | 0084 |
| 248 | Oil Flask | 31 | 0 | 8 | 0 | 0 | 0 | 0001 |
| 249 | Lantern | 44 | 0 | 10 | 0 | 0 | 0 | 00c4 |
| 250 | Humanoid bone | 50 | 5 | 2 | 2 | 2 | 0 | 0008 |
| 251 | Humanoid bone | 51 | 5 | 2 | 2 | 2 | 0 | 0008 |
| 252 | Humanoid bone | 52 | 5 | 2 | 2 | 2 | 0 | 0008 |
| 253 | Gear | 24 | 15 | 2 | 2 | 2 | 0 | 000c |
| 254 | Dark Gauntlet | 98 | 5 | 28 | 0 | 0 | 5 | 000c |
| 255 | Statuette | 96 | 5 | 255 | 0 | 0 | 0 | 0004 |
| 256 | Note | 67 | 0 | 12 | 118 | 65 | 0 | 0001 |
| 257 | Note | 67 | 0 | 12 | 116 | 64 | 0 | 0001 |
| 258 | Note | 67 | 0 | 12 | 126 | 64 | 0 | 0001 |
| 259 | Ceremonial Mask | 69 | 16 | 1 | 0 | 0 | 5 | 0014 |
| 260 | Crucible of Faith | 80 | 0 | 255 | 0 | 0 | 0 | 0004 |
| 261 | Note | 67 | 0 | 19 | -61 | 65 | 0 | 0001 |
| 262 | Bezel Cup | 92 | 0 | 18 | 0 | 0 | 0 | 0221 |
| 263 | Vaelan's Cube | 71 | 0 | 21 | 0 | 0 | 0 | 0005 |
| 264 | Vaelan's Cube | 70 | 0 | 21 | 0 | 0 | 0 | 0005 |
| 265 | Bracers of Defense | 137 | 128 | 1 | 0 | 0 | 15 | 0010 |
| 266 | Green Skull | 68 | 5 | 29 | 8 | 0 | 0 | 0005 |
| 267 | Swarm | 72 | 0 | 24 | 9 | 0 | 0 | 0001 |
| 268 | Note | 67 | 0 | 12 | -50 | 66 | 0 | 0001 |
| 269 | Guardian | 76 | 0 | 24 | 16 | 0 | 0 | 0001 |
| 270 | Ace of Infinity | 132 | 0 | 30 | 0 | 0 | 0 | 0001 |
| 271 | Ace of Dominion | 131 | 0 | 24 | 4 | 4 | 0 | 0001 |
| 272 | Ace of Oblivion | 130 | 0 | 24 | 5 | 3 | 0 | 0001 |
| 273 | Bloodstone | 134 | 0 | 255 | 0 | 0 | 0 | 0004 |
| 274 | Emerald blade | 26 | 5 | 0 | 25 | 129 | 0 | 000e |
| 275 | Note | 67 | 0 | 12 | 86 | 66 | 0 | 0001 |
| 276 | Note | 67 | 0 | 12 | 90 | 66 | 0 | 0001 |
| 277 | Bracers | 136 | 128 | 1 | 0 | 0 | 5 | 0010 |
| 278 | Steel Bracers | 136 | 128 | 1 | 0 | 0 | 10 | 0010 |
| 279 | Bracers of Defense | 137 | 128 | 1 | 0 | 0 | 15 | 0010 |
| 280 | The Whole Truth | 73 | 0 | 31 | 0 | 0 | 0 | 0005 |
| 281 | Shard of truth | 57 | 1536 | 255 | 0 | 0 | 0 | 0005 |
| 282 | Note | 67 | 0 | 12 | 90 | 66 | 0 | 0001 |
| 283 | Note | 67 | 0 | 12 | 0 | 0 | 0 | 0001 |
| 284 | Note | 67 | 0 | 12 | 0 | 0 | 0 | 0001 |

## Spells

Rows are `static_tables.json` `spellProperties`, in that order. The name is `spellNameCode` through the same 0x4000 lands bit. `party.gd` compares `mpRequired` and `hpRequired` with the selected character's current magic and hit points, four levels. `field_a`, `field_c`, `field_16`, and `field_18` are unnamed. Rows 10 through 16 have code 0 and were not given names. Rows 8 and 9 share the name Caustic fog and are not one row.

| row | name | code | mp | hp | flags | field_a |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Spark | 16436 | 5 10 15 25 | 0 0 0 0 | 256 | 0 |
| 1 | Heal | 16437 | 5 10 25 60 | 0 0 0 0 | 1 | 0 |
| 2 | Freeze | 16438 | 8 15 30 80 | 0 0 0 0 | 258 | 0 |
| 3 | Fireball | 16440 | 20 35 65 100 | 0 0 0 0 | 259 | 0 |
| 4 | Hand of Fate | 16441 | 30 60 90 120 | 0 0 0 0 | 260 | 0 |
| 5 | Mist of Doom | 16442 | 30 60 90 150 | 0 0 0 0 | 261 | 0 |
| 6 | Lightning | 16439 | 25 30 50 100 | 0 0 0 0 | 262 | 0 |
| 7 | Vortex | 16443 | 3 6 12 24 | 0 0 0 0 | 263 | 0 |
| 8 | Caustic fog | 16975 | 15 15 15 15 | 0 0 0 0 | 264 | 0 |
| 9 | Caustic fog | 16975 | 15 15 15 15 | 0 0 0 0 | 264 | 15 |

No spell row was joined to a projectile sprite. The large-fireball width stays 63, from L05 and the comment in `items_lol.cpp`.

## Monsters

`monsters.json` is 44 shape banks. Each bank has a `bank` id and a `palettes` list. GUARD.SHP's bank id is `mon_guard` and its palette list has 16 entries. The bank is not a stat row.

Banks: AMAZON, ARCHRSLG, AVIANWRM, BANDIT, BOAR, CABAL, CAVEDWLR, DETHDISK, EXECTNR, FLSPIDER, GIMLET, GRTORC, GUARD, HAG, HORNET, HURZELL, IRONGRZR, KNOWLES, LARKHON, LIZARD, MAGICMIR, MANTHA, MINOTAUR, MOLDER, MORIBUND, MULTIPD, NECROSAP, ORC, PENTROG, RATMAN, ROCKLING, SCAVNGR, SCO_TOAD, SERP_EXE, STARK, SWAMPCIT, SWAMPMON, THUG, TOAD, TOADSERP, TREZ, VIPER, WRAITH, XEOB. Each key ends in `.SHP`.

`loadMonsterProperties` fills one level-local row. `monsters.gd` reads shape from argument 1, hit points from argument 26, and flags from argument 27. Arguments 35 through 38 are attack chance, attack type, defense chance, and defense type. A lot of those four words came back as 0x8000, and this pass did not disassemble the pushes, so those four stay unknown. A second call can overwrite the same index. The table is every concrete INI function 0 row whose hit-point word was a number. Level 14 index 1 appears twice because two calls stored two hit-point words. Level 2's four rows were reached only after an unknown test. The other rows were not.

| level | index | shape | hit points | flags |
| --- | --- | --- | --- | --- |
| 1 | 1 | 0 | 200 | 0x0100 |
| 2 | 3 | 1 | 15 | 0x0080 |
| 2 | 2 | 0 | 15 | 0x0000 |
| 2 | 1 | 1 | 20 | 0x0000 |
| 2 | 4 | 1 | 20 | 0x0000 |
| 3 | 1 | 0 | 15 | 0x0080 |
| 3 | 2 | 1 | 40 | 0x0000 |
| 4 | 1 | 0 | 15 | 0x0080 |
| 4 | 2 | 1 | 50 | 0x0080 |
| 5 | 1 | 0 | 20 | 0x0000 |
| 6 | 1 | 0 | 40 | 0x0000 |
| 6 | 3 | 1 | 35 | 0x0000 |
| 7 | 1 | 0 | 75 | 0x0000 |
| 7 | 2 | 1 | 30 | 0x0000 |
| 7 | 3 | 0 | 35 | 0x0000 |
| 8 | 1 | 1 | 20 | 0x0000 |
| 8 | 2 | 0 | 75 | 0x0000 |
| 9 | 2 | 1 | 20 | 0x0000 |
| 9 | 1 | 0 | 68 | 0x0000 |
| 10 | 1 | 0 | 15 | 0x0080 |
| 10 | 2 | 1 | 78 | 0x0002 |
| 11 | 1 | 0 | 95 | 0x0000 |
| 11 | 2 | 1 | 80 | 0x0000 |
| 12 | 1 | 0 | 110 | 0x0200 |
| 12 | 2 | 1 | 80 | 0x0000 |
| 13 | 1 | 0 | 30 | 0x0000 |
| 13 | 2 | 1 | 90 | 0x0000 |
| 14 | 1 | 0 | 125 | 0x0000 |
| 14 | 2 | 1 | 60 | 0x0000 |
| 14 | 1 | 0 | 233 | 0x0000 |
| 15 | 1 | 0 | 95 | 0x0000 |
| 15 | 2 | 1 | 55 | 0x0000 |
| 16 | 1 | 0 | 145 | 0x0000 |
| 16 | 2 | 1 | 110 | 0x0200 |
| 17 | 1 | 0 | 34 | 0x0000 |
| 17 | 2 | 1 | 200 | 0x0000 |
| 18 | 1 | 0 | 100 | 0x0000 |
| 18 | 2 | 0 | 250 | 0x0000 |
| 18 | 3 | 1 | 34 | 0x0010 |
| 19 | 1 | 0 | 90 | 0x0800 |
| 19 | 2 | 1 | 150 | 0x0800 |
| 20 | 1 | 0 | 40 | 0x0000 |
| 20 | 2 | 1 | 450 | 0x0000 |
| 21 | 1 | 0 | 90 | 0x0800 |
| 21 | 2 | 1 | 150 | 0x0800 |
| 22 | 1 | 0 | 200 | 0x0000 |
| 22 | 2 | 1 | 100 | 0x0000 |
| 23 | 1 | 0 | 100 | 0x0000 |
| 23 | 0 | 1 | 250 | 0x0000 |
| 23 | 2 | 1 | 40 | 0x0000 |
| 24 | 3 | 1 | 250 | 0x0002 |
| 24 | 1 | 0 | 200 | 0x0000 |
| 24 | 2 | 0 | 50 | 0x0080 |
| 25 | 1 | 0 | 100 | 0x0000 |
| 25 | 2 | 1 | 40 | 0x0000 |
| 26 | 1 | 0 | 125 | 0x0000 |
| 26 | 2 | 1 | 180 | 0x0000 |
| 27 | 1 | 0 | 185 | 0x0800 |
| 27 | 2 | 1 | 50 | 0x0000 |
| 28 | 1 | 0 | 100 | 0x0000 |
| 28 | 2 | 1 | 105 | 0x0000 |
| 29 | 1 | 0 | 250 | 0x0000 |

Which `.SHP` a shape index uses is chosen by `loadMonsterShapes` and was not joined. At most 30 live monsters, from `monsters.gd` `MAX_MONSTERS`.
