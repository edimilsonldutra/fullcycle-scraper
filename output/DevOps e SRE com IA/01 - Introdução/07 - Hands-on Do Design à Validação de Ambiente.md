Módulo: DevOps e SRE com IA\
Aula: [Hands-on: Do Design à Validação de Ambiente](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18504)

## Resumo da aula



## Transcrição

00:00

Ok, dei um pause no vídeo aqui para vocês não

00:02

ficarem esperando esse tempo todo para gerar o Rambook,

00:05

que acabou de gerar aqui. Então ele deu uma mensagenzinha no final,

00:09

Rambook criados em Rambook API, rambook .md,

00:13

com todas as seis seções que a gente pediu lá no prompt,

00:17

que é o CLO, Context -HUD, Burn Rate,

00:20

quatro sintomas com diagnósticos e assim por diante.

00:22

Então a gente tem aqui um passo a passo de como a gente verificar.

00:29

Vamos abrir um ECMD aqui,

00:30

um arquivo bem estruturado de como que a

00:33

gente pode verificar a parte de problemas na aplicação.

00:38

Então a gente consegue fazer essa verificação. Então aqui tem os pods,

00:43

como que a gente pode dar um get pod,

00:44

um get log, os eventos e assim por diante. SLO definido,

00:49

os sintomas de diagnóstico, a gente consegue ver aqui latência,

00:52

teste direto. Então a gente consegue ver tudo isso aqui bem desenhado. com esse Homebook. Então,

01:01

o Homebook basicamente vai servir para

01:04

você conseguir fazer uma verificação da

01:09

sua aplicação em caso de problemas no ambiente que ela está rodando.

01:14

Se der algum problema, se recorra ao Homebook,

01:17

que ele vai conseguir te mostrar um passo a passo

01:19

como que você vai fazer o debug dessa aplicação.

01:25

Próximo passo aqui, a gente vai gerar um design doc.

01:28

O que é o design doc? Ele é um documento que vai consolidar tudo.

01:33

Arquitetura, dependências, SLO com os targets,

01:37

os alertas vinculados ao serviço e as decisões de deploy e rollback.

01:43

Então, por que a AI é boa para gerar isso? Por que ela gera isso muito bem,

01:47

esse documento? O que é um exercício de síntese?

01:49

Basicamente ela vai conseguir juntar todas as formações

01:53

espalhadas que estão dentro do nosso repositório.

01:55

Ela vai juntar, então o que a gente tem lá?

01:58

Endpoints, a gente tem SLO, a gente tem os manifestos que definem os resources,

02:02

a gente tem um handbook que define os procedimentos.

02:04

E o design doc vai pegar tudo isso e vai organizar em um documento de referência.

02:09

Esse vai ser o documento da aplicação.

02:11

O famoso readme que fica lá dentro da aplicação pode ser esse documento. Ok?

02:17

Apesar que você pode criar, talvez, um Docs Audios,

02:19

alguma coisa para colocar esse documento também.

02:22

Talvez um portal de TV desenvolvedores,

02:24

onde você consegue colocar esses documentos. Legal?

02:28

Esse documento você pode colocar no Readme. Vai funcionar super bem também.

02:32

As ações visão geral, que vai mostrar a descrição de serviços,

02:37

o propósito, os alunos,

02:38

status, link, arquitetura do serviço. As dependências,

02:42

que tem a dependência de Postgres,

02:44

do Redis, do OpenTelemetry, que é o AutoCollector,

02:48

com impacto de disponibilidade. Os SLOs,

02:53

vai ter uma tabela com SLE e SLO. Os alertas ali, quando que ocorrem.

02:57

E qual que é o erro, o push de que ele pode,

02:59

o tempo máximo que ele pode ficar fora dentro de um mês, semana e assim por diante.

03:04

Os alertas configurados,

03:05

Então a gente vai ter todos os alertas configurados ali dentro.

03:08

Mostrando dentro do nosso documento,

03:11

Mostrando quando que esses alertas vão acontecer,

03:13

Qual que é a parte ali que a gente pode atuar,

03:18

Que a gente pode chamar outras pessoas, fazer o escalonamento da demanda,

03:24

Os procedimentos de deploy e rollback,

03:26

E as lições aprendidas dentro desse cara. Então,

03:31

A validação ali é através de um Pure Review que a gente vai fazer.

03:36

Que corresponde à realidade dos alertas que são configurados corretamente.

03:39

Então, basicamente,

03:41

O documento, a gente vai ter tudo que a gente

03:46

Criou do serviço até agora, vai ser estruturado dentro desse documento.

03:51

Então, novamente, a gente tem aqui um prompt que vai falar desses documentos.

03:57

Deixa eu pegar esse prompt e mostrar para vocês. Vamos

04:04

Lá, vamos abrir ele aqui.

