Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16583)

## Resumo da aula

Prompt chaining organiza uma tarefa grande como uma sequência de etapas especializadas em que a saída de uma vira a entrada da próxima. Isso é útil quando uma única chamada ao modelo mistura responsabilidades demais, como interpretar requisitos, gerar estrutura técnica e produzir artefatos finais. Em vez de pedir tudo de uma vez, o fluxo separa extração de esquema, geração de código e síntese final. O ganho principal é controle sobre a orquestração e sobre o tipo de modelo usado em cada etapa.

No fluxo encadeado, cada prompt template recebe variáveis de entrada, passa sua saída para uma LLM e depois para um parser que normaliza o formato para a próxima etapa. O pipe representa exatamente essa composição: prompt → modelo → parsing → próxima etapa. Retomando o uso de LangChain já conhecido, o ponto novo aqui não é o framework em si, mas a montagem explícita de uma pipeline em que cada bloco tem contrato de entrada e saída. Sem esse contrato, a integração entre etapas fica frágil e difícil de depurar.

A primeira etapa recebe uma especificação de produto em linguagem natural e extrai um JSON mínimo com campos e tipos. Esse passo existe para converter um texto ambíguo em uma estrutura intermediária mais previsível, que pode ser consumida por outras etapas sem reinterpretar o requisito inteiro. No exemplo, a especificação descreve campos como id, name, description, price e stock, além de restrições como obrigatoriedade e valores maiores que zero. Pedir “somente o JSON” reduz ruído e facilita o parsing posterior.

Depois que o esquema foi estabilizado, ele passa a ser o contexto da geração de código. O prompt pede rotas REST idiomáticas em Go, com handlers de CRUD e saída em Markdown com code blocks, o que ajuda tanto na leitura quanto na persistência do resultado. Essa separação evita que o modelo precise inferir simultaneamente os requisitos de domínio e a implementação HTTP. O efeito prático é um código mais alinhado ao esquema produzido na etapa anterior.

A terceira etapa não gera código novo; ela resume o que o pipeline produziu em uma mensagem de commit no padrão Conventional Commits. Esse tipo de síntese é útil porque transforma artefatos técnicos já gerados em documentação operacional curta e padronizada. No exemplo, a mensagem resume a criação da API de produtos com operações CRUD, validação e paginação. Isso mostra que prompt chaining não serve apenas para expandir conteúdo, mas também para condensá-lo em formatos específicos.

Um pipeline pode usar modelos distintos conforme a complexidade de cada tarefa. Extrair campos e tipos para JSON é uma tarefa mais mecânica, enquanto gerar código idiomático em Go exige mais qualidade de raciocínio e de síntese estrutural. Por isso, faz sentido usar um modelo mais simples na etapa de estruturação e um modelo mais forte na etapa de geração de código. Retomando a comparação entre modelos já conhecida, a decisão aqui é arquitetural: distribuir custo, latência e capacidade conforme a função de cada bloco.

O encadeamento só funciona bem quando a saída de uma etapa respeita exatamente o formato esperado pela próxima. Se o primeiro modelo devolve comentário extra, texto fora do JSON ou Markdown inesperado, a etapa seguinte pode falhar ou interpretar dados errados. Esse é um ponto central do prompt chaining: erros pequenos de formatação se propagam pelo pipeline e contaminam os resultados posteriores. Por isso, prompts com restrições explícitas de formato e uso de parsers são parte da implementação, não detalhe opcional.

Quando o pipeline gera muito conteúdo, imprimir tudo no terminal piora a leitura e dificulta reaproveitamento. Gravar o result_content em um arquivo como promptChainingResult.md transforma a execução em um artefato consultável, versionável e fácil de revisar. O pedido recorrente para que cada etapa escreva em Markdown existe justamente para padronizar a composição final do arquivo. O resultado deixa de ser apenas uma resposta efêmera do modelo e passa a ser documentação técnica gerada pela pipeline.

