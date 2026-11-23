Módulo: Protocolos de Comunicação\
Aula: [Tool Calling vs MCP vs A2A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18588)

## Resumo da aula

Tool calling, MCP e A2A resolvem problemas diferentes, embora apareçam no mesmo ecossistema de integração com IA. A distinção correta não é por popularidade da sigla, mas pelo papel arquitetural de cada uma. A pergunta central é simples: o sistema está chamando uma função, acessando uma ferramenta externa ou delegando trabalho para outro agente? Quando essas camadas são confundidas, o sistema até funciona no início, mas acumula acoplamento, dificuldade de evolução e decisões ruins de arquitetura.

Tool calling é o mecanismo mais próximo do SDK e do runtime da aplicação. O modelo recebe uma lista de funções descritas pelo desenvolvedor, escolhe uma delas, a aplicação executa e devolve o resultado para a continuação da resposta. Esse formato funciona muito bem em cenários pequenos, com um LLM, um vendor, um processo e um conjunto conhecido de funções. O limite aparece quando se tenta transformar esse mecanismo local em camada geral de integração.

A primeira limitação é o acoplamento ao vendor: a mesma intenção precisa ser descrita em formatos diferentes conforme OpenAI, Anthropic ou Google, e isso contamina o código ao redor. A segunda é a ausência de discovery padronizado, porque a lista de tools costuma ser montada manualmente e atualizada por redeploy. A terceira é o acoplamento ao processo, já que a função normalmente roda no mesmo ambiente da aplicação que chama o modelo. Por isso, tool calling é excelente como tijolo local, mas frágil como estratégia ampla de interoperabilidade.

Retomando a camada comum já estabelecida, o MCP organiza a relação entre host de IA e ferramentas externas em um modelo cliente-servidor. O host descobre capacidades expostas por um servidor MCP e as consome quando necessário, em vez de embutir manualmente cada integração no SDK de um vendor. A imagem mental correta é vertical: o agente decide a intenção e a ferramenta executa uma capacidade específica. Isso mantém a iniciativa no agente e trata a ferramenta como acesso padronizado a dados, APIs ou operações.

Discovery é a diferença prática mais visível entre MCP e tool calling tradicional. Em vez de registrar manualmente todas as funções em cada aplicação, o host pode consultar o servidor para descobrir quais tools estão disponíveis, por exemplo por meio de tools/list. Essa capacidade transforma a ferramenta em serviço reutilizável por múltiplos hosts, modelos e fluxos. O ganho não é inteligência adicional, mas redução de refatoração, duplicação e lock-in estrutural.

O MCP se apoia no wire format já visto anteriormente: JSON-RPC 2.0. Isso significa que a conversa não depende apenas de abstrações de SDK, mas de mensagens observáveis com método, parâmetros, resposta e erro. O efeito arquitetural é importante porque interoperabilidade deixa de ser promessa informal e passa a ter contrato verificável. Essa base também facilita tracing, debugging e comparação entre implementações diferentes.

A2A muda o problema de acesso para delegação. Em vez de um agente usar uma ferramenta passiva, um agente conversa com outro agente que pode ter LLM próprio, planejamento próprio, ferramentas internas e autonomia de execução. A imagem mental aqui é horizontal, porque os dois lados operam como pares cooperando em uma missão. O foco deixa de ser “qual operação executar” e passa a ser “qual tarefa delegar e como acompanhar seu andamento”.

Quando o outro lado é um agente, o chamador não deveria depender da implementação interna dele. O que precisa estar visível são suas capacidades anunciadas, a forma de invocação e as condições de interação, e isso aparece no agent card. O agent card funciona como mecanismo de discovery para agentes, cumprindo papel análogo ao catálogo de tools no MCP, mas em outra camada. A descoberta deixa de ser sobre funções isoladas e passa a ser sobre serviços autônomos capazes de receber tarefas.

Uma tool costuma seguir um fluxo curto: chamada, execução e retorno. Já uma delegação entre agentes pode durar mais, exigir contexto adicional, pedir input, falhar, ser rejeitada, cancelada ou concluída após várias etapas. Por isso A2A precisa representar lifecycle de tarefa com mais riqueza do que um simples request-response. Essa diferença é decisiva: ferramenta executa operação; agente conduz tarefa.

