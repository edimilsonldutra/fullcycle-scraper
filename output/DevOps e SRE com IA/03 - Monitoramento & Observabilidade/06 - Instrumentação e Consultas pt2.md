Módulo: DevOps e SRE com IA\
Aula: [Instrumentação e Consultas pt2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18511)

## Resumo da aula



## Transcrição

00:00

Feito isso, a gente já tem essa nova branch criada aqui.

00:03

Vamos vir aqui em Code. A gente vem em Branches.

00:07

Temos a nossa nova branch criada. Então, aquele padrão que a gente sempre faz,

00:12

né? Vamos vir aqui em Actions.

00:14

Desculpa, Actions não. Pull Request.

00:17

Criar um novo Pull Request.

00:20

Selecionamos aqui a branch, né? Adicionando Observabilidade App API.

00:24

E dá um Create Pull Request aqui. Ok?

00:27

Vamos pegar esse título aqui e adicionar aqui no

00:30

comentário e dar um create pull request.

00:33

Automaticamente feito por pull request, ele vai iniciar uma action aqui.

00:38

Deixa essa action iniciar aqui certinho.

00:42

Vamos ver se iniciou. Recarregar a página. Ó,

00:45

temos as nossas actions aqui iniciadas. Ok?

00:49

Aqui é o nosso LMS Studio,

00:51

daqui a pouco o agent de segurança vai fazer algumas chamadas aqui,

00:54

mas vamos ficar de olho aqui na nossa Validate AutoCollector.

00:58

Inclusive já validou. Fez aqui uma validação, lint, Run Auto Instrumentation Test.

01:04

Vamos ver o que ele fez os testes aqui. Ah,

01:07

ele conseguiu fazer os testes de toda a stack nossa do OpenTelemetry.

01:12

Então ele fez o teste de todas as funções

01:14

do OpenTelemetry e passou de tudo com sucesso. Ok?

01:18

Então, nessa parte de teste,

01:19

a gente consegue validar se o OpenTelemetry está

01:21

de pé e está funcionando corretamente. Legal?

01:25

Aqui a gente está adicionando a observabilidade,

01:28

igual a gente tinha feito na aula passada.

01:31

Deixa ele terminar aqui, fazer o comentário lá dentro do nosso pull request.

01:35

Vamos esperar esse comentário vir aqui.

01:38

Ok. Vamos só aguardar o comentário aparecer que está rodando aqui.

01:43

Vou abrir uma nova aba para a gente acompanhar e ver o comentário aparecendo.

01:47

Aqui já veio só na scan.

01:49

Agora está rodando o Security Agent aqui no cantinho.

01:52

Rodando aquele esquema que a gente fez via Python.

01:55

Agora está rodando aqui, coletando lá dos outros serviços que rodou,

02:01

do Trivi e do Sonar,

02:03

e fazendo avaliação com AI. Se a gente vier aqui no LMS Studio,

02:07

a gente está gerando alguns tokens aqui em cima,

02:09

igual a gente aconteceu na aula. Então,

02:11

nossa esteira continua a funcionar bacaninha e adicionamos só mais

02:14

um job em paralelo nela que está rodando.

02:18

da parte de teste do OpenTelemetry.

02:22

Ok, finalizado nossos testes,

02:25

agora a gente vai fazer um merge por pull request.

02:29

Vamos colocar aqui, fazer o merge por pull request.

02:33

Ok, merge por pull request feito, e a gente tem as nossas actions aqui rodando.

02:38

Agora, vamos fechar essa aba que a gente abriu.

02:40

Temos a nossa action aqui rodando para fazer o deploy.

02:43

Ok? Então, assim que o deploy terminar,

02:47

Eu volto aqui com vocês para a gente fazer o rollout lá dentro do nosso ambiente.

02:53

E verificar se os serviços estão rodando certinho.

02:57

E enviando os traces lá para dentro do OpenTelemetry, ok?

03:03

Ok, pessoal, deploy aqui finalizado.

03:06

A gente já aplicou tudo lá nos ambientes,

03:11

Ok? Vamos dar uma olhada aqui na nossa aplicação.

03:16

Dentro do ITM aqui, a gente vai abrir aqui o nosso Kubernetes,

03:21

Ok? Temos a nossa aplicação aqui,

03:23

Ela não foi reiniciada sozinha, então vamos dar uma reiniciada nela aqui.

03:29

Ok, vamos olhar.

03:33

Aparentemente tudo certo com a aplicação,

03:35

Então a gente implementou aí a parte de tracing,

03:38

Provavelmente o tracing lá está sem o verbose, sem o debug ativado,

03:44

Em teoria, ele está mandando já o OpenTelemetry.

03:47

Vamos dar uma olhada aqui no OpenTel,

03:48

Ver se a gente está conseguindo ver alguma coisa. Provavelmente,

03:51

Igual eu disse, como está sem o debug,

03:54

