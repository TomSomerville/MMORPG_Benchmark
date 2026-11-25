#!/usr/bin/env python3
"""Builds docs/15-asset-manifest/ : one row per asset, in order of first appearance.

Usage:  python tools/doc-generators/asset_manifest.py [repo root]

Reads the art lists (docs/10-art), the creature, spell, encounter and spoken-line data
(docs/12-data), the zone, class and profession documents and the world layout. Writes
Markdown files split by level band, an index, and asset-manifest.csv.
This is a document generator, not game code.
"""
import csv, os, re, sys
from collections import OrderedDict, defaultdict

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
OUT = os.path.join(ROOT, 'docs', '15-asset-manifest')


# ----------------------------------------------------------------------------- helpers
def rd(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
        return f.read()


def clean(s):
    s = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', s)
    s = s.replace('**', '').replace('`', '')
    s = re.sub(r'(?<![\w*])\*([^*]+)\*(?![\w*])', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def table(rel):
    """Yield (h1, h2, h3, cells) for each table body row of a Markdown file."""
    h1 = h2 = h3 = ''
    for line in rd(rel).splitlines():
        if line.startswith('# '):
            h1, h2, h3 = line[2:].strip(), '', ''
        elif line.startswith('## '):
            h2, h3 = line[3:].strip(), ''
        elif line.startswith('### '):
            h3 = line[4:].strip()
        elif line.startswith('|'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if all(re.fullmatch(r':?-+:?', c) for c in cells):
                continue
            yield h1, h2, h3, cells


def split_top(s, seps):
    out, depth, cur, i = [], 0, '', 0
    while i < len(s):
        ch = s[i]
        if ch in '([':
            depth += 1
        elif ch in ')]':
            depth = max(0, depth - 1)
        if depth == 0:
            hit = next((sep for sep in seps if s.startswith(sep, i)), None)
            if hit:
                out.append(cur.strip())
                cur = ''
                i += len(hit)
                continue
        cur += ch
        i += 1
    out.append(cur.strip())
    return [x for x in out if x]


SCHOOLS7 = ['Physical', 'Holy', 'Nature', 'Arcane', 'Fire', 'Frost', 'Shadow']
SCHOOLS6 = SCHOOLS7[1:]
SCHOOL_LOOK = {
    'Physical': 'white steel flash and red; slash arcs, sparks, dust',
    'Holy': 'gold and warm white; sunbursts, flame-halos, feathers of light',
    'Nature': 'leaf green and amber; leaves, vines, thorns, pollen, green-white lightning',
    'Arcane': 'violet and silver-blue; stars, constellations, moon discs',
    'Fire': 'orange and ember red; flame, cinders, smoke',
    'Frost': 'pale blue and white; ice shards, mist',
    'Shadow': 'purple-black with a violet rim; cracks, voids, inward-falling motes',
}
BODIES = ['Human male', 'Human female', 'Dwarf male', 'Dwarf female']
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
AXES = {
    'schools': SCHOOLS7, 'team colours': ['red', 'blue', 'yellow'], 'teams': ['red', 'blue', 'yellow'],
    'bodies': BODIES, 'sizes': ['small', 'medium', 'large', 'huge', 'colossal'],
}


def mult(el):
    """Expand 'X ×3', 'X ×3 (a, b, c)', 'X ×7 schools' into separate names."""
    m = re.search(r'\s*×\s*(\d+)\s*(schools|team colours|teams|bodies|sizes|tiers|colours|tints|var|variants|states|biomes)?', el)
    if not m:
        return [el]
    n, axis = int(m.group(1)), m.group(2)
    base = (el[:m.start()] + ' ' + el[m.end():]).strip(' ,')
    base = re.sub(r'\s+', ' ', base)
    pm = re.search(r'\(([^()]*)\)', base)
    if pm:
        opts = [o.strip() for o in re.split(r',|;', pm.group(1)) if o.strip()]
        if len(opts) == n:
            stem = (base[:pm.start()] + base[pm.end():]).strip(' ,')
            return [f'{stem}: {o}' for o in opts]
    if axis in AXES:
        return [f'{base}: {v}' for v in AXES[axis][:n]]
    if axis == 'tiers':
        return [f'{base}, tier {i + 1}' for i in range(n)]
    return [f'{base} {LETTERS[i]}' if n <= 26 else f'{base} {i + 1}' for i in range(n)]


def slash(el):
    """'Tunnel straight/bend/T/ramp' -> four names. Only for tokens joined by '/' with no spaces."""
    toks = el.split(' ')
    for i, t in enumerate(toks):
        if '/' in t and not t.startswith('(') and len(t) > 2:
            return [' '.join(toks[:i] + [o] + toks[i + 1:]) for o in t.split('/') if o]
    return [el]


def spaced_slash(el):
    """'Light / Medium / Heavy Leather' -> three names (shared prefix and suffix kept)."""
    if ' / ' not in el:
        return [el]
    parts = [p.strip() for p in el.split(' / ')]
    first, last = parts[0].split(' '), parts[-1].split(' ')
    prefix, suffix = ' '.join(first[:-1]), ' '.join(last[1:])
    opts = [first[-1]] + [p for p in parts[1:-1]] + [last[0]]
    return [' '.join(x for x in (prefix, o, suffix) if x) for o in opts]


def expand(text, seps=(', ', '; ', ' · '), do_slash=False):
    out = []
    for el in split_top(text, seps):
        for a in mult(el):
            out += slash(a) if do_slash else [a]
    return [x.strip(' .') for x in out if x.strip(' .')]


def slug(s):
    s = clean(s).lower()
    s = re.sub(r"[’']", '', s)
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:48]


# ----------------------------------------------------------------------------- zones
# code: (name, low level, order, palette, culture)
ZONES = OrderedDict([
    ('CORE', ('Before the world (login, character creation)', 0, 0, '', '')),
    ('ANY', ('Any zone', 1, 1, '', '')),
    ('BM', ('Brightmead Vale', 1, 2, 'spring green and warm gold', 'human rural: timber frame and thatch')),
    ('ST', ('Stonewake Dale', 1, 3, 'fresh green and grey stone', 'hill dwarf: low, rounded, turf roofs, dry-stone walls')),
    ('SOL', ('Solhaven', 5, 4, 'white stone, royal blue and gold', 'human city: tall, arched, pointed roofs, banners')),
    ('HAM', ('Hammerdeep', 5, 5, 'dark grey stone, iron, ember orange and brass', 'mountain dwarf: square, heavy, angular knotwork')),
    ('SEA', ('The ship crossing', 5, 6, 'sea blue-grey and sail white', '')),
    ('HF', ('Harrowfield', 5, 7, 'wheat gold and rust', 'human rural')),
    ('RW', ('Russetwood', 5, 8, 'copper, red and gold', 'human rural, woodland')),
    ('EC', ('Embercrag Hollow', 5, 9, 'snow blue-white and ember orange', 'mountain dwarf: dark carved stone, iron, brass')),
    ('SD', ('Stoneheart Deeps', 5, 10, 'lamp gold on deep teal dark, glowcap cyan', 'mountain dwarf, underground')),
    ('TM', ('Thornwick Marches', 10, 11, 'desaturated olive and grey-violet', 'human town, dark forest and marsh')),
    ('IR', ('Ironroot Highlands', 10, 12, 'pine green and cold grey', 'mountain dwarf keep-town; hill dwarf steadings')),
    ('CR', ('Crownfall (battleground)', 10, 13, 'pale marble and tarnished brass with red, blue and yellow team dressing', 'imperial ruin')),
    ('GC', ('Gallowmere Crypts (dungeon)', 13, 14, 'ash grey, soot black and brand-orange glow', 'old masonry crypt, Cinderbrand cult')),
    ('CF', ('Cinderfall Barrens', 20, 15, 'black, sulphur yellow and lava orange', 'mountain dwarf fort; Slagborn black iron')),
    ('RL', ('The Riftlands', 20, 16, 'dust ochre and bleached sky', 'mesa town adobe; imperial ruin pale marble and brass')),
    ('VM', ('Veilmoor', 20, 17, 'fog grey-green with lantern gold', 'human town; gothic keep')),
    ('SW', ('The Slagworks (dungeon)', 20, 18, 'black iron, soot and molten slag orange', 'Slagborn forge-works')),
    ('DP', ('The Dustpit (arena)', 24, 19, 'dust ochre and arena sand', 'mesa town')),
    ('HK', ('Hollowspire Keep (dungeon)', 27, 20, 'black, desaturated violet and cold white light', 'gothic keep; the Hollow')),
    ('HT', ('The Hollow Throne (raid)', 30, 21, 'pale marble, tarnished brass and arcane violet', 'buried imperial city')),
    ('WB', ('World bosses', 30, 22, '', '')),
])
ZNAME = {v[0]: k for k, v in ZONES.items()}
ZS = {k: re.sub(r'^The ', 'the ', re.sub(r'\s*\(.*?\)', '', v[0])) for k, v in ZONES.items()}


def zcue(code):
    name, _, _, pal, cul = ZONES[code]
    if code in ('CORE', 'ANY', 'WB'):
        return ''
    bits = [f'Setting: {ZS[code]}']
    if pal:
        bits.append(f'palette {pal}')
    if cul:
        bits.append(cul)
    return '; '.join(bits) + '.'


HINTS = [(re.compile(p), z, l) for p, z, l in [
    (r'Gallowmere Crypts|Crypts\b', 'GC', 13), (r'The Slagworks|Slagworks', 'SW', 20),
    (r'Hollowspire Keep', 'HK', 27), (r'Hollow Throne|[Rr]aid\b', 'HT', 30), (r'Crownfall|battleground', 'CR', 10),
    (r'[Ww]orld.boss', 'WB', 30), (r'Dustpit|Pitmaster', 'DP', 24),
    (r'Larkhill', 'BM', 1), (r'Millbrook', 'BM', 3), (r'Hartwell', 'BM', 2), (r'Greenhollow', 'BM', 3),
    (r'Silverrun', 'BM', 4), (r'Ashhand', 'BM', 3), (r'Burned Mill|The Mill\b|Cray', 'BM', 4), (r'Brightmead', 'BM', 1),
    (r'Coldhearth', 'EC', 5), (r'Anvilrest', 'EC', 5), (r'Old Forge', 'EC', 7), (r'Kiln Cave', 'EC', 7),
    (r'Rimewater', 'EC', 8), (r'Gravelkin Warrens|[Ww]arrens', 'EC', 6), (r'Bouldergate', 'EC', 5), (r'Blackmatch|Slagfall', 'EC', 9), (r'Embercrag', 'EC', 5),
    (r'Athenaeum', 'SOL', 5), (r'Solhaven', 'SOL', 5),
    (r'Hammerdeep|Mount Khaz|Seagate|Rootvault|Goldring|Thane.s Hall', 'HAM', 5),
    (r'Hearth-Oath|[Ss]ea route|ship crossing', 'SEA', 5),
    (r"Harrow's Cross", 'HF', 5), (r'Fenner', 'HF', 5), (r"Reaver", 'HF', 6), (r'Scarecrow', 'HF', 7),
    (r'Dustwater|quarry', 'HF', 7), (r'Burning Rows', 'HF', 8), (r'Vane\b', 'HF', 9), (r'Longstrand|Tollbridge', 'HF', 8),
    (r'Harrowfield', 'HF', 5),
    (r"Cooper's Hollow", 'RW', 5), (r'Birch', 'RW', 5), (r'[Cc]harcoal', 'RW', 6), (r'High Canopy', 'RW', 7),
    (r'Burning Ride', 'RW', 8), (r'Mossback', 'RW', 8), (r'Great Kiln|Kilnmaster|[Kk]iln worker', 'RW', 9), (r'Russetwood', 'RW', 5),
    (r'Sunbank', 'ST', 1), (r'Hopstead', 'ST', 3), (r'Ridgefold', 'ST', 4), (r'\bSinks\b', 'ST', 2), (r'Old Brewery', 'ST', 4),
    (r'Stonewake Dam', 'ST', 1), (r'Millrace', 'ST', 3), (r'Daleside Adit', 'ST', 4), (r'Rustler', 'ST', 4), (r'Stonewake|Dale\b', 'ST', 1),
    (r'Lanternhold', 'SD', 5), (r'Long Stair', 'SD', 5), (r'Glowcap Grotto', 'SD', 6), (r'Underwarrens', 'SD', 6),
    (r'Cartwright|Trestles', 'SD', 7), (r'Crystal Galleries', 'SD', 8), (r'Shattered Hall', 'SD', 9),
    (r'Undercut|Great Bore', 'SD', 10), (r'Stoneheart|\bDeeps\b', 'SD', 5),
    (r'Thornwick [Cc]emetery|cemetery', 'TM', 11), (r'Hedge-Circle', 'TM', 12), (r'Wolfscar', 'TM', 12),
    (r'Gallowmere', 'TM', 13), (r"Warden's Rest", 'TM', 14), (r'Wickerman', 'TM', 15), (r'Pact Watch', 'TM', 14),
    (r'Mistral Hollow', 'TM', 16), (r'Ashgrave', 'TM', 17), (r'Brandspire', 'TM', 19), (r'Thornwick', 'TM', 10),
    (r'Singing Stones', 'IR', 11), (r'Ramshead', 'IR', 11), (r"Smugglers|Lurker Hollows", 'IR', 12),
    (r'Stonemaw Warcamp', 'IR', 13), (r'Screecher|Rimewing', 'IR', 15), (r'Runefall', 'IR', 16),
    (r'Deepseam', 'IR', 17), (r'Brandforge', 'IR', 18), (r'Ironroot', 'IR', 10),
    (r'Scoria', 'CF', 22), (r'Emberwell', 'CF', 23), (r'Obsidian Run|Sulfur Pools', 'CF', 24),
    (r'Exile Camp|Buried Caravan', 'CF', 25), (r"Pyrraxis' Roost", 'CF', 27), (r'Molten Stair', 'CF', 28),
    (r'Blackanvil', 'CF', 29), (r'Fort Ashwatch|Cinderfall', 'CF', 20),
    (r"Kite's Rest", 'RL', 22), (r'Spoil Heaps', 'RL', 21), (r'Howler', 'RL', 22), (r"Blackspade|Widow's Shaft", 'RL', 25),
    (r'Wyrm Furrows|Echoing Chasm', 'RL', 26), (r'Tor Vael|Spire Camp', 'RL', 27), (r'Maw-Scar', 'RL', 29),
    (r"Dawn's Stand|Causeway|Riftlands|Rift interiors", 'RL', 20),
    (r'Lantern Road', 'VM', 21), (r'Low Tarn', 'VM', 21), (r'Pilgrim', 'VM', 22), (r'[Bb]arrow', 'VM', 24),
    (r'Gloomhollow|Cairn Heights', 'VM', 25), (r"Hangman's Hill|Vigil's End|Blightwatcher", 'VM', 26),
    (r'Hollowspire', 'VM', 27), (r'Lanternwatch|Veilmoor', 'VM', 20),
]]


def locate(text, default=None):
    """Lowest-level place named in the text -> (zone code, level)."""
    work, best = text, None
    for rx, z, l in HINTS:
        if rx.search(work):
            work = rx.sub(' ', work)
            cand = (l, ZONES[z][2], z)
            if best is None or cand < best:
                best = cand
    if best is None:
        return default
    return best[2], best[0]


# ----------------------------------------------------------------------------- lookups
CREAT = {}       # lower name -> (zone, level)
for h1, h2, h3, c in table('docs/12-data/creatures.md'):
    if len(c) > 2 and re.match(r'CRE-[A-Z]{2}-\d+', c[0]):
        zname = h2.split(' — ')[0].strip()
        code = ZNAME.get(zname) or ZNAME.get('The ' + zname)
        nm = re.sub(r'\(.*?\)', '', clean(c[1])).replace('"', '').strip()
        lm = re.search(r'\d+', c[2])
        if not lm or not code:
            continue
        CREAT[nm.lower()] = (code, int(lm.group()))
ENC_ZONE = [('Gallowmere', 'GC', 14), ('Slagworks', 'SW', 21), ('Hollowspire', 'HK', 28), ('Hollow Throne', 'HT', 30), ('World bosses', 'WB', 30)]
for h1, h2, h3, c in table('docs/12-data/encounters.md'):
    z = next(((zc, zl) for key, zc, zl in ENC_ZONE if key in h2), None)
    if z and 'Trash' in h3 and len(c) > 1 and re.fullmatch(r'\d+(–\d+)?', c[1]) and c[0] not in ('Creature',):
        CREAT.setdefault(clean(c[0]).lower(), (z[0], int(re.search(r'\d+', c[1]).group())))
for m in re.finditer(r'^\*\*\d+ — ([^*]+)\*\* \((?:event, )?(\d+)', rd('docs/07-instances/dungeons.md'), re.M):
    pos, nm, lv = m.start(), m.group(1), int(m.group(2))
    head = [h for h in re.finditer(r'^## \d\. (.+?) \(', rd('docs/07-instances/dungeons.md'), re.M) if h.start() < pos][-1].group(1)
    z = locate(head) or ('GC', lv)
    for part in re.split(r' & |, ', nm):
        CREAT[part.strip().lower()] = (z[0], lv)


def creature_k(name):
    key = re.sub(r'\(.*?\)', '', clean(name)).strip().lower()
    if not key:
        return None
    if key in CREAT:
        return key, CREAT[key]
    words = key.split()
    hits = [(len(k), k) for k in CREAT if k.endswith(' ' + key) or k.startswith(key + ' ') or (len(words) > 1 and all(w in k.split() for w in words))]
    if hits:
        k = min(hits)[1]
        return k, CREAT[k]
    hits = [(-len(k), k) for k in CREAT if len(k) > 7 and ' ' in k and k in key]
    if hits:
        k = min(hits)[1]
        return k, CREAT[k]
    return None


def creature(name):
    r = creature_k(name)
    return r[1] if r else None


QUEST = {}       # id -> (zone, level, name, objective)
for f in sorted(os.listdir(os.path.join(ROOT, 'docs', '05-zones'))):
    if not f.startswith('t'):
        continue
    for h1, h2, h3, c in table('docs/05-zones/' + f):
        if len(c) > 4 and re.fullmatch(r'[A-Z]{2}-\d+', c[0]) and re.fullmatch(r'\d+', c[2]):
            QUEST[c[0]] = (c[0][:2], int(c[2]), clean(c[1]), clean(c[4]))

ABIL, TAL = {}, {}
cls = ''
for h1, h2, h3, c in table('docs/12-data/spells.md'):
    if h2 in ('Fighter', 'Cleric', 'Druid'):
        cls = h2
    if len(c) > 3 and c[0].startswith('SPL-') and c[3].isdigit():
        ABIL.setdefault(clean(c[1]).lower(), (cls, int(c[3])))
for cname in ('fighter', 'cleric', 'druid'):
    for h1, h2, h3, c in table(f'docs/03-classes/{cname}.md'):
        m = re.match(r'(\d+)( \(\d+\))?$', c[0]) if c else None
        if m and len(c) >= 4 and re.fullmatch(r'\d+', c[2]) and 'alent' in h2:
            tier = int(m.group(1))
            TAL[clean(c[1]).lower()] = (cname.title(), h3.split(' ', 1)[-1], min(30, 10 + 5 * (tier - 1)))


def ability_level(name, default=10):
    key = re.sub(r'\(.*?\)', '', clean(name)).strip().lower()
    if key in ABIL:
        return ABIL[key][1]
    if key in TAL:
        return TAL[key][2]
    for k, v in list(ABIL.items()) + [(k, (v[0], v[2])) for k, v in TAL.items()]:
        if k and (k in key or key in k):
            return v[1]
    return default


# ----------------------------------------------------------------------------- asset store
KIND = OrderedDict([   # kind: (order, pipeline, technical target)
    ('Style bible', (1, 'P01', 'Reference images and data files, frozen before anything else is made')),
    ('Font', (2, 'P20', 'OpenType, Latin Extended; constructed, not licensed')),
    ('UI texture', (3, 'P03', 'Authored at 2x for 4K, 9-slice where it stretches, packed into atlases')),
    ('Painting', (4, 'P04', '2048 px on the long side or larger; painterly, no text')),
    ('Terrain texture', (5, 'P05', '1024 px, tiles seamlessly, colour only; 6 to 8 per zone, blended by weight map')),
    ('Kit atlas', (6, 'P05', '2048 px trim-sheet atlas shared by every piece of one kit')),
    ('Sky preset', (7, 'P09', 'Sky dome texture plus light, fog and colour-grade values')),
    ('Kit piece', (8, 'P11', 'Modular; a whole building is 2 to 8k triangles; shares the kit atlas')),
    ('Building assembly', (9, 'assemble', 'No generation: assembled from kit pieces')),
    ('Set piece', (10, 'P11', 'Built from the named kit where possible; only what the kit lacks is modelled new')),
    ('Nature model', (11, 'P12', 'Trees 300 to 1,500 triangles with leaf cards; rocks 50 to 600; 3 detail levels')),
    ('Water surface', (12, 'P05', 'Tiling surface texture and flow values for the one world shader')),
    ('Prop', (13, 'P10', '50 to 600 triangles; shared 1024 px prop atlas')),
    ('Gathering node', (14, 'P12', 'Full and depleted states; readable at 30 m by its coloured feature')),
    ('Rig', (15, 'P14', 'Skeleton and skin weights; bone names per the rig contract')),
    ('Character model', (16, 'P13', 'Player body 4 to 6k triangles, 1024 px atlas; creature 1.5 to 5k; boss 8 to 12k and 2048 px')),
    ('Hair', (17, 'P21', 'Separate solid painted piece, attached to the head bone or skinned to the head and neck bones; nothing simulated; 300 to 900 triangles')),
    ('Customisation', (18, 'P07', 'Tint, head variant or drawn feature on the body\'s own texture; no new body is generated')),
    ('Skin or outfit', (19, 'P07', '512 to 1024 px on the rig\'s shared layout; mesh variant only where noted')),
    ('Animation', (20, 'P15', 'One clip, on the named rig; loops where it is a loop; contact frames on gameplay timing')),
    ('Armor texture', (21, 'P06', 'One body region on the shared layout that all four bodies use')),
    ('Body geometry swap', (21.5, 'P13', 'Part built into a player body mesh and skinned to its rig; hidden until an item calls for it; no model of its own')),
    ('Armor piece', (22, 'P10', 'Helm or shoulders, attached to a bone; 300 to 600 triangles; one fit per rig')),
    ('Weapon model', (23, 'P10', '300 to 800 triangles; 256 px')),
    ('Effect', (24, 'P08', 'Flipbook sheet up to 1024 px and a particle definition; 150 particles or fewer, 600 for boss effects')),
    ('Icon', (25, 'P02', '128 px source, 64 px shipped; readable at 32 px; no text')),
    ('Music', (26, 'P16', '48 kHz; 1.5 to 3 minutes unless noted; -18 LUFS')),
    ('Ambience', (27, 'P17', '48 kHz; beds loop 60 to 120 s at -24 LUFS; spots are one-shots')),
    ('Sound effect', (28, 'P18', '48 kHz mono for positional sounds; peak-normalised per category')),
    ('Voice line', (29, 'P19', '48 kHz mono; the description is the exact words; it is also the subtitle')),
    ('Quest scene', (30, 'assemble', 'No generation: staged from zone set pieces and quest props')),
    ('Map mask', (31, 'derive', 'No generation: cut from the painted zone map by sub-area polygon')),
])
ASSETS, SEEN = [], defaultdict(int)


def add(aid, kind, name, desc, used, zone, level, source, pipe=None):
    aid = re.sub(r'-+', '-', aid).strip('-.')
    SEEN[aid] += 1
    if SEEN[aid] > 1:
        aid = f'{aid}-{SEEN[aid]}'
    name, desc, used = clean(name), clean(desc), clean(used)
    name = name[0].upper() + name[1:] if name else name
    ASSETS.append(dict(id=aid, kind=kind, pipe=pipe or KIND[kind][1], name=name, desc=desc, used=used,
                       zone=zone, level=int(level), source=source, seq=len(ASSETS)))


# ----------------------------------------------------------------------------- P01 style bible
add('STY-palette', 'Style bible', '32-colour master palette',
    'Eight ramps of four values (shadow, base, light, highlight): warm stone, cool stone, wood, earth, foliage green, autumn orange-red, iron and steel blue-grey, accent gold. Saved as a swatch image and a data file.',
    'Palette lock for every texture', 'CORE', 0, 'Art Direction §4')
for i, a in enumerate(['human rural cottage in a meadow', 'mountain-dwarf hall doorway with braziers', 'hill-dwarf turf-roofed steading',
                       'a wolf and a boar side by side', 'a Fighter, a Cleric and a Druid standing together', 'a sword, a staff and a shield on plain ground',
                       'a forest clearing at dusk with a campfire', 'a gothic ruin in fog with lantern light']):
    add(f'STY-anchor-{i + 1}', 'Style bible', f'Style anchor image {i + 1}: {a}',
        f'Reference painting that fixes the look: {a}. Stylised low-poly forms, hand-painted colour-only surfaces with the light painted in, chunky proportions, strong silhouette, no photographic detail.',
        'Reference image for every generation', 'CORE', 0, 'Art Direction §1')
for b in BODIES:
    add(f'STY-prop-{slug(b)}', 'Style bible', f'Proportion sheet: {b}',
        f'Front, side and back orthographic sheet of the {b.lower()} body at game proportions (human 6.5 heads tall, dwarf 4.5), mitten hands, large feet and forearms.',
        'Reference for characters, armor and NPC outfits', 'CORE', 0, 'Art Direction §2')
for mname in ['timber, pale', 'timber, dark', 'timber, charred', 'plaster', 'thatch', 'slate and tile', 'cut stone, white', 'cut stone, grey',
              'cut stone, dwarven dark', 'rough stone', 'brick', 'turf', 'packed earth', 'cloth, plain', 'cloth, woven', 'cloth, silk',
              'leather, pale', 'leather, dark', 'mail', 'iron', 'bronze and brass', 'gold trim', 'bone', 'bark', 'snow and ice',
              'ash and slag', 'lava (emissive)', 'crystal (emissive)', 'imperial marble']:
    add(f'STY-mat-{slug(mname)}', 'Style bible', f'Material swatch: {mname}',
        f'Tiling hand-painted swatch of {mname}: flat colour areas from the master palette, painted light from above, broad brush grain, no photographic noise.',
        'Material library used by the repaint pass', 'CORE', 0, 'Art Direction §3')
add('STY-adapter', 'Style bible', 'Style adapter', 'Small trained adapter for the image model, made from the anchor images and swatches, if training runs on this hardware.',
    'Holds one look across image pipelines', 'CORE', 0, 'Asset Forge P01')

# ----------------------------------------------------------------------------- list 1: player characters
L1 = 'docs/10-art/01-characters-armor-weapons.md'
RIGS = {'Human': 'CHR-001', 'Dwarf': 'CHR-002'}
add('CHR-001', 'Rig', 'Human rig', 'Skeleton and skin-weight template for human bodies: about 55 bones including fingers as mitten hands, a cloak chain, and sockets for weapon, shield and back.',
    'Both human bodies and every human NPC', 'CORE', 0, 'CHR-001')
add('CHR-002', 'Rig', 'Dwarf rig', 'Skeleton for dwarf bodies with the same bone names as the human rig so animation retargets; own proportions: short legs, broad chest, large hands.',
    'Both dwarf bodies and every dwarf NPC', 'CORE', 0, 'CHR-002')
for i, b in enumerate(BODIES):
    add(f'CHR-00{i + 3}', 'Character model', f'{b} body',
        f'{b} player body: a generated model fitted to the {b.split()[0].lower()} rig, painted bald and clean-shaven in plain underclothes, on the texture layout all four bodies share. '
        f'Hair, facial hair and features are separate pieces, faces are variants of its head, and skin and hair colour are tints. '
        f'Its geometry swaps are built into the mesh and hidden until an item calls for them: lower-body variants (plain legs, short kilt, long robe skirt), cape shapes (short, long, wide), flared sleeves, glove cuffs and boot tops. '
        f'Stylised chunky proportions ({"6.5" if "Human" in b else "4.5"} heads tall), mitten hands. 4 to 6k triangles, one 1024 px texture, one mesh at every distance.',
        'Player characters and NPCs on this body', 'CORE', 0, f'CHR-00{i + 3}')
    add(f'CHR-007-{slug(b)}', 'Customisation', f'Underwear layer: {b}', f'Plain undyed linen underclothes of the {b.lower()} body: part of the body mesh and painted in its texture; the skin tint leaves them alone.',
        'Character with no armor', 'CORE', 0, 'CHR-007')
    add(f'CHR-008-{slug(b)}', 'Character model', f'First-person arms: {b}', f'Forearms and hands of the {b.lower()} body for first-person view, shown only at full zoom-in.',
        'First-person camera', 'ANY', 1, 'CHR-008')
    add(f'CHR-010-{slug(b)}', 'Animation', f'Character-select podium pose: {b}', f'Relaxed idle loop for the {b.lower()} body standing on the character-select screen, weight on one leg, slow look around.',
        'Character select screen', 'CORE', 0, 'CHR-010')

SKIN = {'Human': ['fair', 'light', 'tan', 'olive', 'brown', 'deep brown'],
        'Dwarf': ['Hallborn pale', 'Hallborn ruddy', 'Hallborn ash-pale', 'Dalefolk weathered tan', 'Dalefolk freckled', 'Dalefolk wind-burned brown']}
FACE = ['young, open', 'square-jawed', 'narrow, sharp', 'broad, weathered', 'scarred brow', 'older, lined']
HAIRS = {'Human male': ['cropped', 'short tousled', 'shoulder-length', 'tied back', 'long loose', 'receding', 'shaved sides with top braid', 'bald'],
         'Human female': ['bun', 'single long braid', 'long loose', 'bob', 'ponytail', 'curls', 'short crop', 'tied under a headscarf'],
         'Dwarf male': ['braided crown', 'long twin plaits', 'topknot', 'shaved with one braid', 'wild mane', 'short crop', 'bald', 'ridge of short braids'],
         'Dwarf female': ['twin braids', 'coiled braids', 'one long plait', 'bun', 'loose waves', 'short crop', 'crown braid', 'side braids with rings']}
FACIAL = {'Human male': ['stubble', 'short beard', 'full beard', 'moustache', 'goatee', 'long sideburns'],
          'Human female': ['earrings', 'freckles', 'cheek scar'],
          'Dwarf male': ['Hallborn braided beard, twin', 'Hallborn braided beard, forked', 'Hallborn braided beard with rings', 'Hallborn long plaited beard',
                         'Dalefolk short beard', 'Dalefolk short beard with moustache', 'Dalefolk chin-strap beard', 'Dalefolk bushy sideburns'],
          'Dwarf female': ['beard braids', 'sideburn-plaits', 'ear and nose rings']}
for b in BODIES:
    race = b.split()[0]
    for i, t in enumerate(SKIN[race]):
        add(f'CUS-01-{slug(b)}-{i + 1}', 'Customisation', f'Skin tone {i + 1} ({t}): {b}', f'Skin tone for the {b.lower()} body: a {t} tint of the skin region of the body\'s own texture, laid through the body\'s skin mask so that the eyes, the lips and the underclothes keep their colour; corrected by hand where the plain tint reads wrong.',
            'Character creation option', 'CORE', 0, 'CUS-01')
    for i, t in enumerate(FACE):
        add(f'CUS-02-{slug(b)}-{i + 1}', 'Customisation', f'Face {i + 1} ({t}): {b}', f'Head texture and small mesh morph for the {b.lower()} body: {t} face, painted eyes and brows, readable at game distance.',
            'Character creation option', 'CORE', 0, 'CUS-02')
    for i, t in enumerate(HAIRS[b]):
        add(f'CUS-03-{slug(b)}-{i + 1}', 'Hair', f'Hair style {i + 1} ({t}): {b}', f'The bald style of the {b.lower()} body: the body with no hair piece.' if t == 'bald' else f'Hair piece for the bald {b.lower()} head: {t}. A separate solid painted piece of a few large clumps, grey so the hair colour ramps tint it; a short style is attached to the head bone, a long one is skinned to the head and neck bones. Nothing is simulated.',
            'Character creation option; NPCs', 'CORE', 0, 'CUS-03')
    for i, t in enumerate(FACIAL[b]):
        kind = 'Customisation' if any(w in t for w in ('freckles', 'scar')) else 'Hair' if any(w in t for w in ('beard', 'stubble', 'moustache', 'goatee', 'sideburn', 'plait', 'braid')) else 'Prop'
        add(f'CUS-05-{slug(b)}-{i + 1}', kind, f'Facial feature {i + 1} ({t}): {b}', f'Facial piece for the {b.lower()} head: {t}. Tinted by the hair colour ramp where it is hair.',
            'Character creation option; NPCs', 'CORE', 0, 'CUS-05')
for i, t in enumerate(['black', 'dark brown', 'chestnut', 'auburn', 'red', 'blond', 'grey', 'white']):
    add(f'CUS-04-{i + 1}', 'Customisation', f'Hair colour ramp: {t}', f'Four-step tint ramp (shadow, base, light, highlight) for {t} hair, applied to every hair and facial-hair piece.',
        'Character creation option', 'CORE', 0, 'CUS-04')

ANIM_LEVEL = {'ANM-01': 0, 'ANM-02': 1, 'ANM-03': 1, 'ANM-04': 1, 'ANM-05': 1, 'ANM-06': 1, 'ANM-07': 1, 'ANM-08': 30, 'ANM-09': 1}
ANIM_NOTE = {'ANM-01': 'locomotion', 'ANM-02': 'stance and state', 'ANM-03': 'melee', 'ANM-04': 'ranged', 'ANM-05': 'Fighter special',
             'ANM-06': 'spell casting', 'ANM-07': 'world action', 'ANM-08': 'mounted', 'ANM-09': 'emote'}
for h1, h2, h3, c in table(L1):
    if c and c[0] in ANIM_LEVEL:
        group = c[0]
        for clip in split_top(c[3], [', ']):
            for rig in ('Human', 'Dwarf'):
                lv = ANIM_LEVEL[group]
                if group == 'ANM-07' and re.search(r'Mining|Herb|Skinning|Fishing|Smithing|Crafting', clip):
                    lv = 5
                loop = 'Loops.' if re.search(r'[Ii]dle|Walk|Run|loop|Swim|Strafe|Backpedal|Fall|Sit|Sleep|Stunned|Dead pose|Feared|Channel|Ride', clip) else 'Plays once.'
                add(f'{group}-{rig[0]}-{slug(clip)}', 'Animation', f'{clip} ({rig} rig)',
                    f'Player {ANIM_NOTE[group]} clip "{clip}" on the {rig.lower()} rig{"" if rig == "Human" else ", retargeted from the human clip and corrected for dwarf proportions"}. {loop} Weighty, readable poses; no foot sliding.',
                    f'All {rig.lower()} player characters and NPCs', 'CORE' if lv == 0 else 'ANY', lv, group)

ZONES_T1 = [('BM', 1), ('ST', 1), ('HF', 5), ('RW', 5), ('EC', 5), ('SD', 5)]
ZONES_T3 = [('TM', 10), ('TM', 15), ('IR', 10), ('IR', 15)]
ZONES_T4 = [('CF', 20), ('CF', 25), ('RL', 20), ('RL', 25), ('VM', 20), ('VM', 25)]
REGIONS = ['chest', 'legs', 'feet', 'hands', 'wrist', 'waist']
TIERSET = {}   # (armor type, band) -> set name, for item bindings
for h1, h2, h3, c in table(L1):
    if not c or not c[0].startswith('ARM-') or c[0] == 'ARM-E1':
        continue
    sid, sname, atype, levels, cw, usedby = c[0], clean(c[2]), clean(c[3]), c[4], clean(c[9]), clean(c[10])
    lo = int(re.search(r'\d+', levels).group())
    sets = [(sid, sname, atype)]
    if sid == 'ARM-P1':
        sets = [('ARM-P1F', "Contender's set, Fighter", 'Mail'), ('ARM-P1C', "Contender's set, Cleric", 'Mail'), ('ARM-P1D', "Contender's set, Druid", 'Leather')]
    for sid2, sname2, atype2 in sets:
        zone0 = 'ANY'
        if 'one per level 1–10 zone' in cw:
            ways = [('plain', 'ANY', lo)] + [(ZONES[z][0], z, l) for z, l in ZONES_T1]
        elif 'two per zone' in cw and lo == 10:
            ways = [('plain', 'ANY', lo)] + [(f'{ZONES[z][0]}, {"first" if l % 10 == 0 else "second"} half', z, l) for z, l in ZONES_T3]
        elif 'two per zone' in cw:
            ways = [('plain', 'ANY', lo)] + [(f'{ZONES[z][0]}, {"first" if l % 10 == 0 else "second"} half', z, l) for z, l in ZONES_T4]
        else:
            m = re.search(r'\(([^)]*)\)', cw)
            names = [x.strip() for x in m.group(1).split(',')] if m and 'team' not in m.group(1) else None
            n = int(re.search(r'\d+', cw).group())
            names = names if names and len(names) == n else (['base'] if n == 1 else [f'colourway {LETTERS[i]}' for i in range(n)])
            hz = {'crypt': ('GC', 13), 'slag': ('SW', 20), 'hollow': ('HK', 27)}
            ways = [(nm, hz.get(nm, (locate(usedby, ('ANY', lo))[0], lo))[0], hz.get(nm, (None, lo))[1]) for nm in names]
        # A robe is not a model: the body's robe skirt (a geometry swap, GEO-01) is painted by the set's own region textures.
        robe = sid == 'ARM-T1C' or ('✓' in c[8] and (sid != 'ARM-P1' or sid2 == 'ARM-P1D'))
        skirt = 'tabard-skirt' if sid == 'ARM-T1C' else 'robe skirt'
        for wname, wz, wl in ways:
            pal = f' in the palette of {ZS[wz]} ({ZONES[wz][3]})' if wz not in ('ANY',) and ZONES[wz][3] else ''
            for r in REGIONS:
                add(f'{sid2}-{slug(wname)}-{r}', 'Armor texture', f'{sname2}: {r}, {wname} colourway',
                    f'{atype2} armor texture for the {r} region of the "{sname2}" appearance set, {wname} colourway{pal}. Painted on the shared body layout so it fits all four bodies; seams must be invisible.'
                    + (f' The set is worn with a {skirt}: this region\'s painting carries onto the skirt built into each body, so it must read as one garment from the waist down.' if robe and r in ('chest', 'legs') else ''),
                    f'{usedby}', wz, wl, sid)
        for col, part, fits in ((6, 'helm', ['Human fit', 'Dwarf fit']), (7, 'shoulders', ['Human fit', 'Dwarf fit'])):
            cell = c[col]
            if '✓' in cell:
                note = clean(cell.replace('✓', '')).strip()
                for fit in fits:
                    add(f'{sid2}-{slug(part)}-{slug(fit)}', 'Armor piece', f'{sname2}: {part} ({fit})',
                        f'{part.capitalize()} geometry for the "{sname2}" {atype2.lower()} set{", " + note if note else ""}; fitted to the {fit.lower().replace(" fit", "")} rig. Chunky, readable shape that matches the set\'s textures.',
                        usedby, zone0 if sid not in ('ARM-C4', 'ARM-L5', 'ARM-M5') else 'GC', lo, sid)
        band = 'a' if lo < 10 else 'b' if lo < 20 else 'c'
        if sid in ('ARM-C1', 'ARM-C2', 'ARM-C3', 'ARM-L1', 'ARM-L2', 'ARM-L3', 'ARM-M1', 'ARM-M2', 'ARM-M3'):
            TIERSET[(atype.lower(), band)] = sname

CLOAKS = ['plain', 'trimmed', 'fur-collared', 'patched', 'pelt', 'scale', 'tattered', 'embroidered', 'hooded-look', 'crested', 'winged-membrane', 'burial shroud']
# Geometry swaps (decided 2026-11-24): robe skirts and capes are parts of each player body mesh, not models of their own.
# They are listed with the body they belong to (level 0), after its animations.
SWAP = 'Built into the body mesh, skinned to the {rig} rig and hidden until an item calls for it.'
LOWER = [('plain legs', 'the body\'s own legs as a switchable part, shown under trousers and leg armor and under a kilt, and hidden while the long robe skirt shows', 'Every item that shows the legs'),
         ('short kilt', 'a short skirt from the waist, worn over the legs; painted by the worn item\'s lower-torso and leg region textures', 'Kilts and short skirts'),
         ('long robe skirt', 'a long skirt from the waist to the ankles, which hides the legs under it; painted by the worn robe\'s region textures, whose lower-torso and leg regions carry onto the skirt', 'Robes')]
CAPES = ['short', 'long', 'wide']
for b in BODIES:
    swap = SWAP.format(rig=b.split()[0].lower())
    for v, d, use in LOWER:
        add(f'GEO-01-{slug(b)}-{slug(v)}', 'Body geometry swap', f'Lower body, {v}: {b}', f'Lower-body variant of the {b.lower()} body: {d}. {swap}', use, 'CORE', 0, 'GEO-01')
    for v in CAPES:
        add(f'GEO-02-{slug(b)}-{v}-cape', 'Body geometry swap', f'Cape, {v}: {b}', f'Cape shape of the {b.lower()} body: a {v} cape hanging from the shoulders down the back. It has no texture of its own: it shows the worn cloak item\'s texture. {swap}', 'Cloaks', 'CORE', 0, 'GEO-02')
    for gid, v, d, use in (('GEO-03', 'Flared sleeves', 'a flare at the wrist of each sleeve, painted by the arm regions of the worn chest piece', 'Robes and wide-sleeved chest pieces'),
                           ('GEO-04', 'Glove cuffs', 'a cuff standing out from each lower arm, painted by the lower-arm region of the worn gloves', 'Gauntlets and cuffed gloves'),
                           ('GEO-05', 'Boot tops', 'a top standing out from each lower leg, painted by the lower-leg region of the worn boots', 'Boots with a turned or flared top')):
        add(f'{gid}-{slug(b)}', 'Body geometry swap', f'{v}: {b}', f'{v} of the {b.lower()} body: {d}. {swap}', use, 'CORE', 0, gid)
for i, cdesign in enumerate(CLOAKS):
    for j, way in enumerate(['earth brown', 'forest green', 'slate blue']):
        add(f'CLK-02-{slug(cdesign)}-{j + 1}', 'Armor texture', f'Cloak: {cdesign}, {way}', f'Cloak texture, {cdesign} design in {way}, shown on the cape shape built into each player body. Painted folds, worn hem; back view is what the player sees most.',
            'Cloaks of unnamed drops and vendor goods', 'ANY', 1 + 2 * i, 'CLK-02')
for i, t in enumerate(['brown linen', 'red', 'white formal', 'class starting shirt']):
    add(f'SHT-01-{i + 1}', 'Armor texture', f'Shirt: {t}', f'Shirt texture on the chest and arm regions: {t}.', 'Shirt slot', 'ANY', 1, 'SHT-01')
add('TAB-01', 'Armor texture', 'Guild tabard base', 'Tabard template on the front and back chest region, split into background, border and emblem masks so guild colours tint it.', 'Guild tabards', 'ANY', 10, 'TAB-01')
for e in ['anvil', 'hammer', 'sword', 'crossed swords', 'shield', 'tower', 'crown', 'sun', 'crescent moon', 'star', 'flame', 'oak leaf', 'tree', 'wolf head',
          'bear paw', 'eagle', 'ram head', 'stag antlers', 'boar tusks', 'raven', 'serpent', 'dragon wing', 'fish', 'ship', 'anchor', 'wheat sheaf', 'hop cone',
          'tankard', 'key', 'lantern', 'candle', 'open book', 'quill', 'scales', 'chalice', 'gem', 'pickaxe', 'gear', 'rose', 'skull']:
    add(f'TAB-02-{slug(e)}', 'Armor texture', f'Guild emblem mask: {e}', f'Single-colour emblem mask of a {e}, bold heraldic silhouette, centred, readable at 32 px.', 'Guild tabard designer', 'ANY', 10, 'TAB-02')
for b in ['plain band', 'double line', 'knotwork', 'chevrons', 'studs', 'laurel']:
    add(f'TAB-03-{slug(b)}', 'Armor texture', f'Guild border mask: {b}', f'Single-colour tabard border mask: {b}.', 'Guild tabard designer', 'ANY', 10, 'TAB-03')
for t, z, l in [('Solhaven', 'SOL', 5), ('Hammerdeep', 'HAM', 5), ('Thornwick Wardens', 'TM', 10), ('Freeholders', 'RL', 22), ('Athenaeum', 'SOL', 15), ('Three Banners (PvP)', 'CR', 10)]:
    add(f'TAB-05-{slug(t)}', 'Armor texture', f'Tabard: {t}', f'Fixed tabard of {t}: its colours and badge on the front and back chest region. {zcue(z)}', 'Reputation and PvP tabards; guards', z, l, 'TAB-05')

TIERWPN = {}   # (weapon type, band) -> model name
WAYS3 = ['plain iron and leather wrap', 'bronze fittings and dark wrap', 'blued steel and red wrap']
for h1, h2, h3, c in table(L1):
    if not c or not re.fullmatch(r'WPN-\d+', c[0]):
        continue
    wtype = {'WPN-16': 'Profession tool', 'WPN-17': 'Ammunition and sheath'}.get(c[0], clean(c[2]))
    if c[0] in ('WPN-16', 'WPN-17'):
        models = [(m, 5 if c[0] == 'WPN-16' else 1) for m in split_top(c[3], [', '])]
        nways = 1
    else:
        models = []
        for col, lv, band in ((3, 1, 'a'), (4, 10, 'b'), (5, 20, 'c')):
            cell = re.sub(r'\(.*?\)', '', c[col]).replace('—', '').strip()
            for m in [x.strip() for x in re.split(r',|/', cell) if x.strip()]:
                models.append((m, lv))
                TIERWPN.setdefault((wtype.lower(), band), m)
        nways = max(1, int(c[7]) // max(1, int(c[6])))
    for m, lv in models:
        add(f'{c[0]}-{slug(m)}', 'Weapon model', f'{wtype}: {m}',
            f'{m.capitalize()}, a {"profession tool" if c[0] == "WPN-16" else "generic " + wtype.lower()} for levels {"1–10" if lv < 10 else "10–20" if lv < 20 else "20–30"}'
            f'{" (crude wood, copper)" if lv < 10 else " (bronze)" if lv < 20 else " (iron and steel)"}. Oversized head or blade, thick grip, clear silhouette; base colourway {WAYS3[0]}.',
            'Starting gear, vendor goods, crafted items, unnamed drops and the named items that use tier art', 'ANY', lv, c[0])
        for w in range(1, nways):
            add(f'{c[0]}-{slug(m)}-cw{w + 1}', 'Weapon model', f'{wtype}: {m}, colourway {w + 1}',
                f'Recolour texture for the {m}: {WAYS3[w % 3]}. Same model, palette remap only.', 'Named items that use this tier model', 'ANY', lv, c[0])

add('ATT-02', 'Effect', 'Sharpening stone and weightstone sheen', 'Brief steel glint that runs along a weapon when a stone is applied.', 'Weapon stones', 'ANY', 5, 'ATT-02')
for t in ['wizard oil shimmer (violet)', 'mana oil shimmer (blue)']:
    add(f'ATT-03-{slug(t)}', 'Effect', f'Weapon oil: {t}', f'Soft persistent {t} along the weapon.', 'Weapon oils', 'ANY', 10, 'ATT-03')
add('ATT-04', 'Prop', 'Shield spike', 'Iron spike that mounts on the centre of any shield.', 'Blacksmithing shield spike', 'ANY', 15, 'ATT-04')
add('ATT-05', 'Prop', 'Weapon chain', 'Short iron chain from weapon pommel to wrist.', 'Blacksmithing weapon chain', 'ANY', 20, 'ATT-05')
for s in ['small', 'medium', 'large']:
    add(f'ATT-06-{s}', 'Prop', f'Gun scope, {s}', f'{s.capitalize()} brass scope that mounts on a gun barrel.', 'Engineering scopes', 'ANY', {'small': 10, 'medium': 17, 'large': 25}[s], 'ATT-06')

add('MNT-01-rig', 'Rig', 'Horse rig', 'Quadruped horse skeleton with a rider socket on the saddle.', 'Horse mounts and the Vault Charger', 'SOL', 30, 'MNT-01')
add('MNT-01-mesh', 'Character model', 'Horse', 'Sturdy riding horse, chunky legs and neck, short mane, with saddle and bridle. 3 to 5k triangles.', 'Level-30 mounts sold in Solhaven', 'SOL', 30, 'MNT-01')
for clip in ['Idle', 'Walk', 'Run', 'Jump', 'Rear']:
    add(f'MNT-01-{slug(clip)}', 'Animation', f'Horse: {clip}', f'Horse {clip.lower()} clip with a rider seated.', 'Horse mounts', 'SOL', 30, 'MNT-01')
for t in ['bay', 'black', 'chestnut', 'grey']:
    add(f'MNT-02-{t}', 'Skin or outfit', f'Horse colourway: {t}, with tack', f'{t.capitalize()} horse coat with Solhaven blue saddle blanket and brass tack.', 'Level-30 mount', 'SOL', 30, 'MNT-02')
add('MNT-03', 'Character model', 'Ram mount saddle and tack', 'Dwarven saddle, horn-rings and harness that fit the ram creature rig; rider sits forward.', 'Level-30 mounts sold in Hammerdeep', 'HAM', 30, 'MNT-03')
for t in ['grey', 'brown', 'white', 'black']:
    add(f'MNT-04-{t}', 'Skin or outfit', f'Ram mount colourway: {t}', f'{t.capitalize()} riding ram fleece with iron-banded horns.', 'Level-30 mount', 'HAM', 30, 'MNT-04')
add('MNT-05', 'Skin or outfit', 'Vault Charger', 'Armoured spectral horse: tarnished imperial bronze barding over a translucent violet-lit body, glowing hooves.', 'Raid drop mount', 'HT', 30, 'MNT-05')
add('MNT-07-mesh', 'Character model', 'Crag eagle taxi with harness', 'Very large mountain eagle with a leather passenger harness and grab bar; uses the flying bird rig.', 'Flight between eyries', 'BM', 3, 'MNT-07')
for clip in ['Fly idle', 'Fly forward', 'Bank', 'Take-off', 'Land']:
    add(f'MNT-07-{slug(clip)}', 'Animation', f'Crag eagle taxi: {clip}', f'Eagle {clip.lower()} clip carrying a passenger.', 'Flight between eyries', 'BM', 3, 'MNT-07')
for part in ['hull', 'deck and rails', 'masts and animated sails', "ship's wheel and helm", 'crew stations, hatches and cargo']:
    add(f'MNT-08-{slug(part)}', 'Set piece', f'The Hearth-Oath: {part}', f'Part of the capital ship The Hearth-Oath, a broad two-masted trading vessel built by both peoples: {part}. Human blue-and-gold sails, dwarven iron fittings.',
        'The free ship between Solhaven and Hammerdeep', 'SEA', 5, 'MNT-08')
add('MNT-09', 'Prop', 'Mine-cart with rider seat', 'Iron-banded dwarven mine-cart on rails with a bench seat and brake lever; lantern on the front.', 'The cart ride in Stoneheart Deeps', 'SD', 6, 'MNT-09')

# ----------------------------------------------------------------------------- list 2: creatures and NPCs
L2 = 'docs/10-art/02-creatures-npcs.md'
STD_CLIPS = ['Idle', 'Idle fidget', 'Walk', 'Run', 'Attack A', 'Attack B', 'Hit react', 'Death', 'Stunned', 'Special']
RIG_LEVEL, RIG_NAMES = {}, []
SKIN_FIX = {'Crag Eagle': ('BM', 3), 'Dust Devil': ('RL', 25), 'Chief Gnarr': ('ST', 5), 'Shard-Chief Krakk': ('SD', 9), 'Clockwork Ram': ('ANY', 15),
            'Target Dummy': ('ANY', 10), 'Mechanical Squirrel': ('ANY', 12), 'farm goats and sheep': ('ST', 1), 'critter rat': ('SD', 5), 'ambient deer': ('RW', 5),
            'ambient crows, gulls over Solhaven': ('SOL', 5)}
for h1, h2, h3, c in table(L2):
    if not c or not re.fullmatch(r'CRE-[A-Z]\d+', c[0]):
        continue
    rid, rig = c[0], clean(c[2])
    rigshort = re.sub(r'\(.*?\)', '', rig).strip()
    skins = []
    for el in split_top(clean(c[4]), [' · ']):
        if 'see doc 1' in el:
            continue
        el = el.lstrip('+ ').strip()
        base = re.sub(r'\(.*?\)', '', el).strip()
        note = ', '.join(re.findall(r'\(([^)]*)\)', el))
        names = [f'{base} {LETTERS[i]}' for i in range(int(re.search(r'×(\d)', base).group(1)))] if re.search(r'×\d', base) else [base]
        for nm in names:
            nm = re.sub(r'\s*×\d', '', nm).strip()
            hit = SKIN_FIX.get(nm) or creature(nm) or creature(f'{rigshort} {nm}') or locate(el) or (skins[-1][2] if skins else None)
            skins.append((nm, note, hit))
    known = [s[2] for s in skins if s[2]]
    rz, rl = min(known, key=lambda x: (x[1], ZONES[x[0]][2])) if known else ('ANY', 10)
    RIG_LEVEL[rigshort.lower()] = (rz, rl)
    RIG_NAMES.append((rid, rigshort, rz, rl))
    human = rid == 'CRE-H07'
    if not human:
        add(f'{rid}-rig', 'Rig', f'{rigshort} rig', f'Skeleton and skin weights for the {rig.lower()} body plan, shared by every skin below.', f'All {rigshort.lower()} creatures', rz, rl, rid)
        add(f'{rid}-mesh', 'Character model', f'{rigshort} base model', f'Base model of the {rig.lower()}: stylised low-poly, exaggerated head, jaws or claws, strong silhouette. Skins re-texture it; mesh variants are noted on the skin.',
            f'All {rigshort.lower()} creatures', rz, rl, rid)
        for clip in STD_CLIPS + [x.strip() for x in split_top(clean(c[3]), [', '])]:
            add(f'{rid}-anim-{slug(clip)}', 'Animation', f'{rigshort}: {clip}', f'{rigshort} {clip.lower()} clip. {"Loops." if re.search("Idle|Walk|Run|Fly|Float|Stunned|Sleep|Hang|Sit|Graze|Perch", clip) else "Plays once."}',
                f'All {rigshort.lower()} creatures', rz, rl, rid)
    else:
        for b in ('Elf male body', 'Elf female body'):
            add(f'{rid}-{slug(b)}', 'Character model', b, f'{b}: tall, slender, long ears; NPC quality now, reserved as a future player body. Uses the player animation set, retargeted.', 'Wildpact elves', rz, rl, rid)
    for nm, note, hit in skins:
        z, l = hit or (rz, rl)
        add(f'{rid}-skin-{slug(nm)}', 'Skin or outfit', f'{nm} ({rigshort.lower()})',
            f'{"Outfit" if human else "Skin"} for {nm}, on the {rigshort.lower()} {"body" if human else "rig"}{": " + note if note else ""}. A level {l} creature of {ZS[z]}; re-textures the {rigshort.lower()} base model, with a mesh change only where the note says so. {zcue(z)}',
            f'Creature {nm}', z, l, rid)

BOSS_CLIPS = ['Idle', 'Move', 'Attack A', 'Attack B', 'Special A', 'Special B', 'Stagger', 'Death', 'Emerge', 'Enrage', 'Special C', 'Phase change',
              'Special D', 'Phase change 2', 'Phase change 3', 'Defeat pose']
for h1, h2, h3, c in table(L2):
    if not c or not re.fullmatch(r'BOS-\d+', c[0]):
        continue
    bid, boss, where, needs = c[0], clean(c[2]), clean(c[3]), clean(c[4])
    z, l = creature(boss.split(',')[0]) or locate(where) or locate(boss) or ('ANY', 20)
    if where == 'Raid':
        z, l = 'HT', 30
    if where == 'World boss':
        z, l = 'WB', 30
    z, l = {'BOS-01': ('TM', 15), 'BOS-04': ('SD', 10)}.get(bid, (z, l))
    onrig = re.search(r'(Human-[MF]|Human|Skeleton|Spectre) rig', needs)
    if bid == 'BOS-08':
        add(f'{bid}-aubrec', 'Skin or outfit', 'Lord-Chamberlain Aubrec', f'Unique outfit and head for Lord-Chamberlain Aubrec on the human rig: a gaunt chamberlain in hollow court livery with a staff of office. {zcue(z)}', 'Boss event: the Banquet of Hollows', z, l, bid)
        for i in range(1, 7):
            for cw in ('A', 'B'):
                add(f'{bid}-noble-{i}{cw.lower()}', 'Skin or outfit', f'Banquet noble outfit {i}, colourway {cw}', f'Court dress for one of the twelve seated nobles at the Banquet of Hollows, outfit {i} of 6 in colourway {cw}; faded finery, blank hollowed eyes. {zcue(z)}', 'Boss event: the Banquet of Hollows', z, l, bid)
        for clip in ('Seated idle', 'Rise from seat'):
            add(f'{bid}-anim-{slug(clip)}', 'Animation', f'Banquet noble: {clip} (Human rig)', f'{clip} clip on the human rig for the banquet nobles.', 'Boss event: the Banquet of Hollows', z, l, bid)
    elif bid == 'BOS-18':
        for cw in ('A', 'B'):
            add(f'{bid}-outfit-{cw.lower()}', 'Skin or outfit', f'Tor Vael courtier (Hollow Echo), colourway {cw}', f'Imperial court outfit on the human rig drawn with the translucent hollow shader, colourway {cw}. {zcue(z)}', 'Raid: courtiers and Hollow Echoes', z, l, bid)
    elif onrig:
        add(f'{bid}-outfit', 'Skin or outfit', f'{boss}', f'Unique outfit and head for {boss} on the {onrig.group(1).lower()} rig: {needs}. {zcue(z)}', f'Boss: {boss}', z, l, bid)
    else:
        add(f'{bid}-rig', 'Rig', f'{boss}: rig', f'Unique skeleton for {boss}: {needs}.', f'Boss: {boss}', z, l, bid)
        add(f'{bid}-mesh', 'Character model', f'{boss}', f'Unique boss model, 8 to 12k triangles, 2048 px: {needs}. {zcue(z)}', f'Boss: {boss}', z, l, bid)
        n = int(re.search(r'(\d+) clips', needs).group(1)) if re.search(r'(\d+) clips', needs) else 8
        for clip in BOSS_CLIPS[:n]:
            add(f'{bid}-anim-{slug(clip)}', 'Animation', f'{boss}: {clip}', f'{clip} clip for {boss}; timed to the encounter in the encounter data.', f'Boss: {boss}', z, l, bid)

for h1, h2, h3, c in table(L2):
    if not c or not re.fullmatch(r'NPC-(HU|DW)\d+', c[0]):
        continue
    nid, outfit, worn = c[0], clean(c[2]), clean(c[3])
    rig = 'human' if 'HU' in nid else 'dwarf'
    z, l = locate(worn) or locate(outfit) or (('BM', 1) if rig == 'human' else ('ST', 1))
    if 'All human hubs' in worn or worn == 'Trainers':
        z, l = ('BM', 1) if rig == 'human' else ('ST', 1)
    if 'All Khazrun zones' in worn:
        z, l = 'EC', 7          # the Slagborn are first met at Kiln Cave
    parts = split_top(outfit, [' + '])
    names = []
    base = parts[0]
    m = re.search(r'×(\d+)', base)
    par = re.search(r'\(([^)]*)\)', base)
    note = ''
    if ':' in base and not m:                                   # "Slagborn named: A, B, C"
        stem = base.split(':')[0].strip()
        names += [x.strip() for x in base.split(':', 1)[1].split(',')]
    elif m:
        stem = base[:m.start()].strip(' —-')
        tail = base[par.end():].strip(' —-') if par else ''
        opts = [x.strip() for x in par.group(1).split(';')[0].split(',')] if par else []
        note = '; '.join(x for x in ([y.strip() for y in par.group(1).split(';')[1:]] if par else []) + [tail] if x)
        opts = [o for o in opts if 'none' not in o]
        if len(opts) >= int(m.group(1)) - 1 and len(opts) > 1:
            names += [f'{stem}: {o}' for o in opts]
        elif ' / ' in stem and len(stem.split(' / ')) == int(m.group(1)):
            names += [x.strip() for x in stem.split(' / ')]
        else:
            names += [f'{stem} {LETTERS[i]}' for i in range(int(m.group(1)))]
    else:
        stem = re.sub(r'\(.*?\)', '', base).strip(' —-')
        if par and 'household' in stem and ',' in par.group(1):
            names += [f'{stem}: {x.strip()}' for x in par.group(1).split(',')]
        else:
            names.append(stem)
            note = par.group(1) if par else ''
    for extra in parts[1:]:
        for x in split_top(extra, [', ']):
            for y in mult(x):
                names.append(y[0].upper() + y[1:] if (y[:1].isupper() or '×' in x) else f'{stem} {y}')
    for nm in names:
        own = ', '.join(re.findall(r'\(([^)]*)\)', nm))
        nm2 = re.sub(r'\s*\(.*?\)', '', nm).strip()
        ck = creature_k(nm2.split(': ')[-1]) or creature_k(nm2.replace(': ', ' ')) or creature_k(nm2)
        zz, ll = z, l
        if ck and (ck[1][0] == z or any(w in ck[0] for w in stem.lower().split() if len(w) > 3) or nm2[:1].isupper() and ' ' in nm2 and ck[0].endswith(nm2.lower())):
            zz, ll = ck[1]
        extra_note = '; '.join(x for x in (own, note) if x)
        add(f'{nid}-{slug(nm2)}', 'Skin or outfit', nm2,
            f'NPC outfit on the {rig} rig, worn by male and female bodies: {nm2}{" (" + extra_note + ")" if extra_note else ""}. Body-region textures plus any helm or shoulder piece and hand prop it needs. {zcue(zz)}',
            f'Worn by: {worn}', zz, ll, nid)
add('NPC-SPIRIT', 'Character model', 'Spirit healer', 'Unique winged spectre in pale robes, hooded, translucent blue-white, hovering; seen only by the dead.', 'Every graveyard', 'ANY', 1, 'Service NPCs')

CRIT_Z = {'CRT-01': ('BM', 1), 'CRT-02': ('BM', 3), 'CRT-03': ('BM', 1), 'CRT-04': ('ST', 1), 'CRT-05': ('BM', 1), 'CRT-06': ('TM', 10),
          'CRT-07': ('RL', 20), 'CRT-08': ('TM', 10), 'CRT-09': ('SD', 5), 'CRT-10': ('CF', 20), 'CRT-11': ('BM', 1), 'CRT-12': ('BM', 4)}
for h1, h2, h3, c in table(L2):
    if c and c[0] in CRIT_Z:
        z, l = CRIT_Z[c[0]]
        nm = clean(c[2])
        if 'particle' in nm or 'decal' in nm:
            add(c[0], 'Effect', f'Critter: {nm}', f'Ambient {nm.lower()}; no model.', f'Ambient life in {clean(c[3])}', z, l, c[0])
            continue
        add(f'{c[0]}-mesh', 'Character model', f'Critter: {nm}', f'Tiny ambient {nm.lower()}, 150 to 400 triangles, with its own small skeleton.', f'Ambient life in {clean(c[3])}', z, l, c[0])
        for clip in ['Idle', 'Move', 'Death']:
            add(f'{c[0]}-anim-{slug(clip)}', 'Animation', f'Critter {nm}: {clip}', f'{clip} clip for the {nm.lower()} critter.', 'Ambient life', z, l, c[0])

# ----------------------------------------------------------------------------- list 3: environments
L3 = 'docs/10-art/03-environments-props.md'
BUILDING_POOL = ['wall, straight', 'wall with window', 'wall with doorway', 'outer corner', 'inner corner', 'half-height wall', 'wall end cap', 'gable end wall',
                 'upper-storey wall', 'upper-storey wall with window', 'floor slab', 'floor edge strip', 'ceiling with beams', 'roof slope panel', 'roof ridge',
                 'roof eave end', 'roof hip corner', 'roof valley', 'chimney', 'single door (hinged, opens)', 'double door (hinged, opens)',
                 'window frame with shutters', 'straight stair', 'corner stair', 'porch or awning', 'balcony with rail', 'post or pillar', 'foundation plinth',
                 'exposed beam and trim set', 'interior partition wall', 'interior doorway', 'shop counter', 'hearth and fireplace', 'hanging sign bracket',
                 'ruined wall with broken top', 'ruined roof with holes', 'loft ladder', 'cellar hatch', 'dormer window', 'lean-to shed module',
                 'garden wall segment', 'gate post pair', 'well-head', 'three-tread steps', 'cornice or parapet strip', 'arched doorway', 'buttress',
                 'round tower segment', 'tower cap', 'battlement strip', 'tall window with leaded glass', 'vaulted ceiling bay',
                 'colonnade bay', 'great stair flight', 'rose window', 'spire segment', 'spire cap', 'buttressed wall', 'banner bracket', 'drain channel strip',
                 'paving slab set', 'kerb strip', 'grand doorway surround', 'dais', 'bench row', 'bookshelf wall bay', 'vault alcove',
                 'bridge deck segment', 'bridge rail', 'quay edge block', 'mooring post', 'street lamp bracket', 'market stall frame', 'statue plinth', 'fountain basin']
KIT_FILL = {
    'KIT-04': ['carved wall, straight', 'wall with rune band', 'wall with alcove', 'wall with doorway', 'outer corner', 'inner corner', 'floor slab, plain',
               'floor slab with inlay', 'vaulted ceiling bay', 'beamed ceiling bay', 'column base', 'column capital', 'arch span', 'standing brazier', 'hanging brazier',
               'brass lamp post', 'stone bench', 'stone table', 'hearth', 'forge chimney', 'bellows mount', 'anvil plinth', 'stair landing', 'stair rail', 'bridge span',
               'bridge rail', 'gate winch', 'portcullis', 'window slit', 'light shaft', 'ancestor statue', 'statue plinth', 'banner bracket', 'rail, straight',
               'rail, curve', 'rail buffer stop', 'lift cage', 'lift counterweight', 'water channel', 'floor grate', 'single stone door', 'carved door frame', 'parapet',
               'exterior tower segment', 'exterior roof slab with snow', 'broken wall variant', 'broken pillar variant', 'rubble heap'],
    'KIT-08': ['corridor corner', 'corridor T-junction', 'corridor dead end', 'empty wall niche', 'wall niche with coffin', 'sarcophagus, closed', 'sarcophagus, open',
               'sarcophagus lid', 'pillar', 'arch', 'vaulted ceiling bay', 'floor slab', 'floor with drain', 'cracked floor', 'iron gate', 'iron grille', 'heavy door',
               'stair landing', 'candle stand', 'wall sconce', 'altar', 'bone pile', 'urn', 'shelf of urns', 'mourner statue', 'collapsed wall', 'rubble', 'cobweb drape',
               'crypt entrance facade', 'brazier', 'ossuary wall panel'],
    'KIT-09': ['black iron wall panel', 'wall with pipe run', 'wall with grille', 'corner', 'floor grate', 'floor plate', 'iron stair', 'caged ladder', 'railing', 'chain hoist',
               'crane arm', 'ore chute', 'conveyor, straight', 'conveyor end', 'lever stand', 'valve wheel', 'pipe, straight', 'pipe bend', 'pipe junction',
               'slag channel, straight', 'slag channel bend', 'slag fall', 'mould rack', 'ingot stack', 'coal heap', 'quench trough', 'anvil station', 'tool wall',
               'furnace door', 'chimney stack', 'vent hood', 'gear housing', 'piston', 'support truss', 'heavy iron door', 'brick wall variant (kiln)', 'brick dome (kiln)'],
    'KIT-14': ['skull pile', 'meat rack', 'war drum', 'club rack', 'boulder pile', 'hide banner', 'crude cage'],
    'KIT-15': ['stolen grain heap', 'candle-wax mound', 'scrap ladder', 'nest of rags', 'pick rack', 'tin-pot drum', 'burrow mouth', 'dirt mound', 'bent sign', 'hoard chest'],
    'KIT-16': ['fish basket', 'net on poles', 'reed mat', 'shell midden', 'mooring stake'],
    'KIT-17': ['bone ladder', 'hide drum', 'skull totem', 'carrion rack', 'ledge platform', 'rope bridge', 'feather banner', 'fire bowl'],
    'KIT-18': ['woven hammock', 'root stair', 'bark shield rack', 'herb drying frame', 'spirit pole', 'bow rack', 'seed basket', 'standing lantern stone'],
    'KIT-20': ['road edge kerb', 'road fork decal', 'crossroads decal', 'wheel-rut decal', 'ford stepping stones', 'culvert', 'stile', 'field gate', 'hedge segment',
               'hedge corner', 'dry-stone wall end', 'gate pier', 'bridge abutment', 'toll bar', 'wayside shrine niche'],
    'KIT-11': ['whole column', 'broken column', 'column base', 'fallen column drum', 'wall, straight', 'wall with broken top', 'wall with niche', 'wall corner',
               'paving slab', 'cracked paving', 'paving with inlaid bronze', 'grand stair', 'broken stair', 'pediment', 'entablature', 'dome fragment', 'bronze door leaf',
               'bronze brazier', 'aether crystal, small', 'aether crystal, large', 'crystal conduit', 'obelisk', 'plinth', 'dry fountain', 'broken bridge span',
               'rubble, small', 'rubble, large', 'half-buried roof', 'half-buried arch', 'tall window', 'balcony fragment', 'ballista emplacement', 'tarnished banner pole',
               'mosaic floor panel', 'throne-hall pillar', 'barracks doorway'],
}
CAVE_POOL = ['tunnel, dead end', 'tunnel, narrow squeeze', 'tunnel, wide', 'tunnel, collapsed and blocked', 'four-way junction', 'ledge with drop', 'rock pillar',
             'rubble pile, small', 'rubble pile, medium', 'rubble pile, large', 'stalagmite cluster', 'stalactite cluster', 'timber prop set', 'rail, straight',
             'rail, curve', 'rail junction', 'rail buffer stop', 'lantern hook with lamp', 'ladder', 'plank bridge', 'ore seam wall panel', 'flooded floor section',
             'cave mouth, exterior', 'single boulder', 'wall crack', 'winch and bucket', 'tool rack', 'spoil heap', 'boss-size chamber', 'spiral ramp',
             'natural arch', 'pool basin', 'ceiling shaft with light', 'root-pierced ceiling', 'crystal vein wall panel', 'scaffold platform', 'scaffold stair',
             'rope bridge', 'chain hoist', 'ventilation shaft']
DRESS_POOL = ['crate stack', 'barrel cluster', 'sack pile', 'bedroll', 'cooking tripod', 'drying rack', 'torch stand', 'banner pole', 'stake fence segment',
              'lookout post', 'supply cart', 'hide rug', 'stool', 'rough table', 'woodpile', 'water butt', 'tool rack', 'bone pile', 'rope coil', 'lantern on a pole',
              'chopping block', 'stew pot', 'tarpaulin shelter', 'signal horn stand', 'hitching rail', 'weapon pile', 'cage, small', 'trophy pole', 'rag screen', 'ladder']
KIT_FIX = {'fence ×4': 'fence ×4 (post-and-rail, wattle, picket, split-rail)', 'wall ×3': 'wall ×3 (dry-stone, mortared, rubble)',
           'Tent ×4': 'Tent ×4 (small ridge, large ridge, round, command)', 'wagon ×2': 'wagon ×2 (covered, flatbed)', 'Hide tent ×2': 'Hide tent ×2 (small, chieftain)',
           'totem ×3': 'totem ×3 (skull, tusk, painted hide)', 'Hut ×2': 'Hut ×2 (small, large)', 'statue ×3': 'statue ×3 (emperor, legionary, magister)',
           'pillar ×4': 'pillar ×4 (plain, fluted, rune-carved, broken)', 'Hall facade ×3': 'Hall facade ×3 (plain, arcaded, grand)',
           'Flat-roof house ×3': 'Flat-roof house ×3 (small, two-storey, courtyard)', 'market awning ×3': 'market awning ×3 (striped, plain, patched)'}
KITZ = {'KIT-01': ('BM', 1), 'KIT-02': ('BM', 3), 'KIT-03': ('SOL', 5), 'KIT-04': ('HAM', 5), 'KIT-05': ('ST', 1), 'KIT-06': ('BM', 2), 'KIT-07': ('SD', 5),
        'KIT-08': ('TM', 11), 'KIT-09': ('RW', 9), 'KIT-10': ('HF', 9), 'KIT-11': ('CR', 10), 'KIT-12': ('BM', 3), 'KIT-13': ('BM', 3), 'KIT-14': ('IR', 13),
        'KIT-15': ('BM', 2), 'KIT-16': ('BM', 4), 'KIT-17': ('RL', 22), 'KIT-18': ('TM', 14), 'KIT-19': ('RL', 20), 'KIT-20': ('BM', 1)}
ASSEMBLED = {'KIT-01', 'KIT-02', 'KIT-03', 'KIT-05', 'KIT-10', 'KIT-19'}
for h1, h2, h3, c in table(L3):
    if not c or not re.fullmatch(r'KIT-\d+', c[0]):
        continue
    kid, kit, count, listed, usedin = c[0], clean(c[2]), int(c[3]), clean(c[4]), clean(c[5])
    kname = re.sub(r'\(.*?\)', '', kit).strip()
    kstyle = ', '.join(re.findall(r'\(([^)]*)\)', kit))
    z, l = KITZ[kid]
    add(f'{kid}-atlas', 'Kit atlas', f'{kname} kit: trim-sheet atlas', f'Shared texture atlas for the {kname} kit{": " + kstyle if kstyle else ""}. Bands of wall, roof, trim, door and floor surfaces that every piece of the kit maps onto. {zcue(z)}',
        f'Every piece of {kid}', z, l, kid)
    for a, b in KIT_FIX.items():
        listed = listed.replace(a, b)
    named = [x.replace(': ', ', ') for x in expand(listed, [', '], do_slash=True)]
    if kid == 'KIT-07':
        named = ['cavern shell, small scale', 'cavern shell, medium scale', 'cavern shell, great scale'] + [x for x in named if 'shell' not in x]
    if kid in ASSEMBLED:
        pieces = BUILDING_POOL[:count]
        for bname in named:
            add(f'{kid}-asm-{slug(bname)}', 'Building assembly', f'{kname}: {bname}', f'Whole building put together from {kid} pieces: {bname}. {kstyle.capitalize() + "." if kstyle else ""} Sizes and facing follow World Construction §5.',
                f'Used in: {usedin}', z, l, kid)
    else:
        pool = CAVE_POOL if kid in ('KIT-06', 'KIT-07') else KIT_FILL.get(kid, DRESS_POOL)
        pieces = (named + [p for p in pool if p not in named])[:max(count, len(named))]
    for p in pieces:
        add(f'{kid}-{slug(p)}', 'Kit piece', f'{kname}: {p}', f'Modular piece "{p}" of the {kname} kit{" (" + kstyle + ")" if kstyle else ""}. Snaps to the kit\'s module grid and maps onto the kit atlas. {zcue(z)}',
            f'Used in: {usedin}', z, l, kid)

OBJ = {
    'OBJ-01': [('Mailbox, human', 'BM', 1), ('Mailbox, dwarf', 'ST', 1), ('Mailbox, mesa', 'RL', 22)],
    'OBJ-02': [('Chest, wooden (open and closed)', 'BM', 2), ('Chest, iron-bound (open and closed)', 'TM', 10), ('Chest, imperial (open and closed)', 'RL', 20)],
    'OBJ-03': [('Campfire', 'ANY', 1), ('Cooking spit over a campfire', 'ANY', 1)],
    'OBJ-04': [('Forge, human', 'BM', 3), ('Anvil, human', 'BM', 3), ('Forge, dwarf', 'ST', 3), ('Anvil, dwarf', 'ST', 3)],
    'OBJ-05': [('Meeting stone', 'TM', 13)],
    'OBJ-06': [(f'Headstone {LETTERS[i]}', 'BM', 1) for i in range(6)] + [('Graveyard fence', 'BM', 1), ('Graveyard gate', 'BM', 1), ('Graveyard angel statue', 'BM', 1)],
    'OBJ-07': [('Eyrie perch, human', 'BM', 3), ('Eyrie perch, dwarf', 'ST', 3), ('Eyrie perch, mesa', 'RL', 22)],
    'OBJ-08': [('Bank vault door', 'SOL', 5), ('Guild vault', 'SOL', 10)],
    'OBJ-09': [('Auction podium', 'SOL', 5), ('Notice board', 'BM', 3), ('Wanted poster', 'BM', 5), ('Bounty board', 'HF', 5)],
    'OBJ-10': [('Training dummy, straw', 'BM', 1), ('Training dummy, armoured', 'SOL', 5)],
    'OBJ-11': [('Hitching post', 'BM', 3), ('Water trough', 'BM', 3), ('Feed sack', 'SOL', 30)],
    'OBJ-12': [('Duel flag', 'ANY', 1)],
    'OBJ-13': [('Fishing bobber', 'ANY', 5), ('Fishing pool surface', 'TM', 10)],
    'OBJ-14': [(n, 'SOL', 5) for n in ['Book, closed', 'Book, open on a stand', 'Large tome', 'Scroll', 'Scroll case', 'Letter']],
    'OBJ-15': [('Door, wooden', 'BM', 1), ('Door, iron-bound', 'BM', 2), ('Door, dwarven stone', 'HAM', 5), ('Double gate', 'BM', 3), ('Floor lever', 'ST', 3),
               ('Wall lever', 'SD', 7), ('Portcullis', 'TM', 10), ('Lift platform', 'HAM', 5)],
    'OBJ-16': [('Instance portal frame, dungeon', 'GC', 13), ('Instance portal frame, raid', 'HT', 30)],
    'OBJ-17': [('Crown relic', 'CR', 10), ('Hill banner, red', 'CR', 10), ('Hill banner, blue', 'CR', 10), ('Hill banner, yellow', 'CR', 10), ('Shrine of Steel', 'CR', 10),
               ('Shrine of Bloom', 'CR', 10), ('Shrine of Aether', 'CR', 10), ('Battleground base gate', 'CR', 10), ("Pitmaster's Chest", 'DP', 24)],
}
GENERIC = [('Barrel', ['upright', 'on its side', 'open with water']), ('Crate', ['small', 'large', 'open']), ('Sack', ['grain', 'flour']),
           ('Pot', ['cook pot', 'clay jar', 'tall urn', 'washing tub']), ('Table', ['trestle', 'round tavern', 'work bench']), ('Chair', ['stool', 'ladder-back', 'bench']),
           ('Bed', ['cot', 'box bed']), ('Shelf', ['wall shelf', 'tall bookcase', 'pantry rack']), ('Rug', ['woven red', 'woven blue', 'hide', 'rag']),
           ('Banner', ['Solhaven', 'Hammerdeep', 'Dale-Moot', 'Thornwick Wardens', 'Freeholders', 'plain']),
           ('Tool', ['hammer', 'saw', 'felling axe', 'shovel', 'pitchfork', 'scythe', 'bucket', 'broom', 'rake', 'hoe']),
           ('Food', ['loaf', 'cheese wheel', 'apple basket', 'ham', 'fish on a plate', 'pie', 'stew bowl', 'tankard', 'cabbages', 'turnips', 'sausage string', 'egg basket']),
           ('Bottle', ['wine', 'ale jug', 'potion flask', 'oil flask', 'corked vial', 'empty']), ('Candle', ['single', 'cluster', 'on a stick', 'in a holder']),
           ('Lantern', ['hand lantern', 'hanging lantern', 'storm lantern', 'paper lantern'])]
OBJ['OBJ-18'] = [(f'{g}: {v}', 'BM' if g != 'Banner' else {'Solhaven': 'SOL', 'Hammerdeep': 'HAM', 'Dale-Moot': 'ST', 'Thornwick Wardens': 'TM', 'Freeholders': 'RL'}.get(v, 'BM'), 1)
                 for g, vs in GENERIC for v in vs]
for oid, items in OBJ.items():
    for nm, z, l in items:
        l = max(l, ZONES[z][1]) if z not in ('ANY', 'BM', 'ST') else l
        add(f'{oid}-{slug(nm)}', 'Prop', nm, f'{nm}: interactive world object or generic prop, low-poly with a clear outline. {zcue(z)}', 'Hubs, camps and interiors', z, l, oid)

NODES = [('Copper Vein', 'BM', 1), ('Tin Vein', 'HF', 7), ('Silver Vein', 'SD', 8), ('Iron Deposit', 'IR', 15), ('Gold Vein', 'CF', 20), ('Starmetal Deposit', 'CF', 26),
         ('Slag Heap', 'CF', 22), ('Sunpetal', 'BM', 1), ('Hearthroot', 'BM', 1), ('Dewleaf', 'BM', 3), ('Bramblethorn', 'HF', 6), ('Marshbloom', 'EC', 8),
         ('Gravecap', 'TM', 11), ('Crownleaf', 'TM', 12), ('Emberweed', 'IR', 15), ('Frostcap', 'IR', 16), ('Wyrmtongue', 'CF', 20), ('Veilshade', 'VM', 21),
         ('Riftbloom', 'RL', 22), ('Ashbloom', 'CF', 24), ('Ghostlily', 'VM', 27), ('Starpetal', 'CF', 28), ('Glowcap', 'SD', 5)]
for i, (nm, z, l) in enumerate(NODES):
    ore = i < 7
    add(f'NOD-{i + 1:02d}', 'Gathering node', nm,
        f'{nm} gathering node: ' + ('a rock outcrop with a clearly coloured ore seam; a full state and a depleted state with the seam gone.' if ore else 'a small plant with one distinct coloured bloom or cap and a soft glint; vanishes when picked.') + f' {zcue(z)}',
        'Mining' if ore else 'Herbalism' if nm != 'Glowcap' else 'Cooking pick-up', z, l, f'NOD-{i + 1:02d}')

NAT = {
    'NAT-01': ('BM', 1, ['Oak A', 'Oak B', 'Oak C', 'Birch A', 'Birch B', 'Apple tree A (orchard)', 'Apple tree B (orchard)', 'Willow', 'Dead tree A', 'Dead tree B',
                         'Stump A', 'Stump B', 'Stump C', 'Fallen log A', 'Fallen log B']),
    'NAT-02': ('HF', 5, ['Giant oak A, red leaves', 'Giant oak B, gold leaves', 'Giant oak C, copper leaves', 'Maple A, red', 'Maple B, gold', 'Maple C, copper',
                         'Beech A, gold', 'Beech B, copper', 'Leaf-litter decal, red', 'Leaf-litter decal, gold', 'Leaf-litter decal, copper']),
    'NAT-03': ('EC', 5, ['Frostpine A, snow-laden', 'Frostpine B, snow-laden', 'Frostpine C, snow-laden', 'Highland pine A', 'Highland pine B', 'Highland pine C']),
    'NAT-04': ('TM', 10, ['Gnarled swamp tree A', 'Gnarled swamp tree B', 'Gnarled swamp tree C', 'Reeds A', 'Reeds B', 'Cattails', 'Hanging moss', 'Peat stack', 'Gibbet tree']),
    'NAT-05': ('TM', 10, [f'Thorn-wall segment {LETTERS[i]}' for i in range(4)] + [f'Bramble clump {LETTERS[i]}' for i in range(3)]),
    'NAT-06': ('RL', 20, ['Scrub A', 'Scrub B', 'Scrub C', 'Succulent A', 'Succulent B', 'Tumbleweed', 'Dry tree A', 'Dry tree B']),
    'NAT-07': ('CF', 20, ['Charred tree A', 'Charred tree B', 'Charred tree C', 'Ash-drift decal']),
    'NAT-08': ('SD', 5, [f'Glowcap mushroom, {s}, {col}' for col in ('teal', 'amber') for s in ('small', 'medium', 'large', 'giant')] + ['Cave moss']
               + [f'Crystal cluster, {col}' for col in ('violet', 'cyan', 'white', 'amber')] + ['Root curtain']),
    'NAT-09': ('BM', 1, ['Barley and wheat field strip', 'Turnip rows', 'Hop-poles', 'Orchard row', 'Hay bale', 'Scorched field strip']),
    'NAT-10': ('BM', 1, [f'Grass card, {b}' for b in ('meadow', 'snow', 'autumn', 'highland', 'arid', 'moor')] + [f'Flower {LETTERS[i]}' for i in range(6)]
               + ['Fern A', 'Fern B', 'Heather', 'Snow tuft']),
    'NAT-11': ('BM', 1, [f'{s} rock, size {n}' for s in ('Meadow granite', 'Snow', 'Highland shale', 'Black basalt', 'Red mesa sandstone', 'Moor tor') for n in range(1, 6)]),
    'NAT-12': ('BM', 1, [f'{s} cliff: {m}' for s in ('Meadow granite', 'Snow', 'Highland shale', 'Black basalt', 'Red mesa sandstone', 'Moor tor')
                         for m in ('straight face', 'outer corner', 'inner corner', 'top cap')]),
}
NAT_HINT = [(r'[Ss]now|Frostpine', 'EC', 5), (r'Highland pine', 'ST', 2), (r'Highland|highland', 'IR', 10), (r'basalt|Charred|Ash', 'CF', 20), (r'mesa|arid|Scrub|Succulent|Tumbleweed|Dry tree', 'RL', 20),
            (r'[Mm]oor|Heather|Peat|Gibbet', 'VM', 20), (r'[Aa]utumn|Maple|Beech|Giant oak|Leaf-litter|Scorched|Turnip', 'HF', 5), (r'Hop', 'ST', 3), (r'Willow', 'BM', 4)]
for nid, (z0, l0, names) in NAT.items():
    lib = next(clean(c[2]) for h1, h2, h3, c in table(L3) if c and c[0] == nid)
    for nm in names:
        z, l = next(((z, l) for rx, z, l in NAT_HINT if re.search(rx, nm)), (z0, l0))
        if nid in ('NAT-04', 'NAT-05', 'NAT-06', 'NAT-07', 'NAT-08', 'NAT-03', 'NAT-02'):
            z, l = (z0, l0) if not (nid == 'NAT-03' and 'Highland' in nm) and not (nid == 'NAT-04' and re.search('Peat|Gibbet', nm)) else (z, l)
        look = ('chunky faceted stone with flat painted planes and a few strong cracks' if nid in ('NAT-11', 'NAT-12')
                else 'crossed cards with a painted clump, soft at the base so it blends into the ground' if nid == 'NAT-10'
                else 'rows or patches of a crop as low cards and simple shapes' if nid == 'NAT-09'
                else 'glowing caps and crystals carry their own light (emissive)' if nid == 'NAT-08'
                else 'thick trunk, few heavy branches, leaf clumps as cards')
        add(f'{nid}-{slug(nm)}', 'Nature model', nm, f'{nm}, from the {lib.lower()} library. Stylised: {look}; painted light from above. {zcue(z)}',
            f'Scattered by the world generator in {ZONES[z][0]} and zones like it', z, l, nid)
for nm, z, l in [('River and stream surface', 'BM', 1), ('Pond surface', 'BM', 1), ('Millrace channel surface', 'ST', 3), ('Waterfall and dam spillway', 'ST', 1),
                 ('Harbour sea surface', 'SOL', 5), ('Lava and slag surface', 'CF', 20), ('Sulfur pool surface', 'CF', 24), ('Bog water surface', 'TM', 10)]:
    add(f'NAT-13-{slug(nm)}', 'Water surface', nm, f'{nm}: tiling painted surface with flow direction and edge foam for the one world shader. {zcue(z)}', 'Water and liquids', z, l, 'NAT-13')

ZROW = {'BM': 'BM', 'EC': 'EC', 'HF': 'HF', 'RW': 'RW', 'ST': 'ST', 'SD': 'SD', 'TM': 'TM', 'IR': 'IR', 'CF': 'CF', 'RL': 'RL', 'VM': 'VM'}
zrows = defaultdict(list)
for h1, h2, h3, c in table(L3):
    m = re.fullmatch(r'Z-([A-Z]{2})-(\d+)', c[0]) if c else None
    if m:
        zrows[m.group(1)].append((c[0], clean(c[2])))


def quest_level_for(name, zone):
    key = re.sub(r's$', '', name.lower().split(' (')[0])
    for qid, (qz, ql, qn, qo) in QUEST.items():
        if qz == zone and key and key in qo.lower():
            return ql
    return None


for zc, rows in zrows.items():
    lo = ZONES[zc][1]
    hi = {1: 5, 5: 10, 10: 20, 20: 30}[lo]
    body = [r for r in rows if not re.match(r'(Terrain set|Floor set|Sky|Lighting presets|Quest objects)', r[1])]
    for rid, text in rows:
        if re.match(r'(Terrain set|Floor set)', text):
            for t in expand(text.split(':', 1)[1], [', ']):
                add(f'{rid}-{slug(t)}', 'Terrain texture', f'{ZONES[zc][0]} ground: {t}', f'Tiling ground texture of {t}. Hand-painted, colour only, soft painted shading, no photographic detail; tiles without a visible repeat at 4 by 4. {zcue(zc)}',
                    f'Terrain of {ZONES[zc][0]}', zc, lo, rid)
        elif re.match(r'(Sky|Lighting presets)', text):
            for t in expand(text.split(':', 1)[1], [', ', '; ']):
                add(f'{rid}-{slug(t)}', 'Sky preset', f'{ZONES[zc][0]} {"lighting" if zc == "SD" else "sky"}: {t}', f'{"Lighting" if zc == "SD" else "Sky and light"} preset: {t}. Sets sky colours, sun or lamp colour, fog colour and distance, and the zone colour grade. {zcue(zc)}',
                    f'{ZONES[zc][0]} time of day and weather', zc, lo, rid)
        elif text.startswith('Quest objects'):
            for t in expand(text.split(':', 1)[1], [', ']):
                ql = quest_level_for(t, zc) or (lo + hi) // 2
                add(f'{rid}-{slug(t)}', 'Prop', f'Quest object: {t}', f'{t}: quest prop for {ZONES[zc][0]}, small and readable, sparkles for players on its quest. {zcue(zc)}', f'Quests in {ZONES[zc][0]}', zc, ql, rid)
        else:
            idx = body.index((rid, text))
            lv = locate(text)
            lv = lv[1] if lv and lv[0] == zc else lo + round((hi - lo) * idx / max(1, len(body) - 1))
            kit = ', '.join(re.findall(r'KIT-\d+(?:/\d+)?', text))
            label, _, rest = text.partition(':')
            els = []
            for e in (expand(rest, [', ', '; ']) if rest.strip() else []):
                if els and re.match(r'(two|three|four|\d+) (states|interior)|with |incl|and |plus |\d+ states', e):
                    els[-1] += ', ' + e                       # a note about the previous piece, not a piece
                else:
                    els.append(e)
            els = els if els else expand(text, ['; '])
            for e in els:
                nm = re.sub(r" *\(KIT[^)]*\)", "", e) if not rest.strip() else f'{re.sub(r" *\(KIT[^)]*\)", "", label).strip()}: {e}'
                add(f'{rid}-{slug(e)}', 'Set piece', nm, f'{nm}. Location set piece in {ZONES[zc][0]}{", built from " + kit if kit else ""}; unique shapes are modelled, the rest is assembled from kit pieces and nature. {zcue(zc)}',
                    f'{ZONES[zc][0]}: {re.sub(r" *\(KIT[^)]*\)", "", label).strip()}', zc, lv, rid)

for h1, h2, h3, c in table(L3):
    if not c or not re.match(r'(CITY|INS)-', c[0]):
        continue
    text = clean(c[2])
    z, l = locate(text) or ('SOL', 5)
    m = re.match(r'(.+?)(?: \((KIT[^)]*)\))?(?: at monumental scale\))?[,:] ?(.*)$', text)
    head = re.split(r'[:(]', text)[0].strip()
    rest = text.split(':', 1)[1] if ':' in text and ' · ' in text else ''
    els = split_top(rest, [' · ']) if rest else [text]
    for e in els:
        add(f'{c[0].split("–")[0]}-{slug(e)}', 'Set piece', f'{head}: {e}' if rest else e,
            f'{e}. Part of {head}; built from its kit with unique shapes modelled where the kit has none. {zcue(z)}', head, z, l, c[0])

# ----------------------------------------------------------------------------- list 4: effects
L4 = 'docs/10-art/04-vfx.md'
SHARED = {
    'VFX-S01': [f'Cast-hand glow, {s}: {st}' for s in SCHOOLS7 for st in ('ready', 'loop', 'release')],
    'VFX-S02': [f'Generic projectile, {s}: bolt with trail' for s in SCHOOLS7],
    'VFX-S03': [f'Generic impact, {s}: {sz}' for s in SCHOOLS7 for sz in ('small', 'large')],
    'VFX-S04': [f'Generic buff-up swirl, {s}' for s in SCHOOLS7],
    'VFX-S05': [f'Generic debuff cloud, {s}' for s in SCHOOLS7],
    'VFX-S06': [f'Heal sparkle, {s}: {sz}' for s in ('Holy', 'Nature') for sz in ('small', 'large')],
    'VFX-S07': ['Melee hit sparks', 'Blood puff', 'Block spark', 'Parry clang flash', 'Miss whoosh'],
    'VFX-S08': [f'Weapon swing trail: {w}' for w in ('one-handed', 'two-handed', 'dagger', 'polearm', 'staff')],
    'VFX-S09': [f'Ground telegraph decal: {sh}, {col}' for sh in ('circle', 'cone', 'line', 'ring', 'donut') for col in ('enemy red', 'friendly blue-green')],
    'VFX-S11': ['Interrupt and school-lockout burst'],
    'VFX-S12': ['Threat and taunt flash over the target\'s head'],
}
PARTS = {'Cast': 'on the caster while casting', 'Proj': 'projectile in flight', 'Hit': 'impact on the target', 'Aura': 'persistent effect on a unit',
         'Area': 'ground effect', 'Weapon': 'weapon trail or glow'}
CLASS_OF = {'F': 'Fighter', 'C': 'Cleric', 'D': 'Druid'}
VFX_PARTS = defaultdict(list)     # row id -> [(ability, part label, level)] for sounds
MLIB = []                          # creature ability library elements, for icons and sounds
BOSSFX = []                        # (row id, element, zone, level)
for h1, h2, h3, c in table(L4):
    if not c or not re.fullmatch(r'VFX-[A-Z]\d+', c[0]):
        continue
    vid, name, detail = c[0], clean(c[2]), clean(c[3]) if len(c) > 3 else ''
    fam = vid[4]
    if fam == 'S':
        els = SHARED.get(vid) or expand(name.split(':', 1)[-1], [', '])
        for e in els:
            sch = next((s for s in SCHOOLS7 if s in e), None)
            add(f'{vid}-{slug(e)}', 'Effect', e, f'Shared effect block: {e}.' + (f' School look: {SCHOOL_LOOK[sch]}.' if sch else '') + f' Used for: {detail.lower()}.',
                detail, 'ANY', 1, vid)
    elif fam in 'FCD':
        cls = CLASS_OF[fam]
        aname = re.sub(r'\(.*?\)', '', name).strip()
        if aname.startswith('Passive procs'):
            for e in split_top(name.split(':', 1)[1], [', ']):
                lv = ability_level(e.split(' ')[0] if e.split(' ')[0].lower() in TAL else ' '.join(e.split(' ')[:2]), 15)
                add(f'{vid}-{slug(e)}', 'Effect', f'{cls} proc: {e}', f'Small proc effect for the {cls}: {e}. Brief, under 40 particles, in the class\'s school colours.', f'{cls} talents', 'ANY', lv, vid)
            continue
        lv = ability_level(aname, 10)
        if aname.startswith('Stances'):
            for e in split_top(detail.split(':', 1)[1], [', ']):
                add(f'{vid}-{slug(e)}', 'Effect', f'Fighter stance flourish: {e}', f'Brief flourish when the Fighter enters a stance: {e}.', 'Fighter stances', 'ANY', ability_level(e.split(' ')[0] + ' stance', 1), vid)
            continue
        if aname.startswith('Verdict'):
            add(f'{vid}-proj', 'Effect', 'Verdict: projectile', 'Thrown hammer of light, gold with a short trail.', 'Cleric ability Verdict', 'ANY', lv, vid)
            for o, look in [('base', 'plain gold burst'), ('Radiance', 'sunburst'), ('Zealot', 'red-gold brand on the target'), ('Justice', 'chains of light'),
                            ('Light', 'soft glow mark'), ('Command', 'large hammer strike')]:
                add(f'{vid}-hit-{slug(o)}', 'Effect', f'Verdict: hit, {o}', f'Impact of Verdict under the {o} Oath: {look}. School look: {SCHOOL_LOOK["Holy"]}.', 'Cleric ability Verdict', 'ANY', lv, vid)
            VFX_PARTS[vid] = [('Verdict', 'Proj', lv), ('Verdict', 'Hit', lv)]
            continue
        for p in split_top(detail, ['; ']):
            label, _, look = p.partition(':')
            label = label.strip()
            if label not in PARTS:
                label, look = 'Aura' if 'UI' not in p else '', p
            if not label:
                continue
            add(f'{vid}-{slug(label)}', 'Effect', f'{aname}: {label.lower()}', f'{cls} ability {aname}, {PARTS[label]}: {look.strip()}.', f'{cls} ability {aname}', 'ANY', lv, vid)
            VFX_PARTS[vid].append((aname, label, lv))
    elif fam == 'I':
        els = expand(re.sub(r'^[^:]+: ', '', name) if ':' in name else name, [', ', '; '])
        if vid == 'VFX-I01':
            els = [f'Potion drink, {t}' for t in ('red', 'blue', 'purple', 'green', 'orange')]
        if vid == 'VFX-I10':
            els = [f'Trinket use flash, {s}' for s in SCHOOLS7] + [f'Trinket: {t}' for t in ('Hollowed Heart', 'Acorn of the First Oak', 'Heart of the Cinder Wyrm', 'Eye of the Maw', "Vitrea's Lens reflect", 'Shard of the Hollow Crown')]
        if vid == 'VFX-I05':
            els = [f'Weapon enchant glow: {t}' for t in ('Striking (white)', 'Impact (amber)', 'Hollowbane (violet)', 'Dawnfire (orange flame)')]
        if vid == 'VFX-I07':
            els = [f'Dynamite fuse and explosion, {s}' for s in ('small', 'medium', 'large', 'huge')] + ['Bomb stun', 'Target dummy pop', 'Clockwork ram charge', 'Clockwork ram blast', 'Resuscitator shock', 'Parachute']
        lvl = {'VFX-I01': 3, 'VFX-I02': 5, 'VFX-I03': 1, 'VFX-I04': 5, 'VFX-I05': 10, 'VFX-I06': 5, 'VFX-I07': 10, 'VFX-I08': 20, 'VFX-I09': 8, 'VFX-I10': 15,
               'VFX-I11': 15, 'VFX-I12': 5, 'VFX-I13': 5, 'VFX-I14': 1, 'VFX-I15': 30}[vid]
        ihead = name.split(':')[0].strip() if ':' in name and vid not in ('VFX-I10',) else ''
        for e in els:
            disp = f'{ihead}: {e}' if ihead and ihead.lower() not in e.lower() else e
            add(f'{vid}-{slug(e)}', 'Effect', disp, f'Item or profession effect: {disp}. Small and brief, under 60 particles.', clean(c[2]).split(':')[0], 'ANY', lvl, vid)
    elif fam == 'M':
        body = name.split(':', 1)[1] if ':' in name and not name.startswith('Thrown') else name
        if name.startswith('Thrown'):
            els = [f'Thrown {t}' for t in split_top(name.split(':', 1)[1], [', '])]
        else:
            els = []
            for e in expand(re.sub(r'\(\d+[^)]*\)', '', body), [', ', '; ']):
                els += [x.strip() for x in e.split(' / ')] if ' / ' in e else [e]
        z, l = (creature(detail.split(',')[0]) or ('ANY', 5))
        fam_level = {'VFX-M01': 1, 'VFX-M02': 2, 'VFX-M03': 2, 'VFX-M04': 3, 'VFX-M05': 3, 'VFX-M06': 3, 'VFX-M07': 3, 'VFX-M08': 3, 'VFX-M09': 2, 'VFX-M10': 12,
                     'VFX-M11': 12, 'VFX-M12': 8, 'VFX-M13': 10, 'VFX-M14': 6, 'VFX-M15': 7, 'VFX-M16': 4, 'VFX-M17': 8, 'VFX-M18': 3, 'VFX-M19': 5, 'VFX-M20': 8,
                     'VFX-M21': 5, 'VFX-M22': 7, 'VFX-M23': 12, 'VFX-M24': 7, 'VFX-M25': 12, 'VFX-M26': 8, 'VFX-M27': 22, 'VFX-M28': 1}[vid]
        for e in els:
            add(f'{vid}-{slug(e)}', 'Effect', f'Creature ability: {e}', f'Reusable creature ability effect: {e}. Used by {detail.lower()}.', f'Creatures: {detail}', 'ANY', fam_level, vid)
            MLIB.append((vid, e, fam_level))
    elif fam == 'B':
        z, l = {'VFX-B01': ('BM', 5), 'VFX-B02': ('IR', 13), 'VFX-B03': ('GC', 13), 'VFX-B04': ('SW', 20), 'VFX-B05': ('HK', 27), 'VFX-B06': ('HT', 30),
                'VFX-B07': ('WB', 30), 'VFX-B08': ('WB', 30), 'VFX-B09': ('WB', 30), 'VFX-B10': ('TM', 15)}[vid]
        text = detail if vid != 'VFX-B10' else name.split('(', 1)[1].rsplit(')', 1)[0]
        for e in expand(text, ['; ', ', ']):
            el = locate(e)
            ez, elv = (el if el and vid in ('VFX-B10',) else (z, l))
            add(f'{vid}-{slug(e)}', 'Effect', f'{name.split("(")[0].strip()}: {e}', f'Bespoke encounter effect: {e}. Up to 600 particles; must read clearly as something to avoid or use. {zcue(ez)}',
                f'Encounter: {name}', ez, elv, vid)
            BOSSFX.append((vid, e, ez, elv, name.split('(')[0].strip()))
    elif fam == 'W':
        text = name
        head, _, rest = text.partition(':')
        els = expand(rest, [', ', '; ']) if rest else expand(text, [', ', '; '])
        if vid == 'VFX-W02':
            els = ['available "!" (gold)', 'in-progress "?" (grey)', 'complete "?" (gold)', 'repeatable (blue)', 'class quest (class colour)', 'low-level (dim)']
        if vid == 'VFX-W18':
            els = [f'colour grade for {ZONES[z][0]}' for z in ('BM', 'ST', 'HF', 'RW', 'EC', 'SD', 'TM', 'IR', 'CF', 'RL', 'VM')] + ['underwater tint', 'low-health vignette', 'stun blur', 'ghost desaturation', 'drunk wobble']
        lvl = {'VFX-W01': 1, 'VFX-W02': 1, 'VFX-W03': 1, 'VFX-W04': 10, 'VFX-W05': 1, 'VFX-W06': 1, 'VFX-W07': 1, 'VFX-W08': 1, 'VFX-W09': 1, 'VFX-W10': 1, 'VFX-W11': 1,
               'VFX-W12': 4, 'VFX-W13': 1, 'VFX-W14': 3, 'VFX-W15': 10, 'VFX-W16': 30, 'VFX-W17': 4, 'VFX-W18': 1}[vid]
        for e in [re.sub(r'\s*\(\d+\)$', '', x) for x in els]:
            loc = locate(e) or next(((z, ZONES[z][1]) for z in ZONES if ZONES[z][0] in e), None)
            ez, elv = loc if loc else ('ANY', lvl)
            add(f'{vid}-{slug(e)}', 'Effect', f'{head.strip() if rest else "World effect"}: {e}', f'World or feedback effect: {e}. {zcue(ez)}', head.strip(), ez, max(lvl, elv) if loc else lvl, vid)
# ----------------------------------------------------------------------------- list 5: interface
L5 = 'docs/10-art/05-ui.md'
TREES = [('Fighter', 'Bulwark'), ('Fighter', 'Reaver'), ('Fighter', 'Greatarms'), ('Cleric', 'Aegis'), ('Cleric', 'Grace'), ('Cleric', 'Reckoning'),
         ('Druid', 'Verdance'), ('Druid', 'Stormcall'), ('Druid', 'Starweave')]
UILVL = {'UI-H04': 1, 'UI-H05': 10, 'UI-H11': 1, 'UI-H21': 1, 'UI-H23': 1, 'UI-W03': 5, 'UI-W05': 10, 'UI-W10': 5, 'UI-W11': 10, 'UI-W14': 5, 'UI-W15': 5,
         'UI-W18': 3, 'UI-W19': 5, 'UI-W21': 10, 'UI-W22': 10, 'UI-W23': 3, 'UI-W24': 5, 'UI-W25': 30, 'UI-W26': 10, 'UI-W33': 5, 'UI-W34': 5, 'UI-W36': 13,
         'UI-C06': 10, 'UI-C07': 10, 'UI-C09': 5, 'UI-C05': 5, 'UI-C04': 10}
UI_FIX = {'arrow ×4': 'arrow up, arrow down, arrow left, arrow right',
          'quality borders ×6': 'quality border Poor, quality border Common, quality border Uncommon, quality border Rare, quality border Epic, quality border Legendary',
          'Standing bars ×8 colours': 'standing bar Hated, standing bar Hostile, standing bar Unfriendly, standing bar Neutral, standing bar Friendly, standing bar Honored, standing bar Revered, standing bar Exalted',
          ', faction crests ×5': '', 'Race buttons ×2 (+ locked silhouettes for future races)': 'race button frame, locked silhouette for future races',
          'class buttons ×3 with role tags': 'class button Fighter with role tags, class button Cleric with role tags, class button Druid with role tags',
          'class trees ×3': 'three class-tree tabs', 'Backdrop ×2': 'backdrop'}
# Rows whose look was decided after the art list was written; the id stays the one the row gives.
UI_SAY = {'UI-H12-20-segments': ('XP bar: 10 sections', 'The fill is divided into 10 equal sections ("bubbles") by thin dividers drawn over it; the bar sits directly on the top edge of the main action bar, the same width, and its text is centred inside the fill.')}
LOADING = [(ZONES[z][0], z, ZONES[z][1]) for z in ('BM', 'ST', 'HF', 'RW', 'EC', 'SD', 'TM', 'IR', 'CF', 'RL', 'VM', 'SOL', 'HAM', 'GC', 'SW', 'HK', 'HT', 'CR', 'SEA')] \
    + [('generic A: a road at dawn', 'CORE', 0), ('generic B: a campfire at night', 'CORE', 0)]
for h1, h2, h3, c in table(L5):
    if not c or not re.fullmatch(r'UI-[A-Z]\d+', c[0]):
        continue
    uid, name = c[0], re.sub(r'\s*×\d+', '', clean(c[2]))
    parts = clean(c[3]) if len(c) > 3 else ''
    lv = UILVL.get(uid, 0 if uid[3] in 'FHS' else 1)
    zone = 'CORE' if lv == 0 else 'ANY'
    style = 'Stone-and-brass Concord skin, painterly, high contrast, readable at 1080p.'
    if uid == 'UI-F02':
        for f, d in [('Title serif', 'display serif with chiselled terminals for titles and zone banners'), ('Body sans', 'plain humanist sans for body text and tooltips, clear at 12 px'),
                     ('Number and combat font', 'bold condensed face for damage numbers and timers')]:
            add(f'{uid}-{slug(f)}', 'Font', f, f'{f}: {d}. Latin Extended coverage.', 'All interface text', 'CORE', 0, uid)
        continue
    if uid in ('UI-F09', 'UI-M08', 'UI-C10'):
        if uid == 'UI-C10':
            for b in BODIES:
                add(f'{uid}-{slug(b)}', 'UI texture', f'Portrait fallback silhouette: {b}', f'Plain dark silhouette of the {b.lower()} head and shoulders in a round frame.', 'Unit frames before the live portrait renders', 'CORE', 0, uid)
        continue
    if uid == 'UI-S05':
        for nm, z, l in LOADING:
            add(f'{uid}-{slug(nm)}', 'Painting', f'Loading screen: {nm}', f'Loading-screen painting of {nm}: one wide establishing view with its landmark, no characters in the foreground, no text. {zcue(z)}',
                'Shown while the place loads', z, l, uid)
        add(f'{uid}-bar', 'UI texture', 'Loading bar and tip strip', f'Loading progress bar and a text strip for tips. {style}', 'Loading screens', 'CORE', 0, uid)
        continue
    if uid == 'UI-S06':
        for race, z in (('human', 'BM'), ('dwarf', 'ST')):
            for i in range(1, 4):
                add(f'{uid}-{race}-{i}', 'Painting', f'Intro card {i} of 3, {race}', f'Still painting {i} of 3 for the {race} introduction: the homeland, the trouble, the call to the starting camp. Room at the bottom for text. {zcue(z)}',
                    'First login of a new character', 'CORE', 0, uid)
        continue
    if uid == 'UI-M03':
        for z in ('BM', 'ST', 'HF', 'RW', 'EC', 'SD', 'TM', 'IR', 'CF', 'RL', 'VM'):
            add(f'{uid}-{z}', 'Painting', f'Zone map: {ZONES[z][0]}', f'Painted top-down zone map of {ZONES[z][0]} on parchment, made over the render of the built zone so it matches the ground; roads, water, hubs and landmark drawn, no text. {zcue(z)}',
                'World map window', z, ZONES[z][1], uid)
        continue
    MAPS = {'UI-M01': [('World map: the three continents, Sundrel shrouded', 'CORE', 1)],
            'UI-M02': [('Continent map: Meridia, unbuilt half as unexplored wilderness', 'BM', 1), ('Continent map: Khazrun, unbuilt half as unexplored wilderness', 'ST', 1)],
            'UI-M04': [(f'Stoneheart Deeps layer map: {x}', 'SD', 5) for x in ('Upper Galleries', 'Great Cavern', 'Underworks')],
            'UI-M05': [('City map: Solhaven', 'SOL', 5), ('City map: Hammerdeep', 'HAM', 5)] + [(f'Hammerdeep level layer {i}', 'HAM', 5) for i in (1, 2, 3)],
            'UI-M06': [('Instance map: Gallowmere Crypts', 'GC', 13), ('Instance map: The Slagworks', 'SW', 20), ('Instance map: Hollowspire Keep', 'HK', 27),
                       ('Instance map: The Hollow Throne', 'HT', 30), ('Instance map: Crownfall', 'CR', 10), ('Instance map: The Dustpit', 'DP', 24)],
            'UI-M07': [('Eyrie route map: Meridia', 'BM', 3), ('Eyrie route map: Khazrun', 'ST', 3)]}
    if uid in MAPS:
        for nm, z, l in MAPS[uid]:
            add(f'{uid}-{slug(nm)}', 'Painting', nm, f'{nm}. Painted on parchment in the map style, no text. {zcue(z)}', 'Map windows', z if z != 'CORE' else 'ANY', l, uid)
        continue
    CRESTS = {'UI-C01': ['Allegiance crest: Concord (blue)', 'Allegiance crest: Wildpact (yellow-green)', 'Allegiance crest: Covenant (red)'],
              'UI-C02': [f'Race button: {b}' for b in BODIES],
              'UI-C03': [f'Class crest: {cl}, {sz}' for cl in ('Fighter', 'Cleric', 'Druid') for sz in ('large', 'small', 'minimap size')],
              'UI-C04': [f'Talent tree crest: {cl} {t}' for cl, t in TREES],
              'UI-C05': [f'Reputation crest: {f}' for f in ('Solhaven', 'Hammerdeep', 'Thornwick Wardens', 'Freeholders', 'Athenaeum')],
              'UI-C06': [f'Battleground team banner: {t}' for t in ('red', 'blue', 'yellow')],
              'UI-C07': [f'Raid target icon: {t}' for t in ('star', 'circle', 'diamond', 'triangle', 'moon', 'square', 'cross', 'skull')],
              'UI-C08': [f'Role icon: {t}' for t in ('tank', 'healer', 'damage')],
              'UI-C09': [f'Profession crest: {p}' for p in ('Mining', 'Herbalism', 'Skinning', 'Blacksmithing', 'Leatherworking', 'Tailoring', 'Alchemy', 'Enchanting', 'Engineering', 'Cooking', 'Fishing', 'First Aid')]}
    if uid in CRESTS:
        for nm in CRESTS[uid]:
            add(f'{uid}-{slug(nm)}', 'UI texture', nm, f'{nm}. Bold heraldic emblem, flat painted, readable small.', name, zone, lv, uid)
        continue
    for a, b in UI_FIX.items():
        parts = parts.replace(a, b)
    els = expand(parts, [', ', '; ']) if parts and uid != 'UI-F01' else []
    if uid == 'UI-W05':
        for cl, t in TREES:
            add(f'{uid}-bg-{slug(t)}', 'Painting', f'Talent tree background: {cl} {t}', f'Tall background painting for the {cl} {t} talent tree, dark enough that gold talent buttons read on top; subject is the tree\'s theme.', 'Talents window', 'ANY', 10, uid)
        els = [e for e in els if 'background' not in e and e != '3 tabs']
    if uid == 'UI-S01':
        add(f'{uid}-keyart', 'Painting', 'Login key art', 'Animated key-art scene in layers: Solhaven harbour at dawn with the ship The Hearth-Oath leaving for the mountain on the horizon. No text.', 'Login screen', 'CORE', 0, uid)
        els = ['logo placement frame', 'account fields', 'buttons']
    if uid == 'UI-S03':
        for nm in ('human backdrop: Larkhill hearth', 'dwarf backdrop: Sunbank hearth'):
            add(f'{uid}-{slug(nm)}', 'Set piece', f'Character select {nm}', f'Small 3D backdrop scene for the character-select screen, {nm}; warm firelight, a spot for the character to stand.', 'Character select', 'CORE', 0, uid)
        els = ['10-slot character list', 'enter, create and delete buttons']
    if not els:
        els = [name]
    for e in els:
        nm = e if e == name else f'{name}: {e}'
        say = UI_SAY.get(f'{uid}-{slug(e)}')
        if say:
            nm = say[0]
        add(f'{uid}-{slug(e)}', 'UI texture', nm, f'Interface art for "{nm}". {say[1] + " " if say else ""}{style}', name, zone, lv, uid)

ZHEAD = {v[0]: k for k, v in ZONES.items()}
ZHEAD['The Dustpit'], ZHEAD['Crownfall'], ZHEAD['Gallowmere Crypts'] = 'DP', 'CR', 'GC'
for f in sorted(os.listdir(os.path.join(ROOT, 'docs', '13-world'))):
    if not re.match(r'0[1-8]-', f):
        continue
    for h1, h2, h3, c in table('docs/13-world/' + f):
        if h2 == 'Sub-areas' and len(c) > 2 and re.fullmatch(r'[A-Z]{2,3}', c[0]) and h1 in ZHEAD:
            z = ZHEAD[h1]
            add(f'UI-M03-mask-{z}-{slug(c[1])}', 'Map mask', f'Fog mask: {clean(c[1])} ({ZONES[z][0]})', f'Fog-of-war mask for the sub-area {clean(c[1])} on the {ZONES[z][0]} zone map, cut from its polygon.',
                'World map exploration', z, ZONES[z][1], 'UI-M03')

# ----------------------------------------------------------------------------- list 6: icons and list 7: named items
L6 = 'docs/10-art/06-icons.md'
MAT_LEVEL = [(r'Starmetal|Star Sapphire', 27), (r'Steel', 22), (r'Gold|Citrine|Jade', 20), (r'Iron|Heavy|Solid|Silk|Greater Astral|Large Glinting|Aether|Vault|Hollow Shard|Rift|Cinder|Pyrehound|Golden', 20),
             (r'Silver|Wool|Medium|Coarse|Bronze|Tin|Lesser Astral|Greater Spark|Small Glinting|Moss Agate|Dusk Opal|Moonstone|Mirejaw|Rimewing|Glimmer|Gargoyle|Ore-Bound', 10),
             (r'.', 5)]
HERB_L = {n: l for n, z, l in NODES}
STAT5 = ['Strength', 'Agility', 'Stamina', 'Intellect', 'Spirit']
ICON_FIX = {'stat buff ×5': [f'{s} buff' for s in STAT5], 'resist ×5': [f'{s} resistance' for s in ('Fire', 'Frost', 'Nature', 'Arcane', 'Shadow')],
            'shrine buffs ×3': ['Shrine of Steel buff', 'Shrine of Bloom buff', 'Shrine of Aether buff'],
            'Bread ×3 tiers': ['Brown Bread', 'Hard Cheese loaf', "Traveller's Pasty"], 'cheese ×3': ['Hard Cheese', 'Dale Cheese', 'Blue-veined Cheese'],
            'fruit ×3': ['Orchard Apple', 'Dale Plum', 'Mesa Fig'], 'scopes ×3 (1 icon, 3 tints)': ['Gun Scope'],
            'Copper Rod / Silver Rod / Golden Rod blank (1 shared + tints)': ['Enchanting Rod blank'], 'Sharpening stones ×4': [f'{t} Sharpening Stone' for t in ('Rough', 'Coarse', 'Heavy', 'Solid')],
            'weightstones ×4': [f'{t} Weightstone' for t in ('Rough', 'Coarse', 'Heavy', 'Solid')], 'Dynamite ×4': [f'{t} Dynamite' for t in ('Rough', 'Coarse', 'Heavy', 'Solid')],
            'bombs ×3': ['Small Bronze Bomb', 'Big Bronze Bomb', 'Iron Bomb'], 'arrows ×2': ['Rough Arrow', 'Sharp Arrow'], 'bullets ×2': ['Light Shot', 'Heavy Shot'],
            '6 bandages': ['Linen Bandage', 'Heavy Linen Bandage', 'Wool Bandage', 'Heavy Wool Bandage', 'Silk Bandage', 'Heavy Silk Bandage'],
            'Thread ×2': ['Coarse Thread', 'Fine Thread'], 'Vial ×2': ['Empty Vial', 'Leaded Vial'], 'Skeleton Keys ×2': ['Copper Skeleton Key', 'Iron Skeleton Key']}


def icon_names(text):
    out = []
    for el in split_top(text, [' · ']):
        el = el.strip()
        if el in ICON_FIX:
            out += ICON_FIX[el]
        elif ' / ' in el:
            out += spaced_slash(el)
        else:
            out += mult(el)
    return [re.sub(r'\s*\(.*?\)$', '', o).strip() for o in out]


def icon(aid, name, what, used, zone, level, source):
    add(aid, 'Icon', f'Icon: {name}', f'Square icon of {what.rstrip(" .")}. One subject, centred, on a simple dark vignette; strong silhouette, thick readable shapes, lit from the upper left, no text.', used, zone, level, source)


def recipe_table(rel, heading):
    out = []
    for h1, h2, h3, c in table(rel):
        if h2.startswith(heading) and len(c) > 2 and re.fullmatch(r'\d+', c[0]):
            out.append((clean(c[1]), int(c[0])))
    return out


def skill_level(skill):
    return min(30, max(5, round(skill / 7.5)))


for h1, h2, h3, c in table(L6):
    if not c or not re.fullmatch(r'ICO-[A-Z]\d+', c[0]):
        continue
    iid, group = c[0], clean(c[2])
    body = clean(c[3]) if len(c) > 3 else ''
    fam = iid[4]
    if fam in 'FCD':
        cls = CLASS_OF[fam]
        for nm in icon_names(body):
            icon(f'{iid}-{slug(nm)}', nm, f'the {cls} ability or talent "{nm}", in the class\'s school colours', f'{cls}: {group}', 'ANY', ability_level(nm, 10 if 'talent' in group.lower() else 1), iid)
    elif iid == 'ICO-G1':
        for nm in icon_names(body):
            icon(f'{iid}-{slug(nm)}', nm, f'the racial trait "{nm}"', 'Racial traits', 'CORE', 0, iid)
    elif iid == 'ICO-G2':
        for nm in icon_names(body):
            icon(f'{iid}-{slug(nm)}', nm, f'the general ability "{nm}"', 'Spellbook, general tab', 'ANY', 30 if nm == 'Riding' else 5 if nm in ('Find Minerals', 'Find Herbs', 'Fishing', 'Disenchant', 'Smelting', 'Basic Campfire') else 1, iid)
    elif iid == 'ICO-G3':
        for nm in ['One-handed swords', 'One-handed axes', 'One-handed maces', 'Daggers', 'Two-handed swords', 'Two-handed axes', 'Two-handed maces', 'Polearms', 'Staves',
                   'Bows', 'Crossbows', 'Guns', 'Thrown', 'Defense', 'Unarmed']:
            icon(f'{iid}-{slug(nm)}', f'{nm} skill', f'the weapon skill "{nm}"', 'Skills tab', 'ANY', 1, iid)
    elif iid == 'ICO-G4':
        for nm in icon_names(body):
            icon(f'{iid}-{slug(nm)}', nm, f'the profession {nm}, shown by its tool', 'Professions', 'ANY', 5, iid)
    elif iid == 'ICO-G5':
        for nm in icon_names(body):
            icon(f'{iid}-{slug(nm)}', nm, f'the status "{nm}"', 'Buff and debuff rows', 'ANY', 10 if re.search('Crown|[Ss]hrine|Deserter', nm) else 30 if nm == 'mounted' else 1, iid)
    elif iid == 'ICO-G6':
        seen = set()
        for vid, e, lv in MLIB:
            named = vid in ('VFX-M07', 'VFX-M08', 'VFX-M09', 'VFX-M10', 'VFX-M11', 'VFX-M12', 'VFX-M13', 'VFX-M14')
            if named or vid not in seen:
                seen.add(vid)
                icon(f'{iid}-{slug(e)}', f'creature ability, {e}', f'the creature ability "{e}"', 'Debuffs and cast bars from creatures', 'ANY', lv, iid)
    elif iid == 'ICO-G7':
        for nm, sk in recipe_table('docs/04-professions/crafting.md', '5. Enchanting'):
            for nm in ([x.strip() for x in nm.split(' / ')] if '—' in nm else []):
                icon(f'{iid}-{slug(nm)}', f'enchant, {nm}', f'the enchantment "{nm}": a rune glowing on that piece of gear', 'Enchanting', 'ANY', skill_level(sk), iid)
        for nm in ['Fire proc', 'Shadow proc', 'Nature proc', 'Life-steal proc']:
            icon(f'{iid}-{slug(nm)}', f'weapon {nm}', f'a weapon {nm.lower()}', 'Weapon procs', 'ANY', 15, iid)
    elif iid == 'ICO-E2':
        for (atype, band), sname in sorted(TIERSET.items()):
            lv = {'a': 1, 'b': 10, 'c': 20}[band]
            for slot in ['chest', 'legs', 'feet', 'hands', 'wrist', 'waist', 'head', 'shoulders']:
                icon(f'{iid}-{atype}-{band}-{slot}', f'{sname} {slot}', f'the {slot} piece of the generic {atype} set "{sname}", base colourway (other colourways tint it)', 'Unnamed green and random-suffix armor', 'ANY', lv, iid)
    elif iid == 'ICO-E3':
        for (wtype, band), m in sorted(TIERWPN.items()):
            icon(f'{iid}-{slug(wtype)}-{band}', f'{m} ({wtype})', f'the generic {wtype} "{m}"', 'Unnamed and random-suffix weapons', 'ANY', {'a': 1, 'b': 10, 'c': 20}[band], iid)
    elif iid == 'ICO-E4':
        for cd in CLOAKS:
            icon(f'{iid}-cloak-{slug(cd)}', f'cloak, {cd}', f'a folded {cd} cloak', 'Unnamed cloaks', 'ANY', 1 + 2 * CLOAKS.index(cd), iid)
        for t in ['brown linen shirt', 'red shirt', 'white formal shirt', 'class starting shirt', 'guild tabard']:
            icon(f'{iid}-{slug(t)}', t, f'a {t}', 'Shirts and tabards', 'ANY', 1 if 'shirt' in t else 10, iid)
    elif iid == 'ICO-E5':
        metals = ['Tin', 'Copper', 'Bronze', 'Silver', 'Electrum', 'Gold']
        for i, mt in enumerate(metals):
            icon(f'{iid}-ring-{slug(mt)}', f'{mt} Band', f'a plain {mt.lower()} ring', 'Unnamed rings', 'ANY', 15 + 3 * i, iid)
            icon(f'{iid}-neck-{slug(mt)}', f'{mt} Chain', f'a {mt.lower()} neck chain with a small pendant', 'Unnamed necklaces', 'ANY', 20 + 2 * i, iid)
        for t in ['gem-set ring', 'signet ring', 'bead necklace', 'tooth necklace', 'carved idol trinket', 'brass charm trinket', 'bone fetish trinket', 'lucky coin trinket',
                  'small hourglass trinket', 'glass vial trinket']:
            icon(f'{iid}-{slug(t)}', t, f'a {t}', 'Unnamed jewellery and trinkets', 'ANY', 18, iid)
    elif iid == 'ICO-E6':
        for t in ['Psalter, plain', 'Psalter, gilded', 'Charm, carved wood', 'Charm, antler and feather']:
            icon(f'{iid}-{slug(t)}', f'relic: {t}', f'a relic ({t.lower()})', 'Cleric and Druid relic slot', 'ANY', 10, iid)
    elif iid == 'ICO-E7':
        for nm in icon_names(body.split(' = ')[0]):
            icon(f'{iid}-{slug(nm)}', nm, f'the bag "{nm}"', 'Bags', 'ANY', {'Small Pouch': 1, 'Linen Bag': 5, 'Woolen Bag': 12, 'Small Silk Pack': 22}.get(nm, 20), iid)
    elif iid == 'ICO-E8':
        for t in ['helm', 'shoulders', 'chest', 'hands', 'legs']:
            icon(f'{iid}-token-{t}', f'Vaultforged token: {t}', f'a tarnished imperial bronze token stamped with a {t} mark', 'Raid tier set tokens', 'HT', 30, iid)
    elif iid == 'ICO-E10':
        for t in ['bay horse', 'black horse', 'chestnut horse', 'grey horse', 'grey ram', 'brown ram', 'white ram', 'black ram', 'Vault Charger']:
            icon(f'{iid}-{slug(t)}', f'mount: {t}', f'a bridle and head of the {t} mount', 'Mounts', 'HT' if 'Vault' in t else 'ANY', 30, iid)
    elif fam == 'M':
        for nm in icon_names(body):
            lv = HERB_L.get(nm) or next(l for rx, l in MAT_LEVEL if re.search(rx, nm))
            icon(f'{iid}-{slug(nm)}', nm, f'the material "{nm}": a small pile or single piece on plain ground', f'Materials: {group}', 'ANY', lv, iid)
    elif iid in ('ICO-K1', 'ICO-K2'):
        src = ('docs/04-professions/crafting.md', '4. Alchemy') if iid == 'ICO-K1' else ('docs/04-professions/secondary.md', '1. Cooking')
        for nm, sk in recipe_table(*src):
            icon(f'{iid}-{slug(nm)}', nm, f'the {"potion or elixir" if iid == "ICO-K1" else "cooked dish"} "{nm}"', group, 'ANY', skill_level(sk) if iid == 'ICO-K1' else max(1, round(sk / 7.5)), iid)
        if iid == 'ICO-K2':
            for h1b, h2b, h3b, cb in table('docs/04-professions/secondary.md'):
                if h2b.startswith('2. Fishing') and len(cb) == 3 and re.fullmatch(r'\d+', cb[0]):
                    for nm in (spaced_slash(cb[1]) if len(cb[1].split(' / ')[-1].split()) == 1 else cb[1].split(' / ')):
                        icon(f'{iid}-{slug(nm)}', clean(nm), f'the cooked fish dish "{clean(nm)}"', group, 'ANY', max(1, round(int(cb[0]) / 7.5)), iid)
    elif iid == 'ICO-K4':
        for h1b, h2b, h3b, cb in table('docs/04-professions/secondary.md'):
            if h2b.startswith('2. Fishing') and len(cb) == 5 and re.fullmatch(r'\d+', cb[1]):
                z, l = locate(cb[0]) or ('ANY', 5)
                for nm in (cb[2], cb[3].split(' → ')[0]):
                    icon(f'{iid}-{slug(nm)}', clean(nm), f'the fish "{clean(nm)}"', 'Fishing catches', z, max(5, l), iid)
        icon(f'{iid}-pike-oil', 'Pike Oil', 'a small flask of fish oil', 'Fishing by-product', 'ST', 5, iid)
    elif fam == 'K':
        for nm in icon_names(re.sub(r'^\d+ ', '', body) if iid != 'ICO-K6' else body):
            lv = 3 if iid in ('ICO-K3', 'ICO-K5') else 30 if iid == 'ICO-K11' else 10
            if iid == 'ICO-K3':
                cz = creature(re.sub(r' (Meat|Haunch|Flank|Egg|Tail|Ribs|Drumstick|Fillet|Leg|Eye|Wing|Pellet)$', '', nm).replace('Stringy ', '').replace('Gooey ', ''))
                lv = cz[1] if cz else 8
            icon(f'{iid}-{slug(nm)}', nm, f'the consumable or ingredient "{nm}"', group, 'ANY', lv, iid)
    elif iid == 'ICO-Q1':
        for nm in ['Blacksmithing plan', 'Leatherworking pattern', 'Tailoring pattern', 'Alchemy recipe', 'Enchanting formula', 'Engineering schematic', 'Cooking recipe',
                   'First Aid manual', 'Fishing handbook']:
            icon(f'{iid}-{slug(nm)}', nm, f'a {nm.lower()}: a rolled or folded paper with that craft\'s mark, tinted by quality', 'Recipe items', 'ANY', 5, iid)
    elif iid == 'ICO-Q3':
        for nm in ['Wolf Fang', 'Matted Pelt', 'Cracked Boar Tusk', 'Bristle Tuft', 'Spider Leg Husk', 'Torn Web Sac', 'Bear Claw', 'Lynx Whisker', 'Chipped Ram Horn', 'Stag Hoof',
                   'Fox Tail Tuft', 'Bent Feather', 'Bat Ear', 'Cracked Snapper Shell', 'Mirejaw Tooth', 'Shed Skink Skin', 'Scorpion Pincer', 'Beetle Wing-Case', 'Rat Tail', 'Wyrm Scale Chip',
                   'Strider Claw', 'Drake Scale Fleck', 'Burnt Candle Stub', 'Bent Pick', 'Gnawed Pebble', 'Fish Scale Handful', 'Ogre Toe-Ring', 'Howler Bone Chime', 'Harpy Quill', 'Bone Splinter',
                   'Grave Dirt Clod', 'Tattered Shroud', 'Ooze Residue', 'Cooled Slag Lump', 'Chipped Gargoyle Stone', 'Burst Straw Bundle', 'Stripped Gear', 'Dented Armour Plate', 'Rotten Bark Strip', 'Branded Rag']:
            icon(f'{iid}-{slug(nm)}', nm, f'the vendor-trash item "{nm}", drab and grey-toned', 'Grey loot from creatures', 'ANY', 1, iid)
    elif iid in ('ICO-Q4', 'ICO-Q5', 'ICO-Q6'):
        for nm in icon_names(body):
            z, l = (locate(nm) or ('ANY', 1)) if iid != 'ICO-Q5' else {'Vault Key': ('HT', 30), "Slagheart's Crucible-Shard": ('SW', 23), "Seraphine's Signet": ('HK', 30),
                                                                    "Behemoth's Heart": ('SD', 10), 'Spire Key': ('TM', 19), "Smuggler's Key": ('IR', 12)}.get(nm, ('ANY', 20))
            icon(f'{iid}-{slug(nm)}', nm, f'{"the key or token" if iid == "ICO-Q5" else "the"} "{nm}"', group, z, l, iid)

ITEM_SRC = {'t1-brightmead-vale': 'BM', 't2-embercrag-hollow': 'EC', 't2-harrowfield': 'HF', 't2-russetwood': 'RW', 't2-stoneheart-deeps': 'SD', 't1-stonewake-dale': 'ST',
            't3-ironroot-highlands': 'IR', 't3-thornwick-marches': 'TM', 't4-cinderfall-barrens': 'CF', 't4-riftlands': 'RL', 't4-veilmoor': 'VM',
            'quest-text-rl-riftlands': 'RL', 'quest-text-tm-thornwick-marches': 'TM', 'quest-text-vm-veilmoor': 'VM'}
DUNG = rd('docs/07-instances/dungeons.md')
DUNG_HEADS = [(m.start(), m.group(1)) for m in re.finditer(r'^## \d\. (.+?) \(', DUNG, re.M)]
SLOT_LONG = {'Chest': 'chest armor', 'Legs': 'leg armor', 'Feet': 'boots', 'Hands': 'gloves', 'Head': 'helm', 'Shoulders': 'shoulder armor', 'Waist': 'belt',
             'Wrist': 'bracers', 'Neck': 'necklace', 'Other': 'item', '1H axe': 'one-handed axe', '1H mace': 'one-handed mace', '1H sword': 'one-handed sword', '2H axe': 'two-handed axe', '2H mace': 'two-handed mace',
             '2H sword': 'two-handed sword', 'Off-hand': 'held off-hand item', 'Shield': 'shield'}
ITEM_COUNT = 0
for h1, h2, h3, c in table('docs/10-art/07-named-item-index.md'):
    if not c or not re.fullmatch(r'ITM-\d+', c[0]):
        continue
    ITEM_COUNT += 1
    iid, name, slot, desc, art = c[0], clean(c[2]), clean(c[3]), clean(c[4]), clean(c[5])
    src = h2.replace('Source: ', '')
    real = re.search(r'— ([A-Z][^,]+), ', desc)
    if real and re.match(r'\d+ ', desc):                        # index row named after the creature, not the item
        name, desc = real.group(1).strip(), desc.split(', ', 1)[1] if ', ' in desc else desc
    dropped = re.search(r'dropped by [^(]+\((\d+)', desc)
    am = re.match(r'(?:\*\*)?(cloth|leather|mail)(?:\*\*)? (chest|legs|feet|hands|wrist|waist|head|shoulders)', desc.lower())
    if am:
        slot = am.group(2).capitalize()
    elif desc.lower().startswith('back'):
        slot = 'Cloak'
    if slot in ('Chest', 'Legs', 'Feet', 'Hands', 'Wrist', 'Waist') and art.startswith('Unique model'):
        art = 'Unique body texture + icon'
    if slot in ('Head', 'Shoulders') and art.startswith('Unique model'):
        art = 'Unique 3D piece + texture + icon'
    if slot == 'Cloak' and art.startswith('Unique model'):
        art = 'Unique cloak texture + icon'
    if slot in ('Chest', 'Legs', 'Feet', 'Hands', 'Wrist', 'Waist', 'Head', 'Shoulders') and art.startswith('Tier model'):
        art = 'Tier body texture, recolor + icon'
    if re.match(r'(weapon oil|blacksmithing|leatherworking|tailoring|alchemy|enchanting|engineering|cooking)', desc.lower()) or 'crafting reserve' in desc:
        art, slot = 'Icon only', 'Other'
    m1, m2 = re.search(r'ilvl (\d+)', desc), re.search(r'\[(\d+)', desc)
    if src in ITEM_SRC:
        z = ITEM_SRC[src]
        lv = max(ZONES[z][1], int(m1.group(1)) - 5) if m1 else int(m2.group(1)) if m2 else int(dropped.group(1)) if dropped else ZONES[z][1] + 3
    elif src == 'dungeons':
        pos = DUNG.find(name.split(' / ')[0])
        head = [h for p, h in DUNG_HEADS if p < pos][-1] if pos > 0 and any(p < pos for p, h in DUNG_HEADS) else 'Gallowmere Crypts'
        z, lv = locate(head)
        lv = lv + 2
    elif src == 'raid-the-hollow-throne':
        z, lv = 'HT', 30
    elif src == 'world-bosses':
        z, lv = 'WB', 30
    elif src == 'pvp':
        z, lv = ('DP', 24) if 'Dustpit' in name or 'Pit' in name else ('CR', 30)
    else:
        z = 'ANY'
        lv = max(1, int(m1.group(1)) - 5) if m1 else int(m2.group(1)) if m2 else 27 if src == 'items-and-loot' else 20
    lv = min(30, lv)
    slong = SLOT_LONG.get(slot, slot.lower())
    where = {'crafting': 'crafted by a profession', 'dungeons': f'dungeon loot from {ZS[z]}', 'items-and-loot': 'world-drop epic', 'pvp': 'PvP reward',
             'raid-the-hollow-throne': 'raid loot', 'world-bosses': 'world-boss loot', 'reference-tables': 'reputation, fishing or other reward',
             'quest-text-cq-class-quests': 'class quest reward'}.get(src, f'quest reward or drop in {ZS[z]}')
    band = 'a' if lv < 10 else 'b' if lv < 20 else 'c'
    atype = next((t for t in ('cloth', 'leather', 'mail') if t in desc.lower()), None)
    used = f'Named item {iid}: {name} ({where})'
    binding = ''
    if art.startswith('Unique model'):
        add(f'{iid}-model', 'Weapon model', name, f'Unique {slong} "{name}": its own model and texture, shaped to suit its name and source ({where}). Stated as: {desc}. Oversized, readable silhouette. {zcue(z)}', used, z, lv, iid)
    elif art.startswith('Unique 3D piece'):
        for fit in ('Human fit', 'Dwarf fit'):
            add(f'{iid}-piece-{slug(fit)}', 'Armor piece', f'{name} ({fit})', f'Unique {slong} geometry and texture for "{name}" ({where}); {fit.lower()}. Stated as: {desc}. {zcue(z)}', used, z, lv, iid)
    elif art.startswith('Unique body texture'):
        add(f'{iid}-texture', 'Armor texture', name, f'Unique armor texture for the {slong} region, "{name}" ({where}), on the shared body layout. Stated as: {desc}. {zcue(z)}', used, z, lv, iid)
    elif art.startswith('Unique cloak'):
        add(f'{iid}-texture', 'Armor texture', name, f'Unique cloak texture "{name}" ({where}), shown on the cape shape built into each player body. Stated as: {desc}. {zcue(z)}', used, z, lv, iid)
    elif art.startswith('Tier model'):
        binding = f' Shown in the world with the generic model "{TIERWPN.get((slot.lower().replace("off-hand", "held off-hand"), band), "tier model for its type")}" in a recolour.'
    elif art.startswith('Tier body') or art.startswith('Tier 3D'):
        binding = f' Shown on the character with the generic set "{TIERSET.get((atype, band), "tier set for its type and level")}" in the colourway of its zone.'
    icon(f'{iid}-icon', name, f'the {slong} "{name}" ({where}). Stated as: {desc}.{binding}', used, z, lv, iid)

for h1, h2, h3, c in table('docs/10-art/08-quest-art-index.md'):
    if not c or c[0] not in QUEST:
        continue
    qid = c[0]
    qz, ql, qn, qo = QUEST[qid]
    implied = clean(c[4])
    obj = clean(c[3])
    if 'Item icon' in implied:
        m = re.search(r'(?:collect|recover|gather|bring|find|retrieve|loot|steal|deliver|carry|take|return)\s+(?:(?:the|a|an|\d+)\s+)?(.+?)(?:\s+(?:from|to|in|at|for)\b.*|[;,(].*)?$', obj, re.I)
        thing = m.group(1).strip(' .') if m else re.sub(r'^\[[A-Z0-9]+\] ', '', qn)
        icon(f'QST-{qid}-icon', f'{thing} ({qid})', f'the quest item for {qid} "{qn}". Objective: {obj}', f'Quest {qid}: {qn}', qz, ql, f'Quest {qid}')
    if 'World object' in implied:
        add(f'QST-{qid}-scene', 'Quest scene', f'Scene for {qid}: ' + re.sub(r'^\[[A-Z0-9]+\] ', '', qn), f'Staging for the quest objective "{obj}": place the zone set pieces, quest props and per-player object states this needs.', f'Quest {qid}: {qn}', qz, ql, f'Quest {qid}')

# ----------------------------------------------------------------------------- list 9: audio
L9 = 'docs/10-art/09-audio.md'
CULT_MUSIC = {'BM': 'human: strings, woodwind, lute', 'HF': 'human: strings, woodwind, lute', 'RW': 'human: strings, woodwind, lute', 'TM': 'human, darker: low strings, solo woodwind',
              'VM': 'human with the Hollow: strings, glass harmonica, distant choir', 'SOL': 'human court: strings, woodwind, lute', 'EC': 'mountain dwarf: low brass, male choir, anvils, stone reverb',
              'HAM': 'mountain dwarf: low brass, male choir, anvils, stone reverb', 'SD': 'mountain dwarf, underground: low brass, choir, long reverb',
              'IR': 'mountain dwarf with hill-dwarf fiddle', 'CF': 'mountain dwarf, harsh: brass, anvils, low drums', 'ST': 'hill dwarf: fiddle, pipes, hand drum',
              'RL': 'frontier with imperial hints: hand percussion, bowed metal', 'GC': 'the cult and the dead: low choir, bowed metal', 'SW': 'Slagborn: anvils, brass, machinery pulse',
              'HK': 'the Hollow: glass harmonica, bowed metal, distant choir', 'HT': 'imperial and the Hollow: glass harmonica, bowed metal, distant choir',
              'CR': 'martial: drums, brass, strings', 'SEA': 'both peoples: fiddle and low brass over a rolling rhythm', 'WB': 'full orchestra, heavy', 'ANY': 'orchestral-folk', 'CORE': 'orchestral-folk, full'}
for h1, h2, h3, c in table(L9):
    if not c or not re.fullmatch(r'MUS-\d+', c[0]):
        continue
    mid, text = c[0], clean(c[2])
    head, _, rest = text.partition(':')
    head = re.sub(r'\(.*?\)', '', head).strip()
    z, l = locate(text) or (('CORE', 0) if mid in ('MUS-01', 'MUS-02', 'MUS-28') else ('ANY', 1))
    if mid == 'MUS-22':
        z, l = 'WB', 30
    if mid == 'MUS-23':
        z, l = 'BM', 5
    if mid in ('MUS-25', 'MUS-27'):
        z, l = 'ANY', 1
    if mid == 'MUS-24':
        z, l = 'CR', 10
    tracks = expand(rest, [', ', '; ']) if rest else [head]
    if mid == 'MUS-25':
        tracks = split_top(rest, [', '])
    MUS_FIX = [('human', 'BM', 3), ('mountain dwarf', 'EC', 5), ('hill dwarf', 'ST', 3), ('shard answers', 'TM', 20), ('Three Envoys', 'RL', 24),
               ('goes under', 'RL', 27), ('shatters', 'HT', 30), ('Dustpit', 'DP', 24)]
    for t in tracks:
        tl = next(((zz, ll) for key, zz, ll in MUS_FIX if key in t and mid in ('MUS-16', 'MUS-26', 'MUS-24')), None) or locate(t)
        tz, tlv = (tl if tl and mid in ('MUS-09', 'MUS-10', 'MUS-11', 'MUS-12', 'MUS-13', 'MUS-16', 'MUS-24', 'MUS-26') else (z, l))
        sting = mid == 'MUS-25'
        add(f'{mid}-{slug(t)}', 'Music', f'{head}: {t}' if rest else head,
            f'{"Sting of 3 to 8 seconds" if sting else "Music track"} for {head}{": " + t if rest else ""}. Instruments by culture: {CULT_MUSIC.get(tz, "orchestral-folk")}. {"" if sting else "1.5 to 3 minutes, with a quiet ending so silences between tracks sit well."}',
            head, tz, tlv if not sting else 1, mid)

for h1, h2, h3, c in table(L9):
    if not c or not re.fullmatch(r'AMB-\d+', c[0]):
        continue
    aid, bed, spots = c[0], clean(c[2]), clean(c[3])
    z, l = locate(bed) or ('ANY', 1)
    if aid == 'AMB-12':
        z, l = 'BM', 1
    if aid == 'AMB-15':
        z, l = 'ST', 1
    if ':' in bed:
        beds, spots_l = split_top(bed.split(':', 1)[1], [', ']), []
        if aid == 'AMB-06':
            beds, spots_l = ['large-reverb cavern air'], expand(spots, [', '])
        if aid == 'AMB-18':
            beds = expand(bed.split(':', 1)[1], [', '], do_slash=True)
    elif aid in ('AMB-13', 'AMB-14'):
        beds, spots_l = [re.sub(r'\(.*?\)', '', x).strip() + ' (' + ', '.join(re.findall(r'\(([^)]*)\)', x)) + ')' for x in split_top(spots, [', '])], []
    else:
        stem = re.sub(r'\(.*?\)', '', bed).strip()
        beds = [stem.replace('day / night', t).strip() for t in ('day', 'night')] if 'day / night' in stem else [stem]
        spots_l = expand(spots, [', '], do_slash=False) if not re.fullmatch(r'\d+( beds)?', spots) else []
    head = re.sub(r'\s*(by \w+ )?×\d+', '', re.sub(r'\(.*?\)', '', bed.split(':')[0])).strip()
    for b in beds:
        bl = locate(b)
        bz, blv = (bl if bl else (z, l))
        add(f'{aid}-bed-{slug(b)}', 'Ambience', f'Ambience bed: {b}' if b != head else f'Ambience bed: {head}', f'Looping ambience bed, 60 to 120 seconds, seamless: {b}{" for " + head if head not in b and "day / night" not in head else ""}. No music, no speech. {zcue(bz)}', head, bz, blv, aid)
    for s in spots_l:
        add(f'{aid}-spot-{slug(s)}', 'Ambience', f'Ambience spot: {s} ({head})', f'One-shot ambience sound, 1 to 6 seconds, heard at a distance: {s}. {zcue(z)}', head, z, l, aid)

SURF = ['grass', 'dirt', 'stone', 'wood', 'snow', 'sand', 'mud', 'leaves', 'metal grate', 'shallow water']


def sfx(aid, name, desc, used, zone='ANY', level=1, source=''):
    add(aid, 'Sound effect', name, desc, used, zone, level, source)


for s in SURF:
    for gait in ('walk', 'run'):
        for v in (1, 2):
            sfx(f'SFX-P01-{slug(s)}-{gait}-{v}', f'Footstep: {s}, {gait}, variation {v}', f'Single footstep on {s} at a {gait}; short, dry, variation {v} of 2.', 'Player and humanoid footsteps', 'ANY', 1, 'SFX-P01')
P_LIST = {
    'SFX-P02': ['jump', 'land, light', 'land, heavy', 'fall damage thud', 'swim stroke A', 'swim stroke B', 'swim stroke C', 'dive under', 'surface', 'armor rustle, cloth', 'armor rustle, leather',
                'armor rustle, mail', 'sit down', 'stand up'],
    'SFX-P03': [f'weapon swing: {w}, variation {v}' for w in ('one-handed blade', 'two-handed blade', 'axe', 'mace', 'dagger', 'polearm', 'staff', 'unarmed') for v in (1, 2, 3)],
    'SFX-P04': [f'weapon impact: {w} on {mat}, variation {v}' for w in ('blade', 'blunt', 'pierce', 'unarmed') for mat in ('flesh', 'armor', 'wood or plant', 'stone or construct', 'bone') for v in (1, 2)],
    'SFX-P05': ['shield block A', 'shield block B', 'shield block C', 'parry A', 'parry B', 'parry C', 'dodge whoosh', 'miss', 'glancing blow', 'critical hit accent', 'crushing blow', 'block with weapon'],
    'SFX-P06': ['bow draw', 'bow release', 'crossbow shot', 'gun shot A', 'gun shot B', 'gun shot C', 'throw', 'arrow impact', 'bullet impact', 'thrown weapon impact', 'reload'],
    'SFX-P07': [f'{act}: {w}' for w in ('blade', 'blunt weapon', 'staff', 'shield') for act in ('draw', 'sheathe')],
    'SFX-P10': ['eat', 'drink', 'bandage', 'potion', 'loot coin', 'loot item', 'bag open', 'bag close', 'equip cloth', 'equip leather', 'equip mail', 'equip weapon', 'equip jewellery', 'repair', 'unequip', 'item break'],
    'SFX-P11': [f'horse hoof on {s}' for s in ('grass', 'dirt', 'stone', 'wood')] + ['horse whinny A', 'horse whinny B', 'horse snort'] + [f'ram hoof on {s}' for s in ('grass', 'dirt', 'stone', 'snow')]
               + ['ram bleat A', 'ram bleat B', 'ram snort', 'mount up', 'dismount'],
    'SFX-P12': ['death thud', 'ghost whoosh', 'resurrect', 'hearthstone channel', 'hearthstone arrive', 'level-up chime', 'rest area enter'],
}
for sid, names in P_LIST.items():
    for nm in names:
        sfx(f'{sid}-{slug(nm)}', nm[0].upper() + nm[1:], f'Player sound: {nm}. Short and dry, under 1.5 seconds, mono, with no reverb baked in; variations differ in pitch and attack.', 'Player and combat sounds', 'ANY', 30 if sid == 'SFX-P11' else 1, sid)
for b in BODIES:
    for e in ['attack grunt A', 'attack grunt B', 'attack grunt C', 'hit A', 'hit B', 'hit C', 'critical hit taken', 'death', 'jump', 'drown', 'laugh', 'cry', 'cheer', 'roar']:
        sfx(f'SFX-P08-{slug(b)}-{slug(e)}', f'{b} vocal effort: {e}', f'Wordless vocal effort for the {b.lower()} player voice: {e}.', 'Player voice', 'CORE' if e.startswith('attack') else 'ANY', 1, 'SFX-P08')
    for line in ['Not enough rage', 'Out of range', "I can't do that yet", 'Not enough mana', 'Target too close', 'Inventory is full', "I'm busy", 'No target']:
        add(f'SFX-P09-{slug(b)}-{slug(line)}', 'Voice line', f'{b} error line: "{line}"', f'"{line}." Spoken by the {b.lower()} player voice, flat and brief.', 'Player error feedback', 'ANY', 1, 'SFX-P09')
for s in SCHOOLS6:
    for st in ('cast loop', 'pre-cast', 'release'):
        sfx(f'SFX-S01-{slug(s)}-{slug(st)}', f'{s} {st}', f'Shared {st} sound for {s} spells. Character: {SCHOOL_LOOK[s].split(";")[1].strip()}.', 'Every cast-time spell', 'ANY', 1, 'SFX-S01')
    for sz in ('small', 'large'):
        sfx(f'SFX-S02-{slug(s)}-{sz}', f'{s} impact, {sz}', f'Shared {sz} impact sound for {s} spells.', 'All spell hits', 'ANY', 1, 'SFX-S02')
    for st in ('buff-up', 'debuff-apply', 'damage tick'):
        sfx(f'SFX-S03-{slug(s)}-{slug(st)}', f'{s} {st}', f'Shared {st} sound for {s} effects.', 'Buffs, debuffs and periodic damage', 'ANY', 1, 'SFX-S03')
for nm in ['dispel', 'heal tick']:
    sfx(f'SFX-S03-{slug(nm)}', nm.capitalize(), f'Shared {nm} sound.', 'Dispels and periodic healing', 'ANY', 1, 'SFX-S03')
for nm in ['stun', 'root', 'fear', 'sleep', 'silence', 'slow', 'interrupt', 'immune tink', 'absorb', 'enrage', 'knockback', 'taunt']:
    sfx(f'SFX-S04-{slug(nm)}', f'State sound: {nm}', f'Sound when a unit is affected by {nm}.', 'Crowd control and status', 'ANY', 1, 'SFX-S04')
SND_PART = {'Cast': 'cast or pre-cast', 'Proj': 'release and travel', 'Hit': 'impact', 'Aura': 'aura loop or onset', 'Area': 'area loop', 'Weapon': 'swing accent'}
for vid, parts in VFX_PARTS.items():
    cls = CLASS_OF[vid[4]]
    srow = {'F': 'SFX-S05', 'C': 'SFX-S06', 'D': 'SFX-S07'}[vid[4]]
    for aname, label, lv in parts[:3]:
        sfx(f'{srow}-{vid[4:]}-{slug(label)}', f'{aname}: {SND_PART[label]}', f'Sound for the {cls} ability {aname}, {SND_PART[label]}; matches effect {vid}.', f'{cls} ability {aname}', 'ANY', lv, srow)
for nm in ['potion', 'elixir', 'scroll', 'enchant apply'] + [f'weapon proc: {s}' for s in ('Fire', 'Shadow', 'Nature', 'life-steal')] + [f'trinket use: {s}' for s in SCHOOLS7] \
        + [f'dynamite fuse and blast, {s}' for s in ('small', 'medium', 'large', 'huge')] + ['bomb', 'gadget: target dummy', 'gadget: clockwork ram', 'gadget: mechanical squirrel',
                                                                                             'gadget: resuscitator', 'gadget: parachute', 'mining strike A', 'mining strike B', 'mining strike C',
                                                                                             'herb pick', 'skinning', 'fishing cast', 'fishing bobber', 'fishing splash', 'fishing reel',
                                                                                             'anvil strike A', 'anvil strike B', 'anvil strike C', 'forge', 'alchemy bubbling', 'enchanting hum',
                                                                                             'disenchant', 'sewing', 'cooking sizzle']:
    sfx(f'SFX-S08-{slug(nm)}', nm.capitalize(), f'Item or profession sound: {nm}.', 'Items and professions', 'ANY', 5, 'SFX-S08')
CRE_SND = ['idle or breath A', 'idle or breath B', 'aggro', 'attack A', 'attack B', 'attack C', 'wound A', 'wound B', 'death', 'special']
SND_ROW = {'B': 'SFX-C01', 'H': 'SFX-C02', 'U': 'SFX-C03', 'E': 'SFX-C04', 'C': 'SFX-C04', 'P': 'SFX-C04'}
for rid, rig, rz, rl in RIG_NAMES:
    if rid == 'CRE-H07':
        continue
    for s in CRE_SND:
        sfx(f'{SND_ROW[rid[4]]}-{rid[4:]}-{slug(s)}', f'{rig}: {s}', f'Creature sound for the {rig.lower()} rig: {s}. Shared by all its skins, pitched by size.' + (' A gibberish voice, no real words.' if rid[4] == 'H' else ''),
            f'All {rig.lower()} creatures', rz, rl, SND_ROW[rid[4]])
for cid, (z, l) in CRIT_Z.items():
    if cid in ('CRT-11', 'CRT-12'):
        continue
    nm = next(clean(c[2]) for h1, h2, h3, c in table(L2) if c and c[0] == cid)
    for s in ('call', 'death'):
        sfx(f'SFX-C05-{cid[4:]}-{s}', f'Critter {nm}: {s}', f'Small {s} sound of the {nm.lower()} critter.', 'Ambient life', z, l, 'SFX-C05')
for vid, e, lv in MLIB:
    sfx(f'SFX-C06-{vid[4:]}-{slug(e)}', f'Creature ability: {e}', f'Sound for the creature ability effect "{e}" ({vid}).', 'Creature abilities', 'ANY', lv, 'SFX-C06')
for race, z in (('human', 'BM'), ('dwarf', 'ST')):
    for v in ('male A', 'male B', 'male C', 'female A', 'female B'):
        for s in ['aggro A', 'aggro B', 'aggro C', 'attack A', 'attack B', 'attack C', 'wound A', 'wound B', 'death', 'flee']:
            sfx(f'SFX-C07-{race}-{slug(v)}-{slug(s)}', f'Enemy {race} voice {v}: {s}', f'Wordless combat vocalisation for {race} enemies, voice {v}: {s}.', f'{race.capitalize()} enemy humanoids', z, 3, 'SFX-C07')
BROW = {'VFX-B01': 'SFX-B01', 'VFX-B02': 'SFX-B01', 'VFX-B10': 'SFX-B01', 'VFX-B03': 'SFX-B02', 'VFX-B04': 'SFX-B03', 'VFX-B05': 'SFX-B04', 'VFX-B06': 'SFX-B05',
        'VFX-B07': 'SFX-B06', 'VFX-B08': 'SFX-B06', 'VFX-B09': 'SFX-B06'}
for vid, e, z, l, enc in BOSSFX:
    sfx(f'{BROW[vid]}-{vid[4:]}-{slug(e)}', f'{enc}: {e}', f'Mechanic sound for the encounter effect "{e}"; a clear warning cue where the effect must be avoided.', f'Encounter: {enc}', z, l, BROW[vid])
for nm, z, l, row in [("The Stitched Choir's six-voice out-of-tune hymn, layered loop", 'GC', 15, 'SFX-B02'), ('Molten Maw roar A', 'SW', 22, 'SFX-B03'), ('Molten Maw roar B', 'SW', 22, 'SFX-B03'),
                      ('Slagworks machinery loop', 'SW', 20, 'SFX-B03'), ('Slag flood rising', 'SW', 23, 'SFX-B03'), ('Polite applause loop', 'HK', 29, 'SFX-B04'),
                      ('Banquet toast', 'HK', 29, 'SFX-B04'), ('Ink pooling', 'HK', 30, 'SFX-B04')] \
        + [(f'Ward Strain crack {i}', 'HT', 30, 'SFX-B05') for i in (1, 2, 3, 4)] + [('Ward collapse', 'HT', 30, 'SFX-B05')] \
        + [(f'{b}: {s}', 'WB', 30, 'SFX-B06') for b in ('Grimroot', 'Pyrraxis', 'Gorrath') for s in ('spawn omen', 'roar A', 'roar B', 'roar C', 'death')]:
    sfx(f'{row}-x-{slug(nm)}', nm, f'Encounter sound: {nm}.', 'Boss encounters', z, l, row)

SPK = rd('docs/12-data/spoken-lines.md')
sec = lambda a, b: SPK[SPK.index(a):SPK.index(b)]
VOICE_L = [(r'Human', 'BM', 1), (r'Mountain dwarf', 'EC', 5), (r'Hill dwarf', 'ST', 1), (r'Human guard', 'BM', 1), (r'Dwarf guard', 'ST', 1), (r'Elf', 'TM', 14), (r'Ogre', 'IR', 12), (r'Covenant', 'RL', 22)]
for line in sec('## 2. NPC barks', '## 3. Story lines').splitlines():
    if not line.startswith('|') or '"' not in line:
        continue
    cells = [x.strip() for x in line.strip('|').split('|')]
    voice = clean(cells[0])
    z, l = next(((z, l) for rx, z, l in VOICE_L[::-1] if re.search(rx, voice)), ('ANY', 1))
    kinds = ['greeting', 'farewell', 'annoyed', 'vendor'] if len(cells) == 5 else ['greeting', 'warning', 'attack call'] if len(cells) == 4 else ['line']
    for k, cell in zip(kinds, cells[1:]):
        for i, q in enumerate(re.findall(r'"([^"]+)"', cell)):
            add(f'VOX-bark-{slug(voice)}-{slug(k)}-{i + 1}', 'Voice line', f'{voice}, {k} {i + 1}', f'"{q}" Bark for the voice set "{voice}", said plainly in 1 to 4 words.', f'NPCs with the {voice} voice', z, l, 'Spoken Lines §2')
STORY_L = {1: ('BM', 5), 2: ('TM', 20), 3: ('TM', 20), 4: ('SOL', 15), 5: ('HAM', 15), 6: ('TM', 18), 7: ('IR', 18), 8: ('CF', 23), 9: ('CF', 23), 10: ('RL', 24), 11: ('RL', 24),
           12: ('RL', 24), 13: ('RL', 24), 14: ('RL', 25), 15: ('RL', 26), 16: ('VM', 28), 17: ('HK', 30), 18: ('RL', 30), 19: ('HT', 30), 20: ('HT', 30)}
for line in sec('## 3. Story lines', '## 4. Announcers').splitlines():
    m = re.match(r'\| (vo\.story\.(\d+)) \| ([^|]+) \| ([^|]+) \| "(.+)" \|', line)
    if m:
        z, l = STORY_L[int(m.group(2))]
        add(m.group(1), 'Voice line', f'{clean(m.group(3))}: {clean(m.group(4))}', f'"{m.group(5)}" Spoken by {clean(m.group(3))} at the moment "{clean(m.group(4))}"; voiced once, subtitled.', 'Story moment', z, l, 'Spoken Lines §3')
for line in sec('## 4. Announcers', '## 5. Boss lines').splitlines():
    if not line.startswith('| vo.'):
        continue
    cells = [x.strip() for x in line.strip('|').split('|')]
    z, l = ('CR', 10) if 'bg' in cells[0] else ('DP', 24) if 'pit' in cells[0] else ('WB', 30)
    for i, q in enumerate(re.findall(r'"([^"]+)"', cells[3])):
        add(f'{cells[0].split("–")[0]}-{i + 1}', 'Voice line', f'Announcer: {clean(cells[2])} {i + 1 if i else ""}'.strip(), f'"{q}" Announcer line for the event "{clean(cells[2])}".', 'Announcers', z, l, 'Spoken Lines §4')
boss, bz = '', ('GC', 15)
for line in sec('## 5. Boss lines', '## 6. The Athenaeum books').splitlines():
    if line.startswith('### '):
        bz = locate(line) or ('WB', 30)
        continue
    if not line.startswith('|') or '---' in line or line.startswith('| Boss'):
        continue
    cells = [x.strip() for x in line.strip('|').split('|')]
    if cells[0]:
        boss = clean(cells[0])
    cz = creature(boss) or bz
    for i, q in enumerate(re.findall(r'"([^"]+)"', cells[2])):
        add(f'VOX-boss-{slug(boss)}-{slug(cells[1])}-{i + 1}', 'Voice line', f'{boss}: {clean(cells[1])}', f'"{q}" Spoken by {boss} at the moment "{clean(cells[1])}"; heard by everyone in the room.', f'Boss: {boss}', cz[0], cz[1], 'Spoken Lines §5')

UIA_L = {'UIA-07': 3, 'UIA-08': 2}
for h1, h2, h3, c in table(L9):
    if not c or not re.fullmatch(r'UIA-\d+', c[0]):
        continue
    uid, text = c[0], clean(c[2])
    head, _, rest = text.partition(':')
    els = []
    for e in expand(rest, [', ', '; ']):
        if uid == 'UIA-02':
            base = re.sub(r'\(.*?\)', '', e).strip()
            els += [f'{base} window open', f'{base} window close']
        elif uid == 'UIA-04' and 'by material' in e:
            els += [f'{act} item: {m}' for m in ('cloth', 'leather', 'metal', 'wood', 'gem', 'paper', 'food', 'liquid', 'herb', 'ore') for act in ('pick up', 'drop')]
        else:
            els += slash(e) if uid in ('UIA-05',) else [e]
    for e in els:
        lv = UIA_L.get(uid, 0 if uid in ('UIA-01', 'UIA-10') else 1)
        add(f'{uid}-{slug(e)}', 'Sound effect', f'Interface: {e}', f'Short interface sound, under 1 second, stereo: {e}.', head.strip(), 'CORE' if lv == 0 else 'ANY', lv, uid)

# ----------------------------------------------------------------------------- order and write
for a in ASSETS:
    if a['zone'] not in ZONES:
        a['zone'] = 'ANY'
    a['level'] = max(0, min(30, a['level']))
    if a['zone'] == 'CORE' and a['level'] > 0:
        a['zone'] = 'ANY'
ASSETS.sort(key=lambda a: (a['level'], KIND[a['kind']][0], ZONES[a['zone']][2], a['seq']))
for i, a in enumerate(ASSETS):
    a['order'] = i + 1

os.makedirs(OUT, exist_ok=True)
for f in os.listdir(OUT):
    if f.endswith('.md') or f.endswith('.csv'):
        os.remove(os.path.join(OUT, f))
BANDS = [(0, 0, 'Before the world: login, character creation and the core kit'), (1, 2, 'Levels 1 to 2'), (3, 5, 'Levels 3 to 5'), (6, 9, 'Levels 6 to 9'),
         (10, 14, 'Levels 10 to 14'), (15, 19, 'Levels 15 to 19'), (20, 24, 'Levels 20 to 24'), (25, 29, 'Levels 25 to 29'), (30, 30, 'Level 30: raid, world bosses, mounts')]
CAP = 1000
files, n = [], 1
for lo, hi, title in BANDS:
    rows = [a for a in ASSETS if lo <= a['level'] <= hi]
    chunks = [rows[i:i + CAP] for i in range(0, len(rows), CAP)] or [[]]
    for k, chunk in enumerate(chunks):
        if not chunk:
            continue
        fname = f'{n:02d}-{slug(title.split(":")[0])}{"-part-" + str(k + 1) if len(chunks) > 1 else ""}.md'
        files.append((fname, title + (f', part {k + 1} of {len(chunks)}' if len(chunks) > 1 else ''), chunk))
        n += 1


def esc(s):
    return s.replace('|', '/').replace('\n', ' ')


for i, (fname, title, chunk) in enumerate(files):
    prev = f'[← {files[i - 1][1]}]({files[i - 1][0]})' if i else '[← Manifest index](00-manifest-index.md)'
    nxt = f' · Next: [{files[i + 1][1]}]({files[i + 1][0]})' if i + 1 < len(files) else ''
    out = [f'# Asset Manifest — {title}', '', f'{prev} · [Index and rules](00-manifest-index.md){nxt}', '',
           f'Assets {chunk[0]["order"]} to {chunk[-1]["order"]} of {len(ASSETS)}, in order of first appearance. Generated by `tools/doc-generators/asset_manifest.py`; do not edit by hand. Columns are explained in the [index](00-manifest-index.md#2-columns).', '',
           '| # | Asset id | Kind | Pipeline | Name | Description to generate from | Used for | Zone | Level | Source |', '|---|---|---|---|---|---|---|---|---|---|']
    for a in chunk:
        out.append(f'| {a["order"]} | `{a["id"]}` | {a["kind"]} | {a["pipe"]} | {esc(a["name"])} | {esc(a["desc"])} | {esc(a["used"])} | {ZONES[a["zone"]][0]} | {a["level"]} | {a["source"]} |')
    with open(os.path.join(OUT, fname), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')

with open(os.path.join(OUT, 'asset-manifest.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['order', 'id', 'kind', 'pipeline', 'name', 'description', 'used_for', 'zone', 'first_seen_level', 'technical_target', 'source'])
    for a in ASSETS:
        w.writerow([a['order'], a['id'], a['kind'], a['pipe'], a['name'], a['desc'], a['used'], ZONES[a['zone']][0], a['level'], KIND[a['kind']][2], a['source']])

bykind, bypipe = defaultdict(int), defaultdict(int)
for a in ASSETS:
    bykind[a['kind']] += 1
    bypipe[a['pipe']] += 1
gen = sum(v for k, v in bypipe.items() if k.startswith('P'))
idx = ['# Asset Manifest — every asset, in order of first appearance', '',
       '[← Master Plan](../../MASTER_PLAN.md) · Made by: [Asset Forge](../14-asset-pipeline/00-asset-forge.md) · Look: [Art Direction](../10-art/10-art-direction.md) · Source lists: [Art Master To-Do](../10-art/00-art-master-todo.md)', '',
       f'One row for every asset the game needs: **{len(ASSETS):,} rows, of which {gen:,} are generated by the forge** and {len(ASSETS) - gen:,} are assembled or derived from them. '
       'Each row says what the asset is, gives a description to generate it from, what it is for, the zone it belongs to and the level at which a player first meets it. '
       '**The rows are in order of first appearance, and that is the order the forge generates them in**, so the placeholders a new player sees first are replaced first.', '',
       'This manifest is generated from the art lists and the design data by `tools/doc-generators/asset_manifest.py`. Regenerate it after any change to those documents; do not edit it by hand. '
       'The same rows are in [`asset-manifest.csv`](asset-manifest.csv) for programs to read.', '',
       '## 1. The order', '',
       '| Rule | Detail |', '|---|---|',
       '| First key | **First-seen level**: the lowest character level at which a player normally meets the asset. Level 0 is everything seen before entering the world (login, character creation) and the core kit every character needs at once |',
       '| Second key | Kind, world first: interface, paintings, ground, sky, buildings, nature, props, then rigs, models, hair, skins, animation, then armor and weapons, effects, icons, and last music, ambience, sound and voice. So at every level the textures and models a player looks at come before the sounds |',
       '| Third key | Zone, in the order of the journey: any-zone assets, Brightmead Vale, Stonewake Dale, Solhaven, Hammerdeep, the ship, Harrowfield, Russetwood, Embercrag Hollow, Stoneheart Deeps, Thornwick Marches, Ironroot Highlands, Crownfall, Gallowmere Crypts, Cinderfall Barrens, the Riftlands, Veilmoor, the Slagworks, the Dustpit, Hollowspire Keep, the Hollow Throne, world bosses |',
       '| Where the level comes from | Creatures: their level in the creature and encounter data. Items: required level, from the item level or the bracketed level. Abilities and talents: the level learned. Zone ground, sky, music and kits: the level at which the zone opens. Set pieces: the level of their place in the zone. Profession items: recipe skill divided by 7.5 |',
       '| Shared assets | An asset used in several places takes the earliest. A rig, its base model and its animation take the level of the lowest-level creature that uses it |',
       '| What the forge does with it | Each asset machine takes the next row in this order that one of its pipelines can make. Images and audio on one machine and 3D on another therefore advance side by side, each in order of first appearance |', '',
       '## 2. Columns', '',
       '| Column | Meaning |', '|---|---|',
       '| # | Position in the order |',
       '| Asset id | The stable id: the one in the asset status file and the one the game loads by. It begins with the id of the art-list row it was expanded from |',
       '| Kind | What sort of asset it is (table below) |',
       '| Pipeline | The forge pipeline that makes it (P01 to P21). `assemble` and `derive` rows need no generation: they are put together or cut from generated assets by the world generator |',
       '| Name | Short name |',
       '| Description to generate from | The subject text for the generator. The pipeline adds the style bible\'s fragment, reference images and technical settings; the description does not repeat them |',
       '| Used for | What in the game uses it |',
       '| Zone | Where it first appears. "Any zone" means it follows the character, not a place |',
       '| Level | First-seen level |',
       '| Source | The art-list row or data document the row was expanded from |', '',
       '## 3. Kinds, pipelines and technical targets', '',
       '| Kind | Rows | Pipeline | Technical target |', '|---|---|---|---|']
for k, (o, p, spec) in KIND.items():
    if bykind[k]:
        idx.append(f'| {k} | {bykind[k]:,} | {p} | {spec} |')
idx += ['', '## 4. The files', '', '| File | Covers | Rows | Positions |', '|---|---|---|---|']
for fname, title, chunk in files:
    idx.append(f'| [{fname}]({fname}) | {title} | {len(chunk):,} | {chunk[0]["order"]:,} to {chunk[-1]["order"]:,} |')
zcount = defaultdict(int)
for a in ASSETS:
    zcount[a['zone']] += 1
idx += ['', '## 5. Rows by zone', '', '| Zone | Opens at level | Rows |', '|---|---|---|']
for z, v in ZONES.items():
    if zcount[z]:
        idx.append(f'| {v[0]} | {v[1]} | {zcount[z]:,} |')
idx += ['', '## 6. Rows by pipeline', '', '| Pipeline | Rows |', '|---|---|']
for p in sorted(bypipe, key=lambda x: (not x.startswith('P'), x)):
    idx.append(f'| {p} | {bypipe[p]:,} |')
idx += ['', '## 7. What is not a row', '',
        '| Thing | Why |', '|---|---|',
        '| Placeholders | Every row has one, made from its contract ([Placeholders and Swapping](../14-asset-pipeline/04-placeholders-and-swap.md)) |',
        '| Named items that use tier art | They get an icon row only. Their description names the generic model or set and colourway they are shown with |',
        '| Starting outfits, guild tabard colours, macro and guild-bank tab icons | Built from, or reusing, assets already listed |',
        '| Minimap tiles, navigation meshes | Rendered or baked from the built zones |',
        '| Voiced lines for zone elites and act bosses | Not voiced. The voice lines are exactly those in [Spoken Lines](../12-data/spoken-lines.md) |',
        '| Levels 31 to 60, epic mounts, future races and classes | Out of scope for version 1.0 |', '',
        '## 8. Limits', '',
        '- Descriptions are composed by rule from what the art lists, data and layout documents say: the subject, its notes, its culture and its zone palette. They do not add invented detail. A named item\'s description is its name, type, stated numbers and where it comes from; the generator must take the look from the name.',
        '- Where a list gives a count without names (kit pieces beyond the named ones, hair styles, guild emblems, generic props, vendor-trash icons), the names here were written for this manifest and are now the specification.',
        '- First-seen levels inside a zone are approximate for set pieces and for creatures the data does not list by name; they take their place\'s level or the lowest level of their rig.',
        f'- The counts here replace the estimates in the art lists. The art lists said about 9,100; expanding every grouped row gives {len(ASSETS):,}.']
with open(os.path.join(OUT, '00-manifest-index.md'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(idx) + '\n')

print(f'assets {len(ASSETS)}; generated {gen}; named items read {ITEM_COUNT}; files {len(files)}')
for k in KIND:
    if bykind[k]:
        print(f'  {bykind[k]:5d}  {k}')
