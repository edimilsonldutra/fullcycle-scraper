Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16866)

## Resumo da aula

Correctness e relevance já foram introduzidos anteriormente; aqui, o avanço está em executá-los com referência e ler o resultado como score contínuo, não como decisão binária. Quando a saída do modelo é comparada com o esperado do dataset, o evaluator passa a julgar aderência ao alvo conhecido, o que torna a análise mais útil para tarefas como revisão de código com ground truth estruturado. Scores como 0.75 e 0.84 não significam apenas “passou” ou “falhou”: eles mostram grau de qualidade e permitem comparar versões de prompt com mais nuance.

Faithfulness pode ser transformado em uma rubrica operacional própria quando o critério built-in é genérico demais para o caso de uso. No cenário de revisão de código, a rubrica precisa deixar explícito que a resposta deve ser grounded no código fornecido, sem inventar problemas, contexto ou suposições não observáveis. Isso muda o evaluator de um julgamento abstrato para uma checagem alinhada ao contrato real da aplicação. Como o foco é a fidelidade ao input analisado, esse critério pode ser aplicado sem referência, desde que a descrição da rubrica seja precisa.

Format adherence já era conhecido como critério, mas aqui ele deixa de ser apenas “seguir formato” e vira uma especificação concreta do que conta como conformidade. A rubrica define que a resposta deve retornar somente um JSON válido, sem texto antes ou depois, sem markdown e sem explicações extras. Esse nível de detalhe importa porque uma saída quase correta ainda pode quebrar integração, parser ou pipeline automatizado. Em vez de confiar em uma noção vaga de formato, o evaluator recebe instruções suficientes para penalizar desvios pequenos, mas operacionalmente relevantes.

Code specificity é um critério novo que mede o quanto a análise técnica realmente aponta evidências concretas no código. Uma resposta específica menciona linha, problema identificado, terminologia técnica adequada e sinais observáveis que sustentam a conclusão. Esse critério existe porque uma revisão pode parecer correta em alto nível e ainda assim ser genérica demais para uso prático. Ao separar especificidade de outros critérios, fica mais fácil distinguir “resposta plausível” de “resposta acionável para engenharia”.

Um critério built-in serve como ponto de partida, não como limite do sistema de avaliação. Quando a equipe reescreve o critério com instruções próprias, ela transforma uma categoria ampla em uma rubrica ajustada ao comportamento esperado do produto. Isso é especialmente útil quando o evaluator precisa julgar detalhes que o built-in não explicita, como idioma esperado, ausência total de texto fora do JSON ou necessidade de citar linhas do código. O ganho não é só flexibilidade: é diagnóstica, porque a nota passa a refletir exatamente o que a equipe considera qualidade.

A nota sozinha não basta; o valor real aparece no reasoning associado ao score. Quando o evaluator atribui 0.98 em format adherence, o próximo passo é inspecionar por que a nota não foi máxima e localizar o desvio concreto. No exemplo, a saída estava estruturalmente correta, mas houve desalinhamento com a instrução de linguagem, o que justificou a penalização. Essa leitura transforma avaliação em ferramenta de depuração de prompt, não apenas em dashboard de números.

Retomando o cenário de revisão de código, a mesma resposta pode receber notas altas em especificidade, médias em faithfulness e quase máximas em formato. Essa separação evita conclusões simplistas como “o prompt é bom” ou “o prompt é ruim”, porque cada critério revela uma dimensão diferente do comportamento. Uma saída pode estar bem formatada e ainda exagerar inferências; outra pode ser fiel ao código, mas vaga demais para ser útil. Avaliar em paralelo permite decidir qual aspecto do prompt precisa ser refinado.

A qualidade da resposta não é a única variável relevante em prompt engineering. Latência, consumo de tokens e custo por execução aparecem ao lado dos scores e ajudam a medir a viabilidade do prompt em produção. Um prompt com rubrica excelente, mas custo excessivo, pode ser inadequado para uso contínuo; um prompt barato, mas com baixa fidelidade, também não resolve o problema. A avaliação prática combina qualidade semântica e restrições operacionais na mesma análise.

## Transcrição

00:01

Bom, pessoal, no exemplo anterior, a gente conseguiu entender, de forma geral, como que a gente consegue trabalhar normalizando essas informações e não trabalhar com isso de forma binária. Agora, eu tenho um outro exemplo 4, que é focado em correctness. Mas, olha só que interessante aqui que a gente vai fazer. Basicamente,

00:25

Pegada é a mesma pegada, a data com referência. E aqui, agora, o que eu tenho? Eu tenho um prompt do correctness, e se eu for olhar, deixa eu olhar aqui, o prompt do correctness eval. Pretty much a mesma coisa que a gente está acostumado. Cadê aqui? correctness eval.

00:49

E o lance aqui é o seguinte, se você olhar agora aqui, eu tenho os dados com referência, tá? Estou trabalhando aqui com referência, sempre aqui trabalhando. Então, quais são os evaluators que eu estou colocando agora aqui? Eu resolvi colocar...

