Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17776)

## Resumo da aula

mixed

O PRD, já definido anteriormente como a base do produto, não é suficiente para implementar uma feature com segurança técnica. O Spec Writer deriva desse PRD dois artefatos por feature: uma especificação técnica detalhada e um plano de desenvolvimento. Essa separação reduz ambiguidade porque o spec.md descreve a solução técnica com profundidade, enquanto o plan.md organiza a execução em fases e passos. O resultado é um caminho intermediário entre requisito de produto e implementação.

No modo single feature, a skill gera dois arquivos dentro de docs, organizados pelo ID e nome da feature. O spec.md concentra decisões técnicas, como esquemas, índices, migrações, contratos de API, componentes e testes. O plan.md mantém uma visão de alto nível, com pré-requisitos, fases, passos numerados e decisões de execução. Essa divisão evita misturar arquitetura detalhada com checklist operacional.

O Spec Writer depende do PRD para ler o ID da feature, seu escopo, critérios de aceitação, fluxos de erro e relações de consumo e provisão entre features. Como essas conexões já foram mapeadas no PRD, a skill não parte do zero: ela herda a estrutura funcional e transforma isso em instruções técnicas acionáveis. Sem esse documento, a geração perde contexto de integração e tende a produzir especificações isoladas. Por isso, o PRD não é opcional nesse fluxo.

Retomando o grafo de dependências já definido no PRD, a skill verifica quais features dependem de outras antes de gerar a especificação. Em projetos Greenfield, isso é decisivo porque certas capacidades precisam existir primeiro como foundation features, formando a base mínima do sistema. A skill distingue cenários de fundação inexistente, parcial ou completa para evitar planejar uma feature sobre infraestrutura ausente. Isso impede, por exemplo, especificar fluxos avançados antes de autenticação, persistência ou estrutura básica estarem prontas.

A exploração da codebase é separada em dois níveis para evitar análises superficiais ou desorganizadas. A primeira camada identifica a fundação observável do sistema: linguagem, framework, banco de dados, ORM, autenticação, estratégia de API, testes, exceções e estrutura de pastas. A segunda camada amplia a leitura para padrões globais de implementação, decisões arquiteturais, convenções de nomes e abstrações recorrentes. Quando a codebase está vazia, a skill procura sinais mínimos, como scaffolding ou package.json, e ajusta a análise a essa ausência de código real.

Depois de ler PRD e codebase, a skill entra em uma entrevista técnica semelhante à clarificação já usada no PRD, mas com foco arquitetural. As perguntas não repetem decisões de produto; elas exploram organização do sistema, escolhas técnicas e detalhes necessários para estruturar a implementação. Isso força a especificação a capturar decisões que normalmente ficariam implícitas na cabeça do desenvolvedor. O ganho principal é transformar contexto tácito em documentação reutilizável por agentes e por humanos.

A skill classifica a feature como trivial, simples, média ou complexa e usa essa classificação para calibrar a quantidade de fases, steps e nível de detalhe. Features triviais tendem a exigir poucas fases e pouca profundidade; features complexas recebem mais fases, mais steps e uma especificação mais extensa. Essa heurística foi definida de forma prática, com base na experiência do autor, e não como regra universal. Ainda assim, ela resolve um problema real: evitar tanto documentação excessiva para mudanças pequenas quanto documentação rasa para mudanças estruturais.

O spec.md aprofunda a solução técnica em seções como overview, arquitetura, decisões, componentes, contratos de API, data model e processo de testes. A presença dessas seções força a feature a ser descrita como parte do sistema, não como tarefa isolada. Quando a feature é cross-cutting, a especificação também precisa deixar explícito onde ela toca outras partes da aplicação. Isso é o que permite gerar implementação com contexto de integração, e não apenas código local.

O plan.md traduz a especificação em execução incremental. Ele organiza pré-requisitos, fases e passos numerados, com uma descrição curta do que precisa ser feito em cada etapa. Em vez de repetir detalhes profundos do spec.md, o plano funciona como roteiro operacional para implementação. Essa separação é útil porque agentes diferentes podem consumir o plano para executar e o spec para decidir como executar.

