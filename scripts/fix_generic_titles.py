# -*- coding: utf-8 -*-
"""Replace the generic "X Calculator | CalculatorBoss" titles with benefit-first ones.

Each title promises the specific outcome the page actually delivers, taken from
that page's own subhead rather than invented. Target length 40-65 characters,
which is what the AdSense readiness checklist in DESIGN_AND_SEO_GUIDE.md sets.
og:title and twitter:title are kept in step with <title>.

Descriptions are left alone where they already sit in the 120-160 band; only the
short ones get a friction-removal clause added, which is the cue section 3 of the
guide asks for.
"""
import re, io, glob, os

REPO = "/home/claude/repo"

TITLES = {
 '401k-calculator': '401(k) Calculator — Project Your Balance at Retirement',
 'auto-loan-calculator': 'Auto Loan Calculator — Payment With Trade-In and Tax',
 'bandwidth-calculator': 'Bandwidth Calculator — How Long a Download Takes',
 'btu-calculator': 'BTU Calculator — The Right Size for Your Room',
 'calorie-calculator': 'Calorie Calculator — Daily Needs to Lose or Gain',
 'concrete-calculator': 'Concrete Calculator — Cubic Yards and Bags Needed',
 'confidence-interval-calculator': 'Confidence Interval Calculator — For a Sample Mean',
 'conversion-calculator': 'Unit Conversion Calculator — Length, Mass, Volume',
 'crypto-profit-loss-calculator': 'Crypto Profit / Loss Calculator — Fees and Real ROI',
 'date-calculator': 'Date Calculator — Add, Subtract or Count Between',
 'day-counter': 'Day Counter — How Many Days Between Two Dates',
 'day-of-the-week-calculator': 'Day of the Week Calculator — Any Date, Past or Future',
 'density-calculator': 'Density Calculator — Solve for Density, Mass or Volume',
 'dew-point-calculator': 'Dew Point Calculator — And How Humid It Really Feels',
 'dice-roller': 'Dice Roller — Roll Any Number of Dice Online',
 'electricity-calculator': 'Electricity Cost Calculator — Monthly Cost per Appliance',
 'exponent-calculator': 'Exponent Calculator — Negative and Fractional Powers',
 'factor-calculator': 'Factor Calculator — All Factors and Prime Factorization',
 'fuel-cost-calculator': 'Fuel Cost Calculator — What Your Trip Will Cost',
 'gas-mileage-calculator': 'Gas Mileage Calculator — Work Out Your Real MPG',
 'golf-handicap-calculator': 'Golf Handicap Calculator — Your WHS Handicap Index',
 'gpa-calculator': 'GPA Calculator — Weighted and Unweighted, Instantly',
 'grade-calculator': 'Grade Calculator — What You Need on the Final Exam',
 'gravel-calculator': 'Gravel Calculator — Tons and Cubic Yards to Order',
 'half-life-calculator': 'Half-Life Calculator — Solve Any Decay Variable',
 'heat-index-calculator': 'Heat Index Calculator — What the Heat Really Feels Like',
 'hex-calculator': 'Hex Calculator — Hexadecimal Math and Conversion',
 'hours-calculator': 'Hours Calculator — Hours Worked and Pay, With Breaks',
 'ip-subnet-calculator': 'IP Subnet Calculator — Full CIDR Breakdown',
 'log-calculator': 'Log Calculator — Any Base, Including ln and log₂',
 'love-calculator': 'Love Calculator — A Just-for-Fun Compatibility Score',
 'mass-calculator': 'Mass Converter — Convert Between Any Mass Units',
 'matrix-calculator': 'Matrix Calculator — Multiply, Invert and Find Determinants',
 'mean-median-mode-range-calculator': 'Mean, Median, Mode and Range — All Four at Once',
 'mileage-calculator': 'Mileage Calculator — IRS Reimbursement and Deduction',
 'molarity-calculator': 'Molarity Calculator — Concentration and Dilutions',
 'molecular-weight-calculator': 'Molecular Weight Calculator — From Any Chemical Formula',
 'mulch-calculator': 'Mulch Calculator — Cubic Yards and Bags to Order',
 'number-sequence-calculator': 'Number Sequence Calculator — Find the Pattern and Next Term',
 'ohms-law-calculator': "Ohm's Law Calculator — Solve for V, I, R or Power",
 'password-generator': 'Password Generator — Strong Passwords, Made Locally',
 'percent-error-calculator': 'Percent Error Calculator — Measured vs Accepted Value',
 'percent-off-calculator': 'Percent Off Calculator — Sale Price and What You Save',
 'permutation-and-combination-calculator': 'Permutation and Combination Calculator — nPr and nCr',
 'probability-calculator': 'Probability Calculator — AND, OR and Complement Events',
 'pythagorean-theorem-calculator': 'Pythagorean Theorem Calculator — Find Any Missing Side',
 'quadratic-formula-calculator': 'Quadratic Formula Calculator — Real and Complex Roots',
 'resistor-calculator': 'Resistor Color Code Calculator — Read Any Band Code',
 'retirement-calculator': 'Retirement Calculator — Will Your Savings Be Enough?',
 'right-triangle-calculator': 'Right Triangle Calculator — Solve From Any Two Values',
 'roman-numeral-converter': 'Roman Numeral Converter — Both Directions, Any Number',
 'roofing-calculator': 'Roofing Calculator — Roof Area, Squares and Bundles',
 'root-calculator': 'Root Calculator — Square, Cube and Any nth Root',
 'rounding-calculator': 'Rounding Calculator — To Decimals or Any Multiple',
 'sample-size-calculator': 'Sample Size Calculator — How Many Responses You Need',
 'scientific-notation-calculator': 'Scientific Notation Calculator — Convert Both Ways',
 'slope-calculator': 'Slope Calculator — Slope, Equation, Distance and Angle',
 'square-footage-calculator': 'Square Footage Calculator — Area and Material Cost',
 'stair-calculator': 'Stair Calculator — Risers, Treads and Stringer Length',
 'staking-reward-calculator': 'Staking Reward Calculator — Projected Crypto Rewards',
 'statistics-calculator': 'Statistics Calculator — Every Descriptive Stat at Once',
 'surface-area-calculator': 'Surface Area Calculator — For Every Common Shape',
 'tile-calculator': 'Tile Calculator — Exactly How Many Tiles to Buy',
 'time-calculator': 'Time Calculator — Add and Subtract Hours and Minutes',
 'time-card-calculator': 'Time Card Calculator — Weekly Hours and Pay',
 'time-duration-calculator': 'Time Duration Calculator — Between Two Dates and Times',
 'tip-calculator': 'Tip Calculator — Tip, Total and Split per Person',
 'tire-size-calculator': 'Tire Size Calculator — Compare Sizes and Speedo Error',
 'url-encode-decode': 'URL Encoder and Decoder — Percent-Encoding Both Ways',
 'voltage-drop-calculator': 'Voltage Drop Calculator — With NEC Compliance Check',
 'volume-calculator': 'Volume Calculator — For Every Common 3D Shape',
 'weight-calculator': 'Weight Calculator — Your Weight Anywhere in the System',
 'wind-chill-calculator': 'Wind Chill Calculator — What the Cold Really Feels Like',
 'z-score-calculator': 'Z-Score Calculator — Standard Deviations and Percentile',
}

