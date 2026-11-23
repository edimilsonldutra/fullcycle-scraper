Módulo: DevOps e SRE com IA\
Aula: [Conceitos, Arquitetura & Hands-on](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18516)

## Resumo da aula



## Transcrição

00:00

Eu já passei por essa parte no módulo 0,

00:02

explicando um pouco mais sobre a diferença de SRE e DevOps,

00:07

mas é bom a gente sempre voltar, para a gente sempre ficar na mesma página.

00:11

O DevOps vai entregar esteiras, GitOps,

00:14

todos os padrões para o desenvolvedor fazer a entrega do aplicativo dele,

00:20

da aplicação dele. O SRE vai trazer a estabilidade,

00:23

então ele vai definir SLE, SLO, Error Budget e etc. para reduzir,

00:28

a carga de trabalho que eles têm para monitorar,

00:31

para manter as aplicações de pé. Então,

00:34

a IA generativa consegue ajudar em ambos ali. Então,

00:37

a IA vai conseguir fazer ambos os papéis ali para ajudar no

00:41

dia a dia do desenvolvedor e de toda a equipe de SRE. Então,

00:47

falando um pouco mais aqui aonde que a IA vai atuar, ela vai conseguir...

00:52

Para o DevOps mais GNI, ela vai conseguir gerar Dockerfiles, Manifest,

00:56

Docker Compose. Ela vai conseguir criar pipelines de CI/CD via PropT. Então,

01:02

a gente consegue definir uma pipeline completa de entrega de código em ambientes, Kubernetes,

01:08

qualquer outro tipo de ambiente, via PropT. Digitando,

01:12

simplesmente conversando com a IA ali.

01:16

Ela consegue fazer code review de tudo que é gerado,

01:19

você consegue usar até o próprio open code para isso, ou o compiler,

01:23

o que seja, você consegue usar para fazer esse code review.

01:28

E por último ali, na parte de DevOps com o GNI, a gente consegue gerar também IACs.

01:34

O IAC a gente vai conseguir provisionar dentro de infraestrutura cloud,

01:39

serviços como Postgres, etc. Vários serviços ali,

01:45

como armazenamento de dados e assim por diante.

01:48

de várias nuvens disponíveis no mercado,

01:52

usando o Terraform AI.

01:57

Então, na parte de SRE,

02:00

vamos conseguir mapear SLI e SLO automaticamente.

02:04

Vamos conseguir dar um diagnóstico conversacional usando os servidores MCP.

02:10

Os servidores MCP são como braços ali para puxar informações para dentro da

02:14

IA e ela conseguir resolver isso para você e te dar uma resposta bacana.

02:18

Vamos criar homebooks e pós-mortes

02:22

gerados automaticamente e agents de troubleshoot operacionais.

02:26

Legal? Então, o que muda aqui não é a ferramenta.

02:29

O que muda é a velocidade e a qualidade do... arquivo inicial,

02:34

mas ainda a gente continua validando. Nós, como DevOps e SRE,

02:39

continuamos validando o que é gerado. Então, ele vai gerar um Dockerfile,

02:42

a gente vai usar um Docker Build para fazer a validação, validar o tamanho, etc.

02:48

Gerou um manifesto de Kubernetes ali,

02:50

a gente vai fazer a validação daquilo, fazer o deploy,

02:53

dar um get pod ali para tentar ver se aquilo está rodando conforme o esperado.

02:59

Um robô que ainda vai precisar de uma revisão humana. Então,

03:02

várias coisas ainda a gente vai precisar da revisão humana usando IA.

03:06

Ela vai facilitar o seu dia a dia,

03:09

porém a revisão humana é indispensável porque ela pode criar coisas

03:13

ali que não estão de acordo com a realidade da sua empresa.

03:18

Nesse próximo momento aqui,

03:19

nós vamos começar falando um pouco da aplicação que vai ser a base

03:24

para a gente desenvolver todo o nosso projeto até chegar lá no módulo 5.

03:28

A gente vai começar com uma aplicação simples, em FastAPI, com SLOs bem definidos,

03:34

um SLO de 99,9% de disponibilidade, ou seja,

03:40

um erro rate ali abaixo de 0,1%,

03:45

o percentil 99 abaixo de 500 milissegundos e o

03:50

percentil 95 abaixo de 200 milissegundos de respostas ali, ok?

