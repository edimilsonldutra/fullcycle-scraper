Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17984)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, no vídeo anterior,

00:02

a gente terminou basicamente com os artefatos que a gente precisa,

00:07

com o arquivo de contract, plan e de spec.

00:09

E agora a gente vai para essa skill,

00:12

que ela é interessante de forma geral, que é a implement e evaluate.

00:18

Essa feature, na realidade, qual que é a ideia dela? É que ela, na mesma

00:24

tacada, ela consiga, na realidade, fazer a chamada do implement feature,

00:31

e também fazer a chamada do evaluator.

00:35

Então, ele cria um ciclo aqui. Então, ele está falando que esse implement evaluator,

00:41

ele é um end-to-end orchestrator for getting a feature from spec, plan e contract,

00:49

e depois pegar um clean evaluator para

00:52

que ele consiga fazer as paradas funcionarem.

00:57

Então, essa que é a ideia inicial. Então,

01:00

ele tem um input de como que as coisas vão entrar, né?

01:03

E depois a gente tem o output no meio de tudo isso,

01:07

tá? Tem alguns pontos que são importantes,

01:09

que é a quantidade de retries, por exemplo,

01:12

né? Como que eu quero isso? Ele vai ficar iterando pra sempre?

01:16

Como é que isso aí funciona no meio de toda essa história,

01:19

tá? Agora, tem alguns pontos importantes aqui pra gente, tá? Que é o seguinte.

01:25

No meio de toda essa história...

01:27

O que eu resolvi fazer para deixar um pouquinho diferente esse fluxo para a gente?

01:32

Toda vez que ele implementar a feature e ter o evaluator no meio,

01:36

e se o evaluator falar não deu certo,

01:39

ao invés dele chamar o cara que implementa a feature,

01:43

a gente vai chamar um camarada que eu chamei de fixrunner.

01:48

Basicamente, ele é um cara responsável por resolver

01:52

problemas de quando uma feature não deu certo. Basicamente,

01:57

o que ele faz? Ele vai ler o relatório, que é aquela feature que o evaluator trouxe,

02:02

e baseado naquele relatório, ele vai fazer o quê? Ele vai fazer a correção, tá?

02:08

Basicamente é isso. Ou ele também tem um modo de fazer a merge de pull request,

02:12

que às vezes a gente está trabalhando em paralelo com várias features,

02:15

tem várias PRs funcionando, então ele é muito bom em fazer merge aqui também, tá?

02:21

Mas o nosso ponto principal é esse modo A,

02:24

que ele vai olhar, na realidade, a feature,

02:27

entender o contrato,

02:28

ver o report para que ele consiga fazer a correção caso tenha algum problema.

02:34

Então aqui dá um exemplo de report para ele e tudo mais.

02:37

Então basicamente o nosso fluxo é implementa,

02:41

testa, deu problema, chama um fixer,

02:44

aí o fixer resolve o problema e aí o evaluator...

02:48

continua verificando e a gente consegue colocar um número

02:51

máximo ali de retries para ele não

02:54

ficar para sempre tentando resolver um problema e às

02:57

vezes não dá para resolver o problema.

02:58

Às vezes tem até um problema na especificação em relação a isso, tá? Então,

03:03

o que eu vou fazer agora? Eu vou mandar esse cara rodar. Então,

03:07

eu vou colocar implement and evaluate e agora aqui eu vou passar.

03:12

Eu gosto sempre de passar o meu PRD, mas agora aqui eu vou passar a minha feature.

03:17

02 aqui para mim, que é o meu sistema de autenticação, tá? Aqui para mim.

03:24

E aqui eu vou dar um enter aqui para a gente. E eu até esqueci de mudar de branch,

03:31

mas ok, galera. Quando a gente for trabalhar ali em paralelo,

03:34

daí a gente cria as work trees. Eu acho que você já está familiarizado com isso.

03:38

Nosso grande ponto aqui realmente é ter o cara que faz...

