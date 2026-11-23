Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17775)

## Resumo da aula

O PRD organiza o Videomax como um produto de uso individual, com biblioteca privada, contas isoladas e processamento assíncrono de vídeos. O fluxo central combina upload por drag and drop, transcrição automática, sumarização e busca no conteúdo processado. Essa descrição não é técnica por implementação; ela delimita o comportamento esperado do produto e o que precisa existir para o usuário final.

As personas definem para quem o sistema está sendo construído e condicionam decisões de interface e escopo. Aqui, o foco recai sobre criadores de conteúdo, profissionais, estudantes e usuários comuns que precisam arquivar e consultar vídeos próprios. O profile complementa isso ao explicitar o contexto de uso: acesso por desktop ou laptop, espera de alguns minutos pelo processamento e preferência por uma experiência clean, minimalista e sem prioridade para mobile neste momento.

Retomando a estrutura do PRD já estabelecida, as user stories são o ponto em que o comportamento do sistema vira uma sequência explícita de interações esperadas. Elas descrevem o que visitante, usuário e sistema precisam conseguir fazer: ver a landing page, criar conta, autenticar, fazer logout, enviar vídeos, acompanhar progresso e consumir o resultado processado. Isso importa porque as features deixam de ser blocos soltos e passam a ser justificadas por fluxos reais de uso.

As user stories descrevem a intenção e a interação; as funcionalidades detalham capacidades concretas que precisam existir para sustentar essas histórias. No caso da landing page, por exemplo, a história fala em entender o valor do produto e criar conta com facilidade, enquanto a funcionalidade explicita rota pública, nome do produto, supporting paragraph, CTA e link de login. Essa separação evita confundir necessidade do usuário com decisão de implementação.

A experiência do usuário aparece no PRD como comportamento observável, não como refinamento visual de front-end. O documento registra que o usuário deve conseguir acessar a página, localizar a CTA, navegar, criar conta e autenticar sem fricção desnecessária. No mesmo nível, o tratamento de erro precisa estar especificado: credenciais inválidas, conta duplicada e senha fraca não são detalhes secundários, mas parte do contrato funcional do sistema.

Retomando o cenário de upload já mapeado nas histórias, o vídeo enviado dispara um fluxo em background que valida regras, chama o OpenAI Whisper, gera transcrição, produz sumário com GPT-4 Nano e expõe o resultado ao usuário. O PRD também registra requisitos operacionais visíveis, como exibir progresso, manter o item na biblioteca durante o processamento e aplicar retry de três tentativas. Isso transforma um simples “fazer upload” em uma cadeia coordenada de comportamentos dependentes.

Lembra daquelas features já identificadas no PRD? Aqui elas deixam de ser independentes, porque o upload precisa prover o path do vídeo para outras partes do sistema continuarem o processamento. Essa relação de dependência é essencial para desenvolvimento paralelo: sem ela, cada feature pode funcionar isoladamente e ainda assim falhar quando integrada. O diagrama de dependências existe justamente para mostrar o que pode ser feito em paralelo, o que precisa vir antes e qual prioridade cada bloco recebe.

A seção out of scope não serve apenas para documentação passiva; ela limita o espaço de ação da IA e reduz deriva de implementação. Ao declarar explicitamente o que o sistema não terá, o PRD evita que o agente preencha lacunas com inferências indevidas. Em SDD, restringir é tão importante quanto descrever, porque a especificação precisa orientar tanto o que construir quanto o que não construir.

Critério de aceitação funciona como contrato de validação: cada feature precisa satisfazer condições mínimas observáveis para ser considerada pronta. Esses critérios são derivados das user stories, das funcionalidades, da experiência esperada e do que ficou fora de escopo. Além dos critérios por feature, entram os de cross-feature integration, que garantem que uma feature se conecte corretamente à outra em vez de apenas “existir” de forma isolada.

Retomando o problema de integração já discutido anteriormente, o ponto decisivo aqui é tornar essa conexão verificável dentro do próprio PRD. Quando os critérios de aceitação descrevem como dependências se encontram, o documento deixa de listar partes do sistema e passa a especificar continuidade de fluxo. Em SDD, isso é o que impede que landing page, autenticação, upload, biblioteca e processamento funcionem como ilhas desconectadas.

## Transcrição

00:00

Bom, pessoal, o PRD gerado aqui para a gente. Então,

00:05

olha só, o PRD Videomax, ele está trabalhando.

00:08

O Videomax é uma plataforma web que deixa usuários individuais

00:12

