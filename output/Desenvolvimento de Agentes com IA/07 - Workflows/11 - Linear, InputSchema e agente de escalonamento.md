Módulo: Desenvolvimento de Agentes com IA\
Aula: [Linear, InputSchema e agente de escalonamento](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18575)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos criar a outra ramificação da triagem do estorno,

00:04

que é o escalonamento para um ser humano. Eu não consegui fazer o estorno,

00:08

tem a questão ali do limite que nós vimos,

00:10

pode ter algo obscuro, então o ser humano vai precisar interceder.

00:18

Então, como vai ser esse escalonamento?

00:20

Vamos pensar que o ser humano vai interagir com esse agente de AI, talvez

00:27

não seria nem bom. Isso acontecer.

00:32

A empresa poderia ter qualquer tipo de ferramenta

00:36

que ajudasse a ela a entender esses tickets.

00:40

Poderia usar um Gira, um Linea, Plane, enfim,

00:46

qualquer uma dessas ferramentas. Então, quando

00:51

o usuário vê aquele ticket dentro dessa plataforma,

00:55

ele vai lá e toma uma ação. Essa ação desencadeia um webhook.

01:02

O webhook faz a chamada para uma API nossa.

01:08

E a API, obviamente, tem por trás ali o agente de AI.

01:16

Então, tem a interferência humana, mas de forma indireta.

01:21

Então, eu vou trabalhar com essa ideia.

01:24

Nós vamos criar um agente que

01:31

vai ser o escalonador. Vou puxar daqui para cá.

01:45

Então, ele vai e abre.

01:49

uma issue lá no Linear, para

01:55

a gente poder até fazer uma comunicação externa. Nós vamos usar aqui MCP.

02:02

Então, feito isso,

02:03

o usuário poderia interagir lá direto e os eventos

02:08

do Linear chegam através de uma API no nosso agente.

02:11

O agente sozinho não faz nada,

02:13

tem que ter uma camada que está na frente.

02:17

Eu implementei essa primeira parte do agente,

02:20

então nós vamos chamá-lo de escalonador.

02:22

Tenha o escalonador dev para que a gente possa rodar de forma separada,

02:26

que nós vamos fazer nessa aula, e nós vamos entender as peculiaridades desse agente.

02:30

Ele vai trabalhar com algumas questões que são

02:35

um pouco mais delicadas em relação aos outros agentes,

02:39

nós vamos conversar sobre isso.

02:42

Então aqui está o agente, nós vamos passando o

02:46

código fonte conforme nós vamos testando,

02:48

porque aí vai ficar mais fácil de você entender.

02:53

Qual é o cerne dele, qual é a lógica. Então,

02:56

vamos chegar aqui e rodar o escalonador dev.

03:04

Para que nós possamos brincar com ele no ADK Web,

03:08

nós vamos precisar colocar o ticket ID e o customer ID como estado, e

03:16

diferente dos outros agentes, ele tem um input.

03:19

Assim como nós temos uma saída estruturada,

03:22

que nós já tínhamos aprendido,

03:23

nós podemos ter também uma entrada estruturada, assim.

03:27

Nós garantimos que precisamos de tais dados e

03:31

eu só vou processar se esses dados estiverem corretos.

03:34

Então, nós temos esse escalonador input. Nós vamos ver isso daqui a pouco.

03:39

Vamos fazer um primeiro teste?

03:41

Eu vou passar aqui

03:44

No state o

03:47

Ticket ID e o Customer ID, que são as duas informações que eu necessito.

03:52

Aqui eu vou colocar 234, o Customer ID 234, pode ser qualquer coisa.

03:59

Eu preciso de uma entrada estruturada, mas eu não quero passar isso agora.

04:05

Olha só. Ao passar um A, ele acusou um erro de validação, porque

04:12

eu preciso passar o escalonator input.

04:17

Se eu não passar, o agente não vai aceitar trabalhar.

04:21

Então eu tenho a intenção desse escalonamento, qual

04:25

é o assunto que eu sumo ali, e a severidade.

04:30

A intenção é justamente para saber se é uma confirmação de...

04:34

Estorno. Eu passei daquele limiar de 50 reais.

04:38

Então, agora vai cair para o ser humano lá no linear para que ele autorize ou não.

04:43

Ele move lá a issue para concluída.

04:46

E aí, daquele webhook, executou a gente como nós já havíamos falado.

04:51

Ou o handoff, que é...

04:53

O ser humano vai assumir também,

04:55

só que ele vai tomar alguma atitude no background dele.

05:00

O agente só teria a... Que...

05:03

processar o restante da

05:07

conclusão do ticket. Colocaria ali a mensagem,

05:10

