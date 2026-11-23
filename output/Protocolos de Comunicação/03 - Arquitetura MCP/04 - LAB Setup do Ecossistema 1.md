Módulo: Protocolos de Comunicação\
Aula: [LAB: Setup do Ecossistema 1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18595)

## Resumo da aula

Operar servers MCP de terceiros é a etapa que transforma entendimento arquitetural em repertório operacional. Antes de escrever um server próprio, você precisa saber conectar um server existente, validar se ele anuncia capabilities corretamente e observar como o host interage com ele em ambiente real. Retomando o cenário de consultar dados e agir sobre múltiplos domínios, a novidade aqui é enxergar isso funcionando sem costura manual entre integrações. O foco deixa de ser definição de papéis e passa a ser inspeção, comparação e troubleshooting.

O fluxo prático começa subindo um PostgreSQL local em container, com um esquema mínimo de clientes e pedidos, suficiente para consultas realistas. Em seguida, conecta-se o PostgreSQL MCP ao host e valida-se a conexão com o Inspector. Depois, adiciona-se o GitHub MCP ao mesmo host e repete-se a inspeção. A etapa final combina os dois servers em uma única pergunta para observar fanout entre domínios sem escrever código de integração manual.

O PostgreSQL MCP usado aqui é didaticamente valioso porque concentra a leitura do domínio em resources e mantém uma tool poderosa para SQL. Esse desenho torna visível a diferença entre expor contexto navegável e expor execução, conforme a distinção entre resources e tools já estabelecida anteriormente. Cada tabela mapeada como resource facilita exploração semântica do banco, enquanto a tool centraliza a capacidade de consulta ativa. Em produção, porém, esse reference server não deve ser adotado sem cautela, porque foi arquivado e possui vulnerabilidades conhecidas.

O GitHub MCP representa o extremo oposto: zero resources e dezenas de tools granulares para ações e consultas operacionais do domínio GitHub. Esse estilo é adequado quando o valor principal está em operações bem delimitadas, como abrir issue, ler pull request ou pesquisar código, em vez de navegar por um espaço de leitura estruturado. A comparação lado a lado com o PostgreSQL MCP ajuda a decidir quando um domínio deve privilegiar resources, quando deve privilegiar tools e quando vale equilibrar ambos. O ponto central não é copiar um formato fixo, mas entender a semântica do domínio antes de modelar o contrato.

Um server resource-heavy concentra seu valor em superfícies de leitura, normalmente com estrutura navegável e baixo risco operacional para descoberta de contexto. Um server tools-heavy desloca o foco para operações explícitas, com contratos mais granulares e invocação orientada a intenção. Essa distinção não é binária: um mesmo server pode combinar os dois estilos, mas quase sempre haverá uma ênfase dominante. A utilidade prática dessa classificação está em orientar modelagem, governança e experiência de uso no host.

O MCP Inspector funciona como um analisador neutro do protocolo, independente do host final e da linguagem de implementação do server. Ele permite verificar se o problema está no server, no contrato ou na integração do host antes de abrir o código-fonte. Isso reduz diagnóstico por tentativa e erro e cria um ponto comum de observabilidade para o time. Em vez de depender da interface de um produto específico, você inspeciona o MCP diretamente.

O Inspector é composto por dois processos: a interface visual e o proxy que intermedeia a comunicação com o server. Essa separação existe para desacoplar exploração interativa da mecânica de transporte e autenticação, o que também viabiliza uso por linha de comando. Na prática, a UI serve para inspeção manual e o proxy concentra a sessão, o tráfego e os headers necessários. Entender essa arquitetura evita confusão ao depurar portas, tokens e comportamento de conexão.

O proxy do Inspector exige autenticação por padrão e gera um token de sessão usado como Bearer em Authorization. Esse token é persistido no browser para facilitar sessões repetidas, mas continua sendo parte da superfície de segurança da ferramenta. A variável DANGEROUSLY_OMIT_AUTH=true existe apenas para ambientes isolados de desenvolvimento e o próprio nome sinaliza que desativar auth é uma exceção perigosa. Tratar isso como detalhe operacional menor é um erro, porque a observabilidade também precisa ser governada.

