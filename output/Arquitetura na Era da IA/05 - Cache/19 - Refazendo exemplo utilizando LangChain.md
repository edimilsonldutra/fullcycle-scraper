Módulo: Arquitetura na Era da IA\
Aula: [Refazendo exemplo utilizando LangChain](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18355)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, nos exemplos anteriores, a gente criou vários arquivos,

00:05

diversos métodos, endpoints, etc.

00:08

Mas agora eu queria consolidar tudo isso utilizando o Langchain em um único

00:12

arquivo com FastAPI de uma forma extremamente simples para você ver como

00:16

é que quase tudo isso que eu mostrei ou trouxe para vocês

00:19

já são coisas que já são extremamente consolidadas e simples de se implementar.

00:26

Eu quis e eu fiz questão de trazer tudo aquilo de uma forma bem crua para você,

00:29

para que você conseguisse entender a ideia e o conceito que está ali por trás,

00:33

sem muita mágica acontecendo. Agora, entrando no mundo da mágica,

00:37

basicamente a gente está aqui. A gente está utilizando o Langchain,

00:42

e você vai perceber que a gente vai utilizar o

00:45

Langchain tanto para fazer comunicação com a IA,

00:48

quanto a Langchain para a gente falar diretamente com o PG Vector,

00:51

para a gente ter toda uma camada de abstração para fazer embed,

00:55

em comparação e tudo mais,

00:56

trazer isso tudo pronto para a gente. Então,

00:58

o que acontece? Tem minhas variáveis aqui de ambiente,

01:01

uma coisa que é importante é essa minha collection,

01:03

isso aqui ele vai utilizar por padrão,

01:05

como se fosse uma espécie de um namespace,

01:07

como se fosse aquele fingerprint, se eu mudar,

01:09

basicamente tudo aquilo vai ser invalidado,

01:13

ou seja, ele vai trabalhar numa...

01:15

como se fosse uma espécie de um outro namespace, ou seja, como se fosse um contexto.

01:20

E aqui eu tenho a categoria, o meu modelo de análise de ticket,

01:26

onde eu tenho a categoria, a confidência e a razão. Aqui eu tenho o request,

01:30

que é a mensagem, e o response, que é como foi feito,

01:34

chamado, se é cache de execução, se é cache semântico ou AI model.

01:39

Eu tenho a quantidade de chamadas, eu tenho o tempo que demorou,

01:42

a similaridade de quanto foi,

01:45

o threshold de quanto foi, e o resultado, que é a minha análise de ticket,

01:50

que no final das contas é esse modelo aqui de cima. Então,

01:53

é basicamente isso que ele tem. Eu tenho o prompt,

01:55

mas agora, olha só que interessante.

01:57

Eu falo o seguinte, LLM é igual a init chat model,

02:02

passo que é o OpenAI, falo qual que é o provider, a temperatura zero.

02:07

E estou falando que o meu analyzer vai chamar esse meu provider,

02:12

passando aqui a estrutura que

02:17

ele vai ter que analisar,

02:20

que é o nosso ticket analysis. Então, quando ele rodar isso aqui para a gente,

02:24

ele vai pegar o nosso prompt, no final das contas,

02:26

e vai rodar esse cara para basear esse cara em cima desse resultado aqui.

02:33

Ou seja, ele vai preencher esse esquema.

02:36

para a gente ter como resultado. Ou seja,

02:38

ele vai pegar o resultado do LLM e vai

02:40

fazer com que esse resultado preencha os campos desse esquema.

02:45

Agora, a parte mais interessante, aqui, Vector Store, é um PG Vector,

02:50

onde eu falo qual é o meu modelo de embedding,

02:52

o nome da minha coleção, a minha URL de conexão,

02:56

e aqui é onde eu seto o meu cache local, o meu cache exato. Ou seja,

03:02

Eu tenho um dicionário com o string, que vai ser a minha chave,

03:04

e o ticket analysis é o valor, que é o resultado, né?

03:08

Que tá cacheado aqui pra mim. AI calls, zero,

03:13

e a minha função de normalização aqui pra gente.

03:15

Um monte desses coisas aqui é log de como que eu

03:18

acabei colocando aqui pra ficar mais simples pra gente ver.

03:21

Ou seja, tudo isso aqui é log,

03:22

mas aqui que é o ponto mais importante da nossa API, tá? Então,

03:26

a nossa API vai funcionar da seguinte forma. Quando alguém acessar /tickets,

03:29

/analyze, a gente vai receber o request, que vai ser a mensagem,

03:34

e a response, que vai ser a resposta que a gente vai trazer.

03:38

