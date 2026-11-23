Módulo: Arquitetura na Era da IA\
Aula: [Soluções prontas de providers e decisão build vs buy](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18454)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

Até aqui a gente construiu um RAG praticamente de ponta a ponta.

00:06

A gente preparou documentos, gerou chunks, colocou metadados,

00:09

indexou no post o grafo com o pgVector, fez o retrieval,

00:12

criou o query planner, adicionou o re-ranking,

00:16

expôs uma API e colocou logs, tempos, tokens,

00:20

informações do modelo no pipeline.

00:22

Agora faz sentido fazer uma pergunta arquitetural aqui.

00:27

Eu preciso construir isso sempre?

00:30

Eu preciso construir tudo isso, tá? E a resposta é não.

00:35

O objetivo de construir esse projeto foi entender o que acontece por dentro.

00:40

Porque quando você entende o pipeline,

00:42

você consegue avaliar a melhor solução pronta que pode existir no mercado.

00:47

Sem isso, qualquer ferramenta vai parecer muito mágica. E quando algo dá errado,

00:52

você não sabe se o problema está na ingestão,

00:54

no chunking, no índice, no retrieval, no re-ranking,

00:57

no prompt ou até mesmo no modelo.

00:59

Hoje, os providers já têm soluções prontas ou

01:03

semi-prontas para esse tipo de problema.

01:05

No Google Cloud, por exemplo,

01:07

existe o Reg Engine dentro do Gemini Enterprise Agent Platform.

01:13

A documentação posiciona o Reg Engine como um componente para construir

01:19

aplicações com LLM usando o contexto aumentado com dados da empresa,

01:25

incluindo etapas de ingestão, transformação, embedding, indexação,

01:31

retrieval e geração. A própria documentação,

01:35

depois se você dá uma olhada,

01:36

mostra diversas fontes que você pode utilizar como arquivos locais,

01:42

você pode pegar dados do Cloud Storage, dados do Google Drive,

01:45

tudo isso colocar como fluxo de ingestão ali no seu pipeline.

01:51

Falando de AWS, Amazon, ela tem o Amazon Bedrock Knowledge Basis. Então,

01:58

ele permite integrar dados proprietários em aplicações generativas

02:02

e recuperar informação relevante para responder às perguntas.

02:06

A documentação, inclusive, atual,

02:09

separa o Knowledge Basis em opções gerenciadas e Customer Managed.

02:15

Na versão gerenciada, a AWS assume partes como injeção,

02:21

Ingestão, indexação, armazenamento, retrieval, embedding,

02:26

re-ranking e conectores para fontes como o S3, o SharePoint, o Confluence,

02:32

o Google Drive, o OneDrive e também o Web Crawlers. Já na Azure,

02:37

a Azure AI Search é uma peça muito forte se você quer utilizar a RAG.

02:43

Por quê? Porque a documentação, inclusive,

02:45

dá dois caminhos ali para a gente. O reg clássico,

02:48

usando uma busca híbrida e uma parte de semantic ranking. E o agentic retrieval,

02:55

que adiciona uma query planning com LLM, com múltiplas fontes,

03:00

respostas estruturadas, citações e metadados ali na execução.

03:04

Ela também tem um ponto ali em relação ao Azure AI Search, que ele serve como base,

03:10

tá? para um outro serviço ali, que é o Foundry IQ,

03:14

que é uma camada gerenciada de conhecimento para agentes.

03:19

Então, a gente também tem aí,

03:21

no caso, OpenAI. Na OpenAI, existe o File Search na Responsys API.

03:28

Ela é uma ferramenta que é hospedada,

03:30

que permite o modelo a buscar arquivos antes de gerar a resposta.

03:35

Então, a documentação, se você olhar mesmo, ela fala o seguinte, tá?

03:40

que em vector stores,

03:43

onde você precisa de busca semântica e também keyword

03:47

search sobre os arquivos que são enviados,

03:50

você não precisa fazer essa implementação, vamos dizer, por conta própria.

03:56

Então, existe isso no file search, nas responses APIs ali.

04:01

Não sei se você conseguiu perceber o padrão, tá?

04:04

O que a gente construiu manualmente, tá,

04:06

nesse capítulo, vários providers tentam abstrair.

04:09

Eles cuidam de partes do pipeline para você. Em alguns casos,

04:13

eles cuidam da gestão, em outros cuidam do Vector Store,

04:16

em outros oferecem uma busca híbrida, permissão, citação,

04:19

ranking, etc. Isso, assim, é super ótimo para a produtividade.

04:23

Se você precisa validar uma ideia rápida,

04:25

