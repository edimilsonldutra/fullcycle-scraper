Módulo: Desenvolvimento de Agentes com IA\
Aula: [O artefato App](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18478)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos conhecer o app, que é outro conceito fundamental do ADK,

00:05

que vai trabalhar junto do Session Service e do Runner.

00:09

Foram os dois elementos que nós conhecemos na última aula,

00:12

essenciais para que nós possamos fazer a nossa execução personalizada.

00:17

Este app, ele acaba envolvendo a gente.

00:21

Como nós não o definimos de forma personalizada, quando o Runner foi criado,

00:27

ele internamente acaba criando esse app,

00:29

mas nós podemos criá-lo de forma personalizada. Veja só.

00:34

Nós vamos criar,

00:36

na verdade importar,

00:38

de google.adk.apps a classe app.

00:45

E aqui eu vou definir o app.

00:51

Neste app passamos qual é o root agent que já está importado ali em cima,

00:56

então root agent igual a root agent, e qual é o nome dele.

01:01

Pode ser operador, conta, como nós definimos ali no runner.

01:07

Com ele definido, podemos

01:12

passar apenas app igual a app.

01:21

Vai ter alguma diferença na hora de executar?

01:28

Vai porque eu tenho que tirar esse agent igual a root agent,

01:32

porque agora ele fica somente no app.

01:38

Não vai ter nenhuma diferença.

01:40

Nós vamos ver aqui que ele vai mandar aquela mesma mensagem, por favor informe

01:46

o seu ID de cliente. E a questão é, o que é esse app?

01:50

Por que ele está presente aqui? Qual é a vantagem dele?

01:53

Vamos navegar para a classe e aqui nós já conseguimos ver uma série de propriedades,

01:59

como model config, name nós usamos e root agent, que são as obrigatórias.

02:07

Mas temos plugins, events, compactation config,

02:12

que é para trabalhar com a compactação dos eventos.

02:17

Provavelmente você já viu compactação no seu agente de codificação para

02:22

poder reduzir a janela de contexto.

02:26

Temos configurações de como esses eventos vão sendo compactados à

02:29

medida que a janela de contexto vai acontecendo.

02:33

ContextCacheConfig, que é o cache que vai acontecer lá com o LLM,

02:37

eu poderia colocar quanto tempo que ela vai fazer e outras configurações também.

02:45

ResumabilityConfig, que é a capacidade de retomada.

02:51

Vamos pegar aqui o Cloud Code para dar como exemplo. Eu

02:58

posso mandar uma mensagem qualquer.

03:04

Na verdade, já aconteceu muita coisa aqui,

03:07

tool call e mais uma série de outras questões,

03:09

se eu fechar essa janela e abrir novamente, nós podemos fazer uma retomada.

03:19

Dá para fazer também com Cloud menos R passando ID,

03:22

enfim, tem várias formas. Mas também...

03:26

eu posso retroceder ao momento anterior. Então, se eu mandei uma outra mensagem,

03:30

eu posso voltar lá para o Olá. Então, eu desfiz tudo o que eu fiz antes.

03:34

Então, isso aqui controla como nós vamos fazer essa capacidade de retomada,

03:37

de continuar de onde parou, de retornar para

03:41

onde nós estávamos anteriormente.

03:44

Então, olhando para tudo isso, não tem muitas coisas nesse app.

03:48

Esse base model aqui, na verdade,

03:50

ele é apenas de uma biblioteca chamada Pydantic.

03:56

Que está presente junto nesse ecossistema do ADK,

03:58

que é apenas para poder te ajudar a definir as propriedades e validá-las.

04:03

Enfim, é uma biblioteca bem famosa já na comunidade Python.

04:07

Então, o app define informações de como

04:11

que essa aplicação agêntica vai se comportar.

04:15

Então, veja, ele está definindo questões de cache, de retomada.

04:24

Plugins que controlam como os agentes vão ser executados,

04:27

eu poderia colocar ali um plugin de debug, de monitoramento,

04:34

monitoramento, enfim.

04:37

Imagine que tudo isso aqui poderia ser definido no agente,

04:40

mas ia ficar sobrecarregado, e também o agente tem os seus subagentes,

04:44

eu teria que ficar responsável por ficar replicando,

04:47

ia ficar muito confuso. Então, o app só define como

04:54

esse projeto agêntico tem que executar.

04:57

O que o runner vai fazer é extrair essas informações,

05:01

é uma classe apenas que tem essas informações, ela não faz mais nada.

05:05

Ela vai pegar essas informações, tem até uma validação aqui, na verdade.

05:09

Ela vai pegar essas informações, olha,

05:13

entendi que tem esses plugins, etc., ele vai lá,

05:16

o runner é responsável por criar o contexto da invocação,

05:22

replicar tudo isso,

05:24

enfim. Então, o runner que está sendo aqui o...

05:27

o orquestrador da execução dos agentes.

05:30

Então, isso precisa ficar muito claro na sua cabeça.

05:34

Então, o app é um conceito de como você está montando a sua aplicação agêntica,

05:39

com todas as configurações que você precisa,

05:42

sem se preocupar em replicar nada para ninguém. Você não define essas questões nos seus agentes.

05:51

Então, isso se replica para todo lado.

05:54

Imagine que você tem um plugin de monitoramento. Você só...

05:57

chega aqui em plugins, passa

06:02

seu log

06:05

plugin, ou o que seja, você

06:12

vai colhendo os eventos que vão acontecendo,

06:15

vai registrando em qualquer ferramenta que você tenha,

06:18

enfim, utilizando já os conceitos que nós já sabemos.

06:22

Nós vamos ir mexendo ainda com esse runner,

06:25

vai ficando cada vez mais claro, nós vamos aprofundando cada vez mais,

06:28

mas aqui nós já entendemos como que as coisas funcionam.

06:31

E aqui eu já acho interessante que...

06:33

Vendo isso da forma que é, você já começa a relacionar com

06:40

o que está acontecendo por trás na sua ferramenta.

06:43

Como você acha que está acontecendo aqui no Cloud Code?

06:48

É muito parecido. Você tem a sessão, vai ter capacidade de retomada,

06:52

tem essas definições que são replicadas entre os agentes.

06:57

Quando você está lá no ChatGPT, Cloud AI,

07:01

Open Code, qualquer coisa funciona exatamente da mesma forma.

07:07

Então... Se eu tenho que fazer algumas configurações personalizadas,

07:13

eu defino esse app,

07:14

mas ele não é obrigatório, como nós fizemos na aula anterior.

07:18

Mas a tendência é que você faça a definição dele até

07:21

mesmo para deixar já abertas as configurações que podem ser passadas.

## Resumo IA

[RESUMO_IA]