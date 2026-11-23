Módulo: Arquitetura na Era da IA\
Aula: [Mapeando o threat model do projeto atual](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18841)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

Na aula anterior a gente falou sobre superfícies de

00:05

ataque e trust boundaries em aplicações com IA.

00:08

E agora eu quero que esses conceitos,

00:11

eu quero pegar esses conceitos de olhar para

00:13

o sistema que a gente realmente construiu.

00:16

E a ideia dessa aula não é corrigir nada ainda.

00:18

O objetivo é criar uma fotografia da arquitetura atual,

00:22

identificar onde a confiança muda,

00:24

quais controles já existem e quais pontos ainda precisam de atenção.

00:30

Olhar esse primeiro diagrama, eu simplifiquei bastante a arquitetura de propósito.

00:35

Aqui nós temos o usuário entrando na aplicação,

00:40

passando pelo query planner no final das contas,

00:44

também pelo retrieval e chegando no modelo e

00:49

depois voltando ali de novo para a aplicação.

00:53

Também a gente tem a nossa base de conhecimento e também

01:01

E também a gente tem um agente,

01:03

onde a gente tem uma ferramenta que a gente pode gerar um efeito real no sistema.

01:08

Então, o ponto principal aqui não é ficar decorando o componente.

01:12

O que eu quero olhar são essas quatro boundaries.

01:16

E esse aí eu acho que é o ponto principal. Essa primeira boundary aqui é,

01:21

na realidade, o quê? É o input boundary, que é onde o usuário chega.

01:25

O segundo ponto é o contexto, ou data boundary.

01:29

Basicamente, é onde, na realidade...

01:34

A gente faz o retrieval dos documentos que estão ali no PG

01:38

Vector e a gente coloca os chunks no contexto do modelo.

01:41

E aqui tem uma mudança importante de confiança.

01:44

Só porque o documento está dentro do nosso banco,

01:47

não significa que o conteúdo dele deve ser automaticamente confiável.

01:52

Alguém criou esse documento, alguém colocou metadado nele,

01:55

alguém... Passou para uma, vamos dizer,

01:58

ele passou para uma ingestão e depois esse texto

02:01

faz parte do contexto que o modelo vai interpretar.

02:06

Então, você consegue perceber que cada parte aqui começa a ter uma ação.

02:11

Por exemplo, quando a gente está falando no input boundary,

02:15

aqui o usuário está fora da aplicação e envia o conteúdo para dentro dela.

02:20

E essa pergunta é simples. Eu posso confiar naquilo que o usuário está enviando?

02:25

E a resposta é, obviamente, que não.

02:28

Só que uma aplicação com IA...

02:30

E isso é especialmente importante porque esse conteúdo não vai

02:34

apenas preencher um campo no banco de dados.

02:36

Ele pode influenciar um modelo que vai tomar as decisões. Então,

02:40

esse aí é um ponto importante. A gente tem também aqui, no final das contas,

02:46

um terceiro boundary, que é o model... Output Boundary, tá? O modelo,

02:51

ele gera uma resposta ou uma decisão e devolve isso para o código da aplicação.

02:57

Hoje, nós já usamos a Structure Output e o Pydantic em vários

03:01

pontos e isso é um controle importante porque garante o formato da resposta,

03:07

vamos dizer assim. Mas ele não garante que o conteúdo... Está correto.

03:11

Um JSON perfeitamente válido ainda pode carregar, vamos dizer assim,

03:16

uma decisão errada. Então,

03:18

A saída do modelo precisa continuar sendo

03:21

tratada como algo que não é automaticamente confiável.

03:25

E daí, a gente tem o nosso quarto boundary ali, que é o nosso...

03:29

Action Boundary. Essa aparece principalmente no nosso Support Triage Agent. Por quê?

03:36

Porque o modelo pode escolher chamar uma ferramenta como Create Support Ticket

03:41

e nesse momento nós deixamos de ter apenas a geração de texto.

03:46

A gente tem no final das contas uma decisão probabilística

03:49

que no final das contas pode virar um efeito real.

03:53

Hoje, a ferramenta possui esquema,

03:56

validação de severidade e alguns controles básicos.

03:59

Mas existe uma pergunta maior.

04:01

Só porque o modelo escolheu usar essas ferramentas não

04:05

significa que ele está autorizado a fazer isso.

04:08

Então, não necessariamente isso é verdade.

04:11

E essa fronteira entre a decisão e a execução vai ser

04:15

uma das mais importantes quando a gente chegar na parte de agentes. Agora...

04:20

