Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16972)

## Resumo da aula

Retomando a lógica do PRD de feature, o rate limiter agora aparece em um cenário mais técnico: um serviço centralizado usado por todos os microserviços da plataforma. Ele existe para controlar volume de requisições por chave de API e por IP, reduzindo sobrecarga e protegendo disponibilidade. Quando essa decisão é centralizada, o comportamento de limitação deixa de ficar espalhado entre serviços e passa a ser governado de forma consistente.

Os objetivos já conhecidos no PRD de feature ganham aqui uma forma operacional muito clara: reduzir indisponibilidade, limitar abuso e preservar desempenho. Isso se traduz em métricas como tempo de indisponibilidade abaixo de um minuto, proporção de respostas 429 e latência P95 inferior a 150 ms. A utilidade prática dessas métricas é transformar proteção de plataforma em algo verificável, e não apenas em intenção genérica de robustez.

O escopo inclui limitação por chave de API e por IP, controle de burst e uso de janela deslizante, além do retorno de bloqueio com status 429. Fora do escopo ficam capacidades adjacentes, como fila de prioridade, console em tempo real, API administrativa e operação multi-região. Essa delimitação impede que uma feature de proteção de tráfego se transforme prematuramente em plataforma completa de governança.

Quando o PRD explicita o fluxo principal — cliente envia requisição, o rate limiter identifica o chamador, verifica o limite e decide permitir ou bloquear — a feature deixa de ser apenas uma lista de requisitos soltos. Esse encadeamento melhora entendimento humano e também fornece contexto sequencial para IA, que passa a inferir menos e operar mais sobre comportamento declarado. Fluxos alternativos e erros previstos completam essa leitura ao mostrar o que acontece quando o limite já foi atingido.

Headers padrão de rate limit tornam a limitação observável para os clientes que consomem a API. Em vez de receber apenas um bloqueio opaco, o consumidor passa a ter sinais explícitos sobre limite, uso e eventual tempo de espera, o que melhora adaptação do cliente e reduz comportamento agressivo por desconhecimento. Em um PRD consumido por times e agentes, registrar esses headers evita ambiguidade sobre o contrato de resposta.

Controle de burst lida com picos curtos de tráfego sem tratar todo excesso como abuso imediato. A janela deslizante distribui a contagem ao longo do tempo de forma mais precisa do que janelas fixas, reduzindo efeitos artificiais de borda e tornando a limitação mais justa. No exemplo, essa escolha mostra que o comportamento do rate limiter não é apenas “contar requisições”, mas definir uma política temporal coerente com uso real.

Redis aparece como storage principal para contadores porque oferece operações rápidas e adequadas para controle de estado efêmero em alta frequência. Em um rate limiter, a necessidade central é registrar e consultar contagens por chave e por intervalo com baixa latência, o que combina bem com esse tipo de armazenamento em memória. O risco correspondente também precisa ser documentado: se Redis ficar indisponível, a política de limitação pode falhar ou bloquear incorretamente.

Prometheus e OpenTelemetry entram no exemplo para tornar o rate limiter mensurável e rastreável em produção. Prometheus ajuda a expor e coletar métricas como volume de bloqueios, latência e taxa de erro, enquanto OpenTelemetry permite instrumentar traces e sinais operacionais entre serviços. Essa combinação é importante porque uma feature de proteção só é confiável quando o time consegue observar seu efeito real no tráfego e diagnosticar desvios.

A arquitetura registrada no PRD é suficiente para enquadrar a solução sem substituir o design doc: microserviço dedicado, back-end em Go, Redis, middleware e integração HTTP com consumidores. Os trade-offs explicitam escolhas estruturais, como usar Go para a implementação, Redis como armazenamento principal e REST como forma de exposição. Isso transforma preferências implícitas em decisões rastreáveis, úteis tanto para o time quanto para automações.

O mesmo PRD que existe em Markdown pode ser exportado em JSON para ganhar estrutura legível por máquina. Markdown favorece leitura humana e revisão rápida; JSON favorece processamento sistemático, validação de campos, filtragem e consumo por agentes. A representação em JSON não substitui o documento textual, mas funciona como contrato estruturado da mesma informação.

Agentes de IA trabalham melhor quando o contexto está organizado em campos previsíveis, em vez de depender apenas de interpretação livre de texto corrido. Em JSON, seções como objetivos, escopo, requisitos, riscos e critérios de aceitação podem ser acessadas de forma determinística, o que reduz ambiguidade e melhora automação. Isso é especialmente útil quando o PRD precisa alimentar prompts, pipelines, validações ou geração de artefatos técnicos.

