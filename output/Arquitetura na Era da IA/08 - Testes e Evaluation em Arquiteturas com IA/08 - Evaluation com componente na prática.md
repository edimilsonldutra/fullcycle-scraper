Módulo: Arquitetura na Era da IA\
Aula: [Evaluation com componente na prática](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18787)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, agora o negócio é o seguinte, nós temos ainda o nosso Evolve Dataset,

00:07

onde a gente tem o foco no dataset de forma geral,

00:10

para fazer todas essas verificações. Porém,

00:13

o nosso ponto principal agora aqui é falar sobre componentes, porque o que acontece?

00:19

Quando você faz uma avaliação direta ali só no dataset,

00:23

você está olhando muito o quê? Principalmente a resposta final.

00:27

Porém... Essa resposta final, no caso de um pipeline para RAG,

00:31

ele tem diversas etapas para essa resposta final ser gerada. Então,

00:37

o que eu preciso saber também é em quais componentes do meu

00:41

RAG eu tive o problema para que a minha resposta estivesse errada.

00:47

E eu acho que esse é o grande ponto,

00:49

porque se você não consegue fazer esse tipo de verificação...

00:53

você acaba ficando se perdendo.

00:54

Você muda prompt, você muda isso, muda aquilo,

00:57

mas você não sabe aonde realmente o problema aconteceu. Então, o que acontece?

01:03

Nesse eval component, o que eu acabei fazendo? Eu consegui passar,

01:09

eu consegui fazer a avaliação dele somente naquela etapa que ele está.

01:15

Eu vou dar um exemplo que eu acho que fica um pouco melhor para você.

01:20

Então, se você olhar, e depois eu vou mostrar isso como um Langfuse,

01:23

provavelmente num próximo vídeo aqui, tá?

01:26

Então, o que acontece? Eu tenho um run components evol a igual a true,

01:30

e se você olhar, eu estou dando um Python -m, a evol components no Langfuse,

01:36

eu não quero que ele mande isso para o Langfuse agora,

01:38

e eu estou passando o case ID,

01:40

que é o SLA P1 Enterprise. Quando eu dou um Enter aqui,

01:45

o que acontece? Eu vou pegar esse case,

01:48

e esse case vai gerar meio que um relatório aqui no meu console,

01:54

trazendo aqui para mim todas as etapas do componente e se aquela etapa passou.

01:59

Ou seja, se deu certo de acordo com o que eu estava imaginando.

02:04

Então, se você olhar agora aqui,

02:05

eu tenho o Planner Clarification Match. Então, ele deu um 1 de 1.

02:09

Ou seja, o Planner passou. Ou seja,

02:12

deu o resultado como eu esperava. O Plan Match deu certo também.

02:16

O Doctype. Deu certo, o Retrieval Source Hit. Deu certo.

02:20

O re-rank source-capt deu certo. E o clarification-skips-retrieval deu zero.

02:26

Mas se você ver aqui, ele está como NA,

02:28

como não aplicável. Por quê? Porque eu não preciso de clarificação,

02:33

uma vez que não houve uma pergunta de clarificação.

02:37

Então, não faz sentido esse aqui estar de um a um.

02:39

Mas também o zero dizer que é um erro não é um erro.

02:42

É simplesmente porque o ponto não é aplicável. Então, nesse momento agora,

02:46

eu consigo ver que essa resposta, ela deu certo.

02:49

Porque cada etapa do meu pipeline acabou dando certo no final das contas.

02:55

Então, esse aí que é o grande ponto no meio dessa história.

02:59

Eu vou dar mais um exemplo aqui de pontos que talvez, por exemplo, não se apliquem.

03:04

Deixa eu limpar aqui.

03:07

Aqui, se você perceber, eu tenho uma pergunta ambígua. Ou seja,

03:12

se você olhar o meu case a dia, é ambíguo quanto ao pagamento. O que isso significa?

03:19

Quando a pergunta é ambígua, ele precisa de clarificação, certo?

03:24

Então, se você olhar aqui, o Planner Clarification,

03:27

ele passou, ou seja, ele conseguiu verificar se precisa de clarificação.

03:31

Todos os outros agora aqui,

03:33