A aba Server concentra parâmetros de conexão, como comando, URL, transporte, variáveis de ambiente e timeout, sendo o ponto de entrada para qualquer inspeção. A aba Tools executa chamadas manuais e valida o contrato declarado; se a execução falha ali, o defeito está no server ou no schema, não no host. A aba Resources confirma leitura, MIME type e templates; a aba Prompts mostra o texto final gerado; e a aba Notifications, chamada History em versões antigas, registra o tráfego JSON-RPC em ordem cronológica. Essa última é a principal fonte de prova para debugging de protocolo.

O modo UI é adequado para exploração inicial e depuração interativa, enquanto o modo CLI serve para automação, scripts e pipelines. Em CI/CD, o uso correto do Inspector não é “abrir a interface”, mas validar programaticamente se o server sobe, anuncia capabilities e responde como esperado. Isso transforma o protocolo em contrato verificável antes do merge ou do deploy. Um smoke test simples já detecta regressões como tools ausentes, resources quebrados ou falhas de inicialização.

Tempo de setup, quantidade de tools, latência observada e linhas de glue code são métricas úteis para comparar servers e avaliar custo real de integração. O PostgreSQL tende a responder rápido por executar localmente, enquanto o GitHub herda a latência da API externa. A diferença no número de tools revela estilos de modelagem distintos, não necessariamente qualidade maior ou menor. Já o objetivo de glue code próximo de zero mostra se o contrato MCP realmente absorveu a complexidade que antes ficava espalhada entre adapters.

Glue code é a cola artesanal entre sistemas que ninguém quer manter, mas que cresce quando cada integração exige adapters próprios, mapeamentos duplicados e refatoração em vários pontos. O MCP desloca essa cola para dentro de cada server, onde o time dono do domínio mantém o contrato uma vez e o redistribui para múltiplos consumidores. O efeito arquitetural é sair de um acoplamento próximo de N×N para um modelo muito mais governável. O ganho não é apenas elegância: é reduzir custo de mudança quando contratos internos evoluem.

Retomando o cenário de cruzar dados entre domínios, a pergunta combinada sobre issues do GitHub e pedidos com falha no banco mostra o valor operacional do ecossistema. O host consulta os dois servers, recebe respostas independentes e o modelo constrói uma síntese sem que você escreva um microserviço intermediário para cada par de sistemas. Esse fanout é visível tanto na interface do host quanto no Inspector, onde as chamadas aparecem no tráfego do protocolo. O resultado prático é integração rápida com governança melhor do que a costura manual tradicional.

Um host pronto, como uma IDE ou ferramenta já integrada ao MCP, oferece ergonomia e reduz o esforço de conexão a comandos de configuração. Um client customizado em Python expõe as engrenagens internas, permitindo controlar fluxo, tratamento de erro e uso do SDK com mais precisão. Os dois caminhos exercem o mesmo protocolo; a diferença está no nível de abstração e no objetivo de aprendizado ou operação. Para exploração do ecossistema, vale usar ambos: um para velocidade, outro para entendimento profundo do comportamento real.

## Transcrição

00:00

Pessoal, tudo bem? Vamos para mais um lab, tá? Diferentemente do lab 8,

00:05

em que a gente teve que construir ali o nosso server,

00:12

né? A gente construiu ali a API,

00:15

né? O MCP server que consome a API, né?

00:18

A gente viu a diferença entre o to -call e o MCP server, nesse caso aqui, né?

00:25

A gente vai plugar dois servers MCP de produção real no host.

00:31

A gente vai usar um host custom que a gente fez aqui, que eu disponibilizei lá para vocês,

00:37

mas vocês poderiam plugar em qualquer outro host que aceite MCPs.

