Módulo: Desenvolvimento de Agentes com IA\
Aula: [Criando agente de atendimento com MCP](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18570)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos construir um agente de atendimento geral,

00:04

que vai ser o outro caminho,

00:07

o caminho padrão do nosso grafo.

00:12

Eu vou chamá-lo de atendente.

00:17

Ele vai fazer esse atendimento geral, exceto o estorno. Então,

00:21

se é dúvida, verificar se a plataforma da Acme está funcionando,

00:26

quaisquer outras questões que não são estorno, ele vai conseguir fazer.

00:30

Até mesmo, nós vamos trabalhar aqui com...

00:33

um operador da conta, parecido com o que nós já tínhamos feito anteriormente.

00:40

Ele vai ser um subagente desse atendimento. Então,

00:42

se ele ver que o usuário quer adicionar um membro ou algo assim,

00:49

então tem o agente operador da conta.

00:52

É muito bom fazer essa separação, até mesmo para o atendente conhecer tudo.

00:58

Se tiver que fazer alguma coisa específica, ele pode...

01:03

mandar para outro subagente. Ele pode ter ali uma leva de subagentes.

01:09

Eu já trouxe esses dois agentes criados e nós temos algumas coisas novas,

01:14

mas toda a base que nós já aprendemos durante a disciplina.

01:17

Então, nós vamos nos concentrar em entender como esses agentes funcionam e ver

01:22

essas questões novas e depois nós vamos fazer a integração com o grafo.

01:28

Eu preciso mostrar duas configurações novas porque nós vamos ter agora...

01:33

um servidor MCP. Essas duas variáveis estão adicionadas no env.example,

01:38

você precisa colocar no seu .env. Então, temos o attendant e o account operator.

01:45

O account operator é um subagente do attendant.

01:48

Vamos rodar primeiro o account operator, que ele está conectado com o servidor MCP,

01:53

e nós conseguimos rodar ele diretamente.

01:58

Com aquela estratégia que eu tinha mostrado,

02:00

eu criei ali a pasta account-operator-dev e o arquivo agent.py. Então,

02:06

vamos fazer aqui o

02:08

adk-web account-operator mais

02:14

account-operator-dev. Pronto.

02:21

Então, vou

02:24

recarregar. Então, está aqui account-operator-dev.

02:29

Mas antes disso, nós precisamos entender o que esse agente precisa para trabalhar.

02:34

Vamos chegar aqui nele.

02:37

Ele tem o seu nome, account operator,

02:41

especialista em ações de conta da Acme. É um single churn,

02:47

então no operator DAG, nós mudamos para chat,

02:51

senão nós não vamos conseguir brincar com ele. Tem o modelo, o system prompt,

02:58

aqui a configuração do MCP que nós vamos ver daqui a pouco.

03:01

E ele é obrigado a retornar um output.

03:06

Temos um formato, porque às vezes ele pode não executar de forma correta.

03:10

Então, esse output padronizado, essa saída estruturada, como nós já falamos,

03:16

vai ajudar o atendente a formatar a mensagem, entender o que aconteceu. Então,

03:22

nós vamos ter o status da operação. Ah, ele adicionou,

03:26

o membro já foi adicionado, e e-mail inválido ou erro.

03:31

Se a gente até quisesse colocar uma action ou algo assim, poderia...

03:36

colocar essas operações e aí o status virar um sucesso ou erro.

03:41

Podemos trabalhar de várias formas. E a mensagem do que ele fez?

03:45

Se ele não conseguiu fazer a operação ou a confirmação do que ele fez.

03:52

E aí ele vai fazer essa operação na conta.

03:58

Mas ele precisa de duas informações, do ticket message e do customer ID.

04:05

Então veja que nesse caso estamos utilizando o state,

04:08

porque quando a gente olha para o nosso grafo, qual

04:14

é a entrada de dados?

04:16

Ele vai ser acionado e

04:20

nós vamos puxar as informações do ticket.

04:22

Poderíamos passar o ticket message como user content,

04:26

como se o usuário estivesse passando a mensagem, sim, sem problemas nenhum.

04:31

Mas já que nós estamos no state, isso está gravado no banco de dados, passamos a...

04:37

Eles interpolados no meio do System Prompt. Então,

04:41

ele vai fazer as ações da conta e tem o retorno apenas especificando, a

04:48

gente pode até simplificar aqui apenas o status, não precisa colocar de forma...

04:54

Tem gente que até gosta de repetir isso aqui,

04:58

mas a gente acaba economizando tokens e a mensagem de confirmação.

05:02

Vou colocar só message, que vai ser melhor.

05:07

E aí eu coloquei algumas restrições, isso aqui vai fazer sentido depois,

05:11

