Módulo: Arquitetura na Era da IA\
Aula: [Refatoração Após Saída da Zona de Perigo](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18127)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, no vídeo anterior a gente tirou o nosso database, no final das contas,

00:06

da nossa zona de dor, mas a gente sabe que ele está carregando muita coisa,

00:11

apesar de serem classes diferentes aqui.

00:13

O que eu quero fazer agora aqui é o seguinte,

00:18

tá? Eu vou colocar aqui, o meu @database

00:24

.ts saiu

00:29

da zona de dor.

00:33

conforme o @meu main sequence.html.

00:39

Porém, ele está

00:42

carregando muita coisa,

00:47

ou seja, carregando muitas classes.

00:52

Faça o split dessas classes

00:56

e deixe apenas o necessário,

01:01

o database.ts.

01:05

A separação dessas

01:08

classes fará

01:14

com que cada arquivo

01:18

tenha apenas a sua

01:23

responsabilidade e fará novamente e

01:30

utilizará sua interface,

01:35

o que já está acontecendo.

01:45

Perceba, galera, que eu não estou aqui querendo trabalhar no workflow,

01:49

num processo, em algo desse tipo.

01:51

Estou escrevendo de uma forma bem simples, porque a gente,

01:54

a nossa ideia aqui não é processos,

01:57

mas assim, entendimento arquitetural.

01:59

O que eu vou colocar aqui pra ele também é o seguinte.

02:04

Faça isso utilizando diversos

02:10

agentes em paralelo. No Superpower ou em outras prompts ou outros skills,

02:16

eu consigo claramente dar esse comando,

02:22

mas eu estou pedindo expressamente aqui.

02:25

Qualquer refatoração e mudança nos testes,

02:32

utilize...

02:38

vou mandar ver, nem criei, se você perceber aqui.

02:42

Planejamento, nem fui no mal do plan perceba que eu tô

02:45

indo meio que no go horse aqui com vocês,

02:47

porque o meu objetivo aqui não é ter a

02:49

minha boa prática da implementação, as minhas coisas,

02:53

o meu primeiro ponto aqui é realmente direção,

02:55

setas e fazer com que esses caras mudem,

02:57

tá? Um outro ponto importante que eu queria trazer aqui pra vocês, tá,

03:02

quando a gente tá falando que quanto mais perto eu

03:05

esteja dessa linha mais equilibrado eu tô, não significa que isso

03:10

é o melhor do mundo, tá?

03:13

Isso simplesmente significa que eu tenho um equilíbrio entre

03:17

quem eu importo e quem me importa.

03:20

Basicamente é isso, ou seja, eu tenho uma classe ali equilibrada e ainda,

03:25

principalmente, se ela está fazendo implementações de algo que é abstrato, tá?

03:33

Não de algo que vem da zona de dor. Então,

03:36

Uma coisa que eu quero que você sinta paz é,

03:38

não é porque eu tenho um cara aqui e eu estou ruim,

03:42

tá? Na realidade, significa que eu tenho meu nível de equilíbrio.

03:46

E se você olhar aqui,

03:48

por exemplo, esse cara, ele depende de quatro, nesse caso aqui, duas interfaces.

03:55

Ele depende de duas interfaces e quatro caras dependem dele.

03:58

Então, é um sistema pequeno. Então,

04:00

eu não sei se eu tenho que ter uma preocupação

04:03

grande aqui e tentar fazer ele querer subir,

04:05

tanto que não faz sentido.

04:06

Eu vou ter que criar código a mais para tentar

04:09

fazer ele ficar perto de uma linha verde, tá? Então,

04:12

eu quero que você tenha esse bom senso e eu não

04:15

estou querendo dizer que tudo que está aqui está ruim,

04:16

tá? Mas, sempre você tem que ficar de olho,

04:20

principalmente nesses caras que estão com...

04:24

Essa borda preta, porque eles estão dependendo,

