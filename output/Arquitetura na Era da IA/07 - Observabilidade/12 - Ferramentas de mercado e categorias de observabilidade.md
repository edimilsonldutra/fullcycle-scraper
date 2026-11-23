Módulo: Arquitetura na Era da IA\
Aula: [Ferramentas de mercado e categorias de observabilidade](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18759)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem? Até aqui a gente trabalhou com uma ideia importante,

00:05

a nossa aplicação não deve ficar presa diretamente

00:07

a uma ferramenta específica de observabilidade.

00:11

A gente instrumentou utilizando o OpenTelemetry,

00:14

a gente conseguiu exportar via o OTLP

00:17

e a gente conseguiu mostrar o destino mudando,

00:21

quando a gente trabalhou entre o Jaeger e o Langfuse.

00:24

Agora, eu queria organizar melhor, vamos dizer, o mercado,

00:28

somente para você ter uma visão geral mesmo do que acontece.

00:33

Porque quando a gente fala de observabilidade para aplicações com IA,

00:36

existem várias ferramentas,

00:39

mas elas não estão todas resolvendo exatamente o mesmo problema.

00:44

Algumas são mais focadas em tracing tradicional,

00:47

outras são mais focadas em aplicações com LLM, outras fazem...

00:51

parte de plataformas grandes de APM e outras

00:55

ali vêm integradas ao próprio Cloud Provider.

00:58

Então, ao invés de a gente ficar decorando nomes,

01:01

eu acho que é melhor a gente pensar em

01:03

categorias e talvez isso acabe ajudando melhor.

01:06

Lembrando que eu estou categorizando aqui de uma forma como eu acho.

01:10

Vamos dizer como eu acredito, não existe uma documentação formal,

01:14

mas eu acho que fica meio que simples de você ter

01:17

um esqueminha para ficar mais tranquilo de você entender.

01:21

Então, não necessariamente eu preciso e eu quero que você concorde

01:25

comigo em 100% do que eu vou colocar. Beleza?

01:28

Então é o seguinte, a primeira categoria é a de ferramentas de tracing tradicional.

01:33

Aqui entram ferramentas como Jaeger,

01:35

Grafana Tempo, e elas são muito boas para visualizar traces, spans, latência,

01:43

fluxo entre serviços e dependências,

01:45

se você quer entender o caminho de uma requisição,

01:48

quanto tempo cada etapa levou e onde aconteceu um erro,

01:52

e esse tipo de ferramenta vai realmente ajudar muito.

01:55

O ponto é que elas não nasceram especificamente para LLMs,

01:59

então elas enxergam bem o tracing,

02:01

mas talvez não tragam por padrão uma experiência tão rica para prompts,

02:06

gerações, custo, tokens, avaliação de respostas e datasets.

02:11

Mesmo assim, são extremamente úteis,

02:13

principalmente quando a empresa já tem uma

02:15

stack de observabilidade mais tradicional.

02:17

A segunda categoria é a de ferramenta AI-first ou LLM-first.

02:24

Aqui entram LangFuse, Phoenix,

02:27

LangSmith e outras soluções focadas em aplicações com modelos de linguagem.

02:33

O LangFuse, por exemplo,

02:34

pode receber os traces via... OpenTelemetry,

02:38

e também oferece recursos específicos para LLM,

02:41

como token usage, cost tracking, prompt linking e scoring também.

02:47

O Phoenix é uma opção também open source bem forte nesse espaço.

02:53

A documentação dele posiciona traces como uma forma de capturar model calls,

02:59

retrieval tool e uso de lógicas customizadas,

03:03

além de aceitar traces via OpenTelemetry. E a gente tem, por exemplo,

03:09

a LangSmith, por outro lado.

03:11

Ela fica muito natural quando o projeto já usa LangChain.

03:16

Ele faz tracing, debugging, avaliação,

03:19

monitoramento de aplicações com LLM e a vantagem é

03:23

a integração do ecossistema do Land Chain. Quando eu estou falando isso,

03:27

eu estou falando também, por exemplo, do LandGraph.

03:29

