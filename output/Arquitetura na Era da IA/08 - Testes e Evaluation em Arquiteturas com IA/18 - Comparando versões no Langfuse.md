Módulo: Arquitetura na Era da IA\
Aula: [Comparando versões no Langfuse](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18797)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem? Agora a gente volta com a história de a gente fazer o EVOL,

00:07

que nem a gente fazia, nosso processo de evaluation,

00:09

com resposta determinística simples para a gente testar.

00:14

Mas o que a gente começa a pensar nesse momento?

00:18

É o seguinte, esse experimento está melhorando,

00:23

então foi o que a gente falou no vídeo anterior em relação à baseline.

00:26

Eu tenho baseline e depois disso eu saio comparando.

00:30

Então a minha ideia é ter um cara que é um baseline,

00:32

ou seja, é um cara que já está em produção, vamos dizer assim,

00:36

certo? E esse cara que a gente vai rodar, que é o baseline,

00:40

ele é um cara que está usando o re -ranking, ou seja, uma etapa do nosso pipeline.

00:47

E a gente tem um outro cara que é chamado de candidate.

00:50

Ou seja, ele vai rodar o mesmo pipeline,

00:52

com o mesmo dataset, etc., mas sem o re -ranking. Ou seja, nada no pipeline mudou.

00:59

A gente, inclusive, já tinha uma flag, que é o use re -rank, que já gera,

01:03

no final das contas, com ou sem o re -ranking. Então, isso aí é um ponto importante.

01:09

Então, primeiro, para a gente rodar, só para a gente começar do zero,

01:11

a gente vai, inclusive, ver isso no LangFuse. É o seguinte.

01:16

Eu vou rodar aqui e ele vai fazer o experimento aqui do meu camarada,

01:22

legal? E vai trabalhar esse cara aqui como o Variant,

01:27

como Baseline aqui pra gente.

01:29

Então ele vai rodar aqui todos os casos que a gente tem e ele vai...

01:34

Ficar rodando. Isso aqui é, de forma geral, rápido e barato, de forma geral,

01:39

pelo fato de que eu não estou chamando o modelo.

01:42

São testes mais determinísticos aqui. A gente vai ver o shape da resposta,

01:46

se está esperando o comportamento como a gente estava querendo,

01:51

se tem o source das fontes de dados,

01:57

se tem aquele campo de os termos, required terms, se match.

02:03

aqueles termos obrigatórios que tem que ter, a latência média,

02:06

a quantidade de tokens e o custo estimado.

02:10

Então, essa é uma ideia para a gente conseguir ter meio

02:13

que um relatório de tudo que está acontecendo em relação a isso.

02:17

Então, é bem essa ideia. Então,

02:22

vamos deixar ele terminar desse cara rodar aqui para a gente conseguir...

02:26

a verificar todos esses dados. Ou seja,

02:29

cada item que ele está passando no final das contas, ele está pegando,

02:32

processando tudo e mandando ali para o LangFuse de forma geral.

02:37

Então, acho que isso aí é um ponto importante.

02:42

Outra coisa, são 37 casos, então isso aí é um ponto importante.

02:46

E uma coisa que eu tinha falado em relação ao teste determinístico,

02:51

na realidade não é necessariamente isso.

02:57

Porque é muito fácil confundir na realidade.

03:00

Quando eu falo de não chamar o modelo e teste determinístico,

03:04

isso são coisas um pouco diferentes.

03:07

Quando a gente está trabalhando com experiment, a gente vai chamar o modelo,

03:11

mas os dados que estão ali são dados determinísticos. Então,

03:16

esse é o ponto importante. Então, por quê?

03:19

Quando eu chamo modelo e eu tenho um componente,

03:22

eu tenho um teste determinístico. Quando eu estou com o ragas,

03:24

eu chamo modelo, eu tenho uma chamada de modelo com ragas,

03:28

Porque ele vai meio que trabalhar.

03:31

Como uma IA validando o que está acontecendo no Regas.

03:34

No Judge, mesma coisa que o Regas.

03:36

Você está usando um modelo para avaliar a resposta de outro cara.

03:40

Nesse nosso caso, no experimento,

03:42

a gente chama o modelo porque ele vai rodar o pipeline,

03:44

mas no final a gente tem o critério determinístico,

03:48

melhor chamado dessa forma. Então, se você olhar aqui, olha só que interessante.

03:55

Eu tenho o sumário, então a variante aqui pra mim é o baseline,

03:58

eu tenho o dataset, os casos, e aqui tem, ó, answer shape, 37,

04:03

expected behavior, 34, 37,

04:06

accepted, sourced match, 28, 29,

04:10

required terms match, 27, 29, average latência aqui e tal, ó,

04:15

latência média aqui de 4 segundos, o total de tokens que ele gastou aqui.

04:19

Foi bastante token e o custo estimado nesse caso aqui foi de dois centavos,

04:23

