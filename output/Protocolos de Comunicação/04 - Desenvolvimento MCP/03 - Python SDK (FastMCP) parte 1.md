Módulo: Protocolos de Comunicação\
Aula: [Python SDK (FastMCP) parte 1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18600)

## Resumo da aula

FastMCP é a camada de mais alta ergonomia do SDK Python para MCP. Ele preserva a mesma arquitetura já conhecida — server, schema e transport — mas reduz o trabalho mecânico de declarar capacidades, contratos e descrições manualmente. O ganho principal não é “esconder o protocolo”, e sim usar a própria função Python como fonte de verdade do contrato exposto. Isso reduz drift entre implementação, validação e documentação operacional.

A camada low-level fica mais próxima do protocolo e oferece mais controle, ao custo de mais detalhe e mais cerimônia. A camada high-level, representada pelo FastMCP, troca esse custo por produtividade: decorators registram capacidades, type hints ajudam a formar o schema e docstrings viram descriptions consumíveis pelo host. A escolha não é irreversível, porque o SDK continua permitindo descer de camada quando o caso exigir controle fino. O ponto arquitetural é separar produtividade de perda de semântica: a semântica do MCP continua a mesma.

A instância mcp = FastMCP("Meu Server") ocupa o papel central de registro das capacidades do servidor, de forma análoga ao que já foi visto na trilha TypeScript. Sobre essa instância, três decorators organizam a superfície semântica do servidor: @mcp.tool para ação, @mcp.resource para leitura contextual e @mcp.prompt para intenção guiada. Essa divisão importa porque evita modelar tudo como tool e melhora a forma como host e usuário interagem com o servidor. O transporte continua explícito em mcp.run(transport="stdio").

Um servidor mínimo em FastMCP costuma ter import da camada high-level, criação da instância, uma função decorada e um bloco if __name__ == "__main__" para inicialização. O nome passado ao FastMCP não é cosmético: ele participa da identificação do servidor no handshake e ajuda na operação quando existem múltiplos servidores parecidos. O decorator @mcp.tool transforma uma função Python comum em capacidade exposta, sem exigir montagem manual da camada protocolar. O guard evita subir o servidor durante import, testes ou pipelines de CI.

No FastMCP, a assinatura da função deixa de ser apenas detalhe interno e passa a compor o contrato externo da capability. O nome da função, os parâmetros tipados, a docstring e o tipo de retorno fornecem insumos para inferir nome, description, input schema e conteúdo estruturado. Isso desloca a manutenção do contrato para perto do código que realmente executa a regra. Quando a função muda, o contrato tende a mudar junto, o que reduz inconsistências silenciosas.

Field permite anexar restrições e descrição diretamente ao parâmetro, como min_length=1 e texto explicativo, sem duplicar essas regras em outro artefato. Literal fecha o domínio de valores aceitos, como "C" | "F", transformando uma string genérica em enumeração operacional simples. Por baixo, o Pydantic usa essas anotações para validar a entrada antes do handler rodar, cumprindo o mesmo papel de validação na borda já conhecido da trilha TypeScript. Quanto melhores os tipos, mais forte fica a fronteira da tool.

Retornar dict ou outra estrutura explícita melhora a composição com host e com etapas posteriores de raciocínio. Texto livre ainda funciona, mas perde previsibilidade quando outra etapa precisa extrair campos, correlacionar resultados ou encadear decisões. Em MCP, estrutura no retorno não é apenas conveniência de serialização; ela melhora interoperabilidade semântica. A escolha do formato de saída afeta diretamente a qualidade do consumo da capability.

Retomando o cenário de pedidos, a mesma capacidade de negócio pode ser separada em três primitivas com papéis diferentes. tool representa ação com efeito, como cancelar um pedido; resource representa leitura idempotente, como consultar um pedido ou listar pedidos; prompt representa uma intenção guiada, como investigar um pedido com profundidade básica ou detalhada. Essa separação organiza melhor a experiência do usuário e evita tratar leitura previsível como se fosse decisão operacional.

Um resource combina uma URI com uma função leitora. A URI pode ser estática, como uma lista conhecida, ou parametrizada, fazendo o placeholder virar argumento do handler. O critério de modelagem não é “parece consulta”, e sim “é leitura idempotente e contextual?”. Se repetir a operação não altera estado nem dispara efeitos colaterais, a modelagem como resource tende a ser a mais adequada.

