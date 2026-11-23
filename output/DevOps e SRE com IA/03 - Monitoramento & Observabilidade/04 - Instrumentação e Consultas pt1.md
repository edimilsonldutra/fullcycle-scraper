Módulo: DevOps e SRE com IA\
Aula: [Instrumentação e Consultas pt1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18497)

## Resumo da aula



## Transcrição

00:01

Vamos lá, pessoal. Estou de volta aí.

00:03

Vamos continuar o nosso bloco aqui, o nosso próximo bloco,

00:07

A implementação de consultas e do nosso OpenTelemetry aqui para a nossa aplicação,

00:11

que a gente está construindo desde o primeiro módulo. Fechou?

00:14

Então, vamos continuar aqui.

00:17

Primeira parte, a gente vai falar aqui um pouco da instrumentação via OpenTelemetry.

00:23

Então, basicamente, aplicação sem instrumentação nenhuma.

00:27

Hoje a gente não tem nada de instrumentação lá,

00:29

a gente não vai conseguir medir nada.

00:31

Então a gente vai adicionar os traces e métricas via prompt.

00:35

Então a gente vai criar isso aqui, tá bom?

00:39

Então o que a gente vai gerar? Traces de spans de cada endpoint.

00:45

A gente vai gerar as métricas que têm Instagram,

00:49

lá tem esse counted request e um exporter de OTLP, de collector,

00:54

que vai para o tempo e prometeu-se aqui. Legal? Então, para rodar,

00:59

a gente vai enviar o request, ver os spans chegando no coletor. Beleza?

01:06

Então, aqui a gente tem só mais ou menos um comando que vai listar nosso prompt aqui.

01:10

Eu vou pegar e mostrar com mais detalhes para vocês aqui.

01:13

E a gente vai conseguir ver isso acontecendo aqui em tempo real. Ok?

01:20

Vamos lá. Vamos começar a fazer.

01:23

Demo 1, gerando o código via OpenTelemetry aqui.

01:26

A nossa aplicação,

01:27

a TeamFast API hoje não tem nenhuma instrumentação

01:30

para a gente conseguir fazer o monitoramento.

01:32

A gente vai gerar o código do OpenTelemetry via prompt e validar os traces no tempo.

01:37

Legal? Então a gente vai usar um prompt estruturado do que a gente tem aqui,

01:43

que eu vou mostrar para vocês, que vai gerar via OpenCode esse arquivo,

01:49

que é o telemetry.py. Rodar o app.

01:54

A gente vai subir esse app para dentro do nosso pipeline.

02:00

Ele vai fazer o deploy.

02:02

Vai começar a comunicar com o nosso host collector. E o tempo, via Docker Compose,

02:09

vai receber todas essas... Vai receber todas essas...

02:14

Como é que eu vou explicar? Todas essas logs. Ok?

02:18

Enviar o request e verificar lá no tempo e na UI como que está ocorrendo isso. Ok?

02:25

Nosso namespace aqui, OpenTelemetry, está depreciado,

02:29

vou usar um OpenTelemetry Instrumentation.

02:31

Beleza? Esse aqui é só um adendo aqui que a gente tem.

02:35

Depois disso, vamos usar um curve para fazer a validação do nosso serviço aqui.

02:39

Legal? Então vamos lá. Vamos na primeira parte aqui. Só um ponto.

02:45

Antes da gente

02:47

gerar toda essa stack,

02:53

que a gente está falando de telemetria aqui,

02:55

nós vamos primeiro gerar o Docker Compose aqui da nossa stack de observabilidade, ok?

03:02

Então agora vamos criar aqui o nosso stack de

03:07

observabilidade antes de criar a instrumentação dentro do nosso aplicativo,

03:13

instrumentação com OpenTelemetry, ok?

03:16

Só um ponto, eu comentei que a gente iria gerar alguns Docker Compose,

03:21

porém a gente vai gerar...

03:23

manifesto Kubernetes para subir a aplicação dentro do nosso K3d,

03:27

dentro do nosso Kubernetes, que já está rodando,

03:29

Ao invés de criar Docker Compose e subir através do Docker, então,

03:33

a primeira etapa que eu fiz para a gente gerar

03:35

esses manifestos foi basicamente criar um repositório dedicado para observability.

03:42

Eu não vou colocar ele dentro da aplicação,

03:44

vou criar um repositório aqui dedicado e também não vou subir dentro do Git.

03:48

A gente vai criar um script .sh aqui que vai fazer a

03:51

subida para a gente de toda a stack de observabilidade.

03:54

E quem vai gerar essa stack para a gente é a própria generatividade.

03:58

Então a gente vem aqui dentro de documentos,

04:00

observability, que foi a pastinha que eu criei. Vamos colocar um open code aqui.

04:06

Eu tenho um prompt aqui que eu já gerei. Eu vou disponibilizar para vocês aí também.

