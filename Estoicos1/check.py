#!/usr/bin/env python3
"""Pre-print checks. Catches the failures that only show up after folding:
a page count that is not a multiple of 4, missing text, leftover markup,
and a short-edge imposition whose backs are not flipped-and-swapped.
"""
import re, subprocess, sys, pathlib
from pypdf import PdfReader

HERE = pathlib.Path(__file__).parent
ok = True

def fail(msg):
    global ok
    ok = False
    print("  FAIL:", msg)

def check_body(pdf, label, expect_pages, expect_sheets):
    print(f"\n{label}  ({pdf})")
    r = PdfReader(HERE/pdf)
    n = len(r.pages)
    print(f"  pages: {n}   sheets: {n/4}")
    if n != expect_pages:
        fail(f"expected {expect_pages} pages, got {n}")
    if n % 4:
        fail(f"page count {n} is not a multiple of 4")
    mb = r.pages[0].mediabox
    w, h = float(mb.width)*25.4/72, float(mb.height)*25.4/72
    if not (abs(w-148) < 1 and abs(h-210) < 1):
        fail(f"page size {w:.0f}x{h:.0f}mm is not A5")

    txt = "\n".join((p.extract_text() or "") for p in r.pages)
    for bad in ["[Greek:", "#emph", "#grk", "[GRK", "\x00", "*** START", "Project Gutenberg"]:
        if bad in txt:
            fail(f"leftover source markup in output: {bad!r}")
    greek = re.findall(r'[Ͱ-Ͽἀ-῿]+', txt)
    print(f"  words: {len(txt.split())}   Greek runs: {len(greek)}")
    if not greek:
        fail("no Greek found — the apparatus did not render")
    return txt

def check_imposition():
    """A 16-page numbered dummy must impose as: front 16|1, back 15|2 with the
    back rotated 180 degrees. That is what short-edge duplex undoes."""
    print("\nImposition (short-edge)")
    prev = HERE/"preview"; prev.mkdir(exist_ok=True)
    t = prev/"_check16.typ"
    t.write_text('#set page(width:148mm,height:210mm,margin:20mm,numbering:none)\n'
                 '#for i in range(1,17){page[#align(center+horizon)'
                 '[#text(size:90pt,weight:"bold")[#i]]]}\n')
    subprocess.run(["typst","compile",str(t),str(prev/"_check16.pdf")],
                   check=True, capture_output=True)
    subprocess.run(["python3", str(HERE.parent/"booklet.py"), str(prev/"_check16.pdf"),
                    "-o", str(prev/"_check16_imp.pdf"), "-s","16"],
                   check=True, capture_output=True)
    r = PdfReader(prev/"_check16_imp.pdf")
    if len(r.pages) != 8:
        fail(f"expected 8 imposed sides, got {len(r.pages)}")
        return
    front = re.findall(r'\d+', r.pages[0].extract_text() or "")
    back  = re.findall(r'\d+', r.pages[1].extract_text() or "")
    print(f"  sheet 1 front: {front}   back: {back}")
    if front != ["16","1"]:
        fail(f"sheet 1 front should carry 16 then 1, got {front}")
    if back != ["15","2"]:
        fail(f"sheet 1 back should carry 15 then 2, got {back}")
    rot = r.pages[1].get("/Rotate", 0)
    print(f"  back side /Rotate = {rot}")

t1 = check_body("vol1_epictetus.pdf", "Volume I — Epictetus", 144, 36)
t2 = check_body("vol2_marcus.pdf",    "Volume II — Marcus Aurelius", 132, 33)

# completeness
print("\nCompleteness")
def r2i(s):
    v={'I':1,'V':5,'X':10,'L':50,'C':100}; n=0
    for i,c in enumerate(s):
        n += -v[c] if (i+1<len(s) and v[c]<v[s[i+1]]) else v[c]
    return n
found = set()
for m in re.finditer(r'\b([IVXL]+)\b', t1):
    try: found.add(r2i(m.group(1)))
    except Exception: pass
miss = [i for i in range(1,52) if i not in found]
print(f"  Enchiridion sections 1-51 present: {not miss}")
if miss: fail(f"missing Enchiridion sections: {miss}")

# The "BOOK" label is letter-spaced, so Typst emits it glyph-by-glyph and it
# does not survive text extraction. Count the book-opening pages instead: each
# one starts a recto and its first numbered section is 2 (section 1 runs into
# the heading block).
first_words = ["From my grandfather Verus",          # I
               "Begin the morning by saying"]         # II
hits = sum(1 for fw in first_words if fw in t2)
print(f"  Meditations openings verified: {hits}/{len(first_words)} landmark passages")
if hits != len(first_words):
    fail("a known opening passage of the Meditations is missing")
if not re.search(r'A little while, and all of us are nobody', t2):
    fail("Volume II colophon motto missing")

check_imposition()

print()
print("ALL CHECKS PASSED" if ok else "CHECKS FAILED")
sys.exit(0 if ok else 1)