Prompt, nesse contexto, não é texto solto de uso individual, mas um artefato operacional exposto como menu no host. O usuário escolhe uma intenção guiada, preenche campos controlados e dispara um fluxo padronizado que pode orientar o uso das tools disponíveis. Isso transforma prompt engineering em ativo versionável, revisável e sujeito a code review. A governança melhora porque a intenção deixa de ficar dispersa em documentos ou memória tácita da equipe.

Context transforma uma tool de “função que recebe input e devolve output” em operação observável. Ele entra como parâmetro explícito, o que evita estado global implícito e facilita teste, leitura e manutenção. Métodos como info, warn e error produzem logs estruturados; report_progress comunica andamento; sample permite pedir inferência ao host quando necessário. Isso é especialmente importante em operações longas, em lote ou dependentes de APIs externas.

Quando o transporte é stdio, o stdout faz parte do canal protocolar com o host. Usar print nesse fluxo pode misturar logs com mensagens do protocolo e corromper a comunicação. Por isso, logs operacionais devem passar pelos mecanismos apropriados do Context ou por logging estruturado compatível com a execução. O erro costuma parecer pequeno no código, mas produz falhas difíceis de diagnosticar em runtime.

A escolha por Python faz sentido operacional quando o servidor precisa conviver com automação, análise tabular, inferência, ORMs e chamadas HTTP assíncronas já presentes nesse ecossistema. O FastMCP reduz o atrito para expor essas capacidades como primitives MCP sem reescrever a lógica em outra linguagem. A vantagem não é apenas sintática; ela está na proximidade com bibliotecas e fluxos que já existem no ambiente real do time. Isso acelera integração sem alterar o modelo arquitetural do protocolo.

## Transcrição

00:01

Oi pessoal, tudo bem? Vamos lá! Esta aula é sobre o Python SDK,

00:06

mais especificamente sobre o principal componente do SDK, que é o FastMCP.

00:12

E a ideia aqui é bem direta, pegar a especificação MCP,

00:17

que a gente já vem construindo nas aulas anteriores,

00:20

e olhar para ela pela porta de entrada mais produtiva do ecossistema Python.

00:25

E repara no detalhe e no nome, não é só o Python SDK.

00:30

A gente coloca e fecha MCP junto e isso importa, tá pessoal?

00:35

Porque na prática a maioria dos times não quer começar escrevendo

00:38

o CV do MCP no nível mais baixo possível.

00:41

O que normalmente se busca no começo é velocidade de integração.

00:45

E transformar uma função Python comum em uma tool, resource ou prompt, né?

00:50

Com poucas linhas e pouca cerimônia, acho que esse é o grande objetivo, tá?

00:55

Bem, vamos então começar.

01:03

O primeiro momento, pessoal, ele responde por que o FastMCP existe.

01:08

Antes de sair escrevendo o decorator,

01:10

a gente precisa entender qual problema ele resolve. Sem isso,

01:14

você olha para o decorator de tool e pensa, nossa, isso é mágica, né?

01:19

E não é mágica, né? É ergonomia em cima de um contrato que já existe.

01:24

O segundo momento conecta as três peças com os três decorators.

01:29

Aqui a gente liga o mundo anterior com o novo server, scheme,

01:35

transporte continuam valendo só que agora aparece como

01:38

instância decorator e ramp e o

01:41

terceiro momento é o server iniciando o

01:45

server inicial em três linhas aqui, aqui

01:50

entra o código real e é importante porque mostra o esqueleto

01:56

que você provavelmente vai repetir em muitos servers em Python e quando

02:01

E o quarto, na verdade, é o quarto momento,

02:06

na verdade, pessoal, é a integração e a sync.

02:09

Aqui aparece o argumento de domínio. Python não entra nesta aula por hype.

02:14

Python entra porque muita automação, análise tabular, inferência, ORM,

02:20

chamada HTTP assíncrona, já vive nesse ecossistema.

02:24

Então, guarda a progressão. Razão, depois forma,

02:27

depois código, depois integração operacional. Bem,

02:33

agora entra a tese técnica da aula.

02:38

E ela começa com uma constatação simples.

