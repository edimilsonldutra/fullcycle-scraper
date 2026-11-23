Módulo: IA Labs\
Aula: [Evaluation trigger](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18281)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, então, continuando aqui a nossa trilha sobre avaliações,

00:06

o que a gente fez até o presente momento?

00:08

Nós começamos com uma skill que era super simples, muito mal feita,

00:14

e baseado na percepção da avaliação,

00:19

a gente conseguiu reescrevê-la, nós iniciamos ali.

00:23

trabalhando a nível de description,

00:25

foi identificado que ela não estava rodando e

00:27

que necessitaria de uma reescrita total.

00:31

Então, a gente utilizou o artifício da

00:33

avaliação para fazer esse processo de reescrita e,

00:38

baseado nisso, a gente chegou no seguinte resultado. Então,

00:43

agora a gente já tem uma skill mais bem feita ali,

00:48

se comparado com o que a gente havia feito.

00:52

Temos aqui as referências de antepartners e tudo mais. E aí,

00:55

o que a gente vai fazer a partir de agora?

00:57

Como nós rodamos a nossa avaliação e foi identificado que a nossa skill, na verdade,

01:03

precisaria ser reescrita,

01:05

acabou que o processo de avaliação da nossa descrição aconteceu,

01:11

mas acabou tendo que ser pausado pelo fato de que a gente precisou reescrever.

01:16

E quando a gente reescreveu, ela rodou. Só que rodou baseando-se...

01:21

na avaliação de qualidade. E, inclusive, se a gente der uma olhada aqui,

01:27

foi gerado alguns inputs com eventos SQL para fazer essa avaliação de qualidade.

01:33

E agora o que a gente vai fazer?

01:34

Vamos voltar agora rapidamente no

01:36

processo de avaliação para a descrição,

01:42

ou o trigger, como também é chamado,

01:45

e a gente vai verificar qual vai ser o resultado.

01:48

Somente para vocês saberem.

01:50

Eu excluí aquele workspace que a gente estava trabalhando,

01:53

só para a gente gerar um novo e

01:57

a gente conseguir trabalhar em cima da trigger.

02:01

Vamos rodar aqui o nosso Skill Creator.

02:04

Já temos aqui a Tool Ask User perguntando o que a gente deseja fazer.

02:09

Então, eu vou falar que eu quero otimizar agora a descrição. E aí,

02:12

ela vai começar o processo de avaliação

02:15

para especificamente otimizar o processo de trigger.

02:20

E aí, se a gente der uma olhada aqui, nós já temos algum resultado. O que aconteceu?

02:26

Ele abriu uma página da web com os itens aqui

02:30

para a gente escolher o que nós queremos testar ou não.

02:34

Voltamos aqui no browser para vocês darem uma olhada

02:37

e a gente tem aqui as possibilidades.

02:39

Posso incluir,

02:41

excluir da forma que eu achar que deve ser feito. Basta clicarmos aqui no Add.

02:47

Query, e aí a gente tem a possibilidade de fazer essas inclusões.

02:51

Voltando aqui, então, no nosso VS Code,

02:54

vamos ver o que a gente tem que fazer a partir de agora.

02:59

Então, nesse primeiro momento,

03:00

eu não vou mexer em exatamente nada relacionado às queries.

03:05

Vou permanecer aquilo com o que já tem lá e vou pedir para ele continuar.

03:10

Então, continue o

03:13

Processo e vamos ver o que vai acontecer.

03:17

Já temos aqui uma pequena resposta. Bom, o loop está rodando aqui em background.

03:22

Se a gente botar uma setinha abaixo aqui,

03:24

a gente consegue verificar o que está acontecendo.

03:26

Já está rodando há praticamente dois minutos. Vamos aguardar até o resultado final.

03:33

Bom, pessoal, temos aqui o resultado. Então, ele conseguiu rodar o loop.

03:39

Inclusive, identificou aqui que na versão que eu