01:05

o correctness com referência e coloquei novamente o relevance também com referência aqui também para mim. Assim, eu consigo inclusive focar mais só nessa parte de correctness e também garantir que eu estou passando todos os exemplos e coisas que eu queria colocar aqui. Então, o que eu vou fazer? Vou executar esse meu camarada, número 4,

01:34

E enquanto esse número 4 está rodando, para a gente não ter que ficar criando necessariamente um vídeo inteiro para cada exemplo, eu vou no meu exemplo 5, que é Additional Criteria. E esses exemplos aqui são importantes porque são outros evaluators que eu posso ter de diversas formas. Então, nesse meu caso, se você olhar, eu coloquei

02:03

também com ScoreString, e eu coloquei Criteria Faithfulness. E aqui eu coloquei um detalhe para ele, ou seja, essa é uma resposta que é grounded, ou seja, ela vem realmente de alguma base,

02:21

Não invente nenhum problema ou contexto que não existe no código. Ela não assume alguma coisa que não foi mostrada. E aqui eu pedi pra ele normalizar por 10, aqui pra mim. E outra coisa que é importante você entender em relação a isso é que eu não estou usando essa opção

02:45

Built-in. Basicamente, o que eu estou dizendo é, eu criei um critério Faithfulness, e nesse critério eu coloquei a minha descrição, inclusive, para ele fazer essa verificação. Então, no final das contas, eu estou customizando o meu Faithfulness. Ou seja, isso aqui é uma customização que eu vou utilizar como base para ele fazer a minha verificação.

03:10

E se você perceber, eu estou trabalhando com data sem referência aqui pra mim. Perceba que ele nem é labeled, tá vendo? Mas ele é Faithfulness, e eu passando detalhes aqui pra mim. E aqui o formato também, né? Então, ó, a Format Adherence aqui pra mim, e eu coloquei, a resposta seguiu exatamente as instruções, ele retornou somente um JSON válido, sem nenhum texto antes ou depois, nem markdown, nenhuma...

03:35

explanação extra, né? Então, novamente, criei um outro formato customizado que utiliza as instruções que eu estou passando aqui nesse meu evaluator. E aqui, eu também criei um code specificity. Basicamente, ele analisa, por exemplo, o quão específico foi em relação a

03:58

O quão específico ele foi em relação à análise dele, ou seja, ele mostrou qual é a linha de código com aquele problema, ele usou termos técnicos, ele trouxe dados, ou seja, coloquei meio que um prompt bem simples somente para a gente entender essa situação. O ponto principal aqui é que o que a gente está fazendo é usando, e vamos dizer, reescrevendo um critério

04:22

que a gente pode ter eventualmente built-in, mas eu consigo fazer a minha detalhação. Então, ele acaba sendo um critério customizado meu. Então, isso aí eu acho que é o ponto importante. A gente estava no correctness aqui e provavelmente ele já deve ter terminado de rodar. Vamos ver como é que ficou o correctness aqui para a gente. Ele apareceu aqui, correctness evolve. Esse correctness foi o inicial, que era true ou false.

04:51

E o que a gente está vendo é o outro cara aqui. Então, vamos ver... Aqui ó, score, correctness, aqui 0.75, e o relevância 0.84. Então, foi outra forma de a gente conseguir fazer essa nossa verificação aqui, tá? Mas, a grande diferença nesse nosso caso, em relação ao critério de Evol, é que a gente está trabalhando, nesse nosso caso, com a parte de...

05:19

A gente está trabalhando usando os dados ali como referência. Então, a gente tem aqui o correctness 0.84, 0.75. E se eu for olhar aqui, deixa eu ver se eu tenho aqui outro correctness. Deixa eu ver se eu tenho aqui.

05:38

Aqui está 0.14 e 13 em relação à correctness, aqui para mim. Então eu consigo fazer até meio que essas comparações de sim ou não, ou baseado inclusive no tipo de métrica com ou sem inclusive referência que eu estou passando, que eu sei que esses últimos dois eu passei como referência ali, por exemplo.

06:02

Mas, galera, a ideia acaba sendo meio que sempre a mesma. Eu posso usar built-ins, ou seja, que o Langsmith traz, ou eu posso customizar, ou eu posso trazer que um existe, mas mesmo que seja built-in, eu posso trabalhar com ou sem referência na hora de a gente trazer esses caras aqui, tá? Vamos rodar esse Additional Criteria porque a gente tem essas opções um pouco mais customizadas, né? Então, eu vou colocar aqui Python 1,

06:32

E aí eu tenho cinco additional criteria, eu vou botar esse cara pra rodar, vou dar uma pausa rápida aqui no vídeo, e daí eu volto assim que ele terminar. Prontinho, rodou aqui, e agora vamos olhar aqui no nosso camarada. Então a gente tem aqui, deixa eu esconder esse cara aqui pra gente ficar melhor com a tela. Então ó, Custom Criteria Evolved. Então a gente vai olhar aqui...