porque na hora que a gente está usando um servidor MCP, pode

05:19

ser que ele não identifique as tools e aí

05:21

ele tente executar e entenda que ele executou com sucesso.

05:26

Na verdade, se ele não se comunicou com a tool do MCP, então ele não fez nada.

05:30

Então eu falei que você só pode declarar que você teve

05:35

algum resultado após receber a resposta de uma tool.

05:38

Se a tunnel estiver disponível na lista de ferramentas ou for chamada a falhar,

05:43

retorne o status de erro.

05:47

Se você tiver um modelo melhor, isso aqui tende a não acontecer,

05:51

mas é algo que eu já vi acontecer bastante

05:55

e é uma restrição para que você evite este problema.

05:59

Então nós vamos precisar dessas duas informações.

06:02

Mas antes disso, vamos pegar aqui as duas partes do MCP.

06:09

Então nós temos o servidor MCP, que

06:15

inclusive tem esses erros aqui de tipagem que eu

06:20

não importo por causa de pegar as coisas do Envy.

06:23

Nós estamos utilizando o pacote MCP, que você pode instalar com uv

06:31

-add -mcp. É o pacote oficial do Python para

06:38

que você possa criar os seus servidores MCPs ou fazer qualquer coisa.

06:42

Usamos esse Fast MCP para

06:45

criar a instância do servidor, passando algumas opções.

06:50

Aqui tem o dicionário dos Customer IDs e dos membros.

06:55

Eu não vou trabalhar com banco de dados para não ser algo mais complexo,

06:58

porque senão a gente adiciona muitas camadas aqui no nosso software. Então,

07:03

com o MCP na mão, nós queremos usar tudo o MCP com o decorator.

07:10

Então, tem a listagem dos membros, passa o Customer ID e ele vai fazer a listagem.

07:16

Adicionar um membro, passa o Customer ID e o e-mail.

07:20

Então, lembrando de uma tool, temos DocString,

07:24

temos as tipagens, tudo isso vai ser relevante,

07:28

tudo isso vai ser passado lá para o modelo.

07:32

E aqui no final, se eu chamar esse arquivo diretamente como main,

07:36

ele vai rodar o servidor MCP como um streamable HTTP. A gente pode ter

07:44

STDIO, Server Center Events. Então, aqui seria uma

07:50

das formas mais utilizadas hoje para que você disponibilizasse esse servidor MCP na frente da sua API.

07:58

Você poderia fazer com que esse servidor MCP, como é um outro software,

08:02

se comunicasse com um banco de dados, mas normalmente se faz expondo... essas tools,

08:08

e você não vai ter regra de negócio nenhuma aqui,

08:11

sendo que você já tem uma API que já atende

08:14

aos clientes e também vai atender agora ao agente de IA.

08:21

Então, nós vamos rodar esse servidor MCP,

08:25

nós podemos executá-lo com o Python,

08:30

outside, tudo que é externo, como a gente está fazendo essa questão do externo,

08:35

vai ficar em outside, account MCP server.

08:45

Ele está chiando comigo por conta que o

08:51

argumento precisa ser, vamos

08:58

colocar um loadenv, que

09:02

é o que eu tinha esquecido,

09:08

load .env. Pronto.

09:14

Então, você pode até pegar esse endereço,

09:17

que ele roda na porta 8.7.65, e

09:22

colocar aí no seu agente de IA, no Cloud Code, Copilot, OpenCode.

09:27

Qualquer lugar você vai conseguir brincar com essas tools diretamente também,

09:31

é algo bem interessante. Então, tem o meu servidor rodando,

09:35

obviamente tem o client, que é o que vai plugar ali no agente.

09:40

Então, nós especificamos a URL,

09:44

e aí com essa função, createAccountToolSet, porque nós vamos ter todas as tools,

09:49

quantas tools que nós temos?

09:52

Temos uma, duas, são duas tools.

09:57

todas as tools vão ser

10:00

adicionadas no MCP Toolset,

10:05

que é uma instância do próprio ADK,

10:08

para que você integre coisas de MCP com seus agentes.

10:12

Então, iniciamos ela passando qual é a forma que a gente vai se conectar,

10:17

que é usando o Streamable Server HTTP com o mesmo endereço.

10:21

A ideia é justamente essa. Então, ao olhar isso aqui no nosso operador,

10:28

a gente vai ver aqui embaixo, que é o Create Account Toolset.

10:33

A questão é que ele precisa se comunicar com o

10:40

servidor MCP para ele expor as tools,

10:42

justamente por conta dessa instrução aqui que eu adicionei para evitar problemas.

10:47

Se ele não consegue criar e

10:52

se comunicar com o servidor MCP, ele não consegue expor as tools,

10:55

