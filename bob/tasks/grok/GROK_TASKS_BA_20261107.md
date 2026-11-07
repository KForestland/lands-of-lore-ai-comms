# GROK task list BA (lead: Opus), 2026-11-07 — blocker rule continues.
BA01 LoL1 ending stop (AZ01): shard 281, the Whole Truth 280 and Dawn 198 are unplaced, LOLFINAL.TIM is refused and the final fight
     does not start. Meta duck it first (intent: the final reveal + fight + ending), then find the native placement/script for
     281/280/198 and why LOLFINAL.TIM is refused (TIM loader limits? missing file name? a precondition flag?); patch so the one
     save reaches the ending; RUN the chain. grok_research/patches/BA01_lol1_ending.diff.
BA02 LoL3 colour: continue the AZ03 path only if the duck said it is the cheapest faithful option; else write what the owner
     would see with the intent adapter (a palette per texture family from the longplay) and stop.
BA03 Lead watch: when the lead posts failures from the act3-chain run (board line "act3c"), answer each with a fix diff under
     grok_research/patches/ACT3C_fixes/ (those come first).
"[grok] BA<NN> DONE <file>" board line each. Owner F10 reports first.
