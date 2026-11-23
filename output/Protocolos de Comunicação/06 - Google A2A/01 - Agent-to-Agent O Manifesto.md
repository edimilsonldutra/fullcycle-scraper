Módulo: Protocolos de Comunicação\
Aula: [Agent-to-Agent: O Manifesto](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18613)

## Resumo da aula

Quando cada agente adota seu próprio dialeto de integração, a colaboração entre agentes escala mal. Se o agente de estoque precisa falar com o de logística, e depois ambos precisam interoperar com faturamento, atendimento ou antifraude, surgem adapters específicos para cada par de agentes. Esse crescimento N×N multiplica custo de manutenção, fragilidade operacional e dependência acidental de frameworks. Em vez de uma fronteira estável entre domínios, a arquitetura vira uma malha de integrações ponto a ponto.

Vendor lock-in horizontal acontece quando os agentes ficam presos ao modo de comunicação de um framework ou fornecedor, não por mérito funcional, mas porque toda a rede de colaboração já depende daquele dialeto. O custo de trocar um runtime deixa de ser apenas migrar um agente isolado e passa a incluir reescrever suas integrações com todos os demais. Em cenários enterprise, isso reduz liberdade arquitetural e dificulta composições entre times, plataformas e fornecedores diferentes. Um protocolo comum reduz esse aprisionamento ao padronizar a fronteira, não o interior do agente.

A2A define como um agente expõe capacidades e recebe trabalho de outro agente sem exigir alinhamento de framework, memória interna ou ferramentas locais. O protocolo não substitui LangChain, LangGraph, CrewAI ou runtimes equivalentes; ele atua na borda de comunicação entre agentes. Retomando o cenário de colaboração entre estoque e logística, a fronteira padronizada permite que cada lado preserve sua implementação interna enquanto participa do mesmo fluxo operacional. O ganho arquitetural está na interoperabilidade horizontal entre agentes autônomos.

A passagem do A2A para a Linux Foundation altera o valor arquitetural da especificação porque reduz a percepção de controle exclusivo por um fornecedor. Governança aberta sinaliza continuidade, participação multilateral e maior previsibilidade para adoção em produção. Esse tipo de maturação institucional importa tanto quanto a sintaxe do protocolo em ambientes enterprise, onde risco de dependência estratégica pesa nas decisões técnicas. A trajetória relevante é anúncio inicial, abertura de governança, evolução da spec e aumento de tração no ecossistema.

A distinção mais útil entre A2A e MCP é o eixo da integração. MCP opera no eixo vertical: um agente consome ferramentas, APIs, bancos, documentos ou funções externas como capacidades. A2A opera no eixo horizontal: um agente delega ou coordena trabalho com outro agente que possui autonomia, contexto, estado e responsabilidade própria sobre uma tarefa. Os dois coexistem naturalmente; um agente especialista acionado por A2A pode usar MCP internamente para acessar sistemas e dados.

Agent Card é o contrato público de descoberta do agente. Ele informa identidade, endpoint, capacidades suportadas, esquema de autenticação e skills oferecidas, funcionando como um cartão de visita técnico consumível por software. Em vez de integração baseada em conhecimento prévio informal, o cliente consulta metadados padronizados antes de interagir. Isso viabiliza descoberta automatizada e reduz acoplamento entre quem chama e quem implementa.

A forma mais simples de localizar o Agent Card é publicar o documento em um caminho conhecido como /.well-known. O cliente resolve o domínio do agente, faz um GET nesse endpoint e recebe o JSON com as instruções necessárias para iniciar a interação. Em ambientes enterprise, esse não é o único mecanismo possível: catálogos privados, registros internos e configuração direta também são válidos. A ideia central é separar descoberta de execução, para que o cliente saiba com quem está falando antes de enviar trabalho.

