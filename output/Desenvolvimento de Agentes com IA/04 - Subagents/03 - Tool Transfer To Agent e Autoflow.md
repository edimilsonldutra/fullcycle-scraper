Módulo: Desenvolvimento de Agentes com IA\
Aula: [Tool Transfer To Agent e Autoflow](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18258)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos trabalhar com a tool TransferToAgent,

00:04

que é uma tool embutida no ADK que permite que

00:07

um agente transfira o controle para o outro.

00:11

Nós vamos trabalhar no mesmo exemplo da aula anterior e

00:15

apesar de ser um exemplo que parece muito simples,

00:18

tem muita coisa acontecendo aqui por trás e é bom manter este exemplo

00:23

simples porque nós precisamos entender tintim por

00:27

tintim do que está acontecendo aqui.

00:29

O não entendimento disso faz com que

00:32

você organize os seus agentes de forma incorreta.

00:37

Nós vamos ver isso aqui durante a aula.

00:39

Então, nós vamos rodar o ADK Web apontado para esse agente,

00:44

porque nós vamos conseguir ter o trace de tudo que aconteceu.

00:47

Então, vamos listar as faturas, colocar

00:53

minhas faturas, como nós já tínhamos feito anteriormente.

00:58

Então nós vimos aqui que o operador da conta que respondeu,

01:03

veja ali a mensagem, o controle ainda está nele.

01:10

Exatamente porque também vai ter aqui nas instruções

01:15

que o usuário precisa fornecer o ID do cliente.

01:17

Isso aqui poderia estar nos nossos subagentes, mas nós colocamos no operador.

01:23

Então ele não mudou o controle ainda.

01:26

Vamos agora... Colocar o cliente em 1, 2, 3 e veja o que vai acontecer. Aqui

01:33

nós temos o transfer to agent.

01:37

Isso aqui é executado no

01:40

nosso projeto, código Python.

01:43

E se passa, qual é o agente que vai receber essa transferência, a passada de bola?

01:49

Que é o consultor faturas,

01:50

exatamente o nome que está declarado no subagente.

01:57

Consultor faturas.

02:00

Então, a partir disso, temos

02:05

a execução para valer,

02:07

o consultor faturas assume a passada de bola e até mesmo

02:12

a corzinha muda aqui para simbolizar que é um outro agente.

02:16

Aqui nós temos o azul escuro do operador da conta e

02:19

o consultor faturas agora é um azul mais claro.

02:22

Então, veja que esse final, que é a resposta das faturas, é

02:30

o consultor faturas nos respondendo.

02:33

e não o operador da conta. Com o ADK run,

02:39

se você voltar na aula,

02:40

você vai ver que essa mudança fica aparecendo aqui no cantinho.

02:46

Mas é porque nós vamos tender a desprezar isso,

02:49

não entender exatamente esse controle que aconteceu.

02:53

Se eu mandar qualquer coisa aqui agora, o

02:58

controle continua com o consultor faturas.

03:03

Mas esse controle pode voltar para o operador da conta? Pode.

03:08

Como ele pode ir para o consultor assinaturas?

03:15

Uma vez que o seu agente tem o controle, ele volta para o coordenador,

03:20

quem começou tudo, ou ele pode ir para os irmãos dele,

03:24

ou até mesmo para os subagentes. Um subagente pode ter outros subagentes.

03:29

Aí, obviamente, a coisa vai ficando mais complexa.

03:35

Vamos entender como que isso está funcionando na prática. Agora,

03:38

sua cabeça vai explodir em relação a como as coisas acontecem. Na verdade,

03:43

é aquela história de contar que o Papai Noel não existe. Ela vai explodir,

03:49

mas você vai ver que não há mágica por trás de como essas coisas funcionam.

03:54

Então, voltando aqui para o listar faturas, não temos request nem response.

03:59

Agora, nesse aqui, como temos a...

04:01

A response nós vamos conseguir ver a request que foi enviada para que nós

04:09

capturemos essa response. Ele acrescenta o system prompt do

04:16

operador da conta, você é atendente de conta, o usuário precisa fornecer o ID,

