Módulo: Desenvolvimento de Agentes com IA\
Aula: [Finalizando o workflow com RequestInput](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18577)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos fazer a confirmação desse estorno que está acima do teto,

00:05

dado o processo que nós criamos. Porque agora nós temos esse

00:12

escalonamento,

00:16

depois que

00:19

se cria no linear, cria-se também no banco de dados, chegou aqui na triagem, aí

00:27

nós temos que parar o processo como se fosse uma tool confirmation.

00:32

Nós já aprendemos durante essa disciplina,

00:35

para que um usuário autorizado possa fazer a confirmação.

00:41

Porém, nesse caso, nós não temos uma tool.

00:45

Vamos voltar aqui para o código, porque quando chega na triagem do escalonamento,

00:51

se eu verifico que não há falha e que tem o Refund Confirmation, o que nós vamos fazer?

01:02

Nós já poderíamos resolver aqui, mas...

01:05

sempre a dica que eu estou mostrando nesse capítulo. Sempre crie nós menores,

01:11

porque fica fácil na hora de você ver o graph,

01:13

fazer debug, a IA,

01:14

também na hora que você estiver desenvolvendo o seu agente de IA com IA,

01:18

fica tudo mais fácil.

01:19

Então, na verdade,

01:20

aqui eu vou criar uma nova rota

01:24

que eu vou chamar de Refund Await Input,

01:30

porque vai precisar de uma entrada do usuário. Então, disso,

01:38

vai desencadear, vamos

01:41

abrir o agent do workflow, então

01:47

nós vamos ter refund, await, input.

01:51

Então eu vou criar o await, refund,

01:58

input, node. Então

02:05

vai ser mais um nó, aqui

02:08

nós vamos colocar async, def, com o mesmo nome,

02:12

e aqui eu não tenho nenhuma informação, obviamente nós...

02:18

Podemos receber alguma coisa aqui, nós já aprendemos a passar através do output,

02:21

mas eu não tenho nenhuma necessidade.

02:23

O que nós vamos retornar aqui vai ser um request input, que

02:29

ele é parecido com o tool confirmation, na verdade é muito parecido.

02:33

Então aqui de eventos nós vamos requisitar o request input.

02:42

Nele nós vamos definir primeiro qual é a mensagem que vai aparecer para o usuário.

02:47

Vai aparecer o irmão da KWeb, ou que a gente mostraria...

02:51

para alguém que estivesse manipulando numa outra interface.

02:56

A gente pode colocar assim,

02:58

aprovação humana

03:03

necessária para o refund, algo do tipo.

03:10

Vamos colocar para o store.

03:16

A ideia é passar, eu

03:21

vou colocar de uma forma mais didática,

03:24

mas obviamente não precisaria ser dessa forma.

03:27

Vou colocar assim, responda com...

03:32

confirmed igual a true para provar

03:36

ou confirmed igual a false para provar.

03:39

Lembra do que nós já fizemos de tool confirmation?

03:42

Em alguns dos exemplos, temos aqui tool confirmation.

03:49

Será que é exatamente esse?

03:52

Exatamente isso aqui.

03:54

Temos o Tool Context, verificamos ali no Tool Confirmation se é Confirmed.

03:58

Aqui é a mesma ideia. Então, temos essa primeira parte.

04:03

Agora, a segunda vai ser o Response Schema, para

04:09

que a gente delimite padrão conforme as informações que nós queremos.

04:14

Pense que nesse Request Input nós poderíamos preencher sem

04:20

o Confirmed True ou qualquer coisa que a gente quisesse.

04:23

Então, aqui é um JSON Schema. Vou falar que ele é do tipo Object.

04:29

Nós vamos receber um Confirmed que é do tipo Boolean.

04:34

Pronto. É

04:38

somente isso. Mas aqui carrega -se muito mais

04:43

lógica, em termos do que vai acontecer por trás. Então, quando

04:49

redirecionar para esse Refund Await Input, vai

04:57

bater aqui, por causa da nossa rota.

05:08

Mas ainda não acabou. Por quê? Quando eu tiver o

05:14

Await Refund Input Node, aí

05:19

eu posso tomar duas decisões.

05:22

Alguém já confirmou que tem que fazer o reembolso.

05:26

Então, eu poderia reusar o

05:31

AutoRefundNode, porque

05:36

ele já faz todo o reembolso para

05:39

a gente, ou

05:42

até criar um outro nó que faria, às vezes,

05:45

esse reembolso de uma maneira um pouco diferente.

05:49

A princípio, eu não quero mexer no AutoRefundNode, porque vai ser idêntico,

05:54

mas nós temos que verificar se tem aquele Confirm para provar ou não.

05:58

Como nós já vimos lá com o ToConfirmation.

06:01

Então, eu vou criar mais um nó, só

06:06

para deixar separado, acho que isso vai ser bom,

06:09

vou fazer a função de RefundWithConfirmation.

06:16

Então, nós vamos receber aqui um NodeInput, vou colocar como dicionário genérico,

06:22

porque nós não vamos...

06:25

nós vamos receber o retorno disso aqui,

