Módulo: Desenvolvimento de Agentes com IA\
Aula: [Persistência da sessão no banco de dados](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18485)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos fazer a persistência das sessões. Até o momento,

00:04

nos dois exemplos que nós fizemos no web e no main.py,

00:08

nós estamos utilizando o serviço de gerenciamento da sessão em memória,

00:13

com o In-Memory Session Service.

00:15

Não significa que é errado usá-lo,

00:18

porque ele é apenas para desenvolvimento, para debug, ou algo nesse sentido.

00:23

Às vezes, você pode querer que o seu agente não armazene sessão. Isso é bem comum.

00:29

Então... Não tem problema. A questão é que se eu quero sessões longas,

00:34

que o usuário consiga retomar o que ele está fazendo,

00:37

nós vamos persistir essa sessão em algum lugar.

00:41

E o próprio ADK já fornece drivers para que a gente faça armazenamento no

00:47

SQLite, no Postgres, no SQL, no Vertex AI,

00:51

que é um serviço provido pela própria Google, que está no Google Cloud.

00:55

Então nós temos já várias opções padrão.

00:58

de armazenamento. Então, vamos mudar isso aqui.

01:01

Eu vou deixar comentado o In-Memory Session Service.

01:06

Então, eu vou importar de google.adk

01:12

.sessions. Vamos começar pelo SQLite.

01:17

SQLite Session Service.

01:19

Aqui deu a sugestão errada.

01:22

Aqui o SQLite é escrito tudo em minúsculo. Então,

01:27

Session Service vai

01:33

ser igual...

01:36

a nossa classe. Eu

01:42

estancinho ela passando qual o caminho do meu banco

01:47

de dados. A gente pode colocar aqui,

01:49

na verdade nem precisa desse parâmetro nomeado, podemos

01:53

colocar apenas ponto barra.

01:56

Vou aceitar essa sugestão, está de bom tamanho.

01:59

Operador conta session.sicolite. Vamos rodar o projeto.

02:05

Então ele já está de pé, eu

02:08

não tenho ainda nenhum ponto sicolite. Então...

02:17

Nós podemos fazer a

02:23

criação da sessão.

02:25

Só isso aqui já vai ser suficiente. Veja só.

02:29

Operador conta session.sicolite. Aí aqui o caso do caminho,

02:33

ele vai considerar exatamente a raiz do projeto,

02:36

que é onde nós estamos rodando o nosso comando.

02:39

Aí você pode organizar e armazenar onde você quiser.

02:43

Então, nós já temos tudo sendo armazenado ali.

02:47

A partir do momento que eu tenho... Esse código da sessão, ele

02:54

criou o banco de dados que não existia, vai

03:00

armazenar tudo de forma correta.

03:03

Vamos aguardar aqui o retorno dele. Então, aqui já deu certo,

03:08

nós podemos ver, isso eu tenho o SQLite 3,

03:11

que você pode instalar na sua máquina. Então, SQLite 3 para o operador SQLite,

03:18

com o ponto schema, na verdade, ponto tables.

03:25

temos já as tabelas criadas.

03:28

Tabela de app states, eventos, sessions e user states.

03:34

Então, se eu fizer um select na tabela de sessões,

03:40

Eu tenho o operador da conta, que é o nome, na verdade, do app.

03:46

Agora, é bom ver e fazer a relação disso.

03:51

Esse operador de conta que está ali é esse operador de conta aqui.

03:56

Qual é o usuário? O ID da sessão e

04:04

outras informações. Se você quiser ver o esquema da tabela,

04:08

pode colocar esquema .sessions, então tem o appName, o username,

04:13

o ID, o state, que a sessão pode ter estado,

04:17

quando ela foi criada e foi atualizada, e

04:23

a definição da primaryKey, então é uma primaryKey composta.

04:27

Ela tem o appName, o userID e o ID.

04:32

Exatamente por isso... Quando nós vamos pegar a sessão, nós

04:38

precisamos passar os três valores.

04:43

Isso significa que eu poderia ter um ID de sessão, obviamente um UID versão 4,

04:50

a chance de gerar um idêntico é muito pequena,

04:54

mas eu poderia ter um ID de sessão repetido,

04:58

mas com userID e appName diferentes. É a forma que ele está organizando.

05:06

Nós conseguimos ver até mais detalhes disso ao ver o código-fonte.

05:10

Aqui em cima, quando ele

05:14

vai carregar, tem o esquema das tabelas.

05:18

Então, no momento que ele vai processar ali pela primeira vez,

05:22

se não tiver o banco de dados,

05:23

ele vai lá e cria todo o esquema. Então, a tabela de eventos,

05:26

a tabela de sessão que nós estamos vendo, enfim.

05:30