04:27

certamente, aqui de muita gente. Esse cara aqui, o Notification Service,

04:32

depende de 10, tá? E somente 3 dependem dele.

04:36

Então, ele é um candidato aqui, eventualmente, para a refatoração também,

04:40

tá? Então, a gente tem que tomar cuidado.

04:42

Por outro lado, ele está ali no meio de instável,

04:47

ou seja, ele não está extremamente concreto e...

04:51

Quer dizer, ele não está ali na zona de dor como eu não gostaria que ele estivesse.

04:56

E a gente não está com classes aqui na zona de inutilidade.

05:01

E aqui ele já começou a mexer aqui nos nossos arquivos e rodar e tudo mais.

05:07

Então, vamos ver assim que ele terminar para ver se a

05:11

gente tem um resultado e ver o que aconteceu.

05:16

Bom, pessoal, ele acabou de trabalhar e fazer,

05:20

na realidade foi até que bem rápido, e o que ele fez é,

05:22

ele foi criando uma nova classe para cada tipo de repositório,

05:26

e ele mostrou onde que ele criou o arquivo,

05:29

em Memory Order Repository, e ele fala qual cara que implementa ele e etc. Ou seja,

05:35

eu tirei aquele monte de peso de em cima do database.ts,

05:40

mas olha só que interessante.

05:42

Mesmo eu tirando esse peso todo do database.ts, o meu database.ts,

05:48

qual que é o objetivo dele no final das contas? É expor o In-Memory Database.

05:54

Então, ainda que eu tenha diversos arquivos que esse cara vai

06:00

chamar e esses arquivos estão trabalhando com implementações e tudo mais.

06:06

ele ainda é um cara que ele é extremamente chamado,

06:09

tá? Então, isso aí que é um ponto importante.

06:12

Deixa eu até olhar aqui o que o Claudio trouxe, olha só.

06:16

Métrica, continua fora da zona de dor, região concreta instável, sem risco.

06:20

Por ser Composition Root, né? Ou seja,

06:23

o acoplamento referente aproximadamente 9, é inerente,

06:28

mas o arquivo agora tem responsabilidade única,

06:32

só compor. Não mais nove definições de classes.

06:35

As quatro dependências cíclicas intencionais ficaram intactas.

06:39

A gente está ainda com dependência cíclica.

06:42

Mas esse cara foi regenerado. Então,

06:44

deixa eu olhar aqui para ver se o gráfico mudou aqui no nosso ponto.

06:48

Deixa eu dar um atualizar.

06:50

Prontinho. Então, olha só o que aconteceu agora.

06:53

Provavelmente, eu tenho mais caras agora aqui.

06:57

In -memory repository.

06:59

Eu tenho in -memory order repository. Então,

07:01

perceba que eu tenho um monte desses caras.

07:04

E eles estão aqui de forma geral saudáveis,

07:07

porque ele depende de uma interface e alguns caras dependem dele.

07:10

Um dos caras que provavelmente depende dele é o nosso database .ts. Vamos olhar aqui.

07:16

Database .ts.

07:17

Perceba que ele ainda continua ali dependendo diretamente de outros caras.

07:23

E isso significa o que no final das contas? Ele é...

07:29

um camarada que expõe toda a parte de banco de dados.

07:33

Então, ele tem a característica dessa,

07:36

vamos dizer assim, dessa classe Deus,

07:39

porque ele é o cara que faz a parte de instância,

07:43

de criação concreta dos caras. Aí,

07:46

todo mundo que vai precisar utilizar banco de dados ou qualquer coisa desse tipo,

07:51

vai depender dele. Então, se eu abrir agora esse cara aqui,

07:55

vamos abrir o nosso database .ts,

07:58

A gente vai ver que a gente vai ter o quê? Um monte de importação,

08:02

porque ele precisa dessa importação,

08:04

mas perceba agora que ele importa caras concretos,

08:08

