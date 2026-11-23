Módulo: DevOps e SRE com IA\
Aula: [Hands-on: Ambiente local, Dockerfile e Docker Compose](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18517)

## Resumo da aula



## Transcrição

00:00

A primeira parte que a gente vai fazer vai ser subir uma infra-local.

00:04

O que é essa infra-local? Ela vai subir para mim um pod, não um pod,

00:10

vai subir um container para mim dentro do Docker

00:13

de Postgres e um container do Redis,

00:16

que a aplicação pede isso.

00:18

Então, ao invés de eu rodar ela local,

00:19

eu vou rodar essas duas partes da aplicação já em containers Docker.

00:25

Então, vamos rodar aqui a infra-local.

00:28

Faltou um comandinho aqui no final, que é o up, e ele vai subindo.

00:32

Ok. Se a gente vier aqui no nosso Docker Desktop,

00:37

a gente já tem o MBA Postgres e o MBA

00:40

Heads aqui sendo executados dentro do nosso Docker Desktop aqui.

00:50

Voltando aqui no Code, a gente agora vai subir a aplicação.

00:55

Vou dar um clear aqui, só para a gente conseguir...

00:58

Deixar a tela mais limpa e

01:00

vou dar um python3 -m app.main.

01:06

Basicamente, eu estou subindo a aplicação. Ela fez a conexão no banco de dados.

01:11

Então, aqui fez a conexão no banco de dados.

01:15

Aqui já fez as migrações do LNBIC, que simplesmente criou a tabela lá dentro,

01:20

criou o database e fez a conexão no Redis.

01:24

Agora, a gente pode fazer um teste aqui dentro da aplicação.

01:28

Eu estou usando aqui um HTTP 0002.8000/health.

01:34

Vou dar um send aqui.

01:36

Você vai ver que o status vai estar health e a versão 1.0.0. Ok?

01:41

Eu vou procurar aqui os itens que têm lá no banco de dados.

01:44

Vocês estão vendo que estão vazios. Ok?

01:47

E eu agora vou inserir um item lá dentro. Vamos inserir esse cara aqui.

01:53

Inseriu. Feito isso, ele vai aqui dando os logs para mim, mostrando o /health,

01:58

a listagem de itens e aqui a inserção do item. Isso tudo rodando localmente.

02:03

A gente não está rodando a aplicação ainda em Docker.

02:06

Ela está rodando dentro da máquina, está sendo executada dentro da minha máquina.

02:10

E por último, a gente consegue ver que dentro do banco de dados,

02:14

esse aqui é o banco de dados que está criado lá dentro do Docker,

02:19

o esquema public.

02:22

E aqui as tabelas, a gente tem a tabela de itens com essas colunas.

02:26

Se a gente dá um select aqui,

02:27

a gente vai conseguir ver que o item que eu inseri vai estar aqui.

02:31

Memória RAM, tal, tal, tal, tal, tal, tal, tal.

02:34

Feito isso, a gente pode vir aqui e fazer o delete daquele item.

02:39

Respondeu 204 e a gente vem aqui fazer o select de novo.

02:43

Esse item não vai estar mais aqui presente.

02:46

Então, isso tudo fazendo a aplicação rodando localmente.

02:50

com os logs informando cada uma das etapas que a gente fez lá.

02:54

Combinado? Então, conseguimos ver que a aplicação está funcionando. Agora,

03:01

a próxima etapa é a gente gerar o Dockerfile para a

03:04

gente subir essa aplicação dentro de um container Docker.

03:08

Porque aí eu não vou rodar ela mais local. Eu já estou rodando em Docker.

03:11

Já está meio que simulando ali uma execução desse container dentro de um Kubernetes,

03:17

por exemplo. Só que está em Docker por enquanto.

03:20

Combinado? Então, vamos para a próxima etapa.

03:23

Nessa etapa agora, vamos gerar o Dockerfile.

03:27

Vamos aqui matar a aplicação que está rodando localmente.

03:32

Aplicação desligada.

03:38

Agora, vamos fazer a geração do Dockerfile usando o OpenCode.

03:44

OpenCode aberto dentro do projeto do app.

03:47

Vou copiar todo aquele prompt que a gente passou por ele. Ok?

03:52

Pronto, está copiado. Quando a gente colar aqui,

03:54

o OpenCode não mostra todo o conteúdo nessa tela,

04:01

só quando a gente dá um Enter na tela. Então,

04:04

quando a gente dá um Enter, basicamente,

