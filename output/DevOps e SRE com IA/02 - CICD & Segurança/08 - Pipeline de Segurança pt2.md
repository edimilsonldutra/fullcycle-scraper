Módulo: DevOps e SRE com IA\
Aula: [Pipeline de Segurança pt2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18506)

## Resumo da aula



## Transcrição

00:00

Na próxima etapa aqui, a gente vai falar alguns ataques versus mitigações,

00:05

então aquele do SolarWinds lá,

00:07

que é um build comprometido, onde que a gente ia conseguir pegar ele?

00:11

Aqui no SL, SA, no Corsair também,

00:15

no SBOM não, e no Kerberos a mesma coisa.

00:18

Aqui algumas outras que a gente tem, que é a parte de Backdoor,

00:22

Departamento, a gente pegaria aqui no nível 2,

00:24

no LCL2, que é um rastreamento aqui instantâneo

00:29

do raio de contágio, até onde que ele foi contaminado, ok?

00:37

O malha - seus inspections, que é a dependência que eu fui usando,

00:40

e o typo, palavra bem difícil, typo - scratching,

00:47

que é o S-bomb, S-cabinal,

00:49

que bloqueia na admissão, ok? Na admissão. O modo poisoning,

00:54

SignoStore para modelos, mais SBOM para modelos,

00:57

que vai assinar e inventariar e verificar no deploy.

01:03

Legal? E a parte aqui de LCP, a gente está em evolução ainda,

01:08

para ver como a gente pode evitar esses problemas, mas ainda está em evolução.

01:14

Então, a discussão central, nenhum mecanismo isolado vai cobrir tudo.

01:19

Então basicamente é o que eu disse no slide anterior,

01:22

não é só o Cosine que vai cobrir,

01:25

não é só o SL, SA que vai te dar toda a camada de proteção.

01:32

A gente precisa de várias camadas para conseguir chegar numa posição.

01:37

Então uma camada vai passando para outra e reduzindo como um

01:40

funil e no final você vai ter esses problemas de ataque mitigado.

01:47

Então, aqui tem uma discussão. Nenhum mecanismo isolado cobre tudo.

01:51

Defense Path é a estratégia.

01:53

Que é basicamente muitas camadas de

02:00

segurança para proteger o seu código.

02:03

Agora a gente vai falar um pouco da pipeline de segurança aqui.

02:08

Vamos criar uma branch nova para a gente subir essa pipeline.

02:12

Vamos gerar o security agent aqui, que é um arquivo .py,

02:18

que ele vai concatenar o resultado

02:20

lá do SonarQube mais o Trivy,

02:26

ele vai concatenar e fazer um comentário,

02:28

vai avaliar esses outputs desses dois ambisistemas para fazer

02:35

uma análise e comentar isso lá no nosso pull request.

02:40

Depois a gente vai gerar o nosso security YAML,

02:44

que é basicamente a nossa pipeline do YAML.

02:48

E vamos criar o push para a main para fazer rodar a pipeline de novo para subir.

02:52

A gente vai assistir aqui a parte do SonarQube mais o Trivy e

02:57

o security agent rodando e fazer o agent comentar no pull request lá, igual eu tinha dito.

03:04

Aqui é só um fluxo que a gente vai ter para fazer a criação disso, ok?

03:09

Então, vamos lá. Vamos aqui no Monamassa para a gente criar.

03:12

Aqui eu tinha mostrado que a gente não tem mais nenhum,

03:15

que é o K9S, né? A gente não tem mais nenhum.

03:19

Deixa eu mostrar aqui o namespace.

03:21

Ó, o namespace nosso está aqui certinho. A gente não tem mais nenhum. Pode execução.

03:26

Tudo desligado aqui, né? A gente fez o destroy dele na última etapa.

03:31

A gente tem o nosso run aqui rodando com sucesso.

03:33

Acho que eu não tinha mostrado na última, mas aqui é o job rodando.

03:38

Run job test, run job build,

03:41

Run job deploy e run job destroy aqui que eu rodei no final. Ok?

03:48

Deixa eu dar um zoom aqui para ficar mais fácil. Ok.

