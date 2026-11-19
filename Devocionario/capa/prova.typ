// 1:1 PLACEMENT PROOF: the outside of the case, laid flat —
// back board | spine | front board — on the leather colour.
// Print at actual size on A4 landscape and lay it over the real cover
// to judge placement. Board and spine sizes are ASSUMED until the sewn
// block is measured: change the three numbers below.
#import "pecas.typ": *

#let BOARD_W = 104mm     // 105 block − ~3 groove + 2 square
#let BOARD_H = 152.5mm   // 148.5 block + 2 × 2 squares
#let SPINE_W = 12mm      // MEASURE the sewn, pressed block + 2 boards
#let JOINT   = 6mm       // gap between board and spine stiffener

#set page(width: 297mm, height: 210mm, margin: 0mm)
#set text(font: "Futura", size: 8pt, fill: rgb("#555555"))

#let total = 2 * BOARD_W + 2 * JOINT + SPINE_W
#let x0 = (297mm - total) / 2
#let y0 = (210mm - BOARD_H) / 2
#let xfront = x0 + BOARD_W + JOINT + SPINE_W + JOINT
#let xspine = x0 + BOARD_W + JOINT

#place(top + left, dx: x0 - JOINT, dy: y0 - 4mm,
  rect(width: total + 2 * JOINT, height: BOARD_H + 8mm, fill: LEATHER, stroke: none))
#for x in (x0, xfront) {
  place(top + left, dx: x, dy: y0, rect(width: BOARD_W, height: BOARD_H,
        stroke: (paint: rgb("#ffffff40"), thickness: 0.3pt, dash: "dashed")))
}
#place(top + left, dx: xspine, dy: y0, rect(width: SPINE_W, height: BOARD_H,
       stroke: (paint: rgb("#ffffff40"), thickness: 0.3pt, dash: "dashed")))

// Cross and initials on the optical centre: horizontally centred,
// centre of the piece 45% down from the top of the board.
#context {
  let c = measure(cruz)
  place(top + left, dx: xfront + (BOARD_W - c.width) / 2,
        dy: y0 + 0.45 * BOARD_H - c.height / 2, cruz)
  let i = measure(iniciais)
  place(top + left, dx: x0 + (BOARD_W - i.width) / 2,
        dy: y0 + 0.45 * BOARD_H - i.height / 2, iniciais)
  let l = measure(rotate(90deg, reflow: true, lombada-txt))
  place(top + left, dx: xspine + (SPINE_W - l.width) / 2,
        dy: y0 + 0.45 * BOARD_H - l.height / 2,
        rotate(90deg, reflow: true, lombada-txt))
}

#place(bottom + left, dx: 10mm, dy: -8mm)[
  #let mm(x) = str(calc.round(x / 1mm, digits: 1)).replace(".", ",") + " mm"
  Prova 1:1 — imprimir em tamanho real. Pastas #mm(BOARD_W) × #mm(BOARD_H), lombada #mm(SPINE_W) (a medir),
  junta #mm(JOINT). Peças centradas a 45% da altura (centro óptico).
]
#place(top + left, dx: x0, dy: y0 - 9mm)[verso (contracapa)]
#place(top + left, dx: xfront, dy: y0 - 9mm)[frente]
