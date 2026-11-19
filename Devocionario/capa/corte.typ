// CUT SHEET for the Silhouette Cameo — all three pieces on one sheet of
// gold HTV. `make capa` exports SVG and mirrors it (HTV is cut from the
// back): the file that goes to the machine is corte_espelhado.svg.
#import "pecas.typ": *

#set page(width: 150mm, height: 80mm, margin: 0mm)

#place(top + left, dx: 12mm, dy: 14mm, cruz)
#place(top + left, dx: 52mm, dy: 30mm, iniciais)
#place(top + left, dx: 128mm, dy: 10mm, rotate(90deg, reflow: true, lombada-txt))
