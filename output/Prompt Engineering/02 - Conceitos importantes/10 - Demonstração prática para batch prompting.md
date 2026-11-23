Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16605)

## Resumo da aula

Retomando o cenário da aplicação, os logs do servidor deixam de ser apenas entradas isoladas e passam a alimentar um workflow com agentes: um recebe o log, outro classifica, outros refinam a issue e um agente final publica no GitHub. O ponto novo aqui não é a existência de múltiplos agentes, mas o impacto arquitetural de processar logs continuamente em alto volume. Quando o sistema trata cada log como uma conversa independente sem estratégia de agrupamento, o fluxo funciona, mas escala mal em custo e latência.

A implementação mais direta envia cada log recebido para a LLM assim que ele chega. Isso resolve o problema funcional: logs de health check encerram o fluxo cedo, enquanto logs de erro seguem para geração e revisão de issue. O problema é operacional: cada item dispara uma nova request com o mesmo conjunto de instruções, multiplicando overhead, repetição de prompt e tempo total de processamento.

Se vários logs forem inseridos na mesma sessão, a conversa passa a carregar o histórico anterior a cada nova análise. Como a sessão preserva mensagens passadas, cada log novo faz o modelo reprocessar conteúdo que já não é necessário para aquela decisão específica. Nesse caso, a janela de contexto deixa de ser apenas um limite técnico e vira uma fonte direta de desperdício de tokens.

Uma conversa por log elimina o acúmulo indevido de histórico, mas ainda mantém o custo de uma chamada por item. O redesenho mais eficiente cria uma nova sessão a cada X logs, não a cada evento individual. Esse corte por lote preserva isolamento suficiente para evitar crescimento descontrolado da conversa e, ao mesmo tempo, reduz a repetição estrutural do prompt.

O buffer é a estrutura que acumula logs até atingir um limiar, como 100 itens, e então dispara o processamento em lote. Ele existe para desacoplar a chegada contínua dos eventos da frequência de chamadas ao modelo. Esse desenho transforma um fluxo reativo item a item em uma operação controlada por volume, o que facilita previsibilidade de custo e melhor aproveitamento do batch prompting já definido anteriormente.

Cada log do lote precisa carregar um identificador próprio antes de ser enviado ao modelo. Esse ID permite mapear a resposta de volta ao item original e decidir qual ramo do workflow deve continuar: encerrar, abrir draft, revisar ou notificar. Sem esse identificador, o lote perde rastreabilidade e a arquitetura de agentes deixa de saber qual saída pertence a qual entrada.

A resposta em lote precisa vir em um formato que a aplicação consiga consumir sem ambiguidade, por isso JSON estruturado ou JSONL são escolhas naturais. O campo mínimo útil tende a ser algo como id, classificação do log e conteúdo necessário para a próxima etapa; qualquer excesso aumenta custo sem agregar valor operacional. Em lotes grandes, JSONL simplifica parsing incremental e reduz atrito quando cada linha representa um item independente.

Depois da classificação inicial, o próximo agente não precisa reinterpretar o lote inteiro; ele só consome os resultados já estruturados e encaminha cada item conforme sua categoria. Um log informativo encerra o fluxo imediatamente, enquanto um erro segue para draft, revisão, refinamento, criação de issue e notificação. A arquitetura de agentes fica mais previsível quando a primeira etapa devolve uma saída compacta e roteável, em vez de texto livre.

Mesmo após o batch inicial, pode ser útil abrir novas conversas nas etapas seguintes para impedir que JSONs anteriores contaminem o contexto das próximas decisões. Essa separação evita que o histórico do lote se acumule artificialmente em agentes posteriores, especialmente quando cada item passa a seguir caminhos diferentes. O ganho não é conceitual, mas operacional: menos contexto inútil sendo reenviado e menor risco de respostas influenciadas por itens vizinhos.

Um prompt longo demais pode conter papel do agente, regras, formato de saída e muitos exemplos, mas isso não o torna automaticamente melhor. Quando cada log precisa carregar esse bloco inteiro, o sistema paga repetidamente por instruções fixas para classificar algo simples, como distinguir health check de erro real. A avaliação correta não é “o prompt funciona?”, mas “qual é o menor prompt que preserva o mesmo comportamento com custo aceitável?”.

Exemplos ajudam a estabilizar comportamento, mas em excesso podem aumentar tokens e até confundir o modelo com variações desnecessárias. O critério técnico não é quantidade, e sim utilidade marginal: cada exemplo adicional precisa justificar seu custo. Se remover exemplos ou regras redundantes mantém a qualidade, o prompt anterior estava superdimensionado.