03:42

estou utilizando aqui do Cloud Code,

03:44

aconteceu um erro.

03:46

No qual, ao gerar esse teste,

03:50

ele acabava acrescentando o hash dentro do

03:54

nome da skill e aí impossibilitava de encontrar.

03:59

Então, automaticamente, ele já se autocorreu e aí ele conseguiu medir aqui.

04:05

E aí a gente tem o accuracy aqui de 100%,

04:09

recall também 100%, precision também 100%.

04:12

Ou seja, isso quer dizer que a nossa descrição está muito boa.

04:17

E logo mais abaixo, a gente tem aqui a nossa decisão. A descrição já está ótima,

04:24

não alterei nada e tudo mais. E aí, ao final disso, o que ele gera para a gente?

04:28

Ele gera um HTML também, assim como eu mostrei anteriormente para vocês,

04:32

da parte de dados.

04:35

Ele também vai gerar um HTML focado

04:38

no processo de trigger e otimização da descrição.

04:43

Eu vou mostrar para vocês.

04:46

Inclusive, eu pedi para ele gerar duas versões para mim,

04:49

para ficar um pouco mais fácil de mostrar para vocês.

04:51

Então, essa aqui é a versão padrão que ele vai gerar para você,

04:55

no qual ele mostra para a gente a versão

04:57

original que está na nossa skill atualmente.

05:01

E ele também já faz aquele processo de auto

05:04

-otimização que eu havia falado para vocês.

05:06

Então, em tese, se vocês lerem aqui...

05:10

A descrição em si é praticamente a mesma coisa, tá?

05:13

E aqui embaixo a gente tem os dados de teste e tudo mais.

05:16

Depois eu falo um pouco mais sobre essa parte do treino e do teste.

05:20

E aí eu pedi, como eu disse,

05:22

para gerar uma versão um pouco melhor de visualizar a parte dos testes em si,

05:26

que já está aqui. Então,

05:28

a gente tem aqui a medição. Temos a descrição, de fato.

05:31

E aqui a gente tem toda a legenda do que aconteceu,

05:35

tá? Então, o verdinho que é o shoot trigger.

05:39

O vermelho, should not trigger.

05:41

Temos aqui a parte de treino e temos a parte de teste.

05:44

E aí, nós temos o resultado esperado aqui, baseando-se nos itens do dataset.

05:51

Conforme a gente pode ver, nós temos aqui o que foi executado,

05:55

como foi executado e qual foi o resultado. Assim,

05:58

a gente consegue visualizar muito melhor. Porque se você reparar aqui,

06:02

não fica tão legal o processo de visualização.

06:05

Então, eu só pedi para ele remodelar,

06:09

com um layout diferente. Para ficar mais fácil para vocês.

06:11

Analisarem junto comigo. Então, dessa forma.

06:15

O que a gente consegue notar. Que a gente consegue.

06:19

Fazer bastante coisa com o Skill Creator. Desde.

06:24

Usar ela como realmente.

06:26

Algo que eu vou.

06:29

Testar. E viabilizar versões novas. Da minha Skill.

06:34

Baseando -se naquilo que eu já. Havia produzido. Ou.

06:39

Por meio desse processo de evaluation, a gente consegue, como eu mostrei para vocês,

06:44

entender os pontos de melhoria ou até mesmo utilizar isso

06:50

como uma bússola para saber aonde a gente quer melhorar.

06:54

Então, se vocês pararem para analisar,

06:56

a gente meio que pode seguir ali um caminho um pouco mais padrão,

07:01

que é o uso da skill para, de fato, aquilo que ela foi feito,

07:05

que é avaliar, ou um caminho... tipo uma bússola,

07:09

onde olha, tem essa skill,

07:10

não sei se realmente está indo de acordo com o que eu quero,

07:14

olha aí, baseado nisso, vamos corrigindo junto,

07:17

em conjunto ali com os comandos que você vai passando para o CLI,

