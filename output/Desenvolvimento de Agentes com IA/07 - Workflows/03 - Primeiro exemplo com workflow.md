Módulo: Desenvolvimento de Agentes com IA\
Aula: [Primeiro exemplo com workflow](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18567)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos criar o primeiro exemplo com workflows.

00:04

Eu não quero já sair criando alguma coisa do Ticket Resolution,

00:07

mas só o que nós vamos já fazer de primeiro exemplo já vai

00:12

permitir que a gente entenda várias coisas ao

00:15

em volta desse ecossistema do workflows.

00:18

Mas vamos criar então a pasta do Ticket Resolution, porque já vai ficar criada.

00:27

E dentro dela... o agent.py. Então, veja que mesmo trabalhando com workflows,

00:33

nós queremos trabalhar com as boas práticas do ADK.

00:40

Porque aí, na hora que eu rodar o ADK Run, o ADK Web,

00:43

ele vai encontrar a pastinha com o agent.py.

00:48

Então, a nossa ideia é criar também o root agent,

00:51

só que ele vai ser igual ao workflow.

00:55

Nós vamos importar esse workflow de google.adk import

01:03

Workflow. Dentro dele nós vamos passar um nome e aí é

01:07

aquela mesma história de definir o nome do agente,

01:09

então TicketResolution,

01:11

esse nome que vai aparecer lá no topo do DecalWeb, é como se fosse o nome do agente.

01:15

Tem a descrição dele que é importante também fazer a definição.

01:21

Aqui eu vou colocar descrição do

01:27

agente. Eu não quero definir nada nesse momento,

01:30

mas é bom que a gente já... Entenda isso.

01:33

E a parte mais importante que é a parte dos edges, onde nós vamos definir os nós.

01:41

Então declaramos o array do Python, que é a lista, e

01:48

aí criamos várias tuplas, que

01:52

vai ser a definição de cada nó.

01:56

Aqui nós não vamos desenhar o grafo e colocar setinhas.

02:02

Quando nós estamos falando de tupla,

02:05

é importante explicar, principalmente se você não tem

02:09

experiência com Python, ela também é um tipo de array, só que é um array imutável.

02:16

Então, uma vez que você define a tupla,

02:18

você não consegue pegar aquele objeto e adicionar um elemento, remover.

02:24

Então, a tupla faz com que nós tenhamos

02:27

uma estrutura mais eficiente para poder lidar,

02:30

ela é mais rápida,

02:31

utiliza menos memória, porque ela não tem que ficar alocando...

02:35

se preocupando em alocar mais memória. Definiu a tupla, acabou.

02:39

Então, por isso que nós podemos definir aqui,

02:43

na verdade, o grafo conforme a gente quiser.

02:45

A questão é que você defina certo. O start pode estar aqui,

02:49

como pode estar aqui em cima.

02:50

O ponto é que tem que ter o start para o

02:53

ADK saber como que ele começa a montar esse grafo.

02:56

Então, não precisa definir isso aqui de forma ordenada,

02:59

mas é óbvio que nós vamos definir de forma ordenada.

03:02

para que fique fácil o entendimento, fique legível.

03:06

Até mesmo se a gente passa de forma desordenada,

03:09

pode ser que a gente faça coisas erradas.

03:12

Então, nós temos que importar o google.adk.workflow import start,

03:19

totalmente em maiúsculo.

03:22

Então, aqui vem o start.

03:24

É o primeiro nó.

03:25

O start é

03:29

um base node. Na verdade, tudo é um base node,

03:31

se a gente for olhar no final das contas.

03:35

Então esse nó inicia, mas eu tenho que fazer alguma coisa.

03:38

Então eu tenho que passar aqui uma tool,

03:39

uma function code ou um agente. Como nós não criamos nada,

03:43

vamos usar o próprio recepcionista para isso. Então eu vou colocar

03:48

agents .ticketReceptionist .agent import

03:55

rootAgent e aí eu vou colocar um alias,

03:59

porque senão vai confundir com essa variável que aqui está. Então...

04:05

Vamos passar lá para cá.

04:09

Ok, está montado aqui o meu primeiro workflow,

04:13

que na verdade é só a execução do próprio agente, não vai mudar nada a princípio.

04:20

Nós vamos ter o agente sendo executado da mesmíssima forma.

04:25

A questão é que na hora que nós vamos tendo o nosso gráfico,

04:28

vai tendo as várias tuplas e nós vamos tendo aqui um monte de coisas.

04:32

Isso aqui pode ficar gigante. Vamos executar este agente.

04:37

Então, eu vou rodar a DKWebTicketResolution. Da mesma forma, ele vai subir o agente.

04:44

Nós vamos tê -lo aqui.

04:47

Então, TicketResolution, tudo bonitinho.

04:51

Vamos colocar que nós queremos criar um

04:55

ticket para informar erro de integração com

05:01

GitHub. Mesma coisa, gente.

05:04

Erro 500.

05:10

Veja só, já apareceu aqui o

05:14

diagrama e agora nós temos um grafo.

05:19

Ele fez a primeira parte corretamente,

05:22

mas deu um erro aqui no final.

05:25

Então tem o start, iniciou,

05:28

