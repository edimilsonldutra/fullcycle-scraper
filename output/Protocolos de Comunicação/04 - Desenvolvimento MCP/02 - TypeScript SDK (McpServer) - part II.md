Módulo: Protocolos de Comunicação\
Aula: [TypeScript SDK (McpServer) - part II](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18599)

## Resumo da aula

Executar tsc sem emitir artefatos é uma verificação estrutural do servidor antes do bootstrap. Esse passo não substitui a validação em runtime feita pelo schema, mas confirma que imports, tipos, assinaturas e organização do projeto estão consistentes para gerar JavaScript executável. Quando o compilador termina em silêncio, o projeto ainda não está “correto” do ponto de vista de negócio, mas está estruturalmente pronto para subir. Isso reduz ruído no troubleshooting porque separa erro de compilação de erro de protocolo ou de execução.

Retomando o McpServer e o StdioServerTransport já definidos anteriormente, o primeiro teste operacional útil é expor uma tool mínima como systemPing. Ela não existe para demonstrar lógica de negócio, e sim para validar o pipeline completo: instanciar servidor, registrar tool, conectar no transport e confirmar no Inspector que o host consegue listar e executar capacidades. Se esse hello world falha, o problema está no bootstrap, no transporte ou na resolução do projeto, não no domínio de e-commerce. systemPing funciona como teste de sanidade do ambiente.

A validação com Zod acontece na borda da tool e transforma input inválido em erro protocolar antes de qualquer lógica interna rodar. No caso de getOrderStatus, exigir orderId com pelo menos um caractere e restringir urgency a low ou high impede que chamadas malformadas atinjam query, conexão ou regra de negócio. Quando o cliente omite orderId, a falha aparece como -32602, que é o erro de parâmetros inválidos observado no fluxo JSON-RPC abstraído pelo SDK. O ponto importante não é o código em si, mas o fato de que o contrato operacional vira comportamento observável no protocolo.

A evolução relevante do exemplo é sair do contrato abstrato e executar uma consulta real em PostgreSQL. A tool recebe os parâmetros já validados, instancia um client do banco e executa um select parametrizado para verificar se o pedido existe e retornar seu estado. Isso mostra onde a integração com infraestrutura entra: depois da validação e dentro do handler, nunca antes. Demos em memória servem para aprender a superfície da API; banco relacional entra quando o servidor precisa responder com dados reais do domínio.

O Inspector continua útil mesmo quando a tool já consulta banco, porque ele isola o servidor do restante da orquestração. Com ele, é possível confirmar se a tool aparece no catálogo, testar inputs válidos e inválidos e observar diretamente o retorno ou o erro -32602 sem depender de outro cliente. Esse tipo de teste encurta o ciclo de depuração: primeiro valida-se o servidor sozinho, depois a integração com clientes mais complexos. Em implementação prática, essa ordem evita confundir erro de tool com erro de agente.

Quando uma tool pode demorar, o handler precisa observar o AbortSignal recebido no contexto da execução. Esse sinal representa o cancelamento enviado pelo cliente ou orquestrador e permite interromper trabalho que já não tem valor, como uma query longa ou uma simulação de processamento. O ganho não é apenas responsividade: cancelamento correto evita consumo residual de CPU, memória e conexões. Em servidores MCP, ignorar esse sinal significa continuar executando mesmo depois que ninguém mais precisa da resposta.

Uma Promise manual envolvendo setTimeout é uma forma simples de simular uma operação longa e tornar o cancelamento observável. O setTimeout agenda a conclusão futura; o listener do AbortSignal chama clearTimeout para remover esse agendamento da fila do Node.js e rejeita a Promise, desviando o fluxo para tratamento de erro. Esse padrão ensina a disciplina correta: cancelar não é apenas “parar de esperar”, mas limpar explicitamente o recurso pendente. Em código real, o mesmo raciocínio vale para query, stream, subprocesso ou chamada HTTP.

