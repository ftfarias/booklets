#!/usr/bin/env python3
"""Verify devocionario_imposto.pdf against the book before printing:
every A4 side must carry exactly the folios quarto.py's fold simulation
predicts for it (pages without a folio — blanks, title — are allowed to be
silent), and the sheet count must match."""
import re, sys
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT.parent))
import quarto  # noqa: E402

SHEETS = 2
book = PdfReader(ROOT / "devocionario.pdf")
imp = PdfReader(sys.argv[1] if len(sys.argv) > 1 else ROOT / "devocionario_imposto.pdf")
n, size = len(book.pages), 8 * SHEETS
fail = []

if len(imp.pages) != 2 * n // 8:
    fail.append(f"{len(imp.pages)} sides, expected {2 * n // 8}")
b = imp.pages[0].mediabox
if (round(float(b.width) * 25.4 / 72), round(float(b.height) * 25.4 / 72)) != (297, 210):
    fail.append("sides are not A4 landscape")

k, seen = 0, set()
for g in range(n // size):
    tab = quarto.signature_pages(g, SHEETS)
    for s in range(SHEETS):
        for side in "FB":
            exp = {tab[(s, p)] + 1 for p, (sd, *_) in quarto.LAYOUT.items() if sd == side}
            got = {int(x) for x in re.findall(r"^\s*(\d{1,3})\s*$", imp.pages[k].extract_text() or "", re.M)}
            if not got <= exp:
                fail.append(f"side {k + 1} (sig {g + 1}, sheet {s + 1}{side}): expected {sorted(exp)}, found {sorted(got)}")
            seen |= got
            k += 1

if len(seen) < 100:
    fail.append(f"only {len(seen)} folios found — imposition empty or text unreadable")

for f in fail: print("  FAIL ", f)
if fail: sys.exit(1)
print(f"  ok    {len(imp.pages)} sides = {len(imp.pages)//2} A4 sheets; {len(seen)} folios each on the predicted side")
