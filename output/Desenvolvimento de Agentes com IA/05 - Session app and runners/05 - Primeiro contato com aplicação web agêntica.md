Módulo: Desenvolvimento de Agentes com IA\
Aula: [Primeiro contato com aplicação web agêntica](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18480)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos ter um primeiro exemplo de um agente de AI rodando em uma aplicação web.

00:08

Eu tenho esse web.py que está dentro do próprio operador Conta Session,

00:14

com um código que é bem parecido com o que está no main.

00:18

Tem apenas 48 linhas.

00:21

Ele não tem o async.io porque ele já vai

00:24

trabalhar com esse padrão embutido no framework que nós utilizamos,

00:28

que é o FastAPI.

00:31

Não é necessário instalar esse framework porque

00:34

o SDK já incorpora esse framework por padrão,

00:38

um framework muito conhecido na comunidade Python,

00:41

um dos principais para a criação de APIs.

00:45

Então, quando nós rodamos, na verdade, o SDK Web,

00:49

o FastAPI já é usado por debaixo dos panos. Então,

00:54

o que é legal é que você já pode utilizá-lo se você vai...

00:57

ter os seus agentes de IA habilitados em uma API.

01:04

Então, nós vamos rodar esse exemplo, já vamos entender algumas coisas,

01:08

e ao decorrer das aulas, nós vamos trabalhando com esse conceito da web.

01:15

Então, veja que esse começo é idêntico, criamos o SessionService,

01:22

o app do SDK, mas aqui eu tive que mudar o nome porque...

01:28

Normalmente, se dá, na verdade, não é obrigação,

01:31

mas quando criamos a instância do FastAPI, chamamos de app.

01:36

Então, eu mudei o nome para SDK app.

01:39

Então, temos o app do SDK e o runner.

01:42

E aí, a instância do FastAPI. E aí, com o padrão decorator,

01:48

colocamos em cima de qualquer método, ele vira uma rota.

01:51

Então, aqui por padrão, acesso na porta 8000.

01:55

Eu já consigo brincar com esse teste direto.

01:58

E veja que ele é uma função já assíncrona.

02:03

Então, que eu já poderia usar a wait para

02:07

melhorar a minha concorrência, como está sendo aqui no caso do session service,

02:11

que nós já tínhamos utilizado na aula anterior.

02:14

Então, aqui não mudou nada, exceto por esse trecho que está aqui.

02:19

Porque nós poderíamos colocar um return já com a resposta,

02:25

retornar isso aqui direto, que ele vai... fazer um JSON,

02:27

mas quando nós estamos rodando esse trecho que é um async generator,

02:34

ele vai acabar tendo uma finalização e o

02:38

return vai finalizar antes que essa estrutura feche,

02:44

lançando um aviso.

02:46

Nós vamos ter o resultado,

02:48

mas não é bom ter esse fechamento porque depois

02:51

nós podemos ter problemas como memory leak.

02:54

Então... É recomendado que você coloque uma variável,

02:58

inicie ela com qualquer valor, ou None,

03:02

armazene, e depois que passou tudo isso, você usa o valor, faz alguma coisa,

03:08

faz qualquer coisa que você necessite. Então,

03:11

chama esse via GET e dá essa resposta.

03:16

Para executarmos essa aplicação web,

03:19

nós rodamos este comando, uvicorn.

03:25

Esse Uvicorn também é um pacote que vem junto com o FastAPI,

03:30

que vem junto com o SDK, tudo vem, na verdade, emaranhado de coisas.

03:35

Ele que vai levantar,

03:37

Ele vai rodar o servidor web já com o padrão assíncrono. Então,

03:43

Nós não nos preocupamos em fazer nada ali,

03:46

A não ser desenvolver o nosso código. Então,

03:48

Daqui para frente, é exatamente o caminho...

03:51

Do arquivo do Python. Então, nós colocamos sempre ponto,

03:55

Como se a gente estivesse importando. Então,

03:56

Temos ali a pasta agents.operador.conta.session.web.

04:04

Aí colocamos os dois pontos para

04:07

Qual é a variável que iniciou o

04:12

FastAPI, porque ela concentra tudo. Ela está com o decorator,

04:16

Ela vai saber tudo o que precisa.

04:19

E aí passamos o menos menos reload, que é uma opção para desenvolvimento,

04:23

Porque ele vai habilitar o modo watch,

04:25

Qualquer coisa que eu mudar no código,

04:27

Ele levanta o servidor sem que eu tenha que ficar parando e rodando novamente.

04:32

Então aqui nós vamos rodar o localhost na porta 8000, ele

04:38

Vai ter a latência porque tem aquela comunicação com o LLM, nós já entendemos isso,

04:43

E aqui ele mostra aquela mensagem pedindo o ID do cliente, então não teve diferença.

04:49

Nós só não vimos ainda como é a continuidade

04:52

De uma comunicação quando o usuário está mandando várias mensagens. Então, veja só,

04:58

Nós acabamos de ver mais um exemplo em que

05:01

Nós utilizamos um agente de IA junto com um projeto.

05:06

Isso aqui esclarece muito bem que não é um bicho de sete cabeças.

05:11

O agente de IA acaba sendo um componente do software,

05:14

Assim como eu posso ter banco de dados, cache, mensageria,

05:18

Storage e várias outras coisas.

## Resumo IA

[RESUMO_IA]