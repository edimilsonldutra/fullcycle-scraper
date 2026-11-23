Módulo: Desenvolvimento de Agentes com IA\
Aula: [Agente Mode Single Turn](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18262)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos ver o agent mode chamado de single churn.

00:06

Ele permite que o agente não tenha controle da conversa.

00:13

Como nós temos o consultor de faturas,

00:16

se eu ativar esse mode aqui, quem continua tendo controle é o operador da conta.

00:22

Vamos fazer uma experimentação. É bom a gente brincar e ver os resultados.

00:27

Esse é o momento para que nós possamos experimentar.

00:32

Eu vou colocar o mode single churn nesse agente.

00:39

E aqui nós não precisamos daquele bloqueio de transferência,

00:44

até mesmo que agora ele sendo um single churn,

00:46

mas eu vou deixar comentado de qualquer forma.

00:49

Vamos fazer um novo teste?

00:54

E a questão é que nós não vamos ter mais aquele transfer para esse subagente.

01:01

Vai ser bem diferente.

01:03

Então eu quero listar minhas faturas.

01:13

Veja só, para

01:16

listar, eu preciso do ID do cliente.

01:23

Veja que a

01:25

forma de invocar, ele conseguiu chegar no agente,

01:29

mas não ocorreu o transfer to agent, ou seja,

01:33

esse agente de consultor de faturas não pegou a bola para ele,

01:38

a bola continua com o operador da conta, porque

01:43

quando foi

01:45

enviado... não ocorreu a transferência,

01:48

e mesmo que ele tenha conseguido mandar essa mensagem aqui,

01:55

ela volta como resultado, está vendo? Esse result que está

02:03

aqui é aquele que a gente tinha falado lá nas tools,

02:09

quando você não delimita que é um dicionário que está sendo retornado,

02:13

ele vai acabar encapsulando isso no result. Então,

02:16

na verdade, isso aqui acabou sendo retornado

02:20

para o agente coordenador e ele repetiu a mensagem.

02:26

Mas está aparecendo duplicado, então nós estamos num loop,

02:31

exatamente porque quando o subagente é um single churn,

02:37

vamos verificar o que está acontecendo aqui.

02:42

Na lista de

02:45

agentes que nós podemos transferir,

02:47

está constando apenas o consultor de assinaturas.

02:53

Então, aquele mesmo prompt que nós já tínhamos visto.

02:57

Aí temos o transfer to agent,

02:59

porque está relacionado com a possibilidade do consultor de assinaturas,

03:03

mas o nosso agente, consultor de faturas,

03:08

agora se torna uma tool em

03:12

que passamos uma request do tipo string,

03:17

ou seja, podemos passar uma frase, um conteúdo, vai ser processado e retornado.

03:24

para o agente coordenador.

03:27

Então, veja que interessante.

03:29

Colocando aqui mais uma vez, no próximo,

03:33

veja que foi ativado o System Prompt do agente, tem

03:40

a tool de listar faturas, ele está recebendo todo o contexto, só

03:49

que com uma abordagem diferente.

03:51

Então, a ideia aqui é que eu execute e retorne um valor para o coordenador.

03:58

Mas o single churn tem a ideia de ser esse turno único.

04:03

Eu retorno já um resultado sem interferência do usuário.

04:09

Então, se eu precisar

04:12

perguntar qualquer informação para ele,

04:16

não é o modo ideal. Se eu tiver tool confirmation, também não vai caber,

04:23

porque eu perco esse controle, justamente porque eu não tenho...

04:28

uma transferência, e na estrutura do ADK, quando,

04:32

por exemplo, nós temos essa confirmação,

04:34

nós vamos ter um registro no meio da sessão que

04:39

garante que eu pare ali, eu posso continuar de onde eu parei,

04:44

colocando aquela mensagem do yes.

04:48

Então aqui é como se nós estivéssemos invocando uma função retornoValor e pronto,

04:53

apesar dela receber todo o contexto, que nós vimos aqui que ela está recebendo o...

