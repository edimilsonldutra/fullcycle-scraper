Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17782)

## Resumo da aula

Autenticação funciona como uma Core Feature porque estabelece a base operacional da área interna do sistema. Retomando o bootstrap já criado anteriormente, ela conecta usuário, sessão, password storage, rotas de acesso e redirecionamento para /app. Esse papel estrutural faz a especificação crescer mais do que a de uma landing page, já que envolve persistência, fluxo de sessão, validação e regras de acesso. Em SDD, isso exige que a feature já nasça preparada para sustentar dependências futuras.

A costura entre features aparece quando uma entrega anterior cria pontos de extensão para a próxima. O getSession em _lib/session.ts, que inicialmente retorna null, é uma stub criada na feature da landing page para que a autenticação substitua esse comportamento depois. Isso evita retrabalho na integração e permite que a próxima feature se apoie em contratos já existentes. A dependência entre features, portanto, não é um acidente: ela é planejada na especificação.

A especificação da autenticação descreve o comportamento em nível de fluxo, não apenas em nível de arquivo. O registro detalha visita à rota, renderização da página, submissão do form, execução de server action, validação e tratamento de casos inválidos ou duplicados; o login e o logout seguem a mesma lógica de encadeamento. Esse formato reduz ambiguidade porque transforma requisitos em passos verificáveis. Em features com mais back-end, esse nível de detalhe é necessário para alinhar implementação, dados e testes.

A especificação inclui escopo, exclusões, impactos, workflow local, Docker Compose, variáveis de ambiente, contratos de API, modelagem de banco, SQL e representação no Prisma. Isso concentra em um único artefato as decisões que normalmente ficariam espalhadas entre documentação informal e código. Quando essas decisões vêm de entrevistas e interações com o modelo, elas deixam de ser implícitas e passam a ser auditáveis. O resultado é uma implementação mais previsível e menos dependente de interpretação ad hoc.

Critério de aceitação útil não fica solto no PRD: ele precisa estar ligado aos recursos implementados e aos testes que comprovam seu atendimento. A correlação entre requisito, funcionalidade e estratégia de teste cria rastreabilidade, permitindo responder exatamente o que precisa ser construído para validar cada critério. Em autenticação, isso é especialmente relevante porque fluxos como registro, login e logout têm múltiplos estados de erro e sucesso. Sem esse mapeamento, a implementação pode parecer completa e ainda assim deixar lacunas comportamentais.

Assumptions registram decisões inferidas pelo agente ou pelo processo de geração quando algo não foi explicitamente definido. Elas não são verdades do sistema; são hipóteses operacionais que podem ser revisadas antes ou durante a implementação. Tornar essas inferências visíveis reduz o risco de o projeto absorver decisões silenciosas que ninguém validou. Em SDD, isso é crucial porque parte da velocidade vem justamente da capacidade de explicitar e corrigir suposições cedo.

O plano de execução organiza a feature em stages e steps, separando fundação de banco, autenticação, server actions e demais partes da entrega. Essa decomposição transforma uma feature grande em unidades menores e ordenadas, o que ajuda tanto o agente quanto o desenvolvedor a manter contexto e sequência. Retomando a lógica de costura entre features, o plano também preserva dependências internas: primeiro a base, depois os comportamentos que dependem dela. Em prática, isso reduz implementação fora de ordem e facilita acompanhamento do progresso.

O guidance não precisa começar com um harness rígido para já produzir ganho. Uma instrução no CLAUDE.md para carregar a skill Next Best Practice em sessões que alterem TS, TSX, rotas, server actions e Prisma já cria um comportamento padrão reutilizável. Isso elimina a necessidade de repetir o mesmo prompt operacional a cada nova sessão. A estratégia é progressiva: primeiro o mínimo de guidance, depois regras mais fortes quando houver necessidade de maior controle.

Criar uma branch com o nome da feature isola a implementação e mantém o fluxo compatível com o processo já estabelecido anteriormente. A partir daí, o agente recebe a especificação da feature, o PRD e as instruções de guidance para iniciar a implementação com contexto suficiente. O comportamento esperado é explorar o estado atual do projeto, identificar as stubs existentes e substituir ou expandir esses pontos conforme o plano. Esse fluxo mostra como SDD combina especificação detalhada com execução incremental assistida por agente.

## Transcrição

00:00

