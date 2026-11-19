# Cadernos e imposição

> **A regra que resolve quase tudo:** **4 folhas por caderno** é o ponto
> ideal — dobra limpa, *creep* pequeno, costura confortável. Não passe de
> 5. E a fibra do papel corre **paralela à dobra**, sempre.

Entre a impressão e a costura há uma etapa que parece burocrática e não é:
decidir como as páginas se distribuem nas folhas, dobrá-las e conferir a
ordem. Errar aqui só aparece depois de costurado, quando não tem conserto.

---

## Consulta rápida

| Pergunta | Resposta |
|---|---|
| Quantas folhas por caderno? | **4** (= 16 páginas). Até 5 se necessário |
| Total de páginas precisa ser? | Múltiplo de 4; idealmente, do tamanho do caderno |
| Fibra do papel | **Paralela à dobra** (= paralela à lombada) |
| Sangria para o refile | 3–4 mm nas três faces |
| Margem interna extra | +3–4 mm acima de ~250 páginas |
| Qual borda de virada no duplex? | **Curta** (*short-edge*) — teste antes |

### Folhas por caderno

| Folhas A4 | Páginas A5 | Veredito |
|---|---|---|
| 2 | 8 | Seções finas, *creep* mínimo |
| 3 | 12 | Bom; útil para encaixar contagens difíceis |
| **4** | **16** | ✅ **O padrão.** Dobra limpa, costura fácil |
| 5 | 20 | Aceitável; *creep* já perceptível |
| 6+ | 24+ | ❌ Difícil de dobrar, *creep* forte |

---

## O que é um caderno

![Como as dobras sucessivas geram fólio, quarto e oitavo. Cockerell, 1901.](figuras/cockerell-fig2-dobras-folio-quarto-octavo.jpg)

Uma folha dobrada ao meio dá **4 páginas**. Dobrada de novo, 8. De novo,
16. É daí que vêm os nomes de formato — fólio, quarto, oitavo — que o
cap. 4 trata em detalhe.

Na encadernação caseira moderna o processo é mais simples: você imprime
**duas páginas A5 por folha A4**, frente e verso, dobra cada folha ao meio
e **aninha** as folhas umas dentro das outras. Quatro folhas aninhadas = um
caderno de 16 páginas.

> Cockerell observa que, no fólio, o costume é montar o caderno inserindo
> duas ou mais folhas uma dentro da outra — exatamente o que fazemos.

---

## Imposição

**Imposição** é descobrir qual página vai em qual posição de qual folha,
para que tudo apareça na ordem certa depois de dobrado.

Num caderno de 16 páginas, a ordem é esta:

| Folha | Frente (esq., dir.) | Verso (esq., dir.) |
|---|---|---|
| 1 | 16, 1 | 2, 15 |
| 2 | 14, 3 | 4, 13 |
| 3 | 12, 5 | 6, 11 |
| 4 | 10, 7 | 8, 9 |

A lógica: a folha mais externa carrega a primeira e a última página; a mais
interna carrega as duas do meio. Cada folha soma sempre o mesmo —
17, neste caso (16+1, 2+15, 14+3…).

### O `booklet.py`

O estúdio tem a ferramenta pronta, um script em Python:

```bash
python3 booklet.py meulivro.pdf -s 16
```

Ela faz a imposição, compõe duas A5 por folha A4 paisagem, prepara o verso
para duplex de borda curta e junta tudo num PDF só. Este manual é impresso
com ele.

### A borda de virada

O ponto que mais dá errado. A impressora pode virar a folha pela **borda
curta** (topo↔base) ou pela **longa** (esquerda↔direita), e isso muda tudo:

- **Borda curta** — o padrão do `booklet.py`. O verso gira 180° *e*
  espelha esquerda↔direita, então o script compensa girando e trocando as
  duas páginas de lugar.
- **Borda longa** — use `--long-edge`.

> ⚠️ **No Adobe Reader os nomes vêm invertidos** — experiência do
> estúdio. Se sair errado, troque a opção.

**Sempre teste uma folha.** Imprima as páginas 1–2, dobre, e confira se lê
na ordem. Trinta segundos que evitam 100 folhas no lixo.

---

## Creep

![Visto pela cabeça: as folhas têm o mesmo tamanho, mas as de fora gastam mais papel contornando as de dentro — e as internas avançam na goteira. Esquema exagerado.](figuras/desenho-creep.svg)

Quando você aninha folhas dobradas, as internas **avançam** na goteira.
O motivo: as folhas de fora precisam **contornar** as de dentro na dobra, e
gastam nisso mais papel — sobra menos para chegar à goteira. Isso é o
*creep* (ou *push-out*).

**Consequências:**

1. A goteira fica escalonada, não reta.
2. As páginas centrais perdem margem externa quando você refila.
3. Quanto mais folhas no caderno, pior.

**Quanto dá:** cada folha a mais aumenta o raio da dobra em uma espessura
de papel e gasta **π × espessura** a mais na volta — metade para cada
lado, ou seja, cerca de **1,6 × a espessura** em cada goteira. Em Pólen 90
(0,135 mm), são **~0,2 mm por folha**: com 4 folhas, a interna avança
~0,6 mm sobre a externa; com 8, ~1,5 mm, e já come margem visivelmente.

