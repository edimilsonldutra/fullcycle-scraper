Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17226)

## Resumo da aula

Vamos falar agora sobre Software Development Guidelines. Este é um tipo de documento fundamental que precisamos ter. O que são essas Software Development Guidelines? Entendam que quando falo sobre Guidelines, não necessariamente teremos apenas um documento desse tipo. Eventualmente, podemos ter múltiplos documentos, de forma mais específica, em domínios mais particulares do projeto.

Software Development Guidelines são um conjunto de regras e boas práticas que orientam como escrevemos, organizamos e evoluímos o código dentro de um time ou de uma empresa de forma geral. Dependendo do projeto e do time, você pode ter guidelines diferentes, e isso também acontece em nível de governança corporativa. Algumas empresas tentam seguir um padrão bem estrito para toda a organização ou para áreas específicas.

O ponto principal é entender que esse tipo de documento não define apenas o estilo de codificação, mas sim como desenvolvemos software naquele contexto. Quando falamos de Guidelines, muitas vezes pensamos apenas nos padrões de nomenclatura de variáveis, estilo de código, essas coisas. Isso também faz parte, claro. Mas o mais importante é compreender que as Guidelines abrangem todo o processo de desenvolvimento de software em nível de código, linguagem, framework e diversos aspectos que cobrem o fluxo de desenvolvimento.

Qual é a importância disso no universo dos Design Docs? Primeiro, ele facilita enormemente o onboarding automático pela IA. Imaginem a IA como um novo funcionário da empresa, um novo parceiro de time. Quando um novo desenvolvedor entra, fazemos um onboarding, explicamos como programamos, como funciona o ambiente, como subir o ambiente, como desenvolver, como rodar os testes. Com as Guidelines prontas e a IA capaz de lê-las, as coisas mudam completamente. É como dar uma injeção de conhecimento, uma pílula do saber para a IA entender o nosso processo de codificação. Até agora falamos muito sobre arquitetura e decisões técnicas, mas não entramos no ponto mais micro, que é o processo de programar em si. As Guidelines tratam exatamente desse aspecto mais específico.

Outro ponto importante é que as Guidelines reduzem divergências e mantêm consistência. Quando desenvolvemos com IA, se pedimos para ela criar um novo módulo ou funcionalidade sem orientações claras, a forma como ela programa — os padrões de variáveis, comentários, arquitetura — pode ficar inconsistente, fugindo do padrão estabelecido. Com as diretrizes prontas, fica muito mais fácil desenvolver novos projetos, pois já temos uma estrutura clara de como o desenvolvimento deve funcionar.

Além disso, as Guidelines ajudam a reduzir erros. Sabemos que a IA comete erros com frequência. Com as diretrizes bem definidas, fica mais fácil, inclusive, criar verificações automatizadas, como hooks de pré-commit, para validar se o código está em conformidade. Isso reduz erros e retrabalho. Nada é garantido, tudo é probabilístico, mas as Guidelines minimizam esses problemas.

Outro ponto importante também é o ruído em revisões. O que acontece? Uma das coisas mais terríveis no processo de desenvolvimento de software é o ruído. O que são ruídos? Imagine que estou desenvolvendo um software com diversos arquivos, todos organizados. De repente, faço uma alteração e peço para a IA ajustar uma determinada feature. O que pode acontecer? Tenho o arquivo 1, arquivo 2, arquivo 3, e assim por diante. Esses arquivos não têm nada a ver com a feature que estou desenvolvendo, mas muitas vezes a IA, ao ajustar e criar a nova feature, percebe que algum desses arquivos tem alguma relação e começa a fazer pequenos ajustes neles.

Às vezes esses ajustes são simples refatorações, ou melhorias em comentários, e realmente faz sentido que esses arquivos recebam essas melhorias. Mas imagine que quero desenvolver apenas uma feature específica, que vai gerar alterações em um, dois, quatro, cinco arquivos. Na hora de abrir um pull request, de comitar e submeter para code review, eu quero que apenas essa feature seja revisada. Se a IA gerar ruídos, ou seja, sair mexendo em vários outros arquivos, o que acontece? No code review, não terei que revisar apenas cinco arquivos criados, mas sim cinquenta, porque a IA mexeu em outros arquivos, nem que sejam apenas comentários. Os commits começam a ficar inconsistentes, as features passam a ter relações com outras partes do código que não precisariam ter sido alteradas.

