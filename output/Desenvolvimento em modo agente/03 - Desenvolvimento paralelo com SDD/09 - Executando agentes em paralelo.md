Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17798)

## Resumo da aula

Git Worktree permite materializar múltiplos branches em diretórios separados da mesma máquina, evitando que várias implementações concorram pela mesma árvore de arquivos. Retomando o desenvolvimento paralelo por waves, esse é o mecanismo que impede o caos de editar a mesma codebase física enquanto várias features avançam ao mesmo tempo. Cada worktree funciona como um espelho operacional de um branch, com isolamento suficiente para rodar agentes, testes e mudanças locais sem sobrescrever o trabalho das outras frentes.

Sem worktree, iniciar várias features em paralelo a partir de main ou de branches distintos no mesmo diretório gera conflito de arquivos, estado local inconsistente e dificuldade para validar cada implementação separadamente. O problema não é apenas Git; é também o runtime local, os artefatos temporários e os comandos executados por agentes diferentes sobre o mesmo conjunto de arquivos. O worktree resolve isso criando cópias de trabalho independentes, cada uma associada ao seu próprio branch.

O uso de cloud --work-tree mostra uma integração prática entre o orquestrador e o recurso nativo do Git. O ponto central não é o comando específico da ferramenta, mas a ideia de iniciar cada sessão já dentro de uma worktree dedicada à feature correspondente. Isso reduz setup manual, deixa explícito qual contexto cada agente está usando e facilita rastrear branch, modelo e estado do repositório durante a execução.

Cada feature paralela deve ser associada a uma sessão própria, com identificação clara do número ou nome da feature. No exemplo, Background Processing, Video Library e painel administrativo são disparados em sessões separadas, inclusive em ferramentas diferentes, como Cursor e Claude Desktop. Essa organização evita confusão operacional quando há muitas execuções simultâneas e permite acompanhar progresso, logs e bloqueios de cada frente sem misturar contextos.

A skill de implementação, já definida anteriormente, continua sendo o ponto de entrada para o trabalho do agente; o que muda aqui é o contexto de execução. Em vez de rodar tudo sobre a mesma árvore de arquivos, cada chamada recebe sua própria worktree e a feature correspondente no PRD.md. Isso preserva o workflow padronizado da skill enquanto adiciona paralelismo real na camada de execução.

O prompt da feature pode carregar restrições e observações específicas que o agente deve respeitar durante a implementação. No caso da pipeline de transcrição, a exigência foi solicitar a chave da OpenAI no momento apropriado, mas registrar a variável no .env.example em vez de embutir credenciais diretamente. Esse tipo de instrução é importante porque adapta a implementação às necessidades operacionais da feature sem quebrar o padrão geral da skill.

Mesmo em execução paralela, o agente precisa inspecionar features anteriores e convenções já estabelecidas no projeto antes de começar a implementar. Retomando o grafo de dependências e o estado compartilhado do codebase, isso garante que a nova feature respeite integrações existentes, como upload já implementado, padrões de teste e possíveis decisões de infraestrutura. A exploração inicial também revela necessidades como uso de Testcontainers, resolução de portas e navegação da interface para validar fluxos reais.

Executar agentes em paralelo não elimina supervisão; apenas desloca o trabalho humano para monitoramento e intervenção pontual. Durante a execução, é útil observar se o agente está resolvendo portas, capturando screenshots, navegando na aplicação e lidando com erros do sistema em tempo de desenvolvimento. Essas inspeções intermediárias ajudam a detectar cedo se a implementação está avançando de forma saudável ou se entrou em um ciclo improdutivo.

Algumas ferramentas criam automaticamente uma pasta agregadora, como WorkTrees, para armazenar os diretórios associados a cada sessão. Isso não é um requisito do Git Worktree, mas pode facilitar inspeção manual dos arquivos enquanto o branch principal permanece aberto em outro contexto. A utilidade prática está em permitir que você acompanhe o que cada agente alterou sem precisar trocar constantemente de diretório ou perder visibilidade do main.