realmente, porque ele está importando o cara que está fazendo a

08:12

implementação e agora ele apenas está expondo o nosso in -memory database.

08:18

Wesley, mas ele ainda está importando coisa concreta? Sim,

08:22

ele está importando coisa concreta. Porém, a gente tem uma diferença.

08:27

Essas nossas classes aqui,

08:30

elas usam uma implementação,

08:34

como que eu posso dizer?

08:37

Uma implementação baseada em uma interface, então é fácil ainda de eu mudar.

08:43

O que eu poderia fazer aqui que eu não gosto e

08:46

que poderia me ajudar aqui em relação ao nível de abstração?

08:50

Como ele é um database .ts, e aqui ele simplesmente está...

08:57

importando diretamente esses caras. Agora, olha só que interessante.

09:05

Ele importa, de forma geral,

09:09

ainda o quê? Um objeto concreto.

09:13

Então, no bom senso, o que acontece?

09:17

Esse cara aqui está dando nil direto nessas outras classes.

09:23

Qual é o grande problema aqui?

09:25

ele ainda tem um acoplamento alto. Por que ele tem um acoplamento alto?

09:30

Porque aqui ele não está dependendo mais de diversas abstrações.

09:36

Ele está dependendo de classes concretas. Então,

09:39

deixa eu olhar aqui. Vamos pegar esse cara.

09:45

Cadê o nosso database .ts? Aqui. Se você ver,

09:51

ele está dependendo de nove módulos.

09:55

aqui para a gente, tá? Então, está esse grande ponto. Mas, se você perceber,

09:59

os módulos que ele está dependendo são módulos ou classes extremamente concretas.

10:06

Se eu quiser trabalhar de uma forma,

10:08

entre aspas, vamos dizer assim, mais correta, vamos dizer assim,

10:13

o que eu faria no final das contas?

10:16

Esse in -memory database,

10:19

ele receberia construtores aqui dentro.

10:22

que tem as interfaces dessas classes, para quê?

10:27

Para que eu possa

10:31

fazer a injeção de dependência

10:34

na hora que eu for instanciar essa minha classe.

10:37

Então, se eu tivesse que trabalhar com mais uma refatoração aqui,

10:41

com certeza o que eu faria é jamais instanciar uma classe dentro de outra.

10:47

O problema desse meu database, agora .ts, é o quê?

10:51

no final das contas, é ter um monte de new dentro dele.

10:55

Se eu tenho um monte de new dentro de um arquivo,

10:57

é muito difícil de eu testar, inclusive, esse cara.

11:00

Como nesse nosso caso aqui é um exemplo bem simples que a gente está fazendo,

11:05

ainda mais com o In -Memory Database,

11:07

onde eu carrego um database .ts e eu tenho

11:11

acesso a todos os componentes de bancos de dados,

11:15

isso aqui, de forma geral, não está me incomodando. Porém,

11:18

se eu fosse, ou se eu precisar fazer uma...

11:21

o que eu poderia simplesmente chegar

11:25

agora e colocar da seguinte forma.

11:29

Eu posso colocar o

11:33

database

11:36

.ts está

11:39

instanciando diretamente outras

11:46

classes concretas. Logo, quero

11:52

poder

11:53

trabalhar.

11:55

com dependency inversion onde

11:59

ele receberá como parâmetros as

12:07

interfaces e

12:10

depois quando ele for instanciado

12:17

teremos então

12:21

que

12:23

passar as classes

12:26

concretas somente para você lembrar e aqui é um grande

12:32

ponto porque eu estou falando isso aqui para vocês porque

12:37

Provavelmente tem muita gente que o que eu estou falando aqui é muito óbvio.

12:41

Instanciar algo dentro de uma classe é algo de forma

12:45

geral ruim em relação à testabilidade de muita coisa.

12:48

A gente está trabalhando com um exemplo simples.

12:50

Por outro lado,

12:52