foi para o ticket receptionist e teve o final que foi com um erro.

05:32

Não tivemos nem a execução do registrar ticket.

05:38

Então o princípio se comporta da mesma forma.

05:44

Por que aconteceu esse erro aqui?

05:46

Ele falou que no function call

05:49

foi encontrada para function response id.

05:54

Ele está dando esse id aqui.

06:04

Vamos voltar para o VS Code.

06:07

Eu vou copiar esse

06:12

trecho e substituir por esse id para correlacionar com o que a gente tem.

06:18

Nós tivemos quatro eventos acontecendo.

06:21

O primeiro evento que eu quero criar um ticket, o segundo.

06:26

Aqui nós estamos considerando que isso aqui foi enviado para a LLM,

06:28

aí a LLM pediu para fazer um function call para o ticket classifier,

06:34

lembrando que o nosso subagente é um single turn, então é como se fosse uma tool.

06:38

Então é ticket classifier passando parâmetro,

06:44

devolve a resposta.

06:47

Então isso aqui é um function call que

06:50

a LLM considera e depois temos o function response.

06:57

Então, quando isso acontece, o ticket classifier devolve o JSON,

07:03

Então há o function response sendo enviado lá para a LLM.

07:10

E a LLM precisa que tenha um ID relacionado,

07:14

é uma identificação para aquela função que está acontecendo,

07:17

porque depois, quando nós mandamos tudo,

07:20

lembrando que a LLM é stateless, ela não guarda nada, nós

07:26

precisamos sempre enviar as coisas para ela.

07:28

Porque quando nós enviamos o function response desse ID,

07:31

nós falamos que há esse function call.

07:37

Então, ela relaciona o function call com o response.

07:41

Toda function response precisa ter uma function call.

07:45

Mas isso, na verdade, não aconteceu.

07:47

O que ele está dizendo aqui é que, olha, para essa function response, eu

07:53

não tenho function call.

07:55

Isso acontece exatamente por conta do comportamento padrão do workflow.

08:00

O nosso agente é

08:05

um modo chat.

08:08

Só que quando nós o declaramos sem definir o modo chat,

08:14

o workflow muda ele para single churn.

08:17

E aqui que é o segredo do erro. Não foi nada de errado que nós fizemos.

08:24

Então, assim como o ticket classifica single churn,

08:27

também ele se transforma dessa forma.

08:30

E quando é um single churn, é adicionado um include,

08:36

Contents igual a None.

08:37

Justamente para que não signifique que esse include content

08:42

não significa que não vai trabalhar com nenhum conteúdo.

08:45

A ideia é que eu não adicione o histórico

08:49

de conteúdos na hora de mandar para a LLM.

08:53

Então aquele agente ali não vai pegar todo o histórico.

08:56

Ele está se comportando apenas como uma ferramenta.

09:01

Então a ideia no single churn é que ele pegue...

09:06

O último, na verdade, o primeiro evento,

09:08

ele verifica de trás para frente, do último para o primeiro.

09:13

Vai pegar o primeiro evento cuja autoria da resposta não é dele.

09:19

Então, pense que o receptionist vai enviar esse function response aqui.

09:26

Então, ele vai olhar para

09:30

o evento 3. Ah, tem ali a resposta do ticket classifier.

09:34

Ah, o autor é outro agente, então...

09:39

ele não vai pegar mais nenhum outro conteúdo,

09:42

justamente para poder fechar esse escopo mais simplificado.

09:48

Então, enviando apenas essas duas coisas, ele

09:52

não envia o function call. Ele deveria, na verdade, enviar tudo, né? Nesse caso.

09:58

Então, como ele não envia um function call,

10:01

a LLM dá aquele aviso. Então, mudando o nosso agente para chat,

10:07

fazendo justamente isso aqui, vai mudar tudo.

10:14

Então, nós vamos ter o mesmo comportamento que tínhamos antes.

10:17

Então, é importante entender essas nuances, porque

10:21

veja, não é tão simples. Temos meio que uma cilada por trás.

10:28

Nós vamos ver que agora ele

10:31

vai conseguir fazer a criação. Então, registrar ticket e pronto.

10:35

Então, o nosso grafo foi executado desde

10:42

Aqui de cima. Temos o start e o end. Então, ticket Receptionist.

10:49

Obviamente o single channel vai aparecer, mas ele executou, aí vem registrar ticket,

10:53

aí teve o envio, a setinha, voltou, e agora a resposta final.

11:01

O workflow faz isso porque ele entende que a princípio nós estamos

11:05

enviando uma mensagem e essa mensagem

11:09

vai já ser processada direto por

11:16

esse pipeline. Ela vai navegando até terminar.

11:21

Obviamente nós podemos ter o

11:25

workflow que

11:28

o chat precisa do controle, né?

11:31

Desse controle, inclusive

11:35

até para fazer perguntas e etc. Porque se ela é um single churn,

11:39

ele não vai poder interagir com o usuário. Mas enfim,

11:42

então temos aqui o nosso primeiro exemplo,

11:45

já aprendemos mais coisas sobre o modo single

11:49

churn e também detalhes específicos sobre o workflow.

## Resumo IA

[RESUMO_IA]