04:06

Esse prompt aqui a gente tem.

04:10

Algumas coisinhas aqui em cima dele. Design Doc, contexto da aplicação,

04:15

Sempre vai ter, nunca esqueçam dessa parte,

04:18

SLO de produção, vai estar aqui definido, e as sessões obrigatórias,

04:22

Igual a gente fez com o Runbook,

04:24

Vai ter a sessão obrigatória. Visão geral, arquitetura, dependências, SLO,

04:29

Alertas configurados, todos os alertas estão configurados dentro do nosso serviço,

04:35

Os procedimentos de deploy e rollback, e as lições aprendidas,

04:39

Do nosso serviço, ok? O formato de saída cria um arquivo .doc,

04:43

Design doc .md, diretamente.

04:46

Não aplique no código e apenas gere o arquivo completo. Vamos copiar esse prompt.

04:52

Ele deve demorar um pouquinho para gerar de novo.

04:54

Eu vou dar um pause no vídeo e, assim que terminar de gerar,

04:58

Ó, mandei. Assim que terminar de gerar, eu retorno aqui e a gente continua.

05:06

Ok, pessoal, estou de volta.

05:09

O documento design doc criado, com as sete sessões que a gente pediu para ele,

05:13

Que é uma visão geral do serviço,

05:15

Arquitetura com alguns diagramas, dependências,

05:18

Com algumas dependências do Postgres,

05:21

Do Redis e de outros serviços,

05:24

Se forem surgindo. O SLO, com a delimitação de erro de budget e assim por diante.

05:28

E as seis regras de alertas e os procedimentos de deploy e rollback,

05:32

Com as lições aprendidas lá no final.

05:35

Beleza? Vamos dar uma olhada aqui nos nossos docs.

05:39

Que ele criou, e o design -doc .md.

05:42

Vamos clicar aqui na lupinha para a gente ver esse documento montadinho.

05:45

Esse aqui é o prompt, eu vou fechá-lo.

05:51

Fechou o documento também. Deixa eu abrir aqui o documento de novo.

05:56

Vamos aqui na lupinha para a gente ver ele formatado.

05:59

E a gente tem aqui o documento. Então a gente tem campo,

06:02

Valor, serviço, time de SRE, os owners, status em desenvolvimento,

06:08

Versão 1.0 e a data que foi gerada aqui.

06:11

O nosso documento. Repositório, aqui vai ter o repositório do GitHub.

06:19

Grafana, o link do Grafana. O Runbook, que vai ser o nosso Runbook aqui. E o CI,

06:25

CD, GitHub Actions aqui. Legal? Visão geral,

06:31

como a gente tinha falado aqui do nosso serviço.

06:35

Os SLOs do ambiente de produção.

06:39

que aqui é a disponibilidade maior que 99%,

06:41

aqui a latência, latência aqui menor, assim por diante,

06:45

e o error rate aqui de 0,1%. O diagrama dos componentes aqui,

06:52

então aqui a gente tem request, passa pelo FastAPI,

06:55

vai para o Redis, vai para o Postgres,

06:57

e aqui a gente tem o outro restante do diagrama,

07:00

que tem o Prometheus, o Grafana,

07:02

que a gente vai falar lá na parte de observabilidade, mas ele já detalhou aqui.

07:07

como que funciona essa parte. E aqui no final tem um LM Studio,

07:11

que a gente chama aqui na parte de API de causa LLM.

07:14

O fluxo de dados, o client bate aqui no FastAPI, que faz aqui o health check,

07:21

e a gente tem os itens aqui, que vão no Postgres,

07:25

que vão no CacheReduce e no DownResponse,

07:28

e assim por diante, que explica todo o fluxo de dados.

07:31

As dependências, Postgres, Redis, Autocollector e o LM Studio.

07:35

e que é baixa a funcionalidade de agentes antes de ele ficar disponível.

07:41

Mas o CRUD Health Check funciona normalmente. Então está aqui como dependências,

07:46

mas a dependência maior é esse cara aqui. O SLA tem que ser de 99%.

07:51

Cliquei duas vezes e ele abriu o documento.

07:53

O SLA tem 99%. Então esses caras aqui são indispensáveis para a aplicação.

07:59

A gente consegue ver isso tudo dentro do nosso documento de serviço.

08:03

As estratégias aqui de resiliência.

08:05

o PostgreSQL Heads e o LM Studio e assim por diante.

08:10

Desativação do erro budget e alertas configurados.

08:14

Aqui tem os alertas que são configurados. Aqui algumas regras do PromQL.

08:20

Procedimento de deploy rollback.

08:23

Push na main do GitHub Actions.

08:28

Ele vai fazer o build do Docker, vai fazer o push da imagem para registrar ela,

08:32

vai fazer o deploy do Kubernetes e vai fazer

