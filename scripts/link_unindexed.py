# -*- coding: utf-8 -*-
"""Give the pages Google crawled and refused to index more internal links.

Search Console reports 20 pages as "Crawled - currently not indexed". They are
not thin: they run 2,400 to 7,771 words each. What they have in common is that
they sit on 3 to 5 internal links, against a site median of 9, and that not one
of them appears in a single related-links block.

The reason is in add_related_links.py: its hand-drawn clusters cover numbers,
encoding, geometry, building, vehicles, time and physical sciences, and nothing
else. Every page on this list is a mortgage, loan, retirement, tax or body
calculator, so no cluster ever matched and the scoring never picked them.

This adds the missing finance and health clusters and runs the same block over
the pages in those clusters that do not have one yet, weighting the under-linked
pages hard so the links land where they are needed. Same markup and styling as
the existing blocks - one quiet line under the article, no new card.
"""
import re, io, glob, collections, os, sys

REPO = "/home/claude/repo"
HUBS = {'all-calculators', 'about', 'privacy-policy', 'terms', 'contact',
        'sitemap', '404', '_not-found'}
PER_PAGE = 6

STOP = {'calculator', 'converter', 'generator', 'counter', 'roller', 'the', 'a',
        'of', 'and', 'to', 'your', 'free', 'online'}

# Reported by Search Console as crawled and not indexed, trailing-slash variants
# and the two non-page URLs removed.
UNINDEXED = {
    'lean-body-mass-calculator', 'amortization-calculator',
    'canadian-mortgage-calculator', 'simple-interest-calculator',
    'estate-tax-calculator', 'one-rep-max-calculator',
    'mutual-fund-calculator', 'fha-loan-calculator', 'bra-size-calculator',
    'inflation-calculator', 'conception-calculator', 'va-mortgage-calculator',
    'interest-rate-calculator', 'mortgage-calculator-uk',
    'repayment-calculator', 'ira-calculator',
    'take-home-paycheck-calculator', 'army-body-fat-calculator',
    'business-loan-calculator', 'healthy-weight-calculator',
}