02:41

O Python SDK tem duas camadas. Essa ideia organiza tudo o que vem daqui para frente.

02:47

De um lado, existe uma camada low-level.

02:49

Low-level significa ficar mais perto do protocolo,

02:53

mais controle, mais detalhe, mais responsabilidade e,

02:56

naturalmente, muito mais cerimônias.

02:59

Do outro lado existe a camada High Level e aqui que entra o Fast MCP.

03:03

E no Fast MCP a palavra-chave é ergonomia.

03:07

Decorators, esquema inferido, docstring virando description,

03:11

Type Hint virando contrato.

03:14

Repara que aqui eu estou resumindo isso em uma única frase.

03:20

DX maior que boilerplate. Ou seja...

03:25

Developer Experience é a experiência de quem desenvolve, é o DX.

03:30

Ou DevEx, muita gente chama de DevEx.

03:33

E aqui essa frase não é ilógica, ela é bem operacional mesmo.

03:36

O problema em sistemas reais é quase nunca escrever o esquema manual uma vez.

03:42

Isso qualquer pessoa faz. O problema é manter esquema, validação,

03:47

descrição e implementação alinhados depois que o código começa a mudar.

03:53

Se a função ganha um parâmetro novo e o esquema não acompanha, você criou drift.

03:57

O código e o contrato começam a se descolar em silêncio.

04:00

Se o docstring promete uma coisa e o handler faz outra,

04:03

o modelo de linguagem pode escolher mal quando usar aquela capacidade.

04:08

Se o tipo muda e a validação fica antiga,

04:10

o bug aparece na borda, na chamada, no host,

04:13

no usuário final ou no log de produção.

04:16

E é esse tipo de desalinhamento que o Fashion CP tenta reduzir.

04:20

A ideia é usar o próprio Python como fonte da verdade.

04:23

A assinatura da função, os type hints,

04:25

a docstring e o retorno passam a compor o contrato que o serviço expõe.

04:31

Agora, olha para esse bloco de pacote, pessoal. Eu costumo confundir no começo.

04:38

Então, a leitura prática para esta aula é o seguinte, tá?

04:41

O caminho foi ao pacote oficial, que é o MCPCLine.

04:46

Ele é a base... Ele é a base de tudo que a gente vai usar aqui nesta aula.

04:53

O projeto Fecha MCP aparece aqui porque tem uma história própria.

04:57

Ele foi doado à Anthropic e pode carregar nuances ou recursos específicos.

05:03

Mas o ponto pedagógico aqui não é decorar pacote,

05:06

pessoal. É entender o modelo mental. Fecha MCP é uma camada de autoria.

05:10

Ele não muda a semântica do MCP. Ele muda o custo de escrever o servidor MCP.

05:16

E é por isso que o último bloco aqui, pessoal,

05:18

funciona bem. Quem nunca usou, olha e pensa. Isso é mágica.

05:24

Prefiro escrever na mão. Quem já usou em um projeto real,

05:28

normalmente muda a pergunta.

05:29

Por que eu escreveria esquema manual se a assinatura da função já diz quase tudo?

05:34

Então, este é o ponto importante.

05:37

Fashion CP não esconde arquitetura. Ele esconde repetição mecânica.

05:41

E quando você precisa descer uma camada,

05:44

o low level continua lá. Então, não é uma prisão.

05:46

É uma escolha de produtividade com rota de escape.

05:50

De novo, vamos guardar isso aqui. O FastMCP não troca a semântica do MCP.

05:54

Ele troca o custo de autoria do servidor.

05:58

Bem, agora

06:00

a gente conecta esta aula com o que já foi construído antes.

06:03

Repara só, pessoal. Server, esquemas e transporte continuam valendo.

06:07

O FastMCP não remove essas peças.

06:10

Ele só reduz a cerimônia para trabalhar com elas.

06:14

A primeira peça é a instância do FastMCP.

06:17

MCP igual FastMCP, meu servidor, mais server.

06:20

Meu server. Então, essa linha ocupa o papel do novo MCP server,

06:26

que a gente viu lá em TypeScript.

06:27

Ele cria o ponto central onde o server registra capacidades.

06:31

Depois vimos três decoradores principais.

06:34

O MCP tool, que registra ações. O MCP resource,

