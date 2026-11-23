Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17769)

## Resumo da aula

O projeto é estruturado em fases incrementais para mostrar como a especificação passa a orientar a implementação sem depender de um ambiente fortemente guiado. A escolha deliberada é trabalhar com zero guidance e sem custom harness, deixando apenas o mínimo de instrução em arquivos como CLAUDE.md e AGENTS.md. Isso força a observação do que o agente consegue produzir quando a principal fonte de direção está nos documentos do projeto, e não em uma camada operacional construída ao redor dele. A única ajuda adicional é o uso de uma skill com guideline de boas práticas.

A primeira etapa organiza o desenvolvimento a partir de três artefatos: um PRD com fases de implementação, uma especificação técnica para cada fase e um plano de desenvolvimento correspondente. O PRD define o recorte funcional do que será construído, enquanto a especificação técnica traduz cada fase em decisões implementáveis. O plano de desenvolvimento conecta esses documentos à execução, servindo como ponte entre intenção e entrega. As skills PRD Writer e Spec Writer automatizam essa produção documental por feature.

Gerar um PRD por comando é insuficiente quando o objetivo é construir um processo reutilizável. O ponto central está no racional da skill: como o prompt foi estruturado e como partes da especificação são conectadas às features que surgem ao longo do projeto. Esse desenho importa porque uma skill útil não apenas escreve documentos; ela preserva coerência entre requisitos, decomposição funcional e implementação futura. Quem entende esse racional consegue adaptar uma skill existente ou criar a própria com mais controle.

Retomando a separação entre especificação e controle operacional já discutida, a lista de tarefas aqui não existe para microgerenciar cada ação do agente. Sua função principal é registrar o estado do processo: onde a execução parou, o que já foi concluído, o que ainda falta e o que está ou não funcionando. Esse uso é mais valioso do que um checklist excessivamente detalhado, porque mantém continuidade sem sufocar a capacidade de decisão do modelo. A granularidade, portanto, serve ao rastreamento do progresso, não ao comando minucioso.

Modelos mais modernos reduzem a necessidade de decompor o trabalho em instruções muito pequenas. Quando a lista de tarefas fica detalhada demais, ela pode limitar o agente a seguir caixas de seleção em vez de explorar soluções melhores dentro da especificação disponível. Isso não elimina a necessidade de granularidade; apenas desloca seu papel para casos em que o modelo precisa de mais orientação. A quantidade de detalhe passa a depender da capacidade do modelo e do nível de autonomia que se deseja permitir.

Depois que algumas fases já estão estabelecidas, o processo evolui para execução simultânea de features dependentes. O mecanismo proposto é o uso de múltiplas git worktrees, permitindo que diferentes linhas de desenvolvimento avancem em paralelo sem disputar o mesmo diretório de trabalho. Esse arranjo amplia a produtividade porque cada feature pode seguir seu fluxo próprio até o momento de integração. O paralelismo, porém, exige atenção às dependências entre fases para que a ordem lógica do sistema continue consistente.

Quando as branches paralelas convergem para a main, conflitos passam a ser parte normal do fluxo. A expectativa é que a IA consiga lidar com parte dessa reconciliação, desde que as features tenham sido desenvolvidas com especificações claras e escopo razoavelmente isolado. O merge deixa de ser apenas uma operação de Git e passa a ser um teste da qualidade da decomposição do projeto. Se as fases foram bem separadas, a integração tende a preservar funcionalidades já operantes.

A necessidade de mais ou menos granularidade reabre a fronteira, já discutida anteriormente, entre especificação do produto e mecanismos de controle do agente. Quando o documento começa a detalhar demais como executar o trabalho, ele deixa de apenas descrever o sistema e passa a influenciar diretamente o comportamento operacional do modelo. Esse ponto é importante porque o mesmo artefato pode funcionar como especificação em um contexto e como guidance em outro. A decisão depende do modelo usado e do quanto se quer restringir sua autonomia.

## Transcrição

00:01

Bom pessoal, então para que a gente consiga entender o que nós vamos fazer,

00:05

porque a gente não vai ficar aqui só na teoria, a gente vai desenvolver as coisas,

