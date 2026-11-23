Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17792)

## Resumo da aula

Batch Mode é um modo de execução que automatiza a geração de especificações de múltiplas features em paralelo. Em vez de conduzir manualmente a entrevista de refinamento para cada feature, o processo passa a aceitar por padrão as recomendações sugeridas pelo agente. Isso reduz o tempo operacional quando o objetivo é produzir várias specs de uma vez, especialmente em cenários organizados por waves. O custo dessa automação é a perda de revisão interativa durante a geração, por isso o resultado pode exigir ajuste posterior antes de uso em produção.

A execução paralela é organizada por um agente principal, que atua como orquestrador, e por vários subagentes responsáveis por features individuais. Cada subagente recebe sua própria janela de contexto, o que evita misturar raciocínios e reduz a pressão sobre o contexto do agente principal. Esse isolamento permite que várias especificações sejam produzidas simultaneamente sem concentrar todos os tokens em uma única sessão. Para workloads de especificação, essa divisão tende a ser suficiente para evitar estouro de contexto mesmo em codebases maiores.

O disparo do processo pode ser feito de duas formas: informando explicitamente um conjunto de features, como 1, 2 e 3, ou pedindo a geração de uma wave inteira. Quando a entrada é uma wave, o sistema consulta o PRD e identifica automaticamente quais features pertencem àquele agrupamento. Isso transforma o planejamento definido anteriormente em uma unidade operacional de execução. Retomando a organização por waves já estabelecida, o ganho aqui é converter dependências e prioridade em um comando executável.

A geração paralela não ignora a ordem lógica entre features. Se uma feature depende de artefatos, contratos ou fundações que ainda não existem, o processo deve bloquear sua geração, porque a especificação perderia base concreta no codebase e no PRD. Esse comportamento reaproveita o grafo de dependências já definido anteriormente, agora como regra de validação de execução. Paralelismo, portanto, só é seguro entre itens cujas dependências já estejam satisfeitas.

Antes de iniciar a geração, o processo inspeciona o estado atual do codebase para verificar fundações implementadas e dependências resolvidas. Esse levantamento produz um relatório consolidado com o que já existe, o que está pronto para ser derivado e quais features podem entrar na rodada atual. No exemplo, a wave 3 contém as features 4, 7 e 12, e a execução só prossegue porque a fase anterior já foi concluída. A especificação deixa de ser abstrata e passa a ser ancorada no estado real do projeto.

No fluxo interativo, a entrevista com o agente serve para negociar opções, refinar decisões e ajustar o nível de detalhe da spec. No modo batch, essa etapa continua existindo conceitualmente, mas suas recomendações são aprovadas automaticamente. Isso acelera a produção de documentos quando a prioridade é throughput, não curadoria detalhada. Em ambientes reais, esse atalho é útil apenas se houver revisão posterior, porque especificação incompleta ou mal calibrada ainda gera retrabalho downstream.

Executar com subagentes não elimina o custo de gerar especificações; apenas distribui o trabalho. O sistema ainda precisa explorar diretórios, inspecionar o codebase, consolidar dependências e produzir os artefatos de cada feature. Por isso, o tempo de execução continua relevante mesmo com paralelismo. O ponto crítico passa a ser observar como a divisão entre agentes afeta o consumo total de tokens e a eficiência da janela de contexto.

## Transcrição

00:00

Bom, pessoal, é só para consolidar um pouco mais agora na sua cabeça,

00:04

porque a gente vai desenvolver, começar a desenvolver daqui para frente em paralelo,

00:08

eu queria que você entendesse esse gráfico de dependências

00:12

para saber o que a gente vai fazer,

00:13

mas também para você entender,

00:15

consolidar meio que o que eu falei em relação às integrações. Então,

00:20

eu tenho a feature 01, que tem autenticação, a feature 02, aqui,

00:25

por exemplo, que vai fazer um vídeo upload, que tem o vídeo upload...

00:29

path com metadata, e aí cai para uma funcionalidade 3,

00:35

que é o background processing. O background processing faz o que para a gente?

00:39

Ele processa o vídeo, ou seja, ele pica o vídeo nos tamanhos pequenos,

00:43

gera o thumbnail, e a partir dele eu posso ter o meu player de vídeo funcionando,

00:48

eu posso sumarizar os dados,

