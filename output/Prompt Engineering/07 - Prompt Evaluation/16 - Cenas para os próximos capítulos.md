Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16871)

## Resumo da aula

Avaliar prompts é um processo de engenharia porque o mesmo dataset pode sustentar várias leituras de qualidade, desde que as métricas estejam alinhadas ao objetivo já definido. O ponto central não é acumular scores, mas extrair sinais úteis para decidir se um prompt atende ao comportamento esperado. Essa estrutura permite comparar versões de forma reproduzível, em vez de depender apenas de impressão subjetiva.

No mesmo experimento, convivem evaluators que julgam por meio de outro LLM e verificações mais exatas, como validação estrutural e comparações determinísticas. Retomando o cenário de revisão de código, critérios como correctness, relevance, faithfulness, conciseness e helpfulness entram como julgamento subjetivo quando um modelo atua como juiz; já schema validation, embedding similarity, string similarity e exact match entram como sinais mais objetivos. A consequência prática é que um pipeline maduro combina tipos diferentes de evidência, porque cada métrica captura uma dimensão distinta do comportamento do prompt.

Precision, recall e F1 pertencem ao grupo de métricas de classificação e exigem uma camada adicional de formalização. Elas importam quando a saída precisa decidir entre classes ou estados observáveis, como tratar um achado como erro real ou não, ou decidir se um pull request deveria receber merge. Nesse contexto, não basta um evaluator genérico: é preciso contar acertos, falsos positivos e falsos negativos, aplicar fórmulas explícitas e transformar o resultado em medida operacional de desempenho.

Essas métricas normalmente pedem implementação própria ou, no mínimo, uma instrumentação mais explícita do experimento. O fluxo envolve escrever funções, separar resultados por categoria, calcular proporções e consolidar os números em precision, recall e F1. Isso explica por que nem toda ferramenta expõe essas métricas de forma direta: elas dependem de como a tarefa foi modelada e de como a classificação foi extraída da saída do prompt ou do agente.

Retomando o mesmo cenário de revisão de código, a próxima camada não é reavaliar estilo ou utilidade, mas medir capacidade de classificar corretamente problemas. A pergunta passa a ser quantitativa: quantos problemas reais o sistema encontrou, quantos ele inventou e quantos deixou passar. Esse enquadramento é especialmente importante quando a saída do prompt influencia decisões como aprovar merge, sinalizar risco ou priorizar correções.

A lógica de classificação não se limita ao texto final gerado por um prompt isolado. Quando um agente executa vários passos intermediários, consulta contexto e produz uma decisão final, precision, recall e F1 continuam sendo formas válidas de medir o quanto esse processo acerta. O valor dessas métricas está em resumir, em números comparáveis, a confiabilidade do comportamento produzido após toda a cadeia de processamento.

A comparação pairwise entra quando o objetivo deixa de ser apenas medir um prompt isoladamente e passa a ser decidir qual de duas versões é melhor no mesmo dataset. Em vez de olhar scores independentes e inferir manualmente um vencedor, o sistema confronta duas saídas diretamente e delega o julgamento a um juiz. O ponto novo aqui é que o critério de comparação também vira prompt: o juiz precisa receber instruções explícitas sobre como decidir entre as alternativas.

No pairwise, duas respostas geradas para a mesma entrada são colocadas lado a lado, e o evaluator decide qual delas vence segundo uma rubrica definida pela equipe. Retomando o exemplo recorrente, o mesmo caso de revisão de código seguirá adiante para comparar prompts concorrentes não por impressão geral, mas por julgamento estruturado entre saídas. Escrever o prompt do juiz é decisivo porque ele determina o que conta como vitória: mais precisão, melhor aderência ao código, menos alucinação ou outro critério operacional relevante.

## Transcrição

00:01

Bom, pessoal, seguinte, vamos juntar algumas pontas agora, tá? Se você percebeu, nós conseguimos fazer diversas avaliações utilizando os mesmos, como que eu posso dizer, o mesmo dataset. A gente conseguiu entender que essas métricas