Quando o agente conclui uma feature, o relatório final consolida fases executadas, commits, critérios de aceitação validados, integrações entre features, desvios e soft fails. Esse relatório é valioso porque transforma a execução do agente em evidência auditável, mostrando exatamente o que foi testado e quais adaptações foram necessárias. Ainda assim, ele não substitui validação humana: a conclusão correta é usar o relatório como ponto de partida para verificar se a funcionalidade realmente opera como prometido.

No caso do background processing, a verificação relevante não termina em “os testes passaram”; ela inclui confirmar que o upload se conecta à pipeline, que a transcrição e o resumo são produzidos e que o fluxo aceita intervenção manual quando necessário. A integração com a feature de upload, já definida anteriormente, aparece aqui como checagem concreta de ponta a ponta. Esse é o tipo de validação que distingue uma implementação localmente correta de uma feature realmente integrada ao sistema.

Credenciais e chamadas externas precisam ser tratadas de forma controlada para que a feature seja reproduzível em desenvolvimento e em CI/CD. Registrar a variável da OpenAI no .env.example, preencher a chave real apenas no .env.local e permitir um modo fake com OPENAI_FAKE=1 cria um fluxo seguro para testar sem custo de API. Da mesma forma, instruções como rodar npm run dev e depender de um hook de instrumentation deixam explícito como o worker inicia e sob quais flags a pipeline entra em operação.

## Transcrição

00:00

Bom, pessoal, agora para a gente começar o desenvolvimento,

00:04

nós vamos rodar três features simultaneamente.

00:08

E uma vez que a gente vai fazer isso, nós vamos precisar trabalhar com Git Worktree.

00:15

A gente já passou por esses conceitos de Git Worktree durante o curso,

00:20

mas de qualquer forma, apenas um recap aqui para a gente, que é o seguinte,

00:25

se você... por algum momento, vai trabalhar dentro de um branch,

00:31

o que vai acontecer? Vamos imaginar que a gente está aqui no branch main.

00:36

Se eu começar a pedir para que a minha feature seja

00:41

desenvolvida e ela comece no branch main ou no branch x,

00:44

etc., e eu for fazer isso em paralelo,

00:47

todas as features vão começar a trabalhar no mesmo code base,

00:51

fisicamente no mesmo local. E aí, simplesmente vai virar o caos,

00:55

a gente vai ter problema de concorrência de arquivo e tudo mais.

00:58

Então, quando a gente está trabalhando com Git Worktree, o que vai acontecer?

01:02

Basicamente, a gente vai fazer um espelho desse branch,

01:07

é como se a gente estivesse copiando o que a gente vai fazer em

01:13

branches separados, rodando simultaneamente na nossa máquina. Então,

01:19

essa vai ser a ideia do Git Worktree que a gente vai trabalhar.

01:24

Então, a gente vai criar três worktrees para que

01:29

nós possamos botar esse cara e tudo para rodar. Então,

01:34

eu vou fazer, existem algumas formas de a gente fazer esse tipo de coisa.

01:38

Uma forma, nesse caso, por exemplo,

01:42

se eu for usar o Cloud Code, eu estou usando o Cloud Code,

01:44

mas isso dá tranquilamente para fazer em qualquer outro...

01:51

sistema, porque o Git Worktree não é um recurso de IA,

01:54

é um recurso no Git que já existe faz tempo,

01:56

né? Você dá um Git Worktree e você pode criar

01:59

o Worktree baseado no branch que você quiser,

02:01

tá? Então, falando especificamente aqui em Cloud Code,

02:07

eu vou fazer esse cara de duas formas, tá? Então, o que que acontece?

02:13

Se você olhar aqui, né? Eu tô no meu branch main, ok?

02:18

E eu tenho essas três features que eu vou ter que desenvolver agora aqui, né?

02:23

Que são as features de background processing,

02:25

a parte de painel de administração e qual que é a outra?

02:31

Qual que foi a que a gente criou por último? Não é a Video Library.

02:34

Deixa eu abrir o PRD aqui só para a gente lembrar,

02:37

porque a numeração delas é diferente, né?

02:40

Porque as dependências trabalham de forma diferente aqui.

