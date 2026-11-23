Módulo: Protocolos de Comunicação\
Aula: [Host, Client e Server](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18592)

## Resumo da aula

Espaguete agêntico surge quando prompt, esquema de banco, chamadas de API e lógica de negócio ficam misturados na mesma integração. Nesse arranjo, cada mudança estrutural — como renomear uma coluna ou trocar o provider do modelo — força alterações em vários pontos ao mesmo tempo. O resultado é um sistema frágil, difícil de evoluir e caro de manter. O MCP existe para quebrar esse acoplamento com contratos explícitos e papéis bem definidos.

O MCP organiza a integração em uma tríade: host, client e server. Essa separação cria uma fronteira entre contexto conversacional, conformidade de protocolo e execução de domínio. Em vez de a aplicação conversar diretamente com banco, APIs e prompts sem mediação, cada parte assume uma responsabilidade específica. Isso reduz o impacto de mudanças e torna a arquitetura mais sustentável ao longo do tempo.

Host é a aplicação que detém o ciclo de vida da experiência e o contexto da conversa. Se o host encerra, a sessão e a inteligência associada também deixam de existir, porque é ele quem controla quais servidores participam, qual modelo será usado e quais permissões estão ativas. Em ambiente corporativo, esse papel pode estar em um dashboard, portal de atendimento ou IDE integrada. Ele não é o modelo; é a plataforma que governa o uso do modelo.

O host concentra interface, orquestração e segurança. Ele recebe o prompt, mantém histórico, decide como expor capacidades ao usuário e escolhe para qual LLM encaminhar cada interação. Também aplica guardrails e RBAC, definindo, por exemplo, que um usuário pode consultar dados, mas não executar operações destrutivas. Por isso, o host funciona como o ponto central de governança da arquitetura.

Expor todas as capacidades disponíveis ao modelo em toda conversa aumenta latência, desperdiça tokens e pode estourar a janela de contexto. O host evita isso selecionando, em tempo de execução, apenas os servers relevantes para aquele diálogo. Em uma conversa sobre finanças, faz sentido expor contabilidade; em uma conversa sem relação com RH, não faz sentido abrir esse domínio. Esse filtro dinâmico melhora eficiência e reduz risco operacional.

Client é a camada acoplada ao host que faz a aplicação falar a linguagem do MCP. Ele funciona como um driver: recebe uma intenção da lógica de negócio e a traduz para o formato exigido pelo protocolo. Seu papel não é decidir regras de negócio nem executar ações de domínio, mas garantir que a comunicação aconteça corretamente. Sem essa camada, a aplicação teria de implementar manualmente detalhes de protocolo e transporte.

A conformidade de protocolo inclui serializar requests, controlar identificadores de transação e validar respostas. No cenário apresentado, isso aparece como JSON-RPC 2.0, que fornece uma estrutura padronizada para chamadas e retornos. O client também gerencia o transporte, mantendo conexões via STDIO ou Server-Sent Events, tratando timeouts e acompanhando o ciclo de vida da comunicação. Protocolo e transporte separados da lógica de negócio tornam a integração mais previsível.

Quando um server externo entra em loop, responde com lixo ou falha de forma instável, o client impede que esse problema se propague para o restante da aplicação. Ele isola a conexão defeituosa, interrompe a comunicação e reporta o erro ao host. Esse comportamento é o papel de circuit breaker: conter a falha antes que ela derrube o sistema inteiro. A consequência prática é maior resiliência operacional em ambientes com múltiplos servers.

A analogia do restaurante ajuda a separar responsabilidades sem confundir os papéis. O host corresponde ao cliente da mesa, que decide o que quer; o client é o garçom, que traduz o pedido para o formato que a cozinha entende; o server é a cozinha, onde o trabalho real acontece. Se o pedido vier errado, o garçom valida antes de entregar; se a cozinha falhar, ele comunica o problema sem levar o caos para a mesa. A arquitetura funciona pelo mesmo princípio: intenção, tradução e execução ficam desacopladas.

Server é o componente que concentra a complexidade real do negócio. Ele encapsula acesso a APIs, bancos de dados, sistemas legados e outras integrações, expondo isso de forma organizada para a arquitetura MCP. Isso não significa mover todo o legado para dentro dele, mas criar uma camada que consulta, compõe e entrega capacidades úteis. O ganho está em esconder detalhes internos atrás de uma interface estável.

Resources são exposições de dados que o server fornece ao ecossistema, como documentos, logs, tabelas e contexto estruturado para leitura. Tools são capacidades executáveis, como enviar e-mail, calcular valores, registrar dados ou efetivar uma ação em outro sistema. A distinção importa porque ler contexto e executar efeitos colaterais são operações diferentes e exigem governança diferente. Esses primitivos serão reutilizados nas próximas partes do capítulo.

