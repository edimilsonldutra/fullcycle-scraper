Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16860)

## Resumo da aula

Runner é o agente que efetivamente roda a avaliação definida pela equipe. Objetivo e métrica dizem o que medir e como medir; o runner responde quem aplica essa checagem sobre entradas, saídas e, quando existir, uma referência. Em implementações reais, esse executor pode ser código determinístico, uma LLM configurada para julgar respostas ou um avaliador especializado em comparação entre alternativas.

Code Evaluator é um evaluator implementado como lógica programática: fórmula, regra ou função que inspeciona o resultado gerado e devolve um valor avaliativo. Ele normalmente opera sobre três elementos: input, output e um campo opcional de referência, usado quando existe ground truth para comparação. O retorno costuma ser estruturado e simples de consumir por pipeline, como número, string categórica ou booleano.

A referência é o valor esperado usado pelo evaluator para decidir se a saída ficou dentro ou fora do critério definido. Quando ela existe, o evaluator deixa de apenas inspecionar a resposta e passa a compará-la contra uma base explícita, o que viabiliza métricas determinísticas como Exact Match. Sem essa referência, a avaliação ainda pode existir, mas tende a depender de julgamento por rubrica em vez de comparação direta.

Retomando o uso de métricas já estabelecidas, Exact Match é um caso típico de Code Evaluator porque a regra de decisão é literal: a saída coincide exatamente com a referência ou não. Se a pergunta tem como ground truth PostgreSQL e a resposta também é PostgreSQL, o evaluator pode retornar algo como key = Exact Match e score = 1; caso contrário, score = 0. Esse formato binário é útil quando a tarefa exige correspondência exata e não tolera variação intermediária.

LLM as Judge usa uma LLM para aplicar critérios subjetivos já definidos por rubrica ou instrução. Em vez de calcular igualdade literal, esse evaluator interpreta a resposta segundo dimensões como relevância ou conciseness e devolve um score acompanhado, em muitos casos, de comentário justificativo. Se a pergunta é sobre goroutines em Go e a resposta fala de threads em Java, o evaluator pode atribuir baixa relevância porque a saída não atende ao domínio solicitado.

Pairwise evaluation é o método comparativo entre duas saídas; pairwise evaluator é o agente que executa essa comparação e produz o resultado. A diferença importa porque o critério comparativo já pode estar definido previamente, mas ainda é preciso um executor que receba as duas respostas, aplique esse critério e devolva uma preferência. Em um caso com o mesmo input, se a resposta A usa context.WithTimeout e a B sugere time.Sleep, o evaluator pode retornar pairwise preference = A por aderência técnica ao problema.

Summary Evaluator agrega resultados individuais de vários exemplos e os transforma em métricas consolidadas. Ele existe porque olhar item por item em um dataset maior dificulta perceber o comportamento geral do prompt, enquanto o resumo mostra tendência, taxa de acerto e desempenho agregado. Em um conjunto de dez casos, esse evaluator pode compilar pass rate, precision, recall e F1 para representar o experimento em poucas medidas finais.

Métricas agregadas são valores calculados a partir do conjunto de avaliações individuais, não de um único exemplo isolado. Elas servem para responder como o prompt se comporta no dataset como um todo, reduzindo o risco de concluir algo com base em casos pontuais. Pass rate, precision, recall e F1 entram nessa camada porque resumem distribuição de acertos e erros ao longo da amostra avaliada.

Composite Evaluator combina múltiplas métricas em um score derivado por fórmula definida pela equipe. Diferentemente do summary simples, ele não apenas resume o que já foi medido: ele aplica pesos e produz uma medida composta alinhada ao que mais importa no sistema. Se correctness vale 0,9, relevance 0,7 e conciseness 0,8, uma média ponderada com pesos 0,5, 0,3 e 0,2 pode gerar um score final como 0,83, sintetizando prioridades de negócio e engenharia.

O fluxo completo pode ter três níveis: avaliação individual por exemplo, resumo agregado do dataset e score composto por fórmula. O primeiro nível responde ao caso específico; o segundo mostra o comportamento geral; o terceiro reorganiza esse comportamento segundo pesos estratégicos. Essa separação ajuda a interpretar experimentos de prompt sem confundir observação local com decisão global.

## Transcrição

00:01

Bom, pessoal, agora que a gente entendeu de forma geral, né, objetivos e métricas e tipos de avaliação, a gente tem que ter alguém que vai executar essa avaliação pra gente, tá? Então, eu sei quem...

