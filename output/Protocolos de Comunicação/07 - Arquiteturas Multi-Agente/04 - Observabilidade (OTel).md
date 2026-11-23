Módulo: Protocolos de Comunicação\
Aula: [Observabilidade (OTel)](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18625)

## Resumo da aula

Observabilidade torna um sistema distribuído visível durante a execução. Em fluxos lineares, a investigação costuma seguir uma cadeia relativamente determinística de chamadas; em arquiteturas multiagente, o fluxo vira um grafo dinâmico, com delegações, handoffs e decisões em tempo real. Essa mudança aumenta a opacidade operacional, porque uma falha pode surgir no LLM, em uma chamada MCP ou na comunicação A2A. O papel da observabilidade é transformar esse comportamento distribuído em um mapa legível para diagnóstico e operação.

OpenTelemetry é o padrão usado para coletar telemetria sem exigir a criação de um mecanismo próprio de logs e tracing. Ele importa porque registra a execução ponta a ponta e permite correlacionar eventos que atravessam processos, containers e serviços distintos. Em vez de depender de arquivos de log isolados, o sistema passa a expor uma visão unificada da jornada de uma requisição. Isso reduz o tempo de diagnóstico e melhora a resiliência operacional.

Trace é o identificador da jornada completa de uma requisição distribuída. Ele existe para responder o que aconteceu do início ao fim, mesmo quando a execução atravessa múltiplos agentes, ferramentas e serviços. Em um cenário de pedido travado, o trace une o clique inicial, as chamadas intermediárias e a resposta final sob o mesmo contexto. Sem esse identificador comum, a análise vira correlação manual entre logs dispersos.

Span é uma unidade individual de trabalho dentro de um trace. Cada chamada MCP, interação A2A, query em banco ou etapa local relevante pode ser representada como um span com início, fim e relação hierárquica com um span pai. Essa estrutura permite reconstruir a topologia real da execução e medir latência por etapa. O efeito prático é localizar gargalos sem precisar inferir a ordem dos eventos manualmente.

Context propagation é o mecanismo que mantém a continuidade do trace entre componentes distribuídos. Quando um agente chama outro por HTTP, o contexto precisa seguir junto para que o serviço de destino saiba que aquela operação pertence à mesma história. O header traceparent carrega esse vínculo entre processos. Se a propagação falha, o próximo serviço cria um rastro novo e o trace fica quebrado, produzindo spans órfãos e perda de causalidade.

O retorno da observabilidade aparece primeiro como redução de atrito operacional, não apenas como economia direta. Sem tracing distribuído, incidentes exigem arqueologia de logs, comparação de timestamps e investigação sujeita a clock drift entre servidores. Com tracing, a equipe abre uma visualização única e identifica em segundos onde a latência concentrou, como uma chamada LLM travada por 1,2 segundo enquanto FastAPI e MCP responderam rapidamente. Esse ganho devolve foco ao time para evoluir produto em vez de caçar fantasmas em produção.

Retomando o cenário do pedido travado, a camada nova começa quando cada chamada MCP abre seu próprio span. A operação deve iniciar com algo como trace.start_as_current_span(...), marcando explicitamente o começo da unidade de trabalho, e em seguida enriquecer o span com span.set_attribute(...) para registrar metadados úteis, como nome da ferramenta e tipo de entrada. Isso permite medir duração e filtrar execuções por contexto técnico. O ponto central não é logar tudo, mas registrar a operação com identidade e significado.

Na chamada A2A, o problema não é apenas abrir um span, mas transportar o contexto para outro processo. O lado emissor injeta o contexto atual nos headers HTTP com uma função de inject headers, evitando que a correlação dependa de código manual e frágil. O lado receptor precisa ler esses headers com extract request headers antes de continuar a execução. Esse par de operações reconecta a linha do tempo entre agentes e preserva a causalidade do trace através da rede.

Atributos transformam spans em registros consultáveis, não apenas em marcas de tempo. Campos como AgentVersion e ToolName permitem perguntar quais erros ocorreram em uma versão específica, em um agente específico ou em uma integração específica. Sem atributos, a telemetria vira texto bruto difícil de agrupar e filtrar. Com atributos bem escolhidos, o trace passa a funcionar como base analítica para operação e depuração.

Sampling é a estratégia de amostragem usada para controlar custo e volume de telemetria. Em desenvolvimento, capturar 100% das execuções pode ser aceitável porque o objetivo é depurar cada detalhe; em produção, isso tende a explodir armazenamento e orçamento. Uma taxa como 1% já pode ser suficiente em sistemas de alto volume para detectar padrões de erro, gargalos e anomalias sistêmicas. A escolha da taxa depende da escala e do perfil de risco do sistema.

Em uma execução típica, a FastAPI recebe a solicitação coordenada pelo grafo, aciona um agente pesquisador via A2A, esse agente consulta fatos por MCP e depois o fluxo segue para um nó que chama uma LLM para gerar o resumo. A visualização do trace mostra essas etapas em hierarquia temporal, com duração e dependência entre spans. Isso substitui a leitura isolada de múltiplos logs por uma linha do tempo única. Em um grafo dinâmico, essa visualização é o principal mecanismo para entender o caminho real da execução.

Dados pessoais identificáveis não devem ser enviados como atributos de spans ou logs de observabilidade. E-mail, CEP e outros identificadores sensíveis podem circular por plataformas terceiras de monitoramento, ampliando o impacto de vazamentos e criando risco jurídico e regulatório. A alternativa correta é mascarar, anonimizar ou resumir esses dados com hash seguro ou metadados genéricos. Telemetria precisa ser útil para operação sem expor informação crítica.

Cardinalidade explode quando atributos recebem valores únicos demais, como user_id, IDs aleatórios de transação ou chaves altamente variáveis usadas como tags indexadas. Cada valor novo pode gerar séries temporais adicionais e degradar custo, consulta e armazenamento no backend de observabilidade. O padrão seguro é agrupar por dimensões estáveis, como endpoint, versão ou tipo de operação, e deixar a variabilidade extrema fora das tags principais. Sampling complementa esse controle.

