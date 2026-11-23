Módulo: Arquitetura na Era da IA\
Aula: [Melhorando uma busca ruim](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18441)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

Agora eu quero também trazer para vocês coisas que podem ser sutis,

00:07

mas que vão fazer diferença radical,

00:09

muito forte na hora de você trazer o contexto ali para ser enviado para o modelo.

00:16

Principalmente em relação ao header e os metadados. Por que eu estou dizendo isso?

00:20

Antigamente, o que a gente estava fazendo?

00:22

A gente tinha a nossa coluna dos metadados e

00:25

a gente deixava elas para a gente filtrar. Mas, de forma geral,

00:28

a gente não estava colocando isso dentro do conteúdo em si, tá?

00:31

E eu quero fazer aqui para você uma demonstração de

00:35

antes e depois para que você consiga entender,

00:38

tá? Então, aqui no meu ingest, se você olhar,

00:42

eu fiz uma mudança nesse cara no final das contas. O que eu fiz?

00:46

Eu adicionei um parâmetro, tá? Que chama no context header, tá?

00:51

O que isso significa, esse parâmetro no context header?

00:56

ele vai apenas colocar o conteúdo,

01:00

mas não colocar o header com aquelas informações de contexto de onde ele vem.

01:05

Ou seja,

01:06

o conteúdo vai ser passado,

01:08

mas ele não vai necessariamente trazer os pontos

01:13

que podem ser relevantes para a gente trabalhar, que é basicamente aqui.

01:18

Ele vai carregar os documentos e ele vai ativar ou não se ele vai trazer o header,

01:24

aqueles headers dentro dos documentos para a gente fazer a

01:27

busca vetorial para ver o tipo de resultado. Então,

01:30

o que eu vou fazer aqui? Eu vou rodar primeiro,

01:32

eu vou reindexar, olha só, eu vou dar um Python,

01:36

python -m app.ingest, eu vou fazer a ingestão de novo,

01:43

e eu vou colocar no --context --header aqui para mim.

01:49

E aqui, ele fez a ingestão ali para mim. Agora,

01:53

eu vou rodar um Python, "-m", app.index, aqui para mim, e

02:03

ele está fazendo a indexação agora aqui para mim. Primeiro ele gerou o JSON,

02:08

agora ele indexou. E agora, eu vou dar um Python,

02:12

"-m", app.retrieve, e

02:18

aqui eu vou colocar, sei lá, assim, quais são...

02:22

os limites do plano Pro, certo?

02:29

E eu vou colocar aqui, ó, menos --top-key, é 3.

02:37

Olha só o que a gente recebeu agora aqui, ó.

02:41

Vamos lá. Então eu recebi aqui do Billing, olha só,

02:45

nos planos Pro, Enterprise, o volume de gestão,

02:47

que ultrapassar o limite do plano é cobrado. Ele trouxe aqui,

02:52

né, o Chunk ID, Source, Title e etc.

02:56

e o preview aqui para a gente. E a gente tem esses scores aqui. Então, isso aí é

03:03

a forma como a gente estava fazendo, vamos dizer, antes. Ou seja,

03:07

onde nós tivemos somente esse tipo de informação. Então,

03:12

aqui a gente tem esse tipo de resultado.

03:17

Beleza? Então, essa foi a nossa query, o TopKey, sem filtros,

03:22

e eu tive o total... de resultados que eu coloquei.

03:26

Agora, o que eu vou fazer?

03:28

Eu vou colocar com o ingest,

03:33

trazendo os cabeçalhos.

03:37

Mas, antes de eu colocar, eu quero que fique bem claro aqui para você.

03:43

É questão de pensar em contexto. Vamos, inclusive, entender o conteúdo,

03:47

porque agora não tem como não entender o conteúdo das nossas políticas comerciais, etc.

03:52

Se você perceber, eu perguntei quais são os limites do plano Pró.

03:57