tá? E aqui ele mostra quais foram as falhas, né? Ou seja,

04:26

o experimento estava esperando um determinado behavior,

04:29

a gente teve o ponto ambíguo,

04:32

o negativo e o company, aquele problema do e-mail financeiro famoso.

04:36

A gente tem o experimento aceito com o source que tem esse

04:40

cara do company e o experimento que tem os termos com match,

04:44

a gente tem esses dois caras aqui também.

04:47

E isso aqui foi gerado, um JSON local, mas eu tenho aqui como rodar no LangFuse,

04:53

porque essas informações foram rodando e também

04:56

foram sendo enviadas aqui pro LangFuse. Deixa eu dar um enter aqui.

05:00

Olha só, se você cai no meu experimento,

05:03

então basicamente eu tenho aqui, ó, questão,

05:05

abriu um chamado, e aqui eu tenho meu baseline, basicamente, e esse meu baseline,

05:11

tá até escrito aqui o nome do meu experimento, baseline re-rank. Está vendo?

05:15

Ou seja, aqui tem a opção com o re-rank aqui para mim.

05:17

E aqui tem as notas que estão acontecendo,

05:20

os scores que ele está gerando. Basicamente,

05:22

o que a gente fazia e o que a gente tinha logo desde o início aqui para a gente.

05:28

Então, esse cara aqui é o nosso baseline e acabou. Isso aqui não tem muito segredo.

05:34

Agora, o grande ponto de tudo isso vai ser o seguinte.

05:39

Uma vez que eu tenho esse baseline, eu já tenho toda essa informação,

05:43

o que eu preciso fazer? Eu preciso rodar o meu candidato.

05:47

Então, qual que vai ser o meu candidato no final das contas?

05:51

O meu candidato vai ser exatamente o mesmo cara,

05:55

porém, ele vai ter sem re-rank. Então, eu vou...

06:01

Deixa eu até dar um comando direto aqui. Então, se você olhar, Variant,

06:06

esse aqui é o Variant. E no re-rank aqui para mim.

06:11

Então esse cara aqui, ele vai fazer a mesma coisa no experimento,

06:15

mas ele vai pular a etapa de re-rankear. Lembrando que essa etapa de re-rankear,

06:21

ela tem um custo no meio dessa história.

06:23

Esse custo, no final das contas,

06:25

tem chamado de modelo e a latência que acaba trabalhando.

06:28

Porém, o re-rank normalmente melhora os nossos resultados.

06:32

Então isso aí é um ponto importante para a gente olhar.

06:36

Então esse aqui é o nosso segundo passo. Então eu tenho uma variante.

06:41

quer dizer, eu tenho um baseline, eu tenho uma variante,

06:43

e depois disso a gente vai para o ponto terceiro no final das contas,

06:49

que é meio que uma comparação entre o baseline e com o no re -rank,

06:55

para a gente conseguir ver o que acaba ficando melhor.

06:59

Então a gente tem que esperar esse cara rodar ali para a gente ter os resultados.

07:05

Eu dei uma pausinha e agora...

07:07

rodou aqui esse nosso cara agora com essa nossa variante. Então,

07:10

a variante é, não tem re -rank, o mesmo dataset, a quantidade de casos, e aqui,

07:16

37, 33, 27, 24, a latência, o total de tokens e o total,

07:23

o custo estimado aqui para mim.

07:26

Então, se você olhar aqui, esses resultados agora,

07:29

eles já são significativamente diferentes.

07:33

do outro resultado que a gente teve ali com o Baseline. Principalmente, inclusive,

07:40

a parte de latência, mas tem a parte de qualidade aqui.

07:42

E tem os experimentos aqui que acabaram falhando. Se você perceber,

07:46

eu tenho mais falhas aqui do que o anterior.

07:50

Porém, o que acontece nesse tipo de situação?

07:54

Eu tenho que poder comparar. Mas antes disso, deixa eu abrir aqui no Langfuse.

07:59

Já peguei até a URL para a gente olhar.

08:03

esse cara aqui. Então deixa eu pegar aqui, o Lenfuse, vou abrir,

08:10

e eu tenho aqui agora esse candidato que a

08:15

gente utilizou para comparar em relação com o nosso baseline.

08:19

Então, todas as perguntas e todas as respostas, ou seja, um experimento normal,

08:24

mas a diferença é que aqui a gente não teve a etapa do re -rank.

08:28

Ou seja, teve uma etapa a menos no nosso pipeline.

08:31

E agora o interessante é que a gente vai conseguir, no final das contas,

08:35

comparar se realmente valeu a pena a gente ter a etapa de re -rank.

08:41

Porque até agora a gente partiu do princípio que era melhor.

08:44

Mas será que eu consigo provar isso com um dado?

08:47

Então, por conta disso, o que eu posso fazer? Eu tenho meu outro script aqui,

08:52

que eu dou um eval experiment e eu dou um menos menos compare do meu baseline.

08:57

com o meu no re -rank. E aí,