O server não deve depender do provider nem do modelo que originou a chamada. Ele precisa apenas expor uma interface padronizada, sem saber se a solicitação veio de GPT, Claude ou outro modelo. Essa neutralidade protege a lógica de domínio contra trocas de LLM e contra mudanças internas de infraestrutura, como migrar de SQL para NoSQL. Desde que o contrato MCP permaneça estável, a IA continua operando sem reescrita da integração de domínio.

A arquitetura de contratos define onde começa e onde termina a responsabilidade de cada parte. O host governa contexto, experiência e permissão; o client garante protocolo, transporte e contenção de falhas; o server executa domínio e expõe capacidades. Essa divisão permite que times diferentes evoluam partes distintas do sistema sem interferir diretamente uns nos outros. O efeito arquitetural é governança mais clara, menor acoplamento e evolução mais segura em produção.

## Transcrição

00:00

Fala galera, beleza?

00:02

Natan Pasquarelli na área de novo.

00:04

Sejam bem-vindos a mais um módulo do nosso curso aqui.

00:08

Vamos falar mais um pouquinho?

00:09

Vocês querem me ouvir contando mais um capítulo do

00:12

que a gente tem para aprender aqui? Bom,

00:14

a gente vai falar um pouquinho agora sobre uma das

00:17

coisas muito importantes que a gente precisa aprender aqui.

00:19

A parte de Host, Client e Server.

00:22

Então a gente vai entrar um pouquinho neste capítulo, tá bom pessoal?

00:24

Primeira coisa que a gente tem que pensar é o seguinte.

00:26

Vamos falar um pouquinho sobre o momento que a gente está agora,

00:30

tá? Então, basicamente,

00:31

a gente já entendeu aqui que IA não é mais uma feature isolada, certo?

00:35

Está todo mundo entendendo já que quando a gente

00:37

está falando de um sistema agente aqui,

00:39

a gente precisa entender IA como algo maior do que isso.

00:43

Então, a gente está tentando compreender como é que

00:45

a gente vai fazer essa IA funcionar,

00:47

beleza? Então,

00:48

a gente não pode mais tentar fazer o puxadinho que muita gente está fazendo por aí.

00:52

Não pode ter aquela ideia aí,

00:53

vamos fazer um comparativo aqui com o motor de carro,

00:56

não vamos fazer um motor igual ao do Fusca, né? Ou da Brasília, para quem...

01:01

que dá problema ali com a gasolina,

01:03

que pode cair em cima do motor e pegar fogo e assim por diante,

01:06

vamos fazer uma coisa um pouco mais bem arquitetada,

01:08

vamos começar a montar de um jeito que a gente

01:11

saiba que a gente vai ter uma perenidade, uma evolução,

01:14

e aí os defensores do Fusca e da Brasília devem estar querendo me matar,

01:17

foi só uma comparação,

01:18

eu nem sou um cara que é grande conhecedor de carros,

01:21

mas eu ouvi falar que o motor ali nem sempre funciona tão bem, mas vamos lá.

01:26

Está aí até hoje, está funcionando, mas vamos lá.

01:28

Para a nossa aplicação não ficar uma gambiarra,

01:31

um puxadinho, a gente vai falar um pouquinho então sobre essas estratégias.

01:35

Então nessa aula a gente começa a mudar um pouco esse jogo.

01:38

A gente vai abrir aqui o capô.

01:40

para a gente entender como é que vai funcionar mesmo

01:42

as engrenagens do que a gente quer trabalhar.

01:45

Então a gente vai começar a entender o Model Contact Protocol,

01:48

o que a gente está falando ali do MCP, mais a fundo,

01:51

o papel que ele vai ter aqui em transformar a nossa arquitetura

01:55

em uma arquitetura que é resiliente e mais do que isso,

01:58

uma arquitetura sustentável,

01:59

para que ao longo do tempo a gente não tenha que ficar mexendo toda hora,

02:02

não tenha que ficar estragando o que a gente já fez ou refazendo e assim por diante.

02:07

Então a gente vai parar de fazer um...

02:09

e começar a construir uma plataforma, gente. Vamos lá? Então tá,

02:13

a primeira coisa que a gente tem que pensar aqui é

02:15

A gente tem que diminuir aquela ideia de espaguete agêntico,

02:18

Tá bom? Então, como o Tech Lead, a gente tem que pensar no seguinte,

02:21

