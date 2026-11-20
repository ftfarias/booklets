#!/usr/bin/env python3
"""Converte os capítulos Markdown do manual em fragmentos Typst.

Entrada:  MANUAL.md, capitulos/*.md, NEGOCIO.md
Saída:    typst/corpo.typ  (um único fragmento, com todos os capítulos)

O Markdown do manual usa um subconjunto previsível: headers h1-h4, tabelas
GFM, blockquotes, listas com - e 1., negrito, itálico, código inline e links.
Não há blocos de código, HTML embutido nem imagens — por isso um conversor
próprio (no padrão dos build.py dos outros volumes) resolve, sem pandoc.
"""
import re, pathlib, sys

HERE = pathlib.Path(__file__).parent
CAPS = HERE / "capitulos"
OUT  = HERE / "typst" / "corpo.typ"

# Ordem de impressão. O MANUAL.md vira a abertura; NEGOCIO.md vai ao final
# como parte separada, espelhando a separação que existe nos arquivos.
# Ordem de impressão: a ordem em que o livro nasce, não por material.
# (None, "nome") abre uma parte; (arquivo, título) é um capítulo.
ORDEM = [
    (None, "I · O que é um livro"),
    ("capitulos/01-historia-do-livro.md",             "Breve história do livro"),
    ("capitulos/02-anatomia-do-livro.md",             "Anatomia do livro"),
    ("capitulos/03-tipos-de-encadernacao.md",         "Tipos de encadernação"),

    (None, "II · O miolo"),
    ("capitulos/04-tipografia-e-editoracao.md",       "Tipografia e editoração"),
    ("capitulos/05-papel.md",                         "Papel"),
    ("capitulos/06-impressao.md",                     "Impressão do miolo"),
    ("capitulos/07-cadernos-e-imposicao.md",          "Cadernos e imposição"),
    ("capitulos/08-costura.md",                       "Costura"),
    ("capitulos/09-do-miolo-ao-bloco.md",             "Do miolo costurado ao bloco pronto"),

    (None, "III · Da costura à capa"),
    ("capitulos/10-colas.md",                         "Colas e adesivos"),
    ("capitulos/11-guardas.md",                       "Guardas"),
    ("capitulos/12-montagem-da-capa.md",              "Montagem da capa"),

    (None, "IV · Revestimento e acabamento"),
    ("capitulos/13-capas-em-papel-e-tecido.md",       "Capas em papel e tecido"),
    ("capitulos/14-capas-em-couro.md",                "Capas em couro"),
    ("capitulos/15-douracao-e-cortes.md",             "Douração e cortes"),
    ("capitulos/16-foil-latao-e-impressao-na-capa.md","Foil, latão e impressão na capa"),
    ("capitulos/17-plotter-e-tecnicas-modernas.md",   "Plotter de corte e técnicas modernas"),
    ("capitulos/18-papeis-decorados.md",              "Papéis decorados"),
    ("capitulos/19-caixas-e-estojos.md",              "Caixas, estojos e proteção"),

    (None, "V · O livro que já existe"),
    ("capitulos/20-reencadernacao.md",                "Reencadernação"),
    ("capitulos/21-restauro-e-conservacao.md",        "Restauração e conservação"),

    (None, "Apêndices"),
    ("apendices/A-tabelas.md",            "A · Consulta rápida"),
    ("apendices/B-glossario.md",          "B · Glossário português / inglês"),
    ("apendices/C-fornecedores.md",       "C · Fornecedores no Brasil"),
    ("apendices/D-medidas.md",            "D · Medidas e folgas"),
    ("apendices/E-testes.md",             "E · Protocolos de teste"),
    ("apendices/F-ordem-de-operacoes.md", "F · Ordem de operações"),
]


# ── Escape ────────────────────────────────────────────────────────────
# Typst trata estes como marcação. Escapamos tudo que não vamos converter.
ESC = "\\#$@<>_*~"   # ~ é espaço inquebrável no Typst: sem escape, some

def esc(s):
    """Escapa texto puro para Typst (sem tocar em marcação já convertida)."""
    s = s.replace("\\", "\\\\")
    for ch in ESC[1:]:
        s = s.replace(ch, "\\" + ch)
    return s

def inline(s):
    """Converte marcação inline do Markdown para Typst.

    Converte primeiro (código, links, negrito, itálico) guardando cada
    resultado num marcador opaco; só então escapa o texto puro restante.
    Assim o escape nunca come a marcação, e um `_` ou `*` solto (como em
    "Laus ___") vira literal em vez de abrir ênfase.

    Os marcadores vivem numa lista passada adiante nas chamadas
    recursivas — se cada nível criasse a sua, os marcadores do nível
    interno nunca seriam restaurados e vazariam como \x00 no PDF.
    """
    return _inline(s, [])

