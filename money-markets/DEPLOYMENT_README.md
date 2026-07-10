# Calculator Boss — Site Structure & Deployment Guide

## What's in this package

```
calculatorboss-site/
├── index.html                              ← Home page (all 21 tools listed, search, categories)
├── break-even-calculator/index.html
├── cagr-calculator/index.html
├── compound-interest-calculator/index.html
├── crypto-position-size-calculator/index.html
├── crypto-profit-loss-calculator/index.html
├── crypto-tax-calculator/index.html
├── currency-converter/index.html
├── dca-calculator/index.html
├── dividend-yield-calculator/index.html
├── gold-value-calculator/index.html
├── investment-calculator/index.html
├── leverage-calculator/index.html
├── liquidation-price-calculator/index.html
├── mining-profit-calculator/index.html
├── pe-ratio-calculator/index.html
├── portfolio-allocation-calculator/index.html
├── risk-reward-calculator/index.html
├── roi-calculator/index.html
├── sip-calculator/index.html
├── staking-reward-calculator/index.html
└── stock-average-price-calculator/index.html
```

All 21 originally planned calculators are now live — DCA Calculator and ROI Calculator
(previously missing) have been added and fully connected.

## Why "folder/index.html" instead of "folder.html"?

Cloudflare Pages (and most static hosts) serve a clean URL like `/currency-converter/`
by looking for a file at `currency-converter/index.html`. If the file were instead named
`currency-converter.html`, the live URL would be `/currency-converter.html`, not
`/currency-converter/`. Every calculator here is already arranged the correct way —
just push this folder structure as-is.

## How to deploy

1. **Push to GitHub** — copy this entire folder structure into the root of your connected
   GitHub repo (the same repo Cloudflare Pages auto-deploys from). Commit and push.
2. **Cloudflare Pages auto-builds** — since it's already connected, the push triggers a
   deploy automatically. No build command needed (this is plain static HTML — build
   command can stay empty, output directory is `/` or wherever you place this folder).
3. **Check the live URLs** — `https://your-domain/`, `https://your-domain/currency-converter/`,
   etc. should all resolve correctly.
4. **Custom domain** — once `calculatorboss.com` is connected in Cloudflare Pages, no file
   changes are needed. All internal links are relative (`../`, `./`), so the site works
   identically on the `.pages.dev` subdomain now and on the custom domain later. Only the
   `<link rel="canonical">`, Open Graph, and JSON-LD tags in each file hardcode
   `calculatorboss.com` — that's intentional and correct for SEO once the domain is live.

## What changed from the original files

- **Brand name**: unified to "Calculator Boss" everywhere (the home page template had
  "CalcFolio" left over from an earlier draft).
- **Domain**: all internal navigation now uses relative paths (works on any domain);
  SEO tags (canonical/OG/schema) point to `calculatorboss.com` as agreed.
- **Hub pages**: `money-tools.html` and `all-calculators.html` were referenced in every
  calculator's nav/breadcrumb but never existed as separate files. Since the home page
  already covers search + all categories + all tools in one page, every calculator now
  links to `index.html` for both instead of two extra near-duplicate pages. Nav and
  breadcrumbs were simplified accordingly (removed the redundant middle crumb).
- **Dead links removed**: the original files linked to 6 calculators that don't exist yet
  — **DCA Calculator**, **ROI Calculator**, **Savings Goal**, **Retirement**, **Loan/
  Amortization**, and **Simple Interest** calculators. Every one of those links has been
  replaced with a real, working calculator instead, so nothing 404s.
- **Tool count corrected**: hero text and stat chips now say **21**, matching every
  calculator that's actually live and linked.

## DCA Calculator and ROI Calculator — now built

Both calculators that were referenced but missing in the first pass have been built and
connected the same way as the other 19:
- **DCA Calculator** (`dca-calculator/`) — backtests dollar-cost averaging against real
  historical crypto prices, with a live CoinGecko price feed and lump-sum comparison.
- **ROI Calculator** (`roi-calculator/`) — total ROI, annualized ROI, a target-value
  solver, and a side-by-side investment comparison tool.

Both went through the same fixes as the rest of the site (brand name, relative links,
SEO tags, dead-link cleanup) before being added to the home page and folder structure.