06:30

tipo... de um dicionário, que não tem um tipo forte, não é nada do PyIdentic.

06:37

Nós vamos receber, na verdade, um CONFIRMED igual a TRUE.

06:42

Então, nós colocamos esse dicionário genérico.

06:45

Primeira coisa, vamos pegar o TICKET ID.

06:51

Nós precisamos pegar ele do contexto também. Então, preciso aqui do contexto.

06:59

E a gente pode fazer aquela mesma verificação,

07:01

que eu não estou preocupado com repetição de código.

07:06

Consultamos, e aí se o ticket não existe, ticket não encontrado.

07:10

Então agora eu pego o Confirm, e

07:14

ele está no Node Input, porque quando voltar,

07:17

então isso aqui vai ser a entrada do meu nó.

07:22

Então, se eu tiver, se não Confirm, nós

07:31

vamos falar que foi analisado, que não foi aprovado,

07:35

então ele vai ser resolvido e salvo. Agora...

07:40

Caso seja aprovado, então nós vamos processar o reembolso.

07:47

E aí o que nós fizemos aqui em cima vai ser exatamente esse mesmo código.

07:54

Ele tem a resposta final.

08:05

Ok, então eu tenho acesso ao nosso billing fake, ele

08:12

chama o issue refund, tem aqui o response e salva.

08:18

Mas veja que nós temos erros de variáveis que nós não temos aqui.

08:23

Nós não temos...

08:24

Nós não vamos ter essa informação no Node Input,

08:28

diferente do Auto Refund que nós criamos o Auto Refund

08:31

anteriormente com essas informações.

08:37

Então eu preciso do

08:40

Refund Amount, Refund SKU e

08:45

só. São essas informações aqui. E do Refund Mouth também.

08:51

Então, como que nós vamos lidar com isso? É porque...

08:56

Eu preciso capturar essas informações e o

08:59

último lugar que nós manipulamos essas informações é

09:08

antes aqui na triagem. Nós temos essas informações aqui na triagem.

09:15

Então nós podemos adicionar essas informações como state delta aqui ou

09:22

poderia adicionar até aqui na triagem.

09:26

Eu vou preferir adicionar aqui por mais formalidade, então nós vamos colocar state delta,

09:37

então refund, amount, month e o sku.

09:42

Que aí eles vão fazer parte do state, então veja que tem essa diferença.

09:50

Nós vamos pegar essas informações, vou colocar assim, refund, amount,

09:55

pega do state, month e o sku. Então aqui

10:01

mudamos para as variáveis e aqui também mudamos para as outras. Pronto.

10:11

Agora, esse Refund with Confirmation,

10:15

ele vem para o nosso agente aqui. Ótimo.

10:27

Agora vamos recarregar aqui só por precaução e

10:35

vamos fazer o teste. Então, vamos criar

10:41

um novo ticket. Eu vou reusar a mensagem que a gente já tinha feito.

10:46

Então, o usuário aqui continua... Na verdade, aqui precisa ser o C204. Vou criar nova sessão.

10:55

Mando a questão do estorno de junho de 2026.

11:01

Ele vai registrar o ticket.

11:04

Vamos criar uma nova seção no ticket resolution.

11:07

Então, aqui vem o ticket ID com o valor. Então, vamos lá.

11:18

Já está buscando a fatura. Refund confirmation.

11:23

E a gente vai ver que ele vai parar o processo.

11:26

Ele vai pedir que... vai ser idêntico ao to confirmation.

11:34

Agora ele vai escalonar lá no linear.

11:43

Está salvando a sessão no linear,

11:46

criando o ticket escalonamento localmente.

11:51

E agora vem o ADK request input, com

11:57

o que nós colocamos. Então ele vai dar já a opção, como temos

12:01

um JSON esquema que define toda a tipagem, nós temos a definição em JSON,

12:07

payload, podemos passar, inclusive o payload é interessante.

12:13

Eu poderia passar essas informações também ali do refund, mouth e outras coisas,

12:18

que eu mostraria para o usuário, olha,

12:21

você autoriza essa operação, envolve essas informações, tem esse valor,

12:28

esses valores aqui envolvidos. Então, ok, eu marco aqui,

12:33

como ele já está me dando a opção,

12:34

e submeto novamente. Pronto, então,

12:36

seu pedido foi aprovado. Então, agora vamos olhar o que aconteceu.

12:45

Então ele foi para o awaitRefundInputNode e o RefundWithConfirmation.

12:53

E assim nós terminamos esse fluxo que é o mais complexo do nosso grafo.

13:01

Então, lembrando mais uma vez o que nós criamos aqui, nós

13:08

criamos um fluxo com o escalonador que ainda é potente,

13:11

porque se acontecer qualquer reexecução e é possível, nós

13:16

não vamos correr nenhum risco de duplicar isso.

13:20

no linear, ou até mesmo duplicar linhas no banco de dados.

13:24

Utilizamos essa opção aqui para requisitar essa autorização de restore.

13:31

Então, terminamos o nosso workflow.

## Resumo IA

[RESUMO_IA]