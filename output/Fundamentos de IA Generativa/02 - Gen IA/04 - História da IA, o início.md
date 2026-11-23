Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16369)

## Resumo da aula

A ideia de construir entidades artificiais capazes de agir por conta própria é muito mais antiga que a computação digital. Na Antiguidade, especialmente na mitologia grega, já apareciam narrativas sobre seres artificiais criados por humanos ou deuses, com comportamento autônomo e aparência de inteligência. Isso importa porque a IA não nasce apenas como problema técnico: ela nasce como uma pergunta persistente sobre simular capacidades humanas em artefatos.

Entender a origem da IA ajuda a interpretar os conflitos éticos, econômicos e profissionais que reaparecem a cada nova onda tecnológica. A discussão sobre trabalho, autonomia da máquina e limites da simulação não começou com modelos generativos recentes; ela acompanha a área desde suas formulações iniciais. Esse contexto histórico evita tratar a Gen AI como fenômeno isolado e mostra que cada avanço responde a perguntas antigas com ferramentas novas.

Em 1950, Alan Turing desloca o debate para uma formulação decisiva: máquinas podem pensar? A força dessa pergunta está em trocar o foco da automação mecânica pela simulação de processos cognitivos, aproximando computação e inteligência como objetos do mesmo problema. A partir daí, a IA passa a ser pensada menos como mecanismo que executa movimentos e mais como sistema que reproduz aspectos do raciocínio humano.

O teste de Turing é um experimento mental que avalia se uma máquina consegue sustentar uma interação indistinguível da de um humano. Ele não mede consciência nem prova inteligência no sentido filosófico; mede capacidade de imitar comportamento linguístico ou conversacional de forma convincente. Sua importância histórica está em oferecer um critério operacional para discutir inteligência sem depender de uma definição fechada de “pensar”.

A mudança proposta por Turing reorganiza o objetivo técnico da área. Em vez de apenas construir máquinas que executam ações automáticas, o foco passa a ser construir sistemas que simulem processos cognitivos por meio de algoritmos. Essa virada prepara o terreno para abordagens posteriores que tentam representar decisão, aprendizado e adaptação, cada uma com limitações próprias.

A Conferência de Dartmouth, em 1956, marca a consolidação da IA como campo de pesquisa identificável. Nela, nomes como John McCarthy, Marvin Minsky e Herbert Simon ajudam a transformar uma provocação intelectual em agenda científica, com a hipótese de que aspectos da inteligência humana poderiam ser simulados computacionalmente. O evento importa menos pelo tamanho e mais por estabelecer um programa de trabalho que orientou pesquisas nas décadas seguintes.

Retomando a busca por máquinas que não dependessem apenas de regras explícitas, os perceptrons introduzem a ideia de aprender a partir de exemplos. Inspirados de forma simplificada em neurônios biológicos, eles representam uma das primeiras tentativas de construir redes neurais capazes de ajustar seu comportamento com base em dados observados. Esse movimento antecipa a lógica que, muito mais tarde, sustentaria abordagens modernas de aprendizado e geração já referenciadas anteriormente.

Os primeiros modelos neurais esbarraram em restrições severas de hardware, capacidade de processamento e disponibilidade de dados. Isso não era um detalhe operacional, mas um limitador estrutural: sem escala computacional e sem volume suficiente de exemplos, o aprendizado ficava rudimentar e difícil de expandir. A consequência foi que ideias promissoras surgiram cedo, mas não conseguiam amadurecer tecnicamente naquele momento histórico.

Nos anos 1960, ganha força a IA baseada em regras, estruturada em lógicas do tipo “se... então” e frequentemente organizada como árvores de decisão. Essa abordagem funciona bem quando o domínio pode ser explicitado por especialistas, como em diagnósticos ou classificações com critérios claros. O problema é que ela depende de codificação manual do conhecimento, o que limita a adaptação do sistema a situações não previstas.

A tensão central desse período está entre duas estratégias: programar explicitamente o raciocínio ou permitir que a máquina aprenda com exemplos. Sistemas baseados em regras eram mais viáveis com a infraestrutura da época, por isso ganharam notoriedade, mas carregavam o limite de só operar dentro do que havia sido previamente especificado. Já a linha das redes neurais apontava para uma IA menos rígida, porém ainda bloqueada por restrições técnicas que só seriam enfrentadas muito depois.

Esse início da história produz um ciclo clássico de entusiasmo seguido por frustração. A crença de que a inteligência humana seria rapidamente simulada gerou expectativas maiores do que a tecnologia conseguia sustentar, especialmente quando os métodos mais promissores ainda eram imaturos e os métodos mais viáveis eram rígidos demais. Esse descompasso prepara diretamente o cenário do inverno da IA, quando o avanço da área passa a desacelerar.