00:23

elas conseguem, no final das contas, nos mostrar informações cuja elas vão ser úteis para a gente atender os nossos objetivos que a gente vai escolher na hora que a gente vai fazer a avaliação de um prompt. Então, por isso que essas métricas são tão importantes.

00:42

Por outro lado, o que acontece? Muitas dessas métricas, tá? Elas trabalham de uma forma um pouco mais exata. Muitas dessas métricas, de forma geral, nós estamos passando algumas instruções. Muitas delas a gente passou com ou sem referência. E muitos avaliadores que a gente utilizou do LangChain, alguns deles são mais diretos, né? Porque utilizaram uma fórmula customizada, como eu mostrei pra vocês.

01:09

Mas outros avaliadores que a gente utilizou, deu para perceber que ele executou uma I.A. por trás para rodar. E aí, nesse caso, houve sim avaliações subjetivas.

01:24

Se você olhar, correctness, relevance, faithfulness, conciseness, helpfulness, todos esses tipos de métricas foram subjetivas. E essa subjetividade aconteceu por quê? Porque, nesse caso, quem fez o julgamento foi um outro LLM. Então, a gente trabalhou aqui com métricas.

01:43

subjetivas, trabalhando com LLM as Judge, e, ao mesmo tempo, a gente trabalhou com algumas métricas objetivas e determinísticas, como a parte de validação de JSON, o Schema, a gente falou do Embedding Similarity, a gente falou do String Similarity também, tá? Então, a gente trabalhou com o ExecMatch também, eu acredito que sim,

02:06

E o único que a gente acabou não falando é o Precision, Recall e F1. Porque esses caras aqui, na realidade, são métricas conhecidas, importantes, padrão de mercado, mas nem todas as ferramentas implementam isso claramente, principalmente porque elas têm relações diretas umas com as outras.

02:33

Então, a gente vai ter um próximo capítulo, onde nós vamos falar especificamente sobre métricas de precisão. E essas métricas de precisão, você vai perceber que eu vou ter que mostrar, de forma geral, um pouquinho de teoria. A gente vai escrever uma função, a gente vai fazer algumas divisões, a gente vai pegar alguns resultados, a gente vai usar algumas fórmulas para criar esse sistema

03:01

para que a gente consiga ter essas informações, porque elas realmente são importantes, principalmente em conceitos de classificação. E a classificação é algo tão importante

03:14

que é aquilo que define se aquilo é um erro ou não é um erro. Esse pull request pode ser dado merge ou não. Ou seja, eu consigo classificar problemas que eu tenho e, baseado nessas informações, eu consigo garantir qual é o meu nível de precisão.

03:32

das informações que eu estou tomando, qual é o nível de precisão que o meu prompt está retornando baseado em tarefas que eu acabei passando para ele, ou até mesmo o meu agente, ou seja, o agente fez diversos processamentos ali, quanto que eu consigo garantir de precisão que ele teve? Quanto que foi o recall? Quanto que foi o F1? Então,

03:53

o nosso próximo passo, nosso próximo capítulo, é ir em cima desse aspecto, que é extremamente importante, na minha opinião, e também num outro aspecto, que é a parte de pairwise, que é exatamente quando a gente está

04:09

fazendo já comparações diretas de um mesmo dataset, com prompts diferentes, e fazer... bater os resultados de quem é o melhor ou não, baseado num juiz. E esse juiz, nós vamos escrever o prompt dele, inclusive. Beleza? Então, cenas para os nossos próximos capítulos. Vamos nessa!

## Resumo IA

**Abreviações**  
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)  
- **I.A.** — Inteligência Artificial  
- **JSON** — *JavaScript Object Notation*  
- **Schema** — Esquema/estrutura de validação de dados  
- **Embedding Similarity** — Similaridade por embeddings  
- **String Similarity** — Similaridade entre strings  
- **Exact Match** — Correspondência exata  
- **Precision** — Precisão  
- **Recall** — Revocação/sensibilidade  
- **F1** — Medida F1, combinação harmônica entre precision e recall  

