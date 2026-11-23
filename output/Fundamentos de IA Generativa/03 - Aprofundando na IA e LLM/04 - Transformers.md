Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16375)

## Resumo da aula

Transformers surgem como resposta direta às limitações que permaneceram mesmo após LSTM e GRU: dificuldade em capturar dependências longas e baixa capacidade de paralelização. Retomando essas limitações já conhecidas, a mudança decisiva foi abandonar a recorrência como mecanismo central de processamento. O paper Attention Is All You Need consolida essa virada ao propor uma arquitetura baseada em atenção, capaz de tratar relações entre elementos distantes sem depender de uma passagem sequencial token por token.

Attention é o mecanismo que permite atribuir pesos diferentes às partes de uma sequência conforme o contexto. Em vez de tratar todas as palavras com a mesma relevância, o modelo calcula quais tokens mais influenciam a representação de cada token atual. Em self-attention, essa comparação acontece dentro da própria sequência de entrada: cada token observa todos os demais e estima a importância relativa de cada um. Isso permite conectar elementos semanticamente ligados mesmo quando estão longe na ordem do texto.

Na frase “O livro que o João leu ontem era interessante”, a interpretação central depende da ligação entre “João”, “leu” e “livro”, embora existam termos intermediários. O mecanismo de atenção aumenta o peso dessas conexões e reduz a influência relativa de partes menos centrais para aquela relação. O mesmo vale para “O cachorro que o menino viu estava latindo”: mesmo com “menino” mais próximo de “latindo”, o modelo pode dar mais peso a “cachorro” para preservar a interpretação correta. O ganho prático é representar dependências sintáticas e semânticas sem ficar preso à proximidade linear.

A camada de atenção compara cada token com todos os outros tokens da sequência para calcular pesos de influência. Esses pesos passam a compor uma nova representação contextualizada de cada token, isto é, a representação deixa de refletir apenas o token isolado e passa a incorporar o contexto relevante ao redor dele. Esse é o núcleo da arquitetura, porque substitui a memória recorrente por um cálculo explícito de relações. O resultado é uma modelagem mais flexível de contexto, especialmente útil em linguagem natural.

Depois da atenção, cada token passa por camadas densas feedforward, descritas como MLPs. Essas camadas transformam a representação contextualizada de forma não linear, ampliando a capacidade do modelo de aprender padrões complexos além de simples combinações lineares. A atenção decide “com quem” cada token deve se relacionar; a MLP transforma “como” essa informação combinada será refinada internamente. Essa composição entre atenção e transformação densa é parte essencial do poder expressivo dos Transformers.

Como a arquitetura não processa a sequência de forma recorrente, ela precisa receber explicitamente informação de ordem. Positional Encoding adiciona aos embeddings um sinal que indica a posição de cada token na sequência. Isso permite processar tudo em paralelo sem perder a noção de quem veio antes ou depois. Em termos práticos, é como anexar um identificador posicional a cada token para que a ordem continue disponível durante o cálculo.

Retomando o gargalo das RNNs, o Transformer processa todos os tokens simultaneamente em vez de depender de uma cadeia temporal estrita. Essa mudança se alinha muito melhor ao hardware moderno, especialmente GPUs e TPUs, e acelera o treinamento em larga escala. O efeito não é apenas ganho de desempenho bruto: a arquitetura viabiliza experimentação, aumento de escala e ciclos mais rápidos de evolução de modelos. Foi esse encaixe entre arquitetura e infraestrutura que acelerou a IA generativa moderna.

Ao calcular relações diretamente entre tokens distantes, Transformers aprendem dependências de longo prazo com muito mais eficiência do que arquiteturas recorrentes. O modelo não precisa carregar contexto por uma cadeia longa de estados ocultos, o que reduz o impacto dos problemas clássicos de degradação do gradiente já discutidos anteriormente. Isso melhora a preservação de informação relevante ao longo da sequência e sustenta respostas mais coerentes. Em escala, essa propriedade contribui para maior estabilidade do treinamento e melhor qualidade de geração.

Transformers escalam bem para modelos muito grandes porque sua estrutura favorece paralelização e treinamento distribuído. Essa característica permitiu construir sistemas com bilhões de parâmetros mantendo desempenho e capacidade de generalização em tarefas complexas. A escalabilidade não é apenas quantitativa; ela muda qualitativamente o tipo de comportamento que o modelo consegue exibir, especialmente em geração, diálogo e multimodalidade. Por isso, a arquitetura se tornou a base dominante dos LLMs.