02:43

Então deixa eu só confirmar aqui a nossa Wave 3 que a gente está.

02:48

Aqui, Wave 3, Feature 4, que é a Video Library,

02:52

a biblioteca de vídeos. A gente tem o Background Processing,

02:56

que é onde ele vai fazer a pipeline para pegar o vídeo,

02:59

processar o vídeo com FFmpeg,

03:02

depois ele vai transformar esse vídeo em áudio,

03:04

vai pegar o Whisper da OpenAI, depois do Whisper da OpenAI,

03:09

ele vai gerar a transcrição do vídeo,

03:11

vai gerar o resumo do vídeo ali para a gente. Então, a gente tem essa pipeline.

03:14

E a gente tem aqui a Video Library,

03:18

onde vai ter ali a listagem dos vídeos e a

03:21

gente tem a área administrativa ali do nosso sistema.

03:25

Como a gente vai trabalhar ali com o Git Worktree,

03:28

eu vou fazer duas coisas um pouco diferentes aqui, tá? Então,

03:33

eu vou trabalhar uma vez aqui dentro do cursor e com outros dois processos,

03:39

eu vou trabalhar lá no Cloud Desktop,

03:41

somente para mostrar ali para vocês que é algo completamente possível

03:47

Normalmente a gente vai poder começar a trabalhar dessa

03:51

forma e cada vez vai ser mais comum,

03:54

a gente não está na nossa IDE,

03:55

mas sim nas ferramentas onde a gente gerencia

03:58

várias sessões que estão trabalhando ali simultaneamente.

04:02

Falando sobre, nesse caso, o Cloud Code, como é que funciona aqui nesse caso?

04:07

Estou dando um exemplo, pelo menos nesse momento,

04:10

como o Cloud Code está. Essas coisas podem mudar,

04:12

por isso que é importante você entender o conceito. Eu vou...

04:17

abortar aqui o meu Cloud Code, mas aqui agora,

04:20

o que eu vou fazer? Eu vou dar Cloud, tá?

04:23

E eu vou colocar assim, ó, --work-tree.

04:27

E eu vou dar um nome aqui para a minha Worktree chamado de Background Processing,

04:32

tá? Então, eu vou colocar esse cara aqui como Background...

04:38

Como que ele chama o nome da feature?

04:41

Background Processing Pipeline. Background Processing. Processing. É isso aí.

04:49

Background Processing. Quando eu fizer isso, o que vai acontecer?

04:54

Ele vai iniciar o meu Cloud Code agora,

04:56

mas já dentro de uma Worktree. Eu coloquei até aqui dentro do meu estágio do Slime.

05:04

Cada um personaliza essas coisas da forma como quiser. Eu coloco sempre um WT aqui,

05:10

o nome do branch que eu estou e o WT,

05:12

para dizer que eu estou dentro de uma Worktree.

05:14

E qual o modelo que eu estou usando? E se tem esse verdinho aqui,

05:17

é porque eu não tenho nenhum arquivo pendente que não está traqueado ali no Git.

05:22

E agora que eu tenho esse cara aqui, o que eu simplesmente posso fazer?

05:29

Eu vou rodar ali a minha skill. Então, eu vou dar aqui um implement feature,

05:35

que foi aquela skill que a gente colocou.

05:38

Eu vou passar, eu posso passar aqui nesse caso,

05:42

o meu PRD, que eu posso passar, e eu posso falar qual é o nome da feature,

05:47

onde eu posso colocar aqui que é feature 07.

05:52

Esse aí é um ponto importante. E eu posso, inclusive,

05:56

aqui nessa feature 07, ou passar, inclusive, normalmente...

06:02

Se você passa uma pasta, ele vai conseguir entender também. Então,

06:07

esse tipo de coisa é importante para você saber que a abertura de uma skill,

06:12

a inteligência que o modelo tem,

06:15

ele é totalmente entendível que isso vai precisar trabalhar.

06:20

Mas o que eu quero que eu vou passar de informação adicional aqui para ele?

06:26

Quando for realizar a transcrição,

06:34

me informe para

06:38

