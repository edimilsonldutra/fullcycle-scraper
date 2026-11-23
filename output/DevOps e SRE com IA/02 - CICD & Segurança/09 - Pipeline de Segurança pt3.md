Módulo: DevOps e SRE com IA\
Aula: [Pipeline de Segurança pt3](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18528)

## Resumo da aula



## Transcrição

00:00

Antes da gente rodar esse agent,

00:02

deixa eu mostrar para vocês como eu falei aqui que a gente vai usar o LM Studio.

00:07

Vocês podem usar qualquer outro serviço aí que vocês tenham disponível,

00:11

mas se vocês tiverem uma máquina aí que consiga rodar

00:14

algum modelo e quiserem rodar eles open source,

00:17

nós temos a possibilidade aqui de rodar o LM Studio. Deixa eu mostrar aqui.

00:22

Então basicamente essa aqui é a carinha do LM Studio. Como funciona, tá gente?

00:27

Basicamente, a gente tem esse último botãozinho aqui, dessa barra lateral,

00:30

a possibilidade de baixar vários modelos

00:33

open source direto lá dentro do Hugging Face.

00:38

Então, eu estou usando um modelo um pouco mais leve aqui,

00:42

que não é tão pesado, que é esse 3.5 35B com... A3B aqui,

00:50

que ele ativa menos parâmetros para rodar e vai ativando

00:53

à medida que for necessário os outros parâmetros.

00:55

Está até aqui como Downloaded. Então, esse modelo pesa 29 GB.

01:00

Quando eu subir ele aqui, ele vai consumir da minha máquina 29 GB.

01:05

Deixa eu puxar aqui a telinha para vocês verem.

01:08

Ele está rodando agora. Deixa eu fechar aqui.

01:13

Tirei ele, estava rodando o modelo.

01:16

Vamos lá, deixa eu puxar a telinha aqui de monitor para a gente.

01:20

Então aqui vocês viram que o modelo estava rodando,

01:23

minha máquina tem 48 GB disponível,

01:26

e o modelo aqui eu acabei de tirar ele, de fazer o eject dele,

01:30

e o serviço desceu aqui para estar usando agora 17 GB,

01:35

basicamente do meu sistema operacional.

01:38

Então agora vamos subir aqui no LM Studio.

01:44

Nosso modelo, que basicamente tem alguns outros baixados aqui,

01:47

mas a gente vai subir esse Queen 3.5 de 35 bilhões,

01:51

de 35 bilhões de parâmetros,

01:55

tá? Acho que pode ter cortado um pouquinho aí,

01:57

mas é de 35 bilhões de parâmetros, ok? Então vamos subir esse modelo aqui.

02:03

Vamos usar aqui o GPU Offload,

02:06

basicamente a quantidade de GPUs que ele pode usar ali.

02:10

E vamos subir aqui o contexto dele para 10 mil, para ele caber.

02:15

A nossa análise aqui legal e vamos dar um colocar 10 mil redonda aqui fica mais

02:20

fácil 10 mil toques então ele consegue 10

02:25

mil toques aí é na verdade é para receber

02:29

os parâmetros que a gente gerar lá no Sonar e no Trf, beleza? Vamos

02:34

dar um logo de modos, o modo tá carregando, ok? Temos um modelo pronto aqui para usar.

02:40

Se vocês notarem, o meu consumo de memória já subiu aqui para 44 GB.

02:46

Beleza? Então, vamos iniciar o novo chat, só para a gente fazer um teste aqui.

02:51

Vamos selecionar esse modelo. Vamos falar, dá um olá aqui. Olá.

02:56

Infelizmente, essa tela aqui, eu não consigo...

02:58

Deixa eu ver se eu consigo dar um zoom. Ah,

02:59

eu consigo dar um zoom nessa tela. Aí fica melhor para vocês.

03:02

Ele está aqui pensando, fazendo o think.

03:05

E eu mandei um olá para ele. Ele está pensando aqui um punhado para me responder.

03:09

Mandou um olá. Como posso te ajudar? Vou mandar aqui para ele.

03:12

Você pode me contar uma piada?

03:18

Ó. Então ele vai pensar de novo.

03:21

Isso tudo rodando localmente, tá, gente?

03:23

Então a gente tem aqui o consumo da nossa GPU aqui.

03:30