00:42

Eu posso até depois mostrar para vocês aqui, de repente,

00:46

no lab, na hora que eu estiver apresentando,

00:49

ver se a gente consegue conectar na nossa própria IDL. Tá bom? Bem...

00:58

tá basicamente são cinco etapas tá é e que

01:03

é assim cara primeiro é subir o postgres local

01:05

no container tá a segunda é o postgres mcp

01:09

no host e mais um inspecto ali a gente garantindo

01:12

que realmente tá funcionando tá depois o github mcp no

01:16

host tá depois a gente vai fazer uma

01:18

tarefa combinada com o fanout dos dois servos ou seja

01:21

né consumindo tanto o github quanto o postgres tá

01:26

E quatro, tá? A gente vai lá para o Spectre, tá?

01:29

Para discutir ali como que debugar de forma avançada,

01:32

tá? E fazer o comparativo de resources heavy versus tools heavy, tá? Tools heavy, ou seja,

01:37

servidores que são resources heavy versus servidores

01:40

MCP servers que são tools heavy,

01:43

ou seja, pesado com relação a tool, tá?

01:45

E depois dois exercícios de avaliação, tá bom? Bem...

01:53

Nossa motivação aqui é a inversão pedagógica. Antes de você escrever um MCP Server,

01:59

que faremos no próximo módulo, que já vai escrever o MCP Server fim a fim,

02:04

você precisa saber operar um server alheio.

02:07

Ou seja, é o vocabulário antes do dialeto.

02:10

Hoje você vai plugar dois servers de produção real,

02:13

tanto em Roche pronto, quanto no nosso...

02:18

tanto em hosts prontos, como uma IDE, um Cloud Code, e por aí vai,

02:25

quanto no nosso orquestrador customizado em Python,

02:27

que a gente desenvolveu para poder ser didático aqui, inclusive.

02:31

E por que escolhemos exatamente esses dois?

02:36

esses dois servers. PostgreSQL e MCP.

02:41

Usaremos o reference server original da Antropica.

02:45

Um aviso importante aqui em 2026.

02:49

que ele foi arquivado e possui vulnerabilidades conhecidas.

02:52

Em produção, prefira forks da comunidade,

02:55

como o das 10 indústrias. Mas para fins de lab, ele é didaticamente perfeito.

03:00

Ele expõe apenas uma tool super poderosa de SQL e

03:04

mapeia cada tabela dentro como um resource distinto.

03:08

Então, de novo, pessoal, aqui é só para fins didáticos,

03:11

que ele realmente é muito resource intensivo.

03:14

E depois nós vamos usar o GitHub MCP, que já é Tools Heavy, o Tools Intensivo.

03:20

Esse é o server oficial em Go, distribuído via Docker pela própria GitHub.

03:26

Ele é o exato oposto do PostgreSQL, ele possui zero resources,

03:29

mas te entrega mais de 60 tools atualmente granulares,

03:33

Como abrir issue, ler por request, pesquisar código e por aí vai.

03:39

Então, o que a gente aprende com isso? Lado a lado,

03:42

você verá os dois perfis arquiteturais mais comuns do mercado.

03:45

Quando chegar a sua vez de desenhar um server para a sua empresa,

03:48

a decisão entre criar uma tool ou um resource já estará clara na sua mente.

03:54

E detalhe, você pode ter um servidor MCP que é equilibrado entre tools e resources.

03:59

Ele pode ter os dois, obviamente. É isso que eu quero dizer. Ele não precisa ser...

04:05

ser só tool ou só resource. No caso do Postgre,

04:08

por exemplo, ele tem tools, mas ele é resource intensivo.

04:12

E para arrematar, o que a gente vai fazer?

04:17

Nós usaremos o MCP Inspector como o nosso Y-Shark.

04:23

Você aprenderá a debugar essas capabilities sem precisar ler

04:26

uma única linha de código fonte do servidor.

04:28

