Módulo: Desenvolvimento de Agentes com IA\
Aula: [Agentool e integração ao atendimento ao grafo](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18571)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos integrar o agente de atendimento geral,

00:04

que responde às dúvidas gerais,

00:05

faz até operações da conta através do subagente operador da conta,

00:11

ao nosso grafo. Nós vamos integrá-lo ao workflow do Ticket Resolution.

00:16

Então, nós voltamos para a triagem, que é esse novo caminho.

00:20

Se ele não for Out of Scope,

00:23

nós retornamos um evento em que nós vamos definir a rota.

00:31

Vamos colocar o mesmo nome do agente, porque aí vai ficar fácil.

00:37

Em inglês também, até poderíamos mudar o nome desse atendente,

00:43

porque às vezes o nome Customer Service é o

00:47

nome que seria mais adequado ao atendimento,

00:50

mas aí Service pode gerar confusão no meio do nosso projeto.

00:54

Então eu vou manter esse nome aqui mesmo.

00:57

Então, dessa forma, nós

01:00

vamos vir aqui.

01:03

E aí, quando for o attendant,

01:07

ele vai para o nó, que é o subagente.

01:13

Ele importou certo aqui agora, acho que sim,

01:15

é porque ele tem um delayzinho até assumir essa mensagem.

01:19

Porém, isso aqui não vai ser suficiente,

01:21

porque o nosso atendente necessita de duas informações que precisam estar no state,

01:27

o ticket message e a classification justification.

01:31

Mais o operador da conta que precisa do Customer ID,

01:34

mas ele precisa também da mensagem que já estaria no State.

01:38

Então, nós precisamos adicionar essas informações no

01:42

State antes de realizar o redirecionamento.

01:46

Elas já vão ser acessíveis. Então,

01:48

nós usamos o ContextState passando o TicketMessage.

01:53

É só pegar as informações que nós já temos. E tem o Customer ID.

01:58

É tudo bem do Ticket.

02:00

Aqui nós poderíamos pegar também o context e o user ID.

02:08

Mas é até bom pegar com o ticket Customer ID,

02:12

porque a gente não teria que mudar o usuário na hora de usá-lo no ADK Web,

02:16

mas na hora de criar com o ticket receptionist,

02:20

nós vamos ter que mudar o usuário para poder brincar com a questão da conta.

02:24

Se eu quero apenas testar uma resposta genérica, não precisamos mudar o

02:31

ID do usuário, que vai acabar sendo o Customer ID. Então, pronto.

02:35

Com isso aqui, o nosso agente vai ser executado,

02:37

mas e agora o final desse grafo?

02:41

Porque temos o atendente,

02:45

e o que vai acontecer depois daqui?

02:47

Nós vamos precisar salvar as informações no banco de dados.

02:52

E essa discussão, essa visão sobre como fazer isso é importante,

02:56

porque vem mais uma vez o contraste do determinismo versus o não determinismo.

03:03

Nós poderíamos chegar nesse atendente, no

03:08

System Prompt, e colocar uma tool que vai realizar esse salvamento.

03:13

Ah, então depois que você finalizou tudo,

03:16

então salve aqui as informações do ticket e segue a vida.

03:20

Mas veja,

03:21

uma vez que a gente tem esse workflow e

03:24

A oportunidade de fazer essa operação de forma linear, nós

03:31

Vamos... economizar mais complexidade no System Prompt.

03:35

Vamos ver se isso aqui depois pode ir mudando.

03:38

Não deixamos chance para o acaso.

03:42

Nós vamos ter certeza, não vai restar nenhuma dúvida,

03:46

que depois desse agente nós vamos salvar de fato.

03:52

Então, eu gosto dessa ideia do determinismo,

03:56

essa ideia de ter um nó para um nó pós que resolve.

04:03

O que o agente anterior fez,

04:05

isso não significa que eu estou dizendo aqui que o agente

04:09

não tem que salvar nada no banco de dados,

04:11

não tem que escrever nada.

04:13

Não, mas esse resultado que está saindo do agente nós podemos deixar para um nó.

