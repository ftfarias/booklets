// Placas do grupo de CCA — A4 paisagem, para imprimir e plastificar.
//
//   typst compile placas.typ placas-roxo.pdf
//   typst compile --input tema=claro placas.typ placas-claro.pdf
//
// "roxo": fundo roxo, letra branca (como a placa original).
// "claro": fundo branco, letra roxa — gasta pouca tinta e não ondula o papel.

// ---- Dados da tesouraria (trocar quando mudar a tesoureira) ----
#let tesoureira = "Luciana"
#let cpf = "163.027.678-22"
#let whatsapp = "(11) 96308-8901"
// Para o QR Pix: maiúsculas, sem acento; nome ≤ 25 e cidade ≤ 15 letras.
#let pix-nome = "LUCIANA"
#let pix-cidade = "SAO PAULO"

#import "@preview/tiaoma:0.3.0": qrcode
#import "pix.typ": pix-payload
#let pix = pix-payload(cpf.replace(regex("\D"), ""), pix-nome, pix-cidade)

// ---- Tema ----
#let tema = sys.inputs.at("tema", default: "roxo")
#let roxo = rgb("#4b2a86")
#let fundo = if tema == "claro" { white } else { roxo }
#let tinta = if tema == "claro" { roxo } else { white }
#let suave = if tema == "claro" { roxo.lighten(35%) } else { white.transparentize(25%) }

#set page(paper: "a4", flipped: true, margin: 0mm)
#set text(font: "Futura", fill: tinta, lang: "pt")
#set par(leading: 0.55em, spacing: 0pt)

// Moldura comum: painel com cantos arredondados e filete interno.
#let placa(corpo) = {
  place(top + left, dx: 9mm, dy: 9mm,
    rect(width: 297mm - 18mm, height: 210mm - 18mm, radius: 7mm, fill: fundo,
      stroke: if tema == "claro" { 0.6mm + roxo } else { none }))
  place(top + left, dx: 16mm, dy: 16mm,
    rect(width: 297mm - 32mm, height: 210mm - 32mm, radius: 4mm,
      stroke: 1.6mm + tinta))
  place(top + left, dx: 16mm, dy: 16mm,
    box(width: 297mm - 32mm, height: 210mm - 32mm, inset: (x: 14mm, y: 12mm),
      align(center + horizon, corpo)))
}

#let rodape = text(size: 12pt, tracking: 0.2em, fill: suave)[COMEDORES COMPULSIVOS ANÔNIMOS]
#let filete = line(length: 60mm, stroke: 0.9mm + tinta)

// ---- 1. Anonimato ----
#placa[
  #text(size: 68pt, weight: "bold", tracking: 0.12em)[ANONIMATO]
  #v(9mm)
  #filete
  #v(13mm)
  #text(size: 34pt, weight: "medium", tracking: 0.04em)[
    O QUE VOCÊ OUVIU AQUI \
    QUEM VOCÊ VIU AQUI \
    QUANDO SAIR DAQUI
  ]
  #v(11mm)
  #text(size: 44pt, weight: "bold", tracking: 0.04em)[DEIXE QUE FIQUE AQUI]
  #v(18mm)
  #rodape
]

#pagebreak()

// ---- 2. Sétima Tradição / PIX ----
// O QR fica sempre em quadro branco: QR invertido (branco no roxo)
// não é lido por boa parte das câmeras.
#placa[
  #text(size: 48pt, weight: "bold", tracking: 0.1em)[7ª TRADIÇÃO]
  #v(8mm)
  #text(size: 16pt, weight: "medium", tracking: 0.2em, fill: suave)[CONTRIBUIÇÃO POR PIX]
  #v(7mm)
  #filete
  #v(11mm)
  #grid(
    columns: (1fr, auto),
    column-gutter: 12mm,
    align: center + horizon,
    [
      #text(size: 12pt, weight: "medium", tracking: 0.25em)[CHAVE PIX · CPF]
      #v(5mm)
      #text(size: 42pt, weight: "bold", tracking: 0.02em, number-width: "tabular")[#cpf]
      #v(6mm)
      #text(size: 17pt, weight: "medium")[#tesoureira, tesoureira]
      #v(13mm)
      #text(size: 15pt, weight: "medium")[Envie o comprovante pelo WhatsApp]
      #v(5mm)
      #text(size: 28pt, weight: "bold", tracking: 0.03em)[#whatsapp]
    ],
    [
      #rect(fill: white, radius: 3mm, inset: 7mm,
        stroke: if tema == "claro" { 0.4mm + roxo } else { none },
        qrcode(pix, width: 60mm, options: (fg-color: roxo)))
      #v(4mm)
      #text(size: 10pt, weight: "medium", tracking: 0.2em)[ESCANEIE NO APP DO BANCO]
    ],
  )
  #v(12mm)
  #rodape
]