# The clusters the first pass was missing. Same principle as the originals:
# the groupings a person would actually make, not whatever shares a category.
CLUSTERS = [
    # home loans
    ['mortgage-calculator', 'mortgage-amortization-calculator',
     'mortgage-payoff-calculator', 'mortgage-calculator-uk',
     'canadian-mortgage-calculator', 'fha-loan-calculator',
     'va-mortgage-calculator', 'refinance-calculator',
     'house-affordability-calculator', 'down-payment-calculator',
     'home-equity-loan-calculator', 'heloc-calculator', 'amortization-calculator'],
    # borrowing generally
    ['loan-calculator', 'personal-loan-calculator', 'business-loan-calculator',
     'auto-loan-calculator', 'boat-loan-calculator', 'student-loan-calculator',
     'repayment-calculator', 'payment-calculator', 'apr-calculator',
     'debt-consolidation-calculator', 'debt-payoff-calculator',
     'credit-card-payoff-calculator', 'interest-rate-calculator'],
    # interest and the time value of money
    ['simple-interest-calculator', 'compound-interest-calculator',
     'interest-calculator', 'interest-rate-calculator',
     'future-value-calculator', 'present-value-calculator',
     'savings-calculator', 'cd-calculator', 'inflation-calculator'],
    # investing and retirement
    ['investment-calculator', 'mutual-fund-calculator', 'sip-calculator',
     'roi-calculator', 'cagr-calculator', 'average-return-calculator',
     'retirement-calculator', 'ira-calculator', 'roth-ira-calculator',
     '401k-calculator', 'rmd-calculator', 'pension-calculator',
     'annuity-calculator', 'annuity-payout-calculator',
     'portfolio-allocation-calculator'],
    # tax and pay
    ['income-tax-calculator', 'take-home-paycheck-calculator',
     'salary-calculator', 'marriage-tax-calculator', 'estate-tax-calculator',
     'sales-tax-calculator', 'vat-calculator', 'no-tax-on-tips-calculator',
     'land-transfer-tax-calculator', 'hours-calculator'],
    # body composition
    ['bmi-calculator', 'body-fat-calculator', 'lean-body-mass-calculator',
     'army-body-fat-calculator', 'ideal-weight-calculator',
     'healthy-weight-calculator', 'body-type-calculator',
     'body-surface-area-calculator', 'bmr-calculator', 'tdee-calculator'],
    # training
    ['one-rep-max-calculator', 'pace-calculator', 'target-heart-rate-calculator',
     'calories-burned-calculator', 'macro-calculator', 'protein-calculator',
     'carbohydrate-calculator', 'fat-intake-calculator'],
    # pregnancy and cycle
    ['pregnancy-calculator', 'due-date-calculator', 'conception-calculator',
     'pregnancy-conception-calculator', 'ovulation-calculator',
     'period-calculator', 'pregnancy-weight-gain-calculator'],
    # body measurements
    ['bra-size-calculator', 'shoe-size-conversion', 'height-calculator',
     'ideal-weight-calculator', 'healthy-weight-calculator'],
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
        info[slug] = {'cat': cat.group(1) if cat else None, 'title': title,
                      'has_block': 'rel-links' in h,
                      'article': bool(re.search(r'</article>', h)) or
                                 bool(re.search(r'<p class="[a-z0-9\-]*disclaimer"', body)),
                      'file': f, 'words': words(slug)}
    return info


def insert_at(h):
    """Where the block goes. Most pages end their prose with </article>; the
    health pages have no article wrapper and finish with a disclaimer
    paragraph, so the block goes above that rather than below it."""
    i = h.rfind('</article>')
    if i > 0:
        return i
    m = None
    for m in re.finditer(r'<p class="[a-z0-9\-]*disclaimer"', h):
        pass
    if m:
        return m.start()
    return h.rfind('</main>')


def inbound_counts(info):
    c = collections.Counter()
    for slug in info:
        h = io.open(info[slug]['file'], encoding='utf-8', errors='replace').read()
        for t in set(re.findall(r'href="/([a-z0-9][a-z0-9\-]*)/"', h)):
            if t != slug and t in info:
                c[t] += 1
    return c


def main(dry=True):
    info = load()
    inbound = inbound_counts(info)

    # Pages that may carry a new block: in one of the new clusters, no block
    # yet, and an article to append to. Hubs and the targets themselves are
    # left alone, so a page never links only to pages that are also invisible.
    targets = [s for s in info
               if s in CLUSTER_OF and s not in HUBS and s not in UNINDEXED
               and not info[s]['has_block'] and info[s]['article']]

    candidates = [s for s in info if s not in HUBS]
    plan = {}
    for s in sorted(targets):
        me = info[s]
        scored = []
        for c in candidates:
            if c == s:
                continue
            o = info[c]
            score = 0.0
            if CLUSTER_OF.get(s, set()) & CLUSTER_OF.get(c, set()):
                score += 60
            score += 14 * len(me['words'] & o['words'])
            if o['cat'] and o['cat'] == me['cat']:
                score += 8
            # the point of this pass: push the links toward the pages Google
            # has refused to index, but only where they are genuinely related
            if c in UNINDEXED and (CLUSTER_OF.get(s, set()) & CLUSTER_OF.get(c, set())):
                score += 45
            score += max(0, 8 - inbound[c]) * 0.9
            if inbound[c] > 25:
                score -= 5
            if score >= 40:            # cluster-mates only, no loose matches
                scored.append((score, c))
        scored.sort(key=lambda x: (-x[0], x[1]))
        picked = [c for _, c in scored[:PER_PAGE]]
        if len(picked) < 3:
            continue
        plan[s] = picked
        for c in picked:
            inbound[c] += 1

    gained = collections.Counter()
    for s, picks in plan.items():
        for c in picks:
            if c in UNINDEXED:
                gained[c] += 1

    print("pages getting a block : %d" % len(plan))
    print("links added           : %d" % sum(len(v) for v in plan.values()))
    print()
    print("%-34s %6s %6s" % ("unindexed page", "was", "now"))
    before = inbound_counts(info)
    for s in sorted(UNINDEXED):
        print("%-34s %6d %6d" % (s, before[s], before[s] + gained[s]))
    print()
    print("sample plan:")
    for s in sorted(plan)[:6]:
        print("  %-34s -> %s" % (s, ', '.join(plan[s])))

    if dry:
        print("\n(dry run, nothing written)")
        return

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
        links = '<span class="sep">&middot;</span>'.join(
            '<a href="/%s/">%s</a>' % (c, info[c]['title']) for c in picks)
        section = (
            '<section><h2 class="font-display text-xl text-ink mb-5">Related calculators</h2>'
            + block_css +
            '<p class="rel-links">' + links +
            '<span class="sep">&middot;</span><a href="/all-calculators/">All calculators</a></p>'
            '</section>')
        i = insert_at(h)
        assert i > 0, s
        h = h[:i] + section + h[i:]
        io.open(f, 'w', encoding='utf-8').write(h)
        changed += 1
    print("\nwritten: %d pages" % changed)


if __name__ == '__main__':
    main(dry='--write' not in sys.argv)
