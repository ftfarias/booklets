#!/usr/bin/env python3
"""Verify the compiled Devocionário before printing."""
import json, re, sys, unicodedata
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).parent
PDF = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "devocionario.pdf"
SIG = 16          # pages per signature: 2 nested A4 quartos (quarto.py default)
fail = []

def ok(msg):  print(f"  ok    {msg}")
def bad(msg): fail.append(msg); print(f"  FAIL  {msg}")

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"-\s+-", "-", s)      # PT repeats the hyphen on a new line
    return re.sub(r"\s+", " ", s).strip().lower()

print("checking", PDF.name)
r = PdfReader(PDF)
n = len(r.pages)
pages = [norm(p.extract_text() or "") for p in r.pages]

# ── physical format ───────────────────────────────────────────────────
if n % SIG == 0: ok(f"{n} pages = {n // SIG} signatures of {SIG} = {n // 8} A4 sheets in quarto")
else:            bad(f"{n} pages is not a multiple of {SIG} — set PAD to {(-n) % SIG + 0} more (devocionario.typ)")

sizes = {(round(float(p.mediabox.width) * 25.4 / 72), round(float(p.mediabox.height) * 25.4 / 72))
         for p in r.pages}
if sizes == {(105, 148)} or sizes == {(105, 149)}: ok("all pages A6 portrait 105x148.5 mm (quarto.py, 4 per A4 side)")
else:                     bad(f"unexpected page sizes {sizes}")

# ── every Latin/PT pair on the two pages of ONE spread ────────────────
# Units are searched in order, each from the page where the previous one
# was found, so repeated incipits (Ps 41, 6 and 12) resolve correctly.
man = json.load(open(ROOT / "work" / "manifest.json", encoding="utf-8"))
cur, broken = 0, []
for lat, pt in man:
    L, P = norm(lat), norm(pt)
    p = next((i for i in range(cur, n) if L in pages[i]), None)
    if p is None:
        broken.append(f"Latin not found: {lat!r}"); continue
    pageno = p + 1
    if pageno % 2 != 0:
        broken.append(f"Latin on odd page {pageno}: {lat!r}")
    elif p + 1 >= n or P not in pages[p + 1]:
        broken.append(f"PT not facing Latin (p.{pageno}→{pageno + 1}): {pt!r}")
    cur = p
if not broken: ok(f"{len(man)} generated verse pairs: Latin on verso, PT on facing recto")
else:
    for b in broken[:10]: bad(b)

# Hand-set spreads (prayers, novena): spot-check the same rule.
for left, right, label in [
    ("Pater noster, qui es in caelis", "Pai nosso, que estais nos céus", "Pater / Pai-Nosso"),
    ("Credo in Deum", "Creio em Deus Pai", "Credo"),
    ("Salve, Regina", "Salve, Rainha", "Salve Regina"),
    ("Modus recitandi Rosarium", "Como se reza o terço", "how to pray"),
    ("Oratio post Rosarium", "Oração depois do terço", "closing prayer"),
    ("picchiate e vi sarà aperto", "pedi e obtereis", "Novena I (card text: picchiate)"),
    ("ma le mie parole mai", "minhas palavras jamais", "Novena III"),
    ("San Giuseppe, padre putativo", "São José, pai adotivo", "Novena closing"),
]:
    li = [i for i in range(n) if norm(left) in pages[i]]
    if not li: bad(f"missing: {label}"); continue
    i = li[0]
    if (i + 1) % 2 == 0 and i + 1 < n and norm(right) in pages[i + 1]:
        ok(f"facing pages {i + 1}–{i + 2}: {label}")
    else:
        bad(f"{label}: left on p.{i + 1}, right not on the facing recto")

# ── landmarks ─────────────────────────────────────────────────────────
alltext = " ".join(pages)
for probe, label in [
    ("livro de orações", "title page"),
    ("adhuc multiplicabuntur in senecta uberi", "dedication mote (Ps 91,15)"),
    ("numa velhice cumulada de bens", "dedication mote, PT"),
    ("dominus regit me", "Ps 22 Latin"),
    ("o senhor é quem me conduz", "Ps 22 PT"),
    ("miserere mei, deus", "Ps 50 Latin"),
    ("de profundis clamavi", "Ps 129 Latin"),
    ("omnis spiritus laudet dominum", "Ps 150 last verse"),
    ("magnificat anima mea dominum", "Magnificat"),
    ("a abraão e à sua posteridade para sempre", "Magnificat, last verse PT"),
    ("compilado e encadernado à mão por", "colophon"),
    ("pulsate, et aperietur vobis", "colophon mote"),
]:
    if norm(probe) in alltext: ok(f"present: {label}")
    else:                      bad(f"missing: {label}")

# ── index points at the right pages ───────────────────────────────────
idx = next((i for i in range(n) if "índice" in pages[i]), None)
if idx is None: bad("index page missing")
else:
    entries = re.findall(r"([a-zà-ú][a-zà-ú ,]+?)[ .]{6,}(\d+)", pages[idx])
    wrong = []
    for title, pg in entries:
        t, k = title.strip(), int(pg)
        # small caps extract letter-spaced ("m i s t é r i o s"): compare
        # with all spaces removed, on the spread (this page + facing one)
        t = t.removeprefix("índice").replace(" ", "")
        spread_txt = (pages[k - 1] + (pages[k] if k < n else "")).replace(" ", "") if k <= n else ""
        # "Salmos" heads the section; its first page says "Salmo 22"
        if t not in spread_txt and t.rstrip("s") not in spread_txt:
            wrong.append(f"{t!r} → p.{k}")
    if len(entries) >= 15 and not wrong: ok(f"index: {len(entries)} entries, each found on its page")
    else: bad(f"index: {len(entries)} entries parsed; wrong: {wrong[:5]}")

# ── personalisation and leaks ─────────────────────────────────────────
start = next(i for i in range(n) if "in nomine patris" in pages[i])
body = " ".join(pages[start:])
if "⟨nome⟩" in alltext: bad("placeholder ⟨NOME⟩ still in the book — set NOME in devocionario.typ")
else:                   ok("name filled in")

for pat, label in [(r"#\w", "Typst '#' call"), (r"\bvn\(", "vn( helper"),
                   (r'\\"', "escaped quote"), (r"\[|\]", "square bracket (strophe marker)"),
                   (r"[✠℣℟]", "glyph missing from Libertinus (renders as tofu)"),
                   (r"\bhe\b|\bhuma\b|\bdeos\b|\bhum\b", "unmodernised 1828 spelling")]:
    # The introduction quotes "he"/"Deos" on purpose and hyphenates; the
    # spelling probe only looks at the prayer and scripture pages.
    hay = body if "1828" in label else alltext
    m = re.search(pat, hay)
    if m: bad(f"leak: {label} — …{alltext[max(0, m.start() - 30):m.end() + 30] if hay is alltext else hay[max(0, m.start() - 30):m.end() + 30]}…")
    else: ok(f"no {label}")

print()
if fail:
    print(f"{len(fail)} problem(s). Do not print.")
    sys.exit(1)
print("All checks passed.")