Se o prefixo do prompt permanece estável e não pode ser reduzido sem perda de qualidade, a combinação entre batch e prompt caching passa a fazer sentido. O batch reduz a multiplicação de chamadas; o cache reduz o reprocessamento do trecho fixo, conforme já discutido anteriormente. Ainda assim, cache só compensa quando há reutilização suficiente, porque criar e manter conteúdo cacheado também tem custo.

Não basta otimizar a entrada; a saída do modelo também precisa de limite explícito, como “responda com no máximo 100 tokens”. Em muitos providers, tokens de saída custam mais do que tokens de entrada, então uma resposta prolixa destrói parte da economia obtida no prompt. Restringir formato e tamanho da resposta é uma decisão de engenharia, não apenas de estilo.

Quando o lote tem tamanho conhecido e a saída máxima por item está controlada, o custo deixa de ser intuitivo e passa a ser estimável. Se o sistema processa 10 logs por chamada e cada item pode consumir até 100 tokens de saída, já existe um teto operacional para aquela etapa. Multiplicando isso pelo volume diário de logs, a aplicação consegue prever gasto, comparar arquiteturas e evitar surpresas financeiras no fim do mês.

Prompt Engineering não se limita a formular instruções corretas para o modelo; ele define como sessões, lotes, agentes, formato de saída e reaproveitamento de contexto serão organizados. Nesse cenário, um bom prompt é inseparável de uma boa arquitetura de execução. O resultado desejado é simultaneamente semântico e operacional: classificar corretamente, gastar menos, responder mais rápido e manter o workflow rastreável.

## Transcrição

00:01

Bom pessoal, vamos para um exemplo mais prático aqui para que você consiga entender essa parte de batching, porque ela é realmente muito importante mesmo. O lance é o seguinte, toda vez, vamos imaginar que eu estou fazendo um sistema, e esse meu sistema fica verificando se tem logs de erro no meu servidor.

00:26

Caso encontre um erro, ele vai abrir uma ishu no meu GitHub. Basicamente, é isso. Eu tenho um agente de A, ou vários agentes de A, que acabam trabalhando em conjunto para fazer essas detecções. Então, vamos imaginar que eu tenho o seguinte. Eu tenho esse log aqui.

00:49

Deixa eu diminuir o tamanho desse cara para ficar melhor para você conseguir ver. Eu tenho um log de erro de conexão com banco de dados, eu tenho um log

01:01

aqui pra mim, tá? De info, de health check, eu tenho um log de erro de SQL e assim por diante, tá? Então, o que pode acontecer aqui, pessoal? Vamos imaginar que eu vou trabalhar de uma forma, como se diz, de uma forma... de uma forma inocente. Então, como que eu trabalho de uma forma inocente? Eu vou pegar esse log aqui, tá?

01:31

e vou chegar no meu agente de AI. Então, eu tenho um sistema aqui apenas para te mostrar a versão inocente da coisa, tá?

01:38

Então, aqui tá, pessoal, só pra vocês saberem, eu tenho... essa é uma interface do ADK, que é o... é um agente, né? Um sistema, um developer kit de agentes da Google, tá? Muito bom, inclusive. E o que que acontece? Esse cara, ele verifica bugs, e se ele encontra algum bug, algum erro, ele cria uma issue no GitHub. Então, o que que eu vou fazer? Eu vou colar esse cara aqui, e que não é um erro. Então, o que que vai acontecer?

02:06

ele vai receber, tem um agente que recebe os logs, eu tenho um agente que analisa se isso aí é um bug, e esse agente, o que ele falou aqui pra mim? Ele falou que o log indicou que foi um health check de sucesso, logo, não foi encontrado nenhum bug, então o workflow está completo. Beleza? Então, isso aqui que ele fez. Por outro lado, eu posso chegar e pegar esse erro aqui de SQL, tá?

02:36

Então, nesse meu erro de SQL, eu vou colar aqui embaixo, tá? Espera aí, vamos colar. E vamos ver o que vai acontecer agora aqui comigo. Então, ele vai ter o LoggerReceiverAgent, esse cara vai analisar se isso é um bug. Aí, agora ele continuou, então ele vai fazer um draft de uma issue, aí eu tenho um agente que vai revisar esse draft,

03:05

