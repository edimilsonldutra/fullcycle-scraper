Módulo: Protocolos de Comunicação\
Aula: [Agent Cards e Descoberta](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18614)

## Resumo da aula

A descoberta de agentes no A2A usa a convenção de well-known URIs definida pela RFC 8615. Em vez de exigir configuração manual ou documentação humana, o cliente sabe exatamente onde procurar o contrato público do agente. Essa escolha reduz ambiguidade operacional e reaproveita uma convenção já consolidada em segurança e identidade na web, como ocorre com OpenID Connect e security.txt.

O Agent Card precisa estar exposto no caminho exato /.well-known/agentcard.json e ser servido por HTTP GET com Content-Type: application/json. Esse detalhe não é cosmético: qualquer variação de nome ou estrutura quebra a descoberta automática, porque o cliente depende de previsibilidade absoluta. O card pode ser público para descoberta, enquanto os endpoints operacionais descritos nele continuam protegidos por autenticação forte.

O Agent Card é um documento consultado com frequência por clientes, gateways e catálogos, então o custo de descoberta precisa ser controlado. Cabeçalhos HTTP de cache e ETags permitem reutilizar versões já conhecidas e validar mudanças sem baixar o JSON inteiro a cada consulta. Isso reduz latência, evita carga desnecessária na infraestrutura e mantém o contrato de descoberta eficiente em escala corporativa.

Os campos name, description, version, url, provider e documentationUrl formam a camada básica de identidade do agente. name e url identificam o serviço e seu endpoint operacional; version organiza evolução do contrato; provider informa quem mantém aquela inteligência; documentationUrl atende auditoria e inspeção humana. description tem um papel especialmente importante porque a descoberta não é apenas sintática: clientes automáticos e LLMs dependem de semântica textual para inferir adequação funcional.

A seleção de um agente não depende só de nomes de campos, mas da qualidade semântica das descrições publicadas no card. Uma description vaga ou genérica dificulta a escolha automática, enquanto uma descrição precisa melhora roteamento, matching e decisão de uso. Em cenários como logística e estoque, o cliente decide com quem falar antes de criar uma Task analisando o que o agente declara fazer e em quais limites.

Retomando o cenário de descoberta já estabelecido, a lista de skills é onde o cliente verifica se o agente é semanticamente adequado para a demanda atual. Cada skill declara uma tarefa específica com identificador, nome e descrição detalhada, incluindo escopo e limitações para evitar erro de contexto. tags ajudam indexação e filtragem em catálogos, enquanto examples funcionam como pistas operacionais para clientes automáticos e LLMs entenderem melhor quando aquela skill deve ser escolhida.

Os campos inputModes e outputModes explicitam os formatos de entrada e saída aceitos por cada skill. Eles existem para evitar tentativa e erro na integração: o cliente sabe antes da chamada se deve enviar PDF, texto puro ou outro formato suportado. Esse contrato reduz incompatibilidades de payload e melhora previsibilidade no consumo automatizado.

As capabilities não descrevem tarefas de negócio, mas recursos técnicos globais suportados pela infraestrutura do agente. Flags como streaming, pushNotifications e stateTransitionHistory informam como a comunicação pode acontecer e qual nível de observabilidade operacional está disponível. Declarar uma capability é assumir compromisso real de sustentação em produção; por isso, o card deve refletir apenas o que o ambiente consegue manter com consistência.

O bloco authentication reaproveita esquemas de segurança já consolidados na OpenAPI, o que facilita interoperabilidade com API Gateways e clientes existentes. Bearer Token com OAuth 2.0 ou OpenID Connect continua sendo a opção mais comum em integrações modernas, enquanto API keys e mTLS atendem cenários com requisitos diferentes de confiança e criticidade. O valor prático desse alinhamento é eliminar tradução semântica entre o contrato de descoberta e a infraestrutura de segurança já usada pela organização.

A assinatura do Agent Card com JWS protege o próprio documento de descoberta contra adulteração em trânsito. O provedor assina o JSON e publica as chaves públicas em um endpoint JWKS; o cliente recupera essas chaves e valida a autenticidade antes de confiar no conteúdo. Esse mecanismo é especialmente importante quando o tráfego passa por gateways, marketplaces ou ambientes multi-tenant, onde a integridade do card deixa de ser uma suposição e passa a ser um requisito verificável.

