#!/usr/bin/env python3
"""Generate the Typst body fragments for the four weird tales of
Robert W. Chambers' "The King in Yellow" (1895).

Source: Project Gutenberg #8492, public domain.
  raw/king_in_yellow_pg8492.txt

Only stories 1-4 are used. The collection's remaining six pieces are
sentimental Parisian romances with no bearing on the Carcosa material;
the editorial note in the book explains the cut.

Structures recognised in the source, in order of precedence:
  *  *  *  *  *          scene break inside a section
  I / II / III / IV      section heading (centred roman numeral)
  indented verse         epigraph at the head of a story
  CAMILLA: ...           dialogue from the play (opens "The Mask")
  centred caps block     a sign, card or manuscript title
  _italic_               emphasis
"""
import re, sys, json, pathlib

HERE  = pathlib.Path(__file__).parent
RAW   = HERE / "raw" / "king_in_yellow_pg8492.txt"
TYPST = HERE / "typst"
CLEAN = HERE / "clean"

# Line ranges in the Gutenberg file (1-indexed, inclusive), located by the
# story headings. Verified by check.py against the compiled PDF.
STORIES = [
    ("repairer",    "The Repairer of Reputations",   74, 1448),
    ("mask",        "The Mask",                    1449, 2147),
    ("dragon",      "In the Court of the Dragon",  2148, 2497),
    ("yellow_sign", "The Yellow Sign",             2498, 3323),
]

# Cassilda's Song — the book's epigraph, standing before all four tales.
SONG_RANGE = (47, 69)

# Errata against the source text. Each entry MUST still be found, or the
# build fails: an errata table that silently stops matching has rotted.
ERRATA = []  # PG #8492 is clean; kept so the mechanism exists.


def esc(s: str) -> str:
    """Escape Typst markup characters, leaving _italics_ for later."""
    s = s.replace("\\", "\\\\")
    for ch in "#$*`<>@[]":
        s = s.replace(ch, "\\" + ch)
    return s


def italics(s: str) -> str:
    """_word_ -> #emph[word]. Run AFTER esc(), which leaves _ untouched."""
    return re.sub(r"_([^_]+?)_", lambda m: "#emph[%s]" % m.group(1), s, flags=re.S)


def conv(s: str) -> str:
    return italics(esc(s))


def unwrap(lines):
    """Join hard-wrapped lines into single-line paragraphs."""
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


def is_rule(l):      return bool(re.match(r"^\s*\*(\s+\*)+\s*$", l))
def is_sect(l):      return bool(re.match(r"^\s{10,}[IVX]+\s*$", l))
def is_indented(l):  return bool(re.match(r"^ {2,}\S", l))
def is_blank(l):     return not l.strip()


def render_verse(lines):
    """Indented verse -> epigraph block, preserving line and stanza breaks.

    Deeply indented lines are refrains (Cassilda's "In Carcosa."), and the
    hanging indent is part of how the stanza reads. Measure each line
    against the shallowest in the block and carry the offset across.
    """
    body_lines = [l for l in lines if l.strip()]
    base = min(len(l) - len(l.lstrip()) for l in body_lines) if body_lines else 0

    out, blank = [], False
    for l in lines:
        if not l.strip():
            blank = True
            continue
        if blank and out:
            out.append("")          # marks a stanza break
        blank = False
        ind = (len(l) - len(l.lstrip())) - base
        txt = conv(l.strip())
        if ind >= 8:                # a refrain, not a wrapped line
            txt = "#h(%.1fem) %s" % (min(ind * 0.42, 7.0), txt)
        out.append(txt)
    body = []
    for i, l in enumerate(out):
        if l == "":
            body.append("#v(0.55em)")
        else:
            nxt = out[i + 1] if i + 1 < len(out) else None
            body.append(l + (" \\" if nxt not in (None, "") else ""))
    return "#epigraph[\n" + "\n".join(body) + "\n]\n"