Se a gente descer um pouco o documento, a gente acaba, de forma geral,

04:24

tendo o diagrama completo do que a gente construiu. Então, aqui, só para você saber,

04:30

no final das contas, essa aula é quase que um documento que foi gerado,

04:36

mas um ponto é importante, inclusive, você entender. Inclusive, tem uma

04:41

legenda sobre as zonas de confiança.

04:46

Mas eu não quero gastar um tempo gigante. Se você olhar aqui,

04:50

A forma de como a gente olha o fluxo de sistema acaba sendo um pouco diferente, né?

04:55

Porque aqui eu tenho o cliente chegando aqui na aplicação.

05:00

Deixa eu tentar aumentar um pouquinho mais esse

05:02

cara para você conseguir enxergar melhor.

05:05

Na realidade, eu preciso fazer isso, né? Fica melhor para eu conseguir navegar.

05:11

Aqui, eu tenho o cliente chegando e eu estou

05:14

aqui em algo chamado de Trusted Application Code.

05:18

O que isso significa nessa parte aqui?

05:21

Onde eu tenho o código? Perceba que tudo isso aqui,

05:24

na realidade, são pontos determinísticos aqui no nosso ponto. Então,

05:29

eu posso chamar essa parte aqui de Trusted Application Code,

05:33

ou seja, a execução determinística escrita para a aplicação.

05:38

Outra coisa... que você vai perceber tem,

05:41

eu tenho um outro boundary aqui, que é o do agente,

05:44

que é o de query planner, que é o re-ranker,

05:48

e aqui eu tenho o answer model aqui também.

05:53

E aí a gente acaba caindo nessa parte de retrieval e tudo mais.

05:57

E aqui a gente vai para um outro boundary, que é a parte de persistência e de dados.

06:02

Então, eu tenho o PG Vector, eu tenho o meu arquivo JSON, o Current Usage, etc.

06:08

e tudo mais. Então, se você começar a perceber nessa arquitetura,

06:12

você vai começar a ver que eu tenho o Knowledge Pipeline,

06:16

eu tenho aqui o External System,

06:19

que ele acaba acessando tanto o LangFuse como a API da OpenAI e tudo mais.

06:24

Agora, o ponto mais interessante aqui...

06:27

é que cada vez que eu tenho uma setinha apontando e saindo de um boundary

06:32

para o outro significa que no final das contas eu

06:36

posso ter uma superfície de ataque porque

06:39

eu tô saindo de um lado para o outro e da mesma forma como eu saio

06:44

Do meu código é caio aqui para a parte do model aqui em relação a isso eu,

06:49

Essa setinha ela pode voltar

06:52

Para um boundary anterior. E aqui, esse dado que eu recebo do agente,

06:57

Eu tenho que pensar em como que isso aqui vai ser tratado nesse ponto.

07:01

Então, a ideia inicial aqui, na realidade,

07:03

Não é ficar dando uma aula de arquitetura,

07:07

Mas a gente começa a perceber que, por exemplo,

07:10

Se eu mando algo desse ponto verde...

07:14

Para um outro ponto verde, index, index, aqui,

07:17

AppIndex.py que a gente tem, e ele cai direto para o pipeline,

07:21

Eu sei que eu tenho atributos,

07:24

Vamos dizer assim, mais seguros,

07:27

Porque está saindo de uma parte determinística, vamos dizer,

07:30

Para uma outra parte determinística. Então,

07:33

A gente começa a ter esses tipos de informação. Agora,

07:36

A ideia principal é, toda vez que eu saio de um boundary,

07:40

Isso, cara, vai se comunicar com...

07:44

Com outros aspectos,

07:46

A gente tem que verificar qual tipo de dado é algo que vai se chamar o modelo,

07:51

É algo que é determinístico, é algo que está externo,

07:54

É algo que no final das contas acaba caindo numa outra stack,

08:00

Que nesse caso é de observabilidade,

08:01

Porém, a gente sabe que a observabilidade gera dados

08:05

E esses dados podem entrar e ficar...

08:08

Sendo utilizados na hora que o modelo vai rodar

08:11

Ou na hora que a aplicação vai utilizar.

08:14

Então, é importante a gente entender, olha só as fronteiras,

08:17

Do usuário para a aplicação, da aplicação para o modelo,

08:21

Do modelo pode ir para a aplicação.

08:23

O Data Boundary pode ser para o Model Boundary.

08:26

E o Model Decision pode ir para o Data Boundary.

08:28

E a app pode chamar a parte externa.

08:30

