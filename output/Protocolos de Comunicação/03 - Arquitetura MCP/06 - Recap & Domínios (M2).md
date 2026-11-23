Módulo: Protocolos de Comunicação\
Aula: [Recap & Domínios (M2)](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18597)

## Resumo da aula

Host, client e server continuam formando a separação central do MCP, mas aqui o ponto decisivo é operacional: governança fica no host, sessão protocolar fica no client e execução de domínio fica no server. Essa divisão não serve apenas para organizar código; ela determina onde permissões, timeouts, falhas e observabilidade devem ser tratados. Quando autorização escapa do host ou quando o client passa a carregar lógica que não é dele, a arquitetura perde governança e o debug fica ambíguo.

Retomando a distinção já estabelecida entre leitura e ação, a decisão correta depende da natureza da capacidade exposta. Tool representa ação com efeito colateral e, por isso, exige schema claro, argumentos tipados e retorno estruturado; resource representa leitura estável e não deve alterar estado; prompt permanece como template parametrizado disparado pelo usuário. Misturar essas fronteiras degrada a UX do agente, porque ele passa a escolher mecanismos errados para obter contexto ou executar ações.

Sampling é o caso em que o server interrompe sua execução para pedir inferência ao host, usando o modelo já governado por ele. A diferença para uma tool comum não é sintática, mas arquitetural: o server não incorpora vendor, credenciais, budget nem política de uso de modelo. Esse desenho preserva centralização de custo, contexto e governança, mas só faz sentido quando existe uma barreira semântica real que código determinístico não resolve bem.

A conexão MCP começa com initialize, que funciona como handshake entre client e server. Nessa troca, cada lado declara versão suportada e capabilities disponíveis, e capability ausente deve ser lida como funcionalidade desabilitada, não como omissão tolerável. O fechamento dessa fase ocorre com notifications/initialized, uma notification JSON-RPC sem ID, sinalizando que a sessão pode entrar em operação normal.

No MCP, ausência de capability não é detalhe cosmético nem valor default implícito. Se uma capability não foi anunciada, o outro lado deve assumir que aquela superfície não existe e ajustar o comportamento sem tentar adivinhar suporte parcial. Essa regra reduz ambiguidade de integração e evita bugs em que host ou client chamam fluxos que o server nunca declarou suportar.

Depois do handshake, a sessão entra na fase operacional, onde circulam chamadas como tools/call, resources/read e prompts/get, além de mensagens auxiliares de progresso e cancelamento. progress existe para dar visibilidade a operações longas, permitindo que host e usuário acompanhem execução sem tratar silêncio como travamento. cancellation existe para interromper trabalho que perdeu utilidade, expirou por timeout ou foi abandonado pelo usuário, evitando consumo inútil de CPU, rede e recursos externos.

Request sem timeout em integração distribuída é um incidente em potencial, porque rede oscila, dependências degradam e processos congelam. O client precisa impor prazo máximo e, quando esse prazo expira, emitir cancelamento e encerrar a operação de forma controlada. Sem isso, o sistema acumula conexões penduradas, recursos presos e estados difíceis de diagnosticar.

O shutdown do MCP não acontece por uma mensagem de protocolo equivalente a exit; ele depende do transporte usado pela sessão. Em stdio, o client encerra o processo fechando STDIN e, se necessário, escala para sinais como SIGTERM e SIGKILL; em HTTP streaming, o encerramento ocorre pelo fechamento da conexão. Essa diferença importa porque shutdown graceful, limpeza de recursos e tratamento de travamentos precisam ser implementados na camada de transporte, não esperados do protocolo.

Ler o MCP on wire significa observar a sequência real de mensagens JSON-RPC trocadas entre client e server, em vez de inferir comportamento apenas pelo código da aplicação. Retomando o uso do Inspector já conhecido, a trilha de initialize, negociação de capabilities, notifications/initialized, chamadas, progress, cancellation e encerramento permite reconstruir a sessão com precisão. Essa observabilidade transforma debugging de opinião em debugging por evidência.

O Inspector continua sendo a ferramenta neutra para validar contrato, transporte e sequência protocolar antes de culpar host ou modelo. No cenário com múltiplos servers já visto anteriormente, ele ajuda a confirmar que a orquestração depende de contratos e sessão corretos, não de glue code artesanal entre domínios. A próxima etapa natural é implementar servers com SDKs, mas já com critérios claros de handshake, capabilities, timeout, progress, cancellation e shutdown.

