#import "helpers.typ": *

// Novena to the Sacred Heart — Italian | Portuguese.
// Italian checked 2026-10-11 against the printed card of Editrice Shalom
// (code 27100, imagens/27100_retro.webp) and devotidipadrepio.it. Where
// sources differ, the card wins: "picchiate / picchio" (not "bussate"),
// "non avere", "accordaci". Kept "padre putativo" for St Joseph — the
// card's "padre davidico" is the odd one out among the sources.
// In Italy the prayer is a "coroncina" (said daily); in Brazil it is
// known as a novena. Each page uses its own country's name.
// There is no Latin original: the text was born in French (attributed by
// tradition to St Margaret Mary Alacoque) and Padre Pio prayed it in
// Italian, so the left page is Italian here. Portuguese by the editor,
// translated from the Italian.
//
// PERSONALISED: "appoggiata" / "apoiada" are in the feminine, for the
// person who will pray it. The common printed text has "appoggiato".

#let ripresa-it = rubric[Padre nostro, Ave Maria, Gloria al Padre. \ Sacro Cuore di Gesù, confido e spero in te.]
#let ripresa-pt = rubric[Pai-Nosso, Ave-Maria, Glória. \ Sagrado Coração de Jesus, eu confio e espero em vós.]

#let pet(n, body, rip) = block(below: 1.2em, width: 100%)[
  #par(hanging-indent: 6mm)[#box(width: 6mm, red(roman(n) + "."))#body]
  #v(0.25em)
  #pad(left: 6mm, rip)
]

#spread((
  (pet(1)[O mio Gesù, che hai detto: «In verità vi dico, chiedete e otterrete, cercate e troverete, picchiate e vi sarà aperto», ecco che io picchio, io cerco, io chiedo la grazia… #rubric[(si chiede la grazia)]][#ripresa-it],
   pet(1)[Ó meu Jesus, que dissestes: «Em verdade vos digo: pedi e obtereis, buscai e achareis, batei e abrir-se-vos-á», eis que eu bato, eu busco, eu peço a graça… #rubric[(pede-se a graça)]][#ripresa-pt]),

  (pet(2)[O mio Gesù, che hai detto: «In verità vi dico, qualunque cosa chiederete al Padre mio nel mio nome, Egli ve la concederà», ecco che al Padre tuo, nel tuo nome, io chiedo la grazia…][#ripresa-it],
   pet(2)[Ó meu Jesus, que dissestes: «Em verdade vos digo: tudo o que pedirdes a meu Pai em meu nome, ele vo-lo concederá», eis que ao vosso Pai, em vosso nome, eu peço a graça…][#ripresa-pt]),

  (pet(3)[O mio Gesù, che hai detto: «In verità vi dico, passeranno il cielo e la terra, ma le mie parole mai», ecco che, appoggiata all'infallibilità delle tue sante parole, io chiedo la grazia…][#ripresa-it],
   pet(3)[Ó meu Jesus, que dissestes: «Em verdade vos digo: passarão o céu e a terra, mas as minhas palavras jamais», eis que, apoiada na infalibilidade das vossas santas palavras, eu peço a graça…][#ripresa-pt]),

  ([#sep
    O Sacro Cuore di Gesù, cui è impossibile non avere compassione degli infelici, abbi pietà di noi miseri peccatori e accordaci le grazie che ti domandiamo per mezzo dell'Immacolato Cuore di Maria, tua e nostra tenera Madre.

    San Giuseppe, padre putativo del Sacro Cuore di Gesù, prega per noi.

    #v(0.3em)
    #rubric[Salve, o Regina.]],
   [#sep
    Ó Sagrado Coração de Jesus, a quem é impossível não ter compaixão dos infelizes, tende piedade de nós, miseráveis pecadores, e concedei-nos as graças que vos pedimos por meio do Imaculado Coração de Maria, vossa e nossa terna Mãe.

    São José, pai adotivo do Sagrado Coração de Jesus, rogai por nós.

    #v(0.3em)
    #rubric[Salve-Rainha.]]),
), toc: ((1, [Novena ao Sagrado Coração]),), head: (
  [#label[Coroncina]
   #ptitle([Coroncina al Sacro Cuore di Gesù], sub: [di san Pio da Pietrelcina])
   #align(center, rubric[La recitava ogni giorno per quanti \ si raccomandavano alle sue preghiere.])
   #v(0.8em)],
  [#label[Novena]
   #ptitle([Novena ao Sagrado Coração de Jesus], sub: [de São Pio de Pietrelcina])
   #align(center, rubric[Ele a rezava todos os dias por quem \ se recomendava às suas orações.])
   #v(0.8em)],
), cont: (label[Coroncina], label[Novena]), foot: (psfoot, psfoot))