BERT, GPT, T5, PaLM e Llama seguem essa linha arquitetural, aplicando Transformers a classificação, análise de sentimentos, geração de texto, tradução e agentes conversacionais. O mesmo princípio se expande para visão computacional com modelos como ViT e para sistemas multimodais capazes de combinar texto, imagem e áudio. Em vez de manter um modelo isolado por modalidade, a arquitetura favorece representações integradas entre diferentes tipos de dado. O impacto também alcança bioinformática, finanças e recomendação, mostrando que atenção não é apenas uma técnica de NLP, mas um padrão geral de modelagem de relações em sequências e estruturas complexas.

## Transcrição

00:01

Fala galera, beleza? Então a gente agora chega no momento que eu mais queria chegar. A gente começa a ter um ponto de ruptura aqui pra gente discutir. Chega a conversa sobre Attention e Transformers. É a melhor parte de toda essa jornada que a gente tá discutindo. É quando a gente começa a quebrar o paradigma, é quando a coisa começa a borbulhar.

00:23

Então quero falar muito sobre esse assunto com vocês desde a hora que a gente começou a nossa conversa e eu queria chegar nesse momento. Tô ansioso. Vamos falar um pouco disso pra vocês entenderem então onde a gente chega. E eu achei super importante dividir com vocês todo esse histórico porque daí agora fica muito mais simples de vocês entenderem do que eu tô falando. E de novo, vou simplificar pra vocês conseguirem pegar o contexto e depois a gente consegue aprofundar este conceito. Então vamos lá. Até 2017 o que a gente tinha rolando?

00:51

os modelos ali que chegavam do LSTM e do GRU. Quando a gente olhava para esses dois modelos, eles ainda tinham aquele mesmo problema que a gente foi carregando ao longo dos anos desde Markov, desde o bigrama, certo? Que era a dificuldade de a gente capturar a dependência de longo prazo, cada um do seu tamanho. Um bigrama com duas palavras e quando a gente vai evoluindo com as perdas de memória e assim por diante, tudo isso que a gente discutiu até agora, beleza?

01:20

Outra coisa que a gente trazia também de problema e vinha carregando ao longo do tempo, era a incapacidade da gente paralelizar o processamento. Deixava a gente mais lento pra fazer treinamento e assim por diante. Então a sequência ficava muito mais difícil de fazer. E daí com isso a gente demorava muito pra evoluir a IA. Isso deixava a gente amarrado ali, tá? E daí vem o paper.

01:42

Attention is all you need. Parece o nome de música, né gente? Esse paper foi publicado pelos pesquisadores do Google e foi a sacada.

01:52

Na verdade, tinha mais gente falando na academia, mas eles foram os que jogaram isso na mídia e a gente começa a discutir em cima disso. Então, eles propuseram ali uma arquitetura nova chamada Transformer. Dentro dessa arquitetura, a gente exclui, elimina a necessidade dos RNNS. Então, a gente para de ter uma estrutura recorrente e começa a colocar um mecanismo novo que chama auto-atenção, que é o Attention.

02:19

Quando a gente tá falando da auto-atenção, ela começa a ser um marco novo pra IA, começa a mudar todo o paradigma pra gente conseguir evoluir essas arquiteturas, pra gente conseguir ter uma IA generativa mais eficiente. Quem mais se beneficiou disso é a IA generativa. Quando a gente falava ali das IAs, por exemplo, de recomendação, IA de tradução e assim por diante, elas já tinham

02:43

é um caminho um pouco mais pavimentado, mas para as IAs conversacionais, generativas, de vídeo, de som e etc, era mais difícil a coisa acontecer. Bom, chegamos aqui e agora o que faremos, hein? Quando a gente olha esse paper, o que ele traz para a gente nessa atenção? O que está encapsulado aqui? Vou deixar eu explicar para vocês. A atenção, quando a gente está falando no contexto de rede neural,

03:09

ela é um pouco diferente da nossa atenção aqui no dia a dia. A nossa atenção aqui no dia a dia talvez seja focar em um assunto só, certo? Estou com atenção nesse aspecto. Aqui a atenção tem um certo paralelo, mas ela é um pouquinho diferente. A ideia que a gente tem aqui é que quando você processa uma palavra,

