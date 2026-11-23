Módulo: Protocolos de Comunicação\
Aula: [Erros, Logs e Progress](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18603)

## Resumo da aula

POC tolera texto solto e ausência de feedback porque o fluxo ainda está sob controle manual. Em produção, isso falha rapidamente: o host precisa distinguir erro real de resposta válida, o operador precisa rastrear execução e o usuário precisa saber se uma tarefa longa continua viva. Erros, logs e progress formam essa camada de explicabilidade operacional. Um servidor MCP maduro não apenas executa; ele comunica estado, falha e andamento pela linguagem do próprio protocolo.

Os códigos JSON-RPC classificam a natureza da falha para que o consumidor reaja corretamente. -32700 indica parse error, normalmente próximo do transporte; -32600 indica invalid request, quando a estrutura da requisição não bate com o protocolo; -32601 indica method not found, como chamar uma tool inexistente; e -32603 fica reservado para erro interno inesperado. Essa classificação evita que toda falha vire texto ambíguo ou exceção genérica sem semântica operacional.

-32602 (invalid params) é o código mais frequente no dia a dia porque a maior parte das falhas previsíveis nasce no input. Retomando a validação na borda já conhecida, ID menor ou igual a zero, campo ausente, enum fora do domínio e data malformada devem ser tratados como parâmetro inválido, não como erro interno. A consequência prática é simples: o host entende que a chamada falhou por contrato de entrada e pode interromper ou corrigir o fluxo sem mascarar o problema como instabilidade do servidor.

Em FastMCP, falha esperada não deve voltar como string do tipo “ID inválido”. Ela deve ser levantada como MCPError, acompanhada de ErrorData, para que o SDK converta isso em erro JSON-RPC formal. Esse desenho preserva a semântica do protocolo e transforma uma condição previsível em contrato consumível por host, automação e observabilidade. O campo data adiciona contexto útil, mas não deve carregar PII, senha, token ou credencial.

Retomando uma tool já conhecida, como a busca de pedido, a camada nova não está na regra de negócio, mas em como ela falha. Se order_id <= 0, a execução deve parar imediatamente com MCPError usando -32602, porque a causa está no parâmetro e não na infraestrutura. Em revisão de código, três perguntas bastam: o código corresponde à causa, a mensagem ajuda o diagnóstico e o contexto adicional informa sem expor dado sensível.

Log em MCP não é print no terminal; é capability declarada e mensagem de protocolo. O servidor anuncia suporte a log, o host pode ajustar o nível com log/setLevel, e a emissão acontece por notifications/message. Isso permite que o host receba, ordene e apresente eventos com contexto, em vez de depender de texto livre misturado ao canal de transporte.

Os níveis debug, info, notice, warning, error, critical, alert e emergency expressam severidade operacional, não preferência estética. debug ajuda investigação detalhada, info registra comportamento esperado, warning sinaliza condição anômala ainda recuperável e error representa falha efetiva; os níveis acima disso ficam para incidentes críticos. Usar a severidade correta melhora triagem, roteamento e leitura do estado do sistema por operadores e hosts.

O payload de log precisa separar severidade, origem e contexto. Campos como level, logger e data tornam a mensagem pesquisável e correlacionável, permitindo filtrar por request_id, latency_ms, host ou categoria de erro sem depender de parsing de string concatenada. A disciplina importante aqui é manter chaves consistentes ao longo do servidor e nunca registrar PII ou segredos.

O Context, já conhecido no FastMCP, ganha aqui seu papel operacional completo: ele é o canal oficial para logs estruturados e progress. Em vez de criar logging paralelo, a tool usa ctx.info, ctx.warn e, quando necessário, log de erro com extra estruturado. Isso permite reconstruir a linha do tempo de uma execução — por exemplo, início, condição anômala e falha — usando o mesmo identificador de correlação do domínio, como order_id.