eu adicionar a chave da OpenAI.

06:46

Porém,

06:48

deixe isso

06:53

como uma variável de ambiente na .env.example, nesse

07:02

caso, na hora de fazer a criação.

07:05

Deixo essa variável como de ambiente na .env.example para eu poder utilizar.

07:10

Basicamente é isso que eu estou colocando.

07:12

E agora, o que vai acontecer? Eu vou pedir para ele fazer aqui o desenvolvimento.

07:18

Então, eu estou dando aqui um implement feature aqui para ele.

07:22

Então, eu vou dar um Enter e agora o Cloud

07:24

vai começar a trabalhar em uma Worktree diferente.

07:28

O que eu vou fazer agora?

07:29

Nós temos outra feature para implementar, que é a feature 04.

07:33

O que eu posso fazer aqui com essa nossa feature 04?

07:36

Eu posso ir aqui no meu Cloud Desktop,

07:38

por exemplo, e aqui eu vou selecionar o Worktree.

07:42

Uma coisa que eu não gosto, pelo menos no momento dessa gravação,

07:45

é que eu não consigo escolher o nome da minha Worktree. Ou se eu posso, eu não sei.

07:50

Mas o fato é que eu vou marcar aqui como Worktree.

07:53

E aqui, o que eu vou fazer? Eu vou colocar a Implement Feature aqui também.

07:59

E eu vou passar a minha linha aqui do meu PRD.md.

08:03

Vou falar qual que é a feature que eu vou rodar, que é a feature 04,

08:07

né? Video Library aqui para mim. Então eu posso colocar aqui a feature 04, que

08:14

é a minha Video Library aqui para ele passar.

08:18

Aqui de boas, né? Para ele implementar.

08:22

E eu acho que com isso é o suficiente para a gente conseguir trabalhar.

08:26

Então eu vou dar um Enter aqui para mim.

08:28

E eu estou pedindo agora para ele iniciar essa feature aqui.

08:31

O que normalmente eu faço, eu renomeio o nome,

08:34

as minhas sessões aqui, pelo menos com um 04 aqui na frente,

08:38

para eu saber de qual feature que eu estou trabalhando.

08:40

Por que eu estou dizendo isso?

08:42

Porque eu tenho momentos onde eu tenho um monte de sessão rodando,

08:46

e às vezes pelo nome que ele colocou eu não consigo identificar,

08:49

então estou colocando aqui o nome de feature.

08:51

E aqui eu tenho uma outra feature que eu vou começar a desenvolver,

08:56

que é a feature 12. Que eu preciso. Então, eu vou fazer a mesma coisa aqui. Implementar a feature.

09:04

Vou colocar aqui o meu PRD.

09:09

E vou colocar aqui também a feature 12.

09:14

A feature 12 que ele está trabalhando. A 12 aqui para mim.

09:19

Administração do painel aqui para ele trabalhar.

09:22

E vou dar um Enter agora aqui para a gente. Então, vamos lá.

09:28

Botar esse cara para rodar.

09:30

E agora eu vou simplesmente colocar aqui um 12 aqui na frente.

09:35

E agora, galera, é esperar esse cara começar a trabalhar.

09:40

Então, aqui na feature 4, olha,

09:42

estou explorando o codebase para entender a feature 02

09:46

e também as convenções que ele teve ali na 03.

09:50

Provavelmente deve ter algumas dependências,

09:53

porque ele explora a árvore de dependências, lembra?

09:56

Ele tem que entender o que já foi feito também.

09:58

Então, ele está entendendo as convenções,

10:00

ele está vendo se ele vai usar Testcontainers, caso precise,

10:04

e agora ele vai explorar e vai começar a programar.

10:11

Para a gente, obviamente,

10:12

não ficar horas aqui esperando esse cara desenvolver tudo isso.

10:18

O que a gente vai fazer?

10:21

Eu vou dar um pause no vídeo e aí,

10:23

quando essas coisas estiverem terminadas, a gente volta.

10:29

E bom, pessoal, somente pra dar um heads up aqui pra vocês, tá?

10:33

