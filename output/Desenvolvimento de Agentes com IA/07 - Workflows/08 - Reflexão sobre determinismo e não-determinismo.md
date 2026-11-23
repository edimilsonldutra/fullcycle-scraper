Módulo: Desenvolvimento de Agentes com IA\
Aula: [Reflexão sobre determinismo e não-determinismo](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18572)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos começar a trabalhar com a ideia de um

00:04

estorno que vai ser feito através da abertura do ticket.

00:09

Nós já estamos entendendo a dinâmica de trabalhar com workflow,

00:13

que é justamente alinhar o

00:17

que pode ser determinístico versus o que não deveria ser determinístico.

00:23

Então, mix, nós devemos colher esse paradigma.

00:29

Só determinístico, nem só não determinístico.

00:33

Nós estamos trabalhando com agente de IA.

00:36

E quando nós estamos falando de estorno,

00:38

estamos falando de valores, avaliar se realmente o

00:44

estorno deve ser feito. Isso aqui dá muito trabalho para a empresa.

00:48

Então nós vamos automatizar esse processo.

00:52

Só que nós podemos dividir em duas partes.

00:57

Podemos criar um agente de investigação do estorno. Ele

01:06

não vai fazer nada,

01:08

a não ser nos dar um veredito. Então, é

01:14

estorno ou

01:17

ficou meio incerto. Se foi o estorno,

01:26

nós podemos criar um function code, como o nó, para executar esse estorno.

01:32

de maneira determinística.

01:35

Então, veja que interessante.

01:38

Enquanto eu tenho uso das propriedades de

01:42

um agente para nos dar um panorama,

01:46

se o estorno deve ser feito ou não, eu processo esse estorno sem

01:53

dar brechas para o acaso.

01:54

Nós poderíamos criar um agente que faz tudo, tem lá as tools,

01:58

mas a gente está lidando com valores. Ainda mais aqui, nós ganhamos muito com isso.

02:04

porque o nosso agente fica mais seguro,

02:09

ele não vai fazer nenhuma operação desse tipo,

02:11

e nós temos mais controle sobre o estorno que vai ser feito.

02:15

Então a nossa ideia é

02:19

criar este

02:24

agente, ele vai ser o investigador do estorno.

02:31

Então da triagem, quando verificarmos que é estorno, vem para cá.

02:37

Então depois que esse agente executar,

02:41

vamos ter o veredito. E do veredito, vamos

02:48

ter a

02:50

triagem do estorno.

02:52

É estorno ou inseto.

02:55

Então, essa triagem ainda, ela vai pegar e mandar para um outro function code,

03:02

em que nós fazemos um estorno automático,

03:06

baseado num valor, ou caso contrário, um

03:13

humano pode fazer essa avaliação.

03:16

Podemos ter um agente ainda para poder analisar a situação com mais calma,

03:20

seria um segundo nível. Então, veja que interessante esse

03:27

tipo de workflow.

03:32

Nós não transferimos toda a responsabilidade para o agente.

03:44

Nós usamos para investigar e fizemos, vamos fazer o estorno de forma determinística.

03:52

A ideia é justamente essa.

03:57

Então nós temos que ter consciência dessa dobradinha, de fazer o uso do agente.

04:02

Do function code logo em seguida, faz uma triagem.

04:05

Eu poderia fazer o estorno logo em seguida, mas

04:12

É justamente diluir essas responsabilidades que faz com que o nó fique mais conciso,

04:18

Fique mais enxuto, mais fácil de testar.

04:21

Eu tenho a triagem, aí eu tenho outro nó para cuidar desse estorno automático.

04:28

Outras coisas para chamar um humano no meio do processo.

04:34

Vai ser assim que nós vamos trabalhar.

04:36

Então, eu queria trazer essa ideia justamente para que

04:39

A gente pense de uma forma diferente,

04:41

Porque nós estamos acostumados a trabalhar de forma determinística,

04:46

Nós podemos sempre pensar em fazer alguma coisa e

04:50

Logo em seguida já matar com o resultado obtido,

04:54

Eu já faço o que tenho que fazer.

04:56

Nós podemos ramificar isso.

04:58

Diluir, fazer as etapas de forma mais granular.

## Resumo IA

[RESUMO_IA]