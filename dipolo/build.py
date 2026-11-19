#!/usr/bin/env python3
"""
Gera os fragmentos Typst a partir de raw/frases.md.

O caderno tem duas partes impressas e uma enorme parte em branco:
  - frases.typ    : as 10 frases, uma por bifolio de verge
  - (o miolo em branco nao e composto aqui: e papel dobrado, sem impressao)

As frases sao impressas SEPARADAMENTE, em verge 120g, e cada bifolio e
aninhado no meio de um caderno. Ver PAPEL_E_ESTRUTURA.md.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
RAW  = ROOT / "raw" / "frases.md"
OUT  = ROOT / "typst" / "frases.typ"

# Erratas: corrige erros pontuais da fonte. Cada entrada DEVE casar --
# se o erro sumir do raw, o build falha em vez de envelhecer em silencio.
ERRATA = {}


# Versoes inglesas, extraidas de dipolo.ai e raphaelballet.com/en em
# 18/09/2026. NAO usadas na composicao: decidido manter so o portugues,
# a lingua em que ele escreve como brasileiro. Mantidas aqui porque a
# decisao pode voltar atras e a coleta foi trabalhosa. Ver raw/frases.md.
EN = {
 1: "Fewer demos. More results.",
 2: "Done is better than perfect.",
 3: "A proof of concept that never makes it into daily work does not count.",
 4: "The bones were real. The story wasn't.",
 5: "Writing forces you to be precise. You can't get away with a vague "
    "understanding when you have to explain it from scratch.",
 6: "Data alone is never enough.",
 7: "The documentation is not the system.",
 8: "An artifact, still doing its job, after the world that needed it "
    "has moved on.",
 9: "The best way to actually understand something is to try to explain "
    "it to someone else.",
 10: "I write when I have something worth saying.",
}


def parse(md: str):
    """Extrai (n, texto, fonte) de cada bloco '## NN — frase'."""
    frases = []
    # so a secao principal; para em '## Reservas'
    corpo = md.split("## Reservas")[0]
    blocos = re.findall(
        r"^## (\d{2}) — (.+?)\n\n\*\((.+?)\)\*", corpo, re.M | re.S
    )
    for num, texto, fonte in blocos:
        texto = " ".join(texto.split())
        frases.append((int(num), texto, fonte.strip()))
    return frases


def main():
    md = RAW.read_text(encoding="utf-8")

    for errado, certo in ERRATA.items():
        if errado not in md:
            raise SystemExit(
                f"ERRATA obsoleta: {errado!r} nao esta mais em {RAW.name}. "
                "Remova a entrada."
            )
        md = md.replace(errado, certo)

    frases = parse(md)
    if len(frases) != 10:
        raise SystemExit(f"esperava 10 frases, achei {len(frases)}")

    # A 07 e cortada: a original depende do contexto. raw/ registra o porque.
    subst = {7: "A documentação não é o sistema."}
    frases = [(n, subst.get(n, t), f) for n, t, f in frases]

    # Corpo por frase. As longas baixam para equilibrar as linhas e evitar
    # viuva na ultima -- check.py reprova se sobrar alguma.
    CORPO = {3: 14, 5: 14, 8: 15.5, 9: 15.5, 10: 16}

    linhas = [
        '#import "helpers.typ": *',
        "",
        "// Gerado por build.py — nao edite a mao.",
        "",
    ]
    for i, (n, texto, fonte) in enumerate(frases):
        args = [str(n)]
        if n in CORPO:
            args.append(f"corpo: {CORPO[n]}pt")
        linhas.append(f"#frase({', '.join(args)})[{texto}][{fonte}]")
        # verso em branco: a frase cai sempre no recto. O ultimo verso
        # nao precisa de quebra — senao sobra uma pagina vazia no fim.
        linhas.append("#pagebreak()")
        if i < len(frases) - 1:
            linhas.append("#pagebreak()")
    OUT.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)}: {len(frases)} frases")


if __name__ == "__main__":
    main()
