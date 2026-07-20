# Calculator Boss — Build Progress & Priority Queue

Read this together with `DESIGN_AND_SEO_GUIDE.md` at the start of every session.
The guide covers **how** to build/audit a page (design system, SEO checklist,
3-card pattern, protected style block rule). This file tracks **what's been
done and what's next** so a new session doesn't need the whole history
re-explained.

## GSC-based priority queue (established mid-July 2026)

| # | Calculator | Type | Status |
|---|---|---|---|
| 1 | Horsepower Calculator | Upgrade | ✅ DONE — 4 tabs: Torque & RPM (with Solve For + power-to-weight), Force/Distance/Time, Power Unit Converter, Wheel ↔ Crank HP (drivetrain loss) |
| 2 | Engine Horsepower Calculator | Upgrade | ✅ DONE — 4 tabs: Elapsed Time (ET), Trap Speed, Predict My Run (reverse), 1/8-Mile Converter |
| 3 | Time Zone Calculator | Upgrade (thin, ~434 lines) | ✅ DONE — rebuilt to 3-card pattern: city-to-city converter (33 cities, DST-aware via Intl/browser tz database, verified independently in Node + Playwright before shipping), day-shift + hour-difference readout, dual 24h business-hours timeline, live auto-updating World Clock (9 cities), Time Zone Abbreviations reference table, PDF export, 6 H2 content sections + 6 FAQs, new OG image |
| 4 | IRA Calculator | Upgrade (thin) | ✅ DONE — rebuilt to 3-card pattern: 2 tabs — Grow My IRA (age/balance/contribution/return growth projection with 2026 contribution-limit chips, plus an optional 2026 Traditional-deduction eligibility checker by filing status/workplace-plan coverage/MAGI) and Traditional vs. Roth (same-pretax-dollar comparison driven by tax-rate-now vs. tax-rate-in-retirement, verified to correctly flip winners in both directions and tie when rates are equal); year-by-year growth schedule + stacked contributions/growth chart + 2-segment donut; bottomgrid reference cards for 2026 contribution/deduction-limit ranges and a live RMD quick-reference tool (Uniform Lifetime Table lookup, age-73-vs-75 birth-year toggle); PDF export lazy-loaded from the start. 8 H2 sections + 6 FAQs, new OG image. See "Also completed" below for verification detail. |
| 5 | Roth IRA Calculator | Upgrade (thin) | pending — sibling of #4, do next |
| 6 | Annuity Payout Calculator | Upgrade (thin) | ✅ DONE (done out of order, ad-hoc user request Jul 20, 2026) — rebuilt to 3-card pattern, reusing Annuity Calculator's visual/JS conventions (apo- prefix): two tabs — Fixed Length (solve for payout amount) and Fixed Payment (solve for how long a chosen payment lasts, with automatic perpetuity detection when payment ≤ periodic interest); Payout Frequency selector (Monthly/Quarterly/Semiannual/Annual); level-payment annuitization formula verified independently in Node before shipping; year-by-year schedule table + stacked interest-vs-principal chart + 2-segment donut; PDF export; competitor research (calculator.net, annuity.org, catalinastructuredfunding, CBS/SmartAsset $100k-annuity coverage) folded into a "what real lifetime annuities pay vs. this calculator's period-certain math" section; 7 H2 sections + 6 FAQs; new OG image.
| 7 | P/E Ratio Calculator | **New page** (doesn't exist yet) | pending |
| 8 | Gold Calculator | **New page** (doesn't exist yet) | pending |

When #3–8 are all done, re-pull GSC data and re-rank the next batch — don't
assume this exact order still holds after a few weeks of new data.

## Also completed (ad-hoc audit requests, outside the numbered queue above)

- **Business Loan Calculator** (ad-hoc user request, Jul 20, 2026 — flagged
  by the user as a future priority-revenue page: planned affiliate
  placements with banks/lenders and AdSense, aimed at business owners and
  professionals, with an explicit "no bugs, no missing info, world-class"
  bar). Rebuilt from a thin 434-line single-metric page into a 3-tab tool,
  treated with the highest verification rigor of any build so far:
  - **Keyword research first**: cross-checked NerdWallet (payment calc +
    separate factor-rate-to-APR converter), Crestmont Capital, PrimeRates,
    and a dedicated competitor (businessloancalculatorhub.com, which lists
    payment/APR/affordability/DSCR/MCA as separate tools). Confirmed DSCR
    and MCA-true-cost are genuine, distinct, high-value query clusters
    the old page didn't touch at all — decided to fold all three into one
    page as tabs (same beat-the-fragmented-competition strategy used for
    IRA/Bond), rather than a single generic payment box.
  - **Tab 1 (Loan Payment)**: standard amortizing payment/APR, with a
    "solve for max loan amount given a target payment" reverse toggle, and
    an SBA 7(a)-aware fee mode. SBA guarantee fee tiers for FY2026
    (2%/3%/3.5%+3.75% on the guaranteed portion, tiered by loan size, with
    a manufacturer NAICS 31-33 waiver up to $950k) were sourced from a
    trade-association citation of the actual SBA fee notice (NAGGL) and
    cross-verified against an independent worked example from a third
    source (a $1.2M loan -> $900k guaranteed portion -> exact $31,500 fee
    match). The reverse-solve mode uses iterative convergence (fee depends
    on loan size, loan size depends on fee) verified to land on the exact
    target payment to the penny in both the fee-financed and
    fee-paid-upfront cases.
  - **Tab 2 (DSCR Affordability)**: solves the actual number most
    commercial lenders underwrite to — max new loan amount given monthly
    net operating income, existing debt, and a target Debt Service
    Coverage Ratio (1.25 default, the most commonly cited lender minimum,
    confirmed across Fannie-Mae-adjacent and lending-industry sources).
    Round-trip verified: feeding the computed max loan back through the
    payment formula reproduces the exact target DSCR. Correctly handles
    the "existing debt already exceeds capacity" edge case (shows $0,
    error state) and the directional sanity check that a stricter target
    DSCR produces a lower max loan.
  - **Tab 3 (Merchant Cash Advance)**: converts a factor rate into both
    the commonly-cited "simple annualized" cost AND a true,
    remittance-schedule-adjusted effective APR, using the same bisection
    technique this site already uses for reverse APR/YTM problems. This
    second, more accurate number is the genuine differentiator — it
    correctly comes out meaningfully higher than the simple figure (e.g.
    202.9% effective vs. 60.8% simple for the same $50k/1.30-factor/
    180-day example), which matches the qualitative "MCAs often exceed
    150-350% APR when properly calculated" figures found during research,
    rather than just repeating the naive calculation most competitor
    tools stop at.
  - Rate-range reference card (SBA 7(a), SBA 504, bank term, online term,
    bank/online line of credit, equipment financing, MCA factor range) and
    a business-financing glossary (DSCR, factor rate, guarantee fee,
    personal guarantee), all sourced from live research (SoFi, Crestmont
    Capital, Xero, LendingValley, Bankrate) rather than assumed figures.
  - 9 H2 content sections (including a loan-type comparison table) + 6
    FAQs, written for both first-time entrepreneurs and established
    business owners per the user's explicit brief. Proactively ran the
    FAQ-schema-vs-visible-text diff check *before* assembling the page for
    the first time (rather than after, as in every prior session) —
    caught the same em-dash mismatch pattern again (2 of 6 answers) and
    fixed it pre-emptively, confirming this is now a reliable, repeatable
    step regardless of how carefully the content is authored.
  - Given the stakes called out for this specific page, ran a
    substantially heavier-than-usual Playwright pass: default calculation
    on all 3 tabs cross-verified against independent Node calculations
    (exact matches, including the $1.2M SBA worked-example cross-check);
    reverse-solve round-trips in both fee-financed and fee-upfront modes;
    zero-fee sanity check (APR collapses to exactly the stated rate);
    manufacturer-waiver edge case tested both just-under and just-over the
    $950k threshold; DSCR edge case and directional check; MCA daily vs.
    weekly remittance and invalid-factor-rate handling; a dedicated
    duplicate-ID sweep (none found, direct carry-over of the lesson from
    the Budget Calculator session); all 23 internal links and all in-page
    TOC anchors resolve; PDF export verified from all 3 tabs individually;
    mobile layout checked; zero console errors across every round. New OG
    image; title/meta description tightened after drafting to fit
    standard SERP display length for maximum click-through, per the
    user's explicit ask to write it the way a business owner would
    actually want to click.
  **Same-day follow-up** (user asked for a cross-check specifically
  against the biggest/highest-traffic sites in this space): fetched and
  reviewed Bankrate, NerdWallet, calculator.net, SCORE.org (SBA-affiliated
  nonprofit), and Citizens Bank's own business loan calculators. Finding:
  every one of them is meaningfully thinner than what's already built here
  -- most ask only for loan amount/rate/term (Bankrate, SCORE), NerdWallet
  asks for loan amount/term/APR directly without a fee breakdown, and none
  of the five combine a payment calculator with DSCR affordability or an
  MCA true-cost calculator in one tool. No missing calculation coverage
  found. Did find two real UX clarity gaps worth fixing, both addressed:
  (1) borrowed NerdWallet's own good practice of reminding users to
  subtract any down payment before entering the loan amount -- added as a
  subnote under the Loan Amount field, correctly toggled off in
  target-payment reverse-solve mode where that field is hidden; (2) the
  "Manufacturing business (NAICS 31-33)" checkbox assumed the visitor
  already knows what a NAICS code is -- added a plain-English subnote
  ("you make a physical product... rather than provide a service").
  Re-verified after both edits: zero duplicate IDs, zero console errors,
  all 3 tabs' default calculations unchanged, Clear button still resets
  correctly.
  **Second same-day follow-up** (user asked to think as an actual loan
  candidate would, and pushed further on the "biggest sites" comparison
  specifically to find real behavioral gaps, not just field-parity gaps):
  fetched Bankrate/NerdWallet/calculator.net/SCORE loan-calculator pages
  directly (mostly basic amount+rate+term) and researched Fundera/Lendio
  (the major loan marketplaces) -- confirmed they're lead-gen application
  funnels rather than calculators, but their core value prop of
  "compare up to 4 lenders side-by-side" validated a genuine feature gap.
  Cross-referenced our own site's existing Debt Payoff Calculator, which
  already has a proven "extra payment" UX concept -- extended that idea
  into this page rather than inventing a new pattern. Added two features
  to the Loan Payment tab:
  - **Extra monthly payment** field: re-runs the amortization with that
    amount applied to principal every month and reports the accelerated
    payoff time and interest saved. Verified in Node first (baseline 84mo/
    \$93,224 interest -> \$500/mo extra: 72mo/\$78,519, saves 12mo/\$14,704;
    \$2,000/mo extra: 50mo, saves more; \$50,000/mo edge case: 5mo, doesn't
    crash), then confirmed the live page matches every one of those
    figures exactly. The on-screen amortization schedule and chart switch
    to the accelerated version when this is used, and the PDF export was
    updated to match (it was silently ignoring the field before the fix --
    caught and corrected before shipping).
  - **Compare to a second loan offer**: reused the exact proven toggle
    pattern from apr-calculator (checkbox reveals Rate/Term/Fees for
    Offer B, same assumed loan amount as Offer A) rather than designing a
    new one. Verified in Node with a deliberately counter-intuitive
    example -- a higher-rate, shorter-term, lower-fee offer that actually
    has a *lower* total cost than the lower-rate offer -- confirmed the
    live comparison surfaces exactly that "the higher rate is actually
    cheaper" verdict, which is the genuinely useful insight this feature
    exists to catch. Only appears in "I know the loan amount" mode (hidden
    in reverse-solve mode, where there's no fixed loan amount to compare
    against).
  - Caught and fixed two cross-cutting bugs *before* they shipped, found
    by deliberately tracing state across tab switches and error states
    rather than only testing the new feature in isolation: switching to
    the DSCR or MCA tab while the compare box was open left it visibly
    stuck on screen (Tab 2/3's calculate functions never touched it), and
    triggering an input error on the Loan Payment tab left a stale compare
    box showing alongside the error message. Both fixed by explicitly
    hiding the compare box in the tab-switch handler and in showError().
  - Added a short paragraph on both features to "How This Calculator
    Works" and two new FAQs (extra payments, comparing offers), bringing
    the total to 8 -- ran the schema-vs-visible-text diff check before
    testing this time and it matched cleanly on the first attempt (all 8
    entries), the first build session where that's happened.
  - Final full regression after all changes: zero duplicate IDs, all 23
    internal links and all in-page anchors resolve, PDF export verified
    from all 3 tabs again, zero console errors, both original tabs (DSCR,
    MCA) and their default calculations unaffected.

- **Budget Calculator** (ad-hoc user request, Jul 20, 2026, reference:
  calculator.net/budget-calculator.html): rebuilt from a minimal 3-input
  page (Needs/Wants/Savings entered manually by the user, static 45/30/15
  example) into a full itemized budget tool matching every income/expense
  line item calculator.net's reference calculator has -- 4 income lines +
  tax rate + 37 expense line items across 8 categories (Housing &
  Utilities, Transportation, Other Debt & Loan Payments, Living Expenses,
  Healthcare, Children & Education, Savings & Investments, Miscellaneous
  Expenses), each with an independent Monthly/Yearly toggle per the
  reference site's own UX, per explicit user instruction to match its
  value-entry fields one-for-one while keeping our own design and our own
  unique SEO article content (not copying any of its text).
  - Categories are collapsible (first one open by default, Expand/Collapse
    All toggle) given the sheer number of fields; income and category
    fields are rendered from a single JS data model rather than 40+
    hand-duplicated HTML blocks, keeping the page maintainable.
  - Verified the full calculation chain in Node with a realistic worked
    example before locking in the page's default values: gross $6,200/mo
    -> 22% tax -> $4,836 net -> $4,720 total expenses -> +$116/mo left
    over, landing at a 51.5/26.5/19.6 needs/wants/savings split (close to
    the classic 50/30/20 target) and a 22.6% debt-to-income ratio
    ("Excellent" tier) -- a deliberately realistic, illustrative default
    rather than arbitrary round numbers.
  - Built two differentiators beyond the reference site's plain category
    list: an automatic **50/30/20 classification** (each line item
    pre-assigned to needs/wants/savings, with the "Living Expenses"
    category split field-by-field since food/household-supplies are needs
    but clothing/meals-out/other are wants) rendered as target-marked bar
    charts, and a **debt-to-income ratio** card (housing + auto loan +
    credit card + student loan + other loans + child support, divided by
    gross income) with standard lender-tier thresholds (Excellent ≤36%,
    Good/Manageable 36-43%, High 43-50%, Very High >50%) verified via live
    web search against Fannie Mae/FHA/conventional-lending guidance rather
    than assumed from memory.
  - Category-breakdown donut (8 segments) + table (category, monthly $,
    % of after-tax income); PDF export includes the full summary,
    category breakdown, and 50/30/20 + DTI figures.
  - 8 H2 content sections + 6 FAQs, explicitly disclosing Calculator
    Boss's own needs-vs-wants classification methodology as a judgment
    call (not a regulatory standard) rather than presenting it as
    definitive, and citing the 50/30/20 rule's actual origin (Elizabeth
    Warren & Amelia Warren Tyagi, *All Your Worth*, 2005) correctly.
  - Full Playwright pass: default calculation matches the verified Node
    example exactly, all 41 input fields + 8 category sections render,
    expand/collapse-all works, the Monthly/Yearly toggle correctly
    re-normalizes a category total when switched, deficit scenarios
    correctly flip the result card to a warning state, all 23 internal
    links on the page resolve (none broken), lazy PDF export verified,
    mobile layout verified. Caught and fixed the same
    em-dash-vs-double-hyphen FAQ schema mismatch as both prior sessions
    (now the fourth occurrence across four calculator builds) plus a new
    variant this time -- a straight-vs-curly quote mismatch around `"need"`
    / `"want"` in one question's title -- both caught by the same
    schema-vs-visible-text diff check. New OG image.

- **Bond Calculator** (ad-hoc user request, Jul 20, 2026): rebuilt from a
  static/non-functional 434-line thin page (hardcoded example, no live
  recalculation, price-only) into the full 3-card pattern with 2 tabs,
  following the new mandatory keyword-research process (section 4 of
  `DESIGN_AND_SEO_GUIDE.md`) for the first time end-to-end:
  - **Keyword research first**: short-tail "bond calculator" (calculator.net
    ranks with a combined price + off-coupon-date clean/dirty-price tool);
    long-tail cross-check found Omnicalculator runs *separate* dedicated
    pages for "bond price calculator", "bond yield calculator", and "bond
    YTM calculator" -- strong signal that solving for **yield given price**
    is a distinct, high-value query cluster the old page didn't serve at
    all (it only ever solved for price given yield). Decided to fold both
    directions into one page as 2 tabs, beating the fragmented-across-pages
    competitor approach (same strategy that worked for the IRA Calculator).
    Also found Investor.gov/TreasuryDirect's "Savings Bond Calculator" is a
    completely different product (non-marketable EE/I savings bonds) that
    a meaningful slice of "bond calculator" search traffic is actually
    looking for -- added an explicit disambiguation paragraph + FAQ so
    those visitors aren't misled, rather than silently losing them to a
    bounce.
  - **Tab 1 (Bond Price)**: face value/coupon/market yield/years/frequency
    (annual, semi-annual, quarterly) -> standard PV-of-cash-flows bond
    pricing formula. Verified independently in Node against the old thin
    page's own stated example (face $1,000, 5% coupon, 6% yield, 10yr,
    semi-annual -> $925.61, current yield 5.40%, exact match), plus
    zero-coupon, at-par, and premium sanity checks, all passing.
  - **Tab 2 (Yield to Maturity)**: face value/coupon/current price/years/
    frequency -> YTM solved by bisection (same iterative-solve pattern
    used elsewhere on this site for APR and other reverse calculations).
    Round-trip verified across 4 varied scenarios (feed a Tab-1 price back
    into Tab 2 and recover the exact original yield every time).
  - PV-of-coupons vs. PV-of-face-value 2-segment donut; a genuinely novel
    (for this site) **price-vs-yield sensitivity chart** -- an SVG line
    curve plotting price across a yield range around the current point,
    with the bond's own price/yield marked -- directly illustrating the
    core "price and yield move opposite directions" concept rather than
    reusing the stacked-bar amortization-chart pattern, since a bond isn't
    an amortizing loan.
  - Cash-flow & present-value breakdown table (every coupon period plus
    the discount factor and PV, summing to the price) instead of a
    year-by-year amortization schedule, since a bond isn't paid down like
    a loan.
  - Bottomgrid: bond-terms glossary card, and a "Typical Yield Ranges (Jul
    2026)" reference card (10-yr Treasury ~4.5%, investment-grade corporate
    ~5.0-5.5%, high-yield/junk ~7.5-8%, AAA municipal ~3.0%) sourced via
    live web search (Treasury/FRED, corporate credit spread commentary,
    muni market data) rather than training-data figures, matching the
    existing site convention for rate-reference cards.
  - New H2 content section on **municipal bonds and tax-equivalent yield**
    (with the actual formula and a worked example at the top federal
    bracket, 40.8% combined) as a genuine differentiator competitors'
    plain price-calculator pages don't cover. 8 H2 sections + 6 FAQs.
  - **Caught and fixed the same schema/visible-text mismatch class as the
    IRA Calculator session**: 4 of 6 FAQ schema answers used a plain
    double-hyphen where the visible paragraph used an em dash, caught by
    the same JSON-LD diff check and fixed before shipping. Worth watching
    for on every future page -- schema and visible copy are written in the
    same pass but the schema JSON apparently keeps reverting to a
    double-hyphen habit; a final diff check is now clearly a
    standing-required step, not an optional extra.
  - Full Playwright pass (desktop + mobile): zero console errors, price/YTM
    round-trip exact, zero-coupon/at-par/premium scenarios all correct,
    invalid-input error state, frequency-switch row-count changes correctly
    (20 semi-annual vs. 10 annual periods for the same 10-year bond), lazy
    PDF export (zero jspdf requests before click, correct download after).
    New OG image. Sidebar links to Investment/Interest Rate/Present Value/
    Future Value/CD/IRR calculators (all verified against
    `calculators-index.json`).
  **Same-day follow-up** (user shared a calculator.net screenshot showing
  its second "bonds not traded at the coupon date" tool and asked for
  equivalent options): added a **3rd tab, Accrued Interest**, computing
  accrued interest, clean price, and dirty (settlement) price for a bond
  bought between coupon dates — face value/coupon/yield/frequency plus
  maturity date, settlement date, and a choice of 4 day-count conventions
  (30/360, Actual/360, Actual/365, Actual/Actual). Coupon schedule is
  generated by stepping back from the maturity date at the payment
  interval to find the last/next coupon dates and the number of remaining
  coupons. Verified independently in Node: the accrued-interest formula
  matches a textbook worked example exactly (45 days since last coupon,
  30/360, semi-annual, 5% coupon, $1,000 face → $6.25 accrued); settlement
  landing exactly on a coupon date correctly produces $0 accrued and a
  dirty price that exactly matches the existing (non-fractional-period)
  bond pricing formula for the same remaining-coupon count — a clean
  internal consistency check tying the new fractional-period math back to
  the already-verified base formula. New donut (Clean Price vs. Accrued
  Interest), reused the cash-flow/PV table and price-vs-yield chart for
  this tab. Added a new H2 section on accrued interest/clean/dirty price
  and the day-count conventions, 2 new FAQs, updated meta keywords (added
  "accrued interest calculator", "clean price dirty price calculator") and
  the WebApplication schema description to reflect the new feature, and
  removed/corrected the "doesn't cover accrued interest" line from the
  page's own "what this doesn't cover" section since that's no longer
  true. Full Playwright regression pass on all 3 tabs together (zero
  console errors) plus the same FAQ-schema-vs-visible-text diff check —
  passed on the first attempt this time, unlike the em-dash mismatches
  caught on both prior calculator builds.

