Módulo: DevOps e SRE com IA\
Aula: [Demo Prática pt2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18544)

## Resumo da aula



## Transcrição

00:00

Enquanto ele processa aqui,

00:02

eu vou dar um pause no vídeo aqui para a gente

00:05

não ficar olhando para essa tela o tempo todo. Ó, já começou inclusive.

00:09

Vou injetar a falha do tipo ONQ no deploy API e simular o esgotamento de memória.

00:15

Vamos ver. Olha lá, falha injetada com sucesso. Acabou de injetar a falha lá dentro.

00:20

Agora ele está verificando o status do deploy.

00:23

Então ele já está fazendo isso para mim. Perfeito, foi aplicada. Então...

00:29

Tool Investigate Pod. Então ele está investigando o pod ali.

00:33

Vou verificar os eventos do MSpace e descrever o deployment para o estado atual.

00:38

Então ele injetou a falha e agora ele já está fazendo algumas

00:40

descrições aqui do que está acontecendo

00:44

lá dentro do nosso cluster nesse momento.

00:48

Ok? Vou criar um evento no calendário para

00:51

registrar aqui esse incidente de demonstração. Olha que legal.

00:54

O próprio OpenABY decidiu usar o próprio calendário dele.

00:59

para inserir um evento de demonstração. Que legal isso aqui.

01:04

Você pode pedir para ele guardar aqui dentro do calendário o que aconteceu.

01:08

Então se a gente vier aqui em calendário, no cantinho,

01:10

aqui ó, o nosso evento aqui, na data de hoje.

01:16

Como que a gente consegue ver?

01:19

Aqui ó, SRE Health Check.

01:23

Na verdade, hoje é dia 17. Hoje é dia 17.

01:28

Então a gente tem aqui um evento no calendário, ele registrou no dia 18,

01:35

era para registrar no dia 17, mas tudo bem, aqui ó, Medium OmniQ.

01:39

Mas ele registrou aqui, que é aquele chat que a gente está falando lá agora,

01:45

não é aquele chat na verdade, esse chat que a gente está falando aqui,

01:48

ele registrou Medium OmniQ IPPI 2026 .06 .18. Não sei te falar,

01:55

não sei falar para vocês, mas ele... Achou que hoje era dia 18,

01:58

mas hoje é dia 17. Mas tudo bem. A gente sabe que ele tem essa possibilidade.

02:01

Ele consegue inserir aqui no calendário o problema. Está vendo?

02:06

Inclusive, ele consegue até mostrar para você o que aconteceu,

02:09

algumas coisas do incidente, descrição.

02:12

A gente consegue ver isso aqui tudo no calendário. Legal?

02:15

Ah, é porque está em UTC.

02:18

Explicado. Nós somos 9 horas agora. Então, em teoria,

02:21

é meia -noite. Então, ele registrou como 2026 -06.

02:26

18, porque já passou de meia -noite no ambiente do servidor.

02:30

Mas não tem problema, tá? Ele tá achando que hoje é amanhã.

02:34

Por causa que ele tá no horário de UTC e não UTC -3, que é o horário do Brasil.

02:39

Tá bom? Então ele já registrou todo esse calendário aqui certinho pra gente.

02:45

Vamos voltar aqui pro nosso chat e ver o que ele disse.

02:51

Simulação, falta injetada. Ele injetou, lembra que o...

02:58

O pod afetado foi esse. Aqui está o status dele.

03:01

O ACID code 137, onde o container está reiniciando em loop.

03:05

O deploy status tem dois de três pods disponíveis. Então,

03:10

os dois pods que estavam lá, eles não morreram.

03:14

Mas tem um lá com problema. Esse terceiro pod aqui,

03:18

que ele injetou o erro para a gente. Ok?

03:22

Agora a gente consegue ver que ele tá acontecendo esse loop backoff aqui agora, tá bom?

03:28

Que ele tá com crash loop backoff,

03:32

Porque a gente injetou aquele OOMK deles lá, ok?

03:38

Pode OOMK eles, tá? Da state terminate, e este vai ficar assim por diante,

03:43

Ele vai ficar iniciando e terminando,

03:45

Iniciando e terminando com o problema lá.

03:47

Aqui é o evento Kubernetes, comprovamento observado, um evento criado,

03:52

Que é interessante para a gente conseguir colocar um calendário,

03:55

Eu acredito que é possível até compartilhar um calendário,

03:58

E a gente colocar aqui, calendários,

04:00

A gente pode criar um aqui, vamos colocar aqui, teste, criar.

04:06

A gente pode ter a possibilidade de compartilhar esse calendário.

04:10

Só não me recordo aonde aqui.

04:12

Mas a gente consegue colocar aqui um calendário e

04:15

Ir registrando alguns tipos de eventos aqui.

04:17

Legal, isso é bem bacana para a gente conseguir ir acompanhando também

04:20

Através de chat o que está acontecendo no nosso ambiente.

04:24

Então, o próximo passo aqui que a gente vai fazer,

04:29

Eu até sugeri aqui como o próximo passo.

04:31

Mas o próximo passo é diagnosticar via chat.

04:34

Inclusive, ele já diagnosticou para a gente,

04:36

Mas vamos digitar aqui o pedido para diagnóstico para ele, tá? Então, os pods

04:43

Do app-API estão com problemas. Diagnóstico. Diagnóstico. Diagnóstico.

05:01

Verifique o

05:03

Status dos pods.

05:06

Os eventos, os logs e as métricas.

