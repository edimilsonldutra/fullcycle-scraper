Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17079)

## Resumo da aula

Flowchart em Mermaid representa um processo como uma sequência de passos conectados por decisões. Ele serve para responder perguntas do tipo “qual caminho o sistema segue quando uma condição muda?” e funciona especialmente bem quando há bifurcações explícitas. Em documentação técnica, isso torna visível a lógica operacional sem exigir leitura direta do código.

No Rate Limiter, o flowchart modela a decisão do Storage Mode. Retomando o cenário já conhecido do middleware e do storage adapter, a camada nova aqui é o caminho comportamental entre Redis e Memory: com Redis, o fluxo segue para script Lua, uso de EvalSha e estado compartilhado no Redis; com Memory, o fluxo segue para mutex, LocalMap e estado isolado no processo. O valor do diagrama está em mostrar que a mesma responsabilidade de persistência muda de implementação e de propriedade operacional conforme o modo escolhido.

A ramificação Redis representa um caminho voltado a consistência distribuída. O script Lua concentra a operação no servidor Redis, e o uso de EvalSha preserva atomicidade ao executar a lógica como uma unidade única. Isso importa porque o estado do rate limiting deixa de ser local e passa a ser compartilhado entre instâncias.

A ramificação Memory representa um caminho local ao processo. O mutex protege concorrência dentro da instância, enquanto o LocalMap mantém o estado em memória sem compartilhamento externo. Essa alternativa simplifica a execução, mas o isolamento do estado muda o comportamento do sistema em cenários com múltiplas réplicas.

Sequence Diagram em Mermaid representa interações temporais entre participantes. Em vez de enfatizar decisões de caminho, ele mostra quem chama quem, em que ordem, e qual resposta retorna em cada etapa. Esse formato é adequado quando a pergunta principal é “como a requisição atravessa os componentes até produzir a resposta?”.

No exemplo do Rate Limiter, a sequência começa com o client enviando um HTTP request ao middleware já visto anteriormente como ponto de entrada. O middleware trabalha com o contexto da requisição, obtém a chave e delega a checagem ao rate limiter, que lê e altera o estado no storage antes de devolver a decisão. Essa leitura temporal deixa explícito onde a decisão nasce e em que ponto ela volta para o fluxo HTTP.

Quando a decisão retorna como permitida, o processamento continua até o handler, que representa o controller responsável por executar a lógica de negócio e produzir a resposta HTTP. Nesse caminho, os headers associados ao rate limiting acompanham a resposta bem-sucedida. O diagrama deixa claro que a limitação ocorre antes da regra de negócio principal, não depois.

Quando a decisão retorna como negada, o fluxo não segue para o handler. O middleware adiciona o header Retry-After e encerra a requisição com HTTP 429 Too Many Requests. Essa bifurcação temporal complementa o flowchart: um mostra a lógica de escolha do storage, o outro mostra o efeito dessa lógica no ciclo de vida da requisição.

Os dois diagramas descrevem o mesmo sistema por perspectivas diferentes. O flowchart responde qual caminho interno é seguido conforme o Storage Mode; o sequence diagram responde como os componentes colaboram ao longo do tempo para produzir allow ou deny. Usados juntos, eles conectam decisão estrutural de execução com comportamento observável na interface HTTP.

## Transcrição

00:01

Bom, pessoal, vamos lá então, tá? Então, estávamos falando, né? Estamos falando de diagramas Mermaid, e aqui a gente tem o nosso primeiro tipo de diagrama, tá? É chamado de flowchart, que no final das contas é um fluxograma. Então, somente pra deixar bem claro e resumido, o que que isso significa? Ele vai representar pra gente fluxos de decisão, etapas e caminhos alternativos,

00:25

vai ser ideal para mostrar lógica de processos e pipelines, ele vai ser muito útil em documentação de sistemas, API e automações. Então, olha só que interessante, pessoal, eu tenho um fluxo aqui que é verificar a chave do cara para o nosso Rate Limiter. Então, eu vou verificar a chave, vou verificar qual Storage Mode que a gente tem aqui, e eu posso ter Redis ou posso ter Memory. Se for Redis, eu vou usar um script Lua,

00:53

Se for Memory, eu vou trabalhar com o Mutex. Se for usar Script Lua, eu vou usar o EvalChar para fazer atomicidade. Se for Memory, eu vou trabalhar com LocalMap. Se for o Redis, ele vai ser com Redis State, ele vai armazenar o estado no Redis. E aqui vai ser dentro do processo. Aqui é compartilhado, e aqui isolado, e aqui a gente tem a decisão

01:17

baseado no Storage Mode que a gente teve. Então, se você perceber, ele é bem simples de se ver, ele é bem tranquilo. Se você coloca o código dele, fica bem simples de você conseguir entender de forma geral. Então, esse é o nosso primeiro tipo de diagrama, de formato de diagrama que a gente tem.

01:40

um outro diagrama, né, e aí eu já não sei se todo mundo gosta. Eu sempre gostei, de forma geral, e tinha uma época que a gente usava muito mais, e eu acho que pela complexidade, às vezes, de ficar montando esse diagrama, ou tendo que pegar softwares para fazer e trabalhar com ML e tudo mais, e muita gente tem medo de a gente querer voltar para aquela época onde tudo tinha que ter tudo,

02:05

eu acho que agora as coisas ficam um pouco mais fáceis, tá? Então, a gente tem o Sequence Diagram, que é o diagrama de sequência. Então, o que ele faz? Na realidade, ele mostra a troca de mensagens entre os componentes ao longo do tempo. Ele é excelente para a gente visualizar chamadas entre os serviços, APIs, banco de dados, ajuda a gente a identificar as dependências e os gargalos de comunicação. Então, se você olhar aqui, galera, olha que interessante. Eu tenho um client que faz um HTTP request, né? Quando chega o HTTP request, ele vai bater no meu middler,

