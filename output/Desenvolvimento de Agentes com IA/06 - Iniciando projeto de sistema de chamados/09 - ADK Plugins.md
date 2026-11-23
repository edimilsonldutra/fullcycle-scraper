Módulo: Desenvolvimento de Agentes com IA\
Aula: [ADK Plugins](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18564)

## Resumo da aula



## Transcrição

00:00

Nesta aula nós vamos falar sobre plugins.

00:03

Plugins é um recurso do ADK que

00:06

permite colocar os hooks dentro de uma classe.

00:12

Então nós criamos tudo em loco e podemos reusar através dos nossos agentes.

00:18

Então dentro de um plugin nós podemos colocar before run,

00:21

before agent, after agent, before model, podemos colocar um conjunto,

00:26

para atender alguma necessidade.

00:28

O legal é que a gente vai reusando ele através dos agentes,

00:32

ele não é específico para um agente.

00:35

Eu posso criar um plugin e reusar diante de todos os agentes que eu tenho.

00:41

Ele serve para que nós possamos mudar comportamento, fazer log dos dados,

00:47

preparar alguma coisa, interferir. Nós falamos isso na aula anterior,

00:53

olhando para o BeforeModel, por exemplo.

00:57

Nós podemos ver se um tipo de request vai acontecer.

01:02

Nós já temos a resposta para ela. Não precisa ir lá para a LLM.

01:06

Tem também o uso dos eventos, que é muito poderoso.

01:09

Podemos capturar todos os eventos, fazer log,

01:12

mudar este evento, adicionar mais dados,

01:16

adicionar delta de estado, enfim, fazer um monte de coisas. Então,

01:19

a ideia para mostrar esse plugin funcionando é pegar a ideia da última aula.

01:26

e criar um plugin para isso.

01:28

Eu já fiz toda a transformação nesse arquivo aqui de plugins.py com

01:36

todo o comportamento. É a mesma coisa, porém está em uma classe.

01:38

Então nós criamos um plugin dando um nome,

01:41

estendendo de base plugin do próprio ADK, e

01:48

aí tem que ser definido quais hooks que você vai interceptar.

01:52

Então tem o beforeModelCallback, afterModelCallback e o afterAgentCallback.

01:59

todos trabalhando em conjunto.

02:01

A diferença é que antes nós tínhamos aquela variável das requests pendentes,

02:07

ela ficava fora, agora ela fica dentro da própria classe para poder gerir.

02:13

Eu até coloquei o isEmptyResponse fora, mas poderia ficar dentro também.

02:18

Tem o log que tem que ser colocado e o node, que

02:22

é aquela mensagem para forçar o modelo a responder alguma coisa.

02:25

Está fora isso que está fora. Tudo poderia ficar dentro, na verdade, do...

02:29

plugin se a gente quisesse. Mas agora, a forma de encaixá-lo,

02:33

eu comentei os hooks que eu tinha feito na aula anterior,

02:36

a forma de encaixá-lo é no app. E essa é uma diferença interessante,

02:41

porque uma vez que eu tenho o hook no agente, ele fica preso,

02:45

apesar de eu poder criar uma função que é reusável,

02:49

a gente consegue até passar uma lista desses callbacks, mas

02:55

você acaba fazendo assim, que às vezes é um comportamento mais genérico.

03:00

E aí você acaba usando,

03:01

queimando ali a questão do seu hook interno para colocar um callback. Então,

03:08

um plugin é bem melhor porque nós conseguimos

03:11

até mesmo testar esse agente sem esses hooks,

03:16

porque nós podemos levantar apenas o agente, fazer alguns testes diretos. Inclusive,

03:23

a gente até consegue falar ali para o Odeka Run e o app.

03:27

Posso até comentar o app.

03:29

e não usá-lo. Então, nós colocamos aqui plugins e chamamos o plugin.

03:35

Então, vamos lá para o plugin de retry do modelo.

03:41

Temos que iniciá-lo dessa forma.

03:44

Ele vai exigir que eu coloque um nome,

03:46

mas o nome nós podemos até passar aqui com init.

03:52

Vamos fazer aqui o self name.

03:57

Aí podemos dar o nome de Model Retry Plugin.

04:03

É a identificação dele. Pronto.

04:07

Então, na verdade,

04:09

aqui nós podemos colocar o nome igual a nome,

04:14

porque senão ele vai chiar.

04:22

Pronto. A

04:29

gente pode deixar dessa forma aqui o nome ou o próprio nome default. Ok.

04:37

Então, imaginando que a gente não tem nenhum código como esse aqui,

04:41

também ia ficar bem melhor.

04:43

Aí agora vem um pouco da luta. Aqui é aleatório.

04:48

Eu vou tentar novamente brincar com Ticket Receptionist quando acontecer um retry.

04:56

Nós vamos ver aqui no terminal.

04:58

Usando o Gemini 2.5 Flash não é tão difícil de fazer.

05:02

Deu certo até rápido. Então temos aqui o warning e a primeira tentativa.

05:07

Nós temos cinco tentativas, são muitas.

05:11

Então esse comportamento está dentro do plugin.

05:13

Então imagine situações genéricas que você poderia

05:17

ir reutilizando através do seu agente,

05:19

e não somente coisas que você poderia reutilizar.

05:26

Mas nós podemos usar plugins específicos para aquele agente também.

05:30

Então tem um comportamento que você quer mudar,

05:33

alterar, para não ficar usando os hooks.

05:36

Pode ser até usar os plugins de forma padrão.

05:41

Porque fica até legal, a gente consegue testar de forma separada,

05:46

enfim, nós podemos criar a malha de plugins e adicionar no app.

05:50

E o plugin tem um comportamento diferente de um hook,

05:54

que enquanto o hook está intrínseco no agente,

05:58

o plugin é espalhado para todos os agentes daquele app. Então,

06:04

como nós temos o Ticket Receptionist e o Ticket Classifier,

06:09

esse plugin vale para ambos. Enquanto em um callback, imagina, eu coloco aqui,

06:15

se eu quisesse fazer com que esse comportamento fosse padrão

06:17

para todos os agentes e não usasse plugin,

06:20

eu teria que colocar sempre todas as funções em todos os agentes.

06:24

Daria muito trabalho para ficar fazendo até uma

06:28

lista de quais callbacks nós podemos colocar. Você chega lá no app,

06:32

declara e pronto. Então, lembra do que nós falamos de o app é o blueprint?

06:40

Ele cria o contrato,

06:42

depois o runner fica responsável por espalhar isso para todos os agentes,

06:48

através da execução do runner. Então, aqui agora nós temos o nosso plugin, ele não é obrigatório,

06:55

mas eu vou deixar ele aqui como referência para que você lembre do

06:58

conceito e também possa criar os seus ou até reutilizar esse se você quiser.

## Resumo IA

[RESUMO_IA]