#!/usr/bin/env python3
"""Generate the Typst body fragments for Volume I (Epictetus) from the
Project Gutenberg sources in raw/.

  Enchiridion  — Higginson (1865), PG #45109  (translation only; the 1948
                 Liberal Arts Press introduction in that file is copyrighted)
  Discourses   — Long (1877), PG #10661, his own selection, complete

Long transliterates Greek technical terms as [Greek: xxx]; clean/greek_map.json
restores them to real polytonic Greek, which the book carries as apparatus.
"""
import json, re, sys, pathlib

HERE = pathlib.Path(__file__).parent
RAW, CLEAN, TYPST = HERE/"raw", HERE/"clean", HERE/"typst"
GREEK = json.load(open(CLEAN/"greek_map.json", encoding="utf-8"))

SMALL = {'a','an','the','and','or','of','to','in','on','is','are','we','not','be','for','by',
         'with','from','that','which','what','how','who','as','at','it','our','their','his',
         'ought','may','can','when','if','about','against','over','into','has','have','do',
         'does','us','you'}

def titlecase(h):
    out, n = [], 0
    for w in re.split(r'(\s+)', h.lower()):
        if not w.strip():
            out.append(w); continue
        core = w.strip("(),;:'’.")
        out.append(w if (n and core in SMALL) else w[:1].upper()+w[1:])
        n += 1
    return "".join(out)

def esc(s):
    s = s.replace("\\", "\\\\")
    for ch in "#$*_`<>@":
        s = s.replace(ch, "\\"+ch)
    return s

_unmapped = set()

def conv(p):
    """Escape for Typst, restore Greek, convert _italics_ to #emph."""
    grks = []
    def stash(m):
        k = m.group(1).strip()
        if k in GREEK:
            grks.append(GREEK[k])
        else:
            _unmapped.add(k); grks.append(k)
        return f"\x00{len(grks)-1}\x00"
    p = re.sub(r'\[Greek: ([^\]]*)\]', stash, p)
    p = esc(p)
    p = re.sub(r'\\_([^\\]+?)\\_', r'#emph[\1]', p)
    return re.sub(r'\x00(\d+)\x00', lambda m: "#grk[%s]" % grks[int(m.group(1))], p)

def paras_of(text):
    return [x for x in (re.sub(r'\s+', ' ', p).strip()
                        for p in re.split(r'\n\s*\n', text)) if x]

# ── Enchiridion ────────────────────────────────────────────────────────────
def build_enchiridion():
    t = open(RAW/"pg45109.txt", encoding="utf-8").read()
    end = t.find("*** END")
    body = t[t.rindex("THE ENCHIRIDION", 0, end):end].split("\n", 1)[1]

    lines = body.split("\n")
    fn = next(i for i, l in enumerate(lines) if re.match(r'^\[\d\]', l))
    notes_raw, lines = "\n".join(lines[fn:]), lines[:fn]
    notes = {m.group(1): re.sub(r'\s+', ' ', m.group(2)).strip()
             for m in re.finditer(r'^\[(\d)\](.*?)(?=^\[\d\]|\Z)', notes_raw, re.M|re.S)}

    rom = re.compile(r'^\s{10,}([IVXLC]+)(\[\d\])?\s*$')
    secs, cur, note, buf = [], None, None, []
    for l in lines:
        m = rom.match(l)
        if m:
            if cur: secs.append((cur, note, buf))
            cur, note, buf = m.group(1), m.group(2), []
        elif cur is not None:
            buf.append(l)
    if cur: secs.append((cur, note, buf))

    with open(TYPST/"enchiridion.typ", "w", encoding="utf-8") as f:
        f.write('#import "helpers.typ": *\n\n')
        for num, note, buf in secs:
            ps = paras_of("\n".join(buf))
            if not ps: continue
            f.write(f'#sec[{num}]#h(0.6em)' + conv(ps[0]) + "\n\n")
            for p in ps[1:]:
                f.write(conv(p) + "\n\n")
    return len(secs), notes

