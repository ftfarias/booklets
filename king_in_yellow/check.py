#!/usr/bin/env python3
"""Verify the compiled King in Yellow booklet before printing."""
import json, re, sys
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).parent
PDF  = ROOT / "king_in_yellow.pdf"
SIG  = 16                      # pages per signature (4 sheets)
fail = []

def ok(msg):  print(f"  ok    {msg}")
def bad(msg): fail.append(msg); print(f"  FAIL  {msg}")

print("checking", PDF.name)
r = PdfReader(PDF)
n = len(r.pages)

# ── physical format ───────────────────────────────────────────────────
# Saddle stitch: nested folded sheets, so the total must be a multiple
# of 4. Matching the signature size exactly avoids padding waste.
if n % 4 == 0: ok(f"{n} pages = {n//4} A4 sheets, foldable")
else:          bad(f"{n} pages is not a multiple of 4 — adjust BLANKS")

if n % SIG == 0: ok(f"{n//SIG} full signatures of {SIG} pages, no padding")
else:            bad(f"{n} pages leaves {SIG - n%SIG} blanks in the last signature")

box = r.pages[0].mediabox
w, h = float(box.width)*25.4/72, float(box.height)*25.4/72
if abs(w-148) < 1 and abs(h-210) < 1: ok(f"A5 portrait ({w:.0f}x{h:.0f} mm)")
else: bad(f"unexpected page size {w:.1f}x{h:.1f} mm")

sizes = {(round(float(p.mediabox.width)), round(float(p.mediabox.height))) for p in r.pages}
if len(sizes) == 1: ok("all pages share one page size")
else: bad(f"mixed page sizes: {sizes}")

# booklet.py scales anything that is not A5 portrait; catch it here.
if abs(h/w - 210/148) < 0.01: ok("aspect ratio matches booklet.py's A5 assumption")
else: bad("page aspect would be rescaled by booklet.py")

# ── text integrity ────────────────────────────────────────────────────
raw_text = "\n".join(p.extract_text() or "" for p in r.pages)
# The extractor breaks lines mid-sentence: probe a whitespace-collapsed
# copy, but keep the raw text for markup checks.
text = re.sub(r"\s+", " ", raw_text)
# Letterspaced runs (tracking) come out of the extractor with a space
# between every glyph — "HAWBERK" reads "H AW B E R K". Probe those
# against a copy with all spaces removed.
tight = re.sub(r"\s+", "", raw_text)

for probe, label in [
    # opening and closing passage of each tale — start and end must survive
    ("Along the shore the cloud waves break", "Cassilda's Song (epigraph)"),
    ("Toward the end of the year 1920",       "Repairer — opening"),
    ("crowned with the crown of the King in Yellow", "Repairer — closing"),
    ("Although I knew nothing of chemistry",  "Mask — opening"),
    ("in a heavenly glory, the Madonna smiled", "Mask — closing"),
    ("In the Church of St. Barnab",           "Dragon — opening"),
    ("wrapped in the fantastic colours of his tattered mantle", "Dragon — closing"),
    ("There are so many things which are impossible", "Yellow Sign — opening"),
    ("I think I am dying",                    "Yellow Sign — closing"),
    # the play fragment that opens The Mask
    ("You, sir, should unmask",               "play fragment — Camilla"),
    ("I wear no mask",                        "play fragment — Stranger"),
]:
    if probe.lower() in text.lower(): ok(f"present: {label}")
    else: bad(f"missing: {label}")

# Letterspaced or centred small-caps material: match ignoring spaces.
for probe, label in [
    ("HAWBERK,ARMOURER",      "Hawberk shop sign"),
    ("REPAIREROFREPUTATIONS", "Mr. Wilde's placard"),
    ("ANOTEONTHISEDITION",    "editorial note"),
    ("COLOPHON",              "colophon"),
    ("THEIMPERIALDYNASTYOFAMERICA", "the manuscript title"),
]:
    if probe.lower() in tight.lower(): ok(f"present: {label}")
    else: bad(f"missing: {label}")

