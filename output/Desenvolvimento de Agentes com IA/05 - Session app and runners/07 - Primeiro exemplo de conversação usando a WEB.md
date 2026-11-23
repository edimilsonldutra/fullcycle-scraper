Módulo: Desenvolvimento de Agentes com IA\
Aula: [Primeiro exemplo de conversação usando a WEB](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18482)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos voltar para a nossa aplicação web e criar um

00:04

exemplo como se fosse um ChatGPT ou um Cloud AI,

00:08

qualquer coisa que a gente consiga fazer aqui um ChatGPT.

00:14

Acho que a gente consegue, antes a gente até conseguia entrar sem conta,

00:19

mas enfim, você já entendeu a ideia. Nós vamos mandar

00:25

mensagens e vamos ter a resposta da LLM.

00:31

Então... Qual é a primeira coisa que é necessária para que eu inicie uma conversa? Nós já vimos aqui.

00:38

A mensagem, obviamente, mais importante do que a mensagem, uma sessão.

00:45

Eu preciso, essencialmente, do ID dela, que está aqui exatamente nessa linha.

00:52

Então, veja, eu posso fazer a criação de uma rota,

00:56

POST, para trabalhar com as boas práticas do REST,

00:59

e tenho aqui um POST da sessão.

01:02

Então vou criar um async def, criar sessão

01:08

exatamente com o código que está aqui.

01:13

Passo o app name do runner que está definido sempre,

01:17

já está instanciado quando a

01:21

aplicação iniciar. O ID do usuário a gente poderia pegar aqui de várias formas,

01:27

independente de você estar trabalhando com qualquer meio de autenticação,

01:33

não importa. A gente não vai entrar nesses detalhes.

01:37

Mas para quem está se comunicando com essa API,

01:43

se a gente tivesse feito uma aplicação front-end,

01:47

ela precisaria do ID da sessão para

01:52

que nós pudéssemos passar uma mensagem depois. Então nós estamos aqui com o

02:00

SessionService em memória.

02:02

Ok, eu já salvei.

02:04

Agora eu vou utilizar uma extensão aqui no meu VSCode, que é o REST Client,

02:10

se você quiser fazer os testes da mesma forma que eu.

02:13

Então nós podemos criar um

02:17

API .http e fazer um POST

02:21

para http://localhost na porta 8000/sessao,

02:28

que foi o que nós criamos.

02:30

Então ao fazer isso aqui, ele gera... o ID da sessão,

02:36

que é um UUID. Esse é o padrão dele.

02:41

Então, ele está armazenado em memória. Enquanto a

02:45

gente não atualiza... Cuidado, porque se você mudar o código,

02:50

salvar qualquer coisa, ele faz o restart,

02:54

você vai perder o que você tem na sessão.

02:56

Nós não estamos armazenando no banco de dados.

03:00

Cada vez que eu fizer uma

03:03

nova chamada, ele retorna um ID de sessão.

03:07

Então a ideia é que nós tenhamos

03:10

uma rota para poder enviar a mensagem.

03:15

Então vamos fazer algo nesse modelo. Com content type, application/json,

03:21

e aqui eu passo a mensagem que é minha lista de faturas,

03:27

como nós tínhamos feito antes.

03:31

Então aqui nós vamos criar mais uma rota, que

03:37

vai ser a mensagem. E aqui nós vamos receber essa mensagem,

03:41

até porque a gente já vai se acostumando com outra biblioteca que

03:46

é muito importante, já vem nesse contexto do SDK, que é o Pydantic,

03:50

que ela já era uma biblioteca muito importante antes do

03:54

ADK e agora vem com mais destaque ainda.

03:57

Eu já tinha falado sobre ela,

03:58

Ela permite que você faça modelagem de dados no Python,

04:03

Validação, trabalhe com o padrão Data Class, que é algo do Python, enfim.

04:09

Ela já era usada por grandes empresas e agora com a adoção no ADK,

04:16

Vai só expandir mais. Então,

04:19

Quando eu estou recebendo dados do meu POST,

04:23

Eu posso modelar esses dados. Vamos colocar aqui uma classe,

04:34

Mensagem Request. Ela

04:39

Vai ser do tipo BaseModel, que é um tipo do Python,

04:43

Que eu já vou importar aqui em cima.

04:45

Que o VS Code já me ajudou. Então, eu vou colocar que eu recebo a mensagem.

04:51

Ela já vem bonitinha nesse objeto, dado o que eu vou passar na minha request.

04:57

Então, aqui nós podemos colocar que

05:01

Eu vou receber uma request que é do tipo mensagem.

05:05

O legal de trabalhar dessa forma aqui é que se eu não passar essa mensagem,

05:09

O FastAPI já trabalha com o Pydantic também. O ADK também trabalha.

05:16

Então, receberia uma mensagem de validação, enfim.

05:24

Então, recebendo essa mensagem, o que nós vamos fazer? Eu não preciso fazer

05:33

Todo esse processo aqui, eu preciso criar essa ação,

05:37

Mas vou precisar capturá-la para dar continuidade.

05:41

Então, eu vou copiar esse trecho primeiro, tem o conteúdo da mensagem,

05:46

Então aqui vai ser requestMessage, eu vou passar.

05:51

A IA já identificou. Agora, eu preciso identificar a sessão.

05:56

Então, nós vamos fazer um await sessionService.getSession.

06:03

Imagina esse sessionService como se fosse um repositório do seu RM.

06:08