**Como se resolve:** refilando (cap. 9). Por isso a sangria de 3–4 mm no
arquivo — você projeta contando que a borda vai embora.

Se o livro **não** for refilado, o creep fica à mostra. Aí a única saída é
caderno fino: 2 ou 3 folhas.

---

## Escolher o tamanho do caderno

Duas forças puxam em direções opostas:

- **Caderno fino** — menos creep, dobra mais limpa, mas mais cadernos para
  costurar e mais *swell* (mais linha na lombada).
- **Caderno grosso** — menos costura, menos swell, mas creep maior e dobra
  pior.

**4 folhas resolve para quase tudo.** Varie quando:

- **Papel grosso** (acima de ~120 g) → 3 folhas, senão a dobra abre.
- **Papel muito fino** → pode ir a 5.
- **Para encaixar a contagem** → ver abaixo.

### Minimizar páginas em branco

O total precisa fechar em cadernos inteiros, e o que sobra vira página em
branco no fim. Escolha o tamanho que desperdiça menos:

| Documento | Opção | Resultado |
|---|---|---|
| 33 páginas | 3 × 16 | 15 brancas ❌ |
| 33 páginas | **3 × 12** | **3 brancas** ✅ |

Este manual faz a conta sozinho: na montagem, um script escolhe entre
cadernos de 12, 16 e 20 páginas o que deixa menos páginas em branco.

> Páginas em branco no fim não são defeito; todo livro tem algumas. Mas
> 15 numa tiragem são folhas de papel bom desperdiçadas, multiplicadas
> pelo número de exemplares.

---

## Dobrar

### A fibra

**Paralela à dobra.** Dobrar contra a fibra racha, deixa a dobra
felpuda e faz o caderno abrir mal. O cap. 5 ensina a identificar.

Num A4 cortado de folha grande, você escolhe a fibra ao cortar. Num A4 de
resma, a fibra geralmente corre no sentido longo da folha — o que, dobrando
ao meio para A5, dá fibra **perpendicular à dobra**. É o problema estrutural
do papel de escritório, e está tratado no cap. 5.

### O gesto

1. **Alinhe pelos cantos**, não pelas bordas. Papel cortado tem borda
   irregular; o canto é referência melhor.
2. **Segure firme** e vinque primeiro com o dedo, no meio.
3. **Passe o osso** do centro para as pontas, sobre papel siliconado se o
   impresso for recente.
4. **Confira o registro:** frente e verso têm que coincidir. Se o texto do
   verso não bate com o da frente, o problema é da impressão, não da
   dobra — o teste de registro está no cap. 4.

> Cockerell avisa: dobrar exige cuidado, *"or the margins of different
> leaves will be unequal, and the lines of printing not at right angles to
> the back."* Dobra torta não se corrige depois.

### Papel pesado

Acima de ~150 g/m², **vinque antes de dobrar**: passe o osso contra uma
régua, marcando a linha, e só então dobre. Sem isso a fibra racha na face
externa.

---

## Aninhar e conferir a ordem

Depois de dobradas, as folhas de cada caderno são encaixadas umas nas
outras, e os cadernos empilhados na ordem.

**O truque que evita o desastre:** com os cadernos empilhados e alinhados,
**risque uma diagonal a lápis na lombada**, de cima a baixo da pilha.

Se um caderno estiver fora de ordem ou invertido, a diagonal quebra — você
vê na hora. É o equivalente manual da marca de assinatura (*signature
mark*) que a gráfica imprime no pé da primeira página de cada caderno.

Confira **antes de furar**. Depois de costurado, corrigir significa
descosturar.

---

## Armadilhas

| Problema | Causa | Prevenção |
|---|---|---|
| **Verso de cabeça para baixo** | Borda de virada errada | Testar 1 folha antes |
| **Dobra rachada** | Fibra errada, ou papel pesado sem vinco | Fibra paralela; vincar acima de 150 g |
| **Goteira muito escalonada** | Caderno grosso demais | Máx. 5 folhas; refilar |
| **Texto sumindo na lombada** (livro grosso) | Medianiz curta | +3–4 mm na margem interna |
| **Páginas do meio com margem externa estreita** | *Creep* refilado | Sangria de 3–4 mm; caderno mais fino |
| **Caderno fora de ordem** | Não conferiu antes de costurar | Diagonal a lápis na lombada |
| **15 páginas em branco no fim** | Tamanho de caderno mal escolhido | Calcular antes (ver acima) |
| **Frente e verso desalinhados** | Registro da impressão | Ver caps. 4 e 6 |

---

## Fontes

- A documentação do **`booklet.py`**, o script de imposição do estúdio —
  com a tabela de imposição e a recomendação de 4 folhas.
- **Douglas Cockerell**, *Bookbinding, and the Care of Books* (1901) —
  capítulo "Folding".
- **Roberts & Etherington** (1982) — verbetes SECTION, SIGNATURE, FOLIO,
  BOLT.