03:28

ou um token, imagina que tudo que eu tô falando de palavra depois vai ser transformado em cálculo, vai ser transformado em vetor, então não é nada mais do que uma forma vetorizada ou uma ideia de representação

03:45

numeral daquela palavra, se assim eu posso dizer, ou estatística daquela palavra. Então, quando você cria esse token da palavra, o modelo pode focar em diferentes partes da sequência de entrada que ele está tendo com pesos diferentes. Então, pensa o seguinte, você tem lá a sequência de entrada que a gente falou, uma frase. Eu vou transformar em frase, tirar da ideia do token para a gente ter mais facilidade de conversa. Então, chegou aqui uma frase...

04:13

E ela entrou no nosso processamento dos Transformers. Você começa a focar em diferentes partes desse texto. É o jeito mais fácil da gente explicar isso. Então, imagina que eu vou ter um texto e você consegue focar em diferentes partes desse texto com peso diferente. E dependendo do contexto. Pra quem já sacou como é que funciona a nossa linguagem, que é o que eu tô fazendo o tempo todo de comparar como que a gente pensa na hora que a gente tá falando da nossa conversa,

04:40

Como que a gente pensa na hora que a gente tá entendendo os textos, quando a gente tá se comunicando, já começou a sapear do que eu tô falando aqui. Imagina que se eu foco com pesos maiores em determinadas palavras, eu vou ter algo talvez parecido com o que a gente chama de leitura dinâmica. Talvez eu foco em algumas palavras que me dão contexto e criam relação, certo?

05:00

Eu não sou um grande entendedor de leitura dinâmica, mas quando a gente lê com muita pressa alguma coisa, a gente foca em algumas palavras para a gente conseguir ter mais peso nelas e o resto vem meio que para garantir que a gente não está pensando em uma besteira. É mais ou menos assim que a gente pensa normalmente no dia a dia para a gente ter velocidade de raciocínio. Então como que eu posso conversar disso com vocês? Pensa que na nossa leitura

05:21

Quando eu estou interpretando uma frase, nem todas as palavras vão ter o mesmo peso. Vou dar um exemplo. Imagine que a gente vai pensar no seguinte. O livro que o João leu ontem era interessante. A palavra leu

05:38

ela tá conectada ao livro, certo? E ao João. Porque eu preciso saber quem leu, o que fez e o quê, né? Então, eu tô falando assim, olha, o João leu o livro. Esse é o principal ponto da nossa frase. Era interessante, acompanha, mas não é parte crucial da conversa, certo? Então, por mais que essas palavras estejam distantes, livro tem Q-O no meio, João leu

06:07

aqui perto então você tá pegando aqui ó livro joão e leu elas estão separadas pelo que eu ela tem depois o ontem tem depois o era interessante então se tem um monte de coisa aqui no meio mas o livro o livro a palavra livro e joão leu é o principal item aqui de conexão a atenção do modelo de atenção consegue falar assim cara foca

06:30

no livro, no João e no Leo. O resto ele vem acompanhado, ele não é obrigatório de atenção. Entenda que tudo vai ser prestado atenção, o modelo vai olhar pra tudo, mas aqui ele coloca mais peso nessas palavras pra correlacioná-las. Então esse é o grande ponto de diferença do que a gente tinha até então. E o que que essa self-attention faz? O mecanismo ele então pega essas palavras e ele observa todas as palavras da mesma sequência

07:00

e calcula a importância relativa de cada uma dessas, ou seja, ele transforma tudo isso que eu falei pra vocês em cálculo. Então, ele vai calcular qual é a importância relativa de cada uma das palavras que ele tá vendo ali naquele texto pra compor sua própria representação. Então, quando a gente consegue criar uma forma de compreender o peso de uma palavra dentro de uma frase, facilita a conversação, facilita a compreensão do texto. Então, um exemplo de novo. Imagina que o cachorro que o menino viu

07:29

Estava latindo. O cachorro que o menino viu estava latindo. Para a gente entender o latido, o modelo presta atenção no cachorro para saber que o cachorro que está latindo. Ignora o menino, mesmo que o menino esteja mais próximo

07:47

