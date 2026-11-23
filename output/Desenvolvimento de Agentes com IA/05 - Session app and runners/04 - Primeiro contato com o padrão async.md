Módulo: Desenvolvimento de Agentes com IA\
Aula: [Primeiro contato com o padrão async](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18479)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos trabalhar,

00:02

vamos na verdade ter o primeiro contato com o padrão assíncrono,

00:06

padrão async, ou async/await, mais conhecido dessa forma.

00:10

Para quem vem do TypeScript, JavaScript, lá do Node.js, é

00:16

muito comum de ouvir essas palavras.

00:18

Nós temos esse padrão implementado no DNA do Node.

00:23

E nós devemos utilizá-lo com SDK.

00:25

Eu não vou entrar em grandes detalhes nessa aula, nós vamos pegar...

00:30

esse main.py e transformá-lo no padrão assíncrono.

00:35

E já vamos entender a diferença disso, vamos entender por que isso é importante.

00:41

Esse código que nós construímos tem dois lugares que eles fazem I/O.

00:50

Estou considerando que a criação da sessão vai fazer I/O.

00:55

e aqui

00:59

também na hora que eu vou executar o meu agente.

01:02

Apesar de estarmos utilizando

01:05

um serviço que gerencia a sessão na memória RAM, o

01:12

que vai ser mais comumente usado vai ser o serviço

01:16

de administração da sessão no banco de dados,

01:19

pois nós vamos ver isso aqui.

01:21

Então, vamos considerar que vamos trabalhar no banco de dados,

01:26

com o banco de dados aqui na sessão, e

01:30

na hora que eu estou executando o meu agente, vai ter chamadas HTTP. Então,

01:36

Nesses dois lugares aqui na sessão que eu teria o banco de dados e ali embaixo,

01:42

na hora que eu vou comunicar internamente com o LLM, nós vamos ter o I/O bloqueante.

01:55

E para um script como esse não é problemático. Não tenho questão

02:01

nenhuma em deixar o meu programa dessa forma aqui.

02:04

O problema é quando nós estamos fazendo uma aplicação web.

02:09

Vamos para a lousa.

02:12

Então, imaginando que eu tenho aqui a aplicação web, tenho

02:21

várias chamadas que vão chegando.

02:28

E vamos supor que essa primeira chamada que

02:30

está chegando na minha aplicação execute um db.fetch,

02:35

qualquer coisa lá de banco de dados. Então, aqui eu tenho I/O.

02:42

Enquanto essa chamada não terminar,

02:48

ela vai bloquear o código que está sendo executado para as outras duas que chegaram.

02:55

Ela vai bloquear a thread.

02:58

Então, se eu fizer uma chamada para banco de dados,

03:01

HTTP, trabalhar com arquivos,

03:05

qualquer coisa desse tipo vai bloquear todo mundo,

03:10

todo mundo fica esperando. Então isso não é nada eficiente.

03:14

Então o padrão assíncrono,

03:17

em resumo,

03:19

vamos trabalhar com um padrão de event loop numa única thread e

03:28

vai...

03:30

processar esses gargalos.

03:34

Tudo isso eu jogo para essa única thread e através de

03:38

eventos ela notifica o processo que está processando o que devia.

03:46

Aqui nós estamos falando de concorrência.

03:50

Entender esses padrões é muito importante.

03:53

É muito importante. Estamos falando de concorrência.

03:57

De como nós compartilhamos os recursos

04:03

CPU através de múltiplas invocações que estão acontecendo.

04:10

Então, dessa forma que está aqui, se eu pegar essa

04:15

criação da sessão, essa execução da forma que ela está,

04:18

e jogar na aplicação web, eu não vou ter performance.

04:23

Toda hora que alguém fizer uma chamada, vai bloquear os outros.

04:27

Então, nós não trabalhamos dessa forma.

04:30

Não é recomendado. Até mesmo se eu chegar aqui e executar meu

04:38

arquivo, o próprio ADK fala para que a gente migre para o padrão assíncrono.

04:44

Então, aqui

04:47

nós vamos criar, aqui

04:51

na sessão eu vou tirar o createSessionSync, vou deixar o

04:56

createSession, veja que o retorno é totalmente diferente.

05:02

Enquanto aqui ele já retorna a sessão, se

05:05

eu tiro, ele

05:08

vai trabalhar com uma coroutine.

05:11

Já aqui...

05:14

nós acrescentamos um async na frente, que é o padrão async for, e

05:21

mudo para run_async. Enquanto run,

05:25

vamos olhar o que o run retorna, que

05:31

é um generator, nós vamos entender esse padrão depois.

