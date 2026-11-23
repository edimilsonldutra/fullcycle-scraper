Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16615)

## Resumo da aula

Zero-shot é a escolha padrão quando a tarefa é simples, genérica e não depende de um domínio muito específico. Casos como validar JSON, identificar elementos de uma frase ou resumir um texto curto costumam funcionar sem exemplos, porque o modelo já reconhece esse padrão com pouca instrução. Em cenários de alto volume, essa escolha ganha importância econômica: menos tokens por requisição significam menor custo agregado e menor latência.

Few-shot se justifica quando o domínio tem muitas especificidades ou quando o formato esperado precisa ser moldado com precisão. Retomando a ideia de saída esperada já estabelecida, os exemplos funcionam como demonstrações concretas do comportamento desejado: dado X, retorne Y. Isso aumenta a chance de aderência ao padrão correto, mas cobra um preço operacional em tokens, tempo de resposta e processamento.

Um exemplo não serve apenas para “ajudar” o modelo; ele codifica explicitamente o padrão de resposta que deve ser reproduzido. Por isso, few-shot é uma forma prática de controlar formato, estrutura e nível de adequação da saída em domínios sensíveis ou altamente específicos. O ganho de qualidade vem justamente do fato de o modelo não precisar inferir sozinho qual resposta seria considerada correta naquele contexto.

A decisão entre zero-shot e few-shot precisa ser tratada como conta, não como preferência. Se zero-shot entrega 86% de assertividade com custo base e few-shot entrega 90% com custo 20% maior, a pergunta correta não é “qual é melhor?”, mas “quanto custa cada ponto percentual adicional de acerto?”. Essa formulação transforma prompt engineering em decisão mensurável de produto e operação.

Considere um sistema que custa 10 mil dólares por mês com zero-shot e 12 mil dólares por mês com few-shot. O ganho foi de 4 pontos percentuais de assertividade ao custo adicional de 2 mil dólares, então cada 1% extra custa 500 dólares. Esse cálculo permite discutir o prompt em termos de retorno marginal: pagar mais só faz sentido se o impacto do erro evitado justificar esse valor.

A escolha do prompt nem sempre pertence apenas ao desenvolvedor, porque ela afeta orçamento, experiência do usuário e risco operacional. Em vez de decidir isoladamente, a engenharia precisa traduzir a escolha em linguagem de negócio: pagar mais para reduzir erro ou aceitar mais erro com processos de mitigação. Isso conecta prompt engineering a produto, finanças e operação, e amplia o problema para além da escrita do prompt.

Nem todo erro tem o mesmo peso, então a assertividade necessária depende da criticidade da tarefa. Se o processo tolera falhas e possui mecanismos de mitigação, pode ser racional aceitar uma taxa de erro maior para economizar custo e latência. Em tarefas mais sensíveis, o ganho de assertividade pode justificar prompts mais caros, e até 90% pode continuar insuficiente.

Prompt engineering não se limita à formulação textual da instrução; ele também envolve escolher o nível de contexto e exemplificação compatível com a escala de uso. Zero-shot e few-shot são instrumentos com efeitos econômicos e operacionais diferentes, e a escolha entre eles altera a viabilidade do sistema. Projetar prompts, portanto, inclui raciocinar sobre custo recorrente, tempo de resposta e valor de negócio do ganho de qualidade.

## Transcrição

00:01

Então, vamos lá falar de guidelines. Uma ideia que eu vejo com a experiência e vejo também com a experiência de outros devs que estão trabalhando o tempo inteiro com o IA é o seguinte, se você tem uma tarefa simples, um senso comum de alguma coisa, ou seja, valide, identifique, sumarize, faça qualquer coisa desse tipo,

00:24

você vai utilizar zero shots. Você não precisa trazer exemplos a maioria das vezes. Por quê? Porque são coisas que acabam sendo bem simples. Por exemplo, valide-se esse JSON é válido. Cara, a IA vai conseguir identificar. Identifique o sujeito dessa frase. Resuma esse parágrafo em cinco palavras.

00:46

