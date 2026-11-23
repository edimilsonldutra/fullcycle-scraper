Módulo: Desenvolvimento de Agentes com IA\
Aula: [Aprovando Execução de Tools](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18102)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre Tool Confirmation ou aprovação de execução das tools.

00:07

Continuando com o nosso agente operador de conta, eu

00:12

criei mais uma tool de cancelar assinatura e

00:19

ela está listada aqui. Então, agora esse agente tem duas tools.

00:24

Olhando para a tool, estamos seguindo as boas práticas.

00:27

Um nome sugestivo, parâmetros.

00:32

Desnormalizados, na verdade só temos um. O retorno,

00:36

que inclusive a gente não colocou o retorno aqui em cima.

00:42

Sempre ele vai retornar um dicionário, mas é relevante deixar isso claro.

00:46

Temos o docstring falando do parâmetro recebido e também do retorno.

00:52

E aqui um pequeno dicionário com uma assinatura

00:56

apenas para simbolizar a nossa operação.

00:58

Então ele vai lá, pesquisa a assinatura e

01:05

muda ela para cancelada.

01:08

Obviamente, eu nem vou testar isso aqui,

01:10

porque isso aqui está bem óbvio.

01:14

Mas, vão ter situações em

01:18

que, apesar da tool estar disponível,

01:21

não significa que o agente vai sair executando ela de qualquer forma.

01:28

Pode ser que seja perigoso executar essa ação,

01:33

teria que ter uma confirmação do usuário,

01:36

como esse cancelar assinatura pode desencadear uma série de

01:40

problemas que o próprio usuário cancelou por acidente.

01:43

Isso é muito comum.

01:45

Então, nós podemos colocar uma trava nessa

01:49

tool para que o usuário faça uma confirmação.

01:54

E a confirmação não é somente a aprovação de sim ou não. Nós podemos...

02:01

pedir uma informação específica que seja necessária

02:05

depois que ele fez essa confirmação.

02:07

Você confirmou, eu preciso disso aqui para poder efetuar essa operação. Então,

02:13

isso aqui eu acho fantástico correlacionando com o agente de app de codificação,

02:20

que você com certeza está trabalhando com qualquer um,

02:24

Cloud Code ou qualquer um desses.

02:27

Você já percebeu que quando você não está no modo Bypass Permission,

02:32

ou esse Auto Mode aqui do Cloud Code,

02:34

ele pede um Yes para poder fazer uma chamada usando um MCP ou algo assim?

02:41

É justamente esse mesmo conceito. Então nós estamos vendo isso com o ADK,

02:46

mas isso vale de forma geral para qualquer tipo de agente de IA.

02:50

Vamos programar essa confirmação.

02:53

Então, de googleadk.com.

02:57

tools.functionTool. Vamos importar o functionTool.

03:05

Toda tool, na verdade, vai acabar sendo esse tipo de functionTool.

03:09

Inclusive tinha sido invocado o warning,

03:11

ele está sendo manipulado por trás.

03:13

Então nós vamos colocar essa functionTool

03:16

envolvendo o cancelar assinatura exatamente dessa forma.

03:22

Passamos a tool como primeiro parâmetro e o require_confirmation.

03:28

Se eu quero habilitar ou não. Então, já colocando o true,

03:31

ele só vai executar essa tool se o usuário confirmar.

03:36

Primeiro, vamos executar quando é cá run.

03:40

Vamos pedir, quero cancelar minha assinatura.

03:49

Ele vai pedir o ID do cliente. Vamos fornecer.

03:56

Aí ele mostra que carregou esse recurso de tool confirmation.

04:03

Então... o agente é pausado esperando o input do usuário. Veja,

04:08

o agente recebeu a solicitação e foi para executar a tool,

04:14

mas ele não conseguiu. Então, ele teve que parar o processo no meio,

04:18

esperando para que o usuário dê essa confirmação.

04:22

E essa parada é uma parada para que ele continue

04:27

de onde ele parou quando o usuário der uma resposta.

04:32

Então ele mostra aqui esse HITL, isso aqui é um símbolo que é

