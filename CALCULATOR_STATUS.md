# Calculator Status — RETRACTED, do not act on the earlier numbers

_Last updated 2026-08-02._

## What happened

An earlier version of this file claimed that **131 of 206 calculator pages did not work**.
**That number was wrong and has been withdrawn.** It came from an automated scan whose
method was faulty. Three successive attempts to fix the scanner each had a different bug,
and a controlled trial against hand-checked pages ended up agreeing only 4 times out of 12.
At that point the honest conclusion is not a smaller number — it is that **the site's true
working/broken split is currently unknown**.

No page was changed on the basis of the bad data. The site is byte-identical to where it
was before the scan began (tag `backup-before-percentage-fix`).

## Why the automation failed — worth knowing before trying again

1. **Results written into an `<input>` value do not appear in `innerText`.** The first scan
   fingerprinted `main.innerText` only, so every calculator that shows its answer in a field
   looked dead. This is what wrongly condemned `percentage-calculator`.

2. **Including the values you just typed makes everything look alive.** The second attempt
   added all control values to the fingerprint — including the ones the scanner had just
   changed — so all 206 pages 'passed'. A self-fulfilling test.

3. **Index-based before/after comparison breaks silently.** Comparing element *positions*
   across two different selector queries (one including `<select>`, one not) makes the
   scanner's own edits look like recomputed output.

4. **This is a React build, and a controlled input ignores a direct `.value` write.**
   Setting `el.value` in page JS does not update React state; only simulated typing
   (Playwright `fill()`) does. Any in-page nudge is therefore unreliable here.

5. Even after all four fixes, verdicts were **unstable between runs**, which points at
   timing and at which controls happen to get picked. Not trustworthy.

## What is actually established

- **`percentage-calculator` works.** Verified by hand with arithmetic that could not have
  been pre-baked into the markup: 37% of 250 → 92.5, 46 is 25% of 184 → 25, and 64
  increased by 96% → 125.44. All three correct. It recomputes as you type, which is why
  clicking Calculate changes nothing. **It does not need fixing.**

- **`scientific-calculator` is very likely non-functional.** Structural rather than
  behavioural evidence: 34 keypad buttons with no `id`s, no inline script referencing them,
  and no display element anywhere in the markup. Worth a human look before any work.

- **Five pages were confirmed broken by reading their source and have since been rebuilt**
  this session: `inflation-calculator`, `interest-calculator`, `interest-rate-calculator`,
  `irr-calculator`, `lease-calculator`. Each had no calculator JavaScript at all.

- Everything else: **unknown**. Do not treat any earlier list as evidence.

## A method that would actually work

The reliable check is the one used when building each calculator against a reference: feed
**known inputs and assert a known correct answer**. That cannot be generated automatically
for 206 pages without a per-page expected-value table. Two realistic options:

- Build that table gradually — one row per calculator, added as each page is worked on.
  Slow, but it accumulates into a real regression suite.
- Or hand-check a sample, in priority order (the six footer-linked calculators first, then
  whatever Search Console shows getting impressions), and accept that the rest is unknown
  until touched.

What should **not** happen again is a sitewide verdict from a generic scanner. The signal it
produces is too easy to get backwards, in both directions.
