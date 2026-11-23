Módulo: Arquitetura na Era da IA\
Aula: [Preparando pgvector e salvando embeddings](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18349)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, a gente estava falando sobre embedding, correto?

00:05

Então, quando a gente gera o embedding,

00:09

a gente acaba tendo essa experiência de pegar o

00:12

nosso texto e transformá-lo em um vetor.

00:15

Agora, a gente vai fazer isso de uma forma manual, de propósito,

00:20

principalmente para você entender como que isso funciona

00:24

quando nós trabalhamos no banco de dados.

00:27

Para a gente fazer uma busca de similaridade e

00:30

entender a distância em relação a um registro e outro,

00:35

a um vetor e outro. Então, o que acontece aqui?

00:39

Somente para a gente se localizar aqui no nosso programa novamente.

00:43

Eu tenho aqui o normalize_text, builder_fingerprint, build_cache_key,

00:48

que é o que a gente já estava acostumado,

00:49

nosso prompt e etc.

00:51

Até aqui não mudou absolutamente nada em relação ao que a gente está fazendo.

00:56

Porém, o que acontece aqui? Nós adicionamos os seguintes endpoints.

01:03

Esse generate nós já tínhamos,

01:05

que é o que a gente testou na última vez prática que a gente estava trabalhando.

01:09

Mas agora eu tenho esse cara, que é o semantic_cache/items.

01:14

Qual que é a ideia aqui? Eu vou pegar um request,

01:19

que eu vou receber, que é o semantic_cache_create_request.

01:22

Se eu for aqui nos meus models,

01:24

a gente vai ver semantic_cache_create_request,

01:27

onde eu tenho um texto aqui para

01:31

mim e uma resposta aqui em JSON.

01:35

Por que eu estou dizendo isso?

01:36

Porque isso vai fazer eu criar essa informação no meu banco de dados.

01:41

E aqui a response é onde ele vai retornar toda a informação.

01:47

E aqui são os textos do embed_request, que é o que a gente utilizou antes.

01:50

Qual é a nossa ideia aqui? E o meu ponto aqui,

01:53

pessoal, não é você aprender Python e aprender Langchain.

01:56

É para que você entenda a ideia do que a gente está fazendo agora aqui.

01:59

Quando eu recebo uma entrada de informação,

02:02

o que eu faço? Eu gero o fingerprint,

02:04

verifico se esse fingerprint pode ser utilizado por conta da normalização. E aí...

02:12

eu tenho o meu embedding, tá? Aqui no meu caso,

02:14

o meu embedding, eu dou lá embedding_query, tá?

02:17

E eu passo o meu texto normalizado. E agora eu consigo ver,

02:22

inclusive, a dimensão do meu vetor aqui.

02:26

Então, eu dou um len(embedding) aqui para mim. E agora, aqui que está a grande sacada.

02:32

Eu tenho aqui um item_id,

02:34

onde eu vou executar uma função chamada insert_semantic_cache_item,

02:39

onde eu passo o fingerprint.

02:41

O que entrou como texto,

02:43

a response que aconteceu aqui no meu JSON, que eu recebi,

02:49

e o resultado do embedding que eu acabei fazendo aqui.

02:54

De onde que vem essa função insert_semantic_cache_item?

02:58

Eu tenho um arquivo agora que eu chamo de db.py.

03:02

E somente para você entender esse db.py,

03:05

eu falo qual é a tabela que eu vou usar, que é AICacheResponse.

03:11

Você vai ver que eu tenho uma função que é pra ajudar a transformar esse cara próprio pra trabalhar com o PG Vector.

03:13

O que é o PG Vector? É uma extensão...

03:18

do Postgres para a gente trabalhar de forma vetorial. Ou seja,

03:21

eu consigo fazer buscas em vetores utilizando o Postgres.

03:24

Lembrando que no mercado a gente tem diversas outras opções também, como o Pinecone,

03:28

que é um super banco de dados específico para fazer esse tipo de busca.

03:33

Quando o meu banco de dados inicia... O que eu estou fazendo?

03:39

Eu estou executando um CREATE EXTENSION IF NOT EXISTS pgvector,

03:42

para ele poder ter essa extensão ativa do vetor, e crio a minha tabela aqui.

03:46

id, prompt version, rules version, module capability, input text, normalized,

03:51

o response que a gente tem, e o vetor embedado aqui.

03:56

Por isso que ele está aqui do tipo vector.

04:01

E também ele cria um índice aqui para a gente. Perceba, pessoal,

