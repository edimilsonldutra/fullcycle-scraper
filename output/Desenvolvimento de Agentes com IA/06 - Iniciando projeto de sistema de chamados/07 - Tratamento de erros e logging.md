Módulo: Desenvolvimento de Agentes com IA\
Aula: [Tratamento de erros e logging](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18562)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre tratamento de erro na execução das tools.

00:05

A qualquer momento, pode acontecer qualquer tipo de erro nas nossas tools,

00:10

desde um erro de programação básica até mesmo

00:14

algo inesperado quando nós estamos chamando algo externo,

00:18

como banco de dados. Esse trecho pode lançar um erro de SQL,

00:22

por causa que fizemos alguma coisa errada no banco.

00:26

ou porque a conexão com o banco de dados não está funcionando,

00:29

então ele lançaria uma exceção.

00:32

Então nós temos que entender como tratar esse tipo de erro.

00:35

Mas antes da gente chegar lá,

00:37

quero só relembrar o que nós já aprendemos durante a disciplina,

00:42

que uma vez que eu já identifico um problema que aconteceu,

00:45

eu já posso retornar dessa tool.

00:49

um dicionário que vai descrever o problema. Então,

00:52

isso vai lá para a LLM e ela vai dar a continuidade

00:55

dos próximos passos e a gente vai executando tudo o que é necessário.

00:59

Então, em alguns cenários,

01:01

não vale nem a pena a gente acabar gerando aquele lançamento tradicional,

01:07

como esse que está aqui. Aqui nós preferimos lançar uma exceção com raiz.

01:14

falando que se eu não tenho a mensagem do usuário, então a mensagem está vazia.

01:19

Precisa pedir essa mensagem lá para o usuário.

01:21

Eu poderia retornar esse mesmo dicionário aqui? Sim,

01:25

poderia retornar esse mesmo dicionário. Mas aqui,

01:28

por ser algo que eu considerei mais sério,

01:32

preferi lançar essa exceção. Então,

01:35

em lugares onde podem acontecer erros,

01:41

que vão ser...

01:44

lançado exceções, podemos usar um try catch,

01:49

que no caso do Python não tem o catch. É o except,

01:52

que pode ser passado de forma genérica sim, ou você passa, por exemplo, ValueError e

02:01

coloca o alias para variável.

02:05

E aí você tem aqui o bloco do except.

02:08

E aí você poderia retornar esta mensagem já

02:13

para resolver o problema. Mas aqui eu quero alertar,

02:17

que essa forma aqui não tem nada de errado,

02:20

não tem nenhum problema trabalhar dessa forma, nós estamos tratando o erro.

02:24

Mas, uma vez que a gente vai construindo uma aplicação ágil,

02:28

vão ter vários agentes,

02:30

é comum que nós não iremos querer

02:36

colocar todos os tratamentos dentro das tools. Porque veja só,

02:41

aqui nesse trecho nós podemos ter problema com conexão com banco de dados.

02:46

Imagina ficar espalhando em todos os agentes que eu tenho, todas as tools,

02:51

um try para ver se tem um problema de conexão e aí eu retorno aqui uma mensagem.

02:58

Isso iria poluir, iria duplicar o código.

03:01

Então eu quero chamar a atenção para uma forma de trabalhar com

03:07

esse tratamento que nós aplicamos essas boas práticas em uma aplicação tradicional.

03:13

E esses mesmos princípios valem aqui para uma aplicação ágil.

03:17

E quando nós temos um framework convencional,

03:19

normalmente o framework vai nos dar ali um middleware,

03:22

ou se não, um service de handle error, que a gente consegue lidar com os erros.

03:30

Então, se torna mais fácil delegar a essa camada,

03:33

uma camada mais externa, para que ela capture o erro,

03:37

e aí você decide o que você vai fazer com ele, se você vai transformar.

03:41

Numa resposta HTTP com tal status code, se esse erro vai ser logado,

03:46

se vai ser gravado em algum lugar,

03:48

se vai produzir algum outro efeito. Então nós deixamos ali os controllers,

03:53

os nossos serviços e qualquer

03:56

coisa livre desse tratamento de erro.

04:00

Não significa que em determinadas situações eu preciso

04:03

capturar o erro para tentar novamente,

04:07

às vezes eu poderia fazer um retry,

04:09

