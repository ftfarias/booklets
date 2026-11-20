# Manual do Encadernador Novato

*(com mania de saber um monte de detalhe de tudo)*

Compilação temática de 21 conversas de pesquisa sobre encadernação,
condensadas por assunto. O objetivo é simples: **achar a resposta sem ter
que reler conversa por conversa.**

Cada capítulo abre com uma **regra em destaque** (a máxima que resolve a
maior parte dos casos) e uma **tabela de consulta rápida**. Depois vem o
porquê, as receitas, as armadilhas e o kit para começar no Brasil.

> Material de referência, não evangelho. Vem de conversas com LLM
> (Claude Opus, majoritariamente) e pode conter erro. O texto sinaliza
> onde a confiança é menor. **Teste antes de aplicar em peça que importa** —
> na linha do `../CLAUDE.md`: fixe tudo menos uma variável e registre as
> condições.

---

## Capítulos

Organizado na ordem em que o livro nasce — do que é um livro, passo a
passo até o objeto pronto, e depois o livro que já existe.

### I · O que é um livro
| # | Capítulo | |
|---|---|---|
| 1 | [Breve história do livro](capitulos/01-historia-do-livro.md) |  |
| 2 | [Anatomia do livro](capitulos/02-anatomia-do-livro.md) |  |
| 3 | [Tipos de encadernação](capitulos/03-tipos-de-encadernacao.md) | |

### II · O miolo
| # | Capítulo | |
|---|---|---|
| 4 | [Tipografia e editoração](capitulos/04-tipografia-e-editoracao.md) | |
| 5 | [Papel](capitulos/05-papel.md) | |
| 6 | [Impressão do miolo](capitulos/06-impressao.md) | |
| 7 | [Cadernos e imposição](capitulos/07-cadernos-e-imposicao.md) |  |
| 8 | [Costura](capitulos/08-costura.md) | |
| 9 | [Do miolo costurado ao bloco pronto](capitulos/09-do-miolo-ao-bloco.md) |  |

### III · Da costura à capa
| # | Capítulo | |
|---|---|---|
| 10 | [Colas e adesivos](capitulos/10-colas.md) | |
| 11 | [Guardas](capitulos/11-guardas.md) |  |
| 12 | [Montagem da capa](capitulos/12-montagem-da-capa.md) |  |

### IV · Revestimento e acabamento
| # | Capítulo | |
|---|---|---|
| 13 | [Capas em papel e tecido](capitulos/13-capas-em-papel-e-tecido.md) |  |
| 14 | [Capas em couro](capitulos/14-capas-em-couro.md) | |
| 15 | [Douração e cortes](capitulos/15-douracao-e-cortes.md) | |
| 16 | [Foil, latão e impressão na capa](capitulos/16-foil-latao-e-impressao-na-capa.md) |  |
| 17 | [Plotter de corte e técnicas modernas](capitulos/17-plotter-e-tecnicas-modernas.md) |  |
| 18 | [Papéis decorados](capitulos/18-papeis-decorados.md) | |
| 19 | [Caixas, estojos e proteção](capitulos/19-caixas-e-estojos.md) |  |

### V · O livro que já existe
| # | Capítulo | |
|---|---|---|
| 20 | [Reencadernação](capitulos/20-reencadernacao.md) |  |
| 21 | [Restauração e conservação](capitulos/21-restauro-e-conservacao.md) | |

### Apêndices
| | | |
|---|---|---|
| A | [Consulta rápida](apendices/A-tabelas.md) |  |
| B | [Glossário português / inglês](apendices/B-glossario.md) |  |
| C | [Fornecedores no Brasil](apendices/C-fornecedores.md) |  |
| D | [Medidas e folgas](apendices/D-medidas.md) |  |
| E | [Protocolos de teste](apendices/E-testes.md) |  |
| F | [Ordem de operações](apendices/F-ordem-de-operacoes.md) |  |

Apêndices A, D e E são **gerados** dos capítulos por `gera_apendices.py` —
não edite à mão. Ver [`ESTRUTURA.md`](ESTRUTURA.md).

**Fora do manual:** [`NEGOCIO.md`](NEGOCIO.md) (preço, jurídico, ISBN,
marca) e [`../arte-deco/`](../arte-deco/), que virou projeto de livro
próprio.

Fontes brutas em [`raw/`](raw/) — as conversas originais, íntegras, com
[índice próprio](raw/_INDEX.md).

---

## Onde encontrar — perguntas frequentes

**Materiais**

| Pergunta | Onde |
|---|---|
| Que papel uso para o miolo? E para guarda? E para revestir capa? | [5 — consulta rápida](capitulos/05-papel.md) |
| Como sei o sentido da fibra? | [5 — sentido de fibra](capitulos/05-papel.md) |
| Qual a diferença entre couchê, verge, opalina e sulfite? | [5 — os quatro nomes](capitulos/05-papel.md) |
| Holler ou papelão couro? Que espessura? | [5 — papelão de capa](capitulos/05-papel.md) |
| Que linha uso para costurar? Qual bitola? | [8 — consulta rápida](capitulos/08-costura.md) |
| Linha de rami serve? | [8 — rami](capitulos/08-costura.md) |
| Que cordão uso nas nervuras? | [8 — nervuras](capitulos/08-costura.md) |
| Corino serve para treinar? | [14 — corino](capitulos/14-capas-em-couro.md) |
| Para que serve cera microcristalina? Ela alimenta o couro? | [14 — cera](capitulos/14-capas-em-couro.md) |