00:09

mas para que a gente consiga entender o que a gente vai fazer vai ser o seguinte,

00:14

a gente vai fazer alguns exemplos práticos de um projeto,

00:18

e esse exemplo vai ter algumas fases

00:23

incrementais onde a gente vai adicionar alguns documentos,

00:27

algumas especificações.

00:29

para que nós possamos fazer com que o agente ali desenvolva o software.

00:34

Porém, vai ter um detalhe aqui nesses nossos exemplos.

00:38

Nós vamos ter aqui zero guidance. A gente não vai ter custom harness.

00:45

Ou seja, eu vou colocar o mínimo do mínimo de instrução,

00:49

sei lá, no Cloud MD, no Agents MD. Eu não vou...

00:53

ficar colocando detalhes de como subir servidor, de como descer servidor,

00:58

a não ser que realmente o ambiente não esteja

01:01

funcionando ou com algum problema muito grande.

01:03

Mas, basicamente,

01:04

eu vou dar para ferramentas zero ali. Ou seja,

01:09

eu não vou criar em volta do nosso sistema, em volta do agente,

01:15

recursos para facilitar a vida dele,

01:18

para ele criar o software da forma como ele quer.

01:21

A única coisa que eu vou fazer,

01:22

eu vou pedir para ele utilizar uma skill,

01:24

pelo menos para ele ter uma guideline de boas práticas para desenvolver o projeto.

01:28

Apenas isso que a gente vai fazer. E para isso,

01:31

nós vamos separar isso em algumas fases aqui.

01:35

A primeira fase vai ser o quê? A gente vai fazer a geração de um PRD,

01:40

que é um Product Requirement Document.

01:43

E esse PRD vai ter diversas fases de implementação. Certo?

01:49

Também, o que a gente vai fazer?

01:51

A gente vai gerar uma especificação técnica para cada fase.

01:56

E a gente vai gerar um plano de desenvolvimento para cada fase.

02:01

Então, para isso, eu tenho aqui duas skills.

02:05

Provavelmente, ali no futuro,

02:06

eu vou consolidar para uma skill só que faz todas as coisas,

02:09

mas, de qualquer forma,

02:10

eu tenho uma skill que é um PRD Writer e eu tenho uma outra

02:14

skill aqui com um Spec Writer para a gente fazer a geração do PRD.

02:19

e a geração da especificação, tá? Por feature que a gente vai trabalhar.

02:23

Então, esse aqui é o grande ponto. Agora,

02:27

o que eu não quero aqui nesse capítulo é que eu

02:31

simplesmente dê um comando e a gente vai gerar o PRD, tá?

02:37

Por quê? Porque seria muito fácil, né?

02:41

E eu acho que seria muito raso simplesmente trazer isso pra vocês no curso. Então,

02:46

eu vou mostrar pra você...

02:48

qual foi o racional que eu utilizei para fazer essa skill,

02:53

para que quando você for utilizá-la,

02:56

utilizar uma skill de terceiro, ou fazer a sua própria skill e etc.,

03:01

o que acontece? Você consegue entender alguns conceitos básicos,

03:05

porque isso envolve prompt,

03:06

mas principalmente a forma de como você integra

03:10

Partes da sua especificação com as features que...

03:17

Vão sendo geradas.

03:19

A segunda fase aqui que a gente vai fazer é que,

03:24

Além de eu ter esses documentos,

03:27

Eu também vou ter um documento para o controle do

03:31

Estado do processo de desenvolvimento de forma mais granular.

03:34

Ou seja, eu vou gerar como se fosse uma lista de tarefas,

03:38

Mas essa lista de tarefas tem um objetivo bem importante,

03:44

Que é realmente a gente saber aonde... que o processo parou.

03:49

E por que eu estou dizendo isso?

03:51

Porque antigamente nós tínhamos que

03:55

Fazer listas de tarefas muito granulares,

03:59

Com detalhe por detalhe do que o agente tem que fazer,

04:04

Porque senão ele não ia fazer certo.

04:07

Porém, agora, os modelos mais modernos, eles estão muito bons. E muitas vezes,