e dar sugestões para melhoria. Aí eu tenho um agente que vai refinar esse draft para deixar certinho com as melhorias. Eu vou ter um agente que cria uma isha no GitHub, tá?

03:21

e eu tenho um agente que notifica o criador daquele código falando que ele encontrou um problema. E daí aqui, se eu clicar, eu tenho acesso a issue do GitHub. Então, está aqui, Missing Users Table, então ele fala que a aplicação está falhando por conta disso, a tecnologia que está sendo utilizada, a tabela é assim,

03:46

Está faltando essas sugestões de resolução, as consequências se não pode melhorar, e está falando que é um bug com alta prioridade. Então, isso aqui são agentes trabalhando em conjunto. Beleza?

04:02

Agora, o que tem de mais nessa minha solução, vamos dizer, inocente? Essa minha solução tem um problema, de forma geral, muito grave. E o que tem de grave nessa minha solução? É que, imagina que para cada log que eu receba,

04:24

eu faça uma chamada para a minha LLM. Imagina que eu recebi isso, daí recebi outro health check, recebi outro health check, e ele vai continuar fazendo esse processo o tempo inteiro. Então, aí a gente tem algumas coisas que são importantes que você consiga entender, tá? Uma coisa aqui, eu não quero mostrar meu cursor, uma coisa que eu quero que você entenda aqui nesse caso, aqui para essa parte de batch prompting.

04:52

Se toda vez você vai criar uma sessão, se você tem uma session, ou seja, você tem uma conversa, e eu pegar esses bugs, essas mensagens de log, e todas essas mensagens eu vou colocando uma a uma dentro da mesma sessão, qual é o problema que eu tenho aqui dentro? O problema que eu tenho é que para cada

05:18

log que vai entrando nessa conversa, eu vou chamar essa session barra conversa, o que vai acontecer? Ele vai acumular as mensagens anteriores, certo? Então ele vai usar mais tokens, porque ele vai estar reprocessando

05:34

inclusive mensagens que já aconteceram no passado, porque ele guarda o histórico da minha conversa, legal? Então, aí eu tenho o meu primeiro problema. Então, de forma geral, em tese, eu deveria ter uma conversa por log, porque senão ele vai usar o log antigo na janela de contexto e vai gastar mais tokens, tá? Então, aqui está a minha primeira coisa. Então, eu preciso, aqui pra mim, de uma

06:02

conversa ou sessão, por log.

06:08

Então, eu já evito que eu esteja processando, mandando informação desse cara, mas a IA vai ler todo o histórico novamente e vai usar isso como tokens, então eu estou pagando por isso. Uma conversa por log, isso aí já reduz bastante o meu problema. Agora, o grande ponto é que para cada log que eu mando de uma conversa, ele vai fazer o quê?

06:38

uma chamada por log. E toda vez que eu vou fazer uma chamada por log, o que acontece comigo? Eu estou usando prompts repetidos e fazendo múltiplas chamadas, o que vai fazer eu gastar mais e também vai fazer com que eu fique

07:07

mais lento, porque é uma new request que eu tenho que acabar trabalhando. Agora, o que seria o ideal aqui nesse meu caso? O meu ideal seria eu ter uma nova conversa por session, mas não é por log, a cada x logs. Então, o que eu faço? Ao invés de receber um log e já mandar, o que eu posso fazer? Eu posso pegar aqui, por exemplo,

07:38

um buffer de logs. E eu falo que quando ele atingir, por exemplo, 100 logs, o que ele vai fazer? Ele vai iniciar uma nova sessão. E ele vai mandar esses logs serem processados.

07:58

O que vai acontecer? Na hora que ele iniciar o processamento desses logs, a gente vai ter algumas coisas interessantes que vão acontecer. Deixa eu pegar esse log info que é mais simples e colocar aqui para você ver. Aqui nem preciso. Quando eu coloquei o log info aqui para mim, o que aconteceu no final das contas? Teve um agente que recebeu o log, um outro agente que analisou e viu que esse log não é de erro.

08:25

Então, esse log aqui, o processamento, ele já para aqui nesse momento. Quando eu botei um log de erro, o processamento continuou. Então, a primeira coisa que eu tenho que ter em mente é, ele inicia uma sessão, e aí eu vou ter o quê? Um workflow, né? E nesse workflow, o que vai acontecer? Eu preciso nomear, ter um ID para cada log, tá?

08:54

