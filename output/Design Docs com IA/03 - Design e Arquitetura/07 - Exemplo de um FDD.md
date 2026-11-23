Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17058)

## Resumo da aula

O FDD desce do desenho arquitetural para comportamento verificável. Retomando o rate limiter já definido no HLD, o foco agora deixa de ser a topologia geral e passa a ser a padronização de como cada microsserviço aplica limites, expõe contratos e reage a falhas. Esse recorte técnico existe porque inconsistência entre serviços produz sobrecarga, integração confusa e implementação divergente. Um SDK embutido em cada serviço resolve isso ao centralizar a lógica in-process e delegar o estado para Redis ou memória local.

Objetivos técnicos transformam intenção em requisitos de implementação: API pública estável, integração por middleware HTTP, suporte a fixed window e token bucket, telemetria nativa, baixa latência e fallback open. O escopo delimita o que a feature realmente entrega, como suporte a Redis Cluster, memória local e geração de headers, e também o que fica de fora, como autenticação, gestão de políticas e estratégias alternativas. Essa separação evita que a implementação absorva responsabilidades que pertencem a outros componentes. Em FDD, exclusão explícita é tão importante quanto funcionalidade incluída.

A API pública precisa expor contratos concretos, não apenas a ideia de “aplicar rate limiting”. Check representa a operação de decisão síncrona: recebe o contexto da requisição e retorna uma Decision com campos observáveis, como permitido ou bloqueado, quantidade restante e retry_after. Middleware encapsula esse mesmo processo no pipeline HTTP, convertendo a decisão em continuação da requisição ou resposta 429. A Decision existe para separar cálculo interno de efeito externo, o que facilita teste, reuso e consistência entre integração programática e integração via HTTP.

Headers como RateLimit, RateLimit-Reset e Retry-After precisam ter semântica explícita, porque clientes dependem deles para implementar backoff, exibir limites e reagir a bloqueios. O FDD fixa não só quais headers existem, mas o significado operacional de cada valor: quanto resta, quando a janela reinicia e quanto tempo esperar antes de tentar de novo. Essa definição reduz ambiguidade entre serviços e impede que cada implementação publique convenções incompatíveis. Em uma feature de infraestrutura, contrato de header é parte da API pública.

Retomando as estratégias já escolhidas, o FDD não reabre a decisão arquitetural; ele especifica como elas se comportam na interface e no runtime. Em fixed window, a contagem é agrupada por janela discreta e o reset acompanha esse limite temporal. Em token bucket, há recarga contínua por rate até um teto de burst, permitindo absorver rajadas controladas sem perder enforcement. A utilidade do documento está em tornar essas diferenças implementáveis e testáveis, inclusive nos headers e nos exemplos de uso.

O padrão options organiza configuração incremental sem explodir construtores com muitos parâmetros posicionais. Em vez de uma assinatura rígida e frágil, a criação do rate limiter recebe opções composáveis para storage, estratégia, credenciais, pool e comportamento operacional. Esse formato funciona como um builder idiomático: cada opção altera a configuração final de forma explícita e extensível. Para uma feature com múltiplos modos de execução, options melhora legibilidade, compatibilidade futura e ergonomia de uso.

Validação no construtor impede que uma instância inválida exista em runtime. Ao criar o rate limiter, o código precisa verificar se os parâmetros da estratégia são coerentes, se combinações obrigatórias foram fornecidas e se o modo selecionado possui configuração suficiente para operar. Isso desloca erro de produção para erro de inicialização, que é mais barato de detectar e corrigir. Em um componente de infraestrutura, falhar cedo é preferível a aceitar configuração inconsistente e produzir comportamento imprevisível.

Redis e memória local não são apenas implementações intercambiáveis; cada modo define um comportamento operacional distinto. Redis atende o cenário distribuído, no qual múltiplas instâncias precisam compartilhar estado e aplicar o mesmo limite global. Memória local serve para desenvolvimento ou instâncias isoladas, com a consequência explícita de perder estado ao reiniciar pod ou container. O FDD precisa registrar essa diferença para evitar adoção incorreta de um modo local em cenários que exigem coordenação distribuída.

