Módulo: DevOps e SRE com IA\
Aula: [Postmortem Automático](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18552)

## Resumo da aula



## Transcrição

00:00

Vamos lá, pessoal. Agora vamos gerar aqui o nosso pós -mortem.

00:06

Basicamente, o modelo de pós -mortem de direito consome audit logs,

00:09

que os dados serão construídos.

00:10

Incidente MCP audit log, timeline completa do incidente,

00:13

prometer os MCP, métrica de impacto, error rate, calendário,

00:18

ele vai inserir no calendário aqui algumas coisas para

00:21

a gente com as datas do incidente,

00:22

alguma coisa, e com a 8S MCP, que é o status atual do pod. Legal?

00:30

O incidente aqui é só um exemplo de um pós -morte draft.

00:33

E vamos lá fazer os nossos testes aqui para a pós -morte.

00:39

Antes de iniciar, vamos dar uma olhada aqui no LingFuse,

00:42

que estava dando problema na primeira demo.

00:45

Agora a gente tem aqui tudo o que aconteceu naquele chat que a gente falou.

00:49

Até a última parte aqui que eu pedi para

00:51

ele gerar uma nota de documentação completa.

00:53

Legal? Então a gente consegue ter um... um audit de ponta a ponta,

00:58

o que o usuário fez, o que ele pediu, quais foram as tasks chamadas.

01:02

A gente tem aqui, ó, quais foram as tasks que ele chamou.

01:05

Então, temos tudo detalhado aqui do Endoleng Fuse.

01:08

Isso é muito importante para a gente conseguir fazer auditoria,

01:10

verificar quem que fez o quê e assim por diante, entendeu? Inclusive,

01:14

a gente tem até identificado aqui quem que é

01:16

o nome do nosso serviço que está rodando.

01:19

Legal? Então, a gente tem isso tudo bem definido aqui.

01:23

Combinado? Então, vamos voltar lá.

01:25

Trocar o nosso agent aqui para o pós -mortem generator.

01:30

Abrir uma nova abinha aqui, um novo chat. E vamos começar aqui.

01:34

O objetivo nosso aqui é gerar um blameless aqui completo,

01:41

baseado nos dados reais dos acidentes que acabamos de simular aqui.

01:45

Legal? Então vamos lá.

01:47

Gere um pós -mortem.

02:00

Blameless para o incidente

02:06

que acabamos de...

02:13

Na verdade, vou pegar o chat antigo. Vamos pegar esse chat aqui.

02:18

Vamos trocar aqui dentro do próprio chat para o Postmortem Generator.

02:24

Vamos digitar aqui, nesse mesmo chat. Então, gere um post

02:32

-mortem

02:36

blameless para o incidente

02:42

que acabamos de resolver.

02:45

Use o audit

02:47

log do

02:50

incidentes MCP para

02:56

construir a TimeLine

03:00

Consulting o Prometheus para

03:08

métricas de impacto e

03:14

gere o pós

03:17

-mortem completo com

03:21

as nove ações.

03:24

Nove ações.

03:31

Obrigado. Obrigado. Vitórias. Vamos embora.

03:36

Vamos ver o que ele vai fazer aqui pra gente agora.

03:39

O bom é que a gente vai conseguir usar até o próprio histórico.

03:42

Por que eu mudei pro chat, tá, gente?

03:43

A gente consegue usar o próprio histórico do chat com

03:47

o insumo de dados pra ele conseguir gerar esse pós-mortem.

03:51

Entendeu? Então, basta trocar o agent ali em cima,

03:54

ele vai continuar no mesmo chat, com o mesmo histórico de chat,

03:58

para fazer a melhoria aí do pós-mortem.

04:02

Pra fazer a melhoria não, né? Pra fazer a geração do pós-mortem pra gente.

04:06

Combinado? Então isso é bem legal aí pra

04:09

gente conseguir gerar um documento bem completo.

04:14

Tá iniciando aqui a geração.

04:17

Vou gerar um audit log, incidentes. Então aqui, ó.

04:21

Primeiro a gente tá fazendo algumas coisas lá dentro do MCP get audit log.

04:25

Ele já pegou um get audit log lá dos nossos incidentes.

