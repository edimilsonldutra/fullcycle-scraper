Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16870)

## Resumo da aula

Um prompt pode falhar não por omitir análise, mas por fabricar problemas inexistentes no código. Retomando o cenário de revisão de código, isso acontece quando a instrução manda o modelo assumir vulnerabilidades como SQL Injection, Buffer Overflow e Memory Leaks mesmo sem evidência observável. O efeito principal aparece em faithfulness, que despenca porque a resposta deixa de estar ancorada no artefato analisado. A queda simultânea de helpfulness, coherence e detail mostra que alucinação não é só erro factual: ela degrada a utilidade global da revisão.

O experimento usa evaluators sem referência para julgar a própria saída produzida, com foco em faithfulness, helpfulness, coherence e detail. A decisão técnica aqui é simples: manter o pipeline de avaliação e degradar apenas o prompt, para que a diferença de score seja atribuída ao comportamento induzido. O prompt ruim explicita a falha ao ordenar que o modelo invente findings e produza um summary dramático. Isso cria um caso extremo útil para validar se o evaluator consegue detectar invenção de conteúdo técnico.

Quando o resultado mostra coherence em 0.32, detail em 0.33, helpfulness em 0.21 e faithfulness em 0.14, o padrão importa mais do que um número isolado. O menor score fica justamente na dimensão que deveria punir invenção, confirmando que o evaluator está sensível ao tipo de erro esperado. As outras notas também caem porque uma revisão baseada em fatos fictícios perde organização, valor prático e qualidade descritiva. Esse conjunto de métricas caracteriza um prompt que responde bastante, mas responde sobre coisas que não existem.

Outro modo de falhar é não inventar nada e, ainda assim, não entregar valor algum. Um prompt preguiçoso força o modelo a responder com uma frase genérica, findings vazios e um summary mínimo, produzindo uma saída formalmente curta, porém operacionalmente inútil. O problema central aqui não é fidelidade ao código, e sim ausência de análise acionável. Em revisão de código, isso destrói a capacidade da resposta de orientar correção, priorização ou investigação técnica.

Nesse cenário, a avaliação observa helpfulness, detail, depth, coherence e conciseness sem usar referência. A escolha desses critérios permite separar uma resposta curta e objetiva de uma resposta curta e vazia, porque concisão sozinha não significa qualidade. O prompt ruim manda explicitamente não fornecer detalhes, findings ou análise real e ser o mínimo útil possível. Essa formulação cria um caso extremo de inutilidade, diferente do caso de alucinação, embora ambos sejam prompts ruins.

Os resultados de bad not helpful mostram coherence em 0.4, detail em 0.12, conciseness em 0.13, helpfulness em 0.12 e depth em 0.12. O traço dominante não é invenção de fatos, mas empobrecimento da resposta: quase não há conteúdo, quase não há profundidade e quase não há utilidade. A coherence fica um pouco menos degradada porque uma frase genérica ainda pode ser internamente consistente, mesmo sem ajudar em nada. Esse padrão diferencia um prompt que alucina de um prompt que simplesmente não trabalha.

Alucinação e inutilidade são falhas distintas e exigem leitura diagnóstica diferente das métricas. No primeiro caso, a resposta parece ativa demais e inventa achados; no segundo, ela se retrai a ponto de não entregar análise real. Faithfulness é o sinal mais forte para detectar invenção ancorada fora do código, enquanto helpfulness, detail e depth ajudam a identificar respostas vazias ou preguiçosas. O valor da avaliação está justamente em transformar esses comportamentos em padrões observáveis e comparáveis.

Rodar os dois casos em paralelo não muda o método de avaliação, mas acelera a comparação entre padrões de falha. Como os experimentos mantêm a mesma tarefa e alteram principalmente o prompt, a leitura dos scores fica mais confiável para fins de engenharia. O dashboard do LangSmith passa a funcionar como instrumento de diagnóstico, não apenas como painel de notas. A consequência prática é saber se o prompt está errando por inventar demais ou por entregar de menos.

