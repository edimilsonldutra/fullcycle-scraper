Módulo: Arquitetura na Era da IA\
Aula: [Validando dataset para sincronização com o Langfuse](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18782)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:03

O que eu fiz aqui para a gente começar essa nossa jornada com um dataset?

00:10

Então, o negócio é o seguinte, se você ver, eu tenho esse JSON gigantão aqui,

00:15

onde cada linha faz parte dessas informações para a gente ter o nosso dataset.

00:23

Então, se você olhar, eu tenho o ID... eu tenho a question,

00:28

eu tenho o shouldAnswer, por exemplo, igual a true,

00:30

o shouldClarify igual a false, a acceptSearchFiles,

00:36

o nome dos arquivos, os termos obrigatórios,

00:40

uma hora, 24 por 7, os documentos esperados, por exemplo,

00:44

o SLA plan, o expected plan, o enterprise, as tags e tudo mais.

00:50

Então, se você perceber, o nosso dataset é uma quantidade...

00:54

entre aspas, gigante, de casos que a gente tem,

01:00

no final das contas, pontos que a gente espera acontecer.

01:06

Por isso que a grande sacada é no data center, no dataset,

01:12

a gente ser intencional. Ou seja,

01:15

eu coloco um caso e esse caso foi pensado exatamente,

01:18

por exemplo, para falhar. Então,

01:21

esse tipo de coisa é importante. Eu utilizei, obviamente,

01:24

IA para gerar esses datasets aqui, mas o grande ponto é que quando eu pedi,

01:29

eu pedi em casos que realmente para mim são importantes.

01:34

Ou seja, quando tem que ter resposta,

01:36

quando não tem que ter resposta,

01:37

quando a gente tem uma pergunta ambígua e coisas desse tipo.

01:41

Então, de forma geral, olha só que interessante aqui.

01:45

Primeira coisa, eu vou pegar somente para...

01:50

você tem uma ideia de avaliação. Então,

01:52

se eu olhar aqui, eu posso pegar, por exemplo,

01:57

aqui o Evolves e você vai ver que eu tenho 37 itens aqui,

02:02

que é a mesma coisa que eu tenho aqui. Legal?

02:05

Outra coisa que eu posso também fazer é olhar aqui o meu...

02:10

Deixa eu pegar aqui o meu head aqui.

02:12

Somente para você dar mais uma olhada aqui no formato da estrutura.

02:16

Porque eu mostrei em uma linha só,

02:18

então eu tenho o ID, a question, o should answer,

02:21

o should clarify, no caso, o caso seja ambíguo,

02:24

a source que a gente aceita, os required terms, os expected doctypes,

02:30

expected plan e as tags que eu tenho aqui.

02:34

Agora, o grande ponto aqui é, por exemplo,

02:36

eu tenho alguns onde eu tenho algumas atribuições. Por exemplo, se eu olhar aqui,

02:42

você vai ver que eu tenho...

02:44

29 casos onde o should answer é igual a true. Ou seja,

02:49

isso aí é importante para a gente fazer esses tipos de teste.

02:54

Eu tenho aqui, por exemplo, 4 casos onde o should clarify,

02:59

quando uma pergunta é ambígua e a gente pede uma clarificação,

03:04

eu tenho 4 casos. Eu tenho também...

03:09

Casos, aqui, que o should clarify aqui nesse meu caso, ele é falso.

03:15

Opa, onde eu tenho aqui as minhas cinco recusas, deixa eu dar um... Entra aqui, ó.

03:21

Onde ele é falso... O

03:23

que ele tá dando? O meu grep não tá funcionando, deixa eu pegar aqui, peraí.

03:29

É por conta da aspas aqui, né? Provavelmente.

03:35

Duro que não, deixa eu olhar aqui, peraí.

03:40

Deixa eu tentar fazer assim, botando um pipe na frente.

03:43

Porque eu tenho o shouldAnswerFalse e o shouldClarifyFalse aqui para mim,

03:48

onde é como se ele tivesse cinco recusas aqui. Aqui,

03:52

eu tenho os quatro mesmo. É isso mesmo.

03:55

E uma coisa interessante que eu acabei fazendo,

03:59

eu tenho aqui dentro um EvolveDataSet,

04:02

um arquivo que foi criado. E esse arquivo... ele tem, na realidade,

04:08

ele gera para a gente um comando, depois eu vou mostrar mais a fundo,

04:12

porque a gente vai ter uma sincronização com o Langfuse aqui,

04:16

tá? Mas, basicamente,

04:18

quando eu dou um python -m app -evol -dataset -e -validate -only,

04:23

né? Quando eu der um enter,

04:25

o que ele vai fazer no final das contas? Ele vai carregar os datasets,

04:29

ele vai ver os casos, e ele vai validar se esse dataset faz sentido.

04:34

E nesse caso aqui, o dataset é válido. Por que esse caso aqui é importante para mim?

04:40

Porque aqui eu estou realmente conseguindo validar a

04:42

estrutura desse dataset para eu garantir,

04:45

antes mesmo de eu começar a querer fazer aqueles testes,

04:49

sei lá, num Langfuse da vida,

04:51

eu consigo fazer a validação para garantir que essas regras que eu tenho, elas,

04:57

no final das contas, elas façam sentido. Porque se eu subir isso...

05:02

De qualquer forma, o que vai acontecer?

05:05

Eu posso ter casos de regras,

05:10

de negócio mesmo. Por exemplo, shouldAnswer igual a false.

05:14

Mas ele traz um monte de outras informações que não deveriam aparecer.

05:18

Então, o primeiro passo aqui, no final das contas,

05:21

e depois a gente vai falar especificamente sobre isso,

05:23

que é em relação à parte de testes determinísticos,

05:25

depois a gente vai para frente e vai ficando mais fácil de a gente entender.

05:29

Mas o fato principal aqui é que eu consigo

05:31

validar a integridade aqui do meu dataset.

05:34

No próximo vídeo, eu vou mostrar para vocês como que a gente,

05:40

por exemplo, consegue...

05:43

Como que eu posso dizer?

05:45

Sincronizar isso com um Langfuse para que esse dataset possa subir numa plataforma

05:51

para daí a gente começar a fazer esses testes e coisas desse tipo.

05:56

Então, isso aí é um ponto importante que a

05:59

gente pode trabalhar ou qualquer coisa desse tipo.

06:03

O que mais? Eu posso, por exemplo,

06:06

só para a gente testar uma validação, eu acho que eu podia...

06:11

Vou pensar num exemplo aqui.

06:14

Eu posso chegar aqui no

06:18

meu chat. No meu chat não, nas minhas perguntas.

06:22

Acho de answer os files aqui. Eu vou colocar qualquer arquivo.

06:26

Deixa eu ver se ele vai passar na integridade aqui.

06:31

Olha só que interessante.

06:33

Somente para você ver.

06:34

Eu coloquei aqui um nome de arquivo que nesse caso não existia.

06:41

E aqui ele já bateu.

06:43

Com o problema que a gente acaba tendo o problema aqui. Um anon source files,

06:48

Esse cara aqui. Ou seja, se eu não tenho a minha integridade garantida,

06:53

Esse vai ser um problema grande na hora que eu for rodar qualquer coisa semântica,

06:58

Porque se eu não consigo garantir o meu contrato, a gente tem esse problema.

07:01

A gente vai falar especificamente sobre esses testes depois. Fechou? Próximo passo aqui,

07:07

Eu vou mostrar a parte do LangFuse para você ficar

07:10

Por dentro de como que a gente está fazendo.

## Resumo IA

[RESUMO_IA]