Concorrência é um problema central em rate limiting porque múltiplas requisições podem disputar o mesmo contador ao mesmo tempo. Scripts Lua em Redis resolvem isso ao executar leitura, cálculo e atualização como uma operação atômica no servidor, evitando condições de corrida entre clientes concorrentes. Essa escolha protege a correção do limite sem exigir múltiplos round-trips frágeis. Além de consistência, ela ajuda a preservar latência em um caminho síncrono e sensível a desempenho.

No modo em memória, atomicidade depende de sincronização local dentro do processo. Um mutex por chave evita que requisições concorrentes atualizem o mesmo identificador de limite simultaneamente, sem serializar desnecessariamente chaves independentes. Isso reduz contenção em comparação com um lock global e preserva paralelismo onde ele é seguro. O FDD precisa explicitar essa decisão porque concorrência correta não é detalhe opcional em um limitador.

Compatibilidade com Go 1.22 e Redis 6.2 delimita o piso técnico da implementação e evita dependência acidental de recursos mais novos. Dependências como Prometheus, OpenTelemetry, Collector, Linux e arquitetura AMD64 ou ARM deixam de ser contexto implícito e viram requisitos verificáveis de build, execução e observação. Esse nível de detalhe importa porque uma feature pode estar correta em código e ainda falhar por incompatibilidade de ambiente. Em FDD, dependência é condição operacional, não nota de rodapé.

Proteção de dados aparece aqui de forma concreta: logs, métricas, tracing e chaves não podem vazar identificadores sensíveis como IP em texto cru. O documento precisa indicar uso de TLS entre aplicação e Redis quando disponível, tratamento seguro de credenciais e cuidado com atributos e spans exportados. Segurança, nesse nível, não é um princípio abstrato; é uma restrição sobre o que pode circular em observabilidade e infraestrutura. Isso evita que um componente de controle operacional introduza exposição indevida de dados.

O fallback open já foi decidido antes; o avanço agora é especificar quando ele dispara e qual efeito observável produz. Se houver falha no backend de limitação e o modo permissivo estiver ativo, a requisição segue, mas o sistema precisa registrar logs, métricas e transições de conectividade para que a operação saiba que o enforcement foi relaxado. Sem essa definição, a feature até continua disponível, mas o comportamento fica opaco e difícil de auditar. Fallback útil é fallback explicitamente operacionalizado.

Observabilidade aqui deixa de ser preocupação arquitetural genérica e vira contrato operacional do componente. Métricas precisam cobrir decisões, erros, fallback e desempenho; logs estruturados precisam registrar eventos relevantes sem expor dados sensíveis; tracing precisa definir atributos e spans que permitam localizar gargalos e falhas. Esse detalhamento é o que torna o comportamento depurável em produção. Um FDD bom não apenas diz que haverá telemetria, ele define o que será observável.

Critérios de aceite convertem o documento em checklist verificável para implementação. Contratos funcionando, testes passando, desempenho sob carga validado e resiliência confirmada são sinais objetivos de que a feature está pronta para uso. Isso reduz discussão subjetiva sobre “estar pronto” e alinha desenvolvimento, teste e revisão técnica na mesma referência. Quando o FDD chega a esse nível, ele já serve como ponte direta para tarefas de código.

IA acelera a escrita do documento, mas não inventa requisitos corretos que não foram fornecidos ou compreendidos. Se o autor não souber que scripts Lua, mutex por chave, semântica de headers ou modos de fallback são relevantes, o rascunho tende a omitir exatamente os pontos que mais afetam a implementação. Pesquisa técnica profunda amplia o repertório de decisões que podem ser pedidas e revisadas. O valor da IA cresce quando ela recebe contexto técnico real, não quando substitui entendimento do problema.

## Transcrição

00:01

Bom, pessoal, aqui está para a gente, então, um Feature Design Doc do nosso Rate Limiter. Estou querendo seguir a mesma linha para que a gente consiga fazer as coisas se conversarem, tá? Então, se você perceber agora, o contexto e a motivação técnica não é algo tão grande, porque a gente já tem isso desenhado no produto, a gente tem uma visão mais high level,