O maior inimigo que vocês vão ter aí no seu dia a dia,

02:24

Você que está numa liderança técnica,

02:26

É a falta de capacidade de escala. Não é só memória ou CPU,

02:30

Mas a gente está falando aqui quando a gente... de quando a gente tem acoplamento.

02:33

Se a gente tiver um acoplamento técnico rolando ali,

02:36

A gente não vai conseguir escalar isso. Ao longo do tempo,

02:39

Vai ser muito difícil de a gente mudar essa aplicação,

02:42

A gente conseguir responder o time de marketing no

02:44

Mercado e do negócio e assim por diante.

02:46

Então, antes do MCP,

02:48

Qual era o padrão que a gente tinha? A gente fazia o que eu costumo dizer aqui,

02:53

Que é meio que uma integração artesanal. Você vai fazer uma por uma,

02:57

Você vai fazer aquilo que você precisa basicamente...

03:02

Consultar um banco de dados ali, se você tivesse que consultar um banco de dados,

03:06

Você criava uma função específica para isso.

03:08

Você formatava ali o JSON na mão, na unha,

03:10

E muitas vezes você tinha que ensinar ali um esquema

03:13

De tabela dentro do seu próprio system prompt.

03:16

E daí essa coisa...

03:17

Queria acoplamento, certo? Se você quiser colocar outra tabela,

03:20

Vai ter que fazer outra coisa nesse sentido. Ou seja,

03:22

É artesanal. Se tiver que mudar alguma coisa aqui, mudou o esquema da sua tabela.

03:26

Vai ter que mexer no seu System Prompt e assim por diante.

03:29

Você gera esse acoplamento que não é o que a gente quer.

03:31

Então, o resultado que a gente tem aqui é um desastre. No final das contas,

03:34

Você vai ter um desastre anunciado ali. Se o DBA mudar o nome de uma coluna,

03:38

Capota tudo. Você vai ter que mexer tudo ali e seu Prompt vai quebrar.

03:41

Se você quiser trocar,

03:43

Sei lá, o modelo da OpenAI por um modelo de GPT, que é o da Anthropic. Já era,

03:48

Vai precisar reescrever toda a lógica ali de calling que você fez,

03:51

Porque os esquemas ali vão ser diferentes.

03:53

Então, a gente começa a ter vários probleminhas aqui,

03:56

Vocês estão conseguindo entender? Então,

03:57

Você acaba ali com um código que eu chamo meio espaguete, meio macarrônico,

04:01

E que daí vai acabar atrapalhando o seu dia a dia.

04:04

A lógica de negócio vai estar misturada com a lógica do modelo.

04:06

Bom, para quem já está acostumado aqui com o microserviço, a lógica é a mesma,

04:10

A gente está tentando desacoplar as coisas,

04:12

Tentando fazer as coisas sem uma derrubar a outra, tá?

04:16

Então, a gente tem aqui basicamente, com o MCP,

04:20

A chegada de uma forma para você resolver esse problema.

04:23

Ele vai resolver esse acoplamento separando em três entidades.

04:27

E essas entidades vão ser soberanas toda vez que a gente estiver conversando aqui.

04:32

É o host, o client e o server.

04:34

Vocês que já estão acostumados com microservices, já estão acostumados a codar,

04:37

Vocês devem saber mais ou menos como é que isso vai funcionar.

04:40

Já estão conseguindo entender como é que vai se desenhar na sua cabeça,

04:42

Certo? Então, ele vai criar aqui uma zona de...

04:46

de desmilitarização ali entre os dados e o cérebro. Então,

04:49

ele está criando ali uma zona neutra para você conseguir

04:53

separar o que é a camada de cérebro,

04:56

ou seja, a camada onde vai estar suas regras ali por diante,

04:58

e a camada de dado para você conseguir separar uma coisa da outra, tá bom?

05:02

Então, basicamente, o que a gente está falando aqui é...

05:06

como a gente vai definir contratos claros e como é que a gente vai definir

05:10

onde começa e onde termina a responsabilidade de

05:13

cada aplicação e do protocolo MCP aqui,

05:16

tá bom? Então, onde vive o estado da conversa,

05:19

quem é o responsável por bater na porta do banco de dados,

05:22

como que a gente vai garantir que o servidor MCP está bem escrito ou

05:26

está mal escrito para que ele não derrube a sua aplicação e assim por diante.

05:30

Então, a gente vai começar a aprofundar agora neste assunto, beleza?

05:34

Então vamos lá, vamos definir aqui essa tríade aqui que é o host,

05:37

o client e o server. O host,

05:39

ele é o cara da governança, tá?

05:41

