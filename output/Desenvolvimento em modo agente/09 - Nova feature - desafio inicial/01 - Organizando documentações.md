Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17989)

## Resumo da aula



## Transcrição

00:01

Bom pessoal, agora a gente vai para a nossa feature número 3,

00:04

tá? Somente para você saber,

00:05

para a gente poupar tempo, o que eu fiz?

00:07

Eu pedi para o sistema, usando lá o Spec Writer,

00:10

gerar para mim a feature número 3 e ele gerou aqui para mim, ó, F3 Upload,

00:15

onde eu tenho o plano, o Spec e o Contract,

00:18

basicamente é a feature de vídeo upload aqui, tá?

00:22

Quando eu vou para essa feature de vídeo upload, basicamente,

00:28

deixa eu pegar o... o diagrama dela aqui.

00:33

Basicamente, ele vai, eu vou fazer o drop, né, do arquivo,

00:40

ele vai fazer o upload, vai bater no back-end,

00:43

vai cair aqui no FFmpeg, é fire and forget,

00:46

não tem retry, ele vai verificar aqui se vai guardar.

00:52

local fire storage aqui pra mim e ele também vai fazer

00:56

o thumbnail aqui também pra mim e guardando no disco, tá? Ou seja,

01:00

a gente tá trabalhando no disco e aqui tem a parte dos

01:04

uploads recentes de como que isso aqui é pego ali pra mim,

01:09

né? Então ele vai pegar, vai consultar a rota, vai trazer os vídeos,

01:13

vai listar os vídeos. vai passar pelos use cases,

01:16

vai cair no repositório do Prisma. Então,

01:18

é basicamente como que ele organizou isso aqui.

01:21

A grande questão não está muito nesse aspecto.

01:25

Alguns pontos que eu quero trazer aqui com você.

01:28

Um ponto que você tem que levar sempre em consideração,

01:31

e aí vai depender muito da sua equipe,

01:33

como que você trabalha, ou se essa feature você está desenvolvendo...

01:39

Não digo para você, mas dentro de um subdesenvolvimento de uma etapa,

01:43

e depois você vai juntar isso com mais alguma coisa e fazer uma pull request.

01:48

Por que eu estou dizendo isso? Estou dizendo que, nesse momento,

01:51

se você olhar, eu estou no meu branch main aqui,

01:53

tá? E no meu branch main... Opa, nossa, cara, que loucura. No meu branch main,

01:59

eu gerei essa feature, tá? Então, a minha grande questão aqui,

02:04

que a gente tem que sempre tomar cuidado,

02:06

é tudo que está em main... de forma geral, está em produção.

02:11

Então, nesse caso, se eu não comecei a desenvolver a feature,

02:16

esse meu progresso aqui desse meu PRD,

02:19

ele tem que estar pendente. Caso eu comece a desenvolver,

02:22

eu tenho que fazer a alteração desse cara.

02:25

Uma outra coisa que você tem que levar em consideração é você vai querer fazer

02:30

o commit disso e já ter isso no main para ficar disponível para todo mundo,

02:35

ou você vai gerar internamente.

02:38

vai fazer a feature e depois subir já com essa documentação.

02:42

Então, existem essas questões que você pode levar em conta.

02:46

Eu já vi esses dois aspectos sendo feitos. Ou seja,

02:52

coloca todas as features ali no docs, está no main, para todo o time ver.

02:57

Ou você fala, eu vou fazer a feature 3, você cria o seu branch,

03:02

a sua work tree ali, gera a especificação da feature.

03:06

e depois faz a pull request. Isso,

03:09

para time pequeno, talvez possa ajudar, mas normalmente,

03:11

quando a gente está trabalhando uma feature maior,

03:14

Você não vai só gerar a feature cegamente da forma como eu fiz.

03:19

A gente vai revisar, a gente vai olhar, vai iterar,

03:21

Talvez isso tenha que passar pelo code review do time para ver se essa feature,

03:26

Ela realmente vai ser desse jeito, tá? Então...

03:30

Provavelmente isso vai ficar, de forma geral,

03:32

Num branch main ou num branch de desenvolvimento,

03:35

Vai depender de como você organiza isso na sua empresa.

03:38

Mas é importante você saber o que você faz com essas especificações, tá?

03:44

Se ela fica o tempo inteiro num branch principal,

03:47

Se ela fica num branch de desenvolvimento, ou se ela não fica,

03:50

Se ela só aparece depois que ela é feita.

03:52

Então, isso são decisões que, na minha opinião,

03:54

Não tem muito certo e errado, tá?

03:57

Mas o que você tem que levar em consideração é

04:00

