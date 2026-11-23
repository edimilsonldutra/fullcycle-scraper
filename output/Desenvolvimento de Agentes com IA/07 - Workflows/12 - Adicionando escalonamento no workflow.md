Módulo: Desenvolvimento de Agentes com IA\
Aula: [Adicionando escalonamento no workflow](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18576)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos adicionar o nosso agente de escalonamento,

00:04

o escalonator agent, no meio do workflow.

00:07

Então, onde que ele vai entrar no meio desse processo?

00:10

Depois que nós fizermos o refound investigator, podemos fazer o auto -refound,

00:17

mas dentro desse agente, temos no

00:22

output schema, decision.

00:28

Pode ser refund ou escalate.

00:32

Então, nós vamos...

00:34

capturar isso na triagem do estorno e

00:39

colocar o escalate

00:42

equivale ao escalator agent.

00:50

Então, acho

00:54

que aqui já importou de forma correta.

01:01

A descrição nós não tínhamos mudado antes, vou aproveitar o momento,

01:05

foi passando o tempo e não mudamos,

01:08

então pronto. Agora vamos para o node. Então, aqui embaixo na triagem,

01:16

temos a parte do auto -refound,

01:21

e nesse if que o amount é maior que o threshold,

01:26

que é o 50, é que nós vamos colocar. Então,

01:28

nós conseguimos fazer o escalonete nesses três lugares.

01:34

Cada um dos três lugares nós vamos passar informações diferentes.

01:38

Então, aqui eu vou retornar o evento em

01:44

que, em actions,

01:48

Vamos ter o event actions.

01:53

Então nós já sabemos que o route vai ser igual a

01:58

escalonate e

02:03

temos que passar o output. Vamos

02:10

pegar novamente, agora é um monte de agent .py, né?

02:14

Antes tínhamos um monte de index .ts, agora são vários. Vou

02:22

colocar escalonator, é esse aqui.

02:28

ele tem o escalonator input.

02:31

Então, o output deste evento tem que ser o input do outro.

02:37

Então, nós vamos chamar o escalonator input,

02:41

passando as três informações.

02:45

Então, vem o intent, que

02:52

aqui vai ser o refound confirmation.

02:55

Então, chamamos novamente o escalator input ponto...

03:01

Na verdade, é escalator intent que temos um em um com essas informações.

03:07

Então passamos aqui, we found confirmation.

03:11

Summary vai ser um texto, o

03:16

pedido de

03:19

um estorno, vou deixar com que aí eu preencha o pedido de estorno,

03:23

referente, a fatura e etc. E

03:27

a severidade, que

03:34

aí nós poderíamos fazer um certo cálculo.

03:38

eu acho que eu tenho essa função já aqui em cima,

03:42

eu passo o status e o amount.

03:47

Então, se for igual a um block e found é alto,

03:50

porque eu bloqueei de alguma forma, identifiquei um problema,

03:53

se é not found ou invalid, porque eu posso não ter encontrado ali abaixo,

03:58

E se o amount não existe,

04:03

Ou melhor, se ele não é None, e se ele é menor que duas vezes o threshold,

04:10

Então, eu considero como alto ou médio.

04:12

Eu criei uma lógica de exemplo para que

04:15

Nós pudéssemos colocar aqui e não ter apenas uma

04:24

informação fixa. Então, nós poderíamos colocar toda essa lógica. Veja,

04:28

Mais uma vez, nós estamos nos pautando pelo determinismo para

04:34

mandar as coisas para o agente e não deixar que tudo seja processado por IA também.

04:41

Então, excelente. Temos...

04:47

Tudo isso aqui feito,

04:50

Colocamos o escalate. Agora,

04:54

O que vai acontecer quando o escalator agent processar?

04:58

Então, mais uma tupla do escalator agent

05:07

Vai

05:10

para um function code.

05:12

Nós vamos ter uma triagem da

05:16

escalação. Vou colocar uma

05:19

triagem de escalation. Acho que já está de bom tamanho. Assim, dessa forma. Pronto.

05:29

Então, vai ser mais um node, vamos colocar aqui de baixo,

05:34

node, def,

05:37

Vamos colocar já um async aqui, só que eu acho que não é necessário,

05:42

mas podemos colocar. Nós vamos receber como node input o

05:49

escator output, e aí nós vamos tomar alguma providência.

05:55

Então, se eu

05:58

tiver node

06:00

input status,

06:05

diferente de failed, que nós podemos ter,

06:10

Vamos voltar aqui, nós podemos ter created,

