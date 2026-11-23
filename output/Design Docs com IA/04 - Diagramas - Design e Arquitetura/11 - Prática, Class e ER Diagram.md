Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17080)

## Resumo da aula

Class diagram em Mermaid representa estruturas próximas do código: classes, structs, atributos, métodos e relacionamentos. Essa visão se aproxima do nível de detalhe do C4-Code, porque torna explícitos contratos internos e tipos que normalmente ficam implícitos em diagramas mais altos. No exemplo do Rate Limiter, RateLimiter, Decision, Options, StorageConfig e RedisConfig aparecem como peças estruturais do design, o que ajuda a enxergar como configuração, decisão e storage se conectam no domínio.

A utilidade principal desse diagrama está em mostrar forma e responsabilidade, não fluxo temporal. Decision concentra o resultado do check, incluindo se a requisição foi permitida, quantas chamadas ainda restam e quando uma nova tentativa pode ocorrer; Options concentra parâmetros como estratégia, limite e duração da janela. Quando StorageConfig contém a configuração de storage e o modo Redis exige RedisConfig, o diagrama deixa visível a separação entre contrato genérico e configuração específica de implementação.

Quanto mais o diagrama se aproxima do código, maior a precisão estrutural e maior o custo de mantê-lo atualizado. Essa granularidade é útil quando o time precisa discutir interfaces, métodos e tipos concretos, mas perde valor rapidamente se o código evolui e o diagrama não acompanha. Por isso, a prática sustentável é regenerar o diagrama a partir da fonte textual ou do código sempre que houver mudança relevante.

ER diagram modela entidades, atributos, chaves e relacionamentos, com foco em estrutura de dados. Ele é especialmente adequado para tabelas, modelagem relacional e definição de como informações se conectam no domínio. No exemplo, campos como ID, Name e Type, além de entidades como Policy, Service, Window e Assignment, mostram a camada de dados do sistema em vez da camada de comportamento.

A diferença para class diagram é o tipo de pergunta que cada um responde. O class diagram responde como o software está estruturado em termos de tipos e contratos; o ER diagram responde como os dados são organizados e relacionados. Quando o objetivo é discutir persistência, chaves e cardinalidade, a modelagem entidade-relacionamento é mais direta do que uma visão orientada a classes.

Mermaid Live Editor é um ambiente web para escrever, renderizar e ajustar diagramas Mermaid em tempo real. Ele reduz o ciclo de tentativa e erro porque a sintaxe textual e o resultado visual ficam lado a lado, o que facilita aprender a linguagem e corrigir problemas rapidamente. Além do uso gratuito, o editor permite salvar diagramas em conta e oferece apoio de IA para correções pontuais de sintaxe.

No flowchart, a primeira linha define o tipo do diagrama e a direção do grafo. flowchart TD indica um fluxograma orientado de cima para baixo (top-down); outras direções mudam a leitura espacial do fluxo. Essa escolha não altera a lógica, mas altera a legibilidade, especialmente quando há muitos ramos ou decisões.

Cada nó recebe um identificador interno e um rótulo visível. Em uma definição como A[User], A é a referência usada nas conexões e User é o texto exibido; a seta A --> B cria a relação entre os nós. O identificador não deve ser reutilizado para outro nó, porque ele representa uma instância única dentro do diagrama.

O formato do delimitador altera o significado visual do nó. No exemplo prático, um nó de decisão é usado para representar o roteador que decide o destino e também a verificação de cache hit no Redis; isso comunica que dali saem caminhos alternativos condicionais. Os rótulos dos ramos, como service A e service B, tornam explícito qual condição ou escolha leva a cada destino.

Essa combinação de nó decisório com labels nos arcos torna o fluxo autoexplicativo. O roteador aponta para Microservice A ou Microservice B, e a decisão de cache aponta para leitura no Redis ou consulta ao banco. Em ambos os casos, o diagrama não apenas mostra que há bifurcação, mas também qual é a semântica de cada bifurcação.

