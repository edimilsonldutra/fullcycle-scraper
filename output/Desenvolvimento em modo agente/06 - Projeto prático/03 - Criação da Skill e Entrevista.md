Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17966)

## Resumo da aula

Criar uma skill do zero fica mais eficiente quando o agente conduz uma entrevista sobre o projeto. Em vez de começar escrevendo regras manualmente, você fornece um prompt curto com stack, decisões arquiteturais e o tipo de ajuda desejada, e o agente passa a fazer perguntas para descobrir convenções, camadas e restrições do sistema. Esse formato reduz ambiguidade porque transforma conhecimento implícito do projeto em respostas explícitas que depois viram um primeiro draft da skill.

Uma forma prática de iniciar esse processo é usar uma skill pronta voltada a entrevista, como o recurso citado de Grill Me, ou um Plan Mode equivalente no agente que você já utiliza. O papel dessa skill não é definir a arquitetura por conta própria, mas estruturar a coleta de contexto com perguntas sucessivas. Isso acelera a descoberta de padrões do projeto e evita que a skill final nasça apenas de suposições genéricas do modelo.

O prompt inicial pode ser simples, desde que contenha as decisões centrais do projeto. Informar tecnologias como TypeScript e Next.js, separar o back-end com Clean Architecture e DDD, e pedir ajuda para regras, convenções, anti-patterns e camadas arquiteturais já dá ao agente um eixo claro para a entrevista. Quanto mais específicas forem essas restrições iniciais, mais útil tende a ser a sequência de perguntas e mais alinhado será o draft gerado.

Retomando a ideia de skill como conhecimento explícito do projeto, o agente produz respostas melhores quando consegue inspecionar um codebase real. Por isso, vale incluir no repositório um projeto de exemplo, um hello world ou o scaffolding que já representa seus padrões de organização. Esses artefatos funcionam como evidência concreta das convenções desejadas e diminuem a chance de a skill ser baseada apenas em descrição textual abstrata.

Quando o agente analisa um projeto que já contém uma skill madura, a entrevista tende a ficar enviesada porque parte das respostas já está embutida no próprio repositório. Isso não invalida o processo, mas muda seu objetivo: em vez de descoberta genuína, ele passa a confirmar ou refinar algo que já está parcialmente definido. Para criar uma skill nova, o cenário mais útil é expor exemplos representativos do projeto sem antecipar toda a resposta.

A etapa de perguntas pode ser extensa, porque o agente precisa levantar detalhes suficientes para transformar preferências vagas em instruções operacionais. Esse tempo investido é o que permite chegar ao momento em que ele propõe desenvolver a skill e gera um primeiro draft coerente. O draft inicial não encerra o trabalho; ele serve como base editável para refinamento incremental.

Ter um hello world ou uma estrutura mínima do projeto evita o custo de começar do zero. Mesmo um exemplo pequeno já mostra organização de pastas, convenções de nomenclatura e separação de responsabilidades, o que orienta a entrevista e a escrita da skill. Esse ponto de partida aumenta a independência do agente porque ele passa a operar sobre padrões observáveis, não apenas sobre intenções declaradas.

A criação da skill é um processo iterativo entre IA e desenvolvedor. O agente ajuda a levantar perguntas, organizar o primeiro draft e sugerir estrutura, mas o ajuste fino depende de edição manual, experimentação e validação contínua. Em projetos reais, esse trabalho pode levar horas ou dias, porque a qualidade da skill depende do quanto ela reflete o modo real de trabalho da equipe.

O agente consegue ajudar melhor quando já existe uma noção arquitetural mínima na cabeça de quem está conduzindo o processo. Se essa base não existir, ele ainda pode apoiar no desenho de uma arquitetura mais decente, mas o resultado dependerá muito do contexto e da maturidade técnica de quem responde. A skill não substitui entendimento arquitetural; ela formaliza e operacionaliza esse entendimento.

Usar um projeto já existente como referência é uma estratégia forte para criar uma skill alinhada ao seu jeito de trabalhar. Em vez de inventar padrões durante a entrevista, você pede ao agente que extraia e organize padrões que já aparecem no código e no scaffolding que você confia. Isso torna a skill mais aderente à prática real do time e menos dependente de recomendações genéricas.