## Transcrição

00:00

Fala pessoal, vamos dar mais uma volta então e falar um pouquinho sobre a história da IA. Acho super importante para a gente entender de onde vem esse bicho. Como a coisa tá bombando, é normal a gente ver as pessoas achando que a IA chegou agora. Mas se a gente parar para

00:19

com calma a gente vai entender que a IA já tá aqui com a gente faz tempo que esse assunto aparece por aí a ideia de IA ela já tá perto da gente já desde a antiguidade a gente já tem falado de IA há muito tempo, o ser humano sempre quis

00:35

terceiros autômatos ali perto dele. Então a gente tem isso no nosso imaginário há muito, muito, muito tempo. Então quando a gente olha para a antiguidade, eu vou dar uns passos lá para trás para a gente entender de onde vem essa conversa, para depois a gente aprofundar e compreender como isso evoluiu ao longo do tempo. Por que eu acho isso importante? Porque se a gente não sabe de onde veio, por que a gente pensa assim, como é que essas coisas

00:59

se relacionam, fica difícil da gente entender qual vai ser a nossa relação com essa novidade, querendo ou não aqui, ao longo dos próximos anos. Então a gente tem muitas coisas aqui de conflitos éticos, de dificuldade de pensamento de como o ser humano vai lidar com a IA, como as empresas vão lidar, como vai ser o modelo de trabalho e assim por diante. Então, esse monte de coisa vai aparecer. E por que não?

01:25

usar o que os grandes pensadores já realizaram para ajudar a gente a conseguir pacificar alguns assuntos. Então como isso já vem sendo falado há muito tempo, muita coisa já foi discutida, muita filosofia foi feita em cima desse assunto. Então vamos voltar um pouquinho no tempo, pegar nossa máquina do tempo aqui, voltar um pouquinho alguns montões de anos para trás para entender de onde vem essa brincadeira. Então quando a gente olha

01:49

para a antiguidade, lá mesmo, a gente consegue ver que a Iá já é falada, os seres autômatos já são falados desde a antiguidade. Os filósofos, principalmente os gregos, já falavam muito disso. Então, quando a gente olha para a mitologia grega, a gente tinha ali a ideia de humanos ou animais que têm uma habilidade e conseguem ser criados pelo ser humano ou pelos deuses. Então, a mitologia grega falava que os deuses teriam a capacidade de criar

02:18

Robôs, querendo ou não, um jeito mais fácil de resolver, de explicar isso, mas são robôs que conseguiriam ter pensamento e conseguiriam agir de forma automata. Então, quando a gente olha pra isso, a gente consegue ter uma ideia de inteligência artificial. Querendo ou não, a gente consegue chegar nisso.

02:37

Então, quando a gente começa a olhar pra isso, a gente consegue compreender que a coisa vem desde lá de trás. E aí a moderna começa a surgir mesmo, a gente começa a falar ali, mais na metade do século XX, é quando ela começa a aparecer mais no nosso dia a dia, e por isso que ela conseguiu ganhar mais corpo ainda, e com a chegada do chat GPT ficou ainda mais forte, a gente vai chegar nisso. Mas vamos em frente aqui. Então, da onde que veio a ideia mesmo de uma inteligência artificial? Ela começa, na minha opinião aqui,

03:07

quando a gente olha para a literatura, ela aparece em alguns momentos, mas de uma forma mais concisa, mais legal, mais interessante, começa em 1950, quando Alan Turing, um grande monstro da computação, um grande monstro da

03:25

Da computação mesmo, da programação, pensa um pouco sobre inteligência artificial. Então ele começa a colocar algumas coisas no nosso imaginário. Primeiro publica um artigo falando sobre essa ideia de uma inteligência artificial. Então como que o computador e a inteligência começam a se correlacionar. Então ele começa a trazer um pouquinho

03:50

a pergunta de, será que as máquinas podem pensar? Ele era um grande apaixonado pela profissão, querendo ou não, pelo que ele via como computação na época, e isso fez ele pensar muito a respeito. Será que as máquinas podem pensar? Será que o pensamento de uma máquina é muito diferente do pensamento humano? Como que isso funciona? Ele publica esse artigo e começa a gerar

04:12

um certo furdunço aqui na comunidade científica, porque todo mundo começa a pensar um pouco nesse assunto depois dele. Então ele é um cara que começa a trazer isso para o nosso imaginário com mais força. Ele também escreveu o famoso teste de Turing, que a gente já conhece, muitas pessoas conhecem esse teste.

04:31

e que também traz um pouco isso pra gente, que é um experimento mental pra conseguir comprovar se você tá falando com uma máquina ou se você tá falando com um humano, então pra conseguir compreender se você tá sendo enganado por uma máquina ou se essa máquina pode se passar por um ser humano. Então parte daqui o conceito, o princípio da conversa toda.