ou a gente pode, mais o LLM trabalhando como comparsas, eles...

11:01

Inventam coisas. Então nós precisamos aqui do TicketMessage e do CustomerID.

11:05

Nós já sabemos fazer isso, então vamos colocar aqui no state

11:14

TicketMessage.

11:20

Quero adicionar o fulano arroba

11:26

test.com como

11:29

membro.

11:34

E aí vem o CustomerID, que é essencial ali. Ele é o C201.

11:42

Pronto, vou até copiar isso aqui para a gente quiser usar depois.

11:46

Então aqui a interface não vai deixar que eu dê um enter nada na base,

11:49

eu vou colocar apenas uma letra A, não vai fazer diferença nenhuma. Então veja só,

11:56

ele tem aqui o add team member, então nós já conseguimos ver

12:03

aqui nas chamadas que em termos das tools,

12:07

Temos o set model response que ele vai utilizar.

12:11

Porque nós estamos trabalhando com o chat, é o List Members.

12:14

Com a descrição docstring e o add TeamMember.

12:21

Então ele foi lá, fez a chamada com esses dois parâmetros,

12:25

Então deu tudo certo e depois teve a resposta.

12:28

O membro Fulana -robotet.com foi adicionado com sucesso.

12:33

Então aqui nós já conseguimos ter um

12:40

vislumbre de como as coisas funcionam, tudo padronizado e etc.

12:44

Vamos testar o outro agente? Então nós vamos chamar...

12:52

Tendente mais atendente dev. Agora vamos para o ADK Web.

12:59

Então, vou

13:01

colocar o mesmo state novamente que nós tínhamos usado antes para

13:07

que a gente possa avaliar se ele redireciona para o subagente. Mas vamos ver como

13:14

está o nosso agente de atendimento geral.

13:22

Então, ele tem esse atendimento geral, resolve dúvidas, problemas.

13:28

E verifica o status

13:31

da plataforma. Na

13:35

verdade, dá para colocar, a vírgula estava certa aqui, eu achei que estava errada.

13:39

É porque ele resolve dúvidas,

13:42

verifica o status da plataforma

13:45

e realiza operações de

13:54

conta. A

13:58

diferença em relação ao operador da conta é que ele consegue verificar o status,

14:03

ele tem essa tool aqui que faz uma...

14:06

chamada fakeHttp.

14:09

Então, dentro desse outside,

14:11

eu criei no modo Python de se fazer, nós vamos ter

14:18

esse método que vai simular como se nós estivéssemos fazendo uma chamada.

14:26

Então, ele

14:28

cria aqui um mock para, no final das contas, demonstrar quais os serviços,

14:33

os seus status e os incidentes em aberto. Então, temos...

14:39

Todos os serviços, se está operacional, degradado e os incidentes.

14:43

Assim seria um tipo de um uptime.

14:46

Eu não quis criar aqui nada HTTP porque a gente não tem que subir mais um serviço.

14:52

Então, dentro da pasta tools, aqui dentro do ticket resolution,

14:57

vamos ter a tool que chama esse get status. Então, eu só

15:02

circulei ele com a tool em si, com o docstring que vai...

15:08

ser essencial para que ele saiba que ele tem que fazer a chamada para cá,

15:12

mas aqui seria a mesma coisa de fazer um HTTP e pegar a informação.

15:17

O que vai acontecer é que ele faz a chamada

15:21

simulando esse HTTP e retorna esse JSON que está aqui.

15:27

Então, ele pode fazer essa chamada, tem o subagente que é o operador da conta,

15:31

também ele vai ter o seu formato de saída.

15:35

É importante que a gente trabalhe nesse workflow.

15:39

Isso vai nos ajudar a manipular as informações. Então, temos o status,

15:43

se é sucesso ou erro, dependendo do que ele fez,

15:47

e a mensagem para o cliente. Então,

15:49

vamos pensar no caso do operador da conta que fez

15:51

alguma coisa e retornou o status dele com o message.

15:57

Obviamente, vai ser convertido para sucesso se ele fez totalmente o que foi pedido.

16:04

E a mensagem ainda que pode ser ajustada.

16:11

Nós temos... Podemos colocar instruções,

16:14

Na verdade, eu acho que eu nem coloquei a instrução de ser cordial.

16:17

Não, tem aqui embaixo.

16:18

Ser cordial é educado, então ele pode fazer uma formatação.

16:22

A ideia é que ele seja esse atendimento central,

16:25

que vai ficar na linha de frente para bug, dúvida, onboarding,

16:29

configuração. Então, ele recebe o ticket message também e... O justification,

16:36

nós temos que adicionar mais esse cara na hora de fazer a nossa chamada aqui.

16:45

Então, seria algo do tipo,

16:47

