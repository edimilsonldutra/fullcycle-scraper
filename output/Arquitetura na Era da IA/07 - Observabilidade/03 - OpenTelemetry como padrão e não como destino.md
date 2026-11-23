Módulo: Arquitetura na Era da IA\
Aula: [OpenTelemetry como padrão e não como destino](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18750)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente alinhou os conceitos de logs, métricas,

00:06

traces, spam e eventos. A gente viu que esses conceitos não nasceram com IA,

00:10

mas que em aplicações com IA eles passaram a carregar informações totalmente novas,

00:15

como modelo usado, tokens, custo, contexto, ferramentas e tudo mais.

00:20

Agora, a gente vai falar sobre OpenTelemetry.

00:23

E a primeira coisa importante é entender o que o OpenTelemetry não é.

00:28

O OpenTelemetry não é... uma tela de um dashboard, ele não é um Datadog,

00:34

ele não é um New Relic, ele não é um Langfuse. Na realidade,

00:39

ele não é a ferramenta final onde você

00:43

necessariamente vai entrar para investigar uma resposta.

00:47

O OpenTelemetry é um padrão e um conjunto de ferramentas para instrumentar,

00:52

coletar e exportar... Então, em outras palavras,

00:56

ele ajuda a sua aplicação a produzir dados

00:59

de observabilidade num formato mais padronizado.

01:03

E por que isso é importante? Porque sem um padrão, cada biblioteca, cada framework,

01:08

cada provider e cada time acabam registrando telemetria de um jeito diferente.

01:14

Um time chama de model,

01:16

o outro time chama de LLM model,

01:18

o outro chama de deployment, o outro chama de engine.

01:21

Então, um time registra um token, por exemplo, sei lá,

01:24

com input tokens, o outro como prompt tokens.

01:27

Então, parece detalhe isso aí no começo, mas quando a aplicação cresce,

01:31

fica muito difícil de fazer a correlação de tudo isso,

01:34

tá? Então, o OpenTelemetry, ele tenta organizar essa história.

01:38

A ideia básica é, a aplicação gera traces,

01:41

métricas e logs usando um SDK e as convenções ali conhecidas. Depois,

01:46

esses dados podem ser enviados para diferentes destinos.

01:49

Pode ser um LangFuse, o Phoenix, o Datadog,

01:52

o New Relic, o Azure Monitor,

01:54

o Google Cloud Observability, o CloudWatch, o Grafana Tempo,

01:57

o Jaeger e outras soluções por aí. Então,

02:00

pensa nele como uma chamada de instrumentação e transporte.

02:05

A aplicação não deveria ficar totalmente presa a

02:09

uma ferramenta específica desde o primeiro dia.

02:11

Se o instrumento, tudo...

02:15

apenas com uma API proprietária, talvez funcione bem naquele momento,

02:20

mas depois de trocar ou combinar ferramentas,

02:23

pode ficar mais difícil. Com OpenTelemetry,

02:25

eu consigo ter uma base muito mais aberta.

02:28

A arquitetura típica fica mais ou menos assim.

02:31

A aplicação executa uma requisição. Dentro dela,

02:34

a gente cria spans para etapas importantes.

02:37

Por exemplo, como chamada ao modelo, retrieval, call, re-ranking,

02:42

geração de resposta ou qualquer outro passo que a gente ache relevante.

02:45

Esses spans carregam atributos,

02:47

por exemplo, nome do modelo, provider, quantidade de tokens,

02:51

tempo da chamada, se houve erro,

02:53

se houve fallback, a quantidade de chunks recuperados e por aí vai.

02:56

Depois, esses dados são exportados.

02:59

Às vezes a aplicação exporta direto para uma ferramenta.

03:03

Em outros cenários, ela manda para um OpenTelemetry Collector.

03:07

O Collector funciona como um intermediário. Ele recebe a telemetria,

03:12

pode processar, filtrar, transformar e encaminhar para um ou mais destinos,

03:19

no final das contas. E isso é útil em arquitetura,

03:22

porque separa completamente essa parte de responsabilidades.

03:26

A aplicação fica responsável por instrumentar o que importa.

03:30

O Collector pode cuidar...

03:33

de roteamento, transformação, enriquecimento e inclusive a exportação dos dados.

03:38

A ferramenta final, ela fica apenas para visualização, busca, dashboards,

03:44

alertas e toda a parte de análise. Agora, um cuidado, tá?

03:48

O OpenTelemetry não decide sozinho o que é importante observar.

03:52

Quem decide isso é a arquitetura da aplicação. No nosso caso,

03:57

não basta criar um span genérico chamado chat, porque isso não vai ajudar muito.

04:01

A gente precisa pensar nas etapas que realmente explicam o comportamento do sistema.

04:07

Em uma chamada simples do modelo, talvez um span de model call seja suficiente.

04:12

Num workflow com ferramentas, talvez faça sentido ter span para cada tool call.

04:17

Em um agente,

04:19

talvez cada ciclo de decisão e execução precise aparecer. Por exemplo,

04:24

no nosso lab de RAG, a gente vai usar os spans como...

04:28

query planning, retrieval, re-ranking, answer generation.

04:32

Porque essas etapas são importantes e explicam por que uma resposta foi gerada.

04:38

Então, o OpenTelemetry não é o objetivo, vamos dizer assim,

04:42

final da aula. O objetivo final é...

04:45

Observabilidade. O OpenTelemetry entra como um meio para gerar

04:48

dados de forma mais padronizada e permitir

04:52

que a gente envie esses dados para uma ferramenta

04:55

onde seja possível investigar ali o sistema.

04:59

Então, nesse módulo, a ferramenta principal, provavelmente,

05:01

a gente vai trabalhar com uma LangChain da vida.

05:03

A gente vai usar o LangChain como um destino visual para enxergar o pipeline.

05:09

Vamos dizer assim. Mas o conceito por trás,

05:12

ele vale para outras ferramentas também. A mensagem principal dessa aula é...

05:16

O OpenTelemetry é a camada que ajuda a

05:19

aplicação a falar a linguagem da observabilidade,

05:22

mas o valor ele aparece quando essa telemetria é bem pensada,

05:26

bem filtrada e enviada para uma ferramenta onde

05:30

o time consegue investigar o comportamento, custo,

05:32

latência e qualidade, tá?

05:34

Então, no próximo vídeo, a gente vai começar ali essa parte mais prática.

05:38

Vamos instrumentar ali o nosso pipeline com o Spence,

05:41

preparar o projeto para enxergar essas etapas de execução ali de forma mais... Mais clara.

## Resumo IA

[RESUMO_IA]