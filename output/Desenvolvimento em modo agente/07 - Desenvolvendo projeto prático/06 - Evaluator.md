Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17981)

## Resumo da aula

Um evaluator é um agente separado usado para verificar uma feature já implementada com base no contrato definido anteriormente. Retomando o contract.md, ele continua sendo a referência dos critérios de aceitação; a novidade aqui é adicionar uma segunda camada de validação, independente da autoverificação feita pelo agente implementador. Essa separação importa porque um agente externo pode encontrar desvios que passaram despercebidos por quem executou a implementação. O ganho principal é uma visão de fora sobre a conformidade da entrega.

Adicionar um evaluator aumenta o custo operacional do fluxo, porque há mais uma execução consumindo tokens. Isso transforma a avaliação externa em uma decisão de engenharia: nem toda feature precisa desse nível extra de validação. Em fluxos mais rigorosos, vale aplicar o processo completo by the book para reduzir risco e aumentar a confiança na entrega. Em fluxos mais simples, o custo adicional pode não compensar.

A skill evaluator usa o estado do projeto e os artefatos já produzidos para executar a análise. Ela consulta o progress.json, lê o contrato da feature e recebe explicitamente qual feature deve ser avaliada. Com isso, a avaliação deixa de ser genérica e passa a ser orientada por contexto, escopo e critérios observáveis. O resultado é uma checagem alinhada ao que foi especificado, não apenas ao que parece funcionar.

A avaliação pode retornar evidências em formatos diferentes, conforme a necessidade do fluxo. Entre as saídas possíveis estão screenshots, um report final e mensagens no chat com as descobertas encontradas. Isso permite combinar evidência visual, resumo consolidado e feedback textual no mesmo processo. A utilidade prática é facilitar tanto a inspeção humana quanto a decisão automatizada sobre aprovação ou correção.

O evaluator segue uma sequência operacional: carregar o projeto, acessar o contrato e executar verificações para confirmar se está tudo ok. Como o contrato já foi definido antes, ele funciona aqui como checklist executável para a análise. A qualidade da avaliação depende menos de opinião subjetiva e mais da aderência aos critérios já estabelecidos. Esse desenho reduz ambiguidade e torna a validação mais previsível.

O tamanho ideal de uma skill depende do contexto de avaliação. Em alguns casos, uma skill curta basta; em outros, faz sentido explicitar muitos steps para restringir melhor o comportamento do agente e garantir que ele siga um procedimento verificável. Essa escolha é controversa porque envolve preferências de estilo e confiança no modelo. Quanto mais detalhado o passo a passo, maior o controle; quanto mais enxuta a skill, maior a dependência de inferência.

À medida que os modelos ficam mais capazes, parte dos passos explícitos pode ser removida sem perder qualidade de execução. Isso acontece porque o agente passa a inferir melhor a intenção operacional a partir de menos instruções. Ainda assim, reduzir steps cedo demais pode enfraquecer a consistência da avaliação, especialmente em fluxos críticos. O ponto de equilíbrio está em ajustar o nível de detalhamento ao risco e à maturidade do modelo.

## Transcrição

00:01

Bom, pessoal, agora que ele terminou essa parte do desenvolvimento,

00:05

a gente entra em outro aspecto aqui,

00:08

que é a parte dos evaluators, tá?

00:10

E é aqui que a gente tem que começar a tomar muito cuidado.

00:14

Por que eu estou dizendo isso? Nós temos aqui uma feature,

00:18

e essa feature foi desenvolvida,

00:20

tá? Porém, nós temos aqui o nosso querido amigo aqui,

00:24

chamado de contract.md.

00:27

E esse contrato é o que definiu, basicamente,

00:30

os critérios de aceitação pra que essa página ficasse do jeito que a gente queria,

00:35

tá? E agora, o que eu tenho que fazer é,

00:38

como que eu consigo colocar um outro agente, tá? Pra quê?

00:42

Pra que ele consiga verificar o trabalho desse camarada.

00:46

Esse cara, ele se autoverificou, tá? Em tese,

00:50

ele fez o trabalho certo. Por outro lado,

00:52

a gente sabe que ter um agente separado para isso vai conseguir

00:57

ter uma visão de fora e eventualmente pegar problemas que acabam acontecendo,

01:02

tá? Não sei se ele vai pegar problema agora,

01:04

não sei se vai deixar de pegar e tudo mais,

01:06

mas é importante que a gente saiba que nós temos um outro avaliador.

01:12

Um outro ponto importante também no meio dessa história.

01:15

Uma vez que você tem um outro avaliador,

01:17

você vai ter mais custo no meio desse processo,

01:20

porque vai ser mais a gente rodando, gastando mais tokens. Então sempre vai,