Bom, pessoal, então, nosso ponto agora aqui é ir para a nossa Feature 2.

00:05

Eu gerei essa Feature 2, para que você não fique esperando 10 horas aqui, tá?

00:11

E o ponto importante aqui dessa nossa Feature 2 é o seguinte, né?

00:18

Vamos apenas dar uma olhada nela, não quero ficar muito tempo aqui nela,

00:22

tá? Mas, basicamente, a ideia dela, ela também é uma Core Feature,

00:28

porque ela dá toda a base...

00:30

para a parte interna do sistema, então ela é a autenticação.

00:35

Então, technical overview, vai ter usuário,

00:38

vai ter uma session com a tabela de password e vai ter um cookie backend

00:43

session store que está compartilhado em um get

00:46

session reader consumido para o sistema de autenticação.

00:52

Vai ter a rota register, barra login e vai redirecionar para a barra app.

00:57

Por que ele sabe que vai redirecionar para a barra app, pessoal?

01:00

Porque tem toda aquela história de uma feature grudar na outra.

01:04

Ele coloca por quê? Porque toda feature que foi feita,

01:07

que foi dependendo da feature 01 que a gente fez,

01:10

da landing page, tem o bootstrap do projeto.

01:14

Inclusive, ele tem ali o session .ts, que é uma stub.

01:19

Então, isso aqui, galera, que é algo importante.

01:22

Se você olhar aqui, a underline lib,

01:27

session .ts, você vai ver aqui que o getSession,

01:31

ele sempre retorna em branco. Se você perceber,

01:35

essa responsabilidade não necessariamente teria que ser

01:40

da feature que faz a landing page.

01:43

Concorda comigo? Porque isso faz parte da autenticação.

01:47

Porém, como uma feature precisa grudar na outra, o que acontece?

01:51

A feature de landing page já criou uma base

01:59

de getSession como uma stub para que a segunda

02:02

feature já esteja preparada para fazer esse CRUD, vamos dizer assim,

02:06

para fazer essa integração. Então, aqui ele até colocou,

02:09

feature1 stub, this module will replace pela feature2 authentication system.

02:15

Até então, o getSession apenas retorna nulo por conta disso. Então, se você perceber,

02:21

há essa dependência, né?

02:27

de uma feature com a outra que acaba acontecendo.

02:30

E aí tem o que está no escopo, tudo que vai ser feito, como é que vai ser feito,

02:34

vai ter um Docker Compose, vai ter um .wav e .local no workflow,

02:39

o Docker Compose ele vai subir, pode utilizar, o que está excluído,

02:45

impactos, arquivos, e galera, aqui vai longe,

02:49

que é toda a especificação de como é que funciona.

02:52

Então tem todos os arquivos, as especificações,

02:55

o visitante, acesso barra register, register barra page, tem o form,

03:01

daí tem o submit, daí tem o server action,

03:03

faz a validação, se está inválido, se não está inválido, se existir, ou seja,

03:08

ele traz todos os aspectos aqui para a gente.

03:11

Mas esse aqui é o data flow de registrar.

03:14

A gente tem o data flow da outra parte, que é o de login.

03:17

Visita o login, faz o login, etc., valida, busca.

03:23

O usuário verifica o password, se não retorna. Então,

03:26

ele gera todo esse fluxo aqui para a gente e como é que funciona o fluxo de logout.

03:30

E aí tem as decisões técnicas.

03:32

Essas decisões técnicas, elas foram feitas na entrevista,

03:36

na hora que eu fui gerar as conversas ali com o modelo.

03:42

Então, isso aí é um ponto importante para a gente conseguir trabalhar.

03:47

Então, aqui, olha as instruções e tudo mais.

03:53

Então, essa que é a ideia principal, ele gerou essas especificações,

03:57

os contratos da API que ele vai trabalhar,

04:00

ou seja, aqui já é uma especificação, como tem muito back-end,

04:05

acaba sendo uma especificação muito maior, no final das contas,

04:08

do que necessariamente uma especificação daquela landing page,

04:13

porque tem mais código, tem mais detalhes,

04:16

então ele traz até tabelas do banco de dados, o SQL.

04:20

que ele vai precisar, como que isso pode ser modelado lá no Prisma,

04:23

a estratégia de teste de como que isso funciona.

04:27

E uma das coisas mais interessantes de tudo isso, novamente,

04:31

é que ele vai conseguir entender

