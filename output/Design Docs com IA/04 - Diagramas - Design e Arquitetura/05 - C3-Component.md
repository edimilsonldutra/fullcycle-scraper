Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17074)

## Resumo da aula

C3 detalha a estrutura interna de um container já conhecido no C2. Em vez de tratar o serviço HTTP do Rate Limiter como caixa preta, esse nível expõe os componentes que colaboram para tomar a decisão de allow ou deny. O objetivo não é redesenhar o sistema inteiro, mas tornar visíveis responsabilidades, contratos internos e pontos de acoplamento. Isso ajuda a preservar coesão entre módulos e a reduzir dependências desnecessárias entre partes internas.

No C3, apenas o container aberto é decomposto em componentes; dependências externas continuam aparecendo como containers externos. Retomando o serviço HTTP já visto, Redis, Prometheus e OpenTelemetry permanecem fora da decomposição interna porque não pertencem ao interior lógico do Rate Limiter. Essa convenção visual evita misturar “o que está dentro do container” com “o que o container usa”. O diagrama fica mais legível porque a fronteira do container continua explícita mesmo quando o nível de detalhe aumenta.

O HTTP middleware é o componente central porque toda requisição passa por ele antes de seguir no pipeline do servidor. Ele recebe a chamada, extrai a identidade relevante da requisição, aciona a API interna do Rate Limiter, interpreta a decisão e escreve os headers de resposta. Esse papel o torna o ponto de orquestração do fluxo, mesmo sem concentrar toda a lógica de negócio. A vantagem é separar entrada HTTP, decisão de limitação e persistência de estado em contratos distintos.

Key Extractor é o componente que transforma a requisição em uma chave de rate limiting. Essa chave pode representar IP, API key, API token ou tenant, dependendo da política aplicada pelo sistema. Ele existe porque o limite nunca é calculado “para a requisição em si”, mas para alguma identidade derivada dela. Em um cenário multi-tenant, essa extração define corretamente quem está consumindo a cota e evita aplicar o mesmo contador a entidades diferentes.

API pública interna é o contrato exposto pelo Rate Limiter para outros componentes do mesmo container, especialmente o middleware. “Pública” aqui não significa externa nem remota; significa apenas que existe uma interface acessível e estável dentro do processo para solicitar a checagem de limites. Essa separação importa porque o middleware depende do contrato, não da implementação concreta da estratégia ou do storage. O resultado é uma composição interna mais testável e mais fácil de evoluir.

Strategy Engine decide qual algoritmo de limitação será aplicado para a requisição corrente. No exemplo, ele seleciona entre fixed window e token bucket, preservando a ideia de paridade comportamental entre os modos suportados. Esse componente existe porque a decisão de limite não é única: cada estratégia tem regras próprias de consumo, reposição ou contagem. Ao centralizar essa escolha, o sistema evita espalhar condicionais de algoritmo pelo middleware e pelo acesso ao estado.

Fixed window conta requisições dentro de janelas discretas de tempo, como “N chamadas por minuto”, e reinicia a contagem ao trocar de janela. Token bucket modela capacidade disponível por meio de tokens que são consumidos a cada requisição e repostos ao longo do tempo, permitindo bursts controlados. A escolha entre eles altera diretamente o comportamento percebido pelo cliente, especialmente em bordas de janela e em picos curtos de tráfego. Por isso, o diagrama C3 precisa mostrar onde essa decisão algorítmica é tomada.

Storage adapter encapsula a leitura e a atualização do estado usado pelas estratégias. Ele abstrai se o estado está em memória local com locks por chave ou em Redis com script Lua para operação distribuída e atômica. Esse isolamento evita que a lógica de estratégia conheça detalhes de persistência e sincronização. Também permite manter o mesmo contrato interno mesmo quando o modo operacional muda entre execução local e distribuída.

