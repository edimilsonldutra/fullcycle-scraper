Módulo: Desenvolvimento de Agentes com IA\
Aula: [Criando base do agente de recepção dos tickets](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18557)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos criar a primeira parte do agente que vai

00:04

interagir com o usuário para a criação de tickets.

00:08

Eu já fiz a criação base dele dentro da pasta Agents,

00:12

ele é chamado de Ticket Receptionist.

00:15

Ele tem ali o __init__.py, o agent.py e os subagentes.

00:20

E aqui nós vamos ver algumas coisas interessantes,

00:23

mas só tem um subagente, apesar de ter alguns arquivos e pastas.

00:29

Vamos olhar o agent.py.

00:33

Ele tem apenas 31 linhas. Tem o root agent, o app, que podemos definir aqui dentro.

00:41

Inclusive, isso é interessante, porque quando rodamos o ADK web ou o ADK run,

00:47

ele vai dar precedência para o app. Depois,

00:51

se não existir o app, ele vai importar o root agent.

00:55

Então, temos tanto o root agent quanto o app com o nome ticket receptionist.

01:01

Ele vai ser responsável por receber tickets de suporte e classificá-los.

01:07

Tem um modelo que nós já estávamos utilizando, que é o Gemini 3.5 Flash.

01:12

O System Prompt está separado em uma variável.

01:16

Eu gosto de fazer isso para que não fique

01:19

muita sobrecarga em cima da definição do agente.

01:23

E o subagente é o agente de classificação dos tickets.

01:28

Então, nós vamos ter...

01:30

Um agente que vai ser o recepcionista da central de atendimento da Acme Cloud.

01:35

Se o usuário perguntar sobre algum ticket já registrado,

01:39

pesquise o status do ticket e dê uma resposta adequada.

01:42

Se o usuário pedir para listar tickets,

01:45

então forneça uma lista de tickets registrados

01:48

de acordo com os critérios fornecidos.

01:50

Por exemplo, categoria, status, enfim.

01:52

Então aqui nós já vemos com essas duas perguntas.

01:56

Podemos criar tools. Nós já sabemos fazer isso. A tool vai acabar desencadeando ali,

02:01

seja o que for, um HTTP ou um banco de dados.

02:04

Isso não é mais um problema para que nós possamos criar os nossos agentes.

02:11

Nós não definimos aqui como vai ser a questão de criar o ticket.

02:16

Não tem essa informação,

02:18

mas nós vamos criar uma vez que se tem a classificação do ticket.

02:25

Por exemplo, é uma dúvida...

02:28

fora do escopo, é algo de reembolso, às

02:34

vezes está se falando de clima,

02:36

o usuário pode ser brincalhão e falar qualquer coisa que não é necessária. Então, enfim,

02:45

nós vamos fazer essa classificação porque ela vai nos ajudar a depois acionar

02:51

o outro agente de resolução.

02:56

Então essa classificação vai ser crucial.

02:59

Então por isso que este agente de...

03:02

da recepção do ticket, vou chamar o agente de classificação do ticket.

03:07

Então ele está definido aqui em subagents,

03:10

que é uma forma que eu gosto de organizar, e o nome da pasta,

03:14

ticket classifier.

03:17

Então tem o agent.py.

03:20

Ele já é um agente com muito mais conteúdo. Nós temos aqui 78 linhas.

03:28

Então temos o nome dele, que é o mesmo, a variável.

03:34

Recomendo não colocar, apesar de... isso ser possível.

03:38

Não chega aqui e coloque um Root Agent.

03:42

Porque a ideia do Root Agent é dizer assim, aqui é o ponto de entrada.

03:48

Root Agent não é ponto de entrada.

03:50

Então nós nomeamos dessa forma, aí importamos no ponto de entrada.

03:59

Porque depois isso vai acabar gerando confusão para você poder programar,

04:03

para um agente de IA também poder programar.

04:07

Todas essas semânticas vão ser cruciais. Então tem o nome dele,

04:11

ele vai classificar tickets de suporte da Acme Cloud em categorias pré-definidas.

04:16

O mesmo modelo que nós estamos utilizando, gratuito, é o 3.5 Flash.

04:23

E o modo single churn,

04:24

porque esse a gente não precisa perguntar nada para o usuário,

04:28

ele não vai ter nenhuma interação,

04:31

ele só vai receber o texto que o usuário digitou e fazer a classificação.

04:36

Então o single churn seria o ideal.

04:39

A instrução que está em cima.

04:42

O Output Schema,

04:44

porque nós podemos padronizar essa resposta e ela

04:49

vai nos ajudar depois para seguir com a resolução,

04:52

nós vamos falar disso daqui a pouco. O Output Key,

04:56

