Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16863)

## Resumo da aula

A primeira execução de evaluation conecta quatro peças em sequência: dataset já enviado ao LangSmith, prompt carregado do arquivo, chamada ao modelo e evaluators aplicados sobre cada saída. O experimento nasce quando o prompt é executado sobre todos os exemplos do dataset e cada resposta recebe uma ou mais avaliações. Retomando o cenário de revisão de código, o objetivo aqui não é medir qualidade semântica profunda, mas verificar se a saída respeita o contrato estrutural exigido pela aplicação. Isso transforma um teste manual de “parece certo” em um experimento rastreável dentro da ferramenta.

O upload apenas publica o conjunto de exemplos locais para que eles possam ser usados em execuções reproduzíveis no LangSmith. Depois dessa etapa, a interface passa a mostrar o dataset e, separadamente, os experimentos associados a ele; se nada foi executado ainda, a área de experimentos permanece vazia. Essa separação importa porque dataset é base de casos, enquanto experimento é uma execução concreta sobre essa base. O fluxo correto é sempre subir ou atualizar os exemplos antes de rodar a avaliação.

O prompt foi externalizado em YAML e recebe a variável code, que é preenchida com o conteúdo vindo do dataset. Esse formato ajuda a manter instrução, placeholders e contrato de saída separados do código Python, o que facilita versionamento e comparação entre variações de prompt. Aqui, a instrução força o modelo a atuar como revisor de código e responder apenas em JSON com campos como findings, type, description, criticidade e summary. A vantagem prática é que o prompt vira um artefato editável e testável sem acoplar a lógica de avaliação ao texto da instrução.

A chamada ao modelo usa o SDK da OpenAI com um wrap para manter tracing no LangSmith, evitando dependência forte de abstrações do LangChain. Essa escolha reduz acoplamento e tende a preservar compatibilidade ao longo do tempo, porque a execução continua próxima da API base do provedor. O modelo configurado com temperatura zero privilegia estabilidade de saída, o que é desejável quando o foco da avaliação é conformidade de formato. Em avaliações estruturais, mais determinismo geralmente produz sinais mais confiáveis do que criatividade.

A etapa de prepareJSONData organiza o que o evaluator built-in precisa receber para validar a saída gerada. Nesse caso, o output de referência pode ficar vazio porque JSON validity não depende de ground truth semântico; basta inspecionar a resposta produzida. Já prepareSchemaData prepara os dados para a validação do schema e pode incluir reference quando a função customizada precisar acessar outputs esperados ou metadados do exemplo. A preparação existe para adaptar o formato bruto da execução ao contrato esperado por cada evaluator.

JsonEvalLangChainStringEvaluator é usado aqui como evaluator pronto para checar se a resposta é um JSON válido. Ele não verifica se os campos corretos existem nem se a estrutura está de acordo com o contrato da aplicação; ele apenas confirma se a string pode ser interpretada como JSON bem formado. Essa distinção é importante porque um JSON pode ser sintaticamente válido e ainda assim ser inútil para consumo por código. Por isso, JSON validity costuma ser a primeira barreira, não a última.

validateJSONSchema adiciona a segunda barreira: além de ser JSON válido, a resposta precisa obedecer ao schema esperado. A função tenta interpretar a saída, aplica a validação estrutural e retorna um resultado com score e value, diferenciando erro de parsing de erro de schema. Quando o schema bate, o score é 1; quando o JSON é inválido ou a estrutura não corresponde ao contrato, o score é 0 com uma justificativa explícita. Esse evaluator customizado existe porque o contrato da aplicação raramente cabe integralmente em um validador genérico pronto.

A chamada de evaluate recebe o prompt, o nome do dataset e uma lista de evaluators, permitindo combinar validadores prontos e funções customizadas no mesmo experimento. Isso produz duas leituras complementares sobre cada saída: uma para validade sintática do JSON e outra para aderência ao schema definido pela equipe. A combinação é superior a usar apenas um dos lados, porque separa falha de serialização de falha de contrato estrutural. Em engenharia de prompts, essa decomposição ajuda a localizar rapidamente onde o output degrada.

