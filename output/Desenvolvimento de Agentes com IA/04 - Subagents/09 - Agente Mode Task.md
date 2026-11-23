Módulo: Desenvolvimento de Agentes com IA\
Aula: [Agente Mode Task](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18264)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos trabalhar com o agente em modo task,

00:05

que é o último tipo disponível no ADK.

00:10

Vamos entender onde que ele se encaixaria.

00:14

Pegando o consultor de faturas e o consultor de assinaturas, que são subagentes,

00:21

todos os dois têm tools,

00:23

todos os dois vão precisar perguntar pelo menos uma informação ao usuário,

00:30

que é o ID do cliente.

00:32

Então, eles vão precisar de ter uma interação. Então, o modo chat faz

00:40

com que eles tenham controle, consigam pegar a informação e fazer o processamento.

00:46

Mas será que eles necessitariam ou seria legal dar esse

00:52

controle para que ele possa conversar diretamente com o usuário?

00:56

Ou esses agentes são mais de processamento de uma tarefa, de uma task?

01:02

E depois o operador da conta retorna o resultado.

01:05

Então, são dois modelos diferentes.

01:08

Nesse caso,

01:09

eu vejo mais como subagentes de processar uma tarefa e retornar

01:14

para o operador da conta do que eles terem um controle.

01:18

Porque até mesmo aqui no operador da conta, nesse caso eu estou atendendo o usuário,

01:24

eu posso ter uma série de políticas e controles que não vão estar nesses subagentes.

01:31

E até bom não estar, porque eles sejam especialistas no que eles fazem,

01:35

porque eles não comecem a fazer um monte de coisas.

01:39

Lembra lá do conceito do Solid, do Single Responsibility? Então,

01:42

nós podemos usar o Task nos dois, tanto

01:48

no de listar faturas, quanto no de colocar

01:56

ele em cima, e esse aqui também. Então,

01:59

temos três subagentes, esse aqui seria Single...

02:05

Churn ou agent2, como nós já havíamos falado,

02:08

aqui ele está como agent2 porque eu copiei o exemplo da aula anterior.

02:12

Então, veja essa arquitetura que foi montada. Nós podemos considerar que

02:19

o task é um meio termo entre o chat e o single churn.

02:24

Enquanto o single churn... Nós até testamos,

02:27

vimos que ele vai tentar mandar uma resposta para o usuário, mas vai perder o controle,

02:32

e aí nós vamos ficar num loop infinito,

02:34

porque toda hora que eu mandar uma informação, ela

02:37

não vai ser processada corretamente. Então, ele está aqui, como meio termo.

02:42

Por quê? Não só nós conseguimos fazer um esclarecimento,

02:48

pedir mais informações, mas

02:53

a questão é que o controle não vai para esse subagente.

02:58

Obrigatoriamente, ele tem que devolver o controle, ou melhor, devolver não,

03:03

o controle continua sempre com o agente operador,

03:09

na verdade, o nosso coordenador.

03:12

Então, sempre volta para ele. Então, isso que é interessante,

03:14

porque nós tínhamos colocado no consultor de faturas que, quando ele terminar,

03:20

ele tem que fazer o transfer to agent. Então, isso aqui se torna redundante.

03:25

Interessante. Então, não preciso colocar aqui.

03:28

E nem tinha colocado em assinaturas, e essa parte,

03:31

por exemplo, de ser cordial e direto,

03:33

não tem necessidade, porque sempre vai voltar agora para o operador da conta.

03:39

Então, vamos fazer a execução do novo subagente.

03:51

Antes disso, na verdade, deixa eu fazer uma mudança.

03:57

Eu vou começar a utilizar o 3.5,

04:00

e nós vamos falar sobre isso daqui a pouco, o 3.5 Flash.

04:05

Ah não, ele já está na verdade presente nos dois, então ótimo.

04:08

Esse aqui pode ficar com 3.1, 3.5, é o modelo melhor. Ok.

04:18

Então agora, até mesmo a questão aqui para a gente poder testar, eu

04:24

vou tirar, vou comentar aquela parte do return aqui do erro,

04:28

mas se você quiser brincar depois,

04:31

você pode ativar, mas eu quero que ele liste as faturas corretamente,

04:35

a assinatura não foi mexida.

04:37

Então eu tenho que... Rodar novamente o exemplo.

04:50

Então estou com o agente correto, vou colocar listar minhas faturas. E

05:01

acredito que aconteceu algum problema. Eu

05:13

cometi algum erro de indentação? Ah,

05:18

não coloquei um comentário aqui embaixo.

05:22

Então não executou de forma correta.

05:25

Então aqui, só

05:27

criar uma nova seção.

05:32

Então listar minhas faturas.

05:37

Agora sim. Então veja. Nós... Estamos

05:46

do operador da conta acessando. Igual o single task parece com o single turn,

05:52

só que com essa extensão de poder pedir mais coisas para o usuário.

05:56

Então, eu acesso como uma ferramenta o subagente.

06:02

Aqui aparece o consultor de faturas, mas não houve a transferência para ele. É só,

06:07

nós estamos dando uma permissão para que ele faça essa interação.

06:11

O controle continua com o operador da conta.

06:14

Aqui na request, nós vamos ver todo o system prompt.

06:21

Aí veja que não tem aquela parte toda dos agentes que você pode transferir.

06:26

Então ele vai formatar o system prompt colocando os nossos agentes.

06:33

Esse aqui é a primeira ferramenta do consultor de

06:35

faturas e depois o consultor de assinaturas.

06:38

Então eles recebem o request como

06:42

parâmetro para poder executar.

06:44

Então liste -me as faturas que foram passadas para ele.

