Módulo: Protocolos de Comunicação\
Aula: [Python SDK (FastMCP) parte II](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18601)

## Resumo da aula

makePriorityShift modela uma ação operacional real: ativar envio prioritário apenas quando o pedido pertence a cliente Prime e o atraso ultrapassa um dia. O ponto central não é a consulta ao PostgreSQL, já conhecida do cenário anterior, mas o contrato de saída da tool: em vez de retornar texto solto, a operação devolve uma estrutura com success, error e message. Esse formato separa sucesso operacional, motivo de falha e mensagem legível, o que facilita consumo por hosts, agentes e fluxos automatizados. Em um agente, essa estrutura reduz ambiguidade porque a decisão seguinte pode depender de um campo explícito, não de interpretação de linguagem natural.

Retorno estruturado transforma a tool em uma API de decisão, não apenas em um comando remoto. Quando success=false, o agente consegue distinguir casos como “pedido não encontrado”, “cliente não é Prime” ou “pedido já tratado” sem inferir isso a partir de texto livre. Quando success=true, message continua útil para auditoria, logs e resposta ao usuário, mas a automação se ancora no campo booleano. Esse desenho é especialmente importante quando a mesma capability será usada em lote ou encadeada com outras ações.

Prompts no FastMCP não precisam ser uma única string; eles podem ser compostos como uma sequência tipada de mensagens. UserMessage representa a instrução principal que o host ou agente entregará ao modelo, enquanto AssistantMessage antecipa uma resposta ou enquadramento esperado, funcionando como guia semântico para a execução. Essa composição é útil quando se quer induzir um fluxo mais controlado, como triagem logística seguida de uso de tools específicas. O resultado é um prompt mais governado do que texto livre improvisado.

Um prompt parametrizado é um template cujo conteúdo depende de argumentos como pedido_id ou canal. Em vez de expor uma instrução genérica, o servidor publica uma intenção reutilizável que o host pode instanciar com valores concretos, por exemplo para diagnosticar um pedido específico ou gerar um comunicado via e-mail ou SMS. Isso aproxima prompt de contrato operacional: a intenção é fixa, mas os dados variam. Para agentes, esse modelo reduz variação desnecessária e melhora previsibilidade de execução.

Prompt estático serve para intenções recorrentes sem parâmetros, como uma triagem em lote de pedidos problemáticos. Prompt template existe quando a intenção permanece a mesma, mas precisa ser especializada por entrada, como um diagnóstico de um pedido ou uma mensagem para um canal específico. A diferença importa porque o catálogo MCP passa a explicitar o que é menu fixo e o que é operação configurável. Esse nível de semântica ajuda o agente a escolher a capability correta para cada contexto.

Retomando a distinção já estabelecida entre leitura e ação, o resource continua sendo a forma de expor leitura idempotente; a novidade aqui é o contraste entre URI fixa e template parametrizado. Um resource estático lista uma coleção previsível, como pedidos não finalizados, enquanto um resource template representa uma família de leituras, como “pedido por ID”. O template não é apenas conveniência sintática: ele define explicitamente quais partes da leitura o cliente pode variar. Isso transforma a URI em contrato navegável para host e agente.

O Inspector continua sendo a forma mais direta de validar o catálogo exposto, mas aqui ele ganha um papel semântico: confirmar não só que a capability existe, e sim se ela foi classificada corretamente como tool, prompt, resource ou template. Ao inspecionar prompts, é possível verificar a lista de mensagens geradas e os argumentos exigidos. Ao inspecionar resources, fica visível a diferença entre leitura fixa e leitura parametrizada. Essa checagem evita integrar um agente com capacidades mal modeladas.

Quando um agente consome um servidor MCP, ele não precisa conhecer a implementação interna em Python nem a lógica do banco; ele enxerga um catálogo de capacidades executáveis. Na integração com frameworks de agentes, esse catálogo costuma ser adaptado para o modelo de function calling, no qual o LLM recebe uma lista de funções disponíveis e escolhe quais chamar. Nesse arranjo, o MCP vira a camada de execução confiável por trás das chamadas do agente. O valor arquitetural está em separar decisão semântica do agente e execução operacional do servidor.