09:02

ele rodou aqui a comparação desse meu experimento. Então,

09:08

o shape das respostas é zero. Aqui, o expected behavior caiu um.

09:14

O accepted source match caiu um. O required terms match caiu três.

09:19

A latência aqui caiu um segundo.

09:23

E o total de tokens caiu aqui 49 mil tokens

09:26

e o custo estimado caiu em menos 0 ,082 centavos. Agora,

09:33

o ponto que a gente tem que entender é, sei lá,

09:36

se eu estou economizando quase 50 % nos tokens e um segundo por pergunta,

09:41

isso significa melhor?

09:43

Depende. Eu tive quatro regressões de qualidade aqui, se você perceber. Então,

09:48

aqui é onde que a empresa, o produto e as coisas vão colocar na balança.

09:54

O que é melhor?

09:55

Eu ter uma regressão aqui e

09:58

ter menos um segundo e economizar 42%,

10:03

sei lá, 40 % dos tokens por pergunta. Então,

10:06

por quatro regressões de qualidade. E agora, a grande questão é...

10:10

Você aceita isso ou não? E não tem pergunta certa.

10:14

O ponto é que a gente tem que decidir e basicamente

10:18

o fato é que nós temos aqui de forma geral essa comparação.

10:23

Então isso aí é um ponto importante quando a gente quer trabalhar.

10:30

E em relação ao Langfuse, a gente consegue fazer algo bem interessante.

10:34

Eu estou aqui no meu baseline e eu posso

10:37

bater esse cara contra um outro experimento.

10:40

Ok? E agora, olha só que interessante aqui. Deixa eu esconder esse cara,

10:45

esconder os filtros aqui para mim. Se você olhar agora,

10:49

olha só que interessante, galera. Eu tenho o meu baseline,

10:53

que foi o primeiro cara que eu fiz,

10:54

e eu tenho o meu experimento que eu fiz aqui com o re -ranking. E agora,

10:59

aqui, eu estou fazendo essa comparação.

11:01

E aqui ele está mostrando para mim exatamente...

11:04

cada item, aonde ficou mais caro, mais barato, como é que as coisas mudaram.

11:09

Aqui diminuiu 227 milissegundos, aqui menos 103 milissegundos,

11:14

nesse cara aumentou 6 milissegundos,

11:17

nesse cara caiu aqui um segundo e diminuiu o custo.

11:21

Então você consegue ver item a item para que você

11:26

consiga realmente ver o que vale a pena. Por quê?

11:29

Naquele meu relatório simples que eu trouxe ali embaixo, né?

11:33

eu peguei, categorizei e tirei. Mas aqui eu consigo olhar por item.

11:38

Eu acabo conseguindo olhar por linha do dataset o que cada cara aconteceu.

11:43

Então, se você olhar aqui, por exemplo, essa pergunta,

11:47

qual é o preço do plano enterprise,

11:48

sem o re -rank, você vai ver que eu tenho aqui esses tipos de problema aqui.

11:54

Eu perdi esses caras.

11:56

Agora, tem casos aqui que, no final das contas, olha só.

12:01

quanto o plano pró. Então, eu tinha um aqui de pontos,

12:05

a pontuação aqui continuou um,

12:07

o meu custo diminuiu, quer dizer, o meu custo diminuiu,

12:12

eu tive essa mudança em relação a custo,

12:14

e ainda a minha latência acabou sendo menor em relação a tudo isso.

12:19

Então, é interessante você conseguir olhar,

12:23

porque agora você consegue bater com dados. Esse claramente aqui,

12:26

são pontos importantes. Qual é o e -mail de suporte?

12:30

Galera, aqui dá pra ir longe, a nossa ideia não é ficar discutindo o dado em si,

12:36

mas que você consiga entender que essa parte de

12:38

comparação é algo importante aqui nesses aspectos,

12:42

principalmente quando você faz essa utilização desses experimentos, tá?

12:46

O LangFuse, obviamente, ele vai te ajudar, você consegue filtrar, e aqui,

12:50

né, no script que eu acabei rodando, você tem acesso,

12:53

vai ter acesso a todo esse repositório e tudo mais,

12:55

então fica sossegado com isso, onde você pode ver, mas basicamente...

13:00

rodar o experimento e jogar pro LangFuse nada tão

13:02

diferente do que a gente já havia falado

13:05

e a única coisa foi essa parametrização pra gente

13:08

conseguir gerar esses experimentos e gerar um arquivo JSON,

13:13

inclusive na nossa pasta de eval runs aqui

13:18

que tem o resultado e é esse resultado que

13:21

no final das contas tá indo lá pro LangFuse

13:23

então a gente tem aqui a nossa comparação

13:27

E, no final das contas,

13:29

Lá você consegue ver no Langfuse item a item para ficar um pouco mais fácil.

13:34

Fechou? Então, é isso aí, galera.

## Resumo IA

[RESUMO_IA]