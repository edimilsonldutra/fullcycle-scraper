Módulo: Arquitetura na Era da IA\
Aula: [Instrumentando o pipeline com OpenTelemetry](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18751)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, então vamos colocar aqui um pouco a mão na massa e eu quero mostrar para vocês

00:04

essa implementação na realidade de trás para frente para

00:08

a gente entender o que está acontecendo.

00:10

Então o negócio é o seguinte,

00:12

eu vou colocar aqui o nosso RegChat que

00:16

a gente tinha aqui com o debug habilitado.

00:19

E eu vou colocar uma pergunta igual nos dois exemplos no final das contas.

00:24

Aqui é, qual é a SLA para incidentes P1 no plano Enterprise?

00:28

Então, vou dar um Enter aqui.

00:30

E aqui a gente tem que pegar todo o debug de tudo que aconteceu ali na aplicação,

00:34

que é o que a gente já tinha antes, tá?

00:36

Então, o que acontece aqui?

00:38

Deixa eu voltar aqui para o debug para a gente entender

00:40

até aqui em cima onde que as coisas aconteceram,

00:43

né? Então, o que acontece é o seguinte, qual é o incidente?

00:46

Então, ele mostra aqui que ele passou por algumas etapas,

00:48

né? Ele teve aqui o query plan,

00:51

ele teve o que ele recebeu aqui de retrieval, né? Dos chunks.

00:56

Depois disso... ele teve, vamos lá, ele teve o que ele selecionou,

01:02

depois ele tem aqui a parte do pipeline em si.

01:05

Então, o pipeline ele teve planejamento,

01:08

o retrieval, o re -ranking e o answer generation.

01:11

Esses caras aqui para trazer o tempo todo que ele demorou para a utilização,

01:17

qual foi o modelo utilizado e aqui a nossa resposta. Então,

01:21

isso aqui é o que a gente tinha e esses dados aqui,

01:24

no final das contas, são os dados que a gente estava trabalhando.

01:27

Então, o que eu vou fazer agora aqui, tá?

01:30

Deixa eu coisar. Eu tenho a variável de ambiente nova aqui no meio dessa história.

01:37

Deixa eu aumentar aqui para você não ver a minha chave da OpenAI.

01:42

Aqui. E se você perceber,

01:43

eu tenho uma variável aqui que está escrito Observability Enabled,

01:48

tá? E aqui eu vou colocar como True.

01:50

Uma vez que eu coloque esse cara aqui como True, o que vai acontecer? Eu vou...

01:59

executar o mesmo chat, a mesma aplicação,

02:02

mas agora você vai perceber que a gente vai receber a resposta, na realidade,

02:08

do que está acontecendo ali com o OpenTelemetry no terminal, no chat também,

02:13

porque é o mecanismo que eu coloquei aqui para exportar.

02:16

Então eu vou dar um Enter aqui.

02:18

e agora a gente vai começar a ver outras informações que a gente não tinha,

02:22

que são as informações ali de telemetria que a gente acabou colocando,

02:27

tá? Então, vamos lá, deixa eu voltar aqui, tudo

02:31

que a gente tinha lá pra cima,

02:33

mas eu quero chegar nesse JSON gigante que a gente vai ter agora em cada parte,

02:37

tá? E é aqui que eu quero mostrar aqui pra vocês,

02:39

vamos lá. Então, o que que acontece? Qual é a SLA de incidente?

02:43

Então, primeira coisa, ele tá pegando aqui, né, o pedaço, né,

02:49

daquilo que ele vai transformar nesses nossos tracings. Então,

02:53

olha só que interessante. Então, eu tenho aí .reg.queryplanning.

02:57

Então, ele está pegando esse query planning e ele está

03:00

gerando isso aqui dentro de um contexto,

03:02

Gerando um Trace ID. O que isso significa?

03:05

O Trace ID é o ID que, no final das contas,

03:10

vai estar presente em todos os tracings. Ou seja,

03:14

para eu saber que dentro daquela requisição,

03:18

eu tenho os pedaços dela, que nesse caso são os nossos spans, né?

03:23

E todos esses spans,

03:24

eles fazem parte do mesmo Trace ID para a gente conseguir agrupar.

03:28

Então, se você olhar aqui, eu tenho um span, aqui que ele foi gerado,

03:31

né? E o Trace State aqui está em branco.

03:34

Agora, se você olhar aqui, que é o que eu quero que você preste atenção,

03:37

é o seguinte. Tem dados aqui de quem é o pai,

03:40

o tempo de início, o tempo de final,

