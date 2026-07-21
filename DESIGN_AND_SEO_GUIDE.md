# CalculatorBoss — Design & SEO Build Guide
*Last updated: 2026-07-18. This file is the persistent reference for how every calculator page on this site must be designed, written, and SEO-optimized. Read this in full before building or upgrading any page.*

---

## 0. Site facts (don't relearn these every time)

- **Stack:** Next.js, statically exported (`next export`-style output). The **built HTML/CSS/JS output lives directly in the repo root** — there is no `src/` or `package.json` in this repo. You edit the exported `index.html` files directly.
- **Hosting:** Cloudflare Pages, connected directly to this GitHub repo. **Any push to `main` deploys live instantly** — there is no staging/preview step in the normal workflow. Treat every commit as a production release.
- **Brand name:** CalculatorBoss (`calculatorboss.com`).
- **Total calculator pages:** ~199 folders as of this writing.
- **Two tiers of pages currently exist:**
  1. **Custom-built pages** (e.g. `mortgage-calculator`, `bmi-calculator`, `savings-calculator`, `tip-calculator`) — deep content, bespoke interactive calculator UI (charts, multi-field forms), full SEO treatment. ~1000–2000 lines of HTML.
  2. **Template/generic pages** (e.g. `body-fat-calculator`) — thinner content, simpler generic title tag (`X Calculator | CalculatorBoss`), fewer FAQ items, less topical depth. ~400–600 lines.
  - **The goal going forward: bring every template-tier page up to custom-built tier**, using the pattern below.

---

## 1. Design system (do not break this)

There is a **PROTECTED SHARED STYLE BLOCK** duplicated near the top of every page's `<style>` tag. Rules for touching it:
- Never add a universal `*{...}` reset — it has broken `.mx-auto` centering site-wide before.
- Never remove `--surface`, `--surface-sunken`, `--border`, `--border-fine`, `--ink-faint`, `--shadow-sm` from `:root` — 185+ pages depend on these via Tailwind utility classes.
- If you must change this shared block, propagate the identical change to **every page**, then spot-check at minimum: one custom-built page (bmi-calculator or tip-calculator) and one template page (body-fat-calculator) for layout/centering/card visibility/nav display, with zero console errors — before assuming it's safe to push.

### Design tokens
- **Fonts:** IBM Plex Sans (body/UI), IBM Plex Mono (`.mono`, eyebrows, kickers, labels) — loaded from Google Fonts.
- **Background:** `#F3F1EA` warm off-white, with a soft green radial gradient wash near the top.
- **Core palette:**
  - Brand accent (gold/green): `--gold:#1BA94C`, `--gold-deep:#128A3D`, `--gold-hi:#33C266`, `--gold-tint:#E4F5EA`
  - Category accent colors (used to color-code calculator categories): Finance `--fin:#22417A`, Health `--hea:#0C9268`, Math `--mat:#4B4ED8`, Other `--oth:#CF3F53` (each with a paired `-tint`).
  - Ink/text: `--ink:#181A1F` (headings), `--ink-soft:#474C55` (body), `--muted:#787D86`, `--muted-2:#A6AAB1`.
- **Radii:** `--r-sm:12px; --r:16px; --r-lg:24px; --r-xl:32px`. Max content width: `--maxw:1180px` via `.wrap`.
- **Shadows:** layered soft shadows (`--sh-sm`, `--sh`, `--sh-lg`) — never hard drop-shadows.
- **Header:** sticky, white, blurred backdrop, height 70px, nav links + search trigger + CTA button.
- **Hero:** two-column (`1.04fr .96fr`), left = eyebrow badge + H1 + subhead + search bar + quick-filter chips; right = a live preview/chart card of the calculator's output.

### Page skeleton (in order)
1. Sticky header (logo, nav links, search trigger, CTA)
2. Hero — eyebrow, H1 (calculator name only, e.g. "Mortgage Calculator"), one-sentence subhead, optional search/chips
3. The interactive calculator panel itself (glassmorphic `.panel`, inputs left / live results+chart right)
4. 6–9 educational H2 sections building topical depth (see content architecture below)
5. FAQ section (H2 "Frequently Asked Questions", 5–6 Q&As)
6. Footer

**Gap to fix going forward:** current custom-built pages have **no visible "Related Calculators" internal-linking block** and no visible on-page breadcrumb trail (breadcrumb only exists as invisible schema). Every new/upgraded page should add a visible related-calculators module (3–6 links to topically adjacent calculators, using `calculators-index.json` as the source of truth for valid slugs) and a visible breadcrumb — this is free internal-linking equity we're currently leaving on the table.

