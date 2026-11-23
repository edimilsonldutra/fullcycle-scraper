Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16578)

## Resumo da aula

Tree of Thought expande a ideia de raciocínio em etapas ao permitir que o modelo abra vários ramos de análise, aprofunde sub-ramos e compare alternativas antes de concluir. A técnica não busca apenas uma resposta plausível, mas um espaço de possibilidades organizado. Isso importa em problemas abertos, nos quais a qualidade depende de comparar hipóteses concorrentes, como diagnóstico de latência, desenho de arquitetura e planejamento técnico.

Retomando o self-consistency, a lógica ali é repetir a tarefa em múltiplas execuções e consolidar a resposta mais recorrente. Em Tree of Thought, o foco muda: o modelo explora alternativas explicitamente dentro de uma estrutura de branches e escolhe entre elas com base em um critério declarado. A diferença central não é apenas gerar várias respostas, mas construir e avaliar caminhos distintos de decisão.

Um branch representa uma hipótese ou direção de raciocínio; sub-branches detalham como essa hipótese se sustenta, como pode ser testada e quais consequências produz. Sem critério explícito, a árvore vira apenas verbosidade organizada. O prompt precisa dizer o que torna um caminho melhor: plausibilidade, custo, escalabilidade, risco, simplicidade operacional ou outro fator mensurável.

Tree of Thought funciona bem em brainstorming arquitetural, comparação de estratégias, análise de trade-offs e investigação de causas prováveis. Ele é especialmente útil quando a tarefa exige gerar alternativas, pesar prós e contras e tomar uma decisão final justificável. Em software, isso aparece em escolhas como arquitetura de processamento, hipóteses de gargalo e priorização de ações de debug.

Explorar vários caminhos aumenta verbosidade, consumo de tokens e latência, porque o modelo produz mais estrutura intermediária antes da conclusão. Também não há garantia de diversidade real entre os branches: caminhos supostamente diferentes podem repetir a mesma intuição com palavras distintas. Por isso, prompts vagos tendem a gerar árvores pobres ou redundantes; instruções claras sobre número de opções, critérios e formato de comparação melhoram bastante o resultado.

No cenário do endpoint /user lento, o prompt pede pelo menos três causas possíveis da latência, uma linha de raciocínio para cada causa, formas de verificação e comparação entre branches. Isso força o modelo a tratar cada hipótese como uma trilha investigativa separada, em vez de responder com um palpite único. Quando ele compara banco de dados, network e cache, a técnica produz não só alternativas, mas uma priorização explícita da hipótese mais plausível e da próxima ação de debug.

Uma formulação útil combina papel, problema, número mínimo de hipóteses, exigência de verificação e regra de seleção final. No exemplo, o modelo recebe o contexto de um software engineer sênior, analisa a lentidão do endpoint, gera três causas, explica como chegou a cada uma e define qual branch merece ser investigado primeiro. Esse formato conecta geração de alternativas com tomada de decisão, que é o núcleo da técnica.

Retomando o cenário de milhões de imagens por dia, a árvore não serve só para listar arquiteturas, mas para compará-las por escalabilidade, custo e complexidade. O modelo abre opções como serverless, microservices com containers e monólito escalável em cloud, avalia cada uma por critérios comuns e escolhe o melhor trade-off. O valor não está em a resposta final ser sempre correta, mas em tornar explícito por que uma alternativa foi preferida.

A mesma árvore pode ser usada com dois objetivos diferentes: inspeção do raciocínio ou entrega apenas da conclusão. Se o prompt pede comparação completa, o resultado fica mais auditável, porém mais longo; se pede somente o final answer, a árvore continua orientando a decisão, mas a saída exibida fica enxuta. Essa escolha depende do contexto: depuração e brainstorming pedem visibilidade; integração em produção muitas vezes pede só a decisão consolidada.

Mesmo prompts curtos podem produzir respostas muito densas quando a técnica exige múltiplos branches e comparação entre eles. Isso mostra que custo não depende apenas do tamanho do input, mas também da estrutura de raciocínio solicitada e do volume de output gerado. Em aplicações reais, Tree of Thought vale mais quando o ganho de exploração e decisão compensa o overhead de tokens e latência.

## Transcrição

00:01

Agora, pessoal, que a gente entendeu melhor sobre Chain of Thought, a gente vai falar sobre Tree of Thought, que a ideia é que o modelo pode explorar diferentes caminhos de raciocínio, comparar e escolher o melhor. E agora você deve estar pensando, qual é a diferença disso com o Self-Consistency? O Self-Consistency, a ideia dele é de ele ficar realmente