Usar um cliente Python para conversar com um servidor TypeScript via stdio comprova que a interoperabilidade está no protocolo, não na linguagem. O cliente recebe o catálogo de tools exposto pelo servidor, o modelo escolhe quais chamar e os schemas orientam a montagem dos argumentos. Quando o Claude decide usar analyzeLogistics ou runDiagnostic, ele está consumindo capacidades publicadas pelo servidor TypeScript sem acoplamento à implementação interna. Essa etapa valida que o servidor não funciona apenas no Inspector, mas também em um cenário real de orquestração entre runtimes diferentes.

BrokenResourceError aparece quando uma tarefa de leitura em segundo plano tenta encaminhar dados para um canal que o cliente já fechou. No cenário cancelado, a lógica de negócio pode até ter se comportado corretamente — o AbortSignal foi emitido e a execução foi interrompida —, mas a borda do cliente ainda precisa tratar a exceção gerada pelo fechamento assíncrono do stream. Por isso o erro é operacionalmente inofensivo para o domínio, mas ruim para a experiência de execução: polui o terminal e pode encerrar o processo com código de falha. A correção não está na tool, e sim no tratamento explícito dessa exceção no cliente.

Capturar a exceção no main do cliente é a diferença entre um cancelamento esperado e uma falha aparente do sistema. O abort faz parte do contrato operacional de uma tool longa; portanto, ele precisa ser tratado como fluxo previsto, não como pane inesperada. Quando essa captura não existe, a exceção “estoura na cara do cliente”, mesmo que o servidor tenha feito a limpeza corretamente. Em produção, a borda deve traduzir esse evento para uma resposta controlada, como “diagnóstico cancelado”, em vez de expor stack trace ou encerrar com erro bruto.

## Transcrição

00:01

Pessoal, vamos lá para a aula, para a parte prática,

00:04

para o hands-on, que é a parte mais legal.

00:07

Então, vamos começar aqui.

00:10

Deixa eu fechar aqui.

00:16

Começar aqui do zero. Bem, vou dar um start aqui. Vamos lá.

00:23

Primeira coisa, eu vou só dar o CD para a aula.

00:28

O tempo aqui para dar tudo certinho. Bem, vamos lá. Beleza?

00:37

Então pessoal, olha só,

00:39

nos módulos 1 e 2 nós vimos a arquitetura conceitual do

00:42

MCP e interagimos com servidores que já vieram prontos da comunidade,

00:46

né? Como PostgreSQL e GitHub.

00:48

Mas agora chegou a hora da verdade,

00:50

nós vamos desenvolver o nosso próprio servidor MCP personalizado do zero.

00:54

A gente vai criar ferramentas focadas no nosso domínio de triagem de

00:58

e-commerce usando a SDK oficial da Anthropic e TypeScript.

01:02

E a grande força de construir esse seu servidor usando TypeScript,

01:05

pessoal, é a segurança dos contratos de dados.

01:08

O SDK oficial se integra de forma nativa com a biblioteca Zod.

01:12

E o Zod é quem vai definir e validar as estruturas

01:15

que a inteligência artificial envia para a nossa aplicação.

01:18

Ao fazermos isso,

01:19

garantimos em tempo de compilação que os dados passados pelo LLM

01:23

respeitem exatamente o formato que a nossa aplicação espera.

01:26

Sem quebras inesperadas em produção, tá?

01:29

Então, para isso, pessoal, eu vou executar o compilador aqui,

01:35

só que eu vou pedir para ele não emitir nada, só para saber se está tudo certinho.

01:41

Deixa eu só garantir também, fazer o npm install aqui, pessoal.

01:49

Gente, está tudo ok.

01:52

Então, vamos rodar aqui. Beleza, nesse caso aqui, no news, good news.

01:57

Vocês podem ver que o compilador encerrou silenciosamente,

02:02

sem nenhum aviso ou erro.

02:05

Isso confirma que nossos arquivos estão perfeitamente

02:07

consistentes e prontos para rodar, tá bom?

