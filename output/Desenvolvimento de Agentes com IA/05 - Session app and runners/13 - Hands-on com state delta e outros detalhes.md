Módulo: Desenvolvimento de Agentes com IA\
Aula: [Hands-on com state delta e outros detalhes](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18488)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre o State Delta.

00:03

É muito importante entender o que é ele e a diferença para o State principal.

00:08

Nós já sabemos que uma sessão tem vários eventos e também tem o State,

00:12

que não é nada definitivo, ele é modificado ao longo da execução dos agentes.

00:19

O State Delta, ele está ligado com o evento.

00:23

Um evento pode ter o State Delta,

00:26

pode porque não é obrigatório que você tenha... algum tipo de dado.

00:32

E esse delta significa a diferença,

00:35

significa que é um state que

00:38

vai causar uma transformação no state principal.

00:43

Então é essa diferença que vai ser aplicada.

00:48

E esse state pode ser um resultado,

00:51

esse state delta pode ser um resultado de um agente,

00:54

assim como algo que é produzido dentro de uma tool.

00:59

Esses são os dois jeitos

01:02

principais de mudarmos o State Delta.

01:06

Vamos começar enxergando pelo prisma do agente.

01:12

Eu tenho o operador da conta,

01:13

que nós já estamos trabalhando há um bom tempo,

01:15

assim nós assimilamos mais os conceitos passados.

01:19

Podemos passar uma output key.

01:23

E aqui eu vou colocar operador,

01:28

conta, resultado. Ao

01:34

colocar essa output key,

01:36

Então nós vamos ter o state delta com essa chave e

01:42

vai ser o resultado que esse agente vai retornar e vai

01:47

acabar indo lá para o usuário da forma que nós fizemos.

01:51

Então vamos aqui no web para

01:55

ver como que nós podemos acessar essa informação.

01:59

Nós temos o evento final que é o que nós queremos capturar.

02:04

Então aqui eu vou colocar um print.

02:09

para capturar o evento .actions .stateDelta.

02:17

Veja que ele é um dicionário do Python, chave-valor, não tem nada complexo.

02:22

Então eu posso jogá-lo num print, que eu consigo capturar todas as informações.

02:28

Assim como eu posso pegar com a anotação de get, posso usar a anotação de array,

02:35

como em outras linguagens, para poder pegar o valor, enfim, tem... muitas formas.

02:39

Bom, vamos lá.

02:44

Então eu vou rodar o

02:47

projeto e

02:51

agora com o API HTTP vamos

02:56

criar uma nova sessão e

03:00

passá-la numa mensagem.

03:05

Não vai ter nenhuma mudança com o retorno,

03:07

nós vamos ter aquele retorno que ele vai acabar. Agora, como nós temos o

03:12

ID do cliente já sendo passado direto,

03:15

aqui nós temos o retorno de todas as faturas. Mas agora vamos olhar no terminal.

03:22

Então eu tenho operador conta resultado exatamente com o mesmo resultado.

03:29

Então nesse caso com o output key é

03:34

outra maneira que eu poderia pegar essa informação.

03:37

Eu conseguiria fazer aqui em get operador conta resultado ao invés de pegar do

03:45

Event Content Parte 0. Text que nós já tínhamos feito isso.

03:50

Aí nós poderíamos pensar assim,

03:52

por que eu pegaria a saída de um

03:56

agente do State Delta ao invés do partes.txt?

04:01

Veja só, nós temos vários agentes nesta aplicação,

04:06

apesar de que nós já vimos a questão dos modos do agente,

04:11

que tem o task e o single churn, nós

04:14

devemos lembrar sobre a forma que eles vão fazer o agente trabalhar,

04:19

que é... os agentes vão ser chamados como tool,

04:22

mas você vai ter cenários que o modo dos subagentes, por exemplo, vai ser chat.

04:31

Então, veja que este evento final,

04:35

ele poderia ser produzido pelo coordenador,

04:40

pelo subagente de faturas, pelo agente de assinaturas, e

04:46

seria difícil saber qual é o agente que está produzindo este evento.

04:51

Então o State Delta ajuda nesse sentido,

