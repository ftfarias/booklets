// ─────────────────────────────────────────────────────────────
//  Wrap cover — back | spine | front, in one sheet.
//  Japanese stab binding: the sewing margin eats ~15mm of the
//  front edge, so the block is bound, then this cover wraps it.
//
//  Compile per volume, e.g.
//    typst compile --input vol=1 cover/cover.typ cover/cover_vol1.pdf
//    typst compile --input vol=2 cover/cover.typ cover/cover_vol2.pdf
//  Override the paper caliper (mm per sheet) if you use other stock:
//    typst compile --input vol=1 --input cal=0.15 cover/cover.typ out.pdf
// ─────────────────────────────────────────────────────────────

#let vol   = int(sys.inputs.at("vol", default: "1"))
#let cal   = float(sys.inputs.at("cal", default: "0.115"))   // mm per sheet
#let sheets = if vol == 1 { 36 } else { 33 }

#let spine-mm = (sheets * cal) * 1mm
#let board-w = 151mm      // 148 block + 3 fore-edge
#let board-h = 216mm      // 210 block + 3 head + 3 foot
#let total-w = board-w * 2 + spine-mm

#set page(width: total-w, height: board-h, margin: 0pt)
#set text(font: "Libertinus Serif", fill: rgb("#f2efe8"))

#let title    = if vol == 1 { "The Enchiridion" } else { "The Meditations" }
#let greek    = if vol == 1 { "Ἐγχειρίδιον" } else { "Τὰ εἰς ἑαυτόν" }
#let author   = if vol == 1 { "EPICTETUS" } else { "MARCUS AURELIUS" }
#let subtitle = if vol == 1 { "with a selection from the Discourses" } else { "in twelve books" }
#let numeral  = if vol == 1 { "I" } else { "II" }
#let blurb    = if vol == 1 {
  "Epictetus was born a slave and lame, and taught that no one who is free
   inside can be owned. He wrote nothing: his pupil Arrian took the words
   down, and the Enchiridion — the handbook, the thing kept ready in the
   hand — is what was distilled from them."
} else {
  "Marcus Aurelius commanded the armies of Rome and wrote these twelve books
   for no reader at all. He gave them no title; the Greeks called them
   simply to himself. Much of it was written on campaign, by a man
   reminding himself at night that he would shortly be dead."
}

#let ink = rgb("#1c1c1a")

// ── the whole wrap, painted dark ──
#rect(width: 100%, height: 100%, fill: ink, stroke: none)[
  #place(top + left, dx: 0mm, dy: 0mm)[
    #grid(
      columns: (board-w, spine-mm, board-w),
      rows: (board-h,),

      // ─── BACK COVER ───
      block(width: 100%, height: 100%, inset: (x: 18mm, y: 22mm))[
        #set par(justify: false, leading: 0.8em, first-line-indent: 0em)
        #v(1fr)
        #text(size: 9.5pt, fill: rgb("#b9b3a4"), style: "italic")[#blurb]
        #v(1.6em)
        #line(length: 28%, stroke: 0.4pt + rgb("#6b6558"))
        #v(1.2em)
        #text(size: 8pt, fill: rgb("#8a8478"), tracking: 1.5pt)[
          PUBLIC DOMAIN TEXTS · PRIVATELY PRINTED
        ]
        #v(1fr)
      ],

      // ─── SPINE ───
      // A stab-bound block this thin gives ~4mm of spine: only a rule of
      // small caps fits. Type is sized to the spine, not the other way round.
      block(width: 100%, height: 100%)[
        #align(center + horizon)[
          #rotate(90deg, reflow: false)[
            #box(width: board-h - 40mm)[
              #align(center)[
                #text(size: 6.5pt, tracking: 1.5pt, fill: rgb("#e8e3d8"))[
                  #author #h(0.9em) · #h(0.9em) #title
                ]
              ]
            ]
          ]
        ]
      ],

      // ─── FRONT COVER ───
      block(width: 100%, height: 100%, inset: (x: 18mm, y: 22mm))[
        #v(1fr)
        #align(center)[
          #text(size: 8.5pt, tracking: 4pt, fill: rgb("#8a8478"))[
            VOLUME #numeral
          ]
          #v(2.4em)
          #text(size: 11pt, tracking: 5pt, fill: rgb("#b9b3a4"))[#author]
          #v(1.8em)
          #text(size: 25pt, weight: "bold", fill: rgb("#f2efe8"))[#title]
          #v(0.7em)
          #text(size: 12pt, fill: rgb("#b9b3a4"))[#greek]
          #v(1.6em)
          #line(length: 34%, stroke: 0.5pt + rgb("#6b6558"))
          #v(1.4em)
          #text(size: 10pt, style: "italic", fill: rgb("#b9b3a4"))[#subtitle]
        ]
        #v(2fr)
        #align(center)[
          #text(size: 8pt, tracking: 3pt, fill: rgb("#6b6558"))[THE STOICS]
        ]
      ],
    )
  ]
]
