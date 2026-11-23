Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17979)

## Resumo da aula

Retomando os artefatos já gerados pelo fluxo, spec.md concentra a especificação geral da feature, enquanto plan.md organiza a implementação em etapas. O avanço aqui está no contract.md, que deixa de ser apenas um complemento e passa a funcionar como referência operacional para execução e validação. Ele conecta o que deve existir no ambiente, como a feature será verificada e quais evidências precisam ser observadas. Isso reduz ambiguidade tanto para quem implementa quanto para quem avalia.

contract.md explicita os pré-requisitos mínimos para que a feature possa ser executada e testada. No exemplo da landing page, isso inclui um Next.js Dev Runtime ativo no VideoMax Web na rota / e um browser real operado via Playwright CLI. A utilidade prática é direta: se o ambiente não atende ao contrato, a avaliação nem começa, porque o sistema não está em condições válidas de teste. Em projetos mais complexos, esse mesmo documento precisa listar dependências adicionais como mensageria, brokers e microserviços.

O contrato funciona como um checklist que pode ser entregue a alguém sem conhecimento prévio do sistema. Essa pessoa consegue verificar se possui runtime, serviços auxiliares e ferramentas suficientes antes de tentar validar a feature. O ganho está em transformar conhecimento implícito do time em instruções explícitas e auditáveis. Sem isso, falhas de ambiente podem ser confundidas com falhas de implementação.

Além do ambiente, o contrato registra os gates de qualidade que a feature precisa satisfazer. Isso inclui comandos e verificações como execução com npm, lint com ESLint e build do projeto. Esses gates definem um piso técnico de aceitação antes mesmo da inspeção funcional detalhada. A consequência é que a validação deixa de depender apenas de percepção visual e passa a incluir critérios objetivos de integridade do código.

O manifesto de cobertura declara o que precisa ser verificado e quem cobre cada parte da feature. No caso apresentado, a cobertura está associada à UI da feature 01, identificada como Public 01. Esse mapeamento evita lacunas, porque cada comportamento esperado passa a ter uma superfície de validação associada. Em vez de testar “a página” genericamente, o contrato delimita exatamente quais aspectos da interface entram no escopo.

A cobertura é organizada por surfaces, isto é, camadas ou áreas observáveis do sistema. Na surface de UI com public access, o contrato define o cenário de um visitante anônimo acessando / sem cookies e sem VideoMax Session. A partir desse estado inicial, a validação verifica comportamentos concretos da landing page, como carregamento da rota, exposição do produto e elementos visuais esperados. Essa estrutura aproxima o contrato de um teste orientado a comportamento, mas com foco em aceitação operacional.

A landing page não é validada por uma descrição vaga de “estar correta”, e sim por sinais observáveis. O contrato exige, por exemplo, presença de CTA de registro, login na navegação superior, comportamento de redirecionamento ligado à autenticação e aderência da identidade visual. Cada item serve como evidência verificável de que a feature atende ao que foi especificado. Quanto mais critérios de aceitação existirem, mais extenso e detalhado o contrato tende a ficar.

O contrato não serve apenas para o avaliador final; ele também orienta o agente implementador. Quem implementa já sabe quais condições de ambiente precisa respeitar, quais gates técnicos precisa passar e quais comportamentos serão cobrados depois. Isso alinha construção e validação em torno do mesmo documento, o que é especialmente útil no uso conjunto de Harness e SDD. O resultado é um fluxo em que a feature nasce com critérios de execução e aceitação já formalizados.

## Transcrição

00:01

Bom, pessoal, é o seguinte, né? Ele rodou agora aqui o nosso spec writer,

00:06

né? E ele gerou aqui a nossa primeira feature 01,

00:09

que é a minha landing page. Se você olhar agora na minha landing page,

00:14

eu tenho a minha spec.md, tá?

00:18

Deixa eu fechar o meu cloud aqui, vai.

00:21

Vou fechar ele só para a gente ter mais espaço na tela.

00:24

Eu tenho esse meu spec.md.

00:27

que no final das contas vai trazer a especificação do

00:30

que eu preciso fazer de forma geral.

00:32

Então, vai trazer tudo isso aqui, arquitetura e tudo mais.

00:36

Aí eu tenho o meu plan.md,

00:38