**Colas**

| Pergunta | Onde |
|---|---|
| Que cola uso em cada etapa? | [10 — consulta rápida](capitulos/10-colas.md) |
| Como faço engrudo? E CMC? E metilcelulose? | [10 — receitas](capitulos/10-colas.md) |
| Qual PVA comprar no Brasil? | [10 — o PVA neutro](capitulos/10-colas.md) |
| Posso usar cola de contato no couro? | [10 — por que não](capitulos/10-colas.md) |
| Como colo uma impressão colorida sem borrar? | [10 — jato de tinta](capitulos/10-colas.md) · [6 — parte IV](capitulos/06-impressao.md) |

**Técnica e estrutura**

| Pergunta | Onde |
|---|---|
| Que tipo de encadernação escolher? | [3 — consulta rápida](capitulos/03-tipos-de-encadernacao.md) |
| O que é lombada oca? E nervura falsa? | [3 — eixo B](capitulos/03-tipos-de-encadernacao.md) · [8 — nervuras](capitulos/08-costura.md) |
| Como controlo o *swell* da lombada? | [8 — swell](capitulos/08-costura.md) |
| Como douro os cortes? | [15 — cortes dourados](capitulos/15-douracao-e-cortes.md) |
| Ouro, latão ou foil? | [15 — o que muda de verdade](capitulos/15-douracao-e-cortes.md) |
| Como faço bolo armênio? | [15 — bolo a partir de caulim](capitulos/15-douracao-e-cortes.md) |
| Como faço filete dourado sem equipamento? | [15 — filetes sem equipamento](capitulos/15-douracao-e-cortes.md) |

**Decoração e projeto**

| Pergunta | Onde |
|---|---|
| O que uso no lugar de marmorizado? | [18 — consulta rápida](capitulos/18-papeis-decorados.md) |
| Como faço cianotipia em papel de guarda? | [18 — cianotipia](capitulos/18-papeis-decorados.md) |
| Como é uma capa Art Déco de verdade? | [projeto à parte](../arte-deco/) |
| Que margens uso? Que corpo? Que entrelinha? | [4 — consulta rápida](capitulos/04-tipografia-e-editoracao.md) |
| Que formato de livro tiro de uma folha A4? | [5 — formatos](capitulos/05-papel.md) |

**Impressão**

| Pergunta | Onde |
|---|---|
| Como tiro um miolo profissional da L4360? | [6 — a L4360 e o miolo](capitulos/06-impressao.md) |
| Que verniz protege impressão colorida? | [16 — capa, caixa e painel impressos](capitulos/16-foil-latao-e-impressao-na-capa.md) |
| Quando vale terceirizar a impressão? | [6 — quando terceirizar](capitulos/06-impressao.md) · [NEGOCIO](NEGOCIO.md) |

**Ofício e negócio**

| Pergunta | Onde |
|---|---|
| Por onde começo na restauração? | [21 — caminho técnico](capitulos/21-restauro-e-conservacao.md) |
| Quanto cobrar? | [NEGOCIO — precificação](NEGOCIO.md) |
| O que comprar primeiro? | [NEGOCIO — prioridades](NEGOCIO.md) |
| Como registro um livro? ISBN? | [NEGOCIO — registrar um livro](NEGOCIO.md) |
| Posso encadernar livro esgotado? | [NEGOCIO — a parte jurídica](NEGOCIO.md) |

---

## As regras que atravessam tudo

Uma de cada capítulo — se você só ler uma coisa deste manual, leia isto:

1. **A fibra corre paralela à lombada.** Em todas as peças: miolo, guarda,
   revestimento e papelão. Errar isso estraga mais livros que qualquer
   escolha de gramatura, cola ou papel.
2. **Corino treina estrutura, não treina couro.** E cera não alimenta couro —
   esse mito já foi aposentado pela conservação.
3. **A linha é o elemento de sacrifício.** Ela deve ceder antes do papel.
   Linha mais forte que o papel é um defeito, não uma virtude.
4. **Cola boa em camada fina.** Quase todo problema de cola é excesso de
   água ou excesso de cola, não escolha errada de produto.
5. **Nome tradicional não é um tipo** — é uma combinação de quatro escolhas
   independentes. Decida os eixos e o nome aparece sozinho.
6. **O sulco é que segura o ouro.** 90% do resultado da douração acontece
   antes de a folha encostar na peça.
7. **Guarda e capa são fundo, não quadro.** O que funciona é padrão de campo,
   sem ponto focal e com paleta limitada.
9. **Escolha a medida de linha primeiro** (60–70 caracteres) e derive dela o
   corpo, a entrelinha e o formato.
10. **Sobre tinta corante, só verniz à base de solvente.** Qualquer coisa
    aquosa dissolve o corante — inclusive verniz "acrílico à base d'água".
11. **Reversibilidade e pH neutro.** Nada que não possa ser desfeito sem
    destruir o objeto.
12. **Preço = hora × valor da hora + material.** Nunca "material × 3".

---

## Sobre este manual

Montado em setembro de 2026 a partir de conversas acumuladas ao longo do ano.
As fontes originais estão em `raw/`, íntegras, caso algum trecho condensado
precise ser conferido no contexto em que foi dito.

Onde as fontes divergiam, o texto sinaliza. Onde a informação é de baixa
confiança (preço, disponibilidade no Brasil, nome comercial de produto), o
texto avisa para confirmar antes de comprar.
