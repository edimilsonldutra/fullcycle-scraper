Módulo: DevOps e SRE com IA\
Aula: [Pipeline de Deploy pt5](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18524)

## Resumo da aula



## Transcrição

00:00

Se precisar refazer o deploy, como que a gente precisa fazer?

00:04

Nós vamos aqui no cantinho, a gente tem uma parte aqui de summary,

00:09

na verdade na tela anterior.

00:12

Nessa tela aqui a gente tem, clica no seu workflow,

00:16

aqui vai ter uma lista de workflows,

00:17

você vai clicar nele e aqui você vai dar um run workflow e vai colocar

00:21

aqui qual que é o workflow que você quer rodar de maneira manual.

00:23

No caso aqui o deploy, se eu clicar aqui em deploy ele vai rodar.

00:27

Toda a minha parte de deploy de novo em cada

00:30

um daqueles steps que a gente rodou anteriormente.

00:33

Só que esse deploy é um job só para rodar todas as etapas.

00:39

Lá a gente separou em três jobs,

00:41

que foi o test, o build e por último o deploy.

00:45

Se a gente rodar aqui é um job só que vai fazer todas as etapas no mesmo job.

00:49

Poderia separar também, se fosse o caso.

00:55

A gente tem aqui dentro do nosso Merge a parte de Destroy também.

00:59

Se a gente vier aqui,

01:01

podemos fazer também o Destroy do nosso ambiente.

01:05

Mas antes de fazer o Destroy do ambiente,

01:07

aqui você pode selecionar em qual branch você vai rodar.

01:10

Se você quiser, por exemplo,

01:12

rodar um Action lá na branch XPTO aqui,

01:16

você pode também rodar em outras branches, não necessariamente só na main.

01:20

Porque ele vai usar os arquivos daquela branch como

01:24

base para fazer o deploy para você. Então,

01:27

feito o deploy, a gente pode vir aqui dentro do nosso Kubernetes.

01:33

Vou mostrar para vocês aqui uma outra ferramenta também,

01:36

que eu não listei lá no começo,

01:38

que é uma ferramenta para a gente conseguir administrar o nosso Kubernetes. Então,

01:42

vocês podem usar essa ferramenta, é bem simples de instalar, pode pesquisar na web.

01:49

Mostrar pra vocês aqui o que que é. Ó, dá um Google aqui,

01:52

K9S, que basicamente é um Manager Kubernetes aqui,

01:56

que é uma interfacezinha mais amigável pra gente usar o Kubernetes,

02:00

tá? Então, é uma interface bem amigável,

02:03

posso soltar o vídeo aqui, eu vou falar um pouco dela aqui já já,

02:05

que vocês conseguem administrar o seu Kubernetes de maneira mais simples.

02:11

Então, só vocês instalar que você consegue usar essa CLI aqui do K9S, ok?

02:17

Então vamos aqui dentro do nosso cluster do Kubernetes,

02:21

dá um K9S, ele automaticamente vai abrir o seu cluster,

02:24

e aqui a gente já tem, vamos colocar aqui os namespaces,

02:27

a gente tem aqui os namespaces que a gente tem,

02:30

nosso namespace é o demo-apple-mba,

02:32

se você clicar dois pontos,

02:35

você pode selecionar qual que é o objeto Kubernetes que você quer usar,

02:39

que você quer ver, na verdade. Então, por exemplo, dois pontos, pod,

02:43

a gente vai conseguir ver todos os pods, a gente consegue ver aqui que o...

02:47

App API está ligado e está aqui com o Health Check fazendo bonitinho. Então,

02:52

a gente consegue ver que ele está de pé. O segundo pod dele também está de pé aqui.

02:58

O Postgres também, se a gente entrar,

03:00

ele está aqui listando e funcionando bonitinho.

03:03

Legal. O Heads também está aqui, legal.

03:06

Funcionando bacana. A gente pode vir aqui em Services, por exemplo. Service.

03:11

Dois pontos. Service.

03:13

Você consegue ver todos os serviços que foram criados, ok?

03:18

ConfigMap, mesma coisa, a gente consegue ver os serviços que são criados,

03:23

por exemplo, AppConfig,

03:24

aqui a gente tem todas as variáveis de ambiente que

03:27

a gente está usando dentro do nosso projeto,

03:31

ok? E a gente tem também aqui os Deploys,

