Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17233)

## Resumo da aula

Antes de finalizarmos esta disciplina sobre Design Docs, acho que vale a pena ter em mente e ter clareza sobre as categorias de Design Docs que podemos aplicar. Nosso foco aqui é o desenvolvimento, somos desenvolvedores, então nosso principal ponto é o que mais utilizamos no mundo do desenvolvimento. Por outro lado, existem categorias que não estão necessariamente ligadas ao desenvolvimento, mas que precisamos saber que, indiretamente, esses documentos podem existir.

Por conta disso, gerei uma categorização apenas para que vocês entendam os tipos de documento que podem existir e com os quais podem se deparar. Alguns desses documentos continuaremos vendo ao longo do curso, em outras disciplinas, mas o principal ponto é que vocês tenham mais clareza.

Separei as categorias da seguinte forma:

Documentações de Produto (não são exatamente design docs, na maioria das vezes):

Relevantes: PRD (Product Requirements Document)

Secundários: User Stories e Epics (dependem muito da área de produto)

Legados: FRD (Functional Requirements Document), cujo uso hoje não é tão ativo

Design e Arquitetura:

Relevantes: High-Level Design, Feature Design Doc, ADR (Architecture Decision Records), Modelo C4

Emergentes: AI Design Docs e Prompt Specs. Esses são documentos que antes não existiam e agora começam a surgir exatamente para que possamos desenvolver e desenhar aplicações utilizando IA. Vamos explorar isso quando abordarmos workflows com IA.

Secundários: RFCs (Request for Comments) — embora sejam extremamente importantes, especialmente em projetos open source, muitas definições são feitas apenas através de RFCs, não necessariamente via ADRs. Outro documento secundário, e raro de encontrar com clareza nas empresas, é o Low-Level Design, pois os projetos mudam tão rapidamente que esse tipo de documento pode ficar obsoleto facilmente.

Legados: TRD (Technical Reference Document) e LLD no formato RUP, que eram utilizados antigamente.

Documentos de Conhecimento e Referência:

Relevantes: Engineering Guidelines (que acabamos de ver) e Security Design Doc

Emergentes: Documentos de como trabalhar com Evaluation

Legados: Test Plan e Test Case formal — antigamente muito utilizados para planejamento de testes, especialmente na área de QA. Embora os processos de teste continuem importantes, esses documentos específicos são bastante datados.

Documentos Operacionais e de Infraestrutura:

Operacionais relevantes: Runbooks e Playbooks, que orientam como executar a aplicação em produção e o que fazer quando algo dá errado.

Operacionais emergentes: Documentos de Observabilidade — antigamente não se falava nisso, hoje é item obrigatório, mas ainda não vemos documentações tão específicas sobre o tema. Abordaremos isso ao longo do curso, inclusive na parte de SRE.

Infraestrutura secundários: Design Docs focados em infraestrutura e documentos sobre CI/CD. Coloco como secundários porque, no ponto de vista do desenvolvimento, não somos necessariamente os responsáveis pela criação da infraestrutura. Obviamente, se você atua como DevOps ou SRE, isso é diferente, mas no contexto de codificação, esses documentos são secundários.

Essa categorização é baseada na minha experiência ao longo dos anos e em conversas com pessoas de grandes empresas. Não espero que 100% das pessoas concordem com essa categorização ou com os documentos listados, mas acredito que traga uma visão clara do que é mais relevante quando falamos de documentação.

Ao longo do curso, vamos esbarrar em diversos desses documentos, e essa visão categorizada vai fazer sentido, independentemente do momento da jornada do seu projeto.

Espero que tenham curtido. Tudo de bom e até a próxima!

## Transcrição

00:01

Bom, pessoal, e antes de a gente finalizar, então, essa nossa disciplina aí de Design Docs, o que eu acho que vale a pena é você conseguir, pelo menos, ter na sua mente e ter uma clareza muito grande de quais categorias a gente pode aplicar os Design Docs, tá? No nosso caso aqui, a gente... nós somos desenvolvedores, tá? Então, o nosso principal ponto é o que a gente mais vai utilizar no mundo desenvolvimento. Por outro lado, existem categorias que não estão necessariamente ligadas com desenvolvimento,

00:30

mas que nós podemos e a gente tem que saber que, indiretamente, esses documentos podem existir. Então, por conta disso, eu gerei aqui uma categorização somente para você entender os tipos de documento que podem existir, que você possa trombar. Alguns desses documentos a gente vai continuar vendo ao longo do curso e tudo mais em outras disciplinas.

00:51

