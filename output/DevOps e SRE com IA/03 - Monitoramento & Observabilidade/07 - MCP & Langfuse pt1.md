Módulo: DevOps e SRE com IA\
Aula: [MCP & Langfuse pt1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18529)

## Resumo da aula



## Transcrição

00:00

Vamos lá galera, estamos de volta aí para a gente falar um pouco agora de MCP,

00:05

para a gente dar as capacidades aí para os nossos LLMs

00:10

conseguirem consultar dados externos e levar isso para o contexto dele,

00:14

para ele fazer análise para a gente, e o LangFuse,

00:19

onde a gente vai conseguir rastrear tudo o que o LLM fez ali,

00:24

tá bom? Então, o que a gente vai começar aqui?

00:30

Sobre o MCP,

00:31

ele é um protocolo aberto que funciona como uma camada

00:34

de padronização entre os modelos de AI e ferramentas externas.

00:39

Imagine assim, sem o MCP,

00:41

cada ferramenta precisaria de uma integração customizada com cada LLM. Beleza?

00:46

Com o MCP, a ferramenta expõe suas capacidades para o LLM. Então,

00:53

no formato padrão, padronizado ali, que é o do protocolo, do protocolo MCP. Ok?

00:57

Então, qualquer LLM compatível com chamadas de MCP consegue fazer a chamada.

01:03

Legal? Então, basicamente,

01:04

ele vai te dar possibilidades de fazer chamadas externas para

01:10

complementar o seu contexto ali para a AI te responder,

01:14

com o generative AI te responder. Tá? Então, a gente vai contar com dois MCPs ali,

01:19

tá? A gente vai contar com o primeiro MCP, que é o Kubernetes MCP Server,

01:24

tá bom? Beleza? Que ele vai expor algumas ferramentas como podlist,

01:29

para listar os pods, podlogs, para obter os logs específicos de um determinado pod,

01:34

eventlist, para pegar alguns eventos do cluster, deploymentlist,

01:38

para conseguir puxar a lista de deploys que tem dentro do cluster,

01:43

e cada um desses será uma tool que o LLM terá a capacidade

01:47

de chamar ela para pegar os seus resultados e complementar o seu contexto.

01:52

Teremos também o Prometheus MCP Server,

01:56

que ele vai me dar coisas como métricas, tipo, eu consigo fazer uma query lá dentro,

02:03

executar uma query com PromQL, que é o padrão de query que o Prometheus te entrega,

02:10

em intervalo de tempo. Então, se eu quiser pegar, tipo assim,

02:13

os últimos 30 minutos que meu serviço estava rodando,

02:16

eu vou conseguir fazer isso, tá?

02:18

conseguir pegar alguns metadados e algumas informações lá dentro do Prometheus.

02:23

Então ele tem um query range,

02:24

series, metadados e assim por diante que o Prometheus vai me entregar. Legal? Então,

02:31

agora que vem a parte poderosa da Generative AI ali,

02:35

que a gente consegue trazer coisas externas para dentro dela,

02:39

que você vai perguntar sobre, por que meu pote está com problema tal coisa?

02:44

Ele vai conseguir fazer as chamadas,

02:45

ele vai definir as chamadas que ele quer fazer, que ele vê que faz sentido fazer,

02:51

vai pegar o estado daquele container e vai te devolver o resultado.

02:56

E esse resultado,

02:57

ele vai fazer a análise em cima e você vai ler

02:59

essa análise toda para tentar entender o que está acontecendo.

03:03

Lembrando que sempre valide. Então,

03:06

ele vai te dar as informações e você sempre vai validar.

03:12

O LLM em si sozinho não vai conseguir fazer nada. Então,

03:15

a tool é muito importante para a gente trazer coisas de fora.

03:18

Tá bom? Então, basicamente, lá naquela primeira infra que a gente subiu,

03:23

da nossa infraestrutura aqui, a gente subiu um cara que chama MCP.

03:30

O que é o MCP? Deixa eu fechar essa parte aqui.

03:33

O MCPO, basicamente, ele vai conseguir pegar o protocolo STDIO.

03:39

que é um padrão de MCP que a gente tem, que a gente roda com o NPX,

03:43

e vai subir um container e vai rodar vários serviços ali de STDIO,

03:49

e isso vai ser disponibilizado para o OpenMBI,

03:53

que é a ferramenta de conversação que a gente vai usar aqui nessa parte.

03:56

Beleza? Então, o MCPO,

03:59

o OpenMBI não tem compatibilidade com o STDIO. Então,

04:04

o MCPO vai fazer essa tradução para o OpenMBI e

04:08

o OpenMBI vai conseguir consumir essas ferramentas aqui.

04:11

Então, é aqui na configuração do MCPO que a gente vai

04:15

definir quais são os MCP servers e vamos definir aqui Kubernetes,

04:19

Prometheus e aqui a gente conseguiu até o do lock também, que não está no slide,

04:24

mas a gente vai ter a possibilidade de usar um lock aqui. Legal?

04:28

Aqui a conexão com o cluster.

04:31

direto do Prometheus, a conexão com o cluster de observabilidade aqui do Lock,

04:36

a gente tem essa possibilidade, e aqui é a conexão com o Kubernetes.

04:43

Descendo aqui um pouco, a gente criou uma CFC Account aqui,

04:46

uma CFC Account para o MCPO,

04:48

que essa CFC Account, ela vai ter acesso a essas leituras aqui dentro do serviço,

04:55

que é tipo, consegue ler pods, verbs, etc, ele consegue puxar essas coisas,

04:59

e veja, que ele consegue fazer só consultas, tá?

05:03

Podemos colocar para ele conectar um pod? Sim, podemos colocar.

05:06

Mas aí, cabe um pouco de risco aí.

05:09

