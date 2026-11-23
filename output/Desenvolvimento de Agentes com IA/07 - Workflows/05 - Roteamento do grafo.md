Módulo: Desenvolvimento de Agentes com IA\
Aula: [Roteamento do grafo](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18569)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos dar continuidade ao conceito de Node e também de Function Code.

00:05

Para aplicar uma melhoria e também aprender um novo conceito também com workflows.

00:10

Nós temos esse nó de triagem do ticket,

00:14

que consulta o ticket, vê se ele é fora do escopo,

00:18

faz uma definição no ticket ou até mesmo se ele não foi encontrado,

00:25

retorna uma mensagem.

00:27

Então nós já podemos ver aqui que essa triagem ainda não terminou,

00:33

nós vamos ter mais códigos sendo adicionados aqui.

00:36

Daqui a pouco essa triagem pode ficar tão

00:39

grande que ela incorpora muita responsabilidade,

00:42

ficando difícil de testar, de manter, de acrescentar novos códigos.

00:47

Essa parte, por exemplo, do Out of Scope, é responsabilidade da triagem? Não.

00:52

Isso aqui é uma definição própria quando o ticket é fora de escopo.

00:57

Deveria ficar em um outro lugar. Então aqui mais uma vez,

01:01

nós não precisamos colocar em agente.

01:05

Nós podemos continuar trabalhando de forma determinística.

01:09

Para isso nós podemos então diluir isso em um outro nó.

01:14

Então eu vou usar barra node, já

01:17

vou colocar o async de uma vez, def,

01:20

e aí nós devemos sempre, é bom que a gente sempre...

01:25

coloque um nome sugestivo.

01:26

A própria IA já está identificando que eu vou

01:29

fazer um handle Out of Scope Ticket Node,

01:33

seria um ótimo nome. Então sempre coloque um verbo para o que você vai fazer.

01:38

A gente está fazendo uma triagem,

01:40

eu estou lidando com isso, mas aqui eu vou colocar um nome melhor,

01:45

um ticket, ou melhor, um Refuse Ticket Node.

01:51

Então aqui eu recebo o contexto.

01:55

E na verdade ele já fez tudo. Vamos fazer tudo logo de cara.

01:59

Como nós vamos precisar aqui do Ticket ID,

02:02

porque nós vamos precisar recuperar o ticket aqui mais uma vez.

02:05

O state também é aceito como parâmetro no

02:10

Function Code. Então eu não preciso pegar ele dessa forma.

02:14

Você decide como você pegar.

02:17

Então eu preciso desse trecho aqui, porque senão eu

02:30

não tenho garantia que aqui eu tenho... um Ticket Model.

02:34

Eu posso ter None on Ticket.

02:38

Pode acontecer que alguém faça a exclusão.

02:41

Então, é uma segurança que nós temos. Então, colocamos aqui a mesma mensagem e,

02:46

obviamente, à medida que esse código vai crescendo,

02:47

essas mensagens podem ser colocadas em constantes,

02:52

nós podemos melhorar esse código. Então, vem esse trecho de

03:00

código, que é o mesmo de cima. Só precisa estar alinhado,

03:06

porque senão o Python não vai deixar

03:10

que a gente execute corretamente o código.

03:12

Então, aqui não preocupo se é um Out of Scope, eu sei que já é.

03:17

Então, veja, mais uma vez a gente está consultando aqui e aqui também.

03:21

E aí, nesse caso, não adiantaria se a gente quisesse colocar,

03:27

por exemplo, um contexto de state colocando o ticket.

03:31

Isso aqui até nos ajudaria a não ter que consultar novamente.

03:35

Mas lembra do que eu falei do state lá atrás?

03:38

Em relação a que a gente tenha que garantir que isso seja serializável ou

03:47

deserializável

03:52

Facilmente, colocar um objeto mais complexo como esse, de

03:59

um RM, pode nos trazer surpresas.

04:03

E até mesmo com um RM qualquer,

04:06

quando a gente faz um get duas vezes logo em seguida,

04:09

ele armazena isso em memória. Então, isso não é um problema.

04:15

Então, você pode usar o state.

04:18

Caso você veja que o seu objeto não vai

04:22

trazer nenhum problema se ele for precisar ser deserializado novamente.

04:27

Mas tome cuidado com isso. Aqui eu vou usar esse artifício do SQLAlchemy,

04:30

que nem consulta ele vai fazer no banco de dados.

04:33

E aí você pode ativar cache, enfim. A gente entraria em outras searas,

04:37

mas aqui nós já vemos que pode acontecer de você ter que recuperar a informação,

04:43

sendo que você não escolheu.

04:46

Transmiti-la através do state. Então são várias formas da gente trabalhar.

04:51

Mas agora a questão é,

04:53

se eu ver que é out of scope, o

04:59

que eu vou fazer? Como que eu vou conectar? Eu vou chamar esse node diretamente?

05:03

