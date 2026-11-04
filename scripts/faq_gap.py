# -*- coding: utf-8 -*-
"""Which live calculator pages never answer 'how do you calculate this?'

Assistants and featured snippets lift a short answer to the question as the
user phrased it. A page can explain the formula in prose for 1,500 words and
still lose, because nothing on it is shaped like the question.
"""
import os, re, io, json

REPO = "/home/claude/repo"
hdr = io.open(os.path.join(REPO, '_headers'), encoding='utf-8').read()
hidden, cur = set(), None
for line in hdr.splitlines():
    s = line.strip()
    if not s or s.startswith('#'):
        continue
    if not line[0].isspace():
        cur = s.strip('/').split('/')[0]
    elif cur and re.search(r'(?i)X-Robots-Tag:.*\bnoindex\b', s):
        hidden.add(cur)

SKIP = {'og', 'scripts', 'node_modules', '_next', '404', '_not-found',
        'about', 'contact', 'privacy-policy', 'terms', 'sitemap',
        'all-calculators'}

HOWTO = re.compile(r'(?i)\bhow (do|is|are|to|can|would) .*(calculat|work out|figure|determin|comput)')
FORMULA = re.compile(r'(?i)\bwhat (is|\'s) the .*(formula|equation)\b')

missing, have, nofaq = [], [], []

for d in sorted(os.listdir(REPO)):
    p = os.path.join(REPO, d)
    if not os.path.isdir(p) or d.startswith('.') or d in SKIP or d in hidden:
        continue
    f = os.path.join(p, 'index.html')
    if not os.path.isfile(f):
        continue
    h = io.open(f, encoding='utf-8', errors='replace').read()
    qs = []
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try:
            o = json.loads(b)
        except Exception:
            continue
        if isinstance(o, dict) and o.get('@type') == 'FAQPage':
            qs = [q.get('name', '') for q in o.get('mainEntity', [])]
    if not qs:
        nofaq.append(d)
        continue
    if any(HOWTO.search(q) or FORMULA.search(q) for q in qs):
        have.append(d)
    else:
        missing.append((d, len(qs)))

print('pages with a how-to-calculate or formula FAQ : %d' % len(have))
print('pages with FAQs but no such question         : %d' % len(missing))
print('pages with no FAQ block at all               : %d' % len(nofaq))
print()
if nofaq:
    print('NO FAQ AT ALL:')
    for d in nofaq:
        print('   ', d)
    print()
print('HAVE FAQs BUT NEVER ANSWER "HOW IS IT CALCULATED":')
for d, n in missing:
    print('   %-38s (%d FAQs)' % (d, n))
