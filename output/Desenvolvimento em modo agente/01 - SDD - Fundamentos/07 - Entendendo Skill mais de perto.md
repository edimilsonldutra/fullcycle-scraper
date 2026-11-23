Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17771)

## Resumo da aula

Uma skill pode ser armazenada em uma pasta como .cloud, mas não depende de uma ferramenta específica. O ponto central é o conteúdo instrucional que orienta o agente, não o ambiente em que ele está salvo. Retomando o uso de skills já discutido anteriormente, o PRD Writer é um exemplo de skill reutilizável que pode operar com diferentes agentes, desde que eles consigam interpretar o arquivo de instrução.

O PRD Writer pode existir inicialmente como um único arquivo .md, concentrando a lógica da skill e o formato esperado de saída. Separar depois o template de output é uma decisão de organização: a instrução continua definindo o comportamento, enquanto o template passa a servir como referência estrutural. Essa separação reduz acoplamento entre regra de geração e formato final do documento.

A geração começa com um conjunto explícito de entradas: nome do projeto, pasta de output, caminho do PRD e descrição combinada com o contexto. Esses dados delimitam o escopo e evitam que o agente produza um documento genérico ou desconectado do repositório. Sem esse pacote mínimo de inputs, a skill perde capacidade de contextualização e aumenta a necessidade de inferência.

Antes de escrever qualquer seção, a skill precisa confirmar o que será feito e validar esse entendimento com o usuário. Em seguida, ela inspeciona pastas e documentos para descobrir se está lidando com um projeto novo ou com algo já existente. Essa etapa reduz ambiguidade e impede que o PRD seja construído sem considerar restrições reais do projeto.

A clarificação obrigatória funciona como uma entrevista conduzida por prompt. A qualidade dessas linhas de instrução determina quanto o agente vai iterar, quantas perguntas fará e quão profundo será o refinamento antes da escrita. Um prompt superficial acelera a geração, mas tende a produzir lacunas; um prompt mais exigente aumenta o tempo de interação, porém melhora a precisão do PRD.

Depois da clarificação, a skill entra na fase de construção usando primeiro o que já foi respondido pelo usuário. Quando uma informação não existe, o agente infere com base no contexto disponível, em vez de bloquear o fluxo. Esse equilíbrio é importante porque evita tanto a dependência total de respostas manuais quanto a geração arbitrária sem fundamento.

Cada item relevante do produto vira uma feature identificada por um ID como F01 ou F02. Esse identificador cria rastreabilidade entre descrição, histórias e futuras etapas de especificação técnica. Em vez de tratar o PRD como texto solto, a skill o organiza em unidades nomeadas que podem ser referenciadas ao longo do desenvolvimento.

Retomando a estrutura de PRD já introduzida anteriormente, o avanço aqui está em como a skill preenche seções como sumário executivo, problema, oportunidade, audiência, objetivos e métricas. A audiência tem papel decisivo porque define quem usa o produto, quais necessidades esse público possui e que experiência espera encontrar. Essas características não ficam isoladas no documento: elas alimentam diretamente a formulação das histórias de usuário.

Quando o PRD identifica uma feature, ele passa a gerar histórias compatíveis com as capacidades dessa feature. Retomando os exemplos de registro, reset de password e upload em drop zone, cada história descreve uma intenção do usuário vinculada a uma funcionalidade concreta do produto. A relação correta não é “histórias soltas geram features”, mas sim “features identificadas no PRD sustentam as histórias que expressam seu uso”.

A seção de funcionalidades precisa registrar não apenas o nome da feature, mas também o que ela faz e qual experiência o usuário deve ter ao utilizá-la. Isso aproxima o PRD de um artefato operacional, porque a feature deixa de ser apenas uma etiqueta e passa a carregar comportamento e expectativa de uso. Essa definição é o que permite transformar intenção de produto em implementação verificável.

Consumes and Provides descreve dependências funcionais entre features: uma fornece informação e outra a consome. Essa ligação é especialmente importante quando o desenvolvimento ocorre em paralelo, porque explicita como as partes do sistema se conectam sem depender apenas de interpretação implícita. Uma das maiores dificuldades em SDD está justamente em modelar essas relações de forma clara, já que features isoladas são fáceis de listar, mas difíceis de integrar corretamente.

## Transcrição

00:01

Bom, pessoal, o seguinte, tá? Nós temos aqui, então, o nosso PRD Writer, tá?

00:07

E essa aqui é uma skill, tá? Tá aqui numa pasta .cloud, mas, novamente,

00:12

você poderia estar usando isso com Codex ou com qualquer outra ferramenta.

00:16

É uma skill, pode ser utilizada em qualquer lugar, tá?

00:20

Dentro dessa skill, eu tenho esse PRD Writer, onde eu tenho apenas um skill .md.

00:25

Depois eu vou separar o template do output dele como

00:29

referência para não ficar somente no arquivo de skill,

00:31

tá? Mas o grande ponto aqui é o seguinte.

00:36

Nesse nosso PRD Writer,

00:39

eu vou apenas passar pelas principais fases sem dar... tantos detalhes,

