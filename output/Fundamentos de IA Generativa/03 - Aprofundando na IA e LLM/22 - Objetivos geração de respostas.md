Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16393)

## Resumo da aula

LLMs geram respostas prevendo um token por vez com base no contexto disponível e em distribuições de probabilidade aprendidas no treinamento. Retomando o pré-treinamento e a inferência já vistos, o ponto novo aqui é observar a geração como um processo controlável: a resposta final emerge da sequência de escolhas locais do próximo token. Isso explica por que pequenas mudanças no prompt alteram significativamente a saída. Também explica por que o modelo pode parecer “memorizar” respostas prontas em alguns casos, embora operacionalmente continue fazendo predição token a token.

Tokenização é a etapa que converte texto em unidades manipuláveis pelo modelo, e essas unidades não coincidem necessariamente com palavras inteiras. Um token pode ser um caractere, uma palavra curta, um espaço seguido de palavra ou fragmentos de palavras menos frequentes. Essa segmentação importa porque a geração, o custo e a interpretação do contexto acontecem nesse nível, não no nível intuitivo de “palavras humanas”. Quando o texto é quebrado de forma diferente, o modelo passa a operar sobre outra granularidade de representação.

Palavras mais comuns tendem a aparecer em tokens mais estáveis ou mais compactos, enquanto palavras raras costumam ser divididas em vários pedaços. No exemplo com “paralelepípedo”, a palavra é fragmentada porque é mais provável o modelo reutilizar subpartes frequentes do que tratar o termo inteiro como uma unidade recorrente. Isso reduz a necessidade de armazenar tokens longos e raros no vocabulário. Na prática, o modelo compõe a palavra a partir de segmentos que já têm boa cobertura estatística.

Modelos diferentes podem quebrar a mesma frase de formas distintas porque foram treinados com vocabulários, estratégias de tokenização e distribuições de dados diferentes. A comparação entre variantes como GPT-4, GPT-3.5 e versões Legacy mostra que um modelo pode representar “cachorro”, “praça” ou “paralelepípedo” com mais ou menos fragmentação. Quanto maior a fragmentação, maior tende a ser o número de tokens consumidos para expressar a mesma informação. Isso afeta custo, janela de contexto e, em alguns casos, a fluidez da geração.

Cada token processado entra no cálculo de custo e consumo de contexto, por isso tokenização não é apenas um detalhe interno do modelo. Uma mesma frase pode custar mais em um modelo do que em outro se a segmentação for menos eficiente. Retomando a discussão sobre context window, a consequência prática é direta: mais tokens ocupam mais espaço da janela e aumentam o custo de inferência. Entender essa mecânica ajuda a projetar prompts e aplicações com melhor previsibilidade operacional.

A saída de um LLM pode ser orientada para estilos diferentes, como respostas mais factuais, criativas, resumidas, técnicas, informais, empáticas ou diretas. Esse controle acontece por uma combinação de instruções no prompt e parâmetros de geração, que deslocam a distribuição de probabilidade dos próximos tokens. O resultado não é uma troca de “modo fixo”, mas uma mudança no perfil de amostragem da resposta. Por isso, o mesmo modelo pode se comportar de maneiras bastante diferentes sem mudar seus pesos.

Temperatura, Top-K e Top-P são mecanismos para controlar quão conservadora ou diversa será a escolha do próximo token. Em termos práticos, valores mais restritivos tendem a favorecer respostas mais previsíveis e consistentes, enquanto configurações mais abertas ampliam variedade e criatividade. Esse ajuste tem trade-offs claros: ao aumentar liberdade de geração, também pode aumentar o risco de deriva e alucinação. A configuração ideal depende da tarefa, como resumo, geração de código, e-mail ou chatbot.

Compreender tokenização e ajuste de geração permite usar LLMs com mais intenção em tarefas do dia a dia. Resumos, escrita de e-mails, produção de conteúdo, geração de código e chatbots exigem perfis de saída diferentes, e esses perfis podem ser induzidos de forma mais confiável quando se entende o mecanismo interno. O ganho não está apenas em obter uma resposta, mas em obter uma resposta adequada ao objetivo do sistema. Esse conhecimento transforma o uso do modelo de tentativa e erro em engenharia de comportamento de saída.

O OpenAI Tokenizer permite inspecionar visualmente como uma frase é quebrada em tokens em diferentes modelos, sem necessidade de login para testes básicos. Ao digitar frases simples e depois termos menos frequentes, fica fácil observar quando a segmentação é quase “um para um” e quando passa a ser fragmentada em subunidades. Essa visualização torna concreto o que normalmente fica abstrato na teoria de geração. Para quem desenvolve aplicações com LLM, essa ferramenta ajuda a antecipar custo, entender comportamento e depurar prompts.

