Módulo: Protocolos de Comunicação\
Aula: [Ecossistema Final part 2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18934)

## Resumo da aula

Retomando o Resolution Center já montado anteriormente, a camada nova começa na implementação concreta da tool ler_pedido_financeiro. Essa tool encapsula a leitura financeira do pedido: extrai o identificador a partir da entrada, consulta a fonte de dados e devolve um JSON estruturado para o restante do fluxo. O ponto importante não é apenas “buscar no banco”, mas transformar uma entrada textual em um contrato operacional confiável para o investigador. Sem essa etapa, o LLM continuaria genérico; com ela, passa a operar sobre dados reais do domínio.

Extrair o ID do pedido é a etapa que converte linguagem natural em chave de consulta. Se essa extração falha ou fica ambígua, todo o restante do fluxo perde confiabilidade, porque estoque, logística e síntese passam a trabalhar sobre um pedido errado ou inexistente. O retorno em JSON fecha esse contrato com um formato previsível, fácil de transportar entre nodes e simples de validar em testes. A alternativa seria retornar texto livre, mas isso aumentaria acoplamento semântico e dificultaria tanto a composição quanto a manutenção.

A consulta ao banco aparece aqui como implementação da blindagem já estabelecida pelo MCP: o investigador não emite SQL arbitrário, ele chama uma capacidade controlada. No exemplo, a busca do pedido é mostrada de forma direta, inclusive com retorno de dados financeiros em estrutura serializável. Essa mediação importa porque o restante do ecossistema passa a depender de um payload estável, e não de detalhes internos da persistência. Quando a fonte mudar de dicionário para PostgreSQL, o contrato da tool pode permanecer o mesmo.

O orquestrador materializa as integrações remotas com funções assíncronas que disparam requisições HTTP para portas específicas. No fluxo mostrado, estoque e logística são chamados separadamente, cada um em seu endpoint, o que preserva autonomia de serviço e permite evolução independente. Esse wiring precisa ser explícito porque a topologia do grafo só vira comportamento real quando cada node sabe como acionar seu destino remoto. Uma alternativa seria serializar as chamadas em sequência, mas isso aumentaria a latência total sem necessidade.

Lembra do fan-out já definido anteriormente; aqui ele deixa de ser padrão abstrato e vira duas arestas saindo do node investigador. Essa decisão topológica significa que, após a investigação inicial, o sistema abre duas linhas de execução concorrentes: uma para estoque e outra para logística. O ganho prático é desempenho, porque o tempo de resposta passa a depender do ramo mais lento, e não da soma dos dois. O desenho do grafo e o runtime ficam alinhados: duas saídas no grafo correspondem a duas chamadas remotas disparadas no mesmo estágio.

Depois do paralelismo, o sistema precisa reconciliar os resultados em um ponto único de consolidação. O critique recebe os payloads produzidos por estoque e logística, inspeciona o que cada agente devolveu e compõe a resposta final para o cliente. Essa junção não é mera concatenação; ela funciona como etapa de compilação semântica, transformando relatórios parciais em uma mensagem coerente. O valor dessa etapa aparece quando os agentes produzem saídas complementares e o usuário precisa de uma resposta única.

Os payloads são os objetos que carregam contexto de trabalho entre investigador, agentes remotos e critique. O aspecto novo aqui não é o uso de JSON em si, mas a visibilidade de quais mensagens cada componente recebe e devolve durante a execução. Isso permite inspecionar contratos reais em vez de inferi-los pelo código, o que ajuda a depurar incompatibilidades de campo, ausência de dados e erros de integração. Em sistemas multiagente, payload mal definido costuma ser uma fonte mais comum de falha do que o transporte HTTP.

A visualização em waterfall mostra a ordem temporal e a sobreposição das operações distribuídas. Quando o LangGraph inicia a requisição pai e cada integração gera seus spans, o Phoenix passa a exibir a causalidade completa: chamada da tool, acesso ao MCP, requisição para logística e demais etapas do fluxo. Esse formato é especialmente útil para confirmar se o fan-out realmente ocorreu em paralelo ou se alguma integração ficou bloqueando a outra. Em troubleshooting, o waterfall transforma a topologia lógica do grafo em evidência observável de runtime.

A telemetria útil não registra apenas o início e o fim da requisição principal; ela precisa capturar também invocações de tools e chamadas entre serviços. No fluxo implementado, isso permite navegar por cada etapa e localizar onde o tempo foi gasto ou onde uma falha ocorreu. A consequência prática é operacional: o sistema deixa de ser uma caixa-preta e passa a oferecer rastreabilidade ponta a ponta. Em produção, essa visibilidade reduz o custo de diagnosticar erros intermitentes e gargalos distribuídos.

