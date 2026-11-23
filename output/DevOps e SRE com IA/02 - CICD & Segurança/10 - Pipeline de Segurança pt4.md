Módulo: DevOps e SRE com IA\
Aula: [Pipeline de Segurança pt4](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18507)

## Resumo da aula



## Transcrição

00:00

Nosso Workflow de Security agora a gente já conta aqui com o GitHub Workflows,

00:04

que temos dois jobs aqui dentro,

00:07

e temos aqui um agent, que a gente tem um arquivo .py aqui dentro,

00:11

que é o nosso agent de validação.

00:15

Estamos subindo aqui, gente, tudo dentro do mesmo repositório,

00:19

mas vocês podem criar repositórios à parte e apontar o

00:23

seu código para pegar de outros repositórios e fazer a execução.

00:26

Se você quiser, por exemplo, criar um repositório... de workflows.

00:30

Você pode criar o repositório de workflows,

00:32

colocar todos os workflows dos seus projetos,

00:34

etc. lá dentro e começar a usar de lá, versionado, tudo certinho.

00:40

A gente está subindo tudo aqui no mesmo repositório somente para aproveitar.

00:43

Pode criar um repositório de agents também, onde você vai consumir esses agents.

00:48

Então a gente tem várias possibilidades aí de fazer.

00:56

Essas criações aí dentro do GitHub, GitLab,

01:00

seja o versionador de código que você está usando aí. Vamos lá?

01:06

Primeira parte. Quando a gente fizer o pull request,

01:09

essa pipeline tem que iniciar. Vamos ver que isso vai iniciar.

01:12

Vocês podem ver aqui que a gente não tem nenhuma pipeline aqui.

01:16

A gente só tem a pipeline de merge que a gente fez e aquela que a gente executou,

01:22

que fez o destroy, ok? Então vamos executar aqui o pull request.

01:28

Vamos aqui primeiro no pull request, mesmo procedimento, new pull request,

01:33

agora a gente vai subir a branch de workflow security,

01:38

subir o workflow security,

01:40

aqui temos nossa branch e aqui temos nosso código Python do agent,

01:44

ok? Vamos criar o pull request agora.

01:51

Aqui é só um comentário.

01:53

Vou aproveitar esse de cima e colocar aqui para não precisar digitar de novo.

01:56

E vamos criar o pull request aqui dentro do GitHub.

02:01

Ok? Beleza. Pull request criado.

02:04

Vocês vão notar que automaticamente vai iniciar uma pipeline aqui.

02:08

Iniciou. Está vendo?

02:10

Então a pipeline de security começou a rodar. Aqui a gente pode ver ela,

02:14

mas aqui em Actions a gente pode abrir ela e

02:18

olhar o que está acontecendo.

02:21

Basicamente, SonarScan ainda não iniciou. Vamos ver se o TriviScan aqui já iniciou.

02:26

Ah, o TriviScan já tá rodando. Já fez aqui alguns scans. Vamos

02:34

atualizar aqui pra ver o que ele tá fazendo. Ah,

02:37

ele tá fazendo a setup ainda. Se vocês notarem, aqui dentro do terminal,

02:44

na parte lá do agent que a gente tá... do agent não, né?

02:48

Do runner que tá rodando, ele já começou a fazer o TriviScan aqui.

02:53

Está fazendo aqui o Trivial Scan.

02:55

Então vamos voltar lá na pipeline para a gente acompanhar a execução dela.

03:01

Deixa eu tentar dar um zoom aqui. Vai ficar mais fácil a visualização de todos.

03:07

Então ele está fazendo alguns downloads aqui. Está fazendo alguns updates.

03:12

Vamos ver. Vamos atualizando.

03:15

Apple Mirror. Ele está baixando algumas coisas aqui do Trivial para fazer os testes.

03:23

Enquanto ele está rodando aqui.

03:26

Vamos olhar aqui as actions e ver como está o Sonar.

03:32

O Sonar ainda não pegou aqui. Não pegou para ser executado ainda.

03:38

Porque se não me engano, ele está configurado para rodar um drop por vez.

03:44

Terminou o TrivScan. Acabou de terminar. Vamos ver o resultado lá.

03:48

Está rodando o scanner do Sonar. Daqui a pouco a gente volta para ver o resultado.

03:53

Então a gente tem aqui o TrivScan. Terminou. Qual foi o resultado?

03:57

Ele fez aqui um upload dos resultados que me entregou o arquivinho

04:03

aqui de JSON com o resultado final do processo aqui do Drift.

04:09

Deixa eu tirar o zoom aqui para ver se a gente consegue... Não, isso mesmo.

