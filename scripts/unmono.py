# -*- coding: utf-8 -*-
"""Take monospace off the number pages that do not need it.

Four pages set their own --<prefix>-mono and apply it to the input boxes, the
big answer and the result rows. On a page whose values are plain decimal
numbers that reads as code rather than as a finished tool.

Only the page's own variable is touched. The shared --f-mono stays: the shell
uses it for pills, eyebrows, category counts and footer headings on all 224
pages, and those are meant to be monospace.

Monospace is also kept, deliberately, on binary-calculator, base64 and
big-number-calculator, where fixed-width characters are the point.
"""
import io, re, sys, os

REPO = "/home/claude/repo"
PAGES = ['confidence-interval-calculator', 'log-calculator',
         'root-calculator', 'exponent-calculator']

SANS = ("var(--f-body,'IBM Plex Sans',ui-sans-serif,system-ui,sans-serif);"
        "font-variant-numeric:tabular-nums")


def fix(slug, write=False):
    path = os.path.join(REPO, slug, 'index.html')
    h = io.open(path, encoding='utf-8').read()

    prefixes = sorted(set(re.findall(r'var\(--([a-z0-9]+)-mono\)', h)) - {'f'})
    if not prefixes:
        return '%-34s nothing page-specific to change' % slug

    h2, total = h, 0
    for pfx in prefixes:
        needle = 'font-family:var(--%s-mono)' % pfx
        n = h2.count(needle)
        h2 = h2.replace(needle, 'font-family:' + SANS)
        total += n

    shared_before = h.count('var(--f-mono)')
    shared_after = h2.count('var(--f-mono)')
    if shared_before != shared_after:
        return '%-34s REFUSED: would change shared --f-mono' % slug

    if write:
        io.open(path, 'w', encoding='utf-8').write(h2)
    return ('%-34s changed %d page rules (%s); shared --f-mono untouched at %d'
            % (slug, total, ', '.join('--%s-mono' % p for p in prefixes), shared_after))


write = '--write' in sys.argv
for s in PAGES:
    print(fix(s, write))
print('written' if write else '(dry run)')
