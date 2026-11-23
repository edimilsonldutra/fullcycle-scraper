Módulo: DevOps e SRE com IA\
Aula: [Deploy do Fault Injection MCP](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18514)

## Resumo da aula



## Transcrição

00:00

A gente volta aqui para o nosso slide,

00:05

que agora a gente vai fazer de fato o deploy do nosso Fault Injection MCP.

00:11

Tanto tudo atualizado lá, vamos fazer aqui o deploy do nosso Fault Injection MCP.

00:16

Esse deploy, eu vou fazer ele localmente,

00:18

localmente não, sem passar por pipeline nem nada,

00:22

igual a gente fez a nossa stack de observabilidade aqui.

00:27

Porém, a gente vai criar aqui dentro de referência,

00:29

vamos renomear essa pasta de K8S? Vamos lá, K8S é observability,

00:36

observability é obs, traço, web -wide. Vamos renomear ela, e a gente vai,

00:43

já tem uma pastinha aqui criada com o código do nosso MCP de Fault Injection,

00:47

e a gente vai colocar aqui dentro de referência a nossa Fault Injection,

00:51

beleza? O que temos aqui dentro da nossa Fault Injection?

00:56

Temos aqui... Dois arquivos de deploy.

00:59

Dois arquivos de deploy, não. Dois arquivos de manifesto Kubernetes.

01:02

Então, a gente tem aqui um deployment .yaml,

01:05

que já está todo preenchido.

01:07

Esse cara vai responder na porta

01:09

8000 dentro do nosso namespace de observabilidade, tá bom?

01:16

Na verdade, vai responder na porta 8000, não, né? Aqui a gente tem o health dele,

01:19

né? Para verificar se ele está de pé, tudo certinho.

01:22

E aqui no service... ele vai deployar algumas coisas de service and account,

01:27

vai colocar algumas habilidades para esse agent conseguir

01:29

simular os erros dentro do Kubernetes.

01:32

Então, esse cara consegue fazer algumas operações dentro

01:34

do Kubernetes para quebrar o serviço,

01:37

gerar erros 500 e assim por diante. Então,

01:41

a gente consegue ter essa habilidade aqui nesse servidor MCP.

01:45

E aqui a gente vai ter um API RBAC authorization,

01:49

que vai dar liberação aqui para o service account e por fim

01:53

o nosso service que de fato aqui vai responder na porta 8000, ok?

01:58

Aqui o script deploy,

02:00

simplesmente um ponto sh aqui que vai fazer para a gente a geração,

02:05

o build e o import da imagem,

02:07

então vou fazer o build desse Dockerfile aqui,

02:10

vou fazer o import dela para dentro do nosso cluster

02:13

e por fim vou aplicar a stack aqui.

02:17

Deixa eu dar uma olhada, ele está pegando K8S, isso mesmo, scriptdir é K8S,

02:22

ele vai fazer a aplicação aqui dentro do nosso Kubernetes.

02:25

O nosso arquivo Dockerfile, que vai fazer aqui o update,

02:29

basicamente, vai fazer a instalação do requirements,

02:32

vai copiar o service .py para o ponto,

02:36

vai expor a porta 8000, vai fazer um python serve .py e vai subir.

02:42

O requirements, que simplesmente vai usar só o Flask MCP, e aqui a gente tem todo,

02:49

todo o serviço pronto.

02:52

O nosso MCP aqui prontinho para funcionar.

02:56

Então aqui eu removo fault e aqui o inject fault para

03:00

a gente conseguir quebrar as coisas lá dentro do Kubernetes.

03:04

Quebrar para fins de teste.

03:06

Então esse cara aqui é só para a gente conseguir fazer alguns testes.

03:10

Então basicamente você vai dar um MCP .run transporte

03:13

stream.http na porta no roast 000000 na porta 8000,

03:20

que a gente vai rodar esse carinha aqui, ok? Então vamos lá,

03:24

vamos rodar nosso script aqui, terminal, novo terminal, observability,

03:30

então a gente vai dar um ponto barra, referência, fault, injection,

03:36

deploy.sh. Vamos testar, está importando, está fazendo o build da imagem.

03:42

e ele deu um problema, vamos descobrir o que que tem de problema

03:45

aqui requirement copy requirement.txt, ele não

03:51

conseguiu copiar o arquivo e não conseguiu

03:55

copiar aqui debaixo apt-get copy, ele deu um problema no copy, vamos olhar

04:01

aqui o nosso talker file de novo

04:03

copy requirement.txt

04:08

então vamos dar um

04:11

.requirement.txt aqui e vamos

04:14

dar um .requirement.py aqui.

04:19

Vamos dar um clear aqui e vamos tentar rodar de novo. Clear.

04:24

Vamos tentar rodar de novo.

04:28

Ok. Temos um novo problema.

04:30

Ele conseguiu copiar o requirement agora. Funcionou. Conseguiu instalar, inclusive.