def render_play(lines):
    """Dialogue lines from the play: NAME: text."""
    out = []
    for l in lines:
        l = l.strip()
        if not l:
            continue
        m = re.match(r"^([A-Z][A-Z ]+):\s*(.*)$", l)
        if m:
            out.append("#play[%s][%s]" % (conv(m.group(1)), conv(m.group(2))))
        elif l.startswith("_") and l.endswith("."):
            out.append("#attrib[%s]" % conv(l))
        else:                       # continuation of the previous speech
            if out:
                out[-1] = out[-1][:-1] + " " + conv(l) + "]"
    return "\n".join(out) + "\n"


def render_sign(lines):
    out = [conv(l.strip()) for l in lines if l.strip()]
    return "#sign[\n" + " \\\n".join(out) + "\n]\n"


def classify(block):
    """Decide what an indented block of lines actually is."""
    txt = [l for l in block if l.strip()]
    joined = " ".join(l.strip() for l in txt)
    if any(re.match(r"^[A-Z][A-Z ]+:", l.strip()) for l in txt):
        return "play"
    if re.match(r"^_.*_\.?$", joined.strip()):
        return "play"            # bare attribution line
    # Verse: opens with a quote mark, or several short lines of prose case.
    if joined.lstrip().startswith(("“", "‘")) and len(txt) > 1:
        return "verse"
    return "sign"


def build_story(slug, title, a, b, lines):
    body = lines[a - 1 : b]
    # drop the heading line itself and any blank run beneath it
    assert title.upper() in body[0].upper(), f"{slug}: heading mismatch"
    body = body[1:]

    out = []
    i, n = 0, len(body)
    first_para_seen = False

    while i < n:
        l = body[i]

        if is_blank(l):
            i += 1
            continue

        if is_rule(l):
            out.append("#brk()\n")
            i += 1
            continue

        if is_sect(l):
            out.append("#sect[%s]\n" % l.strip())
            i += 1
            continue

        if is_indented(l):
            j = i
            grp = []
            while j < n and not is_blank(body[j]):
                grp.append(body[j]); j += 1
            # a paragraph merely continuing after a soft break is not a block
            kind = classify(grp)
            if kind == "verse":
                out.append(render_verse(grp))
            elif kind == "play":
                out.append(render_play(grp))
            else:
                out.append(render_sign(grp))
            i = j
            continue

        # ordinary prose paragraph
        j = i
        grp = []
        while j < n and not is_blank(body[j]) and not is_rule(body[j]) \
              and not is_sect(body[j]) and not is_indented(body[j]):
            grp.append(body[j]); j += 1
        para = conv(unwrap(grp))
        if para:
            out.append(para + "\n")
            first_para_seen = True
        i = j

    text = "\n".join(out)
    header = '#import "helpers.typ": *\n\n'
    (TYPST / f"{slug}.typ").write_text(header + text, encoding="utf-8")
    words = sum(len(unwrap([l]).split()) for l in body)
    return words


def main():
    src = RAW.read_text(encoding="utf-8")
    for wrong, label in ERRATA:
        if wrong not in src:
            sys.exit(f"ERRATA no longer matches (source fixed?): {label}")
        src = src.replace(wrong, label)
    lines = src.split("\n")

    CLEAN.mkdir(exist_ok=True)
    TYPST.mkdir(exist_ok=True)

    # ── Cassilda's Song ──
    a, b = SONG_RANGE
    song = lines[a - 1 : b]
    cut = next(i for i, l in enumerate(song) if l.strip().startswith("Cassilda"))
    verse, attrib = song[:cut], song[cut:]
    frag = ['#import "helpers.typ": *', ""]
    frag.append(render_verse(verse).rstrip())
    frag.append("#attrib[%s]" % conv(unwrap(attrib)))
    (TYPST / "song.typ").write_text("\n".join(frag) + "\n", encoding="utf-8")

    report = {}
    for slug, title, a, b in STORIES:
        w = build_story(slug, title, a, b, lines)
        report[slug] = {"title": title, "words": w}
        print(f"  {slug:12} {w:6} words -> typst/{slug}.typ")

    (CLEAN / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"  total {sum(v['words'] for v in report.values())} words")


if __name__ == "__main__":
    main()
