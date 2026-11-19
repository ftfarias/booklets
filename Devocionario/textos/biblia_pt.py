"""
Portuguese: António Pereira de Figueiredo (1725–1797), translated from
the Vulgate. Source: "A Santa Biblia ... traduzidos em portuguez segundo a
Vulgata", London, 1828 — archive.org/details/santabibliaconte00pere,
OCR in raw/figueiredo_1828_djvu.txt.

Hand-cleaned from that OCR, passage by passage. What was changed:
  * OCR damage repaired (ç read as p/j/y, ã/õ tildes lost, "he" for "é",
    stray page headers interleaved mid-verse).
  * ORTHOGRAPHY ONLY modernised: huma→uma, Deos→Deus, elle→ele,
    peccado→pecado, sancto→santo, bemdize→bendize, cousas→coisas,
    mai→mãe, interrogative "porque"→"por que", capitals on common nouns
    (Casa, Ceo, Anjo) lowered.
  * Vocabulary and syntax are Figueiredo's and were NOT touched, even where
    archaic ("Espera ao Senhor", "a to oferecer", "Benta és tu", "lume",
    "peladinhos"). Minimal intervention: this is his translation.

Verse numbers follow the Clementine Vulgate (the Latin page), NOT
Figueiredo's: the Vulgate counts the psalm superscription as verse 1 (or
1–2), Figueiredo does not. Where his verse boundaries differ from the
Vulgate's, the Portuguese was re-split to match the Latin — noted inline.
"""

