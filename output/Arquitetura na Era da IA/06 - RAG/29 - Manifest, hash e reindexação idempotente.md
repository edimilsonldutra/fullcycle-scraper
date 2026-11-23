Módulo: Arquitetura na Era da IA\
Aula: [Manifest, hash e reindexação idempotente](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18450)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, no vídeo anterior a gente falou sobre a importância que a gente

00:05

tem de conseguir saber se os documentos base que a gente tem,

00:10

se eles realmente são fiéis.

00:12

Lembrando que esse banco de dados não é a fonte da verdade.

00:16

A fonte da verdade é o documento no qual ele se baseou.

00:19

Então, o que acontece aqui? Primeiro,

00:22

eu vou mostrar o comportamento e depois a gente vai para o código,

00:26

mais ou menos como a gente tem feito nas últimas aulas aqui.

00:29

Então, a primeira coisa é o seguinte,

00:31

eu vou rodar aqui no Python, eu vou rodar python -m, opa,

00:38

vamos lá, python -m app.index. Esse cara,

00:42

ele indexa os documentos, tá? Se você olhar agora aqui,

00:46

eu tenho sources aqui nos oito chunks,

00:52

está se conectando com Postgres,

00:53

nada foi mudado, mas olha só, ele tem aqui um data.

00:59

indexmanifest.json. Então, se eu olhar agora aqui,

01:03

eu estou gerando um novo arquivo, que é esse cara, indexmanifest.json.

01:10

Esse arquivo aqui, é um arquivo que ele faz o que no final das contas?

01:15

Ele tem os chunks IDs de cada documento.

01:22

Então, se você olhar aqui, eu sei que o billing police,

01:25

ele tem esse hash desse documento, o título, o tenant,

01:29

a versão, e os IDs desses caras aqui dentro.

01:34

Eu tenho a política comercial, eu tenho o hash, política comercial,

01:39

e tenho os IDs desse cara aqui também. E assim por diante.

01:44

Ou seja, basicamente, esse hash aqui é o que torna esse documento único.

01:50

Os chunks IDs, basicamente, a gente está utilizando, inclusive, o começo.

01:55

desses hashes também, aqui também, tá? Então,

01:58

a gente tem todos esses caras aqui indexados.

02:02

Obviamente, pessoal, eu estou jogando isso num arquivo JSON,

02:04

provavelmente esse manifesto estaria num banco de dados,

02:07

tá? No dia a dia, no mundo real, tá?

02:11

Então, o que que acontece aqui? Eu tenho,

02:14

e eu chamei esse cara de pipeline -reg -v1, tá? Então,

02:18

é basicamente esse cara que eu tenho aqui disponível pra mim,

02:22

que eu dei um nome aqui do meu pipeline. Agora,

02:25

o que isso me ajuda no final das contas? Eu mandei indexar esses documentos.

02:32

Então, ele gerou esses documentos aqui. Ou seja,

02:35

ele achou oito documentos e não teve nenhuma mudança. Ou seja,

02:41

teve oito não mudanças nos nossos arquivos. É basicamente isso que aconteceu.

02:46

Agora, o que eu vou fazer aqui para a gente entender um pouquinho mais?

02:51

Seguinte, eu vou pegar...

02:53

E vou adicionar uma nova linha no meu documento do ProPlan.

02:58

Deixa eu aqui, ó. Vou chegar aqui no meu ProPlan, certo?

03:05

Eu vou colocar ProPlan.

03:08

É o plano self-service voltado e tal. E eu vou fazer aqui o seguinte.

03:13

Todos os números são fictícios.

03:14

Eu vou colocar uma exclamação aqui na frente para mim,

03:18

tá? Ou seja, eu fiz uma alteração nesse documento, se você perceber. Agora,

03:24

o que acontece no meio de toda essa história?

03:28

Se eu chegar e rodar, vamos lá, aqui,

03:32

Python -m app .ingest,

03:38

aqui para mim,

03:39

e depois eu posso dar um Python -m app .index,

03:46

o que ele vai fazer? Ele vai fazer a ingestão dos documentos, certo? E a indexação.

03:52

desses caras aí. Quando ele for fazer a ingestão, ele vai perceber,

03:56

inclusive, se houve mudança pra, inclusive, ele fazer esses ajustes. Então,

04:02

eu vou dar um enter aqui e vamos ver o que vai rolar. Olha só.

04:09

Vamos nessa. Então, o que aconteceu agora aqui? Olha só.

04:13

Carregando documentos da base de dados, ler os oito documentos,

04:17

gerando os chunks, gerando os headers, tal, tal, coisado, 134 chunks,

04:23

né? E salvou isso aqui no chunks .json .jsonl,

04:28

que é o que a gente sempre fazia no processo de ingestão. Beleza?

04:32

E aqui tem alguns exemplos de chunks que a gente tinha,

04:35

