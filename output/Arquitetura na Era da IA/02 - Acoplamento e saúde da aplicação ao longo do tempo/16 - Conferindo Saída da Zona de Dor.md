Módulo: Arquitetura na Era da IA\
Aula: [Conferindo Saída da Zona de Dor](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18126)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, agora a gente chegou num ponto esperado,

00:04

porque a gente realizou aquela refatoração para tentar

00:08

tirar aquele nosso database da zona de perigo.

00:12

Então, se você olhar o gráfico antes,

00:15

ele estava basicamente aqui, certo? Ou seja,

00:18

eu tenho meu database e esse cara depende de 17 camaradas aqui.

00:24

O grande ponto é que ele está nessa zona de dor porque ele é extremamente...

00:30

ou seja, ele instancia todos esses caras, na realidade,

00:35

quer dizer, 17 caras dependem dele diretamente,

00:39

ou seja, ele é uma classe que quer ser uma classe deus, vamos dizer assim,

00:45

mas ao mesmo tempo ela é tão estável que faz

00:49

com que ela esteja nessa zona de perigo,

00:52

faz com que o sistema inteiro tenha problema de mudar.

00:56

Então, a nossa ideia que a gente fez com a refatoração é, nós pegamos, na realidade,

01:01

esses caras aqui que dependem dele, principalmente,

01:05

e como a gente estava falando de banco de dados,

01:08

cadê ele aqui? como a gente estava falando de banco de dados especificamente,

01:11

a ideia era conseguir fazer com que a gente tivesse

01:15

abstrações para cada módulo ou componente do nosso banco de dados,

01:19

e a gente trabalhou ali com repositórios,

01:21

então a ideia era ter interfaces para cada um desses camaradas.

01:25

O que eu espero agora aqui na realidade?

01:29

Eu espero tirar ele da zona de dor,

01:31

espero ter mais interfaces aqui no estável e abstrato,

01:35

não necessariamente 100 % estável, mas abstrato,

01:38

E fazer com que esse meu banco de dados, no final das contas,

01:42

ele venha pra cá, tá? Porque uma vez que ele vem pra cá,

01:46

eu sei que ele já tá numa zona fora da zona de perigo, né?

01:51

Não necessariamente ele vai ficar perto dessa linha. Por quê?

01:55

Porque ele é, de forma geral, uma classe quase que Deus.

02:01

mas não no mau sentido,

02:03

na realidade significa que tem muita coisa dentro dele, na realidade.

02:07

A gente poderia até fazer um split e a gente faz isso depois,

02:09

mas a gente tem que entender esse processo.

02:11

Primeira coisa, eu quero tirar ele da zona de dor. Como eu refatorei, o que eu fiz?

02:16

Eu gerei um gráfico para a gente comparar agora como ficou depois,

02:20

que é esse cara aqui.

02:22

Então, olha só que interessante que aconteceu.

02:25

Ele não está mais na nossa zona de dor, se você procurar o database.

02:29

Nós agora temos outras interfaces, se você olhar aqui, a abstração é tudo um,

02:34

se você olhar, certo? Olha só que interessante.

02:38

Mas o mais legal de tudo isso é que, agora que...

02:43

Eu tenho essas interfaces aqui, se você olhar, é Payment Gateway,

02:48

Stock Repository, Coupon Repository, Audit Log Repository.

02:54

Quanto mais para perto da zona de inutilidade,

02:57

é porque menos caras usam ele no final das contas.

03:00

E aqui é quanto mais caras dependem dele.

03:02

Por exemplo, o Order Repository tem cinco dependências,

03:05

cinco dependem dele. Então, ele está mais para esse lado aqui.

03:09

do que da zona de inutilidade e acaba tendo mais perto,

03:13

Inclusive, dessa main sequence. Mas a grande questão aqui,

03:16

é que eu queria deixar claro pra vocês, é o seguinte,

03:19

não é que é porque nós temos uma classe que, entre aspas,

03:24

é considerada o Deus, que ela é uma classe errada,

03:27

tá? Então, o ponto que a gente tá agora aqui é, a gente saiu dessa zona de dor,

03:32

e olha aqui agora, se eu olhar aqui, eu tenho... o meu database.

03:36

Então eu tirei ele da zona de perigo e coloquei ele numa zona aqui instável,

03:42

mais próxima de concreto. O que isso significa?

03:46

Ele tem uma instabilidade grande. E por que ele tem uma instabilidade grande?

03:50

Porque ele depende de 10 outros camaradas,

03:53

ou seja, ele depende de bastante gente.

03:56

Mas eu só tenho 3 caras que dependem dele ali diretamente. Então,

04:02

aqui ele começa a cheirar para a gente uma classe Deus.