# Psalms: number (Vulgate) -> (superscription, {verse: text})
# Verse keys are Clementine numbers; superscription verses are omitted.
PSALMS = {
22: ("Salmo de David.", {
 1: "O Senhor é quem me conduz: nada me poderá faltar.",
 2: "Ele me pôs num lugar abundante de pastagens. Ele me educou ao pé de uma água que fortifica.",
 3: "Ele converteu a minha alma. Ele me conduz pelas veredas da justiça, para glória do seu nome.",
 4: "Porque, ainda quando eu ande no meio da sombra da morte, eu não temerei mal algum, porque tu estás comigo. A tua vara e o teu báculo foram a minha consolação.",
 5: "Tu preparaste uma mesa diante de mim contra aqueles que me atribulam. Tu ungiste de óleo a minha cabeça. Que admirável é o meu cálice, que tem virtude de embriagar!",
 6: "Assim que a tua misericórdia me seguirá todos os dias da minha vida, para que eu habite por longuíssimo tempo na casa do Senhor.",
}),
26: ("Salmo de David, antes de ser ungido.", {
 1: "O Senhor é a minha luz e a minha salvação: que poderei eu temer? O Senhor é o defensor da minha vida: quem me poderá assustar?",
 2: "Quando os que me querem perder estavam perto de investir comigo, para me comerem as carnes, então esses inimigos que me perseguem, esses mesmos foram enfraquecidos e caíram.",
 3: "Ainda quando, pois, se acampem contra mim os exércitos, não temerá o meu coração; ainda quando se esteja a me darem batalha, não deixarei eu de esperar, ainda no meio do combate.",
 4: "Uma só coisa pedi ao Senhor, e essa unicamente buscarei: e é que eu habite na casa do Senhor por todos os dias da minha vida, para contemplar as delícias do Senhor e considerar o seu templo.",
 # Figueiredo ends v.5 with "ele me elevou sobre a pedra"; the Vulgate
 # opens v.6 with it ("In petra exaltavit me"). Moved to v.6.
 5: "Porque ele me escondeu no seu tabernáculo; ele me protegeu no dia da aflição, metendo-me no secreto do seu tabernáculo.",
 6: "Ele me elevou sobre a pedra; e agora elevou ele a minha cabeça por cima dos meus inimigos. Eu andei ao redor, e eu imolei no seu tabernáculo uma vítima com clamores de júbilo: cantarei, e farei ressoar a melodia dos hinos para glória do Senhor.",
 7: "Ouve, Senhor, a voz com que clamei a ti: tem compaixão de mim, e ouve-me.",
 8: "O meu coração te disse: O meu rosto te buscou: eu buscarei, Senhor, o teu rosto.",
 9: "Não apartes de mim a tua face, e não te retires do teu servo na tua ira. Sê minha ajuda: não me deixes, nem me desprezes, ó Deus, meu Salvador.",
 10: "Porque meu pai e minha mãe me deixaram; mas o Senhor me tomou na sua proteção.",
 11: "Prescreve-me, Senhor, a lei que devo seguir no teu caminho; e digna-te, por causa dos meus inimigos, de me conduzir pela vereda direita.",
 12: "Não me entregues à má vontade dos que me afligem: porque se levantaram contra mim testemunhas iníquas, e a iniquidade mentiu contra si mesma.",
 13: "Eu creio que verei os bens do Senhor na terra dos vivos.",
 14: "Espera ao Senhor, e obra varonilmente: fortifique-se o teu coração, e está firme esperando ao Senhor.",
}),
41: ("Para o fim. Inteligência aos filhos de Coré.", {
 2: "Do modo que o cervo suspira pelas fontes das águas, assim a minha alma suspira por ti, ó Deus.",
 3: "A minha alma está ardendo de sede por Deus, pelo Deus forte e vivo: quando virei eu, e quando aparecerei diante da face de Deus?",
 4: "As minhas lágrimas me serviram de pão de dia e de noite, quando se me diz todos os dias: Onde está o teu Deus?",
 5: "Eu me lembrei destas coisas, e derramei a minha alma dentro de mim mesmo: porque eu passarei ao lugar do tabernáculo admirável, até a casa de Deus, entre cânticos de alegria e de louvor, e entre gritos de júbilo, como os daqueles que estão num banquete.",
 # The Vulgate carries "et Deus meus" over into v.7; Figueiredo closes
 # the sentence in v.6. Left as he has it — splitting "e Deus meu" off
 # would only reproduce a quirk of the Latin verse division.
 6: "Por que estás tu triste, alma minha, e por que me turbas tu? Espera em Deus, porque eu ainda o louvarei, como quem é a salvação do meu rosto, e Deus meu.",
 7: "A minha alma toda se turbou em mim mesmo: por isso eu me lembrarei de ti, da terra do Jordão, de Hermon e do pequeno monte.",
 8: "Um abismo chama outro abismo ao ruído das tempestades e das águas que tu mandas. Todas as tuas águas levantadas como umas serras, e todas as tuas ondas passaram por cima de mim.",
 9: "De dia enviou o Senhor a sua misericórdia; e à noite é o meu cântico em ação de graças por ela. Eis aqui a oração que eu oferecerei no meu interior ao Deus da minha vida.",
 10: "Eu lhe direi: Tu és o meu defensor. Por que te esqueceste tu de mim? Por que ando eu oprimido de tristeza, enquanto o meu inimigo me aflige?",
 11: "Ao tempo que os meus ossos se quebram, me improperam os meus inimigos que me perseguem, dizendo-me todos os dias: Onde está o teu Deus?",
 12: "Por que estás tu triste, alma minha, e por que me turbas tu? Espera no Senhor, porque eu ainda o louvarei, como quem é a salvação do meu rosto, e Deus meu.",
}),
50: ("Para o fim. Salmo de David, quando o profeta Natã veio ter com ele, por ter pecado com Betsabé.", {
 3: "Tem compaixão de mim, ó Deus, segundo a tua grande misericórdia; e apaga a minha iniquidade, segundo a multidão das tuas comiserações.",
 4: "Lava-me cada vez mais da minha iniquidade, e purifica-me do meu pecado.",
 5: "Porque eu conheço a minha iniquidade, e tenho sempre o meu pecado diante dos olhos.",
 6: "Eu pequei contra ti só, e fiz o mal na tua presença; para que tu sejas reconhecido justo nas tuas palavras, e saias vitorioso nos juízos que se farão de ti.",
 7: "Porque tu vês que eu fui gerado na iniquidade, e que minha mãe me concebeu no pecado.",
 8: "Porque tu amaste a verdade: tu me descobriste os segredos e os mistérios da tua sabedoria.",
 9: "Tu me borrifarás com o hissopo, e eu serei purificado; tu me lavarás, e eu me tornarei mais alvo do que a neve.",
 10: "Tu me farás ouvir uma palavra de consolação e de alegria; e os meus ossos humilhados saltarão de gosto.",
 11: "Aparta a tua face dos meus pecados, e apaga todas as minhas iniquidades.",
 12: "Cria em mim, ó Deus, um coração puro; e restabelece de novo um espírito reto nas minhas entranhas.",
 13: "Não me lances de diante da tua face, e não retires de mim o teu Santo Espírito.",
 14: "Restitui-me a alegria da tua saudável assistência, e fortifica-me com um espírito principal.",
 15: "Eu ensinarei aos iníquos os teus caminhos, e os ímpios se converterão a ti.",
 16: "Livra-me dos sangues, ó Deus, ó Deus da minha salvação; e a minha língua engrandecerá a tua justiça em cânticos de júbilo.",
 17: "Senhor, tu abrirás os meus lábios, e a minha boca anunciará os teus louvores.",
 18: "Porque, se tu tiveras desejado um sacrifício, eu não teria faltado a to oferecer; mas tu não terás por agradáveis os holocaustos.",
 19: "O sacrifício digno de se oferecer a Deus é um espírito traspassado de dor: tu, ó Deus, não desprezarás a um coração contrito e humilhado.",
 20: "Senhor, trata benignamente a Sião, e faze-a sentir os efeitos da tua bondade, para que se edifiquem os muros de Jerusalém.",
 21: "Então é que tu receberás com agrado o sacrifício de justiça, as oblações e os holocaustos; então é que se te oferecerão os novilhos sobre o teu altar.",
}),
83: ("Para o fim, pelos lagares. Salmo aos filhos de Coré.", {
 2: "Senhor dos exércitos, quanto são para amar os teus tabernáculos!",
 3: "A minha alma deseja ardentemente estar na casa do Senhor, e quase que desfalece com o ardor deste desejo. O meu coração e a minha carne saltam de júbilo pelo amor que têm ao Deus vivo.",
 4: "Porque o pardal achou para si uma casa a que se retire, e a rola um ninho onde ponha os seus peladinhos. Assim desejo eu por lugar do meu retiro e do meu descanso os teus altares, ó Senhor dos exércitos, meu Rei e meu Deus.",
 5: "Bem-aventurados os que habitam na tua casa, Senhor: eles te louvarão por séculos de séculos.",
 # Figueiredo divides 6–8 differently (his 5 | 6 | 7). Re-split at the
 # Vulgate's boundaries: "ascensiones in corde suo disposuit, | in valle
 # lacrimarum, in loco quem posuit. | Etenim benedictionem dabit..."
 6: "Bem-aventurado o homem que de ti espera o seu socorro, e que neste vale de lágrimas assentou no seu coração subir e elevar-se sempre,",
 7: "até chegar ao lugar que o Senhor lhe constituiu.",
 8: "Porque o divino Legislador lhe dará a sua bênção; e eles se adiantarão, passando de uma virtude a outra virtude, e enfim verão o Deus dos deuses em Sião.",
 9: "Senhor Deus dos exércitos, ouve a minha oração: põe atentas a ela as tuas orelhas, ó Deus de Jacó.",
 10: "Olha para nós, ó Deus, que és o nosso protetor; e lança os teus olhos sobre o rosto do teu ungido.",
 11: "Porque um só dia que seja nos teus tabernáculos vale mais do que outros mil. Por isso eu escolhi ser antes o último na casa do meu Deus, do que habitar nos tabernáculos dos pecadores.",
 12: "Porque Deus ama a misericórdia e a verdade: e o Senhor dará a graça e a glória;",
 13: "e não privará dos bens aqueles que caminham na inocência. Senhor Deus dos exércitos, bem-aventurado o homem que espera em ti.",
}),
90: ("Louvor de cântico de David.", {
 1: "Aquele que permanece debaixo da assistência do Altíssimo descansará seguro debaixo da proteção do Deus do céu.",
 2: "Ele dirá ao Senhor: Tu és o meu defensor e o meu refúgio: ele é o meu Deus, e eu esperarei nele.",
 3: "Porque ele mesmo me livrará do laço dos caçadores e da palavra áspera.",
 4: "Ele te meterá como à sombra debaixo das suas espáduas, e tu esperarás estando coberto das suas asas.",
 5: "A sua verdade te cercará como um escudo: tu não temerás nada que suceda de noite;",
 6: "nem da seta que voa de dia; nem dos males que se preparam nas trevas; nem os ataques do demônio do meio-dia.",
 7: "Cairão ao teu lado mil, e à tua direita dez mil; mas a morte não se aproximará a ti.",
 8: "Antes tu contemplarás, e verás com os teus olhos a retribuição que levam os pecadores.",
 9: "Porque tu disseste: Senhor, tu és a minha esperança; e porque escolheste por teu refúgio ao Altíssimo.",
 10: "O mal não chegará a ti, e o flagelo não se aproximará à tua tenda.",
 11: "Porque ele mandou aos seus anjos que te guardassem em todos os teus caminhos.",
 12: "Eles te tomarão nas suas mãos, para que não suceda magoares o teu pé, dando nalguma pedra.",
 13: "Tu andarás por cima do áspide e do basilisco, e pisarás o leão e o dragão.",
 14: "Porque ele esperou em mim, eu o livrarei; eu serei o seu protetor, porque ele conheceu o meu nome.",
 15: "Ele clamará a mim, e eu o ouvirei; eu estou com ele no tempo da tribulação; eu o livrarei, e o cobrirei de glória.",
 16: "Eu lhe darei uma vida dilatada; e eu lhe farei ver a salvação que lhe tenho destinada.",
}),
91: ("Salmo de cântico para o dia de sábado.", {
 2: "É bom louvar ao Senhor, e cantar em honra do teu nome, ó Altíssimo;",
 3: "para anunciar de manhã a tua misericórdia, e à noite a tua verdade,",
 4: "ao som do saltério de dez cordas, com cântico ao som da cítara.",
 5: "Porque tu, Senhor, me encheste de gosto ao ver as tuas criaturas; e eu mostrarei esta minha alegria, louvando as obras das tuas mãos.",
 6: "Que grandiosas são, Senhor, as tuas obras! Que profundos os teus pensamentos!",
 7: "O homem insensato não as poderá conhecer, e o louco não terá delas inteligência alguma.",
 8: "Quando os pecadores tiverem nascido como a erva, e quando todos os que obram a iniquidade tiverem aparecido, eles perecerão para todos os séculos;",
 9: "mas tu, Senhor, eternamente és o Altíssimo.",
 10: "Porque eis aí, Senhor, que os teus inimigos perecerão; e todos os que obram a iniquidade serão dissipados.",
 11: "E a minha força se exaltará como a ponta do unicórnio; e a minha velhice se remoçará pela tua abundante misericórdia.",
 12: "E o meu olho olhou com desprezo para os meus inimigos; e a minha orelha ouvirá falar do castigo dos maus que se levantam contra mim.",
 13: "O justo florescerá como a palmeira, e se multiplicará como o cedro do Líbano.",
 14: "Os que estão plantados na casa do Senhor florescerão à entrada da casa do nosso Deus.",
 15: "Eles se multiplicarão de novo numa velhice cumulada de bens; e serão cheios de vigor e de paciência,",
 16: "para anunciarem que o Senhor nosso Deus é reto, e que nele não há injustiça.",
}),
102: ("Do mesmo David.", {
 1: "Alma minha, bendize ao Senhor; e tudo o que há dentro de mim bendiga ao seu santo nome.",
 2: "Alma minha, bendize ao Senhor; e não te esqueças jamais de algum dos seus benefícios.",
 3: "Pois que ele é o que te perdoa todas as tuas iniquidades, e o que sara todas as tuas enfermidades;",
 4: "ele o que resgata a tua vida da morte, o que te cerca da sua misericórdia e das suas graças;",
 5: "ele o que satisfaz os teus desejos, enchendo-te dos seus bens; e o que renova a tua mocidade, como a da águia.",
 6: "O Senhor faz sentir os efeitos da sua misericórdia, e faz justiça a todos os que padecem qualquer injúria.",
 7: "Ele deu a conhecer os seus caminhos a Moisés, e as suas vontades aos filhos de Israel.",
 8: "O Senhor é misericordioso e cheio de ternura; é paciente, e todo cheio de misericórdia.",
 9: "Ele não há de estar sempre irado, nem há de usar eternamente de ameaças.",
 10: "Ele não nos tratou como mereciam os nossos pecados, nem nos castigou segundo a grandeza das nossas iniquidades.",
 11: "Porque quanto o céu está elevado acima da terra, tanto corroborou ele a sua misericórdia sobre os que o temem.",
 12: "E quanto o oriente dista do ocidente, tanto afastou ele longe de nós as nossas iniquidades.",
 13: "Como um pai se compadece ternamente de seus filhos, assim o Senhor é todo compassivo para os que o temem.",
 14: "Porque ele conhece a fragilidade da nossa origem, e ele se lembra que não somos senão pó.",
 15: "O dia do homem passa como a erva: o seu florescer é como o da flor do campo.",
 16: "Assopra o vento, e ela se seca; e não ficou mais vestígio dela no mesmo lugar em que tinha nascido.",
 17: "Porém a misericórdia do Senhor é desde a eternidade, e ela durará eternamente sobre os que o temem. E a sua justiça sobre os filhos dos filhos,",
 18: "sobre os que guardam o seu pacto, e que se lembram dos seus preceitos para os cumprirem.",
 19: "O Senhor preparou no céu o seu trono, e todas as coisas serão sujeitas ao seu império.",
 20: "Bendizei ao Senhor, vós todos os que sois seus anjos; que tendes tanta força e tanto poder, que fazeis o que ele vos manda, para obedecerdes à voz dos seus preceitos.",
 21: "Bendizei ao Senhor, vós todos os que compondes os seus exércitos; que sois os seus ministros; que executais as suas vontades.",
 22: "Bendizei ao Senhor, todas as que sois obras suas, em todo o lugar da sua dominação; e tu, alma minha, bendize também ao Senhor.",
}),
120: ("Cântico dos degraus.", {
 1: "Eu levantei os meus olhos aos montes, donde me há de vir o socorro.",
 2: "O meu socorro não deve vir senão do Senhor, que fez o céu e a terra.",
 3: "Ele não permita que o teu pé seja abalado, nem que dormite o que te guarda.",
 4: "Seguramente o que guarda a Israel não dormitará, nem dormirá.",
 5: "O Senhor te guarda: o Senhor está à tua mão direita para te proteger.",
 6: "Não te queimará de dia o sol, nem de noite a lua.",
 7: "O Senhor te guarda de todo o mal: o Senhor guarde a tua alma.",
 8: "O Senhor proteja a tua entrada e a tua saída, desde agora e para sempre.",
}),
129: ("Cântico dos degraus.", {
 1: "Eu, do profundo abismo em que me achava, clamei a ti, Senhor:",
 2: "Ouve, Senhor, a minha voz. As tuas orelhas se ponham atentas à voz da minha súplica.",
 3: "Se tu observares, Senhor, as nossas iniquidades, quem poderá subsistir, Senhor?",
 4: "Mas tu és cheio de misericórdia; e eu esperei em ti, Senhor, por causa da tua lei. A minha alma esperou na palavra do Senhor;",
 5: "a minha alma esperou no Senhor.",
 6: "Israel espere no Senhor desde a guarda da manhã até a noite.",
 7: "Porque o Senhor é cheio de misericórdia, e nele se acha uma redenção copiosa.",
 8: "E ele mesmo resgatará a Israel de todas as suas iniquidades.",
}),
150: ("Aleluia.", {
 1: "Louvai o Senhor residente no seu santuário; louvai-o assentado no trono incontrastável do seu poder.",
 2: "Louvai-o nos efeitos da sua virtude; louvai-o na sua grandeza, que é infinita.",
 3: "Louvai-o ao som da trombeta; louvai-o com o saltério e com a cítara.",
 4: "Louvai-o com o tambor e com a flauta; louvai-o ao toque da viola e do órgão.",
 # Figueiredo runs v.6 into v.5; split at the Vulgate's boundary.
 5: "Louvai-o com os timbales de um som retumbante; louvai-o com os timbales de um som alegre.",
 6: "Tudo o que tem fôlego louve ao Senhor. Aleluia.",
}),
}

