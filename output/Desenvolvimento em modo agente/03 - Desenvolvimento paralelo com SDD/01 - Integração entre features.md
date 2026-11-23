Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17790)

## Resumo da aula

A seção de features do PRD funciona como um hub do qual outras partes do documento são derivadas. Problemas e oportunidades geram features, e essas features passam a sustentar User Stories, escopo e artefatos de planejamento. Esse arranjo importa porque o paralelismo não nasce de dividir trabalho arbitrariamente, mas de explicitar o que cada feature faz e como ela se relaciona com as demais.

Desenvolver features em paralelo só é viável quando os bloqueios entre elas estão claros. A organização em waves surge justamente desse mapeamento: algumas features precisam ficar prontas antes, enquanto outras podem avançar simultaneamente depois que suas dependências forem satisfeitas. O ganho de velocidade não vem de “mágica”, e sim de uma estrutura que reduz ambiguidade sobre o que bloqueia o quê.

A relação entre features pode ser modelada por dois verbos: consumir e prover. Quando uma feature consome algo que outra provê, existe uma dependência real e rastreável entre elas. Essa modelagem produz uma árvore de dependências mais consistente, porque a ligação não é inferida de forma vaga; ela nasce de contratos funcionais explícitos entre partes do sistema.

Retomando a organização por waves, o gráfico de dependências mostra quais features podem ser executadas em paralelo e quais precisam esperar outras entregas. A prioridade da feature, combinada com suas dependências, permite representar esse fluxo também em um diagrama Mermaid. O valor desse grafo está em transformar relações arquiteturais em uma visão operacional de execução.

No cenário apresentado, a feature AI Summary Display consome artefatos produzidos por outras features, como Summary Overview, bullet points e dados necessários para playback e timestamps. Ao mesmo tempo, ela também provê novos elementos, como a renderização da transcrição segmentada e controles para navegação no vídeo. Esse tipo de descrição evita que uma feature seja implementada como ilha, sem saber o que já existe ou o que precisa entregar para as próximas.

Quando as ligações entre features não são definidas, o sistema tende a acumular código morto, lógica duplicada e integrações quebradas. Uma feature pode refazer algo que já estava pronto simplesmente porque não havia clareza sobre o que outra já provia. Em SDD, explicitar consumo e provisão reduz esse desperdício e melhora a coerência entre implementações feitas por fluxos paralelos.

Cada feature precisa de critérios de aceitação próprios para determinar se ela funciona isoladamente. Esses critérios operam como uma checklist objetiva do que deve existir para considerar a entrega válida. Mais adiante, essa checklist pode evoluir para um contrato entre agentes com funções distintas, como um agente que implementa e outro que avalia.

Além dos critérios por feature, é necessário definir critérios de aceitação para a integração entre features. Quando uma feature consome algo de outra, essa relação precisa ser validada explicitamente, e não presumida. O objetivo é garantir que o sistema “se converse” de fato, por exemplo verificando se metadata e thumbnail produzidos em upload renderizam corretamente na grid ou se um vídeo enviado entra automaticamente na pipeline seguinte.

A IA não infere de forma confiável como todas as partes se conectam, especialmente quando o trabalho é dividido em sessões diferentes e sujeito a limites de janela de contexto. Mesmo com janelas grandes de tokens, reduzir o conjunto de features por sessão pode ocultar dependências importantes. Por isso, dependências explícitas e critérios de integração funcionam como mecanismos de preservação de contexto arquitetural.

## Transcrição

00:00

Bom, pessoal, no capítulo anterior,

00:02

a gente fez o desenvolvimento aqui até a nossa feature número 3, tá?

00:06

Mas agora a gente entra numa nova etapa e é uma das

00:09

etapas mais significativas em relação à velocidade

00:13

de desenvolvimento que você vai encontrar,

00:15

que é para que você consiga fazer o desenvolvimento paralelo das suas features,

00:19

das suas implementações, tá? Se você perceber aqui,

00:22

eu tenho uma Wave 3, ou seja,

00:24

é onde eu consigo trabalhar e criar essas features de uma forma paralela,

00:28

porque... Esse cara que era bloqueante, ele agora já me permite eu conseguir fazer.

00:34

Se essas features estiverem prontas,

00:36

eu consigo fazer essas aqui em paralelo e depois essas em paralelo.

00:40

E já dá para perceber que isso aí consegue mudar bastante o jogo.

00:43

Existe mágica? Não.

00:45

Mas eu preciso muito que você consiga entender o raciocínio que está por trás disso,

00:50

porque se você for criar o seu framework, o seu...

00:54

a sua skill, ou se você vai usar isso de terceiros,

