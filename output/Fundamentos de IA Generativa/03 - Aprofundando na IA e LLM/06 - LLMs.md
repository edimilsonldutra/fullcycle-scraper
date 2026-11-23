Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16377)

## Resumo da aula

LLM é a categoria de modelos de linguagem treinados em larga escala com bilhões de parâmetros e grandes volumes de texto. Retomando a arquitetura Transformer, já vista anteriormente, o ponto novo aqui é a escala: ela permite que o modelo aprenda padrões linguísticos, contexto e adaptação textual com alcance muito maior do que abordagens anteriores. Por isso, LLM não é um produto específico, mas uma estratégia de modelagem e treinamento aplicada a diferentes sistemas. GPT, BERT, LLaMA e Gemini pertencem a essa família, embora tenham objetivos distintos.

Retomando os Transformers, um LLM combina autoatenção, embeddings e camadas feedforward empilhadas. A autoatenção permite que cada token considere os demais tokens relevantes do contexto; embeddings transformam tokens em vetores densos; e as camadas feedforward refinam essas representações ao longo da rede. O ganho não está em um bloco isolado, mas na composição desses três elementos em profundidade e escala. É essa combinação que sustenta a capacidade de modelar linguagem com coerência e contexto.

O pré-treinamento expõe o modelo a bilhões de tokens vindos de livros, sites, fóruns e código-fonte para que ele aprenda regularidades da linguagem. Esse processo costuma usar autossupervisão, em que o próprio texto fornece o sinal de treino ao exigir previsão da próxima palavra ou preenchimento de lacunas. O resultado é um modelo geral, capaz de capturar estilo, estrutura e relações semânticas antes de qualquer especialização. A qualidade e a quantidade dos dados importam diretamente, inclusive porque o treinamento depende de corpora extensos e, às vezes, controversos do ponto de vista autoral.

Depois do pré-treinamento, o modelo pode ser refinado para tarefas específicas por meio de fine-tuning supervisionado. Esse ajuste direciona o comportamento para aplicações como classificação, resposta a perguntas ou outros usos mais delimitados. Em vez de treinar um sistema do zero para cada problema, parte-se de uma base generalista e adapta-se o modelo ao domínio desejado. Isso reduz custo relativo e aumenta a utilidade prática do modelo em cenários reais.

RLHF significa Reinforcement Learning with Human Feedback, ou reforço de aprendizado com feedback humano. Nesse processo, preferências humanas ajudam a orientar quais respostas são mais úteis, adequadas ou alinhadas ao comportamento esperado. O efeito prático é menos sobre aprender gramática básica e mais sobre ajustar estilo de resposta, utilidade e aderência a instruções. Sistemas conversacionais amplamente usados incorporam esse tipo de refinamento para evoluir ao longo do tempo.

LLMs conseguem gerar texto fluente, responder de forma contextualizada, resumir, traduzir, analisar sentimento e imitar estilos de escrita. Em modelos mais avançados, aparecem capacidades emergentes como raciocínio em múltiplas etapas, resolução de problemas lógicos e execução de tarefas com poucas instruções. Nesse contexto entram os regimes few-shot e zero-shot: o modelo realiza uma tarefa com poucos exemplos ou quase nenhum. Isso amplia muito a generalização, porque o sistema deixa de depender exclusivamente de treinamento específico para cada caso.

Quanto maior o volume de tokens usado no treinamento, maior a chance de o modelo aprender relações, padrões e conexões linguísticas mais fiéis. A escala melhora a cobertura estatística de palavras, fragmentos, pontuação e contextos, o que tende a elevar a performance do modelo final. Em termos práticos, versões mais novas de uma mesma família frequentemente evoluem por combinar mais dados, mais parâmetros e mais refinamento. Essa progressão explica parte da diferença entre gerações como GPT-3, GPT-3.5 e GPT-4.

GPT significa Generative Pretrained Transformer e segue uma estratégia autoregressiva de previsão da próxima palavra. O modelo processa o contexto em uma direção e gera a continuação token por token, o que o torna especialmente forte em geração textual, respostas abertas e storytelling. Retomando os Transformers, a novidade aqui não é a atenção em si, mas o objetivo de treino orientado à continuação de sequência. Por isso, produtos como ChatGPT, GitHub Copilot e Jasper se encaixam bem em cenários de assistência e produção de conteúdo.

