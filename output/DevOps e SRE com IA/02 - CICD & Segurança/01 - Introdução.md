Módulo: DevOps e SRE com IA\
Aula: [Introdução](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18523)

## Resumo da aula



## Transcrição

00:01

Fala pessoal, bem-vindos ao módulo 2.

00:05

Nós vamos falar um pouco hoje de CI, CD, segurança e supply chain.

00:10

No módulo 1, a gente gerou os nossos artefatos via prompt,

00:16

via AI, usando o OpenCode.

00:22

Geramos Dockerfile, geramos manifesto Kubernetes,

00:25

geramos Homebrew e fizemos o deploy disso de maneira manual.

00:30

Então, a gente fez a aplicação ali do Dockerfile, dos manifestos Kubernetes,

00:35

dentro do nosso cluster Kubernetes, tudo de maneira manual. Nesse módulo agora,

00:41

nós vamos falar de como automatizar isso e como automatizar isso com segurança.

00:46

Então, a gente vai colocar alguns elementos de segurança aqui dentro do nosso IACD.

00:51

E vamos fazer a esteira mesmo de CI e CD,

00:53

que é Continuous Integration e Continuous Delivery,

00:57

que basicamente é a parte de integração e a

00:59

parte de entrega do sistema ali no ambiente,

01:03

dentro de Kubernetes, dentro de um EC2,

01:06

seja o local que você for fazer o deploy.

01:11

No nosso caso aqui,

01:12

a gente está fazendo dentro de um cluster Kubernetes usando o K3D ali.

01:17

Bacana? Então, esse módulo também.

01:20

Como módulo 1, a gente vai ter bastante mão na massa. Então,

01:24

a gente vai passar por algumas partes teóricas e vamos ter três demos.

01:29

Já está até escrito no primeiro slide que a gente está vendo.

01:33

A gente vai ter uma demo que vai fazer um

01:35

deploy dos nossos serviços através de uma pipeline.

01:40

A gente vai ter uma pipeline de segurança que vai entrar antes do deploy.

01:45

Então, precisamos passar por segurança para depois chegar no deploy.

01:49

E a gente vai ter uma pipeline de EVOL ali. Esse EVOL, basicamente,

01:52

a gente vai validar um prompt que vai estar dentro do nosso projeto.

01:57

Legal? Então,

01:59

isso vai andar junto com a pipeline de segurança

02:01

que depois vai liberar a pipeline do deploy. Vai lá? Beleza?

02:06

Então, vamos começar com a de deploy,

02:08

que é a parte que a gente vai fazer de fato deploy.

02:11

Depois a gente vai acrescentando as outras aí. Tá bom?

02:17

Então, vamos aí. Para a próxima parte.

02:21

Aqui eu vou falar só um pouquinho do que a gente vai usar aqui de ferramentas,

02:24

né? Na nossa primeira...

02:27

Nesse módulo. Então, basicamente,

02:30

é a mesma coisa que a gente já usou lá no primeiro módulo.

02:32

A gente vai ter aqui o nosso OpenCode Go, tá?

02:36

Que é o licenciamento mais barato aí do OpenCode.

02:39

A gente consegue usar vários modelos aí open source de maneira... De maneira fácil, né?

02:45

Então é 5 dólares ali o primeiro mês e você

02:48

consegue depois manter por 10 dólares por mês ali.

02:51

E igual eu falei, se vocês tiverem acesso a outros modelos,

02:55

outras plataformas, sintam-se à vontade em usá-los, ok? O LM Studio,

03:00

onde a gente vai rodar os nossos modelos locais aqui para fazer uns testes.

03:05

Vou mostrar para vocês como funciona.

03:07

E a OpenAI SDK, onde vai fazer as chamadas dentro do nosso código.

03:13

A gente vai gerar um código em Python aqui também.

03:15

Para fazer a parte de validação de segurança.

03:17

E vamos usar a OpenAI SDK para fazer a conexão no LV Studio. Além do PromptFull,

03:23

que vai ser usado para validar os nossos prompts

03:26

aqui de sistema quando eles tiverem alguma mudança. Ok?

03:31

E a parte de qualidade e segurança, a gente vai usar o SonarQube,

03:35

que vai fazer a avaliação estática,

03:38

a análise estática do código, do nosso código, ok?

03:42

O Trivy, que vai fazer o scan de vulnerabilidade do nosso código.

03:47

E o ActionLint, que vai fazer a validação do nosso GitHub Actions,

03:52

que é a pipeline que a gente vai gerar.

03:54

A pipeline que a gente vai usar para fazer

03:56

tanto o deploy quanto a parte de segurança, beleza?

04:00

O eval prompt aqui, que a gente vai usar o prompt full. E o LLM Duke,

04:06

que é a técnica de avaliação automática para validar

04:10

se o nosso prompt está bacana para ser usado.

04:13

E esse ICD, a gente vai usar o GitHub Actions,

04:16

que basicamente é de graça.

04:20

Eu vou mostrar para vocês como a gente pode configurar uma pipeline para rodar.

04:25

E como que a gente pode configurar isso para rodar localmente na nossa máquina,

04:30

no nosso computador local.

04:33

Tem como fazer,

04:34

a gente vai usar a estratégia de orquestração do GitHub Actions,

04:41

porém ele vai executar coisas dentro da nossa máquina,

04:44

dentro do nosso computador que a gente está trabalhando aqui.

04:49

Vou mostrar para vocês o passo a passo de como configurar isso. Ok?

04:54

PyGithub, para fazer interações ali com o GitHub, se for necessário, e o OpenAI SDK,

04:59

que vai consumir o LV Studio ali para fazer algumas partes também,

05:03

ok? Então, a gente vai ter, igual eu falei,

05:05

três demos, que a gente vai fazer o deploy,

05:07

o push para o K3D, vamos fazer a parte de segurança, usando o SonarQube,

05:12

mais TIF, mais LLM, para fazer um comentário lá no nosso pull request,

05:18

e fazer um eval ali, para a gente validar a parte do nosso prompt que a gente gerar. Combinado?

05:24

Então, essa é uma introdução aqui do que a gente vai fazer.

05:27

Eu volto no próximo vídeo para a gente

05:30

iniciar as nossas demos e as nossas partes teóricas.

05:36

Combinado, pessoal? Muito obrigado. Aquele abraço.

## Resumo IA

[RESUMO_IA]