08:35

a verificação de health check lá dentro.

08:38

Esse é o nosso fluxo que vai ser gerado nas próximas

08:41

aulas para a gente fazer a parte automatizada do deploy dessas aplicações.

08:48

Procedimentos de rollback,

08:49

está tudo aqui. E aqui o rollback manual passo a passo,

08:53

se for o caso. E as lições aprendidas que a gente vai definir.

08:57

a hora que os acidentes que aconteceram, essas coisas. Sugestão de preço é a última,

09:02

esse é o de acidentes. Ok?

09:04

Então a gente tem aqui um documento completo da nossa aplicação, tá?

09:08

Aqui referente a essa aplicação bem simples,

09:10

mas se vocês tiverem aplicações mais complexas, esse documento é super importante.

09:16

Aplicações críticas,

09:17

esse documento é super importante para o dia a dia de trabalho aí da equipe de SRE.

09:23

E da própria equipe de desenvolvimento e das equipes interessadas.

09:26

A gente tem o Postgres lá, a equipe de DBA pode ajudar.

09:29

O Redis também, com a equipe de DBA,

09:31

a gente pode fazer vários contatos durante esse processamento.

09:38

Durante esse... Com esses docs.

09:42

Então, aqui é só uma validação do que a gente fez agora.

09:45

A gente criou lá em cima o nosso Dockerfile. Beleza?

09:50

Com base no Dockerfile,

09:51

construímos o nosso Docker Compose para a gente rodar

09:54

no nosso ambiente de dev e fazer uns testes.

09:56

Criamos todos os nossos manifestos do Kubernetes para a

10:02

gente fazer a aplicação do Kubernetes dentro do nosso K3D,

10:07

que é o nosso cluster local que está rodando.

10:10

Fizemos um Notebook operacional para a gente fazer a parte ali de...

10:17

De validação mesmo da aplicação, quando ocorre algum problema, etc.

10:21

E por fim, fizemos a documentação completa da nossa aplicação,

10:26

que está nesse design Docker, beleza? E a regra sempre é a seguinte,

10:30

se não validou, não comitou. Então sempre valide tudo que você fez através da AI.

10:35

Isso eu disse lá no primeiro módulo, lá no módulo zero,

10:38

na introdução. E agora eu estou dizendo de novo,

10:41

porque isso é muito importante. Valide sempre antes de fazer alguns commits.

10:46

Antes de fazer os commits, no caso.

10:48

A próxima parte, agora,

10:51

a gente vai falar um pouco sobre o Readme Checklist.

10:56

A gente vai usar um pouco de Skills agora.

10:59

E eu vou explicar um pouquinho como que funcionam essas Skills, ok?

11:05

Então, pessoal, as Skills funcionam da seguinte maneira.

11:09

Elas são habilidades que a gente pode chamar...

11:13

de um agent, de um serviço de native AI,

11:18

que elas são específicas e podem ser compartilhadas com todas as equipes.

11:23

Então, são os procedimentos mais padrões. Então,

11:26

eu quero fazer um procedimento de fazer uma read list checklist.

11:30

Eu quero fazer um checklist de se meu sistema está todo no ar,

11:34

se está funcionando 100%. Ok? Então, a gente consegue ter uma skill para isso.

11:40

Então, ele vai fazer esse checklist.

11:42

que é esse exemplo que a gente tem ali. Legal? Então,

11:45

agora a gente vai construir essa skill com os prompts.

11:51

Basicamente, a skill é um prompt, mas é um prompt reutilizado,

11:53

que a gente vai conseguir chamar ela várias vezes e

11:56

compartilhar com toda a equipe para ela fazer.

11:58

Então, a skill 1 vai receber a descrição.

12:02

Você é uma API REST com Python, com SQL,

12:07

em um ambiente -alvo, dev, stage ou prod, você vai colocar.

12:12

Produz um checklist de prontidão com cinco categorias,

12:15

a segurança, recursos, observabilidade, dependências e estimativa de custo.

12:21

Então, como a gente está usando o OpenCode aqui, o que a gente tem que fazer?

12:28

O OpenCode, dentro do seu projeto, tem uma pastinha que se chama .opencode.

12:34

Aqui tem algumas arquivas de configuração e aqui a gente

12:38

vai criar uma pasta que se chama skills.

12:42

Se você está usando outra ferramenta, seja o Cloud Code, etc.,

12:46

entenda como que funcionam essas skills para dentro dessa ferramenta.

12:51

Eu já defini aqui a skill certinha para dentro da ferramenta do OpenCode. Então,

12:56

basicamente, eu vou ter uma skill aqui que vai ser o Region Checklist.

13:02

Vamos puxar ela para cá. Então, como funciona aqui para o OpenCode?

13:06

Eu tenho uma skill, Region Checklist.

