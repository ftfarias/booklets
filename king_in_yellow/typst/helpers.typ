// Shared styling helpers for the four weird tales.
//
// Fragments are brought in with #include, which does NOT inherit the
// parent's `let` scope — every fragment must re-import this file.

// ── Section number within a story (I, II, III…) ──
#let sect(n) = block(above: 1.6em, below: 1.2em)[
  #align(center)[
    #text(size: 11pt, tracking: 3pt, fill: rgb("#777777"))[#n]
  ]
]

// ── Verse epigraph standing at the head of a story ──
// Chambers opens three of the four tales with quoted verse. Set ragged
// and indented, never justified: these are lines, not prose.
#let epigraph(body) = block(above: 0em, below: 2.0em, width: 100%)[
  #set align(left)
  #set par(justify: false, first-line-indent: 0em, leading: 0.62em)
  #pad(left: 8%, right: 4%)[
    #text(size: 9.5pt, style: "italic", fill: rgb("#444444"))[#body]
  ]
]

// ── Attribution line under an epigraph ──
#let attrib(t) = block(above: 0.7em, below: 2.2em, width: 100%)[
  #set align(right)
  #set par(justify: false, first-line-indent: 0em)
  #text(size: 8.5pt, style: "italic", fill: rgb("#666666"))[#t]
]

// ── A line of dialogue from the play itself ──
// Used for the fragment of Act I, Scene 2 that opens "The Mask".
#let play(name, body) = block(above: 0.55em, below: 0.55em, width: 100%)[
  #set align(left)
  #set par(justify: false, first-line-indent: 0em, leading: 0.62em)
  #pad(left: 8%, right: 4%)[
    #text(size: 9.5pt)[
      #text(weight: "bold", size: 8.5pt, tracking: 0.5pt)[#name]
      #h(0.5em) #body
    ]
  ]
]

// ── Text reproduced as it appears on a sign, card or manuscript ──
// Centred, letterspaced, small — a shopfront or a nailed-up placard.
#let sign(body) = block(above: 1.5em, below: 1.5em, width: 100%)[
  #set align(center)
  #set par(justify: false, first-line-indent: 0em, leading: 0.65em)
  #text(size: 9pt, tracking: 1.2pt, fill: rgb("#333333"))[#body]
]

// ── Scene break within a section (the source marks these * * * * *) ──
#let brk() = block(above: 1.4em, below: 1.4em, width: 100%)[
  #align(center)[
    #text(size: 9pt, fill: rgb("#aaaaaa"))[\u{2766}]
  ]
]

// ── Reserved page for a hand-mounted plate ──
//
// The illustrations are printed separately on photo paper, varnished,
// and tipped in by hand. The book does NOT embed them: this reserves
// the leaf and marks where the plate goes.
//
// Mounting is a tip-in: a 4-5 mm bead of neutral-pH adhesive along the
// INNER margin only, so the plate lifts like a flap and the book still
// opens flat. Gluing the whole face stiffens the leaf and strains the
// sewing.
//
// Default 96 x 143 mm keeps the sources' 3:2 proportion and leaves room
// inside the 113 x 174 mm text block for the ticks and the caption.
// The ticks sit OUTSIDE the plate area so they remain visible once the
// plate is mounted, and give something to register against.
//
// Note: this returns ONE block sized to the full text height and centres
// its contents. Stacking two `v(1fr)` in the page flow overflows onto a
// second page — the plate must own its height, not push against it.
#let plate(caption: none, w: 96mm, h: 143mm, box-h: 174mm) = {
  let m = 0.4pt + rgb("#bbbbbb")
  let t = 5mm      // tick length
  let g = 3mm      // gap between plate edge and tick

  block(width: 100%, height: box-h)[
    #set align(center + horizon)
    #stack(
      dir: ttb,
      spacing: 3.2em,
      box(width: w, height: h)[
        // Each corner is an L of two ticks, both sitting outside the
        // plate rectangle and meeting at the corner point.
        // top-left
        #place(dx: -g - t, dy: -g,     line(length: t, stroke: m))
        #place(dx: -g,     dy: -g - t, line(length: t, angle: 90deg, stroke: m))
        // top-right
        #place(dx: w + g,  dy: -g,     line(length: t, stroke: m))
        #place(dx: w + g,  dy: -g - t, line(length: t, angle: 90deg, stroke: m))
        // bottom-left
        #place(dx: -g - t, dy: h + g,  line(length: t, stroke: m))
        #place(dx: -g,     dy: h + g,  line(length: t, angle: 90deg, stroke: m))
        // bottom-right
        #place(dx: w + g,  dy: h + g,  line(length: t, stroke: m))
        #place(dx: w + g,  dy: h + g,  line(length: t, angle: 90deg, stroke: m))
      ],
      if caption != none {
        text(size: 8.5pt, style: "italic", fill: rgb("#777777"))[#caption]
      },
    )
  ]
}