o que fosse necessário para que a gente pudesse ter esse ticket concluído.

05:14

Se ele tivesse que fazer o estorno,

05:15

ele vai fazer o estorno manualmente, etc. Aqueles casos mais raros. No summary,

05:21

nós obviamente colocamos o porquê e a severidade apenas

05:24

para poder controlar se ela é urgente,

05:25

se é alta, se é média, etc.

05:28

Então, dessa forma, aqui logo no System Prompt, veja só.

05:32

Nós falamos que ele é um agente de... Aqui

05:37

está a mistura de inglês com português, né? O escalonador.

05:43

Escalonador da Acme Cloud.

05:48

Nós podemos manipular essas informações que estão no input no

05:54

nosso System Prompt. Então, eu já coloquei logo de cara,

05:57

eu tenho a intenção, eu tenho a suma, eu tenho severity.

06:00

Aí nós poderíamos...

06:02

usá-las em qualquer momento que ele vai entender que essa

06:05

informação que está entrando ele consegue capturar e fazer alguma manipulação,

06:09

mandar para uma ferramenta ou qualquer coisa nesse sentido. Então é importante também que,

06:13

como na saída estruturada nós explicamos algumas coisas para a gente,

06:17

aqui nós podemos explicar também,

06:19

mas como o nosso contexto é bem simples,

06:22

isso nem acaba sendo necessário. Então, vamos voltar para cá?

06:30

Eu já tenho a intenção.

06:36

Já previamente criado, então nós vamos, ou melhor, a entrada estruturada,

06:42

vou pegar a intenção, que é um Confirmed Confirmation, o sum,

06:46

que é esse estorno, com mais 50 reais, para a gente possa brincar.

06:49

E o severity igual a alto. Ok.

06:54

Só que é bom que a gente faça um novo teste para não ter essa interferência,

07:01

então vamos colocar, na verdade, aqui isso e...

07:09

O outro que eu já tenho aqui. Vou

07:12

colocar 234, 234.

07:17

Pronto. Então, vamos ver o que vai acontecer.

07:21

Então, veja só o grafo do nosso agente. Temos aqui

07:25

mais de três tools, mas ele mostra as tools do Linear,

07:31

tudo nesse MCP Toolset. Então,

07:33

ele está chamando algumas tools para poder fazer a conclusão.

07:37

Qual é a conclusão? O status.

07:39

Created, com o detail do que ele fez, ele escalonou o ticket com sucesso.

07:44

Tem o ID dele lá no Linear para aprovação de reembolso.

07:48

Ele cria esse ID de forma automática na minha conta.

07:53

Então já estamos com essa informação no Linear.

07:57

Não vou mostrar exatamente o que ele criou no Linear,

08:00

mas vamos ver o output. Então tem o status,

08:05

que eu coloquei Created, Reused e Failed.

08:10

Por quê? Poxa, mas não vai criar um sucesso?

08:15

É aí que mora a peculiaridade desse agente.

08:20

Porque quando você imagina o workflow, até

08:26

o momento o nosso workflow sempre ia até

08:30

um certo ponto, e mesmo que ele tivesse algum erro no meio do processo,

08:37

tudo que fosse executado...

08:39

não teria risco de duplicidade ou de fazer um estorno mais de uma vez.

08:45

A gente não tem nenhum agente desse modelo.

08:49

Mas agora, com esse estorno, com esse escalonamento aqui, eu tenho risco.

08:54

Porque se eu crio no Linear, vou lá e crio no Linear a

09:00

minha issue, e

09:02

se acontecer um erro antes desse agente terminar, ele foi lá e criou no Linear e

09:07

a gente dá continuidade.

09:10

Ele vai fazer um save issue de novo lá,

09:12

que é a tool que ele usa para poder fazer a criação da issue.

09:17

Não tem um controle. Então, por isso que nós temos essas duas tools, de

09:23

get ticket escalation e create ticket escalation,

09:27

que nós vamos ter mais uma tabela no banco de dados local para criar esse registro.

09:33

Nós vamos colocar que há esse escalonamento e também o ID do Linear.

09:40

Temos ali o campo chamado de external reference.

09:45

Porque se acontecer dele executar de novo,

09:48

aí vai acontecer justamente do status Reused.

09:54

Se ele já não tiver retornado um Fail.

09:58

Então nós garantimos a idempotência, que nós já havíamos falado,

10:02

que agora é muito, muito importante na construção de agentes de AI.

10:08

Então tem o detalhe do que ele fez,

10:10

do que aconteceu diante do status, e a intenção do escalonamento,

10:16

estou repetindo ela mais uma vez,

10:18

porque logo depois que acontecer aqui o Created ou Reused,

10:23

