Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16857)

## Resumo da aula

Evaluation pode medir duas coisas diferentes: o comportamento do modelo sob o mesmo prompt ou o comportamento de prompts diferentes sobre um mesmo modelo. Na avaliação de modelo, a variável principal é o modelo; na avaliação de prompt, a variável principal é a instrução. Essa distinção importa porque muda o experimento inteiro: o que fica fixo, o que varia e o que a equipe pode concluir com segurança. Neste contexto, o foco está em isolar o efeito do prompt para entender como a instrução altera qualidade, custo e performance da execução.

O prompt é um ponto sensível porque pequenas alterações de redação podem melhorar ou degradar o resultado gerado pela LLM. Retomando o cenário já conhecido de comparação entre versões, a diferença entre duas instruções aparentemente parecidas pode produzir comportamentos bem distintos. Por isso, a avaliação não serve apenas para validar uma versão atual, mas para detectar regressões e ganhos reais quando o prompt evolui. Em sistemas voltados a produtividade ou aplicações em produção, essa sensibilidade torna o prompt um componente que precisa de controle técnico.

Qualquer processo de avaliação de prompt começa com três perguntas-guia: por que avaliar, como avaliar e quem vai avaliar. O “por que” define o objetivo da avaliação, isto é, qual propriedade do prompt precisa ser medida ou comparada. O “como” determina o tipo de avaliação, os testes e a forma de medir o resultado de acordo com esse objetivo. O “quem” define o evaluator, isto é, a entidade responsável por julgar a saída, o que influencia custo, consistência e escalabilidade do processo.

Definir o objetivo é a etapa mais difícil porque obriga a explicitar o que realmente se quer melhorar ou verificar. Sem isso, a equipe até consegue testar prompts, mas não consegue escolher métricas, tipos de avaliação nem evaluators de forma coerente. O objetivo funciona como a restrição de projeto do experimento: ele delimita o que conta como sucesso e evita avaliações genéricas demais. Quando o objetivo muda, o restante do processo de evaluation também muda.

Os tipos de avaliação respondem à pergunta “como medir” depois que o objetivo já está claro. Como existem várias formas de testar prompts, a escolha do método precisa ser compatível com o que se quer observar, por exemplo comparação entre versões, comportamento em produção ou análise de qualidade sob um critério específico. Essa camada operacionaliza o objetivo em procedimentos concretos. Sem essa ponte, a avaliação fica conceitual demais para orientar decisões de engenharia.

Evaluators são os agentes que executam o julgamento da saída produzida pelo prompt. Como há várias possibilidades de avaliação, também há várias formas de definir quem avalia, e essa escolha afeta a confiabilidade do processo. Um evaluator adequado precisa ser compatível com o objetivo e com o tipo de avaliação escolhido. Em outras palavras, não basta saber o que medir; é preciso decidir quem aplica o critério de forma consistente.

Para comparar prompts de forma justa, é necessário usar um dataset comum, isto é, o mesmo conjunto de entradas para todas as versões avaliadas. Isso reduz a confusão entre diferença de prompt e diferença de caso testado, porque a comparação passa a ocorrer sob condições equivalentes. O dataset cria uma base reproduzível para observar quais saídas são melhores ou piores diante da mesma entrada. Sem essa base compartilhada, a comparação entre prompts perde validade técnica.

Lembra da comparação estruturada entre prompts já estabelecida: ela só vira processo de engenharia quando dataset, critério e análise aparecem juntos. O critério define o que conta como melhor ou pior; a análise interpreta os resultados obtidos a partir desse critério. Essa combinação permite acompanhar, ao longo do tempo, como cada prompt está performando e se uma nova versão realmente representa melhoria. Comparar sem análise explícita produz observações soltas, não evidência utilizável.