04:06

Isso significa que está errado? Não necessariamente.

04:09

E é isso que eu quero trazer aqui para vocês,

04:12

que vocês tenham entendimento. Não é porque uma classe é uma classe Deus,

04:19

que ela é uma classe completamente errada.

04:22

Mas é um cheiro de que ela está acumulando muita responsabilidade.

04:26

Um exemplo bem simples ali para você.

04:28

Às vezes eu tenho uma classe Deus que ela importa

04:30

um monte de coisa para subir o servidor.

04:33

Então, eventualmente, o seu sistema vai fazer isso e ela vai cheirar dessa forma,

04:37

mas o importante é que você tenha consciência disso.

04:40

No nosso caso da classe database.ts,

04:44

ela está se comportando como uma classe Deus porque ela exporta, como se diz,

04:49

ela usa muitos caras,

04:50

então ela tem uma instabilidade muito grande com pouca gente dependendo dela ali.

04:55

Principalmente porque a gente está trabalhando com muita coisa em memória,

04:58

etc. Então,

04:59

a gente vai ter essa característica. Uma coisa que a gente poderia fazer é quebrar,

05:04

na realidade, esse database, né? E fazer com que esse database,

05:09

cada um desses caras ali,

05:11

tivessem a sua implementação concreta. Deixa eu mostrar aqui para vocês.

05:15

Se eu chegar aqui em shared e database,

05:18

vamos olhar agora o arquivo aqui em conjunto,

05:21

pessoal. E é isso que eu quero que vocês entendam.

05:24

Se vocês olharem, tá?

05:28

Dentro desse meu database.ts, eu estou importando um monte de gente.

05:33

Basicamente, esses caras que eu estou importando aqui,

05:35

eles são interfaces, tá? E agora, olha só que interessante.

05:41

Ele tem aqui, class in-memory product repository,

05:44

class in-memory stock repository,

05:47

class in-memory customer repository.

05:50

Class in-memory Order Repository. Ou seja,

05:53

eu tenho uma pancada de classes aqui dentro,

05:56

implementando, na realidade, uma interface.

06:00

Então, isso aqui está errado, de forma geral? Não está.

06:04

Ou seja, eu tenho um arquivo de database que,

06:07

no final das contas, está fazendo a...

06:10

Como que eu posso dizer? A exportação, na realidade.

06:16

Do meu in-memory database de uma forma... concreta aqui,

06:20

mas que teve a nossa implementação baseada numa interface.

06:25

Então, de forma geral, isso não é ruim. Por outro lado,

06:29

eu começo a ter um arquivo que sai acumulando um trilhão de coisas.

06:33

De forma geral, tem uma coisa.

06:36

A gente está trabalhando sempre com memory repository. Então...

06:42

O certo, entre aspas,

06:44

e daí depende muito de como que a gente

06:46

quer trabalhar ou fazer isso sem evitar overengineering, etc.,

06:50

é que cada cara desse aqui pudesse ser um arquivo diferente,

06:54

para que eu não tivesse um arquivo único

06:57

database e que tivesse muitas responsabilidades.

07:01

Então, é interessante, inclusive,

07:03

você entender o que é múltiplas responsabilidades. Por exemplo...

07:06

Uma classe pode ter múltiplas responsabilidades e isso

07:10

está quebrando para a gente o SRP,

07:12

o Single Responsibility Principle, onde ela tem apenas uma razão para a mudança.

07:18

Se você levar esse mesmo conceito para arquivos e não necessariamente classes,

07:25

eu também, cada vez que eu mexo nesse arquivo,

07:28

provavelmente tenho uma razão diferente para a mudança. Então,

07:32

o que eu poderia fazer aqui no final das contas é fazer um split desse

07:36

database.ts para que, para cada classe dessa,

07:39

no final das contas, eu tivesse o quê?

07:43

Um arquivo. E aí, nesse nosso caso, se eu tenho um arquivo diferente,

07:47

eu já não vou ter mais um único arquivo classe Deus,

07:50

vamos dizer assim, para conseguir, como que eu posso dizer,

07:54

tirar essa carga em cima do database.ts.

07:59

No contexto que a gente está agora, isso seria interessante.

08:02

A gente está num projeto exemplo, onde a gente está rodando com tudo em memória,

08:07

onde essa classe de repositórios nossas acaba sendo uma classe que praticamente

08:12

é extremamente simples e por isso que a gente está carregando aqui.

08:16

Mas ainda assim, eu não gosto tanto desse tipo de situação.

08:23

Então, a gente pode ir para...

08:25

um passo a mais caso eu queira,

08:27

porque no final das contas, esse database.ts, o que ele acaba fazendo?