Então aqui ele é a aplicação soberana que vai deter o contexto que a gente tem.

05:45

Então ele vai gerenciar a permissão,

05:46

orquestrar qual modelo utilizar e assim por diante.

05:49

Aqui eu estou dando só um overview dos três pontos que a gente tem que olhar.

05:53

Só que depois eu vou entrar em cada um deles com vocês,

05:56

tá? Então eu vou falar do host,

05:57

do client e do server, e vou falar também da arquitetura de contratos,

06:00

que eu acho importante, que está separado da triade, mas que é importante.

06:03

Então eu vou dar um passant aqui, contar um pouquinho de cada um deles,

06:07

e depois a gente aprofunda em cada um deles, tá bom?

06:09

Então na sequência eu vou falar do host com mais detalhamento para vocês.

06:12

Mas em grandes linhas,

06:13

só para você ter uma linha de raciocínio, host é a governança,

06:16

é o cara que está tendo ali a aplicação soberana e que mantém o contexto, beleza?

06:20

O segundo cara que a gente vai ver logo depois do host é o client.

06:25

Então, ele é o componente ali que vai garantir a conformidade do protocolo.

06:28

Ele vai ter o JSON ali,

06:29

ele vai isolar as falhas que a gente tem com

06:32

o Circuit Breaker ou alguma coisa nesse sentido.

06:34

E o server é o cara da execução, é o músculo do sistema,

06:38

tá bom? Então, ele vai ter ali superpoderes,

06:40

no final das contas, que são as tools e os recursos que a gente tem para,

06:43

de forma agnóstica, ao modelo de IA,

06:45

ele possa executar as ações que a gente quer fazer, beleza?

06:48

E depois a gente vai falar um pouquinho da arquitetura de contratos, então,

06:51

qual que é a separação... aquela área de responsabilidade. Então, por exemplo,

06:55

o time de A vai focar ali na experiência, host.

06:58

O time de back -end vai focar na estabilidade, que é o server, por exemplo. Então,

07:02

a gente tem que ter essa separação de responsabilidade para

07:05

a gente conseguir pensar na arquitetura de contratos.

07:07

Vamos entrar um pouquinho agora em como funciona o host,

07:11

tá? Bom, pessoal, vamos lá então.

07:13

Então, para começar, a gente vai definir aqui um pouquinho o que é o host,

07:17

Tá bom? Então, muita gente ali acaba confundindo o host com o modelo de A.

07:22

Mas no MCP, no final das contas, ele é uma aplicação soberana, tá?

07:26

Você não pode colocar no host um modelo de AI que vai ser usado.

07:30

O host, na verdade, ele tem que ser soberano. Então a gente pode usar, por exemplo,

07:35

um Cloud Desktop, que é um host, ou o VS Code,

07:38

quando a gente tem integrado com o MCP, é um host também.

07:41

Mas, para que a gente consiga entender direitinho aqui numa arquitetura corporativa,

07:45

o host vai ser a sua plataforma.

07:47

É o dashboard de BI que você vai ter ali, por exemplo,

07:50

para um portal de atendimento ou o seu app de vibe coding que você está criando,

07:54

que seja. Então, por que eu chamo ele de soberano?

07:57

Porque o host detém o ciclo de vida.

08:00

Se o host fechar, a inteligência apaga, tá?

08:03

Então é o dono ali da casa quem decide

08:05

quem que vai participar ou não da brincadeira.

08:09

Ele que vai decidir os servidores que podem entrar na configuração aqui,

08:13

entrar na nossa jogada ou não. A gente tem aqui...

08:18

Uma outra coisa que a gente precisa pensar quando a gente está falando do host

08:20

é que ele não é apenas uma moldura do que a gente tem aqui para fazer.

08:25

Ele tem responsabilidades críticas. Aqui eu gosto de separar em três.

08:29

São três responsabilidades que você tem que ter e que você tem que garantir.

08:33

Primeiro é a interface e o UX.

08:35

O host é quem lida com o mundo real. Ele vai receber o prompt,

08:39

ele gerencia o histórico de conversa,

08:40

ele é quem decide como vai apresentar as ferramentas para o usuário.

08:44

Ele tem que fazer também a orquestração do LLM. É o host que vai decidir ali,

08:48

como, sei lá, um mestre de cerimônia da brincadeira,

08:51

ele decide se vai enviar aquele prompt para o Cloud 3.0,

08:55

3.5, perdão, da Sonet, por exemplo,

08:58

ou se ele vai decidir que vai ser um Gemini 1.5 Pro, ou assim por diante,

09:02

para você conseguir decidir ali qual é o modelo que você vai usar.

