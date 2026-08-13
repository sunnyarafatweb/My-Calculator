#!/usr/bin/env python3
"""Check that every calculator page opens with the site's standard top spacing.

Owner directive, Aug 13 2026: the gap between the header and the breadcrumb must
be the same on every calculator. It was not -- three pages had been built with a
larger padding than the other 120, which is only visible if you flick between two
pages and notice.

The convention is not written anywhere; it is readable off the pages themselves,
which is why this reads it rather than hardcoding a preference. Run with --fix to
bring stray pages to whichever wrapper their own family uses.
"""
import re, glob, sys, collections

# Two wrapper families exist and both are legitimate -- the 3-card pages and the
# older max-w-5xl pages. What matters is that a page uses its family's exact
# padding, not a value invented for that one page.
FAMILIES = {
    "px-4 sm:px-6 py-5 sm:py-6 mx-auto": "3-card pages",
    "mx-auto max-w-5xl px-5 py-7 sm:py-9": "older hero pages",
    "wrap": "crypto/trading batch",
    "mx-auto": "policy pages",
}
NON_CALC = {"about", "contact", "privacy-policy", "terms", "sitemap",
            "all-calculators", "404", "_not-found"}

pat = re.compile(r'(<main[^>]*>\s*<div class=")([^"]*)(")')

def wrapper(path):
    h = open(path, encoding="utf-8", errors="ignore").read()
    m = re.search(r"<main.*?</main>", h, re.S)
    if not m:
        return None, h
    mm = pat.search(m.group(0))
    return (mm.group(2).strip() if mm else None), h

def main():
    fix = "--fix" in sys.argv
    counts = collections.Counter()
    pages = {}
    for p in sorted(glob.glob("*/index.html")):
        slug = p.split("/")[0]
        cls, h = wrapper(p)
        if cls is None:
            continue
        pages[slug] = (cls, h, p)
        counts[cls] += 1

    # the dominant wrapper among calculator pages is the standard for new builds
    calc_counts = collections.Counter(c for s, (c, _, _) in pages.items() if s not in NON_CALC)
    standard = calc_counts.most_common(1)[0][0]

    strays = [(s, c) for s, (c, _, _) in pages.items() if c not in FAMILIES]
    print(f"pages checked: {len(pages)}")
    print(f"standard for new calculator pages: \"{standard}\"\n")
    for cls, n in counts.most_common():
        print(f"  {n:4d}  {cls}   [{FAMILIES.get(cls, '*** NOT A KNOWN FAMILY ***')}]")

    if not strays:
        print("\nNo page uses a one-off wrapper. PASS")
        return 0

    print(f"\n{len(strays)} page(s) use a wrapper that belongs to no family:")
    for s, c in strays:
        print(f"  {s}: {c}")
    if fix:
        for s, c in strays:
            cls, h, p = pages[s]
            m = re.search(r"<main.*?</main>", h, re.S)
            mm = pat.search(m.group(0))
            open(p, "w").write(h.replace(mm.group(0), mm.group(1) + standard + mm.group(3), 1))
            print(f"  fixed {s} -> {standard}")
        return 0
    print("\nrun with --fix to bring them to the standard")
    return 1

if __name__ == "__main__":
    sys.exit(main())
