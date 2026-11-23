Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17073)

## Resumo da aula

C2 aprofunda a visão externa já estabelecida no C1 e passa a mostrar a organização executável do sistema. Nesse nível, “container” não significa Docker: significa um bloco implantável ou executável relevante para entender como o sistema funciona em operação. O objetivo deixa de ser apenas mostrar quem interage com o sistema e passa a ser mostrar quais partes existem, como se comunicam e quais dependências tornam o sistema viável. Por isso, C2 serve como ponte entre arquitetura lógica e decisões de deploy, integração e infraestrutura.

No C4, um container é uma unidade de execução ou armazenamento com responsabilidade arquitetural clara, como serviço, aplicação, banco de dados, fila ou API. O nome foi escolhido para organizar o sistema em blocos operacionais, não para indicar tecnologia de empacotamento. Essa distinção evita um erro comum: confundir o diagrama com a topologia de Docker ou Kubernetes. O que importa aqui é o papel executável do bloco dentro do sistema documentado.

Retomando o Rate Limiter já contextualizado, o container principal agora aparece como um serviço HTTP desenvolvido em Go, com a biblioteca de rate limit embutida in process. Esse bloco expõe endpoints e aplica middleware HTTP para checagem de limites, o que o torna o ponto central de execução da lógica. Em vez de descrever apenas o sistema como uma biblioteca usada por outros serviços, o C2 explicita onde essa lógica roda e como ela se apresenta operacionalmente. Isso transforma uma visão conceitual em uma visão utilizável por quem precisa implantar, integrar e operar.

As anotações do container condensam decisões técnicas que ajudam a interpretar o bloco sem abrir um nível mais profundo do diagrama. No exemplo, elas registram modos de armazenamento como Redis com script Lua para atomicidade ou InMemory com locks por chave, além de estratégias como janela fixa e token bucket e o uso de headers padronizados. Esse tipo de anotação existe para comunicar restrições e capacidades relevantes sem exigir um C3 imediato. Quando bem usadas, elas tornam o container semanticamente mais rico sem poluir a leitura.

As setas do C2 não servem apenas para ligar caixas; elas precisam comunicar a natureza da interação. Verbos como “leitura e atualização”, “exporta métricas” ou “usa” deixam explícita a responsabilidade da relação, enquanto protocolos como HTTP refinam a forma de comunicação. Uma representação pode priorizar o verbo e colocar o protocolo entre parênteses ou chaves, desde que a leitura continue clara. O critério principal é semântico: quem lê deve entender rapidamente o que flui entre os blocos e por qual meio.

No caso do Prometheus, a coleta de métricas é representada como HTTP pull porque o servidor de observabilidade busca as métricas no serviço, em vez de recebê-las por envio ativo. Esse detalhe é importante porque altera a direção correta da relação no diagrama e evita uma representação enganosa do fluxo operacional. Em termos práticos, o serviço expõe métricas para scrape, e o Prometheus faz a leitura periódica desse endpoint. C2 precisa capturar esse comportamento porque ele afeta configuração, rede e operação.

O estado de limitação fica em Redis quando o Rate Limiter precisa operar de forma distribuída. Isso permite manter contadores e buckets por chave compartilhados entre múltiplas instâncias do serviço, preservando consistência do limite mesmo com escalabilidade horizontal. No diagrama, Redis não aparece como detalhe interno de implementação, mas como dependência operacional indispensável ao comportamento correto do sistema. Essa é exatamente a informação que times de infraestrutura e plataforma precisam enxergar no C2.

O OpenTelemetry Collector aparece como sistema externo que recebe traces e potencialmente também métricas e logs. A representação, porém, precisa seguir a especificação disponível: se o documento-fonte não diz explicitamente que o Prometheus lê métricas do Collector, o diagrama não deve inventar esse fluxo apenas porque ele seria arquiteturalmente mais elegante. Esse ponto mostra um princípio importante no uso de IA para diagramas: fidelidade ao texto de origem vale mais do que completar lacunas com suposições plausíveis. Quando a especificação muda, o diagrama pode mudar junto; antes disso, a precisão documental vem primeiro.