nós vamos tomar uma providência de acordo com isso,

10:26

porque se for um Refund Confirmation,

10:28

aí nós já vamos abrir a possibilidade para que alguém só confirme,

10:34

e esse estorno seja executado.

10:37

Então, é o nosso primeiro agente que usa o Input Schema e Output Schema.

10:43

Aqui no System Prompt, nós

10:47

passamos as duas informações do State, Ticket ID e Customer ID.

10:51

Então, o primeiro passo desse agente é

10:54

Ver se tem o Ticket Escalation.

10:56

E aqui nós temos no Models a nossa nova tabela, que não tem... nada além.

11:03

Inclusive tem até uma forma aqui de a gente evitar que

11:05

seja criado ali mais de um ticket escalation,

11:09

tem um unique no ticket ID. Então eu não consigo criar dois registros.

11:13

Eu protejo para não ter nenhum tipo de duplicidade.

11:16

Então tem o ID desse escalonamento,

11:18

o ticket ID, o título, o borrow, a severidade e o status.

11:23

Se está aberto ou se está fechado para a gente saber ter esse controle também.

11:27

Apesar de que a gente tem o controle pelo próprio agente.

11:29

E as datas de criação e de atualização.

11:32

E o external ref, como eu havia falado. Então, temos essas duas tools,

11:37

a primeira que vai fazer a criação do ticket e a outra que é de consulta.

11:43

Então, eu recebo o ticket ID, faço a

11:47

consulta, aqui eu estou fazendo o retorno mais enxuto,

11:52

eu vou falar se existe ou se não existe,

11:54

qual é o external ref e o ID.

11:56

Poderíamos retornar o objeto, eu quis deixar mais simples.

12:01

Então, a gente usa... Isso aqui no primeiro passo para saber se existe

12:06

ou não, porque aí ele vai responder com o status Reuse.

12:09

Mas aí na hora de criar, nós também vamos criar com cuidado.

12:15

Tenha o controle para que nós geremos

12:20

esse TicketEscalation com o título com bore,

12:22

esse FormatEscalation vai apenas organizar o

12:27

título e o bore do conteúdo.

12:31

Então ele tem aqui a criação. Então, como ele verifica antes,

12:35

já é uma proteção ali para que a gente evite,

12:39

às vezes pode ter duas execuções simultâneas também, isso é muito comum.

12:45

Como em outros cenários que a gente tivesse consumidores de uma fila,

12:50

aí a mensagem pode chegar para vários consumidores,

12:53

nós temos que entender que são as mesmas coisas.

12:56

Então aqui ele consegue criar. Então, se ele viu...

13:00

que existe ou que não existe,

13:02

agora ele vai primeiro fazer essa criação no linear, então

13:11

compõe o título e a descrição claros a partir da intenção e do sumo,

13:15

incluindo o ticket ID e o customer ID.

13:20

Para o refund confirmation, deixe em destaque para aprovar,

13:23

move esse ticket para a don, que eu posso mover lá a issue,

13:28

na verdade, para a don. Caso seja um handoff,

13:30

o mano vai assumir manualmente, ele vai ter o controle, enfim. Depois disso,

13:34

crio o ticket escalation passando o ID que foi criado do

13:39

linear e aí tenho o retorno com o status e o detalhe.

13:45

A gente pode até colocar aqui

13:50

o intent, isso aqui é o mesmo do input.

13:54

Então, quando a gente analisa o histórico do agente, ele tentou consultar, não existia.

14:05

Então ele...

14:06

pega um list teams justamente para ter o controle ali de qual time

14:09

que o meu usuário faz parte e faz o salvamento lá no linear.

14:15

Então, olha só. Ele vai colocar essas informações. Na

14:21

verdade, é porque não fica.

14:23

Aqui é o resultado que ele retornou.

14:26

Então, ele passou essas informações, criou

14:29

o ticket de escalonamento e teve essa resposta aqui.

14:36

Vamos olhar agora para o código, como ficou essa parte das tools.

14:40

Então, primeiramente, eu coloquei as duas tools,

14:44

que estão justamente nesse arquivo aqui, que nós já tínhamos visto,

14:49

para depois concatenar com as tools do Linear. Então, tem o MCP Client

14:57

aqui do Linear, ele

15:00

tem um código parecido com o que havíamos feito anteriormente, em testes de MCP.

15:06

Mas eu criei uma classe personalizada porque recentemente o MCP

15:11

remoto do Linear mudou como ele informa as tools disponíveis.

15:18

Então, não estava sendo compatível conforme a identificação que o ADK precisa.

15:25

Então, nós vamos ter aqui esse Sanitize Schema

15:29

que vai verificar quando a tool vem para

15:34