Durante a execução, o LangSmith já exibe resultados em tempo real, o que permite acompanhar progresso e inspecionar falhas sem esperar o lote inteiro terminar. Ao final, cada evaluator aparece como uma métrica separada no experimento, com nomes como json validity e validateJSONSchema. Quando todos os casos recebem score 1, o prompt passou tanto na validade do JSON quanto na conformidade com o schema. Esse checkpoint confirma que o cenário de revisão de código já está operacionalmente consumível por software, não apenas legível para humanos.

Usar API diretamente em vez de depender da interface evita esconder detalhes importantes do fluxo de evaluation, como preparação de dados, retorno de score e composição de evaluators. A armadilha mais comum é assumir que JSON válido já resolve o problema; na prática, muitos outputs passam no parser e falham no contrato esperado pela aplicação. Outra fonte de erro é misturar criatividade alta com avaliação estrutural, o que aumenta variação desnecessária e dificulta reproduzir resultados. Para troubleshooting, a primeira inspeção deve separar três causas: resposta não parseável, resposta parseável com schema errado e resposta correta estruturalmente.

## Transcrição

00:01

Bom, pessoal, então vamos nos nossos exemplos aqui, tá? Então, só para você entender uma coisa, é o seguinte, eu estou utilizando recursos bem básicos do lang chain, inclusive para evitar problemas de compatibilidade ou qualquer coisa desse tipo, mas, de forma geral, a ideia principal é a gente fazer testes e entender esse ponto aqui.

00:21

Então é o seguinte, a gente vai trabalhar com o LangSmith, então a gente tem algumas bibliotecas e pacotes aqui em Python com LangSmith, a gente está trabalhando também com OpenAI. Se você perceber esse exemplo, eu estou usando alguma coisa do LangChain, mas, de forma geral, eu estou tentando deixar ele um pouco mais não tão amarrado no LangChain, aqui nesse aspecto, para tentar manter a compatibilidade um pouco maior ao longo do tempo, tá? Bom,

00:50

Mas, de forma geral, aqui nesses aspectos, o que você vai perceber que a gente tem em comum? Que eu tenho um nome do meu dataset, que é EvaluationBasicDataset. Esse EvaluationBasicDataset, se a gente for olhar, esse aqui é o nosso dataset.json, onde eu tenho meus exemplos aqui.

01:06

E eu tenho um arquivo chamado de UploadDataset. Basicamente, o que esse cara faz, ele vai ler o meu JSON, vai iterar e vai subir lá no LangSmith. É basicamente isso, tá pessoal? Não vou nem ficar gastando o nosso tempo aqui no código, depois você tem acesso a esse código fonte aí também. Beleza? Então, o que acontece? Primeira coisa que eu vou fazer, eu vou pedir aqui para ele fazer o upload do meu dataset.

01:33

Então, quando eu pedir para ele fazer o upload, ele vai subir esse dataset inteiro lá no Langsmith, na plataforma. E é isso que eu quero mostrar aqui para você, só esperar ele terminar de executar. Então, rodou aqui 18 exemplos, e agora eu vou aqui na plataforma da Langsmith.

01:48

No momento que eu estou rodando esse exemplo, o Langsmith está desse jeito, com essas opções, com essa cor e etc., com esse menu. Pode ser que, no momento que você esteja vendo esse vídeo, ele esteja diferente, que ele possa ser amarelo e vermelho e etc., mas eu acredito que os conceitos, de forma geral, são os mesmos. Então, se você perceber agora aqui, eu estou no menu chamado Datasets e Experiments. E o que acontece aqui nesse aspecto?

02:17

