Módulo: DevOps e SRE com IA\
Aula: [Instrumentação e Consultas pt3](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18533)

## Resumo da aula



## Transcrição

00:01

Vou fazer o deploy lá, vocês já cansaram de ver essa parte?

00:05

Então, assim que tiver no jeito, mesmo procedimento,

00:09

a gente vai fazer o pull request.

00:11

Então, assim que tiver no jeito, a imagem pronta,

00:13

eu volto aqui para mostrar para vocês que a gente agora consegue

00:17

chamar o serviço através de uma URL por causa do Ingress,

00:20

tá? Essa é uma novidade que eu estou trazendo aqui também para essa aula.

00:23

Eu não tinha falado na outra aula porque a gente estava chamando direto.

00:27

o nosso container ali através do service.

00:30

Mas a partir do momento que a gente colocou mais serviços,

00:33

começou a fazer sentido a gente dar nome para esses serviços através do Ingress,

00:37

para a gente conseguir visualizar certinho o que a gente está chamando, entendeu?

00:41

Então tinha faltado o Ingress aqui para o nosso app API e eu acabei de criá-lo.

00:46

Combinado? Então vamos lá, vou fazer aqui o merge e já volto, pessoal.

00:52

Ok, pessoal, deploy feito aqui.

00:54

Vocês podem ver que nesse meio tempo até a minha tela aqui mudou de tema.

00:58

Já foi para o tema escuro aqui.

01:01

Virou o horário, né? Foi para o tema escuro.

01:04

Então, não é que o deploy demorou muito, tá, gente?

01:06

Porque o horário que eu estou fazendo mudou, tá? Então o deploy foi rapidinho,

01:09

2 minutos e 4 segundos aqui.

01:11

E agora a gente já tem um serviço novo rodando aqui dentro.

01:16

Ok? O serviço já está rodando aqui. A gente já tem o health check sendo feito. Ok?

01:23

E lá dentro do Grafana, que a gente tinha visto aquela hora,

01:27

vamos explorar aqui um pouquinho o Grafana.

01:30

Aqui a gente tem a parte aqui do Health Check, ok?

01:34

E aqui dentro do Search, a gente pode fazer aqui um Name, Spam Name.

01:41

Esse Spam Name,

01:42

a gente pode selecionar qual que é o endpoint

01:44

que a gente quer ver aqui sendo enviado.

01:49

Então vamos selecionar esse aqui, que é o do teste que a gente tem lá no slide.

01:52

Que é esse API v1 items aqui. E dar um refresh.

01:56

Ok. Feito isso, ele está pegando o limite 20 aqui. E o span limit 3.

02:01

Tá bom? Então vamos fazer aqui uma chamada.

02:08

Através lá do nosso curl, né? Vamos aqui no curl.

02:12

Cadê? Cadê? Perdi.

02:14

Achei. Não, não é esse não. Aqui.

02:17

Então a gente já tem o curl montadinho aqui. Agora,

02:19

como a gente criou o Ingress lá com aquele nome,

02:22

a gente consegue fazer a chamada aqui através do Curlset.

02:25

E aqui é o retorno do JSON que a gente tem.

02:27

A gente fez um GET na API de itens e

02:31

ele retornou a lista de itens para mim vazia. Tendo isso,

02:37

a gente consegue olhar aqui dentro do Grafana que

02:40

ele vai trazer as informações aqui para mim. Ele aqui embaixo.

02:45

Então, basicamente, o que aconteceu aqui? Fiz a chamada.

02:49

Nossos endpoints estão instrumentados pelo OpenTelemetry.

02:52

O OpenTelemetry está conectado no tempo e o tempo está recebendo

02:57

todos esses tracers aqui que estão acontecendo lá dentro do pod.

03:03

Então, se vocês entrarem ali no pod, vou entrar no meu pod aqui agora.

03:08

Se vocês entrarem no pod agora, vocês vão ver que um deles...

03:13

Um deles recebeu um getItem.

03:15

E esse getItem vai ser refletido através do OpenTelemetry lá para o nosso dashboard.

03:21

Nosso dashboard não, desculpa, para o nosso Grafana. Fui longe no dashboard agora.

03:24

Para o nosso Grafana.

03:26

E com isso você consegue criar aqui quando foi mais usado, etc.

03:30

A gente consegue definir isso através de dashboards aqui no Grafana.

03:34

Tem um addDashboard aqui.

03:37

Então, vamos abrir aqui.

03:40

Ele deu problema. Vamos abrir aqui.

03:45

Add dashboard. Open dashboards.