Não, nós não vamos chamá-lo diretamente.

05:06

Nós só vamos produzir um evento em que na actions,

05:11

vamos passar um event actions e aqui em cima.

05:17

Temos que importar de

05:21

eventos. A gente ainda não colocou. Então,

05:24

google.adk.events. Import event actions.

05:33

Nesse event actions, nós temos muitas informações que podem ser passadas.

05:37

Uma leva de informações.

05:39

Mas tem informação chamada de route.

05:42

E aqui eu vou colocar refuse.

05:48

É um nome que vai permitir rotear através do nó no nosso workflow.

05:57

Então, quando

06:01

esse

06:03

nó de triagem for executado, eu

06:08

posso passar um dicionário falando assim, se

06:13

for refuse, vai ser refuse ticket node.

06:20

Então, olha só que legal isso.

06:25

Nós estamos criando um evento que

06:28

vai causar um redirecionamento no grafo.

06:33

Na verdade é só o caminho. Então nós podemos colocar assim que nós

06:41

temos a

06:48

triagem e

06:50

agora temos uma ramificação, um

06:57

refuse. Então, da triagem vem para cá, mas

07:04

se não for triagem vai para outro lugar.

07:07

Então, através do... nós criamos esse redirecionamento.

07:12

Agora, a nossa triagem fica exatamente só para fazer a

07:17

triagem ou para já quebrar o comportamento logo de cara,

07:21

permitindo que a gente adicione outras coisas.

07:24

Então, temos mais um nó determinístico. Pronto.

07:31

Vamos fazer o mesmo sistema de antes. Na verdade,

07:36

aqui eu saí. Já vou deixar o SQLite aqui.

07:43

Fiz dois Ctrl -C, não deveria ter feito, mas ele tinha quebrado já o servidor.

07:49

Então, voltando para o Receptionist,

07:53

temos esse aqui que eu quero falar de novela.

07:57

Eu não vou reusar o ticket, eu tenho que criar um novo.

08:08

Então, chamou o ticket classifier, registrou o ticket. Ok, então agora vamos pegar o ticket resolution,

08:15

passar o state de

08:19

ticket ID e esse valor.

08:25

e vamos passar um A.

08:28

Então, agora,

08:31

nosso grafo já ficou um pouquinho mais complexo.

08:35

Do start, ele foi para a triagem,

08:38

da triagem foi para o nó function code de recusa,

08:44

e aí teve o end.

08:46

E aqui teve, obviamente, a operação do banco de dados,

08:48

então aqui nós ficaríamos mais livres para fazer notificação e etc.

08:53

Ou até mesmo, pense,

08:56

Poderíamos nem ficar preocupando com notificação aqui do Refuge,

09:01

poderíamos ter um Notification.

09:03

Vamos pensar que, a não ser que aconteça algum problema muito grave,

09:08

nós vamos querer notificar o usuário. Então,

09:13

poderíamos considerar que a mensagem que vamos

09:16

registrar ali como resultado é uma notificação,

09:20

envio de e -mail, WhatsApp, qualquer coisa assim.

09:23

Seria também essas notificações agregadas.

09:27

Então vai de acordo com o seu entendimento.

09:29

Mas aqui ele mostra que a triagem não tem um default.

09:37

Porque uma vez que eu crio essa ramificação, como ela está presente aqui,

09:45

e se acontecer, nós não fizemos ainda, mas se acontecer...

09:53

de não entrar nesse if, ele vai ficar a ver navios. Então,

09:57

ele está colocando esse default porque nós conseguimos criar aqui um default também.

10:04

Aqui é o roteamento, chave valor. Então, eu consigo colocar um default. Ah,

10:09

o default vai para tal lugar. Mas, obviamente,

10:12

nós não estamos preocupados com isso no momento.

10:16

Porque, no final das contas, vai sempre para algum lugar.

10:18

Se quisermos usar o default,

10:20

importamos o default route, que é apenas... uma string

10:26

default declaramos aqui

10:31

default route

10:36

aqui poderia ser um xpto node

10:42

ou um agente ou

10:47

um human input ou

10:53

uma tool nós já falamos que o node pode ser qualquer coisa então

10:59

você pode decidir qualquer coisa aqui, mas nós não vamos

11:03

fazer nada aqui no momento.

11:04

Então tivemos aqui o nosso roteamento e criação de mais um Node,

11:11

que é o de Refuge.

11:13

A ideia é sempre mantermos organizados,

11:16

Que o Node execute um bloco específico,

11:21

As mesmas boas práticas de funções menores, mais enxutas.

11:28

Vai ser muito bom para esse contexto. No final das contas,

11:31

Nosso processo até o momento é totalmente síncrono, não teve nenhum agente,

11:36

Não tem nada que a gente consiga pegar de LLM,

11:40

Porque nós estamos apenas produzindo um gráfico até o momento.

## Resumo IA

[RESUMO_IA]