03:55

Isso dá um erro budget de 43 minutos por mês,

03:59

então a gente pode falhar no máximo 43 minutos por mês com essa aplicação.

04:05

Esses SLOs serão o fio condutor para as nossas próximas atividades,

04:11

para os nossos próximos desenvolvimentos. Eles informam para o HPA...

04:16

quantas réplicas são necessárias para escalar,

04:19

o HPA vai ser usado dentro do Kubernetes, os resource limits,

04:22

conta de memória e CPU que eu vou alocar ali para dentro do meu serviço,

04:26

e os alertas de thresholds ali, quando disparar notificações,

04:31

as ações com o robô, disparar notificações,

04:35

e as ações no Helm chart e decisões de rollback,

04:38

quando sobe alguma coisa e precisa dar um rollback ali.

04:43

Todo downstream parte dos SLOs.

04:46

A aplicação não tem Dockerfile, não tem manifesto e não tem um README.

04:52

Então a gente vai gerar tudo aqui usando a Generative AI.

04:59

Pessoal, no próximo slide aqui,

05:02

a gente vai falar um pouco da arquitetura da nossa aplicação. Na primeira camada,

05:07

a gente está falando aqui do app. E é um FastAPI comum,

05:11

bem simples aqui para a gente demonstrar.

05:14

A gente tem alguns paths dele aqui. O primeiro é o /health,

05:19

onde a gente vai conseguir fazer um health check

05:21

de Kubernetes para validar a saúde do pod,

05:24

se ele está saudável,

05:26

se ele precisa ser reiniciado ou algo do tipo. Vai ter um API v1 /itens,

05:31

que é o endpoint principal da aplicação, onde a gente consegue consultar,

05:35

inserir e deletar itens da nossa aplicação.

05:39

E o /metrics é onde o Prometheus vai conseguir fazer o scrape

05:44

das métricas para monitoramento, ok?

05:47

Ele vai se conectar a um PostgreSQL desenvolvido...

05:52

Deployado junto com a aplicação ou qualquer outro

05:56

PostgreSQL que você esteja deployado aí

05:59

já e um Redis para fazer cache de algumas coisas que são necessárias aí.

06:05

Combinado? Na terceira camada, a gente tem aqui a parte de observabilidade.

06:11

onde a gente tem um Prometheus, que vai fazer o scrape do /metrics,

06:14

que eu já falei ali em cima na aplicação. A gente tem um Grafana,

06:17

que a gente consegue ver gráficos do Kubernetes,

06:21

de qual está a saúde do pod, de como ele está se comportando,

06:25

se está gastando muita memória, se não está, e assim por diante.

06:28

E o Langfuse a gente vai usar lá no final

06:31

para fazer o rastreio das interações com o Generative AI.

06:36

A gente vai fazer o log dessas informações dentro do Langfuse.

06:41

Aqui embaixo a gente tem algumas alternativas que a gente pode usar,

06:44

que são pagas,

06:46

que substituem perfeitamente esses serviços que eu falei que são open source.

06:52

Datadog, New Relic e Home Assistant, que são alternativas pagas para a gente usar.

06:57

Aqui na última, na penúltima parte aqui,

07:01

A gente está falando aqui só dos SLOs definidos,

07:03

que é o percentil 99 de menos de 500 milissegundos.

07:08

A disponibilidade de 99,9% e os

07:13

erros com menos de 0,1% de erro.

07:18

Então, os SLOs vão definir o HPA,

07:22

vai definir alertas e vai definir a maneira que

07:26

a gente vai fazer o deploy dos nossos serviços.

07:32

Então, visto a arquitetura aqui, a gente vai passar para a parte de mão na massa.

07:38

Na primeira etapa,

07:39

Nós vamos ter um hands-on para gerar os Dockerfiles multistage usando

07:46

o OpenCode e os prompts que a gente já tem gerado aqui,

07:52

eu vou passar para vocês, e mostrar o resultado fazendo execução,

07:56

fazendo um Docker build,

07:57

fazendo uma imagem Docker para a gente ver as imagens de fato.

08:03

A gente também tem o Docker instalado aqui na máquina e

08:06

vamos mostrar para vocês aqui como que vai funcionar. Então,

08:10

primeiro vamos gerar um Dockerfile.

08:14

Primeiro passo, pessoal,