00:51

a feature de sumarizar e transcrever o conteúdo,

00:56

o texto do vídeo. E em cima disso,

00:59

eu posso inclusive fazer a busca em cima das transcrições ali do vídeo.

01:04

Tudo isso porque eu tenho o providers e o consumers aqui para a gente.

01:09

Como que a gente vai organizar isso agora para a gente fazer?

01:14

Quando eu... Deixa eu fechar esse cara aqui.

01:17

Eu vou limpar essa minha sessão. E o que acontece?

01:23

Nesse meu spec writer, aqui, ó.

01:29

Pra facilitar a vida.

01:32

Entendam muito bem, tá? Entendam muito bem. Pra facilitar a minha vida,

01:36

principalmente para essa aula aqui, sabe a parte da entrevista? A entrevista,

01:44

a gente fica discutindo com a IA e ela vai descrevendo e ela vai

01:48

sugerindo e você vai concordando ou não concordando e você fica ali num ciclo que,

01:52

sei lá, vai demorar meia hora, 40 minutos, 10 minutos.

01:55

Depende do tempo e do nível de especificidade que você quer

01:59

e que você quer trazer de acordo com a complexidade da ficha.

02:03

Para facilitar a coisa aqui, eu criei como se fosse um piloto automático.

02:09

O que é esse piloto automático aqui?

02:13

Eu criei um modo chamado Batch Mode aqui. Deixa eu mostrar para você.

02:20

O que é esse Batch Mode?

02:22

O Batch Mode vai conseguir fazer o processamento

02:25

e a geração de features em paralelo.

02:30

Mas sabe a entrevista que a Yaa iria fazer para a gente?

02:33

Toda entrevista que ela faz, ela dá as opções e ela dá a sugestão dela.

02:39

Por padrão, nesse modo,

02:41

eu estou falando que eu vou sempre aceitar

02:44

todas as recomendações da entrevista dela.

02:49

Entendeu? Então, quando eu faço isso, com um comando,

02:52

eu consigo gerar todas as especificações ao mesmo tempo.

02:57

Um outro ponto importante é que eu falo aqui

03:00

para ele fazer em paralelo com múltiplos agentes.

03:03

Então, o que vai acontecer na prática aqui para mim? Vai acontecer algo desse tipo.

03:10

Eu vou ter aqui o meu agente principal do meu cloud,

03:14

meu agente, sei lá, meu cloud, por exemplo, meu agente principal, certo?

03:20

Vou chamar ele de orquestrador. É o meu agente main que tem ali.

03:24

E aí eu vou rodar essa minha skill. Quando eu rodar essa minha skill,

03:28

o que eu vou fazer? Eu vou falar o seguinte,

03:30

Eu quero que você tenha um sub-agente que

03:34

vai fazer a geração da especificação da feature 01.

03:40

Depois, eu vou querer que você faça a

03:45

mesma coisa com outro sub-agente para a Feature 2. E depois,

03:50

eu vou querer que você faça a mesma

03:52

coisa com o sub-agente na sessão 3.

03:58

E o que isso vai facilitar a minha vida? Primeiro ponto,

04:02

o orquestrador tem a janela de contexto dele.

04:05

Cada sub-agente tem a própria janela de contexto. Ou seja... Esses caras,

04:10

eles conseguem trabalhar e fazer o trabalho em paralelo,

04:13

desenvolver tudo o que eles estão fazendo e quando eles terminarem,

04:16

ele apenas avisa esse cara. Esse cara tem a própria janela dele,

04:20

não mistura. Então, em tese, os nossos tokens,

04:23

a nossa janela de contexto, ela não vai estourar e ficar compactando.

04:26

Vai depender muito do trabalho,

04:28

mas para esse tipo de especificação é muito difícil isso aí

04:31

estourar uma janela de contexto de 200 mil tokens, por exemplo.

04:34

Então essa que é a ideia que esse spec writer, o grande ponto, é que na hora que

04:39

ele vai gerar a especificação, eu estou aceitando por

04:41

padrão o que o que o agente está me recomendando.

04:48

Então eu estou muito mais fazendo isso para a

04:50

gente, como se diz, poupar tempo aqui no curso do

04:56

que necessariamente é uma recomendação para que você faça nos

04:59

seus projetos em produção. Talvez você possa até fazer,