06:56

E aqui ele criou. Então, olha só. O nível de especificidade do nosso código foi 0.91. O nível de confiança do meu código foi 0.71. E o formato aqui deu 0.98.

07:14

E é interessante, galera, porque agora a gente consegue, por exemplo, por que é 0.98? Deixa eu tentar entender aonde que ele acabou trazendo esse tipo de retorno para mim, porque eu começo a olhar essas informações e aí vai ficando cada vez mais fácil eu conseguir entender. Por exemplo, aqui ele está colocando aqui para mim as notas ruins, por isso que ele ficou 0.7, 0.9778,

07:43

deve ter algum motivo que eu não sei aonde, aqui ó, esse cara aqui ele achou que o formato provavelmente não foi igual, por isso que ele deu 0.98. Reason, o assistente respondeu com um válido JSON formato, mas sem o texto antes e depois, porém a resposta

08:04

a não estar em inglês, o que não estava sendo esperado pela resposta da linguagem. Então, o assistente não aderiu ao formato e às instruções completamente. Ou seja, estava tudo certinho, mas teve coisa que provavelmente ali estava em português, e aí ele falou, cara, não seguiu o formato. Estava todo mundo falando inglês, você metou um português aí no meio, eu vou te penalizar. Foi basicamente isso que aconteceu.

08:28

Galera, essas informações são muito preciosas na hora que você quer avaliar os seus prompts, ver realmente como é que a sua aplicação está funcionando, e o interessante, ver a latência, quanto eu gastei, vocês conseguem ver quantos tokens e qual está sendo o meu custo para conseguir rodar tudo isso aí. Isso é interessante porque depende muito do tamanho do prompt também, eu sei quanto eu estou gastando com esse cara ao longo do tempo, fechou? Então, vamos seguir porque a gente tem mais caras aí para a gente rodar. Vamos nessa!

## Resumo IA

**Abreviações**
- **LLM** — Large Language Model
- **JSON** — JavaScript Object Notation
- **prompt engineering** — engenharia de prompt
- **ground truth** — verdade de referência / dado esperado

**Resumo**
A aula mostrou como evoluir a avaliação de respostas de modelos de linguagem de uma lógica binária para uma análise com score contínuo, usando dados com referência para comparar a saída do modelo com o resultado esperado do dataset. O instrutor reforçou que critérios como correctness e relevance ficam mais úteis quando retornam notas intermediárias, pois isso permite comparar versões de prompt com mais nuance e detectar melhorias ou regressões parciais.

Em seguida, foi apresentado o uso de evaluators com referência no cenário de revisão de código, destacando que o correctness pode ser medido junto com relevance para focar na aderência ao alvo conhecido. Depois, a aula avançou para critérios adicionais e customizados, como faithfulness, format adherence e code specificity. O faithfulness foi redefinido de forma operacional para exigir que a resposta estivesse grounded no código fornecido, sem inventar problemas ou contexto não observável. O format adherence também foi detalhado como uma regra concreta, exigindo somente um JSON válido, sem texto extra, sem markdown e sem explicações adicionais. Já o code specificity passou a medir o quanto a análise técnica realmente aponta evidências concretas, como linha do código, termos técnicos e sinais observáveis.

O instrutor enfatizou que mesmo critérios built-in podem ser reescritos e ajustados às necessidades do produto, transformando uma categoria genérica em uma rubrica mais precisa e diagnóstica. Também mostrou a importância de interpretar o reasoning associado à nota: um score alto, como 0.98 em format adherence, ainda pode esconder um desvio relevante, como responder em português quando o esperado era inglês. Por fim, a aula conectou a avaliação de qualidade com aspectos operacionais, como latência, consumo de tokens e custo, reforçando que um prompt só é viável em produção quando equilibra qualidade semântica e eficiência.

**Pontos de atenção**
- Não tratar avaliação como “passou/falhou” quando o score contínuo traz informações mais úteis sobre qualidade parcial.
- Usar dados com referência quando o objetivo for comparar a saída do modelo com um alvo conhecido.
- Customizar critérios built-in quando eles forem genéricos demais para o caso de uso real.
- Em faithfulness, deixar explícito que a resposta deve se basear apenas no que está no código, sem inventar contexto, causas ou problemas.
- Em format adherence, especificar rigidamente o formato esperado; pequenas quebras podem quebrar parser, integração ou pipeline.
- Exigir code specificity para evitar respostas genéricas que parecem corretas, mas não são acionáveis.
- Sempre ler o reasoning junto com a nota para entender o motivo do score e localizar o desvio concreto.
- Avaliar critérios separadamente, pois uma resposta pode ir bem em formato e mal em fidelidade, ou o contrário.
- Considerar latência, tokens e custo junto com os scores, especialmente para uso em produção.
- Observar idioma e instruções auxiliares, pois uma resposta estruturalmente correta ainda pode ser penalizada por não seguir a linguagem esperada.