Se você olhar no resultado,

04:00

ele está trazendo aqui para mim coisas de cobrança. Se você perceber,

04:06

nos planos Pró e Enterprise,

04:08

o volume de ingestão que ultrapassar o limite do plano é cobrado, como

04:14

consumo excedente e etc. Então, perceba esse tipo de pergunta.

04:22

Ok? Então, aqui, no final das contas,

04:25

ele está trazendo muita coisa referente à cota

04:27

de utilização de cobrança em relação ao nosso plano.

04:33

Outra coisa, ó, cálculo fictício. Outra coisa, tudo de cobrança,

04:38

forma de cartão de crédito, recorrente e tudo mais. Então,

04:41

a gente tem que pensar no REG agora com qualidade de conteúdo. Então,

04:45

o que eu vou fazer agora? Eu vou rodar de novo o esquema do ingest,

04:50

tá? Mas agora, o que eu vou fazer?

04:53

Eu vou rodar aqui de novo o ingest com os headers.

04:58

Então, ele gerou esses caras. Agora, eu tenho que fazer o índice para ele indexar de

05:07

novo. E agora, eu vou fazer de novo a mesma pergunta que eu fiz antes.

05:13

Quais são os limites do plano PRO?

05:17

E agora, olha só a diferença da resposta. Olha só.

05:24

Plano, Enterprise, diferença em relação aos planos Starter e Pró.

05:29

Agora aqui, se você perceber, eu já tenho uma tabela de planos,

05:35

falando o que tem em cada plano.

05:37

Outra coisa, plano Enterprise, documento, o plano traz essas informações.

05:45

Outra coisa no plano.

05:47

Tem esses tipos de benefício em relação aqui.

05:50

Mas o ponto principal aqui, na realidade,

05:53

principalmente em relação à parte de plano, é o quê?

05:57

É que, de uma forma ou de outra,

06:00

principalmente nessa resposta, que seria um candidato bom de usar,

06:03

porque quase tudo que a gente tem é do plano Enterprise,

06:07

mas a gente tem uma tabela que tem um plano Pró. Então,

06:10

nesse aspecto, o que acontece? Ele conseguiu trazer...

06:14

Mesmo trazendo coisas em relação ao plano Enterprise,

06:17

ele conseguiu achar aqui para mim uma tabela onde

06:20

eu tenho informações também do plano Pró.

06:23

E ele não ficou focando na parte de cobrança como ele ficou. Então,

06:28

você consegue perceber que mudou radicalmente a resposta simplesmente

06:31

pelo fato de eu adicionar ou não adicionar os headers. Então,

06:36

perceba que quanto mais contexto você traz...

06:39

mais acertado pode ser o resultado. Então,

06:42

muitas vezes você pode considerar também trazer

06:46

esses headers dentro do conteúdo do documento.

06:51

Na prática, uma coisa que não sei se você percebeu,

06:55

antes a gente estava trazendo o header colocando apenas no prompt.

07:02

Agora, a busca semântica também é feita...

07:06

batendo nesses headers. Ela não é só usada mais como filtro. Mas,

07:11

novamente, fazer isso também vai trazer mais,

07:14

Vai colocar mais dados dentro daquele chunk. Mas, por outro lado,

07:20

esses dados vão poder ajudar a gente também no meio de toda essa história. Então,

07:26

isso aí ajuda bastante a gente a conseguir... a deixar as respostas melhores.

07:32

Então, novamente, são coisas que parecem bobas,

07:36

mas elas são sutis,

07:38

mas essas sutilezas fazem com que a resposta seja diferente.

07:44

Novamente, aqui a questão de reg não é, não está em fazer o programa funcionar,

07:50

está em trazer a resposta correta aqui para a gente.

07:55

Fechou? Então, era isso aí que eu queria passar.

07:58

Agora com headers dentro da nossa resposta.

## Resumo IA

[RESUMO_IA]