04:36

o mapeamento e os critérios de aceitação,

04:39

ou seja, baseado no critério de aceitação do PRD,

04:44

vai estar coberto esses critérios aqui.

04:50

Esses critérios vão ser baseados nesses recursos que vão ser feitos.

04:55

Esses aqui vão ser baseados nesses caras, nesses testes aqui.

04:58

Esse vai ser nesse. Então,

05:00

ele traz uma correlação do que é critério e para eu testar esse critério,

05:04

o que vai precisar fazer.

05:06

Então, isso aí é um ponto importante.

05:09

Está falando que é uma cross-features. E assumptions, basicamente,

05:13

é o que ele acha que deve fazer. Ou seja, o que ele tirou da cabeça dele,

05:19

que não foi feito em uma entrevista, e se eu quiser,

05:22

eu posso vir aqui e mudar e avaliar.

05:26

Então, normalmente, é super importante a gente trabalhar nesse tipo de aspecto.

05:30

Então, basicamente está aqui, lembrando que ele já está preparando, inclusive,

05:36

essa feature para outras features lá da frente. Então,

05:40

é importante que você consiga ver. E depois, nós temos aqui o nosso plano.

05:48

que ele trouxe aqui para a gente trabalhar. Ou seja, ele vai usar esse plano,

05:53

aqui são os pré-requisitos, e aqui tem passo 1, banco de dados e fundação.

05:59

Prisma, aqui, autenticação, daí vai, server actions,

06:05

daí tem todos os passos aqui que ele faz.

06:07

E, ou seja, tem quatro steps,

06:09

quatro fases, quatro stages, com quantos steps?

06:15

com 15 steps para ele fazer cada um desses stages aqui para mim. Então,

06:20

isso aí eu acho que é um ponto importante.

06:23

E agora, para a gente conseguir fazer, basicamente,

06:26

o que eu vou trabalhar vai ser basicamente o que a gente fez da outra vez.

06:33

E enquanto ele vai gerar isso, no vídeo futuro,

06:37

lá em seguida, eu quero mostrar a estrutura do PRD,

06:41

porque é muito importante que você vai...

06:44

entendendo como uma feature costura a outra,

06:46

tá? Então, se você perceber, eu tô reforçando muito isso,

06:49

porque essa é a maior dor de todo mundo que vai trabalhar com SDD, tá? Então,

06:55

tá aqui essa feature de como que ela vai ser

06:58

feita e como que ela vai ali ser trabalhada, beleza?

07:03

Eu vou colocar aqui pra mim, eu vou dar um...

07:07

Eu posso mudar de branch, obviamente, aqui.

07:12

Ou se eu quiser, eu não vou comitar diretamente no master, no main,

07:14

mas o ponto importante aqui é que eu vou criar e

07:19

vou mudar de branch para a gente conseguir trabalhar.

07:22

Então eu vou pegar e vou chamar esse branch do nome aqui da minha feature,

07:28

Tá? Então eu vou colocar aqui git checkout -b,

07:34

vou colocar esse cara aqui dentro, legal? E agora que ele está dentro desse branch,

07:40

eu vou pedir para ele fazer a mesma coisa que ele fez da outra vez,

07:44

que é fazer a parte de implementação.

07:49

E enquanto ele faz essa parte de implementação,

07:51

eu quero mostrar para vocês também a

07:55

parada e a skill do Playwright CLI também,

08:00

que a gente viu ele utilizando da última vez.

08:03

Ele pegou a skill que eu já tinha colocado ali no meu computador. Beleza? Então...

08:09

Eu vou colocar novamente, sem nenhum prompt,

08:11

e depois você pode ver que eu tenho um cara aqui,

08:15

de Implement Feature, que facilita a minha vida,

08:17

que tem mais regras, mas por enquanto eu vou fazer aqui na boa,

08:23

aqui com vocês. Então eu vou colocar Implement, a

08:29

F02,

08:38

ele não está conseguindo, ele ainda não achou.

08:41

Porque eu acho que não está comitado ou acabei de mudar.

08:44

Implemente, eu vou colocar o arroba... Ixi, espera aí.

08:49

É que eu estou com zoom gigante,

08:51

então o Claudio acaba caindo. Implemente arroba... Vou

08:57

copiar aqui o perf relativo.

09:03

Aqui, baseado no arroba PRD,

09:09

utilize a skill...

