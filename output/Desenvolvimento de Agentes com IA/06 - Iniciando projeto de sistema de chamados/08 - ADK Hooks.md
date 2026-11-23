Módulo: Desenvolvimento de Agentes com IA\
Aula: [ADK Hooks](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18563)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre os hooks do ADK.

00:03

Uma vez que um ciclo é iniciado, vários hooks são disparados,

00:09

que vão ser chamados de algo que aconteceu no meio desse processo.

00:15

Essa imagem que está aqui ilustra muito bem essa ideia dos hooks.

00:20

Quando o usuário manda uma mensagem, temos o onUserMessage.

00:27

Então, nós podemos adicionar um callback,

00:30

no meio do agente para capturar essa mensagem,

00:33

fazer um log dela ou fazer qualquer modificação.

00:38

Quando o runner começa a executar, tem o before run,

00:43

antes dele executar, podemos fazer alguma coisa.

00:47

Aí, quando o agente é acionado, tem o before agent. E por aí vai.

00:52

Então veja que tem o agente, o model e a tool.

00:56

Então temos o before e after para cada um.

01:00

E aí entra, até no caso da tool aqui, o onToolError,

01:03

que acaba sendo também esse hook. Mas tudo isso acaba desencadeando em eventos.

01:10

Toda vez que o agente processa, o model processa,

01:16

a tool também processa, nós temos os eventos.

01:19

E aí tem um dos hooks mais importantes, na verdade ele concentra tudo,

01:23

que é o onEvent. Nós conseguimos capturar aquele evento.

01:28

Podemos até mudar o evento que vai ser produzido,

01:32

desencadear um comportamento diferente.

01:36

Conseguimos transformar essa execução que está acontecendo. Então,

01:40

nós podemos manipular esses hooks para fazer o log,

01:44

preparação da tarefa, enfim, uma série de configurações.

01:48

Nós vamos fazer um exemplo com o Ticket Receptionist

01:50

em que o agente não vai conseguir responder.

01:55

Ele vai dar um erro que nós chamamos de response mal-formed, ou

02:02

vai responder vazio, na verdade vai responder como uma string vazia,

02:08

não temos nenhum tipo de conteúdo.

02:10

E nós vamos usar os hooks para que nós possamos contornar esse comportamento,

02:15

aprendendo como eles funcionam. Eu mudei o modelo para o Gemini 2.5 Flash,

02:20

porque aí vai ficar mais fácil da gente tentar simular esse comportamento.

02:24

Então vamos colocar aqui, quero criar... um ticket.

02:28

Como é aleatório, pode ser que ele não aconteça de primeira.

02:32

A mensagem é

02:34

estouro. Aqui nós estamos trabalhando, obviamente, com más práticas,

02:39

porque a gente teria que pedir detalhes desse ticket para o usuário.

02:44

Criou. Então, quero criar outro ticket. Erro 500.

02:59

Pronto. Aconteceu um dos comportamentos.

03:03

Veja que... Foi feita a classificação e

03:08

tivemos uma resposta vazia. Veja só, o

03:16

conteúdo da LLM não tem nada. Tem um stop e

03:22

não veio nada. Não tem erro, nós podemos até olhar aqui os logs, não tem nada.

03:30

É alguma coisa que nós fizemos de errado? Não, é o comportamento do modelo.

03:33

Com todo o conteúdo que foi enviado para ele,

03:38

nós podemos pegar aqui a request, já tem o system prompt.

03:43

Aí, tem as tools, inclusive o registrar ticket está lá. Nós já estamos aqui na parte

03:51

13, que

03:53

foi a

03:56

classificação. Ela é

03:59

Enviada ali para o modelo e não teve nada.

04:04

Então, pode acontecer um mal formed ou length.

04:09

O mal formed é um erro que acontece.

04:13

Do modelo não conseguir gerar a resposta.

04:15

É um tipo de resposta vazia, mas acaba mostrando um erro aqui.

04:20

Nós conseguimos capturar esse erro. Ou uma resposta vazia, que é um erro silencioso.

04:26

E dessa forma, imagina que o usuário recebe isso, ele vai ficar totalmente perdido.

04:32

Ele teria que interagir, continuar e tentar novamente. Então,

04:35

nós podemos corrigir esse comportamento através de hooks.

04:40

Então... Eu adicionei três callbacks, nós vamos utilizar o before model callback,

04:46

o after model callback e o after agent. Então,

04:51

pegando aquela imagem, veja, o before model, ou seja,

