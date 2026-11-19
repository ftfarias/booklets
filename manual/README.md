# Manual do Encadernador Novato (com mania de saber detalhe de tudo)

Compilação de material de pesquisa sobre encadernação, restauração e o lado
editorial, reunido a partir de conversas separadas com LLM (Poe / Claude Opus)
ao longo de 2026.

**Comece por [`MANUAL.md`](MANUAL.md)** — índice temático e "onde encontrar".

## Estrutura

```
manual/
  MANUAL.md       Índice geral, perguntas frequentes e as regras que atravessam tudo.
  NEGOCIO.md      O lado editora/empresa: preço, investimento, jurídico, ISBN, marca.
  ESTRUTURA.md    Plano da reorganização de nov/2026.
  capitulos/      Os 21 capítulos, na ordem em que o livro nasce.
  apendices/      Consulta rápida, glossário, fornecedores, medidas,
                  testes e ordem de operações. A, D e E são gerados.
  raw/            Conversas originais, íntegras (verbatim). Fonte bruta — não editar.
    _INDEX.md     Lista das 21 conversas com título e tema.
    _duplicatas/  Conversas 06 e 07 (mesmas da 03 e 04, por outro link).
  build.py        Converte os .md em typst/corpo.typ.
  gera_apendices.py  Extrai os apêndices A, D e E dos capítulos.
  check.py        Confere o PDF compilado.
  cadernos.py     Escolhe o tamanho de caderno que desperdiça menos.
  typst/          manual.typ (mestre), helpers.typ, corpo.typ (gerado).
  README.md       Este arquivo.
```

## Imprimir

```bash
make            # manual.pdf + manual_booklet.pdf (imposto)
make check      # confere o PDF compilado
make preview    # PNGs de páginas-amostra
```

O tamanho do caderno — 12, 16 ou 20 páginas (3, 4 ou 5 folhas A4) — é
escolhido pelo `cadernos.py` para deixar o mínimo de páginas em branco no
fim, com preferência por 16, o padrão que o `../README.md` recomenda. O
`make` imprime a escolha (*"[1/17] pages 1–16"* = 17 cadernos de 16).

Imprimir `manual_booklet.pdf`. **Cada página do PDF é um lado de folha:**
o número de folhas de papel é a metade das páginas do PDF (o `booklet.py`
chama de *sheets* o que são lados).

1. **Tamanho real / 100%** — nunca "Ajustar", nunca "Livreto".
2. **Frente e verso, virar na borda curta.** No Adobe Reader os nomes vêm
   invertidos — se sair errado, gere com `--long-edge`.
3. Teste as páginas 1–2 primeiro: dobre e confira se lê na ordem.
4. Papel: Pólen Bold 90 g/m², **fibra paralela à lombada** — a regra que
   abre o cap. 5.

Dobre cada folha, aninhe as folhas de cada caderno, empilhe os cadernos na
ordem e costure. Lombada estimada: (páginas ÷ 2) × 0,135 mm em pólen 90 —
uns 18 mm para ~270 páginas. Meça o miolo real antes de cortar a capa.

## Fonte e conversão

Os capítulos são Markdown; `build.py` converte para Typst (headers,
tabelas, blockquotes, listas, negrito/itálico/código). Não usa pandoc —
segue o padrão dos `build.py` dos outros volumes. A tipografia é a mesma
da casa: Libertinus Serif, A5 148×210, margem interna de 21 mm.

Editou um capítulo? `make` refaz tudo.

## Por que existe

O material estava espalhado por 23 conversas e achar uma resposta exigia
reler tudo. Os capítulos condensam por assunto, cada um com uma regra em
destaque e uma tabela de consulta rápida no topo.

**Novembro de 2026:** reorganizado de enciclopédia-por-material para a
ordem em que o livro nasce — seis partes, da história do livro até o
restauro. Sete capítulos e cinco apêndices ainda são esqueletos; ver
`ESTRUTURA.md`. O capítulo de Art Déco saiu para `../arte-deco/`, onde
vira livro próprio.

O lado *negócio* ficou em `NEGOCIO.md`, separado do ofício. As formas de
comercialização e os nichos considerados continuam em `../CAMINHOS.md`, que
`NEGOCIO.md` complementa em vez de repetir.

## Status

- [x] Baixar as conversas para `raw/` (21 únicas + 2 duplicatas)
- [x] Definir a taxonomia de capítulos
- [x] Escrever os 11 capítulos + `NEGOCIO.md`
- [x] Montar o `MANUAL.md` com índice e busca por pergunta
- [x] Gerar o PDF A5 e a versão imposta para impressão
- [x] Reorganizar na ordem em que o livro nasce (nov/2026)
- [x] **Escrever os 21 capítulos**
- [x] **Montar os 6 apêndices** (A, D, E gerados dos capítulos)
- [ ] Imprimir e encadernar
- [ ] Revisar contra a prática — corrigir o que a bancada desmentir

## Ressalva

Vem de LLM e pode conter erro. Preço, disponibilidade no Brasil e nome
comercial de produto são os itens de menor confiança — confirme antes de
comprar. Teste antes de aplicar em peça que importa.
