Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17075)

## Resumo da aula

C4-Code é o nível mais detalhado do modelo C4 e aproxima o diagrama da estrutura real do código. Em vez de mostrar apenas componentes, ele expõe interfaces, structs, construtores, tipos e relações técnicas internas. Esse nível existe para responder perguntas que C3 não cobre bem, como contratos explícitos entre partes do sistema e regras que precisam ser padronizadas ou auditadas. Por isso, ele representa a granularidade máxima útil antes de o diagrama começar a competir com o próprio código-fonte.

O principal problema do C4-Code é que ele envelhece muito rápido quando o sistema muda com frequência. Como o diagrama descreve detalhes próximos da implementação, qualquer refatoração em interfaces, tipos ou composição interna pode torná-lo incorreto em pouco tempo. Esse custo histórico explica por que o nível raramente aparece como prática comum em empresas, mesmo quando o time reconhece seu valor conceitual. Um diagrama detalhado e desatualizado deixa de orientar e passa a gerar desconfiança.

C4-Code faz sentido quando existe necessidade real de padronização técnica, revisão de contratos internos, auditoria ou alinhamento fino antes da implementação. Ele também ajuda quando o time quer discutir a estrutura de uma solução com mais precisão do que o C3 permite, especialmente em brainstorming técnico ou desenho pré-código. Fora desses casos, o custo-benefício costuma ser ruim, porque o leitor passa a consultar mais o código do que o diagrama. A decisão correta não é “sempre gerar”, mas escolher esse nível apenas quando a pergunta arquitetural exige esse detalhe.

A IA não elimina o problema conceitual do C4-Code, mas reduz bastante o custo operacional de produzi-lo e mantê-lo. Quando o diagrama pode ser derivado de uma especificação textual bem escrita, atualizar a fonte tende a ser mais barato do que redesenhar manualmente cada detalhe técnico. Isso reabre a possibilidade de usar C4-Code em contextos onde antes o esforço de manutenção inviabilizava o artefato. Ainda assim, a utilidade do diagrama continua dependendo de alguém realmente precisar ler esse nível de detalhe.

Retomando o Rate Limiter já visto nos níveis anteriores, o C4-Code não nasce da imaginação da IA: ele depende do que o FDD explicita. Se o documento traz snippets das principais interfaces, tipos de configuração e contratos centrais, a IA consegue transformar esse conteúdo em uma visão estrutural coerente. Se essas definições não estiverem no FDD, o agente terá pouco grounding para gerar um diagrama confiável. O limite do que pode ser automatizado é, portanto, o limite do que foi especificado com clareza.

No C4-Code, a Public API interna do Rate Limiter deixa de ser apenas um bloco conceitual e passa a aparecer como um agrupamento de contratos técnicos. Esse agrupamento pode incluir interfaces expostas ao restante do container, structs de configuração, tipos de decisão e definições relacionadas ao storage. O valor dessa representação está em mostrar quais formas de interação são estáveis e quais detalhes concretos ficam por trás delas. Em vez de apenas dizer que existe uma API interna, o diagrama mostra do que ela é feita.

Algumas informações importantes não são componentes, mas restrições que governam o comportamento correto do sistema. Semântica de headers, invariantes de decisão e regras de uso de contratos podem aparecer no C4-Code porque influenciam diretamente a implementação e a integração entre partes. Esse tipo de detalhe é valioso quando o time precisa preservar consistência entre múltiplas implementações ou evitar interpretações divergentes do mesmo contrato. O diagrama deixa de mostrar só “quem chama quem” e passa a registrar condições que não podem variar livremente.

Lembra do middleware, do Strategy Engine e do storage adapter já vistos no C3: aqui eles continuam existindo, mas agora podem ser lidos a partir de suas formas concretas no código. O diagrama passa a revelar, por exemplo, que a integração HTTP envolve um wrap sobre o handler, que o núcleo possui um construtor explícito e que a escolha entre estratégias depende de parâmetros técnicos definidos em contrato. Essa leitura é útil porque conecta a colaboração entre blocos à estrutura implementável que sustenta essa colaboração. O resultado é uma visão menos abstrata e mais verificável.