03:37

que aqui é o Deploy do nosso FAPI. E o StatefulSet,

03:41

que é o deploy das nossas duas aplicações.

03:43

Posting dos SQL e o Heads aqui. Voltando para o pod,

03:46

a gente consegue ver que está tudo de pé.

03:49

Podem usar o K9S, é bem bacana, é bem mais simples.

03:52

Se vocês preferirem também, podemos usar também o kubectl.

03:59

kubectl get pods -n,

04:05

que é o namespace,

04:06

que agora eu esqueci.

04:09

Vamos lá, deixa eu get ns, opa,

04:13

esqueci qual que é o código get namespace que é

04:18

o ns que é a abreviação de namespace,

04:20

nosso namespace é esse demo app mba, então aí a gente

04:25

pode pegar o nosso namespace aqui agora e vamos dar um kubectl

04:32

get pod -n de namespace, colar,

04:37

o nosso namespace, esqueci do L aqui.

04:42

Foi. Temos aqui nossos apps. Se vocês quiserem também usar o kubectl,

04:47

fiquem à vontade para usar qualquer um dos dois aí, tá bom?

04:51

Dando zoom aqui para vocês conseguirem ver melhor.

04:54

Então aqui a gente tem a idade do pod e assim por diante.

04:57

Vamos voltar lá para o K9S para

05:02

a gente ver quando a gente rodar o Destroy,

05:03

esses caras aqui morrendo, tá? Então vamos aqui dentro do nosso...

05:09

Do nosso deploy app API. Vamos rodar um workflow.

05:12

Run workflow. Vamos rodar aqui um destroy. Beleza?

05:16

Dá um run workflow. Ele vai subir todo o workflow.

05:19

Porém, ele vai rodar só o destroy aqui.

05:24

Está esperando aqui.

05:28

Ele fez aqui erro server. Deu alguns problemas aqui de erro.

05:32

Porém, ele já matou todos os jobs aqui.

05:35

Se a gente voltar aqui no Kubernetes,

05:36

a gente não tem mais nenhum cara aqui. Não temos services também.

05:40

Então sumiu, não temos config map, tá vendo?

05:45

O config map continuou, na verdade, ele não destruiu. Temos o config map,

05:49

né? Mas a gente tem aqui, por exemplo, StatefulSet,

05:52

não temos mais nenhum, não temos mais nenhum deploy, nem nada.

05:57

Então aquele comando, ele matou totalmente nosso ambiente aqui, tá?

06:03

Novamente, aqui nosso ambiente, nós temos somente essa aplicação.

06:08

Então você pode rodar um destroy em tudo.

06:11

Mas, no caso, se você estiver em um ambiente com mais aplicações,

06:14

sempre tenha algum job de purge para você tirar aquilo.

06:20

Ou até um job de rollback, que você guarda a imagem anterior.

06:24

A gente tem aqui a imagem 11, né? Se vocês guardarem a imagem anterior, a imagem 10,

06:31

vocês conseguem fazer o rollback para a imagem anterior.

06:33

E é possível a gente programar isso tudo dentro aqui do Kubernetes Jobs.

06:39

Do Kubernetes Jobs não, gente. Desculpa. Dentro do... Fui longe agora.

06:44

Dentro do workflow lá do GitHub, ok? Da parte de Actions.

06:49

Fechou? Então a gente conseguiu fazer todo o deploy

06:53

aí da nossa aplicação de maneira automatizada.

06:56

Fizemos um push para dentro de um repositório do Git,

06:59

onde a gente consegue versionar,

07:00

ter todas as etapas ali do que foi feito no programa, de melhorias, etc.

07:07

Conseguimos fazer backup, conseguimos fazer build,

07:10

conseguimos fazer tudo dentro do workflow de deploy. Então,

07:16

basicamente, essa é a função da pipeline para ajudar a

07:21

gente no nosso dia a dia com o CI e CD.

07:25

Próxima etapa da agora, a gente vai falar um pouco da pipeline de segurança.

07:30

Vou encerrar esse vídeo com essa parte de pipeline,

07:34

e volto em seguida para a gente falar um pouco da etapa de pipeline de segurança,

07:39

que a gente vai adicionar alguns jobs de segurança antes de fazer o deploy de fato.

07:45

Fechou? Valeu, galera. Um abraço.

## Resumo IA

[RESUMO_IA]