- **IRA Calculator — cross-check against major competitors + on-page SEO audit**
  (ad-hoc user request, Jul 20, 2026, same day as the build above): user asked
  to cross-check the just-built IRA Calculator against big competing sites and
  verify on-page SEO is genuinely top-class, and separately asked that **every
  future calculator, starting now, get real keyword research (short-tail +
  long-tail, competition-aware) before its title/meta/content are written**,
  plus ongoing **Google AdSense policy compliance** given the site monetizes
  via AdSense. Concretely this session:
  - Compared the page against calculator.net, NerdWallet, SoFi, Vanguard,
    Fidelity, Forbes Advisor, and AARP's IRA/Traditional-IRA/Roth-IRA/IRA-
    contribution calculators. Findings: this page's tabbed
    growth-projection + deduction-eligibility-checker + Traditional-vs-Roth
    comparison + RMD reference already covers more ground in one page than
    any single competitor does (most split growth vs. contribution-
    eligibility vs. Roth-vs-Traditional into separate tools/pages); confirmed
    "IRA contribution calculator" and "traditional IRA deduction calculator"
    are genuine, distinct, dedicated-tool-worthy query clusters at Vanguard/
    SoFi/Fifth Third/nationaltaxtools.com — already reflected in this page's
    meta keywords and its dedicated H2 + interactive checker, so no gap there.
  - On-page SEO checklist re-verified: title/meta/OG/canonical/robots/
    googlebot all correct; sitemap.xml and calculators-index.json both list
    the page correctly (no accidental duplicate entries — the earlier grep
    match was just "roth-ira-calculator" also containing the substring
    "ira-calculator"); robots.txt allows crawling site-wide.
  - **Caught and fixed a real accuracy issue during the cross-check**: an
    inline sentence pointed readers to the site's separate `/rmd-calculator/`
    page and claimed it covered "multi-year RMD planning, penalty rules, and
    inherited-IRA scenarios" — checking that page's actual content showed
    it's itself still a thin, generic template-tier page (bare 3-H2 pattern,
    no penalty/72(t) content) that doesn't yet cover any of that. Corrected
    the sentence to a neutral, accurate pointer instead of an overclaim.
    Flagging `/rmd-calculator/` to the user as another thin page worth a
    future queue slot — not added to the numbered queue unilaterally, since
    that ranking should stay GSC-data-driven per the existing process.
  - Improved internal linking: swapped the sidebar's "Annuity Calculator"
    link for "RMD Calculator" (more topically relevant to an IRA page) and
    added a contextual in-article link to `/rmd-calculator/` from the RMD H2
    section. Re-ran a Playwright pass after the edits — zero console errors,
    links resolve correctly.
  - **`DESIGN_AND_SEO_GUIDE.md` updated** (see sections 4 and 10 in that
    file) to make keyword research a mandatory, non-skippable step before
    writing title/meta/content for every future calculator — short-tail head
    term + 5-10 long-tail variants + a "high-volume, lower-competition
    middle ground" callout + a competitor cross-check against 3-4 major
    sites — with an honest note that this environment has no paid keyword
    tool or GSC connection, so the method is web-search-based competitive
    proxy research, not guessing. Also added a new Google AdSense compliance
    section (sourced from `support.google.com/adsense`, not third-party
    "how to get approved" blogs, which invent numeric rules Google doesn't
    actually publish) covering original-content/no-thin-pages, no doorway/
    keyword-stuffed pages, no claiming features a linked page doesn't
    actually have (the exact mistake just caught and fixed above), trust
    pages, YMYL disclaimers, future ad-placement spacing, and the `ads.txt`
    file that will need to be added once the user has a real AdSense
    publisher ID (none exists in this repo yet — flagged, not invented).