06:38

que expõe leitura contextual via URI.

06:40

E aqui vale prestar atenção na diferença, resource não é ação,

06:44

e só ser dado acessível como contexto.

06:47

E MCP prompt, que transforma prompt em um menu do host.

06:50

Não é o modelo escolhendo sozinho, é o usuário disparando uma intenção guiada.

06:56

E no fim vem o transporte. MCP.run transporte igual a STDIO.

07:02

Essa linha define como serve a conversa com o host.

07:05

Localmente, STDIO costuma ser o caminho mais comum.

07:08

Em produção, normalmente aparece outro transporte.

07:12

Vamos no foco disso tudo que a gente falou aqui.

07:15

Decoradores escondem boilerplate,

07:17

mas arquitetura MCP continua exatamente ali por baixo.

07:21

Você reduz código repetido sem perder a semântica do protocolo. Bem,

07:27

agora o primeiro código real da aula. Então,

07:31

aqui a gente precisa ficar mais direcionado.

07:36

Repara primeiro no import.

07:39

Fecha MCP.

07:41

from mcp.server.festmcp import festmcp. Isso

07:48

confirma que estamos usando a camada high level do SDK.

07:53

Na linha seguinte, MCP igual festmcp meu server.

07:57

Esse nome não é só em face, o meu server,

08:00

tá gente? Ele identifica o servidor no handshake.

08:03

Quando o host e o server se apresentam, isso é super importante.

08:09

Em ambientes com vários servers parecidos, isso evita muita confusão operacional.

08:13

Depois é o ponto central do slide, que é o MCP.tool, que é o decorador.

08:17

Esse decorador registra a função abaixo como uma tool MCP.

08:22

A função continua sendo o Python comum,

08:24

mas agora vira uma capacidade exposta pelo server.

08:27

Olha a função ping.

08:29

Ele retorna string, str. Então o SDK já tem uma pista de esquema.

08:35

A docstring também importa.

08:37

Ela vira description e ajuda o host e o

08:40

modelo a entenderem para que aquela tool serve. Bem,

08:55

corpo, pessoal, o retorno é um Pog, com um timestamp UTC.

09:00

Isso é útil porque confirma a execução real daquele instante,

09:04

não só uma resposta antiga ou cacheada.

09:10

Ou seja, no final, olha o guard aqui.

09:14

Ele evita, que é o if name igual a main,

09:17

ele evita que o server suba sem querer durante import,

09:20

test ou continuous integration.

09:24

E dentro dele vem MCP.run transport stdio.

09:29

Este é o entry point, é onde o server começa a conversar com o host.

09:34

Guarda cinco pontos, então, de tudo que a gente falou aqui.

09:36

Nome do server, decorator.

09:38

Docstring, transporte e guard. O esqueleto é curto,

09:41

mas cada linha tem função operacional.

09:44

Agora a gente entra no ponto onde o FreshMCP começa a pagar a conta.

09:48

Type hint virando esquema. Olha para o decorador.

09:52

MCP.to. Ele registra a função abaixo como a tua MCP.

09:57

Agora olha para a assinatura da função get_weather.

09:59

Até aqui parece Python comum. Mas repara no parâmetro sit.

10:08

Ele é uma string, uma str. Mas não só isso.

10:12

Ele usa um field com min length igual a 1 e uma description.

10:18

Isso quer dizer que parte do contrato da tool está escrita junto ao parâmetro.

10:22

Não está perdida em outro arquivo. Não está duplicada em esquema manual.

10:27

Agora, olha o parâmetro unit.

10:30

Ele usa literal C e F.

10:34

No modelo mental de Scheme, isso funciona como um conjunto fechado de valores.

10:37

A função não aceita qualquer string.

10:39

Ele aceita C ou F. Tão simples quanto isso, que é o Celsius ou Fahrenheit.

10:44

Então, vamos lá.

10:47

TypeHint aqui não é só ajuda de editor. TypeHint vira contrato de entrada.

10:52

A docstring também tem papel operacional.

10:54

Ou seja, no final, a docstring descreve a tool para o host e para o modelo. Então,

11:00

uma docstring ruim não é só documentação ruim.

11:03

Ela pode levar o modelo a escolher mal quando invocar a ferramenta.

11:06