04:06

ele vai mostrar todo o conteúdo que a gente tinha

04:08

passado para gerar o Dockerfile com todas as definições. Aqui,

04:13

ele está usando o modelo GLM 5.1 do OpenCode Go. Então, basicamente,

04:18

ele conseguiu gerar aqui para mim.

04:20

O meu Dockerfile e criou o Dockerfile no repositório raiz.

04:25

Então, se a gente vier aqui, agora a gente possui um Dockerfile definido.

04:29

Vamos limpar a tela e vamos ver o conteúdo desse Dockerfile.

04:37

Primeira parte, está usando aqui a imagem slim que a gente definiu lá para ele usar.

04:41

A gente está usando aqui o apt-get para fazer

04:45

o update do sistema operacional

04:49

da imagem e fazer a instalação.

04:52

De algumas coisas recomendadas aqui,

04:54

que é o curl e fazer a remoção de outras coisas.

04:57

Dá um copy no requirements.txt,

05:00

a gente tem uma lista aqui com todas as bibliotecas

05:04

que a gente precisa para o nosso projeto,

05:06

e aqui nesse momento ele faz esse copy

05:08

e faz a execução do install desses requirements,

05:13

ok? No segundo momento, ele vai fazer o runtime,

05:17

então aqui ele fez o build e aqui ele faz o runtime.

05:20

Que é definir as variáveis e adicionar as coisas aqui dentro da aplicação.

05:26

Primeiro, ele fez a instalação das bibliotecas,

05:30

agora ele está copiando de fato a aplicação lá para dentro.

05:35

Na última etapa, a gente tem um CMD,

05:38

que é simplesmente o comando que vai fazer a execução da nossa aplicação.

05:43

Então, a gente consegue aqui fazer alguns testes.

05:48

Fazendo um docker build.

05:50

Então, a gente consegue vir aqui e fazer o build dessa imagem.

05:53

Então, vamos buildar ela. Então, vai lá, docker, comando é docker build,

06:01

ok, menos t, que aqui é o nome da aplicação,

06:06

vai ser app-api,

06:10

dois pontos. Aqui é a versão dela, né? Então, vai ser latest.

06:16

Que é a última, normalmente latest é a última versão estável,

06:21

ou a última versão que foi lançada, latest, escrevendo

06:29

errado, aí fica difícil, latest, ok, aí ponto,

06:33

porque ele vai usar esse arquivo Docker aqui, que está nessa raiz,

06:39

para fazer o build dessa imagem, então, vamos fazer o build dela,

06:43

ele vai iniciar, fazer a primeira etapa,

06:46

e vai começar a fazer a instalação,

06:48

a primeira etapa aqui está fazendo a instalação do sistema operacional.

06:51

E aqui já está fazendo a instalação dos componentes Python,

06:56

das bibliotecas Python que são necessárias ali para o projeto.

07:02

Está fazendo a exportação da imagem, criando, feito.

07:05

Então a imagem já está criada e disponibilizada no nosso Docker.

07:10

E agora a gente consegue validar a imagem usando o comando do Docker.

07:16

Images, e a gente consegue ver que ela está aqui,

07:22

a primeira imagem. Ela tem um tamanho de 114 MB,

07:27

então ela tem aquele tamanho mais ou menos igual que

07:31

a gente pediu lá nas definições da criação do Dockerfile.

07:36

Então é muito importante a gente definir o Dockerfile sempre nos mínimos detalhes.

07:42

Colocar qualquer aplicação, se é um FastAPI,

07:46

se é qualquer outro tipo de aplicação que você está rodando,

07:49

vou colocar qualquer versão que você está usando,

07:52

quais são os arquivos de dependência, por exemplo,

07:55

o requirements.txt, a porta que vai ser a exposição, o tamanho máximo da imagem,

08:01

então tem muita importância nessas definições do tamanho da imagem.

08:06

E se você também quiser ver ao invés só pelo comando docker images,

08:12

Se você quiser ver também pelo Docker Desktop,

08:15

a gente consegue acessar a imagem por aqui também.

08:18

Ela vai estar disponível aqui.

08:19

E aqui tem alguns layers dela que você consegue ver. Como, por exemplo,

08:25

qual é o comando que está acontecendo, qual é o usuário que está rodando,

08:31

qual é a porta que está exposta. Então,

08:32

você consegue ver mais alguns detalhes.

08:34

E qual é o comando que vai ser feito no

08:37