Então aqui eu tenho uma legenda, depois você vai olhar com calma.

08:33

E eu não quero trazer e fazer essa aula ficar aqui gigante,

08:37

Porque é um documento grande,

08:39

Mas é interessante você olhar esse cara aí no repositório, tá?

08:43

Um outro ponto importante que a gente acaba tendo é a parte de assets.

08:49

Então, cada asset é algo que pode ser lido,

08:52

Alterado ou forjado por quem, na realidade, não deveria. Então,

08:57

É aqui que são os pontos que são importantes para a gente se ligar.

09:00

Ou seja, a entrada do usuário é um asset,

09:03

Porque essa entrada não é confiável, ela alcança o planner, o re-ranking,

09:08

Etc. O System Prompt também é um outro asset.

09:11

Os documentos do Knowledge Base são um outro asset.

09:15

Os metadados, os embeddings, o Tenant Identity, as respostas,

09:19

Cada um desses caras são caras que podem ser

09:22

Utilizados no final das contas para a mudança.

09:26

Mudar, na realidade, o comportamento do sistema e trazer problemas de segurança.

09:31

Então, aqui a gente tem os boundaries que são confiáveis,

09:34

Onde a gente tem do usuário para o nosso FastAPI,

09:39

A gente tem o usuário para o Carry Planner,

09:41

A gente tem o Knowledge Base para a parte de ingestion,

09:43

A gente tem ingestion para o Vector Store, do Vector Store to Model,

09:47

Do Model Output para a aplicação, do User para o suporte,

09:51

Do Agente para a decisão da ferramenta. E o output para o contexto,

09:56

A aplicação para o OpenTelemetry, a aplicação evaluation,

09:59

O dataset para o evaluation runner. Agora, tudo isso, de forma geral,

10:03

São itens que nós temos na realidade de proteção e você vai perceber

10:08

Que muito disso é porque ele

10:11

Acaba interagindo direto com a nossa aplicação.

10:15

Mas a gente tem diversas superfícies de ataque e é sobre isso que eu queria falar.

10:19

Eu não quero passar por uma a uma.

10:22

Mas o que eu fiz? Eu cruzei essa superfície de ataque com o WASP,

10:27

Que na realidade, no final das contas, o que ele faz?

10:32

Ele tem os top 10 riscos que a gente tem de segurança aqui nesse caso.

10:37

Então, se você for olhar,

10:39

Só para você que talvez nunca tenha ouvido falar de WASP,

10:43

Se eu acessar aqui, deixa eu pegar.

10:46

Se você acessar, eu vou deixar o link disponível para vocês,

10:50

Mas eu tenho aqui o Top 10 de GNI e LLM aqui nesse caso,

10:54

2026, e ele tem um documento,

10:57

Um PDF que ele traz que você pode ter acesso a esses recursos.

11:02

E se você for olhar aqui nesse PDF, você vai perceber que é um documento bem grande.

11:09

Que tem no final das contas, ele tem 122 páginas, esse cara.

11:13

Ele mostra as diferenças do que foi mudado em relação a 2025, em relação a 2026,

11:20

Eventualmente você vai estar vendo isso, pode ter 2027, 2028,

11:24

Mas o grande ponto é que eles fizeram um

11:25

Alinhamento nesses caras e cada item desses,

11:29

No final das contas,

11:31

E eu recomendo que você tente ler ou pelo menos ter uma ideia,

11:34

Ele acaba... gerando um código,

11:37

Por exemplo, LLM01 - 2026. Então,

11:41

Ele está falando que um dos caras é prompt injection. Então,

11:44

Ele está fazendo a descrição do que é o prompt injection,

11:47

Como é que isso aqui funciona e tudo mais,

11:49

Etc. Os tipos de prompt injection que a gente pode ter, os exemplos comuns,

11:56

Os riscos e tudo mais. Então...

11:58

O ponto importante aqui é que esse tipo de documento,

12:02

Ele acaba trazendo informações de como que você trata,

12:06

Por exemplo, um prompt injection.

12:08

E ele traz alguns cenários aqui do direct injection,

12:12

Indirect injection, unintentional injection e o rag repository poisoning.

12:16

Se você olhar, a gente está falando de rag, então a gente tem isso,

12:20

Né? Se o repositório, onde ele pega as informações,

12:23

Pode estar poluído. E daí... Meu,

12:25

Essa lista acaba sendo longa para cada item. Então,

12:28

Se a gente voltar aqui no meu documento,

12:31

Você vai ver de qual cara a gente está falando. O LLM01, LLM01. Então,

12:36

