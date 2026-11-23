Módulo: Desenvolvimento de Agentes com IA\
Aula: [Padrão async e event loop](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18484)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre o padrão assíncrono e o padrão event loop,

00:05

que estão sendo utilizados pelo SDK para que nós

00:08

possamos lidar com a concorrência de uma forma melhor,

00:14

de uma forma eficiente.

00:16

Primeiro, quando nós estamos trabalhando com o padrão assíncrono,

00:20

significa que eu executo algo

00:25

e isso tem um determinado tempo até eu ter a resposta.

00:31

sendo que eu

00:34

não bloqueio nesse intervalo outras

00:39

coisas que podem acontecer. Eu executo algo, isso pode vir a ser executado depois.

00:45

Várias ferramentas, linguagens, implementam esse padrão.

00:48

Eu posso trabalhar com o padrão assíncrono em mensageria.

00:54

Porque muitas vezes, quando a gente fala de event loop,

00:59

é uma das formas...

01:02

de implementar padrão assíncrono.

01:05

Então, quando nós temos um async await, estamos

01:11

trabalhando com padrão assíncrono. Quando nós fazemos os famosos callbacks,

01:16

eu faço, sei lá, uma execução assim.

01:19

Aí faço um run, aí passo aqui uma função, que

01:25

obviamente não tem nada a ver com Python, mas quando eu faço isso aqui,

01:29

é assíncrono, porque até mesmo o próprio código que está vindo depois...

01:35

vai ser executado.

01:37

Não vai ser bloqueante. Em algum momento posterior,

01:41

eu vou receber aqui o valor e vou fazer algum processamento. Agora,

01:47

quando eu tenho um createSessionSync,

01:52

aí aqui estaria errado com await,

01:55

eu tenho uma tarefa bloqueante. E aí nós podemos voltar àquela

02:02

imagem que nós já havíamos conversado. Se esta primeira chamada que aqui está, ela

02:10

bloqueou, ela não utiliza o padrão assíncrono,

02:15

as outras n requests que estão chegando na minha aplicação web,

02:19

todas elas vão ficar esperando a

02:27

execução dessa que terminar, que ela bloqueia.

02:33

Quando eu estou utilizando o padrão assíncrono, é diferente.

02:41

Ela executa...

02:44

e libera para que outras tarefas concorrentes, nós estamos falando de concorrência,

02:48

olhando para a mesma thread.

02:51

E não paralelismo quando nós olhamos para múltiplas threads.

02:58

Então, quando nós utilizamos esse await

03:03

com async, isso aqui é, eles andam em conjunto, em outras linguagens também é assim,

03:08

isso faz com que quando essa linha vai ser executada,

03:13

aqui nós estamos utilizando...

03:16

o armazenamento da sessão em memória,

03:19

mas poderíamos trabalhar com um banco de dados.

03:23

Se eu estou fazendo um banco de dados, vai acabar fazendo uma chamada TCP.

03:28

Então, quando nós fazemos essa chamada TCP, todo

03:34

o tempo até receber a resposta do banco de dados,

03:38

nós não bloqueamos a execução de outras tarefas.

03:47

Ela fica livre para poder executar.

03:51

Esse código, obviamente, ele é bloqueante naquela execução,

03:55

porque eu preciso da sessão para poder continuar a fazer as outras coisas.

03:59

Mas quando a gente fala não bloqueante,

04:01

é em relação a outras tarefas que estão chegando na minha aplicação.

04:08

Então, ele libera o controle.

04:13

E assim vai.

04:14

Então, quando

04:17

nós estamos falando desse padrão assíncrono, por trás está sendo implementado com...

04:24

o event loop, ou seja, é um loop de eventos, ou uma

04:32

estrutura circular de eventos que vão acontecendo.

04:35

Eu tenho nessa mesma thread que eu estou,

04:38

que eu rodo aqui o meu projeto, eu

04:42

vou ter uma estrutura, eu fiz um desenho para poder representar isso, para

04:50

poder ficar mais fácil.

04:52

Dentro dessa single thread eu tenho esse event loop que

04:56

controla essas tarefas.

05:02

bloqueantes, que não vão ser bloqueantes, eu faço uma chamada await HTTP GET.

05:10

Então, ela fica suspensa até que se receba o valor.

05:15

Então, ele cede o controle ao looping. Quando ela executa,

05:19

nós ficamos esperando o controle. Então,

05:22

eu posso receber uma outra tarefa ao mesmo tempo,

05:25

que vai fazer uma consulta no banco de dados.

05:28

Fez a consulta, cede o controle ao looping.

05:31

Mas uma outra que já tinha executado,

05:35

quando chegou o resultado, o loop retoma,

05:41