ou alguma outra coisa, e aí se aconteceu um outro erro,

04:14

aí eu vou e faço um raise do erro.

04:16

Aí ele vai subindo. Então a ideia é a mesma que com as tools.

04:21

Mais abaixo no código, eu fiz uma implementação de como que seria isso.

04:26

O SDK nos dá uma captura desse

04:31

erro da tool através da propriedade onErrorCallback.

04:36

Aqui nós passamos uma função que vai capturar esse erro. Mas essa propriedade,

04:42

ela recebe não somente um callback, ela pode receber também uma lista de callbacks.

04:49

Nós vamos entender como funciona essa questão de lista também. Então,

04:52

eu posso ter aqui um array de funções que vão

04:55

me ajudar a fazer esse tratamento de erro.

04:58

Aqui está o handleToError. Então, é um tratamento geral.

05:03

Se eu tiver alguma questão...

05:07

específica para uma tool, nós conseguimos identificar dentro da própria função.

05:11

Porque ela recebe a tool que foi invocada,

05:15

os argumentos que foram passados para essa tool. Então,

05:20

se eu tivesse lá aquele client ID,

05:22

senha que nós já trabalhamos, se ele foi passado para a tool,

05:26

conseguimos pegar. Aqui é um dicionário, chave e valor.

05:30

O tool context que nós já conhecemos e o erro que foi lançado na exceção.

05:37

A ideia é

05:39

que nós retornemos um dicionário, ou na verdade um nome.

05:44

Nós podemos retornar as duas coisas, como na

05:52

tipagem que ele vai acabar demonstrando esse tipo de situação.

05:56

Porque no momento que eu estiver fazendo um tratamento de erro,

06:00

eu posso escolher não

06:02

fazer nada pelo tipo de erro que aconteceu.

06:06

Então, imaginando que eu tenho uma lista de handleError,

06:13

handleError2, o

06:15

primeiro que resolver, entre aspas, a parada, vai fazer com que aquela resposta,

06:23

aquele dicionário, seja a resposta da tool.

06:27

Caso ele retorne none, então vai para o próximo e assim vai.

06:31

Se nenhum deles resolver,

06:32

vai acabar sendo, esse erro vai subir e vai acabar estourando no runner ali.

06:39

E aí...

06:40

nós teríamos que identificá-lo aqui.

06:45

Mas eu quero também chamar a atenção para

06:48

essa questão de fazer tratamento de erros nesta execução,

06:54

porque se

06:56

Você faz algo aqui tendo em vista para que

07:01

Você possa recuperar o erro e tomar alguma providência,

07:05

Cuidado com a fragmentação da lógica do seu agente.

07:10

Fora que também...

07:12

Se você faz algo no seu web, no seu CLI, no desktop, na

07:18

Hora que você vai testar com a DKWeb e com a DKRun, está fragmentado.

07:23

Você não vai conseguir ver todo o processo acontecendo. Então,

07:27

A ideia é que a gente mantenha tudo dentro do agente.

07:32

Na hora que nós estivermos utilizando o runner,

07:34

É apenas a capa ali para que a gente...

07:36

Ah, aconteceu um erro, então eu capturo essa informação.

07:41

Para poder dar um parecer para o usuário ou fazer alguma coisa com isso.

07:44

Nada perto de resolver os problemas dentro do agente.

07:50

Então, nós podemos passar essa lista. Às vezes,

07:53

Você tem vários tratamentos de erros para erros específicos. Se for tal erro,

08:00

Então eu quero capturar e fazer o tratamento. Caso não seja,

08:03

Passo para frente, que não é minha responsabilidade.

08:06

Mas veja só, aqui nós estamos capturando o erro que aconteceu e nós temos,

08:11

Fora um erro de programação básico,

08:14

Nós temos um ValueError, se o usuário não passar a mensagem,

08:17

Um erro em relação ao repositório.

08:19

Fora isso, nós não vamos ter nenhuma outra oportunidade. Então,

08:22

Eu verifiquei se o erro é do tipo,

08:25

Esse is instance,

08:29

É a mesma coisa do instance of e de outras linguagens de programação.

08:34

Nós verificamos se é do tipo ValueError.

08:37

Como eu estou padronizando sempre o statusError mais a mensagem,

08:40

Estou utilizando a mensagem da própria seção, convertendo ela para string.

