Módulo: DevOps e SRE com IA\
Aula: [Introdução](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18519)

## Resumo da aula



## Transcrição

00:00

Fala pessoal, sejam bem -vindos ao módulo 1. Aqui começa a parte prática.

00:05

Se vocês ainda não configuraram o ambiente,

00:07

o Docker, K3D e Python,

00:10

pausem agora o vídeo e façam a configuração antes de continuar,

00:14

ok? Nesse módulo,

00:16

vamos partir de uma aplicação que já tem SLO definido e

00:21

vamos definir e vamos gerar todo o pacote de plataforma via AI.

00:28

Dockerfile, Docker Compose para o ambiente de Dev,

00:31

Manifesto Kubernetes para o ambiente de Prod,

00:34

o Rambook, que vai explicar como fazer o troubleshoot de toda a aplicação,

00:39

o DesignDoc,

00:40

que vai explicar a aplicação em si

00:43

e vamos construir duas skills reutilizáveis que toda

00:48

a equipe pode usar no seu dia a dia para fazer algumas coisas específicas da...

00:55

da aplicação e gerar alguns relatórios da aplicação em si, ok?

01:00

Então, vamos embora lá. Vamos fazer essa prática aí.

01:04

Então, pessoal, primeira parte aqui,

01:06

a gente vai falar um pouco das ferramentas que a gente vai usar durante esse módulo, ok?

01:11

Então, se tratando de LLM e as interfaces para conversação,

01:15

a gente vai falar do Open Code,

01:17

tá bom? A gente vai usar durante todo esse módulo o Open Code.

01:21

E o LLM Studio, se você não tiver nenhuma assinatura de LLM.

01:29

Algumas outras opções. O OpenCode Go é a opção paga do OpenCode,

01:34

que você paga 5 dólares e consegue ter acesso

01:36

a vários modelos top de linha do mercado,

01:39

modelos open source, que eles liberam isso para você.

01:43

Você pode também usar o CloudCode ou o Copilot, se for.

01:48

se você tiver ele disponível, ok?

01:52

No nosso caso aqui, no meu caso, que eu vou mostrar para vocês,

01:55

eu vou usar o OpenCode Go com alguns modelos como GLM 5 .1,

02:00

que é um modelo chinês,

02:03

é um modelo de alta performance que vai ajudar a gente bastante aqui.

02:07

Na parte de container e orquestração, a gente vai usar o Docker.

02:12

para fazer o build e o run dos containers que a gente precisa,

02:16

o build das imagens e o run do container, ok? Vamos gerar docker files,

02:21

docker composer e fazer o docker build para gerar a imagem,

02:24

beleza? Para a parte do Kubernetes,

02:26

a gente vai ter o K3D. O K3D, ele sobe um container...

02:32

cluster Kubernetes usando container Docker dentro da máquina.

02:36

Então você consegue ter um cluster Kubernetes interno dentro

02:41

do seu servidor para fazer os seus testes.

02:43

E a alternativa que vocês podem usar é o EKS ou GKE da Google.

02:48

EKS da AWS e GKE da Google. E para a validação do código,

02:52

a gente vai usar o Python 3 .11 mais o código de validação.

02:57

A gente vai usar o Python 3 .11 mais FastAPI.

03:00

e o Docker Build com o Dive Code Kubectl ali,

03:05

para a gente fazer a subida dos serviços em Kubernetes, ok?

03:10

GitHub Actions é o destaque de CSD,

03:13

mas a gente vai falar disso um pouco mais no módulo 2,

03:17

porque são eles que vão fazer o deploy automático para você.

03:21

Nossa regra aqui normalmente é sempre o software open source primeiro.

03:25

O ferramenta gratuita é sempre o começo.

03:26

Se necessário, você pode usar, se necessário,

03:30

se você tiver, você pode usar ferramentas pagas, aí no caso de cada um, combinado?

03:38

Aqui eu vou dar um destaque para a ferramenta do Open Code,

03:42

porque ela vai ajudar a gente em vários momentos aqui,