No C4-Code, o storage deixa de aparecer apenas como abstração e se desdobra em variantes concretas como Redis Store e Memory Store. Essa distinção importa porque o comportamento distribuído e o comportamento em memória local impõem restrições diferentes de consistência, operação e configuração. A interface Store continua sendo o contrato comum, mas o diagrama explicita quais implementações reais cumprem esse contrato e em que contexto elas fazem sentido. Esse é o ponto em que a arquitetura mostra não só a abstração, mas também as escolhas concretas que materializam o sistema.

C4-Code não é o destino natural de toda documentação arquitetural; ele é um instrumento especializado. Quanto mais o diagrama se aproxima do código, maior a chance de o próprio código ser a fonte mais eficiente de leitura, especialmente em times que já dominam a base. O uso responsável desse nível exige perguntar se o diagrama está reduzindo custo cognitivo ou apenas duplicando informação com atraso. Quando a resposta for duplicação, é melhor parar no C3 e deixar o restante para a implementação e para o FDD.

## Transcrição

00:01

Bom pessoal, e agora a gente vai para o nosso último tipo de diagrama C4, que é o C4, que ele é chamado de Code, ou seja, ele traz detalhe técnico, ele traz código, ou seja, o que ele vai fazer?

00:16

Ele vai aprofundar a gente nas classes, nas funções, nas estruturas específicas, nas structs, usando apenas quando há necessidade real de padronização ou auditoria. Não é obrigatório na maioria dos projetos, inclusive, deixa eu ver se eu consigo aumentar isso aqui, que eu acho que tinha algo aqui, e raramente recomendado. Por que eu estou dizendo raramente recomendado, galera?

00:40

Atualmente, eu acho muito difícil ou eu não sei o quão importante é, honestamente, pensando aqui com vocês, você ter tantos diagramas técnicos para conseguir definir como que você vai desenvolver o seu sistema. Como assim, tá? O que eu estou querendo dizer é que quando a gente chega aqui em detalhe, entre aspas, de código,

01:05

Me lembra muito quando a gente estava lá naquela época do waterfall, onde a gente criava e mostrava tão claramente todos os componentes, tá? Pra daí sair executando.

01:17

O grande ponto aqui é que nós desenvolvedores sabemos, de forma geral, que sistemas mudam o tempo inteiro. Às vezes a gente inicia desenvolvendo de um jeito e a gente percebe no meio do caminho que não está legal, e a gente acaba mudando um pouco a forma de como que a gente vai trabalhar. E esses tipos de diagrama, às vezes, eles podem não estar representando tanto a realidade do sistema.

01:47

Por outro lado, e é esse ponto de reflexão que eu quero trazer aqui pra você, é, com inteligência artificial, como as formas dos nossos códigos estão trabalhando e tudo mais, provavelmente não é tão difícil manter um diagrama desse atualizado. A gente consegue fazer isso de forma automática. Agora, o grande ponto aqui é

02:11

o quanto você, desenvolvedor, iria querer ficar olhando para esses diagramas. Então, vai muito de necessidade. Honestamente, se eu tiver que apresentar para alguém como eu estou pensando em estruturar o meu sistema e eu mostro os componentes, fica uma forma interessante de ver.

02:31

dependendo do nível de detalhe da estruturação ou se eu quero estruturar bem antes realmente, antes de colocar a mão no código, fazer um brainstorming com a minha equipe e etc.

02:42

Realmente, talvez esse diagrama seja útil, mas é um tipo de diagrama que raramente eu vejo qualquer empresa usar. Eu posso estar muito enviesado com os contatos e com as empresas que eu acabo tendo no dia a dia, mas é muito raro. Agora, também é o seguinte, é raro porque dá muito trabalho também para fazer. Agora, com o IA,

03:03

Vamos ver se ao longo do tempo isso realmente continua sendo raro ou não, tá? Mas não necessariamente você é obrigado a gerar. Na realidade, tá? Sendo bem honesto, você não é obrigado a gerar nada, tá? Mas aqui estão algumas opções que realmente, com a possibilidade que a gente tem com o IA, gerar esses caras agora é muito mais fácil.

03:25

