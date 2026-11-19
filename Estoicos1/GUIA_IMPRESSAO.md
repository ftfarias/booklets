# Estoicos — guia de impressão e encadernação

Dois volumes A5, textos 100% em domínio público, montados com Typst e
impressos em casa na Epson L4360 (dúplex automático, virada na **borda curta**).

---

## Os arquivos

| Arquivo | O que é |
|---|---|
| `vol1_epictetus.pdf` | Miolo Vol. I, A5, 144 pp — **leitura na tela** |
| `vol1_epictetus_booklet.pdf` | Vol. I **imposto** para impressão — 36 folhas A4 |
| `vol2_marcus.pdf` | Miolo Vol. II, A5, 132 pp — leitura na tela |
| `vol2_marcus_booklet.pdf` | Vol. II **imposto** — 33 folhas A4 |
| `cover/cover_vol1.pdf` | Capa envolvente Vol. I (contracapa \| lombada \| capa) |
| `cover/cover_vol2.pdf` | Capa envolvente Vol. II |
| `cover/colofon_vol*_verge_A4.pdf` | Colofão no meio-A4, para o bifólio de verge |

> Imprima sempre os arquivos **`_booklet`**. Os miolos "limpos" são só para conferir.

---

## 1. Miolo

**Configuração da impressora — a mesma que funcionou no Platão:**

- Tamanho: **A4**
- Escala: **Tamanho real / 100%** — nunca "ajustar à página"
- **Frente e verso: ATIVADO, borda curta (short-edge)**
- **NÃO** use o modo Livreto/Booklet do Acrobat ou do Preview

**Antes de imprimir tudo:** imprima só as páginas **1–2** (uma folha),
dobre ao meio e confira que as páginas saem na ordem certa e para cima.
Só depois mande o resto.

### Assinaturas

| Volume | Páginas | Assinatura | Resultado |
|---|---|---|---|
| I — Epicteto | 144 | 16 pp | 9 cadernos × 4 folhas, **0 páginas em branco** |
| II — Marco Aurélio | 132 | 12 pp | 11 cadernos × 3 folhas, **0 páginas em branco** |

Cada caderno sai já na ordem certa; é só dobrar cada grupo de folhas ao meio
e empilhar os cadernos na sequência.

---

## 2. Guardas e colofão

Como no Platão: dois bifólios de **papel verge (laid)**, A4 dobrado ao meio
(dobra vertical → duas faces A5).

- **Bifólio da frente:** em branco.
- **Bifólio de trás:** imprima `cover/colofon_volN_verge_A4.pdf`
  — **face única, 100%, no verge.** O colofão está na **metade direita**,
  então, com a lombada à esquerda, ele cai na folha de guarda voltada para
  dentro (legível ao abrir o livro pelo fim). A metade esquerda fica em branco.

⚠️ Confira a direção das **linhas d'água (chain lines)** do verge antes de imprimir.

---

## 3. Encadernação — costura japonesa

Costura japonesa com **quatro furos** (*yotsume toji*), como no volume do Platão.
Diferente do Platão, aqui **não é grampo canoa**: os cadernos vão empilhados e
costurados pela margem, não dobrados um dentro do outro.

Por isso o miolo tem margem interna de **20 mm** — a costura come uns 15 mm.

**Ordem da pilha:**
1. Bifólio de verge (guarda da frente), dobrado
2. Cadernos 1…N na ordem
3. Bifólio de verge com o colofão (guarda de trás), dobrado

---

## 4. Capa

`cover/cover_volN.pdf` sai como uma peça só: **contracapa | lombada | capa**,
já no tamanho certo (151 × 216 mm cada lado + lombada).

A lombada é calculada a partir da gramatura. O padrão é 90 g/m² (0,115 mm/folha):

- Vol. I — 36 folhas → lombada **4,1 mm**
- Vol. II — 33 folhas → lombada **3,8 mm**

Usando outro papel, recompile com a espessura real:

```bash
typst compile --input vol=1 --input cal=0.15 cover/cover.typ cover/cover_vol1.pdf
```

---

## Reconstruir tudo

```bash
make
```

```bash
make check
```

`make check` confere o número de páginas (múltiplo de 4), o tamanho A5, se
sobrou marcação das fontes, se as 51 seções do Enchiridion estão presentes e
se a imposição de borda curta está com o verso girado e com os lados trocados.
