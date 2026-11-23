Módulo: Protocolos de Comunicação\
Aula: [TypeScript SDK (McpServer) - part I](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18598)

## Resumo da aula

McpServer é a classe de alto nível usada para construir a maior parte dos servidores MCP em TypeScript. Ela existe para encapsular a mecânica do protocolo e expor uma API mais direta para registrar capacidades, conectar transportes e operar o servidor. Em vez de começar pelo protocolo cru ou por JSON-RPC manual, o desenvolvimento parte de uma abstração que já representa o formato dominante em produção.

O MCP surgiu primeiro com SDK em TypeScript, não em Python, e isso influencia a forma como o ecossistema foi consolidado. Hosts como Claude Desktop, Cursor e VS Code já operam próximos de Node e Electron, então TypeScript se tornou o caminho de menor atrito operacional. Por isso, o SDK em TypeScript funciona como referência estrutural para entender como um servidor MCP real é montado.

A linha v1.x do SDK é a referência estável para produção, enquanto a v2 ainda introduz mudanças no modelo de schema. Essa diferença importa porque o código, os imports e a forma de declarar contratos podem mudar entre versões. Quando o objetivo é formar modelo mental sólido e implementar com menos entropia, faz sentido ancorar o estudo na v1.x.

Um servidor MCP em TypeScript gira em torno de três elementos: McpServer, schema e transport. O server concentra as capacidades expostas; o schema define e valida o contrato de entrada; o transport liga essa lógica ao meio físico de comunicação. Essa separação protege a arquitetura porque evita misturar regra de negócio com detalhes de borda e de conectividade.

Schema, no contexto de MCP, não é apenas tipagem estática: é contrato operacional validado em runtime. Como a entrada vem de um modelo de linguagem, o fato de o TypeScript compilar não garante que o JSON recebido esteja correto. O schema existe para barrar dados inválidos antes que eles atinjam handler, banco de dados ou integrações externas.

No SDK v1, o schema é definido com Zod v3. O Zod valida o input antes da execução da tool e também materializa o contrato que o host enxerga. Isso produz falha precoce e explícita: se orderId vier vazio em getOrderStatus, a chamada é rejeitada na borda em vez de contaminar a lógica de negócio.

Uma tool representa uma capacidade formal do servidor, não apenas uma função utilitária. Ao registrar getOrderStatus, o servidor declara identidade, descrição e contrato de entrada para uma operação de negócio que o host pode invocar com previsibilidade. Retomando o cenário de e-commerce, consultar status de pedido precisa virar capacidade explícita antes de qualquer query, porque o valor do MCP está justamente em expor operações confiáveis na fronteira com o modelo.

server.registerTool conecta duas dimensões da operação em uma única definição: o schema de entrada e o handler que executa a ação real. Essa composição reduz a verbosidade de lidar diretamente com JSON-RPC e concentra o ponto de manutenção da tool. O resultado é um código mais legível para implementação, revisão e debugging, porque contrato e comportamento ficam lado a lado.

No SDK, os imports usam extensão .js mesmo quando o código-fonte está em TypeScript. Isso acontece porque o caminho precisa apontar para o artefato JavaScript final consumido em execução. Parece detalhe de sintaxe, mas é um ponto de bootstrap: errar aqui impede o servidor de subir antes mesmo de qualquer lógica de tool ser avaliada.

name e version fazem parte da identidade operacional do servidor e entram no handshake com o host. Esses campos não servem apenas para documentação; eles ajudam a identificar o que está conectado e qual versão está em execução. Em ambiente real, isso facilita rastreamento, compatibilidade e diagnóstico.

Transport é o mecanismo que carrega as mensagens entre host e servidor. Em cenários locais, STDIO é o caminho direto; em cenários remotos, HTTP cumpre esse papel. A lógica do servidor permanece separada do transporte, o que permite trocar o meio de comunicação sem reescrever a regra de negócio.

O servidor só fica operacional depois de await server.connect(new StdioServerTransport()). Sem esse await, o processo pode existir, mas a capacidade MCP não fica efetivamente disponível para responder ao host. Compilar ou iniciar o processo não basta; a conexão com o transport é o passo que completa a ativação do servidor.

