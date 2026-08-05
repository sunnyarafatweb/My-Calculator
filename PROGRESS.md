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
- **Workflow / no repo clutter**: all scratch work (`build_*.py`,
  `test_*.js`, `verify_*.js`, screenshots) lives in the sandbox's
  `/home/claude/work/` scratch directory for that session only — it is
  never part of this repo and never committed. Only the actual page file
  (`<slug>/index.html`), its `og/<slug>.png`, and any shared files touched
  (`sitemap.xml`, `calculators-index.json`, `all-calculators/index.html`)
  get `git add`ed. Nothing accumulates in the repo between sessions.