Progress não é emitido automaticamente para toda requisição longa. O cliente precisa pedir acompanhamento enviando um progress token em _meta, e esse token funciona como identificador de correlação entre a chamada original e as futuras notifications/progress. O contrato é opcional porque nem toda operação precisa disso, mas, quando a execução pode durar vários segundos, omitir progress aumenta a incerteza do usuário e favorece cancelamentos desnecessários.

O progress token não representa percentual, lote ou etapa; ele apenas liga cada atualização à execução correta. A notificação de progresso reutiliza esse token para que o host saiba a qual chamada aquele update pertence, mesmo em cenários concorrentes. Essa simetria entre request e notification é o que torna o acompanhamento confiável em ambiente distribuído.

Em FastMCP, a emissão prática acontece com ctx.report_progress, sem necessidade de montar manualmente a notificação de protocolo. Retomando uma operação como processar_lote, o servidor informa progress, opcionalmente total, e uma message humana como “item 3 de 10”; quando o total é desconhecido, esse campo pode ser omitido. O requisito operacional é manter avanço monotonicamente crescente, porque isso sinaliza ao host que o trabalho continua vivo.

A diferença entre POC e produção aparece quando o sistema precisa ser operado por terceiros, não apenas executado pelo autor. Em POC, texto livre e silêncio podem parecer suficientes; em produção, isso vira custo de suporte, diagnóstico ruim e experiência frágil para o usuário. Por isso, no laboratório de construção do servidor do zero, MCPError, logs estruturados e report_progress devem entrar nas tools como parte do contrato desde o início, não como acabamento posterior.

## Transcrição

00:01

Pessoal, vamos para a próxima aula. Então,

00:06

essa aula é sobre três coisas que caminham juntas,

00:10

que são erros, logs e progress.

00:14

De primeira vista, pode parecer uma aula sobre detalhes,

00:17

coisas que a gente adiciona depois que o server já está funcionando,

00:22

mas guarde essa ideia desde o começo.

00:25

Em produção, erro, log e progresso... Não são acabamento.

00:29

Eles fazem parte do contrato do sistema. Então, o recorte da aula é este.

00:34

Reportar falhas e acompanhar tarefas longas dentro da especificação.

00:39

Repare nessa última parte, dentro da especificação.

00:42

A aula não é sobre inventar um jeito próprio

00:44

de registrar logs ou de mostrar progresso.

00:47

É sobre usar aquilo que o MCP já define como linguagem comum entre server, host e usuário. Então...

00:55

A gente vai entrar nessa aula com esse modelo mental.

00:58

A gente não está decorando uma API.

01:01

A gente está aprendendo a tornar o server explicável. Então vamos lá.

01:08

Primeiro, por que se importa? A gente começa pela diferença entre POC e produção,

01:12

porque muita solução que parece suficiente em uma demonstração começa

01:16

a falhar quando o sistema precisa ser operado,

01:19

observado e mantido.

01:20

Segundo, erros chipados. com códigos padrões do JSON RPC,

01:25

inclusive coisas que a gente já viu lá atrás,

01:27

mas a gente vai recapitular alguns deles aqui.

01:32

Terceiro, logs estruturados,

01:33

com MFC 5424 e notifications barra messages.

01:40

Aqui o foco é sair do print solto e entrar

01:43

em uma comunicação que o host consegue receber,

01:46

ordenar e apresentar com contexto.

01:50

Quarto, a gente vai falar de progress,

01:52

com progress stock e notifications barra progress.

01:54

Quando uma tarefa demora,

01:57

o usuário precisa saber se ela ainda está trabalhando ou se travou.

02:00

Então, pense nessa aula como um mapa.

02:04

Erros, logs e progressos não são acessórios.

02:07

Eles fazem parte do comportamento esperado de um server MCP em produção. Então, vamos lá.

02:13

Bem, agora a gente entra nesse primeiro slide, que é o porquê que isso importa.