Toda etapa adicional aumenta o tempo total de execução, porque cada chamada ao modelo adiciona latência própria e espera de rede. Se uma etapa inicial errar o esquema, as seguintes podem produzir código e commit coerentes com um estado incorreto, o que torna o erro mais difícil de perceber. Além disso, múltiplas chamadas elevam o consumo total de tokens, mesmo quando cada prompt individual é curto. Prompt chaining compensa quando a decomposição melhora qualidade, auditabilidade ou automação mais do que aumenta o overhead.

Retomando a ideia de agentes já conhecida, delegação entre agentes frequentemente implementa o mesmo princípio estrutural do prompt chaining: um componente produz algo que outro consome. A diferença é que, em fluxos com agentes, essa passagem pode aparecer como decisão operacional entre papéis especializados. No exemplo, a lógica é equivalente: um bloco extrai estrutura, outro gera implementação e outro sintetiza o resultado final. Isso aproxima o pipeline de arquiteturas reais com múltiplas responsabilidades coordenadas.

## Transcrição

00:01

Bom, galera, e agora a gente tá chegando, entre astros, no nosso último tipo de prompt, mas não é que ele é o último, tá? É o último dessa lista que eu tô trazendo de importâncias, mas existem alguns outros tipos que nós vamos acabar vendo de uma forma ou de outra aí no curso, tá? Mas esse cara aqui, ele é bem interessante porque você consegue combinar

00:28

chainings, ou seja, encadeamentos de prompt. Então, a gente já entendeu do chain of thoughts, onde ele encadeia pensamentos. Agora, o prompt chaining, basicamente, o que ele faz é ele pega tarefas que devem ser executadas de forma sequencial,

00:50

onde a saída de uma é entrada na outra. Imagina o porquê você tem o lang chain. Qual você acha que é o grande diferencial do lang chain, por exemplo, que a gente está usando? Exatamente para isso. Então, vamos imaginar, eu quero converter um texto

01:05

e traduzir e resumir. Eu quero gerar um esquema, pegar os endpoints e gerar o código. Eu quero analisar o login, o parsing, classificar e a resposta. Eu quero criar um fluxo de agente com passo a passo definido. Eu quero organizar um raciocínio completo dentro de uma pipeline. Limitação, latência, porque você tem múltiplas etapas. Você propaga erro de uma etapa para outra. Então, você pode gerar um erro em cima de outro, em cima de outro. Aumenta custo de token. Depende de parsing correto. Se uma IA

01:32

mandar o resultado de um jeito pra outra que está esperando o resultado de outro jeito, a gente pode ter problema. Então, você tem que conseguir garantir saídas em padrões. E você tem complexidade de orquestração, porque vai virando um pipeline ali pra gente, tá? Mas ele é muito interessante e eu vou mostrar aqui pra vocês como é que esse cara aqui funciona, tá? Então, vamos lá aqui no nosso prompt chaining, aqui, pra gente olhar esse cara aqui. Vamos apagar.

02:00

e vamos olhar como esse cara funciona. Então, o seguinte, aqui é um pouco de lang chain, mas nada tão difícil de você compreender o que está sendo feito. Então, a gente vai criar primeiro um chain, ou seja, uma linha de encadeamento. Então, eu criei aqui, para deixar mais legal o nosso exemplo,

02:23

Três opções de modelo para a gente trabalhar. Um com o 3.5 Turbo, o modelo 2 com o GPT-5 Mini e o 3 com o GPT-4O Mini aqui para mim. E coloquei temperatura zero mesmo para evitar criatividades. Então, o que acontece aqui? Primeiro encadeamento. O primeiro encadeamento que a gente vai fazer

02:48

que a gente tem que trabalhar. Então, eu tenho que especificar especificação para um esquema. Então, aqui eu tenho um prompt onde eu vou colocar. Você é um back-end senior, siga as especificações do produto, extraia um JSON mínimo,

03:06