do do latiu é certo então o menino tá mais próximo do que do que o latiu porque o cachorro que o menino viu estava latindo o menino tá mais próximo do latindo mas quem tava latindo era o cachorro na hora que doideira para uma programação é muito complexo você viu como eles foram parar distantes mas o mecanismo de self attention vai fazer o seguinte vai dar mais peso pro cachorro pra ele saber que quem latiu não foi o menino foi o cachorro então ele tá trazendo pra cá essa

08:16

Essa forma de você permitir com que as palavras, por mais que distantes, criem conexões por sua força de conexão. Então é mais ou menos disso que a gente tá falando. Acho que deu pra ficar mais claro aqui, né? Eu tentei ser repetitivo, mas eu acho que é um assunto que é um pouquinho chatinho de entender. E essa é a grande sacada que fez as coisas evoluírem, tá bom?

08:37

E como que funciona esse transformer? Transformer é uma arquitetura, gente. Uma arquitetura de ML, no final das contas. Então ela é composta por alguns blocos de dois componentes principais. A gente pode pensar em dois componentes principais. Na verdade três, mas eu vou focar em dois e o último ele chega só pra acompanhar. Então a primeira coisa é uma camada de alta tensão.

08:58

Cada token de entrada, ou seja, cada palavra no nosso cenário aqui de entrada, não é bem uma palavra, depois eu explico como funciona um token, mas eu não vou trazer essa discussão para agora, porque senão vai ficar muito complicado a nossa conversa, um token é mais completo do que isso. Mas então, cada palavra vai ser comparada com todas as outras para calcular os pesos de atenção, beleza? Então, imagina que cada palavra aqui

09:24

Ela vai ser calculada e você vai dar um peso para ela de atenção. Então esse atributo acompanha essa palavra. Esse peso ele vai determinar quanto que cada token será considerado ao formar uma nova representação. Então aqui você consegue criar uma representação de força de cada token. Palavra, não é bem uma palavra, mas vamos fingir que é palavra.

09:45

Outro ponto que a gente tem que é super importante, são as camadas de feedforward. Então a gente não trabalha mais só com uma intencionalidade, a gente tem uma camada de feedforward. Então após atenção, cada token ele começa a ter uma rede neural densa, chama MLP.

10:02

E essa rede neural vai transformar cada representação individual. Então, a gente mudou o paradigma de só uma ideia de feedforward. Com isso, eu consigo permitir um negócio chamado não linearidade de aprendizado. Então, eu não vou ter um padrão de aprendizado linear, eu vou começar a ter camadas de feedforward que transformam em não linearidade, porque elas se cruzam no final das contas. Então, esse MLP que depois eu entro com vocês para explicar,

10:29

mostra a densidade da rede neural e que faz a gente sair daquele outro problema que a gente tinha de processamento que era cada coisa processando sozinha agora consigo processar é coisas em paralelo tá bom então aqui tem o terceiro item que eu falei pra vocês que ele chega um pouco ali é próximo mas ele não tá no mesmo grau de importância desses dois primeiros ao meu ver que chama

10:52

O Positional Encoding é uma forma de você conseguir pegar os tokens

11:04

e colocar uma posição pra cada um deles, mais ou menos. Então, pensa assim, como os Transformers não vão processar o token de forma sequencial, como os RNNs que a gente falou, ou seja, eu não vou processar só de uma forma feedforward, é necessário que eu consiga colocar uma posição pra cada um. Tô dando, então, uma posição na fila pra cada um desses tokens. Pensa assim,

11:25

Estou dando um número para cada um para a gente ter a posição deles. E com base nisso, eu consigo depois sequenciar esse cara para conseguir ter a conversa. Então, essa codificação é adicionada aqui aos embeddings. Lembra que a gente falou desses lá atrás? Para manter o sentido da ordem do que eu estou falando. Então, eu consigo processar em paralelo, dar um ticket para cada um falando... Olha, o seu número é tal, o seu número é tal, o seu número é tal... E depois eu venho e junto tudo que faz sentido para aquela numeração. E com isso, eu consigo processar muito mais coisa. Viu como mudou para caramba tudo o que a gente estava falando?

11:54

