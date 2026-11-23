Módulo: Arquitetura na Era da IA\
Aula: [Realizando experimento no Langfuse](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18789)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente começou a explorar mais esses

00:06

problemas que a gente acaba tendo por componentes,

00:09

e aí quando a gente identifica problemas no componente,

00:11

a gente consegue saber onde a gente vai resolver esse problema.

00:14

Agora, o grande ponto interessante aqui é o seguinte,

00:19

eu posso, na realidade agora, fazer uma rodada completa desses meus componentes.

00:26

E aí eu consigo jogar essa rodada no meu LangFuse.

00:31

Então eu tenho esse comando, que é o run components eval true,

00:35

e aqui eu só estou dando um eval components.

00:37

E se você perceber, eu não estou com a flag menos menos no LangFuse,

00:43

porque agora eu quero mandar isso aqui para o LangFuse. Então aqui nesse caso,

00:48

ele vai rodar um caso, os 37 casos aqui para mim.

00:53

Então o que ele está fazendo? Ele está pegando...

00:56

pegando a pergunta, chamando o modelo,

00:58

pegando o resultado do modelo,

01:01

e daí ele está pegando essas informações e subindo para o LangFuse.

01:06

E aí, no caso, o que a gente vai ter?

01:08

A gente vai ter a pergunta, nós vamos ter a resposta esperada,

01:13

que a gente criou no nosso dataset, por conta do dataset.

01:17

E por terceiro,

01:18

a gente vai ter a resposta gerada pelo modelo e

01:21

a gente vai ter o score por cada uma daquelas etapas.

01:25

Mas lembrando sempre que não necessariamente esse

01:29

score vai mostrar onde está o problema.

01:34

Ele pode mostrar... Quem teve o problema ali,

01:37

na realidade, ele vai mostrar onde estava o problema ali no re-ranking,

01:41

mas o problema surgiu, por exemplo, numa etapa anterior, tá?

01:45

Então a gente tem que ter esse tipo de clareza,

01:49

por isso que a gente teve um vídeo só para falar sobre isso.

01:52

Então ele vai rodar aqui esses 37 casos,

01:56

e daí com esses 37 casos a gente consegue fazer uma avaliação lado a lado,

02:01

tá? Isso aqui vai demorar, eu acho que uns 5 minutos para rodar.

02:04

Eu não quero esperar tanto,

02:06

então o que eu vou fazer aqui vai ser o seguinte,

02:09

eu vou abrir o meu LangFuse e a gente provavelmente

02:12

já vai ver um experimento que ele vai trazer.

02:14

Então se eu for aqui no meu LangFuse e clicar em experiments,

02:18

eu vou dar um atualizar aqui.

02:21

E se você olhar aqui, eu já tenho um experimento aqui que tem 16 itens por enquanto,

02:26

são 37 no total. E ele fala qual foi o meu dataset aqui.

02:31

Quando eu entro no meu experimento,

02:32

agora que as coisas acabam ficando bem interessantes.

02:35

Por quê? Olha só que interessante. Eu tenho o input, que é a questão.

02:40

Quero abrir um chamado urgente. O expected output.

02:43

Eu tenho as tags. Eu tenho o expected plan.

02:47

O should answer false. Ou seja, isso aqui é o que eu espero como resultado.

02:52

E agora eu tive esse output como resultado do modelo.

02:56

Certo? Que são esses outputs. Então,

02:59

baseado nesse output, eu tive aqui no final das contas o meu score aqui calculado.

03:06

E nesse caso, quero abrir um chamado urgente. O clarification ficou como zero.

03:11

O planner ficou com clarification matched zero aqui para mim.

03:15

Deixa eu dar uma atualização, inclusive, nesses caras aqui.

03:21

Fica melhor para eu ver. Zero.

03:25

Agora, se a gente for olhar aqui, qual o limite do meu plano?

03:29

E aí o clarification skip retrieval e o clarification match ficam como um.

03:34

Por quê? A gente entra naquela pergunta clara.

03:38

É uma pergunta ambígua e já que é uma pergunta ambígua,

03:41

ele teve que fazer uma clarificação e ele teve que

03:45

dar um skip na parte do retrieval aqui para mim.

03:49

Então, porque é uma pergunta ambígua. Se eu olhar aqui esse caso,

03:53

eu já tenho o quê? É uma outra pergunta, é quanto paga?

03:57

Então, aqui eu tenho um e um no score.

03:59

Aqui, outra pergunta ambígua do suporte do plano da empresa.

04:03

E aqui a gente vai andando. Então, aqui, commercial,

04:08

downgrade, próximo ciclo. Ou seja,

04:10

a partir de quanto vale eu fazer o downgrade do plano?

04:15

E aqui, se eu olhar o score, deu um, o planner deu um,

04:20

o planner type, a Dock Coverage, ele não falou especificamente de qual plano,

04:26

e aqui eu tenho o Plan Match 1, e eu tenho o Source Capt,

04:30

agora 1 aqui também. Então, quando a gente começa a olhar,

04:33

a gente começa a ver quais são os itens que estão passando,