Nós temos métodos para poder criar a sessão, pegar a sessão, excluir a sessão.

06:13

Você está vendo aqui, listar as sessões. Enfim,

06:16

Você consegue fazer tudo com as sessões.

06:19

Então, na hora de pegar essa sessão, eu preciso passar alguns parâmetros.

06:28

Primeiro deles, qual é o ID da sessão?

06:31

Então, nesse caso, eu preciso passar o ID da sessão aqui sempre na mensagem também.

06:36

Então, eu vou acrescentar o

06:39

session_id. Então, aqui eu passo. Session ID vai ser igual a request.session_id.

06:46

Qual é o user ID? Que nós não temos nada dinâmico,

06:49

Eu vou continuar mantendo o mesmo.

06:52

Aqui, quando eu criei, eu usei o cliente em 2.3, então está certinho.

06:58

E por último, o app name.

07:01

O app name pegamos do runner. Então, pronto.

07:08

Tenho a sessão,

07:10

Então, copio esse trecho e

07:17

Vai ser a mesmíssima coisa.

07:25

Aí aqui eu preciso só alinhar o código.

07:33

E nós vamos ter um erro, porque o getSession...

07:38

Vai ser uma coroutine, eu colocando await, nós vamos fazer

07:45

O processamento, depois que ele terminar, coloco o resultado aqui. Então,

07:50

Veja que no retorno, podemos receber, isso aqui é o retorno que

07:56

É armazenado na variável que eu vou colocar ali.

07:59

Eu recebo a sessão ou não recebo nada, porque eu posso passar um ID inválido,

08:04

Essas informações podem não bater com o que está armazenado, e ele retorna None.

08:09

Então, por segurança, eu coloco uma nova sessão, se eu não tiver a sessão,

08:16

eu coloco sessão não encontrada, que é assim que o chat.pt,

08:20

cloud.ai vai acabar fazendo. Então, eu não tenho nenhum erro,

08:25

um código bem simples de entender. Então,

08:29

eu crio o conteúdo, recapturo a sessão, enfim.

08:35

Então, aqui vamos...

08:40

Vou ver se está tudo ok primeiro no terminal.

08:43

Faço a criação da

08:46

sessão, então agora eu passo a sessão, acho

08:51

que foi assim que eu coloquei, né?

08:53

Coloquei sessão,

08:57

na verdade session ID, né?

09:00

Eu já ia errar session ID passando esse valor. Pronto.

09:06

Então aqui eu coloco três hashtags e vamos fazer a chamada. Está vendo aqui embaixo?

09:13

A waiting é

09:15

para listar as faturas. Por favor, me informe o ID do cliente. Então,

09:20

significa que deu certo. Agora, nós podemos enviar a próxima mensagem.

09:27

Vamos colocar cliente 123. A

09:38

waiting tem, obviamente, a latência,

09:40

que já é um problema que nós vamos ter que lidar com as nossas aplicações.

09:43

Está aqui a

09:46

listagem das

09:50

nossas faturas. Então, veio como um texto.

09:53

Nesse formato que a gente teria que colocar onde quer que seja,

09:57

mas isso não importa. Agora,

10:00

se eu dou um Enter, ele

10:05

vai recarregar, como vocês viram aqui.

10:10

Se eu enviar uma mensagem novamente, usando esse ID,

10:15

ele vai mostrar se está sendo encontrado.

10:16

Então, até bom ter um IF como esse, para

10:21

que nós não tenhamos surpresas, principalmente testando em desenvolvimento.

10:25

Porque toda hora ele vai acabar recarregando uma vez que

10:27

a gente está usando a sessão em memória.

10:30

Então aqui nós já vemos um comportamento dessa sessão,

10:35

porque ela garante a continuidade da conversa.

10:39

Eu criei essa sessão no endpoint diferente e

10:46

continuei no outro. Então, não importa.

10:49

Uma vez que eu tenha a sessão,

10:51

se o usuário quiser continuar a conversa amanhã... eu tenho tudo isso armazenado.

10:56

Obviamente, nesse caso aqui, em memória seria arriscado,

11:01

mas a gente utilizaria banco de dados.

11:04

Então, nós já temos a ideia de como funciona esse fluxo ágil e, na verdade,

11:11

como que essas aplicações que nós já trabalhamos trabalham também,

11:15

exatamente dessa forma.

11:17

Eles vão ter a sessão, armazenam em algum lugar,

11:19

e a sessão tem todo o histórico e a coisa vai dando continuidade dali,

11:23

a sessão tem os eventos, nós vimos, System Prompt vai com o conteúdo,

11:29

tudo que já foi respondido, a IA vai decidindo,

11:33

vai sendo armazenado de volta na sessão, e por aí vai.

11:36

Mas, obviamente, aqui nós temos um exemplo mais simples.

11:42

Porque se nós tivermos Tool Confirmation e outras coisas,

11:47

Aí nós vamos ter que tanto mudar um pouco esse trecho,

11:52

quanto também na mensagem

11:56

Adicionar outras opções.

11:58

Você tem aquelas situações de um questionário que

12:03

aparece para você poder escolher opções,

12:05

você autoriza a execução de uma tool,

12:07

igual acontece na sua ferramenta de codificação local. Então,

12:11

eu não vou enviar necessariamente uma mensagem,

12:13

mas outras informações de autorização e outras coisas.

12:19

Então, feito a nossa primeira conversa básica utilizando uma aplicação web.

## Resumo IA

[RESUMO_IA]