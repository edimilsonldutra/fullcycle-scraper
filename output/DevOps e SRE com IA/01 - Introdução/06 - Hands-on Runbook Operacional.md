Módulo: DevOps e SRE com IA\
Aula: [Hands-on Runbook Operacional](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18518)

## Resumo da aula



## Transcrição

00:00

Então, a gente vai fazer um comandinho aqui de kubectl

00:03

kubectl port -for -routes svc

00:09

app -api -service -n o namespace,

00:14

demo e a exposição da porta.

00:16

Eu quero a porta 8000 de lá exposta na porta 8000 no meu serviço, do meu local host.

00:24

Feito isso, ele vai criar para mim um port for road e essa sessão fica fechada aqui, fica travada,

00:30

porque ele pegou a porta dele e expôs para mim na porta

00:33

8000 e essa sessão que está mantendo essa porta aberta,

00:37

essa sessão que eu acabei de fazer aqui.

00:39

Ok? Então, feito isso,

00:42

eu consigo vir aqui no nosso Health e fazer um

00:45

teste da minha aplicação que está rodando lá no Kubernetes.

00:49

Está funcionando perfeitamente. Se vocês notarem aqui... Nos nossos serviços locais,

00:54

eu posso vir aqui e deletar esse app.

00:58

Vou deletar o app, porque eu subi aquela hora com o Docker Compose. Ok?

01:01

E vim aqui fazer a chamada da aplicação, que ela vai funcionar do mesmo jeito.

01:05

Porque agora está lá dentro dos nossos servidores Kubernetes.

01:08

E aqui a gente não tem mais nenhuma aplicação rodando localmente.

01:12

Ok? Então aqui a gente consegue fazer a consulta dos itens.

01:16

Vocês vão ver que estão zerados. Aqui está zerado os itens.

01:19

E aqui a gente consegue inserir um item lá dentro.

01:22

Então a gente já está inserindo isso dentro do

01:24

serviço que está deployado dentro do Kubernetes.

01:26

Se a gente vier aqui e fazer um send,

01:28

a gente tem aqui o item que eu acabei de inserir.

01:31

E por fim eu posso deletar esse item.

01:35

Ele deu algum erro aqui para deletar. Item ID 1, 2 .80. Ah, funcionou.

01:42

Agora foi certinho. Deu só um erro ali, deu algum erro de rede.

01:46

Agora ele fez a eleição do item. Se a gente vir aqui e listar de novo,

01:49

a gente não tem mais nenhum item.

01:52

Então, vamos aqui inserir mais alguns itens para a gente fazer um teste.

01:56

Tem uma listinha de itens aqui que a gente pode testar.

02:00

Exemplos de itens. Vamos pegar o primeiro.

02:03

A aplicação, como eu falei, é bem simples,

02:05

pessoal. Então, acaba que tem que inserir um a um. Primeiro aqui.

02:10

Depois a gente pode pegar o outro aqui.

02:14

Vamos colar lá.

02:16

E assim por diante a gente vai inserindo os itens.

02:20

Se a gente aqui dar um send aqui, a gente já tem o item 2 e o item 3.

02:24

E assim por diante,

02:26

a gente pode inserir o item e ele vai estar

02:28

disponível lá dentro do Kubernetes para a gente.

02:31

A gente pode fazer um port forward também do banco de

02:35

dados para a gente validar que os itens estão sendo inseridos lá.

02:39

Vamos abrir aqui um novo terminal. Terminal.

02:47

Nesse novo terminal,

02:48

vamos pegar o mesmo comando que a gente usou para o nosso serviço.

02:53

E vamos rodar aqui no terminal.

02:57

Port for World, SRSVC, App API Service.

03:02

A gente pode vir aqui no Postgres Stateful.

03:05

Vamos pegar o nome do serviço dele,

03:08

que é Postgres SVC.

03:13

Vamos deletar aqui e vamos colar o nome do serviço dele.

03:17

E vamos colocar a porta que o serviço dele roda. Basicamente, 5, 4, 3,

03:21

2. Porta padrão, post 5, 4, 3, 2. E aqui a mesma coisa.

03:26

A gente quer expor também na 5, 4, 3, 2.