A leitura do código Mermaid deve seguir a mesma ordem das conexões. User chama API Gateway, o gateway passa por um ponto de decisão que escolhe entre Microservice A e Microservice B, e cada ramo segue seu próprio fluxo operacional. No ramo A, a decisão de cache separa o caminho curto de leitura no Redis do caminho mais longo que consulta e grava no banco antes de retornar ao gateway.

No ramo B, a sequência mostra chamada à API externa, verificação de limite no cartão e retorno OK, com ou sem etapa intermediária de aumento de limite. Esse tipo de inspeção textual é valioso porque permite revisar o diagrama como código: você entende o comportamento lendo identificadores, rótulos e setas, sem depender apenas da renderização visual. Em Markdown, basta usar um bloco cercado por três crases com a palavra mermaid para que plataformas compatíveis renderizem o diagrama.

## Transcrição

00:01

Bom, pessoal, e agora que a gente já viu o diagrama de sequência e o flowchart ali pra gente, nós temos um outro tipo de diagrama que é o nosso famoso diagrama de classes. E aqui a gente começa a cair em baixo nível novamente, do mesmo esquema que eu falei pra vocês do C4, do último C do C4. Por quê? Porque aqui a gente acaba tendo também acessos a como é que funcionam esses diagramas.

00:30

Então, nesse caso, diagrama de classe ali com o nosso querido Mermaid Diagram. Então, no final das contas, ele exibe classes, structs, os seus relacionamentos, mostra os atributos, os métodos, as heranças. Ele é bom para explicar a estrutura interna do código e o design do domínio. Então, se você olhar aqui, eu tenho o rate limiter, que eu tenho um check para decidir alguma coisa, e eu tenho um middleware, que é o nosso handler.

01:00

Então, baseado nisso, eu vou retornar uma decisão e a minha decisão pode ter, se ela está permitida, quantos chamados ele pode fazer ainda e depois de quanto tempo ele pode fazer uma duração, dependendo da minha decisão. E aqui é configurado por quem? Configurado, eu tenho uma struct de options no Go, onde eu falo qual é a estratégia, qual é o limite, qual é a duração da janela, etc.

01:25

E esse cara aqui contém a configuração do Storage. Está vendo? Storage.config aqui é um tipo, que é esse tipo aqui. E o Storage como tipo tem aqui o Redis. E o Redis é um tipo também, onde se for usar o mode Redis, eu preciso desse Redis.config. Então, se você olhar, é um diagrama de classes bem simples, se você conseguir perceber, mas

01:51

Além de ele ser simples, eu acho que ficou bem claro, por exemplo, na sua cabeça, nesse momento olhando, como é que funciona o nosso Rate Limiter. Mesmo que se você não tivesse entendido quase nada do nosso FDD, eu acho que isso aqui acaba ficando uma forma bem simples de você olhar. O grande ponto é o nível de granularidade. Aqui ele está trazendo basicamente todas as minhas interfaces, os meus métodos e tudo que eu estou trabalhando aqui nesse meu caso.

02:18

Nem sempre isso é sustentável ao longo do tempo, mas você pode tentar manter isso atualizado. Conforme o seu código muda, você pede para ele regerar esses diagramas ali para você. Maravilha? E aí, a gente tem um outro tipo de diagrama, e esse diagrama vai mais longe ainda, que é o diagrama de entidade e relacionamento.

02:42

Ou seja, aqui nesse nosso caso, no final das contas, eu realmente vou ter aqui, quase que, basicamente, quando a gente está falando principalmente em tabelas, em bancos de dados, esse tipo de coisa.

02:58

Então, eu tenho o ID, o Name e o Tipo, eu tenho a minha Policy aqui, eu tenho aqui o meu Service, o tipo de Window que eu vou trabalhar, o Assignment... Então, se você começa a perceber, eu acho que você já olhou bastante e por muitas vezes esses tipos de...

03:17

diagrama, não sei se você está acostumado, mas normalmente, principalmente quando a gente ia fazer a definição de tabelas em banco de dados, etc. Normalmente isso é muito comum, onde você tem as chaves, o que está relacionado com o que, e etc. Então, esse é um outro tipo de diagrama que você consegue também gerar utilizando o código ali com o Mermaid, tá? Eu quero mostrar aqui rapidamente também aqui para você o seguinte,