09:18

Next best practice aqui pra gente, tá? Mas, o que que acontece?

09:23

Pra eu não ficar agora escrevendo isso ali o tempo todo,

09:28

o que que eu posso já começar a querer fazer, tá?

09:32

E eu vou fazer isso de forma progressiva, pessoal,

09:34

pra dar o mínimo de guidance, mas não vai ser algo com harness muito forte,

09:39

porque a gente vai ter a parte de harness engineering,

09:42

Tá? Então, o que eu posso fazer aqui pra facilitar a minha vida,

09:46

eu posso... Chegar no meu Cloud.md, tá?

09:51

E colocar uma parte assim, ó. Que eu tenho aqui.

09:59

É a seguinte forma.

10:04

Development. Load next best practices skill at the

10:08

start of any session that will touch código TS,

10:11

TSX, route, servers, actions, Prisma e etc.

10:15

Basicamente, é isso aqui que eu estou colocando.

10:19

Vamos ver agora que eu vou iniciar uma nova sessão. Vamos ver se esse cara...

10:22

Se esse cara acaba subindo.

10:25

Deixa eu copiar aqui somente para não perder o meu texto.

10:30

E agora, deixa

10:32

eu diminuir um pouquinho o meu zoom, galera.

10:35

E agora eu vou colar esse cara aqui, tá?

10:40

Não vou pedir para ele escrever para usar skill,

10:42

Mas vamos ver como é que ele vai se comportar agora, daqui para frente. Vamos nessa.

10:50

Vamos ver esse cara começando a iniciar. Então,

10:53

ele está lendo a especificação e também...

10:56

vai ler ali o nosso PRD para ele começar a fazer o desenvolvimento.

11:01

Então, leu o CloudMD também, carregou a skill Next Best Practice,

11:08

que foi importante para a gente,

11:10

o mínimo de guidance que a gente está dando aqui para ele. E agora,

11:13

provavelmente, ele vai começar a fazer o processo de desenvolvimento. Primeira parte,

11:19

provavelmente ele vai explorar o que ele já tem

11:21

pronto e daí ele vai começar a desenvolver. Fechou?

11:25

Pessoal, eu vou deixar isso aqui rodando, tá?

11:27

E aí eu quero entrar e falar para

11:30

vocês um pouco do Playwright CLI por cima, tá?

11:35

Porque isso aí vai ser feito de uma forma mais

11:39

intencional quando a gente estiver na parte de Harness Engineering.

11:43

Lembre que o nosso ponto principal aqui é focar no quê, no final das contas?

11:50

Focar no SDD.

11:52

A especificação é gerada e eu vou dar o mínimo de guidance

11:55

ali pro nosso agente da forma como ele for trabalhar.

11:59

Então, vamos nessa.

## Resumo IA

**Abreviações**
*   **SDD**: Software-Defined Development
*   **PRD**: Product Requirements Document
*   **TS**: TypeScript
*   **TSX**: TypeScript XML (ou JSX para TypeScript)
*   **API**: Application Programming Interface
*   **SQL**: Structured Query Language
*   **CRUD**: Create, Read, Update, Delete
*   **CLI**: Command Line Interface
*   **.env**: Environment variables (variáveis de ambiente)

**Resumo**
A aula introduz a Feature 2, focada na autenticação, que é classificada como uma "Core Feature" por estabelecer a base operacional para a área interna do sistema. Ela aborda conceitos como gerenciamento de usuários, sessões, armazenamento de senhas, rotas de acesso (register, login) e redirecionamento para `/app`. A autenticação exige uma especificação mais detalhada do que uma landing page devido à sua complexidade, que envolve persistência, fluxo de sessão, validação e regras de acesso, garantindo que a feature possa sustentar dependências futuras, conforme o princípio do SDD.

Um ponto central é a "costura entre features", onde uma entrega anterior prepara o terreno para a próxima. Um exemplo é o `getSession` em `_lib/session.ts`, que inicialmente é uma stub (um retorno nulo) criada na feature da landing page, mas que será substituída e expandida pelo sistema de autenticação. Isso exemplifica como a dependência entre features é planejada na especificação para evitar retrabalho.

A especificação da autenticação vai além da listagem de arquivos, descrevendo o comportamento em nível de fluxo. Isso inclui o detalhamento de visitas a rotas, renderização de páginas, submissão de formulários, execução de server actions, validação e tratamento de casos inválidos ou duplicados para registro, login e logout. Esse nível de detalhe é crucial para alinhar implementação, dados e testes em features com mais back-end.