04:50

E depois disso, a gente começou a criar máquinas mecânicas que conseguem simular os processos cognitivos humanos com alguns algoritmos de computação. Então, quando a gente olha pra isso, esse questionamento foi fundamental lá, porque ele muda um pouco do debate. Ele começa a pensar que em vez de criar máquinas mecânicas, a gente tem que pensar em como criar máquinas pensantes, que conseguem simular o pensamento cognitivo do ser humano.

05:16

E daí com isso a gente começa a mudar um pouco a nossa visão de algoritmos que existiam e como que esses algoritmos vão se relacionar para conseguir chegar nesse ápice que seria o pensamento humano.

05:27

E vamos falar agora de algumas décadas. Vou passar primeiro com vocês entre 1950 e 1960, quando a gente fala dos primeiros modelos, ainda muito rudimentares, mas que começam a tirar o mato alto pra gente poder estar discutindo isso hoje. Em 1956, teve a Conferência de Dartmouth. Essa conferência foi um grupo de cientistas que se reuniu ali

05:50

para discutir um pouco de computação, inteligência artificial e esse tipo de coisa. Então eles pararam para falar um pouco desse assunto. Foi uma conferência nem tão grande assim, mas com grandes nomes. Então não foi muita gente participando, como a gente olha as conferências de hoje, mas foram nomes importantes que começaram a falar sobre a inteligência artificial. Então nessa conferência...

06:10

a gente começa a ter ali nos Estados Unidos alguns pensadores como o John McCarthy, o Minsky, a gente tem o Simon, Herbert Simon também, que sentam para discutir inteligência artificial. E daí quando eles sentam para falar sobre isso, eles chegam a uma conclusão, depois de acho que foram seis dias se não me engano essa conferência, eles começam a

06:33

achar que sim, a gente conseguiria ter computadores simulando a inteligência humana, então depois disso a gente começa a ter experimentos de aprendizado automático, então a gente começa a caminhar para isso, então essa conferência foi legal para dar o start depois das provocações que a gente teve ali com o Turing, o que a gente consegue ter de start realmente para a comunidade acadêmica científica começar a evoluir este assunto, beleza? Beleza, dentro disso

07:01

a gente começa a falar dos primeiros modelos práticos. Então, terminou a conferência, a galera começou a discutir o assunto, vem ali o Frank Roosevelt e começa a puxar os perceptrons. Então, a ideia dele era pensar em alguma similaridade com neurônios biológicos. Olha que legal, um pouco do que a gente fala de rede neural de hoje já começa a sair dali. Então, a primeira ideia é bem rudimentar,

07:26

de um modelo de rede neural surge dessa época, então ali seria um modelo onde a gente começa a ter

07:34

um pouco de algoritmo, mas mais orientado para as redes neurais, para aprender a aprender a partir de exemplos, tá? Então aqui a gente tá falando, ficou até repetido, né? Aprender a aprender. Mas essa rede neural, querendo ou não, ela aprende com exemplos que a gente tem ali. Então a gente já começa a falar um pouquinho disso, e apesar da gente ter muita limitação na época, porque pensa,

07:57

Limitação de dados era um problema, limitação de máquina era um problema, processamento e etc. Era tudo isso um problema. Então, aqui a gente tem um monte de problema, mas a gente já tem uma ideia de começar a fazer a máquina aprender com base em aprendizado, com base em exemplos e não com base em código direto. Então, isso já muda um pouquinho o paradigma. É muito legal esse momento, mas a gente ainda tem um monte de barreira que vai travar a gente de evoluir.

08:24

E depois quando a gente chega ali nos anos 1960, a gente começa a ter algumas IAs baseadas em regras. E essas IAs baseadas em regras levam a gente, na minha opinião, um pouquinho para trás. Porque, querendo ou não, a gente volta para a lógica básica de programação. Então, ali a gente está usando regras de C. Então, a gente vai muito numa árvore de tomada de decisão. Foi o que ficou na nossa mente aqui

08:47

e na área de tecnologia por muito tempo nos acompanhando certo então quando a gente olha para isso a gente começa a colocar alguns problemas específicos como por exemplo definições médicas ou alguns diagnósticos ali usando-se então ou seja querendo ou não lógica básica de programação para a gente conseguir chegar aqui

09:06

em alguma resposta que seja minimamente interessante no ponto de vista de uma máquina pensando e dando uma resposta. Então aqui tem um grande potencial que acontece ali, mas tem a necessidade de cada regra ser incluída e daí isso gera um grande problema para uma máquina pensar

09:25