Então, aqui a gente começa normalizando a quantidade

03:42

de chamadas da IA e também o tempo,

03:48

quando começou o contador do nosso tempo.

03:50

E aqui eu tenho uma função dentro de uma função que é chamada de respond.

03:55

O que essa função aqui faz no final das contas?

03:58

Ela vai pegar um source para dizer se é AI model, se é cache,

04:02

se é análise semântica, vai pegar o resultado, que é o meu ticket análise,

04:08

a similaridade, e vai trazer isso aqui no formato de response.

04:13

Por que eu tenho essa função aqui dentro no final das contas?

04:17

Porque essa função, ela simplesmente vai fazer o seguinte, olha...

04:21

Se o tipo de source for por similaridade aqui, por exemplo,

04:25

se a minha similaridade for zero,

04:27

quer dizer que eu nem passei pela minha busca vetorial.

04:31

Legal? Agora, caso não seja zero,

04:34

significa que foi uma busca semântica por conta que

04:38

a gente teve algum resultado de cache aqui,

04:40

porque eu tive um valor na minha similaridade. Legal?

04:45

E caso isso tenha acontecido, ele vai pegar...

04:49

e vai gerar esses resultados nesse formato para eu conseguir ver depois.

04:54

E vai retornar para o usuário final o response que eu queria.

05:00

Agora, por que eu tenho essa função aqui? Porque vai ficar assim.

05:04

É aqui que, na realidade, a mágica mora.

05:06

Se a normalização estiver em cache exato, ou seja,

05:11

se aquela chave de normalização já existe,

05:14

o que ele vai falar? Ele vai falar exec cache e vai retornar.

05:19

o valor que a gente já tinha ali normalizado.

05:22

Ou seja, acabou, ele responde por aí. E por isso que ele dá um return respond,

05:27

porque o respond é exatamente essa função aqui onde ele faz esse tratamento.

05:32

Aí eu tenho o 2, que é cache semântico.

05:36

Então, se a similaridade, daí ele coloca a similaridade é 0,

05:40

aqui é none, e aqui ele vai fazer um match.

05:42

E aqui ele vai fazer o quê?

05:44

Ele vai fazer uma busca no banco de dados por relevância, baseado em score,

05:48

com o texto normalizado e pegar o primeiro

05:51

resultado que tem mais match para a gente trabalhar.

05:57

Se houve match e essa similaridade que ele trouxe também bateu o nosso threshold,

06:04

o que ele vai fazer? Ele vai retornar, falando que é um semantic cache,

06:08

trazendo o resultado da análise baseado nos dados que ele retornou,

06:13

que é no best data com os metadados, baseado na similaridade. Agora,

06:20

Caso não tenha sido o cache exato, caso ele não tenha batido no banco de dados,

06:25

isso significa o quê? Que foi um cache miss,

06:28

tanto no cache exato quanto no cache semântico.

06:32

Então, o que ele vai fazer? Ele vai dar um analyzer.invoke.

06:36

E o que isso é? Analyzer.invoke?

06:39

Lembra aqui em cima, onde nós tivemos um LLM?

06:46

A analyzer é igual a llm.withStructureOutput, que é ticket analysis.

06:52

Basicamente, quando eu dou um invoke aqui, eu estou chamando a IA nesse momento.

06:58

Então, eu estou chamando a IA,

06:59

estou passando o meu prompt, estou falando qual é a mensagem do humano,

07:04

e aqui eu tenho, então, exec cache,

07:08

estou pegando a mensagem normalizada e salvando esse dado no cache local.

07:13

E ao mesmo tempo...

07:15

Eu estou pegando essa mensagem e guardando no

07:19

banco de dados com os metadados que eu quero.

07:23

Então, olha só que interessante, galera.

07:26

Com uma chamada, eu guardei isso no cache e aqui eu salvei no meu banco de dados.

07:31

Perceba que esse meu vector store.addText já é algo

07:36

extremamente pronto que já vem aqui do Langchain para mim,

07:39

por exemplo, com o pgVector, onde eu passo o texto normalizado. E os dados,

07:44

eu peguei o resultado de tudo o que aconteceu e dei um model dump

07:48

em JSON para ele salvar no banco de dados essas informações ali em JSON.

07:53

E aí, o resultado é AI model. Então, eu tenho três possíveis resultados.

07:58

Execute cache, eu tenho cache semântico, ou ele deu um miss nos dois,

08:02

então o tipo é AI model que ele vai trabalhar aqui para a gente.

08:07

Então, se você perceber... Virou um programa extremamente pequenininho,

08:10

porque eu tenho um endpoint simples aqui,

08:13

