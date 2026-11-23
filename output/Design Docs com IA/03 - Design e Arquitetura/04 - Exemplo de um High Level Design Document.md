Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17055)

## Resumo da aula

Rate limiting entra aqui como exemplo recorrente porque é um problema conhecido pelos desenvolvedores, mas nem sempre compreendido do ponto de vista de implementação e desenho arquitetural. O HLD fixa o objetivo do sistema: um SDK embutido nos microserviços, escrito em Go, capaz de limitar acesso com base em API key, IP e plano do cliente. Esse recorte já mostra o papel do documento: transformar uma necessidade operacional em responsabilidades, metas e fronteiras técnicas sem descer ao código.

Metas não funcionais moldam a arquitetura antes de qualquer detalhe de implementação. Exigir P95 inferior a 5 ms para operações com Redis significa que 95% das verificações do limitador precisam terminar abaixo desse tempo, o que restringe escolhas de topologia, armazenamento e número de hops na requisição. Essa meta existe porque o rate limiter fica no caminho crítico da chamada HTTP; se ele for lento, toda a plataforma herda essa latência.

O SDK é integrado in-process, funcionando como middleware HTTP antes da lógica de negócio do serviço hospedeiro. Essa decisão reduz acoplamento com um serviço remoto dedicado e evita uma chamada extra de rede para cada requisição, mantendo o controle de acesso no próprio processo da aplicação. O efeito prático é simples: a requisição entra, o middleware consulta identidade e política, decide permitir ou negar, injeta headers e só então a lógica de negócio continua.

Redis aparece como backend de estado porque o limitador precisa de leitura e atualização rápidas, com possibilidade de compartilhamento entre múltiplas instâncias. O processo do microserviço permanece stateless, enquanto os contadores e janelas ficam em Redis ou, em cenários específicos, em memória local. Essa separação permite escalar horizontalmente os serviços sem perder consistência básica do controle distribuído.

Retomando o cenário do rate limiter, as estratégias de fixed window e token bucket aparecem no HLD não para detalhar algoritmo, mas para registrar a direção arquitetural. A primeira é útil para limites por janela temporal fixa; a segunda lida melhor com rajadas e recomposição gradual de capacidade. No documento de alto nível, o importante é explicitar que estratégias diferentes atendem perfis distintos de tráfego e influenciam modelagem de estado e chaves.

Como já visto no HLD, componentes e interfaces públicas aparecem aqui apenas no nível necessário para orientar a solução. O desenho inclui microserviço hospedeiro, SDK de rate limiting, Redis, telemetria e, em produção, eventual orquestração com Kubernetes. Dentro do SDK, o ponto central é um check síncrono que recebe identidade, rota, método e plano, resolve a política aplicável e devolve decisão com metadados como Retry-After e headers de limite.

O fluxo em alto nível começa quando a requisição atinge o serviço e passa primeiro pelo middleware do SDK. Em seguida, a identidade é composta a partir de elementos como API key, tenant, IP, rota e método HTTP; a política correta é resolvida; o estado é consultado em Redis ou memória; e a decisão retorna como permissão ou bloqueio. Se o limite for excedido, o host responde com 429 Too Many Requests; se for aceito, a requisição segue e a telemetria registra métricas, logs e tracing.

A composição das chaves de rate limiting precisa considerar PII porque identificadores como IP e dados de cliente podem vazar informação sensível se forem gravados de forma ingênua. O HLD não define a implementação exata da proteção, mas registra a exigência de não expor diretamente dados identificáveis nas estruturas de estado e observabilidade. Isso importa porque a chave técnica usada para contagem também é um ponto potencial de risco regulatório e operacional.

Hot keys surgem quando muitas requisições concentram leitura e escrita na mesma chave do Redis, criando contenção e degradando latência. Em um rate limiter, isso pode acontecer quando muitos clientes compartilham um mesmo escopo global ou quando a estratégia de chaveamento concentra tráfego demais em poucos identificadores. O HLD precisa registrar esse risco porque ele afeta diretamente a meta de P95 e pode exigir particionamento, granularidade melhor de chave ou revisão de política.

Fallback open significa liberar a requisição quando o mecanismo de limitação falha, por exemplo em indisponibilidade de Redis. Essa é uma decisão arquitetural, não um detalhe de código, porque troca rigor de proteção por continuidade de acesso ao sistema em situações degradadas. O documento precisa explicitar essa escolha para que todos entendam o trade-off: reduz-se o risco de indisponibilidade para usuários legítimos, mas aceita-se exposição temporária a sobrecarga.