que vai ser temporário,

04:58

permitindo que o usuário faça a criação contínua de tickets,

05:04

ou seja, numa mesma sessão ele pode criar três tickets, quatro, cinco.

05:10

Nós vamos falar disso depois, mas essa classificação aqui precisa ser temporária,

05:14

porque senão nós vamos ter que forçar o usuário a

05:17

criar uma nova sessão para criar um novo ticket.

05:20

Às vezes ele quer criar mais de um, enfim.

05:23

Então, no System Prompt,

05:25

nós vamos dizer que ele é um classificador de

05:28

tickets da central de atendimento da Acme Cloud.

05:31

A tarefa dele é analisar a mensagem do usuário e

05:34

classificá-la em uma das categorias pré-definidas.

05:38

fornecendo também uma justificativa curta para a classificação.

05:43

Então, ele vai classificar de acordo com o contexto abaixo.

05:46

Nós vamos falar o que é essa Acme Cloud.

05:50

Ela é a plataforma de SaaS B2B, gestão de equipes, tem PI de cobrança,

05:55

faturas mensais, reembolso automático, integrações com GitHub,

06:00

Linear, Webhook, Teams, enfim.

06:02

Então, um pedido, vou colocar isso aqui de forma separada.

06:07

Um pedido cujo objeto é claramente outra coisa, cripto, banco pessoal, clima,

06:12

não é coerente com a ACME. Isso alimenta as regras 1 e 4 da escada abaixo.

06:18

Eu tenho aqui essas regras de como que ele vai fazer essa classificação.

06:23

Nós vamos chegar aqui daqui a pouco. Então, logo abaixo, nós

06:28

vamos ter as categorias reais que elas vão ser usadas

06:33

pela classificação. Vai ser billing se é questão de fatura,

06:36

cobrança, qualquer coisa financeira.

06:39

Bugs, tem algo quebrado. Feature requests,

06:42

se é um pedido de um recurso de integração,

06:44

desenvolver alguma coisa nova, ou se é um onboarding, dúvida de uso, configuração.

06:49

E as categorias de fallback, elas são o último recurso, não use como atalho,

06:55

porque a LLM pode usá-las, deixa eu já ver se não é isso aqui.

07:01

Tem a compositive, quando é uma ou mais categorias reais.

07:07

Undefined quando o suporte é plausível,

07:09

mas nenhuma categoria real vai se encaixar, se aplica com clareza.

07:13

E fora do escopo, que nem é um pedido de suporte,

07:17

uma saudação, spam de tópico, enfim.

07:20

Mas isso também nós queremos registrar porque pode ser interessante de

07:24

alguma forma para poder entender o que está acontecendo na Acme Cloud.

07:29

E aí tem a precedência, a escada de precedência,

07:32

que é o que está dizendo aqui de 1 a 4.

07:35

para que ele não se perca. Primeiro, ele vai ver se não

07:39

é apenas um fora de escopo,

07:43

mas ele vai olhar se o ticket inteiro não é de suporte. Isso que é importante.

07:48

Eu posso mandar várias coisas, por causa de uma,

07:51

ele classifica o resto todo como aquilo que ele identificou.

07:57

Então, primeiro, se não é fora de escopo o ticket inteiro,

07:59

se não é Compositive, ou se se encaixa em... Várias categorias.

08:06

E depois, se não é uma categoria única real.

08:09

Aí tem algumas regras sobre isso. Isso aqui demandaria um prompt muito bem feito.

08:15

Para que a gente tivesse uma categoria.

08:17

E essa categoria vai definir como as coisas vão acontecer depois.

08:21

E por último, undefined. Não tem um suporte plausível,

08:25

mas nenhuma categoria real se aplica com clareza. Então,

08:29

inclui o caso como o ruído,

08:33

que está grudado no objeto e o torna incoerente com o domínio da Acme. Enfim.

08:40

E aqui mais abaixo nós temos algumas instruções

08:43

de como que ele vai acabar preenchendo o TicketClassifierOutput,

08:50

porque nós temos a categoria, que é isso que nós estamos conversando,

08:53

o Confidence, e aqui mais informações, veja só, tem aqui um GreaterOrEqual

09:02

e um LessOrEqual, ou seja, maior,

09:06

ou igual a 0, menor ou igual a 1,

09:10

que é a classificação de 0 a 100%. O

09:14

quanto que essa classificação é confiável? Nós estamos fazendo.

09:19

Colocou lá a categoria bug. Pode ser que não seja muito confiável.

09:23

Então isso pode mudar como nós vamos resolver esse ticket.

09:27

Tem a justificativa que é apenas a string e

09:32

o needsRefound que se tem alguma coisa de reembolso no meio.

09:37

