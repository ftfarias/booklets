// Shared styling for the Devocionário (Liber Precum).
// Fragments must `#import "helpers.typ": *` — Typst #include does NOT
// share the parent's let-scope.

// ── Geometry ──────────────────────────────────────────────────────────
// A6 "in quarto": quarto.py puts four A6 pages on each side of an A4
// sheet, folded twice. The second fold is the spine and runs WITH the
// grain of long-grain A4 — an A4→A5 fold would run across it. The first
// fold lands at the head and is slit open after sewing; fore-edge and tail
// are the sheet's own cut edges, so there is nothing else to trim.
// (No waste → no crop marks; they come back by themselves if TRIM < MEDIA.)
#let MEDIA_W = 105mm
#let MEDIA_H = 148.5mm
#let TRIM_W  = MEDIA_W
#let TRIM_H  = MEDIA_H
#let WASTE_X = MEDIA_W - TRIM_W
#let WASTE_Y = (MEDIA_H - TRIM_H) / 2

// Margins inside the page. Sewn codex: inside/outside by parity is right.
// Fore-edge and tail sit on the A4's outer edge — the L4360 cannot print
// the outer ~3 mm, so neither margin may go below ~6 mm.
#let M_IN  = 12mm
#let M_OUT = 10mm
#let M_TOP = 12mm
#let M_BOT = 16mm
#let TEXT_W = TRIM_W - M_IN - M_OUT
#let TEXT_H = TRIM_H - M_TOP - M_BOT

// ── Colour and type ───────────────────────────────────────────────────
// Rubrics in red, as in the old missals: headings, verse numbers and
// instructions. Everything that is said aloud is black.
#let RED   = rgb("#9e1b1b")
#let INK   = rgb("#141414")
#let MUTED = rgb("#7a7a7a")
#let BODY  = 12pt          // older eyes: ~14% larger than the Estoicos

// ── Crop marks ────────────────────────────────────────────────────────
// Hairlines in the waste, never touching the trimmed page. On a recto the
// fold is at the left and the waste on the right; on a verso, mirrored.
#let cropmarks() = context {
  if WASTE_X < 4mm or WASTE_Y < 4mm { return }
  let recto = calc.odd(here().page())
  let x0 = if recto { 0mm } else { WASTE_X }      // trim box, left
  let fore = if recto { x0 + TRIM_W } else { x0 } // fore-edge x
  let gap = 3mm
  let len = 6mm
  let s = 0.25pt + rgb("#808080")
  for y in (WASTE_Y, WASTE_Y + TRIM_H) {
    // horizontal tick in the fore-edge waste, marks the head/tail cut
    let hx = if recto { fore + gap } else { fore - gap - len }
    place(top + left, dx: hx, dy: y, line(length: len, stroke: s))
    // vertical tick in the head/tail waste, marks the fore-edge cut
    let vy = if y == WASTE_Y { y - gap - len } else { y + gap }
    place(top + left, dx: fore, dy: vy, line(angle: 90deg, length: len, stroke: s))
  }
}

#let setup(body) = {
  set document(title: "Liber Precum — Livro de Orações", author: "Felipe de Toledo Farias")
  set page(
    width: MEDIA_W, height: MEDIA_H,
    margin: (
      inside: M_IN, outside: M_OUT + WASTE_X,
      top: M_TOP + WASTE_Y, bottom: M_BOT + WASTE_Y,
    ),
    background: cropmarks(),
    footer-descent: 6mm,
    // Folio only on pages that carry text: blank pages left by
    // pagebreak(to: ...) stay clean. See `inked`.
    footer: context {
      let n = here().page()
      let s = query(<ink-s>).map(m => m.location().page())
      let e = query(<ink-e>).map(m => m.location().page())
      if s.zip(e).any(((a, b)) => a <= n and n <= b) {
        align(center, text(size: 9pt, fill: MUTED, str(n)))
      }
    },
  )
  set text(font: "Libertinus Serif", size: BODY, fill: INK, lang: "pt",
           hyphenate: false, number-type: "old-style")
  // Ragged right: at ~42 characters a justified line opens rivers, and
  // without hyphenation it would be worse. Breviaries with short lines
  // do the same.
  set par(justify: false, leading: 0.62em, spacing: 0.62em)
  body
}

// Index entry: level 1 = section, level 2 = piece. Collected by the
// index page with query(<toc>); its page is where the marker lands.
#let tocmark(level, body) = [#metadata((level: level, body: body))<toc>]

// Marks a stretch of content whose pages get a folio.
#let inked(body) = [#metadata(none)<ink-s>#body#metadata(none)<ink-e>]

// ── Building blocks ───────────────────────────────────────────────────
#let rubric(body) = text(fill: RED, style: "italic", size: 0.86em, body)
#let red(body) = text(fill: RED, body)

// Small letter-spaced red label at the head of a page.
#let label(body) = block(width: 100%, below: 1.1em)[
  #align(center, text(size: 8.5pt, tracking: 1.6pt, fill: RED, upper(body)))
]

// Title of a piece (prayer, psalm, mystery).
#let ptitle(body, sub: none) = block(width: 100%, below: 0.9em)[
  #align(center)[
    #text(size: 15pt, body)
    #if sub != none {
      v(0.15em)
      text(size: 0.86em, style: "italic", fill: RED, sub)
    }
  ]
]