03:29

Basicamente, eu estou fazendo a mesma coisa que eu fiz para o meu serviço,

03:32

só que agora para o Postgres, que é para a gente

03:34

validar que os dados estão sendo inseridos lá dentro.

03:38

Feito isso, Postgres Watch pronta.

03:40

A gente pode vir aqui no nosso pgAdmin. Então, recarregar aqui.

03:44

E a gente tem aqui a tabela itens.

03:49

Então a gente tinha localmente e a tabela completinha aqui com todos os campos.

03:53

A gente fez um select,

03:54

vai dar um erro aqui, dá um continue,

03:56

e a gente tem os dois itens que a gente inseriu,

03:58

dois e três que a gente inseriu lá pelo Postgres, na chamada Post lá. Legal?

04:05

Então basicamente a gente conseguiu criar todos os manifestos Kubernetes com

04:10

o uso de AI e subir

04:13

ele lá dentro do nosso K3D.

04:19

que é o nosso Kubernetes rodando no ambiente local. Então, dessa maneira,

04:24

a gente consegue simular como seria a gente subir isso dentro de

04:29

um cluster Kubernetes rodando em uma das nuvens que a gente tem disponível.

04:34

Se a gente quiser ver os logs também, faltou a parte de log,

04:38

que é interessante também a gente ver.

04:40

Vamos abrir mais uma aba aqui para a gente não derrubar nossas conexões.

04:45

E vamos ver os logs que estão acontecendo lá.

04:48

Dentro do meu ambiente. Se vocês notarem, os logs aqui de GET têm vários.

04:53

Isso aqui é o health check do Kubernetes agindo.

04:56

Então ele vai lá de tempo em tempo e faz a

04:59

chamada do serviço para ver se aquele serviço está up,

05:03

se ele está vivo.

05:06

O health check faz essa checagem.

05:08

O Kubernetes tem essa rotina de checagem que, se o serviço por um acaso parar,

05:14

ele consegue dar um restart naquele serviço e fazer ele voltar a funcionar aí,

05:20

se for só o restart funcionar. Então, pessoal,

05:25

a gente passou aqui pela criação dos nossos manifestos Kubernetes usando AI,

05:30

e agora a gente vai falar um pouco do Rambook operacional.

05:35

O Rambook operacional, basicamente,

05:37

ele é gerado a partir da aplicação mais o SLO como contexto.

05:42

Não é um template genérico, é específico. Então, basicamente, a gente vai ter

05:47

Aqui é a geração de um handbook que vai mostrar como que a aplicação se comporta.

05:54

Ele tem referências, igual eu falei, com o SLO. Ele vai ter o erro limite ali,

06:00

o erro rate ali de 0,1% contra os erros de alerta.

06:06

E vai definir toda a parte ali de como que o serviço opera, como que ele vai...

06:14

Faz a parte de restart, a parte de rollback, se for o caso.

06:18

O que acontece quando acontecem muitos erros, 500 e assim por diante.

06:23

O prompt é estruturado com o contexto da aplicação, os endpoints,

06:28

dependências, SLO, mais as seções obrigatórias de sintomas, diagnóstico,

06:33

mitigação e como que a gente pode resolver um erro na aplicação.

06:38

O handbook vai servir isso aí, para isso, para a gente.

06:41

Saber o passo a passo de como resolver algum erro na aplicação,

06:46

Ok? Então, aqui no slide até fala um pouco.

06:51

De sintomas, o que o time de infra deve observar, diagnósticos,

06:55

Que são os comandos e as queries para investigar um problema na aplicação,

06:59

O passo a passo para a medicação e resolução

07:02

De algum determinado problema e o escalonamento,

07:04

Quando chamar o time de desenvolvimento,

07:06

Quando chamar o time de DBA,

07:08

Quando chamar o time de DevOps, quando chamar várias coisas.

07:13

Então aqui só tem um exemplo inicial aqui, Generate, Operacional, Gramado.

07:19

Para First API, Post Grid App e assim por diante. Então,

07:22

Do mesmo jeito que a gente tem do outro,

07:24

Eu vou pegar aqui um prompt que já tenho criado aqui,

07:28