No LangChain, as capacidades do servidor são adaptadas para a superfície que o agente entende como tools. Isso não significa que prompts e resources deixam de existir semanticamente no servidor; significa apenas que, no lado do agente, a integração os projeta para o modelo de chamada de função do framework. O efeito prático é que o agente pode descobrir capabilities MCP, invocá-las e encadear resultados sem reimplementar a lógica de negócio. O servidor continua sendo a fonte de verdade do contrato operacional.

A execução em lote aparece quando o agente lê um conjunto de pedidos, identifica casos relevantes e dispara múltiplas operações sequenciais ou paralelas, como reembolso, envio expresso ou cálculo de CEP. Esse padrão depende de retorno estruturado e de capacidades bem delimitadas, porque o agente precisa decidir o próximo passo com base em resultados confiáveis. O lote também evidencia por que prompts, resources e tools não são redundantes: o agente lê via resources, recebe orientação via prompts e age via tools. A composição das três primitivas forma um backend operacional completo.

O agente só consegue raciocinar sobre os dados que o servidor realmente expõe. Se o resource retorna status e previsão de entrega, mas não inclui CEP ou endereço, o agente não pode inventar essa informação; no máximo, pode pedir outro recurso ou solicitar dados adicionais. Esse limite é um princípio de projeto de contrato: expor menos reduz risco e acoplamento, mas também restringe automação. Por isso, definir o catálogo MCP é decidir deliberadamente o alcance cognitivo e operacional do agente.

Retomando o cenário de pedidos, a composição começa com uma tool de negócio como makePriorityShift, que aplica regra real e devolve resultado estruturado. Em seguida, o servidor publica prompts que orientam triagem em lote, diagnóstico individual e comunicação ao cliente, além de resources para listar pedidos e consultar um item específico. Depois, o catálogo é validado no Inspector para confirmar argumentos, mensagens e templates. Por fim, o agente em LangChain consome essas capacidades como functions, executa operações em lote e responde apenas com base nos dados que o servidor decidiu expor.

## Transcrição

00:00

Pessoal, tudo bem? Olha,

00:02

lembro que na aula anterior a gente criou o nosso

00:06

próprio servidor MCP e TypeScript usando o Node.js, né?

00:11

E hoje a gente vai cruzar essa fronteira e usar o Python, tá bom?

00:15

E só para relembrar aqui,

00:17

o FastMCP usa decorator simples para abstrair toda a complexidade

00:21

do protocolo e vamos ver isso na prática,

00:24

tá? Tudo que a gente falou agora, agora há pouco. Bem,

00:27

aqui é o

00:31

seguinte, pessoal.

00:37

Então, vamos lá. Dê uma olhada.

00:39

Nós criamos uma ferramenta que se chama MakePriorityShift.

00:44

Ele recebe o parâmetro id.

00:47

Ele está usando o field. Só para vocês verem aqui,

00:50

gente. O field é da classe Pydantic.

00:52

A Pydantic aqui é o equivalente do Zod e do TypeScript.

00:55

É uma classe muito conhecida para quem trabalha em Python.

00:59

Quem não conhece, pessoal, dá uma pausa, dá uma estudada.

01:03

uma visão geral do que é Pydantic e depois

01:05

retorna super importante para vocês isso aqui,

01:07

tá? Quem trabalha com IA e com Python, tá?

01:10

Pydantic é biblioteca básica, tá?

01:14

Bem, e...

01:18

E a ideia aqui, pessoal, é que essa ferramenta, essa tool,

01:23

ela conecta no nosso banco PostgreSQL e valida se o cliente é Prime.

01:28

E se o pedido está com atraso de entrega maior

01:30

que um dia antes de ativar o envio prioritário. Então, ou seja,

01:34

é tão simples quanto o seguinte, pessoal.

01:37

Valida se o pedido... Vamos lá aqui,

01:39

deixa eu só fechar e tirar aqui. Então, vamos lá.

01:42

Então, vocês podem ver aqui. A gente instanciou.

01:47

o FastMCP, aqui é o nome do nosso servidor,

01:50

aqui é a conexão com o nosso banco de dados PostgreSQL,

01:55

aqui basicamente eu estou pegando essa conexão,

01:58

esse objeto, o que eu faço aqui?

02:01

Eu executo este select no meu banco de dados e vejo,

02:06

se não tem nenhuma ordem, beleza, pedido não foi encontrado.

02:11

Então, primeira validação, o cliente é prime, se é prime,

02:16

Se não é prime, retorna falha. Se é prime e

02:20

o pedido tem uma data de

02:26