Então, nós conseguimos ter essa persistência aqui e gerenciá-la.

05:35

Quando nós rodamos os agentes,

05:37

tanto com ADK Run quanto com ADK Web, desde lá de trás, nós já estávamos trabalhando com,

05:44

se você já teve a oportunidade de rodar os exemplos do curso,

05:47

fazer os seus exemplos,

05:48

você sempre vai ver essa pastinha .adk,

05:51

que obviamente nós vamos tender a ignorar, porque

05:58

nós não queremos que isso faça parte do controle de versão.

06:01

Então, nós vamos ter... todo o histórico das sessões,

06:04

porque nós podemos retomar isso a qualquer momento, enfim,

06:07

fazer no nosso ambiente de testes. Por padrão, sempre é assim.

06:11

Nós vamos ter sempre o ponto ADK com SessionDB quando você roda com os dois.

06:17

Até mesmo quando você para o seu projeto e roda de novo com ADK Web,

06:22

você vai conseguir ver a lista das sessões e retomar de onde você estava.

06:28

Agora, como nós já sabemos armazenar a sessão,

06:31

tendo em vista que nós vamos usar bastante esse agente na web.

06:36

Vamos ficar rodando a nossa API,

06:38

ficar fazendo os testes, caindo exatamente neste SQLite.

06:44

Se nós rodarmos o ADK Web, se

06:50

eu já tinha deixado rodando aqui,

06:52

vamos dar um Enter, eu

06:57

não vou ter nenhuma sessão ativa. Ao clicar aqui, ele mostraria a lista das sessões,

07:03

eu conseguiria importar. Já tem todo o ambiente para gerenciar isso.

07:09

E agora nós temos o SessionDB que diverge do nosso SQLite que está aqui.

07:14

Então, nós podemos fazer o comando

07:17

apontando para o mesmo agente, passando o SessionServiceURI,

07:23

que vai conter a URI para

07:27

O banco de dados, no nosso caso o SQLite.

07:31

Então cuidado que aqui no protocolo, que é passar usando o SQLite, são três barras.

07:37

Para que dê certo. Então, pronto.

07:43

Agora, eu vou recarregar novamente, e

07:49

Ao clicar aqui, veja que não tem nenhuma sessão,

07:54

Apesar de nós termos duas.

07:57

Nós vamos fazer aqui, novamente, SQLite,

08:01

3 no arquivo, e aqui

08:07

Vem o VS Code encaixando virtualenv, que acabou quebrando.

08:13

Temos duas sessões.

08:16

Ele está marcando que não existe para o usuário.

08:21

Mas eu posso trocar esse usuário para

08:25

Cliente 123, que é o que está presente ali.

08:30

Também não vai ser encontrada nenhuma sessão.

08:33

Exatamente por quê? O nome do

08:38

Nosso agente é Operador Conta Session, mas não é só o nome do agente.

08:42

Agora nós já sabemos que tem um app no meio. Quando eu estou rodando o ADK Web...

08:50

Ele já vai preparar a questão do runner, a questão do app. Ele vai pegar, na

08:57

Verdade, aqui está Operador Conta, está vendo?

09:03

Então, nem é esse nome.

09:06

Ele vai acabar criando um app igual

09:09

A app com o nome Operador Conta Session.

09:14

Então, nós não vamos conseguir identificar aquelas sessões,

09:20

A não ser que nós mudássemos.

09:22

O nome da pasta, mas agora vamos colocar aqui um Olá e

09:28

Agora nós temos essa sessão ligada a usuário 123.

09:35

Então, se eu mudo para usuário User,

09:39

Que é o padrão, você pode fazer o reset se você quiser. Veja só.

09:45

Eu não tenho, mas ao

09:49

Colocar o cliente 123, nós vamos ter a sessão.

09:56

Veja só. Então, esse User aqui pode...

10:02

Ter dado a impressão, desde quando nós começamos a mexer,

10:05

Que era algo de usuário autenticado,

10:08

Na verdade, é porque tudo é escopado pelo usuário.

10:13

Nós podemos ver agora, ao rodar novamente, que o

10:20

Nome, o

10:23

Namespace, é

10:25

Operador Conta Session.

10:31

É o app name. É

10:34

Por isso que a definição do app name é importante.

10:36

Ele vai colocar essa informação aqui, ela vai ser buscável através disso.

10:42

Então, agora eu posso matar essa execução, rodar novamente,

10:47

Eu tenho acesso a essas sessões que vão ser do Operador Conta Session.

10:53

Nós conseguimos fazer essa mesma

10:57

Situação para o ADK Run, a mesma coisa.

11:02

Aqui, no caso, estávamos

11:08

Em um terminal que não tinha virtualenv,

11:10

