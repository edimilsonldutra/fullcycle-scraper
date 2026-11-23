Módulo: Arquitetura na Era da IA\
Aula: [Indexando chunks no Postgres com pgvector](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18415)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, seguinte,

00:02

agora eu tenho aqui o nosso index .py e

00:06

agora a gente está entrando num ponto mais interessante que, na realidade,

00:10

é pegar os chunks que a gente tem e realmente guardar isso no banco de dados.

00:16

Então, basicamente,

00:17

eu tenho dentro desse index .py um carregamento dos

00:23

documentos dentro daquele arquivo chunks .jsonl que eu tenho aqui,

00:27

ou seja, só estou carregando, basicamente é Carregamento,

00:31

não tem muito o que colocar.

00:34

Mas o ponto mais importante que a gente tem aqui é esse index chunks.

00:39

Mas antes disso,

00:40

deixa eu posicionar alguns pontos aqui para vocês que é importante.

00:45

Isso aqui pode parecer um detalhe,

00:46

mas na realidade ele conta. Se você olhar aqui,

00:50

eu tenho um camarada chamado de id column.

00:53

E o name está name, chunk id, data type, text, nullable, false. Por quê?

00:58

Quando nós estávamos no nosso ingest .py,

01:02

a gente criou aqui um chunk ID.

01:06

E esse chunk ID, basicamente, o que a gente estava colocando, né?

01:10

O nome do chunk, tracinho, 0, 1, 2, 3,

01:13

pra gente saber meio que a ordem de como que isso aparece ali no documento.

01:18

Pra gente, inclusive, visualmente, pra buscar,

01:21

pra debugar ou qualquer coisa desse tipo,

01:23

acaba, inclusive, fazendo muito sentido,

01:25

porque a gente sabe qual é a ordem que aquilo foi feito,

01:28

vamos dizer ali, o split, tá? E o que que acontece?

01:33

Esse nome, ele é meio que o padrão que vem na hora que você vai trabalhar ali com...

01:39

O Langchain e Compostgres.

01:41

O grande ponto é que quando você define isso aqui,

01:46

falando qual vai ser a coluna principal do ID,

01:50

você, na realidade,

01:52

está fazendo um conflito com o Chunk

01:55

ID que seria gerado no formato do UUID.

02:00

Está errado utilizar UUID? Não está. Mas eu, pessoalmente, prefiro...

02:07

eu declarar qual que é o ID que eu estou utilizando,

02:11

para inclusive eu entender um pouco melhor de ordem,

02:14

eu entender a forma de debug, acaba sendo melhor, pelo menos na minha visão.

02:19

Eu vejo muita gente também trabalhando dessa forma. Então,

02:22

quando eu estou olhando aqui o meu index .py,

02:26

eu estou apenas falando que o ID dos meus chunks

02:31

que vão ser indexados vão ser baseados no chunk ID. Basicamente é isso.

02:35

É dizendo que a chave que eu vou utilizar aqui

02:37

vai ser o chunk ID que eu acabei criando, tá?

02:41

E aí eu tenho aqui o meu index chunks, tá?

02:43

Então vamos entender o que esse cara faz agora aqui,

02:46

porque tem alguma mágica, tem mágica por trás disso, do framework. Então vamos lá.

02:50

Primeira coisa que vai acontecer é eu estou carregando o

02:54

meu modelo de embedding aqui que eu estou utilizando da OpenAI,

02:58

legal? Aí o que acontece no meio de toda essa história?

03:02

Eu estou fazendo uma pequena query aqui para saber qual que é a dimensão,

03:07

Ou seja, o tamanho do vetor que eu vou trabalhar. Por que eu estou dizendo?

03:11

Porque para cada tipo de modelo de embedding eu posso ter dimensões diferentes.

03:16

Então eu quero saber o tamanho do meu vetor,

03:18

porque isso vai me ajudar também para eu colocar na coluna ali no banco de dados.

03:23

E agora...

03:25

Eu tenho aqui uma opção que é chamada, e se você olhar aqui,

03:28

Está recreate the vector table, atualizando os conteúdos que já existem.

03:35

Por que eu estou dizendo isso? Porque essa parte é idempotente.

03:39

O que isso significa? Eu posso rodar isso quantas vezes eu quiser.

03:44

E ele não vai duplicar os dados. Ou ele não vai dar erro ao criar a tabela.

03:50

Ele roda a primeira vez. Se rodar de novo,

03:52

ele simplesmente pode ignorar ali para a gente.

03:56

Então, a gente não tem esse tipo de problema. Então, esse cara aqui,

03:59

quando eu estou usando o PG Engine, normalmente a gente usava o PG Vector e etc.

