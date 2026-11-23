Módulo: Desenvolvimento de Agentes com IA\
Aula: [Criando tool de registrar o ticket](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18559)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos criar a ferramenta que vai registrar o ticket,

00:04

assim como nós aprendemos que qualquer operação externa deve ser feita,

00:10

na verdade é uma das opções que nós temos,

00:12

que é a ferramenta. Então, eu vou criar o registrar, vou

00:17

colocar em português, registrar ticket.

00:22

E aí eu poderia pedir para que fosse passada a mensagem que vai ficar nesse ticket, mas...

00:29

Como nós vamos pegar o que o usuário está enviando?

00:33

Através do tool context nós conseguimos extrair essa informação.

00:41

Então vamos importar de

00:46

google.adk.tools import tool context. Pronto.

00:56

Então a ideia, vou

01:02

até deixar essa

01:05

sugestão aqui da ideia, ela vai registrar um ticket, tem o tool context.

01:12

e vai retornar um dicionário com

01:17

o status do registro do ticket.

01:24

Então, o que nós vamos fazer aqui, logo de cara, é pegar a mensagem do usuário.

01:30

Vamos ter o userMessage.

01:34

De toolContext, nós conseguimos pegar o userContent,

01:40

que é a mensagem que o usuário enviou,

01:43

e ele está segmentado em partes, como nós já vimos.

01:46

Esse userContent pode estar em partes, que podem ser null,

01:50

dentro da parte posso ter o texto que é null.

01:53

Então nós temos que tomar cuidado com isso.

01:56

E eu prefiro criar um método adicional de mensagem ao usuário.

02:02

Então recebemos aqui o conteúdo, que é do tipo content.

02:08

Aí de google.gen.ai.types importamos o content.

02:15

Então, se verificarmos que o conteúdo não existe, ou se...

02:21

conteúdo.parts não existe, vai ser vazio.

02:26

Não tem nada para fazer. Agora, caso contrário, ele

02:32

até está sugerindo o

02:37

que eu vou fazer, nós temos que pensar o que eu quero pegar dessa mensagem.

02:42

A ideia aqui é pegar tudo, porque o usuário pode começar assim, com um olá, aí

02:48

ele tem a resposta, você pode listar os tickets, criar os tickets,

02:52

aí ele fala assim, eu quero criar um ticket.

02:55

Aí depois ele manda a mensagem.

02:59

O LLM vai pedir para ele colocar qual é o assunto do ticket.

03:04

Então são três mensagens. Eu quero pegar somente a última, quero pegar todas.

03:09

A ideia aqui é pegar todas, mas isso depende do que você está fazendo.

03:12

Então eu vou usar um artifício de usar o

03:16

barra n com o join para poder concatenar tudo. Então veja só.

03:24

Nessa estrutura de repetição, para cada parte que tiver em partes,

03:28

se tiver parte.text, porque ele pode ser None, nós vamos incluir,

03:33

depois o join faz com que cada pedacinho do array seja juntado com o barra n,

03:40

que aí fica fácil depois para poder mostrar.

03:43

Então pronto, temos aqui a nossa função.

03:49

Então passamos o userContent, que pode ser None, então aqui também.

03:56

Vai ser None e retorna uma string.

04:01

Mas se o userMessage não existir, é

04:09

algo que é uma falha grave aqui.

04:13

Tem que ter esse userMessage de alguma forma. Então, eu não quero nem retornar um

04:21

dicionário com um erro. Eu quero retornar um erro que

04:27

aconteceu alguma coisa. É porque se ele não pediu a mensagem,

04:31

se a mensagem não veio...

04:33

Não é nem o ponto de continuar esse processo, tem alguma coisa bem errada.

04:37

Então depende da forma como nós queremos lidar com isso.

04:40

Nós já vimos que nós poderíamos retornar um dicionário sendo mais permissivos,

04:45

mas aqui eu considero que é um erro grave.

04:50

Então quando tiver essa mensagem de usuário, agora

04:57

vem a hora da classificação.

05:00

A ideia aqui no System Prompt é eu classifico, depois

05:06

registro.

05:09

Então, ao fazer a classificação, inclusive eu fiz uma mudança antes aqui da aula,

05:16

para poder colocar essa key sobre uma constante,

05:20

porque aí fica fácil para que a gente possa trabalhar.

05:23

Tem esse output key com output schema, então tem que verificar se ele existe também.

05:34

Então nós vamos importar esse

05:38

output key e

05:43

até mesmo...

05:45

Antes de verificar essa mensagem,

05:47

eu quero verificar se eu tenho o classifier output key no contexto,

05:53

melhor, no state.

05:57

Porque se eu não tiver,

06:01

aqui eu posso ser permissivo.

06:05

Nós podemos falar, olha, o ticket não foi classificado,

06:08

eu vou classificar antes de registrá -lo.

06:10

Essa instrução nós não adicionamos lá no system prompt,

06:13

mas nós vamos adicionar. Então aqui é diferente do de baixo,

06:17

que nós estamos preferindo lançar um erro.

06:19

Aqui nós lançamos esse dicionário.

06:25

Agora, como que eu vou lidar com esse state? Porque

06:31

eu tenho do context state passando essa aqui,

06:36

vai ser um dicionário,

06:38

mas eu posso garantir que ele seja uma instância do próprio ticket output aqui,

06:45

que é uma classe do Python, que é todo bonitinho.

