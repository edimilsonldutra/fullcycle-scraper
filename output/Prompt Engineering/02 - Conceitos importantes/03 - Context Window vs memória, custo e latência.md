Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16598)

## Resumo da aula

A janela de contexto já foi definida anteriormente; o ponto novo aqui é o custo interno de usar esse espaço. Durante a geração, o modelo não olha apenas para o último token isoladamente: ele reconsidera a sequência disponível para prever o próximo token. Retomando a frase "Go é...", ao gerar "rápida" e depois "eficiente", o modelo passa a trabalhar com um contexto que cresce a cada iteração. Isso faz cada novo token depender de um processamento sobre o histórico acumulado, e não apenas sobre a última palavra gerada.

Esse comportamento leva a um custo computacional que pode crescer na ordem de O(n²) em relação ao tamanho do contexto considerado. A intuição é simples: quanto mais tokens existem, mais relações entre eles o modelo precisa avaliar, e esse trabalho se repete ao longo da geração. Por isso, aumentar contexto não afeta apenas o limite máximo suportado; afeta também o volume de computação necessário para produzir cada resposta. Janela grande amplia capacidade, mas também amplia o custo operacional de usá-la.

Mais contexto implica mais memória consumida durante o processamento, porque o modelo precisa manter e manipular mais informação ao longo da inferência. Esse aumento de memória se converte em custo de infraestrutura e, em serviços pagos por uso, também pressiona o custo por chamada. Ao mesmo tempo, o processamento de mais tokens aumenta o tempo até a resposta, elevando a latência do sistema. Retomando o cenário da aplicação, adicionar contexto sem critério faz o sistema gastar mais, demorar mais e escalar pior.

Caching já foi apresentado antes; aqui importa entender seu limite dentro do próprio processamento do modelo. Quando uma sequência de tokens já foi processada e pode ser reaproveitada, parte do trabalho é evitada, reduzindo reprocessamento desnecessário. Isso não resolve o problema por completo, porque muitas sequências novas ou ligeiramente diferentes geram cache miss e exigem computação adicional. Em aplicações reais, pequenas variações no prompt, no histórico ou na geração já bastam para diminuir bastante o reaproveitamento.

A consequência prática é que token não é apenas espaço ocupado na janela: ele também representa trabalho computacional recorrente durante a geração. Por isso, o objetivo de Prompt Engineering não é simplesmente colocar o máximo de contexto possível, mas obter a melhor resposta com a menor quantidade de tokens necessária. Essa lógica explica por que técnicas como truncamento, sumarização, caching e batch prompting existem: elas atacam diretamente memória, custo e latência. Eficiência de prompt é, portanto, uma decisão de engenharia, não apenas de redação.

Retomando a escolha de modelo já discutida antes, o critério não é usar sempre o modelo com maior capacidade, mas o mais adequado ao problema. Se a tarefa é simples, usar um modelo maior ou com contexto excessivo pode introduzir custo e latência desnecessários sem ganho proporcional de qualidade. A decisão correta equilibra complexidade da tarefa, volume de contexto exigido e restrições operacionais do sistema. Em engenharia de software, isso significa evitar superdimensionamento do modelo da mesma forma que se evita superdimensionar infraestrutura.

## Transcrição

00:00

Bom, pessoal, no vídeo anterior eu revisitei rapidamente aqui com você o conceito de janela de contexto e limite de tokens que você tem aqui nos seus modelos. E eu também falei que não é porque eu tenho bastante janela de contexto que significa que o meu modelo é maior ou menor. O importante que a gente tem que entender é como que o modelo, no final das contas, acaba trabalhando por baixo dos panos aqui. Então, uma coisa que eu queria trazer e deixar sempre bem claro aqui para vocês

00:30

É o seguinte, deixa eu aumentar o zoom para ficar mais claro. Toda vez que você está pensando em janela de contexto, vamos imaginar aqui esse gráfico, esse eixo Y, imagina que eu tenho a minha janela de contexto, mas esse meu gráfico X pode ter diversas variáveis ou opções que você pode colocá-lo nesse momento, que é memória, custo e tempo de processamento.