O System Boundary, já introduzido antes, continua sendo a referência para separar o que pertence ao sistema do que apenas se integra a ele. No C2, essa fronteira ganha consequência prática: um container pode ter a mesma aparência estrutural de outro e ainda assim estar fora do sistema documentado. Redis, Prometheus e OpenTelemetry Collector são blocos relevantes para a operação, mas externos ao limite do Rate Limiter. Essa distinção evita que dependências sejam confundidas com partes internas do sistema.

C2 orienta decisões concretas de operação porque revela quais blocos precisam existir para o sistema funcionar fora do papel. Ao mostrar Redis como requisito, Prometheus como coletor em pull e OpenTelemetry Collector como destino de telemetria, o diagrama informa necessidades de rede, provisionamento e observabilidade. Ele também ajuda a discutir escalabilidade e custo operacional, como no caso de sampling para não enviar 100% dos sinais de telemetria. Por isso, C2 não é apenas uma visão intermediária do C4; é um artefato útil para transformar arquitetura em ambiente executável.

Para ler esse C2 do Rate Limiter, comece pelo container principal dentro da fronteira do sistema e identifique sua responsabilidade executável. Em seguida, percorra as setas observando verbo e protocolo para entender chamadas de clientes, leitura e atualização de estado em Redis, scrape de métricas pelo Prometheus e exportação de telemetria para o OpenTelemetry Collector. Depois, use as anotações técnicas para inferir capacidades e restrições do serviço, como estratégias de limitação e modos de armazenamento. Essa sequência conecta o desenho à operação real: o que roda, do que depende e como cada integração acontece.

## Transcrição

00:01

Bom, pessoal, agora que a gente pegou a ideia em relação ao C1, que é o contexto do sistema, a gente vai aqui para o nosso C2. E o nosso C2, na realidade, ele é chamado de container. E o porquê que a gente chama esse cara de container? Porque container é qualquer coisa que consiga representar o nosso sistema dentro de um determinado escopo,

00:31

mas que ao mesmo tempo consiga representar outros sistemas, mas de uma forma um pouquinho mais granular aí nesse nosso caso, tá? Então, se você olhar aqui em relação a containers, o que eu tenho em relação a containers aqui nesse meu caso? Eu tenho um container nesse caso, que é um serviço HTTP, se você olhar aqui, ele está desenvolvido em Go, se você olhar aqui, tem até o ícone.

00:56

tá da marmotinha do Gol. Eu vou mostrar, inclusive, pra vocês que eu configurei todos os nossos prompts pra que ele já gere os ícones, pra ficar um pouquinho mais agradável. E é importante que você consiga entender que isso é um container e essas tracejadas é o nosso limite do nosso sistema, tá? Se você olhar aqui, ó, é o API do serviço com biblioteca de rate limit embutida in process. Exposição de endpoints e middleware HTTP pra checagem de limites. Então, se você perceber agora aqui,

01:24

eu tô muito mais agora focado indo um pouco mais nos detalhes do que acontece. Por quê? Porque aqui no lado eu tenho uma anotação, que nesse caso coloca modos de armazenamento Redis com script Lua para atomicidade ou InMemory com locks por chave

01:43

por locks por chave, e aqui eu tenho estratégias, que é janela fixa, token bucket, e eu tenho aqui outro ponto, headers padronizados. Então, basicamente, essa anotação está meio que descrevendo o que eu tenho dentro desse serviço, que são APIs, que no final das contas é uma API, é um contrato que a gente tem em um middleware no final das contas, para que a gente consiga configurar todos esses tipos de coisa.

02:11

Agora, um ponto interessante aqui, ó, quem que vai chamar aqui? Clientes de outras aplicações podem chamar esse meu sistema. Eu também tenho aqui, ó, coleta de métricas do serviço, que vai ter o Prometheus aqui, e a coleta de métricas dele é HTTP pool. Por quê?

02:29