03:54

E por último aqui o nosso Open Code.

03:58

Então, nessa etapa agora, vamos fazer como a gente estava fazendo antes.

04:02

Vamos tirar a pipeline de deploy porque ela já está pronta lá.

04:05

Vamos dar um clear aqui, vamos subir,

04:08

Vamos mudar para branch checkout e main,

04:14

Vamos mudar para nossa branch main,

04:16

Se vocês notarem, sumiu aqui o nosso workflow, mas é igual a isso,

04:20

Vamos fazer um pull para a gente ficar atualizado lá com a branch main.

04:24

Nosso workflow, GitHub workflow, subiu aqui de novo.

04:28

Clear, vamos limpar, vamos fechar essa telinha por enquanto.

04:32

Vamos gerar um SecurityAgent. O que é esse SecurityAgent?

04:36

É um arquivo .py, que a gente gerou aqui,

04:43

A gente vai gerar via prompt. Esse arquivo .py,

04:46

Ele vai ser um arquivo que vai

04:50

Validar os outputs do Tivoli e do SonarQube.

04:54

Então, a gente vai dar um contexto para ele aqui, gere um script em agent,

04:58

Security Agent, para analisar o arquivo do SonarQube e Trivy.

05:03

Priorizar os blast rails usando LLM e postar um comentário, botou um R aqui, né?

05:09

Postar um comentário no pull request com o resultado da análise.

05:15

Contexto, script dentro do GitHub, e aqui tem todo o contexto do sistema,

05:19

Vocês podem ler com calma aí depois.

05:22

O script dev, buscar as issues do SonarQube via API REST.

05:26

Então, ele vai lá no SonarQube,

05:27

Pega as issues que a execução do SonarQube subiu, vai ler os finds do Trivy,

05:34

Que é um arquivo Trivy .json,

05:35

Que vai gerar quando a gente fizer a execução do nosso projeto,

05:40

Da nossa pipeline. Vai formatar isso para enviar para o LLM.

05:45

Vai chamar o LLM Space Prompt para priorizar o Batch Range em P1,

05:48

P2 e P3, que são aqueles níveis que a gente falou lá.

05:52

E vai postar um comentário com o resultado da análise usando o PyGitHub.

05:58

Então, ele vai usar o PyGitHub para fazer o comentário lá dentro do GitHub.

06:02

As variáveis de ambiente aqui que ele vai usar.

06:06

O SonarQube está rodando internamente na nossa máquina aqui também.

06:12

Tem um podzinho rodando dele lá,

06:14

Então, essa aqui é a variável de ambiente que ele vai usar. A autenticação,

06:17

Ele vai usar o que a gente colocou lá dentro

06:20

Das variáveis de ambiente que a gente criou do GitHub.

06:28

Ok? Sonar Project também, que vai ser o padrão, chave do projeto, Default, App API,

06:33

Aqui a gente colocou o Default, mas você pode colocar para ele gerar qualquer uma.

06:36

LLM Base, a gente está usando aqui localhost 234,

06:40

Que basicamente é o nosso LLM Studio, que eu vou mostrar aqui já já.

06:44

Modo LLM Name, o nosso padrão aqui é o Queen 3.5,

06:47

Vocês podem usar, se você tiver assinatura da OpenAI,

06:52

Assinatura do Anthropic,

06:54

Vocês podem usar também. Ok? E aqui a API Key,

06:58

Que vai estar também na nossa variável de ambiente lá dentro do GitHub.

07:02

Agent Path, que é onde o Path, que é onde o nosso agent vai se chamar,

07:09

Vai ser chamado. GitHub Repository, que é basicamente o owner / repo,

07:15

que a gente vai ter também na nossa variável de ambiente.

07:17

E o PR Number, que é o número do pull request. Ok?

07:21

Aqui é o app context, nome de serviço, o ambiente, que é staging, network zone,

07:27

que é internal VPN, e aqui só o runtime, que é um Python 3.11 usando FastAPI aqui.

07:35

Aqui é um output esperado,

07:37

então ele vai fazer um output nesse formato,

07:42