00:58

Por que eu estou dizendo isso? Todas as vezes que eu for enchendo a minha janela de contexto, mesmo que eu não exceda, você vai perceber naturalmente que o modelo vai precisar usar mais memória.

01:15

Segundo ponto, se ele usa mais memória, eu tenho mais custo, porque eu vou precisar de mais placas, mais memória, o que tem isso custo. E, obviamente, que quanto maior, mais contexto eu utilizar, maior vai ter o tempo para eu processar toda essa informação.

01:36

Uma coisa que é importante que vocês consigam entender claramente é que, internamente, o modelo avalia a relação de todos os tokens para a gente. Então, o custo computacional chega a bater O de n². Isso vai sendo exponencial. Por que acontece? Toda vez que eu coloco assim, o gol é

02:02

Imagina que eu tenho essa frase que eu acabo colocando aqui para o meu modelo, certo? Então, eu coloco assim, ó, a linguagem Go é... Vou colocar aqui.

02:12

O que o modelo, no final das contas, vai fazer? Ele vai pegar todos esses tokens e, baseado com todos esses tokens juntos, ele vai tentar prever qual é o próximo. E daí, quando ele vai tentar prever qual é o próximo, o que acontece? Ele vai prever que, por exemplo, o Goal É pode ser rápido. Ele pode trazer. Beleza. Aí, o que pode acontecer no próximo caso? Ele vai pegar todos esses tokens de novo e pode colocar

02:42

Eficiente. Estou dando um exemplo. Então, o que acontece? Ele começa com esses três tokens. Obviamente, um token não é uma palavra, necessariamente, mas vamos fingir, nesse caso, que é uma palavra por completo. Quando eu coloco o goal é, ele vai tentar trazer o próximo token para rápido, por exemplo. E, quando ele for para a próxima iteração, ele vai pegar agora o goal é rápido e

03:10

ele previu o próximo token, que é o E. Depois disso, o que ele pode fazer? Ele pode chegar e ele vai pegar todos esses tokens novamente, reprocessar para pegar o eficiente. Então, você consegue entender que para cada token que você acaba trabalhando, ele reprocessa tudo novamente. E isso gera um custo enorme, memória enorme. Obviamente, né, pessoal, que...

03:38

só para dizer e tentar deixar claro também, não é porque a gente está trabalhando dessa forma que o modelo vai fazer isso o tempo todo. Por quê? Porque ele trabalha com o cache também. Então, toda vez que ele vê o Go é rápido e eficiente, isso aí provavelmente vai entrar num cache. Quando ele vê esse conjunto de tokens juntos, ele não precisa reprocessar tudo novamente. Mas, novamente, galera,

04:06

muita coisa bate em cache miss, ou seja, tem muita coisa, muita informação da forma como ela é gerada, da forma como os tokens são gerados e tudo mais, não vai ser cacheado. Então, a gente tem que lembrar que cada token acaba contando. E, obviamente, que se você sabe disso, que gasta mais memória, que tem mais custo e mais tempo de processamento,

04:31

No final das contas, isso vai afetar quem? Você. O seu sistema. Vai afetar diretamente você. Então, a grande regra, de forma geral, que você tem que pensar na parte de Prompt Engineering é como que eu consigo ter a melhor resposta com a menor quantidade de tokens a ser utilizada, tá? E isso não é simples, tá? Tanto que a gente vai ver que nós temos diversas formas, inclusive, de testar

04:58

inclusive qual é o melhor prompt com o menor tamanho para ter o resultado que a gente trabalha. E a gente vai poder fazer isso e a gente vai ver, inclusive, pontos bem parecidos aqui ainda nessa disciplina. Então, é importante que você entenda que toda vez que eu estou falando em janela de contexto, tokens, eu estou falando em custo, tempo e processamento. Se você quer trabalhar bem com prompt engineer e não tiver isso em mente o tempo todo, às vezes você vai...

