Módulo: DevOps e SRE com IA\
Aula: [Demo Prática pt1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18549)

## Resumo da aula



## Transcrição

00:00

Fala pessoal, tô de volta aí.

00:03

Vamos para nossas demos aqui agora.

00:06

Vou executar cada passo, se algo quebrar. E pode quebrar, claro.

00:11

Sistemas, né? A gente sabe que pode quebrar o tempo todo.

00:14

Mas vamos debugar juntos, se acontecer alguma coisa.

00:17

E esta é a realidade da operação aí do dia a dia.

00:19

Se quebrar algo, você tem que ir lá e operá-lo,

00:23

e arrumar para voltar a funcionar. Tá bom?

00:27

E antes de começar a demo,

00:30

Eu vou deixar dois slides aqui de arquitetura como referência, tá bom?

00:34

Então, a arquitetura é a mesma que a gente construiu no módulo 4.

00:37

O Open Web UI vai ser o orquestrador central ali,

00:40

conectando a três modelos que a gente criou

00:43

dentro do próprio Open Web UI e quatro MCPs,

00:48

que a gente criou dois e fizemos a

00:52

importação de dois que já existiam aí na web,

00:55

a gente trouxe para dentro para usar junto com o MCP,

00:58

que faz parte ali do Open Web UI.

01:02

O ChromaDB vai ser o nosso Knowledge Base,

01:06

que a gente vai guardar nossos dados vetorizados,

01:08

e o LangFuse vai ser a nossa parte de auditoria.

01:14

A gente vai conseguir ver tudo o que aconteceu. Então,

01:17

quem quiser revisar os slides 9 e 10,

01:20

mostra um diagrama detalhado do que a gente tem de...

01:25

infraestrutura e do que a gente tem de arquitetura e dos nossos serviços. Ok?

01:29

Aqui é só a parte mais visual mesmo,

01:31

que eu estou mostrando aqui para vocês. Legal? Então, antes da gente iniciar,

01:38

vamos fazer só um checklist rápido aqui do que a

01:41

gente tem rodando lá dentro do nosso cluster,

01:44

tá bom? Então, nos dois primeiros pods aqui, temos o nosso serviço de App API.

01:51

Dois pods, o PostgresSQL e o Redis, que são usados dentro do App API.

01:57

Esses aqui são pods do kube-system, não interessa para a gente.

02:01

Esses aqui são pods do Prometheus,

02:02

também não interessa para a gente neste momento.

02:05

São pods que são criados quando o sistema é colocado aqui dentro.

02:09

Os pods de observabilidade aqui, do namespace de observabilidade.

02:13

Então, a gente tem um fault injection,

02:15

que é o que a gente vai inserir o problema dentro do nosso ambiente.

02:18

O problema será inserido dentro do App API, ok?

02:22

Temos o Grafana para fazer o dashboard, essas coisas de monitoramento.

02:27

Incidentes MCP, que é onde a gente faz as confirmações,

02:30

onde a gente consegue gerar a confirmação, se o agent for tomar alguma ação,

02:34

esse cara que vai fazer para a gente. A gente já tinha falado isso no módulo 4.

02:38

Temos o Lock, o Hotel Collect, onde a gente vai coletar os nossos...

02:42

os nossos dados e enviar para o Prometheus, que está logo aqui abaixo,

02:45

e o tempo para fazer alguns logs de auditoria.

02:50

Dentro do OpenMBI, do namespace e do OpenMBI,

02:54

a gente tem o LinkFuse, os dois LinkFuse estão rodando aqui dentro,

02:59

temos o MCP e temos o OpenMBI propriamente dito,

03:05

que está aqui rodando. Legal?

03:08

Um ponto, tá gente?

03:09

Essa distribuição foi o que eu achei que fez mais

03:11

sentido aqui para a construção da nossa aula. Porém,

03:15

você pode separar de diversas maneiras. Você pode criar um namespace para MCPs,

03:20

que a gente pode colocar MCPO lá dentro.

03:23

Você pode criar um MCP só para o OpenMUI, tá bom?

03:26

Vocês podem criar um MCP de observability para

03:30

colocar as ferramentas de observability lá dentro.

03:32