Ou seja, esse tipo de tarefa, e normalmente essas tarefas, não são necessariamente utilizadas para desenvolvimento. Ou seja, para um workflow de desenvolvimento. É muito raro você fazer isso.

01:02

Então, você vai trabalhar com zero shot. Você não precisa dar nem exemplo. Você pede e aguarda o resultado com a menor quantidade de tokens possível. Outra coisa, alto volume. Se você tem ali uma requisição, umas chamadas para IA que tem um volume absurdamente alto, você também vai trabalhar com zero shot.

01:28

Ou seja, faça isso e ela vai fazer isso de uma forma mais barata e rápida. Obviamente, você tem que testar, tem que ver modelo e tudo mais, mas se você tem um alto volume, o volume é muito grande, a quantidade de tokens é muito grande, esse negócio vai virar praticamente inviável. Então, sempre que você puder, você vai desenvolver um agente, você vai fazer qualquer coisa, e se forem coisas que

01:58

não tenha um domínio muito específico, você vai poder usar zero shot, tá? Agora, se você está numa situação, tá? Onde há muitas especificidades, o resultado, o formato esperado, ou seja, você está num domínio extremamente específico, sei lá, eu estou fazendo algo de medicina, eu estou fazendo algo de psicologia, eu estou fazendo contas matemáticas, eu estou fazendo qualquer coisa desse tipo,

02:26

O que acontece? Você vai utilizar o fill shot. Por quê? O fill shot vai sempre mostrar para você o resultado esperado. Então, baseado no exemplo X, eu espero que você retorne Y. Baseado no exemplo Z, eu espero que você retorne W. Baseado no exemplo A, eu espero que você faça COMPLETE.

02:52

E aí ela vai trazer esse resultado. Ou seja, trabalhar com o fio shot é muito mais caro com o zero shot, a latência é maior, e acredite que você gasta muito mais token e processamento da IA quando ela tem que imitar um comportamento que você passou pra ela.

03:11

Então, nesse momento, o que eu recomendo sempre é, trabalhe com exemplo. E uma coisa interessante é que, se você perceber, o exemplo sempre traz o que é esperado dela. Ou seja, no final do dia, você está dando o quê? O formato de saída. Que foi exatamente isso que a gente falou logo no início.

03:32

aqui desse módulo, tá? Então, isso aí é um ponto importante, porque isso afeta diretamente o custo ali pra gente, tá? Então, eu vou dar um exemplo aqui em relação à reflexão e trade-offs em relação a isso, tá? Então, vamos imaginar que, com zero shot, eu tenho 86% de assertividade com custo X.

03:54

Legal? Com o FeelShot, eu tenho 90% de assertividade com custo X mais 20%, por exemplo. E aí, eu vou ter que fazer a minha conta em relação ao meu Prompt. Quanto custa 4% de assertividade? Ou seja, que é a diferença de ZeroShot para FeelShot. Então, eu vou dar um exemplo simples aqui para você. Imagina que o custo atual no ZeroShot é de 10 mil dólares por mês.

04:21

E, como o feel shot é de 12 mil dólares por mês, então significa que com a cada 1% de assertividade a mais que eu vou ter da minha, vai custar 500 dólares. Legal? Ou seja, para que eu saia de 86 para 90, eu vou gastar 2 mil dólares a mais, ou seja, para cada

04:46

1% eu tô pagando 500 dólares. E aí a questão aí, no final das contas, é...

04:52

vale a pena? Então, é essa conta que você tem que colocar no papel. E quando você coloca no papel, você também vai ter que chegar na área de produto, na área financeira, em todos os momentos, e trazer, inclusive, para ele, porque, muitas vezes, essa decisão não compete, não é de competência do desenvolvedor. O que o desenvolvedor vai ter que falar é

05:18

Cara, a gente vai ter 4% de respostas piores por conta de 2 mil dólares. O que vocês querem? Pagar 2 mil dólares a mais ou ter 4% de possibilidade de erro? Mas nós temos algumas coisas, alguns processos de mitigação.

05:38