00:24

mas você vai perceber que o contexto, a motivação, ela acaba sendo mais técnica. Olha só, os micro-serviços da plataforma tratam limitação de requisições de maneiras diferentes, o que gera inconsistência, risco de sobrecarga, recursos compartilhados, um SDK embutido em cada serviço resolve o problema de centralizar a lógica de rate limiting dentro do processo. Ele decide localmente, persistindo o estado no Redis em modo distribuído, em memória local, modo isolado, isso garante baixo acoplamento, performance e tal.

00:54

Já deu uma clareza pra mim muito grande. Perceba que eu não estou falando daquele microserviço X, do que motivou a criação lá pra área de produto, nada disso. Se você perceber, aqui é o aspecto mais técnico mesmo, né? Então, aqui ó, objetivos técnicos. Oferecer uma API pública estável pra checagem de limites.

01:12

via integração com o Midway HTTP, suportar estratégias de janela fixa e token bucket com semântica de headers opções configuráveis, permitir execução em modos Storage e Redis e Memory, garantir baixa latência e atomicidade com scripts Lua no Redis e sincronização por chave memória,

01:30

promover telemetria nativa com métricas, logs estruturados e tracing, suportar modo permissivo, ou seja, fallback open para evitar falhas catastróficas em disponibilidades no back-end, tá? Escopos e exclusões. Olha aqui, ó. Middleware HTTP em Go em lógica em process, estratégia janela fixa e token bucket com semântico uniforme,

01:50

suporte a Redis Cluster e memória local, integração com Prometheus e OpenTelemetry, geração dos headers tal, excluído, autenticação, autorização, gestão de políticas, estratégias, outras estratégias de Slide Window, GCRA, Leak Bucket, adaptativas, etc. Edge, CNN, Rate Limiting, WAF,

02:10

a parte de Firewall, o Web Firewall que a gente tem, persistência durável obrigatória no Redis, que é EOF ou RDB nesse caso, e aqui os fluxos e diagramas detalhados. Então, não trouxe aqui diagramas específicos nessa versão,

02:27

Mas, de forma geral, eu estou colocando quais são a parte conceitual desses fluxos que acabam acontecendo. Existem dois caras principais, que é o fixer do window e o token bucket aqui para a gente. Ou seja, recarga contínua de tokens, que é o rate, até um teto, que é o burst, para evitar aquele pico forte mesmo dentro de um limite. E aqui, se você olhar agora, eu já tenho mais detalhes mais específicos. Olha só, interface pública, rate limiter com check e com middleware, decision,

02:57

Está permitindo quanto ainda tem, retry after, de quanto tempo da duração, a parte de semântica dos headers, rate limit, reset, retry after aqui pra gente. Exemplos claros, sucintos de como trabalhar com fixer do window, com tucking bucket, se você olhar.

03:18

Opções, configuração e opções, a linguagem é 1.22 do Go, armazenamento com Redis 6.2, para conseguir pegar, inclusive, sistemas mais antigos, modo de memory para desenvolvimento local em instâncias isoladas, porque em memória, se reiniciar o pod, o container, ele zera as informações. O Docker, que a gente pode fazer, inclusive, por conta do Redis, o Docker Compose para desenvolvimento,

03:44

a segurança, falar que vai trabalhar com TLS, mútuo ou TLS, entre o Redis e a aplicação, quando disponível, credenciais do Redis, o pool é configurável em relação ao do cliente no Redis, aqui são as principais opções de configuração do rate limiting, independente se você trabalha com Go ou não, normalmente a gente vai trabalhando com options, onde a gente vai trabalhando como se fosse um builder,

04:08

onde nós vamos falando cada opção que a gente quer na hora de a gente configurar. E aí a gente passa as configurações aqui em relação a Storage e Config, se você vai usar Redis ou não. Se for usar Redis, ele vai trazer as configurações usando o modo Redis aqui para a gente.

04:25

Validações recomendadas. Toda vez que eu vou dar um new, ele vai fazer a validação para garantir que os parâmetros daquela estratégia todos estejam parecidos. Então, isso é importante. Caso de erro e fallback. Problemas de concorrência e atomicidade. Então, isso é um grande problema, que é concorrência na hora que você está trabalhando com rate limiting, porque tem muita