Os agentes, eles já estão trabalhando e já estão um tempinho trabalhando,

10:38

né? Esse cara aqui começou faz 13 minutos,

10:41

pra você ter uma ideia, tá? E ele tá implementando a Video Library.

10:44

Eu só tava querendo dar uma passada aqui, né?

10:46

Eu vou fazer algumas interrupções intermediárias pra vocês não ficarem esperando.

10:50

Mas aqui, ó, ele já tá fazendo a implementação, mas...

10:54

Veja que ele começou a resolver o processo de portas e agora ele começa a navegar,

10:59

tirar screenshots e verificar os problemas que ele

11:02

está tendo na hora de desenvolver.

11:04

Então, aqui nesse momento,

11:06

o sistema ali está com erro e etc. Então, esses aí são pontos. E aqui,

11:11

implementando o painel de admin que ele está trabalhando ainda aqui com esse cara.

11:17

Então, as coisas estão indo.

11:21

Esse cara aqui do pipeline,

11:24

de background, de processing, já tá rodando, tá? Então,

11:28

ele tá na parte dos testes agora aqui, aplicando migrações,

11:32

fazendo as verificações. Ele pediu pra mim a chave da OpenAI e eu passei pra ele.

11:38

E somente uma curiosidade,

11:40

aqui no Cloud, no caso do Cloud Code, mas isso não é obrigatório,

11:43

toda vez que você cria uma WorkTree dentro da pasta Cloud,

11:47

ele cria uma pasta chamada WorkTrees, e aqui tem as WorkTrees aqui dentro. Então,

11:51

se você estiver no main, pelo menos você consegue acessar os arquivos da WorkTree.

11:55

Isso não é obrigatório, tem gente, inclusive,

11:57

que não gosta. Eu não gostava, hoje em dia eu acostumei mais,

12:00

porque eu consigo ir acompanhando caso eu precise,

12:02

caso eu precise, na realidade...

12:05

ter acesso a ver o que está acontecendo aqui com cada parte dos arquivos.

12:09

E aqui ele já está rodando os critérios de aceitação, daqui a pouco eu volto aí.

12:16

E bom pessoal, o nosso agente aqui acabou de terminar uma das tarefas,

12:22

deixa eu tentar colocar aqui melhor para a gente ver,

12:26

que é a do background processing.

12:29

Então aqui ele gerou aquele relatório final para a

12:31

gente conseguir dar uma olhada no que aconteceu.

12:34

Então, o que acontece? Feature Set, ele falou que teve um sucesso,

12:37

que ele fez as cinco fases com cinco commits,

12:40

usando o branch da WorkTree Background Processing.

12:43

Ele falou que ele checou os critérios de aceitação, ou seja,

12:47

a pipeline roda e valida, transcreve,

12:50

resume e está pronta para intervenção manual.

12:53

Ele colocou os testes que ele fez, validou, ou seja,

12:58

ele pegou basicamente os critérios de aceitação e rodou

13:01

um a um para verificar se tudo funcionou.

13:03

Depois ele pegou também o cross-feature integration, ou seja,

13:07

como que eu pego da integração da feature 3 que faz o

13:11

upload e gruda no pipeline dele para que ele consiga fazer a transcrição.

13:16

Aqui tem a parte do que ele mudou. Na realidade,

13:20

Ele fez um raw update para retornar os dados no...

13:26

Na tabela, não no formato aqui do Prisma Camel Case.

13:31

Aqui, na realidade, ele criou, na realidade,

13:33

E mostrou como que ele fez uma adaptação por

13:36

Conta de alguma situação que estava acontecendo.

13:38

Eu não quero entrar nesses detalhes,

13:39

Mas aqui ele traz um desvio. E aqui, soft fails.

13:44

Ele falou que nenhum... Ele rodou ali o runtime,

13:48

O smoke check tinha sido pulado pelo npm run build,

13:52

Mas ele rodou com todas as rotas colocadas,

13:56

Não teve failures. E aqui, overrides applied.

14:00

Aqui ele falou, nada além do que o usuário tinha pedido,

14:03

Anunciado, foi feito na transcrição.