13:09

E um skill .md. que é justamente esse arquivinho aqui.

13:13

O que a gente tem aqui, que tem que ter na parte do Open Code?

13:17

O nome da sua skill e uma descrição. Tem alguns outros campos aqui,

13:21

nessa parte, só que não são obrigatórios.

13:24

Basicamente, a skill vai ser um prompt,

13:26

um prompt do jeito que a gente fez várias vezes lá.

13:29

Vai falar, você é um SRE sênior, responsável pelo Read,

13:32

Review, dando serviço no ambiente-alvo.

13:35

Produz o Read Checklist completo com cinco categorias.

13:39

Cada categoria deve ter itens específicos marcados como atendido,

13:42

não atendido, parcial e uma justificativa breve. Então, basicamente,

13:47

ele vai rodar dentro do seu ambiente,

13:49

verificar essas coisas que ele acabou de falar aqui e vai te devolver um resultado.

13:56

Ou atendido, não atendido ou parcial.

14:00

Na segunda parte, a gente tem aqui o contexto do serviço.

14:04

onde a gente vai ter o nome, a linguagem,

14:07

o framework, o banco de dados, o cache e várias coisas aqui,

14:12

DSL, OSC, ICD, ambiente e assim por diante.

14:15

Aqui as categorias obrigatórias,

14:18

que a gente tem segurança, recursos, observabilidade,

14:22

dependências e estimativa de custo. Ele vai criar essa skill,

14:27

vai dar esse retorno para a gente. Aqui o formato de saída. Para cada categoria,

14:34

faz a listinha aqui com o OK, o X ou a interrogação, a exclamação aqui,

14:39

falando qual é o status do serviço com uma justificativa pequena de cada linha. Legal?

14:46

Aqui só tem um como usar e uma validação esperada e um se der erro, ok?

14:53

Aqui um exemplo.

14:55

A gente tem um exemplo aqui de

14:57

como que está preenchido o nosso skill.

15:04

Então, daqui para cima eu vou deletar, vou manter só o cabeçalho.

15:09

E aqui a nossa skill pronta, que já estava preenchida,

15:12

já deixei pronta aqui para a gente ganhar tempo.

15:15

Então, vamos salvar essa skill.

15:19

Basicamente, lá no OpenCode, ao invés de você copiar e colar,

15:23

igual eu fiz com os prompts para gerar os artefatos desde o início,

15:26

lá no OpenCode a gente vai ter uma barra de skills.

15:31

A skill... estaria listada aqui.

15:34

Mas provavelmente ela não está listada justamente porque eu criei.

15:40

Provavelmente, eu vou precisar reiniciar o serviço.

15:42

Aí aqui dentro do arquivo de novo, eu vou dar um OpenCode.

15:46

Vou vir aqui e dar uma barra de skill de novo.

15:49

E ela já está aqui embaixo. Region checklist.

15:52

Quando a gente faz isso,

15:54

ele basicamente vai pegar todo aquele texto que estava escrito lá na

15:57

skill e vai jogar dentro aqui do prompt para fazer a validação.

16:03

que eu pedi. Então, ele vai executar.

16:06

Se ele precisar executar alguma coisa ou algo do tipo diferente,

16:10

ele vai fazer essa validação.

16:12

Então, ele vai explorar aqui. Ele está explorando o meu código,

16:15

basicamente. Então, ele vai validar a segurança,

16:17

vai validar a observabilidade, vai validar as dependências.

16:22

Vai fazer a estimativa de custo e assim por diante. Legal?

16:28

Deixe ele rodar aqui,

16:29

Vou dar um pause e assim que terminar eu volto com vocês

16:33

Aqui para a gente não perder tanto tempo só esperando isso aqui rodar.

16:39

Pessoal, voltando aqui, ele está terminando de gerar já,

16:42

Já terminou de fazer as validações.

16:44

Então, primeiro ele explorou todo o nosso serviço de configuração,

16:49

Ele avaliou a segurança, categoria de segurança, avaliou os recursos,

16:53

Fez a avaliação de observabilidade, avaliou dependências.

16:58

Fez uma estimativa de custo e produziu no final um Read Checklist.

17:03

Então, está aqui o nosso checklist pronto.

17:07

Se você quiser, é que ele soltou na tela para você, mas se você quiser,

17:11

Você pode pedir para ele gerar em um arquivo .markdown também,

17:14

Para você conseguir colocar em outros lugares que formatam o Markdown. Então,

17:19

Qual é a validação que a gente tem que ver aqui?

17:21

Vamos validar. A gente pediu cinco categorias para ele. Segurança, recursos,

17:29

Observabilidade. E aqui, dependências.

17:32

Ele está gerando o resto aqui ainda. Vamos esperar.

## Resumo IA

[RESUMO_IA]