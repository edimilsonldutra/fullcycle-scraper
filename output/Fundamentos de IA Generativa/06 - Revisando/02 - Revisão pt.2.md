Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16406)

## Resumo da aula

Retomando a base de Transformers já estabelecida, multi-head attention é o mecanismo que permite ao modelo relacionar cada token com vários outros tokens da sequência ao mesmo tempo. Cada head aprende um padrão de dependência diferente, como causa e efeito, sujeito e ação, tom implícito ou pistas contextuais menos óbvias. Isso importa porque a geração não depende só da palavra atual, mas das relações que ela mantém com o restante da frase. O resultado é uma representação contextual mais rica, formada por múltiplos ângulos de leitura em paralelo.

A camada feed-forward position-wise aplica uma transformação não linear a cada posição da sequência depois da atenção. Ela existe porque atenção sozinha mistura informações entre tokens, mas ainda precisa de uma etapa que reprocesse cada representação e aumente a capacidade expressiva da rede. Como a mesma transformação é aplicada posição por posição, o processamento continua paralelizável, sem voltar ao comportamento sequencial das RNNs. Esse bloco ajuda a refinar significados ao longo das camadas e é parte central do ganho de poder dos Transformers.

Como o Transformer processa tokens em paralelo, ele precisa receber explicitamente informação de ordem. A codificação posicional com seno e cosseno injeta essa ordem usando funções periódicas que geram padrões matemáticos distintos para cada posição. Isso permite ao modelo distinguir não apenas quem são os tokens, mas onde eles aparecem na sequência. Sem esse sinal, frases com os mesmos termos em ordens diferentes tenderiam a parecer estruturalmente parecidas demais para o modelo.

Embeddings posicionais aprendidos substituem fórmulas fixas por vetores de posição ajustados durante o treinamento. Em vez de receber um padrão matemático pré-definido, o modelo aprende internamente como representar “primeiro”, “segundo”, “terceiro” e assim por diante de forma útil para a tarefa. Essa abordagem dá mais flexibilidade, porque a noção de posição passa a ser otimizada junto com os demais parâmetros. No exemplo “o cachorro mordeu o homem” versus “o homem mordeu o cachorro”, essa codificação ajuda a preservar a diferença semântica causada apenas pela ordem.

Embeddings são vetores densos que representam tokens em um espaço numérico onde proximidade indica semelhança ou relação de uso. Retomando o cenário anterior de vetores, eles são a base sobre a qual atenção, posição e transformações internas operam. O modelo não manipula palavras diretamente; ele manipula essas representações vetoriais e as atualiza camada após camada. Isso permite que significado, contexto e posição sejam combinados no mesmo fluxo computacional.

Layer normalization estabiliza os valores que circulam entre as camadas ao reescalar ativações dentro de cada exemplo processado. Ela existe porque redes profundas tendem a ficar instáveis quando a distribuição interna dos sinais varia demais ao longo do treinamento. Ao manter a escala mais controlada, o modelo aprende de forma mais previsível e com menos degradação numérica. Esse ajuste é um dos fatores que tornam viável treinar arquiteturas profundas como LLMs.

Conexões residuais criam um atalho que soma a entrada original de um bloco à sua saída transformada. Esse desenho preserva informação útil mesmo quando a transformação intermediária não consegue carregar tudo sozinha, além de facilitar o fluxo de gradientes durante o treinamento. A consequência prática é menor risco de perda de sinal em redes profundas e maior estabilidade de otimização. Em termos intuitivos, o modelo processa a informação sem abrir mão do que já estava disponível antes do bloco.

Causal Language Modeling treina o modelo para prever o próximo token usando apenas o contexto anterior. O treinamento é unidirecional: cada posição enxerga o passado, mas não o futuro, o que reproduz a lógica da geração autoregressiva usada em modelos da família GPT. Essa estratégia é adequada quando o objetivo principal é continuar texto token por token. O mascaramento causal garante que a previsão não vaze informação de posições futuras.

Masked Language Modeling treina o modelo escondendo alguns tokens e pedindo que ele os recupere com base no contexto ao redor. Como a inferência usa pistas à esquerda e à direita do token mascarado, o treinamento é bidirecional. Isso favorece tarefas em que compreender a frase inteira importa mais do que gerar texto passo a passo. A diferença para CLM não é apenas operacional; ela molda o tipo de representação linguística que o modelo aprende.