02:19

Então, a constatação de partida é simples. Em uma POC,

02:22

você devolve uma string dizendo erro X e ninguém reclama.

02:27

Testando localmente, com poucos inputs e pouca integração,

02:30

isso até que parece suficiente.

02:32

O problema é que essa solução não escala quando entra um roxo real,

02:37

usuário real, tarefa demorada e falha intermitente.

02:40

Então, repara só, pessoal. O primeiro é erro silencioso.

02:45

O primeiro dos pontos aqui é erro silencioso.

02:48

O server devolve texto em vez de um erro tipado.

02:51

O host não entende bem que falhou. Ou seja, o modelo pode,

02:58

inclusive, tentar continuar repetindo a chamada.

03:00

E o usuário não recebe um sinal confiável.

03:03

A questão não é estética, é semântica.

03:06

O próximo ponto é falta de observabilidade.

03:09

Sem logs estruturados, debugar vira arqueologia.

03:13

E você procura string no terminal, tenta lembrar o horário,

03:17

cruza a execução manualmente e fica refém de print.

03:21

O terceiro ponto aqui, pessoal, é tarefa longa sem feedback.

03:27

Talvez o server esteja funcionando, mas para o usuário o silêncio parece travamento.

03:31

Depois de 30 segundos sem sinal, muita gente até cancela.

03:35

Então, a tese por trás disso aqui é o seguinte, pessoal,

03:38

o MCP não trata isso como detalhe.

03:40

Ele oferece contratos para erro logo em progresso.

03:43

Então, em produção, não basta o server responder.

03:46

Ele precisa falhar de forma interpretável,

03:48

registrar o que aconteceu e mostrar andamento quando a operação demora.

03:53

E o principal contrato que a gente vai olhar é justamente o de erro.

03:56

Como classificar uma falha usando os códigos padrões do JSON RPC

03:59

que a gente até já viu lá atrás alguns deles.

04:03

Então, o jeito mais útil de ler este slide,

04:05

pessoal, é com uma tabela de diagnóstico.

04:07

Cada código diz ao host que tipo de problema aconteceu.

04:12

Quando é retipado, o consumidor consegue reagir melhor.

04:16

Pode exibir uma mensagem adequada, decidir se tenta de novo,

04:20

ou interromper a execução com um sinal mais claro.

04:23

O código "-32700", é o parse error, JSON mal formado. Em geral...

04:30

Fica mais perto da camada do transporte, de transporte e de parsing, ou parsing.

04:36

Normalmente o SDK já trata isso automaticamente.

04:39

O código -32600 é o invalid request.

04:43

A request chegou, mas não está no formato esperado.

04:46

Pode faltar campo obrigatório ou a estrutura pode não bater com o protocolo.

04:50

O código -32601 é o method not found.

04:56

Method not found. Um exemplo típico é chamar uma tool ou um resource que não existe.

05:01

Ou usar um nome que já foi registrado, que não foi registrado.

05:05

Então, agora, repare no destaque, pessoal.

05:08

-32602. Invalid params. Gente, esse é o erro que você vai mais usar.

05:14

No caso, mais vai encontrar.

05:17

No dia a dia de uma tool, no dia a dia de uma tool... é muita falha previsível,

05:23

é input inválido. id menor ou igual a zero,

05:26

campo ausente, enum fora do conjunto permitido,

05:30

ou data e formato errado. Isso no final, inclusive, pessoal,

05:33

a gente já viu nos nossos exercícios que a gente mesmo gera esse erro.

05:37

O próprio Zod no TypeScript,

05:39

ou o Pydantic, esse erro é...

05:47

Ele é gerado pelo próprio... O próprio MCP,

05:51

ele dispara esse erro, tá? O último é o "-32603",

05:56

que é um erro interno para erro inesperado,

05:59

né? Agora, esses vamos usar com cautela.

06:01

Se tudo virar erro interno, você perde o diagnóstico.