04:30

Incidentes MCP. Então ele pegou aqui um calendário. Search. Calendário event.

04:36

Então ele está olhando aqui o calendário.

04:40

Query range, query range.

04:42

Ele está pegando algumas coisas aqui dentro do nosso Prometheus.

04:48

Get Prometheus status post. Está pegando aqui algumas coisas do Prometheus.

04:53

Está puxando aqui mais dados. Vamos esperar para ver o que ele está puxando.

05:00

Não há alerta configurada no Prometheus. A gente não tem nenhum alerta configurado.

05:04

Vou consultar o Homebook. Ele está consultando o Homebook lá.

05:07

Os alertas parecem que não se aplicaram ali para o nosso API.

05:13

Mas não tem problema.

05:15

Ele consegue puxar outras coisas aqui para ele construir esse pós-mortem.

05:20

No melhor dos mundos, esses alertas aplicados,

05:23

ele conseguiria puxar e trazer esses dados lá pra gente. Entendeu?

05:27

Então foi um incidente de P2.

05:31

Crash no... Backoff, na API, dia 18 de junho de 2026,

05:36

aí ele escreve aqui, resumo, 18 vezes,

05:40

não vou ler tudo aqui, mas ele fala que no dia tal,

05:44

aconteceu tal caos, tal coisa, no namespace tal,

05:47

entrou em estado de crash loop backoff, afetando todos os pods do serviço,

05:53

o incidente foi resolvido após a remoção da

05:55

falha injetada propositalmente para fins de simulação.

05:58

A duração foi 8 minutos, o impacto foi 100%,

06:02

dos pods indisponíveis durante o crash do Backoff,

06:05

afetando todos os usuários da

06:09

aplicação API no ambiente staging demo. O impacto,

06:13

aqui é uma timeline do que aconteceu, audit log, sistema demo,

06:18

análise dos cinco porquês, que é os cinco Ws, né?

06:22

Por que os pods entraram? Resposta,

06:24

porque a aplicação falhava na legislação com o erro de ESC1, simples.

06:29

Por que a aplicação falhava na inicialização?

06:32

Resposta. E assim por diante. Aplicou os cinco dados.

06:34

O que funcionou bem? Que o switch,

06:36

governança de ações, o que poderia ter sido melhor? Tudo aqui, gente.

06:40

A gente tem toda a descrição certinha do que aconteceu e do que a gente...

06:46

do que aconteceu durante esse incidente.

06:50

Ele gerou tudo automático. Imagina você digitar essa verificação toda. Entendeu?

06:57

Então, fazer uma análise aqui rápida.

07:01

Vamos ver aqui o porquê. Quê porquê.

07:03

Por que a simulação foi devidamente documentada e comunicada? Não foi.

07:08

Porque o processo de gerenciamento de simulações de falhas não

07:11

inclui requisito obrigatório de documentação e assim por diante.

07:14

E aqui a causa raiz. Porque não existe processo formal de simulação de falha.

07:20

Resposta e assim por diante.

07:22

Vocês vão conseguir simular isso aí também e ver funcionando.

07:26

A gente vai conseguir verificar aqui no LengthFuse também,

07:30

essa geração do

07:31

nosso post-mortem aqui.

07:37

Deixa ele iniciar aqui o LengthFuse. Está

07:43

em loading aqui, vamos esperar um pouquinho para ele carregar a tela.

07:48

Ok, carregou aqui.

07:50

Vamos ver lá na última resposta. A gente tem aqui...

07:56

gerar um post-mortem, que foi a que eu fiz, né?

07:59

E aqui embaixo a gente tem o post-mortem gerado.

08:03

Deixa eu descer aqui um pouquinho. Aqui, ó. Temos aqui o nosso post-mortem gerado.

08:08

P2, Crash Look Back Off, a aplicação tal, e assim por diante.

08:12

Tem aqui toda a documentação feita também dentro do nosso Langfuse, tá? Então,

08:18

tudo está sendo enviado lá para o Langfuse fazer

08:21

a documentação disso e o rastreio também.

08:25

ponta a ponta das coisas que estão acontecendo. Ok?

## Resumo IA

[RESUMO_IA]