Bem, a pedagogia aqui, pessoal, não é decorar comandos de pacote NPM, tá?

04:34

É entender a mecânica da coisa, assim, como o server se apresenta,

04:38

como o host descobre as capabilities e como

04:40

domínios tão diferentes coexistem em harmonia, tá?

04:43

Quando você for projetar isso para a sua equipe,

04:46

essa imagem mental aqui vai fazer a diferença, ok?

04:50

Então, a gente aqui tem algumas métricas que a gente gostaria de

04:54

endereçar para de fato a gente ter como foco e objetivo do lab,

05:00

que é do docker run até o ícone da tua aparecer no seu chat,

05:05

qual é o tempo de setup.

05:08

Em um laptop com Docker já rodando, a inicialização,

05:11

por exemplo, é imediata. Só para vocês terem uma ideia.

05:14

Quantidade de tools. O Postgre expõe apenas uma tool.

05:17

O GitHub expõe várias. Então, nós vamos ver essas diferenças.

05:22

Outra métrica, latência de chamada.

05:24

Ou seja, a aba History,

05:30

por exemplo, do Inspector, ele mostra os timestamps.

05:34

Vocês vão ver que, por exemplo,

05:36

a tuto Postgre é super rápida, que ela roda localmente.

05:38

Agora, tudo do GitHub depende do tempo de resposta da API externa. Bem,

05:44

linhas de glue code, que é o santo grau, que aí vocês vão ver que é zero.

05:51

Ou seja, eu já falo a métrica e vocês precisam observar essas métricas.

05:58

E tem que bater com isso que a gente está discutindo aqui.

06:01

Exatamente isso. Parece um spoiler, mas não é.

06:04

É ter essa noção de que são pontos importantes que você precisa ter em mente,

06:09

do ponto de vista arquitetural.

06:12

Bem, e aí é o seguinte. Não tem dono.

06:17

O time do banco de dados fez a parte dele,

06:19

o time de A, a sua. Então, a cola no meio apodrece sem manutenção.

06:25

Multiplica com escala. Integrar N sistemas exige N vezes N pedaços de cola.

06:31

Então, é o caos. E quebra silenciosamente.

06:33

MCP absorveu o glue code. A cola vive dentro de cada servidor MCP,

06:37

sendo mantida pelo time dono dele.

06:40

Frase âncora para colar no caderno. O que dói não é escrever adapter,

06:43

refatorar... Isso aqui, na verdade...

06:48

De novo, é o que a gente aprendeu no slide passado.

06:51

Refatorado em N lugares quando o contrato muda. Então, de novo, nesse caso aqui,

06:56

o que a gente tem é exatamente

06:59

essa visão de que nós precisamos usar,

07:05

precisamos entender o como que o MCP serve,

07:10

ele quebra esse N vezes N. E agora é N mais N.

07:14

ou seja, ou um para N, na verdade, melhor dizendo,

07:19

você tem um lugar sendo

07:21

alterado e distribuído para N clientes.

07:29

Bem, o

07:31

nosso Roche MCP, o Roche, a opção é out of the box,

07:37

a gente tem a opção out of the box da Anthropic,

07:39

que a gente poderia usar... um Cloud Code da vida, por exemplo,

07:45

uma IDE, que tipicamente já traz uma interface pronta,

07:52

ele orquestra,

07:53

a orquestração é oculta e adiciona servers via CLI de forma muito ergonômica.

07:59

A Tropic faz isso muito bem com os produtos dela. Cloud Code,

08:03

o Cloud Coworking, por aí vai.

08:07

E a gente vai ter um orquestrador customizado em Python, que a gente que fez.

08:10

É a opção, faça você mesmo, do it yourself.

08:13

Perfeito para quem quer entender as engrenagens internas, que é o que a gente vai fazer,

08:18

que é lidar com o SDK bruto, controlar a vazão de tokens, e tratar erros na raiz.

08:26