Chamadas de tool frequentemente dependem de API, banco, I/O e outros recursos assíncronos, então async/await é o fluxo natural de implementação. Isso não é detalhe de estilo, mas requisito estrutural para lidar com operações que não retornam imediatamente. O servidor precisa assumir desde o início que sua execução convive com latência, espera e composição de tarefas.

Se o host cancelar uma chamada, o servidor precisa interromper o trabalho em andamento e liberar recursos. AbortController fornece o mecanismo para propagar esse cancelamento a operações assíncronas que ainda estão executando. Ignorar esse ponto gera requests presas, consumo desnecessário e comportamento operacional ruim sob carga ou interrupção.

Quando existe sessão, cache ou contexto do cliente, o estado deve ficar isolado por conexão. Isso evita vazamento de contexto entre clientes diferentes e impede que uma interação influencie indevidamente outra. Em servidores MCP, esse cuidado é essencial porque múltiplas conexões podem coexistir com expectativas e dados distintos.

Paginação por cursor expõe ao cliente apenas um marcador opaco, como nextCursor, que deve ser devolvido na próxima chamada. O cliente não precisa conhecer a estrutura interna de paginação nem a ordenação usada no backend. Esse modelo reduz acoplamento, melhora estabilidade da navegação e prepara o servidor para listas grandes sem expor detalhes internos.

## Transcrição

00:00

Pessoal, tudo bem? A gente entra agora no módulo de desenvolvimento MCP.

00:07

E aqui a conversa muda de natureza.

00:11

Até esse ponto a gente falou bastante de arquitetura,

00:14

protocolo, integração, papel dos hosts, clients, enfim.

00:18

Agora a gente começa a olhar para a implementação real. Como o MCPC é construído,

00:23

como ele opera e quais decisões começa a importar quando isso vai para a produção.

00:29

O primeiro caminho que a gente escolhe para fazer isso é o TypeScript SDK,

00:32

mais especificamente a classe MCP Server.

00:35

Esse nome importa porque ele define o nível de abstração da aula inteira.

00:39

A ideia aqui não é começar pelo protocolo cru,

00:42

nem por detalhes low level.

00:43

A ideia é começar pelo padrão que hoje representa a maior

00:46

parte dos servers MCP que você encontra em produção.

00:50

E eu

00:53

quero que você acompanhe essa aula com uma pergunta simples na cabeça.

00:57

Quando eu olho para um server MCP real, o que exatamente está acontecendo ali? Vamos lá.

01:06

Essa é a agenda da aula.

01:09

Primeiro a gente começa pelo contexto, porque o sistema MCP nasceu em TypeScript.

01:13

Isso ajuda a entender algumas escolhas que aparecem no SDK

01:16

e no jeito como os servers são estruturados.

01:20

Depois a gente entra nas três peças que todo TypeScript server costuma ter.

01:25

E este é o centro técnico da aula,

01:27

entender o que você vai escrever,

01:29

revisar e debugar quando estiver olhando para uma implementação real.

01:33

Na sequência, a gente fala de zode e segurança em runtime.

01:36

Aqui a pergunta prática é,

01:38

como garantir que aquilo que vem do modelo

01:40

bate com o contrato esperado pela ferramenta?

01:43

Depois a gente passa por async, await e gerenciamento de estado.

01:47

Esse ponto é importante, porque MCP Server não vive isolado.

01:51

Ele chama API, espera I .O.,

01:53

lida com sessão e precisa se comportar bem quando o fluxo não é linear.

01:58

Então, esse é o caminho. Contexto, estrutura, segurança,

02:02

estado, assíncrono e decisão arquitetural. Vamos lá.

02:07

Antes de ir para o código, vale entender por que estamos começando por TypeScript.

02:11

Quando a Tropic publicou o MCP em novembro de 24,

02:16

O primeiro SDK foi o TypeScript, tá? Muita gente acha que foi em Python primeiro,

02:21

foi em TypeScript. Isso tem uma razão prática, tá? Os host principais,

02:25

tá? Como o Cloud Desktop, o Cursor, né? E o VS Code,

02:31

propriamente dito, eles já vivem muito perto do ecossistema Node e Electron, tá?

02:36

Então, para MCP Server,

02:38

