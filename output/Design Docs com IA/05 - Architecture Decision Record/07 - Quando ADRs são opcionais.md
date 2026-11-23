Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17124)

## Resumo da aula

Uma decisão continua forte candidata a ADR quando produz implicações relevantes em performance, segurança, custo, interoperabilidade ou manutenção; isso já foi estabelecido antes. A zona cinzenta aparece quando a escolha existe, mas seu efeito pode permanecer local, reversível ou já absorvido pela cultura técnica do time. Nesses casos, o critério deixa de ser “houve decisão” e passa a ser “essa decisão precisa virar memória arquitetural explícita”. O custo de documentar também entra na análise, porque registrar o óbvio consome tempo sem aumentar entendimento futuro.

Um padrão arquitetural local é uma convenção de implementação adotada dentro do contexto do time, como usar MVC, Clean Architecture ou arquitetura hexagonal como base recorrente. Se esse padrão já é o boilerplate normal da empresa e aparece de forma estável em todos os projetos, criar ADR tende a ser redundante, porque a decisão já está institucionalizada. O cenário muda quando há ruptura de paradigma: migrar de um MVC estrito para Clean Architecture combinada com arquitetura orientada a eventos altera responsabilidades, fronteiras e forma de evolução do sistema. Nesse ponto, a escolha deixa de ser convenção local e sobe para nível arquitetural, o que justifica ADR.

Entidades, agregados e regras de negócio isoladas normalmente não pedem um ADR por item, porque fazem parte da evolução natural do domínio e mudam com frequência. O que pode merecer registro é o estilo de modelagem adotado, isto é, a forma estrutural escolhida para organizar o domínio. Retomando o cenário de migração de abordagem, usar DDD com decisões explícitas sobre Aggregate Root, árvore de dependências e Value Objects pode justificar ADR quando isso representa uma forma incomum ou deliberadamente diferente de modelar. O documento não serve para catalogar cada regra de negócio, mas para registrar a opção estrutural que orienta várias delas.

Estrutura de pastas e módulos costuma ficar melhor documentada em artefatos operacionais, como README ou CONTRIBUTING.md, porque esses documentos orientam contribuição cotidiana e podem ser atualizados com menor atrito. Um ADR só agrega valor aqui quando a organização expressa uma decisão arquitetural mais profunda, e não apenas uma convenção de navegação do repositório. Se a estrutura apenas reflete um padrão já conhecido do time, formalizar isso em ADR tende a gerar burocracia. Se a organização materializa uma nova separação de responsabilidades ou um novo modelo de modularização, o caso pode subir de nível.

Escolhas como usar Strategy, Adapter ou determinadas interfaces não viram ADR automaticamente só por envolverem design. O ponto de elevação é a existência de contratos públicos: quando a interface passa a ser consumida por outros sistemas, APIs ou SDKs, a decisão deixa de ser interna e cria dependências externas. Nesse caso, o racional da escolha precisa sobreviver ao tempo, porque mudanças futuras podem quebrar consumidores ou gerar acoplamentos difíceis de desfazer. Sem contrato público, a mesma decisão pode continuar sendo apenas detalhe local de implementação.

Um SDK é um bom exemplo de contexto em que contratos públicos pesam mais do que o tamanho do código. Mesmo que a implementação interna seja simples, a superfície pública define como terceiros integram com o sistema e, por isso, carrega impacto arquitetural desproporcional. Registrar em ADR por que certos contratos foram expostos, e por que aquela abordagem foi escolhida, reduz ambiguidade para manutenção e evolução. Nem todo SDK exigirá isso, mas a presença de dependentes externos torna o caso muito mais forte.

Parâmetros como timeout e batch size normalmente pertencem a feature docs, low-level design ou high-level design, porque são ajustes operacionais sujeitos a variação frequente. Eles só merecem ADR quando deixam de ser tuning local e passam a representar uma restrição sistêmica ou uma estratégia arquitetural incomum. Se um timeout crítico sustenta uma carga pesada, impõe comportamento fora do padrão ou força compensações relevantes, o parâmetro deixa de ser mera configuração e vira parte do desenho arquitetural. O critério não é o número em si, mas o papel estrutural que ele desempenha.

A mesma escolha pode merecer ADR em um projeto e não merecer em outro, porque maturidade do time, padrões já consolidados e tipo de sistema alteram o custo-benefício do registro. Em um ambiente onde todos já operam com o mesmo stack e o mesmo boilerplate, documentar novamente a convenção pouco acrescenta. Em um time que está migrando de paradigma, a documentação ajuda a alinhar linguagem, fronteiras e expectativas. O julgamento correto depende menos da tecnologia isolada e mais do quanto a decisão precisa ser explicada para continuar sendo compreendida.