04:58

antes do model executar, o after model, depois do model executar e o after agent.

05:04

Então, esse aqui vai executar primeiro, antes de ir lá para o model.

05:09

Depois do model, é o segundo, e aí vem para o agent,

05:13

aí vem o after agent. Nós conseguimos capturar, então, um, dois e três.

05:21

Qual vai ser a ideia por trás disso?

05:25

No before model, usamos um captureRequestCallback, nós vamos capturar a request.

05:32

Nessa variável de requests pendentes, é um dicionário,

05:36

chave valor, que nós vamos armazenar essas requests,

05:40

que são enviadas para o LLM. Então, nesse callback,

05:44

nós recebemos o contexto do callback e qual é a request que está sendo feita.

05:49

Isso aqui é legal, porque nós conseguimos interferir nessa request,

05:52

mudar ela, fazer uma série de transformações.

05:56

Então, eu pego esse dicionário com o ID da invocação daquele turno,

06:02

guardo o LLM request que nós vamos usar mais tarde. Então, é somente isso.

06:09

Veja que eu posso retornar um LLM response fazendo com que

06:14

eu já determine uma resposta como se fosse a LLM que determinou. Então, isso aqui é legal porque,

06:19

às vezes, dependendo do que estiver acontecendo no seu agente,

06:21

você nem deixa ir lá para a LLM.

06:23

Você já faz um LLM response e coloca aqui a sua resposta.

06:28

Isso aqui é muito utilizado.

06:30

Ok. Então, o primeiro comportamento. Então, o próximo é o after model.

06:35

Então, tem o retry malformed callback.

06:39

Nós vamos receber mais uma vez o callback context e aí o llm response,

06:45

que é a resposta do que foi executado lá na LLM.

06:48

Então, a primeira coisa é verificar se eu tenho as condições para fazer o retry.

06:55

Capturo o llm request lá da minha variável,

06:59

uso o pop em vez do get, porque ele já pega

07:03

tirando do dicionário,

07:06

porque senão a gente fica armazenando isso infinitamente

07:08

e vai usando cada vez mais memória.

07:11

No software. Então, eu passo o ID da invocação que é aqui.

07:16

Caso não tenha nada, vai ser nome. Ok.

07:19

Tenta identificar qual é o código do erro. Então, do llmResponseErrorCode,

07:25

nós vamos tentar pegar o atributo name. Está vendo esse getAttribute?

07:30

É uma função do próprio Python que você tenta pegar uma propriedade de um objeto.

07:36

Caso não tenhamos nada,

07:38

Ele vai pegar o próprio error code.

07:41

Então, nós vamos ver se o code não está

07:44

Presente nos erros que nós possamos retentar com o LLM.

07:51

Isso aqui é uma variável que eu deixei aqui em cima.

07:52

Então, é retornado um malformed response.

07:56

Então, se esse erro não está presente, eu poderia colocar outros também.

08:01

Se não está presente aqui, se não é uma resposta vazia,

08:04

e para isso eu tenho um helper,

08:06

veja só. Eu passo o LLM response para esse helper.

08:10

Se for uma resposta parcial,

08:13

se eu estiver trabalhando com streaming, então não é vazio.

08:17

Se tiver error code, também não é vazio.

08:21

Aí nós vamos pegar, então, o conteúdo e as partes.

08:24

Então, para cada parte, nós olhamos se tem texto,

08:27

se tem o function call que nós já vimos,

08:30

se tem function response, se tem line data, se

08:35

há algum código executável, enfim.

08:38

Algumas verificações que tem lá. Aqui, na verdade,

08:41

para esse agente nem precisava disso tudo.

08:44

Apenas o texto ou esses três aqui já seriam o suficiente.

08:48

O resto não vai ser utilizado.

08:51

Mas aqui nós já abrangemos mais essa função

08:55

para ser utilizada em agentes mais complexos.

08:58

Então, se passou tudo isso e

09:01

ele não retornou falso, então é vazio.

09:04

Ok. Ou também se eu não conseguir pegar a LLM request.

09:10

Então eu gero uma cópia dessa request com esse model copy,

09:13

fazendo deep true, então ele vai copiar propriedades alinhadas.

09:18

E na parte de conteúdo da request, que é esse conteúdo que vai, eu

09:23

pego o conteúdo que foi enviado, como eu fiz a cópia, ou

09:30

se não tiver conteúdo nenhum,

09:31

fazemos esse else da listagem vazia e acrescentamos um nut,