BERT significa Bidirectional Encoder Representations from Transformers e foi projetado com foco maior em compreensão do que em geração. Seu treinamento considera o contexto dos dois lados de um token faltante, o que favorece tarefas como classificação, análise de sentimento, busca, extração de informação e pergunta e resposta. Em vez de continuar texto livremente como o GPT, BERT se destaca quando o problema exige interpretar com precisão um trecho textual. Essa diferença de objetivo explica por que modelos da mesma família Transformer podem servir a aplicações muito diferentes.

LLMs mudam o paradigma porque substituem vários modelos estreitos por uma base generalista que depois pode ser adaptada. Eles operam com representação semântica, não apenas com frequência superficial de palavras, e conseguem transferir conhecimento entre tarefas com pouco exemplo. O resultado é uma aproximação maior do comportamento linguístico humano em fluência, coerência e flexibilidade. Essa combinação tornou os LLMs centrais na IA generativa contemporânea.

## Transcrição

00:00

Bom galera, vamos começar então a falar de LLM. Se a minha estratégia deu certo, agora vai ser muito mais fácil de você entender LLM. Eu tentei trazer até aqui da forma mais tranquila e mais simples possível, pra agora quando você ouvir o LLM ele parecer simples também. Se eu tivesse falado direto de LLM no começo, possivelmente ia ter muita dificuldade de entendimento. Então se minha estratégia deu certo, você vai achar essa aula simples. Então vamos lá.

00:27

O LLM é o Large Language Model. Então, quando a gente tá falando disso, é basicamente o termo que a gente usa pra descrever todas as linguagens de larga escala que a gente vê hoje em dia, tá bom? O que que é isso? São linguagens que são treinadas ali com bilhões de parâmetros e um grande volume de dados no final do dia. De volume de dados de texto, principalmente.

00:48

esses modelos eles não vão apenas memorizar padrões, mas eles também entendem como funciona a representação, por exemplo, de contextualização de linguagem e assim por diante para conseguir realizar tarefas que você precisa de fluência, coerência, adaptabilidade textual, beleza? Então quando a gente está falando basicamente do que está mais no dia a dia das pessoas que acham a GPT e comparam esses carinhas, eles normalmente estão usando

01:16

por trás LLMs que são as estratégias para a gente conseguir compreender o linguajar entre máquina e homem aqui no final do dia. Então, essa forma de treinamento é o que permite essa capacidade generativa no final do dia, tá bom? Esses modelos normalmente são baseados na arquitetura Transformer,

01:36

mas cada um pode ter um diferente objetivo. Eu vou falar um pouco disso pra vocês. Quando a gente fala LLM, muita gente compreende isso como uma coisa só. LLM é como se fosse uma estratégia. Uma estratégia de arquitetura de treinamento, eu posso dizer assim. Não só uma coisa, tem vários LLMs. E a gente vai falar um pouquinho disso, tá bom? Então, pensa o seguinte. Se tudo que a gente falou até agora

02:01

deu certo e entrou na sua cabeça, agora chegou a hora da gente juntar tudo pra vocês entenderem como as coisas se falam. Então, toda aquela história do bigrama, de vir evoluindo a forma como a IA funciona, agora traz mais clareza quando a gente cria o LLM e junta tudo isso num bolo só. Que dentro do LLM e da arquitetura de Transformers, você basicamente tem tudo isso incubado, se é assim que eu posso dizer, tá bom? Então...

02:29

Quando a gente tá falando da base técnica de LLM, então ela é baseada em Transformers, tá bom? Então esses LLMs baseados em Transformers, eles vão operar com algumas coisas que a gente já falou aqui. Um, auto-atenção. A gente já falou sobre isso, certo? Então vamos lembrar lá, cada palavra

02:45

que no final das contas eu expliquei na última aula, são os tokens e não palavras. Então cada token presta atenção em todo o resto de tokens que foi gerado, em todas as outras sequências que estão sendo geradas. Lembram disso? Então lembra que a gente falou de palavras, agora a gente só muda isso para token porque a gente já aprendeu o que é token. Então cada token ele vai prestar atenção em tudo que rolou

