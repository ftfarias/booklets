# Dipolo + Raphael Ballet — material de referência

Coletado em 17/09/2026 de `dipolo.ai` (EN e `/pt-br`) e
`raphaelballet.com/pt/`. Páginas arquivadas em `site/`, marca em `logo/`.

## A empresa

**Dipolo** — "O estúdio de IA aplicada para o mundo real."
Consultoria/estúdio de IA aplicada: transforma estratégia de IA em
sistemas que rodam na operação do dia a dia. Fundada por Raphael, 2026.

Vocabulário da casa — útil para a composição, porque é a voz dele:

- "Menos demos. Mais resultados."
- "Todo mundo merece um lugar na fronteira da IA."
- "Feito é melhor que perfeito."
- "Pragmático by design."
- "Uma prova de conceito que nunca sai do papel não conta."
- "Writing is how I think out loud." (assinatura do site pessoal)

Os quatro níveis de valor, da base para cima: **01** dados em que você
confia · **02** enxergar o negócio com clareza · **03** IA em produção ·
**04** empresa AI-native. E o método em quatro passos: visão de IA,
design pragmático, entregar, medir e evoluir.

A numeração `01–04` em duas casas é um maneirismo consistente do site.
**Vale ecoar na tipografia do miolo** — numerar seções assim amarra o
livro à identidade sem precisar de ornamento.

## A pessoa

Raphael Ballet. Mestrado no **ITA**. Uma década em ML e dados em
produção: time inicial da **Pipo Saúde**, depois **Loggi**, **Elo7**, e
então **Meta** (Instagram) e **Expedia Group** (Tech Lead), com sistemas
de recomendação servindo milhões de usuários.

O fio que puxou a Dipolo, nas palavras dele: a maioria dos projetos de IA
nunca chega em produção; o modelo funciona, os números offline são ótimos,
sobe pra produção e nada acontece. **"Quase nunca é o modelo. São os
dados, os sistemas ao redor e a forma como os times estão organizados."**

Escreve pra pensar — posts que começam como notas enquanto depura algo ou
constrói a empresa. Temas: ML aplicado, sistemas de IA, startups,
empreendedorismo. E **Gaia**, a cachorra dele, que saiu na BBC como
"cachorra genial". Faz advisory e mentoria.

**Isso importa para o presente:** um livro de anotações não é um objeto
genérico para ele. Ele já tem prática de escrever à mão para pensar — o
caderno entra num hábito que existe, não inaugura um.

## A marca

`logo/dipolo-logo.svg` — extraído inline do header (`viewBox 107 221 810 582`),
com `fill="currentColor"`. `dipolo-logo-solid.svg` é a mesma coisa em preto,
que é a que vai para o Silhouette. `dipolo-favicon.svg` traz a versão em
quadrado arredondado, verde com o mark em branco.

Duas formas em espelho, inclinadas, cada uma com um vazado interno — dois
polos que se aproximam sem se tocar (daí "dipolo"). Geometria pura, sem
serifa, sem gradiente, sem texto. Aresta reta e canto arredondado.

**Isso cai como uma luva no Legrain/Adler da linha premium** — assimetria
contida, ouro sobre superfície lisa, forma que significa. Não precisa de
nada em volta.

### Recorte em vinil — medido, não estimado

Rasterizado a 600 dpi, larguras reais de traço (percentil 10, conforme
`Vulgata/cover/check_vinyl.py`):

| largura do mark | p10 horizontal | p10 vertical |
|---|---|---|
| 40 mm | 4,11 mm | 4,91 mm |
| 50 mm | 5,12 mm | 6,18 mm |
| 60 mm | 6,18 mm | 7,41 mm |

Piso da casa é 1,2 mm. Mesmo a 40 mm o mark está **3,4× acima** — sobra
folgada. Pela proporção, ele ainda passaria do piso por volta de **15 mm**.

Os mínimos absolutos aparecem como 0,04 mm: são as pontas onde as
diagonais afinam até virar bico, mais antialiasing. É exatamente o caso
que o `CLAUDE.md` manda ler pelo p10 e não pelo mínimo. Mas as pontas são
reais e **descascam mal** — na peça final vale conferir se as extremidades
agudas não levantam junto com o refugo. Se levantarem, truncar a ponta em
~1 mm resolve sem mudar a leitura da forma.

Não esquecer de **espelhar** antes de cortar (HTV corta pelo verso).

## Paleta

Tirada do CSS do site (`--forest`, `--sand`, etc.). Os nomes são deles:

| token | hex | onde |
|---|---|---|
| `paper` / `syn-bg` | `#0b1512` | fundo, quase preto esverdeado |
| `forest` | `#17362a` | verde escuro |
| `linen` / `card` | `#14201b` | cartões |
| `sage` | `#2a3d34` | verde acinzentado |
| `moss` | `#52705c` | verde médio |
| `sand` | `#d9c48e` | **dourado/areia — o destaque** |
| `ink` / `pine` | `#e9efe9` | texto, branco esverdeado |
| `clay` | `#b56f4b` | terracota, acento raro |

O site é escuro: fundo `#0b1512`, texto `#e9efe9`, destaque `#d9c48e`.

**A sorte aqui é grande:** verde muito escuro com dourado é *exatamente*
couro escuro com vinil dourado. A paleta da marca já é a paleta da
encadernação — não precisa traduzir nada. Couro verde-escuro (ou
preto-esverdeado) com o mark em dourado é a identidade dele, literal.

O `clay` (`#b56f4b`) é a saída se couro verde não aparecer: um marrom
avermelhado que também está na marca.

## Fontes do site

- **Hanken Grotesk** — texto (grotesca geométrica, sem serifa)
- **Newsreader** — display/serifa
- **Geist Mono** — monoespaçada, usada na numeração

Para a **capa**, a regra da casa continua: geométrica de espessura
uniforme. Hanken Grotesk é grotesca de traço razoavelmente uniforme e é
a fonte dele — vale medir antes de assumir que passa, mas é uma
alternativa legítima à Futura, e mais fiel à marca.

Para o **miolo** o padrão da casa segue Libertinus. Mas **Newsreader é a
serifa do site dele** e é livre (OFL) — merece ser considerada, ou usada
só nos títulos com Libertinus no corpo. A decisão vai no `TESTES.md`.
