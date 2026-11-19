#!/usr/bin/env python3
"""Gera os apêndices A, D e E a partir dos capítulos.

Em vez de manter cópias à mão (que saem de sincronia no primeiro
retoque), extraímos dos próprios capítulos:

  A — Consulta rápida ... as seções "## Consulta rápida" de cada capítulo
  D — Medidas e folgas ... as tabelas cujo conteúdo é numérico
  E — Protocolos de teste . os blocos marcados com "teste" nos capítulos

Rode antes do build; o Makefile já cuida disso.
"""
import re, pathlib, unicodedata

HERE = pathlib.Path(__file__).parent
CAPS = HERE / "capitulos"
AP   = HERE / "apendices"

def titulo_de(p: pathlib.Path) -> str:
    """O h1 do capítulo."""
    for l in p.read_text(encoding="utf-8").split("\n"):
        if l.startswith("# "):
            return l[2:].strip()
    return p.stem

def num_de(p: pathlib.Path) -> int:
    return int(p.name[:2])

def secoes(texto: str):
    """Divide em (nível, título, corpo) por heading."""
    partes = re.split(r'^(#{2,4}) (.+)$', texto, flags=re.M)
    out = []
    for i in range(1, len(partes), 3):
        out.append((len(partes[i]), partes[i+1].strip(), partes[i+2]))
    return out

def tabelas(corpo: str):
    """Extrai blocos de tabela Markdown."""
    blocos, atual = [], []
    for l in corpo.split("\n"):
        if l.lstrip().startswith("|"):
            atual.append(l)
        else:
            if len(atual) >= 2:
                blocos.append("\n".join(atual))
            atual = []
    if len(atual) >= 2:
        blocos.append("\n".join(atual))
    return blocos

# Tabelas que batem a heurística numérica mas não são medidas de bancada.
NAO_E_MEDIDA = ("proporção", "proporções", "sensação", "veredito",
                "preço", "custo", "quando cada rota compensa")

def numerica(tabela: str) -> bool:
    """A tabela é majoritariamente de medidas?"""
    celulas = [c.strip() for l in tabela.split("\n")[2:]
               for c in l.strip().strip("|").split("|")]
    if not celulas:
        return False
    com_num = sum(bool(re.search(r'\d+\s*(mm|cm|g/m|g |pt|°C|%|µ|:)', c))
                  for c in celulas)
    return com_num >= max(2, len(celulas) * 0.22)

CABECA = """<!-- GERADO por gera_apendices.py — não editar à mão. -->
"""

# ── A — Consulta rápida ───────────────────────────────────────────
def apendice_A():
    out = [CABECA, "# Apêndice A — Consulta rápida\n",
      "> Onde o leitor vai quando pensa *\"só quero tirar uma dúvida\"*.",
      "> Reúne as tabelas de abertura dos capítulos, na ordem deles.\n",
      "Cada bloco indica o capítulo de origem, onde está o porquê.\n"]
    for p in sorted(CAPS.glob("*.md")):
        for nivel, tit, corpo in secoes(p.read_text(encoding="utf-8")):
            if nivel == 2 and tit.lower().startswith("consulta rápida"):
                tabs = tabelas(corpo)
                if not tabs:
                    continue
                out.append(f"\n## {num_de(p)} · {titulo_de(p)}\n")
                sub = tit[len("consulta rápida"):].lstrip(" —–-")
                if sub:
                    out.append(f"*{sub}*\n")
                out.extend(t + "\n" for t in tabs)
                # subseções de números logo abaixo da consulta rápida
                break
    (AP / "A-tabelas.md").write_text("\n".join(out), encoding="utf-8")
    return sum(1 for l in out if l.startswith("\n## "))

# ── D — Medidas e folgas ──────────────────────────────────────────
def apendice_D():
    out = [CABECA, "# Apêndice D — Medidas e folgas\n",
      "> Todos os números do manual, numa página só, para consulta na",
      "> bancada. O porquê de cada um está no capítulo indicado.\n"]
    for p in sorted(CAPS.glob("*.md")):
        achadas = []
        for nivel, tit, corpo in secoes(p.read_text(encoding="utf-8")):
            if any(x in tit.lower() for x in NAO_E_MEDIDA):
                continue
            for t in tabelas(corpo):
                # a 1ª linha da tabela também denuncia conteúdo não-métrico
                cab = t.split("\n")[0].lower()
                if any(x in cab for x in NAO_E_MEDIDA):
                    continue
                if numerica(t) and all(t != x[1] for x in achadas):
                    achadas.append((tit, t))
        if achadas:
            out.append(f"\n## {num_de(p)} · {titulo_de(p)}\n")
            usados = {}
            for tit, t in achadas:
                usados[tit] = usados.get(tit, 0) + 1
                rot = tit if usados[tit] == 1 else f"{tit} ({usados[tit]})"
                out.append(f"**{rot}**\n")
                out.append(t + "\n")
    (AP / "D-medidas.md").write_text("\n".join(out), encoding="utf-8")
    return sum(1 for l in out if l.startswith("\n## "))

# ── E — Protocolos de teste ───────────────────────────────────────
def apendice_E():
    out = [CABECA, "# Apêndice E — Protocolos de teste\n",
      "> Os testes que o manual manda fazer, reunidos. Quase todos levam",
      "> minutos e evitam estragar a peça.\n"]
    vistos = set()
    for p in sorted(CAPS.glob("*.md")):
        achadas = []
        for nivel, tit, corpo in secoes(p.read_text(encoding="utf-8")):
            t = tit.lower()
            if "teste" in t or "protocolo" in t or "checagem" in t:
                txt = corpo.strip()
                if txt and txt not in vistos:
                    vistos.add(txt)
                    achadas.append((tit, txt))
        if achadas:
            out.append(f"\n## {num_de(p)} · {titulo_de(p)}\n")
            for tit, txt in achadas:
                out.append(f"### {tit}\n")
                out.append(txt + "\n")
    (AP / "E-testes.md").write_text("\n".join(out), encoding="utf-8")
    return sum(1 for l in out if l.startswith("\n## "))

if __name__ == "__main__":
    a, d, e = apendice_A(), apendice_D(), apendice_E()
    for nome, n, f in (("A — Consulta rápida", a, "A-tabelas.md"),
                       ("D — Medidas", d, "D-medidas.md"),
                       ("E — Testes", e, "E-testes.md")):
        kb = (AP / f).stat().st_size / 1024
        print(f"  {nome:22s} {n:2d} capítulos, {kb:5.1f} KB")
