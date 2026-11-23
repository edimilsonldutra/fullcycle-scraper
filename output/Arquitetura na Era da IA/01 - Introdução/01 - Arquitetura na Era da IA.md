Módulo: Arquitetura na Era da IA\
Aula: [Arquitetura na Era da IA](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18106)

## Resumo da aula



## Transcrição

00:03

Bom, pessoal, e antes de a gente começar a falar especificamente de arquitetura de software,

00:08

arquitetura de solução, agentes, RAG, MCP, modelos,

00:12

frameworks e tudo mais que envolve inteligência artificial,

00:15

eu queria começar com um ponto que parece simples,

00:19

mas que muita gente acaba meio que errando.

00:21

Quando a gente fala em arquitetura dentro de tecnologia...

00:25

Muita gente já pensa diretamente em ferramentas. Pensa em microserviços, Kubernetes,

00:31

cloud, mensageria, banco de dados, cache, filas,

00:34

eventos, API Gateway, Service Mesh, etc.

00:38

Mas o grande ponto é que tudo isso pode fazer parte,

00:42

sim, de uma arquitetura. Não tem problema nenhum.

00:45

A gente vai falar, inclusive, de várias dessas coisas ao longo do nosso módulo.

00:49

Mas a arquitetura não começa necessariamente pela ferramenta.

00:53

A arquitetura não começa com a pergunta: qual tecnologia eu vou usar?

00:58

A arquitetura começa com a pergunta: qual o problema que eu estou tentando resolver?

01:02

E essa diferença parece pequena,

01:05

mas muda completamente a forma de como a gente pensa.

01:08

Porque quando você começa pela ferramenta,

01:11

você começa tentando encaixar o problema dentro da tecnologia que você quer usar.

01:15

E isso é muito comum. A pessoa vê uma tecnologia nova,

01:18

vê um framework novo, vê uma abordagem nova, vê um vídeo no YouTube,

01:22

em qualquer coisa, e já começa a pensar: preciso colocar isso no meu projeto.

01:28

Só que arquitetura não é sobre o que está na moda.

01:31

Arquitetura é sobre tomada de decisão. É sobre entender o problema,

01:35

o contexto, as restrições, entender o objetivo do negócio e,

01:39

a partir disso, conseguir desenhar uma solução ali que faça sentido.

01:44

E quando eu falo que faça sentido, não é só funcionar na máquina do desenvolvedor.

01:49

Não é só subir em produção de uma vez.

01:52

Não é só fazer, por exemplo, uma demonstração,

01:54

uma demo, uma prova de conceito ali bonitinha.

01:58

Basicamente, é fazer sentido para o negócio,

02:00

para o time, para a operação, para custo, para a segurança,

02:03

para a evolução e para a manutenção daquele software ao longo do tempo.

02:07

E aqui já entra um ponto ali muito importante para a era da IA.

02:10

Com inteligência artificial, principalmente agora, com os modelos generativos,

02:15

agentes, ferramentas de coding e tudo isso aí que a gente está vivendo,

02:19

ficou muito mais fácil começar pelo lugar errado.

02:22

A pessoa quer criar uma aplicação com IA e a primeira pergunta dela é...

02:27

Qual o modelo que eu uso?

02:28

Eu vou usar, sei lá, algum modelo do GPT,

02:31

eu vou usar o Cloud Code, vou usar o modelo, não,

02:34

o Cloud, algum Opus ou qualquer tipo de modelo,

02:37

algum modelo do Gemini, algum modelo que eu vou usar local,

02:40

vou usar qual framework? O Langchain, o Langraph, o Crew AI,

02:44

a Google SDK, usar algum banco de dados vetorial.

02:49

Então, novamente, essas perguntas, vamos dizer assim,

02:54

elas não são, obviamente, inúteis.

02:56

Em algum momento, elas vão aparecer,

02:59

só que elas não deveriam ser as primeiras perguntas.

03:02

Antes de perguntar qual modelo usar,

03:04

A gente precisa perguntar qual o problema que a gente vai resolver.

03:07

E esse problema realmente precisa de inteligência artificial?

03:12

Precisa de IA? A IA vai trazer realmente valor?

03:15

Ou ela só vai deixar a solução mais cara e mais complexa?

03:19

O usuário precisa de uma resposta ali generativa ou uma regra básica tradicional,

03:24

Usando o Rejects, por exemplo, resolveria melhor. Então a IA vai apenas surgir, tá?

03:30

A IA vai apenas sugerir algo, né?

03:34

Ou ela vai executar alguma ação. Quais dados ela vai poder acessar?

03:38

Quais dados ela não pode acessar de jeito nenhum?

03:41

Que risco que a gente tem caso ela responda errado? Quem que valida essa resposta?

03:46

Quanto que pode custar por usuário, por chamada, por tarefa ou por mês?

03:51

Como que a gente sabe se a resposta está boa?

03:53

Como que a gente vai fazer auditoria de tudo isso?

03:56

Percebe que isso muda muito a conversa, porque no final das contas,

04:00

a pergunta arquitetural não é qual é o LLM mais poderoso.

04:04

A pergunta arquitetural é...

04:06

Onde que a inteligência artificial entra nessa solução

04:09

e quais as consequências que essa decisão vai trazer.

04:13