Como está desativado, ele não aparece nada aqui.

03:58

Prometheus também não tem nada. O tempo aqui está rodando algumas coisas.

04:03

E o lock também algumas coisas aqui.

04:06

Então, o que a gente vai fazer agora para a

04:09

Gente conseguir ver se está mandando de fato?

04:11

Vamos lá no nosso Grafana.

04:15

Então, o Grafana, como a gente colocou... Ah,

04:19

Deixa eu deixar uma coisa clara para vocês aqui.

04:21

A gente adicionou o Ingress. O que é o Ingress?

04:25

Tudo que vem de fora do seu cluster, ele entra pelo Ingress, pelo Kubernetes.

04:31

Então, o Ingress é a porta de entrada para as coisas externas.

04:35

Então, a gente adicionou o Ingress para a

04:36

Gente conseguir acessar os serviços do Grafana,

04:40

Os serviços ali do Lock, essas coisas de forma externa,

04:43

Para a gente conseguir usar a UI deles,

04:47

Ok? Tanto para o Grafana,

04:49

Quanto para o Web UI e os serviços que têm

04:53

A possibilidade de usar a interface web dele aí por fora,

04:58

Ok? Então, o que a gente vai fazer? Aqui dentro do Ingress,

05:03

A gente consegue dar um nome para ele. Então,

05:06

Vamos aqui pegar o nosso Ingress do Grafana.

05:08

Então, o nome dele é grafana.teste,

05:12

O nome da URL dele. Vamos vir aqui,

05:16

Amgattp://grafana.teste

05:21

.2.8080.

05:24

A gente mapeou tudo na porta 8080.

05:28

Erro de certificado, ok.

05:31

O aparelho deu safe.

05:33

Barra e o Y.

05:37

Ok, temos um problema aqui. Vamos ver qual é o problema.

05:43

Vamos ver o problema.

05:46

O Grafana está com um problema.

05:49

Deixa eu dar uma investigada aqui. O problema... Deixa

05:54

Eu ver...

06:00

Ó, abriu aqui agora. Peraí, deixa eu ver o que eu tinha digitado. Ah,

06:04

eu tinha colocado HTTPS, só que lembrando,

06:07

a gente não está trabalhando com nenhum certificado aqui agora.

06:11

Então a gente está fazendo só um HTTP e estamos aqui dentro do Grafana.

06:16

A senha inicial sempre é admin, admin,

06:19

ele vai pedir para você alterar no primeiro login,

06:21

eu já fiz isso. E a gente tem a nossa telinha do Grafana aqui. Ok?

06:26

Aqui na parte de connections, a gente tem a parte de data source,

06:30

que isso já é configurado quando o Grafana faz o deploy. Quando a gente faz o deploy,

06:35

a gente já consegue configurar alguns data source padrão. Então,

06:37

como a gente está usando esses três serviços aqui,

06:40

a gente já configurou esses três serviços para vim. Legal?

06:44

Vamos ver aqui se no lock a gente tem alguma coisa.

06:46

Não, no lock a gente não tem nada ainda,

06:48

porque lembrando, a gente está colocando só logs aqui, aqui no Prometheus.

06:53

A gente não tem nada ainda por enquanto.

06:56

Aqui é a parte de métricas. E aqui no tempo. A gente tem.

07:02

Aqui a gente consegue ver. Os tracers certinho vindo aqui.

07:06

Tracer ID. Ver o que ele chamou. Então a gente consegue.

07:11

Ver que o health está sendo enviado. Está funcionando tudo certinho. E em teoria.

07:15

Quando eu fizer um curve para o URL. Do meu serviço.

07:20

Vamos fazer um teste aqui. Vamos

07:25

fazer um curr aqui.

07:26

Isso aqui é só a parte que mostra que a gente está gerando a documentação aqui,

07:30

a documentação não, né? A instrumentação, usando o telemetry .py aqui,

07:35

rodar o app, mais autocollect via K8s kubesupply, beleza?

07:41

Via Kubernetes,

07:43

ok? E enviar um request para testar no tempui,

07:49

ver os spans do tempui, ok?

07:53

Vamos fazer esse request aqui para a gente validar o funcionamento.

07:57

Vamos abrir uma nova abinha aqui e fazer um request do nosso serviço.

08:03

Ok, temos um problema de localhost 8000.

08:09

Vamos dar uma olhada,

08:10

ver se o serviço está certinho lá e exposto na porta dele. Vamos ver aqui.

08:19

Opa, aqui.

08:22

Vamos aqui no Kubernetes.

08:24

vamos ver o serviço service olha temos o appdata

08:31

aqui exposto na porta 8000 http 8000 tá aqui

08:37

exposto dentro do namespace tudo certinho então em teoria

08:43

local roxo 8000 não deveria

08:47

funcionar em teoria porém todavia

08:52

Vamos olhar aqui o nosso network policy.

08:55

Aqui o nosso network policy,

