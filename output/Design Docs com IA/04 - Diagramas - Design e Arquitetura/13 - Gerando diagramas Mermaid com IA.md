Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17082)

## Resumo da aula

Um agente Mermaid Generator transforma o FDD em um pacote de diagramas Mermaid a partir de um workflow explícito, em vez de responder com um único diagrama improvisado. A função central dele é ler o documento-fonte, extrair elementos relevantes, identificar o que está dentro e fora de escopo e só então escolher as representações visuais adequadas. Isso reduz alucinação estrutural, porque o agente recebe regras claras como não inventar elementos, usar language matching e justificar inferências inevitáveis. O resultado deixa de ser uma resposta solta do modelo e passa a ser uma geração guiada por critérios auditáveis.

O prompt precisa explicitar a ordem de trabalho: leitura do FDD, extração dos elementos principais, identificação de inferências, seleção dos diagramas, geração e revisão interna. Regras como short labels, clean syntax, ausência de emojis e proibição de duplicar a mesma visão evitam saídas visualmente poluídas e semanticamente redundantes. Inferência não é proibida, mas deve ser minimizada e justificada, porque a ausência de dados no FDD não autoriza o agente a completar o sistema com suposições arbitrárias. Esse desenho do prompt importa mais do que um texto genérico pedindo “gere diagramas Mermaid”.

A escolha do tipo de diagrama deve ser dirigida pela pergunta técnica que precisa ser respondida. Se o problema é interação temporal, o agente tende a priorizar sequência; se a questão é fluxo decisório ou algoritmo, flowchart; se o foco é contrato estrutural, class diagram; se houver modelagem de dados relevante, ER pode entrar como opcional. Retomando o Rate Limiter, o mesmo FDD se desdobra em visões diferentes sem repetir conteúdo: fluxo HTTP, algoritmos de limitação, modos de storage, contratos públicos e cenários de fallback. O ganho está em cobrir perspectivas complementares, não em multiplicar diagramas por volume.

Diferentemente do C4, Mermaid não impõe um conjunto fixo de arquivos, então o prompt precisa controlar quantidade e granularidade. Um intervalo como 6 a 8 diagramas costuma equilibrar cobertura e legibilidade, enquanto um teto como 10 impede explosão de artefatos pouco úteis. Regras de densidade, como agrupar fluxos com mais de 8 etapas ou dividir diagramas com mais de 10 nós em views complementares, evitam que o diagrama compile mas continue ilegível. O critério correto não é “quanto mais, melhor”, e sim “quantos são necessários para explicar sem redundância”.

No eixo Mermaid, a saída mais prática é um único arquivo Markdown contendo texto explicativo e blocos Mermaid renderizáveis. Isso simplifica versionamento, leitura e incorporação direta em documentação, sem espalhar a visão do sistema em vários arquivos pequenos como ocorre com o pipeline C4. O arquivo único também favorece revisão humana, porque contexto, justificativas e diagramas ficam lado a lado. Para um pacote de visões do Rate Limiter, esse formato funciona bem como documento curado de referência técnica.

A execução pode ser reduzida a um comando simples que chama o agente, aponta para o FeatureDoc e define a pasta de saída. No exemplo, o comando generateMermaid usa o agente MermaidDiagramGenerator sobre o contexto do @rate-limiter, delegando ao prompt as fases de análise, seleção, geração e checagem. Essa separação é importante porque o comando permanece estável, enquanto a inteligência do processo fica concentrada no agente. Quando o prompt está bem desenhado, trocar modelo ou ferramenta altera menos o workflow do que parece.

A autorrevisão é uma etapa explícita em que o próprio agente relê o que gerou e corrige problemas antes da entrega final. Isso captura erros de sintaxe, inconsistências de nomenclatura, excesso de densidade e escolhas ruins de representação que passariam se a geração terminasse na primeira tentativa. No exemplo, a diferença entre a versão inicial e a revisada mostra que pedir revisão não é detalhe cosmético; é parte do controle de qualidade. Sem essa etapa, o custo da depuração manual cresce rapidamente.

Mermaid oferece uma forma objetiva de validação inicial: se a sintaxe estiver errada, o diagrama não compila ou não renderiza. Esse feedback é valioso porque separa erro estrutural de erro semântico; primeiro garante-se que o artefato é renderizável, depois verifica-se se ele representa corretamente o sistema. No exemplo, a compilação bem-sucedida dos diagramas já elimina uma classe inteira de falhas mecânicas. Ainda assim, renderizar não prova fidelidade ao FDD, apenas prova que o código Mermaid está formalmente aceitável.

