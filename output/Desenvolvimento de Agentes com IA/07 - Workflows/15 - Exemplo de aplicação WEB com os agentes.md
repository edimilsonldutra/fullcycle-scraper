Módulo: Desenvolvimento de Agentes com IA\
Aula: [Exemplo de aplicação WEB com os agentes](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18579)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos fazer a capa dos nossos agentes de IA,

00:04

permitindo que nós iniciemos um ticket através

00:09

da web e também manipulemos o ticket resolution.

00:12

Nós vamos ter um web .py, como nós já tínhamos feito anteriormente,

00:17

para que nós possamos brincar com o nosso exemplo.

00:20

Mas aqui eu quero exercitar o raciocínio de como

00:23

que a gente poderia organizar esse agente numa aplicação web.

00:28

sendo que o ticket resolution não ficaria no endpoint.

00:32

Na verdade, somente uma parte dele.

00:35

Porque eu poderia criar um barra API barra tickets,

00:39

que obviamente vai fazendo aqui um post.

00:43

Nós vamos criar tickets.

00:47

Só que a parte do resolution não

00:51

ficaria numa... Essa primeira parte não ficaria numa API,

00:55

porque depois que eu criasse o ticket,

00:57

a gente poderia publicar... um evento, um evento não do ADK,

01:01

publicar um evento numa fila, e

01:06

aí ter um consumer .py, em que nós consumimos a mensagem,

01:11

e a mensagem vai para o runner, acessando o workflow do ticket resolution.

01:17

A ideia seria essa. Mas como nós temos o linear,

01:22

então poderíamos ter um post

01:26

barra API,

01:29

barra tickets mais o ticket ID,

01:34

barra approval ou aprovação, vamos colocar dessa forma.

01:44

Então, imaginando que você vai configurar o linear ou

01:47

qualquer ferramenta para fazer o webhook de aprovação,

01:50

quando tem aquele refund confirmation,

01:52

iria fazer uma chamada para cá, você iria pegar os dados,

01:57

fazer o runner retomar de onde parou.

02:04

Seria isso. E

02:08

pronto, aqui nós teríamos a nossa aplicação agêntica. Tudo é baseado nos agentes.

02:14

Mas eu não quero focar nesses pontos ou em ferramentas,

02:18

mas aqui você pode fazer essa implementação com base com

02:22

o que nós temos aqui no Web API.

02:25

Então, tenho aqui o Web API que nós vamos ver daqui a pouco.

02:29

Eu quero me concentrar em mostrar como ficou os endpoints.

02:34

Eu fiz também algumas modificações no nodes .py.

02:39

Por exemplo, quando nós vamos retornar aquele request input,

02:43

nós podemos já mudar o ID do ticket.

02:49

Inclusive, aqui, se não ticket, o

02:55

evento é ticket não encontrado. Eu não precisaria disso

03:00

aqui. Ok, eu coloco um status nele. Isso aqui já existia antes.

03:04

Ele estava com a waiting approval.

03:07

Esperando a aprovação.

03:08

que serve para que você faça um controle em

03:11

todo o workflow que está sendo desempenhado.

03:15

Também aqui na triagem do Refound, eu

03:22

acrescentei aqui onde estava o Pass, agora tem a

03:28

geração do evento com o Randolph, e também quando ele

03:33

está no Not Found, o Invalid ou o Block Refound,

03:36

Que passa ali do teto, passa dos 200...

03:41

Reais, 200 dólares.

03:43

Antes não tinha nada aqui, tinha um PES também. Então,

03:47

por isso que ele passava por esses dois IFs, mesmo se pudesse entrar,

03:53

ele ia continuando. E a gente conseguiu usar o C204 para fazer o teste,

03:59

porque o reestorno dele é 480.

04:03

Então, 480 é block found, deveria cair aqui.

04:07

Porque aqui é somente quando a gente está na faixa de 50 a 200. Dado,

04:12

o intervalo que a gente está usando. Então,

04:14

na hora que você for testar essa questão do aprovação com a confirmação,

04:20

teste com C207. Isso já está ali, mas já estou falando sobre isso.

04:27