e a gente vai conseguir lidar com isso. Sei lá, da mesma forma que a gente lida com consistência eventual em sistemas, e isso é um trade-off também, talvez a quantidade de acertos que a IA vai dar em determinado tipo de tarefa, e às vezes essa tarefa não é nem tão crítica,

05:54

Às vezes vale a pena economizar ou às vezes vale a pena eu pagar ainda mais porque 90% não é o suficiente, tá? Então, fique sempre ligado com esses trade-offs. São pegadinhas e isso aqui tem tudo a ver com o quê?

06:13

Prompt, galera. Perceba que a gente está falando aqui em zero-shot, a gente está falando aqui em few-shot. Você entende como quando a gente vai em aspectos um pouco mais profundos na parte de prompt engineering, a gente não está pensando em apenas como escrever prompts, tá? Obviamente que quando a gente acaba entrando em assuntos como arquitetura e a gente vai falar de prompt,

06:40

Ainda assim, a gente vai falar um pouco disso, mas o prisma é diferente, tá? O prisma é diferente, tá? Então, esses aí são aspectos que eu quero que você leve em consideração quando você vai criar o seu prompt, perfeito? Então, vamos nessa!

## Resumo IA

**Abreviações**  
- **IA**: Inteligência Artificial.  
- **JSON**: JavaScript Object Notation.  
- **devs**: desenvolvedores.  
- **workflow**: fluxo de trabalho.  

**Resumo**  
A aula apresentou orientações práticas para escolher entre **zero-shot** e **few-shot** na engenharia de prompts. O instrutor explicou que o **zero-shot** deve ser a escolha padrão quando a tarefa é simples, genérica e não depende de um domínio específico, como validar um JSON, identificar um elemento de uma frase ou resumir um texto curto. Nesses casos, o modelo geralmente reconhece o padrão sem necessidade de exemplos, o que reduz custo, latência e consumo de tokens, especialmente em cenários de alto volume.

Já o **few-shot** foi apresentado como a abordagem adequada quando há muitas especificidades, quando o domínio é altamente particular ou quando o formato de saída precisa ser moldado com precisão. Os exemplos funcionam como demonstrações do comportamento esperado, isto é, deixam explícito para a IA o padrão de resposta a ser reproduzido. Isso aumenta a aderência ao resultado desejado, mas encarece a requisição em tokens, tempo de resposta e processamento.

O instrutor reforçou que a decisão entre zero-shot e few-shot não deve ser tratada como preferência pessoal, mas como uma análise de custo-benefício. A escolha precisa considerar métricas como assertividade, custo mensal, latência e impacto do erro. Foi exemplificado um cenário em que um ganho de 4 pontos percentuais de acerto custaria 2 mil dólares a mais por mês, levando à pergunta central: quanto custa cada ponto percentual adicional de qualidade? A partir disso, a aula conectou prompt engineering a decisões de produto, finanças e operação, destacando que nem toda tarefa exige a mesma precisão e que a criticidade do contexto determina se vale a pena pagar mais por melhor desempenho.

**Pontos de atenção**  
- **Zero-shot é indicado para tarefas simples e genéricas**, principalmente quando o modelo já conhece bem o padrão esperado.  
- **Em alto volume, o custo por tokens importa muito**: mesmo pequenas diferenças de consumo se tornam relevantes no agregado.  
- **Few-shot aumenta custo, latência e processamento**; use apenas quando o ganho de qualidade justificar esse impacto.  
- **Exemplos em few-shot não são “ajuda genérica”**: eles definem explicitamente o padrão de saída desejado.  
- **A escolha do prompt deve ser feita por trade-off**, não por preferência subjetiva.  
- **Considere sempre a conta de negócio**: custo adicional versus ganho de assertividade.  
- **Nem todo erro tem o mesmo peso**; a criticidade da tarefa deve definir a taxa de erro aceitável.  
- **A decisão não é só do desenvolvedor**: envolve produto, finanças e operação.  
- **Processos de mitigação podem permitir aceitar menos assertividade**, quando o risco for tolerável.  
- **Prompt engineering vai além de escrever instruções**: inclui escolher o nível adequado de contexto e exemplificação para a escala de uso.