04:47

chamado que acontece ao mesmo tempo, né? Garantia comportamental, atomicidade no Redis, aqui tá dando uma... como que vai trabalhar, então o Redis vai usar um script Lua pra conseguir fazer essa parte de concorrência com a gente, é bem rápido trabalhar dessa forma também, aqui vai falar como que vai trabalhar com a parte atômica na memória, usando o mutex no Go, como que vai ser em janela fixa, como que é um token bucket, então se você perceber, galera,

05:13

é um documento bem detalhado de feature mesmo, né? O que vai ter, o que não vai ter, quais são os principais erros que vão acontecer, quais são, a pontos gerais, como que eu consigo fazer o tratamento desse tipo de erro, né? Modo permissivo, ou seja, dá problema quando o fallback está open true, a gente vai deixar todo mundo acessar, né? Como é que vai ser o log desse documento? Quando volta a conectividade, o que acontece? Quando que vai ser?

05:39

Quais são as principais métricas que a gente vai utilizar em relação a tudo isso? Como que vai ser estruturado os logs desse cara? Como que vai funcionar o tracing? O que que vão vir nos atributos e nos spans? Como que vai ser a proteção de dados para evitar que a gente tenha o IP do cara vazado nos nossos logs e coisas desse tipo? Quais são as dependências que a gente tem? Então, Go, Redis, Prometheus, OpenTelemetry, o Collector que ele vai trabalhar,

06:08

O Linux, qual ambiente? AMD64 ou ARM? Critérios de aceitação. E aqui são pontos importantes. Ou seja,

06:18

Quando eu tiver com os contratos tudo bem feito e funcionando, quando esses meus testes estiverem passando, quando eu fizer esses testes de performance e carga, quando ele estiver trabalhando e funcionando bem com essa parte de resiliência, eu acredito que a minha feature vai estar funcionando. E aqui, principais riscos e como eu mitigo esses riscos. E aqui, anexos e referências, ou seja, existem diversos rate limitings na internet.

06:47

Então, durante a pesquisa que eu fiz, ele trouxe aqui para mim diversos links que eu posso utilizar como base para eu conseguir desenvolver esse cara aqui para a gente, tá? Então, é basicamente isso. Tudo isso, galera, gerado com o IA, mas, obviamente, eu tinha que entender mais sobre Rate Limiting, eu tinha que entender dessas estratégias, eu tinha que saber que existem formas diferentes de trabalhar com Fallbacks.

07:13

Então, se você perceber... Ah, eu nem sabia que dava para trabalhar com scripts Lua no Redis. Então, você consegue perceber que uma coisa é ter o documento. E a IA pode gerar seu documento, mas raramente ela vai conseguir gerar um documento baseado naquilo que você não pediu para ela ou naquilo que você não conhecia.

07:32

E é por isso que, muitas vezes, fazer uma pesquisa, Deep Research, para você entender mais sobre o assunto, vai ajudar muito você a conseguir criar esses tipos de documento. Mas, novamente, a IA não vai fazer milagre. Se você não souber o que tem que ser feito, se você for aquela pessoa que vai criar esse tipo de documento e não tem o conhecimento para conseguir especificar essa feature, a gente pode tentar fazer o que for, você não vai conseguir gerar esse produto porque você não conhece sobre esse produto.

08:01

A ideia aqui é que a gente tem esses documentos para que o time converte, para que a IA consiga ler, para que todo mundo fique na mesma página, mas, obviamente, a pessoa que vai gerar esse documento tem que entender do que vai ser feito. E por isso que a gente vê que esse documento acaba indo um pouco mais baixo nível.

08:21

Se você percebe, ele é mais baixo nível. Tem mais detalhes de implementação. Fala quais são as métricas que eu tenho que olhar, fala como é que vai ser os meus logs, quais são as minhas dependências, as partes de compatibilidade, os detalhes maiores da minha interface de como que eu vou fazer. Então, se você olhar, é bem mais detalhado do que...

08:42

