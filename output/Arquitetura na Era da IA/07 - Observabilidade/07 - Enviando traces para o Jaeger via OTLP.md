Módulo: Arquitetura na Era da IA\
Aula: [Enviando traces para o Jaeger via OTLP](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18754)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

Agora a gente vai ver um pouquinho mais na prática, inclusive,

00:06

sobre o poder que a gente acaba tendo quando a gente utiliza, por exemplo,

00:10

um OpenTelemetry pelo fato de você poder trabalhar

00:15

com múltiplos backends ou providers da parte de telemetria,

00:21

de visualização e etc.

00:23

Então eu criei um exemplo aqui de forma geral bem interessante.

00:27

Por quê? Porque existem duas ferramentas famosas, vamos dizer assim,

00:33

para trabalhar com observabilidade em relação a dashboard, visualização e etc.

00:39

Uma que é extremamente simples e conhecida no mercado para

00:42

quem já trabalhava com observabilidade já faz um bom tempo,

00:47

que é o famoso Jaeger, tá? E um outro cara que é uma stack bem grande, né?

00:54

trabalha com muita coisa e não apenas observabilidade, que é o Langfuse.

01:00

O Langfuse é uma plataforma focada para a parte de A,

01:04

onde tem diversos recursos e a parte de

01:07

observability é apenas mais um desses recursos.

01:10

Então, qual que foi a ideia aqui?

01:13

Depois eu vou fazer exatamente como eu fiz com os outros vídeos,

01:17

de trás para frente. Então, o que acontece?

01:21

Primeiramente, se você olhar aqui...

01:23

Eu comentei a parte de public e secret key aqui no LangFuse,

01:28

tá? E o host,

01:31

né? Que é o OpenTelemetry Export Endpoint aqui,

01:35

onde a gente tem. Eu passei o URL, tá?

01:38

Do Jaeger, tá? E só pra você saber, eu tô trabalhando com Docker.

01:41

Então, quando você sobe o Docker Compose,

01:45

você pode rodar um --profile Jaeger. E aí,

01:49

ele vai subir também a stack do Jaeger.

01:51

Se você fizer com o LangFuse, vai acontecer a mesma coisa.

01:54

Assim, quando você subir o sistema pela primeira vez,

01:56

você não vai precisar subir essas stacks de observabilidade para você testar, tá?

02:01

Mas quando você quiser, você sobe ali com --profile.

02:05

Vou deixar sempre aí tudo no README do projeto,

02:08

quando você baixar o repositório, tá? Mas o ponto principal aqui é o seguinte, tá?

02:15

O OpenTelemetry, basicamente, o que ele vai fazer no meio de toda essa história?

02:20

Ele vai pegar todas aquelas informações, aqueles spans,

02:24

o tracing de forma geral, e ele vai mandar,

02:27

aqui nesse caso, para uma URL num formato,

02:30

num protocolo já pré-especificado. Então, o Jaeger,

02:34

aqui, ele consegue receber as informações nesse

02:37

formato que o OpenTelemetry consegue fazer. Então,

02:41

o que acontece é o seguinte,

02:43

se eu chegar aqui na minha aplicação e fizer uma pergunta, qual

02:51

nível de suporte é melhor?

02:58

Vamos colocar assim, uma

03:04

pergunta aqui de forma geral. Aqui ele deu ali, qual plano você se refere?

03:11

Plano Enterprise. Vamos lá.

03:20

E agora ele está pensando aqui para a gente.

03:24

Beleza. Ele pensou e provavelmente aqui trouxe a resposta que

03:28

a gente estava esperando aqui para a gente.

03:30

Beleza? Agora, o que acontece?

03:33

Vamos imaginar que eu quero ter mais informações

03:35

sobre quanto tempo demorou cada etapa. E não só isso.

03:39

Eu quero conseguir amarrar uma etapa na outra.

03:43

Antes a gente tinha feito isso através de um JSON que você viu,

03:47

mas... Assim, obviamente, você não tem uma clareza muito grande.

03:51

As ferramentas que são utilizadas para resolver esse tipo de problema,

03:54

elas realmente conseguem mostrar para a gente de uma forma muito mais clara.

03:59

Então, se você for aqui,

04:01

aqui é a ferramenta, a plataforma do Jaeger. E se eu selecionar aqui,

04:07

você vai ver que ele já tem aquele meu FC aí, a Reg API,

04:11

porque é o nome que eu estou dando ali para a minha aplicação.

04:14

Vou dar aqui um Find Traces e aqui você vai ver

