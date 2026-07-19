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
| 4 | IRA Calculator | Upgrade (thin) | ⬅️ NEXT |
| 5 | Roth IRA Calculator | Upgrade (thin) | pending — sibling of #4, do together if convenient |
| 6 | Annuity Payout Calculator | Upgrade (thin) | ✅ DONE (done out of order, ad-hoc user request Jul 20, 2026) — rebuilt to 3-card pattern, reusing Annuity Calculator's visual/JS conventions (apo- prefix): two tabs — Fixed Length (solve for payout amount) and Fixed Payment (solve for how long a chosen payment lasts, with automatic perpetuity detection when payment ≤ periodic interest); Payout Frequency selector (Monthly/Quarterly/Semiannual/Annual); level-payment annuitization formula verified independently in Node before shipping; year-by-year schedule table + stacked interest-vs-principal chart + 2-segment donut; PDF export; competitor research (calculator.net, annuity.org, catalinastructuredfunding, CBS/SmartAsset $100k-annuity coverage) folded into a "what real lifetime annuities pay vs. this calculator's period-certain math" section; 7 H2 sections + 6 FAQs; new OG image.
| 7 | P/E Ratio Calculator | **New page** (doesn't exist yet) | pending |
| 8 | Gold Calculator | **New page** (doesn't exist yet) | pending |

When #3–8 are all done, re-pull GSC data and re-rank the next batch — don't
assume this exact order still holds after a few weeks of new data.

## Also completed (ad-hoc audit requests, outside the numbered queue above)

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
  the next session. Consider setting up a way to authenticate that doesn't
  require pasting the raw token into chat each time (e.g. the user storing
  it outside the conversation and Claude Code/CLI picking it up from local
  environment instead).
- **Workflow / no repo clutter**: all scratch work (`build_*.py`,
  `test_*.js`, `verify_*.js`, screenshots) lives in the sandbox's
  `/home/claude/work/` scratch directory for that session only — it is
  never part of this repo and never committed. Only the actual page file
  (`<slug>/index.html`), its `og/<slug>.png`, and any shared files touched
  (`sitemap.xml`, `calculators-index.json`, `all-calculators/index.html`)
  get `git add`ed. Nothing accumulates in the repo between sessions.