## Transcrição

00:00

Fala galera, beleza? Vamos dar uma evoluída agora então, entrar no próximo módulo, agora que a gente já entendeu quais são as dificuldades que a gente vai ter com o LLM. Bom, queria falar com vocês um pouquinho do objetivo que a gente tem agora nesse próximo módulo. Eu quero explicar pra vocês e ensinar como que funciona a geração de resposta das LLMs, tá bom? Então, como que a gente vai conseguir chegar na resposta que a gente tem quando a gente começa a fazer um prompt. Acho que essa é a grande sacada que eu quero mostrar pra vocês durante essa aula.

00:28

Então, o primeiro objetivo que a gente vai ter aqui vai ser como compreender como que as LLMs geram essas respostas. Então, a gente vai precisar entender, por exemplo, como funciona uma inferência, como que esse modelo vai memorizar respostas prontas, como que ele prediz um token, um a um, e como que ele usa isso com base na probabilidade. Muito do que a gente falou até agora, mas eu quero dar uma aprofundada com vocês, tá bom? Tem uma outra coisa também que eu quero ver com vocês, que é qual o papel da tokenização, ou seja, como que a gente entende

00:57

como as palavras são quebradas, como elas são representadas internamente no LLM, como o modelo utiliza o contexto para decidir o próximo token, como ele faz para montar isso e como isso importa nos diálogos que ele está formando com a gente, como análise de redação e assim por diante. Então, a gente vai aprender a dominar essa estratégia, ou seja, entender como o motor do modelo

01:19

funciona para geração de respostas, para a gente parar de ser só usuário e a gente começar a entender como é que esse mecanismo funciona. Então a gente falou muito até agora sobre esse assunto, como ele foi evoluindo e etc. Agora eu quero aprofundar com vocês nessa geração.

01:34

Outra coisa também que eu quero falar com vocês é o seguinte, como que os LLMs são ajustáveis, como que você prepara ele pra gerar um resultado da maneira como você quer, ou seja, como que eu controlo estilo, comportamento e saída de resposta. Então, agora pensa que você tá usando um motor, então como é que você tune ele, como é que você decide se esse motor vai ser 1.0, 2.0 e assim por diante. Então, aqui eu quero mostrar pra vocês como que um prompt pode gerar

02:00

diferentes resultados, factuais, criativos, resumidos ou não, a gente começa a mostrar como que a gente organiza uma LLM pra ela dar o resultado mais pra um lado ou mais pro outro, tá bom? Então aqui eu quero te mostrar como é que a gente vai fazer pra, por exemplo, controlar parâmetros como temperatura, a gente vai falar um pouquinho do que é temperatura, um Top K, um Top P e assim por diante pra gente

02:25

receber o resultado sob medida para o que a gente quer. Então se amanhã você quiser treinar uma LLM para ela atender algum business seu ou compreender como que ela vai trabalhar para você, você vai precisar saber isso, tá bom? Outra coisa também, como é que a gente influencia no tom, como que a gente controla as respostas mais técnicas ou mais informais ou mais empática ou mais direta, então como é que você prepara isso? Como é que isso funciona para você conseguir organizar?

02:50

E outra coisa também que eu quero trazer pra vocês é como que a gente evita algumas armadilhas, como alucinação, por exemplo. Porque quando você mexe nesses parâmetros, você abre caminho pra mais alucinação ou menos alucinação. Então como que a gente se prepara pra isso, tá bom? Outra coisa que eu quero também passar pra vocês é como que a gente usa isso no nosso dia a dia, como que a gente vai aplicar isso nos problemas do dia a dia,

03:13

Ou seja, como que a gente vai usar isso pra criar resumo, pra criar código, pra escrever e-mail, pra produzir conteúdo, pra criar chatbot e assim por diante. Vou trazer alguns exemplos então de como a gente pode usar isso no nosso dia-a-dia e como que isso pode melhorar a nossa produtividade ou até virar um business pra vocês, beleza?

03:29

Então aqui é mais do que você só aprender o básico, é a gente começar a aprofundar um pouco mais. A gente já falou ali como funciona, já deu uma entrada no modelo mais intermediário, que normalmente as pessoas não conhecem. E agora a ideia é a gente aprofundar e levar você para um modo um pouco mais avançado de quando a gente está falando de conceitos de LLM. Beleza? Então agora vamos parar de falar e eu vou mostrar para vocês um hands-on. Cinco minutinhos e já volto com vocês para mostrar um hands-on rapidinho.