# varied friction-removal tails, so 40 short descriptions do not all end alike
TAILS = [
    ' Free, instant, no sign-up needed.',
    ' Free to use, with no sign-up.',
    ' Instant results, nothing to install.',
    ' Free and instant, straight in your browser.',
    ' No sign-up, no download, instant answers.',
]


def esc(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;')


def main():
    changed = skipped = desc_fixed = 0
    report = []
    for i, (slug, title) in enumerate(sorted(TITLES.items())):
        f = os.path.join(REPO, slug, 'index.html')
        if not os.path.exists(f):
            report.append(('MISSING', slug, ''))
            continue
        h = io.open(f, encoding='utf-8', errors='replace').read()
        cur = re.search(r'<title>(.*?)</title>', h)
        if not cur:
            report.append(('NOTITLE', slug, ''))
            continue
        if not re.search(r'\| CalculatorBoss\s*$', cur.group(1)):
            skipped += 1
            report.append(('ALREADY', slug, cur.group(1)))
            continue
        t = esc(title)
        h = h.replace('<title>%s</title>' % cur.group(1), '<title>%s</title>' % t, 1)
        # keep the social titles in step
        h = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + t + m.group(2), h, count=1)
        h = re.sub(r'(<meta name="twitter:title" content=")[^"]*(")', lambda m: m.group(1) + t + m.group(2), h, count=1)

        d = re.search(r'<meta name="description" content="([^"]*)"', h)
        if d and len(d.group(1)) < 120:
            newd = d.group(1).rstrip()
            if not newd.endswith('.'):
                newd += '.'
            newd += TAILS[i % len(TAILS)]
            if len(newd) <= 160:
                h = h.replace('content="%s"' % d.group(1), 'content="%s"' % newd)
                desc_fixed += 1
        io.open(f, 'w', encoding='utf-8').write(h)
        changed += 1
        report.append(('OK', slug, title))

    print('titles rewritten :', changed)
    print('already specific :', skipped)
    print('descriptions grown:', desc_fixed)
    bad = [r for r in report if r[0] in ('MISSING', 'NOTITLE')]
    if bad:
        print('problems:', bad)


if __name__ == '__main__':
    main()