Retomando o problema de integração entre features visto antes, a especificação precisa prever o ponto de acoplamento futuro. Se a autenticação precisa redirecionar para o dashboard, esse vínculo já deve aparecer como algo que a feature provê ou consome, inclusive com testes preparados para essa conexão. A tabela de correlação entre critérios de aceitação e testes técnicos ajuda a transformar requisitos em validações executáveis. Assim, a feature nasce pronta para se encaixar no restante do sistema, em vez de virar um bloco isolado.

## Transcrição

00:01

Bom, pessoal, com esse PRD gerado, a partir dele a gente tem que derivar o quê?

00:07

Aquilo exatamente que eu passei para vocês logo aqui no início.

00:11

Nós precisamos de algo que gere uma especificação técnica para

00:16

cada fase e um plano de desenvolvimento para cada fase.

00:19

Eu tenho uma outra skill chamada Spec Writer.

00:23

Para que a gente não fique aqui de uma forma extremamente só maçante,

00:27

eu vou iniciar o processo.

00:31

do desenvolvimento, como que eu posso dizer, da geração dessa feature,

00:38

tá? Da primeira feature, para que a gente possa, então,

00:42

entender como que é feita essa

00:46

skill para fazer a geração dessa documentação,

00:50

porque a partir dali a gente consegue fazer o

00:52

desenvolvimento e fazer a implementação e etc,

00:55

tá? Então, basicamente,

00:58

o que eu vou fazer aqui vai ser o seguinte.

01:01

Eu vou pegar essa skill chamada Spec Writer,

01:06

depois a gente vai olhar ela com mais calma.

01:09

Eu não quero entrar no nível de profundidade que eu dei para o PRD,

01:12

porque o PRD é o documento mais importante nesse nosso caso.

01:17

Mas essa skill aqui, especificamente,

01:21

o que ela acaba trazendo?

01:25

aqui pra gente de, vamos dizer, de importante, tá?

01:29

Basicamente, ela vai gerar uma especificação técnica no formato,

01:35

nesse caso,

01:36

de single feature. Eu vou falar apenas de single feature por agora,

01:40

depois a gente vai falar em batch mode, tá? Mas, basicamente,

01:44

ele vai gerar dois arquivos, tá? Ele vai usar esse padrão,

01:48

vai jogar dentro de barra docs, com o nome da feature.

01:51

Com o ID da feature, com o nome da feature,

01:53

com um arquivo chamado spec.md e outro como plan.md.

01:57

Basicamente isso. E ele tem seis passos para execução.

02:02

Primeiro ponto é analisar o PRD. Ou seja,

02:06

ele vai carregar, ele vai precisar analisar o PRD.

02:09

Ou seja, o PRD é obrigatório aqui para a gente.

02:13

Depois disso, o que ele precisa fazer?

02:17

Verificar dependências. Por quê?

02:20

Como uma feature tem uma dependência da outra,

02:23

ele vai verificar o gráfico de dependências do PRD

02:27

para conseguir entender o que cada feature consome da outra.

02:32

E aí, baseado nisso, ele vai verificar, por exemplo,

02:36

se for um projeto Greenfield, por exemplo,

02:38

o que tem por trás do projeto. Ou seja,

02:44

qual é a tecnologia? Qual é o framework?

02:47

Baseado nisso, ele consegue fazer o quê? Ele consegue falar, ok,

02:52

esse projeto é um projeto Greenfield, que vai começar do zero,

02:56

então como ele vai começar do zero,

02:58

eu preciso ter algumas features que são foundation features, ou seja,

03:02

eu não posso criar nada antes dessas features,

03:05

porque se eu fizer isso, não dá para trabalhar,

03:09

porque eu preciso de uma foundation, eu preciso de uma base ali no meu sistema.

03:13

Então, isso aí é importantíssimo. Então,

03:17