com o esquema baseado nos campos e nos tipos, e retorne somente o JSON sem comentário. Escreva todo o código usando em Markdown. E aí, eu passei a especificação, e aqui é uma variável que vai ser injetada.

03:23

Depois que ele fizer isso, perceba que aqui eu tenho um pipe. Um pipe, ou seja, eu estou pegando a saída desse cara, jogando pra minha LLM1, que vai ser com GPT 3.5, e vou converter isso numa string de parser pra ele poder ser entrada de outro canal.

03:43

Por que eu estou colocando o spec aqui? Porque nessa especificação é aqui onde eu vou passar a entrada, que vai ser dinâmica, onde eu vou pegar os campos e ele vai transformar em JSON pra mim. Então, aqui é o nosso primeiro passo do nosso primeiro encadeamento. Então, a gente vai ter encadeamento do encadeamento. Eu tenho um segundo passo aqui.

04:05

que é as rotas. Então, eu tenho, você é um Go developer, baseado no esquema que está sendo abaixo, desenhe as rotas REST, de uma forma idiomática com Go, com handlers para um CRUD.

04:23

Seja simples, seja conciso, production-oriented, mostre os code snippets para a gente. Escreva tudo usando markdown com codeblocks, para não ter problema. E aqui eu estou pegando o esquema do JSON, que está vindo da minha primeira etapa, que está saindo daqui.

04:42

E aqui ele está pegando o JSON. Mas esse cara agora, eu estou pedindo para essa parte ser usando o LLM2, que é o GPT-5 mini. Por quê? Porque esse código...

04:54

ele precisa ser bem feito. Então, eu quero pegar um modelo melhor para gerar o código em Go. Mas, o GPT-3.5 Turbo é um modelo mais ruizinho, mas ele consegue pegar campus e transformar em JSON, tá? E não estou falando em custo, tá? Porque, se eu não me engano, o GPT-5 já é mais barato que o GPT-3.5 Turbo, tá? Mas, independente disso, estou pegando um modelo mais fraco para fazer tarefas mais simples, modelo mais inteligente para fazer tarefas

05:23

mais complexas, tá? E depois a gente tem a terceira parte, né? Agora a gente precisa da API de produto. Então, ah não, terceira parte não, aqui o esquema dois

05:37

A gente tem, ele validou. Ah, beleza. E aqui tem, né? Você é um desenvolvedor pragmático, escreva numa single line conventional um commit, sumarizando a API e o esquema de rotas. Basicamente, eu estou pedindo para ele escrever a mensagem de commit aqui para mim, tá? Numa single line.

05:59

usando o Conventional Commits aqui para mim. Então, o ponto principal é, eu vou passar uma lista de especificação, olha a minha especificação. Nós temos uma API, a gente precisa de uma API de produto. Campus, id, uuid, name, string, required, description, string, price, float, maior que zero, stock, int, maior que zero. A gente tem que suportar paginação, criação, get, bind, update, delete.

06:28

Então, essa é a especificação. Agora, sim, vamos falar do prompt chaining itself. Basicamente, eu tenho três chains aqui, e cada chain desse tem o seu subchain, basicamente é isso. Então, eu vou pegar o meu esquema JSON e vou passar a minha especificação de texto. Esse esquema JSON vai retornar para mim o quê? O JSON. Aí, o que eu vou fazer? Eu vou pegar a

06:57

Então eu vou pegar o Json que foi gerado por esse cara aqui e jogar ele aqui.

07:04

E eu vou pegar agora a mensagem de commit que vem desse esquema JSON e vou gerar aqui, inclusive com as rotas. É basicamente isso que eu estou fazendo, beleza? E cada parte dessa eu estou usando um modelo diferente aqui pra mim. E aqui eu vou ter o resultado que eu estou pedindo aqui pra ele na minha especificação. Então a minha especificação agora que eu pedi vai ser o seguinte, tá?

07:30