A avaliação de prompt continua ao longo do ciclo de vida do sistema, inclusive com testes em produção quando isso fizer sentido. Retomando a ideia já conhecida de avaliação contínua, o ponto novo aqui é que essa continuidade precisa ser organizada por objetivo, tipo de avaliação, evaluator e dataset. Isso transforma testes isolados em um processo repetível de evolução. O resultado é uma base mais sólida para decidir quando um prompt melhorou, piorou ou apenas mudou de comportamento.

## Transcrição

00:01

Bom, pessoal, então vamos iniciar aí nos nossos conceitos em relação à Prompt Evaluation. A primeira coisa que a gente tem que saber, que é o objetivo desse nosso capítulo aqui, é focar bastante na avaliação do prompt em si. E o que eu estou querendo dizer? Porque, normalmente, quando a gente está falando em evaluation, de forma geral,

00:19

Essa evaluation pode ser também referente ao modelo, ou seja, você pode ter o mesmo prompt e você pode trocar os modelos para ver como isso acaba se comportando, o que é algo completamente comum. Ou seja, você vai realizar diversos testes com diversos modelos e aí você vai ver, inclusive, qual modelo está performando melhor, está gastando menos e tudo mais em relação ao mesmo prompt.

00:46

No nosso caso aqui, a gente não vai ficar focando necessariamente em mudar o modelo, tá? Nós vamos, na realidade, focar bastante em mudar o prompt e entender quais são as principais métricas, avaliadores e conceitos que a gente precisa saber para fazer isso, beleza?

01:04

O que acontece é o seguinte, o Prompt Evaluation, no final das contas, ele deixa para a gente cada vez mais claro como que a instrução que a gente dá para a LLM consegue influenciar na qualidade das respostas. Isso é algo que a gente está cansado de saber. E também tem outro ponto, às vezes uma pequena mudança que você pode fazer no Prompt pode melhorar ou degradar a performance nas execuções.

01:26

Então, quando a gente está falando em verificação, a evaluation do prompt, isso aí, de forma geral, ele é um processo que acaba sendo contínuo, tá? Inclusive, a gente vai ver, inclusive daqui pra frente, formas ou diversos tipos de testes que você pode fazer, inclusive em produção, pra conseguir verificar se um prompt é melhor que o outro ou qualquer coisa desse tipo.

01:50

O ponto importante aqui que você tem que entender é que se tem algo extremamente sensível na hora que a gente está trabalhando com IA, independente se a gente está focando em produtividade ou desenvolvimento de aplicações, isso aí está exatamente no nosso prompt. Beleza?

02:09

Agora, como que eu começo o meu processo de avaliação no meu prompt? Na realidade é o seguinte, qualquer prompt que você vai pensar em fazer uma avaliação, você tem que responder aqui três pontos importantes que eu coloquei aqui para ser um esqueminha mais fácil de você conseguir lembrar. Eu tenho que pensar o porquê, no final das contas, eu estou querendo avaliar aquele prompt.

02:33

Legal? Outra coisa, quais são os tipos de avaliação que eu vou usar? Ou seja, como que eu vou avaliar entendendo os meus porquês? E o outro ponto é quem vai fazer a avaliação? Então nós temos essas três variáveis, tá? Porque dependendo das respostas que você vai dar, o seu processo de evaluation vai ser bem diferente, tá?

02:56

Agora, uma outra coisa que é extremamente importante também aqui é como eu vou fazer a comparação de um prompt com outro prompt, que é algo extremamente comum, porque a gente consegue ver, ao longo do tempo, como a gente pode melhorar e verificar como cada prompt está.

03:14

performando. Então, para fazer isso, o que você precisa ter no final das contas também? Você vai precisar de ter um dataset, ou seja, um conjunto de dados. Você vai ter o critério para verificar, obviamente, o que eu considero algo melhor ou pior. E eu tenho, então, depois a minha análise. O dataset é importante porque ele vai ser igual

03:36

