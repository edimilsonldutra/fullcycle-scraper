Módulo: DevOps e SRE com IA\
Aula: [Pipeline de Eval de Prompt pt1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18527)

## Resumo da aula



## Transcrição

00:01

Vamos lá, pessoal. Estamos de volta.

00:03

Vamos para a nossa última pipeline aí que a gente vai construir nessa aula,

00:08

dessa aula aí do módulo 2, né?

00:13

Vamos falar um pouco aqui de pipeline de EvolProp. O que é isso, tá, gente?

00:20

O EvolProp, se vocês notarem,

00:25

nós temos aqui dentro do nosso security agent.

00:29

A gente tem um prompt que vai definir o que esse security agent vai fazer. Então,

00:36

esse prompt foi construído para ele fazer a

00:38

avaliação dos resultados que chegarem do SonarQube

00:43

mais o Trivy e te entregar essas avaliações

00:46

para você conseguir seguir com o seu merge request,

00:51

com o seu pull request, fazer o merge dele para a sua branch principal, que é a main.

00:58

Então, com esse eval aqui,

01:02

a gente vai conseguir evitar que alterações nesse prompt possam

01:08

atrapalhar o resultado da sua avaliação do agent lá no final,

01:13

depois que ele processa os outputs do SonarQube mais o Trivy.

01:18

Então, imagine que hoje a gente construiu um prompt,

01:21

ele está funcionando 100%, está fazendo a avaliação conforme esperado.

01:25

Aí depois de determinados dias ou momentos, alguém vai lá e altera esse prompt,

01:30

ele para de fazer essa avaliação. Então,

01:33

faz essa avaliação de maneira assertiva, né?

01:36

Ele começa a alucinar,

01:37

a fazer outras coisas ali que você não definiu no prompt do sistema.

01:41

Então é aí que entra a parte do eval prompt dentro da pipeline,

01:46

pra gente evitar... que isso aconteça. Então, prompt degradado.

01:51

Alguém remove alguma coisa de lá de dentro que você escreveu,

01:55

o modelo começa a fazer coisas que você não pediu, que você não definiu,

02:00

e isso pode gerar algum problema ali. Então, qualquer solução,

02:04

a gente vai ter um arquivinho de system.md, que vai ser versionado com o git.

02:09

Toda vez que alterar, ele vai ser versionado.

02:12

Alterou um arquivo desse,

02:13

ele vai disparar o eval automaticamente para aquele arquivo. Legal?

02:17

É aquele arquivo .md. Então, a gente vai rodar o prompt full,

02:22

que é um sistema para fazer avaliações desse prompt,

02:25

que foi com mais de 20 testes aí,

02:28

né? A gente colocou aqui 20 testes de

02:30

acurácia, relevância e toxicidade daquele prompt.

02:34

E eu vou mostrar para vocês aqui como que a gente vai

02:37

conseguir usar pipeline para fazer essa avaliação de maneira automatizada e rápida.

02:44

O pipeline vai usar um LLM local,

02:47

o nosso aqui que a gente está usando lá no LLM Studio,

02:50

igual o nosso agent em Python, o agent de segurança que usamos.

02:54

E a gente vai conseguir fazer essa avaliação de

02:57

maneira mais assertiva para evitar problemas com o prompt.

03:02

Problemas que alguém alterou e aquele prompt para de ser assertivo

03:06

e o LLM não te entrega o que é necessário ali. Então,

03:12

vamos lá. O que a gente tem aqui? Prompt version com LLM STD Google.

03:17

Versionar o prompt com LLM julgando se aquilo que a gente está no prompt,

03:22

se aqui a gente passar para ele,

03:25

aquele prompt vai responder de maneira assertiva. Então, basicamente,

03:29

A demo 2 aqui que a gente criou lá,

03:31

O nosso serviço, o nosso...

03:37

Nosso avaliador dos outputs,

03:40

A gente vai avaliar aquele prompt ali e se tiver alguma alteração,

03:43

A gente vai fazer uma nova avaliação dele.

03:45

Ok? Então, basicamente, vamos lá,

03:50

Vamos começar a criar aqui, tá? Então,

03:53

A gente vai criar uma pasta dentro do nosso projeto que vai chamar Prompt System MD,

04:00

Beleza? Vamos lá dentro do nosso projeto.

04:05

Basicamente, o que a gente tem aqui? Se vocês notarem, dentro do agent,

04:10

A gente tem aqui o prompt que está setado direto.

04:12

O ideal seria a gente estar referenciando um arquivo de prompt,

04:17

Que seria esse arquivo que eu estou colocando aqui agora, prompts.

