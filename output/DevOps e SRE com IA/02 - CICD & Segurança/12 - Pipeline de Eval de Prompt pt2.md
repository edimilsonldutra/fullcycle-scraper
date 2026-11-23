Módulo: DevOps e SRE com IA\
Aula: [Pipeline de Eval de Prompt pt2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18508)

## Resumo da aula



## Transcrição

00:00

Ok, ok, é foi. Agora ele está fazendo aqui a parte da avaliação mesmo.

00:06

Se vocês notarem aqui dentro do nosso LLM Studio,

00:09

ele está chamando várias LLMs aqui para fazer essa avaliação.

00:15

Então vamos esperar ele terminar essa avaliação para me dar o resultado final aqui.

00:22

Basicamente, ele está mandando aqueles inputs, recebendo

00:26

o output com o formato de JSON e vendo se a classificação vai bater com

00:32

o que a gente já sabe a classificação daqueles exemplos que a gente está mandando.

00:38

Então a gente sabe que o exemplo lá,

00:39

a classificação é P1. Se o LLM retornar algo diferente disso,

00:43

aquele prompt parece que está meio zoado ali, não está legal.

00:47

Então a gente consegue avaliar vários casos ali e evitar que um

00:51

prompt seja mudado e pare de atender esses exemplos que a gente colocou.

00:58

Se parar de atender esses exemplos, pode ser um problema.

01:00

Porque pode ser que outras coisas venham e a gente não

01:04

consiga avaliar de maneira mais assertiva a parte de segurança aí.

01:11

Então, aqui a gente viu que, por exemplo, vamos dar um exemplo aqui.

01:17

Vamos pegar o primeiro ali em cima.

01:20

CVE, alguma coisa, X e Utils, Backdoor, Compressor e assim por diante.

01:25

A gente ganhou um pass aqui, um summary, a gente passou esse summary para ele.

01:30

Faz de crítica um potencial RCR remoto.

01:33

A gente conseguiu ver que o ID está aqui e a severidade dele é P1. Legal,

01:38

a gente espera lá no nosso EVOL,

01:40

vamos voltar aqui no nosso EVOL. A gente sumiu a tela, apareceu.

01:45

Aqui no nosso EVOL,

01:46

a gente espera que esse primeiro seja um P1 e que ele inclui a CVE.

01:53

Que aqui a CVE é a circulação desse cara que mostra esse problema,

01:58

né? O circular desse cara que mostra esse problema.

02:00

A gente, nesse segundo aqui,

02:03

a gente espera um P1 e espera que o componente tenha um config .py. Vamos ver lá.

02:09

Ele tem um P1 e aqui tem três pontinhos, porque não mostrou o resto.

02:14

Mas aqui provavelmente como ele passou. Tem um config .py. E assim por diante.

02:19

Então ele vai avaliar cada caso ali e vai me falar se passou ou não passou.

02:23

No nosso caso aqui tem 21 casos que passaram. Ele fez 21 testes aqui. Legal?

02:30

Ele deve estar rodando o resto das pipelines ali. Vamos ver?

02:34

Já terminou de rodar. Já fez a avaliação aqui de segurança.

02:37

Se vocês notarem, a avaliação de segurança aconteceu de maneira...

02:42

normal aqui, conseguiu os resultados do driven, fez a execução e tudo mais. Ok?

02:50

Depois disso, vamos fazer um teste aqui, vamos pegar aqui no nosso código,

02:55

vamos pegar algum cara aqui que vai... Vamos pegar esse primeiro,

03:00

que a gente sabe que ele é uma CVE -P1, e vamos trocar ele,

03:05

imagine que agora ele virou uma CVE -P3, ou melhor.

03:10

Vamos mudar aqui embaixo. Vamos mudar o prompt.

03:15

Vamos mudar alguma coisa aqui no prompt. Vamos ver o que a gente pode mudar.

03:20

Serviços públicos, eu exposto VPN, alguma coisa. Vamos...

03:29

P1 é crítico, P2 é high, P3 é isso aqui.

03:35

Severidade P1, P2, P3.

03:39

Componente afetado, recomendação.

03:43

Deixa eu ver o que a gente pode mudar aqui.

03:46

Ok, a gente pode mudar o seguinte.

03:49

Vamos remover esse P1 aqui.

03:53

Removei o nosso System Prompt.

03:56

Removei o P1 aqui. Então, isso aqui pode ser um problema.

03:59

Alguém foi lá e removeu esse P1. Legal?

04:03

