Módulo: Protocolos de Comunicação\
Aula: [LangGraph part 2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18932)

## Resumo da aula

compile() é a etapa que transforma a definição declarativa do grafo em uma aplicação executável. Enquanto nodes e edges descrevem a receita da orquestração, o compiler materializa essa receita em um workflow pronto para rodar, com transições, estado e integração com persistência. invoke() é a porta de entrada de execução: recebe o input inicial e dispara o grafo já compilado. No MVP do Resolution Center, isso separa claramente modelagem de fluxo e execução real do atendimento.

Retomando o Resolution Center já estabelecido, o fluxo mínimo usa um state tipado simples e dois nodes locais: node_atendente e node_analista. O atendente extrai a intenção do ticket e o analista transforma esse resultado em uma resposta conversacional. Esse desenho é útil como base porque mostra a passagem explícita de contexto entre etapas, mas também expõe a limitação central do fluxo isolado: sem integração externa, o sistema ainda precisa pedir dados que a empresa já possui.

node_triagem introduz roteamento dinâmico dentro do grafo. Em vez de codificar a decisão com if/else espalhado, o node grava no state uma categoria, e o router devolve o nome do próximo node com base nesse valor. As conditional edges conectam essa decisão ao fluxo, permitindo enviar o ticket para reclamação, comercial ou técnico sem perder a estrutura declarativa. O comportamento do sistema muda de pipeline fixo para orquestração orientada por classificação.

O router não executa trabalho de domínio; ele converte um valor do state em próxima transição válida do grafo. Isso importa porque a decisão deixa de ser implícita no código de um node e passa a ser parte testável da topologia do workflow. No exemplo de e-commerce, uma mensagem sobre parcelamento segue para o caminho comercial, enquanto uma reclamação ativa outro especialista. A escalabilidade vem dessa separação entre classificar e executar.

A memória contínua surge quando o checkpoint passa a ser gravado em armazenamento persistente com SqliteSaver. Em vez de manter contexto apenas em memória de processo, cada passo do grafo gera um snapshot do state que pode ser recuperado depois. Isso transforma o atendimento em uma execução retomável por identidade, não em uma conversa efêmera. O ganho prático é continuidade operacional mesmo entre invocações separadas.

thread_id é a chave que associa execuções diferentes ao mesmo histórico persistido. Quando o mesmo identificador é enviado na configuração, o grafo recupera o state anterior e continua a partir daquele contexto; quando o identificador muda, uma nova linha de atendimento começa do zero. No Resolution Center, usar o nome ou ID do cliente como thread_id permite lembrar produto, pedido e contexto sem exigir que o usuário repita tudo. A memória deixa de ser global e passa a ser segmentada por identidade.

A continuidade observada aqui não depende de uma janela de chat acumulando mensagens arbitrariamente. O que persiste é o state do workflow, com os campos que a orquestração decidiu registrar e reutilizar. Isso torna a memória mais controlável, auditável e alinhada ao processo de negócio. No exemplo, o sistema lembra a TV comprada porque esse dado foi salvo no state associado ao thread_id de João.

node_investigador_remoto muda a fronteira de execução: o node local deixa de resolver tudo com LLM na mesma máquina e passa a disparar uma chamada remota para um agente especializado. A coordenação continua no LangGraph, mas a investigação logística ocorre fora do processo, via A2A sobre HTTP. Esse padrão preserva especialização e permite que o orquestrador componha capacidades distribuídas sem absorver a lógica de cada domínio. O efeito arquitetural é um grafo local governando execução remota real.

O agente remoto pode devolver um dado frio, como prazo padrão de entrega ou ausência de fornecedor identificado. Esse retorno bruto ainda não é a resposta final ao cliente; ele precisa ser reinterpretado por um node analista que preserve fidelidade ao dado e adicione clareza, tom e empatia. A tradução conversacional existe para transformar saída operacional em comunicação útil sem inventar fatos. O sistema, assim, separa obtenção de evidência e formulação da resposta.

