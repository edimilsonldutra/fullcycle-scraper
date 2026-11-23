Módulo: Desenvolvimento de Agentes com IA\
Aula: [Estorno automatizado](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18574)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos fazer o estorno automatizado.

00:04

Nós vamos investigar com o que nós vimos na última aula a situação ali do estorno.

00:09

Uma vez que o agente emite o seu parecer,

00:13

teremos um function code que faz a triagem e depois o estorno automático.

00:19

Então, a primeira coisa que nós temos que configurar é na triagem...

00:24

Ao verificarmos se tem relação com o estorno,

00:27

ele vai para esse caminho ao invés desse outro caminho que nós temos aqui no grafo.

00:33

Portanto, aqui em cima, logo

00:40

depois, porque nós temos essas informações básicas aqui no state,

00:44

nós podemos fazer um if, e eu coloquei uma

00:49

função simples para ver se precisa de resolução de refund.

00:54

Como nós temos dentro do classification needs refund, E o confidence,

00:59

nós vamos usar para ver se ela está true e se o confidence é maior que 60%. Então,

01:04

que é uma lógica, obviamente, fictícia. Nós consideramos que,

01:08

de fato, esse estorno tem que ser analisado. Então,

01:12

veja que eu posso ter a necessidade de estorno, mas uma confiança baixa,

01:19

ele iria para o atendimento. E do atendimento, talvez,

01:24

poderíamos escalar.

01:26

Nós poderíamos criar esse caminho também.

01:29

Então, se verificarmos que precisa de resolução de refund,

01:34

ele vai para o caminho Refund Investigator.

01:39

Então, nós vamos ter que declarar essa linha aqui.

01:43

Refund Investigator puxa o agente Refund

01:50

Investigator Agent.

01:52

Ok, ele vai executar, nós já sabemos como que isso funciona.

01:55

E agora vem o próximo nó com a triagem. Então,

01:58

depois que tiver a investigação, vamos ter a triagem do Refund Node. O

02:06

que ele vai fazer? Ele recebe o Node Input e essas

02:14

informações que vão estar no objeto, inteiramente validadas.

02:20

Então, nós podemos ter dois tipos de decisão.

02:24

Ou é Refund ou é Escalar.

02:27

Então, se não for Refund, aqui nós vamos escalar.

02:32

Esse passo do Python serve para quando eu não quiser colocar nada no if.

02:37

Por enquanto, se eu deixar a instrução vazia, é um erro de sintaxe.

02:44

Então, aqui nós podemos

02:46

prosseguir com o escalonamento.

02:54

Então, nós vamos pegar o mês, os itens indevidos, o customer ID.

03:03

Nós vamos calcular.

03:08

Esse veredito que aconteceu. Então, tem esse computeRefundable. Veja só.

03:19

Nós estamos chamando o billing mais uma vez com o getInvoice

03:23

para poder pegar qual é a fatura que tem que ser estornada.

03:26

Então, se tiver um erro, nós retornamos como resultado aqui um erro. E tem a razão.

03:33

Caso contrário, nós vamos varrer cada item para ver se de fato...

03:39

Ele está batendo com o que nós mandamos,

03:42

porque se tiver alguma coisa inválida, não tem nenhuma linha,

03:45

porque isso aqui é a segurança que a

03:46

gente está consultando essa informação novamente.

03:50

Consegui consultar a linha fatura existe, então vamos somar o que

03:55

foi identificado e analisar se essa

03:58

somatória é maior que o RefundMaxLimit.

04:04

Então nós vamos ter duas variáveis, eu acrescentei elas aqui no EnvExample.

04:09

Eu tenho o Threshold e o Max. Então, o Threshold é 50.

04:14

Então, até esse teto a gente faz automático.

04:17

E aí tem um 200 que já está extrapolando,

04:20

que aí a gente tem que ter um cuidado maior.

04:24

Então, o que eu estou analisando aqui é se é maior que esse limite.

04:28

Então, nós vamos bloquear esse Refund.

04:37

Ou nós vamos retornar OK. Então,

04:39

eu sempre retorno aqui um dicionário com as informações pertinentes.

04:44

Essa função aqui é uma função que está fazendo uma análise totalmente direta,

04:50

sem a LLM.

04:53

Então, ela retorna esse que eu chamei aqui de calc.

04:57

Então, se tiver o status not found inválido,

05:00

o block refund, que ele ultrapassou o limite,

05:02

também eu vou prosseguir com o escalete.

05:09

Agora, se eu fiz toda essa análise, então nós vamos tentar

05:16

fazer o refund automático. Mas nós temos que tomar o devido cuidado. Na verdade,

05:22

eu até vou pegar essa partezinha aqui.

05:25

Ela não faz sentido mais embaixo do que em cima.

05:30

Então, analisei tudo.

05:31

Se o limite não foi quebrado,

05:34

eu vou pegar o Amount e ver se ele está dentro daquele True Short que é 50.

05:43

Eu criei

05:46

também, se eu não tinha mostrado, eu criei um Env lendo já direto,

05:54

conseguimos importar o env aqui sem ter que ficar fazendo código de os .environ,

06:01

que é a parte do Python. A gente já consegue usar diretamente.

06:05

Então, se for maior,

06:08

então também aqui nós vamos prosseguir com o escalete. A

06:13

questão é que cada um desses prossegue com essa human in the loop,

06:19

passando determinadas informações.

06:22

Então, passou de tudo isso, sabemos que o amount é 50 ou menor que 50.

06:30

Então, nós vamos gerar um objeto com as informações

06:34

necessárias para que nós possamos fazer o nosso