Abrir spans dentro de loops extensos cria overhead cumulativo e pode degradar a própria performance que se deseja medir. Em vez de instrumentar 10 mil itens individualmente, instrumenta-se o lote ou a operação agregada na borda do processamento. Essa escolha preserva visibilidade suficiente sem transformar telemetria em gargalo. Observabilidade eficaz mede o sistema sem desestabilizá-lo.

Em arquiteturas multiagente, coordenação distribuída só é operável quando a execução pode ser rastreada entre componentes heterogêneos. OTel fornece a camada que costura MCP, A2A e o grafo de orquestração em uma narrativa única de execução. Isso não elimina falhas, mas reduz drasticamente a incerteza sobre onde elas surgem e como se propagam. Resiliência operacional depende dessa capacidade de enxergar o comportamento real do sistema em produção.

## Transcrição

00:00

Fala galera, beleza? Olha eu de novo, Natan Pasquarelli Freitas na área.

00:05

Vamos falar um pouquinho agora sobre observabilidade, meu povo.

00:09

Então a gente vai, nessa aula,

00:11

falar de um dos maiores pesadelos que a gente tem enquanto arquiteto de software,

00:16

enquanto engenheiro. Uma das coisas que acaba tirando o nosso sono,

00:20

que é qual? A invisibilidade. Por que que tira o nosso sono?

00:24

Porque quando isso acontece e a gente entra no War Room, é aí que a chinela canta.

00:30

A coisa fica complicada para o nosso lado. Então,

00:33

quando a gente está falando de observabilidade,

00:35

o assunto é muito sério,

00:36

muitas pessoas acabam deixando isso para um segundo momento,

00:38

mas eu levo muito a sério porque eu sei a tensão e a dificuldade que é resolver um

00:45

problema quando você está no meio do fogo cruzado e

00:48

sem saber de onde está vindo o tiro.

00:50

Bom, voltando então para cá, o que a gente precisa pensar?

00:54

Quando a gente está falando aqui de

00:56

sistemas de desenvolvimento de software tradicional,

00:59

Basicamente, a gente pode pensar que é como se a gente fosse um motorista ali,

01:03

com o nosso carrinho, numa estrada reta.

01:06

Às vezes ela é meio tortinha, mas ela é uma estrada,

01:09

e você está ali com o seu carro. Do nada, seu carro para.

01:13

Você vai fazer o quê? Você vai olhar para o motor,

01:15

vai olhar para a pista, você consegue ter um fluxo ali.

01:17

Um pouco mais linear e determinístico do que você vai olhar.

01:21

Você tem um passo a passo, quem já trabalhou muito em incidente, em problema,

01:25

em correção de problemas,

01:26

tem ali um passo a passo de como você pode fazer

01:29

para ir separando problemas e resolvendo esses problemas de pouco a pouco.

01:34

Você consegue ver ali um rastro de migalhas mais óbvio no seu dia a dia.

01:38

Mas quando a gente está falando agora de agentes,

01:41

de sistemas multiagentes, não é mais uma estrada...

01:44

A gente está falando basicamente de um bando de pássaros,

01:48

um monte de pássaros voando de um lado para o outro.

01:52

A coisa já começa a mudar um pouco de direção, fica mais difícil de resolver.

01:57

Então, quando a gente está falando de um código linear, código tradicional,

02:01

se eu chamo a função A e ela chama a função B,

02:05

que chama a função C,

02:06

você consegue ter uma linha contínua de execução

02:10

onde você vai resolvendo os problemas.

02:12

Em um multiagente, o fluxo não é uma linha, ele é um grafo.

02:17

E como é um grafo dinâmico para melhorar a nossa vida,

02:20

o agente A pode decidir chamar o B ou não.

02:24

Mas se o agente B achar que o tempo não está muito legal para ele,

02:28

ele pode delegar para o C e daí volta para o A.

02:31

Então é um organismo meio que vivo ali, as decisões são feitas em tempo real.

02:36

O problema, no final das contas, ele vira uma caixa preta.

02:40

Quando algo falha no meio de uma cadeia de quatro,

02:43

cinco agentes, a gente tem um mistério ali de quem é a culpa. O LLM alucinou?

02:48

É o MCP que buscou o dado tudo errado, falhou ali no meio?

02:53

Ou foi uma comunicação ali no Agent to Agent?

02:56

Um handoff que deu algum problema e perdeu um pacote?

02:59

Se você não tiver uma ferramenta de observabilidade,

03:01

você não fica... Você não tem como saber, você vai ficar tateando no escuro ali,

03:06

tentando adivinhar onde que esse seu pássaro se perdeu no meio do caminho ali,

03:10

no meio do seu bando que você estava controlando.

03:13

A solução que a gente vai trazer aqui é usar o OpenTelemetry,

03:17

que já está acostumado,

03:19

sabe que a gente gosta bastante do OpenTelemetry aqui no Full Cycle,

03:22

eu sou um dos grandes...

03:26

entusiastas dele, inclusive. Então,

03:27

quando a gente está falando aqui do OpenTelemetry,

03:29

a gente pode resolver com ele,

03:32

com o que eu vou chamar aqui durante a nossa conversa de hotel,

03:35

que eu simplifico para a nossa conversa,

03:37

beleza? Então,

03:38

assim como um avião que tem a caixa-preta

03:42

ali que está registrando cada movimento que está acontecendo,

03:45

a gente vai usar o hotel para registrar cada pensamento, cada ação dos seus agentes.

03:50

Ele não é só um log. Ele é o GPS, é o radar que transforma o gráfico dinâmico,

03:57

essa visão caótica,

03:58

num mapa legível que a gente vai aprender um

04:01

pouco como trabalhar isso no nosso sistema.

04:05