TypeScript virou o caminho de menor atrito operacional, tá? Agora,

02:41

vamos olhar para esses blocos aqui para a gente se situar, tá?

02:45

Primeiro, V1 .x do SDK.

02:49

Este é o caminho estável hoje para a produção.

02:52

É o que a gente, inclusive, vai usar aqui como referência.

02:56

A V2 ainda está em desenvolvimento. Então,

02:58

tem mudanças importantes no modelo do esquema que não é o foco aqui do Renzo agora.

03:03

Então, vamos para o caminho...

03:08

de menos entropia.

03:11

Terceiro, o Spectre, que a gente já viu aqui algumas vezes, a importância dele.

03:14

É super necessário,

03:16

é uma ferramenta essencial na mão de qualquer desenvolvedor que está fazendo MCP.

03:22

Quarto, a gente vai falar um pouco de servidores de referência.

03:26

Na verdade, a gente já falou de algum deles, inclusive um dos principais,

03:30

que é o do GitHub, que inclusive foi um dos primeiros.

03:33

Então, assim, eles são úteis para ver padrões reais de implementação,

03:36

tá? Não só de documentação também.

03:39

Então, a ideia é simples. Entender o contexto,

03:41

escolher o caminho estável e seguir para a implementação. Bem,

03:44

e aqui está o mapa mental que a gente vai levar para o código, tá? Então,

03:49

assim, todo o servidor MCP e TypeScript costuma gerar em torno de três peças.

03:54

MCP Server, Scheme e Transport.

03:56

Então, MCP Server.

03:58

Essa é a classe de alto nível que vamos usar na maior parte dos casos.

04:02

A classe de baixo nível, low level, até existe,

04:05

mas normalmente só entra quando você tem uma necessidade bem específica. Então,

04:09

a gente vai trabalhar no nível da abstração da classe MCP7. Ou seja,

04:14

no Redzone, vamos ficar nesse caminho que é o caminho recomendado.

04:21

Segundo os esquemas, hoje no SDKv1,

04:24

significa que nós vamos usar o Zod na versão 3. O ponto prático é simples.

04:30

O schema valida o input em runtime e gera o contrato que o host enxerga.

04:34

Isso evita muitos bugs bobos chegando dentro da lógica da ferramenta.

04:39

E por fim, o transporte. É o meio por onde o servidor conversa.

04:45

Local com STDIO, remoto com HTTP. Simples assim.

04:49

Então, a ideia é separar a lógica do servidor do meio físico da comunicação.

04:54

A lógica do servidor do meio físico de comunicação.

04:58

Então, guarda só isso antes de abrir a IDE que a gente vai fazer daqui a pouquinho.

05:01

Server, esquema e transporte.

05:04

O resto a gente vai entender olhando para o código.

05:08

Por falar em olhar para o código, olha só.

05:10

Vamos começar aqui com esse código mínimo de

05:13

inicialização de MCP Server e TypeScript.

05:16

Dê uma olhada aí.

05:20

Passando por cima aqui no código. Vamos lá. Aliás,

05:23

vamos fazer isso junto. Primeiro, olha só, gente, os imports.

05:27

import com extensão .js.

05:30

Isso é importante, porque o SDK usa a mesma extensão. Então,

05:36

mesmo escrevendo TypeScript, o import aponta para o caminho JavaScript final.

05:42

Parece detalhe,

05:44

mas é um daqueles detalhes que quebram o bootstrap

05:47

antes de você chegar na lógica da TUR.

05:50

Depois, vem aqui o MCP7.

05:55

E aqui nasce o servidor propriamente dito. Tem name,

05:59

version, e depois a gente tem os handlers.

06:06

Então, esses dados entram no handshake com o host. Então, não trate como detalhe.

06:12

Em ambiente real, nome e versão ajudam a identificar o que está rodando.

06:21

Esse await... Ah, desculpa. Vamos lá. Olha a última parte, pessoal.

06:25

Await server connect, abre parênteses, new stdio server transport.

06:32

Este await é obrigatório. Sem ele, você pode ter um processo vivo.

06:38

Mas um servidor que não responde. É o famoso compile, mas não está operacional.

06:43

Então, assim, gente, super rápido. Do lado direito aqui...