08:57

ele tem uma definição aqui do que pode entrar e o que pode sair.

09:03

Então aqui a gente tem um network policy, que é o ingress,

09:07

a partir de, pode entrar na porta 8000.

09:11

Então em teoria era para funcionar. Quando a gente tem isso aqui,

09:15

a partir de qualquer lugar, a gente pode chegar na porta 8000.

09:22

para todos os lugares. Namespace selector e todos os lugares aqui.

09:26

Então, em teoria, era para funcionar aqui.

09:30

Só que aqui a gente está falando do Ingress.

09:32

A gente tem Ingress criado para o nosso app?

09:35

Acredito que não. Vamos dar uma olhada. Vamos dar uma olhada lá. Vamos ver. Ingress.

09:40

A gente tem dois Ingress. Um de observabilidade e um de... e

09:47

um Ingress do OpenRBY.

09:49

Porém, a gente não tem nenhum Ingress do nosso app test.

09:54

Então, vamos criar um Ingress aqui?

09:56

Vamos criar na mão mesmo para a gente ver como vai funcionar esse Ingress.

10:00

Então, vamos dar aqui um git checkout main.

10:05

Eu fiz uma mudança aqui. Essa mudança não era para ser feita. Eu colei sem querer.

10:10

Git checkout main.

10:13

Vou atualizar a policy aqui do antigo app nosso.

10:19

A policy vai ter que ser aquela menos restrita,

10:22

que eu tinha gerado aqui no nosso stack de observabilidade.

10:28

Eu vou colocar ela aqui também,

10:29

para a gente não ter problema aqui de conexão.

10:32

Então, eu vou colocar essa policy aqui.

10:33

Não era para ter atualizado naquela hora, mas agora a gente precisa dela.

10:37

A policy vai simplesmente liberar que o cluster se comunique todo entre si.

10:42

Aqui dentro de K8s, vamos gerar um novo arquivo aqui.

10:51

Nesse Ingress, vamos pegar o de exemplo que a gente tem lá dos outros serviços.

10:56

Vamos vir aqui, a gente tem um Ingress aqui de exemplo.

11:01

Bacana, temos um Ingress aqui de exemplo. Vamos copiar ele aqui.

11:05

Namespace, nome, observability Ingress.

11:08

Vamos colar ele aqui e vamos fazer juntos esse Ingress aqui para o nosso app API.

11:15

Ele estava funcionando antes em localhost,

11:18

porém agora a gente usando o Ingress e fazendo os ajustes dentro das portas,

11:24

fazendo os ajustes das portas, ele passou a dar problema.

11:28

Então, vamos criar um Ingress e até dar um nome para ele. Legal?

11:31

Então, vamos lá. Qual vai ser o nome dele? Vai ser app -api

11:36

-ingress. O namespace vai ser,

11:42

vamos pegar o namespace que está rodando o nosso pod.

11:46

Temos aqui, pod, a gente tem o namespace demo -app -mba.

11:53

Esse é o nosso namespace. Vamos colocar aqui,

11:56

que esse cara vai ser feito o deploy lá dentro.

11:59

Notation, traffic Ingress Kubernetes -houtend .web. A gente já está tudo certinho.

12:05

Aqui as várias rotas,

12:07

vários hosts que a gente pode adicionar dentro do nosso Ingress.

12:11

Então, vamos arrancar todos esses.

12:13

E vamos manter somente o que faz sentido para a gente.

12:20

Tirei... Peraí que eu tinha tirado errado, se eu não me engano.

12:24

Vamos ver. É daqui para baixo. Eu não preciso do Prometheus para baixo.

12:28

Então, Prometheus para baixo. Tchau. Foi embora.

12:31

Então, agora a gente tem um aqui.

12:34

App API

12:36

ponto teste. Esse vai ser o nosso DNS.

12:40

Ok? Esse, a partir de agora, vai ser o nosso DNS. Então, aqui um path.

12:45

Prefixo barra, então ele não tem nenhum prefixo.

12:49

Backend, service. Vamos lá pegar o service do nosso serviço,

12:52

para a gente apontar para o nosso service.

12:55

Vamos colocar service aqui. Então a gente tem o service aqui do app .api .service.

13:01

Esse é o nome do nosso service. Então vamos colocar ele aqui. E aqui no port number,

13:06

a gente vai colocar a porta 8000,

13:09

que é a porta onde está rodando o nosso serviço. Ok?

13:14

Feito isso, vamos salvar e vamos fazer um deploy novo para esse cara.

13:19

git add ponto, git commit menos m,

13:23

adicionar ingress app

13:29

API, git, faltou o checkout de novo, menos b,

13:34

adicionar add ingress app API,

13:40

git push origem add ingress app API.

13:46

Ok, mandamos para lá. Vamos fazer novamente a parte de pipeline de deploy aqui, ok?

## Resumo IA

[RESUMO_IA]