mas eu acho que o principal ponto aqui é que você tenha um pouco mais de clareza. Então, se você olhar, eu separei aqui por documentações de produto, não são design docs, na maioria das vezes, design e arquitetura, documentos de conhecimento e referência, documentos da parte operacional e de infraestrutura, tá? Então, se olhar aqui a parte de produto, eu separei aqui documentos que são mais relevantes, ou seja, PRDs, que é Product Requirements Document,

01:17

documentos secundários, que é user stories e epics, depende muito da área realmente de produto, e também documentações que eu resolvi chamar de legadas, mas principalmente porque o uso dela no dia de hoje não é algo tão ativo, tá? Ou seja, nesse caso aqui, FRD, Functional Requirements Document, tá?

01:36

Aqui em Design e Arquitetura, olha só, eu coloquei como relevante High-Level Design, Feature Design Doc, ADR, que é Architecture Decision Records, modelo C4, aqui para a gente. Coloquei também Emergentes, AI Design Docs e Prompt Specs. A gente vai começar a olhar esses tipos de documento e, no final das contas, a gente vai ver muito isso quando nós tivermos workflows para a gente trabalhar com IA.

02:02

Então, isso na prática vai fazer muito mais sentido, mas são documentos que antes não existiam e agora a gente já está começando a ter exatamente para quê? Para que a gente consiga desenvolver utilizando o IA e a gente consiga desenhar nossa aplicação utilizando o IA.

02:17

A gente também tem documentos secundários, ou seja, RFCs, apesar de ser um documento extremamente importante. Eu até coloquei um asterisco aqui. Muitos projetos open source, muitas das definições desse projeto são feitas apenas através de RFCs e não necessariamente através de Architecture Decision Records. Então, é importante colocar. Outro documento que é importante, mas é secundário, raramente você vai ver, é o Low-Level Design.

02:43

Eu acho que é difícil você encontrar uma empresa que tenha esse documento com uma clareza muito grande, principalmente porque os projetos mudam tão rapidamente que esses documentos podem acabar, não digo nem facilmente ficando utilizados, mas a gente muda de ideia muito rapidamente na hora que a gente desenvolve. E aqui, documentos, outros caras que são legados, que é o TRD, Technical Reference Document, LLD, com o ML no formato do RUP, que a gente trabalhava antigamente.

03:11

E aí, documentos de conhecimento e referência, ou seja, Engineering Guidelines, que foi o que a gente acabou de ver, e a gente tem Security Design Doc, Emergence, a gente tem documentos de como que a gente trabalha com Evaluation.

03:26

documentos de referência também, legados, test plan and test case formal, ou seja, como que a gente organiza toda essa parte de planejamento de testes, etc. Antigamente isso era muito utilizado, não que a gente não tenha processos de teste, principalmente na área de QA,

03:43

Mas é super importante a gente entender que esses documentos de planejamento de teste, esses caras aqui especificamente, eram caras que eram muito utilizados no passado. Novamente, não que você não precise ou que você não tenha documento de teste, mas especificamente esses caras, eles são caras bem passados. E aí, documentos operacionais, runbooks e playbooks, ou seja, como que...

04:09

eu executo a minha aplicação quando eu vou colocá-la em produção, o que eu tenho que fazer quando alguma coisa dê errado, por exemplo. Outros documentos operacionais são emergentes, documentos de observabilidade, ou seja, antigamente a gente não tinha, e agora, cada vez mais, observabilidade já está virando arroz com feijão, já antigamente...

04:29

não era algo tão falado, as coisas começaram a ser implementadas e tudo mais, e hoje em dia já virou mundo real, mas você não vê tão claramente documentações tão específicas sobre observabilidade. Mas, indo para essa área mais operacional, inclusive essa parte de SRE, inclusive a gente vai falar sobre isso ao longo do curso,

04:50

Esses documentos são extremamente importantes também. E a gente tem também documentos de infraestrutura, e eu estou colocando aqui como secundários, porque a gente pode ter, inclusive, documentos de design docs só focado em infraestrutura e também documentos de como é que funciona a parte de CI e CD. E por que eu coloquei como secundário? Pessoal, só para vocês entenderem, tá?

05:14

Eu tô colocando aqui, primeiro, no meu ponto de vista e no ponto de vista do mundo do desenvolvimento. Ou seja, por que eu não coloquei documento primário de infraestrutura?

05:26

Porque nós desenvolvedores, nós não somos responsáveis pela criação necessariamente da infraestrutura. Obviamente, você for um desenvolvedor, trabalha na área de DevOps, faz parte da área, sei lá, de SRE da sua empresa e tudo mais, você faz os seus provisionamentos, faz gerações e organizações dos seus terraformes da vida e tudo mais,

05:45

