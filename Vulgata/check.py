#!/usr/bin/env python3
"""Verify the compiled Vulgata booklet before printing."""
import json, re, sys
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).parent
PDF  = ROOT / "vulgata.pdf"
fail = []

def ok(msg):   print(f"  ok    {msg}")
def bad(msg):  fail.append(msg); print(f"  FAIL  {msg}")

print("checking", PDF.name)
r = PdfReader(PDF)
n = len(r.pages)

# ── physical format ───────────────────────────────────────────────────
# One page per A4 side, stacked and stab-sewn: no folding, so a multiple
# of 4 is not required — only an even count, one sheet per two pages.
if n % 2 == 0: ok(f"{n} pages = {n//2} A4 sheets printed duplex")
else:          bad(f"{n} pages is odd — adjust PAD in vulgata.typ")

box = r.pages[0].mediabox
w, h = float(box.width)*25.4/72, float(box.height)*25.4/72
if abs(w-297) < 1 and abs(h-210) < 1: ok(f"A4 landscape ({w:.0f}x{h:.0f} mm)")
else: bad(f"unexpected page size {w:.1f}x{h:.1f} mm")

sizes = {(round(float(p.mediabox.width)), round(float(p.mediabox.height))) for p in r.pages}
if len(sizes) == 1: ok("all pages share one page size")
else: bad(f"mixed page sizes: {sizes}")

# ── text integrity ────────────────────────────────────────────────────
raw_text = "\n".join(p.extract_text() or "" for p in r.pages)
# The extractor breaks lines mid-sentence, so probe against a
# whitespace-collapsed copy; keep the raw text for markup checks.
text = re.sub(r"\s+", " ", raw_text)

for probe, label in [
    ("Vanitas vanitatum",            "Ecl. 1:2 Latin"),
    ("Omnia tempus habent",          "Ecl. 3:1 Latin"),
    ("Tudo tem a sua ocasi",         "Ecl. 3:1 Portuguese"),
    ("Osculetur me osculo oris sui", "Cant. 1:1 Latin"),
    ("fortis est ut mors dilectio",  "Cant. 8:6 Latin"),
    ("Si linguis hominum",           "1 Cor 13:1 Latin"),
    ("caritatem autem non habeam",   "1 Cor 13:1 Latin (cont.)"),
    ("major autem horum est caritas","1 Cor 13:13 Latin"),
    ("o maior destes é o amor",      "1 Cor 13:13 Portuguese"),
]:
    if probe.lower() in text.lower(): ok(f"present: {label}")
    else: bad(f"missing: {label}")

# ── source errata must have been applied ──────────────────────────────
for wrong, label in [("Voê", "OCR 'Voê' (should be 'Vê')"),
                     ("0s teus", "digit-zero 'Os teus'"),
                     ("a sua; própria", "stray semicolon in Ecl. 4:5")]:
    if wrong in text: bad(f"uncorrected source typo: {label}")
    else: ok(f"errata applied: {label}")

# ── no leftover build markup ──────────────────────────────────────────
for pat, label in [(r"#v_\(", "raw #v_() macro"),
                   (r"#chapnum", "raw #chapnum macro"),
                   (r"\[Vanitas", "unstripped strophe bracket")]:
    if re.search(pat, raw_text): bad(f"leftover markup: {label}")
    else: ok(f"no leftover: {label}")

# ── verse counts match the build report ───────────────────────────────
rep = json.load(open(ROOT/"clean"/"report.json"))
for slug, st in rep.items():
    if st["mismatch"]:
        bad(f"{slug}: {len(st['mismatch'])} chapters still misaligned")
    else:
        ok(f"{slug}: {st['verses']} verses, Latin/Portuguese fully aligned")

print()
if fail:
    print(f"{len(fail)} CHECK(S) FAILED")
    for f in fail: print("  -", f)
    sys.exit(1)
print("all checks passed")