Então, vamos fazer aqui um novo git add ponto.

04:07

Um novo git commit.

04:11

E no fim aqui, a gente vai fazer o git push.

04:14

Quando a gente faz isso, a gente vai atualizar lá o pull request.

04:18

Deixa eu pegar aqui o pull request.

04:23

Atualizou o pull request, ele vai subir mais duas novas pipelines aqui.

04:27

Uma de prompt e eval.

04:29

Vamos ver se ele está rodando. Não, não está rodando não.

04:31

O de segurança começou a rodar primeiro.

04:33

A pipeline de segurança aqui. Então eu vou dar um pause aqui,

04:37

esperar essa pipeline rodar e já volto com vocês em seguida.

04:43

Ok, voltando aqui,

04:45

a pipeline de segurança terminou de rodar e agora a

04:48

gente já está rodando a pipeline de EVOL aqui de novo.

04:52

Lembrando que a gente tirou lá da pipeline,

04:55

lá do prompt, a gente tirou o P1. Então, em teoria,

04:59

quando ele fizer aqui os casos de teste, ele não vai conseguir classificar mais.

05:05

Se a gente tirou, ele vai dar algumas falhas aqui na classificação,

05:09

porque a IA não vai ter essa informação

05:12

lá mais no sistema para fazer a classificação correta.

05:16

Vamos ver se ele está rodando aqui. Está rodando,

05:19

está fazendo as chamadas aqui dentro do nosso LM Studio.

05:22

A gente consegue ver as chamadas sendo feitas aqui.

05:25

Vamos esperar um pouquinho para ele dar essa classificação

05:27

para a gente validar se de fato

05:30

aquela mudança que a gente fez no prompt pode

05:31

interferir em alguma coisa aqui no nosso retorno.

05:36

Vou guardar uns minutinhos aqui.

05:39

Ok, está processando. Vamos ver ele processando aqui enquanto isso.

05:52

Ok, já foram 16, tá?

05:54

16 testes e completou. Agora a gente teve alguns problemas aqui.

06:00

Vamos ver o

06:04

que a gente teve. Aqui, teve uma falha. Ele conseguiu achar uma falha aqui.

06:10

Vamos dar um CTRL F aqui. E achar esse fail.

06:13

Aqui ele classificou como P1 ainda.

06:19

Sim, ele classificou como P1. Mas tudo bem.

06:22

Provavelmente tem outras referências de P1 dentro do prompt.

06:27

Então ele conseguiu ainda classificar.

06:29

Se ele tirar as referências, ele vai dar algum problema.

06:32

Mas agora a gente teve uma falha.

06:33

A gente teve uma falha aqui que é o summary, variabilidade etc.

06:38

A gente passou isso aqui e ele agora conseguiu ter essa falha,

06:42

conseguiu gerar essa falha aqui,

06:44

o que atrapalhou os nossos testes e parou aqui o nosso processo. Então,

06:49

esse cara a gente vai conseguir fazer avaliações de mudanças de prompt que podem...

06:57

de processos, de agentes que a gente usa, que podem vir a gerar falha,

07:03

talvez de segurança, que é o nosso caso.

07:04

Que a gente tem um prompt de um agent de segurança, que se ele for alterado,

07:09

a gente pode ter problemas aqui na nossa pipeline de security agent,

07:13

que faz a avaliação da saída do SonarQube,

07:19

mais o Trivy lá. Então a gente pode ter esses probleminhas aí.

07:24

Vamos voltar ao prompt original aqui.

07:28

Então, a intenção é a seguinte, aqui está tudo dentro do mesmo projeto,

07:32

mas se for o caso,

07:34

talvez faça sentido criar um repositório mesmo de prompts,

07:41

e esse repositório vai ser usado para versionar todos os prompts que você tem,

07:47

de todos os entes que você tem no seu ambiente.

07:51

Então você cria o prompt,

07:53

cria as avaliações para ele e cria a configuração do prompt full para ele.

07:59

Toda vez que ele for alterado,

08:01

a gente vai conseguir ver essa alteração e se

08:05

os casos de teste que passarem por ele falharem,

08:10

a gente vai ver que aquele prompt foi alterado para uma coisa pior do que estava.

08:16

Então o prompt tem sempre que evoluir. Então,

08:18

é sempre bom a gente versionar ele ali no Git para que, se der algum problema,

08:22

a gente consiga fazer um rollback rápido e a gente consiga fazer tudo isso.

08:26

Legal, pessoal? Então, essa foi a parte aqui de prompt.