Tool calling tende a não ter esquema universal, discovery padronizado nem separação natural entre processos, porque nasceu como mecanismo local de execução. MCP introduz contrato comum, discovery de tools e comunicação mais adequada entre componentes separados, mas continua no eixo agente-ferramenta. A2A acrescenta autonomia do outro lado, discovery por agent card e lifecycle mais rico, porque seu problema é coordenação entre agentes. Cada opção é adequada quando o tipo de relação está corretamente identificado.

As três abordagens podem coexistir sem conflito porque operam em camadas diferentes. Retomando o cenário do assistente de pós-venda, o orquestrador delega tarefas para agentes especializados por A2A, o agente redator acessa histórico e políticas por MCP, e um agente interno pode usar tool calling para acionar funções locais do SDK. O mesmo sistema, portanto, combina delegação, acesso padronizado a capacidades externas e execução local. A clareza vem de mapear cada interação para a camada correta, não de eleger uma sigla vencedora.

A decisão pode começar por três perguntas sequenciais. Se o outro lado tem LLM próprio e autonomia, o problema é de agente para agente e A2A tende a ser o encaixe natural. Se não há agente do outro lado, mas a mesma capacidade precisa ser compartilhada entre múltiplos hosts ou modelos, MCP tende a ser a melhor camada. Se nada disso existe e o cenário é um protótipo simples, com um vendor e um processo, tool calling costuma ser suficiente.

## Transcrição

00:02

Opa pessoal, bem -vindos!

00:07

To calling, MCP e HWA.

00:10

Três siglas que aparecem o tempo todo quando a conversa é sobre agentes,

00:13

ferramentas e integração com o IA.

00:15

O problema é que elas costumam aparecer misturadas.

00:19

Às vezes alguém fala de to calling como se fosse uma arquitetura completa,

00:23

às vezes alguém fala de MCP como se substituísse qualquer integração.

00:28

Às vezes alguém fala de A2A como se fosse só mais um jeito de chamar outra gente.

00:32

E aí a discussão fica confusa. Nesta aula,

00:35

o objetivo é simples, separar as camadas. Não é decorar sigla,

00:39

não é escolher uma tecnologia vencedora,

00:41

é entender que cada uma responde uma pergunta diferente.

00:44

Tu colhe e responde a um tipo de problema,

00:47

MCP responde a outro e o A2A responde a outro.

00:49

No final, você deve conseguir olhar para um desenho de arquitetura e dizer,

00:53

olha, aqui eu estou chamando uma função.

00:56

Aqui eu estou consumindo uma ferramenta externa.

00:58

Aqui eu estou delegando um trabalho para outra gente. Então,

01:01

essa distinção parece pequena, mas muda muito a forma de projetar sistemas com IA.

01:08

Porque quando a chamada está certa,

01:10

o sistema pode até funcionar no começo.

01:12

Mas depois ela começa a ficar difícil de manter,

01:15

difícil de escalar e difícil de explicar para o time.

01:17

Então, guarda a pergunta central dessa aula.

01:20

Quando eu integro IA com alguma coisa,

01:23

eu estou falando com uma ferramenta ou com outra agente?

01:26

Essa pergunta vai guiar todo o caminho aqui. Bem,

01:30

são cinco passos a agenda de hoje. A agenda começa, ou seja, o primeiro é o autocode.

01:37

A agenda começa por ele porque foi a primeira forma que

01:40

muita gente usou para conectar LLMs com ações externas.

01:43

Depois vem o MCP. Aqui aparece a ideia de um eixo vertical.

01:48

O agente ou host de IA acessando ferramentas,

01:52

recursos e capacidades externas por um protocolo padronizado. Em seguida,

01:56

o A2A, aí a gente muda de eixo.

01:58

Não é mais agente para ferramenta, é agente para agente.

02:04

Depois disso, vem a bússola. Esse é o momento de comparação.

02:07

A pergunta deixa de ser o que é cada coisa para ser quando eu uso cada uma.

02:12

E por fim, a gente fecha mostrando como elas coexistem.

02:15

Esse ponto é importante, pessoal. A aula não é uma competição entre siglas,

02:19

tá? A aula é sobre encaixe, né?

02:21

Cada tecnologia fica mais clara quando a gente

02:24

entende qual papel ela ocupa na arquitetura, né? Então,

02:28

nós vamos sair do mais básico, passar pela padronização,

02:32

