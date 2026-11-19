# Fontes de referência

Material consultado para escrever o manual. **Não editar** — é fonte.

## `roberts-etherington.json`

**Roberts, Matt T.; Etherington, Don.** *Bookbinding and the Conservation
of Books: A Dictionary of Descriptive Terminology.* Washington: Library of
Congress, 1982. 3.861 verbetes.

A referência canônica em inglês. Extraído do SGML da edição eletrônica em
`cool.culturalheritage.org/don/` (Conservation OnLine). Formato:
`{"termo": "definição"}`.

Consultar assim:
```bash
python3 -c "import json;d=json.load(open('fontes/roberts-etherington.json'));print(d['squares'])"
```

## `BN_marsico_encadernacao.txt`

**Mársico, Cida.** *O surgimento da encadernação e da douração.* Fundação
Biblioteca Nacional. Texto de conservadora-restauradora da FBN, com
glossário em português do Brasil ao final.

Fonte institucional brasileira — tem precedência sobre dicionário de
Portugal quando os dois divergem e o uso corrente aqui for diferente.

## Outras consultadas (não baixadas)

- **Ligatus, *Language of Bindings*** — `ligatus.org.uk/lob/`. Tesauro de
  ~1.000 termos, estruturas do séc. IX ao XIX. Bom para encadernação
  histórica.
- **Tesauro UFRGS** — `ufrgs.br/tesauros`. Bibliográfico, não técnico de
  oficina: útil para nomes de tipos de encadernação, fraco para peças.
- **Faria & Pericão**, *Dicionário do livro* (Lisboa, 1988) — citado pela
  BN; português europeu.
- **Castelo Branco, Zelina**, *Encadernação* (Hucitec, 1978) — manual
  brasileiro clássico, citado pela BN. **Vale procurar.**