04:39

um acrônimo para Human In The Loop, que

04:43

é o ser humano no meio do processo.

04:46

Isso aqui não é um processo que vai rodar totalmente autônomo,

04:49

porque precisa de interferência de um ser humano, ele precisa aprovar.

04:54

Então guarde isso aqui.

04:56

Então ele está mostrando uma mensagem em relação a essa tool.

05:03

Por favor, aprove ou rejeite, atue, cancele e tal.

05:07

Então, vamos responder aqui com o Yes.

05:13

Com certeza, a assinatura foi cancelada com sucesso. Sinto muito por não

05:18

ter você conosco. Isso aqui ele acabou,

05:21

por causa do ser cordial aqui, né? Ser cordial e direto,

05:26

ele acabou colocando isso. Vamos para o ADK Web, então,

05:28

que eu só vou rodar o operador conta.

05:32

Então, agora, ao...

05:35

fazer o lockout na porta 8000, ele só vai mostrar o operador conta.

05:41

Então vamos, quero cancelar minha assinatura, ele

05:48

vai pedir client

05:50

ID, então veja que agora eu tenho duas tools que elas já são,

05:55

nós já vimos que isso já foi enviado para a LLM, ele conhece essas duas tools.

06:00

Ao enviar isso aqui, a

06:04

LLM vai dar a recomendação de executar.

06:08

cancelar a assinatura. Porém, quando a gente vai executar, tem a trava.

06:17

Vamos pegar esse evento aqui e

06:24

fazer o stack trace dele.

06:30

Então nós tentamos invocar,

06:34

obviamente não vai ser possível, dado o

06:42

evento que nós temos, que

06:48

é esse ADK Request Confirmation, não tem outras informações. Nós

06:56

vamos ter apenas...

06:58

uma parte na mensagem que vai registrar essa confirmação da tool.

07:04

Então, foi retornado para

07:08

o front-end para ele mostrar essa mensagenzinha aqui, tem como personalizar isso.

07:15

Então, aqui eu dou a aprovação, pronto.

07:17

Nós vamos ver que ele invocou a tool nesse processo.

07:25

Então, é como se a gente tivesse aqui uma função intermediária, um middle, um

07:31

firewall, bloqueando.

07:35

E aí ele pausa e permite que nós continuemos.

07:38

Este comportamento que nós vimos é o comportamento mais básico

07:42

para ter segurança na execução de uma tool.

07:47

Agora vamos avançar um pouco mais.

07:50

Com esse require confirmation,

07:52

nós conseguimos passar também uma função. Veja que ele

08:00

pode receber apenas um booleano ou uma função que a torna um booleano,

08:05

se vai aprovar ou não.

08:07

Então nós poderíamos criar uma função, vamos dar um exemplo aqui, uma função de

08:16

verificar valor assinatura.

08:22

Então além do client ID,

08:27

poderíamos receber o valor que é o float.

08:32

Então, caso nós

08:36

verifiquemos se o

08:42

valor for menor que 100, então

08:52

ele vai retornar falso. Então poderíamos colocar esse verificar assinatura aqui.

08:59

Ele vai retornar um

09:02

boolean. Agora, por que ele está chiando aqui?

09:07

Às vezes ele demora um pouquinho para sumir.

09:13

Na verdade, o problema é

09:18

exatamente porque a função tem que ser definida antes,

09:22

não pode ser depois aqui do agente, porque senão ela precisa existir antes.

09:27

Para esse caso, eu precisaria também...

09:30

usar esse valor, tudo que eu tenho como parâmetro numa tool,

09:34

aqui nessa função também eu recebo.

09:38

Então, dessa forma, eu conseguiria já

09:42

ter uma aprovação direta se o valor é

09:46

menor que 100 e pedir uma aprovação do usuário se o valor for maior que 100.

09:52

Eu posso criar, a ideia aqui é criar qualquer lógica.

09:54

Obviamente, isso não faz sentido com a tool,

09:57

porque nós só vamos saber o valor da assinatura

10:01

uma vez que a gente consiga consultá-la.

10:04