09:38

que é o empurrãozinho.

09:41

que é um conteúdo de texto, que

09:45

é justamente para forçar a barra com a LLM. Olha, sua resposta não teve conteúdo.

09:51

Por favor, tente novamente e forneça uma resposta clara.

09:54

Um incentivo para que ele faça isso. Então,

09:56

nós grudamos isso como uma mensagem.

09:59

Porque não adianta nada a gente tentar, ficar tentando novamente.

10:03

A LLM vai retornar, tem uma chance muito grande dela retornar o mesmo resultado. Ok.

10:10

Então, nós vamos pegar... o modelo de LLM do contexto de invocação,

10:17

porque se a gente pega o agente,

10:19

esse canonical model, a gente vai pegar o Gemini 2.5 Flash, que

10:27

nós vamos fazer a chamada direta.

10:30

E aí eu tenho a parte de retries, que coloquei aqui um max de 5,

10:35

enfim, você pode definir qual número que você quiser.

10:39

Então vai de 1 até 5. Aí vai mostrar um logger. Dessa resposta e das retentativas.

10:47

Então, nós tentamos fazer o LLM generateContentAsync. Então,

10:52

aqui nós estamos fazendo a chamada direta, desabilitando o modo stream,

10:57

para pegar a resposta de uma vez. Então, uma vez que nós tenhamos a resposta,

11:02

se a resposta não for none, se não for vazia, senão ele vai retentando,

11:06

a ideia é justamente essa. Então, depois que nós fizemos tudo isso aqui,

11:11

Se eu tiver uma resposta com o conteúdo,

11:15

nós estamos olhando aqui, né?

11:16

Ou se não tiver error code, retornamos essa resposta. Ah,

11:21

esgotou o meu retry. Então, a gente vai informar.

11:26

Aqui nós estamos fazendo esse retorno do LLM response,

11:30

que é o retorno como se fosse do modo. Tive um problema técnico,

11:34

eu concluí essa tarefa. Pode reenviar sua mensagem,

11:37

por favor? Então, nós estamos depois do before.

11:42

melhor, depois do after model, então eu consigo transformar a request que está indo,

11:48

quanto transformar a response, reescrever ela totalmente,

11:51

ou fazer alguma mudança precisa.

11:54

E aí, esse after agent callback serve apenas para poder fazer a limpeza, porque

12:02

pode ser que o hook não seja executado com sucesso,

12:06

se o hook não seja executado aqui,

12:08

e aí eu vou recebendo solicitações, então isso aqui serve como um...

12:12

uma válvula de escape para limpeza.

12:14

Ele faz ali o pop apenas para poder fazer a remoção.

12:18

Aqui eu poderia até colocar um return none,

12:21

mas acaba sendo retornado none se eu não colocar nada também.

12:26

O after agent callback também eu consigo,

12:29

nesse caso aqui eu não estou interferindo diretamente na LLM, mas

12:36

depois que ele acontece, eu consigo ter um novo conteúdo.

12:42

Eu posso avaliar o que foi feito ali.

12:44

e poderia controlar qual é a resposta final que vai para o usuário.

12:48

Eu fiquei tentando algumas vezes até conseguir,

12:51

porque tem alguma hora do dia que esse erro nem acontece.

12:55

Então, acabei mudando o modelo para o Gemini 2

12:58

.5 Flashlight e depois de alguns minutos deu certo.

13:03

Então, veja só, tem um warning aqui com o agent na linha 163.

13:08

Resposta vazia, retry 1 de 5. Aí depois a coisa...

13:11

acabou acontecendo. Então eu fiz essa mudança aqui.

13:15

Então isso é muito comum de usarmos vários hooks em conjunto para dar consistência

13:22

a um comportamento que nós queremos alterar ou

13:25

fazer no meio do processamento do turno.

13:28

Ou às vezes nós podemos usar o

13:32

hook para um comportamento específico.

13:34

Tem vezes que diante de alguma coisa que acontece,

13:38

não, não vai nem lá para o modelo.

13:40

Então nós podemos usar

13:43

o before model callback, ah, verifiquei alguma coisa,

13:47

já faço o LLM response como nós vimos que ele pode ser montado.

13:52

Então nem vai lá para o LLM e já retorna o resultado.

13:55

Então nós capturamos todos esses comportamentos e podemos fazer

14:01

qualquer tipo de transformação e processamento no meio desse processo.

## Resumo IA

[RESUMO_IA]