#!/usr/bin/env python3
"""Inject the shared CB-UX behaviour into every 3-card calculator page.

Idempotent: re-running replaces the existing block rather than adding a second one.
Never touches the protected shared style block, the head, or any calculator logic.
"""
import os, re, sys

MARK_OPEN  = '<!-- CB-UX:'
SNIPPET    = open(os.path.join(os.path.dirname(__file__), 'cb_ux.html')).read().rstrip() + '\n'
BLOCK_RE   = re.compile(r'<!-- CB-UX:.*?</script>\s*', re.S)


def in_scope(path):
    s = open(path).read()
    return ('form result sidebar' in s) or ('form rightstack sidebar' in s)


def patch(path):
    s = open(path).read()
    if ('form result sidebar' not in s) and ('form rightstack sidebar' not in s):
        return 'skipped (not a 3-card page)'
    before = s
    s = BLOCK_RE.sub('', s)                      # idempotent: drop any previous block
    i = s.rfind('</body>')
    if i < 0:
        return 'FAILED (no </body>)'
    s = s[:i] + SNIPPET + s[i:]
    if s == before:
        return 'unchanged'
    open(path, 'w').write(s)
    return 'patched'


def main(slugs):
    for slug in slugs:
        p = os.path.join(slug, 'index.html')
        if not os.path.isfile(p):
            print(f'  --  {slug:40} no index.html')
            continue
        print(f'  {patch(p):10} {slug}')


if __name__ == '__main__':
    main(sys.argv[1:])