02:10

Então é o seguinte, vamos começar pelo esqueleto absoluto de um servidor MCP.

02:14

Eu vou mudar para a aba de arquivos aqui, pessoal,

02:17

para abrir o terminal aqui, o primeiro, né?

02:21

Que é esse do servidor mínimo, tá?

02:25

Bem, só para a gente ficar na mesma página, esse aqui é a nossa versão...

02:33

é nosso hello world de e-commerce, então aqui eu tô só simulando

02:39

um ping no sistema, tá? E nesse caso aqui, como vocês podem

02:42

ver, eu tô usando a importação da classe MCPServer, né? Do pacote

02:48

mcp.js, que tá dentro do

02:53

model, context, protocol no SDK oficial, tá?

02:57

E estou também importando o STDIOTransport

03:01

que é o STDIOServerTransport, pessoal, porque

03:05

nesse caso aqui, o mecanismo de transporte vai ser o STDIO padrão, né? Normal aqui,

03:10

de entrada e saída de console, tá?

03:12

E nesse caso aqui, pessoal, eu aqui, ó,

03:17

tá vendo, primeiro, extensivo MCP-Server, né? Eu dou o nome para ele e uma versão,

03:23

depois eu registro uma ferramenta. A minha ferramenta, ela chama System Ping, tá?

03:27

E ela simplesmente retorna, vai sempre retornar esse texto aqui, tá?

03:32

E aqui, na sequência, eu pego e inicializo o meu servidor,

03:35

Tá? Conecto e inicializo o meu servidor, tá bom?

03:38

Então, vamos lá. Vamos

03:43

rodar aqui no Specter mesmo, tá?

03:46

Vamos no bom e velho Specter.

03:49

Vamos ver onde ele vai aqui.

03:51

Para essa demo aqui, ela é muito simples rodar no Specter. Vamos lá.

03:58

Para variar, ele abriu aqui na outra tela.

04:03

Então, como vocês lembram, vou conectar no meu servidor.

04:07

Vou listar minhas tools. Tem o System Ping.

04:12

Tem o Run Tool. E tem aqui o texto. Então,

04:14

ou seja, o nosso primeiro servidor MCP rodando com sucesso.

04:19

Eu vou só derrubar ele aqui para a

04:23

gente poder rodar o Specter no próximo exemplo. Então, vamos lá.

04:31

Agora a gente vai ver os DOD junto ali com

04:37

o banco de dados real que a gente usou no M2,

04:40

Tá? Vamos fazer essa integração, tá?

04:42

Então, demos simples de memória são legais,

04:44

mas em aplicação comercial de e-commerce real, pessoal,

04:47

a gente precisa bater no banco de dados relacional. Então,

04:50

vamos abrir aqui agora a segunda demo, tá?

04:56

Então, essa segunda demo é o seguinte.

05:02

Mesma coisa, MCP-Server, stdio, agora eu estou importando a biblioteca Zod, tá?

05:09

Estou importando também o pacote de PostgreSQL, tá?

05:14

E estou também criando aqui um client PostgreSQL,

05:20

Tá bom? Beleza?

05:22

Estou declarando aqui o meu servidor, tá? Como o Zod PostgreSQL, beleza?

05:30

Estou registrando uma única tool, que é GetOrderStatus, tá? E olha que interessante.

05:37

Ele tem dois parâmetros, tá? O OrderId e o Urgence.

05:42

Só que eu estou usando o Zod para validar o seguinte,

05:46

Tá? Que este parâmetro tem que ter pelo menos um caractere,

05:50

Ou seja, não pode vir vazio, tá bom?

05:52

E estou validando aqui também que o segundo parâmetro só aceita dois textos,

05:57

Ou low ou high. Se não vier nada, o default é low, tá?

06:03

Bem, vamos lá.

06:08

Dentro da lógica da ferramenta,

06:10

nós instanciamos o cliente do banco de dados Postgres,

06:13

