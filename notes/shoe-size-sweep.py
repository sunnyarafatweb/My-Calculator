import random, re, sys, math, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

def h5(x):   # nearest half, halves away from zero; keeps -0.0 so "-0" survives
    v = x*2
    r = (math.floor(v+0.5) if v >= 0 else math.ceil(v-0.5))/2
    return math.copysign(r, x) if r == 0 else r
def w1(x):   # nearest whole
    return math.floor(x+0.5) if x >= 0 else math.ceil(x-0.5)
def fmt(v):
    # keep negative zero: absurd inputs make the reference print "-0"
    neg = math.copysign(1, v) < 0 and v == 0
    t = str(int(abs(v))) if float(v) == int(v) else str(abs(v))
    return ('-' if (v < 0 or neg) else '') + t

# Derived from the reference by inverting size -> foot length. Note these are quarter
# sizes (22.75, 9.75, 23.75, 10.75) while the reference's own article text states halves.
K = {'a': {'usw':21, 'usm':22, 'uk':23},
     'k': {'big_us':22.75, 'lit_us':9.75, 'big_uk':23.75, 'lit_uk':10.75},
     'i': {'lit_us':9.75, 'lit_uk':10.75}}

ORDER = ['usw','usm','uk','eu','jp','cn','fl']
LABEL = {'usw':'US/Canada women', 'usm':'US/Canada men', 'uk':'UK/India',
         'eu':'EU', 'jp':'Japan/Mexico', 'cn':'China'}

def lengths(ac, field, v, flu='in'):
    """Returns (inches, cm) computed natively for the source, so a metric entry is
       never round-tripped through inches - 10.75 cm coming back as 10.749999 shifts
       a half-size."""
    def frm_in(L): return (L, L*2.54)
    def frm_cm(c): return (c/2.54, c)
    if field == 'fl':
        if flu == 'in': return frm_in(v)
        return frm_cm(v if flu == 'cm' else v/10)
    if field == 'usw': return frm_in((v + K['a']['usw'])/3)
    if field == 'usm':
        if ac == 'a': return frm_in((v + K['a']['usm'])/3)
        if ac == 'i': return frm_in((v + K['i']['lit_us'])/3)
        # a kid entry uses the big-kid scale only while it is inside that scale's range
        return frm_in((v + K['k']['big_us'])/3 if v <= 7 else (v + K['k']['lit_us'])/3)
    if field == 'uk':
        if ac == 'a': return frm_in((v + K['a']['uk'])/3)
        if ac == 'i': return frm_in((v + K['i']['lit_uk'])/3)
        return frm_in((v + K['k']['big_uk'])/3 if v <= 6 else (v + K['k']['lit_uk'])/3)
    if field == 'eu': return frm_cm((v - 2)/1.5)
    if field == 'jp': return frm_cm(v)
    return frm_cm((v + 10)/2)            # cn

OOS = 'out of scope'
def scoped(ac, field, v, big=True):
    """Adults enforce only a floor of 1; kids and infants only a ceiling."""
    if field == 'cn':
        return OOS if v < 5 else fmt(v)
    if field in ('eu','jp'):
        return fmt(v)
    if ac == 'a':
        return OOS if v < 1 else fmt(v)
    if v < 0:
        return OOS
    if ac == 'k':
        # the cap depends on which branch produced the value: the big-kid scale tops
        # out at 7 (US) or 6 (UK), the little-kid scale at 13.5
        cap = (7 if field == 'usm' else 6) if big else 13.5
        return OOS if v > cap else fmt(v)
    return OOS if v > 13.5 else fmt(v)

def sizes(ac, L, cm):
    out = {}
    if ac == 'a':
        out['usw'] = h5(3*L - K['a']['usw'])
        out['usm'] = h5(3*L - K['a']['usm'])
        out['uk']  = h5(3*L - K['a']['uk'])
    elif ac == 'k':
        big = 3*L - K['k']['big_us']
        out['usm'] = h5(big) if big >= 1 else h5(3*L - K['k']['lit_us'])
        out['_usm_big'] = big >= 1
        bigk = 3*L - K['k']['big_uk']
        out['uk'] = h5(bigk) if bigk >= 1 else h5(3*L - K['k']['lit_uk'])
        out['_uk_big'] = bigk >= 1
    else:
        out['usm'] = h5(3*L - K['i']['lit_us'])
        out['uk']  = h5(3*L - K['i']['lit_uk'])
    out['eu'] = w1(1.5*cm + 2)
    out['jp'] = h5(cm)
    out['cn'] = w1(2*cm - 10)
    return out