14:07

Basicamente, ele manteve a OpenAI API

14:11

Key no ambiente de .env .example.

14:15

Ele fez no passo número 1,

14:18

E aqui ele colocou uma nota, olha,

14:20

A sua OpenAI Key já foi preenchida no .env.local,

14:23

Porque eu mesmo preenchi durante o passo 2. Então ele coloca agora,

14:28

Para você testar no pipeline de CI/CD,

14:33

Basta você colocar OpenAI Fake 1, que vai substituir as chamadas reais,

14:37

Mas ele falou aqui que todos os testes rodaram sem

14:40

Custo de API quando eu coloco dessa forma.

14:42

Ele coloca, para rodar o worker,

14:44

Eu tenho que dar o npm run dev e vai ter um

14:49

Hook chamado instrumentation que vai inicializar o loop automaticamente no caso o

14:55

Vídeo Max Pipeline 1 estiver enabled então é basicamente isso que ele

15:01

Colocou, mas eu tenho todas as minhas dúvidas nesse momento, é ok,

15:06

Mas essa parada toda funcionou ou não funcionou?

15:10

Como que eu vejo? Eu pergunto para ele, eu testo,

15:14

Como é que eu vou fazer? Então, eu vou parar esse vídeo agora,

15:16

Enquanto as outras sessões estão rodando,

15:19

E eu vou focar nessa sessão aqui somente para

15:21

A gente ver aqui de cara essa funcionalidade,

15:25

Se ela funcionou, o ajuste que a gente vai precisar fazer e etc. Em tese,

15:30

A IA falou que está tudo certo ali com a gente. Então, vamos ver.

## Resumo IA

**Abreviações**
*   **PRD**: Product Requirements Document
*   **IA**: Inteligência Artificial
*   **CI/CD**: Continuous Integration/Continuous Deployment
*   **API**: Application Programming Interface
*   **IDE**: Integrated Development Environment

**Resumo**
A aula teve como objetivo demonstrar a utilização do Git Worktree para viabilizar o desenvolvimento paralelo de múltiplas features simultaneamente, sem os problemas de concorrência de arquivos e estados inconsistentes. O conceito central é que o Git Worktree permite materializar múltiplos branches em diretórios separados na mesma máquina, criando um espelho operacional de cada branch com isolamento suficiente para rodar agentes, testes e mudanças locais sem interferir no trabalho de outras frentes. Isso é crucial não só para o Git, mas também para o runtime local e artefatos temporários gerados por diferentes agentes.

As ferramentas e conceitos abordados incluem:
*   **Git Worktree**: Recurso nativo do Git que cria cópias de trabalho independentes, cada uma associada ao seu próprio branch.
*   **Orquestradores e IDEs**: Como Cloud Code, Cursor e Claude Desktop, que podem integrar-se ao Git Worktree para gerenciar sessões de desenvolvimento.
*   **PRD.md**: Documento utilizado para guiar o desenvolvimento das features.
*   **OpenAI, FFmpeg, Whisper**: Ferramentas e APIs mencionadas na pipeline de processamento de vídeo e transcrição.
*   **Testcontainers**: Ferramenta mencionada para testes.
*   **Variáveis de ambiente**: Utilização de `.env.example` e `.env.local` para gerenciamento de credenciais.

O fluxo explicado pelo instrutor seguiu os seguintes passos:
1.  **Preparação para Desenvolvimento Paralelo**: O instrutor introduziu o cenário de rodar três features (Background Processing, Video Library e Painel Administrativo) simultaneamente, destacando a necessidade do Git Worktree.
2.  **Criação e Início de Worktrees Dedicadas**:
    *   Para a feature "Background Processing Pipeline", foi utilizado o comando `cloud --work-tree "Background Processing"` para iniciar o Cloud Code já dentro de uma worktree nomeada.
    *   Para as features "Video Library" (Feature 04) e "Painel Administrativo" (Feature 12), o instrutor utilizou o Claude Desktop para iniciar sessões separadas, cada uma em uma worktree, associadas às respectivas features.