04:14

Rodou o config scan aqui, fez o escaneamento de todas as coisas que a gente tem.

04:21

Fez o escaneamento aqui dos projetos, das portas, essas coisas todas, tá?

04:25

Tá tudo aqui bem descrito. E ele me entregou um arquivinho aqui, .json,

04:31

pra gente validar, juntar isso e colocar dentro da nossa análise com a AI.

04:38

Então, SonarScan. Então, ele fez aqui o scan do SonarQube. Beleza?

04:44

O scan do SonarQube, ele fica disponível,

04:48

tem uma interface do SonarQube. Tá até aberta aqui, ó.

04:51

Então a gente cria uns projetos aqui dentro,

04:53

a gente tem aqui o nosso projeto de App API e a gente

04:56

tem aqui as vulnerabilidades que podem ter dentro do meu código.

05:01

Então basicamente aqui a gente tem algumas vulnerabilidades de segurança,

05:05

de reability, maintainability, etc. A gente tem várias issues abertas aqui.

05:11

Então ele fez aqui a análise de todos os meus arquivos .py do meu projeto.

05:18

Então, esse cara, o SonarQube,

05:20

fez a avaliação dos arquivos .py e o Trivy

05:24

fez algumas avaliações aqui

05:26

dos arquivos dos meus deploys,

05:32

dos meus arquivos de deploy do Kubernetes. Então,

05:34

aqui eles acharam algumas configurações aqui que podem ter problema.

05:42

Inclusive, achou três configurações aqui em RAI.

05:48

E várias fases de failure aqui. Ok? Por último, deixa eu recarregar a tela.

05:56

Já rodou, inclusive, o nosso Security Agent,

05:59

que aqui é a parte do Python Dependency.

06:01

Então, a gente fez a instalação aqui dos arquivos .py.

06:06

Rodou o Security Agent, o código Python mesmo, aqui ele rodou o Python 3, etc.

06:12

fez a chamada lá, fez a chamada no LLM,

06:15

se a gente olhar aqui no nosso LLM Studio,

06:19

tem uma parte aqui que é a parte de programática dele,

06:22

aqui é a chamada que ele fez, com o retorno, com tudo mais, entendeu?

06:27

Então ele já fez a chamada aqui, se vocês notarem o horário, 22h19,

06:32

olharem aqui, 22h20, acabou de ser feita essa chamada,

06:36

então funciona certinho, ele fez a chamada do meu modelo,

06:41

O código Python fez a chamada do

06:43

meu modelo lá dentro do meu LLM local.

06:48

E por último,

06:50

ele rodou esse run actions aqui e finalizou o job,

06:53

ok? E comentou postagem com sucesso.

06:57

Então, basicamente, ele conseguiu fazer a postagem do comentário aqui dentro do Git.

07:02

Vou tirar um pouquinho o zoom do GitHub.

07:06

Zoom aqui, ok?

07:08

Então, vamos aqui dentro do nosso pull request,

07:11

entrar nele aqui e ver o comentário.

07:17

Aqui a gente tem o nosso comentário. Aqui ele colocou em inglês.

07:20

Vocês podem pedir para o LLM colocar em português,

07:23

Tá bom? Então, a application is critical networking expository.

07:30

Inglês aqui vai ser foda de ler.

07:32

Mas vamos lá. A gente tem aqui várias coisas, que é P1, crítico.

07:38

O que é crítico para a gente mexer no código por parte de segurança. Temos aqui nenhum.

07:44

P2, RAI. A gente tem um cara com RAI aqui. E tem o P3,

07:50

que é médio e low. Treze coisas aqui encontradas. Então,

07:53

o que a gente tem aqui no nosso RAI?

07:55

A application está liberada para todas as portas entrarem.

08:00

Então, todas as portas, não, todos os IPs, que é 000 aqui.

08:04

Então, ele está meio que liberado para todo mundo entrar.

08:07

Ele considerou isso como high e a gente tem que mexer na

08:10

aplicação porque isso pode ser uma exposição para a aplicação.

08:14

E aqui tem comentário de cada uma das coisas que a

08:18

gente tem de crítico dentro do

08:23

projeto que a gente pode melhorar. De crítico não, né?

08:27

De vulnerabilidade que tem dentro do projeto que a gente pode melhorar isso aí.

08:32

Ok? E aqui a gente tem...

08:34

o crítico nenhum, high 1, e o médio e low 13,

08:37

que são esses 13 comentários aqui pra baixo. Ok?

08:41

Vamos ignorar esse aqui agora, esse high agora,

08:43