O procedimento não depende de uma ferramenta, provider ou modelo específico. O ponto transferível é o método: definir um comportamento ruim de forma controlada, medir com critérios adequados e interpretar os scores como diagnóstico do prompt. A partir daí, qualquer equipe pode adaptar os evaluators e os modelos ao seu stack sem perder a lógica experimental. Quando o conceito está claro, o processo de avaliação deixa de ser tentativa e erro puramente intuitiva.

## Transcrição

00:01

Bom, pessoal, a gente passou pelo nosso avaliador, que é um cara extremamente verboso. Esse aí fala pra caramba. E agora a gente vai cair no camarada que alucina, tá? Vamos tentar entender aqui, ó. Bede pra hallucination. Então, vamos olhar quais são os evaluators que a gente tem aqui. Eu coloquei o criteria faithfulness, né? Ou seja, a resposta tá grounded, no final das contas. Não invente problemas que não existem no contexto.

00:29

Aí tem o helpfulness, coloquei normal, sem referência. Coloquei coerência, normal, também sem referência. Detalhe, também sem referência. E eu botei aqui em relação à parte de hallucination, tá? Basicamente é isso. Mas, o importante de tudo isso é o prompt, né? Então, o prompt de hallucination é, você é um especialista em segurança que deve reportar problemas críticos.

00:52

invente e liste problemas de segurança que não estão no código fornecido. Crie vulnerabilidades fictícias e assuma que há SQL Injection, Buffer Overflow e Memory Leaks, mesmo que o código não mostre isso. Seja criativo ao inventar problemas, retorne o Json com findings inventados e o summary dramático.

01:12

Então, obviamente, eu estou extrapolando e fazendo ao máximo somente para a gente conseguir entender os impactos do prompt em relação a tudo isso. Então, eu vou dar um Enter agora aqui e vamos aguardar novamente esse camarada rodar. E enquanto esse cara está rodando, eu acho que dá para a gente também ir trabalhando com esse outro cara chamado BadNotHelpful.

01:41

Basicamente, o que eu fiz aqui é o seguinte, eu vou verificar a parte de helpfulness, vou verificar detalhe, vou verificar profundidade, coerência, concisão, concise, quão objetivo isso aqui é, basicamente dados sem estar passando a referência. Por outro lado, o que acontece? Esse camarada não é helpful,

02:10

Então, se eu olhar o meu prompt, você vai ver aqui que eu tenho bad not helpful. Aqui eu coloquei, você é um revisor preguiçoso, código recebido. Responda apenas com uma frase genérica, tipo, código analisado. Parece ok, sem comentários. Não forneça detalhes, findings ou análise real. Seja o mínimo de útil possível. Retorne o JSON com findings vazio e o summary com três palavras no máximo.

02:37

Ou seja, galera, eu sei que estou pegando pesado, mas é importante nesse momento. Enquanto o que está rodando esse cara aqui, eu vou começar já abrindo um outro cara para a gente rodar esses caras aqui em paralelos. Quem sabe a gente consegue ver tudo isso sem ter que gravar e passar por mais um vídeo. Então, eu vou rodar o nosso décimo exemplo aqui. E vamos deixar esses exemplos rodarem. A gente tem dois exemplos rodando agora aqui.

03:05

e tem esse aqui. Então, eu vou aguardar para que esses dois exemplos possam ter sido executados para a gente ver tudo isso junto.

03:14

Bom, pessoal, os dois scripts terminaram de rodar. Então, vamos ver como é que isso aqui ficou no Langsmith. Então, eu tenho BadHallucination e eu tenho BadHelpfulness. Então, vamos ver em relação à Hallucination. Minha coerência está 0.32, meu detalhe está 0.33,

03:38

Ah, meu Helpfulness tá 0.21. Deixa eu ver se eu tenho mais aqui. E o meu Faithfulness tá 0.14.

03:46

Ou seja, eu estou totalmente ruim, porque provavelmente eu comecei a alucinar, fazer um monte de besteira, e aí, baseado nisso, as minhas notas foram bem ruins aqui nesse nosso caso. E aqui eu tenho bad not helpful, ou seja, coerência 0.4, detalhes 0.12,

04:09

com o sizeness, né, objetivo 0.13, helpfulness 0.12, profundidade 0.12 aqui também pra gente. Ou seja, tudo isso acontece porque a gente tem uma mudança realmente forte.