05:38

Aqui vai ser run_async, então já vai mudar que ele vai receber um async generator.

05:47

Esse código aqui não vai executar.

05:51

Primeiro porque eu vou precisar, aqui quando eu trabalho com... uma coroutine,

05:56

acrescentar um await, e aí ele vai falar que ele não pode ter um

06:04

await sem que eu tenha um async.

06:08

Isso aqui também não vai funcionar.

06:10

Ele vai falar que não posso ter um async fora de um async function, enfim.

06:16

Então eu vou ter que colocar isso aqui dentro de uma função.

06:20

Então nós vamos criar um async function def

06:25

run_agent.

06:30

Uma função convencional teria

06:33

apenas o def, mas ela vai ser uma função assíncrona. Então,

06:38

como o Python trabalha com alinhamento, a gente alinha tudo dentro dela.

06:47

Então, em essência, o

06:50

código vai produzir o mesmo resultado.

06:54

Pronto. Então agora não temos mais nenhum erro.

06:58

Aqui nós podemos ver, em tipagem,

07:03

até que ele não vai mostrar aqui, porque ele não conseguiu identificar,

07:09

mas aqui eu tenho também uma coroutine.

07:14

E ela, não adianta eu chamar ela aqui dessa forma assim,

07:18

se eu fizer um run, event direto, ele

07:26

vai até mostrar um erro que eu não tenho ali,

07:29

o await, mas eu posso executar ela diretamente.

07:35

Ele está me dando um aviso que nunca essa coroutine, ela vai ser... executada,

07:44

porque isso aqui é apenas a definição.

07:48

O Python não trabalha com padrão assíncrono por padrão.

07:53

Nós precisamos ativar uma das formas,

07:56

é a própria lib dele que é o asyncio.

08:02

Então aqui embaixo nós vamos fazer

08:08

async.io.run

08:12

Passando esse

08:16

run agent.

08:21

Então agora vamos executar esse

08:25

código e nós vamos ver que não vai mudar nada. Agora ele tirou deprecated do

08:32

terminal e agora o nosso código está adaptado.

08:38

Quando eu tenho essa rotina, eu

08:43

poderia executá-la com um await.

08:47

Mas se eu fizer exatamente dessa forma, se você trabalha com JavaScript,

08:50

você sabe que isso seria possível no JavaScript, o

08:56

await só vai ser permitido se...

08:59

nós trabalharmos dentro de uma async function. Então,

09:03

por exemplo, se eu tiver aqui uma função qualquer,

09:11

coloco o async na frente, e aqui eu poderia fazer assim,

09:16

db.fetch usando o await.

09:20

Aí aqui eu estaria fazendo o event loop,

09:24

permitindo que não seja bloqueante. Então todos esses...

09:32

Esse tipo de execução aqui não iria bloquear,

09:35

os outros poderiam continuar executando. Obviamente, a linha,

09:39

ela fica... Se eu tiver próximas linhas,

09:43

aquela execução fica aguardando retornar o resultado aqui.

09:49

Mas outras execuções que estão ali com correntes, elas

09:56

não precisam aguardar esse resultado, elas vão fazendo a execução delas.

10:00

Se tiver também o await,

10:01

ela empilha... lá na single thread. Depois nós vamos conversar mais sobre isso,

10:06

só para que a gente tenha um pouco mais de contexto. Então, nesse caso,

10:11

como eu tenho essa coroutine sendo executada aqui na raiz,

10:16

nós passamos ela diretamente.

10:21

Quando eu crio uma aplicação web, às

10:25

vezes nem o async.io eu preciso colocar diretamente,

10:28

porque o framework acaba nos ajudando a

10:34

esconder esses detalhes.

10:36

Mas esse é o ponto. Então, na hora que você vai criar a sessão,

10:39

na hora que você vai executar o seu agente com o runner,

10:43

faça com o run async. Mas eu poderia usar padrão síncrono,

10:48

bloqueante, em algumas situações? Claro, pode usar.

10:52

Você está fazendo alguns testes locais, está fazendo qualquer debug,

10:57

não precisa ficar trabalhando com padrão assíncrono.

11:00

Você não vai precisar de concorrência.

11:04

Então por isso que é habilitado, tem essa opção,

11:07

para que você escolha nos momentos adequados,

11:12

nos momentos determinados. Então com isso aqui agora nós vamos evoluindo,

11:16

nós vamos entender todo esse processo,

11:18

vamos criar também uma aplicação web e vamos ampliar nosso conhecimento. Vamos seguindo.

## Resumo IA

[RESUMO_IA]