aquele high level design que a gente fez. Mas, ainda assim, ele é um documento de feature. A partir desse documento, na minha opinião, eu já consigo começar a desenvolver uma feature. Mas, dependendo da empresa, a gente pode ir mais a fundo e criar um low level

09:00

Document, que é esse documento de low level, aí ele traz realmente os detalhes dos detalhes da implementação. Honestamente, eu não vejo muito hoje em dia documentos de tão baixo nível sendo desenvolvidos.

09:17

Porque principalmente com documentos de mais alto nível, ou até mesmo nesse nível que a gente acabou de olhar, já é bem suficiente, na maioria das vezes, de você começar a desenvolver a sua feature. E mesmo com um documento desse tipo, se você tiver com um workflow legal de trabalho para utilizar com o IA, você já consegue ir definindo em relação às tarefas, o que deve ser feito, o que não deve ser feito, os detalhes mais de baixo nível.

09:43

Mas, dependendo da empresa, você pode precisar de um documento de baixo nível, mas eu acho que não é nem o nosso foco aqui. Eu acho que o ponto importante é, se você chegar a esse nível de documento aqui, de Feature Design Doc, eu acho que já é uma super...

09:59

grande caminho para você desenvolver e sair criando qualquer parte do seu sistema. E, principalmente, se você já existe um sistema e você quer criar uma nova feature. Imagina que você vai criar uma nova feature num CodeBase que já existe, que o seu time está acostumado. Com certeza, com um documento desse, já é um baita ponto de partida para o seu time começar a desenvolver. Obviamente, pessoal,

10:24

Eu garanti que esse meu documento aqui não fosse gigante, principalmente por conta do nosso curso. Mas, obviamente, dependendo do tamanho da feature que você vai desenvolver, esses documentos podem ficar realmente bem grandes, mas o importante é que ele realmente tenha as informações importantes sobre aquilo que vai desenvolvido, principalmente no lado mais técnico aí. Beleza? No próximo vídeo, eu vou mostrar também para você prompts que ajudam você a gerar esse tipo de documento também.

## Resumo IA

**Abreviações**
- **FDD** — *Feature Design Doc* (Documento de Design de Feature)
- **HLD** — *High Level Design* (Design de Alto Nível)
- **SDK** — *Software Development Kit* (Kit de Desenvolvimento de Software)
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)
- **HTTP** — *Hypertext Transfer Protocol* (Protocolo de Transferência de Hipertexto)
- **Redis** — Banco de dados em memória usado como armazenamento e coordenação distribuída
- **Redis Cluster** — Modo de operação distribuído do Redis
- **GCRA** — *Generic Cell Rate Algorithm*
- **WAF** — *Web Application Firewall* (Firewall de Aplicação Web)
- **EOF** — *End of File* (Fim de Arquivo)
- **RDB** — *Redis Database Backup* (snapshot/persistência em formato de dump)
- **TLS** — *Transport Layer Security* (Segurança da Camada de Transporte)
- **Go** — Linguagem de programação Go
- **Prometheus** — Ferramenta de métricas e monitoramento
- **OpenTelemetry** — Framework de observabilidade para métricas, logs e tracing
- **ARM** — *Advanced RISC Machine* (arquitetura de processador)
- **AMD64** — Arquitetura de processador x86-64 da AMD

**Resumo**
A aula mostrou como evoluir o desenho arquitetural de um rate limiter para um Feature Design Doc, detalhando o comportamento verificável da feature em vez da visão apenas de alto nível. O foco passou a ser padronizar como cada microsserviço aplica limitação de requisições, expõe contratos e reage a falhas, evitando inconsistências entre serviços. A proposta central foi um SDK embutido em cada serviço, com lógica in-process e estado persistido em Redis no modo distribuído ou em memória local no modo isolado.

O instrutor estruturou o documento com objetivos técnicos, escopo, exclusões e fluxos principais. Entre os objetivos estavam: API pública estável para checagem de limites, integração via middleware HTTP, suporte a fixed window e token bucket, telemetria nativa, baixa latência e fallback open. O escopo incluía Redis Cluster, memória local e geração de headers, enquanto excluía autenticação, autorização, gestão de políticas e outras estratégias como sliding window, GCRA e leak bucket. Também foi reforçado que, em um FDD, dizer explicitamente o que não faz parte da feature é tão importante quanto definir o que faz.

