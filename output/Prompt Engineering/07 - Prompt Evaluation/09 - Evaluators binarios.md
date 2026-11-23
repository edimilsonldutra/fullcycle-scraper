Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16864)

## Resumo da aula

Avaliação binária explícita transforma um critério subjetivo em uma decisão de aprovação ou reprovação: yes/no, pass/fail, 1/0. Esse formato é útil quando a decisão de engenharia não precisa de gradação intermediária e o objetivo é saber se a saída atende ou não a um requisito. Em vez de interpretar um score contínuo, o experimento passa a contar quantos casos passaram em cada critério. Isso simplifica leitura de resultado e facilita comparar versões de prompt por taxa de aprovação.

Retomando o experimento de revisão de código, a nova camada está em como os dados são entregues ao evaluator. Uma função como prepareDataNoRef envia apenas o necessário para o julgamento sem ground truth, enquanto prepareDataWithRef inclui também a referência do exemplo, como exampleOutputs. A escolha altera a base do julgamento: sem referência, o evaluator decide apenas pela resposta gerada e pelo critério; com referência, ele pode confrontar a saída com um alvo conhecido. Isso não garante resultado melhor automaticamente, mas muda o tipo de evidência disponível para a decisão.

Os criteria evaluators built-in do LangSmith evitam implementar manualmente a lógica de julgamento para critérios já suportados pela ferramenta. No cenário mostrado, conciseness e helpfulness são usados diretamente como evaluators prontos, o que reduz código operacional e acelera o experimento. A vantagem prática é padronizar critérios recorrentes sem escrever prompts de julgamento do zero. O cuidado necessário é lembrar que o evaluator continua sendo uma camada de julgamento e deve ser interpretado à luz do critério escolhido.

Labeled Criteria é a variação em que o critério é avaliado com apoio explícito de uma referência. Em vez de julgar apenas se a resposta parece adequada, o evaluator recebe também o valor esperado e usa esse contexto para decidir yes ou no. Isso é especialmente útil quando o critério depende de aderência ao conteúdo correto, como no caso de correctness. O rótulo existe porque o julgamento passa a ser ancorado em um alvo fornecido pelo dataset.

Cada critério entra no experimento como um evaluator independente dentro da lista passada para a execução. Na prática, isso permite avaliar a mesma saída sob múltiplas perspectivas no mesmo run: por exemplo, concisão sem referência, utilidade sem referência e correção com referência. O resultado não é um único veredito global, mas um conjunto de decisões binárias por critério. Essa separação melhora o diagnóstico porque mostra exatamente em qual dimensão o prompt falhou.

A leitura do experimento muda quando o score é binário: o painel passa a mostrar contagens de yes e no por evaluator, em vez de médias ou faixas numéricas. Se conciseness retorna 18 yes, o prompt passou em todos os exemplos para esse critério; se correctness retorna 14 yes e 3 no, existe falha localizada que precisa ser inspecionada. Esse formato é direto para decisões rápidas, porque a pergunta deixa de ser “quão bom foi?” e vira “passou ou não passou?”. Em datasets pequenos, essa visualização já permite identificar rapidamente se o problema está concentrado em um critério específico.

LangSmith tracing permite abrir cada execução e inspecionar o caminho completo do julgamento. Ao clicar em um item, é possível ver o exemplo recebido, o output gerado, o reasoning do evaluator, o score binário e o critério usado para justificar a decisão. Isso transforma o evaluator em algo auditável, não em uma caixa-preta que apenas devolve yes ou no. Quando um caso falha em correctness, o tracing mostra por que falhou e orienta a próxima iteração do prompt.

O valor operacional do evaluator binário aparece quando um caso não passa e a equipe precisa agir. Em vez de apenas registrar a falha, o fluxo correto é abrir o tracing, verificar metadados, entender o reasoning e decidir se o problema está no prompt, no critério ou na própria referência. Depois disso, o experimento pode ser executado novamente com o mesmo dataset para validar a correção. O ciclo fica objetivo: falhou, inspecionou, ajustou, reexecutou.