---

## 2. Content architecture (what makes a page "custom-built" tier)

Looking at mortgage / bmi / savings-calculator, the H2 pattern is consistently:

1. **"Understanding / What [X] Actually Tells You"** — plain-language concept primer.
2. **"How This Calculator Works" / "The Formula"** — the actual math, transparently shown (builds trust + E-E-A-T).
3. **Breakdown of each input field** — what each field means, why it matters, common mistakes.
4. **A comparison section** — X vs. adjacent concept (e.g. "Savings Accounts vs. Money Market Accounts", "Fixed vs. Adjustable Rates", "15-year vs 30-year").
5. **A nuance/misconceptions or "what this doesn't cover" section** — signals depth and honesty, differentiates from thin competitor pages.
6. **A practical decision-help section** — "Should you...", "How much should you...", "Is there such a thing as...".
7. Occasionally: a short historical/context section for topical authority.
8. **FAQ (H2) — 5–6 Q&As**, phrased as real people would search them (these double as FAQPage schema content and PAA-snippet bait).

Template-tier pages (body-fat-calculator) currently only have ~3 H2s before FAQ. **Target for every upgraded page: at least 6 substantive H2 sections + FAQ**, matching the depth of the three reference pages.

---

## 3. On-page SEO checklist — apply to every page, no exceptions

This is the standing SEO spec. Follow this for every page whether new or upgraded, written for 2026 search behavior (answer-engine + AI Overviews + traditional SERP all matter now):

### Meta / head
- [ ] `<title>`: **"[Calculator Name] — [specific benefit/outcome, not just a keyword restate]"**. Pattern from reference pages: *"Mortgage Calculator — See Your True Monthly Payment"*, *"BMI Calculator – See Your Healthy Weight Range"*, *"Savings Calculator – See When You'll Reach Your Goal"*. Write for **click-through**, not just impression — it should promise a specific outcome the searcher gets, not just name the tool. Avoid the generic `X Calculator | CalculatorBoss` pattern found on template pages — replace it during upgrades.
- [ ] `meta description`: benefit-first sentence + trust/friction-removal cues (free / instant / no signup) + a specifics hook (what it accounts for, e.g. "principal, interest, taxes, insurance and PMI"). ~150–160 characters.
- [ ] `meta keywords`: include primary term + 4–6 close variants (harmless legacy tag, keep for consistency with existing pages).
- [ ] `canonical` URL set to the trailing-slash production URL.
- [ ] `robots` + `googlebot` tags: `index, follow, max-image-preview:large, max-snippet:-1` (as currently set).
- [ ] Open Graph + Twitter card tags mirroring title/description, plus an `og:image` (1200×630) — confirm an image exists at `/og/[slug].png` or generate one; don't ship a page with a broken OG image.

### Structured data (JSON-LD) — required on every page
- [ ] `BreadcrumbList` (Home → Category → This calculator)
- [ ] `FAQPage` with every FAQ question/answer that's also visibly rendered on the page (schema must match visible content — mismatches risk manual action / rich-result loss). **Known recurring failure mode (hit on all four calculator rebuilds so far — IRA, Bond, and now Budget Calculator):** the schema JSON tends to get typed with a plain double-hyphen (`--`) or straight quotes (`'`/`"`) where the visible article text uses an em dash (`—`) or curly/HTML-escaped quotes, since the two are written in separate passes. **Do not rely on writing them consistently by hand** — after finalizing both the schema and the visible FAQ HTML, run the same automated diff check used in every session so far (extract each schema Q/A, extract each visible `<h3>`/`<p>` pair, assert exact string equality) before shipping, every single time, regardless of how careful the authoring felt in the moment.
- [ ] `WebApplication` with `applicationCategory` (FinanceApplication / HealthApplication / etc.), `offers: {price: 0, priceCurrency: USD}`, and a one-line description
- [ ] Add visible `BreadcrumbList` HTML (not just schema) to the page itself, per the design gap noted above.