Beleza? Então, você não vai mais precisar adivinhar,

04:08

você vai olhar para o mapa e vai entender mais ou menos o que aconteceu.

04:10

Esse é o grande objetivo dessa nossa aula. Beleza?

04:15

Depois, então, que a gente desenha ali a arquitetura,

04:18

olha para os design patterns que a gente já conversou,

04:20

a gente precisa garantir que ela seja operável. Então,

04:23

por isso que a gente está aqui agora, a gente já falou ali do MCP,

04:26

do agent-to-agent, já falamos dos design patterns,

04:28

agora a gente vai falar de observabilidade, beleza?

04:32

Então, quando a gente está falando de observabilidade,

04:34

a gente precisa olhar tudo aquilo que a gente definiu e construiu

04:36

e ver como é que a gente olha para isso,

04:38

como é que a gente acompanha no dia a dia.

04:41

Então, a nossa agenda, a gente vai passar aqui por três camadas. Basicamente,

04:45

a gente vai focar no básico bem feito, que é o que a gente precisa ter na cabeça.

04:49

Primeiro, a gente vai falar o vocabulário aqui, trace, span e context.

04:54

Depois, a gente vai falar um pouquinho do ROI, o que você ganha com isso.

04:58

E depois, a gente vai falar um pouco de como fazer,

05:01

como é que a gente instrumentaliza o código MCP, o VGT,

05:08

e assim por diante, e como a gente não quebra o sistema,

05:11

com pitfalls aqui no meio do caminho, beleza?

05:13

Então, basicamente, essa é a nossa agenda, pessoal. E vamos lá.

05:18

Falando dos três conceitos de OpenTelemetry aqui,

05:21

pessoal. Vamos lá. Para dominar ele,

05:24

a gente vai falar primeiro aqui do Trace, mas para dominar o OpenTelemetry,

05:28

a gente precisa esquecer ali os diagramas de arquitetura por um

05:31

momentinho e pensar em como funciona o rastreamento de uma compra online, por exemplo.

05:37

Então, quando a gente está olhando para isso,

05:38

Open Telemetry vai se resumir ali em três grandes palavras,

05:42

Tá? O Trace, o Span e o Context Propagation, beleza?

05:47

Vamos olhar cada uma delas. Primeiro, o Trace.

05:50

Esse carinha aqui que está do nosso lado esquerdo, o Trace.

05:54

Nessa sequência, ele é o código de rastreio, tá? Então,

05:58

nessa estratégia aqui que eu falei para vocês de olhar para uma compra online,

06:01

ele seria como o nosso código de rastreio. O Trace é a história completa.

06:07

Como um código de rastreio de uma encomenda que eu estou

06:09

falando para vocês que você comprou na Amazon lá.

06:11

Não importa se o seu pedido começou no clique do usuário,

06:14

se ele passou pelo galpão central, se ele foi para o caminhão,

06:17

se ele terminou no banco de dados da lojinha,

06:20

não importa. Aquele único código une a jornada inteira. Então,

06:24

você tem o único código que você vai fazer o tracing da jornada inteira.

06:27

É a resposta para aquela pergunta de ponta a ponta.

06:31

O que aconteceu desde o momento em que o

06:33

usuário abriu a boca até o sistema responder?

06:35

Então, esse é o trace.

06:38

O segundo carinha que está aqui no meio, cadê meu mouse? Está aqui. É o span.

06:45

Quando a gente está falando de span, são as paradas do caminhão ali,

06:49

os capítulos que a gente tem. Se o trace é a viagem inteira,

06:52

o span são as paradas que a gente fez ali durante essa trajetória.

06:56

Cada unidade de trabalho isolada vai ser um span.

06:59

Então, quando a gente chama uma ferramenta MCP, por exemplo,

07:02

para buscar um dado ali, isso é um span.

07:04

Quando ele faz uma chamada do agent-to-agent ali para resolver alguma coisa,

07:09

para conversar, para falar com outra gente, é outro span.

07:11

Até uma query simples que ele fez num banco de dados vai gerar um span.

07:15

O detalhe aqui que a gente precisa ter na cabeça é que todo span conhece o seu pai.

07:20

Ele sabe exatamente qual etapa anterior ele se encaixa.

07:23

Então, ele consegue compreender que ele tem hora para começar,

07:27

hora para terminar e a assinatura de quem o gerou.

07:30

Porque daí você consegue gerar uma conectividade entre cada um dos spans. Beleza?

07:34

Depois você tem o terceiro carinha aqui, o terceiro carinha é o Context Propagation,

07:40

Beleza? Esse carinha aqui ele vai ser o bastão de revezamento. Imagina que

07:44

você está em uma corrida de revezamento lá, é esse carinha aqui,

07:46

é aqui que a mágica acontece,

07:49

é onde a maioria dos sistemas que a gente chama de amador acaba quebrando. Como é que

07:55

o agente B rodando no

08:00

servidor separado ali na nuvem sabe que ele fez

08:03

parte da mesma história do agente A. Porque pensa,

08:06

eles estão em lugares separados. Isso vai chamar o Context Propagation.

08:11

Essa propagação de contexto aqui.

08:13

Pensa que é como se fosse um bastão de corrida de

08:15

revezamento que você está passando de um para o outro.

08:18

Ou uma etiqueta de uma caixa de encomenda ali.

08:21

Aquela que você cola na caixa de encomenda.

08:23

Quando o agente A faz uma requisição HTTP,

08:26

sei lá, para o agente B, ele vai esconder ali um caboclinho invisível nos headers,

08:33

que é da requisição ali, que são os trace parents.

08:38

Esses carinhas, esse header é o fio condutor que vai carregar o DNA do trace.

08:43

E daí você vai conseguir fazer todo o mapinha dele.

08:49

Se você esquecer de propagar esse contexto,

08:51

a gente vai receber uma mensagem,

08:52

vai achar que a vida começou nele e vai gerar um log isolado.

08:56