- **Boat Loan Calculator** (ad-hoc user request, Jul 20, 2026): rebuilt
  from a thin ~434-line page (basic loan-amount/rate/term only) into the
  full tabbed pattern established by Auto Lease Calculator — **Solve for
  Payment** and **Solve for Max Boat Price** (reverse mode). Standard
  amortizing-loan formula verified against two independent, real worked
  examples from competitor sites: boats.com's own published example
  ($76,000 loan, 5.49% APR, 240 months → $522.37/mo, exact match to the
  penny) and BoatTrader's example ($70,000 loan, 120mo, comparing 7% vs.
  9.5% APR → $812.76/$905.78, matching their rounded $813/$906). Sales
  tax and fees are financed into the loan by default (matching how most
  boat buyers actually pay them), with a trade-in tax credit assumption
  clearly disclosed since it varies by state. Reverse-solve formula
  (target payment → max boat price) derived algebraically and round-trip
  verified (feeding a forward result back in recovers the original boat
  price to the penny). Full year-by-year amortization schedule + stacked
  bar chart + principal/interest donut, reused from the established loan-
  calculator pattern. Researched current (Jul 2026) rate context: secured
  boat loans ~7-10% for well-qualified borrowers (best rates ~6.5%,
  average ~8.4% per LendingTree Q4 2025 data), unsecured/personal-loan-
  style boat loans a much wider 7-36%, plus the secured-vs-unsecured
  distinction as its own content section since several competitor pages
  treat this as an important, underexplained nuance. 8 H2 sections + 6
  FAQs, new OG image, PDF export lazy-loaded from the start per the
  standing convention. Full Playwright pass (desktop + mobile): correct
  default calculation, tab switching, reverse-solve round-trip, chip
  presets, invalid-input handling, Clear-button reset, 15-row amortization
  schedule for a 15-year term, lazy PDF export, zero console errors.
  Protected shared style block re-verified byte-identical to bmi-
  calculator.