Documentar demais transforma ADR em burocracia; documentar de menos apaga o raciocínio das decisões realmente relevantes. O equilíbrio está em evitar tanto o documento óbvio quanto a omissão de mudanças estruturais. Retomando os exemplos, registrar a migração de MVC para DDD com Clean Architecture faz sentido porque houve ruptura de abordagem; registrar a troca de Repository por DAO em um microserviço pequeno com duas tabelas tende a desperdiçar esforço. O valor do ADR aparece quando ele preserva contexto que não permanecerá evidente no código ou na cultura do time.

## Transcrição

00:00

Bom, pessoal, só pra terminar o que a gente falou no vídeo anterior, ou quando você deve utilizar uma Architecture Decision Record, use isso como regra geral. E quando eu uso a palavra regra geral, eu coloquei até entre aspas aqui pra você, tá? Porque a sua decisão tem implicações em performance, segurança,

00:22

custo, interoperabilidade ou manutenção gere um ADR. Então, se eu poderia trazer um resumo de todos aqueles itens que eu coloquei, você vai perceber que tem muito a ver com isso que eu acabei de trazer aqui pra vocês. Por outro lado, o que que acontece?

00:42

Quando que um ADR é opcional? Ou seja, ele depende muito do contexto do time, do projeto, do negócio, tá? Então é o seguinte, padrão arquitetural local. Aqui a gente começa a falar muito já de implementação um pouco mais baixo nível. Ou seja, eu estou trabalhando com MVC, Clean Architecture, arquitetura hexagonal, etc. Então assim,

01:06

Eu devo documentar isso? Eu devo criar uma DR para isso? Por isso que eu digo que é opcional. Por exemplo, se a escolha for padrão do time e já é dotada em todos os projetos, eu não vou criar uma DR. Agora, se for uma mudança de paradigma, sim. Vou dar um exemplo. Em todos os projetos, a gente trabalha com MVC. Model View Control ali, mas assim, de uma forma muito estrita mesmo, tá?

01:32

E, de repente, eu vou falar, olha, a gente vai mudar isso para trabalhar com Clean Architecture. E eu vou mudar isso também para trabalhar com a arquitetura baseada em eventos. Meu, muda completamente. Eu devo registrar uma DR nesse caso?

01:53

Sim, provavelmente, porque não é o padrão da empresa, tá? Agora, não tem essa. Se todos os projetos da empresa seguem o mesmo boilerplate, usa sempre o mesmo banco de dados, usa sempre toda aquela história, você já está acostumado? Meu, não faz sentido algum você gastar seu tempo em fazer um documento óbvio, porque faz parte, inclusive, da cultura da empresa, tá? Outra coisa, modelagem de domínio.

02:20

Normalmente, você não precisa de uma ADR para uma entidade, um agregado, mas pode ter uma ADR para o estilo de modelagem adotado, tá? Então, o que isso significa? Meu, você não precisa, no final das contas, ficar registrando uma ADR por contas de regras de negócio. Por que regras de negócio mudam? Como que você vai mapear suas regras de negócio?

02:47

Provavelmente, você não precisa muito. Mas, eventualmente, eu estou dando um exemplo, se você vai trabalhar, por exemplo, com o Domain Driven Design, a forma de como que você vai criar a sua árvore de dependências, o seu Aggregate Root, como que você vai trabalhar com Vue ou seus velhos Objects, ou seja, às vezes você está trabalhando de uma forma um pouquinho diferente do que se costuma trabalhar, vale a pena, talvez, você registrar isso. Mas, lembrando que a gente já está entrando em pontos que, às vezes, é um pouquinho mais baixo nível, tá?

03:16

E não confunda, necessariamente, Domain Driven Design com arquitetura. Apesar de arquitetura tem a ver com Domain Driven Design, mas não necessariamente Domain Driven Design acaba sendo uma arquitetura

03:33

tão de baixo nível, tá? Mas isso aí é uma outra história, é para uma outra conversa. Organização de pastas e módulos, tá? Então, às vezes, a gente cria ADRs para mostrar como é que vai funcionar as nossas pastas, organizações e tudo mais. Isso é opcional, tá? Ou seja, eu não preciso às vezes criar uma ADR para isso. Às vezes, eu posso ter guidelines no meu software, né?

04:00