05:14

Consulte a Knowledge Base

05:21

Para

05:35

Book

05:40

Relevante.

05:43

Vamos mandar esse prompt para ele aqui agora.

05:47

E assim que ele processar, que ele vai dar o processamento um pouco mais lento,

05:50

Porque o nosso contexto já está bem grande, eu retomo aqui o vídeo.

05:55

Ok, iniciou aqui o processo.

06:00

Começou a fazer algumas chamadas de tools aqui já.

06:04

Então, agora ele está investigando o pod problemático,

06:07

Para ver detalhes dos logs dele.

06:09

Então, ele já identificou qual é o pod.

06:12

Ele fez um get aqui, já conseguiu pegar os dados certinho lá dentro do Kubernetes.

06:17

Está investigando o pod. Vamos

06:25

Ver o que mais que ele tem.

06:26

Agora, ele está vendo aqui algumas coisas dentro. View, knowledge file.

06:31

Então, ele está olhando algumas coisas aqui dentro do knowledge base.

06:38

Então, ele fez um view, knowledge file aqui.

06:42

Perfeito, encontrou o runbook. Leu o conteúdo completo.

06:45

Então, ele está lendo o conteúdo do lado do nosso runbook.

06:47

Está dando um get top resource consumer.

06:52

Ele está olhando algumas coisas aqui lá dentro do

06:55

Nosso Prometheus, tá?

07:02

Então, aqui ele conseguiu fazer um diagnóstico para a gente, ó. Temos aqui os três pods,

07:06

Tá? Aqui tem a quantidade de restarts que ele fez, tá tudo aqui.

07:11

O problema é identificado.

07:12

Tem um pod que está em crash loop backoff devido a OOMKiller.

07:20

Os eventos mais relevantes para o pod problemático,

07:23

então aqui estão alguns eventos que foram relevantes para ele aqui.

07:29

Os logs, então aqui os logs estão vazios,

07:32

o que indica que foi morto muito rápido, então nem gerou log,

07:37

então nem gera log para a gente, porque o pod ele nasce e morre rapidamente.

07:41

E aqui alguns detalhes técnicos do problema.

07:46

Então, last state terminate, reason, OOM-liquid, exit, untrace set.

07:51

Então a gente tem uns problemas aqui. Problema crítico,

07:53

pode ter um limite de memória de apenas 5 megas,

07:56

enquanto o deploy original deveria ter 512 megas.

08:00

Isso foi confirmado pelo ambiente crash loop inject true.

08:06

A gente tem essa variável lá, que está presente no container.

08:11

Então, aqui algumas métricas de uso, deployment version e assim por diante.

08:15

Aqui o limite de memória detectado, o homepage consultado.

08:19

Segundo o homepage, a Omnicare technology base. A gente tem lá todos os detalhes.

08:23

A gente consegue ver aqui o homepage. Está aqui certinho.

08:28

Sintomas confirmados. Pode estar os mortos Omnicare.

08:31

Contagem de restart está aumentando.

08:34

Prometer os alertas esperados.

08:36

Error rate e pode restart rate behind.

08:41

E essa ali é a violação, disponibilidade pode cair abaixo de 99,9%.

08:48

Então isso aqui é o que a gente pode atingir com esse problema.

08:52

Análise da situação atual, te dá a tua análise completa aqui.

08:56

Recomendação de mitigação, baseada no Runbook.

08:59

Então ele usou o Runbook que a gente criou lá na

09:01

base de conhecimento para fazer a análise da recomendação de mitigação aqui.

09:07

que é basicamente dar um CUP CTL aqui, set resource e assim por diante,

09:11

demo, e trocar os limites dele aqui, ok?

09:14

Então, follow-up após resolver, para a gente verificar,

09:18

o SLO aqui de novo, SLO afetado, e a conclusão. Diagnóstico final,

09:23

o pod tal está com crash devido a um evento de onDQ

09:27

causado por limite de memória de 5 MB para fins de demonstração.

09:32

Então aqui está bem claro que a gente está demonstrando.

09:35

Claro que se fosse uma situação real, não estaria escrito para fim de demonstração.

09:39

Ação necessária.

09:41

Remover fault usando o remove fault.

09:44

Ou ajustar os recursos de deployment para valores adequados.

09:49

Claro que a gente não vai usar o remove fault aqui.

09:52

Vamos pedir para o nosso Kubernetes fazer esse ajuste para a gente.

09:58

Então diagnosticamos.

10:01

Agora a gente vai registrar uma ação aqui.

10:06

Vamos lá. O bug rate é high,

10:08

então a gente sabe que essa é uma situação de high para a gente,

10:13

é um problema que está fora, um serviço que está fora do ar.

10:17

Mesmo que o namespace esteja no demo app,

10:19

força o módulo Copilot aqui a mostrar o fluxo completo da aprovação.

10:24

Vou pedir para o modelo aqui para registrar uma ação como pendente. Então vamos lá.

10:29

Registre a

10:33

Ação de holding start

10:41

Como ação

10:48

Pendente no

10:52

Incidentes MCP.

10:57

Blast radius

11:01

High

11:07

Justificativa.

11:15

OOM Key Liddy com

11:19

Serviço indisponível.

11:24

SLO violado.

11:26

Então nós estamos aqui pedindo para ele fazer um

11:29

Registro aqui para a gente do que aconteceu.

11:32

Vou mandar isso aqui para ele.

## Resumo IA

[RESUMO_IA]