Isso é super importante, tá, pessoal?

11:09

E o retorno como dict indica que a resposta vem estruturada.

11:14

Isso facilita a leitura pelo host e por etapas posteriores, tá?

11:19

Texto solto funciona,

11:20

mas dado estruturado costuma ser muito melhor para encadear raciocínio.

11:25

Agora, vamos dar uma olhada aqui embaixo, pessoal. Olha só. O

11:30

flash MCP infere automaticamente o nome da tool.

11:33

A description, o input schema e o structured content.

11:37

Mas a parte mais importante é a última linha, validação e borda.

11:41

O Pydantic rejeita input inválido antes do handler executar. O Pydantic,

11:47

pessoal, foi usado nesse field. Esse field e o literal,

11:52

ele vem do Pydantic. Ou seja, no final,

11:55

ele equivale ao Zot,

12:00

que a gente viu lá no TypeStream.

12:03

No TypeScript, beleza?

12:05

Zod, no TypeScript.

12:09

Bem, em produção isso muda o lugar onde o erro aparece.

12:13

Então, se a borda está bem tipada,

12:14

muita coisa ruim nem chega na lógica de domínio.

12:17

Por isso a regra prática é simples. Quanto melhor o tipo,

12:20

melhor o contrato. N e dict genérico parecem flexíveis,

12:24

mas muitas vezes jogam fora a principal vantagem do PSMCP.

12:27

Ou seja, type hints bons não documentam só o código,

12:31

eles protegem a fronteira da tool.

12:35

Agora a gente entra numa distinção crítica, o decorator de resource.

12:38

Se você passar rápido por aqui, começa a transformar toda a leitura em tool.

12:43

E esse é um erro comum de arquitetura, tá? Repara no título,

12:48

olha só, gente. MCP resource, URI mais função leitora, tá?

12:52

Essa é a ideia central. Um resource junta duas coisas,

12:56

uma URI e uma função que lê dados.

12:59

A palavra leitora importa. No código da esquerda temos dois exemplos,

13:03

ó. O primeiro é uma URI estática, pedidos barra lista.

13:08

Ou seja, ele representa uma fonte conhecida.

13:12

A função listar pedidos devolve os dados daquela lista.

13:16

E o segundo é uma URI parametrizada, pedidos barra pedido ID.

13:23

Aqui o placeholder da URI vira parâmetro da função. Ou seja,

13:27

pedido ID entra como pedido ID 2.str no Handler.

13:32

Aqui embaixo, está vendo?

13:34

Então, olha só, agora vem a distinção mais importante do slide,

13:37

resource versus tool.

13:41

Resource é leitura indepotente, tool é ação.

13:45

Indepotente aqui quer dizer repetir a leitura,

13:48

repetir a leitura não deve alterar o estado.

13:50

Eu leio o mesmo pedido duas vezes e eu não cancelei nada,

13:54

não aprovei nada, não disparei o workflow nenhum, vai ser o mesmo estado.

14:00

Então, se eu tenho algo como getUser, receber na ID,

14:04

isso apenas consulta dados, provavelmente é resource.

14:07

Agora, se eu tenho cancelar pedido, aí muda tudo.

14:10

Isso altera o estado, pode exigir autorização, auditoria,

14:15

confirmação e observabilidade. Isso é tudo.

14:17

Essa diferença não é só semântica, ela muda a experiência do usuário. Então,

14:22

uma leitura previsível pode aparecer como contexto,

14:25

uma ação normalmente precisa ser decidida, invocada e muitas vezes aprovada.

14:30

E aqui vale um cuidado. O slide, olha só, pessoal.

14:33

O slide aqui fala em pré-carregar resources.

14:36

A leitura prática é que o host pode expor

14:39

ou pré-carregar resources dependendo da implementação.

14:42

O ponto não é decorar comportamento de um host específico,

14:45

tá? O ponto é arquitetural.

14:47

Não transforme toda a leitura em decisão ativa do modelo, tá?

14:51

Então, guarda a regra do Code Review, pessoal. GetUserId tende a ser resource.

14:55

Cancelar UserId tende a ser tool. Leitura previsível vira resource.

14:59

Ação com efeito vira tool.

15:02

Aqui entra a terceira peça, que é o prompt. A primeira coisa a fixar é essa.

