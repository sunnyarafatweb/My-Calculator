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

  **Still outstanding for this slug**: `present-value-calculator` is still a
  484-line template-tier page. Checked per the AdSense no-over-claiming rule:
  the new article makes no claim about it — the article's only links are its
  own TOC anchors, and the sidebar lists it by name with no feature promise,
  so nothing needs correcting. It is still the obvious next upgrade, and the
  two pages should end up as a matched pair.

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
  rather than repeating this note a fourth time. **Update, Jul 27, 2026
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
- **Workflow / no repo clutter**: all scratch work (`build_*.py`,
  `test_*.js`, `verify_*.js`, screenshots) lives in the sandbox's
  `/home/claude/work/` scratch directory for that session only — it is
  never part of this repo and never committed. Only the actual page file
  (`<slug>/index.html`), its `og/<slug>.png`, and any shared files touched
  (`sitemap.xml`, `calculators-index.json`, `all-calculators/index.html`)
  get `git add`ed. Nothing accumulates in the repo between sessions.