que ele vai trazer para mim como que eu vou fazer a implementação.

00:43

Passo 1, estágio 2,

00:44

estágio 3, aqui para mim. E daí, por último,

00:49

eu tenho aqui o meu contract.md.

00:52

Esse meu contract.md, que de forma geral, ele é o cara.

00:57

Porque nesse caso aqui, o que ele vai fazer?

01:00

Ele vai falar, ó,

01:01

essas são as condições de ambiente que eu preciso pra deixar esse cara rodando.

01:07

Então, de forma geral, ele tá falando, olha,

01:10

qual é o runtime service que eu preciso?

01:12

Eu preciso do Next.js Dev Runtime rodando no

01:16

VideoMax Web na página barra para eu conseguir rodar.

01:20

E um browser real para eu fazer a avaliação ali para mim usando o Playwright CLI. Galera,

01:25

isso aqui é muito importante e eu vou dizer

01:27

para vocês que deu um trabalhão para fazer. Por quê?

01:30

Às vezes eu estou desenvolvendo um projeto mais complexo.

01:32

Eu preciso ter não só o Next, eu preciso ter RabbitMQ,

01:37

eu preciso ter Kafka, eu preciso de um microserviço ali,

01:39

outro aqui. E aí, nesse caso, o que acontece?

01:43

Esse camarada aqui,

01:44

ele tem que ter tudo que é necessário para que ele consiga testar.

01:50

Então, imagina que você está dando um documento para uma pessoa,

01:53

que não sabe nada do seu sistema, e nesse documento tem uma checklist falando,

01:57

olha, você precisa ter isso de pré-requisito.

02:00

E daí na hora que você vê esses pré-requisitos,

02:02

se eu consigo atender, eu consigo fazer.

02:04

Se eu nem conseguir chegar nesses pré-requisitos,

02:07

eu nem vou conseguir testar. Esse que é o grande ponto.

02:10

Então aqui tem as configurações que ele trouxe aqui para mim,

02:14

e os gates de qualidade.

02:16

Então ele está falando, para rodar esse cara, você vai rodar aqui o NPM,

02:20

você pode ter o S-Link. Você pode dar um build aqui nesse camarada aqui para rodar.

02:26

Então ele falou, esses são os gates de qualidade. E aqui,

02:29

a parte de cobertura, de manifesto de cobertura. O que isso significa?

02:34

A página tem que carregar a partir do barra.

02:38

Quem está cobrindo isso?

02:40

Então é uma cobertura baseada na parte de UI, Public 01,

02:45

ou seja, a feature 01 da parte de UI.

02:47

Daí a gente vai ver que cada feature, cada pedaço tem... os detalhamentos, ou seja,

02:53

O que vai ter nesse nosso manifesto para ser coberto,

02:56

Vai ser baseado em diversas surfaces, ou seja, em diversas camadas aqui.

03:02

Então, na camada de UI, public access, um visitante anônimo,

03:07

Ele é capaz de visitar essa página barra.

03:10

Given no cookies, ou seja, uma vez que o cara não tem nenhum cookie, etc.,

03:14

Em particular, no VideoMax Session. O cookie vai estar presente.

03:19

Quando ele acessar isso,

03:20

Ele vai ter que ver a página acessada,

03:26

Ele vai ter que ver que a página expõe o produto,

03:30

O top right, ele começa a dar esses detalhes.

03:33

Outro ponto, CTA, o register, vai ter que ter ali, ele vai ter que colocar.

03:38

O top navigation, vai ter que ter o login. A parte de redirecionamento,

03:42

Quando o cara fizer uma autenticação, ele pode ser autenticado.

03:46

A parte de identidade visual vai ter que estar batendo aqui com a página.

03:51

Então, basicamente,

03:52

Esse contrato nos ajuda a fazer com que quem for avaliar consiga garantir,

03:58

Mas não somente quem vai avaliar,

04:02

Mas também quem vai implementar essa feature. Então,

04:05

Isso aí que para a gente acaba sendo extremamente importante.

04:09

Esse documento de contrato, como é uma landing page simples, ele é bem pequeno,

04:14

Mas dependendo do nível de feature que você vai desenvolver,

04:17

E tem diversos critérios de aceitação,

04:19

Ele fica bem longo e acaba ficando bem complexo,

04:22

