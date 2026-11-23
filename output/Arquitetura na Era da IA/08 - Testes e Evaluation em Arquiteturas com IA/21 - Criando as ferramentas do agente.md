Módulo: Arquitetura na Era da IA\
Aula: [Criando as ferramentas do agente](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18800)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

Agora, para que a gente comece a mexer com esse agente que a gente vai criar,

00:07

a primeira coisa que eu quis fazer aqui é trabalhar com as ferramentas.

00:13

Então, se você olhar, eu vou ter aqui três itens importantes para a gente verificar.

00:20

Um item é o Get Current Usage,

00:22

o outro é o Create Support Ticket e o outro é o Search Knowledge Base,

00:26

aqui para a gente. O que que acontece? Se você olhar aqui o meu programa, tá?

00:31

Você vai ver que eu tenho um get pipeline somente para eu acessar a pipeline do RAG,

00:36

mas olha aqui, aqui a gente já começa com a minha anotação aqui,

00:39

arroba tool, que vai ser utilizado ali pelo meu agente, tá?

00:43

Uma coisa importante que quando eu tenho essa tool aqui e o meu agente for olhar...

00:48

ele vai olhar essa docstring e essa docstring vai mostrar para

00:52

ele se vale a pena ele chamar essa ferramenta ou não. Ou seja,

00:56

o que está escrito aqui é muito importante,

00:58

porque o agente vai se basear nisso para fazer a chamada de ferramenta.

01:03

Então aqui, quando ele dá um Search Knowledge Base,

01:06

basicamente ele está chamando o pipeline, pegando a questão...

01:10

usando o re-rank e fazendo o debug igual a falso.

01:13

Ou seja, no final das contas, eu estou pegando os dados do pipeline,

01:16

pegando os resultados das sources e tudo mais,

01:19

e eu vou responder esse cara aqui para ele com a resposta.

01:23

Basicamente é isso que eu faço.

01:25

Eu tenho uma outra tool, que é o Get Current Usage, e basicamente é para ele pegar,

01:31

aqui no nosso caso, um dado fake, que está na minha pasta data,

01:35

que ele vai olhar e vai mostrar...

01:38

Por tenant, quanto que foi a utilização ali para a gente. Ou seja, é um dado falso,

01:45

eu não ia criar um banco de dados para ter um número.

01:47

Então eu criei isso aqui no JSON.

01:49

E o outro cara é o createSupportTicket. O Create Support Ticket,

01:54

também para não ter banco de dados,

01:55

cada vez que a gente cria, ele cria um novo artefato ali.

01:59

Então, um novo JSON, onde cada um vai ter,

02:03

no final das contas, o ticket de suporte.

02:05

Perceba que ele recebe como parâmetro a severidade P1, P2,

02:10

P3, ou seja, se eu mandar um parâmetro inválido aqui,

02:13

P4, provavelmente ele vai dar erro.

02:15

Mas uma coisa interessante é que, mesmo que ele dê erro,

02:19

ele sempre vai ter que retornar o resultado.

02:22

E esse resultado vai ter que ser legível. Por quê?

02:26

Porque o agente vai pegar essa ferramenta e vai te consultar.

02:30

Se retornar um erro estourando para o agente,

02:33

vai dar ruim. Então,

02:34

a ferramenta sempre tem que retornar de uma forma legível para

02:37

o agente para ele entender o que está acontecendo,

02:40

mesmo que tenha sido acontecendo um erro ali. Então,

02:44

eu tenho aqui a minha lista de support tools que eu vou passar para o meu agente.

02:49

Eu tenho um método aqui chamado show, vocês já vão ver.

02:52

E aqui eu tenho o meu main. Então, o que esse meu main aqui faz?

02:56

Eu tenho um show onde eu vou passar o meu cara 1,

02:59

onde eu vou chamar a ferramenta get current usage e aqui eu

03:03

Vou mostrar quando ele tem um tenant que existe e outro tenant aqui, ou seja,

03:08

Basicamente, ele vai usar as informações que ele tem para pegar a

03:12

current usage que está dentro da nossa pasta data aqui para a gente,

03:16

currentusage.json. Então é esse cara aqui.

