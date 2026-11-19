// Shared geometry of the cover art — imported by corte.typ (what the
// Cameo cuts) and prova.typ (1:1 placement proof on the leather colour).
//
// Gold HTV on dark red leather. Weeding floor 1.2 mm for every stroke
// (../../CLAUDE.md); Futura, never a serif.

#let GOLD    = rgb("#c9a227")
#let LEATHER = rgb("#5a1619")

// ── Front: Latin cross ────────────────────────────────────────────────
// Classic proportions: arm span 2/3 of the height, crossing at 1/3 from
// the top. Stroke ~1/11 of the height — present, not heavy. One solid
// island: nothing to weed inside it.
#let CROSS_H = 46mm
#let CROSS_W = CROSS_H * 2 / 3
#let CROSS_T = 4.2mm
#let cruz = box(width: CROSS_W, height: CROSS_H, {
  place(top + left, dx: (CROSS_W - CROSS_T) / 2,
        rect(width: CROSS_T, height: CROSS_H, fill: GOLD, stroke: none))
  place(top + left, dy: CROSS_H / 3 - CROSS_T / 2,
        rect(width: CROSS_W, height: CROSS_T, fill: GOLD, stroke: none))
})

// ── Back: her initials ────────────────────────────────────────────────
// Middle dot rather than full stops: "D.G." leaves a trailing dot that
// pulls the pair off-centre; "D·G" is symmetric. One character to change.
#let INICIAIS = "D·G"
#let iniciais = text(font: "Futura", weight: "medium", size: 36pt,
                     fill: GOLD, tracking: 3pt, INICIAIS)

// ── Spine ─────────────────────────────────────────────────────────────
// Read top to bottom (book lying face up: tops of the letters toward the
// front board). Cap height ~6 mm: fits a spine down to ~10 mm (2 mm each side).
// At 22pt the strokes measured 1.23 mm — too close to the floor.
#let TITULO = "PRECES"
#let lombada-txt = text(font: "Futura", weight: "bold", size: 24pt,
                        fill: GOLD, tracking: 2.5pt, TITULO)
