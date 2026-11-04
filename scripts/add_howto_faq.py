# -*- coding: utf-8 -*-
"""Add the missing 'how is this calculated' FAQ to a page.

One question, worded the way people search it, answered in a few sentences with
the formula and a worked example. Goes into the visible article and the FAQPage
JSON-LD together, so an assistant and a search engine see the same thing.

Every number in these answers was verified in Node before being written.
"""
import io, re, json, sys

REPO = "/home/claude/repo"

FAQS = {
 'bmi-calculator': (
  "How is BMI calculated?",
  "BMI is your weight in kilograms divided by your height in metres squared. Someone who is "
  "70 kg and 1.75 m tall has a BMI of 70 divided by 3.0625, which is 22.9. In pounds and "
  "inches the formula is weight times 703, divided by height in inches squared: 154 lb at 68 "
  "inches gives 703 times 154 divided by 4,624, or 23.4. The two formulas describe the same "
  "measurement; the 703 simply converts the units."),

 'mortgage-calculator': (
  "How is a monthly mortgage payment calculated?",
  "Principal and interest come from the amortisation formula: the loan amount times the "
  "monthly rate, divided by one minus one plus that rate raised to minus the number of "
  "payments. On a 320,000 dollar loan at 6.5 percent over 30 years the monthly rate is "
  "0.065 divided by 12, and the payment works out at 2,022.62 dollars. Property tax, "
  "homeowners insurance, PMI and any HOA fee are added on top, which is why the figure a "
  "lender quotes is usually several hundred dollars higher than the loan portion alone."),

 'compound-interest-calculator': (
  "What is the compound interest formula?",
  "The balance equals the principal times one plus the rate divided by the number of "
  "compounding periods per year, all raised to the power of the periods per year times the "
  "number of years. One thousand dollars at 7 percent for 10 years grows to 1,967.15 dollars "
  "compounded annually, or 2,009.66 dollars compounded monthly. The gap between those two is "
  "the whole of what compounding frequency buys you, which is less than most people expect."),

 'tip-calculator': (
  "How do you calculate a 20 percent tip?",
  "Multiply the bill by 0.20, or move the decimal one place left to get 10 percent and double "
  "it. On a 48.50 dollar bill, 10 percent is 4.85, so 20 percent is 9.70 and the total comes "
  "to 58.20. For 15 percent, take the 10 percent figure and add half of it again. For 18 "
  "percent, take 20 percent and subtract a tenth of that. Doing it on the pre-tax subtotal is "
  "the usual convention in the United States."),

 'auto-loan-calculator': (
  "How is a car loan payment calculated?",
  "The same amortisation formula as any fixed instalment loan: the amount financed times the "
  "monthly rate, divided by one minus one plus that rate raised to minus the number of months. "
  "Twenty-five thousand dollars at 7.2 percent over 60 months gives a payment of 497.39 "
  "dollars. The amount financed is the price after your trade-in and down payment, plus any "
  "sales tax and fees rolled into the loan, which is why the payment is often higher than the "
  "sticker price alone suggests."),
}


def add(slug, question, answer, write=False):
    path = '%s/%s/index.html' % (REPO, slug)
    h = io.open(path, encoding='utf-8').read()
    if question in h:
        return '%-32s already present' % slug

    m = re.search(r'<h2 id="[a-z0-9\-]*faq"[^>]*>\s*Frequently Asked Questions\s*</h2>', h)
    if not m:
        m = re.search(r'<h2[^>]*>\s*Frequently Asked Questions\s*</h2>', h)
    if not m:
        return '%-32s NO FAQ HEADING' % slug
    head = m.group(0)
    if h.count(head) != 1:
        return '%-32s heading not unique' % slug

    h2 = h.replace(head, head + '\n<h3>%s</h3>\n<p>%s</p>\n' % (question, answer), 1)

    # The JSON-LD is minified on some pages and pretty-printed on others, so
    # work on the parsed object rather than on the text, and write it back in
    # whichever style that block already used.
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h2, re.S)
    target = None
    for b in blocks:
        try:
            o = json.loads(b)
        except Exception:
            continue
        if isinstance(o, dict) and o.get('@type') == 'FAQPage':
            target = (b, o)
            break
    if target is None:
        return '%-32s no parseable FAQPage' % slug

    raw, obj = target
    obj['mainEntity'].insert(0, {"@type": "Question", "name": question,
                                 "acceptedAnswer": {"@type": "Answer", "text": answer}})
    pretty = '\n' in raw.strip()
    new_raw = (json.dumps(obj, ensure_ascii=False, indent=2)
               if pretty else
               json.dumps(obj, ensure_ascii=False, separators=(',', ':')))
    if h2.count(raw) != 1:
        return '%-32s FAQ block not unique' % slug
    h2 = h2.replace(raw, new_raw, 1)

    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h2, re.S):
        try:
            json.loads(b)
        except Exception as e:
            return '%-32s WOULD BREAK JSON-LD: %s' % (slug, e)

    if write:
        io.open(path, 'w', encoding='utf-8').write(h2)
    return '%-32s ok' % slug


write = '--write' in sys.argv
for slug, (q, a) in FAQS.items():
    print(add(slug, q, a, write))
print('written' if write else '(dry run)')
