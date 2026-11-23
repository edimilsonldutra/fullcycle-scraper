Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17227)

## Resumo da aula

O vídeo anterior ficou meio longo, mas é importante que consigamos entender e explorar as possibilidades, compreender o que está por trás e as vantagens de termos documentos desse tipo, ainda mais documentos extremamente especializados como estes.

Agora, o que normalmente encontramos em guidelines quando definimos a forma como o software será desenvolvido? Toda vez que pensamos em guidelines, precisamos considerar as convenções de código: como será desenvolvido, se usaremos tabs ou quatro espaços no Python, como nomear variáveis, como comentar o código. Tudo isso faz parte das guidelines.

A estrutura do projeto também pode ser incluída, embora às vezes seja mantida em documentos arquiteturais. Mas se quisermos destacar algo específico, podemos trazer mais detalhes, falar sobre padrões arquiteturais e linkar para documentos externos. Segurança, testes, commits, Git, pull requests, performance, observabilidade — tudo isso pode estar nas guidelines.

É importante saber que, dependendo do projeto, você não precisa ter tudo isso. Em alguns casos, vale a pena ter muito mais. Vou trazer algumas seções de um template e mostrar o prompt de como isso funciona, para que vocês tenham um ponto de partida para criar guidelines nos seus projetos.

São muitas seções, não vou explicar cada uma profundamente, mas é importante que vocês tenham clareza das possibilidades. Algumas seções podem ser opcionais, outras obrigatórias, e vocês podem incluir outras.

Começamos com Core Principles: princípios claros que não devem ser quebrados durante o desenvolvimento. Dependendo do projeto, os princípios podem variar.

Depois, Setup e Inicialização: uma das coisas que a IA mais precisa saber é como subir e descer o ambiente, rodar scripts, fazer migrações, etc.

Estrutura do Projeto: como está organizado, uso de containers, Dockerfile, Docker Compose.

Convenções de Código: nomenclatura, tipagem, funções, métodos, tratamento de erros, concorrência e paralelismo, abstrações e interfaces.

Testes: testes de unidade, mocks, testabilidade, testes de integração, estresse, carga.

Profiling e Diagnósticos: como verificar se o software está se comportando como esperado, rodar benchmarks, otimizações.

Segurança: pontos críticos a serem considerados.

Padrões de Código: o que deve e o que não deve ser feito. Quando trabalhamos com IA, dar exemplos do que é bom e do que é ruim ajuda muito a dar clareza ao modelo.

Gerenciamento de Dependências: como lidar com pacotes, gerenciadores, etc.

Comentários e Documentação: como a IA deve comentar e documentar, e onde encontrar outras partes da documentação do software para fazer linkagem.

Banco de Dados: diretrizes para modelagem, consultas, etc.

Logs e Observabilidade: como estruturar logs, métricas, tracing.

Por fim, as Golden Rules — regras de ouro que amarram tudo o que foi dito. Com base nelas, podemos ter uma checklist pré-commit. Na hora de desenvolver, a IA pode seguir essa checklist para garantir que está mantendo a integridade do sistema e seguindo as convenções.

E as Referências: links externos e internos que ajudam durante todo o processo.

Essas são algumas das seções. Vamos olhar com mais calma daqui para frente, para vermos na prática como tudo isso pode ser gerado.

## Transcrição

00:00

Bom, pessoal, o vídeo anterior ficou meio longo, mas é importante que a gente consiga entender e explorar as possibilidades e entender o que está por trás, as vantagens de realmente a gente ter documentos desse tipo, ainda mais documentos extremamente especializados como esses aqui, tá? Agora, o que normalmente a gente tem em guidelines quando a gente vai editar a forma de como o nosso software vai ser desenvolvido, tá? Então, normalmente,

00:27

Toda vez que a gente vai pensar em guidelines, a gente tem que pensar o seguinte... Como que eu vou gerar minhas convenções de código? Como que vai ser desenvolvido? Vão ser um tab no Python ou quatro espaços? Eu vou utilizar...

00:43

qual forma de trabalhar com as variáveis, como que eu vou comentar o meu código. Então, tudo isso acaba, de forma geral, incluindo, fazendo parte dessas guidelines. Como que vai ser a estrutura do meu projeto? Eventualmente, as passas de como que isso pode ser organizado. Não necessariamente isso tem que ter nas guidelines, mas, eventualmente, você pode ter. Às vezes, a gente quer manter essa estrutura mais na parte arquitetural, mas, eventualmente, se eu quero

01:09

ressaltar alguma coisa dentro daquela estrutura, eu posso trazer mais detalhes. Eu posso falar quais são os padrões arquiteturais e posso colocar de forma geral como isso pode ser feito, posso linkar isso para...