00:27

repetindo a mesma coisa diversas vezes e pegar uma média do que ali é o melhor, tá? Agora, quando a gente fala em Tree of Thoughts, você consegue fazer layers e sublayers. Ele pode gerar o raciocínio, do raciocínio, do raciocínio, tá? E aí, baseado em um critério, ele escolhe o melhor. Então, uma das coisas importantes, tá? Principalmente em relação ao Tree of Thoughts, em relação ao self-consistency, é o seguinte,

00:56

que, normalmente, no Tree of Thoughts, você vai colocar também o critério do que é melhor.

01:06

Esse é o ponto. Quando que você usa isso? Fazer brainstorming, pedir diversas soluções para ele fazer uma coisa, para ele planejar algo considerando alternativas, para ele decidir em diferentes estratégias de estudo, avaliar a pró, a contra, ver hipóteses e tomar uma decisão final. Qual que é a limitação? Resposta longa e complexa, gasta mais token, é difícil de garantir que os ramos, ou seja, os branches que ele vai gerando sejam completamente distintos, porque às vezes ele pega linhas de raciocínio bem parecidas,

01:36

Pode ficar repetitivo por conta disso e ele precisa de instruções bem claras pra funcionar bem, tá? Cara, eu uso muito esse cara na hora de fazer brainstorming, escolher a arquitetura, de tentar a...

01:49

de tentar ver opções que eu nem sabia que sabia, tá? E a gente, ao longo da disciplina, a gente vai fazer isso na prática e agregar todos esses tipos de prompt num único assistente, por exemplo, tá? Vamos dar uma olhada aqui no nosso Tree of Thoughts pra gente ver aqui, inclusive, pra não ter confusão em relação ao self-consistency, que é uma dúvida que acaba

02:11

podendo ser recorrente, tá? Então é o seguinte, eu tenho um prompt aqui pra mim que é o seguinte, você é um desenvolvedor sênior software engineer, o usuário reportou que tem uma API request com endpoint barra user que tá tomando 5 segundos pra responder e tá sendo muito lenta.

02:30

E daí eu botei aqui para ser bem específico, principalmente por conta do exemplo, mas você não precisa necessariamente escrever, pense como um tree of thought. Eu não preciso colocar dessa forma explicitamente. Aqui eu estou colocando muito mais para a gente registrar. Aí eu pedi para ele, gere pelo menos três possíveis causas dessa latência. Para cada causa, gere uma linha de raciocínio passo a passo de como que você

02:59

chegou isso e como que você pode verificar realmente essa causa. Depois compare esses branches, ou seja, essas situações, essas linhas de ramificação, e escolha a mais plausível das hipóteses primárias. E termine recomendando a próxima ação para debugar e resolver esse problema.

03:28

Olha só que prompt muito louco, galera. Pensa a seguinte. Qual foi a última vez que você fez um prompt desse para resolver um problema de código? Segunda pergunta aqui. Você está desenvolvendo um serviço que processa milhões de imagens diariamente. Pense da seguinte maneira, em Tree of Thoughts. Gere pelo menos três diferentes opções de arquitetura.

03:48

Para cada opção, pense passo a passo em relação à escalabilidade, custo e complexidade. Compare as opções. Escolha o melhor trade-off e explique o porquê uma é mais superior que a outra. Finalize com um final answer com a opção escolhida. Essa é a mensagem número 2. E o nosso prompt número 3 é, você está desenvolvendo um serviço que vai processar milhões de imagens, pense daquela forma...

04:17

aqui, etc, etc. Eu fiz exatamente igual, mas no final eu escrevi assim, ó, passa o output apenas da resposta final,

04:26

não tem nenhum outro texto tá então é basicamente isso que eu acabei colocando aqui vamos voltar aqui para o modelo eu vou colocar aqui o gpt 3.5 turbo tá e eu pedi aqui para ele invocar uma mensagem a de cada vez tá para gente testar porque fica muito verboso tá então deixa eu descomentar

04:47

eu vou pedir para ele executar e para ele responder a nossa primeira questão aqui. Então, vamos lá. Python, eu vou colocar um, barra, tree of thoughts aqui para a gente. Então, vamos ver, ele vai responder somente o nosso primeiro prompt. Então, o nosso primeiro prompt foi o seguinte, verificar a latência do endpoint.

05:13

