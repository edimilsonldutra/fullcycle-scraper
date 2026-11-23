Módulo: Arquitetura na Era da IA\
Aula: [OTEL - Show me the code](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18753)

## Resumo da aula



## Transcrição

00:00

E agora, pessoal, tem aquela parte do Show Me the Code, né?

00:03

Como que foi feito isso? E para ficar mais fácil de a gente olhar,

00:07

no final das contas, eu vou mostrar isso de trás para frente,

00:11

porque vai ficar mais fácil para que você consiga entender,

00:15

tá? Então, o que eu quero pegar? Eu quero pegar essa nossa classe do RegPipeline,

00:20

que no final das contas é ela que vai fazer a montagem desse...

00:26

É nela que a gente vai escolher o que a gente quer colocar como telemetria.

00:31

Então, a primeira coisa que eu quero que você olhe, tá?

00:33

É que eu tenho um Observability Setup, Tracing, tá?

00:37

Mas depois a gente vai ver que a gente tem esse arquivo de Observability,

00:39

tá? Aí, tudo igual por enquanto, né? Então,

00:42

eu tenho o Chat Model, o Planner, o Reranker, a parte do Answer,

00:46

tudo que a gente já tinha. E aqui, né?

00:48

A nossa função, o nosso método para a gente executar o Pipeline,

00:54

tá? Agora, uma coisa que é interessante é as coisas.

00:58

Request ID foi gerado com UUID, o Timings, a gente usou aqui um Pipeline Timings,

01:03

depois você vai dar uma olhada sobre isso.

01:05

E o Usage, que é o Usage Metadata Callback Handler,

01:09

onde a gente pega os dados da Langchain,

01:13

e consegue meio que adaptar para a resposta do resultado que a gente quer.

01:17

Então, o que acontece é o seguinte, se você perceber,

01:20

e pessoal, obviamente, isso aqui é um código de exemplo,

01:23

e o que eu quero mais pontuar nesse código é cada pedaço.

01:27

Então, se você olhar, eu tenho um try aqui,

01:29

e eu tenho aqui no Python, a gente usa muito um context manager, que a gente chama,

01:34

que a gente utiliza o with. O with é com,

01:37

e eu tenho um underline step, que é um passo.

01:40

Então, nesse passo eu pego o timing, ou seja,

01:44

o momento que esse negócio, que esse cara começou nesse step,

01:47

o tempo total de milissegundos,

01:50

e eu estou falando que ele vai entrar num pipeline span,

01:55

e isso aqui vai ser no final das contas

01:57

uma variável que a gente criou lá no nosso observability,

02:02

ali nas partes de configuração. Basicamente, é uma constante aqui,

02:07

então esse cara aqui como um span, que é aquele pedaço.

02:11

Dentro desse span, o que eu vou falar?

02:13

Utilizando a nossa biblioteca de observabilidade,

02:16

que é baseada no SDK do OpenTelemetry,

02:18

eu quero setar alguns atributos no span que a gente está,

02:23

o span atual, e eu vou falar que o request ID foi esse,

02:26

o feature name foi esse, o tenant foi esse, o product foi esse, e useRerank,

02:31

e aqui a gente tem o true ou false aqui no final das contas.

02:35

E aqui... eu mando ele executar, ou seja,

02:38

aqui é o nosso pipeline normal aqui rodando,

02:41

e aqui eu tenho outra parte de observabilidade,

02:44

que é os set attributes agora, que eu tenho,

02:47

tem the answer, precisa de clarification,

02:49

quantas fontes ele encontrou,

02:53

então perceba que eu estou colocando tudo isso no meu...

02:58

dentro desse meu span. Ou seja,

03:01

Essas informações são úteis para fazer sentido de que eu tenho esse span.

03:04

Caso eu tenha algum problema,

03:06

eu coloco aqui como exceção com os erros e tudo mais aqui para a gente.

03:13

E depois disso, eu tenho aqui, mas isso é muito mais para debug,

03:19

que é onde eu tenho o build model usage, a gente já tinha esse cara.

03:24

E aqui para a gente fazer o log. E agora, o que acontece?

03:28

Se você perceber, tudo que é de rodar o pipeline,

03:33

ele vai gerar esse span grandão aqui para a gente com essas informações.

03:37

E perceba que essa informação é uma informação mais de alto nível.

03:42

Porém, quando a gente entra para a execução, aí a gente tem vários passos, certo?

03:48

E aí a gente entra nesses passos. Então, o primeiro passo aqui, o step.

03:54

onde a gente tem aqui o query planning aqui que eu quero. Ou seja,

03:58

o query planning acaba virando um passo aqui para mim,

04:01

onde eu falo o que eu tenho como atributo nele.

04:05

Eu tenho o tamanho da pergunta, a pergunta normalizada,

04:11

o tipo de documento, os planos, os termos exatos e tudo mais.

04:15

Então, foi nesse step aqui. Aí, no meio de toda essa história aqui, eu tenho...

04:23

a pergunta se precisa de clarificação e tudo mais,

04:26

tem os filtros, etc. Aí eu entro em outro passo,

04:30

que é o retrieval em milissegundos,

04:32

onde eu falo que ele é de um span chamado de retrieval.

04:37

E aqui eu mostro os chunks que ele conseguiu pegar,

04:40

os filtros que ele conseguiu utilizar e tudo mais. Se teve re-rank,

04:43

ele vai trazer aqui e vai fazer o step do re-rank,

04:47

quais foram os chunks selecionados por re-rank.