Por isso que gerar esses documentos não são tão fáceis assim,

04:26

E daí você pode aproveitar essa skill,

04:28

Mudar e adaptar para o seu uso no dia a dia. Nada perfeito,

04:32

Eu criei isso aqui muito mais para que a gente consiga ter essa guidance

04:37

De ter Harness e SDD simultaneamente para você

04:41

Aí conseguir criar aí os seus projetos,

04:43

Beleza? Então é isso aí, próximo passo que a gente vai,

04:46

A gente vai falar sobre o agente implementador, né?

04:49

O cara que vai realmente colocar a mão na massa e implementar,

04:52

Mas ele também vai ter guidance porque ele vai ter que seguir esse contrato também.

## Resumo IA

**Abreviações**
*   **CLI**: Command Line Interface
*   **NPM**: Node Package Manager
*   **ESLint**: ECMAScript Linter
*   **UI**: User Interface
*   **CTA**: Call To Action
*   **SDD**: Software Development Document (ou Documento de Desenvolvimento de Software)

**Resumo**
A aula retoma o fluxo de desenvolvimento de features, destacando os artefatos `spec.md` (especificação geral) e `plan.md` (plano de implementação), e avança para o `contract.md`. O objetivo central é transformar o `contract.md` de um mero complemento em uma referência operacional crucial para a execução e validação de features. Este documento tem a função de conectar o que deve existir no ambiente, como a feature será verificada e quais evidências são necessárias, visando reduzir a ambiguidade para implementadores e avaliadores.

O instrutor explica que o `contract.md` detalha os pré-requisitos mínimos de ambiente, como a necessidade de um Next.js Dev Runtime rodando em `VideoMax Web` na rota `/` e um browser real operado via Playwright CLI. Em cenários mais complexos, ele também lista dependências como mensageria (RabbitMQ, Kafka) e microserviços. Além disso, o contrato explicita os "gates de qualidade" que a feature deve satisfazer, incluindo comandos como `npm`, `ESLint` e `build`. Um manifesto de cobertura é incluído, declarando o que precisa ser verificado e quem cobre cada parte da feature, organizando a validação por "surfaces" (camadas ou áreas observáveis do sistema), como a UI de acesso público para um visitante anônimo. O fluxo de validação da landing page, por exemplo, é detalhado com verificações concretas como carregamento da rota, exposição do produto, presença de CTA de registro, login na navegação superior, comportamento de redirecionamento e aderência à identidade visual. O `contract.md` serve tanto para o avaliador final, como um checklist auditável, quanto para o agente implementador, alinhando a construção e a validação desde o início, especialmente útil na integração de Harness e SDD.

**Pontos de atenção**
*   **Redução de Ambiguidade**: O `contract.md` é fundamental para reduzir a ambiguidade, explicitando os pré-requisitos e critérios de aceitação tanto para quem implementa quanto para quem avalia.
*   **Pré-requisitos Ambientais**: Se o ambiente de teste não atender ao contrato (pré-requisitos mínimos), a avaliação da feature não deve sequer ser iniciada, evitando desperdício de tempo e recursos.
*   **Conhecimento Implícito vs. Explícito**: O contrato transforma o conhecimento implícito da equipe em instruções explícitas e auditáveis, prevenindo que falhas de ambiente sejam confundidas com falhas de implementação.
*   **Gates de Qualidade**: A definição de gates de qualidade no contrato estabelece um piso técnico de aceitação da feature, indo além da percepção visual e incluindo critérios objetivos de integridade do código.
*   **Cobertura Detalhada**: O manifesto de cobertura, organizado por "surfaces", evita lacunas na validação, garantindo que cada comportamento esperado tenha uma superfície de verificação associada.
*   **Alinhamento Implementação/Validação**: O `contract.md` orienta tanto o implementador (quais condições respeitar e o que será cobrado) quanto o avaliador, alinhando a construção e validação em torno de um documento comum, o que é valioso no uso de Harness e SDD.
*   **Complexidade do Contrato**: A extensão e complexidade do `contract.md` aumentam proporcionalmente ao número de critérios de aceitação e à complexidade da feature.
*   **Geração de Documentos**: A geração desses documentos detalhados pode ser um desafio, mas a habilidade de adaptá-los para o uso diário é um diferencial.