Nem tudo a gente sabe, certo? A gente vai aprendendo ao longo da vida e pra uma máquina pensar como um ser humano, pra gente ter uma inteligência artificial, ela não pode ser uma inteligência limitada a tudo aquilo que eu codifiquei. Ela precisa conseguir aprender, assim como um ser humano aprende, porque a gente é um ser que cria novas sinapses e assim por diante. Eu não vou entrar nesse núcleo agora, mas é mais ou menos isso.

09:45

Então a gente consegue evoluir aqui até 1960 com dois pontos de vista. Um ponto de vista que já vai pra uma visão de rede neural e o segundo ponto de vista que vai pra uma visão de C então. E querendo ou não, esse cara do C então, na época foi o cara que conseguiu ganhar mais notoriedade porque ele tinha mais espaço pra você codificar, enquanto o outro tinha muita, muita barreira. Barreira como tudo isso que eu te falei, de dados, barreira de tecnologia, de processamento e assim por diante.

10:13

mas esse C então gera um problema que a gente vai ver mais pra frente. Daqui a pouco eu volto pra falar pra vocês sobre um momento importantíssimo que foi a época do... é... do inverno da IA, quando a gente começa a ter a IA um pouco atravancada. Então aqui a gente tem um boom de todo mundo, eeeh, agora vai! Aí teve uma queda do que foi o inverno da IA, a gente já fala disso, da parte ruim da nossa história aqui. Beleza? Até já já.

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **Gen AI** — Inteligência Artificial Generativa
- **ChatGPT** — Chat Generative Pre-trained Transformer
- **C então** — lógica condicional “se... então”

**Resumo**
A aula apresentou a história da Inteligência Artificial como um tema muito anterior à computação digital, destacando que a ideia de entidades artificiais autônomas já aparecia na Antiguidade, especialmente na mitologia grega. O instrutor explicou que esse contexto histórico é importante para evitar tratar a IA como uma novidade isolada e para compreender melhor os impactos éticos, profissionais e econômicos que se repetem a cada nova onda tecnológica.

Em seguida, a aula avançou para 1950, quando Alan Turing formulou a pergunta “máquinas podem pensar?” e publicou um artigo que aproximou computação e inteligência como problema científico. Também foi explicado o Teste de Turing como um experimento mental para verificar se uma máquina consegue se passar por humana em uma interação, sem medir consciência, mas sim a capacidade de imitar comportamento linguístico de forma convincente. Esse marco reorganizou o foco da área: em vez de apenas automatizar ações mecânicas, passou-se a buscar sistemas capazes de simular processos cognitivos.

Depois, a aula abordou a Conferência de Dartmouth, em 1956, como o momento de consolidação da IA como campo de pesquisa, com nomes como John McCarthy, Marvin Minsky e Herbert Simon. A partir daí, foram introduzidos os primeiros modelos práticos, como os perceptrons, inspirados em neurônios biológicos e voltados ao aprendizado por exemplos, uma ideia que antecipava as redes neurais modernas. O instrutor ressaltou, porém, que esses modelos enfrentavam limitações severas de dados, processamento e hardware, o que impediu sua maturação naquele momento.

Por fim, a aula tratou da IA baseada em regras nos anos 1960, estruturada em lógicas do tipo “se... então” e frequentemente organizada como árvores de decisão. Essa abordagem foi útil em domínios com regras bem definidas, como diagnósticos e classificações, mas exigia codificação manual do conhecimento e tinha pouca capacidade de adaptação a situações novas. O fluxo explicado pelo instrutor mostrou a tensão entre programar explicitamente o raciocínio e permitir que a máquina aprendesse com exemplos, preparando o terreno para o surgimento de frustrações e do posterior inverno da IA.

**Pontos de atenção**
- A IA não surgiu com o ChatGPT; ela tem raízes históricas e conceituais muito antigas.
- O Teste de Turing não mede consciência nem prova inteligência “real”; ele avalia se a máquina consegue sustentar uma interação indistinguível da humana.
- O contexto histórico é essencial para entender debates éticos, econômicos e profissionais atuais.
- Os primeiros modelos neurais tinham forte limitação técnica por falta de dados, poder de processamento e hardware adequado.
- Aprender por exemplos foi uma mudança de paradigma importante em relação à programação por regras explícitas.
- Sistemas baseados em regras funcionam bem quando o domínio é claro e previsível, mas são frágeis diante de casos não previstos.
- A necessidade de codificar manualmente cada regra limita a escalabilidade e a capacidade de adaptação da IA.
- Houve entusiasmo excessivo nas primeiras décadas, seguido de frustração quando a tecnologia não acompanhou as expectativas.
- O aprendizado histórico da área ajuda a entender por que surgiram períodos de desaceleração, como o inverno da IA.