Fine-tuning supervisionado pega um modelo já pré-treinado e o adapta para tarefas mais específicas com datasets rotulados ou estruturados para aquele objetivo. Esse refinamento direciona o comportamento do modelo para domínios como geração de código, resposta a perguntas especializadas ou resumo de textos jurídicos. O ganho não vem de reaprender linguagem do zero, mas de especializar capacidades já adquiridas. A escolha entre base unidirecional ou bidirecional depende do tipo de tarefa que se quer otimizar.

Reinforcement Learning from Human Feedback adiciona uma etapa de alinhamento em que julgamentos humanos orientam quais respostas são preferíveis. Em vez de apenas prever texto plausível, o modelo passa a ser ajustado para produzir saídas mais úteis, apropriadas, seguras e compatíveis com o comportamento esperado de um assistente. Isso é especialmente importante quando o sistema representa empresas ou organizações, porque qualidade técnica sozinha não garante adequação de resposta. RLHF transforma competência linguística em comportamento mais alinhado ao uso real.

## Transcrição

00:00

E o que mais a gente aprendeu, pessoal? A gente aprendeu sobre as camadas de atenção multi-head que a gente falou aqui. Lembra disso? Então a gente aprendeu que o modelo não só lê a palavra, ele distribui a sua atenção quando ele está fazendo isso. Ele começa a olhar para múltiplas partes da frase ao mesmo tempo. Cada head que a gente fala captura um tipo de relação.

00:25

Por exemplo, o caos e efeito, o sujeito e a ação que a gente tem na frase, ou mesmo o tom de ironia ou de algum contexto oculto que pode ter dentro de uma frase. Então a gente começa a olhar que a análise gramatical, a análise textual que a gente tem quando a gente tá falando de GNI,

00:43

é uma das coisas mais importantes, mais do que um conhecimento, dado que ela não conhece. O que ela faz é tentar prever a próxima palavra, como a gente falou várias vezes aqui. Lembra de todas as discussões que a gente teve sobre criação de vetores, organização deles e como eles são trabalhados ali no dia a dia? Então, quando a gente está falando das camadas,

01:03

de multihead attention, a gente tá falando de como a IA se estrutura pra conseguir compreender todas as, como eu posso dizer,

01:17

Todas as dinâmicas de um texto, todas as capacidades de você compreender um texto, não só do que você tá lendo, mas de como aquilo tá se comportando, enquanto a sensação, o sentimento que você quer trazer, como quando a gente tá falando de forma temporal e assim por diante. Então, a gente tá olhando várias camadas reais ali de como uma GNI vai compreender o que a gente tá passando pra ela e a geração textual que ela tem que fazer depois disso.

01:46

Então, a gente falou bastante disso e explicou como isso funciona. E é como se o modelo olhasse para a frase por diversos ângulos diferentes ao mesmo tempo. Olha que complexo, olha o poder computacional que a gente tem que ter por trás para conseguir fazer isso.

02:03

E combinando essas visões, aí sim ele consegue fazer uma geração de texto que seja interessante pra gente. Por isso que a gente olha e a gente entende que ele tá pensando no final do dia. Porque ele consegue compreender a nossa fala e dar uma resposta. Beleza? A gente falou de multi-head attention, depois a gente falou um pouquinho de feed-forward position.

02:28

A gente falou um pouquinho sobre esse carinha, a gente viu que essas camadas de atenção do modelo, que ele aplica ali nas redes neurais, eles independem de cada posição. Ou seja, ele consegue introduzir, quando a gente tá falando dos modelos de Transformer, a não linearidade. Isso mudou o jogo, você permite que a transformação entre os tokens

02:50

seja mais rica, você consegue fazer isso em forma paralela e sem precisar de dependência posicional para o processamento e daí com isso você consegue ir ajustando os significados ao longo da rede neural e esse processamento é extremamente importante pessoal

03:09

Entendam isso. A mudança, quando a gente tira da linearidade e vai para a não linearidade, é o que faz a gente ter a capacidade de geração de DNAi que a gente tem hoje. Geração de DNAi ficou complicado, né? Gen, gen... Mas tá bom. Então, a gente cria essa capacidade, a gente expande essa capacidade. Isso é super importante de ficar na nossa cabeça. Isso mudou o jogo quando a gente tá falando de DNAi.

