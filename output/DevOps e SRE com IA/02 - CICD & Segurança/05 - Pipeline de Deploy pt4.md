Módulo: DevOps e SRE com IA\
Aula: [Pipeline de Deploy pt4](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18505)

## Resumo da aula



## Transcrição

00:00

Então, a gente pode voltar aqui no Code, na primeira aba,

00:03

onde a gente tem o nosso código.

00:05

Lá no começo, eu mostrei para vocês que a gente só tinha uma branch, que era a main.

00:09

E a branch que eu acabei de criar, ela está aqui.

00:11

Subiu o workflow de deploy. Então, a gente vai clicar nela.

00:16

Clicando nela, a gente consegue ver todos os arquivos que subiu.

00:19

A gente consegue ver aqui que tem um GitHub Workflow, que é o que a gente subiu.

00:24

E aqui, por request, a gente vai criar.

00:28

Um novo pull request, ou simplesmente clicar no botãozinho aqui em cima.

00:31

Mas a gente vai criar um pull request aqui para a gente ver como funciona.

00:36

Criar um novo pull request. Esse pull request,

00:38

ele vai mandar subir o workflow de deploy,

00:45

que foi a branch que eu criei, para dentro da branch main,

00:48

que a setinha está mostrando aqui. Dessa branch para essa branch main.

00:52

O que a gente está fazendo? Estamos fazendo um merge.

00:56

Criando a solicitação de merge para a branch principal,

01:00

que é a nossa branch main aqui.

01:02

Aqui temos tudo o que foi adicionado,

01:05

que é todo o código do workflow que a gente passou por ele.

01:07

Se tiver mais arquivos que você mexeu,

01:09

vai estar tudo descrito aqui. O que foi adicionado,

01:13

o que foi retirado, assim por diante. Então a gente vai criar um pull request. Beleza?

01:21

Aqui... Foi a mensagem do commit que eu coloquei e aqui é um comentário.

01:26

Se você quiser colocar um comentário,

01:27

uma descrição, vamos colocar aqui.

01:30

Subindo um workflow novo para

01:34

fazer o deploy da aplicação para

01:40

o ambiente Kubernetes usando

01:45

o K3D no ambiente.

01:53

Ok? Feito isso, a gente pode criar o nosso pull request.

02:00

Ok? O request criado. Aqui, basicamente,

02:04

está falando que não tem nenhum conflito com essa branch.

02:07

Conflitos, normalmente, é igual eu falei, se você não der o pull lá na main,

02:11

na sua máquina, no seu repositório local,

02:14

você pode ter problemas de estar atrás de

02:19

outras coisas que já foram feitas por outros desenvolvedores.

02:22

Então, é bom você fazer esse pull para você conseguir

02:25

fazer tudo certinho aqui e não ter nenhum problema do tipo, ok?

02:31

Então, feito isso,

02:33

o pull request já está aberto. Agora,

02:40

a gente precisa fazer o merge para a branch main.

02:42

Então, aqui a gente tem o ready to merge.

02:46

A gente tem os commits, basicamente é um commit só,

02:48

se você tivesse alterado e feito todos os commits,

02:50

você teria aqui também. Aqui é o nosso commit,

02:53

onde mostra tudo que foi adicionado, tudo que foi removido e assim por diante,

02:56

você tem essa possibilidade, que no caso, quando eu cliquei aqui dentro do commit,

03:00

ele me mandou para mim o file change,

03:02

que é basicamente tudo que a gente fez

03:06

ali de alteração dentro do código nesse request.

03:12

Então vamos lá, vou dar um merge request aqui.

03:14

A partir do momento que eu clicar nesse botão,

03:16

ele já vai iniciar para mim uma action lá que

03:19

vai fazer a inicialização do

03:24

nosso processo aqui de deploy.

03:28

Então, vamos clicar no nosso botãozinho aqui de merge request. Mas antes,

03:34

eu mostrei lá como que a gente configurava o nosso run.

03:38

O nosso run aqui, ele está parado. Está nessa telinha aqui, ele está parado.

03:45

Se a gente vier aqui, vamos sair um pouco dessa tela,

03:47

vamos aqui em Settings, nossas Actions, Runners.

03:52

Nosso Run aqui está como idle, deixa eu ver se eu consigo atualizar aqui.

03:58

Offline, está aqui. Então, nosso Run, Runner,

04:02

que vai fazer a execução do nosso projeto, vai fazer a execução do deploy,

04:05

está parado. Então eu não mostrei essa telinha,

04:09

mas quando vocês baixarem o projeto para vocês,

04:11

no caso aqui como é macOS, vai funcionar desse jeito,

04:15

o Windows vai funcionar de outro e o Linux vai

04:17

funcionar parecido com o macOS que estiver usando.

04:20

Você vai dar um .run .sh dentro do pacote que ele entregar para você.

04:26

Antes do run .sh, lá no passo a passo vocês vão ver que tem uma parte aqui de...

04:33

de config .sh. É aqui que você vai fazer as configurações do seu runner.

04:39

Você vai dar o nome para ele,

04:41

você vai colocar a chave de API dele e assim por diante.

04:44

Mas eu já fiz essa configuração, eu vou simplesmente rodar ele aqui.

04:47

Então, .run .sh. Ele vai fazer a conexão com o GitHub,

04:52