04:03

eu estou fazendo isso manual, porque a ideia aqui é mostrar...

04:07

essa parte em relação a quando os dados são vetorizados e etc.

04:11

O meu grande questão aqui não está em fazer tudo automático,

04:16

está em fazer isso de forma manual para você entender

04:20

que o dado que a gente vai colocar,

04:22

ele está entrando no banco de dados num formato vetorizado aqui para mim. Então,

04:24

quando eu dou aqui para a gente o insert semantic cache, o que ele está fazendo?

04:29

Eu estou dando o insert no meu Postgres com SQL puro aqui para mim.

04:33

E se você olhar aqui,

04:40

eu tenho um pgvector que basicamente ele só está preparando o

04:42

meu campo aqui para ele conseguir grudar os dados do meu vetor aqui.

04:47

Na realidade ele está formatando simplesmente a entrada. Beleza?

04:52

E então, aqui ele está inserindo essa versão. Então,

04:56

quando eu chegar aqui no meu main.py,

05:00

eu tenho o semantic cache items. Então, esse cara aqui,

05:02

eu consigo fazer essa inserção. Então,

05:06

vamos fazer o teste e rodar. Somente para você saber,

05:09

eu estou utilizando o Docker Compose, tá? Então,

05:12

eu dei um docker-compose up -d e ele subiu o Postgres aqui para mim,

05:15

somente para você utilizar.

05:18

Eu tenho ele aqui para você baixar depois. Tudo isso aí fica disponível para você.

05:21

Beleza? Então, eu vou dar aqui um Python.

05:26

Aqui, main.py.

05:31

Subiu a minha aplicação. Eu vou ver o meu arquivo de teste aqui.

05:35

E agora, eu quero chamar o meu camarada do Semantic Cache Items. Então,

05:40

o texto que eu vou entrar é como eu cancelo a minha assinatura.

05:46

E a resposta... que eu já estou esperando, ou seja,

05:49

eu estou simulando como se eu tivesse chamado a IA,

05:53

categoria cancellation, confidence 0.92,

05:55

reason, usuário quer cancelar assinatura. Ou seja,

05:59

esse cara aqui,

06:03

eu já estou simulando como se ele tivesse feito a chamada para a IA

06:06

e já está retornando esse resultado aqui para ele transformar tudo isso em vetor.

06:12

Então eu vou dar um send request aqui para a gente.

06:17

E espera um pouquinho, porque ele deu um timeout aqui,

06:20

falou que... Ele não conseguiu chamar a minha aplicação.

06:26

Acho que o meu Postgres não estava no ar ainda direito. Deixa eu rodar.

06:34

Agora sim foi aqui.

06:35

Porque ele iniciou o banco de dados aqui para a gente com o pgVector.

06:40

Agora deixa eu dar um sendRequest aqui para a gente.

06:44

E prontinho. Então, se a gente olhar aqui, o cache semântico criado.

06:48

Então, eu tenho o ID no nosso banco de dados,

06:50

o input, o normalize de texto,

06:53

o tamanho da dimensão e se ele foi criado igual a true. E aqui,

06:57

eu tenho esse registro lá para mim. Então,

07:01

eu tenho o ID, o prompt, as rules, o model,

07:03

o normalized text, o embedding, aqui o preview que eu tenho e a minha response aqui.

07:09

Então, esse endpoint agora, no final das contas, o que ele está fazendo?

07:13

Ele está criando esses itens no meu banco de dados.

07:18

Ou seja... Isso aí já facilita bastante a minha vida,

07:22

porque em seguida a gente vai começar a perceber como que,

07:26

utilizando essas informações,

07:28

eu consigo fazer uma busca para ver

07:31

quais vetores estão próximos ou na mesma direção,

07:36

para que a gente consiga entender todo

07:38

esse processo de verificação com similaridade.

07:41

Então, essa é a ideia. Então, nesse caso aqui, a gente inseriu...

07:46

o item aqui no banco de dados. A gente não fez busca, nada disso por enquanto,

07:51

que a gente foi simplesmente subir o banco de dados e fazer a inserção.

07:56

Aí, no próximo vídeo, a gente vai seguir um pontinho de cada vez.

08:00

Então, primeiro a gente aprendeu a criar um embedding,

08:03

agora a gente aprendeu a inserir um embedding no

08:06

banco de dados com Postgres com PG Vector,

08:08

e depois a gente vai para o próximo passo.

## Resumo IA

[RESUMO_IA]