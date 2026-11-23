Módulo: Desenvolvimento de Agentes com IA\
Aula: [O grafo do workflows](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18566)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre o grafo do ADK.

00:03

Nós dizemos que o grafo é a estrutura base.

00:07

Precisamos definir os nós. Então,

00:10

vai acontecer um fluxo de trabalho do início ao fim.

00:15

Então, todo o workflow começa no start.

00:19

Não é apenas um nome genérico.

00:23

Na hora que nós fazemos a definição do workflow, vai ter um nó chamado de start.

00:29

Porque na hora de definir, nós podemos definir no array como vai ser o grafo,

00:35

nós não vamos desenhar, vai ser em programação mesmo.

00:38

Eu não tenho uma ordem para

00:41

definir as coisas, então o start pode estar aqui nessa linha.

00:45

O que acontece é que na hora que ele vai montar, ele vai ver onde está o start,

00:49

ele sabe que começa dali. E aí depois ele vai montando o grafo.

00:53

Então tudo é um nó. Depois que eu começo, eu vou ter o próximo nó.

01:03

E o conceito de nó

01:05

abrange várias estruturas. O nó pode ser um agente, como nós já mais

01:12

que sabemos aqui durante a disciplina, pode ser uma tool, que também nós criamos,

01:18

pode ser apenas uma function code, que não é uma tool,

01:22

é uma função com comportamento mais

01:27

básico, ou até um human input, ou seja, o...

01:35

vai cair para um usuário que esteja interagindo com a

01:39

gente e ele tem que enviar alguma coisa.

01:44

Então é assim, nós vamos definindo os nós de acordo com a nossa necessidade.

01:49

Se eu quero algo não determinístico, é a gente.

01:54

Agora, todos os outros três vão ser determinísticos.

01:58

A função e o function code, ou melhor,

02:00

a tool e o function code, nós vamos definir...

02:03

com programação. Nós vamos criar aquele processo linear.

02:07

Já o human input é como se fosse aquele tool confirmation,

02:10

mas que nós não estamos querendo confirmar algo,

02:14

mas pedindo mais uma informação ou informações para o usuário.

02:20

Então, depois que isso aqui acontece, nós

02:24

podemos ter um roteamento disso

02:29

para outros nós.

02:37

E a partir disso, o nosso grafo vai se tornando

02:42

complexo. Então, vamos imaginar que aqui eu já tenho um outro nó,

02:48

aqui eu tenho outro nó, e aqui eu tenho outro nó.

02:53

E aí o grafo vai acontecendo.

02:56

Em algum momento, vai se chegar ao final do grafo. Eu posso ter três caminhos e

03:03

três finais. Dois finais ou N finais, conforme eu queira.

03:08

Quando um nó executa...

03:11

nós vamos ter o que chamamos de roteamento.

03:16

Então é roteado o

03:22

caminho para o workflow saber que se acontecer tal coisa,

03:26

ele tem que vir para cá, ou para cá, ou para cá, tem esse roteamento.

03:33

E aí nós criamos um nó também de roteamento, aqui no meio desse processo.

03:38

Nós vamos entender isso ali no código, mas aqui já fica bem claro.

03:44

Também, cada

03:46

nó... que vai ser executado, ele produz um resultado e passa para o próximo.

03:52

Então, ele passa o resultado para esse próximo aqui e

03:57

Esse próximo passa o resultado para os outros.

03:59

Então, sempre um nó, ele recebe como parâmetro a saída do outro nó.

04:07

Então, seja o agente, tool, function code e human input,

04:12

esse nó, esse aqui vai receber o que o outro processou. E assim vai indo...

04:18

A qualquer momento que a gente quiser também quebrar o grafo,

04:22

chegou em alguma condição aqui,

04:24

eu quero retornar uma resposta para o usuário,

04:26

acabou. Não tem problema nenhum. Então,

04:29

o grafo pode ser tão complexo

04:32

ou tão linear conforme for necessário. Então,

04:37

a questão de determinar um bom workflow é conhecer as limitações,

04:42

porque algumas coisas nós não podemos fazer.

04:45

algumas coisas podem causar um comportamento inesperado no

04:50

conjunto do agente e da LLM.

04:52

Então, assim,

04:53

nós vamos ser os

04:57

orquestradores do fluxo de trabalho.

05:02

E aí nós vamos construir isso para o nosso agente de Ticket Resolution.

## Resumo IA

[RESUMO_IA]