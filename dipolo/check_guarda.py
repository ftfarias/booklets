#!/usr/bin/env python3
"""
Verifica as guardas compiladas -- no PDF, nao no fonte.

guardas/guarda.pdf: 2 paginas A4 paisagem, unidas depois por tira de
tecido na dobra (cloth-jointed endpaper).
  pagina 1 = guarda volante (flyleaf)   -> as 10 frases
  pagina 2 = contraguarda (pastedown)   -> o logo
"""
import sys
from pathlib import Path

ROOT = Path(__file__).parent
MM = 72 / 25.4

FRASES = [
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

# folha A4 paisagem; area util = a pagina deitada, com corte sobrando.
FOLHA_W, FOLHA_H = 297.0, 210.0
UTIL_W, UTIL_H = 240.0, 165.0

# Zona morta sob a tira de tecido: nada impresso pode invadi-la.
JOINT_MM = 16.0

VAZAMENTOS = ["#image", "logo.svg", "helpers.typ", "#place", "TODO"]


def norm(s):
    return " ".join(s.split())


def main():
    from pypdf import PdfReader
    erros = []
    pdf = ROOT / "guardas" / "guarda.pdf"
    if not pdf.exists():
        print("FALHA: guardas/guarda.pdf nao existe. Rode 'make'.")
        return 1

    r = PdfReader(str(pdf))
    if len(r.pages) != 2:
        erros.append(f"{len(r.pages)} paginas, esperava 2 (volante + contraguarda)")

    for i, p in enumerate(r.pages, 1):
        w = float(p.mediabox.width) / MM
        h = float(p.mediabox.height) / MM
        if abs(w - FOLHA_W) > 0.5 or abs(h - FOLHA_H) > 0.5:
            erros.append(
                f"pagina {i}: folha {w:.0f}x{h:.0f}, "
                f"esperava {FOLHA_W:.0f}x{FOLHA_H:.0f} (A4 paisagem)"
            )
        if UTIL_W > w or UTIL_H > h:
            erros.append(f"pagina {i}: area util nao cabe com margem de corte")

    # pagina 1: as frases. pagina 2: o logo, sem texto.
    volante = norm(r.pages[0].extract_text()) if len(r.pages) > 0 else ""
    for f in FRASES:
        if norm(f) not in volante:
            erros.append(f"volante: frase ausente {f[:38]!r}")
    for n in range(1, 11):
        if f"{n:02d}" not in volante.replace(" ", ""):
            erros.append(f"volante: numeracao {n:02d} ausente")

    if len(r.pages) > 1:
        contra = norm(r.pages[1].extract_text())
        if contra.strip():
            erros.append(f"contraguarda devia ser so o logo, achei texto: {contra[:40]!r}")

    for i, p in enumerate(r.pages, 1):
        t = p.extract_text()
        for v in VAZAMENTOS:
            if v in t:
                erros.append(f"pagina {i}: marcacao vazada {v!r}")

    if erros:
        print(f"FALHOU ({len(erros)}):")
        for e in erros:
            print("  -", e)
        return 1
    print("OK: 2 faces A4 paisagem, 10 frases na volante, logo na contraguarda")
    return 0


if __name__ == "__main__":
    sys.exit(main())