## Transcrição

00:02

Oi pessoal, tudo bem? Vamos lá, vamos para mais um recap e domínios, tá bom?

00:09

Só para relembrar, são quatro perguntas,

00:11

eu leio e você responde mentalmente, em silêncio, né?

00:13

E depois eu respondo em voz alta, né?

00:16

Se a sua resposta bateu com a minha, anota mentalmente aí que,

00:20

putz, dominou esse assunto, tá? Se não bateu,

00:23

anota no caderno o número da pergunta, né?

00:26

E o nome dele na hora original, né?

00:28

Porque o slide vai te dizer exatamente para onde voltar.

00:31

Sem julgamento, né? Recap é diagnóstico, tá, pessoal? Não prova, tá? Beleza? Então, vamos lá.

00:38

A pergunta é, o que fazem host, client e server?

00:45

Nesse momento, pessoal, você dá uma pausa aí, tá? No seu vídeo, tá bom?

00:50

Já já eu volto para poder responder.

00:55

Bem, a

00:57

resposta vem em três papéis, né? Host é governança, é a aplicação onde o LLM vive.

01:02

Mantém o contexto da conversa, gerencia permissões e decide qual modelo usar.

01:07

Por exemplo, o Cloud Desktop,

01:09

o Cursor, o VSCode, o IntelliJ, enfim,

01:13

todos exercem esse papel. E repara no ponto importante,

01:16

autorização pertence ao host.

01:18

É ele que decide se uma tool pode ou não ser executada.

01:22

O client é a diplomacia, ele fica dentro do host.

01:26

E existe um client para cada server conectado.

01:29

Ele cuida da conversa protocolar, tá? O handshake com o MCP,

01:33

conformidade JSON-RPC e ciclo de vida do transporte.

01:37

Pensa como uma sessão dedicada, tá?

01:39

Isso ajuda a isolar o estado, né, conexão e falha de cada server.

01:45

Quando alguma integração quebra em produção,

01:47

essa separação faz a diferença no debug.

01:49

E agora o server propriamente dito.

01:51

O server é a execução. É um processo separado, tá? Sem LLM dentro, tipicamente.

01:56

Eles põem tools, resources e prompts ao host via o protocolo.

02:00

É onde normalmente mora a lógica de negócio e integração externa,

02:04

tá? Então, vamos lá. Host governa, client traduz e server executa.

02:09

E esse detalhe importa mais do que parece, tá?

02:12

Se alguém propõe colocar lógica de autorização no client, por exemplo,

02:16

você já consegue perceber o problema arquitetural, tá? Ou seja,

02:19

o client conduz sessão. Governança pertence ao host, tá bom?

02:24

Vamos para a próxima, pessoal.

02:30

Leia a pergunta, já já eu volto.

02:36

Bem, como escolher entre True, Tool, Resource ou Prompt? E aí?

02:43

Bem, a resposta é simples, pessoal.

02:47

Pergunta, qual é o domínio da coisa? Tool é ação com efeito, ou seja, criar eixo,

02:53

enviar e-mail, iniciar serviço, executar query mutativa, enfim.

02:58

Existe efeito colateral, alguma coisa muda no sistema.

03:02

E repara em outro detalhe importante.

03:04

Tu precisa de contrato claro, argumentos tipados,

03:08

retorno estruturado, esquema bem definido.

03:10

Tu sem esquema normalmente vira debugging por tentativa e erro.

03:15

Agora, resource é dado indepotente. Ou seja, um arquivo,

03:20

Esquema de tabela, configuração, histórico do cliente.

03:23

A leitura não altera o estado. Você consulta,

03:26

injeta contexto, referencia via URI estável, mas não execução.

03:31

E aqui existe uma pegadinha comum.

03:33

Quando alguém coloca efeito colateral dentro de resource, porque fica mais fácil.

03:38

Então vamos lá.

03:39

Isso quebra a expectativa do host e confunde o modelo mental do agente.

03:44

Bem, e prompt é template controlado pelo usuário.

03:49

É uma sugestão pronta, parametrizada,

03:51

normalmente exposta como menu ou slash command do host. Quem dispara é o humano,

03:57

não o LLM automaticamente. Então guarda essa regra. Leitura é resource, ação é tool,

04:03

template do usuário é prompt. E parece detalhe de modelagem, mas não é.

04:08

Quando essas fronteiras ficam borradas, o agente começa a tomar a decisão errada.

04:13