Task é a unidade operacional central do A2A. Diferentemente de uma chamada efêmera de API, ela pode durar no tempo, acumular contexto, receber atualizações, pedir novos inputs e encerrar com sucesso ou falha. Retomando o cenário de estoque e logística, uma solicitação de separação e envio não precisa caber em uma única resposta imediata; ela pode evoluir conforme o trabalho avança entre agentes. Essa persistência torna o protocolo adequado para colaboração real, não apenas para RPC simples.

Message representa a troca de contexto dentro de uma Task, tanto do cliente para o agente quanto no sentido inverso. Part é a granularidade interna da mensagem: uma mesma Message pode combinar texto, arquivos, dados estruturados ou referências, sem reduzir toda a interação a uma string. Esse modelo acomoda fluxos mais ricos, nos quais agentes trocam instruções, evidências e resultados parciais em formatos diferentes. A semântica da conversa fica estável mesmo quando o conteúdo varia.

Os estados da Task tornam o trabalho observável. Em vez de apenas aguardar uma resposta final, o cliente consegue saber se a tarefa foi submetida, está em execução, precisa de input adicional, exige autenticação ou já atingiu um estado terminal como conclusão ou falha. Essa visibilidade é decisiva em fluxos enterprise porque permite monitoramento, retomada e tratamento operacional de exceções. Os nomes oficiais da spec importam porque padronizam integração entre implementações diferentes.

A2A separa o significado da colaboração do meio de transporte usado para carregá-la. Agent Card, Task, Message e Part continuam os mesmos conceitos, independentemente de o binding usar JSON-RPC, HTTP + JSON ou gRPC. Essa separação evita que a arquitetura de interoperabilidade fique presa a um único estilo de comunicação. O transporte pode variar conforme o ambiente, enquanto a semântica do protocolo permanece estável.

JSON-RPC oferece um formato leve e familiar, fácil de inspecionar em logs, traces e ferramentas HTTP. HTTP + JSON se encaixa melhor em ambientes já organizados em torno de API Gateways e convenções REST corporativas. gRPC, com Protobuf e streaming nativo, tende a ser mais adequado para sistemas internos de alta performance. A escolha do binding muda características operacionais, mas não altera o contrato conceitual do protocolo.

Nem toda Task deve ser tratada como request/response simples. Quando o trabalho demora ou produz progresso incremental, o agente pode emitir eventos por streaming, tipicamente com Server-Sent Events, para informar andamento e resultados parciais. Também existe o acompanhamento assíncrono por assinatura de updates, no qual o cliente registra interesse em mudanças de estado e conclusão. Isso transforma a interação em um fluxo observável e persistente, em vez de uma chamada bloqueante única.

A2A não cria um mecanismo proprietário de segurança; ele reaproveita padrões já consolidados como Bearer Token, OAuth 2.0, API Key, OpenID Connect e mTLS. O Agent Card declara o esquema exigido, mas não carrega o segredo em si, que deve ser obtido por um fluxo apropriado e enviado na requisição. Autenticação responde quem está chamando; autorização decide o que esse chamador pode fazer dentro daquele agente. A política de acesso continua sendo responsabilidade arquitetural da implementação do servidor.

A2A faz sentido quando existe uma fronteira real entre agentes autônomos: outro runtime, outro time, outro domínio, outro fornecedor ou outro sistema que assume responsabilidade por uma Task. Se o outro lado apenas expõe uma capacidade bem definida, como consultar banco, chamar API ou executar função local, o caso tende a ser de MCP ou tool calling. Esse critério evita overengineering e preserva o protocolo para cenários em que há colaboração entre agentes, não simples invocação de ferramenta. A pergunta decisiva é se o outro lado é um agente autônomo ou apenas uma capacidade consumível.

## Transcrição

00:01

Olá pessoal, hoje começamos uma etapa importante de nossa jornada de

00:05

arquitetura de software para sistemas de IA.

00:07

Vamos falar sobre o Edge-to-Edge, ou Edge-to-Way.

00:11

Eu uso Edge-to-Edge porque é a forma mais intuitiva de entender a ideia,

00:16