09:06

Então, ele que vai fazer essa jogada aqui,

09:08

esse routing de inteligência. Então, vamos lá. É o cara que tem o CX ali,

09:12

o X, para conseguir interagir com o mundo real.

09:17

E é o cara que faz a definição ali.

09:20

Ele faz a governança de quem ele vai chamar por trás, tá bom?

09:24

Ele também tem um outro, o terceiro ponto é a segurança.

09:27

São os guardrails que você vai colocar para conseguir garantir a sua aplicação. Então,

09:32

ele é a parte mais importante ali para quem está trabalhando em escala.

09:35

Porque ele vai ter que controlar ali o acesso, o RBAC que a gente fala,

09:39

certo? Então, no final das contas, ele é quem vai falar, o usuário,

09:43

o Nathan, ele vai poder rodar a ferramenta de leitura, por exemplo,

09:46

no SQL, mas ele não tem permissão para dar um drop table, por exemplo.

09:52

Então, ele que vai fazer essa diferenciação. O servidor ali, ele vai...

09:58

a capacidade, mas quem vai dar a canetada final, quem vai decidir se vai,

10:03

se não vai, se pode, se não pode,

10:04

é o host. Então tem essa grande separação, tá bom?

10:08

Então essa é a primeira coisa que a gente tem que falar.

10:10

Ainda falando sobre o host,

10:12

vamos entender esses outros quatro pontinhos que a gente tem que

10:15

Olhar aqui para definir que isso vai funcionar direitinho,

10:18

Tá bom? Então, o guardião de segurança,

10:20

No final das contas, o host, ele é a última palavra em controle de acesso.

10:24

Ele vai definir quais são as ferramentas que

10:26

O usuário vai ter permissão de disparar. Então, por exemplo,

10:29

Imagine que você está cuidando de uma aplicação gigantesca e dentro

10:32

Da sua empresa ou dentro do que você está cuidando,

10:35

Você pode ter acesso para uma pessoa fazer determinada coisa e outra não. Então, por exemplo,

10:41

Pode ter acesso a informações ali do banco de dados

10:43

Ou das informações que você tem referentes ao marketplace,

10:46

Mas não pode ter acesso às informações de RH para não buscar, por exemplo,

10:50

O salário de todo mundo da empresa. Então,

10:51

Aqui você pode fazer essas diferenciações.

10:54

Tanto as que a gente está falando que são mais orientadas aqui à funcional,

11:00

Ou como eu tinha comentado antes,

11:02

Você pode ter uma separação ali mais de pode ler,

11:05

Mas não pode deletar tabela e assim por diante.

11:07

Então, tem esse primeiro passo, tá bom?

11:09

A segunda coisa que a gente tem que olhar é que esse carinha aqui,

11:12

Ele vai ser um filtro de contexto,

11:15

Tá? Então, ele gerencia ali o tráfego, o tráfego,

11:17

Desculpa, tráfego não, né? Pelo amor de Deus.

11:20

Ele gerencia o tráfego baseado em contexto. Então, ele vai fazer o seguinte,

11:24

Imagine que você tem 50 servidores aqui batendo na porta,

11:26

No MCP. Eles estão disponíveis ali para a sua empresa.

11:29

Tem 50 servidores para fazer isso,

11:31

Tá bom? Se você colocar todos eles para o LLM ao mesmo tempo,

11:34

Você vai fritar. A sua janela de contexto vai explodir.

11:38

Imagine o seguinte, está colocando 50 servidores na entrada.

11:41

Você vai aumentar a latência e vai...

11:43

Torrar tokens e explodir a janela de contexto, possivelmente,

11:46

Dependendo do que você tiver aqui, você não vai nem aguentar fazer isso.

11:49

Então, o host tem que ser inteligente para olhar

11:52

A conversa e fazer um filtro dinâmico.

11:56

Nessa conversa sobre finanças, eu vou olhar o cliente do servidor de contabilidade,

12:01

Por exemplo, mas eu não vou olhar o de RH porque não faz sentido.

12:03

O host vai decidir em tempo de execução quais são as

12:06

Capacidades que você vai deixar visível para o modelo,

12:09

Para você não abrir tudo para ele numa tacada só. Ou seja,

12:12

O host não vai ser só um passador de caneta. Tem gente que olha para o host aqui,

12:18

Gente, isso tem que tomar muito cuidado,

12:19

Como só um barramento, um barramento meio tapado.

12:23

Mas não, ele tem que ser mais inteligente do que isso.

12:25

Ele é um filtro de segurança e ele vai ser um

12:27

Otimizador de contexto para garantir a experiência funcionando melhor.