06:05

E o campo data serve para contexto adicional,

06:09

mas não coloque ali PII, tá, gente? Senha, toque, credencial, né? Guarde...

06:15

Então, a gente tem que guardar muito bem isso na cabeça.

06:18

O código classifica, a mensagem explica e o data contextualiza.

06:23

Então, vamos... Agora a gente vai...

06:26

A gente sai da tabela e vê como isso aparece no Flash MCP.

06:31

A ideia central é essa, pessoal.

06:33

Em Flash MCP, você levanta o MCP error com o error data.

06:37

E o SDK sinaliza isso para o host como uma JSON RPC error.

06:43

Uma JSON RPC error responde automaticamente. Isso muda o jeito de escrever código.

06:49

Você não retorna uma string dizendo ID inválido.

06:52

Você levanta um erro que preserva a semântica de protocolo.

06:55

Em produção, essa diferença pesa.

06:58

Porque o host deixa de receber texto solto e passa a receber uma falha.

07:03

E uma

07:07

falha classificável ainda por cima.

07:11

Para esses impostos, pessoal, a gente traz o MCP error e também o invalid params,

07:16

junto com o error data.

07:19

Isso conecta diretamente com o site anterior.

07:22

O invalid params é a forma prática de usar o código "-32602". Agora,

07:27

olha a função buscar pedido. Ele recebe um ID inteiro.

07:31

Se o ID é menor ou igual a zero,

07:33

a tool não deve seguir adiante e também não deve lançar uma exception genérica.

07:37

O problema não é interno do server, é parâmetro inválido.

07:41

Então, a linha principal, RAISE MCP ERROR,

07:44

passando um error data com código de mensagem. Então, olha só.

07:51

Então, vê a linha, pessoal.

07:53

RAISE MCP ERROR, passando um error data com código de mensagem.

07:57

O erro previsível vira contrato e não improviso.

08:02

Então, vamos lá. Em um code review, por exemplo,

08:05

eu olharia três coisas. O código bate com a causa.

08:08

A mensagem ajuda a entender o problema?

08:10

Existe contexto suficiente sem vazar dados sensíveis?

08:13

A mensagem do exemplo está em português para facilitar a aula,

08:16

mas em sistemas reais eu tenderia para analisar mensagens operacionais

08:20

em inglês e em formato mais machine-friendly.

08:24

Então, guarda a ideia principal.

08:26

Quando a falha é esperada, você não trata como surpresa.

08:29

Você classifica, comunica e deixa o protocolo carregar esse significado.

08:34

Depois de classificar as falhas,

08:36

o próximo passo é registrar o que aconteceu durante

08:38

a execução e aí que entra os logs,

08:40

tá? Vamos para os logs então, pessoal. Bem,

08:46

agora aqui vale separar duas coisas, tá? Protocolos e níveis, tá?

08:52

Do lado do protocolo, o server declara a capability log.

08:56

Depois, o nível pode ser ajustado via log / set

09:00

level e a emissão acontece por notifications / message.

09:04

Repara na mudança de modelo mental. Não é mais print espalhado no terminal.

09:08

O log vira mensagem estruturada de protocolo.

09:11

O host consegue receber, ordenar e exibir isso com contexto.

09:15

Agora, olha para os níveis.

09:18

Debug, info, notice, warning, error, critical, alert e emergency.

09:24

A ideia não é decorar todos. O importante é entender a intenção operacional.

09:30

Debug ajuda no diagnóstico. Info registra o evento esperado.

09:35

O warning indica algo estranho. Erro representa a fábrica.

09:39

E os níveis mais altos ficam para situações críticas.

09:42

Tanto que no payload do slide, os campos principais são level, log e data.

09:47

O level informa a severidade. O log indica a origem.

09:51

E o data carrega contexto estruturado em JSON.

09:55

Isso é importante, pessoal,

09:57

