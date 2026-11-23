Módulo: DevOps e SRE com IA\
Aula: [Observabilidade de Agentes pt3](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18530)

## Resumo da aula



## Transcrição

00:02

Ok, pessoal, temos aqui o OpenWebWire de volta.

00:06

Não sei o que ocorreu aqui, eu precisei reiniciar os pods aqui,

00:10

tanto do próprio OpenWebWire quanto do MCPO.

00:14

Aparentemente travou mesmo, falta de memória, mas memória no sistema, né,

00:19

que está rodando localmente aqui dentro do nosso cluster.

00:21

Mas estamos de volta aqui com ele.

00:24

Vamos fazer o último teste aqui, ver se ele vai aguentar, né. Ah,

00:31

ele me deu a resposta. Então aqui, ó, nem precisava fazer outro teste.

00:35

Ele conseguiu me dar a resposta. Então,

00:37

eu perguntei aqui quais os bots dentro do meu SP de observabilidade.

00:41

Ah não, isso aqui foi a parte de status. A gente quer saber o duration aqui.

00:47

Qual é o valor do duration em milissegundos no meu sistema Web API?

00:50

Então, a gente tem o resultado mediano por segundo.

00:52

A gente consegue fazer o troubleshooting de todo o sistema aqui.

00:55

A análise mediana, aproximadamente 4 a 7 milissegundos.

00:59

que meu sistema está respondendo,

01:02

e faixa observada entre 2 e 7 minutos da maioria dos pontos,

01:05

status e assim por diante.

01:06

Ele consegue te dar uma análise completa

01:08

usando as tools aqui da parte do Prometheus,

01:13

tá? Que faz a consulta aí de tempo e isso assim por diante,

01:17

tá? E aqui no Prometheus a gente tem uma...

01:20

Eu preparei umas queries aqui pra gente olhar,

01:22

que é de milissegundos, tempo que está sendo respondido, etc.

01:27

Então aqui um P99 do meu serviço, tá?

01:32

Served Racial Milliseconds Bucket.

01:35

Então aqui a gente tem um P99,

01:37

a gente consegue ver aqui o tempo em

01:39

milissegundos que o serviço está sendo retornado, tá bom?

01:42

Então essa faixa aqui embaixo são os GETs que a gente está

01:46

fazendo e aqui algumas coisas que estão rodando lá também.

01:50

E assim por diante. A gente consegue ver tudo aqui por dentro do Prometheus,

01:55

tá? Claro que é bom vocês explorarem as queries, como funciona, etc.

02:00

Pra gente ver as coisas aqui internamente.

02:04

Aqui a gente consegue pegar os requests ativos, que estão rodando lá agora,

02:09

tá vendo? Então,

02:10

o próprio OpenTelemetry faz esse envio aqui pro

02:17

Prometheus e a gente consegue ver essas verificações.

02:20

E a gente consegue ver até os erros 500 que dão nos serviços.

02:26

Claro que eu acredito que a gente não teve nenhum erro 500 aqui.

02:28

Então, não achou nada aqui na quantidade de tempo. Vamos colocar aqui mais tempo. Uma hora.

02:35

Uma hora é pouco ainda, né? Mas a gente não teve nenhum erro 500. Então, 5 horas.

02:41

Não conseguimos puxar nada. Então, a gente não teve nenhum erro 500.

02:44

E a gente consegue ver essas partes aqui, tá?

02:50

através dessas chamadas. Chamadas não, né?

02:53

Através lá da observabilidade que a gente preparou lá no começo da aula,

02:57

passando aqui pelo OpenTelemetry e mandando,

03:00

descarregando dentro do Prometheus para a gente conseguir ver essas telas.

03:03

E com a AI a gente consegue coletar no MCPCF do

03:07

Prometheus e entregar todo esse troubleshooting aqui para a gente.

03:10

Ok? E, por último,

03:12

essa última consulta que a gente fez, a gente tem aqui o...

03:17

Quero saber o duration em vídeos seguros do meu sistema API.

03:21

A gente tem aqui a geração, que é o evento,

03:23

que eu fiz a pergunta, e o generation. Aqui ele está como não,

03:26

porque deu uma travada lá no LightGLM,

03:28

mas a gente consegue tentar puxar aqui de novo.

03:31

Vamos tentar puxar de novo. Tomara que não trave, né?

03:34

E vamos ver se ele vai mandar lá para o Power BI.

03:37

Pode acontecer essas falhas, tá, gente? Aqui o ambiente de teste, o ambiente local.

03:42

A máquina acaba que não vai aguentar muita pancadaria aqui.

03:45

Mas em um ambiente um pouco mais parrudo, em nuvem, etc., AWS, Azure, GCP,

03:50

você consegue ter esses recursos com mais abundância e evitar esses travamentos. Vamos ver aqui no tracer.