03:08

ali naquela conversa, ali naquela discussão, quando a gente tá falando sobre a criação ou comunicação, beleza? Tem outro conceito que a gente falou também, são os ebendings, que são a representação ali dos tokens em vetores, pra gente conseguir ter uma multidimensão mais densa de estratégia de busca ali, no final das contas, de proximidade.

03:31

A gente falou também do Feedforward, a gente falou bastante de Feedforward, lembra gente? Então a gente falou de Feedforward e depois a gente falou das camadas empilhadas de Feedforward, quando a gente conseguiu evoluir isso para processamento em paralelo. Então essas múltiplas camadas também estão aqui incluídas nessa representação. Basicamente o LLM ele é formado desses três grandes blocos, tá? E como que ele funciona ali no dia a dia? O modelo ele vai ser treinado com muito texto em

04:01

em larga escala. Então ele tem um pré-treinamento para ele começar a conseguir ter uma atuação junto com o usuário, pensa assim. Então antes do chatGPT, por exemplo, jogar para todo mundo, ele teve um pré-treinamento muito grande, muito massivo, para conseguir entrar no jogo ali, conseguir ser utilizado pelas pessoas. Então esse pré-treinamento

04:21

Ele vai ser um modelo ali que vai ser exposto a bilhões de tokens. Então pensa o seguinte, você vai pegar um monte de livro, site, fórum, código-fonte, tudo quanto é tipo... Perdão, gente. Tudo quanto é tipo de textual e jogar pra ele aprender padrões de linguagem, forma de escrita e assim por diante, pra ele

04:43

ter uma auto-supervisão para prever a próxima palavra e preencher as lacunas que a gente tá tendo ali na hora da criação do texto. Inclusive, teve muita discussão na hora de treinamento de várias dessas LLMs por usar textos, livros, etc. sem direitos autorais ou coisas do tipo. E daí isso também deu uma baita de uma confusão. Ou seja, dado o textual aqui, é uma coisa que é super importante pra essa galera pra conseguir treinar essas LLMs, beleza?

05:12

Depois tem uma coisa que se chama Fine Tuning e Instrução. Depois do pré-treinamento ele pode ser refinado. Então você consegue ter um Fine Tuning ali supervisionado para tarefas específicas, por exemplo, classificação, resposta e assim por diante. Você consegue deixar ele tunado para certo tipo de aplicação no dia a dia. E você também tem um outro negocinho que se chama

05:34

Esse é difícil. RLHF. Eu até anotei aqui para poder falar, porque toda hora eu esqueço que é isso. RLHF. Reinforcement Learning with Human Feedback. Então, é o reenforço de aprendizado com o feedback de um ser humano passando ali. Então, você vai fazer um aprendizado com as preferências humanas e o ChatGPT, por exemplo, faz isso. Ele tem um reenforço de...

06:01

meu deus a gente fala inglês depois para falar em português confunde o certo e tem um reforço de aprendizado tão reenforce de learning é o reforço de aprendizado aqui no chatGPT que ajuda ele a evoluir ao longo do tempo beleza

06:16

Algumas capacidades que os LLMs têm, por exemplo, geração de texto, como escrever textos para conversação aqui no dia a dia com fluência e coerência, pode escrever livro, gera respostas contextualizadas, consegue imitar estilos, por exemplo, de escrita, de vocabulário, de tipo de comportamento textual, tudo isso que a gente consegue

06:41

fazer ali com essas Gen AI de texto, beleza? Consegue ter uma compreensão semântica também, por exemplo, fazendo resumo automático, fazendo uma análise de sentimento inclusive, tradução, tudo isso ele consegue fazer, perguntas e respostas e assim por diante.

06:57

Ele tem uma capacidade emergente de raciocínio e generalização. Modelos como o GPT-4, por exemplo, conseguem trazer para a gente algumas ideias do tipo capacidade de resolver problemas de lógica,

07:15

é, raciocinar multi-etapas, por exemplo, conseguir criar várias etapas sequenciais sem você estar dando tanto direcionamento nesse sentido, e ele consegue ter uma coisa que é super interessante por um momento, que é realizar tarefa com pouco exemplo.

07:32