entrega maior do que um dia,

02:28

a gente pede o upgrade.

02:32

Então, se o delay for negativo ou menor que 24 horas,

02:35

não está atrasado. Ou seja, agora ele também pode já ser prioritário.

02:42

Mas se não for o caso, de novo, não tem problema.

02:45

Então aqui é o seguinte, no final ele executa o upgrade, ou seja, ele vai lá,

02:49

ou seja, vamos só recapitular, é prime,

02:54

tá com mais de um dia de atraso, beleza?

03:02

Aliás, tem pedido com mais de um dia de atraso, faz update.

03:06

Os outros casos aqui, pessoal, né? Esses citantes aqui, ó. Esse aqui,

03:10

Por exemplo, ó. É se o pedido não está atrasado.

03:14

Esse aqui é se já foi feito um pedido de envio prioritário, né? Então,

03:18

se a gente está aqui e deu uma olhada aqui,

03:21

que interessante, tá vendo? A gente tem o parâmetro de sucesso,

03:23

né? E aqui, que o sucesso é igual a falso e o erro, tá?

03:26

Sucesso é igual a falso e erro. E aqui, no caso,

03:28

o sucesso é igual a true e a mensagem,

03:30

Ó. Envio prioritário ativado com sucesso para o pedido tal do cliente Prime XPTO, tá?

03:35

Então, é tão simples quanto isso. É uma ferramenta simples, tá?

03:37

Super simples, né? O que a gente vai fazer,

03:39

pessoal, é rodar um espectro pra gente poder validar. Vamos rodar um espectro aqui.

03:55

Nosso bom amigo, nosso bom e velho amigo espectro. Vamos conectar no servidor.

04:01

Vamos ter certeza que tem as ferramentas corretas. Beleza,

04:04

está com as ferramentas corretas. Vamos aqui executar um qualquer aqui, ó.

04:12

Falso. Pedido 2 já está finalizado com status de falha.

04:17

Apertei de ignorado. Vamos pegar aqui o 1.

04:21

Esse envio prioritário ativado com sucesso para o pedido 1 do cliente Prime Ana Silva. Então,

04:27

estou aqui para vocês verem que os fluxos que a Atul está funcionando bonitinho.

04:33

Só para garantir que a gente não vai ter depois.

04:36

Agora, vou derrubar o servidor.

04:39

Então, a gente viu aqui.

04:41

É basicamente a aplicação do parâmetro, né? Do

04:45

decorator tool e a questão do pai dente que aqui

04:48

pessoal, que de novo essa descrição aqui, né? Ele vira

04:53

ele vira no final, é semântica, tá? É dentro do

04:56

esquema que vai ser enviado pelo CP7, que fazer isso afastando

05:00

sempre por trás. Então, vamos para a segunda demo,

05:03

tá? Que a distribuição dinâmica de template, né? O que é

05:05

o que é o prompt, beleza? Vamos aqui, ó.

05:11

Eu pulei recursos, tá, pessoal? Depois eu volto nele, beleza? Vamos lá.

05:19

Aqui, inclusive, eu tinha feito esse ajuste, pessoal.

05:26

Esse aqui é o Hayab ajudando a editar, tá?

05:31

Inclusive, vou fazer até uma coisa aqui, pessoal. Seguinte,

05:35

vou fazer junto aqui com vocês, ó.

05:38

Vou fazer o seguinte, ó. Aqui.

05:44

Mudar a ordem, né? Vou colocar na ordem certa, né?

06:06

Beleza. Isso aqui foi. Aqui, recursos.

06:12

Beleza, aqui já estava certo.

06:16

Então, vamos seguir a ordem aqui, tá?

06:19

Bem, pessoal, na hora que eu estava preparando aqui para mostrar,

06:23

eu decidi inverter a ordem,

06:25

tá? Então, eu não tinha renomeado. Vou fazer isso ao vivo aqui. Então, vamos lá.

06:29

Então, o que a gente vai falar agora é da primitiva de recursos,

06:33

tá, pessoal? Basicamente,

06:34

deste decorator aqui. O início é muito parecido, tá vendo? Não tem muita diferença.

06:39

Vão aparecer tipos novos aqui, que é o message,

06:43

user message, assistant message aqui,

06:45

e a gente vai entender um pouco do que está rolando aqui por trás. Bem,

06:50

a gente aqui, pessoal, a gente não definiu apenas um,