04:54

porque se você colocar um output key em todos os seus subagentes,

05:01

você consegue identificar facilmente vendo qual é a key que está

05:05

presente aqui neste State Delta de um evento que é isFinalResponse.

05:10

Você consegue identificar, então às vezes você vai fazer alguma coisa neste código

05:18

dependendo de qual é o agente que executou aquela solicitação.

05:22

Então isso aqui também ajuda nesse sentido.

05:26

Agora no ADK Web nós podemos ver que ele é alinhado com o State Global.

05:32

Eu coloquei uma lista minha de faturas sem ter um State associado,

05:36

obviamente ele não vai conseguir encontrar.

05:38

Então temos o texto que foi associado. Mas quando nós olhamos para...

05:47

este evento, que é exatamente o último que aconteceu,

05:51

nós conseguimos ver o

05:56

State Delta. Esse aqui não é o State Global,

06:00

esse aqui é o State Global e aqui é o Delta.

06:02

Então temos um valor, um old value e um new value.

06:08

À medida que esse agente vai interagindo, nós poderíamos ter daqui a pouco aqui, eu

06:15

quero fazer aqui um State colocando

06:20

o cliente ID.

06:23

que é igual a cliente 1, 2, 3.

06:29

Acho que aqui agora ficou certo.

06:31

Então, ao fazer isso, vou pedir para listar minhas faturas.

06:41

Pronto, então agora eu tenho as minhas faturas.

06:44

Então, neste evento final, eu

06:51

consigo ver o novo valor e o valor antigo.

06:57

Então, nós temos todo esse rastreamento do que está acontecendo.

07:01

Essas mudanças são todas registradas neste histórico da sessão.

07:06

Os eventos fazem parte da sessão e tudo isso fica gravado ali,

07:10

seja em qual armazenamento que você quiser. Então, isso aqui é algo poderoso.

07:16

E nós vamos brincar mais um pouco, veja só o que nós vamos fazer aqui agora.

07:22

Nós vamos adicionar mais um agente nessa brincadeira,

07:25

que vai ser um agente de pesquisa de satisfação da Acme.

07:31

A ideia é que a gente faça uma pesquisa de satisfação para conduzir...

07:37

o cliente e perguntar qual é a experiência com os serviços da Acme.

07:41

E aqui eu estou colocando apenas um

07:44

formato que ele precisa produzir esse resultado.

07:50

Que é o feedback, que é o que o cliente está achando dos serviços, e um sentimento,

07:55

que seria a partir da mensagem que ele enviou, se é um sentimento positivo,

08:00

neutro ou negativo. E quando ele fizer a pesquisa,

08:07

Ele precisa voltar para o agente pai. Nós vamos ter uma situação interessante aqui.

08:14

Este agente está no modo chat.

08:17

Nós não fizemos nenhuma mudança, exatamente porque,

08:21

numa pesquisa de satisfação, poderíamos fazer várias perguntas.

08:27

Também temos uma ferramenta, apenas para poder fazer uma brincadeira,

08:32

que eu quero identificar se o cliente já respondeu à pesquisa.

08:37

Então, aqui no web, eu fiz até uma modificação em relação ao getUser,

08:43

onde está a nossa função.

08:46

Posso passar um userId para pegar o cliente123 que já existia,

08:52

agora o cliente456.

08:55

Então, nós extraímos a informação do cliente em específico,

09:01

retornamos o cliente123.

09:03

Enfim, daria até para poder reduzir e melhorar esse método aqui.

09:07

Aqui em cima, tanto na listagem de faturas quanto de assinaturas,

09:12

eu adicionei mais alguns dados para que nós tenhamos este outro cliente.

09:17

Então, a ideia, para que a gente possa exercitar esse conhecimento,

09:21

é que uma vez que o coordenador vai ser lançado,

09:26

ele vai ver se aquele cliente já respondeu à pesquisa de satisfação.

09:31

Obviamente, se for o cliente 123, ele já respondeu.

09:36

Se ele já respondeu...

09:38

o coordenador vai redirecionar para o agente de faturas ou de assinaturas.

09:43

