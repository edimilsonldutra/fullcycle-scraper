Módulo: Desenvolvimento de Agentes com IA\
Aula: [Agenttool](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18263)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar do Agent Tool,

00:02

que é uma outra abordagem, uma outra alternativa ao Single Churn.

00:07

Nós vimos que o agente acaba se tornando uma tool,

00:11

ele é invocado sem a transferência de controle para ele,

00:16

ele executa alguma coisa e retorna um resultado.

00:19

A questão é que, quando nós utilizamos o Single Churn, tudo

00:25

o que está acontecendo é transparente na mesma sessão.

00:30

Que nós estamos trabalhando. Nós não chegamos ainda nesse conceito de sessão,

00:34

vamos aprender daqui a pouco. Mas aqui em cima nós podemos criar uma sessão,

00:39

você já fez isso nessas ferramentas como ChatGPT, Cloud AI,

00:44

você sempre cria uma nova sessão e vai interagindo até que você

00:48

Resolva o seu problema ou até que não faça mais sentido.

00:52

Então, com o SQL Churn, tudo fica registrado,

00:55

fica presente, fica auditável, fica transparente.

00:58

Mas às vezes nós queremos utilizar o agente

01:03

só para poder executar alguma coisa e retornar,

01:06

não queremos que ele tenha contato com o usuário,

01:10

mas queremos deixá-lo de forma isolada.

01:12

Aí que entra esse Agent Tool. Então aqui eu

01:19

criei um novo exemplo copiando o que nós já tínhamos feito.

01:24

Então, nós temos aqui embaixo o

01:28

Acme Status Subagent, que está declarado com o Single Churn,

01:32

nós vamos remover essa opção e

01:36

nós vamos englobar o Agent Tool em volta dele.

01:41

Porém, veja só,

01:43

isso aqui transforma o agente numa tool

01:50

no mais puro do conceito. Então,

01:54

nós declaramos isso em tools e não em agents. Aí

02:03

vamos importar aqui em cima. O Agent Tool.

02:09

Ok. Então, nós vamos fazer o ADK Web, depois

02:16

que ele fizer o source do env.

02:21

Então, aqui vai ser o Agent Tool. Pronto.

02:32

Então, agora vamos recarregar essa página.

02:35

Nós já temos uma memória fotográfica de como ficou a execução da aula anterior.

02:43

Ótimo, então vamos colocar o List Minhas Faturas. Ele vai acabar dando um erro,

02:49

vai cair aqui no Acme Status.

02:51

Nós já vimos logo de cara que o Acme Status não

03:00

transparece a tool que ele vai usar.

03:04

Nós estamos transformando o agente em uma tool, mas ele também tem uma tool interna,

03:09

que é a verificação do status. Então, isso já não aparece. Ele até mostra o Acme Status,

03:17

como se fosse, na verdade, ele é uma tool agora do agente coordenador.

03:23

Ele é a mesma coisa que um Cancelar Assinatura, Listar Faturas.

03:29

Aqui nós podemos ver nessa transferência como está sendo a chamada.

03:36

Então, você é o atendente, aí

03:41

estamos, aqui até poderia, seria correto mudar para ele usar

03:47

a tool de Acme Status, mas nós podemos fazer um teste também.

03:51

Então, na lista de subagents, ele

03:55

não está aparecendo, e antes também não aparecia, quando é Single Churn.

03:59

Então, nós temos o

04:02

Transfer to Agent e o Acme Status.

04:06

A forma como ele é abordado não muda,

04:11

é só a forma como ele vai ser executado. Então, vamos dar continuidade.

04:18

Colocando o cliente 123.

04:26

Pronto, então nós vemos aqui que ele fez a execução.

04:31

E quem

04:35

mantém o controle da conversa é o operador da conta.

04:39

Nós não vemos que há um novo agente.

04:43

Então há essa privação.

04:46

Quando esse agente que vai ser executado como um ator invocado, ele

04:53

cria uma sessão separada para ele. Diferente da sessão que nós estamos.

05:01

Então isso faz com que ele meio que rode numa caixa preta.

05:04

Então numa situação em que eu quero

05:07

executar, só pegar o resultado,

05:11

não me interessa o que está acontecendo lá dentro,

05:15

eu não quero que essa execução faça parte da minha sessão,

05:19

vamos supor que eu esteja trabalhando com dados sensíveis,

05:21

nós podemos utilizar o agent tool.

05:24

Aqui ele vai ser... literalmente descartado, não vai fazer,

05:28

se eu recarregar de novo essa sessão, nós

05:33

não temos detalhes do que aconteceu dentro

05:38

do agente que é um agent tool.

05:41

Então nós teríamos que corrigir aqui,

05:43

quando algum subagente retornar um erro do sistema, use a

05:49

tool AcmeStatus. O modelo obviamente vai improvisar,

05:55

mas não devemos deixar chance para... Ambiguidade.

06:02

Então nós podemos fazer essa mistura,

06:04

não tem problema nenhum de ter modelo modeChat,

06:09

single churn, coagent2. A questão é a escolha.

06:14

Nesse caso do status, não

06:17

tem necessidade, a princípio,

06:20

eu vejo que não tem necessidade de mantermos detalhes sobre essa execução,

06:25

eu só quero verificar o status dado o problema que aconteceu.

06:30

Então é algo muito simples.

06:33

Isso vai até economizar mais contexto.

06:38

Economizando mais contexto, estamos economizando dinheiro.

06:44

Então ele não é um mode, mas ele entra sempre em confronto com o single churn.

06:51

Nós já entendemos essa diferença. Aqui nós vamos ter a mesma sessão,

06:55

rastreabilidade,

06:59

transparência, enfim.

07:02

Às vezes nós podemos querer isso, às vezes não.

07:04

Você vai decidir de acordo com o contexto

07:08

do que vai ser executado no seu agente.

## Resumo IA

[RESUMO_IA]