06:56

mas três templates de prompt.

06:59

O primeiro que é o relatório pedidos atrasados,

07:02

que é um prompt estático instruindo a IA a fazer a triagem de lote.

07:07

Então, seu diretor logístico, nossa operação,

07:09

sua missão é resolver dois problemas críticos na nossa base de pedidos,

07:12

né? Pedidos com status de falha, né?

07:15

Eita, ia tentar me ajudar.

07:18

Pedidos com status de falha, parar, periri, parar. Então,

07:20

assim, é tão simples quanto o seguinte,

07:22

pessoal. Nesse caso aqui, eu tenho uma mensagem do usuário,

07:27

tá? Assim, é o sistema,

07:28

o framework vai entender que é o usuário fazendo esse pedido,

07:32

tá? E aqui é a mensagem do assistente, tá?

07:36

que é basicamente um sistema, tá bom? Olha lá, perfeito, eu vou

07:39

ler o risco sócio pedidos e imediatamente mapear a situação logística,

07:43

identificarei os pedidos cancelados e falhas atrasados do cliente para executar as

07:46

ferramentas de processamento de dados em lote, por aí vai. Então, esse

07:53

aqui, pessoal, é interessante porque mostra que este pedido aqui vai gerar

07:58

duas listas de mensagens que, no final do dia, equivalem a uma, a uma

08:03

execução encadeada, que para mim é a de dois prontos, tá? Um prompt de

08:09

usuário e um pronto, como se fosse um ponto de sistema, tá bem? O

08:13

segundo, que é o diagnóstico de cliente atrasado, pessoal, ele é parametrizado com

08:18

o pedido, né? Que a gente viu,

08:20

inclusive na, quando a gente tava falando dos conceitos,

08:25

tô aqui, então, o pedido aí, olha que interessante,

08:28

ele entra parametrizado aqui no prompt, né? E aí entra aquela ideia da template, né?

08:35

De ser uma template de prompt, tá? E aqui ele basicamente faz isso,

08:40

ó. Ele direciona o agente a inspecionar uma entrega específica, né? Ou seja,

08:46

validar o CEP e oferecer frete prioritário, tá bom? E, por fim, pessoal,

08:50

gerar comunicado ao cliente, que também é parametrizado com o pedido ID e o canal.

08:54

O canal pode ser e-mail ou SMS.

08:57

Aqui, eu estou criando, na verdade, parece com o de cima,

09:00

mas eu estou colocando dois parâmetros ao invés de um.

09:03

No final, é mais uma template aqui de prompt.

09:06

Então, vamos executar aqui. Vamos até aproveitar e seguir aqui.

09:11

Nós vamos executar o Spector e ver se as tuas estão funcionando.

09:21

Ele sempre abre aqui no meu outro monitor. Não tem problema.

09:25

Vamos primeiro conectar.

09:28

Vamos ver as... Não tem tools, não tem resource,

09:33

mas tem prompts. Tem três prompts aqui.

09:37

Então, olha que interessante, pessoal.

09:39

Get prompt. Vamos ver que prompt ele gerou.

09:43

Prompt estático. Instruir a fazer a descrição.

09:48

Olha que interessante, pessoal.

09:50

Instruir a fazer uma triagem de lote lendo recursos e corrigindo o banco.

09:56

Então, tem duas mensagens.

09:59

que a primeira é a mensagem do usuário,

10:03

a segunda é uma mensagem do assistente, como se fosse um system prompt, tá?

10:07

Beleza. O

10:20

que mais, pessoal? Vamos ver aqui, ó. Aí tem o... Vamos entrar com... Então,

10:26

vamos pegar esse prompt aqui. Opa, está faltando argumento. Como é que envia?

10:34

Ah, vou entrar aqui, ó. Então,

10:39

Pedido parametrizado, triagem individual de um pedido, tá?

10:42

Então, ele gera esse prompt aqui,

10:43

Ó. Por favor, faça o diagnóstico detalhado para o pedido 1.

10:48

Se possui CEP. Enfim, é um prompt aqui de novo.

10:54

Então, beleza, pessoal. Tão simples quanto isso.

10:56

Esses dados aqui, o que ele vai fazer?

11:00

Vocês vão ver que o cliente pega esse prompt aqui,

11:04

esses prompts que ele tem como retorno,

11:06

e já envia para a gente.

11:08

