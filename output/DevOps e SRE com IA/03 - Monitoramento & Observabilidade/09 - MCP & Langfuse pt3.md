Módulo: DevOps e SRE com IA\
Aula: [MCP & Langfuse pt3](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18535)

## Resumo da aula



## Transcrição

00:00

Vamos fazer mais um teste,

00:01

mas agora a gente vai colocar aqui a chamada de função nativa. Então vamos lá.

00:06

Vou fazer a mesma pergunta adicionando aqui a ferramenta de novo do Kubernetes.

00:13

Legal? Vamos mandar. A

00:16

ferramenta aqui, ela vai pesquisar.

00:19

Vamos ver.

00:24

Ok, está pensando.

00:27

Explorando o LustTools.

00:29

Então aqui ele já conseguiu fazer uma...

00:34

tool list do K8S, já tentou explorar, já viu o resultado aqui,

00:38

a gente tem a possibilidade tool list K8S resource post,

00:42

então ele já conseguiu retornar esses resultados e tem aqui todos os negócios.

00:47

Então, qual que é legal do nativo?

00:49

Ele fez duas chamadas, tá vendo? Ele pode fazer mais de uma chamada por vez,

00:55

ele pode orquestrar isso melhor pra você.

00:58

Então vamos fazer aqui de novo,

00:59

vamos fazer uma pergunta um pouco mais complexa agora.

01:03

Olhe meus pods e

01:06

verifique qual deles tem maior

01:12

recurso e

01:18

quais deles têm pouco recurso e

01:24

eu posso e eu devo aumentar ou

01:32

tem muito recurso, muito recurso, e quais deles têm pouco recurso e que

01:39

eu devo tirar

01:43

recurso ou aumentar. Então,

01:49

uma pergunta um pouco mais complexa,

01:50

no modo aqui de chamada de função nativo, e vamos enviar.

01:55

Vamos enviar. Então, vocês vão notar que ele vai começar a fazer o pensamento,

01:59

ele vai explorar a lista de tools aqui,

02:01

vai verificá-la. A gente não tem a tool list com text post. Result,

02:07

não tem nada aqui. Então, basicamente, o que ele fez aqui?

02:10

Ele deu um kind pod namespace.

02:13

Pegou aqui todos os nossos namespaces. Nossos namespaces que a gente tem disponível.

02:18

E os pods que estão dentro deles.

02:21

Dentro disso, ele começou a fazer a chamada de cada pod.

02:26

Pegando quais são os recursos dele.

02:28

Então, o deploy dele está aqui. Está vendo? Então,

02:32

ele já começou a fazer várias coisas.

02:34

Então, lá dentro, ele está dando mais coisas aqui.

02:36

Então, ele está olhando o contexto. K8sContextPost.

02:41

Então, aqui ele está pegando o resource. De novo.

02:46

Resource. Está buscando mais resources aqui. Então,

02:48

ele está olhando o resource de cada um dos meus pods.

02:50

Isso aqui vai demorar um pouquinho para fazer.

02:52

Mas vamos deixar ele processar aqui. Assim que terminar de processar,

02:55

eu já volto com vocês aqui.

02:58

Porque senão vai ficar o vídeo aqui da tela processando para vocês. Não tem necessidade.

03:03

Vamos esperar um pouquinho para validar.

03:06

Pessoal, essa pergunta foi muito para o meu contexto aqui.

03:11

Estourou o contexto e o computador não conseguiu responder.

03:16

Então acabou que eu não consegui obter a resposta.

03:19

Porém, estou rodando um modelo local.

03:21

Vocês podem ver aqui que o modelo consome bastante memória da minha máquina.

03:25

Então, assim, em um LLM que está rodando na nuvem ou algo do tipo,

03:31

você talvez conseguiria essa resposta.

03:33

Talvez não, com certeza você conseguiria essa resposta.

03:35

Aqui que a gente chegou no nosso final de contexto,

03:38

fez várias chamadas de tool e não conseguiu resolver, tá bom?

03:42

Então vamos olhar aqui as perguntas mais simples.

03:46

Vamos olhar aqui, tipo, quais podem, podes, quais

03:53

podes, quais, vamos lá, quais,

03:57

os recursos dos meus pods dentro

04:04

do namespace

04:07

namespace de observabilidade

04:13

vou trocar o namespace

04:16

opa, esqueci de ativar a tool, vamos lá, ativar

04:24

a tool, jogar aqui a pergunta de novo e

04:28

colocar a chamada de função nativa aqui pra gente conseguir

04:31

Quais os recursos dos meus pods dentro do namespace observabilidade?

04:34

Aqui vai ser mais fácil para ele conseguir a resposta.

04:37

Se eu vier aqui, está processando meu prompt,

04:41

minha máquina chegou até e ligava em twin aqui,

04:44

de tanto processo que ela estava rodando,

04:47

então ela conseguiu fazer um resource aqui e pegou meus pods.

04:53

Quero saber quais são os recursos.

05:02

configurados para eles.

05:04

Ele vai usar o contexto que já tem e vai conseguir fazer essa consulta para mim.

05:15

Então ele fez a consulta e conseguiu pegar o recurso de cada um dos pods.

05:20

Executou cinco tools em paralelo.

05:22

Informação geral. Aqui ele vai me dar o namespace, vai me dar o IP,

05:25

etc. Aqui a gente tem as portas e assim por diante.

05:29

Ele vai escrever tudo para mim aqui de cada um dos meus serviços.

05:33

Então a gente consegue ter uma tool.

05:36

Para fazer isso. Ah, mas aí vocês podem pensar aí, né?

05:40