04:18

Então a ideia vai ser semelhante ao que nós fizemos com o Fuse.

04:27

Até para ficar um nome sugestivo, vou colocar assim, FinishTicketNode, porque em

04:35

inglês fica complicado colocar um...

04:40

FinishCustomerService, porque service já é um nome muito utilizado em programação.

04:44

Então, nós já temos o Ticket ID, nós vamos consultar,

04:51

mas eu vou precisar das informações que o atendente vai retornar através do output,

04:57

e aqui nós ganhamos o

05:01

NodeInput,

05:03

que vai ser do tipo AttendantOutput.

05:08

Isso aqui é muito...

05:10

importante porque não só eu recebo essa informação e

05:14

ela não vai ser apenas um dicionário,

05:16

ela vai ser um objeto. Aqui nós temos o uso mais

05:21

avançado do Python, que vamos dizer assim,

05:25

que se o agente produzir um resultado e não for desse tipo aqui,

05:31

o nó vai fazer com que seja validado o dado.

05:36

Então, se o dado chegar inválido, vai lançar um erro e a gente nem faz nada. Então,

05:40

nós temos total confiança que o NodeInput é o objeto desse tipo,

05:44

nós conseguimos pegar todas as informações.

05:46

Então, nós podemos pegar o NodeInput.Message, colocar

05:54

aqui no TicketMessage, e no caso do status, lembrando que nós temos um erro,

06:00

vai ser o TicketResolved se o status for sucesso.

06:06

Caso contrário, acho que tem um Failed.

06:09

Nós poderíamos colocar. Enfim, é que se tivesse falha, teria resposta.

06:13

Nós poderíamos ter um outro processo que permitisse continuar nesse ticket,

06:19

mas nós não estamos fazendo isso.

06:21

Ou de um erro também poderia desencadear alguma coisa.

06:24

Nós poderíamos muito bem fazer um se o

06:28

status é igual a erro.

06:33

Aí a gente poderia fazer alguma coisa. Poderia fazer...

06:39

Algum tratamento de erro aqui, enfim, só

06:46

para que nós possamos lembrar disso.

06:48

Então ele vai lá,

06:50

atualiza o ticket e depois retorna a mensagem. Então agora, no TicketResolution,

06:56

como que nós vamos encaixar esse nó?

07:01

Aqui, essa tupla já está pronta, não temos mais nada para mexer.

07:07

A continuidade do grafo se dá em uma outra tupla.

07:11

Repetindo quem nós queremos manipular, que vai ser o agente de atendimento,

07:16

passando o nó. Pronto.

07:20

Então, veja que esse ponto liga com esse.

07:25

Nós não temos aqui um design para fazer a setinha.

07:29

Então, se eu quisesse fazer

07:31

uma continuidade também para o RefuseTicketNode,

07:36

declaramos mais uma vez o nó.

07:40

E colocamos o que nós quisermos. Aí,

07:44

se tiver o redirecionamento, vem o dicionário com as rotas.

07:50

Então, aqui não importa, na verdade, a ordem, por isso que tem esse start,

07:55

como nós já havíamos dito. Então, nós só temos isso aqui.

07:59

E como eu havia falado também, como esse

08:04

attendant é default, nós poderíamos até colocar isso

08:09

aqui, dessa forma.

08:12

Se o

08:14

triage

08:17

não fizer

08:19

nada, na verdade não tomar nenhuma decisão, ele poderia ir para uma rota default.

08:24

Então, nós poderíamos comentar aqui e comentar essa parte daqui.

08:33

Mas não tem necessidade. Então, não colocando default route,

08:37

ele vai aparecer que não tem default,

08:39

mas obviamente tem default,

08:40

porque de qualquer forma nós vamos ter alguma coisa acontecendo.

08:47

Ou se é refuse ou se vai para o atendimento. Então, ótimo. Temos tudo isso aqui

08:55

construído. Agora, vamos rodar todos os agentes,

09:00

porque nós precisamos criar o ticket. Vou

09:04

fazer aqui o decal word para a barra agents.