Caso contrário, ele vai fazer a pesquisa de satisfação,

09:48

aí a gente poderia registrar, fazer qualquer outra coisa.

09:51

E eu quero ligar esse ponto com o que esse agente produzir,

09:56

eu quero usar no subagente de assinaturas.

10:01

A gente poderia criar uma estratégia que, se a pesquisa de satisfação...

10:05

com o cliente, é negativa e ele está querendo cancelar,

10:09

poxa, eu já entendi que ele não está gostando.

10:12

Talvez eu possa oferecer um desconto ou algo nesse sentido.

10:16

Então, nesse cenário, veja,

10:18

um subagente de pesquisa vai precisar dar as

10:22

informações para o agente de assinatura.

10:25

Como que nós vamos fazer esse compartilhamento dessas informações?

10:31

Através do state.

10:33

No agente coordenador,

10:35

eu coloquei que, antes de fazer qualquer interação que o cliente queira,

10:41

antes

10:43

de responder qualquer pergunta,

10:44

você deve verificar se o cliente já respondeu à pesquisa de satisfação.

10:48

Vou até tirar essa questão aqui dos últimos três meses.

10:51

A gente só quer fazer uma verificação básica. Se não,

10:55

você deve conduzir a pesquisa de satisfação

10:58

utilizando o subagente de pesquisa de satisfação.

11:02

Eu já adicionei ele aqui e ele tem um nome,

11:05

nós já sabemos que é possível identificar pelo nome.

11:08

Aqui nós não vamos usar o autoflow,

11:10

nós vamos dar uma ordem para que ele chame esse cara.

11:13

Então só depois de responder à pesquisa, aqui nós vamos dar continuidade.

11:19

Pois bem, eu vou reposicionar essa tool que já,

11:22

da questão de já responder à pesquisa, que nós não demos nenhuma instrução.

11:27

de como ele vai fazer essa verificação, você já respondeu à pesquisa.

11:31

A instrução está no coordenador. Eu tinha colocado no agente errado. Então, ok.

11:40

Temos o reload aí, gente, rodando com o DKWeb. Então, vamos...

11:45

Eu tinha feito o teste antes e tinha identificado essa questão.

11:50

Então, eu vou colocar aqui o

11:55

cliente ID

11:58

é igual ao cliente 456, que é o que não respondeu à pesquisa.

12:06

Então, vou pedir para listar minhas faturas.

12:10

Ele vai ter que mostrar a pesquisa de satisfação,

12:12

está vendo? Ele executou a tool.

12:15

Então, antes de prosseguirmos com a consulta de faturas,

12:17

gostaria de realizar uma pesquisa de satisfação.

12:20

Como tem sido a experiência com o serviço da Acme?

12:23

Nós conseguimos ver aqui o agente de pesquisa de satisfação. Então,

12:28

eu posso falar assim, eu quero criar um sentimento negativo. É ruim, cara.

12:38

Aqui acontece um problema.

12:40

E eu estou aproveitando, isso não tem nenhuma relação direta com o State Delta,

12:46

mas é aproveitando o gancho por conta dessa situação,

12:49

isso vai acontecer no seu dia a dia,

12:51

você precisa entender essas limitações ou como as

12:56

coisas estão acontecendo e se comportando.

12:58

Porque se eu estou mandando essa mensagem,

13:00

o agente roxinho, que é o de pesquisa de satisfação,

13:03

que deveria receber essa mensagem, mas veja quem está recebendo ela, o

13:09

operador da conta.

13:13

Então, acontece aqui até a transferência para a pesquisa de satisfação,

13:18

mas ela não acontece. Ele não terminou a pesquisa.

13:24

Isso acontece porque nós temos o runner e

13:32

subagentes que

13:35

o modo é igual a task.

13:40

Quando eu tenho isso, não é interessante que eu tenha um subagente em modo chat.

13:50

Quando o runner vê que tem uma nova mensagem e

13:53

eu tenho pelo menos um subagente modo task,

13:56

ele vê que o task não vai conseguir agir sozinho.

13:59

Então, o coordenador que vai entrar em ação.

14:02

