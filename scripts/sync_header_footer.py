#!/usr/bin/env python3
"""
Sync header/footer from index.html (homepage) to every other page on the site.

Homepage's <header>...</header> and <footer>...</footer> are the canonical
source of truth. Run this any time index.html's header or footer changes,
and every other index.html on the site gets updated to match exactly.

Usage:
    python3 scripts/sync_header_footer.py

Also runs automatically via .github/workflows/sync-header-footer.yml
whenever index.html is pushed to main.
"""
import glob
import sys


def extract_block(html: str, tag: str):
    open_tag = f"<{tag}>"
    close_tag = f"</{tag}>"
    i = html.find(open_tag)
    j = html.find(close_tag)
    if i == -1 or j == -1:
        return None
    return html[i:j + len(close_tag)]


def main():
    home = open("index.html", encoding="utf-8").read()
    canonical_header = extract_block(home, "header")
    canonical_footer = extract_block(home, "footer")

    if not canonical_header or not canonical_footer:
        print("ERROR: could not find <header> or <footer> in index.html — aborting.")
        sys.exit(1)

    files = [f for f in glob.glob("**/index.html", recursive=True) if f != "index.html"]

    changed = []
    skipped_no_header = []

    for f in files:
        c = open(f, encoding="utf-8").read()
        page_header = extract_block(c, "header")
        page_footer = extract_block(c, "footer")

        if page_header is None and page_footer is None:
            skipped_no_header.append(f)
            continue

        new_c = c
        if page_header is not None and page_header != canonical_header:
            new_c = new_c.replace(page_header, canonical_header, 1)
        if page_footer is not None and page_footer != canonical_footer:
            new_c = new_c.replace(page_footer, canonical_footer, 1)

        if new_c != c:
            open(f, "w", encoding="utf-8").write(new_c)
            changed.append(f)

    print(f"Checked {len(files)} pages.")
    print(f"Updated: {len(changed)}")
    for f in changed:
        print(f"  - {f}")
    print(f"Skipped (no header/footer found, e.g. 404 pages): {len(skipped_no_header)}")

    return len(changed)


if __name__ == "__main__":
    main()