Mas se você já tem o dado de alguma forma, você já consegue ter

10:12

um condicional para falar se fica dinâmico,

10:16

porque ele pode pedir a confirmação ou não.

10:20

Mas a gente vai deixar isso aqui comentado e

10:24

o comportamento disso aqui

10:28

duplicado eu vou manter como true.

10:36

Mas mesmo assim, colocando um condicional,

10:40

ele vai continuar mostrando essa mensagem padrão,

10:45

que muitas vezes não vai ser legal.

10:49

Nós precisamos formatar.

10:51

Tudo bem que às vezes eu posso ter um front-end que ele pega,

10:54

entende o que o agente está enviando e faz a formatação,

10:58

mas seria interessante que o agente já organizasse isso para a gente.

11:03

Então, você pode fazer o comportamento desse tool confirmation.

11:08

De forma totalmente manual.

11:12

Então, muda totalmente a forma de trabalhar,

11:15

porque você vai precisar fazer a sua interseção aqui na tool.

11:23

Então, vamos deixar isso aqui comentado.

11:28

Vou colocar o cancelar assinatura.

11:32

E aí nós vamos receber mais um parâmetro aqui

11:37

que vai ser o tool context, que é o contexto da tool. Ele vai ser do tipo Tool

11:44

Context. Nós vamos importar aqui em cima from google

11:50

.adk

11:52

.tools .toolContext toolContext.

12:00

Através dessa

12:03

variável, que ela é sempre passada, a gente usa o que quiser.

12:08

Nós conseguimos acessar várias informações do agente, muitas

12:14

coisas podem ser relevantes para a nossa execução. Mas nós temos aqui a tool

12:24

Imagine que essa tool está sendo executada pela primeira vez.

12:28

Esse tool confirmation pode existir ou não. No caso da primeira vez,

12:33

não vai existir. Então, ele vai ser None.

12:36

Então, se tool

12:40

context.ponto.toolConfirmation is None, que é assim que faz,

12:45

não tem igual a igual, a gente não faz dessa forma, com o None.

12:53

Então, eu sei que eu tenho que pedir a confirmação.

12:56

Então nós vamos chamar toolContext.requestConfirmation,

13:01

passando o hint que vai ser a mensagem que vai aparecer

13:08

lá para o usuário. Eu vou até deixar essa mensagem que a IA já me ajudou,

13:13

bom, que eu não tenho que digitar.

13:18

E aqui eu retorno o resultado.

13:21

Lembra do que nós havíamos falado sobre ter um dicionário também sugestivo?

13:26

Nós já vimos se...

13:28

não retornar um dicionário, ele vai acabar colocando um result.

13:33

Eu costumo fazer assim nas minhas aplicações.

13:37

Eu coloco um status com...

13:41

Aqui eu estou colocando no português para poder ficar mais fácil.

13:45

Então, colocaria um aguardando, um waiting,

13:48

confirmation, enfim, aguardando confirmação.

13:52

Assim, em uma forma mais simples possível.

13:59

Então aqui ele já vai retornar, ele vai quebrar o comportamento.

14:02

Mas como eu já fiz o encaixe disso aqui,

14:05

ele pausa e retorna. Então nós estamos tendo controle totalmente manual.

14:11

Mas acontece que quando o usuário fizer a aprovação,

14:16

então eu

14:20

vou olhar se o toContext.toConfirmation

14:26

.confirmed, esse

14:30

aqui que vai ser o yes ou o no,

14:33

Ou seja, se eu

14:37

não aprovei, então coloco não

14:40

cancelado ou qualquer outra coisa no status.

14:45

Ele poderia colocar uma mensagem

14:48

associada a isso.

14:53

Então cancelamento do usuário, ou melhor, cancelamento não confirmado.

14:58

Enfim. Então veja esse bloco.

15:00

É um bloco simples, mas agora nós temos controle.

15:04

E não é só a questão de definir.

15:08

um comportamento para personalizar a mensagem.

15:12

Mas imaginando que você tem uma tool mais complexa,

15:17

dependendo do que acontece ali dentro,

15:20