Então... Pensando, tá pensando. Daqui a pouco ele dá a resposta.

03:33

Você consegue acompanhar aqui no fim que ele tá gerando, né? De pensamento.

03:38

Então ele... De acordo com o que você manda ali e pensou.

03:42

Então, claro que sim, eu chamo você.

03:46

O que o zero diz para o oito? Contou uma piadinha aqui sem graça.

03:49

Mas a gente está rodando um modelo localmente e é o modelo que

03:52

a gente vai usar para fazer a análise lá dentro do nosso serviço. Ok?

04:00

Do nosso agent, no caso. Então, vamos lá.

04:04

Vamos voltar aqui.

04:06

Aqui a gente está dentro do GitHub.

04:09

Vamos voltar aqui no nosso code. A gente,

04:14

por último, tinha esse script aqui,

04:18

que é o nosso prompt para gerar o agent.

04:21

O agent está gerado, já está aqui disponível.

04:24

Então, a próxima etapa é a

04:26

gente conseguir gerar a parte do workflow, do security workflow.

04:34

Então, essa parte do security workflow é onde a gente vai gerar a pipeline.

04:38

que vai executar o Trivy e vai executar o SonarQube

04:42

e vai dar o resultado para o nosso agent atuar.

04:46

Legal? Então, vamos de novo aqui no OpenCode.

04:50

Na verdade, deixa eu vir aqui para mostrar para vocês o prompt. Deixa

04:54

eu copiar o prompt aqui.

04:59

Está dando problema para copiar, gente. Espera aí. Dá um minutinho.

05:03

Vamos lá. Aí, o prompt está aqui. Vamos lá.

05:07

Então, gere um workflow. Vamos colocar aqui um...

05:10

um warp aqui, quebrar a linha, gera um workflow, o pipeline de segurança,

05:15

o workflow roda um pull request,

05:16

roda em pull request para a branch main e executa três jobs,

05:22

só na kube-scan, tree-scan e security-agent. Então ele vai executar esse aqui,

05:27

esse aqui e esse aqui por último, esses dois em paralelo.

05:31

Alguns contextos do repositório, Python, FastAPI e assim por diante.

05:38

O workflow deve incluir, por request, os jobs. Job 1, SonarQube scan. Legal?

05:44

Job 2, Preview scan,

05:46

que vai fazer os scans

05:47

de vulnerabilidade do nosso código.

05:54

E o SonarQube também vai fazer alguns scans.

05:56

O job 3 é o security agent, que a gente vai executar o arquivo .py.

06:01

Aqui, se você ver, vai ter um pip style, GitHub, OpenAI,

06:04

basicamente o código que ele vai precisar executar ali

06:07

para fazer a chamada do nosso security agent.

06:11

As condições,

06:13

que um vai dependendo do outro ali, e os requisitos. No final,

06:18

ele vai gerar um YAML com workflow sem explicação adicional.

06:21

Então, vamos copiar esse prompt aqui. Lembrando, tá, gente?

06:27

Todos esses prompts aqui vão estar disponíveis para vocês e vocês podem

06:30

colocar ele como skills também dentro do OpenCode ou de qualquer outra ferramenta.

06:36

E você passa a usar skills, fazer o preenchimento de variáveis, etc.

06:41

E que você vai conseguir usar também.

06:43

Aqui a gente está usando um prompt bem formatado, mas de maneira mais rápida,

06:49

que é simplesmente jogando na janela de contexto e

06:51

ele vai fazer o processamento para a gente,

06:53

porém nada impede você de usar skill com esse cara, ok?

06:57

Vamos aqui dentro do, deixa eu tirar esse monitor daqui,

07:01

que a gente não precisa dele mais,

07:02

vamos aqui dentro do terminal do OpenCode,

07:09

colar aqui o nosso prompt e mandar ele gerar o YAML aqui do nosso workflow,

07:15

nosso workflow lá do GitHub Actions, ok? Então,

07:19

foi, gerou o arquivinho aqui pra gente,

07:22

a gente já tem um arquivo security aqui.

07:25

Um workflow de security .emo. Então, security pipeline,

07:28

um pull request para a branch main,

07:32

quando a gente abrir um pull request para a branch main,

07:33

do tipo open, synchronize e reopen. Então, basicamente, desses tipos.

07:39

