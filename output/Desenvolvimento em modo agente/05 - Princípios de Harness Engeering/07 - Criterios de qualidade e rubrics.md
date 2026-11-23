Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17891)

## Resumo da aula

Passar ou falhar resolve apenas a parte determinística da avaliação. Em Harness Engineering, isso é insuficiente quando o resultado depende de percepção de usuário, qualidade de design, navegabilidade ou legibilidade de código. Nesses casos, a avaliação precisa capturar gradações de qualidade, não apenas conformidade mínima. A consequência prática é substituir parte do julgamento binário por escalas e critérios explícitos.

Rubrica é um conjunto de critérios claros que orienta um agente avaliador sobre o que observar e como pontuar. Em vez de perguntar apenas se algo está certo, a rubrica define dimensões de qualidade e pode incluir exemplos calibradores, como o que conta como design moderno, alinhado ou visualmente ruim. Isso reduz ambiguidade e aproxima a avaliação do padrão esperado pelo time ou produto. O ganho principal é transformar preferência implícita em regra operacionalizável.

Quando a qualidade é subjetiva, o agente precisa de referências concretas para julgar com consistência. Exemplos do tipo “isto é bonito” e “isto é feio” funcionam como ancoragem de gosto, estilo e expectativa, permitindo que o modelo aprenda o padrão desejado sem depender de interpretação genérica. Essa calibração é especialmente útil em UX, design visual e comportamento percebido pelo usuário. Sem isso, a nota tende a variar demais conforme a formulação do prompt.

A saída de uma rubrica pode ser uma nota, como uma escala de 0 a 10, em vez de um veredito binário. Essa nota alimenta um gate de qualidade: acima de um limiar, como 7, o resultado segue adiante; abaixo disso, entra em revisão. O gate converte julgamento qualitativo em decisão operacional automática. Assim, o pipeline continua automatizado sem fingir que toda qualidade pode ser reduzida a “passou” ou “falhou”.

A nota isolada tem pouco valor se não vier acompanhada de justificativa. Quando o agente avaliador explica por que atribuiu uma nota baixa — por exemplo, logo desorganizado ou elementos desalinhados — esse reasoning vira insumo direto para o agente executor revisar o trabalho. Isso fecha um ciclo de melhoria orientado por feedback estruturado, e não por tentativa cega. Retomando a separação entre execução e avaliação, o avaliador não corrige; ele diagnostica com critérios reutilizáveis.

Mesmo em contextos mais próximos de back-end, onde testes binários são comuns, ainda existem aspectos graduais de qualidade. Complexidade excessiva, clareza estrutural e qualidade geral de implementação podem ser avaliadas por rubricas quando não há uma regra mecânica suficiente para capturar o problema. Isso não substitui testes, linters ou guardrails já definidos anteriormente; complementa esses mecanismos onde o julgamento exige nuance. O uso correto é avaliar o que é importante, mas não totalmente formalizável.

O padrão de LLM as judge é especialmente útil quando o sistema precisa medir atributos subjetivos com escala e justificativa. Em cenários com datasets, agentes não voltados à codificação ou fluxos gerais com IA, esse modelo permite comparar saídas por critérios qualitativos sem depender exclusivamente de revisão humana em cada item. A utilidade cresce quando a rubrica está bem especificada e o julgamento precisa ser repetido em volume. O ponto central não é delegar gosto ao modelo, mas codificar critérios para que ele julgue de forma consistente.

Uma mesma entrega pode ser avaliada por agentes diferentes, cada um focado em uma dimensão específica. Um agente pode julgar design de página, outro navegação, outro comportamento observado e outro qualidade do código. Essa especialização melhora a precisão da avaliação porque cada rubrica fica mais estreita e mais calibrável. Em vez de um único veredito genérico, o harness passa a operar com múltiplos sinais de qualidade.

## Transcrição

00:00

Bom, pessoal, e ainda em avaliação, a gente tem que entender que muitas vezes,

00:06

simplesmente saber se uma tarefa foi terminada ou não,

00:11

ou se está passando ou não, não é o suficiente.

00:14

A gente tem que também ter critérios de qualidade. Ou seja,

00:19

nem tudo é zero ou um. Ou seja, às vezes,

00:24

muitas das coisas são referentes à percepção do usuário.

00:28

Por exemplo, eu pedi para ele fazer um sistema bonito.

