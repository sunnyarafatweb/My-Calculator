#!/usr/bin/env python3
"""Rewrite sitemap.xml <lastmod> values from git history, and report coverage gaps.

Why git rather than "today": lastmod is only a useful signal to a search engine while it
is true. Stamping every URL with the current date on each deploy makes the whole file
untrustworthy and the dates get discounted. Taking the date from the last commit that
actually touched a page's index.html means the file always tells the truth for free.

Usage:
    python3 scripts/update_sitemap.py            # report only, changes nothing
    python3 scripts/update_sitemap.py --write    # rewrite sitemap.xml

Run it as the last step before a deploy, after the page files are committed.
"""
import argparse, os, re, subprocess, sys
from datetime import datetime, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP = os.path.join(REPO, 'sitemap.xml')
BASE = 'https://calculatorboss.com/'

# Directories that are not public pages.
SKIP_DIRS = {'404', '_not-found', '_next', 'og', 'scripts', 'node_modules', '.git'}


def git_iso(path):
    """Last commit date that touched path, as an ISO-8601 UTC string, or None."""
    try:
        out = subprocess.run(['git', 'log', '-1', '--format=%cI', '--', path],
                             cwd=REPO, capture_output=True, text=True, timeout=20)
        s = out.stdout.strip()
        if not s:
            return None
        dt = datetime.fromisoformat(s).astimezone(timezone.utc)
        return dt.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    except Exception:
        return None


def redirected_slugs():
    """Slugs that 301 elsewhere must stay out of the sitemap."""
    out = set()
    rp = os.path.join(REPO, '_redirects')
    if not os.path.exists(rp):
        return out
    for line in open(rp, encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if len(parts) >= 2:
            out.add(parts[0].strip('/').split('/')[0])
    return out


def page_dirs():
    out = set()
    for d in sorted(os.listdir(REPO)):
        if d in SKIP_DIRS or d.startswith('.') or not os.path.isdir(os.path.join(REPO, d)):
            continue
        if os.path.exists(os.path.join(REPO, d, 'index.html')):
            out.add(d)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true', help='rewrite sitemap.xml in place')
    args = ap.parse_args()

    xml = open(SITEMAP, encoding='utf-8').read()
    blocks = re.findall(r'<url>.*?</url>', xml, re.S)
    print(f'sitemap.xml: {len(blocks)} URLs')

    changed, missing_page, no_git = [], [], []
    new_xml = xml

    for blk in blocks:
        loc = re.search(r'<loc>([^<]+)</loc>', blk).group(1)
        slug = loc.replace(BASE, '').strip('/')
        rel = 'index.html' if slug == '' else f'{slug}/index.html'
        if not os.path.exists(os.path.join(REPO, rel)):
            missing_page.append(slug or '(home)')
            continue
        iso = git_iso(rel)
        if not iso:
            no_git.append(slug or '(home)')
            continue
        old = re.search(r'<lastmod>([^<]*)</lastmod>', blk)
        if not old:
            continue
        if old.group(1) != iso:
            changed.append((slug or '(home)', old.group(1)[:10], iso[:10]))
            new_blk = blk.replace(f'<lastmod>{old.group(1)}</lastmod>',
                                  f'<lastmod>{iso}</lastmod>')
            new_xml = new_xml.replace(blk, new_blk, 1)

    # coverage
    listed = {re.search(r'<loc>([^<]+)</loc>', b).group(1).replace(BASE, '').strip('/')
              for b in blocks}
    redirects = redirected_slugs()
    absent = sorted(d for d in page_dirs() if d not in listed and d not in redirects)

    print(f'\nlastmod updates: {len(changed)}')
    for slug, o, n in changed[:12]:
        print(f'   {slug:38} {o} -> {n}')
    if len(changed) > 12:
        print(f'   ... and {len(changed)-12} more')
    if missing_page:
        print(f'\nURLs in sitemap with no page ({len(missing_page)}): {missing_page[:8]}')
    if no_git:
        print(f'\nno git history ({len(no_git)}): {no_git[:8]}')
    if absent:
        print(f'\nlive pages absent from sitemap ({len(absent)}):')
        for d in absent:
            print(f'   {d}')
    else:
        print('\nlive pages absent from sitemap: none')

    added = 0
    if args.write and absent:
        # Insert any live page that is missing, just before the closing tag.
        entries = []
        for slug in absent:
            iso = git_iso(f'{slug}/index.html') or datetime.now(timezone.utc).strftime(
                '%Y-%m-%dT%H:%M:%S.000Z')
            entries.append(
                f'<url>\n<loc>{BASE}{slug}/</loc>\n<lastmod>{iso}</lastmod>\n'
                f'<changefreq>monthly</changefreq>\n<priority>0.8</priority>\n</url>')
            added += 1
        new_xml = new_xml.replace('</urlset>', '\n'.join(entries) + '\n</urlset>')

    if args.write:
        open(SITEMAP, 'w', encoding='utf-8').write(new_xml)
        print(f'\nwrote sitemap.xml ({len(changed)} lastmod updated, {added} URLs added)')
    else:
        print('\n(report only — pass --write to apply)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
