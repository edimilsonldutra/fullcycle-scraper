Módulo: Desenvolvimento de Agentes com IA\
Aula: [Arqutietura do runtime do ADK](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18486)

## Resumo da aula



## Transcrição

00:00

Nesta aula nós vamos falar sobre a arquitetura do runtime do ADK.

00:05

Agora nós temos condição de ver todos esses componentes trabalhando em conjunto.

00:10

Já criamos todo esse processo de forma manual. Nós temos que entender bem tudo

00:18

o que acontece desde quando o usuário envia sua mensagem.

00:22

Nós já vimos o app, o runner,

00:26

o session e falamos um pouco do invocation context. Agora nós vamos entender...

00:31

para valer o que está acontecendo desde quando o usuário envia uma mensagem

00:35

até quando o LLM responde e tudo o que está acontecendo por trás.

00:39

É crucial que você entenda isso,

00:41

porque vai melhorar o seu conhecimento com o próprio ADK e

00:44

também para a construção de aplicações ágeis com qualquer outro framework.

00:49

Nós já vimos que tudo começa com o runner.

00:55

O runner que é o nosso grande facilitador.

01:02

Quando nós estamos falando de turno, estamos falando de invocação.

01:08

Então significa que o runner foi provocado por alguém.

01:12

O usuário mandou uma mensagem, ou alguém está utilizando o nosso agente.

01:17

Nós conseguimos ver isso aqui no ADK Web.

01:21

Toda vez que eu mando uma mensagem, é gerado o invocation ID, que é um UID.

01:29

Então acontecem algumas coisas. Vai ter ali a resposta.

01:34

que é retornada para o usuário. Pois quando ele envia uma próxima mensagem,

01:37

é gerado um novo Invocation ID. Pode acontecer N coisas.

01:42

Então o runner gera esse Invocation ID e

01:50

semeia um objeto que é o Invocation Context, o contexto da invocação.

01:58

É um objeto efêmero, ele não é gravado em nenhum lugar.

02:02

O que é gravado é a sessão. Ele pode ser remontado a qualquer momento.

02:07

Então ele pega o app,

02:10

o session service e o gerenciamento de plugins, o app,

02:14

nós já vimos que não é obrigatório colocar,

02:16

se nós não colocarmos ele vai definir um dele,

02:19

mas nós podemos criar o nosso app,

02:21

que não tem nenhuma lógica, é apenas um blueprint declarativo,

02:24

é apenas um contrato com o nome, o root agent, plugins,

02:29

configuração de cache, configuração de retomada e compactação dos eventos.

02:35

E obviamente isso aqui já vai conter, como ele tem o agente,

02:38

toda a nossa árvore de agentes.

02:41

Então eu tenho o invocation ID que já foi gerado,

02:44

a sessão também que já foi gerada anteriormente,

02:49

e é interessante observar no run

02:52

async que eu não passo a sessão,

02:56

eu passo apenas o ID da sessão nele,

02:59

porque como ele tem acesso ao session service,

03:03

ele prefere consultar a sessão lá dentro.

03:07

Nós criamos a sessão ou consultamos uma sessão já existente, nós já vimos isso.

03:13

Vamos aqui até um... Esse aqui acaba gerando a sessão,

03:16

enfim, mas ele precisa de uma sessão.

03:19

E também temos o SessionService, porque ele vai administrar,

03:23

ele que vai fazer as chamadas para fazer o save da sessão, e

03:30

o agente e as configurações dele, que vem aqui do app.

03:34

Então, esse objeto é feito uma cópia dele... e passada para os agentes,

03:41

então atinge todo mundo, todo mundo tem as suas configurações e tudo mais.

03:46

Então, logo de cara,

03:48

nós já vemos o benefício de não invocar o agente de forma direta.

03:52

Então, tenho essas camadas que me permitem organizar a execução do agente.

03:59

E a cada vez que nós vamos tendo essa invocação,

04:04

nós já vimos que nós temos os eventos.

04:09

Nós podemos navegar entre os eventos aqui do lado, nós temos os 14 eventos, e

04:21

esses eventos ficam dentro da função e eles vão sendo armazenados.

04:24

Nós já vimos no armazenamento da sessão, nós

04:32

já vimos que há uma tabela de sessões e uma tabela de eventos.

04:38

Então, a cada evento que vai sendo produzido, nós temos ali os 14,

04:41

ele vai gravando esses eventos. Ele usa uma operação de append event,

04:46

que grava o evento,

04:49

mais o state delta, que são os dados daquele evento.

04:54

Por exemplo, o agente, principalmente o subagente, acaba produzindo um

05:01

resultado. Nós podemos ter uma output key, vamos

05:10

supor que seja XPTO. Então, esse XPTO...

05:15

acaba fazendo parte do state e de outras coisas

05:18

também que podem ter sido definidas nas tools.

05:21

Então, é o estado ali do evento.

05:23

Ele não muda.

05:25

Mas esse state também está presente dentro da sessão.

05:31

Esse aqui é o que é o atual,

05:33

considerando que eu estou no estágio atual daquela sessão.

05:37

Estou aqui na minha última mensagem. Então, eu tenho qual é o estado geral.

05:42

Mas cada evento tem o seu estado congelado. Assim, nós conseguimos fazer...

05:46

a construção, então ele vai fazendo o armazenamento.

05:52

E aí, nós temos uma

05:55

cardinalidade, porque nós sempre olhamos bem para banco de dados,

05:59

nós podemos falar que uma sessão tem N eventos que aconteceram,

06:05

obviamente, nessa sessão que nós vimos ali, tem 14 eventos,

06:11

e uma invocação,

06:13

ela faz parte, obviamente, de uma sessão, mas ela tem também os seus