Quando trabalhamos com guidelines e temos uma forma muito clara de utilizar a inteligência artificial, evitamos esses tipos de ruído. Imagine pedir para alguém do seu time desenvolver uma feature e a pessoa trazer 100 arquivos modificados porque a IA refatorou tudo. Como você vai revisar isso? Esse é o grande problema dos ruídos.

Outra questão importante é o agente especializado trabalhando em paralelo. Hoje é comum termos agentes especializados em front-end, back-end, Java, PHP, .NET, e até agentes focados em melhorar processos de CI/CD. Esses agentes já têm seus próprios prompts, mas isso não significa que eles vão ditar como o projeto deve ser desenvolvido. Quem dita isso sou eu, através das minhas guidelines. Precisamos fazer com que essas guidelines substituam, de certa forma, alguns comportamentos desses agentes que podem ser executados em paralelo no código, garantindo que não teremos uma bagunça de padrões.

Outro benefício é o code review automático. Com guidelines claras, os agentes que farão o processo de code review conseguem verificar se algo não está de acordo com as diretrizes baseadas naquele commit. Fica muito mais fácil.

Temos também a maximização da previsibilidade em ambientes multimodais. Os modelos hoje conseguem ler imagens, processar texto, vídeo, e os agentes conseguem utilizar tudo isso. Quando temos guidelines claras, podemos especificar que determinada parte do processo deve ser focada em um diagrama C4, ou em um design de front-end. Os agentes, através das guidelines, podem acessar imagens e outros tipos de mídia que facilitam todo o processo. Por exemplo, um agente focado em front-end pode precisar ler guidelines de como desenvolver uma interface, com documentação pronta, exemplos, imagens e diagramas. Isso facilita enormemente.

As possibilidades são infinitas. No próximo vídeo, quero trazer as principais seções que podem inspirar vocês a considerarem a adoção dessas guidelines nos seus projetos.

## Transcrição

00:01

Bom, pessoal, então vamos falar agora sobre Software Development Guidelines. Então, esse é o nosso tipo de documento que nós precisamos ter. E vamos lá. O que são esses Software Development Guidelines? Entenda o que eu estou dizendo sobre Guidelines. Então, não necessariamente você vai ter apenas um documento desse, mas, eventualmente, você pode ter mais desses tipos de documentos também, mas de uma forma mais específica, num domínio mais específico em relação ao seu projeto.

00:30

Então vamos lá, o que é isso? A Software Development Guidelines são um conjunto de regras e boas práticas que vão nos orientar como que a gente escreve, como a gente organiza e como que a gente consegue evoluir o código dentro de um time ou dentro de uma empresa de forma geral.

00:47

Então, eventualmente, dentro do projeto que você está trabalhando, dependendo do time que você tem, você pode ter guidelines para desenvolver de uma forma ou em outros times de outra forma, e também isso acontece em nível de governância de empresa. Tem empresas que tentam seguir um padrão bem estrito para a empresa inteira ou para áreas específicas e etc.

01:09

Agora, o que a gente tem que entender é que esse tipo de documento, essas guidelines, elas não definem apenas o estilo, mas como que a gente desenvolve o software aqui, dentro da empresa, dentro do seu projeto. Por que eu estou dizendo? Porque normalmente quando...

01:26

a gente acaba falando de Guidelines, já vem na mente a forma de como que a gente programa, né? Quais são os padrões das variáveis? Que estilo que eu vou utilizar? Como é que funciona isso? Como é que funciona aquilo? E tá errado? Na realidade, não. Isso também faz parte, tá? Mas o mais importante é que você entenda. Quando eu tô falando de Guidelines é como que eu desenvolvo o software aqui.

01:47

