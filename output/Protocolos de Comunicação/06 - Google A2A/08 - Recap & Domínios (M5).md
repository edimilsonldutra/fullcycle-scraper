Módulo: Protocolos de Comunicação\
Aula: [Recap & Domínios (M5)](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18620)

## Resumo da aula

MCP e A2A não competem pelo mesmo problema arquitetural. O MCP cobre a integração vertical entre agente e ferramenta, como acesso a banco de dados, sistema de arquivos ou APIs utilitárias. O A2A opera na integração horizontal entre agentes, onde a preocupação deixa de ser chamar uma função isolada e passa a ser coordenar especialistas independentes por meio de um contrato comum. Essa distinção explica por que os dois protocolos coexistem: um conecta capacidades instrumentais ao agente, o outro conecta agentes entre si.

O Agent Card, já estabelecido como contrato público do agente, é a base da descoberta sem hardcoding. Seu papel aqui é permitir que um cliente ou orquestrador identifique capacidades, forma de invocação e requisitos de autenticação de maneira legível por máquina. Em um ecossistema com muitos agentes, isso substitui cadastro manual de endpoints por publicação padronizada de capacidade. Quando um novo agente entra no ambiente e publica seu card, ele se torna descobrível sem exigir reconfiguração artesanal do consumidor.

Retomando o ciclo de vida da Task, a colaboração entre agentes exige uma unidade de trabalho que sobreviva além de uma chamada request-response curta. O valor prático não está apenas em ter estados observáveis, mas em sustentar processos longos, interrupções e retomadas com rastreabilidade. Streaming e webhooks entram como mecanismos de acompanhamento dessa execução persistente, evitando que o cliente dependa de polling agressivo. A separação entre messages e artifacts preserva a fronteira entre conversa operacional e entregável formal.

Domínio é a camada organizacional que agrupa múltiplos agentes sob um contexto coerente de negócio. Em vez de expor agentes isolados como unidades dispersas, o domínio reúne seus Agent Cards e apresenta um ponto de entrada mais estável para descoberta e governança. Isso reduz a fragmentação percebida pelo cliente e transforma um conjunto de especialistas em um catálogo coeso de capacidades. O domínio não substitui o agente individual; ele organiza a forma como vários agentes são publicados e consumidos em conjunto.

A função mais importante do domínio é impor governança sobre um conjunto de agentes relacionados. Essa governança inclui fronteiras de segurança, políticas de compartilhamento de dados e critérios de exposição de capacidades, o que evita que cada agente publique regras incompatíveis de forma isolada. Em ambiente corporativo, essa camada é o que torna a expansão sustentável, porque descoberta e colaboração passam a obedecer a limites institucionais claros. Sem domínio, a interoperabilidade técnica pode existir, mas a operação em escala tende ao caos organizacional.

Considere um contexto empresarial com agentes de folha de pagamento, recrutamento e benefícios. Retomando o cenário de múltiplos especialistas, a novidade aqui é que eles deixam de aparecer apenas como serviços independentes e passam a compor um domínio de recursos humanos. Para o cliente, a descoberta fica mais simples porque as capacidades são percebidas sob um mesmo guarda-chuva semântico e operacional. Para a organização, isso facilita controle de acesso, consistência contratual e evolução coordenada do ecossistema.

A progressão natural do A2A começa com contratos individuais, passa por execução persistente e alcança a organização por domínios. Esse passo muda a pergunta arquitetural de “como chamar um agente?” para “como publicar, proteger e descobrir um conjunto de agentes de forma coesa?”. Em sistemas reais, a dificuldade raramente está em conectar um único especialista; ela aparece quando dezenas ou centenas deles precisam coexistir com segurança e previsibilidade. O domínio é a resposta para essa camada de escala.

## Transcrição

00:01

Pessoal, vamos para a sessão de fechamento do nosso módulo sobre A2A.

00:06

Nas últimas aulas, nós mergulhamos profundamente na mecânica técnica,

00:11

falamos de manifestos, detalhes de ciclo de vida de task,

00:15

exploramos a anatomia do agent card,

00:18

enfim. Hoje, nosso objetivo é consolidar.

00:20

Vamos elevar o olhar para entender como essas peças

00:23

se encaixam na arquitetura de domínios e garantir...

00:26

que você tenha clareza absoluta sobre interoperabilidade horizontal.

00:32

E esta não é apenas uma aula de revisão,

00:34

é um momento em que transformamos conceitos isolados em uma visão sistêmica,

00:38

pronta para ser aplicada.

00:41

Pessoal, é aquele esquema de sempre, pergunta,

00:44

a gente para um pouco, vocês pensam e eu passo a resposta junto com vocês.

00:50

Então vamos agora à primeira questão.

00:54

Talvez mais comum em fóruns técnicos.

00:56

Por que o Google Gateway precisa existir dado que o MCP,

00:59

o Model Context Protocol, já é uma realidade de mercado?

01:03

Ou seja, se o MCP já permite que modelos se conectem a ferramentas,

01:07

por que criar uma nova camada de complexidade?

01:10

Pense nisso por um instante. Bem,

01:15

a resposta reside na direção do eixo de integração.

01:18

O MCP é uma solução vertical. Ele foca na relação agente para ferramenta.

01:23

É excelente para dar braços ao modelo,

01:26

permitindo que ele leia um banco de dados ou acesse o sistema de arquivo local.

01:31

Já o Google A2A,

01:33

por outro lado, é horizontal. Ele foca na relação agente para agente.

