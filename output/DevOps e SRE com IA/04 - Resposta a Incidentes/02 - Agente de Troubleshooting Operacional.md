Módulo: DevOps e SRE com IA\
Aula: [Agente de Troubleshooting Operacional](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18539)

## Resumo da aula



## Transcrição

00:00

Então, um agent de troubleshooting operacional. O que a gente vai fazer aqui?

00:05

O sistema identifica os erros de código

00:08

e o cluster e a gente vai

00:12

sugerir ações e a gente vai decidir usando aqui o OpenAPI e 4 MCP.

00:19

Então, o OpenAPI vai se conectar aos MCPs via protocolo

00:24

de stream HTTP para os MCPs que a gente vai desenvolver.

00:29

O K8S vai usar aquele Flux 159 via MCPO, que eu já tinha falado.

00:33

E o LLM, que vai dar acesso do LLM ao cluster Kubernetes para consultar log,

00:39

ler pods, fazer rollout, escalar deployments e assim por diante. E o Prometheus,

00:45

a gente vai conseguir dar acesso às métricas. Legal?

00:48

Igual a gente tinha feito na última aula.

00:52

O nosso serviço, default injection.

00:56

vai rodar em FastMCP, e o serviço de incidentes MCP,

01:00

que é o guardião ali que vai te pedir para você tomar a decisão,

01:04

vai rodar também em FastMCP. Já tem ele desenvolvido aqui,

01:07

vou disponibilizar para você,

01:09

você sobe na infraestrutura e faça um teste aí também. Ok?

01:13

O que nome de base que a gente vai usar aqui?

01:16

Ele vai colocar todas as homebooks do nosso serviço,

01:21

que são as regras de reiniciar quando tem algum tipo de problema,

01:24

etc. Então a gente tem quatro arquivos homebooks aqui para a gente colocar.

01:29

Vou mostrar eles já já para vocês,

01:31

que vão ser carregados direto pela interface do OpenRBI e vão ficar

01:34

disponíveis para busca semântica lá dentro

01:37

dos nossos agents dentro do OpenRBI. Legal?

01:42

O LangFuse vai trackear tudo, a gente vai rastrear tudo,

01:46

igual a gente já tinha configurado o LangFuse na última aula.

01:49

Então ele vai trackear tudo na entrada e vai,

01:53

quando sair, trackear a resposta que vai ser capturada.

01:56

Isso vai substituir um audit log customizado,

02:00

etc. A gente vai conseguir rastrear

02:02

todas as interações através do LangFuse.

02:08

Então no Open Web UI a gente vai configurar três modelos.

02:11

Um vai ser o SRE Thresholder, que a gente já tinha configurado na última aula.

02:17

Na verdade, a gente tinha configurado o Kubernetes Thresholder.

02:19

Agora vai ser um SRE Thresholder, que vai diagnosticar e sugerir ações.

02:24

Um Pós -Mortem Generator,

02:26

que vai conseguir gerar um pós -mortem para a gente com um rascunho.

02:30

Vai gerar um rascunho de pós -mortem para a gente validar.

02:32

E um SRE Health Monitor, que vai monitorar a saúde geral.

02:37

em três automações.

02:38

A gente vai ter três automações que a gente vai conseguir colocar pelo Open Web UI,

02:42

que ele vai ter um health check,

02:44

que ele vai ficar a cada cinco minutos rodando

02:46

para fazer um health check do seu serviço,

02:47

um SLO monitor,

02:49

que vai ficar a cada 15 minutos rodando para validar o SLO,

02:51

e um pós -mortem reminder, que vai ficar diariamente rodando, diariamente, assim,

02:58

a cada nove horas ele roda e faz um pós -mortem de tudo que aconteceu.

03:02

Ok? Então a classificação do Blast Eraders,

03:05

Vai definir o modo de operação. Então,

03:09

o copiloto ali vai descer os necessários para

03:15

ações de aprovações humanas e vai ser semi-autônomo, beleza? Então,

03:20

alguns agentes desses vão ser

03:23

copilotos dos nossos operadores ali do

03:28

SRE para fazer a manutenção desse serviço que a gente tem.