que é o que a gente acabou fazendo ali.

04:38

Maravilha? Agora, o que acontece?

04:41

Uma vez que a gente leu esses chunks, ele achou oito caras, certo?

04:47

Zero nova sources, ou seja,

04:48

não encontrou mais nenhum novo cara que a gente adicionou.

04:51

Mas ele viu que teve uma mudança dessas

04:55

fontes, desses documentos. Certo? Teve algum documento removido? Não.

05:01

Teve documentos que não foram alterados? Teve. Sete. Um mudou, sete foram alterados.

05:06

E aqui ele fez o quê então? Ele deletou 15 chunks e adicionou,

05:13

indexou novamente 15 chunks. O que significa no final das contas?

05:18

Aquele documento que a gente alterou,

05:21

Ele simplesmente foi removido do nosso índice porque o

05:27

hash dele não bate mais com o conteúdo dele.

05:33

Ou seja, quando eu coloquei o exclamação, o hash dele mudou. Se ele mudou,

05:37

eu consigo perceber que houve uma diferença no conteúdo

05:40

que eu tinha e que está indexado.

05:43

Quando ele viu essa diferença, ele falou, opa,

05:46

esse documento aqui mudou. Então,

05:48

deixa eu remover isso do meu índice do banco de

05:50

dados e agora eu vou reindexar nessa versão.

05:54

E não só isso,

05:55

eu vou atualizar também o meu manifest .json

05:59

que agora consta essa nova versão que foi colocada. Agora,

06:04

uma coisa que é interessante aqui também é que eu posso fazer algo do tipo.

06:09

Vamos imaginar aqui, eu posso dar um...

06:13

sei lá, mv, knowledge base, proplan

06:20

.md, e eu vou jogar ele aqui na raiz do meu projeto.

06:25

Por que eu joguei na raiz do meu projeto?

06:27

Para ele não ficar dentro dessa pasta. Ou seja,

06:30

esse documento não existe mais no nosso sistema.

06:34

Então, o que eu vou fazer agora? Eu vou rodar o ingest e o index novamente.

06:41

Vamos deixar esse cara rodar. E olha só o que acontece agora.

06:45

Ele carregou os documentos,

06:47

carregou os chunks, mas agora ele percebeu que um documento foi removido. Ou seja,

06:52

ele viu que de todos os documentos que existiam,

06:54

aquele documento foi removido. Então, o que ele fez?

06:58

Deletou os 15 chunks que existiam desse documento

07:02

E salvou esses dados atuais no manifest.

07:05

Então, ele sempre vai bater o manifest com o que a gente está ingerindo.

07:10

E o que a gente está indexando, se tiver alguma mudança,

07:13

ele vai perceber e vai fazer essa alteração. Se eu quiser voltar esse cara aqui,

07:17

Cadê o meu arquivo que eu joguei ele para a raiz aqui, né?

07:22

Cadê? Onde que eu deixei esse arquivo nosso? Ele deve estar em algum lugar. Knowledge Base.

07:31

Cadê meu Pro Plan aqui?

07:32

De onde que eu mandei esse documento? Meu documento desapareceu.

07:37

Cadê o meu Pro Plan?

07:40

Onde é que eu dei um MV?

07:46

Aonde que eu dei aqui,

07:51

knowledge .mv pro plan, menos, menos, barra.

07:55

Ele deve estar por aqui. Cadê meu documento?

08:00

Ah, ele deve ter parado em...

08:03

Ah, eu estava dentro da pasta principal, né? Óbvio. Então,

08:09

eu tenho que dar um mv pro plan para

08:13

dentro da nossa pasta, que é o nosso Knowledge Base. Aqui de volta.

08:18

E agora eu vou rodar de novo o meu ingest e o index.

08:24

E agora, olha só o que ele detectou. Que entrou um novo sorte de documento,

08:29

e foram 16, 15 caras indexados aqui dentro,

08:34

e foi atualizado aqui o nosso index manifest.json.

08:40

Então, se você olhar agora,

08:42

basicamente o que a gente tem é esse indexador garantindo que...

08:48

a gente tem os documentos tudo em ordem. Se eu rodar de novo esse cara,

08:52

é demotente, ou seja, ele vai bater, nada mudou, os hashes estão todos iguais,

08:57

então ele acaba não fazendo nada, tá? Então, é basicamente essa que é a ideia.

09:02

E, obviamente, pessoal, em larga escala,

09:04

normalmente esses processos começam através de...

09:08

Chrome Jobs, eventos, dados que estão vindo de uma plataforma de streaming, sei lá,

09:13

um Apache Kafka, um RabbitMQ. Então,

09:16

tem diversas formas de como essas coisas acontecem.

09:19

O fato é que existe um manifesto que você consegue

09:22

fazer essa verificação para garantir que tudo está funcionando de acordo. Beleza?

## Resumo IA

[RESUMO_IA]