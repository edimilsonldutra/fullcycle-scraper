Módulo: DevOps e SRE com IA\
Aula: [Pipeline de Deploy pt3](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18526)

## Resumo da aula



## Transcrição

00:00

GitHub deploy. Está aqui o nosso workflow direitinho.

00:03

Deixa eu ver se ele já terminou. Terminou. Aqui ó,

00:05

arquivo criado com três caminhos e assim por diante.

00:08

Tudo descrito aqui conforme eu pedi lá no prompt.

00:11

Então o workflow está aqui criado.

00:13

Deixa eu tirar essa telinha de pesquisa. Vou tirar aqui também o prompt.

00:18

O prompt vai estar disponível para vocês.

00:20

Eu não sei se eu já falei, mas falando de novo,

00:22

ele vai estar disponível aqui para vocês.

00:24

Então a gente vai passar aqui pelo YAML.

00:26

Vamos fazer um code review aqui basicamente do YAML. O nome,

00:29

do nosso workflow, deploy app API,

00:32

o on aqui no push para a branch main, ok? O workflow dispatch,

00:38

que basicamente são as etapas manuais que a gente pode fazer.

00:45

Então a gente tem aqui toda a descrição dela.

00:47

E os jobs? O job de teste, o que ele vai fazer?

00:51

Ele vai instalar as dependências do Python.

00:53

que é basicamente um comando de fato, igual eu tinha dito lá,

00:56

a gente vai dar um comando de pip install e assim por diante, vai fazer um run lint,

01:01

vai usar o lint do próprio

01:03

Python aqui para fazer um teste

01:08

e vai rodar alguns testes aqui com o pytest na aba testes aqui,

01:13

que é o nosso arquivinho aqui. Legal?

01:17

O build, o que o build vai fazer? Como a gente está rodando localmente,

01:21

Como funcionaria, assim, se a gente estivesse usando um servidor cloud?

01:26

Você poderia, por exemplo, na AWS,

01:28

você poderia fazer um build para mandar para o ECR, por exemplo,

01:33

que é o repositório de imagens que você coloca essas imagens dos seus projetos lá.

01:40

No nosso caso,

01:41

como a gente está usando aqui localmente,

01:43

a gente vai dar um Docker Build Image. Na verdade,

01:46

esse é o nome do step lá dentro, né? Da parte lá dentro do nosso job.

01:52

Esse step, ele vai rodar um docker build,

01:54

menos -t, app, latest e assim por diante. Então,

01:58

ele vai buildar a imagem para mim e deixar disponível através do Docker.

02:02

Vai colocar uma tag na imagem nossa,

02:06

tag image with number, então ele vai gerar lá uma tag com o número de execução,

02:11

tanto que ele pega aqui github run number,

02:15

então ele vai, para cada vez que ele rodar aquele job,

02:17

ele gera uma imagem, daquela execução,

02:20

legal? Então assim você consegue meio que versionar

02:23

e ver aquelas imagens ali guardadas. Se tiver dentro de um ECR,

02:27

por exemplo, você consegue ir vendo como aquela imagem foi evoluída,

02:31

ok? O deploy, que vai usar o EFS host também,

02:34

que é a parte que vai depender, esse needs aqui,

02:37

a dependência, então ele depende do build da etapa anterior,

02:40

e vai verificar se github .invitename for um push,

02:44

ele vai fazer, vai iniciar aqui, ok?

02:48

Então, em primeira parte, a gente vai fazer o load da imagem para dentro do K3D,

02:52

porque a imagem está disponível dentro do Docker. Então, a gente precisa inserir,

02:57

Fazer a inserção dessa imagem dentro do nosso Cluster Kubernetes. Depois,

03:03

vai fazer o deploy de todos os arquivos que estão dentro do K3D. Legal?

03:10

Desculpa, todos os arquivos que estão aqui na pasta. Então,

03:12

a gente tem um K8s barra. todos os arquivos. Então,

03:16

ele vai fazer o deploy de cada um desses caras aqui.

03:18

Ele vai dar um wait rollout, que ele vai esperar todos os caras ficarem ativos.

03:25

Ficaram ativos, ele vai terminar. Fica nesse wait for rollout aqui do app API.

03:31

Ele vai ficar também esperando o Postgres ficar pronto e o Heads ficar pronto,

03:35

que são esses dois caras aqui. Esse é o Postgres,

03:39

esse é o Heads e aqui é o deploy de fato do nosso serviço. Ok?

03:44

Ficou todo mundo pronto, ele vai fazer um smoke test,

03:46

que é basicamente só um teste de se nosso serviço está funcionando, se ele está de pé.

03:51

Ele vai simplesmente fazer um curl lá dentro. Fez o curl, a gente vai terminar ali,

03:57

deploy está feito. Manual deploy vai fazer exatamente todas aquelas etapas lá.

04:01

E o destroy, ele vai deletar os recursos do K8s.