03:43

a avaliação da coisa, tá? Então,

03:46

ele trabalha em duas etapas e esse cara trabalha como um orquestrador, fechou? Então,

03:52

vou dar um enter agora aqui e vamos ver como é que

03:54

ele vai se sair aí no meio de toda essa história.

03:58

Então, vamos aguardar um pouquinho porque eu acho que

04:00

vai demorar um pouco agora esse processo,

04:02

porque ele vai implementar e depois ele também vai

04:05

ter que verificar e se ele encontrou problema,

04:09

ele vai ter que corrigir, verificar e assim vai.

04:12

Mas se você começa a perceber,

04:14

a gente já começa a entrar num processo autônomo e nesse processo a gente tem gates,

04:20

a gente tem caras que resolvem,

04:23

a gente tem mais especificações ali no cloud

04:28

.md e depois a gente tem uma forma

04:32

de ver o progresso de cada tarefa e a gente aos poucos vai pegando algumas manhas,

04:37

vai melhorando o nosso cloud .md e eu vou falar sobre isso um pouquinho.

04:42

A mais com vocês logo depois dessa tarefa aqui.

04:46

Um ponto importante também a falar é que quando ele começa essa feature,

04:51

eu dou um lock naquela tarefa pra caso alguém queira

04:55

começar uma próxima feature e não cair nela.

04:57

Então se você olhar aqui,

04:58

olha só, escreveu uma orquestração aqui. O que que esse cara funciona, galera?

05:04

Isso aqui é importante eu mostrar pra vocês.

05:06

Enquanto ele tá desenvolvendo aqui, eu tô na feature 2,

05:09

você vai ver... que ele tem um orchestrate .lock,

05:13

isso aqui significa que se alguém iniciar uma próxima tarefa,

05:17

ele não vai iniciar a tarefa 02, porque ela está sendo desenvolvida.

05:21

Mas uma coisa que eu pedi para ele criar, que eu acho que é interessante,

05:24

é um journal, como se fosse um diário, tá? Deixa eu mostrar aqui para vocês.

05:31

E esse journal, o que ele faz? Olha, está rodando isso, essa feature nesse branch,

05:36

começou tal hora, e aqui tem... O que que teve de override, ou seja,

05:41

o que que o orquestrador teve que fazer em cima, que em tese ele não precisaria, né?

05:46

O que que foi feito em relação às outras implementações,

05:50

mas aqui tá todo o ciclo do que aconteceu.

05:53

Ou seja, quando um cara terminar, ele vai lá e marca, olha,

05:57

ele terminou assim. Quando o cara corrigiu, fez assim, aí voltou. Ou seja,

06:01

ele cria como se fosse um diário de tudo que aconteceu,

06:05

né? Pra que o orquestrador...

06:07

não se perca aí no meio e ele consiga continuar de onde que ele parou eventualmente,

06:12

tá? Então, quando eu tô nesse implement e evaluate,

06:18

eu tenho um orquestrador,

06:20

tá? E é um orquestrador simples, se você olhar,

06:23

depois você vai olhar com calma o que tá no prompt dessa skill,

06:28

mas basicamente ele dá um lock somente pra garantir que ninguém vai entrar,

06:32

ele cria esse jornal,

06:34

mas no final das contas o que ele está pedindo

06:36

É que tenha um agente para implementar e tenha

06:40

um outro cara para fazer a avaliação e tenha um

06:43

outro cara para corrigir caso tenha tido algum problema.

06:47

Wesley, por que você não pediu para o cara implementador corrigir?

06:51

Eu poderia ter pedido, mas esse cara fixer, eu...

06:55

foquei no prompt dele muito mais em resolução de problema do

06:59

que fazer toda aquela análise de construção de feature,

07:01

pra eu ter que remodelar o prompt dele, tá? Então,

07:04

por isso que eu acabei de criar esse fixer,

07:06

mas não necessariamente você é obrigado,

07:08