a Prompt Chain Result, o esquema gerado pelo GPT-3.5 Turbo, e aqui é o esquema gerado, a rota e os handlers gerados pelo GPT-5 e a mensagem de commit e mostrando os modelos do pipeline.

07:46

Para que a gente não fique no terminal com uma mensagem muito grande, porque é muita coisa, o que eu fiz? Eu basicamente criei um arquivo e estou gravando esse resultado final, esse result content, dentro de um arquivo markdown.

08:02

Por isso que toda hora eu pedia para ele escrever em Markdown. E eu coloquei resultado salvo em promptChainingResult.md. Então, somente para você entender de forma geral, a saída de um ponto é a entrada do outro. Saída de um ponto, entrada no outro. E é legal que eu posso também usar diferentes modelos para cada diferente tipo de necessidade. Então, isso é promptChaining. Vamos executar esse cara aqui. Python 1 e esse cara é promptChaining. Então, eu vou rodar esse cara aqui.

08:32

Ele vai demorar um pouco mais porque ele faz três chamadas para três modelos diferentes. Basicamente é isso. E o modelo do GPT-5 é Reasoning, então ele vai demorar ainda mais para processar. Então, a gente tem esse ponto aí, então ele vai demorar um pouquinho aí para a gente.

08:49

Prontinho, galera, ele gerou. E só pra você saber, eu pausei o vídeo. Então, parece que foi mais rápido do que foi, mas ele demorou um pouquinho sim, só pra você saber. Então, vamos ver como é que saiu o arquivo gerado. Agora é uma surpresa, né? promptChainingResult.md E agora, aqui, eu vou pedir pra eu visualizar esse cara como um markdown. Então, vamos lá. Visualizar esse cara como um markdown.

09:15

e ver como é que ele gerou o resultado aqui pra mim. Deixa eu fechar esse cara aqui, deixar só o markdown que ele gerou, e vou tentar diminuir um pouco o zoom pra gente ver, galera. Então, o Prompt Chain Result, esquema, gerado pelo GPT 3.5 Turbo. Então, aqui ele gerou pra mim o meu JSON.

09:33

do jeito que eu estava querendo, baseado naquelas especificações. Aí, Roots e Handlers. Então, aqui está o resultado conciso de um CRUD REST idiomático usando o Go e etc.

09:52

Então, aqui ele dá uma justificativa falando que isso aqui é para copiar e colar num código main.go que já deve estar funcionando, tá? E se quiser trabalhar com banco de dados é substituir porque está em memória. Então, aqui ele trouxe o meu código go,

10:07

E, em tese, fez todo o meu CRUD ali e ele trabalhou com dados em memória mesmo. Olha só que interessante! Daí criou os handlers, criou para criar o JSON... Cara, ele gerou realmente o código, não sei se está funcionando, não vou copiar e colar para ver se funcionou, mas o fato é que ele pegou todo esse código, tá?

10:28

e gerou um resumo, inclusive, aqui para mim. Resumo das rotas, notas, etc. E aqui, por último, commit, gerado pelo GPT-4 Mini. E daí, como é convencional o commit, e como é uma feature, ele colocou feature do tipo API, implemente crude operations for products with validation pagination support.

10:49

E aqui eu tenho o resultado do pipeline, né? Como que foi o cada passo aqui pra gente. Então perceba, galera, isso aí é o famoso prompt chaining, tá? Ou seja, você tem diversos prompts pra cada etapa separada que ela entra num formato de um pipeline.

11:06

Então, isso aqui é prompt chaining, é bastante usado, muito usado. Quando você está trabalhando com agentes e você tem patterns, por exemplo, de agentes de delegation, um agente delega algo para outro, indiretamente acaba sendo uma espécie de um prompt chaining, porque ele está delegando a saída de um lado para a entrada do outro. Então, tem muito conceito e patterns que a gente acaba utilizando quando a gente cria as agentes,

11:34