A desvantagem arquitetural é o cuidado para

03:32

não confundir framework com estratégia de observabilidade.

03:37

A terceira categoria é o famoso APM corporativo.

03:43

Então, vamos dizer assim,

03:45

aí entram Datadog e New Relic, por exemplo.

03:48

A gente tem Splunk.

03:49

Essas ferramentas são fortes quando as empresas querem

03:53

olhar e ir junto com o resto do ambiente.

03:57

E aí eu estou falando da aplicação, da infraestrutura, do banco de dados, das APIs,

04:03

das filas, dos logs, dos traits e agora também as chamadas de LLM.

04:07

O Datadog, por exemplo, ele tem recurso de LLM observability para custo estimado,

04:14

token usage, breakdown por provider, modelo e prompt version também.

04:19

O New Relic também posiciona AI Monitoring como uma forma de observar performance, custo,

04:26

qualidade em aplicações com IA,

04:28

incluindo suporte a frameworks como o próprio LangChain.

04:32

E a quarta categoria é a dos Cloud Providers. Por exemplo, a AWS,

04:38

o Google Cloud e a Azure estão trazendo ali

04:41

observabilidade de IA para dentro das suas próprias plataformas.

04:45

A AWS tem o GNI Observability no CloudWatch, um dashboard de consumo de tokens,

04:51

logs e traces, inclusive com suporte a frameworks também,

04:55

como o LangChain e o LangGraph.

04:57

O Google Cloud também documenta a instrumentação de

05:02

aplicações generativas com OpenTelemetry e também com exemplos,

05:07

com o LangChain e também o LangGraph,

05:09

enviando telemetria para o Google Cloud Observability.

05:13

A gente também tem o Azure Foundry,

05:15

que também utiliza OpenTelemetry e as... Application Insights,

05:20

para observar os agentes com tracings,

05:22

telemetria de produção também. Então, a decisão arquitetural,

05:26

ela não é simplesmente escolher a ferramenta mais famosa.

05:29

A pergunta correta é, qual o tipo de visibilidade que eu preciso?

05:33

Se eu quero tracing abertos e simples, o Jaeger já pode ser o suficiente.

05:38

Se eu quero observar uma aplicação LLM com prompt, token, custo,

05:42

traces, etc., o Langfuse, o Phoenix ou o próprio LangSmith,

05:46

eles podem fazer mais sentido.

05:48

Agora, se a minha empresa já usa um Datadog, um New Relic da vida,

05:51

talvez seja melhor integrar e ir dentro da stack que o time já está operando.

05:57

Então, se eu estou também profundamente dentro de uma AWS,

06:01

Google, Azure e etc., utilizando as ferramentas dele,

06:04

talvez já valha a pena utilizar e

06:07

aproveitar esses recursos nativos de observabilidade. E aí,

06:11

isso volta para o ponto principal desse módulo.

06:13

OpenTelemetry ajuda a manter a instrumentação mais aberta,

06:17

a aplicação emite a telemetria de forma padronizada e

06:21

O back-end pode ser escolhido conforme a maturidade,

06:24

custo, governança e o ecossistema da empresa. Então, no nosso curso,

06:29

a gente usou o Langfuse e o Jaeger porque isso mostra dois mundos.

06:32

Uma ferramenta mais voltada para aplicações com IA

06:35

e uma ferramenta mais tradicional de tracing.

06:37

Mas, numa arquitetura real... A escolha precisa considerar o que o time já usa,

06:42

quais dados podem sair da aplicação,

06:44

quanto tempo os tracings vão ficar guardados e etc.

06:47

Além de toda a parte de governança, custos,

06:50

contratos e tudo mais. Então a mensagem principal dessa aula é...

06:54

Ferramenta de observabilidade não é apenas uma escolha técnica,

06:57

é uma decisão arquitetural,

06:59

também é uma decisão de negócio e vai definir

07:02

muito como o time investiga os problemas,

07:04

acompanha o custo,

07:06

entende o comportamento e opera as aplicações com IA ali em produção.

## Resumo IA

[RESUMO_IA]