Retomando o Rate Limiter, o FDD foi convertido em múltiplas visões complementares dentro do mesmo Markdown. O conjunto inclui sequência da requisição HTTP com allow e deny, fluxo de fixed window, fluxo de token bucket, comparação entre Redis e Memory, cenário de fallback open, atomicidade com script Lua no Redis, concorrência local com mutex e contratos públicos extraídos das interfaces e structs. Essa decomposição mostra como um único documento-fonte pode gerar diagramas operacionais, algorítmicos e estruturais sem reexplicar o domínio do zero. O ponto principal é que cada diagrama responde a uma pergunta técnica distinta.

Mesmo com compilação, autorrevisão e um modelo rápido produzindo saída útil em segundos, a revisão humana continua sendo a etapa decisiva. É preciso conferir se o agente representou corretamente detalhes como cluster Redis, réplicas, políticas de fallback, contratos públicos e limites do que estava realmente documentado. Diagramas plausíveis podem esconder simplificações indevidas ou omissões importantes, especialmente quando o agente precisou inferir algo. A IA acelera a produção do rascunho técnico; a responsabilidade pela correção arquitetural continua com quem revisa.

## Transcrição

00:01

Bom, pessoal, agora estamos aqui de volta com demonstrações de IA e esses diagramas e, novamente, você vai ter o prompt de tudo isso para você testar, utilizar aí nos seus sistemas e tudo mais.

00:17

Nesse nosso caso aqui, também, mesmo esquema que eu fiz com os diagramas C4, eu tenho aqui com o Mermaid. Então, eu criei aqui um sub-agente ou um agente para Mermaid Generator, e basicamente aqui está

00:38

a descrição, o prompt desse agente. Então, ele vai ler o nosso FDD, a missão principal dele, o mesmo esquema de linguagem, para ser em português, correto ou errado, para ele utilizar a linguagem que ele precisa, e aqui tem o workflow. E eu coloco muito claro, não crie, não invente elementos, utilize language matching, verifique a relevância,

01:03

versus a quantidade, multiplique os diagramas, múltiplos diagramas do mesmo tipo são permitidos, o que é mais importante primeiro e etc., não inventar, short labels, clean syntax, no emojis e tudo mais. E aqui são regras críticas que ele tem que seguir, mas aqui eu mostro o workflow de uma forma bem clara, primeiro leia o arquivo,

01:27

extraia os principais elementos, identifique quais são os pontos de sucesso, o que vai ser excluído disso aí, o que está out of scope, quais são as principais inferências, porque às vezes a gente não tem toda a informação, mas eu posso inferir baseado naquilo que

01:52

Funciona daquela forma, por exemplo, o cara não tem saldo na conta, eu deixo ele fazer a transação, então eu coloco como inferência não, porque ele não tem dinheiro. Estou dando um exemplo aqui, somente para você entender. Então eu pedi para ele inferir, mas também para ele minimizar ao máximo, e se ele fizer alguma inferência, ele vai ter que justificar para mim o que ele fez, somente para garantir que eu não tenha algum problema depois.

02:17

Então, aqui está todo o prompt. Então, tem a forma que ele vai primeiro tentar selecionar o tipo de diagrama para o tipo de problema. Então, diagrama de sequência, flowchart aqui top-down, flowchart left-right, diagrama de classe, diagrama de ER, que é opcional. Então, se você olhar aqui, ele dá exemplos de quando usa um e quando usa outros. E aqui tem

02:47

Otimização. E aqui tem um ponto que é diferente do C4, tá, galera? Por quê? Porque no C4, são quatro diagramas. São três C's, de forma geral. Nos diagramas Mermaid,

02:59

depende da quantidade de diagramas que eu quero naquele momento, entendeu? Então, nesse prompt, o que eu fiz, e daí eu recomendo que você altere de acordo com o que faz sentido pra você, é o seguinte, eu falei que ele pode gerar até 10 diagramas, e no mínimo 1 diagrama, tá? E que normalmente, se ele fizer entre 6 a 8 diagramas, a...

03:22

Tá bom, entendeu? É um número mais ótimo ali pra gente, tá? Então, você pode mudar com essa quantidade de números, ou você pode especificar exatamente qual tipo de diagrama que você quer pra cada caso de uso. Aqui eu fiz pra uso mais geral, por isso que eu deixei ele criar até 10 diagramas ali pra gente. E aí, ó, nunca faça diagramas que mostrem a mesma coisa. Se tiver mais de 8 steps nesse diagrama, faça um agrupamento de 8 pra não ficar...

03:51

tudo agrupado e o negócio não ficar muito grande. Se o diagrama ficar muito denso, mais de 10 nodes, considerar para criar duas views complementares. E aqui tem algumas prioridades que eu recomendo, ou seja, o fluxo principal,