e vamos publicar nossa aplicação. Tá bom? Basicamente,

08:47

rodou esse cara, fez o comentário, comentário feito,

08:51

a gente agora pode fazer o merge pull request.

08:55

Feito o merge pull request, vou copiar esse cara e jogar aqui pra cima.

09:01

E vou confirmar meu merge request. Ok.

09:07

Feito o merge aqui para master, a gente vem aqui em actions.

09:12

Vocês podem notar que de novo iniciou uma pipeline aqui para fazer o deploy.

09:17

Vai rodar aquele mesmo deploy que a gente fez lá na etapa anterior.

09:22

Vai fazer os testes,

09:24

vai fazer o build. Vocês podem notar aqui, deixa eu entrar aqui dentro do meu...

09:30

do meu desktop aqui, vocês podem notar que ele fez um build 13 aqui,

09:34

que é a pipeline número 13,

09:35

porque a gente rodou outra pipeline antes, de security,

09:38

então acabou que pulou do 11 pro 13, tá?

09:41

E vai gerar uma nova laystitch aqui, ok? Feito isso,

09:46

ele vai fazer o deploy dentro do nosso Kubernetes.

09:48

Se vocês notarem, a gente tinha nada lá dentro do Kubernetes,

09:52

e agora, se a gente vier aqui no iTern, vamos aqui no nosso K9,

09:56

aqui ó, os serviços estão subindo de novo.

09:59

Serviços todos de pé nesse momento.

10:02

Então ele vai aguardar que a idade do agent acabou de subir alguns segundos.

10:06

Se vocês notarem aqui dentro,

10:08

ele terminou de fazer o processo e o deploy está feito no ambiente.

10:15

Então a gente conseguiu combinar as duas pipelines.

10:18

Uma pipeline de deploy,

10:19

mais a pipeline de segurança que a gente fez em desenvolvimento.

10:26

Então, security pipeline e a pipeline de deploy.

10:30

Primeiro rodou uma. Essa pipeline de security,

10:34

a gente tem a possibilidade de bloquear o pull request para a main.

10:39

Então, a gente tem a possibilidade de bloquear o merge do pull request para a main.

10:45

Então, ela é super importante para a gente conseguir

10:48

mitigar erros na aplicação e assim por diante.

10:51

Então a gente pode construir isso tudo

10:53

com um projeto automatizado e que o desenvolvedor, o pessoal de segurança,

10:59

tenha toda uma visão para fazer esse deploy nos ambientes do nosso ecossistema.

11:07

Ok, feito isso, temos lá a nossa aplicação funcional.

11:11

Na última etapa aqui da pipeline, deixa eu abrir aqui para vocês,

11:14

para vocês verem que ele fez a chamada aqui da pipeline.

11:18

Na verdade, o teste, o smoke test,

11:20

que basicamente é uma chamada aqui para ver se o status está como health.

11:23

Ele fez a chamadinha aqui. Nosso serviço está de pé novamente aqui no Kubernetes.

11:28

Ok. Então, o que a gente fez, gente?

11:31

A gente acabou de construir aqui uma pipeline na parte 1.

11:35

Construímos uma pipeline de segurança que complementou essa

11:38

pipeline de deploy da parte 1,

11:40

nessa parte 2. Então, agora a gente vai criar uma pipeline aqui de eval prompt.

11:47

Basicamente, a gente vai ter um prompt de sistema lá dentro do nosso ambiente.

11:51

Esse prompt de sistema vai ser ele que vai ser capaz de

11:56

gerar as coisas lá para dentro daquele código Python que a gente criou.

12:02

Lá está fixo,

12:03

mas esse prompt de sistema é ele que vai gerenciar. Então,

12:06

se você precisar adicionar alguma coisa, criar outra coisa, etc.,

12:09

você pode mudar nesse prompt de sistema.

12:12

E a gente vai criar um pipeline que vai avaliar esse prompt de sistema,

12:16

usando o prompt full.

12:18

Bacana? Quando esse prompt mudar, essa pipeline vai iniciar,

12:22

vai fazer a chamada do prompt full aqui, que vai fazer a análise com outra AI,

12:27

no caso nossa aqui, a AI local,

12:29

do que mudou nessa parte do prompt.

12:34

Se faz sentido essa mudança.

12:36

Uma outra AI vai conseguir avaliar isso, uma outra generatividade. Então,

12:41

volto em breve aí, para a nossa última parte.

12:44

Hoje a gente vai criar a pipeline de Evolve Prompt aqui.

12:48

Então, gente, aquele abraço. Daqui a pouco eu volto.

## Resumo IA

[RESUMO_IA]