04:17

que eu tenho alguns Tracings que acabaram aparecendo aqui para mim, tá?

04:22

A primeira coisa aqui nesse caso,

04:25

você vai perceber que eu tenho um cara com dois Spans,

04:29

mas eu tenho um outro cara aqui com cinco Spans.

04:31

Vou clicar nesse cara aqui. Se você olhar aqui nesse momento,

04:36

a gente tem algo que, de forma geral, ele é bem interessante. Por quê?

04:40

Porque lembra que eu falei que a gente estava dando um nome do AI Reg Pipeline,

04:45

que pegava o pipeline como um todo? Então,

04:47

aqui você consegue ver, na realidade, desde o início até o final,

04:52

o tempo que demorou essa requisição. Mas o ponto aqui importante é...

04:58

Quanto tempo demorou cada etapa?

05:00

E agora aqui que a parte de observabilidade acaba ficando bonita.

05:03

Por quê? Porque quando eu clico aqui nesse span,

05:06

eu consigo abri-lo. E se eu clico aqui, por exemplo,

05:10

em tags, aí eu consigo ver aqui, app docs.

05:14

usar o termo exato, precisa de clarificação, aqui foi a segunda resposta,

05:18

na segunda interação, o plano enterprise,

05:20

o tempo que ele demorou, o escopo que ele estava, o tipo de span,

05:25

porque é um span interno, porque acontece dentro da própria aplicação.

05:29

Se eu for aqui no retrieval,

05:31

eu vou ter as informações aqui de retrieval, de como que aconteceram.

05:35

Se eu for aqui na parte de API,

05:37

eu consigo também verificar como é que foi essa parte de API.

05:43

aqui nesse caso por conta do re-ranking que a gente teve,

05:48

então se você começa a perceber,

05:51

Agora eu começo a entender cada etapa da minha requisição.

05:56

E se eu chegar aqui na parte de generation,

05:58

answer generation, aqui eu vejo o tempo que demorou, se teve resposta,

06:03

o total de tokens, qual foi o modelo, input, output,

06:07

o escopo, app.reg, internal aqui para mim.

06:10

Então quando você começa a olhar as coisas dessa forma,

06:14

você consegue realmente entender...

06:18

o que está acontecendo com a sua aplicação.

06:20

E eu acho que esses pontos são um dos pontos mais importantes,

06:24

porque com isso você consegue medir cada etapa do processo.

06:27

E novamente o que eu queria trazer,

06:29

o que a gente está vendo aqui e essas etapas que a gente está mostrando.

06:35

Isso foi colocado de forma intencional.

06:39

Então, o que isso significa?

06:40

Que nós escolhemos quais etapas a gente resolveu colocar a parte de tracing.

06:45

Então, isso aí é importante.

06:47

Outra coisa importante também que talvez você deva estar perguntando,

06:51

se você nunca trabalhou com OpenTelemetry,

06:53

se você olhar,

06:54

a minha aplicação está mandando direto as informações para o Jaeger,

07:00

aqui nesse caso. Porém, o OpenTelemetry possui algo chamado de Collector,

07:06

que pode ser um serviço do lado da sua aplicação.

07:11

Ele funciona como um sidecar proxy,

07:13

ou ele pode ser um servidor onde você manda as informações para esse collector,

07:18

esse collector ele decide, formata e organiza as

07:22

informações para onde elas vão ser enviadas,

07:25

em quais casos, se ela vai enviar log, se ela vai enviar tracing,

07:28

se ela vai enviar as informações que você está querendo. Então,

07:32

desse jeito que a gente está falando, a gente está falando direto com o backend,

07:36

nesse caso o Jaeger, mas com OpenTelemetry conforme você...

07:40

vai querendo avançar daí, é um ponto mais específico,

07:43

você tem essas outras opções onde você pode escolher.

07:47

Inclusive, você escolhe o modo sampling.

07:50

Ou seja, você não precisa necessariamente mandar 100% dos seus tracings,

07:54

porque você vai ter um overhead.

07:55

Então, ele vai fazendo por base de amostras para você também ir verificando.

08:00

Então, esse é um ponto importante, mas perceba, tá?

08:03

Somente pelo fato de eu utilizar o SDK do OpenTelemetry,

08:07

basicamente, eu não precisei fazer nada ali no Jaeger,

08:11

a não ser colocar a URL dele. No próximo vídeo,

08:14

a gente vai fazer a mesma coisa, mas com o LangFuse, beleza? Então, vamos nessa!

## Resumo IA

[RESUMO_IA]