04:21

Vou colocar essa pastinha, que a gente tem aqui um arquivo de prompts,

04:28

Que é esse systemd.

04:29

É exatamente aquele mesmo prompt que a gente tem lá no nosso agent, tá bom?

04:35

E assim por diante. A gente tem esse módulo.

04:39

Você é um engenheiro. Só que tem em português.

04:41

E assim por diante. Está tudo descrito aqui.

04:46

Dentro desse System.md. Se alguém alterar alguma coisa aqui,

04:51

Por exemplo, tocou P1 de Critical Key para Low.

04:53

Isso pode afetar diretamente o nosso projeto,

04:59

A nossa avaliação. Que o LLM vai fazer,

05:07

Das saídas do Trivy e do SonarQube.

05:10

Então isso aqui tem que ser alterado de maneira gerenciada e versionada.

05:15

Então é aí que entra. Versionar,

05:17

Faz a avaliação do prompt. Versionar de novo,

05:20

Faz uma nova avaliação do prompt com o prompt full. Legal?

05:25

Para usar o prompt full, a gente tem aqui,

05:28

Vamos voltar aqui no nosso slidezinho, nós temos aqui,

05:34

O promptful config, tá bom? Mais o teste -evol.yaml,

05:39

Que são os casos de teste que a gente vai testar.

05:41

Então eu tenho aqui um arquivo de configuração já pronto.

05:44

Vamos voltar lá no nosso terminal. Vou

05:49

Dar um clear aqui.

05:53

Vamos fechar aqui. Vamos voltar aqui no nosso repositório.

05:56

E vamos puxar aqui o promptful.config.

06:00

Peguei esse promptful.config. Ele é só uma descrição do que o promptful vai fazer.

06:07

Os providers aqui a gente está usando, no caso, o GPT-3.5,

06:10

Com a API OpenAI aqui, né? A gente está usando o protocolo OpenAI para fazer.

06:17

Protocolo não, né? O contrato de API OpenAI para fazer,

06:20

Usando o LL local nosso aqui, com o MacStore aqui, essas coisas configuradas.

06:26

Os properties.

06:28

Aqui a gente vai listar todos. No nosso caso,

06:31

A gente só tem o prompt -system.md, que está aqui.

06:34

E vamos colocar os testes aqui que vão ser feitos em cima desse prompt. E os testes,

06:39

A gente tem um arquivo que se chama eval.yaml,

06:42

Que está até descrito aqui no nosso slide,

06:45

Que é o eval.yaml. E esse eval.yaml,

06:48

A gente vai colocar ele dentro aqui de testes.

06:52

Ok? Então, o que tem nesse arquivo? A descrição de que é esse teste.

06:57

Um input, que é o CVE 2024, backdoor, compressor, e assim por diante.

07:02

Ele vai fazer a avaliação desse input e vai retornar se a severidade dele é P1,

07:08

e se inclui,

07:10

e se não inclui isso aqui. E aqui, várias coisas aqui, se a severidade dele é P2,

07:15

P3, e assim por diante. Então,

07:18

você configura... o retorno do LLM,

07:23

você vai pedir que o LLM retorne aquilo num JSON válido ou qualquer outra coisa.

07:28

E vai conferir através desse JSON parse aqui se o retorno do LLM foi válido.

07:35

O que é que meio que você dá? Eu estou mandando...

07:38

Essa informação. Eu sei que essa informação era do tipo P3.

07:42

Será que o LLM vai retornar o P3 com aquele prompt que eu mandei?

07:46

Então é aqui que você vai validar isso, se o prompt de fato está sendo efetivo.

07:51

Mesma coisa aqui em cima. Eu sei que esse sonar cúbico,

07:54

SQL injection, no endpoint de use,

07:57

contratação direta e assim por diante, eu sei que a severidade dele é P1.

08:02

Será que quando o LLM avaliar...

08:04

Com aquele prompt, com esse system prompt aqui, quando eu mandar esse texto pra ele,

08:09

ele vai me retornar uma severidade P1. Então é isso que o prompt evolve vai fazer.

08:14

Entendeu? Então, se a partir do momento que eu troco esse cara aqui,

08:18

coloco esse cara e retorno aqui um P3,

08:21

se o LLM retornar outra coisa, tipo assim,

08:26

se ele retornar outra coisa que não seja o P3,

08:28

ele vai falhar meu job e vai bloquear o meu...

08:33

O meu versionamento do prompt, o meu merge ali do prompt,

08:38

ok? Então a gente vai fazer um teste aqui,

08:41

o primeiro teste subindo esse cara para ver o prompt full fazendo a avaliação dele,