chegar na comunicação entre a gente e depois voltar para a decisão arquitetural. Bem,

02:41

visão geral, tá? Então, temos três camadas de integração com o IA.

02:45

Tu colhe no CPI to A.

02:46

Cada um resolve um problema diferente, como eu disse antes, tá?

02:48

Então, vamos começar sem entrar em todos os detalhes, né?

02:51

Porque cada uma vai ganhar seu próprio slide, né?

02:54

Então, a ideia aqui é só posicionar, tá?

02:57

Tu colhe a camada mais próxima do modelo e do SDK, né? É quando o LLM,

03:01

dentro do fluxo de uma aplicação, decide que precisa chamar uma função.

03:05

Essa função pode buscar dados, capturar algo, gravar informação e chamar uma API.

03:10

Mas a integração normalmente está muito ligada ao vendor e ao runtime da aplicação.

03:15

Então, nesse primeiro bloco, pense em call como um mecanismo interno de chamada.

03:20

Agora, olha para o MCP. O MCP já muda o nível da conversa.

03:23

Ele tenta padronizar a relação entre um host de IA e ferramentas externas.

03:29

A imagem mental aqui é vertical.

03:32

O agente está em cima, decidindo o que precisa.

03:35

A ferramenta está embaixo, executando uma capacidade específica.

03:38

O agente pergunta quais ferramentas você tem. O servidor responde com o catálogo.

03:43

Depois, a gente escolhe e depois... O agente escolhe e chama.

03:47

Por fim, A2A. O A2A muda de novo o tipo de relação.

03:51

Aqui não estamos falando de uma ferramenta passiva esperando ser chamada.

03:54

Estamos falando de outro agente.

03:56

Um agente com sua própria lógica, seus próprios recursos,

03:59

talvez seu próprio LLM, seu próprio ciclo de tarefa.

04:04

Então, a relação aqui é horizontal. Um agente delega trabalho para um outro agente.

04:09

Então... Por enquanto, segura esse modelo mental aí, tá?

04:13

Tu colhe uma ferramenta dentro do ecossistema do LLM,

04:16

MCP é a gente conversando com ferramenta e A2A é a gente conversando com a gente, tá?

04:21

E essas repetições, pessoal, parecem too much, tá? Mas ela é importante, né?

04:26

Para a gente começar a entender de fato o que cada um está fazendo. Porque, realmente,

04:33

às vezes as discussões começam a ficar muito confusas quando

04:36

a gente fala dos três termos ao mesmo tempo,

04:38

tá? Bem... Vamos para o Tukoli, que é a primeira geração.

04:42

O Tukoli foi para muita gente o primeiro contato real

04:46

com a IA fazendo algo fora do texto.

04:48

E é muito legal a primeira vez que eu fiz Tukoli. Pessoal, experiência absurda.

04:53

Além disso, o modelo respondia. E além disso, o modelo respondia.

04:59

Com o Tukoli, o modelo passa... Aliás, perdão, gente. Antes disso,

05:03

o modelo só respondia. Com o Tukoli,

05:05

o modelo passa a poder escolher uma função descrita...

05:09

pelo desenvolvedor. Por exemplo, buscar um pedido,

05:12

consultar um cliente, calcular a frete, abrir um ticket e classificar uma mensagem.

05:19

Então, a aplicação descreve as funções disponíveis. O modelo escolhe uma,

05:24

a aplicação executa e depois o resultado volta para o modelo continuar a resposta.

05:30

Isso funciona muito bem para muitos casos.

05:34

Principalmente quando o cenário é simples, um LLM,

05:36

um vendor, um processo, um conjunto conhecido de funções.

05:39

O problema começa quando tentamos transformar esse mecanismo

05:43

em uma camada de integração mais ampla.

05:45

Olha o primeiro bloco do slide, pessoal, específico do vendor.

05:49

A mesma função precisa ser descrita de formas diferentes dependendo do vendor.

05:55

Ou seja, na UPNA você encontra um formato, no Anthropic outro, no Google outro.

06:00

A gente até já viu isso. A ideia é parecida,

06:03

mas o contrato muda. E quando o contrato muda, o código ao redor também muda.

06:07

Então, agora, o segundo bloco, pessoal, sem discovery padronizado.

06:12

No Tukoli tradicional,

06:14

Você normalmente passa a lista de ferramentas manualmente para o SDK.

06:18

