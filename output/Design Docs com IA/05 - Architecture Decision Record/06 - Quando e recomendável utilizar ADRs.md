Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17123)

## Resumo da aula

Uma decisão merece ADR quando tem impacto arquitetural, tende a permanecer por bastante tempo e seu motivo deixará de ser óbvio no futuro. Retomando o critério de uso já estabelecido, o ponto não é documentar qualquer escolha técnica, mas registrar aquilo que altera a estrutura do sistema ou condiciona sua evolução. O custo de perder esse contexto é alto porque a decisão continua influenciando código, operação, integrações e times muito depois da implementação inicial.

Impacto arquitetural aparece quando a escolha afeta vários componentes, módulos ou até times, e não apenas um trecho isolado de implementação. Esse tipo de decisão cria restrições duradouras: muda interfaces, dependências, operação, observabilidade, segurança ou forma de escalar o sistema. Quanto mais sistêmica for a consequência e mais difícil for reverter sem retrabalho amplo, mais forte é a justificativa para registrar um ADR.

Escolhas como banco de dados principal, linguagem, framework central e mensageria moldam o ciclo de vida inteiro do sistema. Elas influenciam performance, custo operacional, contratação, ecossistema de bibliotecas e até a forma como o time resolve problemas futuros. Como trocar esses elementos depois costuma exigir migração cara e risco elevado, o ADR preserva por que aquela base foi adotada e quais alternativas foram descartadas.

REST, gRPC, eventos, GraphQL, MCP e A2A não são detalhes locais; são contratos de interação entre partes do sistema. Mesmo quando o comportamento evolui, o padrão de comunicação tende a permanecer e a orientar novas integrações, tooling e observabilidade. Se um novo padrão é introduzido, a arquitetura passa a conviver com novas regras e trade-offs, o que justifica um ADR específico para registrar essa decisão.

Persistência não é apenas escolher um produto, mas definir propriedades arquiteturais como consistência, disponibilidade, latência e complexidade operacional. A comparação entre Postgres e MySQL, por exemplo, só faz sentido quando o time consegue explicar os trade-offs que motivaram a escolha, em vez de tratar a decisão como preferência pessoal. Um ADR é apropriado porque a estratégia de dados costuma ser central, duradoura e cara de substituir depois.

JWT, OAuth2 e OpenID Connect afetam segurança, interoperabilidade e compatibilidade entre componentes internos e externos. Essas escolhas definem como identidades circulam pelo sistema, como permissões são verificadas e quais integrações futuras serão mais simples ou mais difíceis. Como mudanças nessa camada costumam se propagar amplamente e envolver risco operacional, o racional precisa ficar explícito em ADR.

A organização da stack de telemetria é uma decisão arquitetural porque define como o sistema será entendido em produção. Escolher OpenTelemetry, usar Collector, adotar sidecar, enviar dados direto ao vendor ou passar por um intermediário altera custo, acoplamento operacional, padronização e capacidade de evolução. O mesmo vale para tracing com ou sem sampling: a decisão muda volume de dados, precisão diagnóstica e viabilidade econômica, portanto o contexto não deve ficar implícito.

Kubernetes, ECS, Cloud Run e Terraform não representam apenas ferramentas de execução, mas um modelo operacional para escalar, versionar e manter o sistema. Essas escolhas determinam o grau de automação, a complexidade da plataforma, a forma de rollout e o tipo de conhecimento que o time precisa sustentar. Como infraestrutura e deploy criam dependências difíceis de remover e afetam todo o ambiente produtivo, seu racional merece registro formal.

Circuit breaker, retry e timeout definem como o sistema se comporta sob falha, degradação e alta carga. Essas políticas não são ajustes cosméticos: elas alteram confiabilidade percebida, consumo de recursos, propagação de erro e experiência operacional do time. Quando a arquitetura escolhe um padrão de resiliência, ela está definindo uma postura sistêmica diante de falhas, e isso precisa ser documentado.

Versionar API é uma decisão arquitetural porque controla compatibilidade contratual ao longo do tempo. A estratégia adotada determina como o sistema evolui sem quebrar consumidores existentes, quanto legado será mantido e como mudanças incompatíveis serão introduzidas. Como esse efeito se acumula por anos e impacta múltiplas integrações, o ADR evita que o time perca o motivo da política escolhida.