Igual a gente tem aqui esse observability, acabou que veio dois MCPs para cá também.

03:37

tá bom? Então, nome do namespace fica a critério de vocês,

03:41

se vocês quiserem mudar aí, beleza?

03:45

Pra testar mesmo, ver se tá funcionando, se tá tudo ok, legal?

03:49

Então, vamos lá, vamos passar aqui pra nossa primeira demo,

03:54

que já, opa, já tá aberta aqui já, vamos passar na nossa primeira demo aqui,

03:59

onde a gente vai fazer uma demo de OOM Killed,

04:05

dentro do nosso

04:07

Kubernetes dos nossos serviços lá.

04:09

Então a gente vai diagnosticar e tomar alguma ação.

04:11

Tá bom? Primeira parte, a gente vai injetar um problema.

04:16

Então injetamos o problema lá. Segunda parte,

04:21

a gente vai usar o agent que a gente criou de

04:23

SRE Troubleshoot para fazer o diagnóstico

04:28

via K8S MCP e Prometheus MCP.

04:33

Ah, aqui é troubleshoot. Eu tô falando o Trash World e tem algumas aulas,

04:38

né? Eu tava lendo errado.

04:41

Desculpa por esse erro aí, pessoal.

04:42

O nome do nosso agent é SRE Troubleshooter. Tô falando errado.

04:47

Então a gente vai ter o Incidentes MCP que

04:50

vai registrar que aquela action é pendente. Tá bom?

04:54

O humano vai aprovar via chat. Nós que estamos interagindo com o chat vamos aprovar.

05:00

E... O K8S vai fazer a execução do rolling restart aí pra restaurar o nosso S ali, ó.

05:06

Tá bom? Então, o que você vai ver? Comando de linguagem natural, a gente já sabe.

05:10

Pods entrando com um crash loop back off, tá bom?

05:17

Modelos diagnosticados ferramenta MCP.

05:22

Solicitação de aprovação, a gente vai ter aqui.

05:24

A gente viu isso aqui um pouquinho na última aula.

05:26

E aprovação humana e execução da correção, ok? Então,

05:30

vamos lá. Vamos aqui na primeira parte do nosso problema.

05:36

Do nosso demo, na verdade. O nosso problema vai acontecer agora.

05:40

Então, o primeiro passo aqui para a nossa primeira demo,

05:43

nós vamos selecionar aqui o modelo que a gente criou na última aula,

05:47

que é o SRE Troubleshooter. Beleza?

05:55

Vamos selecionar ele aqui. A primeira coisa que a gente vai fazer vai ser pedir.

06:00

para ele verificar como que está a saúde dos nossos pods.

06:06

Então vamos editar esse prompt.

06:08

Verifique a saúde do serviço app API no namespace demo app API.

06:14

Mostre o status dos pods e os SLOs atuais. Então vamos lá.

06:21

Espera ele responder aqui.

06:23

Lembrando que eu estou usando o modelo localmente na minha máquina,

06:26

rodando aqui dentro do meu computador.

06:31

Então, vocês podem usar modelos além desse também, tá?

06:35

Vocês podem usar modelos aí de clouds e assim por diante. Que, inclusive,

06:40

a resposta provavelmente pode ser até mais rápida do que a minha aqui.

06:44

Então, ele já está começando a executar aqui, fazendo a chamada de algumas tools.

06:48

Fez a chamada de várias aqui, inclusive, juntas.

06:52

Vamos ver se ele colocou.

06:54

Os pods com deployment appi não foram encontrados.

06:58

Vou listar o recurso namespace. Vamos ver aqui.

07:02

Agora vou obter mais detalhes. Está obtendo alguns detalhes do pod aqui. Ok.

07:13

Olha, notei que o deployment de ambiente tem um clash loop inject,

07:18

que indica que é uma falha injetada para demonstração.

07:21

Vou investigar o pod. Então, ele está investigando aqui.

07:26

Ficou alguma variável lá solta que está errada, inclusive.

07:30

Essa variável não deveria existir. Mas tudo bem. Ele está verificando.

07:35

Está vendo, falando aqui que as métricas não estão retornando nenhum dado. Vamos

07:43

aguardar aqui ele dar o resultado.

07:46

