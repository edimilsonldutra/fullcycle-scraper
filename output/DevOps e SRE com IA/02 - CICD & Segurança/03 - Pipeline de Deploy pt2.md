Módulo: DevOps e SRE com IA\
Aula: [Pipeline de Deploy pt2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18525)

## Resumo da aula



## Transcrição

00:00

Então, primeiro passo. Na aula anterior,

00:02

a gente viu que a gente gerou o nosso código aqui,

00:07

que está até aqui. A gente tem o app,

00:09

a gente tem aqui os arquivos de configuração do Kubernetes,

00:15

do K8S, o nosso handbook, os nossos testes aqui, e assim por diante.

00:20

A gente gerou a documentação também, está tudo aqui.

00:23

O primeiro passo que a gente vai fazer é...

00:28

Vamos criar um repositório no GitHub.

00:31

Se você não tem uma conta do GitHub, vocês podem criar essa conta,

00:36

é gratuita, não tem nenhum problema aí. O uso do Actions aqui também,

00:42

quando você usa o seu Self Hosted também é gratuito, então é bem tranquilo.

00:48

Vocês podem notar aqui que a gente tem a mesma

00:50

estrutura de arquivos que a gente tem aqui dentro do nosso...

00:57

do nosso projeto, que já está tudo aqui dentro,

00:59

ok? E nós temos aqui uma branch criada,

01:03

que é a nossa branch main, que é a branch principal,

01:06

e temos aqui dentro dessas partes aqui em cima,

01:12

a gente tem algumas abas aqui de issues,

01:15

por exemplo, se for um projeto interno e tiver algum problema,

01:20

o pessoal consegue abrir issues,

01:21

que são os problemas para vocês resolverem. Por request,

01:24

que basicamente quando a gente vai fazer o request para dentro da nossa branch,

01:29

para dentro da branch main, a gente vai passar por essa telinha. Os agents,

01:33

que a gente pode usar aqui também, criar agents de AI, etc.

01:37

Porém, a gente não vai entrar nessa parte. As actions,

01:40

que é onde vai rodar as pipelines de fato.

01:43

Temos aqui vários exemplos de actions que a gente pode usar.

01:48

Aqui os projetos, que é uma parte mais administrativa,

01:51

a gente pode criar projeto, atrelar o projeto e assim por diante.

01:54

Security Quality, a gente pode configurar várias partes de segurança aqui dentro,

01:59

nós não vamos entrar nesse mérito aqui agora.

02:03

Insights, que a gente pode ver quantos commits foram feitos,

02:06

quem que commitou, quando as coisas aconteceram.

02:09

Então tem aqui alguns testes que eu fiz aqui para a parte do pull request,

02:13

a gente consegue ver quantos commits foram feitos aqui, etc.

02:16

quantas issues que tem e assim por diante.

02:18

E aqui as configurações do repositório, ok?

02:22

Primeira parte aqui, vamos aqui em Settings, ok? Em Settings,

02:28

a gente tem aqui a parte de Actions,

02:30

na parte esquerda aqui, e a gente tem a parte de Runners.

02:35

Se vocês notarem, a gente tem o Runner API,

02:38

que esse cara aqui é basicamente o que está rodando dentro da minha máquina.

02:42

Então aqui a gente tem até um Self Hosted,

02:44

MacOS e um A64, ok? Para você fazer a configuração,

02:49

você vai simplesmente clicar nesse botão Self Hosted e aqui você tem um passo a

02:55

passo de como você vai fazer a

02:57

inicialização desse Self Hosted dentro da sua máquina.

03:03

O GitHub se comunica através da internet mesmo,

03:08

então ele vai conseguir mandar os comandos da internet

03:10

para a sua máquina fazer a execução.

03:12

E aqui tem um passo a passo de como você pode fazer isso.

03:15

E aqui você pode selecionar o seu sistema operacional,

03:18

no meu caso aqui é o macOS, na arquitetura ARM64.

03:23

Podemos selecionar Windows, podemos selecionar Linux também e assim por diante.

03:29

Temos várias possibilidades aqui e você vai fazer a configuração.

03:33

Basta seguir esse passo a passo. Bem simples, tá gente, vocês fazerem.

03:37

Eu falei um pouco das variáveis,

03:39

a parte que interessa para a gente aqui é a parte das variáveis