é no script desse lado e mostraremos a sintaxe do

08:29

roxo né por ser mais visual para demonstração mas

08:32

nosso código custom client ele faz rigorosamente a mesma coisa

08:36

sobre o capô tá bom

08:37

bem é que mais acho

08:44

que é isso pessoal vamos lá vamos vamos vamos vamos entender agora passar

08:49

parte então etapa um pessoal vocês vão precisar subir o posto igreja local tá

08:54

Ou seja, a gente vai ter um banco de dados real rodando, com esquema mínimo,

08:59

obviamente, que é clientes e pedidos.

09:01

Um realismo suficiente para perguntas interessantes ao host.

09:06

E, pessoal, assim como no outro NAB8,

09:08

vocês vão ver que o nosso Readme está super completinho aqui.

09:12

Aqui tem muito do código que vocês podem usar,

09:15

obviamente, mas lá está explicando exatamente cada uma.

09:20

cada um desses blocos e que momento que ele vai ser executado, tá?

09:24

Isso aqui é basicamente subir na imagem do dock PostgreSQL dentro, tá bom?

09:31

Depois a gente vai configurar o PostgreSQL MCP, tá?

09:34

Que é o seguinte, agora é hora de plugar o banco, né?

09:37

Então o PostgreSQL MCP é o reference server original da Anthropic, tá?

09:44

Então, nós vamos conectá -lo usando a abordagem do host pronto.

09:48

Em seguida, a do nosso custom client.

09:53

Se você já está operando...

09:57

O Cloud Code, tá, cara? É um host pronto, tá bom? Então, assim,

10:01

adiciona -se o server uma única vez via CLI e a partir desse

10:05

momento o host passa a falar SQL nativo com o seu banco,

10:08

tá? Ou seja, zero código de adapter,

10:10

zero SDK, enfim, tá? Super simples, tá bom?

10:17

Então, acho que é um aviso importante aqui.

10:19

O pacote NPM oficial foi arquivado em julho de

10:22

2025 e possui vulnerabilidade à SQL injection documentada, tá?

10:26

Eu estou frisando isso aqui, pessoal, é o seguinte, não faça isso em casa,

10:32

tá? Isso aqui é só para fins didáticos, tá bom, pessoal?

10:34

Nós usamos ele no lado porque o seu perfil resources have,

10:37

muito fácil de instalar, inclusive,

10:39

ele tem um valor didático canônico insubstituível, tá?

10:42

Muita gente, inclusive, usa ele para isso, tá?

10:44

Mas em produção, obviamente, utilize forks ativos da comunidade,

10:47

tá? A gente tem do ZED, por exemplo,

10:50

que é o ZED.dev, tá? Tem aqui o link exatamente para vocês poderem usar, tá? Beleza?

10:57

Bem, aí o que a gente vai fazer? A gente vai usar o MCP Inspector,

11:00

que é a nossa ferramenta de debug,

11:02

para poder entender o que está

11:08

acontecendo ali por debaixo dos panos.

11:09

A gente já usou ele um pouquinho no Lab 8,

11:13

agora a gente vai usar ela de forma mais intensiva.

11:15

Ou seja, só para lembrar,

11:17

o Inspector é o que separa quem consome MCP de quem domina MCP.

11:23

Ela é uma arquitetura em...

11:26

com dois processos, tá? Que tem o CP Spectre, que é o UI, tá?

11:30

E ela tem o MCP Proxy, tá?

11:31

Que você pode usar ela via, inclusive, linha de comando, tá bom?

11:37

Curiosidade, né? As portas, elas vêm no T9 Dialpad Map, né?

11:42

De MCP e MCPP, né? Que é o mnemônico bobo,

11:48

mas ajuda a lembrar quando você estiver debugando, tá?

11:51

Inspector na porta UI e Proxy na porta... na ponta do servidor,

11:57

tá? Então, ou seja, se você abriu esse lab em material antigo,

12:03

que dizia porta 5173, né?

