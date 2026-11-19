#!/usr/bin/env python3
"""Escolhe o tamanho de caderno que deixa menos páginas em branco.

O número de páginas do manual muda a cada revisão; fixar o caderno à mão
obrigava a trocá-lo toda vez. Candidatos: 12, 16 e 20 páginas (3, 4 e 5
folhas A4). Em empate, 16 — as 4 folhas que o README do booklet.py
recomenda.

    python3 cadernos.py manual.pdf      → imprime só o número (para o make)
"""
import sys, math
from pypdf import PdfReader

CANDIDATOS = (16, 12, 20)          # ordem = preferência no empate

def escolhe(n):
    return min(CANDIDATOS, key=lambda s: math.ceil(n / s) * s - n)

if __name__ == "__main__":
    n = len(PdfReader(sys.argv[1] if len(sys.argv) > 1 else "manual.pdf").pages)
    print(escolhe(n))
