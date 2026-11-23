Módulo: DevOps e SRE com IA\
Aula: [Ferramentas & Prática](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18540)

## Resumo da aula



## Transcrição

00:00

Então, pessoal, retornamos aqui para a gente falar um pouco das nossas ferramentas e práticas aqui.

00:06

Vamos passar por algumas teorias e depois vamos fazer o deploy do resto das

00:12

ferramentas que a gente vai usar para o nosso troubleshoot de ponta a ponta.

00:17

Na etapa anterior, a gente criou o MCP,

00:23

que a gente consegue injetar problemas dentro da nossa ferramenta

00:27

para a gente simular problemas que vão ocorrer.

00:30

aí dentro do nosso ambiente. Ok?

00:32

Então agora vamos para os próximos aqui falar de algumas coisas que

00:36

a gente precisa saber antes de fazer a criação do restante.

00:39

Ok? Então vamos lá.

00:42

A RAG sobre os Runbooks.

00:45

Agora a gente vai entender como o próprio OpenMBI consegue consultar os

00:49

Runbooks via Keynote Base para fazer

00:53

um enriquecimento do contexto do Generative AI.

00:59

para montar algumas ações mais assertivas,

01:06

tá bom? Então,

01:08

o Key Knowledge Base, ele é padrão do OpenAI,

01:11

quando você sobe ele, ele já cria para você um ChromeDB por trás,

01:15

já tem um modelo de open source aí que faz

01:18

embed da informação e guarda essas informações lá,

01:21

tá? Basicamente aqui,

01:23

a gente vai subir quatro arquivos .md de Chromebook,

01:29

que são eles, né? O primeiro vai ser o OOMKilled,

01:34

que são os procedimentos para pod com status de OOMKilled,

01:38

incluindo diagnóstico de uso e de memória

01:41

e recomendação de resources de limits aqui,

01:46

tá bom? Vai ter também um runbook de Crashloop Backoff,

01:51

que são os procedimentos para pods com esse erro, com Crashloop Backoff,

01:55

cobrindo a verificação de logs, configuração e dependências.

02:01

Um high latency, que tem um procedimento para latência alta,

02:05

incluindo a verificação de dependências, downstream,

02:08

conexões com banco de dados e assim por diante. E database connection,

02:12

que é um procedimento para problemas de conexão com banco de dados,

02:16

incluindo connection pooling e timeouts com banco de dados.

02:22

Então o fluxo vai buscar lá dentro do nosso banco de dados,

02:29

do nosso ChromaDB, por aproximação, de acordo com a pergunta do usuário,

02:34

de acordo com o contexto do usuário, vai trazer essa informação de volta, tá bom?

02:39

E vai entender o que o usuário está falando ali e vai tomar ações em cima daquilo.

02:44

Legal? Então,

02:46

nós vamos criar uma RAG aí,

02:52

uma Keynote Base com esses Runbooks que eu comentei aqui. Legal?

02:56

Para o próximo aqui, o OpenMBA é a nossa interface de chatops.

03:00

Então, a gente está definindo isso aí desde o modo anterior.

03:03

Então, toda a interação com o sistema vai acontecer via chat com linguagem natural.

03:08

A gente já tinha falado disso também. Então, comandos como simula o homenagem,

03:13

kill it no app, qual o status do meu pod, aprovar ação pendente,

03:19

gerar pós-morte no incidente de ontem.

03:22

Todo em português ou em inglês a gente pode

03:24

mandar lá que o LLM vai conseguir entender.

03:27

Mas isso pode ter algumas ações aí que exigem confirmação.

03:33

Então se eu pedir para ele fazer um rollout em alguma coisa,

03:35

a gente precisa confirmar e assim por diante.

03:39

Então a gente vai criar também uma parte aí que a gente

03:43

vai exigir algumas confirmações do usuário

03:48

que está operando ali o agent para...

03:52

para dar seguimento na ação. Então, por exemplo,

03:54