03:57

Ele já viu o primeiro tracer, que foi a pergunta que eu fiz.

04:00

Então, assim que ele terminar de fazer a resposta, ele vai passar naquele outlet.

04:05

O outlet vai mandar o tracer final, que vai ser a resposta do LLM. Vamos ver.

04:11

Ele aqui já pegou, fazendo aqui algumas queries tool.

04:14

Ele tá pegando alguns dados aqui.

04:18

Query range. A gente consegue ver até a query que ele tá usando,

04:21

tá vendo? Instagram, vamos testar essa query.

04:24

Ele que montou essa query, tá? O próprio LLM que fez a montagem dessa query.

04:28

Ó, conseguiu pegar, tá vendo?

04:32

Instagram quality.

04:34

A gente consegue ver aqui. Dá pra ver até no gráfico aqui também.

04:40

Ó, agora ele conseguiu retornar sem travar.

04:43

Então aqui a gente tem um P50, P90, tudo aqui certinho,

04:47

igual a gente tinha no outro chat lá que respondeu,

04:49

que travou, mas agora a gente tem o tracing disso.

04:53

Isso aqui é todas as tools que ele chamou,

04:55

está tudo aqui descrito, não está formatado,

04:57

podemos entender lá dentro do próprio exporter que a gente criou lá de funções,

05:03

como que a gente pode formatar isso.

05:06

Combinado? Então a gente vê toda a stack aí funcionando de ponta a ponta, pessoal.

05:13

Demos aqui, o roteiro prático, que é implementar e definir SLO,

05:17

subir stack, conversar com cluster,

05:19

a gente conseguiu passar por tudo isso, por todas essas demos que a gente fez,

05:23

tá? Então, sugiro que vocês façam todas elas, montem o ambiente de vocês localmente,

05:30

façam os testes, se vocês não conseguirem rodar o modelo local, vocês podem...

05:36

ter acesso a alguma API paga, assim por diante,

05:38

para vocês conseguirem fazer esse teste,

05:40

ou fazer através lá até do OpenCode lá também,

05:43

tá? O OpenCode você consegue fazer todas as configurações que eu

05:47

fiz usando o modelo deles lá do OpenCode Go.

05:50

Só queria demonstrar para vocês aqui como usar o Light LLA.

05:54

Mas o OpenCode vai fugir muito disso, não.

05:56

Você vai subir sua infraestrutura,

05:57

vai configurar os MCPs e ele vai usar o MCP do mesmo jeito que usou aqui, ok?

06:02

Aqui é um resuminho do módulo 3, então a gente definiu essa linha SLA,

06:08

SLA e derivamos o erro budget com a SQL que a gente criou lá na primeira aula, no primeiro módulo,

06:14

mapeamos aqui o foregain designers,

06:16

que a gente já definiu todos eles aqui nessa aula,

06:19

instrumentamos o nosso serviço API com o OpenTelemetry via prompt,

06:24

a gente criou o serviço todo via prompt ali.

06:27

Exploramos consultas conversacionais com Natural Language,

06:31

que transformou a minha linguagem natural em PromQL.

06:34

Então, esse PromQL aqui basicamente é a linguagem que a gente usa no Prometheus.

06:39

Ele conseguiu traduzir a linguagem natural para fazer um PromQL,

06:43

como se fosse um SQL lá dentro do Prometheus. Ok?

06:46

Conectamos MCP Server, K8s mais Prometheus, tá bom?

06:50

Observando os LLMs aqui com o LinkFuseFilter, mandando os dados para lá.

06:56

com as duas pipelines de trace aqui. Pipeline de inbound, que é a pergunta,

07:00

pipeline de outbound, que é a entrega. Então, no próximo módulo, o que a gente vai falar?

07:04

Workflow de troubleshoot assistido, um agent diagnóstico via MCP,

07:09

então a gente vai criar um agent aqui para diagnosticar problemas na ferramenta.

07:12

A gente vai criar um runbook via RAG,

07:15

então a gente vai subir um banco de dados de vetores para gerar

07:19

a RAG daquele runbook que a gente criou lá na primeira aula.

07:22

A gente vai ter um chatops com copilotos aqui,

07:25

e vão ter os pós-morte emblemas automáticos,

07:28

a gente vai gerar isso de maneira automática, ok? Tudo usando o OpenAI aqui,

07:33

que é essa interface que a gente já subiu. Legal?

07:37

Então, obrigado pessoal, a gente já falou desses estudos aqui,

07:40

nos vemos nas próximas aulas, que a gente vai colocar,

07:43

vamos desenvolver aí, a resposta de incidentes com IA agora,

07:47

usando tudo que a gente já criou até o momento.

07:50

Então, obrigado por terem assistido até agora, e um abraço até o módulo 4.

## Resumo IA

[RESUMO_IA]