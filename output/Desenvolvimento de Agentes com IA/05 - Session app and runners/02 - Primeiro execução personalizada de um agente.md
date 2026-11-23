Módulo: Desenvolvimento de Agentes com IA\
Aula: [Primeiro execução personalizada de um agente](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18477)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos fazer a primeira execução personalizada de um agente. Até o momento,

00:05

nós rodamos sempre com ADK Run e ADK Web,

00:08

mas isso é somente para desenvolvimento, para debug.

00:14

O nosso projeto vai ser alguma capa com CLI,

00:17

com desktop, com web, com qualquer coisa que seja,

00:21

e isso vai permitir a interação do usuário de um sistema com o agente.

00:25

Então, vamos supor que nós estivéssemos criando aqui um programa executável...

00:31

diretamente no terminal.

00:33

Então eu vou criar aqui dentro um main.py e aqui não importa,

00:38

isso aqui não poderia ser na raiz, em qualquer pasta, o ADK não me impõe nada.

00:46

Então a primeira coisa que eu preciso definir é qual é o gerenciamento da sessão,

00:50

qual é o gerenciador da sessão. Então de google.adk.sessions eu

00:56

vou importar WinMemorySessionService,

01:02

que vai me permitir gerenciar as sessões do meu agente em memória.

01:08

Então isso vai ficar na memória RAM. Uma vez que o meu programa finaliza,

01:13

então eu perco tudo que está ali, se eu não vier a salvar.

01:17

Então isso aqui serve muito para testes, para ambiente de desenvolvimento.

01:23

O próximo passo é criar o runner. Então de google.adk eu

01:30

vou importar Runner.

01:34

Lembra que eu falei... Na aula anterior,

01:37

que nós não executamos o agente de forma direta,

01:41

eu chego aqui e faço, apesar de ser possível,

01:44

uso run ou run async. Nós

01:49

temos o, vamos colocar assim, o executador. Runner é isso.

01:55

Ele vai criar já o ambiente para que a gente não consiga,

02:00

para que a gente não tenha a responsabilidade de ficar gerenciando o agente.

02:05

Então vou criar a instância desse runner, tenho

02:09

que passar qual é o nome do meu projeto,

02:12

o app name, podemos deixar como operador de conta,

02:17

não precisa ser o mesmo nome aqui do agente que nós vamos utilizar,

02:22

e o session service, então o runner acaba usando

02:28

esse gerenciamento da sessão, conectando com o agente.

02:32

Para o runner poder executar o agente,

02:34

nós necessitamos de duas coisas. Uma mensagem,

02:37

que na verdade nem é obrigatória, é opcional.

02:41

Podemos executar o agente sem passar a mensagem.

02:44

E a sessão.

02:49

Como nós já temos o SessionService,

02:51

vamos criar a sessão

02:53

a partir do SessionServiceCreateSessionSync.

02:59

Nós vamos ver esse outro aqui depois, que é o CreateSession, que é o Async, mas...

03:07

Esse síncrono é o que precisamos no momento.

03:11

Vamos passar o app name, ele vai precisar para poder fazer o namespace,

03:18

ele armazena toda a sessão no namespace.

03:20

Como nós já temos um app name no runner,

03:22

podemos reusar essa informação. E qual é o user ID?

03:29

Que nós usamos muitas vezes, na verdade acho que em todos, o cliente123.

03:35

Isso aqui não tem influência nenhuma na execução do agente,

03:38

mas é só para relacionar com o que nós já tínhamos feito.

03:41

Então, está aqui a nossa sessão.

03:44

Agora vem o conteúdo da mensagem.

03:48

Este conteúdo é

03:52

formado a partir de um tipo que vem junto com a ADK,

03:57

que está no Google Jam AI, que nós podemos trabalhar com vários formatos, que é o Types.

04:06

Então, de... Types, nós vamos criar a mensagem.

04:09

Eu não posso colocar uma lista minhas faturas diretamente,

04:13

ele não aceita dessa forma. Então, de types.content, nós

