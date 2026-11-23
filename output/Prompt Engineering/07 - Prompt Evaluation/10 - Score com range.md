Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16865)

## Resumo da aula

Avaliação binária continua útil quando a decisão precisa ser operacional, mas ela perde nuance ao reduzir tudo a yes/no ou 0/1. Em critérios subjetivos como concisão, coerência, detalhe e profundidade, duas respostas podem ser aprovadas e ainda assim ter qualidades bem diferentes. O uso de ScoreString resolve isso ao permitir notas em range, que depois podem ser normalizadas para a faixa de 0 a 1. Essa mudança transforma a leitura do experimento: em vez de apenas contar aprovações, você passa a comparar intensidade e qualidade relativa entre saídas.

ScoreString é o formato usado para pedir ao evaluator uma nota textual estruturada que pode ser convertida em score numérico. A configuração normalizada por 10 faz o evaluator produzir algo equivalente a uma escala de 0 a 10, mas o resultado final é convertido para 0 a 1, o que facilita agregação e comparação entre critérios. Isso padroniza a interpretação no dashboard e evita misturar escalas diferentes no mesmo experimento. Quando um critério aparece como 0.78, a leitura prática é “78% da escala máxima definida para esse julgamento”, não apenas “passou”.

Retomando o cenário de revisão de código, conciseness já existia como critério binário e agora ganha uma camada de nuance. Em vez de perguntar apenas se a resposta é concisa o suficiente, o evaluator passa a medir quão concisa ela é dentro de uma escala contínua. Esse reaproveitamento é valioso porque mantém o mesmo critério conceitual, mas muda a resolução da medição. A escolha entre binário e range depende do tipo de decisão: triagem rápida favorece binário; comparação fina entre versões favorece score contínuo.

Coherence mede se a análise está logicamente organizada, consistente e bem estruturada como texto técnico. Esse critério faz mais sentido em escala contínua porque coerência raramente falha de forma absoluta; com frequência, a resposta é parcialmente clara, mas tem trechos confusos, saltos de raciocínio ou organização irregular. Uma nota como 0.85 comunica que a estrutura geral está boa, mesmo sem ser perfeita. Isso ajuda a diferenciar respostas aceitáveis de respostas realmente bem construídas.

Detail avalia se a resposta traz detalhamento suficiente para sustentar a análise; depth mede se ela vai além do óbvio e apresenta profundidade real. Os dois critérios parecem próximos, mas não são equivalentes: uma resposta pode ser longa e cheia de detalhes superficiais, sem aprofundar nada, ou pode ser profunda em poucos pontos, mas insuficiente em cobertura. Separar essas dimensões evita confundir volume com qualidade analítica. No experimento, isso permite identificar se o prompt precisa incentivar mais explicação, mais profundidade ou ambos.

Os critérios de coherence, detail e depth podem ser avaliados sem referência porque dependem principalmente da qualidade interna da resposta. Já relevance, retomando o critério já conhecido, pode ser mais bem sustentado com referência quando existe um alvo esperado no dataset. Nessa situação, a configuração muda de ScoreString para labeled ScoreString, porque o evaluator precisa comparar a saída com dados de referência. A presença da referência não muda a ideia de score contínuo; ela muda a evidência usada para atribuir a nota.

No LangSmith, os critérios aparecem agregados com valores como 0.85 para coerência, 0.78 para concisão, 0.79 para profundidade, 0.81 para detalhe e 0.82 para relevância. Esses números convivem com métricas operacionais como P50, P99, latência, erro e quantidade de execuções, mas o foco analítico está no score dos critérios. A vantagem é imediata: você deixa de enxergar apenas aprovação ou reprovação e passa a ver onde a resposta está melhor ou pior. Isso torna a iteração do prompt mais orientada, porque a correção pode mirar exatamente a dimensão degradada.

Granularidade é a capacidade de distinguir diferenças pequenas, mas relevantes, entre saídas que antes cairiam na mesma classe binária. Se duas respostas receberiam yes em conciseness, um score contínuo pode mostrar 0.62 para uma e 0.91 para outra, revelando que ambas passam, mas com qualidade bem diferente. Essa leitura é especialmente útil quando o prompt já atingiu um nível razoável e o objetivo deixa de ser “fazer funcionar” para passar a ser “otimizar comportamento”. Em engenharia de prompts, essa etapa reduz subjetividade sem forçar simplificações excessivas.

