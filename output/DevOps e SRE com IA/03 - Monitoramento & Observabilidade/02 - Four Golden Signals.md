Módulo: DevOps e SRE com IA\
Aula: [Four Golden Signals](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18534)

## Resumo da aula



## Transcrição

00:00

A gente vai falar agora do For Guided Signals,

00:03

que é definido pelo Google SRE. Bacana? Então, o Google SRE,

00:09

ele define quatro sinais fundamentais para que todo serviço deve ser monitorado. Então,

00:13

a gente tem esses quatro sinais. Então, basicamente, eu digo,

00:17

todo serviço, sem exceção, tem que ter os quatro sinais.

00:22

Latência, Traffic, Errors e Saturation. Ok? O que é a latência? Tempo de resposta.

00:30

Então, é um tempo de resposta do serviço.

00:34

A média é mais ou menos ali mentirosa, né?

00:39

Porque se 99 % dos requests respondem em 10 milissegundos,

00:42

1 % responde em 1 milissegundo,

00:45

a média parece ok. Por isso, precisamos de percentis, tá?

00:49

Então, não necessariamente a gente vai medir sempre desse jeito. Então,

00:53

a gente vai ter percentis. Então, a gente vai ter uma mediana.

00:56

que é a P50, a gente vai ter a principalidade, que é a P99,

01:01

que captura os 1 % mais lento ali,

01:04

que vai conseguir mostrar para a gente onde está lento,

01:07

justamente onde os problemas estão escondidos. E se alguém falar em latência,

01:12

pergunta -se latência em que percentil.

01:15

Então a gente vai definir ali por percentil.

01:18

O tráfego. que é a demanda sobre o sistema.

01:22

Então vai falar quanto request por segunda, quantas conexões estão ativas,

01:25

qual o troubleshoot e assim por diante.

01:27

Então isso vai dizer quanto o sistema está sendo

01:30

usado e nos ajudar a planejar a capacidade,

01:33

ou seja, escala de serviço, escala de infraestrutura e assim por diante.

01:38

Se o tráfego dobrou de uma hora para outra,

01:40

a latência e a saturação provavelmente vão ser afetadas.

01:43

Então imagine uma empresa que mexe com e -commerce. Está no período de alguma festa,

01:50

alguma coisa que vai receber uma quantidade de conexão maior do que o normal.

01:56

Então, provavelmente o tráfego que vai receber esse serviço vai aumentar bastante.

02:01

Então, a gente vai conseguir pegar nesse cara. Legal?

02:05

Então, o tráfego a gente mede assim.

02:08

Quantidade de demanda no sistema. Aí a gente consegue planejar a escala e etc.

02:13

Beleza? Os erros. que é simplesmente a taxa de request que falhou, tá? Então,

02:20

a gente tem uma SLI ali de 500 rate e um SLO de errors rate,

02:26

que é de 0 ,01%, ou seja,

02:28

as minhas requisições só podem falar em 0

02:32

,1 % das vezes que elas forem chamadas.

02:37

Claro que a gente ainda entra lá na parte de...

02:43

De definição ali do percentil, tá? Também cabe aqui. Ok?

02:48

Então, por essa taxa corresponder a erros 500, taxa de timeout,

02:53

taxa de erro de negócio e assim por diante. Você consegue colocar vários tipos aí.

02:57

Aqui a pergunta é simples. A cada 100 requests, quantos falharam?

03:02

Aí a gente tem que olhar isso. Se a taxa de erro está em 0 ,1%,

03:06

nosso SLO é de 99 ,9 % de sucesso. Está em risco.

03:12

Então aqui a gente vai definir essa parte de erros.

03:17

A saturação é o quão cheio o sistema está. CPU está em 80%, memória em 90%,

03:24

connection pool 95%. Então são os sinais que o sistema está perto do limite.

03:29

Então é a saturation,

03:30

onde a gente vai olhar se o sistema está no limite da operação dele.

03:36

Então a saturação é o sinal...

03:40

mais importante. Então,

03:41

a gente consegue ver quando o sistema está para falhar a infraestrutura. Então,

03:47

a saturação ali que ajuda a gente. Então,

03:49

antecipar problemas antes dos incidentes virem de fato.

03:54

Se a saturação está subindo,

03:56

você pode agir com antecedência, aumentando a infraestrutura,

04:00

aumentando a capacidade do sistema e assim por diante para evitar um erro.

04:04

A gente vai evitar de cair em um erro aqui. Tá bom?

04:08

Então, cada um desses sinais vira um SLI, que vira um SLO com target,

04:13

o target nosso aqui é o nosso limite de falha, ok?

04:17

Então, por exemplo, latência de P99 menor que 500 milissegundos,

04:23

taxa de erros menor que 0,1%,

04:27

a saturação do CPU abaixo de 80%,

04:31