03:36

Assim como outras coisas, mas isso foi muito relevante. A gente também falou da codificação posicional. A gente falou então que o Transformer, ele não lê só da esquerda pra direita como os humanos lêem. Ele precisa de uma maneira de entender a ordem das palavras, porque a gente tá falando de não linearidade. Então tá bom, eu consigo processar de forma não linear, mas eu consigo depois juntar isso e voltar a uma linearidade?

04:00

Dado que o texto é linear, ele é da esquerda para a direita, ele é algo que é só em um sentido, só uma dimensão no final do dia. Então quando a gente está falando dessa ordem das palavras desorganizada para fazer o processamento massivo,

04:16

como que isso reflete quando a gente vai para a criação textual final depois disso. Então, para isso a gente falou um pouco de duas grandes abordagens, lembra? Seno e cosseno, as funções matemáticas que a gente aprendeu que criam padrões regulares de posição. Então, a gente aprendeu a posicionar usando seno e cosseno e falou muito de embeddings aprendidos. Então, a gente falou muito do modelo onde

04:42

do ponto onde o modelo vai aprender internamente a codificar posições ao longo do seu treinamento, como que ele compreende cada palavra, eu até dei o exemplo simplificado, óbvio minha gente, de que é como se ele estivesse dando uma senha

04:58

de posição para cada token que está sendo gerado, cada vetor que está sendo conduzido ao longo da criação neural. E depois, cada um deles chega e junta isso falando... Olha, eu sou o primeiro, eu sou o segundo, eu sou o terceiro. Um jeito mais simples de a gente explicar como os embeddings por trás funcionam. Bem simplificado, gente.

05:17

Então aqui fica na cabeça de vocês como que funciona essa organização para geração final. Essa codificação é essencial para diferenciar coisas do tipo o cachorro mordeu o homem de o homem morder o cachorro, que muda bastante, inclusive a dor vai ser muito maior quando o cachorro morder o homem.

05:37

É muito interessante a gente ver que esses detalhes precisam ser processados, organizados e pensados no final do dia pela DNAI, beleza? O que mais a gente falou, meu povo? Vamos lá! Layer Norm e Conexão Residual. A gente falou desses dois carinhas, então a gente mostrou como o modelo normaliza os sinais entre as camadas para manter os atalhos residuals.

06:04

que faz com que a gente não perca informação ao longo do tempo. Então, facilita o aprendizado forçando e evitando que os gradientes desapareçam. Quando a gente tem estouro de gradiente ou perda de gradiente, lembra que a gente falou sobre isso, que isso é um problema? Então, as conexões residuais colocam as informações na próxima

06:29

geração. Então faz com que a gente não perca o treinamento, não faça com que o treinamento tenha vetores perdidos ao longo do caminho. Isso vai fazer a gente ser mais estável e mais eficiente. Esse é um detalhe do detalhe de como funciona uma LLM, como funciona um transformer. Então aqui a gente tá falando basicamente de

06:46

como a gente faz pra manter mais qualidade do que a gente tá processando ali no dia a dia. Então lembra o que a gente falou? Eu coloco na minha camada de entrada o informacional, deixo ele processar e na saída eu coloco de novo a mesma informação da entrada pra ser calculada junto com o vetor de saída e com isso eu tenho uma estratégia de conexão residual, tá bom? Então a gente falou um pouquinho disso. A gente também falou do pré-treinamento com CLM e com MLM, lembra disso?

07:15

Então, a gente falou da Casual Language Modeling, que é o CLM, e a gente falou do Masked Language Modeling, que é o MLM. Dois jeitos de pré-treinamento. Beleza? Então, a gente entendeu que tem duas grandes formas de a gente fazer isso. Então, quando a gente tá falando do CLM, a gente tenta prever a próxima palavra, que é o que o Shared APT faz. Então, a gente vai lá...

07:38

E não olha pro futuro, a gente olha pro que a gente tem pra processar só na próxima palavra. Então eu tampo futuro, eu não olho as 400 palavras que eu vou ter pela frente, eu olho só a próxima palavra com base no que eu já processei de passado. Então a gente compreendeu que nesse tipo de estratégia há...

