Módulo: Arquitetura na Era da IA\
Aula: [Logs, métricas, traces e spans em aplicações com IA](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18749)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente começou falando sobre

00:04

O problema de operar sistemas com IA.

00:07

A ideia principal foi entender que não basta saber se a aplicação respondeu,

00:11

Em sistemas com IA a gente também precisa entender como ela respondeu,

00:15

Quanto custou, quanto demorou,

00:17

Qual modelo foi usado e quais decisões aconteceram ali no caminho.

00:22

Agora, antes de a gente falar sobre OpenTelemetry,

00:24

LangFuse ou qualquer ferramenta específica,

00:27

A gente precisa alinhar alguns conceitos básicos,

00:30

Que são logs, métricas, traces, spans e eventos.

00:36

Esses conceitos não nasceram com a IA,

00:38

Eles já fazem parte da observabilidade de sistemas há muito tempo.

00:42

O que muda agora é que as aplicações com a

00:45

IA adicionam novos sinais que a gente precisa observar.

00:50

Então, vamos começar ali pelos logs.

00:52

O log é um registro de que algo aconteceu.

00:56

A aplicação pode registrar que recebeu uma requisição,

00:59

Chama um modelo, recebeu uma resposta, aplicou um fallback,

01:03

Teve erro de estrutura de output,

01:06

Recusou uma resposta ou atingiu algum limite de custo. Então,

01:12

O log é muito útil quando você quer investigar um caso específico. Por exemplo,

01:17

Um usuário reclamou que recebeu uma resposta ruim. Se você tem um request ID,

01:22

Você consegue procurar os logs daquela execução e entender o que aconteceu.

01:28

Mas o log tem um perigo grande em aplicações com IA, que é logar demais.

01:35

Prompt, ele pode ter dado sensível. O contexto, ele pode ter informação interna.

01:40

As respostas podem conter dados do usuário. O resultado de ferramenta,

01:45

Uma tool calling, pode trazer informação privada. Então, o log precisa ser útil,

01:50

Mas também precisa ser totalmente controlado. Agora,

01:54

Vamos para métricas. Métrica é um número medido ao longo do tempo.

02:00

Quantas chamadas foram feitas? Qual foi a latência? Qual foi o P95?

02:05

Quantos tokens de input foram usados? Quantos tokens de output?

02:09

Qual foi o custo estimado? Quantas respostas ali foram recusadas?

02:13

Quantas chamadas usaram o fallback? Quantas falharam ali por output inválido?

02:19

Então, a métrica é ótima para acompanhar uma determinada...

02:23

Então, se o custo de uma feature começou a subir, uma métrica vai mostrar.

02:28

Se a latência piorou demais depois de trocar um modelo,

02:31

A métrica também vai mostrar. Se a taxa de recusa aumentou muito,

02:35

Essa métrica também, se a gente tiver tudo organizado,

02:38

Ela também mostra, tá? Mas ela não explica tudo sozinha,

02:43

Mas ela mostra que algo necessariamente mudou.

02:46

Agora, já o trace, ele é diferente, tá?

02:51

A trace é um caminho de execução dentro do sistema.

02:55

Ele ajuda a gente a enxergar a história de uma requisição.

02:59

Numa aplicação tradicional, o trace pode mostrar que a API recebeu a requisição,

03:04

Consultou o banco, chamou outro serviço e retornou. Numa aplicação com IA,

03:09

Esse caminho pode mudar bastante dependendo da arquitetura.

03:13

Em um chatbot simples, por exemplo, o trace pode ter só a entrada do usuário,

03:18

A chamada ao modelo, e a resposta final. Numa aplicação com RAG,

03:23

Pode ter o query planning, pode ter o retrieval,

03:25

O re-ranking, a montagem de contexto,

03:28

chamar o modelo e ter ali as respostas como fonte.

03:32

Numa aplicação com tool calling, a gente pode ter decisão do modelo,

03:37

a chamada de uma ferramenta,

03:39

o retorno da ferramenta e uma nova chamada ao modelo para responder.

03:43

Num agente, a gente pode ter vários passos.

03:46

Planejamento, chamadas de ferramenta, observação,

03:50

nova decisão, outra ferramenta, condição de parada para a resposta final. Então,

03:55

percebe que o trace mostra o fluxo, não apenas o resultado. E dentro de um trace,

04:01

a gente tem spans. Então, um span representa uma etapa daquele fluxo.

04:07

Se o trace é a história completa da execução... O span é um capítulo dessa história,

04:12

vamos dizer assim. Por exemplo, em uma aplicação com IA,

04:15

você pode ter um span chamado model call,

04:18

um outro chamado tool call, outro chamado retrieval,

04:22

outro chamado re-ranking, outro chamado answer generation.

04:25

Cada span pode ter duração,

04:29

status e os seus atributos.

04:31

E é aí que a gente começa a registrar as informações importantes sem transformar,

04:37

tudo num log com texto solto.

04:40

No span de uma chamada a um modelo,

04:42

por exemplo, a gente pode registrar o modelo usado,

04:45

os providers, token de entrada, token de saída e a latência.

04:49

No span de uma ferramenta, a gente pode registrar o nome da ferramenta,

04:53

o tempo de execução, o status, se houve erro. Por exemplo, no expand de um reg,

04:58

a gente pode registrar quantos chunks foram recuperados,

05:01

quantos foram selecionados e se a resposta veio com fontes.

05:04

E a gente também tem, então, os eventos.

05:09

Evento é algo pontual que aconteceu dentro de uma execução. Por exemplo,

05:15

cache miss, fallback used, clarification requested,

05:19

structure output failed, no context found.

05:23

Tool Timeout. Então, o evento não precisa virar um span próprio,

05:27

mas ele marca algo importante que aconteceu no meio do caminho.

05:31

Então, simplificando, log registra acontecimentos,

05:35

qualquer coisa que está no passado. A métrica,

05:38

ela mede o comportamento ao longo do tempo.

05:41

O trace mostra o caminho de uma requisição e

05:44

o span representa uma etapa desse caminho.

05:47

E o evento marca algo relevante dentro dessa execução.

05:51

O ponto principal é que esses conceitos ajudam a gente a sair dessa caixa preta. Sem eles,

05:58

a aplicação com IA vira um bloco...

06:01

Vamos dizer assim, totalmente misterioso. O usuário perguntou,

06:04

alguma coisa aconteceu, o modelo respondeu. Já com observabilidade,

06:09

a gente começa a enxergar o caminho.

06:11

Qual etapa rodou, quanto tempo demorou, quanto custou, qual modelo foi usado,

06:16

se houve ferramentas, se houve RAG, se houve uma recusa,

06:19

se teve fallback ou qualquer tipo desses tipos de coisa. Então,

06:23

vamos dizer assim que no nosso laboratório a gente vai usar o projeto

06:26

do RAG porque ele teve várias etapas bem legais para a gente conseguir observar.

06:31

Mas o conceito não é exclusivo de RAG.

06:34

A mesma lógica vale para chamadas diretas a modelos.

06:37

Classificadores, geradores de relatório, tool calling,

06:41

Workflows assíncronos e agentes, tá?

06:43

Então no próximo vídeo a gente vai falar sobre OpenTelemetry, tá?

06:48

A ideia vai ser entender como que a

06:50

gente consegue padronizar essa instrumentação para depois enviar

06:55

esses dados para uma ferramenta onde a gente

06:57

consiga visualizar e investigar o comportamento ali da aplicação.

07:03

Fechou? Então vamos nessa

## Resumo IA

[RESUMO_IA]