04:07

Não digo que ele ficou depreciado,

04:09

mas agora é mais utilizado essa lib. Então, o que acontece?

04:13

Aqui eu estou fazendo uma conexão com o banco de dados,

04:17

estou aqui inicializando a minha tabela de vetor,

04:23

onde eu estou colocando o nome da minha tabela, estou colocando o tamanho do vetor,

04:27

estou falando qual vai ser o ID da minha coluna, que é aquele chunk ID.

04:32

E estou falando que é para ele substituir os

04:35

dados existentes caso eu rode esse cara aqui.

04:38

E aí, o que acontece para a gente?

04:41

Eu vou na segunda parte, que é abrir essa tabela,

04:47

de forma geral, para escrever os chunks dentro dela.

04:52

Ou seja, para cada linha daquela que é um chunk,

04:54

eu vou criar ali uma linha no banco de dados.

04:57

Então, o que acontece aqui no meio da história?

05:01

Eu vou falar qual que é o engine que eu estou usando,

05:03

que eu acabei de configurar aqui em cima.

05:05

Qual que são os embeddings que eu vou utilizar,

05:08

que é o modelo de embedding que a gente pegou aqui em cima.

05:12

Eu vou pegar o nome da tabela,

05:14

vou falar qual que é a coluna de ID que eu vou trabalhar.

05:17

E agora, o que eu vou dar aqui para a gente? Um add document.

05:22

E aí, como é que vai funcionar? Eu tenho...

05:25

os meus documentos e eu vou separar os meus documentos de qual forma.

05:29

Isso aqui é o Python facilitando a vida, mas às vezes,

05:31

para quem não entende de Python, acaba não entendendo.

05:34

Eu tenho a minha lista de documentos e eu vou fazer o seguinte,

05:37

que os IDs que ele vai correr vão ser

05:41

baseados no Chunk ID para cada documento que ele recebeu.

05:46

E isso aqui vai fazer a adição ali no banco de dados. Ou seja,

05:50

eu vou adicionar ali... no meu banco de dados, nas minhas tabelas,

05:55

todas aquelas informações,

05:57

onde o meu ID vai ser o chunk ID e

05:59

o restante dos documentos vão ser adicionados ali dentro.

06:04

Quando eu executar esse cara, o meu index.py,

06:09

ele vai criar a tabela para mim e depois fazer o

06:12

store e adicionar todos esses documentos ali no meu banco de dados.

06:17

E eu vou executar esse cara aqui.

06:21

Vamos lá, mas agora aqui é o ponto index.

06:27

Então, ele ainda tem lá os 106 itens.

06:30

Perceba que ele demorou um pouquinho mais, mas agora,

06:32

olha só, indexando os chunks na tabela tal,

06:35

106 itens indexados e terminei a indexação.

06:39

E agora, se eu for aqui no meu banco de dados,

06:42

deixa eu dar um play aqui de novo no camarada aqui, minha extensão.

06:50

Olha só que interessante.

06:52

Eu tenho Billing Policy 0, 1, 2, 3, 4, 5. Por isso que eu estou dizendo,

06:57

esse Chunk ID acaba sendo a chave onde eu vou buscar.

07:00

Mas quando eu olho aqui,

07:02

eu sei de qual tipo de documento que eu estou falando aqui para mim.

07:05

Então acaba ficando um pouco mais simples.

07:07

Caso você não queira trabalhar dessa forma,

07:09

não tem problema. Todo esse cara aqui vira um UUID e vai funcionar de boas.

07:14

Eu gosto de trabalhar aqui dessa forma. Agora, o interessante de tudo isso,

07:19

deixa eu diminuir o zoom desse cara para você conseguir ver melhor.

07:21

é que eu tenho o Chunk ID,

07:23

o Content, e é aí que muita gente acaba não entendendo e acaba se confundindo.

07:29

Pessoal, o chunk, ou seja, aquele pedaço de texto que a gente pega,

07:33

a gente vai colocar ele no banco de dados de forma pura. Se você olhar aqui,

07:38

isso aqui é o conteúdo que a gente splitou,

07:41

tá vendo? Mas além do conteúdo que eu estou colocando,

07:47

eu também tenho... esse mesmo conteúdo no formato vetorizado. E aí,

07:52

por isso que eu tenho aqui uma coluna chamada de embedding.

07:55

Porque essa coluna embedding é a representação desse texto aqui no formato de vetor.

08:02

Então, quando eu for fazer uma busca semântica,

08:06

eu não vou fazer um select onde o content like alguma coisa aqui nessa coluna.

08:12

Eu vou fazer uma busca onde o vetor é mais próximo, tá?

08:16