04:15

Colocar uma granularidade muito grande de

04:17

Tarefas vai limitar o potencial do agente

04:22

Fazer coisas melhores e não ficarem limitadas somente com um monte de checkbox. Então,

04:28

Cada dia a mais, eu acredito que lista de tarefas do que a IA vai ter que fazer,

04:33

Elas vão ser cada vez menores, porque os modelos estão ficando ali cada vez...

04:38

Ali mais inteligentes, vamos dizer assim.

04:41

Mas de qualquer forma, essa parte de tarefas,

04:44

Ela vai servir muito mais como um documento de estado, tá? Da onde parou,

04:49

O que foi feito e o que ainda não feito,

04:52

O que tá funcionando e o que não tá funcionando,

04:55

Tá? Então essa vai ser a nossa fase 2.

04:58

E a nossa fase 3,

04:59

Que na minha opinião é uma das fases mais legais e é o

05:03

Que vai mais mudar o seu jogo no dia a dia, tá?

05:06

Que é conseguir trabalhar com dependência entre

05:08

As fases de desenvolvimento em paralelo. O que significa?

05:12

Que após eu desenvolver determinadas fases,

05:16

A gente vai ter a possibilidade de trabalhar em fases de forma simultânea.

05:21

Ou seja, a gente vai criar e trabalhar com diversas work trees,

05:26

Git work trees, e a gente consegue desenvolver features em paralelo.

05:30

Quando a gente fizer um merge ali na main, por exemplo, o que que...

05:34

Isso vai acontecer no final das contas,

05:37

Nós vamos poder jogar isso na main, eventualmente, claro,

05:43

A gente vai encontrar conflitos, a Yala vai ser capaz de resolver esses conflitos,

05:47

Mas as nossas features vão estar falando ali e funcionando.

05:51

Então, essa aqui é a nossa ideia. Então,

05:54

A ideia aqui desse nosso capítulo, dessa parte do nosso curso,

05:58

É que a gente consiga desenvolver um sistema...

06:01

Esse sistema vai ter as especificações,

06:04

A gente vai desenvolver algumas features de forma mais sequencial e ao longo

06:09

Do tempo nós vamos ter também o processo de desenvolvimento trabalhando em paralelo.

06:15

Esse documento aqui onde a gente gera para trabalhar com estado, ele é interessante,

06:20

Mas novamente o que eu queria deixar aqui para você muito claro é,

06:24

Ele vai servir muito mais aqui para a gente guardar

06:28

O estado de como que as coisas estão.

06:30

Do que necessariamente ficar com um checkbox de muitos itens por item.

06:36

Eu não quero trabalhar tanto assim.

06:38

Cada dia mais que eu vejo os modelos evoluindo,

06:41

mais eu vejo que a granularidade tem que ser menor. Por outro lado,

06:45

dependendo do modelo que você for utilizar, sim,

06:48

você vai precisar ter mais granularidade para conseguir guiar melhor o agente.

06:53

E aí a gente vai entrar,

06:55

a gente entra naquele ponto. Até que ponto a especificação...

07:00

muda o comportamento do agente,

07:02

ou seja, acaba entrando um pouco na parte de harness.

07:05

Beleza? Então,

07:07

essa aqui é a nossa ideia principal e vamos nessa porque

07:12

a gente vai falar sobre o PRD Writer aqui para vocês.

## Resumo IA

**Abreviações**
*   **PRD**: Product Requirement Document
*   **IA**: Inteligência Artificial

**Resumo**
A aula tem como objetivo demonstrar, através de exemplos práticos e incrementais de um projeto, como a especificação pode orientar a implementação de software por um agente, operando com "zero guidance" e sem um "custom harness". A abordagem deliberada é de fornecer o mínimo de instrução (exceto em arquivos como CLAUDE.md e AGENTS.md), forçando a observação do que o agente consegue produzir quando sua principal fonte de direção são os documentos do projeto, e não uma camada operacional construída ao redor dele. A única ajuda adicional permitida é o uso de uma skill que forneça diretrizes de boas práticas.