devolve o valor ali para o código onde nós estávamos e

05:47

o processamento continua. Neste event loop, nós vamos ter,

05:51

como se fosse um while eterno,

05:54

um while true, que vai ficar checando uma fila de eventos.

06:03

Então, eu tenho nessa fila de eventos um HTTP que foi feito,

06:06

algo de banco de dados, algo que está no disco.

06:10

Nós fizemos a execução, estamos aguardando o valor.

06:14

Existe também o chamado de file descriptor e

06:22

quando eu faço essa execução o kernel me devolve um inteiro e

06:26

é o identificador que eu consigo verificar qual é o estágio daquela execução.

06:34

Utilizando essa fila de eventos e um file descriptor que é feito,

06:37

nós conseguimos verificar o status e

06:41

também ser notificados sobre aquilo que aconteceu.

06:45

Então, esse while true fica sempre verificando essa fila de eventos.

06:49

Opa, eu tenho ali um resultado, então deixa

06:53

eu mandar para o código correspondente.

06:58

Imagine que eu possa ter aqui... N tarefas de N chamadas HTTP.

07:04

No caso, estamos utilizando aqui o HTTP como exemplo.

07:08

Várias tarefas de várias requests diferentes.

07:13

Então, a grosso modo, é assim que está acontecendo por trás.

07:18

E é isso que está liberando para que nós

07:21

possamos ter várias tarefas distintas acontecendo ao mesmo tempo.

07:28

E onde que isso se conecta com generators? Olha só.

07:33

O que nós temos aqui, na verdade, nós já tínhamos visto que um await retorna

07:41

uma co-rountine, mas olha só esse run async.

07:46

Se retorna um async generator.

07:49

Na verdade, tanto a co-rountine quanto esse async generator,

07:55

Todos os dois trabalham com generator,

07:58

porque a ideia é que eu tenha uma função que eu consiga controlar a execução dela.

08:06

Mas aí, adicionando a questão assíncrona.

08:14

Esse await, na verdade, é como se ele fosse um yield.

08:18

Obviamente, ele não vai retornar essa função e enviar mensagem.

08:22

Mas esse await é uma cessão do controle. Olha, estou fazendo aqui a execução,

08:29

tiro o controle de mim, mas eu só quero o valor quando ele vai ser retornado.

08:37

Então, nesse caso aqui, como nós estamos tendo...

08:41

uma chuva de eventos, mas

08:45

somente trabalhar com o padrão generator não permite que você seja assíncrono,

08:51

então com o async generator permite que tudo que está aqui dentro seja

08:58

executado com o padrão assíncrono / event loop,

09:02

que é a forma que o padrão assíncrono está sendo implementado.

09:08

Então nós vamos ter aqui dentro,

09:09

na verdade vão ser múltiplos awaits, uma sequência de awaits.

09:16

que vão sendo executadas lá. Vai ter LLM, vai ter questão de sessão,

09:20

pode ter também questão de memória, pode ter N coisas.

09:23

Tudo que tiver aqui dentro, as tools também que vão ser executadas, nós fazemos,

09:30

pode chamar banco de dados, pode chamar disco, pode chamar N coisas.

09:37

Então, nesse caso aqui, essa função, olha só, ela é apenas uma função

09:44

assíncrona.

09:46

Ela está descrevendo que ela retorna YSyncGenerators.

09:54

Quando nós olhamos para uma função como essa aqui, ela está retornando

10:02

apenas um dicionário. Não significa que toda função assíncrona retorna.

10:07

Nós já vimos que a função assíncrona por padrão vai

10:13

ser uma coroutine. Mas essa função que está aqui,

10:18

na verdade esse método que está aqui, código mais abaixo, ele

10:26

tem o yield.

10:30

É porque a combinação do generators mais

10:36

o async acaba sendo o async generators.

10:40

Eu controlo a

10:44

execução da função que vai fazer um monte de coisas e permito que

10:49

ela use o padrão assíncrono com o event loop para que ela não trave,

10:54

para que ela não gere execuções bloqueantes.

10:57

Para deixar bem claro o que nós estamos fazendo. Nós vamos ter... os yields aqui.

11:06

Seria a mesma coisa da gente fazer dessa forma.

11:11

Está vendo

11:14

aqui em cima que ele está nos dizendo que é um generator,

11:17

mas na verdade aqui embaixo ele está corrigindo.

11:20

Quando eu faço async com yield, async generators.

11:24

Quem muda um pouquinho é obviamente porque eu tenho um controle mais apurado.

11:30

Mas esse entendimento é crucial. Então eu tenho um controle

11:36

apurado de vários retornos,

11:39

permitindo executar tarefas bloqueantes de forma não bloqueante.

## Resumo IA

[RESUMO_IA]