então aqui a gente vê uma mudança gigantesca é isso é aqui é o ponto que eu queria chegar com vocês porque daqui pra frente fica muito mais fácil vocês compreenderem o que está rolando por trás como que essas coisas funcionam lógico que aqui tem muito cálculo muita estatística muita é

12:10

muito muito código também para fazer isso acontecer, mas essas são as arquiteturas que acompanham o que hoje a gente chama de Gen AI de forma tão trivial, querendo ou não. E quais são os benefícios dessa arquitetura principais? Eu sei que já ficou claro, mas eu vou passar para vocês de novo. Então, diferente do que a gente tinha ali de RNNs, quando a gente chega com os Transformers, você consegue processar todos os tokens

12:34

palavras simultaneamente então com isso eu consigo fazer o processamento ser muito mais rápido eu consigo ter uma aceleração no treinamento e daí com isso tendo hardware que eu tenho hoje o moderno GPU e TPU eu consigo ser muito mais rápido no treinamento de máquina coisa que antes não conseguia antes eu tinha uma barreira tanto de máquina quanto das arquiteturas que estavam ali

12:58

E daí quando eu tenho isso pra me acompanhar, eu começo a ter um outro benefício, o aprendizado de dependências longas. Como eu falei pra vocês, a partir de agora eu consigo captar as relações entre palavras distantes, que tem mais prioridade e sem degradação do gradiente. Então eu não tenho mais aquele ponto de degradação do gradiente, perdendo a importância dele e daí começando a alucinar. Então com isso eu consigo resolver outro problema gigantesco.

13:24

e daí resolvendo isso daí eu tenho escalabilidade os transformers eles são extremamente eficientes quando você escala para bilhões de parâmetros então você consegue processar muita muita coisa e manter desempenho e estabilidade que é o principal ela alucina muito pouco com isso você consegue cada vez mais tá treinado e evoluir sem perder a mão ali do que a gente tá falando de uma Gen AI beleza

13:49

Quais são os impactos práticos que a gente vê? A arquitetura de Transformer, no final das contas, virou a base de quase todos os modelos de linguagem que vocês estão vendo por aí hoje, tá? Então, por exemplo, o BERT tá usando isso daí, tá bom? Pra análise de sentimentos, classificação de texto, assim por diante. O GPT, óbvio, chatbot ali, escrita automática, geração de tudo que ele faz ali, todos os caras que estão com ele vão nesse caminho.

14:13

o T5, o Palm, o Llama, todo mundo indo ali na mesma pegada pra tradução, pra multimodalidade, todos esses outros trabalhos que a gente tem de IA também. Então você tá vendo que todo mundo tá indo no caminho de utilização de Transformers, ele mudou o mercado, tá bom? Então além disso, a gente tem também

14:32

O conceito de atenção expandido para outras áreas também. Visão computacional foi beber disso. Então, quando você olha o VIT, tá bebendo do mesmo esquema, tá começando a trabalhar com isso também e com isso tá conseguindo evoluir a visão computacional que faz o que?

14:49

A multimodalidade também de modelos ali como por exemplo o GPT-4 que consegue lidar com imagem, texto, áudio ao mesmo tempo. Porque antes a gente tinha que fazer o que? Focar em um assunto. Eu não conseguiria ter uma IA que ela é multimodal. Eu precisava ter uma IA multimodelo. Ela era uma IA que falava só de texto, só de vídeo, só de imagem, só de som. Aqui eu tô tendo então o GPT-4, por exemplo, e ele começa a falar com o Dalí e trazer imagem. Ele consegue falar, ou Dalí, cada um chama de um jeito,

15:19

você consegue fazer com que essas plataformas se falem muito bem, porque você consegue trabalhar com multimodalidade. E tem uma outra coisa também que vem junto, que é bioinformática, finanças, recomendação, todo mundo começa a beber de se consegue evoluir com os Transformers.

15:36

gente eu fico empolgado quando estou falando dos transformers porque na minha opinião essa foi a grande mudança essa foi a sacada aqui o time lá do google tá de parabéns que conseguiu dar esse salto lógico que teve muita gente que veio e evoluiu e etc mas a primeiro paper tem que dar os parabéns para os caras para trazer isso para a comunidade e daí a coisa foi ganhando corpo e hoje a gente consegue ter

15:58

