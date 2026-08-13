#!/usr/bin/env python3
"""Structural checks for scientific-calculator.

These exist because two real bugs shipped that every behavioural suite missed:

  1. Five digit keys were dead. The suites called press() directly; the bug was
     one layer above, in the DOM-facing hit(). So: assert against the rendered
     ATTRIBUTES, the way a click actually resolves.
  2. Variables and History fell out of the grid entirely. The CSS was perfect and
     deployed; a stray </div> closed the container early. So: assert the DOM TREE,
     not the stylesheet.

Both were obvious in a screenshot and invisible to 8,000 numeric assertions.
"""
import re, sys
from html.parser import HTMLParser

PAGE = "scientific-calculator/index.html"
w = open(PAGE, encoding="utf-8").read()
main = re.search(r"<main.*?</main>", w, re.S).group(0)
css = re.search(r"<style>(.*?)</style>", main, re.S).group(1)

passed = failed = 0
def check(name, cond, detail=""):
    global passed, failed
    if cond: passed += 1; print(f"  [PASS] {name}")
    else:    failed += 1; print(f"  [FAIL] {name}  {detail}")

# ---------------------------------------------------------------- DOM tree
class Tree(HTMLParser):
    VOID = {"br","img","meta","link","input","hr","source","area","base","col","embed","param","track","wbr"}
    def __init__(self):
        super().__init__(); self.stack=[]; self.parents={}; self.unclosed=[]
    def handle_starttag(self, tag, attrs):
        if tag in self.VOID: return
        cls = dict(attrs).get("class","")
        self.stack.append((tag, cls))
        for c in cls.split():
            self.parents.setdefault(c, [a for _, a in self.stack[:-1]])
    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]; return
tree = Tree(); tree.feed(main)

print("=== container tree ===")
for col in ("sci-unit", "sci-vars", "sci-hist", "sci-bottom"):
    anc = tree.parents.get(col)
    check(f"{col} sits inside .sci-grid",
          anc is not None and any("sci-grid" in (a or "").split() for a in anc),
          f"ancestors={anc}")
art = tree.parents.get("sci-article")
check("article is OUTSIDE the grid",
      art is not None and not any("sci-grid" in (a or "").split() for a in art),
      f"ancestors={art}")
check("no unclosed tags in <main>", not tree.stack, f"left open: {tree.stack}")

# div balance, ignoring script/style/comment text
clean = re.sub(r"<style>.*?</style>", "", main, flags=re.S)
clean = re.sub(r"<script.*?</script>", "", clean, flags=re.S)
clean = re.sub(r"<!--.*?-->", "", clean, flags=re.S)
depth = 0; went_negative = False
for m in re.finditer(r"<div\b|</div>", clean):
    depth += 1 if m.group(0).startswith("<div") else -1
    if depth < 0: went_negative = True
check("div depth returns to zero", depth == 0, f"ends at {depth}")
check("div depth never goes negative", not went_negative)

# ---------------------------------------------------------------- grid areas
print("\n=== grid areas ===")
used = set(re.findall(r"grid-area:([a-z]+)", css))
for m in re.finditer(r"grid-template-areas:((?:\"[^\"]*\"\s*)+)", css):
    named = set(" ".join(re.findall(r'"([^"]*)"', m.group(1))).split())
    bp = re.findall(r"@media\(max-width:(\d+)px\)", css[:m.start()])
    label = f"@{bp[-1]}px" if bp else "desktop"
    check(f"{label} names every positioned area", not (used - named),
          f"missing {sorted(used - named)}")

# ---------------------------------------------------------------- keys
print("\n=== keypad ===")
buttons = re.findall(r"<button[^>]*data-k=\"([^\"]+)\"[^>]*>", main)
tags = {m.group(1): m.group(0) for m in re.finditer(r"<button[^>]*data-k=\"([^\"]+)\"[^>]*>", main)}
for d in list("0123456789") + ["."]:
    t = tags.get(d, "")
    check(f"key {d} is not blocked", bool(t) and "data-soon=" not in t,
          "data-soon would make hit() refuse the press")
for op in ["+", "-", "*", "/", "="]:
    t = tags.get(op, "")
    check(f"operator {op} is not blocked", bool(t) and "data-soon=" not in t)
check("every key with data-soon-s still has a working primary",
      all("data-soon=" not in t for k, t in tags.items() if "data-soon-s=" in t))

soon = [k for k, t in tags.items() if "data-soon=" in t]
print(f"         (deliberately unbuilt primaries: {', '.join(soon) or 'none'})")

# ---------------------------------------------------------------- ids the script needs
print("\n=== elements the script looks up ===")
script = re.search(r"<script>\n\(function\(\)\{(.*?)\n\}\)\(\);\n</script>", main, re.S).group(1)
wanted = set(re.findall(r"getElementById\('([^']+)'\)", script))
present = set(re.findall(r'id="([^"]+)"', main))
missing = sorted(w for w in wanted if w not in present)
check("every getElementById target exists in the markup", not missing, f"missing {missing}")

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