00:57

é importante você entender como é que você consegue gerar

01:00

as áreas derivadas de outras

01:06

partes ali da sua aplicação.

01:08

Então, o que eu vou fazer? Deixa eu trazer aqui no Scaledraw para ficar mais claro.

01:13

Isso aqui é um formato de como eu estou fazendo esse PRD.

01:19

E não necessariamente é a forma como você tem que fazer. Às vezes o seu PRD é maior,

01:24

é menor, tem mais coisa, tem menos coisa. Depende, tá?

01:27

Às vezes você não está usando nem necessariamente um PRD, né?

01:30

Esse cara aqui, ele está consolidando features no final das contas. Então,

01:33

o que acontece é o seguinte. Eu tenho o meu problema, a minha oportunidade,

01:36

né? Que foi colocado lá inicialmente com a input,

01:41

né? E aqui, nessa seção... que é a seção 6 do meu PRD,

01:46

eu tenho a área de Features. Então,

01:48

baseado nos problemas e nas oportunidades,

01:51

eu tenho todas as Features que eu preciso e o que essas Features fazem.

01:55

Então, isso aqui é um Hub, porque a partir dessas Features,

01:58

eu consigo gerar as outras áreas do meu PRD.

02:02

Por exemplo, a gente tem a parte de User Stories. Eu,

02:05

como usuário, quero poder clicar e fazer o login.

02:08

Eu, como usuário, quero poder me registrar com nome e e-mail e fazer isso. Então,

02:12

essa sessão é baseada em uma das features que

02:14

estão aqui dentro para conseguir fazer isso funcionar.

02:18

Essa sessão também traz o que não vai estar no escopo do meu projeto.

02:23

Isso aqui é importante.

02:25

Mas agora que está o ponto importante que eu queria trazer para você,

02:31

que é a geração dessa sessão 8 e dessa sessão 9.

02:36

Porque nesse caso, quando a gente vai trabalhar em paralelo,

02:39

é o que a gente precisa ter mais destaque e cuidado para gerar.

02:43

Por que eu estou dizendo?

02:45

Porque quando eu vou gerar essa sessão 8,

02:50

por exemplo, onde eu tenho aquele gráfico de dependências,

02:53

se eu voltar aqui no cursor, eu consigo olhar esse cara.

02:58

Essa feature, eu tenho uma prioridade e as dependências. Então, aqui, basicamente,

03:02

Eu tenho todas as dependências entre as features.

03:05

Aqui é como eu vejo como isso pode ser paralelizado.

03:07

E aqui é como que são as dependências se eu for olhar aqui no meu...

03:11

Como um diagrama Mermaid, tá? Então, o que acontece aqui?

03:18

Essa dependência, ela só consegue existir por quê?

03:22

Porque na hora que eu estou criando uma feature... Eu, novamente, como eu falei para vocês,

03:28

Eu estou falando que essa feature consome

03:31

Alguém ou essa feature provê algo para alguém.

03:37

Então, baseado no que alguém consome e no que alguém provê,

03:41

Eu consigo gerar essa dependência. Então,

03:45

Olha só que interessante. Deixa eu olhar aqui.

03:49

Deixa eu pegar aqui qualquer feature que a gente tenha aqui.

03:54

Se eu olhar aqui, por exemplo, nessa feature, 10, AI Summary Display,

04:00

Ela está falando que ela consome o Summary Overview,

04:04

O parágrafo do Summary Overview e os

04:08

Tópicos em Bullet Points da Feature 7. Ok?

04:15

E uma coisa que é interessante é, você vai perceber que em diversos aspectos aqui,

04:20

Você vai ver, esse cara consome algo da Feature 8.

04:25

A gente vai ver que, por exemplo,

04:27

Esse cara consome dados da feature 3,

04:33

Que ele precisa do path do arquivo para o playback.

04:36

Ele precisa também da feature 7 para a transcrição dos segmentos,

04:41

Para iniciar os timestamps do vídeo. Mas, além disso,

04:44

Ela provê a renderização da transcrição com todos

04:48

Os segmentos para fazer o playback e

04:50

Também o controle onde vai fazer para a gente pular em cada parte do vídeo.

04:54

Então, se você perceber,

04:56

Quando eu crio e desenvolvo as features pensando

05:00

Como uma feature se conecta com a outra,

05:03

Consumindo ou provendo,

05:05

Eu tenho uma árvore de dependências muito mais consistente.

05:11

É muito, mas é muito comum você...

05:16

Ver sistemas, frameworks de SDD, não tendo essas ligações.

05:21

E aí a gente acaba caindo naquele ponto onde

05:24