O modelo não sai por aí descobrindo capacidades e tempo de execução.

06:21

Não existe, nesse nível, catálogo aberto e padronizado para ele consultar. Você,

06:26

como desenvolvedor, monta a lista. Você decide o que aparece.

06:31

Você redeploya quando muda. E, por fim, é o acoplado ao processo. Em geral,

06:37

a função chamada roda dentro do mesmo ambiente da aplicação que está chamando o LLM.

06:44

Ou seja, é muito amarrada a ele. Isso não é necessariamente ruim. Para um protótipo,

06:49

por exemplo, isso é ótimo. Para o fluxo simples, é direto.

06:53

Para um produto pequeno pode até ser suficiente,

06:55

mas quando você quer compartilhar a mesma ferramenta entre vários agentes,

06:59

vários modelos ou vários serviços,

07:02

esse acoplamento começa a pesar. Então a frase do rodapé resume bem, olha só.

07:06

Tu colhe e resolve o caso, um LLM, uma venda, um processo.

07:11

Fora dessas fronteiras, ele ainda pode ser usado,

07:14

mas você começa a... pagar em adaptação,

07:17

duplicação e manutenção.

07:18

É justamente esse incômodo que abre próximo para a próxima camada.

07:24

O MCP como eixo vertical. Então, ou seja, MCP,

07:28

a gente já viu várias vezes,

07:29

mas não custa lembrar. Significa Model Context Protocol.

07:32

É o protocolo para contexto de modelo.

07:37

Uma forma simples de pensar nele é o seguinte.

07:41

MCP tenta padronizar a conversa entre aplicações de IA e ferramentas externas.

07:45

Não é só o modelo que chama uma função.

07:48

É uma arquitetura cliente-servidor. De um lado existe o host ou cliente-MCP.

07:52

Do outro existe o servidor-MCP. O servidor expõe capacidades.

07:57

Essas capacidades podem ser tools,

07:59

resources e outros elementos previstos pelo protocolo.

08:02

O host descobre o que existe e chama quando precisar.

08:06

Olha só, pessoal. O primeiro bloco. Ponto de atenção.

08:13

Interoperabilidade e descobre. A palavra descobre aqui é central.

08:16

Em vez de eu escrever manualmente dentro de cada aplicação,

08:19

todas as ferramentas disponíveis... Desculpa.

08:25

Em vez de escrever manualmente dentro de

08:27

cada aplicação todas as ferramentas disponíveis,

08:30

o Roche pode perguntar ao servidor. Quais tools você oferece?

08:33

E o servidor responde com uma lista.

08:35

Esse é um avanço importante em relação ao protocolo impuro.

08:39

Porque a ferramenta passa a existir como serviço separado,

08:42

com um contrato mais claro.

08:44

Eu tenho um servidor MCP para GitHub, PostgreSQL, FileSystems ou Slack.

08:48

Diferentes hosts podem consumir essa capacidade sem precisar

08:52

reescrever toda a integração do zero.

08:54

Agora, olha o que vem depois, pessoal. Padronização e execução.

08:59

MCP usa JSON-RPC 2.0. Olha como as coisas começam a se conectar agora.

09:03

Como base de comunicação.

09:05

Isso conversa com o que a gente já viu antes no iFormat. Ou seja,

09:09

não é apenas uma ideia abstrata. Existe um protocolo de mensagem,

09:12

existe método, parâmetros, respostas, existe erro.

09:15

Isso ajuda muito quando pensamos em interoperabilidade.

09:18

Agora vem a parte conceitual mais importante desse slide, que é o eixo vertical.

09:23

Vertical porque a gente está usando uma ferramenta.

09:26

O agente decide o que quer fazer. A ferramenta executa uma capacidade.

09:31

A ferramenta não está ali para negociar objetivos,

09:34

planejar missão ou tomar iniciativa como um agente autônomo. Ela fornece acesso.

09:41

Pode ser acesso a dados, uma API ou uma operação qualquer. Mas nesse modelo,

09:45

quem decide a intenção é o agente ou o host.

09:48

O servidor MCP executa lógica.

09:53

Ele não precisa ter um LLM próprio e ele

09:55

não precisa ser inteligente no mesmo sentido. Ou seja,

09:59

uma forma segura de pensar é que o MCP

10:01

transforma ferramentas em capacidades descobríveis e reutilizáveis por agentes.

10:07