Segurança, observabilidade e riscos arquiteturais já fazem parte da estrutura esperada de um HLD; aqui o avanço está em como eles se concretizam no exemplo. Observabilidade inclui métricas, logs, tracing e integração com Prometheus e OpenTelemetry para acompanhar latência, falhas e decisões do limitador. Entre os riscos principais estão Redis indisponível ou particionado, configuração incorreta bloqueando tráfego legítimo, hot keys e exposição de PII.

O documento mostra interfaces como check, contexto, identidade, escopo, decisão, next e render, mas não detalha contratos completos, campos finais nem código. Esse é o limite correto entre arquitetura e implementação: o leitor entende como a solução se organiza, quais decisões foram tomadas e onde estão os riscos, sem confundir o HLD com um Low Level Design. Quando a equipe precisar definir estruturas exatas, contratos e regras operacionais, o próximo passo será um documento de nível mais baixo.

## Transcrição

00:01

Bom pessoal, seguinte, agora eu quero falar especificamente desse high level design. E nesse caso aqui, eu quero utilizar como estudo de caso geral a parte de um rate limiter.

00:16

Por que eu falo tanto de Rate Limiter? Porque de forma geral, é algo que nós desenvolvedores estamos acostumados a mexer, ou nós estamos acostumados a pelo menos entender o que um Rate Limiter faz. Ou seja, ele ajuda, na realidade,

00:33

a colocar um limite de acesso a determinadas APIs e esses limites podem ser atribuídos por diversos tipos de estratégias. Existem muitas estratégias de rate limiting e é isso que acaba diferenciando, às vezes, um profissional que já trabalhou com rate limiting ou não. Normalmente,

00:53

A maioria das vezes que eu percebo é que desenvolvedores normalmente acabam consumindo plataformas que têm rate limiting, mas raramente a gente vê um desenvolvedor que implementa rate limiting e que entenda as principais estratégias. Então, a minha ideia aqui era de trazer duas estratégias, por exemplo, do nosso rate limiter,

01:15

para que a gente consiga não discutir e ir a fundo em Rate Limiting, mas que a gente consiga ver sentido nesses documentos e como eles podem nos ajudar a entender sobre isso. Então, apesar de ser um assunto comum no mundo do desenvolvimento,

01:30

não é tão comum os desenvolvedores entenderem todos os tipos de Rate Limiting. Legal? Então, esse é um ponto importante. Então, aqui nesse caso, esse meu documento de High Level, basicamente ele traz um objetivo muito claro, que é fornecer uma visão clara dos princípios e responsabilidades e metas

01:49

do Rate Limiter embutido, ou seja, ele vai ser um SDK, que vai ser desenvolvido em Go, e ele vai ser integrado diretamente nos microserviços da plataforma. O objetivo é permitir que cada serviço controle o seu Rate Limiting e ele vai ser baseado em chaves de API, endereços de IP, planos de clientes, garantindo previsibilidade e proteção sobre carga. E aqui, olha só que interessante,

02:11

Esse SDK vai implementar as estratégias de janela fixa, ou seja, fixa do window e token bucket, para equilibrar o desempenho de diversos tipos de tráfego, ou seja, ele protege a gente com picos de tráfego e também ele protege a gente também quando a gente quer definir a quantidade de acessos dentro de um determinado limite. Eu não quero entrar em níveis tão

02:37

técnicos, porque o nosso assunto aqui é muito mais sobre o documento e não sobre o rate limiting, mas às vezes é um pouco difícil a gente fugir, né, porque vocês têm que entender esse documento, entender o que ele tem. Se você perceber, olha só, no objetivo é que ele também tem que garantir isolamento entre clientes, a estabilidade da plataforma, picos de carga, baixa latência operacional, daí tem aqui, ó, meta do P95 inferior a 5 milissegundos, ou seja, P95 é que

03:04

95% das requisições consigam ser menores que 5 milissegundos para operações com Redis. Então, já tem uma dica aqui que a gente vai trabalhar com Redis para fazer o controle do nosso Rate Limiting. Além disso, deve ser fácil de integrar, observável, configurável e consistente na operação, tanto com Docker Compose, durante o desenvolvimento.

03:27

E aqui, se você perceber, a gente está trazendo, de forma geral, uma arquitetura geral do sistema. E aqui, basicamente, é o que a gente vai utilizar. Então, está falando aqui que a gente vai trabalhar com o Go como linguagem de programação, onde ele fala que tem concorrência nativa e canais, baixa latência, footprint reduzido de memória. Fala a versão do Go.

03:54