O fluxo interno começa no HTTP middleware, que intercepta a requisição e delega a extração da chave ao Key Extractor. Em seguida, o middleware chama a API interna do Rate Limiter, que usa o Strategy Engine para escolher o algoritmo e consultar ou atualizar o estado por meio do storage adapter. Com a decisão pronta, o middleware devolve allow ou deny e escreve os headers correspondentes na resposta. Esse encadeamento transforma o container antes visto como bloco único em um mecanismo interno compreensível.

O diagrama C3 ganha confiabilidade quando cada componente e cada anotação podem ser rastreados ao Feature Design Doc. No exemplo, os headers e os comportamentos de storage são justificados por seções específicas do documento-fonte, em vez de inferidos livremente. Esse grounding reduz alucinação na geração assistida por IA e mantém o diagrama fiel ao design aprovado. A próxima evolução natural é materializar esses contratos internos em artefatos mais próximos do código.

## Transcrição

00:01

Bom, pessoal, e agora que nós passamos da parte de container, a gente vai agora mergulhar um pouco mais em relação à parte de componentes. Então, o que esse C3 faz? Um, ele organiza cada container em módulos, pacotes ou camadas. Depende de como você vai chamar e depende do tipo do seu sistema.

00:28

ele vai deixar claro onde estão as responsabilidades. Então, ele auxilia os desenvolvedores a manterem a coesão e reduzirem o acoplamento. E o porquê que eu estou dizendo isso, galera? Porque, até agora, se você olhar,

00:43

Isso aqui era como se fosse uma black box, uma caixa preta, onde eu sei o que isso faz, mas eu não tenho os detalhes de aqui dentro, de como que esses caras se comunicam para que esse rate limiting funcione, tá? Então, nesse caso aqui, perceba que eu tenho um serviço HTTP. Então, se eu olhar aqui e falar, ok, eu tenho o meu serviço HTTP, que é um container. Então, perceba, esse cara azul agora, que é um container,

01:13

ele virou esse cara aqui expandido, ou seja, isso aqui é o que está dentro do nosso container referente ao nosso rate limiter, tá? E aqui como é que ele funciona então, os componentes do nosso rate limiter? A gente tem aqui o middleware HTTP, ou seja, esse middleware vai ser chamado toda vez que bater qualquer coisa dentro do nosso servidor HTTP, legal?

01:37

ele vai extrair a chave via KeyFunk, no final das contas, ou seja, a chave nesse caso do RateLimiter é, vou ver se o cara está num determinado IP, vou ver se ele está num determinado plano, vou tentar entender quem é esse cara, ou seja, a gente tem que identificar. Então, esse componente vai extrair, vai chamar o RateLimiter, vai checar

02:04

se a pessoa tem acesso ou não, e vai escrever e retornar no header a resposta. Beleza? Então, é basicamente isso. Ou seja, o cara central no nosso rate limiter, de forma geral, o componente principal, é o HTTP middleware. Porque esse middleware vai precisar usar um monte de componente para que, no final, vai ser ele que vai falar

02:30

se o cara vai poder acessar aquela requisição ou não, caso ele tenha atingido um determinado limite. Se você perceber, ele extrai a chave via keyfunc, ele chama o rate limiter, ele checa e escreve os headers da resposta. Então, baseado nisso, olha só que interessante.

02:50

ele precisa fazer uma verificação aqui nesse nosso caso. Então, para eu fazer isso, eu preciso de um Key Extractor. Ou seja, vai ser algo que nesse momento ele vai me ajudar a entender qual é o tipo de chave que eu vou utilizar. Ou seja, pode ser uma chave de API, pode ser uma Key, um API Token, pode ser um IP ou pode ser um Tenant, porque esse nosso Rate Limiter é um Multi-Tenant.

03:19

a partir de uma determinada requisição, tá? Outra coisa que esse cara vai fazer é ele vai bater na API pública do Rate Limiter. E quando eu falo API pública, pessoal, eu não estou falando que é uma API externa de outro sistema, tá? API, no final das contas, significa Application Program Interface, ou seja, é uma interface para você falar

03:42