Porque nesse caso, a parte de observabilidade, quando você está trabalhando com o Prometheus, não sei se você já teve contato, mas basicamente ele pega métricas do seu sistema, o Prometheus utiliza pool. Não é que você joga suas métricas para o Prometheus, é o contrário, ele vem fazer o scrape das suas métricas. Então, por isso que está aqui, httpool.

02:52

Outro ponto aqui interessante, se você olhar, eu tenho estado de limitação, ou seja, é onde que eu vou armazenar o estado dos limites em relação aos acessos à plataforma

03:09

que o Rate Limiting está trabalhando, tá? Ou seja, aqui vai ter contadores e buckets por chave em modo distribuído. E por que é distribuído? Porque eu posso ter um monte de sistemas desse rodando, né? E todos esses sistemas acabam armazenando isso aqui no Redis, nesse caso, tá?

03:28

E uma outra coisa interessante é que eu também tenho aqui um outro sistema externo, que nesse caso é o OpenTelemetryCollector, e esse sistema, no final das contas, ele fica pegando todos... ele recebe do nosso sistema, na realidade,

03:48

todos os nossos traces e também poderiam receber as nossas métricas e os nossos logs. Por que o OpenTelemetryCollector não existe somente ele e o Collector disponibiliza os dados para o Prometheus? Isso aqui seria, na realidade, uma forma mais adequada, inclusive, de se fazer.

04:09

Porém, naquele nosso feature design doc, não está falando isso explicitamente. Então, o que aconteceu? A IA gerou o negócio da forma como estava descrito no nosso sistema. Agora, se no sistema, se naquela descrição a gente estivesse colocando, olha...

04:26

Toda parte de telemetria, logs, traces e métricas vão ser rodadas a partir do Open Telemetry Collector, e o Prometheus vai ler essas métricas do Open Telemetry Collector, provavelmente a gente teria esse cara chamando esse, ou, eventualmente, somente a gente mandando para um Open Telemetry Collector, e aí o Prometheus poderia nem aparecer, aí depende do nível de granularidade que a gente queria.

04:53

Então, pessoal, somente para a gente entender essa ideia, a gente está falando de containers. E você vai perceber que é algo bem comum...

05:04

Se você olhar aqui, onde eu tenho essa setinha apontando para outra, normalmente, nessa setinha, eu posso usar algumas abordagens na hora de comunicar. Por exemplo, aqui está a leitura e atualização. Ou seja, eu estou dizendo que esse cara vai fazer a leitura e atualização desses contadores. Vai falar que esse cara exporta as métricas para o OpenTelemetry. Muitas vezes, eu posso colocar que os clientes usam

05:34

a plataforma System, tá? Então, ao invés de ter HTTP aqui, eu poderia colocar USAM e, entre parênteses, entre chaves, aqui o HTTP. Tem várias formas de você representar, mas eu acho que o mais importante de tudo isso, de forma geral, é você conseguir bater o olho e entender o que está acontecendo nesse sistema.

05:54

Para mim, olhando o que é mais contraditório nisso aqui, entre aspas, é o Prometheus consumindo os dados direto da plataforma, sendo que a gente tem um OpenTelemetry Collector aqui pra gente. Beleza? Mas, entendam então que aqui é a nossa visão de container. Então, o container agrupa os principais blocos,

06:17

são serviços, aplicações, banco de dados, filas, APIs, ele evidencia como esses blocos se comunicam e em quais protocolos, e ele ajuda nas decisões de infraestrutura, escalabilidade e deploy. Isso aqui é interessante, pessoal, porque se você mostrar

06:32

Esse C2 ali, a gente sabe que a gente está desenvolvendo um SDK, mas no final das contas, eu sei que a galera de DevOps, de infra, vai ter que disponibilizar um Redis para mim. Eu sei que eu vou ter que ter uma forma interessante, inteligente de controlar a forma de como eu vou colocar essas métricas no Open Telemetry Collector.

06:51