Retomando os componentes já construídos, o planner extrai o ID do ticket e dispara duas consultas em paralelo: uma para o servidor MCP ligado ao PostgreSQL e outra para o agente logístico via A2A. O grafo deixa de depender de uma única fonte e passa a consolidar dados financeiros e operacionais na mesma execução. Quando ambos retornam, o sintetizador combina os resultados e produz uma visão única do caso. Esse fan-out seguido de síntese reduz latência e aumenta cobertura informacional.

A síntese final não apenas concatena respostas; ela reconcilia formatos e lacunas entre fontes heterogêneas. Se o PostgreSQL retorna dados financeiros completos e a logística informa que o ticket não contém fornecedor suficiente, a resposta final precisa expor o que foi confirmado e o que ainda está ausente. No Resolution Center, isso produz uma resposta mais honesta e operacionalmente útil. O grafo passa a funcionar como cérebro central que organiza coleta, memória, roteamento e consolidação.

## Transcrição

00:01

Pessoal, nós já construímos agentes autônomos e orquestrações simples.

00:05

Mas quando o projeto cresce e chega na vida real,

00:08

a inteligência bruta da LLM não basta. Precisamos de processos,

00:11

de fluxos determinísticos, de loops controlados.

00:14

E é exatamente aqui que brilha o Lang Graphs.

00:16

Ele é o maestro que transforma agentes soltos numa orquestra.

00:20

E hoje nós vamos construir os blocos fundamentais

00:23

do nosso Resolution Center de e-commerce. Bem...

00:28

Vou prestar atenção aqui, pessoal, nesse primeiro aqui,

00:31

que é o mínimo. Aqui temos o MVP do nosso suporte.

00:35

É a base absoluta do LangGraph, dividida em cinco pilares estruturais.

00:40

O primeiro é o State.

00:44

Notem que usamos um simples TypeDict, um dicionário mesmo.

00:49

Ele é o coração do ticket de atendimento.

00:52

Pense no State como uma folha de papel que vai

00:54

sendo passada de mão em mão entre os nós.

00:56

Se não está no State, não existe no grafo. O segundo pilar são os nós. Vamos

01:03

ver que a função é node atendente e node analista.

01:10

Então, a gente tem o node atendente e o node analista.

01:14

Um node nada mais é do que uma função Python que recebe o ticket, faz o trabalho,

01:19

extrai a impressão ou rascunha a resposta,

01:21

por exemplo, e atualiza aquela folha de papel.

01:25

Então, sempre isso, ó. Recebe o State, tá?

01:30

Agora, vamos ver como é que a gente compila, né? Esse workflow, tá?

01:36

E como que a gente conecta as coisas. Então, olha só.

01:42

Com o terceiro pilar, os edges, que são as arestas, né?

01:46

A gente vai

01:47

criando o nosso gráfico,

01:53

tá? Então, olha só.

01:55

É declarativo, explícito e claro. Então, ao final,

01:58

nós chamamos o Workflow Compiler, que é o nosso quarto pilar,

02:04

que pega essa receita e transforma em uma aplicação rodável,

02:07

executável. E, por fim, o Invoke.

02:13

O Invoke, pessoal,

02:15

ele... Vou achar aqui. O

02:19

Invoke, pessoal, nada mais é...

02:23

do que a gente entrar com uma, obviamente,

02:28

com crompt, tá? E executar, beleza?

02:32

Então, vamos ver isso no Streamlit, pessoal, acontecendo, ó. Vamos ver.

02:38

Então, vamos pra demo 1, ó.

02:41

Comprei o celular ontem e agora o status não mudou. O que que houve? Vamos ver.

02:48

É um fluxo linear. Atendente e analista.

02:51

O atendente extrai a intenção do ticket e o analista rascunha a resposta.

02:56

Olha só. Ele extraiu a intenção e gerou uma resposta conversacional educada. Está aqui embaixo.

03:03

Mas repare no detalhe. A gente pediu o número do pedido.

03:08

Se você for olhar, olha só.

03:12

Deu uma olhada no pedido para confirmar o status.

03:14