15:07

O que a gente precisa fixar é essa. Prompts viram menus no host.

15:11

Repara uma frase no topo. Não é o LLM que decide chamar, é o usuário.

15:16

Essa distinção é importante. Tool é capacidade operacional.

15:20

Prompt é a intenção guiada pelo usuário.

15:23

Agora, olha o código. A função recebe dois campos, pedido de profundidade.

15:28

E repare que o profundidade usa o literal,

15:32

básico ou detalhado. Isso cria uma experiência controlada.

15:36

O usuário não precisa lembrar o prompt certo,

15:38

nem copiar texto de algum lugar. Ele escolhe uma opção,

15:42

preenche os campos e dispara um fluxo padronizado.

15:45

O retorno da função monta a mensagem.

15:48

Investiga esse pedido,

15:49

use esse nível de profundidade e use as tuas disponíveis para buscar dados.

15:55

Então, o ponto aqui não é prompt grande.

15:57

O ponto é template operacional.

15:59

Essa template pode retornar um listing simples, como neste exemplo,

16:02

ou uma lista de messages,

16:04

quando você precisa de uma estrutura multi-run mais controlada.

16:07

Agora, do ponto de vista do tech lead, isso muda bastante a governança.

16:12

Porque prompt engineering deixa de ser algo solto,

16:15

que vive na cabeça de cada pessoa,

16:17

ou em um documento perdido. Ele vira artefato de plataforma.

16:20

Pode ser versionado, pode ser revisado, pode passar por code review.

16:23

E pode evoluir junto com o server. Guarda a diferença.

16:27

Tool expõe uma capacidade.

16:29

Resource expõe leitura.

16:32

Prompt expõe uma intenção guiada para o usuário executar melhor uma tarefa.

16:37

Então, isso aqui é o decorator MCP .prompt, pessoal.

16:41

Bem, agora a gente sai do retorno simples e entra em operação.

16:46

E o personagem central aqui desse slide é o context.

16:50

Até aqui, a tool parecia basicamente uma função que recebe input e devolve input.

16:55

Mas ato real e produção nem sempre é instantânea.

16:58

Às vezes ela processa em lote. E às vezes chama a API externa.

17:02

Às vezes demora. E quando demora,

17:04

ela precisa comunicar o que está acontecendo. Então, olha o código.

17:08

Async def processar_lote.

17:11

Ele recebe uma lista de IDs e recebe também um CTX, que é o context.

17:15

É tipado como context. Então, repare nesse detalhe.

17:19

O contexto entra como parâmetro explícito.

17:22

Não é estado global escondido. Isso ajuda na leitura,

17:26

teste e manutenção. Então, dentro do loop,

17:28

a primeira chamada importante é await context.info. Isso envia um log estruturado.

17:34

E aqui tem uma pegadinha operacional. Isso não é a mesma coisa que print,

17:39

tá? Em server stdio, usar print no stdout pode corromper o protocolo,

17:44

porque o stdout é o canal de comunicação com o host.

17:48

Esse é o tipo de bug que parece pequeno no código,

17:50

mas vira uma falha difícil de entender em execução.

17:53

Depois vem await context.report_progress,

17:57

que é o segundo método mais importante aqui.

18:00

Então, aqui a tool comunica o progresso.

18:04

Para uma chamada rápida, talvez isso seja irrelevante.

18:08

Mas para processamento de lote,

18:09

cada experiência do

18:10

usuário muda a experiência

18:16

do usuário e ajuda muito no diagnóstico.

18:19

Então, olha só.

18:23

A gente resumiu aqui os canais principais do context.

18:26

Info, warn e erro para logs estruturados.

18:29

Report progress para andamento.

18:31

E sample para pedir inferência ao host quando

18:34

a tool precisa desse tipo de interação.

18:36

Não precisa aprofundar tudo agora. O importante é guardar o papel do context.

18:40

Ele transforma uma chamada de tool em uma operação observável.

18:45

Bem, o que mais? Vamos lá.

18:52

Então, esse aqui, pessoal, é o momento que, na verdade, já foi para o recap,

18:57

eu vou dar pausa aqui para poder abrir a IDE e retornar aqui com vocês, tá bom?

## Resumo IA

[RESUMO_IA]