Adoção de frameworks, middlewares ou vendors proprietários pode gerar lock-in técnico e operacional. O problema não é apenas depender de uma tecnologia específica, mas aceitar custos futuros de migração, treinamento, renegociação e adaptação de processos internos. Quando um API Gateway proprietário, por exemplo, passa a estruturar o tráfego e a segurança da plataforma, a dificuldade de substituição vira parte da arquitetura e deve ser registrada.

Trocar RabbitMQ por Kafka, substituir um SDK corporativo ou alterar outro componente central exige ADR porque a mudança afeta fundações do sistema. A reversão costuma ser cara, o impacto se espalha por múltiplos serviços e o sucesso depende de entender claramente por que o componente anterior deixou de atender. Nesses casos, o ADR funciona como memória da transição e como referência para futuras revisões ou novas substituições.

## Transcrição

00:00

Bom, pessoal, apesar de eu ter dado várias dicas de quando você deve usar uma DR ou não, eu resolvi fazer algo que possa te ajudar um pouquinho mais para você tomar essas decisões. E, novamente, pessoal, isso não está escrito em pedra. Não é porque eu escrevi isso que você deve seguir isso à risca. Sempre leve o contexto da sua empresa, a cultura da sua empresa, o que você acredita, o que você não acredita.

00:30

Eu não concordo com, muitas vezes, com decisões técnicas de diversos desenvolvedores, inclusive desenvolvedores muito bem conceituados, e provavelmente muitos deles também não concordam com muito, muito do que eu posso, de algumas decisões que eu possa tomar. Mas, uma coisa que eu tenho em plena certeza, a gente acaba concordando muito mais do que a gente acaba discordando.

01:00

E quando a gente consegue encarar isso de uma forma mais leve, a gente começa a perceber que não é porque alguém não concorda com algo que você faz que significa que essa pessoa ou você não seja um bom profissional. Sempre pense o quanto que vocês mais, como que eu posso dizer, concordam do que discordam.

01:27

Porque isso vira muito jogo, inclusive, para a gente ter um nível muito maior de empatia com o time que a gente está trabalhando. Beleza? Mas vamos lá, galera. Quando um ADR é necessário, ou seja, altamente recomendado, recomendo mesmo,

01:42

quando vocês têm decisões, quando decisões têm impacto arquitetural e acompanhará o projeto por muito tempo. Se aquela decisão que você está fazendo agora vai ficar um bom tempo no projeto, definitivamente você precisa de uma ADR. Outra coisa, uma ADR é necessária quando elas afetam vários módulos, quando você tem uma mudança, uma decisão que afetam vários módulos. Quando eu falo módulo, galera,

02:12

Pensem da forma como vocês quiserem, como partes do sistema. Eu gosto muito do termo componentes do sistema, inclusive times, e que dificilmente vão mudar com frequência, tá? Quando algo muda com frequência o tempo inteiro,

02:28

provavelmente a gente está testando muita coisa, tá? Ou a gente não criou um nível de dependência tão grande em cima daquilo que ainda está permitindo com que a gente consiga fazer mudanças frequentes. Agora, quando você vai tomar aquela decisão e que a gente sabe que muitas dessas decisões, para mudar, a gente vai sofrer porque às vezes tem algo muito de fundação ali no seu software,

02:53

aí, definitivamente, você precisa também ter uma DR, tá? Então, eu coloquei algumas deparas aqui para você, somente para você se ligar. Então, por exemplo, uma situação é a seguinte, uma escolha de tecnologias base, por exemplo, eu vou escolher o banco de dados, a linguagem de programação, o framework principal, mensageria, ou seja, por que isso merece uma DR? Porque ela afeta todo o ciclo de vida do sistema, a parte de performance e também a parte de custos.

03:23

Padrões de comunicação, REST, gRPC, trabalhar com eventos, GraphQL, agora, trabalhar com MCP, trabalhar com outros protocolos, A2A. Então, se você perceber, padrões de comunicação não mudam o tempo inteiro.

03:41

Normalmente, ele pode existir e, às vezes, você altera o comportamento, mas o padrão está lá. Às vezes, você adiciona um novo padrão. E, se você adiciona um novo padrão, o que acontece? Você precisa também de uma Architecture Decision Record, ok? Estratégias de persistência. Banco de dados, vou trabalhar com SQL, NoSQL, vou trabalhar com Redis, vou trabalhar com Pinecone, vou trabalhar com qualquer outro tipo de banco de dados. Meu...

04:11