# ── Discourses ─────────────────────────────────────────────────────────────
def discourse_region():
    t = open(RAW/"pg10661.txt", encoding="utf-8").read()
    a = t.index("A SELECTION FROM THE DISCOURSES OF EPICTETUS.")
    a = t.index("A SELECTION FROM THE DISCOURSES OF EPICTETUS.", a+10)
    return t[a:t.index("THE ENCHEIRIDION, OR MANUAL.", a)].split("\n")

def chapter_map(lines):
    """A chapter opens with an ALL-CAPS heading that ends in '.—' inline."""
    starts = []
    for i, l in enumerate(lines):
        if ".—" not in l: continue
        m = re.match(r'^([A-Z0-9 ,;:\'’\(\)\.\-]*?)\.—', l.strip())
        if not m: continue
        j = i
        while j-1 >= 0:
            s = lines[j-1].strip()
            if s and re.match(r'^[A-Z0-9 ,;:\'’\(\)\.\-]+$', s) and re.search(r'[A-Z]{2}', s):
                j -= 1
            else:
                break
        head = " ".join(lines[k].strip() for k in range(j, i))
        starts.append((j, (head + " " + m.group(1)).strip()))
    starts = sorted(set(starts))
    return [{"line": ln, "end": (starts[k+1][0] if k+1 < len(starts) else len(lines)),
             "head": h} for k, (ln, h) in enumerate(starts)]

def build_discourses():
    lines = discourse_region()
    chs = chapter_map(lines)
    json.dump(chs, open(CLEAN/"discourses_map.json", "w"), indent=1)
    with open(TYPST/"discourses.typ", "w", encoding="utf-8") as f:
        f.write('#import "helpers.typ": *\n\n')
        for c in chs:
            seg = "\n".join(lines[c["line"]:c["end"]])
            i = seg.find(".—")
            ps = paras_of(seg[i+2:] if i >= 0 else seg)
            if not ps: continue
            f.write(f'#chap[{esc(titlecase(c["head"]))}]\n')
            for p in ps:
                f.write(conv(p) + "\n\n")
    return len(chs)

# ── Biographical note (Long's, biography proper only) ──────────────────────
def build_life():
    t = open(RAW/"pg10661.txt", encoding="utf-8").read()
    a = t.index("EPICTETUS.\n\n\nVery little is known")
    bio = t[a:t.index("A SELECTION FROM THE DISCOURSES OF EPICTETUS.", a)].split("\n", 1)[1]
    keep = paras_of(bio)[0:4]          # 4+ are bibliographic apparatus
    with open(TYPST/"life.typ", "w", encoding="utf-8") as f:
        f.write('#import "helpers.typ": *\n\n#pagebreak(to: "odd", weak: true)\n')
        f.write('#block(above: 0em, below: 1.2em)[\n  #set par(first-line-indent: 0em)\n'
                '  #align(center)[\n    #text(size: 16pt, weight: "bold")[Epictetus]\n'
                '    #v(0.4em)\n    #text(size: 9pt, style: "italic", fill: rgb("#777777"))'
                '[a life, by his translator]\n  ]\n]\n\n')
        for p in keep:
            f.write(conv(p) + "\n\n")
        f.write('#v(1em)\n#align(right)[#text(size: 8.5pt, style: "italic", '
                'fill: rgb("#777777"))[George Long, 1877]]\n')
    return len(" ".join(keep).split())

if __name__ == "__main__":
    n_sec, notes = build_enchiridion()
    n_ch = build_discourses()
    n_bio = build_life()
    print(f"Enchiridion : {n_sec} sections, {len(notes)} footnotes")
    print(f"Discourses  : {n_ch} chapters")
    print(f"Life        : {n_bio} words")
    if _unmapped:
        print("UNMAPPED GREEK:", sorted(_unmapped), file=sys.stderr)
        sys.exit(1)
    print("All Greek terms mapped.")