a gente falando com a gente. Mas pode falar Edge-to-Way que também funciona bem.

00:22

Enfim, a visão aqui é simples e poderosa.

00:26

Permitir que agentes de IA colaborem sem que precisem conhecer o framework,

00:30

a memória, as ferramentas ou a implementação interna do outro.

00:33

Um agente pode estar em LingGraph,

00:35

outro pode estar em LingChain ou qualquer outro framework.

00:39

Pode estar em CrueAI, em Google SDK, enfim, não importa.

00:46

Pode estar em uma plataforma corporativa e ainda assim

00:49

todos conseguem conversar por uma fronteira padronizada.

00:53

Esse é o manifesto da aula,

00:54

que é sair de agentes isolados e começar a pensar em ecossistemas de agentes.

00:58

A diferença entre improvisar integrações ponto a ponto e usar um protocolo como

01:03

o E2A é a diferença entre criar silos e construir uma arquitetura interoperável.

01:10

Então, primeiro nós vamos entender o problema,

01:13

o caos N por N de integrações entre agentes antes de existir uma fronteira comum.

01:19

Depois vamos passar pela timeline real do E2A.

01:22

que é o anúncio pela Google,

01:24

doação para Linux Foundation, amadurecimento e especificação.

01:27

Em seguida, vem uma distinção fundamental, que é A2A versus MCP.

01:32

Essa é uma das confusões mais comuns de arquitetura de agente hoje.

01:37

E depois vamos fixar o vocabulário base, agent card, task, message e part.

01:43

Por fim, fechamos olhando para o ecossistema I26.

01:47

para entender por que isso deixou de ser só uma

01:49

ideia experimental e passou a ser discutida como infraestrutura.

01:55

Vamos ao problema central.

01:57

Por que precisamos de um protocolo para a gente conversar? Antes do A2A,

02:01

cada framework ou empresa tendia a criar seu próprio dialeto.

02:04

Se o agente A precisava falar com o agente B,

02:07

alguém escrevia um adapter específico. Se depois entrava o agente C,

02:11

mais adapters. Se entrava o agente D,

02:15

mais integrações. No pior caso, com integrações direcionais,

02:19

chegamos a N vezes N, menos uma conexão.

02:23

Bem, com cinco agentes, isso pode virar...

02:26

20 relações de integração, com 10 agentes, 90.

02:29

E o problema não é só a quantidade. Cada adapter precisa entender o vocabulário,

02:34

os formatos e os comportamentos do agente específico.

02:37

Esse é o vendor lock-in horizontal.

02:41

Você fica preso a um dialeto de framework, não porque ele é tecnicamente melhor,

02:45

mas porque todos os seus agentes já dependem dele para conversar.

02:49

O A2A entra como uma camada comum de fronteira.

02:53

Ele não substitui o Langchain, ou o Autogen, ou o Cruear,

02:56

ou qualquer outro framework com runtime interno.

02:58

Ele define como o agente expõe capacidades e aceita o trabalho de outro agente.

03:04

A timeline do A2A é curta, mas ela é muito relevante. Em abril de 2025,

03:09

Google anunciou o A2A Protocol com mais de 50 parceiros iniciais.

03:13

Dois meses depois, em junho de 2025,

03:16

Veio o movimento mais importante do ponto de vista de governança.

03:19

O projeto foi levado para a Linux Foundation.

03:21

Com a transferência da especificação SDK e Turing. Isso muda a percepção do mercado.

03:26

O gateway deixa de parecer apenas uma iniciativa de um

03:29

fornecedor e passa a operar sob uma governança aberta,

03:32

com participação de grandes empresas de cloud, software, cooperativa e integração.

03:36

No primeiro ciclo de maturação, a especificação evolui,

03:39

a autenticação ganha forma mais padronizada e a versão

03:42

1.0 marca uma fase de estabilidade maior.

03:46

No marco de um ano,

03:47

a Linux Foundation reporta mais de 150 organizações apoiando o

03:51

