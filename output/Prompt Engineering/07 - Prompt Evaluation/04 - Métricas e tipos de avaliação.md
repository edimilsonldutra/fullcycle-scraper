Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16859)

## Resumo da aula

Objetivos de avaliação dizem o que importa medir; métricas e tipos de avaliação definem como isso será observado. A mesma tarefa pode exigir mecanismos diferentes de medição, porque nem todo critério produz um resultado verificável por fórmula. Por isso, a avaliação de prompts se organiza em grupos distintos: métricas objetivas, subjetivas, sistêmicas e comparativas. Essa taxonomia evita misturar qualidade semântica, conformidade estrutural, desempenho operacional e comparação entre versões como se fossem a mesma coisa.

Métricas objetivas produzem um resultado calculável a partir de uma regra explícita, normalmente por fórmula, validação ou comparação exata. Elas são úteis quando existe um critério observável sem depender de interpretação humana, o que aumenta reprodutibilidade e reduz ambiguidade. Precision, Recall e F1 entram nesse grupo e serão aprofundadas depois; aqui, o ponto central é que elas ajudam a quantificar acertos, falsos positivos e falsos negativos. Retomando o cenário de classificação de bugs, dizer que “tudo tem bug” pode capturar muitos casos reais, mas ainda degradar a avaliação por marcar como erro itens que não eram erro.

Exact Match verifica se a saída gerada coincide exatamente com a referência esperada. Esse tipo de métrica é apropriado quando a resposta correta precisa ser idêntica ao gabarito, como em labels, valores fechados ou respostas canônicas. String distance relaxa essa rigidez e mede o quão próxima a string gerada está da referência, o que ajuda quando pequenas diferenças textuais não devem ser tratadas como erro absoluto. As duas métricas dependem de uma referência conhecida e, por isso, se apoiam diretamente em ground truth.

Embedding similarity mede proximidade semântica, não igualdade textual. A referência e a saída são convertidas em embeddings, e a comparação ocorre no espaço vetorial para estimar se os dois textos expressam sentidos próximos. Isso é útil quando duas respostas podem usar palavras diferentes e ainda assim transmitir a mesma ideia, algo que Exact Match não captura. O custo dessa flexibilidade é que a métrica deixa de validar forma literal e passa a depender da qualidade da representação semântica.

Quando a saída será consumida por código, a primeira pergunta não é se ela está elegante, mas se ela respeita o contrato esperado. Validação de JSON e schema validation verificam se o output está estruturado corretamente, com campos, tipos e formato compatíveis com a aplicação. Esse grupo é determinístico porque a resposta passa ou falha segundo regras explícitas de estrutura. Retomando os objetivos já vistos, isso operacionaliza format adherence sem depender de julgamento subjetivo.

Métricas subjetivas dependem de julgamento, porque o critério não se resolve apenas com fórmula ou comparação exata. Nesse grupo entram avaliações aplicadas por humanos ou por outra LLM atuando como juiz, prática conhecida como LLM as Judge. A lógica é delegar a um evaluator a tarefa de analisar aspectos como adequação, utilidade ou fidelidade da resposta segundo uma rubrica. Mesmo quando automatizadas com LLM, essas avaliações continuam sendo subjetivas porque o resultado nasce de interpretação guiada por critérios.

Termos como Criteria Evaluators, Custom Rubric e LLM Judge Rating Criteria costumam apontar para o mesmo padrão: uma avaliação baseada em critérios descritivos. Em vez de perguntar apenas “passou ou falhou?”, a rubrica define dimensões de julgamento e orienta como atribuir nota, preferência ou classificação. Isso permite avaliar correctness, relevance, faithfulness, conciseness, helpfulness, harmfulness, bias e toxicity com mais nuance do que uma regra binária. A consistência do processo depende da clareza dos critérios e da estabilidade do evaluator escolhido.

Métricas sistêmicas observam o comportamento operacional da execução, não o conteúdo semântico da resposta. Latência, custo em tokens, preço, throughput e pass rate mostram como o prompt afeta o sistema em termos de performance e viabilidade operacional. Esse grupo é essencial porque um prompt pode melhorar a resposta e, ao mesmo tempo, piorar custo ou capacidade sob carga. Retomando efficiency e custo, a diferença aqui é a camada de medição: agora esses objetivos ganham indicadores concretos de execução.

Avaliação comparativa responde qual saída vence quando duas alternativas são colocadas lado a lado. Em pairwise evaluation ou model comparison, compara-se a saída A com a saída B, geralmente produzidas por prompts diferentes, para decidir qual atende melhor ao critério definido. Esse formato é útil quando a pergunta prática não é “a saída está boa em absoluto?”, mas “qual versão é melhor para este conjunto de casos?”. A comparação continua dependente do critério de vitória, que já foi estabelecido anteriormente.

