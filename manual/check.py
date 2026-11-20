#!/usr/bin/env python3
"""Confere o PDF compilado do manual — não o fonte.

Na linha do check.py dos outros volumes: verifica o que a encadernação
exige e o que costuma quebrar silenciosamente na conversão MD→Typst.
"""
import sys, re, pathlib, math
from pypdf import PdfReader

HERE = pathlib.Path(__file__).parent
SIG  = None  # escolhido por cadernos.py, como no Makefile
falhas = []

def ok(cond, msg):
    print(("  ok   " if cond else "  FALHA ") + msg)
    if not cond:
        falhas.append(msg)

pdf = HERE / "manual.pdf"
if not pdf.exists():
    sys.exit("manual.pdf não existe — rode make primeiro")

r = PdfReader(pdf)
n = len(r.pages)
paginas = [p.extract_text() for p in r.pages]
texto = "\n".join(paginas)

import pathlib as _pl, re as _re
print(f"\nmanual.pdf — {n} páginas")

esqueletos = texto.count("ESQUELETO")

print("\nEncadernação")
# Mesmo critério do Makefile: o tamanho que deixa menos páginas em branco.
sys.path.insert(0, str(HERE))
from cadernos import escolhe
SIG = escolhe(n)
cadernos = math.ceil(n / SIG)
brancas = cadernos * SIG - n
# Paridade e encaixe de cadernos só valem quando o texto parar de mudar;
# com esqueletos a paginação é provisória.
if esqueletos:
    print(f"  --   {n} páginas, {'par' if n % 2 == 0 else 'ÍMPAR'} (provisório)")
else:
    ok(n % 2 == 0, f"contagem par ({n})")
# Enquanto houver capítulos em esqueleto a paginação é provisória; só
# exigimos encaixe bom quando o manual estiver escrito.
if esqueletos:
    print(f"  --   {cadernos} cadernos de {SIG}, {brancas} brancas "
          f"(provisório: {esqueletos} capítulos em esqueleto)")
else:
    ok(brancas <= SIG // 2,
       f"{cadernos} cadernos de {SIG}, {brancas} páginas em branco no fim")

print("\nGeometria")
larguras = {round(float(p.mediabox.width) / 72 * 25.4) for p in r.pages}
alturas  = {round(float(p.mediabox.height) / 72 * 25.4) for p in r.pages}
ok(larguras == {148} and alturas == {210},
   f"todas as páginas A5 148×210 (achado {larguras}×{alturas})")

print("\nConteúdo")
PARTES = ["I · O que é um livro", "II · O miolo", "III · Da costura à capa",
          "IV · Revestimento e acabamento", "V · O livro que já existe",
          "Apêndices"]
CAPS = ["Breve história do livro", "Anatomia do livro",
        "Tipos de encadernação", "Tipografia e editoração", "Papel",
        "Impressão do miolo", "Cadernos e imposição", "Costura",
        "Do miolo costurado ao bloco pronto", "Colas e adesivos",
        "Guardas", "Montagem da capa", "Capas em papel e tecido",
        "Capas em couro", "Douração e cortes",
        "Foil, latão e impressão na capa",
        "Plotter de corte e técnicas modernas", "Papéis decorados",
        "Caixas, estojos e proteção", "Reencadernação",
        "Restauração e conservação",
        "A · Consulta rápida", "B · Glossário português / inglês",
        "C · Fornecedores no Brasil", "D · Medidas e folgas",
        "E · Protocolos de teste", "F · Ordem de operações"]
# Os 21 capítulos saem numerados ("10 · Colas e adesivos"); os apêndices
# já trazem a letra.
CAPS = [f"{i} · {t}" for i, t in enumerate(CAPS[:21], 1)] + CAPS[21:]
def norm(s):
    return re.sub(r'\s+', ' ', s)

# Buscar no texto inteiro daria falso negativo: todo capítulo aparece
# também no sumário. Exigimos o título no TOPO de alguma página — mas a
# primeira linha extraída pode ser o cabeçalho corrente (que ainda traz o
# capítulo anterior), então olhamos as duas primeiras.
# Um título longo quebra em duas linhas na folha de rosto ("IV · Reves-
# timento e / acabamento"), então comparar linha a linha dá falso
# negativo. Juntamos as primeiras linhas de cada página e procuramos o
# título como substring, sem hífen de quebra.
aberturas = set()
for pg in paginas:
    linhas = [l for l in pg.strip().split("\n") if l.strip()][:3]
    junto = norm(" ".join(linhas)).replace("\u00ad", "").replace("- ", "")
    aberturas.add(junto)

def consta(titulo):
    t = norm(titulo)
    return any(t in a for a in aberturas)
for c in CAPS:
    ok(consta(c), f"capítulo abre em página própria: {c}")
for pt in PARTES:
    ok(consta(pt), f"parte abre em folha de rosto: {pt}")

print("\nMarcações que não podem vazar para o texto")
# Se o conversor falhar, sobra sintaxe de Markdown ou de Typst no PDF.
vazamentos = [
    (r'\*\*', "negrito Markdown (**)"),
    (r'#strong\[', "chamada Typst (#strong)"),
    (r'#emph\[', "chamada Typst (#emph)"),
    (r'#tabela\(', "chamada Typst (#tabela)"),
    (r'#regra\[', "chamada Typst (#regra)"),
    (r'\]\([^)]*\.md\)', "link Markdown para .md"),
    (r'<!|GERADO por', "comentário HTML do fonte"),
    (r'\|\s*---', "separador de tabela Markdown"),
    # o Typst converte "---" em travessão: a tabela que vaza aparece assim
    (r'\|\s*[—–]+\s*\|', "separador de tabela vazado (com travessão)"),
]
for pat, nome in vazamentos:
    achados = re.findall(pat, texto)
    ok(not achados, f"sem {nome}" + (f" — {len(achados)} ocorrência(s)" if achados else ""))