03:42

mas eu acho que o ponto mais importante aqui que você olha é o seguinte.

03:47

Lembra que a gente falou? A gente tem o Trace,

03:49

a gente tem o Span, e dentro do Span tem atributos,

03:52

que são as informações que vão nos ajudar a entender

03:55

o que estava acontecendo para a gente conseguir rastrear.

03:58

E nesse caso de atributos, ele colocou aqui, AppNormalizedQuestions66,

04:04

AppDocs, que são informações que a gente tinha,

04:07

Enterprise, os termos exatos, NeedClarificationFalse,

04:10

e AppQuery aqui para a gente, em milissegundos, quanto tempo ele demorou.

04:16

E aqui ele tem o resource, ou seja,

04:19

outros atributos que vêm junto aqui no meio da história.

04:22

Ou seja, quais são os recursos que foram utilizados para isso?

04:25

Então, teve a telemetria, o SDK foi com Python, o nome do SDK foi do OpenTelemetry,

04:31

a versão, o Service Instance ID e aqui o nome do Service Name aqui para a gente.

04:37

Então, se você perceber, eu tenho um span,

04:40

que é um pedaço criado de um Trace completo, tá?

04:45

E esse aqui é uma etapa desse span, que é o Query Planning.

04:51

Se eu continuar descendo, você vai ver agora que eu tenho outro cara,

04:54

que é o Reg Retrieval, tá? E aqui, ó, ele vai ter o mesmo Trace ID,

04:58

mas o Span ID é diferente. E agora você vai ver o quê?

05:03

Que nós vamos ter aqui os atributos. Então, ó, quantos chunks teve,

05:09

quais são os filtros que foram utilizados e

05:11

quanto tempo ele demorou para o Retrieval.

05:13

Os atributos, o resource, aqui praticamente ficou a mesma coisa.

05:17

Então, se você perceber,

05:18

o que está diferenciando uma etapa da outra aqui para a gente conseguir rastrear,

05:21

no final das contas, são esses atributos e o nome do span,

05:26

ou seja, o nome daquele momento que a gente estava no software.

05:28

Lembrando que quem define isso somos nós. Então,

05:31

quando a gente for olhar o código fonte, você vai perceber exatamente isso.

05:35

Existem ferramentas com OpenTelemetry que você tem a instrumentação automática que

05:39

ele tenta pegar coisas padrão que a linguagem coloca.

05:42

No nosso caso, a gente está fazendo isso de forma intencional.

05:45

Então, vamos lá. Eu tenho aqui ai .reg .reranking. E aí,

05:50

quando eu olhar aqui, ele gerou o mesmo Trace ID, o Span.

05:54

E aqui, a gente olha atributos de re-ranking.

05:57

Eu tive quatro chunks e aqui o tempo que ele demorou aqui pra mim.

06:02

E aqui, por fim, eu tenho o Span de Answer Generation.

06:07

Ou seja, aquele momento onde ele vai gerar a resposta.

06:10

E aqui eu tenho alguns atributos. E esses atributos aqui são importantes, inclusive.

06:15

GeneAI... response model, request model, etc.

06:19

Eles acabam entrando já num padrão semântico que

06:21

já está sendo utilizado pelo mercado.

06:23

Então, esses nomes GenAI já são nomes meio que padrões,

06:27

padrão para que você utilize e trabalhe no dia a dia. Então,

06:30

tem request model, model usage, input tokens, output tokens, total.

06:36

Teve uma resposta? Sim.

06:38

Quanto tempo demorou para a geração dessa resposta? E aqui embaixo,

06:42

a mesma coisa. E aí, por fim,

06:46

Se você perceber, eu tenho o meu trace ID,

06:48

mas agora é da minha pipeline inteira, se você perceber.

06:52

E o que isso significa no final das contas?

06:56

Quando eu rodo a minha pipeline, o que acontece?

06:59

Eu tenho os atributos, a feature, o tenant, qual foi o produto,

07:04

se teve re-ranking, se teve resposta, se precisou de clarificação, quantas sources,

07:11

ele trouxe e o total de milissegundos. Então, se você perceber,

07:15

ele pegou desde os pedaços pequenos até agora uma visão completa do que aconteceu.

07:21

E aqui embaixo, no final das contas, é o que a gente já tinha.

07:25

Mas o importante aqui é você entender que essas

07:28

informações que foram geradas ali por aquele

07:31

JSON foram utilizando o SDK do OpenTelemetry e a gente vai ver isso logo em seguida.

## Resumo IA

[RESUMO_IA]