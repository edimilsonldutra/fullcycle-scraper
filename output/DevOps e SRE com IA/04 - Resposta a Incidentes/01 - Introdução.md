Módulo: DevOps e SRE com IA\
Aula: [Introdução](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18538)

## Resumo da aula



## Transcrição

00:00

Fala pessoal, sejam bem -vindos ao módulo 4, penúltimo módulo da nossa matéria.

00:08

Vamos falar aqui um pouco hoje sobre respostas a

00:11

incidentes com o suporte de Generative AI.

00:14

Legal? A gente vai conseguir simular, diagnosticar,

00:18

mitigar e documentar os incidentes que a gente tem dentro da nossa infraestrutura,

00:23

dos nossos serviços.

00:24

Legal? Então, o nosso foco aqui vai ser infraestrutura e control blockchute com AI.

00:29

E a entrega do sistema completo,

00:31

configurado e verificado que ele esteja funcionando.

00:34

E a gente vai construir o MCP e fazer o deploy dele.

00:37

Alguns MCPs e fazer o deploy deles, vou passar por eles em breve.

00:41

E a gente vai fazer uma verificação de ponta a ponta do funcionamento.

00:47

No próximo módulo, no módulo 5, já adiantando um pouco, lá para o final,

00:51

tudo que a gente construir aqui, a gente vai testar no módulo 5.

00:56

Então boa parte das ferramentas no módulo anterior,

00:59

no módulo 3 a gente já colocou de pé,

01:02

agora a gente vai construir algumas ferramentas adicionais e vamos fazer o

01:07

uso dela aqui para fazer a resposta de incidente de algumas maneiras automatizadas,

01:13

algumas com interação pelo chat e assim por diante. Legal? Então vamos lá.

01:20

O próximo slide aqui.

01:23

Como a gente está fazendo em todos os módulos,

01:28

vamos passar pelas ferramentas que a gente vai usar no módulo.

01:31

Vou ler a descrição aqui,

01:32

porque a gente já está mais do que sabendo quais são essas ferramentas. Então,

01:37

temos aqui o OpenRBY, OpenCodeGo, LangFusePipeline,

01:42

que a gente vai usar dentro do OpenRBY.

01:44

Para a parte de Knowledge Base e MCP,

01:46

a gente vai usar o ChromaDB. Quando a gente sobe o OpenMBI,

01:49

ele automaticamente sobe um ChromaDB por trás,

01:52

que ele é um banco de dados voltado para o Vector Store.

01:57

O Vector Store vai servir para a gente construir uma Knowledge Base.

02:03

Essa Knowledge Base vai...

02:05

Usar a técnica de RAG para pegar e fazer uma pesquisa semântica e colocar

02:10

as informações dentro do contexto da AI para

02:13

a gente conseguir responder algumas coisas.

02:15

Vamos usar o FastMCP para desenvolver alguns servidores MCPs aqui,

02:22

dois servidores adicionais que eu vou falar deles aqui já já.

02:24

O MCPO que a gente usou na última

02:26

aula para a gente usar os MCPs de STDIO.

02:32

para fazer a conversão do STDI ou para o formato que o Open Web UI espera, ok?

02:38

K3D, que a gente vem usando desde a primeira aula, K8S MCP,

02:42

que a gente vai agora fazer uma mudança, né? A gente fez,

02:45

a gente deployou o MCP do K8S na última aula,

02:47

porém aquele MCP, ele é somente para consulta,

02:53

então é somente um read. Então agora a gente vai ter as oportunidades.

03:01

de fazer com que o MCP faça algumas requisições dentro do servidor, como rollout,

03:06

como reiniciar algum pod,

03:10

como trocar algum deploy e assim por diante.

03:13

A gente consegue fazer com esse Flux 159 aqui, que ele é um servidor MCP.

03:19

Vou mostrar para vocês, a gente vai atualizar aqui.

03:22

Prometer os MCP que a gente já tinha deployado.

03:25

Governance e Simulator, a gente vai ter um incidente MCP.

03:29

que a gente vai conseguir simular os incidentes. Na verdade, o incidente MCP,

03:36

a gente vai conseguir ter um ok de tipo assim,

03:40

ah, eu quero reiniciar um pod. Então,

03:44

antes de reiniciar esse incidente MCP,

03:47

vai conseguir fazer essa verificação para a gente. Tipo assim, ah,

03:53

você quer reiniciar? Ele vai pedir a confirmação para você, um approve ou um reject.

03:56

Então a gente vai conseguir documentar quando foi reiniciado alguma

04:00

coisa e quem aprovou e assim por diante.

04:02

Então a AI não vai tomar essa decisão de reiniciar sozinha.

04:06

Ela vai te sugerir e você vai aprovar ou não.

04:08

Então a gente tem um fault injection aqui,

04:11

que esse aqui de fato vai conseguir simular,

04:14

injetar um problema lá dentro do nosso serviço,

04:18

a API, para a gente conseguir simular as coisas.

04:20

E um template aqui de pós-mortem para a gente conseguir...

04:25

criar um pós-mortem após os problemas. Legal? Então,

04:28

na etapa 3 a gente vai construir, verificar a estrutura,

04:31

confirmar o end-to-end e no módulo 5 a

04:34

gente completa fazendo um teste de ponta a ponta. Ok?

04:38

Então, vamos lá.

04:39