Então, aqui no API Tickets,

04:29

nós vamos ver que os endpoints parecem com o que nós já tínhamos visto,

04:33

mas eles carregam mais informações,

04:36

eles têm mais código, como nós vamos ver daqui a pouco no web.py.

04:40

Então, eu tenho aqui criar sessão, as mensagens.

04:44

As coisas estão via variáveis, porque aí você pode mudar conforme você quer.

04:48

Eu já estou rodando também o projeto.

04:51

Vou até rodar novamente. Ele já cria o banco de dados de forma automática.

04:57

Vamos criar a sessão,

04:58

que é o que nós já tínhamos feito lá atrás, para ser a primeira coisa,

05:02

mas nós poderíamos até fazer um endpoint diferente na

05:04

hora que eu estou enviando a mensagem.

05:06

Já poderia abrir uma sessão. Então,

05:08

tem o C207 como Customer e o 7ID. Não preciso anotar nada.

05:13

Porque tudo vai via variáveis, então nós podemos já criar o ticket.

05:17

Ele vai aqui com a mensagem que tem o ajuste de 120 dólares na

05:24

fatura de junho, solicito estou.

05:26

Então, ele vai mostrar o ticket ID que é armazenado nessa

05:32

variável, então

05:34

nós podemos já fazer a resolução.

05:36

Agora, o que vai causar ansiedade é que, passando muito tempo no ADK Web,

05:41

nós não estamos vendo o que está acontecendo por trás. E, obviamente, tem o delay.

05:46

Esses são os novos desafios que nós temos para essas aplicações.

05:52

Tem o delay. Quanto mais complexo o agente,

05:55

maior vai ser o delay. Então, ele mostra essa

06:01

formatação aqui, mas, obviamente, não é o agente que está retornando isso.

06:04

Do resultado do agente,

06:06

estamos formatando esses dados. Então, vem o ticket ID, esse é o item approval,

06:14

que ficou justamente como o status aqui

06:20

antes de fazer o input, mas

06:23

na verdade aqui eu só estou colocando, deixando claro.

06:27

E na aprovação pendente, temos o ID da interrupção,

06:32

que faz com que a gente faça a retomada. Na verdade, nem precisa ficar passando

06:40

isso aqui na request para a API.

06:43

Se a gente tentasse retomar, seria só rastrear os eventos,

06:47

e ver ali qual foi o último evento e se ele tem essa interrupção,

06:53

enfim, o que aconteceu e a gente retoma de onde parou.

06:56

E a mensagem que vem, justamente, como nós tínhamos determinado. Então,

07:00

aprovação humana para reestorno e etc. Então,

07:03

Simplesmente, nós podemos fazer um reembolso

07:06

mandando o confirmed igual a true, vai ser passado para a gente e tudo aconteceu.

07:12

Então, o que nós temos aqui nesse web.py...

07:16

Eu deixei alguns comentários para ficar fácil que você entenda todo o processo.

07:20

Tem algumas constantes para definir banco de dados,

07:23

se você quiser trocar para um Postgres,

07:25

quiser deixar com o SQLite que é o padrão, tudo bem.

07:31

Temos a delimitação do SessionService, dado o que você escolher como banco de dados.

07:37

O app do Resolution, a

07:40

definição dele que nós vamos utilizá-lo.

07:43

No caso, o app do Ticket to Reception,

07:45

a gente não precisa porque já está dentro do Agents.py, como nós já vimos definido.

07:50

Então, aqui está o runner do Reception, que pega o app dele,

07:53

mais o SessionService, e o runner do Resolution.

07:57

Essa função,

07:58

ela entra para poder iniciar o banco de dados com um lifespan no FastAPI.

08:04

Então, ele inicia e já roda isso.

08:07

Nós não precisamos ficar rodando vários comandos.

08:10

Aí tem alguns helpers que nós vamos ver ao longo do processo,

08:14

mas até aqui a parte da criação da sessão,

08:16

como nós já tínhamos visto anteriormente, nada demais, passa-se o Customer ID,

08:21

ele vai lá e cria e devolve a sessão. Na parte da mensagem,

08:25