04:19

vamos passar duas informações. Primeira, qual é a role do conteúdo?

04:24

Se é usuário, ou seja, usuário que produziu esse conteúdo, ou model,

04:30

que significa que é a LLM que produziu. Lembra lá do ADK?

04:35

web que nós fizemos a inspeção,

04:37

tinha parte lá de partes com todos os conteúdos,

04:42

a cada turno nós

04:45

tínhamos esse histórico, esse histórico acaba indo para a LLM.

04:49

Então tem a ver com o que nós estamos fazendo aqui.

04:53

Então de role, ou

04:56

melhor, de role não é model, eu tinha mudado para model,

04:59

é user, aí vem partes, que eu posso passar múltiplas mensagens.

05:06

Veja que na hora que você está interagindo com o seu agente de IA,

05:09

você pode passar uma imagem junto com o texto,

05:12

fazer uma miscelânea de conteúdo. Então, nós podemos fazer essa mesma coisa aqui.

05:16

Mas eu só vou passar apenas uma mensagem.

05:18

Então, de types.part.fromText,

05:26

eu quero

05:30

listar minhas faturas, que

05:36

precisa ser o parâmetro nomeado.

05:41

Nós temos vários outros, olha que interessante, se eu colocar aqui from,

05:45

tem from text, from bytes, from code execution result, enfim, pronto.

05:56

Aqui ele deu um erro do user ID que eu não coloquei vírgula aqui.

06:02

Então agora nós podemos fazer um runner,

06:05

ponto run, passando o

06:10

session ID, que nós pegamos ali da sessão, nós temos...

06:15

muitas coisas nesse objeto, tem o id, os eventos, o app name, modo config, state.

06:23

Então, passo o session ID, o

06:28

user ID, nós vimos ali que é possível também pegar da sessão, e

06:34

o new message, que é a mensagem, a primeira mensagem que eu estou passando.

06:39

Na verdade, eu coloquei errado aqui.

06:42

Nós estamos trabalhando em português.

06:47

Então, isso aqui vai acabar.

06:49

adicionando o contexto da invocação e

06:53

aí o agente vai começar a rolar.

06:57

Poxa, mas aonde que eu conecto o agente?

07:04

Nós temos o root agent aqui nesse arquivo, então aqui em cima de

07:11

agents.operador.session.agent

07:17

vamos importar o root agent.

07:21

Então aqui juntamente com

07:23

os outros dois parâmetros no runner nós vamos informar para ele qual é o agente.

07:30

Então aqui vem agente, root agent. Ok.

07:36

Então agora não falta nada.

07:38

Mas aqui nós poderíamos de forma ingênua colocar uma response.

07:44

Mas nós já vimos no ADK Web que quando nós fazemos a invocação...

07:50

Aí vai para o agente, do agente vai para a LLM, a LLM e o agente fazem alguma coisa,

07:56

aí manda para a LLM de volta, pode fazer o transfer to agent,

08:03

enfim, nós podemos ter N coisas acontecendo.

08:07

E cada uma dessas coisas vai ser os eventos.

08:10

Lembra lá no topo da parte da esquerda que

08:14

tinha a coleção dos eventos que nós navegamos,

08:18

na verdade, muitas vezes durante as aulas? Pois é.

08:22

São os eventos que estão acontecendo.

08:25

Então, quando ele terminar, ter ali a resposta final,

08:29

vai ser o último evento que aconteceu.

08:32

Nós não sabemos quando esse último evento vai acontecer. Nós podemos, às vezes,

08:39

ter seis eventos sendo executados nessa invocação e em outra cinco, em outra três.

08:46

Então, nós vamos recebendo aqui desse run uma série de eventos,

08:52

na verdade.

08:54

E esses eventos vão acontecendo ali

08:58

em tempo real.

09:01

Então, na verdade, aqui nós passamos um for, porque

09:07

nós vamos receber uma turminha desses eventos. E a questão,

09:12

eu vou até colocar aqui um print do evento que está sendo recebido.

09:17

