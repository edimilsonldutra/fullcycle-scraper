Módulo: DevOps e SRE com IA\
Aula: [Introdução](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18548)

## Resumo da aula



## Transcrição

00:00

Fala pessoal, estou de volta aí para a gente fazer o encerramento da nossa matéria aqui agora.

00:05

A gente vai falar um pouco aí,

00:07

vai dar uma resumida do que a gente viu lá desde o módulo

00:10

1 até aqui o módulo 5 e vamos falar aí dos próximos passos,

00:15

do que a gente vai fazer,

00:16

do que vocês precisam fazer aí para fazer esse desenvolvimento,

00:21

para melhorar as coisas do seu dia a dia de trabalho com o SRE,

00:26

do seu dia a dia de trabalho com o DevOps e assim por diante. Ok?

00:30

Então, nós fizemos lá no início, a gente construiu desde o início, desde o zero,

00:36

uma aplicação que se chamou lá no começo de App API. Legal?

00:41

Bem simples o nome da aplicação aí. Então,

00:44

a gente construiu essa aplicação com FastAPI,

00:46

construímos um Dockerfile para ela, construímos um Kubernetes Manifest.

00:52

Construímos o Runbooks para recuperação de caso de falha dessa aplicação.

01:00

E aplicamos também o Kubernetes Manifest lá dentro para a gente rodar usando o K3D.

01:06

Legal? Isso foi lá no módulo 1. No módulo 2,

01:09

a gente implementou a automação de deploy. Então,

01:11

clicamos na esteira CICD usando o GitHub Actions e criamos alguns

01:17

agentes de segurança e de Prompting Versalink para a gente conseguir

01:22

monitorar o prompt desse agente de segurança nosso.

01:26

Então a gente conseguiu construir isso tudo lá no módulo 2.

01:30

Módulo 3, a gente falou de observabilidade, fizemos a instalação do OpenTelemetry,

01:36

plugamos o OpenTelemetry dentro da nossa App API,

01:40

fizemos a construção...

01:45

Também de Grafana e de outros serviços de observabilidade que a gente tem aí.

01:51

Eu dei alguns exemplos,

01:52

não me aprofundei em todos os serviços,

01:54

porque senão a gente ficaria aqui eternamente,

01:56

ficaria aqui mais de meses falando dessas aplicações,

02:01

porque cada um tem as suas particularidades e as suas finalidades ali.

02:06

E falamos também um pouco de SLI e SLO na módulo 3, ok?

02:12

No módulo 4, a gente criou, fez o build ali,

02:16

de toda a nossa stack de incidentes,

02:19

de observabilidade e de SRE. Então,

02:24

a gente conseguiu entregar na mão de uma pessoa SRE,

02:29

algumas ferramentas que ele pode,

02:31

com chat conversacional, ir fazendo ações ali dentro, com segurança, com governança.

02:39

Com chatops, basicamente, mandando mensagens por chat,

02:43

ele conseguiu administrar toda a infraestrutura para ele.

02:46

E por último, a gente entrou no módulo 5 aqui,

02:49

fizemos algumas demos, mostrei ali como funciona, tivemos alguns probleminhas,

02:54

igual a gente teve no Langfuse, teve uns problemas aqui do agente travar também,

02:59

algumas coisas que eu fui testando ali no meio do caminho,

03:02

que a gente colocou chats separados e deu alguns problemas,

03:04

então isso que é o legal, a gente consegue criar as coisas e ir testando.

03:09

Validando ali o funcionamento de fato dele.

03:11

Então, é isso que eu aconselho vocês. Criem,

03:15

testem bastante, vejam onde estão os pontos de falha,

03:19

e após ver esses pontos de falha, vão fazendo melhorias contínuas.

03:24

Melhore o prompt, melhore as suas ferramentas, os seus MCPs, os seus serviços MCPs.

03:30

Faça as melhorias dentro das plataformas que você tem,

03:33

para você chegar no melhor agent

03:38

o melhor agente possível para atender às necessidades de você,

03:41

da sua equipe, da sua empresa. Ok?

03:45

Então, o recado fica aqui.

03:47

A gente saiu do zero com o

03:49

simples FastAPI e chegou lá em um chatbot,

03:55

um chatops automatizado com várias ferramentas que conseguiam

03:59

tomar ações desde que a gente aprovasse ela.

04:02

Legal? Então, seis... takeaways que a gente fez, que é chatops real,

04:09

então o engenheiro interage com a linguagem natural,

04:13

o modelo traduz a interação e faz as ações do IMCP.

04:16