Ele verificou se o Prometheus está funcionando.

07:51

Então, ele fez várias chamadas aqui de tools.

07:55

Está vendo que ele consegue encadear várias tools aqui para fazer essa chamada.

08:00

Ele fez até um search aqui no Knowledge Base. Que bacana.

08:03

Ele explorou o search aqui no Knowledge Base. Ok.

08:14

Ele está respondendo o resto lá agora.

08:17

Deixa eu ver o que ele explorou aqui no log de base.

08:21

Explorou algumas coisas aqui no log de base. Então, vamos lá. Status, serviço e API.

08:25

Então, ele retornou aqui os dois pods. Temos aqui running e o criado em.

08:30

Os dois pods estão rodando com o 2 de sucesso.

08:35

2 / 2 com ready. O nome aqui do nosso deployment.

08:41

As réplicas. Tem duas aqui, duas atualizações, total, algo assim por diante. Strategy.

08:48

Health check de performance, o log dos pods mostram apenas respostas saudáveis,

08:53

como latência, excelentes e assim por diante.

08:56

Alertas de evento, então aqui, third get resource metric horizontal,

09:01

o pod não consegue obter métrico de CPU,

09:02

porque o pod não tem request de CPU configurada.

09:07

Interessante, a gente achou algum, podemos achar algum probleminha aqui, nesse caso.

09:13

Prometheus, health up.

09:16

Data de scrap, alguma coisa assim, e os SLOs atuais. Então, infelizmente,

09:21

as métricas do Prometheus não estão retornando dados aqui.

09:23

Tivemos um problema aqui com as métricas do Prometheus.

09:27

Provavelmente ele não está enviando os dados lá para dentro do pod.

09:31

Mas isso aqui não há problema. A gente configura depois e consegue ver isso aqui.

09:37

Então, algumas recomendações que ele deu aqui.

09:42

Verificar se o app... exporta métrica,

09:44

confirmar que a aplicação está exportando as métricas de latência em erro,

09:47

para o endpoint, métricas, depois a gente pode verificar isso,

09:51

configurar o request de CPU,

09:53

adicionar request de CPU e deployment, aqui já deu uma recomendação,

09:58

e remover a fault injetada aqui,

10:02

se o crash loop reject true não for necessário,

10:07

removam, remover das variáveis, ok?

10:13

Deixa eu recarregar o chat aqui, para ver.

10:17

Ah tá, faltou um pedacinho, o chat não completou.

10:21

Remova, cadê? Aqui ó. Se for necessário, remova do ambiente.

10:25

Validar o Cephs Monitor,

10:27

Verificar se o Cephs Monitor está configurado corretamente para coletar as métricas. Ok?

10:32

O estado geral operacional pode estar rodando,

10:34

Com os cheques passando, tudo certinho.

10:37

Temos o nosso pod rodando, que é o que importa pra gente nesse momento, beleza?

10:42

Então, na próxima etapa aqui, nós vamos fazer a injeção,

10:49

Injetar dentro do pod um problema, tá?

10:53

Então, como que a gente vai fazer isso?

10:56

Nós vamos pedir para o nosso...

11:01

Deixa eu achar aqui.

11:02

Na verdade a gente não criou um agent específico para esse cara. Então vamos...

11:08

Deixa eu dar uma olhada. Vamos dar uma olhada aqui.

11:11

Porque eu não me lembro, não me recordo.

11:15

Essa aí é troubleshoot. Vamos ver se ele tem aqui a parte de inject.

11:22

Fault inject está selecionada.

11:24

Nós podemos pedir para aquele chat lá mesmo fazer o fault inject. Ok?

11:30

Vamos voltar aqui naquele chat, está aqui em cima.

11:33

Então, simule. Vamos lá.

11:36

Simule um OOMKill LED

11:42

no app -api. Vamos fazer uma simulação aqui.

11:49

Vamos mandar aqui para ele.

11:55

Guardar a resposta. Como tem muitas ferramentas aí,

12:01

ele está demorando um pouquinho para processar e

12:03

o nosso contexto está ficando bem grande.

12:05

Tá bom? Então vamos aguardar um pouquinho para ele fazer o processamento.

## Resumo IA

[RESUMO_IA]