08:46

tá? Vocês podem usar qualquer outro aqui, qualquer outro provider.

08:57

Aqui está usando o local, mas você pode usar o OpenAI,

08:59

pode usar o Drop, e assim por diante, tá? Mas antes disso,

09:03

a gente tem um outro prompt aqui que a

09:05

gente vai conseguir gerar o pipeline de Evolve. Deixa eu pegar ele aqui.

09:13

Vou mostrar aqui para vocês o que é o nosso

09:17

prompt para gerar o YAML da nossa pipeline de Evolve. Então,

09:23

gera um GitLab Actions com YAML, e assim por diante, seguindo.

09:27

Aquela mesma estrutura que a gente criou para deploy e security,

09:31

ok? Vou copiar ela aqui, não vou ler tudo,

09:33

e depois vocês dão uma olhada com mais calma,

09:35

que vai ficar disponível para vocês, tá?

09:38

E a gente vai jogar isso dentro do nosso open code.

09:43

Aqui está o código, e aqui está o...

09:48

Gente, sumiu? Terminou, achei. Dentro do open code. Vamos colar aqui, e vamos...

09:55

Esperar ele gerar o nosso YAML workflow ali,

09:58

para a gente subir essa última pipeline. Então

10:04

Vamos ver aqui, já

10:08

que pensando, ok,

10:12

gerado, a gente tem um Evolve aqui agora,

10:16

que vai fazer a instalação do PromptFull, vai fazer o npm install,

10:20

vai rodar aqui o LM Studio,

10:22

mandando o arquivo de configuração que a gente colocou aqui embaixo.

10:26

O arquivo de configuração referencia o prompt que a gente quer avaliar,

10:29

mas as avaliações que ele precisa fazer nele.

10:32

E depois vai ter um código em Python aqui que vai checar a acurácia daqueles dados.

10:38

Se 80%, 85%, 0,25% de acurácia,

10:43

acima de 0,25% a gente tem uma acurácia ok.

10:46

Se a gente estiver abaixo disso, a gente tem uma acurácia,

10:50

nosso prompt não está... fazendo o que eu deveria fazer.

10:53

Ele não está classificando corretamente o que a gente precisava.

10:57

Ah, detalhe, nosso prompt aqui embaixo tem alguns exemplos também,

11:00

tá? De input, do que as coisas vão retornar,

11:04

que a severidade P1 e assim por diante, ok? Então,

11:07

dentro do prompt vai alguns exemplos também do que acontece.

11:11

Então, vamos lá. Já coloquei aqui o nosso Evolgator. Vamos fechar essa parte aqui.

11:18

Abrir um novo terminal.

11:22

Vamos fazer um git checkout -b,

11:26

subir workflow prompt evolve, ok?

11:30

Vamos fazer um git add ponto, git commit, subir workflow prompt evolve.

11:38

A gente já tem esse commit aqui, já estava escrito aqui.

11:42

Ok? Então, git push origin, subir workflow prompt evolve.

11:48

E vamos mandar essa branch nova lá para o GitHub.

11:55

Vamos abrir o GitHub aqui. A gente tem três branches, tá?

11:59

E a que a gente subiu agora está aqui. Subir workflow prompt eval.

12:04

A partir do momento que eu criar aqui o pull request para essa branch,

12:10

vamos criar esse pull request aqui agora. Prompt eval.

12:16

Vamos criar esse pull request. O que a gente tem aqui, tá?

12:20

o Promptful YAML, que a gente subiu, o Prompt System,

12:25

os testes aqui do Evol, e aqui tem o Evolgate YAML,

12:31

que é o nosso workflow. Vamos criar o pull request.

12:34

Vamos continuar aqui só copiando e colando para a gente ganhar um tempinho.

12:40

Criar pull request.

12:42

Automaticamente aqui dentro de Actions, ele vai iniciar dois workflows.

12:48

O primeiro workflow é o do security, que a gente tinha feito na etapa anterior.

12:52

Eles estão parados aqui. E o workflow acima,

12:55

que já está rodando, é o de eval do prompt. Então,

12:58

ele está fazendo aqui a instalação do prompt full.

13:03

Então, ele usa o npm para fazer a instalação.

13:08

Deixa ele terminar de fazer aqui. Logo em seguida, tem um job de run.

13:12

prompt eval, prompt full eval,

13:15

que ele vai rodar de fato a avaliação daquele prompt

13:18

em cima daqueles testes que a gente criou,

13:20

que a gente pediu para ele criar.

13:23

Deixa ele terminar aqui.

## Resumo IA

[RESUMO_IA]