Nós só estamos interessados no evento final.

09:22

Então, do evento, nós temos muitas informações, mas são muitas.

09:26

Nós poderíamos verificar o que é que tem,

09:29

se é tool call e mais um monte de outras coisas.

09:32

Mas tem um isFinalResponse que a

09:38

IA já está sacando que é o que eu quero, que

09:42

mostra se é o evento final, que é a resposta que a LLM vai mandar para a gente,

09:48

que ela processou, está aqui o resultado. Então,

09:53

a partir deste evento, temos o conteúdo.

09:59

E conteúdo partes, como aqui em cima. É um tipo que lida com o mesmo formato.

10:06

Nós vimos isso lá no ADK, vai sendo acumulado as partes.

10:09

Então, nesse evento específico, eu

10:13

vou ter uma resposta de texto, eu

10:17

consigo pegar partes na posição 0 .text, porém,

10:23

eu posso não ter o conteúdo que ele pode ser None,

10:26

posso também não ter partes que ele pode ser None.

10:29

Então, nós vamos fazer um if.

10:31

Se event content e partes,

10:37

aí nós colocamos aqui a resposta final. Pronto.

10:42

Veja, essa aqui é a execução

10:45

personalizada de um agente. Vai ser parecido com isso em qualquer outro projeto,

10:52

só que nós vamos tender a trabalhar com paradigma assíncrono,

10:55

mas não vamos falar, nós não vamos focar nesse assunto nesta aula.

11:01

Então, eu vou executar um Python apontando para esse main.py. Olha só.

11:13

Ele disse que não conseguiu encontrar o API key.

11:17

E aqui nós já vemos as facilidades que o DKRun e o DKWeb fazem.

11:24

Por padrão, ele vai na raiz do projeto, tanto um como o outro,

11:29

e lê o meu .env que tem a minha Google API key.

11:34

Então, neste projeto...

11:37

melhor, nesse arquivo,

11:39

eu vou importar o .env que é a biblioteca que vai

11:43

me permitir carregar as variáveis de ambiente aqui do meu arquivo.

11:48

Então logo no princípio nós fazemos isso.

11:51

Então ela por padrão já faz o carregamento e nós temos que fazer de modo manual.

11:57

Ou melhor, opa, eu executei outro agente. Pronto.

12:07

Então veja só,

12:08

eu tenho muito conteúdo que aconteceu aqui justamente para poder demonstrar.

12:14

porque nós temos um print antes

12:19

executar esse if, foram os eventos. Então, tivemos aqui o primeiro, listar faturas.

12:31

Aí depois teve mais um, para listar suas faturas,

12:36

por favor, me informe o id.

12:42

Nós tivemos esses dois eventos que aconteceram.

12:46

Então, não tem como garantir, poderia ser 3, 4, 5. Então, nesse for...

12:52

Nós vamos capturando os eventos e a partir das

12:55

informações do evento nós vamos entender o que é.

12:59

Nós estamos focados aqui no final response para dar a resposta final.

13:03

Mas o evento poderia ser que o usuário precisa ativar,

13:09

precisa dar permissão lá no toolpol.

13:15

Aí eu poderia pegar, formatar bonitinho um botão,

13:20

quando o usuário clicasse ia voltar aqui para o...

13:25

meu projeto, meu software, iria continuar a execução.

13:31

Nós vamos ver ainda como reiniciar a sessão novamente,

13:36

como

13:39

manuseá -la através de toda a interação que o usuário vai fazendo,

13:44

mas aqui é só para ter essa primeira noção de como as coisas funcionam.

13:50

Então, no final das contas,

13:51

ODK Run e ODK Web estão fazendo exatamente isso aqui.

13:58

Eles já estão criando para você o gerenciador da sessão,

14:02

o runner, e já lá com a execução totalmente pronta.

14:07

Você só está preocupado em mandar a mensagem e ver as informações,

14:12

fazer o trace, fazer o debug, ver tudo o que está acontecendo.

## Resumo IA

[RESUMO_IA]