onde eu mostro o contributing a .md, um readme, mostrando como que é a estrutura do projeto. Então, não necessariamente isso precisa ser uma DR. Mas, se você criar uma DR, eu não vou dizer que isso também está errado, entendeu? Mas...

04:16

Como eu disse, opcional. Aí a gente tem alguns outros pontos. Decisões de design menores. Por exemplo, eu vou utilizar as seguintes interfaces para isso. Eu vou usar o padrão strategy para tomar essa decisão. Eu vou trabalhar com adapter para fazer isso.

04:35

Será que eu devo realmente criar uma ADR para isso? Depende. Por exemplo, se eu registrar apenas se isso influencia na arquitetura e contratos públicos, vale a pena eu registrar. Por quê?

04:50

Porque, como é uma interface pública, outros softwares podem utilizar, outras APIs podem chamar, tanto que são internas ou externas, mas é algo público. Registrar isso provavelmente é importante, porque gera muita dependência de outros softwares em cima dos seus.

05:07

Agora, se você está fazendo algo que você não vai ter essa necessidade a todo momento de outros sistemas ficarem acessando o seu sistema, outras interfaces, outros SDKs, não necessariamente você precisa registrar uma DR. Por isso que eu estou colocando como é opcional. Depende do seu contexto, depende do seu projeto. Imagina se eu estou fazendo um SDK, por exemplo.

05:32

Poxa, eu vou ter diversos contratos públicos. Eventualmente, eu vou criar uma DR para deixar claro a minha decisão arquitetural, por que esses contratos, dessa forma, eles realmente ficaram públicos e por que eu usei essa abordagem. Mas depende muito. Nem sempre eu preciso disso.

05:48

Outra coisa, configurações específicas. Vou trabalhar com o timeout da aplicação caso ele não consiga gerar uma nota fiscal em tanto tempo. O batch size, quantos documentos eu mando processar ao mesmo tempo. Eventualmente, eu posso falar, vou gastar 10 milissegundos para fazer isso, o meu batch size vai ser de 500. Eventualmente, eu posso registrar isso no meu

06:12

no meu documento de feature, no meu low-level design, no meu high-level design, depende muito, mas não necessariamente isso precisa ser uma DR, principalmente porque muitas dessas coisas acabam sendo bastante variáveis. Agora, se timeout na sua aplicação foi algo extremamente crítico, porque você está utilizando uma estratégia bem diferente para suportar uma carga, e ali você está fazendo algo extremamente

06:41

pesado, às vezes até quebrando alguns padrões, sem dúvida vale botar uma DR. Por isso que eu digo que é algo um pouco mais opcional, tá? Então, um exemplo aqui simples pra você. Criar uma DR pra utilizar a DDD em conjunto com o Clean Architecture faz sentido se o time migrará de um MVC tradicional pra essa abordagem.

07:01

Ou seja, se o time inteiro sempre trabalhou com MVC e eu tô mudando isso agora, o que vai acontecer? Provavelmente vale a pena uma DR. Porque pra eu tomar essa decisão, alguma coisa aconteceu.

07:12

Um outro exemplo, criar um ADR para usar repositório ao invés de DAO, ou seja, uma outra forma de persistência, um microserviço pequeno que pode não fazer sentido. Cara, provavelmente você não vai criar um ADR para esse. Ah, agora eu não estou usando um repository, estou usando o Data Access Object, um microserviço onde eu tenho duas tabelas de banco de dados. Meu, você vai gastar tempo à toa, na minha opinião, tá?

07:37

Agora, próximo vídeo, a gente vai falar quando nós não devemos usar ADR ou quando não faz muito sentido eventualmente, tá bom? Então vamos nessa.

## Resumo IA

**Abreviações**

- **ADR** — *Architecture Decision Record* (registro de decisão arquitetural)
- **MVC** — *Model-View-Controller*
- **DDD** — *Domain-Driven Design*
- **SDK** — *Software Development Kit*
- **README** — arquivo de documentação introdutória do projeto
- **CONTRIBUTING.md** — arquivo com orientações para contribuição no projeto
- **DAO** — *Data Access Object*
- **API** — *Application Programming Interface*
- **feature docs** — documentação de funcionalidade
- **high-level design** — desenho de alto nível
- **low-level design** — desenho de baixo nível

**Resumo**

A aula explicou quando uma decisão deve ou não ser registrada em um ADR, reforçando que a regra geral é usar ADR quando a escolha traz implicações relevantes em performance, segurança, custo, interoperabilidade ou manutenção. O instrutor destacou que, em muitos casos, a decisão existe, mas seu impacto é local, reversível ou já faz parte da cultura técnica do time; nesses cenários, documentar pode ser desnecessário e até burocrático. O critério central deixa de ser apenas “houve decisão” e passa a ser “essa decisão precisa se tornar memória arquitetural explícita”.