Você vai perceber que ele está listando aqui para mim o dataset e ele vai mostrar aqui algo que a gente chama de experimentos. Ou seja, experimentos é quando você realmente faz uma avaliação baseada naquele dataset. Então, essa que é a ideia principal. Então, se eu clicar aqui no nome do dataset, você vai ver que eu tenho os meus exemplos aqui. Então, essa que é a ideia principal. E se eu clicar aqui, você vai ver que eu tenho os meus experimentos e eu não tenho nenhum experimento.

02:47

Ou seja, porque eu não executei nada. E se você verificar aqui também, eu tenho algo chamado Evaluators, porque o Langsmith me permite criar um Evaluator usando os templates deles, as coisas deles, mas eu não queria que os nossos exemplos aqui e tudo que a gente aprendesse fosse algo tão mágico por trás do Langsmith. Então, por isso que, ao invés de a gente ficar clicando na plataforma o tempo inteiro, eu resolvi fazer tudo com chamadas de API,

03:14

para que a gente consiga entender mais o que está por trás disso e, obviamente, daí a gente vê o resultado dos experimentos por aqui, tá? Então, essa que é a nossa ideia principal aqui nesse momento, fechou? Então, aqui eu tenho os meus experimentos. No momento, eu não tenho nenhum experimento. Então, o que vai acontecer agora, galera? Eu vou aqui no meu...

03:37

arquivo que eu tô querendo, que eu tô trabalhando, e se você perceber, você vai ver que todos esses dez exemplos que eu tenho aqui, eles seguem exatamente a mesma estrutura. É como se o código praticamente fosse repetido, mas eu queria, eu preferi separar em vários exemplos pra ficar mais fácil e mais didático aqui pra você, tá?

03:57

Bom, a primeira coisa que a gente tem que se ligar é que ele está importando um prompt, e eu estou usando o prompt aqui no formato de YAML. Eu gosto bastante de trabalhar dessa forma. Então, se você olhar, é chamado Format Underline Evolve. Então, se você olhar aqui, Format Underline Evolve, você vai ver que eu tenho o meu prompt, ou seja, a minha variável é code, o meu template é, você é um revisor de código que sempre responde em JSON, revise o código abaixo, descreva os problemas, responda apenas o JSON no formato. E aqui, eu trouxe o quê?

04:27

o formato findings, type, description e o nível de... não é severidade, mas eu acredito que você entendeu, o nível de...

04:40

Eu já lembro a palavra, tá? Mas eu acho que você entendeu, né? O quão severo, o quão crítico, o nível de criticidade a gente tem. E o resumo final aqui. E aqui eu tenho o código e o code que tem ali do nosso dataset, no final das contas, tá? Então, essa que é a nossa ideia que a gente tem aqui. Maravilha? E como é que funciona esse meu cara? Uma vez que eu carreguei esse prompt, o que eu vou fazer?

05:04

Eu estou formatando agora o meu prompt, ou seja, estou pegando o meu prompt, estou pegando o código que veio dele ali, ou seja, a minha variável, o código que tem ali dele.

05:15

E o que eu estou fazendo é, eu estou fazendo com que o meu SDK da OpenAI, perceba que eu não estou usando o SDK da LengChain por trás, na realidade eu estou fazendo até um wrap da OpenAI com a ferramenta do LengSmith, para ele manter o tracing disso aí, tá? Mas perceba que eu não estou utilizando o LengChain aqui que cria um LLM, tá? Eu estou tentando deixar isso mais vanilla aqui nesse caso para a gente, tá?

05:42

E aqui, no meu caso, eu coloquei as mensagens, que é roleUser, o content, eu tenho o meu prompt, o modelo, coloquei o GPT-4 mini, a gente sabe, já tem GPT-5 e tudo mais, mas eu estou colocando um que não tem advanced reasoning, ele acaba sendo rápido aqui para executar, escolhi um, coloquei temperatura zero, inclusive, para deixar ele zerado criativamente ali para a gente, para ele ter a resposta mais

06:10