Contexto errado entra no fluxo e a UX degrada rápido. Isso não é problema estético,

04:20

é problema de arquitetura do agente. Então, para você como um tech lead,

04:24

vale transformar essa regra em padrão de revisão do time.

04:28

Tu se esquima é tu cega,

04:30

resource com efeito é resource mentirosa e prompt

04:33

com lógica demais vira tu disfarçada, tá bom?

04:36

Vamos para a próxima? Deu uma lidinha aí na pergunta.

04:46

Então vamos lá. A pergunta 3 é,

04:49

o que é sampling e por que ele é diferente? Bem, a

04:55

resposta é fluxo inverso. O fluxo normal do MCP é host apontando ou...

05:01

para o servidor. O LLM do Roche decide chamar uma API.

05:06

O servidor executa e devolve o resultado.

05:09

Sempre inverte isso. Agora é o servidor que pede inferência ao Roche.

05:13

Ou seja, no meio da execução,

05:15

a API percebe que precisa de inteligência de linguagem natural.

05:18

Pede ajuda ao LLM do Roche. Recebe a resposta e depois continua.

05:23

Olha um caso típico.

05:25

A API recebe o endereço incompleto de uma API externa. Falta o bairro.

05:29

Em vez de criar heurística frágil, cheia de infiel,

05:33

ela pede ao LLM um julgamento curto.

05:35

Qual é o bairro mais provável dado esse contexto?

05:38

E repara na vantagem arquitetural aqui. O servidor não embarca em LLM próprio.

05:43

Não escolhe vendor, não guarda chave de API,

05:46

não controla budget e nem paga inferência. Quem decide tudo é o host.

05:51

Servidor pede e host governa. Isso é importante porque governança de modelo,

05:57

custo e dado continuam centralizados, onde já existe contexto e controle.

06:02

Agora, cuidado com uma armadilha comum.

06:05

Simple é poderoso, mas caro. Se o infiel resolve,

06:11

use infiel. Então, se é hot path de latência,

06:15

pense duas vezes antes de adicionar inferência no meio da execução.

06:18

E se o dado é sensível,

06:19

talvez ele nunca devesse sair do servidor para o LLM. Então,

06:23

guarda essa ideia. Sempre não é tool call em reverso.

06:27

É o servidor usando a LLM do host sem precisar carregar o modelo próprio.

06:34

Vamos para a quarta pergunta. Dá uma olhadinha aí.

06:37

Pensa na resposta que já já eu volto.

06:46

Bem, quais são as fases da conexão MCP? Essa é um pouco mais difícil.

06:53

A primeira é o initialize, é o handshake. O cliente abre a conversa dizendo...

06:59

Qual versão do protocolo suporta e quais capabilities possui?

07:03

O server responde declarando o que consegue oferecer.

07:06

E aqui tem um detalhe importante.

07:08

Capability ausente significa feature desligada. Ou seja, nada implícito.

07:14

O handshake termina quando o

07:18

cliente envia uma notification / initialize.

07:21

Lembra do... do JSON-RPC,

07:25

nesse caso da notification, ele vai mandar uma mensagem sem ID com essa informação,

07:30

só de curiosidade. Depois vem a operação.

07:33

Aqui entra o tráfego normal. Tools / call,

07:36

resources / read ou prompts / get. Progress, cancellation e tudo mais.

07:41

De novo, tudo é JSON-RPC 2.0 nos dois sentidos.

07:47

E existe uma regra operacional crítica aqui.

07:49

Request sem timeout vira incidente esperando acontecer.

07:53

Integração distribuída trava. Rede oscila.

07:56

Processo congela. Dependência externa degrada.

08:00

Então o cliente precisa controlar timeout e cancelar a operação quando expira.

08:05

Senão você acumula recurso preso e conexão pendurada.

08:08

E a terceira fase é o shutdown. Essa é a pegadinha clássica.

08:13

Não existe mensagem MCP de exit. O encerramento acontece via transporte.

08:18

No STDIO, o client fecha o STDIN do processo. Se travar, SIGTERM,

08:25

depois SIGKILL. No streamable HTTP,

08:30

fecha HTTP ou o server sent event.

08:33

Bem, mas enfim. Então, guarda esta frase.

08:38

Shutdown é responsabilidade do transporte,

08:41

não do protocolo. Isso muda bastante quando você começa a construir server custom.

08:46

Shutdown graceful. Timeout absoluto e cancellation não são refinamento.

08:51