## Transcrição

00:01

Bom, pessoal, agora que a gente já passou por esses evaluators, mas eles são ali no formato binário, a gente vai agora pra um camarada que é muito importante e eu uso bastante, tá? Que é quando você consegue trabalhar com score.

00:18

O início é tudo igual, vocês já devem ter percebido, ou seja, o começo do código é totalmente repetitivo, aqui também o mesmo esquema, com referência e sem referência, mas agora a gente tem algo um pouco diferente, porque eu consigo

00:33

trabalhar para fazer um score, ele trabalha com score string, onde eu consigo normalizar isso até 10. Ou seja, eu consigo, no final das contas, fazer uma conta onde o resultado vai ser de 0 até 1, tá? Então, quando eu estou trabalhando com...

00:51

Se o exemplo tiver, por exemplo, dois casos de uso binário, eu vou ter 0 e 1. Se eu tenho três usos com ScoreString, eu posso ter dados que vão variar de 0 a 1 para mim. Então, basicamente, essa é a ideia. Agora, quais são os camaradas que eu estou usando nesse nosso caso? Então, eu tenho conciseness,

01:18

Beleza? Por que eu estou colocando o conciseness de novo? Porque se você olhar aqui, eu tenho o conciseness aqui já, tá vendo? Mas aqui eu tenho ele apenas no formato binário, 0 ou 1. Aqui, se você olhar, eu vou trabalhar com score string, ou seja, eu vou poder ter esse cara, mas trabalhar ele de forma com range, entendeu? Então, por isso que nesse caso,

01:44

eu estou colocando aqui como ScoreString, tá? Então, basicamente, eu estou pegando ScoreString, o critério é Consistency Normalized by 10. Basicamente, é isso que você precisa e, nesse caso aqui, eu não estou passando nenhuma referência.

01:58

Aqui é a parte de coerência, essa análise é coerente e bem estruturada, então é um outro cara que existe, é um outro critério, e também estou passando. O outro camarada é o critério de detalhe, ele tem detalhamento suficiente para conseguir fazer essa análise. Um outro cara que eu tenho aqui é depth, ou seja, o nível de profundidade, ou seja, não é algo óbvio.

02:22

o resultado, que é algo que está sendo trazido. E perceba que eu estou colocando tudo sem referência. E o último, em relação à relevância, eu estou colocando ele com referência. Mas lembrando, pessoal, isso aí você pode brincar, e testar, e ver as diferenças. Se você olhar, é relevance. Então, se você olhar, galera, basicamente,

02:44

você vai perceber, quando eu preciso de data, eu tenho que colocar como labeled scoreString, tá? E quando eu não tenho data, eu não preciso colocar, eu coloco apenas scoreString e eu tenho essa parada aqui. E agora, os meus evaluators, ou seja, são bastante caras que eu tenho agora, eu vou conseguir fazer algumas análises e vamos ver como é que essa parada fica aqui com a gente. Então, eu vou colocar um basic, é o exemplo 3 aqui que a gente precisa. Vou colocar esse cara aqui para rodar,

03:14

E temos que esperar agora um pouquinho. Eu vou pausar o vídeo e volto assim que ele fizer o trabalho dele.

03:24

Bom, pessoal, ele terminou aqui, então vamos aqui na nossa interface do Langsmith e tá aqui, apareceu aqui pra gente. Vamos ver se ele terminou de processar tudo. Mas se você olhar aqui, eu tenho o Criteria Score, que é o que a gente estava mexendo. Esses aqui estão todos em brancos porque a gente não rodou esses exemplos, mas a gente tem esses caras aqui.

03:45

por esses caras que a gente colocou. Então, se você olhar aqui, a parte de coerência 0.85, concise 0.78, o depth 0.79, o nível de detalhe 0.81 e a relevância 0.82. Ele sempre traz aqui o P50, o P99 em relação à latência, níveis de erro, quantos rodaram e coisas desse tipo. Mas o nosso maior ponto aqui, e o que eu queria que você entendesse, é que nesse nosso caso, se você olhar,