09:07

Ok, nós conseguimos.

09:10

Então, vamos até antes disso, na verdade, vamos puxar um

09:19

novo nó, que

09:21

aqui vai ser o finish. Então,

09:33

agora, recepcionista. Como eu quero testar a questão do operador da conta, vou

09:40

colocar o C -201.

09:45

Então, quero

09:47

criar um ticket para adicionar o fulano,

09:52

o arroba -test.com, na minha conta. Ele

10:01

vai lá no classifier. Pronto,

10:06

então temos o ticket ID. Agora, selecionamos o resolution.

10:11

Nós só temos que passar um state a partir da identificação do ticket ID.

10:16

O restante do state vai ser adicionado pelo

10:23

próprio nó de triagem. Então, aqui não temos mais nada para dizer,

10:29

como diria a música.

10:31

Vamos ver o que vai acontecer. Agora, olha só que legal todo o nosso grafo.

10:39

Tem lá o noDefault.

10:41

A execução não conseguiu ser concluída com sucesso e nós vamos falar

10:45

exatamente da mesma questão quando nós fizemos o teste do Ticket Receptionist.

10:51

E vai ser o mesmo problema aqui, mas vamos analisar o que foi feito.

10:56

Então, o state foi gerado, roteamento para o atendente, o

11:03

subagente foi executado com a sua devida tool Edge Team Member.

11:10

Depois teve esse set model.

11:12

Response associado aqui ao account operator,

11:18

teve a resposta dele e aí vem de novo para o atendente e teve o problema.

11:25

Nós já entendemos que todo agente que é adicionado aqui

11:32

em ads, no nosso grafo,

11:34

ele vai se transformar num single churn. Por

11:41

padrão não fizemos nenhuma modificação, ele é chat, mas ele vai virar single churn.

11:46

Então tem aquela situação que ele tem que reconstruir

11:50

pegando do último evento qual foi o evento diferente,

11:55

qual foi o evento anterior diferente da autoria dele.

11:59

Qual foi o, fora os eventos,

12:02

o evento que eu emiti, qual foi o último evento que é diferente da minha autoria.

12:08

Então ele quebra daquela mesma forma. Então...

12:16

a LLM não tem condição de saber que esse function call,

12:21

que foi exatamente esse que aconteceu aqui,

12:23

corresponde ao function response.

12:27

Então, aqui

12:30

nós temos uma restrição,

12:32

quando nós estamos trabalhando com workflows, então veja que,

12:36

num cenário que eu não rodasse com workflows,

12:40

não teria problema nenhum estar com esse subagente adicionado.

12:48

ele iria se comportar, nós até testamos isso.

12:51

Mas quando ele está no workflow, ele

12:56

vai se tornar esse single churn,

12:58

e um single churn no momento não suporta subagents também.

13:05

Não é bom que você coloque.

13:08

Então, como que nós vamos solucionar essa questão?

13:14

Lembra do que nós já fizemos, acho que tem algum exemplo aqui de agent tool?

13:25

Nós já tínhamos falado, eu não lembro exatamente se a gente tinha feito...

13:29

Algo desse tipo. Então, nós vamos deixar esse subagente de lado e

13:36

declarar um agent tool

13:41

passando o nosso subagente.

13:47

Então, ele já

13:58

está pedindo aqui para fazer o import.

14:00

Na verdade, o import está totalmente errado.

14:04

Não é exatamente isso.

14:07

Ele vem aqui das tools, ele pode até colocar aqui em cima.

14:12

Então a diferença agora é que ele sendo de fato,

14:15

tendo essa execução da tool, ele é totalmente isolado,

14:19

nós não vamos ter toda aquela visibilidade,

14:22

o que não é um problema para o nosso caso.

14:25

Então quando tiver essa situação, quando eu tenho uma

14:32

agente que não vai ter nenhuma interatividade,

14:34

ele vai executar diretamente, ele vai virar esse single churn.

14:40

Não declare subagents,

14:42

mas aí aqui eu chamo atenção sobre a construção do ADK e de outros frameworks,