### Content / E-E-A-T (2026 rules)
- [ ] Match **search intent** first: a calculator query wants the tool above the fold, immediately usable, before any essay.
- [ ] Show the underlying formula/methodology transparently — this is now a strong E-E-A-T + AI-Overview-citation signal; generic/unsourced claims get skipped by both users and AI answer engines.
- [ ] Write FAQs as literal search queries people type (People-Also-Ask phrasing), not marketing phrasing.
- [ ] No keyword stuffing — natural language, topical coverage over repetition. Google's helpful-content systems and AI Overviews both penalize thin, keyword-stuffed pages harder than in past years.
- [ ] Internal links: every page must link out to 3–6 related calculators (visible module, not just sitemap-level) and back to the relevant category hub (`/all-calculators/`).
- [ ] Keep Core Web Vitals clean — since this is static HTML already, mainly watch image weight and avoid layout shift from late-loading charts.
- [ ] Mobile-first check on every shipped page (this audience searches mobile-first for finance/health calculators).

---

## 4. Keyword research — MANDATORY step before writing title/meta/content, every calculator, from now on

**Standing directive (added Jul 2026, applies to every calculator build or upgrade going forward, no exceptions):** before drafting or finalizing the title tag, meta description, H1/subhead, or content outline for any calculator page, do real keyword research for that specific calculator first, and let the findings shape the copy — don't write the copy first and back-fill keywords into it.

**Tool-honesty note:** this environment doesn't have a login to a paid keyword tool (Ahrefs, SEMrush, Google Keyword Planner) or a connected Google Search Console. Don't imply access to one. The real, honest process here is **web-search-based competitive proxy research**, which is a legitimate and commonly-used method, not a lesser substitute to hide:
1. Web-search the calculator's core **short-tail / head term** (e.g. "ira calculator") to see who currently ranks, how deep their content is, and what "People Also Ask" questions surface. Head terms are typically **high search volume but high competition** — worth targeting in the H1/title for long-term authority-building, but not the only thing to target on a new/low-authority site.
2. Web-search **5–10 long-tail variants** (e.g. "ira contribution calculator", "ira deduction calculator", "traditional vs roth ira calculator", "ira calculator with catch up contribution"). For each, check: is there a dedicated competitor page/tool for it (signals it's a real, distinct query cluster, not just a phrasing variant), or does it only show up folded into a broader page (signals it's a sub-topic to cover within this page rather than a separate query worth its own title focus). Long-tail terms are typically **lower competition, sometimes lower volume individually, but higher intent** — these are the near-term rankability opportunities for a new domain and should be woven into H2s, FAQs, and the meta description/keywords tag.
3. Explicitly look for the **high-search-volume + comparatively lower-competition** middle ground where it exists (e.g. a specific benefit/feature phrase big sites haven't optimized a title around even though they mention it) — this is the best ROI keyword type and worth calling out specifically when found, not just lumped in with the long-tail list.
4. Cross-check the page's planned content/formulas against **at least 3-4 major competing calculators** for the same tool (e.g. calculator.net, Bankrate, NerdWallet, SoFi, Fidelity/Vanguard/Forbes Advisor for finance; verified official sources like IRS.gov for any figures) — this both surfaces keyword gaps (a distinct query cluster a competitor targets with a dedicated page that this page should at least cover as a section) and content gaps (a feature/section competitors have that's genuinely useful and missing here).
5. Write the **title** to win the click, not just the impression: benefit-first, matching the highest-value term found in step 1-3 naturally rather than forcing the exact head term verbatim if a more specific/compelling phrase tested better in competitor titles. Follow the format already established in section 3 (benefit-first, not a bare keyword restate).
6. Write the **meta description** (~150-160 characters) to convert an impression into a click: lead with the concrete benefit, include a specific hook (what it accounts for/covers), include a friction-removal cue (free/instant/no signup), and naturally include 1-2 of the researched long-tail phrases if they fit without sounding forced.
7. Populate `meta keywords` with the primary term plus the 4-6 best long-tail variants found in step 2-3 (harmless legacy tag, but should reflect real research, not guesses).
8. **Every future calculator build in this repo must show this research happened** — briefly note in the PROGRESS.md entry for that page which head term(s) and long-tail variant(s) were targeted and why, the same way past entries note formula-verification steps.
9. **Geography**: apply section 8 below (USA-first, then Tier-1 English markets, then worldwide) when choosing which regional phrasing/spelling/competitor set to prioritize — a term big US sites converge on beats a technically-correct but region-neutral phrasing.
10. If/when the user connects Google Search Console (check `search_mcp_registry` for a connector, or the user exports GSC data manually) or a paid keyword tool becomes available, switch to that real query/impression/volume data as the primary signal for that page and treat the web-search method as the fallback it always was.