ele vai detectar se o meu projeto é Greenfield,

03:19

ele vai ver se tem uma fundação parcial ou se ele já tem uma fundação completa,

03:25

que a partir dali ele já pode sair criando um monte de casos. E aqui tem os cenários.

03:29

Se for Greenfield e tiver uma foundation, então, basicamente,

03:33

são algumas verificações, basicamente, é um monte de IFPs.

03:39

E aqui o batch mode é quando eu quero fazer

03:41

a geração de várias features ao mesmo tempo. O que acontece?

03:46

Nesse aspecto aqui, eu fiz uma separação importante,

03:50

que é o code base pattern discover.

03:53

Normalmente, a gente tende a pedir para o agente explorar o nosso code base.

03:58

E ele faz isso já naturalmente.

04:00

Mas eu quero que ele faça essa exploração em duas etapas,

04:05

em duas camadas. A primeira camada... Ou seja,

04:09

é a fundação. Ou seja,

04:11

extrair o mínimo observável de padrões em determinadas categorias do sistema.

04:17

Ou seja, qual a linguagem, qual o framework, qual o banco de dados, qual o RM,

04:23

qual a estratégia de autenticação, qual a estratégia de API,

04:26

como que é o framework de teste,

04:28

como que ele trabalha com as exceções,

04:30

qual que é a estrutura de pastas. Então, basicamente,

04:33

ele fala, é o chão, não é o teto que ele vai olhar.

04:37

Essa exploração inicial, nessa primeira camada,

04:41

vai fazer com que ele entenda a base do sistema.

04:44

E a segunda exploração é Broad Exploration, ou seja...

04:48

Ele precisa agora olhar o projeto como um todo e entender os padrões do projeto,

04:54

as decisões arquiteturais, a forma de como o projeto é escrito,

05:01

como estão criados os nomes das variáveis, as abstrações e tudo mais. Então,

05:06

ele faz uma verificação fundacional e ele faz uma verificação,

05:11

de forma geral, mais ampla agora em nível de implementação.

05:19

E aqui tem caso, no caso,

05:21

se tiver um code base vazio, ele vai buscar, por exemplo,

05:26

se tem um scaffolding, sei lá, um package.json e etc.

05:31

Então, ele vai dar um skip nesses layers ali.

05:35

Ignorando por hora o batch mode.

05:37

E agora, o que eu peço para ele fazer?

05:40

Ler o PRD e entender a feature com ID,

05:45

verificar se ele tem...

05:47

Se essa feature consome algo de outra feature e

05:50

se essa feature provê algo para outra feature.

05:54

Entender qual que é o core scope block, ou seja,

05:58

a parte base do escopo da aplicação e os outros escopos da aplicação que

06:05

são o que vão grudando as features adicionais que vão sendo adicionadas no sistema.

06:10

O que cada feature faz, a experiência,

06:12

o processo de erro e também os critérios de aceitação de cada feature,

06:18

e os critérios de integração de uma feature e outra.

06:21

É isso que eu estou pedindo para ele ler do meu PRD.

06:23

E aí, ele vai trazer para a gente,

06:27

baseado nessa análise do usuário, eu entendi isso aqui. Então,

06:31

esse passo é para ele entender de uma forma minuciosa o código.

06:37

os padrões que a gente tem,

06:39

e o PRD com as features que a feature que ele vai desenvolver.

06:44

E aí a gente cai. na entrevista de novo, tá? E o que que acontece?

06:51

Eu tô colocando aqui batch mode,

06:53

eu vou falar depois pra vocês quando a gente

06:54

chegar na fase de programar de forma paralela,

06:56

tá? Mas basicamente,

06:58

eu peguei também a adaptação do prompt do Grilled Me,

07:03

que é uma skill bem legal que é feita,

07:06

e novamente ele vai fazer o quê? Ele vai fazer agora perguntas técnicas.

07:11

Da mesma forma...

07:12

Como no PRD nós tivemos interações com perguntas extremamente de produto,

07:18