você pode escolher o momento de ativar essa confirmação ou não, dependendo de uma situação.

15:26

Algo que o Function Tool não permite, nem com o Require Confirmation.

15:30

Ele sempre é uma trava antes da execução da tool.

15:34

Então aqui nós temos... Total controle. Onde for necessário,

15:38

eu consigo encaixar essa lógica.

15:41

Vamos testar no ADK Web. Então, quero cancelar minha assinatura. Cliente 123.

15:52

Então, eu invoco o API e aqui está a nossa mensagem personalizada.

15:56

Então, eu vou marcar, confirmar e submeter.

16:00

Pronto. A assinatura foi cancelada com sucesso.

16:06

Nós podemos ver aqui em Tracing. Veja só o que eu vou fazer. Vou colocar o mouse.

16:10

clicando aqui no Invocation ID, exatamente quando ele vai executar a

16:17

tool, pedir a confirmação e depois nós vamos dar a confirmação e

16:22

ele vai executar novamente fazendo o cancelamento.

16:27

Aqui na parte de Spans, que é cada etapa que vai acontecendo,

16:31

nós podemos voltar um pouquinho.

16:36

Então aqui eu vejo o Execute Tool do Cancelar Assinatura, em

16:42

que a resposta vai ser o Aguardando Confirmação. Então aqui é exatamente quando ele

16:51

não conseguiu continuar o processo.

16:55

Então ele chama o call LLM e aqui

17:00

embaixo nós vamos ver que isso também virou contexto.

17:04

Então nas partes da mensagem vai acabar sendo

17:08

acrescentado lá que está aguardando confirmação.

17:15

Aí foi gerado o conteúdo pelo LLM,

17:18

aí agora vem o invocation ID, aí ele vai invocar...

17:24

o cancelamento, que agora sim está cancelado.

17:29

Isso aqui parece estranho porque o ADK Request Confirmation está aqui embaixo,

17:33

mas colocando em eventos,

17:36

obviamente ele está antes da chamada novamente que é feita na tool.

17:43

Aqui eu consigo clicar nesse botão limpando

17:47

e aí nós temos os dados aqui envolvidos.

17:53

Isso aqui foi a... Mensagem enviada pelo usuário.

17:58

Obviamente uma mensagem mais estruturada

18:01

para simbolizar essa confirmação que aconteceu,

18:05

porque ele envia ali um

18:08

confirmar igual a true.

18:13

E nós podemos fazer ainda outros comportamentos.

18:16

Vamos supor que fosse necessário uma senha para

18:25

poder fazer essa confirmação. Então a gente poderia colocar assim, se...

18:30

senha, é diferente de senha secreta,

18:34

então aqui quando eu peço autorização dele, eu posso também pedir mais informações.

18:41

Então no payload, eu

18:44

posso acrescentar que além do client ID,

18:49

que obviamente eu preciso dessa informação, eu

18:53

preciso da senha, que eu não sei. Essa

19:00

senha vai ser passada pelo usuário.

19:07

Então agora vamos rodar novamente.

19:19

Então, quero

19:21

cancelar minha assinatura.

19:27

Vai pedir o ID. Aí,

19:34

tá vendo? Para confirmar o cancelamento, por favor, poderia me fornecer sua senha?

19:39

Então, senha, como é que foi definido?

19:42

Senha secreta.

19:45

Foi quando a escola contraiu.

19:48

Então, senha

19:49

secreta. Então,

19:57

o cancelamento foi...

20:01

Iniciado, então eu tenho aqui como se fosse duas confirmações,

20:04

nós podemos fornecer quaisquer informações relevantes.

20:11

Pronto, a assinatura foi cancelada.

20:17

Então aqui no payload eu posso exigir qualquer informação

20:20

e aqui eu passo um valor default.

20:25

Então isso aqui é muito poderoso,

20:27

porque eu posso encaixar em qualquer lugar, pedir informações,

20:31

validar essas informações de qualquer forma,

20:34

e nesse caso aqui seria importante colocar também

20:37

a docstring relativa a isso

## Resumo IA

[RESUMO_IA]