- **Average Return Calculator** (ad-hoc user request, Jul 20, 2026,
  reference: calculator.net/average-return-calculator.html): rebuilt from
  a thin page (arithmetic-vs-geometric-mean content only, fixed 5-year
  input) into the full 2-tab pattern, covering both scenarios calculator.net's
  version does. **Tab 1 (Cash Flow Method)**: solves for the Money-
  Weighted Rate of Return (MWRR) — same concept as Excel's XIRR — from a
  starting balance, ending balance, and a dynamically add/remove-able
  list of dated deposits/withdrawals. This is a genuinely new UI pattern
  for the site (no prior calculator here needed dynamic row lists); used
  `document.createElement` + event delegation per row rather than a fixed
  field set. Solved via the same bisection approach used elsewhere on the
  site, but **independently cross-verified against Python's
  `scipy.optimize.brentq`** (a different algorithm, different language)
  across four scenarios including a 5-cash-flow case — exact match to
  4 decimal places every time, giving high confidence beyond the site's
  usual single-method Node verification. **Tab 2 (Multiple Period
  Returns)**: geometric vs. arithmetic average and cumulative return
  across a variable number of periods with independent holding lengths
  (years + months each, properly time-weighted rather than assuming
  equal-length periods) — extends the old page's good arithmetic/
  geometric/volatility-drag content (kept and expanded) with dynamic rows
  and an explicit cumulative-return figure the old page lacked. Verified
  against the classic +50%/−50% textbook example (arithmetic mean exactly
  0%, but real cumulative result is −25%, geometric mean ≈ −13.4%/yr).
  Researched and used correct CFA-level terminology throughout (MWRR vs.
  TWRR, why they diverge, which one applies to personal vs. fund-manager
  performance) as a genuine content differentiator — calculator.net's own
  page doesn't explain this distinction. **Caught and fixed two bugs
  during Playwright testing** before shipping: (1) the static starting/
  ending balance and date fields had no live-recalculation listeners
  attached (only the dynamic rows did), so editing them required an
  explicit Calculate click; (2) clicking "+ Add row" didn't trigger an
  immediate recalculation, so a freshly-added empty row silently showed
  a stale prior result instead of the expected validation prompt. Both
  fixed and re-verified. PDF export lazy-loaded from the start per the
  standing convention. 6 H2 sections + 6 FAQs, new OG image, sidebar
  links to Investment/ROI/IRR/Present Value/Compound Interest/Interest
  calculators. Protected shared style block re-verified byte-identical
  to bmi-calculator; scratch build source re-synced from the deployed
  file and confirmed to rebuild byte-identical.