padrão e mais de 22 mil stars no repositório.

03:54

Não decore o patch version do SDK, porque isso muda rápido.

03:58

O que importa aqui é a trajetória. Anúncio,

04:01

governança aberta, amadurecimento da spec e adoção enterprise.

04:06

Este é um dos slides que eu gosto mais aqui, um dos mais importantes aqui da aula.

04:11

Por que 2A e MCP são confundidos o tempo todo?

04:16

A forma simples de separar é pensar no eixo. MCP fica no eixo vertical.

04:21

Um agente ou um modelo usa ferramentas, APIs,

04:24

bancos de dados, documentos ou funções externas.

04:27

É o agente consumindo uma capacidade.

04:30

H-way fica no eixo horizontal, agente falando com agente.

04:33

Todo o outro lado não é só uma função.

04:36

Ele pode ter autonomia, estado, ferramentas próprias,

04:39

contexto próprio e capacidade de participar de uma tarefa de forma mais ativa.

04:43

Em uma arquitetura real,

04:45

os dois coexistem.

04:46

Um agente pode usar A2A para delegar trabalho a outro agente especialista.

04:51

E esse agente especialista pode usar MCP internamente para acessar Port Grease,

04:56

uma API corporativa ou sistema de arquivo.

04:58

A regra de arquitetura é MCP conecta agente a

05:02

capacidade e A2A conecta agente a agente.

05:07

Agora vamos fixar o vocabulário que vocês vão

05:10

ouvir em praticamente toda discussão sobre A2A.

05:14

O primeiro conceito é o Agent Card.

05:17

Pense nele como um cartão de visita técnico do agente.

05:20

Quem ele é, qual endpoint expõe, quais capacidades suporta,

05:24

como autenticar e quais skills ele oferece.

05:26

O segundo é a Task. A2A não é só uma chamada efêmera de API.

05:31

O protocolo trabalha com a ideia de unidade de trabalho.

05:35

Uma task pode ser criada, acompanhada, atualizada e finalizada.

05:39

O terceiro conceito é Message.

05:42

Carregam a conversa ou o contexto dentro de uma task.

05:45

Elas podem ir de um cliente para o agente ou do agente para o cliente.

05:50

O quarto conceito é parte.

05:52

Uma mensagem não precisa ser só texto.

05:55

Ela pode ser composta por partes, texto, arquivo,

05:58

dados estruturados ou referências. Quando falamos de estados,

06:02

vou usar termos simples como submit, work e completed.

06:06

Mas na spec V1.0, os nomes aparecem no formato.

06:12

task_underscore_state_underscore_submitted,

06:14

ou task_underscore_state_underscore_working,

06:18

task_underscore_state_underscore_completed,

06:20

e assim por diante. Mais adiante, também vamos falar de artifacts,

06:24

que são uma forma comum de devolver resultados de uma task.

06:31

Bem, pessoal, aqui a gente está falando de wire format, tá?

06:36

A decisão importante é... O A2A não tenta reinventar toda a pilha de transporte.

06:42

Ele define uma semântica de colaboração entre agentes e

06:45

essa semântica pode trafegar por bytes diferentes.

06:50

O primeiro caso é o JSON-RPC, que é familiar, leve e fácil de inspecionar em logs,

06:55

traces e ferramentas HTTP. O segundo é HTTP mais JSON,

06:59

mais próximo do estilo REST tradicional.

07:03

Bom para ambientes como API Gateways e padrões corporativos já existentes.

07:07

O terceiro é o gRPC,

07:09

usando protobuf e stream ativo.

07:13

Últimos sistemas internos de alta performance. Um cuidado.

07:17

Quando o slide mostra nomes como task/send ou task/subscribe,

07:23

leia isso como vocabulário conceitual.

07:25

Na versão 1.0, a fala correta é send message,

07:29

send streaming message, get task, cancelTask ou subscribeToTask.

07:34

No Binding Raster, aparecem endpoints como /message2.send,

07:40

