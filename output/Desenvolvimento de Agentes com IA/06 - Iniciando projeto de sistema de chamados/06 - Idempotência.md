Módulo: Desenvolvimento de Agentes com IA\
Aula: [Idempotência](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18561)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre o conceito de idempotência.

00:05

É uma palavra que vem lá da matemática, um conceito que vem da matemática,

00:08

mas que nós aplicamos na área de desenvolvimento de aplicações.

00:12

É algo muito importante na hora que nós estamos desenvolvendo,

00:16

porque ela garante que algo que pode ser

00:21

executado n vezes vai produzir o mesmo resultado.

00:24

Então, nós garantimos a consistência daquela operação.

00:28

Se eu tenho uma fatura, por exemplo, ela só pode ter um reembolso.

00:33

Então, imagine que você tem uma API REST e

00:37

o endpoint que vai receber essa solicitação de reembolso. Então,

00:41

você vai lá e tem o reembolso feito.

00:44

Mas, e se eu chamar mais 10 vezes?

00:48

Pode ser de forma sequencial ou simultânea.

00:51

A ideia da idempotência é que essa fatura vai continuar com um reembolso só.

00:56

E aí você vai escolher como retornar esse aviso,

01:00

seja ele por um erro ou seja apenas por um aviso convencional.

01:04

O ponto é que no banco de dados ou qualquer

01:07

coisa que esteja conectado com o nosso sistema,

01:10

não vai ter nenhuma mudança de estado, não vai ter nenhuma alteração.

01:15

Nós vamos ter todos os dispositivos para checar se aquela operação já foi feita.

01:21

Não vai ser possível duplicar um reembolso, um saque,

01:26

um depósito ou qualquer coisa que traria

01:29

consequências catastróficas para o nosso projeto.

01:33

Existem várias formas de fazer essa idempotência.

01:36

Através de locks,

01:37

estamos falando aqui mais especificamente em nível de banco de dados,

01:41

um lock pessimista permite que você trave a tabela ou banco de dados,

01:45

então somente quem estiver manipulando, escrevendo, pode fazer a operação,

01:50

os outros vão ter que esperar.

01:52

O lock otimista não tem o travamento em nível técnico no banco,

01:55

mas a gente faz em nível da aplicação. Tem o lock distribuído,

01:59

que normalmente se usa um sistema de cache para que você trave

02:03

um valor e todo mundo fique esperando até que aquele valor seja desbloqueado.

02:08

Podemos usar condicionais.

02:12

É basicamente fiel. Se eu estou fazendo um reembolso,

02:15

a primeira coisa que eu deveria fazer é verificar se

02:17

eu tenho esse reembolso no banco de dados.

02:19

Se caso tiver, então... nós já não executamos nada, já devolvemos a resposta.

02:26

Com chaves de unicidade também em banco de dados,

02:29

quando usamos os IDs, chaves primárias,

02:32

índices, constraints, unique,

02:34

nós garantimos que aquele valor não possa ser duplicado na tabela.

02:41

Isso garante que se eu tento fazer algo duplicado,

02:44

esse registro, eu não vou conseguir,

02:47

meu banco de dados vai ter um erro. Então, temos outros...

02:51

Outras N formas,

02:53

e nós não estamos aqui justamente para poder

02:55

falar como você vai implementar a idempotência,

02:59

mas a questão é que você entenda que nós podemos fazer a idempotência, que

03:06

vai garantir esse mesmo resultado quando nós estamos processando a operação

03:12

Naquele processo, ou

03:18

De forma a garantir a idempotência em processamento.

03:29

Vários estão tentando fazer o reembolso ao mesmo tempo de uma fatura.

03:36

Então somente um pode processar e os outros vão dar um erro ou vão

03:43

ter uma resposta de que o reembolso já foi emitido ou que ele está sendo emitido.

03:51

Isso é importante para o caso dos nossos agentes porque nós

03:57

vamos ter usuários que

04:00

enviam informações para o agente e se comunicam com o LLM.

04:09

Vamos pensar que nessa comunicação, quando

04:15

temos um turno, nós

04:21

já entendemos esse conceito, nesse turno, a

04:25

LLM pediu para o agente executar uma ferramenta, mas por causa do System Prompt,

04:31

por causa do tipo, do modelo que você está utilizando,

04:36

depois da execução da ferramenta, nós já vimos que

04:40