recebemos as três informações, Session ID, Customer ID e Mensagem,

08:31

então criamos a sessão com as informações,

08:33

se ela não existe, 404, e passamos o conteúdo, que vai aqui para o Runner.

08:41

Então, na hora da resposta,

08:42

aqui nós temos um código diferente que nós não tínhamos visto e que vai o

08:47

macete de que nós podemos pegar esses eventos

08:50

e manipulá-los para extrair informações relevantes.

08:54

Porque quando o runner começa a rodar, seria

08:58

interessante que eu tivesse o Ticket ID.

09:00

Eu poderia pegar o evento final e tentar fazer alguma expressão regex,

09:07

uma expressão angular, para poder extrair o ID do ticket.

09:09

ele acaba sendo retornado aqui, mas veja só, o

09:13

ID do ticket é capturado dessa forma. Tem esse helper, que

09:19

é o ticket registrado, então eu passo o evento,

09:21

vejo se o evento é uma function response,

09:25

ou seja, é uma resposta lá da ferramenta.

09:30

E eu vejo se ele é da ferramenta registrar ticket, isso aqui é uma constante.

09:37

Então, se for function response e for essa ferramenta,

09:41

então isso aqui não quebra se eu adicionar outras ferramentas no agente, eu pego a resposta,

09:47

vejo se o status é sucesso e o Ticket ID, porque quando nós temos aqui

09:56

o agente, vamos pegar a ferramenta, nós temos o status e

10:03

o Ticket ID. Então, veja essa forma de extrair.

10:08

Então, esse ponto de utilizar esses helpers,

10:11

a forma como você organiza para extrair essas informações é interessante.

10:14

Olha como ficou fácil de ler.

10:17

Porque quando você tem vários eventos acontecendo,

10:19

pode ser que você queira extrair várias coisas,

10:22

e aí você vai colocando muitos ifs.

10:25

Ficando difícil de ler, até o agente se complicar,

10:30

Se você estiver utilizando um agente de IA para desenvolver.

10:33

Então extraímos o ticket ID,

10:34

Depois, se for evento final, helper de texto para pegar as partes,

10:39

E aí devolvemos a resposta, que

10:44

É o que está aqui. Então, na hora de rodar a resolução.

10:48

Então, tem um Ticket ID Resolução,

10:51

Recebemos o Ticket ID, consulta, se não existir, 404.

10:56

Aí nós vamos tentar pegar a sessão, porque nós podemos querer retomar,

11:02

Às vezes pode acontecer um erro,

11:04

E aí enviamos uma mensagem novamente,

11:08

Igual quando você está manipulando um ChatGPT ou qualquer coisa assim.

11:13

Ela pode não existir, se ela não existir...

11:16

Mas nós estamos criando a sessão com o próprio Ticket ID,

11:20

Porque aí fica fácil recapturá-la.

11:24

Posso passar qualquer ID que eu quiser.

11:27

Mas aí nós precisamos passar o State também.

11:31

E aqui tem a definição de conteúdo,

11:33

E esse ponto também é importante, porque o conteúdo,

11:37

Na hora que você passa lá para o Run Async, ele nem é obrigatório, o New Message.

11:44

Se você olhar ali, ele pode receber None.

11:48

Entretanto, como nós temos um workflow e os agentes vão ser single churn,

11:54

Tem aquela questão de você pegar o último evento e ir voltando até você

12:01

Pegar o anterior que não é da autoria do próprio agente que está manipulando.

12:07

Então, nós temos que tomar cuidado porque aqui é bom passar um conteúdo.

12:13

A gente usou bastante ele durante...

12:18

Os nossos testes passando um A.

12:21

A gente poderia passar qualquer coisa.

12:23

Então, eu coloquei como resolva, como algo mais formal,

12:27

Mas nesse caso é necessário para que a gente não tenha problema.

12:31

O agente pode ficar em um loop infinito. Então, definimos a sessão,

12:37

Aí vai ter aqui o rodar resolução. Então, agora nós estamos pegando... Aqui

12:44

É o runner, já está com o runner. Não muda nada.

12:49

O runner foi criado lá em cima com o workflow, como nós já tínhamos visto