/message2.streams e /tasks/{id}. O

07:44

ponto principal é mudar o transporte e não mudar a semântica.

07:48

AgentCard, task, message e part continuam sendo o vocabulário central.

07:53

Como a gente encontra outro?

07:56

Pelo AgentCard. A forma mais simples é o padrão /.well-known.

08:02

O cliente conhece o domínio do agente,

08:07

faz um get nesse caminho conhecido e recebe o JSON dizendo quem é aquele agente,

08:14

onde ele atende, quais capacidades suporta, como autenticar e quais skills oferece.

08:19

A analogia com o OpenID Connect ajuda porque o padrão mental é parecido.

08:24

Você consulta um endpoint conhecido e recebe metadados

08:28

que ensinam como interagir com aquele serviço.

08:31

Mas não é a mesma intensificação, tá, pessoal? É só uma analogia didática.

08:34

Também é importante entender que /.elnone não é o único caminho possível.

08:39

Em ambientes enterprise pode haver registros internos,

08:42

né? Ou seja, catálogos privados, enfim,

08:45

configuração direta, tá? Agora, se o agent card revelar capacidades sensíveis,

08:49

endpoints internos ou skills restritas,

08:52

ele precisa ser protegido com autenticação e autorização, né?

08:55

A mensagem deste slide é, antes de chamar um agente A2A,

08:59

você descobre quem ele é pelo agent card.

09:03

Agora entramos no ciclo de vida da task.

09:06

A diferença para uma API comum é que

09:09

uma task A2A pode viver ao longo do tempo.

09:13

Ela pode começar,

09:15

trabalhar, pedir mais inputs, exigir autenticação, terminar com sucesso ou falhar.

09:20

Temos três modos principais de interação. O primeiro é o request/response.

09:25

útil para tarefas curtas. Na spec v1.0, pessoal,

09:29

pense em sendMessage ou no REST post /message2.send.

09:35

O segundo é stream, tá? Aqui o agente devolve eventos incrementais,

09:40

Normalmente via Server Sent Events,

09:43

para mostrar progresso ou resultados parciais. Na versão 1.0,

09:47

pessoal, pense em sendStreamMessage ou em REST post barra message 2.stream.

09:53

O terceiro é a assinatura assíncrona de updates. Nesse caso,

09:58

o cliente acompanha o estado da task e registra

10:01

interesse em notificação de atualização e conclusão.

10:04

Na fala, a gente vai usar... Gente, é que é importante o seguinte,

10:08

pessoal. A gente precisa usar, ter os nomes oficiais do estado,

10:11

tá? Então, quando vocês forem falar, pessoal, usem o test,

10:15

task.state.submit, task.state.work e por aí vai, tá?

10:23

Eu acho que isso é importante porque foi uma mudança da versão 0.3,

10:27

que era das mais utilizadas para essa.

10:31

E o ponto central é que o A2A torna o trabalho observável,

10:35

ou seja, você consegue saber se a task que está andando travou,

10:38

precisa de input, precisa de autenticação e já chegou a um estado terminal.

10:45

Agora aqui, pessoal, não existe colaboração entre a gente sem confiança.

10:48

Por isso o H2A não inventa um modelo de autenticação do zero.

10:52

Ele se apoia em padrões conhecidos no mundo web e enterprise.

10:56

O AgentCard declara como o cliente deve se autenticar,

11:02

que é o Bear Token, OAuth 2.0, API Key,

11:06

OpenID Connect, MTLS, dependendo do caso.

11:10

Isso é parecido com a forma como APIs ou OpenAPIs já descrevem security schemes.

11:16

Mas atenção, o AgentCard não deve carregar segredo estático. Ele declara o esquema,

11:21

a credencial em si é obtida por um fluxo apropriado,

11:25

tá? Muitas vezes fora do protocolo e enviada nas requisições.

11:30

Também é importante separar autenticação de autorização.

11:33

Autenticação responde quem é você.

11:35

Autorização responde o que você pode fazer.