04:15

Aqui, se você olhar onde estava o nosso amigo, aqui ó, Consciousness, aqui ele estava 18, Correctness estava 14, Helpfulness. Agora, se eu olhar aqui, eu tenho Consciousness, ele é 0.78.

04:32

ele encontrou aqui, e aqui ele falou que é yes, então provavelmente ele deve ter um critério aí a partir de tanto vai yes, a partir de tanto vai no, mas no nosso caso quando a gente pegou agora para fazer um range, ao invés de ser sim ou não, eu acabo tendo os números mais granulares e

04:51

fica muitas vezes mais fácil para eu conseguir ter uma ideia do meu nível de precisão em relação a isso, apesar de a gente vai falar de precision um pouco mais pra frente aí, fechou? Então, mais um exemplo que a gente tem aí em relação de coerência, consistency, depth aqui pra gente e também detail. E também relevance. Então, a gente teve esses caras aqui que a gente acabou avaliando. Vamos nessa, galera.

## Resumo IA

**Abreviações**
- **P50** — percentil 50; mediana das medições.
- **P99** — percentil 99; valor abaixo do qual ficam 99% das medições.
- **ScoreString** — formato de avaliação textual estruturada que gera um score numérico.
- **LangSmith** — ferramenta/plataforma para observabilidade, avaliação e análise de experimentos com LLMs.
- **Yes/No** — formato binário de decisão: sim/não.

**Resumo**
A aula mostrou a evolução de avaliadores binários para avaliadores com score contínuo, destacando que a avaliação em yes/no ou 0/1 é útil para decisões operacionais, mas perde nuance quando o objetivo é medir qualidade relativa. Para isso, foi apresentada a abordagem com **ScoreString**, que permite atribuir notas em uma escala, depois normalizada para a faixa de **0 a 1**. Assim, em vez de apenas contar aprovações, passa-se a comparar intensidade e granularidade entre respostas.

O instrutor retomou o cenário de revisão de código e reaproveitou critérios já conhecidos, mas agora em formato contínuo. O critério de **conciseness** deixou de ser apenas binário e passou a ser medido em range, o que permite distinguir respostas que “passam” com níveis diferentes de qualidade. Em seguida, foram apresentados critérios como **coherence**, **detail** e **depth**, todos avaliados sem referência, por dependerem da qualidade interna da resposta. Já o critério de **relevance** foi avaliado com referência, exigindo o uso de **labeled ScoreString**.

Na prática, o fluxo explicado foi: configurar os critérios com score contínuo, executar o experimento, e então analisar os resultados no **LangSmith**. No painel, apareceram scores como 0.85 para coerência, 0.78 para concisão, 0.79 para profundidade, 0.81 para detalhe e 0.82 para relevância, além de métricas operacionais como **P50**, **P99**, latência e erro. O ponto central foi que a avaliação contínua melhora a leitura do experimento porque revela diferenças pequenas, porém relevantes, entre respostas que antes cairiam na mesma classe binária.

**Pontos de atenção**
- Avaliação binária é útil para triagem e decisões rápidas, mas não captura diferenças de qualidade entre respostas que “passam”.
- **ScoreString** deve ser usado quando se quer medir intensidade e não apenas aprovação/reprovação.
- A normalização para **0 a 1** padroniza a leitura no dashboard e evita misturar escalas diferentes.
- **Conciseness** pode continuar sendo o mesmo critério conceitual, mas com resolução maior quando avaliado em range.
- **Coherence** faz mais sentido como score contínuo, porque respostas costumam ser parcialmente boas e parcialmente confusas.
- **Detail** e **depth** não são equivalentes: volume de informação não significa profundidade analítica.
- Critérios sem referência podem ser avaliados pela qualidade interna da resposta; critérios como **relevance** podem exigir **labeled ScoreString** quando há alvo esperado.
- Ao interpretar um valor como 0.78 ou 0.85, a leitura correta é relativa à escala máxima definida, e não apenas “passou”.
- O painel do LangSmith mostra métricas operacionais junto dos scores; o foco analítico deve ser o critério, não apenas latência ou erro.
- A principal vantagem do score contínuo é a granularidade, especialmente quando o prompt já funciona e o objetivo passa a ser otimização fina.