04:34

Só que esse cara aqui não conseguiu copiar, que é o server.py. Virou para ponto.

04:41

Vamos ver.

04:45

Toquei. Deixa eu entender o que está acontecendo. Vamos salvar aqui de novo.

04:49

É isso aí. Ao vivo dá problema mesmo. Vamos testar.

04:55

Não está conseguindo copiar nem expor a porta 8000 aqui.

05:00

Porque ele está parando na parte de copy.

05:04

Vamos ver aqui o problema. Vamos dar uma olhada aqui no deploy.sh.

05:08

Quando ele faz o build, tem o "-t", que eu vou dar o nome.

05:14

Lasted, aponto o arquivo, Dockerfile, e passo mais uma variável, que é o scriptd. Ah,

05:20

ele está dando um ponto, ponto aqui.

05:22

Esse ponto, ponto está voltando na pasta anterior.

05:27

Acredito que é isso. Vamos testar.

05:30

Fechar. Aqui a gente tem um ponto barra.

05:32

Acredito que nem vai precisar do ponto barra aqui mais,

05:34

porque agora ele vai trabalhar na pasta certinha.

05:37

Vamos dar um clear aqui e vamos fazer o deploy de novo.

05:43

Ó, conseguiu fazer, fez a instalação, aí ó,

05:46

conseguiu. Agora, a partir desse momento,

05:48

a gente já tem as imagens criadas lá dentro do nosso K3D, ok?

05:54

Vamos olhar dentro do nosso K3D. A gente tem as imagens aqui. Na

06:07

verdade, eu quero o namespace, as imagens não, né? Quero o namespace aqui.

06:12

Namespace, open web UI.

06:15

E ele

06:17

criou o deployment.

06:21

Vamos ver o comando que a gente fez aqui. Ele aplicou o K8S aqui.

06:26

Scriptdir K8S. Em teoria, era para ter aplicado.

06:31

Deployment criado. Está tudo criado.

06:35

Create inspection. Tudo criado. Vamos ver aqui porque ele não subiu. Deploy.

06:43

Engfusing. Eu estou no namespace certo.

06:47

Estou. Open UI. Está aqui.

06:51

Vamos ver aqui o namespace. Observability.

06:57

Ah, aqui, ó. Estamos no namespace errado.

07:01

Ele está criando dentro de observability aqui.

07:04

Criou, mas está com algum problema. Estou tomando um 404 aqui, not found. Então,

07:11

acaba que ele não consegue entender que o serviço está de pé.

07:16

Tá bom? Então, esse problema aqui é simples de resolver.

07:22

Inclusive o Kubernetes acabou de derrubar ele porque

07:24

ele não conseguiu fazer o health check.

07:26

Então vamos fazer um ajuste aqui dentro do nosso server .py.

07:31

A gente vai adicionar aqui dentro um comando

07:37

que além de subir esse mcp run transporte aqui,

07:41

a gente vai subir uma rota de

07:46

HTTP onde a gente consegue fazer o health.

07:51

um transporte stream HTTP.

07:53

Ele vai ser só um HTTP simples para ele fazer um health check ali.

07:59

Vamos fazer isso aqui dentro do nosso serviço aqui agora.

08:03

Aqui vai ser uma rota simples que a gente vai adicionar somente um HTTP aqui.

08:10

Então vamos lá no início do código. Vamos dar aqui um from start

08:18

start

08:28

starlet .response

08:30

import

08:35

jsonResponse

08:41

ok?

08:44

só para a gente conseguir usar um jsonResponse aqui porque ele

08:49

é um pouquinho diferente aqui do nosso do nosso resposta de mvcp Tá bom?

08:55

Então a gente vai importar isso aqui pra gente conseguir dar um JSON response.

08:58

E aqui logo no início mesmo, vamos tirar em cima do MCP,

09:03

da primeira MCP tool aqui,

09:05

a gente vai dar um arroba MCP ponto custom

09:12

custom

09:15

route a

09:19

gente vai colocar um entre aspas aqui um barra health vamos

09:25

pegar certinho como que ele tá fazendo um health check aqui.

09:29

No deployment, a gente vai fazer um barra health aqui. Vamos fazer um barra health.

09:33

E ele vai ser do tipo method.

09:38

O tipo dele vai ser igual a um get aqui. Um get.

09:49

Vamos fechar aqui o parêntese. Basicamente, ele vai ser um async. Async. Async.

10:04

Async. Def.

10:06

Vai ser aqui uma função que vai se chamar health

10:15

check. A

10:22

gente vai chamar ela aqui de request.

10:28

Ok? Dois pontos. E a gente vai fazer só um return simples aqui. Return.

10:35

E a gente vai pegar aquele JSON response que a gente criou.

10:39

Vai abrir aqui. Abre e fecha parênteses.

10:43

E a gente vai retornar somente um status aqui. Status, dois pontos, health,