ali pra gente. E o retorno que eu dou é um output, legal? Baseado no conteúdo da minha mensagem. Basicamente, ele pega a última mensagem que eu tenho, o conteúdo, como output ali pra mim. Beleza? Aqui, tá? Somente pra você entender o que eu fiz, também é o seguinte. Eu tenho duas funções. Uma é chamada prepareJSONData.

06:35

que eu tenho um prediction, onde ele vai executar para pegar o resultado, e você vai ver que eu tenho um output que, nesse caso aqui, está em branco. E o porquê que esse cara aqui, nesse caso, está em branco? Porque, dependendo da situação, a gente não vai ter grounding, a gente não vai ter ground truth, ou seja, eu não vou ter nenhuma referência para que aquilo seja executado, ou seja, eu não estou passando um exemplo de como eu espero. Basicamente é isso.

07:03

E um outro camarada que eu tenho aqui também é prepare-schema-data. Por quê? Porque eu vou querer também verificar o esquema do JSON que está sendo retornado ali pra mim. Então, um eu posso ter exemplo e não. Então, somente pra você entender como é que funciona. Esse cara aqui, se você olhar, ele já tem reference, onde ele tem os outputs aqui pra mim. Então, um tem e o outro não tem essas informações.

07:29

E aí, o que acontece é o seguinte, a primeira coisa que eu fiz é eu criei um JsonEvalLangChainStringEvaluator. É um cara pronto, tá? E eu falo que o tipo de cara que eu quero trabalhar é a validade do meu Json. E pra isso, eu tô, o prepareData, eu tô passando essa minha função.

07:49

que pega o meu prediction e vai rodar esse cara, vai fazer execução pra pegar o resultado. Ou seja, é basicamente isso como funciona. Esse cara aqui usa uma função que vai executar um evaluation, por isso que eu tenho o meu run aqui, o cara que vai fazer a execução.

08:05

para trabalhar com isso. Então, eu tenho um runner que vai ser executado no final das contas. Outro ponto, galera, eu não queria que vocês ficassem, inclusive, muito presos a código. O nosso ponto principal é entender os formatos de evaluation e não você também ficar entendendo linha por linha, detalhe por detalhe. Mas, como esses exemplos são muito parecidos, eu estou gastando um tempo a mais nesse nosso primeiro exemplo para que você consiga entender e não ficar viajando no código.

08:31

Aqui, eu criei de uma forma linda, tá? Eu criei o esquema de como eu quero o JSON o resultado. Eu falei que é um objeto, find, type, array, deixei tudo organizadinho da forma como eu quero, pra garantir que eu consiga fazer esse tipo de verificação. Então, aqui, eu tenho o meu

08:51

minha função chamada validateJSONSchema, onde eu tenho meu runner e eu tenho o exemplo caso eu queira trabalhar aqui. Maravilha? Então, como é que vai funcionar no final das contas? Quando essa função for chamada, ele vai fazer a execução, vai carregar os outputs, vai cair nessa minha função que faz a validação do meu schema, tá?

09:15

E aí, se retornou, se o esquema realmente bateu, o score vai ser 1 e eu vou colocar a value de esquema. Caso tenha algum erro de JSON, de codificação, ou seja, formatação do meu JSON, o score é 0 e eu estou falando que o JSON é inválido e o erro.

09:31

E se o meu esquema tiver inválido, eu vou falar que é zero, e eu vou falar o porquê que o esquema aqui é inválido. Então, se você olhar aqui, essa função, no final das contas, vai ser a responsável para fazer o quê? Para dizer o nosso resultado, o score que a gente vai trabalhar lá no nosso Langsmith. Então, como que eu faço a minha avaliação?

09:56

Então eu dou um EVALUATE, passo o meu PROMPT, passei o nome do meu DATASET e falei quais são os meus EVALUATORS. Quais são os meus EVALUATORS então? Eu tenho um que é o JSON EVOL, que ele já vem pronto aqui pra mim.

10:12