Na parte de interface, a aula destacou a operação `Check`, que retorna uma `Decision` com informações observáveis como permissão, quantidade restante e `retry_after`, além do middleware HTTP que transforma essa decisão em continuação da requisição ou resposta 429. Os headers `RateLimit`, `RateLimit-Reset` e `Retry-After` foram tratados como parte do contrato público, com semântica operacional clara para apoiar clientes em backoff e tratamento de bloqueios. O comportamento das estratégias também foi detalhado: no fixed window a contagem é agrupada por janela discreta; no token bucket há recarga contínua até um teto de burst para absorver rajadas controladas.

O instrutor explicou ainda o padrão options para organizar a configuração incremental da feature, evitando construtores com muitos parâmetros e facilitando evolução futura. A validação no construtor foi apontada como prática essencial para impedir que instâncias inválidas existam em runtime, deslocando erros para a inicialização. Em relação ao armazenamento, foi enfatizada a diferença operacional entre Redis e memória local: o primeiro atende cenários distribuídos e o segundo é útil para desenvolvimento ou instâncias isoladas, com a limitação de perder estado ao reiniciar o processo.

A concorrência recebeu atenção especial, pois múltiplas requisições podem disputar o mesmo contador simultaneamente. No Redis, a atomicidade é garantida por scripts Lua que executam leitura, cálculo e atualização de forma atômica. Em memória, a sincronização é feita com mutex por chave, evitando condições de corrida sem bloquear todo o sistema. Também foram citadas as versões mínimas de Go 1.22 e Redis 6.2, além de dependências como Prometheus, OpenTelemetry, Collector e suporte a Linux em AMD64 ou ARM.

Por fim, a aula tratou de segurança, fallback open, observabilidade e critérios de aceite. Foi reforçado que logs, métricas, tracing e chaves não devem expor dados sensíveis, como IP em texto cru, e que o uso de TLS e credenciais seguras é parte do contrato operacional. O fallback permissivo deve ser acionado em falhas do backend, mas com sinais claros em logs e métricas para auditoria. O documento termina com critérios objetivos de pronto: contratos funcionando, testes passando, desempenho validado e resiliência confirmada. Também foi enfatizado que a IA pode acelerar a redação do FDD, mas depende de conhecimento técnico prévio e pesquisa adequada para não omitir requisitos críticos.

**Pontos de atenção**
- Diferenciar claramente o que é decisão arquitetural já tomada no HLD do que precisa ser especificado no FDD.
- Evitar inconsistência entre microsserviços; a lógica de rate limiting deve ser padronizada.
- Definir contratos explícitos de API, especialmente `Check`, `Decision` e middleware HTTP.
- Tratar os headers como parte da API pública, com semântica operacional bem definida.
- Especificar claramente o comportamento de `fixed window` e `token bucket`, incluindo exemplos e efeitos observáveis.
- Usar o padrão options para configuração extensível e legível, evitando construtores frágeis.
- Validar parâmetros no construtor para falhar cedo e impedir instâncias inválidas.
- Não confundir modos de armazenamento: Redis é para coordenação distribuída; memória local perde estado ao reiniciar.
- Garantir atomicidade em concorrência:
  - Redis: scripts Lua.
  - Memória: mutex por chave, não lock global.
- Deixar explícitas as versões e dependências mínimas do ambiente para evitar incompatibilidades.
- Considerar segurança e privacidade na observabilidade: não vazar IP, credenciais ou dados sensíveis em logs, métricas e tracing.
- Definir claramente quando o fallback open é acionado e como isso aparece em telemetria e logs.
- Não incluir responsabilidades fora do escopo, como autenticação, autorização e gestão de políticas.
- Usar critérios de aceite objetivos para reduzir ambiguidade sobre pronto ou não pronto.
- Não depender da IA para “adivinhar” requisitos; pesquisa e entendimento técnico são necessários para produzir um FDD útil.