É uma outra história, mas pensando em codificação, tá? Esses documentos, pra gente, eles são secundários, tá? Então, somente uma forma de categorizar, pra que você pudesse ter mais clareza, não necessariamente 100% das pessoas possam... como que eu posso dizer?

06:02

concordar com essa categorização ou especificamente com esses documentos, mas assim, com a minha experiência ao longo dos anos e com muitas pessoas que eu acabo conversando de grandes empresas, o que eu fiz aqui foi trazer o que na minha opinião

06:19

é o que tem de mais relevante aí pra vocês quando a gente tá falando de documentação. E, obviamente, ao longo do curso a gente vai acabar esbarrando em diversos documentos, mas esses caras aí que a gente acabou vendo, né, e agora tendo uma visão um pouco mais clara de uma forma categorizada, eu acho que eles vão fazer bastante sentido, independente do momento que você vai estar na jornada ali do seu projeto. Fechou? Então é isso, galera. Espero que você tenha curtido. Tudo de bom e até a próxima.

## Resumo IA

**Abreviações**  
- **PRD** — *Product Requirements Document*  
- **FRD** — *Functional Requirements Document*  
- **ADR** — *Architecture Decision Records*  
- **RFCs** — *Request for Comments*  
- **TRD** — *Technical Reference Document*  
- **LLD** — *Low-Level Design*  
- **QA** — *Quality Assurance*  
- **SRE** — *Site Reliability Engineering*  
- **CI/CD** — *Continuous Integration / Continuous Delivery*  
- **IA** — Inteligência Artificial  

**Resumo**  
A aula encerra a disciplina de Design Docs apresentando uma categorização dos principais tipos de documentação que um desenvolvedor pode encontrar ao longo de um projeto. O instrutor destaca que, embora o foco esteja no desenvolvimento, existem documentos ligados a produto, arquitetura, conhecimento, operação e infraestrutura que podem surgir indiretamente e que é importante reconhecer.

Na parte de documentações de produto, são citados como relevantes os PRDs, enquanto user stories e epics aparecem como documentos secundários, dependendo da área de produto. Como exemplos legados, são mencionados os FRDs, que hoje têm uso menos frequente. Em design e arquitetura, o instrutor aponta como relevantes High-Level Design, Feature Design Doc, ADR e o modelo C4. Também introduz documentos emergentes, como AI Design Docs e Prompt Specs, que ganham espaço com o uso de IA no desenvolvimento. Entre os secundários, aparecem RFCs e Low-Level Design, sendo este último pouco comum por ficar rapidamente obsoleto. Como legados, são citados TRD e LLD no contexto do RUP.

Na categoria de conhecimento e referência, o instrutor cita Engineering Guidelines e Security Design Doc como relevantes, além de documentos emergentes ligados a Evaluation. Como legados, aparecem Test Plan e Test Case formal, que eram muito usados no planejamento de testes, especialmente em QA. Já na parte operacional e de infraestrutura, os destaques são Runbooks e Playbooks, usados para orientar a execução da aplicação em produção e o tratamento de incidentes. O instrutor também comenta documentos de observabilidade como emergentes, além de documentos de infraestrutura e CI/CD, classificados como secundários no contexto do desenvolvimento.

Ao final, ele explica que essa classificação reflete sua experiência e conversas com profissionais de grandes empresas, reforçando que a intenção não é criar uma regra absoluta, mas oferecer uma visão prática para que o aluno reconheça os tipos de documentação e entenda sua relevância ao longo da jornada de um projeto.

**Pontos de atenção**  
- Nem toda documentação citada é considerada design doc no sentido estrito; várias são documentos de produto, operação ou referência.  
- A classificação entre relevante, secundário, emergente e legado é contextual e pode variar entre empresas e áreas.  
- RFCs são extremamente importantes em projetos open source e podem concentrar decisões sem uso de ADRs.  
- Low-Level Design tende a se tornar obsoleto rapidamente em ambientes de mudança frequente.  
- FRD, TRD, LLD no formato RUP, Test Plan e Test Case formal são exemplos de documentos mais datados.  
- AI Design Docs e Prompt Specs são documentos novos, associados a workflows com IA, e tendem a crescer em importância.  
- Runbooks e Playbooks são essenciais para operação em produção e resposta a falhas; não devem ser negligenciados.  
- Observabilidade já é prática obrigatória, mas ainda há pouca documentação específica e bem estruturada sobre o tema.  
- Documentos de infraestrutura e CI/CD são mais centrais para DevOps e SRE do que para desenvolvedores focados em codificação.  
- A categorização serve para dar clareza prática ao aluno, não para estabelecer um padrão universal.