porque necessariamente eu quero trabalhar com sampling, eu não quero mandar 100% das informações para ele, para não ficar pesado para a minha aplicação, então depende muito. Mas o importante é você entender que eu tenho, nesse caso aqui, é o usuário, aqui dentro eu tenho um container, esse cara aqui cinza também é um outro container, mas perceba que ele está

07:14

fora dos limites da minha aplicação, ou seja, ele é um container externo, tá? E aqui é o limite da nossa aplicação, é o System Boundary. Beleza? Então, aqui estamos aqui, de forma geral, olhando o container, tá? Ou seja, a parte do C2 aqui pra gente.

## Resumo IA

**Abreviações**  
- **API** — *Application Programming Interface*  
- **C1** — *Contexto de Sistema*  
- **C2** — *Container*  
- **C4** — *Container* (nível de diagrama do modelo C4)  
- **HTTP** — *HyperText Transfer Protocol*  
- **SDK** — *Software Development Kit*  

**Resumo**  
A aula aprofundou o nível C2 do modelo C4, apresentado como uma visão mais executável e operacional do sistema em comparação ao C1. O instrutor explicou que, nesse nível, “container” não se refere a Docker, mas sim a uma unidade arquitetural relevante — como serviço, aplicação, banco de dados, fila ou API — que ajuda a entender como o sistema funciona em operação, quais blocos existem, como se comunicam e de que dependências precisam. Usando o exemplo do Rate Limiter, foi mostrado um serviço HTTP em Go, com rate limit embutido in process, expondo endpoints e middleware para checagem de limites. As anotações do container foram usadas para condensar capacidades e restrições importantes, como modos de armazenamento em Redis com script Lua para atomicidade ou InMemory com locks por chave, além de estratégias de limitação como janela fixa e token bucket e o uso de headers padronizados. Também foi explicado como as setas devem comunicar a natureza da interação, combinando verbo e protocolo para deixar claro se há leitura, atualização, exportação ou uso de um recurso. O instrutor destacou a coleta de métricas pelo Prometheus em modelo HTTP pull, enfatizando que o Prometheus faz scrape das métricas expostas pelo serviço, e não o contrário. O Redis apareceu como estado de limitação para suportar operação distribuída, preservando contadores e buckets por chave entre múltiplas instâncias. Já o OpenTelemetry Collector foi tratado como sistema externo que recebe telemetria, com a observação de que o diagrama deve respeitar estritamente o que está documentado na fonte, sem inventar fluxos “mais elegantes” que não foram explicitados. Por fim, foi reforçado que o System Boundary separa o que pertence ao sistema do que é dependência externa, e que o C2 é útil para orientar deploy, infraestrutura, escalabilidade, observabilidade e operação real do sistema.

**Pontos de atenção**  
- **Não confundir container do C4 com container de Docker/Kubernetes**; aqui o termo é arquitetural, não tecnológico.  
- **Respeitar o System Boundary**: Redis, Prometheus e OpenTelemetry Collector podem ser relevantes para a operação, mas continuam externos ao sistema documentado.  
- **Evitar suposições não presentes no documento-fonte**; o diagrama deve refletir a especificação existente, mesmo que uma alternativa pareça mais “correta” arquiteturalmente.  
- **Representar corretamente a direção da comunicação**, especialmente no Prometheus, que usa **pull/scrape** para coletar métricas.  
- **Usar setas com semântica clara**: o ideal é deixar explícito o verbo da relação e, quando necessário, o protocolo entre parênteses ou chaves.  
- **Anotações no container devem enriquecer, não poluir**; elas servem para registrar decisões técnicas relevantes sem exigir detalhamento de nível mais profundo.  
- **Redis é dependência operacional crítica** quando o rate limiting é distribuído; sua ausência afeta diretamente a consistência do limite entre instâncias.  
- **Telemetria deve considerar custo e volume**; o instrutor destacou sampling para evitar enviar 100% dos sinais e sobrecarregar a aplicação ou o pipeline.  
- **O C2 deve ser lido como visão de operação**: o foco é entender o que roda, do que depende e como integra, não apenas listar componentes.