14:50

que pode ser que numa outra versão posterior isso

14:55

tenha sido mudado, esse suporte tenha sido adicionado.

15:01

Mas a questão também é que nós poderíamos

15:04

mudar esse agente de atendimento para chat,

15:08

mas aí ele poderia...

15:11

Chamar o usuário, né? Chama o usuário para falar alguma coisa, o

15:16

que nós não queremos. Então, eu poderia mudar para chat,

15:20

eu não vou fazer isso, mas fazer isso nesse fluxo, eu

15:25

tenho que deixar uma instrução nele para não chamar o usuário em hipótese nenhuma.

15:29

Uma restrição, não chama o usuário.

15:32

Execute diretamente, mas enfim.

15:34

Então, fizemos essa mudança, agora vamos rodar novamente.

15:49

Agora aqui o problema que eu não tenho,

15:51

na verdade a gente tem o ticket, como não aconteceu nada,

15:56

nós podemos rodar

16:00

facilmente sem ter que criar um novo. Então, o ticket ID é igual ao ticket.

16:07

Então, bora fazer o nosso novo teste. E

16:19

aqui na verdade eu tenho que mudar, ele deu restrição no account operator,

16:25

que nós vamos tirar aqui

16:29

o single churn.

16:32

Agora ele já está rodando como uma tool. Então, vamos rodar novamente.

16:42

Então, ticket ID.

16:56

Agora nós não vamos ver mais a execução da tool dentro do account operator.

17:02

Pronto. Então, temos

17:07

o atendente em todo esse fluxo. Ele vai colocar aqui como resolved.

17:14

Na verdade, isso aqui é o account atendente.

17:17

Eu tinha colocado exatamente isso no output.

17:22

Ou ele desobedeceu o que eu coloquei.

17:29

É bom que a gente coloque informações sobre o status,

17:34

está vendo como ele desobedeceu,

17:37

sucesso ou erro, mas ele colocou, não

17:47

totalmente errado, mas verifiquei com a sua solicitação,

17:50

após realizarmos a verificação do nosso sistema,

17:53

constatamos que o usuário já está cadastrado como membro.

17:57

Ah, já tinha adicionado por causa que...

18:03

Então, esse resultado não está meio que errado, porque como a execução do MCP está

18:09

ainda em memória, a gente teria que fazer aqui o reset dela,

18:12

só para rodar novamente.

18:19

Mas aqui está a nossa resolução final.

18:23

Então, vamos fazer novamente um teste?

18:27

Então, eu vou criar aqui com

18:37

esse mesmo trecho, porque fica fácil. Ele

18:48

vai registrar o ticket, vai na resolução.

18:57

Passamos o ticket change.

19:00

Pronto. Então, vamos lá.

19:10

Ele considerou meio que um resolved, que é um meio termo entre o erro e o sucesso.

19:15

Está vendo agora como que... Então,

19:18

a gente dá margem para a interpretação.

19:20

A gente tem a opção que nós conseguimos passar no agente,

19:25

informando para a LLM qual é a temperatura do modelo.

19:29

A gente pode colocar a temperatura totalmente zerada para o modelo...

19:33

Não ficar fazendo essas invenções ou dar uma instrução também

19:36

para ele não sair do que nós colocamos.

19:39

Então, ele

19:41

rodou todo o fluxo e agora nós temos aqui o que foi feito.

19:46

Então, começou no start, foi na triagem, foi no atendente,

19:51

aí vai para o account operator, que

19:57

é uma tool agora,

19:59

e foi para o end, na verdade foi para o finish ticket node. e foi para o engine.

20:04

Então agora vai ficando mais claro como que é o comportamento desse grafo.

20:09

A tendência é que o grafo vai ficando cada vez mais complexo,

20:13

e ainda como eu tinha falado,

20:15

nós conseguimos até reroutear para um

20:21

nó anterior

20:24

e fazer todo o processo novamente, enfim,

20:26

nós temos toda a liberdade aqui e usando LLM no meio dessa história toda.

## Resumo IA

[RESUMO_IA]