01:24

você determina se você vai querer colocar um evaluator em cima disso ou não, tá?

01:30

Aqui eu estou fazendo by the book para que a gente veja todo esse processo,

01:34

beleza? Então vamos nessa, aqui se a gente olhar, nós

01:40

temos um...

01:43

Cadê o nosso camarada? Um camarada chamado de evaluator.

01:48

Cadê o nosso camarada? Evaluator.

01:51

Isso aqui é uma skill, tá? E essa skill, basicamente, o que ela vai fazer?

01:55

Ela vai olhar o nosso progress.json, inclusive, ela vai ver o nosso contract,

02:00

a gente vai falar qual é a feature que a gente quer que ela avalie,

02:03

e daí ela vai avaliar e também dar a resposta do que ela achou em relação àquilo,

02:10

né? Então, ela vai trazer... aqui para mim.

02:12

Então ela pode trazer em formatos de screenshots,

02:15

ela pode gerar um report final e ela pode colocar

02:17

no chat quais foram as descobertas ali para ela.

02:20

Então tem todos os passos das resoluções que ela pode utilizar.

02:25

Novamente, eu não vou ficar aqui, vamos dizer assim...

02:29

explicando, lendo cada detalhe, porque eu acho que você pode olhar,

02:33

ler com calma e etc, mas basicamente ela vai olhar o projeto,

02:37

vai carregar o projeto e vai acessar aquele contrato,

02:40

vai fazer as verificações para ver se está tudo ok. Então assim, são bastante steps.

02:47

Eu sou uma pessoa que eu gosto de criar skills bem pequenas,

02:49

mas dependendo do que eu for avaliar,

02:52

eu gosto de ser bem restritivo, tá?

02:54

E isso aí é meio que controverso, tem gente que gosta,

02:57

tem gente que não gosta. Então, dependendo do contexto,

03:00

eu quero uma skill que tenha meia dúzia de linhas.

03:04

E dependendo do contexto, eu prefiro que uma skill seja mais completa,

03:07

que eu consiga seguir passo a passo do que ela tem que fazer. Então,

03:11

isso vai depender e, obviamente, quanto mais inteligente o nosso modelo fica,

03:15

esses passos a gente vai diminuindo porque ele já consegue fazer por inferência. Então,

03:21

o nosso passo agora aqui vai ser deixar para a gente rodar o nosso evaluator.

03:28

Eu vou fazer isso no nosso próximo vídeo.

## Resumo IA

**Resumo**
A aula introduz o conceito de "evaluator" como um agente separado, cuja finalidade é verificar uma feature já implementada com base no contrato previamente definido em `contract.md`. Este contrato continua sendo a referência para os critérios de aceitação. A adição do evaluator cria uma segunda camada de validação independente da autoverificação realizada pelo agente implementador, proporcionando uma visão externa que pode identificar desvios não percebidos internamente.

O fluxo de trabalho com um evaluator envolve uma "skill evaluator" que consulta o estado do projeto em `progress.json`, lê o `contract.md` e recebe explicitamente qual feature deve ser avaliada. Com base nesses dados, a skill carrega o projeto, acessa o contrato e executa verificações para confirmar a conformidade. A avaliação pode retornar evidências em diversos formatos, como screenshots, um report final e mensagens no chat com as descobertas.

**Pontos de atenção**
*   **Custo Operacional**: Adicionar um evaluator aumenta o custo operacional do fluxo, pois envolve mais uma execução e o consumo adicional de tokens. Esta é uma decisão de engenharia; nem toda feature requer este nível extra de validação.
*   **Aplicação Seletiva**: Em fluxos mais rigorosos, a aplicação do processo completo com evaluator é recomendada para reduzir riscos e aumentar a confiança na entrega. Contudo, em fluxos mais simples, o custo adicional pode não compensar.
*   **Qualidade da Avaliação**: A qualidade da avaliação depende da aderência aos critérios estabelecidos no contrato, e não de opiniões subjetivas, tornando a validação mais previsível.
*   **Detalhe da Skill**: O tamanho ideal de uma skill de evaluator é controverso e depende do contexto. Skills mais detalhadas (com muitos steps) oferecem maior controle e seguem um procedimento verificável, enquanto skills mais enxutas dependem mais da inferência do modelo. Reduzir os passos cedo demais pode comprometer a consistência da avaliação, especialmente em cenários críticos.
*   **Maturidade do Modelo**: À medida que os modelos de IA se tornam mais capazes, a necessidade de explicitar muitos steps pode diminuir, pois eles conseguem inferir melhor a intenção operacional com menos instruções. O ponto de equilíbrio é ajustar o nível de detalhamento ao risco e à maturidade do modelo.