Isso reduz acoplamento,

10:09

ajuda a compartilhar integração e cria uma camada mais

10:12

limpa entre IA e o mundo externo.

10:15

Mas ainda estamos falando de... Agente para ferramenta.

10:19

Agora a gente vai pensar o seguinte.

10:21

E se do outro lado tiver um agente?

10:22

Aí que entra o A2A. O A2A significa agent to agent.

10:27

E aqui a mudança não é só técnica.

10:31

É de papel arquitetural. No MCP o agente usa uma ferramenta.

10:35

No A2A um agente fala com outro agente.

10:38

Essa diferença parece sutil, mas muda quase tudo.

10:42

Olha só, gente.

10:45

Agentes opacos e discovery. Quando você fala com outro agente,

10:49

você não deveria precisar saber como ele foi construído por dentro.

10:52

Ele pode usar blockchain, pode usar autogênio,

10:55

framework próprio, pode usar outro modelo,

10:57

pode ter ferramentas internas, pode ter MCP por baixo,

11:00

não importa. Para quem chama, isso não deveria ser relevante.

11:04

O que importa é, esse agente aceita tarefas? Quais capacidades ele anuncia?

11:11

Como eu envio uma solicitação e como acompanho o andamento dessa solicitação?

11:16

A ideia do agent card aparece nesse contexto. É o mecanismo de descoberta.

11:21

O agente publica informações sobre quem ele é, o que faz e como pode ser chamado.

11:28

Isso cria uma lógica mais parecida com descoberta de serviço.

11:34

Na sequência, ciclo de vida e delegação. Esse é um ponto muito importante.

11:39

Quando você chama uma ferramenta,

11:41

muitas vezes espera uma resposta direta. Chamei, executou, retornou,

11:44

acabou. Mas quando você delega para um outro agente, a tarefa pode demorar.

11:50

Ela pode exigir mais contexto, pode pedir input, pode falhar, pode ser cancelada,

11:56

pode ser rejeitada, pode terminar depois de várias etapas.

12:00

Por isso o ciclo de vida aparece com mais força em A2A.

12:03

O protocolo precisa representar o estado da tarefa.

12:07

Submetida, em andamento, aguardando input, concluída,

12:10

com falha, cancelada, rejeitada. Enfim,

12:13

não precisa decorar esses nomes agora. O ponto é entender a diferença de natureza.

12:18

A ferramenta executa uma operação ou o agente conduz uma tarefa.

12:21

Essa é a frase-chave do slide. O cliente em A2A é outro agente.

12:27

Não é simplesmente o LLM chamando a função.

12:30

Não é só o host consumindo uma ferramenta.

12:32

É um agente delegando o trabalho para outra gente,

12:35

possivelmente em outro sistema, outro time, outra empresa.

12:39

Agora faz sentido falar em horizontal,

12:41

porque os dois lados têm comportamento mais próximo de pares. Um agente orquestra,

12:47

outro agente executa uma parte da missão e a comunicação

12:50

precisa carregar mais do que parâmetros de função.

12:53

Precisa carregar tarefa, estado, mensagens e resultado.

12:58

Com isso, já temos as três peças principais, né? Agora a gente pode comparar,

13:03

misturar os níveis, tá bom? Então vamos lá, né?

13:06

Esse aqui é o slide de decisão, tá?

13:08

Aqui a gente começa a transformar conceito em escolha arquitetural.

13:12

A tabela compara, tu cola MCP2E por critérios.

13:15

Vamos olhar linha por linha, sem pressa, tá?

13:18

Primeira linha, LLM próprio, né? E tu cola em não.

13:22

A função chamada não tem LLM próprio,

13:24

ela é uma função que a aplicação executa, simples assim.

13:28

E MCP também não, neste modelo mental que a gente está fazendo aqui.

13:32

O servidor MCP expõe ferramentas e recursos.

13:35

Ele executa a lógica, mas não precisa ser um agente inteligente.

13:39

Agora, em A2A, sim. O outro lado é um agente.

13:42

Ele pode ter LLM próprio, planejamento próprio,

13:45

ferramenta própria e ciclo próprio de execução.

13:48

Então, essa linha é uma das mais importantes para decidir.

13:51

Se o outro lado tem autonomia de agente,

13:54

provavelmente você está no território de A2A.

13:57

Segunda linha, esquema padrão. Tem esquema padrão?

