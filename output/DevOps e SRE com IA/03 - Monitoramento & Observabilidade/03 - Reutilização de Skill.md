Módulo: DevOps e SRE com IA\
Aula: [Reutilização de Skill](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18532)

## Resumo da aula



## Transcrição

00:00

Então, vamos para o próximo aqui,

00:02

que é a nossa skill que a gente criou lá no módulo 1.

00:07

Então, basicamente, a gente vai reutilizar a skill do módulo 1,

00:11

que a gente fez a criação dela, com mapeamento de SLI e SLO. E essa skill,

00:17

ela recebe o input da descrição textual do serviço. Por exemplo, REST API.

00:24

com endpoint CRUD, database Postgres SQL, com cache Redis e assim por diante.

00:29

E ela vai retornar o SLI

00:32

organizado com os four golden signals,

00:37

com latência, tráfego,

00:39

erros e saturação. O SLO com os targets porcentuais de conceitos específicos,

00:46

como o 99,9% de disponibilidade,

00:50

latência de P99 de menos de 500 milissegundos.

00:54

Então o cálculo do erro budget mensal e diário de cada SLO,

00:58

a gente vai ter isso também,

01:00

e os troubleshooting de alerta recomendado,

01:04

que vai falar para a gente quais são os alertas recomendados para essa aplicação. Então aqui,

01:14

Vamos tentar aqui usar a nossa skill

01:20

que a gente criou lá no módulo 1.

01:23

Só dar um barra skills, já está criado aqui. E a gente tem um SLI, SLI mapping aqui.

01:29

Vamos dar um enter.

01:31

Basicamente, ele vai definir que já tem toda a descrição que a

01:34

gente já tinha criado do serviço e assim por diante.

01:38

Legal? Deixa ele gerar aqui, que eu vou lá na nossa pastinha.

01:42

Dos nossos serviços.

01:45

Vamos achar aqui a pastinha do serviço. Está aqui. Legal?

01:52

Ele está aqui dentro de... AppNow.

01:57

Agent GitHub. Deixa eu voltar aqui e ver onde ele está gerando.

02:03

Está gerando ainda. Por isso que não apareceu lá.

02:07

Vou dar um pause aqui. Assim que terminar de gerar, eu já volto com vocês.

02:11

Estou de volta. Terminou de gerar aqui.

02:15

Então, a gente tem aqui exatamente todo o planejamento de erro budget gerado. Então,

02:19

o que levava bastante tempo antes, a gente consegue fazer agora em

02:25

minutos. Que demorou alguns minutos aqui. Tá bom? Então, vamos lá.

02:30

Minutos por mês. A gente tem 43.830 minutos por mês.

02:36

De 30,42 dias vezes minuto por mês aqui. Então,

02:41

a gente tem 86.400 segundos por dia.

02:44

Então, o nosso budget mensal aqui é basicamente 1, que vai representar o 100%,

02:50

menos 0,9999. Então, a gente vezes os 43.830 minutos.

02:57

Então, a gente tem no final aqui mais ou menos 43 minutos de budget mensal.

03:04

Budget diário, 1 minuto e 26 segundos, que a gente pode ficar indisponível.

03:09

Então, com esse prompt da skill 1,

03:11

a gente consegue definir exatamente os pontos aqui dos erros de budget.

03:17

Legal? E definir todas as partes aqui de saturação,

03:21

de tráfego, etc. Como vocês têm um prompt,

03:25

eu não vou passar um por um aqui, mas ele serve para a gente.

03:28

fazer isso. Já demonstrei isso no módulo 1,

03:30

só estou demonstrando de novo aqui que ele vai funcionar e você

03:33

pode reutilizar para vários outros serviços que você tem no seu ambiente.

03:40

Legal? Então, voltando aqui,

03:43

a gente consegue fazer essa geração de maneira mais fácil,

03:47

Que demorava antes bastante tempo. A gente consegue usar a nossa AI para fazer isso.

03:55

Continuando, a gente vai falar aqui um pouco dos

03:58

For Golden Signals SLI e a gente chega aqui