12:55

Anteriormente.

12:58

O resolution, que

13:00

Eu chamei de resolution, na

13:05

Verdade dá para chamar isso aqui de agent,

13:09

Né? Na verdade, não é. Ah não, tá certo,

13:12

Esse aqui é o app, né? É o ticket resolution, que

13:20

Tá com o app registrado aqui. Então, não tem nenhuma mudança.

13:26

A questão é que eu vou deixar ele rodar, não quero pegar nada.

13:31

Então, colocamos esse passo.

13:33

Depois que eu rodei, eu tenho a sessão com tudo o que aconteceu.

13:38

Eu capturo essa sessão e aqui eu tenho que ver se há alguma aprovação pendente.

13:45

Então, dada essa sessão, nós vamos varrer os eventos. Aí eu vou olhar se não

13:52

Conteúdo ou não tiver conteúdo, continue.

13:55

Então, para cada conteúdo, nós vamos buscar o function call.

13:59

Nós estávamos manipulando o function response.

14:02

Ou, em outras linhas agora, que eu vejo se é o request input,

14:05

Que é a constante que carrega o ADK request input.

14:09

Então, se verificarmos que é isso,

14:13

então nós estamos com uma execução pendente.

14:20

Então, desse rastreamento,

14:23

nós extraímos o interrupt ID e a mensagem, justamente

14:32

para poder passar. Então,

14:34

voltando para cá,

14:38

pego aqui...

14:41

que está pendente, verifica o ticket.

14:43

Se está pendente, então retornamos aquilo que a gente tinha visto,

14:47

o interrupt ID, a mensagem. Caso contrário, retorna o

14:52

fluxo normal. Então, ele atende os dois casos.

14:58

E aí vem a aprovação. A aprovação recebe o ticket ID e se está confirmado ou não,

15:04

porque o interrupt nós conseguimos capturar aqui.

15:06

Então verifico o ticket, se não existir 404,

15:09

pego a sessão pelo ticket ID, então facilita demais.

15:14

Então eu preciso ver aqui agora a interrupção. Então eu uso a mesma função de novo,

15:19

porque se eu pego esse pendente e tenho um interrupt ID,

15:21

o que nós vamos fazer é adicionar uma resposta, que a role é do usuário,

15:28

em que vai ser uma function response,

15:32

nós estamos respondendo àquele request input.

15:37

Passa qual é o ID da interrupção, o nome,

15:41

e as informações, nós podemos passar em informações.

15:45

Então ele vai lá e roda a resolução de novo.

15:47

Então estou reaproveitando o código. E no final,

15:50

se a gente quiser apenas consultar o ticket só para ver as informações,

15:55

nós temos aqui também. Eu acho que ele não se perdeu. O

15:59

ticket está resolvido com tudo mais.

16:03

Então... De coisas que a gente não tinha aprendido ainda e nós estamos vendo

16:07

aqui como manipular os resultados e vão

16:12

ter várias informações que cercam os eventos,

16:14

que é a principal informação que nós vamos manipular,

16:17

o que importa é justamente que você organize essa

16:20

parte que vai estar aqui no runner.

16:23

Você pode querer function response,

16:25

você pode querer function call se for uma interrupção,

16:29

você pode querer pegar alguma coisa do state, apesar que... do state.

16:34

Você pode esperar toda essa execução acontecer e

16:37

depois da sessão você pega as informações,

16:40

mas aí você pode querer pegar o State Delta, enfim.

16:43

O que importa é que isso fique

16:45

organizado nesse modelo como nós temos aqui do Ticket

16:56

Receptionist, que fique algo nesse sentido. E aí você pode usar

17:03

alguns design patterns que nós já conhecemos com orientação

17:06

a objeto para poder fazer essa organização. Então,

17:09

aqui nós temos a capa e eu aconselho você a brincar mais com esse projeto,

17:14

acrescente fila,

17:16

faça outros exemplos para que você expanda seus conhecimentos e

17:22

vá além utilizando os conhecimentos que você teve aqui neste capítulo.

17:28

Na verdade, na disciplina como um todo.

## Resumo IA

[RESUMO_IA]