principalmente de comportamento,

07:20

aqui ele vai fazer perguntas explorando tecnicamente.

07:26

E quando você for fazer a sua prova de conceito e utilizar,

07:29

eu recomendo que você vá fazer isso depois,

07:31

um projeto especificamente com essa skill para você sentir.

07:36

Você vai ver o nível de exploração, o nível de detalhe,

07:39

o nível de discussão que você chega para

07:42

que a estrutura do projeto esteja ali criada. Então,

07:48

aqui tem as regras de como ele vai perguntar, entender cada aspecto de arquitetural,

07:55

de organização,

07:57

e ele vai começar primeiro perguntando de escopos principais e depois as adições.

08:04

Não seja redundante o que tem no PRD,

08:06

você não vai perguntar de novo. Foque na entrevista.

08:09

E aqui ele vai trazer o resultado de tudo que ele entendeu baseado naquilo.

08:16

E com isso ele vai gerar dois documentos.

08:19

E esses documentos vão ser baseados em um nível de complexidade.

08:26

Ou seja, se for apenas umas duas fases de desenvolvimento, ele vai ser algo trivial.

08:32

Se for simples, vai ser de duas a três fases com cinco a oito steps.

08:37

Se for uma complexidade média,

08:39

vai ser de dez a quinze, com três fases. E complexo,

08:44

com quatro a cinco fases, com quinze a vinte e cinco steps.

08:47

Que steps são esses? O nosso plano de implementação vai ter o quê?

08:52

Fase um, quais são os passos para terminar a fase um?

08:55

Fase dois, quais são os passos? Então,

08:58

esses passos são os passos que ficam dentro de cada fase.

09:02

E no spec, ele vai trazer informações profundas, desde esquemas,

09:07

índices, migrações, pontos de escala. E o plano,

09:11

ele traz apenas a visão alto nível do que vai ser feito. Então, para especificação,

09:17

ele vai analisar o nível de complexidade e vai colocar,

09:21

falando sempre, se essa feature é uma cross -cutting,

09:25

ou seja, se ela é integrada com outras features ali também. Então, a ideia é que...

09:31

Eu tenho o PRD, que faz o mapeamento, e aí eu tenho o que consome, o que provê,

09:36

se isso está incluso no escopo principal do projeto ou se

09:41

está nas features adicionais que vão ser feitas em outras etapas.

09:46

Isso é importante, porque quando eu gero a minha especificação, eu tenho que falar,

09:51

eu vou fazer aqui até a autenticação, mas eu sei que para a autenticação...

09:59

funcionar, ela vai ter que redirecionar para o dashboard.

10:02

Então, eu já vou deixar prover um teste, por exemplo,

10:06

Para que o dashboard já seja integrado e que a

10:10

outra feature já consiga fazer o grude de toda essa história.

10:14

Então, ele traz os detalhes, ou seja,

10:17

eu provei, ele vai trazer isso. Então,

10:19

ele fez uma tabela de correlação até os testes

10:23

ali de critérios de aceitação que vão virar testes.

10:28

De técnicos mesmo que vão ter que ser executados. Ou seja, baseado nisso,

10:32

eu vou ter quais são os testes que

10:34

são necessários para fazer aquela funcionalidade trabalhar.

10:37

E para gerar o plano, basicamente,

10:39

é uma sentença com um pequeno parágrafo falando o que vai ter que ser feito.

10:44

E o plano e tudo mais,

10:46

eles estão para ele ler nessa referência Feature Template aqui para a gente.

10:51

Ele vai validar e depois vai salvar aqui para a gente.

10:55

Não quero falar de batch mode aqui.

10:57

Aqui está a referência só para você ver do nosso template.

11:00

Então, aqui eu tenho dois templates. Um do spec.md e o plan.md.

11:06

Deixa eu só colocar aqui para ficar mais fácil para a gente ver.

11:09

E aqui eu tenho como que eu detecto o nível de complexidade.

11:14

Lembra que eu falei para vocês que ele verifica a complexidade?