fazer upload de vídeos pessoais e automaticamente recebe um timestamp,

00:17

ou seja, a transcrição.

00:19

Gerada por IA com um resumo do conteúdo e

00:22

também o cara pode fazer a busca nas transcrições,

00:27

no próprio material, pode ser para estudantes,

00:29

para profissionais que querem consumir horas de aulas gravadas,

00:35

reuniões, etc. O produto é organizado na área de uma forma privada,

00:40

single user mode.

00:41

As contas são de forma isolada,

00:43

tem um processo de drag and drop para o vídeo e o background,

00:48

o processo de transcrição de background que vai acontecer,

00:53

vai validar as regras, vai chamar o OpenAI Whisper,

00:58

vai fazer a transcrição, vai gerar o sumário, vai utilizar o GPT-4 Nano.

01:04

Quando processar o processo completo, o usuário consegue ver ali.

01:08

Então, basicamente... Tem uma parte de administração, ou seja,

01:12

quem é administrador vai ter ali um ex-admin para ele. Daí tem problema,

01:17

oportunidade, eu não vou ficar passando por muitos desses aspectos,

01:21

mas aqui tem interessante que eu falei na hora da geração,

01:25

quem que vai ser? São criadores de conteúdo, profissionais,

01:28

estudantes e usuários comuns que querem ter arquivos dos vídeos deles e etc.

01:35

Então, eu coloquei esses três tipos de persona.

01:39

E aqui tem o profile, ou seja,

01:42

o perfil dessas pessoas normalmente como que

01:45

elas trabalhariam dentro desse nosso sistema. Ou seja,

01:49

tem que ter uma forma simples de fazer um drag and drop nas interfaces,

01:53

não esperando compatibilidade mobile nesse momento.

01:57

Tem que priorizar uma forma clean, minimalista de experiência.

02:03

Tem que esperar alguns minutos para fazer a transcrição,

02:07

e acessar a plataforma através de um desktop,

02:10

um laptop, com login e senha ali trabalhando.

02:15

Coisas importantes aqui são objetivos.

02:18

Então, o objetivo principal é entregar, prover,

02:21

organizar e manter e vai habilitar uma área de

02:24

admin onde a gente pode administrar os usuários.

02:27

Métricas de sucesso e as user stories.

02:31

Galera, aqui que eu acho que é uma das partes mais importantes desse nosso PRD.

02:37

Porque a partir dessas user stories, na realidade,

02:40

elas foram mapeadas através das features que ela acaba utilizando.

02:45

Então, a landing page,

02:47

como um visitante, eu quero ver uma landing page minimalista,

02:52

com um clear value proposition,

02:55

que eu consiga entender o que a plataforma faz.

02:58

Como visitante, eu quero poder criar uma conta,

03:01

ou seja, ter uma call to action para criar uma conta,

03:05

ali, sem eu ter que ficar procurando muito,

03:07

e retornar ao visitante um link de login no topo ali para ele.

03:13

Ali é, como sistema de autenticação,

03:16

Eu, como visitante, quero me registrar com e-mail e senha,

03:19

Então, eu posso iniciar o uso da plataforma. Eu, como usuário,

03:22

Eu quero poder fazer o login com as minhas

03:23

Credenciais para acessar a minha private library. Eu, como usuário,

03:27

Eu quero poder fazer o logout. Então, se você perceber, são as histórias de usuário. Ou seja,

03:33

Aqui, eu estou contando basicamente passo a passo tudo que o sistema vai poder.

03:38

Então, ó, vídeo upload. Como usuário, eu quero poder fazer o drag na drag zone.

03:42

Eu quero ver o progresso do que está sendo feito no background do meu vídeo, né?

03:46

Quando eu começo a subir. Como usuário,

03:49

Eu quero poder bloquear e limpar essa mensagem ou...

03:54

Principalmente quando der ali passado os 2 GB. Como usuário,

03:58

Eu quero que fique visível o vídeo na minha

04:01

Library enquanto está sendo feito o upload,

04:04

Colocando o que está em processamento.

04:06

Na minha Video Library, eu quero poder fazer isso.

04:09

Para organizar minhas pastas, eu quero ter isso. Para organizar minhas tags,

04:14

Eu quero ter isso. Para eu fazer o processo de background,

04:17

Então, ele fala como sistema, e não mais como usuário,

04:21

Eu quero automaticamente pegar cada novo upload,

04:24

Fazer a validação, transcrição,

04:26

Sumarização e geração para o usuário final poder ver o vídeo.

04:29

Como sistema, eu quero fazer um retry de três vezes.