06:49

Ter um resumo dos pontos para chegar quando algo não dá certo.

06:55

São basicamente os pontos que eu repassei aqui com vocês.

06:58

Import JS, top-level weight, STDIO versus HTTP e server info. Bem,

07:06

Agora a gente entra no ponto mais importante desse exemplo, o esquema com o Zod.

07:13

Uma das partes mais importantes de um server MCP...

07:19

É que dado que o input vem de um modelo de linguagem,

07:22

Nunca confie que o JSON vai chegar certo só porque o TypeScript compila.

07:27

O Zod entra nessa borda.

07:30

Antes do handler rodar, o SDK valida o input.

07:34

Se o modelo mandar algo fora do contrato, o ator nem chega na lógica de negócio.

07:39

E é isso que a gente quer em produção. Erro cedo, erro claro e erro na borda.

07:46

O Zod não só tipa o código. Mas nesse exemplo aqui,

07:50

Ele não só tipa o código, mas ele protege o banco de dados.

07:53

Se o modelo alucinar e tentar enviar um

07:58

order ID vazio durante uma triagem de e-commerce,

08:02

O Zod barra a aquisição localmente.

08:08

Ele verifica.

08:10

O order ID é no mínimo um. Order ID obrigatório. Não pode ser vazio,

08:15

Tá? Ou seja, tem que ter no mínimo o tamanho,

08:17

Né? Aqui é o tamanho da string, né?

08:19

Tem que ter no mínimo um caractere, não pode vir vazio, tá?

08:22

Esse é o ponto, esse é o ponto, esse é o

08:30

ponto para a gente guardar, tá? No MCP,

08:32

Esquema não é detalhe de tipagem, esquema é contrato operacional, tá?

08:38

Bem, agora, beleza, a gente tem o MCP -7,

08:40

Agora como é que a gente registra uma tool?

08:42

A gente faz isso usando server.registerTo.

08:46

Dá uma olhada aqui.

08:49

Server.registerTo. Essa To é a getOtherStatus.

08:54

Tem aqui o título, uma descrição e um input esquema. Então, olha só.

08:59

Veja essa abstração. Com o registerTo, nós unimos o contrato de dados,

09:04

que é o Zod, e a execução real, que é a query do PostgreSQL. A gente...

09:12

A gente une as duas coisas, tá?

09:15

E o SDK, aliás, numa única chamada, tá? Numa única chamada, beleza?

09:21

E com isso, pessoal, a execução,

09:25

Com isso o SDK ele abstrai toda a verbosidade do JSON RPC,

09:30

Permitindo que a gente foque exatamente na regra de negócios da nossa empresa, tá?

09:34

Então, ou seja, isso facilita a implementação, leitura e code review, né?

09:40

Bem, ah, só lembrando, tá? A query é a API, tá gente?

09:46

Então isso aqui é a execução da API, tá bom? Vamos lá.

09:55

Bem, agora a gente sai da estrutura da tool. Ou seja,

09:58

A gente viu como é que cria um server.

09:59

A gente viu como é que adiciona uma tool nesse server.

10:02

E agora a gente vai olhar para o comportamento operacional.

10:05

Aqui o ponto é simples, tá? MCP com TypeScript, MCP com TypeScript,

10:09

Tudo tende a passar por assim que a wait.

10:20

Então, ou seja, esse é o caminho normal, tá? Segundo,

10:24

Cancelamento com abort controller. Se o host cancela a chamada,

10:27

O servidor precisa parar o que estiver fazendo e liberar recursos.

10:31

Isso evita requests presas e vazamentos simples de resolver, mas é fácil de esquecer.

10:37

Terceiro, estado por conexão. Quando existe sessão, cache ou contexto do cliente,

10:44

esse estado precisa ficar isolado.

10:46

Então não misture estado entre clientes. E paginação por cursor.

10:51

O cliente recebe o next cursor e devolve na próxima chamada,

10:56

sem conhecer a estrutura interna, tá?

10:58

Guarda só o checklist para o hands-on, assim que o cancelamento estiver de cursor, tá?

11:05

Bem, vamos embora para o código? Agora a gente vai para o hands-on, tá?

## Resumo IA

[RESUMO_IA]