**Resumo**  
A aula mostrou que avaliar prompts é uma atividade de engenharia e não apenas de “dar notas”, porque o mesmo dataset pode ser usado para diferentes leituras de qualidade desde que as métricas estejam alinhadas ao objetivo da avaliação. O instrutor destacou que o valor real de uma métrica está em produzir sinais úteis para decidir se um prompt, um agente ou uma solução atende ao comportamento esperado de forma reproduzível, em vez de depender de impressões subjetivas.

Foram retomados diferentes tipos de avaliadores usados no LangChain. De um lado, há métricas subjetivas, nas quais outro LLM atua como juiz, como correctness, relevance, faithfulness, conciseness e helpfulness. De outro, há avaliações mais objetivas e determinísticas, como validação de JSON, Schema validation, Embedding Similarity, String Similarity e Exact Match. A ideia central foi mostrar que um pipeline maduro combina evidências de naturezas diferentes, já que cada métrica captura uma dimensão distinta do comportamento do prompt.

Em seguida, a aula introduziu precision, recall e F1 como métricas de classificação. O instrutor explicou que elas são especialmente úteis quando a saída precisa ser enquadrada em classes observáveis, como decidir se um resultado é erro ou não, ou se um pull request deve receber merge. Nesse caso, não basta um avaliador genérico: é necessário definir a lógica de classificação, contar acertos, falsos positivos e falsos negativos, aplicar as fórmulas correspondentes e transformar isso em uma medida operacional de desempenho.

Também foi ressaltado que essas métricas normalmente exigem implementação própria ou instrumentação explícita do experimento, porque dependem da forma como a tarefa foi modelada. O fluxo mencionado inclui escrever funções, separar resultados por categoria, calcular proporções e consolidar os valores em precision, recall e F1. O objetivo é medir de modo objetivo a confiabilidade do comportamento do sistema, inclusive quando se trata de um agente com múltiplos passos intermediários.

Por fim, a aula apresentou o conceito de pairwise comparison. Nesse formato, duas versões de prompt são comparadas diretamente sobre o mesmo dataset, e um juiz decide qual resposta é melhor conforme uma rubrica definida pela equipe. O ponto importante é que o próprio critério de comparação também precisa virar prompt, pois o juiz deve receber instruções claras sobre o que conta como vitória, como maior precisão, melhor aderência ao código, menos alucinação ou outro critério operacional relevante.

**Pontos de atenção**  
- Avaliar prompts não é acumular scores; o importante é extrair sinais alinhados ao objetivo da tarefa.  
- O mesmo dataset pode sustentar leituras diferentes de qualidade, desde que a métrica esteja bem definida.  
- Métricas subjetivas dependem de LLM as Judge e, portanto, refletem julgamento modelado por instruções.  
- Métricas objetivas e determinísticas, como validação de schema, string similarity e exact match, devem ser usadas quando a saída permite verificação mais rígida.  
- Combinar métricas subjetivas e objetivas costuma produzir uma avaliação mais confiável e completa.  
- Precision, recall e F1 não são métricas “automáticas” em muitas ferramentas; frequentemente exigem implementação ou instrumentação adicional.  
- Essas métricas só fazem sentido quando a tarefa é formalizada como classificação clara entre classes, estados ou decisões observáveis.  
- É preciso definir corretamente o que conta como acerto, falso positivo e falso negativo antes de calcular precision, recall e F1.  
- Em cenários com agentes e múltiplos passos, a métrica deve capturar o resultado final e não apenas a saída textual isolada.  
- No pairwise, o resultado depende fortemente do prompt do juiz; instruções vagas podem enviesar a comparação.  
- Comparações diretas entre prompts devem usar o mesmo dataset e critérios explícitos para evitar julgamentos subjetivos soltos.  
- A rubrica de vitória no pairwise precisa ser operacional, por exemplo priorizando precisão, aderência ao contexto ou redução de alucinação.