Ou seja, ele vai criar o dele. Então pensa assim,

08:59

na sua aplicação ela sempre tem que passar o bastão.

09:01

Se ela não passar o bastão é porque ela é a primeira.

09:04

E daí ela faz o que? Cria um bastão para passar.

09:06

Então é basicamente essa a estratégia. Então se você não passar,

09:10

imagina que no meio do caminho aqui você quebrou essa passagem de bastão, esse context propagation.

09:14

Você quebrou ela e gerou para o próximo,

09:17

ela vai gerar um log isolado e você vai ter um log órfão.

09:21

Então aqui você vai ter um dado que está perdido no sistema e

09:24

ninguém sabe de onde ele veio nem para onde ele está indo.

09:27

Se isso acontecer, o trace vai ter um problema ali.

09:32

Ou seja, o trace é a jornada,

09:34

o span são as paradas e a propagação de contexto é o que?

09:38

É o fio invisível que costura tudo isso através

09:42

dessa rede que a gente acabou de montar.

09:44

Fechou? E aqui então,

09:46

vamos falar um pouquinho do antes e depois de instrumentar

09:50

quando a gente está falando aqui do OpenTelemetry.

09:52

Qual que é o... O verdadeiro retorno sobre investimento.

09:55

Não vou falar com vocês sobre grana,

09:57

por mais que eu esteja falando sobre retorno sobre investimento,

09:59

eu vou falar com vocês sobre experiência,

10:02

que no final das contas vai virar grana, tá? Ó,

10:07

ao invés de eu ficar lendo esse slide aqui,

10:09

eu vou fazer um teatrinho com vocês que eu acho que vai ser mais legal.

10:12

Então, ao invés de eu ficar contando aqui, ah, bullet 1,

10:15

bullet 2, bullet 3, vamos contar a vida como ela é. Imagina o seguinte,

10:20

primeiro, sem OpenTelemetry. O que significa sem OpenTelemetry?

10:27

Significa que quando você, você que é desenvolvedor, você que já sofreu um órgão aí,

10:32

tenso, que teve que resolver as coisas,

10:34

sem OpenTelemetry, sem observabilidade,

10:36

ainda mais quando a gente está falando de agente, meu filho.

10:39

O que vai acontecer?

10:40

Você vai trabalhar no estilo arqueologia de incidente, arqueólogo de software.

10:48

Você vai fazer o seguinte, dá um problemão, você faz o seguinte, se vai, sei lá,

10:52

tirar um raio X. Que é o OpenTelemetry. Tirar um raio X do problema.

10:56

Você vai fazer uma arqueologia.

10:58

Você vai pegar aquela múmia e vai dissecar. O seu pincelzinho lá.

11:02

Vai ficar tentando entender o que está acontecendo com a sua múmia. Agora.

11:06

Se você tem o OpenTelemetry.

11:08

Você vai lá e vai tirar o raio X. Já sentiu a diferença.

11:11

Primeiro que quando você não tem, você vai se desgastar muito.

11:16

Vai sair sujo, podre, cansado.

11:18

E dificilmente vai achar o problema. Agora quando você tem,

11:22

Você consegue tirar ali um raio-X em tempo real.

11:24

A vida não é linda, vai dar um trabalhinho às vezes,

11:27

mas você vai conseguir chegar num resultado sem perder anos de vida.

11:30

Então, essa é a grande diferença, tá?

11:33

E vamos lá, vamos fazer um exercício aqui da realidade.

11:36

Vamos fazer o testezinho que eu falei para vocês,

11:38

um exemplo. Vou montar aqui com vocês. Então,

11:40

desculpem se eu der uma viajada,

11:42

porque eu achei que vai ficar mais legal fazer assim.

11:45

Então, pensa que, na realidade, você está ali no seguinte cenário.

11:49

O seu cliente ali mandou uma mensagem para você dizendo o seguinte, ó,

11:53

o meu pedido aqui travou no meio do caminho,

11:56

se você não tem hotel, o que vai acontecer?

11:59

Vamos lá, você vai fazer aquela arqueologia que eu falei,

12:02

você entrou no modo de desespero, começa daí, já pega seu café e se prepara.

12:07

Começa aquele jogo do detetive, mas do detetive cego, né?

12:11

Como é que era o nome daquele filme?

12:12

Tinha um filme que era do detetive cego, esqueci. Mr. Magoo, né? Um filme velho.

12:17

Então você vai lá, Mr. Magoo, com toda a sua habilidade,

12:21

abre o terminal do servidor ali do API Gateway,

12:24

vai dar um grip ali, vai procurar pelo ID da requisição. Pegou o ID da requisição.

12:29

Depois você abre o servidor do agente, e daí você vai lá no servidor do agente A,

12:33

baixa o arquivo de log e tenta achar o mesmo ID.

12:36

Já sofreu aí. Conseguiu achar no arquivo.

12:39

Aí você vai lá no servidor da gente B e acha

12:42

ali no servidor da gente B a ferramenta MCP. Sabe o que você vai descobrir?

12:47

Que os relógios dos servidores não estão batendo perfeitamente.

12:51

Cheguei aqui. O relógio do servidor não está batendo.

12:54

Aí o relógio do servidor não está batendo. Por quê? Você teve um clock drift.

12:59

Tem uma dessincronização ali temporal entre as máquinas na nuvem. E isso acontece.

13:04

O logo do servidor A está dizendo que a mensagem saiu 10, deixa eu ver,

13:10

10 e 5 segundos. E o servidor B está dizendo que recebeu a mensagem 10 e 3.

13:16

Aí você fala, pronto, peguei o ID errado, não estou mapeando certo,

13:20

estou com a requisição de uma do outro,

13:21

já se complica tudo. Mas quando você vai ver,

13:24

na verdade... O tempo do computador ali está mentindo.

13:27

Você gasta 40 minutos cruzando coisa de um lado para o outro,

13:29

dado para lá e para cá. Juntando pedaço dessa sua jornada invisível aí.