12:05

Que é o padrão do Vite, está desatualizado, né? Porque ele mudou.

12:08

Agora é o 6274 e o 6277, tá bom?

12:15

Alpha é obrigatório, tá, gente? A gente não vai pular isso, tá bom?

12:19

Desde a metade de 2025, tá?

12:25

O proxy passou a exigir autenticação por padrão.

12:28

É um token de sessão aleatória gerado e printado no console.

12:33

E o browser abre automaticamente com o token pré-preenchido.

12:37

O token vai via Bearer

12:42

no header Authorization de cada request.

12:46

Inclusive, eu vou mostrar para vocês o token no Bearer.

12:50

Vocês vão ver bonitinho lá o token fica salvo

12:54

no Local Storage do browser para sessões múltiplas,

12:57

tem até um ID da sessão,

12:59

ele fica salvo lá dentro para que a gente possa executar mais de uma vez,

13:03

obviamente bem

13:05

Agora, se for preciso desligar, esse aqui é o não recomendado,

13:09

a gente seta o dangerously omit alpha igual a true,

13:13

tá? Ou seja, o nome da env var foi escolhido para desacoplar,

13:19

tá bom? Não usem produção, nem mesmo no servidor compartilhado, tá bom? Ou seja,

13:23

não desliguem o alpha, não omitam o alpha,

13:28

tá? Basicamente isso aqui, beleza?

13:32

Então, vamos lá. O Inspector tem cinco abas principais, tá?

13:35

A aba server, que é a configuração da conexão, né?

13:37

Ou seja, é o URL, o comando, é transporte, tá? É se é STDIO, se é streamable HTTP,

13:43

se tem variáveis de ambiente, timeout, né?

13:47

É onde você escolhe o servidor para inspecionar. Tem a aba Tools, né?

13:52

Chama o Matuquags manualmente, sem LLM no meio. Você testa contrato.

13:57

Se a tua quebra aqui, o problema é no servidor, não no host.

14:01

Suporta argumentos JSON com validação contra o esquema declarado.

14:06

Tem a aba Resources, que você vai ler manualmente, inclusive.

14:11

É possível. Você confirma que retorna o conteúdo esperado com o MIME type correto.

14:16

Você lista templates RFC 6570 também.

14:20

E aí, enfim, né? Vocês têm uma gama de flexibilidade bacana aqui com Resources,

14:26

tá? A aba Prompts, ela testa template de prompt com argumentos,

14:30

tá? Você vê o texto final que o servidor gera antes de mandar para o LLM,

14:35

tá? Útil para debug de prompt complexo, tá?

14:38

Tem a aba Notifications, tá, pessoal? É chamada de History em versões antigas,

14:43

né? É a captura do pacote MCP, ou seja,

14:45

todo o tráfego JSON -XCP, lembra que a gente falou lá no início,

14:48

tá? Ele fica gravado em ordem cronológica.

14:53

Initialize, tools/list, tools/call, notification, barra, progress,

14:57

errors e por aí vai. Ou seja, copia, debug e prova.

15:02

Beleza? Então, quando alguém disser que meu servidor está bugado,

15:05

você abre essa aba e prova o que aconteceu no fio.

15:10

De novo, está vendo como as coisas começam a se conectar. Está bom,

15:14

pessoal? Tem dois modos, tem a UI e tem o CLI,

15:17

que eu já tinha dito isso antes.

15:19

O Inspector tem dois modos de operação e você usa cada um para uma coisa diferente.

15:24

O modo UI, ele abre no browser na porta 6274. É o que vimos no Lab,

15:29

a gente já viu no Lab 8, inclusive.

15:32

É bom para exploração interativa, primeira conexão e debug casual.

15:36

Já o modo CLI, você chama via NPX.

15:41

arrobamodelcontextprotocol -specto -cli, ele é programático,

15:45

ele é sem browser, ele é bom para automação,

15:47