04:12

os pontos mais complexos para a decisão lógica, os pontos arquiteturais, os pontos críticos em relação a APIs públicas, e os pontos de erro, caso não sejam triviais. E aí, como ele vai preparar, usar os patterns de nome, as labels que ele vai utilizar, e aí a documentação, aí eu criei aqui um

04:34

uma forma de ele gerar esse documento, porque esse documento aqui, galera, somente para você entender, não é igual ao C4, porque o C4 são quatro arquivos, tá? E mais um readme que ele gerou ali para mim, né? Esse cara é um único arquivo que ele vai gerar.

04:53

Então, porque através de um Markdown eu tenho já o meu diagrama C4, C4 não, Mermaid feito. Então, ele tem uma característica diferente, então por isso que eu tentei deixar ele sempre mais aberto.

05:08

aqui pra gente. Então, aqui eu tô dando vários exemplos de diagrama, se você olhar aqui, a parte, fase 8, fazer uma revisão interna pra corrigir. Então, galera, é um prompt bem grande de forma geral também, tem workflow e tudo mais, tá? Então, tem checklist, ou seja, é um prompt realmente grande,

05:30

Fiquei muitas horas e inclusive dias aqui gerando esse cara, testando com diversos projetos. Como eu sempre digo, de modelo para modelo as coisas podem mudar, de projeto para projeto pode mudar, mas isso aqui para você pode ser um ponto de partida, tá? Mas da mesma forma que eu tenho um agente, eu tenho um comando, né? E esse comando aqui, basicamente, ele é um comando simples, bem parecido com o do outro, que é

05:54

Você tem que chamar o Mermaid Diagram Generator, extrair os dados do FeatureDoc Document aqui, o Output Folder, como que é o nome, o agente deve completar essas fases, tem que analisar e selecionar a parte de geração, qualidade, regras críticas e etc. Basicamente, é um comando de forma geral bem simples para você conseguir trabalhar.

06:21

Aqui, o que eu vou fazer, galera? Nós vamos fazer isso juntos nesse momento, porque eu não testei, na realidade, esse modelo Composer com diagramas Mermaid. Eu acredito que eu tenha feito isso somente com o C4. Vamos ver o que ele gera, vamos ver se tem muito erro. É interessante que o Mermaid, quando tem erro, ele não compila. Aparece o erro ali pra gente. Então, eu vou colocar, baseado no...

06:50

E aqui eu vou colocar o nome do nosso agente, que é a MermaidDiagramGenerator. Execute o comando generateMermaid usando o arroba

07:13

rate limiter aqui pra mim. Eu vou dar um enter e vamos ver se esse cara vai gerar rápido isso aqui pra gente. Então, ele já criou o diretório, tá executando as paradas aqui, tá criando o markdown já. Vamos aguardar alguns momentinhos.

07:36

E gerou aqui pra gente. Agora ele vai ter que refazer a revisão interna. Ele já tá fazendo a autorrevisão, tá? Então, é importante ter essa parte de autorrevisão, galera. Olha quanto que ele tá alterando baseado no código inicial que ele gerou, se eu não tivesse pedido, tá? Então, esse aí é um ponto importante aqui pra gente. Então, ele gerou, o bendito, né? A diagrama aqui pra gente. Vamos dar uma olhada se vai funcionar.

08:05

Tem o Mermaid, Rate Limiter Diagrams, e eu vou aqui para visualizar, vou esconder aqui o meu cara, e aqui ó, Diagramas Mermaid, Rate Limiter, a visão geral, ele dá uma visão geral do sistema, elementos identificados, cliente HTTP fazendo requisições, microserviços integrando o SDK, Redis como Backend Storage distribuídos,

08:32

e o Prometheus e OpenTelemetry para telemetria. Processos internos, método check, middleware HTTP, janela fixa, token bucket, atomicidade com script Lua do Redis, modo fallback open para resiliência. Variações de comportamento, modo storage Redis é compartilhado versus memory local, estratégia de fixa do window e token bucket, fallback open habilitado, permissivo, desabilitado, restritivo.

08:58

Contratos públicos e diagramas. Agora aqui que é o ponto que a gente quer ver, né?

09:04

Diagramas. Vamos ver se vai compilar esses diagramas dele. Cara, já compilou aqui de interessante, hein? Esse diagrama de sequência ilustra o fluxo completo de uma requisição HTTP através do midware, do rate limiter. Mostra a interação entre clientes, midware, SDK, rate limiter e storage, incluindo a decisão de allow e deny os headers HTTP. Então, ele trouxe esse cara aqui. Deixa eu dar um keep nesse cara aqui e fechar para a gente ficar com uma tela maior aqui.

