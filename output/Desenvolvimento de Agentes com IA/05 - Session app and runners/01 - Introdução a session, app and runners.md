Módulo: Desenvolvimento de Agentes com IA\
Aula: [Introdução a session, app and runners](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18476)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos iniciar um novo capítulo dedicado a entender os conceitos de Session,

00:06

App e Runners, que são conceitos do ADK,

00:10

mas o conceito de Sessão é algo

00:14

que você vai encontrar em qualquer framework ágil, não importa.

00:20

Você pode ver que nas suas ferramentas como o Cloud Code,

00:24

qualquer coisa de codificação,

00:26

você tem sessão envolvida. Se você vai lá no ChatGPT no seu browser,

00:30

no Cloud AI, vai ter sessão envolvida.

00:33

Então, esse capítulo agora é crucial,

00:34

porque nós vamos entender como rodar os nossos agentes em qualquer lugar,

00:40

seja nossa aplicação CLI, aplicação web, desktop,

00:44

qualquer coisa que seja. Até o momento, nós rodamos tudo.

00:49

Pegamos o nosso root agent e rodamos com o ADK Run, que é um CLI,

00:56

e o ADK Web, que é uma aplicação web que vai ter um servidor ali por trás.

01:01

Então não importa, um agente pode ficar em qualquer lugar.

01:05

Nós vamos rodar esses agentes diretamente.

01:08

Apesar de um agente como esse root agent,

01:12

nós podemos rodá-lo usando o Run ou Run Async,

01:16

ou seja, rodar diretamente, nós não vamos fazer isso,

01:20

porque o agente vai precisar de sessão. Vai precisar de outros controles,

01:24

que no caso o ADK vai nos dar isso.

01:28

Ele vai gerenciar, inclusive,

01:29

a sessão para que nós não tenhamos que fazer isso na mão. Seria bem complicado.

01:33

Apesar de você fazer um teste muito básico com o Run,

01:37

para rodar em produção não seria nada recomendado.

01:40

Aqui a gente passaria o chamado invocation,

01:46

contexto da invocação,

01:49

mas quando eu faço isso aqui eu vou ter que

01:51

salvar a sessão para o usuário poder retomar depois.

01:55

Enfim, então nós temos essas outras camadas no ADK para nos ajudar a fazer todo esse

02:02

gerenciamento.

02:05

E vai ser muito legal aprender isso porque você vai

02:10

sair daqui com a mente aberta em relação aos agentes.

02:15

Você vai começar a ver o seu Cloud Code, qualquer outra ferramenta,

02:18

na hora que você está interagindo, você sabe no que está acontecendo por trás.

02:24

Ah, isso aqui gerou uma sessão, então foi salva em tal lugar,

02:29

eu posso fazer um rewind, eu posso voltar para tal ponto,

02:33

porque eu tenho os eventos que aconteceram, eu consigo reconstruir,

02:36

enfim. Isso aqui vai ser muito legal,

02:38

você nunca mais vai ver, com certeza você já está entendendo.

02:42

Como funcionam os agentes, mas a partir de agora,

02:45

você nunca mais vai ver qualquer ferramenta ágil da mesma forma.

02:50

Você vai ser a pessoa técnica que vai conseguir enxergar do que está por trás. Então, bora lá.

## Resumo IA

[RESUMO_IA]