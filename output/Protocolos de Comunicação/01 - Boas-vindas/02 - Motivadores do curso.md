Módulo: Protocolos de Comunicação\
Aula: [Motivadores do curso](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18583)

## Resumo da aula

O principal problema de sistemas agênticos em produção não é apenas escolher um bom modelo, mas fazer modelos, ferramentas e agentes se comunicarem sem criar acoplamento excessivo. Quando cada integração depende do formato específico de um provedor, trocar o LLM da aplicação pode exigir reescrever parte relevante da camada de integração. Esse cenário reduz a sustentabilidade do código e transforma evolução técnica em retrabalho.

O ecossistema de IA ainda é fragmentado: frameworks adotam convenções próprias, provedores expõem formatos distintos de tool calling e times constroem integrações ad hoc. O resultado é caos operacional, porque cada novo agente exige esforço extra para descoberta, compatibilidade e colaboração com outros agentes. Em vez de infraestrutura reutilizável, a organização acumula conexões pontuais difíceis de manter.

Acoplamento acontece quando ferramentas, dados e fluxos de execução ficam presos à forma como um provedor ou framework específico opera. Isso parece aceitável em protótipos, mas se torna caro quando a empresa precisa trocar de GPT para Claude, ou conectar o mesmo conjunto de capacidades a múltiplos modelos. Uma arquitetura sustentável precisa isolar essas dependências para que a troca do “cérebro” da aplicação não force a reconstrução do restante do sistema.

Antes do Language Server Protocol, cada IDE precisava de integrações específicas para cada linguagem, o que multiplicava esforço e incompatibilidade. Um protocolo comum mudou esse cenário ao padronizar a comunicação entre ferramentas e ambientes, reduzindo a necessidade de plugins exclusivos para cada combinação. Em ecossistemas de agentes, a mesma lógica permite sair de integrações artesanais para uma base compartilhada de interoperabilidade.

Quando cada agente precisa de uma integração customizada com cada outro agente, o número de conexões cresce de forma combinatória. Isso inviabiliza escala, especialmente em organizações com muitos times, linguagens e domínios de negócio. Protocolos existem para substituir conexões ponto a ponto por contratos comuns, permitindo que novos participantes entrem no ecossistema sem renegociar tudo do zero.

MCP, Model Context Protocol, trata da integração vertical: como um modelo acessa ferramentas, contexto e fontes de dados de forma padronizada. O ganho arquitetural está em desacoplar a ferramenta do modelo específico, expondo capacidades por meio de servidores que podem ser consumidos por diferentes IAs com mais segurança. Retomando o cenário de adoção em produção, isso evita que cada modelo exija uma implementação exclusiva para acessar a mesma base, API ou recurso operacional.

A2A, Agents to Agents, trata da integração horizontal: como agentes distintos se descobrem, trocam mensagens e colaboram mesmo sendo construídos por times diferentes e em stacks diferentes. Esse protocolo reduz a necessidade de escrever integrações sob medida para cada par de agentes, como um agente de RH falando com um agente financeiro. O efeito prático é permitir colaboração autônoma entre agentes heterogêneos sem transformar cada novo vínculo em um projeto de meses.

Dar permissão de escrita a um agente ou permitir acesso a bases e contexto sem controles adequados cria risco operacional real, inclusive por prompt injection. Por isso, governança precisa entrar no desenho desde o início, com mecanismos como OAuth 2.1, isolamento por sandbox e execução controlada em Docker. Esses elementos não servem apenas para proteger infraestrutura; eles tornam viável expor capacidades ao mundo real sem comprometer produção.

Conectar um agente a um banco SQL resolve um caso local, mas não resolve a arquitetura da empresa. O salto técnico está em pensar em catálogos de ferramentas, servidores reutilizáveis, políticas de acesso, interoperabilidade e capacidade de plugar diferentes modelos ao mesmo ecossistema. Essa mudança transforma IA de consumo de API em infraestrutura organizacional.

A abordagem prática entra para transformar esses conceitos em implementação observável. Construir servidores do zero, configurar isolamento e expor capacidades reutilizáveis mostra como protocolos deixam de ser ideia abstrata e passam a organizar sistemas reais. A referência anterior à abordagem hands-on continua válida; aqui ela ganha foco específico em infraestrutura, segurança e comunicação entre agentes.