Os testes cumprem um papel adicional em ecossistemas com IA: eles descrevem com precisão o que entra, o que deve sair e quais contratos precisam ser preservados. Texto e diagrama continuam úteis, mas testes executáveis delimitam comportamento esperado de forma verificável, inclusive para manutenção assistida por IA. Quando a suíte cobre tools, payloads e integrações do grafo, ela se torna a documentação mais confiável para evoluir o sistema sem quebrar o fluxo. Quanto melhor a IA consegue ler esses testes, maior a chance de ela propor mudanças compatíveis com o comportamento real do código.

## Transcrição

00:01

Bem, chegamos ao último laboratório do nosso curso, tá? E ao longo dessa jornada,

00:05

aprendemos a conectar LLMs a banco de dados com MCP

00:08

e aprendemos a fazer agentes conversarem via protocolo A2A,

00:12

né? Agora a gente vai unir isso tudo, tá?

00:16

Bem, só para vocês terem uma ideia, né?

00:19

Aqui é o nosso aplicativo, né? O nosso Streamlit,

00:22

tá? Tem aqui a topologia do nosso lab,

00:27

tá? Tem aqui a interface conversacional.

00:30

Tem aqui o OpenTelemetry do Phoenix, tá?

00:35

Bem, então

00:38

vamos seguir aqui, ó.

00:41

Então, vamos lá.

00:45

Então, como vocês já deveriam ter resolvido os desafios laboratoriais,

00:49

né? Então, vamos analisar o resultado final, tá?

00:54

Deixa eu mostrar aqui o PostgreSQL, tá?

00:58

Então, vamos lá. Então, é...

01:03

Vamos procurar aqui o TUDU.

01:08

TUDU 1. Boa. O TUDU 1 era implementar a declaração da TUR,

01:12

ler pedido financeiro, tá bom?

01:15

Então, aqui está o coração do investigador, tá?

01:18

O objetivo era declarar a TUR, né? E logo abaixo, tá?

01:23

Nós extraímos, que é no TUDU 2 e 3, tá?

01:28

E 4 também, nós extraímos o ID, consultamos o banco e devolvemos o JSON.

01:33

Isso transforma o LLM genérico no analista financeiro

01:36

plugado à realidade do banco de dados, tá, pessoal?

01:39

Mas legal, olha aqui, o OpenTelemetry aparecendo aqui também, tá?

01:43

Então, pessoal, era simples assim, era

01:46

fazer a declaração da TUR, né?

01:51

Obviamente, a chamada da TUR, né? Que é extrair o ID do pedido.

01:54

Depois buscar o pedido no dicionário e, enfim,

01:58

retornar o conteúdo com os dados via JSON, tá?

02:03

Bem, agora aqui no grafo, pessoal, que tal?

02:05

Isso aqui é a espinha dorsal do nosso sisteminha, tá? Então,

02:12

a topologia é start, play no investigador, tem o fanout, tá?

02:15

O pre-stock para a logística, depois o critique, né?

02:19

E aí, retornando para o usuário, tá bom?

02:24

Aqui, vamos... Especificamente no grafo, tá? Vou procurar o to-do aqui também.

02:37

Veja como que ficou, gente. Aqui no orquestrador, os to-dos 1 e 2.

02:42

Eu acho que eu apaguei os to-dos, mas deixa eu ver se eu acho aqui.

02:46

É uma função assíncrona que dispara a requisição HTTP. Vamos ver aqui. Vamos lá.

03:14

Tanto para estoque quanto para logística. Aqui, boa.

03:18

Tanto para estoque. Beleza?

03:20

Tanto para estoque, que é o 8-way call, tá?

03:24

Quanto para logística, pessoal, tá?

03:27

O que a gente está fazendo é exatamente isso.

03:30

Um na porta 9002, outro na porta 9003, tá?

03:34

Beleza? Agora, vamos ver como é que o grafo ficou,

03:39

tá, pessoal? Vamos lá embaixo.

03:46

A mágica da performance acontece aqui, que é o fanout, tá? É aqui, o fanout.

03:52

Ó, a gente tá criando dois ads, tá?

03:55

Os dois saem do mesmo nó, que é o investigador.

03:58

Um vai pro nó estoque, o outro vai pro nó logística, tá?

04:01

Então aqui eu tenho um nó investigador, né?

04:03

E um do investigador eu vou pro do estoque e pro logística.

04:07

