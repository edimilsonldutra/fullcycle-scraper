Módulo: Desenvolvimento de Agentes com IA\
Aula: [Fluxo de Invocação da Tool](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18100)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos entender como essa tool é invocada.

00:05

Esse conhecimento também é crucial para que você evolua.

00:09

Porque uma vez que o agente é executado,

00:12

e eu mandei um listar faturas como usuário para ele,

00:16

listar minhas faturas, o que acontece?

00:19

Ele já vai e executa logo de cara, ou pede autorização para a LLM,

00:23

como que ele comunica as coisas com a LLM.

00:28

Eu tenho um diagrama de sequência que ilustra isso.

00:31

Então, o usuário vai

00:35

mandar a mensagem dele. Bate primeiro no agente.

00:38

A gente nem tem ainda nada da LLM. O agente já está rodando,

00:43

nós estamos acessando, no caso, via CLI. Então, o agente vai carregar,

00:50

ele carrega ali todo o ambiente dele e

00:54

vai enviar esse prompt para

01:00

a LLM, listar minhas faturas.

01:05

Então, a LLM vai ver, poxa,

01:07

tem ali as instruções que é para atender em relação a essa questão financeira.

01:13

Está óbvio que eu preciso do ID do cliente,

01:17

mesmo antes de colocar uma instrução como essa.

01:21

Se a gente tirasse, ele iria pedir, ele iria inferir isso.

01:27

Então, ele volta com uma

01:32

resposta para o agente falando, olha, você precisa pedir o client ID.

01:40

Essa resposta já está prontinha. Então,

01:43

a gente pega e manda essa resposta para o usuário.

01:47

Então, fica lá o terminal esperando.

01:50

Logo em seguida, o usuário envia o cliente 123.

01:57

Então, lembre-se que nós temos nessa seção que está sendo executada,

02:03

tudo vai sendo juntado. O contexto vai crescendo com o input e o output.

02:10

Ele pega... isso que foi enviado, mais o histórico.

02:15

E aí, a LLM volta

02:20

uma resposta para o agente, falando, olha, chama o listar faturas.

02:28

Mas como que a LLM sabia disso?

02:32

Logo aqui nesse primeiro prompt que foi

02:37

enviado, eu tenho, vou

02:40

colocar aqui, eu tenho o system prompt, mais

02:47

outras informações, como as tools.

02:51

Eu tenho, na verdade, o system prompt, mais a mensagem do usuário,

02:55

mais as tools.

02:59

E, obviamente, aqui nós recebemos essa informação de novo.

03:05

Então, são muitas coisas passadas para a LLM.

03:10

Então, ela sabe desse conceito também.

03:13

Então, ela vê que existe essa tool que tem a docstring,

03:19

que tem os parâmetros, que tem o seu próprio nome.

03:23

Então, ela infere que... precisa chamar ou listar faturas.

03:28

Então, o agente recebe esse comando, ele executa a tool, a

03:36

tool vai devolver as faturas, aí

03:40

o agente envia o resultado para a LLM,

03:44

mas envia o resultado com todo o histórico antes já feito,

03:50

com a mensagem inicial, etc., com tudo.

03:55

Então, o agente...

03:57

Decide se às vezes ele vai formatar ou fazer qualquer outra questão.

04:02

Então, ele devolve a resposta final para o agente,

04:05

o agente devolve a resposta mostrando todas as faturas

04:10

de forma formatada ou de qualquer outra forma que seja.

04:16

Então, isso

04:19

aqui deixa claro que o agente é como se fosse um subordinado da LLM.

04:24

Ele faz as operações...

04:28

Uma vez que a LLM está orientando ele a fazer.

04:32

Sempre funciona dessa forma. Porque pode parecer que

04:38

o listar faturas está sendo executado dentro da LLM. Lembre-se,

04:42

a LLM é um cérebro que não faz nada.

04:44

Você só manda as coisas para ela e ela pensa no que precisa ser feito.

04:50

Mas o chão de fábrica, quem faz mesmo é o próprio agente.

## Resumo IA

[RESUMO_IA]