03:34

Lembrando que aqui a gente está trabalhando só com um serviço,

03:36

claro que você pode também expandir para outros serviços do seu cluster,

03:43

ok? Então, ele não serve só para esse serviço,

03:46

você pode colocar N outros serviços para serem monitorados

03:50

ou até o cluster todo por essa stack.

03:53

Fazer o troubleshoot completo aí do seu Kubernetes ou outros stacks que você tem, ok?

04:01

Passando aqui para o próximo slide,

04:04

a gente tem aqui o fluxo que o agent de troubleshoot vai seguir.

04:08

Então, centralizado ali no meio, a gente tem um OpenMBI,

04:12

que vai ser a arquitetura centralizada,

04:16

o ponto central de entrada de dados aqui dos nossos usuários. Então,

04:22

o OpenMBI vai contar ali com quatro MCPs, o K8S MCP,

04:29

Prometer os MCP, Acknowled Base e os Incidentes MCP. Ok?

04:34

A gente tem quatro stacks aí que vão fornecer dados para o OpenWebUI, nossa, embolei tudo,

04:41

para o OpenWebUI fazer o troubleshoot para você. Ok?

04:47

Então, Acknowled Base vai usar ali por trás um ChromaDB.

04:54

Falando aqui de Knowledge Base, que é um que se destaca aqui, que não é um MCP,

04:58

é só uma base de conhecimento onde a gente vai consultar algumas coisas.

05:01

Então, ele vai usar o ChromaDB.

05:03

O Incident MCP, como já tinha dito, a gente vai usar o FastAPI.

05:09

E os outros dois aqui a gente vai usar o STDIO convertido para o MCP. Beleza?

05:16

O Langfuse vai rastrear tudo. Então a gente vai rastrear.

05:20

todas as partes ali com o Langfuse,

05:22

e a gente vai ter Agents ali com o CopilotMod,

05:25

onde a gente pode usar ele como copiloto para a operação de SRE,

05:30

e a gente vai ter alguns Semi-Autonomous Mode ali,

05:33

onde eles vão iniciar alguma coisa quanto a diagnosticar,

05:37

e você vai dar continuidade aprovando ali o segmento de um rollout,

05:44

de um restart, de um scale de pod e assim por diante. Legal?

05:49

No final, a gente vai ter o diagnóstico com linguagem natural e um pós-mortem, um draft,

05:54

que é um rascunho do pós-mortem aí,

05:56

feito para você entregar o

06:01

relatório final daquele incidente que aconteceu. Ok, pessoal?

06:06

Continuando, a gente aqui na primeira parte,

06:11

a gente vai fazer um teste aqui com o Fault Injection MCP.

06:14

O que esse cara é na prática? Ele é só um cara que a gente está criando à parte.

06:19

Se vocês notarem aqui na arquitetura, ele não aparece aqui.

06:22

Mas a gente está criando esse cara à parte para

06:24

a gente conseguir simular um problema dentro da nossa infraestrutura.

06:29

Então, a gente vai pedir para ele fazer a simulação de um problema,

06:35

validar se aquele serviço está quebrado e assim por diante.

06:40

Então, vamos construir. Porém... Antes de construir,

06:44

a gente vai fazer uma atualização aqui no nosso serviço.

06:46

A gente vai colocar o serviço aqui.

06:48

do App API com deployment de produção.

06:54

A gente vai chamar isso de deployment.

06:56

A gente vai adicionar alguns alerts brownies

06:59

aqui que o Prometheus vai fazer o get.

07:05

vai puxar isso automaticamente para dentro das métricas dele,

07:09

então esse cara vai ter isso lá dentro.

07:12

Então esse alert rule é um componente do Kubernetes que o Prometheus consome.

07:19

Ok? E vamos fazer a configuração do nosso novo MCPO,

07:23

que como eu disse anteriormente aqui, esse novo MCPO, ele vai ser capaz de destruir,

07:28

destruir não, né? Ele vai ser capaz de fazer o rollout de alguns serviços,

07:32

fazer um autoscale de alguns serviços, ele pode fazer N coisas. Ok?

## Resumo IA

[RESUMO_IA]