13:34

Para tentar descobrir o que é. E no final você vai achar o que?

13:37

Que o gargalo era o LLM. Que demorou um segundo a mais.

13:42

E isso vai gerar um baita de estresse. Você vai ficar bravo.

13:47

Vai demorar. Vai ter gente na sua orelha falando,

13:49

E aí? E aí? E aí? Já resolveu? E aí? Falta quanto? E você...

13:54

gastou um tempo do caramba porque você não tinha o OpenTelemetry para te ajudar.

13:58

Pô, vendi bem o OpenTelemetry agora, hein, gente? Vai,

14:01

vamos lá. Então, aqui é uma coisa interessante de você pensar. Agora,

14:07

vamos pensar no cenário com o OpenTelemetry, beleza? Com o OpenTelemetry,

14:11

a gente tem um raio-x cirúrgico. Então,

14:14

quando você está falando com o OpenTelemetry,

14:16

o cliente chega lá e fala, ó,

14:18

meu pedido travou. Você vai abrir a interface do Jagger ali,

14:21

Vai digitar... O trace ID que veio na aquisição do usuário.

14:26

E vai falar o que aparece na sua tela aí.

14:30

Uma linha do tempo perfeita, unificada e cirúrgica. É isso que você vai ver.

14:36

Em 30 segundos você vai olhar o gráfico e vai ver exatamente o que aconteceu.

14:39

Então, ao invés de você ficar ali naquela arqueologia de pega teco de um lado, teco do outro.

14:44

Aqui você já vai ver uma linha do tempo perfeita. E vai olhar o que aconteceu.

14:50

Aconteceu, você vai ver que a FastAPI respondeu em 3 milissegundos,

14:53

que a gente já chamou o MCP em 50 milissegundos, mas aqui,

14:57

nesse nó, a chamada da LLM ali ficou travada por 1,2 segundos.

15:04

Aí você vai ver, putz, foi aqui o problema, foi aqui que eu fiquei com um gargalo.

15:09

Então, isso, na verdade, é o ROI do OpenTelemetry.

15:13

Eu podia ficar aqui falando sobre retorno sobre investimento,

15:17

com o número e o caramba, mas, na real,

15:19

Aqui que está o verdadeiro retorno que você tem quando você usa o OpenTelemetry.

15:26

Então, quando você for falar com o seu time de negócio,

15:28

com a sua área parceira, com quem você atende,

15:30

está aí. Por isso você tem que ter o OpenTelemetry instalado,

15:33

porque daí você vai ganhar anos de vida.

15:37

Então, aqui, quando a gente está falando desse tipo de situação,

15:42

o OpenTelemetry compra saúde mental, vai devolver...

15:47

foco para o time criar produto,

15:48

ao invés de ficar se matando, caçando fantasma dentro de log.

15:51

Então, esse é o verdadeiro retorno sobre investimento do OpenTelemetry. Aqui, pessoal,

15:57

eu coloquei um trecho para vocês verem aqui como é

16:00

que a gente faz a implementação no código mesmo, para vocês verem como é que funciona.

16:03

Mas depois o Isaac vai fazer isso aqui na prática com vocês ali no código,

16:08

que vai ser ainda melhor para vocês entenderem.

16:10

Mas eu queria mostrar um pouquinho para vocês entenderem do que eu estou falando.

16:12

Achei que era mais fácil, tá? Então, vamos lá.

16:15

Aqui a gente está falando de como colocar isso.

16:17

Primeira coisa que você tem que saber é o seguinte.

16:19

Você não precisa reinventar a roda aqui, criar um sistema de log do zero.

16:23

O OpenTelemetry já dá um padrão ali pronto para consumo via SDK.

16:27

A gente só precisa usar ele.

16:28

Então a gente vai traduzir ele aqui em três bloquinhos, tá?

16:31

Então a gente criou aqui três bloquinhos para a gente.

16:34

O primeiro bloquinho vai ser aqui na sua MCP,

16:37

beleza? O segundo vai ser numa comunicação, uma chamada aqui,

16:41

agent to agent. E o terceiro bloquinho,

16:45

vai ser na comunicação com o servidor aqui do Agent to Agent.

16:50

Beleza? Então, vamos lá. Primeiro bloquinho que a gente vai falar.

16:54

Quando o seu agente decide chamar uma ferramenta MCP,

16:57

que é esse primeiro bloquinho, por exemplo, para consultar um CEP,

17:00

um banco de dados ou qualquer coisa assim, ele vai abrir uma nova subtask,

17:04

certo? O que o código faz ali com essa parte aqui?

17:09

Trace, start as a current span. Aqui,

17:12

o que ele está fazendo é como se ele estivesse apertando

17:15

um play ali no cronômetro e abrindo uma nova pasta no arquivo.

17:20

Aí ele está fazendo essa lógica aqui, beleza?

17:23

Então, aqui você está dizendo, comecei a executar a tarefa X, a ferramenta X.

17:27

Logo em seguida, você usa aqui o span set attribute,

17:33

certo? set input set. Você está dizendo aqui...

17:39

Como se você estivesse colocando um post-it nessa pasta

17:42

aqui com os metadados que são importantes para ela. Então,

17:45

esse span vai garantir que o sistema vai saber exatamente quanto tempo

17:48

aquela ferramenta específica demorou para rodar e qual foi o insumo dela.

17:52

Então, aqui você está cronometrando o tempo dessa brincadeira aqui.

17:56

Fechou? Então, esse é o primeiro passo.

17:58

Vai, simples, né, gente?

18:00

Na comunicação do agent-to-agent,

18:02

que nós estamos falando aqui na chamada, segundo pedaço.

18:05

Agora, no agent-to-agent, o agente A está precisando falar com o agente B.

18:09

O que está rodando em outro container,

18:12

o agente B que está rodando em outro container, certo?

18:15

Daí, esse agente B está rodando em outro container, em outro servidor,