quero fazer o rollout restart do pod X. Então, você vai confirmar.

04:00

Confirmado, você vai reiniciar aquele pod.

04:02

Ok? Então,

04:04

a gente tem aqui o serviço que a gente vai fazer o deploy daqui a pouquinho, que a gente vai falar.

04:09

A roda diagnóstica de tal API. Ele vai te falar aqui qual que é o diagnóstico.

04:13

Aí você vai mandar o user.

04:16

Rollout restart API deployment. Ele vai fazer.

04:20

Ele vai perguntar seu pedido de aprovação,

04:22

você vai fazer, vai falar que vai aprovar,

04:24

user approve e o rollout será feito aqui. Legal?

04:27

Isso tudo através de ferramentas de MCP.

04:32

Então, uma coisa que é legal do ChatOps, ele vai democratizar o acesso.

04:39

A gente pode liberar o acesso para várias pessoas aí.

04:41

Qualquer engenheiro pode ir lá, fazer o diagnóstico,

04:44

testar e assim por diante. Legal? E tudo vai ficar registrado.

04:49

A gente vai registrar tudo através do LingFuse.

04:52

A gente vai fazer algumas atualizações naquela pipeline que a gente criou

04:55

na aula passada para o LingFuse e vamos fazer tudo ser registrado lá.

05:01

Tudo que ocorrer será registrado lá. Tá bom?

05:06

Vamos falar aqui agora do pós-mortem automático. Então,

05:10

o modelo do pós-mortem automático consome múltiplas fontes de

05:14

dados para gerar rascunho de audit log e de incidentes.

05:18

Legal? Então, se você aprovou, quem aprovou,

05:21

por que aprovou e assim por diante. Os três do LingFuse,

05:25

a AI diagnosticou e sugeriu. Então,

05:29

a gente consegue pegar basicamente tudo o que foi sugerido. Tudo que foi aprovado,

05:36

tudo que foi diagnosticado e colocado no nosso pós-mortem. Tá bem?

05:39

Então o resultado é um rascunho completo com esses cinco W's aí,

05:44

né? Pra fazer os cinco porquês, né?

05:48

Pra fazer o nosso pós-mortem aí,

05:52

tá? Então o rascunho vai incluir resumo do incidente,

05:56

timeline dos eventos com timestamp, análise dos cinco W's com causa raiz,

06:03

métrica de impacto, duração, os olhos afetados e assim por diante,

06:08

e as ações de itens sugeridos, tá bom? O LLM vai fazer cerca de 80% do trabalho,

06:15

que vai te entregar ali 80% do trabalho pronto,

06:19

e você vai precisar somente refinar e fazer os ajustes humanos ali,

06:24

com contexto institucional.

06:27

Qual que são os serviços que podem ter parado,

06:29

qual que foram os impactos no ambiente,

06:31

na instituição e assim por diante. Ok? Então,

06:35

a gente consegue adiantar bastante um assunto aí. Então,

06:39

aqui o pós-mortem vai ser gerado para a gente de maneira automatizada. Ok?

06:45

Então, temos algumas ferramentas de mercado que fazem tudo isso já prontas.

06:52

Então, a gente tem aqui o RotoAI.

06:56

Que faz a summarização de incidentes em tempo real, timeline automática,

07:00

ação sugerida e assim por diante. Então, a gente consegue integrar com OpenUI,

07:06

etc, PGDurry e assim por diante. Temos Incidente.io AI,

07:10

que a gente consegue fazer agrupamento de alertas, correlacionados,

07:15

resumo em linguagem natural e um pós-mortem gerando também automaticamente.

07:20

E a gente tem o PGDurry AIOps,

07:23

que também... A gente consegue fazer um agrupamento inteligente de alertas,

07:27

supressão de ruídos, se tiver algum problema, tiver algum texto errado,

07:33

etc., ele consegue ajudar isso com a gente.

07:35

Porém, na nossa demo, a gente vai construir o nosso próprio sistema,