Um card de um analisador de documentos mostra como o contrato se traduz em decisão operacional. O cliente encontra o nome do agente, verifica a versão, localiza o endpoint base, observa que há suporte a streaming, identifica Bearer Token como requisito de autenticação e confirma que a skill aceita PDF e produz resumo em texto. Antes mesmo de criar uma Task, já é possível decidir se esse agente é o candidato correto para a demanda atual.

## Transcrição

00:01

Pessoal, sejam bem -vindos.

00:04

Hoje nós vamos entrar em um pilar absolutamente crítico no ecossistema do 8 -way,

00:10

que são os agent cards e também, obviamente, os mecanismos de descoberta autônoma.

00:17

Até aqui, pessoal,

00:18

a ideia de agentes inteligentes conversando entre si pode

00:21

ter parecido um conceito abstrato ou puramente teórico.

00:25

Mas quando trazemos isso para a realidade da

00:27

engenharia de software e da arquitetura corporativa,

00:29

uma pergunta prática,

00:31

imediata, ela surge na nossa cabeça,

00:33

que é como que um agente descobre que outro agente existe? Mais do que isso,

00:38

como ele compreende o que o outro agente é capaz de

00:41

fazer e decide se vale a pena interagir com ele?

00:45

Exatamente para resolver esse desafio técnico que existe o Agent Card.

00:49

Pensem nele como uma identidade pública.

00:54

E no final, gente, é o cartão de visitas estruturado de um agente.

00:59

Ele expõe metadados fundamentais, capacidades operacionais,

01:04

tarefas específicas que ele sabe executar e as regras de segurança para o acesso.

01:09

E ao longo desta aula,

01:10

nós vamos analisar a fundo a anatomia desse documento e entender como

01:13

ele viabiliza a verdadeira descoberta autônoma em ambiente de produção.

01:18

Nossa agenda de hoje é estruturada para

01:20

transformar esse conceito em engenharia prática.

01:23

Então, simples como o seguinte, vamos analisar a base normativa do protocolo,

01:28

que é a RFC 8615,

01:31

responsável pela padronização de caminhos conhecidos na web, os chamados well -known.

01:35

Well -known, o R -I -L, tá?

01:38

O R -I -S. Em seguida, veremos o caminho oficial, exato,

01:44

onde esse card precisa ser exposto na internet, tá?

01:48

Para que seja localizado.

01:50

Depois faremos uma autópsia completa na anatomia do Agent Card,

01:54

dividindo nossa análise em três grandes blocos estruturais.

01:57

A identidade de metadados básicos, as chamadas skills,

02:01

que representam as tarefas granulares que o agente declara saber executar, e as capabilities,

02:06

que são os recursos técnicos globais que a infraestrutura dele suporta,

02:10

como o stream de dados. Por fim, fecharemos o encontro abordando segurança,

02:17

detalhando os esquemas de autenticação suportados e o uso

02:20

de criptografia para garantir a integridade do card.

02:24

Bem, vamos começar estabelecendo uma premissa de arquitetura muito saudável.

02:28

O ecossistema AG Trade não tenta reinventar a roda

02:32

quando o assunto é descoberta de serviços.

02:33

Em vez de criar um protocolo proprietário complexo,

02:37

ele se apoia diretamente na RFC 8615.

02:40

Esse é um padrão de mercado altamente consolidado desde 2019.

02:45

que define o uso de caminhos fixos e previsíveis sob o prefixo .elnom.

02:53

Se você já trabalhou com segurança e identidade na web,

02:56

certamente já cruzou com esse padrão.

02:58

Exatamente o mesmo mecanismo utilizado pelo OpenID

03:01

Connect para expor configurações de provedores

03:03

de identidade ou pelo mercado de segurança cibernética

03:07

Para publicar arquivos como security.txt.

03:10

Ao adotar essa mesma convenção para o arquivo agentcard.json,

03:14

O protocolo garante que qualquer cliente ou gateway possa descobrir

03:18

as capacidades de um agente realizando uma requisição HTTP simples,

03:22

sem depender de documentações externas legíveis apenas por seres humanos.

03:28

Então, entendendo a norma, vamos ao detalhe de implementação do caminho oficial.

03:32

O arquivo de metadados deve estar obrigatoriamente acessível através de uma

03:39