Uma feature acaba não conseguindo falar com outra,

05:27

Ou nós temos muito código morto ou replicado, porque o que uma consome prevê,

05:33

Uma coisa já estava pronta e ela tem que refazer,

05:36

Porque ela não sabia que aquilo estava pronto. Então,

05:39

A gente acaba tendo esses tipos de problema. Então, por isso que...

05:43

Essa parte é importante. Então,

05:45

Esse gráfico de dependências que foi gerado é baseado nessa

05:49

Relação de quem consome e de quem provê.

05:53

Por outro lado, o que acontece?

05:55

Eu tenho uma outra parte, que é uma das partes mais importantes, inclusive, do PRD,

06:00

Que é os critérios de aceitação. AC normalmente é chamado, né? AC. O que acontece?

06:07

Esses critérios de aceitação, eles têm duas formas. Uma forma é o que eu preciso...

06:13

Ter para dizer que essa minha feature está funcionando. Ou seja,

06:18

Para cada feature eu tenho um critério de aceitação.

06:21

Vários critérios de aceitação, claro.

06:24

Por outro lado, o que acontece?

06:27

Eu tenho também, dentro de critérios de aceitação, que é cross-feature integration.

06:33

O que isso significa?

06:35

A gente vai pegar tudo que uma feature consome da outra, ou seja,

06:42

significa que... Quando uma consome da outra, significa que elas estão integradas.

06:47

E aí eu vou gerar critérios de aceitação

06:50

para garantir que uma feature esteja integrada à outra.

06:55

Então, a ideia principal do PRD no formato que eu gerei aqui,

07:00

essas árvores de dependência,

07:02

elas não são árvores arbitrárias, separando para uma funcionalidade de login,

07:07

uma parte de upload,

07:08

uma parte de transcrição. Não. O sistema tem que se conversar.

07:12

E o que a maioria das vezes você vê é, vamos fazer login,

07:17

vamos fazer isso, e daí você faz e as coisas não se falam.

07:20

Então, essa é uma forma para mitigar.

07:22

Isso significa que vai funcionar perfeitamente? Não,

07:25

mas já ajuda bastante aí. Então,

07:28

lembre-se que os critérios de aceitação eu tenho

07:30

por feature e tenho por cross-feature integration.

07:34

Então, se você olhar aqui,

07:35

deixa eu cair nos meus critérios de aceitação lá para baixo, as

07:41

dependências, e olha só. Eu tenho critérios de aceitação.

07:45

Da feature 1, da landing page,

07:47

o que ele tem que ter aqui como critério de aceitação? Autenticação.

07:52

Feature de upload. E eu não sei se você está percebendo,

07:55

eu não vou pedir, inclusive,

07:57

para a IA sair mudando esse PRD.

07:59

Mas se você perceber, é como se fosse uma checklist.

08:02

E você vai perceber que quando a gente for falar em Harness Engineering,

08:05

você vai perceber que essa checklist, ela vai acabar virando um contrato.

08:11

entre o agente que escreve o código e o agente que avalia o código,

08:16

porque eles serão diferentes, ok?

08:18

Então, isso vai começar a servir como um contrato,

08:20

como uma interface entre dois agentes com funções diferentes,

08:24

tá? Então, eu tenho todas essas features que são desenvolvidas,

08:28

mas depois, aqui embaixo, eu tenho cross-feature integration.

08:32

Ou seja, eu quero ver se o vídeo metadata,

08:35

o thumbnail que foi provido para o upload,

08:40

pode renderizar corretamente na Library Grid,

08:44

que foi feito pela funcionalidade 4,

08:49

incluindo o título e a descrição.

08:51

Eu quero ver se o vídeo produzido pelo Upload 3

08:54

é automaticamente pego no processo da Pipeline 7.

08:57

Então, aqui é onde eu consigo ver se realmente

09:01

o meu sistema está coerente e se ele está conversando.

09:06

Então, levem isso em mente,

09:08

porque é muito inocente a gente achar que a IA vai entender como tudo gruda,

09:13

principalmente se você fizer em sessões diferentes.

09:17

E toda sessão tem um limite de tokens,

09:19

né? A gente tem, normalmente, modelos com 200 mil tokens de janela,

09:24

tem janelas de 1 milhão de tokens.

09:27

Que o Cloud está tendo, por exemplo, atualmente. Mas a questão é que, quando você...

09:33

Diminui a quantidade de features para caber dentro de uma janela ou alguma coisa,

09:37

Isso é um outro detalhe que a gente vai falar em Harness,

09:39

O importante é a gente conseguir entender como as coisas se integram,

09:42