Então, ele trouxe aqui, ó, causas possíveis para as latências do barra users. Um, queries de performance no banco de dados. Provavelmente, pode ser que o banco de dados esteja lento, as queries sejam lentas e impactando na resposta do endpoint da API. Como que você verifica isso? Verifique as execuções do banco de dados e vê o tempo que vai estar

05:35

utilizando e monitorando isso, analise as queries com o plano de execução, identifique os potenciais gargalos, otimize as queries adicionando índices ou reescrevendo, se necessário.

05:50

Segunda opção, latência, pode ser problema de network. Como você vai verificar? Faz um traceroute, faz um ping. Verifica o seu equipamento de network. Considere usar um content delivery network para aumentar a performance. E aqui tem code optimization. Pode ser ineficiência de mecanismo de cache, por exemplo. Então, faça essas verificações. E aí ele faz a comparação aqui.

06:16

Olha, comparando essas três branches, essas três linhas, o mais plausível dessas hipóteses pode ser latência por conta de banco de dados. Bancos de dados e queries normalmente são causas comuns para endpoints, e otimizando pode melhorar. Então, a recomendação da próxima ação.

06:33

Comece a investigação otimizando pelo banco de dados, monitore as ferramentas aqui, etc. Ele gerou ali para ver a performance da API. Galera, é muito louco você conseguir ver esses níveis de resposta e ver como ele está trazendo, analisando e justificando isso aqui para a gente. Então, isso aqui é muito legal.

06:57

em relação a esses tipos de pontos, tá? Eu não vou chamar aqui os outros LLMs, porque senão esse vídeo vai ficar muito grande e muito repetitivo, mas a ideia principal é essa. O que eu quero fazer agora aqui, eu vou pegar a mensagem 2 pra gente ver aqui, tá? Então eu vou pegar mensagem 2, vou dar um invoke nela, vou comentar a 1 e vou descomentar a 2, aqui pra mim, e eu vou mudar agora só pra...

07:25

Tem uma outra opção aqui de A. Vou usar o GPT-4O. E vamos ver como é que ele vai se comportar. E essa análise aqui é análise do quê mesmo? Era análise não da latência, era análise do processamento de milhões de imagens baseado em escalabilidade, custo e complexidade. E aqui, vamos ver o que ele trouxe pra gente, galera. Olha isso aqui, povo.

07:54

Então, quando está desenvolvendo um sistema escalável e processando milhões de imagens, é essencial considerar alguns fatores, escalabilidade, custo-eficiência e complexidade. Embaixo tem opções de arquitetura para você avaliar através desses prismas.

08:14

Então, vamos lá. Opção 1. Serverless Architecture. Desenho de arquitetura. Utiliza serviços como Lambda e etc. Usa um object storage. Trabalha com message queues. A escalabilidade dele trabalha de forma automática. Tem limitações que podem ser em relação à quota restrictions ou duração de limites. Custo. Você paga pela execução. Potencialmente,

08:40

é bom nesse momento, mas pode crescer substancialmente em volumes de pico. Complexidade, simplifica a arquitetura, né? Mais complexidade e lógica você precisa para fazer tarefas em ambientes serverless. Aqui, ele trouxe, segunda opção, microserviços com containers. Design da arquitetura, usar container, a escalabilidade, o container prover um high level, o custo, dessa forma, pode ser assim, a complexidade é essa.

09:08

Opção 3, sistema monolítico escalável com cloud e com infraestrutura. Aí ele dá a justificativa nível de complexidade. Aí ele trouxe a comparação. Escalabilidade do serverless é escalável, por isso o microservice faz isso, o monolítico faz isso. Em relação a custo, serverless faz isso, isso aqui faz isso, etc. Então ele gerou a comparação para ele mesmo e a resposta final é serverless architecture. Escolhendo a arquitetura serverless é superior em relação aos trade-offs

09:36

em relação a escalabilidade, eficiência, custo, etc, etc. Eu concordo com essa resposta, não necessariamente depende, falta muita coisa nesse prompt pra ele colocar. O importante aqui, que eu quero, é que você entenda como que um prompt

09:52

pode gerar a quantidade gigante de informação, e como que você pode explorar isso no seu dia-a-dia, pra montar o seu plano de desenvolvimento, pra você montar a sua arquitetura, pra você tirar dúvida, pra você estudar, pra você analisar possibilidades que você nem sabe que existem, né? Eu poderia pedir pra ela colocar dez tipos diferentes de arquitetura. Eu teria mais dez tipos de... mais sete informações com comparações de cada uma delas. Você entende?