A gente vai ver isso no nosso cliente customizado aqui. Beleza? Já chega neles.

11:13

A gente vai ver como que a gente usaria esse prompt, tá? Esses prompts aqui.

11:21

Então, por fim, pessoal, agora a gente vai para a terceira primitiva,

11:24

que é uma primitiva super essencial, que é a primitiva de resources, tá?

11:29

E aqui a ideia é a mesma coisa, pessoal, né?

11:33

Ó, criei um servidor, conectei com o banco, tá?

11:41

E tem aqui dois resources, tá?

11:44

Eu tenho o resource que lista os pedidos.

11:47

O RI estático lista pedidos não finalizados,

11:52

ou seja, ou pendente ou pago com status logístico. Então,

11:57

é de status, parará, parará, parará, aonde o status está, ou pendente,

12:02

ou pago, ou falha, ou cancelado. Eu vou até colocar aqui, pago,

12:08

falha, falha

12:14

ou cancelado. Beleza?

12:24

Ele basicamente formata aqui do final e fica bonitinho.

12:27

Aqui, na verdade, é para pegar um pedido.

12:29

Ele busca detalhes de um único pedido no banco de dados pelo ID. Tão simples quanto isso.

12:34

Onde o ID do cliente é esse cara aqui. Desculpa.

12:41

Na verdade, ele pega o seguinte.

12:45

Ele pega os pedidos por ID do cliente.

12:52

Na verdade, é isso.

12:57

Então, aqui ele lista todos os pedidos de um

13:02

cliente.

13:14

Tem o pedido status. Então,

13:18

ele faz o join. Ah, desculpa, pessoal.

13:20

Isso aqui é só para garantir. Foi mal, foi mal, foi mal.

13:25

Pela ID, desculpa.

13:28

Então, aqui é o seguinte, pessoal. Isso aqui é só um join, tá?

13:30

Porque eu quero saber quais são os clientes, qual é o cliente daquele pedido,

13:37

tá? Então aqui é o seguinte,

13:39

aqui eu pego o p .id que é o ID do pedido e retorno, beleza? Ele

13:46

formata aqui bonitinho e depois retorna,

13:48

tão simples quanto isso. Vamos ver funcionando usando o inspector. Opa, esqueci

14:09

que eu tinha renomeado. Deixa

14:13

eu ver se aqui tá certinho então,

14:17

retornou, abriu o inspector, vamos

14:22

aqui. Aí, eu quero mostrar, ele não tem tools,

14:26

ele não tem prompt, mas ele usa a primitiva de resource, pessoal. Olha que legal.

14:32

Listar pedidos, tá?

14:34

Ele, olha lá, olha.

14:37

Pedidos. Lista, ID 20, status pago, valor 290, tá? Então, aqui, na verdade,

14:43

ele tem, ele está listando todos os pedidos que estão lá, tá? Beleza?

14:53

Vamos listar. E tem também uma template.

14:57

Que a template, pessoal, é quando é parametrizado, tá?

15:00

Então, nesse caso aqui, eu vou colocar 1.

15:07

Então, aqui eu estou lendo, eu quero ler um pedido cuja ID é 1, tá?

15:12

E nesse caso ele está pago e tem uma previsão de entrega,

15:14

tá? Então, olha que interessante.

15:17

O pedido, o resource, ele pode ser do tipo resources ou resources templates.

15:21

Templates é quando é parametrizado,

15:25

é um resource parametrizado, tá? Que é esse caso aqui, pessoal, tá vendo?

15:29

Ele é mapeado como resource do tipo template, tá bom? Beleza?

15:35

Aqui da passada. Fechado.

15:48

Pessoal, chegou um momento aqui que eu estava doido para que acontecesse, que é o seguinte,

15:55

a gente vai criar o nosso primeiro agente, tá? De verdade. Então,

16:01

aqui eu não vou entrar em detalhes muito de implementação, tá?

16:07

Mas eu quero mostrar para vocês uma coisa que é o seguinte.

16:12

A gente vai... Deixa eu só fazer as atualizações aqui.

16:18

A gente vai criar o nosso primeiro agente,

16:24

que é esse cara aqui. Beleza?

16:30

E esse cara, ele... Então, esse cara, ele vai...

16:34

E a gente vai fazer uma demo que junta todas as primitivas, tá?

16:38

que vai incluir ferramenta de execução assíncrona, com contextos e tudo mais,