00:32

Como que eu consigo definir o que é bonito,

00:34

o que é feio, referente à percepção do usuário?

00:38

Como que eu consigo realmente pegar coisas que,

00:42

na realidade, não são simplesmente fazer um código passar,

00:46

mas simplesmente fazer com que a experiência do usuário,

00:50

lá na ponta, seja muito melhor?

00:53

Ou que, ao longo do tempo, eu consiga avaliar...

00:57

se aquela complexidade determinada de um determinado código está boa ou não,

01:02

ou qualquer coisa desse tipo. Então, o que acontece?

01:08

Quando a gente vai fazer avaliações,

01:11

muitas vezes a gente vai fazer avaliações utilizando rubricas. Basicamente, o que é?

01:17

É você ter um agente,

01:19

e nesse agente você vai dar regras claras de critérios de qualidade para ele.

01:26

Você vai colocar exemplos, vou dar um exemplo muito bobo. Isso para mim é bonito,

01:30

isso é feio. Isso aqui é um design que é um estilo moderno dessa forma.

01:35

Isso aqui não é. Ou seja, você pode ir calibrando e falando, vamos dizer assim,

01:41

qual é o seu gosto, o que você espera daquilo. E aí, o que acontece?

01:46

Na hora que o agente vai avaliar aquele resultado,

01:49

ele não vai mais avaliar se está certo ou se está errado.

01:52

Ele pode dar uma nota de 0 a 10. E aí você pode ter um gate de qualidade falando,

01:57

olha, se foi acima de 7, eu deixo passar,

02:00

se não, eu mando o agente revisar.

02:03

E o mais interessante disso é que na hora que você pede para esse agente revisar,

02:09

você vai passar o reasoning do agente, ou seja,

02:12

o agente que avaliou e deu nota 3 aqui nesse caso, por exemplo, ele vai falar,

02:17

olha, o design dessa página ficou feio porque o logo não ficou...

02:23

organizado dessa forma, essa parte está desalinhada, assim assim é sábio. Ou seja,

02:29

ou a gente vai lá e consegue corrigir.

02:31

Então a gente tem que entender que nos dias de hoje, nem tudo é binário também.

02:36

Quem está muito acostumado com back-end e fazer um teste e passar ou não,

02:42

é uma coisa, mas às vezes até mesmo para o código,

02:45

você pode criar rubricas, que vão fazer o que no final das contas?

02:51

Gerar critério de qualidade.

02:53

Ou seja, a IA, através de prompts muito claros,

02:58

você consegue fazer com que ela consiga pontuar e, baseado nessa pontuação,

03:03

na justificativa,

03:05

você pode pedir para o outro agente que desenvolveu aquilo melhorar todo o processo.

03:12

E isso aí é muito comum, pessoal.

03:15

Isso na hora que você está desenvolvendo qualquer software que

03:18

se integra ou que você está trabalhando com...

03:22

IA de forma geral, você tá criando agentes não de codificação,

03:26

com datasets e tudo mais, isso aí é a coisa mais comum do mundo,

03:31

que você tem o LLM as judge, e você cria essas rubricas exatamente pra quê?

03:37

Para que em relações qualitativas

03:42

você consiga também fazer essas medições.

03:46

Porque uma coisa é você ter métricas ali quantitativas.

03:49

Zero, um, bateu. Esse número,

03:52

ele fez essas chamadas de ferramenta nessa ordem,

03:55

ele seguiu essa determinada trajetória,

03:58

mas quando a gente está falando de coisas que são mais subjetivas, ainda assim,

04:03

a gente consegue fazer essas avaliações, e isso aí é muito importante,

04:06

e nessa parte de Harness Engineering, a gente deve,

04:10

com certeza, levar em consideração,

04:13

dependendo do tipo de trabalho, onde você pode ter um agente,

04:16

sei lá, que vai avaliar o design de uma página.

04:20

Ou um agente que vai avaliar como é que está a navegação,

04:24

ou um agente que vai avaliar determinado tipo de comportamento,

04:28

ou um agente que vai avaliar até mesmo a

04:31

qualidade do código que está sendo desenvolvido. Então,

04:34

isso aí não necessariamente é binário. Então,

04:38

qualidade é algo que você pode dar uma nota e você

04:42

pode ter um gate para esse tipo de nota.