você tem toda a liberdade do mundo pra fazer,

07:10

isso aqui são exemplos que eu tô trazendo e dando aqui pra vocês,

07:14

beleza? Então, vamos aguardar a coisa rodar aí,

07:17

porque provavelmente tem bastante coisa que tá rodando aqui,

07:21

que ele já tá desenvolvendo aqui, ó. Se você olhar... importante. Agent,

07:26

tá vendo? Ciclo 0, implementando a feature 02. Se você olhar,

07:31

esse agent aqui não é agora o agente principal do cloud.

07:36

É um subagente que ele lançou que tem uma

07:39

janela de contexto separada da janela principal.

07:43

Isso aí é importante pra que você consiga entender como que essas coisas funcionam,

07:47

porque senão, se eu tiver um cara que implementa,

07:51

um cara que testa, tudo isso, né? esse ciclo todo,

07:54

na primeira, em toda janela, a janela de contexto,

07:56

ela vai embora, tá? Então, nesse caso,

07:59

a ideia é que a gente trabalhe com subagentes. Então,

08:02

esse subagente, tá? Ele tá trabalhando dessa forma.

08:06

Se você olhar aqui no cloud, eu tenho o main agent,

08:08

que eu tô olhando, mas se eu colocar aqui uma setinha pra baixo e dar um enter...

08:12

eu consigo ver o que esse agente está fazendo agora aqui.

08:17

Então, eu consigo andar entre agentes. Então,

08:20

esse agente agora está escrevendo o .env aqui dele no back-end.

08:23

E se eu voltar aqui para cima no main,

08:26

eu consigo ver o que o main está olhando aqui nesse momento.

08:30

Então, eu consigo ficar verificando,

08:33

andando de agente para agente aqui para agente. Beleza? Vamos aguardar,

08:37

vai demorar um pouco e a gente se fala assim que ele terminar.

08:41

E olha, ele está processando agora aqui,

08:43

o agente está no ciclo zero e dá para ver

08:47

que ele está fazendo os testes com o Playwright agora mesmo.

08:50

Então, o próprio agente implementador está fazendo os

08:53

seus próprios testes por enquanto aqui.

08:55

Vamos ver como é que isso aí termina.

08:58

Aqui já dá para perceber que ele está indo para a parte do Register,

09:01

ele limpou os cookies ali na hora que estava fazendo o login, dá para perceber.

09:05

Então, vamos ver, ele está fazendo aquele teste com o nome Alice,

09:09

que estava lá no contract.md, inclusive.

09:12

E agora, aparentemente, ele está mudando o progresso, o prdprogress.json,

09:19

pelo jeito ele disse que ele terminou a tarefa dele aqui.

09:23

Então, deixa eu olhar aqui onde está o nosso camarada,

09:28

aqui, progress.json, ele marcou aqui como implementado.

09:33

Mas vamos ver o que acontece agora,

09:35

porque a gente vai ter uma outra fase, que é a fase do evaluator,

09:40

e aí a gente vai ver se realmente foi implementado ou não, e etc.

09:44

Mas agora vai depender do orquestrador aqui mandar o

09:49

outro agente ser despachado para a parte de avaliação.

09:55

E olha aqui o que ele colocou agora, olha só, ele terminou,

09:59

deixa eu voltar aqui na coisa, ele terminou,

10:02

deu done, e ele vai retornar como sucesso,

10:05

as 12 fases foram commitadas e ele está atualizando o jornal

10:08

dele e despachando um novo agente que é o evaluator.

10:11

Então, ele alterou aquele jornal dele,

10:14

falando que a feature foi implementada, o que foi feito, desvios, etc.

10:19

E agora tem a parte do evaluator agora aqui. E agora, se você olhar,

10:24

ele despachou evaluator for feature 02 e agora...

10:29

Ele vai já começar lendo o contrato e agora esse cara só vai

10:32

fazer a verificação pra ver se tá tudo certo ou não.

10:38

