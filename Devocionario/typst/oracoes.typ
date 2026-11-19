#import "helpers.typ": *

// The common prayers, Latin | Portuguese. Hand-set, not generated.
// Latin in the Clementine's ecclesiastical spelling (Jesus, ejus, caeli)
// so the whole book reads alike. Portuguese in the forms prayed in
// Brazil.

#spread((
  (prayer("Signum Crucis")[In nomine Patris, et Filii, et Spiritus Sancti. Amen.],
   prayer("Sinal da Cruz")[Em nome do Pai, e do Filho, e do Espírito Santo. Amém.]),

  (prayer("Symbolum Apostolorum")[Credo in Deum, Patrem omnipotentem, Creatorem caeli et terrae. Et in Jesum Christum, Filium ejus unicum, Dominum nostrum: qui conceptus est de Spiritu Sancto, natus ex Maria Virgine, passus sub Pontio Pilato, crucifixus, mortuus, et sepultus: descendit ad inferos; tertia die resurrexit a mortuis; ascendit ad caelos; sedet ad dexteram Dei Patris omnipotentis: inde venturus est judicare vivos et mortuos. Credo in Spiritum Sanctum, sanctam Ecclesiam catholicam, Sanctorum communionem, remissionem peccatorum, carnis resurrectionem, vitam aeternam. Amen.],
   prayer("Creio · Símbolo dos Apóstolos")[Creio em Deus Pai todo-poderoso, criador do céu e da terra; e em Jesus Cristo, seu único Filho, nosso Senhor; que foi concebido pelo poder do Espírito Santo; nasceu da Virgem Maria; padeceu sob Pôncio Pilatos, foi crucificado, morto e sepultado; desceu à mansão dos mortos; ressuscitou ao terceiro dia; subiu aos céus, está sentado à direita de Deus Pai todo-poderoso, donde há de vir a julgar os vivos e os mortos. Creio no Espírito Santo, na santa Igreja católica, na comunhão dos santos, na remissão dos pecados, na ressurreição da carne, na vida eterna. Amém.]),

  (prayer("Oratio Dominica")[Pater noster, qui es in caelis, sanctificetur nomen tuum. Adveniat regnum tuum. Fiat voluntas tua, sicut in caelo et in terra. Panem nostrum quotidianum da nobis hodie. Et dimitte nobis debita nostra, sicut et nos dimittimus debitoribus nostris. Et ne nos inducas in tentationem. Sed libera nos a malo. Amen.],
   prayer("Pai-Nosso")[Pai nosso, que estais nos céus, santificado seja o vosso nome; venha a nós o vosso reino; seja feita a vossa vontade, assim na terra como no céu. O pão nosso de cada dia nos dai hoje; perdoai-nos as nossas ofensas, assim como nós perdoamos a quem nos tem ofendido; e não nos deixeis cair em tentação, mas livrai-nos do mal. Amém.]),

  (prayer("Salutatio Angelica")[Ave Maria, gratia plena, Dominus tecum; benedicta tu in mulieribus, et benedictus fructus ventris tui, Jesus. Sancta Maria, Mater Dei, ora pro nobis peccatoribus, nunc et in hora mortis nostrae. Amen.],
   prayer("Ave-Maria")[Ave Maria, cheia de graça, o Senhor é convosco; bendita sois vós entre as mulheres, e bendito é o fruto do vosso ventre, Jesus. Santa Maria, Mãe de Deus, rogai por nós, pecadores, agora e na hora de nossa morte. Amém.]),

  (prayer("Doxologia")[Gloria Patri, et Filio, et Spiritui Sancto. Sicut erat in principio, et nunc, et semper, et in saecula saeculorum. Amen.],
   prayer("Glória")[Glória ao Pai, e ao Filho, e ao Espírito Santo. Como era no princípio, agora e sempre, e por todos os séculos dos séculos. Amém.]),

  (prayer("Oratio Fatimensis")[O mi Jesu, dimitte nobis debita nostra, libera nos ab igne inferni, conduc in caelum omnes animas, praesertim illas quae maxime indigent misericordia tua.],
   prayer("Oração de Fátima")[Ó meu Jesus, perdoai-nos, livrai-nos do fogo do inferno; levai as almas todas para o céu e socorrei principalmente as que mais precisarem da vossa misericórdia.]),

  (prayer("Salve Regina")[Salve, Regina, Mater misericordiae; vita, dulcedo et spes nostra, salve. Ad te clamamus, exsules filii Hevae. Ad te suspiramus, gementes et flentes in hac lacrimarum valle. Eia ergo, advocata nostra, illos tuos misericordes oculos ad nos converte. Et Jesum, benedictum fructum ventris tui, nobis post hoc exsilium ostende. O clemens, o pia, o dulcis Virgo Maria.

  #V Ora pro nobis, sancta Dei Genitrix. \
  #R Ut digni efficiamur promissionibus Christi.],
   prayer("Salve-Rainha")[Salve, Rainha, Mãe de misericórdia, vida, doçura e esperança nossa, salve! A vós bradamos, os degredados filhos de Eva; a vós suspiramos, gemendo e chorando neste vale de lágrimas. Eia, pois, advogada nossa, esses vossos olhos misericordiosos a nós volvei; e, depois deste desterro, mostrai-nos Jesus, bendito fruto do vosso ventre, ó clemente, ó piedosa, ó doce sempre Virgem Maria.

  #V Rogai por nós, santa Mãe de Deus. \
  #R Para que sejamos dignos das promessas de Cristo.]),

  (prayer("Sub tuum praesidium")[Sub tuum praesidium confugimus, sancta Dei Genitrix: nostras deprecationes ne despicias in necessitatibus; sed a periculis cunctis libera nos semper, Virgo gloriosa et benedicta.],
   prayer("À vossa proteção")[À vossa proteção recorremos, santa Mãe de Deus; não desprezeis as nossas súplicas em nossas necessidades, mas livrai-nos sempre de todos os perigos, ó Virgem gloriosa e bendita.]),
), toc: ((1, [Orações]),), head: (label[Orationes], label[Orações]), cont: (label[Orationes], label[Orações]))

// ── How the rosary is prayed ──────────────────────────────────────────
// The Latin rubrics are the editor's; plain Latin, in the manner of the
// old manuals.
#spread((
  ([#ptitle[Modus recitandi Rosarium]
    #set par(hanging-indent: 6mm)
    #box(width: 6mm, red[1.]) Signo crucis facto, dicitur _Credo_.

    #box(width: 6mm, red[2.]) _Pater noster_; ter _Ave Maria_, pro fide, spe et caritate; _Gloria Patri_.

    #box(width: 6mm, red[3.]) Pro singulis quinque mysteriis diei: enuntiatur mysterium et legitur textus; dicitur _Pater noster_, decies _Ave Maria_, _Gloria Patri_ et _O mi Jesu_.

    #box(width: 6mm, red[4.]) Rosario absoluto, _Salve Regina_ et oratio _Deus, cujus Unigenitus_.
  ],
   [#ptitle[Como se reza o terço]
    #set par(hanging-indent: 6mm)
    #box(width: 6mm, red[1.]) Faz-se o sinal da cruz e reza-se o _Creio_.

    #box(width: 6mm, red[2.]) Um _Pai-Nosso_; três _Ave-Marias_, pela fé, pela esperança e pela caridade; um _Glória_.

    #box(width: 6mm, red[3.]) Para cada um dos cinco mistérios do dia: anuncia-se o mistério e lê-se o trecho; reza-se um _Pai-Nosso_, dez _Ave-Marias_, o _Glória_ e o _Ó meu Jesus_.

    #box(width: 6mm, red[4.]) Terminado o terço, reza-se a _Salve-Rainha_ e a oração final.
  ]),
  ([#v(1.2em)
    #set par(hanging-indent: 0mm)
    #align(center, rubric[Gaudiosa: feria secunda et sabbato. \ Luminosa: feria quinta. \ Dolorosa: feria tertia et sexta. \ Gloriosa: feria quarta et dominica.])],
   [#v(1.2em)
    #align(center, rubric[Gozosos: segundas-feiras e sábados. \ Luminosos: quintas-feiras. \ Dolorosos: terças e sextas-feiras. \ Gloriosos: quartas-feiras e domingos.])]),
), toc: ((1, [O Terço]), (2, [Como se reza o terço])), head: (label[Rosarium], label[O Terço]))