Que vocês estão vendo que toda hora eu estou ativando aqui,

05:42

estou ativando o recurso aqui, etc. Que chato, né?

05:45

Toda hora eu tenho que fazer isso para fazer uma pergunta.

05:47

Aí que vem o pulo do gato.

05:49

O que a gente pode fazer aqui com o OpenWebWire? Dentro de espaço de trabalho,

05:53

a gente tem essa possibilidade de criar modelos, tá?

05:57

Os modelos nada mais são aqui do que agents,

06:00

tá bom? A gente pode criar esses agents aqui dentro. Beleza?

06:05

Então, por exemplo, a gente consegue criar um agent,

06:09

vamos criar um agent aqui, que vai se chamar Kubernetes

06:17

Troubleshooter. Deixa eu copiar essa palavra Troubleshooter, porque é uma palavra difícil.

06:25

Kubernetes Troubleshooter.

06:28

Ok? Estamos aqui criando um serviço.

06:32

Eu já tenho um prompt de sistema pronto para ele aqui, tá bom?

06:37

Já tenho todos os próprios sistemas aqui. Então,

06:40

deixa eu puxar esse cara aqui dentro.

06:46

Colocar aqui para vocês. Default.

06:51

Specifying space. Default é esse aqui. Tá bom. Então, temos

06:59

aqui um próprio sistema que vai definir a personalidade do meu agent.

07:03

Então, tem todas as regras aqui. Vai ficar disponível para vocês.

07:07

Esse cara aqui. E a gente tem todas as regras do meu agent, tá?

07:12

Lembra lá que eu estava ativando toda hora o nativo?

07:15

Aqui a gente pode colocar direto a chamada de função.

07:18

O nó do padrão que funciona, a gama mais ampla. Tá aqui, ó, nativo.

07:23

Estamos ativados aqui. E aqui a gente tem a possibilidade de ativar as ferramentas,

07:28

que aqui, Kubernetes, beleza? Então, temos um agent.

07:32

Opa, faltou criar, selecionar o modelo. Vamos selecionar o modelo básico,

07:35

que vai ser o nosso Queen 3.5.

07:38

E vamos salvar.

07:40

Ok? Então, a partir de agora, aqui na nossa listinha,

07:43

a gente vai ter um Kubernetes RoboShutter.

07:46

Que ele já vai vir com aqui a ferramenta ativada.

07:49

E aqui na chamada, aqui ele não vai mostrar,

07:51

mas por trás ele está escrito que ele é... Que ele... Que

07:58

ele está escrito não, né? Está definido que ele vai ser nativo.

08:00

Que ele vai chamar através do native. Então,

08:02

eu vou perguntar, o que você pode fazer?

08:06

Vamos saber dele aqui. O que ele pode fazer?

08:09

Eu sou assistente especializado em todo o que é exatamente o que tem lá, tá vendo?

08:14

Então, investigação de pod, análise de logs. Então, vamos ver.

08:18

Posso fornecer resumo de estado atual do namespace,

08:21

identificação de causa raiz, passos e assim por diante. Então,

08:25

vamos pegar aqui a análise de log, tá?

08:27

Analise os logs dos

08:32

pods do Open Web UI.

08:38

Eu coloco o LightLM na cabeça toda, eu falo LightLM, mas é o OpenMBI.

08:42

Então, vamos lá. Analise os logs dos pods do OpenMBI.

08:46

Então, ele vai lá, pegar o namespace.

08:49

Encontrei, o namespace é o OpenMBI. Beleza, agora ele vai pegar os recursos,

08:54

vai tentar chamar lá dentro para pegar o log.

08:57

Então aqui ele pegou os recursos.

09:01

Excelente, o pod principal do OpenMBI está em execução e pronto.

09:05

Zero, com zero reinicializações. Agora eu quero verificar os outros,

09:08

agora eu vou verificar outros pods para ver a televisão completa.

09:11

Depois eu vou recuperar os logs do container principal.

09:15

Pode recuperar os

09:19

logs do container principal.

09:30

Vamos ver se não estourou o meu contexto também, né?

09:34

Agora ele está fazendo, executando a ferramenta, pegando o pod,

09:37

pod logs post, fez a chamada.

09:40

Opa, tomei um 500 aqui, ó. O

09:44

que eu tomei de erro? 500.

09:46

Do not exist. Então, pegou aqui um contexto, não achou. Logs.

09:55

K3dmba cluster.

09:58

Aqui ele tentou achar.

10:01

Tô tomando um erro 500. Depracted de erro.

10:05

Resource pod not found.

10:09

Não tá achando meu pod. Que coisa, né?

10:15

Direct name.

10:20

Ah, agora ele conseguiu aqui, ó. Então ele conseguiu se resolver.

10:23

O legal do Nate é isso aqui.

10:25

Ele conseguiu fazer várias chamadas e conseguiu se resolver.

10:28

Então ele listou aqui os resources,

10:31

não achou nada. Ele listou aqui o namespace post.

10:36

Conseguiu pegar o Open Web UI aqui do namespace.

10:39

Conseguiu fazer a chamada e ver os pods que estão lá dentro. E com base no pod,

10:45

ele conseguiu fazer a consulta e pegar exatamente os logs que estão lá dentro.

10:50

Toda a parte de log completo.

10:52

Análise de pods. Lista todos os pods. Específico.

10:55

Capacidades principais. Ih, ele me respondeu coisa errada.

10:59

Sou assistente. Ele acabou de me responder coisa errada.

11:02

Provavelmente é o meu LLM local que está dando

11:05

problema aqui por causa do tamanho do contexto.

## Resumo IA

[RESUMO_IA]