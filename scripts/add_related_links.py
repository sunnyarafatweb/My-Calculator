# -*- coding: utf-8 -*-
"""Give the dead-end template pages a quiet Related-calculators block.

Why: 51 template-tier pages carry zero links out of <main>. They receive link
equity from the sitewide footer and pass none of it on, and they give Google no
topical signal about what they sit next to. This adds six links each, chosen for
genuine relevance and weighted toward pages that are currently under-linked, so
equity spreads instead of pooling on the six calculators the footer already
links from all 220 pages.

Styled to match the existing FAQ section on those pages: same heading classes,
muted link colour, one flowing line. No new card, no colour block.
"""
import re, io, glob, json, collections, os

REPO = "/home/claude/repo"
HUBS = {'all-calculators', 'about', 'privacy-policy', 'terms', 'contact',
        'sitemap', '404', '_not-found'}
PER_PAGE = 6

STOP = {'calculator', 'converter', 'generator', 'counter', 'roller', 'the', 'a',
        'of', 'and', 'to', 'your', 'free', 'online'}

# Hand-drawn topical clusters. Word overlap alone pairs "exponent" with "dice
# roller" because both are filed under Math, which is true and useless. These
# are the groupings a person would actually make, and they outrank everything
# else in the scoring below.
CLUSTERS = [
    # numbers and notation
    ['exponent-calculator', 'root-calculator', 'log-calculator',
     'scientific-notation-calculator', 'big-number-calculator',
     'rounding-calculator', 'significant-figures-calculator'],
    # bases and encoding
    ['binary-calculator', 'hex-calculator', 'base64-encode-decode',
     'url-encode-decode', 'ip-subnet-calculator', 'bandwidth-calculator',
     'password-generator'],
    # factors and fractions
    ['gcf-calculator', 'lcm-calculator', 'factor-calculator',
     'fraction-calculator', 'ratio-calculator', 'percentage-calculator',
     'long-division-calculator', 'prime-factorization-calculator'],
    # statistics and probability
    ['statistics-calculator', 'standard-deviation-calculator',
     'mean-median-mode-range-calculator', 'confidence-interval-calculator',
     'z-score-calculator', 'sample-size-calculator', 'probability-calculator',
     'permutation-and-combination-calculator', 'random-number-generator',
     'dice-roller', 'average-calculator'],
    # geometry and shapes
    ['area-calculator', 'volume-calculator', 'surface-area-calculator',
     'triangle-calculator', 'right-triangle-calculator',
     'pythagorean-theorem-calculator', 'circle-calculator',
     'distance-calculator', 'slope-calculator', 'square-footage-calculator'],
    # algebra
    ['matrix-calculator', 'quadratic-formula-calculator', 'slope-calculator',
     'number-sequence-calculator', 'factor-calculator'],
    # building and materials
    ['concrete-calculator', 'gravel-calculator', 'mulch-calculator',
     'square-footage-calculator', 'roofing-calculator', 'tile-calculator',
     'stair-calculator', 'btu-calculator'],
    # vehicles and travel
    ['gas-mileage-calculator', 'fuel-cost-calculator', 'mileage-calculator',
     'speed-calculator', 'distance-calculator', 'horsepower-calculator',
     'engine-horsepower-calculator', 'tire-size-calculator'],
    # time and dates
    ['date-calculator', 'day-counter', 'day-of-the-week-calculator',
     'time-calculator', 'time-duration-calculator', 'time-card-calculator',
     'time-zone-calculator', 'age-calculator', 'hours-calculator'],
    # physical sciences
    ['density-calculator', 'mass-calculator', 'molarity-calculator',
     'molecular-weight-calculator', 'half-life-calculator',
     'dew-point-calculator', 'heat-index-calculator', 'btu-calculator'],
    # everyday / fun
    ['love-calculator', 'dice-roller', 'random-number-generator',
     'age-calculator', 'golf-handicap-calculator'],
]
CLUSTER_OF = {}
for _i, _c in enumerate(CLUSTERS):
    for _s in _c:
        CLUSTER_OF.setdefault(_s, set()).add(_i)