---

## 5. The "3-card" pattern (current best-practice evolution)

Pages like `sales-tax-calculator` and `salary-calculator` represent a **leaner evolution** of the design system, superseding the older big-hero pattern (mortgage/bmi/savings-calculator). Use this 3-card pattern for all new/upgraded pages going forward:

- Simple header: `<h1>` + one-sentence subhead directly in the content wrapper (`<div class="px-4 sm:px-6 py-8 sm:py-10 mx-auto" style="max-width:1160px">`) — no big split hero/chart-preview section. Faster to ship, less CSS/markup weight, still on-brand.
- A CSS grid (`grid-template-areas:"bar bar ." "form result sidebar" "bottomgrid bottomgrid bottomgrid"`) with a page-specific class prefix (`tax-`, `cur-`, etc. — pick a short prefix per page to keep styles self-contained and easy to reason about):
  1. **bar** — thin navy status bar across the top (context line for the tool), with a white "💾 Save as PDF" button on the right (`justify-content:space-between`). This is now a standing pattern for every page — see loan-calculator and sales-tax-calculator for the reference implementation. **Load jsPDF + jspdf-autotable lazily, on click, not unconditionally on page load** (~403KB combined — real weight for a feature most visitors never use). Don't put `<script src="...jspdf...">` tags in the page at all; instead add a small `loadScriptOnce(src)` / `ensurePdfLibs()` helper (dynamically creates the `<script>` tags and resolves a cached Promise once loaded) and call it from the PDF button's click handler before running the existing `generatePdf()` — show the button as disabled with "Loading…" text while the Promise resolves, then restore it and call `generatePdf()`. See apr-calculator, annuity-payout-calculator, or time-zone-calculator for the reference implementation (confirmed via Playwright: jsPDF fetches zero bytes on page load, first click still produces a correct download, second click doesn't re-fetch). Keep the bar's status text short enough to stay on one line next to the button at the bar's actual width (it spans 2 of the 3 grid columns, not the full page width) — a too-long sentence wraps the button onto its own line, which still works but doesn't match the reference layout.
  2. **form card** — inputs.
  3. **result card** — big-number output + supporting rows.
  4. **sidebar card** — a navy "related calculators" card (this *is* the visible internal-linking module — the earlier-noted gap is solved by this pattern; older hero-style pages still lack it and should get one when next touched).
  5. **bottomgrid** — two supporting cards (e.g. a breakdown/comparison card + a reference/glossary or fact-list card).
- Below the grid: `.{prefix}-seo-article` with a byline (`Written by the CalculatorBoss Finance Team · Reviewed for accuracy · Last updated [Month Year]`), a table-of-contents nav linking to `<h2 id="...">` anchors, then the H2 sections + FAQ H3s, then a small disclaimer paragraph.
- Responsive: grid collapses to a single column under 860px; test both breakpoints.
- **The form card's button row is Calculate + Clear only — no Share button.** A prior version of several pages had a 3rd "🔗 Share" button crowding the row; this is now removed sitewide (kept only the harmless, independent URL-param pre-fill logic where it existed, since that's not tied to a visible button and costs nothing to leave dormant). Both buttons flex to fill the full row width (`flex:1.3` on Calculate, `flex:1` on Clear — Calculate ends up visibly but not dramatically wider, ~1.28x in practice, as the primary action), not a fixed-width pair with empty space where the 3rd button used to be. (Note: the separate, older "crypto/trading batch" design system — position-size/leverage/liquidation-price/mining-profit/risk-reward/staking-reward/crypto-tax calculators — has a *different*, already-clean 2-button 50/50 `calc-btn-row`, plus a distinct "Copy shareable link" button grouped with Print/CSV export tools in a separate `export-row`. That's a different feature in a different context, not the same crowding issue — don't touch it as part of this convention without a separate, explicit decision to do so.)
- **The page's `<h1>` must render bold.** The common `font-display text-3xl sm:text-4xl tracking-tight text-ink mb-3` class combo does *not* include a bold weight on its own — `font-display` only sets the font-family, not weight, so it silently renders at regular (400) unless `font-bold` is explicitly added to the class list. Always include `font-bold` in the H1's classes (e.g. `font-display font-bold text-3xl sm:text-4xl tracking-tight text-ink mb-3`) and confirm with `getComputedStyle(h1).fontWeight === '700'` in a Playwright check — don't assume the class name alone guarantees the rendered weight.

