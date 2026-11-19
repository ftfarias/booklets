#!/usr/bin/env python3
"""
Verifica o PDF compilado das frases -- nao o fonte.

O que confere:
  - 20 paginas (10 frases, cada uma com verso em branco)
  - tamanho de pagina 165x240 mm, uniforme
  - as 10 frases presentes e integras
  - nenhuma marcacao de build vazada
  - nenhuma linha final orfa (viuva de 1-2 palavras)
"""
import re, sys, subprocess
from pathlib import Path

ROOT = Path(__file__).parent
PDF  = ROOT / "frases.pdf"

W_MM, H_MM = 165.0, 240.0
MM = 72 / 25.4

ESPERADAS = [
    "Menos demos. Mais resultados.",
    "Feito é melhor que perfeito.",
    "Uma prova de conceito que nunca sai do papel não conta.",
    "Os ossos eram reais. A história não era.",
    "Escrever força precisão.",
    "Dados sozinhos nunca são suficientes.",
    "A documentação não é o sistema.",
    "Um artefato, ainda fazendo seu trabalho,",
    "A melhor forma de entender algo de verdade",
    "Escrevo quando tenho algo que vale a pena dizer.",
]

# Inicios das linhas de fonte: marcam onde a frase termina na pagina.
FONTES = ["Dipolo,", "blog,", "site pessoal,"]

# Marcacao que nunca pode chegar ao PDF.
VAZAMENTOS = ["#frase", "#import", "helpers.typ", "pagebreak", "[", "]", "TODO"]


def norm(s: str) -> str:
    """O extrator quebra linhas no meio das frases: normalizar espacos."""
    return " ".join(s.split())


def main() -> int:
    if not PDF.exists():
        print(f"FALHA: {PDF.name} nao existe. Rode 'make'.")
        return 1

    from pypdf import PdfReader
    r = PdfReader(str(PDF))
    erros = []

    if len(r.pages) != 20:
        erros.append(f"paginas: esperava 20, achei {len(r.pages)}")

    for i, p in enumerate(r.pages, 1):
        w = float(p.mediabox.width) / MM
        h = float(p.mediabox.height) / MM
        if abs(w - W_MM) > 0.5 or abs(h - H_MM) > 0.5:
            erros.append(f"pagina {i}: {w:.1f}x{h:.1f} mm, esperava {W_MM}x{H_MM}")

    texto = norm(" ".join(p.extract_text() for p in r.pages))

    for frase in ESPERADAS:
        if norm(frase) not in texto:
            erros.append(f"frase ausente: {frase[:45]!r}")

    for v in VAZAMENTOS:
        if v in texto:
            erros.append(f"marcacao vazada: {v!r}")

    # Numeracao 01..10 em duas casas
    for n in range(1, 11):
        if f"{n:02d}" not in texto.replace(" ", ""):
            erros.append(f"numeracao ausente: {n:02d}")

    # Viuvas na frase em portugues (o corpo da pagina). A versao inglesa
    # e a fonte vem depois e sao medidas a parte.
    for i, p in enumerate(r.pages, 1):
        linhas = [l.strip() for l in p.extract_text().split("\n") if l.strip()]
        if len(linhas) < 3:
            continue
        # descarta a numeracao "0 1" e para na linha da fonte
        corpo = [l for l in linhas if not re.fullmatch(r"\d\s*\d", l)]
        pt = []
        for l in corpo:
            if any(l.startswith(f) for f in FONTES):
                break
            pt.append(l)
        if len(pt) >= 2:
            ultima = pt[-1].split()
            if len(ultima) <= 2 and sum(len(w) for w in ultima) < 14:
                erros.append(
                    f"pagina {i}: viuva na frase PT: {' '.join(ultima)!r}"
                )

    if erros:
        print(f"FALHOU ({len(erros)}):")
        for e in erros:
            print("  -", e)
        return 1

    print(f"OK: {len(r.pages)} pp, {W_MM:.0f}x{H_MM:.0f} mm, 10 frases integras")
    return 0


if __name__ == "__main__":
    sys.exit(main())