E essa aí, no meio de tudo isso, é a grande diferença no meio de...

04:19

Todo esse monte de informação que, ultimamente, a gente entra no meio da história,

04:25

Tá? Então, a arquitetura, ela entra nesse aspecto.

04:28

A arquitetura é o que ajuda a gente a sair do modo

04:31

Vou pedir pra IA fazer alguma coisa e entra no modo.

04:34

Eu sei qual o problema que eu quero resolver,

04:37

Sei quais são as restrições, preciso respeitar a...

04:41

Tudo que o negócio traz em volta dele,

04:43

E também vou entender melhor quais as decisões que precisam ser tomadas.

04:48

Porque a IA pode ajudar a implementar,

04:50

Ela pode sugerir caminhos, ela pode gerar código, ela pode revisar, pode documentar,

04:55

Pode criar testes, mas ela não tem sozinha a responsabilidade pelo negócio.

05:00

Ela não entende completamente o contexto da empresa,

05:03

Ela não sabe todas as restrições políticas,

05:05

Técnicas, a parte comercial, a parte regulatória. Entendeu? Então,

05:09

Esse tipo de coisa que a gente tem que levar em consideração.

05:13

E quem precisa ter essa visão, no final das contas, é você.

05:16

E é aqui que eu quero deixar uma coisa bem clara.

05:18

Quando eu falo de arquitetura, eu não estou falando apenas no cargo do arquiteto.

05:23

Eu não estou falando só para quem é arquiteto no LinkedIn.

05:27

Um desenvolvedor sênior toma decisão arquitetural,

05:30

Um tech lead toma decisão arquitetural, um CTO toma também esses tipos de decisão.

05:35

Às vezes, até um desenvolvedor que está começando ali na carreira,

05:40

De alguma forma, dentro de um determinado contexto,

05:42

Ele toma decisões arquiteturais que vão impactar a

05:46

Arquitetura do software sem ao menos perceber.

05:49

Então, nessa área da IA, nesse momento de IA que a gente vive,

05:53

Isso vai ficar mais forte,

05:54

Porque cada vez mais o desenvolvedor deixa de ser apenas uma pessoa que vai

05:58

Escrever código e ele passa a ser uma pessoa que direciona a construção do software.

06:03

Você vai dar contexto,

06:04

Você vai dar especificação, você vai revisar e etc.

06:08

Mas o grande ponto de tudo isso é a decisão

06:12

em relação à arquitetura, deixa de ser uma coisa distante.

06:16

Que só alguém muito sênior, na sala fechada,

06:19

ali vai fazer e vai passar parte do dia a dia para falar quem vai desenvolver o quê.

06:25

No final das contas, a gente tem uma armadilha muito grande agora.

06:29

Como as ferramentas estão cada vez mais, vamos dizer assim, boas,

06:32

a sensação inicial é que o software ficou fácil demais.

06:35

Você escreve uma ideia e a ferramenta gera lá a tela, cria API, etc.

06:40

Só que esse é o tipo de software... que é apenas uma pequena parte do problema.

06:45

O mercado não vai pagar caro para alguém que apenas vai gerar o básico.

06:49

O diferencial vai estar em quem consegue construir o

06:52

software que se sustenta em ambientes reais,

06:55

que se integra com sistemas, que lida com dados sensíveis,

06:58

que consegue escalar, que é seguro, que tem observabilidade,

07:01

que tem um custo controlado,

07:03

que consegue evoluir ao longo do tempo e que, obviamente,

07:06

vai conseguir utilizar IA com critério. E esse é o ponto central do nosso módulo.

07:12

Não está estudando arquitetura porque é bonito falar de arquitetura.

07:15

A gente está estudando arquitetura porque daqui para frente

07:17

cada vez mais pessoas vão conseguir criar software.

07:21

Mas nem todo mundo vai conseguir criar software confiável,

07:24

sustentável, seguro, bem integrado e preparado para crescer.

07:28

E a diferença vai estar justamente na capacidade de pensar, vamos dizer assim,

07:33

arquiteturalmente. Então, antes da gente falar dos tipos de arquitetura...

07:38

Guarda aí essa primeira ideia aí.

07:41

A arquitetura não começa com a tecnologia, ela começa no problema,

07:45

depois vem o contexto, depois vem as restrições, depois as decisões,

07:49

e só então a gente começa a chegar nas ferramentas.

07:53

Quando a gente investe nessa ordem,

07:55

a chance de criar uma solução ruim aumenta muito.

07:58

Então, com a IA, essa ordem fica ainda mais importante,

08:00

porque agora...

08:02

a gente está colocando dentro dos nossos

08:04

sistemas uma capacidade nova de interpretação,

08:07

geração e, em alguns casos, acionamento de ferramentas.

08:11

Isso pode trazer também grandes riscos para a nossa aplicação. Beleza? Então,

08:16

é exatamente isso que a gente vai alinhar a partir do nosso próximo vídeo.

08:20

E antes de entrar nos detalhes de A,

08:22

a gente vai separar rapidamente os principais tipos de

08:25

arquitetura para você entender onde cada decisão se

08:28

encaixa e por que isso é tão importante para

08:31

a gente desenvolver software nessa era da inteligência artificial.

## Resumo IA

[RESUMO_IA]