o nosso agente.

15:37

Vem um JSON Schema com todas as informações dela,

15:40

nós já falamos disso aqui durante a disciplina,

15:42

então, a ideia é trocar quando vem um const por enum.

15:47

Isso está acontecendo no dia 30 de setembro de 2026, para deixar bem claro. Então,

15:54

dê uma olhada nessas informações e aqui vai mais

15:58

um trade-off quando eu tenho um servidor MCP remoto.

16:02

Eu fico à mercê de como ele está se comportando, como ele retorna esse JSON Schema.

16:06

Às vezes, a forma como a gente trabalha,

16:09

que no caso todo o ADK é construído com PyIdentic,

16:13

não estava alinhado com a mudança que o Linear fez recentemente,

16:18

porque antes estava funcionando normalmente com aquele código padrão do MCP Toolset.

16:24

Então, o que acontece aqui é que ele vai criar... adicionar essas tools,

16:29

mas nós só queremos essas três aqui, que são necessárias, porque são muitas,

16:34

então, cuidado também sempre para poder fazer um filtro.

16:37

Então, nós vamos precisar do list teams,

16:39

get issue e save issue. Aí tem o endereço do

16:46

MCP remoto,

16:47

mas também há uma variável de ambiente que você pode modificar,

16:52

mas o mais importante é a API key do Linear,

16:56

que vai permitir, obviamente, que a...

16:58

a gente faça a comunicação focada no usuário

17:01

e que estejamos autorizados a fazer essa comunicação.

17:06

Então, vamos aqui para o Linear.

17:08

Eu tinha feito um teste anteriormente. Então, esse último que fiz aqui,

17:12

o 234, olha só como fica.

17:15

Aprovação de reembolso do ticket.

17:18

Solicitação de reembolso, ticket ID, customer ID, resumo e tal. Então,

17:23

nós podemos mover esse ticket para Done. Na verdade, podemos até vir aqui.

17:29

Clicar com o botão direito e mudar para Done. Essa seria a ideia.

17:33

Então, você configura um webhook dentro do Linear,

17:37

que vai bater na sua API, que vai acessar o seu agente. Então,

17:41

agora isso fica bem claro. Então,

17:44

o humano que assumisse isso aqui, só precisaria checar algumas informações,

17:49

obviamente, pedir autorização para alguém,

17:51

para ver se ele podia fazer aquele reembolso. Ele só move.

17:56

uma dinâmica bem diferente. Se fosse lá o caso do handoff,

17:59

ele vai criar com um texto parecido,

18:03

porém aí o humano vai ter que

18:07

fazer o procedimento conforme tem que ser.

18:12

Aí nós temos que fazer uma configuração para poder pegar a

18:18

API Key. Então, vem aqui em Settings, Security e Access,

18:22

aí você gera uma API Key e coloca ela...

18:26

uma variável de ambiente que eu já coloquei

18:32

aqui e obviamente tem a linha dentro do .env. Pronto,

18:35

então nós já conseguimos fazer esse teste.

18:38

Então nós temos, recapitulando, duas tabelas, temos

18:44

também, obviamente, as duas funções no repositório para criar, o ticket escalation,

18:50

mais repetição do que nós tínhamos feito antes.

18:53

E para poder pegar... o ticket escalation,

18:56

só que sempre a gente tenta pegar pelo ID do ticket,

18:59

que é a chave única que nós acrescentamos para evitar tudo isso.

19:04

Então, são esses cenários que nós temos que tomar cuidado.

19:08

Nós vamos ter esse fluxo agora que pode ter essa repetição,

19:13

então nós temos esse controle para que isso

19:16

aqui possa ser executado novamente sem ônus nenhum.

19:21

E aí nós poderíamos já passar uma proteção, isso aqui eu já tenho que falar.

19:25

Talvez você já tenha identificado essa necessidade.

19:28

Quando nós temos aqui em nodes a primeira triagem,

19:33

imagina que eu já tenho um ticket que está resolvido ou que falhou, qualquer motivo,

19:38

o status daquele ticket não suporta mais que a gente tenha nenhuma interação.

19:44

Então, o momento certo para que a gente faça qualquer coisa também é aqui.

19:49

Se a triagem deixou passar, significa que, a princípio,

19:53

o ticket existe e que o status dele...

19:56

está ok. Então, aí vai um controle aqui em regras de negócio.

20:01

Então, nós poderíamos, num primeiro momento,

20:05

fazer várias verificações para ver se esse workflow pode de fato ser executado. Então,

20:12

com esse escalonador feito, aqui nós temos esse controle,

20:18

agora nós vamos adicioná-lo no meio do nosso workflow.

## Resumo IA

[RESUMO_IA]