05:04

mas depois revisar e reajustar esse documento,

05:07

tá? Porque especificar algo dá trabalho,

05:10

galera. E o grande problema que a gente,

05:13

às vezes, a gente esquece,

05:14

a gente acha que ficar especificando dá trabalho, que demora muito,

05:17

mas quantas vezes o nosso projeto vai e volta

05:20

quando a gente está trabalhando sem AI,

05:23

etc., porque faltaram detalhes de especificação,

05:26

tá? Então,

05:27

esse aí é um aspecto ali super importante que eu quero que vocês entendam.

05:31

Então, é basicamente isso.

05:33

Mas o que eu fiz além disso? Para que eu consiga gerar essas features,

05:37

eu criei alguns formatos. Eu posso falar,

05:40

gere em paralelo a feature 1, 2 e 3,

05:43

por exemplo. Ou eu posso pedir para ele fazer assim,

05:46

gere a wave 3.

05:48

E daí ele vai pegar todas as features daquela wave e vai fazer o desenvolvimento.

05:53

E eu também estou seguindo o gráfico de dependências.

05:56

Ou seja, se eu pedir para ele criar features que...

05:59

têm dependências de coisas que não foram desenvolvidas ainda, o que vai acontecer?

06:05

Ele vai falar que não pode,

06:06

porque ele não consegue gerar uma feature baseada em algo que ainda não existe,

06:10

que ele não tem uma base ainda para trabalhar.

06:12

Então, essa que é a ideia principal em relação a isso. Então,

06:17

basicamente, o que eu vou fazer aqui vai ser o seguinte.

06:22

Se você olhar o nosso PRD... De novo, cadê o nosso PRD?

06:28

Eu tô abrindo e fechando ele toda hora e eu

06:33

tenho, se eu não me engano, é o Wave 3.

06:39

Cadê minha Wave 3?

06:42

Aqui, ó. Tem o meu Wave 3. A Wave 3, ela tem a feature 4, 7 e 12.

06:48

Ok? Então, eu vou chegar aqui no Cloud e vou fazer o seguinte, tá?

06:53

Eu vou colocar a Spec Writer,

06:57

vou falar qual que é o meu PRD, certo?

07:02

Vou falar... quem que é o meu PRD, e aqui eu vou falar o seguinte,

07:06

eu quero que ele faça a minha Wave 3 aqui para mim.

07:11

Quando eu começar a trabalhar dessa forma,

07:13

vamos ver o que ele vai fazer aqui para a gente.

07:17

E esse processo, ele vai demorar de qualquer forma,

07:20

mesmo trabalhando com subagentes,

07:21

porque gerar especificação é algo que demora em forma geral.

07:25

Então, ele está listando os diretórios, obviamente ele também vai explorar

07:32

Tudo o que acontece no nosso Codebase.

07:35

E eu quero trazer um detalhe também importante aqui pra você, tá?

07:39

E esse detalhe vale a pena eu

07:43

mencionar, tá? Porque, inclusive, não é uma limitação.

07:49

É algo que eu fiz de propósito pra simplificar um pouco as coisas,

07:53

tá? Mas deixa eu mostrar aqui pra vocês. Olha só. Aqui ele fez um relatório.

07:57

Olha, a fundação tá completa. Eu tenho esses caras feitos.

08:01

Fase 1, Feature 1, 2 e 3 implementadas.

08:03

Tem essas dependências aqui, estão satisfeitas. Então, eu posso trabalhar.

08:07

Então, qual que é o plano consolidado?

08:10

Fazer a Feature 4, a 7 e a 12.

08:13

O módulo vai ser um módulo em paralelo com três agentes.

08:16

Vai usar o Codebase State baseado no que tem de fundação e

08:22

vai aceitar automaticamente as recomendações e vão ser gerados nessa pasta aqui.

08:28

Você concorda? Eu falo que sim.

08:31

E agora ele vai começar o trabalho dele aqui para a gente. Então,

08:35

olha só. O Claudio já colocou aqui. Estou criando três agentes em paralelo.

08:43

Legal? E daí ele vai fazer com que cada agente

08:46

seja capaz de executar e

08:51

fazer a especificação daquela feature.

08:55

Então, você vai ver aqui que eu já tenho um agente para gerar a feature 4.

08:59