Porque se eu não tiver um ID de cada log, eu não consigo rastrear se esse log vai ter que continuar ou não. E depois eu tenho a mensagem, que é o log. E aqui no prompt, eu posso chegar e falar o seguinte, analise os logs abaixo e retorne em JSON

09:24

na seguinte estrutura. E depois eu posso falar que o JSON tem que ter um ID. Eu posso falar que o JSON tem que ter a mensagem do log ou o tipo do log. Quanto menor for isso aqui, menor o meu JSON, melhor. Por quê? Porque eu gasto menos tokens aqui para mim. Quando eu receber a resposta num monte de conjunto de JSON,

09:51

O meu próximo agente vai fazer o quê, no final das contas? Pegar todas essas respostas, né, e baseadas nessas respostas, partindo. Então, ele vai fazer... Os agentes ou o agente, ele vai seguir, né, com cada parte do sistema.

10:09

E, para cada workflow, eu trabalho de uma forma. Então, se for o log de info, vai acontecer isso. Se for erro, vai ser assim. Se for crítico, vai ser assado. Mas ele vai sempre processando tudo isso em batch para evitar, a cada momento, eu ficar trabalhando. E aí, nesses casos, eu posso...

10:28

No meu workflow, iniciar novas conversas para ele não pegar o conteúdo todo do JSON passado e utilizar como base para os JSON futuros. Então, esses tipos de coisa, galera, são importantes. E você vai começar a perceber que muito disso tem a ver como de arquitetura, ou seja, como que eu vou arquitetar a minha cadeia de agentes.

10:51

Mas também muito disso vai ter a ver como eu trabalho com os meus prompts, porque dependendo do meu prompt, esse meu prompt pode ser longo e custar muito caro.

11:02

Aqui, por exemplo, eu vou te dar um exemplo de um prompt desse sistema de logs que está extremamente grande. E esse prompt poderia ser reduzido, diminuído e também tratar todo esse processamento em batch, o que ele não está fazendo. Então, deixa eu mostrar aqui rapidinho para vocês um prompt desse agente que verifica

11:27

se algo é um bug ou não, tá? Então, basicamente, olha só o que ele fala aqui. Deixa eu aumentar um pouco mais a minha tela. Aqui está o prompt. Então, ele está falando, você é um bug analyzer, agent, expert em analisar logs do sistema para identificar e classificar bugs de software. Sua responsabilidade inclui isso, isso, isso, isso, aquilo. Importante, filtrar operações normais de logs que não são erros.

11:56

E daí eu coloquei regras críticas. Somente analise erros de verdade. Você tem que conseguir distinguir erros e bugs de operações normais de log. E retorne para o meu agente principal, que é o root agent, um JSON nesse formato aqui.

12:16

Ou seja, se é erro, qual é o tipo do log e o conteúdo do log? E aqui eu estou dando alguns exemplos. Por exemplo, uma chamada de sucesso para uma API. Então, ele vai trazer o timestamp, o level, o service, o message, o response time, status code e etc. Isso aqui é um exemplo de log, porque ele pode ter um log recebendo um log em JSON.

12:44

Aqui, ele pode ter outros tipos de log que venham em outros formatos. Então, perceba aqui que eu dei muitos exemplos para ele. Outro tipo de log. Logs no formato de uma linha, de operações normais. Então, o JSON que ele tem que responder é nesse formato aqui.

13:04

logs de warning, como que eu consigo identificar. Então, aqui tem diversas coisas, bastante. Galera, vocês conseguem perceber o tamanho desse prompt? A quantidade de coisa que tem aqui?

13:21

Agora, imagina um negócio, e aqui vai o log que vai ser embedado nesse prompt. Agora, galera, imagina para cada log eu ter que mandar todas essas instruções para ele fazer o processamento. Ou seja, para ele processar uma linha para verificar se algo é log ou não, ele tem que receber essa quantidade absurda de tokens aqui para mim. Então, com certeza, isso não é uma boa prática.

13:50

Não é uma boa prática porque, primeira coisa, eu posso testar outros prompts que deixem esse prompt inicial muito menor. Eu vou dar um exemplo bem simples. Somente de eu tirar essa linha, talvez o meu sistema rodasse da mesma forma.

14:10

Talvez, se eu tirar critical rule, only analyze true errors, eu poderia, por exemplo, retirar esse parágrafo e eu poderia testar, por exemplo, se o meu sistema iria conseguir ainda assim analisar os logs. Agora, outra coisa,

14:30