## Transcrição

00:00

Bom, pessoal, seguinte,

00:02

eu estou com um projeto aberto aqui e a única coisa que esse projeto tem,

00:07

de forma geral, é a skill que eu criei.

00:09

Mas antes de eu sair mostrando a skill, dando um monte de exemplos e etc.,

00:14

eu queria dar algumas dicas para quando você for criar realmente a sua skill.

00:20

Porque daí vai começar a valer bastante a pena

00:23

para você gerar mais esse nível de independência.

00:26

Então, o negócio é o seguinte.

00:28

Uma dica que eu dou é procurar alguma skill

00:32

pronta ou utilizar o Plan Mode do seu agente.

00:37

Eu estou aqui com o Cloud Code,

00:38

mas poderia ser com qualquer outro para ele conseguir te entrevistar.

00:43

Então, esse aí é o grande ponto. Hoje, eu estou utilizando...

00:48

Esse camarada que chama Grill Me, tá? Então, se você for no skills.sh e buscar,

00:52

é um camarada, ele cria várias skills bacanas, vale a pena você dar uma olhada.

00:56

Mas, basicamente, essa skill, ela é muito simples, tá? É muito simples.

01:02

É uma skill com três linhas, basicamente. E ela faz com que você, o agente,

01:08

ele comece a te explorar, a perguntar um monte de coisa ali no seu caso,

01:14

tá? Então, nesse caso... Normalmente, como é que eu começo?

01:19

Eu dou aqui um Grill Me e eu coloco o seguinte,

01:23

eu posso escrever da forma mais simples possível.

01:26

Preciso criar uma skill para

01:30

meu projeto em

01:33

TypeScript usando

01:36

Next.js.

01:41

Porém, a

01:44

parte do back-end será separada usando

01:52

Clean Architecture e DDD.

01:56

Preciso de ajuda

02:02

para criar regras,

02:05

convenções,

02:07

anti-patterns,

02:11

camadas arquiteturais e

02:16

etc. Quando você dá um Enter,

02:19

ele vai analisar o seu codebase e, baseado no seu codebase, ele vai...

02:24

começar a ajudar a tirar as suas dúvidas, as suas perguntas e coisas desse tipo.

02:29

Então, o que normalmente eu recomendo que você faça?

02:36

Pegue um projeto que você já tem de exemplo,

02:38

pegue o scaffolding que você já usa de exemplo no seu projeto e coloque isso aí...

02:45

na sua árvore, aqui dentro dos seus arquivos.

02:48

Pode ver que ele está explorando a minha própria skill. Então,

02:50

isso aqui que eu estou fazendo, ele vai sair extremamente enviesado,

02:53

porque ele já sabe o que eu estou querendo.

02:55

Mas a ideia é que, quando você tem o seu projeto,

03:00

ele vai entender a ideia daquele seu projeto e ele vai começar.

03:04

A fazer as perguntas. E aqui ele vai entender, ó,

03:06

eu já encontrei uma skill aqui, bem completa.

03:09

Você quer o quê? Então, se você perceber,

03:11

ele vai começar a fazer um monte de perguntas. E, às vezes,

03:14

você pode ficar horas nesse monte de perguntas.

03:17

O fato é que, quando ele terminar a entrevista e etc.,

03:22

ele vai chegar, então, vamos desenvolver a skill? Sim.

03:25

Aí ele vai gerar aquele primeiro draft. Então,

03:28

essa que é a ideia. Então, tenha um hello world. Vamos dizer ali,

03:33

pra facilitar a sua vida na hora de você fazer a criação da sua skill,

03:37

porque daí isso vai fazer muita,

03:39

mas muita diferença mesmo na hora pra você não partir ali do zero.

03:44

A própria IA vai ajudar,

03:45

você vai ter que ir editando junto, ou seja,

03:48

não é um trabalho que você faz em uma hora, tá?

03:52

Eu quando fiz essa skill aqui pra... Pra dar o exemplo pra esse nosso projeto,

03:56

eu gastei aí, sei lá, dois dias brincando, mexendo, fazendo bastante experiência,

04:00

mas também pra ficar um pouco mais didático aí pra todo mundo, tá?

04:03

Então essa aqui é a primeira dica pra vocês na

