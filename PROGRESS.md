# CalculatorBoss — Build Progress & Priority Queue

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

- **Rent vs. Buy Calculator — full rebuild from thin React/Tailwind-slider
  shell to 3-card pattern** (ad-hoc user request, Jul 21, 2026, prompted by a
  real Google Ads Keyword Planner screenshot showing 10K–100K monthly
  searches, Low competition, $0.26–$1.65 CPC — a genuinely strong opportunity
  the user found and shared directly, not sourced from web-search proxy data
  this time).
  - **Keyword research done before writing any copy, per section 4.**
    Head-term competitive landscape: NYT (the canonical reference everyone
    cites), NerdWallet, Zillow, Redfin, Freddie Mac, calculator.net — mixed
    with smaller independent tools that still rank (rentingvsbuycalculator.com,
    moneycalc.net, calcipedia.org, a state-specific variant on agoodlender.com).
    That mix — Google ranking well-built smaller tools alongside giants, not
    just the giants — is what makes this worth pursuing rather than a lost
    cause against NYT specifically. Cross-checked math/content approach
    against 6+ of these. **Differentiation angle found and built around:**
    nearly every competitor treats the "money you didn't spend on a down
    payment gets invested instead" return rate as a buried/fixed assumption;
    one source states plainly that the break-even year moves from ~year 12
    (at a 4% return) to never-within-30-years (at 6%+) purely from that one
    number — most calculators don't surface this. Built the whole page around
    making that assumption visible, adjustable in the core (non-advanced)
    fields, and backed by a dedicated sensitivity table.
  - **Told the user honestly, before building, that "definitely page 1" isn't
    a promise anyone can make** — explained the Keyword-Planner "Low
    competition" metric is paid-ad competition, not organic ranking
    difficulty (different things), and set expectations around long-tail /
    second-tier ranking as the realistic near-term target rather than
    beating NYT outright.
  - **Math independently verified in Python against a real, independently-published
    competitor result before writing a line of page code** — a $400,000
    home / 20% down / 6.5% rate / 4% investment return scenario, cross-checked
    against rentingvsbuycalculator.com's stated "~year 12" break-even and
    "$2,022.62/mo" payment: both matched exactly. Also verified the
    sensitivity claim itself (2%→8% return sweep): break-even year moves from
    Year 8 down through Year 12, Year 19, then never-within-30-years at 6%+,
    matching the "6%+ and renting can win the whole 30 years" pattern found
    in research. Re-verified twice more after the JS was built — once against
    the page's actual default inputs (an initial discrepancy of ~$2,200 in
    the renter's year-10 net worth turned out to be the Python spot-check
    missing the $15/mo renters-insurance input the real page includes, not a
    bug — re-ran Python with it included and got an exact match) and once
    against a second, unrelated scenario ($250k home, 10% down, 7% rate, 5yr
    horizon) — both matched the JS to the cent.
  - **Full rebuild, not a patch.** The prior page was a React/Tailwind range-slider
    component with 5 inputs, fixed hidden assumptions (3% appreciation, 3% rent
    inflation, 6% return, 3%/7% transaction costs — none adjustable), no chart,
    1 H2, and 3 FAQs — the generic template-tier pattern this repo has been
    working through. Replaced the entire `<main>` with a hand-built vanilla-JS
    3-card-pattern page (`rvb-` prefix), keeping the protected shared
    style block and header/footer untouched. New calculator: 6 core inputs
    (home price, down %, rate, rent, years to compare, investment return) +
    an Advanced-assumptions toggle (loan term, property tax, insurance, PMI,
    maintenance, HOA, renters insurance, closing %, selling %, appreciation %,
    rent increase %) with 2026 US-average defaults; month-by-month simulation
    of both paths (standard amortization + PMI phase-out at 20% equity on the
    buy side, invest-the-monthly-difference compounding on the rent side);
    break-even year, monthly P&I, upfront cash needed, and both sides' net
    worth at the chosen horizon; a year-by-year net-worth line chart; a
    sensitivity table (break-even year and winner at 6 different investment
    return rates, current rate highlighted); a "5% rule" quick-reference
    card; PDF export (jsPDF lazy-loaded on click, per section 6 — confirmed
    zero bytes fetched before the button is clicked); a navy related-calculators
    sidebar (mortgage, loan, house-affordability, mortgage-payoff, down-payment,
    investment, compound-interest — all confirmed to actually exist before
    linking). 8 H2 sections (understanding / how-it-works-and-formula /
    input breakdown / real trade-offs / what-this-doesn't-cover / how-long-
    to-stay decision help / worked example) + 7 FAQs + table of contents.
  - **Fixed the existing breadcrumb/H1/title while rebuilding:** breadcrumb
    schema already correctly said category "Finance", fixed the category
    link to the `#fin` anchor convention and the crumb's schema name from
    "Rent Vs Buy" to "Rent vs. Buy Calculator" to match the page's own H1;
    added `font-bold` to the H1 classes (confirmed `fontWeight:700` via
    Playwright, per the section-5 known failure mode); rewrote title
    ("Rent vs. Buy Calculator — Find Your Break-Even Year") and meta
    description around the break-even/investment-return angle instead of
    the old generic `X Calculator | CalculatorBoss` pattern.
  - **What this page deliberately doesn't model, disclosed on-page:** the
    mortgage-interest tax deduction (most homeowners take the standard
    deduction post-2018, so it's worth $0 to them in practice — modeling it
    accurately would need itemization/filing-status data this calculator
    doesn't collect), rent control caps, mid-horizon refinancing, and
    state-specific transfer taxes. Called out explicitly in its own H2
    section and an FAQ rather than silently ignored.
  - Verified: FAQ schema vs. visible-content diff check (7/7 exact,
    per the section-3 recurring-failure-mode warning); zero console/page
    errors at 1280px and 390px mobile (no horizontal overflow); Advanced
    toggle, Clear-to-defaults, and live recalculation on every input all
    functional; PDF button confirmed lazy (no jsPDF request before click)
    and fails gracefully with a clear message (this sandbox can't make
    real outbound HTTPS calls from its browser at all — confirmed
    unrelated to this specific integration the same way as the leverage
    calculator's live-price feature — so this is the correct verification
    ceiling here; will work normally on the real production site).
  - **Same-day follow-up: design + SEO/GEO audit and fix pass** (ad-hoc user
    request, Jul 21, 2026, later same session). User reported "design
    structure" and "SEO" problems on the just-shipped page; found via a
    fresh Playwright viewport sweep (the original verification above only
    spot-checked 1280px/390px, which both happen to sit outside the broken
    range) that `.rvb-grid`'s three fixed-ish columns (380px / minmax(370px,1fr)
    / 300px) genuinely overflow the `max-w-5xl` content wrapper across
    **~861px-1220px** viewport width — a real, reproducible horizontal-scroll/
    squish bug (confirmed 0px→210px→0px overflow curve by sweeping viewport
    width in Playwright), not a false alarm. **Note for future sessions:**
    the identical grid pattern (same three column widths) is also used by
    `salary-calculator` and `sales-tax-calculator`, and measurement confirms
    they have the exact same overflow bug — this is a site-wide characteristic
    of the current 3-card grid convention, not unique to this page. Only
    this page was fixed this session (scope was this page specifically);
    the other two are a flagged follow-up, not yet done. Fix applied here:
    extended the single-column collapse breakpoint from `860px` to `1220px`
    (verified safe margin — real overflow stopped at 1200px measured, no
    overflow from 1221px up through 1920px with the original 3-column
    layout intact). Re-verified after the fix: 0px overflow at every
    tested width from 390px to 1920px (one negligible 4px blip at exactly
    1000px, well under any visible threshold), Calculate button and live
    recalculation still functional, zero new console errors.
  - **SEO gaps found and fixed:** `og:image`/`og:image:width/height`/
    `og:type` were completely missing from `<head>` (no image existed at
    `/og/rent-vs-buy-calculator.png` either) — generated a new 1200×630 OG
    image matching the site's established template (brand mark, category
    badge, H1, subhead, trust line) and added the full tag set. Separately,
    `twitter:title`/`twitter:description` were still the generic homepage
    copy ("CalculatorBoss — Free Online Calculators...") instead of mirroring
    this page's own title/description per section 3's checklist — fixed to
    match. `WebApplication` JSON-LD was missing the checklist's required
    one-line `description` field (confirmed by diffing against `ira-calculator`
    and `annuity-payout-calculator`'s already-correct schema shape) — added.
    Also fixed a stale `calculators-index.json` entry ("Rent Vs Buy
    Calculator" → "Rent vs. Buy Calculator", matching the page's actual H1
    and site capitalization convention — this feeds the header search
    modal) and a stale `sitemap.xml` `<lastmod>` still dated Jul 3 despite
    today's full rebuild. Re-ran the FAQ schema-vs-visible-content diff
    check as a regression guard — still 7/7 exact, untouched by this pass.
  - **GEO / AI-citation pass:** confirmed `robots.txt` (`Allow: /` for all
    user-agents) doesn't block AI crawlers (GPTBot, ClaudeBot, PerplexityBot,
    Google-Extended, etc.) — no change needed. `llms.txt` already listed
    this page but as a bare link with no descriptor, unlike most sibling
    entries — added a short descriptive suffix ("— Break-Even Year") to
    match convention and give AI-answer crawlers a clearer one-line summary
    without a full page fetch. Confirmed the page already had the stronger
    GEO signals (transparent formula section, FAQ phrased as literal
    search queries, a standalone quotable break-even definition, static
    server-rendered HTML with no JS-rendering barrier for crawlers) from
    the original build — this pass only added the missing metadata layer
    around content that was already sound.
  - **Same-day follow-up #2: real root cause of the "design structure"
    complaint** (user sent a screenshot with red guide-lines showing the
    whole calculator body sitting narrower/indented relative to the
    header). The overflow-breakpoint fix above was real but was NOT what
    the screenshot was showing — the actual cause was the page's content
    wrapper div right after `<main>`: it used `class="mx-auto max-w-5xl
    px-5 py-7 sm:py-9"` (Tailwind `max-w-5xl` = **1024px**), while every
    other already-rebuilt 3-card page (ira-calculator, annuity-payout-
    calculator, apr-calculator, time-zone-calculator, budget-calculator,
    bond-calculator, loan-calculator, salary-calculator, sales-tax-
    calculator — checked all of them) uses the exact same
    `class="px-4 sm:px-6 py-5 sm:py-6 mx-auto" style="max-width:1160px"`,
    matching this guide's own section-5 spec. Rent vs. Buy was the one
    page built against the wrong width, making its body ~136px narrower
    than the 1180px header — visually "indented." Fixed by matching the
    universal convention exactly. Re-verified in Playwright: header-wrap
    vs. content-wrapper edges now differ by a consistent 10px on each
    side (same small padding-convention gap every reference page has,
    not a bug), full-page screenshot confirmed visually centered/aligned
    at 1920px, FAQ schema diff still 7/7 exact, zero console errors.
    **Re-ran the overflow sweep after this change** (the wrapper-width
    fix changes the container size at every viewport, so the earlier
    breakpoint math needed re-checking, not just left alone): the danger
    zone shrank dramatically with the wider 1160px wrapper — clean at
    every width tested except a 54px overflow at exactly 950px, which
    traced (via a widest-element scan) to the **header's own search-bar
    trigger** (`.icon-btn.cf-search-trigger`, a fixed 296px), not this
    page's grid at all. Confirmed via the same test on salary-calculator
    and mortgage-calculator (164px overflow on both, actually worse) —
    this is a **pre-existing, site-wide header bug**, unrelated to this
    session's page-specific work and out of scope here (the guide's own
    rules require any shared-header change to be propagated + spot-
    checked across custom-built and template pages before pushing, which
    is a separate task). Flagging for a future session rather than
    touching the shared header inside a single-page fix.
  - **Same-day follow-up #3: byline + TOC didn't match the established
    pattern** (user sent two screenshots — mortgage-calculator's plain
    jump-link list vs. this page's boxed two-column card with an avatar
    circle — and asked for this page to match the former). Checked the
    actual byline/TOC CSS on every already-rebuilt page (mortgage-
    calculator, ira, apr, budget, time-zone, salary, sales-tax, annuity-
    payout, bond — 9+ pages) and every single one uses the identical
    `.{prefix}-byline{font-size:12.5px;color:var(--ink-faint);
    padding-bottom:16px;margin-bottom:16px;border-bottom:1px solid
    var(--border-fine)}` (plain text, no avatar) and `.{prefix}-toc
    {background:var(--surface-sunken);border-radius:10px;padding:16px
    20px;margin-bottom:28px}` with bare `<a>` links directly in the
    `<nav>` (no `<ul>`/`<li>`, no header label) — `--surface-sunken` is
    the same color as the page background, so it renders with no visible
    box border at all, just indented text, matching the screenshots
    exactly. Rent vs. Buy was built with a one-off avatar-circle byline
    (also inconsistently classed `rb-byline` instead of this page's own
    `rvb-` prefix) and a bordered white two-column TOC card with an "ON
    THIS PAGE" label — this was the one outlier across the whole site,
    not a case of an old page lagging behind a newer pattern. Replaced
    both to match the universal convention exactly (including the exact
    verbatim byline copy and "Jul 2026" abbreviation every other page
    uses instead of this page's custom wording). Verified: TOC links
    still scroll to the correct sections (all 8 checked programmatically),
    FAQ schema still 7/7 exact, zero console errors.

- **Leverage Calculator — round 3: live price feed** (ad-hoc user
  request, Jul 21, 2026, direct follow-up to the round-2 "one honest
  gap" note about competitors fetching live crypto prices): user said
  to add it and make the page as strong as possible.
  - **API selection, verified rather than assumed.** This repo's own
    hard-won-lessons section explicitly warns not to trust a live-data
    integration on curl/Node output alone, since a broken-CORS domain
    can silently fail in every real browser (the currency-calculator's
    original frankfurter.app incident). Followed that instruction:
    `curl -sI -H "Origin: https://calculatorboss.com"` against
    CoinGecko's public `/simple/price` endpoint confirmed
    `access-control-allow-origin: *`, and a direct multi-currency,
    multi-coin request (`vs_currencies=usd,gbp,cad,aud,eur`) confirmed
    one call returns every currency this page already supports, so
    switching the existing currency dropdown doesn't require a second
    request. Attempted the recommended in-browser Playwright fetch too;
    it failed with `ERR_CERT_AUTHORITY_INVALID` — then proved that's a
    sandbox-wide TLS interception issue, not a CoinGecko/CORS problem,
    by fetching `api.github.com` (unrelated, definitely-fine domain)
    from the same browser context and getting the identical failure.
    The curl-based CORS header is the valid signal here; the sandbox
    just can't make outbound HTTPS calls from its bundled Chromium at
    all, which won't apply on the real production site.
  - **Feature:** a coin selector (BTC, ETH, SOL, BNB, XRP, DOGE, ADA,
    TRX) plus a "Use live price" button in the Position Value tab's
    Advanced section. On click, fetches all 8 coins × 5 currencies in
    one request, fills the Entry Price field in whichever currency is
    currently selected, shows the 24h change (color-coded) and a
    timestamp, attributes the source ("via CoinGecko"), and immediately
    re-runs the liquidation-price calculation. Responses are cached for
    20 seconds so switching the coin dropdown re-displays instantly
    without a second network call, and switching currency then
    re-fetching correctly re-reads from the same cached payload.
    Manual entry remains the default and is untouched — this is a
    convenience layered on top, not a replacement.
  - **Error handling, tested rather than hoped for:** used Playwright's
    request-mocking to test both paths without depending on this
    sandbox's broken outbound HTTPS — (1) a mocked successful response
    (verified the field populates, currency-awareness works, the cache
    avoids a second call, and calc() + the liquidation estimate both
    re-run correctly) and (2) a mocked aborted/failed request (verified
    a clear inline message appears, the button re-enables, and the
    entry-price field remains fully manually editable — the page never
    breaks or gets stuck if the API is unreachable for any reason).
    8-second timeout via `AbortController` so a hung request can't leave
    the button stuck on "Fetching…" indefinitely.
  - **Caught and fixed a real mobile overflow bug during testing:** the
    coin-select + button row overflowed its own card by about 10px on a
    390px viewport (button text visibly cut off at the edge) — the
    combined natural widths of the two flex children didn't actually
    fit the container at that width. Fixed by stacking them vertically
    below 680px, matching how the page already handles other two-up
    rows on mobile; confirmed zero overflow afterward.
  - **FAQ + schema:** added a matching "Where does the live price come
    from?" Q&A to both the visible FAQPage accordion and the JSON-LD
    schema (attribution, coverage, and the "reference not a guaranteed
    execution price" caveat). Ran this repo's own mandated schema/
    visible-content diff check afterward and caught a real instance of
    the exact failure mode the guide warns about: the schema had typed
    "It's" with a straight apostrophe while the visible JS array had
    the curly one, from writing the two in separate passes. Fixed to
    match exactly; re-ran the diff — 15/15 questions and answers now
    byte-for-byte identical between schema and visible content.
  - Also updated the Advanced-section toggle label ("live price,
    liquidation estimate") so the new capability is discoverable before
    expanding it.
  - Verified: all 6 round-1 math checks still pass; full FAQ diff
    15/15 exact; zero console/page errors at 1280px and 390px.

- **Leverage Calculator — round 2: gradient/font/spacing parity + tab
  layout fix** (ad-hoc user request, Jul 21, 2026, immediately following
  the round-1 audit above): user pointed at two screenshots — this
  page's calculator card vs. Loan Calculator's — and asked for the
  background gradient gone, "wired" fonts replaced with something
  professional, spacing tightened, and the mode tabs moved from inside
  the form card to their own row above it, all to match Loan Calculator
  specifically. Also asked for another full math re-check and a
  competitive feature-parity check against calculator.net, Omni
  Calculator, and similar large sites.
  - **Background gradient — root-caused properly this time.** Round 1
    kept the standard site-wide 0.05-opacity gradient on the theory that
    every calculator page shares it. Direct pixel/computed-style
    comparison against `loan-calculator` proved that theory wrong:
    `getComputedStyle(document.body).backgroundImage` returns `"none"`
    on loan-calculator despite the identical gradient rule sitting in
    its stylesheet, because its actual `<body>` tag carries an inline
    `style="background:var(--bg)"` — the shorthand `background` property
    resets `background-image` to its initial value, silently cancelling
    the stylesheet's gradient. Confirmed this exact inline style is
    present verbatim on mortgage/bmi/savings/sales-tax/salary-calculator
    too (5/5 checked) — it's the real, consistent site convention, not
    the gradient rule itself. Added the identical inline style to this
    page's `<body>` tag; `backgroundImage` now correctly resolves to
    `"none"` here too.
  - **Fonts — found a real, previously-unnoticed typography mismatch.**
    Systematically compared computed `font-family` across every text
    role on both pages rather than eyeballing it: loan-calculator's H1,
    tab labels, and all numeric/result values compute to `Inter,
    ui-sans-serif, system-ui, sans-serif` (loaded via the shared Tailwind
    bundle every page already includes, just never applied outside
    Tailwind's own utility classes), while this page's equivalents were
    IBM Plex Sans (H1) and IBM Plex Mono (tab labels, stat values,
    milestone numbers, table cells) — a monospace, code-editor-style
    font sitting under every number on the page, which is almost
    certainly what read as "wired." Repointed `--f-head` and `--f-mono`
    to the same Inter stack, verified via computed style afterward that
    H1/tabs/stat-rows/milestones/table-cells all now match
    loan-calculator exactly.
  - **Spacing — removed the GEO callout added in round 1** (it was
    contributing to the extra height and, via the `.mono` class, part of
    the font complaint too — moot now that `--f-mono` itself changed,
    but removed anyway since loan-calculator's hero has no equivalent
    element) **and found the real structural cause**: this page stacks
    independent section-level paddings (`.crumb`, `.hero`,
    `.calc-section` each contributing their own top/bottom padding) where
    loan-calculator uses one flat outer wrapper with no such stacking.
    Measured the actual gap (subhead-bottom to bar-top: 40px here vs.
    24px there) and trimmed `.crumb`, `.hero`, and `.calc-section`
    padding to bring it to 16px — closer to the reference than not
    touching it, without a full structural rewrite. H1 top position also
    moved from 27px-lower than reference to within 7px of it.
  - **Tabs moved to their own row, matching Loan Calculator's grid
    exactly.** Read loan-calculator's actual grid definition rather than
    guessing: `grid-template-areas:"bar bar ." "tabs tabs ." "form
    result sidebar"` with `.ln-tabs{grid-area:tabs}` as an independent
    row spanning the form+result columns (not the sidebar column, and
    not nested inside any card). This page's tabs previously lived
    inside `.calc-area-form` as the first thing in that card. Added a
    matching `"tabs tabs ."` grid row, moved the tab markup out to its
    own `.calc-area-tabs` sibling in the HTML, and restyled the buttons
    off the old small-pill/mono-font/horizontal-scroll treatment onto
    loan-calculator's actual button convention (larger, `border-radius:
    10px`, flex-wrap instead of scroll). Updated the ≤980px mobile grid
    stack to include the new tabs row too.
  - **Math re-verified after every structural change** — all 6
    Playwright-driven checks from round 1 (worked example, short-
    direction sign flip, required-margin tab, required-leverage tab,
    the "already at spot" edge case, the 125x cap) re-run and still
    passing after the font/spacing/gradient/grid changes; nothing here
    touched calculation logic.
  - **Competitive feature-parity check, done honestly rather than just
    asserted:** searched specifically for what calculator.net and Omni
    Calculator offer here. Calculator.net's own financial-calculator
    index (Mortgage, Loan, Auto Loan, Retirement, Investment, 401k,
    etc.) has no leverage or trading-margin calculator at all — nothing
    to match. Omni Calculator does have a "Financial Leverage Ratio"
    and a "Degree of Operating Leverage" calculator, but both compute a
    *corporate* leverage concept (debt-to-equity / EBIT sensitivity for
    analyzing a company's balance sheet) — a genuinely different tool
    for a different audience than a trader sizing a margin position, not
    a feature gap on this page. Checked against the specialized
    trading-tool sites instead (gaspntrader, cryptocalk.com,
    leverage.trading, pineify.app, flicker.finance — same set researched
    in round 1): this page's existing feature set (solve for any of
    3 variables, long/short, multi-currency, liquidation estimate,
    leverage-vs-spot chart, scenario table, leverage-comparison table,
    saved setups, PDF/CSV/share export) already matches or exceeds most
    of them. One genuine, disclosed gap noted for a future session if
    wanted: a live/real-time price feed for the entry-price field (a
    couple of competitors fetch live crypto prices) — not added now
    since it wasn't asked for this round and introduces an external API
    dependency that would need its own CORS/reliability verification
    pass per this repo's own hard-won-lessons section before shipping.
  - Verified at 1280px and 390px after all changes; zero console/page
    errors.

- **Leverage Calculator — full audit + rebuild to current design system**
  (ad-hoc user request, Jul 21, 2026, framed as "act as an expert Leverage
  Calculator auditor"): user asked for real verification of the math, a
  visual migration off the page's old crypto-tier theme onto the same
  look as mortgage/bmi/savings-calculator, removal of the yellow/gold
  accent in favor of the site's navy `#1E3A5F` bar color, Calculate/Clear
  buttons matching the site convention, and better title/meta for CTR —
  plus four specific issues shown via screenshot. Scope was this one page
  only (explicitly, not site-wide).
  - **Math verification (the actual audit):** hand-checked every formula
    against the visible worked example before touching any code —
    Position Value = Margin × Leverage, ROI% = Price Move% × Leverage,
    and the isolated-margin liquidation estimate
    `Entry × (1 − 1/Leverage + MMR)` (long) / mirrored for short — all
    confirmed correct and internally consistent (the page's own "$67,500
    entry, 10x, 0.5% MMR → ~$61,087.50, 9.5% away, -95% ROI" example
    reproduces exactly). Then re-verified live in Playwright across all
    3 tabs plus edge cases (short-direction sign flip, the "your margin
    already covers this, no leverage needed" case, and the 125x realistic
    cap) — 6/6 automated checks passed against independently computed
    expected values. The math was never the problem; everything below
    was UI/UX and content.
  - **Found and fixed 3 real bugs during verification, not just the ones
    in the screenshots:**
    - The mobile Calculate button was hidden entirely below 680px
      (`.btn-accent{display:none}` inside a mobile media query) — no
      plausible reason for this, and it directly contradicted matching
      the site's Calculate/Clear convention. Removed; Calculate now
      shows on every breakpoint like every other page.
    - Three "Hypothetical price move" hint labels had a literal
      `\u2014` sitting in raw HTML text (not inside a JS string, where
      it would have been interpreted) — rendered on the live page as
      the literal 6 characters `\u2014` instead of an em dash. Fixed to
      an actual "—" in all three tabs.
    - A confirmed-dead "P&L bar" element inside the result card
      (`#plBarWrap`/`#plBarFill`/`#plBarFill2`, plus a `setPlBar()`
      function) was called with `(0,0)` at all 4 call sites, site-wide,
      always — meaning it never rendered anything in any state. Removed
      the markup, the function, and all 4 calls.
  - **Image 2 (empty white bar):** root-caused, not guessed at — the
    "Price-move scenario table" was wrapped in `.table-scroll-y`, a
    collapse/expand pattern (`max-height:0` → `.open{max-height:480px}`)
    with a matching but entirely unused `.show-more` button style. No
    JS anywhere on the page ever added `.open` to it — confirmed via
    `grep`, zero references outside the CSS itself. The table's data was
    always fully correct (verified 10 real rows in the DOM via
    Playwright) and was just permanently collapsed to zero height by
    dead CSS. Fixed by removing the collapse system entirely, matching
    how the page's other data table already displays (fully expanded,
    no toggle) — per the user's own framing, the data existed, so it
    now shows.
  - **Image 3 (chart/legend overlap):** root-caused via computed-style
    inspection rather than CSS guessing — `.chart-box` had a fixed
    `height:280px`, but the SVG inside it only had `viewBox="0 0 900
    280"` with no matching CSS height, so the browser auto-sized it to
    900:280 aspect-ratio-correct height at its actual rendered width
    (~1078px wide in practice → ~335px tall), and `overflow:visible` let
    that extra ~55px spill downward directly into the legend below.
    Fixed by making the container height auto (no more fixed/actual
    mismatch) and the SVG `display:block;width:100%;height:auto`, then
    re-verified zero overlap (a positive 13–14px gap instead) at every
    leverage from 2x to 100x.
    - While in there, also fixed something the chart was quietly getting
      wrong: the leveraged-return line used a fixed `yMin/yMax:±150`
      clamp, so it flattened at an arbitrary point tied to that constant
      rather than to real liquidation — meaning the "cliff" appeared in
      a different, disconnected place than the page's own "-100% ROI
      (margin wiped)" annotation, and gains got an equally arbitrary
      artificial ceiling with no real-world meaning (leveraged upside
      isn't capped, only the downside is, at liquidation). Rebuilt the
      chart's Y-axis to scale to the actual leverage
      (`yMax = xMax × leverage`) and explicitly floored the loss line at
      exactly -100% ROI, so the flat cutoff now always lines up with the
      dashed annotation and the chart is mathematically honest at any
      leverage (spot-checked 2x/10x/25x/50x/100x).
  - **Image 4 (voting widget):** removed entirely — CSS, HTML, and its
    JS click handlers — and fixed the one sentence in the review box that
    referenced "the feedback widget below."
  - **Image 5 (brand color) + general re-theme:** the page carried a
    second, entirely separate `:root` block — dark-theme variable values
    immediately overridden by a duplicate "forced light theme" block
    directly beneath it (dead weight; no dark-mode toggle exists anywhere
    on the page, confirmed via `grep`), including its own slightly-off
    variant of the site's gradient (`0.08` opacity vs. the standard
    `0.05`) and an orange/amber `--cx` accent (`#B0790F`) used for the
    chart line, the "Key takeaways" card border, and the Calculate
    button's yellow gradient — sampled the color the user marked as
    "our brand color" directly from the screenshot pixel (`#1E3A5F`,
    exact) and confirmed it's the same navy already used elsewhere on
    this exact page for the calculator-bar and active-tab state.
    Replaced the whole second `:root` with a minimal alias block pointing
    the handful of genuinely-needed variable names (`--panel`, `--text`,
    `--text-soft`, etc.) at the site's real tokens, changed `--cx` to the
    navy, and deleted the duplicate gradient/body rule outright — the
    page now inherits the one standard site-wide gradient (matching
    mortgage/bmi/savings-calculator) with no separate treatment, exactly
    as requested. Calculate button rebuilt to the exact convention used
    on bmi/sales-tax/salary-calculator (`#16A34A` solid, not flex-stretched
    to fill the row); Clear button matched to the same reference.
  - **SEO title/meta, informed by the user's own GSC screenshot:** the
    dominant query for this page is the bare "leverage calculator" (42
    impressions) but only 1 click — a CTR problem, not a visibility
    problem. Long-tail rows in the same screenshot ("leverage trade
    calculator," "leverage trading calculator," "leverage profit
    calculator," plus international "leverage rechner"/"leverage
    berekenen" signal) confirmed real demand beyond the crypto-specific
    framing the old title led with ("Crypto Leverage Calculator...").
    Cross-checked against 8+ competitor pages (cryptocalk.com,
    gaspntrader.com, stockcalculators.org, leverage.trading,
    flicker.finance, pineify.app, miniwebtool.com, investknow.io) — most
    ranking pages for the bare term aren't crypto-exclusive. Rewrote the
    title to lead with the proven head term and a concrete 3-output
    benefit hook ("Leverage Calculator — Position Size, Margin &
    Liquidation Price"), meta description to add the free/no-signup
    friction-removal cue and broaden to "crypto, forex or futures" ,
    added a `meta keywords` tag (previously missing on this page,
    present on every reference page) populated with the actual
    researched long-tail terms, and mirrored all of it to og:/twitter:
    tags. H1, URL, and category placement left untouched, per the
    guide's own "blend, don't force a rename" rule.
  - **GEO / AI-citation:** added a one-line "Quick answer: Position Value
    = Margin × Leverage, and ROI on Margin = Price Move % × Leverage"
    callout directly under the hero subhead, matching the direct-answer
    style the strongest competitor pages already lead with — the page
    already had strong foundations here (FAQPage with 14 Qs, HowTo,
    WebApplication, BreadcrumbList schema all present and left as-is).
  - **Verification before shipping:** Playwright across 1280px, 1024px,
    and 390px mobile; zero console/page errors (the only errors seen
    were the sandbox's pre-existing Google Fonts/GTM cert issue,
    unrelated); math re-verified after every structural change; menu and
    search re-confirmed still functional (header wasn't touched this
    session); full before/after screenshots at every fixed section.
  - Net diff: -63 lines (dead-code removal outweighed the additions).
    Touched only `leverage-calculator/index.html`, per explicit scope.

- **Site-wide brand name rename: "Calculator Boss" → "CalculatorBoss"**
  (ad-hoc user request, Jul 21, 2026): user asked for the spaced brand
  name to become one word everywhere, explicitly excluding any text
  containing `.com` (i.e. domain/URL mentions stay untouched).
  - Surveyed the whole repo first rather than guessing: found exactly
    1,960 case-sensitive instances of "Calculator Boss" across every
    `.html`/`.txt`/`.json`/`.xml`/`.md` file, all in the identical
    casing (no stray "calculator boss" or "CALCULATOR BOSS" variants to
    worry about) — plus 23 instances written as "Calculator Boss.com"
    (a PDF-export "Generated by ~" footer line, inconsistently already
    "CalculatorBoss.com" with no space on some pages, still spaced on
    others). Confirmed separately that every lowercase `calculatorboss`
    occurrence (1,318 of them) is exclusively part of the
    `calculatorboss.com` domain in URLs/canonical/schema/sitemap/robots
    — never a standalone brand-name mention — so there was nothing to
    change there per the user's "leave .com text alone" rule.
  - Ran a scripted regex replace (`Calculator Boss(?!\.com)` →
    `CalculatorBoss`) across every non-binary file in the repo: 1,943
    replacements in 217 files. The 23 "~Boss.com" PDF-footer instances
    were correctly left untouched (deliberately not "fixed" to match,
    since the user's rule was explicit and this is now a pre-existing,
    out-of-scope minor inconsistency, not something this request asked
    for). Also updated `DESIGN_AND_SEO_GUIDE.md` and `PROGRESS.md`'s own
    references to the brand name for consistency, since both are the
    persistent reference docs for future sessions.
  - **Verified, not assumed:** re-scanned afterward to confirm exactly
    zero bare "Calculator Boss" instances remain outside the 23
    `.com`-attached ones; confirmed all `calculatorboss.com` domain/URL
    references (canonical tags, JSON-LD `url` fields, sitemap.xml,
    robots.txt) are byte-for-byte unchanged; parsed a sample of pages'
    JSON-LD blocks to confirm the text-only substitution didn't corrupt
    any JSON; re-ran the full 211-page Playwright mobile-menu regression
    suite (still 211/211 passing) since this touched every page's header
    text; re-confirmed search still opens and returns results. Desktop
    screenshot confirms `<title>`, header logo text, and footer copyright
    line all correctly read "CalculatorBoss" with layout otherwise
    unchanged.

- **Site-wide mobile menu fix + search-modal gap fix** (ad-hoc user request,
  Jul 21, 2026, first mobile-optimization pass): user reported the mobile
  hamburger button (top-right, visible ≤680px) did nothing when tapped, and
  asked search to be functional everywhere too, explicitly asking to keep
  the existing header design/markup unchanged and only fix behavior.
  - **Root cause (menu): the hamburger button had zero JS wiring anywhere
    on the site.** `.menu-btn` existed purely as CSS-toggled markup — no
    click handler, no drawer/panel, no nav-open state existed on any of the
    ~212 pages (confirmed via `grep` site-wide before touching anything).
    On mobile, `.nav-links` is `display:none` below 900px with the button
    as the only way to reach Home/Calculators/Categories/About, so this
    meant mobile visitors had **zero way to navigate the site header at
    all** below that breakpoint.
  - **Fix:** added a small dropdown nav panel + backdrop overlay, entirely
    new markup (no existing element renamed/removed/restyled — confirmed
    via diff that desktop is byte-identical to before), inserted inside the
    canonical `<header>` in `index.html` so it propagates automatically via
    the existing `scripts/sync_header_footer.py` (same sync mechanism this
    repo already uses for header/footer, no new tooling introduced). Icon
    swaps hamburger↔X on toggle; closes on backdrop click, Escape, nav-link
    click, or resize past 900px; `aria-expanded`/`aria-controls` set.
  - **Bug caught during Playwright verification, not left for the user to
    find:** first implementation used `top:70px;bottom:0` for the overlay,
    which computed to a **0px-tall box** — `header` has
    `backdrop-filter:blur(16px)`, and per the CSS spec any ancestor with
    `filter`/`backdrop-filter`/`transform` becomes the *containing block*
    for `position:fixed` descendants, so the overlay's `bottom:0` was
    resolving against header's own 70px box, not the viewport. Confirmed
    via an isolated minimal-HTML repro before/after to pin the exact cause
    rather than guessing. Fixed by switching to an explicit
    `height:calc(100vh - 70px)` (`100dvh` fallback), which is viewport-unit
    based and unaffected by the containing-block substitution.
  - **Root cause (search): 9 crypto/trading-tier pages** (leverage,
    staking-reward, liquidation-price, crypto-profit-loss, risk-reward,
    mining-profit, dca, crypto-position-size, crypto-tax calculators) were
    **entirely missing** the `#cfSearchOverlay` modal + its script (found
    via a site-wide `grep` sweep) — the search icon button rendered but
    had nothing to open, since that block lives after `</footer>` and
    isn't covered by the header/footer sync. Every other page already had
    a working search (confirmed independently in Playwright: opens on
    click, loads `/calculators-index.json`, filters correctly). Fixed by
    inserting the identical, byte-for-byte modal block (style + overlay +
    script) used on every other page into these 9 files, right before
    `</body>`, with the placeholder count normalized to the real total
    (204, per `calculators-index.json`, vs. the stale count some pages
    already carry as pre-existing drift — left that pre-existing minor
    inconsistency alone since it's cosmetic and out of scope for this fix).
  - **Verification:** Chromium/Playwright at a 390×844 mobile viewport
    against a local static server. Menu tested (open/close via button,
    backdrop click, Escape, real navigation) on all **211/211** pages
    site-wide — zero failures, zero duplicate IDs, zero console/page
    errors attributable to this change (the only console errors seen were
    pre-existing `net::ERR_CERT_AUTHORITY_INVALID` on Google Fonts/GTM
    calls, an artifact of this sandbox's network, unrelated). Search
    re-verified working (opens, loads index, filters, keyboard nav) on the
    9 previously-broken pages plus a spot-check of already-working pages.
    Desktop (1440px) screenshotted before/after and confirmed pixel-
    identical — menu button hidden, `.nav-links` visible, no layout shift.
  - Files touched: `index.html` (canonical header edit) +
    `scripts/sync_header_footer.py` run to propagate to 210 other pages +
    manual insertion of the search block into the 9 crypto-tier pages.
    Two commits: one for the menu fix (header sync, all pages), one for
    the search-modal gap fix (9 pages) — kept separate since they're two
    distinct root causes even though delivered in the same session.
  - **Not done (flagged, not fixed):** discovered a separate, smaller,
    pre-existing responsive gap while testing — `.nav-links` hides at
    ≤900px but `.menu-btn` only appears at ≤680px, so a window/tablet in
    the 681–900px range currently shows neither the nav links nor the
    menu button. Didn't touch it this session: that CSS lives in the
    protected shared `<style>` block in `<head>` (not covered by the
    header/footer sync script), so fixing it site-wide means hand-editing
    the protected block across ~212 files — real phones are almost always
    under 680px so this doesn't affect the reported bug, and the guide's
    own rule is to propagate + spot-check protected-block changes
    carefully rather than do it as a drive-by. Flagging for a deliberate
    follow-up pass rather than bundling it into this fix.

- **Cross-calculator gap-closing pass** (ad-hoc user request, Jul 20, 2026,
  directly following the "is everything 100% ok?" exchange): user pushed
  back on the honest "here's what's disclosed as not covered" answer with
  a fair challenge — if a gap stops a visitor from actually solving their
  problem, disclosing it isn't enough, it should be closed. Went back
  through both pages' own disclosed limitations and closed the ones that
  were genuinely fixable in scope, rather than leaving them as permanent
  disclaimers.
  - **Cross-link fix**: found Land Transfer Tax Calculator already linked
    to Canadian Mortgage Calculator in its sidebar, but not the reverse —
    added it, positioned first since it's the most directly relevant
    companion tool.
  - **Canadian Mortgage Calculator — Rate Type (Fixed/Variable) +
    Compounding selector**: the page previously assumed semi-annual
    compounding unconditionally, correct for fixed-rate (legally mandated,
    Interest Act) but only sometimes correct for variable-rate, which
    genuinely isn't standardized. Research turned up an authoritative
    single data point worth citing directly — the Government of Canada's
    own FCAC template "Credit Agreement for a Variable Interest Loan"
    example states its own variable-rate product is "compounded twice per
    year but charged monthly," i.e. semi-annual, same as fixed — but this
    doesn't generalize to every lender, several of which compound monthly
    instead. Rather than guessing one convention and risking being wrong
    for an unknown fraction of variable-rate users, added a rate-type
    selector that locks Fixed to semi-annual (no ambiguity, no choice
    needed) and, for Variable, exposes an explicit Semi-Annual/Monthly
    compounding choice so the user can match their own contract instead of
    the tool guessing for them.
    - Generalized the core rate-conversion function to accept any
      compounding frequency rather than duplicating it; verified in Node
      that the general form is bit-for-bit identical to the original
      semi-annual-only version at compoundingPeriodsPerYear=2 across
      multiple rates and payment frequencies before wiring it in anywhere.
    - Caught and fixed a real consistency bug before it shipped: the Down
      Payment Scenarios table (added in an earlier follow-up this session)
      computed its own rate conversion independently and would have kept
      showing semi-annual-based numbers even when Variable+Monthly was
      selected, silently mismatching the highlighted "current" row against
      the main displayed payment. Passed the compounding choice through to
      that function too and verified the two now agree exactly at
      Variable+Monthly (both show $2,966.42 for the current 10% tier where
      they'd previously have shown two different numbers).
    - Fixed the PDF export's schedule regeneration, which also called the
      semi-annual-only conversion directly and would have quietly exported
      a fixed-rate schedule for a variable-rate calculation.
    - Verified: Fixed unchanged ($2,955.79); Variable+Semi-Annual identical
      to Fixed (correct, since it's the same math); Variable+Monthly
      produces a small, correctly-higher payment ($2,966.42); switching
      back to Fixed restores the original exactly; Stress Test tab (Tab 2)
      unaffected; zero duplicate IDs; PDF export verified with
      Variable+Monthly active; zero console errors.
  - **Land Transfer Tax Calculator — Closing Costs estimate**: added an
    optional "Include legal/notary fees & title insurance" section with
    editable defaults ($1,500 / $350), researched against 8+ sources
    clustering around $900–$3,000 for legal/notarial fees and a very
    consistent $250–$500 for title insurance. Labeled correctly per
    province ("Notary fees" for Quebec, "Legal fees" elsewhere, switching
    automatically). Explicitly framed as rough national averages the user
    should override with a real quote, not a precise number -- avoiding
    the false-precision trap of presenting a guess as a fact.
  - **Land Transfer Tax Calculator — Quebec first-time buyer tax credit**:
    surfaces the $5,875 credit (already researched earlier this session
    but never displayed) as an explicit informational line when Quebec +
    first-time buyer is selected, correctly described as a separate
    refundable credit claimed on the tax return rather than subtracted
    from the welcome tax itself, since it doesn't work as a point-of-sale
    exemption the way Ontario's or BC's rebates do.
  - Fixed both pages' "what this doesn't cover" paragraphs, which
    described these exact features as absent -- both were the actual
    limitations these additions closed, so leaving the old wording would
    have been actively wrong now rather than just outdated.
  - Full regression after all changes: all 10 provinces' previously-
    verified LTT values unchanged; closing-costs math exact at both
    default and adjusted values; Quebec credit note appears/disappears
    correctly with the first-time-buyer checkbox; both pages' FAQ schemas
    re-confirmed matching; zero duplicate IDs on either page; all links
    (including the new cross-links, checked both directions) resolve;
    both PDF exports verified with the new features active; zero console
    errors across both pages.

- **Land Transfer Tax Calculator** (ad-hoc user request, Jul 20, 2026,
  following up directly on the Canadian Mortgage Calculator's "what this
  doesn't cover" disclosure and this session's competitive research, which
  had already surfaced land transfer tax repeatedly as a real, distinct
  gap): built as a genuinely new, separate page rather than folding it
  into the mortgage calculator, and placed immediately after Canadian
  Mortgage Calculator in All Calculators' Finance section per explicit
  request (breaking strict alphabetical order intentionally, since
  they're companion Canada-specific tools).
  - **Scope: all 10 provinces**, each researched and verified
    independently rather than assumed from a single source:
    - **Ontario**: 5-bracket marginal LTT (0.5%-2.5%), verified against
      3 independent worked examples ($300k/$750k/$800k, all exact
      matches). Toronto's municipal LTT mirrors the same brackets up to
      $3M (April 2026 luxury tiers above that noted but not modeled in
      full, given the smaller affected population); combined Toronto+ON
      on $700k matched an independent source's $20,950 figure exactly.
      First-time buyer rebates (ON $4,000 cap, Toronto $4,475 cap,
      $8,475 combined) verified via the well-documented $368k full-
      coverage threshold.
    - **British Columbia**: 4-bracket PTT (1%-5%, with the 5% top tier
      confirmed as a residential-specific surcharge via a more detailed
      source after an initial simpler source gave a different, less
      precise structure), verified against an independent $1M/$18,000
      example. Two separate, non-stacking exemptions modeled with their
      exact linear phase-out math -- First-Time Buyer ($500k full,
      $8,000 flat to $835k, phase-out to $860k) and Newly Built Home
      ($1.1M full, phase-out to $1.15M) -- verified in Node at multiple
      points including the phase-out midpoints (e.g. $847,500 correctly
      returns exactly half the $8,000 exemption).
    - **Quebec**: standard 3-bracket "welcome tax" plus Montreal's 2
      additional tiers, calculated correctly (confirmed via independent
      manual verification matching the live tool to the penny at
      $700k/Montreal: $9,471) -- Montreal's own official example gave a
      slightly different $9,349 for the same price point, attributed to
      year-to-year threshold indexation and disclosed as such rather
      than silently treated as a match. The new 2026 refundable tax
      credit (up to $5,875) and Montreal's own rebate program are
      surfaced as informational notes rather than subtracted directly,
      since both work through different mechanisms (tax filing / separate
      program) than a point-of-sale exemption this calculator can model.
    - **Manitoba**: 5-bracket LTT (0%-2%) + flat $70 registration fee, no
      first-time buyer rebate -- verified exactly ($300k: tax $3,650 +
      fee $70 = $3,720).
    - **Alberta & Saskatchewan**: correctly modeled as having NO land
      transfer tax (registration fees only), a distinction the page makes
      explicit in its labeling rather than implying a tax exists.
      Alberta's sliding-scale title + mortgage registration fees verified
      exactly ($500k property + $400k mortgage = $550+$450=$1,000);
      Saskatchewan's 0.4%-above-$6,300 fee verified exactly ($300k=$1,200).
    - **Nova Scotia**: municipal-set Deed Transfer Tax, defaulted to
      Halifax's 1.5% (the largest market, confirmed directly against
      Halifax's own official page) with an editable rate field and
      explicit disclosure that other municipalities set their own rate.
    - **New Brunswick & PEI**: flat 1%, with PEI's full exemption for
      first-time buyers under $200,000 correctly modeled (verified at
      $150k=exempt vs $250k=$2,500, the boundary behaving correctly).
    - **Newfoundland & Labrador**: correctly modeled as having no real
      transfer tax, just an approximated modest registration fee,
      explicitly labeled as an approximation rather than an exact figure.
  - Every province's core formula was verified in Node against an
    independent published worked example BEFORE being wired into the
    page, then re-verified live via Playwright after assembly -- the same
    two-pass discipline used throughout this session.
  - Conditional UI: only the fields relevant to the selected province
    show (Toronto checkbox for ON, newly-built checkbox for BC, Montreal
    checkbox for QC, editable rate for NS, mortgage amount for AB) --
    verified explicitly that switching provinces correctly shows/hides
    each field and that the first-time-buyer note itself hides for
    provinces where it does nothing (avoiding implying false hope).
  - FAQ schema-vs-visible-text check caught the em-dash mismatch pattern
    again (4 of 6 answers on the first pass, then one more hidden
    instance within an already-partially-fixed answer) -- all 5 total
    instances fixed and reconfirmed clean before assembly, consistent
    with every other build this session.
  - Full regression: all 10 provinces' default and edge-case
    calculations verified against independent Node math; province-switch
    conditional field visibility verified for ON/BC/QC/NS/AB and for the
    NL case (nothing relevant shown); zero duplicate IDs; all 23 internal
    links + anchors resolve; PDF export verified; mobile layout checked;
    zero console errors throughout. New OG image (navy theme, matching
    the site convention from the start this time -- no country-color
    detour needed). Added to all-calculators/index.html (Finance count
    77→78) and calculators-index.json, both placed immediately after
    Canadian Mortgage Calculator per explicit request.
  **Same-day follow-up** (user directly questioned whether the page was
  a real, complete tool or just a thin demo, pointedly noting how few
  input fields were visible): checked the live default view honestly
  rather than just reassuring -- on Ontario/default, the form really did
  show only province + price + 2 checkboxes, which is legitimately
  sparse compared to every other calculator built this session. Rather
  than defending the sparseness as "correctly scoped for the domain"
  without evidence, re-examined the page's own "what this doesn't cover"
  disclosure and found a genuine, substantial gap already flagged there
  but never built: foreign buyer / non-resident surcharges, which are
  large enough (20-25%) to be the single biggest number on the page for
  an affected buyer, not a minor edge case.
  - Re-verified current rates before implementing, given how much these
    percentages matter: Ontario's Non-Resident Speculation Tax, 25%
    province-wide (confirmed directly against the Government of
    Ontario's own page); a previously-unknown-to-this-build detail
    surfaced in the same research pass -- Toronto itself charges a
    *separate* 10% Municipal NRST on foreign buyers (effective Jan 1,
    2025), on top of the provincial 25%, for a combined 35% in Toronto
    specifically; BC's 20% Additional Property Transfer Tax, confirmed
    as regionally restricted (Metro Vancouver, the Capital Regional
    District, and a few other designated areas) rather than province-
    wide, a distinction the UI now discloses explicitly rather than
    over-applying it; Nova Scotia's 10% non-resident surtax (increased
    from 5% in April 2025). Also surfaced and disclosed the federal
    Prohibition on the Purchase of Residential Property by Non-Canadians
    Act, which bans most non-Canadians from buying in major urban areas
    until January 1, 2027 regardless of what any provincial tax
    calculates -- important context a purely-provincial-tax calculator
    would otherwise miss entirely.
  - Verified all figures in Node against independent published examples
    before wiring up (\$1M ON NRST = \$250,000; \$700k Toronto-combined
    foreign buyer surcharge = \$245,000; BC/NS equivalents) -- all exact
    matches -- then confirmed the live page matches exactly, including
    the combined ON+Toronto+foreign-buyer case (\$265,950 on \$700k).
  - Added an explicit "Foreign buyer / non-resident" checkbox with the
    rate and regional/federal-ban caveats stated directly in its own
    subnote (not just buried in the article), so a user encounters the
    limitation at the point of decision rather than only in a footnote.
    For the 7 provinces with no currently-known equivalent surcharge,
    added a single centralized check (rather than duplicating the same
    conditional 7 times) that surfaces an explicit "no known surcharge"
    note when checked, so the box silently doing nothing doesn't read as
    a bug.
  - Fixed the "what this doesn't cover" paragraph, which had described
    this exact feature as *not* covered -- now accurately describes what
    is modeled and what its real limits are (BC's regional restriction,
    the federal ban's practical override of all of this for many buyers).
  - Full regression: default and all previously-verified per-province
    values unchanged; new foreign-buyer calculations verified exactly
    for ON (plain and Toronto-combined), BC, and NS; the no-surcharge
    note verified showing correctly for Manitoba without changing the
    total; FAQ schema re-confirmed still matching (unaffected by this
    change, but checked rather than assumed); zero duplicate IDs; all
    23 links/anchors resolve; PDF export (now including foreign-buyer
    line items) verified; zero console errors.

  - Confirmed the Next.js RSC payload files present in every previously-
    rebuilt page's directory (__next.*.txt) are stale artifacts from the
    original build, already mismatched with hand-edited content on every
    page touched this session, and evidently non-critical for the live
    site (every rebuild has worked correctly in production despite this)
    -- created only index.html for this brand-new page rather than
    attempting to regenerate them.

- **Canadian Mortgage Calculator** (ad-hoc user request, Jul 20, 2026,
  reference: calculator.net/canadian-mortgage-calculator.html as first
  priority, cross-checked against Ratehub.ca, WOWA.ca, the official CMHC
  and Canada.ca/FCAC calculators, and OSFI directly): rebuilt from the
  434-line static template into a 2-tab tool covering the genuine
  regulatory/mathematical differences between Canadian and US mortgages,
  not a relabeled US calculator.
  - **Core formula verified independently, twice, to the penny**: the
    semi-annual-compounding-to-monthly-rate conversion (nominal/2, square
    it, then take the 12th root) was cross-checked against two unrelated
    published worked examples (a York University finance course's 6%
    example: predicted monthly rate 0.493862%, matched to 6 decimal
    places; a mortgage-education site's $500,000-at-5%-first-month-
    interest example: predicted $2,061.96, matched exactly). A third
    source (mortgagecalculator.org) gave a conflicting example, but its
    own numbers were internally inconsistent ($400k home - $320k loan
    claimed as a "$20,000" down payment, when it's actually $80,000) --
    disregarded as unreliable rather than treated as a formula error.
  - **CMHC insurance**: down payment tiers (5% under $500k, 5%+10% up to
    $1.5M, 20% at $1.5M+) and premium tiers (4.00%/3.10%/2.80% for 5%/10%/
    15% down) cross-verified against 8+ independent sources including
    WOWA.ca's own $19,000-premium worked example (exact match), plus the
    Dec-2024 federal reform details (30-year insured amortization for
    first-time buyers/new builds, +0.20% surcharge; $1.5M insured-price
    ceiling, up from $1M).
  - **Payment frequency**: all 6 standard Canadian schedules (monthly,
    semi-monthly, bi-weekly, accelerated bi-weekly, weekly, accelerated
    weekly). The two "accelerated" modes needed a genuinely different
    calculation (monthly-payment/2 or /4, not a fresh annuity formula at
    26 or 52 periods) plus a period-by-period acceleration simulation to
    find the new, shorter actual payoff time -- verified against a third
    independent published example (efunda.com's $200k/7.5%/15yr case:
    regular bi-weekly $848.30 and accelerated bi-weekly $920.51, both
    matched exactly), then confirmed internally consistent: accelerated
    bi-weekly and accelerated weekly both represent the same "13 monthly-
    equivalent payments/year" effect and, as expected, produced the same
    ~21.8-year payoff time on the live page independently.
  - **Stress Test Affordability tab**: the mortgage qualifying rate
    (greater of contract rate + 2%, or a 5.25% floor) confirmed directly
    against the OSFI regulator's own page plus 8 other sources; GDS/TDS
    debt-service ratios (39%/44% limits, condo fees counted at 50%)
    reverse-solved into a max mortgage amount and max home price, with the
    binding constraint (GDS or TDS) reported explicitly. This is the
    single feature that most differentiates this build from every
    "calculator.net-tier" competitor checked, none of which combine a
    payment calculator with a stress-test affordability check in one page.
  - Caught a real self-inflicted issue during testing: the page's own
    default down payment ($30,000 on a $600,000 home) was actually *below*
    Canada's legal minimum ($35,000) for that price, so the auto-adjust-
    to-minimum logic correctly fired but produced a confusing "adjusted"
    note on a completely default, untouched page load. Fixed by choosing
    a legitimate default (10% down, above every applicable minimum) rather
    than leaving the correct-but-confusing behavior in place for a first-
    time visitor.
  - 8 H2 content sections (semi-annual compounding, CMHC, amortization-
    vs-term, stress test, payment frequency/acceleration mechanics,
    what lenders look at, what's not covered) + 6 FAQs. Ran the FAQ
    schema-vs-visible-text diff check before assembly as now-standard
    practice -- caught the em-dash mismatch pattern in 5 of 6 answers on
    the first pass, then found *two more* instances of the same issue
    within answers that already had one instance fixed (multiple em-dashes
    per answer, not always caught by fixing just the first one) -- fixed
    all 7 total occurrences and reconfirmed a clean match before moving on.
  - Full Playwright pass: default calculation cross-verified against the
    independent Node math exactly; down payment $/% toggle round-trips
    correctly; below-minimum auto-adjustment and 20%+-down CMHC-section
    hiding both verified; 30-year amortization gating (locked at 25 unless
    the first-time-buyer/new-build box is checked, correctly adds the
    0.20% surcharge) verified; all 6 payment frequencies produce sane,
    internally-consistent numbers; accelerated schedules correctly
    terminate early with a $0.00 final balance; stress-test edge case
    (debts exceeding capacity) correctly shows $0 and an error state;
    zero duplicate IDs; all 23 internal links and in-page anchors resolve;
    PDF export verified from both tabs; mobile layout checked; zero
    console errors throughout. New OG image; title/description tightened
    to fit standard SERP length after drafting.
  **Same-day follow-up #1** (user asked to cross-check colors specifically):
  the page had been deliberately themed red (Canada's flag color) rather
  than the site's own navy finance-category accent every other calculator
  uses -- user correctly pushed back that a site should keep one consistent
  brand identity rather than chasing a per-country color scheme. Reverted
  all 15 page-specific red instances to navy, restored red specifically
  for the error state (it had been swapped to gray to avoid clashing with
  the red theme, which was itself a symptom of the theme being wrong),
  removed the flag emoji from the status bar badge and OG image to match
  every other calculator's plain \$/% badge convention. Full log in the
  commit message; not duplicated here.
  **Same-day follow-up #2** (user asked for a fresh cross-check plus
  deeper keyword research, with instructions to implement any real
  improvement found): re-examined Ratehub.ca, NerdWallet Canada, and the
  official Canada.ca/FCAC calculator specifically for *feature* gaps
  rather than just field-parity. Found two with enough independent
  corroboration to justify building:
  - **Annual Prepayment**: the official Government of Canada mortgage
    calculator itself has a prepayment feature (one-time/yearly/matching
    regular payment) -- this page had no equivalent despite already
    discussing prepayment privileges in its content as something *not*
    covered. Implemented an annual lump-sum prepayment field, verified in
    Node against the existing amortization engine (\$5,000/yr on the
    \$556,740 default: saves 4.67 years and \$67,946 in interest; a 10%-of-
    principal annual prepayment -- a realistic privilege amount --
    collapses a 25-year amortization to 7.3 years), then confirmed the
    live page matches those figures exactly, including the combined case
    of prepayment stacked with an accelerated payment frequency (both
    accelerating simultaneously, correctly compounding the effect further
    without conflict). Fixed the now-contradictory "doesn't model
    prepayment" line in the What This Calculator Doesn't Cover section,
    which the new feature made false, and added a paragraph on both new
    features to How This Calculator Works.
  - **Down Payment Scenarios table**: Ratehub.ca's stated signature
    differentiator is automatically showing multiple down-payment options
    side by side rather than requiring the visitor to re-enter values
    three times. Added a compact table (10%/15%/20% tiers, 5% auto-hidden
    when below the legal minimum for the entered price) inside the result
    card, dynamically recalculated from the current home price/rate/
    amortization, with the tier matching the currently-entered down
    payment visually highlighted. Verified in Node against the existing
    CMHC/payment engine before wiring up, matched exactly live.
  - Proactively handled the same cross-tab and error-state visibility
    issue caught after-the-fact in the Business Loan Calculator session
    (a new result-card element left stale when switching tabs or hitting
    an input error) *before* it could ship this time -- added the
    scenario table to both the tab-switch handler's cleanup and
    showError(), then verified both paths explicitly in the same test
    pass rather than treating it as a one-off bug to catch later.
  - Considered a third gap (Ratehub/multiple sources also flag land
    transfer tax as commonly missing) but declined to add it this
    session: an accurate implementation needs full province-by-province
    tax brackets plus Toronto's separate municipal top-up, and a rough
    placeholder risked being wrong in a way that's worse than the
    existing honest disclosure that it's not covered. Left as a
    documented limitation rather than risk a half-accurate addition
    under time pressure -- candidate for its own dedicated calculator
    in the future instead of being bolted onto this page.
  - Full regression after both features: default calculations on both
    tabs unchanged, FAQ schema still matches visible content (6/6, no new
    mismatches introduced), zero duplicate IDs, all 23 internal links +
    anchors resolve, PDF export (now including prepayment figures when
    active) verified from both tabs, zero console errors.

- **Site-wide consistency pass** (ad-hoc user request, Jul 20, 2026,
  following the Mortgage Calculator Share-button fix): user asked for the
  same fix across every already-developed page, plus separately noticed
  the H1 title ("Loan Calculator", "BMI Calculator", etc.) renders bold on
  some pages and regular on others, asked to make all of them bold.
  - Surveyed all 44 already-rebuilt calculator pages (identified by line
    count != 434, the untouched static template's exact length) via a
    batch Playwright script checking each page's actual computed H1
    `font-weight` and Share-button presence, rather than guessing from
    source or class names.
  - **H1 bold fix**: found 33 pages (all built across this and earlier
    sessions, including this session's own IRA/Bond/Budget/Business Loan
    builds) rendering at `font-weight: 400` because their H1 used
    `font-display text-3xl sm:text-4xl tracking-tight text-ink mb-3` --
    `font-display` only sets font-family, not weight, so it silently
    fell back to regular. Confirmed `.font-bold{font-weight:700}` is a
    globally available utility class (same external stylesheet loaded on
    every page, bold pages like mortgage-calculator already used it
    successfully) before touching anything. Added `font-bold` to the class
    list on all 33 pages via a script (each matched the identical class
    pattern, one clean substitution per file, zero "unexpected pattern"
    or "matched N times" flags), plus ira-calculator by hand as the first
    test case. Verified via a second batch Playwright pass: all 34 pages
    now report `getComputedStyle(h1).fontWeight === '700'`, zero console
    errors introduced. DESIGN_AND_SEO_GUIDE.md updated with this as a
    mandatory standing check for all future builds (H1 must explicitly
    include `font-bold`; don't assume `font-display` implies it).
  - **Share-button fix**: found 7 pages (crypto-position-size,
    crypto-tax, leverage, liquidation-price, mining-profit, risk-reward,
    staking-reward calculators) that matched on "Share" text in an initial
    scan. Investigated each individually rather than assuming they had
    Mortgage Calculator's exact problem -- found they're a *different*,
    older design system entirely (`.calc-btn-row`, `.share-row`,
    `.export-row` classes vs. this session's `{prefix}-btn-row` pattern).
    Their actual Calculate/Clear row (`.calc-btn-row`) is already a clean,
    equal-width 2-button pair with no Share button mixed in -- the "Share"
    match was a separate "Copy shareable link" button living in a
    different `export-row` alongside "Print / Save as PDF" and "Download
    as CSV", confirmed structurally identical across all 7 pages by
    directly checking each file rather than assuming from the first one.
    This is a different feature in a different context, not the same
    crowding problem, so **did not touch it** -- flagged it back to the
    user for an explicit decision rather than silently removing a working
    export feature grouped with tools they likely still want.
  DESIGN_AND_SEO_GUIDE.md's 3-card pattern section now documents both the
  no-Share-button/Calculate-wider-than-Clear convention and this
  crypto-batch distinction explicitly, so future sessions don't have to
  re-derive either finding from scratch.

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
- **Mining Profit Calculator — full rebuild from the older crypto/trading-batch
  pattern to the current 3-card pattern** (ad-hoc user request, Jul 25, 2026,
  reference: bitcoinfoundation.org/tools/mining-calculator/). **Explicit
  design-pattern decision**, flagged and confirmed with the user before
  starting: `DESIGN_AND_SEO_GUIDE.md` §5 names the crypto/trading batch
  (position-size/leverage/liquidation-price/mining-profit/risk-reward/
  staking-reward/crypto-tax) as a protected, intentionally-different pattern
  not to be converted without a separate explicit decision — the user chose
  to convert this one page anyway (accepting temporary inconsistency with its
  7 siblings), modeled directly on `apr-calculator` (closest existing
  reference for bar+lazy-PDF+tabs+donut+schedule+bottomgrid, and the correct
  `loadScriptOnce`/`ensurePdfLibs` lazy-load pattern — NOT `loan-calculator`,
  which still eager-loads jsPDF via a bare `<script src>` tag and should be
  treated as a stale example, not a template, until someone fixes it).
  - **Schema gap found and fixed**: the live page had `BreadcrumbList` only —
    both `FAQPage` and `WebApplication` were completely missing despite 12
    visible FAQs and a dead JS snippet that tried (and silently failed) to
    stamp a `dateModified` onto a `WebApplication` block that didn't exist.
    Same audit found this is a batch-wide gap, not unique to this page:
    of the 7 siblings, only `leverage-calculator` and `crypto-profit-calculator`
    currently have both schemas — worth a dedicated pass later.
  - **FAQ schema/visible-copy match guaranteed by construction, not by manual
    care**: extracted the 12 existing Q&A pairs programmatically into one
    JSON source, then generated *both* the `FAQPage` schema and the visible
    FAQ HTML from that same source, so the exact-match requirement in §3
    can't drift the way the guide's own recurring-failure note describes.
  - **Keyword research (§4)**: web-searched the head term alongside CoinWarz,
    SimpleMining, HashrateIndex, and bitcoinfoundation.org. Finding: nearly
    every serious competitor's biggest differentiator is *live* BTC price +
    live network difficulty/hashrate pre-filled into the calculator, not a
    static default — this page had neither (a stale hardcoded $95,000 coin
    price default, when live BTC was actually ~$64,000 the day of this
    session). Retitled from the generic `X | CalculatorBoss` pattern to
    *"Mining Profit Calculator — Live BTC Price, Hashrate & ROI"* to match
    that finding, kept the URL/H1 as-is per §8 (don't force a rename), and
    rewrote every worked-example number in the article against the corrected
    live-informed defaults (300 TH/s, 900 EH/s network, $64,000, $0.05/kWh).
  - **New live-data feature**: a click-triggered (never automatic) "Use Live
    Bitcoin Price & Network Hashrate" button pulling from
    `api.coingecko.com/api/v3/simple/price` (BTC/USD) and
    `mempool.space/api/v1/mining/hashrate/3d` (current network hashrate).
    Per the CORS hard-lesson in §6: checked `access-control-allow-origin`
    headers via curl+Origin first as triage, then confirmed for real with a
    live Playwright browser-context fetch (succeeded: $63,994 · 912.2 EH/s,
    zero console errors) before treating it as working.
  - **Formula verification**: the existing hashrate-share formula, break-even
    rate, payback period, and solo-odds math were already correct (re-derived
    and hand-checked independently in Node against the new defaults before
    reuse — all matched). The new 12-month schedule table reuses the same
    daily-compounding difficulty/price growth model already used by the old
    page's forecast table (`Math.pow(1+monthly/100, 1/30)-1`), re-verified in
    Node for the new month-by-month (not 6-checkpoint) sampling, plus a
    donut-segment sum-to-revenue check.
  - Dropped from the old page (scope decision, not a bug): the circular
    profit-margin gauge, the localStorage "saved setups" feature, and the
    separate hardware-efficiency benchmark table — folded into the note/badge
    text, the new quick-preset chips (apr-calculator convention), and the
    article's existing efficiency discussion respectively, to match the
    leaner 3-card pattern's shape rather than carrying over every prior
    sub-feature 1:1.
  - Verified before push: schema JSON validity (all 3 blocks), `node --check`
    on all 6 script blocks, protected shared-style-block byte-for-byte
    identical to `apr-calculator`'s (confirmed no drift), zero duplicate/
    dangling element IDs, and a full Playwright pass (desktop + mobile) —
    zero console errors on load/tab-switch/live-fetch, zero horizontal
    overflow, jsPDF confirmed unfetched until the button click and fetched
    correctly after, 3-column grid geometry confirmed non-overlapping,
    12-row schedule + donut + stacked-bar chart all render, Clear button
    resets correctly, and the Solo tab's bottom-grid/donut/PDF-export edge
    cases all checked separately since they use a different EFF shape.
- **Mining Profit Calculator — same-day follow-up, ad-hoc user request Jul 25,
  2026**: user shared a screenshot of bitcoinfoundation.org's mining
  calculator (currency pills, coin icon + live price, 4 simple fields,
  Profit Ratio/Day + Profit/Month cards, Day/Week/Month/Year 2x2 grid) and
  asked for a "same to same" visual replica, with our existing extra
  features (Break-Even & ROI, Solo vs Pool, 12-month schedule, PDF export)
  kept below it rather than removed — confirmed this split explicitly before
  building. Added a new, self-contained `.mcw-*`-prefixed widget as the
  primary tool, with the existing `.min-*` widget relabeled under a new
  "Advanced Tools" divider beneath it.
  - **Multi-coin**: BTC/ETC/XMR/ZEC/DASH/LTC/KAS, all 7 CoinGecko IDs
    verified in one batched price call. Live price fetch now runs
    automatically on page load (not click-gated like the jsPDF/BTC-only
    button in the Advanced Tools section) since a live price is this
    widget's core displayed value, not an optional export feature — same
    category as the site's existing currency-calculator precedent, not a
    deviation from the lazy-load philosophy. Falls back to static per-coin
    prices (verified to keep the widget fully functional) if the fetch
    fails or CoinGecko rate-limits, which it did mid-session from repeated
    test reloads — confirmed the fallback path directly rather than
    assuming it.
  - **Real bug caught before shipping, twice**: first pass's per-coin
    default hashrate/network-hashrate pairs were not sanity-checked against
    each other — ZEC's default had "your hashrate" numerically *exceeding*
    network hashrate (a >100% share, nonsensical), and several others
    produced absurd results (ZEC $680/day profit, ETC/DASH/KAS thousands-of-
    percent negative margins) purely from mismatched magnitudes, not from
    the (already-verified) formula itself. Fixed by hand-deriving every
    coin's defaults from an explicit share-ratio check in Node until every
    coin landed in a modest, plausible daily range. Second bug: the
    electricity-rate and pool-fee fields had no default `value` in the HTML
    and weren't set by the per-coin JS either, so the widget silently
    computed profit as raw revenue (0% costs) until a Playwright check
    caught the mismatch against the expected $5.36 BTC default.
  - Block reward/block time for the 6 non-BTC coins are presented as
    editable "Advanced" defaults, not live data — researched current
    approximate values for each (ETC 2.048, about to reduce to 1.6384 per
    ECIP-1017 around the time of this session; XMR 0.6 tail emission,
    stable; ZEC 1.5625 gross / ~1.25 effective miner share after the
    lockbox+grants split; DASH ~1.0, decreases continuously; LTC 6.25 until
    the ~Jul 2027 halving; KAS ~2.5, decreases monthly) but deliberately did
    **not** try to build 6 more live network-hashrate/difficulty
    integrations to match — several of these coins' rewards are genuinely
    too volatile (Kaspa monthly, Dash continuous, ETC mid-halving this
    week) to respect as a hardcoded "live" figure, so the advanced panel
    says so explicitly rather than overclaiming precision.
  - Verified: schema still valid (3 blocks), all 7 script blocks pass
    `node --check`, protected style block still byte-identical, zero
    duplicate ids across 114 total, full Playwright pass on both the new
    widget (24 checks: all 7 coins compute sane non-NaN results, live price
    pill, advanced toggle, mobile 1-column collapse) and the pre-existing
    Advanced Tools section (22 checks, re-run twice — unaffected by the
    new widget).
- **Mining Profit Calculator — same-day UX/SEO audit, user-requested Jul 25,
  2026**: user asked directly whether the page was 100% confusion-free and
  100% SEO-optimized given a low-competition/modest-demand niche (~20K/mo
  traffic on top competitors per user). Actually audited rather than
  reassured — found and fixed real gaps:
  - **UX**: the new multi-coin widget had no heading/label at all, while
    the pre-existing tool below it was clearly labeled "Advanced Tools" —
    confirmed via DOM inspection (nothing but a `<style>` tag sat above the
    widget). Added a matching "Quick Calculator" divider above it, and
    rewrote both dividers' subtext so each explicitly names the other
    section, so the two-tool structure explains itself. Also found the
    currency pills were only 38px tall on mobile (Playwright
    `getBoundingClientRect`), short of the 44px tap-target guideline —
    bumped padding to fix.
  - **SEO**: confirmed the title, meta description, WebApplication schema,
    and every H2/FAQ were still 100% BTC-only despite the page now
    genuinely supporting 7 coins — a real content-freshness gap, not
    reassurance-worthy. Retitled to "Mining Profit Calculator — Multi-Coin
    ROI, Live BTC Price," rewrote the meta description and WebApplication
    schema to name the coins, added meta keywords for each coin's mining-
    calculator long-tail, added a new H2 ("Mining Profit for BTC, LTC, ETC,
    XMR, ZEC, DASH and Kaspa") with one accurate, sourced fact per coin
    (algorithm, block-time character, reward-schedule quirk), and added 2
    new FAQ entries about multi-coin support and defaults-vs-live-data
    honesty. Validated market-opportunity claim via search: "crypto mining
    calculator" (multi-coin framing) is a real, actively-targeted term
    (CoinDCX, ValueHash, Minerset, CoinWarz, hashrate.no all run 2+ coin
    calculators) that this page previously had zero content overlap with.
  - FAQPage schema went from 12 to 14 questions; re-verified the
    schema/visible-HTML match programmatically (not by eye) after the
    edit, since hand-editing escaped JSON is error-prone — first attempt
    at a targeted string-replace on the raw escaped JSON failed silently
    (mismatched backslash-escaping), caught by an assertion, fixed by
    parsing with `json.loads`/re-serializing with `json.dumps` instead of
    string-patching.
  - Re-verified after every edit: schema JSON validity (3 blocks, FAQPage
    now 14 entities), all 7 script blocks pass `node --check`, div/ul/li
    tag balance, zero duplicate ids, TOC-to-H2 anchor match, protected
    style block still byte-identical, and a full Playwright re-run of both
    prior test suites (only "failure" was a stale selector in an old test
    script picking up the new divider instead of the old one — confirmed
    both headings are present and correctly ordered via a fresh check, not
    a real regression) plus a new 11-check pass covering every fix above.

- **Cash Back or Low Interest Calculator — full rebuild from thin/template
  tier to the 3-card pattern** (ad-hoc user request, Jul 27, 2026; part of
  the broader "23 done / 55 still old-style in Finance" push the user kicked
  off this session).
  - **Keyword research done before writing any copy, per §4.** Head term
    ("cash back or low interest calculator") matches calculator.net directly.
    Cross-checked against Edmunds, Kohler/Purdue credit unions, First
    Citizens, autocheatsheet.com, findthebestcarprice.com, carclearance.com,
    dinkytown.net, AAA. Finding: 5+ major sites converge on an alternate
    framing — **"Low APR vs. Cash Back Calculator"** — blended naturally into
    the title/meta per §8 without renaming the H1/URL.
  - **Content/differentiation gap found:** the old page had no trade-in, no
    sales tax, and no fees — every real competitor above has at least trade-in
    + tax. Bigger find, confirmed across multiple independent sources
    (dinkytown.net, autocheatsheet.com, lease-vs-buy.com): **sales tax is
    calculated on the full pre-rebate price in almost every state** — a cash
    rebate, unlike a trade-in, does not reduce the taxable amount. Built the
    whole page around making this explicit and state-aware, reusing the
    exact `NO_TRADE_REDUCTION` (CA, DC, HI, KY, MD, MI, MT, VA) /
    `NO_SALES_TAX` (AK, DE, MT, NH, OR) state sets already verified and
    shipped in Auto Loan Calculator.
  - **New feature, not on any competitor site checked:** a second tab,
    **Break-Even Cash Back**, reverse-solves the minimum rebate that would
    make the cash-back option match the low-interest offer's total cost.
    Closed-form (payment is linear in loan amount for a fixed rate/term, so
    no iteration needed) — derived algebraically and verified against two
    independent scenarios in Node (exact match both times), plus the
    forward/reverse cross-check convention (§6) confirmed both modes agree.
  - **Math independently verified in Node before any HTML was written**:
    core comparison formula, the state trade-in/no-sales-tax branching, the
    "cash back doesn't reduce taxable base" rule, and the break-even
    reverse-solve — each checked against hand-computed expectations,
    matched exactly.
  - Built on the 3-card pattern (`cbl-`/`cblb-` prefixes), modeled on
    Auto Loan Calculator's own tab/bar/PDF structure (each tab carries its
    own full grid incl. its own PDF button with a distinct id — avoided the
    duplicate-`id="...-pdfBtn"` bug that would otherwise occur from copying
    the bar markup into both tabs verbatim). jsPDF lazy-loaded correctly
    from the start via `loadScriptOnce`/`ensurePdfLibs` (no eager
    `<script src>` regression this time).
  - New OG image generated (none existed for this page before) matching the
    site's real palette/typography (fonts pulled from Google Fonts' own
    CDN to render it, since IBM Plex isn't installed locally).
  - 6 H2 sections + 8 FAQs, written with direct-answer-first phrasing
    ("Short answer: ...") for AI-Overview/GEO citability, plus a visible
    formula block. FAQ schema and visible FAQ HTML generated from one
    shared Python source list to guarantee exact-match by construction
    (per the recurring-mismatch note in §3).
  - Visible sidebar "Related Calculators" now genuinely topical (Auto Loan,
    APR, Auto Lease, Loan, Down Payment) — not the site-wide generic
    6-link copy-paste block flagged as a systemic bug earlier this session.
  - Also updated the one-line card description on `all-calculators/index.html`
    to match the new content (was a generic placeholder sentence).
  - Verified before push: all 3 schema blocks parse + FAQ schema/visible
    exact-match (0 mismatches), zero duplicate element ids site-page-wide,
    `node --check` on all 6 inline script blocks, protected `:root` block
    byte-identical to bmi-calculator, zero eager jsPDF requests (confirmed
    lazy on first click, `window.jspdf` undefined until then), full
    Playwright pass desktop (1440×900) + mobile (390×844): zero console/page
    errors, zero horizontal overflow, non-overlapping grid geometry
    (form/result/sidebar/bottomgrid bounding-box checked programmatically),
    state selector verified across three real states (Texas/California/
    Oregon, each hitting a different branch of the tax logic), Clear button
    resets correctly, both tabs' Calculate buttons produce the exact
    Node-verified numbers ($35,663.56 / $33,654.87 / $2,008.69 diff /
    $3,211.03 break-even) live in the browser.

- **Cash Back or Low Interest Calculator — post-ship audit against calculator.net**
  (ad-hoc user request, Jul 27, 2026, same-day follow-up to the initial
  rebuild above). User asked to specifically cross-check the just-shipped
  page against calculator.net's version for missing fields/result info.
  - **Real bug found and fixed, not just a gap:** the initial build assumed
    a cash-back rebate *never* reduces the sales-tax base, in any state.
    Cross-checking calculator.net's own page content surfaced a claim that
    ~20 states *do* let the rebate reduce the taxable amount — verified
    independently via CarsDirect (citing Edmunds), which lists the same
    ~21 states. **Texas — this page's default state — is on that list**,
    meaning the bug affected the very first calculation every visitor saw.
    Added a `REBATE_TAX_EXEMPT` state set (Alaska, Arizona, Delaware, Iowa,
    Kansas, Kentucky, Louisiana, Massachusetts, Minnesota, Missouri,
    Montana, Nebraska, New Hampshire, Oklahoma, Oregon, Pennsylvania, Rhode
    Island, Texas, Utah, Vermont, Wyoming), independent of and combined
    with the existing `NO_TRADE_REDUCTION` set (a different question).
  - **The Break-Even reverse-solve formula needed re-deriving, not just a
    constant swap** — in rebate-exempt states, increasing the rebate also
    lowers the tax base, changing the linear coefficient in the closed-form
    solution. Re-derived algebraically and re-verified in Node against
    three independent scenarios (Texas/rebate-exempt, California/neither
    exempt, Arizona/rebate-exempt-with-trade-in) — all matched to the cent.
  - **Missing result fields found and added**: calculator.net shows 7 rows
    per scenario (loan amount, sales tax, upfront payment, monthly payment,
    total of N payments, total interest, total cost) — this page only had
    3 (monthly, interest, total). Added the missing 4 rows to both
    scenarios (now 14 result rows total) and to the PDF export.
  - Corrected the worked example, the "Hidden Rule" article section (was
    factually wrong — said "almost every state" taxes the full pre-rebate
    price when it's really closer to 60/40), and the FAQ #3 answer to match
    (FAQ schema and visible text updated identically, exact-match verified
    again). Regenerated the OG image with the corrected savings figure
    ($1,898.63, was showing the pre-fix $2,008.69).
  - Verified again before push: schema valid + FAQ exact-match (0
    mismatches), zero duplicate ids, `node --check` on all 6 script blocks,
    protected `:root` block still byte-identical to bmi-calculator, zero
    eager jsPDF requests, full Playwright pass desktop+mobile with the
    corrected numbers cross-checked against Node for three different states
    (Texas, California, Arizona), break-even re-verified live ($3,022.14),
    PDF export re-tested with the new 14-row breakdown.
  - **Process note for future sessions**: this is a good example of why the
    §4 keyword-research/competitor cross-check should happen *before*
    shipping, not just after a user asks for an audit — the same
    calculator.net content that surfaced this bug was available during the
    original build. Make the competitor content cross-check (not just
    title/keyword research) a standard part of the pre-ship checklist for
    every calculator with state-specific or jurisdiction-specific tax/legal
    rules, not just an afterthought.

- **CD Calculator — full rebuild from thin/template tier to the 3-card
  pattern** (ad-hoc user request, Jul 27, 2026, same "23 done / 55 old-style
  in Finance" push).
  - **Keyword research + competitor cross-check done before writing any
    copy, per §4 and the process note from the Cash Back audit above.**
    Checked calculator.net, Bankrate, NerdWallet, goodcalculators.com,
    savingsinterestcalculator.com. Old page had only 3 compounding buttons
    (Daily/Monthly/Quarterly), no tax consideration, no schedule/chart, and
    no early-withdrawal-penalty feature — all four gaps closed in the
    rebuild.
  - **Math verified in Node against calculator.net's own published example**
    before writing any HTML: $10,000 @ 5% APY, 3-year term, annual
    compounding → their site shows exactly $11,576.25; this calculator's
    formula reproduces that figure to the cent. Continuous compounding
    cross-checked against the direct e^(rt) formula (exact match). Annual
    tax-withholding-per-12-month-block model (matching how CD interest is
    actually 1099-taxed each year it accrues, not just at maturity) checked
    against a simple single-year hand calculation. Early-withdrawal penalty
    formula (balance × (APY/12) × penalty months, sourced from
    savingsinterestcalculator.com) verified exactly. After shipping, the
    literal function from the live JS file was re-extracted and re-run in
    Node directly (not just re-derived by hand) to confirm no transcription
    drift between the verified formula and the shipped code.
  - **New feature not found on any competitor checked**: a
    "Compounding Frequency Compared" card that shows the same deposit/APY/
    term's maturity value across all 6 compounding frequencies side by
    side, live-updating with the user's own inputs — ties directly into
    the FAQ answer about compounding frequency mattering less than people
    assume once APY (not APR) is quoted.
  - Two tabs: **CD Growth** (deposit/APY/term/6 compounding options/
    marginal tax rate, year-by-year schedule + stacked bar chart) and
    **Early Withdrawal Penalty** (current balance, interest earned so far,
    penalty, net proceeds, profitability note) — both with jsPDF lazy-
    loaded correctly from the start.
  - 6 H2 sections + 8 FAQs, each grounded in an actual feature on the page
    (formula, worked example cross-checked against calculator.net, APY vs.
    APR, the withdrawal-penalty tab, the tax-rate field, CD vs. savings vs.
    money market). New OG image (none existed before).
  - **Two real bugs caught by the standard verification pass, not just a
    style formality**: (1) a duplicate-id collision between the article's
    "APY vs. APR" H2 anchor and the APY input field, both accidentally
    named `cdg-apy` — renamed the anchor to `cdg-apy-vs-apr`; (2) a
    leftover `cbl-formula-box` class reference copy-pasted from the Cash
    Back Calculator build, which doesn't exist in this page's own
    stylesheet — removed. Both would have been easy to miss without the
    duplicate-id and byte-level checks being a standing part of the
    pre-push routine.
  - Verified before push: schema valid + FAQ exact-match (0 mismatches),
    zero duplicate ids (after the fix above), `node --check` on all 6
    script blocks, protected `:root` block byte-identical to bmi-calculator,
    zero eager jsPDF requests, full Playwright pass desktop+mobile (zero
    console errors, zero overflow, non-overlapping grid geometry), both
    tabs' results cross-checked live against Node output including the
    calculator.net reproduction case, PDF export tested on both tabs.

- **College Cost Calculator — full rebuild from thin/template tier to the
  3-card pattern** (ad-hoc user request, Jul 27, 2026, same "23 done / 55
  old-style in Finance" push).
  - **Competitor cross-check (calculator.net) done before writing any copy.**
    Old page had only 4 inputs (annual cost today, years until enrollment,
    tuition inflation rate, years of college) and one output (total cost) --
    calculator.net's version additionally offers quick-select average costs
    by school type, a savings-percentage/balance/return/tax model, and cross-
    links to a Student Loan Calculator. Closed all of these gaps.
  - **Math verified in Node before writing any HTML**, cross-checked against
    two independent sources: the cost-projection formula reproduces this
    page's own prior worked example exactly ($25k/yr, 10yr, 5%, 4yr ->
    $40,722.37 first-year / $175,518.49 total, both to the cent); the
    savings-growth and reverse-solve-required-contribution formulas were
    checked against a hand-rolled step-by-step simulation (exact match) and
    a third-party illustrative example (an Indiana University 529 explainer's
    "$125/month for 18 years at 4%" scenario) -- close but not exact, which
    on investigation is because that blog post's own numbers are an
    approximate illustration, not a canonically-sourced worked example, so
    the internal step-by-step cross-check (not the blog post) was treated as
    the authoritative verification.
  - **New feature not found on calculator.net**: a reverse-solve "monthly
    contribution needed to fully close the gap" result, alongside the
    forward projection -- verified by solving for the contribution, then
    simulating forward with that exact value and confirming it reproduces
    the target cost to the cent (including a zero-return-rate edge case).
  - Two tabs: **Projected Cost** (annual cost today with 2025-26 College
    Board quick-select chips for 4-year private/in-state public/out-of-state
    public/2-year public, years until enrollment, increase rate, years of
    college, year-by-year schedule + chart) and **Savings Gap** (current
    balance, monthly contribution, years, return rate, tax rate with "0%
    for a 529 plan" guidance, auto-synced with Tab 1's projected total unless
    the user overrides it) -- both with jsPDF lazy-loaded correctly from the
    start. 6 H2 sections + 8 FAQs covering the formula, 529 vs. prepaid
    plans, and what a "cost of attendance" figure actually includes. New OG
    image (none existed before).
  - **Caught before push, by actually running the shipped numbers through
    Playwright and diffing against Node rather than trusting hand-written
    prose**: the article's own worked-example paragraph and the static
    HTML placeholder in the Savings Gap result card both had wrong
    illustrative numbers ($84,135 projected / $91,383 gap / $682/month --
    an arithmetic slip made while drafting the prose, never actually run
    through Node for that specific input combination before being written
    down). The shipped JS itself was correct throughout; only the written
    example numbers were wrong. Re-verified the real numbers in Node
    ($58,260.79 projected / $117,257.70 gap / $1,015.51 required) and
    corrected both the article text and the static placeholder to match.
    **Process takeaway**: verifying a formula in the abstract does not
    verify every specific example number written into the page's prose --
    each concrete worked-example figure quoted in article copy needs its
    own direct Node check against that exact input combination before
    shipping, not just a general formula-correctness check.
  - Verified before push (after the worked-example fix above): schema valid
    + FAQ exact-match, zero duplicate ids (checked proactively during
    assembly this time, not just after a failure), `node --check` on all 6
    script blocks, protected `:root` block byte-identical to bmi-calculator,
    zero eager jsPDF requests, full Playwright pass desktop+mobile (zero
    console errors, zero overflow, non-overlapping grid geometry), both
    tabs' live results re-confirmed against Node output, quick-select chips
    tested, cross-tab total-cost sync tested, PDF export tested.

- **Credit Card Calculator — full rebuild from thin/template tier to the
  3-card pattern** (ad-hoc user request, Jul 27, 2026, same "23 done / 55
  old-style in Finance" push).
  - **Significant scope-mismatch found during competitor cross-check, not
    just a content-depth gap.** The old page only computed one thing --
    this billing cycle's interest charge via the average-daily-balance
    method. But calculator.net's own page at the identical URL slug/head
    term ("Credit Card Calculator") is described as finding "the time it
    will take to pay off a balance, or the amount necessary to pay it off
    within a certain time frame" -- i.e. a payoff-time/payment calculator,
    which matches the dominant search intent per SmartAsset, WalletHub, and
    Bankrate too. The old page was answering a real but much narrower
    question than what the term/title actually implies to searchers.
  - **Checked the sibling Credit Card Payoff Calculator first to avoid
    scope duplication** before deciding what to add: that page already
    covers single-card balance/APR/fixed-payment -> payoff-date (the
    forward direction only, no min-payment presets, no reverse mode).
    Decided to keep this page's existing ADB content (genuinely different,
    still useful) as Tab 1, and add the two things calculator.net's version
    has that neither of our own pages had -- the reverse mode (target
    payoff date -> required payment) and minimum-payment quick-select
    presets -- as a new Tab 2, rather than duplicating the sibling's
    forward-only calculation.
  - **Math verified in Node against multiple independent authoritative
    sources before writing any HTML**: the existing ADB formula re-verified
    against calculator.net's own worked example (15% APR, 15 days @ $500 +
    15 days @ $400 over 30 days -> $450 ADB, $5.54 interest, matched to the
    cent allowing for their own rounding); the new payoff/reverse-solve
    formulas verified against Bankrate's own two published examples ($7,000
    @ 21%, $200/mo -> ~54.6 months / ~$3,929 interest, and the same balance
    targeted for 24 months -> ~$359.70 required payment / ~$1,633 interest) --
    both matched almost exactly. A forward/reverse round-trip cross-check
    (solve required payment for a target, then solve months back from that
    payment) also confirmed exactly 24 months both ways.
  - Two tabs: **Interest Charge This Cycle** (kept from the old page: ADB,
    APR, days in cycle) and **Payoff Time & Minimum Payment** (new: balance,
    APR, a payment-vs-target-date mode toggle, and minimum-payment quick-
    select chips modeling common "interest + 1-5% of balance" issuer
    formulas) -- both with jsPDF lazy-loaded correctly from the start, and
    a "this payment never pays it off" warning state when payment doesn't
    cover monthly interest. 6 H2 sections + 8 FAQs covering the three
    interest-calculation methods, minimum-payment reality, and common
    interest-cost mistakes. New OG image.
  - Verified before push: schema valid + FAQ exact-match, zero duplicate
    ids (checked proactively during assembly), `node --check` on all 6
    script blocks (after fixing three escaped-apostrophe syntax errors
    caught by the same check), protected `:root` block byte-identical to
    bmi-calculator, zero eager jsPDF requests, full Playwright pass
    desktop+mobile (zero console errors, zero overflow, non-overlapping
    grid geometry), both tabs' live results reconfirmed against Node
    output including the Bankrate reproduction cases, minimum-payment chip
    math checked by hand, the never-pays-off warning state tested, PDF
    export tested.

- **Credit Card Calculator — same-day follow-up field-parity check** (Jul
  27, 2026, user explicitly asked to re-cross-check against calculator.net
  to confirm no input fields were missing). Found one minor gap: their
  "pay off within a certain timeframe" mode accepts Years + Months as two
  separate fields (summed internally), while ours only had Months. Not a
  functional limitation (any duration is expressible in months alone), but
  added a Years field alongside Months for exact convenience-parity anyway.
  Verified the combined value is used correctly (2yr + 6mo -> 30 months,
  cross-checked against calling the payment formula directly with n=30 --
  matched to the cent), re-checked for duplicate ids and JS syntax, and
  re-ran the full Playwright pass (desktop+mobile, zero errors/overflow,
  new field doesn't crowd the row).

- **Commission Calculator — full rebuild from thin/template tier to the
  3-card pattern, PLUS a real systemic bug discovered and fixed** (ad-hoc
  user request, Jul 27, 2026).
  - **Miscategorization caught first**: this page's title
    ("Commission Calculator — Flat or Tiered Rates | CalculatorBoss")
    slipped through the earlier automated "which Finance pages are done"
    regex check as custom-tier, because the regex only flagged the fully
    generic `X | CalculatorBoss` pattern with no dash. This page has a dash
    before the CalculatorBoss suffix, so it was wrongly counted as done.
    Actual content was thin: 484 lines, 2 hardcoded tiers, no PDF, no
    schedule, no sidebar, 2 FAQs -- confirmed thin on inspection before
    starting the rebuild. **Flag for later: re-audit the "done" Finance
    list for other titles with a dash-before-suffix that may have slipped
    through the same way.**
  - **Competitor cross-check (calculator.net)**: their page actually offers
    two tools -- a simple solve-for-any-of-3 calculator (sales price /
    commission rate / commission amount, given any two) and a tiered
    calculator supporting up to 8 tiers plus an optional base commission.
    Our old page had neither the solve-for-any feature nor a base-commission
    option, and only 2 tiers. Rebuilt with both: a Simple Commission tab
    (solve for any of the 3 values) and a Tiered Commission tab (3 tiers +
    base commission).
  - **Math verified in Node against calculator.net's own three worked
    examples** before writing any HTML: real-estate commission-only
    ($500,000 @ 3% = $15,000, plus the round-trip solving each of the other
    two variables back from that result); their tiered example ($27,000
    sale, $0-20k@3%/20k-25k@5%/25k+@10% -> $1,050 exactly); and their
    base-plus-commission example ($500 base + 1.5% of $25,000 = $875).
    All three matched exactly, and the literal shipped JS functions were
    re-extracted and re-run in Node directly to confirm no transcription
    drift.
  - **Real mobile-overflow bug found and fixed during the standard
    Playwright pass, with likely implications for four other pages already
    shipped this session.** The second tab's grid used an inline
    `style="grid-template-areas:...三-column shape..."` override (a pattern
    copied from every earlier build this session -- Cash Back, CD, College
    Cost, Credit Card -- for the tab that has no bottomgrid row). Inline
    styles always win over any external stylesheet rule for the same
    property regardless of viewport, so the mobile media query's
    single-column `grid-template-areas` was being silently overridden by
    the inline 3-column area shape on every viewport, including mobile --
    causing the grid to lay out with implicit 3-column tracks and overflow
    horizontally. This went undetected in every earlier build because the
    tab affected was never the *default* active tab in those pages, and
    the standard mobile-overflow check ran on page load without switching
    tabs first. Commission Calculator made the affected tab (Simple
    Commission) the *default* tab, which is what surfaced the bug
    immediately via the standard test. **Fixed here** by replacing the
    inline style with a dedicated `.com-grid-nobg` class carrying its own
    desktop-width and mobile-media-query rules, with no inline-style
    involved at all. **Action item, not yet done**: re-check the
    non-default ("reverse mode") tab on Cash Back or Low Interest
    Calculator, CD Calculator, College Cost Calculator, and Credit Card
    Calculator for the same latent bug -- switch to each page's second tab
    specifically before running the mobile-overflow check, since checking
    only the default tab will not catch it.
  - Two tabs: **Simple Commission** (solve-for-any-of-3 with a "Solve for"
    selector that disables the field being solved) and **Tiered Commission**
    (3 tiers + base commission, tier breakdown table + chart) -- both with
    jsPDF lazy-loaded correctly from the start. 6 H2 sections + 8 FAQs. New
    OG image.
  - Verified before push: schema valid + FAQ exact-match, zero duplicate
    ids, `node --check` on all 6 script blocks, protected `:root` block
    byte-identical to bmi-calculator, zero eager jsPDF requests, full
    Playwright pass desktop+mobile re-run after the overflow fix (zero
    console errors, zero overflow on both tabs this time), both tabs' live
    results reconfirmed against Node/calculator.net reproduction cases,
    solve-for-any round-trip tested in the browser, PDF export tested.

- **Site-wide mobile-overflow fix: the 4 pages flagged after the Commission
  Calculator discovery** (Jul 27, 2026, same-day follow-up). Applied the
  identical fix to Cash Back or Low Interest Calculator, CD Calculator,
  College Cost Calculator, and Credit Card Calculator's second ("no
  bottomgrid") tab: replaced each page's inline
  `style="grid-template-areas:'bar bar .' 'tabs tabs .' 'form result
  sidebar'"` with a dedicated `.{prefix}-grid-nobg` class carrying its own
  desktop-width rule plus a proper mobile `@media(max-width:860px)` rule
  -- no inline style involved, so the mobile media query can no longer be
  silently overridden.
  - Verified per page: brace-balanced CSS, zero remaining inline
    `grid-template-areas` styles, zero duplicate ids, schema still valid.
  - **Playwright re-run with the specific check that was missing before**:
    switched to each page's second tab explicitly (not just checked the
    page on load) at both 1440px and 390px widths -- all 4 pages now show
    zero horizontal overflow on both the default and second tab, at both
    widths. Also re-ran each second tab's live calculation as a regression
    check (Cash Back break-even $3,022.14, CD withdrawal net $10,188.05,
    College Cost savings gap $117,257.21, Credit Card payoff 54.6 months)
    -- all matched their previously-verified values exactly, confirming
    the CSS-only fix didn't disturb any calculation logic.
  - **Process takeaway, reinforcing the one already logged under Commission
    Calculator above**: a mobile-overflow check that only runs on page
    load will not catch a bug confined to a non-default tab. Any page with
    multiple tabs now needs the overflow (and console-error) check re-run
    once per tab, not once per page, as a standing part of the pre-push
    routine going forward.

- **Credit Card Payoff Calculator: full rebuild, template-tier → custom-built**
  (Jul 27, 2026). The existing page was worse than template-tier — it was a
  dead static snapshot of a React SSR render (hardcoded input `value`
  attributes, a hardcoded "2y 10m" result, zero calculator JS anywhere in
  the file), so it never actually worked for a real visitor. Rebuilt from
  scratch using the auto-loan-calculator 3-card pattern as the direct
  reference (bar+lazy-PDF, tabs, form/result/sidebar/bottomgrid grid).
  - **Keyword research** (mandatory step, done before writing title/meta):
    web-searched the head term and confirmed "Credit Card Payoff Calculator"
    is the term every major competitor uses verbatim (Bankrate, Experian,
    KeyBank, calculator.net, Federal Reserve, Yahoo Finance) — no rename
    needed. Confirmed via the same search that the two-mode pattern (given
    payment → find payoff time; given a payoff-time goal → find required
    payment) is the standard structure competitors use, which shaped the
    two-tab design below. Long-tail variants worked into meta
    keywords/content: "credit card debt payoff calculator", "how long to
    pay off credit card", "credit card interest calculator", "credit card
    repayment calculator".
  - Two tabs: **Fixed Payment** (balance + APR + monthly payment → payoff
    time, total interest, debt-free date, donut chart, Annual/Monthly
    payoff schedule table, stacked bar chart of interest vs. principal by
    year) and **Fixed Payoff Time** (balance + APR + payoff-goal-in-months
    → required monthly payment, reverse-solved).
  - **Formula verification in Node before embedding** (per standing
    directive): forward month-by-month simulation cross-checked against
    the analytic amortization-style formula, and both directions
    cross-checked against each other and against Bankrate's own published
    worked examples ($7,000/21%/$200mo ≈ 4.58yr/$3,930 interest vs.
    Bankrate's stated "~4.5 years/~$4,000"; $7,000/21%/24mo-goal → $359.70
    required payment/$1,632.79 interest vs. Bankrate's stated "$359/mo,
    $1,632 interest" — both matched closely).
  - **Real bug caught during verification, same pattern as the Annuity
    Payout fractional-period lesson already logged in this file**: the
    reverse "required payment" solve produces an exact fractional-cent
    payment; naively rounding it to the *nearest* cent can round down by a
    fraction of a cent, which is just enough to leave the balance
    unpaid at the stated goal and silently push the real payoff one month
    late (caught by simulating the rounded payment and finding it took 25
    months instead of the requested 24). Fixed by always rounding the
    reverse-solved payment **up** to the cent before simulating/displaying
    it, never to nearest or down.
  - Never-payoff case handled explicitly: if the entered payment doesn't
    exceed the first month's interest charge, the result card switches to
    a red/warning state instead of showing a misleading number.
  - 8 FAQs, generated from a single Python source list so the FAQPage
    schema and the visible `<h3>`/`<p>` HTML are built from the exact same
    strings and can never drift apart (the recurring em-dash/quote-drift
    failure mode already logged multiple times in this file for IRA/Bond/
    Budget) — verified programmatically post-build that schema Q/A text
    equals the visible Q/A text exactly, not just eyeballed.
  - Verified before push: all 3 JSON-LD blocks parse; protected `:root`
    style block byte-identical to auto-loan-calculator; header and footer
    blocks byte-identical to auto-loan-calculator; `node --check` clean on
    the extracted script; full Playwright pass at 1440px and 390px (zero
    console errors, zero horizontal overflow at both widths, H1
    `getComputedStyle` confirmed `fontWeight:'700'`); confirmed jsPDF/
    autotable fetch zero bytes on page load and exactly once total across
    two PDF-button clicks; both tabs' live results reconfirmed in-browser
    against the Node-verified numbers (34 months/$1,749.88 interest on the
    default $5,000/22%/$200 case; $259.40/$1,225.32 interest on the
    reverse $5,000/22%/24-goal case) — exact match.
  - No og image existed for this slug (same as auto-loan-calculator) — no
    `og:image` tag shipped, consistent with that reference page rather
    than shipping a broken image URL.

- **Credit Card Payoff Calculator: post-build cross-check against calculator.net +
  SEO/AdSense tightening** (Jul 27, 2026, same-day follow-up to the rebuild above,
  per an explicit new standing user directive — see below). Live-fetched
  calculator.net's "Credit Cards Payoff Calculator" (turned out to be a
  *different* tool — multi-card debt-avalanche, not single-card) and its
  actual single-card equivalent, "Credit Card Calculator", to diff fields.
  - **Real gap found and fixed**: calculator.net's single-card tool offers an
    "Interest + X% of Balance" payment mode (1-5% presets) modeling how most
    real issuers actually define the minimum payment — ours only had fixed-
    amount and fixed-time-goal modes. Verified the math in Node first
    (confirmed it's geometric decay independent of APR: balance next =
    balance × (1 − pct/100); at 2% on $5,000/22% APR it doesn't clear within
    50 years, at 5% it clears in 270 months/$1,833.33 interest) before wiring
    it in as a third **Payment Type** selector on the Fixed Payment tab, with
    a "50+ years / capped" warning state distinct from the true
    never-payoff state (payment ≤ interest).
  - Added a new H2 ("How Your Card's Minimum Payment Is Actually Calculated")
    and a 9th FAQ for this feature — same one-source-list generation +
    programmatic Q/A exact-match verification as the original 8.
  - **Real AdSense/honesty issue caught and fixed**: the original copy
    claimed the Debt Payoff Calculator "handles multiple cards... and
    compares" avalanche/snowball. Checking that page's actual live code
    (per section 10's "verify claims about other pages are true" rule)
    showed it's currently a dead template — same broken static-snapshot
    pattern this page was in before its rebuild, not an interactive
    multi-card tool. Reworded both mentions (one FAQ answer, one body
    paragraph) to only claim the page *covers the topic*, not that it
    computes anything, in both the FAQPage schema and the visible HTML
    consistently.
  - Tightened title (`Credit Card Payoff Calculator — Debt-Free Date &
    Interest Cost`) and meta description for click-through, not just
    keyword match; expanded `meta keywords` with more long-tail terms
    tied to the new feature ("credit card minimum payment calculator",
    "minimum payment credit card calculator").
  - Re-verified everything after all edits: all 3 JSON-LD blocks valid,
    FAQ schema/visible-HTML exact match re-confirmed with a corrected
    (section-scoped, not whole-document) diff script after an earlier
    false-alarm caused by footer `<p>` tags bleeding into a naive
    "last N paragraphs" check, protected style block still byte-identical
    to auto-loan-calculator, zero duplicate ids, all 6 inline `<script>`
    blocks pass `node --check`, zero console errors and zero horizontal
    overflow on a full Playwright re-run at 1440px/390px covering both
    tabs and all three payment modes, PDF export still lazy and still
    correct in each mode.
  - **New standing directive this session, saved into
    `DESIGN_AND_SEO_GUIDE.md` section 3a (not just here, since PROGRESS.md
    entries aren't re-read the way the guide file is) — applies to every
    future calculator build/upgrade**: live-diff calculator.net's
    equivalent page (checking for a same-scope sibling page if the
    exact-title match turns out to cover a different scope, as happened
    here) for missing input fields or result rows before finalizing any
    page, and keep title/meta optimized for click-through and AdSense
    compliance explicitly in mind on every page, not as a one-off.

- **Credit Card Payoff Calculator: added a genuine third tab (Multiple Cards /
  Debt Avalanche) after the user pushed back on the calculator.net cross-check**
  (Jul 27, 2026, same-day follow-up). The prior session's cross-check had
  concluded calculator.net's exact-URL-match page ("credit-card-payoff-
  calculator.html") was a different-scope tool (multi-card avalanche) and
  left it at that -- the user correctly pointed out that since our URL slug
  matches theirs exactly, visitors comparing the two would find ours simply
  doesn't do what theirs does at all. Closed that gap for real instead of
  just documenting the difference.
  - Added a third tab: per-card rows (name/balance/min payment/APR, add up
    to 10, remove any), one combined monthly budget, full debt-avalanche
    simulation (pay every card's minimum, cascade all leftover budget to
    the highest-APR active card, roll the payment forward the instant a
    card clears), insufficient-budget warning, payoff-order table, a
    stacked balance-by-card chart, an aggregate principal/interest donut,
    and PDF export.
  - **Avalanche algorithm verified in Node before wiring in** (per the
    section 3a directive this exact session created): built a hand-checked
    3-card scenario and confirmed the highest-APR card is paid off first
    and total interest comes out lower than a snowball (balance-first)
    ordering on the same cards -- $708.82 lower in the specific test case,
    confirming the cascade logic is genuinely APR-priority and not
    coincidentally matching balance-priority (the first test scenario used
    happened to have the same order both ways and would have hidden a bug).
  - Updated meta description, keywords, H1 subhead, added a new H2 section
    with the exact Node-verified 3-card worked example (Card A/B/C, $500
    budget -> 25 months, $2,421.01 total interest, payoff order C-then-A-
    then-B), revised one now-outdated FAQ that used to point elsewhere for
    multi-card support, and added a 10th FAQ clarifying this tab is
    avalanche-only (not snowball) -- all done via the same one-source-list
    generation + programmatic schema/visible-HTML exact-match verification
    as every other FAQ batch on this page.
  - Re-verified everything after the addition: all 3 JSON-LD blocks valid,
    all 10 FAQs match exactly (schema vs. visible, section-scoped diff),
    protected style/header/footer blocks still byte-identical to auto-
    loan-calculator, zero duplicate ids, all 6 script blocks pass
    `node --check`, full Playwright re-run (two separate test scripts, one
    per existing/new feature set) at 1440px/390px: zero console errors,
    zero horizontal overflow, add/remove-card-row interactions work,
    insufficient-budget warning triggers correctly, PDF export works on
    the new tab, and every displayed number (25 months, $2,421.01 interest,
    Card C/A/B payoff dates of Apr 2027/Jan 2028/Aug 2028) matches the
    Node-verified figures exactly.

- **Crypto Profit Calculator link consolidated into Crypto Profit / Loss
  Calculator** (Jul 27, 2026). Per explicit user instruction: the Finance
  category previously listed a separate, older "Crypto Profit Calculator"
  entry pointing to `/crypto-profit-calculator/` (a thinner, earlier build),
  while the Crypto & Trading category already listed the fully-built
  "Crypto Profit / Loss Calculator" at `/crypto-profit-loss-calculator/`.
  User wanted the same one calculator (same URL) to show up under both
  categories, with the old separate link gone.
  - Added a 301 redirect (`/crypto-profit-calculator/` and the no-slash
    variant \u2192 `/crypto-profit-loss-calculator/`) to `_redirects`, same
    convention as the existing money-markets migration block. Confirmed via
    Cloudflare's own docs before relying on this: redirects are always
    followed regardless of whether a static asset exists at that path, so
    the old `/crypto-profit-calculator/` folder didn't need to be deleted
    for the redirect to take effect -- left the folder in place (harmless,
    never served once the redirect fires) rather than risk an unrelated
    deletion.
  - Updated every live reference to the old link to the new one, matching
    name/description/icon to the existing Crypto & Trading card exactly so
    both category listings show the literal same calculator: the Finance
    section card in `all-calculators/index.html`, the Finance-section entry
    in `calculators-index.json` (used by the site search modal -- now has
    two identical-name/link entries by design, one per category, matching
    how the card appears twice on `all-calculators`), the Finance-section
    row in `sitemap/index.html`, one entry in `llms.txt`, and both the
    sidebar link and an inline body-text mention on `currency-calculator`'s
    related-calculators content.
  - Removed the now-redundant `<url>` block for `/crypto-profit-calculator`
    from `sitemap.xml` entirely (a sitemap shouldn't list a URL that only
    301-redirects).
  - **Found but deliberately did not touch** (out of scope for this
    request, noted below instead): a large legacy Next.js JS chunk
    (`_next/static/chunks/3jjeklmpxnvz6.js`) also contains an embedded
    calculator-metadata array with a `crypto-profit-calculator` slug --
    confirmed via grep that this chunk is only `<script>`-referenced by a
    handful of not-yet-rebuilt legacy pages (bmi-calculator, loan-
    calculator, grade-calculator, gpa-calculator, the 404 pages) and NOT by
    any of the pages actually edited here, so it can't silently overwrite
    today's static-HTML edits at runtime. Left as-is since editing a shared
    minified bundle for an unrelated task is exactly the kind of scope
    creep this repo's "one calculator/task per commit" convention warns
    against.
  - Verified: `sitemap.xml` still valid XML, `calculators-index.json` still
    valid JSON, tag-balance check clean on all touched HTML files, and a
    full Playwright pass on `all-calculators/` confirmed zero remaining
    `/crypto-profit-calculator/` links, exactly two identical `/crypto-
    profit-loss-calculator/` cards (one per category) with matching name/
    description text, and zero console errors; same pass on
    `currency-calculator/` confirmed both the sidebar and inline links
    updated with zero console errors.

- **Credit Card Payoff Calculator: proactive edge-case bug hunt per user
  request ("bug thakle fix kore felo" -- fix any bugs)** (Jul 27, 2026,
  same-day follow-up). Rather than waiting for a bug report, ran a
  systematic Playwright sweep across all three tabs feeding deliberately
  hostile inputs (zero/negative balance, zero/negative APR, zero/negative
  payment, empty fields, zero monthly budget, negative card balances,
  APR=0 combined with min-payment=0, adding the 11th card, removing every
  card, etc.) and found three real, confirmed bugs:
  1. **Fixed Payoff Time tab, literal-entity display bug**: the "never
     pays off" fallback branch set `bignum.textContent = '&mdash;'` --
     `textContent` does not parse HTML entities, so visitors would have
     seen the literal text "&mdash;" on the page instead of an em dash.
     This specifically triggered whenever Current Balance was 0 (or
     effectively 0), since the reverse-solved payment came out to exactly
     $0, which the never-payoff guard (`payment <= balance*r`) treats as
     true at the zero/zero boundary. Fixed by using the actual `\u2014`
     character, and separately added a dedicated "balance is already $0,
     no payment needed" message ahead of that guard so the common case
     (someone testing with 0) gets an accurate, specific message instead
     of routing through the generic never-payoff fallback at all.
  2. **Negative balance/APR/payment not clamped** in the Fixed Payment
     tab: typing a negative balance (e.g. -500) produced a nonsensical
     "Total Amount Paid: -$500.00" instead of being treated as invalid/
     zero. The Multiple Cards tab already correctly filtered non-positive
     card balances via `readCardRows`, but the two single-card tabs had
     no equivalent guard. Fixed by clamping balance/APR/payment/percent/
     budget reads to `Math.max(0, ...)` at the point each render function
     reads them, and hardened `readCardRows` to also clamp min-payment
     and APR (previously only balance was implicitly filtered).
  3. **Multiple Cards tab, missing warning banner on the 50-year-cap
     state**: when the avalanche simulation hits the cap (budget too low
     relative to the cards' needs) it correctly showed "50+ years" but,
     unlike the single-card Fixed Payment tab's equivalent capped state,
     displayed no explanatory warning banner -- a user would see a bare
     "50+ years" with no indication of why or what to do. Added the same
     warning-banner pattern used elsewhere on this page for consistency.
  - Re-verified after fixes: all 3 JSON-LD blocks valid, all 10 FAQs still
    exact-match (schema vs. visible), protected style/header/footer
    blocks still byte-identical to auto-loan-calculator, zero duplicate
    ids, all 6 script blocks pass `node --check`, zero remaining
    `textContent = '&...'` entity bugs anywhere in the file (grepped for
    the whole pattern, not just the one instance found), full Playwright
    re-run of both existing regression suites confirms zero console
    errors / zero horizontal overflow and every previously-verified
    number (2y 10m, $259.40, 22y 6m, 25-month avalanche schedule, etc.)
    is unchanged -- these were genuine bug fixes with no side effects on
    the already-correct paths.

- **Debt Consolidation Calculator: further pass on top of the same-day
  rebuild above** (Jul 31, 2026, separate session running in parallel with
  the one that produced the "dead template to custom-built" rebuild
  described in the commit this entry sits after). Both sessions
  independently rebuilt this page to the 3-card pattern at the same time;
  this pass fetched the other session's already-pushed version before
  pushing its own, compared the two rather than blindly overwriting, and
  kept that version as the base (it was already solid: weighted-average
  rate, fee-adjusted real-APR bisection solver, 8 exact-match FAQs, lazy
  PDF) while adding what a feature/content diff showed was genuinely
  missing relative to the site's own standing pattern and this page's
  keyword research:
  - **Amortization Schedule (Annual/Monthly toggle) + a stacked
    principal-vs-interest bar chart by year** for the new consolidation
    loan — the base version had a single comparison chart but no schedule
    table at all, and the Annual/Monthly-schedule-plus-stacked-chart
    pairing is the site's own standing bottomgrid convention (see
    auto-loan-calculator, apr-calculator) that every 3-card page is
    expected to carry.
  - **Break-even Point** output (months for the loan fee to be recovered
    via lower monthly payments) — surfaced during this page's own keyword
    research as a real, repeatedly-used concept on competitor pages
    (calculatorbank.com, LendingTree's fee discussion), not present in the
    base version.
  - A debt-row cap (20, matching calculator.net's own limit) with a plain-
    language warning once reached, rather than an unbounded list.
  - Title/meta description merged: kept the base version's
    APR-forward title (`— Compare Your Real Savings & APR`) since it
    covers more of the researched keyword set than this session's
    independently-drafted title, rather than reverting it.
  - Re-verified everything after merging in the additions: all schema
    blocks valid JSON, 8/8 FAQ schema-vs-visible exact match, zero
    duplicate ids, inline script passes `node --check`, protected style
    block confirmed byte-identical to a current reference page, full
    Playwright pass (desktop 1400px + mobile 390px) shows zero console/
    page errors, zero horizontal overflow, `h1` at font-weight 700, and
    the new schedule/chart/break-even additions all populate correctly
    alongside the base version's existing working features.
  - **Process note for future sessions**: this is the second time in one
    day two sessions have independently built out the same queued page
    (see the token-reuse note below for the other recurring cross-session
    issue). Worth considering whether the priority queue in this file
    should be checked/claimed at the start of a session, or the user
    confirms which page is "taken," before starting a full rebuild, to
    avoid this doubled effort recurring.

- **Debt Consolidation Calculator: real-user UX audit + fixes** (Jul 31,
  2026, same-day follow-up, user request: "audit this so it's easy to use,
  not confusing/boring, and competitive with calculator.net on impression/
  click/AI-citation quality"). Walked through the page as a first-time
  visitor rather than re-reading the code, and found real issues:
  1. **Mobile debt-row fields had no visible labels.** The column headers
     (`Debt name / Balance / Payment / APR`) are `display:none` under
     520px, and the inputs only had invisible `aria-label`s — a phone
     visitor would see four unlabeled boxes per debt with no way to tell
     which was which. Fixed by adding a small uppercase label above each
     field that only renders on narrow screens (`.dc-mlabel`, hidden by
     default so desktop is unaffected), and switching the mobile row from
     a 2-column grid to a stacked flex layout so label+input pairs read
     naturally top to bottom.
  2. **No plain-language verdict.** The green/red bignum ("$5,650.66")
     answers "how much," but a non-finance visitor still has to work out
     whether that's good news. Added a one-line verdict sentence under the
     bignum ("✓ Worth it — this loan costs less overall..." / "✗ Not worth
     it as entered..."), so the takeaway is unmissable without reading the
     rest of the card.
  3. **Loan Amount default could look broken.** It's hardcoded to 16000 to
     match the default debts, but a real visitor entering their own debts
     would see it stay at 16000 while their own total balance is something
     else entirely — reads like a bug. Changed to auto-sync to the current
     total balance on every debt edit, stopping automatically the moment
     the visitor types into the Loan Amount field directly (tracked via a
     `loanAmountTouched` flag, set only by a real `input` event — a
     programmatic `.value =` assignment doesn't fire it, so the auto-sync
     itself doesn't accidentally mark the field as touched).
  4. **Jargon with no inline explanation.** "Loan Fee / Points," "Real APR
     (fee-adjusted)," and "Blended Current APR" are all explained in the
     article below the calculator, but a visitor scanning just the tool
     itself has no idea what they mean in the moment. Added small "?"
     tooltip icons (native `title` attribute, zero extra JS/markup weight)
     with a one-sentence plain-language explanation on each.
  5. **No immediate "so what" answer above the fold.** Added a short
     highlighted "Quick answer" callout right under the subhead stating
     the core decision rule in one sentence — this both orients a
     confused/impatient visitor before they've touched a single field, and
     is written as a clean, standalone, quotable definition for AI
     Overviews / ChatGPT / Perplexity to lift directly (GEO consideration
     alongside traditional on-page SEO).
  6. **Hardened an extreme edge case**: if a Loan Fee is entered at or
     above 100% of the loan amount (net proceeds ≤ 0), Real APR is now
     `null` → displayed as "N/A" everywhere it's shown (results card and
     PDF export), instead of silently falling back to the stated rate,
     which would have been quietly wrong.
  - Re-verified after all fixes: JSON-LD still valid, 8/8 FAQ schema-vs-
    visible still exact match, zero duplicate ids, script still passes
    `node --check`, protected style block still byte-identical to
    apr-calculator, full Playwright re-run (desktop + mobile) confirms
    zero console/page errors, zero horizontal overflow, mobile field
    labels now compute `display:block`, manual Loan Amount edits correctly
    stop the auto-sync, and every previously-verified number/feature
    (default $5,650.66 savings, PDF lazy-load, add/remove row, fee toggle,
    Annual/Monthly toggle) is unchanged.

- **Batch of five calculators rebuilt in one session** (Jul 31, 2026):
  Depreciation, Discount, Down Payment, Estate Tax, FHA Loan. All five were
  484-line template-tier pages; all five are now custom-built 3-card pattern
  pages. Per-page detail is in the individual commit messages; what follows
  is what carried across the batch and is worth reusing.

  **Tooling built this session and kept in the sandbox scratch dir** (not in
  the repo, per the no-clutter rule). Three pieces did most of the work and
  are worth rebuilding next time rather than hand-rolling each page:
  1. `builder.py` — pulls head/header/footer from apr-calculator, swaps the
     meta values, and emits the shared grid/article CSS. Crucially it
     generates the FAQPage schema and the visible FAQ markup **from one list
     of (question, answer) tuples**, which makes the schema-vs-visible
     mismatch bug that hit four previous sessions structurally impossible
     rather than something to catch in review. All five pages passed 8/8
     exact match on the first try as a result.
  2. `verify_page.py` — static gate: JSON-LD validity, FAQ match, duplicate
     ids, tag balance, protected style block byte-compare, H1 bold, wrapper
     padding, unconditional-jsPDF detection, `node --check` on every inline
     script, internal links resolving to real directories, meta length, H2
     count. Caught three dead sidebar links and two id collisions before any
     browser was opened.
  3. `audit.py` — Playwright harness taking a per-page checks module, run on
     desktop and mobile: console/page errors, horizontal overflow, H1 weight,
     jsPDF-not-loaded-before-click, article-vs-grid alignment, and a real PDF
     download.

  **Two recurring bug classes were fixed at the tooling level, not per page:**
  - Article heading anchors now carry an `-a-` namespace (`#dep-a-formula`),
    because plain topic anchors kept colliding with form input ids of the
    same name and producing duplicate-id failures.
  - The audit harness filters sandbox-blocked Google Analytics beacons, which
    were surfacing as a 503 console error and reading like a page bug.

  **Verification standard applied to every page**: math written and checked in
  Node *before* being wired in, and wherever possible cross-checked against a
  figure published by an established source, so the check is against an
  outside answer rather than my own arithmetic:
  - Depreciation — MACRS percentages derived from the underlying rules rather
    than hard-coded, then matched against published IRS Pub. 946 tables for
    all six GDS classes (3/5/7/10/15/20-year), every schedule summing to 100%.
  - Discount — stacked-discount result matched calculator.net's own worked
    example (\$279 at 20% then 15% = \$189.72).
  - Down Payment — monthly payment matched a published SmartAsset example
    (\$600k at 20% down, 6.59%, 30yr = \$3,062).
  - Estate Tax — 2026 figures corroborated across eight independent legal and
    CPA sources citing IRS Rev. Proc. 2025-32 and OBBBA P.L. 119-21 s.70106.
  - FHA — every figure matched a lender's own published worked example
    (lower.com: \$386,000 base, \$6,755 UFMIP, \$2,482.48 P&I, \$176.92 MIP).

  **Real bugs the audits caught before commit** (all fixed): negative headline
  figures when salvage exceeded cost or asset cost was zero (Depreciation); a
  completed savings goal rendering as "Not required" because a PMI-oriented
  month formatter was reused where zero means success (Down Payment); plus
  the dead links and id collisions noted above.

  **Competitive positioning found during research**, since this is the part
  that decides whether a page can rank rather than just exist:
  - Depreciation: calculator.net has no MACRS at all, despite MACRS being what
    the IRS requires on US returns and having a large dedicated-page keyword
    cluster. Biggest single gap found in the batch.
  - Discount: calculator.net splits this query across two pages (discount and
    percent-off); both are covered here, plus reverse solving and BOGO.
  - Down Payment: calculator.net mentions PMI but never prices it or says when
    it ends.
  - Estate Tax: calculator.net has no equivalent page; benchmarked against the
    real competing set instead. A lot of live content still wrongly warns the
    exemption halves in 2026, which the article corrects explicitly.
  - FHA: calculator.net explains the 11-year vs life-of-loan MIP rule but does
    not price the consequence or compare against conventional.

  **Site-wide regression after the batch**: the five new pages plus
  debt-consolidation, apr, auto-loan, body-fat and bmi all load with zero
  console errors, zero horizontal overflow, and correct nav behaviour on both
  desktop and mobile — confirming nothing shared was disturbed.

- **Future Value Calculator rebuilt** (Aug 1, 2026): 484-line template-tier
  page (lump-sum only, generic `X Calculator | CalculatorBoss` title, 3 H2s,
  2 FAQs, no PMT field at all) → 1,053-line custom-built 3-card page with the
  `fv-` prefix.

  **Parity (3a-PRIME, calculator.net/future-value-calculator.html)**: their
  raw form HTML was fetched and parsed rather than eyeballed — it has exactly
  five inputs (`cyearsv` 10, `cstartingprinciplev` 1000, `cinterestratev` 6,
  `ccontributeamountv` 100, `ciadditionat1` radio defaulting to `end`), no
  Advanced section and no tab/mode variants. All 5 mapped 1:1; the
  beginning/end radio became a segmented tab control per the standing
  "tabs, not dropdowns" directive. Result parity 12/12: Future Value,
  PV (Present Value), Total Periodic Deposits, Total Interest, the 3-segment
  donut, the 5-column schedule (Start balance / Deposit / Interest /
  End balance) and the 3-series stacked bar chart.

  **Numeric verification** (Node, before any code was wired in): every figure
  calculator.net publishes on that page reproduces to the cent — FV
  $3,108.93, PV $1,736.01, deposits $1,000.00, interest $1,108.93, donut
  32/32/36, and schedule rows 1/2/10 ($60.00→$1,160.00, $69.60→$1,329.60,
  $170.32→$3,108.93), plus their own doc example ($10 at 6% for 1 period =
  $10.60). The period-by-period simulation and the closed-form
  `PV(1+i)^N + PMT[((1+i)^N-1)/i](1+iT)` were computed independently and
  agree, which is what the page ships (the schedule is built the long way, so
  the two act as a permanent cross-check). Zero-rate falls back to
  `PV + PMT*N` = $8,750.00 rather than dividing by zero; annuity-due mode
  verified separately at $3,188.01 with period-1 interest of $66.00.
  Defaults deliberately differ from theirs: 15 / $5,000 / 7% / $250.

  **Keyword research**: head term "future value calculator" is high-volume /
  high-competition (calculator.net, CalculatorSoup, Symbolab, Omni,
  FinancialMentor). Distinct long-tail clusters with their own dedicated
  competitor pages — so real query clusters, not phrasing variants — are
  "future value of annuity calculator", "future value of annuity **due** /
  ordinary vs due", "future value formula", "future value with monthly
  deposits" and "lump sum future value". The middle-ground opportunity taken:
  calculator.net *has* the beginning/end toggle but says nothing about it in
  its title or meta, and only small sites target the annuity-due phrasing —
  so it got its own H2 and FAQ here. Title
  "Future Value Calculator — See What Your Money Grows To" (54 chars),
  meta 154 chars.

  **Content**: 9 H2 sections, 2,455 words, 8 FAQs, all original. Every number
  quoted in the prose was computed in Node first, not estimated — the
  $13,795.16 / $6,282.26 lump-vs-deposits split (which sums exactly to the
  $20,077.41 default), the $439.76 annuity-due gap, the $49,163.80 monthly
  conversion against the $3,954.24 wrong-units answer, the period-12
  interest-overtakes-deposit crossover at $276.21, and the $12,886.93
  inflation-adjusted figure.

  **Two things worth reusing next time.**
  1. *Generate the FAQ schema and the visible FAQ from one Python list.*
     The recurring em-dash/quote drift between schema and visible text
     (flagged in the guide as hitting every rebuild so far) cannot happen if
     both are emitted from the same source string. 16/16 exact-equality
     assertions passed on the first run with no manual reconciliation.
  2. *Build the OG image against measured geometry, not by eye.* The template
     was reverse-engineered from `og/annuity-payout-calculator.png`: element
     bounding boxes and exact colors sampled per-pixel, and the background's
     green radial wash recovered by least-squares fitting a 2D polynomial to
     the text-free rows (max error 3/255, visually identical). A first
     attempt at building a clean background plate by taking the per-pixel
     median across all 42 existing OG images failed and was abandoned —
     the images vary too much in layout, so the median erased the shared
     template elements (pill fill, divider, footer) too.

  **Bug caught by the checks, not by reading**: the tail slice that splices
  the shared footer back on was off by four lines and silently dropped
  `</div></main><footer>`, leaving the page with no `</main>` and two
  unbalanced divs. Nothing visual gave it away — it surfaced only as a
  68-open/70-close div count. Worth keeping the tag-balance assertion in the
  standard check set; it is cheap and it caught a real structural break.

  **Verification before push**: 3 JSON-LD blocks valid, FAQ schema ↔ visible
  HTML 16/16 exact match, all 6 inline scripts `node --check` clean, the
  PROTECTED SHARED STYLE BLOCK byte-identical to finance-calculator and
  body-fat-calculator (sha256 `d2dadb0c…`, 20,166 bytes), header and footer
  partials byte-identical to the reference page, TOC anchors matching H2 ids,
  tag balance clean. Playwright on desktop (1280×900) and mobile (390×844):
  zero console/page errors, zero horizontal overflow, no element wider than
  the viewport, `h1` computing 700, every card heading measured for contrast
  against its resolved background (the Jul-31 vanishing-heading lesson),
  the full calculator.net parity case re-run in-browser, and jsPDF confirmed
  to fetch zero bytes on load, load on first click and not re-fetch on the
  second. Site-wide regression across future-value, finance, present-value,
  bmi, tip, body-fat, home and all-calculators on both breakpoints: clean.

  **Post-build accessibility pass** (same session, following the convention
  set by the Jul 31 "Restore post-build accessibility and text-size fixes"
  commit rather than inventing a new remedy): no text below 12px anywhere on
  the page — `.fv-note` and `.fv-chart-legend` went 11.5px → 12px, the bar
  badge 11px → 12px, and both SVG chart renderers' axis/label text 11 → 12;
  TOC links given `padding:7px 0; min-height:32px` so they clear a 32px tap
  target; schedule `<th>`s given `scope="col"`. Re-audited after: 0 elements
  under 12px, 0 inputs without an accessible name, 0 SVGs without a role or
  aria-label, 0 elements with clipped or overflowing text.

  **Outstanding, site-wide, NOT introduced here — shared-token colour
  contrast.** A WCAG AA sweep found 6 failing text/background pairs on this
  page: the input unit suffixes ("$", "% / period") and `.fv-hint` /
  `.fv-note` / chart-card kickers at `var(--ink-faint)` on white (2.06–2.33
  against a 4.5 requirement), the sidebar's white-on-`#22C55E` "View More"
  button (2.28), the SVG axis labels (3.30) and the breadcrumb links (3.66).
  The same probe run against untouched pages returns finance-calculator 6,
  sales-tax-calculator 5, bmi-calculator 4 — i.e. this comes from the shared
  design tokens and the shared `.crumb` / view-more patterns, and this page
  sits exactly where its reference pages do. Deliberately left alone: fixing
  it on one page only would make that page visibly inconsistent with ~199
  others, and fixing it properly means darkening `--ink-faint`/`--muted` and
  the view-more green across the whole site, which is a shared-token change
  that section 1 says must be propagated everywhere and spot-checked before
  pushing. Worth doing as its own focused task — it is a real accessibility
  gap, and Google's page-experience signals care about it — but it should not
  be smuggled in under a single calculator rebuild. The two remaining
  sub-32px tap targets are the shared breadcrumb links, same reasoning.

  **Still outstanding for this slug**: `present-value-calculator` is still a
  484-line template-tier page. Checked per the AdSense no-over-claiming rule:
  the new article makes no claim about it — the article's only links are its
  own TOC anchors, and the sidebar lists it by name with no feature promise,
  so nothing needs correcting. It is still the obvious next upgrade, and the
  two pages should end up as a matched pair.

- **GDP Calculator rebuilt** (Aug 1, 2026): 484-line template-tier page →
  1,052-line custom-built 3-card page with the `gdp-` prefix and two tabs.

  **The gap that mattered**: the old page implemented only the expenditure
  approach — its title literally said so — while calculator.net has *two*
  calculators on that URL. Half the tool was missing, not half the polish.

  **Parity (3a-PRIME, calculator.net/gdp-calculator.html)**: their form HTML
  was fetched and parsed rather than read off the page, confirming two
  separate forms with 13 inputs between them and no defaults at all (every
  field ships blank). Expenditure: personal consumption, gross investment,
  government consumption, exports, imports. Income: employee compensation,
  proprietors' income, rental income, corporate profits, interest income,
  indirect business taxes, depreciation, net income of foreigners. All 13
  mapped 1:1 and split across two tabs rather than two stacked forms.

  **Numeric verification**: rather than trusting the published formulas,
  both of their forms were actually submitted over HTTP and the returned
  result tables captured, then reproduced in Node — expenditure
  (12000/3500/2800/1500/2100) returns 17,700 on both sides, and income
  (9000/1400/600/2200/800/1300/2500/-300) returns GNP 14,000 and GDP 17,500
  on both sides. Their result table shows GNP as an intermediate subtotal, so
  ours does too. Cross-checked independently against a textbook example that
  reaches 602 by both routes, plus trade-deficit, trade-surplus, negative-NIF
  and all-zero edge cases. Defaults were then chosen so the two approaches
  reconcile to exactly 22,800, which makes the accounting identity visible
  the moment the page loads.

  **Two additions beyond calculator.net, both flagged as intentional.**
  1. A *Both Approaches Compared* card that reports expenditure GDP, income
     GDP and the difference between them, labelled as the statistical
     discrepancy. calculator.net runs its two forms in complete isolation and
     never reconciles them, yet "both approaches give the same answer" is the
     single point every textbook makes about GDP. It is the page's main
     differentiator and it costs nothing, since both figures are already
     computed.
  2. An optional population field yielding GDP per capita, hidden behind a
     "+ Per capita (optional)" expander so it does not clutter the parity
     fields. This targets a real, separately-served query cluster — Omni,
     Calculator Academy and others all run dedicated GDP-per-capita pages.

  **Keyword research**: the audience here is students, not consumers — the
  head term "gdp calculator" surfaces AnalystPrep (CFA), Study.com and
  course material rather than finance brands, so the title promises the
  working rather than a financial outcome: "GDP Calculator — Both Formulas
  With Every Step Shown". Distinct clusters each with dedicated competitor
  pages (so genuine clusters, not phrasings): "gdp formula" / "how to
  calculate gdp", "expenditure approach" vs "income approach", "gnp
  calculator" / GDP vs GNP, "real gdp calculator" and the GDP deflator,
  "gdp growth rate calculator", "gdp per capita calculator". Real GDP,
  growth rate and per capita are separate tools elsewhere, so they are
  covered as article sections and FAQs rather than bolted on as fields.

  **Content**: 9 H2 sections, 2,394 words, 8 FAQs, all original, including an
  explicit section on why the two approaches must agree and a candid
  "what GDP leaves out" section (unpaid work, distribution, depletion,
  quality change, the informal economy).

  **Two stale claims elsewhere on the site, found and fixed** — both were
  accurate before this rebuild and became wrong because of it, which is
  exactly the AdSense no-over-claiming case in section 10 read in reverse:
  `all-calculators` described the page as "Estimate Gross Domestic Product
  using the expenditure method", and `llms.txt` listed it as "GDP Calculator
  — Expenditure Approach". Both now mention both approaches. Worth making a
  habit: after adding a capability to a page, grep the hub page and
  `llms.txt` for that slug, because a description that was true yesterday can
  be the thing that under-sells the page today.

  **One real fix surfaced by the automated check**: the two form section
  kickers ("Income components", "Adjustments") were on `var(--ink-faint)`,
  which is fine for a decorative chart label but too weak for a structural
  form label. Moved to `var(--ink-soft)`, an existing token — no new colour
  invented and no shared token touched. Note the check initially reported
  them as invisible for the wrong reason: they were measured while the
  income tab was hidden, so width was 0. The probe now switches tabs before
  measuring — a reminder that a visibility assertion has to be run in the
  state where the element is actually supposed to be visible.

  **Verification before push**: 3 valid JSON-LD blocks, FAQ schema ↔ visible
  HTML 16/16 exact match (same single-source generation as the Future Value
  page), all 6 inline scripts `node --check` clean, PROTECTED SHARED STYLE
  BLOCK byte-identical across gdp / future-value / finance / bmi
  (`d2dadb0c…`), header and footer partials byte-identical, tag balance clean
  (122/122 divs), TOC anchors matching H2 ids. Playwright desktop + mobile:
  both calculator.net parity cases re-run in-browser, tab switching swaps
  field sets, GNP subtotal present, per-capita row appears and disappears
  correctly, Clear restores defaults, no text under 12px, every input has an
  accessible name, `th` carries `scope`, all card headings contrast-checked
  in their visible state, zero console errors, zero horizontal overflow, and
  jsPDF fetching nothing until first click and not re-fetching after. New OG
  image generated from the same measured template. Site-wide regression
  across 8 pages on both breakpoints: clean.

  **Usability pass, same session, after the owner asked whether the page was
  actually easy to use.** Re-reading the build from a visitor's point of view
  rather than a parity checklist's found three things worth fixing, one of
  them a genuine defect that every automated check had passed:

  1. **The cross-check card accused users of mistakes they had not made.**
     Both tabs ship with example figures. A visitor who filled in only the
     expenditure tab with their own numbers had those compared against *our*
     untouched income examples, and the card then reported a discrepancy and
     told them "a component is missing or entered in the wrong units". The
     feature meant to teach the identity was instead alarming people about a
     gap they had no part in creating. Fixed by tracking which approach the
     visitor has actually edited: untouched, the card frames the match as our
     example; one side edited, it shows "not entered yet", no invented
     discrepancy number, and a neutral prompt naming the tab still to fill;
     both edited, it does the real comparison. Clear resets the state. This
     is worth remembering as a class of bug — **a feature that compares two
     things must know which of them the user actually supplied**, or it will
     confidently report nonsense about its own defaults.
  2. **GDP per capita returned a meaningless number.** GDP entered in
     billions (22800) divided by a real head count (250,000,000) gave
     $0.000091, which reads as a broken calculator. Added a "Figures are in"
     segmented control (plain units / millions / billions) that labels the
     headline result and converts per capita to plain currency, so billions
     with a 250m population now gives $70,800. Where the per-head figure
     still lands under $1 with a large population, the warning banner names
     the likely cause rather than showing a silent $0.00.
  3. **Two different percentages for the same thing.** The donut legend gave
     each component's share of the positive components while the breakdown
     table gave its share of GDP — two denominators side by side for the same
     items. The donut legend now shows amounts and the table alone owns the
     percentages, and the donut's note explains a negative component rather
     than burying it in a generic footnote.

  Deliberately not changed: **Clear** refills the example values rather than
  emptying the fields, which does not match calculator.net and arguably does
  not match the word "clear" either. It is the established behaviour on every
  3-card page on this site, so changing it here alone would be a worse
  inconsistency than the mismatch itself. If it is ever revisited it should
  be revisited site-wide.

  **Still outstanding for this slug**: nothing on parity. Worth considering
  later — a dedicated real-GDP / GDP-deflator tool and a GDP growth-rate
  tool are each their own query cluster with dedicated competitor pages, and
  are currently only covered as prose here.

- **HELOC Calculator rebuilt** (Aug 1, 2026): 484-line template-tier page →
  1,219-line custom-built two-tab 3-card page with the `hel-` prefix.

  **Scope decision made first: their rate table is advertising, not a
  feature.** The owner asked directly whether the lender comparison table on
  calculator.net's HELOC page ("Compare Home Equity Rates", Advertiser
  Disclosure, NMLS numbers, View Details buttons) is a user feature or
  monetisation. It is monetisation, and the page source proves it rather than
  the layout suggesting it: the table is injected by
  `widgets.icanbuy.com/...?siteid=77c21319f69f80e0`, a third-party
  lead-generation widget carrying their own site ID, alongside
  `securepubads.g.doubleclick.net/tag/js/gpt.js` for Google Ad Manager. That
  is why the disclosure text does not appear in the static HTML at all.
  Excluded from parity scope, and it should stay excluded: we hold no
  licensed rate feed, so reproducing it would mean publishing invented
  interest rates on a YMYL page. **Generalisable check for future parity
  work: before treating a block on a competitor page as a feature, grep the
  page source for third-party widget and ad-tag script hosts.** A Playwright
  assertion now guards the page against any of that content reappearing.

  **Parity (3a-PRIME)**: 11 inputs across their two calculators, taken from
  the raw form HTML — loan amount, interest rate, draw period, repayment
  period, the closing-costs-and-fees section (amount with a $/% selector,
  paid-upfront vs deducted-from-loan, annual fee), and the borrowing-power
  calculator (home value, mortgage balance, LTV limit with six options). All
  11 mapped; their checkbox became our standard expander and their radios and
  dropdown became segmented controls, same states either way.

  **Numeric verification — their forms were submitted, not read.** The
  screenshots only show the base case, and submitting the form over HTTP
  revealed that enabling closing costs *adds result rows the screenshots
  never show*: Cash received (deduct mode only), Closing costs (shown in %
  mode), Total annual fees, Cost of loan and APR. All reproduce exactly:
  draw payment $333.33, repayment payment $477.83, total of 240 payments
  $106,008.69, total interest $56,008.69, donut 47/53, schedule years 1, 6
  and 7 to the cent, total annual fees $250.00 (which is what revealed the
  fee is counted for the draw years only, not the full term), cost of loan
  $58,258.69, cash received $48,000.00, 4% resolving to $2,000, and the
  borrowing calculator's $230,000 and 41.7%.

  **The APR is a deliberate, evidenced deviation.** Theirs returns 8.755%
  where the standard method gives 8.555%. Roughly twenty conventions were
  tested (fee timing, net-proceeds basis, rounded vs exact payments, term
  length) and none reproduced it. What did fit, consistently across two
  independent data points — 8.771% vs their 8.755% at $2,000 closing, and
  8.422% vs their 8.407% at $1,000 — is discounting **only the 180
  repayment-period payments and omitting the 60 interest-only draw
  payments**. That contradicts their own "Total of 240 payments" row, and
  dropping sixty real payments from the cash-flow overstates the rate. Ours
  discounts the whole stream, per the standard definition. Flagged in the
  step-7 report, explained in a dedicated paragraph on the page, and the test
  suite asserts 8.555% with a comment recording why it differs. This is the
  FHA-MIP precedent applied a second time: match the field, not the error.

  **Two additions beyond calculator.net.** An LTV scenario table on the
  borrowing tab running all six limits against the same home, since the LTV a
  lender accepts is one of the few variables here worth shopping around for;
  and a monthly schedule alongside the annual one, with the first
  amortizing month marked, because the payment jump is the thing people
  come to this page for.

  **Keyword research**: head term "heloc calculator" is competitive
  (Bankrate, credit unions, mortgage.com). Every serious source converges on
  two themes that shaped the page — the payment shock when the draw period
  ends, and that HELOC rates are variable. The title leads on the first
  ("See Your Payment Before and After Draw") and the article and disclaimer
  are explicit about the second, since holding the rate fixed is this
  calculator's largest simplification. Distinct clusters covered as sections
  and FAQs: heloc payment / repayment / payoff, how much can I borrow,
  heloc vs home equity loan vs cash-out refinance, heloc APR.

  **Content**: 9 H2 sections, 8 FAQs, all original, including a risks section
  that states plainly what the tool cannot show (variable rates, gradual
  draws, the home as collateral, lines being frozen when values fall, and
  conditional interest deductibility).

  **Verification before push**: 3 valid JSON-LD blocks, FAQ schema ↔ visible
  HTML 16/16 exact match, all 6 inline scripts syntax-clean, PROTECTED SHARED
  STYLE BLOCK and header/footer partials byte-identical, tag balance clean,
  all six sidebar link targets confirmed to exist on disk. Playwright desktop
  and mobile: every parity figure re-run in-browser, annual and monthly
  schedules (240 rows, month 1 pure interest, month 61 amortizing, final
  month clearing to zero), both closing-cost modes, % mode, the LTV table and
  its highlighted row, the over-leveraged case flooring at $0 with a warning,
  zero-rate and zero-draw edge cases, no text under 12px, every input named,
  `th` scoped, headings contrast-checked, and jsPDF lazy on first click only.
  `llms.txt` updated from the now-incomplete "Draw Period" label. New OG
  image. Site-wide regression across 8 pages: clean.

  **Layout fixes after the owner spotted cut-off text.** Three things were
  clipping their own boxes, and only one of them was visible in the
  screenshot that prompted the check:
  - The six-option LTV segmented control needed 192px in a 168px column, so
    "60%" was sliced in half. Replaced with a dropdown at the owner's
    request. The standing "tabs, not dropdowns" convention holds for two or
    three modes; six numeric options in a narrow form column is where a
    select is simply the right control.
  - The closing-cost toggle ("Paid upfront" / "Deducted from loan") needed
    209px in the same 168px column and was clipping too, unnoticed. Second
    label shortened to "Deducted", which the row label already contextualises.
  - The donut legend put label and value on one flex row with the value set
    `white-space:nowrap`, so a long label squeezed the percentage off the
    edge. Rebuilt as a two-column grid with the value on its own line
    underneath, which makes clipping structurally impossible rather than
    dependent on label length. The same fragile pattern was on the GDP page
    and was measured to be clipping slightly there too, so both were fixed.

  **Permanent guard added to both suites**: an assertion that walks every
  element under `main` and fails if `scrollWidth` exceeds `clientWidth` while
  `overflow-x` is visible. Cheap, and it would have caught all three of these
  before they shipped. Worth adding to the standard check set for every page.

  **One environment note for next session**: the shared Google Analytics
  beacon returns 503 from this sandbox IP after enough test runs, and shows
  up as a console error on *every* page including untouched ones. Confirmed
  against finance-calculator and bmi-calculator before excluding it. The
  HELOC suite ignores that one third-party host by name rather than
  blanket-ignoring console errors, so real page errors still fail the run.

- **Internal links were causing a 301 hop on every click** (found Aug 1, 2026
  while auditing the HELOC page against the section 3 checklist). The
  sidebar "Related Calculators" links are written without a trailing slash
  (`/loan-calculator`), but the site serves and canonicalises the
  trailing-slash form, so every one of them redirects: confirmed live with
  `curl -L`, which reports `num_redirects=1` for `/amortization-calculator`
  and `0` for `/amortization-calculator/`. Harmless for visitors, mildly
  wasteful for crawlers, and trivially avoidable. Fixed on the three pages
  rebuilt this session (heloc, gdp, future-value). **This is a site-wide
  pattern inherited from finance-calculator and worth a dedicated pass** —
  unlike the shared-token contrast issue, this one has no visual or
  consistency downside at all, so it can safely be scripted across every
  page in one commit.

- **Naming convention settled for acronym calculators** (Aug 1, 2026, HELOC).
  The owner asked whether "Home Equity Line of Credit (HELOC) Calculator"
  would be better for SEO than "HELOC Calculator". Checked what the
  top-ranking US pages actually do rather than reasoning about it: Bankrate
  runs the long form in both title and H1; calculator.net and mortgage.com
  both run the **short form in the title and the long form in the H1**. Two
  of three treat title and H1 as different jobs, which is the sensible read —
  the title's ~60 characters are scarce and have to win a click, while the
  H1 never appears in the SERP and can carry the longer variant for free.
  Applied: H1 became "Home Equity Line of Credit (HELOC) Calculator" and the
  WebApplication schema name matches it; the title, URL slug and breadcrumb
  label all stay on the short high-volume form. The subhead was reworded
  because it had been carrying the long form and now read as an immediate
  repetition of the H1. **Use this split for any future acronym calculator**
  (APR, BMI, GDP, IRR, LTV, RMD, TDEE and so on): short form in title, URL
  and breadcrumb, expanded form in the H1. Measured before shipping — the
  longer H1 stays on one line at desktop, two at 390px and three at 360px,
  with no clipping.

- **Home Equity Loan Calculator rebuilt** (Aug 1, 2026): 484-line template-tier
  page → 1,172-line two-tab 3-card page with the `heq-` prefix. Built directly
  after the HELOC page, and the two are deliberately treated as a pair.

  **Same ad exclusion, verified again.** calculator.net's home-equity-loan
  page carries the identical `widgets.icanbuy.com/...?siteid=...` lead-gen
  widget and `doubleclick` ad tag as its HELOC page. Excluded on the same
  grounds and guarded by the same test assertion.

  **Parity**: 9 inputs across their two forms. One detail that only shows in
  the raw HTML: the closing-cost radio defaults to **deducted from loan**
  here, whereas the HELOC page defaults to *paid upfront*. Ours matches each
  page's own default rather than assuming they are the same. There is no
  annual-fee field on this calculator, unlike HELOC. Result rows again only
  appear once closing costs are enabled (Cash received, Closing costs, Cost
  of loan, APR), which the screenshots do not show — their form was submitted
  in all four modes to find them.

  **Numeric verification**: monthly $1,433.48, total of 180 payments
  $258,026.06, total interest $108,026.06, donut 58/42, schedule years 1, 2
  and 15 (clearing to $0.00) all to the cent, cost of loan $115,526.06, cash
  received $142,500.00, 5% resolving to $7,500, and $230,000 at 41.7% on the
  borrowing tab.

  **The APR here matches calculator.net exactly at 8.860% — and that is the
  useful finding.** On this page, with a single term and no draw period,
  their APR is the standard net-advance IRR and agrees with ours to three
  decimals. It only diverged on the HELOC page. That independently confirms
  the diagnosis recorded in the HELOC entry: their HELOC APR drops the
  interest-only draw payments from the cash-flow, and the deviation shipped
  there was correct rather than a difference in convention. **Worth
  remembering as a technique — when a competitor's figure cannot be
  reproduced on one page, check whether the same figure reproduces on a
  simpler sibling page before concluding anything about the method.**

  **Duplicate-content guard.** This page and `/heloc-calculator/` cover
  adjacent topics and would be easy to write as near-duplicates. The article
  was written from a different angle throughout (second-lien position,
  subordination, the lump-sum-from-day-one consequence, term length as the
  main lever) with a different FAQ set. Measured after writing: 8-word
  shingle overlap between the two articles is 1.32% Jaccard / 2.66%
  containment, and the only shared phrases are the boilerplate disclaimer.
  **This shingle check is worth running whenever two sibling calculators are
  built in the same session.**

  **Reuse note**: the page CSS is extracted from `build_heloc.py` at build
  time and prefix-swapped rather than copied, so the sibling pages cannot
  drift apart visually. Confirmed zero leftover `hel-` references in the
  output.

  **Verification before push**: 3 valid JSON-LD blocks, FAQ schema ↔ visible
  HTML 16/16, scripts syntax-clean, protected style block and header/footer
  byte-identical, tag balance clean, hub description and `llms.txt` entry
  both updated (the hub had omitted the borrowing calculator, `llms.txt` had
  no descriptor). Playwright desktop and mobile: all parity figures re-run
  live, annual and monthly schedules, all closing-cost modes, LTV table,
  over-leveraged and zero-rate edges, the clipping guard, accessibility
  checks, jsPDF lazy. New OG image. Site-wide regression across 8 pages
  clean.

- **House Affordability Calculator rebuilt** (Aug 1, 2026): 484-line stub →
  1,154-line two-tab page (`haf-` prefix). The most involved parity job so far:
  18 inputs, nine $/% unit toggles, a 12-option DTI standard, and a fee
  checkbox.

  **Same ad exclusion** — their page carries the same icanbuy lead-gen widget
  and doubleclick tag, guarded by the standing assertion.

  **The whole engine was reverse-engineered from their outputs and matched
  first try.** Housing allowance = min(income x front-end, income x back-end −
  other debts); price = allowance ÷ [(1 − down%) × M + (tax% + ins% + HOA%)/12].
  Every published figure reproduces: $409,354 price, $327,483 loan, $81,871
  down, $12,281 closing, $94,152 at closing, 28%/28% DTI, $2,118 payment,
  $6,140 tax, $2,047 insurance, $6,140 maintenance, $3,312 total monthly; the
  back-end-binding case at $307,016 with 21%/36%; the 10%-down PMI case at
  $356,157 with $134/mo; and both budget-tab cases, $432,631 with fees and
  $676,541 without.

  **Two structural facts only visible from submitting their form**: maintenance
  (1.5%) is shown in the total monthly cost but deliberately *excluded* from
  the DTI ratio, and PMI is 0.5%/yr of the loan applied below 20% down.

  **Three deliberate corrections, all evidenced.**
  1. *VA funding fee.* They show it as a monthly charge. It is a one-time fee
     with no ongoing component — confirmed against 2026 sources including
     Rocket Mortgage — at 2.15% under 5% down, 1.50% from 5%, 1.25% from 10%
     for first use. Ours puts it in the closing costs. Their own VA numbers
     are additionally self-inconsistent: the price is solved using roughly a
     0.75%-of-loan annual charge while the display shows 1.25%, so their
     stated "front-end 31%" does not match their own displayed costs (32.4%).
  2. *FHA monthly MIP* is excluded from their front-end ratio; FHA
     underwriting counts it, so ours does, which lowers the FHA figure
     slightly.
  3. *PMI in dollar-mode down payments.* Theirs shows PMI at a 23.6% down
     payment entered in dollars. Ours compares the actual down-payment
     percentage against 20%, so it correctly shows none.

  **Two internal-consistency fixes found by the checks**: the result column
  mixed whole dollars and cents (`$2,117.74` beside `$6,140`) which read as
  sloppy — now whole dollars throughout, matching calculator.net and itself;
  and the `.haf-per` unit hints were 11.5px, caught by the sub-12px assertion.

  **Form layout fixed after the owner looked at the rendered page.** On desktop
  the label column was 196px of a 400px card, and the remaining row had to hold
  the input, a $/% toggle and a suffix chip. The inputs were crushed to 61px,
  43px and — for monthly debt — **16px**, hiding most of the typed value:
  "145000" displayed as "14500". Fixed by stacking the label above the control
  row for this page, which gives every input the full card width (219–334px
  now). Number spinners hidden, and a wheel handler added so a focused
  `type=number` field cannot be silently changed by scrolling past it.

  **The check that should have caught it, and now does.** The existing clipping
  guard walks elements comparing `scrollWidth` to `clientWidth`, but an
  `<input>` whose value overflows its box does not report as clipped in that
  sweep — the text is simply hidden inside the field. A separate assertion was
  added to **all five** suites: no `main input` may have `scrollWidth >
  clientWidth`. Re-measured across every page built so far — only the
  affordability page was affected, because it is the only one putting label,
  input, unit toggle and suffix on a single row. **Worth keeping in the
  standard check set: element clipping and input-value clipping are two
  different measurements.**

  **Duplicate-content measured** against both sibling pages built earlier the
  same day: 0.95% containment vs the HELOC article, 1.00% vs home-equity-loan.

  **Verification**: schema 16/16, scripts clean, protected block and partials
  byte-identical, tag balance clean, all six sidebar targets confirmed on
  disk, hub description and `llms.txt` descriptor both updated. Playwright
  desktop and mobile: every parity figure re-run live, dollar/percent toggles,
  FHA and VA modes, budget tab with and without fees, rate-sensitivity table,
  clipping guard, accessibility checks, jsPDF lazy. New OG image. Site-wide
  regression clean.

- **Inflation Calculator rebuilt** (Aug 2, 2026, ad-hoc user request): 484-line
  template stub → 1,298-line three-tab page (`inf-` prefix).

  **The old page did not work at all.** It was a static React snapshot with no
  calculator JavaScript and no CPI data anywhere in the file — the inputs were
  inert and the "result" (`$186.96` for $100 in 2000) was hardcoded in the
  HTML, along with a matching hardcoded worked example in the body copy. Any
  visitor who changed a dropdown got the same number back. Worth checking other
  surviving template-tier pages for the same pattern rather than assuming a
  thin page at least computes something; a page can pass a visual skim and a
  "does the tool exist" check while being a picture of a calculator.

  **Data**: BLS series `CUUR0000SA0` (CPI-U, U.S. city average, all items, NSA)
  pulled from `download.bls.gov/pub/time.series/cu/cu.data.1.AllItems`, 1,475
  records covering Jan 1913 – Jun 2026, monthly plus annual averages, embedded
  as an 8.6 KB nested array. Six published figures reproduced exactly on parse
  (Jan 2016 236.916, Jan 2017 242.839, 2024 avg 313.689, 2000 avg 172.2, 1913
  avg 9.9, Jun 2022 296.311), and BLS's annual average confirmed to be the mean
  of the twelve monthly readings.

  **October 2025 has no CPI figure** — BLS never published it (footnote `X`;
  the autumn 2025 shutdown interrupted collection), and the 2025 annual average
  is the mean of the eleven months that exist. Handled explicitly: the month
  appears in the dropdown as a disabled "October (not published)" option rather
  than being hidden or interpolated, and the article explains it. Caught only
  because the parse printed the raw year row; a naive `.get(month)` would have
  returned undefined and produced a silent NaN.

  **Parity** (calculator.net/inflation-calculator.html, live-audited from raw
  HTML, not from the rendered page — the month dropdowns are empty in source
  and populated by an `updateMonths()` script that also encodes their
  `cpiLatestYear`/`cpiLatestMonth` cutoff, which the markdown extraction lost
  entirely). Their page is three separate forms; ours is three tabs:
  `cstartingamount1/2/3` → `#inf-amount`, `cinmonth1`/`coutmonth1` →
  `#inf-fromMonth`/`#inf-toMonth`, `cinyear1`/`coutyear1` →
  `#inf-fromYear`/`#inf-toYear`, `cinrate2/3` → `#inf-rate`, `cinyear2/3` →
  `#inf-years`, plus Calculate/Clear and their historical inflation chart.
  16/16 inputs, 5/5 results, 0 gaps on the final DOM cross-check.

  **Numeric verification ran in the browser against the shipped code**, not
  just in Node, and against four independent published sources rather than only
  calculator.net: their own defaults ($100 Jan 2016 → Jan 2026 = $137.29),
  their own article example (Jan 2016 → Jan 2017 = 2.5%), their forward and
  backward flat-rate defaults ($134.39 and $74.41 at $100/3%/10y),
  CalculatorSoup ($100 Jan 2015 → Jul 2025 = $138.23) and NerdWallet (1990 →
  2010 annual averages = 66.837%). All seven matched to the cent/basis point.

  **A real bug the checks caught**: the first build listed Jul–Dec 2026 as
  "(not published)" because the data row pads unpublished months with `null`,
  which is correct for October 2025 but wrong for months that simply have not
  happened yet. Fixed by walking to the last published month per year and
  omitting anything after it, so only genuine interior gaps stay visible.
  Nothing in the DOM or the numbers flagged this — only an assertion that the
  2026 month list equals exactly `['1'..'6']`.

  **Verification before push**: 3 valid JSON-LD blocks; FAQ schema ↔ visible
  HTML 8/8 exact (both emitted from one Python list, so drift is structurally
  impossible — second build in a row where this needed no reconciliation);
  `node --check` clean; protected style block and header byte-identical against
  four pages (future-value, bmi, tip, body-fat) with only the breadcrumb line
  differing, and that line proved identical apart from the name/URL; tag
  balance clean (67/67 divs, main/footer/article/table/svg all paired — the
  splice bug from the Jul 31 session re-checked); Playwright desktop 1280 and
  mobile 390: 28/28 checks, zero real console errors, zero horizontal overflow,
  jsPDF absent on load and fetched only on click. New OG image.

  **OG image built against measured geometry** again, reusing the method from
  the Jul 31 session: background wash recovered by least-squares fitting a 2D
  polynomial to the text-free pixels of `og/future-value-calculator.png` with an
  outlier-rejection refit (max error 2.07/255), palette sampled per-element, and
  all five element bands verified to land within 2 px of the reference. Two
  things worth noting for next time: IBM Plex is not installed in the sandbox
  and both the GitHub raw paths and jsDelivr are blocked, but `npm pack
  @ibm/plex-sans @ibm/plex-mono` works and fontTools converts the shipped
  `.woff` to `.ttf` for PIL. And PIL's `getbbox()` under-reports the left
  bearing on some glyphs, so text placed by bbox alone landed 3 px off; a
  two-pass helper that renders to a temp bitmap and measures the actual ink
  extents fixed it.

  **Keyword research before any copy** (section 4). Head term "inflation
  calculator" is dominated by Minneapolis Fed, NerdWallet, in2013dollars,
  usinflationcalculator, CalculatorSoup, SmartAsset and calculator.net. The
  pattern worth copying: NerdWallet, CalculatorSoup, usinflationcalculator and
  in2013dollars all put the **year range in the title tag** ("U.S. CPI and
  Dollar Value 1913-2026", "Find US Dollar's Value From 1913-2026"), so the
  range went into ours rather than a bare keyword restate. Middle-ground
  opportunity found and built around: the big sites almost all do historical
  CPI lookup *only*, while the forward-projection cluster ("future inflation
  calculator", "what will X cost in Y years", "purchasing power calculator") is
  served mainly by small sites — covering both clusters on one page is the
  differentiation, and it happens to be exactly calculator.net's three-tool
  structure. Long-tail woven into H2s/FAQs: purchasing power, inflation by
  year, value of money over time, monthly vs annual average, US average
  inflation rate, deflation years.

  **A parity gap the HTML audit missed, caught only by the user's screenshots.**
  The live-fetched source and the markdown extraction both showed the three
  forms and the historical inflation *chart*, so the first build shipped
  without the **full year-by-month inflation rate table** that sits under that
  chart (Year | Jan..Dec | Average, 1914 to date). It is rendered client-side
  from a data blob, so it simply is not in the fetched HTML as a table, and
  nothing in the source hinted it existed. Lesson for the standing protocol:
  a raw-HTML audit is necessary but not sufficient — for any calculator.net
  page, also render it (screenshot or headless browser) before declaring the
  field/output map complete, because their heavier pages build result tables
  and charts in JS. Added as a full-width card under the bottom grid, 113 rows
  x 14 columns, with ten cells spot-checked against the user's screenshots and
  all ten matching. One apparent mismatch, Mar 2026 at 3.26% vs a screenshot
  reading of 3.28%, resolved in favour of the raw BLS series (330.213/319.799
  = 3.2564%); the other five months of 2026 match to the basis point, so it was
  a digit misread at screenshot resolution, not a data difference. October 2025
  renders blank in their table too, which matches our null.

  **The purchasing-power chart was also upgraded to month resolution** to match
  theirs (their graph plots monthly points across the span; ours had plotted one
  point per year). The year-by-year schedule table stays yearly for readability.
  Long spans are downsampled to 420 points so the SVG path stays light.

  **Two site-wide findings, deliberately not changed here** (one page should
  not diverge from ~200 others):
  1. *Contrast below WCAG AA on several shared design tokens.* Measured
     computed colour against effective background: `--ink-faint` body notes,
     hints, chart titles and the byline sit at 2.06–2.33, `.inf-viewmore`
     (white on `#22C55E`) at 2.28, white on the `#16A34A` result header and
     Calculate button at 3.30, breadcrumb links at 3.66. Verified **identical**
     on future-value-calculator and gdp-calculator, so this is the established
     baseline, not a regression introduced here. Worth its own focused pass
     with a propagated token change and spot-checks, like the `llms.txt`
     cleanup already queued.
  2. *Sitemap omits trailing slashes on all 210 `<loc>` entries* while every
     canonical carries one, so each crawled URL takes a 301 hop — the same
     class of issue as the related-calculator links fixed on Jul 31, but at
     sitemap scale. Also its own task.

- **Interest Calculator rebuilt** (Aug 2, 2026, ad-hoc user request): 484-line
  dead stub → 1,207-line page (`int-` prefix). **Second confirmed case of the
  same failure mode as the Inflation Calculator** — no calculator JavaScript at
  all, inert inputs, a hardcoded dollar figure in the HTML. That is now two of
  two template-tier pages inspected. Treat the remaining 484-line pages as
  presumed non-functional until checked; `interest-rate-calculator` was noticed
  in passing at exactly 484 lines and should be looked at next.

  **The big methodological win: their form submits by GET, so their own engine
  can be used as an oracle.** `interest-calculator.html?cstartingprinciple=...`
  returns a fully rendered Results panel and both schedules. That turned parity
  from "read their page and hope" into a measurable exercise: ten scenarios were
  pulled covering every compounding option, beginning/end contributions, tax,
  monthly + annual contributions together, and a years+months term, and the
  engine was fitted against them until all ten matched. Worth checking for this
  on every future calculator.net page — several of their calculators post back
  the same way, and it is far stronger evidence than eyeballing one screenshot.

  **What the oracle exposed about their model**, none of which is guessable from
  the page: the effective annual factor is `(1 + r/n)^n` (or `e^r` for
  continuous), converted to a monthly rate as `EAF^(1/12) - 1`, and the whole
  thing is simulated monthly regardless of the compounding option — which is why
  their monthly schedule shows $101.85 of interest in month 1 on $25,000 at 5%
  compounded *annually* (25000 x (1.05^(1/12) - 1)). The annual contribution goes
  in once a year, at the start of the year when contributing at the beginning and
  at the **end of the year** when contributing at the end. Getting that last
  detail wrong was the first draft's only structural error, and it showed up as
  $54,417.49 against their $53,153.79.

  **Tax mechanics**: interest accrues gross, tax is taken out of each period's
  interest before it is added, so the balance compounds on the net amount. Their
  "Total interest" is the gross figure, which is why raising the tax rate lowers
  total interest as well as the ending balance. Reproduced exactly.

  **A genuine defect in their calculator, matched as a field but not as a bug**
  (per the section 3a-PRIME rule). Their "Interest of initial investment" line
  ignores the tax rate completely. Verified by sweep: at 0%, 25%, 50% and 90%
  tax it returns 5525.63 every single time, while total interest falls from
  9535.20 to 8647.21. Since they force the two "Interest of" lines to sum to the
  total, the entire error is dumped into "Interest of the contributions", which
  at 90% tax is understated by roughly 40%. Ours tracks the initial investment
  and the contributions as separate balances through the same net-growth loop,
  so both lines are correct and still sum exactly to the total. Flagged in the
  step-7 report and explained on the page.

  **Also divergent, but trivially**: on non-annual compounding their two split
  lines differ from ours by 0.14 to 0.31 on figures around 5,000 (0.005%), in
  cases where both sets reconcile to the same total. Their daily and continuous
  compounding return an *identical* split figure (5680.37) despite different
  totals, which suggests a closed-form shortcut on their side. Not chased
  further; ours is derived from the simulation and is self-consistent.

  **Verification**: all ten oracle scenarios re-run through the shipped page in
  a real browser, headline figures matching to the cent in every one. 3 valid
  JSON-LD blocks; FAQ schema 8/8 exact (single-source generation again, third
  build running, still zero reconciliation needed); `node --check` clean;
  protected style block and header byte-identical; tag balance 80/80 divs;
  TOC and headings resolve both ways; Playwright desktop 1280 and mobile 390
  with zero real console errors, no sideways scroll, jsPDF absent on load and
  fetched only on click; annual schedule 9 rows and monthly 102 for the default
  8-year-6-month term. New OG image, all five element bands within 2 px of the
  template.

  **Keyword research**: head term "interest calculator" overlaps almost entirely
  with "compound interest calculator", and this site already has a real
  867-line page on that slug — so the two were deliberately separated rather
  than left to cannibalise. This page is positioned on what the sibling does not
  do: **tax and inflation adjustment**, the annual + monthly contribution split,
  and nine compounding options including continuous. Title built around that
  ("What You Keep After Tax and Inflation") rather than on the raw head term.
  Long-tail woven in: compound interest with monthly contributions, APY /
  effective annual rate, monthly interest, interest after tax, money doubling
  time. Checked the sibling pages before linking to them so no claim describes a
  feature that is not there.

  **Article**: 2,858 words, 11 H2 sections plus FAQ, covering the topics their
  article covers — simple vs compound, the Rule of 72, fixed vs floating,
  contributions, tax rate, inflation rate — written from scratch, plus sections
  they lack on APY, reading the accumulation schedule, and what the calculator
  leaves out. Every figure quoted was computed first: the annual/monthly/
  continuous spread is $448.23, the beginning-vs-end gap is $4,510.92, and the
  Rule of 72 checks (9 vs 9.01 at 8%, 16 vs 15.75 at 4.5%) were verified rather
  than asserted.

- **Interest + Inflation Calculator: rendering fix and SEO pass** (Aug 2, 2026,
  user reported a clipped donut legend from a screenshot).

  **Two rendering bugs, one of them worse than reported.** The user flagged the
  donut legend clipping; the same screenshot also showed the "Contribute at the"
  segmented control rendering as unstyled text reading "BeginningEnd". Cause:
  the interest page's stylesheet was derived from the inflation page's, and the
  inflation page had no segmented control, so `.fv-seg` had been dropped when
  that stylesheet was first written — the interest page then used
  `class="int-seg"` against a rule that did not exist. **Every automated check
  passed with this on the page**: the element existed, was the right size, had
  adequate contrast, and the JS toggle worked. Nothing short of looking at it,
  or asserting on a specific CSS property, would have caught it. Added a check
  that asserts the control has a border, a radius and distinct active/idle
  backgrounds, rather than only that it exists.

  Legend clipping fixed by wrapping the label in a `<span class="t">` with
  `min-width:0` and allowing `.lg` to wrap, so the value drops to its own line
  instead of overflowing. Applied to both pages; verified by measuring each
  value's bounding box against its container at 1280 and 390.

  **SEO pass on the interest page.** Audit was mostly clean: 94.6 KB, zero
  external scripts on load, 1 H1 / 12 H2 / 8 H3, all 17 outbound links valid
  with trailing slashes, registered in sitemap, index, hub and `llms.txt`,
  strong coverage of every target term. Changes made:
  - WebApplication schema enriched on both pages with `dateModified`,
    `inLanguage`, `isAccessibleForFree`, `publisher` and a `featureList` —
    entity and freshness signals, and the feature list is the kind of thing AI
    answer engines quote. No `aggregateRating`: inventing ratings is a policy
    violation, not an optimisation.
  - "Doubling time" surfaced explicitly in the Rule of 72 section; it was a
    real long-tail phrase from the research that the copy talked around.

  **The finding worth acting on next: only 22 of 214 pages have a related-
  calculators sidebar.** This is the exact gap section 1 of the guide flagged
  months ago, and it is the site's single biggest untapped internal-linking
  lever. Both new pages had just 6 inbound internal links each, two of which
  were the hub and the sitemap. Added the topically strongest ones available
  (future-value → interest + inflation, inflation → interest), taking both to
  8. Deliberately did **not** pad with weak matches — home-equity-loan →
  interest was available and skipped, since loan interest and savings interest
  are different intents and a link that does not fit is not worth the equity.
  The real fix is retrofitting the sidebar module onto the ~190 pages without
  one, which is its own project and should not be smuggled into a page build.

- **Interest Rate Calculator rebuilt** (Aug 2, 2026, ad-hoc user request):
  484-line dead stub → 1,151-line page (`irc-` prefix). **Third stub in a row
  with no calculator JavaScript at all.** Three for three now; the presumption
  should be that a 484-line page does not work.

  **This one is a reverse solve, which is a different class of problem.** The
  loan equation `PV = PMT x [1 - (1+i)^-n] / i` has no closed form for `i` — the
  rate sits both as a divisor and inside an exponent. Solved by bisection over
  200 iterations, which is safe here because PV falls monotonically as i rises,
  so the bracket can never straddle a false root. Section 3a's standing rule
  about reverse-solve modes was applied: the solved rate is fed back into the
  **forward** payment formula and returns $355.0000 against an input of $355,
  and the independently-built amortization lands on a balance of exactly zero
  at the final payment. Both cross-checks are asserted in the browser test, not
  just in Node.

  **Oracle again.** Their form submits by GET, same as the Interest Calculator,
  so eight scenarios were pulled covering a 30-year mortgage, a 6-month term, a
  years+months term, a 22% rate, a 0.49% rate and a zero-interest loan. All
  eight match on term length, total of payments and total interest.

  **Intentional difference: ours is the more accurate solve.** On three of the
  eight their rate differs from ours in the third decimal (14.454 vs 14.452,
  9.924 vs 9.923, 26.927 vs 26.931). Substituting each back into the loan
  equation settles it — ours lands within $0.001-$0.14 of the target loan
  amount, theirs within $0.01-$0.25, so ours is roughly ten times closer in
  every divergent case. The divergence grows with the rate, which points at a
  convergence tolerance on their side. Separately, on a loan with no interest at
  all ($12,000 over 24 months at $500) they return **0.001%** where the answer
  is exactly 0; ours returns 0.000% and short-circuits that case before
  iterating.

  **Also handled, which they do not**: payments that never repay the loan. Enter
  $20,000 over 2 years at $100 a month and the page explains that the payments
  total $2,400 against a $20,000 balance rather than returning a number.

  **A real bug the checks caught, and a process fix worth keeping.** The first
  build came out with two `</article>` tags and unbalanced structure. Cause: the
  build scripts spliced the shared scaffold using **hard-coded line offsets**
  (`ref[:352]`, `ref[928:]`) into `future-value-calculator/index.html` — and two
  sidebar links had been added to that file earlier in the same session, pushing
  every line down by two. The tail then started mid-article. Nothing about the
  page looked wrong; only the tag-balance assertion caught it. **All three build
  scripts now locate the splice points by content** (`</header><main`,
  `</div></main><footer>`, the line carrying the title, the BreadcrumbList line)
  instead of by index, and inflation and interest were rebuilt and re-verified
  through their full suites. Any future scaffold edit is now harmless. Worth
  remembering: a build script that reads another live page is coupled to it, and
  fixed offsets are the most fragile possible coupling.

  **Verification**: 8/8 oracle scenarios through the shipped page in a browser,
  30 assertions total; 3 valid JSON-LD blocks; FAQ 8/8 exact; `node --check`
  clean; protected style block byte-identical; tag balance 62/62 divs and
  1/1 article after the fix; TOC resolves both ways; desktop and mobile with
  zero real console errors and no sideways scroll; jsPDF lazy. New OG image,
  bands within 2 px. Meta descriptions on all three pages trimmed into the
  150-160 range (interest-rate 157, inflation 153, interest 154).

  **Keyword research**: the head term "interest rate calculator" is crowded and
  ambiguous — most of what ranks for it is forward loan-payment calculators
  (Bankrate, NerdWallet, CalculatorSoup). The distinct intent for *this* page is
  the reverse one, which calculator.net states outright: car dealers quote a
  payment and not a rate. Title built on that ("Find the Rate Behind Any Monthly
  Payment") with the long-tail cluster woven through the copy and FAQs: what
  interest rate am I paying, find interest rate from monthly payment, reverse
  loan calculator, car loan rate from payment. Article is 2,704 words, 11 H2
  sections plus FAQ, covering their topics (what an interest rate is, simple vs
  compound, fixed vs variable, APR, uncontrollable and controllable factors,
  real interest rate) in original wording, plus sections they lack on reading
  the amortization schedule and what the tool leaves out.

- **IRA Calculator: recheck and rename** (Aug 2, 2026, user asked whether the
  page was correctly named).

  **Health check first — the page itself is fine.** Protected style block
  byte-identical, 109/109 divs, three valid JSON-LD blocks, FAQ 6/6 exact
  against the visible copy, all 17 outbound links resolve, OG image present,
  both tabs compute in a real browser (Grow My IRA returns $1,196,925 and
  Traditional vs. Roth returns "Traditional wins by $103,678"), 35-row
  schedule, zero console errors and no sideways scroll at 1280 and 390, jsPDF
  still absent on load. Nothing was broken.

  **The naming was genuinely inconsistent, in five places at once.** The URL is
  `/ira-calculator/`, `calculators-index.json` (which drives the on-site search
  box) said "IRA Calculator", the title, H1 and visible breadcrumb said
  "Traditional IRA Calculator", the BreadcrumbList schema said just "IRA", and
  `llms.txt` said "Traditional IRA Calculator". The schema/visible breadcrumb
  mismatch is the same class of defect the guide already warns about for
  FAQPage, and it applies to BreadcrumbList too — worth checking on every page,
  not just the FAQ block.

  **Settled on "IRA Calculator"**, on evidence rather than preference:
  calculator.net names this exact slug "IRA Calculator" and keeps a separate
  Roth IRA Calculator, which is the same two-page structure this site has; the
  URL and the search index already used the generic name; and the page covers
  *both* account types across its two tabs, so "Traditional" understated it and
  invited confusion with the pending `/roth-ira-calculator/` page. The higher
  volume also sits with the generic head term. Title now blends all three terms
  rather than picking one, per section 8: **"IRA Calculator — Traditional vs.
  Roth, and What Yours Grows To"** (62 chars, down from 72, which Google was
  truncating). Meta description rewritten to 149 characters and leading with
  both account types.

  Renamed consistently in title, og:title, twitter:title, H1, visible
  breadcrumb, BreadcrumbList schema, WebApplication name and description, the
  PDF report header, and `llms.txt`. Verified afterwards that the visible
  breadcrumb and the schema breadcrumb are now the same string. WebApplication
  schema also brought in line with the pages rebuilt today (`dateModified`,
  `inLanguage`, `isAccessibleForFree`, `publisher`, `featureList`). New OG image
  with the corrected name, bands within 2 px of the template.

  **Note for whoever does queue #5**: `/roth-ira-calculator/` is still a
  484-line stub, and its title is still the generic `X | CalculatorBoss`
  pattern. Now that `/ira-calculator/` is explicitly the Traditional-plus-
  comparison page, the Roth page should be scoped narrowly to Roth-specific
  mechanics — after-tax contributions, the income phase-out, the five-year
  rule, no RMDs — rather than repeating the comparison, or the two will
  compete for the same queries.

- **IRA Calculator: the parity gap the recheck almost missed** (Aug 2, 2026).

  The first pass of the recheck covered structure, function and naming and
  reported the page healthy. It did **not** re-run the field/output parity
  audit, on the assumption that a prior session had done it. Pushed on that
  point, the audit was run properly and found two real gaps. Lesson: "is this
  page OK" means re-running the whole protocol, not the parts that are quick.
  A page can be structurally perfect and still be missing a third of its
  output.

  **Their model, recovered exactly.** Seven inputs, all of which we already had
  (current balance, annual before-tax contribution, expected return, current
  age, retirement age, current marginal tax rate, expected rate in retirement).
  The output is a **three-way** comparison, not two: Traditional/SIMPLE/SEP IRA
  against Roth IRA against **regular taxable savings**, shown before and after
  tax, plus a year-by-year table carrying all three. Their arithmetic:
  Traditional grows pre-tax and is multiplied by (1 - retirement rate); Roth is
  the same gross future value multiplied by (1 - current rate); taxable savings
  starts from after-tax money and pays tax on its gains annually, which is
  exactly a growth rate of `rate x (1 - current tax rate)`. All four of their
  published figures reproduce to the dollar: $1,066,343 before tax, $906,392
  Traditional after tax, $799,758 Roth, $563,434 taxable.

  **Gap 1: the taxable-savings arm was missing entirely.** Ours compared
  Traditional against Roth and stopped. Added as a third column, three extra
  result rows, a line in the verdict and a row in the PDF. It is arguably the
  most useful of the three, since it answers "what does sheltering the money
  actually buy me" rather than the narrower Traditional-versus-Roth question.

  **Gap 2: the comparison silently dropped the current balance.** The code
  comment said "contribution-only, per verified model" — a deliberate earlier
  choice to isolate the tax question. Defensible in itself, but it meant the
  two tabs disagreed: the growth tab projected $1,196,925 while the comparison
  ran on $1,036,777, a $16,015 swing in the headline number with nothing on the
  page explaining why. Now both tabs run on the same money and reconcile
  exactly, which is also what calculator.net does.

  Also updated: the PDF heading still said "same contribution", now corrected,
  and the article gained a paragraph describing the taxable-savings column so
  the copy matches what the page actually shows.

  **Verification**: their four figures reproduced through the shipped page in a
  browser; both tabs asserted to reconcile on the same before-tax balance;
  protected block byte-identical; 113/113 divs; FAQ 6/6 exact; `node --check`
  clean; three compare columns render at 1280 and 390 with no clipped values,
  no sideways scroll and zero console errors; jsPDF still absent on load and
  fetched only on click.

- **IRR Calculator rebuilt** (Aug 2, 2026, ad-hoc user request): 484-line dead
  stub → 1,364-line two-tab page (`irr-` prefix). **Fourth stub in a row with
  no calculator JavaScript.**

  **Two modes, both reverse solves.** Fixed recurring cash flow (initial, holding
  period, ending balance, recurring withdrawal or deposit at one of seven
  frequencies, beginning or end of period) and irregular annual cash flow
  (initial plus up to 50 yearly figures, negatives allowed). Their page is two
  separate forms with independent initial investments, so ours keeps a separate
  initial value per tab rather than sharing the field — sharing it was the
  first build's bug, and it silently showed 60.588% on the irregular tab because
  the fixed tab's $25,000 was still sitting in the box.

  **Oracle again**, both forms submit by GET. Eleven scenarios pulled, and every
  published figure reproduced first time: their two defaults (29.768% and
  12.446%) and all three worked examples from their own article (19.438%,
  11.290%, 10.259%), plus deposit-instead-of-withdraw, quarterly, annual,
  zero-cash-flow and a loss-making case. Watch out when scripting their forms:
  the select values are short codes (`a`, `sa`, `q`, `m`, `sm`, `bw`, `w` and
  `d`/`w`), and passing the visible labels silently falls back to monthly rather
  than erroring — the first oracle run looked plausible and was wrong.

  **Intentional difference — their beginning-of-period case counts one payment
  too many.** Probed across four term lengths and it is consistent: one year
  annual gives 2 payments, three years gives 4, thirty months monthly gives 31.
  N periods have N beginnings, so the correct counts are 1, 3 and 30. Their
  end-of-period case is right, which is what makes this an off-by-one rather
  than a convention: they place an extra payment at the terminal date, which is
  by definition the *end* of the last period. Ours uses the standard annuity-due
  placement, so on their default the cumulative withdrawals read $3,000 against
  their $3,100 and the IRR 30.052% against 30.361%. Flagged in the step-7 report
  and explained on the page.

  **Multiple IRRs are handled properly, which most competitors skip.** The
  solver sweeps the whole rate band and collects *every* zero crossing rather
  than returning the first root a Newton iteration lands on. On the textbook
  double-root case (−4,000, +25,000, −25,000) the page reports both 25%
  and 400% and says plainly that a single IRR has stopped meaning much. It also
  counts sign changes and warns on patterns that merely *could* produce several
  roots, and refuses to invent a number when no root exists at all.

  **A real bug the checks caught**: `part_irr_script.js` was written without its
  closing `</script>` tag. The page still looked fine and the calculator still
  worked, because the browser closed the block for it — but the tag-balance
  assertion caught `div 67/66` and `main 1/0`, and `node --check` failed with
  `Unexpected token '<'` because the extracted "script" ran on into
  `</div></main><footer>`. Second time in this session that tag balance has
  caught something invisible.

  **Verification**: 11/11 oracle scenarios through the shipped page in a
  browser, 38 assertions; running NPV in the discounted cash flow table asserted
  to end at $0.00; 3 valid JSON-LD blocks; FAQ 8/8 exact; protected style block
  byte-identical; 75/75 divs; TOC resolves both ways; desktop and mobile with
  zero real console errors and no sideways scroll; jsPDF lazy. New OG image,
  bands within 2 px.

  **Keyword research**: the IRR SERP is split between finance-education pages
  (Wall Street Prep, Corporate Finance Institute, Omni, GigaCalculator) and
  niche real-estate IRR tools. Two things almost nobody else offers and both
  went into the positioning: the **fixed recurring cash flow** mode, and an
  **NPV-versus-discount-rate curve** with the roots marked. Article is 2,620
  words across 11 H2 sections plus FAQ, covering their topics in original
  wording and adding sections they lack on reading the NPV curve, why timing
  beats totals, and IRR versus NPV versus ROI. The timing example was computed
  rather than borrowed: $80,000 returning $100,000 over five years scores 9.655%
  front-loaded and 6.697% back-loaded on an identical 25% gross return.

- **IRR Calculator: second audit found two real solver bugs** (Aug 2, 2026,
  user asked for a re-audit the day it shipped).

  Learning from the IRA recheck, this pass ran the whole protocol rather than
  the quick parts — and specifically went looking for failures instead of
  confirming successes. Structure, schema, FAQ parity, registration and the
  eleven oracle scenarios were all still clean. The problems were in the solver,
  at inputs the original eleven scenarios never reached.

  **Bug 1: the search ceiling was too low.** The scan ran to 500% per period in
  fixed mode and 1,000% in irregular mode. Anything above that returned "no rate
  fits these figures" — including $1,000 growing to $1,000,000 in a year, where
  calculator.net correctly returns 99,900%, and $1,000 returning $500,000, where
  they return 49,899.963%. Fixed by keeping the fine 4,000-step scan over the
  ordinary band and, only when that finds nothing, widening decade by decade up
  to 20,000,000%. A single scan wide enough for a 100,000% return would have
  been far too coarse to catch an ordinary 3% one, which is why it is staged.

  **Bug 2: a root landing exactly on a scan step was stepped over.** The
  bracketing test was `fprev * fx < 0`, a strict inequality, so a sample point
  where NPV came out at exactly zero produced `0 * fx = 0` and was skipped —
  twice, since the next step then had `fprev = 0` as well. Rare with arbitrary
  numbers and much less rare with round ones, which is what people actually
  type. The $1,000 → $500,000 case needed **both** fixes: widening to reach the
  band containing the root, and this to notice the root sitting exactly on a
  step at 499. Now handled explicitly.

  Measured honestly rather than dramatised: on a ten-case probe, two failed
  before and both work now; the other eight were unaffected. Both failures were
  above the old ceiling.

  **Bug 3: a warning that misdiagnosed the problem.** The irregular mode told
  users "every flow points the same way" whenever no root was found, which was
  wrong for −1,000 then +500,000. Messages now distinguish no sign change at
  all, nothing came back from the investment, and no root inside the searched
  range.

  **A process lesson worth keeping**: `engine_irr.js`, the harness used to
  validate against the oracle, is **not** the shipped code — it is a
  reimplementation. It had an early `if(!isFinite(npv(lo))) return null` that the
  page script does not, so the harness reported the 1,560-period weekly case as
  failing when the live page handles it fine (5.640%, where calculator.net
  returns nothing at all). Validate against the harness for speed, but confirm
  every edge case against the shipped page in a browser before believing it.

  Also aligned `llms.txt`, which still read "IRR Calculator — Internal Rate of
  Return" while the H1, breadcrumb and search index all said "IRR Calculator".
  Same class of drift as the IRA naming, and worth a sweep across all pages at
  some point.

  Four new regression tests pinned: the two very-high-return cases, the
  1,560-period case, and the nothing-came-back message. Suite is 42 assertions,
  all passing, and the 99900.000% figure was checked for clipping at 1280 and
  390 rather than assumed to fit.

- **IRA Calculator: schedule and chart split into two cards** (Aug 2, 2026,
  user pointed out the inconsistency from a screenshot).

  Every other page on the site puts the year-by-year table and its chart in two
  separate cards side by side. The IRA page had them inside a single card, with
  an inner `ira-schedule-body-grid` doing the two-column split. Restructured to
  a `.ira-schedule-row` holding two `.ira-schedule-card` siblings, matching the
  rest of the site: 696px + 400px at 1280, stacked at 390, both with the same
  white background, 1px border and 16px radius. The chart card gained a "Balance
  by Year" heading and the SVG gained an aria-label it did not have.

  **One trap in that change**: the JS tab switch did
  `$('ira-scheduleCard').style.display = 'block'`, and the wrapper is now a grid.
  Setting `block` inline would have silently flattened the two cards into one
  column on every switch back to the growth tab. Changed to `''` so the
  stylesheet value wins. Asserted in the check: hiding on the compare tab and
  restoring to `grid` on the growth tab.

  **A pre-existing layout bug found while verifying, and half-fixed.** Testing
  across widths turned up horizontal overflow, and comparing against the live
  page proved it was not from this change. Two independent causes:

  1. *Grid minimum wider than its breakpoint.* The IRA grid was
     `380px minmax(370px,1fr) 300px` — a minimum of about 1,138px including
     page padding — but only collapsed to one column at 860px, leaving
     **861-1113px broken**, which includes iPad landscape. Fixed by making the
     columns flexible in the same pattern the other pages use and moving the
     breakpoint to 1000. The pages built this session had a smaller version of
     the same fault (minimum ~958px against a 940px breakpoint, so 941-1003
     overflowed); their breakpoints moved to 1000 as well, and the build-script
     style sources were patched too so a rebuild does not undo it. Verified
     across fourteen widths from 1440 down to 390.

  2. *The shared header search box.* `.cf-search-trigger` is a fixed 296px
     inside `.nav-cta`, and the header stops fitting below about 1004px while
     the mobile nav does not take over until around 900. That leaves roughly
     **901-1003px overflowing on all 214 pages** — the rule is byte-identical
     everywhere. It sits in the protected shared block, so it was not touched
     today. This is its own task and a worthwhile one: it is a common laptop and
     split-screen width, and it affects the whole site rather than one page.

  Verified after: two cards at both widths with matching styling, 35 schedule
  rows, 36 chart bars, both tabs computing ($1,196,925 and "Traditional wins by
  $119,693"), three comparison columns still present, protected block
  byte-identical, 115/115 divs, zero console errors, jsPDF still lazy.

- **IRR + Inflation: tabs moved below the bar, and the IRR H1 expanded**
  (Aug 2, 2026, user spotted the tab placement on a screenshot).

  **The tab position was my inconsistency, on two pages.** Counting the grid
  areas across the site: **39 pages put the mode tabs below the blue bar**, and
  exactly two put them above — `inflation-calculator` and `irr-calculator`,
  both built this session. Fixed on both, desktop and mobile stack order, plus
  the build-script style sources so a rebuild keeps it. Verified by measuring
  the rendered offsets against `loan-calculator` and `ira-calculator`: bar at
  252px, tabs at 339px, identical on all four.

  Worth remembering when starting a page from a fresh stylesheet: the grid
  areas are where the house layout conventions actually live, and a wrong order
  there looks deliberate rather than broken, so nothing flags it.

  **Naming, settled on evidence.** calculator.net titles this page "Internal
  Rate of Return (IRR) Calculator" while ours said just "IRR Calculator". The
  SERP is unambiguous: essentially every page ranking for either query carries
  **both** the abbreviation and the expansion — Omni ("Internal Rate of Return
  (IRR) Calculator"), GigaCalculator ("IRR Calculator - Calculate Internal Rate
  of Return"), dqydj, Ajelix, Swoop, thecalculatorsite. Our title already did
  both; the **H1 did not**.

  Changed the H1 to **"Internal Rate of Return (IRR) Calculator"**, which
  contains "IRR Calculator" verbatim, so the short form is not lost and the long
  form is gained — strictly more coverage at no cost. The WebApplication schema
  name now matches the H1 with `alternateName: "IRR Calculator"`. Title left
  alone: it already leads with the short form, carries the expansion, and sits
  at 57 characters.

  Deliberately **not** renamed: the URL, the visible breadcrumb, the
  BreadcrumbList schema, `calculators-index.json` and `llms.txt` all stay "IRR
  Calculator". Unlike the IRA case, these are not contradictory — breadcrumbs
  should stay short, and the H1 is the fuller form of the same name rather than
  a different one. The visible and schema breadcrumbs still match each other,
  which is the check that matters.

  H1 wrapping checked rather than assumed: one line at 1280 and 768, two at 390,
  no clipping and no page overflow at any of them. Both pages re-run through
  their full suites afterwards, all clean.

- **Lease Calculator rebuilt** (Aug 2, 2026, ad-hoc user request): 484-line
  dead stub → 1,201-line two-tab page (`lse-` prefix). **Fifth stub in a row
  with no calculator JavaScript.**

  **The model, recovered from the oracle.** The obvious guess — the money-factor
  shortcut every lease guide teaches, `(asset - residual)/n + (asset + residual)
  x MF` — gives $403.33 on their defaults where they return **$405.06**, so it
  is not what they use. What they actually do is finance `asset - residual/(1+i)^n`
  and amortise it: the asset value less the **present value** of the residual.
  That reproduces $405.06 exactly, and every one of the six fixed-rate scenarios.
  Worth remembering: the widely-taught lease formula is an approximation, not the
  formula, and it drifts further with rate and term. That gap became a section of
  the article.

  **Oracle via GET again**, eleven scenarios across both modes. One trap: the
  hidden mode field takes `fixpayment`, not `fixpay`, and passing the wrong value
  silently falls back to fixed-rate and returns plausible-looking wrong output —
  the same class of failure as the IRR select codes. Always confirm a mode switch
  actually changed the result before trusting a batch.

  **Intentional differences, all three flagged:**
  1. On two reverse-solve cases their rate differs from ours in the third
     decimal (6.683 vs our 6.682, 7.269 vs 7.268). Substituting back settles it:
     ours reproduces the target payment to within $0.0035 where theirs is
     $0.0086 out, and the exact root is 6.682290%. Same pattern as the Interest
     Rate Calculator — their solver converges less tightly.
  2. When the payment is below the depreciation, they print the words "the
     interest/return rate is negative" and no number. Ours returns −2.841%,
     which reproduces the $300.00 payment exactly, and explains that a negative
     rate is the signature of a subsidised lease. A real answer beats a refusal.
  3. Defaults differ as required: $34,500 asset, $19,200 residual, 2y6m, 7.4%,
     $625.

  **A cross-check the page can prove to itself**: the schedule amortises the
  asset value down and must land on exactly the residual. It does, to within
  4e-11, on every case tried including 0% and zero-residual. The finance-charge
  column also sums to their "Total Interest" and the depreciation column to
  `asset - residual`, so three independent totals reconcile. Asserted in the
  browser test rather than only in Node.

  **Verification**: 11/11 oracle scenarios through the shipped page, 38
  assertions; 3 valid JSON-LD blocks; FAQ 8/8 exact; protected style block
  byte-identical; 69/69 divs; TOC resolves both ways; tabs asserted to sit
  **below** the bar this time, having got that wrong on the previous two builds;
  desktop and mobile with zero real console errors and no sideways scroll;
  jsPDF lazy. New OG image, bands within 2 px.

  **Article**: 2,285 words, 10 H2 sections plus FAQ. Built around what the
  reference page does not explain — that residual value moves the payment more
  than anything you can negotiate ($678.60 against $806.47 on the same car for a
  $4,200 residual difference), that money factor is just the rate over 2,400,
  and that the shortcut formula is off by about three dollars a month. Every
  figure computed first.

- **Behavioural scan of every calculator page** (Aug 2, 2026, user asked to
  settle how much of the site actually works).

  Method deliberately behavioural rather than a code heuristic: load each page,
  change a visible input, fire the events, click a Calculate button if one
  exists, and check whether **anything on the page recomputes**. A page can be
  full of markup, pass every structural check and compute nothing — five of
  those have been rebuilt this session already.

  **Result: 75 of 206 pages work. 131 do not.** Roughly two thirds of the site
  does not respond to input at all. Written up in `CALCULATOR_STATUS.md` in the
  repo root, with the full list both ways, so this does not have to be
  rediscovered.

  **The 485-line template is an almost perfect tell** — 129 of the 131 broken
  pages are exactly 485 lines. That makes the two exceptions the important ones,
  because nothing about their size would ever flag them:
  - `age-calculator`, 821 lines, broken
  - `percentage-calculator`, 715 lines, broken

  **The finding that should be acted on first**: `percentage-calculator` is one
  of only six calculators linked from the **shared footer on all 214 pages**,
  and it is the only one of those six that does not work. Every page on the site
  currently points visitors and crawlers at a calculator that computes nothing.
  The other five (mortgage, loan, income-tax, bmi, compound-interest) are fine.

  **Six broken pages duplicate a working one**, so a redirect is cheaper than a
  build and removes near-duplicate thin content: `crypto-profit-calculator` →
  `crypto-profit-loss-calculator`, `mortgage-amortization-calculator` →
  `amortization-calculator`, `payment-calculator` and `repayment-calculator` →
  `loan-calculator`, `simple-interest-calculator` → `interest-calculator`,
  `roi-calculator` → `irr-calculator`.

  Six further pages render **no visible inputs at all** — `scientific-calculator`,
  `statistics-calculator`, `standard-deviation-calculator`,
  `mean-median-mode-range-calculator`, `base64-encode-decode`,
  `url-encode-decode` — so they are not merely inert, they have no interface.

  **A methodology mistake worth recording.** The first hand-verification of the
  scanner's verdicts compared only the first 160 characters of the rendered
  text, which is breadcrumb and heading, and duly reported `tip-calculator` — a
  page known to work — as broken. The scanner itself compared the whole text and
  was right. Spot-checks need to be at least as rigorous as the thing they are
  checking, or they manufacture false conclusions about correct work. Re-run
  against the full text, the two LIVE controls changed and the DEAD ones did
  not, and the verdicts held.

  This also reframes the sidebar question from earlier in the session: adding
  related-calculator links to the 137 short pages would have been pointing
  internal link equity at pages that compute nothing. The scan should come
  before any sitewide linking work, not after.

- **The calculator status scan was wrong, and has been retracted** (Aug 2, 2026).

  Earlier in this session I published `CALCULATOR_STATUS.md` claiming **131 of 206
  pages did not work**, and recommended acting on it. **That number was wrong.**
  Investigating the top recommendation — fixing `percentage-calculator`, which
  the scan called broken and which the shared footer links from all 214 pages —
  showed it computes correctly: 37% of 250 gives 92.5, 46 is 25% of 184, and 64
  increased by 96% gives 125.44. It recomputes as you type, which is why clicking
  Calculate changes nothing.

  **The cause, and it kept moving.** Four separate defects, found one after
  another:
  1. The fingerprint was `main.innerText`, which **excludes `<input>` values**, so
     any calculator that writes its answer into a field looked dead.
  2. Adding all control values to the fingerprint made everything look alive,
     because the values the scanner had just typed were part of it. A
     self-fulfilling test that passed all 206 pages.
  3. Comparing element *indexes* across two different selector queries (one
     including `<select>`, one not) made the scanner's own edits register as
     recomputed output.
  4. This is a **React build**: writing `el.value` from page JS does not update
     React state. Only simulated typing works, so any in-page nudge is unsound
     here.

  Even after all four were fixed, a controlled trial against hand-checked pages
  agreed only **4 times out of 12**, and verdicts moved between runs. At that
  point the honest conclusion is not a better number but that **the true split is
  unknown**, and the file now says so.

  **My spot-checks were wrong twice as well**, in both directions — once
  comparing only the first 160 characters of rendered text (breadcrumb and
  heading) and declaring a working page broken, once mis-indexing and declaring
  dead pages alive. A verification that is less rigorous than the thing it
  verifies does not verify anything; it just launders a guess.

  **Nothing was changed on the site.** `git diff backup-before-percentage-fix
  HEAD` over everything except the two markdown files is empty, the working tree
  is clean, and `percentage-calculator/index.html` is byte-identical to the copy
  taken before starting. Tag `backup-before-percentage-fix` remains as a rollback
  point.

  **What to do instead**: the check that has actually worked all session is the
  per-calculator one — known inputs, known correct answer, asserted against a
  reference. It does not generalise to 206 pages without a per-page expected-value
  table, which is worth building one row at a time as pages get touched. A generic
  sitewide scanner produces a signal that is far too easy to get backwards.

- **Margin Calculator rebuilt** (Aug 2, 2026, ad-hoc user request): 484-line
  dead stub → 1,302-line three-tab page (`mgn-` prefix). Confirmed dead by
  reading the source — no calculator maths and no inputs in `<main>` at all —
  not by the retracted scanner.

  **Three unrelated calculators under one word.** Profit margin (business sense),
  stock trading margin and currency exchange margin (broker sense). Their page
  runs them as three separate forms with a hidden `ctype`, and the values are
  **1 = profit, 3 = stock, 2 = currency** — not in the order the forms appear,
  which is the third time this session a hidden mode field has been a trap.

  **The interesting part is the any-two solve.** Cost, revenue, margin and
  profit are locked together, so any two fix the other two. All six pairs were
  pulled from their engine and all six reproduce: margin 25.00%, markup 33.33%,
  profit $40.00 from every combination. Ours tracks which fields the user
  touched most recently and treats the last two as given, labelling the other
  two as results and tinting them; typing into a third quietly demotes the
  oldest entry. That is better than their blank-fields-and-submit approach and
  keeps the promise the page makes.

  Also reproduced: the negative case (cost $200, revenue $160 → −25.00%
  margin, −20.00% markup), stock margin at three requirements, and currency
  margin at five leverage ratios.

  **Formulas confirmed against their outputs**: stock margin is
  `price x shares x requirement%`, currency margin is
  `rate x units / ratio`. The currency figure needed care to extract, because
  all three result panels say "Amount required" and a naive regex returns the
  stock answer for every currency query — it silently produced 549.00 for five
  different currency scenarios before I scoped the search to the right section.

  **Verification**: 6/6 input pairs plus 6 stock and currency scenarios through
  the shipped page, 28 assertions, zero failures; 3 valid JSON-LD blocks; FAQ
  8/8 exact; protected style block byte-identical; 86/86 divs; TOC resolves both
  ways; tabs asserted below the bar; desktop and mobile clean with no sideways
  scroll; jsPDF lazy. New OG image within 2 px of the template.

  **Article**: 1,956 words, 9 H2 sections plus FAQ, built around the confusion
  the reference page states but does not dwell on — that margin and markup are
  different numbers for the same profit, and that adding 30% to cost produces a
  23.1% margin rather than 30%. Every figure computed first.

- **AdSense readiness folded into the build process** (Aug 2, 2026, user asked
  to comply during the build rather than retrofit before applying).

  Checked the current requirements rather than working from memory. The load-
  bearing ones: original content, no thin pages, real About/Contact/Privacy
  pages, HTTPS, working navigation, and — the one that matters most here —
  **finance and health are Google "sensitive categories"**, so this site is
  almost entirely YMYL and held to a higher bar.

  **Originality, measured rather than asserted.** The user asked directly
  whether the articles are adapted from calculator.net. They are not, and
  `check_originality.py` now proves it: across all seven pages built this
  session the worst **8-word overlap is 0.02%**, and the longest verbatim run
  anywhere is 8 words — "the consumer price index for all urban consumers",
  which is the official BLS series name and cannot be written differently.
  Checkers flag above roughly 15-20%.

  Also measured the risk nobody asks about: **internal duplication**. Reusing
  article structure across pages could trip the same filters. Highest overlap
  between any two of our pages is **0.99%**, and each article shares 0.4-1.2% of
  its 8-word runs with any other. Repeated headings are fine; repeated sentences
  would not be.

  **New: `check_adsense.py`**, run per page before pushing. Enforces 800+ article
  words, 5+ H2, 4+ FAQ, byline, last-updated date, a section on what the tool does
  not cover, a closing disclaimer, canonical, indexability, breadcrumb, links to
  About and Privacy, no broken internal links, valid JSON-LD with FAQ schema
  matching visible text, title 40-65 and description 120-160.

  **Three real findings on the first run**, all fixed:
  1. `ira-calculator` had **no closing disclaimer** — on the most sensitive page
     on the site, retirement plus tax. Every other finance page had one. Added.
  2. `inflation-calculator` title was 66 characters and
     `interest-rate-calculator` 67, both past the point Google truncates.
     Trimmed to 62 and 54, build sources updated too.
  3. The check itself was wrong once: it looked for "Leaves Out" and missed the
     IRA page's "What This Calculator Doesn't Cover". The page was fine; the
     check was not. Regex widened.

  **Five site-level items recorded in the guide, not fixed** — they are decisions
  for the owner, and one is a judgment call worth flagging plainly: every article
  byline says **"Reviewed for accuracy"** while `/about` names nobody and
  describes no editorial process. In a YMYL niche an unsupported authorship claim
  is worse than no claim. The honest fix is available and unusually strong: we
  really do verify every calculator against a reference implementation with a
  recorded test suite, so About should say so. Inventing a named reviewer would
  not be acceptable. Also noted: `/contact` at 225 words, `/about` promising ads
  that do not yet run, ~110 template pages under 300 words, and no `ads.txt`.

- **Margin Calculator: the tinted "result" fields were wrong, and fixed**
  (Aug 2, 2026, user asked simply "why is this green?").

  Good question, and checking it found two real faults I had introduced:
  1. **Contrast 4.24, below WCAG AA's 4.5** — green text on a green tint. The
     visual suite did not catch it because that suite checks *site-wide design
     tokens*, and this was a colour I invented for this page alone. Page-local
     colours sit in a blind spot.
  2. **The colour was not from the palette.** `#F0FDF4` was my invention; the
     site's green tint token is `--gold-tint:#E4F5EA`.

  There was a third problem that no measurement would have found: **green means
  "valid" in a form**, not "this was computed". The wrong signal entirely.

  Fixed by distinguishing the derived fields the way the design system already
  distinguishes things — the sunken surface plus bold weight, against white and
  regular for the fields the user supplied. The RESULT label moved from
  `--gold-deep` (4.44, just under) to `--fin` (9.98). Worst contrast anywhere in
  that group is now **8.63**, and the two states are still clearly distinct at
  both 1280 and 390.

  Rather than invent yet another colour — which is what caused this — the
  replacement was chosen by listing the palette tokens that clear AA on white and
  picking one already used for finance pages.

  **Lesson for the guide**: if a page needs a colour the design system does not
  already have, that is a signal the design system is being worked around, not
  that a new colour is needed. Check any page-local colour against AA explicitly,
  because the site-wide token check will pass it silently.

- **Mortgage Amortization: two different "15 years" on one card, and the note
  explaining it was unreadable** (Aug 3, 2026, owner asked why the same rates
  block appears twice across two pages).

  The owner was right, and the fault was mine from the previous commit. The
  rates card carried two things that meant different things: Freddie Mac survey
  chips (30-yr 6.66%, 15-yr 6.04%) and a term-comparison table priced at the
  rate in the form (6.42%). So one card showed "15-year fixed 6.04%" and, two
  centimetres below, "15 years - $3,425.69", which is the 15-year payment at
  6.42%. The honest figure at 6.04% is $3,343.89 - $82/month and about $14,700
  of total interest apart. Worse, the two buttons carried the same label and did
  different things: the chip set rate *and* term, the table's Use set term only.

  Nothing was miscalculated - every number was right on its own terms, and the
  header did say "Term at your rate". The failure was that "your rate" reads as
  "the rate I'll get", not "the number in the box".

  Fixed by giving each element one job:
  - Chips moved to the form, directly under Interest rate, as small pills
    (`30-year 6.66% up 0.08`), labelled "tap to load that term and rate" so the
    two-field change is stated before the click, not discovered after it. The
    chip matching the current form turns navy, so the active rate is visible
    rather than inferred.
  - The bottom card became a pure comparison: "Compare loan terms", a new
    **Rate** column repeating the rate on every row, and a live "All rows at
    6.42%" in the header. Nothing left to guess.
  - The old `.amz-chip` block (6 dead rules) removed.

  **A real second finding, which the question surfaced.** The explanatory notes -
  exactly the text meant to prevent this confusion - use `--ink-faint` #A6AAB1,
  which is **2.33:1 on white**, well under WCAG AA's 4.5. The explanation existed
  but was close to unreadable. Set to `--ink-soft` #474C55 (**8.63:1**) on this
  page. Following the Margin Calculator lesson, no new colour was invented -
  `--muted` #787D86 was measured first and rejected at 4.14. All nine text
  elements in the touched area now pass AA, zero failures.

  **Site-level, deliberately not touched here:** #A6AAB1 is the note colour on
  many pages, so the same 2.33 failure is sitewide. This commit only overrides it
  page-locally. A sitewide pass on that token belongs in its own task, not folded
  into an unrelated page fix.

  Verified: shared style block byte-identical to bmi/tip/body-fat/mortgage;
  inline JS `node --check` clean; 3 JSON-LD blocks parse, all 8 FAQ Q&As match
  visible text exactly; 52 functional assertions across desktop 1280 and mobile
  390 - payments cross-checked against independent Node values ($2,477.49 at
  6.42%/30y, $3,343.89 at 6.04%/15y), zero console errors, no horizontal
  overflow, h1 at 700, jsPDF still fetches nothing until the button is clicked.

- **UK Mortgage Calculator: full rebuild from a 484-line template stub to the
  3-card pattern** (Aug 3, 2026, owner request, reference page
  calculator.net/mortgage-calculator-uk.html supplied with a screenshot).

  The old page was a React-slider shell: four sliders, 383 words, one H2, three
  FAQs, no schedule, no chart, no PDF. Rebuilt at custom-built tier.

  **Parity (protocol 3a-PRIME).** Their markdown extraction loses input `value`
  and `name` attributes, so the field audit was done against the raw HTML — that
  is what produced the complete set of 11 controls. All 11 map to ours. Every one
  of their outputs is present: the two headline figures, the Monthly/Total table
  (mortgage payment, taxes, insurance, other, total out-of-pocket, loan amount,
  deposit, total interest), the donut, and the Annual/Monthly schedule with the
  balance/interest/capital chart.

  Formulas were verified in Node **before** any page code was written, and the
  browser suite re-checks them: feeding their own defaults (£500,000 / 25% / 25y
  / 5%) reproduces £2,192.21 monthly, £1,562.50 interest-only, £282,663.80 total
  interest, £1,020,164 lifetime out-of-pocket, and their published schedule rows
  at months 1, 12, 180 and 300 plus year-1 interest of £18,574.

  **Two intentional differences, both flagged on the page.**
  1. *Council tax is entered in pounds per year, not as a percentage of the
     price.* Their "Taxes" field is the US property-tax field transplanted
     unchanged; UK council tax is a flat band-based bill set by the local
     authority and is not a function of what the house is worth. Same rule as the
     FHA upfront-MIP case: keep the field, drop the modelling error. Entering the
     equivalent amount reproduces their figures exactly, which the parity test
     asserts.
  2. *Added Stamp Duty and overpayment.* SDLT appears only in their prose, not in
     their calculator — **and the rates in that prose are out of date**, still
     showing the temporary 2022-2025 thresholds (£250,000 nil-rate, FTB
     £425k/£625k). This page uses the bands in force from 1 April 2025, taken from
     gov.uk, and the SDLT function is checked against HMRC's own worked examples:
     £295,000 standard = £4,750, first-time buyer at £500,000 = £10,000,
     additional property at £300,000 = £20,000. A band-by-band breakdown table
     shows the arithmetic rather than just the answer. Overpayment is the largest
     UK-specific query cluster their page does not serve.

  **Keyword research.** UK SERP for the head term is owned by HSBC, MoneySavingExpert,
  Compare the Market, Barclays, Nationwide, Halifax and MoneySuperMarket. The term
  the banks converge on is "mortgage repayment calculator", not "mortgage calculator
  UK", and MSE's own title pairs it with "interest only". Title therefore covers both
  the head term and the second-largest cluster: *UK Mortgage Calculator — Repayments
  and Stamp Duty* (50 chars). Long-tail woven into H2s and FAQs: interest-only,
  first-time buyer stamp duty, overpayment savings, 25 vs 30 year term, lender quote
  differences. Note this page is the section-8 exception — UK-first, British spelling,
  £ and UK conventions throughout.

  **A mistake caught by the suite, worth recording.** The headline figure was
  labelled "Monthly repayment" while actually showing the total including council
  tax and insurance — £1,872 where the mortgage payment was £1,594. This is the
  same class of mislabelling fixed on the amortization page earlier the same day,
  reintroduced from the other direction. The headline is now the payment to the
  lender; the all-in figure sits beneath it and in the table, which also matches
  how the reference page separates the two.

  **Contrast.** Three inherited failures were found by measuring, not by eye:
  `.ukm-crumb a` at 3.66 and, more seriously, the result-head label and sub-line
  at **3.30** — white on `#16A34A`. Both fixed page-locally with existing tokens
  (`--fin` navy at 11.50, `--ink-soft` at 7.64); no new colour invented, and
  `--gold-deep` was measured at 4.44 and rejected for being under the line. All 28
  text elements on the page now pass AA. **The green result-head is used across
  other pages, so that 3.30 failure exists site-wide** — recorded below, not fixed
  here.

  **Originality.** Zero eight-word runs shared with calculator.net (0.00%). Against
  our own pages the first draft hit 1.99% with mortgage-amortization-calculator,
  above the 0.99% site record; the shared runs were the annuity-formula sentence,
  which was reworded to bring it to 1.09%. What remains is byline and TOC
  boilerplate.

  Verified before push: shared style block byte-identical to bmi/tip/body-fat/
  mortgage; `node --check` clean; three JSON-LD blocks parse; all 8 FAQ Q&As match
  the visible text exactly (schema and HTML are generated from one Python list, so
  they cannot drift); 90 browser assertions across desktop 1280 and mobile 390;
  zero console errors; no horizontal overflow; h1 at 700; jsPDF fetches nothing
  until the button is clicked. New OG image at 1200x630. Directory entry renamed
  from the awkward "Mortgage Uk Calculator" to "UK Mortgage Calculator" in
  `calculators-index.json` and `all-calculators`, and the sitemap lastmod bumped.

- **Jump to the result on Calculate, added to 63 completed pages**
  (Aug 3, 2026, owner request after the UK Mortgage build).

  The figures already update as you type, but on a phone the result card sits
  below the form and off screen, so tapping Calculate looked like nothing had
  happened. Calculate now scrolls the result card to just under the sticky
  header. One self-contained script appended to each page - no existing
  handler, style or markup touched, and every changed file was diffed to prove
  the snippet is the only difference (63 files, +1701, zero deletions).

  Whether to scroll is decided from live geometry rather than a breakpoint: if
  the result is level with the form it is already visible and nothing moves.
  That keeps desktop untouched without needing to know each page's collapse
  point, which matters because the prefixes and breakpoints vary page to page.
  The 71px sticky header is subtracted, and prefers-reduced-motion gets an
  instant jump.

  **Nine pages were deliberately left out**, because their own scripts already
  scroll on Calculate and a second scroll would fight the first:
  crypto-position-size, crypto-tax, fha-loan, leverage, liquidation-price,
  marriage-tax, mortgage-amortization, risk-reward and staking-reward. The
  snippet was injected into all 72 first and then reverted on those nine.

  **A measurement trap worth recording, because it nearly produced the wrong
  answer.** The first attempt classified pages by behaviour: click Calculate on
  the pre-change build and see whether the page scrolled. That said 65 of 72
  already had the feature, which would have meant abandoning the task. It was
  wrong. Clicking Calculate re-renders the DOM, and the browser's **scroll
  anchoring** then shifts scrollY to keep a visible element steady - loan
  calculator moved 378px with no change in document height and no scroll code
  anywhere in its source. Re-running the identical build three times gave
  spreads of 19-44px, so the signal was noise. The reliable classifier is
  static: does the page's own script call scrollIntoView, window.scrollTo or
  set scrollTop. That gives 9, not 65.

  The same trap applies to verification. Comparing scroll movement before and
  after the change reported five desktop failures that were all noise; the
  sound desktop check is geometric - measure the form-to-result offset and
  confirm the guard blocks - plus a same-build repeat run to establish the
  noise floor.

  Verified: 12-page sample across every structure on the site (single button,
  multi-tab buttons, the separate crypto design system, the largest file, the
  heaviest tables). At 390px the result lands in view and clear of the header
  on all twelve, with no console errors; at 1280px the guard blocks on all of
  them. Injected script parses under node --check on all 63.

## Mutual Fund Calculator — rebuilt Aug 3, 2026

Was a 484-line template-tier page with no calculator at all. Rebuilt to the 3-card
pattern (`mf-` prefix), reusing investment-calculator's component conventions.

**Reference audited live** (raw fetch + the owner's screenshot of the rendered page,
per the guide's "do both" rule): calculator.net/mutual-fund-calculator.html. It has
no tabs/modes and no schedule; 8 inputs, 8 result rows, one donut.

**Field map: 9/9 input controls, 9/9 result fields, zero omissions.** Ours adds a
conditional Deferred sales charge result row, an Annual/Monthly schedule, a stacked
bar chart, a Fee Impact card and PDF export.

**Math reverse-engineered and verified in Node before embedding.** Their engine is
the industry-standard convention: net annual rate = rate of return − expense ratio,
compounded monthly as `(1+net)^(1/12)−1`, contributions at month end, front-end load
taken from the initial investment and from every contribution, deferred charge on
`min(total principal, ending balance)`, and Net IRR solved from the monthly cash-flow
sequence and reported as an annual effective rate. Verified against their reference
case (20000 / 0 / 1000 / 5% / 5y / 2% / 0% / 0.5%): ending value, total principal,
total contributions, net return, Net IRR (3.844%), sales charge and all four donut
percentages match exactly. Also checked a closed-form lump sum, a deferred-charge
case, a loss case, a 40-year and a 100-year horizon, and a partial-year term.

**Intentional difference — Operating expenses shows $1,324.00 where they show
$1,323.40 (0.045%).** calculator.net is internally inconsistent on this one line:
their ending value comes from a 4.5%-net path, but their fee figure comes from a
separate ledger running at ~4.4767% (solved both ways; their number sits between the
two orderings of that ledger, within a cent). Reproducing their figure would break
tie-out between the result card and the schedule. Ours accrues the fee from the same
balance path the page displays, so every schedule row satisfies
`start + added + growth − fees = end` exactly and the fee column sums to
"Total charges and fees". Flagged on-page in the methodology section.

**Two bugs the DOM-level checks passed and only the screenshot caught** — the exact
failure mode section 3a-PRIME warns about:
1. `solveIrr` bracketed from −0.9999, where `Math.pow(1+x, -i)` overflows to Infinity
   once the horizon passes ~10 years, so Net IRR silently rendered as an em-dash for
   any realistic holding period. Now brackets from a range where npv stays finite.
2. Native number spinners ate ~16px of the 55px-wide years/months boxes, hiding the
   values entirely while `input_value` still returned them. Spinners removed, split
   control widened. Both now have regression assertions in the browser suite.

**Keyword research** (web-search competitive proxy; no paid tool or GSC connector in
this environment). Head term "mutual fund calculator" — calculator.net, NerdWallet
and Omni rank. NerdWallet titles theirs around growth *and fees*, which is the
differentiator; the fee/expense-ratio angle is a distinct query cluster with its own
dedicated competitor pages ("expense ratio calculator", "mutual fund fee
calculator", "front-end load"). SIP framing deliberately avoided — those SERPs are
India-facing and section 8 says USA-first. Title: "Mutual Fund Calculator — See Your
Real Return After Fees" (56 chars); description 147 chars, fee-benefit first.

**Verification before push.** Static: 52 checks — protected shared style block
byte-identical to body-fat-calculator, all six `:root` vars intact, no universal
reset, `<title>`/description/canonical/OG/Twitter present, all JSON-LD parses,
BreadcrumbList + FAQPage + WebApplication present, FAQ schema string-equal to the
visible `<h3>`/`<p>` pairs (8/8, automated diff), 7 inline scripts pass
`node --check`, 2,449-word article, 9 H2s, 18 internal links none broken.
Browser (Playwright, 1280px and 390px): zero console/page errors, zero horizontal
overflow, H1 computed weight 700, all five cards render with real geometry, numeric
parity re-checked in-browser, schedule rows tie out, jsPDF fetches nothing until the
button is clicked. Five untouched pages spot-checked clean.

Defaults deliberately differ from theirs: 15,000 / 1,200 / 400 / 7% / 12y / 1.5% /
0% / 0.65%.

**Still open on this page:** no `og/mutual-fund-calculator.png` was generated this
session — the OG tags point at the shared default. Worth adding next time the page
is touched.

**Observed in passing, not fixed:** `investment-calculator` requests jsPDF on page
load rather than on click, contrary to the guide's standing lazy-load rule. Left
alone to keep this commit to one page; worth its own pass across whichever pages
still do this.

## Mortgage Payoff Calculator — rebuilt Aug 3, 2026

Was a 46KB template-tier page: one slider form (4 inputs), 3 H2s, a generic
`X Calculator | CalculatorBoss` title, no biweekly, no lump sum, no schedule,
no chart. Rebuilt to the 3-card pattern (`mpo-` prefix), reusing
loan-calculator's tab conventions and mortgage-calculator-uk as the structural
donor.

**Keyword research done before any copy was written, per section 4.**
Head term "mortgage payoff calculator" is high-volume/high-competition:
Ramsey, AARP, calculator.net, Allstate, mortgagecalculator.org, plus a long
tail of near-duplicate bank pages all running the same Fiserv widget and the
same stock line ("How much interest can you save by increasing your mortgage
payment?"). That last part is the opportunity — dozens of thin, identical,
non-differentiated pages rank on this term, which is a much softer SERP than
the big names alone suggest. Distinct long-tail clusters confirmed to have
their own dedicated competitor pages (so real query clusters, not phrasing
variants): "extra payment mortgage calculator" (PrimeLending, TotalMortgage,
mortgagecalculator.org), "biweekly mortgage calculator" (PrimeLending,
mortgagecalculator.biz), "early mortgage payoff calculator" (many banks),
"additional mortgage payment calculator" (Navy Federal), "what if I pay more".
**Mid-tail gap built around:** nobody covers the "I don't know my remaining
term" case well except calculator.net, and "payoff amount" intent (Allstate
ranks on it) is underserved and is a genuinely different question from
"balance" — both got their own tab/section. Title targets the two outcomes a
searcher actually wants: *Mortgage Payoff Calculator — Payoff Date & Interest
Saved* (57 chars), description 151.

**Reference audited live** (raw source fetch for the input set + server-rendered
result pages for the output set, per the guide's "do both" rule):
calculator.net/mortgage-payoff-calculator.html. Two separate calculators on one
page, which became our two tabs. Fetched their rendered result for every
repayment option separately rather than assuming — worth it, because
"Payback altogether" and "Normal repayment" render a completely different
result block (no savings boxes, different headline) that the default view
never shows.

**Field map: 12/12 input controls, 24/24 result fields, zero omissions.**
Intentional differences, all flagged rather than silent: one shared strategy
radio + extra-payment trio across both tabs instead of duplicating them (only
one tab is visible at a time); "pay in full" hidden on tab 2, matching them,
since there the balance *is* the input; our chart shows the payoff plan's
yearly principal/interest as stacked bars plus both balance curves rather than
their four raw lines, with the original's per-year interest carried in the
adjacent schedule table. Ours adds an Annual/Monthly schedule toggle, a donut,
and PDF export.

**Biweekly is the part worth recording, because three reasonable models are all
wrong.** Not a true 14-day amortisation at r/26, and not a 13M/12 monthly
equivalent — both miss by roughly half a payment. Reading calculator.net's own
per-period `allPayOffData` array settled it: they simulate **monthly** at r/12
and add an extra **half-payment every 6th month**, which is what 26
half-payments a year actually comes to (2 extra halves = 1 extra payment).
Their schedule shows payments of 2398.20 with 3597.30 landing on months
6, 12, 18, 24… Once that replaced the guess, every figure matched. Lesson
worth generalising: when a mode won't reconcile, their embedded chart/schedule
data array is the ground truth, not the rendered summary.

**All 15 numeric checks matched to the cent** — payment, balance-after-k,
original totals, extra-monthly, extra-annual (lands at year end), one-time
(lands on the first payment), biweekly and pay-in-full, on both tabs. Verified
first in Node, then re-asserted in the rendered browser against the same
reference figures.

**Two bugs caught during the build, both by testing rather than inspection:**
a floating-point edge case where the untouched known-mode schedule ran 317
months instead of 316 (now pinned to the exact remaining term via `fixedN`),
and a savings percentage computed against *remaining* interest instead of
*whole-loan* interest, which read 35% where calculator.net correctly reads 26%.
The dollar saving was right in both cases; only the denominator was wrong,
which is exactly the kind of thing that survives a code read.

**A third fix shipped separately after the owner asked about it:** a blank rate
box fell through to 0%, so mid-edit the page showed a plausible but wrong
payoff date (20y8m where the answer was 20y2m) rather than an obvious error.
Blank and typed-zero are now distinguished — an empty box is rejected like
every other empty box, an explicit 0% still computes an interest-free loan.
Negative rates rejected, negative extras clamped. The general shape of this
bug is worth watching for on other pages: a guard was omitted precisely
because zero is a *legitimate* value for that field.

**Verified before push:** 63 Playwright checks at 1280 and 390px, 11 browser
edge cases (0% rate, blank/negative inputs, remaining > original term, extras
exceeding the balance, 50-year term, tab-2 zero balance/payment), zero console
errors, zero horizontal overflow, protected style block byte-identical to both
a custom-built and a template-tier page, jsPDF fetching zero bytes on load and
firing only on click. Article 2,175 words, 8 H2s + 8 FAQs, FAQ schema and
visible FAQ generated from one Python source so the em-dash drift that has hit
every previous rebuild cannot occur. Originality: 0.155% eight-word overlap
with calculator.net (field labels only) and **zero** article-level overlap with
any other page on this site. New OG image.

### Three site-level fixes shipped in the same session

1. **Sitemap pointed at redirects, not canonicals.** All 210 entries omitted
   the trailing slash while every page canonicalises with one, so each
   submitted URL returned a 308 to the real address (confirmed live before
   changing). Not broken, but a redirect hop on every crawl and a "Page with
   redirect" report in Search Console. All 210 now end in a slash.

2. **`/about/`, `/contact/`, `/privacy-policy/` and `/terms/` canonicalised to
   the homepage.** Found by cross-checking every sitemap URL against the
   canonical on the page it points to — exactly four mismatches, all four these.
   This tells Google the trust pages are duplicates of "/", i.e. an instruction
   to drop them from the index. Worse than a normal canonical slip, since these
   are the pages an AdSense review looks for on a site in a sensitive category,
   and they are the destination of footer links sitewide. Now self-referencing;
   sitemap and canonical agree on all 210 URLs.

3. **Mortgage Amortization's OG image showed the wrong text** — the Marriage Tax
   subtitle spliced into the middle of it, plus an em dash written as a literal
   ".mdash;". Redrawn. Then audited the other 56 rather than assume it was
   isolated: OCR across all of them for rendered entity fragments (zero hits),
   and each image's OCR'd text compared against its own page's meta description
   to catch copy from a different page (nothing else wrong). Defect was confined
   to that one file.

## Net Worth Calculator — rebuilt Aug 3, 2026

Was a 484-line template-tier page with no calculator. Rebuilt to the 3-card pattern
(`nw-` prefix).

**Reference is NOT calculator.net this time.** calculator.net has no net worth
calculator — checked and confirmed. The owner supplied
omnicalculator.com/finance/net-worth as the reference, audited live. Per section 3a,
also diffed Bankrate, NerdWallet, Forbes Advisor, Schwab MoneyWise, AARP and
Financial Mentor.

**Field map: 9/9 assets, 8/8 liabilities, 3/3 result fields, zero omissions.**
Omni's asset and liability field sets are reproduced exactly (primary home, holiday
home, other real estate, shares and investments, other investments, savings,
checking, motor vehicles, other assets / mortgage, car loan, personal loan, student
loan, lease purchase, consumer loan, credit card and overdraft, other debt).

**Added beyond the reference**, each because a majority of the other competitors have
it and it answers a distinct query cluster:
- Debt-to-asset ratio, liquid assets, home equity, and net worth excluding home
  equity as derived result rows.
- Asset-mix donut and a stacked assets-vs-liabilities column chart by category.
- A balance-sheet panel showing each line item's share of its own side.
- **Ten-year projection** (annual savings + expected growth). Bankrate, Schwab and
  AARP all have this; Omni does not. Verified against the closed form
  `NW·(1+g)^10 + S·((1+g)^10−1)/g` — both give $801,189 on the page defaults.
- **Benchmark panel** with the age group as a tab row (not a dropdown, per standing
  UI rule), showing median, average AND the top-10% threshold.

**Benchmark data deliberately differs from the reference.** Omni's comparison table
is the Federal Reserve's *2016* SCF (published Sept 2017) and shows only the mean.
This page uses the **2022 SCF** (released Oct 2023, the most recent completed wave;
the 2025 wave is expected late 2026) and shows median, mean and the 90th-percentile
threshold together, because the median/mean gap is the single most misread thing in
net worth statistics — mean $1,063,700 vs median $192,700 across all US families.
Figures used, in 2022 dollars: median by age 39,040 / 135,300 / 246,700 / 364,270 /
410,000 / 334,700; mean by age 183,380 / 548,070 / 971,270 / 1,564,070 / 1,780,720 /
1,620,100; top-10% thresholds 372,100 / 1.04M / 1.96M / 2.96M / 2.88M and 1.94M all
ages. **Known limitation, stated on the page:** the Fed reports top-10% thresholds
for 18–34/35–44/45–54/55–64/65+, so the 65–74 and 75+ tabs both show the 65+ figure.

**Intentionally omitted from the reference:** Omni also compares by income tier and
by education level. Those cuts were dropped rather than shipped, because current
(2022 SCF) figures for every bracket could not be verified to the same standard this
session — only fragments were available (e.g. median net worth by education: no high
school diploma ~$38,000, college degree ~$464,000). Shipping a half-populated table
on a YMYL page was the worse option. Worth adding once the full 2022 breakdowns are
pulled from the Fed's own SCF tables.

**Verification.** Every displayed figure recomputed independently in Node before
embedding: total assets 710,500, total liabilities 311,300, net worth 399,200,
debt-to-asset 43.8%, liquid 247,500, home equity 152,000, ex-home 247,200, donut
59.1/29.4/5.4/3.9/2.1%. Static: 52 checks pass — protected shared style block
byte-identical to body-fat-calculator, all six `:root` vars intact, no universal
reset, title/description/canonical/OG/Twitter present, all JSON-LD parses,
BreadcrumbList + FAQPage + WebApplication, FAQ schema string-equal to visible text
(8/8), 7 inline scripts pass `node --check`, 2,130-word article, 9 H2s, 19 internal
links none broken. Browser (Playwright, 1280px and 390px): zero console/page errors,
zero horizontal overflow, H1 computed weight 700, all cards render with real
geometry, assets−liabilities ties to the displayed total, benchmark tabs switch and
show the right figures, negative-net-worth path shows a minus sign and turns the
header red, Clear zeroes everything, jsPDF fetches nothing until the button is
clicked.

**Originality.** 8-word overlap with omnicalculator.com: **0.000%** (0 of 2,122
shingles); 6-word 0.047%, and the only 5-word matches are unavoidable phrases like
"how to increase your net worth" and the literal field list. Overlap with our own
mutual-fund-calculator initially measured 1.13%; one repeated sentence about
inflation eroding a nominal projection was reworded, bringing it to **0.94%** — the
remainder is the site-wide legal disclaimer opening and shared headings, which are
intended to be consistent.

**Keyword research.** Head term "net worth calculator" — NerdWallet, Bankrate, Forbes
Advisor, Schwab, AARP and Omni all rank. The genuinely differentiating clusters are
"average/median net worth by age" and "net worth percentile / top 10%", which is why
the benchmark panel leads with all three reference points rather than a single
average. Privacy ("all calculations run in your browser") is a recurring trust signal
across the competitor set and is stated in the form and the article. Title: "Net
Worth Calculator — See Where You Actually Stand" (50 chars); description 147 chars.

**Still open on this page:** no `og/net-worth-calculator.png` and no `og:image` tag —
same gap as the mutual fund page and most of the site (only 58 of 214 pages have an
og:image at all). The `sitemap.xml` `lastmod` for this URL is also stale.


## OG images, sitemap and inbound links for the two Aug 3 pages

Closing the gaps flagged at the end of both builds.

**OG images generated** for `mutual-fund-calculator` and `net-worth-calculator`, and
`og:image` / `og:image:width` / `og:image:height` added to both pages in the site's
existing position (immediately after `og:url`, before `twitter:card`). Both verified
to return 200.

The generator lives in the session scratch dir, not the repo, but the template was
reverse-engineered from `og/apr-calculator.png` and is worth recording so it does not
have to be redone: 1200x630; base `#F3F1EA`; the green wash is a **clipped diagonal
linear gradient**, not a radial one — `t = clamp(0.001*x + 0.000586*y - 0.630, 0, 1)`
blending toward `#D3E5D1`. Logo bars at x=66 baseline y=79, brand text IBM Plex Sans
Bold 25 at x=100. Category pill x=64 y=147 h=34, fill `#E8EDF6`, border `#CEDAEC`,
IBM Plex Mono Bold 13 in `#22417A` with ~1.6px letter spacing. H1 IBM Plex Sans Bold
64 on baseline 268, subhead Regular 24 on baseline 324, both with about -3% tracking
(Pillow has no letter-spacing, so draw per character). Divider at y=529, footer
baseline 566. Two gotchas: IBM Plex Sans has no U+2713 and Pillow's fallback renders
it as a radical sign, so the tick is drawn as a polyline; and IBM Plex Sans is not on
the box — pull it with `npm pack @ibm/plex-sans` and convert the complete woff2 to
ttf with fontTools (Plex Mono is already at
`/mnt/skills/examples/canvas-design/canvas-fonts/`). Reproducing apr-calculator.png
with this recipe gives a mean absolute pixel difference of 2.39 and an exactly
matching H1 width.

**sitemap.xml** `lastmod` updated for both URLs (they still read 2026-07-03).

**Correction to an earlier note in this session:** I reported that sitemap `<loc>`
entries lack the trailing slash while canonicals have it. That was wrong — a bad
regex. All 209 entries **do** carry the trailing slash and match their canonicals.
There is no slash mismatch to fix.

**Inbound internal links added** — both pages previously had outbound links but were
only reachable from `/all-calculators/` and `/sitemap/`. Added one related-card link
each from: investment, compound-interest, IRR and bond → Mutual Fund; savings,
debt-consolidation and budget (already present) → Net Worth. `retirement-calculator`
was deliberately skipped: it has four tab panels each with its own sidebar and four
`-viewmore` anchors, so the insert point is ambiguous and it needs a considered edit
rather than an automated one. Note the `-viewmore` anchor markup is **not** uniform
across pages (`href="/"`, `href="/all-calculators/"` and `href="/all-calculators/#fin"`
all appear), so any future automated pass over related cards must match on the class,
not the href.

**Verified after:** all six donor pages plus both targets, body-fat-calculator and
retirement-calculator load with a page-specific title, canonical, meta description,
`nav-links: flex`, no horizontal overflow and zero page errors; both pages' full
static and browser suites still pass.

**Still open site-wide:** only 58 of 214 pages have an `og:image` at all, and most
`lastmod` values are stale. Worth its own pass.

## Net Worth Calculator — post-launch audit, Aug 3, 2026

Adversarial pass over the shipped page (not a re-run of the build's own tests) plus a
field-coverage diff against NerdWallet, Bankrate, Forbes Advisor, Schwab MoneyWise and
AARP. Five defects and one coverage gap found and fixed.

**Bugs, all of which the build-time suite passed straight over:**
1. **Negative asset input corrupted every total.** `min="0"` does not stop a typed
   minus sign. Entering −500,000 for a home produced total assets of −$209,500 and a
   nonsense net worth. Now clamped on read via a `money_in()` helper and the field
   itself is reset to 0 on blur.
2. **Projection bars ran straight out of the SVG.** With a negative net worth the bars
   drew downward from a fixed baseline; measured bottom edge was y=202 in a
   viewBox 120 tall. Rewritten to split the plot around a computed zero line sized to
   whichever side has values, with a visible zero rule when any year is negative.
3. **Debt-to-asset ratio showed an em-dash for the single most alarming case** — debts
   with no assets. Now reads "No assets to cover it".
4. **A very large total overflowed the result card.** The headline was a fixed 30px.
   Now steps down to 24px and 20px by string length.
5. **Negative totals rendered in green** in the balance-sheet row and the projection
   headline. A negative number in the positive colour is actively misleading; both now
   go red.

**UX: focus now selects the field contents.** Every box ships with a worked example in
it. Without select-on-focus, tapping a field on a phone puts the caret beside the
existing digits, so a user aiming for 250000 gets 420000250000. This is worth applying
to any other page that prefills example values.

**Coverage gap vs the big US sites.** NerdWallet, Bankrate and Forbes Advisor all name
retirement accounts as their own asset line; ours had them buried in "other
investments", which is the largest single balance most households own and the most
likely thing to be left out entirely. Added a **Retirement accounts (401k, IRA)** field
in the Investments group — deliberately excluded from the liquid-assets line, since
that is the point of showing liquid separately. Asset and liability counts are now
10 and 8; the reference's 9 and 8 are all still present, so parity is unaffected.

Also rewrote the two form hints to say explicitly where ambiguous items go: business
ownership, crypto and cash-value life insurance under other investments; land, art,
jewelry, collectibles and money owed to you under other assets; medical bills, business
loans, taxes owed, payday/title loans and family debts under other debt. NerdWallet
lists medical debt, business loans and payday loans by name, and users were otherwise
left guessing.

Defaults changed with the new field: assets 806,500, liabilities 311,300, net worth
495,200, debt-to-asset 38.6%, liquid 247,500, ex-home 343,200, ten-year projection
957,563 (matches the closed form to the dollar).

**All six fixes now have permanent assertions in the page's browser suite**, so they
cannot regress silently. Re-ran the full adversarial pass on desktop and mobile
afterwards: zero issues.

**Lesson for future builds:** the build-time suite tested the happy path and the
documented edge cases, and passed all of them while five real defects sat in the
shipped page. Worth running a deliberate junk-input pass — negatives, empty strings,
text, absurd magnitudes, all-zero, all-negative — against every calculator before
calling it done, and checking that negative results are coloured as negative.

## Mutual Fund Calculator — same audit applied, Aug 3, 2026

Ran the Net Worth adversarial pass against the Mutual Fund page as well, since the
defects there were a class of bug rather than a one-off. Four found, all fixed, all
now asserted in that page's suite.

1. **`money()` never handled negatives.** A losing fund rendered its net return as
   `$-33,307.96`, with the sign stranded after the dollar. Now `\u2212$33,307.96`,
   matching the rest of the site.
2. **A negative net return and a negative IRR rendered in neutral ink**, the same
   colour as a gain. Both now go red via an `is-loss` row class.
3. **A very large ending value overflowed the fixed 30px headline.** Steps down by
   string length, same fix as the net worth page.
4. **No select-on-focus**, so tapping a prefilled box on a phone appended to the
   example (15000 + typed 50000 = 1500050000).

Things that were already correct and are worth knowing hold: negative initial
investment is rejected, 100% sales charge is rejected with a message, junk text does
not produce NaN, an expense ratio above the return still computes, and the schedule
chart and donut stay inside their boxes with a loss.

**Standing item:** the same junk-input pass has NOT been run against the other ~60
custom-built pages. Given four of four checks failed on both pages audited so far,
assume the rest carry the same defects until checked \u2014 particularly the negative
formatting, negative colouring and select-on-focus, which are shared conventions
rather than page-specific logic.

## Site-wide: select-on-focus across 174 pages, Aug 3, 2026

Rollout of the fix found in the net worth audit, plus one genuine money-formatting bug.

**select-on-focus, 174 pages.** Almost every calculator on this site ships with worked
example values already in its boxes. Without select-on-focus, tapping a field on a
phone puts the caret beside the existing digits, so someone aiming for 250000 in a box
reading 420000 ends up with 420000250000. Only the two pages fixed earlier today had
it.

Implemented as **one delegated `focusin` listener injected before `</body>`**, the same
injection pattern the "Calculate jumps to the result" script already uses. Deliberately
not a regex over each page's own JS: the pages have wildly different script structures
and a broad replace over 174 of them is exactly the kind of change that has broken this
site before. The helper needs no per-page knowledge, guards itself with a
`window.__cbSelectOnFocus` flag, and skips `readOnly`/`disabled` inputs so computed
output boxes (horsepower's `hp-hpInput`, investment's `inv-end`) are left alone.

One non-obvious detail worth keeping: a mouse click focuses first and *then* places the
caret on mouseup, which throws the selection away. The helper swallows that single
mouseup and removes the listener after 400ms. Without it the fix works on mobile tap
but silently does nothing on desktop.

40 pages were skipped because they have no `type="number"` inputs at all (404,
_not-found, about, all-calculators, age-calculator, base64-encode-decode and similar).

**bitcoin-calculator: a losing position rendered as `$-1,234.56`.** `'$'+profit.toLocaleString(...)`
with no sign handling. Fixed inline at the call site — note that `fmtUSD()` on that page
lives in a *different* `<script>` block, so calling it from the profit code would have
thrown a ReferenceError. Caught before pushing; worth checking scope on that page before
any future refactor.

**Correction to what I reported before this pass.** I said eight pages had the negative
money-format bug. That came from a regex that only looked at a single expression, and
seven of the eight (debt-consolidation, depreciation, discount, down-payment, estate-tax,
fha-loan, finance) already do `var neg = n<0; n = Math.abs(n);` on the line above and are
correct. Only bitcoin-calculator was actually broken. This is the second bad-regex
false positive this session — the first was the sitemap trailing-slash claim. **Read the
surrounding lines before believing a pattern match.**

Minor known inconsistency, deliberately not churned: those seven pages prefix a plain
ASCII hyphen (`-$1,234`), while net-worth and mutual-fund use a typographic minus
(`\u2212$1,234`). Both read fine; standardising would mean touching seven working pages
for a typographic preference, which was not worth the risk inside a 175-file commit.

**Verification, before and after, per the mandatory site-wide process.** A baseline was
captured for all 214 pages first (protected style block SHA-1, title, canonical,
description, byte length, script count). After the change, across all 214: zero
protected-style-block hashes changed, zero titles changed, no canonical or meta
description lost, all six `:root` variables intact everywhere, no universal `*` reset
introduced, and every inline script on every page still parses under `node --check`.
All 214 pages then loaded in a real browser: `nav-links: flex`, no horizontal overflow
and zero page errors on all but `404` and `_not-found`, which were already React error
pages with no canonical or description before this change. Both the mutual-fund and
net-worth suites still pass. Finally the behaviour itself was verified at a 390px
viewport with a real click on 69 pages that actually have an editable prefilled number
box: 69 working, 0 failing.

**Two test artifacts that looked like failures and were not**, recorded so the next
person does not chase them: clicking the *centre* of a number input hits the native
spinner and increments the value (salary-calculator went 25 to 25.01 before any typing),
and the first visible number input on several pages is a read-only result box. Target
the first editable input and click its left edge.

## Payment Calculator — rebuilt Aug 4, 2026

Owner request, with the calculator.net page and two screenshots supplied as the
reference. Built under the section 3a-PRIME parity protocol.

**Before:** a template-tier stub — 220 words in `<main>`, 3 H2s (one of which was
just the form's "Solve for" label), 2 FAQ entries, a React-rendered
payment/loan-amount toggle with no element IDs, and no amortization schedule,
chart, or fixed-payment mode at all. Generic `Payment Calculator | CalculatorBoss`
title.

**Keyword research (section 4), done before any copy was written.**
Head term "payment calculator" is effectively owned by calculator.net, which is
also the only major that titles the tool that bare way. Every US competitor that
ranks — TransUnion, Bankrate ("Simple Loan Payment Calculator"), Finaid, United
FCU — uses **"loan payment calculator"**, so per section 8 that higher-volume
phrasing went into the title tag and meta while the H1 and slug keep "Payment
Calculator". A genuinely separate query cluster sits behind the second tab:
"loan payoff calculator" / "how long to pay off my loan" has dedicated pages at
MoneyUnder30, thecalculatorsite, CalcXML, DCU and Atomic CU, so it earned its own
H2, its own FAQ entries and a mention in the meta description rather than being
folded in silently. Middle-ground gap found: nobody titles around *both*
directions in one tool, which is what the title now leads with.
Title `Loan Payment Calculator — Monthly Cost or Payoff Time` (53 chars),
description 149 chars.

**Parity work.** Live-fetched calculator.net's source for the input set and also
fetched the `ctype=fixpay` result URL, because the Fixed Payments headline and
its extra "Time Required to Clear Debt" row do not appear on the default page
load. Input parity 6/6, result parity 11/11.

**Formula verification in Node before any of it was wired into the page**, against
calculator.net's own published figures — 32 assertions, all passing: the fixed-term
payment, both totals, the 15-row annual schedule and sampled monthly rows for
200000/15y/6%, plus the payoff time (11 years 6.98 months), 11.58-year figure,
138.98-payment total and 12-row schedule for 200000/$2000/6%.

**One real discrepancy found and resolved rather than papered over.** In fixed-payment
mode the term lands on a fraction of a month, and a plain discrete simulation
(138 full payments plus a real final payment of balance + one month's interest)
totals $277,951.56 while calculator.net's headline says $277,951.44. The 12-cent
gap is not a bug on either side: their headline is the closed form `M × n`, and
their schedule silently back-solves the last period as a residual so the table
reconciles to it — which is why their year-12 interest cell reads "$274" where
every other cell on the page carries two decimals (the true residual is $274.07).
We adopted the same convention, so our headline and our schedule agree with each
other *and* with theirs, and the article explains plainly that the closing payment
is smaller than the rest. Flagged under intentional differences rather than left
silent.

**Built** on the loan-calculator/apr-calculator 3-card conventions with a `pay-`
prefix: navy bar + lazy PDF button, Fixed Term / Fixed Payments tabs, form card,
result card with headline + sub-line + rows + principal/interest donut, navy
related-calculators sidebar (9 links), and a bottomgrid pairing the amortization
schedule (Annual/Monthly toggle, "End of year N" separators in the monthly view)
with a three-line balance / cumulative-interest / cumulative-paid chart matching
the three series calculator.net plots. Defaults deliberately differ from theirs:
$28,500 over 5 years at 7.4%, and $600/month on the second tab.

**FAQ schema generated from the same Python list as the visible FAQ HTML.** The
guide records this em-dash/curly-quote mismatch biting every previous rebuild;
generating both from one source makes it structurally impossible rather than a
thing to remember. Verified anyway: 8/8 exact string equality.

**Verification before push**
- Protected shared style block byte-identical to the pre-edit file and to
  bmi-calculator's.
- All JSON-LD parses; BreadcrumbList left in `<head>` per site convention (an
  earlier build of this page added a second one in `<main>` — caught and removed).
- Inline JS passes `node --check`; sitemap.xml parses.
- Playwright, desktop 1280px and mobile 390px, 30 assertions each, all passing:
  default render, both tabs, annual/monthly toggle (5 rows / 60 rows + 4 year
  separators), the two calculator.net parity cases typed in live, the
  payment-below-monthly-interest error path, h1 computed font-weight 700, zero
  console errors, zero horizontal overflow. Screenshotted rather than only
  asserting nodes exist, per the guide's note that DOM checks passed on the
  invisible-headings bug.
- jsPDF: zero bytes fetched on load, `window.jspdf` undefined until the button is
  clicked, PDF downloads on first click, no re-fetch on second.
- Originality: 0.00% 8-word-run overlap with calculator.net's page. Against our own
  74 substantial articles, worst overlap is 0.26% once the site-wide byline and
  disclaimer boilerplate are excluded (1.57% including it, and 28 of those 31
  shared runs *are* that boilerplate).

Article is 2,030 words, 8 H2 sections, 8 FAQs, 12 distinct internal links.
New OG image at `og/payment-calculator.png`; sitemap lastmod refreshed.

**Left open, flagged to the owner**
1. **20 pages still load jsPDF eagerly** — loan-calculator, mortgage-calculator,
   bmi-calculator, salary-calculator, income-tax-calculator, sales-tax-calculator,
   savings-calculator, tip-calculator, age-calculator, amortization-calculator,
   annuity-calculator, bra-size-calculator, compound-interest-calculator,
   currency-calculator, engine-horsepower-calculator, gpa-calculator,
   horsepower-calculator, investment-calculator, resistor-calculator,
   retirement-calculator. That is ~403KB paid by every visitor on every view of
   those pages for a feature most never use, and the guide already forbids it.
   Worth a dedicated commit.
2. **`check_adsense.py` and `check_originality.py` do not exist in `scripts/`**
   even though the guide's AdSense section instructs running them before every
   push. Only `sync_header_footer.py` is there. The equivalent checks were run
   by hand this session; writing the two scripts once would make that repeatable.
3. **Only 3 pages link to /payment-calculator/** (all-calculators, sitemap,
   business-loan-calculator). Adding it to the sidebar of loan-calculator,
   auto-loan-calculator and amortization-calculator is cheap inbound equity.

## Pension Calculator — rebuilt Aug 4, 2026

Owner request, with the calculator.net page and four screenshots supplied. Built under the
section 3a-PRIME parity protocol. This is the largest single page on the site so far:
three independent calculators, two charts and seventeen inputs.

**Before:** the slug held a completely different tool — a defined-benefit formula estimator
(years of service x final average salary x multiplier), 369 words, three H2s, four FAQs.
None of the three decision calculators the reference page is actually known for existed here.

**Keyword research (section 4), before any copy.** The bare head term "pension calculator"
is ambiguous in US search — it pulls DB-formula tools and UK pension-pot calculators as often
as the payout decision. The dominant high-intent cluster is **"pension vs lump sum
calculator"**, which has dedicated pages at Schwab MoneyWise, Ameriprise, Fidelity, Clark
Howard, SmartAsset and a long tail of advisor sites. Per section 8 that phrasing went into the
title and meta while the H1 and slug keep "Pension Calculator". Secondary clusters targeted in
H2s and FAQs: single-life vs joint-and-survivor, pension maximization / life insurance instead
of a survivor benefit, and "should I retire early or work longer". Title 48 chars, description
159.

**Reverse-engineering the reference maths.** Nothing about the three calculators' conventions
is documented, so they were derived from the reference tool's own output: the two SVG charts
were decoded back to dollar values by calibrating against their gridlines, and the exact
integer figures printed by the second calculator were used as fixed targets. The result is
that the three calculators do **not** share one convention:

- **Calculator 1 and 3** value each year's pension total at the *middle* of that year —
  discount exponent `j + 0.5`, with the year count being `death age - retirement age`. Fitted
  against 56 decoded chart points spanning ages 66-120; worst error 0.006%.
- **Calculator 2** values the survivor stream at the *start* of each year (exponent `j`) and
  counts spans *inclusively*: a spouse aged 62 with life expectancy 82 gets 21 payments, not
  20. That convention reproduces all three of its printed figures to the dollar —
  $657,173 replacement lump sum, $514,709 invested difference, $428,530 remaining survivor
  value. The "20 years" quoted for the term-life comparison is the non-inclusive span, which
  is a separate quantity in their own text.

Engine verified in Node before being wired into the page: 17 assertions, all passing,
including three independent break-even probes for calculator 1 fetched live with different
inputs (ages 81, 81, 101 — all matched).

**One deliberate deviation, flagged rather than copied.** The third calculator's verdict
sentence is off by one year. With the reference defaults it says to retire at 65 if you live
to 86, but at 86 retiring at 60 is still ahead by $3,105 — and their own chart on the same
page shows the earlier-retirement line above the later one at that age. Probed with four
different input sets and the error is systematic: their stated age is always one year early,
by $1,158 to $5,850 of remaining gap. Calculator 1's break-even, by contrast, matched exactly
on every probe, so this is specific to the third tool rather than a difference of convention.
We report the first age at which working longer genuinely wins (87 on the defaults) and say so
on the page. Same reasoning as the FHA upfront-MIP deviation already recorded in the guide:
match the field, not the error.

**Built** on the established 3-card pattern with a `pen-` prefix. Three tabs swap the form
fields and the result layout; tabs 1 and 3 render a two-series present-value line chart with
life expectancy on the x-axis, tab 2 renders a two-bar comparison instead since the reference
shows no chart there. Bottom grid pairs a value-by-age table with a standing "before you elect
anything" card covering irreversibility, spousal consent, pre-tax figures and PBGC caps.
Defaults deliberately differ from the reference throughout.

**Two real defects caught by looking at the render, not the DOM** — both would have passed
every node-level assertion:
1. The chart legend on tab 1 was reversed. Series A is the pension value and series B the flat
   lump sum, but the labels were passed in the opposite order, so the rising navy line was
   captioned "Lump sum". The table's column headers had the same swap.
2. On tab 2 the comparison bars ran to the edge of the viewBox and their value labels were
   clipped mid-number ("$360,4"). Fixed by reserving label width; the tab-2 table also had a
   stray empty fourth column, now three columns with the explanation left-aligned.

**Verification before push**
- Protected shared style block byte-identical to the pre-edit file and to bmi-calculator's.
- JSON-LD all parses; BreadcrumbList left in `<head>` per convention and corrected there to
  match the visible trail ("Pension Calculator", and the Finance step pointing at
  /all-calculators/#fin) — the stub had the older short-name form.
- FAQ schema generated from the same list as the visible HTML; 8/8 exact string equality.
- Inline JS passes `node --check`; sitemap.xml parses.
- Playwright, desktop 1280px and mobile 390px, 22 assertions each, all passing: every tab,
  all three calculator.net parity cases typed in live, both validation paths (joint pension
  not below single-life; second retirement age not later than the first), h1 computed weight
  700, zero console errors, zero horizontal overflow.
- jsPDF: nothing fetched on load, downloads on first click, no re-fetch on the second.
- Originality: 0.00% 8-word-run overlap with the reference page. Against our own articles the
  worst is 0.10% once byline and disclaimer boilerplate are excluded.

Article is 2,028 words, 8 H2 sections, 8 FAQs, 12 distinct internal links. New OG image;
sitemap lastmod refreshed; the folder's stale Next.js RSC payload files removed as with the
payment page.

## Personal Loan Calculator — rebuilt Aug 4, 2026

Owner request with the calculator.net page and two screenshots. Section 3a-PRIME protocol.

**Before:** a 224-word stub with two FAQs and six inputs — loan amount, rate, term and a currency
selector — producing a payment and total interest. No origination fee, no insurance, no APR, no
schedule, no chart. The reference tool's entire reason for existing (turning a quoted rate plus a
fee into a real APR) was missing.

**Keyword research (section 4) before any copy.** "Personal loan calculator" is one of the more
contested finance terms in US search — NerdWallet, Bankrate, Wells Fargo, OneMain, LendingTree and
a long tail of credit unions all hold pages. Reading what they actually do was the useful part:
the bank and credit-union tools (Wells Fargo, OneMain, Landmark, SCU) return a monthly payment and
stop. Only NerdWallet and calculator.net handle the origination fee and convert it into an APR,
and NerdWallet's own page copy leads with "with or without an origination fee". That is the gap
worth owning, so the title leads on fees and true APR rather than competing on the bare head term.
Title 55 chars, description 150.

**Parity work.** Nine input controls, including two the stub had no equivalent of: the % / $
selector on the fee amount and the deducted-vs-upfront radio pair. Result rows are conditional and
that conditionality had to be derived rather than guessed — four separate result URLs were fetched
(no fee; fee deducted; fee upfront; fee deducted plus insurance) to establish which rows appear
when. "Cash received" only shows when a fee is deducted; "Monthly pay + insurance" and "Total
insurance" only when a premium is entered; "Origination fee", "Cost of loan" and "APR" whenever the
optional panel is on. The donut's segments change with the same logic — deducted shows cash
received, upfront shows the full loan amount.

**A non-obvious finding worth recording:** the APR is identical whether the fee is deducted or paid
upfront. Both leave the borrower holding the loan minus the fee and repaying the full balance, so
the cash flows match; only the day-one cash position differs. Verified against the reference, which
prints 12.239% for both, and now explained in the article because it is the sort of thing a
borrower assumes must differ.

**Verified in Node before wiring anything in** — 11 figures reproduced exactly: $424.94 payment,
$25,496.45 total, $5,496.45 interest, $1,000.00 fee, $19,000.00 cash received, $6,496.45 and
$9,496.45 cost of loan, $474.94 payment-with-insurance, $3,000.00 total insurance, and the APR at
12.239%.

**One deviation, at the rounding level.** APR was probed across seven input sets. Five match to the
printed digit. Two differ by 0.001 percentage points, and critically they differ *in opposite
directions* — ours 9.377855 (displays 9.378) where they print 9.377, and ours 17.267970 (displays
17.268) where they print 17.269. A systematic convention difference would push the same way every
time; opposite drift is their solver's tolerance in the last digit. Ours is a 300-iteration
bisection on the standard APR definition. Recorded as an intentional difference; the magnitude is
one part in twenty thousand.

**Built** on the 3-card pattern with a `pl-` prefix. No tabs here — the reference is a single
calculator with a collapsible fee panel, so the panel is a checkbox-revealed block rather than a
tab. Annual schedule carries the date-range column (8/26-7/27) and the monthly view carries per-month
dates with end-of-year separators, both matching the reference. Start date defaults to the current
month via JS rather than shipping a hardcoded date that goes stale.

**Two things fixed after looking at the rendered page, not the DOM:**
1. The fee amount row showed "3 %" inside the input *and* a "%" dropdown beside it — the unit stated
   twice on one line. The reference does this too; we dropped the in-field marker and kept the
   dropdown.
2. The result sub-line read "Before fees this is a $381.13 payment", which is misleading — the
   payment is $381.13 either way; what the fee changes is the cost, not the installment. Reworded.

**Internal duplication caught and fixed.** First measurement showed 1.42% eight-word-run overlap
with payment-calculator, above the guide's ~1% line. The overlap was real: the amortization formula
explanation and a few stock sentences were near-identical prose I had written on both pages.
Rewrote four passages — the formula paragraph, the first FAQ answer, the variable-rate bullet and
the worked example — and it fell to 0.24%. The worked example's new figure ($143.79 of the first
payment being interest) was checked in Node rather than asserted.

**Follow-up fix, same day (owner spotted it).** The months half of the loan-term row rendered its
value invisibly on desktop. Both halves shared `flex:1` with `min-width:0`, and because the word
"months" is wider than "years" the second input collapsed to 32px — after padding and the space
Chrome reserves for the number spinner, there was nothing left to show the digit in. Measured
rather than guessed: 43px vs 32px at 1280px wide. Fixed by giving the two boxes an equal
`flex:1 1 0` basis, tightening the unit labels, right-aligning the figures against them and
suppressing the spinner on those two fields only. Now 49px and 39px, nothing clipped, checked at
1280, 768 and 390px. Worth remembering as a pattern: any field-control holding two input groups
with different-length unit labels will do this.

**Verification before push**
- Protected shared style block byte-identical to the pre-edit file and to bmi-calculator's.
- JSON-LD parses; breadcrumb corrected in `<head>` to match the visible trail.
- FAQ schema generated from the same list as the visible HTML; 8/8 exact.
- Inline JS passes `node --check`; sitemap.xml parses.
- Playwright desktop 1280px and mobile 390px, 39 assertions each, all passing: all four reference
  configurations typed in live, both fee units, the reference's own year-1, year-5 and month-1
  schedule rows matched character for character, monthly view 60 rows with 4 separators, and five
  edge cases (blank amount, fee >= loan, months-only term, zero term, 0% rate).
- jsPDF: nothing on load, downloads on first click, no refetch on second.
- SEO audit, 21 checks, all clear. Originality 0.00% against the reference page.

Article 1,857 words, 8 H2, 8 FAQs, 12 internal links. New OG image; sitemap refreshed; stale RSC
payload files removed.

## Present Value Calculator — rebuilt Aug 4, 2026

Owner request with the calculator.net page and a screenshot. Section 3a-PRIME protocol.

**Before:** a 212-word stub covering only the single-amount case, with two FAQs. The reference
page's second calculator — the present value of a stream of deposits, which is the half most
people actually arrive looking for — did not exist here, nor did the schedule or chart.

**Keyword research (section 4).** "Present value calculator" is held by Omni, CalculatorSoup,
FinancialMentor, MoneyChimp and Stanford's IFDM alongside calculator.net. Reading what they do was
the useful part: MoneyChimp handles only a lump sum, and FinancialMentor splits the two cases
across separate pages and links between them, which tells you "present value of annuity calculator"
is a distinct query with its own demand. Doing both in one tool, with the period-by-period
schedule, is the position worth taking, so the title carries both. Title 49 chars, description 144.

**Parity.** Two calculators, eight input controls including the beginning/end timing radio pair.
Both modes verified in Node before any code was wired in — 18 assertions, all passing: $558.39 and
$441.61 for the single amount; $736.01 / $1,318.08 / $1,000.00 / $318.08 for deposits at period
end; $780.17 / $1,397.16 / $397.16 at period beginning; and five sampled schedule rows in each
timing mode reproduced to the cent, including the reference's slightly odd column mix where
"Deposits" is cumulative but "Interest" is per-period.

No deviations found. Every figure the reference prints, we print identically.

**Two additions beyond the reference, flagged rather than silent:** a principal/interest donut on
the single-amount tab (the reference shows one only on the deposits tab), and a schedule plus chart
for the single-amount tab showing the present value compounding back up to the future amount. Both
exist because our result card and bottom grid would otherwise sit empty on that tab; neither
changes any number.

**Built** on the 3-card pattern with a `pv-` prefix, two tabs, stacked bars matching the
reference's accumulated-deposits-plus-interest chart.

**Fixed after looking at the render:** the chart card was stretching to the height of the 15-row
schedule beside it, leaving roughly 200px of empty white below the legend. `align-items:stretch`
on the bottom grid changed to `start`; card heights now 509px and 310px. Worth noting for future
builds — stretch only looks right when the two cards are naturally similar in height, which was
true on payment-calculator's five-row table and false here.

**Second follow-up, same day (owner spotted it).** The form and result cards were badly mismatched
in height on the first tab. Measured across the rebuilt pages before touching anything, because
the question was whether this page was out of line or the whole pattern was: payment-calculator
54px apart, personal-loan 46px, pension 16px, present-value 187px. So it was this page.
Two causes, both fixed:
1. The donut legend label "Growth to future value" was long enough to wrap, which pushed the
   legend column past the 150px donut and made the whole block 242px instead of the 174px every
   other page gets. Shortened to "Growth".
2. The result card carried "Periods" and "Discount rate" rows that only repeated the two inputs
   sitting a few centimetres to the left. The reference shows neither. Removed from the card and
   added explicitly to the PDF export instead, so nothing is lost from the saved report.
Now 35px apart on the first tab and 4px on the second, inside the range the other pages sit in.
General lesson for the pattern: a result card's height is driven by the donut legend's longest
label as much as by its row count, and rows that merely echo an input are worth removing anyway.

**Verification before push**
- Protected shared style block byte-identical to the pre-edit file and to bmi-calculator's.
- JSON-LD parses; breadcrumb corrected in `<head>` to match the visible trail.
- FAQ schema from the same list as the visible HTML; 8/8 exact.
- Inline JS passes `node --check`; sitemap.xml parses.
- Every figure quoted in the article body was checked in Node rather than asserted: 1.045^8 =
  1.4221, $17,579.63, the $13,507 comparison at 8%, and $736.01 x 1.06 = $780.17.
- Playwright desktop 1280px and mobile 390px, 32 assertions each, all passing: both tabs, both
  timing modes, all reference schedule rows compared string-for-string, and six edge cases (0% rate
  in each mode, blank deposit, zero periods, over 600 periods, rate above 100).
- jsPDF: nothing on load, downloads on first click, no refetch on second.
- SEO audit 21 checks clear. Originality 0.00% against the reference; worst against our own pages
  0.31%.

Article 1,782 words, 8 H2, 8 FAQs, 12 internal links. New OG image; sitemap refreshed; the folder
had no stale RSC files left to remove.

## Card width alignment — personal-loan and present-value, Aug 4, 2026

Owner pointed at margin-calculator as the standard: the value-input card and the result card should
be the same width. Height is expected to vary with how much each side has to show and is not part
of this.

Measured before changing anything. margin-calculator resolves to 390 / 382 / 300 (form / result /
sidebar) at 1280px — an 8px gap. The two pages named were running their own column values,
`360px minmax(360px,1fr) 285px` and `355px minmax(360px,1fr) 285px`, which resolved to 390/427 and
390/432 — 62px and 77px apart, with the result card visibly wider.

Both now use margin-calculator's exact declaration:
`minmax(300px,390px) minmax(320px,1fr) minmax(250px,300px)`. Verified identical to
margin-calculator at 1440, 1280, 1024 and 900px (the last stacks), zero horizontal overflow at
every width, and both full test suites still passing.

**One thing tried and backed out.** At the narrower result width the donut legend on these two
pages dropped below the donut instead of sitting beside it, so the donut was shrunk to 128px to
make room. Then margin-calculator was measured properly: its donut is 150px, the same as everywhere
else, and its legend fits only because its labels are short ("Cost $185 71%"). Shrinking ours would
have introduced a new inconsistency to solve a problem the owner had not raised, so it was reverted.
The legend wrapping below the donut at narrower widths is existing site behaviour —
payment-calculator does the same thing at 1024px. Final diff is one line per file.

**Still on the old column values:** payment-calculator (390/422, 32px apart) and pension-calculator
(390/432, 42px apart) at 1280px. Left alone because the owner scoped this to two pages; worth
folding into the final audit pass if site-wide consistency is wanted.

## Real Estate Calculator — built from research, Aug 4, 2026

Owner flagged that calculator.net's real-estate page carries no calculator, only links, and asked
for the design to come from researching the wider field instead. Verified their observation first:
that page has one input on it and the input is the site search box.

**What the research showed.** "Real estate calculator" splits into two intents. calculator.net and
ELIKA answer it as a hub — a list of seventeen or twenty links. FinancialMentor, WealthBuilders and
Wikipedia's "property investment calculator" entry answer it as investment analysis: cap rate, cash
flow, cash-on-cash. A second search on the selling side turned up a dense field — HomeLight,
Casaplorer, SoldNest, EstatePass, AskDoss and several others all run dedicated seller net-proceeds
tools, and all of them lead with the same finding, that sellers hand over 6-10% of the price before
the loan payoff.

**The problem that decided the design.** We already have `/rental-property-calculator/`, and it
already does cap rate and cash-on-cash. The `/real-estate-calculator/` stub was doing exactly the
same thing — its title even read "Real Estate Calculator — Cap Rate". Building another cap-rate tool
here would have set two of our own pages against each other for the same query. Meanwhile we had no
seller-side calculator anywhere on the site, against a field of competitors who all have one.

So the page answers the umbrella query with three working calculators covering the three moments
money actually moves, two of which were site-wide gaps:
1. **Buying** — cash to close. Down payment plus closing costs plus prepaid escrow, less seller
   credit. Our mortgage and down-payment pages give the monthly figure; none gave the day-one cash.
2. **Selling** — net proceeds. Price less payoff, commission, title/escrow, transfer tax,
   concessions and repairs. Nothing on the site covered this at all.
3. **Renting out** — a one-year return screen. Kept deliberately as a snapshot, with a prominent
   link to `/rental-property-calculator/` for the full hold-period projection, so the two pages have
   distinct jobs rather than competing.

**No reference implementation exists**, so every figure was hand-derived and checked in Node rather
than matched against someone else's output: 22 assertions covering cash to close ($107,100), net
proceeds ($141,750 with costs at 8.94%), NOI ($20,280), cap rate (5.96%), and the P&I payment
($1,662.41) cross-checked independently against the annuity formula. Edge cases included a seller
credit, an all-cash purchase, and an underwater sale where the payoff exceeds the price — that last
one correctly returns a negative net and tells the seller what they would have to bring to closing.

**One current fact worth getting right.** The 2024 NAR settlement ended MLS-advertised buyer-agent
compensation and made it a purchase-agreement negotiation. National averages through 2026 sit nearer
5.5% than the old 6% where a seller pays both sides. The commission field defaults to 5.5% and the
article explains why treating 6% as fixed is now a mistake.

**Second follow-up, same day.** The total row's background was `--surface-sunken`, which resolves
to #F3F1EA — the exact same colour as the page background, rgb(243,241,234). The row therefore
disappeared into the page and read as though it had fallen outside the card. Measured rather than
eyeballed: the two computed values were identical. Replaced with the navy already used for the
table header, so the table is bookended, with a white label and a light-green figure. Contrast on
navy is 11.5:1 for the label and 7.1:1 for the figure, both clear of the 4.5:1 WCAG AA threshold.
Applies to all three tabs. General note: `--surface-sunken` is the same colour as the page
background, so it only works as a tint *inside* a white card, never as the last row of one.

**Follow-up fix, same day (owner spotted it).** The buying tab's breakdown table ended on a total
row with an empty third cell, which read as a hole at the bottom of the table. The sell and
invest tabs both fill that cell; only this one had been left as `''`. Filling it with a number
was not enough on its own — the column had been "Share of cash" measured against the pre-credit
subtotal, which gives no sensible figure for the row that comes after the credit. Switched the
column to "Share of price", matching the sell tab, so every row divides by the same denominator
and the total lands on something worth reading: cash to close is 23.80% of the purchase price on
the defaults. Also stopped a zero seller credit rendering as "-$0.00".

**Verification before push**
- Protected shared style block byte-identical to the pre-edit file and to bmi-calculator's.
- JSON-LD parses; breadcrumb corrected in `<head>` to match the visible trail.
- FAQ schema from the same list as the visible HTML; 8/8 exact.
- Inline JS passes `node --check`; sitemap.xml parses.
- Playwright desktop 1280px and mobile 390px, 32 assertions each, all passing, including the card
  widths resolving to 390/382/300 to match margin-calculator.
- One test failure turned out to be the test's fault, not the page's: it set a $5,000 seller credit
  and then ran the all-cash case without clearing it, so $462,100 was the correct answer and the
  expectation was wrong. Test corrected rather than the calculator.
- jsPDF: nothing on load, downloads on first click, no refetch on second.
- SEO audit 23 checks clear. Originality 0.00% against calculator.net's hub page and 0.00% against
  every one of our own articles.

Article 1,918 words, 8 H2, 8 FAQs, 12 internal links including five "which calculator you actually
need" pointers. New OG image; sitemap refreshed.

**Follow-up worth doing:** `/rental-property-calculator/` is still a 295-word stub. Now that this
page holds the one-year snapshot, that one should be built as the multi-year projection with
appreciation, loan paydown and sale proceeds, which keeps the two clearly separated.

## Refinance Calculator — rebuilt Aug 4, 2026

Was a 393-word template stub with 7 inputs that only compared monthly payments and used the
naive `closing costs / monthly saving` break-even. Rebuilt to the 3-card pattern (`rfi-` prefix)
with full field parity against calculator.net.

**Parity work (section 3a-PRIME).** Their page computes client-side, so the raw HTML gave the
input set but no results. Submitted their form by GET to recover the rendered result block, then
ran five more scenario submissions to pin down behaviour that is invisible in a single sample:

- **Points are a percent of the NEW loan amount**, including any cash out (verified: cash-out
  50k moved upfront cost 6,500 -> 7,500).
- **APR** solves `(new loan - upfront) = payment x annuity factor`, i.e. on money actually received.
- **Remaining term is floored**, not rounded (payment 1,800 -> 285.70 months displays 285; payment
  2,000 -> 224.55 displays 224). Total payments then use that integer count.
- **Known sell price back-solves an implied appreciation rate** for interim years.
- **Break-even is NOT closing costs / monthly saving.** It is the first month where cumulative
  payment savings PLUS the equity gap between the two loans exceeds the upfront cost. Confirmed
  on three independent scenarios (30, 32 and 33 months) where the naive formula gives 728, 44 and 31.
- Rows are conditionally hidden: no mortgage row when the loan is cash, no break-even line when the
  new payment is higher, no faster/slower line when both terms match.

**Numeric verification.** Node model checked against their output before any page code was written:
6 scenarios x 45 assertions, all exact to the cent, including a row-level check of 7 sampled years.
The same 5 scenarios were then re-run through the finished page in Playwright and matched again.

**Keyword research (section 4).** Head term "refinance calculator" is held by Zillow, Bankrate,
NerdWallet and calculator.net; Zillow titles theirs literally "Should I Refinance?". The best
long-tail cluster is **"refinance break even calculator"** — Bankrate, Churchill, Refi.com and
mortgagecalculator.org each run a *dedicated page* for it, which marks it as a real query cluster
rather than a phrasing variant. Title targets the head term plus that cluster:
"Refinance Calculator — See Your Break-Even Point & Savings" (58 chars).

**Differentiation angle.** Every major competitor states the naive break-even formula. Ours counts
the equity difference, which is both more correct and a defensible content angle — the article
explains why, using the page's own default figures (naive says 16 months, correct answer is 12)
and the extreme case where the naive method reports decades for a refinance that pays back in years.

**Audit fixes before shipping.** Two real defects were found and fixed: 124px horizontal overflow on
mobile (grid items default to `min-width:auto`, letting the chart's min-width escape its scroll
container), and `$-253.55` sign placement corrected to `-$253.55` per US convention — calculator.net
renders the former, but only their maths is copied, not their formatting.

FAQ schema is generated programmatically from the article HTML at build time rather than hand-typed,
which structurally removes the em-dash/quote mismatch failure mode the guide has hit on every
previous rebuild. Verified exact.

Article 2,500 words, 10 H2, 8 FAQs, 9 internal links. New OG image. Sitemap lastmod refreshed.
Protected style block byte-identical to bmi/tip/body-fat/real-estate. jsPDF lazy (0 requests before
click, 2 after). Desktop and mobile both 0px overflow, zero page errors. 10 edge cases (0% rates,
garbage text, negatives, empty, payment-below-interest, $2.5M balance) produce no NaN/Infinity.

Input fields: 13/13. Result fields: 15/15.

**Note for the deferred audit list:** the shared head preloads
`/_next/static/chunks/36m08sdd6fi_4.js` but nothing consumes it, so every rebuilt page (confirmed on
real-estate, present-value and this one) logs a console warning ~4s after load. Pre-existing and
site-wide, not introduced here — belongs with the other deferred items.

## Rental Property Calculator — rebuilt Aug 5, 2026

Closes the follow-up left open by the Real Estate Calculator entry above: this page was a 295-word
template stub with 6 inputs (price, down payment, rate, term, rent, vacancy) that printed a single
monthly cash-flow number. It is now the multi-year projection the site was missing — appreciation,
loan paydown, equity build-up and sale proceeds — which is the split those two pages were always
meant to have. `/real-estate-calculator/` keeps the one-year snapshot; this page owns the hold-period
question.

**Reference audit went further than usual, and it paid off.** calculator.net computes this page
server-side, so the arithmetic is not in the fetched HTML at all. Their form submits by GET, so
instead of guessing, the whole calculation was reverse-engineered by **probing their live endpoint
with eight parameter sets** and reading the rendered output back. That surfaced three rules that
were nowhere in the source and would have been wrong if assumed:
- **Management fee is charged after vacancy**, on rent actually collected — 10% of $22,800, not of
  $24,000. Their own "Total Rental Income" line is net of both.
- **A known sale price is converted to an implied appreciation rate**, `(sell ÷ base)^(1/hold) − 1`,
  and applied to every intermediate year, so the equity column stays consistent in year three.
- **With repairs enabled the appreciation base becomes the after-repair value**, not the price, and
  the cap-rate label switches to "Purchase Capitalization Rate" while still dividing by the price.

**Numeric verification.** The model was written independently in Node first and matched against all
eight probes before any of it was wired into the page, then re-asserted in the browser through
Playwright. Every figure matches to the cent:

| Scenario | IRR | Total profit | Cash on cash | Cap rate |
|---|---|---|---|---|
| Their defaults | 18.42% | $402,304.36 | 874.57% | 8.05% |
| Management 10% | 14.89% | $341,039.90 | 741.39% | 6.91% |
| Repairs on | 15.35% | $482,001.70 | 730.31% | 8.05% |
| All cash | 10.56% | $558,937.50 | 271.33% | 8.05% |
| Known sale price | 18.73% | $437,979.89 | 952.13% | 8.05% |
| Hold 35yr / 30yr loan | 17.62% | $1,099,849.11 | 2,390.98% | 8.05% |

Row-level parity is asserted too, not just the summary: the whole first-year table (9 rows × monthly
and annual), the Begin row, years 1, 2 and 20 of the schedule, and the Total row all match their
published output exactly. Year 31 of a 35-year hold correctly shows $0 mortgage.

**Input parity: 23/23.** Purchase price, use-loan toggle, down payment, rate, term, closing costs,
repairs toggle, repair cost, after-repair value, five operating-expense lines each with their own
compounding increase, rent and other income each with an increase, vacancy, management fee,
known-sale-price toggle, appreciation, sale price, holding period, cost to sell. Nothing dropped,
nothing merged.

**One deliberate deviation, flagged.** Their donut chart disagrees with their own table: it computes
vacancy and management on **gross** rent ($2,400 at 10%) while the table uses **collected** rent
($2,280), and it ignores other monthly income entirely — add $300/mo of parking income and the donut
does not move. Ours is computed from the same figures as the table, so the two always agree.

**Beyond parity.** An Annual/Monthly toggle on the schedule (240 monthly rows with exact loan
balances, and the last two columns swapping to cumulative cash flow and property value, since a
monthly IRR is not a meaningful number); a stacked bar chart splitting each year's rent into
mortgage, operating expenses and cash flow, with a separate amber "shortfall" segment when the year
runs negative; a "cash needed up front" row; and the headline number is **first-year monthly cash
flow**, not IRR — it is what the query is actually asking, and it turns amber when the property runs
at a loss.

**Chart sizing note worth remembering.** An SVG with `width:100%` and a fixed `viewBox` narrower than
its container does not stretch — `preserveAspectRatio` defaults to `xMidYMid meet`, so it scales to
the height and floats in the middle with dead space either side. This is visible in a screenshot and
invisible to every DOM check. Fixed by computing the viewBox width from `parentNode.clientWidth`
(1:1 with rendered pixels, so it stays crisp) and redrawing on a debounced resize. The same latent
issue exists on refinance-calculator and mutual-fund-calculator; worth folding into the audit pass.

**Keyword research.** Head term "rental property calculator" is heavily contested (Zillow,
BiggerPockets, TurboTenant, Omni, calculator.net). The distinct long-tail clusters that each have
dedicated competitor pages — and so are covered in H2s and FAQs rather than fought for in the title —
are cash-flow calculator, ROI calculator, cap rate, cash-on-cash return, investment property and
rental income calculator. Title: "Rental Property Calculator — Cash Flow, Cap Rate & ROI" (54 chars),
which carries three of those clusters and promises an outcome rather than restating the tool name.
Meta description 147 chars.

**Checks run.** 3 JSON-LD blocks valid; FAQ schema and visible text generated from a single Python
source and asserted byte-equal, which removes the em-dash mismatch failure mode structurally rather
than by care; 7 inline scripts pass `node --check`; protected shared style block byte-identical to
both refinance-calculator and body-fat-calculator; `apply_cb_ux.py` applied and its behaviour
asserted (bar sentence, `__cbAutoRuns` increments, `.cb-flash` on the full result card, jump link);
jsPDF fetches zero bytes until the button is clicked and is not re-fetched on a second click; zero
console errors and zero horizontal overflow at 1280px, 430px and 390px, with a single grid track and
every child at full width on mobile; 15 edge cases including negative cash flow, 0% interest, 100%
down, a 1-year hold, all costs at zero, Clear, and non-numeric input.

**Result layout reworked same day, after an owner review.** The first build followed the standard
3-card split: result card in the middle column, everything else in the bottomgrid. On this page that
failed, because the form carries 23 fields and is far taller than the other two columns. Measured at
1440px: form 1492px, middle 1013px, sidebar 756px — **479px of dead space**, with the "first year,
line by line" table stranded 1,511px below the result head. calculator.net, whatever else is wrong
with it, puts its summary and its first-year table side by side, so cause and effect are on one
screen. We had thrown that away.

Now: the first-year table sits in the middle column directly under the result card, the "how the
first year is built" explainer moved into the sidebar, and the bottomgrid holds only the full-width
breakdown-over-time card. Columns come out at 1492 / 1483 / 1223 — dead space gone. Mobile order is
unchanged (bar, form, result + first-year, breakdown, sidebar).

**Deliberate deviation from the shared cb-ux behaviour, flagged per section 5a.** The injected
`.cb-jump` ("See the full breakdown ↓") is hidden on this page via
`.rpc-area-result .cb-jump{display:none}`. The link exists to bridge a long scroll between the
result and the detail; that scroll no longer exists here, so the button pointed at something already
in view. The snippet is untouched — only this page's CSS hides it. If another page ever ends up with
its detail card adjacent to the result, the same one-liner applies; if that happens more than once
or twice, the snippet should learn to skip the link when the target is already near, rather than
each page hiding it by hand.

**A layout mockup was rendered and reviewed before any of this was pushed** — the change was applied
in the browser with `page.evaluate`, screenshotted before/after with the dead space outlined, and
approved. Worth repeating for any layout change: it costs one Playwright run and it caught that the
proposal was worth doing at all.

**Top spacing, fixed same day.** The page shipped with the guide's stated 3-card wrapper padding
(`py-8 sm:py-10`, a 41px gap between the sticky header and the breadcrumb). The owner compared it
against `/mortgage-calculator/` and the gap was visibly larger. Measured across pages: mortgage and
real-estate both use `py-5 sm:py-6` (21px), while rental and refinance used the larger value.
Rental now matches at 21px on both 1280px and 390px. **Left inconsistent on purpose:**
`refinance-calculator` still carries the 41px gap, and DESIGN_AND_SEO_GUIDE.md section 5 still
documents `py-8 sm:py-10` as the pattern. One of the two is wrong — worth settling in the audit pass
and then writing the winner into the guide, rather than fixing one more page unasked.

**Originality.** 3,088-word article, 8 H2 sections, 8 FAQs. Longest shared 8-word run with
calculator.net: **zero**. Highest overlap with any of our own pages: 0.65% (refinance-calculator,
boilerplate byline and disclaimer). 18 internal links; new OG image; sitemap lastmod refreshed.

## Rent Calculator — rebuilt Aug 5, 2026

Was a 2-input stub (gross monthly income, target percentage) printing one number. The reference page
is itself unusually thin — three inputs, four output figures and a **static PNG** for the
safe/acceptable/aggressive scale — so this is one of the few builds where matching parity took an
hour and the value came from what was added around it.

**Reference audit.** Their form submits by GET, so the arithmetic was recovered by probing the live
endpoint with nine parameter sets rather than guessed:
- "You can afford up to" = 36% of gross monthly income **minus existing monthly debt** (back-end DTI).
- "It is recommended to keep below" = 28% of gross monthly income minus debt (front-end DTI).
- The "1/3 of gross income" landlord note = gross monthly ÷ 3, **ignoring debt**, and it only appears
  when the 36% figure exceeds it — i.e. only when the landlord cap would actually bite. Confirmed by
  bracketing: debt $100 shows the note, debt $200 does not.
- When the 36% figure falls to zero or below, everything is replaced by a "hard to meet rent
  payments" message.

All nine cases match exactly, including their negative-recommendation case (income $5,000/mo, debt
$1,500 → recommended −$100) and the boundary where the maximum lands on exactly zero.

**Input parity: 3/3**, plus two additions. Their per-year/per-month control is a `<select>`; ours is
a segmented toggle, per the standing no-dropdown rule. Added: **share of income for rent** (default
30%, which RentCafe, Apartments.com and Zumper all expose) and **other housing costs** (utilities,
renters insurance, parking, pet rent), which feeds a total-housing-cost figure and never touches the
parity numbers — set the share to 30 and other costs to 0 and every reference figure is unchanged,
which the browser suite asserts directly.

**Result parity: 4/4**, and their static scale image is replaced by a real SVG drawn from the
visitor's own numbers, with a pointer at their target. Added rows: the 40× annual rent rule, the
annual income a landlord would want for the target rent, total housing cost and its share of gross
income, and an explicit warning row when the 36% maximum sits above the landlord's 3× cap — which is
the single most useful thing on the page, because that is the gap where someone gets approved for a
rent their budget cannot carry.

**Two defects caught in review, both worth recording.**
1. *The scale contradicted the article.* Green ran to 28% (matching the reference's boundary), so the
   default 30% target landed in the amber "a stretch" band while the article on the same page called
   30% the standard rule. Green now runs to 30%; the 28% front-end ratio stays as a result row. The
   lesson is that a chart's thresholds are content and have to agree with the prose.
2. *The disclaimer was inherited wholesale.* The build script was adapted from the rental-property
   page and a `str.replace` for the closing disclaimer silently failed to match, so a rent
   affordability page shipped a paragraph about depreciation recapture and "committing to a
   purchase". `check_originality` is what surfaced it — internal overlap read 4.32% against
   rental-property, and inspecting the overlapping runs showed one of them was 90 words of the wrong
   disclaimer. **Adapting a build script means every replace needs an assert, not a hope.** After the
   rewrite, overlap is 1.77% and both remaining runs are deliberate sitewide boilerplate (the byline
   and the About/Privacy tail).

**Keyword research.** The head term is "rent calculator", but the dominant query is *how much rent
can I afford* — it is the reference page's own H2 and every major competitor's H1. The second
cluster is the rules themselves: 30% rule, 3x rent, 40x rent, rent-to-income ratio. Title:
"Rent Calculator — How Much Rent Can I Afford? (30% Rule)" (56 chars), which carries the head term,
the full question and the biggest rule cluster while staying distinct from the reference's own
title. Meta description 153 chars.

**Checks.** 3 JSON-LD blocks valid; FAQ schema byte-equal to the visible text (same generator);
8 inline scripts pass `node --check`; protected shared style block byte-identical to two other
pages; `apply_cb_ux.py` applied and asserted; jsPDF lazy; zero console errors and zero horizontal
overflow at 1280/430/390px; 8 edge cases. One found a real defect — after Clear the share box was
empty and the whole result refused to render, so a blank share now falls back to 30% while an
out-of-range value still errors. Article 2,445 words, 8 H2s, 8 FAQs, zero 8-word overlap with the
reference. Columns balance at 813 / 976 / 764. New OG image; sitemap refreshed.

## Repayment Calculator — rebuilt Aug 5, 2026

Was a 508-line template stub. The reference page is a compounding-vs-payment-frequency loan engine
with two solve directions, and it computes server-side, so the arithmetic was again recovered by
probing the live endpoint — fifteen parameter sets this time, covering every compounding basis and
several payment frequencies.

**What the probes established** (none of it visible in their HTML):
- The periodic rate is `(1 + r/c)^(c/p) − 1`, with `c` compounding periods a year and `p` payment
  periods; continuous compounding collapses to `e^(r/p) − 1`.
- Their stated conventions matter and are load-bearing: **biweekly is 26 periods** (52 weeks) and
  **daily is 365.25** (leap years averaged in). Both appear only as footnotes on their result.
- A term entered as years and months converts to `(years×12 + months) × p / 12` and is **kept
  fractional**. This was caught by a case that did not match: biweekly over 3y5m is 88.83 payments,
  not 89, and rounding it broke the payment by 21 cents.
- The displayed payment count is `ceil(n)`; the term is rendered as whole years plus months to one
  decimal.

**Input parity: 7/7.** Balance, rate, 9-option compounding select, 8-option payback select, the
fixed-term / fixed-installment mode switch, years+months, installment amount. Their mode switch is a
radio pair; ours is the site's tab pattern, matching loan-calculator, which also keeps selects for
the two long frequency lists rather than forcing 9 options into tabs.

**Result parity: 5/5** — payment (or payoff term), payment count, total of all payments, total
interest, and the principal/interest donut. Their "View Amortization Table" popup becomes a proper
schedule card with a by-year / every-payment toggle, a stacked chart and a total row. Added rows:
effective annual rate (APY) alongside the nominal rate, the rate applied to each payment, and
interest as a share of everything repaid.

**Intentional difference, and it is the interesting one.** Where the term is fractional, the
reference reports total paid as `payment × n` — settling the loan partway through a period and
billing a part-period of interest. A loan does not work that way: the balance clears on the 65th
payment date and that final period carries a full period of interest. Our totals come from the
period-by-period simulation instead, which is 4c higher on their $200 case, 9c on the $90 case and
3c on the fractional-term case. Payment, payment count and the term wording still match exactly.
The deciding argument was internal consistency: the schedule table is generated from the same
simulation, so using their figure would have printed a total the rows below it do not sum to — the
exact fault found in their own rental-property donut two builds ago. The browser suite now asserts
the schedule sums to the printed total.

**Two build defects caught, both by checks rather than by eye.**
1. *The assert convention paid for itself immediately.* Adapting the rent-calculator build script,
   the disclaimer replacement failed to match again — same class of failure as yesterday, this time
   a trailing-space mismatch in the search string. Because the replacements now assert, it raised
   instead of silently shipping a rent disclaimer on a loan page. Worth noting that the assert fired
   *before* `build.py` was rewritten but *after* the page had already been generated once from the
   unpatched script, so the first output still had to be discarded — asserts belong before any
   generation step, not just before the write.
2. *The chart was unreadable.* Bars (a year of payments, ~$5k) and the balance line (~$18.5k) shared
   one axis, so every bar was flattened to a sliver. Split onto two axes with the right-hand scale
   labelled and the legend marking which line uses it. Bar width is also capped at 86px so a
   five-bar chart does not render as slabs.

**Keyword research.** "Repayment calculator" is a nearly uncontested head term in the US — the
reference and some UK sites hold it. The high-volume American phrasing for the same intent is
**"loan payoff calculator" / "how long to pay off my loan"**, held by Bankrate-tier sites and credit
unions. Title: "Repayment Calculator — Your Payment or Your Payoff Date" (55 chars), which keeps the
head term and promises both solve directions; the payoff-time cluster is carried in the H2s and FAQs
rather than fought for in the title. Meta description 152 chars.

**Checks.** 3 JSON-LD blocks valid; FAQ schema byte-equal to visible text; 8 inline scripts pass
`node --check`; protected shared block byte-identical; `apply_cb_ux.py` applied, and the suite
switches tabs before asserting auto-calculate, per the tabbed-page note in section 5a; jsPDF lazy;
zero console errors and zero overflow at 1280/430/390px; 8 edge cases including a payment below the
interest accrual, 0% interest, a blank months box and an absurd rate. A 1,826-payment daily schedule
caps at 600 rows with the cap explained. Article 2,152 words, 8 H2s, 8 FAQs, zero 8-word overlap
with the reference, 1.96% internal overlap and both runs are the deliberate byline and About/Privacy
boilerplate. Columns balance at 881 / 838 / 710. New OG image; sitemap refreshed.

### Deployment stall, Aug 5, 2026 — unresolved at end of session

The Repayment Calculator commit (`6ab77629`) is correct in the repo and passes every check, but
Cloudflare Pages did not publish it. `/repayment-calculator/` kept serving the old stub title and
`/og/repayment-calculator.png` returned 404 for more than 25 minutes, while the three commits before
it that session (rental-property restyle, rent-calculator, layout change) all went live within
~75 seconds each.

Ruled out from this side:
- **Not caching.** The response carries `cf-cache-status: DYNAMIC` and `cache-control: no-store`, so
  Cloudflare is genuinely serving an older deployment rather than a cached copy.
- **Not the file.** The committed HTML is 104,284 bytes, valid UTF-8, zero null bytes, zero stray
  control characters, and byte-identical to the copy that passed the browser suite.
- **Not repo size.** 1,055 tracked files, largest single file 390KB — far inside the Pages limits of
  20,000 files and 25MiB per file.
- **Not a bad push.** The commit is on `origin/main`; an additional empty commit (`b9a6bd7b`) was
  pushed to queue a fresh build and also did not publish.

**Most likely cause, unverifiable without dashboard access: the Cloudflare Pages free-tier build
quota of 500 builds a month.** The symptom fits exactly — builds simply stop being produced and the
last successful deployment keeps serving. Four pushes went out inside an hour that session, which is
the kind of burst that finishes off a monthly allowance.

**What to check first:** the Pages project's Deployments tab, for a deployment stuck in *queued*, or
marked *failed*, or a "build limit reached" notice on the account. If it is the quota, the fix is
either waiting for the monthly reset or upgrading the plan; if it is a failed build, "Retry
deployment" is enough, since this repo has no build step and Pages only uploads static files.

**Working note for future sessions:** do not respond to a stalled deploy by pushing more commits.
One empty commit to re-queue is reasonable; beyond that, each push consumes another build and makes
a quota problem worse rather than better. Verify the dashboard first.

## RMD Calculator — rebuilt Aug 5, 2026

Was a 508-line stub. This is the first build on this site whose accuracy depends on **published
government tables rather than a formula**, so the sourcing mattered more than the arithmetic.

**Where the numbers came from.** The reference computes server-side and does not ship its tables, so
guessing was not an option and neither was deriving them — the IRS periods come from a mortality
basis that cannot be reproduced to one decimal by hand. The tables were parsed directly out of
**IRS Publication 590-B, Appendix B** (fetched from irs.gov, 996KB of HTML, 35 tables with
`summary` attributes):
- **Table III, Uniform Lifetime** — ages 72 to 120, 49 values.
- **Table II, Joint Life and Last Survivor** — 5,611 published cells across 20 chunk tables,
  symmetrised to 10,201, then sliced to the part this page can reach (owner 73-120, spouse
  20 to owner-11) = 3,192 values.

Both are stored as **zero-padded tenths in a fixed-width string** read positionally, which puts the
whole of Table II in 9,576 characters instead of a 60KB+ JSON object. Uniform is 147 characters.

**Verification: 24 checks, all exact.** Thirteen distribution-period probes against the reference
plus eleven projection rows across both tables. The parsed data reproduced the reference's Joint
Life figures before any of it was wired into the page — (75,51) → 35.8, (75,36) → 49.7,
(75,20) → 65.1 — which is the strongest evidence available that both sides are reading the same
IRS table.

**Rules recovered by probing, not assumed:**
- The Joint table applies only when the spouse is sole beneficiary **and** more than ten years
  younger, measured by year of birth. Bracketed it: an 11-year gap uses Joint (25.3), a 10-year gap
  uses Uniform (24.6).
- **SECURE 2.0 start ages are handled correctly by the reference and by us**: age 73 for births up
  to 1959, age 75 from 1960. Confirmed at the boundary — born 1959 → first RMD 2032, born 1960 →
  first RMD 2035.
- The projection re-looks-up the period every year with **both** ages advancing, so a Joint-table
  case stays on the Joint table.
- Balance projection is `balance x (1 + return) − RMD`, distribution taken at year end.

**Input parity: 6/6. Result parity: 5/5**, including the fraction graphic (balance over period
equals RMD), which is the clearest thing on their page and worth keeping.

**Two intentional differences, both improvements rather than deviations:**
1. *A spouse under 20 is handled instead of refused.* Pub 590-B prints Table II from age 20, and the
   reference simply fails to produce a result below that. We use the age-20 row and say so in the
   result text. This errs toward a **larger** required withdrawal, which is the safe direction —
   the penalty is for taking too little, never too much.
2. *Periods print to one decimal everywhere*, matching the IRS's own formatting, so 22 appears as
   22.0. The reference prints "22". Formatting only; no figure differs.

**Beyond parity.** The full Uniform Lifetime table is rendered as a visible reference table in the
article, because "IRS uniform lifetime table" is its own query cluster. The result card names which
table was used and why. The RMD is shown as a percentage of the balance. The year selector
**rebuilds itself around the real current year on load**, so the page cannot silently go stale the
way a hard-coded list would — the reference's list stops at 2027.

**Note for whoever picks this up next: the title contains "2026" and needs an annual edit.** The
year-qualified query dominates this term (every competitor titles that way), so it is worth having,
but it is a maintenance item. The tables themselves should also be re-checked against Pub 590-B
whenever the IRS revises them — the current set has been effective since 2022.

**Keyword research.** Head term "RMD calculator" is heavily contested (NerdWallet, AARP, Schwab,
Fidelity, FINRA, Investor.gov). The gap worth taking: **Investor.gov explicitly refuses the
spouse-more-than-ten-years-younger case** and tells the reader to go and read Publication 590-B.
That is the one thing this page does properly, so it leads the subhead and gets its own sidebar
card. Title: "RMD Calculator 2026 — Required Minimum Distribution by Age" (58 chars). Meta 158.

**Checks.** 3 JSON-LD blocks valid; FAQ schema byte-equal to visible text; 8 inline scripts pass
`node --check`; protected shared block byte-identical; `apply_cb_ux.py` applied; jsPDF lazy; zero
console errors and zero overflow at 1280/430/390px; edge cases including a non-numeric birth year,
a negative balance, a zero balance (returns $0 rather than an error), a blank return rate, and an
age past 120 clamping to the table floor of 2.0. Article 2,141 words, 8 H2s, 8 FAQs, **zero** 8-word
overlap with the reference after rewording one unavoidable factual sentence. Columns balance at
868 / 768 / 756. New OG image; sitemap refreshed.

## ROI Calculator — rebuilt Aug 5, 2026

Was a 508-line stub. Small surface (five inputs, four outputs) but one genuinely non-obvious rule
hidden in it, which probing found and a formula would not have.

**The date convention is not days ÷ 365.25.** The obvious guess reproduces the reference's own
default case (1,609 days → 4.405 years) and then disagrees on almost everything else. Probing ten
date pairs showed the real rule:

    years = whole anniversary years + leftover days ÷ 365

The tells were the clean ones: 2020-01-01 → 2021-01-01 returns exactly 1.000 despite spanning 366
days, and 2000-01-01 → 2026-01-01 returns exactly 26.000 across 9,497 days. Neither is possible
under a flat day-count. The divisor for the leftover is **always 365, never 366** — confirmed by
2024-01-01 → 2024-07-01, which is 182 days in a leap year and returns 0.499 (365) rather than 0.497
(366). All ten date pairs and five ROI cases match exactly, fifteen checks in total.

**Input parity: 5/5. Result parity: 4/4** — gain (label flips to "Investment loss" on a negative
return, as theirs does), ROI, annualized ROI, investment length, plus the invested/profit donut.

**Two things the reference refuses that this page handles:**
1. *A total loss.* Return zero and theirs produces no result at all; here it prints −100.00% ROI and
   −100.00% annualized, which is simply what a wipeout is.
2. *Costs and fees.* An optional field, defaulting to zero so parity is untouched. When it is set,
   ROI after costs and annualized ROI after costs appear alongside the gross figures, and the
   headline stays gross so nothing about the comparison with the reference moves. Every serious
   source on ROI says to net off commissions and tax; none of the calculators surveyed except
   CalculatorSoup actually offers the field.

**Beyond parity.** Return multiple, time-to-double at the annualized rate, and a year-by-year table
with a matching stacked chart showing the original stake holding steady while the profit builds on
top. A fractional holding period adds an exact final row (0, 1, 2, 3, 4, 4.405) so the table always
lands on the real returned amount rather than stopping short. Default dates are set to today and
five years ago on load, so the page cannot go stale.

**Article figures were checked, and two were wrong.** The comparison table and the worked examples
were all recomputed in Node before shipping: 55.20% over ten years is 4.49% a year, not the 4.50% I
had written, and 60% over twelve years is 3.99%, not 4.00%. Both were corrected. Worth keeping as a
habit — an article that quotes rounded annualized rates is making arithmetic claims, and rounding
them by hand goes wrong about as often as it goes right.

**Keyword research.** Head term "ROI calculator" is crowded (Omni, CalculatorSoup, Gigacalculator,
DQYDJ, Corporate Finance Institute, calculator.net). The cluster worth carrying is **annualized ROI
and its equivalence to CAGR** — DQYDJ is the only major that states the two are the same thing, and
it is a real bridge between two separate query sets. Title: "ROI Calculator — Total and Annualized
Return on Investment" (58 chars). Meta 158.

**Checks.** 3 JSON-LD blocks valid; FAQ schema byte-equal to visible text; 8 inline scripts pass
`node --check`; protected shared block byte-identical; `apply_cb_ux.py` applied, and the suite
switches tabs before re-asserting auto-calculate; jsPDF lazy; zero console errors and zero overflow
at 1280/430/390px; edge cases including a zero stake, reversed dates, a same-day span and a zero
length. Article 1,961 words, 8 H2s, 8 FAQs, **zero** 8-word overlap with the reference. Built with
the schedule table and chart as two separate cards from the start, per the owner correction earlier
in the session. Columns balance at 846 / 758 / 809. New OG image; sitemap refreshed.

## Roth IRA Calculator — rebuilt Aug 5, 2026

Was a 508-line stub. Seven inputs, a two-column Roth-versus-taxable comparison, and three rules that
only probing could have found — plus a real arithmetic bug in the reference.

**Rules recovered by probing** (none of it visible in their HTML, which computes server-side):
- Both accounts **grow first, then take the year's contribution**: `balance x (1 + r) + contribution`.
  Contributing first would have shifted the age-30 row from $39,300 to $39,750.
- The taxable side is charged at the marginal rate on its growth **every year**, so it compounds at
  `r x (1 - tax)`. At 6% and 25% that is 4.5%, which reproduces their $38,850 first row exactly.
- **Contributions are silently capped at the IRS limit**, and the two capping rules are different:
  a typed amount is held at the limit for your *current* age for the whole projection, while
  "maximize" steps the limit up when you reach 50. Confirmed by a pair of probes at age 45 — typing
  $20,000 gives $150,000 of contributions (20 x $7,500) while maximize gives $166,500
  (5 x $7,500 + 15 x $8,600).

**Verification: 5 scenarios, all exact** — balance, contributions, taxable growth and tax across
defaults, a sub-limit contribution, a 45-to-67 run at 7% and 32%, and maximize from both 30 and 55.
The 35-row annual schedule matches the reference row for row at both ends.

**A bug in the reference.** Their Roth "Total interest" is one annual contribution too high:
$781,343 where balance minus contributions is $773,843. It is consistent across every scenario — the
gap is always exactly the final year's contribution ($7,500, $6,000, $8,600 depending on the case).
The giveaway is that their own Roth column does not add up: $292,500 + $781,343 = $1,073,843, not
the $1,066,343 they print two rows above. Their taxable column *does* reconcile
($292,500 + $611,660 − $152,915 = $751,245), so it is an off-by-one in one branch rather than a
different definition. We print $773,843 and the browser suite asserts that both columns reconcile.

**One intentional difference.** The reference caps an over-limit contribution and says nothing —
type $20,000 and you get $7,500 with no explanation. We cap identically but show a note naming the
limit for your age and the higher figure from 50. Same arithmetic, disclosed.

**Beyond parity.** The Roth advantage and the tax never paid as headline figures, growth as a share
of the balance, the after-tax return the taxable account actually earns (5.32% on a 7% return at
24%), and a three-line chart — Roth, taxable, and contributions — that shows the two accounts
diverging. Layout uses the stacked two-card pattern from rental-property, since the seven-column
schedule needs the full width.

**Article figures were computed, not estimated.** Three numbers in the FAQ were written from a rough
guess and checked in Node before shipping: the default projection is $807,921 with $597,921 of
growth, and $533,478 at a 5% return — I had written $832,000, $618,000 and $556,000. All corrected.
This is the second build in a row where hand-estimated article figures were wrong; the check is now
routine.

**Keyword research.** Head term is crowded but shallow — NerdWallet, Thrivent, Clark, and a long
tail of credit unions running the same white-label widget that only projects growth. Almost none of
them show the taxable comparison, which is this page's actual differentiator. Title:
"Roth IRA Calculator — How Much Will It Grow by Retirement?" (58 chars), aimed at the dominant
question rather than the head term alone; the comparison carries the meta description.

**Contribution limits are 2026 figures ($7,500 under 50, $8,600 from 50) and need an annual check**
against IRS.gov, alongside the income phase-out ranges quoted in the sidebar and article.

**Checks.** 3 JSON-LD blocks valid; FAQ schema byte-equal to visible text; 8 inline scripts pass
`node --check`; protected shared block byte-identical; `apply_cb_ux.py` applied; jsPDF lazy; zero
console errors and zero overflow at 1280/430/390px; edge cases including retirement age at or before
current age, a zero starting balance, a 0% tax rate (both columns land level, advantage $0), a 100%
rate, and a negative return. Article 1,982 words, 8 H2s, 8 FAQs, **zero** 8-word overlap with the
reference. Columns balance at 972 / 833 / 852. New OG image; sitemap refreshed.

## Simple Interest Calculator — rebuilt Aug 5, 2026

Was a 508-line stub. Four solve modes over one formula, two unit dropdowns, and a rounding fault in
the reference's schedule.

**Rules recovered by probing** (their page computes server-side, tab held in a hidden `ctype` field):
- Interest is `P x r x t` with **the term converted into whatever period the rate is quoted in**.
  All four unit pairs behave: annual rate with a term in months divides by 12 ($20,500), monthly rate
  with a term in years multiplies by 12 ($92,000), matching units leave it alone.
- On the **Term** tab the answer is always reported in **years**, and the rate's own unit decides the
  raw number — a monthly rate gives 16.67 months, printed as 1.39 years. The term dropdown is ignored
  there, because term is the output.
- On the **Rate** tab the answer is always **per year**, and the term's unit decides the raw number —
  10 months gives 5% a month, printed as 60% per year. Symmetric to the Term tab.

**Verification: 14 reference cases, all exact** — four unit pairs on Balance, principal and its
interest, and all four unit pairs on both Term and Rate.

**A rounding fault in the reference.** When the term comes out fractional, their schedule's final row
uses the *displayed* two-decimal term rather than the exact one. On their own worked example the last
row reads $402.00 of interest and a closing balance of $30,002.00 — two dollars above the $30,000
they printed as the answer four lines earlier. We use the exact remainder, so the final row is
$400.00 and the schedule closes on $30,000.00 exactly. The browser suite asserts that row.

**Beyond parity.** Calculation steps rendered as real working rather than a static string, a
principal/interest donut, the interest as a share of the balance, the total return on the principal,
and interest per year. Bottom row is the two-card schedule-and-chart pattern; the schedule is only
three columns so it sits side by side comfortably, and the chart card stretches to match it
(367 / 367 at 1440px).

**Article figures were computed before shipping,** including the full simple-versus-compound table at
1, 5, 10, 20 and 30 years — all five rows verified in Node, along with the $18,500 / 4.5% / 6-year
default, the eight-month unit example both ways, and the 16.67-versus-13.7-year term comparison.

**Keyword research.** The formula itself is a query: CalculatorSoup, NerdWallet and Vertex42 all put
"I = Prt" in their titles, and CalculatorSoup runs a second page for "A = P(1 + rt)". Those
competitors solve one direction each; the four-tab rearrangement is the differentiator, so the title
carries both: "Simple Interest Calculator — I = Prt, Solved Four Ways" (54 chars). Meta 158.

**Checks.** 3 JSON-LD blocks valid; FAQ schema byte-equal to visible text; 8 inline scripts pass
`node --check`; protected shared block byte-identical; `apply_cb_ux.py` applied, and the suite
switches tabs before re-asserting auto-calculate; jsPDF lazy; zero console errors and zero overflow
at 1280/430/390px; edge cases including a zero principal, a 0% rate on both the Balance tab (balance
unchanged) and the Term tab (explained rather than dividing by zero), and an end balance below the
principal. Article 1,548 words, 8 H2s, 8 FAQs, **zero** 8-word overlap with the reference.
New OG image; sitemap refreshed.

## Social Security Calculator — rebuilt Aug 5, 2026

Was a 508-line stub. Two calculators on one page, and the hardest model recovery of the session.

**How the model was pinned down.** The reference prints one sentence per calculator, which is far too
little to fit a discounting model against. The leverage came from **the chart**: its nine bars are
plain SVG rects, so their heights are nine data points. Reading them out gave the relative lifetime
value of every claiming age from 62 to 70, and fitting against that turned a guess into a
measurement.

The first attempt matched the best age and the benefit multiplier but got the *curve* wrong — too
flat early, too steep late, eight bars out. A search over the discount factor and the horizon found
the fault in one place: the benefit stream runs **through the life-expectancy year inclusive**, one
year more than I had. The fitted discount factor came back as 0.98096 against the theoretical
(1 + cola) / (1 + return) = 0.980952, i.e. the discounting was right all along. With the horizon
fixed, all nine bars match to 0.01% and the RMS error is 0.003%.

**Rules confirmed:**
- Full retirement age follows the SSA schedule: 66 to birth year 1954, plus two months a year to
  1959, then 67.
- Early claiming costs 5/9 of 1% a month for the first 36 months and 5/12 of 1% beyond; delaying
  adds 2/3 of 1% a month and stops at 70. At a full retirement age of 67 that gives 70% at 62 and
  124% at 70, matching their text.
- Someone already past 70 gets a "claim now" message rather than a calculation — found by probing a
  1955 birth year, which returns a different sentence entirely.

**Verification: 17 checks, all exact** — 9 chart bars, 4 best-age scenarios across different life
expectancies and rate assumptions, and 4 break-even cases on the second calculator.

**The result card was deliberately kept lean,** following the owner's instruction earlier in the
session. Four rows on the best-age tab and three on the compare tab, and the browser suite asserts
that **no row simply repeats a value the user typed** — it pulls every input value and every result
value and checks the sets do not intersect. Everything shown is something the calculator worked out:
the full retirement age derived from the birth year, the benefit multiplier at the chosen age, and
the two anchor points at 62 and 70 for comparison.

**Keyword research.** "Social security calculator" is dominated by SSA.gov itself plus AARP,
Bankrate and NerdWallet. The differentiated cluster is the decision rather than the estimate: "best
age to claim social security", "social security break even age", "claim at 62 or 70". Title:
"Social Security Calculator — Best Age to Claim Benefits" (55 chars).

**Checks.** 3 JSON-LD blocks valid; FAQ schema byte-equal; 8 inline scripts pass `node --check`;
protected shared block byte-identical; `apply_cb_ux.py` applied; jsPDF lazy; zero console errors and
zero overflow at 1280/430/390px; edge cases including a life expectancy below 62, a second claiming
age earlier than the first, and a delayed option paying less than the early one. Cards finish level
at 440/442. Article 1,545 words, 8 H2s, 8 FAQs, **zero** 8-word overlap with the reference.
New OG image; sitemap refreshed.

## Student Loan Calculator — rebuilt from stub (Aug 6, 2026)

Replaced a 392-word, 3-H2 template stub with a full three-tab tool at
`/student-loan-calculator/`. Reference page: calculator.net/student-loan-calculator.html,
which carries three separate sub-calculators; all three are covered as tabs.

**Parity (§3a-PRIME).** Input fields 18/18, result fields 17/17. Their page was read
BOTH as source and as rendered output, per the standing note — the source gave the input
set, and re-fetching the form with each `cpayoffoption` value (`together` / `extra` /
`original`) and each `cpayinterest` value gave the result set, which differs per mode and
does not appear in a single fetch. Two rows (Balance After Graduation, Balance After Grace
Period) are correctly dropped when interest is paid during school; we match that.

**Formula verification.** 40 Node assertions before any code was embedded, all passing
against their published figures:
- Payment mode: 30,000 / 10y / 6.8% -> $345.24, interest $11,428.92, total $41,428.92
- Term mode: 30,000 / $400 -> 8y 2m, total $39,173.06
- Balance mode: $345.24 / 10y -> $29,999.91 ; Rate mode -> 6.80%
- Payoff: 30,000 / $350 + $150/mo -> 6y 2m, total $36,767.26, saves $4,421.28
- Projection: 2y / $10k / $20k / 10y / 6mo -> $526.96, grad $44,263.99, grace $45,790.44
- Projection with interest paid in school -> $460.32, interest $15,238.56

Three conventions had to be reverse-engineered rather than assumed:
1. Their *Simple* tool totals the term-solve using the **fractional** period count
   (M x n, giving 39,173.06) while displaying the ceiling in years and months. A
   carry-forward loop gives 39,173.13 and does not match.
2. Their *Repayment* tool uses month-by-month simulation for the original schedule too
   (41,188.54), not the closed form (41,188.33). The two tools genuinely disagree with
   each other by 21 cents; each is matched to its own tool rather than unified.
3. Their *Projection* tool drips **annual borrowing in twelfths each month** during study
   (`b = b*(1+r) + annual/12`). Lump-sum-at-start-of-year is out by $795 and
   lump-sum-at-end by $658 on the default case.

An own bug was caught by internal cross-check: feeding tab 1's exactly-solved payment into
tab 2's simulator returned 145 months instead of 144, because a sub-cent floating-point
residue after the final period kept `bal > 0` true and billed a phantom month. Fixed with a
half-cent epsilon on both the loop test and the final-payment test.

**Deliberate differences.** All numeric defaults differ from theirs (27,500 / 12y / 6.52% /
$310 / $125 extra / 3y / $9,500 / $14,000). Two do not, flagged rather than faked: the
**6-month grace period**, which is the statutory federal figure and would be wrong at any
other value, and the **No** default on paying interest during school, which is correct for
unsubsidized loans and is a binary with no neutral third option.

**Keyword research (§4).** Head term "student loan calculator" is dominated by
studentaid.gov, Bankrate, NerdWallet, Ramsey and the reference site. Long-tail clusters with
dedicated competitor pages, therefore real: "student loan payoff calculator" (Ramsey,
Purefy, savingforcollege, studentloanplanner), "extra payment calculator", "repayment
calculator", "interest calculator" — tab 2 targets these directly. The high-value gap is
recency: OBBBA took effect July 1, 2026, and the reference article still describes
PAYE/REPAYE/ICR/SAVE as live options. Our article covers RAP, the tiered Standard plan, the
Grad PLUS removal and the new caps, plus confirmed 2026-27 rates (6.52% / 8.07% / 9.07%,
from the May 12, 2026 ten-year auction at 4.468% high yield) and origination fees
(1.057% / 4.228%). Title: "Student Loan Calculator — See When You'll Be Debt-Free" (54).

**Additions beyond the reference** (none of these exist on their page): year-by-year
amortization table with a stacked interest/principal chart, a two-line balance comparison
for the payoff tab, an in-school balance-growth table and chart, and per-tab PDF export.

**Checks.** 3 JSON-LD blocks valid; FAQ schema generated from the same Python strings as the
visible HTML, so the em-dash/quote drift the guide warns about is structurally impossible
rather than hand-checked, and the diff asserts byte-equality anyway; 7 inline scripts pass
`node --check`; protected shared style block byte-identical to simple-interest-calculator;
`apply_cb_ux.py` applied after the build (build overwrites it, so the order matters);
jsPDF confirmed lazy — zero bytes on load, fetched on first click only. 99 Playwright
assertions pass at 1280/430/390px: zero console errors, zero horizontal overflow, all three
tabs computing, both radio groups switching, mobile grid resolving to a single track with
every child at full width. Article 2,704 words, 9 H2s plus FAQ, 8 FAQs.

**Originality.** 8-word overlap with the reference article: **0.000%**. Highest overlap with
any of our own 87 articles: 1.79% (simple-interest-calculator), of which all but two runs are
the standard byline and disclaimer blocks. The two genuine prose repeats found — a daily
simple-interest explanation and a "paying a few days early" phrasing — were reworded before
shipping rather than left.

**Two harness bugs worth remembering, both of which produced false failures:**
1. `node --check` was being fed the JSON-LD blocks, because the filter matched on script
   *content* for the string "application/ld+json" — which appears in the tag's `type`
   attribute, never in the body. Filter on the tag, not the body.
2. The "auto-calculate must not move the page" check failed at 430px and 390px with ~50px
   drift, and passed at 1280px. It was `page.fill()` scrolling the element into view before
   typing — Playwright's own scroll, not the page's. Clicking the field first, so the
   scroll-into-view happens before the baseline is taken, gives 0px drift at all three
   widths. This is the same trap the guide already flags for `scrollIntoView`; `fill()`
   does it too.

**Housekeeping.** New OG image; sitemap lastmod refreshed; stale RSC payload removed
(`index.txt` + six `__next*.txt`). Already listed in `calculators-index.json` and
`/all-calculators/`. Inbound links currently 4 (sitemap, all-calculators,
repayment-calculator, college-cost-calculator) — leaving the sidebar sweep to the deferred
internal-linking pass rather than touching many files here.

**Security.** A GitHub PAT was pasted in plaintext in the first message again — the ninth
time this is being recorded. The previous note already downgraded this from a reminder to a
standing unresolved risk, and nothing has changed. Treat the token as burned. The durable
fix remains unimplemented: the owner needs to store the token outside the conversation and
let the CLI read it from the local environment.

### Follow-up, same day: result cards show results, not the visitor's own input

Owner feedback on the live page: the result card was leading with Loan balance,
Remaining term and Interest rate — three values the visitor had just typed into the
form sitting immediately to its left. That pushed the actual answers below the fold of
the card for no gain. Changed across the tool:

- **Tab 1** now lists only derived figures: total interest, total of all payments,
  interest per dollar borrowed, and interest as a share of the total. The solved value
  stays in the green headline; the inputs stay in the form where they were entered.
- **Tab 3** dropped `Monthly payment` from its rows, which was a verbatim repeat of its
  own headline.
- **The donut moved to its own card** below the result card, with a subline reading
  "$X repaid on $Y borrowed", per the owner's request to make it a separate chart.

While doing this a real defect surfaced in tab 3: in "Yes, I pay interest while studying"
mode the card printed `Interest paid while studying: $0.00`, which is simply false — that
is the one mode where the borrower *is* paying it. The in-school and grace-period interest
is now accumulated properly in the loop and reported, along with a new
"Everything paid, in-school interest included" total. Cross-checked independently in Node:
$6,833.77 against the page's $6,833.78 on the default figures (one cent of float ordering).
The comparison this unlocks is the point of the toggle — $68,215.66 all-in if the interest
is paid during study against $72,213.23 if it capitalises.

Parity is unaffected: no field was removed, and every reference figure still matches. The
removed rows echoed inputs rather than reporting outputs, so the reference site's own result
set is still fully covered. Browser suite grown to 114 assertions across 1280/430/390px,
including explicit checks that neither tab echoes its own inputs and that the $0.00 bug
cannot return.

## Take-Home Paycheck Calculator — audit complete, build NOT started (Aug 6, 2026)

Owner asked for `/take-home-paycheck-calculator/` against
calculator.net/take-home-pay-calculator.html. Step 1 and Step 2 of the parity protocol are
done and the reference site's tax model has been fully reverse-engineered. **No page code
was written and nothing was shipped** — recording the findings here so the next session
does not have to redo an hour of probing. The current page is still the 43KB stub.

### Field map (21 inputs, all confirmed from the live form)

| calculator.net | type / default |
|---|---|
| `cannualincome` Your job income (salary) | $/year, 80000 |
| `cpayfrequency` | select: Daily, Weekly, Bi-weekly, Semi-monthly, Monthly, Quarterly, Semi-Annually, Annually |
| `cfilestatus` | select: Single, MarriedJoint, MarriedSeparately, HeadofHousehold |
| `cchildren` Children under 17 | 0 |
| `cotherdep` Other dependents | 0 |
| `cnonjobincome` Other income (not from jobs) | $/year, 0 |
| `chelddeduction` Pretax deductions withheld | $/year, 6000 |
| `cnothelddeduction` Deductions not withheld | $/year, 0 |
| `citemdeduction` Itemized deductions | $/year, 0 |
| `chasotherjobincome` Has 2nd/3rd job or spouse income | radio yes/no, no |
| `cjobincome2`, `cjobincome3` | $/year, 0 (shown only when the radio is yes) |
| `cstatetax` State income tax rate | %, 0 |
| `ccitytax` City income tax rate | %, 0 |
| `cage65` Are you 65 or older | radio yes/no, no |
| `cspouse65` Is your spouse 65 or older | radio yes/no, no |
| `ctips` Qualified tips income | $/year, 0 |
| `covertime` Qualified overtime compensation | $/year, 0 |
| `cloaninterest` Qualified passenger vehicle loan interest | $/year, 0 |
| `cgifts` Cash gifts to charities | $/year, 0 |
| `cselfemployed` Self-employed or independent contractor | radio yes/no, no |

**Result fields (8 rows + two W-4 blocks):** Gross Pay, Federal Income Tax, Social Security
Tax, Medicare Tax, State Income Tax, City Income Tax, Deductions withheld, Final Pay Check;
then "Step 3: Claim Dependents" (qualifying children, other dependents, total) and
"Step 4: Other Adjustments" (a other income, b deductions, c extra withholding per period).

### Their model, reverse-engineered and confirmed to the cent

Derived by probing ~40 parameter combinations against the live page. Every rule below
reproduces their output exactly unless noted.

1. **Gross per period** = annual income / periods (Daily uses 260, weekly 52, bi-weekly 26,
   semi-monthly 24, monthly 12, quarterly 4, semi-annual 2, annual 1). Their footnote says
   "based on 52 weeks per year".
2. **Social Security** = 6.2% of income up to a **$184,500** wage base (12.4% if
   self-employed). Confirmed: 200k single -> $11,439.00.
3. **Medicare** = 1.45% of all income (2.9% self-employed), plus the 0.9% additional
   Medicare surtax above a threshold.
4. **Federal taxable income** = job income + non-job income + 2nd/3rd job income
   − FICA actually paid − pretax deductions withheld − deductions not withheld
   − max(standard deduction, itemized) − qualified tips − qualified overtime
   − qualified vehicle loan interest − min(charitable gifts, 1000 single / 2000 MFJ)
   − senior deduction. Then 2026 brackets, then credits.
5. **Credits**: $2,200 per child under 17, $500 per other dependent.
6. **Standard deductions 2026**: 16,100 single and MFS, 32,200 MFJ, 24,150 HoH — matches
   IRS Rev. Proc. 2025-32.
7. **Senior deduction**: the OBBBA $6,000 per qualifying person 65+.
8. **Self-employed**: FICA doubles, and an extra deduction equal to half of it is applied.
9. **State and city tax**: a flat percentage of gross job income. No brackets, no state
   standard deduction, no local rules. Simple by design.

### THREE defects in the reference, all confirmed — do not replicate

Per the guide's standing rule (the FHA MIP precedent), match the field but not the error,
implement the correct figure, explain it on the page, and flag it in the step-7 report.

1. **FICA is subtracted from federal taxable income.** This is the big one and it affects
   *every single result on their page*. The employee share of FICA is not deductible for a
   W-2 employee. Worked example, $100,000 single, no other inputs:
   - Correct: taxable 100,000 − 16,100 = 83,900 -> **$13,170** federal tax.
     Independently confirmed against a third-party 2026 bracket calculator, which states
     the same $83,900 / ~$13,170 for exactly this case.
   - calculator.net: taxable 100,000 − 7,650 − 16,100 = 76,250 -> **$11,487.00**.
   - They understate federal income tax by **$1,683, or 12.8%**, and the understatement
     scales with income. On a YMYL paycheck page that is not a rounding difference; it
     tells a visitor their take-home is ~$140/month higher than it will be.
   - The one place this deduction *is* partly legitimate is self-employment, where half the
     SE tax is deductible — and they already apply that separately on top, so the
     self-employed path double-counts.
2. **Senior deduction is a cliff, not a phase-out.** The statute phases the $6,000 out at
   6% of MAGI above $75,000 single / $150,000 MFJ, gone entirely by $175,000. They apply it
   in full at $74,000 and zero at $76,000. Verified: single 74k diff $903.90, single 76k
   diff $0.00.
3. **Additional Medicare threshold is $0 for Married Filing Separately.** Implied
   thresholds from a 300k probe: Single 200,000 (correct), MFJ 250,000 (correct),
   HoH 200,000 (correct), **MFS 0** (should be 125,000). An MFS filer on $80,000 is charged
   $720 of surtax they do not owe.

Also worth deciding at build time: they ignore the pre-OBBBA additional standard deduction
for age 65 ($2,050 single/HoH, $1,650 per spouse MFJ), which is separate from and stacks
with the new $6,000 senior deduction. Whether to add it is a judgement call, but it should
be a deliberate one.

### Build notes for next session

- Three defects above mean our numbers will diverge from the reference on purpose. The
  step-7 report must list all three under "Intentional differences", and the article needs a
  short section explaining why our federal figure is higher than some other calculators'.
- Because the numbers will differ, the usual "matches the reference to the cent" evidence
  does not apply here. Verify instead against the IRS bracket tables directly, and
  cross-check two or three whole scenarios against an independent 2026 calculator.
- This is the most YMYL page on the site so far. Budget time for the tax-table article
  (2026 brackets for all four statuses, FICA rates and caps, the OBBBA deductions) rather
  than treating it as a normal calculator build.
- Suggested tabs, given the field count: a main Paycheck tab, and a Self-employed tab, so
  the 21 fields are not stacked into one form card.

### Built, Aug 6, 2026 — and it deliberately does NOT match the reference

Owner instruction: fix what is wrong and build it correctly. Done. This is the first page
on the site where matching the reference to the cent would have been the wrong outcome, so
the usual evidence standard is replaced: every figure is checked against the published IRS
tables and against independent third-party calculators instead.

**Input fields 21/21, result fields 8/8 plus both W-4 blocks.** No field dropped.

**Where we differ from the reference, on purpose:**
1. **FICA is not deducted from federal taxable income.** Theirs does; the employee share is
   not deductible. On $100,000 single: correct taxable $83,900 -> $13,170, theirs $11,487.
   Independently confirmed — a third-party 2026 bracket calculator states the same
   $83,900 / $13,170 for that case, and the engine test asserts it.
2. **Senior deduction phases out at 6% of income above $75,000 / $150,000** rather than
   falling off a cliff at $75,000. At $80,000 single the correct deduction is $5,700; theirs
   is $0.
3. **Additional Medicare threshold for married filing separately is $125,000,** not $0.
   Theirs charges an MFS filer on $80,000 a $720 surtax they do not owe.
4. **The OBBBA deductions are capped and phased out.** Theirs applies tips, overtime and car
   loan interest with no cap at all. Correct: tips $25,000, overtime $12,500 / $25,000,
   car loan interest $10,000, each with its own phase-out ($100 per $1,000 for tips and
   overtime above $150k/$300k; $200 per $1,000 for car loan above $100k/$200k).
5. **Self-employment tax applies to 92.35% of net earnings,** as the code requires. Theirs
   uses 100% and then also subtracts full FICA at step 1, double-counting the relief.
6. **The additional standard deduction for 65+** ($2,050 single/HoH, $1,650 per spouse) is
   applied and stacks with the new $6,000 senior deduction. Theirs ignores it.

The article carries a callout explaining point 1 in plain language, because a visitor who
cross-checks against another site will otherwise think our number is wrong. That is a
feature: the difference is roughly $140 a month of take-home that does not exist.

**Verification.** 53 Node assertions on the engine covering bracket maths for all four
statuses (anchored on two independently published totals, $13,170 single and $45,196 joint),
FICA caps and all three surtax thresholds, credit and deduction phase-outs, itemizing,
self-employment, all eight pay frequencies, and row-reconciliation. The engine lives in
`part_engine.js` and is **inlined verbatim** by the builder, and the browser suite asserts
the shipped copy is byte-identical to the tested one — so the two cannot drift.
85 Playwright assertions at 1280/430/390px, zero console errors, zero overflow.

**Other checks.** 3 JSON-LD blocks valid; FAQ schema generated from the same strings as the
visible text; 9 inline scripts pass `node --check`; protected style block byte-identical;
`apply_cb_ux.py` applied after the build; jsPDF lazy. Article 2,483 words, 9 H2s, 8 FAQs.
8-word overlap with the reference article: **0.000%**. Highest internal overlap 1.09%
(student-loan-calculator), all of it byline, disclaimer and shared H2 headings.

**Keyword research.** Head term "take home paycheck calculator" is held by ADP, SmartAsset,
PaycheckCity and the reference. The differentiated angle is again currency plus correctness:
the 2026 brackets, the four new OBBBA deductions with their real caps, and the W-4 Step 3/4
output that most paycheck calculators omit. Title: "Take-Home Paycheck Calculator — 2026
After-Tax Pay" (50 chars).

**Validator note.** `validate.py` hard-coded a `tabs` grid area, which this untabbed page
does not have. Fixed by deriving the required area set from the page's own `grid-area:`
declarations instead. Worth folding back into the shared validator.

**Housekeeping.** New OG image; sitemap lastmod refreshed; stale RSC payload removed.
Already in `calculators-index.json` and `/all-calculators/`; 6 inbound links.

### Self-audit pass, Aug 6, 2026 — used both pages as a visitor and fixed what got in the way

Owner asked for a final audit, including actually using the tools and fixing anything
confusing. Five real defects found, all now fixed and covered by tests.

**Student Loan Calculator — a value the visitor typed was silently discarded.**
The worst of the five. Tab 1 solves for whichever of the four boxes is left empty, and the
default leaves Monthly payment blank. So the natural next move — typing "400" into the
payment box to ask "what if I paid $400?" — filled all four boxes, and the code fell back to
`solveFor = 'payment'`, recomputed $275.82 and displayed that. The page looked frozen and
ignored the visitor. Reproduced in Playwright before fixing. All four filled is genuinely
ambiguous, so it now says so and names the box to clear, with a worked suggestion for each
direction. Two assertions added.

**Take-Home Paycheck — four fixes from an edge-case sweep and a read-through:**

1. **A negative paycheck came out as a bare minus number.** Entering pre-tax deductions
   larger than the salary, or a large non-job income against a small salary, produced things
   like -$91,664 with no explanation. There is now an amber strip under the headline that
   names the cause: deductions exceeding salary, or tax on the household exceeding what one
   check can bear (with the note that payroll withholds only what the check covers and the
   rest settles at filing).
2. **Capped and phased-out entries looked broken.** Type $60,000 of tips and only $25,000
   counts; the number simply did not move and there was no way to know why. The strip now
   names which of tips, overtime, car loan interest or charitable gifts was limited.
3. **The spouse-65 question showed for single filers,** where the engine ignores it. Now
   hidden unless the filing status is married.
4. **Nothing explained where the tax came from.** Added a "How the tax was worked out"
   block: which deduction was used and whether it was standard or itemized (this is what
   makes an ignored itemized entry legible), the new-2026 deductions actually applied, the
   dependent credit, and taxable income. Also an impossible state/city rate is now flagged
   against the ~13% real-world maximum, and the FICA rows say "both halves" when
   self-employed rather than implying an employer is paying half.

**Verification after the changes.** Student loan: 40 engine assertions, validation, 116
Playwright assertions. Paycheck: 53 engine assertions, validation, 115 Playwright
assertions. All pass at 1280/430/390px with zero console errors and zero overflow.

**Sitewide regression check.** All 214 pages scanned: `git status` shows only the two files
this session touched, and the protected shared style block is byte-identical on every page
that carries one. Two pre-existing findings for the deferred audit, neither caused here and
neither touched: six pages carry a shared block that differs from the reference
(debt-to-income, debt-payoff, profit-loss, all-calculators, 404, _not-found), and the eight
crypto/trading pages carry no protected block at all, which matches the separate design
system the guide documents for that batch.

### The second card did not explain itself (Aug 6, 2026)

The owner read the finished page and asked what the "Deductions and other income" card was
actually for. That is the signal that matters: if the person who commissioned the page
cannot tell, no visitor will either. The card was a bare list of twelve jargon fields with
one line of instruction ("Leave anything that does not apply at zero") that said what to do
and never why.

Fixed in three places:

1. **The card now states its purpose.** Retitled "Anything else that affects your tax", with
   an intro saying the first card assumes a plain situation and this one is for whatever
   makes your case different &mdash; and that most people can leave all of it at zero.
2. **Each of the four sections carries a one-line note saying which way it moves the
   paycheck** and why. The deductions note calls out the counter-intuitive case explicitly:
   pre-tax deductions push take-home *down* because the money goes to your 401(k) or HSA
   rather than your bank. Two sub-labels were also expanded ("claimed on your return, not
   through payroll"; the $1,000/$2,000 charity limit).
3. **A new article section, "What the second card is for, and when to touch it"**, with a
   table giving the annual effect of every field against the page defaults, so the
   abstraction is grounded in dollars. It also explains that doubling a 401(k) costs $4,154
   of take-home but adds $4,800 to the account, leaving you $646 ahead &mdash; the single
   most misread line on any paycheck calculator.

**Every figure in that table is generated from the shipped engine and asserted**, not typed
from memory: thirteen claims checked against `THP.compute` on the page defaults, all within
a dollar. Writing worked examples into a YMYL article by hand is exactly how a wrong number
gets published, so this check should be repeated whenever the article quotes an output.

Article now 2,854 words and 10 H2s plus FAQ. 115 Playwright assertions still pass.

### Second form card gets its own button pair (Aug 6, 2026)

Owner: a visitor who works down the optional second card reaches the bottom, finds no
Calculate or Clear anywhere near, and reasonably concludes the card does nothing. Correct
reading. Auto-calculate meant it *worked*, but nothing on screen said so, and the visitor
also lost the thing pressing Calculate actually buys on a long form: cb_ux scrolls the
result card into view and flashes it. From the bottom of card two the answer is well off
screen, so that jump is the whole point.

Both form cards now carry the standard Calculate + Clear pair. One `run()` and one
`clearAll()` behind both, so Clear from either card empties the whole form rather than only
its own fields.

`apply_cb_ux.py` needed no change: it collects every button whose text is exactly
"Calculate" as well as any `[id*="-calc"]`, so `pay-calc-2` is tagged automatically. The
browser suite now asserts that **two** buttons carry `data-cb-calc` and that `pay-clear-2`
does **not** — the `-calc` id substring rule would happily grab a badly-named Clear button,
and this page proves it does not here.

Verified rather than assumed: from a scroll position centred on the second card's button,
clicking it lands the result card at 88px from the top of the viewport at all three widths
— under the 70px sticky header rather than behind it. 136 Playwright assertions now pass.

Worth carrying forward: **any page whose form area holds more than one input card needs a
button pair on each of them.** This is the first page on the site with a split form; the
single-card pages are unaffected, and the student loan calculator's form area is one input
card plus a notes card, so it already ends on its buttons.

## DEFERRED — site-wide fixes held back for the final audit pass

**Owner decision, Aug 4, 2026:** finish building/rebuilding the individual calculators
first. Do **not** fix the items below along the way, even when a session touches a file
that has one of these problems. They are collected here so that when the owner asks for a
full-site audit, this list is the starting point and nothing has to be rediscovered.

Assistant memory does not persist between sessions, so this file is the only thing that
carries the decision forward. Read it before proposing any site-wide change.

1. **20 pages still load jsPDF eagerly.** `<script src=...jspdf...>` tags in the markup
   instead of the `loadScriptOnce`/`ensurePdfLibs` lazy pattern the guide requires. About
   403KB fetched by every visitor on every view of those pages for a feature most never
   use. Full list as of Aug 4, 2026: age-calculator, amortization-calculator,
   annuity-calculator, bmi-calculator, bra-size-calculator, compound-interest-calculator,
   currency-calculator, engine-horsepower-calculator, gpa-calculator, horsepower-calculator,
   income-tax-calculator, investment-calculator, loan-calculator, mortgage-calculator,
   resistor-calculator, retirement-calculator, salary-calculator, sales-tax-calculator,
   savings-calculator, tip-calculator. Re-derive the list at audit time with:
   `grep -l 'script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf' */index.html`
   The working lazy implementation to copy is in apr-calculator, payment-calculator or
   pension-calculator.

2. **`check_adsense.py` and `check_originality.py` do not exist.** The guide's AdSense
   section instructs running both before every push, but `scripts/` only holds
   `sync_header_footer.py`. Every page built so far has had those checks done by hand.
   Writing them once would make the standard repeatable and is the natural companion to
   the audit itself. What they need to assert is already specified in the guide's
   "Per page, enforced by check_adsense.py" list.

3. **Thin inbound linking on rebuilt pages.** Freshly rebuilt calculators tend to link out
   well through their sidebar but receive few links back. payment-calculator had 3 inbound
   links at launch (all-calculators, sitemap, business-loan-calculator). At audit time,
   sweep the sibling pages of each rebuilt calculator and add it to their related-calculator
   sidebars — cheap internal equity, but it touches many files so it belongs in its own pass.

4. **Stale Next.js RSC payload files remain in 70 folders.** The 111 folders whose payload
   contradicted their page were cleared on Aug 4; the remaining 70 still match their (as yet
   unrebuilt) pages, so there was no defect to fix. Each one becomes stale the moment that
   page is rebuilt — delete that folder's `index.txt` and `__next*.txt` as part of the rebuild,
   as was done for payment-calculator and pension-calculator.

5. **Site-level AdSense items already listed at the end of DESIGN_AND_SEO_GUIDE.md** —
   `/contact` being only 225 words, the unsupported "Reviewed for accuracy" byline claim,
   `/about` describing ads that do not run yet, ~110 pages under 300 words, and the missing
   `ads.txt`. These belong to the same final pass; do not treat them as separate discoveries.

## Standing notes for next session

- **`llms.txt` is generally stale**, found in passing while fixing the crypto-
  profit-calculator link (Jul 27, 2026): it still contains old `/money-markets/`
  -prefixed URLs for several Crypto & Trading calculators (e.g. a duplicate
  "Crypto Profit / Loss Calculator" line still pointed at
  `/money-markets/crypto-profit-loss-calculator/`), left over from before that
  section's URL restructure. Only fixed the one entry directly relevant to
  today's task; a full pass to re-generate/clean up `llms.txt` against the
  current live URL set is still outstanding and worth doing as its own
  focused task rather than folding it into an unrelated change.
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
  rather than repeating this note a fourth time. **Update, Aug 3, 2026 session
  (Mutual Fund Calculator build)**: it happened a seventh time — a PAT was pasted
  in the first message again. Treat it as burned. Flagged to the owner at the top
  of the session before any other work; the durable fix (token stored outside the
  chat, read from local environment) is still not in place. **Update, Jul 27, 2026
  session**: it happened again (a fourth time) — a PAT was pasted directly
  in chat at the very start of this session too. Treat that token as burned
  and rotate it before the next session. **Update, separate Jul 27, 2026
  session (Credit Card Payoff Calculator rebuild)**: it happened again (a
  fifth time) — a new PAT was pasted directly in the first message of this
  session too. Treat that token as burned and rotate it before the next
  session. **Update, Jul 31, 2026 session (Debt Consolidation Calculator
  rebuild)**: happened a sixth time, and this time it was worse — the user
  explicitly asked to reuse the same already-flagged-as-burned token from a
  prior session's transcript rather than even generating a new one, and it
  was still valid/functional — meaning it was never actually rotated
  despite five prior notes saying to. Flagged again at the very start of
  this session before doing any other work. Six notes in without the
  underlying rotation happening; if a durable fix (the user storing the
  token outside the chat and Claude Code/CLI reading it from local
  environment instead) isn't in place before the next session, treat this
  as a standing unresolved risk rather than a one-off reminder.
  **Update, Aug 3, 2026 session (Mortgage Payoff Calculator rebuild)**: a
  seventh token was pasted in the first message. Flagged at the start of the
  session before any other work, as with the previous six. The condition the
  previous note set has now been met — six notes passed without the rotation
  happening — so this is recorded as a **standing unresolved risk**, not a
  reminder. An eighth note will add nothing; the durable fix (owner stores the
  token outside the conversation, CLI reads it from the local environment)
  needs to happen before the next session.

## VA Mortgage Calculator — rebuilt from stub (Aug 7, 2026)

Replaced a 46KB template stub at `/va-mortgage-calculator/` with a full 3-card build
(117KB). Reference page: calculator.net/va-mortgage-calculator.html, supplied by the owner
with a full-page screenshot alongside the URL.

**Parity (§3a-PRIME).** Input fields 37/37, result fields 30/30 — both re-verified by a
script that greps the *built file* rather than the plan (`parity.py` in the session
scratch), per step 6. Their page was read both as source and as rendered output: the
source gave the 30 form controls, but the result set only appears after submitting the
form, and it **changes shape depending on `caddoptional`** — with optional costs off they
show principal and interest alone, with them on they show the full Monthly/Total cost
table. A single fetch of the default page would have missed the entire cost table, the
biweekly box and the payoff date. We always render the full version.

**Funding fee logic was derived empirically, not from memory.** Eighteen probe requests
with varied `cdownpayment` / `vaeligibility` / `valoanbefore` / `disabled` values
reconstructed their table:

| Down payment | First use | Repeat use |
|---|---|---|
| under 5% | 2.15% | 3.30% |
| 5% to 9.99% | 1.50% | 1.50% |
| 10% or more | 1.25% | 1.25% |

Cross-checked against current published VA rules (military.com, Veterans United,
valoannetwork, VA Circular 26-22-13 as cited by several of them) — the table matches 2026
law exactly, including the 0.50% IRRRL rate and cash-out using the zero-down purchase
rates, both of which are now in a bottomgrid card even though their form has no field for
them.

Two findings worth recording:
1. **The fee is charged on the base loan amount, not the home price, and their page gets
   this right.** Probing with 3% down ($12,000 on $400,000) returns $8,342, which is
   2.15% of $388,000, not of $400,000. This is *not* the same defect as the FHA page's
   upfront-MIP handling noted in the guide — do not assume the FHA finding generalises to
   other pages on their site. No deviation was needed here.
2. **The Reservist/National Guard radio produces results identical to Active/Veteran.**
   That is correct, not a bug: rates were equalised across service categories by the Blue
   Water Navy Vietnam Veterans Act. The field is kept for parity and because it still
   matters for entitlement, and the page says so in a note rather than leaving a control
   that visibly does nothing.

**Formula verification.** A standalone Node engine was written and asserted against their
published output before a line of it went into the page. Seven scenarios, all exact:
- 400k / 0 down / 6.5% / 30y -> P&I $2,582.63, total $929,746.78, interest $521,146.78,
  out-of-pocket $3,607.63 / $1,298,746.78, payoff Aug 2056
- Their own default (500k / 6.706%) -> $3,297.79, $1,187,204.50, $676,454.50
- 10% down -> 1.25%, $4,500 fee, $364,500 loan ; repeat use -> 3.3%, $13,200 ;
  surviving spouse and 10%+ disability -> 0%
- 3% annual property-tax increase -> $228,362.00 total (compounds once a year, not monthly)
- HOA $300/yr + $200/mo extra -> 24y 6m, mortgage total $758,671.29, extra total
  $58,600.00, out-of-pocket $3,832.63 / $1,125,971.29

Three conventions had to be reverse-engineered:
1. **Biweekly.** Four candidate conventions were tested against their $401,129.25 /
   24.04-years figures. The one that matches exactly: the biweekly payment is the rounded
   monthly payment **truncated** to two decimals (1291.315 -> 1291.31, not 1291.32), the
   rate is annual/26, the final period is left fractional, and the payoff is reported as
   `n x 14 / 365.25` years. Rounding instead of truncating is out by $4.42; reporting
   `n / 26` gives 24.12 years instead of 24.04.
2. **The final instalment carries no extra payment.** With $200/mo extra their extra-payment
   total is exactly 293 x $200 while the mortgage total covers 293 full payments plus a
   $1,960.70 stub — so the last month is whatever clears the balance, and the extra is
   dropped that month.
3. **The payoff date is the month *after* the last payment.** Starting Aug 2026 with 360
   payments, payment 360 falls in Jul 2056 and they report Aug 2056.

**Keyword research (§4).** US competitors converge on "VA **loan** calculator", not
calculator.net's "VA mortgage calculator" — Bankrate, Zillow, Veterans United, U.S. Bank
and VAMortgageCenter all use it. Per §8 the term was blended into the title and meta rather
than renaming the H1 or slug. A second cluster with its own dedicated competitor pages,
"VA funding fee calculator" / "VA funding fee chart 2026", is the higher-volume /
lower-competition middle ground and is targeted through the title, an H2 and a bottomgrid
rate table. Title: "VA Loan Calculator — Payment With Funding Fee Included" (54 chars);
description 148.

**Content.** 2,236-word article, 9 H2s, 8 FAQs, byline, TOC, disclaimer, visible breadcrumb,
a "what this calculator does not cover" section (closing costs, points, ARMs, entitlement
limits, residual-income underwriting). Every worked figure in the prose is computed from the
page's own defaults ($425,000 / 6.45%) and verified in Node, so no example is borrowed.
Originality: 0.11% 8-gram overlap with their page (3 grams, all unavoidable — the VA
department's name and two field-label sequences), and **0.00% article-prose overlap with any
of our own pages** after one fix, below.

**Design.** 3-card grid with a `schedule` area (`amortization-calculator` was the structural
donor). Navy bar with lazy PDF, form / result / navy sidebar, full-width schedule card with
Annual and Monthly tabs plus a Balance / Principal-paid / Interest-paid line chart, and a
bottomgrid pair (live-highlighted funding-fee tier table + exemption list). Taxes, insurance,
HOA and other costs sit on the form directly rather than behind their "More Options" link;
cost escalation and extra payments are behind one toggle.

**Verification.** 75 Playwright assertions at 1280 / 430 / 390px: zero console errors, zero
horizontal overflow, mobile grid resolves to a single track with every child at least 90% of
grid width, h1 computed weight 700, jsPDF fetches zero bytes until the button is clicked and
the download then succeeds, schedule tabs produce 30 annual and 360 monthly rows, and the
schedule matches theirs row-for-row (monthly #1 `8/2026 $2,213 $369 $408,231`; annual #1
`8/26-7/27 $26,425 $4,567 $404,033`). Protected shared style block byte-identical (6,425
bytes). Three JSON-LD blocks valid; FAQ schema and visible text asserted equal on all 8
pairs. New OG image generated at `og/va-mortgage-calculator.png`.

### Three process notes from this session

**The FAQ-drift failure mode was designed out rather than checked for.** The guide records
this breaking on four consecutive rebuilds. Instead of writing the schema and the visible
HTML separately and diffing them, both are generated from one Python list in the build
script, so an em dash or curly quote cannot appear in one and not the other. The diff check
still runs, but it now confirms a property the build guarantees.

**Rebuilding from the working file silently inflated the page by 23KB.** The build script
originally lifted the shared chrome (gtag head, protected block, header, footer, trailing
site scripts) out of the page it was about to overwrite. After `apply_cb_ux.py` had run once,
a rebuild folded the injected block back in and the file grew from 106KB to 139KB with no
duplicated content visible to a `count()` check on any of the obvious markers. The fix is a
one-line rule now written into the script: **shared chrome always comes from the pristine
committed copy (`git show HEAD:...`), never from the working file.** Worth applying to any
future page builder that follows this pattern.

**`apply_cb_ux.py` owns the status-bar sentence and will delete markup it does not expect.**
The bar was written as `<span class="va-bar-text"><span class="badge">$</span><span
id="va-barText">...</span></span>`. The injector keeps the badge and removes every following
sibling, so the `#va-barText` span was destroyed at runtime while remaining present in the
source — a DOM grep on the file would have passed. Match the reference markup exactly:
badge span, then a bare text node.

**One prose collision was caught and fixed.** The opening line of the "what this doesn't
cover" section, "Being clear about the edges matters more than…", already existed in
`refinance-calculator` and `marriage-tax-calculator`. Whole-page 8-gram comparison hid it
inside 83 shared-chrome matches; an article-only comparison surfaced it. **The internal
originality check should run on the article region alone** — header, footer, nav and the
shared disclaimer will always match and drown out the one line that actually matters.



## VAT Calculator — rebuilt from stub (Aug 7, 2026)

Replaced a 43KB template stub at `/vat-calculator/` with a full 3-card build (104KB).
Reference page: calculator.net/vat-calculator.html, supplied by the owner with a
screenshot.

**Parity (§3a-PRIME).** Input fields 6/6, result fields 11/11, and — the part that
matters on this tool — **all 6 of the two-of-four solve combinations**. Their calculator
takes any two of {rate, net price, gross price, tax amount} and derives the other two.
The result set does not appear in the fetched page at all, so each combination was
obtained by submitting the form: rate+net, rate+gross, rate+tax, net+gross, net+tax and
gross+tax were probed individually, along with the rounding and error behaviour.

Behaviour reverse-engineered from those probes and matched exactly:
- Two-decimal rounding, so 17.5% on 99.99 gives 117.49 gross and 17.50 VAT, and 20% off a
  gross 100 gives 83.33 net and 16.67 VAT (which still add back to 100).
- `gross + tax` derives the rate from the implied net, so 100 gross with 20 tax is 25%,
  not 20%.
- A tax amount larger than the gross price is rejected rather than returned as a negative
  net.
- When more than two boxes are filled their tool takes the first two in field order. Ours
  cannot reach that state (see below), so the two-field behaviour — which is all six
  combinations — is identical.

**Formula verification.** A standalone Node engine was asserted against their published
output before anything was embedded: all 6 combinations plus 10 rounding and edge cases,
16 assertions, all exact.

**Keyword research (§4) — and a deliberate departure from USA-first.** §8 names the VAT
calculator as an example of an explicitly region-specific tool, and the SERP confirms it:
the US has no VAT, and every page ranking for "VAT calculator" is UK-focused
(vatcalculator.co.uk, calculatethevat.co.uk, contractoruk, vatcalcu.uk, online-vat-calculator).
Three things are near-universal among them and absent from calculator.net:

1. The framing is **Add VAT / Remove VAT**, not "provide any two values".
2. £ and a 20% default, with 5% and 0% one click away.
3. A "reverse VAT calculator" cluster with its own dedicated pages, and a recurring
   "don't subtract 20%" common-mistake angle.

So the page defaults to £ at 20% and leads with Add/Remove tabs, while a third
**Any two values** tab carries the full reference capability. Title:
"VAT Calculator — Add or Remove VAT at 20%, 5% or Any Rate" (57 chars); description 147.

**Beyond parity.** Country presets for 34 jurisdictions that set the rate and switch the
currency, an 18-currency selector, rate chips per country, a live VAT-fraction hint (at
20% the VAT in a gross price is exactly one sixth of it), a rates-by-country reference
table that highlights every country using the current rate, and a formulas card. Rates
were cross-checked across several 2026 sources; only well-corroborated ones are listed,
and the card says plainly that rates move with national budgets. Where sources conflicted
(Luxembourg 16 vs 17 in a single internally inconsistent page) the corroborated figure was
used.

**Content.** 2,463-word article, 9 H2s, 8 FAQs, byline, TOC, visible breadcrumb, a "what
this calculator does not cover" section (rate classification, place-of-supply, flat-rate
and margin schemes, reverse charge, partial exemption) and a disclaimer. Every worked
figure is computed and verified rather than borrowed. Originality: **0.00% 8-gram overlap
with calculator.net**; the only internal overlap is the standing byline, the disclaimer
opener and one shared H2 heading — no duplicated body prose.

**Verification.** 82 Playwright assertions at 1280 / 430 / 390px: zero console errors,
zero horizontal overflow on all three tabs, single-track mobile grid with every child at
least 90% width, h1 weight 700, jsPDF fetching nothing until clicked, all six solve
combinations correct through the UI, country preset and chip behaviour, error states, and
tab isolation. Protected shared style block byte-identical. Three JSON-LD blocks valid,
FAQ schema equal to the visible text on all 8 pairs. New OG image.

### The bug the screenshot caught, and why it was structural

In the free-form tab the calculator writes its answers back into the boxes the visitor
left empty, tinting them so it is clear which figures were typed and which were worked
out. A screenshot review showed the derived **rate** rendering untinted.

The cause was not styling. `render()` decided which two fields were "given" by looking at
which boxes were non-empty — so on the second render it read its own output back as user
input. The values happened to stay correct because the relationship is self-consistent
(net 1200 + gross 1440 implies rate 20, and rate 20 + net 1200 implies gross 1440), which
is exactly why it was invisible to every numeric assertion. What it broke was the editing
model: once nothing was marked derived, typing a new figure no longer released the stale
ones, and the solver could end up reading a pair the visitor never chose.

The fix is to track ownership explicitly — an `owned` list of the two fields the visitor
has typed into, most recent last. Typing in a third box releases and clears the oldest;
emptying a box hands it back so it becomes something to solve for again. `render()` now
reads only the owned fields and never re-infers from the DOM. A side effect is that our
version can never hold more than two user-supplied values, so the reference tool's
"first two in field order" tie-break is unreachable rather than unmatched.

Two regression assertions were added for it: that `net + gross` leaves rate and tax marked
derived, and that the marking survives a second render.

**Process note — `scrollIntoView` is muted, so it cannot position a screenshot harness.**
The guide already says this about measuring scroll behaviour; it applies to taking
screenshots too. A capture script that scrolled to the bottom grid with `scrollIntoView`
silently produced a screenshot of the top of the page, because the shared cb_ux snippet
mutes that method around an auto-run. Use `mouse.wheel` after letting the ~700ms mute
expire.


### VA Mortgage Calculator — Clear looked dead on a tall form (Aug 7, 2026)

Owner report: Calculate works, Clear does not. Clear was in fact resetting every field
and re-rendering correctly on both local and live — the defect was that **nothing it
changed was on screen**. This page's form is the tallest of the 3-card builds (loan
basics, entitlement, costs, advanced toggle), so the button row sits far below the fields
it resets. Measured from the position a visitor actually clicks from: on a 390px phone
none of `#va-price`, `#va-rate`, `#va-down` or the result card are in the viewport, and on
desktop only the rate field is. Calculate feels responsive purely because the shared cb_ux
snippet scrolls and flashes the result for it; Clear had no such confirmation.

Checked the other 3-card pages the owner was comparing against — amortization,
mortgage-payoff and the new vat-calculator all keep their first field visible from the
button, which is why their Clear reads as working. This page is the outlier, so the fix is
page-level rather than a change to the shared snippet.

Clear now confirms itself the same way Calculate does: scroll the top of the form back
into view, then flash the result card.

**The part worth remembering.** The first attempt used `window.scrollTo` and silently did
nothing. cb_ux installs a capture-phase click listener on the whole grid that arms a
700ms scroll mute for any click that is not `[data-cb-calc]` or `.cb-jump` — Clear is
neither, so it muted its own scroll. Instrumenting the call showed `scrollTo` being invoked
with the correct target and the page not moving, which is what pointed at the wrapper
rather than at the maths. The mute exists to stop auto-calculate from yanking the page
while someone types, and a real press of Calculate is explicitly exempted from it via
`releaseScroll()`; a real press of Clear deserves the same exemption. Since `releaseScroll`
is not exposed, the scroll is driven through `scrollingElement.scrollTop` with a small
rAF easing loop, which the snippet does not wrap.

Regression assertions added at all three widths: Clear resets the form, Clear brings the
reset fields back on screen, Clear flashes the result card, and — because this deliberately
bypasses the mute — typing still does not move the page (measured as drift of the touched
control, 0px at every width). Suite now 87 assertions.


### VAT Calculator — built UK-first, corrected to USD-first (Aug 7, 2026)

The owner rejected the build within hours: it defaulted to GBP, preselected the United
Kingdom country preset, and used pound examples throughout the article. Corrected the same
day to USD-first.

**What happened.** §8 of the guide read "default to USD / US units / US conventions unless
the tool is explicitly region-specific (e.g. a UK-mortgage or **VAT calculator**)" — VAT
calculator was named in the guide as an example of a region-specific tool. Competitive
research agreed: every page ranking for "VAT calculator" is a .co.uk site in GBP at 20%.
So the page shipped UK-first.

**Why that was still wrong.** The guide line was ambiguous and the research was about
ranking pages, not about this site's audience. ~70% of traffic here is American. A US
visitor reaches a VAT page because they sell into VAT countries, buy from them, or travel
— none of which is served by a GBP default. And a UK-mortgage calculator is genuinely
about one country's system; VAT is a concept that exists in 170 countries. The two are not
the same kind of exception.

**The actual mistake is a process one, not a research one.** Parity was fine — 6/6 inputs,
6/6 solve combinations, 11/11 result fields, all verified. What went wrong is that a
decision about the site's primary market was made *inside a build*, on the strength of one
ambiguous line, without asking. A US-first default is the kind of thing to raise before
building, not to quietly reverse.

**What changed.** Currency list reordered with USD first and defaulted to `$`; no country
preselected (the dropdown opens on "Custom rate…"); rate note, form hints and Clear reset
all follow. The article was rewritten rather than find-and-replaced: every example is now
in dollars, and two new sections lead the page — "VAT and US sales tax are not the same
tax" and "When a US business has to deal with VAT" (digital services, shipping abroad,
overseas suppliers, travel refunds). Two FAQs were replaced with the two a US reader
actually asks first. Picking a country still switches the currency with it, so the
international use case is unharmed. Title and description no longer name the UK.

Zero pound signs remain in the page body. Article 2,588 words, 9 H2s, 8 FAQs, still 0.00%
8-gram overlap with the reference page. Suite extended to 89 assertions, adding explicit
checks that the page defaults to USD with no country preselected at all three widths.

**Guide corrected.** §8's Defaults bullet no longer cites the VAT calculator as an
exception, states plainly that it is not one, and adds a standing rule: a US-first default
is never deviated from without asking the owner first.


### VAT Calculator — stripped back to the reference layout (Aug 7, 2026)

Second correction the same day, and the more important one. The owner's words: as a user
he was confused by the page, so other users would be too. Everything added on top of the
reference tool came out.

**Removed:** the Add VAT / Remove VAT / Any two values tabs, the 34-country preset
dropdown, the 18-currency selector, the rate chips, and the VAT-fraction hint under the
result. The calculator is now what calculator.net has and nothing more — one card, four
boxes (VAT rate, Net price, Gross price, Tax amount), Calculate and Clear. Fill any two,
get the other two. Clear blanks all four, as theirs does.

**Kept:** the site's own 3-card shell, since that is the established design system and was
never what confused anyone — status bar with PDF export, result card with the donut, navy
related-calculators sidebar, the two bottom reference cards, and the article. Also kept
the shading that marks which boxes the calculator filled in, because without it a
four-box any-two form gives no clue which numbers were yours.

**One deliberate difference from the reference, flagged rather than silent.** Their result
strips trailing zeros, printing $17.5 where the tax is 17.50. Ours prints two decimal
places for money. The arithmetic is identical; only the formatting differs.

**Feature claims in the prose had to be rewritten, not just the markup.** The article
described "the three tabs", told the reader to use "Remove VAT" for a refund estimate,
said the calculator "shows the applicable fraction under each result", and referred to the
"country selector" and "country presets". All four described things that no longer exist.
Leaving them would have been a content-accuracy problem in its own right, and §10 of the
guide is explicit about never claiming a feature the page does not have. The relevant
paragraphs were rewritten to describe the four ways two inputs can be combined, and the
subhead and meta description no longer promise country presets either. Dead CSS for the
removed components was deleted too (1.2KB).

Page went 105KB to 95KB. Suite rewritten to 74 assertions: all six reference combinations
through the UI, rounding parity, error states, the derived-field shading and that it
survives a re-render, the headline naming whichever value was solved for, Clear blanking
all four boxes and the form still working afterwards, and explicit assertions that the
form contains exactly four inputs, zero dropdowns, and none of the removed elements.
Overlap with the reference page is 0.03% — a single 8-gram, which is the four field labels
in order and unavoidable.

**The lesson, stated plainly.** Two corrections in one day on this page, both from adding
judgement the owner had not asked for. The first was a market default; this one was
feature scope. The reference is the specification. Additions beyond it are a proposal to
put to the owner before building, not a decision to make inside a build — the same
conclusion the USD correction reached hours earlier, which should have been enough.


### VA Mortgage Calculator — Clear rewritten to match the reference (Aug 7, 2026, third correction)

The owner's report: pressing Clear redirects to the result card exactly like Calculate does,
so what is Clear even for — it is supposed to empty the value boxes.

Both halves of that are right, and both were my own invention rather than anything the
reference does.

1. **Clear was restoring default values, not clearing.** It put 425000 / 6.45 / 30 back into
   the boxes. Fetching calculator.net's `common.js` settles it: `clearForm()` sets every
   `text`, `number`, `date` and `textarea` element to `''`, leaves selects, radios and
   checkboxes alone, and does not recalculate or scroll.
2. **The earlier "fix" made it worse.** Diagnosing the button as feeling dead, I added a
   scroll-to-form plus a result-card flash — so Clear moved the page like Calculate while
   the boxes still held values nobody typed. That was solving a problem the reference does
   not have, by inventing behaviour instead of copying it.

Clear now blanks all 19 typed boxes, keeps every select, radio and checkbox as the visitor
left them, and does not move the page. The result panel returns to its empty prompt because
this page calculates as you type. The `smoothScrollTo`/`confirmCleared` helpers and the
now-unused `DEF` defaults object were deleted.

A second jump survived the first attempt: `$('va-price').focus()` at the end of the handler
scrolled the off-screen input into view, moving the page 489px on desktop and 812px on
mobile. Removed. **Focusing a field after clearing is the same jump by another route.**

Verified at 1280/430/390px, measuring the drift of the pressed button rather than
`window.scrollY`, since emptying the schedule legitimately shortens the page: every typed
box empty, selects and radios untouched, 0px drift, no flash, empty-state prompt restored,
and the form immediately usable again. Typing still does not move the page. Suite now 97
assertions. Audited the VAT calculator the same way — its Clear already blanks all four
boxes correctly.

**Pattern to stop.** This is the third correction on the same theme in one day: USD default,
feature scope, and now button behaviour. Each time the reference already specified the
answer and I substituted judgement for it. Guide updated with a section stating that button
behaviour is part of parity, with the exact `clearForm()` semantics written out so it does
not have to be rediscovered.


### VA Mortgage Calculator — schedule and chart split into two cards (Aug 7, 2026)

Owner: the schedule table and the chart were sitting inside one card; every other page keeps
them as two separate cards in the same position.

Correct — `mortgage-payoff-calculator` is the house pattern: a `minmax(0,1fr) 400px` grid
holding a schedule card and a chart card as siblings, each with its own header bar and border.
The VA page had them as one `.va-schedule-card` containing a `.va-schedule-body-grid` that
split the interior, which reads as a single card with a divider rather than two cards. The
donor page for this build (`amortization-calculator`) uses the older combined form, which is
how it got copied in.

Rebuilt to match mortgage-payoff: `.va-schedule-grid` wrapping `.va-sched-card` (header with
the year count and the Annual/Monthly toggle, then the scrolling table) and `.va-chart-card`
(header, then the SVG and legend, vertically centred so the chart does not sit at the top of a
tall card). Both stretch to equal height; at 900px they stack full width. Dead CSS for the old
combined layout removed.

Verified at 1280/430/390px: two distinct cards, same row with a 16px gap and equal height on
desktop, single full-width track stacked on mobile with zero horizontal overflow. Three
assertions added, including one that fails if the chart card is ever nested inside the schedule
card again. Suite now 100 assertions.

Worth noting for future builds: when copying structure from a donor page, check the donor is
current for the component being copied. `amortization-calculator` was the right donor for the
grid areas and is the wrong one for the schedule/chart card split.


## Body Fat Calculator — rebuilt from stub (Aug 7, 2026) — first Health & Fitness build

Replaced a 46KB template stub at `/body-fat-calculator/` with a full 3-card build (100KB).
Reference: calculator.net/body-fat-calculator.html.

**Parity (§3a-PRIME).** Input fields 17/17, result fields 7/7, both unit tabs, the
female-only hip row, and the reference's conditional row behaviour.

**The reference's implemented formula does not match its own published formula.** Its
article prints the U.S.-customary Navy equations (86.010 x log10(waist-neck) - 70.041 x
log10(height) + 36.76 for men). Its calculator does not use them. Feeding the US tab
inputs where the two formulas diverge shows it converting to centimetres and applying the
SI equation instead:

| Case (male, 152 lb, 5'10.5", neck 19.5") | USC formula | SI via conversion | calculator.net |
|---|---|---|---|
| waist 32" | 1.7% | **2.4%** | 2.4% |
| waist 48" | 32.4% | **32.5%** | 32.5% |
| female default | 21.8% | **21.5%** | 21.5% |

The default inputs hide this — both formulas give 15.3% there, which is presumably why it
has survived. We match the implementation (SI throughout), so our numbers agree with
theirs everywhere, and our article publishes the SI equations we actually use rather than
a different pair. **Flagged to the owner for a decision** rather than changed unilaterally:
switching the US tab to the USC equation would match the published Navy method and their
article text, at the cost of the two unit tabs disagreeing by up to ~0.7 points for the
same body.

**Formula verification.** 17 Node assertions against the reference's own output before any
code was embedded — all exact on the first run. Covered both sexes, both unit systems,
every category band, the 0% clamp, Jackson & Pollock interpolation, and the age rules.

Conventions reverse-engineered and matched:
- Jackson & Pollock ideal body fat interpolates linearly between five-year steps (age 33 ->
  13.3%) and is **omitted entirely outside ages 20-55** rather than extrapolated.
- The row label flips to "Body fat to **gain** to reach ideal" when below the ideal figure.
- The BMI-method equation switches to the youth version under 18 and the adult version from
  18 (verified at 17 -> 18.4% and 18 -> 13.7%).
- Body fat percentage clamps at 0.0% and the category becomes "Less than Essential Fat".

**Keyword research (§4).** Head term "body fat calculator"; the distinguishing cluster is
"navy body fat calculator" / "body fat calculator with tape measure", which is what the
tool actually is and what competitors title around. Title: "Body Fat Calculator — U.S. Navy
Method With Tape Measure" (56 chars); description 143.

**Health-category conventions applied.** `HealthApplication` schema, Health & Fitness
breadcrumb to `#hea`, `--hea` accent (#0C9268) instead of the finance navy/green, named
sources for every formula, and a YMYL disclaimer that says plainly it is not medical advice
and names low body fat as something to discuss with a doctor rather than chase.

**Content.** 2,387-word article, 9 H2s, 8 FAQs, byline, TOC, breadcrumb, "what this does not
cover" (fat distribution, pregnancy, children, unusual builds, medical conditions). Every
worked figure computed from the page's own defaults. Originality: 2.20% 8-gram overlap with
the reference, all of it unavoidable — 42 grams are formula constants and ACE range numbers,
17 are the form's field-label sequence; **zero prose overlap**. Internal overlap is the
standing byline only.

**Verification.** 83 Playwright assertions at 1280/430/390px: all 9 reference cases exact
through the UI, both unit tabs, hip row visibility by gender, gain/lose wording, ideal-row
omission at 18 and 70, the 0% clamp, category table highlighting, error states, Clear
emptying the boxes with 0px page drift, zero console errors, zero overflow, single-track
mobile grid, jsPDF fetching nothing until clicked.

### A rendering bug the assertions missed

The gauge pointer was inserted with `insertAdjacentHTML` on every render, so it stacked a
new marker on each recalculation — after three keystrokes the scale read
"17.9 18.9 20.7%" on top of itself. Every DOM assertion passed throughout, because
`querySelector('.bf-gauge-ptr')` finds the first of many. It was caught by looking at the
screenshot, which is exactly the failure mode §3a-PRIME warns about. Fixed by giving the
pointer a fixed element that gets repositioned, and a regression assertion now counts the
pointers after repeated recalculation rather than checking one exists.


### Body Fat Calculator — colours brought back to the sitewide scheme (Aug 7, 2026)

Shipped using the health category token `#0C9268` for the result card head, the Calculate
button, the active unit tab, the radios, the highlighted row and the article links, plus a
non-palette gauge ramp (`#3B82F6`, `#EAB308`, `#F97316`, `#DC2626`). The owner sent a
screenshot of the VA page and pointed out that every page on the site uses one scheme.

Corrected to the standard: `#16A34A` result head and Calculate, `#128A3D` hover and links,
`#1E3A5F` bar, active tab and sidebar. The gauge now uses only site-palette colours, mapped
so both extremes read as caution and the middle bands as healthy. OG image regenerated in
the standard green, and the PDF header switched from the health green to navy.

The mistake was reading `--hea` as a page theme when it is a **category-listing** token —
it colour-codes entries on all-calculators, not the page itself. Guide updated with the
exact standard values and that distinction stated explicitly, since this is the first
Health & Fitness build and would otherwise have propagated across the whole section.

83 assertions still pass; computed colours verified against the VA page
(`rgb(22,163,74)` and `rgb(30,58,95)`).


## BMR Calculator — rebuilt from stub (Aug 7, 2026)

Replaced a 46KB template stub at `/bmr-calculator/` with a full 3-card build (93KB).
Reference: calculator.net/bmr-calculator.html.

**Parity (§3a-PRIME).** Input fields 13/13, result fields 7/7 (BMR headline plus six
activity rows), both unit tabs, the collapsible Settings panel with its results-unit,
formula and body-fat controls, and both validation rules.

**Formula verification.** 8 Node assertions against the reference's own output before any
code was embedded, all exact:
- US Mifflin 1,717 with rows 2,060 / 2,361 / 2,515 / 2,661 / 2,962 / 3,262
- Metric Mifflin 1,605 · Revised Harris-Benedict 1,614 · Katch-McArdle at 20% 1,407
- Metric female 1,439 · Metric kJ 6,720 · US kJ 7,189 · US Katch at 30% 1,467

Three conventions reverse-engineered:
1. **Activity rows come from the unrounded BMR**, not the displayed one. 1717 x 1.375
   rounds to 2,362; the reference shows 2,361, which is 1716.998 x 1.375. Multipliers are
   1.2 / 1.375 / 1.465 / 1.55 / 1.725 / 1.9.
2. **Kilojoules use 4.1868**, the International Steam Table calorie, not 4.184 — which
   4.184 would put the metric BMR at 6,715 against their 6,720. Each row is converted from
   its own unrounded calorie value rather than from the rounded kJ headline.
3. **Age is restricted to 15-80 and Katch rejects a 0% body fat**, both with their own
   error rather than a computed result. Our messages say the same thing in our words.

**Keyword research (§4).** Head term "bmr calculator"; the distinguishing long-tail is the
equation names, which is what people search when a tool gave them a different number
("mifflin st jeor calculator", "harris benedict calculator", "katch mcardle"). All three
are selectable and named in the result subhead. Title: "BMR Calculator — Calories You Burn
at Complete Rest" (51 chars); description 150.

**Content.** 2,098-word article, 8 H2s, 8 FAQs, byline, TOC, breadcrumb, a "what this does
not cover" section that puts *a calorie target* first, and a YMYL disclaimer naming
pregnancy, under-18s, medication and disordered-eating history explicitly. The 2005
Johnstone analysis the reference cites is used for the honest accuracy claim (about a
quarter of between-person variation stays unexplained).

**Verification.** 85 Playwright assertions at 1280/430/390px: all 7 reference cases exact
through the UI including both kJ cases, the equation-table highlight, age bounds accepted
at 15 and 80 and rejected at 14 and 81, Katch rejecting 0% while Mifflin ignores the field,
the kJ column header switching, sitewide colours asserted by computed value, Clear emptying
the boxes with 0px drift, zero console errors, zero overflow, single-track mobile grid.

### Three things worth carrying forward

**A test-harness artifact that looked like a page bug.** The Clear drift check failed at
185px. The page was fine: `html{scroll-behavior:smooth}` is set in the shared protected
block, so the scroll that Calculate legitimately performs is *animated*, and the harness
was measuring mid-flight. Added a `settle()` helper that polls `window.scrollY` until it
stops changing rather than using a fixed wait. **Any drift measurement on this site needs
that**, because the smooth-scroll rule is sitewide.

**Hiding a result section on error moves the page.** The first version hid the whole
activity table when inputs were blank, collapsing the result card ~185px and shifting the
document under the visitor. It now keeps the table with em-dash placeholders, which holds
the height steady and also shows what the tool will produce.

**Two genuine copies caught by the originality check, not by eye.** The exercise-level
footnote ("15-30 minutes of elevated heart rate activity") was near-verbatim from the
reference, and "Worked through with the values this page opens on" had been reused from the
body-fat article. Both rewritten; overlap with the reference fell from 2.37% to 1.43%, and
what remains is formula constants and the form's field-label sequence.


### Body Fat and BMR — the missing "Other Units" tab (Aug 7, 2026)

The owner noticed that both pages were missing the third tab the reference carries. He is
right, and the way it went missing is worse than the omission: I recorded it in the Body Fat
completion report as an "intentional difference — it is calculator.net's global unit-converter
widget, not a mode of this calculator" and shipped. Nobody agreed to that. §3a-PRIME says a
deliberate omission is flagged **with a reason**, which means asked before shipping, not
noted afterwards. Then I repeated the same omission on BMR without even flagging it.

**Full re-audit of both pages first**, since the question was "what else is missing":
Body Fat inputs 17/17 and results 7/7; BMR inputs 13/13 and results 7/7. The Other Units tab
was the only gap on either page.

**What was actually there**, read from their scripts rather than assumed from screenshots —
the two pages use *different* converters:
- Body Fat embeds `/converter/converter.php` in an iframe: the generic five-category converter
  (Length, Temperature, Area, Volume, Weight) with unit tables in `/js/conversion.js`.
- BMR uses `/js/quick-conversion.js`: two purpose-built converters, Height (meter, centimeter,
  millimeter, yard, foot, inch, defaulting meter to inch) and Weight (kilogram through carrat,
  defaulting kilogram to pound).

Both now implemented to match, in our own design, as a third tab that shows the converter above
the form so a converted figure can be typed straight in without losing existing entries.
Temperature is handled with its own offset conversions rather than a scale factor. Their pound
factor is `0.453592` rather than the exact `0.45359237`, and matching it is what makes 80 kg
come out at 176.3699536 lb on both sites.

Verified: 180 cm to 70.86614173 in, 6 ft to 72 in, 80 kg to 176.3699536 lb, 100 C to 212 F,
0 C to 273.15 K, 1 m² to 10.76391042 ft², 1.75 m to 68.8976378 in, 12 oz to 340.194 g.
Each suite grew to 97 assertions, adding the tab count, the category list, every conversion
above, blank-input clearing, and that calculator entries survive a trip to the converter tab
and back.

**Guide updated** with the per-page converter definitions so this does not have to be
rediscovered, and with the rule that an omission counts as intentional only once the owner has
agreed to it.


## TDEE Calculator — rebuilt from stub (Aug 7, 2026)

Replaced a 44KB template stub at `/tdee-calculator/` with a full 3-card build (102KB).
Reference: calculator.net/tdee-calculator.html.

**Parity (§3a-PRIME).** Input fields 14/14 including the Other Units tab, result fields
15/15 (TDEE headline, BMI line with category and healthy range, three weight-loss rows and
three weight-gain rows each with a percentage of maintenance).

**Formula verification.** 6 Node assertions against the reference's own output before any
code was embedded, all exact: US moderate 2,549 with BMI 23.7; metric 2,425 with BMI 20.1;
metric female 2,181; Katch at 20% 2,188; metric kJ 10,153; and an obese case at 2,937 with
BMI 30.9 that keeps all three loss rows.

Conventions reverse-engineered:
1. **Step sizes are per unit system.** US shows 0.5 / 1 / 2 lb per week, metric 0.25 / 0.5 /
   1 kg per week, and both map to 250 / 500 / 1000 Calories a day. A pound a week and half a
   kilo a week are both treated as 500.
2. **kJ converts the *rounded* Calorie value here** — and the BMR page converts the
   unrounded one. Their own two pages disagree by a unit or two, so each is matched to its
   own page rather than unified. Getting this wrong put the headline at 10,151 against their
   10,153.
3. **Any loss row that would fall below 1,500 Calories is withheld** and replaced with a
   note, and **below a healthy BMI the entire weight-loss section disappears**.
4. **Choosing "Basal Metabolic Rate" as the activity level** returns BMR alone, with no BMI
   line and no intake tables.
5. Age range is 18-80 here, not the BMR page's 15-80.

**Keyword research (§4).** Head term "tdee calculator"; the intent behind it is nearly always
a calorie target, so the title leads with the outcome ("Daily Calories to Maintain, Lose or
Gain") rather than the acronym's expansion. Title 58 chars, description 147.

**Content.** 1,930-word article, 7 H2s, 8 FAQs, and a limitations section that puts "what to
eat" and "anyone with a difficult history around food" in it explicitly.

**Verification.** 102 Playwright assertions at 1280/430/390px: all reference cases exact
through the UI, the BMR-only mode, the 1,500 floor, the underweight path, age bounds at 17/18
and 80/81, Katch rejecting 0% fat, the converters, sitewide colours by computed value, Clear
with 0px drift.

### The originality check earned its keep

First build came in at **8.04% article overlap with the BMR page** — far above the ~1% these
pages normally sit at. Inspecting the grams showed why: I had reused my own BMR limitations
bullets and the health disclaimer nearly verbatim, plus three individual sentences. None of it
was copied from the reference; it was self-plagiarism between two neighbouring pages, which is
exactly what Google's helpful-content guidance treats as thin.

Rewrote the limitations list and the disclaimer from scratch rather than adapting them, and
replaced the three repeated sentences. Overlap fell to **2.45%**, and what remains is the
Mifflin/Katch equations (identical by necessity), the standing byline, the about/privacy
sentence and two shared H2 headings.

**Worth generalising:** two calculators in the same family will share formulas and audience,
so the article-only originality check needs running *between our own pages* on every build in
a cluster, not just against the reference. The whole-page check would have hidden this behind
shared chrome.


### Other Units: wrong converter on TDEE, incomplete unit lists on Body Fat (Aug 7, 2026)

The owner sent a screenshot of the reference's five-category converter and asked whether ours
needed updating. It did, in two ways.

**TDEE had the wrong converter entirely.** Checking which script each reference page loads
settles it: Body Fat and TDEE both embed `/converter/converter.php` (five categories), while
BMR loads `/js/quick-conversion.js` (Height and Weight only). I had given TDEE the BMR-style
pair because I built it from the BMR page and assumed neighbouring calculators shared a
converter. They do not. TDEE now has the five-category version; BMR keeps Height/Weight,
which is correct for it.

**Body Fat's unit lists were incomplete.** I had transcribed them from a screenshot rather
than from `/js/conversion.js`, and a scrolling list box hides most of its contents. Against
their actual tables:

| Category | Theirs | Ours before | Missing |
|---|---|---|---|
| Length | 11 | 11 | — |
| Temperature | 3 | 3 | — |
| Area | 11 | 10 | Acre |
| Volume | 23 | 17 | all six Imperial units |
| Weight | 10 | 10 | — |

Several volume factors were also rounded versions of theirs (`0.003785412` against their
`0.00378541`, `0.764555` against `0.764554857984`), which would have put us a digit or two
apart on any US-gallon or cubic-yard conversion. The table is now generated directly from
their script rather than typed, so transcription error is designed out.

Both pages now report 11 / 3 / 11 / 23 / 10 units, asserted as a dict in both suites so a
dropped unit fails a test rather than passing quietly.

### A stray `</div>` that silenced cb_ux

Splicing the new panel into the TDEE markup left one extra `</div>`, which nested the result
card inside the form card. Nothing looked wrong and no JavaScript errored — but `apply_cb_ux.py`
could no longer resolve the result card, so `data-cb-result` was never set and the Calculate
flash stopped working. The suite caught it only because it asserts the flash.

Added a direct guard to all three suites: `document.querySelector('[data-cb-result]')` must
exist. That fails immediately and points at the cause, instead of surfacing three viewports
later as a missing animation. Suites now 106 (Body Fat), 115 (TDEE), 103 (BMR).


## Ideal Weight Calculator — rebuilt from stub, and More Options rolled out (Aug 7, 2026)

Two pieces of work.

### Ideal Weight Calculator (45KB stub -> 96KB build)

Reference: calculator.net/ideal-weight-calculator.html. Input fields 8/8 (age, sex, height in
either system, three tabs including the five-category converter), result fields 5/5 (Robinson,
Miller, Devine, Hamwi, plus the healthy BMI range).

**Formula verification.** 4 Node assertions against the reference's output, all exact on the
first run: US male 5'10" gives 156.5 / 155.0 / 160.9 / 165.3 lbs with a 128.9-174.2 range;
metric male 180cm gives 72.6 / 71.5 / 75.0 / 77.3 kg; metric female 165cm gives
57.4 / 59.8 / 56.9 / 56.4 kg.

Three things the reference does that had to be found rather than assumed:

1. **Under 21 the healthy range is not BMI 18.5-25.** It switches to CDC growth-chart
   percentiles for that age and sex, while the four formulas stay unchanged. The switch is at
   21, not 18. The table is not published anywhere on their page, so it was extracted by
   probing ages 2-20 for both sexes at a fixed height and dividing out h^2 — 38 requests at
   250cm for resolution, which recovers the underlying one-decimal BMI values.
2. **Heights below 5 feet are refused.** Every formula is "base weight at 5 feet plus an
   increment per inch above", so under 60 inches there is nothing to build on. 152cm errors,
   153cm works.
3. **Age range is 2-80**, wider than BMR's 15-80 and TDEE's 18-80. Each page differs.

Content: 1,751-word article that leads with the fact these formulas were written for drug
dosing rather than fitness, which is the single most useful thing a visitor can know before
reading their number. Originality 0.14% against the reference; internal overlap is byline
level, the disclaimer having been written fresh after the TDEE lesson.

86 Playwright assertions, including the CDC-vs-adult switch at 20/21 and the 5-foot floor in
both unit systems.

### More Options control on BMR and TDEE

The owner asked for the Settings checkbox on the health calculators to match
mortgage-calculator's "+ More Options" button. Copied exactly: same markup shape, same
`#131313` full-width button, same `.X-hidden` display rule, same label swap to
"- Fewer Options" on open. Verified by reading computed styles off all three pages side by
side rather than by eye — background, colour, font size, weight, padding and radius all match.

**mortgage-calculator itself is byte-identical**, confirmed by md5 against `git show HEAD`
before committing, since the instruction was explicit that it must not change.

Guide updated with the exact markup and CSS so the next page with an optional section uses it
without going to look.


## Macro Calculator — rebuilt from stub (Aug 7, 2026)

Replaced a 42KB template stub at `/macro-calculator/` with a full 3-card build (103KB).
Reference: calculator.net/macro-calculator.html.

**Parity (§3a-PRIME).** Input fields 15/15 (age, sex, height, weight, activity, **Your Goal**,
the More Options formula and body-fat pair, three unit tabs with the five-category converter),
result fields 6/6 across **five diet tabs** including Create Your Own.

**Formula verification.** The diet tabs are client-side, so rather than reverse-engineering
from two screenshots I pulled the reference's own server-emitted variables
(`balancedProtein`, `lowfatCarbs`, and so on) off a calculated page. That gave twelve exact
figures to solve against, and the model fell out cleanly. 4 Node assertions, all exact.

What the numbers turned out to be:
- **Atwater specific factors, not 4/4/9.** Protein 4.1, carbs 3.75, fat 8.8 Cal/g. Balanced
  protein is exactly `E * 0.25 / 4.1`. Using 4/4/9 would have been wrong on every row.
- **Four fixed percentage splits**, each summing to 100%: Balanced 25/50/25, Low Fat
  27.5/52.5/20, Low Carb 30/40/30, High Protein 35/42.5/22.5.
- **Energy is rounded to whole Calories before the macros are derived.** Their low-carb
  protein is `2549 * 0.30 / 4.1`, not the unrounded 2548.63 equivalent — the difference showed
  up as 186 against their 187 and nowhere else.
- **kJ converts the rounded Calorie figure**, matching their TDEE page.
- Ranges: protein from **1 g per kg of body weight** (not a percentage) to 35% of energy; fat
  20-35%; carbs from 40% up to *whatever is left* once protein and fat sit at their minimums.
  Sugar and saturated fat are each 10% of energy.
- Goal adjustments are the same +/-250/500/1000 as TDEE, and the age range is 18-80.

**Content.** 1,736-word article, 7 H2s, 8 FAQs. Leads with what macros do and do not tell you
(identical numbers can describe very different diets), and explains the Atwater factors, since
that is why our gram figures differ slightly from tools using round numbers.

**Verification.** 122 Playwright assertions: all four splits exact against the reference, every
range, sugar and saturated fat, kJ, Katch, a goal adjustment, the Create Your Own sliders
including the "does not total 100%" note, age bounds, the converter, More Options, sitewide
colours by computed value, Clear with 0px drift.

### The same originality trap, caught again

First build shared 3.7% of its article with TDEE and the reuse was in exactly the two places it
was last time: the **limitations bullets** and the **YMYL disclaimer**. I had adapted rather
than rewritten them. Both rewritten from scratch; non-boilerplate overlap with every sibling is
now a single shared H2 heading, and the reference comparison sits at 0.53%.

This is now a standing guide rule rather than a note in one build log: for any page in a family,
run the article-only check against our own siblings and expect the limitations list and the
disclaimer to be the offenders.


### Macro Calculator — a real bug found by sweeping, not spot-checking (Aug 7, 2026)

The owner asked whether the page's calculations and SEO were right. The honest answer was that
I did not know: four hand-picked cases had passed, which tests the path I already understood.

A **40-case randomised sweep** against the reference — varying sex, unit system, activity, goal,
formula and body, comparing all twelve emitted macro figures per case — found **2 mismatches**.
Both sat where energy runs low relative to body weight.

**The bug.** The reference puts a floor under protein, and rebuilds the whole split when a diet
falls below it: protein to the floor, fat down to its 20% minimum, carbohydrate taking the
remainder. We had no floor at all, so a heavy person on an extreme deficit got protein figures
well under what the reference gives — for a 240 lb 78-year-old on an extreme deficit, 104 g
against their 109 g, with carbs and fat wrong to match.

**Finding the rule took four wrong turns.** From displayed values the floor looked like 1 g/kg,
then 0.83 g/kg, then something energy-dependent — the observed ratio flipped between 1.00 and
0.83 across cases and none of my triggers held. It was settled in a single probe by reading the
**protein slider's `min` attribute**, which exposes the floor directly:

> **0.83 g per kg of body weight for BMR and Sedentary, 1.0 g/kg from Light upward.** Set by
> activity level, independent of energy, sex and formula.

Ported to the page, re-validated: **46 cases, 552 individual figures, all exact.** Suite grew to
131 assertions with both floor regimes covered, plus a check that an unclamped split on the same
body is left alone.

**SEO audit alongside.** Title 56 chars, description 143, canonical, robots, OG with a real image
file, Twitter card, `lang`, viewport, one H1, 7 H2 with all TOC anchors resolving, 8 H3, three
valid JSON-LD blocks with the FAQ matching the visible copy exactly, 10 internal links and no
broken ones, in sitemap.xml, not disallowed, not orphaned (5 inbound internal links). Two gaps
found and one fixed: the exact head term "macro calculator" appeared **zero times** in the
article body, now twice and naturally.

**Noted, not fixed (different pages):** `crypto-profit-loss-calculator` and
`crypto-profit-calculator` share an identical title tag. Also every `sitemap.xml` `lastmod` still
reads 2026-07-03 regardless of when a page was rebuilt, so today's work is not being signalled as
fresh. Both worth a pass of their own.


## Pregnancy Calculator — rebuilt from stub (Aug 7, 2026)

Replaced a 39KB template stub at `/pregnancy-calculator/` with a full build (96KB).
Reference: calculator.net/pregnancy-calculator.html.

**Parity (§3a-PRIME).** All five dating methods with their own input panels — due date, last
period with cycle length 22-44, ultrasound with gestational age, conception date, and IVF
transfer with day-3/5/6 embryo — plus the full 42-week table with trimesters, milestones and
a today marker.

**Formula verification.** 11 Node assertions against the reference's own output, all exact
first run:

| Method | Rule |
|---|---|
| Last period | +280 days, shifted by (cycle − 28) |
| Conception | +266 days |
| IVF transfer | +266 days − embryo age at transfer |
| Ultrasound | scan date + (280 − gestational age in days) |

Also reverse-engineered: week 1 begins 279 days before the due date (so week 40 *ends* on it),
trimesters are 1-12 / 13-27 / 28-42, and the fetal size table was extracted week by week by
probing 39 due dates and reading the reported figures back.

**A bug in the reference, handled rather than copied.** Past week 40 it has no size data and
falls back to printing "your baby weight less than 1 gram at this stage" — obviously wrong for
a term baby, and the sort of line that would alarm someone at 41 weeks. We hold the week-40
figures and label them "average size at week 40" instead.

**Open question for the owner.** The reference's secondary "X months Y days" restatement could
not be reproduced exactly. Calendar months from week 1 matches it in 11 of 13 probes; the two
misses are off by 3 days and 1 day. Their own figure is internally inconsistent (160 days shown
as "5 months 10 days", which is ~162 days), so ours is arguably the sounder conversion — but it
is a difference and it is flagged rather than assumed.

**YMYL treatment, heavier than usual.** A disclaimer sits *above* the article as well as below
it, saying plainly that where these dates disagree with a midwife or doctor, theirs win. The
limitations section leads with twins, and the closing disclaimer names bleeding, pain and
reduced movements as reasons to call, including things the reader is unsure are worth
mentioning. Milestone wording was rewritten from the reference's ("gender can be found out"
became sex usually being visible on a scan).

**Verification.** 81 Playwright assertions: all 11 dating cases exact through the UI, panel
switching, the 42-row table with both trimester boundaries and the single today marker, week 1
and week 40 dates, a future due date reading as not started, scan-day validation, sitewide
colours, Clear with 0px drift. Originality 0.15% against the reference.

### A CSS class collision the assertions missed

The status bar and the progress bar both ended up named `.pg-bar` — the progress bar inherited
the navy background and flex layout, collapsing "Week 1 / 57% through / Week 40" into one
unreadable line. Every assertion passed; it was caught by looking at the screenshot. Renamed to
`.pg-prog`, and there is now a computed-style assertion that the progress bar is *not* styled
like the status bar. **Worth generalising:** these pages are built by prefix-renaming a sibling,
so a new component can silently land on a class the template already uses. Grep the new prefix
for duplicate class names before building.


## Due Date Calculator — rebuilt from stub (Aug 7, 2026)

Replaced a 39KB template stub at `/due-date-calculator/` with a full build (97KB).
Reference: calculator.net/due-date-calculator.html.

**Parity (§3a-PRIME).** Four dating methods — last period with cycle length 22-44, dating
ultrasound, conception date, and IVF transfer with day-3/5/6 embryo. No due-date input, because
here the due date is the output. Full 42-week schedule with trimesters, milestones and a today
marker.

**Formula verification.** The engine is the one built for the pregnancy calculator, and running
it against *this* page's reference gave 10/10 exact on a completely different set of dates
(LMP 2026-06-08 across four cycle lengths, conception, all three embryo ages, two scan ages).
That is a useful independent confirmation: the same rules reproduced two separate reference
pages without adjustment.

**Content.** 1,787-word article, 8 H2s, 8 FAQs, deliberately angled away from the pregnancy
page: the Naegele sum and the assumption inside it, the 4% figure, when clinicians re-date and
when they refuse to, the early/full/late/post-term bands and why term was split in 2013, and
what going past the date actually means. Originality against the reference: **0.00%**.

### The real risk on this page was internal, not external

Pregnancy and Due Date compute the same thing from the same inputs. The first draft shared
**6.61%** of its article with the pregnancy calculator — and the offenders were the same two
places as every previous time, the **YMYL disclaimers** top and bottom, plus repeated statistic
phrasing ("roughly 60% arrive within a week either side", "the centre of a month-wide window").

Both disclaimers rewritten from scratch and the shared phrasings replaced. Overlap fell to
**1.96%**, of which the non-boilerplate remainder is the formula block (identical by necessity)
and two section headings.

Two smaller things the prefix-rename carried over, now both asserted:
- a **self-link** — the sidebar still listed "Due Date" while sitting on the due date page;
  swapped for the pregnancy calculator, with an assertion that no `main` link points at the
  page's own slug.
- the **PDF filename and heading** still said "Pregnancy Timeline" / `pregnancy-timeline.pdf`;
  the suite only checked the extension, so it passed. Now asserts the exact filename.

Also ran the duplicate-class guard the pregnancy build's `.pg-bar` collision prompted: six
duplicates reported, all legitimate media-query overrides or a more-specific selector, none a
collision.

**Verification.** 85 Playwright assertions: all 10 dating cases exact, four-method panel
switching, the 42-row table with both trimester boundaries and a single today marker, scan
validation, no self-link, cross-link to the pregnancy calculator, exact PDF filename, Clear with
0px drift.


### Close-out audit of everything flagged today (Aug 7, 2026)

The owner asked whether the problems found during the day had actually been fixed. Rather than
answer from memory, every fix was re-verified and the newly-learned checks were run
retroactively across all nine pages touched today.

**Verified fixed and holding:** sitewide colour scheme; Other Units missing from Body Fat and
BMR; TDEE carrying the wrong converter; incomplete unit lists (Acre and the six Imperial volume
units); converter layout stacked From-above-To; Settings replaced by the mortgage More Options
button; the BMR result label; the Macro protein floor; the `.pg-bar` class collision; the due
date self-link and PDF filename; sitemap `lastmod` and the two missing URLs.

**Retroactive sweep across all nine pages.** No self-links anywhere else. Every PDF filename
matches its page. The duplicate-class guard reported six hits per page, all false positives on
inspection — sibling (`.x+.x`) and descendant (`.a .b`) selectors, not collisions. The `.pg-bar`
case remains the only real one.

**One genuine finding: four stale assertions on the VA mortgage suite.** They described the
*earlier* Clear behaviour — reset to defaults, scroll the fields back into view, flash the result
card — written before the site standardised on calculator.net's `clearForm()` (empty every typed
box, leave selects and radios, no scroll, no recalculation, no flash). The live page was checked
directly and behaves correctly: 0px drift, no flash, radios and selects untouched. So the page
was right and the tests were out of date, which is its own kind of failure — a suite that
asserts superseded behaviour will eventually block a correct change. Block rewritten; VA suite
now 91 assertions.

**Also closed:** `/crypto-profit-calculator/` was a self-canonicalising indexable duplicate of
`/crypto-profit-loss-calculator/` sitting in the repo. It 301s and is absent from the sitemap, so
it has no effect today, but it becomes a live duplicate the moment `_redirects` is touched. Its
canonical now points at the replacement and it is `noindex, follow`. Deleting the directory
would also work but risks a 404 if redirect precedence ever changes.

**Final state:** VAT 74 · VA Mortgage 91 · Body Fat 97 · BMR 112 · TDEE 124 · Ideal Weight 86 ·
Macro 131 · Pregnancy 81 · Due Date 85 — all passing against the live site.

**Still open, awaiting the owner's decision** (flagged, deliberately not changed):
1. **Body Fat** — the reference publishes the US-customary Navy equations but its calculator
   applies the SI ones to both unit tabs. We match the implementation, so our numbers agree with
   theirs everywhere; switching would match the published Navy method at the cost of the two
   tabs disagreeing by up to ~0.7 points for the same body.
2. **Pregnancy** — the secondary "X months Y days" line matches in 11 of 13 probes, the two
   misses being 3 days and 1 day out. Their own figure is internally inconsistent, so ours is
   arguably sounder, but it is a difference.


### Both open items closed, and a larger correctness bug found while closing them (Aug 7, 2026)

The owner's instruction was that users must get correct calculations and correct information,
so both flagged items were resolved rather than left as questions.

**The bigger find: gestational age was a day behind clinical convention.**

Checking what the reference reports on the due date itself — the single most-quoted number on
either page — it says **39 weeks 6 days**. Convention is unambiguous: gestational age is days
since the first day of the last period, and the estimated due date is that day plus 280, so on
the due date you are **40 weeks 0 days**. The reference starts its table a day after the LMP and
is one day short throughout. We had copied it.

This mattered more than either open item, because it is the figure a woman repeats to a midwife.
Corrected on both pages: week 1 now begins on the LMP, and the due date opens week 41 at exactly
40w0d and is tagged in the table. Verified at the boundary — due date reads 40w0d, the day before
reads 39w6d.

Two related fixes came out of the same pass:
- A due date more than 42 weeks in the past produced **"80 weeks 0 days"**. It now says the date
  is historic and suggests checking the input, rather than extrapolating a pregnancy from it.
- The result line led with the week ordinal, which reads oddly once the due date sits in week 41.
  It now leads with the gestational age — the number people actually use — with the week number
  and calendar months beneath it.

**Item 1, Body Fat SI vs USC — no change needed, and now explained.** On inspection the page was
already correct and self-consistent: it applies the metric Hodgdon & Beckett equations, publishes
exactly those equations, and states that US entries are converted to centimetres first. Nothing
wrong was reaching a user. The real gap was that someone comparing against a tool using the
inch-based form would see a small difference and have no way to know why, so the article now
explains that the inch form is an algebraic conversion of this one, that rounding puts it a few
tenths of a point away, and that running one set of equations for both tabs is what stops the
page contradicting itself when you switch units.

**Item 2, the months restatement — resolved by not copying an inconsistent figure.** The
reference's own "X months Y days" does not reconcile with its own day count (160 days shown as
"5 months 10 days", which is about 162). Ours is exact calendar months from the start of week 1
and is now labelled **"by the calendar"** so the reader knows what is being counted and can check
it. Matching the reference here would have meant shipping a figure that contradicts the day count
sitting next to it.

**Verification.** Body Fat 106, Pregnancy 86, Due Date 90 assertions, all passing, with new
checks covering the due-date convention at the boundary, the historic-date path, and the tagged
due-date row.


- **Workflow / no repo clutter**: all scratch work (`build_*.py`,
  `test_*.js`, `verify_*.js`, screenshots) lives in the sandbox's
  `/home/claude/work/` scratch directory for that session only — it is
  never part of this repo and never committed. Only the actual page file
  (`<slug>/index.html`), its `og/<slug>.png`, and any shared files touched
  (`sitemap.xml`, `calculators-index.json`, `all-calculators/index.html`)
  get `git add`ed. Nothing accumulates in the repo between sessions.

## Pace Calculator — rebuilt from stub (Aug 8, 2026)

Replaced a 41KB template stub at `/pace-calculator/` with a full 3-card build (110KB).
Reference: calculator.net/pace-calculator.html, supplied by the owner with six screenshots
(essential here — their results are rendered server-side and appear nowhere in the fetched
HTML, exactly the failure mode the Inflation Calculator hit).

**Parity (§3a-PRIME).** The reference page is not one calculator but four, and all four are
built: the three-tab main calculator (Pace / Time / Distance, 4 distance units, 10-event
picker, 8 pace units), the 12-row Multipoint segment analyser with its pace-trend chart, the
Pace Converter, and the Finish Time projector. No "Other Units" tab on this page — confirmed
by grepping their markup for `converter.php` / `quick-conversion.js`; neither is loaded.

**Their mile is 1609.35 m, not 1609.344.** This was the whole difficulty of the build. Their
maths is server-side, so the engine was reconstructed by fitting a model to live responses.
An exact-metre mile disagreed with the reference in three independent places: exactly ten
miles renders as "16,093.5 Meters"; 17,600 yards produces 9 mile-split rows, not 10; and the
7K split of the default run reads 43:51 where 1609.344 gives 43:52. A grid search over
candidate constants put the true value in a narrow band, and 1609.35 is the only round number
in it. Yard is 0.9144.

Other behaviours that had to be measured rather than assumed:
- **Splits appear only once distance exceeds 2 km** — at exactly 2.00 km they are absent, at
  2.05 km present. Row counts themselves are plain floors, so this is a separate visibility
  gate, not a rounding effect.
- **Three different time formats on one page.** Race and split tables are zero-padded whole
  seconds (`1:02:39`). The segment table is *unpadded* with 2 decimals and pads minutes only
  when hours exist (`1:05:3`, `5:5`, `6:9.23`). Prose results are worded, with a comma before
  "and" when hours are present and none when they are not.
- **Rounding is half-up, not banker's.** One sweep case (an 11 km split landing on exactly
  2812.5 s) was the only thing that exposed it.
- The main calculator shows six pace units; the finish-time calculator shows eight, adding
  yards per minute and per second. That asymmetry is theirs and is reproduced.

**Verification.** The engine was written standalone and run in Node before being embedded, per
the standing rule. **306 randomised reference cases across all three main tabs — every head
value, all 12 race-table cells and every split row compared — plus 16 targeted assertions for
the three secondary calculators: 322 comparisons, zero mismatches.** The randomised sweep
(10 seeds x 34 cases, varying mode, distance unit, pace unit and magnitude) is what found both
the rounding mode and the 2 km split gate; the four hand-picked cases run first had passed
while both bugs were live — the same lesson as the Macro Calculator.

Then 48 Playwright assertions at 1280/390/430px: default values matched against the reference
for our own (deliberately different) defaults, tab switching and field hiding, the event
picker, cb_ux auto-calculate firing, the 8-row finish-time card, chart bars rendering, Clear
emptying typed boxes while leaving selects untouched with 0px drift, single-track mobile grid
with every child at full width, zero console errors, zero horizontal overflow, and no jsPDF
byte fetched before the button is clicked.

**Content.** 2,373-word article, 8 H2s, 8 FAQs. Originality against the reference page:
**0.00%**. Highest overlap against any of our own pages: **0.04%** (mutual-fund-calculator),
and that match is the byline, which is boilerplate that should repeat. FAQ schema is
*generated from the visible HTML at build time* rather than typed alongside it, which removes
the em-dash/curly-quote drift that has broken this check on every previous build.

**Keyword research.** Head term "pace calculator" is heavily contested (Strava, Active,
Runna, McMillan, calculator.net). US sites overwhelmingly say "Running Pace Calculator", so
per §8 that phrasing is blended into the title rather than replacing the H1. Distinct query
clusters found with their own competitor pages: 5k / marathon / half-marathon pace, pace
charts, pace conversion, finish-time projection. The best-value gap is **splits** — widely
mentioned, rarely titled around, and this page genuinely outputs a full per-km and per-mile
split table plus a segment analyser. Title: "Pace Calculator — Your Running Pace, Splits &
Race Times" (55 chars).

### Open item the owner needs to decide

calculator.net carries a **"Typical Races and World Record Paces"** table and an **exercise
heart-rate-zone image**. Neither shipped, and per the rule that an omission is only intentional
once agreed, this is raised rather than recorded:
- The world-record table is static third-party data. Reproducing their figures verbatim is the
  kind of copying the originality standard exists to prevent, and the records move, so the
  honest version needs current times sourced and the paces computed by us. That is a small
  piece of work, not a decision I should make inside a build.
- Their zone chart is an image asset. Rather than copy it, the article carries an equivalent
  **HTML table of heart-rate zones as a share of max HR**, with the 220-minus-age estimate and
  an explicit caveat about its spread. That substitution is a deliberate difference.

### Edge case knowingly not matched

At distances that are an exact whole number of miles expressed in another unit, their
mile-split row count can differ from ours by one, because the answer turns on floating-point
representation inside their code at a relative difference of ~6e-6. 3,218.69 m is the one
probe found where they show 2 mile rows and we show 1; the 17,600-yard case goes the other way
and we match it. Both are boundary values no visitor types, and no single constant reproduces
both. Recorded rather than papered over.

### Pace Calculator — layout corrected to the site pattern (Aug 8, 2026, same day)

The owner sent a screenshot of `business-loan-calculator` and pointed out the first build had
drifted from the house pattern in four ways. All four were structural, none were caught by the
48-assertion suite, because that suite tested *behaviour* and every one of these is *shape*.

1. **The four calculators were stacked as `<section>`s below the grid instead of being tabs.**
   The correct pattern is what business-loan does with Loan Payment / DSCR / MCA: one grid, one
   form card, one result card, and the top tab row switches which calculator occupies them. Now
   the tabs read Pace Calculator | Multipoint Pace Calculator | Pace Converter | Finish Time
   Calculator, and the bottomgrid swaps between the race/splits pair and the segment chart.
2. **Pace / Time / Distance were top-level tabs; they are sub-modes of one calculator.**
   They now sit inside the form card as a `.pc-mode-toggle` segmented control, mirroring
   business-loan's "I know the loan amount / I know my target payment".
3. **The header block above the bar was bespoke.** The subhead carried an inline style instead
   of `class="text-ink-soft text-lg max-w-2xl mb-6"`, and the crumb margin differed. Both now
   match business-loan exactly.
4. **The sidebar had been rebuilt rather than reused.** It was a plain navy panel with
   underlined text links. The house component is `.pc-calc-card` — navy, a titled header rule,
   one row per link with a right-hand arrow, and a green `.pc-viewmore` button at the foot.
   Restored, including the arrow glyphs and the green.

The result card also changed shape to the house form: coloured head carrying label, big value
and sub-line (`.k` / `.v` / `.s`), body holding the supporting rows, instead of the value
living in the white body.

**The lesson worth keeping.** Every one of these four was a case of building the component from
the design tokens rather than lifting the existing component. §5's note already says to confirm
the donor is current for the *specific component* being copied — the gap is that the first
build picked `body-fat-calculator` as donor for the whole page and never checked whether a
closer donor existed for the parts it lacked. Body Fat has no multi-calculator tab set and no
sub-mode toggle, so both were invented. **Before building any page with more than one
calculator or a solve-for switch, diff against `business-loan-calculator` specifically** — it
is the current reference for tab sets, segmented mode toggles, the sidebar card and the result
card head. Checking that the maths matches the reference site says nothing about whether the
page matches our own.

Re-verified after the rewrite: 54 Playwright assertions at 1280/390/430px, covering all four
tab panels, the three sub-modes, bottomgrid swapping, sidebar computed colours, the subhead
class, cb_ux auto-calculate, Clear with 0px drift, zero console errors and zero overflow.
Numbers unchanged and still matched against the reference. Article 2,378 words, 0.00% overlap
with the reference, 0.04% with our own pages (byline boilerplate).

### Pace Calculator — squeezed input fields (Aug 8, 2026, third pass)

The owner circled the Pace box in "I want my time" mode and asked why it was empty. **It was
not empty.** `00:07:55` was in the DOM the whole time; the input had been squeezed to **24px
wide**, so the value was rendered outside the visible box.

The cause is `min-width:auto` on flex items. `.pc-w-unit` set `flex:0 0 124px`, but a `<select>`
whose longest option is "Kilometers Per Hour" has a min-content width near 180px, and
min-content wins over flex-basis unless `min-width:0` is set explicitly. The select therefore
took ~180px of a ~207px control and left 24px for the input beside it. The distance rows looked
fine purely because their four options (Miles / Kilometers / Meters / Yards) are short enough
to fit — which is exactly why this was invisible during review.

Fixed in three places:
- The eight-option pace-unit selects (main calculator, converter "From") now sit on **their own
  labelled row** rather than sharing a line with the value box. Same fields, same values, just
  not competing for one row.
- Floors added so it cannot recur silently: text inputs `min-width:90px`, all field selects
  `min-width:0`, `.pc-w-unit` changed to `flex:0 1 124px`.
- The multipoint table's per-row unit selects were also cramped (66px, showing "Kilomete…").
  Their display labels are now `km / mi / m / yd` with the full name kept in `aria-label`; the
  submitted values are unchanged. Column widths rebalanced so distance and time inputs land at
  ~121px and the select at 60px.

**New standing assertion.** The suite now runs a `widthGuard` in every mode and every tab,
asserting that no visible text input is under 80px and no visible select under 58px. Two rounds
of tuning it were needed — the first threshold flagged the legitimately-narrow `km` selects —
which is itself the point: the guard forces a deliberate answer about every cramped control
rather than letting one hide. It caught the multipoint case immediately after fixing the pace
case. Screenshots of both panels were checked by eye afterwards, per §"Verify in a browser, not
just in the DOM".

**The wider lesson.** Every previous check on this page asserted that a *value was correct*.
None asserted that the value was *visible*. A `pg.input_value()` assertion passes on a 24px
box, and so did all 54 earlier assertions. Value-correctness and value-legibility are separate
properties and need separate tests; the width guard is now the second one and should be carried
to any page with a value-plus-unit-select row.

## Army Body Fat Calculator — rebuilt from stub (Aug 8, 2026)

Replaced a 42KB template stub at `/army-body-fat-calculator/` with a full 3-card build (86KB).
Reference: calculator.net/army-body-fat-calculator.html, supplied by the owner with a screenshot.

**Parity (§3a-PRIME).** A genuinely simple reference page: one form, no tabs, no unit switcher,
US units only. Inputs are gender radio, age, weight in pounds, and waist as separate feet and
inches boxes. Confirmed no "Other Units" tab by grepping their markup for `converter.php` and
`quick-conversion.js` — neither is loaded on this page. Outputs are the body fat percent, a
compliance sentence naming the standard for the age, and, when over, the percentage and pound
reduction needed.

### Fitting their maths cost most of the session, and blind fitting was the wrong tool

Their calculation is server-side, so the engine had to be reconstructed from live responses. A
linear fit over a probe grid looked convincing — 2.0 per inch of waist, −0.12 per pound for men
— and then broke on boundary cases in ways that made no sense: the same modelled value of 29.33
produced 30, 30 and 29 at three different weights.

Two rounding steps were the reason, and neither is visible in the outputs:
- **Abdominal circumference is rounded to the nearest half inch** before the equation runs.
  Every AC crossing I measured landed on x.25 or x.75, which I first read as evidence about the
  coefficient when it was actually evidence of the bucket midpoints.
- **Weight is rounded to the nearest pound.** Weight crossings all landed on x.5 for the same
  reason.

Because both inputs are quantised, no amount of binary searching on the *inputs* can recover
the true coefficients — the function is a step surface, and I was fitting a plane to stairs.
Switching to a web search for the published equation settled it in one step:

```
Male:    %BF = 1.99 x waist  - 0.12  x weight - 26.97
Female:  %BF = 1.27 x waist  - 0.015 x weight -  9.15
```
with waist in inches, weight in pounds, both inputs pre-rounded as above and the result rounded
to a whole percent, clamped at zero (their page shows 0%, not a negative, for absurd inputs).

**The lesson.** When a reference implements a *published standard*, find the published source
before fitting. I spent most of the build inferring coefficients that were a search away, and
the inferred ones were wrong — 2.0 versus the real 1.99, and a female intercept that failed
half the boundary cases. Fitting is the right tool for a house formula with no public spec; it
is the wrong first move for a regulation. Add to the §3a-PRIME step-1 audit: ask whether the
reference is implementing something documented, and if so read the document.

**Verification.** Engine written standalone and run in Node before embedding: 85 live reference
comparisons during fitting, then 40 held-out cases (randomised across sex, all four age bands,
100-300 lb, quarter-inch waist steps, and both the pass and fail branches) comparing the full
output string set — **0 mismatches**. Re-extracted from the shipped file afterwards and re-run,
per the rule about verifying the code actually written.

Then 38 Playwright assertions at 1280/390/430px: both worked reference cases exact, pass and
fail banner wording and colour, the age-band row highlighting, the gauge pointer, the target
table, cb_ux auto-calculate, Clear emptying typed boxes while leaving the gender radio alone
with 0px drift, the width guard in every viewport, zero console errors, zero overflow, no jsPDF
before click.

**Content.** 1,761-word article, 9 H2s, 8 FAQs. Overlap with the reference page is **0.57%**,
and every match is the standards table digits (`17 20 20 30 21 27 22 32`…) — unavoidable
regulatory data, the same category as the CPI series name noted earlier. Overlap with our own
pages fell to **0.40%** after one fix: the first draft reused the phrase "worked through with
the values this page loads with" from the pace calculator, which is precisely the worked-example
lead-in §"article-only originality check" warns against. Rewritten; no non-boilerplate matches
remain.

**Keyword research.** Head term "army body fat calculator". Competitors are a mix of calculator
sites and Army-adjacent explainers (BodySpec, gigacalculator, calculator.academy). Distinct
clusters with their own pages: "army tape test calculator", "ABCP calculator", "army body fat
standards by age", "one-site tape test". The gap worth taking is the **2023 one-site** framing —
many pages still describe the retired neck-and-waist method, so the title leads with it.

**OG image generated as part of the build this time**, not retrofitted after the owner found it
missing on the pace calculator.

### Pace Calculator — the three open items closed (Aug 8, 2026)

**1. World record pace table added.** The reference carries a static "Typical Races and World
Record Paces" table; it was held back on the first build because copying their figures is the
kind of reproduction the originality standard exists to prevent, and records move. Now built
properly: the record *times* were sourced from World Athletics and cross-checked against
Wikipedia and specialist pace sites, and every **pace figure in the table is computed by this
page's own engine** at build time, so no number is lifted.

Records used, current as of Aug 2026. Note that several are recent enough that Wikipedia's
summary boxes were still stale when checked — the men's mile in particular: Wikipedia listed
El Guerrouj 3:43.13, while World Athletics' own report has **Josh Kerr 3:42.66, 18 July 2026**.
Two independent confirmations were required before using it. Same story for the men's marathon
(Sawe 1:59:30, April 2026) and half (Kiplimo 57:20, March 2026).

Sanity check on our arithmetic: our computed paces match those a specialist pace site publishes
independently for the same records — Cheptegei's 5000 m at 4:03/mile, his 10,000 m at 4:13,
El Guerrouj's 1500 m at 3:41. Distances use 1500 m and 800 m as track events plus the mile,
5000 m, 10,000 m, half and full marathon.

**2. Heart rate zones now vary by age.** The reference has an image plotting exercise zones
against age. Ours was a flat percent-of-max table, which carried less information than theirs.
Replaced with a zone-by-age table giving actual beats per minute for ages 20 through 70 in
ten-year steps, derived from the 220-minus-age estimate, with the caveat about individual
spread kept directly under it. Equivalent information, our own rendering, no image copied.

**3. The mile-split edge case is not ours to fix — and that is now proved, not assumed.**
Earlier this was recorded as a floating-point difference. It is worse than that: the reference
is **internally inconsistent**, and no implementation can match it.

The two probe distances are 3218.688 m and 4828.032 m, which is exactly 1.5x the first. The
reference shows **2 mile-split rows for both**. For any constant M with rows = floor(d/M):

```
floor(3218.688/M) = 2  =>  M in (1072.896, 1609.344]
floor(4828.032/M) = 2  =>  M in (1609.344, 2414.016]
intersection: EMPTY
```

So their row count is not a function of distance through any single mile constant, and the
behaviour cannot be reproduced without replicating whatever internal state differs between the
two paths. Ours uses one constant consistently and is self-consistent; theirs is not. Recorded
as a deliberate divergence rather than an outstanding bug.

**Re-verified after all three changes**: engine re-extracted from the shipped file still passes
306 randomised reference cases plus 16 sub-calculator assertions; 64/64 browser assertions;
FAQ schema still exactly matches the visible text; article now 2,456 words at **0.00%** overlap
with the reference.

### Card headers switched to the white house style (Aug 8, 2026)

The owner flagged the two bottom-grid card headers on the pace and army pages as looking wrong
— a beige `--surface-sunken` fill that sits oddly against the white card body — and asked for
white or the deep navy.

Checked the house pattern before choosing rather than picking by eye. `mortgage-payoff-calculator`,
which §"Schedule and chart are two cards, not one" already names as the reference for exactly
this side-by-side card layout, uses a **white header with a bottom hairline** and a 15px/700
title in `--ink`. No fill. Navy would have been a new invention on this site; white is what the
reference component already does, so both pages now match it:

`padding:16px 18px; font-size:15px; font-weight:700; color:var(--ink);
 background:var(--surface); border-bottom:1px solid var(--border-fine)`

Result card heads stay green and the status bar and sidebar stay navy — the sitewide colour
rule is unchanged; only the neutral card headers moved.

**This is the second time a component was built from tokens instead of lifted from the current
donor** (the first was the tab set, mode toggle and sidebar on the pace calculator). Both times
the fix was to go and read `business-loan-calculator` or `mortgage-payoff-calculator` for the
specific component. Worth stating plainly: for any card, header, toggle or table on a 3-card
page, find the page that already ships that component and copy it, and only style from tokens
when nothing on the site has the component yet.

Re-verified after the change: 64/64 pace and 38/38 army browser assertions, both engines still
exact against the reference (306 + 16 and 40 cases), protected style block byte-identical on
both, FAQ schema still matching the visible text on both.

## Blood Alcohol Concentration (BAC) Calculator — rebuilt from stub (Aug 8, 2026)

Replaced the stub at `/bac-calculator/` with a full 3-card build (92KB). Reference:
calculator.net/bac-calculator.html. Owner asked for the full name in the H1 with "(BAC)" kept,
so the H1 and title read **Blood Alcohol Concentration (BAC) Calculator** while the slug stays.

**Parity (§3a-PRIME).** One form, no tabs: gender radio, body weight with three units, time
since first drink in hours and minutes, and four drink rows (beer, wine, liquor, other) each
with amount, size and ABV. 28 size options, 9 volume units for the free-form row. All present.

### The maths took the longest and the first three attempts were wrong

Server-side again, so it had to be reconstructed. Three false starts worth recording, because
each was a reasoning error rather than a typo:

1. **A clamped search bracket produced garbage constants.** The first probe used a fixed
   `lo=60` pound bracket, and every drink whose crossing weight fell below 60 lb silently
   returned the bracket edge. That made the Widmark factor look inconsistent across drink types
   when it was fine — the measurement was broken, not the model. Any binary search over a
   physical quantity needs its bracket validated against the answer, not assumed.
2. **The dropdown sizes are not the millilitres on their labels.** Every fixed size is held
   internally as a whole or half **US fluid ounce**: "12oz/330ml bottle" is 12 oz (354.882 ml),
   "250ml bottle" is 8.5 oz (251.375 ml), "1 liter" is 34 oz (1005.5 ml). Their own data is
   inconsistent here — `b500` and `c500` are both labelled "16oz/500ml" but one stores 16 oz and
   the other 17. Measured all 28 options individually rather than trusting any label.
3. **The display format is not a fixed precision.** It is 2 decimal places, widened to 2
   significant figures when that would round a small value to one digit: 3.662 shows as 3.66,
   0.0107 as 0.011, 0.0071 as 0.0071. Reading it as "2 significant figures" matched the small
   values and failed on everything above 1.

Settled formula, matching to every case tested:

```
BAC % = (A x 5.24) / (W x r) - 0.015 x H
A = fluid ounces of pure alcohol, W = body weight in pounds
r = 0.73 male / 0.66 female,  H = hours elapsed
```

The r ratio came out as 1.1060601 against 0.73/0.66 = 1.1060606 — seven-figure agreement, which
is what identified those two values rather than any other pair with the same ratio. Volume and
weight units are all standard (1 kg = 1000 g, 1 lb = 453.592 g, US fl oz = 29.5735 ml, UK fl oz
= 28.4131), with "Liter" in the free-form row being the one quantised exception at 34 oz.

**Verification.** Engine written standalone, run in Node before embedding, and re-extracted from
the shipped file afterwards: **42 held-out randomised reference cases** spanning both sexes, all
three weight units, all four drink rows, all 28 sizes and all 9 volume units, comparing both the
BAC string and the hours-to-zero figure — 0 mismatches. Then 36 Playwright assertions at
1280/390/430px including three worked reference cases, the chart, the impairment-band
highlighting, the width guard, cb_ux auto-calculate and Clear with 0px drift.

### This one needed care beyond parity

A BAC calculator can be used to decide whether to drive, and that decision can kill someone. The
page is built so it cannot be read as permission:
- A red banner sits **inside the result card, above the number, on every state**, saying the
  figure is an estimate and must never be used to judge fitness to drive.
- The article says plainly that the estimate can be out by 0.02% either way — the entire
  distance between the legal limit and a charge — and that the page therefore cannot answer the
  driving question and does not try.
- A section on alcohol poisoning with the actual warning signs and instruction to call emergency
  services, and a section for readers whose drinking has stopped being a choice, carrying
  SAMHSA's free 24/7 National Helpline (1-800-662-4357).
- The closing disclaimer repeats all of it.
- The PDF export carries the never-drive line too, since the PDF outlives the page.

**Content.** 1,988-word article, 9 H2s, 8 FAQs. Overlap with the reference **0.00%**; highest
against our own pages 0.42%, all of it the shared byline and about/privacy boilerplate. OG image
generated as part of the build.

### Unit labels overflowing their card — army and BAC (Aug 8, 2026)

The owner sent a screenshot of the Army page with the waist row running off the right edge of
the form card, the "inches" box half-cut, and asked for it to line up with the Age field above.

**Root cause: `.af-unit-tag` and `.bc-unit-tag` were used in the markup and never written in
the CSS.** Both pages shipped with unstyled `<span>`s carrying the unit words. With no width on
them and `min-width:90px` on every text input, a two-input row (feet + inches) demanded more
than the control could give, so the trailing span was pushed past the card, which has
`overflow:hidden` and quietly clipped it. Nothing errored and the width guard passed, because
the guard measures *inputs* and the thing overflowing was a span.

Fixed on both pages:
- `.{prefix}-unit-tag{flex:0 0 32px;...}` — a real, fixed width, so tags cannot be squeezed and
  cannot push siblings out.
- Field labels narrowed from 165px to 80px, which is what actually creates room for a two-input
  row; the hint indent follows at 88px.
- Unit words shortened to `lb`, `ft`, `in`, `hrs`, `min` so they fit a uniform tag width, with
  the full wording moved into the hint line under the waist row.
- Age gets an empty tag of the same width, so its input ends exactly where the rows that do
  carry a unit end.

Result: on the Army page all three input rows now share one right edge, verified at 1280, 430
and 390px (425 / 357 / 317 px respectively, identical across rows at each width). On the BAC
page the same fix removes the overflow; its two rows deliberately keep different inner edges
because one ends in a dropdown and one in a unit tag, while the outer control edges align.

**Check added to the standing suite:** assert that within a form card, every field's *last*
input shares the same right edge, and that no child extends past its control. The existing
width guard would never have caught this — it only looked at inputs and selects, and the
element being clipped was a span. Any element inside a field control can overflow, so the
assertion now measures against the control's right edge rather than against a minimum width.

Re-verified after the change: army 38/38 and BAC 36/36 browser assertions, both engines
re-extracted from the shipped files and still exact (40 and 42 reference cases), protected
style block byte-identical on both, FAQ schema still matching visible text.

## Body Surface Area (BSA) Calculator — rebuilt from stub (Aug 8, 2026)

Replaced the stub at `/body-surface-area-calculator/` with a full 3-card build (86KB).
Reference: calculator.net/body-surface-area-calculator.html. H1 carries the full name with the
abbreviation, matching the convention set on the BAC page.

**Parity (§3a-PRIME).** One form: gender radio, weight with three units, height as feet plus
inches OR centimeters. Output is all eight formulas in three units each, plus the BMI line.
No tabs, no "Other Units" converter — confirmed by grepping their markup for `converter.php`
and `quick-conversion.js`, neither of which this page loads.

### Their own page contradicts their own code on Fujimoto

Seven of the eight formulas reproduced exactly on the first attempt, straight from the equations
printed in their article. Fujimoto did not: ours read 1.80 m² where theirs read 1.79.

Fitting a curve to five probe points showed the ratio was flat at **0.99403** across the whole
range, so only the leading constant differed, not the exponents. Solving it out gives **0.00883**
— and testing that against six cases reproduced their in² figures 6/6, while the constant they
print on their own page, 0.008883, matched 0/6.

So their article states the correct published Fujimoto constant and their code uses a value with
a digit dropped. Per the standing rule on this — *match the field but not the error, and say so*
— **we use the published 0.008883**. Our Fujimoto row therefore reads about 0.6% higher than
theirs. This is the same call made on the FHA upfront-MIP case earlier.

Everything else matched exactly, including the display rules: m² and ft² to two decimals, in² to
a whole number with a thousands comma, and BMI to one decimal with a trailing zero stripped
("50", not "50.0").

**Verification.** Engine written standalone and run in Node before embedding, then re-extracted
from the shipped file: 30 randomised reference cases across both sexes, all three weight units
and both height paths, comparing all eight formulas in all three units plus BMI — **720 compared
values, 0 mismatches** (excluding the deliberate Fujimoto difference). Then 49 Playwright
assertions at 1280/430/390px.

### A CSS specificity bug the new alignment guard caught

The unit column would not take its width: `.sa-w-unit{flex:0 0 60px}` was being beaten by
`.sa-field-control select{flex:1}`, which has one more element in the selector and therefore
higher specificity. The select stayed at flex:1, so the weight row's input ended 97px short of
the height rows' inputs.

This is worth flagging because **the same pattern exists on every page built from this
stylesheet** — a bare `.x-w-unit` class will always lose to `.x-field-control select`. Fixed
here with `.sa-field-control select.sa-w-unit`. Also had to drop the text-input floor from 90px
to 56px, because a row with two inputs and two 60px unit columns cannot fit a 90px floor in the
available width.

The assertion added after the Army overflow — every field's last input shares one right edge,
and nothing extends past its control — is what surfaced both problems, at all three viewports.
It failed three times during this build and each failure was a real defect.

**Content.** 1,573-word article, 8 H2s, 8 FAQs. Overlap with the reference **1.21%**, and every
match is a formula coefficient string (`0 007184 w 0 425 h 0 725`) — unavoidable, the same
category as the Army standards table digits. Against our own pages 0.51%, all boilerplate.
OG image generated as part of the build.

The article carries a clear line that BSA estimates must not be used to calculate or check
medication doses, since per-square-meter chemotherapy dosing is the main reason people look this
up and it is not something a web page should be trusted for.

### BSA unit column widened, full unit names restored (Aug 8, 2026)

The owner circled the weight dropdown: the shortened `lb / kg / g` labels I had used to make the
column fit were the wrong trade, and the fields needed to line up on both edges.

The constraint that forced the abbreviations was that a two-input row (feet + inches) plus two
equal-width unit columns has to fit the control. Solved properly instead: the **trailing** unit
column is 110px on every row so all rows end at the same x, while the "ft" tag sits *mid-row*
and is a narrow 30px variant. Text inputs drop to a 50px floor so the height row still fits.

Result at 1280 / 430 / 390px: first inputs all share one left edge (197 / 35 / 35), last inputs
all share one right edge (347 / 279 / 239), and the dropdown is a full 110px carrying the full
words again.

Checked that the longest option actually fits rather than assuming: measured the rendered text
width of each option against the space inside the select minus padding and arrow — pounds 43px,
kilograms 56px, grams 36px, against 72px available. All three clear.

**Note for the next page with a unit dropdown:** shortening the label is the wrong first move.
The room comes from making the trailing column uniform and letting mid-row tags be narrow, not
from abbreviating the thing the visitor reads.

Re-verified: 49/49 browser assertions at three viewports, engine re-extracted from the shipped
file and still 720/720 exact, protected style block byte-identical, FAQ schema still matching.

## Body Type Calculator — rebuilt from stub (Aug 8, 2026)

Replaced the stub at `/body-type-calculator/` with a full 3-card build (87KB). Reference:
calculator.net/body-type-calculator.html.

**Parity (§3a-PRIME).** Four measurements (bust, waist, high hip, hip), each with its own
inches/cm selector. Output is the body shape name plus the waist-hip ratio, and a WHO note when
the ratio is high. No tabs, no unit converter — confirmed by grepping their markup.

**The maths was the easy part for once.** The seven classification rules are printed on their
page and reproduced exactly on the first attempt, including the evaluation order, which matters:
several measurement sets satisfy more than one rule and the first match wins. Two details had to
be measured rather than assumed:
- **The waist-hip ratio strips trailing zeros** — "0.6", "1", "0.8", not "0.60".
- **The WHO note threshold is on the *displayed* ratio, not the raw one.** Binary search put it
  at exactly 0.855, which is the point where the 2-decimal display becomes 0.86. So the
  condition is `round(whr, 2) > 0.85`, not `whr > 0.85`.
- Some measurement combinations match none of the seven rules. The reference says so rather than
  forcing a category, and so do we.

**Verification.** Engine written standalone, Node-verified before embedding and again after
extraction from the shipped file: 45 randomised reference cases comparing shape, ratio string
and the presence of the WHO note — 0 mismatches. Then 45 Playwright assertions at 1280/430/390px
covering all five worked reference cases, the no-match path, the cm conversion path, the shape
highlighting, and both edge-alignment guards.

### This page needed a different kind of care

A body-shape calculator sits close to body image, and the reference's own framing calls the
hourglass "typically presented as the ideal". The build deliberately does not:
- The subhead says it is for finding clothes that fit, **not a verdict on your body**.
- The article states in its first section that there is no ideal shape here and the categories
  are descriptive, not ranked, and later notes that the shape marketed as the default is the
  rarest one actually measured (about 8%).
- A section on using the result to shop ends by saying the clothes are supposed to fit the
  person, explicitly pushing back on styling advice built on dressing every body to look like an
  hourglass.
- No advice anywhere on changing your shape, no goal measurements, no weight targets.
- The disclaimer carries the National Alliance for Eating Disorders helpline (1-866-662-1235),
  per the standing note that NEDA's line is disconnected and this is the correct referral.
- The WHO note is worded as a reason to raise it with a doctor rather than as a verdict.

**Content.** 1,720-word article, 8 H2s, 8 FAQs. Overlap with the reference **3.11%** — the
highest so far, and every one of the 53 matching runs is classification-rule text
(`bust waist 9 or hips waist 10`) or a shape name adjacent to it. Checked explicitly: zero
shared prose sentences. Against our own pages 0.59%, all boilerplate. OG image built in.

### Body Type Calculator — original SVG illustrations added (Aug 8, 2026)

The owner asked for the two illustrations the reference has — the measurement diagram beside the
form and the body-shape figures — but sourced from Pinterest rather than copied from
calculator.net.

**Declined the Pinterest sourcing and said why.** Effectively every image on Pinterest is under
someone's copyright; Pinterest grants no reuse licence. AdSense program policy prohibits
copyright-infringing content and this site is still pending approval, so a scraped image is a
live risk to the application, not a theoretical one. The same objection applies to tracing the
reference's own artwork.

**Drew our own instead, parametrically.** `svggen.py` builds body outlines from cubic paths
whose control points are computed from bust / waist / high hip / hip values, so each of the
seven shapes is generated from proportions rather than drawn by hand or traced from anything:

- **Seven shape silhouettes**, one per card in the shapes grid, each generated from
  representative proportions for that category. Strokes use `currentColor`, so the card matching
  the visitor's measurements renders its figure in the site green while the rest stay navy.
- **A measurement diagram** in the bottom-right card, showing a single figure with dashed
  callout lines at the bust, waist, high hip and hip, with leader lines and labels.

Total cost about 10KB of inline SVG, no image requests, sharp at any density, and it themes
itself from the site palette. The page is 98KB, still under the 110KB the other builds sit at.

Two rounds of visual iteration were needed and both were caught by looking rather than
measuring: the first outlines were squat and lumpy at the hip-to-hem transition, and the first
integration rendered the figures at 38px where the seven shapes are indistinguishable. Now 54px.

**New assertions**, since this is the first page carrying illustrations: seven `svg.bt-fig`
elements present, the measurement diagram present, zero `<img>` elements anywhere in `main`,
zero image requests to any third-party host, and the matched figure computing to `rgb(22,163,74)`.
That last one is the guard against the figures silently losing their highlight. 50/50 passing.

**Standing note for future pages:** when a reference page carries artwork, generate an
equivalent rather than sourcing one. Parametric SVG has been cheaper than finding a licensed
image would have been, and it carries no attribution or licensing obligation at all.

### Bra Size Calculator — visual cup-size guide added (Aug 8, 2026)

The owner sent a Pinterest infographic for a bra size calculator and asked for something like it,
explicitly so that AdSense has no problem and visitors understand the page more easily.

**Same answer as the body-type page on sourcing:** the sent image is itself a third-party
copyrighted pin, so it was not copied, adapted or traced. Built the equivalent ourselves.

**What the page already had:** it turns out this page was never a stub — it is a full 94KB build
with its own inline SVG measurement diagram in the How to Measure section, SVG breast-shape
buttons in the form, and reference tables for band and cup sizes. Checked before building
anything, which saved duplicating work that already existed.

**What was genuinely missing** was the single most useful element of the infographic: a *visual*
cup-size guide. The page explained the bust-minus-underbust rule in prose and in a table, but
nothing showed the visitor where their own result sat on the scale. Added a row of cup pills
(AA through G) under the result rows, with the inch difference beneath each and the visitor's own
cup filled in the site green, re-rendered on every calculation from the existing `calcBra` result
so it can never drift from the number above it.

Details worth keeping:
- Labels follow the unit toggle — inches in inch mode, converted centimetres in cm mode.
- Above G the window slides, showing the eight letters ending at the visitor's cup, so very large
  differences still land on a visible highlighted pill rather than running off the end.
- Laid out as a 4-column grid that becomes 8 columns above 1100px. The first attempt used flex
  with `flex:1 1 52px`, which let the two pills on the wrapped second row stretch to double width
  — uniform pill widths verified at all three viewports (39 / 85 / 75px, all equal within 1px).

Cost: about 1.5KB. No image requests, nothing to license.

Also re-asserted after the edit, because this was a surgical change to an already-shipped page
rather than a rebuild: protected style block still byte-identical *both* to the reference page
and to this page's own previous version, FAQ schema still matching visible text, title and H2
count unchanged, zero console errors, zero overflow.

### Body Type Calculator — owner-supplied illustration added (Aug 8, 2026)

The owner supplied an AI-generated four-shape illustration (the filename showed it was generated
in ChatGPT, so it is their own asset — the copyright objection raised against the earlier
Pinterest suggestion does not apply here) and asked for the heading and footer text cropped off,
since that copy already exists in our article.

**Crop was measured, not eyeballed.** Profiled the row and column variance of the source to find
where the heading block, the coloured dot row, and the "Remember" strip actually end, then cropped
to those lines: `(146, 228)` to `(1415, 912)`. The first pass cut at y=198 and left the dot row
visible, which the profile made obvious on review.

**Delivered at 47KB.** Resized to 1200px wide and saved as WebP at q82, which is 47KB against
630KB for the equivalent PNG. No PNG fallback shipped — WebP has universal support now and a
630KB fallback would defeat the point.

**Placed where it is actually relevant.** The image shows the *four* fashion shapes while this
calculator uses the *seven*-category research system, so dropping it at the top would contradict
the tool. It sits in the "Why fashion says four and research says seven" section instead, with a
caption that states the relationship explicitly. The seven parametric SVG silhouettes stay where
they are, in the shapes grid.

Shipped with `width`, `height`, `loading="lazy"`, `decoding="async"` and a 125-character alt
describing what the figure shows — dimensions present so it cannot cause layout shift.

Suite updated: the previous "zero `<img>` in main" assertion was correct when the page had no
raster images and is now wrong, so it is replaced by two better ones — every `main` image is
served from our own `/img/`, and the content image carries alt text, explicit dimensions and lazy
loading. The third-party-image-request guard still stands and now covers `.webp` too. 51/51.

## Calories Burned Calculator — built (Aug 8, 2026)

Two calculators on one page at `/calories-burned-calculator/` (99KB): 106 activities by duration,
and walking/running/cycling by distance. Reference: calculator.net/calories-burned-calculator.html.

### The reference does not follow the formula it publishes

Their page prints `Calories = Time × MET × Body Weight / 200`, which is linear in weight. It is
not. Measured at 10 hours of slow walking, kcal per kg per hour reads 2.246 at 40 kg, 2.070 at
80 kg and 2.057 from 85 kg up. Duration scales perfectly linearly; weight does not.

A one-kilogram sweep showed the curve is **piecewise linear**, and sweeping in pounds put the
breakpoints at **125, 155 and 185 lb** — the column headings of the classic published calorie
tables. So each activity carries three anchor rates, the per-pound rate is interpolated linearly
between them, and it is held flat outside. That reproduces their output exactly, including their
own default (45 min, 150 lb, walking slow = 108) which the printed formula gives as 105.

The distance calculator uses the same anchors with a second interpolation over speed. Fitting
lines to sampled points left ±1 calorie errors; the fix was noticing the fitted nodes matched
named activities **exactly** — walking fast at 3.5 mph has the same rate as "Walking: fast", to
four decimals. Rebuilding the curves from the exact anchor rates rather than fitted lines made it
exact. Recovered speeds: walking 2.0/2.8/3.5/4.0, running 5.0/6.0/7.5/10.0, cycling
13/15/17.5/21 mph.

**Three rounded unit constants** also had to be measured rather than assumed: km/h→mph uses
0.621, min/km uses 0.6215 and yd/s uses 2.045, not the exact conversions. Miles, meters and m/s
are exact. Found by brute-forcing the constant against collected reference cases.

### Two broken entries in their data

- **Cycling, Stationary: vigorous** — total calories at 155 lb come out *below* the 125 lb figure
  (556,000 vs 630,000 over 1000 h), which cannot be right. As METs the 125 and 185 anchors read
  11.1 and 10.5, both sane, while 155 reads 7.9. Fixed by interpolating the middle anchor.
- **Walk/Jog: jog <10 min.** — the radio value contains a raw `<`, and their own server answers
  "Please select an activity" for it, so the activity can never be calculated on their site.
  Included here using the Compendium MET of 6.0.

The other 104 reproduce exactly.

**Verification.** Engine written standalone, Node-verified, then re-extracted from the shipped
file: 45 duration cases (random activities, both weight units, 5–900 minutes) and 45 distance
cases (all three activities, all six speed units, all four distance units) — **0 mismatches** —
plus a 40-case unit-conversion sweep, also 0. Then 38 Playwright assertions at three viewports,
including that all 106 activities are reachable across the five categories, both reference
worked examples, and both edge-alignment guards.

One assertion failed on first run because I had guessed 640 calories for running fast where the
reference gives 657. The engine was right and my guess was wrong — the article's illustrative
figures were all replaced with queried values rather than estimates.

**Content.** 1,550-word article, 8 H2s, 8 FAQs. Overlap with the reference **0.00%**. Against our
own pages 2.48% versus body-type, which is entirely the shared disclaimer and byline — the eating
disorder helpline text is deliberately identical across both.

## Carbohydrate Calculator — rebuilt from stub (Aug 8, 2026)

Replaced the 44KB template stub at `/carbohydrate-calculator/` with a full 3-card build
(106KB, `carb-` prefix). Reference: calculator.net/carbohydrate-calculator.html, supplied by
the owner with four screenshots covering US units, metric units, the Other Units converter
and the expanded Settings panel. Donor for the shared chrome was `tdee-calculator` — the
protected style block, header and footer were confirmed byte-identical afterwards.

**Keyword research.** Head term "carbohydrate calculator" is dominated by calculator.net
itself plus a long tail of macro tools; the higher-intent variants that have their own
competitor pages are "how many carbs should i eat a day", "carbs per day calculator" and
"carb calculator for weight loss" — the first is a question the page now answers in its own
H2 and FAQ rather than only in the tool. Title written for the click rather than the
impression: *Carbohydrate Calculator — Daily Carb Grams for Your Goal* (56 chars, inside the
40–65 band), description 144 chars leading with the gram outcome and the four percentages.

### Their published formula is not the formula they use

The page prints nothing about energy density, and every diet source quotes 4 Calories per
gram of carbohydrate. Their numbers do not follow from 4. Measured against the live page the
divisor is **3.75** — the FAO/INFOODS factor for available carbohydrate as monosaccharide
equivalents. This is defensible rather than a bug, so it was matched and then explained on
the page in its own H2, which is a genuine differentiator: no competing calculator surfaces
it, and it accounts for the ~6% gap between this page and any 4-based tool.

Two further details had to be measured, not assumed:

- **The percentage cells are computed from the unrounded calorie allowance**, while the
  calorie column shows that same value rounded. Deriving grams from the displayed calories
  is off by one gram in a good fraction of cases.
- **Their pound is `0.453592`, not `0.45359237`.** Found through a single failing case in the
  first 40-case sweep: one ounce figure read 25.89 where the exact constant gives 25.895 and
  rounds to 25.90. Before changing it, three purpose-built discriminating cases were put to
  the reference to rule out the alternative explanation (that the ounce divisor was 28.35
  rather than 28.3495) — the reference sided with 28.3495 all three times, which left the
  pound constant as the only candidate. Gram-per-ounce and gram-per-pound are **not** rounded:
  28.3495 and 453.592.

### Verification

Engine written standalone in Python and swept against the live reference twice with different
seeds — **90 cases, 0 mismatches** — comparing every row label, the calorie column and all
four percentage cells including Oz and lb, across both unit systems, both formulas, both
sexes and the full 18–80 / 1.2–1.9 input space. Then the *shipped* page was driven in
Chromium over a fresh **60 random cases** against the same engine: **0 mismatches, 0 console
errors**. Hand-picked cases would not have found the pound constant; the sweep did, on case 31.

Separately, the Other Units converter's unit tables were diffed field by field against the
reference's own `/js/conversion.js` (fetched live): Length 11, Area 11, Volume 23, Weight 10,
**0 mismatches** on both names and factors, with Temperature handled as offsets. Note the
script also carries a time array (`mA`, 11 units) that this page's converter does not expose —
the rendered tab set is five, confirmed against the owner's screenshot.

**48 browser assertions, all passing**: H1 computed weight 700, sitewide status-bar sentence,
More Options button computed style identical to mortgage-calculator's, result head and
Calculate both `#16A34A`, six activity multipliers matching theirs exactly, US vs metric row
labels and the metric grams-only cells, converter category and unit counts, Clear emptying
every typed box while leaving selects and radios alone and moving the pressed button under
40px, `__cbAutoRuns` incrementing on input with no page movement, `.cb-flash` and `.cb-jump`
present, jsPDF fetching zero bytes before the click, no horizontal overflow and a single grid
track at 1280/430/390px with every child at full column width, and card edge alignment.

### One deliberate wording difference from the reference

Their footnote attributes a **40% to 65%** range to the Institute of Medicine. The IOM AMDR
for carbohydrate is **45% to 65%** (RDA 130 g/day), verified against the DRI literature before
writing. The 40/55/65/75 columns were kept exactly as theirs so the numbers stay in parity,
but our footnote states the ranges correctly and says plainly that the 40% column sits below
the IOM floor as a lower-carbohydrate option rather than a recommendation. Repeating a wrong
attribution on a YMYL page was not worth field-level fidelity in prose. Flagged to the owner
in the completion report, not made quietly.

**Content.** 2,422-word article, 9 H2s, 8 FAQs, table of contents, byline and YMYL disclaimer.
Overlap with the reference **0.00%**. Against our own health pages the worst is **0.95%**
(bmr-calculator), with macro, tdee and body-fat all at 0.83% — boilerplate level, well under
the ~1.2% this repo has been running at. The near-duplicate trap was live here: Macro, TDEE and
BMR share this page's inputs and its whole first calculation step, so the limitations section
and the disclaimer were written from scratch rather than adapted.

**Also shipped**: OG image at `/og/carbohydrate-calculator.png` in the house style (IBM Plex
Sans is not installed in the build environment, so the display face falls back to DejaVu Sans;
the mono chips use real IBM Plex Mono). `calculators-index.json`, `sitemap.xml` and `llms.txt`
already carried the slug from the stub, so no entry was needed. Reciprocal sidebar links added
from **tdee, bmr and calorie**; macro and fat-intake already linked here. That is four files,
scoped to this build — **not** the site-wide inbound-link sweep, which stays deferred.

## Conception Calculator — rebuilt from stub (Aug 8, 2026)

Replaced the 40KB template stub at `/conception-calculator/` with a full 3-card build
(88KB, `con-` prefix). Reference: calculator.net/conception-calculator.html, supplied by the
owner with a full-page screenshot. Donor for the shared chrome was `due-date-calculator`,
the current sibling for a date-driven health page; protected style block, header and footer
confirmed byte-identical afterwards.

**Keyword research.** The head term is contested by Flo, What to Expect, the American
Pregnancy Association and calculator.net, all with deep pages. The variants with their own
dedicated competitor pages — and therefore real query clusters rather than phrasings — are
"fertile window calculator", "best days to get pregnant" and "when am I most fertile"; those
drive the H1 subhead, the result-card label and two FAQs. Title *Conception Calculator —
Your Fertile Window and Best Days* (57 chars), description 155.

### The model, read off the page rather than out of it

Their page explains none of its arithmetic. Probed live, every date follows from ovulation
placed at **cycle length minus 14**, not at a fixed day 14 — i.e. counted backwards from the
next period, not forwards from the last one:

- ovulation window = O−2 … O+2
- most probable conception days = O−2 … O+3
- best intercourse days = O−5 … O+2
- pregnancy test = O+9
- next period = LMP + cycle
- due date = LMP + 280 + (cycle − 28), which is the same thing as O + 266

The six-cycle table repeats the whole calculation for period starts at LMP + k·cycle. The
month calendar tracks the **probable-conception** window, not the LMP month — a 44-day cycle
entered with an August LMP renders September only — and renders two grids when the window
straddles a month boundary. Both behaviours were confirmed against the reference and are
reproduced.

### Verification

Engine written standalone and swept against the live reference twice — **75 cases, 0
mismatches** — comparing all six milestone dates, the calendar month list, the exact set of
highlighted days, and all eighteen cells of the six-cycle table, over random LMPs across
2025–2028 and every cycle length from 22 to 44. Then the shipped page was driven in Chromium
over **50 fresh random cases** against the same engine: **0 mismatches, 0 console errors**.

**50 browser assertions, all passing**, including the two failure modes specific to this page:

- **Timezone off-by-one.** `new Date('2026-01-01')` parses as UTC midnight and lands on
  Dec 31 west of Greenwich, shifting every date by a day. The page parses the box manually
  into a local date; there is an explicit assertion on a Jan 1 input.
- **Month-straddling calendars.** Asserted that an LMP of Feb 15 2027 renders February *and*
  March grids, and that a within-month window renders exactly one.

Also asserted: H1 weight 700, sitewide bar sentence, result head and Calculate both
`#16A34A`, sidebar `#1E3A5F`, cycle select carrying exactly 22–44 with the reference's "N days"
labels, six-cycle table headers, six highlighted days, Clear emptying the date box while
leaving the select alone and moving the pressed button under 40px, `__cbAutoRuns` on change
with no page movement, `.cb-flash` and `.cb-jump`, jsPDF fetching zero bytes before click, no
horizontal overflow and a single grid track at 1280/430/390px, and card edge alignment.

### Deliberate differences

1. **A real date input instead of their three dropdowns.** They build the date from month,
   day and year `<select>`s via `DateInput()`. Ours is `<input type="date">`, which is what
   `due-date-calculator` and `pregnancy-calculator` already use, so this is the house
   convention rather than a new decision. Side effect worth recording: their select trio
   permits Feb 30, which their server silently rolls forward to Mar 2 (verified). A native
   date picker cannot produce it, so that path does not exist here.
2. **A Clear button, which the reference does not have.** Their form is Calculate only. The
   site design system specifies a Calculate + Clear row, and with a real date box Clear has
   something to do — it empties the box, leaves the cycle select untouched, and does not move
   the page, per §"The buttons are part of parity too".
3. **Default LMP is today minus 14 days**, where theirs is today. Defaults must differ per
   §3a-PRIME, and this one also lands the visitor mid-cycle so the first thing on screen is a
   window they can act on rather than one a fortnight away. Cycle length stays at 28 because
   28 is the clinical standard, not the reference's invention.
4. **An "Estimated ovulation day" row** the reference does not print as a line, though its
   whole table is built around that date and the calendar marks it. It is the anchor every
   other row is derived from, so stating it is disclosure rather than a new feature.

**Content.** 2,062-word article, 9 H2s, 8 FAQs. Overlap with the reference **0.05%** — a
single eight-word run of unavoidable phrasing. Against our own pages the raw figure is 1.81%
versus carbohydrate-calculator, which is entirely the byline and the about/privacy disclaimer
sentence; with those excluded the article body is at **0.10%**, and the remainder is two
shared H2 headings. Against the two pages that genuinely overlap in subject —
due-date-calculator 0.63% and pregnancy-calculator 0.59% — the near-duplicate trap was
handled by giving this page a different angle entirely: it is about the window before
conception, where those two are about dating a pregnancy after it.

**Also shipped**: OG image at `/og/conception-calculator.png`. `calculators-index.json`,
`sitemap.xml` and `llms.txt` already carried the slug from the stub. due-date-calculator and
pregnancy-calculator already link here from their sidebars. **No new reciprocal links were
added**: the four other natural linkers — ovulation, period, pregnancy-conception and
pregnancy-weight-gain — are all still React/Tailwind stubs with no sidebar card to insert
into. They should pick this page up when each is rebuilt; nothing was edited in them.

## GFR Calculator — rebuilt from stub (Aug 8, 2026)

Replaced the 44KB template stub at `/gfr-calculator/` with a full 3-card build (96KB,
`gfr-` prefix). Reference: calculator.net/gfr-calculator.html, supplied by the owner with
two screenshots showing both calculators. Donor for the shared chrome was `tdee-calculator`;
protected style block, header and footer confirmed byte-identical afterwards.

**Keyword research.** Head term "gfr calculator" is held by MDCalc, the National Kidney
Foundation and calculator.net. The variants with their own competitor pages are "egfr
calculator", "ckd-epi calculator", "creatinine clearance calculator" and "schwartz formula
calculator"; the first three are folded into the tab labels, result rows and FAQ, and the
fourth is the children's tab. Title *GFR Calculator — Kidney Function From Serum Creatinine*
(56 chars), description 148.

### The maths

Two calculators on one page, presented as tabs the way `calories-burned-calculator` does
rather than as two stacked forms. All four equations reproduce exactly:

- **MDRD 4-variable** — 175 × Scr^−1.154 × age^−0.203, × 0.742 female, × 1.212 Black
- **CKD-EPI (2009)** — base × (Scr/k)^a × 0.993^age, k 0.7/0.9, base 144/141 non-Black and
  166/163 Black, exponent −0.329/−0.411 below k and −1.209 above
- **Mayo quadratic** — exp(1.911 + 5.249/Scr − 2.114/Scr² − 0.00686·age − 0.205 female),
  with Scr floored at 0.8
- **Bedside Schwartz** (children) — 0.413 × height in cm ÷ Scr

**The micromole divisor is 88.4, not 88.42**, and that had to be measured. Three
purpose-built discriminating cases — inputs where the two candidates disagree in the last
displayed digit — were put to the reference, and it sided with 88.4 all three times. Same
technique as the pound constant on the carbohydrate page; it is now the standard way to
settle a rounded constant here rather than assuming the textbook value.

### Verification

Engine written standalone and swept against the live reference twice — **85 cases, 0
mismatches** — mixing adult and paediatric cases, both creatinine units, both height units,
both sexes and both race settings, across creatinine 0.3–9 mg/dL and 25–800 µmol/L. Then the
shipped page was driven in Chromium over **55 fresh random cases** against the same engine:
**0 mismatches, 0 console errors**.

**52 browser assertions, all passing.** Beyond the usual set: the reference's own worked
examples reproduce exactly (89.3 / 99.2 / 120.3 for 0.9 mg/dL, age 50, male, not Black; 50.5
for the child default), the CKD stage table and the population-mean table match theirs row
for row, the stage row matching the current result is highlighted and no row is highlighted
on the children's tab, age under 18 is refused on the adult tab and a zero creatinine is
refused on both, and — per the tabbed-page warning in section 5a — auto-calculate was
re-checked **after** switching tabs, not just on the first one.

### The race coefficient — parity kept, deprecation stated

The reference's adult form has a **Race** radio (Black / Not Black) which multiplies MDRD by
1.212 and switches the CKD-EPI base constants. That coefficient is no longer clinical
practice: in September 2021 a joint NKF–ASN task force concluded it lacked biological
justification and called for immediate adoption of the race-free **2021 CKD-EPI creatinine
equation**, which US laboratories now report. Verified against NKF, ASN and the AJKD/KDOQI
position statement before writing a word of it.

Handled as follows, and the reasoning is worth carrying forward because this will recur:

- **The field is kept and the maths is unchanged.** Removing it would silently alter what the
  reproduced equations produce, and parity is the specification.
- **It is flagged in three places** — a caution box directly under the Race control linking to
  the explanation, the "The 2009 version, with a race coefficient" subtitle on the CKD-EPI
  result row, and a dedicated H2 covering the task force decision and its practical effect
  (delayed staging, referral and transplant listing for Black patients).
- **The 2021 race-free equation was deliberately NOT added as a fourth result row.** It would
  be genuinely useful and it is what a visitor's lab actually reports — but adding an equation
  the reference does not have is an extra, and §"Standing rule on scope" says extras are a
  proposal to the owner before building, never a decision made inside one. **Raised with the
  owner in the completion report; not built.** If he says yes it is a small change: one more
  row and one more paragraph.

The caution box originally used a new amber palette and was recoloured to the existing
sitewide caution pair (`#8E2233` on `#FCEDEF`, border `#F0C6CC`) before shipping — no new hex
values were introduced, per §"One colour scheme sitewide".

### Other deliberate differences

- **A headline number.** The reference prints three equal results and no primary figure; our
  result card needs a big number, so it uses CKD-EPI, labelled "CKD-EPI 2009" in the subtitle.
  All three still appear as rows, and none is presented as more correct than the others.
- **Defaults differ per §3a-PRIME**: 1.1 mg/dL, age 42, female (theirs: 0.9, age 50, male);
  children 0.6 mg/dL and 132 cm (theirs: 0.9 and 110 cm). Race stays on "Not Black", which is
  the no-multiplier setting rather than a value worth varying.
- **A spread figure** under the results, showing the gap between the highest and lowest of the
  three equations. It is derived entirely from numbers already on screen, and it makes the
  point the article makes: a wide spread means creatinine is pinning the answer down poorly
  for this body.

**Content.** 2,305-word article, 9 H2s, 8 FAQs. Overlap with the reference **0.00%** despite
both pages necessarily printing the same four formulas — the formulas live in a code block, not
in prose. Against our own pages the raw worst is 1.75% (conception-calculator) and 1.71%
(carbohydrate-calculator), both entirely byline and disclaimer boilerplate.

**Also shipped**: OG image at `/og/gfr-calculator.png`. `calculators-index.json`, `sitemap.xml`
and `llms.txt` already carried the slug. Reciprocal sidebar links added from **bmi, bmr,
body-fat and body-surface-area** — four files, scoped to this build, not the deferred
site-wide sweep.

### GFR Calculator — the CKD stage table belonged in the result, not the bottom grid (Aug 8, 2026)

Owner reported, on the day of the build, that the adult result card looked like it carried
less than the reference and did not read the way theirs does. He was right, and the
completion report had said "Result fields: 10/10" — so this is worth recording, because the
checklist passed while the page was still wrong to a reader.

Dumped the reference's result region as plain text and read it in order:

1. Result heading
2. "The following are the GFR results based on 3 formulas often used:"
3. Formula / Result table, three rows, each with the unit
4. **"Chronic Kidney Disease Stages" heading and the six-row stage table**

Item 4 is *inside their result block*. Ours had it in the bottom grid, two cards down. Every
field existed, so a field-presence check passed — but on screen the visitor got three bare
numbers and no way to read them, which is exactly the complaint. **Presence is not parity if
the reader has to go looking.** A result element the reference prints under its result belongs
under ours.

Fixed by moving the stage table into the result card in the reference's order, with the row
matching the current CKD-EPI figure highlighted, and by spelling the band out on the stage
line itself (`CKD3 (Moderate)` now carries `30 to 59` underneath) rather than making the
visitor match a code against a table. The bottom grid slot it vacated became a new
**The Three Equations** card — each equation, the population it was fitted on, and where it
reads best — which is genuinely new information rather than a second copy of the table.

Children's tab checked at the same time and matches the reference exactly: their paediatric
result is the single Schwartz number and nothing else, no stage table. The block is therefore
hidden on that tab and while the form is in error, rather than shown with nothing highlighted.

One thing the screenshot caught that the assertions had not: the closing note under the
result still read "where the three equations disagree widely" on the children's tab, which
shows one equation. That is the §"if a page's prose describes a feature that is later removed,
the prose has to be rewritten" failure in miniature. The note is now written per mode.

Re-verified after the change: **59 browser assertions, 0 failed** (four new ones covering
where the stage table lives, that it hides on the children tab and in the error state, and
that the closing note is mode-appropriate), plus **40 fresh browser cases against the engine,
0 mismatches**. One assertion failed on the first run because it expected the "60 to 89" band
for the reference's own worked example, which actually lands in Normal/CKD1 — the test was
wrong, not the page, and it was corrected rather than the page bent to fit it.

### GFR Calculator — used it as a visitor, then added the equation their lab actually reports (Aug 8, 2026)

Owner asked for a judgement call rather than a fix list: use the page as a human would, and
change whatever a real visitor would trip over. Did that with a concrete scenario — a
58-year-old woman holding a blood test that reads creatinine 1.4 mg/dL and **eGFR 44**.

Three things broke, in descending order of seriousness.

**1. None of our numbers matched her lab report.** The page showed 41.4 as the headline, with
38.6 / 41.4 / 53.5 below. Her report says 44. Nothing on screen was that number, because US
laboratories report the **2021 race-free CKD-EPI equation** and the reference tool implements
only the three older ones. A visitor comparing the two concludes the calculator is broken.
This was the whole point of the earlier "should we add the 2021 equation" question, and using
the page for two minutes settled it.

**2. The Race field was a dead end.** The box explained the history and then told her nothing
about what to do. Ticking Black moved the headline from 41.4 to 47.8 — a six-unit jump with no
guidance attached, on a YMYL page.

**3. Analyst language in the result.** "Spread across equations 6.7" means nothing to someone
holding a lab slip, and "Estimated GFR (CKD-EPI)" names a formula the reader has never heard
of.

**What changed.** The 2021 CKD-EPI creatinine equation was added and made the headline. It is
listed first in the results, highlighted, and described as "Race-free — what a US lab report
shows today". Constants taken from NKF, NIDDK and the Tufts implementation guide, all three of
which also state the µmol/L divisor as 88.4, independently corroborating the value measured
off the reference earlier. The same scenario now returns **43.6**, against her lab's 44.

The Race field keeps full parity — it still drives MDRD and CKD-EPI 2009 exactly as before —
but it no longer touches the headline, so the box could be rewritten as instruction rather
than alarm: *"You can leave this alone. Race does not affect your estimated GFR…"* It was also
restyled from the red caution palette to the neutral sunken surface, because it is now
guidance rather than a warning. No new hex values.

Headline label became "Your estimated GFR"; "Spread across equations 6.7" became "All four
equations 38.6 – 53.5"; and a line under the results says plainly which row to match against a
blood test.

**This is an addition beyond the reference, made with owner authorisation.** It was raised as
a proposal in the previous completion report per §"Standing rule on scope", and the owner's
instruction to optimise for the visitor is the approval. Parity is untouched: all three
reference equations remain, under their exact reference names, producing identical numbers —
re-swept against the live site, **35 cases, 0 mismatches**.

**Prose reconciliation was the bulk of the work**, exactly as §"if a page's prose describes a
feature that is later removed, the prose has to be rewritten in the same commit" predicts.
Eight places said or implied that the 2021 equation was *not* on the page: two FAQ answers, the
race section's closing paragraph, the limits paragraph, the bottom-grid note, the closing note
under the result, the H1 subhead, and the meta description. A grep for "three equations" after
the edit caught two survivors. All eight fixed in the same commit; the FAQ question itself
became "Why do the four equations give different answers?".

Re-verified: **62 browser assertions, 0 failed** (new ones covering the headline value and
plain-language label, the 2021 row being first and highlighted, and the race box opening with
actionable wording), **45 browser cases against the engine, 0 mismatches**, **35 live-reference
cases on the three original equations, 0 mismatches**, FAQ schema still exact at 8/8, article
originality 0.00% against the reference. Description trimmed back to 153 characters after the
first rewrite came in at 169.

## Healthy Weight Calculator — rebuilt from stub (Aug 8, 2026)

Replaced the 44KB template stub at `/healthy-weight-calculator/` with a full 3-card build
(90KB, `hw-` prefix). Reference: calculator.net/healthy-weight-calculator.html, supplied by
the owner with US and metric screenshots. Donor `tdee-calculator`; protected style block,
header and footer byte-identical afterwards. The simplest page built so far — one input,
height — which made the two constants below the whole of the difficulty.

**Keyword research.** "healthy weight calculator" is held by the NHS, calculator.net and a
long tail of BMI tools. The variants with their own competitor pages are "how much should I
weigh", "healthy weight for height" and "normal weight range", all of which are the same
question phrased as a person would actually type it; they drive the H1 subhead, the result
label and the first FAQ. Title 54 chars, description 143.

### Two things measured off the reference, not assumed

**1. It does not use the 703 shortcut.** The obvious way to get pounds is
`BMI x inches² / 703`. Theirs converts inches to centimetres, works the weight out in
kilograms, and converts to pounds at the end. Brute-forcing every height from 3'0" to 7'11"
across the six BMI boundaries found exactly four inputs where the two routes differ by a
pound; three were put to the reference and it sided with the metric route every time.
6'1" is the cleanest: 703 gives 190 lb at BMI 25, the metric route gives 189, and the
reference says 189.

**2. It squares the centimetres before dividing by 10,000.** `(cm/100)²` and `cm²/10000` are
algebraically identical and one bit apart in a double. At 230 cm the first gives 132.2 kg at
BMI 25 and the second gives 132.3 — the reference says 132.3. Caught by the first 40-case
sweep, on the single tallest input it generated. A spot check at ordinary heights would never
have found it.

Also worth recording: **the lowest boundary is BMI 16.5**, not the WHO severe-thinness cut-off
of 16. Matched for parity, and the page states the actual WHO sub-bands (severe under 16,
moderate 16–17, mild 17–18.5) in a reference card so the number is not passed off as WHO's.

### Verification

Engine swept against the live reference twice — **85 cases, 0 mismatches** — comparing the
healthy-range sentence and all six boundary figures, across US heights 3'0"–7'11" and metric
90–230 cm. Then the shipped page driven in Chromium over **45 fresh cases**, checking the
headline, the six scale ticks and all seven category weight ranges: **0 mismatches, 0 console
errors**. **55 browser assertions, 0 failed**, including explicit regression guards on both
constants (6'1" must read 140–189, and 230 cm must read 132.3).

### Design decisions

The reference renders its scale as a **fixed PNG** with the tick numbers positioned in a
table above it. Ours is built from the same six numbers and seven labels as coloured `<i>`
segments with the boundary figures absolutely positioned on the joins, so it recolours and
relabels live and survives a 390px viewport. Band widths are layout rather than data: on a
true linear axis the healthy band would be a sliver and the top class would run off the page,
so the widths are fixed and that is stated on the page rather than left to look like an axis.

Underneath it, a category table gives every band as a weight range for the entered height —
the same six numbers expanded, which is what a visitor actually wants to read.

Two things were caught by looking at the screenshot rather than by the assertions, both
readability rather than correctness: the full category names were breaking mid-word under the
band ("Severely underwei / ght") at every viewport, so the strip now carries short labels with
the full names in the table below and a `title` attribute on each; and the top band read
"248 and above lbs", now "248 lbs and above".

### Wellbeing

This is the first weight-range page built since the eating-disorder wording was standardised
on `body-type-calculator`, and it follows it: the National Alliance for Eating Disorders
helpline with its number, **not NEDA**, whose line is disconnected. There are no calorie
targets, no diet or exercise plans and no goal weights anywhere on the page — the article
deliberately routes the "what should I do about it" question to waist-to-height, trend over
time and blood markers rather than to a number. Four assertions now enforce this: the helpline
must be named, NEDA must not appear, no calorie or meal-plan language, and the disclaimer must
say plainly that a weight inside the band is not a clean bill of health.

**Content.** 1,983-word article, 8 H2s, 8 FAQs. Overlap with the reference **0.00%** — notable
because the reference's article covers the same ground at length, so the sections were chosen
to attack it from different angles (where the categories came from, what BMI cannot see,
better questions than "what should I weigh"). Against our own pages the worst is 1.77%
(gfr and carbohydrate), which is byline and disclaimer boilerplate, plus 1.06% against
body-type-calculator, which is the shared helpline sentence — deliberately identical wording.

**Also shipped**: OG image at `/og/healthy-weight-calculator.png`, using the page's own
category band with the healthy segment marked rather than the ring the last few pages used.
`calculators-index.json`, `sitemap.xml` and `llms.txt` already carried the slug. calorie,
height and ideal-weight already linked here; reciprocal links added from **body-fat, bmr and
gfr**. bmi-calculator has no standard sidebar anchor and was left alone.

## Lean Body Mass Calculator — rebuilt from stub (Aug 9, 2026)

Replaced the 44KB template stub at `/lean-body-mass-calculator/` with a full 3-card build
(97KB, `lbm-` prefix). Reference: calculator.net/lean-body-mass-calculator.html, supplied by
the owner with US, metric and Other-Units screenshots. Donor `body-fat-calculator`, which
carries the same five-category converter; protected style block, header and footer
byte-identical afterwards.

**Keyword research.** Head term "lean body mass calculator" is held by calculator.net, Omni,
Bodybuilding.com, BodySpec and a long tail of body-composition tools. The variants with their
own competitor pages are "how to calculate lean body mass", "lean body mass formula",
"lean body mass vs fat free mass" and "which formula is most accurate" — the last of these is
the gap worth taking, since competitors mention the disagreement between formulas but almost
none build a title or a section around it. That drives the H1 subhead, the spread line under
the result table and two FAQs. Title 54 chars, description 151.

Note for future pages: most competitors take the *body-fat-percentage* route
(LBM = weight x (1 - BF%/100)). The reference does not, and per the scope rule that route was
not added. It is covered in an FAQ instead, which says plainly that a measured body-fat
percentage beats any formula here.

### The constant took four wrong answers to pin down

Their US-mode figures depend on how pounds convert to kilograms and back, and this page does
**not** use the factor recorded in the guide for BMR/body-fat (`0.453592`). Four hypotheses
each passed a sweep and then failed on fresh cases: `0.453592`, then `0.45359237`, then
`0.45359` paired with `2.20462`, then `1/2.20462`. Every failure was the same shape — our
value 0.1 higher than theirs, at a rounding boundary — which is easy to dismiss as float noise
and is not.

Guessing was the wrong method. What settled it was **measuring**: hold height fixed and binary-
search the weight at which the printed answer steps by 0.1 lb. The steps land **0.2457002 lb**
apart, and that spacing plus the absolute position of one step gives the constant directly.
The answer is a **single hard-coded 2.2046**, divided going into kilograms and multiplied
coming back — not two independent constants, which is what every failed hypothesis assumed.
An LP over 344 bounded observations had said "feasible" for several pairs, because a bounding
box on the marginals is a superset of the actual polytope; that check was misleading and the
flip-point measurement is the one to reach for next time.

Also read off the reference rather than assumed: inch-to-cm is 2.54; the percentage is
`round(LBM/weight x 100)` with body fat as `100 - that`; figures at or past 1,000 carry a
comma separator; empty or zero inputs render no result block at all; and there is no clamping,
so implausible inputs produce negative lean mass and body fat over 100%.

### The row the screenshots do not show

Answering **yes** to "Age 14 or younger" adds a **Peters (for Children)** row at the *top* of
the table, followed by a blank spacer row, then Boer/James/Hume. All three supplied screenshots
have "no" selected, so a screenshot-led build would have shipped without it. Caught by probing
the live page across the age radio — the same failure mode as the Inflation Calculator's
missing table, in the opposite direction.

One judgement call on top of parity: the result card's headline features **Peters** when the
age answer is yes, and Boer otherwise. The reference has no headline at all — it is a bare
table — so this is our design system choosing which existing row to feature, not a new figure.
Showing Boer for a child while the article says Peters is the applicable formula would have
been actively misleading. Caught from the screenshot, not the assertions.

### Verification

Engine swept against the live reference: **1,060 cached-case field comparisons + 250 fresh
random cases + 150 extreme-range cases, 0 mismatches**, covering both unit systems, both sexes,
the child formula, negative results and comma-formatted thousands. Then the shipped page driven
in Chromium over **45 fresh cases**, comparing every emitted figure — LBM value, percentage of
body weight and body fat percentage, for every row: **0 mismatches, 0 console errors**.
**64 browser assertions, 0 failed**, including regression guards on the constant, on Clear
emptying boxes without moving the page (0.0px drift), on jsPDF staying unloaded until clicked,
and on the converter's unit counts (Length 11, Temperature 3, Area 11, Volume 23, Weight 10,
Acre and all six Imperial volume units present).

A 32px horizontal overflow at 390px and 430px turned out to be a `file://` artifact — the
Tailwind chunk 404s off a filesystem path. Over `python3 -m http.server` it is 0. **Test over
HTTP, not `file://`**; the two remaining console errors are the sandbox having no CA for
Google Fonts and gtag.

### Content

2,051-word article, 8 H2s, 7 FAQs. FAQ schema is **generated from the rendered article at
build time** rather than typed alongside it, which removes the em-dash/quote drift failure the
guide records against four earlier pages — the equality check passes by construction.
Overlap with the reference **0.05%** (one unavoidable phrase, the topic name itself) and worst
against our own pages **0.05%** (ideal-weight and gfr). The disclaimer and limitations sections
were written from scratch per the sibling-originality rule, and the article's angle — why four
formulas exist, how to read a spread rather than a number, who actually uses LBM (drug dosing,
CT contrast) — deliberately avoids the reference's own structure.

**Also shipped**: OG image at `/og/lean-body-mass-calculator.png`. `calculators-index.json`,
`sitemap.xml` and `llms.txt` already carried the slug. Nine pages already linked here; a
reciprocal link was added from **army-body-fat**. `bmi-calculator`'s sidebar uses a different
anchor convention and was left alone, consistent with the healthy-weight session's decision.

### Open question for the owner

The reference does not clamp, so extreme inputs print things like "-292.0 kg lean body mass,
246% body fat". The numbers are matched exactly for parity. Whether the result card should
carry a short caution line when body fat falls outside 0-100% was **put to the owner before
building and not answered**, so per the scope rule nothing was added; the limitation is covered
in the article's "What this calculator cannot see" section instead. Easy to add later if wanted.

### Article styling corrected after owner review (Aug 9, 2026)

Shipped first with a hand-written article stylesheet instead of the site's. The owner sent a
screenshot: the byline was rendering in **IBM Plex Mono at body size, with no rule under it**,
which no other page does. Three things were wrong and all three are now taken verbatim from
`healthy-weight-calculator`, prefix-renamed:

- **Byline** was mono with no bottom border. House style is 12.5px body font, `--ink-faint`,
  `padding-bottom:16px`, and a `--border-fine` rule beneath.
- **Body copy** was 14.5px/1.72 with a 12px gap. House is **15px/1.75, margin-bottom 14px**.
- **Table of contents** was a horizontal row of green chips on `--surface-sunken` with a
  "On this page" span heading. House is a **white card with block-level 13.5px `--ink-soft`
  links**, no heading span, and the label lives in `aria-label` only.

Also added the missing **`.lbm-formula2` box**: the site has a standard mono equation panel
(surface-sunken, 1px border, 10px radius, `<b>` as an uppercase body-font label) and the article
had no formula display at all, which section 2 of the guide asks for. All four equations plus
the two unit conversions now sit in one, inside "Why four formulas, not one".

Verified the fix by **diffing the article stylesheet against healthy-weight's with the prefix
normalised — string-identical** — and by comparing computed styles across four pages in
Chromium, which now agree on every property checked.

**Pre-existing site-wide quirk found while doing this, not introduced here and not fixed here:**
`.X-byline` and `.X-disclaimer` both ask for `font-size:12.5px`, but `.X-seo-article p` is
`(0,1,1)` specificity against the class's `(0,1,0)`, so **both render at 15px on every page on
the site** — healthy-weight, body-fat and tdee all measure 15px too. Our page now matches that
behaviour exactly, which is the right call for consistency. Fixing it properly means either
scoping the rule (`.X-seo-article p.X-byline`) or reordering with equal specificity, applied
**site-wide in one pass** — doing it on one page would make that page the odd one out again.
Worth raising with the owner as its own task rather than folding into a calculator build.

Lesson for the next build: **lift the article stylesheet from a recent page rather than
authoring one.** The 3-card grid CSS was correctly copied from the donor; the article CSS was
written fresh and drifted, and a screenshot caught what no assertion was checking.

### Monospace removed from the bottomgrid cards (Aug 9, 2026, second styling correction)

The owner flagged the two bottomgrid cards as reading oddly. They were right, and it was the
same class of mistake as the article stylesheet: **mono used somewhere the site does not use
it.** Audited five built pages — healthy-weight, body-fat, tdee, gfr, carbohydrate — and
`var(--f-mono)` appears in exactly **one** place on each: the article's `.X-formula2` equation
panel. Nothing in a bottomgrid card uses it; those follow `.X-ref-table` at 12.5px and
`.X-note` at 11.5px, both body font.

`.lbm-work` (the step-by-step card) and `.lbm-fdef code` (the formula glossary chips) were both
mono and are now IBM Plex Sans at 13px and 12.5px. The article formula box keeps mono, which is
correct. Verified with a **computed-style sweep over every leaf element in `<main>`**: the only
nodes still resolving to a mono family are the `<br>` and `<sup>` children inside
`.lbm-formula2`, which is the one place it belongs.

Two follow-ons caught by looking at the render rather than the DOM:
- Peters was written `W^0.6469` in caret notation while the article box used real superscripts.
  Converted to `<sup>` for consistency — which then **broke out of the chip's tinted
  background**, because `vertical-align:super` on a tight inline box paints the raised text
  outside it. Fixed by making the chip `inline-block` with `line-height:1.35` and offsetting the
  sup with `position:relative;top:-.42em;line-height:0` so the line box does not grow. Asserted
  geometrically afterwards (`sup.top >= chip.top && sup.bottom <= chip.bottom`) rather than by eye.
- Chip padding trimmed to `3px 6px`; at `1px 6px` the right padding read as a stray space before
  the following comma.

**Running note across both corrections:** every styling defect on this page was invisible to the
64-assertion suite and visible in a screenshot. The suite checks behaviour and geometry, not
whether the page looks like the rest of the site. Worth adding a cheap guard to future builds:
a computed-style comparison of `.X-byline`, `.X-seo-article p`, `.X-toc a` and any mono usage
against a named reference page, which would have caught both of these before shipping.

## One Rep Max Calculator — rebuilt from stub (Aug 9, 2026)

Replaced the stub at `/one-rep-max-calculator/` with a full 3-card build (86KB, `orm-` prefix).
Reference: calculator.net/one-rep-max-calculator.html. Donor `body-fat-calculator` for shell;
article stylesheet lifted from `healthy-weight-calculator` per the lesson logged above and
verified string-identical after prefix normalisation.

**No tabs on this page.** The reference has a unit dropdown and a "+ Settings" disclosure, not
unit tabs, so none were added — parity is a ceiling. Grid areas are `bar / form result sidebar /
bottomgrid`, no tabs row.

**Keyword research.** "one rep max calculator" and "1RM calculator" are crowded (Omni, arvo,
hypro, hubfit, coachway, ajdesigner). Nearly every competitor shows two to four formulas *side
by side* and offers an average; the reference does not, and per the scope rule neither do we.
The gap worth taking is the pair of tables the competitors mostly skip — weight for each rep
count, and the inverse percentage table — plus explaining the ten-rep cap, which competitors who
allow 1-12 never justify. Title 50 chars, description 152.

### Four separate arithmetic traps, none of them guessable

A 40-case sweep opened at **51 mismatched blocks**. Each cause was distinct:

1. **Rep 1 is special-cased.** Epley at r=1 would give w x (1 + 1/30) = 1.033w. The reference
   returns w. Sensible — if you lifted it once, that is the max — but it is a branch, not a formula.
2. **Algebraically identical, not identical in floating point.** Epley's row share written as
   `1/(1 + n/30)` lands a hair under 0.625 at n=18 and rounds to 62%; written as `30/(30 + n)`
   it is exactly 0.625 and rounds to 63%, which is what the reference shows. Same for the reverse
   table: `30*(1/p - 1)` gives 9.999999 at 75% and floors to 9, while `3000/p - 30` gives exactly
   10. **Integer-first arithmetic, every time.**
3. **Lombardi's reverse column uses `exp(log(100/p)/0.10)`, not `pow(p, -10)`.** Both are the same
   mathematically. The reference prints **1023** at 50% where the clean form gives exactly 1024 —
   dividing by 0.10 leaves the error that flooring then exposes. That single displayed digit is
   the only evidence of which form the reference uses.
4. **PHP's `round()` pre-corrects to 15 significant digits before rounding half away from zero.**
   138.55 is stored as 138.5499..., so a naive implementation rounds it down and drifts. The
   correction has to be applied **after** scaling by the decimal factor, not before.

### The conversion constant is per-page, again

The lean-body-mass page uses **2.2046**. This page does not, and it is not the true kg/lb factor
(2.20462262) either. Interval analysis over every cross-unit row gave a feasible band of
**[2.2046243, 2.2046245]**, and a grid scan confirmed zero mismatches only inside it:
**2.2046244**. Two pages, two different hard-coded constants, neither of them correct physics.

Repeat of the LBM lesson, and it bit again here: an initial 31-case fit reported **0/496 for
three different constants**, because none of the 31 cases discriminated. The failures only
appeared once known-failing cases were added to the fit set. **A fit that reports zero on a set
that does not discriminate is not evidence.**

### Verification

Engine against the live reference: **150 normal + 120 extreme-range cases, 0 mismatched**, each
case comparing four blocks — the 1RM headline, the 15-row rep table, the 11-row percentage table
and all 20 chart bars. Then the shipped page driven in Chromium over **40 fresh cases** comparing
every rendered cell: **0 mismatches, 64 assertions, 0 failed**, including the six validation
paths (zero/blank weight, zero reps, reps above ten, fractional reps, non-numeric reps), Clear
emptying only the two typed boxes while leaving unit, formula and the open Settings panel alone
at 0.0px drift, jsPDF unloaded until clicked, and 20 chart bars with per-bar tooltips.

Chart is hand-drawn SVG rather than a library — no dependency, and it inherits the site palette.

### Content

2,145-word article, 8 H2s, 7 FAQs, FAQ schema generated from the rendered article at build time.
Overlap **0.00%** with the reference and worst **0.76%** against our own pages — that 0.76% is
almost entirely the shared byline template line, with the next-highest real overlap at 0.10%.
Article carries the house `.orm-formula2` box with all three equations and a worked example.
OG image added; slug was already in `sitemap.xml`, `calculators-index.json` and `llms.txt`.

### Settings disclosure switched to the house More Options pattern (Aug 9, 2026)

Shipped with a bespoke "+ Settings" toggle — transparent background, navy text, inline
`style.display`. The owner asked for the mortgage calculator's treatment instead. Checked before
changing anything: **six pages already share one pattern** — bmr, carbohydrate, due-date,
ideal-weight, macro and mortgage all carry the identical black `#131313` full-width button. This
page was the only one doing something else.

Now matched exactly, verified by extracting each rule and comparing against `macro-calculator`:
`.orm-more-btn`, `.orm-hidden` and `.orm-section-title` are all rule-identical after prefix
normalisation. Markup switched from an inline-styled div to `class="orm-hidden"`, section labels
from a bespoke `.lbl` to `.orm-section-title`, and the toggle from a `style.display` flip to
`classList.toggle`, with the house labels **"+ More Options" / "- Fewer Options"**.

One thing worth recording: the regression suite reported `[settings] collapses=False` after the
change and **that was the assertion being wrong, not the page** — it still probed
`style.display === "none"`, which no longer applies once the panel is class-driven. Manually
driving the toggle in the browser showed it working correctly. The assertion was rewritten to
test `classList.contains('orm-hidden')`, i.e. the mechanism actually in use. A test that checks
the old implementation rather than the behaviour will pass or fail for the wrong reasons; worth
re-reading assertions whenever the mechanism under them changes.

Full suite re-run afterwards: 64 assertions, 40 engine cases, 0 mismatches, overflow 0 at 1280,
430 and 390px. No calculation changed.

## Ovulation Calculator — rebuilt from stub (Aug 9, 2026)

Replaced the stub at `/ovulation-calculator/` with a full 3-card build (73KB, `ovu-` prefix).
Reference: calculator.net/ovulation-calculator.html. Article stylesheet lifted from
`healthy-weight-calculator` and verified string-identical after prefix normalisation.

**No Clear button.** The reference form carries only Calculate. Buttons are parity, so none was
added. No tabs either.

### Finding the input names cost the first three probes

The date field is rendered by `DateInput('today', true)` from `calendardateinput.js`, and the
first probes with `cmonth/cday/cyear` came back looking plausible — because those params were
silently ignored and the page fell back to today's date, which happened to be the date I was
testing. The cycle param worked, so results changed and nothing looked broken. Reading the
script showed it writes **one hidden field named after its first argument**, so the real
parameter is `today=MM/DD/YYYY`. **A probe that "works" because the default matches your test
input is a false positive** — vary the input you are trying to confirm, not just the other one.

### The rules

    ovulation = LMP + (cycle - 14)          i.e. fourteen days before the next period
    next period = LMP + cycle
    ovulation window = ovulation +/- 2 days
    intercourse window = ovulation - 5 to ovulation + 2
    pregnancy test = ovulation + 9
    due date = ovulation + 266
    next six cycles = the same, from LMP + cycle*k for k = 0..5

The luteal phase is the fixed part, so cycle length is added *before* ovulation, not after.

### Two things I nearly got wrong in opposite directions

**A reference "bug" that was my parser.** When the fertile window straddles a month, the
reference renders **two calendars** (e.g. February 2027 and March 2027). My regex read both
grids as one, so it looked like the reference was highlighting day 1 of February when the
window was Feb 25 to Mar 1. I was one step from "fixing" a bug that did not exist. Checking the
raw markup first is what caught it.

**A real reference bug that looked like noise.** At LMP 30 Jan 2100 with a 44-day cycle the
reference's February grid renders a **29th**. 2100 is not a leap year — divisible by 100, not by
400 — so the calendar is using a naive `year % 4` rule. The text dates are correct (Feb 27 to
Mar 3); only the grid invents the day. Per the standing rule the field is matched and the error
is not: our calendar comes from `new Date(y, m+1, 0)`, which applies the full century rule, and
there is a regression assertion pinning February 2100 to 28 days. Practically irrelevant, but
correctness here was free.

### Verification

Engine against the live reference: **30 + 120 normal + 100 edge cases** biased toward month
ends, Februaries and leap years, each comparing three blocks (the six this-cycle dates, all six
projection rows, and every calendar with its highlighted days) — **0 mismatched**, the sole
known divergence being the 2100 leap bug above. Then the shipped page driven in Chromium over
**35 fresh cases** comparing every rendered cell: **0 mismatches, 51 assertions, 0 failed**,
including the day list rebuilding for short months (Feb 2027 = 28, Feb 2028 = 29, Jan = 31),
the 22-44 cycle range, the absent Clear button, year validation, and 0 overflow at three widths.

### Content, and a sibling-originality catch

1,901-word article, 8 H2s, 7 FAQs, FAQ schema generated from the rendered article. Overlap with
the reference **0.00%**.

The first draft scored **0.67% against our own `conception-calculator`** — and unlike the
byline-only overlaps against other pages, that one was **real prose**: cervical mucus, the LH
surge, false negatives. Both pages cover the same fertile-window territory, so re-wording would
only have hidden the duplication. Instead the whole "signs to track" section was **cut and
replaced** with material the sibling does not cover — how confidence decays across the six
projected cycles and how to plan around a range rather than a printed date — with a link handing
body-signs readers to the conception calculator. Real overlap is now **3 shingles**, all of them
the formula itself and the standard definition of cycle length, which should not be reworded.

**YMYL treatment.** The reference's own warning is that it must not be used as birth control.
That is the first H2 on our page rather than a footnote, the result card carries a short line
saying the same, and the disclaimer names the situations where the arithmetic does not apply.
OG image added; slug already present in `sitemap.xml`, `calculators-index.json` and `llms.txt`.

## Period Calculator — rebuilt from stub (Aug 9, 2026)

Replaced the stub at `/period-calculator/` with a full 3-card build (74KB, `per-` prefix).
Reference: calculator.net/period-calculator.html. Closest sibling yet to a page we had just
shipped, and that turned out to be the main risk on this build — see the originality note below.

**Inputs 6/6, results 11/11.** Same date widget and `ccycle` as the ovulation page plus
`clength` (1-10 days, default 5). No Clear button and no tabs, matching the reference.

### The calendar logic came from their own client-side JS

Unlike the tables, the reference's calendar is rendered in the browser, so the page ships the
rules in plain sight:

    isPeriod(d):    ((d - LMP) mod cycle) < periodLength
    isOvulation(d): ((d - LMP - (cycle - 16)) mod cycle) < 5

with negatives folded back into range, which is why months *before* the entered date shade
correctly too. Period wins over ovulation when a day satisfies both. The five ovulation days are
the same window the ovulation calculator draws: `cycle-16` to `cycle-12` is ovulation +/- 2.
They build dates at **11:00 rather than midnight** — a daylight-saving guard, since a date-only
value can cross a DST boundary and drag a whole month's shading with it. Worth copying, and
copied.

`showMonth` also carries **the same naive `smYear % 4` leap rule as the ovulation page**, so
February 2100 renders a 29th there too. Field matched, error not: ours uses `new Date(y, m+1, 0)`
and there is an assertion pinning February 2100 to 28 days.

### A real bug the suite caught, that manual clicking did not

The suite reported "Previous 3 months" doing nothing while "Next" worked, which made no sense
from the code. Clicking it by hand worked fine. The difference was timing: the shared auto-run
fires a few hundred milliseconds after an input changes, `calculate()` reset the calendar view
to the entered month, and in the suite the click landed inside that window. **Anyone who changed
a cycle length and then paged the calendar would have been yanked back.**

Fixed by anchoring the view: `calculate()` now only resets the visible quarter when the entered
month itself changes, and leaves it alone otherwise. Verified all three ways &mdash; navigation
survives a pending auto-run, survives a cycle-length change, and still jumps when the LMP month
changes. Note the sequence here: the suite looked wrong, hand-testing looked right, and the suite
was correct. Checking which one is lying beats trusting either.

### Verification

Engine against the live reference: **35 + 120 + 90 edge-heavy cases** (month ends, Februaries,
year rollovers, period length 1 and 10, cycle 22 and 44) comparing the six-row table and the JS
constants the calendar is driven by &mdash; **0 mismatched**. Then in Chromium over **35 fresh
cases**, comparing the table *and the shading of every visible day across all three calendars*
against an independent port of the classifier: **0 mismatches, 91 assertions, 0 failed**,
including backward shading, three-month paging in both directions, the leap guard, the day list
rebuilding for short months, and 0 overflow at three widths.

### Originality: the closest call so far

First draft scored **2.86% against our own ovulation calculator, 39 real shingles** &mdash; by far
the highest yet, and all of it my own safety and irregularity framing repeated from a page I had
written hours earlier. Five passages were rewritten rather than reworded: the irregular-cycle
advice now hangs on the shortest-to-longest *spread* rather than "run it twice", the limits
section leads on why an interval stops existing, and the disclaimer was recentred on menstrual
health (heavy bleeding, bleeding between periods, post-menopausal bleeding) instead of mirroring
the contraception-first framing of the ovulation page.

Now **1.43%, 13 real shingles**, and those are the domain's fixed vocabulary — the definition of
cycle length and "count from the first day of proper bleeding, not from spotting". Any correct
explanation converges on those; rewording them would make the page worse.

**Lesson worth keeping:** the sibling-originality check needs to run against *recently built*
pages specifically, not just the corpus. The risk is not copying calculator.net, which scored
0.11% here — it is repeating yourself across two adjacent topics in the same week.

The article deliberately avoids the fertile-window mechanics, cervical mucus, LH and BBT that
the ovulation and conception pages already cover, and links out for them instead. Its own
territory is period-specific: the two lengths people confuse, what "regular" means numerically,
why later rows drift, using backward navigation to fit your own cycle length, and the bleeding
changes that warrant a doctor. OG image added; slug already in all three registry files.

## Pregnancy Conception Calculator — rebuilt from stub (Aug 9, 2026)

Replaced the stub at `/pregnancy-conception-calculator/` with a full 3-card build (78KB,
`pcc-` prefix). Reference: calculator.net/pregnancy-conception-calculator.html.
**Inputs 8/8, results 12/12.** Three input modes behind one "Calculate based on" select, no
Clear button and no tabs, matching the reference.

### All three modes collapse to one date

Due date, last period and ultrasound are three doors into the same arithmetic. Each produces a
notional last menstrual period, and everything after that is identical:

    due date   -> LMP = due - 280            (cycle fixed at 28)
    last period-> LMP as entered             (cycle 22-44, default 28)
    ultrasound -> LMP = scan - (weeks*7+days) (cycle fixed at 28)

    base = LMP + (cycle - 14)
    most probable conception  = base-2 .. base+2      possible = base-3 .. base+7
    most probable intercourse = base-5 .. base+2      possible = base-8 .. base+7

The intercourse ranges are the conception ranges opened 3 and 5 days earlier for sperm survival,
which is exactly the 3-5 days the reference's own intro paragraph cites. The possible range is
deliberately asymmetric — seven days forward against three back — because late ovulation is more
common than early.

### I was stricter than the reference, which is also a parity break

The first build validated the ultrasound inputs sensibly: reject a day count above six, reject a
gestational age of zero. Probing the reference showed it does neither. `12 weeks 9 days` is
accepted and simply added as 93 days; `0 weeks 0 days` computes; a blank box counts as zero.
Only a negative or non-numeric entry stops it.

So six inputs the reference happily answers were returning an error on our page. **Being stricter
than the reference is still a parity break** — the rule is not "don't be looser", it is "match
the fields". Validation now matches exactly, verified against the reference's own output on all
six cases plus the two it does reject. Worth remembering: the instinct to tidy up sloppy input
handling is the same instinct that quietly changes behaviour.

### Verification

Engine against the live reference: **40 + 120 + 90 edge-heavy cases** across all three modes
(month ends, Februaries, leap years, gestational ages from 1 to 42 weeks, cycles 22 and 44) —
**0 mismatched**. Then in Chromium over **36 fresh cases** spanning the three modes, comparing
all four rendered ranges: **0 mismatches, 59 assertions, 0 failed**, including mode switching
showing exactly one pane, the six ultrasound edge cases above, per-picker day lists rebuilding
for short months, and 0 overflow at three widths. The reference's own default (due date
7 Dec 2026) reproduces exactly: 14-18 Mar, 11-18 Mar, 13-23 Mar, 8-23 Mar.

### Originality: best sibling result so far, because it was planned first

Five close neighbours already exist — conception, ovulation, period, due-date and pregnancy.
Rather than write and then measure, this time I **read the sibling H2 lists before drafting** and
deliberately took the ground none of them held: that this is a backwards calculation and
reversing a calculation widens uncertainty rather than narrowing it; which of the three routes to
trust when you have more than one; the two-week offset that makes an eight-week pregnancy a
six-week embryo; and the paternity question, which is a large share of the search intent for this
exact page and which the neighbours never touch.

Result: **0.00% against the reference** and, against our own pages, a single real shingle
("pregnancy is counted from the first day of") with the pregnancy calculator. Everything else was
byline boilerplate. Compare the period calculator two builds ago, which needed five passages
rewritten after the fact — planning the scope beforehand was much cheaper than repairing it.

**On paternity specifically:** the page says plainly that it cannot settle it, that a sixteen-day
possible window cannot separate two dates inside it, that a date outside the narrow range is less
likely rather than excluded, and that DNA testing — prenatal from around week eight or nine, or
after birth — is the route to an actual answer. The disclaimer states it cannot establish a date
for legal, immigration or paternity purposes. Given who searches this term, that felt like the
part worth getting right.

OG image added; slug already in all three registry files.

## Target Heart Rate Calculator — rebuilt from stub (Aug 9, 2026)

Replaced the stub at `/target-heart-rate-calculator/` with a full 3-card build (82KB, `thr-`
prefix). Reference: calculator.net/target-heart-rate-calculator.html. **Inputs 14/14, results
12/12.** The most branching page built so far: two max-heart-rate modes, three estimation
formulas, three intensity scales, and an optional resting rate — which together produce **four
different result tables**, not one.

### The four output shapes

    resting rate given + Karvonen  -> 5 zones, % of heart rate reserve
    resting rate given + Borg      -> 10 rows, RPE 6-20  -> bpm
    resting rate given + CR10      -> 10 rows, CR10 0-10 -> bpm
    resting rate blank             -> 5 zones, plain % of maximum

The last one is the catch: **a blank resting rate overrides the intensity scale entirely.** Pick
Borg, leave resting blank, and the reference silently returns the percentage-of-maximum table,
because every perceived-exertion scale needs a reserve to work from. Easy to miss, and it would
have shipped as a broken-looking scale selector.

    MHR: Haskell & Fox 220 - age | Tanaka 208 - 0.7*age | Nes 211 - 0.64*age
    reserve   = MHR - RHR
    Karvonen  = RHR + reserve * pct
    Borg      = RHR + reserve * (B - 6) / 14      (B = 0 returns RHR)
    Borg CR10 = RHR + reserve * B / 10

### The maximum is rounded before anything else uses it

First sweep opened at 9 mismatches, all a single beat low, all on Tanaka or Nes. Haskell never
failed because 220 minus an integer age is already whole. The cause: **the reference rounds the
estimated maximum to a whole beat before deriving anything from it.** Tanaka at 36 is 182.8; keep
it and every zone lands a beat low, round it to 183 first and all five rows plus the summary line
snap into place. A tenth of a beat, propagated through five zones.

### Validation bounds were measured, not guessed

Binary-searched against the reference rather than assumed: **age 1-119, resting 11-399, tested
maximum 31-499**, with three distinct error messages. Anything outside returns no result at all.
The extreme sweep found these by failing on absurd inputs, which is exactly what it is for.

### Verification

Engine against the live reference: **30 + 120 + 40 + 110 cases** spanning both modes, all three
formulas, all three scales, blank and populated resting rates, and out-of-range inputs —
**0 mismatched**, covering all four table shapes and all three error paths. Then in Chromium over
**45 fresh cases**: **0 mismatches, 74 assertions, 0 failed**. The reference's own default
(age 30, resting 70, Haskell, Karvonen) reproduces exactly: 130-172 bpm and all five rows.

### Two of my own bugs, and which one the suite could see

**A real layout bug the suite caught:** 44px of horizontal overflow at 390px. The zone table's
`th` cells carried `white-space:nowrap`, giving the table a 376px minimum, and `.thr-result-body`
had no `overflow-x`, so the whole grid was pushed to 418px inside a 390px viewport. Headers now
wrap, the result body scrolls if it must, and overflow is 0 at 1280, 430, 390 and 360.

**A real styling bug the suite could not:** the step-by-step card rendered as one unbroken run of
text — "Maximum heart rate220 - 34 = 186 bpmHeart rate reserve186 -". The `.thr-work` rules had
been dropped somewhere in the CSS chain from build to build, so the `.nm` labels were inline
instead of block. Every assertion passed; the screenshot showed it immediately. **Fifth build
running where a screenshot caught what 74 assertions did not.**

Also fixed a **stale check in build.py**: the self-link test had been comparing against a
hard-coded slug carried over through three page builds, so it was checking the wrong page and
reported a false positive here. It now derives the slug from the output path.

### Content

1,953-word article, 8 H2s, 7 FAQs. Overlap with the reference **0.00%** and, against our own
pages, **zero real shingles** — the only matches sitewide are the byline and disclaimer
boilerplate. Best originality result to date. Its territory is the reserve-versus-maximum gap
(19 beats at 70% for the worked example), choosing between the three formulas and what their
spread means, what each zone is for, when perceived exertion beats the monitor, and the reasons
a heart rate reads high on a given day.

**YMYL treatment:** a dedicated section on when to stop and ask a doctor, naming the symptoms
that override any target, plus the beta-blocker case where these numbers do not apply at all —
that one gets its own FAQ as well as a line in the disclaimer.

OG image added; slug already in all three registry files.

## Shoe Size Conversion — IN PROGRESS, NOT SHIPPED (Aug 9, 2026)

`/shoe-size-conversion/` is **still the 44KB stub**. Nothing was pushed to the page. This entry
exists so the next session does not have to re-derive several hours of probing. The verified
engine is saved at `notes/shoe-size-sweep.py` and currently runs **320+ cases against the live
reference with 0 mismatches**, with the open items listed at the end.

Category note: this one is **Other**, not Health & Fitness, and the slug has **no `-calculator`
suffix**. It is already present in `calculators-index.json`, `sitemap.xml` and `llms.txt`.

### Inputs

`ac` (a / k / i), then seven fields any one of which can be the source: `usw`, `usm`, `uk`,
`eu`, `jp`, `cn`, `fl` + `flu` (cm/mm/in). Convert and Clear both present.

**Precedence is form order** — usw > usm > uk > eu > jp > cn > fl. Fill several, the first wins.

Labels and ranges are rewritten per age group by `sscac()`: kids hide the women's row entirely
and relabel to "US/Canada kids" / "UK/India kids"; infants relabel to
"US/Canada babies" / "UK/India babies" in the form, but the **results** table says
"US/Canada infants/toddlers".

### The formulas are not the ones the page prints

The article text states big kid = 3L - 22½, little kid = 3L - 9½, UK 23½ and 10½.
**The calculator uses quarters, not halves.** Inverting size to foot length across the whole
scale gives:

    adults   US women 3L - 21 | US men 3L - 22 | UK 3L - 23
    kids     US big 3L - 22.75 | US little 3L - 9.75
             UK big 3L - 23.75 | UK little 3L - 10.75
    infants  US 3L - 9.75 | UK 3L - 10.75      (little-kid constants)
    all      EU = 1.5*Lcm + 2 | JP = Lcm | CN = 2*Lcm - 10

L is inches for US/UK, centimetres for EU/JP/CN. US/UK/JP round to the nearest half, EU/CN to
the nearest whole. Verified by checking size -> foot length against the reference: US kids 3
gives 21.8 cm, which is 3L - 22.75, not 3L - 22.5 (that would be 21.6).

**The kid scale wraps**, and which branch applies differs by direction:
- computing a size *from* a length: use big-kid if it comes out >= 1, otherwise little-kid
- reading a size *as input*: use big-kid only while it is inside that scale's range
  (US <= 7, UK <= 6), otherwise little-kid

That second rule cost a while. `uk = 6.5` is not a big-kid 6.5; the reference reads it as
little-kid, giving a 5.75 inch foot rather than a 10.08 inch one.

### "out of scope" is per field, and asymmetric

    adults  US women / US men / UK   out of scope below 1; no ceiling (17.5 and 51 both print)
    kids    US  ceiling 7 on the big branch, 13.5 on the little branch
            UK  ceiling 6 on the big branch, 13.5 on the little branch
            no floor at all - it will happily print "-0"
    infants US / UK  floor 0, ceiling 13.5
    China   out of scope below 5
    EU, JP  never out of scope

Negative zero is real: the reference prints **"-0"**, so the rounding helper has to preserve the
sign through `copysign`.

### Other reference behaviour already pinned

- **The source row is dropped from the results table — except UK in adult mode**, where it is
  kept. That exception does *not* apply to kids or infants. Inconsistent; reproduced for parity.
- **No round-tripping.** Foot length must be carried in both units natively. Computing cm as
  inches x 2.54 turns a China size 11.5 (10.75 cm exactly) into 10.749999, which drops
  Japan/Mexico by a half size.
- Decimal display rounds **half up**, not banker's: 13.25 cm prints as 13.3.
- Foot length always prints all three units: `X.X inches  X.X cm  XXX mm`.

### Open items before this can be built

Source values are rejected outright (no result at all) below per-field minimums that are still
being mapped. Confirmed so far: `jp` accepts 6 and rejects 5.5; `cn` accepts 4 and rejects 2;
`fl` accepts 2 inches and rejects 1.5; `eu` accepts 10 and rejects 0; `usw` accepts 0. Kids and
infants also reject any `usm`/`uk` above 13.5. These are per-field constants rather than one
length threshold — `cn = 2` and `jp = 6` both imply a 6 cm foot, and one is rejected while the
other is not, so it is not a foot-length rule.

**Why this stopped here rather than shipping:** the remaining gaps only affect absurd inputs, but
the engine is the part that has to be right, and the session ran out of room to build the page,
write the article, run the browser suite and check originality against 200+ existing pages. A
page shipped without those is exactly the failure mode the one-at-a-time approach exists to
avoid. Resume by finishing the source-minimum map, then building normally.

### Shoe Size Conversion — page built and shipped (Aug 9, 2026)

The engine research recorded in the previous entry is now a live page (79KB, `ssc-` prefix).
**Inputs 13/13, results 14/14.** First page in the Other category rather than Health, so the
breadcrumb, schema `applicationCategory` and related-calculator list all differ from the recent
run of health builds.

**Reused rather than rewritten.** Starting this build I began writing a fresh sweep and hit
"file already exists" — a `shoe_sweep.py` from the earlier session was still on disk, out of my
context. I read it before touching it, and it was **better than what I was writing**: it handles
negative zero (the reference prints "-0" for absurd inputs) and computes metric entries natively
instead of round-tripping through inches, where 10.75 cm comes back as 10.749999 and shifts a
half size. Kept it, and it passed 25 fresh cases immediately. Overwriting unread would have cost
both fixes.

**Verification.** The shipped JS is a direct port of that engine, driven in Chromium over
**45 fresh cases** across all three age groups and all seven entry points, compared against the
Python engine: **0 mismatches, 71 assertions, 0 failed**. The reference's own default (10 inches,
adults) reproduces exactly — 9 / 8 / 7 / 40 / 25.5 / 41. Overflow 0 at 1280, 430, 390 and 360.

**A false alarm worth recording.** The Clear assertion reported 18px of page drift. Chasing it:
no element's height changed across the click, and the h1 moved by the same 18px as the button —
a layout change inside the form cannot move the h1. The 18px was exactly how far the button sat
below the 900px viewport, so it was the browser's native focus-scroll on a clipped button. Also
learned in the process that **`body` on this site carries `overflow: hidden auto`, so `body` is
the scroll container, not `window`** — which is why `window.scrollY` and `window.scrollTo` read
and moved nothing in my probes. The assertion now measures against the document via `offsetTop`,
which is immune to scrolling, and reports 0.0px. Worth reusing on other pages, where the same
measurement has been quietly viewport-relative all along.

**Content.** 1,801-word article, 8 H2s, 7 FAQs. Overlap with the reference **0.00%**; against our
own pages, two shingles of a common phrase. Its territory is why no standard exists, what each
country's number physically counts (the barleycorn behind the three-per-inch US and UK steps),
measuring a foot properly, why round-tripping a conversion does not return you, the children's
restart at 13, and why length alone cannot decide fit. OG image added; slug already in all three
registry files.

## Protein Calculator — rebuilt from stub (Aug 9, 2026)

Replaced the stub at `/protein-calculator/` with a full 3-card build (88KB, `pro-` prefix).
Reference: calculator.net/protein-calculator.html. **Inputs 18/18, results 12/12** — three unit
tabs including the shared Other Units converter, six activity levels, and a Settings disclosure
carrying the BMR formula choice and a body-fat field for Katch-McArdle.

### The one digit the whole CDC band hangs on

Hand-fitting got ADA and WHO immediately (1.0-1.8 and 0.83 g/kg) but the CDC figures came out
about 2% high every time, and no plausible BMR or activity change closed the gap. Rather than
keep guessing, I probed eighteen points varying weight, age, height, sex and activity and solved
for the implied constant. It came back at **4.09 to 4.11 across every single point**: protein is
being counted at **4.1 kcal per gram, not 4**. With 4.0 the default reads 59-207 instead of
58-202. One digit, every figure in the band.

    BMR (Mifflin-St Jeor or Katch-McArdle) x activity = daily calories
    ADA : sedentary 0.8-1.0 g/kg  |  any other activity 1.0-1.8 g/kg
    CDC : daily calories x 10% and 35%, divided by 4.1
    WHO : 0.83 g/kg

**The ADA band is a step, not a slope.** It sits at 0.8-1.0 for the sedentary setting and jumps
to 1.0-1.8 for light activity, then stays there through extra-active. Only the CDC figures keep
climbing, because only they are tied to calories. Easy to model as a smooth function of activity
and be wrong at exactly one setting.

Ranges binary-searched rather than assumed: **age 18-80** (the form's own label is accurate here,
unusually), weight accepted from 1 to 1224 lb, and body fat rejected at both 0 and 100.

### Verification

Engine against the live reference: **35 + 110 cases** across both unit systems, both BMR
formulas, all six activity levels and both sexes — **0 mismatched**. Then the shipped page driven
in Chromium over **45 fresh cases** compared against the Python engine: **0 mismatches, 73
assertions, 0 failed**. The reference's own default (25, male, 5'10", 160 lb, light, Mifflin)
reproduces exactly: 73-131 / 58-202 / 60.

### Two real bugs the suite caught

**The converter was dead.** I lifted the Other Units converter functions from the lean-body-mass
build but not their event listeners, which live in that file's wiring section. Every category
reported 11 units because it was stuck on Length and the category buttons did nothing. Now
Length 11, Temperature 3, Area 11, Volume 23, Weight 10. **Lifting a component means lifting its
wiring too** — the functions alone look complete and are not.

**Overflow of 27 to 97px below 430px.** The activity select's longest option ("Extra active: very
intense exercise daily, or a physical job") has an intrinsic width of ~395px, and a grid item
defaults to `min-width:auto`, i.e. min-content — so that one string held the whole form card open
at 441px inside a 390px viewport. Fixed with `min-width:0` on the grid areas and fields. Worth
remembering as a general trap: **a single long `<option>` can set the minimum width of an entire
grid column**, and nothing about the select looks wrong until you measure.

### Content

1,865-word article, 8 H2s, 7 FAQs. Overlap with the reference **0.00%**; against our own pages
the only matches are the shared disclaimer phrasing about speaking to a doctor or dietitian.
Its territory is why three institutions disagree and how to place yourself between them, that
0.8 g/kg is a floor rather than a target, per-meal distribution and the ~25-40 g synthesis
ceiling, whether more is better, and the situations — kidney disease, pregnancy, children,
recovery — where the page's numbers do not apply. OG image added; slug already in all three
registry files.

## Pregnancy Weight Gain Calculator — engine verified, page not built yet (Aug 9, 2026)

Audit and maths complete and swept clean against the reference; the page itself is still the
stub. Recording the model here so the build can start from it rather than repeating the probing.

### The model

    BMI (pre-pregnancy) -> IOM category -> total gain in pounds
      Underweight  <18.5   singleton 28-40   twins 37-54*
      Normal   18.5-24.9   singleton 25-35   twins 37-54
      Overweight 25-29.9   singleton 15-25   twins 31-50
      Obese        >=30    singleton 11-20   twins 25-42

    * The IOM publishes no underweight twin range. The reference reuses the
      normal-weight one, verified by probe rather than assumed.

    Gain curve, two straight segments meeting at week 13:
      weeks 1-13   0  ->  (1.1, 4.4) lbs        [fixed, whatever the BMI category]
      weeks 13-40  (1.1, 4.4)  ->  (total_low, total_high)

The 1.1 and 4.4 are in **pounds in both unit systems** and must be converted for metric — the
first sweep failed on every metric row because I scaled the totals and left those two alone.

### Reference behaviours worth knowing before building

- **At week 40 the "for week #N" line disappears entirely**, leaving only the delivery line,
  since the two would be identical. My fetch guard keyed off the missing string and reported no
  result at all for every week-40 case until I noticed.
- **A status line uses "weight now"**, which nothing else on the page touches: "in this range",
  or "X lbs lower than the lower bound", or "higher than the upper bound". My first sweep set
  now = before and never exercised it — a whole result field almost went unmodelled.
- **Formatting:** exact zero prints as `0`, values under a tenth print two decimals (`0.09` at
  week 2), everything else one decimal. Rounding is half away from zero — Python's round() turns
  97.55 into 97.5 where the reference prints 97.6.
- **The BMI category is wrapped in `<font color="green">` only for Normal Weight**, which broke
  my parser on every overweight and obese case.

### A reference bug, to match the field and not the error

Entering a current weight just past the upper bound prints the raw float: at 132.4 lbs against a
bound of 132.3 it says **"0.099999999999994 lbs higher than the upper bound"**. Larger gaps print
cleanly (7.7), so the rounding is applied inconsistently. Our page should show a properly rounded
difference and not reproduce this.

### Verification so far

**120 cases, 0 mismatched** across both unit systems, all four BMI categories, singleton and
twins, weeks 1 to 40 — comparing the headline range, the delivery range, the BMI figure and
category, and all forty table rows in every case.

### Still to do

Page build, browser verification, article, OG image. The article needs care: `pregnancy`,
`pregnancy-conception`, `ovulation`, `period` and `due-date` are all close neighbours, so scope it
before drafting as with the conception page — the territory left is IOM categories and why they
differ, the shape of the gain curve, twins, and what under- and over-gaining actually risk.

### Pregnancy Weight Gain Calculator — page built and shipped (Aug 9, 2026)

The engine recorded in the previous entry is now a live page (85KB, `pwg-` prefix).
**Inputs 14/14, results 15/15**: the week range, the delivery range, BMI and category, the
status line against the band, a shaded 40-week chart, and the full week-by-week table.

**Verification.** The shipped JS is a direct port of the swept engine, driven in Chromium over
**40 fresh cases**, comparing the headline, the BMI figure and category, and **all forty table
rows in every case** against the Python engine: **0 mismatches, 65 assertions, 0 failed**. The
reference example from the owner's screenshot (5'6", 120 lb before, 130 now, week 20) reproduces
exactly — 127.3 to 132.3 lbs, gain 7.3 to 12.3, BMI 19.4 Normal Weight. Overflow 0 at 1280, 430,
390 and 360.

Behaviours from the research all held on the built page: week 40 shows the delivery range and
drops the per-week line, underweight twins falls back to the normal-weight 37-54 range, and the
formatting prints a bare `0` at week 1, `0.09` at week 2 and one decimal elsewhere.

**The reference bug was not copied.** Where the reference prints `0.099999999999994 lbs higher
than the upper bound`, ours rounds: `0.1 lbs above the top of that range`. Everything else about
the status line matches, including which of the three variants fires.

**One test artifact, not a page bug.** The validation assertion for height set feet to 0 and left
inches at 6, so the total was still positive and no error fired — correctly. Confirmed by zeroing
both boxes, which does produce the error. The assertion was relabelled rather than "fixed", since
the page was behaving properly.

**Content.** 1,873-word article, 8 H2s, 7 FAQs. Scope was planned against the five neighbouring
pregnancy pages before drafting, as with the conception build. Overlap with the reference
**0.00%**, and against our own pages **zero real shingles** — only byline and disclaimer
boilerplate. Its territory is the one thing none of the neighbours cover: that the range is
anchored to pre-pregnancy BMI and never moves, why the curve is flat then steep, where the weight
actually goes (the baby is a minority of it), that under-gaining carries real risk and pregnancy
is not a time to diet, and twins. OG image added; slug already in all three registry files.

## Sleep Calculator — rebuilt from stub (Aug 9, 2026)

Replaced the stub at `/sleep-calculator/` with a full 3-card build (85KB, `slp-` prefix).
Reference: calculator.net/sleep-calculator.html. **Inputs 20/20, results 11/11.**

**Two calculators on one page**, which the reference runs as two separate forms with their own
Calculate and Clear buttons. Ours keeps that separation: each has its own Clear, and clearing one
leaves the other untouched — asserted, along with the settings surviving both.

    Sleep cycle, from a wake time : bed  = wake - (cycles x length) - time to fall asleep
    Sleep cycle, from a bedtime   : wake = bed  + time to fall asleep + (cycles x length)
    Sleep length (no allowance)   : the other end, plus or minus the length given

    Cycles are listed 5, 6 first as the two recommendations, then 7, 4, 3, 2, 1.
    Defaults: 90-minute cycle, 15 minutes to fall asleep, both adjustable.

**A formatting quirk worth matching:** the reference prints the midnight hour as `0`, so one
cycle after an 11:00 PM bedtime reads **"0:45 AM"** rather than "12:45 AM". Noon still prints as
12 PM. Reproduced, since it is a display convention rather than an arithmetic error — nothing
downstream depends on it and it is what the reference shows.

**Verification.** Engine against the live reference: **20 + 110 cases** across both calculators,
both directions, non-default cycle lengths and fall-asleep times, and times either side of
midnight and noon — **0 mismatched**. Then the shipped page in Chromium over **40 fresh cases**
against the Python engine: **0 mismatches, 68 assertions, 0 failed**. All four reference examples
reproduce exactly — waking at 6:00 AM gives 10:15 PM and 8:45 PM with the full alternatives list;
a 11:00 PM bedtime gives 6:45 AM and 8:15 AM; 100-minute cycles with 20 minutes to fall asleep
give 9:20 PM and 7:40 PM; and the length calculator returns 10:30 PM and 7:00 AM.

**One measurement that looked like a bug and was not.** The minutes label on the "sleep for" row
appeared clipped at the card edge in the screenshot. Measured: 24px of clearance, row scrollWidth
equal to clientWidth, no overflow at any width. Rendering artifact of the screenshot scale, not a
layout fault — left alone rather than "fixed".

**Content.** 1,702-word article, 8 H2s, 7 FAQs. Overlap with the reference **0.00%**, and against
our own pages **zero real shingles**. The reference's own prose is a long tour of REM and non-REM
physiology; ours deliberately goes elsewhere — why waking mid-cycle produces sleep inertia, that
ninety minutes is a population average and errors compound across cycles, the fall-asleep time
everyone forgets to count, thinking in cycles when the night is short, and that schedule
regularity beats any single night's arithmetic. OG image added; slug already in all three
registry files.

### Follow-up: the two calculators moved onto tabs (owner request)

Shipped first as two calculators stacked inside one card. The owner asked for the loan
calculator's pattern instead — a tab bar above, each tab swapping the input fields — so I read
`/loan-calculator/` before changing anything rather than approximating it.

Two things the house pattern does that my first version did not:

- **The tabs live outside the card**, as their own grid area. `.ln-tabs` carries
  `grid-area:tabs` and the grid template has a dedicated `"tabs tabs ."` row. Mine had the tabs
  inside the card and no tabs row at all, so they would never have lined up with the other pages.
- **Tab styling differs from the sub-tabs** used elsewhere: `--border` rather than
  `--border-fine`, 11px/18px padding, 13.5px text. Copied exactly, hover rule included.

The result card now swaps with the tab too, so each calculator owns the headline while it is
active, and the second bottomgrid card became a shared "how the time was worked out" panel that
follows whichever tab is open.

**Caught in review:** the length tab printed its answer twice — once in the green headline and
again immediately below it. Replaced the duplicate with a three-row breakdown (result, length,
counted-from), which is what the space is for.

Re-verified after the restructure rather than trusting that only layout had changed: the suite
was updated to drive each calculator through its own tab, and the whole thing re-run —
**70 assertions, 0 mismatches**, all four reference examples still exact, overflow 0 at four
widths. The tab assertions also pin the grid area and that the tabs sit outside the card, so a
future edit that moves them back inside will fail rather than drift.

**This clears the health and fitness stub batch.** All six from the original queue —
period, pregnancy-conception, pregnancy-weight-gain, protein, target-heart-rate, sleep — plus
shoe-size-conversion are now built, verified and live.

## Technical SEO pass — internal linking and crawl waste (Aug 9, 2026)

Triggered by Search Console showing **222 indexed against 247 not indexed**, and — far worse —
the sitemap view reporting **only 10 of 210 submitted URLs indexed**, with **119 filed as "Page
with redirect"** and site-wide validation on that reason showing **Failed**.

### The sitemap was not the problem

First instinct was a malformed sitemap. Checked it instead of assuming: fetched the live file and
requested **all 212 URLs without following redirects — every one returned 200**, all https, all
trailing-slash, no www, no duplicates. The sitemap was clean.

### The problem was our own internal links

**280 internal links across 32 pages were written without a trailing slash** — `/loan-calculator`
rather than `/loan-calculator/`. The server 308-redirects those to the slash form, so every one
sent Googlebot through a hop before reaching the page. That is what produced the 141 "Page with
redirect" and the 119 inside the sitemap view: Google was following our links to the redirecting
form rather than crawling the sitemap URL directly.

Worst offenders were the sidebar related-calculator cards on older pages — retirement (20),
credit-card-payoff (19), 401k (18).

**On trailing slash generally:** neither form ranks better, and the sources agree the only thing
that matters is consistency. The decision was already made for this site in four places — the
server's 308, 214 canonicals, all 212 sitemap URLs, and our own `_redirects` rules all point at
the slash form. So the links were brought to the site's existing standard rather than the other
way round, which would have meant re-pointing every one of those and re-establishing the index
for no gain.

### What was fixed

| | before | after |
|---|---|---|
| No-slash internal links to real pages | 280 | **0** |
| Internal links to pages that don't exist | 1 | **0** |
| Self-links inside related-calculator cards | 25 | **0** |
| Canonical mismatches on indexable pages | 0 | 0 |
| Reciprocal links to the seven new pages | — | **+15** |

- The one broken link (`bra-size-calculator` → `/waist-to-hip-ratio-calculator/`, a page that has
  never existed) now points at `healthy-weight-calculator`, which is relevant and was not yet
  linked from there.
- 25 self-links removed: sidebar cards were listing the page they were already on.
- `sitemap.xml` lastmod refreshed from **real git commit dates** rather than a blanket stamp —
  21 entries were stale, including sleep-calculator still claiming 21 July after being rebuilt
  today.

### Two bugs my own script introduced, caught before pushing

The reciprocal-link inserter copies the shape of an existing anchor on each page so the markup
matches locally. On two pages the sample anchor wrapped its label in a `<span>`, and the label
substitution only replaced up to the first one — producing
`Target Heart Rate<span>Ideal Weight</span>` on calories-burned and pace. Caught by auditing every
inserted anchor's rendered text against its intended label, then verified in Chromium that all
four repaired links render at the same height as their neighbours.

**Worth keeping:** a bulk edit across 32 files needs its output audited element by element, not
just counted. The counts were right — 15 links added — while two of them were visibly broken.

### Still open, deliberately

- **"Discovered – currently not indexed": 79.** 68 pages still carry two or fewer inbound
  editorial links, mostly Math and Other. The reciprocal pass covered the seven new health pages;
  the long tail needs a wider internal-linking plan rather than a script.
- **404s: 17.** Only one came from an internal link, now fixed. The rest are old slugs Google
  still remembers — they will age out, and `_redirects` already handles the money-markets moves.
- **`crypto-profit-calculator`** is noindex, canonicalises to `crypto-profit-loss-calculator`, and
  is absent from the sitemap. That reads as a deliberate consolidation, so it was left alone.

## On-page SEO audit — Finance and Health sections (Aug 9, 2026)

Audited all **108 built pages** (78 Finance, 30 Health) against title length, meta description
length, canonical correctness, Open Graph and Twitter cards, H1 count, structured data, duplicate
metadata, and leftover no-slash links.

**Clean from the start:** canonicals (108/108 correct), H1 counts, duplicate titles, duplicate
descriptions, and no-slash internal links — the last of which the previous pass had already
cleared.

### What was actually wrong

| Issue | Count | Fix |
|---|---|---|
| Missing `og:image` | 19 | Generated the images and added the tags |
| `twitter:title` / `twitter:description` showing the *site* boilerplate rather than the page | 4 | Pointed at the page's own title and description |
| `<title>` over 62 characters (truncates in results) | 9 | Rewritten shorter, keyword kept at the front |
| Meta description over 165 characters | 3 | Rewritten to fit |
| `og:title` disagreeing with `<title>` | 2 | Aligned to the `<title>` |
| Missing `WebApplication` schema | 1 | Added, copied from the site's own shape |

The 19 OG images were built from each page's real H1 and meta description rather than a generic
template, so the card shows what the page is about. Every title change was applied to `<title>`,
`og:title` and `twitter:title` together — changing one and leaving the others is how the two
mismatches above arose in the first place.

### Two judgement calls, recorded rather than silently made

- **`retirement-calculator` had a shorter `<title>` than its `og:title`.** Before "fixing" it I
  checked git: the mismatch predates this session, so it was not something this pass broke. The
  `<title>` was the length-correct one, so the social tags were brought to it rather than the
  reverse.
- **`crypto-profit-loss-calculator` has no FAQ schema and it stays that way.** Its three H3s are
  topic headings, not questions — "Long vs. short positions" is not a question with an answer.
  Adding `FAQPage` markup there would mean inventing Q&A that isn't on the page, which is exactly
  the sort of thing Google issues manual actions for. The missing `WebApplication` block was a
  genuine gap and was added; the FAQ gap is correct.

### Verified after, not assumed

Re-ran the full audit across all 108 pages: **every check returns zero**. All JSON-LD blocks on
all 108 pages parse as valid JSON. Eight affected pages were then rendered in Chromium to confirm
titles, `og:image` and structured data land correctly and that no page throws a JS error.

## Rebuild 1 of 8 — dividend-yield-calculator (Aug 9, 2026)

First of the eight pages dropped when `061fb5f3` removed `/money-markets/`. The root URL was
returning 404 while `_redirects` sent the old path to a category hub, which Google reads as a
soft 404 — no ranking signal passes. Both rules now point at the real page.

### The parity protocol had no referent, and that had to be settled first

Section 3a-PRIME requires matching calculator.net field for field. **calculator.net does not have
a dividend calculator** — verified against their full site sitemap, not just the finance index.
Nor does it have CAGR, SIP, portfolio allocation, stock average price, break-even, P/E ratio or
gold value. None of the eight has a calculator.net referent, which is presumably why they were
originally built under a separate project.

The check carried its own positive control: the same sitemap fetch *does* return
`sample-size-calculator`, `z-score-calculator`, `probability-calculator`, `triangle-calculator`,
`concrete-calculator`, `tile-calculator` and `random-number-generator`. The lookup finds what
exists, so the absence is real rather than a parsing failure.

**Substitute protocol used, with owner sign-off:** union field map across Forbes Advisor,
MarketBeat and dividend.watch; formulas sourced rather than reverse-engineered; and the sweep run
against an independently written Python implementation (`ref_dividend.py`) derived from the
sourced definitions rather than from the page JS. This catches transcription, rounding and
edge-case errors. It cannot catch a wrong choice of formula — that gap is covered by sourcing,
and it is weaker than what calculator.net gave the Finance and Health pages. Recorded honestly.

### A reference bug, matched-field-not-bug

Forbes Advisor's own worked example calls a $3.50 **quarterly** dividend on a $100 share a "3.5%
yield". Annualised, $3.50 four times a year is $14.00 — a 14% yield. They divided a single payment
by the price. We annualise, per the standard definition, and `ref_dividend.py` carries an
assertion pinning both figures so the distinction can't drift.

### Verification

| Check | Result |
|---|---|
| Sweep cases (yield / YoC / DRIP) | 300 |
| Individual assertions | 870 |
| Mismatches vs Python reference | **0** |
| JS page errors (over HTTP) | **0** |
| Negative control fires | yes |
| FAQ schema ↔ visible HTML | byte-identical, 6/6 |
| JSON-LD blocks parsing | 3/3 (Breadcrumb, FAQPage, WebApplication) |

The first sweep run reported 2 console errors under `file://`. Re-running over `http://localhost`
returned zero — they were protocol artefacts from absolute asset paths, not page bugs. Checked
rather than assumed.

### Three things the screenshots caught that assertions did not

1. **Class-vocabulary mismatch.** The first draft invented its own class names (`.dy-lab`,
   `.dy-btn-go`) while the borrowed CSS defines `.tax-field-label`, `.tax-btn-calc`. Every
   assertion passed — `.dy-grid` present, no stale `tax-` strings, head clean — and the page
   would have shipped as an unstyled column of text. Markup was rewritten against the reference's
   own vocabulary so it inherits CSS already tested at 860px and 430px.
2. **Chart of four identical bars.** Quarterly payments are equal, so the yield chart drew four
   identical rectangles. Correct, and useless. Now a cumulative staircase through the year.
3. **Sensitivity table column of five identical values.** Income on a fixed share count doesn't
   move with price. Replaced with income on a fixed $10,000 stake, which does, and teaches the
   same lesson.

### Registry note — a pre-existing off-by-one

`all-calculators` labelled the Finance panel "Finance (77)" while the panel held **78** links. The
label was already stale. Recounted from the markup rather than incrementing the old number, so it
now reads 79 rather than the 78 an increment would have produced.

### Scope, and what was deliberately left out

Three modes: yield, yield on cost, reinvestment. Flagged omissions, stated on the page rather than
dropped silently — no tax field (treatment varies by country, account type and income band, and a
single field would be wrong for most readers) and no annual-contribution field. The recovered page
also had a `localStorage` saved-presets feature; left out pending a single decision across all
eight.

Sidebar links out to 6 Finance calculators; inbound editorial links added from `investment`,
`roi` and `average-return`. Each was inserted using **that page's own anchor shape** — roi uses
`&rsaquo;` inside `<span aria-hidden>`, the other two use `.arrow` — then audited in Chromium by
rendered text and by height against sibling links, not by count. This is the failure mode that
produced `Target Heart Rate<span>Ideal Weight</span>` on the last bulk edit.

### Remaining seven

cagr, portfolio-allocation, sip, stock-average-price, break-even, pe-ratio, gold-value. All
recovered intact from `061fb5f3^` (85–96 KB each, engine and article present). SIP and gold-value
carry real convention questions — month-start vs month-end contributions, and troy ounce vs tola
plus purity basis — that should be settled explicitly rather than picked silently.

### Correction — DRIP reinvested annually, not at the payment frequency (Aug 9, 2026)

Found by asking whether the page would actually survive a user cross-checking it, rather than by
any test. **All 870 assertions passed straight through this**, because the Python reference and
the page JS shared the same wrong convention — I wrote both. This is exactly the class of bug
flagged when calculator.net turned out to have no referent: the sweep catches transcription and
rounding, not a wrong choice of convention.

The model reinvested once a year. Real DRIPs buy each time a dividend lands, quarterly for most
US and Canadian payers, and so do the competitor calculators a user would check against.

| | annual (was) | quarterly (now) | gap |
|---|---|---|---|
| Default inputs, 20 yrs | $51,400 | $51,540 | +0.27% |
| 8% yield, 30 yrs | $1,282,804 | $1,399,364 | **+9.09%** |

Negligible at the defaults, 9% low on a high-yield holding over a long horizon — enough that
someone modelling a REIT and then checking MarketBeat would conclude the page was broken. Made
worse by the Yield tab already having a payment-frequency selector while the DRIP tab did not:
the page told the user frequency mattered, then ignored it where it compounds.

**Fixed:** reinvestment frequency is now a field (quarterly default, also monthly / semi-annual /
annual). Within a year the annual dividend is split into equal payments and each is reinvested at
that moment's price; the price steps by the freq-th root of the annual rate so annual compounding
is unchanged, and the dividend per share steps once a year, as companies actually raise payouts.
`ref_dividend.py` now asserts the ~9% uplift and that frequency does not distort the price path.
The sweep varies frequency across 1, 2, 4 and 12 — still 300 cases, 870 assertions, 0 mismatches.
Browser-checked that value increases monotonically with frequency.

Also fixed in the same pass:
- **Negative dividends were accepted silently**, printing a -6.41% yield. Now flagged on all three
  modes, matching the existing zero-price guard.
- **Dead `status()` plumbing removed.** It wrote to a `#dy-status` span that cb-ux overwrites on
  load, so it silently no-opped. It surfaced when an edge-case test timed out waiting for the
  selector. cb-ux owns the bar text; the page should not pretend otherwise.
- **Article corrected.** It described the old annual behaviour. Claiming a behaviour the page
  doesn't have is an AdSense content problem as much as an accuracy one, so the reinvestment
  section, the FAQ answer and the "doesn't cover" list were rewritten, and the FAQ schema
  regenerated from the visible HTML and re-diffed.

**Carry into the remaining seven:** `sip-calculator` has the identical exposure — SIP contributions
are monthly and the same annual-loop shortcut would understate every projection. Settle the
contribution timing convention explicitly there rather than inheriting this one.

## Rebuild 2 of 8 — cagr-calculator (Aug 10, 2026)

Four solve-for modes on one grid: growth rate, final value, starting value, time needed.
Period accepts years / quarters / months / weeks / days and converts to fractional years
before the (unchanged, always annualised) formula. Optional fee, tax and inflation behind
the house More Options disclosure.

### Parity had no referent again, as predicted

Re-verified rather than inherited: `calculator.net/cagr-calculator.html` returns 404 and
`growth-rate-calculator.html` returns 404, while `investment-calculator.html` returns 200 as
a positive control. The substitute protocol signed off for dividend-yield applies unchanged.

Union field map across **CalculatorSoup** (four solve-for modes, days/weeks/months/quarters/years
unit selector, and the three reverse formulas stated explicitly), **Omni Calculator** (three modes,
four worked examples) and **MarketBeat RCAGR** (confirms EV = BV(1+r)^N). Every field either of
theirs maps to one of ours; nothing dropped. Ours adds currency, fee, tax, inflation and the
year-by-year table on top — richer than the references, never stricter.

### Verification

`ref_cagr.py` written from the sourced definitions, not from the recovered page JS. Pinned to
**seven independently published worked examples** before any sweep ran — this is the layer that
catches a wrong *choice* of formula, which a self-consistent sweep provably cannot (that gap is
what let the DRIP bug through 870 assertions last time).

Sweep drove `window.__cagrMath` in Chromium against the Python reference:
**2,799 cases, 4,911 assertions, 0 mismatches, 0 console errors**, negative control confirmed
(a deliberate +0.0001 was caught). Browser checks: **45/45** — h1 at 700, byline/disclaimer at
12.5px, single grid track with every child at 100% width at 860/430/390px, jsPDF 0 bytes on load
and 2 requests on first click with no refetch on the second, and CB-UX auto-calculate plus flash
asserted on **all four tabs**, not just the first.

### Conventions settled explicitly rather than picked silently

- **Periods are intervals, not data points.** Engine takes t directly, as both references do.
  Pinned by `test_periods_not_datapoints`: 100 to 200 reads 25.99% over 3 and 18.92% over 4.
  Given its own H2 because it is the differentiator and the mistake is invisible once made.
- **Real CAGR divides, not subtracts** — Fisher, (1+nom)/(1+infl)−1. Asserted to differ from
  naive subtraction by more than 0.15pp so the two can never quietly converge.
- **Fee drag is arithmetic**, matching how expense ratios are quoted, and asserted to differ
  from the multiplicative form. Not applied in rate-solve mode: a measured rate is already net.

### Two checks that were wrong while the page was right

1. The sweep crashed on `32.3 ** 730` — CPython raises OverflowError where JS returns Infinity.
   The reference now models IEEE-754 doubles, since that is what the page runs on.
2. The jsPDF check failed at 0 requests. Cause was the harness: `click()` + `type()` on a number
   input replaced the value with `0`, so the result read "—" and the PDF button **correctly**
   refused to export an empty state. Harness fixed, and that guard is now its own passing check.

A third near-miss during registry work: recounting `all-calculators` category labels with
sloppy section bounds swallowed the Crypto panel into Math and would have pushed "Math (49)".
Re-scoped across all five panels — Math 39 was right all along. Only Finance moves, 79 to 80.

### Article scope

H2 lists of `average-return-calculator`, `roi-calculator` and `investment-calculator` read
*before* drafting. Arithmetic-vs-geometric belongs to average-return and IRR framing to roi, so
this page links out to both rather than restating them. Nine H2s plus a six-question FAQ. The FAQ
is generated from a single `faq.json` into both the JSON-LD and the visible markup, so the
schema-drift bug cannot occur structurally; the exact-match diff still runs, with a negative
control, and reports 6/6.

Sidebar links to 6 Finance calculators. Inbound editorial links from `roi`, `average-return` and
`investment`, each written in that page's own voice and audited individually in Chromium by
rendered text, visibility and box height against a sibling link — not by count.

### Remaining six

portfolio-allocation, sip, stock-average-price, break-even, pe-ratio, gold-value. SIP and
gold-value still carry the open convention questions noted last time (month-start vs month-end
contributions; troy ounce vs tola and purity basis) and should be settled explicitly.

## Rebuild 3 of 8 — portfolio-allocation-calculator (Aug 10, 2026)

Three modes on one grid: rebalance (drift and trades against a band), use new money
(contribution rebalancing without selling), and model allocation (risk profile or age rule).
Five asset classes: US stocks, international stocks, bonds, real estate, cash.

### The recovered page asserted risk profiles that were not sourced

The old file carried `conservative 30/60/10, moderate 60/35/5, aggressive 85/10/5`. Vanguard's
published, commonly cited ladder is **aggressive 80/20, moderate 60/40, conservative 40/60**. The
old conservative sleeve sat 10 percentage points off the standard reference with nothing behind
it — an invented number presented as guidance on a YMYL page.

Rebuilt against Vanguard's spine, with a small cash sleeve carved out of the fixed-income side so
the stock weight matches exactly, and two intermediate steps: 40 / 50 / 60 / 70 / 80. The page
now says on its face where the numbers come from. `test_vanguard_ladder` pins the three anchor
points and asserts monotonicity.

### Verification

calculator.net has no allocation or rebalancing calculator — re-verified live rather than
inherited (`portfolio-allocation`, `asset-allocation`, `rebalancing`, `portfolio` all 404;
`investment-calculator` and `finance-calculator` both 200 as positive controls).

`ref_portfolio.py` written from sourced definitions and pinned to **five worked examples from
four outside sources**: stockalpha.ai (8,000/3,600 at 60/40 → sell 1,040), ryanoconnellfinance
(75,000/41,200 → sell 5,280, and 4.5pp must NOT trip a 5pp band), Bogleheads (drift to 57.45%,
and contribution-only rebalancing to 64/36), and investment-calculator.net (contribution targets
computed on the post-contribution total: 6,600 / 3,300 / 1,100).

Because rebalancing has no single reference calculator, the sweep leans on **ten invariants**
across 400 random portfolios rather than only on pinned numbers: trades net to zero when targets
sum to 100, buys equal sells, drifts sum to zero, applying the trades lands exactly on target,
the total is unchanged, the contribution never spends more than the smaller of itself and the
underweight gap, no asset is ever told to both buy and sell, and a covering contribution lands
every underweight asset exactly on its new target.

Sweep against the page JS: **977 cases, 16,403 assertions, 0 mismatches**, negative control
passing. Browser: **55/55**, including all three tabs, 860/430/390px, and lazy jsPDF.
FAQ schema vs visible: 6/6 exact.

### Conventions settled explicitly

- **Drift is in percentage points, not percent.** Retail guidance means an absolute band;
  several institutions use a relative +/-25% band at sub-asset level, which gives very different
  answers on small holdings. Stated on the page and given its own H2, because "act at 5%" is
  genuinely ambiguous and nobody says which they mean.
- **Contribution targets are computed on the post-contribution total**, pinned against a
  published example. Computing them on the old total lands you near target, not on it.
- The contribution is **prorated across underweight assets in proportion to the gap**, so the
  output is what to buy today rather than a wish list.

### A contradiction assertions could not see

The user-session step — added to the checklist after the CAGR build — caught it again. With
drift under the band the headline read **"$5,280.00"** while the flag underneath read **"no trade
is needed today"**, and the per-asset rows said "Sell $5,280.00". Every figure correct, the card
as a whole incoherent: it handed the visitor a number to trade and then told them not to.

Now the headline reads "None" when nothing breaches the band, the rows report position
("4.5pp adrift — within band") instead of instructions, the full-rebalance figure moves to its
own supporting row so nothing is lost, and the table note explains that its Action column is
hypothetical in that state. Regression checks cover both band states.

Also found by looking rather than asserting: asset classes left at 0 value and 0 target produced
three useless "On target" rows, now suppressed; and the target-% inputs were **clipping** ("60"
rendering as "6C") because the % suffix ate 27px of a 74px column. Measured rather than eyeballed
— `scrollWidth > clientWidth` at every breakpoint — widened, and re-measured to zero clipping at
1280/860/430/390.

### Two build-system faults caught before they shipped

1. `assemble.py` had the output path **hardcoded to cagr-calculator**, so the first portfolio
   build silently overwrote the CAGR page. Restored from git and the path is now derived from
   `SLUG`. The head-integrity assertions added last round did not catch this because the file it
   wrote was internally consistent — just written over the wrong page.
2. The FAQ negative control reported "not caught" and was itself broken: it mutated a hyphen in
   an answer that contains no hyphen, so the mutation was a no-op. Replaced with three controls
   that cannot be no-ops (curly quote, appended space, swapped first character), all caught.

### Registry

Finance 80 to 81, recounted from markup across all five panels. Inbound editorial links from
`retirement`, `investment` and `net-worth`, each inserted after that page's real first block —
the retirement anchor is followed by a `<ul>`, not a `<p>`, which broke the first attempt — then
audited individually in Chromium by rendered text, visibility and box height.

### Remaining five

sip, stock-average-price, break-even, pe-ratio, gold-value. SIP and gold-value still carry the
open convention questions (month-start vs month-end contributions; troy ounce vs tola and purity
basis) and should be settled explicitly rather than picked silently.

## Rebuild 4 of 8 — sip-calculator (Aug 10, 2026)

Three modes: monthly investing (with compound annual step-up), reach a target, and monthly
versus lump sum. Plus a user-facing rate-basis switch, explained below.

### Owner caught a US-first violation before it shipped

The first draft defaulted to INR, because SIP is an Indian term and every reference source is
Indian. Section 8 documents this exact failure already — the VAT calculator was built UK-first
in GBP and rejected on Aug 7 — and carries the standing rule that a US-first default is never
deviated from without asking first. I was deciding it inside the build. The owner spotted the
rupee sign and stopped it.

Rebuilt USD-first on the VAT pattern: dollar defaults, dollar worked examples, US framing
(monthly investing / dollar-cost averaging) leading, INR one click away in the dropdown, and an
H2 explaining what SIP means and how it maps to a 401(k) or an automatic transfer. Slug kept —
recovering that URL's signal is the whole point. The page now carries an assertion that no rupee
renders in the result card, inputs, bar, table or article, only inside the currency `<option>`.

### Three conventions, all settled against published figures

1. **Annuity due.** Deposits at the start of each month, the `x (1+i)` tail. Universal.

2. **Monthly rate basis — genuinely contested, so exposed as a control.** Divide-by-12 is used
   by Mirae Asset, Motilal Oswal and Bajaj Finserv; the twelfth root by Groww, INDmoney, 5paisa
   and YES Securities. Groww calls divide-by-12 "a common mistake"; three large AMCs publish
   figures computed with it. Both camps are pinned in `ref_sip.py` and both reproduce exactly:
   Motilal's Rs 11,61,695 to the rupee, Groww's Rs 12,766 to the rupee. Default is divide-by-12,
   the majority convention and what US monthly-investment tools use. The gap is 1.7% at 5 years
   and **14.6% at 30**, so it is a visible switch under More Options with an H2 explaining why
   another site gives a different number — not a buried assumption. No competitor does this.

3. **Step-up compounds, and the obvious reference is wrong.** Mirae's calculator page describes a
   LINEAR top-up (5,000 -> 5,500 -> 6,000 -> 6,500, total 23.40 lakh) but publishes a corpus that
   matches neither convention: linear gives 0.79 Cr, compound 0.99 Cr, they print 1.16 Cr. Their
   plain-SIP figure (49.96 lakh) reconciles perfectly, so only the step-up number is broken.
   Settled against a separate source — Mirae's own head of products in Business Standard:
   20,000/mo, 20y, 11%, 10% step-up -> **3.58 Cr on 1.37 Cr invested**, which compound matches to
   3.578 / 1.375 while linear would invest only 0.94 Cr. CalcCorp's published progression
   (5,500 / 7,321) matches compound to the rupee. Matched the field, not the bug.

### Verification

Sweep: **1,504 cases, 2,616 assertions, 0 mismatches**, both rate bases, step-ups of 0/5/10/15,
returns from -6% to 25%, horizons 1-30 years.

**A negative control failed, correctly, and exposed a real weakness.** The control perturbed a
result by +0.01 and reported "not caught". It was right: the comparison tolerance is *relative*
(1e-7), which on a $296,474 result permits 0.03 of drift, so the perturbation sat inside it. The
earlier CAGR and portfolio sweeps used the same +constant pattern but on values in the hundreds
or thousands, where it stayed outside tolerance — only six-figure outputs exposed it. Controls
now perturb by a *ratio* (x1.000001) and are applied to two different functions.

Browser: **51/51**, including all three tabs, the USD-default assertions, the rate-basis switch
producing both reference figures ($9,991,479 and $9,198,574), compound step-up landing the final
year at $3,058, and lump-sum beating monthly at a positive return while losing at a negative one.
FAQ schema vs visible 6/6 exact with three working controls. Every numeric claim in the FAQ and
article was run through the reference before writing (296,474 -> "roughly $296,000").

### One anomaly chased down, not waved through

The inbound link on `retirement-calculator` measured 841x45 where the other two measured 95x19 —
same 14-character text. Not a bug: `getClientRects()` returns 2, so the inline anchor wraps
across a line break and the bounding box is the union of both lines. Worth recording as a method
note: **bounding-box height is a misleading audit metric for inline links that wrap**; use
`getClientRects().length` plus computed `display` instead.

### Scope

`investment-calculator` has zero coverage of monthly contributions (checked before drafting), so
there is no cannibalisation — this page owns monthly investing, step-up and DCA. Finance 81 to
82. Inbound links from `investment`, `retirement` and `compound-interest`, each inserted after
that page's real first block and audited individually.

### Remaining four

stock-average-price, break-even, pe-ratio, gold-value. **gold-value carries the same class of
problem the owner just caught**: tola is a South Asian unit, so it defaults to troy ounces and
grams with USD, tola offered as an option — raise it before building, do not decide it inside.