08:15

nós vamos aqui no nosso terminal e abrir o OpenCode dentro da pasta do app.

08:21

Então, a gente tem aqui a pastinha do app e a gente vai abrir o OpenCode.

08:28

OpenCode aberto, a gente vai ter...

08:31

Vou abrir aqui um arquivinho e vou colar para

08:34

vocês aqui o prompt para a gente gerar o Dockerfile.

08:39

Esse prompt eu já tinha definido ele previamente aqui,

08:42

vou só passar com eles para vocês rapidinho,

08:44

para a gente entender o que a gente tem nesse prompt.

08:48

Então vamos lá. Joga um arquivo, Dockerfile, production ready, multistage,

08:53

para a seguinte aplicação FastAPI. Siga todas as melhores práticas e estados abaixo.

08:58

Então aqui eu listo todo o contexto da aplicação, o nome dela,

09:02

a linguagem que a gente está usando, o framework, que é um FastAPI, o Uvicorn.

09:08

Então aqui a gente tem a parte de SLO também, e o ponto aqui de exposição,

09:14

que vai ser a porta que o aplicativo vai ficar exposto,

09:17

e um endpoint de health check que a gente já definiu, que é o /health aqui.

09:23

Em teoria, quando a gente jogar isso aqui dentro lá do nosso prompt,

09:28

dentro do nosso OpenCode, ele vai fazer a geração do arquivo para a gente.

09:32

Aqui a definição de alguns requisitos obrigatórios,

09:36

que é o stage de build e o stage de runtime,

09:40

usando a Python 3.11-slim,

09:43

que é uma das menores imagens de Python que

09:48

tem disponível para a gente conseguir usar.

09:50

Vai instalar as dependências com o --no-cache-dir,

09:54

com o arquivo requirements.txt que a gente tem aqui disponível.

09:59

Não root, a gente vai definir que não vai rodar como usuário root.

10:04

A gente vai ter um layer de cache otimizado,

10:06

que a gente vai usar para fazer o install das dependências

10:09

antes de copiar o código da aplicação. O health check,

10:12

vai definir que o health check vai ser esse /health,

10:16

que eu já falei ali. O tamanho alvo,

10:18

então a imagem tem que ficar no final com menos de 100 megabytes.

10:23

As variáveis de ambiente vão ser definidas aqui.

10:27

O trabalho de estrutura, vamos definir tudo aqui embaixo.

10:32

E por último, a gente vai ter aqui a parte de expose e CMD.

10:37

que é a porta que ele vai ser exposta,

10:38

que aqui é a 8000, e o CMD,

10:41

que vai ser o comando que vai ser executado para iniciar a aplicação.

10:45

Aqui temos algumas regras negativas do prompt,

10:48

que ele fala para não fazer. Então, se você tem alguma restrição,

10:53

alguma coisa que você queira que ele não faça,

10:56

você vai definir nesse momento aqui no prompt. Certo?

11:01

Aí vocês podem me perguntar. Se a gente já está definindo o CMD,

11:06

se a gente já está definindo o expose,

11:08

se a gente vai estar definindo aqui as variáveis de ambiente aqui em cima,

11:12

várias coisas do tipo, por que não criar o Docker Compose direto?

11:16

O Docker Compose não. O Dockerfile, direto.

11:19

Por que a gente não cria ele direto?

11:20

Se a gente já tem todas as informações aqui definidas.

11:23

O interessante da gente ter isso aqui é que a gente pode reutilizar essas partes,

11:27

simplesmente substituindo variáveis.

11:29

Então, apareceu uma aplicação amanhã, a gente pode reutilizar.

11:34

esse prompt para gerar uma aplicação nova e assim por diante.

11:37

Então, definiu o prompt,

11:39

definiu as variáveis, gera a aplicação e vai gerando várias aplicações ali.

11:44

No caso, vários Dockerfiles, não aplicações. A aplicação já está definida,

11:49

já está criada e já vai definir vários Dockerfiles ali.

11:52

Ok? Então, antes de a gente fazer a criação desse Dockerfile,

11:58

eu vou subir a aplicação aqui localmente na máquina,

12:03

para a gente ver que ela está funcionando bacana.

12:05

Eu vou fazer alguns testes aqui para a gente validar o funcionamento do app em si.

## Resumo IA

[RESUMO_IA]