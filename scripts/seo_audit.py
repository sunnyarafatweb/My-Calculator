# -*- coding: utf-8 -*-
"""On-page SEO sweep across the live (non-hidden) pages."""
import os, re, io, json, collections

REPO = "/home/claude/repo"
hdr = io.open(os.path.join(REPO, '_headers'), encoding='utf-8').read()
hidden = set()
cur = None
for line in hdr.splitlines():
    s = line.strip()
    if not s or s.startswith('#'):
        continue
    if not line[0].isspace():
        cur = s.strip('/').split('/')[0]
    elif cur and re.match(r'(?i)X-Robots-Tag:.*\bnoindex\b', s):
        hidden.add(cur)

SKIP = {'og', 'scripts', 'node_modules', '_next', '404', '_not-found'}
issues = collections.defaultdict(list)
pages = 0

def check(slug, path):
    global pages
    h = io.open(path, encoding='utf-8', errors='replace').read()
    pages += 1
    name = slug or '(home)'

    m = re.search(r'<title>(.*?)</title>', h, re.S)
    t = m.group(1).strip() if m else ''
    if not t:
        issues['no title'].append(name)
    elif len(t) > 60:
        issues['title over 60 chars'].append('%s (%d)' % (name, len(t)))
    elif len(t) < 25:
        issues['title under 25 chars'].append('%s (%d)' % (name, len(t)))

    m = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
    d = m.group(1).strip() if m else ''
    if not d:
        issues['no meta description'].append(name)
    elif len(d) > 160:
        issues['meta description over 160'].append('%s (%d)' % (name, len(d)))
    elif len(d) < 70:
        issues['meta description under 70'].append('%s (%d)' % (name, len(d)))

    n = len(re.findall(r'<h1[\s>]', h))
    if n != 1:
        issues['h1 count not 1'].append('%s (%d)' % (name, n))

    if 'rel="canonical"' not in h:
        issues['no canonical'].append(name)
    else:
        c = re.search(r'<link rel="canonical" href="([^"]+)"', h)
        want = 'https://calculatorboss.com/' + (slug + '/' if slug else '')
        if c and c.group(1) != want:
            issues['canonical mismatch'].append('%s -> %s' % (name, c.group(1)))

    if 'og:title' not in h:
        issues['no og:title'].append(name)
    if 'og:image' not in h:
        issues['no og:image'].append(name)
    else:
        oi = re.search(r'og:image" content="([^"]+)"', h)
        if oi:
            f = oi.group(1).replace('https://calculatorboss.com/', '')
            if not os.path.exists(os.path.join(REPO, f)):
                issues['og:image file missing'].append('%s -> %s' % (name, f))
    if 'twitter:card' not in h:
        issues['no twitter:card'].append(name)

    types = set()
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try:
            o = json.loads(b)
        except Exception:
            issues['broken JSON-LD'].append(name)
            continue
        for o2 in (o if isinstance(o, list) else [o]):
            if isinstance(o2, dict) and o2.get('@type'):
                types.add(o2['@type'])
    if 'BreadcrumbList' not in types:
        issues['no BreadcrumbList'].append(name)
    if slug and 'FAQPage' not in types:
        issues['no FAQPage'].append(name)
    if slug and 'WebApplication' not in types:
        issues['no WebApplication'].append(name)

    imgs = re.findall(r'<img\b[^>]*>', h)
    noalt = [i for i in imgs if 'alt=' not in i]
    if noalt:
        issues['img without alt'].append('%s (%d)' % (name, len(noalt)))

    internal = set(re.findall(r'href="/([a-z0-9\-]+)/"', h))
    internal.discard(slug)
    if slug and len(internal) < 6:
        issues['under 6 internal links'].append('%s (%d)' % (name, len(internal)))

    if slug:
        for dest in internal:
            if dest in hidden:
                issues['links to a hidden page'].append('%s -> %s' % (name, dest))

check('', os.path.join(REPO, 'index.html'))
for d in sorted(os.listdir(REPO)):
    p = os.path.join(REPO, d)
    if not os.path.isdir(p) or d.startswith('.') or d in SKIP or d in hidden:
        continue
    f = os.path.join(p, 'index.html')
    if os.path.isfile(f):
        check(d, f)

print('live pages checked: %d   (hidden, skipped: %d)\n' % (pages, len(hidden)))
for k in sorted(issues, key=lambda x: -len(issues[x])):
    v = issues[k]
    print('%-28s %3d   %s' % (k, len(v), ', '.join(v[:5]) + (' …' if len(v) > 5 else '')))
if not issues:
    print('no issues found')