conexão feita. Current running, que vai falar a sua versão,

04:55

e vai ficar esperando aqui, listening for job. Então,

04:58

ele está aqui esperando para fazer a execução de

05:02

algum job lá do que o nosso action mandar,

05:06

ok? Então, vamos deixar essa telinha para a gente ver depois ele rodando aqui.

05:11

Aqui, se eu atualizar, ele vai estar online, idle. Então,

05:15

ele aqui está online de novo, ok? Vamos voltar lá para o nosso pull request.

05:19

Vamos entrar nele. A listinha aqui, a gente tem um pull request só ativo.

05:23

Vamos entrar nele. E vamos fazer aqui um merge pull request.

05:29

Você pode subir aqui o que você quiser. Vamos colocar um commit message aqui.

05:35

Então vamos colocar merge pull

05:38

request para workflow de deploy.

05:44

Feito isso. Workflow de deploy,

05:46

aqui a gente pode deixar uma descrição aqui e confirmar o nosso merge. Ok?

05:53

Merge feito, se a gente vier aqui na nossa branch main,

05:57

a gente vai ter aqui na main agora o nosso GitHub workflows. Legal?

06:02

Temos aqui a nossa action, vocês podem notar que iniciou uma action automaticamente,

06:07

assim que eu fiz o merge, não fiz mais nada, fiz o merge, ele já...

06:12

sensibilizou uma action para iniciar.

06:14

Aqui temos todas as nossas etapas da action. Então temos o teste,

06:18

que a gente viu lá. A gente tem um build da imagem, que a gente viu lá também.

06:22

E temos aqui o deploy da aplicação de fato. Legal?

06:26

Então se a gente entrar dentro de cada job,

06:29

a gente tem cada stepzinho lá dentro. Então a gente tem o workflow.

06:34

Temos jobs, e dentro dos jobs nós temos os steps.

06:38

Então a gente tem o setup aqui do job, o run action,

06:41

que é esse action aqui que ele vai fazer uma verificação,

06:44

vai instalar o Python Dependencies,

06:46

então aqui a gente tem uma lista de tudo que foi instalado lá dentro.

06:49

A gente tem um run link aqui que ele vai validar o nosso código. Temos o run test,

06:54

que ele vai rodar nossos testes, fazer um push aqui,

06:56

e vai completar o job, que é a última etapa.

07:00

Na segunda etapa, a gente tem um build da imagem,

07:03

que ele vai fazer de novo o checksum, vai startar o job, vai fazer o setup dele,

07:07

vai fazer um checksum aqui, v4, vai fazer o docker build da imagem.

07:11

Então aqui a gente tem todo o build da imagem.

07:14

Se eu pegar aqui o meu Docker, deixa eu abrir o meu Docker Dashboard aqui,

07:18

estou em outra tela, deixa eu mostrar para vocês.

07:21

Se a gente abrir aqui, se a gente vier em images,

07:24

a gente vai gerar aqui um appapi build 11.

07:29

Tá bom? Que foi o número do workflow que eu rodei. E o App API Lasted,

07:34

que é justamente o que ele gerou lá como saída da última versão do meu código.

07:40

Então ele versiona a cada pipeline que roda e cria um Lasted aqui também,

07:45

para a gente usar dentro do nosso deploy.

07:48

Tem uma tag, ele vai colocar uma tag na imagem aqui.

07:52

E aqui justamente que ele vai colocar o build11, que é aqui que eu falei.

07:57

E vamos colocar aqui, por último, um action de checksum aqui também.

08:05

Isso é obrigatório aqui dentro do workflow.

08:09

Por último, ele está fazendo o deploy dos nossos serviços.

08:12

Na verdade, já até terminou, né?

08:13

Deixa eu dar um atualizado aqui. Aqui está rodando ainda, mas não tinha atualizado a tela.

08:16

Já até terminou o deploy. Então,

08:18

ele começou aqui fazendo o load da imagem para dentro do K3D.

08:22

Deixa eu dar um zoom aqui para ficar mais fácil.

08:25

Então ele fez o load da imagem para dentro do K3D.

08:29

Deploys fez o deploy dentro do K3D.

08:32

Então ele pegou cada um dos arquivos, um config map, o deploy,

08:36

e fez a criação deles lá dentro do nosso cluster Kubernetes.

08:42

Esperou o rollout da API.

08:44

Então ele aguardou até que a API estivesse como health lá dentro do Kubernetes.

08:50

Usando o comando aqui do kubectl rollout status,

08:54

Ele apontou lá para o nosso app e aguardou aqui um

08:59

timeout de 120 segundos para validar se essa API subiu,

09:03

se o app API subiu.

09:05

Fez o rollout também para o Postgres para ver se ele estava íntegro e de pé.

09:09

Também, mesma coisa para o Redis. E fez um smoke test. O que é esse smoke test?

09:13

Eu tinha falado lá. Ele fez simplesmente um curl para saber o status, se o serviço estava online,

09:19

e fez um curl aqui em outras coisas para saber qual é o ambiente,

09:22

esses negócios. Então, fez toda essa parte. Então,

09:26

a gente acabou de fazer um deploy automatizado

09:28

lá dentro do nosso cluster Kubernetes,

09:31

fazendo cada uma dessas etapas aqui dentro.

## Resumo IA

[RESUMO_IA]