vai ser mandado novamente o resultado disso, mais o system prompt,

04:44

e a LLM pode simplesmente pedir novamente para que essa,

04:48

às vezes não logo em seguida, mas foram

04:52

executadas outras ferramentas, aí aqui eu tenho a ferramenta Y,

04:57

e ela voltou a executar essa ferramenta A, porque

05:02

a LLM mandou.

05:04

Então nós temos que ter consciência que as nossas ferramentas, como sendo essas operações,

05:10

determinísticas, nós temos o controle, nós as programamos, isso

05:15

pode ser executado N vezes durante um turno.

05:19

Então, imagina que fosse um reembolso.

05:22

Eu teria duas tentativas de reembolso.

05:25

Essa primeira teria que dar certo e essa segunda teria que ser descartada ou,

05:31

enfim, produzir um erro. Nesse caso aqui, seria muito mais interessante descartar.

05:39

Mas, de qualquer forma, nós temos que garantir que esse reembolso não seja feito.

05:43

Duas vezes de forma nenhuma. Então,

05:46

por isso que tem o lado de garantirmos a idempotência com

05:49

banco de dados ou com essas ferramentas que nós nos conectamos,

05:53

mas tem a forma de a gente evitar isso através da programação do próprio agente.

06:00

No nosso agente de ticket receptionist, nós temos a ferramenta que vai registrar o ticket.

06:05

Nós temos um artifício que está garantindo uma certa idempotência,

06:10

mas outra deveria ser feita.

06:14

Vamos entender a que já existe e tem a ver com o estado temporário.

06:20

Nós verificamos se existe o

06:24

output key do classificador no

06:27

estado para que assim possamos fazer o registro do ticket.

06:31

Mas como esse output key é temporário,

06:36

ele não sobrevive no próximo turno. Então isso faz com que o agente...

06:47

tentar chamar o registrar ticket vai cair nesse if, porque

06:53

nós não vamos ter a output key

06:57

do classificador no próximo turno.

07:00

Então, isso está me garantindo a idempotência

07:02

através das próximas mensagens enviadas.

07:07

Então, veja que se não tivesse o estado temporário,

07:12

poderíamos muito bem duplicar esse ticket com a classificação, com as mensagens.

07:19

Na verdade, aqui ele iria pegar ainda todo o histórico das

07:27

mensagens agregadas e iria acrescentar com a classificação feita de forma anterior.

07:33

Ficaria de forma incorreta.

07:35

Então, o state temporário serve para nos ajudar nesse sentido, através dos turnos.

07:43

Mas, no mesmo turno, se o agente...

07:48

chamar várias vezes o registrar ticket,

07:52

isso pode acontecer, você pode criar um system prompt ruim,

07:58

você pode ter um modelo que se confunde,

08:02

poderia ser registrar dois tickets, três, às

08:08

vezes a LLM entra ali no loop, ela executa várias vezes, isso é comum.

08:14

Então, como que eu poderia garantir que ele não fizesse esse registro do...

08:20

Ticket várias vezes no turno.

08:24

Uma das formas, não que vai caber exatamente conforme a gente está fazendo,

08:28

é você ter uma chave de unicidade, ter

08:33

alguma coisa que garanta que não fosse duplicado.

08:37

Se a gente tivesse algo na nossa lógica que

08:41

manipulasse uma informação e essa informação XPTO fosse única,

08:47

se eu tentasse criar um novo registro dela, não ia dar certo.

08:52

A gente está falando aqui para o caso de um inset,

08:55

mas obviamente a gente teria que olhar também para casos de update,

09:01

de exclusão, muito que não tem que se preocupar se você já excluiu,

09:06

ele não vai conseguir excluir de novo,

09:08

mas pode às vezes ter outros efeitos colaterais.

09:13

Aqui no nosso caso, como nós geramos o ticket de forma totalmente aleatória,

09:21

então ele sempre criaria... um outro id para ele, mas com as mesmas informações.

09:28

Então nós conseguimos usar esse mesmo artifício do

09:32

state temporário para nos ajudar com essa idempotência,

09:36

porque eu posso chegar aqui em cima e colocar assim,

09:44

ticket created

09:47

key.

09:50

E aí nós vamos usar uma state temporária, porque

09:59

logo depois que eu fiz a criação, nós podemos usar

10:05

o tool context para

10:09

falar que o

10:12

ticket foi criado.

