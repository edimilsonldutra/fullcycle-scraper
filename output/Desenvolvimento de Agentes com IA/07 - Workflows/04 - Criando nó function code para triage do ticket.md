Módulo: Desenvolvimento de Agentes com IA\
Aula: [Criando nó function code para triage do ticket](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18568)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos criar o primeiro nó do grafo do nosso workflow.

00:04

Nós vamos começar a criar o ticket resolution.

00:08

Nós já sabemos que o start é o primeiro nó. Somos obrigados a declará-lo.

00:15

Já está presente lá no workflow, no que a gente fez na aula passada.

00:19

E agora vem o próximo nó.

00:21

Vai ser o quê? Um agente, uma tool,

00:24

um function code. Vamos pensar que nós não temos...

00:28

o ticket ID logo

00:31

de cara, ou ticket, porque

00:36

o ticket receptionist vai estar disponível para o usuário manipular

00:40

através de uma aplicação web ou de um,

00:42

sei lá, enfim, o que seja. Isso na verdade é só a capa.

00:46

A questão é que como o atendimento não vai ser feito ali na hora para o usuário,

00:51

vai ser só informado que o ticket foi aberto,

00:53

então nós poderíamos imaginar que publica-se numa fila

01:03

que esses tickets vão sendo criados,

01:06

então tem um consumidor, pode

01:12

ler dessa fila, essa fila pode ser um Redis, um RabbitMQ, ou qualquer coisa que seja,

01:16

na verdade não importa. O consumidor vai ver que tem uma nova mensagem,

01:21

então ele inicia o runner,

01:23

como nós já vimos, basta iniciar o runner e passar ali a primeira mensagem,

01:29

chamando esse agente e o nosso workflow vai começar.

01:33

É assim que vai acontecer o processo. Então nós não temos o ticket, nós

01:38

vamos ter que recuperá-lo.

01:41

E a primeira coisa que nós podemos fazer é analisar a classificação.

01:47

Como nós temos aqui no modo, a categoria da classificação pode ser algo de billing,

01:54

de bug, de feature request, de onboarding,

01:56

um compositive que envolve dois, pode ser um undefined,

02:01

não conseguimos definir muito bem o que o usuário está falando.

02:04

um out of scope e um incidente de segurança,

02:08

também que seria algo que se a gente

02:11

identificasse que era algo que alguém tentando manipular os

02:17

agentes para conseguir alguma vantagem, poderíamos enquadrar isso aqui também.

02:22

Até não definimos ali na lógica do ticket classifier nada em relação a isso.

02:27

Mas vamos pensar que logo de cara, essas duas aqui, ou o out of scope,

02:33

como isso está presente lá no System Prompt do Ticket Classifier.

02:38

Se a gente verificar que a classificação é desse tipo,

02:42

eu nem preciso fazer nada, não vou precisar mandar para nenhum agente,

02:45

porque fora de escopo, eu já posso definir uma mensagem padrão que

02:50

já retorna um resultado.

02:54

Então, o que eu quero demonstrar aqui é que eu

02:57

posso fazer uma triagem de acordo com a categoria da classificação.

03:03

E isso pode ser determinístico,

03:06

eu não preciso de colocar isso no agente. Então, aqui nós otimizamos.

03:10

O que nós já podemos verificar não é necessário,

03:14

levantar o agente, comunicar com o LLM, gastar com tokens e etc.

03:19

Então, nós vamos criar o primeiro nó depois do start,

03:24

vai ser um function code.

03:26

Eu vou criar aqui dentro um node, que

03:33

é assim que normalmente nós fazemos com...

03:35

o ADK, e aqui nós vamos colocando as nossas funções. Tudo é Node,

03:41

mas quando a gente olha para cá, a gente sabe que vai ter essas funções aqui.

03:45

Eu vou chamá -la de

03:47

TriageTicketNode.

03:53

Para que ele seja um Node, precisamos colocar o decorator Node do ADK.

04:02

Então, de google .adk

04:04

.workflow import Node. Pronto.

04:12

Essa função pode ser tanto assíncrona como síncrona,

04:16

dependendo do que você estiver fazendo.

04:18

Isso aqui encaixa tudo no que nós já aprendemos em relação aos generators,

04:23

ao padrão assíncrono, ao async generator, enfim. Então, nós

04:31

vamos receber aqui o contexto.

04:35

Imagine isso aqui como se fosse lá aquele tool context, porque