04:36

e quais os itens que não estão passando. E aí,

04:40

quando a gente começa a ter essa informação,

04:42

a gente começa a verificar se é realmente,

04:44

tá? Esse componente, ele... Como se diz?

04:52

esse componente em específico que eu estou verificando tem problema ou não,

04:56

porque agora eu tenho um score para cada etapa, basicamente,

05:01

do meu pipeline. E aí tudo começa a mudar,

05:03

eu posso fazer meus filtros aqui,

05:05

eu posso buscar todos os caras que têm um filtro com score igual a tanto,

05:10

ou seja, eu falo assim, o clarification,

05:12

o plan match com score igual a zero. Então,

05:16

aqui ele vai trazer qual que é esse cara aqui para eu conseguir olhar e entender.

05:20

Então, eu consigo fazer diversos filtros aqui para eu conseguir trabalhar.

05:23

Agora, se você perceber, as coisas começam a ficar bem melhores, nesse caso,

05:28

quando eu estou usando o LangFuse, porque eu tenho uma clareza muito melhor.

05:33

E aqui eu posso, inclusive, fazer o entendimento.

05:38

Por que ele deu esse problema? Então,

05:40

Missing Policy, Plan DSLA e Plan, aqui para mim. E se eu clicar nesse item,

05:46

eu vou para o tracing desse item.

05:48

E aí no tracing eu consigo entender melhor. Demorou tanto tempo,

05:52

ele chamou esses caras aqui no experiment item task.

05:57

E agora aqui na parte de avaliação.

06:00

O que aconteceu de cada ponto.

06:02

E eu tenho de uma forma agregada vendo o que está acontecendo aqui.

06:07

Nesse caso, ele acabou nem chamando todos esses itens,

06:11

principalmente porque eu já tive os erros aqui nesse cara.

06:15

Mas eu consigo, na realidade, ver todos os itens,

06:18

tudo o que ele trouxe. Por quê?

06:20

Porque aquela parte de tracing, para mim, é importante. Então,

06:23

não sei se você começa a fazer sentido para você,

06:26

mas... Eu não tenho agora somente o EVOL.

06:32

Eu consigo sim olhar para o meu EVOL e eu consigo ver

06:35

que ele tem o problema que ele pode estar causando aqui nesse momento.

06:40

Mas quando eu quero ir mais a fundo ainda,

06:43

eu consigo olhar até o tracing daquilo para a gente

06:46

ver todas as informações que vierem em cada span.

06:50

Mas lembre-se, tracing ajuda a gente a observar.

06:53

Aqui a gente está, na realidade, testando...

06:57

O resultado do modelo baseado em um resultado que eu estava esperando

07:02

referente ao resultado que não necessariamente veio da forma como eu queria.

07:08

Então, isso aqui que é uma das coisas importantes

07:11

para que você consiga levar em consideração.

07:13

Então, quando eu estou fazendo esses tipos de EVOL,

07:15

eles vão realmente me ajudar a trabalhar e

07:20

ter essas informações lado a lado para me ajudar.

07:24

a conseguir entender o que está acontecendo com cada item.

07:28

E isso, quando eu tenho dentro de uma ferramenta, acaba ficando bem melhor.

07:33

Porque se você perceber, eu tenho essas informações também no meu terminal,

07:37

quando a gente olhou.

07:39

Porém, aqui o que acontece? Eu tenho experimentos, certo?

07:44

E eu consigo começar a comparar diversos experimentos. Então,

07:49

lembra que eu falei de baseline? Ou seja,

07:51

esse cara aqui é a minha baseline desse experimento. Mas, de repente,

07:55

eu faço alterações e agora eu começo a comparar também o

07:59

meu outro experimento baseado na baseline que eu tinha,

08:01

para ver se eu melhorei ou piorei referente ao experimento anterior.

08:06

E aí as coisas começam a ficar mais interessantes para a gente. Fechou?

08:11

Então, eu queria ter dado, na realidade, essa visão... aqui para vocês,

08:17

para vocês entenderem o quão importante é você ter um dataset bem feito e como que

08:23

você consegue pegar problemas e falhas para a gente

08:26

ir arrumando e daí a gente falar, cara,

08:28

esse dataset que eu estava esperando agora está ok

08:31

de acordo com as respostas do modelo. Opa,

08:34

e se eu trocar o modelo? Será que essas minhas respostas mudam?

08:37

Então, isso aí são pontos importantes e sem isso...

08:42

realmente fica difícil de a gente conseguir testar problemas de regressão.

08:47

Porque o que acontece?

08:49

Às vezes a gente está achando que o nosso reg não

08:51

está legal e daí o que começa a acontecer?

08:54

A gente começa a mexer em tudo quanto é lugar.

08:56

Mas a gente pode ter regressão em outros.

08:59

Então, quando você tem um dataset e a gente joga sempre essas comparações,

09:03

a gente consegue ver se a gente teve problemas de regressão e

09:05

coisas que a gente vai vendo ao longo do tempo.

09:09

Fechou? Então, é isso aí, galera.

## Resumo IA

[RESUMO_IA]