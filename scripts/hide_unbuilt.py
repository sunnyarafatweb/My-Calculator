# -*- coding: utf-8 -*-
"""Take the still-unbuilt calculator pages out of circulation, reversibly.

Sixty pages carry a form that looks like a calculator and does nothing: the
answer is hard-coded in the markup and typing changes none of it. That is the
single clearest "low value content" signal on the site, and it is 29% of the
pages. They stay in the repo and come back one at a time as each is rebuilt;
this only stops anyone finding them in the meantime.

Three things have to happen together, because any one alone leaves them
reachable:

  1. X-Robots-Tag: noindex in _headers, so Google drops them from the index.
     Cloudflare Pages' _redirects cannot return 404 - it supports only
     301/302/303/307/308 and 200 - and 301-ing sixty pages at one hub reads as
     a soft 404, so noindex is both the correct signal and the honest one:
     the page exists, it is simply not ready.
  2. Out of sitemap.xml, which is the first thing a reviewer or a crawler reads.
  3. Every internal link removed - 558 of them across 94 pages. Without this
     the site is full of links to pages Google is told to ignore.

Link removal is not one operation. A card in a directory listing is deleted
whole; a link inside a sentence loses its anchor but keeps its words, because
the sentence still reads correctly and deleting it would damage the article.

Run with --write; a dry run otherwise. Restoring one page: drop its line from
_headers, re-add its sitemap entry, and the rebuild puts the links back.
"""
import os, re, io, sys, json, collections, hashlib

REPO = "/home/claude/repo"
SHARED = {'4f709749', 'd82fa8f7', '5adb0f8c'}
NONCALC = {'404', '_not-found', 'all-calculators', 'contact', 'about', 'terms',
           'sitemap', 'privacy-policy'}
SKIP = {'og', 'scripts', '.git', 'node_modules', '_next', 'assets', 'img', 'fonts'}

MARK_OPEN = '# --- unbuilt pages: hidden until each one is rebuilt ---'
MARK_CLOSE = '# --- end unbuilt pages ---'


def unbuilt():
    """A page is unbuilt when it carries no JavaScript of its own - only the
    header, search and footer scripts every page shares."""
    out = []
    for d in sorted(os.listdir(REPO)):
        p = os.path.join(REPO, d)
        if not os.path.isdir(p) or d.startswith('.') or d in SKIP or d in NONCALC:
            continue
        f = os.path.join(p, 'index.html')
        if not os.path.isfile(f):
            continue
        h = io.open(f, encoding='utf-8', errors='replace').read()
        body = re.sub(r'<!-- CB-UX:.*?</script>', '', h, flags=re.S)
        scripts = [s for s in re.findall(
            r'<script(?![^>]*application/ld\+json)[^>]*>(.*?)</script>', body, re.S)
            if len(s) > 300]
        own = sum(len(s) for s in scripts
                  if hashlib.md5(s.encode()).hexdigest()[:8] not in SHARED)
        if own == 0:
            out.append(d)
    return out


def strip_links(h, hidden):
    """Remove links to hidden pages. Returns (html, counts by kind)."""
    n = collections.Counter()

    # 1. directory cards - the whole card goes
    def card(m):
        if m.group(1) in hidden:
            n['card'] += 1
            return ''
        return m.group(0)
    h = re.sub(r'<a class="ci" href="/([a-z0-9\-]+)/">.*?</a>', card, h, flags=re.S)

    # 2. the HTML sitemap page's link list
    def smlink(m):
        if m.group(1) in hidden:
            n['sitemap_link'] += 1
            return ''
        return m.group(0)
    h = re.sub(r'<a href="/([a-z0-9\-]+)/" class="sm-link">[^<]*</a>\s*', smlink, h)

    # 3. sidebar rows in the navy Related-calculators card
    def side(m):
        if m.group(1) in hidden:
            n['sidebar'] += 1
            return ''
        return m.group(0)
    h = re.sub(r'<a href="/([a-z0-9\-]+)/"><span>[^<]*</span><span>&rarr;</span></a>',
               side, h)

    # 3b. the same row in older sidebar markup, where the arrow is a span
    #     with a class rather than an entity
    def side2(m):
        if m.group(1) in hidden:
            n['sidebar'] += 1
            return ''
        return m.group(0)
    h = re.sub(r'<a href="/([a-z0-9\-]+)/">[^<]*<span class="arrow">[^<]*</span></a>',
               side2, h)

    # 3c. and a third sidebar shape, label then a bare arrow span
    def side3(m):
        if m.group(1) in hidden:
            n['sidebar'] += 1
            return ''
        return m.group(0)
    h = re.sub(r'<a href="/([a-z0-9\-]+)/">[^<]*<span[^>]*>[^<]*</span></a>\s*', side3, h)

    # 4. anything left inside a sentence or a related-links line keeps its
    #    words and loses only the anchor
    def unlink(m):
        if m.group(1) in hidden:
            n['unlinked'] += 1
            return m.group(2)
        return m.group(0)
    h = re.sub(r'<a href="/([a-z0-9\-]+)/"[^>]*>([^<]*)</a>', unlink, h)

    # a related-links line can end up with a dangling separator
    h = re.sub(r'(<p class="rel-links">)\s*(<span class="sep">&middot;</span>\s*)+',
               r'\1', h)
    h = re.sub(r'(<span class="sep">&middot;</span>\s*){2,}',
               '<span class="sep">&middot;</span>', h)
    h = re.sub(r'\s*(<span class="sep">&middot;</span>\s*)+(</p>)', r'\2', h)
    return h, n