05:00

Listar faturas, né?

05:03

Se tivesse outras coisas, ela receberia todo o histórico.

05:07

Então, é importante cometer esses erros, porque

05:12

uma definição errada pode fazer o usuário ficar preso.

05:16

Ele manda mensagens para a gente e nunca acontece nada, não sai do lugar.

05:20

Isso é muito comum. Não somente aqui com a escolha de um modo errado,

05:24

mas também, às vezes, se você não trava a transferência,

05:29

voltando à questão lá...

05:32

de bloquear a transferência para os irmãos ou para o pai.

05:36

Pode acontecer, dependendo do modelo que você tem,

05:39

que o usuário fica preso em um looping e não vai para lado nenhum.

05:42

Então, esses controles servem para colocar a

05:46

rédea no cavalo, fazendo uma analogia.

05:50

Então, está clara essa questão do Seagull Churn,

05:52

que é transformar o agente em uma tool.

05:56

Executa, retorna o resultado.

05:58

Eu nem vou mostrar o agente apenas com isso.

06:01

Nós já entendemos o contexto,

06:04

já sabemos criar subagente. É totalmente desnecessário.

06:09

Mas nós vamos encaixar esse single churn adicionando um pouco mais de

06:13

complexidade porque nós vamos alinhar a fome com a vontade de comer.

06:17

Nós adicionamos esse contexto e circulamos com muito mais conhecimento.

06:23

Agora nós vamos ter um controle mais específico.

06:29

Não deixando apenas que o out of flow determine as coisas.

06:33

Então vamos supor que na hora de listar as faturas possa acontecer, é muito comum,

06:37

acontece um erro com o banco de dados ou a sua

06:40

tool faz um HTTP e pode acontecer um erro.

06:43

É recomendado que você evite fazer um, no caso aqui do Python,

06:49

fazer um raise da exceção, um lançarelo.

06:55

Faça um try, except, capture o erro e no except,

07:01

transforme ele num

07:04

dicionário que determina um pouco do erro e faça também

07:07

um log que é importante para que você tenha rastreabilidade disso. Então,

07:12

dessa forma aqui, nós podemos ter esse tipo de erro. Agora,

07:16

pensando que o subagente de consultor de faturas vai ter esse erro,

07:25

não deveria ser ele o responsável por retornar isso para o usuário.

07:35

Nós poderíamos delegar... isso para o agente coordenador.

07:39

Então, eu adicionei aqui uma regra.

07:42

Quando um subagente, quando algum subagente retornar um erro do sistema,

07:46

Use o subagente AcmeStatus.

07:50

Então, agora temos um subagente para verificar o status do sistema.

07:54

Nós poderíamos ter um endereço que a gente... Normalmente,

07:57

Esses status apontam alguma coisa para verificar se está funcionando ou não.

08:03

Então, tem a descrição dele.

08:07

E o System Prompt que não tem muita coisa, é apenas um agente de status.

08:11

E aí nós vamos ter uma tool que

08:15

vai fazer um comportamento aleatório, poderia ser até determinado.

08:20

Mas ele vai retornar um status,

08:22

Está operacional, manutenção intermitente, uma mensagem específica.

08:30

Portanto, se algum subagente ou de assinaturas

08:34

ou de faturas retornar um erro desse sistema,

08:41

nós vamos verificar se está operacional ou não.

08:45

Então, se está intermitente, vai informar o usuário que está indisponível,

08:50

que ele tente mais tarde. Caso os serviços estejam operacionais,

08:55

informe o usuário de um erro do sistema e que ele deve tentar mais tarde.

08:58

O que são erros do sistema? Seria importante usar as nossas capacidades

09:04

de criar prompts, tudo que nós já aprendemos no MBA, para...

09:10

Que ele pode confundir. Então, erros de sistema são bugs,

09:14

erros de comunicação com sistemas externos, bancos de dados,

09:17

IP de terceiros e tudo mais.

09:18

