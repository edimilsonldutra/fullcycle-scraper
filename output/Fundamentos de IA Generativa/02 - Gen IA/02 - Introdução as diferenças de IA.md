Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16367)

## Resumo da aula

A IA tradicional opera sobre entradas e saídas previamente definidas. Em vez de criar algo novo, ela aprende relações entre variáveis conhecidas para estimar uma resposta provável, o que a torna adequada para previsão e apoio à decisão. Esse paradigma depende de exemplos em que o sistema já sabe o que entrou e qual deveria ser o resultado.

Dados rotulados são registros em que cada exemplo já vem associado à categoria ou ao valor esperado. Isso existe porque o modelo precisa de referência explícita para aprender a mapear input para output sem ambiguidade. Se os rótulos estiverem errados — por exemplo, imagens de cachorro marcadas como humano — o sistema aprenderá a associação errada, porque ele não corrige sozinho a semântica do dado.

Classificação é a tarefa de escolher entre categorias discretas, como sobreviver ou não sobreviver, spam ou legítimo, fraude ou operação normal. Regressão estima um valor contínuo ou quantitativo, como volume de tráfego, demanda futura ou número esperado de pessoas indo à praia. As duas tarefas usam padrões observados no histórico, mas diferem no tipo de saída: classe fechada na classificação, valor numérico na regressão.

No cenário do Titanic, o modelo recebe atributos como idade, classe, posição da cabine e outras características dos passageiros. Como o histórico já informa quem sobreviveu e quem morreu, o treinamento ajusta o algoritmo para associar combinações de atributos a um dos dois resultados possíveis. O ponto central não é “descobrir” o passado, mas usar esse passado rotulado para prever o desfecho de novos casos com estrutura semelhante.

Retomando a lógica de previsão já conhecida, a IA tradicional observa padrões recorrentes e transforma isso em decisão operacional. Em fraude bancária, por exemplo, o sistema aprende o comportamento usual do cliente e sinaliza desvios com um score de risco; em filtros de spam, separa mensagens com base em traços já reconhecidos como suspeitos. O valor prático está em automatizar triagem, priorização e recomendação em grande escala.

A restrição desse paradigma é que ele generaliza sobre o que já foi aprendido, mas não sintetiza uma saída nova no sentido generativo. Ele identifica, classifica, ranqueia ou prevê dentro de um espaço de respostas já delimitado pelo treinamento e pela tarefa. Por isso, recomendação, detecção e reconhecimento funcionam bem nesse modelo, enquanto criação aberta exige outra abordagem.

A IA generativa aprende regularidades internas dos dados e usa essas regularidades para produzir novos exemplos coerentes com o que foi aprendido. A mudança de mentalidade está em sair de “qual rótulo devo atribuir?” para “qual saída posso compor a partir dos padrões observados?”. Isso explica por que a resposta não precisa existir previamente como opção fechada: ela é construída no momento da interação.

Diferentemente da IA tradicional, a IA generativa pode aprender com menor dependência de rotulagem manual exaustiva. Em vez de exigir que cada exemplo venha marcado com a resposta correta em formato rígido, ela explora grandes volumes de dados para captar estrutura, sequência, contexto e relações implícitas. Isso amplia a escala de treinamento e muda o tipo de conhecimento que o modelo consegue internalizar.

Retomando a ideia de saída original já introduzida, o ponto novo aqui é o contraste com a previsão tradicional: a saída não está pré-fixada como uma classe conhecida. Quando o usuário fornece uma instrução, o modelo usa o contexto recebido para determinar o que gerar em texto, imagem, som ou código. O resultado continua condicionado aos padrões aprendidos, mas é composto dinamicamente em vez de selecionado de uma lista de respostas possíveis.

Essa capacidade generativa viabiliza tarefas como escrita automatizada, geração de imagens, produção assistida de código e tradução automática sofisticada. Em tradução em tempo real, o sistema não apenas identifica palavras isoladas, mas recompõe a mensagem de forma coerente no idioma de destino. O mesmo princípio começa a aparecer em wearables e dispositivos embarcados, como óculos inteligentes e smart rings, que usam geração contextual para apoiar interação contínua no dia a dia.

Modelos generativos modernos conseguem manter coerência ao longo de entradas maiores porque processam dependências entre partes distantes do conteúdo. Retomando brevemente o Transformer, já apresentado antes, ele é a base que permite lidar melhor com contexto longo e sustentar continuidade semântica durante a geração. Isso é decisivo em tarefas como diálogo, tradução e produção de texto extenso, nas quais o sentido depende do que veio muito antes.