00:47

porque a gente vai ter esses detalhes maiores na hora que

00:52

depois que a gente terminar o

00:54

desenvolvimento da geração do nosso arquivo.

00:59

Eu acho que vai ficar mais claro.

01:01

Mas lembrando que nós tivemos aqui essas

01:06

cinco fases que eu acabei mostrando para vocês.

01:10

Então... Primeira coisa, ele precisa dos inputs,

01:12

o nome do projeto, a pasta de output,

01:15

o caminho que vai ao PRD e a descrição combinada com o contexto.

01:22

Então, aqui ele tem um processo muito claro.

01:25

Primeiro, entender o que vai ser feito e confirmar o

01:29

cara se ele entendeu realmente o que é.

01:31

Explorar o contexto do projeto, olhar pastas, olhar os documentos,

01:35

entender se o projeto é novo ou não e etc.

01:38

Aí nós temos o que? Uma classificação, clarificação obrigatória, ou seja,

01:45

tem um prompt aqui que basicamente ele vai

01:49

fazer com que nós tenhamos essa nossa entrevista, tá?

01:54

Eu adaptei inclusive parte desse prompt através de uma skill chamada Grilled Me,

01:58

depois eu vou passar para vocês,

02:00

ele ajuda muito de como que isso funciona. Mas o grande ponto aqui é...

02:05

Esse prompt, essas linhas aqui,

02:07

é aquilo que vai fazer com que você fique ali

02:10

iterando por muito tempo ou por pouco tempo,

02:12

depende do nível de profundidade que você quer fazer.

02:16

Depois disso, a gente vai para a construção. Ou seja,

02:19

se tem pergunta que já foi respondida pelo usuário,

02:22

usa a pergunta respondida. Senão,

02:25

você vai inferir e tentar entender de

02:31

como você vai gerar baseado nos detalhes.

02:33

E aí... Ele tem uma regra bem básica aqui, é que para tudo que ele for fazer,

02:38

ele vai gerar uma feature e cada feature vai receber um ID. F01, F02, etc, etc.

02:44

E aqui nós vamos ter as nove seções do nosso PRD.

02:49

Ou seja, sumário executivo, ou seja, o que é o produto,

02:53

para quem é, qual é o core value dele, como que ele funciona em alto nível.

03:00

Problema e oportunidade.

03:02

Outro ponto, audiência. Por que a audiência aqui é importante?

03:07

Porque a audiência em si fala quem vai usar o produto.

03:11

E quando você fala quem vai usar o produto,

03:14

quem vai usar o produto normalmente tem necessidades diferentes e

03:19

experiências que ele espera ter para que o produto funcione.

03:23

Então, a gente vai pegar algumas características de tudo isso,

03:29

ou seja, do comportamento desse tipo de público.

03:33

e ver como que nós conseguimos utilizar isso

03:37

para que a gente possa fazer o quê?

03:43

Gerar as nossas, vamos dizer, histórias de usuário ali na frente. Então,

03:49

eu vou ter o objetivo do produto e eu vou ter também

03:53

algumas métricas que eu considero que, quando elas são alcançadas,

03:56

o meu produto também está funcionando da forma como eu queria.

03:59

E aqui, então, a gente entra na parte interessante, que são as histórias. Ou seja,

04:05

eu quero fazer o registro de autenticação. Então, eu falo, eu como usuário,

04:11

eu quero registrar meu e-mail e senha, então eu consigo acessar a plataforma.

04:15

Eu, como usuário, eu quero resetar meu password via e-mail,

04:19

então eu quero recuperar a minha conta. Eu quero fazer um upload de vídeo,

04:23

então eu consigo jogar o vídeo numa drop zone para ele começar. Entendeu? Então,

04:27

se você perceber...

04:29

ele vai gerar aqui para a gente um monte de

04:31

histórias de usuário baseadas nas possibilidades que determinada feature vai existir. Então,

04:38

o que você vai entender é que, com base nessas informações aqui todas,

04:43

nós temos uma lista de features que vão ser necessárias

04:47

para essas histórias serem geradas para a gente,

04:50

tá? Ou seja, cada história vai ser gerada através de uma feature.

04:57

que o nosso PRD vai perceber que ele vai ter que fazer.

05:00

Então, esse aqui que é o grande importante. E aqui estão as funcionalidades.

05:04

E essas funcionalidades, elas são pontos extremamente importantes,

05:08

porque vão trazer para a gente qual é a feature e o que ela faz,

05:13

e qual é a experiência que o usuário tem que ter naquela determinada feature. E aí,

05:21

a gente vai entrar em outro aspecto em relação à parte de 'Consumes and Provides',

05:26

que eu não vou falar agora especificamente, tá?

05:30

Eu vou falar principalmente quando a gente for trabalhar de forma paralela,

05:33

mas basicamente eu vou falar aqui, uma feature consome outra feature,

05:38

e outra feature provê informação para outra feature que vai consumi-la.

05:43

Quando você faz isso, você consegue conectar... as features, tá?

05:48

Essa é a maior dificuldade que grande parte

05:52

