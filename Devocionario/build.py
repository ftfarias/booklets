#!/usr/bin/env python3
"""
Build the generated Typst fragments of the Devocionário.
  Latin : Clementine Vulgate (raw/vul_raw.json, same source as Vulgata/)
  PT    : Pereira de Figueiredo, hand-cleaned in textos/biblia_pt.py

Emits typst/gen_misterios.typ, typst/gen_salmos.typ and
work/manifest.json (first words of every Latin/PT unit, in order, so
check.py can confirm on the compiled PDF that each pair sits on the two
pages of one spread).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "textos"))
from biblia_pt import PSALMS, PERICOPES  # noqa: E402

TYP, WORK = ROOT / "typst", ROOT / "work"
TYP.mkdir(exist_ok=True); WORK.mkdir(exist_ok=True)

VUL = json.load(open(ROOT / "raw" / "vul_raw.json", encoding="utf-8"))

ABBR = {  # book -> (Latin abbrev, Portuguese abbrev)
    "Luke": ("Lc", "Lc"), "Matthew": ("Mt", "Mt"), "Mark": ("Mc", "Mc"),
    "John": ("Io", "Jo"), "Acts": ("Act", "At"), "Revelation": ("Apc", "Ap"),
    "Song of Solomon": ("Ct", "Ct"), "Isaiah": ("Is", "Is"),
}

# Hebrew numbering, shown in parentheses (Vulgate first, as liturgical
# books print it).
HEBREW = {22: 23, 26: 27, 41: 42, 50: 51, 83: 84, 90: 91, 91: 92,
          102: 103, 120: 121, 129: 130, 150: 150}

# Psalm superscriptions in the Vulgate, as the Clementine prints them.
# The JSON folds them into verse 1 (or 1–2); they are split off here.
def latin_psalm(n):
    verses = [v for v in VUL["Psalms"][n - 1] if v.strip()]
    title, body = [], {}
    in_poem = False
    for i, v in enumerate(verses, 1):
        if not in_poem and "[" in v:
            pre, post = v.split("[", 1)
            if pre.strip():
                title.append(pre.strip())
            in_poem = True
            body[i] = clean(post)
        elif not in_poem:
            title.append(v.strip())
        else:
            body[i] = clean(v)
    return " ".join(title), body

def clean(v):
    v = v.replace("[", "").replace("]", "")
    return re.sub(r"\s+", " ", v).strip()

def latin_verse(book, ch, v):
    return clean(VUL[book][ch - 1][v - 1])

def tstr(s):
    """A Typst string literal: no markup is interpreted inside it."""
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

def roman(n):
    out = ""
    for a, r in [(100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"),
                 (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
        while n >= a:
            out += r; n -= a
    return out

def refstr(parts, lang):
    """parts: [(book, ch, [verses])] -> 'Lc 1, 28-31. 38'"""
    out = []
    for book, ch, vs in parts:
        runs, start, prev = [], vs[0], vs[0]
        for v in vs[1:] + [None]:
            if v is not None and v == prev + 1:
                prev = v; continue
            runs.append(f"{start}" if start == prev else f"{start}–{prev}")
            if v is not None:
                start = prev = v
        out.append(f"{ABBR[book][lang]} {ch}, " + ". ".join(runs))
    return "; ".join(out)

manifest = []

def unit(lat, pt, n=None):
    """One (left, right) unit; records probes for check.py."""
    manifest.append((first_words(lat), first_words(pt)))
    if n is None:
        return f"(par({tstr(lat)}), par({tstr(pt)}))"
    return f"(vn({n}, {tstr(lat)}), vn({n}, {tstr(pt)}))"

def first_words(s, k=5):
    return " ".join(s.split()[:k])

def pericope_units(parts):
    """Units for a selection of verses, with an elision mark at gaps."""
    out = []
    for pi, (book, ch, vs) in enumerate(parts):
        pt = PERICOPES[(book, ch)]
        prev = None
        if pi > 0:                 # a second book: mark the join
            out.append("(elide, elide)")
        for v in vs:
            if prev is not None and v != prev + 1:
                out.append("(elide, elide)")
            if v not in pt:
                raise SystemExit(f"missing Portuguese for {book} {ch}:{v}")
            out.append(unit(latin_verse(book, ch, v), pt[v], v))
            prev = v
    return out

# ── Rosary ────────────────────────────────────────────────────────────
MYSTERIA = [
  ("Mysteria Gaudiosa", "Mistérios Gozosos",
   "Feria secunda et sabbato", "Às segundas-feiras e aos sábados", [
    ("Annuntiatio", "A Anunciação do Anjo a Nossa Senhora", [("Luke", 1, [28, 29, 30, 31, 38])]),
    ("Visitatio", "A Visitação de Nossa Senhora a sua prima Santa Isabel", [("Luke", 1, [41, 42, 43, 44, 45])]),
    ("Nativitas", "O Nascimento de Jesus em Belém", [("Luke", 2, [6, 7])]),
    ("Praesentatio in templo", "A Apresentação do Menino Jesus no Templo", [("Luke", 2, [28, 29, 30, 31, 32])]),
    ("Inventio in templo", "A Perda e o Encontro do Menino Jesus no Templo", [("Luke", 2, [46, 47, 48, 49])]),
  ]),
  ("Mysteria Luminosa", "Mistérios Luminosos",
   "Feria quinta", "Às quintas-feiras", [
    ("Baptisma in Jordane", "O Batismo de Jesus no Jordão", [("Matthew", 3, [16, 17])]),
    ("Nuptiae in Cana", "As Bodas de Caná", [("John", 2, [3, 4, 5])]),
    ("Annuntiatio Regni Dei", "O Anúncio do Reino de Deus", [("Mark", 1, [14, 15])]),
    ("Transfiguratio", "A Transfiguração do Senhor", [("Matthew", 17, [1, 2, 5])]),
    ("Institutio Eucharistiae", "A Instituição da Eucaristia", [("Matthew", 26, [26, 27, 28])]),
  ]),
  ("Mysteria Dolorosa", "Mistérios Dolorosos",
   "Feria tertia et feria sexta", "Às terças e sextas-feiras", [
    ("Agonia in horto", "A Agonia de Jesus no Horto", [("Luke", 22, [41, 42, 43, 44])]),
    ("Flagellatio", "A Flagelação de Jesus", [("Mark", 15, [15]), ("Isaiah", 53, [5])]),
    ("Coronatio spinis", "A Coroação de Espinhos", [("Matthew", 27, [28, 29])]),
    ("Bajulatio crucis", "Jesus carregando a Cruz", [("John", 19, [16, 17])]),
    ("Crucifixio et mors", "A Crucificação e Morte de Jesus", [("John", 19, [25, 26, 27, 30])]),
  ]),
  ("Mysteria Gloriosa", "Mistérios Gloriosos",
   "Feria quarta et dominica", "Às quartas-feiras e aos domingos", [
    ("Resurrectio", "A Ressurreição de Jesus", [("Matthew", 28, [5, 6])]),
    ("Ascensio", "A Ascensão de Jesus ao Céu", [("Luke", 24, [50, 51])]),
    ("Descensus Spiritus Sancti", "A Vinda do Espírito Santo", [("Acts", 2, [1, 2, 3, 4])]),
    ("Assumptio", "A Assunção de Nossa Senhora", [("Song of Solomon", 2, [10, 11, 12])]),
    ("Coronatio in caelo", "A Coroação de Nossa Senhora no Céu", [("Revelation", 12, [1])]),
  ]),
]

def emit_mysteries():
    out = ['#import "helpers.typ": *', "",
           "// Generated by build.py — do not edit by hand.", ""]
    foot = ('(mfoot("Pater noster · decem Ave Maria · Gloria Patri · O mi Jesu"), '
            'mfoot("Pai-Nosso · dez Ave-Marias · Glória · Ó meu Jesus"))')
    for glat, gpt, dlat, dpt, items in MYSTERIA:
        for k, (nlat, npt, parts) in enumerate(items, 1):
            day_l = tstr(dlat) if k == 1 else "none"
            day_p = tstr(dpt) if k == 1 else "none"
            head = (f"(mhead({tstr(glat)}, {k}, {tstr(nlat)}, {tstr(refstr(parts, 0))}, {day_l}), "
                    f"mhead({tstr(gpt)}, {k}, {tstr(npt)}, {tstr(refstr(parts, 1))}, {day_p}))")
            units = pericope_units(parts)
            toc = f"((2, {tstr(gpt)}),)" if k == 1 else "()"
            out.append("#spread((")
            out += [f"  {u}," for u in units]
            out.append(f"), toc: {toc}, head: {head}, foot: {foot})")
            out.append("")
    (TYP / "gen_misterios.typ").write_text("\n".join(out), encoding="utf-8")

# ── Psalms ────────────────────────────────────────────────────────────
PSALM_ORDER = [22, 26, 41, 50, 83, 90, 91, 102, 120, 129, 150]

# Latin incipits, by which psalms have been known for centuries — the
# index lists them this way.
INCIPIT = {22: "Dominus regit me", 26: "Dominus illuminatio mea",
           41: "Quemadmodum desiderat cervus", 50: "Miserere mei, Deus",
           83: "Quam dilecta tabernacula tua", 90: "Qui habitat in adjutorio Altissimi",
           91: "Bonum est confiteri Domino", 102: "Benedic, anima mea, Domino",
           120: "Levavi oculos meos in montes", 129: "De profundis",
           150: "Laudate Dominum in sanctis ejus"}

def emit_psalms():
    out = ['#import "helpers.typ": *', "",
           "// Generated by build.py — do not edit by hand.", ""]
    stats = []
    for n in PSALM_ORDER:
        ltitle, lat = latin_psalm(n)
        ptitle, pt = PSALMS[n]
        if sorted(lat) != sorted(pt):
            raise SystemExit(
                f"Ps {n}: verse numbers differ — Latin {sorted(lat)} vs PT {sorted(pt)}")
        heb = HEBREW[n]
        hl = f"Psalmus {roman(n)}" + (f" ({heb})" if heb != n else "")
        hp = f"Salmo {n}" + (f" ({heb})" if heb != n else "")
        head = (f"(pshead({tstr(hl)}, {tstr(ltitle)}), "
                f"pshead({tstr(hp)}, {tstr(ptitle)}))")
        cont = (f"(pscont({tstr(hl)}), pscont({tstr(hp)}))")
        units = [unit(lat[v], pt[v], v) for v in sorted(lat)]
        if not lat[min(lat)].startswith(INCIPIT[n].split(",")[0]):
            raise SystemExit(f"Ps {n}: incipit {INCIPIT[n]!r} does not open the Latin")
        num = f"{n} ({heb})" if heb != n else f"{n}"
        entries = ([("1", '"Salmos"')] if n == PSALM_ORDER[0] else []) + \
                  [("2", f'[{num} #h(0.4em) _{INCIPIT[n]}_]')]
        toc = "(" + "".join(f"({a}, {b})," for a, b in entries) + ")"
        out.append("#spread((")
        out += [f"  {u}," for u in units]
        out.append(f"), toc: {toc}, head: {head}, cont: {cont}, foot: (psfoot, psfoot))")
        out.append("")
        stats.append((n, len(units),
                      sum(len(lat[v].split()) for v in lat),
                      sum(len(pt[v].split()) for v in pt)))
    # The Magnificat closes the section: the canticle of the Virgin, sung
    # every evening at Vespers.
    parts = [("Luke", 1, list(range(46, 56)))]
    head = (f'(pshead("Canticum Beatae Mariae Virginis", {tstr(refstr(parts, 0))}), '
            f'pshead("Cântico de Nossa Senhora", {tstr(refstr(parts, 1))}))')
    out.append("#spread((")
    out += [f"  {u}," for u in pericope_units(parts)]
    out.append(f"), toc: ((2, [_Magnificat_]),), head: {head}, cont: (pscont(\"Magnificat\"), pscont(\"Magnificat\")), foot: (psfoot, psfoot))")
    (TYP / "gen_salmos.typ").write_text("\n".join(out), encoding="utf-8")
    return stats

def main():
    emit_mysteries()
    stats = emit_psalms()
    for n, nv, lw, pw in stats:
        print(f"Ps {n:3d}  {nv:2d} verses  lat {lw:4d}w  pt {pw:4d}w  ratio {pw/lw:.2f}")
    json.dump(manifest, open(WORK / "manifest.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=0)
    print(f"{len(manifest)} paired units written to work/manifest.json")

if __name__ == "__main__":
    main()
