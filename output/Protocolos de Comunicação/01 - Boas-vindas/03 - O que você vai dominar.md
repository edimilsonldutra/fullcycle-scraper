Módulo: Protocolos de Comunicação\
Aula: [O que você vai dominar](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18585)

## Resumo da aula

JSON-RPC 2.0 é um protocolo leve de chamada remota que padroniza como uma aplicação envia requests, identifica operações e recebe responses usando JSON. Ele importa porque transforma integrações ad hoc em contratos previsíveis, reduzindo o acoplamento entre modelos, ferramentas e serviços. Em arquiteturas de IA, essa padronização substitui conexões específicas por uma linguagem comum de troca de mensagens. O ganho prático é eliminar parte do “código macarrônico” de integração e permitir evolução com menor custo de reescrita.

Protocolos abertos permitem trocar provedores e componentes sem reconstruir toda a malha de integração. Conforme visto anteriormente, o problema não é apenas escolher um LLM, mas evitar que o restante da arquitetura dependa do formato proprietário dele. Quando a comunicação passa a seguir contratos universais, trocar OpenAI por Anthropic, por exemplo, deixa de exigir revisão completa das conexões. Isso aumenta portabilidade, reduz custo de manutenção e preserva a infraestrutura já construída.

MCP e A2A resolvem camadas diferentes do mesmo problema de interoperabilidade. Retomando a distinção já estabelecida, MCP organiza a integração vertical entre IA, ferramentas e dados, enquanto A2A organiza a colaboração horizontal entre agentes. A clareza dessa separação evita sobreposição de esforços e ajuda a decidir onde cada contrato deve existir. O efeito arquitetural é reduzir ambiguidade na solução e distribuir melhor responsabilidades entre componentes.

A arquitetura Host-Client-Server do MCP separa quem hospeda a experiência, quem consome capacidades e quem as expõe como serviço. Ela é inspirada na lógica de protocolos como o LSP: um servidor especializado publica recursos reutilizáveis, e múltiplos clientes podem consumi-los sem conhecer detalhes internos da implementação. Isso existe para escalar acesso a contexto e ferramentas com um único servidor atendendo diferentes ambientes. O contrato passa a ser mais importante que o framework ou a linguagem usada por trás dele.

Os primitivos do MCP definem categorias explícitas de interação para reduzir ambiguidade operacional. tools representam ações executáveis com efeitos ou consultas estruturadas; search organiza acesso a informação recuperável; prompt formaliza instruções e moldes de interação que orientam o comportamento do modelo. Essa separação importa porque o agente deixa de tratar tudo como texto indistinto e passa a operar sobre capacidades com semântica clara. O resultado é mais previsibilidade, menos alucinação e maior controle sobre como o modelo lê dados e executa ações.

SDKs oficiais encapsulam os contratos do protocolo em bibliotecas prontas para uso, reduzindo o esforço de implementação manual. Em vez de montar toda a infraestrutura de mensagens do zero, o time usa componentes já alinhados ao padrão para construir servidores e integrações com mais velocidade. Isso acelera entrega e diminui erros de compatibilidade, especialmente em ecossistemas onde TypeScript e Python convivem. O benefício não é só produtividade, mas aderência mais consistente ao protocolo.

Prompt injection e poisoning exploram o fato de que instruções e dados podem carregar comandos maliciosos ou distorções de comportamento. Por isso, segurança em sistemas agênticos exige camadas de validação, sanitização de entradas e organização rigorosa das saídas das ferramentas. Retomando a preocupação já vista com segurança operacional, a novidade aqui é tratar o conteúdo textual como superfície ativa de ataque, não apenas como dado passivo. Sem esse cuidado, um comando escondido em contexto externo pode induzir o agente a agir fora das políticas esperadas.