Tá bom? A gente instanciou o cliente do banco de dados Postgres aqui.

06:18

A gente vai executar esse select aqui no próprio...

06:24

Aliás, a gente vai executar esse select,

06:25

Tá? Que vai receber um Order ID e ele vai simplesmente retornar...

06:31

Se o pedido foi encontrado ou não, tá bom? Tão simples quanto isso, tá?

06:37

Na sequência, eu venho e faço a mesma coisa, inicializo o meu servidor, tá?

06:42

Vamos lá, vamos

06:45

inspecionar esse nosso segundo MCP Server,

06:47

que agora é o MCP Server com uma tool, tá?

07:00

Com uma tool, eu também tinha a tool, né pessoal? Com uma tool mais complexa,

07:05

Tá? Que não seja uma tool Hello World que entra no valor fixo, tá?

07:09

Vou colocar aqui 14, vamos ver se tem, tem esse pedido.

07:15

Agora vamos testar não passando nada para ver,

07:20

Deveria dar um erro, aí deu um erro, lembra que eu falei para vocês que vocês,

07:24

Quando a gente estava discutindo JSON RPC,

07:27

Que a gente viu lá o erro menos 32.602, que input validation error,

07:33

Então eu falei para vocês que a gente ia ver bastante aqui,

07:35

Então olha só, nesse caso aqui,

07:37

É o Zod que forçou esse

07:39

Erro aqui durante a execução aqui, tá?

07:49

Bem, então,

07:53

Bastante simples, pessoal. Aqui a gente vendo na prática o Zod validando, tá? Essa era a ideia.

07:59

Vou de novo aqui dar um CTRL-C aqui nesse... E derrubar esse servidor, tá?

08:06

Só que agora, pessoal, é o seguinte.

08:09

Eu quero fazer uma coisa um pouco mais complexa, ou mais completa, melhor dizendo.

08:16

Então, vamos para a nossa próxima demo.

08:20

Essa é a demo 3 de Async e de State.

08:24

Pessoal, eu implementei, eu fiz uma coisa diferente aqui.

08:28

Nós não vamos usar o Inspector não, mas vamos lá.

08:30

Bem, vamos imaginar o seguinte, pessoal. Se o orquestrador...

08:37

Decidir dar chamada ou cliente desconectar,

08:40

Nós não queremos queries travadas no Postgres consumindo memória.

08:43

Então, como é que a gente lida com cancelamento?

08:46

Então, olha só.

08:48

Nesse caso aqui, pessoal,

08:50

A gente tem uma tool que é a Run Diagnostic.

08:57

O pulo do Gartner está no segundo argumento do Handler do Run Diagnostic, esse aqui de baixo.

09:05

E está no segundo argumento do render, olha só que é o signo né

09:12

É o contexto dele, nós desestruturamos o

09:18

Signo de dentro dele, que é um aborto e

09:22

Signo padrão das WebP, está esse cara aqui, o

09:26

Aborto signo padrão das WebP, está bom

09:28

E aí o seguinte, então o que a gente vai fazer?

09:31

Primeiro, criamos uma promise manual para envelopar

09:34

A nossa simulação do processo demorado,

09:36

Tá? Que é esse cara aqui, tá bom? A gente simula o processo demorado aqui.

09:42

E dentro da promise, a gente inicia um set

09:46

Timeout e resolverá o fluxo após N segundos, tá?

09:49

E paralelamente, nós adicionamos um escutador ao sinal de cancelamento,

09:55

Que é esse signo.

09:56

Que esse cara aqui é

09:58

Um escutador para o aborto. Ou seja,

10:04

Se o MCP client desistir do request e enviar o sinal de cancelamento,

10:08

Nós disparamos o client timeout para remover o agendamento

10:12

Da fila de execução do Node.js,

10:14

Evitando o consumo residual de recursos e rejeitamos a promise, com reject new Error,

10:20

Passando essa mensagem de erro aqui para encerrar o await.

10:25

