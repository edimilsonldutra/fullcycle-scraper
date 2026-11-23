Módulo: Arquitetura na Era da IA\
Aula: [Entendendo falhas de onde e quem](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18788)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, no vídeo anterior eu falei que eu ia mostrar agora quando a gente tem uma falha,

00:07

mas essa falha pode ser um pouquinho mais confusa

00:10

da gente entender e localizar o problema.

00:13

Onde e quem, no final das contas, eles são diferentes. Então,

00:18

o que eu vou fazer? Eu tenho aqui um caso onde...

00:23

A pergunta tem muito mais a ver sobre qual que é o e-mail do financeiro, tá? Então,

00:28

depois a gente pode até ver ali no dataset a pergunta,

00:32

tá? Mas o grande ponto aqui é,

00:34

ele vai rodar e a gente vai tentar entender o que está acontecendo aqui, ó. Então,

00:40

se você olhar, eu tenho o Planner Clarification Match,

00:43

está dando 1, então esse cara passou.

00:45

Depois, o Planner Doctype Coverage dá 1, mas o Plan Match aqui dá 0. Depois,

00:51

o Retrieval Source Hit dá 0, 0 e 0. Então,

00:56

o que acontece aqui de cara que eu consigo perceber?

01:01

Ele deu falha no Rerank e ele deu falha aqui no Retrieval para mim também.

01:06

E por que acabou dando essa falha?

01:09

Um, porque esse Plan Match, no final das contas,

01:12

ele falhou. Na realidade, esse cara aqui...

01:18

dependendo da situação, ele poderia ser não aplicável. Na realidade,

01:22

eu teria que entender o que está acontecendo. Se você olhar,

01:25

eu estou tendo problemas no source e no Retrieval Source Hit.

01:31

Mas aqui a questão não está necessariamente em relação ao plano. Então,

01:36

eu não estou preocupado ali com o plano.

01:38

Por quê? Porque o plano aqui não é relevante,

01:41

porque ele está fazendo uma pergunta de qual que é o e-mail do financeiro.

01:44

Isso não tem a ver necessariamente com o plano. Então, no final das contas,

01:48

eu tenho aqui, se você ignorar o plano,

01:51

eu tenho o Clarification de 1, o Doctype, a Coverage aqui da 1,

01:56

ou seja, ele consegue identificar o tipo de documento. E aqui,

02:00

esses dois caras aqui, eles começam a dar problema. E daí,

02:04

qual que é a sensação que a gente tem? Opa,

02:08

o problema aqui está no Retrieval, no Sort Hit. O problema está no Reranking.

02:14

Mas na realidade, sim, esses caras deram um zero.

02:17

Realmente eles não passaram. Mas por que eles não passaram?

02:21

Talvez por conta do Clarification Match. E o porquê que eu estou dizendo isso?

02:27

Se você der uma olhada e for mais a fundo,

02:31

você vai perceber que se eu fizer uma busca aqui no meu dataset, deixa eu dar um Enter aqui.

02:40

Se eu buscar financeiro, arroba, no meu Knowledge Base, aqui no meu Company Info,

02:46

você vai ver que eu tenho um local onde eu tenho um e-mail.

02:50

Ou seja, isso aqui está funcionando.

02:53

Ou seja... Agora, por que ele não conseguiu ajustar esse detalhe aqui para mim?

03:00

E a resposta,

03:01

na realidade, pode ser um pouco capciosa. E é aqui que entra a história.

03:07

Esses caras, de forma geral, o Reranker, por exemplo, ele não errou.

03:12

Ele recebeu, se você for olhar, oito chunks, daí eu mostro para vocês,

03:17

de billing policy. E apesar de ter billing ter a ver com financeiro,

03:23

A parte de billing não é um local onde tem as

03:26

informações da empresa com o e-mail da história.

03:29

Então, isso aí que acaba entrando no meio da história.

03:34

Por que eu estou dizendo isso? Olha só,

03:35

Se eu der um app retrieve financeiro, financeiro.fca.example,

03:42

você vai ver que eu recebi dois chunks de resultados.

03:45

E isso aí é importante, porque esses chunks têm os e-mails que eu preciso.

03:52