OAuth 2.1 organiza autenticação e autorização para que agentes atuem com identidade verificável e permissões delimitadas. Isso é essencial porque agentes não apenas leem dados: eles podem criar, alterar e acionar recursos em nome de usuários ou sistemas. O controle precisa responder perguntas objetivas: quem é o agente, quais escopos possui e quais ferramentas pode acessar. Retomando o cenário do agente de marketplace, a identidade correta impede que o mesmo agente que cria pedidos também acesse indevidamente dados de RH.

Conforme visto anteriormente, isolamento é parte da governança operacional; aqui ele aparece como infraestrutura prática para servidores e ferramentas. Docker e MCP Toolkit permitem empacotar componentes em ambientes portáteis, reproduzíveis e mais controlados, facilitando deploy e sandbox. Isso reduz o risco de uma ferramenta comprometer o host principal ou vazar acesso além do necessário. O isolamento não elimina a necessidade de políticas, mas torna sua aplicação operacionalmente viável.

Agent cards funcionam como manifestos de identidade e capacidade publicados por cada agente. Eles descrevem o que o agente é, o que sabe fazer e como outros agentes podem interagir com ele, viabilizando descoberta automática no ecossistema A2A. Esse mecanismo evita recodificar integrações sempre que um novo agente entra na rede. Em vez de configuração manual contínua, a colaboração passa a depender de contratos publicados e interpretáveis por outros participantes.

Tasks precisam de estados explícitos para que a colaboração entre agentes seja observável e confiável. Estados como submetida, em execução, aguardando input e concluída permitem acompanhar progresso, lidar com assincronia e coordenar fluxos orquestrados ou coreografados. Retomando o cenário de múltiplos agentes colaborando, o contrato da task substitui suposições implícitas por transições verificáveis. Isso é o que torna possível operar sistemas distribuídos sem perder controle do que cada agente está fazendo.

Comunicação agnóstica a frameworks significa que o protocolo define a interoperabilidade, não a stack interna de cada time. Um agente implementado com LangGraph pode colaborar com outro construído com Agent SDK, desde que ambos respeitem o mesmo contrato de comunicação. Essa separação preserva autonomia tecnológica entre equipes sem quebrar a integração do sistema. O efeito organizacional é permitir que times usem Python, TypeScript ou outras tecnologias sem transformar cada diferença em um projeto de adaptação.

OpenTelemetry fornece um padrão aberto para coletar telemetria e tracing distribuído sem acoplar a solução a um fornecedor específico. Em arquitetura multiagente, tracing é o mecanismo que reconstrói o caminho de uma task entre agentes, ferramentas e chamadas externas, permitindo entender latência, falhas e dependências. Isso é especialmente importante quando a execução deixa de ser linear e passa a envolver múltiplos saltos assíncronos. Observabilidade, nesse contexto, não é acessório: é o que torna o comportamento do sistema auditável e depurável.

Um projeto integrador end-to-end conecta todas essas camadas em uma solução única: protocolo, contratos, identidade, isolamento, colaboração e observabilidade. Retomando o cenário de agentes, a nova camada não é reexplicar o problema inicial, mas organizar tecnicamente a solução em papéis arquiteturais, primitivas, estados de task e mecanismos de controle. A arquitetura multiagente surge quando esses contratos permitem que agentes especializados cooperem sem depender de integrações sob medida para cada par de componentes. O domínio real do tema aparece quando a solução funciona ponta a ponta com governança, rastreabilidade e capacidade de evolução.

## Transcrição

00:00

Fala galera, beleza?

00:02

Vamos então começar a entender o que a gente vai aprender nesse treinamento.

00:06

Vou passar com vocês aqui tudo o que vocês vão aprender nesse curso, tá bom?

00:12

Primeiro, deixa eu perguntar para vocês,

00:13

Curtiram aí conhecer meu querido amigo Isaac?

00:15

O cara é muito fera e ele vai estar com vocês aqui ao longo do curso inteiro.

00:20

Então, é bom vocês terem gostado dele,

00:22