04:06

hora de vocês criarem a skill pra conseguir trabalhar,

04:10

fechou? Então comece por aí,

04:12

desde que você já tenha a ideia da arquitetura do software na sua cabeça.

04:16

Isso aí não vai brotar do nada. Se você não entender nada sobre isso,

04:21

aí você pode pedir pra ele ajudar.

04:23

a te ensinar a criar uma arquitetura decente. Assim,

04:26

é muito complexo porque vai depender muito de como cada um trabalha.

04:30

Eu tô partindo do princípio que você já tem,

04:32

você já sabe como é que você trabalha e você pode pegar um projeto que já

04:36

existe e ir pedindo pra ele criar uma skill baseada nos padrões que você já tem.

04:41

Isso pode ajudar bastante também. Fechou?

## Resumo IA

**Abreviações**
*   **DDD**: Domain-Driven Design
*   **IA**: Inteligência Artificial

**Resumo**
A aula aborda a criação eficiente de "skills" para agentes de IA no contexto de desenvolvimento de software e arquitetura. O objetivo principal é transformar o conhecimento implícito de um projeto em instruções explícitas para a skill, utilizando um processo de entrevista conduzido pelo próprio agente, em vez de escrever regras manualmente.

O fluxo recomendado começa com o uso de uma skill pronta para entrevistas, como "Grill Me", ou um "Plan Mode" equivalente no agente. O instrutor demonstra o processo iniciando com um prompt simples que especifica a stack (ex: TypeScript, Next.js), decisões arquiteturais (ex: back-end separado com Clean Architecture e DDD) e o tipo de ajuda desejada (regras, convenções, anti-patterns, camadas arquiteturais).

Após o prompt, o agente analisa o codebase e inicia uma série de perguntas para descobrir convenções, camadas e restrições do sistema. É fortemente recomendado incluir um projeto de exemplo, um "hello world" ou o scaffolding padrão do projeto no repositório para que o agente possa inspecionar e extrair padrões concretos. Isso reduz a ambiguidade e evita que a skill seja baseada apenas em suposições genéricas. A fase de perguntas pode ser extensa, visando coletar detalhes suficientes para gerar um primeiro draft coerente da skill, que servirá como base editável para refinamento iterativo. O processo é colaborativo entre IA e desenvolvedor, exigindo edição manual e validação contínua.

**Pontos de atenção**
*   A criação de skills é mais eficiente quando o agente conduz uma entrevista sobre o projeto, em vez de começar escrevendo regras manualmente.
*   Utilize uma skill pronta para entrevistas (ex: "Grill Me") ou um "Plan Mode" equivalente no seu agente para iniciar o processo e estruturar a coleta de contexto.
*   Forneça um prompt inicial conciso, mas com informações cruciais: stack tecnológica (ex: TypeScript, Next.js), decisões arquiteturais (ex: back-end separado com Clean Architecture e DDD) e o tipo de ajuda desejada (regras, convenções, anti-patterns, camadas arquiteturais).
*   Inclua um projeto de exemplo, um "hello world" ou o scaffolding do seu projeto no repositório. Isso fornece ao agente evidências concretas dos padrões desejados, diminuindo a dependência de descrições textuais abstratas e aumentando a independência do agente.
*   Se o agente analisar um codebase que já contém uma skill madura, o processo ficará enviesado. Para criar uma *nova* skill, exponha apenas exemplos representativos sem antecipar a resposta completa.
*   Esteja preparado para uma fase de perguntas extensa do agente, pois é fundamental para levantar detalhes e transformar preferências vagas em instruções operacionais.
*   O primeiro draft da skill é apenas uma base; o trabalho exige refinamento incremental, edição manual, experimentação e validação contínua, podendo levar horas ou dias.
*   É crucial que o desenvolvedor já possua uma noção arquitetural mínima. A skill formaliza e operacionaliza esse entendimento, não o substitui ou o cria do zero.
*   Aproveite projetos existentes como referência para que o agente extraia e organize padrões já estabelecidos, garantindo que a skill seja aderente à prática real da equipe.
*   Mesmo um "hello world" ou uma estrutura mínima do projeto evita o custo de começar do zero e orienta a entrevista e a escrita da skill.