Bom, pessoal, depois que ele rodou aqui, tá?

10:40

E eu tenho que assumir que ele teve um probleminha com

10:42

o posto local da minha máquina misturado com o Docker.

10:45

Ele rodou, mas ele disse que falhou aqui, ó. Passou 19 pontos e duas falhas, tá?

10:52

E uma falha foi o logout e a outra falha foi o teste E2E. De sign out,

10:59

que eu acho que tem tudo a ver com log out no final das contas, entendeu?

11:02

Então ele está falando que a partir de agora ele tem que chamar

11:07

o Fixed Runner para o ciclo número 1 para resolver esse tipo de problema.

11:11

Então se você olhar agora aqui, a gente tem o ciclo 1,

11:15

a tentativa 1 do Fixed Runner para a feature 02 aqui no nosso caso.

11:22

Então ele pegou uma falha de...

11:24

logout no meio da história e agora provavelmente

11:27

esse nosso agente para resolver esse tipo

11:31

de problema foi lançado e vamos ver se ele

11:33

consegue botar esse cara aí para funcionar.

11:36

Mas é interessante a gente já ver que um errinho que apareceu,

11:40

ele já conseguiu acabar pegando e mandando para um outro agente.

11:44

A grande vantagem de poder ter esses tipos de

11:48

coisa é que você consegue rodar inúmeras sessões.

11:52

Simultaneamente, sabendo que as coisas estão se revisando.

11:55

A desvantagem às vezes é que, às vezes é um erro muito bobo,

12:00

que se você desse um ESC e ajustasse alguma coisinha ali,

12:04

ele funcionaria e você não precisaria soltar um outro agente, fazer outro agente,

12:08

ler o contexto e ir para tentar resolver o problema a partir dali, ou seja,

12:12

você economizaria mais. Então isso é sempre um trade-off,

12:16

então depende muito de como você quer trabalhar.

12:19

De forma geral, eu trabalho muito parecido nesse formato que vocês estão vendo,

12:23

porque realmente eu coloco muita,

12:26

mas muita feature para ser desenvolvida simultaneamente.

12:30

Então, normalmente,

12:31

grande parte da minha dor hoje em dia é em relação à parte de conflitos,

12:35

mas isso aí faz parte, vai ajustando também em relação a tudo isso. Então,

12:40

está aqui o agente que ele tem que resolver esse problema agora.

12:44

Vamos aguardar esse cara rodar, ele está fazendo os testes dele aqui.

12:49

E agora apareceu aqui que o nosso agente, o Fixed Runner,

12:53

ele fez a correção ali pra gente desse cara.

12:57

Então agora o orquestrador ele vai voltar aqui e ele vai falar que tá com o Fixed, né?

13:04

Aquela alteração aqui nossa. É que aqui eu acho que não tá atualizado.

13:11

Mas ele tá mudando. Ah, tá com o Fixed aqui dentro, né?

13:15

Se a gente olhar aqui, a gente tem os prints.

13:19

A gente tem o report do eval desse camarada, né?

13:23

E agora a gente vai ter, no final das contas, o nosso agente avaliador, né?

13:29

O nosso agente de avaliação fazendo todo o processo agora, garantindo que tudo,

13:34

de forma geral, está passando agora depois dos últimos ajustes.

13:39

E enquanto ele avalia, olha aqui o jornal, né?

13:42

Do nosso orquestrador, da nossa feature 02, né?

13:46

Então, ele colocou a feature e etc. E aqui ele falou,

13:49

implementação foi feita com sucesso, 12 fases.

13:52

O avaliador falou que deu um fail. E os critérios de aceitação,

13:58

um bateu certo aqui, de seis,

14:00

e teve uma falha. E falou qual foi a falha nos itens.

14:04

Aí, o Fixed Runner olhou esse item aqui,

14:08

arrumou e deu um commit e falou que nesse commit ele ajustou,

14:12

que foi nesse arquivo no page.