isso é uma decisão que realmente precisa de uma ADR. E uma das coisas que eu mais gosto de quando estou trabalhando nesse ponto de ADR é que ele acaba sempre perguntando quais eram outras opções que fizeram com que você escolhesse essa que você está escolhendo. Vou dar um exemplo muito claro. Por que você escolheu o Postgres ao invés de utilizar o MySQL?

04:41

Se você não souber responder isso, é porque talvez você precise estudar um pouco mais sobre Postgres e SQL. Quais são os trade-offs de eu trabalhar com aquele banco de dados?

04:51

Entende? Então, essas estratégias de persistência, ela envolve diversos trade-offs de consistência de dados, de disponibilidade, de complexidade, tá? Autenticação e autorização. Vou trabalhar com tokens JWT, OAuth2, OpenID Connect, isso vai impactar na segurança e na compatibilidade de todos os componentes.

05:12

Ou seja, é algo extremamente importante. Observabilidade e telemetria, antigamente não se falava muito disso, hoje em dia é o arroz com feijão. Ou seja, como que eu organizei a minha stack de telemetria?

05:27

Ou seja, quais ferramentas, quais protocolos? Eu vou trabalhar com OpenTelemetry? Eu vou trabalhar com OpenTelemetry Collector? Ele vai ser um sidecar? Eu vou usar o SDK dele mandando direto pro meu vendor? Ou eu vou mandar pra um cara intermediário? Meu, isso muda tudo. Ah, eu vou trabalhar com tracing? Legal, mas eu vou mandar todos os tracings do meu sistema ou eu vou trabalhar com sampling? Entende? Então, esses tipos de coisa são decisões importantes, tá?

05:54

a estratégia de deploy infraestrutura. Eu vou trabalhar com o Kubernetes, vou trabalhar com o ECS, o Google Cloud Run, eu vou utilizar a Terraform, ou seja, ele vai definir como que a escala do sistema, como que vai ser versionado, inclusive,

06:12

Todo esse processo, escalar software é difícil, e quando você está pensando em infraestrutura, deploy, muda completamente. E aí a gente tem outros pontos aqui, cara, e eu botei bastante inclusive, acho que até exagerei. Padrões de resiliência e fallback. A gente vai trabalhar com circuit breaker, a gente vai trabalhar com políticas de retry, a gente vai trabalhar com timeouts,

06:36

Então, vai determinar muito como que é a confiabilidade do sistema sobre as falhas e quando ele está numa carga muito alta. Outras coisas, versionamento de API, por evitar quebras contratuais e manter a compatibilidade

06:55

anterior do seu software. Adoção de frameworks ou mid-works proprietários, ou seja, ela vai gerar uma dependência organizacional do time. Eu contratei especificamente um API Gateway da empresa X e eu sei que uma hora que eu começar a usar esse API Gateway para colocar outro não vai ter esse tom simples.

07:16

E, eventualmente, isso aí tem a ver com negócio, tem a ver com decisões estratégicas da empresa, com custo, às vezes não tá no nosso...

07:28

o nosso nível, vamos dizer ali, nosso nível hierárquico dentro da empresa, mas, de forma geral, é importante isso ser registrado, tá? Aqui, introdução ou substituição de componentes críticos. Cara, vou mudar um componente que é crítico? Ah, eu vou mudar o RabbitMQ por Kafka. Ah, eu vou usar um novo SDK aqui na empresa. Meu, isso aí, sem dúvidas,

07:54

merece você trabalhar com uma Architecture Decision Record, beleza? Para esse vídeo não ficar grande, no próximo passo a gente vai falar um pouquinho do oposto disso aí. Vamos nessa!

## Resumo IA

**Abreviações**  
- **ADR** — *Architecture Decision Record*  
- **REST** — *Representational State Transfer*  
- **gRPC** — *gRPC Remote Procedure Call*  
- **JWT** — *JSON Web Token*  
- **OAuth2** — *OAuth 2.0*  
- **OpenID Connect** — protocolo de identidade baseado em OAuth 2.0  
- **MCP** — *Model Context Protocol*  
- **A2A** — *Agent-to-Agent*  
- **SQL** — *Structured Query Language*  
- **NoSQL** — *Not Only SQL*  
- **Redis** — *Remote Dictionary Server*  
- **Postgres** — *PostgreSQL*  
- **MySQL** — sistema de gerenciamento de banco de dados relacional MySQL  
- **OpenTelemetry** — projeto/framework de telemetria aberta  
- **ECS** — *Elastic Container Service*  
- **SDK** — *Software Development Kit*  
- **API** — *Application Programming Interface*  
- **API Gateway** — gateway de APIs  

