Módulo: DevOps e SRE com IA\
Aula: [Hands-on: Manifests Kubernetes](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18503)

## Resumo da aula



## Transcrição

00:00

Ó, acabei de criar mais uma parte aqui,

00:02

que é a parte do StatefulSet do Postgres, ele já estava criando,

00:06

então demorou um pouquinho para criar por causa da questão que é muito grande,

00:10

né? O StatefulSet do Redis,

00:13

ele já está aqui com o Redis criando, e o Service para o Redis.

00:19

Então ele cria o Service e

00:20

aqui em cima ele cria o Postgres,

00:26

né? E logo abaixo aqui o Service para o Postgres.

00:29

Aqui o Redis e logo abaixo aqui o Service do Redis.

00:34

As aplicações vão se conectar no Service aqui.

00:37

O Deployment, que aqui é a nossa aplicação em si que está sendo executada.

00:42

O Service da aplicação expondo a porta 8000,

00:46

que é a porta padrão da nossa aplicação. O HPA,

00:49

que é a parte de escala. Se vocês notarem aqui,

00:52

ele vai pegar a CPU utilization se for acima de 70%.

00:59

Ele vai fazer a escala e aqui serve a mesma coisa para o pod,

01:04

se a CPU, a média de CPU estiver acima de 350 MB,

01:10

ele vai fazer a parte também, CPU, a verdade, a CPU vela é acima de 350 MB,

01:16

ele vai fazer também a escala do pod ali.

01:21

Aqui a gente tem a parte de Network Policy

01:24

e finalmente ele criou todos os arquivos lá,

01:28

um total de nove arquivos. Primeiro é o Namespace,

01:30

ConfigMap com as variáveis não sensíveis,

01:34

os Secrets com as variáveis sensíveis em base64,

01:38

PostgreSQL e um StatefulSet aqui e o PostgreSQL StatefulSet também. Agora,

01:44

com todos os arquivos criados,

01:48

a gente pode aplicar isso no nosso K3D

01:51

e ver a aplicação rodando em um cluster Kubernetes. Ok, pessoal? Arquivos gerados,

01:58

vamos continuar aqui para fazer a validação desses arquivos, beleza?

02:06

Primeira etapa,

02:07

vamos dar um clear aqui e vamos começar a aplicar os nossos serviços,

02:13

ok? A gente tem uma ordenzinha aqui de aplicação, o primeiro vai ser,

02:18

a gente já fez o build da imagem, né? Antes da gente,

02:24

normalmente as imagens elas são...

02:26

Explicar antes como é que funcionam essas imagens.

02:29

Normalmente elas são publicadas na internet,

02:31

ou publicadas em um repositório específico da internet, ou em um servidor SR,

02:37

seu, onde você tem toda a parte ali de guardar imagens dos seus serviços, etc.

02:44

Então, ele já busca essas imagens de um serviço específico. Porém,

02:49

essa imagem nossa não está publicada, ela está localmente no nosso serviço. Ok?

02:54

Então, basicamente, o que a gente vai fazer na primeira etapa aqui?

02:57

A gente já fez o build da imagem,

02:58

a imagem está disponível no Docker. Lá no K3D,

03:01

a gente tem um comandinho que vai chamar K3D image import,

03:09

import, aí a gente vai falar aqui qual que é a imagem,

03:13

app-api2.laytest,

03:18

ok, "-c mycluster".

03:27

Então aqui basicamente estou importando a imagem de

03:30

dentro do Docker para o meu cluster.

03:33

Então vamos dar um enter aqui para a gente fazer a importação da imagem.

03:37

Estou pegando a imagem que está deployada hoje,

03:40

que fez o build e está dentro do meu Docker

03:42

e coloquei para dentro do meu cluster K3D do Kubernetes.

03:50

Feito isso, nós vamos aqui criar a primeira parte.

03:54

Vamos dar um comando aqui antes, que é o

03:58

kubectlns.

04:05

Opa, getns, se eu tiver errado.

04:09

A gente tem aqui alguns namespaces que a gente

04:12

tem disponível lá dentro do nosso Kubernetes. Então,

04:16

o nosso namespace, vocês notaram que eu já falei um pouco antes,

04:21

o nosso namespace se chama epitemo -mba. Então,

04:27

a gente precisa criar esse namespace. O que é um namespace?

04:30

É um isolamento a nível de serviço, a nível de software,

04:35

dos contextos dentro do Kubernetes. Então,

04:40

um namespace é como se fosse um ambientinho separado dentro do Kubernetes,

04:44

que lá você pode criar diversas coisas que forem necessárias

04:48

para dentro daquele ambiente que você vai usar.

04:51

Então, na primeira parte, a gente vai dar um kubectl.

04:59

apply, "-f", que é menos arquivo, né, fdefile, k8s, barra,

05:04

namespace, dá um tabzinho que ele completa para você,

05:07

namespace .yaml. Então, ele simplesmente dá a mensagem para você, namespace,

05:13

demo app MBA criado. Ok? Então agora a gente vai dar de novo aquele outro comando,

05:19

kubectl get ns. Agora a gente tem aqui um demo app MBA.

05:25

com 11 segundos de criação. Foi criado há 11 segundos atrás,

05:29

que é assim que eu fiz o comando lá.

05:31

Legal? Então agora a gente vai fazer um outro comando.

05:34

Vou dar uma limpada na tela aqui,

05:35

vou só copiar o nome do nosso namespace,

05:40

dar uma limpada na tela e vou dar um kubectl

05:44

get pods menos n de

05:50

namespace e colocar no nosso namespace.

05:52

A gente não consegue ver Nenhum pod aqui dentro,

05:57

porque a gente não tem nada lá dentro.

06:01

Nenhum pod ainda disponível lá, ok? Na próxima etapa,