16:41

tá? Mas vamos dar uma olhada aqui, ó.

16:46

Veja o fluxo do agente, tá? Então, vamos lá.

16:49

Esse aqui é um agente em Langchain, tá?

16:51

Então, ó. Esse aqui, basicamente, eu estou simulando a execução, a conexão com o IA,

16:57

com o agente de IA, e para que ele use todas essas...

17:02

todos os serviços disponíveis no... que a gente viu até aqui agora,

17:09

gente, ó, é, resources, prompt, tools, tudo mais, beleza?

17:13

Então, só dar uma navegada aqui, ó, é, beleza, esse aqui, ele conectando, então, beleza,

17:20

aqui a gente tem a aula 16, ó,

17:22

tô fazendo um negócio bem bonitinho aqui pra vocês, tá?

17:25

É, ele vai pegar o context, que é o 4, na verdade, né?

17:30

Então, o que que ele vai fazer, né? Ele vai iniciar esse servidor, tá?

17:35

e iniciando esse servidor, pessoal, ele vai lá

17:39

ele vai fazer um callback, tá? Em que

17:44

ele vai começar a chamar em lote,

17:48

tá? É a execução aqui das nossas

17:53

tudo de, só se está, enfim, pessoal, tá vendo aqui ó, é ler esses pedidos, é

17:58

fazer então todos aqueles, aquelas, tudo que a gente viu até agora ali, ó. Tá vendo?

18:03

Enviar express em lote, consultar a CEP, né? Eu criei vários tools aqui, pessoal.

18:07

É parecido com aquelas anteriores lá, tá? É... O que mais que eu fiz aqui?

18:13

É... Parará... E aqui a gente vai ficar conversando com ele,

18:17

tá bom? Né? Deixa eu só ter certeza de que...

18:40

Ah, perdão, pessoal. Isso aqui não é... Isso aqui não é a tool...

18:44

Isso aqui não é a tool do MCP Server, não, tá? Beleza? Tá bom?

18:51

Isso aqui é o callback, tá? É a função de callback para executar em lote,

18:57

tá? Então, nesse caso aqui, só para... Importante, tá, pessoal?

19:01

Eu não tinha atinado para isso na hora que eu

19:04

Estava vendo como explicar para vocês isso aqui.

19:07

Mas o que é importante aqui?

19:09

A gente precisa distinguir que esse agente aqui,

19:14

esse nosso agente aqui,

19:16

ele está usando o modelo da Tropic, beleza?

19:21

E a gente vai usar esse cara aqui, tá?

19:23

Esse cara aqui, ele é o nosso MCP Server, beleza?

19:26

Então, o que esse MCP Server tem? Ele tem uma tool.

19:30

Ele tem a tool de envio prioritário.

19:33

Ele tem a tool de reembolsar lote.

19:37

Ele tem uma tool de envio expresso lote.

19:41

Ele tem uma tool de calcular CEP. Ele tem um resource. Então,

19:46

de novo, gente, isso aqui é o nosso MCP Server.

19:48

Ele tem um resource que lista pedidos.

19:52

Ele tem outro resource que lista pedido por ID,

19:55

né? Ele tem dois prompts aqui, tá? Então,

19:59

ou seja, ele é um MCP Server super completo, tá? Na verdade,

20:02

ele até tem um prompt que é gerar comunicado do cliente. Então,

20:05

ou seja, ele tem todas as três primitivas. Esse aqui é o nosso MCP Server,

20:08

tá? Agora, onde esse cara entra, beleza?

20:11

Esse cara entra o seguinte. Ele vai aqui e vai executar o MCP Server aqui,

20:15

tá bom? Depois que ele executar o MCP Server, tá? Tá aqui, ó.

20:22

Depois que ele executar aqui ó, std client, tá? Quer ver?

20:25

Vamos ver aqui ó, você declarar a gente, né? Falar do MCP. Cláudio.

20:30

CDI, outra que você declara, tá? Ele vai iniciar o servidor e vai

20:34

criar uma conexão e vai conversar com esse cara, beleza? É usar ele, desculpa,

20:40

ele vai, ele vai, ele vai usar o MCP Server, tá? Que está

20:43

dentro desse cara aqui, beleza? Que esse cara, ele declara, tá? Implementa, beleza?

20:50

E esse cara aqui, ele basicamente tem essas... Este aqui, ele tem essas...

20:55