10:51

string health,

10:56

é isso mesmo?

10:59

Health, é isso mesmo, correto.

11:03

Status health,

11:05

vírgula, service, ficou sem aspas duplas,

11:11

service, dois pontos, mcp. MCP,

11:23

vamos pegar

11:26

O nome do nosso MCP aqui, a gente tem o nome dele, Fault Injection MCP.

11:34

Ok, temos aqui um retorno.

11:37

Lembrando que tudo isso aqui é entre chaves,

11:43

a gente fazer um JSON aqui. Ok? Temos aqui a nossa rota de health check já.

11:51

Precisamos disso para quê? Para o nosso Kubernetes não matar o nosso pod.

11:55

Então ele vai lá e fica fazendo um health check

11:58

desse cara e não vai matar o nosso pod,

12:01

tá bom? Então vamos criar aqui uma nova imagem.

12:04

Vamos dar um clear aqui e vamos aqui fazer uma criação da nova imagem.

12:11

Então ponto barra referente Fault Injection deploy ponto sh.

12:15

Vamos fazer aqui e subir. Vamos ver se vai dar tudo certo.

12:20

Espero que eu tenha digitado aqui o

12:24

código certinho. Feito aqui, né?

12:28

Já subiu o MCP. Vamos ver lá dentro do nosso Kubernetes o que a gente tem.

12:33

Vamos matar esse cara aqui e subir de novo.

12:37

Ó, tudo running.

12:41

Opa, no modeling. State let response. Ah,

12:45

a gente tem que fazer aqui uma... instalar esse statlet aqui.

12:51

Então, vamos fazer um pip lá,

12:53

vamos colocar nas nossas variáveis de requirements lá, esse statlet aqui.

12:58

Statlet, na verdade.

13:01

Vamos lá nas nossas variáveis de ambiente, e vamos,

13:04

variáveis de ambiente não, do nosso requirements adicionar isso.

13:08

Voltamos aqui no projeto, viemos aqui em requirements,

13:12

vamos colocar aqui o statlet, igual,

13:16

vamos ver qual que a gente está usando. Pip 3 list, a gente está usando aqui, o

13:22

STANET0413, só para a gente manter a compatibilidade.

13:28

Vamos colocar aqui, salvar, salvar aqui. Vamos de novo, fazer um novo deploy.

13:36

Direction, SH.

13:41

Ok, tivemos um problema.

13:45

Ah, tivemos um problema aqui para instalar.

13:50

Ah, igual, igual, coloquei errado. Igual, igual.

13:55

Boa. Agora sim, vamos lá. Problemas ao vivo,

13:58

no meio da demo, acontecem nas melhores famílias.

14:03

A gente vai fazendo os debugs e vai fazendo

14:06

os ajustes aqui conforme a gente vai evoluindo.

14:09

Feito isso, está criando a imagem,

14:11

fazendo a importação da imagem lá dentro do Kubernetes e

14:15

agora rodando o deploy. Feito isso, vamos lá olhar nosso sistema.

14:23

Vou dar aqui um restart. Vamos criar, criou aqui. E

14:32

ainda não deu. Vamos ver o porquê.

14:37

NoModuleStart.Response. NoModuleNotFound.

14:43

Ok. Ainda temos um problema.

14:47

Por que ele não instalou o módulo agora? Deixa eu ver aqui. Deploy.

14:53

Vamos deletar esse deploy. Vamos lá.

14:57

Pode. Beleza. Deploy. Deploy. Start.

15:03

Ok, temos aqui. Vou fazer um teste aqui. From standard

15:10

.response import

15:15

JSON response. Tá tudo certinho aqui. O que ele não encontrou? Boa pergunta.

15:24

Vamos tentar fazer aqui de novo.

15:27

Um novo deploy.

15:31

Ele está fazendo lá o deploy da laced, né?

15:35

Ok, laced. Importou.

15:40

Vamos ver se vai subir.

15:43

Ah, ainda com problema.

15:46

Vou investigar esse problema aqui e já retorno para entender por que

15:50

está acontecendo e já retorno com a solução para mostrar para vocês.

15:54

Pessoal, investigando aqui, consegui achar o problema.

15:58

E para quem é desenvolvedor e programador,

16:01

sabe que o problema mora naquele ponto e vírgula que falta no final do código.

16:07

Então, o que eu notei aqui?

16:09

Olhando certinho a documentação aqui de como criar esse...

16:15

Esse custom route aqui.

16:17

Eu notei que aqui não é response. É responses.

16:21

Então, errei nessa parte.

16:24

Então vamos compilar de novo aqui. E vamos...

16:28

E vamos subir uma nova imagem.

16:33

Então, referência aqui. MCP injection deploy. Mesma coisa. Gerar uma nova imagem.

16:40

E vamos copiar o nosso cara novo lá. Nosso server.

16:45

E está feito.

## Resumo IA

[RESUMO_IA]