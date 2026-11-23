Módulo: Arquitetura na Era da IA\
Aula: [Testes de contrato](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18785)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem? Então, se você olhar aqui,

00:04

eu criei basicamente dois arquivos,

00:07

mas um deles apenas envelopa os meus testes,

00:10

mas aqui que eu criei que você dê uma olhada, tá?

00:13

Eu criei basicamente, eu acredito que foram 13... casos de teste aqui para a gente, tá?

00:20

Mas o ponto principal de tudo isso,

00:23

é isso que eu quero que você leve em consideração,

00:25

esses testes são testes de contrato, tá?

00:28

Para API HTTP e também eu criei um pipeline fake para a gente fazer esse teste.

00:34

Por que esse cara, nesse caso, para a gente, ele é importante?

00:38

Porque com esse teste sendo determinístico, eu consigo,

00:42

por exemplo, testar a estrutura do meu dataset corretamente.

00:47

E não apenas, ah, se existe um arquivo, como a gente fez um teste antes,

00:52

a gente mudou o arquivo MD para ele pegar. Isso também é importante,

00:56

mas a gente tem regras de negócio que para a gente são importantes.

00:59

Se eu rodar aqui, por exemplo, acho que é Python, "-m", pytest.

01:04

Aqui, você vai ver que os meus testes aqui vão rodar,

01:07

13 caras passaram, bonitinho aqui para mim.

01:10

Agora, se você olhar, por exemplo, o nome dos meus testes,

01:15

deixa eu dar um "-v", você

01:19

vai perceber que cada teste meu tem uma intenção.

01:24

Então, por exemplo, teste dataset has no errors.

01:27

Teste dataset... That covers answerable cases.

01:30

That covers refusal cases. O esclarecimento,

01:35

se tem a parte de health, se ele possui, se o teste...

01:43

Answer possui os sources, se o refusal não tem source,

01:47

se o esclarecimento não tem source,

01:49

se o debug está sendo retornado quando está sendo pedido,

01:52

se ele está aparecendo quando ele não está solicitado,

01:56

se o re-rank é falso quando ele bate ali no pipeline

01:59

e se tiver alguma questão em branco ou até etc,

02:03

ele acaba conseguindo passar.

02:06

Por que isso aqui para a gente é importante? Porque tudo isso que eu estou fazendo,

02:11

ele está testando o contrato nosso. E aí,

02:14

a gente sai daquela coisa de eu não preciso chamar a minha LLM. Então, se eu descer,

02:20

por exemplo, o meu Docker Compose,

02:23

meu banco de dados e tudo isso, tudo isso vai ser...

02:27

independente. Por quê?

02:28

Porque aqui eu estou simplesmente colocando um pipeline

02:35

fake para a gente conseguir rodar esses testes,

02:38

mas o mais importante de tudo isso aqui é que, de fato,

02:41

eu não estou testando se a resposta foi boa

02:44

ou se qualquer coisa foi relevante ou não.

02:47

Eu simplesmente estou testando o contrato.

02:49

Se esses contratos não passam, com certeza,

02:52

na hora que eu estiver lá no meu pipeline, no meu pipeline não,

02:56

lá nos meus datasets com Langfuse, tentando fazer LLMS Judge,

03:00

tudo aquilo vai estar contaminado porque eu...

03:04

não tenho essas informações de forma clara e intencional. Então, novamente,

03:08

tudo que eu estou dizendo aqui para você é intencionalidade.

03:11

Os nossos testes automatizados, simples com PyTest,

03:15

você pode fazer com a linguagem de programação que você está usando,

03:17

ele consegue fazer validação determinística.

03:20

E muitas vezes essa validação determinística,

03:22

ela consegue economizar muito dinheiro para a gente. Por quê?

03:26

Porque se a gente fosse fazer essas validações com LLM,

03:29

ia demorar muito mais, ia custar muito mais,

03:32

e às vezes a gente não ia ter esse resultado. A mais, B é igual a C,

03:36

por exemplo. Porque esse teste determinístico,

03:38

ele ajuda nisso e a gente vai falar em seguida sobre tudo isso,

03:41

tá? Então, tenho testes automatizados,

03:44

mas a grande sacada é que ele está testando isso, usando o nosso dataset como base,

03:50

mas principalmente, né? A gente consegue testar isso contra a API,

03:54

que vai ser o que vai responder ali para o usuário final,

03:57

mas obviamente sem passar pelo pipeline completo,

04:00

sem precisar bater em nenhuma LLM. Fechou? Então, essa que é a ideia,

04:05

aqui eu tenho a pergunta, a resposta,

04:07

a refusal e a clarification que eu uso como base

04:10

aqui para a gente fazer esses testes ali. Ou seja,

04:13

eu estou simulando aqui para mim todo esse dataset,

04:16

mas basicamente eu estou trabalhando...

04:19

em cima dessas possibilidades para garantir que essas

04:22

regras de negócio estejam certinhas aqui. Se você olhar,

04:26

eu tenho informações com o Nando Debug,

04:28

o resultado da pergunta, quando está acontecendo o Refusal, ou seja,

04:34

basicamente como é que estão saindo as saídas que eu estou precisando. Fechou?

04:38

Depois você olha com calma, tudo isso vai estar no repositório,

04:41

mas o ponto é que a gente vai falar

04:43

cada vez mais também sobre testes determinísticos. Um abraço!

## Resumo IA

[RESUMO_IA]