Quando o evaluator é binário, o resultado agregado aparece como contador de aprovações e reprovações, não como range contínuo. Isso é adequado para critérios em que a equipe quer uma fronteira clara de aceitação, sem discutir se 0.7 já seria suficiente. A principal consequência é a perda de nuance intermediária em troca de clareza decisória. Para etapas iniciais de validação prática, essa troca costuma ser vantajosa.

## Transcrição

00:01

Bom pessoal, agora que eu acho que ficou um pouco mais claro de como a gente consegue fazer essas execuções, a gente vai entrando item a item naquelas métricas que eu falei para vocês. Então, eu realmente resolvi fazer coisas bem mais detalhadas para que a gente consiga entender as diferenças.

00:20

Então é o seguinte, exemplo número dois é critério binário para evaluation. O que significa? Muitas vezes a gente pode escolher para avaliar algo como zero ou um. Deu certo ou não deu certo, ok? Ou seja, não tem caminho do meio.

00:40

Entende? Muitas vezes eu tenho algo que a minha precisão é de 0.8, mas muitas vezes eu quero fazer essa minha avaliação de 0 e 1 e ponto. E existem alguns caras que conseguem fazer esse tipo de coisa. Então, vamos tentar entender o que a gente vai fazer aqui. Nós temos esse prompt.

01:02

que é o meu Criteria Evolve. Então, basicamente, é um prompt bem simples e bobo, você é um revisor de código especializado, analisa o trecho do código, responde apenas no formato e ponto. Basicamente, igual o outro, eu preferi sempre separar por vários arquivos para cada arquivo ficar autocontido.

01:22

E aqui, o que vai acontecer? Carreguei meu prompt, botei a minha formatação, e agora, novamente, eu tenho duas coisas um pouco diferentes aqui. Eu tenho uma função aqui, se você olhar, que é prepareDataNoRef. O que isso significa? É preparar data sem nenhuma referência. Então, isso aí é um ponto importante. Ou seja, quem vai fazer a comparação não vai ter referência.

01:51

Ou seja, vai funcionar ou não vai, basicamente pelo modelo. Ou eu posso ter PrepareDataWithRef. Ou seja, se você olhar aqui, eu tenho o meu campo de referência, onde eu tenho ExampleOutputs. Você lembra que no meu dataset eu tenho o meu output, onde eu tenho diversos exemplos de como poderia ser o meu output? Então, eu tenho duas formas de executar aqui. Ou seja,

02:17

Com referência e sem referência, ou seja, com Ground Truth ou não. Então, olha aqui que interessante agora aqui, tá? Eu botei esses comentários pra ficar mais claro. Então, o nosso critério aqui é sempre 0 ou 1, tá? Ou seja, ou passou ou falhou, beleza? Normalmente, isso acaba sendo mais direto da forma como a gente quer trabalhar e tudo mais, tá?

02:38

O próximo exemplo que eu vou mostrar para vocês, ele já é mais diferente, porque a gente consegue não ser apenas 0 e 1. Então, por esse aqui que é o nosso caso de exemplo. Então, é o seguinte, somente para você entender.

02:52

No LangChain, quer dizer, no LangSmith, nós temos built-in critérios de avaliação, ou seja, onde eu não fico precisando criar fórmulas para fazer.

03:10

Na realidade, ele já traz isso meio que pronto pra mim. Então, nesse nosso caso aqui, uma das métricas que eu tenho, um dos critérios que eu tenho aqui, é conciseness. Ou seja, o quão conciso direto eu tenho ali na minha resposta. E se você olhar aqui, eu estou pedindo pra ele fazer essa avaliação sem referência.

03:33

Tá? Olha só que interessante. Aqui, eu tenho um outro cara, um critério, se ele é helpfulness, ou seja, se ele é útil. E aqui, se você olhar, eu estou trazendo aqui sem referência.

03:46

E eu tenho um outro cara aqui, tá? E ele é chamado de Labeled Criteria, tá? Porque quando a gente trabalha dessa forma, eu tenho uma referência aqui nesse meu caso. E a minha referência tá aqui. Então, por isso que ele cria um rótulo aqui pra mim. Então, aqui eu estou passando dados como referência.

04:07