03:44

e ela executa em um diretório local da sua máquina, do seu computador, né?

03:51

Então, ela consegue gerar... toda a documentação, todos os artefatos,

03:58

tudo que for necessário dentro do próprio diretório do seu app que foi desenvolvido. No nosso caso,

04:04

a gente vai ter um app aqui. Vocês provavelmente vão ter disponível. Então,

04:09

vocês usam ele como exemplo para fazer as aulas aqui. Então,

04:14

a ordem do fluxo é os prompts.

04:16

A gente vai usar alguns prompts aqui que já estão pré-definidos.

04:19

Eu vou passar para vocês também.

04:21

A gente vai colocar esse prompt no OpenCode.

04:24

Esse OpenCode vai fazer a geração dos artefatos para a gente. No caso ali,

04:28

está mostrando que ele vai chamar o LM Studio se você fizer a stack toda local.

04:32

Se você rodar o modelo da LM local,

04:34

que vai gerar os artefatos e a gente vai fazer a validação. Essa validação,

04:38

a gente vai fazer a subida do serviço e vamos

04:42

rodar ele localmente e vamos rodar ele usando Kubernetes também. Então,

04:46

o OpenCode vai ser a nossa interface principal.

04:50

Esse OpenCode, eu estou usando o OpenCode Go, que eu já falei,

04:53

que é para a gente ter acesso a modelos de maneira mais fácil.

04:58

Mas fique ao seu critério usar ele ou qualquer

05:01

outro software de desenvolvimento que você use com AI. Combinado?

05:09

Agora, a gente vai alinhar um pouco aqui os conceitos do DevOps moderno de 2026, tá?

05:15

Então, o DevOps moderno de 2026 não é só CICD, ele é um ecossistema completo.

05:21

Então, ele envolve muita coisa do que uma esteira de CI/CD.

05:26

Então, ele tem o DORA 2025,

05:28

que são as métricas de Deploy Frequency, Lead Time, Change Failure, Rate e MTTR,

05:34

que eu já falei um pouco lá no módulo 0. Beleza? Então,

05:39

a gente precisa do DORA 2025 para ter

05:45

mais velocidade e governança na nossa stack de Deploy.

05:51

Ok, falamos um pouco do DORA 2025 e agora o segundo ali é o GitOps,

05:57

que sendo o Git como a fonte da verdade de tudo. Ou seja,

06:01

o estado desejado da sua infraestrutura é um arquivo YAML que está dentro do Git.

06:07

E um orquestrador como Argo CD ou Flux CD

06:11

faz a sincronização automática desses arquivos YAML,

06:14

que é o estado do seu cluster, para dentro dele, para dentro do cluster.

06:18

Faz o deploy para você, usando pipelines de CI/CD,

06:21

etc. E usando as branch master ou main,

06:24

dependendo do Git que você estiver usando, para fazer a sincronização. Combinado?

06:29

A Platform Engineering, em vez de cada time reinventar a roda, criamos Golden Paths.

06:35

Templates e plataformas internas que reduzem a carga cognitiva do desenvolvedor.

06:39

O desenvolvedor pede, quer um serviço com banco de dados.

06:45

A plataforma provisiona tudo. Ou seja,

06:48

você consegue criar coisas padronizadas de acordo com a estrutura da plataforma.

06:54

A plataforma vai servir todo mundo ali. O ponto é,

06:58

DevOps é uma cultura e método.

07:00

Então a gente tem que colocar essa cultura para dentro das empresas.

07:03

É o método certo de fazer as coisas.

07:07

Platform Engineer é o produto interno, que é o que entrega o DevOps.

07:11

O SRE é a engenharia de confiabilidade, onde a GNI atua em todos os três.

07:17

A GNI pode ajudar em todas

07:19

as três partes principais da infraestrutura,

07:24

como o código,

07:26

que seria a parte de... DevOps,

07:30

a parte de plataforma de linha e a parte de SRE, ok?

## Resumo IA

[RESUMO_IA]