18:19

talvez até em outra nuvem, dependendo. Vamos extrapolar.

18:23

Como é que a gente passa o bastão do rastreio?

18:26

É aqui que a gente precisa dessa função aqui, que é... Cadê meu mouse? Inject headers.

18:34

Essa função aqui, ela vai te ajudar nisso.

18:37

Pensa que é como se fosse um sistema de despacho de uma transportadora.

18:40

Quando você vai enviar um pacote,

18:42

você coloca a etiqueta de rastreio, que é essa aqui.

18:45

E dentro do bolso invisível dessa caixa de papelão aqui.

18:50

Então, você está colocando essa etiqueta aqui para ele seguir a vida.

18:53

Antes de entregar ela para o entregador.

18:56

O inject vai pegar o contexto do rastreio atual

18:59

e vai injetar dentro dos headers do HTTP,

19:01

da requisição que vai sair pela rede. Então, ou seja, está propagando isso.

19:06

Você não precisa ficar gerenciando manualmente.

19:08

A biblioteca já está fazendo isso para você.

19:10

Ela está pegando a sua etiqueta.

19:12

Por que eu falei que ela não cola na caixa? Ela coloca no bolsinho.

19:17

Que eu pensei num bolsinho para ser nosso exemplo.

19:19

Porque depois ela pega isso e leva para o header. Então,

19:21

ela está levando isso para o header HTTP e essa

19:23

etiqueta vai passando de um lugar para o outro.

19:26

Como é uma caixa, não dá para fazer essa simulação. Mas é basicamente isso, tá?

19:31

Na comunicação AGIT com o servidor, que é a parte de baixo aqui,

19:35

a gente tem uma outra estratégia.

19:39

Do outro lado da linha ali. Então, a gente passou.

19:41

Está do outro lado. O agent B recebeu a requisição HTTP.

19:45

Se ele só ler o body,

19:47

ele vai achar que é o começo de tudo e vai criar um rastro isolado.

19:50

Aquilo que eu falei para vocês, ele vai começar do zero.

19:52

Vai falar, opa, log orphan, deixa eu ser o pai dessa criança. Para evitar isso,

19:57

a gente vai usar a função de extract request headers aqui. É esse carinha aqui.

20:05

Isso vai ser como se você estivesse avisando ele que, quando você chegar ali com...

20:12

com essa caixa na sua casa,

20:14

você vai ter que pegar a etiqueta de rastreio oficial e dizer,

20:18

ah, então, esse pacote aqui faz parte daquela viagem que começou lá no agente A.

20:23

Então agora eu sei do que está acontecendo,

20:25

é o bastão sendo passado de um lado para o outro, então ao fazer isso,

20:29

você reconecta a linha do tempo ali, tá bom?

20:33

Então essa é a grande sacada quando a gente está falando disso. Fechou?

20:37

Só para vocês terem uma ideia de como fica o código que eu quis trazer para vocês.

20:40

Assim fica mais fácil vocês entenderem. Bom, de novo,

20:43

não precisa criar do zero. Já existe. Só usar, meu povo.

20:47

E vamos falar do checklist de instrumentação. Beleza? Então,

20:52

vamos começar a pensar nas coisas que a gente quer recomendar para vocês. Então,

20:57

quando a gente está falando de engenharia de sistemas confiáveis,

21:00

a gente tem que ter esses checklists para ajudar a gente.

21:03

Então, o que eu queria trazer para vocês?

21:07

Vamos quebrar ele em alguns pedaços aqui. O primeiro é o seguinte, é obrigatório.

21:12

O primeiro ponto que a gente tem que ter é a obrigatoriedade. Se não tem spam,

21:17

não existe. Primeira coisa que a gente tem que ter na cabeça. Toda chamada de rede,

21:22

seja uma requisição agent-to-agent ou um MCP,

21:26

vai precisar, obrigatoriamente, abrir um spam.

21:31

Então, pensa que é como se fosse um sistema de crachá de uma empresa.

21:34

Se o funcionário entrou no prédio, passou pela catraca, foi para a sala,

21:38

mas esqueceu de registrar o crachá para o segurança da empresa,

21:42

ele simplesmente não esteve lá, certo? Como se ele não tivesse passado.

21:46

Então, é bater o ponto. No nosso sistema multiagente,

21:50

o sistema A, o agente A, perdão, chama agente B.

21:54

Por debaixo dos panos, se você não abriu um spam nessa chamada,

21:58

essa transação é um fantasma. Ela vai acontecer, consome processamento, gasta token,

22:03

mas é invisível no seu radar. Se deu um erro ali, lascou-se.

22:07

Você vai procurar o culpado no lugar errado. Você não vai saber o que aconteceu.

22:11

Então, esse é o primeiro ponto. Se não tem spam,

22:13

não existe. Tem que ter spam, certo?

22:16

Outra coisa. Dois, os atributos.

22:20

O poder dos metadados é muito grande e importante, tá bom? Então aqui,

22:27

colocar um spam sem atributo é a mesma coisa que ter

22:30

uma gaveta cheia de papel que não tem nenhuma etiqueta,

22:33

você não sabe o que é o que, não sabe qual é a informação que tem ali,

22:36

você vai ter que ficar abrindo uma por uma.

22:38

Para achar, você vai precisar de muito esforço, vai ser desumano,

22:43

vai ser o mesmo caos que você tinha antes.

22:45

Os atributos como o `AgitVersion`, o `ToolName`,

22:49

eles vão funcionar como as etiquetas de metadados de uma foto do que você está vendo,

22:54

uma foto digital do troço.

22:56

Ou como se fosse o código de barras de um produto,

22:59

que ele responde ali o contexto do que está rolando.

23:02

Quando um erro acontece, você não quer saber a pena...

23:06

você quer que aconteça um erro, você quer saber,

23:07

você quer perguntar ali quais foram todos os erros que aconteceram,

23:12

especificamente na versão 2.0, do agente de vendas,