04:21

aquela mensagem que é adicionada que você é um agente,

04:26

seu nome interno é operador de conta,

04:28

e agora vem o system prompt para que... possamos trabalhar com outros agentes.

04:36

Você tem essa lista de outros agentes para transferir.

04:41

Então, todos os subagentes que estão lá naqueles subagents, aquele parâmetro,

04:45

vão ser listados aqui. Então, tem o consultor de faturas,

04:48

o agent name, e tem a descrição dele. Não colocamos nenhuma descrição,

04:52

que é um parâmetro que pode ser adicionado lá.

04:55

Consultor de assinaturas, a mesma coisa. O nome dele e a descrição.

04:59

Então, é colocado que se você...

05:03

É o melhor para responder à questão? Responda. Exatamente esse trecho.

05:08

Agora, se outro agente é melhor para responder, chame

05:15

o transfer to agent. Como é uma ferramenta,

05:18

nós aprendemos que isso é executado no nosso código. Na verdade,

05:21

a LLM só vai responder que é para chamar.

05:25

Quem chama vai ser o agente. No caso, o agente de operador de conta.

05:32

Então, é passado nessa chamada.

05:37

em function declarations, o

05:41

transfer to agent, assim como o listar faturas que nós vimos nas últimas aulas. É uma ferramenta.

05:47

Então, aqui está a docstring da ferramenta, é uma ferramenta que está lá presente no ADK.

05:54

Transfere a questão para outro agente. Essa ferramenta vai fazer o handoff,

05:58

ou seja, vai fazer a transferência do controle para outro agente e etc.

06:04

E ele até já delimita quais são os parâmetros que podem ser passados.

06:08

No agent name, você pode passar o consultor de faturas ou o consultor de assinaturas,

06:13

que são os agentes disponíveis. E a nossa mensagem. Então,

06:17

quando vem aqui o cliente 123, agora quando nós

06:23

já digitamos o ID, porque

06:27

antes... Vamos voltar para cá.

06:29

A response foi exatamente o que é retornado aqui nessa mensagem, pedindo...

06:37

O ID do cliente. Então, digitamos. Agora, aqui,

06:40

a LLM já está pedindo para fazer a transferência.

06:43

Então, na request, nós vamos ter o mesmo system prompt,

06:47

não mudou nadinha. Não mudou nadinha.

06:50

É a mesma coisa. O

06:53

que vai mudar vai ser em contents, que vai agregar a minha primeira mensagem, o

07:02

pedido do ID do cliente e o

07:06

ID do cliente que eu digitei.

07:08

Então, na resposta...

07:11

Como ele tem acesso a tudo isso e também tem esse transfer to agent,

07:16

ele viu que é necessário transferir, veja,

07:20

ele está fazendo a function call que nós já tínhamos visto.

07:23

Transfer to agent consultor faturas.

07:28

Então, o que vai acontecer é que o operador conta nessa linha seguinte,

07:32

vai executar essa tool transferindo o controle para esse subagente.

07:41

Então, veja que interessante.

07:44

Nessa primeira chamada aqui, nós

07:48

vemos que só há o system prompt do operador da conta.

07:54

Não foi passado nenhum outro detalhe dos subagentes. Eles têm o seu system prompt,

08:00

têm as suas tools e nada disso foi passado.

08:05

Porque essa primeira chamada que acontece,

08:08

ela permite que a LLM fale se é para

08:12

continuar com o operador da conta ou se é para transferir.

08:17

para o outro subagente. Vamos fazer uma mudança para mudar esse controle?

08:20

Se eu pegar essa mensagem que você precisa fornecer o ID do cliente e

08:26

colocá-la aqui no subagente,

08:30

nós já veremos um comportamento totalmente diferente. Na verdade,

08:35

eu tenho que rodar de novo o

08:38

ADK, porque eu fiz a mudança no código.

08:42

Então, agora, vamos

08:45

colocar listar minhas faturas.

08:55

Veja só. A transferência já aconteceu logo de cara.

08:59

Aí a passada de bola já foi para o