06:06

a gente vai criar um config map.

06:09

Então, vou copiar o comando aqui, vai ser mais fácil, não vou digitar tudo de novo,

06:13

mas eu falo com vocês qual que é o comando.

06:15

Vou dar um kubectl apply –f k8s configmap .yml.

06:21

Criou o config map lá dentro do meu namespace.

06:27

Feito isso, vamos para o próximo aqui.

06:32

Na verdade, vamos dar uma conferida se ele está lá.

06:36

kubectl get config map menos

06:42

n colo name do namespace.

06:45

Deixa eu pegar o nome do namespace, que eu já perdi ele aqui.

06:50

Demo app MBA.

06:52

Feito isso, a gente tem aqui API config map.

06:56

e aqui dentro o que eu precisava de configmap criado há 31 segundos atrás.

07:04

Detalhe, se vocês notarem, quando eu dou apply aqui,

07:09

eu não estou passando o namespace aqui,

07:11

mas dentro do arquivinho, vamos pegar aqui o configmap como exemplo,

07:16

A gente tem aqui o namespace definido, demo app BA,

07:20

Por isso que ele consegue ir para o namespace correto.

07:23

Então está tudo definido aqui dentro do nosso manifesto Kubernetes.

07:28

Ok? Bora para o próximo.

07:32

Já temos o ConfigMap. Vamos aplicar o Secrets aqui.

07:37

Ok? Criado o Secrets. Agora a gente vai fazer a criação do pod do Postgres.

07:45

Criei. O pod do Postgres tem dois manifestos lá dentro.

07:50

Tanto do Postgres quanto dos services do Postgres. O pod

07:55

do Redis criado.

08:00

Nossa aplicação depende do Postgres e do Redis para funcionar.

08:05

Então a gente vai fazer uma validação para ver se esses dois carinhas subiram.

08:11

Então aqui tem um comando que chama kubectl wait

08:15

for condition ready pod postgres -n timeout 120 segundos.

08:21

Então eu vou validar se o Postgres está criado. Então parece que o Postgres está ok.

08:27

Vamos dar um get pod para a gente verificar.

08:30

Então, kubectl

08:33

get pod,

08:39

menos n, o nome do namespace.

08:43

Vamos pegar aqui de novo o nome do namespace, demo app BA.

08:50

Nós temos dois pods, postgres e heads, criados lá dentro com status de running.

08:56

Eles já estão prontos para funcionar.

08:59

Ok? Então agora nós vamos dar um comandinho aqui para fazer o deploy da aplicação.

09:05

Agora que é a hora.

09:06

A gente vai fazer a subida da aplicação lá dentro do nosso ambiente Kubernetes. Ok?

09:15

Deu um erro aqui. Deploying enable.

09:18

Disable. Decoding erro. Failed. Expecting plate.

09:22

Read on the root file.

09:26

Error set. Pass request.

09:30

Ah, esse aqui é bem tranquilo. Então, a gente abriu aqui o deployment.

09:35

A gente consegue ver que esse read-only root file aqui não foi reconhecido.

09:40

File system. Mas aqui a gente pode pensar também,

09:43

se vocês se depararem com um erro, a gente vai copiar esse erro aqui.

09:48

Copiar toda a linha de comando,

09:51

voltar aqui no nosso editor de código e mostrar para ele qual é o erro que aconteceu.

09:57

E pedir AI para resolver. Então a gente consegue usar AI também para isso. Ok?

10:03

Então vamos ver o que ele vai dar de resultado aqui.

10:06

Está lendo no arquivo. Está fazendo o processamento.

10:11

Então ele simplesmente trocou aqui.

10:13

Ele trocou esse region file set para true.

10:16

Ele tirou já dentro do context level. E fez a aplicação aqui.

10:22

E está mandando a gente aplicar novamente.

10:25

Vamos testar agora para ver se vai funcionar.

10:27

Copiado o comando. Vamos comandar de novo.

10:30

E acabou de criar a nossa aplicação. Temos ela.

10:33

Então a gente consegue ver o poder da AI

10:35

também para a gente conseguir resolver alguns problemas.

10:38

Até o pessoal de SRE usa bastante para fazer isso. Legal?

10:43

Então, feito isso,

10:46

a gente agora vai criar as três últimas partes aqui,

10:50

que é o serviço que aponta para os nossos pods.

10:56

Criado o serviço.

10:57

E a gente pode aqui criar o HPA para fazer o autoscale do nosso pod,

11:02

criar o HPA e a Network Policy para a gente saber o que tudo que entra, o que pode sair,

11:08

o que pode entrar de fora para o nosso serviço.

11:11

Todos os nossos serviços estão criados,

11:14

todos os nossos manifestos de Kubernetes estão criados.

11:18

Vamos dar um clear aqui e vamos fazer alguns comandinhos aqui de kubectl

11:24

-get.

11:28

pod -n, vamos pegar de novo aqui, que deve ter mais espaço, demo -app -mba -n,

11:34

para a gente pegar o namespace, e aqui a gente tem todos os pods criados,

11:39

todos com status de running.

11:41

Então, a gente pode agora fazer um teste da nossa aplicação.

11:46

Como a nossa aplicação não está rodando no local,

11:48

ela está dentro de um cluster Kubernetes,

11:50

a gente precisa fazer um esquema que se chama port-forward.

11:53

O que é esse port-forward?

11:55

A gente consegue se conectar com o Kubernetes na nossa máquina e o

11:59

Kubernetes entrega uma porta do serviço dele para a gente na nossa porta local.

12:05

A gente faz essa conexão e a porta do serviço fica exposta localmente para a gente.

12:10

Assim que a gente vai conseguir fazer a chamada do serviço usando o localhost.

## Resumo IA

[RESUMO_IA]