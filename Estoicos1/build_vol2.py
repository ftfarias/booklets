#!/usr/bin/env python3
"""Generate the Typst body fragment for Volume II (Marcus Aurelius) from
Project Gutenberg #15877 — the George Long (1862) translation.

Long's file carries three layers: the twelve books, his footnotes (indented
four spaces), and a closing index of terms (from the "INDEXES." heading). Only the books go in the volume;
his footnotes are dropped (they are textual-critical, addressed to scholars)
and the index with them.

Long's "thou/thee" is kept verbatim — Felipe's decision, for fidelity.
"""
import json, re, sys, pathlib

HERE  = pathlib.Path(__file__).parent
RAW, CLEAN, TYPST = HERE/"raw", HERE/"clean", HERE/"typst"

GREEK = {
    "melos": "μέλος",
    "meros": "μέρος",
    "aktines": "ἀκτῖνες",
    "apo tou ekteinesthai": "ἀπὸ τοῦ ἐκτείνεσθαι",
}
BOOKS = ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"]

def esc(s):
    s = s.replace("\\", "\\\\")
    for ch in "#$*_`<>@":
        s = s.replace(ch, "\\"+ch)
    return s

_unmapped = set()

def conv(p):
    grks = []
    def stash(m):
        k = m.group(1).strip()
        if k in GREEK:
            grks.append(GREEK[k])
        else:
            _unmapped.add(k); grks.append(k)
        return f"\x00{len(grks)-1}\x00"
    p = re.sub(r'\[Greek: ([^\]]*)\]', stash, p)
    # Long's bracketed clarifications read fine as plain text; keep, drop brackets
    p = re.sub(r'\[([a-z][^\]]{0,60})\]', r'\1', p)
    p = re.sub(r'\[([A-Z])\]', '', p)            # footnote markers
    p = esc(p)
    p = re.sub(r'\\_([^\\]+?)\\_', r'#emph[\1]', p)
    return re.sub(r'\x00(\d+)\x00', lambda m: "#grk[%s]" % grks[int(m.group(1))], p)

def build():
    t = open(RAW/"pg15877.txt", encoding="utf-8").read()
    a = t.find("THE THOUGHTS\n\nOF\n\nMARCUS AURELIUS")
    end = t.index("INDEXES.", a)     # Long's index of terms closes the file
    lines = t[a:end].split("\n")

    rom = re.compile(r'^\s*(' + "|".join(BOOKS) + r')\.\s*$')
    starts = [(i, m.group(1)) for i, l in enumerate(lines) if (m := rom.match(l))]
    assert len(starts) == 12, f"expected 12 books, found {len(starts)}"

    stats = []
    with open(TYPST/"meditations.typ", "w", encoding="utf-8") as f:
        f.write('#import "helpers.typ": *\n\n')
        for k, (ln, name) in enumerate(starts):
            end = starts[k+1][0] if k+1 < len(starts) else len(lines)
            # drop Long's footnotes (indented four spaces)
            body = "\n".join(l for l in lines[ln+1:end] if not l.startswith("    "))
            paras = [x for x in (re.sub(r'\s+', ' ', p).strip()
                                 for p in re.split(r'\n\s*\n', body)) if x]
            f.write(f'#bookhead[{name}]\n')
            for p in paras:
                f.write(conv(p) + "\n\n")
            stats.append((name, len(paras), len(" ".join(paras).split())))
    return stats

if __name__ == "__main__":
    stats = build()
    for name, np, nw in stats:
        print(f"  Book {name:>4}: {np:3d} sections, {nw:5d} words")
    print(f"TOTAL: {sum(s[2] for s in stats)} words")
    if _unmapped:
        print("UNMAPPED GREEK:", sorted(_unmapped), file=sys.stderr)
        sys.exit(1)
    print("All Greek terms mapped.")