fala como que a gente vai trabalhar com containers para fazer isso, vai ter um container da aplicação, vai ter um container com Redis, e se quiser pode trabalhar com Kubernetes em produção, a biblioteca vai estar vinculada a cada microserviço, vai ser stateless no processo, com o estado no Redis, que pode ser um estado compartilhado, ou em memory local ali na configuração.

04:19

Esse rate limiting pode ficar na memória da aplicação que roda ou no Redis para fazer esse cache distribuído de forma geral. A integração vai ser chamada in-process, ou seja, vai funcionar como middleware HTTP antes da lógica de negócio, nenhuma dependência de rede adicional do Redis vai ser preciso.

04:39

Aí fala que o armazenamento vai ser em Redis ou em Memory, a observabilidade vai trabalhar com métricas, logs de tracing integrado, a stack de serveiro hospedeiro, essas coisas geradas por IA, às vezes em português não sai da melhor forma possível, e que vai ter integração nativa com Prometheus e OpenTelemetry.

04:57

Vai ter prioridades, política de por plano, tipo cliente com premium standard, premium e etc. Cada plano faz com que você tenha um limite diferente, tá? Eu vou ter bibliotecas vinculadas para cada serviço, eu vou ter integrações in-process via midware, antes da lógica, aqui, né? Voltei aqui.

05:15

observabilidade, prioridade de planos. E aqui, pessoal, a gente pode colocar diagrama C4. A gente vai chegar em diagramas nas próximas aulas. Então, somente para que você saiba disso, a gente vai falar de C4. Nesse momento, aqui é um desenho simples de como seria o C4. Aqui seria muito simples mesmo, mas depois a gente fala um pouco mais sobre C4.

05:37

E aqui, componentes. Então, olha só, lembra que é para a gente entender quais são os componentes que a gente tem? Então, eu vou ter no Rate Limiter, no SDK, a gente vai ter um ponto de verificação síncrono que vai permitir ou negar o acesso por rota, por tenant, por IP, por plano. Ele vai resolver políticas baseado nos planos e por escopo global, rota, metro, HTTP, retorna dados com headers com retry after e X-rate limiting, ou seja,

06:05

ele faz com que o seu middleware coloque lá na resposta falando, olha, você pode tentar daqui cinco segundos, o seu limit você chegou em tal momento. E a gente vai ter logs, métricas, logs, etc.

06:20

Aqui a gente tem serviços de host, o middleware vai chamar um check, vai injetar a identidade do cara, pode ser uma API key, tenant, o plan, o IP, o route, o método, ele vai compor os headers e quando der algum rolo, a gente vai ter o header com o erro 429, é que o limite foi atingido.

06:40

vai falar sobre o Red Cluster, observabilidade, e aqui, fluxo de requisição em alto nível. Então, entrada, o request atinge o serviço, bate no middleware do SDK, identidade ele acaba verificando, baseado nesses aspectos aqui. A gente tem a política de resolver, daí o estado pode ser em Reds in Memory, a decisão vai poder permitir ou não, e trazer metadados para conseguir retornar como

07:06

como resposta, a resposta do host vai adicionar isso, a telemetria vai incrementar as métricas e as falhas, a gente pode ter inclusive falhas que a gente chama fallback open, é que quando dá um problema, sei lá, de comunicação com Redis, ele vai liberar geral todo mundo pra ninguém perder acesso ao sistema, né? Então é uma forma de fallback.

07:26

Modelo de estado, modelo de dados. Então, se você olhar aqui, existem várias formas de você trabalhar com dados, né? Por exemplo, pode ser uma modelagem de um banco de dados. Nesse nosso caso aqui, uma das coisas mais importantes é como que isso vai ser modelado no Redis, como que as chaves vão trabalhar, baseado em quais estratégias a gente vai utilizar.

07:46

Quais são campos que são importantes? Quais são o nível de prioridades? Então, se você olhar aqui, basicamente, ele está falando como que a gente vai mapear os dados que a gente vai utilizar para cada estratégia. Como é que a gente trabalha com prioridade? Como é que a gente trabalha com a PII, que é para proteger dados identificáveis dos clientes, para não botar ali para que todo mundo possa ver o IP aqui do usuário ou coisas desse tipo, em relação à proteção de dados mesmo.

08:16

aí a gente tem interfaces públicas. Então, se você perceber, olha só, eu estou trazendo aqui interfaces públicas, ou seja, vai ter um check, vai ter um contexto, vai ter uma identidade, vai ter o escopo e vai ter uma decisão. O midware vai ter o next e o render. Se você percebeu o que está acontecendo aqui, ele está trazendo em alto nível para mim quais são as interfaces públicas, os exemplos, como que as coisas vão funcionar. Mas perceba que ele não mostra aqui para mim nenhum detalhe de implementação de como que

