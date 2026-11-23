Módulo: DevOps e SRE com IA\
Aula: [Ferramentas & Prática (Conectar MCP's)](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18515)

## Resumo da aula



## Transcrição

00:00

Agora, o próximo passo,

00:02

a gente vai conectar os MCPs lá dentro do OpenWebWire.

00:07

Lá já temos Kubernetes, K8S MCP, Prometheus MCP,

00:14

Fault Injection MCP, que a gente construiu no vídeo anterior,

00:21

e o Incident MCP que a gente acabou de colocar agora.

00:25

Vamos pegar aqui a URL dele e já vamos adicionar.

00:29

Lá dentro do nosso Open Web UI.

00:36

Então vamos aqui, painel do admin, configurações, integrações,

00:42

e vamos adicionar esse novo carinha aqui.

00:46

Então ele vai se chamar, vamos copiar,

00:50

colar o URL aqui, já está copiado, colei o URL.

00:53

Ele vai se chamar Incidente MCP.

00:55

Vou aproveitar que esse caso já está aberto, já copiar o nome aqui.

00:58

Incidente MCP, Incidente MCP, colocar a mesma descrição aqui,

01:02

tá? Testar a conexão. Ah,

01:04

deu problema aqui na conexão,

01:06

provavelmente porque está faltando parte da URL aqui.

01:08

Então é .svc .cluster

01:14

.local.

01:17

Ah, deu problema na conexão de novo.

01:20

Vamos entender o porquê? Vamos lá no Kubernetes.

01:25

Segue-se. A gente tem um Incident MCP aqui na porta 8000.

01:32

Vamos olhar lá por que está dando esse problema.

01:39

Incident MCP, CRVC, porta, cluster, ponto, local.

01:48

Está com problema aqui para salvar esse cara. Vamos copiar essa URL aqui.

01:53

Vamos dar uma olhada como está esse... Ah! Minto.

02:00

Faltou aqui uma parte. Vamos tirar aqui pra fazer um teste.

02:04

Vamos ver se só com o nome do... Acredito que só com o nome aqui do...

02:10

Do namespace ele já consegue conectar lá. Faltou um SSO aqui. Tá?

02:18

Opa, não funcionou.

02:22

Vamos ver como é que tá esse cara.

02:26

Ah, não é SSO não. Barra MCP. E eu tô configurando no lugar errado também, gente.

02:32

Estou configurando como OpenMPI. Aqui é diferente. Aqui é MCP.

02:37

Estou configurando no lugar errado. Nunca vai funcionar. Agora funcionou certinho.

02:41

Temos uma conexão bem-sucedida lá com o nosso serviço. Fechou? Então,

02:47

salvei. Temos o nosso MCP aqui com uma conexão bem-sucedida.

02:52

Podemos tentar fazer um teste aqui,

02:54

mas eu não garanto nada que vai funcionar. Vamos fazer um teste?

02:58

Vamos... Queen 3.5.

03:02

Vamos ativar aqui o nosso Incident MCP e o nosso Kubernetes. Agora,

03:08

o nosso Kubernetes tem a capacidade de fazer rollout, tá? Então, beleza?

03:12

Ferramentas ativas aqui.

03:14

Vamos aqui nas propriedades, nos controles aqui da nossa chamada.

03:21

E vamos ativar aqui a chamada de função nativa.

03:26

Então, vamos lá. Vamos fazer um teste aqui.

03:29

Vou pedir para ele fazer o rollout dos meus serviços aqui,

03:33

dos meus pods do meu app. Temos dois pods aqui, tá bom? Estão ambos como running.

03:39

Faz cinco minutos que ambos estão rodando.

03:42

Eu vou pedir para ele fazer o rollout restart desses carinhas aqui. Então, vamos lá.

03:48

Preciso fazer o rollout restart dos

03:56

Meus... do meu, né?

04:00

Do meu deploy app API deployment. Ok?

04:06

Vamos mandar para ele lá.

04:08

Vamos verificar o que ele vai fazer.

04:12

Então aqui ele me deu a resposta.

04:14

Me deu aqui um kubectl get.

04:17

O que ele trouxe?

04:19

Olha, ele trouxe aqui para mim todos os deployments que eu tenho.

04:23

Está tudo aqui listado. Legal?

04:26

Depois que ele trouxe, ele veio aqui. Ação pendente registrada. Ação alguma coisa.

04:32

Como esta operação é um rollout restart que pode acessar,

04:37

que pode causar interrupção temporária dos pods,

04:40

preciso de uma aprovação para seguir. Isso aqui que é o legal.

04:44

A gente consegue pedir à IA para fazer e pedir

04:50

para ela confirmar se você quer de fato fazer aquela ação.

04:53

Então aqui é uma ação, rollout, restart deployment API.

04:59

Pedi aqui, ele me deu o comando que ele vai rodar,

05:01

kubectl rollout restart deployment, o nome do pod, "-n",

05:05

que é o meu namespace. Ele me deu aqui impacto médio.

05:09

Pods serão reiniciados com rollout,

05:11

causando breve indisponibilidade durante o processo.

05:14

Vamos falar com ele que eu vou aprovar. Aprovado.

05:19

Vou mandar para ele que está aprovado.

05:22

Em teoria, ele deve continuar o processo de rollout dos meus serviços agora. Ok?

05:28

Registrou que sua aprovação foi registrada.

05:32

Agora vou executar o rollout restart.

05:36

Acabou de executar o rollout restart. Ele conseguiu reiniciar o meu pod.

05:42

Vamos ver? Olha lá, eles reiniciando aqui.

05:46

Legal? A gente tem um que reiniciou até 15 segundos e esse aqui com 6 segundos.

05:51

Então a gente conseguiu fazer isso tudo.

05:53

Com linguagem natural lá dentro do Kubernetes. Isso é muito legal,

05:57

porque a gente consegue fazer bastante coisas interessantes aqui.

06:03

Então, agora,

06:04

eu vou pedir para ele pegar o status dos pods para mim. Vamos

06:16

ver. Está pegando get, kubectl

06:19

get, kubectl get pods,

06:22

status detalhado do rollout. Olha lá,

06:26

os pods reiniciados, criados em...

06:32

4h39, 19 aqui,

06:34

provavelmente está no horário que é uma hora, está no horário 34.

06:39

Ele está no horário aqui de UTC. Então,

06:42

ele pegou aqui 4h e pouquinho da madrugada aqui.

06:48

Foi completado o rollout com sucesso. Escreveu errado aqui, né? Foi completamente,

06:54

não, está certo. O deployment foi completamente rolloutado com sucesso.

07:00

Ok? Então temos uma ferramenta que consegue registrar

07:04

as aprovações dos usuários e devolver todos esses dados

07:10

aqui e fazer ações dentro do cluster Kubernetes para

07:14

a gente facilitar nossa vida com linguagem natural.

07:16

Isso é super interessante para a gente, tá bom?

07:20

Próximo passo, vamos criar aqui no banco de dados.

07:22

Não tem como a gente fazer um teste breve aqui, mas não vai ser muito aplicado.

07:30

Vamos criar essas Keynote Base aqui, bem simples de fazer.

07:35

O nome da Keynote Base vai ser SRE Runbooks,

07:39

então vou copiar aqui do slide de uma vez.

07:41

Vamos voltar lá no nosso OpenRBI,

07:43

deixa eu colocar ele mais pertinho aqui para ficar mais fácil.

07:46

A gente vai vir aqui em espaço de trabalho, conhecimento e novo conhecimento.

07:51

Então a gente vai colocar SRE Runbooks,

07:53

vamos colocar somente uma descrição simples aqui.

07:58

Ele vai ser criado, ok?

08:00

Agora nós vamos adicionar os arquivos aqui do Runbook

08:04

que eu vou disponibilizar para vocês aí também. Legal?

08:09

Vamos pegar aqui os arquivos do Runbook.

08:14

Knowledge. Temos aqui quatro arquivos que a gente falou agora há pouco lá.

08:20

Vou precisar adicioná-los aqui.

08:24

Então vem aqui, carregar arquivo.

08:28

A gente aqui vem carregar arquivo.

08:31

Módulo 4. A gente tem aqui referência.

08:38

Dentro de referência a gente tem... OpenUI.

08:46

Knowledge. A gente vai recarregar esses quatro arquivos aqui.

08:49

Vamos subir eles aqui para dentro.

08:52

Já temos a nossa base de conhecimento pronta. Bem simples de fazer.

08:57

Ok? Base de conhecimento pronta. A gente pode vir aqui,

09:01

vamos colocar aqui, por exemplo, temos um agent aqui,

09:06

nesse agent que eu quero editar ele.

09:09

Vamos nesse agent e a gente pode selecionar a base de conhecimento aqui dentro,

09:14

SRE, Rambux, ou até os próprios arquivos diretamente, tá bom?

09:18

O mais interessante para a gente é selecionar a base de conhecimento como um todo.

09:22

Então, base de conhecimento criada, bem simples de fazer essa parte.

09:27

Vamos aqui atualizar o nosso Lengfuse Pipeline,

09:30

porque agora eu vou precisar

09:31

mandar informações adicionais para o Lengfuse.

09:37

Então eu vou colocar aqui, vou pegar as pipelines,

09:40

eu tenho o arquivo .filter aqui, Lengfuse Filter.

09:44

A gente já tinha criado ele na última aula,

09:47

no último módulo. Vamos aqui em painel do admin, funções,

09:52

a gente vai editar ele. Vamos simplesmente... copiar tudo e colar o novo aqui.

09:57

Vai estar disponível para vocês lá também.

10:00

Então colou.

10:03

Salvou. E pipeline nova disponível aqui do Lengfuse.

10:08

Já enviando as informações para lá. Ok?

10:12

Vamos aqui para o próximo. O que a gente vai fazer?

10:15

A gente vai criar três modelos aqui.

10:18

Lá dentro do OpenRUI. Um modelo de SRE Thresholder.

10:24

Que vai ter o System Prompt, Knowledge,

10:26

e as tools, os quatro tools que a gente tem de MCP.

10:31

A gente vai ter um Post-Mortem Generator, que vai ser o System Prompt,

10:35

mais Tool Incidentes, mais o Prometheus, mais o K8S,

10:42

e a gente vai ter o Health Monitor,

10:44

que vai ter Tools do K8S, Prometheus e Incidentes. Ok?

10:51

Vamos lá, vamos fazer a criação.

10:54

Bem simples também, a gente já criou alguns Agents na última aula,

10:57

então é bem simples da gente fazer a criação aqui.

11:01

Novo modelo, vamos selecionar aqui,

11:04

primeiro vai ser esse SRE Threshold aqui.

11:09

Copiar o nome dele, vamos dar o nome dele aqui em cima.

11:12

O modelo base vai ser o GPT-3.5.

11:15

Aqui no prompt de sistema,

11:17

eu já tenho algum prompt de sistema pronto aqui para esse...

11:22

para esse modelo que a gente está criando.

11:27

Então esse é o SRE Threshold, vou copiar o prompt dele aqui e

11:33

vou colocar aqui, tá bom? Temos alguns detalhes aqui do prompt, etc,

11:38

depois se vocês quiserem é bom parar aí e dar uma olhada melhor,

11:43

tá bom? Temos aqui os detalhes de tudo que ele vai fazer,

11:47

a orientação de que ele vai fazer.

11:49

Parâmetros avançados, vamos sempre habilitar aqui chamada de função nativa, ativo,

11:54

e lá a gente vai selecionar a base, o system prompt,

12:01

a base de conhecimento, o knowledge,

12:03

vamos selecionar o nosso knowledge e vamos selecionar

12:06

as quatro ferramentas conforme está descrito lá.

12:11

Beleza? Feito isso, salvei.

## Resumo IA

[RESUMO_IA]