12:31

Então, se o host está robusto,

12:33

O seu sistema de agentes vai funcionar bem. Se ele não está,

12:37

Você está deixando um script meio perigoso dentro da sua rede.

12:40

Então, de novo, ele vai garantir a segurança,

12:43

Filtro de contexto dinâmico.

12:45

entender o que ele vai abrir e o que não

12:46

vai abrir para a janela de contexto daquela conversa.

12:49

Ele vai entender a eficiência e latência.

12:51

Putz, o que eu vou expor para conseguir deixar...

12:53

a latência funcionando e ele vai transformar, querendo ou não,

12:58

ali os scripts agênticos em um sistema governado e seguro para a produção,

13:02

beleza? Isso é o que o host tem que fazer. Bom, galera,

13:06

vamos falar agora um pouquinho do client, tá? Eu gosto de fazer sempre uma...

13:09

Um paralelo para ficar mais fácil da gente entender. Então o cliente aqui,

13:13

eu trato ele como se ele fosse um tradutor,

13:15

um diplomata. Um jeito da gente conseguir compreender mais fácil o que ele faz.

13:19

Então o que ele é no final das contas? Ele é um conector lógico.

13:22

Ele é uma camada que a gente está tendo ali.

13:26

Basicamente o seguinte, vamos pensar assim. A gente decidiu quem manda.

13:29

Quem manda na brincadeira toda?

13:31

O cara que manda é o nosso host, certo? Aí o cliente,

13:36

ele vem aqui e faz o meio de campo. O client é tipo um componente de infraestrutura.

13:42

Eu acho que é o jeito mais fácil da gente explicar ele.

13:44

Ele vai estar acoplado ali dentro do seu host. Ele não é separado.

13:49

Tem gente que às vezes acha que ele é uma entidade separada. Não.

13:53

Ele é uma entidade que está junto do seu host.

13:56

É uma camada lógica que você acopla na aplicação para que,

14:00

no fim das contas, ele aprenda a falar a linguagem do MCP.

14:04

Beleza? Então, pensa como se fosse um drive de um banco de dados.

14:06

Para quem está mais acostumado aí, você não vai escrever o protocolo,

14:09

por exemplo, binário do Postgres, toda vez que você vai usar, certo?

14:12

Não vai fazer isso na mão. Já tem esse protocolo por trás,

14:14

pronto. Você usa o drive que vai traduzir seu comando ali para o Postgres.

14:18

Certo? O Client MCP é como se fosse esse drive. Afinal das contas,

14:22

ele faz a ponte da sua lógica de negócio e

14:25

o servidor de ferramenta que você está trabalhando aqui.

14:28

Beleza? Vocês vão entender um pouco melhor conforme a gente for

14:30

falando dessas três outras coisinhas que estão aqui para baixo, tá? Então,

14:34

a conformidade de protocolo que a gente tem

14:36

aqui é uma das responsabilidades do client.

14:39

Ele faz o protocolo e o transporte da coisa. Então, pense o seguinte,

14:42

imagina que você tem ali um protocolo compliance,

14:46

como se fosse a gramática da brincadeira aqui.

14:48

O client pega a intenção ali do modelo, certo? E ele vai transformar isso...

14:53

Num formato rigoroso. No nosso cenário aqui, vamos colocar um JSON RPC 2 .0.

14:59

Ele está transformando isso em uma linguagem que

15:01

garante que o request vai estar no esquema esperado.

15:06

E ele lida com os IDs de transação e etc. também.

15:09

E valida se o que está voltando do servidor está

15:11

fazendo sentido para ele poder entregar para a LLM.

15:14

Então, ele é esse carinha aqui que faz esse trabalho aqui, que é o protocol compliance.

15:18

Depois, ele vai para o gerenciamento de transporte. Beleza? Então,

15:21

a gente tem aqui como se fosse um encanamento.

15:23

Então, ele que mantém ali o cano aberto, seja uma comunicação STDio ali,

15:29

por exemplo, uma troca de mensagem via terminal,

15:32

Com processo local, assim por diante,

15:33

ou um server-sense event. Então, para cada servidor ali que você vai ter,

15:40

você pode ir por um caminho nesse sentido, tá bom?

15:42

É o cliente que gerencia o ciclo de vida da conexão no final do dia.

15:45

Ele vai lidar ali com os timeouts,

15:47

ele vai garantir que o pacote chega no destino e assim por diante. O cliente, então,

15:51

ele está... Como eu posso dizer,

15:53

ele está acoplado para conseguir fazer essa brincadeira acontecer, tá bom?

15:58