04:33

Como usuário, eu quero poder agora aqui ver, validar e transcrever. Então,

04:39

Olha só que interessante como acaba gerando tudo isso. Então,

04:44

Aqui, basicamente, são as features que a gente tem.

04:48

Mas, se você olhar...

04:52

A gente não está falando necessariamente de feature.

04:54

Nós estamos falando de stories de usuário,

04:57

Como que o usuário interage com o sistema.

04:59

Porque as funcionalidades, elas ficam aqui. Funcionalidade 1, capacidades.

05:06

Preciso de uma rota pública, nome do produto,

05:11

Short supporting paragraph,

05:14

Chamada para ação, login, minimalista.

05:18

A gente não está falando de qualidade front-end.

05:21

Esse aí é um outro aspecto que a gente vai poder ver utilizando outras ferramentas.

05:27

Eu não estou focando em zero em qualidade de front-end,

05:31

Onde a gente poderia sim, completamente, fazer dando outras especificações.

05:36

A experiência que eu espero, que o usuário consiga acessar,

05:41

Ver a CTA, o Call to Action, que ele consiga navegar,

05:45

Ver a barra, que ele consiga criar a conta,

05:47

Que ele consiga clicar para poder fazer a autenticação no login.

05:50

A autenticação. O que vai ter as capacidades? Ou seja,

05:54

Quais são essas funcionalidades? Qual é a experiência que o usuário vai ter?

05:59

Erro. Quando as credenciais estiverem inválidas.

06:02

Tem que ter e-mail e password inválido.

06:06

Quando ele duplicar, uma conta já existe.

06:09

O password está fraco. Então, é uma forma de trabalhar com erro. Video upload.

06:15

Aqui, a gente vai começar a entrar em relação à dependência entre features. Ou seja,

06:21

Para eu poder fazer o vídeo upload,

06:22

Eu tenho que prover o path do vídeo para

06:30

Diversas outras features. Eu não quero entrar nesse aspecto ainda,

06:33

porque a gente vai entrar quando a gente for fazer o desenvolvimento em paralelo.

06:36

Mas basicamente aqui a gente tem as features,

06:38

todas que vão ser desenvolvidas com todos os detalhes dela.

06:44

Perceba que os nossos detalhes aqui, eles são extremamente, não são técnicos.

06:49

Grande parte disso não são técnicos de forma nenhuma.

06:52

A administração, ela tem detalhes muito básicos, principalmente de rotas.

06:56

E aqui o que não vai ter no nosso sistema de forma específica.

06:59

Aqui está out of scope para garantir que a

07:02

IA não tenha que fazer absolutamente nada.

07:05

E aqui tem o gráfico de dependências das features.

07:09

O que eu posso fazer junto, o que eu posso fazer em paralelo e tudo mais,

07:13

e qual o nível de prioridade que ele traz baseado em toda

07:17

aquela entrevista e ele gera um diagrama dessas dependências aqui para a gente.

07:23

E aqui a gente entra nos aspectos mais importantes,

07:27

que é o critério de aceitação. O que significa?

07:30

É uma forma de eu conseguir validar,

07:33

é um contrato de validação para garantir se o sistema está funcionando. Para cada feature,

07:38

eu tenho que conseguir fazer com que isso funcione.

07:41

Isso aqui vem de onde? Vem das nossas histórias de usuário,

07:45

das features, vem do que está fora de escopo,

07:48

e da experiência que a gente espera. Para cada feature,

07:52

esses critérios de aceitação são mínimos que a gente precisa.

07:56

E aqui eu não estou falando necessariamente só em navegação.

07:59

Então, aqui tem por feature, mas

08:02

também você vai ver que eu tenho cross features integration. Ou seja,

08:06

são critérios de aceitação onde eu garanto que uma feature vai grudar na outra.

08:11

E essa é a maior parte onde grandes sistemas

08:16

e frameworks de SDD acabam deixando o passar batido,

08:20

onde as features não se conversam. Com esses critérios de aceitação dessa forma,

08:25

eu consigo mostrar a dependência de uma feature na outra,

08:28

fazendo com que uma fique colada na outra,

08:30

e para isso eu coloco os critérios de

08:33

como eu faço essas dependências se encontrarem. Então,

08:36

a gente vai ver isso aí com calma ali nos nossos,

08:43

como se diz?

08:45

Nos nossos gráficos ali do PRD. Eu sei que está bastante teórico,

08:52

mas a gente já vai começar a colocar ali a mão na massa.

08:55

Mas, novamente, galera, a gente está falando sobre SDD,