Beleza? Não significa que é porque eu passei referência ou não, o negócio vai ser melhor ou pior. Normalmente, quando eu passo mais referência, eu estou, obviamente, induzindo a inteligência artificial a ter base para conseguir tomar decisão, mas, no final das contas, vai ser executado e aí a gente vai ver como é que funcionou. Agora, perceba que cada cara desse aqui é um

04:34

No final do dia, um evaluator, tá? Então, esse aí é um ponto importante. Perceba que esses caras aqui, ó, eles estão dentro dessa minha listinha. Cada um desses caras é um cara que tá fazendo uma avaliação, tá? E esses evaluators, ou ele tem ou não tem referência aqui pra mim. Então, no final do dia, o que que eu tenho aqui?

04:55

Estou mandando o prompt, estou passando o dataset, estou falando quem vai fazer o meu evaluator, criei um prefixo para a gente saber e não misturar com o anterior, e agora eu vou executar esse cara. Então, vou dar aqui o python, vou colocar 1, 2 aqui. E vou botar esse cara para ser executado agora aqui para a gente.

05:19

e ele vai passar esses caras para os 18 itens, para o meu dataset com as 18 opções que eles acabam tendo. E se a gente for aqui no Langsmith,

05:37

Provavelmente, a gente já vai ver daqui a pouquinho, já pingando aqui pra gente, um outro experimento que é o que começa com um Binary Criteria, provavelmente. Aqui é o Format Evolve aqui ainda, né? Então, daqui a pouquinho, provavelmente, ele já vai começar a aparecer ali pra gente, né? O ponto é que ele tem três evaluators para 18 itens que ele vai ter que resolver aqui pra gente, tá? Deixa eu dar um atualizar, ver quem sabe se ele já tá aparecendo ou não aqui pra mim.

06:07

Ainda não. Então vamos aguardar um pouquinho para ele aparecer.

06:13

Bom, pessoal, eu dei uma pausa rápida no meu vídeo, somente para a gente não ficar esperando o tempo todo, mas se você olhar aqui meu código, ele rodou todos os 18, tá? E agora, se você olhar, apareceu um novo experimento aqui para mim, tá? Criteria binary. E se você olhar aqui, olha só o que apareceu agora. Consistency e tem um yes, um y de yes, 18 aqui para mim.

06:39

O que isso significa? Significa que binário, yes, deu tudo certo. Helpfulness, ou seja, ele achou ok. Foi helpfulness. Mas, se você olhar aqui, o correctness aqui deu 14 corretos e 13 incorretos aqui pra mim. Então, é interessante porque eu posso chegar aqui no meu langsmith agora e olhar item a item

07:09

e entender o porquê que esse cara do correctness não passou e esses outros caras aqui também não passaram. Então, quando eu caio aqui, eu posso clicar e eu consigo ver o runner que executou a minha evaluation.

07:28

E aqui eu consigo ver tudo, olha só que interessante! Ele recebeu o exemplo, ele fez a execução, aqui está o output, o reasoning que teve para fazer isso, o valor não, o score sim, e aqui foi o critério que ele utilizou

07:46

para dizer que não estava correto. Então, é basicamente isso. E é basicamente isso, galera. Ou seja, eu posso querer dar feedback, eu posso trabalhar, ele tem os metadados que ele utilizou e tudo mais, mas o fato é que agora... Ah, não passou? Deixa eu entender. Deixa eu olhar aqui, deixa eu olhar e etc. Ah, depois eu vou rodar de novo. Está correto? Não está? Mas o importante é saber que a gente tem o tracing disso e a gente consegue trabalhar e entender.

08:13

Legal? Mas, olha só, a gente falou agora de critérios, de forma geral, que são binários. Perceba que foi sim ou não. Eu tive 18 yes, 14 yes aqui e 3 não. E o outro teve um therefore aqui ainda.

08:29

que é uma outra opção que provavelmente alguma observação que ele acabou até colocando aqui, se eu for olhar no camarada, tá? Então, de forma geral, essa aqui é a ideia em relação a quando a gente tem algo muito mais sim e não, ele mostra aqui pra gente como um contador e não fica dando range aí pra gente.

## Resumo IA

