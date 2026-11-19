# Capa em vinil termoadesivo dourado sobre couro escuro

Silhouette Cameo + HTV (vinil de transferência a calor) + couro escuro.

## Arquivos

São **duas capas A4 separadas** — frente e verso — cada uma cortada e
aplicada como uma peça independente. Não há envoltória nem lombada: a
costura japonesa deixa o corte exposto, que é como esses livros são de
fato feitos.

| arquivo | o que é |
|---|---|
| `front_vinyl.typ` / `back_vinyl.typ` | fonte da arte, versão de corte |
| `front_vinyl.pdf` / `back_vinyl.pdf` | visualização (como fica **depois** de transferido) |
| `cut_front.svg` / `cut_back.svg` | vetores — **não espelhados** |
| **`cut_front_mirrored.svg`** | **capa: este vai para a máquina** |
| **`cut_back_mirrored.svg`** | **quarta capa: este vai para a máquina** |
| `check_vinyl.py` | mede as espessuras reais e reprova o que não descasca |
| `front_proof_screen.typ` | versão de tela, em Libertinus — só referência de composição, **não use para cortar** |

## O espelhamento

HTV corta-se **pelo verso**, com o filme portador virado para baixo. Sem
espelhar, tudo transfere invertido.

Os arquivos `_mirrored.svg` já vêm espelhados. Se importar a versão sem
sufixo por engano, ligue o *Mirror* no próprio Silhouette Studio — mas não
faça as duas coisas, senão volta ao normal.

Confirmação rápida antes de cortar: na tela, o "Vanitas" deve estar
**ilegível, de trás para frente**. Se está legível, vai sair errado.

## Por que a fonte mudou

O miolo é composto em Libertinus Serif. A capa **não pode** usar a mesma
fonte: as serifas são finas e afiladas, e o contraste entre traço grosso
e fino é alto — exatamente o que arranca junto com o refugo.

A capa usa **Futura**, geométrica, de espessura quase uniforme. Além de
resolver o corte, é contemporânea de Legrain e Adler (anos 1920–30), o
que combina com a referência da encadernação.

## Espessuras medidas

Piso adotado: **1,2 mm**. Abaixo disso o traço levanta junto com o refugo.

| elemento | traço | altura |
|---|---|---|
| Vanitas | 2,2 mm | 15,4 mm |
| EX VULGATA | 1,9 mm | 7,3 mm |
| MMXXVI | 1,5 mm | ~6 mm |
| bandas | 1,2–3,0 mm | — |

Rode `make cover-check` depois de qualquer alteração. Ele rasteriza a
600 dpi e mede a geometria real — a aparência na tela não diz nada sobre
isso: o primeiro rascunho parecia ótimo e tinha traços de 0,5 mm.

## Corte

1. HTV **com o brilho para baixo** no tapete (o filme portador é o lado
   brilhante; corta-se o verso fosco).
2. Lâmina 2–3, força ~10, velocidade 5 — ponto de partida para HTV comum.
   Confirme com a folha de teste do seu material.
3. **Kiss cut**: corta o vinil, não o filme portador. Se o portador
   cortou, baixe a força.
4. Faça um quadradinho de teste antes da peça inteira.

## Descascagem

Comece pelas bordas externas e puxe em ângulo raso, quase rente à mesa —
puxar para cima é o que arranca as letras. Os contra-formas internos
(o meio do **a**, do **e**, e os dois furos do **V** de Vanitas) saem por
último, com a ponta de um estilete.

## Transferência sobre couro — Cricut EasyPress Mini

A Mini tem **três presets fixos**, aproximadamente:

| preset | temperatura |
|---|---|
| baixo | ~130 °C |
| médio | ~155 °C |
| alto | ~205 °C |

**Use sempre o preset baixo.** O ideal para couro seria 110–120 °C, e
mesmo o preset mais baixo já passa disso — não há como acertar essa faixa
na Mini. Por isso compensa-se pela **barreira e pelo tempo**, não pela
temperatura:

- Pano de proteção **grosso**: algodão dobrado ou papel manteiga duplo
  entre a placa e o filme. É isso que baixa a temperatura efetiva na
  superfície do couro.
- Passadas **curtas e repetidas**: 5–8 s, levanta, deixa esfriar, repete.
  Não 15 s contínuos.
- Pressão média e constante. Sem vapor.
- **Descolagem a frio** (*cold peel*): espere esfriar por completo antes
  de puxar o portador.

A placa pequena (~5 × 10 cm) é uma vantagem aqui: dá para trabalhar por
regiões e não aquecer o couro inteiro. As bandas e o bloco de texto estão
em zonas separadas da arte, o que favorece esse método.

**Teste numa sobra de couro antes**, com o preset baixo e a barreira. Se
marcar mesmo assim, o caminho é trocar de adesivo, não insistir na
temperatura. Couro com acabamento sintético ou encerado pode não aderir
de jeito nenhum.

## Cera microcristalina — sim, mas só no fim

Cera microcristalina (Renaissance Wax ou equivalente) é o padrão de
conservação para couro: quimicamente inerte, pH-neutro, não amarela, não
oxida, não fica pegajosa com o tempo e é reversível. Melhor que cera de
abelha ou carnaúba para esse uso.

**Aplique somente DEPOIS da transferência. Nunca antes.**

A cera deixa uma película hidrofóbica. Couro encerado é justamente o caso
em que o adesivo do HTV não gruda — ou gruda mal e solta em algumas
semanas.

Ordem correta:

1. couro limpo e seco
2. transferir o vinil
3. **esperar 24 h**
4. encerar

Aplicada nessa ordem, a cera protege o couro, uniformiza o brilho e sela
discretamente as bordas do vinil, o que reduz o risco de levantar canto
com o uso. Pouca quantidade, pano macio, deixe secar alguns minutos,
lustre com pano limpo. Duas camadas finas são melhores que uma grossa.

**Não esfregue com força sobre o dourado.** A cera não ataca o vinil, mas
fricção forte pode marcar a superfície do HTV. Passe leve sobre a arte e
lustre com mais vigor só no couro em volta.

## Posicionamento

Cada capa é **A4 paisagem (297 × 210 mm)**, do tamanho do bloco.

A margem esquerda das capas também recebe os furos da costura. A arte
foi posicionada com folga para isso:

| face | arte começa a | folga além da costura |
|---|---|---|
| capa | 44 mm da esquerda | 22 mm |
| quarta capa | 40 mm da esquerda | 18 mm |

(A linha de furos fica a 15 mm; a linha e os nós ocupam até uns 22 mm.)

Aplique o vinil **antes** de furar as capas — é mais fácil posicionar
numa folha inteira, e a furação sai depois junto com o bloco.
