Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16408)

## Resumo da aula

Alucinação é a produção de respostas plausíveis, mas incorretas, inventadas ou não verificadas pelo modelo. Isso acontece porque o objetivo do LLM é prever sequências prováveis, não garantir verdade factual. Em tarefas de baixo risco, esse erro pode ser tolerável; em tarefas críticas, como geração de código para produção, a saída precisa passar por validação humana. O uso responsável de LLMs depende de tratar a resposta como rascunho probabilístico, não como autoridade final.

A context window limita quantos tokens o modelo consegue considerar ao mesmo tempo entre entrada e saída. Quando esse limite é excedido, parte do conteúdo precisa ser truncada, o que pode remover instruções, contexto relevante ou histórico da conversa. Isso afeta diretamente qualidade, coerência e custo computacional. Retomando a tokenização já conhecida, a decisão prática é medir tokens, controlar o tamanho do prompt e reservar espaço para a resposta.

LLMs operam muito bem com padrões estatísticos de linguagem, mas não executam raciocínio simbólico de forma nativa com a mesma confiabilidade de sistemas formais. Por isso, tarefas que exigem manipulação exata de regras, estados ou lógica encadeada podem falhar mesmo quando a resposta parece convincente. O problema não é só errar; é errar com fluidez. Em cenários desse tipo, convém combinar o modelo com validação externa, ferramentas determinísticas ou revisão humana.

Dados recentes não estão automaticamente dentro do modelo já treinado, então informações novas precisam ser recuperadas de fontes externas. A busca na web reduz esse limite, mas introduz outro: o modelo pode consultar páginas ruins, desatualizadas ou enganosas. Por isso, restringir onde buscar e pedir referências melhora a confiabilidade operacional. A decisão prática não é apenas “buscar ou não buscar”, mas definir fontes confiáveis e fronteiras explícitas para a recuperação.

Prompt engineering é o desenho intencional da instrução para orientar comportamento, escopo, formato e fontes da resposta. Uma aplicação mais robusta disso é RAG, em que o modelo recebe contexto recuperado de uma base externa antes de gerar a saída. O ganho principal é reduzir dependência exclusiva da memória paramétrica do modelo, especialmente em conhecimento específico, recente ou interno à organização. Retomando o cenário de operação real, isso permite enriquecer a resposta com documentos relevantes em vez de confiar apenas no que o LLM “lembra”.

Embeddings já foram definidos antes; aqui o ponto novo é seu uso operacional para medir semelhança sem depender apenas de palavras idênticas. Quando duas frases têm vetores próximos, o sistema infere proximidade semântica mesmo com vocabulário diferente. Esse mecanismo sustenta busca semântica, recuperação de contexto e testes práticos de similaridade. No hands-on, calcular a semelhança entre embeddings mostra como a IA representa significado de forma contextual, não literal.

Temperatura ajusta o grau de aleatoriedade da geração: valores menores tendem a respostas mais previsíveis, e valores maiores aumentam diversidade e risco. Top-k limita a escolha do próximo token aos k candidatos mais prováveis, enquanto top-p restringe a amostragem ao menor conjunto cuja probabilidade acumulada atinge um limiar. Esses controles existem para equilibrar criatividade, estabilidade e aderência ao objetivo da tarefa. Em uso prático, top-k e temperatura são ajustes diretos para reduzir respostas erráticas ou tornar a geração menos repetitiva.

Retomando tokens e embeddings como conhecimento prévio, a camada nova está em observar o impacto operacional dessas unidades. Ao tokenizar um texto, fica claro que custo, limite de contexto e truncamento não seguem contagem simples de palavras. Um prompt aparentemente curto pode consumir muitos tokens, reduzindo o espaço disponível para a resposta. Testar isso na prática ajuda a evitar cortes inesperados e a planejar prompts compatíveis com o limite do modelo.