para todos os prompts que você quer trabalhar. Ou seja, com a mesma entrada, quais são as saídas que eu tenho que podem ser melhores ou que podem ser piores. Então, eu acho que, muitas vezes, o que acaba gerando uma confusão bem grande no meio de tudo isso é o quê?

03:57

É que entender o objetivo é difícil porque a gente tem que realmente pensar o que a gente está querendo. E os tipos de avaliação, principalmente, você vai perceber que a gente tem bastante. E avaliadores, a gente também tem bastante. Então, por isso que a gente tem que ter clareza do que eu quero fazer para eu poder escolher como e quem ali nesse ponto, tá?

04:18

E daqui pra frente a gente vai entrar com um nível de profundidade bem bacana pra gente entender cada um desses aspectos e também a gente tem bastante exemplo pra conseguir rodar, pra que você consiga ver as coisas aí com seus próprios olhos. Fechou? Então vamos nessa!

## Resumo IA

**Abreviações**
- LLM: *Large Language Model* (Modelo de Linguagem de Grande Porte)
- IA: Inteligência Artificial

**Resumo**
A aula introduz o conceito de Prompt Evaluation com foco específico na avaliação do prompt, e não do modelo. O instrutor destaca que, em avaliação de forma geral, é possível medir tanto o comportamento de um mesmo prompt em modelos diferentes quanto o comportamento de prompts diferentes em um mesmo modelo, mas aqui o objetivo é isolar o efeito da instrução para entender como pequenas mudanças de redação impactam qualidade, custo e desempenho das respostas geradas pela LLM.

Foi explicado que a avaliação de prompt é um processo contínuo, útil tanto para validar versões quanto para detectar regressões e ganhos reais à medida que o prompt evolui. O ponto central é reconhecer que o prompt é um componente extremamente sensível em sistemas de IA, especialmente em aplicações de produtividade e produção, pois mudanças aparentemente pequenas podem alterar significativamente o resultado.

Para iniciar uma avaliação de prompt, o instrutor propõe três perguntas fundamentais: por que avaliar, como avaliar e quem vai avaliar. O “porquê” define o objetivo da avaliação e o que se quer medir ou comparar; o “como” define os tipos de avaliação, os testes e a forma de mensuração; e o “quem” define o evaluator, isto é, a entidade responsável por julgar a saída. Essa clareza é necessária porque o objetivo determina todo o restante do experimento.

Também foi apresentada a base para comparar prompts de forma justa: usar um dataset comum, com o mesmo conjunto de entradas para todas as versões, além de um critério de avaliação claro e uma análise dos resultados. O dataset garante comparabilidade, o critério define o que é melhor ou pior, e a análise interpreta os resultados para permitir decisões técnicas. A aula encerra reforçando que, ao longo do curso, esses elementos serão aprofundados com exemplos práticos e testes, inclusive em produção quando fizer sentido.

**Pontos de atenção**
- A avaliação de prompt é diferente da avaliação de modelo: aqui a variável principal é a instrução, não o modelo.
- Pequenas mudanças no texto do prompt podem melhorar ou piorar bastante a saída da LLM.
- Avaliação de prompt deve ser tratada como processo contínuo, não como teste isolado.
- Antes de testar, é essencial definir claramente o objetivo da avaliação; sem isso, métricas, tipo de teste e evaluator ficam incoerentes.
- As três perguntas-guia — por que, como e quem — devem ser respondidas antes de iniciar qualquer experimento.
- O dataset precisa ser o mesmo para todos os prompts comparados; caso contrário, a comparação perde validade.
- É necessário definir um critério explícito do que conta como melhor ou pior, para evitar julgamentos subjetivos ou inconsistentes.
- A escolha do evaluator impacta custo, consistência, escalabilidade e confiabilidade da avaliação.
- Comparar prompts sem análise estruturada gera observações soltas, não evidência útil para engenharia.
- Avaliações em produção podem fazer parte do processo, mas precisam estar organizadas por objetivo, tipo de avaliação, evaluator e dataset.