00:15

Eu sei o quê, eu sei como, mas quem vai fazer isso? Quem é o meu runner? Normalmente você pode encontrar esse termo também, o runner. O runner é quem vai realizar a avaliação. Então pode ser o avaliador ou pode ser o evaluator.

00:32

Então, é o camarada que vai executar. Então, a gente tem alguns tipos aí nesse nosso caso. Então, a primeira coisa aqui é um Code Evaluator. O que isso significa no final das contas? É um código, uma fórmula que você vai ter e...

00:49

essa fórmula, esse código, ele vai avaliar a saída, baseado no que aconteceu, o código executado, e a gente tem ali a nossa resposta. Legal? Ou seja, normalmente nesse tipo de coisa, quando a gente está falando em Code Evaluator, normalmente a gente tem três pontos importantes. É isso que é importante você se ligar.

01:08

eu tenho a entrada, ou seja, o que eu quero fazer, a minha avaliação, eu tenho a saída, ou seja, o resultado dessa avaliação, e eu tenho um campo que normalmente é opcional, que é a referência. Ou seja, na hora que eu for fazer alguma verificação, se ela tem referência, eu consigo fazer alguma comparação e ver se aquilo está dentro ou fora do que eu estou esperando, tá?

01:32

E, normalmente, um Code Evaluator retorna para a gente um número, uma String, um True ou False. Então, basicamente, essa é a ideia. Vou dar um exemplo aqui. Uma pergunta. Qual o banco de dados mais utilizado no mundo? A referência que eu tenho, o meu Ground Truth, é o PostgreSQL, por exemplo.

01:53

E a saída do camarada, do meu resultado, foi POSSIBLE. Então, eu tenho uma avaliação, nesse caso, que foi feita, nesse caso é um EXACT MATCH, ou seja, no final das contas, o dado bateu exatamente como era a minha referência, e eu tenho meu EXACT MATCH. Então, vamos imaginar que eu recebo um resultado parecido com isso. A minha key é EXACT MATCH e o score é 1, por exemplo.

02:16

Normalmente, quando a gente está trabalhando com um exact match, o score é 0 ou o score é 1. Não tem no meio do caminho, tá? Mas você vai perceber que, ao longo do tempo, a gente vai aprender a fazer outras avaliações, porque a gente não precisa saber algo somente binário, 0 ou 1 também, tá? Então, esse foi um exemplo aí para vocês. Um outro exemplo importante aqui também é a parte do LLM como juiz. Ou seja, eu vou usar o LLM para julgar as minhas saídas,

02:43

com base em uma rubrica, ou seja, com base numa referência que eu tenho, ou com base no que o modelo foi treinado, ou com alguma instrução específica. Então, com isso, eu vou conseguir fazer essa definição desses meus critérios, ou seja, com base na relevância

03:03

eu quero que você verifique isso, o LLM. Com base no conciseness, eu quero que você verifique. Então, basicamente, o LLM as Judge, a gente cria um prompt para ele, e baseado nesse prompt, ele vai fazendo esse julgamento, e a gente pode escolher e falar com ele o que você quer que ele faça esse julgamento para a gente. Então, eu tenho um exemplo aqui. Então, como usar GoalRoutines em Goal?

03:33

aí a saída fala sobre Threads em Java, ou seja, algo que não tem nada a ver.

03:39

Então, vamos imaginar que eu fiz uma avaliação do tipo de relevância, para verificar minha relevância, e o resultado da relevância foi o score 0.2 e um comentário colocando resposta final no fala de gol, por exemplo. Ou seja, eu consegui ver o quão relevante tem ali na minha resposta. Eu vi que a minha relevância ali é baixa. Então, é basicamente isso que a gente consegue ter. Agora, somente para você lembrar, a gente tem aquele montão de métrica que a gente

04:07

falou aí ao longo do tempo e que a gente vai ver nesses exemplos mais práticos, tá? E aqui nós temos um outro camarada que é chamado de pairwise evaluator, tá? Apesar de a gente ter avaliações do tipo pairwise,

04:23

Eu tenho um avaliador de pairwise, então existe o tipo de métrica que foi utilizada como pairwise, mas eu tenho o pairwise evaluator, o cara que faz a evaluação, o evaluation,

04:39

da minha pairwise, tá? Então, não confundam, tá? Porque uma coisa é um pairwise evaluator, outra coisa é o meu pairwise evaluation em relação a comparar as duas saídas. Ou seja, aqui são as métricas que eu vou receber. Aqui é qual o tipo de evaluator que vai rodar para eu receber aquelas métricas, tá? Então, vamos imaginar o seguinte, eu tenho duas respostas com o mesmo input.