A analogia mais útil é comparar a IA tradicional a um aluno de múltipla escolha e a IA generativa a um escritor. O primeiro escolhe entre alternativas já dadas; o segundo produz uma nova história a partir do repertório que acumulou. A implicação prática é direta: sistemas tradicionais são fortes quando o espaço de resposta é conhecido, enquanto sistemas generativos se destacam quando a tarefa exige composição, reformulação e criação condicionada ao contexto.

## Transcrição

00:00

Então pessoal, vamos dar mais um passinho para entender um pouco mais como funciona a IA tradicional, para depois a gente aprofundar na IA generativa. Quando a gente fala dos modelos antes desse boom que a gente está falando, e aqui lógico,

00:16

padronizando, lógico que tinha várias faculdades, instituições que já estavam trabalhando muito em cima de modelos não tradicionais, mas quando a gente fala dessa quebra de paradigma, desse momento onde começa a aparecer a IA generativa, o que a gente tinha até então? Era um modelo de IA tradicional que a gente chama, que ela é basicamente uma IA supervisionada e que vai focar na classificação e na regressão com base em dados conhecidos. O que eu quero dizer com isso?

00:44

Bom, vamos lá. Se vocês lerem aqui tá falando o seguinte, o modelo é treinado com exemplos rotulados, inputs e outputs conhecidos. O que isso significa? Significa que eu tô dando dados que aquela modelagem já sabe trabalhar. Então, meu algoritmo que eu criei já sabe trabalhar com aquela modelagem e com base nesses dados que eu tô entregando pra ele, que ele já sabe quais são e ele já sabe qual é a saída esperada, ele vai trazer aqui uma saída mais provável.

01:11

Então eu vou dar um exemplo pra vocês. Inclusive esse exemplo foi o exemplo no qual eu aprendi no meu primeiro curso de A. Vou usar esse pra vocês. Cara, qual que é o grande ponto? Imagina que eu tenho que fazer um teste pra saber se as pessoas que entraram no Titanic vão viver ou não. O que eu tô querendo dizer com isso?

01:29

Imagina que hoje eu sou o cara que pega o ticket das pessoas lá do Titanic, beleza? Então eu sou o cara, vai ter hoje a viagem, o pessoal tá indo lá, o Jack, a Rose, todo mundo tá indo lá pro Titanic e eu sou a pessoa que tá pra receber os bilhetes. Sabendo que o Titanic vai afundar, eu preciso saber quem morreria ou quem não, beleza? Então eu tô tentando prever o que aconteceria.

01:53

Mas eu já tenho os dados, certo? Eu já sei que o Titanic afundou, já sei quem morreu e quem sobreviveu. Beleza? Então, com base nesses dados, eu consigo, agora, prever o que aconteceria. Mas, pô, Natan, você já sabe o que aconteceu? Não, eu sei. Mas imagina que pra testar o modelo, caso aconteça de novo, eu posso usar esses dados pra prever o modelo do Titanic 2. Um exemplo assim, tá? Um exemplo bem tonto.

02:17

Então, imagina o seguinte, vai entrar as pessoas e eu vou pegar o meu algoritmo e vou treinar ele para, por exemplo, incluir na sua matriz ali dados sobre idade. Tem as pessoas com tal idade, as pessoas com tal altura, as pessoas que estavam nas cabines do lado esquerdo, as cabines do lado direito, as cabines do fundo, as cabines da frente, primeira classe, segunda classe. Tudo isso são dados classificados. Então, é mais ou menos o que a gente está falando aqui.

02:47

Dados classificados e rotulados. Inputs conhecidos. Então, estou dando dados conhecidos. Estou pegando dados que eu já conheço e colocando para dentro disso. Depois desse treinamento, eu pego e executo a base de dados para entender qual é a saída possível. O que eu estou querendo saber? Eu já sei. Eu quero prever quem vai viver e quem vai morrer. Basicamente é isso. Então, eu já tenho uma saída proposta, prevista, ou seja, o modelo já sabe que o que ele tem que me entregar no final é quem vai viver e quem vai morrer.

03:15

E eu já tenho os dados conhecidos de entrada. Eu já fui preparando esse algoritmo para receber esses dados. Beleza? Sei que ficou um pouco confuso, então vamos repassar aqui algumas coisas. Imagina que eu quero saber quantas pessoas vão ir para a praia nesse final de semana. Eu vou pegar então com base

03:35