09:34

Deixa eu diminuir o zoom aqui também pra gente, pra gente conseguir ver esse cara melhor. Então, o cara fez aqui pra gente aquele nosso diagrama de sequência. Cliente, middleware, rate limiter, storage e telemetria. Exibe chave. Eu não vou ficar olhando os detalhes aqui, tá, galera? Mas, ó, tem se é permitido, se é deny, o 429 e o 200, mais os headers. Cara, aparentemente tá super ok.

10:01

Aí tem algoritmo de janela fixa, então ele trouxe aqui para mim o fluxo caso eu vou trabalhar com fixer do Windows, se a janela existe sim, janela inspirada sim, zero o contador, define o tempo de vida, contador abaixo de limite, incremento o contador, atualizo o estado, decisão permitir, calcula e retorna a decisão. Caso seja negado, calculo o retry after e retorna a decisão passando, que o cara tem que tentar daqui tanto tempo, enfim.

10:29

A gente tem aqui o algoritmo de token bucket, tem o estado atual do last refill, calcular o tempo ocorrido, calcula a recarga, atualiza os tokens, atualiza o timestamp, a token está disponível e sim, consome os tokens, atualiza, decisão e etc. Aparentemente ok. Ele traz algumas anotações. Tokens são recarregados continuamente até o burst máximo. E aqui tem o modelo de storage. Se for Redis, faz isso. Se for Memory, vai ser dessa forma. Traz as latências.

10:59

Aqui, fallback open, ou seja, chamou o cheque, verificação, tenta a operação back-end. Se ele não conseguir bater no Redis, se conseguir, der sucesso, sim, ele vai no modo normal, processa, consome cota, faz o log e retorna a decisão e fim. Agora, caso não tenha sucesso, o fallback está habilitado? Sim. Se está habilitado, ele vai liberar sempre o cara acessar porque o Redis está indisponível, provavelmente.

11:27

Se tiver reestabelecido, volta para o modo normal, se não, ele vai para o fallback normal. Se o fallback não está habilitado, ele faz a decisão de denar e colocar o erro, e logo o erro para a decisão final. E aqui a gente tem um outro diagrama que ele fez aqui.

11:45

calcula o Redis, o Rate Limiter, chama aqui o nosso script pra lua, bate no Redis primário, a execução, lê o estado, calcula o novo estado, valida o limite, atualiza o valor, atualiza o time to live e retorna e quantos retries ele tem e

12:02

Isso aqui tem que ser atualizado com o Redis de réplicas, porque eu estou falando que é um cluster em Redis no nosso documento, né? Então, ele trouxe aqui o Redis primário e tem a consistência que ele vai atualizar. E aqui eu tenho atomicidade de memória com mutex, porque aqui eu estou utilizando o Redis back-end externo.

12:22

Aqui eu estou usando memória local. Então, bate nas minhas gorrotinas, tem o lock... Cara, que legal! Ficou muito bacana isso. Um cara adquire o lock, daí o outro não pode mexer, aí ele pode ler o estado... Cara, ficou bem legal isso aqui para evitar race condition. Aqui, contratos públicos, ou seja, ele criou aqui, viu as nossas interfaces, viu as nossas structs de como a gente fez e, cara, ficou bem parecido com aquele que eu mostrei aqui para vocês.

12:49

Então, pessoal, olha só que interessante, tá? Eu não usei o Cloud Code, e mesmo não usando o Cloud Code, aquele Composer, que nesse caso é um modelo super rápido, que foi lançado aí no Cursor, fez isso aí em questão de segundos pra gente ter esse cara funcionando. Obviamente, a gente tem que validar tudo, a gente tem que ser crítico e tudo mais,

13:10

mas é um baita ponto de partida, tá? E é isso que eu queria aqui passar pra vocês, beleza? Próximo vídeo, eu quero mostrar pra vocês aonde você vai poder acessar também esses prompts e tudo mais, e a gente se fala.

## Resumo IA