09:03

consultor de faturas e é ele que está pedindo para listar,

09:07

ou melhor, o ID do cliente.

09:09

Eu passo aqui o ID do cliente e ele vai acabar respondendo com

09:15

as faturas. Aqui nós vemos o que aconteceu.

09:20

Em um momento anterior,

09:22

nós vemos aqui todo

09:26

o fluxo que aconteceu.

09:29

Então, operador de conta passou para o subagente, e

09:33

aí invocou a atu, atu retornou a resposta, enfim, aí nós temos aqui a nossa resposta.

09:42

Isso é interessante observar no ponto de,

09:46

se é o subagente que vai dar essa resposta,

09:50

nós cometemos uma gafe aqui, não é um erro,

09:56

mas muda. O objetivo do qual nós definimos o comportamento do agente.

10:02

Porque nós falamos do operador da conta para ser cordial e direto.

10:08

Mas então, se é o subagente que pega o controle e responde para o usuário,

10:13

o consultor de faturas não é cordial e direto.

10:18

E é justamente aqui que nós erramos em entender o fluxo.

10:23

O entendimento desse vai e vem é o que vai

10:26

definir o sucesso na montagem do seu subagente.

10:30

que tipo de ida e volta que nós vamos ver, outras variações, quais as limitações,

10:35

como ela vai se comportar. Então, nós deveríamos colocar,

10:39

se eu vou delegar o controle para o subagente,

10:45

que tem outras formas de trabalhar, esse aqui tem que ser cordial e direto,

10:49

esse aqui também tem que ser cordial e direto,

10:52

porque senão eles vão estar desalinhados com o que nós desejamos.

10:57

Então, agora nós podemos até fazer um teste.

11:01

que não vai mudar nada, apenas a mensagem,

11:05

listar minhas faturas, vai

11:10

transferir o controle, vamos digitar o cliente 123.

11:14

Ele

11:18

Mudou um pouquinho mais a mensagem, mas enfim,

11:20

aqui não temos muita coisa para acontecer,

11:23

mas são esses detalhes que pegam na hora que nós estamos montando o nosso subagente.

11:28

Eu coloquei aqui um diagrama de sequência,

11:30

que simboliza justamente esse comportamento. Então,

11:33

quando nós editamos, listamos minhas faturas, o

11:37

operador da conta manda o seu system prompt, mais a mensagem do usuário,

11:42

mais as tools, mais os nomes e descriptions dos subagentes.

11:46

Eu vou até acrescentar esse detalhe, que não é só as descriptions,

11:49

é os nomes mais as descriptions.

11:54

Então, com tudo isso, o Gemini ou qualquer outro modelo...

11:58

vai definir se é para transferir para outro ou

12:02

se é para continuar no próprio subagente.

12:07

Então, se aqui aconteceu a transferência, o

12:12

agente de operador de conta vai transferir o controle para o consultor de faturas.

12:18

E agora o consultor de faturas vai

12:21

pedir, na

12:24

verdade, ele vai passar ali o system prompt

12:28

dele, mas o histórico, o legal... dessa transferência,

12:33

que ela não é uma transferência a cegas.

12:34

Ele pega todo o histórico do que aconteceu.

12:40

Nós podemos frisar isso aqui novamente, marcando essa mensagem aqui na

12:47

request. O system prompt mudou,

12:52

que agora nós estamos nesse novo subagente, mas aqui na parte de contents,

12:58

listando minha fatura. Aí tem o transfer que aconteceu,

13:02

então isso aqui é adicionado, o subagente tem acesso a essa informação,

13:06

ele sabe que aconteceu essa transferência de controle.

13:10

Aí depois tem o pedido do ID do cliente, a

13:15

informação que o cliente digitou do ID, a

13:22

invocação do listar faturas e

13:25

os dados.

13:27

Esse aqui é o final, obviamente isso aqui foi passado tudo lá para a LLM,

13:32

ela decidiu formatar dessa forma. Aqui nós temos a resposta.

13:39

Então, depois disso, que

13:42

o subagente recebe a resposta,

13:46