11:38

Autorização é a responsabilidade da implementação do servidor do agente,

11:42

tá? Ele pode considerar skill chamada,

11:45

ação dentro da task, políticas de dados, tenant, grupo, papel ou scopes off.

11:50

Ou seja, no fim é isso.

11:53

A2A padroniza como descobrir e declarar requisito de segurança,

11:56

mas a política de acesso continua sendo desenho de arquitetura enterprise.

12:03

Agora vamos falar do ecossistema, e aqui a mensagem é simples.

12:06

O A2A deixou de ser apenas uma proposta inicial da Google,

12:10

passou a operar como um projeto de governança aberta da Linux Foundation.

12:14

No marco de um ano,

12:17

a Linux Foundation reportou mais de 150 organizações apoiando o padrão,

12:21

e mais de 22 mil estrelas no repositório.

12:24

Isso é um sinal importante de tração. Code providers, vendas enterprise,

12:28

plataformas de agentes e integradores passaram a tratar a

12:31

E2A como uma peça relevante de interoperabilidade.

12:34

Sobre SDKs, cuidado com o número exato, porque ele muda rápido.

12:38

Ou seja, no marco de abril de 2026,

12:41

a comunicação pública falava de 5 linguagens production-ready.

12:45

Na documentação atual do projeto, já aparecem SDKs oficiais em 6 linguagens.

12:50

Também não vale mais comparar com o MCP dizendo que existem só dois SDKs oficiais.

12:56

Esse número está desautorizado.

12:57

O ponto não é competir com o MCP por quantidade de SDK.

13:01

O ponto é que a 2A e o MCP

13:03

estão amadurecendo peças complementares de arquitetura de agentes.

13:08

Em produção e adoção pública, pessoal,

13:10

vemos grandes plataformas de cloud e software corporativo se movendo nessa direção.

13:14

O importante é tratar exemplos como sinais de ecossistema,

13:17

não como promessa de compatibilidade universal automática.

13:21

E sobre o futuro, em vez de especular I3E ou ISO,

13:25

o próximo passo mais concreto é validação, TCK,

13:29

ferramenta de inspeção, redices e boas práticas enterprise.

13:32

Isso é que transforma o protocolo em infraestrutura confiável.

13:39

Bem, esse slide, pessoal, ele evita o overengineering, tá? E2E é poderoso,

13:44

mas não é para tudo. Se você só precisa chamar uma ferramenta externa,

13:48

consultar um banco, buscar um documento,

13:50

executar uma API ou disparar uma operação bem definida,

13:54

isso é domínio do MCP, tá? Ou de Tukoli mesmo.

13:57

O outro lado não é um agente com agenda própria, é uma capacidade.

14:02

Se a função é sua, dentro do seu próprio runtime,

14:06

menos ainda. Use o protocolo local mesmo.

14:09

Não coloque rede, autenticação, agent card,

14:12

lifecycle de tasks ou de uma chamada de função resolve.

14:15

Agora, se o sistema é monoagente, H2A também não ajuda muito.

14:19

H2A começa a fazer sentido quando existe uma fronteira real entre agentes.

14:23

Outro runtime, outro time, outro domínio,

14:26

outro fornecedor ou outro sistema com autonomia.

14:29

A regra prática mais precisa é, se o outro lado tem autonomia,

14:32

manter estado, negocia contexto ou assume responsabilidade por uma task.

14:37

Pense em A2A nesse caso.

14:39

Se o outro lado só expõe uma capacidade com entrada e saída bem definida,

14:44

pense em MCP ou TUCOL em local mesmo.

14:46

Bem, pessoal,

14:48

isso era o que eu queria falar nesse primeiro slide,

14:54

nessa primeira aula sobre A2A.

14:55

Nós vamos ter outras aulas, tá? Daqui pra frente. Agora,

14:58

o mais legal mesmo vai ser os laboratórios, tá? Beleza? Até mais.

## Resumo IA

[RESUMO_IA]