ok? A skill do módulo 2, a skill 2, desculpa, do módulo 1,

04:37

faz essa tradução automaticamente. Legal?

04:40

Então a gente vai tentar usar a skill aqui de novo para mostrar para vocês.

04:43

Que é a descrição do serviço para SLI mapeado

04:46

em golden signals até o SLO com target. Ok?

04:50

Então esses são os forgotten signals aí para

04:54

a gente fazer o monitoramento efetivo dos nossos serviços. Ok?

04:59

Está até escrito aqui que as skills,

05:02

mapeamento e SLO do módulo 1 automatizam essa tradução.

05:06

Combinado? Então, façam um estudo também sobre,

05:09

se aprofundem mais sobre esse assunto,

05:11

que é bastante interessante para a parte de SRE.

05:14

Vamos para o próximo aqui, que é o Error Budget, derivado do SLO.

05:19

Legal? Então, o Error Budget é um conceito simples,

05:23

mas é transformador para a forma de como um time opera.

05:27

Então, ele é muito importante como um time vai operar.

05:30

Então, vamos calcular aqui o nosso Error Budget.

05:37

9%, ok? De disponibilidade em um mês, 30 dias.

05:41

E o error budget é de 0,1%,

05:44

ou seja, 43,2 minutos por mês eu posso ficar indisponível,

05:51

tá bom? Então basicamente é,

05:53

a gente tem 43 minutos ali pra gente ficar disponível e se violar isso,

05:59

a gente viola essa ali, ok?

06:01

Se a gente olhar no dia a dia, a gente, são apenas 8,

06:06

64 segundos por dia que o sistema pode ficar indisponível.

06:09

É um SLO bem agressivo. Então,

06:12

é uma definição bem agressiva esse SLO. Então,

06:16

o sistema tem que ter muita resiliência para operar.

06:19

E para que serve o budget na prática? O erro budget na prática?

06:26

Então, a gente consegue tomar três decisões fundamentais para ele.

06:31

Primeiro, decidir se podemos fazer um deploy.

06:35

Se o erro budget está ok, beleza.

06:38

Podemos fazer um deploy, podemos arriscar um deploy no ambiente de produção,

06:44

porque a gente está com um budget sobrando.

06:47

Legal? O budget quase gasto. Então,

06:51

a gente ali já, desse tempo de 43 minutos,

06:54

A gente já gastou, imagina,

06:56

30 minutos desse tempo e a gente já ficou indisponível dentro do mês.

06:59

Então, beleza. Entre freezing. Não faz nenhum deploy dentro desse mês.

07:04

Porque o nosso SLO já está quase sendo atingido.

07:08

E a gente pode perder meta com isso aí. Legal? Então a gente consegue definir.

07:13

Então a gente consegue, através do SLO, do erro budget com o SLO,

07:19

a gente consegue planejar o que a gente vai fazer ali de deploy.

07:24

Beleza. Essa parte de deploy eu acho que ficou entendida. O segundo, para alertar.

07:30

Se a gente tem 50% do erro budget gasto, ou seja,

07:35

Ali a gente tem 43 minutos, se a gente tem 21,

07:40

22 minutos gastos do erro budget,

07:44

a gente pode gerar um alerta com isso e começar a investigar onde está falhando.

07:51

Então, o que está acontecendo aqui para gerar tanta falha?

07:55

Legal? Então, atingiu 100%? Incidente.

07:59

Bater o SLO ali, você gera um incidente, prioridade máxima para resolver o problema.

08:05

Legal? E o terceiro é a gente

08:07

conseguir equilibrar a inovação versus a estabilidade. Então,

08:13

queremos colocar coisas novas, etc., inovar um aplicativo,

08:18

inovar uma API e assim por diante,

08:21

vamos sempre olhar a parte do erro budget ali. Por quê, tá? Porque se você vai lá,

08:26

inova e derruba a sua aplicação,

08:28

aí já está contando o tempo ali que você tem de 43 minutos, tá?

08:32

Lembrando que esse 43 minutos é um exemplo, tá? Seu erro,

08:35

e aí que está bem agressivo. Então, essa ali é de 99,9%.

08:39

Você poderia colocar 99, você teria 1%. Teria um tempo a mais ali,

08:43

pensando na quantidade de tempo disponível para você ficar indisponível ali,

08:49

tá? O tempo disponível para ficar indisponível. Então,

08:52

basicamente, com o erro budget ali,

08:56

você consegue calcular como que você vai fazer todas essas partes. E com a AI,

09:03

a gente consegue mapear SLI e SLO e calcular o erro budget em segundos, tá?

09:10

Então, o que antes levava reuniões, planilhas, etc., para fazer a cálculo,

09:14

a gente pode conseguir criar um prompt bem estruturado que

09:18

vai ajudar a gente a definir esse erro budget. Ok?

## Resumo IA

[RESUMO_IA]