def words(slug):
    return {w for w in slug.split('-') if w not in STOP and len(w) > 2}


def load():
    info = {}
    for f in sorted(glob.glob(os.path.join(REPO, '*/index.html'))):
        slug = os.path.basename(os.path.dirname(f))
        h = io.open(f, encoding='utf-8', errors='replace').read()
        m = re.search(r'<main.*?</main>', h, re.S)
        if not m:
            continue
        body = m.group(0)
        cat = re.search(r'all-calculators/#(fin|hea|mat|oth|cry)', body)
        t = re.search(r'<h1[^>]*>(.*?)</h1>', body, re.S)
        title = re.sub(r'<[^>]+>', '', t.group(1)).strip() if t else slug
        outs = set(x.strip('/') for x in
                   re.findall(r'href="/([a-z0-9][a-z0-9\-]*)/"', body)) - {slug}
        info[slug] = {'cat': cat.group(1) if cat else None, 'title': title,
                      'outs': outs, 'prose': 'prose-content' in body, 'file': f,
                      'words': words(slug)}
    return info


def main():
    info = load()
    # current inbound count from page bodies, so under-linked pages can be favoured
    inbound = collections.Counter()
    for s, v in info.items():
        for t in v['outs']:
            if t in info:
                inbound[t] += 1

    targets = [s for s, v in info.items()
               if s not in HUBS and v['prose'] and len(v['outs']) == 0]
    candidates = [s for s in info if s not in HUBS]

    plan = {}
    for s in targets:
        me = info[s]
        scored = []
        for c in candidates:
            if c == s:
                continue
            o = info[c]
            score = 0.0
            # topical cluster is the dominant signal
            shared_cluster = CLUSTER_OF.get(s, set()) & CLUSTER_OF.get(c, set())
            if shared_cluster:
                score += 60
            shared = me['words'] & o['words']
            score += 14 * len(shared)
            if o['cat'] and o['cat'] == me['cat']:
                score += 8
            # spread equity: a tiebreaker among relevant pages, never a driver
            score += max(0, 6 - inbound[c]) * 0.8
            if inbound[c] > 20:
                score -= 4
            if score >= 8:
                scored.append((score, c))
        scored.sort(key=lambda x: (-x[0], x[1]))
        picked = [c for _, c in scored[:PER_PAGE]]
        plan[s] = picked
        for c in picked:          # keep the spread honest as we go
            inbound[c] += 1

    block_css = (
        '<style>.rel-links{margin-top:14px;font-size:14px;line-height:2;color:var(--ink-faint)}'
        '.rel-links a{color:var(--ink-soft);text-decoration:none;border-bottom:1px solid var(--border);'
        'padding-bottom:1px;transition:.2s}'
        '.rel-links a:hover{color:#128A3D;border-color:#128A3D}'
        '.rel-links .sep{color:var(--ink-faint);margin:0 7px}</style>'
    )

    changed = 0
    for s, picks in plan.items():
        f = info[s]['file']
        h = io.open(f, encoding='utf-8', errors='replace').read()
        if 'rel-links' in h:
            continue
        links = ('<span class="sep">&middot;</span>'.join(
            '<a href="/%s/">%s</a>' % (c, info[c]['title']) for c in picks))
        section = (
            '<section><h2 class="font-display text-xl text-ink mb-5">Related calculators</h2>'
            + block_css +
            '<p class="rel-links">' + links +
            '<span class="sep">&middot;</span><a href="/all-calculators/">All calculators</a></p>'
            '</section>')
        # append as the last section inside the existing prose article
        i = h.rfind('</article>')
        assert i > 0, s
        h = h[:i] + section + h[i:]
        io.open(f, 'w', encoding='utf-8').write(h)
        changed += 1

    print('pages given a related block:', changed)
    spread = collections.Counter()
    for picks in plan.values():
        for c in picks:
            spread[c] += 1
    print('distinct pages now receiving new links:', len(spread))
    print('most-added targets:', spread.most_common(8))
    print('new links added in total:', sum(spread.values()))


if __name__ == '__main__':
    main()