Markdown continua sendo a forma mais prática para leitura, edição e discussão entre pessoas. JSON passa a valer mais quando o documento precisa ser consumido por agentes, filtrado programaticamente ou transformado em entrada padronizada para outras etapas. A escolha, portanto, não é exclusiva: manter as duas saídas preserva legibilidade para humanos e estrutura para sistemas.

## Transcrição

00:01

Bom, pessoal, eu sei que a gente teve aquele PRD de loja virtual, um exemplo simples, mas aqui é um outro exemplo de PRD de feature que, nesse caso, é um Rate Limiter centralizado. Ou seja, resumo, novo sistema centralizado de Rate Limiter que será utilizado para todos os microserviços da plataforma. O objetivo é controlar o volume das requisições por chave de API e IP, evitando sobrecarga.

00:25

Contexto do problema, times de desenvolvimento de DevOps, público-alvo, microserviços internos e APIs públicas, cenário de uso-chave, onde essa feature vai ser implantada, quais são os problemas priorizados que eu tenho hoje em dia, que estão acontecendo, quais são meus objetivos rimétricos, garantir disponibilidade,

00:43

A meta é essa, reduzir o tempo de indisponibilidade, o tempo médio é esse, então tem que ser menos de um minuto, priorizar clientes premium, limitar abuso de requisições, ou seja, a métrica é erros 429 no total de requisição, garantir desempenho adequado, latência de P95 menor que 150 milissegundos. Nossa, alto, né?

01:04

Bom, escopo, o que está incluso? Limite por chave de API por IP, estratégia de limitação de burst e janela deslizante, bloqueio que retorna 429 no header, o que está fora do escopo é fila de prioridade, console, tempo real, API de administração, multi região, um monte de coisa aqui. E aqui a gente cai de novo, requisitos funcionais, o que deve ter?

01:26

E qual é o fluxo principal? O cliente envia, o rate limit identifica, o sistema verifica se o limite não foi atingido, se o limite foi atingido, fluxos alternativos, erros previstos. Galera, você consegue perceber que esse requisito funcional

01:41

Pode a gente ver esse fluxo principal? Imagina como que uma IA já não vai conseguir entender bem o seu projeto, você simplesmente trazendo como que essa parada vai funcionar. Então, isso aí é extremamente importante. Controle de burst e com janela deslizante.

01:58

bloqueio e retorno de erro 402.9, headers padrão de rate limit, que isso aqui é importante também para os headers, para os sistemas que estão sofrendo a limitação de acesso a determinadas APIs. Requisitos não funcionais. Então, aqui, performance, disponibilidade, segurança, observabilidade, confiabilidade, compatibilidade, compliance, acessibilidade.

02:23

arquitetura, microserviços dedicados, componentes back-end Go, Redis para contador de janelas, Middleware para autenticação de editoria, Prometheus e OpenTelemetry para observabilidade, integrações com microserviços consumidores HTTP, decisões de trade-offs, uso do Redis para storage principal, implementação em Go, exposição via REST,

02:45

Dependências, REST, Redis, quer dizer, organizacional, é uma dependência da galera de DevOps também, externa, os consumidores de microserviços, ou seja, a gente depende desses caras também. Riscos e mitigações, que é o Redis indisponível, o que acontece, configuração incorreta, bloqueia clientes legítimos, critérios de aceitação, testes de validação e um exemplo em JSON, galera.

03:13

O que eu estou querendo dizer com isso agora? O negócio é o seguinte, pessoal. Toda vez que você for gerar qualquer coisa com o IA, daí em seguida eu vou mostrar isso para você no prompt, porque esses PRDs eu desenvolvi um prompt que você vai poder utilizar, eu vou disponibilizar para você. Esse prompt tem duas coisas importantes. Uma coisa é conseguir entregar o documento nesse formato.

03:42

Por outro lado, eu também consigo pedir para esse meu prompt, baseado em informações, e isso você vai ver com mais clareza, que eu quero todo esse meu PRD em JSON.

03:57

Isso ajuda muito quando você vai fazer agentes de ACI comunicar, quando você quiser fazer qualquer tipo de filtro, quando você quiser evitar diversos tipos de ambiguidade. Então, eu gosto muito de ter a opção de fazer com que o meu prompt consiga gerar um markdown para ficar fácil de ler.

04:18

mas também que eu tenha a possibilidade de ter um JSON para que isso seja consumido de uma forma mais sistemática. Então, somente para você saber, tudo aquilo que a gente colocou aqui está num JSON dessa forma aqui. Então, esse JSON acaba representando todo esse Markdown que a gente acabou de ver aqui.

04:41

Isso aí vale a pena. Não necessariamente você sempre vai ter que usar, mas é importante você saber e ter em mente que isso pode te ajudar em algum momento. Maravilha?

## Resumo IA

