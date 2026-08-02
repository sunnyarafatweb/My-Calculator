# Calculator Status — which pages actually work

_Generated 2026-08-02 by a behavioural scan: each page is loaded, an input is changed, and the
page is checked for whether anything recomputes. This is deliberately not a code
heuristic — a page can be full of markup and compute nothing._

## Headline

| | count |
|---|---|
| Working (responds to input) | **75** |
| Not working | **131** |
| Total scanned | 206 |

Roughly **two thirds of the site does not compute anything**. The 485-line page template is
an almost perfect tell: 129 of the 131 broken pages are exactly 485 lines. The two
exceptions are listed below and matter more, because nothing about their size flags them.

## Act on these first

1. **`percentage-calculator` is broken and is linked from the shared footer on every one of
   the 214 pages.** It is one of only six calculators promoted sitewide, and it is the only
   one of those six that does not work. Every page on the site currently points visitors
   and crawlers at it.

2. **`age-calculator` (821 lines) and `percentage-calculator` (715 lines) are broken despite
   not being stubs.** Everything else broken is the 485-line template, so these two would
   never be caught by looking at page size.

3. **Six broken pages duplicate a working one.** Redirecting them is cheaper than building
   them, and removes near-duplicate thin content:

   - `crypto-profit-calculator` → `crypto-profit-loss-calculator`
   - `mortgage-amortization-calculator` → `amortization-calculator`
   - `payment-calculator` → `loan-calculator`
   - `repayment-calculator` → `loan-calculator`
   - `simple-interest-calculator` → `interest-calculator`
   - `roi-calculator` → `irr-calculator`

## Footer-promoted calculators

- `mortgage-calculator` — LIVE
- `loan-calculator` — LIVE
- `income-tax-calculator` — LIVE
- `bmi-calculator` — LIVE
- `percentage-calculator` — DEAD  **← broken**
- `compound-interest-calculator` — LIVE

## Working (75)

`401k-calculator`, `amortization-calculator`, `annuity-calculator`, `annuity-payout-calculator`, `apr-calculator`, `auto-lease-calculator`, `auto-loan-calculator`, `average-return-calculator`, `bitcoin-calculator`, `bmi-calculator`, `boat-loan-calculator`, `bond-calculator`, `bra-size-calculator`, `budget-calculator`, `business-loan-calculator`, `calorie-calculator`, `canadian-mortgage-calculator`, `cash-back-or-low-interest-calculator`, `cd-calculator`, `college-cost-calculator`, `commission-calculator`, `compound-interest-calculator`, `credit-card-calculator`, `credit-card-payoff-calculator`, `crypto-position-size-calculator`, `crypto-profit-loss-calculator`, `crypto-tax-calculator`, `currency-calculator`, `dca-calculator`, `debt-consolidation-calculator`, `debt-payoff-calculator`, `debt-to-income-calculator`, `depreciation-calculator`, `discount-calculator`, `down-payment-calculator`, `engine-horsepower-calculator`, `estate-tax-calculator`, `fat-intake-calculator`, `fha-loan-calculator`, `finance-calculator`, `future-value-calculator`, `gdp-calculator`, `gpa-calculator`, `grade-calculator`, `height-calculator`, `heloc-calculator`, `home-equity-loan-calculator`, `horsepower-calculator`, `house-affordability-calculator`, `income-tax-calculator`, `inflation-calculator`, `interest-calculator`, `interest-rate-calculator`, `investment-calculator`, `ira-calculator`, `irr-calculator`, `land-transfer-tax-calculator`, `lease-calculator`, `leverage-calculator`, `liquidation-price-calculator`, `loan-calculator`, `mining-profit-calculator`, `mortgage-calculator`, `profit-loss-calculator`, `rent-vs-buy-calculator`, `resistor-calculator`, `retirement-calculator`, `risk-reward-calculator`, `salary-calculator`, `sales-tax-calculator`, `savings-calculator`, `speed-calculator`, `staking-reward-calculator`, `time-zone-calculator`, `tip-calculator`

