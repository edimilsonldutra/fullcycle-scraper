Módulo: Arquitetura na Era da IA\
Aula: [Gerando embeddings de textos](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18346)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, agora a gente vai falar sobre embeddings.

00:04

E só para a gente se organizar um pouco melhor aqui no projeto,

00:07

nos arquivos, deixa eu trazer aqui para vocês como é que ficou a organização disso.

00:14

Dentro da pasta Models,

00:16

eu tenho basicamente aquilo que eu já mostrei para vocês antes.

00:19

Ticket Request, Ticket Analysis,

00:21

o Fingerprint, o Cache Info, Ticket Response, o Config Update, o Config Response.

00:28

E agora, o que acontece aqui no meio da história? Entraram três novos models aqui.

00:34

Um é o embedding request, que é quando a gente vai ter um endpoint novo,

00:40

então a gente vai mandar mensagem ali e a gente vai

00:43

ter o request para a gente ter um embedding.

00:46

Eu tenho o item do embedding, ou seja, vai ser o texto normal, o texto normalizado,

00:53

a quantidade de dimensões que vai ter no nosso vetor e um preview,

00:58

do nosso vetor, porque o nosso vetor tem mais de 1 .500 posições. Então,

01:01

a gente só tem um pequeno preview ali para a gente olhar. E aqui,

01:05

o embedding response para a gente retornar o resultado ali para a gente.

01:10

E por que eu estou falando isso aqui?

01:12

Porque o que acontece agora, pessoal, vai ser o seguinte.

01:16

Eu tenho o meu normalize text, que eu já tinha antes.

01:19

Eu tenho o meu build fingerprint.

01:20

Eu tenho o meu build cache aqui. Nada mudou. E aqui,

01:24

eu tenho o meu prompt normal. Nada mudou. Mas agora, olha só aqui que interessante.

01:30

Eu tenho o meu prompt normal aqui, o create chat model,

01:33

mas eu tenho um novo cara aqui nessa minha linha,

01:36

que é o embeddings underline model.

01:38

E ele tem uma chamada aqui, chamada de create embedding model. E o que isso,

01:45

no final das contas, representa?

01:46

Representa que ele vai pegar um modelo, e nesse caso,

01:49

ele vai pegar ali um modelo da OpenAI, que inclusive está no meu .envy.

01:56

exemplo aqui, que eu tenho o meu open embedding e aqui o model temperature,

02:02

deixa eu já aproveitar e colocar aqui,

02:04

tá? E o que que acontece aqui?

02:07

Esse é o modelo da OpenAI pra embedding, a versão small dele.

02:11

Então significa que quando, né, eu chegar aqui no meu main .py,

02:16

né, e dar um create embed model, ele,

02:19

né, usando o langchain nesse caso, ele já vai fazer automaticamente o quê?

02:23

Uma chamada ali pra OpenAI,

02:26

vai pegar aquela informação que a gente precisa,

02:29

e aí com essa informação ele vai gerar o vetor,

02:34

onde vai ter aquela mensagem de forma vetorizada, ou seja,

02:38

a gente vai pegar aquela mensagem e transformar ela dentro de um vetor.

02:42

Então aqui eu tenho um barra config, o config que eu tinha antes,

02:46

aqui eu tenho o meu analyze tickets,

02:48

que continua exatamente a mesma coisa, mas agora aqui,

02:54

Eu tenho um barra embeddings, barra generate.

02:57

E esse generate ele vai usar aquele request que eu falei para vocês. Lembra do nosso model?

03:02

Ou seja, eu tenho embeddings request,

03:05

onde eu vou receber uma lista de textos onde eu posso trabalhar.

03:09

Ou seja, eu vou receber diversos textos.

03:12

E o que ele vai fazer? Vai normalizar os textos normalmente.

03:15

Ou seja, vai ser uma listagem. Então,

03:17

ele está pulando linha para cada texto. Ele vai normalizar.

03:20

Vai verificar o tempo. E agora, o que vai acontecer?

03:24

Ele vai pegar aqui, embeddingsmodel.embeddocuments.

03:28

Lembra que a gente tinha aqui embeddingsmodels para a gente?

03:32

Cadê o nosso camarada?

03:34

EmbeddingsModel, que é o nosso creating embeddingsModel. Agora, aqui,

03:38

o que ele vai fazer? Ele vai usar esse cara. Cadê aqui?

03:42

EmbeddingsModel.embeddocuments. E agora aqui,

03:45

ele vai pegar quais documentos que eu estou querendo fazer o embedding,

03:49

para gerar o nosso vetor.

03:51

São os textos que eu normalizei e que eu recebi via request agora aqui.

03:56

E aí, para cada cara desse aqui,

03:58

eu vou ter, no final das contas, o item desse embedding.

04:03

Ou seja, eu tenho o texto, o texto normalizado,

04:05

as dimensões do meu vetor e um

04:07

preview desse vetor que foi gerado aqui,

04:12

baseado nisso. E aqui, para cada um deles...

04:15

ele vai preenchendo aqui. Então, basicamente, é uma sintaxe do Python.

04:19

Ele fala que para cada item que eu tenho dessa forma,

04:22

ele vai fazer um for e vai preencher cada um desses campos.

04:26

E aqui eu tenho o meu log,

04:28

que eu vou trazer essa informação para a gente olhar aqui no nosso log.

04:34

Somente para você saber, aquele log block,

04:36

eu criei aqui num arquivo log_helpers para não

04:39

ficar meio que misturado dentro da nossa aplicação.

04:42

Então, vamos rodar esse cara agora aqui. Então, vamos lá.

04:48

Aqui. Está rodando. Vou aqui no meu teste.http e a primeira coisa que eu vou fazer,

04:54

eu vou chamar a IA,

04:56

a segunda vai retornar o cache e aqui a configuração atual do embedding

05:01

que eu tenho e eu tenho aqui a opção de gerar embedding de textos,

05:05

que é esse cara aqui que eu quero nesse momento.

05:07

Então, eu vou dar um send request aqui para mim.

05:10

E olha só o que aconteceu.

05:13

Embeddings gerados. A contagem de textos foi três, as dimensões foram 1536,

05:19

que é a dimensão ali do modelo da OpenAI,

05:22

e o tempo que ele demorou aqui para gerar para a gente os nossos embeddings.

05:27

E o resultado aqui foi basicamente isso. Ele trouxe o model,

05:31

quais foram os itens, como calcula a minha assinatura, o texto normalizado,

05:36

as dimensões do embedding e um preview de como que

05:40

é o nosso vetor que ele foi gerado.

05:43

E aqui, mesma coisa com o outro texto. Quero cancelar meu plano. E outra coisa aqui,

05:48

não consigo acessar minha conta. Então, para cada item,

05:52

para cada texto que eu mandei aqui, se você olhar,

05:55

foram vários textos aqui que eu acabei enviando. Então,

05:59

esses textos aqui foram os textos que eu

06:01

acabei fazendo a geração desse embedding aqui.

06:05

Lembrando que isso aqui teve uma camada de abstração do LangChain,

06:09

mas eu poderia fazer uma chamada normal utilizando o SDK da OpenAI,

06:13

que acaba sendo bem simples.

06:14

Mas eu estou usando o LangChain para facilitar aqui a nossa vida.

06:17

Fechou? Então, vamos para a próxima.

## Resumo IA

[RESUMO_IA]