É um cara pronto que existe ali pra mim. Então, esse é o meu primeiro evaluator. Lembra que a gente tem código que faz evaluação, a gente tem o LLM, as Judge. Então, nesse caso, é código. Ou seja, ele tá batendo ali numa função, mas isso aqui é built-in. Ou seja, já existe por padrão no langsmith.

10:30

O validateJSONSchema, o que eu fiz é, eu meio que customizei nesse formato. Então, ao invés de ele usar um formato pronto, eu criei o meu schema, eu customizei a minha função, e eu estou falando que ela vai fazer a avaliação. Ou seja, quando ele executar,

10:50

Essa função vai ser chamada, e essa função vai dar a nota, e essa função vai retornar isso lá pro Langsmith. E aqui, o quanto que ele pode fazer de uma vez, e eu pedi pra ele criar um prefixo nesse exemplo, pra eu conseguir ter o resultado quando eu olhar ali no Langsmith.

11:10

Então, basicamente, essa é a ideia. Então, somente para resumir, e eu estou sendo bem repetitivo, eu sei disso, mas tudo que a gente está vendo aqui, a gente vai ver nos outros exemplos. Por isso que eu estou sendo bem repetitivo para garantir que todo mundo entendeu. Isso aqui é built-in, a gente já tem no Langsmith. Legal? E esse cara aqui, ele tem um cara que pode ser rodado como um runner, ou seja, é executado. E para fazer isso, ele tem um prepareData que ele chamou aqui para mim.

11:40

Beleza? E eu tenho o cara que valida um esquema de JSON ali também pra mim. Fechou? Então, quando eu executo esse Evaluate, ele pega esses dois Evaluators, ele vai fazer essas duas análises baseadas nesse dataset, que a gente já fez o upload, e aí a gente vai ver o resultado.

11:59

Então vamos executar finalmente esse cara aqui. Então vamos lá, python1-basic1-formatEval. Então aqui eu estou fazendo a evaluação de formato. Então eu vou rodar isso aqui.

12:14

E agora, a gente vai esperar ele fazer a iteração por todos os itens dos datasets. Pode ver que ele está aqui 4, 5, 7, e ele vai, provavelmente, até 18 para mim. Porém, você vai perceber que se eu já for na plataforma do Langsmith,

12:32

Olha só o que ele já está trazendo aqui pra mim, galera. Enquanto ele está rodando, ele já vai mostrando em tempo real pra mim como é que estão sendo os resultados aqui pra mim. E deixa eu ver se ele já acabou. Acabou já aqui. Então, se você perceber aqui, olha só. Ele já falou split space, ou seja, já teve somente esse cara. E agora, se você olhar aqui, eu tenho, no final das contas, a minha validade, o quanto que o meu JSON está válido,

13:00

e o meu esquema do meu JSON. Por que eu tenho esses dois caras? Porque foram esses dois caras que eu coloquei que eu queria fazer a evaluação. Ou seja, se eu olhar aqui, tá? E você olhar qual é o nome que ele tá usando? JSON...

13:17

de validade aqui. É o nome desse cara que ele tá trabalhando. E o outro que eu tenho aqui é o validateJsonSchema, que é exatamente esse cara que ele tá trazendo aqui pra mim de resultado, tá? Então, tá aqui o resultado do meu experimento e, no final das contas, todos bateram 1.

13:36

Ou seja, todos os JSONs aqui nesse nosso caso, eles foram válidos e o meu experimento foi bom. Conforme eu posso ir rodando outros experimentos, ele vai, cada vez que eu rodo isso aqui, quantas repetições, ele vai mostrando, inclusive, ou até mesmo com...

13:55

com outros formatos, ele vai gerando meio que o gráfico, você vai ver ao longo do tempo, e ele vai gerando vários gráficos comparativos ali com o que você rodou, tá? Mas, a ideia principal do nosso primeiro cara foi essa, a gente conseguiu fazer essa nossa avaliação. Fechou?

## Resumo IA