porque você deixa de depender de string concatenada

10:00

e passa a ter campos pesquisáveis,

10:02

como erro, host, port, latest, barra, ms, ou request ID, por exemplo.

10:10

Dois cuidados essenciais aqui, tá?

10:12

Manter consistência nas chaves e nunca logar sem a Tokyo PIA.

10:16

Eu não canso de reforçar isso, tá, pessoal?

10:18

Então, vamos lá. Log estruturado não é detalhe de implementação,

10:22

é parte do contrato operacional do server, tá?

10:27

Bem, agora vamos para o próximo slide, pessoal,

10:30

que agora a gente vê o login no SDK,

10:35

tá? A ideia central,

10:37

pessoal, que é simples, tá? Em FastMCP, o context, tá?

10:41

O objeto context é o canal de logs estruturados.

10:44

Aí você não precisa inventar um log paralelo.

10:47

Fazer print ou escrever um arquivo local só para acompanhar a execução.

10:52

Ela usa o CTX, que é o context. E esse,

10:59

que é do tipo context. Então,

11:02

esse CTX é o canal de comunicação com o ambiente MCP enquanto a tua está rodando.

11:07

Bem, a primeira chamada é o context.info.

11:11

Uma mensagem curta, iniciando, uma mensagem curta, iniciando e um extra.

11:18

Com order ID, por exemplo, no nosso caso.

11:21

Esse é o padrão desejado. Mensagem curta e contexto estruturado separado.

11:27

Depois, aparece um context.warn. Olha só.

11:32

O warn não é necessariamente erro fatal. Pode ser uma condição recuperável.

11:37

Algo que merece atenção, mas talvez não interrompa a execução.

11:41

Bem, em seguida vem o try, o processamento e o accept. Então, olha só.

11:49

O exemplo para aí, mas a intenção é clara.

11:52

Uma falha inesperada deveria virar log de

11:54

erro com contexto suficiente para investigação.

11:57

Em produção, pessoal, eu procuraria a linha do tempo.

12:03

Começou com if, apareceu on e depois falhou.

12:07

Com o mesmo order ID, dá para seguir a execução inteira.

12:10

O ponto principal não é logar muito, é logar conforme.

12:14

Então, use o CTX ou Contax, do tipo Contax, como canal operacional da Tu.

12:19

E coloque no extra tudo o que ajuda a rastrear a execução sem vazar dados sensíveis.

12:24

Gente, isso aqui é o que diferencia o nível de maturidade

12:28

que você tem na hora que está desenvolvendo o MCP em produção. Vamos lá.

12:35

Bem, o terceiro contrato é o Progress.

12:39

Então, a primeira palavra importante aqui é que é opcional, tá, pessoal?

12:42

O MCP define um fluxo opcional de progresso para tarefas longas.

12:47

Isso significa que progress não acontece automaticamente para toda request.

12:52

O cliente precisa pedir updates,

12:55

passando um progress token no underscore meta da request original,

12:59

tá? Então, olha só. Olha primeiro o próprio request.

13:05

Ele continua sendo uma chamada normal de tool. JSON RPC 2.0,

13:09

um ID, método tools barra call, nome de tool e argumentos.

13:15

O exemplo é processar lote, uma operação que pode envolver vários itens.

13:19

I .O., chamadas externas ou processamento incremental.

13:23

Em produção, esse tipo de tarefa raramente termina instantaneamente. Agora,

13:27

repare no underscore meta, pessoal. É ali que aparece o progress token.

13:37

E esse token não representa percentual nem quantidade processada.

13:43

Ele é o identificador de correlação.

13:45

Serve para o server dizer depois. Esse update pertence àquela execução.

13:50

Do outro lado, pessoal, vem a notification de progress.

13:54

O método muda para notification barra progress, mas o progress token continua igual.

14:00

Isso é simetria do contrato.

14:02

O cliente pede acompanhamento usando o token e o