Eu tenho aqui como vai ser o meu processo inteiro de desenvolvimento de software em nível de código mesmo, em nível de linguagem, em nível de framework, em nível de diversos aspectos que cobrem o meu processo de desenvolvimento. Então, esse aí é o nosso principal ponto. E qual que é a importância, se eu pudesse trazer alguns tópicos para vocês, dentro desse nosso mundo de Design Docs. Então, vamos lá.

02:16

Ele vai facilitar muito o nosso onboarding automático pela IA. O que isso quer dizer? Imagine que a IA é um novo funcionário da sua empresa. Imagine que a IA é um novo parceiro seu de time. Imagina que está entrando um novo camarada na sua equipe.

02:34

Normalmente, o que acontece é que a gente faz um on-board, a gente acaba explicando como é que programa, como é que funciona, como é que é o ambiente de desenvolvimento, como que eu subo o ambiente, como eu desenvolvimento, como que eu rodo os testes, etc. Então, uma vez que eu tenho esses guidelines e a inteligência artificial consegue ler, as coisas mudam completamente, porque é como se você tivesse dado

02:57

uma injeção, uma pílula do conhecimento para sua I.A. para ela entender como funciona o seu processo de codificação. Porque até agora a gente falou muito em relação ao nível de arquitetura, nível de decisões técnicas, etc. Mas a gente não entrou no ponto mais micro, que é o processo de programar em si. Então, quando a gente está falando de guidelines, a gente está falando nesse aspecto mais específico.

03:20

Um outro ponto importante é que ele vai reduzir a divergência e vai manter mais consistência. Por quê? Você vai perceber que se você está desenvolvendo dentro de um projeto, muitas vezes com inteligência artificial, e você vai pedir para ela criar um módulo novo, uma feature nova e etc., e se ela não tem orientações claras, pode ser que a forma como ela programe, os padrões das variáveis, os padrões dos comentários, a forma de arquitetar a aplicação e tudo aquilo que tange o processo de desenvolvimento,

03:50

pode ter inconsistência, ou seja, ela começa a fugir de um determinado padrão. Outra coisa é que, uma vez que você tem isso pronto, fica muito mais fácil de você desenvolver um projeto novo, uma vez que eu tenho já uma estrutura totalmente clara de como esse desenvolvimento vai funcionar. Outra coisa é erro. Uma das coisas que inteligência artificial faz é errar bastante.

04:15

Mas uma vez que você tem esses guidelines, ficam inclusive muito mais fáceis, inclusive para você mostrar como que ela pode fazer uma verificação, por exemplo, pré-commit, para verificar realmente se não tem nenhum erro ou alguma coisa desse tipo. Então, vai reduzir erro, vai diminuir retrabalho, porque você vai ter uma garantia, entre aspas, nada é garantido, é probabilístico, mas isso aí vai conseguir minimizar esses tipos de problema. Outro ponto importante também é ruído em revisões.

04:45

O que acontece? Uma das coisas mais terríveis que pode acontecer no processo de desenvolvimento de um software é a parte de ruído. O que são ruídos, no final das contas, pessoal? Imagina que eu estou desenvolvendo um software aqui, e esse software tem diversos arquivos, todos bonitinhos aqui para mim, vários arquivos e etc.

05:09

E aí, de repente, eu faço uma alteração e peço para a IA ajustar uma determinada feature aqui. E o que vai acontecer? De repente, eu tenho esse arquivo 1, eu tenho um outro arquivo 2,

05:27

arquivo 2, arquivo 3, etc. E o que acontece? Esses arquivos aqui, eles não têm nada a ver com essa feature aqui que eu estou desenvolvendo. Mas o que acontece muitas vezes, e eu não sei se você já percebeu a Inteligência Artificial fazendo isso, na hora que ela vai ajustar e criar essa nova feature, mexer nesse arquivo, e eventualmente ela percebe que esse arquivo acaba tendo alguma relação, às vezes ela começa a fazer pequenos ajustes aqui nesses arquivos.

05:55