**Abreviações**
- **PRD** — *Product Requirements Document* (Documento de Requisitos do Produto)
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)
- **IP** — *Internet Protocol* (Protocolo de Internet)
- **P95** — 95º percentil
- **HTTP** — *Hypertext Transfer Protocol* (Protocolo de Transferência de Hipertexto)
- **DevOps** — combinação de práticas de *Development* e *Operations* (Desenvolvimento e Operações)
- **Go** — linguagem de programação Go
- **REST** — *Representational State Transfer* (Transferência de Estado Representacional)
- **Redis** — armazenamento em memória usado como banco de dados/contador de alta performance
- **JSON** — *JavaScript Object Notation* (Notação de Objetos JavaScript)
- **IA** — Inteligência Artificial
- **ACI** — Agentes de Inteligência Artificial
- **Markdown** — linguagem de marcação leve para formatação de texto
- **Prometheus** — ferramenta de monitoramento e métricas
- **OpenTelemetry** — framework de observabilidade para métricas, traces e logs

**Resumo**
A aula apresentou um exemplo de PRD de feature para um rate limiter centralizado, pensado para ser usado por todos os microserviços da plataforma. O objetivo principal é controlar o volume de requisições por chave de API e por IP, evitando sobrecarga, reduzindo indisponibilidade e protegendo a disponibilidade do sistema. O instrutor destacou a importância de traduzir a intenção da feature em metas mensuráveis, como indisponibilidade inferior a um minuto, taxa de respostas 429 e latência P95 abaixo de 150 ms.

O conteúdo mostrou como delimitar claramente o escopo do PRD. Entram no escopo a limitação por API key e IP, o controle de burst, a janela deslizante e o bloqueio com retorno de status 429 e headers de rate limit. Ficam fora do escopo itens como fila de prioridade, console em tempo real, API administrativa e suporte multi-região. Essa separação foi apresentada como essencial para evitar que uma funcionalidade de proteção de tráfego vire, prematuramente, uma plataforma completa.

Em seguida, a aula explicou a importância do fluxo principal e dos fluxos alternativos no documento. O exemplo segue a sequência em que o cliente envia a requisição, o rate limiter identifica o chamador, verifica o limite e decide permitir ou bloquear. O instrutor reforçou que descrever esse fluxo melhora o entendimento humano e também fornece contexto estruturado para IA, reduzindo ambiguidades na interpretação do requisito. Também foi ressaltado que os headers padrão de rate limit tornam o comportamento mais observável para quem consome a API, ajudando o cliente a se adaptar ao limite imposto.

A solução foi contextualizada com escolhas técnicas: Redis como storage principal para contadores, pela rapidez e adequação ao controle de estado efêmero; Go no back-end; middleware para autenticação; e integração com microserviços consumidores via HTTP. Prometheus e OpenTelemetry foram citados como ferramentas de observabilidade para medir bloqueios, latência, erros e traces em produção. O instrutor também comentou riscos importantes, como indisponibilidade do Redis e configuração incorreta, que podem causar falhas na política de limitação ou bloquear clientes legítimos.

Por fim, a aula mostrou que o PRD pode existir em Markdown e também ser exportado em JSON. Markdown foi tratado como formato ideal para leitura e revisão humana, enquanto JSON foi apresentado como uma representação estruturada, mais adequada para consumo por agentes de IA, filtros, validações e automações. A mensagem central foi que manter os dois formatos ajuda a conciliar legibilidade para pessoas e processamento sistemático por máquinas.

**Pontos de atenção**
- Definir o rate limiter como serviço centralizado evita regras espalhadas entre microserviços e melhora a consistência da política.
- Metas devem ser mensuráveis: indisponibilidade, taxa de 429 e latência P95 precisam estar explícitas.
- O escopo precisa ser fechado com clareza para não transformar a feature em uma plataforma maior do que o necessário.
- Fluxo principal, fluxos alternativos e erros previstos não são detalhes opcionais; eles reduzem ambiguidade e ajudam tanto times quanto IA.
- Headers padrão de rate limit devem ser documentados para que os consumidores entendam limite, uso e tempo de espera.
- Controle de burst e janela deslizante são importantes para tratar picos curtos de tráfego sem penalizar uso legítimo.
- Redis é adequado para contadores de alta frequência, mas sua indisponibilidade deve ser tratada como risco explícito.
- Configuração incorreta da política pode bloquear clientes legítimos; isso precisa de mitigação e testes.
- Prometheus e OpenTelemetry são fundamentais para observar o comportamento real da feature em produção.
- Markdown é melhor para humanos; JSON é melhor para automação, validação e consumo por agentes.
- Ter a mesma informação em dois formatos aumenta reutilização e reduz ambiguidade em processos técnicos.
- Em PRDs para IA, a estrutura em campos previsíveis ajuda mais do que texto corrido e genérico.