## Transcrição

00:00

Bom, galera, conheceram agora o meu amigo Isaac. E aí, gostaram dele?

00:03

Já segue ele, já começa a criar uma conexão também,

00:07

que ele vai ajudar muito vocês no dia a dia.

00:08

É um cara que manja demais e tem muita informação para contribuir,

00:11

para compartilhar. Bom, vamos lá. Agora que vocês já conhecem a gente,

00:15

vamos entender por que a gente está aqui? Primeiramente, então,

00:18

sejam bem-vindos mais uma vez. Se você chegou até aqui,

00:21

deixa eu entender como é que está o seu dia a dia.

00:23

Possivelmente, você já passou daquela fase de brincar de Hello World ali na IA,

00:27

de começar a usar um OpenAI para fazer brincadeiras no dia a dia,

00:30

e você provavelmente já sentiu na pele a dor que a gente tem de tentar

00:33

colocar um sistema agêntico em produção e se deparou

00:37

com um grande monstro de acoplamento técnico.

00:40

Isso acontece, tá, gente? Você deve ter passado por isso. Se não passou, ótimo,

00:44

você já vai aprender antes de passar, o que vai te ajudar muito no dia a dia.

00:47

Como que a gente, como liderança técnica,

00:50

como quem está implementando isso no dia a dia...

00:52

A gente consegue equilibrar a inovação com a sustentabilidade de código, ou seja,

00:56

como que a gente vai integrar isso de uma forma que faça sentido e que seja perene.

01:00

E vamos ser bem honestos aqui,

01:01

integrar IA hoje parece um Velho Oeste ainda em grande parte das empresas.

01:05

Cada framework vai ter seu jeito, cada LLM tem seu formato de tool calling,

01:09

a gente tem ali uma necessidade de quando você

01:12

vai trocar o cérebro da sua aplicação,

01:13

quando você vai começar a usar uma IA diferente, ou seja,

01:17

vai sair de um GPT e vai para um cloud,

01:19

parece que você vai ter que reescrever metade da sua camada de... de integração, certo?

01:23

Muitas pessoas estão nesse momento e isso acaba gerando um monte de dores

01:26

no nosso dia a dia de como fazer as coisas acontecerem.

01:29

A dor que trouxe a gente aqui é que o problema não é a IA,

01:32

o problema é a comunicação entre as IAs, né?

01:34

Como é que a gente vai trabalhar essa comunicação,

01:36

como é que ela vai funcionar? Então,

01:37

o acoplamento excessivo aqui que a gente tem

01:39

das ferramentas que estão presas ao provedor. Então,

01:42

a gente acaba... trabalhando isso de uma forma muito acoplada hoje.

01:45

Tem um caos de integração.

01:47

Toda vez que um novo time vai criar, por exemplo, um agente,

01:49

você precisa de um projeto de integração de agentes ali para a descoberta.

01:53

São três meses para eles conseguirem se conversar e se entender.

01:57

E a gente tem uma insegurança operacional acontecendo também. O medo real...

02:01

de dar permissão para um agente poder ter uma escrita ou

02:04

um agente poder mexer na sua base ou no seu

02:07

contexto sem sofrer um prompt injection que você pode não estar preparado

02:11

e que vai comprometer todo o seu banco de dados, suas aplicações.

02:14

Então tem esse medo também que aparece ali operacionalmente falando.

02:17

Então a gente está vivendo ali um momento de pré-LSP, né?

02:20

Um Language Service Protocol que a gente está vivendo no pré

02:23

-ele e que quando a gente olha para isso,

02:27

os agentes...

02:28

Cada IDE precisava de um plugin específico para cada linguagem, etc.

02:33

E depois de um protocolo desse tipo, o jogo muda, né?

02:35

A gente consegue ensinar aqui como a gente vai

02:39

aplicar essa mesma lógica para os protocolos de ecossistemas agentes. Então,

02:43

como é que a gente muda isso para os ecossistemas

02:45

agentes a gente usar essa mesma lógica de LSP.

02:48

Então, a gente vai poder evoluir nesse sentido.

02:50

E deixa eu fechar com vocês aqui o que esse curso é e o que ele não é.

02:53

Fica mais fácil da gente se entender também,

02:55

para vocês entenderem o que a gente vai abordar aqui, tá?

02:57