eu não sei nesse momento o quanto que você tem

12:55

de conhecimento também e às vezes isso pode parecer até confuso.

12:59

Mas a minha ideia principal aqui é eu não depender de implementações.

13:06

que é o que está acontecendo aqui, estou dependendo de implementações concretas,

13:09

mas sim depender do que no final das contas? De abstrações. Então,

13:16

o ideal aqui é a gente ter um construtor ou algum método

13:21

que faça com que eu consiga

13:23

receber esses caras através da interface deles.

13:29

Ou seja, eu não tenho essa dependência desses caras concretos.

13:33

Então, eu vou colocar...

13:36

Realize essa refatoração,

13:39

utilize múltiplos agentes,

13:44

trabalhe com o TDD e garanta que

13:49

o sistema continue

13:54

em funcionamento aqui. Uma coisa que provavelmente vai ter que mudar,

14:00

eu acredito, que é o seguinte,

14:01

deixa eu só dar uma olhada aqui. Se eu for no meu index .ts,

14:09

Deixa eu só dar uma olhada aqui. Ele tem um main.

14:11

Se você olhar, o que está acontecendo?

14:14

Ele está dando um db é igual a new in -memory database. Ou seja,

14:18

ele está importando esse cara aqui, esse database aqui, esse in -memory database.

14:24

Porém, ele está importando essas classes aqui de

14:28

forma geral de forma de implementação.

14:31

Ou seja, ele está importando aqui o objeto concreto. E isso aqui...

14:36

acaba sendo um malefício a longo prazo durante o processo.

14:40

Na maioria das vezes, você não vai querer trabalhar assim. A ideia aqui, no final das contas,

14:45

é aqui dentro eu passar todas as minhas classes concretas aqui dentro,

14:51

para aí sim eu ter o meu In -Memory Database,

14:54

e aqui dentro eu vou tirar esses news daqui de dentro e

15:00

falar que no construtor dele ele recebe a interface que esse cara...

15:06

implementa. Então, esse aqui, na realidade, acaba sendo,

15:09

entre aspas, o melhor dos mundos,

15:10

quando a gente trabalha com sistemas ou frameworks de injeção de dependência,

15:14

é super comum que isso acabe sendo até automático na hora de você trabalhar.

15:18

Como a gente está fazendo aqui de uma forma manual,

15:20

é isso que eu estou trabalhando. Então,

15:22

eu vou pedir para ele fazer mais esse passo aqui para a gente aqui,

15:26

tá? Então, trabalhe com o TDD e garanta o funcionamento, né?

15:30

E no main, no arroba... index

15:37

.ts, você deverá

15:45

instanciar

15:47

as classes

15:53

concretas no

15:57

in -memory database.

16:00

Já falei em relação a múltiplos agentes, etc. Estou dando um enter aqui.

16:06

Perceba, galera, não estou em nenhum workflow maluco,

16:08

não estou... pirando em nada aqui de forma geral,

16:12

tá? Estou escrevendo num prompt que fique

16:16

fácil de você entender o que eu estou fazendo, tá?

16:18

O que eu não quero é que essa aula fique tão complexa

16:22

ao ponto de misturar conceito de arquitetura com como programar utilizando o IA.

16:29

Então, por isso que eu estou fazendo aqui com o IA de uma forma extremamente básica,

16:33

sendo o babá dela e entendendo essas iterações.

16:37

O importante aqui é eu conseguir focar nesses

16:39

aspectos mais arquiteturais para você entender.

16:42

Então, olha só,

16:43

isso aqui é um dependency inversion princip refactor aqui do in -memory database.

16:48

Então, o que eu vou fazer é o seguinte,

16:50

Eu vou parar esse vídeo aqui e no próximo a

16:52

Gente, vê o que ele acabou fazendo e terminando.

16:56

Fechou? Um grande abraço e vamos aí para o próximo.

## Resumo IA

[RESUMO_IA]