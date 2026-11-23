Módulo: Arquitetura na Era da IA\
Aula: [Trabalhando de forma assíncrona](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18316)

## Resumo da aula



## Transcrição

00:01

Bom pessoal, e agora a gente está aqui no nosso último exemplo.

00:04

Então o primeiro exemplo que a gente teve é fluxo síncrono,

00:08

onde a mensagem é bloqueante. Segundo exemplo é streaming,

00:12

que é o que a gente viu agora há pouco.

00:15

E agora a parte assíncrona. Então a parte assíncrona, nesse caso,

00:20

como é que ela vai funcionar de forma geral?

00:23

Eu vou ter um endpoint que eu chamei de Full Analysis.

00:27

O que esse endpoint faz? Ele manda o request inicial,

00:31

tá? Quando ele mandar o request inicial,

00:34

o que vai acontecer? A gente vai ter aqui um jobs.createJob,

00:41

aqui para que você, olha aqui, jobs.createJob.

00:44

Se eu for no meu jobs.py, você vai ver que o createJob,

00:48

basicamente, ele vai gerar um ID ali para mim,

00:51

tá? E ele vai retornar isso aqui para mim, um cara aqui com status pending, aqui.

00:58

Beleza? Basicamente é isso. Eu tenho um getJob, que vai retornar basicamente o job,

01:05

ou não vai retornar nada caso não exista. Eu tenho markProcessing,

01:09

ou seja, se tiver em processamento. Eu tenho markComplete,

01:12

para dizer se ele foi completado.

01:14

E eu tenho um markFailed, caso tenha dado algum erro.

01:18

Então, esse jobs.py, basicamente,

01:19

ele fica mudando o status e tem o createJob inicial,

01:23

que é somente para criar e a gente... ter o ID do nosso job aí de forma geral.

01:29

Então, quando eu estou aqui no meu Full Analysis,

01:36

o que vai acontecer é que ele vai dar um createJob

01:40

e aqui eu vou utilizar um background.addTask aqui no meu Python, certo?

01:47

Onde eu vou dar aqui para ele processar o job aqui para mim,

01:50

que é exatamente essa função que vai fazer o quê?

01:54

Vai marcar o cara como processando, vai chamar o meu client da IA,

01:59

e assim que esse client terminar,

02:02

ele vai marcar como completo, caso o contrário, ele vai marcar como falhou.

02:07

Então, na prática, o que vai acontecer? Quando eu executar o meu Full Analysis,

02:12

ele vai criar o job, e por padrão, nesse caso, o job já inicia ali como pending.

02:20

Quando... começa a processar, a gente marca ele como processing,

02:24

e depois, quando ele termina aqui,

02:27

a gente marca ele como completo. Então,

02:29

eu tenho esses status onde eu consigo acompanhar. O ponto principal aqui é que,

02:35

quando eu rodo um Full Analysis, no final das contas,

02:38

eu só tenho um createJob e ele só vai me retornar um jobID como pending.

02:43

Fora isso, tudo vai acontecer via background.

02:47

E quando eu falo background aqui, galera,

02:49

eu dei um exemplo muito simples que vai rodar em background aqui no Python, né?

02:53

Mas o rodar em background ou de forma síncrona,

02:55

pode ser colocar isso dentro de um Redis, pode ser colocar no RabbitMQ,

03:00

pode ser jogar isso para um Kafka, não interessa.

03:03

O ponto é que esse negócio, ele vai rodar...

03:05

fora da minha thread principal para não ficar segurando o meu servidor HTTP.

03:11

E quando tudo fica pronto, aí sim a gente vai poder pegar o resultado.

03:16

Deixa eu subir aqui o servidor. Então,

03:21

vou colocar aqui python main.py.

03:26

Está rodando, certo? E agora eu tenho aquele meu HTTP.

03:33

Cadê meu arquivo?

03:35

Requests .http. E aqui no final, o que eu fiz?

03:38

Eu fiz para ele trabalhar com uma variável,

03:40

tá? Então, o que acontece aqui no meio da história?

03:44

Eu dou um request onde ele vai criar um job, tá? E o resultado desse job, né?

03:51

Aqui ele vai gerar uma variável. E aqui eu tenho outro request com um get,

03:56

que é o get jobs,

03:57

onde eu vou passar o ID do job criado para eu ver... a resposta dele. Então,

04:02

se você olhar aqui, eu tenho o getJobs,

04:05

onde eu passo o ID, onde eu consulto aqui, na realidade,

04:09

o status do job que eu tenho agora, nesse momento.

04:14

Então, basicamente, é isso que acaba acontecendo. Então,

04:17

deixa eu voltar aqui para o meu request .http.

04:20

Vou mandar meu request aqui para esse meu cara.

04:25

E ele está acontecendo o mesmo esquema que estava acontecendo naquela hora.

04:28

Deixa eu dar um request. Eu acho que é Ctrl+Tab que eu aperto pra ele aparecer

04:36

pra mim aquela bendita janelinha aqui pra gente conseguir olhar o resultado. Pera aí.

04:42

Bom, pessoal, coloquei do jeito que eu não queria muito,

04:44

mas foi aqui, tá vendo? Então eu vou clicar aqui Send.

04:47

E aqui ele trouxe a request como pending. Se eu clicar aqui no Send Request agora,

04:52

você vai ver que eu já tenho esse cara como Completed.

04:55

E é o mesmo cara, tá vendo? Então eu vou dar um Send.

04:59

Depois, em seguida, um send request e aqui eu tenho esse cara aqui como completed.

05:05

Então, essa que é, vamos dizer assim,

05:08

a ideia principal de como que a gente consegue trabalhar com ele.

05:12

Porque uma vez que eu mando a request, ele vai criar o meu job ID.

05:16

E ele ficou como um pending. Quando eu dou um send request aqui nesse momento...

05:21

Ele já está dando como completed,

05:22

mas ele poderia estar dando como processing, por exemplo. É que como é muito rápido,

05:27

né? Então, nesse caso, eu não consigo nem ver o intermediário.

05:31

Mas, de forma geral, é isso que acontece. Então, essa minha chamada inicial,

05:36

ela não ficou bloqueando absolutamente nada. Ela só gerou e retornou um ID para mim.

05:40

E a partir desse ID, agora eu faço meio que...

05:44

as consultas que eu quero, e daí conforme de tempo em tempo,

05:47

quando está completo, aí eu posso escolher para o usuário final o que eu vou fazer.

05:50

Se eu vou mandar um e-mail,

05:52

que eu vou abrir um alerta na janela dele,

05:54

enquanto fica rodando em background, se eu vou mandar uma push notification,

05:58

aí a história é outra.

05:59

O grande ponto é que a gente trabalhou com o IA

06:01

e ela não impediu que o cliente final continuasse utilizando.

06:05

Basicamente o que a gente já está acostumado a

06:07

fazer quando a gente tem operações pesadas,

06:10

mas a diferença agora é que a IA está aí no meio,

06:12

mas... É basicamente a mesma coisa. Fechou? Então, é isso aí.

## Resumo IA

[RESUMO_IA]