- **Auto Lease Calculator** (ad-hoc user request, Jul 20, 2026): rebuilt
  from a ~434-line thin page to the full 3-card pattern. Formula verified
  independently in Node against the explicit methodology published by
  Edmunds, Kelley Blue Book, and GoodCalculators (all describe the same
  depreciation-fee-plus-money-factor approach): residual value is based
  on **MSRP** (not the negotiated price — leasing companies set it that
  way, a real accuracy fix vs. the old thin page, which conflated the
  two), adjusted cap cost = negotiated price + acquisition fee − down
  payment − trade-in, depreciation fee = (adj cap cost − residual) ÷
  term, finance fee = (adj cap cost + residual) × money factor. Ran a
  regression check confirming that with MSRP forced equal to negotiated
  price (matching the old page's implicit assumption), the new formula
  reproduces the old page's numbers almost exactly. Added a rate-unit
  toggle (APR % / raw money factor) with verified equivalence (0.00125
  MF and its 3% APR equivalent produce identical finance fees). Adds a
  **Lease vs. Financing comparison card** — reuses the standard loan PMT
  formula already verified elsewhere on the site to show what buying the
  same car would cost instead, since a flat lease payment doesn't have a
  naturally interesting month-by-month amortization schedule the way a
  loan does, so this replaces that grid area with something more useful.
  Bottom grid: Key Lease Terms glossary (cap cost, disposition fee,
  excess mileage fee, gap insurance) + a Money Factor ↔ APR quick-
  reference table. Current (Jul 2026) money-factor/residual-value
  figures and the "good rate" benchmarks (≤0.0015, ≈3.6% APR) sourced
  via live search (Capital One, CarWhere, KBB, Vantage Auto Group) rather
  than relying on training-data figures. PDF export built lazy-loaded
  from the start (this session's new standing convention — see
  DESIGN_AND_SEO_GUIDE.md). 8 H2 content sections + 6 FAQs, new OG image.
  Full Playwright pass (desktop + mobile) confirmed correct calculation,
  chip presets, rate-unit toggle, invalid-input handling, Clear-button
  reset, and lazy PDF export triggering a real download with zero
  console errors; protected shared style block re-verified byte-
  identical to bmi-calculator and body-fat-calculator.
  **Same-day follow-ups**: (1) user asked to double-check the build —
  re-verified the formula against calculator.net's own published worked
  example (exact match to the penny, $517.63) as a second independent
  confirmation, did a full SEO re-audit (all clean), and confirmed the
  field set is appropriately scoped (a justified superset of
  calculator.net's, not bloat); gave "Monthly payment (before tax)" and
  "Total of N payments" their own individual result rows per feedback
  (previously the before-tax figure was buried in the subline). (2) added
  the one genuine gap found during the double-check: a "Solve for Max
  Price" reverse mode (calculator.net has this, the original build
  didn't) — given a target monthly budget, solves for the highest
  negotiated price that fits it. Reverse formula derived algebraically
  from the forward engine and round-trip verified in Node (feeding a
  known forward result back in recovers the original price to the
  penny). Caught and fixed a degenerate edge case in testing: an
  unrealistically low target payment could solve for a price implying
  negative depreciation (residual worth more than what's financed) —
  added a validation check with a clear error message for this in both
  modes. Scratch build source re-synced from the deployed file after all
  changes and confirmed to rebuild byte-identical.

- **Site-wide performance investigation** (ad-hoc user request, Jul 20, 2026):
  user reported the site feeling slow in real use despite a 99/100
  PageSpeed score. Diagnosed via live `curl -I`/timing checks rather than
  guessing: (1) confirmed no Cloudflare outage (Dhaka PoP operational,
  checked cloudflarestatus.com directly); (2) found `_headers`' specific
  asset rules (`/_next/static/*`, `*.svg`, `*.ico`, `*.png`) were being
  **merged** with the general `/*` no-store rule rather than overriding
  it — Cloudflare joins duplicate headers with a comma rather than
  letting the more specific rule win — so the shared CSS/JS every single
  page depends on was never actually cached at the edge
  (`cf-cache-status: BYPASS`) despite the `_headers` file's evident
  intent. Fixed with `! Cache-Control` (Cloudflare's documented
  header-reset syntax) before each specific rule; verified live
  (`BYPASS`→`MISS`→`HIT`) and confirmed zero visual/console regressions
  on several pages before and after. Left the HTML `/*` no-store rule
  itself untouched (intentional from the Jul 11 session, and HTML has no
  ETag to make `no-cache` behave differently in practice anyway) to keep
  the fix minimal and zero-risk. Real navigation timing improved
  noticeably (789ms → 546ms → 322ms across three sequential page loads
  in one browser session) since shared assets no longer re-download on
  every navigation.
  **Follow-up, same day**: lazy-loaded jsPDF + jspdf-autotable
  (~403KB combined) on apr-calculator, annuity-payout-calculator, and
  time-zone-calculator — previously loaded unconditionally on every page
  view for a feature most visitors never use. Now loaded only when the
  Save-as-PDF button is clicked (button shows disabled "Loading…" during
  the one-time fetch); verified via Playwright that zero jspdf-related
  requests fire on page load, `window.jspdf` is undefined until clicked,
  and both first- and second-click PDF generation still work correctly.
  This is now the standing convention for PDF export on **all future
  calculator pages** — documented in `DESIGN_AND_SEO_GUIDE.md` section 5
  and as a hard-won lesson in section 6; do not add unconditional
  `<script src="...jspdf...">` tags to any new page going forward.
- **APR Calculator** (ad-hoc user request, Jul 20, 2026): rebuilt from a
  thin ~434-line single-metric page to the full 3-card pattern. Computes
  the real actuarial APR (loan amount, rate, term, discount points, other
  fees) via bisection-solved level-payment formula — verified independently
  in Node against a cited Bankrate example ($300k/7%/30yr/$6,000 fees →
  7.197% published vs. 7.201% computed here) plus zero-fee, monotonicity,
  and invalid-input edge cases. Adds an optional side-by-side second-offer
  comparison (same amount/term, different rate+fees) with a win/lose
  verdict that explicitly flags the early-payoff nuance rather than just
  naming the lower APR the automatic winner. Full amortization schedule +
  chart, principal/interest/fees donut, PDF export, quick presets spanning
  mortgage/auto/personal-loan use cases. Current (Jul 2026) typical-APR-
  range figures for mortgage/auto/personal-loan/credit-card sourced via
  live web search (Freddie Mac PMMS, Bankrate, WalletHub/LendingTree/Forbes)
  rather than relying on training-data figures, since rates move. 8 H2
  content sections + 6 FAQs, new OG image.
  **Same-day follow-up** after the user pointed at calculator.net's
  two-stacked-calculator page (General + Mortgage APR) and asked for a
  gap check: added a "Fees Financed Into Loan" field (distinct from
  upfront fees — verified independently that financing a fee produces a
  slightly *lower* APR than paying the same dollar amount upfront, an
  interesting but correct result), an "Annual PMI/Insurance" field that
  inflates the payment stream used in the APR solve (verified monotonic:
  APR rises as PMI rises), and a "This is a mortgage" toggle that swaps
  the Loan Amount field for House Price + Down Payment (loan amount
  auto-derived). Deliberately did **not** clone calculator.net's second,
  fully separate Mortgage APR Calculator as a duplicate stacked tool, and
  did **not** add its Compound-Frequency-vs-Payment-Frequency matrix
  (9×8 options) — both would have meaningfully bloated the page's DOM/JS
  weight for a rare real-world need (nearly all US consumer loans compound
  and pay monthly), so the mortgage use case was folded into the existing
  lightweight tool via a toggle instead. Also added a "Fixed APR vs.
  Variable APR" content section, a worked 10%→10.47% APR-to-APY numeric
  example, and a 7th FAQ (PMI's effect on APR) that were present on the
  competitor page and genuinely missing here. Re-verified the full
  regression suite (original 7.201% scenario, comparison feature,
  invalid-input handling) still passes byte-for-byte after the additions.
- **Mortgage Calculator**: fixed a misleading "Live" rates badge that was
  showing 15-day-stale hardcoded numbers (now honestly labeled, sourced from
  Freddie Mac PMMS + Bankrate 5/1 ARM, both dated); added visible TOC; added
  a Biweekly Payment Option feature (true 26-period/year amortization,
  verified independently in Node before shipping); reordered the results
  column so Loan Summary / Biweekly sit above the breakdown chart (less
  scrolling to the numbers that matter); added an Extra Payments vs.
  Refinancing vs. Recasting content section + 2 FAQs.
- **Site-wide breadcrumb rollout**: all 193 pages that lacked one.

## Standing notes for next session

- **GSC data** (9-day window ending ~Jul 18, 2026): 11 total clicks, 498
  impressions, avg. position 53.1. Only click-generating query was "leverage
  calculator" (already a custom-built page). Everything else is
  impression-only long-tail on a brand-new domain — ranking improvements are
  realistically a matter of weeks-to-months, not days. Re-check GSC every
  2–4 weeks to see if the priority order above should change.
- **Security**: the GitHub PAT used in past sessions was pasted in plaintext
  in chat multiple times and should be treated as burned — rotate it on
  GitHub and use a fresh token when resuming work, rather than reusing one
  from an old conversation transcript. As of this session (Jul 20, 2026),
  this happened again — treat that token as burned too and rotate before
  the next session. **Update, same day, later session**: it happened again
  (a third time) — a new PAT was pasted directly in chat to start this
  session. Treat that token as burned too. This is now a recurring pattern
  across at least three sessions; strongly consider setting up a way to
  authenticate that doesn't require pasting the raw token into chat each
  time (e.g. the user storing it outside the conversation and Claude Code/
  CLI picking it up from local environment instead) before the next session,
  rather than repeating this note a fourth time.
- **Workflow / no repo clutter**: all scratch work (`build_*.py`,
  `test_*.js`, `verify_*.js`, screenshots) lives in the sandbox's
  `/home/claude/work/` scratch directory for that session only — it is
  never part of this repo and never committed. Only the actual page file
  (`<slug>/index.html`), its `og/<slug>.png`, and any shared files touched
  (`sitemap.xml`, `calculators-index.json`, `all-calculators/index.html`)
  get `git add`ed. Nothing accumulates in the repo between sessions.
