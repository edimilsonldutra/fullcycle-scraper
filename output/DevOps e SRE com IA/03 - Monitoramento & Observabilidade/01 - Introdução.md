Módulo: DevOps e SRE com IA\
Aula: [Introdução](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18536)

## Resumo da aula



## Transcrição

00:00

Fala pessoal, voltamos aqui com o módulo 3 para a gente

00:04

Falar um pouco de monitoramento e observabilidade assistidos por AI.

00:10

Então a gente vai conseguir gerar alguns prompts aqui,

00:14

gerar alguns arquivos para a gente colocar dentro do nosso app. E além disso,

00:20

vamos fazer o uso de MCP

00:22

e algumas ferramentas de observabilidade para conectar.

00:28

Dentro da nossa interface de LLM e conseguir fazer

00:32

a observabilidade dos nossos serviços através do uso do LLM. Então,

00:39

no primeiro módulo, a gente fez a fundação ali,

00:41

a gente construiu alguns arquivos para subir os serviços localmente. No segundo,

00:47

a gente falou um pouquinho ali de CICD e segurança

00:50

para subir os arquivos através de uma esteira.

00:52

Os arquivos são os serviços através de uma esteira,

00:55

os arquivos que a gente criou do módulo 1.

00:57

E agora, no módulo 3, a gente vai falar um pouco de monitoramento.

01:02

Então, vamos conseguir monitorar onde tem essa aplicação,

01:06

onde ela está lenta, se ela está caindo,

01:08

quais endpoints estão com mais erros, qual é a latência e assim por diante.

01:13

Então, sem o monitoramento, a gente fica operando no escuro.

01:16

Com o monitoramento e observabilidade,

01:18

a gente consegue entender como que está acontecendo.

01:21

E, como já disse, vamos conseguir fazer isso com linguagem natural, tá bom?

01:26

Então, vamos cobrir três camadas aí nesse módulo.

01:30

A gente vai falar um pouco sobre SLI,

01:33

SLO e SLA, e o erro e erro budget,

01:36

e os quatro golden signals do SRE,

01:41

e depois a implementação com o OpenTelemetry e algumas consultas conversacionais, ok?

01:48

Passando aqui para o próximo slide,

01:49

a gente vai falar das ferramentas que a gente vai trabalhar nesse módulo. Beleza?

01:56

Antes da gente trabalhar aí nos conceitos,

01:58

vamos falar um pouquinho aqui. Uma que vocês já conhecem,

02:01

que é o Open Code Go, que eu venho falando aí desde o início das nossas aulas.

02:05

A gente já usou no módulo 1, já usou no módulo 2,

02:08

e agora a gente vai usar aqui no módulo 3 também,

02:10

para gerar os nossos artefatos com o LLM. Ok?

02:15

Vamos usar o LM Studio.

02:17

A gente já usou no módulo anterior para fazer algumas coisas.

02:20

Vamos continuar usando ele aqui para fazer algumas consultas,

02:24

algumas conversas com o LLM de maneira local.

02:26

Como eu já disse, se vocês tiverem conta OpenAI, outra conta da Anthropic, etc.,

02:33

podem se conectar através desse também.

02:35

Estou usando aqui um local para demonstrar para vocês.

02:41

Agora, mais uma ferramenta nova que a gente vai trabalhar aqui é o OpenMBI.

02:46

O Open Web UI vai ser a nossa interface para conversação via MCP.

02:52

Ao invés de a gente consultar usando o Open Code,

02:55

nós vamos ter uma interface agora no estilo ChatGPT,

02:59

onde a gente consegue conversar com os nossos serviços via linguagem natural,

03:04

ver quais os serviços que estão dentro do Kubernetes,

03:07

quais são os logs deles e assim por diante.

03:11

No lado da observabilidade tradicional.

03:15

Temos uma stack com OpenTelemetry, Collector, Prometheus,

03:19

Tempo, Loki e o Grafana. Ok?

03:23

O Grafana a gente vai ver os gráficos ali dos nossos serviços, etc.

03:26

No OTSDK a gente vai instrumentar a nossa aplicação.

03:29

Então a gente vai usar o OpenCollector para instrumentar.

03:33

O collector, que vai rodar através de um serviço, vai rotear os dados, ou seja,

03:37

ele vai pegar esses dados e vai

03:39

entregar nos três backends que armazenam as métricas,

03:44

os traces e os logs, respectivamente. Ou seja, as métricas vão ficar no Prometheus,

03:51

os traces vão ficar no Tempo e os logs no Loki.

03:56

O Grafana unifica tudo e coloca isso em dashboards onde a gente consegue ver.

04:02

Então a gente vai ter três backends,

04:04

a gente vai ter a instrumentação através do OpenTelemetry,

04:08

que vai mandar isso para um coletor OpenTelemetry,

04:11

o coletor OpenTelemetry vai mandar isso para o Prometheus,

04:14

para o Tempo e para o Loki, e o Grafana,

04:17

a gente vai conseguir visualizar isso tudo através de dashboards,

04:20

etc. Então vai funcionar mais ou menos assim.

04:23

E a observabilidade GI,

04:27

a gente vai usar um pouco de LengthFuse, tá bom?

04:32

O OpenMBY, que eu já falei anteriormente,

04:35

vai mandar os logs do que está

04:40

acontecendo com o nosso chat para o LingFuse.

04:43

Então, chamada de MCP,

04:46

os prompts gerados e assim por diante.