E com isso, desvia o fluxo por cache. Então, para testar essa interrupção,

10:30

O estado persistido da sessão de forma elegante,

10:33

Nós vamos despedir da interface gráfica do Spectre.

10:36

A partir de agora, nós vamos usar um cliente local, interativo, escrito em Python,

10:40

Que se integra dinamicamente com o nosso servidor TypeScript via STDIO.

10:45

Aqui a beleza do cross-language.

10:47

O script está no arquivo client, custom

10:54

client,

10:56

é ponto. Pai tá

11:00

roupa Então

11:08

vamos lá você

11:10

que é para validar lá esse é uma demo cross-language da aula 15 tá

11:16

beleza é o cloud que é o modelo tá ele vai agir como orquestrador tá

11:22

ele recebe o catálogo do servidor tá escrito ele decide sozinho quais tu chamar

11:27

para responder e o esquema gerado pelo uso de guia input do Cláudio né

11:31

É erro de avaliação dos óbitos recebidos pelo Code. Estou aqui realmente,

11:36

de fato, pessoal, o que eu estou fazendo aqui, deixa

11:42

eu mostrar para vocês aqui.

11:44

Está vendo? Eu estou executando um modelo,

11:50

estou fazendo um chat,

11:53

estou conversando com o meu modelo e enviando uma mensagem para ele.

11:57

E o modelo que eu estou usando é o Haiku 4.5, está bom?

12:03

E eu vou gerar para ele, na verdade, eu vou pedir para ele uma mensagem.

12:09

Eu vou mandar uma mensagem para ele.

12:11

Um prompt, na verdade. Beleza? Deixa eu mostrar para vocês aqui como é que funciona.

12:18

Vamos lá. Está vendo? Ele está bem detalhadinho aqui, pessoal,

12:21

para explicar o passo a passo. Mas vamos executar para a gente ver?

12:25

Ele recebe...

12:29

é que ele recebe o argumento que é o

12:32

prompt já tá então vamos ver ó vamos olhar aqui

12:37

ó é ele tá ele ou seja ele vai executar

12:40

esse MCP serve e tem um prompt aqui tá olha

12:46

só vamos

12:48

ver ó

12:51

é orquestrado, orquestrando o servidor, conectando o servidor, tem duas das expostas

12:57

pelos ordens análise logística e o diagnóstico aí eu pus no prompt aqui,

13:02

inicia a análise logística dos pedidos 15 e 42

13:05

e me diga o total de pedidos rastreados,

13:08

tá? aí ele viu aqui, cara, tools, né? que ou seja,

13:12

o TypeScript enviou para ele então o Cloud usou a tool TypeScript

13:15

Analyze Logística com ID 15 e depois Analyze Logística com ID 42, tá bom?

13:22

e iniciou, aqui,

13:25

iniciado o track de dois pedidos a resposta final

13:28

análise logística foi iniciada com sucesso com base nos resultados

13:32

pedido 15 iniciado o track de um pedido, pedido

13:36

42 iniciado o track de dois pedidos, tá agora

13:43

pessoal, nós vamos executar uma outra tu, ou seja, ele executou a primeira tu, beleza

13:49

agora eu vou pedir para ele rodar, olha que

13:52

legal, pessoal, vou pedir para ele rodar agora,

13:55

é o mesmo chamado, tá?

13:57

Só que eu vou pedir para ele rodar um diagnóstico de 10 segundos. Então, olha que legal.

14:03

Ele viu lá que tem duas tools. Análise logística, ele usou de cima.

14:07

E análise... Agora, olha só o que eu vou fazer.

14:09

Eu vou forçar um ESC. Eu vou clicar aqui no ESC,

14:11

tá? Olha lá, operação cancelada. Olha só que doideira.

14:17

Resposta final. Diagnóstico foi cancelado. Execução foi interrompida.

14:20

Parece que foi pressionada a tecla X durante o processo. Deseja continuar?

14:25

Novamente com 10 segundos ou um tempo diferente, né?