03:45

Existe esse site aqui, tá? Ele se chama Mermaid Live Editor. Você pode utilizar ele gratuitamente, mas você pode criar uma conta e você pode ter diversos diagramas salvos lá, e ele tem uma parte de A que ele vai corrigindo o seu diagrama caso você precise, tá? E aqui, ele tem um playground que você pode utilizar.

04:09

e eu estava querendo mostrar para vocês como é que funciona para você entender o código do Mermaid. Então, esse código aqui fui eu que acabei fazendo. Então, se você olhar aqui, eu tenho aquele meu gráfico, que é aquele meu fluxograma no final das contas, e eu tenho aqui TD, que é top-down, ou seja, ele vai ser de cima para baixo, poderia ser left e right. E aqui, o que eu falo? Eu defino A,

04:38

e o nome do A é user. E o user aponta para o B, que é um API Gateway. Então, eu tenho o user batendo um API Gateway. Quando eu tenho o meu C, o meu C eu estou chamando de service A.

04:51

Ok? Se você perceber, o meu C está chamando de Service A. Mas se você olhar aqui esse meu C, onde o B aponta para o C, ao invés dele usar esse colchete, ele está usando essa chave. E chave, nesse caso, significa que é um ponto de decisão. Então, eu coloquei aqui, o roteador decide o redestino. E aí, então, o C pode apontar para o Service A,

05:19

Ok? E o C pode aqui também ser o Service B.

05:24

aqui pra mim, beleza? Ou seja, o que isso significa? Significa que esse service A e B vai ser a label que vai aparecer. Por quê? Porque no final das contas, o meu C vai apontar pro meu D, que é o meu microserviço A. E o meu C vai apontar pro meu E, que é o microserviço B. Você nunca pode repetir as letras, uma vez que você define, é assim que é feita a definição. Então, nesse caso, você vai ver aqui que eu tenho um roteador que decide o destino, aí tem aqui o service A,

05:52

que caiu para o microserviço A, que é o meu ponto D aqui. E eu tenho meu microserviço B, que é o serviço B. Agora que eu tenho esse cara aqui, eu criei um D aqui para mim, que ele verifica se bateu no cache, se foi um cache hit no Redis. Então, o D chama o F, e como tem colchetes, é um ponto de decisão.

06:14

Certo? Então, caso tenha batido, caso seja sim, o que vai acontecer? Ele vai bater no G, que é para ler os dados do Redis. Então, ele caiu aqui. Leu os dados do Redis. Legal? E, caso seja não, ele vai para o H, que é consulta o banco de dados. Legal? E, nesse caso, o H vai apontar para o I, que é gravar no banco de dados. E aqui, eu tenho o meu G,

06:43

batendo no meu J, que é retornar a resposta para o Gateway. E aqui eu tenho o meu I,

06:53

batendo também no meu J, retornando a resposta para o Gateway. Ou seja, o NÃO faz com que eu tenha esse passo a mais. O SIM faz com que eu tenha um passo a menos. Então, é basicamente isso. E se você olhar aqui, eu estou batendo, olhando desse lado aqui. Agora, caso seja o serviço B, faz chamada API externa. Verifica se tem limite no cartão, se tiver, retorna OK.

07:20

Se não, aumenta o limite e retorna OK. Então, se você perceber, é dessa forma que funcionam os diagramas Mermaid. Então, se você olhar, é algo muito simples que você pode colocar dentro do seu Markdown, com aqueles três tiques, com aqueles três apóstrofos, e escreve Mermaid, ele vai saber qual tipo. E aqui a gente tem diversos tipos de diagramas, mas normalmente, no nosso caso, a gente vai utilizar sempre muito mais diagramas

07:50

de flowchart, de sequência, de classes, entidade, diagramas de estado também é importante. Vamos ver se a gente dá uma olhada nesse diagrama de estado também.

## Resumo IA