print("\nApêndices gerados")
import subprocess as _sp, hashlib as _hl
_ger = ["apendices/A-tabelas.md", "apendices/D-medidas.md", "apendices/E-testes.md"]
_antes = {f: _hl.md5(_pl.Path(f).read_bytes()).hexdigest() for f in _ger
          if _pl.Path(f).exists()}
_sp.run(["python3", "gera_apendices.py"], capture_output=True, cwd=HERE)
for f in _ger:
    depois = _hl.md5((HERE / f).read_bytes()).hexdigest()
    ok(_antes.get(f) == depois, f"em dia com os capítulos: {f}")

print("\nCaracteres que o Typst interpreta")
# "~" é espaço inquebrável no Typst: se o build.py não escapar, todo
# "~250 páginas" vira " 250 páginas" — e ninguém vê. Os 130 tils do manual
# sumiram assim até nov/2026.
_src = sum(f.read_text(encoding="utf-8").count("~")
           for d in ("capitulos", "apendices") for f in _pl.Path(d).glob("*.md"))
_pdf = texto.count("~")
ok(_pdf >= _src, f"tils preservados ({_pdf} no PDF, {_src} nos fontes)")

# ";" logo depois de negrito/itálico/código some (o Typst o lê como fim de
# comando). Conta os do texto corrido — fora de blocos de código.
def _sem_codigo(s):
    return _re.sub(r"```.*?```", "", s, flags=_re.S)
_src_pv = sum(_sem_codigo(f.read_text(encoding="utf-8")).count(";")
              for d in ("capitulos", "apendices") for f in _pl.Path(d).glob("*.md"))
_pdf_pv = texto.count(";")
ok(_pdf_pv >= _src_pv, f"pontos e vírgulas preservados ({_pdf_pv} no PDF, {_src_pv} nos fontes)")

print("\nBlocos de código")
# Um bloco cercado (```) que o build.py não reconheça vira parágrafo
# corrido — e o PDF continua "válido". Exigimos que a primeira e a última
# linha de cada bloco apareçam como linhas próprias no texto extraído.
_linhas_pdf = {norm(l) for pg in paginas for l in pg.split("\n") if l.strip()}
_nb = _ruins = 0
for _f in sorted(_pl.Path("capitulos").glob("*.md")) + sorted(_pl.Path("apendices").glob("*.md")):
    for _m in _re.finditer(r'^```[^\n]*\n(.*?)^```', _f.read_text(encoding="utf-8"), _re.S | _re.M):
        _ls = [norm(l.replace("\ufe0f", "").replace("⏱", "◷")) for l in _m.group(1).split("\n") if l.strip()]
        if not _ls:
            continue
        _nb += 1
        if not (_ls[0] in _linhas_pdf and _ls[-1] in _linhas_pdf):
            _ruins += 1
            print(f"  FALHA bloco virou parágrafo? {_f.name}: {_ls[0][:50]!r}")
ok(_ruins == 0, f"{_nb} blocos de código preservam as quebras de linha")

print("\nSumário")
# Todo título de nível 1 tem que ser capítulo ou parte. Uma célula de tabela
# começando com "=" virava título e entrava no sumário ("espessura da pasta").
def _titulos(o, d=0):
    for x in o:
        if isinstance(x, list): yield from _titulos(x, d + 1)
        elif d == 0: yield x.title
_esperados = {norm(x) for x in CAPS + PARTES}
_intrusos = [x for x in _titulos(r.outline) if norm(x) not in _esperados]
ok(not _intrusos, "sumário só com capítulos e partes" + (f" — intrusos: {_intrusos}" if _intrusos else ""))

print("\nFiguras")
import re as _re, pathlib as _pl
refs = set()
for _f in list(_pl.Path("capitulos").glob("*.md")) + list(_pl.Path("apendices").glob("*.md")):
    refs |= set(_re.findall(r'!\[[^\]]*\]\(([^)]+)\)', _f.read_text(encoding="utf-8")))
for r in sorted(refs):
    ok(_pl.Path(r).exists(), f"figura existe: {r}")
if not refs:
    print("  --   nenhuma figura referenciada ainda")

print("\nEstrutura")
ok("Sumário" in texto, "sumário presente")
ok("COLOFÃO" in texto or "C O L O F Ã O" in texto, "colofão presente")
ok(len(paginas[0]) < 400, "capa sem cabeçalho nem número")

# Página "vazia" que sai com cabeçalho e número: a função das partes
# criava seis delas, e o colofão uma. Página em branco tem que ser branca.
_quase_vazias = [i + 1 for i, pg in enumerate(paginas)
                 if pg.strip() and _re.fullmatch(r"(?:[^\n]{0,60}\n)?\d+", pg.strip())]
ok(not _quase_vazias, "nenhuma página só com cabeçalho/número"
   + (f" — físicas {_quase_vazias}" if _quase_vazias else ""))

# Abertura de capítulo não leva cabeçalho: o título é a 1ª linha da página.
_com_cab = [c for c in CAPS
            if not any(pg.strip().split("\n")[0].strip() == c for pg in paginas if pg.strip())]
ok(not _com_cab, "aberturas de capítulo sem cabeçalho"
   + (f" — {_com_cab[:3]}" if _com_cab else ""))

# A regra em destaque abre cada capítulo: 12 blocos esperados
regras = len(re.findall(r'A regra', texto))
ok(regras >= 10, f"regras em destaque encontradas: {regras}")  # esqueletos ainda não têm

print()
if falhas:
    print(f"{len(falhas)} FALHA(S):")
    for f in falhas:
        print("  -", f)
    sys.exit(1)
print("tudo certo.")