Então, ele sempre repassa a mensagem para o coordenador.

14:06

Então, quebra aqui no caso do chat.

14:09

Então, veja só aqui a questão de decisão de arquitetura dos nossos agentes.

14:15

Ou eu mudo os três para chat, então não tenho mais esse problema.

14:20

Ou eu passo a pesquisa de satisfação para

14:27

subagent.

14:30

Ou melhor, passo a pesquisa de satisfação, ele já é um subagent,

14:34

eu passo ele para modo task também, porque

14:39

aí não teremos esse problema.

14:42

Então, vamos fazer aqui essa mudança de pegar a pesquisa de satisfação,

14:49

alterá-lo para task, e

14:56

agora nós vamos criar uma nova interação.

14:59

Então, vamos

15:01

adicionar novamente o cliente ID, é igual ao cliente 456.

15:10

E agora eu vou colocar list minhas faturas.

15:19

Agora nós vemos pesquisa satisfação, vou colocar é caro e ruim.

15:27

Então, nós vemos que o agente de satisfação continua ativo.

15:32

Então, ele compreendeu que há

15:36

problemas.

15:41

Fez aí o seu lamento e como a pesquisa foi concluída, posso dar continuidade à sua

15:50

solicitação. E aí nós temos

15:55

que tomar o devido cuidado aqui,

15:58

porque o erro aconteceu exatamente por conta dessa instrução,

16:02

que a gente está pedindo para fazer a transferência de volta, e isso vai ser

16:08

contraditório em relação à tool de finish task. Então a gente teria que tirar...

16:13

essa linha daqui. Eu não quero perder essa linha, então vou deixá -la comentada. Então pronto.

16:20

Vamos atualizar aqui novamente a interação.

16:26

Então temos

16:29

que colocar novamente o cliente ID e

16:38

eu vou listar minhas faturas.

16:44

É caro e ruim.

16:49

Já mudou para pesquisa satisfação. Agora sim aconteceu o finish task.

16:53

Então agora ele vai listar

16:54

as faturas. Então, aconteceu

16:56

corretamente.

16:59

Ok, então eu tenho esse modo task que ele não me atrapalhou,

17:05

nós já vimos que ele pode pedir mais informações para o usuário,

17:08

então está dentro do que aconteceu.

17:11

E aqui no caso da nossa pesquisa de satisfação, temos

17:17

o resultado dela, que o feedback relatou que o serviço é caro e ruim,

17:21

e o sentimento é negativo. Ótimo. Agora,

17:28

Ao chegar aqui, eu

17:31

posso colocar que

17:33

eu quero um output key para pesquisa, satisfação e resultado,

17:39

porque eu quero usar essa informação no meu subagente de assinatura.

17:45

Então, vamos lá novamente.

17:47

São muitas camadas.

17:49

A gente está experimentando situações para entender o comportamento do ADK.

17:57

Nós já vimos ali a questão da...

18:00

task versus chat quando elas estão no mesmo coordenador. Então,

18:06

vou colocar aqui list minhas faturas novamente e eu já vou aproveitar para...

18:12

Ah, não vai deixar eu digitar caro e ruim, depois que ele terminar.

18:18

Então, veja que eu tenho aqui o meu state que

18:28

foi determinado.

18:35

Então, quando eu coloquei que é caro e ruim, ele foi para o finish task

18:43

E veja só, neste evento aqui, nós deveríamos ter,

18:49

na verdade aqui, eu deveria ter o output key,

18:54

mas veja que o output key, ele veio apenas na primeira mensagem do,

19:02

manifestação da primeira mensagem do usuário. Depois que eu coloquei a car e win,

19:07

esse result que está aqui, ele vai para o finish task e ele acaba não entrando no

19:15

state delta do evento.

19:18

Então isso é ruim, eu não tenho as informações aqui.

19:24

Então quando eu tenho single churn e task,

19:26

o output key não vai funcionar corretamente.

19:31

Então nós precisamos entender essas limitações para fazer os

19:34

ajustes e escolher qual é a modelagem desses agentes. Isso é muito importante.

## Resumo IA

[RESUMO_IA]