Que depende muito de como a sua equipe vai trabalhar.

04:06

Ou se você é um desenvolvedor solo, está desenvolvendo algo ali, então...

04:11

Você não vai criar um processo super gigante para um desenvolvedor,

04:16

Para dois desenvolvedores. Então, vai depender muito de como vocês vão trabalhar.

04:19

De forma geral, eu recomendo sempre que isso fique no main,

04:23

Público para todo mundo, para um time grande.

04:25

E, obviamente, que quando você fizer essa feature,

04:28

Por exemplo, isso vai passar para um code review.

04:30

O pessoal vai discutir e tudo mais. Ou seja,

04:33

A gente não sai fazendo as coisas cegamente. De forma geral,

04:37

Uma funcionalidade grande e importante, core, aqui dessa aplicação.

04:41

Se você olhar o PRD,

04:42

Essa feature é bloqueante para que todas as outras continuem fazendo,

04:47

Porque se eu tenho uma plataforma de upload de vídeos,

04:50

O upload de vídeo é uma das features principais

04:52

Que a gente tem que levar em consideração.

04:55

Então, esse aí é um aspecto que eu queria trazer. No próximo vídeo,

04:58

Eu quero trazer um outro aspecto que é em relação a

05:00

Arquivos ou infraestrutura base que você tem que trazer.

05:05

Para o agente, para ele conseguir desenvolver a feature. Então,

05:07

Esse aí é um outro aspecto que a gente tem que

05:10

Conseguir trabalhar e eu vou falar disso daqui a pouquinho.

## Resumo IA

**Abreviações**
*   **F3**: Feature 3
*   **PRD**: Product Requirements Document
*   **Spec**: Specification

**Resumo**
A aula teve como objetivo principal apresentar a Feature 3 (F3) de "Video Upload" e discutir a gestão de suas especificações e o ciclo de vida de desenvolvimento em um ambiente de equipe. O instrutor demonstrou o uso de uma ferramenta, o Spec Writer, para gerar automaticamente o Plano, Spec e Contract da F3.

Foi detalhado o fluxo de upload de vídeo: o usuário realiza o "drop" do arquivo, que é enviado para o back-end. No back-end, o vídeo é processado pelo FFmpeg (em um modelo "fire and forget", sem retry), armazenado no "local file storage" e tem um thumbnail gerado, ambos guardados em disco. Para a exibição de uploads recentes, o fluxo envolve consultar uma rota, trazer e listar os vídeos, passando por "use cases" e utilizando o repositório do Prisma.

A parte central da aula focou na discussão sobre a gestão dessas especificações e do desenvolvimento da feature em relação ao controle de versão (Git). O instrutor levantou a questão de se as especificações devem ser comitadas diretamente no branch `main` (ou de desenvolvimento principal) para visibilidade de toda a equipe, ou se devem ser desenvolvidas e comitadas em um branch de feature, sendo integradas posteriormente via pull request. A escolha da abordagem depende do tamanho da equipe e da organização do processo de desenvolvimento da empresa.

**Pontos de atenção**
*   **Branch `main` em produção**: É crucial entender que, de forma geral, tudo que está no branch `main` é considerado em produção.
*   **Status do PRD**: O progresso do PRD da feature deve ser mantido "pendente" se o desenvolvimento ainda não começou e atualizado assim que se inicia.
*   **Estratégias de gestão de especificações**:
    *   **Publicar no `main` (ou branch de desenvolvimento)**: Recomenda-se para times grandes, onde as especificações são comitadas no branch principal para que toda a equipe tenha visibilidade. No entanto, mesmo geradas, as especificações devem passar por revisão e discussão (code review) antes que o desenvolvimento comece "cegamente".
    *   **Manter em branch de feature**: As especificações podem ser geradas e desenvolvidas dentro de um branch de feature (work tree) e comitadas junto com o código, subindo via pull request. Essa abordagem pode ser mais adequada para times pequenos.
*   **Decisão contextual**: Não há uma regra "certa ou errada" absoluta para a gestão de especificações e features; a melhor abordagem depende fortemente do tamanho e da dinâmica da equipe, e de como a empresa organiza seus processos.
*   **Revisão e iteração**: Mesmo com especificações geradas automaticamente, é fundamental revisar, olhar e iterar sobre elas, além de submetê-las a code review para garantir que a feature realmente atenda aos requisitos esperados.
*   **Features core e bloqueantes**: Funcionalidades como o upload de vídeo em uma plataforma de vídeos são consideradas core (essenciais) e frequentemente bloqueantes para o desenvolvimento de outras funcionalidades, destacando a importância de seu planejamento e execução.