A/B testing é uma forma comparativa aplicada em produção, usando comportamento real do sistema como evidência. Embora também compare duas variantes, o diferencial está no ambiente: a decisão passa a considerar aceitação, performance observada e resposta do uso real, e não apenas julgamento offline sobre exemplos controlados. Por isso, todo A/B testing é comparativo e se aproxima de pairwise, mas nem toda comparação pairwise é A/B testing. A distinção importa porque produção introduz variáveis de uso, escala e impacto operacional que não aparecem em testes locais.

Ground truth é a referência considerada correta para comparar a saída do sistema. Ele funciona como fonte da verdade do experimento: se um dataset contém casos cujo resultado esperado já é conhecido, esse conjunto fornece a base para medir acerto, erro e proximidade. Sem ground truth, várias métricas objetivas perdem sustentação, porque deixam de ter um alvo confiável para comparação. Ao longo de toda a avaliação de prompts, esse conceito serve como âncora para interpretar resultados de forma técnica e reproduzível.

## Transcrição

00:01

Bom pessoal, da mesma forma que a gente tem objetivos, a gente tem que entender agora é, pra eu chegar num determinado objetivo, eu preciso ter dados, eu preciso ter métricas, tá? E quais são as métricas que eu tenho? Como que eu organizo essas métricas, né? Como que isso aí é categorizado? Então vamos lá, são bastante métricas, a maioria delas a gente vai ver isso na prática, tá?

00:22

Por enquanto, nesse momento, eu mais vou falar das métricas de forma geral, mas eu não vou me aprofundar necessariamente nelas, porque a gente vai ter exemplos ali que vão mostrar praticamente todas que a gente está vendo. Beleza?

00:37

Então, a gente tem que entender que nós temos métricas em categorias um pouco diferentes. Nós temos métricas que são objetivas ou mais determinísticas, ou seja, normalmente por uma fórmula matemática ou por algo muito mais claro, a gente consegue ter determinado resultado, ou seja, não é algo subjetivo. É algo que, se eu rodar uma fórmula, eu consigo ter o resultado. É basicamente isso que a gente acaba falando. E quais são essas métricas?

01:06

Precision, Recall, F1... Então, são métricas que normalmente acabam, no final das contas, fazendo com que a gente olhe para um determinado dado e veja o quanto a nossa IA está acertando ou não. Então, vamos imaginar que eu tenho 100 documentos, e desses 100 documentos, 40 desses documentos, 40% daqueles códigos têm bug.

01:31

E os outros 60 não. Então, vamos imaginar que na hora que eu rodo aquilo na minha AIA, a AIA fala, olha, você... Tudo tem bug. Ou seja, ela acertou aqueles 40, mas ela errou 60. Entendeu? Então, ela tem um recall diferente e a precisão dela está baixa. Agora, se a precisão é muito alta, então de...

01:52

de 100 erros que eu tenho, por exemplo, e eu acertei 90% daquilo, a minha precisão é alta. Mas, como a minha precisão é alta, muitas vezes eu posso ter escolhido também coisas que não eram erro como erro. Ou seja, no final das contas, é uma forma de a gente conseguir verificar falsos positivos, falsos negativos, e o F1, basicamente, é uma fórmula da divisão deles.

02:20

Eu não quero que você fique preso a isso, porque eu vou mostrar a gente implementando isso pra você, tá? Então, fica tranquilo em relação a isso, mas são métricas determinísticas importantes. ExecMatch, basicamente, se o resultado que eu esperava é exatamente o resultado que eu tenho.

02:37

String distance, tá? O quão próximo o texto que está gerado é baseado em relação à referência que eu estou trazendo para ele. Normalmente, mais fórmulas. Outro ponto, embedding similarity. Basicamente é semântica, né? Então, da mesma forma que a gente tem vetorização, a gente consegue fazer busca semântica,

02:56

com embed similarity, ele vai pegar a minha referência, a minha saída, transforma em embedding e vê o quão próximo isso faz sentido. Basicamente é isso. E a gente tem validação de JSON, a gente tem schema validation, ou seja, eu quero garantir que o meu output esteja realmente estruturado da forma como eu gostaria. Então, de forma geral, a gente tem essas métricas que são mais determinísticas.

03:24

Por outro lado, a gente tem também algumas métricas que são mais subjetivas. E, nesse caso, métricas subjetivas normalmente podem ser analisadas por alguém. E, nesse caso, você vai encontrar bastante daqui para frente o termo chamado LLM as Judge, ou seja, o LLM como juiz. Ou seja, você pede para uma outra IA avaliar o resultado de uma IA. Então, isso é muito comum.

03:53