08:32

Ele acaba exportando uma classe em memory database

08:36

que está instanciando realmente aqui o objeto concreto,

08:40

mas esse objeto concreto agora pode ser intercambiável pelo

08:45

fato de ele estar sendo baseado em torno de uma interface.

08:50

Então, se em algum momento eu quisesse criar um

08:52

database de verdade implementando o audit log,

08:56

isso iria funcionar,

08:57

porque eu consigo trocar agora seguindo basicamente a

09:01

mesma interface aqui no nosso caso.

09:04

Então, somente para a gente não deixar esse arquivo grandão,

09:08

eu quero fazer mais uma coisa aqui com vocês. Que é o quê? Eu quero fazer o split.

09:14

desse arquivo em diversos arquivos.

09:16

Eu não estou dizendo que isso aqui vai ser saudável.

09:17

A gente vai ter uma pancada de arquivos a mais,

09:20

mas eu vou deixar esse database.ts aqui menor no nosso caso. Então,

09:25

A gente vai ver isso no próximo vídeo. Porém,

09:27

Lembre-se, galera, isso aqui não necessariamente é algo errado.

09:33

O ponto importante que a gente fez e que já mudou muito o sistema

09:37

Nosso agora aqui é que a gente tirou esse cara dessa zona de dor.

09:42

E ele agora consegue trabalhar de uma forma muito mais flexível,

09:46

Apesar de ter um arquivo que possui muita coisa e muitas responsabilidades.

09:51

Então, esse aí é um aspecto. Então, no próximo vídeo,

09:55

Vamos fazer o split desse cara para

09:59

Que a gente consiga entender melhor todo

10:02

O processo e depois a gente pode tentar fazer um goal aqui para ele tentar...

10:08

Tirar o máximo dos arquivos dessa parte de zona de dor, tá? Às vezes,

10:13

Um cara desse que tem simplesmente esse nível aqui, por exemplo,

10:18

common.ts, onde depende de 1 e 4 dependem dele,

10:23

Ele tá numa zona de dor pelo fato desse nível de dependência.

10:27

Mas se você perceber, quantitativamente,

10:29

São poucos caras que dependem dele. São apenas 4, tá?

10:33

Então, às vezes, algo está na zona de dor.

10:36

Mas a dor não é tão grande, vamos dizer assim.

10:40

Diferente daquele nosso banco de dados ou desse cara aqui,

10:43

Que 15 caras dependem dele e ele não depende de ninguém,

10:46

Que é o logger. Então, ele aqui é um grande candidato a problema.

10:49

Agora, esses caras menores, eles não me incomodam muito porque...

10:53

Sabe, ele depende de um e dois dependem deles,

10:58

Então assim, é um alerta, tá numa zona de dor?

11:00

Tá. Mas, quantitativamente, expressivamente,

11:03

Ele não é um cara que pode deixar meu

11:05

Sistema muito instável e com problemas de mudança.

11:09

A não ser que a gente comece a aumentar as dependências dele.

11:14

Aí a coisa começa a ficar... importante, concreta.

11:17

Agora, o importante, se você perceber,

11:18

É que com esse tipo de gráfico, tá?

11:21

Você começa a entender os níveis que o nosso sistema,

11:24

Ele começa a ficar em relação ao perigo,

11:26

Né? Então, se eu olhar aqui, ó,

11:27

Tem uma classe Customer Manager que ele tá aqui numa zona de dor, né?

11:35

Saindo da instabilidade, saindo da estabilidade e indo pra instabilidade.

11:40

Mas ele está aqui numa zona de dor. Então,

11:42

A primeira coisa que eu quero fazer no próximo vídeo aqui com

11:45

Vocês é fazer com que esse banco de dados tenha menos carga,

11:49

Mas a gente sabe que a gente resolveu já um problemão. Então, vamos nessa.

11:53

No próximo vídeo, a gente trabalha e depois a gente

11:55

Tenta fazer uma operação que resolva todas essas dependências.

12:00

Lembrando, pessoal, que não tem harness nenhum. A gente não está criando a...

12:06

E plotando padrões de arquivos, guidelines, etc.

12:10

O meu cloud aqui, nesse caso, ele está fazendo da forma que ele acha melhor,

12:14

O que ele está ajustando aqui, as dependências.

12:16

Eu não estou preocupado com o harness, dele criar padrões e etc.

12:20

Porque os detalhes de implementação não fazem parte do escopo

12:25

Do que eu estou querendo trazer aqui para vocês,

12:27

Que é entender toda essa parte

12:28

De conceitos, dependências e abstrações.

12:34

Beleza? Então, vamos nessa para o próximo vídeo.

## Resumo IA

[RESUMO_IA]