Foram apresentados exemplos de decisões arquiteturais locais e quando elas deixam de ser apenas convenções de implementação. Padrões como MVC, Clean Architecture e arquitetura hexagonal, quando já são o boilerplate padrão da empresa, normalmente não justificam ADR. Porém, uma mudança de paradigma — como migrar de MVC estrito para Clean Architecture combinada com arquitetura orientada a eventos — altera responsabilidades, fronteiras e a evolução do sistema, o que eleva a decisão ao nível arquitetural e torna o ADR adequado.

Na modelagem de domínio, o instrutor observou que entidades, agregados e regras de negócio, isoladamente, não costumam exigir ADR. O que pode merecer registro é o estilo de modelagem adotado, especialmente quando há uma forma incomum ou deliberadamente diferente de estruturar o domínio, como em decisões relacionadas a Aggregate Root, árvore de dependências e Value Objects dentro de um contexto de DDD. O foco do ADR não é catalogar regras de negócio, mas preservar a opção estrutural que orienta várias delas.

Também foi discutida a organização de pastas e módulos. Em geral, esse tipo de informação é melhor documentado em README ou CONTRIBUTING.md, pois são artefatos operacionais mais fáceis de atualizar e mais úteis para o dia a dia. ADR só faz sentido quando a organização de código representa uma decisão arquitetural mais profunda, como uma nova separação de responsabilidades ou um novo modelo de modularização.

Outro ponto abordado foi o uso de interfaces, Strategy e Adapter. Essas escolhas não viram ADR automaticamente, mas passam a merecer registro quando afetam contratos públicos e criam dependências externas, como em APIs, integrações com outros sistemas ou SDKs. O instrutor destacou que, quando há consumidores externos, a justificativa da decisão precisa sobreviver ao tempo, pois mudanças futuras podem quebrar compatibilidade ou gerar acoplamento difícil de desfazer.

Em seguida, ele tratou de configurações específicas, como timeout e batch size. Normalmente, esses parâmetros cabem melhor em documentação técnica de feature, high-level design ou low-level design, porque são ajustes variáveis. Eles só passam a justificar ADR quando deixam de ser tuning local e se tornam restrição sistêmica ou parte de uma estratégia arquitetural incomum, especialmente se sustentam carga pesada ou exigem compensações relevantes.

Por fim, foi reforçado que a mesma decisão pode ou não merecer ADR dependendo do contexto do projeto e da maturidade do time. Em ambientes com stack e boilerplate consolidados, documentar o óbvio é desperdício; em migrações de paradigma, o ADR ajuda a alinhar linguagem, fronteiras e expectativas. O equilíbrio está em evitar tanto a burocracia de documentar tudo quanto a omissão de decisões estruturais importantes.

**Pontos de atenção**

- Use ADR quando a decisão impactar de forma relevante:
  - performance
  - segurança
  - custo
  - interoperabilidade
  - manutenção
- Não transforme convenções já institucionalizadas em ADR apenas por formalidade.
- O contexto do time e do projeto é निर्णante; a mesma decisão pode ser relevante em um cenário e irrelevante em outro.
- Mudanças de paradigma justificam ADR com mais facilidade, especialmente quando alteram responsabilidades e fronteiras do sistema.
- Não registre ADR para cada entidade, agregado ou regra de negócio isolada; isso tende a gerar excesso de documentação.
- O que pode merecer registro é o estilo de modelagem adotado, quando ele for estruturalmente relevante ou incomum.
- Estrutura de pastas e módulos normalmente deve ficar em README, CONTRIBUTING.md ou documentação operacional, salvo quando representar decisão arquitetural mais profunda.
- Decisões de design menores, como escolha de Strategy, Adapter ou interfaces específicas, só justificam ADR se afetarem contratos públicos ou dependências externas.
- Em SDKs, APIs e integrações externas, contratos públicos têm peso arquitetural maior e merecem atenção especial.
- Parâmetros como timeout e batch size não devem ser documentados automaticamente em ADR; só quando forem parte de uma restrição sistêmica ou estratégia incomum.
- Evite documentar o óbvio: isso consome tempo sem aumentar entendimento futuro.
- Também evite o extremo oposto: omitir decisões estruturais faz o raciocínio arquitetural se perder com o tempo.
- ADR deve preservar contexto que não ficará evidente apenas olhando o código.