**Abreviações**
- **API** — Application Programming Interface
- **JSON** — JavaScript Object Notation
- **LLM** — Large Language Model
- **SDK** — Software Development Kit
- **YAML** — YAML Ain't Markup Language
- **OpenAI** — plataforma/provedor de modelos de IA da OpenAI
- **LangChain** — framework para orquestração de aplicações com LLMs
- **LangSmith** — plataforma de tracing, datasets e avaliação de aplicações com LLMs

**Resumo**
A aula apresentou o fluxo básico de evaluation no LangSmith, conectando quatro elementos principais: o dataset já carregado na plataforma, o prompt externalizado em YAML, a chamada ao modelo via SDK da OpenAI com tracing e os evaluators aplicados a cada saída gerada. O objetivo do instrutor foi mostrar como transformar uma checagem manual de “parece certo” em um experimento reproduzível e rastreável, focado não em semântica profunda, mas na conformidade estrutural da resposta com o contrato esperado pela aplicação.

Primeiro, foi explicado o upload do dataset local para o LangSmith, separando claramente a base de exemplos do experimento executado sobre ela. Em seguida, o prompt foi carregado de um arquivo YAML, com variável `code`, instrução para agir como revisor de código e exigência de resposta apenas em JSON com campos específicos, como `findings`, `type`, `description`, criticidade e `summary`. O instrutor destacou a vantagem de manter prompt, placeholders e contrato de saída fora do código Python, facilitando versionamento e comparação entre variações.

Depois, a execução do modelo foi feita de forma mais “vanilla”, usando diretamente o SDK da OpenAI com wrap para preservar o tracing no LangSmith, reduzindo o acoplamento com abstrações do LangChain. O modelo foi configurado com temperatura zero para aumentar a estabilidade da saída, já que o foco da avaliação era estrutural. Para alimentar os evaluators, foram preparadas duas estruturas de dados: uma para validação de JSON, sem necessidade de ground truth, e outra para validação de schema, que pode incluir referência quando necessário.

Na etapa de avaliação, foi usado um evaluator pronto do LangSmith para verificar se a saída era um JSON válido, e também uma função customizada para validar se o JSON obedecia ao schema definido. O instrutor reforçou a diferença entre “JSON válido” e “JSON conforme o contrato”: o primeiro checa apenas sintaxe, enquanto o segundo confirma a estrutura esperada pela aplicação. Por fim, a função `evaluate` recebeu o prompt, o nome do dataset e a lista de evaluators, gerando um experimento com métricas separadas para validade de JSON e conformidade de schema, exibidas em tempo real no LangSmith.

**Pontos de atenção**
- Dataset e experimento são चीजas diferentes: o dataset é a base de exemplos; o experimento é a execução da avaliação sobre essa base.
- O upload do dataset deve acontecer antes da avaliação; sem isso, não há dados reproduzíveis para o experimento.
- Manter prompt em YAML ajuda no versionamento e na separação de responsabilidades entre texto de instrução e lógica de execução.
- Usar chamada direta ao SDK com tracing reduz acoplamento e facilita compatibilidade futura.
- Temperatura zero é preferível em avaliações estruturais, pois diminui variação desnecessária na saída.
- JSON válido não significa JSON correto para a aplicação; é preciso validar também o schema.
- Validar sintaxe e schema como etapas separadas ajuda a identificar rapidamente o tipo de falha.
- `prepareJSONData` e `prepareSchemaData` existem para adaptar a saída bruta ao formato esperado por cada evaluator.
- Evaluators built-in podem resolver verificações simples, mas contratos específicos geralmente exigem função customizada.
- O retorno do evaluator deve informar claramente `score` e motivo do erro ou da aprovação.
- Acompanhar o experimento em tempo real no LangSmith facilita troubleshooting durante a execução.
- Evitar depender excessivamente de abstrações “mágicas” da plataforma ajuda a entender o que realmente está sendo avaliado.
- Em troubleshooting, separar três causas: resposta não parseável, resposta parseável com schema errado e resposta correta estruturalmente.