Legal? Então, aqui é o deployment do MCPO. Ele vai subir, basicamente,

05:14

o serviço lá e aqui é o service dele. Ok? Então, essa é a configuração do MCPO.

05:21

Ele vai servir somente porque a gente está usando o Open Web UI.

05:24

Se você estivesse usando um cursor...

05:27

um Cloud Code ou até o próprio Open Web UI,

05:32

vocês precisariam só desse arquivo aqui de configuração.

05:35

Mas como eu quis trazer o Open Web UI

05:38

aqui para vocês verem a capacidade dele também,

05:40

que é uma interface amigável, que a gente consegue usar, etc.

05:43

Eu coloquei o MCPO aqui para a gente usar lá dentro dele também. Combinado?

05:49

Aqui é o deploy do Open Web UI. Então,

05:51

a gente tem alguns detalhezinhos aqui. Aqui, por exemplo, nas variáveis de ambiente,

05:57

a gente já tem aqui o OpenMBI API base,

06:01

que basicamente está apontando para o meu host local,

06:05

onde está rodando o meu LM Studio. Sim, vamos usar o meu modelo local,

06:09

porque eu não vou conectar nenhum modelo em nuvem.

06:11

Vou usar o modelo local aqui,

06:12

que é aquele Llama que a gente vem usando nas últimas aulas aí.

06:16

Legal? Então, aqui o OpenMBI Secret Key.

06:19

que basicamente é só uma chave de aqui, eu coloquei esse aqui por padrão.

06:22

Então aqui a gente vai ter um Enable Hotel,

06:27

então ele consegue fazer os exports para o Hotel Collector,

06:31

beleza? Ele consegue fazer também essa parte.

06:34

A gente vai na próxima, na próxima, na próxima parte,

06:39

ver duas maneiras de fazer esse export aqui para o Hotel Collector.

06:45

Então essa aqui é uma maneira e a gente vai ter outra

06:48

possibilidade de a gente fazer esse export também da parte do OpenMBI aqui.

06:53

E lá dentro dele a gente vai configurar a parte de

06:57

conexão com os nossos serviços MCP que estão dentro do MCPO.

07:02

Então vamos lá.

07:05

Lembrando que essa stack já está toda deployada,

07:07

então quando a gente subiu lá no começo a

07:09

nossa infraestrutura de observabilidade mais o OpenMBY,

07:12

eles subiram todos juntos. Tá bom? Então,

07:15

está tudo conectado aqui e tudo deployado. Fechou?

07:21

Vamos para o nosso próximo slide aqui. Então, vamos lá.

07:29

Troubleshoots conversacional. Então, basicamente, eu consigo,

07:32

com esse cara, fazer algumas consultas. Então,

07:36

a gente consegue abrir o OpenMby e fazer algumas

07:40

consultas de qual pod que tem mais erros.

07:42

com a métrica de saturação dos últimos 30 minutos,

07:45

porque o deployer reiniciou e assim por diante. Então,

07:48

a primeira parte, nós vamos configurar o MCPO, desculpa,

07:51

o OpenMBUI com o MCP mais prometeus, usando o MCPO.

07:55

Vamos fazer três perguntas aqui e observar as chamadas das tools

07:58

e validar as respostas que contêm os dados reais,

08:01

ok? Então,

08:02

validar o pronto QL gerado pelo LLM e as levas ou funções que podem estar erradas,

08:09

tá? Então, a gente vai conseguir validar isso aqui também. Então, vamos lá,

08:13

vamos começar a nossa demo aqui para fazer esses testes com o OpenRBY.

08:18

Na primeira parte aqui, vamos fazer só uma checagem aqui,

08:24

ver se o nosso LM Studio está de pé,

08:25

está aqui, o serviço está rodando, vou dar uma limpada nos logs aqui,

08:29

o serviço está de pé,

08:30

rodando certinho, com o modelo Queen 3 .5, ok?

08:34

Está aí de pé, rodando dentro da minha máquina.

08:37

Então, se você configurou certinho lá... a parte de ingress,

08:42

a gente vai ter aqui um open, é o weby, né,

08:46

que eu dei o nome pra ele, .test 2 .8080.

08:49

Essa é a carinha do nosso open weby. Legal?

08:53

Deixa eu fazer só uma configuração aqui nele.

08:57

Não, não vou fazer configuração nenhuma por enquanto, não.

08:59

Vou só dar um oi aqui pro meu serviço.

09:02

Vou dar um oi pra ele. O nosso QIN 3 .5 aqui.

09:07

Legal? 3 .5, 50B, eu mandei um oi, ele me respondeu. Se a gente olhar nos logs aqui,

09:13

aqui está o nosso log da chamada que eu fiz agora.

09:17

Inclusive foi até bem rápido a chamada dele. Então vamos colocar um exemplo aqui.

09:23

Conte -me uma piada. Opa, coloquei piana, coloquei errado.

09:28

Claro, aqui está uma piada, já fez a resposta para a gente aqui.

09:32

Fechado? Então temos o Open Web UI respondendo através do nosso serviço local.

09:38

Ah, detalhe, aqui está desativado o Fink.

09:42

Vamos selecionar o perfil aqui de Fink,

09:46

ativar ele e vamos chamar de novo.

09:50

Vai ver se o Fink vai funcionar. Olá, como você pode me ajudar?

09:56

Então agora ele começou a pensar. Então, basicamente,

09:59

agora ele está usando o fim, que é a capacidade de pensamento dele,

10:02

que ele vai pegar esse texto meu, mandar para ele mesmo,

10:07

Sugerir respostas para ele mesmo,

10:10

Aumentar o contexto dele e me devolver o resultado.

10:14

Então, basicamente, ele fez isso e me trouxe esse texto aqui.

## Resumo IA

[RESUMO_IA]