talvez uma solução gerenciada faça muito mais sentido. Se, inclusive,

04:30

por exemplo, a empresa já está toda na AWS,

04:33

na Azure, no GCP, no Google Cloud,

04:35

também pode fazer sentido aproveitar todo esse ecossistema. Agora, se o time também,

04:41

inclusive, não quer operar um vector store, um pipeline de gestão,

04:46

parsing... reindexação, conectores, o provider também pode reduzir muito,

04:52

muito esse trabalho. Por outro lado...

04:55

Quando você usa uma solução pronta, você ganha velocidade,

04:59

mas pode perder um pouco de controle.

05:01

Talvez você não consiga definir exatamente como o chunk é criado.

05:06

Talvez você não consiga aplicar exatamente a lógica de

05:09

query planner que a sua aplicação precisa.

05:11

Talvez o debug seja um pouco mais limitado. Talvez o custo seja menos previsível.

05:17

Talvez a gente tenha um lock-in forte. Ou seja, a gente fica ali preso,

05:22

entre aspas, dentro daquela solução. Então, talvez a solução,

05:27

inclusive, ela funcione muito bem no caso padrão,

05:30

mas que fique muito difícil quando o seu domínio tem muitas regras específicas. Então,

05:36

eu diria que esse tipo de coisa são soluções 80-20,

05:40

que 80% das vezes essa parada vai funcionar,

05:43

mas tem os 20% que o seu caso é

05:46

tão específico que eventualmente essas ferramentas não vão atender você 100%.

05:51

Então, a decisão não é simplesmente build é melhor ou buy é melhor,

05:58

porque a gente sempre tem essa, build ou buy. Então,

06:02

a decisão é quanto controle eu preciso, quanto tempo eu tenho,

06:07

qual é a maturidade do time, qual é o risco do meu domínio,

06:11

quanto eu preciso para debugar e quantas customizações o pipeline vai exigir.

06:18

O RAG é uma feature auxiliar, uma solução pronta pode ser super suficiente.

06:25

Agora, se o RAG for o coração do produto,

06:29

talvez você queira mais controle. Se a base é simples,

06:32

o provider pode acelerar. Se a base tem muita regra de permissão,

06:36

versionamento, metadados específicos e diversos fluxos de aprovação,

06:40

talvez uma implementação própria ou híbrida faça mais sentido.

06:45

E existe também o meio termo.

06:47

Você pode usar o provider para parte da solução e

06:51

manter outra parte ali sob o seu controle.

06:53

Por exemplo, você pode usar um search gerenciado, mas controlar o prompt final.

06:58

Você pode usar conectores prontos, mas ter a sua própria camada de autorização.

07:02

Você pode usar um vector store gerenciado,

07:05

mas manter os logs e métricas do pipeline na sua aplicação.

07:09

O ponto principal é que agora você consegue fazer essa avaliação com mais clareza.

07:14

Porque a gente não está mais falando de RAG como uma buzzword.

07:18

A gente viu as peças. A gente viu onde... a gente tem problemas de falha,

07:24

a gente entendeu um pouco mais sobre custo, latência, tokens, filtros,

07:28

reindexação, query planning, re-ranking. Então, quando você vai,

07:32

por exemplo, para o Vertex AI Reg Engine,

07:35

o Bedrock Knowledge Basis, o Azure AI Search,

07:38

o OpenAI File Search ou qualquer outra solução,

07:42

a pergunta não é, essa ferramenta faz RAG? A pergunta é,

07:46

quais partes do pipeline ela resolve? Quais partes ela esconde?

07:52

E quais partes eu ainda preciso controlar?

07:55

Essa eu acho que é a mentalidade quando a

07:57

gente está pensando em fazer arquiteturas de aplicações, por exemplo,

08:02

nesse tipo de caso. Por quê?

08:04

Porque quando a gente entende a ideia de forma geral, como você viu agora,

08:12

o processo de implementação e quem você vai utilizar para fazer,

08:16

daí já vai ser uma decisão, tanto técnica,

08:19

mas também grande parte das vezes de negócio,

08:22

de acordo com os contratos que a sua empresa tem com o provedor e coisas desse tipo.

08:26

Então, no próximo vídeo,

08:28

a gente vai fechar esse nosso capítulo com um checklist.

08:31

A ideia é transformar tudo o que a gente viu em

08:34

uma lista prática para decidir quando usar a RAG,

08:37

quando não usar, quando construir, quando comprar.

08:41

Quais perguntas precisam ser respondidas antes de levar isso aí para a produção?

08:46

Então, vamos nessa.

## Resumo IA

[RESUMO_IA]