que ele está inicializando,

09:00

e daí provavelmente você vai ver daqui a pouquinho ele já gerando outro agente,

09:05

outro agente e outro agente para ele conseguir trabalhar.

09:08

Então, agente para gerar o 4, o 7,

09:11

daqui a pouco ele está disparando um outro agente.

09:14

Para o vídeo não ficar muito grande,

09:16

eu quero trazer um detalhe desse processo em batch que está sendo feito,

09:21

e é importante você saber como isso está.

09:26

Porque isso impacta muito na quantidade de tokens que está

09:29

sendo utilizado nesse momento para gerar isso aqui.

09:31

Tá bom? Então vamos ver isso no próximo vídeo.

## Resumo IA

**Abreviações**
*   PRD: Product Requirements Document
*   IA: Inteligência Artificial

**Resumo**
A aula apresenta o "Batch Mode" como um modo de execução para automatizar a geração de especificações de múltiplas funcionalidades (features) em paralelo. O objetivo é reduzir o tempo operacional, especialmente para a produção em massa de especificações organizadas em "waves". Neste modo, o sistema aceita por padrão as recomendações sugeridas pelo agente de IA, substituindo a necessidade de uma entrevista de refinamento interativa para cada feature.

O processo de execução paralela é orquestrado por um agente principal, que delega o trabalho a vários subagentes. Cada subagente é responsável pela especificação de uma feature individual e opera em sua própria janela de contexto, o que isola o raciocínio, evita a mistura de informações e reduz a pressão sobre o contexto do agente principal, prevenindo estouros de contexto.

O disparo do processo pode ser feito de duas maneiras: explicitando um conjunto de features (e.g., features 1, 2 e 3) ou solicitando a geração de uma "wave" completa (e.g., wave 3). Quando uma wave é especificada, o sistema consulta o PRD para identificar automaticamente as features pertencentes àquele agrupamento (como as features 4, 7 e 12 para a wave 3 no exemplo dado).

Crucialmente, a geração paralela respeita o grafo de dependências entre as features. Antes de iniciar qualquer especificação, o processo inspeciona o estado atual do codebase para verificar fundações implementadas e dependências resolvidas. Este levantamento produz um relatório consolidado, e a geração de uma feature é bloqueada se suas dependências ainda não estiverem satisfeitas, garantindo que a especificação seja ancorada no estado real do projeto. Após a aprovação do plano, o orquestrador cria os subagentes em paralelo para iniciar a geração das especificações. Embora o Batch Mode acelere a produção de documentos, a aula ressalta que o processo ainda exige tempo, pois as tarefas subjacentes de exploração do codebase, inspeção e consolidação de dependências para cada feature permanecem relevantes.

**Pontos de atenção**
*   **Perda de Revisão Interativa:** O Batch Mode sacrifica a revisão interativa durante a geração das especificações, pois aceita as recomendações do agente de IA automaticamente. Isso acelera a produção, mas os documentos gerados podem exigir ajuste posterior manual antes de serem usados em produção.
*   **Risco de Retrabalho:** Especificações incompletas ou mal calibradas, resultantes da automação sem curadoria detalhada, podem levar a retrabalho ("rework downstream") no ciclo de desenvolvimento.
*   **Validação de Dependências é Crítica:** A execução paralela só é segura para features cujas dependências já estão satisfeitas. O sistema utiliza o grafo de dependências para validar essa condição, bloqueando a geração de especificações que dependam de artefatos, contratos ou fundações ainda inexistentes, garantindo uma base concreta.
*   **Gerenciamento de Contexto dos Agentes:** A utilização de subagentes, cada um com sua própria janela de contexto, é uma boa prática para evitar o estouro de contexto e a mistura de raciocínios, otimizando o consumo de tokens mesmo em codebases maiores.
*   **Tempo de Execução Persistente:** Apesar do paralelismo, a geração de especificações ainda demanda um tempo considerável, pois envolve tarefas complexas como a exploração de diretórios, inspeção do codebase e consolidação de dependências para cada feature.
*   **Contexto de Curso vs. Produção:** A automação via Batch Mode, no contexto da aula, é apresentada como uma forma de poupar tempo didático. Em ambientes de produção, essa abordagem só é útil se houver uma revisão e ajuste posteriores rigorosos das especificações geradas.