14:16

TSX. Então, aqui está o ciclo 1 de tudo o que aconteceu, o avaliador rodou,

14:21

aí o Fixed Runner falou qual foi o arquivo que ele mudou,

14:26

e agora a gente está guardando o agente que faz o evaluator,

14:32

mais ou menos o ciclo 1, para ele fazer os novos testes.

14:37

E as novas falhas. E aqui ele coloca o que é soft fail, né?

14:42

Que na hora que ele foi tentar rodar o init, o stop,

14:45

a gente teve... Eu tive um problema aqui na realidade,

14:47

galera, que foi com... Eu tinha um Postgres local na minha máquina e um com Docker.

14:52

E na hora que eu rodava o init, em um momento tinha 127.0.0.1,

14:58

e tinha um momento que estava arroba localhost e cada hora ele chamava um.

15:01

Então, provavelmente foi aí que gerou toda a confusão

15:04

e fez um drift e ele anotou aqui,

15:07

inclusive, que teve problemas em relação ao ambiente e tudo mais,

15:13

tá? Mas, basicamente,

15:15

foi por questões disso aí.

15:17

Vamos aguardar agora o agente terminar de fazer a revisão

15:20

e vamos ver se o cara do Fixer,

15:22

ele realmente conseguiu resolver o problema.

15:26

E agora, depois desse fix que esse cara marada fez, olha só, se a gente for aqui,

15:32

a gente tem o status da nossa tarefa como done e o report que ele acabou fazendo. Então,

15:39

o mais interessante disso é que a gente conseguiu realmente

15:42

passar por um ciclo onde a gente teve o implementador,

15:47

a gente teve o cara que avaliou,

15:48

a gente teve um cara que corrigiu, caso deu aquele problema,

15:52

o avaliador viu novamente e aí...

15:54

os pontos resolveram aí no meio da história. Então,

15:58

eu acho que esse tipo de fluxo, pessoal, funciona muito bem.

16:02

É um fluxo que, de forma geral,

16:04

tanto Anthropic quanto OpenAI e outras empresas estão usando muito bem.

16:08

É muito claro que você tem um cara que implementa,

16:11

Um cara que avalia. Um cara que corrige, e aí depende muito se é o mesmo,

16:17

se vai participar da mesma janela de contexto ou não, ou coisas desse tipo,

16:20

Tá? O ponto importante aqui é que você entenda o conceito,

16:24

Tá? Você vai ter, obviamente, acesso a todo esse código,

16:27

a toda essa skill e tudo mais,

16:28

Mas eu acho que o ponto principal no meio de toda

16:31

essa história é que você entenda essa ideia e que,

16:35

obviamente, você não vai precisar sair do zero. Uma vez que você tem essas skills,

16:40

e também existem diversos outros frameworks que você pode utilizar, procurar, mexer,

16:45

Mas eu acho que o mais fundamental é você

16:48

conseguir realmente entender tudo o que está acontecendo por trás,

16:53

o conceito que está.

16:54

Uma vez que você entende isso,

16:56

as coisas começam a ficar um pouco mais simples. Fechou?

16:59

Então é isso aí por esse vídeo, depois vamos jogar,

17:02

gerar mais features em paralelo para a gente ver...

17:06

Várias features sendo implementadas em worktrees diferentes utilizando o Tmunks,

17:11

que eu acho que é o ponto interessante aí do que a gente pode colocar.

17:14

Fechou? Um grande abraço e é isso aí, pessoal.

## Resumo IA

**Abreviações**
*   **PRs**: Pull Requests
*   **PRD**: Product Requirements Document
*   **E2E**: End-to-End (teste)
*   **.env**: Environment (arquivo de configuração)
*   **TSX**: TypeScript XML (extensão de arquivo)

**Resumo**
A aula aborda a funcionalidade "implement and evaluate", um orquestrador ponta a ponta (end-to-end) que gerencia o ciclo de vida de uma feature, desde sua especificação até a validação final. O objetivo principal é automatizar o processo de desenvolvimento e correção de funcionalidades, operando de forma autônoma.