O curso não é sobre como escrever um prompt melhor, não é para isso.

03:02

Esse curso é além disso, muito além disso.

03:04

Esse curso é um curso de engenharia e arquitetura.

03:07

Ele está indo para uma profundidade bem maior do que a

03:10

gente fala quando a gente está fazendo implementação de agentes.

03:12

Nosso objetivo aqui é transformar você num profissional que

03:15

consegue desenhar a infraestrutura de AI de

03:17

uma empresa e não apenas alguém que vai consumir as APIs ali no dia a dia.

03:20

Você vai ir muito além disso. A gente vai sair do básico.

03:24

e vai mergulhar aqui nos pilares que estão redefinindo o mercado,

03:27

no que está fazendo a transformação acontecer de verdade.

03:30

Por isso que estou eu aqui,

03:32

e o Isaac, que é quem está colocando a mão na massa,

03:34

quem está fazendo isso acontecer no dia a dia,

03:36

para conseguir trazer para vocês como isso está funcionando,

03:38

o que está mudando, o que a gente está vendo,

03:40

e o que a gente pode compartilhar com vocês, tá bom?

03:43

Então a gente vai apresentar para vocês o MCP, o Model Context Protocol.

03:47

A revolução que a gente tem ali, olhando uma integração vertical,

03:50

que alguns de vocês já devem conhecer, já devem estar usando e assim por diante,

03:52

mas que ajuda a gente a desacoplar as ferramentas dos dados dos modelos e

03:56

que cria ali servidores em que qualquer IA

03:59

pode consumir com segurança as informações.

04:02

A gente também vai falar do H-Way. Dos Agents to Agents ali,

04:06

que veio de um protocolo Google e uma revolução de comunicação horizontal também.

04:10

Como é que a gente faz os agentes

04:11

heterogêneos conseguirem ser construídos em diferentes times, diferentes linguagens,

04:16

e que eles consigam se descobrir e colaborar de forma autônoma. Então,

04:20

a gente vai trazer isso também para melhorar o nosso dia a dia.

04:23

O que você vai levar aqui para o seu dia a dia, que é muito,

04:26

muito importante, é que dentro dessa discussão que a gente vai ter aqui,

04:30

a sua visão técnica vai mudar. Você não vai pensar mais só em como...

04:34

conectar o seu agente a um banco de dados SQL,

04:36

por exemplo, você vai pensar em escalabilidade,

04:39

como que a gente vai criar um catálogo de ferramentas ali

04:41

com MCP servers que conseguem se plugar a qualquer modelo,

04:45

um Gemini, um Cloud, um GPT e assim por diante,

04:47

GROC, qualquer um que você imaginar aí.

04:50

A gente vai pensar um pouco em governança,

04:52

como é que a gente vai implementar ali o ALF 2.1.

04:55

Como é que a gente vai usar Sandbox,

04:57

Como é que a gente vai ter Docker ali para a

04:59

gente ter uma IA que interaja com o mundo real.

05:03

Sem derrubar nada em produção.

05:05

A gente vai falar um pouquinho também de interoperabilidade, tá bom?

05:07

Como é que a gente desenha sistemas onde o agente do RH, por exemplo,

05:11

fala com o agente financeiro via agent-to-agent,

05:14

sem que você precise escrever toda uma linha de código de integração entre eles,

05:18

customizada para só esses dois.

05:20

Imagina que para uma empresa que você vai ter 500 milhões de agentes,

05:22

como é que você vai fazer isso agente por agente?

05:25

Então a gente vai trabalhar um pouquinho disso também.

05:26

A gente vai ter uma jornada de hands-on aqui pesada,

05:29

como eu falei para vocês, a gente vai acabar entrando bastante,

05:31

já se prepara que vai ter bastante coisa de hands-on, onde...

05:34

a gente preparou um conteúdo aqui com mais 60% de

05:37

aula prática pra você pôr a mão no código mesmo,

05:39

olhar a coisa acontecendo e assim por diante.

05:41

A gente não vai apenas na parte teórica,

05:43

mas vai ser teórica também, vai trazer pra vocês embasamento,

05:46

mas a gente vai construir do zero aqui os servidores que

05:48

vão ajudar vocês a expor esse tipo de estratégia,

05:52

esse tipo de tecnologia e assim por diante. Beleza?

## Resumo IA

[RESUMO_IA]