08:44

Agora, caso seja qualquer outro tipo de erro,

08:47

Inclusive esse de banco de dados ou um erro de SQL, eu não vou deixar vazar isso.

08:53

Então, eu retorno um erro genérico.

08:56

Aconteceu um erro inesperado, eu vou processar a sua solicitação.

09:00

Tudo isso vai acabar indo para a LLM.

09:03

E aí nós podemos fazer um log desse erro.

09:07

Aqui também temos um código de como funciona isso.

09:10

O Python já tem toda essa parte para poder fazer login.

09:13

Ele tem uma lib de login. Nós iniciamos um logger,

09:19

Que pode ficar em outra pasta,

09:21

Você pode até colocar esse login integrado com

09:25

Qualquer outra coisa que você queira,

09:27

Com um banco de dados, com qualquer outra ferramenta.

09:29

Você inicia o logger pegando...

09:34

Esse getLogger passando essa variável mágica name.

09:39

Então significa que quando ele vai registrar esse logger,

09:43

Ele vai registrar para o arquivo agents.py com o seu caminho absoluto. Você

09:52

Pode criar o logger a partir do arquivo, a partir da classe, como você quiser.

10:00

Então, com esse logger já disponível no arquivo, basta apenas fazer a escrita dele. Então...

10:09

Nós podemos logar debug,

10:13

Error, exception,

10:16

Informação,

10:17

Informação de log, tem vários métodos,

10:20

Então, como é um erro que eu quero colocar numa string,

10:23

passamos a string com dois tokens que vão

10:27

ser preenchidos por essas duas informações.

10:30

Colocando aspas, nós conseguimos jogar essas duas strings,

10:33

qual é o nome da tool que deu erro e o erro específico.

10:37

Se a gente quisesse até diluir mais esse erro,

10:41

poderíamos pegar outras informações, detalhar um pouco mais, enfim.

10:46

Mas isso aqui já vai ser suficiente para que a gente veja que aconteceu um problema.

10:51

Então, vamos rodar o ADK Web.

11:00

Vou deixar o reload aí, gente, caso a gente faça alguma modificação.

11:05

Então, vamos pegar

11:10

o agente e... Deixa

11:13

eu ver se eu tenho um histórico.

11:19

Eu não tenho que editar a mensagem,

11:20

então estou colocando que está um erro de integração com o GitHub,

11:23

como nós já tínhamos testado anteriormente.

11:28

Ok. Foi registrado o

11:32

ticket. Mas agora eu

11:37

vou chegar aqui

11:39

nesse rise, aumentar essa parte e jogar esse trecho.

11:43

Então, ele vai forçar o lançamento de erro que

11:48

a mensagem está vazia, um ValueError.

11:52

Uma exceção nativa do Python.

11:54

Então, vamos

11:57

pegar a mensagem novamente e fazer o envio.

12:01

Às vezes, esse reloading do agente faz com que

12:06

o agente seja recarregado e ele não funcione. Vamos ver.

12:15

O agente vai receber a mensagem que a mensagem do usuário não foi enviada.

12:21

Obviamente que foi.

12:24

Veja só. Com certeza, para prosseguir com a criação do seu ticket, você poderia...

12:29

me fornecer a descrição detalhada para que eu possa registrar esse problema.

12:34

Então, ele está justamente por

12:37

conta do nosso retorno.

12:39

Está vendo aqui que na parte 6 já tivemos

12:43

o registro do ticket com status de erro e a

12:49

mensagem que foi vazia. Então, apesar de existir,

12:52

ele considerou o que foi enviado depois como a verdade. Então...

13:01

Obviamente, não faz sentido continuar testando porque ele

13:03

vai acabar dando no mesmo aqui,

13:05

porque ele vai tentar registrar o ticket e vai cair naquele erro.

13:08

Agora, veja que nos logs ele

13:11

ficou orgânico no histórico, né?

13:14

Ele ficou juntamente com as informações que vai registrando cada etapa,

13:19

mas enquanto ele sempre mostra o Google LLM .py, aqui temos o agente na

13:26

linha 90. E, obviamente, isso aqui é por conta do nome do arquivo, se eu quisesse...

13:31

colocar o nome do agente aqui.

13:34

A gente poderia chegar ali no getLogger e colocar

13:38