06:15

reused e failed. Então, se for diferente de failed, aconteceu sucesso.

06:21

Então, eu vou olhar se o node input é um refound confirmation.

06:28

Ah, um refound confirmation. O que nós vamos fazer?

06:33

Nós vamos ter que parar o nosso processo, porque

06:39

Aí vai precisar da ação lá externa do usuário.

06:43

Mas o que nós vamos fazer aqui depois disso?

06:47

Nós não vamos definir nessa aula. Então, eu vou colocar apenas um pass.

06:52

Mas aí nós vamos ver que há esse nó. Agora eu preciso voltar aqui e importá-lo.

06:59

Importou aqui em cima.

07:02

Já temos um grafo bem complexo. Pronto. Então, agora em termos de execução.

07:10

Vamos fazer o ADK Web apontando para Agents,

07:13

Porque agora nós vamos precisar criar o ticket e tudo mais.

07:18

Então, vamos selecionar o ticket Receptionist.

07:21

Como nós temos a questão do estorno maior, eu

07:27

Acredito que seja o usuário

07:31

204, que é o que está aqui.

07:36

Então, a fatura de junho que ele vai extrapolar. Na verdade, aqui ele

07:42

tem que estar dentro do limite.

07:48

Vamos testar com esse cara que eu acredito que vai dar certo.

07:52

Então, user.

07:57

Pronto. Então, vamos colocar aqui.

08:00

Quero criar um ticket para se

08:04

Tornar fatura de junho de 2026. Vai

08:12

fazer a classificação.

08:15

Então, o usuário solicita o estorno da fatura

08:18

que se enquadra em questão de cobrança. Vai a billing. Pronto.

08:23

Então, vamos para

08:26

TicketResolution. Então, agora,

08:31

TicketId e

08:35

vamos

08:38

lá. Agora, olha a complexidade do nosso grafo. Está

08:44

ficando bem interessante. E assim vai.

08:47

Podemos ter um grafo bem mais complexo do que esse.

08:55

Aqui é a boa vontade da LLM.

09:05

Então, olha só o que aconteceu. Tivemos aqui...

09:09

Find Invoice, nós estamos no Refund Investigator. Então,

09:13

ele colocou a decisão Refund, ou seja, tem que fazer o estorno,

09:18

só que o valor é maior.

09:19

Então, foi para a triagem do Refund.

09:24

Então, ele vai dar entrada no escalador com o Refund Confirmation, com o assunto,

09:29

tem lá o pedido de 480 reais, a fatura de junho.

09:36

E aí vai entrar no nosso agente de escalonamento.

09:41

E aí, no final das contas, ele

09:45

foi aqui para o escalador e

09:50

nós não conseguimos ver o processo.

09:56

Será que tem alguma coisa

10:00

incorreta? Porque

10:04

também nós não retornamos nada aqui. Então,

10:08

poderíamos colocar um

10:13

teste só

10:16

para que a gente

10:21

veja mais esse grafo, mas antes até de eu fazer de novo,

10:25

vamos olhar agora o que está acontecendo.

10:29

Olha só o caminho, então ele vai no Start,

10:31

triagem do Ticket, Refund Investigation,

10:36

triagem do Refund e o Escalador com todo o aparato que ele tem.

10:45

Aí depois ainda eu teria a triagem do escalonamento.

10:49

Eu fiz a criação de outro Ticket e justamente agora com a mudança que nós fizemos,

10:54

então agora ele bate na triagem do...

11:04

escalonamento e terminou. Mas ainda nós vamos ter um último passo aqui.

11:10

Então agora, voltando até para as nossas issues, temos

11:16

essa última que foi feita.

11:18

Pedido de refund de tantos reais.

11:24

Enfim, poderíamos calibrar da forma que fosse necessária. E a questão justamente,

11:30

aqui eu não quero falar de outras plataformas ou...

11:35

querer focar no linear.

11:38

A questão do webhook é irrelevante para o nosso agente de IA,

11:42

porque ele vai acabar fazendo uma chamada para a API,

11:45

nós vamos formatar os dados conforme o agente de IA precisa,

11:49

mas tudo vai desencadear, fez aqui o don,

11:52

desenvolveu para don, desencadeou, o webhook vai lá para a nossa API,

11:58

mas então fizemos essa parte, agora nós vamos criar a última parte,

12:03

Que nós vamos criar... que nós vamos construir esse workflow,

12:06

que é aprovar esse reembolso acima do teto.

## Resumo IA

[RESUMO_IA]