São o que separa demo funcionando de sistema operacional em produção.

08:58

Legal. Então, quatro perguntas feitas. Se a maior delas bateu,

09:03

esse módulo cumpriu o papel dele. O domínio aqui tem um nome,

09:06

gestão de contexto e primitivos.

09:08

E isso significa cinco capacidades práticas. Primeira.

09:14

Você diferencia tool, resources e prompt em decisão real de design.

09:19

Leitura vira resource, ação vira tool, template controlada pelo usuário vira prompt.

09:26

Essa regra parece simples, mas evita muita arquitetura confusa.

09:31

Segunda, você entende o triângulo host, client e server.

09:34

Host governa, client traduz e server executa.

09:39

E você consegue nomear esses papéis em ambientes como cloud code, cursor,

09:44

ou no host custom, tá? Vocês vão reparar que isso é bem óbvio.

09:50

Terceira, você lê o handshake MCP no fio, tá? On wire, lembra disso?

09:56

Initialize capability negotiation notifications / initialize.

10:00

Vai estar tudo no fio.

10:02

E sabe a pegadinha? Shutdown é via transporte, não via mensagem MCP.

10:08

Quarta, você usa o MCP Spectre como ferramenta neutra do debug.

10:13

Na prática, ele ajuda o time a enxergar o protocolo acontecendo,

10:16

em vez de discutir no escuro. Isso reduz muito o ruído quando a integração quebra.

10:23

Quinta, você entende a consequência arquitetural do MCP.

10:27

Múltiplos servers podem ser orquestrados sem escrever

10:30

glue code para cada combinação.

10:33

O protocolo absorve boa parte da carga que antes virava manutenção espalhada.

10:39

Então, esse slide não é só um resumo, é um checkpoint.

10:45

Antes de entrar em código, você já sabe onde cada responsabilidade mora,

10:50

como a conexão nasce, como opera e como termina.

10:54

Agora sim, no próximo módulo, a gente entra em desenvolvimento MCP.

10:58

Então, aqui é ali que o código começa.

11:05

O próximo módulo é o desenvolvimento MCP, pessoal.

11:07

Então, até aqui a gente entendeu arquitetura,

11:10

né? Papéis, primitivas, simples, ciclo de vida de conexão.

11:13

Agora a pergunta muda, né?

11:15

Não é mais só como o MCP se organiza. É como eu construo um server MCP de verdade,

11:21

tá? Então, a primeira etapa vai ser no SDK oficial e TypeScript, tá?

11:27

A ideia é mostrar como subir um server com tipagem,

11:30

Zod e uma estrutura familiar para quem já trabalha com o sistema on-road.

11:35

Depois vem o SDK mais popular, que é o InPython. E a gente vai usar o FastMCP.

11:41

Aqui o foco é a ergonomia. Decorators como mcp.tool, mcp.resource,

11:47

mcp.prompt, esquema inferido por type hints e prototipagem mais rápida.

11:53

Em seguida, a gente entra no que separa POC de produção,

11:56

que são os erros, logs e progress.

11:59

Porque server que só funciona no caminho feliz não aguenta operação real.

12:03

Você precisa de erro tipado,

12:05

log estruturado e visibilidade de progresso em tools longas, inclusive.

12:10

Depois vem o laboratório. Aí você constrói um server custom do zero,

12:14

pluga no Cloud Code e vê o fluxo rodando de ponta a ponta.

12:18

E por fim, fechamos de novo no recap dos domínios. Então,

12:22

guarda a transição. Nesse módulo, você aprendeu a ler arquitetura.

12:26

No próximo, você começa a escrever essa arquitetura em código.

12:32

Com isso, a gente fecha o segundo módulo do curso.

12:35

E repara como foi construído até agora.

12:39

Você já consegue enxergar um tanto de coisa sobre o MCP.

12:42

E isso, na verdade... Parece teoria até começar a debugar a integração real, né?

12:49

Então, aí essas fronteiras deixam de ser detalhe e viram sobrevivência operacional, tá?

12:54

E detalhe, tá? O espectro, gente, é super poderoso, tá? Ele entra justamente aí,

13:00

como ferramenta neutra para observar handshake, request,

13:03

cancellation e estado do protocolo acontecendo no fio, tá? Enfim, né?

13:10

Agora o próximo modo muda de fase, a teoria virou base e o código entra,

13:14

tá bom? A gente se vê por lá.

## Resumo IA

[RESUMO_IA]