dos desenvolvedores que vão trabalhar com SDD têm. Inclusive,

05:56

eu vou pausar o vídeo aqui e vou trazer um

06:00

detalhe e problemas clássicos que acabam acontecendo ali nesse momento.

## Resumo IA

**Abreviações**
*   **PRD**: Product Requirements Document
*   **MD**: Markdown
*   **ID**: Identifier
*   **SDD**: Software-Driven Development

**Resumo**
A aula abordou o processo de geração de um Product Requirements Document (PRD) utilizando uma "skill" nomeada PRD Writer. O objetivo central é demonstrar como uma skill de inteligência artificial pode estruturar e preencher um PRD de forma contextualizada e rastreável.

A skill é apresentada como uma entidade agnóstica a ferramentas e ambientes (como .cloud ou Codex), cujo valor reside no seu conteúdo instrucional. Inicialmente, o PRD Writer pode ser um único arquivo .md, mas recomenda-se separar o template de output para reduzir o acoplamento entre a lógica de geração e o formato final do documento.

O fluxo de geração do PRD começa com um conjunto explícito de entradas, incluindo nome do projeto, pasta de output, caminho do PRD e uma descrição combinada com o contexto. Essas informações são cruciais para delimitar o escopo e evitar a geração de um documento genérico.

Em seguida, a skill executa as seguintes fases:
1.  **Entendimento e Confirmação**: Confirma com o usuário o escopo do que será feito.
2.  **Exploração de Contexto**: Inspeciona pastas e documentos existentes para identificar se o projeto é novo ou já está em andamento.
3.  **Clarificação Obrigatória**: Conduz uma "entrevista por prompt" para refinar o entendimento, onde a profundidade do prompt determina o nível de detalhe e iteração.
4.  **Construção**: Prioriza as respostas do usuário e infere informações ausentes com base no contexto, evitando bloqueios no fluxo.
5.  **Geração de Features e Histórias**: Cada item relevante do produto é identificado como uma feature com um ID único (ex: F01, F02) para rastreabilidade. As nove seções do PRD são preenchidas: Sumário Executivo, Problema, Oportunidade, Audiência, Objetivos do Produto, Métricas, Histórias de Usuário, Funcionalidades e Consumes and Provides. A audiência desempenha um papel fundamental, pois suas necessidades e expectativas de experiência guiam diretamente a formulação das histórias de usuário. As histórias são geradas a partir das features identificadas, descrevendo a intenção do usuário em relação à funcionalidade.
6.  **Definição de Funcionalidades**: Detalha não apenas o nome da feature, mas também o que ela faz e a experiência esperada pelo usuário.
7.  **Consumes and Provides**: Descreve as dependências funcionais entre features, explicitando quais provêm e quais consomem informações, crucial para o desenvolvimento paralelo e a integração do sistema.

**Pontos de atenção**
*   **Agnosticismo da Skill**: O valor de uma skill reside em seu conteúdo instrucional, não na ferramenta ou ambiente onde é armazenada (ex: .cloud, Codex).
*   **Separação de Preocupações**: Separar o template de output da lógica principal da skill (.md) é uma boa prática para reduzir o acoplamento entre as regras de geração e o formato final do documento.
*   **Inputs Explícitos**: Um conjunto mínimo de inputs bem definidos (nome do projeto, pasta de output, caminho do PRD, descrição e contexto) é essencial para garantir que o PRD gerado seja específico e contextualizado, evitando a produção de documentos genéricos.
*   **Qualidade do Prompt de Clarificação**: A qualidade e a profundidade das linhas de instrução no prompt de clarificação determinam o nível de iteração, o número de perguntas e a precisão do refinamento antes da escrita do PRD. Prompts superficiais podem acelerar a geração, mas com risco de lacunas.
*   **Equilíbrio entre Resposta e Inferência**: A skill deve usar informações respondidas pelo usuário e inferir quando dados estão ausentes, mas sempre baseando-se no contexto disponível, para evitar tanto a dependência total de respostas manuais quanto a geração arbitrária.
*   **Rastreabilidade de Features**: A atribuição de um ID único (ex: F01, F02) a cada feature é crucial para criar rastreabilidade ao longo do desenvolvimento e evitar que o PRD seja tratado como um texto isolado.
*   **Importância da Audiência**: A definição da audiência é um ponto decisivo, pois molda as necessidades do público-alvo, as experiências esperadas e, consequentemente, alimenta diretamente a formulação das histórias de usuário.
*   **Relação Feature-História**: As histórias de usuário devem ser geradas com base nas features identificadas no PRD ("features identificadas no PRD sustentam as histórias"), e não o contrário.
*   **Definição Detalhada de Funcionalidades**: As funcionalidades devem registrar não apenas o nome, mas também o que a feature faz e qual a experiência esperada pelo usuário, transformando-as em artefatos operacionais.
*   **Modelagem de Dependências (Consumes and Provides)**: Descrever explicitamente as dependências funcionais entre features (quais consomem e quais provêm) é fundamental para projetos complexos e desenvolvimento paralelo, sendo uma das maiores dificuldades em SDD.