04:40

logo de cara...

04:42

Aqui eu não tenho nenhuma entrada de dados que alguém está processando.

04:46

O start não vai me dar nenhuma informação.

04:48

Nós poderíamos receber aqui também a saída do nó anterior. Eu não tenho isso.

04:55

Então o contexto vai me dar acesso ao state,

04:58

a mensagem do usuário, a qualquer outra informação que eu necessito.

05:03

Então vamos importá -lo aqui de Google ADK, import context. Pronto. E agora?

05:12

Como que nós vamos trabalhar com o Ticket ID?

05:15

Se eu não recebo essa informação via mensagem, eu

05:22

posso receber via State, o que acaba sendo mais formal.

05:27

Eu passo o Ticket ID, inclusive esse State,

05:31

ele vai acabar valendo para toda a sessão que é criada com esse workflow.

05:37

Então, nós vamos pegar o Ticket ID de...

05:43

context, state, getTicketId.

05:50

Nós não sabemos se de fato vai ter um valor,

05:54

e a gente até poderia já colocar aqui uma validação, mas de qualquer forma,

06:00

eu já quero tentar pegar o ticket usando lá o meu repo,

06:05

e tem um getTicket passando esse ticketId.

06:09

Então como eu tenho operação assíncrona, na verdade acho que é getTicket só.

06:16

Como tem a operação assíncrona, eu preciso colocar o async aqui.

06:21

Então, se verificarmos que o ticket não existe,

06:26

não tem por que nem eu fazer mais nada,

06:29

não tem nenhuma verificação a ser feita.

06:31

Então, o que nós fazemos aqui? A ideia de um nó é sempre produzir um evento.

06:38

É como se fosse o resultado dele.

06:43

o agente também acaba produzindo um evento no seu retorno. Então,

06:47

na verdade, todo mundo, todos os componentes do ODK produzem um evento.

06:52

Só que aqui a gente vai retornar esse evento para valer. Então,

06:56

a gente vai criar o evento, vou importar ele do lado aqui do context, e

07:04

aí a mensagem vai no message. Então,

07:08

podemos colocar aqui ticket não encontrado. Vamos

07:13

colocar em português.

07:16

Não encontrado.

07:19

Poderíamos passar sem interpolar o id, mas não importa.

07:24

A ideia vai mostrar esse erro exatamente porque

07:28

das informações do evento não temos aqui o message,

07:33

mas ele sim é aceito. Tem que ser feita uma atualização,

07:39

Uma correção na tipagem do evento.

07:42

Então, dessa forma aqui, nós já temos...

07:47

Um primeiro nó executando alguma coisa.

07:49

Então vamos tirar o recepcionista daqui que foi apenas

07:52

para que a gente pudesse fazer o teste.

07:55

Então temos a triagem do ticket.

08:02

Sempre que nós formos criar essas funções, nós vamos sempre colocar node,

08:07

exatamente para que nós não conflitemos com as tools.

08:12

Isso aqui também é uma outra convenção. Vale a pena falar. Então

08:23

vamos...

08:27

Pegar o nosso agente mais uma vez.

08:30

Aí aqui, como a gente não vai ter nenhum state,

08:33

na verdade basta mandar qualquer coisa e dar um enter. Veja só.

08:40

Start o ticket.

08:42

Na verdade isso aqui está desatualizado. Vou tentar atualizar do zero.

08:52

Então, é só mandar qualquer coisa.

08:54

Aqui nos dois eventos que nós temos, nós não vamos ter...

09:01

Nem request e nem response para LLM. Não temos nenhum agente envolvido.

09:06

O function code é totalmente determinístico. Nós

09:12

podemos avaliar isso aqui. Até mesmo na

09:17

questão do evento. Está

09:27

vendo que veio o ticket não encontrado como a

09:31

primeira parte do conteúdo. Quando nós colocamos o message dessa forma, como

09:37

ele está presente aqui,

09:39

aí ele... ele vai colocar dentro do content. A gente consegue passar o content,

09:44

mas acaba sendo melhor passar o message.

09:48

Aí dá para colocar aqui um type ignore,

09:52

para ele não ficar chiando com isso,

09:54

ou até mesmo pegar o tipo do erro que

09:58

o PyLink está verificando e adicionar também esses comentários.

10:04

Como nós já temos o ticket, podemos fazer já a primeira decisão para o out of scope.

10:10

Então, depois... Depois que passou esse if,