Ou seja, a informação existe.

03:56

Agora, olha só que interessante.

03:58

Se eu fizer uma busca nesse

04:02

mesmo cara com Top K de 2,

04:06

do meu bolo de cenoura,

04:09

eu quero receita de cobertura de bolo de cenoura,

04:12

o que vai acontecer no meio da história aqui?

04:16

Você vai perceber que ele trouxe esses caras aqui.

04:22

Sem nenhum filtro. E o que está acontecendo?

04:26

Olha o tipo de documento que ele está trazendo aqui no meio da história.

04:32

Por que isso, no final das contas,

04:34

acaba acontecendo aqui? Primeira coisa, se você perceber,

04:39

o tipo de documento aqui, na realidade,

04:46

ele está pegando a policy, certo?

04:50

Aqui como política de faturamento. E aqui, billing policy.

04:54

Então ele está pegando com política de faturamento.

04:56

E aí você deve estar pensando, o que o bolo de cenoura tem a ver com isso?

04:59

Lembra que na hora que ele vai fazer a busca vetorial,

05:01

ele tenta buscar tudo aquilo que tem a menor distância?

05:06

Então, está acontecendo exatamente isso aqui. Esse score aqui, ele está dando 0,77.

05:14

Agora, esse 0,77, aqui nesse caso, é o pior resultado.

05:18

E o porquê que eu estou dizendo isso? Quando você faz uma busca semântica ali,

05:23

fazendo a Semantic Search with Score, o que ele vai trazer?

05:27

Ele vai trazer a busca semântica, tá? Normal,

05:33

da forma como ela é para ser, tá?

05:36

Porém, o que acontece no meio dessa história, tá?

05:41

Quando eu faço a receita de bolo, que não tem nada a ver,

05:44

e ele vem com 0,77, esse número do score é a distância,

05:49

não é a semelhança. Quanto menor a distância, mais perto ele está. Quer dizer,

05:56

quanto menor esse número, mais perto ele está ali do meu vetor.

06:02

Então, no final das contas, o nome do método,

06:05

quando a gente usa a busca lá no Langchain, é Similarity Search.

06:09

Mas o que ele devolve junto ali é a distância,

06:12

tá? E o Postgres, ele ordena pelos menores. Então,

06:16

o que acontece no meio de toda a história é que

06:20

não é que o código tem como errar isso,

06:24

na realidade, porque ele não compara o score.

06:26

Ele pede os oito melhores e usa o que vier na ordem que vai vir,

06:32

tá? Então, quem ordena no final das contas aqui é o banco. O score,

06:36

ele só aparece no debug quando eu vou olhar. Então, o grande ponto,

06:41

se eu quiser pegar realmente o grande problema aqui,

06:44

é esse aqui que eu quero trazer.

06:46

Então, fique esperto, galera. Esse aqui é a distância, 0,77.

06:51

Quanto menor essa distância, mais perto eu tenho. A gente está falando de um vetor.

06:55

O 0,0, nesse caso, é onde ficam as coisas iguais. Então,

07:00

somente para eu mostrar isso, acho que agora vai ficar mais claro,

07:03

se eu trouxer exatamente a pergunta que está sendo feita lá no dataset.

07:09

E olha só o que vai acontecer aqui.

07:12

Se eu falo que o Doctype é Company aqui para mim, e

07:17

a gente for olhar, olha

07:19

só que interessante.

07:21

Eu tenho um chunk com 0.51,

07:24

que já é menor que o 0.77, que tem as informações.

07:29

Eu tenho outro cara aqui também com 0.51.

07:33

Eu tenho outras perguntas e etc. Agora, se quando você olha aqui,

07:37

qual que é o Doctype que eu coloquei?

07:40

Eu coloquei doctype igual a company, onde eu tenho informações da empresa, certo?

07:45

Agora, se eu fizer a mesma coisa, certo?

07:49

Onde o tipo de documento é policy, olha só.

07:53

Perceba, o doctype aqui é policy.

07:56

Ele vai trazer exatamente aqueles documentos que eu estava colocando.

08:01

E se você perceber aqui, a gente começa a pegar as informações,

08:05

mas que não tem o resultado correto, tá?

08:09