Quer que eu dê uma olhada no seu pedido? Óbvio. Só preciso do número. Ou seja,

03:20

a gente já não sabe quem é o cliente logado.

03:26

A gente não tem o banco de dados da loja.

03:30

É por isso que o agente isolado, apenas o LLM, não serve para a produção.

03:34

Ele precisa estar conectado aos sistemas corporativos.

03:38

E é exatamente esse problema que vamos resolver na nossa demo final hoje.

03:44

Agora, vamos para a segunda. Então, vamos lá.

03:48

Mas a verdade dura é que no e-commerce o mundo não é uma linha reta.

03:52

E se precisarmos direcionar o cliente para o setor de retenção ou vendas,

03:56

por exemplo. Então,

04:00

vamos ver aqui o node de triagem.

04:03

Aqui tem o node de triagem. Agora, pessoal,

04:06

isso aqui é uma evolução. Vamos ver o node de triagem.

04:09

Ele avalia se o ticket roteia para o time correto. Então, vamos ver aqui.

04:13

Vejo que é para lá e vamos ver

04:17

aqui ó, eu adicionei também uma conditional adicional, é de

04:22

condicional, é que ele só vai ser chamado para triagem, tá?

04:27

Se tiver uma reclamação, né? Se for uma reclamação para o

04:30

tipo de reclamação, se for comercial, esse por então, simples, quanto

04:32

isso. Então aqui a gente tem o seguinte: ó, tem

04:36

um novo triagem, tem uma nova reclamação, tem um novo comercial e

04:39

tem um novo técnico, tá? E tem o router.

04:42

O router, ele lê a categoria do estado e devolve o nome do próximo nó, tá bom?

04:49

Então, a gente passa qual nó, resumindo o seguinte:

04:52

a gente está passando aqui qual nó toma a decisão,

04:55

né? Que é o triângulo. O link do grafo, ele pausa o fluxo,

04:58

olha para o valor que é o triângulo,

05:00

cuspiu e dinamicamente ativa o setor correto. Sem if,

05:03

else, espaguete, tá? Tudo no contrato do grafo.

05:06

Então, vamos ver aqui, ó, no Streamlit.

05:20

Nó de triagem, categoria e reclamação. Enviou para o nó de reclamação.

05:24

E aí, resposta.

05:31

Como vocês podem ver,

05:33

o LLM triou corretamente para o setor comercial

05:35

e ativou o agente especializado de vendas. Vamos ver.

05:51

Na verdade, é o seguinte. Nesse caso, ainda é reclamação.

05:56

Agora, eu vou mudar o prompt, pessoal.

06:01

Eu errei aqui, eu usei o mesmo, o default,

06:07

esqueci de colar. Então, vamos ver aqui, ó.

06:13

Então, vamos ver. Ó, vocês parcelam 12 vezes no cartão de crédito,

06:16

a gente vai pelo caminho diferente, tá?

06:24

Ó, nó comercial.

06:28

Então, olha que interessante, pessoal. No outro, reclamação foi certinho, tá?

06:33

Agora, a parcela é o seguinte. Como vocês podem ver,

06:36

o LLM criou corretamente o setor comercial e

06:38

ativou o agente especializado de vendas.

06:40

Escalabilidade pura. Sensacional. Então, vamos lá.

06:46

Agora, como seria um atendimento contínuo? Então, até aqui,

06:50

cada vez que rodávamos o grafo, ele começava do zero, com amnésia.

06:53

Mas no canal de atendimento ao cliente, precisamos de memória de contexto contínuo.

06:58

Então, seria esse caso aqui, que é a demo 3. Então, olha só.

07:04

Olha o que a gente demonstra, ó.

07:07

Agora tem o thread ID, tá? Que é o nome do cliente.

07:11

O LLM lembra o número do pedido dele, tá? Aí,

07:14

quando é um outro cliente, ele, obviamente, começa do zero, tá?

07:19

Mas se você voltar para o anterior, ele vai fazer tudo certinho.

07:22

Então, aqui é o seguinte, olha, pessoal. Vamos ver aqui,