Governança não é opcional, então a governança sempre vai estar no meio,

04:21

você precisa colocar a governança para caso aconteça alguma coisa, aprovação humana.

04:26

Caso aconteça alguma ação que é pesada,

04:29

que pode gerar problemas, tem que ter aprovação humana.

04:33

A RAG ali com os nossos runbooks,

04:35

que é o nosso passo a passo de como fazer a recuperação do nosso serviço,

04:39

é sempre bom ter esses runbooks documentados para a gente conseguir saber, tipo assim,

04:43

o serviço X caiu, como que eu consigo recuperar esse serviço X.

04:47

Está tudo descrito no nosso runbook.

04:50

A observabilidade, esse é o alicerce nosso,

04:53

porque sem observabilidade você não consegue ver o que está acontecendo.

04:57

Então sempre aplique a observabilidade, a gente falou.

05:00

um módulo todo de observabilidade, igual eu disse,

05:03

a gente não se aprofundou nas ferramentas,

05:05

porque se eu fosse me aprofundar,

05:06

a gente ficaria ali por dias falando daquelas ferramentas,

05:10

entendeu? Das possibilidades dela, tá?

05:13

Então o módulo do 3 deu essa possibilidade de a gente conhecer

05:17

um pouco das ferramentas que a gente tem disponível aí para observabilidade.

05:21

Claro que tem N outras que vocês podem usar, mas a gente conheceu algumas aí,

05:26

pelo menos as open source que estão disponíveis para a gente conseguir usar, legal?

05:30

Copilot verso semi-autônomo,

05:32

então a gente fez escolhas aí de não vamos usar uma coisa 100% autônoma,

05:38

entendeu a diferença do que é um copiloto,

05:42

que você pergunta e ele te responde,

05:45

e o que é uma coisa semi-autônoma que faz as coisas para você.

05:48

Legal? Deixe que você aprove. E um pós-mortem com Blameless.

05:54

É a cultura, você tem que implementar isso aí,

05:56

porque sempre que acontecer um incidente,

05:58

você tem que documentar aquele incidente para gerar conhecimento para toda a

06:01

equipe e aquele conhecimento tem que ser girado através desse pós-mortem.

06:08

Esse conhecimento vai ser girado, vai ser documentado,

06:10

você consegue tirar métricas disso,

06:12

do que aconteceu e assim por diante.

06:14

Legal? E outra coisa, sempre voltem para ler o pós-mortem,

06:19

não só gerem não, dá uma olhada.

06:22

Vê se faz sentido, se aquilo mesmo aconteceu,

06:24

então é sempre interessante você conseguir fazer essa validação.

06:28

Então não confie friamente no que está escrito lá, ok?

06:32

Então, a gente aqui construiu, está escrito, você construiu,

06:37

porque acredito que vocês fizeram essa matéria certinho,

06:40

criaram as coisas aí de acordo com o que a gente foi conversando,

06:43

e a gente construiu aí o nosso agent de SRE, legal? Pessoal,

06:51

Então, eu vou me despedir de vocês aqui.

06:55

Deixa eu abrir a câmera aqui para falar. Eu vou me despedir de vocês aqui.

06:59

Fico agradecido por ter a oportunidade de passar esses conhecimentos para vocês.

07:04

Espero que nos vejamos depois em outras atividades, em outras aulas possíveis.

07:12

Façam os testes, criem os seus serviços.

07:16

Levantem a infraestrutura, seja local, ou seja,

07:19

se você tiver algum dinheiro na nuvem aí,

07:22

tiver algum desconto na nuvem, qualquer nuvem,

07:25

criem a infraestrutura, façam os testes, validem.

07:29

Se você tiver algum playground,

07:32

até dentro da própria empresa de vocês, onde eu trabalho,

07:35

eu tenho essa possibilidade de ter um playground

07:36

para a gente conseguir testar as coisas.

07:38

Então, façam isso. Testem. Criem agents, brinquem com eles.

07:45

Faça ele fazer algumas coisas,

07:46

lembrando que sempre no ambiente de dev, tá?

07:48

Lembrando também sempre com observabilidade, governança e segurança andando junto,

07:53

que é super importante.

07:54

E usem a IA aí para ajudar vocês a construírem isso. Então é isso.

08:01

Novamente, agradeço a oportunidade e espero que vocês gostem da aula.

08:06

Preparei aqui com carinho para vocês,

08:08

para a gente conseguir aprender o máximo possível. E se precisar, tamo aí,

08:14

tá? Um abraço, fico com Deus e até a próxima.

## Resumo IA

[RESUMO_IA]