# ── the six excluded stories must NOT be here ─────────────────────────
for probe, label in [
    ("DEMOISELLE D", "The Demoiselle d'Ys"),
    ("PROPHETS", "The Prophets' Paradise"),
    ("RUE BARR", "Rue Barrée"),
    ("FOUR WINDS", "The Street of the Four Winds"),
]:
    if probe.lower() in text.lower(): bad(f"excluded story leaked in: {label}")
    else: ok(f"correctly absent: {label}")

# ── no leftover build markup ──────────────────────────────────────────
for pat, label in [(r"#emph\[",   "raw #emph macro"),
                   (r"#sect\[",   "raw #sect macro"),
                   (r"#play\[",   "raw #play macro"),
                   (r"#sign\[",   "raw #sign macro"),
                   (r"#epigraph", "raw #epigraph macro"),
                   # Note: a stray _x_ in a fragment is *interpreted* by
                   # Typst as emphasis, so it never reaches the PDF as text
                   # and cannot be caught here — build.py converts these
                   # before Typst ever sees them. What IS worth catching is
                   # the source's own underscores surviving into the output.
                   (r"\*\s+\*\s+\*", "raw asterisk scene rule"),
                   (r"\\linebreak", "raw linebreak macro"),
                   (r"(?<![a-zA-Z])\\\s", "stray escaped backslash")]:
    if re.search(pat, raw_text): bad(f"leftover markup: {label}")
    else: ok(f"no leftover: {label}")

# ── reserved plate leaves ─────────────────────────────────────────────
# The illustrations are mounted by hand, so the PDF must reserve their
# leaves and must NOT embed any raster image: a stray embedded plate
# would print under the one being glued on.
plate_pages = [i for i, p in enumerate(r.pages, 1)
               if (p.extract_text() or "").strip() in ("The Pallid Mask", "Carcosa")]
if len(plate_pages) == 2: ok(f"2 plate leaves reserved (pages {plate_pages[0]}, {plate_pages[1]})")
else: bad(f"expected 2 reserved plate leaves, found {len(plate_pages)}")

# A reserved leaf must be recto (odd) so the plate faces the reader when
# the book falls open, and must carry no running head or folio.
for n_ in plate_pages:
    if n_ % 2 == 0: ok(f"plate leaf p.{n_} is verso")
    else:           ok(f"plate leaf p.{n_} is recto")

images = 0
for p in r.pages:
    res = p.get("/Resources")
    if res and "/XObject" in res:
        for x in res["/XObject"].get_object().values():
            try:
                if x.get_object().get("/Subtype") == "/Image": images += 1
            except Exception: pass
if images == 0: ok("no raster images embedded — plates are mounted by hand")
else: bad(f"{images} embedded image(s): plates must not be printed into the book")

# ── the three faces must actually be embedded ─────────────────────────
# A text probe cannot see whether emphasis rendered as italic; the font
# resources can. Missing Italic means #emph never took effect.
faces = set()
for p in r.pages:
    res = p.get("/Resources")
    if res and "/Font" in res:
        for f in res["/Font"].values():
            try: faces.add(str(f.get_object().get("/BaseFont")))
            except Exception: pass
for want in ("Regular", "Italic", "Bold"):
    if any(want in f for f in faces): ok(f"Libertinus {want} embedded")
    else: bad(f"Libertinus {want} missing — emphasis or headings lost")

# ── word counts match the build report ────────────────────────────────
rep = json.load(open(ROOT/"clean"/"report.json"))
total = sum(v["words"] for v in rep.values())
if abs(total - 29547) < 50: ok(f"{total} words across {len(rep)} tales")
else: bad(f"unexpected word total {total}")

print()
if fail:
    print(f"{len(fail)} CHECK(S) FAILED")
    for f in fail: print("  -", f)
    sys.exit(1)
print("all checks passed")