08:44

serão todos os dados, os campos e etc, tá? Mas eu tenho ideia aqui de como que vai funcionar.

08:51

Como que eu trabalho com escalabilidade? Então ele fala, olha, pra trabalhar com baixa latência, eu tenho que ter um local, mais um round trip pro Redis, eu vou ter uma meta de 1 a 5 milissegundos sobre a carga nominal. Então, perceba, né, tem sharing hotkeys que podem acontecer no Redis, eu não quero entrar nesses detalhes, mas se você perceber, olha só, segurança, modelo de ameaça alto nível, abuso por chaves, replay de requests,

09:15

floods, GPI, etc. Identidade, transporte, autorização, auditoria. Como é que funciona a observabilidade? Ele traz aqui os service levels, indicators que eu preciso em relação à latência, o que eu preciso ver, como que eu configuro os meus alertas, quais são minhas estratégias de tracing, quais são os atributos que eu uso, como que eu vou trabalhar nos logs,

09:36

em relação para a gente suprimir. Quais são os principais riscos? O que acontece se o Redis estiver indisponível ou particionado? O que acontece se tiver uma configuração incorreta bloqueando? O que acontece com hotkeys caso muita gente está lendo a mesma key lá no Redis, então a gente acaba tendo uma hotkey? Não quero também entrar nesses detalhes técnicos. Divergência temânica.

10:00

e a exposição de PII, ou seja, dados protegidos que não devem existir. Então, se você bater o olho aqui, você consegue, de forma geral, entender o que esse sistema faz. É um Rate Limiting que vai trabalhar com fixa do Window, Tucking Bucket, que vai trabalhar com Redis, com Go, vai rodar com Middleware,

10:20

Ele vai ter observabilidade, vai ter aqui alguns contratos mais públicos, vai ter um fluxo de requisição que eu entendi a ideia, entendi como é que ele vai organizar os dados ali pra mim, como é que vão ser as principais interfaces, como é que eu pretendo escalar pra esse cara, como é que eu penso em segurança, como que eu penso em observar, como que eu penso nos principais riscos e como que eu resolvo esses riscos. Então, isso aqui, galera, é um documento de high level.

10:47

Perceba que ele fala meio que tudo, mas, ao mesmo tempo, ele não fala nada tão específico de como isso vai ser implementado. E por isso que ele é um documento de high level. Eu, como um arquiteto, olhando isso, consigo entender o que vai ser feito. Eu entendo o que vai acontecer. Eu não pensei ainda em níveis tão detalhados, mas já deu para ter uma boa ideia do que vai acontecer. Então, por isso que eu digo, muitas vezes, é necessário que você tenha um documento desse antes,

11:16

de você chegar em um nível de especificação maior, de feature, ou até mesmo num low-level design, tá? Então, por isso que esse documento é importante, mas, novamente, dependendo da empresa ou dependendo de quem vai gerar esse documento, às vezes você pode ir direto para outro, você já pode ir para um documento mais específico, né? Então, muito disso depende de quantos layers, né, que a sua empresa tem na hora de definição dos projetos. Vai depender muito disso.

11:45

mas eu acho que deu para você pegar a ideia de como que esse cara aqui funciona. Maravilha? No próximo vídeo, eu vou trazer aqui também ideia de prompt que você pode utilizar para gerar esses documentos, mas eu tenho todas as considerações do mundo na hora de você querer gerar um documento desses somente através de prompts que acabam te entrevistando. Então, a gente vai falar disso no nosso próximo vídeo.

## Resumo IA

**Abreviações**
- SDK — *Software Development Kit* (kit de desenvolvimento de software)
- API — *Application Programming Interface* (interface de programação de aplicações)
- IP — *Internet Protocol* (protocolo de internet)
- P95 — percentil 95
- Redis — banco de dados em memória usado como armazenamento de alta performance
- HTTP — *Hypertext Transfer Protocol* (protocolo de transferência de hipertexto)
- HLD — *High Level Design* (projeto de alto nível)
- LLD — *Low Level Design* (projeto de baixo nível)
- C4 — modelo de diagramas de arquitetura em quatro níveis
- PII — *Personally Identifiable Information* (informações pessoalmente identificáveis)
- HTTP 429 — código de status “Too Many Requests”
- retry-after — cabeçalho HTTP que informa quando tentar novamente
- middleware — componente intermediário no processamento de requisições
- DNS — não citado na aula
- Go — linguagem de programação Go
- Docker Compose — ferramenta para definição e execução de múltiplos contêineres
- Kubernetes — plataforma de orquestração de contêineres
- Prometheus — sistema de coleta e monitoramento de métricas
- OpenTelemetry — framework para observabilidade
- tenant — locatário/cliente lógico em ambiente multi-tenant
- API key — chave de acesso de API
- token bucket — algoritmo de limitação por acúmulo e consumo de tokens
- fixed window — estratégia de limitação por janela fixa