04:11

E esse prompt é o prompt que orienta como que vai ser gerada essa stack.

04:16

Vou pegar o prompt aqui. Deixa eu copiar ele.

04:20

E vou colar aqui na tela para a gente dar uma lida de como que vai funcionar. Ok? Copiando.

04:28

E aqui o prompt que a gente vai usar para gerar a nossa stack.

04:32

Deixa eu dar um zoom aqui para ficar mais visível.

04:35

Fechar esse aqui que não precisamos. E aqui a gente tem o nosso prompt.

04:40

Primeiro, vamos gerar os manifestos Kubernetes aqui,

04:43

que é um stack completo de observabilidade,

04:45

organizado em dois namespaces.

04:47

Os manifestos consistem em arquitetura com o módulo final.

04:54

Então aqui é só uma documentação da aplicação. Arquitetura em dois namespaces,

04:58

então a gente vai ter o namespace observability,

05:00

e o namespace OpenMBI, onde a gente vai colocar as partes de Generative AI,

05:04

e lá dentro a gente vai ter o OpenMBI,

05:06

MCPO, que faz parte aqui do OpenMBI, o LangFuse,

05:09

para a observabilidade do LLM, e o LangFuseDB,

05:12

para suportar o LangFuse aqui. E aqui é o stack de observabilidade,

05:16

Prometheus, Grafana, Tempo, Loki,

05:18

e Hotel Collector, que é o hub central ali.

05:21

Aqui mais alguns detalhes, o prompt vai estar disponível para vocês,

05:24

vocês podem pegar e ler.

05:26

Mas basicamente é uma descrição exata do que a gente quer fazer o deploy,

05:33

do mesmo jeito que a gente vem fazendo nas outras aulas. Então vamos copiar,

05:36

a gente já está com o open code aberto aqui,

05:38

vamos pedir para ele gerar essa stack de observabilidade para a gente.

05:43

Ele vai demorar um pouquinho para gerar,

05:45

porque ele vai rodar aqui as partes de LLM, pensamento, etc.

05:48

E assim que ele voltar, eu já faço,

05:52

assim que ele terminar de gerar, eu já volto aqui com vocês.

05:56

Ok, terminou de gerar aqui, voltamos aqui.

05:59

Aqui os arquivos que ele gerou, os manifestos Kubernetes.

06:03

E a gente tem aqui dentro do nosso repositório, vamos abrir aqui.

06:08

A gente tem vários arquivos aqui de

06:11

Manifest Kubernetes e um arquivo de SH,

06:15

que é o nosso deploy aqui.

06:17

Legal? Então a gente vai fazer algumas verificações

06:20

antes de fazer a aplicação e aqui

06:23

vai aplicar tudo que vai mostrar para a gente

06:25

as URLs finais aqui dos nossos serviços.

06:29

Então vamos aplicar o script

06:33

aqui agora para subir a estrutura. Esse aqui é o prompt, deixa eu fechar ele.

06:38

Vamos aplicar o script aqui agora para subir a estrutura do nosso observabilidade.

06:51

fazer a execução desse deploy .sh.

06:53

Se a gente vier aqui no nosso K9S,

06:57

onde a gente consegue ver a nossa infraestrutura que está dentro do Kubernetes,

07:00

a gente consegue ver que só tem aquele que a gente criou lá nas primeiras aulas,

07:04

que é o demo -app -mba, e está rodando o nosso demo -app aqui.

07:08

Se a gente vier em namespace, a gente não tem mais nenhum namespace,

07:11

vai ser criado dois, o open -web -y e o observability,

07:16

que são os dois namespaces que a gente vai criar. Então, basicamente, a gente vai dar um

07:20

ponto barra referência

07:23

k8s deploy .sh.

07:28

Esse deploy .sh vai fazer todo o deploy para a gente lá dentro do Kubernetes.

07:34

Fazer as importações das imagens e assim por diante.

07:38

Então, ele está verificando aqui se está tudo de pé.

07:41

Vocês podem notar aqui que a gente já tem dois novos namespaces,

07:44

um de observability.

07:46

que a gente tem aqui o Grafana, Lock, AutoCollector, Prometheus e o Tempo.

07:51

E a gente vai ter aqui um OpenWebUI, onde a gente tem Langfuse,

07:57

LangfuseDB, MCPO, com alguns serviços aqui rodando.

08:01

E a gente tem aqui o OpenWebUI,

08:04

com o serviço do OpenWebUI inicializando aqui.

08:09

Voltando aqui, ele já conseguiu validar tudo para a gente aqui.

08:13

No final ele tem algumas instruções para a gente conseguir

08:15

mapear a entrada nos serviços

08:22

dentro da nossa máquina local.

08:24

Legal? Então ele só dá essas instruções aqui para

08:26

colocar lá dentro do nosso ETC Hosts aí.

08:30