O usuário quer adicionar um membro à sua conta.

16:58

Então, ele tem a ação da conta, que eu coloquei aqui apenas para exemplificar,

17:02

deixar mais claro, mas obviamente a gente sabe que o modelo iria tender,

17:07

a fazer uma operação desse tipo, mas como nós temos esse atendimento geral,

17:10

é mais um reforço para ele não se confundir e para ele

17:13

chamar o subagente de operação de conta quando é para adicionar o fulano,

17:19

a equipe ou coisas assim. Caso contrário, atendimento geral.

17:24

Se o usuário não pede nenhuma ação de conta,

17:27

use o restante do conhecimento para resolver o problema.

17:30

Aqui nós não adicionamos nenhum acesso ao banco de dados, poderíamos ter uma ferramenta.

17:36

Que leria markdowns, acessaria banco de dados,

17:40

poderíamos trabalhar com N situações dependendo do volume dessas informações.

17:46

Então, aqui, como é até mais simples, nem coloquei no formato JSON,

17:51

só falei que vai ser o JSON com os tais campos.

17:54

E a mensagem, essa mensagem, deve ser cordial e educada.

18:00

Deve dar detalhes do que foi feito, porque é importante essa mensagem...

18:05

Ela vai acabar sendo gravada ali no response do

18:08

ticket e o usuário leria isso depois.

18:11

Então, essa é a tônica desse agente.

18:13

Ele pode redirecionar como pode fazer a sua própria resposta.

18:18

Então, nós adicionamos tudo que é necessário desse

18:22

state. Ao fazer isso, vamos enviar alguma coisa.

18:30

Então, já veja que ele fez o redirecionamento lá

18:32

para o subagente e ele vai ter que adicionar via... Tudo MCP.

18:42

E o que aconteceu aqui de errado?

18:44

Faltou uma informação, que é o Customer ID, que nós não tínhamos adicionado.

18:50

Então, o Customer ID está certo, porque

18:54

a ferramenta necessária não está disponível. Ah, não, eu achei que era outra

19:00

coisa. Na verdade, acho que eu tinha desligado aquilo.

19:05

Python, mas... Bom

19:09

que a gente viu que o agente retorna um erro, né? Então, como...

19:15

Deixa eu só copiar isso aqui de novo para

19:19

ficar mais fácil. Criamos uma nova seção e vamos lá.

19:31

Então, operador da conta, agora sim ele vai adicionar.

19:39

Então, tivemos o

19:43

Add Team Member, foi chamado.

19:46

Ele até não está mostrando exatamente ao longo dos eventos, porque

19:52

ele chamou ali o MCP, mas

19:56

ele foi identificado como um componente. Então, foi adicionado à conta.

20:02

E temos aqui o resultado. Então, esse aqui é o resultado do account, mas

20:08

Aí, ele coloca a mensagem final.

20:11

Gostaria de informar que a sua solicitação foi processada com sucesso.

20:14

O membro já foi adicionado à sua equipe.

20:17

Se precisar de mais alguma coisa ou tiver outras dúvidas,

20:19

estamos à disposição para ajudar. Então, vamos criar uma nova sessão.

20:25

Então, agora, com tudo que eu vou passar aqui, a

20:31

ideia... Na verdade, é que ele não redireciona. Vamos

20:38

passar aqui. Eu quero

20:40

informar um bug

20:45

na integração com GitHub.

20:50

Erro 500.

20:53

O usuário quer

20:56

informar um problema que está acontecendo.

21:02

Um erro 500 na comunicação.

21:09

com a API REST. Pronto.

21:16

Vamos ver como ele vai se comportar agora.

21:19

Aí, olha só, ele chamou a nossa tool.

21:25

Pronto, então, agradecemos por entrar em contato para nos reportar esse problema.

21:30

Para ajudar de uma melhor forma,

21:31

fiz a verificação no status atual do serviço. No momento,

21:35

nossa API de integração está operando normalmente, sem nenhum incidente global.

21:42

Temos nada relacionado ali especificamente com GitHub.

21:47

Obviamente, aqui também poderíamos dar mais contexto,

21:50

colocar informações diante de todo o cenário que nós temos ali da Acme,

21:56

de todos os serviços,

21:57

como eles funcionam e algo do tipo.

22:00

Senão, nós vamos ficar só detalhando essas questões com o agente.

22:05

Mas nós já temos agora um agente, então...

22:11

mais interessante para trabalhar aqui no nosso workflow.

22:14

Nós não adicionamos ele ainda. Ele atende, tem operador da conta,

22:18

verifica o status, então ele tem esse atendimento geral. Na próxima aula,

22:23

nós vamos integrá-lo com o nosso Ticket Resolution.

## Resumo IA

[RESUMO_IA]