# BG04 — ending beats in seconds

Base `c9295da`, after BF01–BF07 and BG00a through BG03. Patch `patches/ACT3P2/BG04_ending_seconds.patch`. Not applied to the live tree.

One blow with the blue bow, the Dark Sword, or the horn still starts the same flag. Luther is not moved. Each following beat waits two seconds: chasm, vow, slump, Dawn, Draracle, vanish, then `game_finished`. A dark chasm prop appears with the chasm. The flag is part of the finale save. A credits stub reads "The game is finished." after the last card. `SCENE_NAME` stays `ending-adapter`. e224e.vqa is not in the movie table and was not played.

Printed on display :3:

`PASS l20_finale_test: three weapons, ending adapter, Luther stays`

`PASS earned final fight: the beats take seconds, the chasm prop shows, and the finished flag keeps the credits`