No desenho, pessoal, é esse aqui, ó.

04:11

No desenho é esse aqui, ó. Do investigador eu dou, né? Esse aqui é o nó, né?

04:15

A partir do momento que eu adiciono esses dois caminhos aqui,

04:19

tendo o investigador como origem, tá? É o fanout, tá bom? E

04:25

depois, pessoal, a gente faz a junção desses nós das respostas, que é,

04:31

no caso, ao contrário. Eu tenho dois nós diferentes desembocando no mesmo nó.

04:36

E, obviamente, o final é o nó do critique.

04:39

De novo, é exatamente essa topologia aqui. Beleza? Bem...

04:48

Mas como é que a gente monitora essa produção? Nós não vamos voar cegas, tá?

04:53

Nós vamos implementar o Opentelemetry, tá? E aí, pessoal,

04:57

eu vou abrir aqui para vocês a aba do

05:01

Fenix, tá? Do Opentelemetry, tá?

05:08

O Fenix... Aliás, vamos executar, né, pessoal? Deixa eu mostrar aqui para vocês,

05:14

executando primeiro, né? Vamos ver aqui, ó. E...

05:30

A resposta, pessoal, que eu gerei aqui, vocês vão ver,

05:33

ela está o mais detalhada possível para vocês depois poderem

05:37

entender o que está acontecendo em cada item,

05:39

né? Então, aqui, pessoal, a gente tem basicamente os payloads, tá?

05:43

Tem o planejador, né?

05:45

Vocês podem depois ver com detalhes todas as mensagens que foram passadas,

05:48

tá? O que o investigador recebe, tá?

05:51

né? É o que que ele envia para cada um

05:54

é dos dois agentes, olha para você ver relatório

05:57

do agente de estoque remoto, relatório da gente logística, tá?

06:00

né? E depois esses dois resultados a gente envia

06:05

para o critique, tá? Que vai ver que vai compilar essas

06:08

respostas, gerar uma resposta por cliente. Olha lá,

06:11

tudo bem? É uma boa notícia, bem bacana,

06:13

sobre o seu pedido, né? Da Samsung, ou seja,

06:19

O critique, pessoal, ele é como se tivesse sido o copilador das respostas, tá?

06:24

E vocês podem ver aqui embaixo depois a máquina de estado,

06:27

tá? O que aconteceu quando,

06:28

tá? De novo, pessoal, deem uma navegada aqui depois,

06:32

né? Gastem um tempo em cima dessa parte,

06:34

tá? Mas o mais legal é isso aqui, pessoal. Olha só.

06:38

Aqui vocês vão ver, tá?

06:40

Toda a execução.

06:42

É via OpenTelemetry,

06:47

tá? Toda execução via Telemetry de todas

06:50

as chamadas, tá? Olha, olha que legal, pessoal, a gente tem aqui a chamada ao

06:55

sistema do logística, tá? A chamada

07:00

é do MCP, então, pessoal, aqui vocês

07:03

vão poder de fato navegar, entender o que está acontecendo em cada item, tá? Então,

07:09

isso é um espetáculo,

07:10

né? Ou seja, conseguiu capturar todo o trace, né?

07:13

E o link graph da requisição, obviamente, só para lembrar.

07:16

O Link Graph iniciou a requisição pai, né? E podemos ver o formato waterfall.

07:21

Tá, pessoal? De tudo que está acontecendo, tá? Até mesmo as invocações das tools.

07:24

O servidor MCP do banco de dados são traçadas aqui.

07:27

Tá? Depois dêem uma olhada, tá bom?

07:31

Todas as chamadas estão aqui, ó.

07:33

Ó, tudo, está tudo aqui bonitinho, tá? Para vocês depois darem uma olhada, beleza?

07:40

Bem, e obviamente, pessoal,

07:43

também sugiro depois que vocês deem uma olhada na parte dos testes.

07:51

Inclusive, todos os nossos labs têm uma camada de testes muito bem estruturada. E,

07:59

pessoal, se tem algo que hoje documenta melhor o código do que a...

08:05

Porque o próprio texto, o diagrama, enfim, tá? Não que isso não tenha um valor.

08:08

São os testes somente para IA, tá? Porque os testes, para IA,

08:13

ele entende o que se espera e o que se espera

08:16

de entrada e o que se espera de resultado, tá? Com isso,

08:18

vocês vão ver que a IA que melhor conhece sobre os seus

08:22

testes é a IA que melhor consegue manter o seu código, tá bom?

08:26

Isso aí, pessoal. Até!

## Resumo IA

[RESUMO_IA]