Encoder-only é a arquitetura mais adequada quando a prioridade é compreender texto, classificar, buscar ou representar semanticamente uma entrada. Modelos como BERT e RoBERTa observam o contexto de forma apropriada para tarefas de entendimento, não para geração autoregressiva aberta. Por isso, tendem a ser melhores escolhas para análise textual e recuperação de informação. Usar essa arquitetura em vez de um gerador puro evita forçar o modelo errado para um problema de compreensão.

Decoder-only é a arquitetura dominante em LLMs de geração textual, como GPT-4 e Llama. Ela é otimizada para continuar sequências token a token, o que a torna excelente para redação, chat, código e completions. Essa força em geração não implica superioridade em toda tarefa. Quando o problema central é produzir texto novo, essa arquitetura costuma ser a escolha natural.

Encoder-decoder combina compreensão da entrada com geração condicionada da saída, o que favorece tarefas de transformação textual. Tradução, sumarização e reescrita são casos clássicos porque exigem ler bem uma sequência e produzir outra com objetivo específico. Modelos como BART se encaixam nesse perfil. A escolha dessa arquitetura faz sentido quando a tarefa não é apenas entender nem apenas continuar texto, mas transformar uma entrada em outra saída estruturada.

Escolher arquitetura por hábito é um erro comum; a decisão deve seguir a natureza da tarefa. Compreensão textual e busca favorecem encoder-only, geração aberta favorece decoder-only, e tradução ou sumarização favorecem encoder-decoder. Essa adequação melhora qualidade, eficiência e previsibilidade do sistema. Em produção, a pergunta correta não é “qual modelo é mais famoso?”, mas “qual arquitetura resolve melhor este tipo de problema?”.

## Transcrição

00:00

Pessoal, não é só a parte boa, então a gente fala um pouquinho também

00:05

sobre algumas limitações e desafios que a LLM traz hoje, que a gente precisa resolver e que tem algumas estratégias para resolver, mas que são limitações e desafios para uma LLM, o que ela sofre para fazer, não é normal para ela. Então a gente falou sobre alucinação, que é o grande assunto, como que a gente pode acabar às vezes alucinando na geração de um conteúdo e como que isso é previsto e é...

00:31

anteriormente pensado para que aconteça dessa forma, para a gente poder fazer todo o resto, você precisa deixar alguma abertura para a alucinação. Então esse é um problema que a gente tem na LLM, por isso que é sempre, sempre importante usar uma LLM junto com o ser humano, que vai fazer a validação daquilo que está sendo gerado. Então é importante você ter esse tipo de estratégia. Ah, mas Nathan, eu tenho uma operação que não é crítica. Tudo bem.

00:57

Mas se você tem uma operação crítica, se você tem algo que você não pode errar, vou dar um exemplo, se você que tá assistindo essa aula vai fazer, por exemplo, a geração de um código, olha o código, analisa, não vai jogar isso pra produção de qualquer jeito. Ah não, mas eu tenho aqui a geração de uma FAQ que dá uma resposta pra um cliente sobre um produto e às vezes pode falar uma besteira. Dependendo da sua capacidade empresarial, tudo bem. Aí você precisa avaliar isso. Então vai ter certa alucinação? Sim. E é normal?

01:25

A gente também falou dos limites das janelas, do context window, de como a LLM tem essa dificuldade também, a dificuldade com raciocínio simbólico, como que para ela não é comum fazer um raciocínio simbólico ali, e a falta de atualização em tempo real, que hoje já é resolvida pela maior parte delas fazendo buscas na web, então a maior parte delas busca

01:48

esse entendimento na web e eu dei uma dica pra vocês de nichar a busca você falar onde é pra ela buscar ou até onde não é pra ela buscar mas avisar essa LLM, esse transformer quais são as fontes confiáveis ao seu ponto de vista porque se a gente deixa aberto elas vão tentar buscar essa atualização em qualquer lugar da web, vocês sabem que na web tem de tudo

02:10

Então é importante lembrar disso. Dados que são mais novos não estão no modelo de geração, ela precisa buscá-la, vai ter que fazer um modelo de busca de informação na internet, podendo errar muito aqui. Então é muito importante você pensar nisso.

