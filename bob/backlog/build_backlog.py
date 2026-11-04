#!/usr/bin/env python3
"""Build the LoL2 MASTER BACKLOG (owner 2026-11-01: "pre-plan, have 1000 tasks and just run through them").

Sources (read only): grok backlog 10 reports (route, spells, creatures, NPCs), the item census (170 definitions),
the owner's bugs/complaints reference, the deviations pieces (adapters to revisit), the unregistered tests, and the
lead's fixed lists (Act 1 leftovers, kit, infrastructure). Output: backlog.json (machine) + BACKLOG.md (view).
Statuses already set in an existing backlog.json are kept (by id), so rebuilding never loses claims or done marks.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
G = Path('~/AI_COMMS/grok_backlog_20261028/backlog_20261031I')
R12W = Path('~/opus_work/lol2_r14')  # current integrated tree (was lol2_r12w, archived)
CENSUS = Path('~/AI_COMMS/act1_completion_20261017/item_census.json')
BUGS = Path('~/AI_COMMS/reference_hintbook/Lands_of_Lore_Bugs_and_Complaints_AI_Reference.md')

ACCEPT = {
    'STORY': 'Player does the step in the production scene via the semantic interaction path; inventory/world change persists over save/reload; '
             'wrong item / full inventory refused without loss; joins the earned route test; one owner (act2_quest_ownership.json).',
    'MECH': 'Built on the MECHANISM TRANSACTION API (offer/occupy/commit/retrieve/refuse); headless test incl. refusal and save/reload; '
            'visual/collision restored from committed state.',
    'ITEM': 'Effect from Prima/Brady (page cited) or a decode; routed through item_handlers.gd; focused headless test for use/equip/on-hit; '
            'no invented magnitude (unknown numbers = logged adapter with a source or left out).',
    'SPELL': 'Effect, cost and learning source from Prima/Brady (pages); castable from the spell UI; focused test; numbers from a source or a logged adapter.',
    'CREATURE': 'Stats/behaviour from Brady/Prima (pages) or the decoded template; placed hosts use them; spawn/combat test.',
    'NPC': 'Encounter sequence (prerequisite -> interaction -> one-time consequence -> resume) with the friendly/hostile/following flag; save/reload test.',
    'BUG': 'Original bug fixed in both editions (owner rule) with a DEVIATIONS piece; regression test reproduces the original failure condition.',
    'ACT1': 'Owner-reported Act 1 gap fixed; test at the owner coordinates; F10/playtest confirms.',
    'TEST': 'Test runs in a suite (registry file) or is retired with a reason; no deletion.',
    'INFRA': 'Done-when of the workflow plan item is met and posted.',
    'REVIEW': 'Adapter re-checked against a book/longplay/oracle source: keep (cite), replace by the known behaviour, or flag for the owner.',
    'AUDIT': 'Ordered steps for the area written as STORY tasks (pages, prerequisites, consequences); joins the route graph.',
}


def T(id, type, area, title, source='', lane='any', prio=2, depends=(), phase='story'):
    return {'id': id, 'type': type, 'area': area, 'title': title.strip(), 'source': source, 'lane': lane, 'priority': prio,
            'depends': list(depends), 'phase': phase, 'acceptance': ACCEPT[type], 'status': 'todo', 'claimed_by': '', 'note': ''}


def section(text, head):
    m = re.search(r'^## ' + re.escape(head) + r'.*?$(.*?)(?=^## |\Z)', text, re.M | re.S)
    return m.group(1) if m else ''


def story_tasks():
    out, text = [], (G / 'item1_act23_route/REPORT.md').read_text(errors='replace')
    area, prev = '?', None
    for line in section(text, 'Ordered route').splitlines():
        h = re.match(r'^### (.*)', line)
        if h:
            a = re.search(r'\((L\d+_[A-Z]{2})\)', h.group(1))
            area = a.group(1) if a else h.group(1).strip()[:40]
            continue
        m = re.match(r'^(\d+)\. (.*)', line)
        if m:
            n, body = int(m.group(1)), m.group(2)
            pages = ', '.join(re.findall(r'\((\d[\d,–\- ]*)\)', body)[-1:])
            tid = f'STORY-{n:03d}'
            out.append(T(tid, 'STORY', area, body[:220], f'Prima p.{pages} (grok b10 item1)', 'astra', 1, [prev] if prev else [], 'story'))
            prev = tid
    for a in ('L12_CM', 'L13_RC', 'L14_HT', 'L16_CA', 'L17_HC', 'L19_BC', 'L20_BB'):
        if not any(t['area'] == a for t in out):
            out.append(T(f'AUDIT-{a}', 'AUDIT', a, f'Write the ordered STORY steps for {a} from Prima + Brady (maps and answers)', 'Prima ch.11-14, Brady ch.7-9', 'grok', 1))
    return out


def item_tasks():
    c = json.loads(CENSUS.read_text())
    out = []
    for d in c['definitions']:
        if 152 <= d['index'] <= 156: continue  # ghost rows (spell/projectile placeholders)
        h = d.get('handler') or 0
        out.append(T(f'ITEM-{d["index"]:03d}', 'ITEM', 'items', f'{d["name"]}: effect/use/equip as the books describe (handler {h})',
                     'item_census.json; grok b10 item3; Brady ch.2 p29+', 'fable', 2, [], 'items'))
    return out


def spell_tasks():
    out, text = [], (G / 'item4_spells/REPORT.md').read_text(errors='replace')
    group = '?'
    for line in section(text, 'Thirty spells').splitlines():
        h = re.match(r'^### (.*)', line)
        if h: group = h.group(1).strip(); continue
        m = re.match(r'^- Level (\d), ([^:]+):', line)
        if m:
            out.append(T(f'SPELL-{group[:6].upper().replace(" ", "")}-{m.group(1)}', 'SPELL', 'spells', f'{group} L{m.group(1)} {m.group(2)}',
                         'grok b10 item4; Brady ch.3 p45', 'fable', 2, [], 'items'))
    return out


def creature_tasks():
    out, text = [], (G / 'item6_creatures/REPORT.md').read_text(errors='replace')
    for i, line in enumerate(re.findall(r'^- ([^:]{3,70}):', section(text, 'Creatures'), re.M)):
        out.append(T(f'CREATURE-{i+1:03d}', 'CREATURE', 'creatures', line, 'grok b10 item6; Brady', 'any', 3, [], 'rpg'))
    return out


def npc_tasks():
    out, text = [], (G / 'item7_npcs/REPORT.md').read_text(errors='replace')
    for name in re.findall(r'^## (.+)$', text, re.M):
        if name.strip().lower() in ('page map', 'open', 'sources'): continue
        slug = re.sub(r'[^A-Z0-9]+', '', name.upper())[:14]
        prio = 1 if 'bacatta' in name.lower() or 'baccata' in name.lower() else 3
        out.append(T(f'NPC-{slug}', 'NPC', 'dialog', f'{name.strip()}: encounters, flags and dialog order', 'grok b10 item7', 'any', prio, [], 'dialog'))
    return out


def bug_tasks():
    text = BUGS.read_text(errors='replace')
    lol2 = text.split('## Lands of Lore 2')[1].split('\n## ')[0] if '## Lands of Lore 2' in text else ''
    out = []
    for i, title in enumerate(re.findall(r'^- \*\*(.+?)\*\*', lol2, re.M)):
        out.append(T(f'BUG-{i+1:03d}', 'BUG', 'bugs', f'Original bug: {title}', 'owner bugs/complaints reference', 'any', 2, [], 'small'))
    return out


def act1_tasks():
    items = [
        ('HIVE-FLUTE-SUMMON', 'Hive flute summons the lift from the pit lip (owner 10-26-06 at region 225; Prima 77)', 'lead', 1, []),
        ('HIVE-FLUTE-FLOOR', 'Hive oily-floor slot: the flute slides the green floor over the oil (Prima 78, 81; Brady 160/170) — first caller of the mechanism transaction; ROOM NOT YET LOCATED (no oil material in the export; find it in the longplay or by a walk)', 'lead', 1, ['KIT-API']),
        ('HIVE-LIFT-BRIDGE', 'Hive bridge extends when the lift arrives (owner 10-26-38; Prima 77)', 'lead', 1, ['KIT-API']),
        ('HIVE-DOOR', 'Hive door opens (owner 10-26-54; cat pedestals Prima 79-80)', 'fable', 1, ['KIT-API']),
        ('HIVE-PUZZLE', 'Hive puzzle at (-3505,7100) works (owner 10-30-07; walk Prima 79-80 at the coordinate first)', 'fable', 1, []),
        ('HIVE-ROCK-TRAP', 'Hive rock trap triggers (owner 10-31-19; Prima 80-81 two-boulder room)', 'fable', 1, []),
        ('HIVE-TRAPS', 'Hive flying knives active and shatter (owner 10-32-45; Prima 78)', 'fable', 1, []),
        ('HIVE-GAS', 'Hive gas moves (owner 09-46-09)', 'any', 3, []),
        ('DH-CLOSING-WALLS', 'Dark Halls walls close when walking forward; bookcases move on button/E (owner)', 'any', 2, []),
        ('CAVE-KENNETH-WALL', 'Cave: Kenneth lowers the wall, not the gates', 'any', 2, []),
        ('CAVE-BRIDGE-LEVER', 'Cave: the lever at the bridge', 'any', 2, []),
        ('CAVE-TWO-GUARDS', 'Cave: the 2 guards at the bridge after the sound clip', 'any', 2, []),
        ('CAVE-BOXES', 'Cave: boxes can be moved and stacked', 'any', 3, []),
        ('MUSEUM-DRAGON-CLICK', 'Museum: dragon click point before the dragon movie (owner 09-28-19)', 'any', 2, []),
        ('MUSEUM-DUST', 'Museum: dust prop in the ceiling', 'any', 3, []),
        ('JUNGLE-BACATTA', 'Bacatta friendly and leading after the Jungle (owner bug; build from known behaviour)', 'any', 1, []),
        ('JUNGLE-VILLAGE-DIALOG', 'Huline village dialogue (thieves password man, cat guy animation)', 'any', 2, []),
        ('JUNGLE-TAR-POISON-BRAMBLE', 'Jungle: tar ignition, cub poison gland, bramble burn/regrow', 'any', 2, []),
        ('LIZARD-DROWN-ALL', 'Lizard drowns in deep water in every area (owner-confirmed)', 'fable', 2, []),
        ('ITEMS-HALF2-PICKUP', 'E pickup of the items-half-2 rows works in the rendered run (area_world_items_live_test)', 'fable', 1, []),
        ('ATLAS-ZOOM', 'Atlas wheel-zoom anchor (museum/jungle_interface tests)', 'any', 3, []),
        ('LIGHTING-ACT1', 'Act 1 lighting: Cave O key, torch flicker, Museum/Jungle lights, mushrooms, ceiling cracks', 'any', 3, []),
    ]
    return [T(i, 'ACT1', 'act1', t, 'owner playtests / PLAN_ACT2_3 phase E', l, p, d, 'story') for i, t, l, p, d in items]


def kit_and_infra():
    out = [T('KIT-API', 'MECH', 'kit', 'Mechanism transaction API (offer/occupy/commit/retrieve/refuse), saved with receipts', 'ROADMAP_20261101 round 2', 'lead', 1),
           T('KIT-CHARGER', 'MECH', 'kit', 'Globe charger (insert -> occupied -> retrieve once) for L10/L9', 'astra round 2', 'astra', 1, ['KIT-API']),
           T('KIT-RECEPTACLES', 'MECH', 'kit', 'Keyed receptacles / multi-input doors (emperor boxes, cat pedestals)', 'roadmap', 'astra', 2, ['KIT-API']),
           T('KIT-INTERACT', 'MECH', 'kit', 'One semantic interaction path (target + offered item/spell + form) for input and headless tests (W15)', 'WORKFLOW_PLAN_2', 'fable', 1),
           T('KIT-NPCFLAG', 'NPC', 'kit', 'Thin NPC flag friendly/hostile/following + encounter sequencing', 'roadmap', 'any', 1),
           T('KIT-QUESTSTORE', 'MECH', 'kit', 'Quest/inventory transactions + versioned persistence (W24)', 'roadmap', 'lead', 1),
           T('AUDIT-BRANCHES', 'AUDIT', 'branches', 'Map EVERY good/evil choice and branch: each soul +/- action (who, where, how much), every scene/NPC that changes with the soul value (evil Dawn in the blood bowl room, the real Draracle when evil, ...), and every ending; as a branch graph joined to the STORY steps', 'Brady (search good/evil; text lines ~5717/5996/6208 of brady_guide.txt), Prima ch.14 endings, existing soul decodes (Rix, Dark Halls)', 'grok', 1),
           T('SOUL-SYSTEM', 'MECH', 'kit', 'Soul (good/evil) meter as one saved value with the known +/- events, readable by every host and by branch conditions; Journal shows nothing the original hides', 'AUDIT-BRANCHES; existing soul code', 'any', 1, ['AUDIT-BRANCHES']),
           T('BRANCH-STEPS', 'AUDIT', 'branches', 'Turn the branch graph into STORY-BRANCH tasks (one per alternative scene/NPC/outcome) and add them to the backlog generator', 'AUDIT-BRANCHES', 'lead', 1, ['AUDIT-BRANCHES']),
           T('ENDINGS', 'STORY', 'L20_BB', 'All endings (good/evil variants) as the books and the original describe them, chosen by the soul value and the final choices', 'Brady finale, Prima ch.14', 'any', 2, ['AUDIT-BRANCHES', 'SOUL-SYSTEM']),
           T('ORACLE-SOUL-CUTOFF', 'AUDIT', 'branches', 'DOSBox oracle: the GV_LUTHERS_SOUL value(s) that choose evil Dawn vs good Dawn and the real vs spectral Draracle (read the compare where those groups branch; one watch per branch, an Act 3 save near the lab: $L_H____/AUTOSAV per SAVES_MAP.md)', 'branch_graph.md; oracle_prep_20261031', 'grok', 1),
           T('MAP-V2', 'INFRA', 'maps', 'Annotated maps v2: split multi-storey levels by floor band (one image per storey), label exits/transitions, link markers to backlog task ids', 'MAPS/README.md', 'lead', 2),
           *[T(f'MAP-MARK-{lv}', 'AUDIT', lv, f'Mark {lv}: put every Brady/Prima map point (puzzles, NPCs, items, story steps, the original bugs) into MAPS/{lv}/markers.json by joining the Brady map page to our map; note anything that has no matching geometry', 'MAPS/brady_maps + Prima/Brady text', 'grok' if lv not in ('L1_DC','L3_DH','L4_HJ','L5_HC','L7_DH') else 'any', 1 if lv in ('L5_HC','L10_DC','L9_DR','L8_SJ') else 2) for lv in ('L1_DC','L3_DH','L4_HJ','L5_HC','L7_DH','L8_SJ','L9_DR','L10_DC','L12_CM','L13_RC','L14_HT','L16_CA','L17_HC','L19_BC','L20_BB')],
           T('ROUTE-TEST', 'STORY', 'L8_SJ', 'act2_silverleaf_earned_loop_test (milestone 1)', 'astra round 2', 'astra', 1, ['STORY-027'])]
    for w, t, l in (('W14', 'Sharded test runs (own user dirs per shard)', 'fable'), ('W15', 'Semantic interaction commands + smaller rendered suite', 'fable'),
                    ('W17', 'Lane continuation (owner decision) + task leases', 'lead'), ('W24', 'Save versioning + migration test', 'fable')):
        out.append(T(f'INFRA-{w}', 'INFRA', 'workflow', t, 'WORKFLOW_PLAN_2_20261101', l, 2))
    unreg = R12W / 'tests/registry/_unregistered.txt'
    for n in [l.strip() for l in unreg.read_text().splitlines() if l.strip() and not l.startswith('#')]:
        out.append(T(f'TEST-{n}', 'TEST', 'tests', f'{n}: join a suite or retire with a reason', '_unregistered.txt', 'any', 3, [], 'small'))
    for p in sorted((R12W / 'docs/deviations').glob('*-row-*.md')):
        row = p.read_text(errors='replace').strip()
        cells = [c.strip() for c in row.split('|')]
        if len(cells) > 3 and 'approved' not in row.lower():
            out.append(T(f'REVIEW-{p.stem[:40]}', 'REVIEW', cells[2][:30] if len(cells) > 2 else '?', f'{cells[3][:160]}', f'docs/deviations/{p.name}', 'any', 3, [], 'small'))
    return out


def branch_tasks():
    out, md = [], Path('~/AI_COMMS/review_20261101/branch_graph.md')
    js = Path('~/AI_COMMS/review_20261101/branch_graph.json')
    if not md.exists(): return out
    for line in md.read_text(errors='replace').splitlines():
        m = re.match(r'^\| (BRANCH-\d+[a-z]?) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|', line)
        if m:
            bid, pre, act, con, joins, pages = m.groups()
            deps = [d for d in re.findall(r'STORY-\d{3}', joins)][:1]
            out.append(T(bid, 'STORY', 'branches', f'{act} -> {con} (if: {pre})', f'{pages} (grok branch_graph.md)', 'any', 1, ['SOUL-SYSTEM'], 'story'))
    if js.exists():
        rows = json.loads(js.read_text()).get('rows', [])
        by = {}
        for r in rows: by.setdefault(r['level'], []).append(r)
        for lv, rs in sorted(by.items()):
            deltas = ', '.join(f"{r['delta']:+d} g{r['group']}" for r in rs[:12]) + (' ...' if len(rs) > 12 else '')
            out.append(T(f'SOUL-ADDS-{lv}', 'MECH', lv, f'Host the {len(rs)} native soul changes of {lv} (opcode 206, global 0) so the soul value moves as in the original: {deltas}', 'grok branch_graph.json', 'any', 2, ['SOUL-SYSTEM'], 'story'))
    out.append(T('ROUTE-TEST-GOOD', 'STORY', 'branches', 'Good playthrough test: the good-Dawn Ruby (BRANCH-04) then the dispelled spectral Draracle (BRANCH-06a), soul value earned, not seeded', 'branch_graph.md', 'any', 1, ['BRANCH-04', 'BRANCH-06a']))
    out.append(T('ROUTE-TEST-EVIL', 'STORY', 'branches', 'Evil playthrough test: evil Dawn in the blood bowl room (BRANCH-03) then the real Draracle (BRANCH-06b), soul value earned, not seeded', 'branch_graph.md', 'any', 1, ['BRANCH-03', 'BRANCH-06b']))
    return out


def main():
    # WARNING (lead 2026-11-04): main() rebuilds from generators and DROPS hand-added tasks (CITADEL-*, ENGINE-*, CLEANUP-* ...). Do not run without merging them first.
    tasks = story_tasks() + branch_tasks() + kit_and_infra() + act1_tasks() + item_tasks() + spell_tasks() + creature_tasks() + npc_tasks() + bug_tasks()
    ids = [t['id'] for t in tasks]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup: sys.exit(f'duplicate ids: {sorted(dup)[:10]}')
    old = HERE / 'backlog.json'
    if old.exists():
        prev = {t['id']: t for t in json.loads(old.read_text())['tasks']}
        for t in tasks:
            if t['id'] in prev:
                for k in ('status', 'claimed_by', 'note'): t[k] = prev[t['id']][k]
    tasks.sort(key=lambda t: (t['priority'], t['phase'] != 'story', t['id']))
    (HERE / 'backlog.json').write_text(json.dumps({'version': 1, 'tasks': tasks}, indent=1))
    by = {}
    for t in tasks: by.setdefault(t['type'], 0); by[t['type']] += 1
    lines = ['# LoL2 MASTER BACKLOG (generated by build_backlog.py — do not edit by hand; use backlog.py)', '',
             f'{len(tasks)} tasks: ' + ', '.join(f'{k} {v}' for k, v in sorted(by.items())), '',
             'Lanes: `python3 ~/AI_COMMS/BACKLOG/backlog.py next --lane LANE` then `claim ID LANE`, work, `done ID LANE "receipt"`.', '',
             '| P | ID | Type | Area | Lane | Status | Title | Source |', '|---|---|---|---|---|---|---|---|']
    for t in tasks:
        lines.append(f"| {t['priority']} | {t['id']} | {t['type']} | {t['area']} | {t['lane']} | {t['status']}{(' ' + t['claimed_by']) if t['claimed_by'] else ''} | {t['title'][:110]} | {t['source'][:50]} |")
    (HERE / 'BACKLOG.md').write_text('\n'.join(lines) + '\n')
    print(f'{len(tasks)} tasks', by)


if __name__ == '__main__':
    main()