Para a gente passar por ele, para a gente criar esse runbook operacional.

07:33

Deixa eu fechar esse log, que a gente não vai precisar dele agora.

07:37

Vamos fechar essas abas aqui do lado.

07:39

Aqui o nosso container, o nosso portfólio hoje também, não preciso.

07:46

E esse cara aqui eu vou fechar também e dar um

07:48

Clear nessa tela para a gente manter ela aberta.

07:51

Ok? Vamos fechar aqui.

07:52

Fechar aqui. O K8s a gente já passou por ele. Ok?

07:56

Então vamos criar um arquivinho aqui e vamos

07:59

Mostrar para vocês o Runbook operacional.

08:03

Aqui tem os comandos do prompt falando

08:06

Do Runbook operacional completo para aplicação FastAPI abaixo.

08:13

O Runbook deve ser referencial ao SLO específico de cada ação.

08:17

Então, contexto da aplicação,

08:18

Como do mesmo jeito que a gente trabalhou com os outros caras para gerar,

08:22

Com os outros, tanto para o DocFile, DocCompose,

08:26

Quanto para os objetos Kubernetes, os manifestos Kubernetes,

08:32

A gente também tem aqui o contexto da aplicação. O SLO da aplicação...

08:36

Que isso é super importante para a gente aqui na nossa questão,

08:39

E as seções obrigatórias do nosso handbook.

08:41

O que a gente vai ter? O título e metadados, os sintomas,

08:44

Que são os problemas ali, o que o on-call deve observar,

08:48

Caso dê algum problema, o que ele deve observar dentro do serviço.

08:54

Os comandos de diagnóstico devem copiar e colar os pontos para execução.

08:58

Então aqui a gente tem vários comandos que a gente pode rodar durante o nosso...

09:05

A nossa validação dos erros em produção do nosso serviço. As ações de mitigação,

09:11

O que a gente pode fazer para que esse serviço volte a funcionar?

09:16

O serviço caiu, o que a gente pode fazer para que ele volte a funcionar?

09:19

Dar um rollout, restart, reiniciar o serviço.

09:22

A gente pode escalar o serviço, ele está sendo muito usado,

09:25

A gente pode escalar, aumentar a réplica dele de 2 para 5.

09:28

A gente pode fazer um rollback, que é simplesmente tirar...

09:32

A versão que subiu, se subiu alguma versão,

09:34

Voltar para a versão anterior. Então, para cada ação deve incluir,

09:37

Quando usar, o comando exato e verificar se funcionou.

09:42

Esse é simplesmente um passo a passo,

09:44

Um checklist das ações que a gente pode fazer em caso de problema.

09:49

Critério de escalonamento. Quando acontece a violação do SLO,

09:53

escala para a equipe X. Quando acontece outra violação.

09:58

O P2 aqui, alto e violado, escala para outra equipe, escala em 15 minutos.

10:04

Sintoma não detectado, mas o SLO não é violado, monitorar e investigar.

10:08

Se bateu aqui no crítico, escala para a equipe de SRE.

10:15

Incluir contatos de escalonamento, placeholder que é o e-mail,

10:18

a parte do telefone da pessoa que

10:24

precisa ligar e umas referências aqui de SLO.

10:28

Formato de saída. Crie um arquivo em Rambook, API Rambook, diretamente.

10:33

Não explica o código, apenas gera o arquivo completo.

10:37

Isso é justamente para a gente evitar o custo excessivo de LLM

10:41

e não precisar printar isso na tela para a gente,

10:43

porque ele já vai gerar esse arquivo,

10:45

então não tem necessidade de printar na tela.

10:46

Ele vai gerar uma pastinha aqui com o Rambook operacional para a gente também.

10:52

Vamos lá, colei aqui e bora gerar o Rambook.

10:58

Está pensando e agora está fazendo o Homebook operacional. Já gerou a pasta.

11:03

Está construindo. Vou fechar esse aqui, que esse aqui é somente o prompt.

11:06

Vocês vão ter acesso a ele. E o Homebook operacional aqui está sendo gerado.

11:11

Vou esperar um minutinho para ele gerar.

## Resumo IA

[RESUMO_IA]