e que tem tudo a ver com os tipos de prompts que a gente está aprendendo, tá? Então, eu acho que isso aí é uma das coisas mais importantes. Você ter clareza dos tipos de prompts que existem, e todas as vezes agora que você conseguir ler um determinado prompt, você consiga saber que existem formas melhores que você pode extrair resultados ali.

## Resumo IA

**Abreviações**
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)
- **JSON** — *JavaScript Object Notation*
- **REST** — *Representational State Transfer*
- **CRUD** — *Create, Read, Update, Delete*
- **Go** — linguagem de programação Go
- **Markdown** — linguagem de marcação Markdown
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)
- **CRUD operations** — operações de criar, ler, atualizar e deletar
- **Conventional Commits** — padrão convencional para mensagens de commit

**Resumo**
A aula apresentou o conceito de **prompt chaining**, isto é, a organização de uma tarefa grande como uma sequência de etapas especializadas, em que a saída de uma etapa vira a entrada da próxima. O instrutor explicou que essa abordagem é útil quando uma única chamada ao modelo concentra responsabilidades demais, como interpretar requisitos, estruturar dados, gerar código e sintetizar um resultado final. Em vez de pedir tudo de uma vez, o fluxo separa a extração de esquema, a geração de rotas/código e a síntese em mensagem de commit, permitindo mais controle sobre a orquestração e sobre o tipo de modelo usado em cada momento.

O fluxo mostrado no exemplo começa com uma especificação de produto em linguagem natural, contendo campos como id, name, description, price e stock, além de restrições de obrigatoriedade e validação. A primeira etapa transforma esse texto em um **JSON mínimo**, com saída restrita ao formato esperado, para reduzir ambiguidades e facilitar o parsing. Em seguida, esse JSON passa a ser o contexto da segunda etapa, que gera rotas REST idiomáticas em Go, com handlers para CRUD e saída em Markdown com code blocks. A terceira etapa não cria novo código: ela resume o pipeline em uma mensagem de commit no padrão **Conventional Commits**, condensando o que foi produzido em uma forma curta e padronizada.

O instrutor destacou que cada etapa do pipeline é montada com um contrato explícito de entrada e saída, usando a composição do tipo **prompt → modelo → parsing → próxima etapa**. Também mostrou que é possível combinar modelos diferentes conforme a complexidade da tarefa: um modelo mais simples para estruturar dados e um modelo mais forte para gerar código de melhor qualidade. A execução final grava o resultado em um arquivo Markdown, como `promptChainingResult.md`, para evitar excesso de texto no terminal e transformar a saída em um artefato consultável e versionável. Por fim, o instrutor relacionou essa ideia com agentes e delegação entre agentes, explicando que esse tipo de encadeamento aparece com frequência em arquiteturas com múltiplas responsabilidades coordenadas.

**Pontos de atenção**
- Cada etapa precisa respeitar exatamente o formato esperado pela próxima; pequenas quebras de formato podem contaminar todo o pipeline.
- Saídas com texto extra, comentários ou Markdown inesperado podem quebrar o parsing e gerar erro nas etapas seguintes.
- O uso de parsers e restrições explícitas de formato não é opcional; faz parte da implementação do fluxo.
- O encadeamento aumenta latência, porque cada etapa adiciona uma nova chamada ao modelo e nova espera de rede.
- O pipeline também aumenta o consumo total de tokens, mesmo que cada prompt isolado seja curto.
- Um erro inicial no esquema pode ser propagado para geração de código e síntese final, dificultando a detecção do problema.
- A orquestração fica mais complexa conforme aumentam as etapas; é preciso manter o fluxo bem definido e depurável.
- Faz sentido usar modelos diferentes para tarefas diferentes: tarefas mecânicas podem usar modelos mais simples, enquanto tarefas de maior qualidade exigem modelos mais fortes.
- Quando a saída é volumosa, gravá-la em arquivo Markdown é uma boa prática para leitura, revisão e reaproveitamento.
- Prompt chaining vale mais quando a decomposição traz ganho real de qualidade, automação ou auditabilidade do que o overhead adicionado.