O fluxo inicia com a invocação do orquestrador "implement and evaluate" para uma feature específica (ex: feature 02, sistema de autenticação), utilizando artefatos como `contract`, `plan` e `spec`. Primeiramente, um agente implementador é despachado para desenvolver a feature. Durante este estágio, um arquivo de lock (`orchestrate.lock`) é criado para sinalizar que a tarefa está em andamento, e um "journal" (diário) registra todas as ações e desvios. O agente implementador pode realizar testes iniciais (como com Playwright).

Após a implementação, o orquestrador despacha um agente `evaluator`. Este agente lê o `contract` da feature e executa verificações para garantir que a implementação está correta, gerando um relatório com os resultados, incluindo falhas (ex: falhas em testes de logout ou E2E de sign-out).

Caso o evaluator reporte falhas, o orquestrador, ao invés de chamar novamente o implementador, aciona um agente especializado chamado `fixrunner`. Este agente é focado na resolução de problemas: ele analisa o relatório de falhas do evaluator, identifica o que precisa ser corrigido (ex: um arquivo `page.tsx`), e aplica a correção. O processo é iterativo e configurado para um número máximo de tentativas (`retries`), evitando loops infinitos para problemas insolúveis ou falhas de especificação. Após a correção pelo `fixrunner`, o `evaluator` é novamente despachado para reavaliar a feature, completando o ciclo. O "journal" é atualizado a cada etapa, servindo como um histórico detalhado do desenvolvimento e das correções.

Todo o processo utiliza subagentes com janelas de contexto separadas da janela principal, o que é crucial para gerenciar a complexidade e a extensão das interações. Ferramentas como `work trees` e `Tmunks` (tmux) são mencionadas como facilitadores para o desenvolvimento paralelo de múltiplas features.

**Pontos de atenção**
*   **Limite de Retries**: É crucial definir um número máximo de tentativas de correção (`retries`) para evitar que o processo entre em um loop infinito quando um problema não pode ser resolvido ou indica uma falha na especificação inicial.
*   **Agentes Especializados vs. Agente Único**: A arquitetura com agentes separados para implementação, avaliação e correção (o `fixrunner`) permite que cada agente seja otimizado com prompts específicos para sua função. Isso evita a necessidade de remodelar um prompt complexo para um único agente que teria que lidar com todas as etapas, embora envolva o overhead de iniciar e gerenciar múltiplos agentes. A escolha é um trade-off entre especialização e economia de recursos.
*   **Subagentes e Contexto**: A utilização de subagentes com janelas de contexto isoladas é fundamental para evitar o esgotamento da janela de contexto do agente principal em processos autônomos complexos e de longa duração.
*   **Diário (Journal)**: Manter um "journal" detalhado do ciclo de vida da feature (implementação, avaliação, correção, desvios) é uma boa prática. Ele serve para que o orquestrador possa retomar o trabalho de onde parou e oferece rastreabilidade completa do processo.
*   **Trade-off Autonomia vs. Intervenção Manual**: Embora o processo autônomo seja poderoso para lidar com múltiplas features em paralelo, erros pequenos e óbvios podem, em alguns casos, ser corrigidos mais rapidamente com uma intervenção manual direta do que esperando o ciclo completo dos agentes autônomos. É um balanço que depende do cenário de uso.
*   **Problemas de Ambiente**: Inconsistências no ambiente de desenvolvimento (ex: PostgreSQL local e via Docker conflitantes, diferentes formas de referenciar `localhost`) podem introduzir falhas inesperadas e dificultar a automação.
*   **Conceito é Fundamental**: O mais importante é compreender o conceito por trás dessa orquestração multiagente para o desenvolvimento de software, permitindo adaptar e aplicar esses princípios em diferentes frameworks e contextos, em vez de apenas replicar a implementação específica.