Eu consigo fazer o Session Service UI e aí passo.

11:20

Toda a minha string de conexão.

11:23

Mas aqui há uma diferença, porque para

11:28

Você pode retomar a sessão, você não consegue escolher,

11:31

porque o ADK Run já vai rodar diretamente só um agente,

11:34

enquanto o ADK Web pode te dar uma lista de agentes,

11:37

você teria que fazer um comando como este que está aqui.

11:43

Essa aqui é uma das formas.

11:45

Vou colocar em tela cheia para ficar mais fácil. Você passa o seu agente,

11:50

delimita... um Session ID para ele e passa a mensagem. Então,

11:55

vamos colocar aqui um ID qualquer, não importa, na verdade, qual

12:00

é o ID que está aqui. Podemos colocar assim, 1.

12:06

Então, veja que eu coloquei que esta é a minha primeira mensagem,

12:09

uma pergunta para a gente. Ele falou sim.

12:12

Agora, se eu rodo novamente,

12:15

ele vai

12:20

falar como mencionei anteriormente.

12:23

Nesse caso aqui, nós não estamos apontando o SQLite,

12:27

então, ele está usando o Session

12:32

DB que está criado aqui dentro.

12:36

Agora, isso aqui é ruim para poder interagir com a gente,

12:40

então quando eu estou no ADK Run, se eu quero fazer de forma mais livre,

12:46

aí nós vamos ter que passar aqui,

12:50

nós podemos até colocar o Session ID para determinar este ID,

12:55

mas nós passamos o Save Session.

13:03

Melhor, saveSession, sempre, no caso do Python, sempre com underscore.

13:08

Então agora eu posso fazer um Olá, posso fazer qualquer coisa, e

13:14

você tem que digitar o exit,

13:17

não coloque aqui um Ctrl-C para poder quebrar o comportamento,

13:20

para dar chance que ele termine e salve a sessão.

13:23

Então eu tenho a sessão com esse aí de salvo, ele

13:29

vai criar um JSON da sessão com os eventos,

13:34

porque toda sessão tem um ou mais eventos.

13:39

Então agora nós conseguimos rodar novamente, fazendo

13:46

"-resume", passando

13:52

Agents mais o caminho e

13:57

esse JSON aqui.

13:59

Pronto. Então ele resgata de onde nós paramos,

14:05

assim como você faz com o seu agente de IA. Porque

14:09

o ADK não tem essa facilidade de você...

14:14

ficar escolhendo a sessão que você quer.

14:19

Você precisa administrar dessa forma. Então, inicia uma e faz o Resume, ou faz

14:26

daquela forma que às vezes pode ser um teste mais básico.

14:30

Agora vamos ver como conectar em outro banco de dados.

14:33

Eu criei um Docker Compose na raiz que sobe um container do Postgres,

14:39

fica fácil para que você possa testar na sua máquina,

14:41

você pode pegar esse código e brincar à vontade.

14:45

Existe uma outra classe que permite que a gente conecte em outros bancos.

14:51

Está no mesmo pacote aqui de sessions, porém é

14:56

o DataSessionService.

14:58

Vamos olhar tanto o SQLiteSessionService, que ele estende de BaseSessionService,

15:05

quanto o DatabaseSessionService, que estende de BaseSessionService.

15:13

Essa aqui é uma classe padrão, lembrando que no Python não temos interface.

15:17

Se você não está acostumado com Python,

15:19

Na verdade, nós conseguimos fazer uma espécie de interface de algumas formas,

15:23

Utilizando a própria classe ABC,

15:25

Abstract Base Class,

15:30

que é uma classe base abstrata,

15:35

Justamente o que

15:38

ele está falando aqui. Não é uma interface essa classe,

15:41

Dá até para ser executada e tudo mais.

15:43

Mas se eu quiser fazer qualquer outro tipo de armazenamento,

15:47

Eu crio a classe, estendo dela,

15:49

Ela vai exigir que eu implemente os métodos createSession,

15:53

getSession, listagem das sessões,

15:55

Enfim. Então eu posso fazer o que eu quiser.

15:58

Então vamos comentar aqui

16:01

E agora sessionService

16:07

Vai ser igual ao meu database sessionService.

16:12

Então aqui nós podemos passar uma string de conexão.

16:17

E essa string de conexão, você tem que tomar cuidado, no caso do Python,

16:21

Porque se eu utilizo o que a IA está dizendo aqui,

16:25

Eu vou ter que instalar essa lib com o PG2,

16:31

Que é uma lib que vai permitir que eu faça,

16:34

Que você vai instalar libs dentro de qualquer tipo de projeto.

16:40

Então, depende do que você quer.

16:44

Eu já tenho aqui uma string de conexão.

16:48