Primeiro passo aqui é falar um pouco aqui de workflow de incidente.

04:44

Então, basicamente,

04:45

o ciclo completo aqui de resposta para incidente.

04:49

Então, o que a gente tem aqui?

04:53

Primeira parte, aconteceu um incidente, você vai detectá-lo.

04:57

Então, a gente vai detectar o incidente e vai disparar esse incidente. Então,

05:02

vou dar um exemplo aqui. Ah, quando aconteceu de um aplicativo seu cair.

05:07

Se a gente tiver serviços de monitoramento, igual o New Relic,

05:10

a gente tem serviços pagos no Datadog, etc.

05:15

A gente consegue detectar esse incidente.

05:18

Detectado o incidente, a gente vai fazer a triagem dele. O que é a triagem?

05:22

A gente vai classificar. Porra, o que caiu? Foi um exemplo,

05:26

um serviço crucial para a nossa operação?

05:30

Foi um serviço que roda ali em background, que não é tão essencial assim?

05:36

Vamos classificar a severidade, o impacto ali,

05:39

o escopo que aquele serviço que deu problema está atingindo.

05:44

Diagnosticar, investigar a causa raiz, olhar os logs, métricas e eventos.

05:49

aconteceram para acontecer aquele incidente, mitigar o evento,

05:56

que é aplicar a correção, rolling restart, se precisar, escalar pod,

06:01

fazer um patch do sistema, etc., para mitigar o erro.

06:04

Mitigar o incidente e subir o seu sistema de novo.

06:07

Confirmar a resolução, fazer os testes, ver se tudo funcionou,

06:10

restaurar o SLO e assim por diante. E um pós-mortem.

06:14

O que é um pós-mortem? Ele é o que aconteceu naquele acidente,

06:18

tudo descrito, quais são as ações que foram tomadas,

06:22

o que pode fazer para não

06:25

ocorrer de novo e assim por diante.

06:30

E o que a AI vai ajudar a gente aqui?

06:33

Ela vai conseguir agrupar os alertas correlacionados,

06:36

vai conseguir classificar a severidade automaticamente,

06:39

vai diagnosticar com consulta MCP para acelerar qual é o problema que está dando.

06:44

A gente vai conseguir identificar isso mais fácil.

06:46

Vai mitigar, sugerir executar um Rambock via RAG. Ele vai consultar o RAG,

06:53

ver quais são as operações para restabelecer o serviço

06:56

e vai fazer essa mitigação para a gente.

06:58

Vai resolver, confirmar o SNO restaurado e vai...

07:03

gerar o pós-mortem automático, gerar um draft,

07:06

ele vai gerar um rascunho do pós-mortem para a pessoa validar.

07:12

Então é isso aí que a gente vai conseguir ver.

07:14

E o que a IA não vai ajudar a gente aqui?

07:18

A IA vai amplificar,

07:20

mas não substituir o julgamento humano em situações críticas. Então,

07:25

ações que afetam muitos usuários ou dados sensíveis.

07:29

Decisão humana vai ser obrigatória.

07:31

Então, se for um serviço que vai afetar,

07:34

se você tem milhões de clientes,

07:36

se você tem um serviço que vai afetar esses milhões de clientes,

07:39

você vai tomar essa decisão, não a própria IA, ok?

07:42

Dados sensíveis, credenciais, segredos em logs e assim por diante.

07:45

O humano que vai validar esses vazamentos,

07:48

se ocorrer algum tipo de vazamento de dados,

07:50

de problemas aí dentro da aplicação que podem expor dados de clientes,

07:56

dados de funcionários e assim por diante.

07:59

Então sempre o humano vai avaliar esse tipo de vazamento.

08:05

E situações ambíguas, casos múltiplos, sem correlação clara.

08:10

O humano vai investigar e decidir.

08:11

Então pode ser que sejam vários problemas que ocorreram

08:17

que precisam de uma investigação um pouco mais a fundo,

08:21

porque ela não ficou tão clara. Então a gente tem um humano aqui decidindo também.

08:25

A IA pode tentar te ajudar, mas se ela não chegar a uma conclusão,

08:30

o humano vai ter que atuar. Então a regra vai ser,

08:32

a IA sugere, o humano decide em ambientes críticos,

08:36

a IA age apenas com um blast radius pré-aprovado.

08:41

Então você aprova para ela fazer, nunca ela faz automático.

08:45

Isso é sempre um bom uso para evitar que ela faça

08:49

alguma coisa de maneira automática que você não pediu.

08:52

Ela vai lá e simplesmente faz.

08:54

A gente evita problemas aí. Vai que já aconteceu, conta um caso,

08:59

já aconteceu de um amigo meu que ele tem um servidor

09:04

na casa dele que ele faz o deploy de várias coisas lá,

09:08

vários serviços para fazer um teste e, determinada vez, ele

09:11

pediu à IA para fazer a investigação do problema.

09:13

A IA identificou que o seu servidor está fora aqui.

09:18

Vou deletar tudo, vou deletar todos os servidores e vou subir tudo do zero.

09:21

Ou seja, ele perdeu todos os servidores dele.

09:24

Então, sempre que você for tomar alguma decisão crítica,

09:29

peça a confirmação antes. Então,

09:31

a gente vai implementar para a gente conseguir pegar essa confirmação humana antes,

09:35

Daí vai fazer qualquer coisa.

## Resumo IA

[RESUMO_IA]