E às vezes esses ajustes são simples refaturações, às vezes esses ajustes são simplesmente comentários que ela melhora, e realmente faz todo sentido esses arquivos terem essa melhora. Mas imagina que eu quero uma única feature que eu quero desenvolver.

06:13

E se eu quero desenvolver apenas uma feature, e essa feature vai me gerar um, dois, quatro, cinco arquivos, na hora que eu fizer uma pull request, na hora que eu comitar isso e isso for cair para o code review, vai ter somente essa feature. Mas, se eu tiver ruídos, o que significa ia sair mexendo em todos esses arquivos também, o que vai acontecer?

06:34

Na minha Code Review, eu não vou ter que revisar apenas 5 arquivos que foram criados. Eu vou ter que revisar 50, porque a IA saiu mexendo em outros arquivos, nem que sejam comentários. Então, os meus commits começam a ficar inconsistentes, as minhas features começam a ter relações com outras features ou outras partes do código que não precisariam ter mexido.

06:57

Então, quando você vai trabalhar com guidelines e você tem uma forma muito clara de utilizar a inteligência artificial, você evita esses tipos de ruído. Afinal de contas, imagina que você pede para alguém do seu time desenvolver uma feature e, de repente, ele traz 100 arquivos modificados porque a IA refatorou. E aí, como você vai revisar isso? Então, esse aí é o grande problema.

07:20

em relação à parte de ruídos, tá? Uma outra coisa importante aqui é agente especializado trabalhando em paralelo. Uma das coisas mais comuns agora é você ter um agente especializado em front-end, back-end, um agente especializado em Java, um agente especializado em PHP, em .NET,

07:40

E o que acontece? Muitas vezes esses agentes também não têm especialização apenas em movimento. Às vezes esse agente tem especializações em melhorar o processo de CICD e tudo mais. Então, quando a gente vai fazer isso, o que acontece? Esses agentes já têm, não digo um pré-treinamento, mas já têm um prompt dele.

08:02

E, às vezes, esse prompt desse agente não vai levar em conta as guidelines daquele projeto em específico, porque daqui pra frente o que mais vai começar a ter? Agentes especializados em domínios especializados, tá? Mas não é porque eu tenho um agente especializado em Java que esse agente vai ditar como o meu projeto em Java vai ser desenvolvido, porque quem vai ditar isso vai ser

08:27

Eu, pelas minhas guidelines. Então, a gente tem que dar um jeito de fazer com que essas guidelines, elas, entre aspas, substituam alguns comportamentos de agentes que podem ser rodados em diversas formas, em paralelo ali no seu código, pra garantir que você não vai ter essa bagunça de padrões e tudo mais, tá?

08:47

Outra coisa, Code Review automático. Então, se a gente tem guidelines muito claras na hora dos agentes que vão fazer o processo de Code Review, vai ficar muito mais fácil. Eles olham as guidelines e veem se tem alguma coisa que não está batendo com aquela guideline baseada naquele comite. E aí, também, a gente tem um outro ponto, que é a maximização com a previsibilidade de ambientes multimodais. O que é isso? Hoje em dia, os nossos modelos, obviamente, o que eles fazem? Eles conseguem

09:15

ler imagens, ele tem a parte de texto, tem a parte de vídeo, tem um monte de coisa que os agentes hoje em dia conseguem fazer, os modelos conseguem fazer. E, eventualmente, quando nós temos guidelines claros, a gente pode falar naquele guideline que essa parte aqui vai utilizar um processo ou uma parte que vai ter que ser focada ali naquele diagrama C4.

09:43

Entende? Então, ou naquele determinado front-end, ou naquele determinado design. Então, os agentes agora, através daqueles guidelines, eles podem ter acesso a imagens, eles podem ter acesso a outros tipos de mídia que vão fazer e vão facilitar a utilização de todo esse processo. Eventualmente eu tenho um cara muito mais focado em front-end que vai ter que ler, por exemplo, guidelines de como desenvolver

10:11