04:52

Vai ser tudo documentado dentro do LingFuse e a gente

04:55

vai conseguir rastrear isso de ponta a ponta.

04:58

E a infraestrutura a gente continua aí.

05:01

Com o Kubernetes local, com o K3D, e toda essa stack que eu falei de Prometheus,

05:06

Tempo, Loki, etc., a gente poderia também subir no K3D, se vocês quiserem,

05:11

fica um desafio aí para vocês, mas eu vou subir aqui no Docker Compose,

05:15

só para a gente ganhar um pouco de tempo aqui.

05:18

Então eu não vou instrumentar,

05:19

não vou criar pipelines para a gente instrumentar essa parte.

05:24

Eu vou subir em Docker Compose, mas fica o desafio para vocês,

05:28

se vocês quiserem subir dentro do cluster Kubernetes,

05:31

é super legal também e vocês podem testar o K3D internamente.

05:36

Nesse módulo a gente vai contar com três demos,

05:39

então a gente vai ter a demo para gerar a instrumentação do OpenTelemetry Hotel.

05:45

Beleza? A gente vai gerar um prompt e um código.

05:48

Ok? A gente vai gerar também dentro da nossa aplicação,

05:52

vamos gerar um workflow ali que vai fazer os testes

05:56

do OpenTelemetry quanto a gente subir na pipeline do nosso serviço.

06:01

Então a gente sobe a pipeline do serviço e ele vai

06:02

fazer alguns testes ali se o OpenTelemetry está de pé. Ok?

06:06

Teremos um troubleshoot conversacional com MCP mais linguagem natural, NL,

06:10

que está descrito ali, e uma observabilidade com LingFuseFilter,

06:14

que vai fazer o envio das informações para o LingFuse do Open Webinar.

06:20

Falei sistema errado aqui.

06:23

Então vamos lá. Começando aqui para a parte de SLI,

06:26

SLI e SLA, a gente vai falar de algumas definições aqui,

06:29

só para a gente fazer o alinhamento.

06:31

Por que esses três conceitos são a base de tudo que vamos falar nesse módulo?

06:35

O Google SRE... que fez as definições de SRE, etc.,

06:41

define três camadas que precisam estar claras na cabeça

06:44

de todo o profissional que mexe com SRE.

06:47

Primeiro é o SLI, que é o Service Level Indicator.

06:52

Imagine que o SLI é como uma medida bruta, um indicador quantitativo do serviço.

06:57

É o número que diz como as coisas estão. Então, basicamente,

07:02

por exemplo... A latência de resposta das nossas APIs,

07:07

a taxa de erro de 500 dela é o número

07:11

de request por segundo que o sistema consegue processar.

07:14

O SLI não julga, ele só mede.

07:19

É um termômetro para saber se essa

07:24

quantidade de erro versus a quantidade de...

07:27

de chamadas está ok. A gente consegue tirar o erro,

07:31

o erro limite disso aí. Ok? O SLO é o Service Level Objective.

07:39

Basicamente é o julgamento do SLI. Então ali é um objetivo. Por exemplo,

07:43

eu quero que a minha aplicação ela

07:45

tenha uma disponibilidade de mais que 99 ,95%.

07:51

Então o SLO é onde a gente vai definir qual que é a métrica,

07:57

a meta do time daquela aplicação ficar online,

08:01

ok? Então, a gente define isso no SLO, beleza? Então, basicamente,

08:07

se a disponibilidade

08:09

do SLI for 99%,

08:15

a gente não consegue bater o SLO.

08:17

Então, acaba que a gente perde a meta do mês, sei lá,

08:22

a gente pode definir por mês, por semana, por sei lá.

08:25

Acho que faz mais sentido por mês, né?

08:26

Então a gente pode definir por mês aí. Então a chave é,

08:30

o SLO é uma definição interna. Então o Steam está dizendo,

08:34

esse é o nosso padrão de qualidade.

08:36

Se violado, precisa de uma ação, ok?

08:39

Então o SLO vai definir o objetivo ali do Service Level,

08:43

beleza? E o SLO, que é para externo. Então é o Service Level Agreement.

08:50

É o contrato com o cliente. Se você tem um serviço,

08:53

que é disponibilizado para cliente,

08:55

você vai definir um SLA para ele e vai falar,

08:59

nossos serviços ficam uptime 99

09:03

,9 % das vezes do tempo.

09:07

Então, se acontecer alguma coisa, tem alguma penalidade,

09:10

algum crédito financeiro e assim por diante. Se vocês notarem,

09:14

se vocês dão uma pesquisada na AWS, a disponibilidade da AWS hoje é 99 ,99999%.

09:21

Então, a gente tem um SLA muito agressivo. Então, SLA interno, o objetivo interno,

09:27

vocês têm que manter esses serviços tanto tempo de pé, beleza?

09:32

E o SLA é para clientes, ok?

09:35

A gente vai definir que os serviços ficam esse determinado tempo de pé,

09:41

sem haver falhas, ok?

09:44

SLI médio, SLA é a meta e SLA é o contrato.

09:50

Contrato com os nossos clientes, tá?

09:52

A GNI vai ajudar a gente a definir e mapear o SLA e o SLA automaticamente,

09:56

ok? Como a gente está falando só de serviços internos aqui,

09:59

a gente não vai falar de SLA,

10:00

mas ele vai ajudar a gente a definir ambos aqui, beleza?

## Resumo IA

[RESUMO_IA]