14:00

Tu colhe, em geral, não de forma universal.

14:04

Cada venda define seu formato. A gente já viu isso. MCP, sim.

14:08

A proposta é justamente criar um contrato comum.

14:11

E no A2A, sim, no contexto do protocolo. Terceira linha,

14:17

cross-process. Tu colhe, no caso mais simples, também não.

14:21

Ele costuma viver muito perto do processo que chama o modelo.

14:26

MCP e 8-way sim,

14:27

ambos já nascem mais naturalmente como comunicação entre componentes separados.

14:32

Bem, a quarta linha é o discovery,

14:35

ou seja, tu colhe não tem discovery padronizado nesse sentido,

14:38

você fornece funções, é tão simples quanto isso.

14:41

MCP tem discovery de tools, por exemplo, em tools/list.

14:45

8-way tem discovery para o agent card,

14:48

como indicado no slide anterior. Então, quinta linha, life cycle.

14:53

Tu colhe praticamente, não tem Lifecycle rico. Você chamou e recebeu.

14:58

MCP tem algo parcial, dependendo do uso e das capacidades ao redor. Agora,

15:04

o A2A precisa lidar melhor com o Lifecycle,

15:07

porque tarefas entre agentes podem ser longas, assíncronas e multitarefa, inclusive.

15:12

Então, a tabela não está dizendo que uma tecnologia é melhor que a outra.

15:16

Ela está dizendo que cada uma encaixa em um tipo de problema.

15:20

Se você precisa só chamar uma função simples dentro de uma aplicação,

15:24

o Tupole pode bastar.

15:25

Se você precisa expor ferramentas reutilizáveis para diferentes hosts ou modelos,

15:30

MCP faz mais sentido. Se você precisa delegar tarefas para outra gente,

15:35

E2E entra no jogo. Agora vem uma correção importante.

15:39

Escolher uma camada não significa eliminar as outras, tá bom?

15:43

Por quê? Porque elas coexistem, elas não competem, tá?

15:48

O erro é achar que a pergunta é, vou usar TUCOL, MCP ou A2A?

15:52

Como se fosse uma escolha exclusiva, ou excludente, melhor dizendo. Na prática,

15:57

sistemas reais podem usar os três, cada um em sua camada. Olha a ordem do slide.

16:03

A2A aparece como uma camada de cooperação entre sistemas,

16:06

é quando o agente principal delega uma tarefa para agente especializado.

16:09

Por exemplo, um agente de atendimento chama o agente de cobrança.

16:13

Por aí vai. Um agente de logística ou um agente jurídico,

16:16

por exemplo. Cada um pode ter sua própria lógica. Agora,

16:19

o MCP aparece como camada de acesso a ferramentas,

16:22

como a gente já falou várias vezes aqui. Ou seja,

16:24

um agente pode precisar consultar banco de dados, ler arquivos,

16:28

buscar artigos de uma base de conhecimento ou interagir com uma API interna.

16:33

Em vez de acoplar tudo diretamente no SDK de um vendor,

16:37

MCP permite expor essas capacidades de forma mais padronizada.

16:41

E o nível mais baixo, que é o to call. Mesmo dentro de um agente,

16:44

quando ele decide chamar uma função local ou acionar

16:47

uma to descrita no SDK do modelo,

16:49

o mecanismo de to call ainda pode estar presente.

16:52

Ou seja, to call não desaparece. Ele fica como tijolo da execução.

16:57

Ou seja, elas são camadas. Elas não são times rivais.

17:03

A pergunta certa não é qual vence.

17:05

A pergunta certa é em que camada estou operando agora.

17:09

Esse é o tipo de clareza que evita desenho confuso.

17:12

Porque quando você tenta usar tu colhe para tudo, você cria complemento.

17:15

Quando você tenta usar MCP para tratar outra gente como ferramenta,

17:19

perde life cycle e delegação.

17:21

E quando usa A2A para uma função simples, pode criar complexidade demais. Agora

17:32

vamos aplicar o exemplo que está aqui. Ou seja,

17:36

o caso é um assistente de pós -venda.

17:38

O cliente manda uma mensagem, o sistema precisa entender o tipo de solicitação,

17:42

buscar contexto e redigir uma resposta adequada.

17:45

É um cenário simples de visualizar, mas bom para encaixar as três camadas.

17:52

Primeiro, olha só o orquestrador.