final do processo para subir a sua aplicação em si.

08:42

Então você pode ter mais detalhes lá no Docker Desktop. Beleza?

08:47

Então, próxima parte agora,

08:49

a gente vai fazer a geração do Docker Compose para

08:53

fazer a subida de toda a infraestrutura necessária para a criação,

09:00

para o uso da aplicação ali no Docker. Então a gente tem o Dockerfile,

09:05

porém a gente não tem ainda, a gente teria que subir manualmente,

09:09

o Postgres e o Redis que a aplicação usa para fazer a conexão.

09:14

O Docker Compose vai ajudar a gente nisso.

09:16

A gente vai criar uma cadeia de criação de artefatos,

09:22

de criação de serviços para disponibilizar a aplicação somente com um comando.

09:28

Então vou limpar aqui a tela,

09:31

vou tirar o Dockerfile aqui da tela, criar aqui

09:38

um arquivinho vazio só para mostrar para vocês aqui qual que é

09:41

o prompt que a gente vai usar para gerar o nosso Docker Compose.

09:47

Copiar ele aqui e

09:50

aqui o prompt. Então, o que a gente tem?

09:54

Geração do Docker Compose para

09:56

desenvolvimento local de uma aplicação FastAPI.

10:03

O Compose deve ser... consistente com o Dockerfile, ou seja,

10:08

eu estou mostrando para ele que ele tem

10:10

que usar esse Dockerfile e os Manifest Kubernetes.

10:15

A gente não criou os Manifest Kubernetes,

10:17

mas ele vai criar com o padrãozinho ali do Manifest Kubernetes, ok?

10:21

Então, contexto da aplicação. A gente vai dar o nome,

10:23

Vai mostrar quais são os frameworks que estão sendo usados,

10:26

Os arquivos de entrada, a porta, os requirements, assim por diante, e falar.

10:32

Que ele está usando o Dockerfile.

10:34

Então a aplicação vai usar o Dockerfile aqui, o Dockerfile multistage já existente.

10:40

Então o container name vai ser esse,

10:42

Então ele vai criar esse container para a gente lá dentro do Docker.

10:48

Aqui algumas variáveis de ambiente como banco de dados que ele vai usar,

10:53

Qual é o host que ele vai usar,

10:55

Qual é o Postgres que ele está usando e assim por diante. Tudo definido aqui.

11:01

Dentro das nossas variáveis de ambiente.

11:03

Ok? Então aqui tem um health check,

11:05

Que a gente consegue fazer um curl aqui, fazer um teste,

11:08

A gente consegue fazer esse health check tanto pela linha de comando,

11:13

Quanto lá pelo Postman, igual a gente fez naquela hora.

11:15

Aqui os volumes que ele vai criar. Aqui as regras do Postgres,

11:20

Para ele subir. As regras do Redis,

11:23

Para ele subir o Redis. E aqui alguns requisitos, como a versão 3.8 ou superior.

11:30

O network deve ser definido como bridge,

11:32

Que vai ficar somente internamente. Os volumes,

11:36

É importante definir a database URL,

11:40

Que é onde ele vai fazer a conexão com o banco de dados.

11:44

Comandos de start para dev, deve ser autoreload e assim por diante.

11:49

Então a gente tem várias definições aqui,

11:51

Que de novo, por que fazer com o prompt? Por que é mais fácil?

11:57

O prompt pode ser reutilizado em outras aplicações e

12:01

A gente pode fazer várias aplicações com o mesmo prompt. Então,

12:08

O Dockerfile pronto,

12:10

O serviço vai criar várias etapas para subir tanto a aplicação quanto

12:15

O Postgres quanto o Redis e motivo que gerar o prompt ali.

12:19

E o contexto já vai concluir o SLO.

12:23

Todas as etapas ali que precisa para a aplicação funcionar. Então,

12:28

A gente vai fazer a subida desse cara. Vamos copiar aqui o prompt.

12:34

Na mesma telinha do OpenCode, você vai colar o prompt,

12:38

Vai aparecer sim, mas quando você der o Enter,

12:40

Ele vai aparecer todo o texto completo aqui.

12:43

E assim já está começando a fazer a geração do nosso Dockerfile.

12:49

Desculpa, nosso Docker Compose, que é...

12:51

Toda a workflow para gerar todos os componentes necessários.

12:58

Então ele já conseguiu criar o Docker Compose aqui. Vamos lá dar uma validada nele.

## Resumo IA

[RESUMO_IA]