08:29

A intenção aqui é mostrar para vocês que a gente consegue

08:32

colocar também o versionamento de prompt através do Git. Então,

08:37

a gente consegue versionar,

08:38

administrar todos os prompts dos nossos agents e sistemas

08:43

que a gente usa com o Directive AI.

08:45

E dentro do Git a gente consegue acionar pipelines para validar se

08:50

essas mudanças dentro dos prompts fazem sentido para os nossos casos aqui. Então,

08:58

basicamente a gente conseguiu, no final, construir as três pipelines,

09:03

três workflows aqui.

09:05

Um de deploy de pipeline, o outro que é o deploy da security pipeline,

09:11

onde a gente avalia o retorno do SonarQube mais o Trivy,

09:15

com o agent de AI e um que a gente vai avaliar o prompt daquele agent de AI.

09:22

Então a gente consegue avaliar de ponta a ponta

09:25

toda a parte de segurança do nosso ambiente,

09:29

tudo de maneira automatizada usando o GitHub Actions. Legal?

09:35

Isso a gente consegue ver o poder de uso do GitHub Actions.

09:39

E a gente pode fazer orquestrações de vários serviços,

09:43

porque a gente tem várias possibilidades de serviços

09:46

aí que podem ser integrados com GitHub Actions, ok?

09:53

Então, o que fizemos aqui hoje, né?

09:56

A gente gerou uma pipeline de deploy via prompt, validamos com o ActionLint,

10:01

construímos os agents de segurança, que vão priorizar por brush arrays ali,

10:06

que basicamente é o P1, P2, P3,

10:09

que a gente consegue priorizar quais são

10:11

as falhas críticas que têm naquele código, ok?

10:17

A gente mapeou aqui os ataques to play chain e mitigações para esses ataques.

10:22

Implementamos um Evolgate aqui,

10:24

que faz a avaliação dos prompts dos nossos agents de maneira

10:30

automatizada e de maneira que a gente consegue versionar esses prompts.

10:35

E criamos, no final, essas três pipelines.

10:39

que elas se complementam aí. Então a primeira faz o deploy,

10:42

a segunda avalia a segurança daquele deploy, se de fato aquele código é seguro,

10:47

se aquelas lips não têm nenhuma possibilidade de ataque e assim por diante.

10:50

E o último vai avaliar o agent que faz a avaliação da segurança.

10:58

Avaliar o agent não, né? Avaliar o prompt do agent que faz a avaliação de segurança,

11:03

fazendo testes em cima deles, que é justamente o LLM as the Doodle.

11:08

que é um modelo LLM

11:10

avaliando prompts de outros modelos,

11:16

de outros agents. Então,

11:19

é exatamente isso que a gente conseguiu fazer aqui,

11:21

tudo via pipeline, tudo via um workflow automatizado. Combinado?

11:26

Então, aqui a gente está encerrando o módulo 2.

11:30

Espero que vocês tenham gostado do conteúdo, espero que seja proveitoso para vocês.

11:36

E no próximo módulo,

11:37

a gente vai falar um pouco mais de observabilidade com Generative AI.

11:41

Então a gente vai falar um pouco de SLI e SLO com a ajuda de AI.

11:45

A gente vai falar do For Golden Sinners,

11:49

que é um dos mantras de SRE e DevOps.

11:55

Vamos fazer uma instrumentação usando OpenTelemetry via Prompt.

12:01

Então a gente vai usar via AI,

12:03

a gente vai construir toda a parte de instrumentação do nosso serviço.

12:07

Usamos as principais ferramentas do mercado,

12:09

utilizando as principais ferramentas do mercado,

12:12

que é Prometheus, Grafana, Loki,

12:15

Lake Fuse para avaliação de modelos,

12:20

para a gente conseguir ver os prompts que estão chegando,

12:23

avaliar também o que está vindo,

12:25

etc. E fazer o troubleshooting da nossa aplicação, usando linguagem natural. Então,

12:31

a gente pode conversar com os nossos deploys, conversar com os serviços nossos,

12:36

usando linguagem natural, com o MCP. Então,

12:40

o MCP vai ser o braço que vai buscar as

12:43

informações de dentro dos servidores para trazer para a gente,

12:47

para a gente usar AI com base nas informações que o MCP retornar.

12:54

Então, pessoal, é isso. Nos vemos aí no módulo 3.

12:57

Espero que vocês tenham curtido. Um abraço e até a próxima.

## Resumo IA

[RESUMO_IA]