04:05

Então ele vai matar tudo do Kubernetes.

04:07

Claro que no nosso caso aqui a gente só tem um projeto.

04:09

Se a gente fosse fazer isso em um ambiente maior,

04:13

a gente teria que colocar aqui uma definição certinha

04:17

do que você quer fazer no strike. Ok?

04:20

Então, feito isso, próxima etapa.

04:22

Vamos fazer lá o nosso Action Lint,

04:27

que é simplesmente a gente vai testar se esse YAML está válido,

04:31

se ele está todo certinho. Então,

04:33

a gente vai aqui no próprio Visual Studio Code.

04:41

Podemos abrir aqui um terminal e a gente pode fazer um teste.

04:44

Então, basicamente, vai digitar Action Lint,

04:46

já está até o comando ali que eu tinha feito antes,

04:48

.github barra workflows

04:52

barra security security.yml.

04:58

Isso aqui é yml.

05:01

Feito isso, ele vai validar. Não,

05:04

é que ele não achou o nosso arquivinho. Então, onde que a gente está? App API.

05:11

Não, eu coloquei security, não é security. Security é a outra pipeline. Está vendo?

05:14

Eu fiz o teste na outra e troquei as bolas aqui. Deploy.yml.

05:21

Validou. Vamos de novo.

05:24

Validou. Não achou nenhum erro na nossa pipeline. Então, basicamente,

05:28

nossa pipeline está apta e está funcionando. Se eu, por exemplo,

05:32

viesse aqui e vamos colocar aqui um GitHub Event Name.

05:37

Vamos tentar tirar esse cara aqui e vamos salvar. Já até marcou aqui como erro.

05:41

E vamos rodar essa pipeline de novo. Vou dar um CLI aqui no terminal.

05:45

E vamos rodar de novo esse Action Lint.

05:47

Aqui ele já achou que esse GitHub Name aqui não existe.

05:51

E aqui me dá todas as propriedades que a gente pode usar lá dentro.

05:55

Então, são esses erros que a gente tem que pegar.

05:58

Self-hosted, por exemplo. Esse erro de formatação mesmo.

06:03

Esse V4 aqui. Provavelmente ele vai aceitar. Vamos ver.

06:07

Ele aceitou porque ele não entende esse B4, mas algum erro de formatação,

06:11

algum if que não está legal, etc.

06:14

Ele vai criticar para você e vai te falar exatamente.

06:17

Onde está o erro e você pode corrigir. Então,

06:20

É sempre bom você fazer esse action link depois

06:24

Que você gerar uma pipeline com o uso de AI. Legal?

06:30

Só para ver se está tudo ok.

06:32

Além de passar por cada um dos steps aqui para ver se ele ressurgiu de fato.

06:37

O que você queria ali. Ok? Próxima etapa agora, o que a gente vai fazer?

06:42

Vamos fazer aqui um push para

06:45

Uma branch lá dentro do nosso repositório. Então, vamos lá.

06:51

Git checkout -b. O -b é para criar novas branches,

06:55

Então, a gente vai fazer aqui subindo, o nome da branch, né? Vamos colocar aqui.

07:01

Subir, workflow,

07:05

Deploy.

07:07

Vamos colocar esse nome de branch aqui.

07:10

Fiz o checkout para a branch.

07:12

Lembrando que, quando você estiver na branch main,

07:14

Para você não ter nenhum problema de branches desalinhadas,

07:20

Sempre faz um git pull dentro da branch main para ele baixar

07:24

Tudo que já foi colocado nesse repositório antes de você.

07:28

Então, vamos lá. git add ponto, para a gente adicionar tudo. Você poderia, o ponto aqui,

07:34

Ele pega tudo que você fez de alteração e adiciona.

07:36

Você poderia colocar o caminho completo do arquivo,

07:38

Que ele iria adicionar só aquele arquivo, tá?

07:40

Como a gente alterou só o deploy aqui que ele criou,

07:43

A gente vai colocar um git add ponto, ok?

07:48

Git commit -m, a gente vai colocar aqui uma mensagem de commit, tá?

07:54

O -m é para a gente colocar uma mensagem de commit. Então, vamos lá, subir.

07:59

Workflow de deploy para

08:05

Kubernetes. Ok?

08:09

Então, fazendo um commit, ok? Adicionei.

08:13

Vocês podem notar aqui que ele saiu do verdinho e agora já está aqui no cinza,

08:18

Na mesma cor dos outros, porque a gente adicionou ele. Fazer um git push origin,

08:23

Que é a branch atual, para o nome, o mesmo nome de branch que você criou.

08:29

Porque ele vai fazer o push lá para o GitHub. Então,

08:34

Feito isso, push feito para o GitHub,

08:36

O código já está sincronizado com a nossa branch remota,

08:40

Que no caso aqui é o nosso GitHub. Ok?

## Resumo IA

[RESUMO_IA]