ou eu posso também ter métricas subjetivas com o humano, né, com pessoas olhando e falando, olha, isso aqui não tá legal, isso aqui tá legal e etc. A gente vai fazendo anotações, vamos dizer isso, tá? Então, por exemplo, correctness, né, eu quero ver se a minha resposta tá correta de acordo com uma referência. Relevância, essa saída responde à pergunta de fato. Faithfulness, né, se ele não alucina. Consciousness, a gente já falou um pouco sobre disso, né. Helpfulness, é, harmful,

04:20

harmfulness, bias, toxicity. Então, eu consigo fazer essas verificações. Muitas dessas métricas, inclusive, que são um pouco mais subjetivas, hoje em dia a gente já consegue rodar com um grande nível de precisão com uma validação de LLM mesmo. Mas isso não impede de você querer colocar um ser humano também para fazer esses tipos de avaliação para, no final das contas, a gente dar as nossas notas e etc.

04:49

Uma das coisas que são importantes você entender aqui é que esses nomes que eu estou colocando aqui para vocês, eles podem mudar de acordo com a plataforma, com a ferramenta que você vai usar, de acordo com o artigo que você vai usar.

05:04

Mas, normalmente, essas métricas têm nomes que você pode encontrar. Eu coloquei nas observações somente para você garantir que a gente está falando da mesma coisa. Então, se você ouvir falar em Criterias Evaluators, Custom Rubric,

05:22

a LLM Judge Rating Criteria, por exemplo, você normalmente vai entender que são métricas mais subjetivas que são realizadas normalmente por um humano ou por um outro LLM, tá? Então, quando você ouvir falar em rubrica, quando você ouvir falar em critérios e coisas desse tipo, normalmente a gente está falando nesses tipos de métrica.

05:44

Existe também uma outra categoria diferente de objetivas e subjetivas, que são as categorias sistêmicas e comparativas. O que é sistêmico? Focou simplesmente na execução, ou seja, quanto tempo demorou a latência, quanto que gastou de token versus o preço, ou seja, quanto que eu gastei naquela execução.

06:04

como que foi o throughput, quantas requisições por segundo ele aguentou, quanto que foi o pass rate, ou seja, baseado em um determinado exemplo, quantos passaram, quantos não passaram. Então, eu posso ter essas métricas que são bem claras ali para mim e que eu não estou necessariamente ali focado necessariamente em detalhes do que é o correto ou não. Normalmente, eu estou querendo saber algo que é gerado como output para mim

06:30

para um sistema, para a minha ferramenta. São dados bem claros ali para a gente. E outra categoria que a gente tem aqui também são as formas de você avaliar de forma comparativa. Ou você vai ouvir falar em

06:46

Pairwise Evaluation, o Model Comparison, basicamente é quando eu comparo a saída A versus a saída B. Ou seja, eu tenho duas saídas feitas por Prompts diferentes. E aí eu quero avaliar como eu faço essa comparação.

07:03

Um outro caso que é muito comum é A-B testing, ou seja, a gente mede as taxas de aceitação em produção. Então, quando a gente faz um pairwise evaluation, a gente está comparando duas coisas também. Não deixa de ser um teste A-B, mas quando normalmente a gente fala em teste A-B,

07:21

No contexto dessas verificações, normalmente os testes AB são realizados em produção. Então, isso aí é importante saber, porque o AB não deixa de ser um pairwise, porque eu estou comparando também ali. Mas, o ponto principal é que, no final do dia, o teste AB realmente a gente tem a saída baseado no que

07:47

na performance que foi gerada ali em produção. Não necessariamente se o usuário falou, ah, eu gostei, né? Mas muitas vezes, em produção, a gente consegue entender o quanto aquilo funcionou ou não, tá? Outra coisa extremamente importante, tá? Pra você já se acostumar, tá? Toda vez que a gente for falar em evaluation, de forma geral, você vai ouvir falar no termo Ground Truth, tá? Ou seja,

08:15

qual é a minha referência e a minha fonte da verdade. Ou seja, são as respostas corretas que são conhecidas para eu fazer a comparação da saída. Então, por exemplo, se eu quero pegar um dataset com 10 testes que eu quero rodar, e eu sei o resultado daquele teste antecipadamente,

08:39

e eu sei que aquele resultado está correto, isso é meu Ground Truth. Ou seja, no final das contas, eu sei qual é a minha fonte da verdade. Então, em qualquer lugar, em qualquer artigo que você for, na hora que a gente for conversar aqui e tudo mais, você ouviu falar em Ground Truth, você já sabe que a gente está falando em...

08:57

aquela resposta, basicamente, ela está batendo de acordo com o Ground Truth, ou seja, com a referência que eu tenho, e essa referência é a minha verdade, tá? Ou seja, é o que eu considero ok, é o que eu considero correto, beleza? Então, quando a gente está falando disso aqui, então, a gente está falando das métricas e dos tipos de avaliação. Então, até agora, a gente falou em objetivos, a gente falou em como, né? Ou seja, em quais métricas, como que eu vou fazer esses tipos de avaliação.