o nome do agente ou qualquer outra informação. Então,

13:41

erro ao executar a ferramenta Registrar Ticket.

13:44

A mensagem do usuário está vazia, não foi possível registrar o ticket.

13:49

Agora nós podemos fazer um

13:53

outro teste tirando a message daqui,

13:56

porque ela acaba sendo obrigatória. Vamos rodar novamente.

14:04

E aí, eu

14:07

quero pegar essa mensagem.

14:14

Vamos ver o que vai acontecer.

14:17

Para o SQLAlchemy lançar uma exceção.

14:26

Na verdade, mesmo sem a message, eu

14:30

acredito que a message é obrigatória.

14:33

Mas tem um default dela,

14:40

então o customer vai ser o melhor caso.

14:44

Porque o customer é obrigatório e ele não

14:47

vai conseguir determinar nenhum parâmetro default.

14:53

Então, vamos gerar um

14:55

novo teste.

15:11

Ele tentando fazer a

15:16

invocação do registrar to. Eu vou falar disso aqui que tem a ver com a idpotência,

15:21

você já percebeu. Então, você está enfrentando,

15:24

entendi que você está enfrentando problema com a integração que

15:29

você relatou. Infelizmente, ocorreu um erro inesperado,

15:32

tenta registrar o seu ticket.

15:34

Você poderia confirmar se os detalhes estão corretos?

15:38

Ou gostaria de adicionar mais alguma informação para que eu possa...

15:41

Aqui é o agente, obviamente, tentando resolver.

15:43

E claro que aqui nós poderíamos adicionar

15:47

mais instruções ali no System Prompt do agente,

15:50

já o preparando para como ele vai se comportar nessas situações,

15:54

porque uma vez que ele chamou o

15:57

registrar ticket e nós vamos ter na

16:03

resposta o erro aqui

16:12

na request... aconteceu a... o

16:16

erro foi passado pra ele.

16:19

Então, ele foi lá e chamou de novo. Então, nós vamos ter, fora

16:27

essa parte aqui

16:31

que tá bem grandinha, são os dois erros.

16:38

São as duas chamadas. Tem essa primeira, que

16:45

aconteceu, aí tem a resposta.

16:48

Aí na parte 7 do conteúdo, vai

16:52

ter a resposta novamente.

16:55

Então o modelo viu nesse caso, olha, infelizmente...

17:00

Não vai dar certo isso aqui, não adianta eu ficar tentando. Então,

17:03

às vezes ele pode entrar nesse loop por N motivos,

17:05

mas aqui nós não fizemos a operação. Mas se o seu agente for mais complexo,

17:12

ele pode fazer uma operação numa tool e na próxima dar erro e

17:18

aí ele entende que ele tem que voltar para a tool anterior de novo.

17:21

Então, isso tem que ser idempotente.

17:23

É um tipo de software com um paradigma bem diferente do que nós estamos...

17:29

Eu deixei aqui também um erro de banco de dados

17:32

que você pode usar para que você possa brincar com isso também.

17:37

Então ele retorna aquele erro genérico ali e aí

17:40

o usuário decide o que vai fazer ou não.

17:44

Então seria muito importante que nós tivéssemos essas instruções de

17:49

como que ele vai lidar com o tratamento de erro.

17:51

Nós não vamos deixar isso à mercê.

17:54

Se você deixar à mercê...

17:56

Aqui teria necessidade dele tentar de novo? Depende.

18:03

Pode ser que se for um erro que você

18:07

sabe que ao retentar mais algumas vezes vai dar certo,

18:11

vale a pena. Agora, se for um erro que vai ficar onerando,

18:15

você vai ficar gastando token, gastando comunicação,

18:17

gastando tempo do seu projeto, executando em produção,

18:21

não vale a pena. Então, tudo isso precisa ser gerido. Então,

18:24

por isso que fazer esse tratamento de erro fora até ajuda

18:28

você a entender quais são os erros que podem acontecer nas tools.

18:34

Você pode ter N tools adicionadas e aí você faz o seu tratamento de erro até criar um

18:40

helper ou algo centralizado que você sai reusando através dos

18:45

agentes para que você não tenha que duplicar código.

18:47

Aí sim fica muito mais sustentável.

18:52

Para que você possa gerir esses erros que vão acontecendo.

## Resumo IA

[RESUMO_IA]