# Pericopes: key -> {verse: text}. Keys are (book, chapter); the verse
# selection is defined by the caller in build.py.
PERICOPES = {
("Luke", 1): {
 28: "Entrando, pois, o anjo onde ela estava, disse-lhe: Deus te salve, cheia de graça: o Senhor é contigo: bendita és tu entre as mulheres.",
 29: "Ela, como o ouviu, turbou-se do seu falar, e discorria pensativa que saudação seria esta.",
 30: "Então o anjo lhe disse: Não temas, Maria, pois achaste graça diante de Deus.",
 31: "Eis conceberás no teu ventre, e parirás um filho, e pôr-lhe-ás o nome de Jesus.",
 38: "Então disse Maria: Eis aqui a escrava do Senhor; faça-se em mim segundo a tua palavra. E o anjo se apartou dela.",
 41: "E aconteceu que, tanto que Isabel ouviu a saudação de Maria, deu o menino saltos no seu ventre; e Isabel ficou cheia do Espírito Santo.",
 42: "E bradou em alta voz, e disse: Benta és tu entre as mulheres, e bento é o fruto do teu ventre.",
 43: "E donde a mim esta dita, que venha visitar-me a que é Mãe de meu Senhor?",
 44: "Porque, assim que chegou a voz da tua saudação aos meus ouvidos, logo o menino deu saltos de prazer no meu ventre.",
 45: "E bem-aventurada tu, que creste, porque se hão de cumprir as coisas que da parte do Senhor te foram ditas.",
 46: "Então disse Maria: A minha alma engrandece ao Senhor,",
 47: "e o meu espírito se alegrou por extremo em Deus, meu Salvador.",
 48: "Por ele ter posto os olhos na baixeza de sua escrava; porque eis aí, de hoje em diante, me chamarão bem-aventurada todas as gerações.",
 49: "Porque me fez grandes coisas o que é Poderoso; e santo o seu nome.",
 50: "E a sua misericórdia se estende de geração a geração sobre os que o temem.",
 51: "Ele manifestou o poder do seu braço; dissipou os que no fundo do seu coração formavam altivos pensamentos.",
 52: "Depôs do trono os poderosos, e elevou os humildes.",
 53: "Encheu de bens os que tinham fome, e despediu vazios os que eram ricos.",
 54: "Tomou debaixo da sua proteção a Israel, seu servo, lembrado da sua misericórdia,",
 55: "assim como o tinha prometido a nossos pais, a Abraão e à sua posteridade para sempre.",
},
("Luke", 2): {
 6: "E, estando ali, aconteceu completarem-se os dias em que havia de parir.",
 7: "E pariu a seu Filho primogênito, e o enfaixou, e o reclinou numa manjedoura: porque não havia lugar para eles na estalagem.",
 28: "Então o tomou em seus braços Simeão, e louvou a Deus, e disse:",
 29: "Agora é, Senhor, que tu despedes ao teu servo em paz, segundo a tua palavra;",
 30: "porque já os meus olhos viram o Salvador que tu nos deste,",
 31: "o qual aparelhaste ante a face de todos os povos,",
 32: "como lume para ser revelado aos gentios, e para glória do teu povo de Israel.",
 46: "E aconteceu que, três dias depois, o acharam no templo, assentado no meio dos doutores, ouvindo-os e fazendo-lhes perguntas.",
 47: "E todos os que o ouviam estavam pasmados da sua inteligência e das suas respostas.",
 48: "E quando o viram se admiraram. E sua Mãe lhe disse: Filho, por que usaste assim conosco? Sabe que teu pai e eu te andávamos buscando cheios de aflição.",
 49: "E ele lhes respondeu: Para que me buscáveis? Não sabíeis que importa ocupar-me nas coisas que são do serviço de meu Pai?",
},
("Matthew", 3): {
 16: "E, depois que Jesus foi batizado, saiu logo para fora da água; e eis que se lhe abriram os céus, e viu o Espírito de Deus, que descia como pomba, e que vinha sobre ele.",
 17: "E eis uma voz dos céus, que dizia: Este é meu Filho amado, no qual tenho posto toda a minha complacência.",
},
("John", 2): {
 3: "E, faltando o vinho, a Mãe de Jesus lhe disse: Eles não têm vinho.",
 4: "E Jesus lhe respondeu: Mulher, que me vai a mim e a ti nisso? Ainda não é chegada a minha hora.",
 5: "Disse a Mãe de Jesus aos que serviam: Fazei tudo o que ele vos disser.",
},
("Mark", 1): {
 14: "Mas, depois que João foi entregue à prisão, veio Jesus para a Galileia, pregando o Evangelho do Reino de Deus,",
 15: "e dizendo: Pois que o tempo está cumprido, e se apropinquou o Reino de Deus: fazei penitência, e crede no Evangelho.",
},
("Matthew", 17): {
 1: "Seis dias depois, toma Jesus consigo a Pedro, e a Tiago, e a João, seu irmão, e os leva à parte a um alto monte.",
 2: "E transfigurou-se diante deles. E o seu rosto ficou refulgente como o sol, e as suas vestiduras se fizeram brancas como a neve.",
 5: "Estando ele ainda falando, eis que uma lúcida nuvem os cobriu. E eis que saiu uma voz da nuvem, que dizia: Este é aquele meu querido Filho, em quem tenho posto toda a minha complacência: ouvi-o.",
},
("Matthew", 26): {
 # OCR reads "Estando delles"; Latin "Coenantibus autem eis" — "eles".
 26: "Estando eles, porém, ceando, tomou Jesus o pão, e o benzeu, e partiu-o, e deu-o a seus discípulos, e disse: Tomai, e comei: este é o meu Corpo.",
 27: "E, tomando o cálice, deu graças, e deu-lho, dizendo: Bebei dele todos.",
 28: "Porque este é o meu Sangue do novo testamento, que será derramado por muitos para remissão de pecados.",
},
("Luke", 22): {
 41: "E Jesus se arrancou deles obra de um tiro de pedra; e, posto de joelhos, orava,",
 42: "dizendo: Pai, se é do teu agrado, transfere de mim este cálice: não se faça, contudo, a minha vontade, senão a tua.",
 43: "Então lhe apareceu um anjo do céu, que o confortava. E, posto em agonia, orava Jesus com maior instância.",
 44: "E veio-lhe um suor, como de gotas de sangue, que corria sobre a terra.",
},
("Mark", 15): {
 15: "Então Pilatos, querendo satisfazer ao povo, soltou-lhes Barrabás, e, depois de fazer açoitar a Jesus, o entregou para que o crucificassem.",
},
("Isaiah", 53): {
 5: "Mas ele foi ferido pelas nossas iniquidades, foi quebrantado pelos nossos crimes: o castigo que nos devia trazer a paz caiu sobre ele, e nós fomos sarados pelas suas pisaduras.",
},
("Matthew", 27): {
 28: "E, despindo-o, lhe vestiram um manto carmesim;",
 29: "e, tecendo uma coroa de espinhos, lha puseram sobre a cabeça, e na sua mão direita uma cana. E, ajoelhando diante dele, o escarneciam, dizendo: Deus te salve, Rei dos judeus.",
},
("John", 19): {
 16: "Então, porém, lho entregou para que fosse crucificado. E eles tomaram a Jesus, e o tiraram para fora.",
 17: "E, levando a sua cruz às costas, saiu para aquele lugar que se chama do Calvário, e em hebreu Gólgota.",
 25: "Entretanto estavam em pé junto à cruz de Jesus sua Mãe, e a irmã de sua Mãe, Maria, mulher de Cléofas, e Maria Madalena.",
 26: "Jesus, pois, tendo visto a sua Mãe, e ao discípulo que ele amava, o qual estava presente, disse a sua Mãe: Mulher, eis aí teu filho.",
 27: "Depois disse ao discípulo: Eis aí tua Mãe. E desta hora por diante a tomou o discípulo para sua casa.",
 30: "Jesus, porém, havendo tomado o vinagre, disse: Tudo está cumprido. E, abaixando a cabeça, rendeu o espírito.",
},
("Matthew", 28): {
 5: "Mas o anjo, falando primeiro, disse às mulheres: Vós outras não tenhais medo, porque sei que vindes buscar a Jesus, que foi crucificado.",
 6: "Ele já aqui não está, porque ressuscitou, como tinha dito: vinde, e vede o lugar onde o Senhor estava posto.",
},
("Luke", 24): {
 50: "Depois levou-os fora até Betânia; e, levantando as suas mãos, os abençoou.",
 51: "E aconteceu que, enquanto os abençoava, se ausentou deles, e era elevado ao céu.",
},
("Acts", 2): {
 1: "Quando se completavam os dias de Pentecostes, estavam todos juntos num mesmo lugar.",
 2: "E de repente veio do céu um estrondo, como de vento que assoprava com ímpeto, e encheu toda a casa onde estavam assentados.",
 3: "E lhes apareceram repartidas umas como línguas de fogo, que repousou sobre cada um deles.",
 4: "E foram todos cheios do Espírito Santo, e começaram a falar em várias línguas, conforme o Espírito Santo lhes concedia que falassem.",
},
("Song of Solomon", 2): {
 10: "Eis aí o meu amado, que me diz: Levanta-te, apressa-te, amiga minha, pomba minha, formosa minha, e vem.",
 11: "Porque já passou o inverno, já se foram e cessaram de todo as chuvas.",
 12: "Apareceram as flores na nossa terra, chegou o tempo da poda; ouviu-se na nossa terra a voz da rola.",
},
("Revelation", 12): {
 1: "Apareceu outrossim um grande sinal no céu: uma mulher vestida do sol, que tinha a lua debaixo de seus pés, e uma coroa de doze estrelas sobre a sua cabeça.",
},
}