Beleza? Então vamos tentar aqui entrar no Grafana.

08:34

Vamos dar o Open aqui e a gente já tem o Grafana aqui pronto para uso. Ok?

08:40

Vamos tentar entrar aqui no OpenRBY, que é o que tem interface.

08:45

E a gente já tem o OpenRBY aqui pronto para uso também.

08:49

Tudo deployado lá dentro do nosso cluster Kubernetes.

08:55

Fechou? Então agora a gente vai fazer a geração.

08:59

A gente já tem toda a infraestrutura aqui de observabilidade criada.

09:05

Então agora a gente vai fazer a criação do nosso...

09:10

do nosso... da nossa telemetria dentro do app. Ok?

09:15

Vamos lá. A gente está aqui na branch main. Legal.

09:19

Vamos aqui dentro do nosso terminal.

09:23

A gente está aqui dentro do nosso repositório do app API.

09:26

Vamos aqui dar um open code.

09:31

Fechou? Temos um prompt aqui já pronto, né?

09:34

Como tudo que a gente está gerando aqui, a gente está gerando com um prompt.

09:39

Então a gente já tem um prompt aqui pronto já de instrumentação,

09:42

vou copiar ele aqui, um minutinho,

09:46

ok, prompt aqui copiado, se a gente vier aqui no nosso terminal,

09:53

esse aqui é o observability,

09:54

vamos aqui no terminal, terminal não né, no VS Code do nosso app,

09:58

e aqui a gente já tem todas as regras

10:02

De criação da nossa instrumentação para a gente conseguir ver.

10:09

Esses logs caindo lá dentro dos nossos serviços de observabilidade. Ok?

10:14

Minimizei aqui. Deixa eu dar um view. Vou de Apric.

10:19

Aqui a gente consegue ver melhor. Vamos criar cinco arquivos, né?

10:22

Um app telemetry. A gente vai criar também alguns testes desse telemetry.

10:27

A gente vai criar, fazer alguns ajustes na main.

10:31

Vamos criar um validate author aqui,

10:33

que é uma nova etapa do nosso workflow que vai fazer o deploy,

10:36

que ele vai validar se o OpenTelemetry está de pé.

10:39

E mais algumas coisinhas aqui. Vamos fazer um lint do código, etc.

10:44

Beleza? Então, vamos fazer a criação dessa stack aqui dentro do nosso OpenCode.

10:51

Copiado aqui o prompt colado.

10:53

Vamos esperar gerar. Assim que gerar,

10:56

eu já volto para a gente dar continuidade. Vou dar um pause aqui.

11:00

para a gente conseguir ganhar tempo aí nas nossas aulas.

11:07

Então, pessoal, voltamos aqui.

11:11

Criamos os arquivos, né? Criamos um app Telemetry Key,

11:15

onde tem todas as configurações para telemetria da nossa aplicação App API.

11:19

Fizemos algumas atualizações no main para fazer a

11:22

atualização para envio da telemetria para o OpenTelemetry, ok?

11:30

Foi adicionado aqui os requirements,

11:33

o Dockerfile foi ajustado com as variáveis de ambiente.

11:38

Criamos aqui um arquivo Python de teste e um YAML aqui,

11:44

que é o nosso fluxo para fazer o teste do OpenTelemetry. Então,

11:47

se a gente vier aqui no nosso projeto, a gente tem o ValidateAuto aqui criado,

11:53

que o Job lá criou para a gente, o prompt.

11:59

A gente tem o main criado, a gente tem um arquivo aqui .main criado,

12:03

ajustado na verdade, que já existia. O arquivo telemetry foi criado aqui, ok?

12:09

E a gente tem aqui uma parte de teste, que é o teste de alter instrumentation,

12:13

ok? Que vai fazer os testes iniciais ali do funcionamento do OpenTelemetry,

12:18

legal? Então agora vamos adicionar esses caras aqui na nossa main,

12:24

na nossa branch principal.

12:26

E vamos fazer o deploy dele aqui no ambiente,

12:29

no nosso ambiente do Kubernetes e

12:32

ver essas telemetrias chegando lá no OpenTelemetry,

12:38

através do Grafana a gente vai conseguir enxergar esses logs chegando lá.

12:43

Por enquanto a gente vai ter logs chegando através do Grafana.

12:47

Então, como antes, a gente vai vir aqui e dar um git add ponto, git commit "-n",

12:55

Adicionando observabilidade no serviço de app API. Git.

13:02

Checkout. Faltou checkout, né? Checkout. Adicionando. Adicionando. Observabilidade.

13:12

App API. Ok?

13:18

Adicionando. Ok. Certinho. Aqui já está feito o git add.

13:24

O checkout também. Agora a gente vai dar um git push.

13:28

Vamos fazer um ajuste aqui. Git push, origem e o nome da branch nossa.

## Resumo IA

[RESUMO_IA]