def engine(ac, field, v, flu='in'):
    # a source that implies a non-positive foot, or a kid/infant size past the top of
    # its scale, produces no result at all
    if ac in ('k','i') and field in ('usm','uk') and v > 13.5: return None
    L, cm = lengths(ac, field, v, flu)
    if L <= 0: return None
    s = sizes(ac, L, cm)
    rows = []
    for f in ['usw','usm','uk','eu','jp','cn']:
        if f not in s: continue
        # The source row is dropped - except UK in adult mode, where the reference
        # keeps it. That exception does not apply to kids or infants. Inconsistent,
        # reproduced for parity.
        if f == field and not (f == 'uk' and ac == 'a'): continue
        big = s.get('_'+f+'_big', True)
        rows.append((LABEL[f], scoped(ac, f, s[f], big)))
    d1 = lambda x: f"{w1(x*10)/10:.1f}"      # half-up at one decimal, not banker's
    rows.append(('Foot length', f"{d1(L)} inches {d1(cm)} cm {w1(cm*10)} mm"))
    return rows

def fetch(ac, field, v, flu='in'):
    p = {'ac':ac, 'usw':'', 'usm':'', 'uk':'', 'eu':'', 'jp':'', 'cn':'', 'fl':'', 'flu':flu, 'x':' Convert '}
    p[field] = v
    req = urllib.request.Request("https://www.calculator.net/shoe-size-conversion.html?"+urllib.parse.urlencode(p),
                                 headers={'User-Agent':'Mozilla/5.0 Chrome/120'})
    h = urllib.request.urlopen(req, timeout=30).read().decode('utf-8','replace')
    i = h.find('is equivalent to the following sizes')
    if i < 0: return None
    seg = h[i:h.find('</table>', i)]
    cells = [re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',c)).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', seg, re.S)]
    out = []
    for k in range(0, len(cells)-1, 2):
        lab = cells[k]
        for base in ('US/Canada women','US/Canada men','US/Canada kids','US/Canada infants/toddlers',
                     'UK/India kids','UK/India infants/toddlers','UK/India','EU','Japan/Mexico','China','Foot length'):
            if lab.startswith(base):
                lab = {'US/Canada kids':'US/Canada men','US/Canada infants/toddlers':'US/Canada men',
                       'UK/India kids':'UK/India','UK/India infants/toddlers':'UK/India'}.get(base, base)
                break
        out.append((lab, cells[k+1]))
    return out

def case(i):
    r = random.Random(i)
    ac = r.choice(['a','a','k','i'])
    if ac == 'a':
        field = r.choice(['usw','usm','uk','eu','jp','cn','fl'])
    else:
        field = r.choice(['usm','uk','eu','jp','cn','fl'])
    if field == 'fl':
        flu = r.choice(['in','cm','mm'])
        v = {'in': round(r.uniform(3.5, 13), 1), 'cm': round(r.uniform(9, 33), 1),
             'mm': r.randint(90, 330)}[flu]
    else:
        flu = 'in'
        rng = {'usw':(1,15), 'usm':(1,14) if ac=='a' else (1,13.5),
               'uk':(1,15) if ac=='a' else (1,13.5),
               'eu':(15,50), 'jp':(8,32), 'cn':(8,55)}[field]
        v = round(r.uniform(*rng)*2)/2
    return (ac, field, v, flu), engine(ac, field, float(v), flu), fetch(ac, field, v, flu)

N   = int(sys.argv[1]) if len(sys.argv) > 1 else 30
OFF = int(sys.argv[2]) if len(sys.argv) > 2 else 0
bad = 0
with ThreadPoolExecutor(max_workers=6) as ex:
    for args, mine, theirs in ex.map(case, range(OFF, OFF+N)):
        if theirs is None or mine is None:
            if theirs is None and mine is None: continue      # both refuse: agreement
            bad += 1
            print(f"REFUSAL MISMATCH {args}: mine={'None' if mine is None else 'result'} "
                  f"theirs={'None' if theirs is None else 'result'}")
            continue
        if mine != theirs:
            bad += 1
            print(f"MISMATCH {args}")
            for a, b in zip(mine, theirs):
                if a != b: print(f"    mine {a}\n    theirs {b}")
            if len(mine) != len(theirs):
                print(f"    row counts {len(mine)} vs {len(theirs)}")
print(f"\n{N} cases, {bad} mismatched")