em qualquer tipo de aplicação. Então, eu tenho API internas no meu sistema, que normalmente são os contratos que eu faço através das minhas interfaces. Então, o que acontece é o seguinte, o meu middleware HTTP vai, no final das contas, bater nesse meu rate limiter, porque ele tem uma API pública para eu acessar, e faz a chamada e entende a checagem dos limites. O grande ponto é que, para esse rate limiter funcionar,

04:09

existe a estratégia que a gente vai utilizar. E nesse caso aqui, ele vai orquestrar essa decisão. Ou seja, a gente tem um strategy engine. Ou, no final das contas, a gente trabalha com um pattern de strategy, alguma coisa desse tipo, porque essa estratégia vai depender do quê? No final das contas, se esse rate limiter vai utilizar fixed window ou token bucket com paridade entre os modos. O que isso significa?

04:36

que o meu Rate Limiter tem duas estratégias. Então, aqui, nesse momento, eu vou verificar qual é a estratégia. Porque se for janela fixa, o comportamento é um. Se for token bucket, também o comportamento é outro. Beleza? E se você olhar aqui, especificamente nesse caso,

04:54

o que que eu acabei pedindo pra colocar no prompt, tá? Se você olhar a nossa FDD, o Feature Design Doc, aqui eu pedi pra ele justificar, ou seja, fazer grounding, da onde que vem essa informação. Então, nesse caso aqui, eu falei, ó, na sessão 5, lá do meu Feature Design Doc, tá, que eu vou escrever nos headers, e são esses quatro itens que vai pro nosso, pros três itens que vai no header aqui pra gente, tá?

05:22

Outro ponto importante também é que...

05:26

Eu tenho esse meu Strategy Engine, ele também vai ler e atualizar o estado, e eu tenho um adaptador de storage. Por quê? Porque eu posso utilizar isso de forma... Eu posso usar isso de forma compartilhada, um estado compartilhado com outros sistemas e etc., um estado externo. Nesse caso, eu uso o Redis, ou seja, eu trabalho de forma distribuída.

05:53

Ou eu tenho aqui memória local com locks por via de chave, back-end, Redis, via script Lua. Eu tenho essas duas opções, tá? E aqui, ó, eu tenho a seção onde é falado sobre essas formas que estão sendo utilizadas. Ou seja, memória é um lock por chave, Redis é um script Lua pra atomicidade em variança, paridade entre os comportamentos entre ambos.

06:15

A paridade, depois a gente vai falar sobre isso, de qualquer forma. Mas a ideia aqui, inclusive, é que eu não vou ficar explicando o sistema pra vocês. Eu só tô querendo mostrar pra vocês como que começa a ficar mais simples você entender um sistema olhando os componentes que ele acaba tendo ali dentro. E por isso que é o C3 de component, tá? E aqui mostra o que tá fora

06:38

do nosso serviço HTTP desses componentes, mas são utilizados, que é o Prometheus, OpenTelemetry, etc. Aqui tem uma legendinha, então, né? O component, que é o nosso componente aqui dentro, mas se você olhar aqui, é external container, ou seja, esse cara aqui é um container.

06:55

Isso aqui é um container. Perceba que eu não estou mostrando os componentes do Redis, não estou mostrando os componentes do OpenTelemetry e nem do Prometheus, tá? Eu estou, na realidade, mostrando os componentes apenas do meu RateLimiter, que está dentro de um serviço HTTP. E esse serviço HTTP aqui, nesse caso, é o nosso container.

07:17

Beleza? Então, essa que é a ideia aqui do C3. Mostrar o que tem dentro. Você abre essa caixa aqui, nesse formato, para que você consiga entender. Beleza? E, então, próximo vídeo vamos falar sobre o C4.

## Resumo IA

**Abreviações**  
- **C3**: *Component Diagram* — nível de diagrama de componentes na abordagem C4.  
- **C4**: *Context, Container, Component, Code* — modelo de documentação de arquitetura em quatro níveis.  
- **HTTP**: *Hypertext Transfer Protocol* — protocolo de comunicação usado na web.  
- **API**: *Application Programming Interface* — interface de programação entre componentes ou sistemas.  
- **IP**: *Internet Protocol* — endereço de rede usado para identificar um host.  
- **Redis**: sistema de armazenamento em memória usado como banco/ cache e suporte a operações distribuídas.  
- **Prometheus**: ferramenta de observabilidade e coleta de métricas.  
- **OpenTelemetry**: framework de observabilidade para métricas, logs e traces.  
- **Lua**: linguagem de script usada no Redis para operações atômicas.  
- **FDD**: *Feature Design Doc* — documento de design da funcionalidade.  