a gente deu aqui o output para ele criar o nosso código Python,

07:47

e o comentário no PR, então vai ter o título, a tabela, com P1,

07:52

P2 e P3. As seções detalhadas, por prioridade. E cada arquivo de ID,

07:57

título e remediation blast ratio. E os requisitos,

08:01

o PyHug GitHub e assim por diante.

08:04

E apenas o código Python, sem explicação adicional.

08:08

Esse output aqui é o output que vai sair do nosso código Python.

08:13

Esse aqui é o output que o LLM vai dar para a gente agora.

08:17

Com os nossos arquivos, com o nosso arquivo do agent em si. Então vamos aqui no

08:24

OpenCode, jogar aqui o nosso prompt e mandar ele gerar. Tá

08:32

pensando, mcard agent,

08:34

então ele acabou de criar uma pastinha que chama agent

08:37

aqui e tá gerando o nosso agent Python aqui, ok?

08:49

Vou dar um, demorando um pouquinho, vou dar um...

08:53

Fez a geração. Ia dar um pause na gravação e voltar assim que terminasse.

08:56

Mas ele acabou de fazer a geração aqui do nosso Python aqui.

09:00

Então aqui a gente tem o nosso Security Agent.

09:03

O que a gente tem aqui no nosso Security Agent?

09:06

São as nossas variáveis de ambiente, que ele já setou todas aqui.

09:09

O LLM base URL, o nome do modelo.

09:13

API Key, que basicamente é o LM Studio.

09:15

Nosso LM Studio está setado para não pedir API Key,

09:18

então ele colocou só uma default aqui, mas lá está setado com isso.

09:23

O agent patch aqui basicamente é o GitHub Token,

09:27

que é o token na variável de ambiente lá do GitHub.

09:32

Tem essa variável lá e ele vai usar.

09:35

Essa variável, na verdade, o GitHub Token é o token do GitHub. Então,

09:40

ele vai usar essa variável que está dentro do GitHub para alimentar esse cara.

09:43

Aqui estão os resultados do training, beleza?

09:46

Ele vai pegar o arquivo training.result.json e aqui o app.context, basicamente.

09:52

A gente tem aqui o system prompt, URL, senior, security age,

09:57

performance, e assim por diante. Tem toda uma contextualização aqui.

10:04

FetcherSendSonarHistories, então aqui ele vai pegar as histories que rodar,

10:07

quando a gente rodar a pipeline do Sonar, do SonarQube,

10:13

ele basicamente vai gerar pra gente os problemas que têm no código.

10:17

Então aqui a gente vai pegar esses problemas e

10:19

trazer pra dentro do nosso contexto da IA. Ok?

10:24

Vamos tirar essa parte, minimizar aqui.

10:28

WidgetDrivenResult, ele vai pegar aquele arquivo JSON que ele

10:30

gerar e vai fazer a leitura também. Ok?

10:34

Format finds for LLM.

10:37

Então, ele vai formatar todas aquelas informações que ele trouxe,

10:40

tanto do SonarQube quanto do Trivi. Vai formatar elas.

10:48

Minimizar, minimizar aqui. Ok. Fazer análise com LLM.

10:51

Ele vai mandar isso para o LLM e fazer a validação.

10:57

A validação não, né? A análise. O LLM vai fazer a análise para a gente.

11:00

E por fim... Ele vai fazer o build or comment.

11:03

Então ele vai fazer o comentário lá dentro.

11:06

Na verdade é que ele está montando o comentário,

11:08

desculpa. Ele monta o comentário, vai criar o documento,

11:11

o comentário para colocar lá dentro do nosso pull

11:14

request e depois vai fazer o post comment,

11:17

que ele vai fazer o comentário lá dentro, tá bom?

11:19

Aqui é só a classe main que faz a chamada de tudo e a orquestração.

11:23

Então o nosso agent vai fazer isso.

11:25

Ele tem várias etapazinhas para avaliar todas as partes de segurança e por fim...

11:30

fazer um comentário com o uso de

11:31

Generative AI lá dentro do nosso pull request, ok?

## Resumo IA

[RESUMO_IA]