Módulo: DevOps e SRE com IA\
Aula: [Pipeline de Deploy pt1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18521)

## Resumo da aula



## Transcrição

00:00

Então vamos lá, pessoal. Começando aqui, a gente vai falar um pouco da pipeline de deploy.

00:06

Vamos passar aqui para as partes teóricas, para a gente saber o que é uma pipeline.

00:11

E depois vamos colocar a mão na massa para fazer

00:14

a geração dessa pipeline e fazer a validação,

00:17

se ela está ok, se está tudo certo, para a gente depois subir para o nosso ambiente. Então,

00:24

a primeira parte aqui, a gente vai falar só da anatomia de um workflow.

00:29

que é a nossa pipeline. Basicamente,

00:31

entenda que o workflow e a pipeline são a mesma coisa, só nomes diferentes. Então,

00:37

o workflow, a pipeline,

00:39

roda lá dentro do GitHub usando o GitHub Actions,

00:45

que é basicamente um YAML,

00:47

que é a declaração de um YAML com o que ele deve fazer e o que ele deve chamar,

00:53

lá dentro do seu runner. O runner é onde, de fato,

00:57

vai se fazer a execução das atividades. Então,

01:02

basicamente, o GitHub Actions vai orquestrar,

01:05

fazer as chamadas, validar a chamada anterior, mandar para a próxima,

01:09

e o runner é que vai fazer a execução. Então,

01:14

na primeira parte ali, a gente tem a ação, desculpa, a trigger.

01:21

A trigger vai disparar o workflow, o que você vai iniciar aquele action,

01:27

aquele workflow, ok? Então, seja um push para uma branch,

01:31

seja um pull request que foi iniciado, ele vai disparar o workflow.

01:34

Um workflow dispatch, que basicamente é você iniciar ele de maneira manual.

01:40

Ou tem a possibilidade também de fazer um scheduler,

01:44

que basicamente é você agendar aquela tarefa ali para fazer o início, ok?

01:50

No nosso projeto, a gente está usando uma trigger aqui,

01:53

que é quando a gente faz o merge para a main, para a branch main.

01:58

Iniciou o merge, fez o merge para a branch main,

02:01

ele vai iniciar o nosso workflow. Vai começar aqui. Combinado?

02:07

Os jobs, que são as unidades de execução. Então, a gente tem um workflow,

02:11

que é basicamente todo o fluxo de processo ali. E lá dentro... a gente tem os jobs.

02:16

Então, eles podem rodar em paralelo, podem rodar sequencial,

02:20

podem rodar dependendo um do outro, dependendo da saída do outro,

02:23

o próximo pode iniciar. Então, na nossa pipeline aqui,

02:26

a gente vai contar com três etapas, que são o test,

02:28

o build e o deploy, que vão ser sequenciais,

02:31

e cada um vai depender do anterior. Se um falhar,

02:34

o próximo não continua.

02:36

Mas você pode fazer e montar seu workflow da maneira que desejar. Ok?

02:43

A gente aqui no ponto 3, a gente vai ter os runners. No nosso caso aqui,

02:48

nosso runner é self-hosted,

02:50

que basicamente eu estou rodando isso dentro da minha máquina,

02:54

ela está rodando localmente aqui, o workflow está rodando, o workflow não,

02:58

o runner está rodando localmente dentro da minha máquina,

03:01

o workflow sempre lá no Git, no GitHub,

03:05

orquestrando o que os runners vão fazer.

03:08

Então, o runner está rodando local na minha máquina. Então tudo que eu fizer lá,

03:12

ele vai mandar o comando aqui

03:14

para ser feito dentro do meu computador.

03:20

Os steps, que são as ações dentro do job. Então,

03:23

cada job pode ter vários steps ali. Então,

03:30

Você pode rodar um PyTest, o exemplo aqui que está na tela tem um PyTest.

03:34

A gente pode rodar algum comando de shell, a gente pode rodar ele de alguma forma.

03:39

A gente pode fazer um arquivo Python e pedir para ele rodar.

03:44

A gente tem várias possibilidades aqui dentro dos steps, dentro dos jobs. Ok?

03:49

Só um adendo, aqui é o nome do seu job, tá?

03:52

Depois de jobs, aqui a gente tem o nomezinho dele.

03:55

Então, no caso aqui, é só um job de teste. E aqui são as etapas dele,

04:01

o que ele vai seguir de etapa aqui. E por fim, a gente tem as envs,

04:06

que são as variáveis de ambiente que a gente vai usar.

04:10

Essas variáveis a gente pode armazenar dentro do GitHub.

04:14

Lá dentro tem uma parte que a gente consegue colocar as variáveis de ambiente.

04:19

E durante a execução do workflow, ele consegue recuperar essas variáveis. Então,

04:24

seja um token de um serviço, seja uma URL de algum serviço,

04:29

seja qualquer tipo de variável de ambiente, você pode colocar lá dentro,

04:35

que o workflow vai herdar isso e vai conseguir usar dentro do runner,

04:40

beleza? No nosso caso, a gente tem lá um DBURL.

04:44

A gente tem um LLM base URL e tem um Sonar token,

04:48

que é o SonarQube que vai fazer a parte ali da segurança,

04:51

que a gente vai fazer na etapa seguinte aí, ok?

04:57

Então, próxima pasta aqui, a gente vai gerar essa pipeline.

05:02

Não vamos escrever ela... de ponta a ponta,

05:05

a gente vai entregar um prompt para o LLM,

05:07

ele vai se basear no nosso projeto, então a gente vai ter o projeto,