01:23

um documento externo, como que eu vou trabalhar com segurança, como que eu vou fazer testes, como que eu vou fazer a parte de commit, git, pull requests, como que vai ser a parte de performance, observabilidade. Então, essas guidelines, elas podem ter tudo isso e mais um pouco. E também é importante você saber que

01:41

Dependendo do projeto, você não precisa ter tudo isso. Dependendo do projeto, vale a pena você ter muito mais coisa, tá? Então, eu vou trazer aqui algumas sessões de um template, e eu vou mostrar pra vocês daqui a pouco esse template, o prompt de como que isso funciona, pra que você consiga ter um pouco mais de clareza e ter um ponto de partida pra você começar a criar as guidelines aí nos seus projetos, tá? Então, vamos lá.

02:07

São bastante sessões, eu não vou ficar, obviamente, explicando profundamente cada uma delas, mas é importante que você consiga...

02:18

que é uma clareza das possibilidades que você tem, e aí, eventualmente, tem sessões que podem ser opcionais, outras sessões, na sua opinião, podem ser obrigatórias, e também algumas outras sessões você pode incluir, tá? Então, core principles, ou seja, você pode trazer princípios muito claros que não devem nunca ser quebrados na hora que você tá fazendo o seu desenvolvimento, tá? Então, assim,

02:39

Não tem como a gente negar que o software tem que trabalhar de um jeito, isso tem que funcionar dessa forma, ou seja, dependendo de como cada projeto funciona, eu posso ter princípios diferentes. A gente vai ver isso um pouquinho mais daqui pra frente. Outra coisa, como é que eu inicializo o meu projeto? Ou seja, uma das coisas que a IA mais precisa saber, como é que eu subo, como é que eu desço o ambiente?

03:01

Como é que eu rodo os meus scripts? Como é que eu faço as minhas migrações? Como é que funciona tudo isso? Outra coisa, como é que funciona a estrutura do meu projeto? Eu vou trabalhar com container? Como é que funciona o meu container? Como é que funciona o meu Dockerfile? Como é que funciona o meu Docker Composer? Como é que eu vou trabalhar com convenções de nome? Como é que eu vou tipar as coisas? Como é que vai ser o processo de tipagens? Como é que eu vou trabalhar com as funções, com os métodos? Como é que eu vou tratar erro? Como é que eu vou trabalhar com concorrência e paralelismo?

03:28

como que eu vou trabalhar com abstrações e interfaces, como que eu vou fazer testes de unidade, como é que eu vou fazer a parte de mocs, a parte de testabilidade, como é que eu vou trabalhar com testes de integração, como é que eu vou fazer testes de estresse, testes de carga, como que eu vou fazer a parte de profiling e diagnósticos do meu software pra ver se

03:47

ele realmente está se comportando da forma como eu gostaria, como que eu consigo rodar benchmarks, como que eu posso dizer ali, como que eu devo otimizar o meu software, quais são os pontos de segurança que eu tenho que levar em consideração, quais são padrões de código. E quando eu falo padrões de código, pode ser o que deve ser feito, o que não pode ser feito. Quando a gente está trabalhando muito com o IA,

04:09

Sempre dar exemplos do que pode, do que não pode, o que é ruim, o que é bom, ajuda muito pra dar mais clareza ali pro modelo, tá? Outro ponto importante é como é que eu trabalho com dependências, né? Ah, eu tô trabalhando com o gol, como é que eu vou trabalhar com as minhas dependências? Ah, eu tô trabalhando com...

04:28

JavaScript, como é que eu vou utilizar as minhas dependências? Então, tem diversas formas de a gente olhar pra isso, né? Desde pacotes, gerenciadores e tudo mais. Comentários de documentação. Isso aí é muito importante. Como que a IA, ela comenta, como ela documenta, mas também onde estão outras partes da documentação do nosso software que ela pode utilizar pra fazer toda essa linkagem, tá? Como é que funciona a parte de banco de dados? Como é que funciona a parte de log e observabilidade? E aí,

04:57

Existem algo que eu gosto de chamar de Golden Rules. O que são Golden Rules? São regras de ouro. Por quê? Essas regras vão, de forma geral, amarrar

05:08

tudo o que a gente acabou de falar ali acima. E, baseado nisso, eu consigo ter o quê? Uma checklist antes de eu comitar qualquer coisa. Então, na hora que eu estou pedindo para ela desenvolver e eu falo, olha, sempre faça essas verificações, etc., olhe a minha checklist antes de comitar, sempre siga um pre-commit checklist. Ele vai poder olhar