03:20

Perceba que eu só tenho um tenant, eu tenho o FCIA,

03:22

Não tenho aquele Acme ali para a gente. Então,

03:25

Esse aí é um ponto importante. Vamos voltar aqui para o Support Tools.

03:29

Eu tenho o item 2, que é o Create Support Ticket.

03:32

Ou seja, eu estou passando o parâmetro aqui, Valid,

03:36

e aqui o Create Support Ticket, aqui, Invoke, aqui para a gente.

03:41

E aí, eu tenho também a opção que é para ele dar um invoke com a severidade 2.

03:46

Então, vamos ver como é que esse cara fica.

03:48

E aí, eu tenho um parâmetro chamado Reg Tool, que eu posso passar,

03:53

ou seja, menos --mag, menos --include rag tool,

03:57

que nesse caso ele vai fazer uma chamada do pipeline.

04:01

Então, nesse caso, ele vai chamar o modelo, vai ter custo,

04:04

que acaba entrando nessa minha última questão aqui em relação a isso, tá? Então,

04:09

para a gente ver esse cara rodando, no final das contas,

04:12

acaba sendo, de forma geral, simples, né? Porque eu

04:19

tenho que simplesmente rodar o meu Python --F,

04:25

aqui para mim, e depois que eu fizer isso,

04:28

eu posso utilizar o AddIncludeRegTool aqui também.

04:34

Então, vamos lá aqui. Aqui eu tenho, aqui é das aulas anteriores,

04:39

então eu tenho um Python -M, a AppSupportTools aqui para a gente.

04:46

E olha só que interessante aqui, o GetCurrentUsage, non-tenant,

04:51

e eu trouxe aqui o resultado como JSON com resultado. E aqui a non-tenant,

04:57

Error, a non-tenant Acme. Então,

04:59

você percebe que o agente iria receber a informação desse jeito, e é isso que é importante.

05:03

Create support ticket, o dado do ticket, severidade P2, status created,

05:08

e quando está o empty, o summary aqui, erro, o summary tem que,

05:12

não pode estar em branco, né? Então, eu tenho duas opções, sempre uma que funciona,

05:15

outra não. Uma válida e outra com o empty summary aqui,

05:19

onde eu deixei esse cara em branco, né? E o terceiro foi skipped, né?

05:23

Ele foi skipped por conta que esse

05:26

cara não foi passado aquela --menos --,

05:32

né? Ali na nossa frente.

05:33

Então, isso aí é um ponto importante aqui pra gente se ligar.

05:37

Uma outra coisa interessante, quer ver?

05:40

Onde eu tenho supportetickets.json. Ó, cada chamada que eu for fazendo, ó.

05:45

Ele vai trazendo aqui os tickets de suporte que ele vai gerando,

05:49

simulando ali, obviamente, um banco de dados. Então,

05:52

é somente para constar esse cara aqui. Agora,

05:56

a gente tem aquele outro caso onde eu

05:59

posso adicionar nessa rodada o meu --menos --include,

06:06

como é que é o parâmetro aqui? Deixa eu abrir aqui.

06:09

Meu SupportTools.

06:12

Aqui, --menos --include rag tool.

06:16

Então, eu vou rodar esse cara.

06:18

--menos --include reg2. Quando ele vai rodar o terceiro, o que ele vai fazer?

06:24

Ele vai rodar o nosso reg e vai pegar a resposta.

06:30

Então, ele usou a ferramenta 3.

06:32

qual é o prazo de resposta enterprise e a answer foi o prazo de

06:36

resposta para um chamado até uma hora com atendimento 24 por 7,

06:39

o sources e ele trouxe a fonte aqui para a gente.

06:42

Então perceba que cada ferramenta tem um objetivo diferente. Uma consulta,

06:47

uma cria alguma coisa e outra faz uma consulta semântica, né?

06:51

A outra consulta é como se fosse uma chamada...

06:55

De API, um dado ativo e não algo documental no final das contas.

07:01

Então, essa é a ideia.

07:03

Falamos apenas de ferramentas.

07:04

A gente não criou nenhum agente por enquanto. Então, vamos nessa.

## Resumo IA

[RESUMO_IA]