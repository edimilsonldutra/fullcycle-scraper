Módulo: Desenvolvimento de Agentes com IA\
Aula: [Introdução aos Subagents](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18256)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos iniciar um novo capítulo dedicado aos subagentes.

00:05

Nós vamos falar de forma introdutória o que é esse conceito,

00:10

que eu imagino que você já tenha ouvido falar,

00:12

e não só ouvido falar, mas visto em alguma dessas ferramentas de codificação.

00:17

Em algum momento, em alguma sessão,

00:18

você viu que ele estava delegando alguma coisa a um subagente.

00:22

Então, é um agente que está rodando ali no contexto...

00:27

na sessão que está aberta, mas não é o agente coordenador ou principal.

00:32

Então, para lidar com esses subagentes,

00:36

nós precisamos, obviamente, entender os fundamentos e,

00:41

nisso, o ADK vai ter a sua forma de lidar com subagentes.

00:46

Outros frameworks vão ter as formas deles de lidar com subagentes,

00:50

mas nós precisamos saber quando usar ou não usar. E, obviamente,

00:56

fundamentos que vão ser únicos, independentes do framework que você está utilizando.

01:02

Vamos pegar esse quadro laranja como exemplo de um subagente, ou melhor,

01:07

de um agente. Subagente ainda nós não chegamos nesse ponto.

01:14

Assim como um software vai crescendo e vai se tornando complexo,

01:17

um agente também tende a fazer isso.

01:21

Isso significa que ele vai ter mais system prompt,

01:27

mais tools,

01:30

mais uma série de outras ferramentas.

01:33

Tudo isso vai fazendo com que seja difícil testar esse agente,

01:38

gerenciá-lo,

01:41

fazer avaliação,

01:44

nós podemos avaliar gasto de tokens, latência,

01:50

qualidade de resposta, enfim, várias outras coisas.

01:58

Então, nós podemos dividir esse

02:03

agente ou extrair determinados pedaços,

02:06

para que um outro agente desempenhe esse papel.

02:10

Até mesmo porque, quanto maior a complexidade de um agente,

02:15

nós já sabemos sobre a janela de contexto,

02:22

mais contexto nós vamos ter que lidar de uma vez só.

02:26

Isso também acaba gerando problemas.

02:30

Então, pensando que esse agente está fazendo um monte de coisas, ele

02:35

está fazendo esse pedaço,

02:38

esse pedaço e esse pedaço.

02:44

Às vezes, nós queremos só testar esse pedaço final,

02:48

mas, obviamente, no meu teste, todos esses anteriores vão ter influência.

02:55

Às vezes, eu quero testar somente esse primeiro, os outros também vão ter influência.

02:59

Então, essa quebra eu gosto muito de comparar quando nós estamos...

03:03

quebrando um monolito em um sistema separado para que ele tenha mais independência,

03:09

seja mais fácil testar,

03:10

ou até mesmo quando temos uma classe que se tornou muito complicada de manter,

03:15

nós vamos tender a quebrá-la também.

03:17

Então, nesse caso, nós podemos trabalhar com os subagentes.

03:21

Vamos pegar esse terceiro bloco e

03:26

transformá-lo em um subagente.

03:30

Então, nós temos um

03:34

outro agente, ele está encaixado,

03:39

no agente principal, e

03:42

Nós podemos até chamá-lo de agente coordenador. Então ele está subordinado a

03:49

esse agente. O que poderia ser aqui?

03:52

Nós poderíamos criar um subagente de pesquisa,

03:55

vai que numa situação eu tenho que fazer uma pesquisa,

03:58

que vai procurar alguma coisa na web ou em outros lugares.

04:05

Isso é que acontece muito nas nossas ferramentas de codificação.

04:09

Porque você tem a tarefa principal que você pediu, que é planejar uma nova feature,

04:14

explorar alguma coisa para criar um planejamento. Então,

04:17

essa exploração não precisa fazer parte do contexto principal.

04:22

Ela vai só para o subagente e ele só

04:27

retorna um resultado já condensado para o agente coordenador.

04:32

E aqui nós podemos pensar também num ganho que

04:36

num cenário sem o subagente...

04:40

Imagine que aqui eu preciso de um modelo com mais qualidade.

04:48

Já nos outros pedaços,

04:49

eu não preciso de um modelo de LLM com muita qualidade. Então,

04:53

esse pedaço pauta todo o agente,

04:56

porque eu vou sempre colocar um modelo com qualidade para atender aquele pedaço ali.

05:01

Então, aqui e aqui que eu não preciso de qualidade, eu estou pagando mais tokens.

05:07

Então, nós temos essa vantagem de poder... colocar um

05:13

modelo mais específico que vai atender à necessidade do subagente.

05:21

Fora a questão da janela de contexto.

05:24

Então, nós economizamos a janela de contexto.

05:26

Tudo que acontece aqui vai ser descartado quando ele processar.

05:29

Ele vai retornar o resultado para o agente coordenador

05:33

e ele pega somente o que é necessário.

05:35

Ele não precisa ficar com todo o histórico da pesquisa.