para scripts, para CI/CD, para integração com Code Assist e por aí vai, tá bom? Bem,

15:54

pessoal, enfim,

15:56

o resto aqui são detalhes do Spectre, tá?

16:03

Mas assim, pessoal, o que é importante a gente sair daqui, tá? Desse slide, tá?

16:07

Inspector é a única ferramenta neutra do ecossistema MCP.

16:10

Ele funciona para qualquer servidor, oficial ou custom, em qualquer linguagem.

16:14

Ele padroniza o debugging no time, ou seja, quando alguém abrir isso,

16:20

quando alguém abrir isso, o servidor está bugado.

16:23

Passo zero é colar o print da aba de notificações, tá?

16:27

CISG deve rodar Inspecto em modo CLI, tá? Só de curiosidade para vocês, tá?

16:32

É super importante você ter o MCP Inspecto rodando

16:37

CLI quando estiver subindo MCP server na trilha de deploy,

16:44

tá, gente? Ou seja, smoke test de servidor custom novo, Inspecto menos CLI.

16:49

É menos, menos, sei lá, é mais assets de quantas tools e sócios,

16:52

pronto, desaparece. Quebrou o PR, não, mega, tá? Ela não mergeia, tá?

16:57

Bem, alfa obrigatória é segurança da plataforma, não burocracia, tá?

17:02

Documenta no runbook do time, tá? Como recuperar o token quando perder.

17:07

Como rodar o Dangerous Omit Alfa em ambiente isolado de dev,

17:11

tá? E nunca em outro, tá bom?

17:13

E por aí vai, pessoal.

17:17

Etapa 1, tá? Aí nós vamos, inspecionar as capabilities. Então,

17:21

lembrando, pessoal, a etapa zero foi subir, tá?

17:26

Aí eu abri um parênteses aqui para a gente poder falar do Spectre,

17:30

beleza? Então, a gente vai lá, vai configurar, né?

17:34

Etapa um, desculpa, pessoal. Etapa zero foi subir. Etapa um,

17:39

configurar o PostgreSQL. Aí a gente falou do MCP Spectre.

17:51

Pessoal, na verdade, isso aqui é a etapa um do GitHub,

17:54

tá bom, pessoal? Só ter certeza se é isso mesmo esse

18:02

aqui ainda é do Postgres, esse aqui na verdade, ah, desculpa pessoal, perdão, perdão,

18:08

perdão, olha só, deixa eu resolver essa confusão aqui de slides,

18:13

um minuto, um

18:16

minuto, então olha só

18:18

etapa 1, configurar o Postgres aí eu falei do MCP aí

18:29

A etapa 2, inspecionar. Tá bom?

18:33

Só garantir que está coerente.

18:35

Etapa 1, configurar. Etapa 2... Ah, tá.

18:39

Porque é o inspecionar da etapa 1. Perdão, pessoal.

18:43

Sabia que eu estava viajando. Perdão, pessoal. Ainda na etapa 1.

18:47

A etapa 1 é dividida entre configurar e inspecionar.

18:51

Etapa 2, configurar e inspecionar. Perdão, gente. Voltando aqui.

18:58

Tá vendo? Não é só LLM que alucina não, o professor também, tá? Então vamos lá.

19:03

Então, ou seja, aqui, beleza, né? Configurou o MCP Postgres, falei do MCP Server,

19:10

inspecionar. Agora a gente vai fazer a mesma coisa para o GitHub, tá? Configurar o GitHub.

19:15

A diferença é que no caso do Postgres a gente

19:18

teve que instalar localmente em uma imagem Docker,

19:20

tá? É o Postgres, tá? Nesse caso aqui não. Beleza?

19:24

A gente vai também, a gente vai inspecionar, agora que o quadro ficou mais claro,

19:30

nós temos dois extremos arquiteturais rodando juntos.

19:33

O PostgreSQL MCP e o GitHub MCP.

19:36

De novo, pessoal,

19:37