## 6. Hard-won lessons (read before adding any live/external-data feature)

- **Always test third-party API calls from an actual browser context, not just curl/Node.** `curl`/Node's `fetch` do not enforce CORS, so a working curl response proves nothing about whether client-side JS in a real browser can read that response. Verify with `curl -sI -H "Origin: https://calculatorboss.com" <api-url>` and confirm an `access-control-allow-origin` header comes back — or better, load the real page in Playwright and check for zero console errors after the fetch resolves. (Concretely: `api.frankfurter.app`, the legacy currency-rate domain, sends **no** CORS header and silently fails in every browser; `api.frankfurter.dev` does send one and works. The original currency-calculator page was built against the broken domain — likely never worked for a real visitor.)
- Before pushing any page with live client-side data, run it through a local static server (`python3 -m http.server` from the repo root — note: background it with `setsid ... &` in its own command, since it must be started in the same tool invocation you use it in, or it gets killed) and a headless Playwright pass: check for zero console/page errors, confirm the result actually populates, and screenshot both desktop and a ~390px mobile width.
- When splicing a shared head/footer into a rebuilt page programmatically, diff the final file's shared `:root{...}.menu-btn{display:none}` block against another untouched page's identical block (`a == b` string compare) to prove the protected section wasn't corrupted — don't eyeball it.
- When a "solve for X, given Y" reverse calculation produces a **fractional** period count (e.g. solving for how many months a payment lasts, not how large the payment is), any period-by-period simulation loop must run `Math.ceil(n)` iterations, not `n` directly — a bare `for(i=1; i<=n; i++)` silently drops the final fractional period when `n` isn't a whole number, undercounting the total by almost one full payment. Caught this exact bug in the Annuity Payout Calculator's Fixed-Payment mode via a cross-check against the same scenario computed the other direction (Fixed Length) — the two totals should match and didn't, which is what surfaced it. Always cross-check a reverse-solve mode's output against the forward mode with matching inputs before shipping either one.
- **`_headers` rules are additive, not overriding.** Per Cloudflare's own docs: "If a header is applied twice in the `_headers` file, the values are joined with a comma separator." A path matching both a general rule (`/*`) and a specific one (`/_next/static/*`) gets BOTH Cache-Control values glued together into one self-contradicting header — this silently broke long-term caching for every shared CSS/JS asset site-wide (confirmed live via `curl -I`: `cf-cache-status: BYPASS` and a header reading `no-store, ..., public, max-age=31536000, immutable` at the same time) even though the file's author clearly intended the specific rule to win. Fix: put `! Cache-Control` (Cloudflare's documented header-removal syntax) on its own line in the specific block before re-declaring the header, so it resets rather than merges. Always verify with `curl -sD - -o /dev/null <url> | grep -i cache-control` (and check `cf-cache-status` goes `MISS` then `HIT` on a second request) after touching `_headers` — don't assume path specificity wins by default.
- **Load jsPDF (+ jspdf-autotable) lazily, on the PDF button's click, never unconditionally on page load.** Combined they're ~403KB — real weight paid by every visitor on every page view for a feature most people never use. See the "3-card pattern" section above for the concrete implementation (`loadScriptOnce`/`ensurePdfLibs` helpers + a disabled/"Loading…" button state while the Promise resolves). Verify with Playwright: assert no request URL containing `jspdf` fires before the button is clicked, and that `window.jspdf` is `undefined` until then.

## 8. Standing directive: Tier-1 / USA-first SEO priority

**As of July 2026, ~70% of this site's traffic is from the USA.** Until told otherwise, treat US search behavior as the primary optimization target for every page, with other Tier-1 English-speaking markets (Canada, UK, Australia) as the secondary consideration. Concretely, this means:

- **Keyword choice**: don't assume the site's own brand terminology (e.g. "Calculator") is what searchers actually type. Before finalizing a title/H1 for any page, spot-check what the top-ranking US competitors call the same tool — if they consistently favor a different term (e.g. major finance sites overwhelmingly title currency pages "Currency **Converter**" over "Currency Calculator"), work that higher-volume term into the title tag and meta description even if the URL slug/brand keeps "Calculator" for consistency. Don't force a rename of the H1/URL for this alone — blend the terms naturally instead of replacing one with the other.
- **Spelling & phrasing**: American English throughout (traveling, customize, color, etc. — not travelling/customise/colour). Numbers/currency formatting defaults to US convention ($1,234.56, comma thousands separator, period decimal).
- **Dates**: never show a raw ISO date (`2026-07-19`) to the visitor — format it in a way a US reader parses instantly (e.g. `Jul 19, 2026`), since ISO dates read ambiguously to a non-technical US audience (day/month order confusion).
- **Defaults**: where a calculator needs a default currency, unit, or region-specific assumption, default to USD / US units / US conventions unless the tool is explicitly region-specific (e.g. a UK-mortgage or VAT calculator).
- **Content examples**: worked examples and sample numbers in body content should read naturally to a US reader (dollar amounts, US tax/finance conventions) unless the page is explicitly about another country's system.
- This doesn't mean ignoring worldwide usability (the currency calculator's full 165-currency coverage stands, for instance) — it means that when a genuine trade-off comes up between "technically neutral/international" and "what a US searcher expects to see first," default to the latter.

