Módulo: Arquitetura na Era da IA\
Aula: [O problema de operar sistemas com IA](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18748)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem? No módulo anterior a gente fechou a parte de RAG,

00:05

a gente construiu um pipeline bem completo, com gestão,

00:08

chunks, metadados, query planner, re-ranking e etc.

00:12

Agora a gente vai dar um passo importante,

00:16

entender como que a gente opera tudo isso em produção.

00:20

Porque uma coisa é fazer a aplicação funcionar.

00:23

Outra coisa é saber o que está acontecendo quando ela está rodando de verdade.

00:27

Em sistemas tradicionais, quando a gente fala de operação,

00:31

normalmente olhamos para coisas como erro 500, tempo de resposta,

00:35

consumo de CPU, memória, logs, chamada ao banco de dados, filas,

00:41

APIs externas e assim por diante. E isso continua existindo.

00:45

A IA não remove nada disso. Só que ela adiciona uma nova camada de incerteza.

00:52

Agora, uma requisição pode responder com status 200 e ainda assim... ter dado problema.

00:59

Ela pode ter custado caro demais, pode ter demorado mais,

01:03

pode ter usado o modelo errado, ou consumido o token demais.

01:08

A gente pode ter recuperado o contexto errado no RAG,

01:11

a gente pode ter chamado um re-ranker sem nenhuma necessidade. Ou seja,

01:16

a gente pode até inclusive ter recusado quando ela deveria responder alguma coisa.

01:23

E no final das contas... ter respondido com uma confiança,

01:26

mas sem evidência suficiente.

01:29

Então, o problema, ele muda. Não basta perguntar,

01:33

a API respondeu, e a pergunta passa a ser,

01:36

como ela respondeu? Qual modelo foi usado?

01:40

Quantos tokens entraram? Quantos tokens saíram?

01:43

Quanto custou aquela chamada? Qual foi a latência da geração?

01:46

Teve cache hit? Teve fallback?

01:49

Reg foi usado? Quantos chunks foram recuperados?

01:52

Quantos entraram no contexto final? A resposta teve fonte.

01:56

Então, se você começa a perceber,

01:59

a operação da aplicação começa a se misturar com

02:04

a qualidade da experiência e com o custo do negócio.

02:08

E esse é o ponto central desse módulo.

02:11

Quando colocamos a IA dentro de uma aplicação,

02:14

a observabilidade deixa de ser apenas uma preocupação de infraestrutura,

02:18

ela vira, na realidade... Parte da arquitetura da solução. Se você não observa bem,

02:25

você não consegue responder perguntas simples. Por exemplo,

02:28

qual feature está consumindo mais tokens?

02:30

Qual tenant está gerando mais custo? Qual modelo está mais lento?

02:34

Qual query planner está pedindo esclarecimento demais?

02:39

O reg está retornando chunks ruins?

02:42

Então, o que acontece é o seguinte. Isso aí são sinais.

02:47

que a aplicação acaba virando uma espécie de uma caixa preta.

02:52

E quando a aplicação com IA vira uma caixa preta,

02:55

o time começa a tomar decisões no escuro.

02:59

Troca de modelo sem saber se o problema era retrieval.

03:02

Aumenta o top case sem saber se o problema era chunking.

03:05

Ele diminui o custo sem saber qual feature está gastando.

03:08

Muda o prompt sem saber se o prompt era realmente o gargalo.

03:12

Então a observabilidade...

03:14

Ela serve justamente para evitar isso. Só que aqui a gente precisa tomar cuidado.

03:20

Observar não significa simplesmente logar tudo. Em aplicações com IA,

03:25

logar tudo pode ser perigoso. O prompt pode ter dado sensível,

03:29

por exemplo. Um contexto de um RAG pode conter informação interna. Então,

03:34

as respostas, inclusive, às vezes têm dados ali do usuário.

03:40

A gente tem que tomar muito cuidado com essa parte de informação privada.

03:44

Então, no final das contas,

03:45

o desafio acaba sendo duplo. De um lado, a gente precisa enxergar, por exemplo,

03:49

um pipeline. De outro lado,

03:51

a gente tem que conseguir controlar o que

03:54

é enviado para as ferramentas de observabilidade.

03:57

E isso sim... envolve, no final das contas, a arquitetura.

04:02

A aplicação precisa decidir quais dados vão para os logs,

04:05

quais viram atributos de trace,

04:07

quais ficam só ali em ambiente de desenvolvimento, quais precisam ser mascarados,

04:13

quais podem ser agregados e quais nunca devem sair ali do runtime.

04:18

Então, ao longo desse módulo,

04:20

a gente vai organizar isso em algumas camadas. Primeiro,

04:23

a gente vai revisar fundamentos de observabilidade, logs, métricas, traces e spans.

04:29

Depois, a gente vai falar sobre OpenTelemetry, não como uma ferramenta final,

04:33

mas como um padrão para instrumentar e transportar a telemetria. Em seguida,

04:39

a gente vai usar uma ferramenta real para visualizar o

04:43

que está acontecendo no nosso pipeline de IA, por exemplo.

04:46

A ideia é olhar para o nosso projeto,

04:49

e a gente vai usar ali como exemplo o nosso de RAG,

04:51

e transformar aquele fluxo em algo observável. Então,

04:55

a gente quer enxergar as etapas como query plane,

04:58

retrieval, re-ranking e answer generation, por exemplo.

05:04

Então a gente quer ver o tempo de tokens, o modelo, o custo estimado,

05:08

as fontes, a quantidade de chunks e decisões que são tomadas ali pelo pipeline.

05:13

E depois a gente vai ampliar um pouco a discussão para mercado,

05:16

porque a gente tem ferramentas e empresas como Datadog, New Relic, AWS,

05:22

o Google Cloud, a Azure, a gente tem o Phoenix,

05:25

a gente tem o Langsmith e outras ferramentas. Então, não dá para só decorar nomes,

05:30

mas a gente precisa entender um pouquinho onde cada

05:32

tipo de solução entra numa arquitetura real.

05:35

Então, nesse primeiro vídeo, guarda essa ideia. Em sistemas com IA,

05:39

observabilidade não é só saber se o sistema está no ar.

05:43

Conseguir reconstruir o comportamento da aplicação,

05:46

entender custo, latência, contexto, modelo, resposta,

05:49

e tudo isso é decisão arquitetural. Então,

05:53

se a gente não consegue observar, a gente não consegue operar.

05:56

E se a gente não consegue operar,

05:58

a gente não consegue confiar no sistema ali em produção.

## Resumo IA

[RESUMO_IA]