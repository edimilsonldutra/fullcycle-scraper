Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16379)

## Resumo da aula

LLMs modernos reaproveitam a base dos Transformers e adicionam adaptações arquiteturais e estratégias de implementação para ampliar sua capacidade de modelar linguagem. A ideia central não é substituir o Transformer, mas estendê-lo para lidar melhor com relações contextuais complexas em escala. Retomando o Transformer já estabelecido, o avanço aqui está em como a atenção é refinada para capturar múltiplos sinais ao mesmo tempo.

Single-head attention observa a sequência a partir de uma única perspectiva de relação por vez. Isso permite resolver dependências específicas, mas restringe a análise simultânea de fenômenos como tempo verbal, referência pronominal, ambiguidade e múltiplos sentidos. O efeito prático é uma leitura contextual mais estreita, suficiente para algumas conexões locais, mas limitada para interpretação rica de texto.

O cálculo de atenção usa três vetores por token: Q (query), K (key) e V (value). Q representa o que o token está “procurando” no contexto, K representa a identidade contextual disponível para correspondência, e V carrega o conteúdo que será propagado quando essa correspondência for relevante. No exemplo de um pronome como “ela”, a query equivale à pergunta “quem é ela?”, a key permite localizar a entidade compatível no contexto, e o value entrega a informação usada na interpretação final.

Multi-head attention resolve a limitação anterior executando várias atenções em paralelo, cada uma especializada em um tipo de relação contextual. Em vez de tentar condensar toda a interpretação em uma única leitura, o modelo distribui o trabalho entre várias heads que observam aspectos diferentes da mesma sequência. Isso aumenta a robustez textual porque relações cruzadas passam a ser capturadas simultaneamente, não em etapas isoladas.

A implementação divide os vetores de atenção em subespaços menores, e cada subespaço alimenta uma head distinta. Cada head aprende padrões próprios, como concordância gramatical, relação semântica, referência pronominal, atenção temporal ou hierarquia sintática. Ao final, as saídas dessas heads são concatenadas e enviadas para a camada feed-forward, combinando leituras parciais em uma representação mais completa.

Uma forma útil de interpretar as heads é tratá-las como mecanismos especializados, não como regras fixas programadas manualmente. Uma head pode se tornar sensível a concordância, outra a vínculos semânticos e outra a dependências pronominais, desde que isso seja útil durante o treinamento. Essa especialização emergente explica por que LLMs conseguem manter coerência textual melhor do que uma atenção única.

Geração de linguagem depende de estrutura linguística, não apenas de processamento numérico. Quando o modelo distingue referência, tempo, função sintática e relação semântica, ele melhora a construção de frases e a consistência do texto produzido. Por isso, entender atenção em LLMs exige conectar arquitetura de rede com fenômenos de gramática e interpretação.

## Transcrição

00:02

Fala galera, beleza? Vamos dar uma evoluída agora então e entrar um pouco mais a fundo na estrutura dos LLMs? A gente falou bastante sobre LLMs sim, mas eu quero aprofundar um pouco essa matéria com vocês, esse tema com vocês. Então vamos lá!

00:17

Quando a gente vai aprofundar para os LLMs, a gente tem que partir de um princípio. Os LLMs que a gente tem hoje, eles vieram evoluídos dos Transformers, então eles já usam os Transformers e colocaram algumas camadas adicionais de arquitetura dentro deles ou de estratégias de implementação que fazem eles serem melhorados ainda

00:35

em relação aos Transformers, eles já estão com algumas camadas além, tá bom? Então os LLMs eles são, pensa, o Transformer melhorado pra conseguir entregar o que eles estão fazendo hoje. Então eles tem várias adaptações ali, vou falar da primeira com vocês e vou tentar ser o mais simples possível pra gente conseguir evoluir e que vocês entendam realmente, eu não quero só passar aqui falando e vocês não conseguirem reter essa informação. Então eu vou tentar ser o mais chatinho possível pra explicar pra vocês o detalhe dessa coisa, tá?

01:04

Então, o primeiro cara que a gente tem que falar são as camadas de atenção. A gente falou delas, lembra? A gente já falou sobre essa camada de atenção, o que é? Imagina que você tem um texto e você é como se prestasse atenção em certos elementos da gramática do texto ali pra conseguir ter uma coerência em longos espaços.

01:22

Essa coerência, essa camada de atenção, ela traz uma problemática. Porque ela consegue ter um single attention. Então ela vai começar a ter atenção em uma coisa. Ela não consegue ter muito mais do que isso. E quando a gente pega os LLMs modernos, eles trabalham com uma coisinha que se chama multi-head attention. Então eles trabalham com vários single attentions. O que isso significa? Cada multi-head, então cada cabeça disso aqui, ela vai aprender um tipo de relação contextual.