04:01

Finalmente na stack que a

04:03

Gente vai fazer nesse módulo,

04:08

Ok? Então a nossa stack acompanhando aqui o

04:11

Diagrama, a gente vai começar aqui pela latência, tráfego,

04:17

Erros e saturação, legal? O que a gente vai ter aqui embaixo aqui?

04:21

Aqui são nossos Golden Signals, a gente vai ter tudo

04:25

Isso aqui que vai se derivar do OpenTelemetry,

04:28

O nosso app vai mandar tudo para o Hotel Collector. Através do Hotel .tk,

04:33

Ele vai mandar tudo para o OpenTelemetry. Entenda que Hotel é OpenTelemetry,

04:37

Tá? Só para ficar claro aí. Então,

04:39

O Hotel Collector aqui vai receber tudo e

04:42

Vai mandar essas métricas para o Prometheus,

04:44

Que vai trabalhar com as métricas,

04:46

Para o Tempo, que vai trabalhar com os traces,

04:48

E para o Loki, que vai trabalhar com os logs.

04:51

Através dessas três ferramentas, a gente consegue extrair.

04:55

Com AI, a parte aqui do For Golden Signals, ok?

05:00

Aqui tem uma representação do Grafana,

05:02

Que vai consumir todas essas informações, e o LangFuse,

05:07

Que aqui acabou que ficou um pouco errado, mas a diferença é,

05:11

O OpenMBI vai mandar os prompts de tudo que ocorrer para o LangFuse, tá?

05:17

Ele só está na camada aqui mesmo do Grafana,

05:19

Porque ele é uma camada de observabilidade.

05:22

Mas quem manda para ele as informações é o OpenMBI.

05:26

Então a gente vai ter aqui alguns MCPs, então a gente vai ter um Prometheus MCP,

05:31

Um K8S MCP, onde a gente consegue tirar algumas informações também,

05:36

E a gente vai ter também o Loki MCP, que ficou oculto aqui,

05:40

Mas a gente vai ter o Loki MCP, que vai se conectar aqui no OpenMBI, tá bom?

05:45

Então a gente vai construir todas essas partes,

05:47

Desde o app aqui, onde a gente vai criar através de um prompt,

05:51

Eu já tenho o prompt pronto aqui, vou mostrar para vocês,

05:54

Que a gente vai criar aqui a stack do OpenTelemetry,

05:58

Ok? A gente vai criar aqui o HotelCollector,

06:02

A gente vai subir uma infraestrutura local para criar ele.

06:05

O Prometheus, o Tempo, o Loki, o Langfuse, o Grafana,

06:08

O OpenMBI e os MCPs também vão subir todos nessa stack que eu tenho aqui.

06:15

Basicamente, é um Docker Compose que eu vou disponibilizar para você.

06:19

A gente tem um prompt aqui para gerar esse Docker Compose,

06:21

Porém, eu vou disponibilizar ele completo para vocês também

06:24

Fazerem uns testes aí e subir isso.

06:26

Legal? Então, nesse primeiro momento aqui, a gente falou um pouco da teoria.

06:32

A gente viu uns conceitos aqui de SLI, de SLO e SLA, ok?

06:39

Do Golden Signals, erro budget, a gente viu aqui um pouco falando deles,

06:43

E da nossa stack de observabilidade que a gente vai montar nos próximos slides aí,

06:50

Nas próximas demos, legal? Então, qual que é o próximo bloco?

06:54

Instrumentação e consultas. O que a gente vai fazer?

06:57

A gente vai gerar o código do Otel via prompt.

07:00

e validar os tracers,

07:02

e vai conseguir fazer a detecção de anomalia com linguagem natural,

07:07

Natural Language,

07:08

que é o NL, que vai fazer umas queries através de MCP dentro dos nossos serviços,

07:12

ok? Então a gente, nós nos vemos no próximo bloco aí,

07:17

onde a gente vai falar dessas stacks aí e dessas atividades.

07:22

Obrigado pessoal, abraço.

## Resumo IA

[RESUMO_IA]