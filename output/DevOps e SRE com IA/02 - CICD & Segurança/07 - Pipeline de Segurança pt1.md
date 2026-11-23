Módulo: DevOps e SRE com IA\
Aula: [Pipeline de Segurança pt1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18522)

## Resumo da aula



## Transcrição

00:00

Então é isso aí, pessoal. Bora continuar aqui.

00:03

Vamos agora implementar uma pipeline de segurança

00:06

que vai ser executada antes do nosso deploy.

00:11

Essa pipeline visa fazer alguns scanners dentro do nosso projeto,

00:16

dentro do nosso sistema,

00:18

antes de, de fato, fazer o deploy para o nosso ambiente.

00:22

Então vamos fazer a automação usando o SonarQube mais o Trivy.

00:29

para fazer algumas avaliações,

00:30

e o LLM para juntar

00:35

essas duas avaliações dos dois

00:39

sistemas e dar um parecer final para a gente de segurança.

00:44

Essa pipeline, diferente da outra que roda no merge para a branch main,

00:50

essa vai rodar no momento que a gente fizer a abertura do pull request.

00:55

Fez a abertura do pull request, essa pipeline entra.

00:58

e ela vai definir se a gente pode ou não fazer o merge para main,

01:03

que no caso é o deploy,

01:05

né? A gente pode ou não fazer o merge para

01:06

main para iniciar o deploy do nosso serviço, ok?

01:10

Então, o PR, o pull request como ponto de controle, ou seja,

01:15

feito o pull request,

01:17

é onde o código vai

01:19

pedir permissão para entrar em deploy.

01:25

Então, o código vai executar ali, feito por pull request,

01:29

vai começar a parte de segurança, de qualidade do código,

01:32

e vai ter mais uma pipeline, que é essa pipeline de segurança.

01:37

A gente tem uma outra mostrando aqui,

01:39

só que ela vai ser a próxima pipeline que a gente vai desenvolver,

01:41

na última demo aí,

01:44

né? Então, a gente tem mais essa aqui que a gente vai colocar, ok?

01:49

Então, o merge vai ser bloqueado até o security agent rodar, mas o eval accurate,

01:55

que é a outra pipeline que a gente vai rodar. Então,

01:57

adiantando um pouco aqui como vai funcionar as coisas.

02:00

O code owner e o sign commit continuam obrigatórios,

02:04

então tem as aprovações de code owner, etc.,

02:07

mesmo com os pipelines gerados por IA,

02:10

mesmo com o comentário que a nossa avaliação fizer com o IA. Ok?

02:19

Então, vai funcionar basicamente assim. A gente vai ter uma avaliação do SonarQube,

02:25

vai ter uma avaliação do Trivy, com a CBS,

02:28

imagens de problemas. Então, se tem uma lib que foi comprometida, etc.

02:34

Esse Trivy vai falar isso pra gente. A gente vai ter o SonarQube aqui,

02:38

onde a gente vai ter alguns códigos e smells aqui, de vulnerabilidades, essas coisas.

02:45

E a gente vai ter o contexto para a gente mandar

02:48

para a IA para ela fazer a avaliação para a gente. Legal?

02:52

A gente vai desenvolver um agent em Python, mais o uso do LLM aqui.

02:57

No meu caso, estou usando o LLM local, que é o GPT-3.5.

03:02

Usando o LLM Studio. Vou mostrar para vocês aqui como funciona.

03:05

E a gente vai consolidar tudo isso e fazer um

03:08

comentário no pull request para o pessoal fazer a avaliação,

03:13

aprovar. E se for aprovado, seguir para fazer o deploy. Ok? Então,

03:18

aqui tem RCE em repositórios públicos.

03:24

que a gente consegue validar.

03:27

O CVE também em alguns serviços internos e assim por diante.

03:32

E tem um CodeSmart que são funções internas aqui. Ok?

03:36

Próxima parte aqui é um supply chain, que é um vetor de ataque.

03:39

Então, aqui a gente tem alguns ataques reais que já aconteceram aí.

03:44

Tipo o que aconteceu em 2020 com SolarWinds, que é um build de CISO comprometido,

03:49

então tinha comprometido o uso do SolarWinds aqui.

03:54

Esse XE Utils aqui, que é uma biblioteca,

03:58

que foi injetada uma parte de SSH lá dentro, que poderia fazer invasões em máquinas.

04:04

Dependência de Confusão, que pode colocar código,

04:09

pacotes maliciosos dentro do seu projeto aí. Legal.

04:15

Aqui alguns ataques específicos de AI, que é esse Model Poisoning,

04:20

que é basicamente modelos com backdoors nos pesos,

04:24

então ele pode abrir o backdoor dentro do seu servidor,

04:28

que pode facilitar o uso de ataques hackers, etc.

04:32

Funciona normalmente 99% das vezes,

04:35

executa uma ação do atacante quando

04:39