uma interface, mas eu tenho toda a documentação pronta de como isso deve funcionar. Eu tenho exemplos e imagens, eu tenho diagramas e etc. Então, acaba facilitando bastante aí. Então, assim, são infinitas as possibilidades de como que esses tipos de guidelines vão... nos ajudam, tá? E no próximo vídeo eu quero trazer aqui pra vocês as principais seções que isso aí pode...

10:38

como que eu posso dizer, inspirar para que você leve em consideração se vale a pena ter isso no seu projeto.

## Resumo IA

**Abreviações**  
- IA — Inteligência Artificial  
- CI/CD — Integração Contínua e Entrega Contínua  
- C4 — Modelo C4 de documentação/diagramas de arquitetura  
- Code Review — Revisão de código  
- Pull Request — Solicitação de pull request (pedido de incorporação de alterações em um repositório)  
- Pre-commit — Verificação executada antes do commit  

**Resumo**  
A aula apresenta o conceito de Software Development Guidelines como um conjunto de regras e boas práticas que orientam como o software deve ser escrito, organizado e evoluído em um time ou empresa. O instrutor destaca que essas diretrizes podem existir como um ou vários documentos, dependendo do domínio do projeto e da governança da organização, e que seu escopo vai além de estilo de código, abrangendo linguagem, framework, padrões de implementação e o fluxo completo de desenvolvimento.  

No contexto de Design Docs, as guidelines ganham importância por facilitarem o onboarding automático de IA, funcionando como uma base de conhecimento para que o agente compreenda como o time programa, como o ambiente é configurado, como desenvolver e como executar testes. Também ajudam a reduzir divergências e aumentar a consistência quando a IA cria módulos ou features novas sem orientação clara, evitando variações indesejadas de padrões entre arquivos e funcionalidades.  

Outro benefício abordado é a redução de erros e retrabalho, já que guidelines bem definidas permitem inclusive a criação de verificações automatizadas, como hooks de pre-commit, para checar conformidade com as regras estabelecidas. O instrutor também enfatiza o problema dos ruídos em revisões: quando a IA altera arquivos fora do escopo da feature, o code review fica mais difícil, pois mudanças irrelevantes aumentam o volume de arquivos a analisar e podem misturar assuntos distintos em um mesmo commit.  

A aula ainda destaca o uso de agentes especializados trabalhando em paralelo, como agentes de front-end, back-end, Java, PHP, .NET ou até de CI/CD, e explica que esses agentes devem ser subordinados às guidelines do projeto, e não o contrário, para evitar inconsistência de padrões. Por fim, é citado o code review automático, que fica mais eficiente quando os agentes conseguem comparar commits com diretrizes claras, e a previsibilidade em ambientes multimodais, nos quais modelos e agentes processam texto, imagens, vídeo e diagramas — como C4 ou materiais de front-end — com apoio de documentação, exemplos e mídia visual.  

**Pontos de atenção**  
- Guidelines não devem tratar apenas de estilo de código; devem cobrir o processo de desenvolvimento como um todo.  
- É possível e até desejável ter múltiplos documentos de guidelines, segmentados por domínio ou área do projeto.  
- Diretrizes claras ajudam a IA a seguir o padrão do time e facilitam o onboarding automático.  
- Sem guidelines, a IA tende a gerar inconsistências em nomenclatura, comentários, estrutura e arquitetura do código.  
- Guidelines reduzem erros e retrabalho, mas não garantem perfeição; a melhoria é probabilística.  
- Verificações automáticas, como hooks de pre-commit, são boas práticas para validar aderência às diretrizes.  
- Ruído em revisões é um problema crítico: mudanças fora do escopo aumentam drasticamente o esforço de code review.  
- Evitar que a IA “refatore demais” ou altere arquivos não relacionados é essencial para manter commits e PRs limpos.  
- Agentes especializados em paralelo devem obedecer às guidelines do projeto, não impor seus próprios padrões.  
- Code review automático se torna mais eficiente quando pode comparar mudanças com regras explícitas do projeto.  
- Em contextos multimodais, guidelines podem e devem indicar uso de diagramas, imagens, vídeos e exemplos para orientar a implementação.