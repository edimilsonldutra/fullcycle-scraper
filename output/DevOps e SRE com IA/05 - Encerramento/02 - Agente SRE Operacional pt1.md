Módulo: DevOps e SRE com IA\
Aula: [Agente SRE Operacional pt1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18550)

## Resumo da aula



## Transcrição

00:00

Fala pessoal, sejam todos bem-vindos ao nosso módulo 5,

00:05

nosso último módulo dessa matéria.

00:08

Vamos falar um pouco mais aqui de como operar tudo

00:12

o que a gente construiu no módulo 4.

00:15

Então esse módulo é mais voltado para a prática mesmo, nós vamos praticar aqui,

00:20

mostrar como vai funcionar,

00:22

mostrar os agents funcionando, tudo lá dentro.

00:28

Do nosso cluster Kubernetes. Então,

00:30

a gente vai ter vários agents voltados para SRE e assim por diante.

00:34

Então, vamos focar bastante aqui em prática. Então,

00:38

se você ainda não construiu todo o ambiente,

00:42

igual eu te fiz aqui durante nossos módulos aqui,

00:47

construa o ambiente para você conseguir entender

00:49

como esse módulo aqui vai funcionar,

00:52

tá bom? Então, a gente vai ver sem scripts, sem...

00:57

sem rodar nada assim manualmente, nós vamos falar somente com linguagem natural,

01:01

escrever textos, mandar para a IA,

01:04

ela vai fazer o processamento,

01:06

nós vamos confirmar e ela vai executar o que a gente confirmar para ela,

01:11

o que a gente aprovar. Tudo via Open Web UI, tudo com governança e tudo rastreável,

01:16

que é o mais importante, a gente ter o rastreamento aí. Ok?

01:20

Então, vamos aqui começar falando um pouco mais das

01:24

ferramentas que vamos usar aqui no módulo, tá?

01:27

É um pouco de chover no molhado aí,

01:29

porém eu acho que é interessante a gente passar pelas ferramentas aqui.

01:32

A maior parte dessas ferramentas a gente construiu no módulo anterior.

01:35

Então, por exemplo, os Agents aqui nós construímos no módulo anterior,

01:41

tá? O SRE Thresholder,

01:43

o Postmortem Generator, o SRE Health Monitor,

01:47

a gente construiu tudo no módulo anterior.

01:49

O OpenMBI a gente subiu ele no módulo 3, ok?

01:54

E a gente vai usar esses caras aqui para fazer as nossas orquestrações.

01:59

Infraestrutura, K3D, com os namespaces da web MBA,

02:04

observability, open-end UI,

02:06

o ChromaDB para rodar a nossa base de conhecimento, guardar o nosso keynote de PACE,

02:11

os MCPs que a gente construiu no último módulo,

02:16

que a gente tem um Kubernetes MCP,

02:19

que é o K8SMCP, o Prometheus MCP,

02:22

o Fault Injection, e os incidentes MCP, ok?

02:27

Governança e auditoria, que a gente vai falar aqui do LangFuse, nós já construímos,

02:32

já está de pé, o QSuite e o BlastRadius, ok?

02:37

Que a gente também já construiu tudo aí, legal?

02:41

Então a gente vai focar aqui em quatro demos práticas,

02:44

que a gente vai inserir um problema, diagnosticar aquele problema,

02:49

Olhar como vai funcionar a governança daquilo e depois fazer

02:52

um pós-mortem desse problema que a gente inseriu. Legal?

02:56

Então, somente falando aqui da parte

03:00

de aspecto de autonomia e assistivo.

03:06

Aqui no assistivo,

03:08

nós temos a IA sugerindo

03:13

E explicando as coisas pra você.

03:15

O humano decide e age, ok?

03:19

Então é o que fazemos com Open Coding ou Copilot, por exemplo.

03:24

Seguro, mas limitado.

03:25

Então ele simplesmente vai te sugerir e você vai fazer as coisas.

03:28

É limitado ali pra gente.

03:30

O assistivo, a AI abre por requests,

03:35

sugere mudanças e o humano aprova cada ação.

03:38

Exemplo, o Security Agent que a gente criou lá no módulo 2. Tá bem?

03:43

O supervisionado,

03:45

a AI vai agir dentro de um Blast Range aprovado, ou seja,

03:51

tudo que for aprovado ela vai conseguir agir ali.

03:54

Então você primeiro aprova e depois a IA vai fazer a ação.

04:00

Então aqui é o nosso SRE Agent que vai operar, por exemplo.

04:04

Então nós vamos pedir para o SRE Agent fazer alguma

04:07

coisa e vamos aprovar ele fazer aquela ação antes dele seguir.

04:13

E o autônomo, a IA decide e executa. O humano defende as políticas.

04:18

Porém, em ambientes de alto risco, não é legal a gente aplicar isso. Ambientes simples,

04:26

ambientes de desenvolvimento, ambientes de HML,

04:29

de homologação, nós podemos até aplicar.

04:31

Mas ambientes de produção e de alto risco,

04:34

não é bom a gente aplicar isso aí. Então,

04:38

o nosso eixo vai operar no nível 3. Ele vai operar com MCPs,

04:45

mas com um kill switch,

04:46

que a gente pode parar qualquer coisa a qualquer momento, tipo,

04:49

ah, não quero deixar ele fazer mais, eu bloqueei ele todo pra fazer isso.

04:53

Com governança via incidentes MCP, tá bom?

04:57

Então a gente tem um kill switch e governança dentro dos incidentes MCP.

05:01

E vale notar que o nível 2 aqui,

05:03

que é o assistido, corresponde ao modo de governança Copilot.

05:07

Então o humano aprova cada ação, tá bom? É uma correspondência aí que a gente tem.

05:14

O módulo semi-autônomo, onde a gente age a cada execução,

05:18

opera dentro do nível 3, com tudo aprovado, igual eu já tinha dito.

## Resumo IA

[RESUMO_IA]