simplesmente para filtrar o tipo de resultado na forma de saída,

08:17

e eu tenho os meus três situações que eu trabalho.

08:21

E no final das contas, tudo isso aconteceu porque aqui em cima,

08:25

eu com quatro linhas, eu estou cuidando de toda a parte do meu banco de dados,

08:29

e aqui com duas linhas,

08:31

eu setei já um cara prontinho para fazer a chamada para o meu modelo aqui para mim.

08:37

Então, se você perceber, quando eu estou trabalhando com framework, a vida aqui,

08:41

nesse caso, a coisa vai para um outro patamar.

08:44

Acaba ficando muito mais simples, né? Então, se eu chegar aqui em teste.http, eu

08:50

tenho aqui, deixa eu dar um enter aqui, eu posso fazer a primeira chamada,

08:55

tenho dúvida sobre cobrança na minha fatura. Então, vou dar um enviar,

09:03

prontinho. Então, nesse caso, ele deu um miss nos dois caches,

09:07

chamou a IA. Então, a mensagem foi isso, normalizada,

09:10

nenhuma similaridade, porque não teve nenhum candidato.

09:13

O resultado de confiança é esse.

09:15

Teve que fazer uma chamada de IA.

09:18

Beleza. Agora, o que eu vou fazer? Eu vou mandar a mesma mensagem. Então,

09:23

vamos lá. Mandei a mesma mensagem e agora eu tenho um exec cache hit.

09:27

Ou seja, ele respondeu da memória, não chamou a IA e respondeu de cara.

09:32

A gente nem precisou bater no banco de dados também para fazer essa pergunta.

09:36

E agora... eu tenho basicamente a mesma mensagem,

09:40

mas com uma normalização diferente, bateu de novo no cache hit,

09:45

porque quando normalizou, virou a mesma mensagem.

09:48

Com a mesma fingerprint, não precisou bater no banco.

09:51

Agora, eu tenho uma mensagem parecida, mas ela não é idêntica. Então,

09:56

Estou com dúvida sobre a cobrança da minha fatura. Você pode me ajudar?

10:00

Então, quando eu bater agora aqui, o que vai acontecer?

10:04

Ele... Deu um semantic cache hit. Ou seja, ele reaproveitou a mensagem do PG Vector.

10:10

E está aqui, estou com uma dúvida. A similaridade dele aqui deu 0.93.

10:15

O threshold dele era acima de 0.9. Ou seja, ele teve 0.5 de confiança.

10:20

Teve uma chamada para minha IA aqui nesse momento. E agora,

10:25

Se eu coloco um assunto diferente, não consigo acessar a minha conta.

10:30

Aí, deu um miss nos dois caches, porque ele nunca tinha trabalhado. E aí,

10:34

Se eu volto e faço uma busca, não estou conseguindo acessar minha conta.

10:40

Aí, ele dá um semantic cache hit,

10:42

Porque ele aproveitou aquela chamada anterior que ele tinha dado miss,

10:45

Mas como é parecido,

10:47

Ele consegue trazer. Então,

10:48

Ele buscou no banco de dados e não precisou chamar a IA aqui de volta para a gente.

10:53

Então, e assim vai, galera. Assim vai. Então,

10:56

Tem diversos exemplos aqui. Vou chamar,

10:58

Deu miss nos dois caches. Daí, vou fazer de novo a chamada. Então,

11:04

Se você perceber,

11:06

Esses tipos de coisas são extremamente importantes,

11:12

Principalmente quando você começa a entender o que está acontecendo por trás.

11:17

Eu poderia ter chegado aqui e ter criado um arquivo com

11:21

Meia dúzia de linhas e mostrado isso para você.

11:24

Mas eu queria te mostrar,

11:25

Por baixo dos panos, o que era um embedding, como era um vetor, como ele saía,

11:29

Quais eram as possibilidades. E agora,

11:32

Eu acredito que depois que você tenha tido aquela base...

11:37

Daqui pra frente usar um Langchain ou qualquer

11:39

Outro framework ou qualquer coisa desse

11:41

Tipo já vai te ajudar bastante porque dá pra perceber que o trabalho pra

11:47

Fazer coisas desse tipo acaba sendo cada vez ali mínimo irrisório perto daquilo que

11:53

Acontece caso você tenha feito ali de

11:57

Forma manual como a gente fez antes, tá?

12:02

Então, espero que você tenha curtido essa parte e a

12:04

Gente tem que falar de cache de providers, tá?

12:07

Porque começa a entrar num outro mundo e que acaba confundindo muita gente também,

12:12

Beleza? Então, vamos nessa.

## Resumo IA

[RESUMO_IA]