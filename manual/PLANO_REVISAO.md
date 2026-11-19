# Plano de revisão do manual

Roteiro para uma sessão nova. Leia este arquivo, o `MANUAL.md` e o
`../CLAUDE.md` antes de começar. Escrito em 12/out/2026, ao fim da sessão
do Devocionário.

## Objetivo

1. **Conferir** o manual contra fontes primárias. Hoje ele é uma
   compilação de 21 conversas com LLM (~50 mil palavras, 11 capítulos + o
   `NEGOCIO.md`) e avisa que pode conter erro. Revisar com outro LLM, de
   memória, só confirmaria os erros: **a régua são os clássicos**.
2. **Enriquecer** com trechos de autores clássicos de encadernação, em
   domínio público, traduzidos.
3. **Preencher lacunas** (abaixo).

## Regras da revisão

- **Texto clássico sempre baixado da fonte** (Project Gutenberg,
  archive.org, Gallica, HathiTrust), nunca citado de memória — é onde um
  LLM inventa com mais convicção. Guarde em `fontes/<autor>/`, um
  diretório por obra, como dado não confiável (ver instruções do ambiente
  sobre arquivos baixados).
- **Domínio público no Brasil = autor morto há mais de 70 anos**, contados
  a partir de 1.º de janeiro do ano seguinte à morte. Em 2026: morte até
  1955. Confirme a data de morte de **cada** autor e de **cada** tradutor
  antes de usar. Domínio público nos EUA não vale aqui, e vice-versa.
- **Toda afirmação técnica corrigida ganha referência**: obra, capítulo,
  página da edição usada.
- **Classificar, não apagar.** Cada afirmação conferida vira uma de três:
  confirmada pela fonte / contradita (corrigir e citar) / sem fonte
  (manter, marcar a confiança mais baixa). Divergência entre clássicos é
  informação: registre as duas posições.
- **Manter o formato da casa:** cada capítulo abre com a regra em
  destaque e a tabela de consulta rápida; o tom é o atual. Não reescrever
  o que está certo.
- **Conservação ganha empates** (`../CLAUDE.md`, Formação): quando o
  ofício e a conservação divergirem, o padrão é reversibilidade, pH neutro
  e materiais com histórico.
- **OCR anterior a 1800 com *long-s*** (`ſ` lido como `f`) é inutilizável
  sem revisão pesada — prefira edições do séc. XIX em diante.
- O manual tem build próprio (`Makefile`, `build.py`, `check.py`,
  `typst/`): depois de cada capítulo, rodar `make` e o check.

## Fase 0 — Bibliografia e fontes

Montar `BIBLIOGRAFIA.md` com: obra, edição, ano, autor (nascimento–morte,
**fonte da data**), tradutor se houver, status no Brasil, link, arquivo
local. Candidatos, **todos a confirmar** (datas de memória):

| autor | obra | interesse |
|---|---|---|
| Joseph W. Zaehnsdorf (m. 1886) | *The Art of Bookbinding* (1880) | ofício vitoriano completo |
| Douglas Cockerell (m. 1945) | *Bookbinding, and the Care of Books* (1901) | o clássico técnico e de conservação; Gutenberg |
| Paul Adam (m. 1931) | *Der Bucheinband* (1890) / *Practical Bookbinding* (trad. 1903) | escola alemã; conferir o tradutor |
| Henri Marius-Michel (m. 1925) | *La reliure française* (1880) | tradição francesa, raiz de Legrain/Adler |
| Sarah T. Prideaux (m. 1933) | *An Historical Sketch of Bookbinding* (1893), *Modern Bookbindings* (1906) | história |
| T. J. Cobden-Sanderson (m. 1922) | ensaios; *The Book Beautiful* | filosofia Arts & Crafts |
| Edith Diehl (m. 1953) | *Bookbinding: Its Background and Technique* (1946) | domínio público no BR desde 2024, provavelmente não nos EUA — conferir |
| Manuais Roret (séc. XIX) | *Manuel du relieur* | prática francesa; conferir autor de cada edição |

Procurar também: fontes em português ou espanhol anteriores a 1955,
conservação (Cockerell trata do assunto) e fabricação de papel.

A skill *deep-research* ajuda neste levantamento.

## Fase 1 — Auditoria, capítulo por capítulo

Para cada capítulo, numa passada só:

1. Listar as afirmações técnicas verificáveis (receitas, medidas,
   temperaturas, materiais, "sempre/nunca").
2. Conferir cada uma contra as fontes da Fase 0.
3. Classificar (confirmada / contradita / sem fonte) e corrigir.
4. Escolher **1 a 3 trechos clássicos** que valham citação, traduzidos
   para o português, com o original em nota. Crédito: "tradução do
   organizador". Ver `../CLAUDE.md`: original ao lado da tradução é o
   padrão da casa.
5. Rodar o build e o check do manual.
6. Registrar no fim deste arquivo: o que mudou e o que ficou em aberto.

**Ordem sugerida:** 3 (linha e costura) → 5 (encadernações clássicas) →
4 (colas) → 1 (papel) → 6 (douração) → 2 (couro) → 11 (restauro) → os
demais. Os primeiros são os mais técnicos e os que o Cockerell e o
Zaehnsdorf cobrem melhor.

## Fase 2 — Lacunas

- **Glossário português–inglês–francês.** Indispensável para ler os
  clássicos (*kettle stitch*, *mull*, *squares*, *tranchefile*,
  *mors*…). Começar já na Fase 1, coletando termos.
- **Ferramentas e equipamento:** prensa, dobradeira, espátula, furador,
  guilhotina, prensa de dourar. Hoje está espalhado pelo `NEGOCIO.md`.
- **Dobra, cadernos e imposição:** fólio, quarto, oitavo; o sentido da
  fibra em cada um. Base pronta no que se aprendeu no Devocionário
  (abaixo).
- **História breve da encadernação**, para contextualizar os capítulos
  técnicos (Prideaux).
- **Bibliografia**, da Fase 0.
- Atualizar a tabela de perguntas frequentes do `MANUAL.md`.

## Já aprendido — incorporar ao manual

Do Devocionário (out/2026), com medidas reais (ver `../TESTES.md`):

- **A4 de resma vem com fibra paralela ao lado de 297** (Pólen Bold e
  Opalina, testados com tiras molhadas) → **errada** para a dobra A4→A5.
  O Eco Millennium (reciclado) mostrou fibra pouco orientada.
- **Quarto A6** (duas dobras) resolve: a lombada corre com a fibra. A
  cabeça é aberta depois da costura; pé e goteira dispensam refile.
  Ferramenta: `../quarto.py`, que deriva a imposição simulando as dobras.
- **Espessuras medidas:** Opalina 120 = 0,14 mm/folha (igual ao Pólen
  Bold 90); Opalina 180 = 0,19 mm/folha → boa para guarda.
- **Pólen Bold 90 deixa ver o verso** quando há texto dos dois lados.
- **Guarda A6 de A4 de fibra longa:** cortar a A4 ao meio no lado de 297 e
  dobrar cada metade no lado de 210 → fibra correta.

## Experimento: qual modelo

Pela regra da casa (testar os dois), rodar **o mesmo capítulo** (sugestão:
o 3) com Opus e com Fable, com o mesmo esforço e o mesmo prompt. Comparar:
erros encontrados e confirmados na fonte, falsos alarmes, qualidade das
traduções, respeito ao formato. Registrar em `../TESTES.md`. Uma sessão
nova por capítulo mantém o contexto limpo.

## Registro de progresso

| capítulo | data | modelo | confirmadas | corrigidas | sem fonte | trechos | notas |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