Tá? Então no próximo vídeo eu vou dar um

09:44

Exemplo um pouco mais prático para você entender

09:46

E daí a gente vai fazer a ideia da

09:50

Geração de várias features de forma simultânea aí.

## Resumo IA

**Abreviações**
*   **AC**: Acceptance Criteria
*   **IA**: Inteligência Artificial
*   **PRD**: Product Requirements Document
*   **SDD**: Software Design Document

**Resumo**
A aula aborda o desenvolvimento paralelo de features como um meio de acelerar o processo de desenvolvimento, enfatizando que esse ganho de velocidade não é "mágico", mas resultado de uma estrutura bem definida. O objetivo principal é capacitar os alunos a organizar o trabalho de forma que múltiplas features possam ser desenvolvidas simultaneamente, minimizando bloqueios e ambiguidades.

Central para essa abordagem é a seção de Features de um PRD, que atua como um hub. Problemas e oportunidades identificados no início do projeto dão origem a essas features. Por sua vez, as features são a base para a criação de User Stories, a definição do escopo do projeto (incluindo o que está *fora* do escopo) e outros artefatos de planejamento.

O fluxo explicado pelo instrutor destaca a importância de modelar as relações entre features através dos verbos "consumir" e "prover". Uma feature que "consome" algo que outra "provê" estabelece uma dependência real e rastreável. Essa modelagem permite a construção de uma árvore de dependências consistente, que pode ser visualizada em um gráfico de dependências (como um diagrama Mermaid). Esse gráfico organiza as features em "waves" (ondas), indicando quais podem ser executadas em paralelo e quais precisam aguardar a conclusão de outras dependências.

O exemplo da feature "AI Summary Display" ilustra como ela pode consumir elementos de outras features (como dados para playback e timestamps, e bullet points) e, ao mesmo tempo, prover novos elementos (como a renderização de transcrições segmentadas e controles de navegação). Essa descrição detalhada evita que features sejam desenvolvidas isoladamente.

Além das dependências, a aula enfatiza a criação de Critérios de Aceitação (ACs) em duas frentes:
1.  **ACs por feature**: Para determinar se cada feature funciona isoladamente, agindo como uma checklist objetiva.
2.  **ACs para integração entre features (Cross-Feature Integration)**: Para validar explicitamente que as features se comunicam e integram corretamente, como verificar se metadados de upload renderizam na grid ou se um vídeo entra automaticamente na pipeline seguinte.

Essa abordagem estruturada é crucial para garantir a coerência do sistema e preservar o contexto arquitetural, especialmente quando o desenvolvimento é dividido e realizado com o auxílio de ferramentas de IA, que podem ter limitações no entendimento das conexões complexas.

**Pontos de atenção**
*   **Paralelismo não arbitrário**: O desenvolvimento paralelo eficaz não surge da divisão arbitrária do trabalho, mas da explicitação clara das funcionalidades de cada feature e suas relações.
*   **Clareza de bloqueios**: A viabilidade do desenvolvimento paralelo depende de uma compreensão clara dos bloqueios e dependências entre as features.
*   **Modelagem Consumir/Prover**: Utilizar os verbos "consumir" e "prover" para modelar dependências cria uma árvore de dependências mais consistente e rastreável, baseada em contratos funcionais explícitos.
*   **Features como Hub**: A seção de features no PRD deve ser um hub, do qual outras partes do documento (User Stories, escopo, planejamento) são derivadas.
*   **Definição do "Fora de Escopo"**: É crucial definir explicitamente o que não estará no escopo do projeto para evitar ambiguidades e expectativas desalinhadas.
*   **Evitar código morto e duplicação**: A falta de ligações claras entre features leva a código morto, lógica duplicada e integrações falhas, pois uma equipe pode refazer algo já existente.
*   **Critérios de Aceitação por Feature**: Cada feature deve ter critérios de aceitação próprios para validar seu funcionamento isolado, atuando como uma checklist.
*   **Critérios de Aceitação para Integração**: É fundamental definir critérios de aceitação específicos para a integração entre features (cross-feature integration) para garantir que o sistema "se converse" de fato e que as relações de consumo/provisão funcionem.
*   **IA e Preservação de Contexto**: Não se deve assumir que a IA inferirá de forma confiável todas as conexões entre as partes de um sistema, especialmente em sessões distintas ou com limites de janela de contexto. Dependências explícitas e critérios de integração são mecanismos essenciais para preservar o contexto arquitetural.
*   **ACs como Contrato**: Os critérios de aceitação podem evoluir para contratos entre agentes com funções distintas (ex: quem implementa e quem avalia o código), como no conceito de Harness Engineering.