## Resumo IA

**Abreviações**
*   **UX**: User Experience
*   **LLM**: Large Language Model
*   **IA**: Inteligência Artificial

**Resumo**
Esta aula aborda a limitação da avaliação binária (passar ou falhar) em contextos de desenvolvimento de software, especialmente em Harness Engineering, onde a qualidade depende de aspectos subjetivos como percepção do usuário, qualidade de design, navegabilidade ou legibilidade de código. O objetivo é introduzir métodos de avaliação que capturem gradações de qualidade, em vez de apenas a conformidade mínima.

O conceito central é a **rubrica**, um conjunto de critérios claros que orienta um agente avaliador sobre o que observar e como pontuar. As rubricas definem dimensões de qualidade e podem incluir exemplos calibradores (o que é considerado "bonito" ou "feio", ou um estilo de design específico) para reduzir a ambiguidade e alinhar a avaliação com o padrão esperado pela equipe ou produto. Essa calibração é crucial para transformar preferências implícitas em regras operacionais e garantir consistência no julgamento, especialmente em UX e design visual.

A saída de uma rubrica é tipicamente uma nota (ex: escala de 0 a 10), que alimenta um **gate de qualidade**. Se a nota estiver acima de um limiar definido (ex: 7), o resultado prossegue; caso contrário, entra em revisão. Este gate automatiza decisões operacionais baseadas em julgamento qualitativo. Para que a nota seja útil, ela deve vir acompanhada de uma **justificativa (reasoning)**, que explica os motivos da pontuação. Esse feedback estruturado serve como insumo direto para o agente executor revisar e melhorar o trabalho, fechando um ciclo de melhoria contínua.

Mesmo em contextos de back-end com testes binários, rubricas podem complementar a avaliação de aspectos graduais como complexidade excessiva, clareza estrutural e qualidade geral de implementação. O padrão "**LLM as judge**" é particularmente útil quando sistemas precisam medir atributos subjetivos com escala e justificativa, permitindo comparar saídas por critérios qualitativos de forma consistente e em volume, sem depender exclusivamente de revisão humana em cada item. Uma mesma entrega pode ser avaliada por **múltiplos agentes especializados**, cada um focado em uma dimensão (design, navegação, comportamento, qualidade de código), aumentando a precisão da avaliação.

**Pontos de atenção**
*   **Avaliação Binária Insuficiente**: O modelo de "passar ou falhar" é inadequado para avaliar aspectos subjetivos como percepção do usuário, qualidade de design, navegabilidade ou legibilidade de código.
*   **Necessidade de Gradação**: A avaliação deve capturar gradações de qualidade, não apenas conformidade mínima, usando escalas e critérios explícitos.
*   **Rubricas Codificam Preferências**: Rubricas são essenciais para transformar preferências implícitas (gosto, estilo) em regras operacionais e critérios de avaliação claros e consistentes.
*   **Calibração com Exemplos Concretos**: Para julgamentos subjetivos, é fundamental fornecer exemplos calibradores (ex: "isso é bonito", "isso é feio") para ancorar o gosto e a expectativa, garantindo que o agente avalie de forma consistente. Sem isso, a nota tende a variar conforme a formulação do prompt.
*   **Justificativa é Crucial**: Uma nota isolada tem pouco valor. A justificativa (reasoning) do agente avaliador é um insumo direto para o agente executor revisar e melhorar o trabalho, fechando um ciclo de feedback estruturado.
*   **Avaliador Diagnostica, Não Corrige**: O papel do agente avaliador é diagnosticar problemas e pontuar com base em critérios reutilizáveis, não corrigir a entrega.
*   **Complementa Outras Ferramentas**: Rubricas não substituem testes binários, linters ou guardrails já definidos; elas os complementam onde o julgamento exige nuance e não pode ser totalmente formalizado por regras mecânicas.
*   **Especificação da Rubrica**: A utilidade do padrão "LLM as judge" e a consistência do julgamento do modelo dependem diretamente de uma rubrica bem especificada e calibrada. O objetivo é codificar critérios para julgamento consistente, não delegar "gosto" ao modelo.
*   **Especialização por Dimensão**: Dividir a avaliação de uma entrega entre múltiplos agentes especializados (ex: um para design, outro para navegação, outro para código) aumenta a precisão e a granularidade da avaliação.