05:11

a gente tem o projeto, o API app, e ele vai se basear nesse projeto,

05:17

tem todas as descrições lá dentro do prompt,

05:19

e vamos gerar um pipeline com a IA,

05:25

ok? Então, ele vai gerar um YAML a partir do contexto do REPL,

05:29

e vai... Conseguir pegar tudo que tem no Apple,

05:32

mais o que a gente mandar no prompt e vai gerar o YAML para a gente,

05:38

que é aquele YAML que eu mostrei aqui na tela anterior.

05:41

Ele vai gerar exatamente esse YAML aqui com o nome deploy.yaml.

05:47

Seguindo, ele pode ter suporte para multi-ends aqui.

05:52

Tem essa parte aqui de matrix build, caching, circuit management,

05:56

a gente vai tudo lá dentro. E o GitHub Actions.

05:59

que a gente vai usar, mas ele pode gerar também GitLab CI,

06:04

CircleCI, Azure Pipelines, a gente pode gerar em qualquer lugar.

06:10

Depende do que você está usando, tá bom?

06:12

Validações obrigatórias aqui que a gente precisa fazer

06:14

nesse cara que a gente está gerando.

06:18

Primeiro ponto, nunca usar o pipeline direto em produção,

06:22

que é o que a gente falou na aula anterior,

06:25

né? que é sempre a gente validar o que a IA gerar.

06:30

Segundo ponto, no nosso caso aqui, nós não vamos passar por uma branch de teste,

06:34

a gente vai direto para quando fizer o merge para a main,

06:37

ela vai executar, porque eu não criei nenhuma branch de teste,

06:41

a gente vai mandar para o GitHub fazer o merge e a pipeline vai iniciar.

06:48

O terceiro passo,

06:50

vamos validar o YAML que foi gerado com essa action link.

06:56

Basicamente, ele vai validar a estrutura do seu pipeline que você gerou ali.

07:00

Então, ele vai validar se está ok, se está formatado.

07:03

Se não tem nada de errado ali no seu Yable que você declarou.

07:08

No caso nosso, que a AI declarou.

07:10

Ok? E sempre fazer um code review humano ali. Bate o olho,

07:15

vê se ele gerou tudo, se está tudo ok ali, como você espera,

07:19

de acordo com o que você mandou descrito no prompt para a AI gerar. Então,

07:26

Eu já falei um pouquinho do que a gente vai gerar aqui, mas vamos repassar aqui. Deploy Pipeline,

07:32

que é basicamente o fluxo de deploy automatizado de

07:36

tudo que a gente construiu na aula passada.

07:39

Então, a gente tem três caminhos workflow aqui.

07:42

Um push para main, que vai disparar o deploy automático,

07:45

e depois tem dois jobs manuais que a gente pode refazer o deploy, se for necessário.

07:52

Por exemplo...

07:54

O servidor caiu aqui, morreu as coisas, algo do tipo.

07:57

Você pode refazer o deploy a partir da pipeline. Ou você pode destruir o ambiente.

08:03

Você pode remover tudo. Nosso caso aqui,

08:06

a gente vai fazer o deploy automático e depois destruir o ambiente.

08:09

Porque quando a gente fizer a parte de segurança,

08:14

eu vou construir tudo do zero de novo para mostrar para vocês como vai funcionar.

08:18

Legal? Então, feito o push para a main. Feito o merge aqui para mim,

08:23

a gente vai iniciar nossa pipeline, que vai contar com o test,

08:26

com o build e depois o deploy no K3D, que é o deploy no caso do Kubernetes.

08:32

Os dois de baixo aqui são os

08:36

jobs manuais que a gente pode iniciar,

08:39

que é o job de deploy,

08:40

que é refazer o deploy, e o job aqui de dispatch, que é basicamente a gente... o DispatchDestroy,

08:47

que a gente pode fazer a chamada para destruir todo o ambiente. Então,

08:52

ele vai destruir todo o StatefulSet, todo o Deploy,

08:54

todo o ConfigMap que nós geramos lá. Legal? Então,

08:59

vamos gerar esse YAML aqui agora com vocês e vocês acompanham o passo a passo.

09:04

Mas antes de gerar o YAML,

09:05

vou mostrar para vocês um pouco da configuração lá dentro

09:09

do GitHub e como vocês vão fazer essa configuração.

09:12

Vai ter um manual, tá? Dentro aí dos seus materiais,

09:18

que é o manual de passo a passo, como você pode configurar isso,

09:21

porém eu vou mostrar aqui também onde que a gente vai configurar, ok?

09:26

Então, bora lá. Vamos fazer aqui nossa pipeline de deploy.

09:31

Na demo 1, a gente vai gerar um deploy .yaml,

09:35

vamos validar, vamos fazer o push para main,

09:37

teste, esse aqui já é a pipeline, né? Teste, build, deploy no K3D, ok?

09:45

Primeira parte, vamos gerar o deploy -emo com o open -code -go,

09:50

validar com o action -lint,

09:54

corrigir eventuais problemas, se quando a AI gerar tiver algum problema,

10:00

vamos fazer o push para a branch e fazer o merge para a main,

10:04

e vamos rodar a pipeline,

10:05

e vamos fazer um smoke -test aqui, e depois o manual deploy, ok?

10:13

Aqui é só o fluxo de como isso vai acontecer, depois fazer o destroy do ambiente.

10:19

Falei deploy, mas é destroy, depois a gente vai destruir o ambiente.

## Resumo IA

[RESUMO_IA]