01:48

imagina que a gente tem, por exemplo, tempo verbal, emoção, objeto direto e assim por diante tem várias coisas ali que você precisa ter atenção para conseguir manter correlação

01:59

você vai trabalhar com várias delas em paralelo, multi-head pra você conseguir entender as diferentes relações cruzadas simultaneamente, porque daí você vai te dar mais segurança textual, beleza? Então você não vai olhar uma coisa, depois a outra, depois a outra, depois a outra e tentar conectar tudo. Você vai trabalhar isso já buscando uma conexão no multi-head attention aqui, beleza? Mas pra entender o multi-head attention eu vou começar de um cálculo mais simplificado

02:24

que tá aqui na tela pra vocês, que é o cálculo de single-head attention. O single-head attention, ele parte deste cálculo que vocês estão vendo aí, tá bom? Esse cálculo, ele tem algumas variáveis, se vocês olharem ali. Q, K e V, beleza? Então você tem o Q, o K e o V. O que significa primeiro? O Q é a query, beleza? O K é a key, a chave. E o V é o valor, velho.

02:52

cada palavra, ela vai ter atenção calculada em cima desses três vetores, tá bom? Então, dentro dessa somazinha aqui, dessa soma, não, desse cálculo, você vai ter esses três vetores sendo trabalhados. E o que que significa isso? Imagina que o Q aqui

03:15

A query é como se fosse uma pergunta, uma query mesmo, né? Então é como se cada palavra precisasse de contexto, ela pergunta o contexto, então ela tem a query dela ali. Vou fazer um paralelo aqui pra vocês. Imagina que eu quero saber quem é ela.

03:30

Eu tenho ela ali chegando, a palavra ela. Eu preciso saber quem é ela. Essa é a pergunta, essa é a query. Então vem ela, eu preciso saber quem é ela. Então a query é quem é ela. Seria mais ou menos isso, tá numa abstração aqui pra gente conseguir compreender. Quando eu pego aqui, ela já é a identidade de cada palavra no contexto, é uma chave mesmo. Nessa chave é como se fosse um crachazinho dizendo assim, olha, ela é a Maria.

03:55

então você tem a query que é quem é ela e você vai ter aqui que ela é a maria você conseguiu conectar ou por exemplo eu tenho uma query que é quem é ele e você pode dizer ele é o carro precisa ser sempre pessoa pode ser objeto então eu sou o carro

04:14

Aqui vai ser eu sou o carro, eu estou te perguntando e ele vai te dar a resposta, você vai criar a correlação. E tem o V que é o Value, que é essa resposta de qual o resultado final que você vai usar para conseguir chegar no significado do que você busca ali, tá bom?

04:31

Tentei trazer da forma mais simples o que essa conta significa, porque essa conta no final das contas vai precisar ser calculada, mas o que ela significa é isso. O que ela tá fazendo por trás, o que cada letrinha dessas quer representar, é mais ou menos isso que eu contei pra vocês, beleza? E vamos lá!

04:47

Quando você está falando do Single Headed Attention, então ele vai trazer essa dificuldade. Fiz isso para uma coisa, para saber quem é ela, por exemplo. Consegui criar aqui uma conexão para responder uma pergunta. Ela vai conseguir resolver um problema, mas ela foca só em uma perspectiva por vez. Apenas uma relação

05:05

inicial. Você não consegue colocar, por exemplo, tempo verbal junto com outra relação ali que você precisa fechar. E daí com isso você vai perder algumas nuances importantes de texto que você precisa ter. Então, por exemplo, você não vai conseguir ver ambiguidade, você não vai conseguir ver ironia, múltiplos sentidos, esse tipo de coisa você perde se você for só numa single-head attention. Quando você traz a multi-head, você consegue trabalhar isso. Então você tem essa coisa que a gente falou ali evoluída, tá bom?

05:31

Então, ao invés de ela fazer uma única atenção, ela vai trabalhar com mais do que uma em paralelo. E como isso funciona? Você vai dividir esses vetores em espaços menores

05:42

pra você conseguir trabalhar. E cada um desses espaços menores, que é cada uma das heads que a gente falou lá, então a gente falou multi-head. Então cada um desses espaços é uma head. Cada uma dessas heads vai focar a sua atenção em uma coisa. Então é como se fossem várias cabeças pensantes, cada uma focando em uma coisa. Como se eu tivesse dado uma tarefa direta pra cada uma das cabeças. E no final, o resultado de todas essas cabeças vai ser concatenado pra conseguir gerar uma camada de feed-forward pra você conseguir trabalhar o conteúdo.

06:09