07:24

ó. SQL Lightsaver, tá? Vamos ver aqui, ó.

07:49

Olha só. O link graph, ele resolve a memória com o checkpoint.

07:53

O que isso faz? Ele tira um snapshot, uma foto do estado do grafo,

07:57

e a cada passo se grava no banco usando o SQL Saver, tá bom?

08:02

É isso que ele faz. Checkpoint e ele salva lá, beleza? Então, olha só.

08:10

Para recuperar o histórico do cliente,

08:12

nós simplesmente passamos o thread ID dele na configuração, tá bom?

08:18

É esse cara aqui, o thread ID.

08:21

Eu adiciono o thread ID na configuração, beleza?

08:25

Aí eu invoco a mensagem, que é o pedido, e a gente vê o próximo estado histórico.

08:32

Agora, vamos dar uma olhada no Streamlit,

08:38

como é que isso aqui funciona? Vamos ver. Cliente João.

08:43

Vamos colocar aqui.

09:00

Você comprou TV conosco, que produto excelente.

09:03

Posso ajudar? Agora nós vamos colocar.

09:06

Pode confirmar o produto que eu levei?

09:15

Sim, você levou a TV 4K conosco, é isso mesmo?

09:19

Olha só, reparem, eu não passei o produto na segunda mensagem,

09:22

mas o assistente recuperou o estado inteiro do SQL Lite com base no cliente João, tá bom?

09:30

Então, o atendente agora tem continuidade, ou seja,

09:32

isso aqui não é um chat, tá, pessoal? Então,

09:35

se ele fez transformar no chat, ele falou,

09:37

eu comprei a TV, aí terminou esse fluxo, ele reseta. Aí,

09:41

quando ele voltou, pode confirmar o produto que eu levei?

09:44

Como eu não mudei o ID do cliente,

09:47

obviamente ele mantém, tá? Agora vamos colocar aqui, ó.

09:50

Vamos mudar o ID do cliente, tá?

09:53

De cliente agora é Maria, beleza?

09:57

Oi, sou Maria.

10:21

Agora eu vou mudar para o João.

10:29

E a gente vai ver que ele vai falar... Ah, já viu?

10:32

Voltou para o João e ele resgatou da memória, tá?

10:35

E não é porque está salvo que não, tá, gente?

10:38

Ele realmente usou o SQL Lite. A gente salvou isso no banco de dados, tá? Beleza?

10:45

Então, o seguinte, nós temos o que faz a triagem, o especialista é a memória.

10:51

Falta apenas uma coisa, buscar dados do mundo real.

10:54

E se o nosso analista precisar investigar no stop?

10:57

Então, aí que entra o... Perdão,

11:04

pessoal. Aí que entra... Agora nós vamos fazer o link graph,

11:08

acionar um agente externo via A2A.

11:11

Então, olha só. Preste atenção na mudança do paradigma.

11:13

O nosso Node Investigator remoto... tá achando

11:19

aqui para vocês o Node Investigator remoto, tá? Ele não chama o LLM local na mesma

11:25

máquina, beleza? Tá? É ele dispara uma requisição

11:30

HTTP via protocolo HTTP/2 para o investigador remoto,

11:33

muito legal, né? Então, seja, tá aqui ó.

11:37

Chamar 8way tá, ele vem aqui que que

11:40

Eu chamar 8way faz, olha só, ele cria

11:43

Uma chamada HTTP e envia para o agente,

11:48

Tá? Então, ou seja, a gente não tá aqui fazendo o código no Python aqui agora.

11:52

Então, vamos ver isso acontecendo? Olha que legal.

12:05

O nó investigador, aí

12:08

O nó executado, que é o analista, ó.

12:15

Um, dois, três, então a gente tem... Então,

12:17

Ou seja, é... Pessoal, no final,

12:23

Olha só. Isso significa que o Link Graph virou o orquestrador macro da empresa.

12:27

E fizemos isso de forma totalmente distribuída.

12:30

Ele está se comunicando com agentes reais em tempo real, sem simulação.