requisição HTTP GET apontada para o caminho exato contendo o hífen.

03:44

barra .elnon barra agentcard.json Atenção, olha só pessoal,

03:50

atenção de engenharia aqui, tá?

03:52

Qualquer variação na grafia, como os apontos, os underlines, o nome do arquivo,

03:57

violará o protocolo e quebrará a descoberta automática do sistema.

04:00

O servidor deve responder esta chamada com o content type application/json.

04:06

Um detalhe crucial de governança e segurança é que,

04:09

embora o agentcard em si precise ser um documento que permite uma descoberta livre,

04:15

os endpoints das APIs operacionais que ele descreve dentro

04:18

do JSON podem e geralmente devem exigir autenticação estrita.

04:23

Antes disso, pensando em performance em escala corporativa,

04:27

esse arquivo deve ser cacheado agressivamente usando

04:30

cabeçalhos HTTP padrão e ETags,

04:33

evitando sobrecarga desnecessária na sua infraestrutura de servidores.

04:39

Vamos agora abrir esse JSON e examinar a

04:42

anatomia dos metadados centrais de identidade,

04:45

que representam a linha de frente do contrato técnico.

04:50

O campo name faz uma string única que identifica

04:53

o serviço de forma clara no ecossistema,

04:55

como document-analyser.

04:59

Acompanhando o nome, temos o campo description,

05:02

que fornece uma explicação concisa e textual do propósito do agente.

05:06

servindo como uma descrição funcional de alto nível.

05:09

Essa parte é super importante porque quando a gente trabalha com LLM,

05:13

com inteligência artificial generativa,

05:15

é tudo sobre semântica.

05:16

Aqui esse ponto é significativamente crítico quando a gente fala de descoberta.

05:22

E o controle de ciclo de vida é determinado pelo campo version,

05:26

onde a especificação recomendada recomenda fortemente o

05:31

uso de versionamento semântico tradicional.

05:33

O campo URL...

05:36

dizendo endpoint base onde todas as interações operacionais de fato acontecerão.

05:42

Completando essa sessão estrutural, temos o objeto provider,

05:46

que detalha a organização responsável pela manutenção

05:49

daquela inteligência e o documentation URL,

05:52

um link operacional voltado para desenvolvedores humanos que

05:57

precisam auditar o comportamento do sistema fora da automação.

06:02

Documentation, isso, tá certo. Boa.

06:07

Avançando no arquivo, encontramos a propriedade skills,

06:11

que podemos classificar como os átomos de capacidade do agente.

06:16

Um skill é uma declaração formal de uma tarefa específica

06:20

que o agente domina e sabe executar com sucesso.

06:22

É lendo essa lista que o sistema cliente decide se

06:26

O agente receptor é semanticamente adequado para a demanda atual.

06:31

Cada skill possui um identificador único, um nome legível e uma descrição minuciosa,

06:36

que deve deixar explícito o escopo de atuação e, crucialmente,

06:40

as limitações do modelo para evitar falhas de contexto.

06:43

O array de tags auxilia na indexação e filtros em catálogos de agentes,

06:49

enquanto os exemplos funcionam como poucas demonstrações de uso

06:53

para orientar as decisões de LLMs clientes.

06:57

Na ponta de engenharia de dados, os campos input modes e output modes,

07:03

eles amarram rigidamente os formatos aceitos e produzidos,

07:06

como PDF e texto puro,

07:08

garantindo previsibilidade total antes do tráfego de dados começar.

07:15

Agora, diferentemente das skills que mapeiam tarefas de negócios granulares,

07:20

O bloco Capabilities declara os recursos técnicos e operacionais

07:24

que a infraestrutura do agente suporta em nível de protocolo.

07:28

Aqui tratamos de recursos opcionais da especificação A2A,

07:33

que mudam a forma como a comunicação ocorre no nível de transporte. Por exemplo...

07:38

A flag boolean stream sinaliza se o agente suporta

07:41

o envio progressivo e respostas via SSE.

07:44

O campo push notifications indica se o agente aceita o URL

07:48

de callback para notificar de forma assíncrona

07:51

quando o processamento longo terminar.

07:54

Já o state transition history confirma se o agente mantém trilhas

07:59

detalhadas das mudanças de estado das tarefas para fins de auditoria técnica.

08:04

Como líderes técnicos, pessoal, lembre-se... É importante a gente lembrar,