03:48

Então a gente consegue colocar aqui um dashboard para

03:51

a gente acompanhar as chamadas da API aqui dentro.

03:55

Legal? Isso é só um exemplo do que a gente pode fazer.

03:58

Podemos criar gráficos com a quantidade de chamadas,

04:00

quantidade por endpoint e assim por diante.

04:03

Então assim a gente conseguiu instrumentar a parte de tracings aí do nosso serviço. Ok?

04:11

Então, voltando aqui para o slide, detecção de anomalia aqui com linguagem natural.

04:18

Então, a gente subiu o nosso serviço e agora a

04:21

gente quer saber como que

04:25

a gente pode descobrir a latência,

04:29

se está alta, se está baixa, se está dando problema, etc.

04:32

Então, a gente tem aqui o uso de Datadog, que é uma ferramenta paga.

04:36

A gente tem uma alternativa aqui para o open source,

04:39

que a gente pode usar nosso próprio pod.

04:41

A gente tem um Grafana LLM plugin,

04:44

a gente pode usar dentro do próprio Grafana um LLM plugin para isso.

04:47

E o Honey, como aqui é um query assistente, que faz perguntas em linguagem natural,

04:52

em query estruturadas, e mostra endpoints aqui no heat map,

04:55

que a gente consegue fazer também com a nossa

04:57

stack open source que a gente está trabalhando. Tá bom? Então,

05:00

sempre valide a explicação da AI, tá? Antes de fazer, então, se você pede,

05:05

por que meu serviço está mais lento?

05:07

Por que ele está fazendo isso? Por que ele está fazendo aquilo?

05:09

Então, valide o retorno da AI, porque...

05:15

Como eu sempre digo aí dentro do começo,

05:18

a AI vai te dar as informações, porém é bom você validar.

05:22

É sempre bom você validar de onde as informações estão vindo,

05:26

se estão ok e assim por diante. Combinado, pessoal?

05:31

Então, consultas conversacionais com linguagem natural query.

05:35

Então, pergunte em português.

05:37

Obtenha os dados do Prometheus ou Loki e assim por diante.

05:40

Qual a latência de P99 do serviço EPI nos últimos 30 minutos? Então a gente consegue,

05:46

através dos MCPs que a gente vai criar na nossa próxima etapa,

05:49

fazer essas perguntas.

05:51

Ele vai conseguir montar algumas queries dentro

05:55

do Prometheus para a gente conseguir puxar isso.

05:59

Mostre os erros 500 da última hora e assim por diante.

06:03

Então a regra é sempre validar a query antes de confiar no resultado.

06:10

Validar a query que gerou antes de confiar no resultado gerado pela AI.

06:13

E pode inventar.

06:14

Se ela não conseguir fazer a query e retornar alguma coisa sem pena na cabeça,

06:18

ela pode ter problemas para a parte de responder.

06:24

Então, ela pode inventar essa parte aí. Ok?

06:29

Então, o que a gente conseguiu fazer nessa atividade aqui?

06:32

A gente criou um Open Terminal de Waypoint lá no começo da nossa instrumentação.

06:38

Fizemos a demo 1, que a gente gerou um código hotel.

06:42

OpenTelemetry e validamos no tempo que os caras estão chegando lá,

06:46

os traces. E a consulta de linguagem natural.

06:50

A gente consegue usar linguagem natural para fazer um PromQL

06:54

e linguagem natural para o LogQL para validação.

06:57

E a gente, na próxima etapa,

07:00

vamos usar MCP e Legfuse para fazer o rastreamento dessas coisas todas.

07:06

Com MCP, a gente vai criar braços para a nossa AI. Basicamente,

07:10

o MCP dá a capacidade da EA ir buscar algumas coisas em algum lugar,

07:14

de forma que ela, tipo assim, ah, eu quero fazer a busca de tal coisa.

07:18

Quando ela sentir necessidade de precisar disso,

07:20

ela vai conseguir buscar essas coisas internamente com os MCPs que você definiu.

07:26

E o LengFuse, a gente vai conseguir ver a observabilidade disso.

07:30

Quais foram as tools que foram chamadas.

07:32

Quais foram as tools que retornaram alguma coisa e etc.

07:38

A gente consegue ver essa observabilidade completa dentro do nosso LengFuse.

07:43

E a chamada de LLM e assim por diante.

07:46

Então é isso, pessoal,

07:47

nos vemos aí no próximo bloco para a gente falar

07:50

um pouco de NCP e observabilidade de LLM com LengFuse.

## Resumo IA

[RESUMO_IA]