Então indica se o ticket envolve algum pedido de estorno,

09:40

reembolso, ajuste de valor da fatura.

09:44

Então aqui em regras importantes nós estamos falando se a mensagem cita refund,

09:49

reestorno, ajuste de valor da fatura,

09:51

defina o needsRefound igual a true. Não estime valores,

09:55

o valor do reembolso é determinado depois a partir das informações da fatura.

10:02

O confidence é a sua certeza da classificação.

10:05

Se a mensagem é ambígua, use confidence baixo.

10:11

E a justificativa em uma frase. Então,

10:13

veja o conjunto disso tudo trabalhando lá na LLM.

10:19

Tudo está sendo... vai ser grudado, né? Tudo é enviado para lá.

10:25

Apesar de nós já termos descrições no

10:29

output em cada campo,

10:31

não é aqui que nós vamos colocar como esse campo vai ser preenchido.

10:36

É no system prompt.

10:39

Então, nós não podemos ser repetitivos, como aqui embaixo tem uma definição.

10:44

Bem básica, que o retorno deve ser, obviamente,

10:47

um JSON com cada dado. Mas nós não ficamos colocando descrições.

10:52

Mas em regras importantes, nós colocamos as regras de como tem que ser preenchido.

10:57

Então, cada coisa no seu devido lugar,

10:59

para que nós não sejamos repetitivos, geremos ambiguidade e

11:05

também gastemos mais tokens.

11:08

Então, essa aqui é a definição do nosso subagent.

11:14

E aqui eu tenho uma... outra boa

11:19

prática em relação ao subagent para que

11:22

nós possamos continuar testando ele no ADK Run,

11:27

no ADK Web.

11:31

Como nós já sabemos que uma vez passado ali na pasta, se eu estou em

11:37

Agents com ADK Run ou Web, ele

11:42

vai acabar procurando o agent .py depois um app ou um root agent.

11:53

Nós não temos isso aqui.

11:57

Nós não temos essa definição.

12:03

E nem vamos fazer por conta da convenção. Então, eu gosto de criar uma pasta com

12:11

um agent .py. Eu

12:15

acho que eu deixei lixo aqui, ou não?

12:24

Está mostrando... Ah,

12:25

agora sumiu a mensagem porque eu tinha feito coisas

12:28

que não estão na sintaxe do Python.

12:30

Eu crio essa pasta com agent .py, importo o meu subagent,

12:36

e coloco ele como root agent e faço uma transformação se necessário.

12:41

Temos um método clone que permite que eu faça um clone dele mudando informações,

12:46

porque como ele é um single churn,

12:49

esse detalhe é importante, eu não consigo conversar com ele,

12:53

nem se eu chamar ele direto.

12:56

Então, eu preciso transformá-lo em um agente de chat. Então,

13:00

o clone permite que eu passe mudanças, ele é recriado.

13:05

com as configurações que nós vamos passar. Então,

13:08

aqui também nós podemos definir app. Então,

13:10

a ideia dessa pasta é servir totalmente para desenvolvimento.

13:14

Ela fica totalmente independente.

13:16

É legal que a gente faça alguns testes. Ah, eu quero só testar a classificação.

13:19

Eu tenho que levantar o Ticket Receptionist?

13:23

Para isso, não. Então, nós podemos rodar o

13:26

ADK Web, contando para Ticket Receptionist,

13:31

Subagents, Ticket

13:35

Classifier Dev.

13:37

De forma como nós já aprendemos. E

13:41

faltou uma pasta. Faltou.

13:46

TicketClassifier e depois vem a do dev.

13:50

Pronto. Aí nós vamos ter esse mesmo nome que nós colocamos o nome na pasta,

13:54

TicketClassifierDev.

13:57

Vai ficar claro o que nós estamos fazendo. Eu chego lá e faço os meus testes.

14:02

Ainda mais essa classificação seria interessante testar de forma separada.

14:06

Se eu mandar um olá, estamos

14:10

Fora do escopo. O confidence é 100% porque é uma saudação,

14:15

não tem nenhuma relação com

14:18

o que nós queremos classificar.

14:19

E a justificativa mensagem contém uma saudação não

14:21

se tratando de um pedido de suporte.

14:23

E não precisa de nenhum reembolso.

14:26

Então isso aqui já é uma saída

14:29

estruturada para que nós possamos trabalhar na resolução.

14:35

Como ela está estruturada, esse

14:38

agente vai ser blindado. Ou melhor, vai ser...

14:42

Blindado no sentido não de protegido, mas ele vai receber um presente já

14:47

bacaninha para ele poder trabalhar.

14:50

Então vamos seguindo aqui a criação desse nosso agente.

## Resumo IA

[RESUMO_IA]