17:54

O orquestrador recebe a requisição. Ele não precisa fazer tudo sozinho.

17:58

Ele pode decidir chamar agentes especializados em paralelo.

18:01

Por exemplo, um agente classificador,

18:03

um agente de busca de contexto, ou um agente redator.

18:07

Agora, quando o orquestrador fala com esses agentes,

18:09

estamos no eixo A to A. Por quê?

18:11

Porque ele não está chamando apenas uma função.

18:14

Ele está delegando parte do trabalho para outro agente.

18:17

Esse outro agente pode ter sua própria lógica, seus próprios prontos,

18:20

suas próprias ferramentas e seu próprio ciclo. Agora, olha o agente classificador.

18:25

Ele recebe a tarefa via A2A. Mas, internamente,

18:29

ele pode usar tool calling do SDK do

18:31

vendor para invocar uma função de classificação,

18:34

validar um esquema ou consultar alguma rotina local. Nesse ponto,

18:38

Tool calling aparece dentro do agente. Ele não é a arquitetura inteira.

18:43

Ele é o mecanismo interno. Agora,

18:45

Olha o agente redator. Ele também recebe a tarefa via A2A.

18:49

Mas, para escrever bem, ele precisa de contexto.

18:53

Ele precisa ler o histórico do cliente.

18:55

Talvez buscar artigos da base de conhecimento do cliente.

18:59

Talvez consultar políticas de garantia.

19:01

Essas capacidades podem ser expostas por MCP.

19:04

Então o agente redator usa o MCP para acessar recursos e tools externos.

19:09

Repara no encaixe. A2A conecta o orquestrador aos agentes.

19:13

MCP conecta um agente a ferramentas e recursos.

19:17

Tucoli pode aparecer dentro de um agente com um mecanismo de chamada.

19:20

É a mesma arquitetura, mas em níveis diferentes.

19:24

O resultado é um sistema mais fácil de explicar.

19:26

Eu delego entre agentes como com A2A,

19:29

eu acesso ferramenta com MCP e eu chamo funções internas com TUCOL.

19:35

Bem, guia rápido.

19:37

Imagine que você está no whiteboard escolhendo arquitetura.

19:41

Não comece pela sigla, comece pela pergunta.

19:44

Outro lado tem LLM próprio? Se sim, provavelmente está falando com agente,

19:49

então o mecanismo natural é A2A. Não porque A2A seja melhor.

19:53

Mas por que o problema é de delegação entre agentes?

19:56

Se a resposta for não, vá para a segunda pergunta.

20:00

Múltiplos LLMs ou múltiplos hosts vão consumir essa ferramenta?

20:03

Se sim, MCP tende a fazer sentido.

20:06

Porque agora o problema é padronização e reutilização.

20:09

Você não quer reescrever a mesma integração para cada vendor,

20:12

cada aplicação e cada agente.

20:14

Você quer expor uma capacidade de forma mais estável. Se a resposta for não,

20:18

vá para a terceira pergunta. É um protótipo simples com LLM?

20:23

Um vendedor em um processo? Se sim, tu colhe e provavelmente basta.

20:27

Isso não é errado.

20:28

Tu colhe uma ótima escolha quando o problema é pequeno o suficiente.

20:32

O erro não é começar simples. O erro é fugir,

20:35

é fingir que o simples continua simples quando o sistema cresce.

20:39

Por isso a regra de bolso do slide funciona bem.

20:42

Ou seja... Comece com o Tucoli numa POC, por exemplo.

20:46

MIG para MCP quando cruzar mais modelos,

20:48

mais ferramentas e mais necessidades de compartilhamento.

20:51

E adicione A2A quando houver mais um agente cooperando.

20:54

Não trate isso como lei absoluta, obviamente.

20:57

Trate como uma heurística de arquitetura.

20:59

Com o tempo vocês vão entendendo e vão refinando isso melhor. Ou seja,

21:03

ela ajuda a fazer a primeira pergunta certa e

21:06

muitas vezes isso já evita a decisão errada.

21:11

Pessoal, a gente... Falou de Tucoli, de MCP, de A2A, tá?

21:17

E agora, a gente aguardando para a próxima aula,

21:21

que vai ser o lab comparativo,

21:22

onde a gente vai colocar a mão na massa, tá bom? Até lá!

## Resumo IA

[RESUMO_IA]