A gente chama de few-shot, depois a gente também fala um pouco mais disso. Ou com quase nenhum, tem outro negócio que chama zero-shot, que é menos do que o few-shot. Você dá pouquíssimo exemplo, pouquíssima instrução e ele assim consegue realizar algumas tarefas. Ou seja, tá ficando mais inteligente o bichinho, né?

07:49

E quando a gente tá falando dessa formação, então, de uma LLM, dessa arquitetura, querendo ou não, desse treinamento, você precisa de muito dado. E qual que é a importância desse muito dado? Quanto mais tokens você tiver, mais facilidade você vai ter pra armazenar, criar e conectar

08:12

relações e padrões. Então, o que a gente está falando? A gente vai ter os nós, alguns parâmetros que vão agir como nós de aprendizado, que dependem desse conjunto de textos que estão chegando ali. Então, você tem ali tokens que são fragmentados de texto, como eu falei para vocês, e para você conseguir criar essa conexão entre tokens para virar partes de palavras, palavras, pontuações e assim por diante, quanto mais texto você tiver, mais fiel vai ser a realidade, mais fácil vai ser de você chegar ali num cálculo onde eles se conectem, tá bom?

08:42

Então, quanto mais você tiver, quanto mais escala você tiver, maior a performance que você vai ter daquele modelo treinado. Então, quando você pega o chat GPT-3, o 3.5, o 4, eles vêm evoluindo, por exemplo, com mais e mais treinamento. E daí, com isso, ele consegue evoluir cada vez mais, beleza, gente?

09:03

Eu vou falar agora para vocês alguns LLMs que existem, que estão mais no nosso dia a dia, que a gente já deve ter ouvido falar. Então já tinha GPT 3.5, 4, por exemplo, possivelmente você já ouviu. Deve ter ouvido falar um pouco menos, mas alguns de vocês já devem ter ouvido do BERT. O LLAMA também é bem conhecido da Meta.

09:21

A gente também tem o Gemini do Google, tem alguns deles que são bem conhecidos, tá bom? E daí, alguns deles são melhores em algumas coisas e outros são melhores em outras coisas. Por exemplo, o Chat GPT-3 e o 3.5 e o 4, ele tem muito um foco em geração textual e assistente. Esse é o principal foco dele. Geração textual eu falo porque ele também consegue gerar imagens e etc.

09:45

mas eu tenho a impressão que no dia a dia ele tem ali um modelo autoregressivo que facilita para ele fazer principalmente o textual quando eu comparo com outras ferramentas. Já quando você vai para um Gemini, ele já tem uma pegada mais de geração de texto, imagem e código. Ele já foi pensado para gerar essa multidimensão, mas sem ser tão usado para um assistente possivelmente. Você consegue usar? Não estou dizendo que não dá, tá?

10:08

mas ele tem ali um tipo de treinamento de arquitetura mais multimodal, diferente do autoregressivo do GPT-4, por exemplo. Você pega um BERT, por exemplo, o BERT ele tem uma visão mais bidirecional, então ele vai ser bom para, por exemplo,

10:27

compreensão, classificação, comparação, esse tipo de coisa, ele é muito bom. O que mais? O LLAMA, por exemplo, na Meta, o LLAMA, ele é melhor pra pesquisa e desenvolvimento, por exemplo, porque ele tá aberto, então ele tem uma pegada mais open source, então ele vai ser melhor pra evolução e pesquisa e desenvolvimento, possivelmente, ao longo do tempo, tá bom?

10:51

Basicamente tem esses, tem mais alguns, mas eles são menos conhecidos. E vamos falar um pouquinho então de como funciona, por exemplo, o GPT. Para vocês terem um pouco mais de domínio aqui também. Então o GPT da OpenAI, então pensa assim, tudo que é GPT, que foi usado ali pela OpenAI, tem uma ideia principal. Primeiro, o que é GPT? GPT é Generative Pre-trained Transformer.

11:16

Transformer, não, sorry, Generative Pre-trained Transformer, desculpa gente, é um modelo ali autoregressivo como eu falei para vocês, então ele tem uma generativa que vai ser focada principalmente na geração de texto, ele é pré-treinado para tarefas gerais ali com previsão da próxima palavra principalmente, ele vai usar o Transformer

11:38