que vocês vão ver bastante a carinha dele por aí falando com vocês. Vamos lá!

00:26

Então, o que a gente vai aprender aqui?

00:28

Primeiro, a gente vai passar pelos fundamentos ali de uma visão estratégica,

00:31

onde a gente vai compreender ali como que funciona o JSON e RPC, ou seja,

00:35

como é que a gente vai usar o transporte leve e padronizado

00:39

na hora que a gente está falando da troca de mensagens. Ou seja,

00:42

a gente vai eliminar aquele código macarrônico que a gente tem ali de integração,

00:46

a gente vai criar uma linguagem ali mais

00:48

comum que qualquer modelo consegue entender,

00:51

tá bom? Então, a gente vai resolver esse problema ali.

00:53

Usando a abstração do JSON com o RPC 2.0.

00:57

Depois, a gente vai para uma ideia aqui de transição para protocolos abertos.

01:01

O que isso significa, gente?

01:02

A gente vai substituir ali a integração proprietária como

01:05

OpenAI ou Anthropic e assim por diante,

01:07

por padrões que são mais universais. Ou seja,

01:10

a gente vai tirar aquele lock-in que a gente tem às

01:12

vezes com ferramentas e vai trocar o seu cérebro ali,

01:15

o seu sistema de LLM quando precisar. Sem ter que revisar todas as suas conexões,

01:21

sem ter que refazer todos os seus códigos

01:23

para conseguir usar dados junto dessas aplicações.

01:27

Beleza? Depois, a gente vai para uma parte aqui que é a diferenciação de MCP e o A2A.

01:32

A gente vai começar a falar um pouquinho desse assunto,

01:34

um pouquinho de MCP versus Agent to Agent.

01:37

Então, a gente vai entender aqui toda a

01:40

integração vertical quando a gente está falando

01:41

de IA versus ferramenta e a horizontal quando a gente está falando de IA por IA.

01:46

Então, o benefício que a gente vai trazer aqui

01:47

é a clareza arquitetural para a gente decidir

01:50

onde a gente investe mais esforço de desenvolvimento

01:53

para a gente ter menos sobreposição de ferramenta,

01:59

ter menos esforço quando a gente está colocando isso para...

02:04

rodar no dia a dia.

02:05

Então, a gente vai passar então por essa parte de fundamentos e

02:07

visão estratégica para vocês entenderem como cada uma dessas coisas funciona.

02:11

Depois disso, a gente tem mais umas coisinhas aqui para aprender, pessoal.

02:14

A gente vai aprender o domínio do MCP,

02:16

o Model Context Protocol. Vocês já devem ter ouvido,

02:20

muitos de vocês já devem ter entendido um pouquinho sobre isso,

02:22

mas a gente vai aprofundar nesse assunto.

02:24

A gente vai falar um pouquinho dessa arquitetura Host-Client-Server.

02:27

Então, a gente vai falar um pouquinho aqui dessa estrutura de comunicação,

02:30

que ela é inspirada ali no sucesso que a gente teve no LSP.

02:33

para quem lembra disso do passado,

02:35

que é o Language Server Protocol.

02:36

Então a gente vai começar a trabalhar aqui com

02:38

essa ideia de MCP que foi inspirada nisso.

02:41

A gente vai ter o benefício do seguinte, a gente vai conseguir escalar...

02:46

bastante isso com um único servidor de dados que

02:48

vai poder servir ali para vários ambientes.

02:51

Então a gente vai conseguir resolver isso aí de uma forma bem bacana.

02:54

A gente vai implementar também um pouquinho de primitivos,

02:58

a gente vai aprender um pouquinho de tools, search, prompt,

03:00

então a gente vai entender primeiro qual que é

03:02

o significado claro de cada uma dessas coisas,

03:04

definição clara de como a IA executa essas ações, como que ela lê os dados,

03:09

como que ela recebe instruções e assim por diante,

03:11

para a gente poder ter um pouco de previsibilidade, o modelo...