23:15

usando a ferramenta MCP e assim por diante, você quer saber o que está acontecendo,

23:20

você quer agrupar os erros, saber onde está acontecendo a brincadeira.

23:24

Então, se você não tiver atributos,

23:25

seu log vai ser só texto bruto, sem uma etiqueta, sem um rótulo.

23:31

Ele vai virar ali um banco de dados inteligente, quer dizer, com o

23:36

O bloco, com o rótulo, perdão, ele vai gerar,

23:39

Vai virar ali um banco de dados inteligente que você

23:41

Consegue consultar depois e entender o que está acontecendo.

23:44

Então, todos os atributos ali,

23:47

A gente vai ter que ter ali esse atributo em todos os spans que a gente tiver, beleza?

23:55

Outro ponto que a gente tem aqui é o sampling. Então, ali é a parte de amostragem.

24:00

Quando a gente está falando de sampling, o que a gente tem que pensar?

24:04

É um erro que faz muitas startups irem à falência. Ou,

24:08

Quando a gente fala de um erro de muitos engenheiros, tomar aquele puxão de orelha.

24:13

Você acha que você tem que gravar 100 %

24:16

De absolutamente tudo que aconteceu em produção.

24:18

Se você fizer isso, você está lascado.

24:22

Você tem que pensar em um sampling por amostragem. Então,

24:24

Como um sistema de radar rodoviário, ou uma auditoria de qualidade da sua empresa,

24:30

Se você tem um sistema que tem muita coisa rolando,

24:32

Milhões de aquisições e assim por diante e vai querer gravar tudo,

24:36

Cada milissegundo, cada log bruto, você vai torrar a grana do caramba.

24:40

Então, 100 % do tráfego em produção não dá para gravar.

24:44

Seu custo vai ser caótico. Vai explodir ali seu custo de armazenamento.

24:50

Então, quando a gente está falando...

24:52

Em desenvolvimento, você quer dar 100 % de visibilidade

24:55

Porque está testando e precisa debugar cada detalhe, beleza.

24:58

Em produção, você vai aplicar um sampling de 1 %

25:02

Ou o que a escala permitir, ali mandar. Então,

25:06

Quando a gente fala de 1 % em um sistema de alto volume,

25:10

Já é mais do que o suficiente para você pegar padrões de erros ali,

25:14

Gargalos, performance, anomalia sistêmica e assim por diante. Então,

25:17

Aqui já é o suficiente para você conseguir fazer isso.

25:21

Ou seja, aqui são as formas como você tem que fazer para a coisa dar certo. Fechou?

25:31

E vamos ver aqui como é a anatomia de um trace real,

25:35

Um exemplinho para a gente ver. Então,

25:37

Se a gente olhar para essa tela aqui,

25:39

Você vai começar a ver como é que essa teoria se materializa ali na prática.

25:43

Vocês estão vendo aqui, não é um log de texto comum, é uma linha do tempo.

25:48

É como se fosse alguém que consegue ver ali uma...

25:53

Uma lógica forense da coisa, talvez, de uma requisição. Então, vamos ver junto aqui. Então, começou aqui.

26:01

FastAPI recebeu um pedido do Landgraf. Ela assumiu o fluxo.

26:05

O sistema chama a gente pesquisador via agent-to-agent.

26:10

Aí ele chamou o pesquisador via agent-to-agent que utilizou

26:16

O MCP para buscar os fatos diretamente no banco de dados.

26:19

Quando ele chamou o MCP aqui para buscar...

26:22

As coisas aqui no banco de dados são os fatos, beleza?

26:26

Então, aqui é que ele está fazendo essa busca.

26:32

Em seguida, o fluxo vai passar para o nó de geração de resumo acionando uma LLM,

26:38

Beleza? Então, ele foi lá e mandou para o nó e chamou a sua LLM.

26:43

Pensa nisso aqui como um gráfico de telemetria do que está acontecendo.

26:48

Então, basicamente, essa é a estratégia, certo?

26:52

Antes, quando você não tinha o Trace, se o sistema estivesse lento,

26:57

Você ia ter que estar no escuro, você não ia saber muito bem o que está acontecendo.

27:01

Vai ter que abrir 10, 15 arquivos ali, tentar alinhar os timestamps na unha,

27:05

Você não vai ter essa coisinha bonitinha aqui,

27:07

Você vai ter que alinhar na unha,

27:09

Vai passar horas debatendo para descobrir onde está o gargalo.

27:13

É um chute. Com o Trace, rapidinho,

27:15

Você abre lá e a própria hierarquia aqui, como você olha,

27:19

A organização aqui já está te contando o que está acontecendo.

27:22

Certo? Então, basicamente, essa é a estratégia, beleza?

27:28

Aí chegamos no último slide, que era o que eu estava doido para chegar com vocês,

27:32

Que eu acho que é aqui onde eu tenho mais

27:34

A compartilhar de conhecimento do dia a dia,

27:38

Que é uma das coisas que eu acho mais importantes,

27:41

É a gente mostrar o que não fazer,

27:42

Mais do que falar o que fazer, é o que não fazer, certo? Por quê?

27:47

Porque o que não fazer é o que a gente já errou, né? A gente já passou por isso,

27:51

Não precisa todo mundo fazer o mesmo erro. Então, vamos lá.

27:54

Primeiro deles que eu queria falar com vocês. Esse carinha aqui, o primeiro.

27:57

Que é o quê? Dados pessoais identificáveis. Cara, não dá, né? Aqui,

28:03

Você vai ter um incidente jurídico na sua mão. Então, aqui,

28:07

Ao invés de você colocar a Sponset Attribute User E-mail com o e-mail real, então,

28:12

Você vai colocar o e-mail real do carinha, ou colocar aqui o CEP dele.

28:19

Abertão, bonitão aqui, tu tem que fazer o quê?

28:21

Tu tem que pensar diferente, né?

28:23