Esse curso, por exemplo, acontecendo porque a gente evoluiu demais e eu sou um grande entusiasta deste assunto. Galera, eu espero que vocês tenham gostado. Agora a gente começa a entrar de cabeça no que a gente está falando da IA atual. Vamos em frente. Um grande abraço.

## Resumo IA

**Abreviações**
- **LSTM** — *Long Short-Term Memory*.
- **GRU** — *Gated Recurrent Unit*.
- **RNN / RNNs** — *Recurrent Neural Network(s)*.
- **MLP** — *Multi-Layer Perceptron*.
- **BERT** — *Bidirectional Encoder Representations from Transformers*.
- **GPT** — *Generative Pre-trained Transformer*.
- **T5** — *Text-to-Text Transfer Transformer*.
- **PaLM** — *Pathways Language Model*.
- **Llama** — *Large Language Model Meta AI*.
- **ViT** — *Vision Transformer*.
- **Gen AI** — *Generative AI*.
- **GPU** — *Graphics Processing Unit*.
- **TPU** — *Tensor Processing Unit*.

**Resumo**
A aula apresenta os Transformers como a grande virada arquitetural da IA moderna, em resposta às limitações das RNNs, LSTMs e GRUs, especialmente a dificuldade de capturar dependências de longo prazo e a baixa capacidade de paralelização. O instrutor retoma a evolução histórica dos modelos sequenciais para explicar por que o paper *Attention Is All You Need* foi decisivo ao propor uma arquitetura baseada em atenção, eliminando a recorrência como mecanismo central.

O conceito de attention é explicado como um mecanismo que atribui pesos diferentes às partes de uma sequência conforme o contexto. Em self-attention, cada token compara-se com todos os outros tokens da mesma sequência para calcular a importância relativa de cada um, gerando representações contextualizadas. O instrutor usa exemplos de frases em português para mostrar como palavras distantes podem ter relação semântica central, como “João”, “leu” e “livro” em uma frase, ou “cachorro” como o verdadeiro agente de “latindo”, mesmo que “menino” esteja mais próximo no texto.

Em seguida, a aula descreve os blocos principais da arquitetura Transformer: a camada de atenção, que calcula os pesos de influência entre tokens; as camadas feedforward densas, tratadas como MLPs, que refinam as representações com não linearidade; e o positional encoding, que injeta informação de ordem nos embeddings, já que a arquitetura não processa a sequência de forma recorrente. O fluxo apresentado é: entrada textual convertida em tokens/embeddings, adição de posição, cálculo de atenção entre todos os tokens, e posterior transformação por camadas densas.

Por fim, o instrutor destaca os benefícios práticos: processamento paralelo de todos os tokens, aceleração do treinamento, melhor captura de dependências longas, menor impacto da degradação do gradiente e alta escalabilidade para modelos com bilhões de parâmetros. Isso explica por que Transformers se tornaram a base de modelos como BERT, GPT, T5, PaLM e Llama, além de expandirem seu uso para visão computacional com ViT e para aplicações multimodais, como texto, imagem e áudio em sistemas como o GPT-4. A aula também aponta adoção em áreas como bioinformática, finanças e recomendação, reforçando que atenção virou um padrão geral de modelagem de relações complexas.

**Pontos de atenção**
- A grande mudança dos Transformers é abandonar a recorrência como núcleo do processamento.
- A atenção não significa “prestar atenção a tudo igualmente”, mas atribuir pesos contextuais diferentes a cada token.
- Em self-attention, cada token é comparado com todos os demais da sequência; isso é o que permite capturar relações distantes.
- Palavras próximas na frase nem sempre são as mais relevantes semanticamente; o modelo aprende a priorizar conexões corretas pelo contexto.
- As camadas feedforward/MLP vêm depois da atenção e servem para refinar as representações de forma não linear.
- Como não há recorrência, a ordem precisa ser adicionada explicitamente via positional encoding.
- O ganho de desempenho depende fortemente da paralelização e do uso eficiente de hardware moderno, como GPU e TPU.
- Transformers lidam melhor com dependências de longo prazo e reduzem problemas clássicos de degradação do gradiente.
- A escalabilidade é uma vantagem central: a arquitetura permite treinar modelos muito grandes sem perder estabilidade na mesma proporção dos modelos recorrentes.
- O impacto da arquitetura vai além de NLP; ela também sustenta visão computacional, multimodalidade e outras áreas aplicadas.