03:55

Então vamos lá, pra gente fazer esse hands-on, eu quero mostrar pra vocês essa plataforma muito simples, tá? É uma plataforma da OpenAI que chama Tokenizer, tá? Se você pegar esse... eu vou deixar esse link aqui pra vocês, mas é muito simples, né? platform.openai.com/tokenizer Quando você abre ela, ela já tá direto nessa página, tá? Então aqui ele tá explicando um pouquinho como que você pode aprender mais sobre uma LLM aqui, como funciona esse modelo de tokenização.

04:25

Então aqui ele te dá um exemplo como se fosse uma calculadora, ele explica mais aqui se você quiser ler e assim por diante, mas ele te dá um exemplo de como se fosse uma calculadora de como as coisas funcionam. O que que vai acontecer? Aqui você escolhe qual tipo de GPT você quer usar, então você pode usar o GPT-4 e o Mini como que ele faz a quebra de Token, o GPT-3 e o GPT-4 como que ele faz a quebra de Token, o GPT-3 Legacy como que ele faz a quebra de Token. E daí o que que vai acontecer? Quando você escreve aqui qualquer frase, ele vai mostrar pra você

04:55

como que esse negócio tá sendo quebrado aqui em token então vamos só pra vocês entenderem como funciona então lembra que eu falei pra vocês que o token pode ser uma palavra ou pode ser é mais do que isso então por exemplo olha o tá vendo que ele tá mostrando aqui um token um carácter aqui ele tá mostrando o beleza agora vou escrever cachorro olha que engraçado cachorro quantas quantas letras tem

05:22

o espaço cachorro você ainda tá com dois tokens olha que engraçado então você tem o que é um token tá vendo uma letra só é um token já o espaço cachorro é outro token foi já virou outro token tá vendo na

05:43

praça tá vendo que aqui ó basicamente cada é cada palavra virou um token de agora vou colocar um para ele pedido

05:59

Olha que engraçado! Paralelepípedo não é uma coisa que aparece pra ele todas as vezes. Eu fiz isso proposital pra mostrar pra vocês. Até aqui, você tá vendo que é quase que um token e uma palavra. Uma palavra e um espaço, né? Se a gente parar pra pensar. A hora que você vai pra Paralelepípedo, ele quebrou tudo isso aqui, ó. Porque ele entra naquele modelo que eu falei pra vocês. A partir daqui...

06:20

ele está mostrando como aqueles vetores são calculados. Então, a probabilidade de Paralelepípedo aparecer é muito baixa. E daí, o que ele faz? Ele vai quebrar isso aqui em vários tokens, porque é mais fácil ele achar Par, Ale, Lep, Ip e Edo. Quando você olha a criação de vetores, é mais fácil você ver isso se replicando do que a palavra Paralelepípedo.

06:48

Olha que engraçado, tudo bem que fica uma frase nada a ver, né? Colocar o cachorro foi na praça de Paralelepípedo, não sou um bom construtor de frases, mas é mais ou menos isso que é importante da gente entender, como é que funciona essa brincadeira. Então, aqui você pode ir colocando o quanto de coisas você quiser. Então, ele foi na praça de Paralelepípedo. Ou vou mudar aqui, ele foi na praça...

07:11

Pela Rua de Paralelepípedo. Ficou melhor, né? Então tá vendo que até aqui, olha, tudo tá sendo só um pra um. O Paralelepípedo já começou a quebrar. Isso pra esses dois tipos de GPT aqui. Vamos ver esse outro tipo, o que que acontece se eu mudar pra esse motor, o que que ele vai fazer?

07:26

Então eu mudei, tá vendo que é bem parecido, eu não vi nenhuma mudança na verdade. Aqui entre um e outro, ah não, ele mudou, o paralelepípedo, a forma como ele quebra no GPT-4, aqui no 3.5, ele já quebrou diferente, o O é separado do IPD, tá vendo aqui o paralelepípedo principalmente.

07:43

começou a ficar um pouco diferente. O cachorro também quebrou em dois. Olha que engraçado, a praça ele quebra mais. Então quando você sai desse aqui e vem pra esse, ele já começa a quebrar mais. Vamos ver no Legacy. Ele quebra ainda mais, tá vendo? Ele não consegue controlar um token muito grande. Então por que que isso deve acontecer?

08:02

A treinamento desse carinha aqui, ele tem menos tokens. Então no treinamento ele não conseguiu achar que cachorro é uma palavra tão forte, enquanto neste treinamento que é mais forte, você tem mais tokens aqui. Então por isso, ele acaba fazendo essa quebra de tokenização.