05:05

Ou seja, eu quero verificar quais critérios para eu escolher a minha melhor saída. Então, por exemplo, nesse caso eu vou colocar assim, como trabalhar com timeout em uma HTTP request in go? Aí a minha primeira resposta a retorna trabalho com text with timeout. E a segunda resposta saiu como time.sleep. Então, nesse caso aqui, eu estou querendo avaliar o que está correto.

05:31

E o resultado vai ser o pairwise preference, o value vai ser A. Ou seja, porque a minha resposta foi A com meu context.withTimeout, que é a resposta correta. Galera, eu sei que é bastante coisa, eu sei que é bastante métrica, pode dar um nó na nossa cabeça, mas acredite que eu vou tentar trabalhar isso da forma mais prática para que você consiga entender o que eu estou querendo trazer aqui para vocês. Mas é importante a gente ter essa visão geral.

06:00

E o outro tipo de cara que a gente tem aqui também é o Summary Evaluator, tá? Ou seja, ele agrega métricas, tá? Então ele gera score de múltiplos exemplos em métricas finais, tá? O que isso significa? Porque muitas vezes você faz a...

06:20

avaliação, sei lá, com um dataset de 10 registros, por exemplo, certo? E cada uma dessas avaliações eu vou tendo um resultado diferente, ok? Quando eu estou falando de um summary, basicamente eu estou falando de um resumo. Então, ele pega a resposta de todos e compila para mim.

06:41

para que eu consiga entender o que deu ali para mim. Então, é uma forma de eu conseguir ter a informação de forma resumida para que eu não precise ficar olhando informação por informação. Então, vamos lá. Um exemplo. Imagina que eu tenho um dataset com dez exemplos de pergunta e resposta. 87 foram corretas. A avaliação de pass rate. Então, eu sei. Precisão de 0,80. O recall de 0,84. O F1 de 0,82.

07:10

Pessoal, relaxem em relação a o que é Precision, o que é Recall, o que é F1, porque eu vou mostrar pra vocês isso na prática também, tá? Nesses momentos eu estou apenas querendo dar uma visão geral de objetivo, os tipos de como eu avalio e quem avalia, beleza? Então, esse é um Summary Evaluator, tá? E a gente tem mais um outro cara aqui que a gente chama de Composite Evaluator.

07:35

Esse cara aqui é levemente um pouco mais complexo porque é o seguinte, ao invés de ele fazer um resumo que nem o Summary faz, ele faz esse resumo também. Mas esse resumo ele faz baseado numa fórmula que você quer. Ou seja, imagina que eu quero fazer uma média ponderada de diversos dados,

07:53

E, baseado nessa média ponderada, eu tenho a minha forma de fazer a avaliação. Então, eu posso criar a minha própria fórmula. Então, vou imaginar que eu tenho 0,9 de correctness, 0,7 de relevance, eu tenho de conciseness, eu tenho 0,8. Então, vou imaginar que a minha fórmula, eu dou pesos diferentes. Então, para correctness, eu coloco 0,5, para relevância, eu coloco 0,3, e para conciseness, eu coloco 0,2. Então, nesse caso ali, o que eu fiz?

08:23

eu criei um tipo chamado, a qualidade weight, foi pesado, foi baseado nos pesos, e o score foi de 0,83. Então, basicamente, eu criei a minha própria fórmula baseada nas métricas que eu já tenho para fazer o meu resumo do que eu acho importante para mim. Então, o summary, no final das contas, ele traz o resultado do que ele já tem.

08:46

a parte de composite, no final das contas, ela está fazendo o quê? Pegando o que a gente já tem e criando ainda mais uma camada de abstração em cima dessa, baseada em pesos, normalmente em fazer uma média ponderada do que você quer trabalhar.

09:03

Beleza? Então, esses são os pontos principais que eu queria trazer, pessoal. Porque é bastante coisa, é overwhelming, realmente tem bastante informação. E é por isso que evaluation é algo extremamente difícil, tá? E perceba...

09:20

que no nosso caso aqui, nós estamos muito focados, nos exemplos que eu vou trabalhar, em relação principalmente à prompt, tá? Mas você vai perceber que quando a gente está falando em evaluation, e muitas vezes a gente vai estar, sei lá, em momentos em arquitetura,

09:36