11:17

Então, aqui está, trivial.

11:19

Só tem um componente, não tem a mudança na API,

11:22

não tem a mudança no banco de dados, não tem integração.

11:25

Simples, tem poucos componentes. Tudo isso aqui que está dessa forma foi arbitrário.

11:29

Eu tirei da minha cabeça do que eu acho,

11:31

baseado nos projetos que eu trabalho,

11:33

do que eu acho que uma feature é complexa, simples, média e etc.

11:39

E aí, basicamente,

11:41

eu detalho como que o plano vai detalhar um nível.

11:48

De explicação de cada feature baseado em quantidade de parágrafos.

11:52

Porque quanto mais complexo,

11:54

eu preciso de mais detalhes, preciso de mais contexto.

11:57

Então, ele vai ter sessão de overview, arquitetura,

12:00

as decisões, os componentes, os contratos de API,

12:03

o data model e o processo de teste. Então,

12:06

essas são as sessões que eu vou ter ali na hora de gerar minha especificação.

12:10

E para high level, para o documento de planejamento, ele vai ter technical overview,

12:16

o impacto de arquitetura, vai trazer o que é certo, o que é errado,

12:21

o que é esperado, e um diagrama de como que ele pode gerar,

12:25

por exemplo, numa aplicação, porque cada feature tem o seu próprio diagrama,

12:29

aqui é um exemplo de diagrama,

12:30

e aqui basicamente, galera, é o template de como que funciona, tá?

12:34

Como que eu imagino o output da minha especificação aqui pra gente,

12:41

tá? E aqui é a estrutura do documento do plano, ou seja,

12:44

o nome do plano, os pré-requisitos, e passo 1,

12:47

numerado, passo 2, com as decisões.

12:51

Eu não quero chegar aqui nesses níveis de detalhes,

12:54

mas o grande ponto aqui é que essa skill tem o objetivo de gerar dois documentos,

13:00

e esses dois documentos passam novamente pelaquela

13:03

entrevista que eu falei ali para vocês.

13:07

Então, no próximo vídeo, eu vou executar essa skill, vou mostrar o início dela.

13:13

E vou fazer igual eu fiz no PRD,

13:14

Porque senão a gente vai ficar até amanhã aqui especificando,

13:18

E o nosso objetivo é mostrar na realidade tudo isso aí funcionando.

## Resumo IA

**Abreviações**

*   **API**: Application Programming Interface
*   **ID**: Identifier
*   **ORM**: Object-Relational Mapping
*   **PRD**: Product Requirements Document
*   **plan.md**: Arquivo Markdown de Plano de Desenvolvimento
*   **spec.md**: Arquivo Markdown de Especificação Técnica Detalhada

**Resumo**

O objetivo desta aula é detalhar o funcionamento da skill "Spec Writer", que é responsável por derivar especificações técnicas e planos de desenvolvimento a partir de um PRD (Product Requirements Document) já existente. Essa separação em dois artefatos principais – `spec.md` e `plan.md` – visa reduzir ambiguidades e fornecer um caminho intermediário claro entre o requisito de produto e a implementação técnica.

A skill "Spec Writer" opera em um fluxo de seis passos, no modo de "single feature" (foco em uma única funcionalidade por vez), gerando os arquivos `spec.md` e `plan.md` dentro de uma pasta organizada pelo ID e nome da feature em `/docs`.

O fluxo explicado pelo instrutor consiste em:

1.  **Análise do PRD**: A skill lê o PRD para extrair informações cruciais como o ID da feature, seu escopo, critérios de aceitação, fluxos de erro e, fundamentalmente, as relações de consumo e provisão entre features. O PRD é um documento obrigatório para contextualizar a geração.
2.  **Verificação de Dependências**: Utiliza o grafo de dependências do PRD para entender quais features dependem de outras. Em projetos Greenfield (novos projetos do zero), isso é vital para identificar "foundation features" (funcionalidades base) que precisam existir antes de qualquer outra coisa, evitando o planejamento sobre infraestrutura ausente. A skill distingue cenários de fundação inexistente, parcial ou completa.
3.  **Exploração da Codebase**: Realizada em duas camadas. A primeira camada (fundacional) identifica a base observável do sistema (linguagem, framework, banco de dados, ORM, autenticação, estratégia de API, testes, exceções e estrutura de pastas). A segunda camada (ampla) explora padrões globais de implementação, decisões arquiteturais, convenções de nomes e abstrações recorrentes. Em codebases vazias, a skill busca sinais mínimos como scaffolding ou `package.json`.
4.  **Entrevista Técnica**: Uma fase de clarificação focada em aspectos arquiteturais. As perguntas exploram a organização do sistema, escolhas técnicas e detalhes necessários para estruturar a implementação, sem repetir decisões já contidas no PRD. O objetivo é transformar contexto tácito em documentação explícita e reutilizável.
5.  **Classificação da Complexidade da Feature**: A skill classifica a feature como trivial, simples, média ou complexa. Essa classificação é usada para calibrar a quantidade de fases, passos e o nível de detalhe dos documentos gerados, garantindo uma documentação adequada ao tamanho da mudança.
6.  **Geração dos Documentos**:
    *   `spec.md`: Aprofunda a solução técnica em seções como overview, arquitetura, decisões, componentes, contratos de API, data model e processo de testes. Descreve a feature como parte do sistema, incluindo aspectos "cross-cutting" e integração.
    *   `plan.md`: Apresenta um roteiro operacional de alto nível, com pré-requisitos, fases e passos numerados, descrevendo sucintamente o que precisa ser feito em cada etapa. Ele não repete os detalhes profundos do `spec.md`, servindo como guia de execução.

A especificação também prevê pontos de acoplamento futuros e garante que a feature nasça pronta para se integrar ao restante do sistema, correlacionando critérios de aceitação com testes técnicos executáveis.

**Pontos de atenção**

*   **PRD como Fundamento Indispensável**: O PRD é a base obrigatória para o `Spec Writer`. Sem ele, a skill perde contexto de integração e tende a produzir especificações isoladas e tecnicamente inseguras.
*   **Clara Separação de Documentos**: A divisão entre `spec.md` (solução técnica detalhada) e `plan.md` (roteiro operacional de alto nível) é crucial. Misturar arquitetura detalhada com um checklist operacional pode gerar ambiguidade e dificultar o consumo por diferentes agentes ou desenvolvedores.
*   **Validação de Dependências para Fundação**: Em projetos Greenfield, a verificação das dependências de features é decisiva. É uma boa prática garantir que as "foundation features" (base mínima do sistema) existam antes de planejar funcionalidades avançadas, evitando a construção sobre infraestrutura ausente.
*   **Análise Profunda da Codebase**: A exploração da codebase em duas camadas (fundacional e global) é vital para evitar análises superficiais e garantir que os padrões de implementação e decisões arquiteturais sejam compreendidos antes da especificação.
*   **Entrevista Técnica Focada em Arquitetura**: A fase de entrevista técnica deve ser cuidadosamente focada em detalhes arquiteturais e organizacionais do sistema, sem redundância com o PRD. Isso transforma conhecimento tácito do desenvolvedor em documentação explícita e reutilizável.
*   **Calibragem do Nível de Detalhe**: É uma boa prática classificar a complexidade da feature (trivial, simples, média, complexa) para calibrar a profundidade da especificação e do plano. Isso evita documentação excessiva para pequenas mudanças e escassa para mudanças estruturais.
*   **Integração Explícita e Previsão de Acoplamento**: A especificação deve explicitamente prever e documentar os pontos de acoplamento futuros entre features. Incluir testes preparados para essas conexões garante que a funcionalidade seja desenvolvida com o contexto de integração em mente, e não como um bloco isolado.
*   **Heurística de Complexidade**: A classificação de complexidade é arbitrária e baseada na experiência, mas é uma solução prática para dimensionar adequadamente a documentação.