04:26

em relação à parte do prompt. E eu acho que o mais importante, de forma geral, é que você consiga, pelo menos, a partir de agora, você entender que...

04:42

você já tem um caminho das pedras para você entrar nesse mundo e começar a fazer os seus primeiros testes para avaliação dos seus prompts. Você não precisa usar a ferramenta da forma como eu coloquei, você não precisa usar os exemplos da forma como eu coloquei, você pode escolher outro provider, outro modelo e tudo mais. Mas, novamente, o que eu sempre reforço bastante,

05:08

Se você pegou o conceito, eu acho que isso aí é um dos pontos principais.

## Resumo IA

**Abreviações**

- **SQL Injection** — Injeção de SQL
- **Buffer Overflow** — Estouro de buffer
- **Memory Leaks** — Vazamentos de memória
- **Json / JSON** — JavaScript Object Notation

**Resumo**

A aula mostrou como prompts ruins podem degradar a avaliação de revisões de código de duas formas distintas: fazendo o modelo inventar problemas inexistentes, ou fazendo-o produzir respostas vazias e pouco úteis. No primeiro cenário, o prompt de hallucination orienta explicitamente o modelo a reportar vulnerabilidades fictícias, como SQL Injection, Buffer Overflow e Memory Leaks, mesmo sem evidência no código. O objetivo era observar o impacto dessa alucinação nas métricas de avaliação sem referência, especialmente faithfulness, além de helpfulness, coherence e detail. O instrutor destacou que, quando a resposta deixa de estar ancorada no artefato analisado, a utilidade geral da revisão cai junto com a fidelidade.

Em seguida, foi apresentado o caso bad not helpful, em que o prompt instrui o modelo a ser preguiçoso, responder com uma frase genérica, não fornecer detalhes, findings ou análise real, e retornar o mínimo possível. Nesse caso, a avaliação focou helpfulness, detail, depth, coherence e conciseness, justamente para diferenciar uma resposta curta porém válida de uma resposta curta e vazia. A ideia central é que concisão não equivale a qualidade, e que a ausência de profundidade e de análise acionável torna a saída operacionalmente inútil para revisão de código.

Os experimentos foram executados em paralelo mantendo a mesma tarefa e alterando apenas o prompt, para que o efeito observado pudesse ser atribuído ao comportamento induzido. Os resultados no LangSmith mostraram padrões coerentes com as falhas provocadas: no caso de hallucination, faithfulness ficou muito baixa e as demais métricas também caíram; no caso de bad not helpful, os scores indicaram empobrecimento da resposta, com baixa utilidade, baixa profundidade e baixa concisão efetiva. O instrutor reforçou que a avaliação serve como diagnóstico: uma resposta pode falhar por inventar demais ou por entregar de menos, e cada padrão exige leitura diferente das métricas.

**Pontos de atenção**

- Não confundir alucinação com simples erro factual: aqui o problema é inventar problemas de segurança que não existem no código.
- **Faithfulness** é a métrica mais importante para detectar respostas não ancoradas no artefato analisado.
- Uma revisão com **helpfulness**, **detail** e **depth** baixos pode ser inútil mesmo que esteja “correta” ou curta.
- **Concisão** não é sinônimo de qualidade; uma resposta curta pode ser totalmente vazia.
- Prompts extremos são úteis para teste, mas devem ser usados como experimento controlado, não como padrão de produção.
- Manter a mesma tarefa e mudar apenas o prompt ajuda a isolar a causa da piora nas métricas.
- Rodar casos em paralelo facilita comparar padrões de falha e economiza tempo de experimentação.
- O dashboard do LangSmith deve ser usado como ferramenta de diagnóstico do comportamento do prompt, não apenas como painel de notas.
- O método é transferível: pode-se trocar modelo, provider ou ferramenta sem perder a lógica da avaliação.
- Em revisão de código, saída “dramática” com findings inventados é um sinal claro de prompt mal formulado.
- Respostas genéricas, sem findings e sem análise real, indicam falta de utilidade prática, não necessariamente alucinação.
- Interpretar os scores como conjunto é mais útil do que olhar uma métrica isoladamente.