07:37

com o OpenWebWire, FastMCP,

07:40

com os quatro MCPs que a gente está colocando, mais a Knowledge Base,

07:44

sem depender de um SaaS, sem precisar, em teoria, pagar.

07:48

Um SaaS para isso. Então, que é isso que a gente está construindo aqui,

07:51

umas ferramentas de monitoramento diagnóstico com AI,

07:56

AIOps ali por trás. Legal? Então, agora a gente vai fazer o deploy,

08:01

a configuração da nossa stack aqui.

08:03

Legal? Então, faltam algumas coisas para a gente fazer o deploy. Então,

08:07

a gente vai iniciar aqui no número 1 do Incidentes MCP.

08:12

O que é o Incidentes MCP? Basicamente, a gente vai ter algumas ferramentas aqui.

08:16

Approve Action. Reject Action, Registrando Action, Queue Switch,

08:23

Check Queue Switch e Get Audit Logs. Tá bom? Então, basicamente,

08:28

a gente vai ter essas ferramentas para fazer a aprovação de uma ação,

08:33

alguma coisa ali, se pedir para fazer um rollout,

08:35

restart, etc. A gente vai fazer o deploy desse cara agora.

08:39

Depois a gente volta aqui para fazer o restante dos nossos serviços,

08:44

da nossa stack, né?

08:46

Então... Primeira coisa,

08:48

a gente vai fazer o deploy igual a gente fez lá do inject fault.

08:53

Então vem aqui observabilidade,

08:54

observability. Aqui a gente tem um fault inject.

08:57

E a gente vai agora inserir aqui o nosso incident MCP. Ok?

09:04

Vai ficar aqui dentro de referência.

09:07

Coloquei no lugar errado aqui. Referência.

09:12

Ok. Temos aqui o incident MCP. Temos aqui um deploy .sh,

09:17

basicamente igual ao do outro. Tô trocando os nomes aqui.

09:21

Temos aqui um Dockerfile, simples também, só simplesmente fazer a instalação,

09:26

subir no arquivo .py ali. Os requirements,

09:29

a gente precisa só de um FirstMCP aqui e as tools que a gente tem aqui.

09:35

Então aqui a gente tem definição de todas as tools que eu falei lá dentro do slide, tá?

09:41

Então registro -present -actions, a gente tem aqui approve -actions,

09:45

a gente tem um reject -actions.

09:52

QSuite, CheckQSuite e um GetAuditLog, tá bom?

09:56

Então a gente consegue fazer toda essa parte aqui com esse

10:00

serviço MCP que a gente vai ter disponibilizado lá dentro do OpenMPUI,

10:05

tá? Aqui a gente tem o deployment dele,

10:08

bem simples também, né?

10:10

O arquivo manifesto Kubernetes deployment aqui pra gente colocar,

10:13

vai dentro do MSP de observability e aqui a gente tem o serviço dele, é um service lá

10:18

que vai se chamar incident-mcp dentro também do Observability, ok?

10:23

Então vamos fazer agora o deploy dele. Vamos dar um ponto barra, referência,

10:28

vou deletar aqui que eu aproveitei o comando,

10:32

então a gente vai chamar esse cara aqui de incident-deploy.sh.

10:37

Então, bora fazer esse deploy. Build da imagem,

10:41

vamos subir a imagem aqui para o nosso Docker Desktop.

10:51

Feito isso, ele vai exportar a imagem agora lá para o cluster Kubernetes nosso,

10:56

nosso cluster K3D, que está rodando.

11:00

Ok, temos o nosso serviço pronto lá.

11:06

Teoria, se a gente vier aqui no Kubernetes,

11:08

temos o nosso serviço deployado aqui. Então vamos aqui no serviço, namespace,

11:15

Observability, temos o nosso serviço aqui de...

11:20

Incidentes MCT em funcionamento 100%.

11:23

Combinado? Então temos o serviço pronto.

## Resumo IA

[RESUMO_IA]