a gente vai trabalhar em RAG, você vai perceber que a gente tem evaluation de RAG especificamente, evaluation de conversas multi-turn, ou seja, uma conversa que é longa, não é apenas um simples dataset, ou seja, eu tenho uma conversa que é mais extensa, onde tem um chat e um humano o tempo inteiro conversando e como que eu consigo fazer essas avaliações.

09:59

Mas, no momento que a gente está aqui, nesse capítulo, o nosso foco principalmente está a olhar pelo prisma do prompt e também entender essas principais métricas ao longo dessa nossa jornada. Fechou? Então, vamos nessa!

## Resumo IA

**Abreviações**  
- **LLM**: *Large Language Model* (Modelo de Linguagem Grande)  
- **RAG**: *Retrieval-Augmented Generation* (Geração Aumentada por Recuperação)  
- **F1**: *F1 Score*  
- **HTTP**: *Hypertext Transfer Protocol*  
- **Go**: linguagem de programação Go  
- **Java**: linguagem de programação Java  

**Resumo**  
A aula apresentou quem executa a avaliação em um fluxo de avaliação de prompts e respostas: o **runner**, responsável por aplicar o evaluator sobre entradas, saídas e, quando houver, uma referência. O instrutor explicou que a avaliação pode assumir diferentes formas, começando pelo **Code Evaluator**, que usa lógica programática, regra ou fórmula para verificar o resultado gerado com base em input, output e referência opcional. Nesse contexto, a presença de uma referência, ou *ground truth*, permite comparações determinísticas, como no caso de **Exact Match**, em que a saída deve coincidir literalmente com a referência e retornar um score binário.  

Em seguida, foi abordado o uso de **LLM as Judge**, no qual uma LLM é configurada por rubrica, instrução ou critério para julgar a resposta segundo dimensões subjetivas, como relevância e concisão, normalmente retornando score e comentário justificativo. Depois, o instrutor diferenciou **pairwise evaluation** de **pairwise evaluator**: a avaliação comparativa entre duas saídas e o agente que executa essa comparação, produzindo uma preferência entre as alternativas. Na sequência, foram apresentados os avaliadores de nível agregado, como o **Summary Evaluator**, que consolida os resultados de vários exemplos em métricas finais, como pass rate, precision, recall e F1, facilitando a análise do comportamento geral em um dataset. Por fim, foi explicado o **Composite Evaluator**, que não apenas resume resultados, mas combina métricas por meio de uma fórmula ponderada definida pela equipe, permitindo criar um score composto alinhado às prioridades do sistema. A aula fechou destacando que o fluxo pode ser visto em três camadas: avaliação por exemplo, resumo agregado e score composto, com foco principal em avaliação de prompts, mas com aplicação também em RAG e conversas multi-turn.  

**Pontos de atenção**  
- Não confundir **métrica**, **tipo de avaliação** e **avaliador/runner**: uma coisa é o critério medido, outra é o mecanismo que executa a checagem.  
- Em **Code Evaluator**, os três elementos principais são **input**, **output** e **referência**; a referência pode ser opcional, mas muda bastante a forma de avaliar.  
- **Exact Match** é binário: ou bate exatamente com a referência, ou não bate; não há meio-termo.  
- **LLM as Judge** depende de rubrica, instrução e critério bem definidos; sem isso, o julgamento fica inconsistente.  
- Em avaliações subjetivas, como relevância e concisão, o avaliador pode retornar também comentário explicativo, não apenas score.  
- **Pairwise evaluator** não é o mesmo que **pairwise evaluation**: o primeiro é o agente que executa, o segundo é o tipo de comparação entre duas saídas.  
- Em avaliações **pairwise**, o foco é escolher a melhor entre duas respostas para o mesmo input, geralmente com base em aderência técnica ou qualidade.  
- **Summary Evaluator** serve para enxergar tendências do conjunto; olhar só exemplos isolados pode levar a conclusões erradas.  
- Métricas agregadas como **pass rate**, **precision**, **recall** e **F1** ajudam a interpretar o comportamento global do dataset.  
- **Composite Evaluator** exige definição clara de pesos e fórmula; ele reflete prioridades de negócio e engenharia, não apenas uma média simples.  
- Avaliação é naturalmente complexa e pode ficar “overwhelming”; por isso, é importante separar avaliação local, resumo global e score composto.  
- O conteúdo da aula está mais centrado em **prompt evaluation**, mas os mesmos conceitos aparecem em contextos como **RAG** e conversas **multi-turn**.