Porque isso aqui que você tá fazendo é a mesma coisa que, sei lá,

28:25

Colocar aquela portona de cofre na sua casa com a chave tetra,

28:31

Sei lá, muito boa, aquela chave difícil de abrir.

28:35

Tetra nem é tudo isso, né, gente? Mas finge que é, que eu não sou chaveiro. Então,

28:39

Uma chave ferrada ali e deixar a chave presa na porta,

28:42

Gente. Cara, não dá, né? Você foi lá,

28:45

Organizou tudo bonitinho e deixou ali o e-mail do seu cliente aberto.

28:51

Deixou aqui o CEP dele aberto.

28:53

Tu tem que mascarar essa brincadeira aqui. Então aqui o certo é você não...

28:59

Deixar aberto. Por que é fatal?

29:02

Porque o dado de telemetria não vai ficar isolado no seu servidor.

29:05

Ele vai viajar nas plataformas de observabilidade de terceiros na nuvem.

29:09

Ele vai ficar passando no Datadog, no que você for usar ali.

29:13

Se houver qualquer vazamento, o acesso lá no Datadog da vida...

29:19

Você não vai ter só um bug de software, você tem um incidente jurídico,

29:24

Um LGPD, um processo, e tem que atualizar seu LinkedIn, meu querido.

29:28

Então aqui fica a dica para você, mascarar essas coisas.

29:31

A forma correta é você não mandar o dado cru, gera uma pegada anônima ali,

29:37

Usa um hash seguro, ou limita a meta dado genérico,

29:42

Não vai colocar a coisa abertona ali,

29:45

Certo? Então, o primeiro é esse aqui. Não trafega dado de cliente,

29:51

Dado que é crítico, por aí, certo? Nem no log, não trafega no log,

29:58

Pelo amor de Deus. Então, esse é o primeiro ponto, certo?

30:02

Segundo ponto, explosão de cardinalidade.

30:06

Esse cara aqui acaba com o seu orçamento. Então,

30:08

Se eu usar ID muito único,

30:11

Muito único e infinito ali, como um...

30:15

User ID, a transação aleatória ou um ID exato

30:19

de cada usuário individual com tag de indexação,

30:22

você vai se lascar. Imagina o seguinte,

30:26

imagina que você é dono de uma biblioteca lá,

30:28

ao invés de organizar os livros da biblioteca por sessão,

30:31

igual todo mundo faz, é história,

30:33

tecnologia, é ficção, é geografia,

30:35

você decide alugar uma estante para cada segundo que passa no seu reloginho ali.

30:42

O sistema, ele vai...

30:44

entrar em choque, certo?

30:46

Porque cada valor único gera uma nova série temporal e vai ser

30:50

uma nova série temporal independente ali no banco de dados.

30:53

E daí, se ela estiver independente no banco de dados de monitoramento,

30:56

se você taguear ali milhões de requisições com vários IDs dinâmicos,

31:02

a cardinalidade vai explodir o banco de dados de telemetria,

31:06

vai dar aquela engasgada e a consulta trava e,

31:09

por último, a coisa mais importante de todas,

31:12

a sua... Conta do seu provedor aí de nuvem,

31:15

vai explodir. E daí você também vai ter que atualizar seu LinkedIn.

31:21

Então a regra aqui é agrupar por endpoint e confiar ali em taxa de amostragem,

31:27

que é o sampling que a gente falou antes.

31:29

Beleza? Então esse cara aqui também, muito cuidado.

31:32

Vamos para o Trace. Dentro de looping. Esse é o melhor.

31:36

Então quando você coloca um trace dentro do looping.

31:38

Ele vai ser um veneno para você.

31:40

Então imagina que você está colocando ali a abertura de um span.

31:44

Dentro de um looping. Que vai rodar ali 10 mil vezes. Por exemplo, para processar.

31:49

Os itens de uma lista, um por um.

31:50

Você está recebendo uma lista. Tem um looping. Você mete seu

31:54

seu. Seu span ali dentro desse looping. Então é como se você estivesse entrando ali,

32:02

no museu e a segurança te exigisse ali para parar e abrir a mochila e

32:06

todos os seus bolsos a cada passo que você dá dentro da mesma sala,

32:09

nem saiu da sala, você tem que fazer isso várias vezes,

32:11

ao invés de você fazer uma revista rápida ali na entrada,

32:14

a cada passinho que você dá,

32:16

vai revistar de novo. Então aqui é fatal

32:20

porque se você abrir e fechar o span ali,

32:24

tem um custo computacional que vai ser intrínseco. Então, se você tiver

32:29

e sem contar que você vai ter um overhead a cada 50 microssegundos por operação.

32:34

Se você multiplica isso por 10 mil execuções em looping,

32:38

você vai queimar meio segundo fácil, só dentro da burocracia de telemetria.

32:43

Vai destruir a performance do seu agente, que, vamos lá,

32:48

já não é fácil de manter. Então, a forma correta...

32:51

é você instrumentar o lote, o batch inteiro que você está recebendo,

32:55

em vez de ficar trabalhando isso dentro, trabalha na borda.

33:00

Nunca trabalhe os itens individualmente dentro de laços de repetição,

33:05

pelo amor de Deus.

33:06

Então aqui, pessoal, a moral da história que eu queria trazer para vocês.

33:10

Monitorar é essencial, é importante,

33:13

mas também monitorar sem critério arquitetural pode te gerar um baita trabalho.

33:18

A monitoração...

33:19

é para você conseguir resolver os problemas no dia a dia,

33:22

certo? De forma fácil, de forma rápida,

33:26

entender comportamento e assim por diante.

33:28

O que ela não pode fazer é ela ferrar todo o seu sistema.

33:31

Então, o que não fazer, presta bastante atenção,

33:34

pense na sua monitoração com bastante calma,

33:37

cuidado, faz direitinho que vai dar bom, beleza? Um abraço, até a próxima!

## Resumo IA

[RESUMO_IA]