10:19

o quão poderoso isso aqui pode ficar na mão se você souber realmente trabalhar com prompt, galera? Eu não sei qual é o momento da carreira que você está trabalhando com prompt, utilizando no dia a dia, tá? Mas eu acredito que cada vez e cada vídeo que a gente passa vai ficando mais transparente

10:40

o quão diferente é você mudar alguns ajustes no prompt e como que a resposta pode mudar completamente. Então, perceba, esse prompt ele nem é grande, galera. É um prompt aqui de input tokens, 94 tokens, galera. Então, assim, é muito pouco. E a gente consegue ter respostas desse nível aí. Fechou? Então a gente acabou de ver o Tree of Thoughts.

## Resumo IA

**Abreviações**  
- **LLM**: *Large Language Model* (Modelo de Linguagem de Grande Porte)  
- **API**: *Application Programming Interface* (Interface de Programação de Aplicações)  
- **CDN**: *Content Delivery Network* (Rede de Distribuição de Conteúdo)  
- **Qo** / **quota**: limites de uso/cota do serviço  
- **GPT**: *Generative Pre-trained Transformer* (Transformador Generativo Pré-treinado)  
- **Lambda**: serviço de computação serverless da AWS  
- **Cloud**: computação em nuvem  

**Resumo**  
A aula apresentou a técnica **Tree of Thought**, explicando que ela amplia o raciocínio em etapas ao permitir que o modelo explore vários caminhos, crie subcaminhos e compare alternativas antes de concluir. O instrutor destacou a diferença em relação ao **Self-Consistency**: enquanto este repete a mesma tarefa várias vezes e consolida a resposta mais recorrente, o Tree of Thought organiza explicitamente branches de raciocínio e escolhe a melhor alternativa com base em um critério definido no prompt. A ênfase principal é que não basta gerar múltiplas respostas; é preciso estruturar hipóteses diferentes, avaliá-las e justificar a decisão final.

O conteúdo mostrou que a técnica é especialmente útil em problemas abertos, brainstorming arquitetural, análise de trade-offs, investigação de causas de latência e tomada de decisão técnica. O instrutor enfatizou que o prompt deve deixar claro o que significa “melhor”: plausibilidade, custo, escalabilidade, risco, simplicidade operacional ou outro critério mensurável. Sem isso, a árvore tende a virar apenas uma resposta longa e repetitiva, com branches pouco distintos.

Na prática, foram apresentados exemplos de uso. No caso do endpoint **/user** lento, o prompt pedia pelo menos três causas possíveis da latência, um raciocínio para cada causa, formas de verificar cada hipótese e uma comparação entre as branches para escolher a mais plausível e sugerir a próxima ação de debug. O modelo respondeu com hipóteses como problema de banco de dados, network e cache, comparando-as e priorizando a investigação no banco. Em outro exemplo, sobre um sistema que processa milhões de imagens por dia, o Tree of Thought foi usado para comparar arquiteturas como serverless, microserviços com containers e monólito escalável em cloud, avaliando cada opção por escalabilidade, custo e complexidade até chegar à melhor escolha de trade-off.

A aula também mostrou que a mesma árvore pode ser usada para duas finalidades: expor o raciocínio completo para inspeção e depuração, ou entregar apenas a resposta final em produção. O instrutor explicou que, embora o output possa ficar bem longo e custoso, o ganho de exploração e clareza decisória pode compensar em cenários de arquitetura, estudo, priorização e troubleshooting.

**Pontos de atenção**  
- É obrigatório definir um **critério explícito de escolha**; sem isso, o resultado tende a ser apenas verboso.  
- **Prompts vagos** geram árvores pobres, redundantes ou com ramos muito parecidos.  
- A técnica aumenta **consumo de tokens, latência e tamanho da resposta**.  
- Não há garantia de **diversidade real** entre branches; o modelo pode repetir a mesma ideia com palavras diferentes.  
- Vale mais quando há **alternativas concorrentes reais** e necessidade de comparar prós e contras.  
- Em debugging e arquitetura, peça sempre: **hipóteses mínimas, forma de verificação e regra de comparação final**.  
- Para produção, pode ser melhor pedir **apenas o final answer** para manter a saída enxuta.  
- O benefício depende do contexto: o overhead só compensa quando a exploração adicional melhora a decisão.  
- Mesmo prompts curtos podem gerar respostas muito grandes, então é preciso controlar bem o **escopo da exploração**.