06:48

E eu não posso confiar também que... isso às vezes pode ter um formato inválido.

06:54

Então, nós conseguimos criar um objeto desse tipo usando

07:00

o ticket classifier output ponto

07:03

model validate passando o dicionário.

07:08

Então, ele vai validar e cria

07:12

uma instância do próprio ticket classifier output.

07:15

Se isso aqui for inválido, ele vai lançar um erro. Então, aqui eu tenho certeza...

07:21

de estar trabalhando com a classificação. Então,

07:24

usar esses outputs e esquemas quando cabe,

07:29

quando é necessário, vai ser muito bom, porque tem outros momentos,

07:34

o ADK vai forçar a validação, já vai te dar ali o objeto.

07:39

Não aqui, ele não vai fazer isso,

07:40

mas temos outras áreas que ele até te dá o objeto já pronto.

07:45

Então, depois de termos a classificação, temos a mensagem do usuário.

07:51

Nós vamos chamar aqui um await repo,

07:53

lá do banco de dados, create ticket,

07:56

Passando a instância de Ticket Model. Ela

08:04

já foi importada aqui em cima.

08:07

Na hora que eu dou um tab aqui, veio um monte de coisas que não eram necessárias.

08:18

Agora, se não temos erro, provavelmente ele vai importar ou não.

08:22

Nós vamos passar o Customer ID

08:26

que nós pegamos do context. userId.

08:33

Temos a mensagem do userMessage, e a classificação,

08:37

que a gente tem que passar um ClassificationModel, que é uma subclasse, como

08:45

ela é idêntica ao TicketClassifierOutput,

08:49

nós podemos usar esse artifício aqui no Python,

08:52

de classificationModelDump.

08:54

Esse ModelDump do Pydantic vai converter de novo para adicionar, e

09:02

como eu tenho que passar parâmetros,

09:04

esses dois asteriscos fazem com que eu tenha a

09:08

conversão deles em parâmetros nomeados. Então ele vai lá, coloca a categoria,

09:12

coloca o valor, depois coloca o justification e assim vai.

09:18

Pronto. São essas informações que nós precisamos,

09:21

porque por padrão o ticket vai ser criado de forma pendente,

09:25

porque ele não foi atendido ainda. Agora nós temos que importar o restante do

09:34

que é necessário.

09:39

Ah, coloquei na verdade errado, né? TicketModel. Pronto.

09:49

O erro aqui provavelmente vai sumir, mas nós temos que tornar a nossa tool uma coorte.

10:04

Aí ele vai demorar um pouquinho para sumir o erro. Vamos colocar

10:10

aqui o ticketCreated e aí nós retornamos um

10:17

status de sucesso e o ticket criado.

10:23

Trabalhar nesse padrão aqui é interessante, né? Não precisamos...

10:27

Colocar nenhuma mensagem não é escopo da tool, ela só vai registrar.

10:34

Então, podemos trabalhar sempre com status de erro e mensagem.

10:39

A mensagem não seria obrigatória aqui nesse caso.

10:43

Então, pronto.

10:45

Vamos agora adicionar em tools o

10:53

Registrar Ticket, que é a nossa tool.

10:56

Aí nós precisamos adicionar um System Prompt dizendo

10:59

esse processo de criação do ticket.

11:01

Então, se o usuário pedir para criar um ticket,

11:04

pergunte qual é a mensagem do ticket e em seguida ative

11:08

o processo de classificação do ticket e proceda com o registro.

11:12

Então, ele precisa classificar e depois registrar.

11:16

Se a gente quisesse até dar aqui regras,

11:19

você não pode registrar sem fazer a classificação,

11:22

seria também um reforço interessante.

11:26

Então, vamos lá. Eu

11:30

vou enviar um olá, como nós tínhamos feito anteriormente. Em

11:40

algum lugar, eu coloquei o import errado.

11:50

Qual lugar que eu estou utilizando? Aqui.

12:07

Ele importou de novo no mesmo lugar na hora que eu fui digitar alguma coisa.

12:14

Então, vamos recarregar com uma nova seção.

12:27

Então, olá.

12:30

Como posso te ajudar hoje?

12:33

Quero... criar um novo ticket. Com

12:39

Certeza, a mensagem do ticket tem

12:44

um erro 500 na integração do GitHub.

12:51

Isso porque essa era uma mensagem muito genérica,

12:54

por isso que aquele reforço no System

12:58

.Prompt iria permitir que ele pegasse mais detalhes.

13:02

Então, ele fez a classificação, o usuário relata, tem

13:08

um erro 500, é um bug.

13:11

O Confidence é 100%, aí ele vai registrar o ticket e aqui está

13:20

o nosso resultado.

13:24

E aí nós poderíamos até colocar uma mensagem de como que ele deveria retornar isso,

13:31

colocar a classificação talvez não seria interessante,

13:34

só o ID do ticket que seria, mas

13:38

algumas instruções, obviamente, de como que essa mensagem vai ser trabalhada,

13:44

vai ser notificada por e-mail, enfim.

13:46

Então, conseguimos fazer isso adicionando mais algumas coisas que nós...

13:51

juntando, na verdade,

13:53

todo o conhecimento que nós adquirimos aqui até o momento.

13:56

E agora a nossa ferramenta ficou bem bacana.

13:59

E já fizemos esse registro do ticket.

## Resumo IA

[RESUMO_IA]