e com aquela arquitetura que eu falei para vocês, principal de Attention Is All You Need. Então, quando a gente está falando do GPT, ele tem muito essa ideia. E como é que ele funciona? Ele vai ser pré-treinado para prever a próxima palavra com base em uma tonelada de palavras e de textos.

11:55

que foram colocadas para ele anteriormente. Com isso ele é muito bom na geração de texto porque ele consegue fazer as conexões de token como eu falei para vocês. Então com base no histórico do que ele já construiu ele consegue fazer essa evolução. Ele tem uma característica unidirecional, tá bom? Então ele vai normalmente da esquerda para a direita assim como a nossa leitura textual e ele é ideal para a gente conseguir fazer texto, resposta, criação, storytelling e assim por diante.

12:21

A gente tem aqui então alguns caras que são treinados com GPT, eu falei da OpenAI porque é a que a gente mais conhece, mas você tem chatGPT, tem o GitHub, o Copilot, Jasper, todos esses carinhas eles usam esse mesmo tipo de estratégia, tá bom, por trás deles é isso que tá acontecendo.

12:37

Quando a gente olha do Google, o BERT, ele já tem uma outra visão. Ele tem uma compreensão profunda via bidirecionalidade. O que isso significa, tá bom? Antes de tudo, deixa eu explicar o que significa BERT. É um monte de signinho. BERT é Bidirectional Encoder Representation from Transformers. É isso. Bidirectional Encoder Representations from Transformers. Ele foi criado com outra ideia.

13:04

Ele quer compreender texto e não gerar, ele mais pra compreensão. Por quê? Foi criado pelo Google, possivelmente os problemas que eles tinham pra resolver eram mais de busca, e daí com esse entendimento de texto e mapeamento fica como se fosse o meu principal desafio do dia a dia, certo? Possivelmente foi por isso que ele foi mais pra esse lado. Como que o BERT vai funcionar no dia a dia? Ele é treinado então pra preencher lacunas em frases, por exemplo.

13:28

Ele vai entendendo o que vem antes e o que vem depois de uma palavra frautante. Então tá vendo que ele não vai só unidirecional, ele vai pra uma bidirecionalidade, ele tenta buscar os dois lados pra conseguir ter uma busca mais assertiva e conseguir ter uma compreensão melhor daquele pedaço que a gente tá falando.

13:44

ele não é um cara feito para gerar textos, mas para entender e classificar mais do que gerar. Então o GPT é melhor para geração de texto do que o BERT, por exemplo. O BERT foi feito para busca, para modelos de compreensão profunda, principalmente. Ele é ideal então para

14:01

análise de sentimento, classificação de texto, pergunta e resposta, extração de informação, ou seja, ele está buscando coisas e conseguindo evoluí-las. Então perguntas e respostas, você tem uma busca e você tem que achar uma resposta para aquilo. Análise de sentimento é você conseguir compreender um pedaço e falar qual o sentimento daquela coisa. Classificação de texto é entender como aquele texto é e classificar com algo, ou seja, você sempre pega uma coisa e conecta com outra

14:29

aqui para fazer o funcionamento. O BERT é muito focado para isso, tá gente? Então a gente vai ter ele usado em mecanismo de busca, análise de documento, resumo automático, ele é muito bom para isso também. Eu trouxe esses dois exemplos para vocês verem como muda bastante. Tem outros tantos, tem o LLAMA, como eu falei, todos eles, cada um vai ir para um nível e para um conceito, tá bom? Para não deixar essa aula muito pesada, vamos falar então

14:54

Por que os LLMs são tão importantes e por que eu estou focando neles aqui? Quando a gente fala da chegada dos LLMs, eles vão mostrar uma mudança muito profunda no que a gente tinha até então. Primeiro, ele substitui vários modelos que a gente tinha específicos por um modelo generalista. Então ele consegue trazer uma visão generalista que você depois treina para onde você quer ela.

15:18

Ele aprende com representação semântica e vai além só de frequência de palavras. Ele consegue também se adaptar a novos contextos e tarefas com pouco exemplo.

15:36