Uma outra coisa que é importante,

16:00

o client como circuit breaker. Então, pense o seguinte,

16:04

aqui entra a visão de arquitetura de alta disponibilidade.

16:07

Imagine que o seu sistema tem 10 servidores MCP plugados ali, beleza?

16:11

Um para Slack, um para GitHub e três para a base de dados interna,

16:15

você tem aí, sei lá, alguma coisa nesse sentido.

16:17

O exemplo ruim, né? Mas acho que é o melhor que eu consegui pensar agora. O host,

16:21

ele não vai falar diretamente com os 10 servidores.

16:23

Ele vai gerenciar as 10 instâncias, não foi isso que a gente falou lá?

16:27

Independente do client. Por que que isso é mais importante?

16:31

Porque se um servidor de terceiros começa a enviar lixo,

16:34

por exemplo, um looping ali, o client vai entrar como circuit breaker.

16:39

Ele vai isolar a falha, vai tirar fora esse carinha aqui,

16:42

e o client pode matar aquela conexão e falar,

16:44

cara, eu estou com um erro nessa conexão, vai reportar o erro para o host,

16:49

sem que a integridade da sua aplicação capote, ou seja, ameaçada. Então,

16:54

isso dá uma segurança operacional para que você consiga resolver o problema.

16:59

Se você fizer de forma manual,

17:00

você não vai ter nunca isso. Então, querendo ou não,

17:02

ele consegue segurar essa brincadeira aqui,

17:04

tá bom? Então, esse é um outro ponto aqui. Bom...

17:07

Deixa eu tentar concluir para vocês o que é o client para ficar bem fácil. Então,

17:11

vou fazer uma analogia que vocês sabem que eu gosto. Então,

17:14

aqui eu coloquei diplomata e tradutor. Vou fazer outra.

17:17

Imagina o seguinte, imagina você estar em um restaurante.

17:19

É bom porque é uma analogia parecida quando a gente

17:21

está falando ali de protocolo de comunicação entre microserviços,

17:24

tá? É como se ele fosse um garçom também.

17:27

Lembra quando a gente aprendeu lá sobre microserviços? Então,

17:30

era como se fosse um garçom, tá?

17:32

Basicamente, o host é o cliente da mesa, beleza? E ele quer comer.

17:38

Ele tá querendo comer, chegou ali com fome, quer almoçar. O cliente é o garçom.

17:43

Ele chega lá e anota o pedido, beleza? Só que ele não vai anotar o pedido,

17:46

o cliente vai falar assim, putz, eu tava querendo comer um frango,

17:50

a parmegiana, com molho e com muito queijo e com arroz e fritas.

17:56

O client vai fazer o seguinte, cara, esse aqui no meu menu ali é o número 503,

18:01

que significa frango à parmegiana. Ele não vai escrever tudo isso que o cara falou.

18:05

É o frango à parmegiana, prato 503.

18:08

Beleza, ele vai anotar de um jeito que a cozinha entende.

18:11

Então ele vai falar, pô, beleza, esse prato aqui é esse aqui.

18:14

Quando passar para a cozinha, ela já sabe o que tem nisso aqui,

18:16

porque ela já está acostumada a fazer.

18:18

Ou, vou dar um exemplo mais fácil, tá? Um McDonald's da vida,

18:21

que você chega lá, antigamente você falava assim, ah, quero o número 1,

18:24

e aí já sabe qual que é lá na cozinha,

18:26

o cara já sabe que 1 é o Big Mac. Mas quando o cara falava na porta Big Mac,

18:29

o cara que tá anotando o pedido já falava, Big Mac é 1, e assim por diante.

18:33

Então ele tá fazendo aqui um deparado que é

18:35

pedido pro que ele vai falar pra cozinha,

18:37

beleza? Então essa é a forma mais fácil de entender.

18:41

E daí depois ele vai lá e vai buscar o prato, certo? Ele foi lá,

18:44

levou pro chefe pra ele cozinhar, o cozinheiro lá foi lá, fez o trampo dele,

18:49

que é o server, depois ele vai garantir que o prato está voltando do jeito certo.

18:53

Aí o cara foi lá, em vez de um frango à parmegiana, colocou um, sei lá,

18:57

colocou um pudim. Ele vai olhar e falar, não,

18:59

não foi pudim que eu pedi, eu pedi frango à parmegiana.

19:01

Então ele vai fazer essa,

19:03

vai garantir que o prato está voltando no formato que precisa.

19:07

Se a cozinha estiver pegando fogo, por exemplo, o garçom vai fazer o quê?

19:11

Vai voltar no cliente e vai falar, olha, seguinte, em vez de...

