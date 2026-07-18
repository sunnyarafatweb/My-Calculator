# Calculator Boss — Design & SEO Build Guide
*Last updated: 2026-07-18. This file is the persistent reference for how every calculator page on this site must be designed, written, and SEO-optimized. Read this in full before building or upgrading any page.*

---

## 0. Site facts (don't relearn these every time)

- **Stack:** Next.js, statically exported (`next export`-style output). The **built HTML/CSS/JS output lives directly in the repo root** — there is no `src/` or `package.json` in this repo. You edit the exported `index.html` files directly.
- **Hosting:** Cloudflare Pages, connected directly to this GitHub repo. **Any push to `main` deploys live instantly** — there is no staging/preview step in the normal workflow. Treat every commit as a production release.
- **Brand name:** Calculator Boss (`calculatorboss.com`).
- **Total calculator pages:** ~199 folders as of this writing.
- **Two tiers of pages currently exist:**
  1. **Custom-built pages** (e.g. `mortgage-calculator`, `bmi-calculator`, `savings-calculator`, `tip-calculator`) — deep content, bespoke interactive calculator UI (charts, multi-field forms), full SEO treatment. ~1000–2000 lines of HTML.
  2. **Template/generic pages** (e.g. `body-fat-calculator`) — thinner content, simpler generic title tag (`X Calculator | Calculator Boss`), fewer FAQ items, less topical depth. ~400–600 lines.
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
- [ ] `<title>`: **"[Calculator Name] — [specific benefit/outcome, not just a keyword restate]"**. Pattern from reference pages: *"Mortgage Calculator — See Your True Monthly Payment"*, *"BMI Calculator – See Your Healthy Weight Range"*, *"Savings Calculator – See When You'll Reach Your Goal"*. Write for **click-through**, not just impression — it should promise a specific outcome the searcher gets, not just name the tool. Avoid the generic `X Calculator | Calculator Boss` pattern found on template pages — replace it during upgrades.
- [ ] `meta description`: benefit-first sentence + trust/friction-removal cues (free / instant / no signup) + a specifics hook (what it accounts for, e.g. "principal, interest, taxes, insurance and PMI"). ~150–160 characters.
- [ ] `meta keywords`: include primary term + 4–6 close variants (harmless legacy tag, keep for consistency with existing pages).
- [ ] `canonical` URL set to the trailing-slash production URL.
- [ ] `robots` + `googlebot` tags: `index, follow, max-image-preview:large, max-snippet:-1` (as currently set).
- [ ] Open Graph + Twitter card tags mirroring title/description, plus an `og:image` (1200×630) — confirm an image exists at `/og/[slug].png` or generate one; don't ship a page with a broken OG image.

### Structured data (JSON-LD) — required on every page
- [ ] `BreadcrumbList` (Home → Category → This calculator)
- [ ] `FAQPage` with every FAQ question/answer that's also visibly rendered on the page (schema must match visible content — mismatches risk manual action / rich-result loss)
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

## 4. Keyword targeting approach (no Search Console access in this workflow)

Claude does not have a connected Google Search Console integration in this environment, so per-page GSC impression/CTR/query data can't be pulled directly here. Until that's connected, the substitute process for each calculator page is:
1. Web-search the calculator's core term to identify **short-tail head term** volume/competition proxies (who ranks, what content depth they have, what PAA questions show).
2. Web-search 3–5 **long-tail variants** (e.g. "mortgage calculator with taxes and insurance", "mortgage calculator extra payment") to find lower-competition, high-intent phrasing to weave into H2s/FAQs.
3. Prioritize **high-volume head terms for long-term ranking targets**, and **lower-competition long-tail phrasing for near-term rankability** (since this is a new site with limited authority) — target both in the same page rather than picking one.
4. If/when the user connects Google Search Console (check `search_mcp_registry` for a connector, or the user exports GSC data manually), switch to real query/impression data as the primary signal and treat the web-search method as a fallback.

---

## 5. The "3-card" pattern (current best-practice evolution)

Pages like `sales-tax-calculator` and `salary-calculator` represent a **leaner evolution** of the design system, superseding the older big-hero pattern (mortgage/bmi/savings-calculator). Use this 3-card pattern for all new/upgraded pages going forward:

- Simple header: `<h1>` + one-sentence subhead directly in the content wrapper (`<div class="px-4 sm:px-6 py-8 sm:py-10 mx-auto" style="max-width:1160px">`) — no big split hero/chart-preview section. Faster to ship, less CSS/markup weight, still on-brand.
- A CSS grid (`grid-template-areas:"bar bar ." "form result sidebar" "bottomgrid bottomgrid bottomgrid"`) with a page-specific class prefix (`tax-`, `cur-`, etc. — pick a short prefix per page to keep styles self-contained and easy to reason about):
  1. **bar** — thin navy status bar across the top (context line for the tool), with a white "💾 Save as PDF" button on the right (`justify-content:space-between`). This is now a standing pattern for every page — see loan-calculator and sales-tax-calculator for the reference implementation (jsPDF + jspdf-autotable via CDN, loaded with `defer`). Keep the bar's status text short enough to stay on one line next to the button at the bar's actual width (it spans 2 of the 3 grid columns, not the full page width) — a too-long sentence wraps the button onto its own line, which still works but doesn't match the reference layout.
  2. **form card** — inputs.
  3. **result card** — big-number output + supporting rows.
  4. **sidebar card** — a navy "related calculators" card (this *is* the visible internal-linking module — the earlier-noted gap is solved by this pattern; older hero-style pages still lack it and should get one when next touched).
  5. **bottomgrid** — two supporting cards (e.g. a breakdown/comparison card + a reference/glossary or fact-list card).
- Below the grid: `.{prefix}-seo-article` with a byline (`Written by the Calculator Boss Finance Team · Reviewed for accuracy · Last updated [Month Year]`), a table-of-contents nav linking to `<h2 id="...">` anchors, then the H2 sections + FAQ H3s, then a small disclaimer paragraph.
- Responsive: grid collapses to a single column under 860px; test both breakpoints.

## 6. Hard-won lessons (read before adding any live/external-data feature)

- **Always test third-party API calls from an actual browser context, not just curl/Node.** `curl`/Node's `fetch` do not enforce CORS, so a working curl response proves nothing about whether client-side JS in a real browser can read that response. Verify with `curl -sI -H "Origin: https://calculatorboss.com" <api-url>` and confirm an `access-control-allow-origin` header comes back — or better, load the real page in Playwright and check for zero console errors after the fetch resolves. (Concretely: `api.frankfurter.app`, the legacy currency-rate domain, sends **no** CORS header and silently fails in every browser; `api.frankfurter.dev` does send one and works. The original currency-calculator page was built against the broken domain — likely never worked for a real visitor.)
- Before pushing any page with live client-side data, run it through a local static server (`python3 -m http.server` from the repo root — note: background it with `setsid ... &` in its own command, since it must be started in the same tool invocation you use it in, or it gets killed) and a headless Playwright pass: check for zero console/page errors, confirm the result actually populates, and screenshot both desktop and a ~390px mobile width.
- When splicing a shared head/footer into a rebuilt page programmatically, diff the final file's shared `:root{...}.menu-btn{display:none}` block against another untouched page's identical block (`a == b` string compare) to prove the protected section wasn't corrupted — don't eyeball it.

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