aquela coisa específica. Agora ele consegue se adaptar mais facilmente e com isso você consegue então criar conteúdo mais fluente, coerente, criativo e assim por diante mais próximo do ser humano. Então basicamente o LLM ele conseguiu se tirar mais próximo da forma como um ser humano funciona e como ele faz as coisas. Por isso que o LLM é tão importante, beleza?

## Resumo IA

**Abreviações**
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Escala)
- **GPT** — *Generative Pre-trained Transformer* (Transformador Generativo Pré-treinado)
- **BERT** — *Bidirectional Encoder Representations from Transformers* (Representações de Codificador Bidirecional com Transformers)
- **LLaMA** — *Large Language Model Meta AI* (Modelo de Linguagem de Grande Escala da Meta AI)
- **RLHF** — *Reinforcement Learning with Human Feedback* (Aprendizado por Reforço com Feedback Humano)
- **IA** — Inteligência Artificial
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)

**Resumo**
A aula apresentou o conceito de LLM como uma estratégia de modelagem e treinamento para modelos de linguagem treinados em larga escala, com bilhões de parâmetros e grande volume de dados textuais. O instrutor retomou a arquitetura Transformer para explicar que a base técnica dos LLMs combina autoatenção, embeddings e camadas feedforward empilhadas, destacando que o ganho vem da composição desses elementos em profundidade e escala. Em seguida, explicou o pré-treinamento, no qual o modelo é exposto a bilhões de tokens provenientes de livros, sites, fóruns e código-fonte, aprendendo padrões linguísticos por autossupervisão, como previsão da próxima palavra ou preenchimento de lacunas. Depois disso, abordou o fine-tuning supervisionado, usado para adaptar o modelo a tarefas específicas, e o RLHF, que aplica feedback humano para alinhar o comportamento do sistema com preferências e instruções desejadas.

A aula também descreveu as capacidades que emergem com esse tipo de modelo, como geração de texto fluente, resposta contextualizada, resumo, tradução, análise de sentimento, imitação de estilos e, em modelos mais avançados, raciocínio em múltiplas etapas e uso em poucos exemplos (*few-shot*) ou quase nenhum (*zero-shot*). O instrutor enfatizou que o aumento de escala, com mais dados e mais tokens, tende a melhorar a performance e a fidelidade das relações aprendidas, citando a evolução de famílias como GPT-3, GPT-3.5 e GPT-4. Por fim, comparou diferentes LLMs do mercado: GPT, voltado principalmente para geração textual e assistência; BERT, orientado à compreensão bidirecional e tarefas como classificação e busca; LLaMA, com apelo mais forte para pesquisa e desenvolvimento; e Gemini, com foco mais multimodal. A mensagem central foi que os LLMs representam uma mudança de paradigma por unificarem capacidades antes distribuídas entre vários modelos estreitos, tornando-se uma base generalista adaptável a diferentes contextos e tarefas.

**Pontos de atenção**
- LLM não é um produto específico, mas uma estratégia de arquitetura e treinamento aplicada a diferentes modelos.
- A base dos LLMs depende fortemente de Transformer, especialmente da combinação de autoatenção, embeddings e feedforward.
- No contexto da aula, “tokens” são a unidade correta de processamento, não palavras inteiras.
- O pré-treinamento exige volumes massivos de dados e sua qualidade afeta diretamente o resultado.
- Há implicações legais e éticas no uso de livros, textos e outros materiais potencialmente protegidos por direitos autorais.
- Fine-tuning serve para especialização em tarefas específicas; não substitui o pré-treinamento.
- RLHF é importante para alinhar respostas ao comportamento esperado, especialmente em assistentes conversacionais.
- Quanto maior a escala de dados e parâmetros, maior a tendência de melhor performance, mas isso também aumenta custo e complexidade.
- GPT e BERT têm objetivos diferentes: GPT é mais forte em geração autoregressiva; BERT é mais forte em compreensão bidirecional.
- BERT se encaixa melhor em busca, classificação, análise de sentimento, extração de informação e pergunta-resposta.
- GPT se destaca em escrita, storytelling, respostas abertas e produção textual fluida.
- Nem todo LLM é multimodal; cada modelo pode ter foco distinto, como texto, código, imagem ou combinação desses.
- Capacidades como *few-shot* e *zero-shot* dependem da generalização do modelo, reduzindo a necessidade de treinamento específico para cada tarefa.