Será que eu preciso de tantos exemplos assim? Existem casos, galera, que se você dá muitos exemplos para IA, aí sim que a coisa pode gerar mais confusão para ela. Então, não necessariamente a maior quantidade de exemplos é necessariamente a forma mais eficaz. Agora, uma forma aqui que eu tenho absoluta certeza é que, com certeza, eu consigo, com prompt, muito, mas muito menor,

14:59

ter exatamente o mesmo resultado para fazer com que esse agente continue seguindo, identificar se é erro ou não e etc. Então, isso aqui, galera, é uma forma, né, obviamente eu detalhei, dei um monte de exemplo, para servir como um template de pontos que você tem que ter de atenção. Mas isso aqui, claramente, tá, é como não fazer um sistema de análise de logs.

15:25

principalmente se você for trabalhar log a log. Agora, tem algumas coisas que você pode trabalhar em conjunto que pode facilitar.

15:34

Por exemplo, vamos imaginar, no pior das hipóteses, que nós fôssemos usar exatamente isso. A gente não conseguiu melhorar esse prompt, os resultados não eram os mesmos, eu testei, não deu certo. O que eu poderia fazer aqui para pelo menos tentar ajudar? Primeira coisa, fazer esse prompt conseguir trabalhar em batch, e o segundo ponto,

16:00

Daqui pra cima, isso aqui é sempre igual, não é? O que eu posso fazer? Trabalhar com cash. E na hora que eu trabalho com cash, pelo menos eu tenho o desconto, tá? Então, isso aí é uma forma extremamente clara de como que um cash pode reduzir, se eu fosse trabalhar com Gemini, 75% a...

16:21

de custo, porque eu tenho esse prompt. Agora, obviamente, seria muito mais interessante eu ter mais desconto ainda, não tendo um prompt tão grande desse tamanho. E você também tem que conseguir analisar

16:38

se realmente esse prompt vai ser muito utilizado o tempo todo. Se ele não é um prompt que é utilizado o tempo todo, não compensa às vezes você pagar por cash, porque a primeira cashada que você vai dar, normalmente, ele tem um custo maior. Então, tudo vai depender do contexto que você está. Agora, o fato é, se você está trabalhando em batch,

17:01

você tem que tomar sempre muito cuidado. Existem algumas boas práticas que depois eu vou passar aqui para vocês. Por exemplo, retorne em JSON nesse formato e JSON-L para estar tudo na mesma linha. E fora isso, responda com no máximo, por exemplo, 100 tokens. Então, isso vai conseguir fazer com que o modelo trabalhe da melhor forma

17:30

com a menor quantidade de tokens de saída. Por quê? Porque você paga um valor de tokens de entrada, mas, normalmente, os tokens de saída, que é a resposta do modelo, são o que tem a maior cobrança, a maior taxa que você vai pagar para os providers. Então, você conseguindo controlar a quantidade de saída, a coisa vai ficar melhor, porque eu consigo fazer até contas matemáticas.

17:54

Por exemplo, se eu estou falando que ele vai processar de 10 em 10 e cada log vai ter no máximo 100 caracteres, então eu sei que para cada chamada eu vou gastar de saída pelo menos 1.000 tokens. Então, eu consigo fazer essas contas e dar uma estimativa baseada na quantidade de logs por dia que eu tenho quanto que eu vou gastar.

18:16

Então, isso são informações muito claras que você tem que levar em consideração, inclusive na parte de Prompt Engineer, porque, no final das contas, quem está criando o prompt vai ser o responsável por gastar menos ou mais, ou ter mais eficiência ou mais. Por que eu estou falando tudo isso, pessoal? Porque

18:38

Tem muita gente que acaba confundindo o Prompt Engineering sobre o que pedir para IA, ou como pedir para IA, e está tudo certo. Mas Prompt Engineering vai além. O Prompt Engineering faz com que você pense de uma forma estratégica para ter o melhor resultado, com o menor custo, com a menor latência.

18:57

E isso vai se encaixar nos seus agentes, nas suas chamadas e tudo mais. Então, tome muito cuidado e por isso que eu queria passar esse conteúdo base para você ter uma noção de possibilidades que existem e de problemas que vocês vão poder enfrentar no futuro e que você, às vezes, nem estava no seu radar.

19:20

Então, está aqui mais um exemplo que eu queria passar para que você tenha, vamos dizer assim, mais cautela e evitar surpresas no final do mês com as contas e ser muito mais produtivo. Fechou? Então, é isso aí, galera!

## Resumo IA

