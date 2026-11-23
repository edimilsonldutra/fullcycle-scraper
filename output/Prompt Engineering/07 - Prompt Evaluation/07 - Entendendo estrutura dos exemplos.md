Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16862)

## Resumo da aula

Um laboratório de prompt evaluation precisa separar claramente prompts, dataset e scripts operacionais. A pasta prompts concentra as variações de instrução que serão testadas, enquanto o arquivo dataset.jsonl guarda os casos de entrada usados de forma repetível. Essa organização evita misturar lógica de experimento com dados e facilita comparar versões sem perder rastreabilidade. No cenário de revisão de código, a tarefa permanece a mesma e o que varia entre os exemplos é o código analisado.

JSONL é um formato em que cada linha do arquivo contém um JSON completo e independente. Ele é útil para datasets de avaliação porque simplifica leitura incremental, versionamento e processamento por scripts, sem exigir carregar uma grande estrutura única na memória. Em vez de um array JSON monolítico, o arquivo vira uma sequência de registros autônomos, o que combina bem com pipelines de upload, inspeção e execução em lote. Quando o dataset cresce, esse formato também reduz atrito operacional para adicionar, remover ou revisar exemplos individualmente.

O script de reset existe para limpar o estado anterior do experimento na ferramenta de avaliação antes de reenviar os casos. Isso evita duplicidade, inconsistência entre versões do dataset e resultados contaminados por execuções antigas. Já o uploadDataset publica o conteúdo local para o LangSmith, transformando o arquivo fonte em um dataset utilizável pelos testes. Juntos, esses scripts criam um ciclo operacional simples: limpar, subir e então executar as avaliações sobre uma base controlada.

Retomando o uso de LangSmith já conhecido, o upload serve para registrar os exemplos em um ambiente onde os prompts poderão ser executados e comparados de forma organizada. O ponto importante aqui não é a ferramenta em si, mas o fato de o dataset local virar uma referência compartilhada para os experimentos seguintes. Como a conta e os limites de uso influenciam o volume de exemplos, um conjunto menor pode ser suficiente para preparar o fluxo inicial sem perder a utilidade pedagógica. No exemplo, 18 entradas bastam para estruturar o laboratório antes de escalar a avaliação.

Os exemplos foram organizados em três camadas de complexidade crescente. A primeira categoria cobre casos mais básicos e tende a enfatizar aspectos mais objetivos, servindo como porta de entrada para entender a mecânica da avaliação. Depois entram métricas de classificação, que exigem cálculo e agregação de resultados no dataset inteiro. Por fim, a comparação pairwise passa a responder qual prompt vence contra outro segundo um critério já definido.

Precision, recall e F1 aparecem na etapa seguinte porque exigem uma estrutura de avaliação mais disciplinada do que testes básicos. Essas métricas dependem de contabilizar acertos, falsos positivos e falsos negativos ao longo de vários exemplos, o que torna o dataset e sua organização ainda mais importantes. O ganho é sair de observações caso a caso para uma leitura agregada do comportamento do prompt. Quando o objetivo envolve classificação ou detecção, essas métricas mostram desequilíbrios que uma impressão qualitativa isolada não revela.

Os exemplos numerados funcionam como uma trilha de experimentação. Cada arquivo representa um recorte específico do que será analisado e da forma como essa análise evolui ao longo do projeto. A leitura correta não é tratar cada exemplo como algo isolado, mas como parte de uma progressão: primeiro entender a base operacional, depois medir com fórmulas e, por último, comparar alternativas de prompt diretamente. Esse encadeamento reduz confusão e deixa claro onde cada peça entra no processo de avaliação.

## Transcrição

00:01

Bom, pessoal, no vídeo anterior eu falei com vocês sobre dataset, tá? Então, o que nós temos aqui, tá? Eu tenho três categorias de exemplo aqui pra gente, tá? Nesse momento a gente vai focar nessa categoria número 1, que é básica, tá? Mas é básico, você vai entender o porquê. É básico, mas não é tão básico assim.

00:21

E esse ponto básico aqui vai focar em muitas métricas, em muitos exemplos que estão naqueles aspectos que normalmente são mais objetivos, muitas vezes. Então, vamos nessa. Deixa eu abrir aqui para você, para você entender como é que funciona isso aqui. Então, seguinte.

00:44

Se você olhar aqui, o que eu tenho dentro dessas minhas pastas dos meus arquivos? Eu tenho uma pasta prompts, onde eu tenho alguns prompts que eu vou utilizar. Eu tenho 10 exemplos aqui.

00:58

Eu tenho o meu dataset.json aqui, e se você não sabe o que é JSON-EL no final, é um JSON in-line, tá? Ou seja, cada linha é um JSON completo, tá? Normalmente usa bastante isso para economizar espaço e tudo mais, então se você não conhece, é isso aqui. E se você perceber aqui, ó... Aqui está, basicamente, o meu dataset. São 18 entradas que eu criei aqui, eu não ia criar 100 e etc., senão eu ia até estourar a minha conta do LangSmith também.

01:25