// Superscription of a psalm ("Psalmus David."), and other italic notes.
#let superscr(body) = block(width: 100%, below: 0.8em)[
  #align(center, text(size: 0.86em, style: "italic", fill: MUTED, body))
]

// One numbered verse: red number hanging in a 6mm gutter.
#let vn(n, body) = par(hanging-indent: 6mm)[#box(width: 6mm, text(size: 7.5pt, fill: RED, baseline: -0.15em, str(n)))#body]

// Gap between non-contiguous verses of a pericope.
#let elide = align(center, text(fill: MUTED, size: 0.8em)[· · ·])

// A short ornament for space between pieces on one page.
#let sep = block(above: 0.9em, below: 0.9em, width: 100%, align(center, text(fill: RED, size: 9pt)[✝]))

// ℣ / ℟ responses.
// Libertinus has no ℣/℟ glyphs: draw them — the letter crossed by a
// short oblique stroke through the leg, as the missals print them.
#let slashed(c) = box(text(fill: RED, c) + place(left + bottom,
  dx: 0.08em, dy: -0.02em,
  line(start: (0em, 0em), end: (0.52em, -0.5em), stroke: 0.055em + RED)))
#let V = [#slashed[V]#h(0.25em)]
#let R = [#slashed[R]#h(0.25em)]

// ── The facing-page spread ────────────────────────────────────────────
// Left (verso, even page): the original — Latin, or Italian for the
// Novena. Right (recto, odd page): the Portuguese. Units are kept whole
// and distributed over as many spreads as needed, measured with the real
// fonts, so the two pages of a spread always hold the same verses. A unit
// that would not fit on an otherwise empty page is placed alone (and
// check.py will catch the overflow by parity).
//
//   units:     array of (left, right) contents
//   head:      (left, right) shown on the first spread only
//   cont:      (left, right) shown on continuation spreads
//   foot:      (left, right) shown after the last unit
//   toc:       ((level, title), ...) index entries for this spread
#let spread(units, head: ([], []), cont: none, foot: none, toc: ()) = context {
  let H = TEXT_H - 1mm
  let sidebody(side, us, first, last) = {
    let parts = ()
    // Index markers ride on the first LEFT page, so the index points at
    // the opening of the spread.
    if first and side == 0 { parts += toc.map(e => tocmark(e.at(0), e.at(1))) }
    if first { parts.push(head.at(side)) }
    else if cont != none { parts.push(cont.at(side)) }
    parts += us.map(u => u.at(side))
    if last and foot != none { parts.push(foot.at(side)) }
    block(width: TEXT_W, parts.join())
  }
  let fits(us, first, last, cap) = (
    measure(sidebody(0, us, first, last)).height <= cap and
    measure(sidebody(1, us, first, last)).height <= cap
  )
  // Greedy fill to a height cap. The foot is always reserved: we cannot
  // know yet whether a chunk will be the last — cheap insurance.
  let greedy(cap) = {
    let chunks = ()
    let cur = ()
    for u in units {
      let first = chunks.len() == 0
      let trial = cur + (u,)
      if cur.len() > 0 and not fits(trial, first, true, cap) {
        chunks.push(cur)
        cur = (u,)
      } else {
        cur = trial
      }
    }
    chunks.push(cur)
    chunks
  }
  let chunks = greedy(H)
  // Balance: with k spreads needed, find the smallest cap that still
  // needs only k, so the verses are spread evenly instead of leaving a
  // last spread with two lonely verses.
  let k = chunks.len()
  if k > 1 {
    let lo = H / k
    let hi = H
    for _ in range(9) {
      let mid = (lo + hi) / 2
      if greedy(mid).len() <= k { hi = mid } else { lo = mid }
    }
    chunks = greedy(hi)
  }
  for (i, c) in chunks.enumerate() {
    let first = i == 0
    let last = i == chunks.len() - 1
    pagebreak(to: "even", weak: true)
    inked(sidebody(0, c, first, last))
    pagebreak()
    inked(sidebody(1, c, first, last))
  }
}

// ── Pieces used by the generated fragments ────────────────────────────
#let roman(n) = {
  let out = ""
  for (a, r) in ((10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")) {
    while n >= a { out += r; n -= a }
  }
  out
}

// Head of a rosary mystery. `day` only on the first of each group.
#let mhead(group, k, name, ref, day) = {
  label(group)
  ptitle([#red(roman(k)) #h(0.3em) #name], sub: day)
  block(below: 1em, width: 100%, align(center, text(size: 9pt, fill: MUTED, tracking: 0.5pt, ref)))
}
#let mfoot(body) = block(above: 1.1em, width: 100%, align(center, rubric(body)))

// Head of a psalm: number, then the Vulgate superscription.
#let pshead(num, sup) = {
  label(num)
  if sup != "" { superscr(sup) }
}
#let pscont(num) = label([#num #h(0.2em) · #h(0.2em) _cont._])
#let psfoot = block(above: 0.8em, width: 100%, align(center, text(fill: RED, size: 9pt)[✝]))

// Name of a prayer, inside a unit.
#let oname(body) = block(above: 0.2em, below: 0.6em, width: 100%,
  align(center, text(size: 9pt, tracking: 1.2pt, fill: RED, upper(body))))
// A prayer unit: name + text, with space after.
#let prayer(name, body) = block(below: 1.3em, width: 100%)[#oname(name)#body]