03:15

parar de alucinar e a gente conseguir usar

03:17

essa ferramenta da melhor maneira possível,

03:19

porque a gente está falando aqui,

03:20

a gente está definindo uma interface rigidamente por contrato definido,

03:25

e daí com isso a gente consegue manter uma sanidade,

03:29

quando a gente está falando aqui de LLM,

03:31

que a gente sabe que não é tão fácil de mantê

03:33

-las seguindo o caminho que a gente definiu inicialmente.

03:36

Outra coisa que a gente vai fazer aqui também é desenvolvimento com SDK,

03:39

os oficiais que a gente tem ali, o TS e o Python.

03:43

E a gente vai usar as bibliotecas padrão de mercado para construir os servidores,

03:47

MCP e assim por diante, para ter mais velocidade de entrega,

03:50

a gente conseguir usar o que tem de mais moderno para ter mais

03:53

time to market para o nosso dia a dia de entrega, beleza?

03:57

Bom, tem mais um pouco de coisa para a gente falar aqui.

03:59

Depois a gente vai um pouquinho falar de segurança,

04:01

pessoal. Segurança é um capítulo extremamente importante quando a

04:05

gente está falando do mundo de A.

04:06

Não é fácil, pessoal.

04:08

É um assunto e um capítulo que tem tirado o sono de muitas pessoas,

04:12

de muitos dos arquitetos de A,

04:14

muitas das pessoas que estão implementando isso no dia a dia.

04:16

A gente aqui tem trabalhado bastante nisso, Isaac,

04:19

eu e mais uma galera tentando resolver esse tipo de problema.

04:22

A comunidade está junta. de várias instituições, de vários lugares,

04:27

faculdades, etc., tentando tratar essas coisas com bastante segurança,

04:31

porque é um ambiente novo e a segurança vai ser bastante necessária nesse momento, tá bom? Então, quando a gente está falando de segurança,

04:38

a gente vai ter que trabalhar aqui a mitigação de prompt injection... Poisoning, então,

04:44

a gente está falando aqui das camadas de validação

04:46

que a gente vai ter que implementar,

04:47

a sanitização de entradas,

04:49

a gente ter ali saídas das ferramentas mais organizadas para

04:53

a gente não deixar passar nenhuma loucura aqui.

04:55

A gente vai ter que ter uma cabeça de ter uma

04:58

segurança corporativa que vai garantir que nenhum comando malicioso vindo,

05:01

Escondido ali em dados.

05:03

Ou escondido em prompts que estão vindo externamente,

05:06

que podem comprometer o seu sistema.

05:09

Imagine que antes a gente já tinha um

05:10

monte de dificuldade de trabalhar com segurança.

05:14

A galera é bem...

05:15

A galera consegue ter

05:17

bastante criatividade

05:21

para fazer injeções,

05:25

para conseguir entrar nas nossas aplicações, para conseguir...

05:29

Para conseguir no fim das contas hackear o que a gente está fazendo no dia a dia.

05:32

E o que a gente está tendo agora são outras janelas sendo abertas.

05:35

E a gente tem que aprender a fechar essas janelas e essas portas.

05:38

Para ninguém entrar por lugares onde a gente não imaginou.

05:41

Então aqui a gente tem que se esforçar bastante.

05:44

Porque a gente sabe que do outro lado vai

05:45

vir uma galera esforçada para conseguir quebrar isso.

05:47

A gente também vai trabalhar um pouquinho a autenticação pessoal.

05:50

A gente vai usar ali o Alt 2.1.

05:52

Então a gente vai trabalhar um pouquinho o controle de identidade.

05:54

Que é muito, muito, muito importante.

05:56

Quando a gente está falando de arquitetura. Arquitetura de A.

05:59

O que a gente está falando aqui é que a gente vai ter agentes.

06:00

E agentes, por base, vão agir. Já que eles vão agir e fazer algumas coisas,

