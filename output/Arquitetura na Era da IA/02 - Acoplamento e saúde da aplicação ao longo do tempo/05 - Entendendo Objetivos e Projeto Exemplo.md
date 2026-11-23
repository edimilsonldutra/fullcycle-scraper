Módulo: Arquitetura na Era da IA\
Aula: [Entendendo Objetivos e Projeto Exemplo](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18115)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, agora a gente vai aqui ficar um tempinho,

00:05

um bom tempinho em código para que a gente consiga

00:09

explorar bem a fundo pontos extremamente interessantes sobre acoplamento e como

00:15

que a gente consegue colocar a IA para trabalhar para a gente

00:17

para dar mais tranquilidade na hora de desenvolver o sistema.

00:21

Para que eu tivesse um exemplo para trabalhar,

00:25

o que eu fiz? Eu utilizei a IA, obviamente,

00:28

para ela criar... Um sistema de e-commerce simplificado,

00:32

com banco de dados em memória, com diversos componentes ali em TypeScript,

00:37

apenas os principais endpoints ali. O objetivo aqui, na realidade,

00:44

é até a gente ter uma massa de código para que a gente possa,

00:48

em seguida, fazer o que no final das contas?

00:53

Entendendo... para entender onde estão os principais problemas, zona de dor,

00:59

acoplamentos e pontos que vão fazer com que ao

01:02

longo do tempo e nessa situação atual,

01:04

já faz com que a gente tenha problemas em evoluir a arquitetura.

01:10

Então, se você olhar aqui,

01:12

eu tenho um index.ts, onde você pode ver que eu tenho diversos dados aqui feitos,

01:18

chamando uma função aqui main. Esses caras aqui, eles fazem uma seed.

01:22

para jogar como se a gente tivesse um banco de dados.

01:25

Mas aí a gente começa a entrar em diversos outros aspectos.

01:30

Por exemplo, payment. Então, eu tenho um payment gateway,

01:33

que nesse caso aqui é uma classe. Quer dizer, esse aqui é o PayPal.

01:38

Payment service. Esse payment service vai estar instanciando direto o Stripe.

01:44

Opa, o que aconteceu com o PayPal?

01:46

Você vai perceber que tem coisas onde nós não temos

01:49

interfaces e temos ali classes concretas sendo instanciadas.

01:53

A gente tem um caso, por exemplo, que nós temos uma interface,

01:57

mas ela está sendo subutilizada e ficando quase perto de uma zona de inutilidade,

02:03

por exemplo. Então,

02:05

o nosso objetivo daqui para frente é que

02:08

você tenha uma experiência de a gente conseguir...

02:13

Utilizar uma base de scripts que você vai ver no próximo vídeo.

02:16

E já consigo te adiantar, tá? Não existe um script Deus,

02:21

que vai conseguir resolver todos os problemas de todos os seus códigos.

02:25

Isso vai ser provavelmente altamente customizado para a sua base de código,

02:29

porque cada projeto é diferente, tem estrutura diferente,

02:32

tem projetos com poucos arquivos,

02:34

tem projetos com centenas de milhares de arquivos. Então,

02:37

a gente não pode ser inocente o suficiente de dizer

02:41

que o meu script vai resolver todos os seus problemas,

02:44

principalmente porque a gente trabalha com linguagens de programação diferentes, etc.

02:49

Esses scripts, uma vez...

02:51

uma vez que você entendeu aqueles conceitos que eu passei de acoplamento,

02:54

aferente, eferente, instabilidade, abstração,

02:57

facilmente você consegue reproduzir esses tipos de scripts

03:01

utilizando IA para criar para você. Então,

03:04

eu acho que eu não quero que você foque

03:06

necessariamente em como esse script foi feito,

03:09

mas sim na utilidade de ter uma visualização clara.

03:14

Para entender os grandes gargalos aí no seu sistema, em relação, obviamente,

03:18

ao acoplamento. A gente não está falando muito de detalhe de implementação,

03:22

tá? Então, está aqui o nosso, entre aspas, e-commerce.

03:25

Inclusive, no próprio cloud dele, né? E etc.

03:31

Eu tinha até colocado para ele não... Para ele saber,

03:35

na realidade, que isso aí era um projeto...

03:38

Ele era um projeto que, de propósito, ele tinha sido feito,

03:44

construído dessa forma, com acoplamento, com alguns bugs e coisas desse tipo.

03:49

E aí, no próximo vídeo,

03:50

você vai ter a oportunidade de ver

03:55

um script que a gente consegue analisar,

03:57

por exemplo, os níveis de acoplamento,

03:59

e a gente vai seguir uma linha...

04:02

até onde a gente faça uma refatoração e a gente consiga tirar,

04:07

vamos dizer assim, da zona de perigo,

04:09

classes que poderiam dar muito problema para o nosso sistema, beleza? Então,

04:14

vamos nessa jornada, tem bastante vídeo aí para ir, tá?

04:17

Nosso objetivo não é um curso de refatoração, novamente,

04:19

nosso objetivo aqui também, nesse momento, não é ensinar...

04:23

Como você trabalhar com IA, criar seus workflows,

04:27

SDD, Harness. Eu não estou pensando em nada disso.

04:31

Todos os prompts e coisas eu vou digitar na mão de

04:33

uma forma simples para que a gente consiga entender,

04:37

na realidade, na raiz,

04:39

esses conceitos de acoplamento. Então,

04:42

abstraia essa parte de a forma de trabalhar com IA.

04:47

Isso aqui não é um curso de refatoração. Assim,

04:49

uma forma clara de mostrar para vocês.

04:52

Como que você consegue analisar a saúde entre os sistemas do

04:55

seu sistema ao longo do tempo com essas informações, tá? Então,

04:59

não fique esperando muito em relação ao prompt maluco

05:04

que eu vou utilizar ou uma skill.

05:05

Eu nem estou utilizando skill,

05:07

estou utilizando skills que já vêm aqui nesse caso com o Cloud Code. Mas fora isso,

05:11

basicamente é mão na massa e a gente vai comparando esses

05:15

gráficos conforme a gente vai alterando e sentindo o que está acontecendo.

05:19

Beleza? Um grande abraço e até o nosso próximo vídeo.

## Resumo IA

[RESUMO_IA]