3.  **Execução de Skills com Contexto Explícito**: Em cada sessão isolada, a skill `implement feature` foi invocada, recebendo o `PRD.md` e o ID da feature. Foi demonstrado como passar instruções específicas ao agente, como a solicitação da chave da OpenAI, com a diretriz de registrá-la no `.env.example` em vez de embutir credenciais.
4.  **Monitoramento da Execução**: Durante o desenvolvimento, o instrutor acompanhou o progresso dos agentes, observando a exploração do codebase, resolução de portas, navegação na interface e detecção de erros.
5.  **Análise do Relatório Final e Validação**: Após a conclusão da feature "Background Processing", o agente gerou um relatório detalhado consolidando fases, commits, validação de critérios de aceitação e integrações entre features. O instrutor enfatizou que este relatório serve como ponto de partida para a validação humana, que é crucial para verificar a funcionalidade real e a integração de ponta a ponta.
6.  **Gerenciamento de Credenciais e Ambiente**: Detalhou-se a prática de registrar a chave da OpenAI no `.env.example`, preenchê-la no `.env.local` e a criação de um modo "fake" (`OPENAI_FAKE=1`) para testes em CI/CD sem custo de API.

**Pontos de atenção**
*   **Evitar o "Caos" sem Worktree**: Iniciar várias features em paralelo a partir do mesmo branch ou em diretórios distintos sem Worktree pode gerar conflitos de arquivos, estado local inconsistente e dificuldade para validar implementações separadas. O problema vai além do Git, afetando também o runtime local e comandos executados.
*   **Isolamento de Contexto**: Cada Worktree deve prover isolamento suficiente para que testes, agentes e mudanças locais não interfiram no trabalho das outras frentes de desenvolvimento.
*   **Contexto Explícito na Execução**: Iniciar cada sessão de desenvolvimento já dentro de uma Worktree dedicada à feature correspondente reduz o setup manual, deixa explícito o contexto de cada agente e facilita o rastreamento do branch, modelo e estado do repositório.
*   **Organização de Sessões Paralelas**: Identificar claramente cada sessão com o número ou nome da feature evita confusão operacional e permite acompanhar individualmente o progresso, logs e bloqueios em ambientes com muitas execuções simultâneas.
*   **Importância da Exploração Inicial**: Mesmo em execução paralela, o agente precisa inspecionar features anteriores, convenções estabelecidas e o grafo de dependências do projeto para garantir que a nova feature respeite integrações existentes e padrões de infraestrutura (ex: uso de Testcontainers, resolução de portas).
*   **Supervisão Humana Contínua**: A execução paralela de agentes não elimina a necessidade de supervisão humana. Ela redireciona o trabalho para monitoramento e intervenção pontual, observando se o agente está resolvendo problemas (portas, erros) e se a implementação avança de forma saudável.
*   **Relatório do Agente vs. Validação Humana**: O relatório final do agente é uma evidência auditável e um ponto de partida valioso, mas não substitui a validação humana. É essencial verificar se a funcionalidade realmente opera como prometido e se integra corretamente ao sistema. A validação deve ser de ponta a ponta, verificando a conexão entre features e o fluxo completo do sistema.
*   **Gerenciamento Seguro de Credenciais**: Credenciais e chamadas externas (como a API da OpenAI) devem ser tratadas de forma controlada. Boas práticas incluem o registro de variáveis no `.env.example`, o preenchimento da chave real no `.env.local` e a criação de modos "fake" (ex: `OPENAI_FAKE=1`) para testes em desenvolvimento e CI/CD sem custo ou dependência externa.
*   **Git Worktree é Recurso Nativo**: O Git Worktree é um recurso do próprio Git, o que significa que seus conceitos e benefícios são aplicáveis independentemente da ferramenta de IA ou IDE utilizada.
*   **Estrutura de Pastas Agregadoras (Opcional)**: Algumas ferramentas (como Cloud Code) podem criar pastas agregadoras (ex: `WorkTrees`) para organizar os diretórios de trabalho. Embora não seja um requisito do Git, isso pode facilitar a inspeção manual dos arquivos de diferentes Worktrees.