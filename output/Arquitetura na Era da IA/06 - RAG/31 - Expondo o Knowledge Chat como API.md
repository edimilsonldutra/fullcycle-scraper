Módulo: Arquitetura na Era da IA\
Aula: [Expondo o Knowledge Chat como API](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18452)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, agora a gente está chegando meio que em um dos pontos

00:04

que eu tinha falado logo no começo desse capítulo,

00:07

né? Que a gente tem o nosso reg, obviamente,

00:10

com todas as limitações, é um exemplo didático,

00:12

mas eu também criei endpoints para que a gente consulte esse cara via API,

00:20

tá? Então, eu vou mostrar isso aqui funcionando primeiro, e depois...

00:26

eu mostro o código aqui para vocês que não tem nada demais.

00:29

Só tem uma refatoração meio que grande que eu

00:31

fiz para separar um pouquinho algumas responsabilidades. Mas vamos lá.

00:35

Se eu for aqui, eu criei um arquivo chamado teste.http,

00:39

que você usa o teste client aqui do VS Code. E o que acontece?

00:45

Eu tenho um send request para um health check simples.

00:49

Aí eu tenho chat with answer. Então, eu dou um request e ele vai perguntar.

00:54

Qual é o SLA para incidentes P1 no plano Enterprise aqui para mim,

00:58

tá? E nesse momento, o que acontece? Ele traz aqui a resposta,

01:04

certo? SLA para incidentes no plano 1 é uma resposta de

01:08

até uma hora com atendimento de 24 por 7.

01:10

Tem a resposta? Sim. Needs clarification? Não.

01:13

E os sources de onde veio cada uma das informações,

01:17

beleza? Então é isso que eu tenho em relação a essa chamada.

01:21

Agora, o que eu fiz aqui também? Eu fiz o mesmo esquema,

01:24

mas pude passar um campo a mais chamado debug igual a true.

01:28

Quando eu trago o debug igual a true,

01:30

eu vou trazer mais respostas, mais dados ali para mim. Então,

01:34

eu tenho as respostas que eu tinha antes, certo?

01:37

Mas eu tenho meus objetos aqui de debug, que é o query plan.

01:42

Aqui mostra a questão normalizada, os tipos de documento,

01:46

o plano, os termos exatos, se need clarification,

01:49

a query que foi utilizada para buscar, quais foram os filtros,

01:53

como é que foi feito o filtro dentro do doc type do plano aqui,

01:58

os chunks que foram resgatados.

02:01

Então, ele traz todas essas opções aqui para mim na hora que eu faço essa busca.

02:06

Também eu tenho uma opção que é use re-rank false.

02:11

Então, se eu uso e executo aqui, ele vai fazer tudo,

02:15

mas não vai usar o re-rank aqui para a gente.

02:20

E eu tenho uma opção que eu vou mandar uma pergunta que é ambígua,

02:25

como funciona o plano de suporte da empresa.

02:28

E aí ele cai no needs clarification, porque ele pergunta,

02:33

você precisa especificar qual é o plano. Então,

02:36

basicamente aquilo que a gente tinha rodado, mas naquela pegada interessante.

02:40

E agora, aqui, qual que é a capital da França, né?

02:43

A gente tem que falar que ele não encontrou nada suficiente.

02:46

Uma pergunta em branco também tem que retornar aqui o erro 400,

02:50

que a pergunta não pode ser em branco. Então, se você olhar aqui,

02:52

são endpoints bem simples que eu chamo e ele faz toda aquela busca ali por trás.

02:58

Códigos, falando em código, tá? O que mais foi mudado aqui,

03:01

de forma geral, é esse RAG pipeline.

03:04

Antes, o meu reg chat, ele fazia tudo, né? Ele fazia, montava o prompt,

03:09

chamava a parte do query de analisar, depois ele fazia o re-rank,

03:15

depois ele chamava o modelo, ele fazia tudo. Mas como agora eu tenho,

03:19

Eu posso usar ainda o chat, né? Via comando,

03:23

mas ao mesmo tempo eu tenho um endpoint,

03:25

então toda a parte de pipeline que faz todo esse processo,

03:29

eu separei dentro de um arquivo e ele tem uma classe bem grandona aqui.

03:33

Que chama o modelo,

03:35

que tem o planejamento, o re-rank e a resposta.

03:39

E daí ele tem um run aqui onde eu passo todos

03:42

os parâmetros e basicamente tudo que a gente tinha,

03:45

ele está aqui dentro de uma única classe para facilitar um pouco a nossa vida aqui. Então,

03:50

tudo que a gente tinha naquele chat, RegChat,

03:53

foi migrado para cá e o RegChat agora ele é pequenininho.

03:56

Então, basicamente é a pergunta e ele chama o pipeline run.

04:01

Passando tudo que a gente precisa e assim que funciona agora o RegChat,

04:05

ele fica muito mais simples.

04:07

Mesmo esquema agora aqui com a API.

04:09

A API eu estou utilizando o FastAPI do Python e

04:12

aqui basicamente eu tenho um módulo de chat request,

04:16

que ele tem a pergunta que ele recebe,

04:18

se está em debug ou se para utilizar o re-rank,

04:21

tem o endpoint de health e aqui tem a chamada, então quando eu recebo a request,

04:28

com as perguntas ele tem que retornar um result aqui do nosso pipeline e

04:33

basicamente esse result ele vem do nosso

04:39

objeto de pipeline então aqui basicamente o

04:43

que ele vai fazer é pegar a pergunta e aí uma vez que ele

04:47

pega a pergunta ele chama o pipeline igualzinho

04:50

o nosso RegChat chamou o nosso pipeline

04:53

Passando a pergunta, falando se vai usar re-rank ou não,

04:57

incluindo as informações do debug caso ele queira ali.

05:00

Daí ele vai retornar essa informação aqui para a gente.

05:03

Então a API na realidade ficou bem simples aqui de

05:06

forma geral para a gente acessar via HTTP.

05:09

Funciona, mas ainda a gente tem o nosso RegChat que

05:13

consegue funcionar no formato de chat e toda a nossa lógica, né?

05:17

A lógica não, né? O nosso pipeline.

05:19

Isso aqui é como se fosse um service que vai fazendo um monte de coisa.

05:22

Ou seja, ele orquestra o processo inteiro. Ou seja,

05:24

ele é a pipeline. Faz isso, faz isso,

05:27

faz isso, faz isso. Então, planejar, re-rank e responder.

05:32

Basicamente é isso que essa classe faz.

05:35

Agora que eu tenho essa lógica, eu posso aplicar isso, sei lá,

05:39

num protocolo HTTP, eu posso fazer isso com gRPC, não interessa,

05:43

porque o meu pipeline está aqui dentro.

05:45

Mas isso aqui era somente para a gente não ficar

05:47

duplicando ali regra de negócio e tudo mais.

05:50

Obviamente que a gente tem esses outros arquivos que

05:52

a gente criou durante todo o processo,

05:54

desde mostrar um context chat, etc.

05:59

Mas isso aqui é somente para que você consiga ver uma API funcionando, chamando,

06:03

utilizando. trazendo respostas ali de algo que foi feito utilizando RAG, beleza?

## Resumo IA

[RESUMO_IA]