05:28

fazer com que a empresa ou o software que você trabalhe vai ter um custo muito mais elevado, vai ter uma latência muito maior para responder e, por isso, é importante a gente relembrar esses aspectos. E, novamente, utilize o modelo certo para a tarefa certa. Cada modelo tem uma especialidade e cada modelo, às vezes, para resolver um problema simples, você não precisa de uma bazuca para matar uma formiga.

05:57

Então, é esse aspecto que a gente tem que levar em conta. Fechou? Mas, temos mais coisas por aí que a gente tem aí que rever. Então, vamos nessa!

## Resumo IA

**Abreviações**
- **O(n²)**: notação de complexidade assintótica quadrática, indicando que o custo cresce proporcionalmente ao quadrado do tamanho de entrada.
- **Prompt Engineering**: engenharia de prompts; prática de estruturar entradas para obter melhores respostas de modelos de IA.
- **cache miss**: falha de cache; situação em que um dado não está disponível no cache e precisa ser recalculado ou recuperado.
- **IA**: Inteligência Artificial.
- **X** e **Y**: eixos de um gráfico usados na aula como representação visual para relacionar janela de contexto com variáveis como memória, custo e tempo.

**Resumo**
A aula explicou que, embora a janela de contexto já tenha sido apresentada anteriormente, o ponto central aqui é o custo interno de trabalhar com esse espaço durante a geração de tokens. O instrutor mostrou que o modelo não prevê cada token isoladamente: a cada iteração, ele reprocessa o histórico acumulado para inferir o próximo token, o que faz o custo computacional crescer de forma significativa, chegando à ordem de O(n²) conforme aumenta o contexto.

Foi destacado que ampliar a janela de contexto não afeta apenas o limite máximo de tokens, mas também aumenta o consumo de memória, o custo de infraestrutura e a latência de resposta. Para ilustrar, o instrutor usou uma frase simples como “Go é...” e mostrou como, a cada novo token gerado, o modelo reconsidera toda a sequência anterior. Em seguida, explicou que o caching reduz parte desse retrabalho ao reaproveitar sequências já processadas, mas que na prática muitas variações de prompt e geração levam a cache miss, diminuindo bastante o reaproveitamento.

A partir disso, a aula concluiu que token não é apenas “espaço” na janela, mas também trabalho recorrente de processamento. Por essa razão, Prompt Engineering deve buscar a melhor resposta com a menor quantidade de tokens possível, equilibrando qualidade, custo e desempenho. O instrutor relacionou isso a técnicas como truncamento, sumarização, caching e batch prompting, e reforçou que a escolha do modelo também deve considerar a adequação à tarefa, evitando usar modelos maiores do que o necessário quando o problema é simples.

**Pontos de atenção**
- Aumentar a janela de contexto não impacta só o limite de tokens; impacta também memória, custo e latência.
- O processamento interno do modelo pode crescer de forma quadrática com o tamanho do contexto, elevando bastante o custo computacional.
- Cada novo token pode levar ao reprocessamento do histórico, o que gera overhead significativo.
- Cache ajuda, mas não elimina o problema; muitas mudanças pequenas no prompt ou na geração causam **cache miss**.
- Em Prompt Engineering, o objetivo não é inserir o máximo de contexto, e sim obter o melhor resultado com o menor número de tokens possível.
- Técnicas como truncamento, sumarização, caching e batch prompting existem para reduzir custo, memória e tempo de resposta.
- Usar um modelo maior ou com contexto excessivo para tarefas simples pode gerar desperdício de recursos sem ganho proporcional de qualidade.
- A escolha do modelo deve equilibrar complexidade da tarefa, volume de contexto e restrições operacionais.
- Superdimensionar o modelo é um erro de engenharia semelhante a superdimensionar infraestrutura.
- Ignorar custo e latência na construção dos prompts pode aumentar gastos do sistema e piorar a experiência do usuário.