O fluxo de desenvolvimento é dividido em fases incrementais. A **primeira fase** concentra-se na organização do desenvolvimento a partir de três artefatos principais por feature: um *Product Requirement Document (PRD)*, que define o escopo funcional e as fases de implementação; uma *especificação técnica*, que traduz cada fase em decisões implementáveis; e um *plano de desenvolvimento*, que conecta esses documentos à execução. Para automatizar essa produção documental, são utilizadas skills como `PRD Writer` e `Spec Writer`. É enfatizada a importância de compreender o racional por trás da estruturação dessas skills – como o prompt foi elaborado e como partes da especificação se conectam às features – para que o desenvolvedor possa adaptar skills existentes ou criar as suas próprias de forma eficaz e coerente.

A **segunda fase** introduz um documento para o controle do estado do processo de desenvolvimento, funcionando como uma lista de tarefas. O objetivo principal dessa lista não é microgerenciar cada ação do agente, mas sim registrar o estado do processo: onde a execução parou, o que já foi concluído, o que ainda falta e o que está ou não funcionando. Isso mantém a continuidade sem limitar a capacidade de decisão do modelo. Discute-se que modelos de IA mais modernos reduzem a necessidade de decompor o trabalho em instruções muito pequenas; um detalhamento excessivo pode limitar o agente a seguir caixas de seleção, em vez de explorar soluções melhores. A granularidade ideal, portanto, depende da capacidade do modelo e do nível de autonomia desejado.

Na **terceira fase**, o processo evolui para a execução simultânea de features dependentes. O mecanismo proposto é o uso de múltiplas *Git worktrees*, permitindo que diferentes linhas de desenvolvimento avancem em paralelo sem competir pelo mesmo diretório de trabalho, ampliando a produtividade. Quando as branches paralelas convergem para a `main`, conflitos de merge são esperados. A expectativa é que a IA consiga lidar com parte dessa reconciliação, desde que as features tenham sido desenvolvidas com especificações claras e escopo razoavelmente isolado. O merge, neste contexto, torna-se um teste da qualidade da decomposição do projeto.

**Pontos de atenção**
*   **Zero Guidance e Autonomia do Agente**: A escolha de trabalhar com "zero guidance" e sem "custom harness" é uma boa prática para observar a capacidade real do agente, forçando-o a se basear principalmente na documentação do projeto. A única exceção é uma skill de boas práticas.
*   **Racional por Trás das Skills**: Não basta apenas usar ou gerar documentos com skills; é crucial entender o racional de sua construção (estrutura do prompt, conexão entre especificação e features). Esse entendimento permite adaptar e criar skills que garantam coerência entre requisitos, decomposição funcional e implementação.
*   **Lista de Tarefas como Registro de Estado**: A função primária de uma lista de tarefas deve ser o registro do estado do processo (onde parou, o que está feito/pendente, o que funciona/não funciona), e não o microgerenciamento das ações do agente, que pode limitar sua autonomia.
*   **Granularidade da Orientação**: Com modelos de IA mais modernos, a necessidade de instruções muito granulares diminui. Detalhar demais as tarefas pode limitar o potencial do agente, transformando-o em um executor de checklists. A granularidade deve ser ajustada à capacidade do modelo e ao nível de autonomia desejado.
*   **Gerenciamento de Dependências no Desenvolvimento Paralelo**: Ao usar múltiplas Git worktrees para desenvolvimento paralelo, é essencial ter atenção rigorosa às dependências entre as fases para garantir a consistência lógica do sistema.
*   **Merge como Teste de Qualidade**: O processo de merge para a branch `main` serve como um teste da qualidade da decomposição do projeto. Conflitos são esperados, mas a capacidade da IA de resolvê-los e a manutenção da funcionalidade são indicadores de especificações claras e escopo bem isolado das features.
*   **Fronteira entre Especificação e Controle Operacional**: Um ponto crítico é a distinção entre descrever o sistema (especificação) e influenciar diretamente o comportamento operacional do agente (guidance/harness). Detalhar excessivamente a execução na especificação pode transformar o documento em uma ferramenta de controle, restringindo a autonomia do modelo.