05:39

Então, nós temos reunido nisso vários benefícios,

05:42

poder selecionar um modelo melhor, ter mais janela de contexto.

05:47

Uma vez que temos também vários subagentes, vai que nós temos agora dois subagentes,

05:54

e a execução puder ser paralela,

05:58

nós ganhamos isso. Então, execução paralela, o

06:03

que vai fazer com que o meu agente coordenador...

06:06

consiga dar a resposta mais rápida antes que ele

06:09

tivesse que executar todas as etapas, passo a passo,

06:12

ele delega para os dois agentes ao mesmo tempo,

06:15

os dois retornam a resposta para o coordenador e

06:18

o coordenador continua fazendo a sua execução.

06:24

E aí nós ganhamos em todos esses pontos de testabilidade,

06:28

porque se eu tenho um agente só de pesquisa,

06:30

eu posso rodar uma bateria de testes focados em

06:35

várias questões da pesquisa que eu estou fazendo.

06:38

Posso lançar a web e ver como ele se comporta de outras formas,

06:42

lançar várias chamadas, ir avaliando o modelo,

06:48

gasto de tokens,

06:50

a janela de contexto. Eu tenho um ambiente muito mais fechado,

06:56

muito mais conciso, muito mais específico. Então, a testabilidade,

07:00

o gerenciamento e a avaliação são bem melhores. Eu consigo testar o subagente...

07:06

de forma totalmente separada do agente coordenador.

07:09

Obviamente, nós vamos querer testar o agente coordenador.

07:12

Vamos querer testar a relação dele com os subagentes,

07:16

mas essa granularidade acaba nos dando mais

07:20

refinamento e qualidade no que nós queremos fazer.

07:24

Temos também o benefício do reuso.

07:26

Imaginando que eu tenho muitos agentes no meu projeto, muitos agentes coordenadores,

07:33

e muitos deles precisam de pesquisa,

07:35

por que não criar um subagente de pesquisa,

07:40

não muito genérico, mas que vá atender a esse contexto?

07:44

Ele pode ser reusado em todos os agentes que precisam de pesquisa,

07:47

não preciso criar um novo.

07:49

Como é um subagente que é fácil de testar, gerenciar, fazer avaliação,

07:54

ele vai se encaixar muito bem em todos esses contextos.

07:59

Então nós podemos criar vários subagentes.

08:03

E fazer o reuso deles.

08:05

Então, nós temos vários benefícios, mas, obviamente,

08:08

nós estamos falando aqui de quando usar por conta dos benefícios e quando não usar.

08:16

Nem tudo é perfeito.

08:19

Imaginando que esse agente, que pode ter essas quatro etapas, por

08:25

que eu criaria subagentes? Às vezes, ele pode estar conciso.

08:31

Não precisa fazer essa separação, porque a separação, na verdade,

08:36

ela pode trazer mais latência de processamento,

08:38

se você não tem processamento paralelo, por exemplo.

08:42

Adicionar subagentes vai adicionar mais carga de processamento.

08:45

Pode até diminuir a qualidade, dependendo do que você fizer no subagente,

08:49

com a troca de modelo ou outras configurações.

08:56

Pode até ter mais gasto de token, e aqui não é o problema só de ter mais gasto,

09:00

é o gasto de tokens versus... versus o que está sendo

09:05

colhido de resultado.

09:07

Então, às vezes, pode não se pagar, o gasto de token pode se tornar mais caro.

09:15

Então, não vale a pena.

09:18

Então, nesse caso, o que eu tenho a avaliar,

09:21

a não ser que eu tenha um motivo já inicial de ver que

09:25

esse subagente não deveria fazer todo esse contexto

09:29

que está programado logo de cara,

09:31

eu já vou fazer uma quebra, mas você pode criar o seu agente.

09:36

Colocá-lo em produção e, à medida que você vai entendendo os resultados,

09:41

vai vendo o que ele está fazendo,

09:44

aí sim você pode avaliar o que poderia ser quebrado.

09:47

Ou crie o seu agente e faça uma avaliação dele primeiro.

09:55

Não tente já, você vai ser seduzido por ficar às vezes pegando dois trechos,

10:02

duas linhas do seu system prompt e transformar isso num subagente. Não é assim.

10:08

O subagente tem que se justificar.

10:12

Nós vamos vendo os fundamentos e onde que

10:17

ele vai se encaixando, vai ficando mais claro quando

10:21

eu deveria criar esse subagente. Então, é isso que eu quero alertar.

10:24

Não é só o ponto de quando usar, mas quando não usar também.

10:28

Os mesmos princípios e fundamentos,

10:31

aqueles fundamentos mais conservadores quando você

10:34

está tomando decisões tecnológicas, cabem aqui também.

10:38

Então, primeiro, crie o seu agente, faça alguns testes.

10:42

Veja como ele se comporta. Depois, você sai criando os seus subagentes.

10:49

Vai avaliando o que fazer. Então, a partir de agora,

10:53

nós vamos mandar ver com a DK, vendo esses subagentes em funcionamento.

## Resumo IA

[RESUMO_IA]