**Abreviações**
- **LLM**: *Large Language Model* (Modelo de Linguagem de Grande Porte)
- **AI / IA**: *Artificial Intelligence* / Inteligência Artificial
- **ADK**: *Agent Developer Kit* (kit de desenvolvimento de agentes)
- **JSON**: *JavaScript Object Notation*
- **JSONL**: *JSON Lines* (JSON por linha)
- **GitHub**: plataforma de hospedagem e versionamento de código com suporte a issues, repositórios e automações
- **API**: *Application Programming Interface* (Interface de Programação de Aplicações)
- **prompt caching / cache**: mecanismo de reaproveitamento de trechos fixos do prompt para reduzir custo e processamento
- **batch / batching**: processamento em lote

**Resumo**
A aula apresentou uma aplicação de análise de logs com múltiplos agentes de IA, em que um agente recebe o log, outro classifica se é erro ou operação normal, e, quando necessário, outros agentes refinam o conteúdo da issue, criam a issue no GitHub e notificam o responsável. O instrutor mostrou primeiro um fluxo “ingênuo”, em que cada log é enviado imediatamente para a LLM, o que funciona do ponto de vista funcional, mas gera alto custo, repetição de instruções e aumento de latência quando o volume de logs cresce.

Em seguida, foi explicado o problema de manter vários logs na mesma sessão: o histórico anterior passa a ser reprocessado a cada nova mensagem, consumindo tokens desnecessários. Como alternativa, o instrutor propôs criar uma conversa por log para evitar acúmulo de contexto, mas destacou que isso ainda mantém uma chamada por item. A solução mais eficiente apresentada foi o uso de buffer e batch processing, agrupando X logs por sessão e disparando o processamento somente quando o lote atinge um limiar, como 100 itens.

Nesse fluxo em lote, cada log precisa carregar um identificador próprio para permitir rastreabilidade e roteamento correto da saída. A resposta do modelo deve vir em formato estruturado, preferencialmente JSON ou JSONL, com campos mínimos como id, classificação e conteúdo necessário para a próxima etapa. O próximo agente então consome essa saída já estruturada e encaminha cada item conforme sua categoria: logs de informação encerram o fluxo, enquanto erros seguem para criação e refinamento de issue, publicação no GitHub e notificação.

O instrutor também enfatizou que, após o processamento inicial, pode ser útil abrir novas conversas nas etapas seguintes para evitar que JSONs anteriores contaminem decisões futuras. Além disso, destacou a importância de revisar o tamanho do prompt: prompts longos com muitas regras e exemplos podem ser custosos e nem sempre melhores. Em cenários em que o prefixo do prompt é estável, o batch combinado com prompt caching pode trazer economia adicional. Por fim, foi reforçado que o controle de custo não depende só da entrada: limitar explicitamente a saída do modelo, estimar consumo por lote e pensar a arquitetura de agentes junto com a engenharia de prompt são partes inseparáveis de uma solução eficiente.

**Pontos de atenção**
- Evitar enviar cada log individualmente para a LLM quando o volume é alto; isso aumenta custo, latência e repetição de prompt.
- Não manter uma mesma sessão com histórico crescente para todos os logs, pois o contexto anterior é reprocessado e consome tokens desnecessariamente.
- Preferir processamento em lote com buffer e limiar configurável, em vez de chamadas item a item.
- Garantir que cada log tenha um identificador único para rastrear a resposta e decidir o fluxo correto de execução.
- Usar saída estruturada e previsível, como JSON ou JSONL, para facilitar parsing e roteamento entre agentes.
- Manter o payload mínimo possível: campos excessivos no JSON aumentam custo sem trazer valor operacional.
- Abrir novas sessões nas etapas seguintes quando o histórico anterior puder contaminar as decisões dos próximos agentes.
- Revisar prompts muito longos: muitas regras, papéis e exemplos podem encarecer a operação sem melhorar o resultado.
- Avaliar a utilidade marginal de cada exemplo no prompt; mais exemplos nem sempre significam melhor desempenho.
- Considerar prompt caching apenas quando houver reutilização real do trecho fixo; cache também tem custo.
- Controlar explicitamente o tamanho da resposta do modelo, por exemplo, limitando tokens de saída.
- Lembrar que, em muitos providers, tokens de saída custam mais do que tokens de entrada.
- Estimar custo por lote e por volume diário para evitar surpresas financeiras.
- Tratar Prompt Engineering como decisão de arquitetura e eficiência operacional, não apenas como escrita de instruções.