Mas não informe esses detalhes ao usuário.

09:22

Posso informar um erro de SQL e coloco o SQL lá para o usuário.

09:27

Enfim, o risco não é só com a gente.

09:29

A gente já fazia antes de existir inteligência artificial.

09:33

Então, isso aqui vai ser interessante, porque se acontecer um erro...

09:37

O operador de conta agora é responsável por retornar o resultado.

09:43

Então, vamos rodar novamente o nosso exemplo.

09:49

E agora eu vou pedir para listar minhas faturas.

09:55

Vou transferir para o consultor de faturas.

10:01

Cliente 1, 2, 3.

10:05

Acionou o ato e retornou um erro de conexão com o banco de dados.

10:09

Não era para ter acontecido isso, mas porque...

10:14

O transfer to agent mandou o controle para o consultor de faturas.

10:19

Então, não voltou para o operador da conta. Então, vê o que é necessário fazer aqui.

10:25

Nós precisamos chegar no

10:31

consultor de faturas.

10:33

E agora ele não vai responder direto, mas nós vamos mudar.

10:38

Quando terminar, nós vamos adicionar aqui uma instrução.

10:42

Quando terminar,

10:45

Faça um...

10:49

Transfer to agent para o operador da conta.

10:52

Posso continuar a conversa com o usuário.

10:55

Eu precisaria colocar exatamente dessa forma, não preciso colocar transfer,

11:00

poderia colocar delega a conversa para o operador da conta.

11:04

Existem várias formas de colocar isso.

11:06

Ele vai interpretar e vai conseguir entender o que nós estamos dizendo.

11:10

Mas cuidado aqui com os bloqueios de transferência para peers e para parent, isso é o que eu vou tirar.

11:17

Ele precisa...

11:19

ter liberdade para fazer essa transferência. Na verdade,

11:24

nós até poderíamos colocar para bloquear que ele faça transferência para outros

11:31

irmãos. É porque sempre que ele acabar,

11:35

ele vai ter que ir para o operador dar conta mesmo.

11:37

Então, você está vendo como que cabe uma configuração

11:41

para ter essa rédea e ter uma segurança do comportamento? Ótimo.

11:48

Então, vamos...

11:52

Vou dar mais uma vez.

11:58

Então, list minhas faturas.

12:04

Está aqui os três subagentes. Então, ele chegou no

12:08

consultor de faturas pedindo o ID do cliente.

12:13

Então, agora vai consultar, atua.

12:19

E aí, está aqui.

12:23

Não sei por que ele não avançou. Ele continuou aqui no evento passado.

12:29

Então, o tanto de coisas que aconteceram aqui.

12:33

Ele foi lá, executou a ferramenta, temos aqui a resposta.

12:42

Como ele terminou, vai fazer a transferência para o operador da conta. Transferiu.

12:51

E aí nós vamos ter o aviso de performance,

12:53

porque antes nós tínhamos o system prompt,

12:56

que estava alinhado com o consultor de faturas.

13:01

Agora ele volta para o operador da conta. Então aquele aviso que ele perde o cache. Ok.

13:11

Então, aqui nós temos a transferência para o Acme Status.

13:17

E aqui que está o erro, porque como é uma operação que

13:22

vai executar e vamos ter a resposta,

13:25

mora o problema porque dependendo do que for para esse agente,

13:29

ele pode começar a interagir com o usuário e nós não queremos essa interação.

13:35

Então, é aí que entra justamente, por

13:39

todas as questões, o modo single churn.

13:50

Então, vê como isso muda tudo?

13:56

Então, agora, vamos

13:59

listar minhas faturas, o

14:10

ID do cliente, e

14:18

agora vemos que não tem mais essa transferência do controle.

14:22

Nós já tínhamos visto o

14:24

obter status, na verdade, o Acme Status, como subagente,

14:29

vai ser chamado como Matu, como nós já havíamos visto.

14:33

Então, aqui, ele transferiu o controle de volta para o operador da conta.

14:39