**Abreviações**
- **C4**: modelo de arquitetura em quatro níveis.
- **FDD**: *Feature-Driven Development*.
- **TD**: *Top-Down*.
- **API**: *Application Programming Interface*.
- **Go**: linguagem de programação Go.
- **Redis**: banco/armazenamento em memória amplamente usado como cache e *data store*.

**Resumo**
A aula apresentou o diagrama de classes em Mermaid como uma representação próxima do código-fonte, útil para visualizar classes, *structs*, atributos, métodos, heranças e relacionamentos. O instrutor destacou que esse tipo de diagrama se aproxima do último nível do C4 por explicitar contratos internos e tipos concretos, como no exemplo do Rate Limiter, em que aparecem componentes como RateLimiter, Decision, Options, StorageConfig e RedisConfig para deixar claro como configuração, decisão e armazenamento se conectam no domínio. Também foi explicado que o class diagram serve para mostrar estrutura e responsabilidade, não o fluxo temporal, e que sua utilidade cresce quando o time precisa discutir interfaces e tipos, embora o custo de manutenção aumente conforme o nível de granularidade.

Em seguida, foi apresentado o diagrama ER, voltado para entidades, atributos, chaves e relacionamentos, com foco em modelagem de dados e persistência. O instrutor contrastou esse tipo de diagrama com o diagrama de classes: enquanto o class diagram responde como o software está estruturado em termos de tipos e contratos, o ER diagram responde como os dados se organizam e se relacionam no banco. O exemplo citou entidades como Policy, Service, Window e Assignment, além de campos como ID, Name e Type, para ilustrar a camada de dados do sistema.

Depois disso, a aula mostrou o Mermaid Live Editor como ferramenta web para escrever e renderizar diagramas Mermaid em tempo real, reduzindo o ciclo de tentativa e erro. Foi demonstrado o uso do *flowchart*, começando pela definição da direção do grafo com `TD`, que indica leitura de cima para baixo. O instrutor explicou que cada nó possui um identificador interno e um rótulo visível, que o identificador não deve ser reutilizado e que a forma dos delimitadores altera o significado visual do nó, especialmente para representar decisões. A leitura do código Mermaid foi exemplificada com um fluxo em que User chama API Gateway, o gateway decide o destino entre Microservice A e Microservice B, e o ramo A ainda separa o caminho entre cache hit no Redis e consulta ao banco antes de retornar a resposta. No ramo B, a sequência mostra chamada a API externa, verificação de limite no cartão e retorno OK, com ou sem aumento de limite. Por fim, foi reforçado que Mermaid pode ser embutido em Markdown usando um bloco cercado por três crases com a palavra `mermaid`.

**Pontos de atenção**
- Diagramas de classes em Mermaid são úteis para detalhar o design, mas não devem ser usados para representar fluxo temporal.
- Quanto mais próximo do código, maior a precisão estrutural e maior o custo de manutenção do diagrama.
- É importante regenerar o diagrama sempre que houver mudança relevante no código ou na fonte textual.
- No diagrama de classes, a granularidade pode ficar alta demais; isso é valioso para discutir contratos internos, mas pode perder sustentabilidade ao longo do tempo.
- No ER diagram, o foco deve ser persistência, chaves e cardinalidade, e não comportamento do sistema.
- Em Mermaid, a direção do grafo (`TD`, `LR`, etc.) não altera a lógica, mas muda a legibilidade do diagrama.
- Cada identificador de nó deve ser único e não pode ser reutilizado para outro elemento.
- O tipo do delimitador do nó importa: colchetes, chaves e outros formatos alteram o significado visual, especialmente para decisões.
- Nós decisórios devem ter ramos rotulados para tornar explícita a semântica de cada caminho.
- A leitura do diagrama deve seguir a ordem das conexões; interpretar o fluxo como código ajuda a evitar ambiguidades.
- O Mermaid Live Editor é útil para testar e corrigir sintaxe rapidamente, especialmente para quem está aprendendo.
- Diagramas mais usados no contexto citado são flowchart, sequência, classes, ER e estado; vale escolher o tipo conforme a pergunta que se quer responder.