**Resumo**
A aula apresenta o uso de um documento de HLD para descrever, em alto nível, um rate limiter embutido como SDK em microserviços, escrito em Go. O objetivo é controlar acesso a APIs com base em API key, IP, tenant e plano do cliente, garantindo proteção contra sobrecarga, previsibilidade de uso e isolamento entre clientes. O instrutor destaca que o papel do HLD é definir responsabilidades, metas, fronteiras técnicas e riscos, sem entrar no código nem nos contratos detalhados de implementação.

A arquitetura proposta coloca o SDK em processo, funcionando como middleware HTTP antes da lógica de negócio, evitando uma chamada adicional de rede para um serviço remoto de rate limiting. O estado do limitador pode ficar em Redis ou, em cenários específicos, em memória local, enquanto os microserviços permanecem stateless. Essa abordagem favorece escalabilidade horizontal e baixa latência, que é reforçada pela meta não funcional de P95 inferior a 5 ms para operações com Redis. O documento também menciona o uso de containers com Docker Compose no desenvolvimento e, opcionalmente, Kubernetes em produção.

Do ponto de vista funcional e estrutural, o HLD registra estratégias como fixed window e token bucket, não para detalhar algoritmos, mas para indicar como diferentes perfis de tráfego serão tratados. O fluxo resumido começa com a requisição entrando no serviço e passando pelo middleware do SDK, que compõe a identidade com dados como API key, tenant, rota, método HTTP e IP, resolve a política aplicável, consulta o estado e toma a decisão de permitir ou negar. Se a requisição for bloqueada, o sistema responde com 429 Too Many Requests e headers como Retry-After e informações de limite; se for aceita, a lógica de negócio prossegue e a telemetria registra métricas, logs e tracing.

A aula também mostra que o HLD deve antecipar preocupações de segurança, observabilidade e operação. A modelagem de chaves no Redis precisa considerar PII para evitar exposição indevida de dados identificáveis, enquanto a observabilidade deve incluir métricas, logs, tracing e integração com Prometheus e OpenTelemetry. Entre os riscos arquiteturais destacados estão indisponibilidade ou partição do Redis, configuração incorreta bloqueando tráfego legítimo, hot keys causando contenção e exposição de PII. Como estratégia de degradação, o documento registra o fallback open, no qual a requisição é liberada caso o mecanismo de limitação falhe, priorizando disponibilidade em vez de bloqueio rígido.

Por fim, o instrutor enfatiza o limite correto entre arquitetura e implementação: o HLD apresenta componentes, interfaces públicas e o fluxo principal, mas não define campos finais, regras exatas nem estruturas de código. Ele serve para orientar a solução, alinhar entendimento entre times e preparar o terreno para documentos mais detalhados, como um LLD, quando a equipe precisar especificar contratos e implementação.

**Pontos de atenção**
- O HLD deve definir objetivo, responsabilidades e fronteiras técnicas, mas sem descer para detalhes de código.
- A meta de P95 abaixo de 5 ms é crítica porque o rate limiter está no caminho crítico da requisição.
- Usar o SDK in-process como middleware reduz latência e evita uma chamada extra de rede.
- Redis é escolhido pela necessidade de leitura e atualização rápidas com compartilhamento entre instâncias.
- O estado dos contadores deve ficar fora dos microserviços, que permanecem stateless.
- Fixed window e token bucket devem ser tratados como estratégias arquiteturais, não como implementação detalhada.
- A composição das chaves deve considerar PII para não expor dados sensíveis como IP e identificadores de cliente.
- Hot keys no Redis podem causar contenção e degradar a latência; a modelagem de chaves precisa mitigar isso.
- Fallback open é uma decisão de trade-off: preserva disponibilidade, mas reduz proteção contra sobrecarga.
- Observabilidade precisa incluir métricas, logs, tracing e integração com Prometheus e OpenTelemetry.
- O documento deve registrar riscos como Redis indisponível ou particionado, configuração incorreta, hot keys e vazamento de PII.
- Interfaces públicas como check, identity, scope, decision, next e render devem ser descritas em alto nível, sem contratos completos.
- O HLD é suficiente para entendimento arquitetural, mas o detalhamento de estruturas e regras deve vir em um documento de nível inferior, como LLD.