Então, o trabalho que a gente tem de gerar e manter é muito menor do que era antes. Então, talvez volte a fazer sentido. De qualquer forma, se você olhar cada um desses caras aqui, Extractor, Rate Limiting com API Pública, Telemetry, Strategy Engine, esses caras começam sendo abertos. Então, se você olhar aqui, Public API, onde eu tenho aqui API Pública,

03:51

é dentro dessa caixa. Então, nesse caso, eu estou trabalhando com o Go, então ele já coloca aqui como struct, onde eu tenho as opções de configuração, eu tenho o rate limiter com as APIs públicas, são essas minhas interfaces, eu tenho aqui a struct para fazer a decision, eu tenho o tipo de storage, eu tenho como é feita a configuração do Redis. E aí você deve estar se perguntando, Wesley, de onde saiu essa estrutura?

04:18

por incrível que pareça, essa estrutura, na hora que eu gerei o FDD, eu pedi para ele colocar para a gente pelo menos os snippets principais das principais interfaces do sistema. E o que acontece? Quando eu usei a IA para gerar o diagrama C4, o que aconteceu? A IA foi capaz de entender

04:39

aquele código como APIs públicas e componentes, e ela representou da forma como está no nosso código nesse formato de diagrama. Então, de uma forma geral, esse diagrama não foi criado do zero, da cabeça da IA que gerou o C4. Ele veio da cabeça de quem gerou o nosso feature design doc. Nesse caso, no meu feature design doc,

05:04

tem lá as APIs públicas, tá? Ou seja, vai depender muito se você vai querer que no seu System Design Doc ele já traga coisas desse tipo, porque, na realidade, toda vez que você está desenvolvendo uma feature, é muito complexo você pedir para ir a desenvolver, vamos dizer, o projeto daquela feature, porque normalmente ela inclui regras de negócio da sua empresa, né? Foi o que eu falei bastante para vocês no capítulo quando a gente fala de Feature Design Doc.

05:34

quando a gente fala de PRD. Esses documentos, eles não são fáceis de gerar, puriar, dependendo da situação, exatamente pelo fato de que quem conhece as regras de como as coisas funcionam, tá na cabeça do desenvolvedor, do líder, da pessoa de produto, né? Então...

05:51

Não é tão simples, às vezes, você colocar APIs públicas dentro de um Feature Design Docs, se você não pensou nisso antes, tá? Mas, partindo do princípio que isso estava no Feature Design Docs, a IA foi capaz de entender aquilo e gerar. Então, se você olhar aqui, tem a...

06:11

A HTTP integration, que é o nosso middleware, que usa o rate limiter, que tem um wrap em cima do handler HTTP. Aqui eu tenho o strategy engine, que vai decidir se é o fix the window ou se vai ser o token bucket. Aqui tem os parâmetros principais desse cara. Aqui tem as implementações core, ou seja, como é que vai ser a implementação do rate limiting em si.

06:34

Aqui tem a parte de telemetria, aqui está como é que vai ser o construtor dessa implementação core, como que vai ser a parte de storage, ou seja, eu vou ter que ter o Token Bucket, o Fixer Window, mas aqui eu tenho o Reds Store e eu tenho o Memory Store também, porque eu posso trabalhar com memória local ou distribuída, e o Store aqui tem a interface para dizer que está

06:58

incrementando essas informações. E aqui eu estou setando qual tipo de cara que eu vou trabalhar. Então, a gente sempre tem aqui a semântica de headers, invariantes, tem algumas regras e todas essas regras aqui estão vindo daquele nosso FDD. Então, o nosso ponto

07:17

importante aqui, tá? E eu só tô olhando e mostrando aqui esse sistema pra tentar deixar claro aqui pra você a diferença desses caras, tá? Então, se você, e eu vou voltar isso pela última vez, eu prometo, é que aqui dentro, tá? Tem simplesmente um sistema, tá? A gente tem um sistema aqui dentro.

07:41

Dentro desse nosso sistema, nós temos aqui, no final das contas, um container. Dentro desse container, a gente tem esse container explodido, vamos dizer aqui, que tem os elementos dele. E cada um desses elementos desse container, eu consigo olhar aqui quais são as interfaces, as integrações, as APIs, etc., que esse cara está utilizando.

08:02