01:37

Enquanto o MCP resolve a função específica, o A2A resolve a colaboração complexa.

01:41

No A2A, lidamos com tasks longas, agentes que são opacos uns aos outros,

01:46

e principalmente uma interface padronizada via agent cards e task API.

01:52

O A2A é onde a orquestração acontece,

01:54

permitindo que um agente de viagens, por exemplo,

01:57

colabore com um agente de finanças,

01:59

sem que nenhum dos dois precise conhecer a implementação interna do outro.

02:05

Nossa segunda pergunta foca na experiência do desenvolvedor e na escalabilidade. Então,

02:09

como que um cliente descobre um agente A2A sem precisar de configuração manual?

02:15

Imagine um ecossistema com milhares de agentes.

02:17

Seria impossível configurar manualmente cada endpoint,

02:20

cada permissão e cada capacidade.

02:22

Como o 8-Way resolve o problema da descoberta dinâmica?

02:26

Tempo aí para vocês pensarem ou darem uma pausa no vídeo.

02:33

Vamos lá. A resposta está na padronização do agent card.

02:38

Pense nele como um manifesto de identidade do agente.

02:41

Em vez de uma documentação estática,

02:43

o card é um objeto legível por máquina que descreve três coisas: o que o agente faz,

02:49

como ele deve ser chamado e quais são os seus requisitos de autenticação.

02:54

É através do card que o orquestrador entende a capacidade

02:57

de forma programática e se elimina a necessidade de hardcoding.

03:02

Ou seja, quando um novo agente entra no domínio,

03:04

ele publica seu card e instantaneamente o sistema

03:06

de descoberta o torna disponível para colaboração.

03:10

É a automação da confiança e da capacidade.

03:16

A terceira pergunta, pessoal, nos leva para o campo da execução.

03:20

Uma solicitação foi feita, e agora?

03:23

Como garantimos que o trabalho não se perca e que o cliente saiba

03:26

exatamente o que está acontecendo em processos que podem levar minutos ou até horas?

03:31

Ou seja, como o A2A gerencia a persistência e o estado de uma entrega?

03:35

Tempo aí para vocês pensarem, darem pausa no vídeo.

03:40

Vamos lá. Aqui o herói é o ciclo de vida da task.

03:44

Diferente de uma chamada de API tradicional de Request-Response,

03:48

que morre em milissegundos, A Task Gateway é uma unidade de trabalho persistente.

03:52

Ela navega por oito estados operacionais bem definidos,

03:55

onde o Submitted ou até o Completed ou Failed.

04:00

Aliás, desde o Submitted até o Completed ou Failed. Na verdade,

04:04

é o Task Status Submitted, só para lembrar disso, pessoal. Aqui é só uma...

04:10

uma forma condensada de explicar, inclusive, pessoal,

04:13

era com o padrão da versão 0.3,

04:16

que era basicamente muito utilizada, ela usava, tá? Mas enfim.

04:20

Até que o API permite que o cliente faça

04:22

acompanhamento via streaming de eventos ou webhooks.

04:25

O segredo da clareza técnica, que é a separação entre methods,

04:29

que é o ruído da conversa,

04:30

e os artifacts, que é o valor entregue. Isso aqui é peça-chave, tá pessoal?

04:35

Esse ciclo garante que mesmo em tarefas assíncronas complexas,

04:38

haja a rastreabilidade total de um contrato de entrega respeitado.

04:45

Bem, agora é o seguinte, o que afinal é um domínio,

04:48

o que é afinal um domínio no ecossistema Google 2A e

04:52

qual sua função prática na organização de múltiplos agentes?

04:55

Até agora falamos de indivíduos, o domínio fala de sociedade.

05:00

Bem, o domínio é nosso guarda-chuva de governança. Tecnicamente,

05:03

ele funciona como um agregador de agent cards.

05:06

Imagine que sua empresa tem um domínio de recursos humanos.

05:09

Dentro dele, existem agentes de folha de pagamento, recrutamento e benefício.

05:13

O domínio é o ponto de entrada único que expõe essas capacidades de forma coesa.

05:17

Ele define as fronteiras de segurança,

05:19

as políticas de compartilhamento de dados e simplifica

05:23

a descoberta para o cliente final.

05:25

Em termos simples, pessoal, se o agent card é o currículo do agente,

05:28

o domínio é o departamento onde ele trabalha.

05:31

Ele organiza a complexidade para quem olha de fora,

05:34

o ecossistema parece um organismo único e inteligente.

05:38

Bem, a gente concluiu aqui, pessoal, a nossa jornada com a visão... Com uma visão clara,

05:43

diferenciamos a integração vertical do MCP da colaboração horizontal D2A.

05:47

Entendemos que a descoberta nasce no Agent Card e que

05:51

a execução amadurece no ciclo de vida da task.

05:54

E finalmente vimos que o domínio é que

05:56

permite tudo isso escalar em ambiente corporativo.

05:58

Você agora possui o vocabulário e o modelo mental para

06:01

desenhar sistemas onde agentes não apenas executam comandos,

06:04

mas colaboram para entregar valor real.

06:07

E no próximo módulo,

06:09

Nós colocaremos a mão na massa para construir o seu primeiro domínio. Até lá,

06:14

Revisa os conceitos de estado e garanta que a diferença entre

06:17

Mess e Jet Effect esteja gravada no seu DNA de desenvolvedor A2A.

06:22

Obrigado, valeu pessoal!

## Resumo IA

[RESUMO_IA]