na estrada que a gente tá usando pra ir pra praia, como foi no último final de semana, no último feriado e assim por diante, e com base na probabilidade ou na estatística disso, eu vou tentar dar uma saída de quantas pessoas vão no próximo fim de semana ou no próximo feriado. Então é basicamente uma análise estatística do que a gente já faz quando a gente tá olhando grandes conjuntos de dados, mas aqui com o IA

03:55

trazendo por trás um modelo de recomendação ou de previsão do que vai acontecer. Então, basicamente, em linhas gerais, a gente vai aprofundar mais nisso, mas em linhas gerais pra vocês começarem a entender, é disso que a gente tá falando. Quando a gente tá falando da IA tradicional, ela tem dados de entrada, dados de saída já muito bem definidos. Com base nesses dados, você consegue compreender qual vai ser a previsão futura. Diferente da Gen AI, que vem com uma coisa um pouquinho diferente aqui pra gente. Então,

04:25

Quais são as características principais que a gente acabou de falar aqui? Ela vai ser uma IA baseada em previsão ou decisão.

04:35

com padrões observados. Então, eu estou falando o seguinte, é uma IA que ela está vendo padrões e tentando prever padrões, beleza? Então, ela está prevendo algo ou ajudando a decidir algo com padrões de dados que ela já tinha. Então, ela precisa de dados rotulados e consistentes. Para conseguir fazer isso, ela precisa conseguir saber se, por exemplo, eu vou dar o caso aqui do Titanic, saber separar o que é um

04:57

cachorro do que um ser humano, por exemplo, e daí se eu colocar, por exemplo, cachorros rotulados como seres humanos, ela vai entender que são seres humanos, ela não sabe separar uma coisa da outra. Então, basicamente, aqui a gente está falando de dados categorizados, ou seja, sabendo qual é a categoria de cada dado.

05:15

as tarefas que normalmente utilizavam esse tipo de IA. Detecção a fraude, porque você concorda que quando eu tô falando de fraude, eu tô vendo quais são as ações, por exemplo, que o Natan, como cliente do banco, faz no dia a dia. E com base nessas ações, eu tento prever quais são as ações comuns dele fazer. Quando vem uma ação muito diferente, eu falo, ô, calma aí!

05:38

Isso aqui não está no que eu consegui prever do Natan, inclusive eu consegui dar um score e pensar em como reduzir fraude. Outra coisa também na classificação de e-mails para você saber o que é spam e o que é legítimo. A mesma situação, você consegue ali ter alguns critérios para separar. Eu não sei se você já tinha parado para pensar nisso, mas a sua caixa de e-mail está dotada dessa tecnologia já para fazer essa separação.

06:02

como que ela sabe o que é spam? basicamente analisando que ela já tem como conhecimento de spam reconhecimento de imagem por exemplo quando você chega para uma IA qualquer e pergunta que tipo de bicho é aquele ou até uma música quando você pega e põe um trecho da música e pede para falar qual que é o nome daquela música então aqui você tá

06:22

conseguindo prever ou identificar qual é a coisa que você está procurando, porque de novo os dados de entrada você já tem, você consegue treinar ela para sempre saber que aquele bicho daquele jeito é um gato, é muito mais complicado isso, mas foi possível treinar.

06:39

E previsão de demandas também, que foi o que eu falei. Por exemplo, os marketplaces normalmente usam muito isso. Um marketplace como, por exemplo, uma Amazon da vida, tenta prever o seu comportamento de compra e te indicar o que ela acha que faz sentido pra você com base nas suas compras passadas. Então, esses carinhas estavam muito no dia-a-dia já de grandes organizações. Isso não é novo, gente. Então, vamos lá. Vamos pensar junto. Separar spam.

07:08

propor venda e esse tipo de coisa estão no nosso dia a dia faz tempo, né? E querendo ou não, por trás normalmente a gente está falando de algoritmos de A. Qual é a limitação disso? Tudo que eu falei, vocês viram que eu não falei de criar nada, só de prever, de direcionar, de compreender, mas nunca de criar. Então, eu não estou dando ainda a capacidade de criação. Então, não cria nada novo, só generaliza o que já foi aprendido. Então, essa é a primeira coisa que a gente tem que ter em mente.

07:38

Agora, e na IA generativa? Como é que essa bagaça funciona? Na IA generativa, então, ela é treinada para entender e estruturar os padrões internos dos dados de entrada, e a partir disso, gerar novos exemplos que seguem as mesmas regras implícitas. Ou seja, ela para de só ter dados já adequados para ela, ela já começa a compreender e interpretar os dados de entrada.

08:03