recebe algum input com um padrão específico.

04:43

Então, basicamente,

04:44

se um atacante gerar um modelo que tem esse model-posing,

04:50

ele vai conseguir mandar algum prompt específico que esse modelo vai aceitar,

04:57

processar e abrir um backdoor ali no seu sistema.

05:00

Legal? Prompt-posing via dependências. Então,

05:04

prompts injetados via documentos de RAG. Então,

05:07

você pode ter várias RAGs que você consegue injetar esses prompts lá dentro,

05:12

que vai contaminar o system prompt e outras partes da sua AI.

05:18

E o atacante não ataca o modelo diretamente.

05:21

Ele ataca os dados que o modelo consome.

05:23

No caso, os dados que estão na nossa base de conhecimento.

05:26

Pode acontecer deles fazerem ataques.

05:29

Alguns exemplos que a gente tem de problemas de ataques.

05:35

E por último, o tool pausing via MCP,

05:37

que é simplesmente servidores MCPs que vão

05:39

devolver códigos parecidos para a AI executar.

05:45

Então, a gente tem diversos servidores MCPs públicos aí

05:49

na internet que a gente pode usar,

05:51

porém a gente tem que tomar bastante cuidado para fazer o uso desses servidores,

05:54

desses serviços MCPs, antes de colocar dentro do nosso ambiente.

06:00

Com isso, a gente pode criar regras dentro das nossas pipelines,

06:04

onde a gente valida isso tudo antes de colocar dentro do nosso ambiente.

06:08

Só falei um pouco aqui de segurança para vocês entenderem

06:11

o que é possível colocar dentro da nossa pipeline.

06:14

Então, a gente consegue fazer vários tipos de

06:21

teste antes de fazer o deploy de fato.

06:25

Algumas mitigações aqui de ESL e ESA.

06:31

SAST, SBOM, mais Clifford. Então, a gente tem aqui SLCA, que é o framework,

06:37

que ele é um artefato construído, como se diz, de três níveis.

06:45

Então, a gente tem os três níveis, que é L1, que é o provenance documentado.

06:51

O L2, que é o build platform hospedado com provenance assinada.

06:56

E o L3, que é o build hardening, não.

07:00

Falsificável. SolarWinds seria mitigado em L3,

07:04

que é o build adulterado que não teria a província validada.

07:10

Então ele consegue fazer alguns tipos de validação. O SLSA responde,

07:16

esse artefato foi realmente construído da forma que eu digo?

07:19

Basicamente é isso, entendeu?

07:22

O SignalStoreStack, que ele tem essas partes aí de fusil,

07:28

que vai ser a IODC assinatura de Keyless.

07:31

Então, valida algumas assinaturas.

07:33

Assinaturas do container de Keyless e a transparência do log imutável. Então,

07:40

ele responde essa pergunta. Quem assinou esse artefato e quando?

07:43

Então, tem lá um carimbo de quem assinou.

07:47

Então, a gente consegue usar esses caras para

07:49

validar várias coisas antes da continuidade na pipeline.

07:55

A gente tem um SBOM, que é o Software Bill of Materials,

07:58

que a gente tem um formato ali focado em segurança,

08:01

formado pela OWASP, que é focado em segurança. O SPDX3,

08:07

que é o padrão líquido da Linux Foundation,

08:09

é gerado no build, consumido no deploy,

08:13

e permite rastrear os CVS transitivamente.

08:17

Então a gente consegue rastrear vários CVS ali que vão aparecendo. Legal?

08:23

Esse Kiberno Administration Controller, que verifica validações,

08:27

províncias e SBOM de admissões.

08:32

Bloqueia deploys sem assinatura da COSIGN,

08:35

então ele consegue fazer bloqueios de deploy para evitar

08:39

que a gente coloque código malicioso dentro do ambiente.

08:43

Valida SBOM, que é o que a gente falou no anterior.

08:50

E um policy as code, que é um policy de vacinação no Git.

08:53

Então a gente consegue usar essas mitigações aí

08:56

de segurança dentro da nossa pipeline.

08:59

Legal? E isso é possível porque a pipeline

09:03

dá essa possibilidade de a gente executar. Entendeu?

09:06

Então o fechamento é tipo SLSA, SIGNAL STORE, SBOM, GITHUB,

09:12

SUPLATIA e verificável end-to-end. Então a gente consegue verificar

09:19

a nossa entrega de código do início ao fim ali.

09:21

Nenhum mecanismo isolado cobre tudo. Então, basicamente,

09:26

não é uma coisa que vai te cobrir de todos os problemas do mundo,

09:31

de todos os problemas de ataque que tem aí em vários softwares por fora.

09:38

Então, a gente tem uma camada ali toda de defesa, uma camada...

09:44

complexa ali de defesa para evitar esses problemas.

09:49

Então a gente usa esses frameworks para fazer esses trabalhos.

## Resumo IA

[RESUMO_IA]