eles deram como não aplicável. Por quê? Porque se precisa de clarificação,

03:40

ele não vai passar pelo Plymat,

03:42

para o Doctype Coverage, com o Source Hit e com o Rerank,

03:45

mas ele tem que dar um aqui,

03:48

no final das minhas contas, o Clarification Skips Retrieval 1,

03:53

porque eu pedi a clarificação. Então,

03:57

eu espero que tenha feito sentido isso para você que eu estou te mostrando.

04:01

Então, não é porque o score dá zero, nesse nosso caso que a gente acabou colocando,

04:06

que necessariamente algo está errado. E por isso que você precisa entender...

04:11

na hora que você está fazendo a evaluation, se o score 1 ou 0, 1 ou 0,

04:17

se as coisas passaram ou não,

04:18

faz sentido de acordo com o que a gente estava esperando. Agora,

04:24

a gente começa a entrar em alguns outros

04:27

pontos que a gente realmente começa a ver falha, ou seja,

04:33

as coisas começam a poder ter problema.

04:36

Eu vou dar um exemplo aqui para que você consiga entender, ficar mais claro.

04:42

Se você olhar aqui,

04:44

eu estou pegando um case ID que

04:47

é ambíguos chamado urgente aqui para mim.

04:52

E só para você saber, tudo isso que eu estou rodando agora,

04:55

ele está chamando o modelo. Então,

04:57

isso aí é um ponto importante que eu preciso dizer para você.

05:02

Ele está chamando... o modelo aqui nesse caso.

05:05

Então, o que acontece aqui para mim? Eu acho que esses pontos que são importantes.

05:11

Eu tive aqui algumas falhas. Eu tive uma falha aqui no Planner Clarification Match,

05:18

que ele estava explorando uma clarificação,

05:22

e o Clarification Skip Retrieval, ele deu falso.

05:25

O que aconteceu no final das contas aqui? Realmente houve falha.

05:30

Esse caso, o que aconteceria? Era para ele dar um aqui,

05:35

para ele pedir a clarificação.

05:37

E aí, quando ele pedisse a clarificação,

05:41

a clarificação aqui teria que dar um também e esses caras como zero.

05:45

O que significa isso?

05:47

Que nós temos problema realmente com esse case. Ou seja,

05:51

eu estava esperando um resultado e o modelo me devolveu outro.

05:55

E eu consigo saber agora que o problema...

05:58

principal estava nessa rodada onde aqui era para ter

06:02

dado 1 e gerou um efeito dominó.

06:04

Então provavelmente eu teria que melhorar essa parte do sistema, talvez o prompt,

06:10

etc. Mas focado aqui nessa parte de clarification match aqui para a gente.

06:17

Então isso aqui é um erro que é uma falha limpa, vamos dizer.

06:21

Quando o onde e quem são a mesma coisa, no final das contas.

06:26

Então, isso aí para a gente é importante a gente conseguir entender.

06:31

Então, isso aqui acaba ficando muito claro. Então,

06:34

nos exemplos que eu te mostrei até agora, tudo está fazendo sentido.

06:39

Onde as coisas acertam, eu consigo perceber que funcionaram.

06:43

Quando algo não é aplicável, eu consigo perceber.

06:46

E quando uma falha real acontece,

06:49

A gente consegue perceber exatamente o porquê que isso aconteceu,

06:53

em qual etapa que isso aconteceu.

06:57

Então, eu acho que isso é um ponto importante. Agora,

07:01

existe um outro tipo de falha, que vamos dizer, é uma falha mais rica.

07:06

E quando a parte onde do negócio é quem,

07:11

eles são diferentes. Porque nesse caso aqui são o mesmo cara,

07:15

o Planner e o Clarification, eles têm total relação aqui.

07:18

Agora o ponto é que você pode ter uma

07:21

falha onde na etapa que está acontecendo aquela falha...

07:27

Ela é consequência, na realidade, da falha anterior.

07:30

Então, o problema está anterior,

07:32

apesar de eu conseguir pegar essa falha. No próximo vídeo, eu vou mostrar isso aqui.

07:37

Eu acho que vai ficar mais fácil aí para você entender. Vamos nessa.

## Resumo IA

[RESUMO_IA]