Então, a primeira coisa que muda um pouco é a classificação de dados. Isso já começa a mudar. E o segundo ponto é que ela começa a gerar coisas com base no que ela recebeu. Então, ela não está só mais compreendendo e separando ideias ou até direcionando previsões. Ela já está compreendendo e criando. Aqui começa a aparecer

08:24

a palavra criar. Quais são as características principais? Ela vai ter saídas originais. Ela não vai te falar com clareza aquilo que você previu de entrada. Na verdade, a saída dela vai aprender quando você estiver colocando a entrada. Você entendeu isso?

08:41

Viu que diferente? Por exemplo, quando eu chego por um chat de APT, eu vou colocar pra ele assim, chat de APT, eu preciso disso, disso, disso, disso. Ele não sabia aquilo até então. Quando eu perguntei pra ele, aí ele vai determinar a saída dele. Então ele não tinha como saber isso antes, ele tem que aprender na hora que eu mando pra ele. Então, a saída

08:58

pode ser em texto, imagem, som e assim por diante. A ideia vai ser a mesma, tá bom? Então ela é treinada com muito dado, a outra também era, mas agora com muito dado e sem necessidade de rótulos explícitos no dado. Então muitas vezes você vai dando a informação pra ela e supervisiona

09:16

Ou você pode fazer ela de forma não supervisionada, mas normalmente o que você faz? Você dá os dados e vai por tentativa e erro como uma criança aprende, por exemplo. Você vai colocando e deixando ela rodar e conforme ela vai rodando, você vai reforçando o aprendizado de máquina, falando se o caminho que ela foi positivo ou negativo. Normalmente é isso. E isso cria...

09:39

talvez o que a gente chamaria de sinapses neurais, um jeito de você criar as conexões do caminho que faz mais sentido e do dado que faz mais sentido. Quais as tarefas típicas para esses carinhas aqui? Criação de conteúdo original, então por exemplo, muita gente está usando para criação de vídeo original, agora como eu falei para vocês,

09:58

muita gente utilizando para criação de conteúdo para as redes sociais, muita gente utilizando para, por exemplo, dia-a-dia de trabalho, criação de materiais de apresentação, material de apoio, visão orçamentária, coisa pra caramba. Eu mesmo uso pra caramba no meu dia-a-dia, no meu trabalho basicamente eu só uso IA no dia-a-dia, tá bom?

10:17

Vamos lá, então consegue gerar tanto essa parte aqui textual e etc, como geração de imagens, escrita automatizada, pode gerar código, então também se você tá aí codificando, eu já falei algumas das ferramentas as mais promissoras no momento, Enterprise, ao meu ver é a Manus e o Devin, essas duas estão indo muito bem.

10:39

E também muito boa para tradução automática sofisticada, inclusive a gente já está falando de tradução real-time, inclusive quando você olha os novos, as novas ferramentas vestíveis, né, que a gente pode falar, ou as ferramentas que a gente está colocando, por exemplo, óculos do Google, óculos da Meta,

11:01

o Smart Ring e assim por diante já começam a trazer embarcado esse tipo de coisa para ajudar no dia a dia. Olha a dificuldade que eu tive para traduzir a palavra em inglês para não ficar falando inglês e deixando muito muito chata a aula. Mas vamos lá!

11:17

Aqui a gente está falando o seguinte... A capacidade de lidar com o contexto longo e criar coerência, graças à arquitetura como Transformer. A gente vai falar de Transformer ao longo das nossas aulas, então grave esse nome. A gente já volta, mas Transformer é um nome que a gente vai falar bastante ao longo desse curso, porque é basicamente o segredo do sucesso para que essas IAs generativas funcionem.

11:44

E qual a analogia prática que a gente pode fazer? Eu gosto de fazer uma analogia, porque normalmente a gente fica muito nesse mundo teórico, ou muito no mundo mais complicado de ir a, porque é complicado, inclusive já me perguntaram assim, Natan, me explica o que é de forma simples. Não é simples, se fosse simples...

12:04

Todo mundo conseguia fazer, a gente já tinha isso faz tempo. Então, não é simples. Vamos ser bem honestos? Como que a gente consegue simplificar? Com analogia. Então, eu gosto de fazer algumas analogias. Então, vamos pensar no IA tradicional. Ela é como se fosse um aluno que faz provas de múltipla escolha, escolhe a melhor resposta entre as opções baseadas no que ele já aprendeu. Beleza? Então, ele está fazendo a prova dele de múltipla escolha, pensa naquilo que ele já aprendeu e escolhe a resposta.

12:29