Ou seja... Por que não está tendo resultado?

08:12

Porque eu estou buscando num tipo de documento diferente. Então,

08:16

o nosso maior problema aqui no final das contas foi que

08:21

quando eu fiz a minha busca e rodei o meu EVOL,

08:25

o que aconteceu é que quando eu coloco o TopKey 8,

08:29

ele vai trazer os oito primeiros caras que

08:32

ele teve aqui ordenando pelo aquele score.

08:35

E o que vai acontecer? Os oito caras primeiros que vão aparecer,

08:40

são caras com um tipo de documento na parte de policy.

08:44

Mas o tipo de documento que tem a informação correta é o tipo de company.

08:51

Ou seja, quando eu trouxe o documento, como que eu posso dizer?

08:57

de policy, eu nunca ia ter a resposta.

09:00

Então, como que eu resolveria esse tipo de problema,

09:03

por exemplo? Talvez aumentar o top key,

09:05

porque daí eu não iria pegar somente documentos de

09:08

policy e eu pegaria talvez também documentos de company,

09:12

onde tem a resposta. Ou eu poderia melhorar o meu prompt,

09:15

eu posso fazer um monte de coisa.

09:17

Mas o grande ponto aqui que

09:19

eu consigo perceber agora é que quando...

09:24

eu entro nesse tipo de situação,

09:27

eu acabo tendo uma explicação quase que sozinho no meio dessa história.

09:34

A grande sacada que a gente tem que pensar nesses

09:38

casos é muitas vezes o problema está sendo apresentado numa...

09:45

por exemplo, como o re-rank, que deu zero,

09:47

mas o problema estava numa etapa anterior,

09:49

que nesse caso foi na hora que ele foi fazer

09:52

essas seleções desses documentos lá na busca semântica,

09:55

e ele pegou,

09:56

classificou os documentos certos, porém não tinha uma quantidade grande de top K,

10:02

e o score acabou vindo feito por essa seleção do banco de dados.

10:07

Então, aqui nós realmente temos uma falha. Então,

10:11

a gente tem que tomar muito, mas muito cuidado com esse tipo de coisa,

10:15

porque senão a gente sai mudando em tudo quanto é lugar.

10:18

Então, a gente tem que realmente fazer essa análise e entender o que aconteceu.

10:21

Quando agora eu faço essa busca normal,

10:25

quando eu faço essa busca sem Doctypes e coisas desse tipo,

10:32

aí a coisa acaba ficando sempre mais simples para eu conseguir olhar.

10:37

Se eu dou um TopK 8,

10:39

você vai ver que todos os documentos que retornam aqui são de policy. Então,

10:44

os oito primeiros documentos que estão retornando aqui são de policy.

10:48

E como eles são de policy, o que vai acontecer?

10:51

Ele nunca vai chegar, no final das contas,

10:53

na parte de company que é onde tem o resultado que eu estava esperando.

10:57

E aí que eu acabo tendo aquele problema de classificação.

11:03

Eu não estou querendo trazer aqui como que a gente resolve,

11:06

existem formas de resolver no final das contas,

11:09

que é aumentar o TopK, melhorar o Prompt, coisas desse tipo,

11:12

mas eu sei agora especificamente o problema.

11:15

E eu acho que esse é o aprendizado principal desse nosso bate-papo.

11:20

Entender que quando a gente tem uma falha lá na frente,

11:23

a gente entender qual é o componente que a gente está com o problema.

11:26

E nesse caso, falou que o problema, quem falhou foi o re-rank, por exemplo.

11:31

Mas o problema estava onde? Nessa parte de classificação que acabou acontecendo, tá?

11:37

No nosso próximo vídeo, o que eu vou fazer?

11:39

Eu vou rodar esse... esse EVOL de componentes,

11:43

jogando tudo para o Langfuse,

11:45

para que você consiga entender como que eu

11:48

consigo visualizar isso de uma forma melhor,

11:51

olhando os scores e fazendo a comparação lado a lado, tendo um baseline principal,

11:56

que vai ser essa primeira rodada, para a gente olhar.

11:59

Então, vamos ver isso aí no próximo vídeo.

## Resumo IA

[RESUMO_IA]