def _inline(s, guardados):
    def guarda(txt):
        guardados.append(txt)
        return f"\x00{len(guardados)-1}\x00"

    # `código`
    s = re.sub(r'`([^`]+)`',
               lambda m: guarda('#raw("' + m.group(1).replace('\\','\\\\').replace('"','\\"') + '")'),
               s)

    # ![legenda](caminho) → figura. Antes do link, senão vira texto solto.
    s = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',
               lambda m: guarda(f'#figura("{m.group(2)}", [{_inline(m.group(1), guardados)}])'), s)

    # [texto](destino) → só o texto; link entre arquivos não serve no PDF
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: m.group(1), s)

    # Negrito e itálico. O Markdown permite aninhar (**a *b* c**) e fechar
    # os dois de uma vez (***a***). Consumimos o par externo ** primeiro,
    # deixando o miolo para a recursão tratar o * interno — assim o caso
    # "**Mahé, *Bibliografia***" não deixa asterisco órfão.
    s = re.sub(r'\*\*(.+?)\*\*(?!\*)',
               lambda m: guarda("#strong[" + _inline(m.group(1), guardados) + "]"), s)
    s = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)',
               lambda m: guarda("#emph[" + _inline(m.group(1), guardados) + "]"), s)

    s = esc(s)

    # Logo depois de um comando (#strong[…], #emph[…], #raw(…)), o Typst lê
    # ";" como fim do comando e o engole em silêncio; "(" e "." viram
    # argumento ou acesso a campo. Escapamos o caractere seguinte. Foi assim
    # que "*case*; não exige" virou "case não exige".
    s = re.sub(r'(\x00\d+\x00)([;(.])', r'\1\\\2', s)
    for i, g in enumerate(guardados):
        s = s.replace(f"\x00{i}\x00", g)
    return s

def celula(s):
    """Célula de tabela: converte o inline e protege o começo.

    Dentro de [ ], o Typst lê o começo da célula como início de linha: "= x"
    vira TÍTULO de nível 1 (a célula "= espessura da pasta" entrou no sumário
    como capítulo), "- x" e "+ x" viram lista, "/ x" vira lista de termos.
    Escapamos o marcador quando ele vem seguido de espaço.
    """
    s = inline(s.strip())
    return re.sub(r'^([=+/-])(?=\s)', r'\\\1', s)

# ── Blocos ────────────────────────────────────────────────────────────

def parse(md, arquivo):
    """Percorre o Markdown linha a linha e emite Typst."""
    # Comentário HTML (<!-- … -->) é nota para quem edita o fonte — os
    # apêndices gerados trazem um. Sem isto, saía impresso no livro.
    md = re.sub(r'<!--.*?-->\n?', '', md, flags=re.S)
    out, i = [], 0
    linhas = md.split("\n")
    n = len(linhas)

    while i < n:
        L = linhas[i]

        # --- bloco de código cercado (```): preserva quebras e alinhamento.
        # Antes de tudo, senão o conteúdo vira parágrafo corrido — foi o que
        # aconteceu com a sequência de 41 passos do apêndice F.
        if L.startswith("```"):
            bloco = []
            i += 1
            while i < n and not linhas[i].startswith("```"):
                bloco.append(linhas[i])
                i += 1
            i += 1                                   # pula o ``` de fechamento
            # Emoji com seletor de variação (⚠️) é desenhado mais largo que
            # uma célula monoespaçada e desalinha as colunas; a forma de
            # texto (⚠) não.
            bloco = [l.replace("\ufe0f", "") for l in bloco]
            # ⏱ não existe na fonte mono e cai noutra, mais larga; ◷ existe.
            bloco = [l.replace("⏱", "◷") for l in bloco]
            largura = max((len(l) for l in bloco), default=1)
            literal = "\n".join(bloco).replace("\\", "\\\\").replace('"', '\\"')
            out.append(f'#codigo({largura}, raw("{literal}", block: true))')
            continue

        # --- separador horizontal: usamos como respiro, não como régua
        if re.match(r'^---+\s*$', L):
            out.append("#v(0.6em)")
            i += 1; continue

        # --- headers
        m = re.match(r'^(#{1,4})\s+(.*)$', L)
        if m:
            nivel, txt = len(m.group(1)), inline(m.group(2))
            # h1 do arquivo já virou título de capítulo no mestre
            if nivel == 1:
                i += 1; continue
            # "1. Título" — a numeração manual do NEGOCIO.md é redundante
            # com a ordem do sumário e, sendo mais larga, força quebra de
            # linha nas entradas. Removida.
            txt = re.sub(r'^\d+\.\s+', '', txt)
            out.append(f"#heading(level: {nivel})[{txt}]")
            i += 1; continue

        # --- blockquote (a "regra em destaque" no topo de cada capítulo)
        if L.startswith(">"):
            bloco = []
            while i < n and (linhas[i].startswith(">") or
                             (bloco and linhas[i].strip() and not linhas[i].startswith(("#","|","-","*")))):
                bloco.append(re.sub(r'^>\s?', '', linhas[i]))
                i += 1
            texto = inline(" ".join(x.strip() for x in bloco if x.strip()))
            out.append(f"#regra[{texto}]")
            continue

        # --- tabela
        if L.startswith("|") and i + 1 < n and re.match(r'^\|[\s:|-]+\|?\s*$', linhas[i+1]):
            cab = [c.strip() for c in L.strip().strip("|").split("|")]
            ncols = len(cab)
            i += 2
            corpo = []
            while i < n and linhas[i].startswith("|"):
                cs = [c.strip() for c in linhas[i].strip().strip("|").split("|")]
                cs = (cs + [""] * ncols)[:ncols]      # normaliza colunas
                corpo.append(cs)
                i += 1
            cabs = ", ".join(f"[{celula(c)}]" for c in cab)
            cels = ",\n    ".join(
                ", ".join(f"[{celula(c)}]" for c in linha) for linha in corpo)
            out.append(f"#tabela({ncols})(\n  ({cabs}),\n  (\n    {cels}\n  )\n)")
            continue

        # --- lista (com aninhamento por indentação)
        if re.match(r'^\s*([-*]|\d+\.)\s+', L):
            itens = []
            while i < n and (re.match(r'^\s*([-*]|\d+\.)\s+', linhas[i]) or
                             (linhas[i].startswith("  ") and linhas[i].strip())):
                itens.append(linhas[i])
                i += 1
            out.append(lista(itens))
            continue

        # --- linha em branco
        if not L.strip():
            i += 1; continue

        # --- parágrafo
        par = []
        while i < n and linhas[i].strip() and not re.match(
                r'^(#{1,4}\s|>|\||\s*([-*]|\d+\.)\s|---+\s*$)', linhas[i]):
            par.append(linhas[i].strip())
            i += 1
        if par:
            out.append(re.sub(r'  +', ' ', inline(" ".join(par))))

    return "\n\n".join(out)