desse vetor que está, dos vetores que estão aqui dentro. Então,

08:20

isso aí é um ponto importantíssimo para você levar em conta.

08:25

Outra coisa agora que eu tenho aqui é a minha coluna de metadados. Por padrão,

08:30

o Langchain deixa Langchain Metadata.

08:33

mas você não é obrigado a seguir essa convenção, escolher esse nome,

08:37

eu estou deixando como é padrão, eu ia mudar,

08:39

mas como o framework deixou isso como padrão,

08:41

eu estou deixando o padrão aqui para você, mas você não é obrigado a isso.

08:45

E aqui no metadata, o que acontece se você olhar? Eu tenho o Title,

08:50

Política de Faturamento, o Tenant, aqui o Produto,

08:53

o Plano, o Policy, o Status da Versão,

08:56

aí eu tenho o Chunk ID, o Source File,

08:59

eu tenho o Chunk Index, a seção que ele vem,

09:02

e o tamanho desse cara aqui. Se você perceber, o Chunk ID, né?

09:07

Ele tá aqui replicado e repetido, né? Baseado no ID que eu tô buscando, tá? Então,

09:13

eu tenho ele repetido ali no meu metadata. Então,

09:15

por isso que tem gente que deixa aqui como UUID,

09:18

porque no metadado, ele já consegue pegar o Chunk ID aqui.

09:22

Mas eu prefiro colocar o Chunk ID como chave aqui.

09:25

Mas aí vai depender muito de como você vai trabalhar.

09:28

Eu já vi pessoas trabalhando de diversas formas. De qualquer forma,

09:32

O ponto importante é e é interessante aqui para você é esse índice,

09:36

Para você saber qual é a ordem desse Chunk.

09:40

Porque quando você explica um documento,

09:42

Você explica ele em uma determinada ordem. Então, pedaço 1,

09:46

Pedaço 2, pedaço 3. Então, eu tenho aqui o Chunk Index que eu preciso.

09:52

Se você olhar, eu tenho vários documentos aqui, né?

09:55

E esses documentos, cada documento tem os seus metadados.

09:59

Esses metadados é o que vão fazer muita diferença na hora de você fazer as buscas,

10:03

Né? E os vetores são esses caras aqui, ó.

10:05

São caras gigantescos aqui,

10:08

De um trilhão de, mil e quinhentos e poucas posições esses aqui,

10:12

Onde vai representar exatamente esse conteúdo que é um pedaço de chunk.

10:17

Então, esse pedaço aqui... É esse cara aqui.

10:21

Perceba que eu tenho aqui mensal, anual. Está vendo?

10:24

Se eu pegar o 6 aqui, você vai ver que eu tenho nossos planos, etc,

10:30

Etc e tal. E aqui eu tenho um outro pedaço onde eu vou trabalhar.

10:34

Então, aqui eu vou tendo os pedaços de texto.

10:37

E quando eu fizer a busca no banco de dados, o que acontece?

10:41

Eu vou trazer somente esses pedaços desses documentos e não o documento inteiro.

10:45

E daí a gente entra em outro aspecto.

10:48

Mas o ponto importante de você entender aqui,

10:49

Principalmente, é isso aqui que eu trouxe.

10:53

Saber que eu configurei o modelo de embedding,

10:56

Que eu criei a tabela no banco de dados,

10:57

E que eu fiz o store daqueles documentos que estavam aqui no meu arquivo JSON.

11:04

Uma observação importante, claro, como eu estou fazendo isso aqui passo a passo,

11:08

Eu gerei os arquivos JSON para fazer a importação.

11:11

Mas não necessariamente você precisa fazer isso.

11:14

Você poderia consultar o banco de dados e dar consulta do banco de dados,

11:18

Já ir fazendo a inserção no banco sem ter que gerar um arquivo JSON, tá?

11:23

Somente para você saber. Existem várias formas. Muita gente,

11:26

Quando você vai trabalhar com muitos dados,

11:27

O que você acaba fazendo? Você pega todos esses dados, joga para uma fila,

11:32

Para um RabbitMQ, para uma Apache Kafka,

11:34

E daí você bota ali num pipeline somente para fazer a ingestão num banco de dados.

11:40

Então, tem diversas formas de você arquitetar...

11:43

Fazer a arquitetura de tudo isso, tá? Então, esse aí é um ponto importante,

11:47

Mas é interessante você saber que o que a gente fez aqui no

11:50

Final das contas foi conseguir jogar isso agora para um banco de dados,

11:55

Fechou? Então é isso aí, galera, espero que você tenha curtido,

11:58

Até o nosso próximo vídeo.

## Resumo IA

[RESUMO_IA]