05:31

o modelo, o nosso agente, e ele vai fazer o seguinte, eu vou fazer todas essas verificações antes de fazer um comite para garantir que eu estou mantendo a integridade ali do meu sistema e estou seguindo as convenções. E outra parte que é importante, referências, essa parte de referências, ela pode fazer referências externas, referências entre o próprio projeto, para que você consiga

05:57

ter realmente documentos, links tangíveis que vão te ajudar durante todo esse processo, tá? Então, aqui são algumas dessas sessões, a gente vai olhar isso com mais calma agora, daqui pra frente, pra que a gente veja na prática como é que tudo isso pode ser gerado. Então, vamos nessa!

## Resumo IA

**Abreviações**
- IA — Inteligência Artificial
- Git — sistema de controle de versão distribuído
- PR — Pull Request
- Docker — plataforma de containers
- Dockerfile — arquivo de instruções para construção de uma imagem Docker
- Docker Compose — ferramenta para definir e executar aplicações multi-container
- mocks — objetos simulados usados em testes
- benchmarks — testes de desempenho comparativos
- commit — registro de alterações no repositório
- pre-commit — etapa/validação executada antes do commit

**Resumo**
A aula apresenta o papel das guidelines no desenvolvimento de software e mostra que elas podem ir além de simples convenções de código, abrangendo praticamente todo o fluxo de trabalho do projeto. O instrutor explica que guidelines podem definir padrões de nomenclatura, indentação, comentários, estrutura do projeto, uso de containers, segurança, testes, commits, Git, pull requests, performance e observabilidade. Também destaca que nem todo projeto precisa de todas as seções, e que o conteúdo deve ser adaptado ao contexto e à complexidade da solução.

Em seguida, o instrutor lista as principais seções de um template de guidelines. Entre elas estão Core Principles, com regras fundamentais que não devem ser quebradas; Setup e Inicialização, com instruções para subir, descer e operar o ambiente, rodar scripts e executar migrações; Estrutura do Projeto, com organização de pastas e uso de Docker e Docker Compose; Convenções de Código, cobrindo nomeação, tipagem, funções, métodos, tratamento de erros, concorrência, paralelismo, abstrações e interfaces. Também aborda Testes, incluindo unitários, integração, mocks, estresse e carga; Profiling e Diagnósticos, para verificar comportamento, rodar benchmarks e orientar otimizações; Segurança; Padrões de Código, com exemplos do que fazer e do que evitar; Gerenciamento de Dependências; Comentários e Documentação; Banco de Dados; Logs e Observabilidade.

Por fim, a aula enfatiza as Golden Rules, ou regras de ouro, que consolidam e conectam todas as diretrizes anteriores. A partir delas, é possível criar uma checklist pré-commit para que a IA ou o agente verifique requisitos antes de realizar um commit, preservando a integridade do sistema e o alinhamento com as convenções do projeto. O uso de referências internas e externas também é destacado como forma de apoiar a navegação pela documentação e facilitar a aplicação das guidelines na prática.

**Pontos de atenção**
- As guidelines devem ser adaptadas ao tipo e à maturidade do projeto; nem todas as seções são obrigatórias.
- Convenções de código precisam ser explícitas, incluindo indentação, nomenclatura, tipagem, comentários e tratamento de erros.
- A estrutura do projeto pode ficar nas guidelines ou em documentos arquiteturais, mas deve estar bem referenciada quando houver dependências entre os documentos.
- Ao definir setup e inicialização, é importante detalhar como subir/descer o ambiente, executar scripts e fazer migrações.
- Em projetos com containers, documentar claramente Dockerfile e Docker Compose evita ambiguidades operacionais.
- Testes devem cobrir diferentes níveis: unitários, integração, estresse, carga, além de uso adequado de mocks e atenção à testabilidade.
- Profiling, diagnósticos e benchmarks ajudam a validar comportamento e orientar otimizações antes de mudanças em produção.
- Segurança deve ser tratada como ponto crítico desde o início, não como complemento posterior.
- Em padrões de código, exemplos de “o que fazer” e “o que não fazer” ajudam muito a IA a gerar saídas mais consistentes.
- Gerenciamento de dependências deve considerar a tecnologia usada e o ecossistema de pacotes e gerenciadores.
- Comentários e documentação devem indicar não só como documentar, mas também onde encontrar outras partes da documentação para linkagem.
- Regras de ouro e checklist pré-commit são importantes para garantir integridade e aderência às convenções antes de commitar.
- Referências internas e externas precisam ser tangíveis e úteis para apoiar o processo de desenvolvimento e manutenção.