Entendeu? Então, se a gente parasse pra olhar, vou pensar aqui numa estratégia, comecei a rodar ali várias heads, abri 5 heads, tá bom? A primeira ela vai olhar, por exemplo, concordância gramatical, a segunda vai olhar a relação semântica, a terceira pode olhar, por exemplo, uma atenção temporal, a quarta pode olhar, sei lá,

06:30

uma referência pronominal, e a quinta vai olhar uma hierarquia sintática, pra gente conseguir chegar numa construção de frase completa. Aqui, você consegue criar um conteúdo que passou por grande parte do que a gente fala na gramática, certo? Por quê? Como que você fez isso? Você deixou de forma poderosa a quebra de atenção pra cada um destes itens. Aqui são exemplos, tá gente? Só pra vocês entenderem em como essa construção tá funcionando por trás. Poxa Nath, mas você tá falando um monte de coisa que é mais sobre português do que sobre IA.

06:58

Mas pense o seguinte, a Gen AI tem que focar na geração de conteúdo, no nosso caso aqui é de linguística. Então, isso precisa ter correlação direta e como funciona, você precisa aprender muito sobre gramática para entender como vai funcionar essa geração de conteúdo. Bom, quando a gente está falando de aprofundamento de LLMs, esse é o primeiro pilar incluído ou a primeira camada incluída na nossa visão de Transformers. Eu já volto para falar de mais umas para vocês.

## Resumo IA

**Abreviações**  
- **LLM**: *Large Language Model* (modelo de linguagem de grande porte)  
- **Transformer**: arquitetura de rede neural baseada em atenção  
- **Q**: *Query* (consulta/pergunta)  
- **K**: *Key* (chave)  
- **V**: *Value* (valor)  
- **Gen AI**: *Generative AI* (IA generativa)  

**Resumo**  
A aula aprofundou a estrutura dos LLMs modernos mostrando que eles são uma evolução dos Transformers, com adaptações arquiteturais e estratégias de implementação que ampliam a capacidade de modelar linguagem. O instrutor explicou que o foco não é abandonar o Transformer, mas refiná-lo para lidar melhor com relações contextuais complexas em escala. Primeiro, retomou a ideia de atenção como um mecanismo que ajuda o modelo a manter coerência em sequências longas, observando elementos relevantes do texto para conectar informações distantes. Em seguida, apresentou a limitação da *single-head attention*, que trabalha uma única perspectiva de relação por vez e, por isso, tende a ser estreita para captar simultaneamente fenômenos como tempo verbal, ambiguidade, ironia, múltiplos sentidos e referência pronominal.  

Na parte de cálculo, foram explicados os vetores Q, K e V: a *query* representa o que o token está buscando no contexto, a *key* funciona como uma identidade contextual para comparação e o *value* carrega a informação efetivamente propagada quando há correspondência. O exemplo do pronome “ela” foi usado para ilustrar o fluxo: a query seria a pergunta “quem é ela?”, a key permitiria localizar a entidade correta no contexto e o value entregaria o conteúdo necessário para formar a interpretação final. Depois, a aula introduziu a *multi-head attention* como solução para a limitação da atenção única. Em vez de uma única leitura contextual, o modelo divide os vetores em subespaços menores e executa várias heads em paralelo, cada uma especializada em um tipo de relação, como concordância gramatical, relação semântica, atenção temporal, referência pronominal ou hierarquia sintática. Ao final, as saídas das heads são concatenadas e enviadas para a camada feed-forward, formando uma representação mais rica e robusta. O instrutor reforçou que essas heads não são regras fixas programadas manualmente, mas especializações que emergem durante o treinamento conforme úteis para a tarefa.  

**Pontos de atenção**  
- A *single-head attention* é útil, mas limitada: ela captura bem uma relação por vez, porém perde nuances importantes quando o texto exige múltiplas interpretações simultâneas.  
- Ambiguidade, ironia, múltiplos sentidos e dependências contextuais mais ricas tendem a ser mal representados com apenas uma cabeça de atenção.  
- Q, K e V não devem ser vistos só como variáveis matemáticas; cada um tem papel semântico no mecanismo de atenção: buscar, comparar e propagar informação.  
- A *multi-head attention* não significa “mais do mesmo” em paralelo: cada head pode especializar-se em um tipo diferente de relação contextual.  
- A divisão em subespaços menores é parte essencial do funcionamento da multi-head; não é apenas replicar a mesma atenção várias vezes.  
- O resultado final das heads é combinado por concatenação antes de seguir para a camada *feed-forward*; esse passo integra visões parciais em uma representação mais completa.  
- As heads não seguem regras humanas fixas; a especialização é emergente e depende do treinamento.  
- Para entender LLMs, é importante conectar arquitetura de rede com gramática e interpretação linguística, e não apenas com processamento numérico.  
- A geração de linguagem depende da captura correta de relações como referência, tempo, função sintática e semântica; ignorar isso prejudica a consistência textual.