07:59

O treinamento é unidirecional, ele olha para o passado, compreende aquilo e gera o próximo token, o próximo token, o próximo token, o próximo token... Que é isso que o GPT faz. Lógico que eu estou falando GPT quando eu estou fazendo a geração textual. Hoje o GPT já consegue trabalhar com multi...

08:18

e as ali né ele pensa diferente para cada tipo de coisa que você vai fazer com ele ele consegue fazer outras conexões por trás mas um básico dele gptzinho lá que está falando só da geração textual sem bater em dalí sem nada disso ele é um cara que consegue trabalhar desse jeito unidirecional a gente tem um outro cara que é o mlm

08:37

que ele é diferente. Ele vai ser bidirecional e ele mascara as palavras para você descobrir quais são as palavras ocultas. Então, ele vai olhar tanto para trás quanto para frente, mascarando palavras para conseguir descobrir quais são as palavras ocultas no seu modelo de treinamento. Então, essas palavras, essas estratégias, essas tarefas que parecem simples, elas forjam a forma como os modelos vão ser capazes de entender o texto,

09:03

com mais profundidade para cada tipo de ação que a gente quer fazer. Então a gente falou um pouquinho disso também. A gente falou de uma das coisas também super importantes que é o fine-tuning supervisionado, que é quando depois do pré-treinamento os modelos eles vão ser refinados com tarefas específicas, como por exemplo gerar código, responder a perguntas médicas, resumir por exemplo texto jurídico,

09:26

e usando alguns datasets, algumas bases, alguns cabês de resultado, com o objetivo de irem mais direcionados para o modelo que a gente quer. Ou seja, eu pego um transformer que já foi pré-treinado e já está preparado para, por exemplo, geração textual, tipo um chart GPT,

09:44

E trabalho ele pra ele saber gerar código, saber responder perguntas, saber exumir textos jurídicos e assim por diante. No caso dos exemplos que eu dei, faz mais sentido você pegar um modelo bidirecional, mas você pode fazer a mesma coisa com unidirecional.

09:59

Então, a gente falou também do RLHF, que é o Reinforced Learning from Human Feedback, é onde a gente tem um reforço de aprendizado pelo nosso conhecimento. Então, tem um humano por trás que vai dar o reforço de entendimento pra IA, beleza?

10:15

Então, foi uma das últimas coisas que a gente viu nesse trecho de capacidades que uma D&I tem. O que ele faz? Então, ele mostra, a gente falou ali sobre a técnica de aprendizado por reforço, que é o que a maior parte das pessoas acha que acontece quando a gente tá falando de D&I.

10:33

A gente entende normalmente, a maior parte das pessoas com quem eu converso, entendem que este é o modelo que uma DNA é treinada. Este é um dos modelos, tá bom? Então, aqui a gente tem um aprendizado por reforço, onde a gente tem feedback de um humano que tá vendo a saída ali e ajuda a refinar o modelo pra que eles sejam mais úteis, eles tenham mais ética, sejam mais seguros. Então, você vai deixar o modelo ali mais organizadinho e fechadinho pra você não correr nenhum risco. Então, é a fase onde a gente pega um modelo,

11:03

e ensina ele a agir como um bom assistente, com respostas que são mais apropriadas, que são mais educadas, que são mais alinhadas ao que a gente espera de um bom comportamento de uma IA. Então esse aprendizado por reforço humano

11:20

Ele é super importante pra gente conseguir ter I.A.s que vão responder por empresas, que vão responder por organizações grandes, etc. Então é super importante esse tipo de treinamento também. Bom, bastante coisa também, né? Espero que você tenha conseguido guardar tudo isso. Pausinha, já já eu volto pra falar de mais um pouco do que a gente conversou até agora, beleza?

## Resumo IA

**Abreviações**  
- **LLM**: Large Language Model, ou Modelo de Linguagem Grande.  
- **GPT**: Generative Pre-trained Transformer, ou Transformer Generativo Pré-treinado.  
- **CLM**: Causal Language Modeling, ou Modelagem Causal de Linguagem.  
- **MLM**: Masked Language Modeling, ou Modelagem de Linguagem Mascarada.  
- **RLHF**: Reinforcement Learning from Human Feedback, ou Aprendizado por Reforço com Feedback Humano.  
- **IA**: Inteligência Artificial.  
- **DNAi / D&I**: forma de referência à IA/Inteligência Artificial na fala do instrutor.  