04:51

Então... Aí tem as nossas perguntas normais e basicamente

04:55

eu tenho outro passo que é o Answer Generation, né? Que,

05:00

no final das contas,

05:01

ele vai trazer aqui para a gente qual modelo e

05:04

os dados de utilização que a gente já tinha,

05:07

né? Aqueles dados que vêm do nosso Langchain, certo? Então,

05:11

se você perceber aqui no final das contas,

05:14

a nossa aplicação está meio que exatamente da forma como ela estava.

05:19

A principal diferença é que entre uma etapa e outra, eu entrei com esse with step.

05:25

E no final das contas, ele vai dar um nome para um span, certo?

05:30

E vai pegar esses resultados, por exemplo, aqui no query plan depois do invoke,

05:34

e vai guardar essas informações dentro desse pedacinho, né?

05:41

Informação. E com isso,

05:42

eu consigo ver passo a passo do que está acontecendo na minha aplicação.

05:47

Então, por que eu estava querendo mostrar isso de trás para frente?

05:50

Porque agora que você olha o if-tap,

05:53

acaba ficando um pouco mais fácil de você conseguir entender,

05:56

porque cada passo eu estou registrando o nome dele,

06:00

baseado no tempo que iniciou aquela execução, para eu ter a linha do tempo,

06:04

e com o nome que eu acabei dando. Agora,

06:08

se eu chegar nessa parte aqui de nome, eu vou entrar aqui em Observability.

06:12

E esse arquivo aqui, apesar de ele ser grande... É um arquivo assim,

06:18

como se fosse uma espécie de uma abstração

06:20

para organizar a utilização do OpenTelemetry. Se você olhar aqui,

06:24

eu tenho a utilização do SDK do OpenTelemetry.

06:27

A minha ideia aqui não é dar aula de OpenTelemetry nem aula de Python,

06:30

mas eu queria trazer os conceitos que a gente está utilizando.

06:33

Então, para ficar mais fácil lá naquele RegPipeline, o que eu fiz?

06:37

Eu tenho várias constantes aqui que me ajudam.

06:40

Então, eu tenho o tracerName, app.reg, o OTLP, o OpenTelemetry,

06:46

que eu tenho aqui, é OTLP, que é o que a gente chama de OpenTelemetry,

06:50

o exporter aqui. E aqui eu tenho os nomes dos spans. Então,

06:54

eu tenho o nome da pipeline, o query planning span,

06:56

eu tenho o retrieval span, span re-ranking,

07:00

o answer generation. Então, para cada cara desse aqui,

07:03

para que eu não precisasse ficar digitando dessa forma,

07:06

eu deixei tudo nesse arquivo. Então, esse arquivo define muito mais, né?

07:10

Como que vai ser um nome... dos dados,

07:12

dos atributos que vão aparecer dentro do span.

07:15

Então, request ID, feature, tenancy, product. Então,

07:18

perceba se você olhar, ele está totalmente nested, né?

07:21

Ele tem uma hierarquia utilizando os pontos, né?

07:24

Então, app.tenant, app.userRerank, né?

07:28

E assim vai seguindo. E aqui tem algo que é importante falar, tá?

07:32

Existe algo que é chamado de GNI Semantic Conventions, tá?

07:36

São nomes que já estão sendo utilizados, tá?

07:40

que essas ferramentas já sabem ler,

07:42

que é o GenAI Request Model, GenAI Response Model,

07:45

GenAI Usage Input Tokens e Output Tokens. E daí o Duration,

07:51

Attribute, Setup Tracing, basicamente é setup da aplicação. Então,

07:56

eu estou criando um Trace Provider, falando qual é o nome do serviço,

07:59

falando que eu quero trabalhar com o Spam,

08:02

estou falando qual é o Provider do Spam Processor que eu vou ter.

08:08

E aqui é como que eu defino aquele span,

08:11

aquele with span, onde eu recebo o nome desse cara,

08:14

ele pega onde que ele começou, certo?

08:19

E aí ele executa. E caso eu tenha algum problema,

08:23

aqui é o que acontece caso tenha um erro. O erro, nesse caso aqui,

08:26

acabou caindo naquele momento. Então, é basicamente isso. Então,

08:31

aqui é como que eu seto um atributo.

08:34

Como que eu crio um spam processor,

08:36

basicamente são abstrações simples de forma geral.

08:39

Mas o ponto principal que eu quero trazer aqui para você é,

08:43

utilizando o OpenTelemetry eu consigo colocar passo a passo

08:47

o que eu quero medir com esses dados de telemetria.

08:51

E é interessante que é importante você saber que isso não é algo novo.

08:56

Vamos dizer, é novo em relação à IA,

08:58

o OpenTelemetry trabalhar com IA e ter esses dados mais nativos,

09:03

mas o OpenTelemetry sempre foi utilizado,

09:05

era um dos projetos mais famosos da CNCF, então é um projeto que,

09:10

se você já trabalha com aplicações e já

09:13

trabalhou com ou trabalha com observabilidade,

09:15

o OpenTelemetry não é uma novidade. Agora, a novidade, entre aspas,

09:19

é a entrada da IA dentro do...

09:23

OpenTelemetry e a gente seguir os mesmos conceitos. Para cada etapa que faz sentido,

09:28

Eu consigo medir aquela etapa para que eu consiga entender

09:33

onde estão os problemas que estão ocorrendo na minha aplicação. Fechou?

## Resumo IA

[RESUMO_IA]