09:26

E aí eu tenho objetivo, subjetivo, comparação e também nós temos sistêmica. Maravilha? No nosso próximo vídeo, a gente vai para o nosso outro ponto também, que ele é importante, que é o famoso quem. Então vamos nessa.

## Resumo IA

**Abreviações**
- **AIA**: Inteligência Artificial Generativa / Assistente de IA, no contexto da fala do instrutor.
- **IA**: Inteligência Artificial.
- **LLM**: *Large Language Model* (Modelo de Linguagem de Grande Porte).
- **A/B testing**: Teste A/B, experimento comparativo entre duas variantes.
- **JSON**: *JavaScript Object Notation*.
- **F1**: Métrica F1, combinação harmônica entre *Precision* e *Recall*.
- **Precision**: Precisão.
- **Recall**: Revocação / Cobertura.
- **ExecMatch**: *Exact Match* (correspondência exata), conforme citado na aula.
- **Pairwise**: Comparação em pares.

**Resumo**
A aula apresentou a organização das métricas e tipos de avaliação usados para medir prompts e saídas de modelos, enfatizando que nem todo objetivo pode ser medido da mesma forma. O instrutor explicou que a avaliação se divide em quatro grupos principais: métricas objetivas, subjetivas, sistêmicas e comparativas, e que essa taxonomia evita misturar critérios semânticos, estruturais e operacionais como se fossem equivalentes.

Nas métricas objetivas, foram destacados mecanismos determinísticos, baseados em fórmula ou validação explícita, como Precision, Recall e F1, que ajudam a medir acertos, falsos positivos e falsos negativos. Também foram apresentados Exact Match, para verificar coincidência exata com a referência, string distance, para medir proximidade textual, embedding similarity, para avaliar proximidade semântica por vetores, e validação de JSON/schema validation, para garantir que a saída respeite a estrutura esperada por um sistema. Em todos esses casos, a comparação depende de uma referência conhecida, o ground truth.

Depois, a aula tratou das métricas subjetivas, que dependem de julgamento e podem ser feitas por humanos ou por outra LLM atuando como juiz, o chamado LLM as Judge. Entraram nesse grupo avaliações baseadas em rubricas e critérios descritivos, como correctness, relevance, faithfulness, conciseness, helpfulness, harmfulness, bias e toxicity, mostrando que a qualidade pode ser analisada por múltiplas dimensões e não apenas por uma regra binária.

Em seguida, o instrutor explicou as métricas sistêmicas, focadas no comportamento operacional da execução, como latência, custo em tokens, preço, throughput e pass rate. Por fim, apresentou as avaliações comparativas, como pairwise evaluation e model comparison, nas quais duas saídas são confrontadas, e o A/B testing, que é uma forma comparativa aplicada em produção para observar aceitação e performance real. Ao longo da explicação, reforçou-se que o ground truth é a fonte da verdade usada como base para medir resultados de forma técnica e reproduzível.

**Pontos de atenção**
- Não tratar todas as avaliações como se fossem do mesmo tipo; cada categoria mede um aspecto diferente.
- Métricas objetivas exigem uma regra explícita e, em geral, uma referência confiável para comparação.
- Precision alta não significa necessariamente bom desempenho geral; ela pode vir acompanhada de falsos negativos.
- Recall alto não garante precisão alta; a análise deve considerar o equilíbrio entre ambos e o F1.
- Exact Match é adequado apenas quando a resposta precisa coincidir exatamente com o gabarito.
- String distance tolera pequenas diferenças textuais, mas ainda depende de uma referência correta.
- Embedding similarity mede proximidade semântica, não igualdade literal; a qualidade do embedding influencia o resultado.
- Validação de JSON e schema validation são essenciais quando a saída será consumida por código; a estrutura deve respeitar contrato, campos e tipos.
- Métricas subjetivas dependem de rubricas claras; critérios vagos geram avaliação inconsistente.
- LLM as Judge pode ser útil, mas não elimina subjetividade; a qualidade do evaluator afeta a confiabilidade.
- Critérios como correctness, relevance, faithfulness, helpfulness, harmfulness, bias e toxicity devem ser definidos com cuidado para evitar interpretações ambíguas.
- Métricas sistêmicas avaliam execução, não qualidade semântica; é importante monitorar latência, custo, throughput e pass rate separadamente.
- Pairwise evaluation compara duas saídas em um contexto controlado; A/B testing é tipicamente aplicado em produção e considera comportamento real.
- Ground truth é a base de comparação; sem uma referência confiável, métricas objetivas perdem sustentação.