12:34

Reparem no tom incrível dessa resposta.

12:36

O agente logístico remoto nos devolveu um dado frio de sistema.

12:40

Mas o LLMLocal, o analista, traduziu isso com empatia e fluidez.

12:46

Sem informações do fornecedor. É do produto logístico,

12:50

Prazo estimado, padrão para entrega, cinco dias úteis,

12:52

Tá vendo? Então, aí o analista, ele gerou uma resposta bacana para o cliente, tá?

12:59

Ou seja,

13:01

A nossa orquestração mesclou a governança do State Graph

13:04

Com a força técnica do H-Way.

13:06

Ou seja, a fundação, ela está pronta, tá?

13:08

Agora a gente vai fazer um sisteminha

13:15

Completo, tá, galera? E aí vocês vão ver que massa, tá? Então, olha só.

13:20

Tudo o que vimos até aqui foi legal.

13:22

Mas lembra que no módulo 3 nós criamos um servidor

13:24

E um ICP de banco de dados PostgreSQL?

13:26

E no módulo 5 e 6 nós criamos um agente remote H2A para cuidar da logística?

13:31

Então, a gente vai conectar isso tudo agora, galera. Então, olha só. Vamos

13:37

Ver aqui. Add. Olha só.

13:47

O Planner extrai o Add e então chamamos aqui no adicionar Adds, que é o Add.

13:55

Então, ele adiciona aqui, Start Planner, Planner, Planner. E aí,

13:59

É o seguinte. Quando ambos finalizarem, o sintetizador junta tudo.

14:02

Aí, junta o MCP financeiro, que vem da logística,

14:05

Para o sintetizador. E depois, o sintetizador termina.

14:08

Então, ou seja, agora o Lang Graph é o cérebro central.

14:11

O Planner extrai o ID do ticket.

14:14

E é mais o que acontece aqui. Workflow .Edge, Planner, MCP financeiro. Nesse aqui.

14:23

Planner, MCP financeiro, Planner, H2A, logística. Sim, pessoal,

14:27

O Lang Graph está adicionando o servidor MCP

14:30

PostgreSQL e o agente 8-Way paralelamente.

14:33

E quando ambos retornam, o sintetizador junta tudo. Então, olha só. Vamos ver aqui.

14:45

O nó MCP Financeiro, pessoal, o que ele está fazendo?

14:49

Ele está chamando o MCP Server.

14:53

E, no caso, o logístico está chamando o 8-Way.

14:58

Vamos agora ver o... o resultado disso, pessoal? Ficou muito legal.

15:10

Tem o ID, o MCP financeiro foi lá, executou, o MCP de logística falou,

15:17

Não consigo processar, só o ticket formado, não específico fornecedor.

15:20

Aí, o sintetizador, olha só, PostgreSQL, cliente,

15:25

Nome Maria, saldo, status entregue, motivo cancelamento, custo...

15:31

E armazém físico, não consigo processar essa notificação.

15:33

Ticket informado não especifica o fornecedor ou

15:35

pedido identificado no contexto logístico disponível.

15:38

Para obter status, nome do fornecedor ou nome do produto específico.

15:45

Olha a interface. Na coluna da esquerda,

15:47

dados financeiros puxados diretamente do nosso PushGreen.

15:50

E na coluna da direita, dados físicos do armazém puxados via protocolo E2A.

15:53

E embaixo, a resposta rígida da DLLM cruzando tudo isso, tá? Então, pessoal,

15:58

a gente consegue, de alguma forma, extrair toda a complexidade, tá?

16:03

É, é de um fluxo de término de um fluxo

16:06

a gente tá conectando agora, nós conectamos todos

16:09

os pontos do que a gente desenvolveu até aqui, tá? Agora, é o que a gente então

16:16

seja então, foi um building box, tá? Ou

16:20

seja, dominamos os cinco pilares do link gráfico,

16:22

coroamos com efeito a alta união do MCP e da Link Green, tá bom? Isso aí, pessoal.

## Resumo IA

[RESUMO_IA]