10:19

Então, logo

10:22

aqui em cima, nós podemos fazer uma verificação.

10:25

Se eu não tiver o

10:31

ticket created key em tool context state, ou

10:38

melhor, se eu tiver, a ideia é

10:43

verificar se eu já criei, retorno o status de erro.

10:50

E fala que o ticket já foi registrado,

10:52

não é possível registrar novamente, ou de forma duplicada, enfim.

10:58

Então não importa, se acontecer qualquer problema, nós estamos protegidos.

11:07

Agora tem algo que eu fiz aqui de comentário,

11:13

provavelmente por isso que ele estava dando erro.

11:20

Aí, para poder fazer um teste como esse, nós poderíamos criar um teste

11:26

forçando o System .Prompt, mudando ele,

11:33

ou...

11:35

fazendo um teste automatizado, que é o que nós não vamos fazer aqui.

11:39

Vamos colocar que

11:41

para criar um ticket, pergunte com a mensagem logo em seguida,

11:44

Ative o processo de classificação,

11:48

Chame ou

11:52

Registrar ticket

11:54

Mais duas vezes para testarmos. Pronto.

12:06

Então, ADK

12:09

Apontando o

12:12

Nosso ticket.

12:20

Então, quero...

12:22

Criar um ticket para informar um

12:27

Problema de integração com GitHub.

12:32

Erro 500.

12:34

Ou melhor, foi errado, mas não tem problema.

12:40

Então chamou o nosso agente,

12:43

Registraram o ticket, pronto.

12:49

Então a gente vê que foi invocado mais duas vezes. E

13:00

Aí nós podemos fazer

13:03

Um SQLite 3 com os dados.

13:10

Ele quebrou-se e colou de 3 para a ponta do baseball ainda. Então, vamos

13:15

Lá. Esse último ticket que aconteceu foi com final 3-6, 3-6.

13:23

Então, nós podemos ver pela mensagem que já vemos que é diferente.

13:32

Então, tenho um erro 500. Quero registrar outro ticket.

13:38

Quero criar um ticket com o que nós relatamos.

13:43

Então, só foi criado um.

13:46

Então é isso que nós temos que fazer.

13:48

Nós temos que tomar cuidado tanto na própria execução que está acontecendo.

13:53

Então podemos usar o estado temporário.

13:57

Obviamente, em outras situações, podemos usar um if para ver

14:01

Se lá no banco de dados existe alguma coisa.

14:04

E podemos usar IDs e UNIQUE. Imagine que eu posso ter vários usuários,

14:11

Que estão ao mesmo tempo tentando fazer uma operação,

14:15

E aquela operação só pode ser feita uma vez.

14:18

Então, nesse caso, esses

14:21

Artifícios condicionais, eles podem ajudar,

14:24

Porque às vezes a execução, as execuções concorrentes,

14:28

Uma está executando ali dois segundos, três segundos depois da outra,

14:32

Mas elas podem estar executando ao mesmo tempo, então,

14:36

Com essas ferramentas, nós conseguimos fazer esses locks ou qualquer coisa que seja. Eu não estou aqui para

14:42

Dizer como tem que ser, porque depende exatamente do que você está fazendo.

14:46

A questão é entender que agora é um tipo de software

14:49

Bem diferente do que nós estamos acostumados a desenvolver,

14:53

Porque num cenário determinístico,

14:58

Dificilmente você vai ter uma operação ali naquela execução sendo executada N vezes.

15:07

Que você vai programar, vai chamar um serviço,

15:10

Vai acessar o banco de dados, vai registrar o que precisa.

15:14

Agora nós temos... um fluxo está sendo executado e ele pode ser executado N vezes.

15:23

E você pode ter um sistema impromptu, às vezes, muito bem definido,

15:28

Mas determinados detalhes de como vai ser invocado as ferramentas,

15:33

Nós vimos aquele cenário de pesquisa de satisfação, e aí se tem erro, chama outro,

15:38

Pode-se ter um loop de ser invocado várias vezes.

15:44

E, obviamente, isso... acaba sendo um custo desnecessário.

15:49

Você está indo e voltando com o LLM,

15:51

gastando mais tokens, mas o que importa é a consistência da operação.

15:55

Então você precisa se preocupar com o seu agente,

15:57

com o seu banco de dados, e assim você vai ter essa alta potência.

## Resumo IA

[RESUMO_IA]