Beleza? Então, estamos vistos, de forma geral, como são e como funcionam os diagramas C4. Recomendo que você depois se especialize, se fizer sentido, para você entender esses caras com mais detalhes. Beleza? No próximo vídeo, a gente vai entender um pouco melhor de como que a gente gera esses caras. E fazendo isso tanto de forma manual, como de forma automática, utilizando IA. Beleza? Então, vamos nessa!

## Resumo IA

**Abreviações**

- **C4**: *Context, Container, Component, Code* — modelo de documentação arquitetural em quatro níveis.
- **FDD**: *Feature Design Doc* — documento de design da funcionalidade.
- **PRD**: *Product Requirements Document* — documento de requisitos do produto.
- **HTTP**: *HyperText Transfer Protocol* — protocolo de comunicação web.
- **API**: *Application Programming Interface* — interface de programação de aplicações.
- **API Pública**: interface exposta para consumo por outras partes do sistema.
- **IA**: *Inteligência Artificial*.

**Resumo**

A aula apresentou o nível C4-Code como o estágio mais detalhado do modelo C4, aproximando a documentação da estrutura real do código-fonte. Nesse nível, o diagrama deixa de mostrar apenas componentes e passa a expor interfaces, structs, construtores, tipos, integrações internas e contratos técnicos, sendo útil quando há necessidade de padronização, auditoria, revisão de contratos internos ou alinhamento muito fino antes da implementação. O instrutor destacou que esse nível raramente é usado na prática porque envelhece rapidamente: mudanças frequentes em interfaces, tipos ou composição interna tornam o diagrama desatualizado e pouco confiável. Ainda assim, explicou que a inteligência artificial reduz bastante o custo de gerar e manter esse tipo de artefato, especialmente quando a fonte textual está bem especificada.

Usando o exemplo de um Rate Limiter, o instrutor mostrou que o C4-Code não nasce “da cabeça” da IA, mas do que foi explicitado no FDD. Quando o documento traz snippets das interfaces principais, tipos de configuração e regras centrais, a IA consegue transformar esse conteúdo em uma visão estrutural coerente; sem esse grounding, o diagrama perde confiabilidade. No exemplo, a Public API interna aparece como agrupamento de contratos técnicos, incluindo interfaces expostas, structs de configuração, tipos de decisão e definições de storage. Também foram evidenciados o middleware HTTP com wrap sobre o handler, o Strategy Engine que decide entre Fixed Window e Token Bucket, o construtor explícito da implementação core, a telemetria e as implementações concretas de storage, como Redis Store e Memory Store. O instrutor reforçou que regras como semântica de headers, invariantes de decisão e contratos de uso também podem aparecer nesse nível por influenciarem diretamente a implementação e a integração entre partes. A mensagem final foi que C4-Code é um instrumento especializado: vale quando o diagrama reduz custo cognitivo e responde a uma pergunta arquitetural que exige esse nível de detalhe; caso contrário, é melhor parar no C3 e deixar o restante para o código e os documentos-fonte.

**Pontos de atenção**

- C4-Code é o nível mais detalhado do C4, mas não deve ser adotado por padrão em todos os projetos.
- Diagramas muito próximos do código envelhecem rápido e podem ficar incorretos após refatorações.
- Um diagrama desatualizado deixa de ajudar e passa a gerar desconfiança no time.
- O uso faz sentido principalmente em casos de padronização técnica, auditoria, revisão de contratos e brainstorming pré-código.
- Se o time já consulta diretamente o código-fonte, o C4-Code pode virar apenas duplicação de informação.
- A qualidade do diagrama depende fortemente da qualidade do FDD: sem interfaces, tipos e regras bem especificados, a IA não gera uma visão confiável.
- A IA reduz o custo operacional de criação/manutenção, mas não elimina o problema conceitual de manter documentação muito granular.
- Nem toda informação é componente; regras, invariantes e semântica de contratos também precisam ser documentadas quando afetam a implementação.
- É importante diferenciar abstrações de implementações concretas, como a interface Store versus Redis Store e Memory Store.
- A escolha correta é avaliar custo-benefício e evitar gerar esse nível quando ele não reduz o esforço cognitivo do leitor.