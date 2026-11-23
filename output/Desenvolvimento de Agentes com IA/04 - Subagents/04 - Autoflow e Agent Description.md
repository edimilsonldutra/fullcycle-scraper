Módulo: Desenvolvimento de Agentes com IA\
Aula: [Autoflow e Agent Description](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18259)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre a descrição dos subagentes e o autoflow,

00:07

que nós definimos no finalzinho da última aula,

00:09

mas nós vimos o comportamento durante toda a última aula.

00:13

Nós vimos que uma vez definido um agente coordenador com seus subagentes,

00:19

o próprio ADK com seu System Prompt faz

00:23

com que o roteamento aconteça de forma natural,

00:26

sem que a gente... tenha que ficar demandando como que vai ser,

00:31

apesar de que nós conseguimos fazer isso também.

00:33

Então, para que esse roteamento aconteça,

00:36

nessa primeira chamada que acontece para a LVM,

00:39

ou em toda chamada, vai ser passada a lista dos outros agentes,

00:43

que ele nem vai colocar como subagente, nós vimos isso.

00:46

Ele coloca o agent name e a descrição desse agente.

00:50

Nós trabalhamos de uma forma arriscada, porque não definimos... A descrição dele.

00:56

A descrição é ainda mais importante do que o agent name,

00:59

porque ela vai ser uma frase que vai bater com o que o usuário está pedindo.

01:07

E isso vai ser de extrema relevância para a

01:10

LLM decidir para quem ela vai transferir.

01:13

Ela conseguiu transferir para o consultor de faturas porque eu tenho um

01:20

consultor de faturas batendo com o list minhas faturas.

01:25

Mas imaginando num cenário... eu

01:29

poderia ter um agente de faturas,

01:32

mas um agente de assinaturas que poderia lidar com faturas também.

01:39

Então, como eu não tenho uma descrição, claro, pode ser uma descrição ambígua,

01:44

ou não tenho descrição, ou a descrição está muito ruim,

01:49

pode fazer com que a LLM decida rotear para um

01:52

agente que não devia e causar um estrago,

01:55

ou não atender o usuário, ficar confuso. Então,

01:59

nós temos que fazer a definição da descrição. Isso,

02:03

apesar de não constar com um parâmetro obrigatório,

02:07

isso vai ser essencial para a qualidade do nosso projeto.

02:11

Então, voltando aqui para o código, vamos

02:15

definir essa descrição, colocando debaixo do name.

02:23

E o que colocar aqui? Nós temos que tomar cuidado.

02:27

Description não é System Prompt, diferente de System Prompt.

02:33

Porque no System Prompt nós vamos definir a persona, vamos definir quem ele é,

02:39

o passo a passo, o que ele tem que fazer.

02:41

Na descrição nós não vamos definir isso.

02:44

A descrição tem a ver mais com as capacidades,

02:47

tem a ver com o casamento de

02:52

de acordo com o que o usuário está pedindo.

02:54

Então não é recomendado que a gente coloque você,

02:59

um consultor de faturas da Acme, não precisa colocar.

03:04

Nada disso. Não preciso ficar listando tools.

03:09

É uma descrição que não deve passar de uma linha.

03:14

Então nós podemos colocar assim, especialista em

03:21

faturas.

03:24

Não preciso colocar da Acme.

03:27

Responsável por listar as faturas de um cliente específico. Isso aqui está bom.

03:31

A LLM até que foi bem.

03:35

Eu poderia colocar algo também como especialista em gerenciar faturas,

03:39

mas como nós temos apenas o

03:43

listar faturas como tool, quanto mais preciso, isso aqui vai casar o tempo inteiro.

03:49

Mas se isso começar a aumentar o consultor de faturas,

03:52

ele vai analisar, vai fazer outras coisas,

03:54

aí eu posso colocar um gerenciamento de faturas.

03:58

Então, isso aqui é uma boa descrição.

04:02

Vamos acrescentar aqui também.

04:05

Especialista em assinaturas,

04:07

responsável por informar o cliente sobre a sua assinatura.

04:11

Aí eu não preciso colocar esses detalhes aqui. Eles não vão ser relevantes.

04:16

Tem mais em como casar com o que o usuário

04:18

está mandando para ativar a delegação para esse agente.

04:24

Imagina se eu coloco aqui, seja cordial e direto.

04:27

Isso é o passo a passo, o que ele é. Tem a ver com as capacidades.

04:32

Mas um erro muito comum é não definir também

04:37

a descrição do coordenador. Por quê? O controle pode voltar para ele.

04:45

Então, nós

04:47

podemos colocar coordenador

04:51

responsável por intermediar a comunicação, ou

04:56