**Resumo**  
A aula apresentou o nível C3 do modelo C4, que detalha a estrutura interna de um container já conhecido no nível anterior. Em vez de tratar o serviço HTTP do Rate Limiter como uma caixa preta, o instrutor mostrou como o container é decomposto em componentes, destacando responsabilidades, contratos internos e pontos de acoplamento. A proposta não é redesenhar o sistema, mas tornar explícito como as partes internas colaboram para decidir entre allow e deny, preservando coesão e reduzindo dependências desnecessárias.

Foi explicado que, no C3, apenas o container aberto é detalhado internamente; dependências externas continuam representadas como containers externos. Assim, Redis, Prometheus e OpenTelemetry permanecem fora da decomposição, porque não fazem parte do interior lógico do Rate Limiter. Essa separação mantém a fronteira do container visível e melhora a legibilidade do diagrama, mesmo com mais detalhes.

Entre os componentes internos, o HTTP middleware foi destacado como o ponto central do fluxo, pois intercepta toda requisição, extrai a chave de identificação, chama a API interna do Rate Limiter, interpreta a decisão e escreve os headers de resposta. O Key Extractor foi apresentado como o componente que transforma a requisição em uma chave de rate limiting, podendo usar IP, API key, API token ou tenant, especialmente em cenário multi-tenant. Em seguida, a API pública interna do Rate Limiter foi explicada como um contrato acessível dentro do próprio processo, consumido principalmente pelo middleware, sem depender da implementação concreta.

Também foi abordado o Strategy Engine, responsável por decidir qual algoritmo de limitação será aplicado à requisição corrente. O exemplo citado alterna entre fixed window e token bucket, mostrando que a estratégia influencia diretamente o comportamento do sistema. Por fim, o Storage Adapter foi descrito como a camada que encapsula leitura e atualização do estado, abstraindo se o armazenamento está em memória local com locks por chave ou em Redis com script Lua para garantir atomicidade em ambiente distribuído.

O fluxo interno resumido foi: o HTTP middleware intercepta a requisição, o Key Extractor obtém a chave, o middleware chama a API interna, o Strategy Engine escolhe a estratégia e o Storage Adapter lê/atualiza o estado, e então o middleware retorna allow ou deny junto com os headers apropriados. A aula também enfatizou o uso de grounding no Feature Design Doc para justificar decisões do diagrama, evitando suposições e mantendo o modelo fiel ao documento de design.  

**Pontos de atenção**  
- No C3, decompor apenas o container interno; não detalhar containers externos como Redis, Prometheus ou OpenTelemetry.  
- Manter a fronteira do container explícita para não confundir o que está dentro com o que é dependência externa.  
- O HTTP middleware é o orquestrador do fluxo, mas não deve concentrar toda a lógica de negócio.  
- A extração da chave é crítica: pode variar por IP, API key, token ou tenant, especialmente em ambiente multi-tenant.  
- A API pública interna não é uma API externa; é um contrato interno estável entre componentes do mesmo processo.  
- Centralizar a escolha da estratégia no Strategy Engine evita espalhar condicionais pelo middleware e pelo acesso ao estado.  
- Fixed window e token bucket têm comportamentos diferentes, principalmente em bordas de janela e picos de tráfego.  
- O Storage Adapter deve isolar os detalhes de persistência e sincronização da lógica de negócio.  
- Se usar Redis em ambiente distribuído, garantir atomicidade com script Lua.  
- Se usar memória local, considerar locks por chave para evitar concorrência incorreta.  
- Justificar elementos do diagrama com o Feature Design Doc para evitar alucinação e manter fidelidade ao design aprovado.