02:25

tem demais novidades, às vezes ela pode alucinar ou até criar coisas que não são uma realidade, mas que ela viu em alguma página da web. Então é importante você pedir referências, é importante você nichar para aquele lugar que você quer que ela procure e onde você não quer que ela procure, isso vai te ajudar na hora que você estiver promptando. A gente discutiu ali algumas estratégias de prompt engineering, como por exemplo o REG, o Retrieval Aumented

02:49

Então, a gente falou do uso também de contextos vetoriais para mitigar esses desafios que a gente tem. Então, tem algumas estratégias para a gente conseguir diminuir esse tipo de problema. Então, a gente falou também da geração de respostas e controle, a gente falou sobre como que a gente controla a saída dos modelos

03:13

mexendo um pouquinho ali na temperatura, mexendo no Top K, mexendo no Top P, então a gente mostrou ali como fazer isso, a gente focou mais no Top K, que era o que a gente tinha ali disponível no Hugging Face, então a gente fez ali um handzone, mostrando como que a gente faz tanto a mudança de temperatura no Top K lá pelo Hugging Face, e a gente mostrou também como que a gente faz a tokenização

03:38

e como funciona a tokenização no dia-a-dia, o cálculo de palavras e assim por diante, pra gente chegar no que é um token. Então a gente mostrou também como que funciona o context window e como que ele trunca a sua saída dependendo do número de tokens que você tem de saída ou de poder de processamento.

03:57

Então, a gente também fez um outro testezinho mostrando a semelhança de embeddings, lembra disso? Então, a gente falou, como que eu faço o cálculo de semelhança entre eles, como que eu testo isso, como que eu vejo, como que uma IA entende uma frase, não só pelas palavras propriamente ditas, mas pelo contexto.

04:17

que é depois tratado com o Embeddings e mostra pra gente essa semelhança. Então foi super importante pra gente entender como que isso funciona ali no dia a dia e trazer mais pra um hands-on, mais uma coisa que a gente pode enxergar assim por diante. A gente falou também

04:32

de alguns modelos arquiteturais, beleza? Então a gente falou de três grandes modelos arquiteturais, lembra disso? Encounter Only, então só pra reforçar tudo que a gente falou até agora. Encounter Only, que vai ser usado ali pelo Bert, que é o Bert ou Roberta, eu ainda brinquei que fica o nome de uma pessoa, Roberta, então tem o Bert ou Robert A.

04:54

que é usado para compreensão textual, para busca, para fazer análise de textos maiores. A gente falou do decoder only, que é o que a gente usa no dia a dia mais normalmente, que é o GPT-4, o lhama da vida, que é usado para geração textual. A gente falou de um cara que é a junção dos dois, que é o transformer completo, que é o encoder barra decoder. Esse cara

05:21

Ele tem ali uma capacidade de tradução, sumarização e transformação textual. Então, Bart, por exemplo, é um estilo de fazer isso. E a gente mostrou como que a escolha de cada tipo desse vai impactar na saída que você vai ter.

05:37

Então, se você tentar usar o GPT-4 para fazer uma estratégia de compreensão, ele não vai ser a melhor arquitetura, talvez seja melhor você usar um BERT. Então, é importante você entender como que cada um desses caras funciona, como que a arquitetura de cada um deles, para você poder escolher a aplicação certa no seu dia a dia, onde você for usar isso. Então, a gente falou também desses modelos arquiteturais. A gente, então,

06:01

Terminou a nossa conversa ali falando um pouquinho sobre engenharia de prompt e RAG como a gente fala ali do contexto global de como isso funciona e como isso pode te ajudar no dia a dia. Beleza?

## Resumo IA