SIDEBAR_MIN = 10


def page_title(h, slug):
    m = re.search(r'<h1[^>]*>(.*?)</h1>', h, re.S)
    return re.sub(r'<[^>]+>', '', m.group(1)).strip() if m else slug


def refill_sidebar(h, slug, pool, cat_of):
    """A sidebar that listed mostly unbuilt pages can come out of the strip
    with three links in it, which reads as broken. Top it back up from built
    pages, same category first."""
    m = re.search(r'(<div class="[a-z0-9\-]*calc-card">.*?)(<a class="[a-z0-9\-]*viewmore")',
                  h, re.S)
    if not m:
        return h, 0
    card = m.group(1)
    have = re.findall(r'<a href="/([a-z0-9\-]+)/"><span>', card)
    if len(have) >= SIDEBAR_MIN:
        return h, 0
    mine = cat_of.get(slug)
    taken = set(have) | {slug}
    ranked = sorted(pool,
                    key=lambda s: (cat_of.get(s) != mine, s))
    add = [s for s in ranked if s not in taken][:SIDEBAR_MIN - len(have)]
    if not add:
        return h, 0
    rows = ''.join('<a href="/%s/"><span>%s</span><span>&rarr;</span></a>'
                   % (s, pool[s]) for s in add)
    h = h[:m.end(1)] + rows + h[m.end(1):]
    return h, len(add)


def main(write):
    hidden = set(unbuilt())
    print('unbuilt pages: %d' % len(hidden))

    # built pages, with their titles and categories, to refill sidebars from
    pool, cat_of = {}, {}
    for d in sorted(os.listdir(REPO)):
        f = os.path.join(REPO, d, 'index.html')
        if not os.path.isdir(os.path.join(REPO, d)) or d in SKIP or not os.path.isfile(f):
            continue
        if d in hidden or d in NONCALC:
            continue
        h = io.open(f, encoding='utf-8', errors='replace').read()
        pool[d] = page_title(h, d)
        c = re.search(r'all-calculators/#(fin|hea|mat|oth|cry)', h)
        cat_of[d] = c.group(1) if c else None

    # --- 1. noindex headers
    hp = os.path.join(REPO, '_headers')
    hd = io.open(hp, encoding='utf-8').read()
    hd = re.sub(re.escape(MARK_OPEN) + r'.*?' + re.escape(MARK_CLOSE) + r'\n?',
                '', hd, flags=re.S)
    block = [MARK_OPEN,
             '# Each line goes when that page is rebuilt. The files stay in the repo.']
    for s in sorted(hidden):
        block.append('/%s/*' % s)
        block.append('  X-Robots-Tag: noindex')
    block.append(MARK_CLOSE)
    hd_new = hd.rstrip('\n') + '\n\n' + '\n'.join(block) + '\n'

    # --- 2. sitemap
    sp = os.path.join(REPO, 'sitemap.xml')
    sm = io.open(sp, encoding='utf-8').read()
    removed = 0
    for s in sorted(hidden):
        pat = re.compile(r'\s*<url>\s*<loc>https://calculatorboss\.com/%s/</loc>.*?</url>'
                         % re.escape(s), re.S)
        sm, k = pat.subn('', sm)
        removed += k
    left = len(re.findall(r'<loc>', sm))

    # --- 3. internal links
    totals = collections.Counter()
    touched = []
    for d in sorted(os.listdir(REPO)):
        p = os.path.join(REPO, d)
        if not os.path.isdir(p) or d in SKIP:
            continue
        f = os.path.join(p, 'index.html')
        if not os.path.isfile(f):
            continue
        h = io.open(f, encoding='utf-8', errors='replace').read()
        new, n = strip_links(h, hidden)
        # only repair a sidebar this change damaged, never one that was
        # already short for its own reasons
        if d not in hidden and n['sidebar']:
            new, k = refill_sidebar(new, d, pool, cat_of)
            if k:
                totals['sidebar_refilled'] += k
        if new != h:
            touched.append((d, sum(n.values())))
            totals.update(n)
            if write:
                io.open(f, 'w', encoding='utf-8').write(new)

    print('sitemap entries removed : %d  (left: %d)' % (removed, left))
    print('pages touched           : %d' % len(touched))
    print('links removed by kind   : %s' % dict(totals))
    print('top pages               : %s' % touched[:0] or '')
    for d, k in sorted(touched, key=lambda x: -x[1])[:8]:
        print('   %-34s %d' % (d, k))

    if write:
        io.open(hp, 'w', encoding='utf-8').write(hd_new)
        io.open(sp, 'w', encoding='utf-8').write(sm)
        print('\nwritten: _headers, sitemap.xml and %d pages' % len(touched))
    else:
        print('\n(dry run, nothing written)')


if __name__ == '__main__':
    main('--write' in sys.argv)