isso aqui é só para lembrar que um é mais intensivo para resources,

19:41

outro é mais intensivo para tools.

19:44

E a leitura é indepotente aqui, né? A leitura é indepotente, no caso do MCP,

19:49

ele vira resource, tá? E a ação com efeito colateral, ela vira tool, tá? Ou seja,

19:55

então é, o PostgreSQL e o GitHub, oficiais,

19:57

tomaram essa decisão arquitetural por você. Então,

20:00

copia o padrão deles quando for construir servers para o seu time, tá? Ou seja, né?

20:08

Usem esses dois padrões arquiteturais, usem esse LAB, gente.

20:12

Eu acho que vocês vão lembrar muito deles aqui para frente.

20:16

Por que um foi implementado de uma forma,

20:19

por que o outro foi implementado de outra e

20:20

como essas duas coisas funcionam ao mesmo tempo.

20:24

Que é esse aqui, que é a tarefa combinada. Dois servers e uma mesma pergunta. Então,

20:29

aqui o ecossistema atinge o seu ápice de valor.

20:31

Uma pergunta que exige dados do banco nacional,

20:34

mais contexto da API do GitHub. Então,

20:36

o orquestrador terá que consultar os dois servers, ler as respostas,

20:40

cruzar as informações e gerar um insight.

20:42

Tudo isso sem termos escrito nenhuma linha de código de integração entre eles. Então, ou seja...

20:52

A pergunta de teste, tá?

20:53

Verifique se há issues abertos no nosso repositório mencionando pedido e

20:59

cruze com pedidos com status de falha na nossa base de dados,

21:02

tá? Se você está operando o host, pessoal,

21:05

basta digitar a pergunta, né? Você verá a interface,

21:08

o fanout acontecendo ao vivo, tá? Se você estiver operando o nosso custom client,

21:13

tá? Digite a pergunta no terminal do script,

21:15

né? E aqui você é o dono do motor e

21:17

a solicitará as ferramentas de ambos os domínios, tá?

21:20

O nosso laço processa a chamada do doc e devolve

21:25

os resultados e obriga o modelo a construir a resposta cruzada.

21:28

O que esperar como resposta final?

21:31

Cotei três issues abertas sobre o pedido 102, 115,

21:35

e só a base de dados tem dois pedidos na

21:38

tabela com status de file que batem com esses IDs.

21:41

E o cliente X foi impactado, algo nesse sentido.

21:44

Então, pausa dramática nesse momento, pessoal. Esse aqui é o principal...

21:48

É selling out do MCP para a sua liderança, para a sua diretoria,

21:55

enfim. Não é sobre a elegância de um protocolo novo.

21:58

É sobre a eliminação pura de adapters legados em produção.

22:04

Sem MCP, seu time perderia semanas escrevendo dois microserviços.

22:09

Um com driver PostgreSQL e ORM e outro REST com a ALF e paginação e rate limit,

22:15

tá? Com MCP a integração teve custo de desenvolvimento basicamente zero.

22:18

Plugou, perguntou, entregou, tá? Que é a ideia do, né,

22:21

que o Atropa que fala que é o SBC, tá?

22:24

Bem, vamos lá. É...

22:32

Antecipei demais. Então aqui, pessoal, aqui na verdade, antes de ir pro recap, né,

22:37

eu vou fazer como eu fiz no Lab 8, tá, pessoal? Na verdade eu vou pausar aqui, tá?

22:42

Eu vou abrir o meu ambiente, vou deixar tudo preparado,

22:46

a gente volta lá. Enquanto isso,

22:48

é o tempo de vocês, nessa pausa aqui, é o tempo de vocês navegarem,

22:54

usarem o Readme, tentarem executar sozinhos,

22:57

fazer a instalação antes de voltar para cá,

22:59

que aqui já vai ser, obviamente, a gente repassando o laboratório junto, tá bom? Bem...

## Resumo IA

[RESUMO_IA]