**Resumo**  
A aula retomou a arquitetura de Transformers e aprofundou os principais blocos que permitem ao modelo entender e gerar texto de forma contextual. Primeiro, foi explicado o mecanismo de **multi-head attention**, em que diferentes heads observam relações distintas entre tokens ao mesmo tempo, capturando dependências como sujeito e ação, causa e efeito, ironia e pistas contextuais. Em seguida, a aula abordou a camada **feed-forward position-wise**, que aplica uma transformação não linear a cada posição da sequência após a atenção, aumentando a capacidade expressiva do modelo sem perder o paralelismo do processamento.

Depois, o instrutor destacou a necessidade de **informação de ordem** em Transformers, já que o processamento é paralelo e não sequencial como em RNNs. Para isso, foram apresentados dois caminhos: a **codificação posicional com seno e cosseno**, que injeta posição por meio de padrões matemáticos fixos, e os **embeddings posicionais aprendidos**, em que o próprio modelo aprende representações úteis para cada posição durante o treinamento. Também foi reforçado o papel dos **embeddings** como vetores densos que representam tokens em um espaço numérico, servindo de base para combinar significado, contexto e posição.

A aula também explicou como a estabilidade do treinamento é garantida por **layer normalization** e **conexões residuais**. A normalização ajuda a controlar a escala das ativações entre camadas, enquanto as conexões residuais preservam informação da entrada ao somá-la à saída transformada, reduzindo perda de sinal e facilitando o fluxo de gradientes em redes profundas.

Por fim, foram revisadas estratégias de treinamento e adaptação de modelos: **CLM**, em que o modelo aprende a prever o próximo token apenas com o contexto anterior, típico de modelos autoregressivos como GPT; **MLM**, em que alguns tokens são mascarados e o modelo os recupera usando o contexto dos dois lados; **fine-tuning supervisionado**, no qual um modelo pré-treinado é especializado para tarefas como geração de código, perguntas e resumo jurídico; e **RLHF**, que usa feedback humano para alinhar as respostas do modelo a critérios de utilidade, segurança, ética e comportamento esperado de um assistente.

**Pontos de atenção**  
- Multi-head attention não “lê” a frase de uma única forma: cada head captura um tipo de relação diferente e complementar.  
- Attention sozinha não resolve tudo; a camada feed-forward é essencial para adicionar não linearidade e aumentar a expressividade.  
- Transformers processam tokens em paralelo, então precisam de **codificação posicional** para não perder a ordem das palavras.  
- A ordem das palavras pode mudar completamente o sentido da frase; o exemplo “o cachorro mordeu o homem” vs. “o homem mordeu o cachorro” foi usado para reforçar isso.  
- **Seno/cosseno** e **embeddings posicionais aprendidos** são abordagens diferentes: uma é fixa e matemática, a outra é ajustada no treinamento.  
- **Embeddings** são a base numérica do modelo; o Transformer não trabalha com palavras brutas, mas com vetores.  
- **Layer normalization** ajuda a estabilizar o treinamento, reduzindo variações internas excessivas nas ativações.  
- **Conexões residuais** evitam perda de informação e ajudam a mitigar desaparecimento/explosão de gradientes.  
- Em **CLM**, o modelo deve olhar apenas para o passado; qualquer vazamento de futuro compromete o objetivo autoregressivo.  
- Em **MLM**, o modelo aprende de forma bidirecional, usando contexto à esquerda e à direita do token mascarado.  
- **Fine-tuning supervisionado** é uma etapa de especialização: o modelo não reaprende linguagem do zero, apenas é adaptado para uma tarefa específica.  
- A escolha entre base unidirecional e bidirecional depende da tarefa que se quer otimizar.  
- **RLHF** é importante para alinhar o modelo ao comportamento esperado em uso real, especialmente em contextos corporativos e assistentes.  
- A qualidade técnica da geração não basta; segurança, utilidade e adequação das respostas também precisam ser treinadas e controladas.