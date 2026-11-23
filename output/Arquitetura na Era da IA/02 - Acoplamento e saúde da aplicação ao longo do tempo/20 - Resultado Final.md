Módulo: Arquitetura na Era da IA\
Aula: [Resultado Final](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18130)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, finalmente aqui ele terminou o processo de refatoração.

00:06

Demorou um pouco porque ele mexeu em bastante coisa,

00:09

inclusive alguns bugs plantados que eu tinha colocado, tá?

00:12

E ele fez aquele processo de Code Review.

00:15

Isso foi um ponto também que demorou. Agora, tem um ponto aqui importante,

00:20

é que a ideia que ele trouxe aqui é que ele pegou módulos como Order Service,

00:25

Notification, Sales, Logger, etc.

00:28

onde estavam na zona de dor ou com um acoplamento referente muito grande,

00:33

e ele conseguiu meio que reequilibrar aqui, e aqui principalmente a parte de Logger,

00:38

ele conseguiu melhorar bastante em relação a isso aqui,

00:42

as classes helpers aqui ele também removeu,

00:45

aqui não precisava, e acabou refatorando mesmo aqui de forma geral.

00:49

Meu objetivo aqui é não ficar mostrando os detalhes de informação,

00:53

a qualidade do código,

00:55

não é disso que se trata, eu falei isso aqui várias vezes,

00:58

mas realmente entender a possibilidade que você tem de tentar melhorar isso.

01:02

O gráfico da geração acabou ficando dessa forma agora aqui.

01:07

Então, se você perceber, todos os caras da zona de dor acabaram saindo.

01:12

Esses caras pequenininhos aqui...

01:15

Eu nem considero, de forma geral, eles como se fossem uma zona de dor,

01:19

porque eles são caras muito pequenos, com uma instabilidade média aqui.

01:24

Então, se você começar a perceber, a gente está aí,

01:29

de forma geral... deixando o nosso sistema ali menos acoplado.

01:33

A gente está trabalhando com diversas interfaces, tem uma interface gordona aqui,

01:37

que é o de types, ou seja,

01:39

basicamente muita gente depende dele, mas é uma interface.

01:42

E aqui nós temos o nosso composition.ts, que ele realmente virou uma classe de Deus,

01:49

mas ele está equilibrado em relação a isso,

01:53

porque ele está mais próximo da linha, mas...

01:57

Tem pouca dependência,

01:58

mas ele é sim para ser um cara que tem classes concretas nele.

02:03

O ponto principal é, como ele é de alta instabilidade,

02:07

ele pode ser quebrado ali em relação a

02:11

diversos aspectos quando os outros caras podem quebrar.

02:15

Mas o grande ponto é que ele depende...

02:20

desses caras, então ali nesses tipos de coisas,

02:23

caso não tem muito o que fazer, obviamente a gente poderia mudar, criar

02:27

outras estratégias para esse composition ou usar outros padrões de coisas desse tipo,

02:31

principalmente quando a gente está trabalhando com framework,

02:33

aí a coisa ela muda muito de figura, tá?

02:36

Então, a gente realizou essa refatoração e conseguiu basicamente atingir,

02:42

ou principalmente trazer o ponto aqui para vocês de como

02:46

que é possível você ir mexendo e trabalhando e acompanhando.

02:50

Mas eu acho que uma das coisas que é interessante e que antigamente,

02:56

eu sempre soube... Sempre que estudei muito sobre arquitetura,

03:01

conceitos de abstração, a parte de instabilidade,

03:05

acoplamentos aferentes e eferentes, todos esses tipos de coisas.

03:10

O problema é o que eu faço com esse conhecimento?

03:13

Com a IA agora as coisas ficaram mais simples.

03:16

Agora as coisas ficaram mais úteis.

03:20

Para pegar esses conceitos que antes eram bonitos,

03:23

mas difíceis de praticar,

03:24

para um conceito que agora a gente consegue ver isso de forma... tangível, tá?

03:29

No próximo vídeo eu vou fazer minhas últimas considerações

03:32

em relação a isso e como que você

03:35

deve daqui pra frente trabalhar e dicas pra que

03:40

você consiga aplicar isso no seu dia a dia.

## Resumo IA

[RESUMO_IA]