14:27

Eu não quis isso, tá? Ele basicamente forçou aqui o stop,

14:32

tá? Então, olha só que legal, pessoal. Ele gerou um abort signal.

14:37

E isso, ele desencadeou uma execução, uma...

14:42

Como se ele tivesse... Como se ele tivesse, não.

14:47

Ele subiu uma exceção, tá? E a exceção não está sendo tratada,

14:53

tá? Então, inclusive, olha só que legal, gente.

14:57

Eu vou pedir para ele tratar a exceção.

15:01

Vamos pedir para o nosso agente nos ajudar aqui. Entenda esse erro.

15:14

Aliás, deixa eu dar um stop e começar outro aqui.

15:19

Entenda esse erro.

15:28

Eu não sei se ele está tentando corrigir o erro, inclusive,

15:31

ou se ele está de fato entendendo. Vamos lá. Vamos ver o que ele vai responder.

15:39

Opa, está aqui pensando ainda. Vamos lá.

15:44

Resumo do erro. O erro é... NIO, Broke Resource, dentro de Exception Group,

15:51

é disparado quando uma tarefa em segundo plano, chamada STD Auto Reader, do SDKWCP,

15:56

tenta enviar uma mensagem recebida do servidor para um canal de comunicação interno,

16:00

que é o ReadStream, que foi fechado pelo cliente.

16:04

Por que isso aconteceu quando você cancelou o ESC?

16:06

A diferença fundamental está no tempo de resposta do servidor após o cancelamento.

16:11

A execução normal, que é o sucesso,

16:13

o código termina de responder e o loop de execução principal é finalizado.

16:16

O código sai do bloco e isso fecha o canal receptor do cliente.

16:20

Como o servidor não tem mais nada para enviar,

16:23

a tarefa em segundo plano STD Reader do SDK

16:26

fica bloqueada esperando o STD Out do servidor.

16:29

O código sai do bloco, se fecha o STD in do processo do servidor.

16:32

O processo do servidor detecta que o seu STD in fechou e encerra.

16:38

Consequentemente, fechou o STD out, que é sinalizando end of file.

16:43

O loop da tarefa STD out termina de forma limpa por conta do end of file,

16:47

sem tentar enviar dados adicionais. Nenhum erro é disparado.

16:52

Cenário B, execução cancelada. Então, olha só.

16:56

Como contornar esse erro?

16:57

Como a conexão foi concluída com sucesso e a

16:59

mensagem final do clone foi exibida corretamente,

17:01

o erro é inofensivo para a lógica de negócio,

17:04

mas incomoda por estourar no terminal e retornar um código de saída de falha 1.

17:08

Você pode capturar. Então, vamos fazer o seguinte. Vamos seguir com a sugestão dele.

17:15

Que nesse caso aqui, vamos mudar o nosso main do cliente. Beleza?

17:23

Concordo plenamente com o ponto dele aqui, ó. O menino tá dando

17:28

cat, né? É tão simples quanto isso, né? Vamos ver aqui. Vamos

17:37

agora executar de novo. Eu vou fazer a mesma ação. Vamos ver se a dica do servidor

17:43

que é óbvia, né? Eu deveria estar capturando a

17:46

mensagem aqui no controle, essa mesma coisa, e

17:52

aí esquece, ó.

17:59

O diagnóstico foi cancelado, parece que você pressionou S durante a execução, gostaria de rodar novamente,

18:03

né? Assim, a única diferença, pessoal, é que esse, de fato,

18:07

ele lançou uma exceção lá de dentro que a gente esperava que isso acontecesse.

18:09

Que é o aborto, tá? Só que a gente não tratou a exceção aqui na borda,

18:13

Tá? Isso é um erro muito noob, né?

18:17

Você não tratar a exceção e estourar na cara do cliente,

18:22

Né? Então, pessoal, ficamos por aqui no nosso hands-on de hoje, tá bom?

## Resumo IA

[RESUMO_IA]