**Resumo**  
A aula explica quando uma ADR deve ser usada e reforça que ela não serve para documentar qualquer decisão técnica, mas sim escolhas com impacto arquitetural, duradouras e cuja justificativa pode deixar de ser óbvia com o tempo. O instrutor destaca que decisões desse tipo afetam a estrutura do sistema, vários módulos ou componentes, e muitas vezes também times, operação e evolução futura. A ideia central é preservar o racional por trás da escolha, evitando que o contexto se perca e que a equipe precise “redescobrir” por que algo foi adotado.

Ao longo da explicação, são apresentados vários exemplos de decisões que merecem ADR: escolha de tecnologia base, como banco de dados, linguagem, framework principal e mensageria, pois essas bases influenciam performance, custo, ecossistema e ciclo de vida do sistema. Também são citados padrões de comunicação como REST, gRPC, eventos, GraphQL, MCP e A2A, que funcionam como contratos entre partes do sistema e tendem a moldar integrações futuras. Em persistência, o foco está em explicitar trade-offs entre consistência, disponibilidade, latência e complexidade, como no caso da comparação entre Postgres e MySQL.

A aula também aborda decisões de autenticação e autorização, como JWT, OAuth2 e OpenID Connect, por impactarem segurança e interoperabilidade. Outro bloco importante é o de observabilidade e telemetria, incluindo escolhas sobre OpenTelemetry, Collector, sidecar, envio direto ao vendor e uso de sampling em tracing, já que isso altera custo, acoplamento operacional e capacidade de diagnóstico. Em infraestrutura e deploy, são mencionados Kubernetes, ECS, Cloud Run e Terraform como decisões que definem automação, escalabilidade, versionamento e modelo operacional do sistema.

Por fim, o instrutor fala sobre padrões de resiliência, como circuit breaker, retry e timeout, ressaltando que eles determinam como o sistema reage a falhas e alta carga. Também comenta versionamento de API para evitar quebras contratuais e manter compatibilidade ao longo do tempo, além da adoção de frameworks, middlewares ou vendors proprietários, que podem gerar lock-in técnico e organizacional. A substituição de componentes críticos, como trocar RabbitMQ por Kafka ou alterar um SDK central, é apresentada como outro caso claro de ADR, porque envolve mudança de fundação arquitetural e tende a ter impacto amplo e caro de reverter.

**Pontos de atenção**  
- Não registrar qualquer decisão técnica; ADR é para escolhas com impacto arquitetural relevante.  
- Priorizar decisões que tendem a permanecer por bastante tempo e cujo motivo pode se perder no futuro.  
- Considerar o alcance da decisão: se afeta vários módulos, componentes, integrações ou times, é forte candidata a ADR.  
- Avaliar o custo de reversão: quanto mais difícil e cara a troca, maior a necessidade de documentar o racional.  
- Em tecnologia base, explicitar por que uma opção foi escolhida e quais alternativas foram descartadas.  
- Em persistência, não tratar a escolha como preferência pessoal; registrar trade-offs de consistência, disponibilidade, latência e complexidade.  
- Em autenticação/autorização, deixar claro o impacto sobre segurança, compatibilidade e integração entre sistemas.  
- Em observabilidade, documentar o modelo adotado porque decisões sobre coleta, transporte, sidecar, vendor e sampling mudam custo e operação.  
- Em infraestrutura/deploy, registrar a escolha porque ela define escalabilidade, automação e o modelo operacional do sistema.  
- Em resiliência, documentar circuit breaker, retry e timeout como postura sistêmica diante de falhas, não como ajuste pontual.  
- Em versionamento de API, preservar o motivo da estratégia para manter compatibilidade e controlar a evolução contratual.  
- Ficar atento a lock-in técnico e organizacional ao adotar frameworks, middlewares ou vendors proprietários.  
- Tratar a substituição de componentes críticos como decisão arquitetural formal, especialmente quando o impacto se espalha por múltiplos serviços.  
- Levar em conta o contexto da empresa e da equipe; a orientação não é uma regra rígida, mas um guia para tomada de decisão.  
- Usar o ADR também como ferramenta de empatia e alinhamento entre profissionais com visões técnicas diferentes.