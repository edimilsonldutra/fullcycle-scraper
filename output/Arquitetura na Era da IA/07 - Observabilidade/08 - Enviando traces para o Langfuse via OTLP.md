Módulo: Arquitetura na Era da IA\
Aula: [Enviando traces para o Langfuse via OTLP](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18755)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, agora eu fiz algo diferente, tá? O que eu fiz no final das contas?

00:07

Eu comentei a linha aqui do OpenTelemetry, tá?

00:11

E o que acontece aqui no meio de toda essa história?

00:16

Ao invés de agora a gente mandar a informação para o Jaeger,

00:19

com o endpoint em branco, tá?

00:22

Já está configurado, inclusive, nas variáveis de ambiente.

00:24

Se você for olhar no Docker Compose,

00:26

eu não vou abrir ele agora aqui.

00:29

Para ele enviar o quê? As informações aqui para a porta padrão que é a 3000,

00:33

e aqui eu estou passando a Langfuse Public Secret

00:36

Key para a stack do Langfuse funcionar,

00:39

mas o interessante é que, por padrão, onde a gente tem um set default,

00:44

vamos dizer assim, ele vai mandar todas as informações no formato,

00:48

com os headers, inclusive, padrão,

00:50

que o Langfuse precisa para fazer a parte de autenticação e tudo mais.

00:55

Então, o que isso significa agora? Que quando eu rodar...

00:59

aqui a minha aplicação,

01:01

de cara você já percebe que eu pedi para colocar um localhost 3000,

01:06

api / public / hotel, ou seja,

01:08

aqui é o URL padrão que ele já vai enviar. Os headers,

01:12

eu estou mandando um authorization e também o ingestion version aqui que ele pede.

01:17

O que no final das contas isso quer dizer? Que agora os traces que eu estou fazendo,

01:22

eles vão ser apontados para um outro backend,

01:25

que nesse caso é o Langfuse. Então, quando eu digitar, por exemplo,

01:32

me dê mais detalhes sobre SLA.

01:39

Então, agora a gente vai passar por todo aquele processo,

01:42

onde ele vai fazer o query planner, onde ele vai fazer o re-ranking,

01:45

vai fazer a pergunta de volta,

01:47

vai trazer as informações que eu estou querendo para montar.

01:50

Então, ali é que ele achou os documentos, aqui tem todo o texto que ele colocou,

01:55

e basicamente é isso que a gente tem. Agora, o que acontece?

02:00

Se eu chegar aqui, eu estou no Langfuse, tá?

02:03

E o Langfuse, ele é uma plataforma, assim,

02:06

fantástica, tá? E uma das coisas interessantes,

02:09

é bom que ela é open source, inclusive, tá?

02:12

E ela compete com diversas outras plataformas muito boas também. A gente tem o Phoenix,

02:17

a gente tem, inclusive, ferramentas proprietárias,

02:20

como o Langsmith da vida, tá? Aqui,

02:22

por padrão... foi criado um projeto chamado FCIA Reg,

02:26

se eu vou aqui para o meu projeto,

02:28

você vai começar a perceber aqui que eu tenho sete traces,

02:31

porque eu fui testando, fui mexendo e tudo mais,

02:33

por padrão, ele está trazendo aqui o meu projeto, utilizando aqui o GPT-4.1 Mini,

02:38

é um modelo antigo já no momento que eu estou gravando esse curso, mas tudo bem,

02:41

mostra a quantidade de tokens que foi utilizado, o quanto que eu gastei,

02:46

ele traz os gráficos e tudo mais, tá? Agora,

02:49

uma coisa que é importante é que, se você for nessa parte aqui de tracing,

02:54

olha só que interessante. Quando eu vou aqui em tracing,

02:57

você vai começar a perceber que eu tenho um monte de informação aqui para mim.

03:04

E se você começa a olhar, cada informação dessa acaba sendo,

03:08

No final das contas, um span que acabou acontecendo.

03:12

E toda vez que eu tenho esse ícone aqui de type,

03:15

é porque provavelmente ele fez uma chamada a um modelo.

03:20

Então, isso aí que é uma das coisas importantes para a gente conseguir olhar.