06:20

N eventos, porque

06:24

vendo aqui no trace, essa invocação que aconteceu,

06:30

essa que está aqui, quando eu digitei o cliente 123,

06:33

que vai acabar desencadeando na chamada de

06:36

listar faturas e até o finish task,

06:40

que vai ser uma outra tool que é nativa do ADK,

06:43

nós temos vários eventos que estão acontecendo aqui.

06:49

Nós temos o evento da mensagem do usuário, então, userMessage.

06:58

Temos a resposta da LLM, que é o functionCall,

07:01

que ele está pedindo. Olha, chama aí a listafaturas.

07:07

Mas temos também o functionResponse, que

07:10

é a resposta da tool.

07:16

Então, veja que interessante. Só nesse invocationId,

07:22

eu já tenho esses três aqui.

07:27

Logo de cara, porque sempre que eu tenho uma tool,

07:29

eu tenho o functionCall e o functionResponse. Posso ter outros N.

07:34

Um invocation tem N eventos.

07:39

Então, nós podemos ter uma visibilidade interessante sobre o que está acontecendo.

07:46

O runner é o orquestrador da invocação, ele gera o objeto, o agente invoca,

07:53

vai recebendo a resposta da LLM,

07:56

chama tools e a partir disso os eventos são gerados e

08:01

o runner vai gravando à medida que eles vão sendo gerados. Aqui embaixo,

08:06

nós temos uma cascata da invocação que mostra com

08:09

mais detalhes tudo o que está acontecendo.

08:11

Então, temos o usuário que acionou o runner

08:15

via run async e mandou uma nova mensagem.

08:19

Então, o runner gera o invocation ID, carrega a sessão e grava esse primeiro evento,

08:25

que é a mensagem do usuário. Então, ele gera o invocation context.

08:32

Aciona o agente, que no caso seria o coordenador,

08:36

mas aqui nesse ponto, quando ele gera o invocation context,

08:42

ele aciona o session service e já salva os eventos no banco de dados. Ele faz um append event,

08:49

ele vai adicionando os eventos lá na tabela do banco de dados.

08:55

Quando chega no agente, ele faz uma operação de contexto .agent igual a self,

09:01

que é o this do Python,

09:03

apenas para falar que ele é o agente que está rodando no momento,

09:08

apesar de o contexto já vir com o agente.

09:12

Mas imagine que eu possa ter um transferToAgent,

09:16

então mudo o controle,

09:19

então isso aqui sempre garante que eu vou ter

09:21

o agente correto no contexto da invocação.

09:24

Aí tem uma classe chamada BaseLLMFlow, que ela vai repetir,

09:31

vai fazer um loop,

09:33

até que nós tenhamos um isFinalResponse. Lembrando que o isFinalResponse não é uma

09:42

propriedade, ele é apenas um método em que nós fazemos algumas verificações.

09:48

Verifico algumas coisas do evento, está vendo aqui em cima o evento?

09:52

Verifico algumas propriedades para saber se esse evento

09:55

é a resposta final do agente.

09:59

Então, a cada execução que nós fazemos,

10:06

vai se rodar esse run onStepAsync, que

10:11

vai chamar o generateContent, ou seja, aqui ele vai fazer a chamada para a LLM,

10:17

e nós vemos esse generateContent aqui, que

10:22

nós chamamos e recebemos a resposta.

10:24

Então, quando o

10:27

agente retornou um resultado, ele pode ter retornado um function call,

10:32

então vai fazer com que o agente execute esse

10:37

function call. Então, aqui também é gerado um evento.

10:40

Então, eu tenho sempre... Eu volto aqui

10:49

novamente para o agente.

10:51

O agente que vai acabar invocando essa

10:57

tool. Aí a tool recebe uma resposta. Aí eu venho aqui para cá novamente e

11:03

chamo o LLM de novo.

11:05

O LLM vai me dar uma resposta, no caso agora vai ser a final.

11:09

Então, ela é retornada para o usuário. Então,

11:11

isso aqui roda. Apenas uma comunicação com o LLM.

11:17

Se foi para a tool, vai voltar aqui novamente e vou executar de novo. Ah,

11:22

pedi para fazer outra coisa, aí volta de novo até que eu tenha a resposta final.

11:28

Então, ele vai gravando o que for necessário. Então,

11:32

ter a visibilidade de tudo isso aqui é interessante.

11:35

Relacionado com os eventos que nós vemos aqui, nós temos noção de tudo que está...

11:42

acontecendo. Nós já vimos esse comportamento que quando a tool vai ser executada, como

11:56

essa aqui que foi executada,

12:00

temos a resposta que

12:03

ele pediu um function call.

12:06

Então isso aqui vai gerar um evento.

12:10

Quando ele executar a tool, vamos

12:17

ter o function response.

12:21

Você pode ver esses detalhes, mas aqui em Trace a gente consegue ver.

12:25

Nós já tínhamos visto isso no curso.

12:27

Então tem essa cadeia de eventos que sempre vai sendo remontada.

12:32

Como o invocation context é um objeto para aquela invocação,

12:40

então imagine que eu parei o meu agente e voltei

12:44

no dia seguinte a conversar com ele naquele mesmo session ID.

12:50

Então, essa próxima mensagem que eu enviar aqui vai

12:55

ser a mensagem com todos os eventos agregados. Ele vai juntar. Nós podemos ver.

13:05

Por exemplo, nessa mensagem, que dá para marcar aqui,

13:12

nós temos o

13:15

System Prompt, as Tools e mais todas as partes de comunicação.

13:22

Então, com isso, ele sempre é efêmero,

13:26

ele sempre gera a parte das informações existentes.

## Resumo IA

[RESUMO_IA]