06:05

eles precisam ter um controle de quem está fazendo o quê. A partir de agora,

06:10

eles têm que ter o seu CPF ali para não

06:13

sair fazendo qualquer loucura em nome dos outros.

06:15

Então, os agentes que vão, no final das contas, criar algo,

06:18

mudar algo e ter essa capacidade de integrações com mais...

06:24

liberdade de fazer coisas,

06:25

eles vão ter também a sua identidade e permissões

06:28

para não sair quebrando qualquer coisa por aí.

06:31

Ou seja, a gente vai precisar saber quem acessa o quê,

06:34

quem pode acessar o quê, qual ferramenta cada um pode acessar e assim por diante.

06:37

É aquela governança que a gente precisa ter, que é total.

06:40

A gente saber ali exatamente o que cada agente está fazendo, o limite de cada um,

06:44

até onde eles podem ir e o que eles podem ter de acesso.

06:47

Vou dar um exemplo clássico.

06:49

Imagine que você tem seu agente lá cuidando, por exemplo,

06:51

de um marketplace, trabalhando ali toda a parte de integração.

06:56

Imagine dentro de uma...

06:58

De uma Amazon mesmo, ele trabalhando toda a parte ali de criação de pedido,

07:02

etc. Ele está fazendo tudo isso, podendo comprar, inclusive,

07:05

para os próprios clientes. E ele tem acesso à sua base de RH da sua empresa.

07:10

Ele sabe o salário, sabe tudo. Imagine que confusão, pessoal.

07:13

Então, a gente conseguir trabalhar isso também,

07:15

essa autenticação, esse controle de acesso, etc.

07:17

Vai ser super importante. E o controle de acesso começa a ser sabendo quem é quem,

07:21

né? Então, a autenticação aqui vai ser super importante para isso.

07:24

A gente vai falar também ali da...

07:25

da parte de container com Docker, MCP Toolkit,

07:28

então a gente vai falar um pouquinho disso também,

07:30

como é que a gente empacota os servidores ali em ambientes isoláveis ali,

07:35

isolados e portáteis para a gente conseguir fazer isso.

07:37

A gente vai ter aqui uma facilidade de deploy, sendbox, etc.

07:42

A gente vai poder executar as ferramentas nos ambientes mais controlados,

07:46

sem risco de vazamento para um servidor principal, por exemplo.

07:50

A gente tem mais um pouquinho de coisa para aprender,

07:52

galera. A gente vai falar também...

07:54

Da interoperabilidade, essa palavra não está tão fácil de sair não.

07:59

Interoperabilidade com o Google H -Way.

08:01

Então a gente falou lá no começo um pouquinho sobre o H

08:04

-Way e aqui a gente vai começar a aprofundar isso.

08:06

Então a gente vai falar primeiro ali da publicação de agent cards,

08:09

como é que isso vai funcionar.

08:10

A gente vai... Então, mostrar como é que a gente faz o manifesto de identidade,

08:15

a capacidade para cada agente. A descoberta automática,

08:18

que é super importante no H -Way. Subir um agente novo,

08:21

se não vai sair codando tudo de novo, ele tem que saber.

08:24

descobrir o que está chegando ali de nova ferramenta para ele.

08:26

Então, vai permitir que os novos agentes,

08:28

eles entrem no ecossistema e comecem a colaborar sem você ter

08:31

que parar toda hora ali para configurar uma coisa nova.

08:34

Pessoal, o mundo está mudando. As nossas aplicações,

08:37

elas têm que ser mais inteligentes.

08:38

Se tiver que parar toda hora para a gente codar um agente novo, a gente está ferrado.

08:42

Quanto agente na mesma frase, né, meu povo? Pessoal,

08:45

e não para por aí, gente. Tem mais coisa.

08:47

A gente vai aprender também a gestão do ciclo de vida das tasks desses agentes. Ou seja,

08:51