Ele está passando para o nosso agente aqui. Quer ver?

21:03

Olha lá. Ele tem essas tools aqui.

21:08

Posição de resource das tools, como ferramentas do LinkedIn. Ou seja,

21:12

o LinkedIn precisa entender que ele tem essas tools aqui.

21:15

É assim que funciona. Quando você usa o framework. Beleza?

21:20

De novo, o MCP Server é uma coisa.

21:22

A forma como a gente implementa a execução e a chamada desse cara,

21:25

nesse caso do framework Langchain,

21:27

nós usamos tudo como a tool. Porque o Langchain,

21:30

para o agente, para o LLM,

21:35

no final do dia, é um function calling, que equivale a isso aqui. Beleza?

21:39

Isso aqui significa o seguinte.

21:42

LLM, você tem esses métodos aqui e esses métodos você pode chamar.

21:46

E ao chamar, ele vai executar o MCP Server. Tá bom? Vamos lá.

21:52

Vamos executar aqui que a gente vai ver isso acontecendo aqui. Esse

22:14

aqui, ele processando em lote, pessoal. Muito legal.

22:19

Então aqui, chamada de ferramenta reembolsar o lote.

22:22

Então ele foi lá e fez o reembolso de todos esses lotes aqui.

22:26

Só que o que ele está fazendo é execução via MCP Server. Tá bom?

22:32

Inicializa a análise do estorno.

22:35

Aí, ele fala, estorno feito. Beleza.

22:40

Chamada de ferramenta envio expresso.

22:43

Ele vai pegar esses pedidos aqui e vai fazer o envio expresso dele.

22:48

Então, olha só. E o relatório final é o seguinte.

22:50

Reembolso dos estornos resolvidos. Olha só.

22:53

10 pedidos de 10 processados com sucesso.

22:57

Problema 2. Upgrade para envio expresso. Beleza. Ações.

23:01

E tem aqui um chat interativo. Ou seja, pessoal, isso aqui...

23:05

e depois vocês dêem uma analisada depois, né?

23:09

Sugiro que vocês façam isso para entender como foi

23:13

esse fluxo aqui, esse fluxo ágil, porque no final

23:16

do dia a gente está simulando aqui uma

23:18

execução, está simulando, perdão, nós estamos de fato executando

23:21

fazendo uma execução de um agente LLM que

23:24

a gente já de negativa, é, usando o tremor

23:28

cliente em conectado ao MCP server, tá? Então

23:32

vamos lá, só que, só que, olha que legal, pessoal.

23:36

Eu coloquei um prompt aqui: Consulte o status do pedido 2. Se ele estiver atrasado,

23:40

verifique o CEP dele e me diga a rua e se ele se qualifica. Então, beleza.

23:51

Entendi, meu Deus. Agora eu perdi.

23:54

Então, olha só. Isso aqui foi o que eu coloquei.

23:56

Consulte o status do pedido 8. Desculpa.

23:58

Mesmo que você esteja atrasado,

23:59

eu vou consultar o status do pedido 8 novamente, da lista que tenho em mãos. Pegou o pedido.

24:06

Análise do atraso. Status do atraso. Beleza.

24:09

Qualificação para frete prioritário. Sim,

24:11

o pedido qualifica. Critérios atendidos. Parará.

24:14

Ação já realizada.

24:15

O frete prioritário foi ativado com sucesso, com

24:17

o nosso processamento no lote anterior.

24:20

Olha só. Sobre os dados. Infelizmente,

24:22

os dados do pedido que coletei da base não incluem

24:25

informações completas do endereço do cliente.

24:27

Informações disponíveis no sistema.

24:30

Para acessar o CEP e consultar a rua específica,

24:34

seria necessário acessar o banco de dados de endereço do cliente ou ter o recurso.

24:37

Gostaria que você fornecesse o CEP do cliente Carla Mendes, para que...

24:41

Ou seja, pessoal, olha lá.

24:46

Na verdade, ele tentou, ele deveria ter retornado o CEP e não retornou,

24:52

pessoal. Isso aqui tem a ver com minha base de dados.

24:55

Eu vou fazer esse ajuste aqui.

24:58

E retorno para vocês. Eu vou só dar uma pausa aqui. Foi agora a fala do professor,

25:03

tá bom? Vou dar uma pausa aqui e retorno para vocês.

## Resumo IA

[RESUMO_IA]