A especificação é um artefato abrangente que consolida escopo, exclusões, impactos, workflow local, uso de Docker Compose, variáveis de ambiente (.env), contratos de API, modelagem de banco de dados (SQL e Prisma). Isso centraliza decisões que, de outra forma, estariam dispersas. As decisões técnicas, muitas vezes geradas a partir de interações com o modelo (entrevistas), tornam-se auditáveis.

A aula também enfatiza a importância da rastreabilidade entre os critérios de aceitação do PRD, os recursos implementados e as estratégias de teste. Isso garante que cada critério seja validado, o que é fundamental para fluxos complexos como autenticação, que possuem múltiplos estados de sucesso e erro. "Assumptions" são decisões inferidas ou hipóteses operacionais registradas para visibilidade e revisão precoce, um aspecto crítico no SDD para corrigir suposições antes da implementação.

O plano de execução organiza a feature em estágios e passos, como fundação de banco, autenticação e server actions, decompondo uma entrega grande em unidades menores e ordenadas, respeitando dependências internas. Para a implementação assistida por agente (IA), a aula mostra como um guidance progressivo pode ser configurado em `CLAUDE.md` para carregar habilidades como "Next Best Practice" em sessões que manipulem código TS, TSX, rotas, server actions e Prisma, eliminando a repetição de prompts. A implementação é feita em um branch de feature isolado, com o agente explorando o projeto, identificando stubs e as expandindo conforme o plano.

**Pontos de atenção**
*   **Autenticação como "Core Feature":** Entender que a autenticação é uma funcionalidade estrutural que estabelece a base operacional do sistema interno, e, por isso, sua especificação é inerentemente mais complexa, abrangendo persistência, fluxo de sessão, validação e regras de acesso.
*   **Planejamento da "Costura" entre Features:** Reconhecer que a dependência entre features deve ser planejada desde a especificação. A criação de "stubs" em features anteriores (como `getSession` na landing page) é uma prática fundamental para criar pontos de extensão para features futuras, evitando retrabalho e facilitando a integração.
*   **Especificações Detalhadas de Fluxo para Back-end:** Em features com lógica de back-end significativa (ex: autenticação), a especificação deve detalhar o comportamento em nível de fluxo (visita a rota, submissão de formulário, server action, validação, tratamento de erros). Isso é crucial para reduzir ambiguidades e garantir o alinhamento entre implementação, dados e testes.
*   **Centralização de Decisões na Especificação:** Consolidar todas as decisões técnicas (escopo, exclusões, impactos, workflow, Docker Compose, variáveis de ambiente, contratos de API, modelagem de banco de dados com SQL e Prisma) em um único artefato. Isso torna as decisões auditáveis e leva a implementações mais previsíveis.
*   **Rastreabilidade de Critérios de Aceitação:** É essencial correlacionar os critérios de aceitação do PRD diretamente com os recursos implementados e as estratégias de teste. Isso garante que todos os requisitos sejam verificados, especialmente em fluxos complexos com múltiplos estados de erro e sucesso.
*   **Explicitação de "Assumptions":** Registrar as decisões inferidas (assumptions) que não foram explicitamente definidas. Elas são hipóteses operacionais que devem ser visíveis para revisão e correção precoce, prevenindo que o projeto absorva decisões silenciosas não validadas.
*   **Plano de Execução Estruturado:** Decompor features grandes em estágios e passos menores e ordenados no plano de execução. Isso ajuda a manter o contexto, garante a sequência correta da implementação e preserva as dependências internas (ex: base de dados antes de comportamentos que dependem dela).
*   **Guidance Progressivo para Agentes de IA:** Iniciar com o mínimo de guidance para os agentes (ex: uma instrução simples em `CLAUDE.md` para carregar uma skill específica para certos tipos de arquivos). Adicionar regras mais fortes apenas quando houver necessidade de maior controle, evitando um "harness" rígido desde o início.
*   **Desenvolvimento em Branch de Feature Isolado:** Sempre criar um branch específico para a feature (`git checkout -b <feature-name>`) para isolar a implementação, garantindo a compatibilidade com o processo de desenvolvimento e permitindo que o agente trabalhe em um contexto controlado.