**Abreviações**
- **yes/no** — sim/não
- **pass/fail** — aprovado/reprovado
- **0/1** — zero/um
- **LLM** — *Large Language Model* (modelo de linguagem de grande porte)
- **LangSmith** — ferramenta de observabilidade, tracing e avaliação para aplicações com LLMs
- **LangChain** — framework para desenvolvimento de aplicações com LLMs
- **Ground Truth** — verdade de referência, resposta esperada/rotulada
- **output** — saída gerada
- **prompt** — instrução enviada ao modelo
- **dataset** — conjunto de dados
- **evaluator** — avaliador
- **criteria** — critérios

**Resumo**
A aula apresentou o uso de avaliação binária explícita em experimentos de revisão de código, mostrando como transformar critérios subjetivos em decisões objetivas de aprovação ou reprovação. Em vez de trabalhar com scores contínuos, o instrutor explicou que o resultado passa a ser contado como yes/no, o que simplifica a leitura dos experimentos e facilita comparar versões de prompt pela taxa de aprovação em cada critério.

O fluxo prático foi demonstrado com duas formas de preparação dos dados: `prepareDataNoRef`, que envia somente o necessário para o julgamento sem referência, e `prepareDataWithRef`, que inclui também a referência do exemplo, como `exampleOutputs`. Essa diferença altera a base do julgamento, pois o evaluator pode decidir apenas com a saída gerada e o critério, ou confrontar a resposta com um alvo conhecido quando há Ground Truth.

Na sequência, foram apresentados os evaluators built-in do LangSmith, que evitam a implementação manual da lógica de julgamento para critérios já suportados. O instrutor usou critérios como `conciseness` e `helpfulness` diretamente como avaliadores prontos, destacando que isso reduz código e padroniza avaliações recorrentes. Também explicou a variação chamada `Labeled Criteria`, em que o julgamento é ancorado em uma referência explícita, sendo especialmente útil para critérios como `correctness`.

Cada critério foi tratado como um evaluator independente dentro de uma lista passada para a execução, permitindo avaliar a mesma saída por múltiplas perspectivas no mesmo run. O resultado não foi um veredito global, mas um conjunto de decisões binárias por critério, o que ajuda a identificar com precisão em qual dimensão o prompt falhou. O experimento foi executado sobre 18 itens do dataset, e o painel do LangSmith passou a exibir contagens de yes e no por avaliador, em vez de médias ou faixas numéricas.

Por fim, o instrutor mostrou como o tracing do LangSmith permite abrir cada execução e inspecionar o caminho completo da avaliação: exemplo recebido, output gerado, reasoning do evaluator, score binário e critério utilizado. Isso torna o processo auditável e orienta a ação corretiva quando algo falha, permitindo revisar metadados, entender o motivo da reprovação e reexecutar o experimento após ajustes. A principal mensagem foi que, quando o objetivo é decisão clara de aceitação, a avaliação binária traz objetividade e rapidez, ainda que sacrifique nuances intermediárias.

**Pontos de atenção**
- Avaliação binária é útil quando não há interesse em gradação intermediária; se houver nuance importante, esse formato pode ocultar detalhes.
- `prepareDataNoRef` e `prepareDataWithRef` mudam a base da decisão; com referência, o evaluator tem mais contexto, mas isso não garante automaticamente melhor resultado.
- `Labeled Criteria` depende de referência fornecida pelo dataset; se a referência estiver errada ou inconsistente, a avaliação pode ser enviesada.
- Cada critério deve ser entendido como um evaluator independente; não existe um “resultado global” único que substitua a leitura por dimensão.
- Critérios como `conciseness`, `helpfulness` e `correctness` podem apontar problemas diferentes no mesmo output; é importante analisar cada um separadamente.
- O uso de evaluators built-in reduz trabalho, mas não elimina a necessidade de interpretar criticamente a avaliação feita pela ferramenta.
- Quando um caso falhar, a prática correta é abrir o tracing, verificar o reasoning, os metadados e o output antes de concluir que o prompt está errado.
- O painel em modo binário mostra contagens de yes/no, não médias; portanto, a leitura deve ser feita como taxa de aprovação por critério.
- Em datasets pequenos, a inspeção item a item é especialmente importante para localizar rapidamente a origem do problema.
- O ciclo recomendado é: falhou, inspecionou, ajustou e reexecutou, validando novamente no mesmo dataset.