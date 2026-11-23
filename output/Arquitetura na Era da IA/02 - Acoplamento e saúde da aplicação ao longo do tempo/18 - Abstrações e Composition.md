Módulo: Arquitetura na Era da IA\
Aula: [Abstrações e Composition](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18128)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, a gente conseguiu fazer, de forma geral,

00:04

o que a gente estava querendo, tá? Que é o quê?

00:06

O meu in-memory database agora, refatorado,

00:09

ele não depende mais de uma classe concreta,

00:12

ele depende ali de abstrações, e isso me ajudou,

00:15

porque se eu for no meu index.ts agora,

00:18

na hora de eu criar o meu banco de dados, eu consigo passar as classes concretas.

00:26

que eu estou querendo, e elas são intercambiáveis agora. Então,

00:28

facilita muito a minha vida no meio de toda essa história.

00:32

Por outro lado, o que acontece?

00:34

Eu tenho aqui uma classe que eu estava utilizando e o sistema utiliza aqui,

00:41

que é o composition.ts. O composition é um local, basicamente,

00:46

onde ele instancia todos os objetos que você precisa para

00:51

evitar que na hora que eu estiver no meu main aqui,

00:53

no final das contas, eu tenha que ficar chamando um a um. Basicamente,

00:57

ele ajuda a criar os meus serviços e ele pode

01:00

vir ajudar a criar os meus bancos de dados.

01:04

Tem diversos design patterns,

01:06

você pode ter uma série de opções para trabalhar com isso.

01:10

Nesse meu caso,

01:11

o que eu vou querer fazer aqui no meio de toda essa história é

01:16

eu vou querer continuar esse meu refactoring

01:19

tirando esse cara daqui e utilizando o Composition.

01:24

para que eu consiga trabalhar tudo aqui dentro dele.

01:28

Então eu tinha falado, olha, você quer trabalhar, né?

01:32

Então eu vou pedir para ele centralizar tudo no Composition

01:36

para que eu não precise fazer isso aqui dentro.

01:38

Mas daí é lembrando, o Composition vai ser sim uma classe Deus,

01:42

onde ela vai ser extremamente...

01:46

Vai ter bastante componentes instanciando dentro dela,

01:49

mas eu sei porque o objetivo dela é exatamente esse. Então,

01:54

eu vou dar um enter aqui para ele fazer e terminar esse meu processo de refatoração.

02:01

E prontinho, pessoal, ele terminou aqui. Então,

02:04

se eu for olhar agora aqui no meu index,

02:07

eu tenho no meu DB chamado Create in Memory Database.

02:10

Se eu for nesse Create in Memory Database... Na realidade,

02:14

eu estou no meu arquivo composition.ts e esse

02:17

cara aqui está fazendo a criação do meu objeto. Então, basicamente,

02:23

ele está fabricando esse objeto pronto para mim,

02:26

para que eu não precise ficar fazendo isso em diversos locais do sistema,

02:30

por exemplo. Todo lugar que eu quiser instanciar,

02:32

eu posso trabalhar esse cara, criar esses caras para mim.

02:35

Da mesma forma que ele está fazendo isso aqui com os serviços,

02:39

para criar cada um dos serviços e etc.

02:42

Então, o ponto principal, eu acho que eu queria trazer aqui para vocês,

02:47

é que todas as vezes, né?

02:50

Deixa eu rodar o script aqui de novo do nosso gráfico,

02:55

mas apesar de eu achar que ele não vai mudar muito agora, é

02:59

aqui, né? Eu saí da zona de perigo,

03:02

eu tenho vários carinhas agora aqui, né? Porque são os caras concretos.

03:07

E eu tenho alguns caras aqui, como o Database.

03:12

Parece que é uma classe Deus, mas ele utiliza muito mais interfaces.

03:16

E a gente tem aqui o Composition.

03:18

Esse Composition, sim, ele é uma classe Deus.

03:23

Ele depende de um monte de caras. Ou seja, ele realmente domina.

03:30

Mas o ponto é, eu sei que ele está fazendo isso.

03:34

É o objetivo da classe de como eu creio nesse momento.

03:37

Então eu tô aceitando isso, eu tô feliz,

03:40

vamos dizer, com isso aqui, né?

03:41

O que eu não estou feliz é com esses caras aqui nessa parte de zona de dor, né?

03:46

Isso vai acabar sempre deixando o meu sistema cada vez

03:50

mais difícil de manter em relação à parte de acoplamento,

03:54

tá? Então era isso que eu queria trazer nesse vídeo.

03:57

No final, num próximo vídeo, eu vou rodar um prompt.

04:01

para ver se ele consegue tirar quase todos os

04:03

caras da zona de dor daqui para frente.

04:05

Mas, de forma geral,

04:06

eu espero que você tenha entendido a ideia e depois eu vou falar

04:11

aqui para vocês como que você pode gerar um gráfico desse no seu projeto.

04:15

Porque esse gráfico foi gerado para esse projeto e

04:18

aí você pode trabalhar da sua forma.

04:19

A minha ideia não é te dar necessariamente uma receita de bolo pronta,

04:24

cada projeto é um projeto diferente,

04:26

tem quantidade de arquivos diferentes, tem realidades diferentes.

04:30

Mas o importante é que você consiga entender que

04:33

você consegue trabalhar dessa forma através desse entendimento de acoplamento,

04:38

instabilidade e abstração no seu software.

## Resumo IA

[RESUMO_IA]