14:06

server devolve atualizações associadas ao mesmo token.

14:09

Em progress, o usuário vê apenas o carregando.

14:12

É silêncio e em sistema distribuído parece travamento.

14:19

Com progress, o roxo consegue mostrar movimento,

14:23

barra, texto, etapa atual, número de itens. A representação visual depende do roxo,

14:29

mas o mecanismo nasce aqui. Então, guarde isso aqui,

14:32

pessoal. Progress não acelera a tarefa. Progress reduz a incerteza. Agora,

14:37

vamos ver como é que isso é implementado no FastMCP.

14:41

Bem, a ideia principal é que em FastMCP,

14:45

você não precisa gerenciar manualmente o protocolo de Progress.

14:48

Você chama ctx .reportProgress, passando o avanço atual e opcionalmente o total.

14:55

O SDK cuida do restante. Então, olha o exemplo, pessoal.

14:58

A função processar lote recebe uma lista de IDs e um CTX.

15:02

Primeiro, e que é o context, né? Primeiro,

15:04

ela calcula o total com o tamanho da lista.

15:06

Depois, entra em um for com enumerate, começando com 1.

15:11

Este start igual a 1 parece pequeno, mas melhora a mensagem humana,

15:16

tá? Porque item 1 de 10 é natural para o usuário.

15:20

Contagem começando em zero funciona melhor para a máquina do que para nerds,

15:24

tipo eu no caso, do que para a interface. Brincadeira.

15:28

Dentro do loop, a tool processa um item e chama context .reportProgress.

15:34

Os campos principais são, são três no caso, progress,

15:38

que representa o avanço atual, total, que representa o avanço conhecido,

15:42

e method, que adiciona contexto humano, como item 3 de 10.

15:47

Quando o total é desconhecido, Você simplesmente omite o total.

15:51

Isso acontece em streams,

15:53

paginação de API ou filas sem tamanho definido.

15:56

O importante é que o progress continue monotonicamente crescente,

16:02

ou seja, sempre avançando. Assim o host entende que o trabalho continua vivo.

16:06

Em host real, pessoal, como por exemplo um cloud desktop,

16:10

isso pode aparecer como byte progress. Sem progress,

16:13

o usuário vê apenas um carregando e começa a assumir travamento.

16:16

Agora, em code review a pergunta é direta.

16:19

Essa execução pode passar de alguns segundos?

16:22

Se sim, onde está o report barra progress? Bem,

16:28

progress não serve só para mostrar a perceptual, pessoal.

16:32

Serve para reduzir incerteza durante operações longas.

16:38

Então, vamos lá, pessoal. A tese central foi esta.

16:42

Sair da POC para a produção exige disciplina nos contratos da especificação MCP.

16:47

E essa aula, isso apareceu em três frentes.

16:52

Erros chipados, logs estruturais, notificações de progresso.

16:55

O ponto importante é que nada disso é acessório.

16:58

E produção atua não precisa só funcionar.

17:01

Ela precisa comunicar corretamente quando falha,

17:03

quando demora e quando está saudável.

17:06

Se você leva... O que você pode levar...

17:10

O que você leva daqui se organiza em três coisas.

17:13

Primeiro, conceito central.

17:15

Erros chipados e logs via contexto como parte do contrato do server.

17:20

Segundo, as armadilhas.

17:23

No Code Review, os antepassos que a gente vê nos Code Reviews,

17:29

que parecem pequenos, mas normalmente viram custo operacional depois.

17:32

E terceiro, pessoal, olha só.

17:35

Vocabulário de tech lead. SLA, severidade, observabilidade,

17:38

progress talk. Porque sem linguagem comum, discussão operacional vira opinião.

17:45

Logs e erros não são acessórios. São contratos de confiança com o cliente. Beleza?

17:51

Agora a gente vai pro lado, pessoal. Falou!

## Resumo IA

[RESUMO_IA]