07:22

beleza? E agora, para finalizar,

07:24

eu queria só falar como vai funcionar esse processo de avaliação que é feito.

07:31

Então, vamos lá pessoal, deixa eu voltar aqui no browser rapidão, que a gente vai...

07:34

utilizar ele aqui só para dar um contexto de como tudo isso funciona.

07:39

Bom, basicamente, quando a gente vai fazer esses testes,

07:43

a gente vai fazer primeiro o dataset,

07:46

que eu havia mostrado para vocês,

07:47

e aí ele vai fazer a

07:50

separação desse dataset em grupos diferentes.

07:55

Vai ser um grupo de treinamento e um grupo de teste.

07:59

E aí é provável que em dado momento você deve ter visto...

08:03

Um cara chamado Redout,

08:06

que está logo aqui. Vamos procurar onde ele está.

08:13

Deixa eu ver se ele aparece aqui.

08:15

Aqui, Redout. E aí deve ter se perguntado o que é isso.

08:20

Basicamente, é um termo de metodologia de validação técnica.

08:25

Usado no desenvolvimento e validação das skills e tudo mais. Na prática, o que...

08:31

acontece de fato, como que a gente utiliza isso? Bom,

08:35

nós vamos ter a separação daquele nosso dataset,

08:39

conforme eu havia falado para vocês, em dois itens. O conjunto de treinamento,

08:45

cerca de 60 % dos dados, e a gente vai ter também o conjunto de teste separado,

08:52

que é o nosso head -out, que são... os outros 40%. E aí,

08:57

esses caras meio que vão ficar guardados ali,

09:00

de forma totalmente separada. Então, num primeiro momento,

09:03

não serão utilizados, tá? E não vão ser vistos, conforme já foi falado.

09:09

E eles vão ser utilizados em um segundo momento, para testar se, efetivamente,

09:14

as alterações que estão sendo aplicadas ali no looping,

09:19

que está acontecendo, de avaliação, estão fazendo sentido ou não. Garantindo o quê?

09:25

Que o agente realmente compreendeu a

09:28

habilidade que está sendo testada e, claro,

09:32

se consegue lidar com as situações novas que

09:35

estão sendo demandadas com a devida precisão. Então,

09:39

repare que é um sistema bem inteligente, porque ele consegue,

09:43

Primeiro, baseado naquilo que já existe,

09:46

Fazer o teste, depois ele roda um processo de otimização,

09:49

Pega o restante do dataset,

09:53

E faz novamente uma nova rodada de teste. E assim sucessivamente,

09:57

Até a gente conseguir concluir que nós

10:01

Temos um match melhor de trigger / description,

10:05

E aí a gente tem o resultado. Obviamente,

10:08

Nós poderíamos ficar nesse looping eternamente.

10:11

Então, a ideia é que a

10:14

Gente consiga manter algumas métricas básicas ali,

10:19

E a gente consiga atingir essas métricas básicas.

10:22

Pontos importantes que a gente tem que analisar é que

10:24

Tudo que eu estou mostrando aqui para vocês,

10:26

Como eu disse, estou utilizando um CLI, um Harness,

10:29

Que é o Cloud Code, e o modelo também da Anthropic.

10:33

Vocês têm que fazer isso.

10:35

Me refiro aos testes e tudo mais de acordo com o CLI que

10:38

Você está utilizando e também com o modelo que você está utilizando. Por quê?

10:41

Modelos diferentes vão ter respostas diferentes e atuações diferentes também.

10:46

Então, quando a gente entra nessa parte de...

10:51

Na avaliação, a gente percebe que é um mundo totalmente novo,

10:55

Porque vai mudar muito de acordo com o modelo, de acordo com a versão,

10:59

De acordo com o Harness que está sendo executado.

11:02

E tudo isso a gente deve levar em

11:05

Consideração quando nós estamos criando as nossas habilidades. Fechado?

## Resumo IA

[RESUMO_IA]