Aí agora vem o agente e executa a ferramenta dele e depois,

14:44

no momento, está apresentando problemas de intermitência. Então,

14:50

lamento informar que os serviços estão

14:52

temporariamente indisponíveis devido a uma intermitência.

14:58

Poderíamos formatar essa mensagem e fazer quaisquer outras coisas.

15:04

Então, aqui, nesse ponto,

15:09

que é onde o operador da conta já tem o controle, o

15:14

system prompt que antes estava focado no consultor de faturas mudou,

15:17

por isso que tem um aviso de performance.

15:20

Ele vai falar, olha, antes eu tinha um prompt desse,

15:23

agora mudou, então perdi o cache.

15:28

Aí ele vai falar que é o operador da conta.

15:32

Temos os dois subagentes que ele pode fazer a transferência se ele quiser,

15:39

Então temos a tool de transfer agent. E o Acme Status.

15:46

E aí que é interessante, porque até antes,

15:49

quando o Acme Status estava com o modo chat,

15:55

ele apareceu aqui embaixo.

15:58

Então, nós colocamos uma restrição aqui em cima,

16:01

que, olhando por um ponto contraditório,

16:05

na verdade, entra em contradição com o que está aqui.

16:08

Nós estamos falando que, se houver um agente melhor para ele redirecionar...

16:14

isso vai em confronto com o que nós colocamos aqui em cima.

16:18

Mas essa instrução vai prevalecer.

16:22

Nós colocamos algo específico,

16:25

então ela tende a prevalecer sobre aquela instrução genérica. Mas, obviamente,

16:31

se eu tiver um agente que

16:36

é muito ruim para fazer inferência,

16:40

ainda assim, nós podemos ter um comportamento...

16:46

Então, por isso que é importante você fazer os testes e ver

16:49

se está trabalhando com o modelo que você quer utilizar.

16:53

Então, dessa forma, nós conseguimos usar o Single Churn.

16:57

Eu posso ter uma mistura desses modos de agente.

17:02

Então, nós temos aqui dois que são chat e esse aqui que é Single Churn, como

17:11

uma tool. Ele recebe histórico, mas não detém controle,

17:15

e não vai acabar tendo uma resposta direta para o usuário. A ideia não é essa,

17:20

que é justamente essa do status do sistema da Acme.

17:24

E voltando para o nosso exemplo,

17:26

eu quero lembrar sobre o que é passado para esse agente Single Churn.

17:34

Temos o parâmetro request, e

17:38

quem delimitou essa mensagem, que o serviço de listagem de faturas está operacional,

17:42

então veja que o serviço de status poderia ver algo específico, é

17:47

o próprio...

17:49

A própria LLM que

17:51

inventou isso aqui, essa frase, criou essa frase,

17:55

para o agente poder fazer essa invocação.

18:00

Então, nós

18:02

temos um texto que, a princípio, não é determinístico,

18:07

ele pode dizer a mesma coisa de forma diferente.

18:12

Então, a gente recebe lá e vai fazer a sua interpretação e vai passar a bola.

18:22

Nós podemos até ver aqui na resposta,

18:27

quando foi passado tudo isso com o erro, temos

18:32

todo o histórico que foi passado, teve

18:36

o transfer que aconteceu, mas

18:42

teve aqui o

18:45

erro. Então, ele não perguntou nada de banco de dados.

18:50

Então, a gente que determinou, olha, o serviço de faturas está operacional,

18:55

dado o system prompt, dado o histórico das mensagens,

18:59

ele identificou que isso aqui seria necessário. Poderíamos ter mais controle também,

19:03

como que ele vai mandar essa mensagem e tudo mais,

19:06

mas é um request, ele pode mandar aqui um JSON, pode mandar um texto,

19:09

pode mandar qualquer tipo de conteúdo que ele julgar necessário.

19:13

Então, isso aí é o nosso Single Churn funcionando.

19:17

Agora com um pouco mais de complexidade.

## Resumo IA

[RESUMO_IA]