Beleza? Então, se você olhar aqui, a minha tarefa é sempre a mesma, mas aqui eu tenho os códigos que são diferentes ali. Beleza? O que eu tenho aqui de importante também é o seguinte, eu tenho um script que eu chamo de reset, ou seja, eu apago meu dataset inteiro da ferramenta,

01:44

eu tenho um script chamado de UploadDataset, que eu faço o upload desse dataset, nesse caso no Langsmith, e aí cada um desses exemplos, de 1 a 10 aqui para mim, são exemplos que a gente vai entender o que ele está analisando e como isso está sendo analisado ao longo do tempo. Maravilha? Então,

02:07

Aqui está a estrutura básica de como a gente vai trabalhar nessa nossa primeira etapa com esses exemplos. Depois disso, a gente vai para um ponto um pouquinho mais complexo, que é a parte de precision. Ele é mais complexo, realmente. Vai trabalhar com recall, vai trabalhar com precision, vai trabalhar com F1 e etc. Não é tão complexo, mas a gente vai ter que desenvolver fórmula. E depois, por último, pairwise para a gente fazer comparações de prompt.

02:32

Beleza? Então, no próximo vídeo, vamos começar com o nosso exemplo número 1. Vamos nessa!

## Resumo IA

**Abreviações**  
- **JSONL**: *JSON Lines* — formato em que cada linha do arquivo contém um objeto JSON completo e independente.  
- **JSON**: *JavaScript Object Notation* — formato de representação de dados estruturados.  
- **LangSmith**: plataforma/ferramenta para organização e avaliação de prompts e datasets em experimentos de LLMs.  
- **precision**: precisão — métrica que mede a proporção de acertos entre os casos classificados como positivos.  
- **recall**: revocação/sensibilidade — métrica que mede a proporção de positivos corretos encontrados dentre todos os positivos reais.  
- **F1**: *F1-score* — métrica que combina precision e recall em uma única medida.  
- **pairwise**: comparação par a par — abordagem em que dois prompts são comparados diretamente para determinar qual desempenho é बेहतर.  

**Resumo**  
A aula apresenta a estrutura inicial de um laboratório de *prompt evaluation*, destacando que o experimento deve separar claramente os prompts, o dataset e os scripts operacionais. O instrutor mostra uma organização em pastas, com uma pasta de *prompts* contendo as variações de instrução que serão testadas e um arquivo `dataset.jsonl` com os casos de entrada usados de forma repetível. Ele explica que essa separação evita misturar a lógica do experimento com os dados, além de facilitar comparação entre versões e manter rastreabilidade. No cenário de revisão de código, a tarefa permanece constante e o que muda entre os exemplos é o código analisado.

O formato `JSONL` é explicado como uma sequência de registros independentes, um por linha, o que facilita leitura incremental, versionamento e processamento por scripts. Em vez de um único JSON grande, o dataset fica organizado como vários exemplos autônomos, o que reduz atrito na manutenção e no uso em lote. O instrutor comenta também sobre o volume de exemplos, dizendo que 18 entradas foram suficientes para iniciar o laboratório sem exagerar no consumo de recursos da conta no LangSmith.

Na parte operacional, a aula descreve o uso de um script de *reset* para limpar o dataset anterior na ferramenta de avaliação antes de reenviar os casos, evitando duplicidade e resultados contaminados por execuções antigas. Em seguida, o script `UploadDataset` publica o dataset local no LangSmith, transformando-o em uma base utilizável para testes e comparação de prompts. Assim, o fluxo básico fica: limpar o estado anterior, subir o dataset e executar as avaliações sobre uma base controlada.

Por fim, o instrutor organiza os exemplos em três etapas de complexidade crescente. A primeira é a categoria básica, focada em casos mais objetivos e introdutórios. A segunda entra em métricas como precision, recall e F1, exigindo agregação de resultados e maior disciplina na avaliação. A terceira utiliza comparação *pairwise*, em que um prompt é confrontado com outro para definir qual vence segundo um critério pré-estabelecido. A ideia geral é conduzir o aluno por uma trilha progressiva: entender a base operacional, depois medir desempenho com métricas e, por último, comparar alternativas de prompt diretamente.

**Pontos de atenção**  
- Separar bem **prompts**, **dataset** e **scripts operacionais** para não misturar experimento com dados.  
- Usar **JSONL** para datasets de avaliação, pois cada linha é um registro independente e mais fácil de manter.  
- Evitar datasets excessivamente grandes no início, especialmente quando houver limite de uso da ferramenta.  
- Executar o **reset** antes de novo upload para impedir duplicidade e contaminação por execuções antigas.  
- Fazer o **uploadDataset** como passo obrigatório para tornar o dataset local utilizável no ambiente de avaliação.  
- Entender que a tarefa de avaliação pode ser a mesma; o que varia entre os exemplos é o **código analisado**.  
- Não tratar os exemplos como casos isolados: eles compõem uma progressão de aprendizagem e avaliação.  
- Em métricas como **precision**, **recall** e **F1**, a organização do dataset é crítica, pois os resultados dependem de agregação correta.  
- A comparação **pairwise** só faz sentido quando o critério de vitória entre prompts está bem definido.  
- Começar pela etapa básica ajuda a reduzir confusão antes de avançar para métricas e comparações mais complexas.