Para que eu não digite tudo isso aqui, então eu vou utilizar o async-pg.

16:56

Então nós temos que instalá-lo com

17:00

O uv, só

17:03

Fazer esse comando aqui, eu já tinha instalado previamente, então aqui

17:11

Nós conseguimos, acho que até aqui em cima tem o suporte, nós

17:16

Conseguimos conectar usando isso também com o PostgreSQL, com o MariaDB,

17:21

Com o SQL, com o Postgres, mas nada impede que você faça.

17:25

Não é nada complexo, é muito simples, na verdade, fazer um driver,

17:29

Na verdade, fazer uma adaptação para qualquer outro banco de dados. Então,

17:33

Como todo mundo trabalha aqui no mesmo padrão,

17:36

Na verdade, o que nós estamos olhando,

17:37

Se esse sessionService, se ele é uma base sessionService, não importa.

17:43

Ele vai ter que implementar todos os métodos que nós temos,

17:48

Por exemplo, createSession.

17:54

Ah, vai preparar as tabelas se as tabelas não estão criadas.

17:57

Então, faz com que a gente crie.

18:00

Então, você não tem que importar e criar as tabelas antes.

18:06

Então, vamos rodar novamente isso aqui.

18:10

Então, vou fazer um ADK.

18:13

Na verdade, nós podemos rodar com o próprio UVCore.

18:20

Pronto. Ele está falando que precisa do SQLAlchemy, que é uma lib também.

18:29

Na verdade, é um ORM muito famoso da comunidade Python. Então, vamos instalá-lo.

18:35

E agora o endereço já está em uso. Então, vou

18:41

Tirar o que tinha aqui na porta 80 e rodar novamente. Pronto.

18:48

Então, vamos

18:52

Fazer um teste que

18:58

Ele vai criar a sessão. Da sessão vamos

19:09

Enviar uma mensagem. Nós podemos fazer um reload ali com o

19:14

FastAPI ou até mesmo uma quebra aqui.

19:18

Então... Dessa forma, agora, se eu fizer a mesma chamada,

19:22

Porque eu quebrei o processo,

19:24

E ele armazenou no banco de dados, ele não vai dar erro.

19:29

Ele vai reutilizar a mesma sessão. Agora,

19:33

Ele já está insistindo que a gente faça o envio do Client ID.

19:40

E aí, se eu quiser utilizar o ADK Web, eu posso passar toda

19:45

A string de conexão da mesma forma no Session Service UI.

19:51

Como ele está falando, eu estou utilizando agora a conexão com Postgres e

19:56

Obviamente, nós não vamos conseguir ver sessões iniciais

20:00

Porque vai mudar o nome do app name,

20:03

Como nós já aprendemos aqui nessa aula, mas fazendo um olá, ao

20:12

Ver aqui, nós temos a sessão, enfim, nós

20:16

Poderíamos entrar no

20:19

Banco de dados, vamos fazer aqui um docker compose exec postgres bash com

20:32

Um psql menos o root, na

20:37

Verdade, menos o acme, né?

20:41

Então, eu posso selecionar o database. Na

20:52

Verdade, só temos o acme, ele já está selecionado. Então,

20:54

Nós temos aqui a tabela de eventos, está tudo certinho.

21:00

De sessões, temos

21:03

Aqui a

21:06

Sessão tinha anterior, teve

21:11

A primeira que foi feita com teste...

21:14

Acho que isso aqui foi uma execução prévia que eu tive,

21:16

E essa agora, tem aqui o usuário.

21:18

Então, essa aqui é a anterior, que nós geramos com a aplicação web,

21:22

E essa aqui é agora o que nós geramos no ADK Web.

21:29

Então, tem esse armazenamento persistente, e obviamente,

21:32

Nós não falamos muito aqui desse armazenamento,

21:36

Mas a tabela de eventos tem a sua relação direta com sessão.

21:47

Para cada sessão, nós temos N eventos e eles são armazenados aqui também,

21:52

Obviamente, com todo esse serviço. Ele já tem

21:58

Tudo pronto para ter esse armazenamento consistente,

22:02

Porque se eu estou armazenando a sessão,

22:03

Tenho que armazenar os eventos que aconteceram, tudo certinho,

22:07

Atualizar as datas, nós conseguimos fazer essa escolha.

22:11

E tem a opção também do BetX AI,

22:14

Que é o serviço que eu tinha falado anteriormente, é um serviço que...

22:18

Permite que você não se preocupe em como você vai gerenciar esse armazenamento,

22:23

A busca. Então,

22:24

É um banco de dados como serviço que a Google está hospedando para

22:30

Te dar mais suporte na comunicação da persistência das suas sessões com os agentes.

## Resumo IA

[RESUMO_IA]