03:25

Se eu vou fazendo os filtros aqui, eu consigo filtrar pelo nome do meu projeto,

03:31

que nesse caso aqui é o AI Pipeline.

03:34

E aqui são as fases que eu consigo testar e etc,

03:38

as tags e tudo mais. Então... Quando eu chego nos meus tracings,

03:44

eu posso inclusive ver aqui como gráficos, linhas e tudo mais,

03:47

eu consigo chegar em um desses caras aqui, por exemplo, no meu pipeline,

03:51

e aqui nesse meu pipeline, deixa eu esconder esse cara aqui,

03:55

deixa eu entrar aqui no meu pipeline aqui.

03:58

Quando eu entro nesse meu pipeline, o que vai acontecer no final das contas?

04:03

Ele mostra o histórico, aqui nesse caso,

04:06

no formato de árvore. Então ele mostra o pipeline,

04:10

nesse caso demorou 11 segundos, a somatória do que gastou foi isso.

04:14

Então ele passou no query planner, um retrieval,

04:16

um re-ranking e o answer generation.

04:19

E aqui ele mostra o tempo que ele demorou em cada uma das etapas.

04:23

Se eu clicar aqui em cada etapa agora,

04:25

ele vai me mostrar. Query planning, o que aconteceu?

04:29

Qual foi o path? Quais são os pontos,

04:32

os atributos que acabaram a gente trabalhando aqui?

04:36

E eu tenho... os dados todos em relação ao que ele trouxe de pipeline,

04:41

quais são os atributos, quais são os atributos de query. Então,

04:44

eu consigo ver os logs que foram enviados no meio de toda essa história.

04:48

Se eu chegar no retrieval, eu tenho a mesma coisa aqui.

04:51

Eu tenho os atributos, eu tenho as informações que foram enviadas, o re-ranking,

04:57

mesma coisa em relação a tudo isso. Agora,

05:00

uma coisa que é interessante é que eu também posso ver isso no formato de timeline.

05:06

Então, quando eu venho para cá, olha só que interessante,

05:09

eu começo a ter exatamente aquela visualização que eu tinha no Jaeger. Então,

05:15

se eu clico aqui em Retrieval,

05:17

eu clico e eu tenho as informações aqui de Retrieval para mim.

05:21

Então, isso aqui que é uma das coisas muito,

05:24

mas muito importantes. Por quê? Porque no final das contas,

05:28

eu tenho nesse caso aqui,

05:30

em uma plataforma grande como o Malang Fuse, uma forma de...

05:34

conseguir, de forma geral, integrar, por exemplo,

05:38

todas as chamadas que estão sendo feitas para os modelos,

05:41

a minha parte de avaliação,

05:45

a minha parte de custos, os meus prompts,

05:48

eu consigo navegar sobre esses montes de recursos.

05:51

Um desses recursos é essa parte de tracing.

05:55

Então, se você perceber,

05:56

eu acho que o grande ponto aqui de

05:58

toda essa nossa explicação sobre observabilidade é...

06:04

quais são, no final das contas,

06:06

as possibilidades que eu tenho para conseguir medir o que

06:10

está acontecendo em cada etapa da minha aplicação.

06:13

E nesse caso, com o OpenTelemetry, nesse exemplo,

06:17

que é o padrão, o protocolo e a ferramenta,

06:20

o kit padrão de desenvolvimento para essa parte de observabilidade,

06:23

você consegue fazer isso com a IA. Ou seja,

06:26

ter isso é quase que obrigatório para você colocar uma

06:30

aplicação em produção para saber de onde está

06:34

a demora, de onde está saindo o dinheiro,

06:36

o que está acontecendo, porque sem isso você começa,

06:39

é como se estivesse pilotando um avião, mas sem nenhum dashboard,

06:44

ou se você fosse dirigir um carro e não saber

06:46

quanto de gasolina ele tem ainda para seguir.

06:48

Então você fica cego.

06:49

Nesse caso, você consegue olhar e entender cada etapa. Beleza?

06:54

Espero que você tenha curtido e até o nosso próximo vídeo.

## Resumo IA

[RESUMO_IA]