**Abreviações**
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)
- **RAG** — *Retrieval Augmented Generation* (Geração Aumentada por Recuperação)
- **Top-k** — seleção dos **k** tokens mais prováveis para amostragem
- **Top-p** — amostragem por núcleo (*nucleus sampling*), usando o menor conjunto de tokens cuja probabilidade acumulada atinge um limiar
- **BERT** — *Bidirectional Encoder Representations from Transformers*
- **RoBERTa** — *Robustly Optimized BERT Approach*
- **GPT-4** — *Generative Pre-trained Transformer 4*
- **Llama** — *Large Language Model Meta AI*

**Resumo**
A aula abordou limitações e estratégias práticas no uso de LLMs, começando pela alucinação, isto é, quando o modelo gera respostas plausíveis, mas incorretas ou inventadas. O instrutor destacou que esse comportamento é inerente ao funcionamento estatístico do modelo e que, por isso, em cenários críticos como geração de código para produção, a saída deve passar por validação humana. Em seguida, foram discutidos os limites da *context window*, mostrando como o excesso de tokens pode truncar instruções, histórico e respostas, afetando qualidade e custo. Também foi reforçado que LLMs não fazem raciocínio simbólico com confiabilidade nativa, o que exige cautela em tarefas que dependem de lógica exata.

Outro ponto importante foi a limitação de atualização em tempo real: dados novos não estão no conhecimento paramétrico do modelo, então a solução passa por busca externa, idealmente com fontes confiáveis e escopo bem definido. Nesse contexto, o instrutor apresentou estratégias de *prompt engineering* e o uso de RAG para recuperar conteúdo de bases externas antes da geração, reduzindo a dependência exclusiva da memória do modelo. A aula também retomou o papel dos embeddings na busca semântica e na comparação de similaridade entre frases, mostrando como o significado pode ser representado em vetores, e não apenas por palavras idênticas.

Por fim, foram revisados os controles de geração, como temperatura, *top-k* e *top-p*, que equilibram criatividade, estabilidade e previsibilidade da resposta. A parte final tratou das principais arquiteturas de modelos: *encoder-only* para compreensão, busca e classificação; *decoder-only* para geração textual; e *encoder-decoder* para transformação textual, como tradução e sumarização. O fluxo defendido foi escolher a arquitetura de acordo com a natureza da tarefa, em vez de seguir apenas popularidade ou hábito, e usar validação, busca controlada e engenharia de prompt para tornar o uso de LLMs mais confiável em contexto real.

**Pontos de atenção**
- Alucinação é inerente ao modelo; não tratar a saída como verdade final.
- Em tarefas críticas, sempre aplicar validação humana antes de usar a resposta em produção.
- *Context window* limitada pode truncar instruções, histórico e parte da resposta.
- Um prompt aparentemente curto pode consumir muitos tokens; é importante medir e planejar o uso.
- LLMs não executam raciocínio simbólico com a mesma confiabilidade de sistemas formais.
- Para lógica exata, estados ou regras encadeadas, é melhor combinar o modelo com validação externa ou ferramentas determinísticas.
- Dados recentes não vêm automaticamente no modelo; é necessário buscar em fontes externas.
- Busca na web pode trazer conteúdo ruim, desatualizado ou enganoso; restringir fontes é uma boa prática.
- Pedir referências e delimitar onde o modelo pode ou não buscar melhora a confiabilidade.
- RAG é útil para reduzir dependência da memória do modelo e incorporar conhecimento específico, recente ou interno.
- Embeddings são fundamentais para similaridade semântica e recuperação de contexto, não apenas para comparação literal de palavras.
- Temperatura alta aumenta diversidade, mas também o risco de respostas erráticas.
- *Top-k* e *top-p* ajudam a controlar a geração e evitar saídas excessivamente improváveis.
- Escolher a arquitetura errada prejudica qualidade e eficiência:  
  - *encoder-only* para compreensão/busca/análise,  
  - *decoder-only* para geração,  
  - *encoder-decoder* para tradução, sumarização e reescrita.
- Em produção, a decisão deve ser guiada pelo tipo de tarefa, e não pelo modelo mais famoso.