06:37

estorno.

06:39

Então, esse auto-refund-request nada mais é do que

06:44

um tipo do pidentic em que nós adicionamos todas as informações. Por quê?

06:52

Dessa forma aqui... Esse auto refund, que é o novo caminho que nós vamos mandar

07:00

e vai ter um novo function code, ele recebe a informação validada.

07:05

Aqui eu posso, nesse output, eu posso passar um dicionário,

07:07

pode passar um valor básico,

07:10

mas trabalhando com o pai dentro fica bem melhor, porque está validado.

07:17

Então, quando

07:20

tivermos

07:23

aqui a triagem, nós

07:26

vamos analisar o caminho.

07:28

Ah, é um auto-refund?

07:30

Então vamos colocar auto-refund node, que

07:36

nós possamos processar.

07:39

Então aqui nós vamos definir um node com

07:43

async def auto

07:48

-Refound node. Então nós vamos receber o contexto e o auto-refund request.

07:53

Então veja que a primeira vez que nós estamos pegando,

07:56

apesar de que tem o refield, nós já tínhamos feito antes. Um nó.

08:02

Function Code passando para outro Function Code direto,

08:05

mas agora esse aqui é bem mais importante.

08:07

Nós vamos fazer esse estouro.

08:10

A primeira coisa que nós precisamos fazer é aquela verificação inicial do ticket.

08:16

Como eu já tinha falado, a gente não está se importando aqui com camadas, fazer

08:24

alguma coisa de serviço, aplicar qualquer boa prática.

08:28

Estamos duplicando o código, mas

08:32

isso depois seria facilmente ajustado.

08:35

E agora, depois que eu já vi que o ticket já existe, antes

08:41

de fazer qualquer coisa de salvar ali o ticket, nós usamos o Bidding Issue Refund.

08:48

Então, nós temos que passar o Customer ID, o Amount e

08:56

Reason.

08:59

Vai ser uma frase... Na

09:04

verdade, vamos colocar só Refund aprovado, né?

09:07

Vamos colocar esse automático. Então,

09:10

o customer ID pegamos do ticket, o amount do node input.

09:14

Então, se isso aconteceu com sucesso, aí agora vem um ticket response. A

09:22

própria IA já sacou o que eu quero fazer.

09:24

Então, o seu pedido de reembolso foi aprovado,

09:26

processado, o valor tal. Vou tirar esse S daqui,

09:31

referente à fatura do mês tal, com as linhas tal,

09:38

e será creditado na sua conta em até 5 dias úteis, enfim.

09:42

Aí depois vem o status,

09:45

atualizou o ticket e retorna a mensagem.

09:53

Então, pronto.

09:55

Agora temos que importar corretamente aqui.

10:00

Temos vários nodes, né? Vou

10:04

colocar tudo em múltiplas linhas porque aí fica fácil para que a gente veja melhor.

10:13

Pronto. Então agora vamos...

10:19

Fazer aqui o ADK Web na pasta Agents, porque nós temos que criar o ticket.

10:30

Então, vamos

10:34

selecionar o ticket Receptionist.

10:37

Quero criar

10:43

ticket de estorno da fatura de junho de 2026. Ele

10:56

vai fazer a classificação e vai registrar o ticket. Então, pronto.

11:01

Agora, vamos para o

11:05

ticket Resolution.

11:07

Então, tem o ticket ID,

11:16

que é o que foi gerado.

11:19

Então vamos mandar qualquer coisa e agora veja o tamanho do nosso grafo.

11:24

Tem certa complexidade.

11:32

Eu fiz errado exatamente porque não tem o ID correto

11:38

aqui. Tem que colocar o C203, porque senão ele não vai conseguir consultar.

11:44

Conforme ele retornou aquele erro ali.

11:47

Vamos pegar a mensagem para não ter que digitar de novo. O

11:56

usuário está correto. Agora sim.

12:05

Então, vamos para o Ticket Resolution, Ticket Age.

12:20

Vamos acompanhar todo o andamento do grafo,

12:22

porque à medida que ele for fazendo as coisas,

12:24

nós vamos vendo. Ele foi no Finding Voices.

12:28

Agora, pegou esse caminho daqui. Então, ele tomou a decisão de Refund, e

12:35

aí foi para o Auto Refund e teve ali o pedido que

12:39

foi feito. Então, o nosso grafo tomou este

12:44

caminho. Ele chegou aqui no Refund Investigator.

12:49

Teve o findVoices que não vai aparecer aqui porque ele só vai mostrar os

12:55

caminhos que foram feitos, a tool está dentro do agente.

12:58

Então aqui também não temos o default no refundNode,

13:01

mas nós já fizemos toda a lógica dentro dele, aconteceu o autoRefund, então houve o

13:09

estouro. Então aqui nós agora temos

13:13

um vislumbre com o que é...

13:17

Criar uma aplicação ágil.

13:19

E você pode começar a questionar agora se os agentes de IA que você trabalha,

13:24

será que quantos agentes existem?

13:28

Quais os fluxos podem existir lá?

13:32

Outros vão trabalhar de forma semelhante também.

13:36

Você não sabe quantos agentes vão ter ali.

13:38

Você sabe que o core da aplicação são agentes de IA.

13:41

Então, um cenário como esse é algo fantástico porque...

13:45

Eu tenho um agente de A tomando essa decisão do reembolso,

13:49

mas delegando mesmo a

13:51

operação crítica para ser determinística,

13:56

para ler para o function code, que é mais um nó que nós temos no nosso grafo.

## Resumo IA

[RESUMO_IA]