10:12

se não retornou nada, eu sei que eu tenho o ticket,

10:15

nós podemos ver, vamos pegar a classificação e

10:21

verificar se o

10:24

classification.category

10:27

outofscope.

10:41

Então, se é out of scope,

10:44

nós vamos retornar uma mensagem.

10:48

Mas, pensando aqui nesse caso que eu não tenho mais nada a fazer,

10:53

retornar a mensagem não é a única coisa que eu tenho que fazer.

10:58

Eu tenho que salvar esse ticket novamente com a

11:05

resposta,

11:08

colocando que ele está resolvido, eu preciso fechar esse ticket.

11:13

O próprio fluxo vai fazer isso.

11:17

Então... Nós podemos criar aqui uma mensagem,

11:21

e aí eu tenho uma mensagem já

11:29

declarada, sim, nós podemos colocar, até

11:33

com essa anotação de tupla, múltiplas linhas, então tem uma mensagem,

11:37

o canal exclusivo de suporte da Acme Cloud.

11:40

identificamos um pedido de suporte na sua mensagem,

11:43

se precisar de ajuda com a plataforma,

11:45

descreva o problema e abriremos um novo atendimento.

11:50

Então, podemos...

11:53

falar que o ticket response é igual a essa mensagem,

11:59

agora

12:01

o ticket status vai estar como resolvido e

12:08

podemos

12:13

salvar esse ticket. A

12:18

gente tem, vamos

12:22

verificar se a gente tem aqui o update dele,

12:24

tem o update ticket, mas por que deu erro?

12:28

Aqui tem que ter, obviamente, o await, mas nós já tínhamos adicionado

12:33

O async ali. Então, depois de fazer tudo isso,

12:38

nós enviamos o evento com essa mensagem.

12:41

Pronto. Aí fica declarado no

12:47

histórico o que aconteceu.

12:49

Vamos rodar os dois agentes em conjunto como eles estão na pasta Agents.

12:53

Nós vamos passar para o ADK Web a pasta Agents. Então,

12:57

agora vai ter uma leva de agentes a ser utilizado aqui.

13:03

Então, agora tem uma listinha. Vamos começar pelo ticket Receptionist,

13:07

e aí eu vou falar assim, quero criar um ticket para falar de novela.

13:19

Falar de novela. Então é Out of Scope.

13:25

Pronto, então temos o ID do ticket, agora vamos para o Resolution,

13:31

e aí como nós já aprendemos como fazer,

13:35

nós vamos colocar aqui o ticket ID, vai ser igual...

13:41

ao valor que nós copiamos.

13:44

Então aqui nós podemos, ele não vai aceitar nada, a

13:51

gente dar um enter em nada aqui, apenas fazer um envio,

13:54

então a gente pode só enviar um A. Pronto.

14:01

Então veja só, esse é um canal exclusivo para

14:05

suporte da Acme Cloud e etc. É a mesma mensagem.

14:08

Então o mesmo trecho, aconteceu os dois eventos.

14:13

E agora nós podemos verificar com o SQLite 3, com

14:20

o SELECT, acho que quebrou aqui por conta do virtual env, então

14:27

SELECT asterisco FROM TICKETS, esse

14:32

aqui é o nosso último, eu vou falar de novo,

14:35

eu já vi logo de cara, então ele está resolvido, e

14:39

aqui a mensagem que foi gravada a resposta é essa aqui.

14:43

Então, olhando para esse cenário agora,

14:47

o que nós poderíamos fazer aqui além

14:53

de fazer esse salvamento é um disparo via e -mail ou

14:58

qualquer tipo de comunicação que seja para que o usuário fosse notificado.

15:03

Então, quando ele acessasse uma interface,

15:07

mostraríamos os tickets disponíveis e

15:12

na hora que ele acessar o ticket, tem ali a mensagem.

15:16

Nós não estamos fazendo aqui um caso que ele possa continuar...

15:19

a interagir com esse ticket e aí o suporte continua analisando.

15:24

Inclusive, é até um bom estudo de caso,

15:26

uma extensão do que nós vamos fazer aqui neste capítulo.

15:31

Nós temos muitas coisas que nós poderíamos encaixar nesse agente. Pense, né?

15:37

Pois bem, então criamos o nosso primeiro nó, que é um function code.

15:42

Então, vamos dando prosseguimento à nossa resolução do ticket.

## Resumo IA

[RESUMO_IA]