## 9. Workflow / safety notes

- This repo is the **live production source** — every push deploys instantly via Cloudflare Pages. No draft/preview step exists in current practice.
- Before pushing a change to the shared style block or header/footer partials, spot-check both a custom-built and a template-tier page.
- Prior commit history shows the working pattern is: **one calculator (or a small batch) per commit**, with descriptive commit messages (e.g. "Salary Calculator: add 4 advanced features..."). Keep following that granularity — don't batch unrelated pages into one commit.

## 10. Google AdSense compliance (added Jul 2026 — this site monetizes via AdSense, applies to every page)

The user has confirmed this site runs (or will run) Google AdSense. Every page built or upgraded from now on must stay compliant with Google's actual Program policies — sourced from `support.google.com/adsense`, not from third-party "how to get approved" blog posts, which often state invented numeric rules (e.g. "you need exactly 30 posts of 1,000 words") that aren't things Google itself publishes. Concretely, for every page:

- **Original, substantive content, never thin.** This is the same bar section 2 already sets (6+ H2s, transparent formulas, real depth) — it now does double duty as AdSense's own top content requirement. Never ship or leave a page as a bare tool with no surrounding content; that's the single most common AdSense rejection/disabling reason.
- **No keyword stuffing, no doorway pages, no claiming a feature the page doesn't have.** If a sentence describes what a linked or sibling page covers, verify that's actually true of the current state of that page before writing it (checked live during this session: an inline claim about another calculator's feature set was corrected after checking the actual page, since it was still a thin/generic page that didn't yet cover what was about to be claimed).
- **Essential trust pages must exist site-wide** (already present: `/privacy-policy/`, `/terms/`, `/about/`, `/contact/`) — don't remove or break links to these when touching shared header/footer partials.
- **No prohibited content categories** (adult, violent, hate speech, hacking/malware, drugs, etc.) — not generally a risk for calculator content, but stay aware of it if a future page ever touches an adjacent sensitive topic.
- **Financial/medical/legal calculators (YMYL content) keep clear disclaimers** that results are estimates, not professional advice — already standing practice on this site (e.g. the disclaimer paragraph at the end of every article) and doubles as an AdSense/Google-quality-guidelines trust signal. Keep it on every page.
- **Ad-placement readiness for whenever ads actually go live on a page:** don't design interactive controls (buttons, sliders, tabs) crammed into the very top-of-viewport / edge-of-container space in a way that would force an ad slot to sit flush against them later — Google's ad-placement policy expects clear separation between ads and interactive elements, and disallows ads mimicking content or sitting under misleading headings. This doesn't require adding ad-slot placeholders now, just not painting the layout into a corner.
- **`ads.txt`**: once the user has an AdSense publisher ID, an `ads.txt` file needs to exist at the domain root (`https://calculatorboss.com/ads.txt`) listing it — this doesn't exist yet in this repo as of Jul 2026. Flag this to the user rather than inventing a placeholder publisher ID; it must come from their real AdSense account.
- **Mobile-friendliness and load speed** — already covered by the section 3 checklist and the site's static-HTML/lazy-PDF conventions; both are also things Google's ad quality and Search ranking systems reward independent of AdSense specifically.
- Google can and does change these policies; if AdSense compliance becomes a point of dispute or a specific rejection reason comes back from Google, re-check `support.google.com/adsense/answer/48182` (Program policies) and `support.google.com/adsense/answer/9724` (Eligibility requirements) live rather than relying on this summary indefinitely.