Você vai perceber que eu tenho Direct Prompt Injection,

12:39

Jailbreaking, Query Manipulation e etc.

12:42

E por que eu estou dizendo isso? Porque essa tabela foi baseada,

12:46

gerada, a partir do nosso código fonte.

12:49

Então é o estado atual do nosso software.

12:52

Por isso a gente não teve nenhuma mudança no software ainda.

12:55

Mas eu cruzei esse erro, essa falha de segurança,

12:59

com os riscos do Top 10 ali do OSP para você.

13:04

Então... Aqui a gente tem desde o Query Planner Manipulation,

13:07

Indirect Prompt Injection, Reg Poisoning,

13:10

Document Provenance, Cross-Tenant Retrieval, Hidden Context Exposure. Então,

13:15

a gente tem diversos caras aqui que, baseados no OSP10,

13:19

a gente teria que tomar cuidado em relação às nossas fronteiras de ataque,

13:23

né? Mas, por outro lado,

13:25

para não dizer que o nosso sistema está inteiramente inseguro,

13:28

a gente já tem controle no código, tá?

13:31

E que já trazendo alguns limites. Por exemplo,

13:34

a gente tem a... parte de safe filters,

13:35

que a gente já força direto aqui o tenant,

13:38

a gente força o status que tem que estar publicado,

13:41

a gente está trazendo o structured output com o Pydantic,

13:46

que tem, de forma geral, uma validação,

13:48

tem validações em parâmetros,

13:49

nas tools a gente tem os hints restringindo alguns pontos que o modelo pode ler.

13:57

Então, a gente tem diversos itens, desde o Max Output Token,

14:01

Observability, a Policy por Ambiente. Então,

14:04

todos esses caras são o que a gente tem. Mas aqui que é interessante,

14:07

eu tenho os riscos que estão abertos, baseados no ponto que a gente acabou gerando.

14:12

Então, o risco de segurança, 0.1,

14:14

0.2, 0.3. E esses riscos aqui,

14:17

a nossa ideia é a gente cair e passar por

14:20

alguns desses caras para a gente conseguir entender.

14:22

Então, somente para você ter uma ideia, a gente...

14:26

pode entender que a arquitetura atual, como se fosse um baseline,

14:30

é que eu tenho uma entrada que eu não posso confiar do usuário,

14:35

eu tenho a minha parte que é um Trust Application Code, ou seja,

14:40

essa parte aqui está sendo, é confiável, ou seja,

14:44

eu posso passar somente atributos seguros, porém...

14:51

Quando esse cara, no final das contas, recebe essa informação,

14:56

eu tenho alguns filtros que também já estão seguros.

15:00

E o ponto principal aqui é que eu tenho os

15:04

shapes também da parte do output do modelo,

15:07

mas a partir dali a gente acaba pegando aqui,

15:11

pegando o conteúdo, acesso externo sem autorização, sem aprovação.

15:19

Como que eu posso dizer, human in the loop,

15:21

sem a autorização de um usuário que pode ter que olhar e ver se,

15:26

por exemplo, ele vai criar um ticket,

15:27

se é um P1, eu quero passar para uma revisão humana. Então,

15:31

a ideia aqui é que você consiga ter uma visão

15:34

geral da arquitetura atual, como que a gente está.

15:38

E aí... o que vai acontecer ao longo das aulas,

15:42

a gente vai trabalhar em cima desses caras. Então, é um documento,

15:46

Eu recomendo que você veja, mas é uma forma de você começar,

15:50

inclusive, na hora que você for criar suas aplicações.

15:55

Trabalhar, construir, criar uma skill, criar prompts,

16:00

e isso aí vai ser importante para você,

16:03

porque você tem e entende a sua aplicação,

16:05

entende o codebase, essa nossa aplicação é pequena,

16:09

então de forma geral é fácil gerar um relatório desse,

16:12

de forma geral, mas o ponto importante é, peça...

16:15

e seja criativo em gerar esses tipos de documento para você

16:20

ter uma base de como está a fotografia atual do seu sistema.

16:23

Pede para ele cruzar com o GNI LLM Top 10. ali no Wasp,

16:28

que é bem bacana você conseguir olhar esses tipos de coisa.

16:32

E a gente tem o Top 10 for Agentic Applications também,

16:35

que é um outro cara que você pode pegar lá no site do Wasp,

16:39

tá? Então eu vou deixar os links para vocês,

16:41

mas de forma geral, essa é a ideia. E aí a gente vai seguir daqui para frente.

## Resumo IA

[RESUMO_IA]