02:35

Esse meu middler vai verificar, vai ter um contexto, que é porque a gente está falando de goal, e depois eu tenho a chave. Baseado nisso, ele vai mandar pra gente pro rate limiter, o rate limiter vai ler e vai alterar o estado do nosso storage e vai retornar o estado que aquilo está naquele momento. E aí ele vai decidir se ele deve, no final das contas, negar ou não. Então, a decision volta pra cá.

03:05

Entendeu? E aqui é o interessante, ó. Se for true, vai cair a decisão e vai pra cá. Agora eu tenho outro aspecto aqui, né? Se essa decisão for ok, o que vai acontecer? Simplesmente vai continuar

03:19

o nosso processamento e a gente vai ter o response HTTP com os headers que acaba acontecendo. Dependendo da decisão, se for falso, o que vai acontecer? Ele vai dar um add retry after e vai retornar ali pro request HTTP 1429 falando que é too many requests.

03:39

Então, perceba que, olha que interessante, eu tenho duas alternativas que podem acontecer aqui para mim. Adicionar o headers, caso de true, e caso ao contrário, ele retorna o 429. Então, esse aqui é um diagrama de sequência bem legal. E o que é esse handler aqui, Wesley? Aqui, provavelmente, é o controller que acaba sendo chamado quando ele recebe a chamada HTTP. Ele vai executar um handler, que é um controller, no final das contas,

04:08

para retornar e executar as nossas regras de negócio, chamar os bancos de dados ao pontapé inicial. Mas o interessante é que a gente tem toda essa parte do middleware, do rate limiter, do storage, para fazer todas essas verificações. Beleza? Então, isso aqui é um diagrama de sequência aqui no final dos pontos. Para esse vídeo não ficar grande, no próximo vídeo a gente vai falar de outros diagramas também.

## Resumo IA

**Abreviações**
- **API** — *Application Programming Interface*.
- **HTTP** — *HyperText Transfer Protocol*.
- **Redis** — sistema de armazenamento em memória usado como banco/estrutura de dados em cache e mensageria.
- **Lua** — linguagem de script usada aqui para executar lógica atômica no Redis.
- **EvalSha** — comando do Redis para executar um script Lua já carregado, identificado por SHA.
- **TTL** — *Time To Live* (não foi citado explicitamente na transcrição, portanto não se aplica).

**Resumo**
A aula apresentou dois tipos de diagramas em Mermaid aplicados ao exemplo de um **Rate Limiter**: o **flowchart** e o **sequence diagram**. O objetivo foi mostrar como esses diagramas ajudam a documentar sistemas sem depender da leitura direta do código, deixando visível tanto a lógica de decisão quanto o comportamento temporal entre componentes.

No **flowchart**, o instrutor explicou que o diagrama representa fluxos de decisão, etapas e caminhos alternativos, sendo útil para processos, pipelines, documentação de sistemas, APIs e automações. No exemplo do Rate Limiter, o fluxo começa com a verificação da chave e segue para a decisão de **Storage Mode**. Se o modo for **Redis**, o caminho utiliza **script Lua**, **EvalSha** para garantir atomicidade e armazena o estado no Redis, caracterizando estado compartilhado entre instâncias. Se o modo for **Memory**, o fluxo usa **mutex** para controlar concorrência e **LocalMap** para manter o estado em memória dentro do processo, com isolamento local. A ideia central foi mostrar que a mesma responsabilidade de persistência pode mudar bastante conforme o modo escolhido.

No **sequence diagram**, a aula mostrou a troca de mensagens entre os componentes ao longo do tempo. O fluxo começa com o **client** enviando um **HTTP request** ao **middleware**, que obtém o contexto e a chave, repassa a validação ao **rate limiter**, e este lê e altera o estado no **storage** antes de devolver a decisão. Se a decisão for favorável, o processamento continua até o **handler** — entendido como o **controller** — que executa a regra de negócio e retorna a resposta HTTP com os headers relacionados ao rate limiting. Se a decisão for negativa, o middleware adiciona o header **Retry-After** e responde com **HTTP 429 Too Many Requests**, sem seguir para o handler. O instrutor reforçou que o flowchart mostra o caminho interno escolhido pelo storage, enquanto o sequence diagram mostra como os componentes colaboram no tempo para produzir o resultado final na interface HTTP.

**Pontos de atenção**
- O **flowchart** é mais adequado para mostrar **decisões e bifurcações**; não é o melhor formato para detalhar interações temporais.
- O **sequence diagram** é mais adequado para mostrar **ordem de chamadas, respostas e dependências entre componentes**.
- No modo **Redis**, o estado é **compartilhado** entre instâncias; isso é importante para cenários distribuídos.
- No modo **Memory**, o estado fica **isolado no processo**; isso simplifica, mas muda o comportamento em ambientes com múltiplas réplicas.
- O uso de **mutex** no modo Memory é essencial para proteger concorrência dentro da instância.
- O uso de **script Lua + EvalSha** no Redis é importante para manter **atomicidade** da operação.
- O **Rate Limiter** atua **antes** da regra de negócio principal; se a requisição for bloqueada, ela não chega ao handler/controller.
- Quando a requisição é negada, o middleware deve responder com **HTTP 429 Too Many Requests** e incluir **Retry-After**.
- Os headers relacionados ao rate limiting acompanham a resposta quando a requisição é permitida.
- Os diagramas se complementam: um explica a **estrutura da decisão**, o outro explica o **efeito dessa decisão no fluxo HTTP**.