**Abreviações**
- **FDD** — Feature Document Document
- **Mermaid** — linguagem de descrição de diagramas usada para gerar visões renderizáveis em Markdown
- **C4** — modelo de representação de arquitetura em quatro níveis/visões
- **ER** — Entity-Relationship (Relacionamento entre Entidades)
- **SDK** — Software Development Kit
- **HTTP** — HyperText Transfer Protocol
- **API** — Application Programming Interface
- **Redis** — banco de dados/armazenamento em memória usado como backend de rate limiting
- **Lua** — linguagem usada em scripts para execução atômica no Redis
- **Markdown** — formato de texto leve usado para documentação
- **README** — arquivo de documentação introdutória de um projeto
- **Prometheus** — ferramenta de monitoramento e coleta de métricas
- **OpenTelemetry** — padrão/ferramenta para telemetria observável
- **TTL** — Time To Live
- **CPU** — Central Processing Unit
- **HTTP 429** — código de resposta “Too Many Requests”
- **race condition** — condição de corrida
- **mutex** — mutual exclusion, mecanismo de exclusão mútua

**Resumo**
A aula mostrou como criar um agente especializado em gerar diagramas Mermaid a partir de um FDD, substituindo uma geração improvisada por um workflow explícito e auditável. O foco foi desenhar um prompt robusto para o agente ler o documento-fonte, extrair elementos relevantes, identificar o que está dentro e fora de escopo, registrar inferências necessárias e então selecionar o tipo de diagrama mais adequado para cada problema técnico. O instrutor destacou que o prompt importa mais do que um pedido genérico, porque ele reduz alucinação estrutural e orienta a produção com regras claras, como não inventar elementos, usar language matching, manter short labels, clean syntax, evitar emojis e não duplicar a mesma visão em diagramas diferentes.

Também foi explicado como o agente decide a representação visual conforme a pergunta técnica: diagrama de sequência para interações temporais, flowchart para fluxo decisório ou algoritmo, diagrama de classes para contratos e ER como opção quando houver modelagem de dados relevante. Ao contrário do C4, que possui uma estrutura mais fixa, Mermaid permite uma quantidade variável de diagramas, então o prompt precisa controlar cobertura e legibilidade, com faixa sugerida de 6 a 8 diagramas e teto de 10. O instrutor reforçou regras de densidade, como agrupar fluxos com mais de 8 etapas e considerar visões complementares quando houver mais de 10 nós, para evitar excesso de artefatos e redundância.

A aula também mostrou que o resultado final pode ser entregue em um único arquivo Markdown contendo explicações e blocos Mermaid renderizáveis, o que simplifica versionamento, leitura e documentação. Houve uma demonstração prática com o comando generateMermaid aplicado ao context do rate limiter, usando o agente MermaidDiagramGenerator para ler o FeatureDoc, gerar o pacote e executar uma autorrevisão interna antes da entrega final. Na prática, o agente produziu múltiplas visões complementares, incluindo sequência da requisição HTTP com decisões allow/deny, fluxo de fixed window, fluxo de token bucket, comparação entre Redis e Memory, fallback open, atomicidade com script Lua no Redis, concorrência local com mutex e contratos públicos extraídos de interfaces e structs.

O instrutor também enfatizou que Mermaid oferece validação inicial objetiva, porque diagramas com erro de sintaxe não compilam, o que ajuda a separar falhas mecânicas de problemas semânticos. Mesmo assim, renderizar com sucesso não garante fidelidade ao FDD, então a revisão humana continua sendo essencial para verificar se o agente interpretou corretamente detalhes arquiteturais como cluster Redis, réplicas, políticas de fallback e limites do que estava documentado. O objetivo central da aula foi mostrar que a IA acelera a produção do rascunho técnico, mas a responsabilidade pela correção arquitetural e pela validação final permanece com quem revisa.

**Pontos de atenção**
- Não deixar o agente “inventar” elementos ausentes no FDD.
- Permitir inferências apenas quando necessárias, sempre minimizando e justificando.
- Definir explicitamente o workflow do agente: ler, extrair, identificar out of scope, inferir, selecionar diagrama, gerar e revisar.
- Usar language matching e manter consistência com a língua e terminologia do documento-fonte.
- Evitar diagramas redundantes que mostrem a mesma coisa sob ângulos repetidos.
- Controlar quantidade e granularidade dos diagramas; excesso piora a legibilidade.
- Aplicar regras de densidade: mais de 8 passos deve ser agrupado; mais de 10 nós pode exigir duas visões complementares.
- Priorizar o tipo de diagrama conforme a pergunta técnica, não por preferência estética.
- Manter labels curtas, sintaxe limpa e sem emojis para evitar poluição visual.
- Fazer autorrevisão antes da entrega final para corrigir sintaxe, nomenclatura, densidade e escolhas ruins de representação.
- Lembrar que compilação bem-sucedida em Mermaid não prova fidelidade semântica ao FDD.
- Validar manualmente detalhes arquiteturais críticos, como Redis primário/réplicas, fallback, contratos públicos e concorrência.
- Tratar o arquivo Markdown único como documento curado de referência, mas sem dispensar revisão técnica humana.