melhor, responsável por intermediar a comunicação. Isso aqui já é meio que

05:00

implícito. Responsável por

05:05

ajudar o

05:10

cliente a gerenciar a conta, incluindo faturas e assinaturas.

05:20

Isso aqui está dizendo que ele ajuda a gerenciar.

05:23

Ele não faz exatamente algo específico. Poderia se criar outras frases também,

05:29

mas a ideia é justamente não passar do ponto aqui de

05:32

falar que ele vai fazer alguma coisa ou deixar

05:37

uma descrição que às vezes, numa execução de um subagente, volte para ele,

05:41

porque aqui não tem nenhum motivo para voltar para ele.

05:43

Ele vai passar a bola para o de assinaturas ou de faturas e eles vão continuar.

05:50

Então vamos fazer um teste diante disso aqui no

05:58

ADK Web novamente.

06:02

Então, liste minhas faturas. Então

06:10

agora selecionando esse carinha daqui, nós

06:15

vamos ver que a descrição está lá.

06:18

Obviamente nós estamos colocando aqui tudo em português,

06:21

mas poderia ser tudo em inglês até mesmo para ser mais efetivo.

06:34

Então vemos aqui que ele está no consultor de faturas.

06:39

Agora, criando uma nova sessão, quero cancelar minha assinatura.

06:47

Ele já transferiu para o consultor de assinaturas.

06:53

E aqui já é um problema,

06:54

porque ele está pedindo o número do cliente ou e-mail cadastrado.

06:58

E nós tínhamos feito uma mudança de pedir o

07:05

ID do cliente dentro

07:08

do subagente de faturas. Então, deveria estar aqui também.

07:13

A gente já viu ali que abre... brecha para a interpretação.

07:20

E obviamente abre brecha para a interpretação dado o modelo que nós temos.

07:28

Você pode usar outro modelo e ele já inferir por conta da documentação da tool,

07:34

porque ele vai acabar vendo que tem ali o ID do cliente.

07:40

Tem a documentação, ele já poderia não falar ali de e-mail.

07:44

Então, quero cancelar minha assinatura.

07:53

Pronto. Então, agora sim ele pediu correto.

07:56

Ele está pedindo a ID do cliente e a senha de autenticação.

08:01

Aquilo que nós tínhamos criado. Então, senha secreta.

08:08

Vai pedir a confirmação.

08:13

Pronto. Então, aqui nós temos esse subagente,

08:16

mas agora vamos fazer um outro experimento. Porque,

08:21

e se eu falar que eu quero listar as minhas faturas? Veja só.

08:26

Vou listar as minhas faturas.

08:36

Vê que ele faz o transfer para o consultor de faturas.

08:43

Isso aqui é interessante,

08:44

porque marcando e verificando a request, veja

08:51

que eu sou o consultor de assinaturas. Então,

08:56

ele passa o operador da conta e

09:01

passa o consultor de faturas entre os dois.

09:03

Um é o coordenador responsável por ajudar o cliente a gerenciar sua conta,

09:07

incluindo faturas e assinaturas. E dado também o histórico que já foi feito,

09:11

porque nós vamos ter dentro de Contents muitas mensagens,

09:16

começa desde lá do quero cancelar,

09:19

mas tudo isso é passado para a LLM. Se a gente for olhar em Tracing, quando

09:26

faz aqui a chamada, tudo está sendo juntado.

09:36

Então ele passa... O operador da conta é o consultor de faturas,

09:40

então ele decidiu, olha,

09:42

faz aí o transfer to agent já para o consultor de faturas.

09:46

Não precisaria acionar o operador da conta.

09:50

Nós conseguimos fazer um controle mais

09:54

específico de obrigar os subagentes a

10:00

não transferirem para os seus irmãos.

10:04

Ou até podemos proibir dele transferir para o coordenador.

10:08

Existem essas configurações.

10:10

Mas da forma que está aqui, o AutoFlow vai tomar a decisão mais eficiente.

10:16

Porque passando o System Prompt da forma que foi, a

10:22

tendência, como não é determinístico, nós não sabemos,

10:26

mas a tendência é que ele dê preferência para esse cara,

10:29

porque a gente falou que é especialista em faturas.

10:32

Isso aqui vai ter um peso tremendo.

10:36

Então, essa

10:39

definição que nós estamos aqui no momento...

10:41

É a definição mais básica recomendada

10:44

para que nós trabalhemos com os subagentes.

10:49

Uma descrição numa frase que demonstre as capacidades

10:54

e não o que tem que ser feito.

10:56

Ela não briga com o System Prompt.

11:01

Ela é usada apenas para delegação.

## Resumo IA

[RESUMO_IA]