19:15

Deu chegar aqui, pô, fogo na mesa também. Ele vai chegar e vai falar,

19:18

olha, a gente vai ter que dar uma pausada aqui.

19:22

Posso te trazer uns amendoins que vão ter que jogar água lá na cozinha. Então, basicamente,

19:27

o que ele faz é ele sair de perto da cozinha e não deixar pegar fogo no cliente.

19:31

Então, no final das contas, esse é o paralelo mais fácil de entender,

19:35

tá bom? Ele está fazendo esse meio de campo aqui para as coisas funcionarem.

19:40

Vamos falar do server agora, pessoal. Bom, o server é o que sobrou da brincadeira.

19:44

É o cérebro da brincadeira que é onde está a lógica de negócio.

19:48

São, no final das contas, quando a gente está falando do server, vamos lá,

19:51

voltar na nossa abstração da cozinha. A cozinha estava lá pegando fogo,

19:54

apagamos o fogo dela, vamos entrar nela de novo.

19:57

O server é onde vai estar a lógica do domínio que você realmente tem ali. Então,

20:02

enquanto o host está lá preocupado com o usuário, com o client e assim por diante,

20:06

o server está preocupado com o dado, com o que precisa ser feito,

20:10

com a ação específica. A gente tem que pensar no seguinte,

20:13

o server é o encapsulamento da nossa complexidade de negócio que tem por trás. Então, basicamente,

20:17

tudo que você tinha ali de API, banco de dados, etc.,

20:20

para trás do seu sistema aí, que você pode chamar de sistema legado,

20:24

sistemas acoplados e assim por diante, essa galerinha aí é o que está contido,

20:30

encapsulado dentro do server, tá bom?

20:32

Ele vai encapsular essa complexidade para conseguir entregar. Então,

20:36

não é que você vai pegar o sistema legado e botar dentro do server,

20:38

mas ele é o cara que faz a busca,

20:40

isso e junta para conseguir entregar para o resto que a gente explicou até agora, tá bom?

20:45

Ele mastiga para que a IA consiga trabalhar, fazer o trabalho dela lá, tá bom?

20:50

Então, as responsabilidades desse cara aqui,

20:52

ele tem que garantir ali duas coisas que a gente chama de primitivos, tá? Então,

20:59

encapsular os resources aqui e as tools. Então,

21:02

os recursos e as ferramentas que a gente tem para entregar. Então,

21:06

quando a gente está falando aqui dos resources, o que a gente está falando?

21:10

É como que o servidor vai atuar ali como provedor de dados.

21:13

Então, ele vai expor documentos, tabelas de log, contexto e assim por diante, beleza?

21:19

De um jeito que às vezes a gente tem que até trabalhar ali com as

21:23

organizações semânticas para a IA conseguir ler e entender

21:27

o que ela tem que fazer ali. Beleza? As tools.

21:31

É onde a gente olha o servidor ali,

21:33

por exemplo, que vai fornecer coisas executáveis. Então,

21:36

são aplicações que você consegue executar,

21:38

como disparar um e-mail, realizar um cálculo,

21:41

fazer um registro no banco de dados, por exemplo,

21:43

a contratação de uma viagem por um agente.

21:46

Vai ter uma API lá de efetivação de contratação, alguma coisa nesse sentido.

21:50

Beleza? Então, basicamente, são essas as responsabilidades. Então,

21:55

quando a gente está olhando para isso,

21:56

o que a gente tem que se preocupar?

21:57

A gente tem que ter alguma forma de ser agnóstico aqui nessa brincadeira,

22:01

tá bom? Então,

22:02

para você conseguir dormir tranquilo,

22:04

o servidor tem que ser meio burro em relação ao modelo.

22:08

Ele não pode saber e nem precisa saber se ele está recebendo

22:11

uma ordem GPT-4 do cloud ou de um modelo qualquer,

22:14

o DeepSeq que você inventou aí. Cara,

22:17

ele vai só expor a interface padronizada e que você vai

22:21

conseguir usar na sua lógica interna da API e assim por diante.

22:24

Se você trocar o banco de dados SQL para NoSQL,

22:27

ou, sei lá, otimizar alguma coisa no seu back-end, você pode fazer,

22:31

você só não pode mexer no seu contato de MCP e a

22:34

sua IA vai continuar funcionando ali como se nada tivesse acontecido.

22:36

Então, vai ser meio que uma camada de ACL

22:38

para você conseguir separar uma coisa da outra,

22:41

tá bom? Então, basicamente, é essa a brincadeira, fechou?

## Resumo IA

[RESUMO_IA]