ele vai receber o informe, o ID do cliente, nessa mudança que nós fizemos.

13:52

Nós pegamos a mensagem e colocamos ela diretamente no subagente,

13:58

não no operador da conta, para poder fazer esse teste. Então,

14:01

quando o subagente recebe para informar, ele vai lá para o usuário.

14:08

E manda mensagem para ele poder informar o ID, enfim, aí depois acontece a listagem.

14:15

Entender esse comportamento faz com que a gente perceba que, na verdade,

14:18

agora fica bem mais claro que um agente

14:21

ou agentes de IA

14:24

vão ser um código mais

14:30

um system prompt que

14:33

usa LLM, que

14:38

é status, ou seja, ela não guarda estado.

14:42

Ela vai ter ali o cache apenas do system prompt para poder otimizar.

14:49

E, na verdade, aqui nós podemos colocar mais as ferramentas.

14:56

Então, eles

14:59

vão se comunicando com a LLM e ela vai mudando o controle para outros,

15:04

vai pedindo para executar tools,

15:06

vai fazendo as informações e a jogada acontece dessa forma.

15:14

Então, consegue perceber que eu não quero, obviamente, desmerecer,

15:18

mas é só para exercitar o raciocínio,

15:20

que você poderia criar o seu agente de IA?

15:23

Não tem um segredo.

15:25

Você só precisa estruturar para que eles se comuniquem

15:29

de uma forma correta com o LLM e

15:31

o LLM devolva a resposta conforme nós conseguimos capturar

15:36

e ir mudando o comportamento no meio do código,

15:39

mandando para o usuário, pega as coisas e vão acontecendo.

15:44

Muitas camadas, o ADK é algo muito complexo,

15:47

para que a gente consiga construir algo assim vai demorar um determinado tempo,

15:52

você vai precisar entender um pouco como que LLMs funcionam,

15:58

mas é

16:00

fantástico entender que no final das contas a mudança de agentes

16:04

é tudo o cérebro pedindo para os seus subordinados poderem executar.

16:10

Então aqui nós já tivemos esse primeiro contato

16:12

que esclarece como essas mudanças vão acontecendo.

16:15

Nós já dissemos que as mudanças podem acontecer de

16:20

passar a bola de novo para o coordenador, um subagente passar para o seu irmãozinho,

16:26

o outro passar para o seu irmãozinho e volta para o coordenador,

16:28

dependendo do que você fizer,

16:29

faça a jogada de ficar pingando em cada um dos agentes,

16:34

mas o agente condensa tudo isso.

16:36

É o código System Prompt Tools que vai executar alguma coisa e depois...

16:40

dá a resposta, ou senão a LLM vai falar para ele transferir para outro,

16:45

e assim vai. E a esse comportamento do ADK,

16:48

nós podemos dar um nome muito importante que você conhece,

16:51

que é o AutoFlow, ou fluxo automático.

16:56

Ao contrário de outros frameworks para construção de agentes,

17:00

que você precisa ter um contrato, o fluxo definido,

17:05

você faz essa definição, e aí as coisas já vão trabalhar exatamente daquela forma.

17:12

Aqui nós temos mais flexibilidade, porque

17:15

uma vez que você viu ali que ele usa descrição do agente logo no começo,

17:20

mais o nome, e obviamente tem o system prompt do coordenador, ele

17:28

já toma a decisão de mudança, mas toda vez também que o subagente é executado,

17:33

vai ter o system prompt dele e a descrição dos outros agentes, então ele vai

17:39

pulando de galho em galho. Então ele tem esse fluxo flexível, obviamente...

17:44

que tem a desvantagem que se você não fazer boas descrições,

17:50

tiver um system prompt confuso, na verdade,

17:54

system prompts confusos através do seu coordenador e os seus agentes,

17:59

esse fluxo pode se comportar de uma maneira esperada ou de uma maneira errada.

18:04

Mas esse comportamento é interessante justamente porque ele manda lá e

18:08

a LLM vai decidindo para onde vai e as coisas vão acontecendo.

## Resumo IA

[RESUMO_IA]