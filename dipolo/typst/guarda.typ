#import "helpers.typ": *

// GUARDA COM REFORCO DE TECIDO — duas folhas A4 unidas por tira de
// tecido na dobra (cloth-jointed endpaper). Nao e remendo: e a
// estrutura que a encadernacao de conservacao usa de proposito, porque
// a dobra da guarda e o ponto de maior tensao do livro.
//
//   pagina 1 = guarda VOLANTE  (flyleaf)    -> as frases
//   pagina 2 = CONTRAGUARDA    (pastedown)  -> o logo, cola na capa
//
// Cada face e 165x240 mm, impressa DEITADA numa A4 paisagem (297x210).
//
// A tira de tecido (~28 mm) cobre ~14 mm de cada folha na borda da
// dobra. Essa faixa e ZONA MORTA: nada de texto ou logo ali, ou some
// debaixo do tecido. Ver JOINT nas medidas abaixo.

#set document(title: "Dipolo — guardas", author: "Felipe de Toledo Farias")
#set page(width: 297mm, height: 210mm, margin: 0pt, fill: white)
#set text(lang: "pt", font: "Newsreader 16pt")

#let FRASES = (
  "Menos demos. Mais resultados.",
  "Feito é melhor que perfeito.",
  "Uma prova de conceito que nunca sai do papel não conta.",
  "Os ossos eram reais. A história não era.",
  "Escrever força precisão.",
  "Dados sozinhos nunca são suficientes.",
  "A documentação não é o sistema.",
  "Um artefato, ainda fazendo seu trabalho, depois que o mundo que precisava dele seguiu em frente.",
  "A melhor forma de entender algo de verdade é tentar explicar para outras pessoas.",
  "Escrevo quando tenho algo que vale a pena dizer.",
)

#let GW = 120mm   // largura util (a pagina deitada)
#let GH = 165mm   // altura util
#let JOINT = 16mm // zona morta sob a tira de tecido

// Marcas de corte nos quatro cantos da area util.
#let MX = (297mm - GW) / 2
#let MY = (210mm - GH) / 2
#let marcas() = {
  for (px, sx) in ((MX, -5mm), (MX + GW, 5mm)) {
    for py in (MY, MY + GH) {
      place(left + top, dx: px, dy: py,
            line(end: (sx, 0mm), stroke: 0.2pt + rgb("#9aa89e")))
    }
  }
  for (py, sy) in ((MY, -5mm), (MY + GH, 5mm)) {
    for px in (MX, MX + GW) {
      place(left + top, dx: px, dy: py,
            line(end: (0mm, sy), stroke: 0.2pt + rgb("#9aa89e")))
    }
  }
}

// ---------------------------------------------------------------
// 1. GUARDA VOLANTE — as frases.
// A dobra fica a ESQUERDA, entao a zona morta e a esquerda.
// ---------------------------------------------------------------
#place(center + horizon)[
  #box(width: GW, height: GH, clip: true)[
    // começa depois da zona morta da dobra
    #place(left + top, dx: JOINT + 6mm, dy: 8mm)[
      #block(width: GW - JOINT - 14mm)[   // ~210 mm de largura útil
        #set align(left)
        #set par(leading: 3.2mm)          // espaçamento entre linhas da mesma frase
        #for (i, f) in FRASES.enumerate() {
          block(below: 4.8mm, breakable: false)[
            #text(font: "Hanken Grotesk", size: 6pt, tracking: 1.3pt,
                  fill: rgb("#b9a06a"))[#dois(i + 1)]
            #linebreak()
            #text(font: "Newsreader 16pt", size: 8.8pt, style: "italic",
                  fill: forest)[#f]       // sem hyphenate: false
          ]
        }
      ]
    ]
  ]
]

#pagebreak()

// ---------------------------------------------------------------
// 2. CONTRAGUARDA — o logo, colada na capa.
// A dobra fica a DIREITA (espelhada em relacao a volante), entao a
// zona morta e a direita.
// ---------------------------------------------------------------
#marcas()
#place(center + horizon)[
  #box(width: GW, height: GH, clip: true)[
    #place(center + horizon, dx: -JOINT / 2)[
      #image("logo-forte.svg", width: 108mm)
    ]
  ]
]