Quando a gente abrir esses tipos aqui de pull request,

07:42

quando ele tiver, ele vai iniciar.

07:45

Primeiro job. O job é o SonarScan, self-hustle,

07:49

que vai fazer a primeira parte que você tem, e rodar um... run sonar -cube -scan.

07:55

Então ele vai sonar -scanner e vai mandar aqui todas as partes.

08:00

Essas variáveis aqui estão lá dentro do GitHub.

08:03

Sonar -token, sonar -url estão dentro do GitHub.

08:07

E a gente vai conseguir rodar esse comandinho aqui dentro da nossa máquina

08:11

para fazer o processamento e a validação do nosso código usando o Sonar. triv -scan

08:20

Então a gente vai fazer aqui o runTrivialScan,

08:22

então ele vai fazer o scan do nosso código e dar o resultado através do JSON.

08:28

E por último, a gente vai ter o SecurityAgent,

08:31

que é o agent que a gente gerou com o arquivo .python ali,

08:34

que vai rodar com os modelos SonarScan,

08:37

vai depender da execução do SonarScan e

08:41

do TrivialScan para sempre conseguir pegar os resultados.

08:46

E basicamente ele vai rodar esse comando, pip install, openAI, request, etc.

08:52

E por último vai fazer a execução do nosso serviço,

08:55

que é o Python 3 AgentSecurityAgents.

08:57

Todo isso aqui são as nossas variáveis de ambiente,

09:02

que a gente já tem lá dentro do GitHub Variables, lá dentro da pipeline.

09:08

Então, feito isso, vamos fechar isso aqui, deletar esse prompt.

09:14

E vamos agora fazer a parte de mandar...

09:20

Ah, antes de fazer,

09:22

vamos fazer só um action link aqui para a gente...

09:26

Olha lá. Um action link para a gente validar se esse workflow está correto, ok?

09:32

Achou duas coisas aqui, mas são... Double...

09:37

Double check to prevent... São só partes de...

09:45

Tá, check issue script info.

09:49

Esses não são erros de fato, tá gente? Isso aqui é só um warning aqui,

09:54

tá bom? Então a gente pode desconsiderar,

09:57

ok? Mas é sempre bom ver para ver se a gente tem algum tipo de erro aqui, ok?

10:04

Também vamos rodar aqui a parte do Python, que é algo que eu esqueci de validar.

10:10

Vamos aqui. Para a gente validar se o código em Python está funcionando.

10:13

Então, Python 3, menos N, Py, compile,

10:18

agent,

10:20

Barra, security, agent, ponto, Py. Que, basicamente,

10:25

eu vou fazer a compilação do código

10:30

Python para ver se ele está compilando certinho,

10:33

sem erros. Basicamente, compilou, né?

10:36

O resultado aqui foi zero, nada, então compilou sem erros aqui.

10:40

Nosso código Python está íntegro e funcional aqui.

10:43

Ok? Então vamos lá. Primeira etapa, Git, Git pull. Eu já fiz o Git pull,

10:48

mas vou fazer de novo aqui só para garantir.

10:52

Então a branch está atualizada aí de acordo com a...

10:56

Seguindo, a gente vai fazer o Git checkout,

11:00

menos B. Então vamos subir, subir o workflow.

11:09

Workflow de security, ok?

11:14

Vamos subir o workflow de security.

11:17

Temos os dois aqui, né? Security emu, que é o workflow,

11:20

e aqui o agent. Então git add ponto, para adicionar ambos aqui,

11:24

para marcá-los como possível commit. git commit menos m,

11:30

vou aproveitar essa mensagem que a gente tem aqui.

11:34

Então subir o workflow de security para deploy.

11:43

No Kubernetes, ok?

11:46

Então, já adicionei ambos aqui, já fiz o commit,

11:50

agora a gente vai fazer o push, git push origin,

11:54

vamos copiar o mesmo nomezinho aqui de security,

11:57

vamos mandar lá para o nosso repositório remoto.

12:02

Feito isso, o que a gente tem aqui agora?

12:05

Nós podemos vir aqui no GitHub,

12:10

e olhar nossas branches. O que a gente tem de branch aqui agora? Tem a primeira,

12:14

que é o workflow de deploy, e a segunda, que é o nosso workflow de security. Ok?

## Resumo IA

[RESUMO_IA]