como é que a gente vai padronizar os estados ali de uma tarefa,

08:55

se ela foi submetida,

08:56

se ela ainda está trabalhando, se a gente tem ali um input que está sendo requerido,

09:00

se ela já está completa e assim por diante. A gente vai aprender um pouquinho disso,

09:03

depois a gente vai usar isso ali para ter a confiabilidade dos sistemas assíncronos.

09:08

Pessoal, assim como no microserviço,

09:10

quando a gente está falando de agente,

09:11

a gente pode ter isso de forma assíncrona ou de forma...

09:15

É síncrona,

09:16

a gente pode ter agentes que estão trabalhando

09:18

de forma orquestrada ou de forma coreografada.

09:22

Então é super importante você também saber trabalhar essas requisições,

09:25

como elas estão funcionando e assim por diante,

09:27

para você saber o controle ali do que cada agente está

09:29

fazendo em tempo real para conseguir trabalhar com isso, conseguir acompanhar.

09:34

A gente vai falar também ali como é que

09:36

a gente trabalha frameworks de forma agnóstica.

09:38

Então, Lengraph, o Agent SDK e assim por diante. A gente vai aprender a comunicação.

09:43

entre esses agentes construídos com tecnologias que às vezes são diferentes,

09:47

mas com o mesmo protocolo.

09:49

Isso vai ajudar a gente a ter liberdade ali do time.

09:51

O time vai poder usar Python, por exemplo,

09:54

o time de dados usando um Python,

09:55

enquanto o time de produto pode usar um TypeScript e assim por diante,

09:59

e a solução continua se integrando e funcionando. Beleza? Então,

10:03

isso é um pouquinho do que a gente vai aprender.

10:05

É bastante coisa que tem no nosso cronograma de aula aqui,

10:09

e com isso a gente vai sair do outro lado conhecendo muito sobre agentes.

10:13

A gente também vai aprender aqui a arquitetura multiagente de elite,

10:17

que a gente está chamando. Então a gente vai aprender os design patterns disso,

10:19

da orquestração para fazer isso funcionar,

10:22

a observabilidade e o tracing usando o OpenTelemetry,

10:25

que é uma ferramenta muito boa que a gente tem hoje, que a gente já usa.

10:29

Quem já conhece sabe que ela acaba ajudando bastante a gente

10:31

a não deixar acoplado ao seu sistema de telemetria.

10:35

Então a gente vai conseguir ter esse tracing ali usando o

10:37

OpenTelemetry para ver como é que as coisas estão.

10:39

E a gente vai também falar de um projeto integrador end

10:42

-to -end para vocês entenderem como funciona tudo isso daqui.

10:45

Galera, espero que vocês tenham gostado de ouvir tudo que vocês vão aprender. É bastante coisa,

10:49

mas eu vou falar para vocês uma coisa que eu me comprometo.

10:54

de fazer esse curso ser o mais leve possível, mas com o conteúdo pesado,

10:58

um conteúdo denso, mas de forma leve.

11:00

Vamos tentar trazer isso da maneira mais fácil para vocês

11:03

conseguirem aprender tudo que a gente tem para falar, porque é bastante assunto,

11:08

mas também a gente conseguir trazer bastante conteúdo para vocês, beleza?

11:13

fique aqui com a gente, já já a gente volta para a próxima aula,

11:17

não para não, aproveita que você aguentou até agora,

11:19

que você está aqui ouvindo a gente falar, fica só mais um pouquinho,

11:21

assiste só mais uma aula, que é assim que a gente tem um lifelong learning,

11:24

aqueles 10 minutos a mais que você fica num dia,

11:27

vão fazer diferença ao longo de um ano, então vai lá, assiste mais uma aulinha,

11:30

e amanhã a gente se vê, ou daqui a pouco a gente se vê de novo,

11:33

mas não para não, beleza? Tamo junto, até a próxima aula, um forte abraço!

## Resumo IA

[RESUMO_IA]