08:59

a gente está falando sobre especificação.

09:00

Isso aqui é a parte mais importante de tudo que a gente vai desenvolver.

09:04

Vem a partir de uma especificação,

09:06

você tem que entender isso aí com clareza. Então, vamos seguir,

09:11

porque tem bastante coisa aí para a gente ver.

## Resumo IA

**Abreviações**
*   **PRD:** Product Requirements Document
*   **IA:** Inteligência Artificial
*   **CTA:** Call to Action

**Resumo**
Esta aula focou na importância e na estrutura de um PRD (Product Requirements Document) como documento fundamental para a especificação e desenvolvimento de software. O objetivo central foi demonstrar como o PRD organiza as informações de um produto, neste caso, o "Videomax" – uma plataforma web de uso individual com biblioteca privada, contas isoladas e processamento assíncrono de vídeos (upload via drag and drop, transcrição automática por IA, sumarização e busca no conteúdo processado).

O fluxo explicado pelo instrutor detalha a construção do PRD a partir da definição do produto e seu público. Inicialmente, são estabelecidas as **personas** (criadores de conteúdo, profissionais, estudantes, usuários comuns) e seus **profiles** (acesso por desktop/laptop, espera de minutos para processamento, interface clean e minimalista, sem prioridade mobile). A partir daí, o PRD se aprofunda com **user stories**, que descrevem as interações esperadas do usuário e do sistema (e.g., ver landing page, criar conta, autenticar, fazer logout, enviar vídeos, acompanhar progresso e consumir conteúdo processado).

As **funcionalidades** são detalhadas como capacidades concretas que sustentam as user stories, distinguindo a intenção do usuário da decisão de implementação. A **experiência do usuário** no PRD é abordada como comportamento observável, não como refinamento visual de front-end, incluindo a especificação de **tratamento de erros** (e.g., credenciais inválidas, conta duplicada, senha fraca). O fluxo de processamento de vídeo é mapeado, envolvendo validação, o uso do **OpenAI Whisper** para transcrição e **GPT-4 Nano** para sumarização, além de requisitos operacionais como exibição de progresso e retries.

São introduzidos o conceito de **dependência entre features**, essencial para o desenvolvimento paralelo e a integração do sistema, e a seção **out of scope**, que define explicitamente o que o sistema *não* terá para guiar a implementação e evitar inferências indesejadas. A aula conclui com os **critérios de aceitação**, que servem como contrato de validação para cada feature e, crucialmente, incluem **critérios de integração cross-feature** para assegurar que as partes do sistema se conectem e funcionem de forma coesa, em vez de atuar como "ilhas desconectadas".

**Pontos de atenção**
*   **PRD define comportamento, não implementação:** O documento delimita o comportamento esperado do produto e o que precisa existir para o usuário final, sem ser um guia técnico de implementação.
*   **Diferença entre User Stories e Funcionalidades:** User stories descrevem a *intenção* e a *interação* do usuário, enquanto as funcionalidades detalham as *capacidades concretas* que o sistema precisa ter para atender a essas histórias. Evite confundir necessidade do usuário com decisão de implementação.
*   **Experiência do Usuário (UX) como comportamento observável:** No PRD, a UX é registrada como comportamento esperado (acessar, localizar CTA, navegar, criar conta, autenticar sem fricção), e não como um refinamento visual de front-end.
*   **Tratamento de erros é parte do contrato funcional:** Especificar como o sistema reage a credenciais inválidas, contas duplicadas ou senhas fracas não são detalhes secundários, mas sim componentes críticos do contrato funcional do sistema.
*   **Dependências são cruciais para a integração:** Entender e documentar as dependências entre features é vital para o desenvolvimento paralelo e para garantir que o sistema funcione como um todo integrado, prevenindo falhas quando as features são combinadas.
*   **"Out of scope" é uma ferramenta ativa:** Declarar explicitamente o que o sistema *não* terá ajuda a limitar o escopo, orientar o desenvolvimento e evitar que a equipe preencha lacunas com inferências indevidas. Restringir é tão importante quanto descrever.
*   **Critérios de aceitação devem incluir integração cross-feature:** Além dos critérios para features individuais, é fundamental especificar como as dependências se encontram e como as features se conectam corretamente. Isso impede que diferentes partes do sistema funcionem como "ilhas desconectadas" e garante a continuidade do fluxo.
*   **A especificação (via PRD) é a parte mais importante:** O instrutor reitera que o PRD e a especificação são o alicerce de todo o desenvolvimento de software.