def lista(linhas):
    """Reconstrói lista Markdown (possivelmente aninhada) em Typst."""
    saida, i, n = [], 0, len(linhas)
    while i < n:
        L = linhas[i]
        m = re.match(r'^(\s*)([-*]|\d+\.)\s+(.*)$', L)
        if not m:
            i += 1; continue
        ind, marca, txt = len(m.group(1)), m.group(2), m.group(3)
        # continuação do item (linhas indentadas que não são novo item)
        i += 1
        while i < n and linhas[i].strip() and not re.match(r'^\s*([-*]|\d+\.)\s+', linhas[i]):
            txt += " " + linhas[i].strip()
            i += 1
        # sub-itens
        sub = []
        while i < n:
            m2 = re.match(r'^(\s*)([-*]|\d+\.)\s+', linhas[i])
            if m2 and len(m2.group(1)) > ind:
                sub.append(linhas[i]); i += 1
            elif m2 and len(m2.group(1)) <= ind:
                break
            else:
                break
        corpo = inline(txt)
        if sub:
            corpo += "\n" + lista(sub)
        ordenada = marca not in ("-", "*")
        saida.append((ordenada, corpo))

    if not saida:
        return ""
    ordenada = saida[0][0]
    marca = "+" if ordenada else "-"
    return "\n".join(f"{marca} {c}" for _, c in saida)

# ── Montagem ──────────────────────────────────────────────────────────

def main():
    partes = []
    for rel, titulo in ORDEM:
        if rel is None:                       # abertura de parte
            partes.append(f'\n// ══════ {titulo} ══════\n'
                          f'#parte[{esc(titulo)}]\n')
            continue
        p = HERE / rel
        if not p.exists():
            sys.exit(f"faltando: {rel}")
        md = p.read_text(encoding="utf-8")
        # O título vem do h1 do próprio arquivo — fonte única. Antes vinha
        # da ORDEM e divergia do h1 em 13 arquivos; o apêndice A, que lê o
        # h1, mostrava o mesmo capítulo com dois nomes.
        h1 = re.search(r'^# (.+)$', md, re.M)
        if h1:
            titulo = re.sub(r'^Apêndice ([A-Z]) — ', r'\1 · ', h1.group(1).strip())
        # Capítulo numerado na abertura, no sumário e no cabeçalho: o texto
        # faz quase duzentas remissões do tipo "cap. 12", e sem o número
        # impresso o leitor tinha de contar linhas no sumário.
        m = re.match(r'capitulos/(\d+)-', rel)
        if m:
            titulo = f"{int(m.group(1))} · {titulo}"
        corpo = parse(md, rel)
        partes.append(f'\n// ══ {titulo} ({rel}) ══\n'
                      f'#capitulo[{esc(titulo)}]\n\n{corpo}\n')

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("// Gerado por build.py — não editar à mão.\n"
                   '#import "helpers.typ": *\n' + "".join(partes),
                   encoding="utf-8")
    caps = sum(1 for r, _ in ORDEM if r)
    print(f"escrito {OUT.relative_to(HERE)} "
          f"({len(OUT.read_text(encoding='utf-8')):,} caracteres, "
          f"{caps} capítulos)")

if __name__ == "__main__":
    main()