## Not working (131)

`age-calculator`, `army-body-fat-calculator`, `bac-calculator`, `bandwidth-calculator`, `base64-encode-decode`, `big-number-calculator`, `binary-calculator`, `bmr-calculator`, `body-fat-calculator`, `body-surface-area-calculator`, `body-type-calculator`, `btu-calculator`, `calories-burned-calculator`, `carbohydrate-calculator`, `conception-calculator`, `concrete-calculator`, `confidence-interval-calculator`, `conversion-calculator`, `crypto-profit-calculator`, `date-calculator`, `day-counter`, `day-of-the-week-calculator`, `density-calculator`, `dew-point-calculator`, `dice-roller`, `due-date-calculator`, `electricity-calculator`, `exponent-calculator`, `factor-calculator`, `fraction-calculator`, `fuel-cost-calculator`, `gas-mileage-calculator`, `gcf-calculator`, `gfr-calculator`, `golf-handicap-calculator`, `gravel-calculator`, `half-life-calculator`, `healthy-weight-calculator`, `heat-index-calculator`, `hex-calculator`, `hours-calculator`, `ideal-weight-calculator`, `ip-subnet-calculator`, `lcm-calculator`, `lean-body-mass-calculator`, `log-calculator`, `love-calculator`, `macro-calculator`, `margin-calculator`, `marriage-tax-calculator`, `mass-calculator`, `matrix-calculator`, `mean-median-mode-range-calculator`, `mileage-calculator`, `molarity-calculator`, `molecular-weight-calculator`, `mortgage-amortization-calculator`, `mortgage-calculator-uk`, `mortgage-payoff-calculator`, `mulch-calculator`, `mutual-fund-calculator`, `net-worth-calculator`, `number-sequence-calculator`, `ohms-law-calculator`, `one-rep-max-calculator`, `ovulation-calculator`, `pace-calculator`, `password-generator`, `payback-period-calculator`, `payment-calculator`, `pension-calculator`, `percent-error-calculator`, `percent-off-calculator`, `percentage-calculator`, `period-calculator`, `permutation-and-combination-calculator`, `personal-loan-calculator`, `pregnancy-calculator`, `pregnancy-conception-calculator`, `pregnancy-weight-gain-calculator`, `present-value-calculator`, `probability-calculator`, `protein-calculator`, `pythagorean-theorem-calculator`, `quadratic-formula-calculator`, `random-number-generator`, `ratio-calculator`, `real-estate-calculator`, `refinance-calculator`, `rent-calculator`, `rental-property-calculator`, `repayment-calculator`, `right-triangle-calculator`, `rmd-calculator`, `roi-calculator`, `roman-numeral-converter`, `roofing-calculator`, `root-calculator`, `roth-ira-calculator`, `rounding-calculator`, `sample-size-calculator`, `scientific-calculator`, `scientific-notation-calculator`, `shoe-size-conversion`, `simple-interest-calculator`, `sleep-calculator`, `slope-calculator`, `social-security-calculator`, `square-footage-calculator`, `stair-calculator`, `standard-deviation-calculator`, `statistics-calculator`, `student-loan-calculator`, `surface-area-calculator`, `take-home-paycheck-calculator`, `target-heart-rate-calculator`, `tdee-calculator`, `tile-calculator`, `time-calculator`, `time-card-calculator`, `time-duration-calculator`, `tire-size-calculator`, `triangle-calculator`, `url-encode-decode`, `va-mortgage-calculator`, `vat-calculator`, `voltage-drop-calculator`, `volume-calculator`, `weight-calculator`, `wind-chill-calculator`, `z-score-calculator`

## How to re-run

```
cd /repo && python3 -m http.server 8901 &
python3 scan_stubs.py            # or: scan_stubs.py START END to do it in chunks
```

The scanner lives in the working directory, not the repo. Verify any surprising verdict by
hand before acting on it — and compare the **whole** rendered text, not a truncated slice:
a first pass at hand-verification compared only the first 160 characters, which is the
breadcrumb and heading, and reported a working page as broken.