Então ele já sabe a saída, ou seja, quais são as múltiplas escolhas e com base nisso ele vai lá e separa o que ele... cofrega o que ele acha que é o certo. Aí a generativa já é como um escritor que com base na leitura de vários livros escreve uma nova história que não tem nada a ver, que tem começo, meio e fim originais, que não são uma cópia do anterior. Qual é a grande mudança aqui? Pensa o seguinte, se você é um aluno que você é...

12:57

aprendeu um monte de coisa para responder uma prova de múltipla escolha. Então, você já sabe quais são as escolhas, você já sabe o que você aprendeu, então você sabe que você tem aqui um range de caminhos para seguir. Eu aprendi isso, eu vou responder isso aqui, que é o que tem aqui. Agora, quando eu falo ler uma pancada de livro e gerar alguma coisa, você vai ler um monte de livro, você não sabe o que vai sair ainda, depois que você leu, depois que você adquiriu esse conhecimento, aí você fala,

13:23

Sei pra onde ir agora. Vou criar desse jeito. Pensa que no nosso cérebro não é assim que funcionaria. É a mesma coisa pra Gen AI. Então é mais ou menos pra esse lado que a gente tá caminhando.

## Resumo IA

**Abreviações**  
- IA: Inteligência Artificial  
- Gen AI: Inteligência Artificial Generativa  
- APT: ChatGPT  
- Transformer: Arquitetura de rede neural baseada em atenção, usada para modelar dependências em sequências de dados  
- Enterprise: Ambiente corporativo / soluções para empresas  

**Resumo**  
A aula apresentou a diferença entre IA tradicional e IA generativa, começando pelo paradigma clássico da IA supervisionada, que opera com entradas e saídas previamente definidas. Nesse modelo, o sistema é treinado com dados rotulados e conhecidos para aprender relações entre variáveis e então prever uma resposta provável, sendo muito usado em tarefas de classificação e regressão. O instrutor exemplificou esse fluxo com o caso do Titanic, no qual atributos como idade, classe social e posição na cabine servem de entrada para prever um resultado já conhecido no histórico, como sobreviver ou não sobreviver. A ideia central é que a IA tradicional não cria algo novo, mas identifica padrões, classifica, ranqueia e prevê dentro de um espaço de respostas delimitado pelo treinamento.

Em seguida, a aula contrastou esse modelo com a IA generativa, que aprende estruturas internas dos dados e usa essas regularidades para compor saídas novas e coerentes em tempo de execução. Em vez de depender fortemente de rótulos explícitos, esse tipo de IA explora grandes volumes de dados para captar contexto, sequência e relações implícitas, podendo gerar texto, imagem, som e código. O instrutor relacionou essa capacidade a aplicações como escrita automatizada, geração de conteúdo, tradução sofisticada em tempo real, produção assistida de código e uso em dispositivos vestíveis e embarcados. Também destacou que arquiteturas como Transformer são essenciais para manter coerência em contextos longos, permitindo que o modelo preserve sentido ao longo de entradas extensas. A analogia final resumiu a diferença: a IA tradicional se parece com um aluno de múltipla escolha que escolhe entre alternativas já dadas, enquanto a IA generativa se parece com um escritor que produz uma nova história a partir do repertório aprendido.

**Pontos de atenção**  
- Dados rotulados precisam estar corretos e consistentes; rótulos errados levam o modelo a aprender associações incorretas.  
- IA tradicional depende de entradas e saídas previamente definidas; ela prevê, classifica ou decide, mas não cria conteúdo novo.  
- Classificação trabalha com categorias discretas; regressão trabalha com valores contínuos.  
- Em casos como fraude, spam e reconhecimento de imagem, o valor está na triagem, priorização e detecção de desvios com base em padrões históricos.  
- A IA tradicional generaliza apenas dentro do que foi aprendido; não resolve bem tarefas de criação aberta.  
- IA generativa não produz saídas a partir de uma lista fechada de opções; ela compõe a resposta dinamicamente com base no contexto recebido.  
- A qualidade da saída generativa depende fortemente da quantidade e da diversidade de dados, além da forma como o contexto é fornecido.  
- O modelo generativo pode operar com menos rotulagem manual exaustiva, mas ainda exige supervisão e ajuste para reforçar caminhos corretos.  
- A capacidade de lidar com contexto longo e manter coerência é um diferencial importante, associado à arquitetura Transformer.  
- Ferramentas de IA generativa podem ser muito úteis em produtividade, mas devem ser vistas como apoio à criação e à decisão, não como substitutas automáticas da validação humana.