08:20

Pessoal, super simples, né? Você pode ficar brincando aqui, ó... Click e começar de novo... Outra frase... Começar... Outra frase... Você pode... Opa... Você pode ficar aqui brincando, colocando qualquer coisa pra você ir vendo como isso funciona e entender como funciona a quebra de token. E cada token desse vai virar um custo quando você tá falando de criação do seu próprio modelo. Mais pra frente a gente vai falar disso, mas aqui é só pra você entender um pouquinho. Você viu que eu não fiz nem login, nem treinada, eu só usei aqui.

08:50

só pra brincar um pouquinho, tá bom? Aqui você consegue entender então, na prática, como funciona essa quebra de Token pra você conseguir compreender melhor como o motor funciona por trás. Espero que você tenha gostado, já já a gente volta pra aprender mais um pouquinho. Um abraço!

## Resumo IA

**Abreviações**  
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)  
- **GPT** — *Generative Pre-trained Transformer* (Transformer Generativo Pré-treinado)  
- **Top-K** — estratégia de amostragem que limita a escolha aos K tokens mais prováveis  
- **Top-P** — estratégia de amostragem por *nucleus sampling*, que limita a escolha ao menor conjunto de tokens cuja probabilidade acumulada atinge P  

**Resumo**  
A aula teve como objetivo aprofundar a compreensão de como as LLMs geram respostas, saindo do uso superficial do prompt para uma visão mais técnica do mecanismo interno. O instrutor explicou que a geração ocorre token a token, com cada novo token sendo escolhido com base no contexto disponível e em distribuições de probabilidade aprendidas no treinamento, o que ajuda a entender por que pequenas mudanças no prompt podem alterar bastante a saída e por que o modelo às vezes parece “memorizar” respostas. Em seguida, a aula focou na tokenização, mostrando que o texto é quebrado em unidades que nem sempre correspondem a palavras inteiras, podendo ser caracteres, palavras, espaços ou fragmentos de palavras mais raras. Foi destacado que essa granularidade impacta diretamente custo, consumo de janela de contexto e interpretação do texto pelo modelo. O instrutor também comparou diferentes modelos e versões de GPT, observando que a mesma frase pode ser tokenizada de formas distintas conforme o vocabulário e o treinamento, o que influencia eficiência e fluidez.

Além disso, a aula abordou como ajustar o comportamento de saída das LLMs por meio de prompt e parâmetros de geração, para obter respostas mais factuais, criativas, resumidas, técnicas, informais, empáticas ou diretas. Foram apresentados os conceitos de temperatura, Top-K e Top-P como mecanismos para tornar a geração mais conservadora ou mais diversa, sempre com trade-offs entre previsibilidade, criatividade e risco de alucinação. Por fim, o instrutor mostrou na prática a ferramenta OpenAI Tokenizer, que permite visualizar como frases são quebradas em tokens em diferentes modelos, facilitando a compreensão concreta do processo e ajudando a prever custo, consumo de contexto e comportamento do modelo em aplicações reais como resumo, escrita de e-mails, geração de código, produção de conteúdo e chatbots.

**Pontos de atenção**  
- A geração de LLMs acontece **token por token**, então a resposta final é resultado de decisões locais sucessivas, não de um “texto pronto” recuperado integralmente.  
- **Pequenas mudanças no prompt** podem causar mudanças grandes na saída final.  
- **Token não é sinônimo de palavra**: uma palavra pode virar vários tokens, e um token pode ser apenas um caractere, espaço ou fragmento.  
- **Palavras raras ou pouco frequentes** tendem a ser mais fragmentadas em subpartes, aumentando consumo de tokens.  
- A **tokenização varia entre modelos e versões**, então o mesmo texto pode custar mais ou menos dependendo do modelo usado.  
- Mais tokens significam **maior consumo da janela de contexto** e potencialmente **maior custo de inferência**.  
- Ajustes como **temperatura, Top-K e Top-P** alteram o perfil de geração, mas aumentam o risco de **deriva** e **alucinação** quando ficam mais abertos.  
- Não existe “modo fixo” de resposta: o comportamento é influenciado por **prompt + parâmetros de geração**.  
- Entender tokenização ajuda a **projetar prompts melhores** e a evitar surpresas de custo e comportamento em produção.  
- A ferramenta **OpenAI Tokenizer** é útil para testes rápidos e visuais, inclusive sem login em usos básicos, sendo boa prática para depuração e análise de prompts.