03:43

que estão aqui dentro de secreted variables e a gente tem um action,

03:47

uma parte de actions aqui. Se vocês notarem,

03:52

lá dentro do nosso YAML que a gente gerou para a pipeline,

03:56

a gente vai puxar várias variáveis de ambiente e elas estão aqui, ok?

04:02

Simplesmente vocês podem vir aqui dentro de Actions

04:05

e criar um New Repository Secret.

04:07

Você vai colocar o nome da sua Secret e o valor dela.

04:12

Legal? Essa Secret você pode utilizar ela.

04:15

Ela fica guardada aqui de maneira segura.

04:21

E você pode utilizar ela dentro da sua Pipeline. Então,

04:26

isso aqui é bacana para você guardar seus dados aqui e

04:29

deixar aqui para usarem várias Pipelines se for preciso. Ok? Então,

04:33

vamos lá para a gente gerar o nosso

04:38

workflow de pipeline para a gente rodar lá dentro. Legal?

04:44

Primeira parte. Vamos aqui abrir o nosso OpenCode dentro do nosso repositório.

04:49

Se vocês notarem aqui,

04:50

a gente já tem um repositório API na branch main.

04:55

Então, a gente vai abrir o OpenCode aqui. Ok? OpenCode aberto.

05:01

Vamos no primeiro prompt aqui que vai

05:07

ficar disponível para vocês usarem aí também.

05:10

Então vou copiar o prompt aqui,

05:12

vou colocar aqui na telinha, igual a gente fez nas últimas vezes,

05:15

para a gente acompanhar o que tem escrito nesse prompt.

05:18

Então vamos lá. Deixa eu quebrar essas linhas para ficar mais fácil de ler. Então vamos lá.

05:25

Gere um workflow do GitHub Actions para deploy de uma aplicação no K3D.

05:31

Estamos usando o K3D. O K3D já está rodando localmente.

05:34

O cluster é o meu cluster que a gente criou. E o workflow tem três caminhos.

05:40

Primeiro, o push para a main, que vai fazer o merge do PR,

05:44

fazer o teste e o build vai iniciar.

05:46

Tem outra parte que é o manual deploy e o manual destroy que a gente vai fazer.

05:52

Contexto repositório, linguagem, Python 3.11.

05:55

A gente vai descrever tudo do nosso projeto aqui.

05:58

O workflow deve incluir triggers para main, enquanto vai disparar esse cara,

06:03

e workflow dispatch com input de actions,

06:06

que a gente pode fazer um redeploy ou um destroy aqui. O job 1,

06:13

a gente vai aqui descrever o que ele deve fazer.

06:16

O job 2, vamos fazer que o nome vai se chamar build.

06:21

O job 3, que é o deploy de fato.

06:24

O job 4, que vai ser o manual deploy, que vai rodar no self-hosted.

06:29

Aqui ele está informando, eu estou informando aqui de cada um onde ele vai rodar.

06:34

Porém, você pode colocar um geral lá em cima,

06:39

todos os jobs vão rodar em tal lugar. Ele vai obedecer isso também.

06:42

E aqui a gente vai ter o Job Cycle, que é a parte de destroy do nosso projeto.

06:48

Basicamente, o destroy vai destruir tudo o que a gente criou lá dentro.

06:52

Aqui algumas condições que a gente colocou.

06:55

Que estão definidos no nosso workflow, e o pré-requisito. Usar o Actions,

06:59

a versão em V4, não usar o Docker Base de Actions,

07:03

o RAM do Microsoft Search Host. O K3D já está rodando,

07:07

não precisa criar cluster. E salvar no .github,

07:11

workflows, deploy e enable. Então, basicamente,

07:14

ele vai criar aqui um arquivo, uma pasta oculta para a gente,

07:18

que vai se chamar .workflow. Então, vamos copiar todo esse prompt aqui. Copiar.

07:25

E vamos colar aqui no nosso Visual Studio Code,

07:27

aberto dentro do repositório do nosso projeto, ok? Vamos lá.

07:35

Tá lendo aqui, agora ele criou o arquivinho lá pra gente, .github/.workflows,

07:41

e acabou de gerar o workflow lá pra gente,

07:47

todo o workflow que a gente precisa lá. Legal?

## Resumo IA

[RESUMO_IA]