08:08

habilitar uma capability é assumir um compromisso

08:11

severo de sustentação e infraestrutura.

08:14

Configura apenas o que o ambiente de produção consegue manter com consistência.

08:19

Nenhum desenho de arquitetura corporativa avança sem

08:22

uma estratégia rigorosa de segurança.

08:24

O bloco authentication do Entity Card resolve isso herdando

08:29

diretamente os esquemas de segurança consagrados na especificação OpenAPI.

08:34

Isso significa que ferramentas de API Gateway e clientes

08:37

existentes conseguem interpretar essas diretrizes de forma nativa,

08:41

sem necessidade de tradução. O card expõe um array de esquemas suportados,

08:46

permitindo flexibilidade para o cliente escolher o método mais adequado.

08:50

O padrão ouro em integrações modernas continua sendo o esquema Beryl e Talk,

08:56

integrado a fluxos robustos de OAuth 2 ou OpenID Connect.

09:02

Para cenários cooperativos internos simplificados, apenas chaves de API passadas,

09:06

encabeçados ou parâmetros de consulta são amplamente aceitos.

09:10

Para ambientes de altíssima criticidade e arquitetura de confiança zero,

09:14

o protocolo prevê o suporte a MTLS,

09:17

transformando certificados digitais em identidade criptográfica de ponto a ponto.

09:26

Para elevar ainda mais a barra de segurança e topologias complexas,

09:30

o protocolo traz um recurso avançado opcional, a assinatura digital do próprio JSON,

09:36

utilizando a especificação JWS. Por que isso importa?

09:39

Em cenários onde o tráfego passa por múltiplos gateways ou marketplaces públicos,

09:44

um atacante poderia interceptar a requisição e adulterar o conteúdo

09:48

do JSON para redirecionar as chamadas operacionais para um servidor malicioso.

09:54

O JWS elimina esse risco mitigando ataques de man-in-the-middle.

09:58

O provedor do agente assina o JSON de forma criptográfica e

10:03

Publica suas chaves públicas em um endpoint padronizado pelo tipo JWKS.

10:08

O cliente busca essas chaves e valida a autenticidade do card antes de interagir.

10:13

A decisão arquitetural aqui é clara.

10:15

Para ambientes de rede privada bem delimitados, isso pode ser...

10:19

Isso pode ser preciosismo desnecessário,

10:22

mas para arquiteturas multi-tenant ou ambientes abertos é requisito indispensável.

10:29

Então, para consolidar tudo o que discutimos teoricamente até agora,

10:32

vamos observar como essa estrutura se manifesta de forma prática

10:37

e limpa em um arquivo de resumo real.

10:39

Na tela temos o contrato de um analisador de documento real. Notem o...

10:46

O perfeito alinhamento dos conceitos, o nome de identificação no topo,

10:52

a versão explícita sinalizando estabilidade,

10:55

o endpoint base apontando para API operacional e as

10:59

capacidades de infraestrutura declaradas de forma transparente,

11:02

indicando suporte nativo a streaming, mas sem notificações push nativas.

11:09

Logo abaixo, vemos a existência explícita de um token do tipo barrier.

11:13

No bloco de autenticação e, finalmente, a listagem de suas habilidades funcionais,

11:18

amarrando a entrada de arquivos PDF

11:21

à entrega de

11:28

resumos em texto limpo.

11:29

É essa simplicidade estrutural que confere elegância ao protocolo,

11:33

entregando um contrato enxuto, porém extremamente poderoso.

11:38

Então, chegamos ao fechamento da nossa aula com a tese central muito clara.

11:41

EGIT Card é o coração do ecossistema de descoberta dinâmico do ecossistema AD2AD.

11:48

Ele é a ferramenta técnica que permite qualquer sistema

11:51

responder com precisão a quatro perguntas existenciais críticas.

11:54

Quem é o agente com quem eu estou me conectando?

11:57

Quais tarefas de negócio ele é legitimamente capaz de executar?

12:01

E quais recursos operacionais e de infraestrutura sua plataforma suporta?

12:06

E, crucialmente,

12:07

quais regras de segurança eu preciso cumprir para iniciar essa conversação.

12:12

Bem, na próxima aula a gente vai falar do ciclo de vida da TESC, tá bom?

## Resumo IA

[RESUMO_IA]