06:46

Então vamos colocar aqui o cliente 123,

06:49

ele

06:52

vai acessar a ferramenta que

06:56

está aqui.

06:57

Então foi

07:00

executada a ferramenta,

07:02

tivemos o resultado retornado para

07:08

o operador da conta e

07:11

a invocação de

07:14

uma ferramenta chamada de finish task.

07:16

Essa aqui é que faz com que esse agente fale que ele terminou de executar,

07:23

acabou, não tem... Mas nada, porque se

07:28

eu tiver uma ferramenta de confirmação, se eu passar aqui para o consultor de assinaturas,

07:33

eu vou ter um ponto de parada que vai pedir mais informações,

07:37

diferente de só pedir o ID do cliente. Então,

07:41

isso aqui é um controle para saber

07:44

de fato que o agente finalizou a tarefa.

07:53

Nós até aqui

07:56

não vai ter, aqui no final.

08:01

Temos o System Prompt e o histórico das tools, mas o que aconteceu? Então,

08:07

liste minhas faturas com a primeira mensagem, aí foi passado,

08:11

teve a invocação da tool e depois a resposta.

08:18

No 3, nós

08:21

conseguimos ver que ele foi invocado,

08:23

teve a chamada para a LLM, a LLM retornou, olha,

08:29

faz aí a chamada de listar faturas.

08:34

Então foi executado, aquela mesma dinâmica.

08:38

E aqui no final nós vamos ter a

08:42

response que

08:46

ele está aqui com o finish task. Então a gente está falando assim, olha,

08:50

terminou a tarefa, porque o agente consultor de faturas passou para ele o resultado,

08:56

então ele fala, invoca aí o finish task, ok,

09:00

aí volta para o operador da conta, ele vai ter acesso à informação.

09:09

Depois acaba retornando essa informação para a LLM.

09:14

Aqui ele fez a chamada, né?

09:17

Passando tudo. E aqui é a formatação. Aqui estão as suas faturas.

09:23

É interessante ver todas essas chamadas que aconteceram.

09:27

Vamos criar aqui uma nova sessão. Agora quero cancelar minha assinatura.

09:36

Então vai lá o controle para o consultor de assinaturas. Preciso informar.

09:42

O ID do cliente,

09:43

então temos aqui o subagente perguntando e

09:47

agora ele pode pedir quantos esclarecimentos forem necessários.

09:52

Ele está pedindo a minha senha, vou colocar a senha secreta.

09:58

Então a gente confirma.

10:03

Então ele vai lá, chama a tool de cancelar assinatura,

10:07

depois passa o finish task com o resultado.

10:12

Então o operador da conta pega e faz a formatação dele.

10:17

Então, nesse caso, foi esse o resultado que aconteceu.

10:25

Em determinado momento, se nós passarmos o mouse aqui,

10:30

nós vamos ver que ele chamou cancelar assinatura, no finalzinho aqui, teve

10:36

o finish task. Com esse gráfico, nós conseguimos acompanhar toda

10:43

a comunicação que aconteceu.

10:46

E por que eu estava atribuindo,

10:49

preocupado em colocar esse modelo 3.5 para os dois?

10:56

coloquei no de assinatura e coloquei no de faturas.

11:03

Pegando o caso de assinaturas que temos uma tool de confirmação.

11:07

Ele pode executar a tool de cancelar e

11:12

a tool de invocar o human in the loop.

11:17

Então vai parar o processamento,

11:19

vai aguardar com que o usuário faça uma nova interação.

11:25

Mas como ele é uma task,

11:31

nesse momento aqui que foi passado, quando ele faz esse pedido,

11:37

acaba indo para a LLM de novo.

11:40

A LLM pode falar assim, olha, finalize, faz um finish task, já terminou,

11:45

que ela considera que foi como se fosse uma resposta, e não.

11:48

Então, essa tool no ADK não pode ser chamada até que eu tenha terminado.

11:53

Então, se eu coloco o modelo 3.1,

11:57

Aumenta-se muito a chance dele finalizar,

12:02

a tarefa quando não era para finalizar. Então,

12:06

utilizar um modelo muito cru, muito básico, nós

12:11

podemos, apesar de que o ChatGPT é um modelo muito simples,

12:14

mas o 3.5 é bem melhor e não é o Lite. O Lite ainda é um modelo bem mais básico,

12:21

então nós temos que ter atenção também à escolha dos modelos.

12:25

É importante que a gente crie os nossos agentes, faça os nossos testes.

12:30

Antes de só simplesmente colocar o modelo e sair colocando em produção.

12:37

Essa é mais uma dica que a gente adquire aqui no curso.

12:40

Então, nesse caso, nós colocamos o modelo task, o system prompt fica mais básico.

12:48

Nós até conseguimos ver o system prompt, vamos pegar aqui o caso do... quando ele

12:55

vai mudar aqui, exatamente

12:58

do que a gente está falando. Ele está acrescentando no system prompt,

13:03

olha... Não finalize a task de forma prematura.

13:06

Use as ferramentas disponíveis para completar todos os aspectos delegados.

13:14

Depois, se a tarefa não está clara, pergunte ao usuário para

13:20

que ele possa interagir. Depois que tudo estiver completo, finalize a task.

13:27

Isso é embutido no System Prompt. Então, nós vamos vendo aqui cada vez mais que...

13:33

A ideia abstrata vai se mudando, o sistema imprime e criando

13:36

esse controle para que nós criamos essa aplicação inteligente. No final das contas,

13:40

ela usa o cérebro da LLM para poder fazer todas

13:44

as tarefas e pensar em cada etapa do processo.

## Resumo IA

[RESUMO_IA]